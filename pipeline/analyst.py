"""Paper Analyst agent -- Agent 1 of the reproducibility pipeline.

Extracts structured, source-grounded information from a research paper
sufficient to plan a reproduction attempt.

Primary backend: Google NotebookLM via the notebooklm skill
(free, source-grounded, no hallucination of paper content).
Fallback backend: Gemini API with PDF upload.

Important: Papers must be manually uploaded to a NotebookLM notebook
via the web UI before the analyst can query them. The notebook URL or
ID is then passed to extract_profile().
"""

from __future__ import annotations

import json as _json
import logging
import re
from pathlib import Path
from typing import Any

import requests

from pipeline.ledger import Ledger
from pipeline.notebooklm_client import (
    NotebookLMClient,
    NotebookLMError,
    NotebookLMResponse,
)
from pipeline.schemas import (
    DataAvailability,
    Dataset,
    FigureToReproduce,
    FigureType,
    MethodologyStep,
    PaperProfile,
    TableToReproduce,
)

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

_PROMPTS_DIR = Path(__file__).parent / "prompts"

_QUERY_KEYS = [
    "methodology",
    "datasets",
    "artefacts",
    "figures_tables",
    "parameters",
]


# ---------------------------------------------------------------------------
# Query definitions (loaded from prompts/ at runtime)
# ---------------------------------------------------------------------------

def _load_queries() -> dict[str, str]:
    """Load the NotebookLM query sequence from the prompts file."""
    queries_path = _PROMPTS_DIR / "analyst_queries_v1.md"
    if not queries_path.exists():
        raise FileNotFoundError(f"Analyst queries prompt not found: {queries_path}")

    text = queries_path.read_text()
    queries: dict[str, str] = {}

    for key in _QUERY_KEYS:
        marker = f"## Query: {key}"
        start = text.find(marker)
        if start == -1:
            continue
        # Find the next marker or end of file
        end = len(text)
        for other_key in _QUERY_KEYS:
            other_marker = f"## Query: {other_key}"
            if other_marker == marker:
                continue
            pos = text.find(other_marker, start + 1)
            if pos != -1 and pos < end:
                end = pos
        queries[key] = text[start + len(marker):end].strip()

    return queries


# ---------------------------------------------------------------------------
# Confidence scoring
# ---------------------------------------------------------------------------

def _score_confidence(response: NotebookLMResponse) -> float:
    """Assign a confidence score based on NotebookLM response quality.

    Since the skill returns plain text (no structured citations), we use
    heuristics on the response content:
    - Non-empty substantive answer: 0.8
    - Empty or "not found" response: 0.0
    """
    if not response.text or response.text.strip().lower() in ("not found", "n/a", ""):
        return 0.0
    if response.citations:
        return 1.0
    if response.source_sections:
        return 0.8
    # Substantive text from NotebookLM is inherently source-grounded
    return 0.8


# ---------------------------------------------------------------------------
# DOI resolution via CrossRef
# ---------------------------------------------------------------------------

CROSSREF_API = "https://api.crossref.org/works"


def resolve_doi(doi: str) -> dict[str, Any]:
    """Resolve a DOI via the CrossRef API to retrieve metadata.

    Args:
        doi: A DOI string (e.g. "10.1186/s12544-025-00718-9").

    Returns:
        Dict with title, authors, references, and links. Empty dict on
        failure.
    """
    url = f"{CROSSREF_API}/{doi}"
    headers = {"Accept": "application/json"}

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json().get("message", {})
        return {
            "title": data.get("title", [None])[0],
            "authors": [
                f"{a.get('given', '')} {a.get('family', '')}".strip()
                for a in data.get("author", [])
            ],
            "references": [
                ref.get("DOI") for ref in data.get("reference", []) if ref.get("DOI")
            ],
            "links": [
                link.get("URL")
                for link in data.get("link", [])
                if link.get("URL")
            ],
            "licence": [
                lic.get("URL") for lic in data.get("license", [])
            ],
        }
    except requests.RequestException as exc:
        logger.warning("CrossRef resolution failed for %s: %s", doi, exc)
        return {}


# ---------------------------------------------------------------------------
# NotebookLM-based extraction (primary path)
# ---------------------------------------------------------------------------

def query_notebooklm(
    prompt: str,
    client: NotebookLMClient,
    notebook_url: str | None = None,
    notebook_id: str | None = None,
) -> NotebookLMResponse:
    """Send a single query to a NotebookLM notebook.

    Args:
        prompt: The query text.
        client: A connected NotebookLMClient.
        notebook_url: Direct notebook URL (takes precedence).
        notebook_id: Notebook ID from the skill's library.

    Returns:
        NotebookLMResponse with the answer text.
    """
    return client.query(
        prompt=prompt,
        notebook_url=notebook_url,
        notebook_id=notebook_id,
    )


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

def parse_response_to_schema(
    responses: dict[str, NotebookLMResponse],
    doi_metadata: dict[str, Any] | None = None,
) -> PaperProfile:
    """Parse NotebookLM JSON responses into a PaperProfile.

    Each query prompt asks NotebookLM for strict JSON.  The parsers
    attempt ``json.loads`` first and fall back to lightweight text
    heuristics when the response is not valid JSON.
    """
    raw: dict[str, str] = {}
    for key, resp in responses.items():
        if resp.text:
            raw[key] = resp.text

    profile = PaperProfile(raw_analyst_responses=raw)

    if doi_metadata:
        profile.title = doi_metadata.get("title", "")
        profile.authors = doi_metadata.get("authors", [])

    if "methodology" in raw:
        profile.methodology_steps = _parse_methodology(raw["methodology"])

    if "datasets" in raw:
        profile.datasets = _parse_datasets(raw["datasets"])

    if "artefacts" in raw:
        profile.repository_links = _parse_artefacts(raw["artefacts"])

    if "figures_tables" in raw:
        figs, tbls = _parse_figures_tables(raw["figures_tables"])
        profile.figures_to_reproduce = figs
        profile.tables_to_reproduce = tbls

    if "parameters" in raw:
        hw, sw = _parse_parameters(raw["parameters"])
        profile.hardware_requirements = hw
        profile.stated_software_versions = sw

    return profile


# ---------------------------------------------------------------------------
# JSON extraction helper
# ---------------------------------------------------------------------------

_URL_PATTERN = re.compile(r"https?://[^\s\)\]>\"',]+")


def _clean_nlm_text(text: str) -> str:
    """Strip NotebookLM citation markers, orphan punctuation, and prompts."""
    cleaned = re.sub(r"\n\d+\s*(?:,\s*\n\d+\s*)*(?=\n|$)", "", text)
    cleaned = re.sub(r"\n\s*[.,]\s*(?=\n|$)", "", cleaned)
    cleaned = cleaned.replace("\nmore_horiz\n", "\n").replace("more_horiz", "")
    cleaned = re.sub(r"\nWould you like me to.*$", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r" {2,}", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def _extract_json(text: str) -> Any:
    """Best-effort JSON extraction from a NotebookLM response.

    Tries, in order:
    1. Direct ``json.loads`` on the cleaned text.
    2. Content inside a ``` code fence.
    3. The first ``[…]`` or ``{…}`` substring.

    Returns the parsed object, or ``None`` on failure.
    """
    text = _clean_nlm_text(text)

    # 1 – direct parse
    try:
        return _json.loads(text)
    except (ValueError, _json.JSONDecodeError):
        pass

    # 2 – code-fence
    fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if fence:
        try:
            return _json.loads(fence.group(1))
        except (ValueError, _json.JSONDecodeError):
            pass

    # 3 – outermost [ ] or { }
    for open_ch, close_ch in ("[", "]"), ("{", "}"):
        start = text.find(open_ch)
        if start == -1:
            continue
        end = text.rfind(close_ch)
        if end > start:
            try:
                return _json.loads(text[start : end + 1])
            except (ValueError, _json.JSONDecodeError):
                pass

    return None


def _ensure_list(value: Any) -> list[str]:
    """Coerce a value to ``list[str]``.

    Handles JSON fields that may come back as a string, a list, or None.
    Splits only on semicolons (not commas, which appear inside values
    like "10,000 images").
    """
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if v]
    if isinstance(value, str):
        if not value or value.lower() in ("not stated", "null", "n/a"):
            return []
        # Only split on semicolons — commas are too common inside values
        parts = [s.strip() for s in value.split(";") if s.strip()]
        return parts if parts else [value]
    return [str(value)]


def _null_if_empty(value: Any) -> str | None:
    """Return None for null-ish JSON values, else the string."""
    if value is None:
        return None
    s = str(value).strip()
    if not s or s.lower() in ("null", "not stated", "not mentioned",
                               "not provided", "not available", "n/a"):
        return None
    return s


# ---------------------------------------------------------------------------
# Methodology parser
# ---------------------------------------------------------------------------

def _parse_methodology(text: str) -> list[MethodologyStep]:
    """Parse methodology — expects a JSON array of step objects."""
    data = _extract_json(text)
    if isinstance(data, list) and data:
        steps: list[MethodologyStep] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            steps.append(MethodologyStep(
                order=item.get("step_number", len(steps) + 1),
                description=str(item.get("description", "")),
                tools_mentioned=_ensure_list(item.get("software_tools")),
                data_inputs=_ensure_list(item.get("input_data")),
                expected_outputs=_ensure_list(item.get("expected_output")),
                confidence=0.9,
            ))
        if steps:
            return steps

    # ---- text fallback (legacy free-text responses) -----------------------
    logger.debug("methodology: JSON parse failed, using text fallback")
    text = _clean_nlm_text(text)

    parts = re.split(r"(?=(?:^|\n)\s*Step\s+\d+\s*[:\.])", text, flags=re.IGNORECASE)
    step_blocks = [
        p.strip() for p in parts
        if p.strip() and re.match(r"\s*Step\s+\d+", p.strip(), re.IGNORECASE)
    ]
    if step_blocks:
        steps = []
        for block in step_blocks:
            header = re.match(r"Step\s+(\d+)\s*[:\.]?\s*(.*?)(?:\n|$)", block, re.IGNORECASE)
            if not header:
                continue
            order = int(header.group(1))
            title = header.group(2).strip()
            rest = block[header.end():]
            desc = _extract_text_section(rest, "Description") or rest.split("\n")[0].strip()
            if title:
                desc = f"{title}: {desc}" if desc else title
            steps.append(MethodologyStep(
                order=order,
                description=desc,
                tools_mentioned=_extract_tools_from_text(rest),
                data_inputs=_split_semicolons(_extract_text_section(rest, "Input Data")),
                expected_outputs=_split_semicolons(_extract_text_section(rest, "Expected Output")),
                confidence=0.7,
            ))
        return steps

    items = re.split(r"\n\s*(?:\d+[\.\)]\s+|[-*]\s+)", text)
    return [
        MethodologyStep(order=i, description=it.strip(), confidence=0.5)
        for i, it in enumerate((x for x in items if x.strip()), 1)
    ]


# ---------------------------------------------------------------------------
# Dataset parser
# ---------------------------------------------------------------------------

def _parse_datasets(text: str) -> list[Dataset]:
    """Parse datasets — expects a JSON array of dataset objects."""
    data = _extract_json(text)
    if isinstance(data, list) and data:
        datasets: list[Dataset] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            # Map availability string to DataAvailability enum
            avail_str = str(item.get("availability", "not_mentioned")).lower().strip()
            avail_map = {"open": DataAvailability.OPEN, "upon_request": DataAvailability.UPON_REQUEST}
            availability = avail_map.get(avail_str, DataAvailability.NOT_MENTIONED)

            datasets.append(Dataset(
                name=str(item.get("name", "")),
                url=_null_if_empty(item.get("url")),
                description=str(item.get("description", "")),
                size_estimate=_null_if_empty(item.get("approximate_size")),
                licence=_null_if_empty(item.get("licence")),
                availability=availability,
            ))
        if datasets:
            return datasets

    # ---- text fallback ----------------------------------------------------
    logger.debug("datasets: JSON parse failed, using text fallback")
    text = _clean_nlm_text(text)
    items = re.split(r"\n\s*(?:\d+[\.\)]\s+|[-*]\s+)", text)
    datasets = []
    for item in items:
        item = item.strip()
        if not item or len(item.split("\n")) < 2:
            continue
        name = item.split("\n")[0].strip().rstrip(":.")
        if name.lower().startswith("datasets referenced") or name.startswith("---"):
            continue
        url_m = _URL_PATTERN.search(item)
        datasets.append(Dataset(
            name=name,
            url=url_m.group(0) if url_m else None,
            description=item,
        ))
    return datasets


# ---------------------------------------------------------------------------
# Artefacts parser
# ---------------------------------------------------------------------------

def _parse_artefacts(text: str) -> list[str]:
    """Parse artefacts — expects a JSON object with ``repository_links``."""
    data = _extract_json(text)
    if isinstance(data, dict):
        links = data.get("repository_links", [])
        extras = data.get("supplementary_materials", [])
        return [str(u) for u in (links + extras) if u and str(u).startswith("http")]

    # text fallback
    logger.debug("artefacts: JSON parse failed, using URL extraction fallback")
    return list(dict.fromkeys(_URL_PATTERN.findall(text)))


# ---------------------------------------------------------------------------
# Figures / tables parser
# ---------------------------------------------------------------------------

def _parse_figures_tables(
    text: str,
) -> tuple[list[FigureToReproduce], list[TableToReproduce]]:
    """Parse figures/tables — expects a JSON object with ``figures`` and ``tables`` arrays."""
    data = _extract_json(text)
    if isinstance(data, dict):
        figures: list[FigureToReproduce] = []
        for fig in data.get("figures", []):
            if not isinstance(fig, dict):
                continue
            type_str = str(fig.get("type", "other")).lower().strip()
            try:
                fig_type = FigureType(type_str)
            except ValueError:
                fig_type = FigureType.OTHER
            figures.append(FigureToReproduce(
                id=str(fig.get("id", f"fig_{len(figures) + 1}")),
                caption=str(fig.get("caption", "")),
                type=fig_type,
                data_source=str(fig.get("data_source", "")),
            ))

        tables: list[TableToReproduce] = []
        for tbl in data.get("tables", []):
            if not isinstance(tbl, dict):
                continue
            tables.append(TableToReproduce(
                id=str(tbl.get("id", f"table_{len(tables) + 1}")),
                caption=str(tbl.get("caption", "")),
                columns=_ensure_list(tbl.get("columns")),
                data_source=str(tbl.get("data_source", "")),
            ))

        if figures or tables:
            return figures, tables

    # text fallback — scan for Figure N / Table N references
    logger.debug("figures_tables: JSON parse failed, using text fallback")
    text = _clean_nlm_text(text)
    figures, tables = [], []
    seen: set[str] = set()

    for m in re.finditer(r"(?:Figure|Fig\.?)\s*(\d+[a-z]?)\b", text, re.IGNORECASE):
        fid = f"fig_{m.group(1)}"
        if fid in seen:
            continue
        seen.add(fid)
        line_s = text.rfind("\n", 0, m.start()) + 1
        line_e = text.find("\n", m.end())
        ctx = text[line_s: line_e if line_e != -1 else len(text)].strip()
        figures.append(FigureToReproduce(id=fid, caption=ctx[:300]))

    for m in re.finditer(r"Table\s*(\d+[a-z]?)\b", text, re.IGNORECASE):
        tid = f"table_{m.group(1)}"
        if tid in seen:
            continue
        seen.add(tid)
        line_s = text.rfind("\n", 0, m.start()) + 1
        line_e = text.find("\n", m.end())
        ctx = text[line_s: line_e if line_e != -1 else len(text)].strip()
        tables.append(TableToReproduce(id=tid, caption=ctx[:300]))

    return figures, tables


# ---------------------------------------------------------------------------
# Parameters parser
# ---------------------------------------------------------------------------

def _parse_parameters(text: str) -> tuple[str | None, dict[str, str]]:
    """Parse parameters — expects a JSON object.

    Returns (hardware_requirements, software_versions).
    Hyperparameters are appended to the hardware string so nothing from
    the reply is lost.
    """
    data = _extract_json(text)
    if isinstance(data, dict):
        hw = _null_if_empty(data.get("hardware"))
        sw = {}
        for k, v in (data.get("software_versions") or {}).items():
            sw[str(k)] = str(v)
        # Fold hyperparameters into hardware_requirements so they are kept
        hypers = data.get("hyperparameters")
        if isinstance(hypers, list) and hypers:
            lines = [f"{h.get('name', '?')}: {h.get('value', '?')} ({h.get('context', '')})"
                     for h in hypers if isinstance(h, dict)]
            hp_text = "Hyperparameters: " + "; ".join(lines)
            hw = f"{hw}\n{hp_text}" if hw else hp_text
        return hw, sw

    logger.debug("parameters: JSON parse failed, using text fallback")
    return _clean_nlm_text(text), {}


# ---------------------------------------------------------------------------
# Text-fallback helpers (used only when JSON parsing fails)
# ---------------------------------------------------------------------------

_METHODOLOGY_FIELDS = ["Description", "Input Data", "Expected Output"]


def _extract_text_section(text: str, section_name: str) -> str:
    """Extract ``Section Name: …`` from free-text until the next section."""
    others = [f for f in _METHODOLOGY_FIELDS if f.lower() != section_name.lower()]
    boundary = "|".join(re.escape(h) for h in others)
    pat = re.compile(
        rf"(?:^|\n)\s*{re.escape(section_name)}\s*:\s*(.*?)(?=\n\s*(?:{boundary})\s*:|$)",
        re.IGNORECASE | re.DOTALL,
    )
    m = pat.search(text)
    return m.group(1).strip() if m else ""


_KNOWN_TOOLS = {
    "python", "r", "matlab", "julia", "java", "c++", "fortran",
    "tensorflow", "pytorch", "keras", "caffe", "mxnet", "jax",
    "pandas", "numpy", "scipy", "scikit-learn", "sklearn",
    "matplotlib", "seaborn", "ggplot2", "plotly",
    "adam", "sgd", "rmsprop", "vgg", "resnet", "u-net", "unet",
    "bert", "gpt", "gan", "vae", "ddim", "ddpm",
    "xdog", "sumo", "vissim", "aimsun", "paramics",
    "abaqus", "ansys", "comsol", "openfoam",
}


def _extract_tools_from_text(text: str) -> list[str]:
    """Grep known tool names from free text."""
    found: list[str] = []
    lower = text.lower()
    for tool in sorted(_KNOWN_TOOLS):
        if tool in lower:
            pat = re.compile(rf"\b({re.escape(tool)}(?:[-\s]?\d[\d\.]*)?)\b", re.IGNORECASE)
            m = pat.search(text)
            if m:
                found.append(m.group(1))
    return list(dict.fromkeys(found))


def _split_semicolons(text: str) -> list[str]:
    """Split on semicolons, strip trailing dots."""
    if not text:
        return []
    return [s.strip().rstrip(".") for s in re.split(r";\s*", text) if s.strip()]


# ---------------------------------------------------------------------------
# Extraction configuration
# ---------------------------------------------------------------------------

class AnalystConfig(BaseModel):
    """Configuration for a Paper Analyst extraction run."""

    notebook_url: str = Field(..., description="Direct NotebookLM notebook URL (paper must already be uploaded)")
    doi: str | None = Field(default=None, description="DOI for CrossRef metadata enrichment")
    notebook_id: str | None = Field(default=None, description="Notebook ID from the skill library (alternative to URL)")
    headless: bool = Field(default=True, description="Run browser in headless mode")


# ---------------------------------------------------------------------------
# Main extraction entry point
# ---------------------------------------------------------------------------

def extract_profile(
    config: AnalystConfig,
    ledger: Ledger | None = None,
) -> PaperProfile:
    """Run the full Paper Analyst pipeline on a single paper.

    This is the main entry point for Agent 1. It:
    1. Connects to the NotebookLM notebook via ``notebook_url``
    2. Runs the 5-query sequence to extract structured information
    3. Resolves the DOI via CrossRef for metadata enrichment
    4. Parses all responses into a PaperProfile

    The paper must already be uploaded to the NotebookLM notebook
    at ``config.notebook_url``.

    Args:
        config: Extraction configuration (notebook URL, DOI).
        ledger: Optional Ledger instance for audit logging.

    Returns:
        A populated PaperProfile.
    """
    if ledger is None:
        ledger = Ledger()

    ledger.append("ANALYSE", "start", {
        "notebook_url": config.notebook_url,
        "doi": config.doi,
    })

    # Step 1: Resolve DOI metadata
    doi_metadata = resolve_doi(config.doi) if config.doi else {}

    # Step 2: Connect to NotebookLM (authenticate if session expired)
    queries = _load_queries()
    client = NotebookLMClient(headless=config.headless)
    try:
        client.connect()
    except NotebookLMError:
        logger.info("Session expired, launching interactive login...")
        client.authenticate(headless=False)
        client.connect()

    responses: dict[str, NotebookLMResponse] = {}
    for key in _QUERY_KEYS:
        if key not in queries:
            continue
        logger.info("Running query: %s", key)
        resp = query_notebooklm(
            prompt=queries[key],
            client=client,
            notebook_url=config.notebook_url,
            notebook_id=config.notebook_id,
        )
        responses[key] = resp
        ledger.append(
            "ANALYSE",
            f"query_{key}",
            {"confidence": _score_confidence(resp)},
        )

    client.close()
    profile = parse_response_to_schema(responses, doi_metadata)

    # Step 3: Enrich profile with DOI metadata
    if config.doi:
        profile.doi = config.doi
    if doi_metadata and not profile.title:
        profile.title = doi_metadata.get("title", "")
    if doi_metadata and not profile.authors:
        profile.authors = doi_metadata.get("authors", [])

    ledger.append("ANALYSE", "complete", {"title": profile.title})
    return profile
