"""Gemini + RAG pipeline for reproducibility analysis of a research paper.

Given a single PDF, this module:

1. Uploads the PDF via the Gemini Files API (one source, referenced by handle).
2. Runs five targeted, independent queries adapted from the historical
   ``pipeline/prompts/analyst_queries_v1.md`` prompt suite -- methodology,
   datasets, artefacts, figures_tables, parameters.
3. Asks Gemini to respond with a Pydantic-validated JSON schema for each query,
   with ``temperature=0`` and a system instruction that pins answers to the
   attached document.
4. Merges the five structured responses into a single ``PaperProfile``.

Design notes -- hallucination control
-------------------------------------
- ``response_schema`` forces JSON conformance (no free-form prose to stray).
- ``system_instruction`` explicitly forbids inventing content not in the paper.
- Per-facet queries keep context tight; each answer is about one aspect.
- Every list item carries a ``source_quote`` field so the model must anchor
  its extraction in a literal passage from the PDF. Missing or hallucinated
  quotes become easy to audit against the original text.
- No chunking / embedding layer -- Gemini 2.x handles a whole paper in context.

Environment
-----------
Requires ``google-genai`` (the current Google GenAI SDK) and a valid
``GEMINI_API_KEY`` (or ``GOOGLE_API_KEY``) environment variable.
"""

from __future__ import annotations

import json
import os
from enum import Enum
from pathlib import Path
from typing import Type, TypeVar

from pydantic import BaseModel, Field

from google import genai
from google.genai import types

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

T = TypeVar("T", bound=BaseModel)


# ---------------------------------------------------------------------------
# Pydantic schemas -- adapted from pipeline/schemas.py (commit 9f53a7c) with a
# required ``source_quote`` field added to each extractable item for grounding.
# ---------------------------------------------------------------------------

class FigureType(str, Enum):
    BAR_CHART = "bar_chart"
    LINE_PLOT = "line_plot"
    SCATTER = "scatter"
    HEATMAP = "heatmap"
    IMAGE_COMPARISON = "image_comparison"
    DIAGRAM = "diagram"
    OTHER = "other"


class DataAvailability(str, Enum):
    OPEN = "open"
    UPON_REQUEST = "upon_request"
    NOT_MENTIONED = "not_mentioned"


class MethodologyStep(BaseModel):
    order: int
    description: str
    tools_mentioned: list[str] = Field(default_factory=list)
    data_inputs: list[str] = Field(default_factory=list)
    expected_outputs: list[str] = Field(default_factory=list)
    source_quote: str = Field(
        description="Short literal quote from the paper grounding this step."
    )


class Dataset(BaseModel):
    name: str
    url: str | None = None
    description: str = ""
    size_estimate: str | None = None
    licence: str | None = None
    availability: DataAvailability = DataAvailability.NOT_MENTIONED
    source_quote: str = Field(
        description="Literal quote from the paper mentioning this dataset."
    )


class FigureToReproduce(BaseModel):
    id: str
    caption: str = ""
    type: FigureType = FigureType.OTHER
    data_source: str = ""
    source_quote: str = ""


class TableToReproduce(BaseModel):
    id: str
    caption: str = ""
    columns: list[str] = Field(default_factory=list)
    data_source: str = ""
    source_quote: str = ""


class Hyperparameter(BaseModel):
    name: str
    value: str
    context: str = ""
    source_quote: str = ""


class SoftwareVersion(BaseModel):
    name: str
    version: str


# -- Per-query response containers ------------------------------------------

class MethodologyResponse(BaseModel):
    steps: list[MethodologyStep]


class DatasetsResponse(BaseModel):
    datasets: list[Dataset]


class ArtefactsResponse(BaseModel):
    repository_links: list[str] = Field(default_factory=list)
    supplementary_materials: list[str] = Field(default_factory=list)
    hardware_requirements: str | None = None


class FiguresTablesResponse(BaseModel):
    figures: list[FigureToReproduce] = Field(default_factory=list)
    tables: list[TableToReproduce] = Field(default_factory=list)


class ParametersResponse(BaseModel):
    software_versions: list[SoftwareVersion] = Field(default_factory=list)
    hyperparameters: list[Hyperparameter] = Field(default_factory=list)
    hardware: str | None = None


# -- Final merged output ----------------------------------------------------

class PaperProfile(BaseModel):
    """Structured, source-grounded representation of a research paper."""

    pdf_path: str
    extraction_model: str = ""
    title: str = ""
    authors: list[str] = Field(default_factory=list)
    methodology_steps: list[MethodologyStep] = Field(default_factory=list)
    datasets: list[Dataset] = Field(default_factory=list)
    repository_links: list[str] = Field(default_factory=list)
    supplementary_materials: list[str] = Field(default_factory=list)
    figures_to_reproduce: list[FigureToReproduce] = Field(default_factory=list)
    tables_to_reproduce: list[TableToReproduce] = Field(default_factory=list)
    hyperparameters: list[Hyperparameter] = Field(default_factory=list)
    stated_software_versions: dict[str, str] = Field(default_factory=dict)
    hardware_requirements: str | None = None


class PaperHeader(BaseModel):
    title: str = ""
    authors: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Prompts -- copied verbatim from pipeline/prompts/analyst_queries_v1.md
# (commit 9f53a7c), trimmed so each prompt returns JSON that matches its
# Pydantic schema above.
# ---------------------------------------------------------------------------

SYSTEM_INSTRUCTION = (
    "You are analysing a research paper for reproducibility. "
    "Answer using ONLY information explicitly stated in the attached PDF. "
    "If a fact is not stated, use null / omit it -- do NOT infer, guess, or "
    "draw on outside knowledge. Every item you extract must include a short "
    "literal quote from the paper that grounds it. Respond with valid JSON "
    "conforming to the provided schema; return nothing else."
)

PROMPT_HEADER = (
    "Extract the paper's title and author list. If either is not clearly "
    "printed on the first page, use an empty string or empty list."
)

PROMPT_METHODOLOGY = (
    "List every step of the research methodology in sequential order. "
    "For each step, state: a description of what is done, any software "
    "tools / libraries / frameworks used (with version numbers if stated), "
    "the input data required (data_inputs), and the expected output "
    "produced (expected_outputs). If a version number is not mentioned, "
    "say 'version not stated'. Include a short literal quote "
    "(source_quote) anchoring each step.\n\n"
    "LABEL CONSISTENCY RULES (critical):\n"
    "- Use the SAME label for the same artefact across steps. If step N "
    "  produces an output that feeds step N+1, the string in step N's "
    "  'expected_outputs' MUST appear verbatim in step N+1's "
    "  'data_inputs'. Do not paraphrase, pluralise, or reorder words "
    "  between steps; pick one canonical name per artefact and reuse it.\n"
    "- When a step splits, partitions, or divides data (e.g. train/test "
    "  split, k-fold, train/val/test, stratified sampling), the "
    "  'expected_outputs' MUST list each resulting partition as a "
    "  separate named item (e.g. 'training_set', 'validation_set', "
    "  'test_set' -- use whatever names the paper uses if stated). The "
    "  'description' MUST state the split percentages / proportions / "
    "  fold count exactly as reported in the paper (e.g. '80/20 split', "
    "  '70/15/15', '5-fold cross-validation'). Downstream steps that "
    "  consume a partition MUST reference it by the same name in "
    "  'data_inputs'."
)

PROMPT_DATASETS = (
    "List every dataset referenced in this paper. For each dataset, state: "
    "name, URL or DOI (if provided), description of contents, approximate "
    "size (if stated), licence (if stated), and availability (open, "
    "upon_request, or not_mentioned). Include a short literal quote that "
    "anchors each dataset in the paper."
)

PROMPT_ARTEFACTS = (
    "List all code repositories, supplementary materials, and external "
    "resources mentioned anywhere in this paper -- references, footnotes, "
    "acknowledgements, data availability statement. Include URLs, GitHub "
    "links, Zenodo DOIs, and institutional repository references. Also "
    "state any stated hardware requirements."
)

PROMPT_FIGURES_TABLES = (
    "For each figure and table in the results section, describe what data "
    "it visualises or presents, what computation or analysis produces it, "
    "and what input data is needed to generate it. Include a source_quote "
    "from the caption or surrounding prose."
)

PROMPT_PARAMETERS = (
    "List all parameters, hyperparameters, configuration values, and "
    "hardware requirements mentioned in this paper. Include numerical "
    "values, ranges, and any stated defaults. Return software versions as "
    "a list of objects, each with 'name' and 'version' fields."
)


# ---------------------------------------------------------------------------
# Analyst
# ---------------------------------------------------------------------------

GEMINI_PRICING_USD_PER_MTOK = {
    "gemini-2.5-flash":      {"input": 0.30, "output": 2.50},
    "gemini-2.5-flash-lite": {"input": 0.10, "output": 0.40},
    "gemini-2.5-pro":        {"input": 1.25, "output": 10.00},
    "gemini-2.0-flash":      {"input": 0.10, "output": 0.40},
    "gemini-2.0-flash-lite": {"input": 0.075, "output": 0.30},
}


class GeminiPaperAnalyst:
    """Run Gemini-backed structured extraction on a single PDF."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gemini-2.5-flash",
    ) -> None:
        key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError(
                "Set GEMINI_API_KEY (or GOOGLE_API_KEY) or pass api_key= explicitly."
            )
        self.client = genai.Client(api_key=key)
        self.model = model
        self.usage_log: list[tuple[str, types.GenerateContentResponseUsageMetadata]] = []

    def upload_pdf(self, pdf_path: str | Path) -> types.File:
        """Upload a PDF to the Files API and return its handle."""
        path = Path(pdf_path)
        if not path.is_file():
            raise FileNotFoundError(path)
        return self.client.files.upload(file=str(path))

    def query(
        self,
        file_handle: types.File,
        prompt: str,
        response_schema: Type[T],
        query_name: str = "query",
    ) -> T:
        """Run one structured query against the uploaded PDF."""
        response = self.client.models.generate_content(
            model=self.model,
            contents=[file_handle, prompt],
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0,
            ),
        )
        if response.usage_metadata is not None:
            self.usage_log.append((query_name, response.usage_metadata))
        parsed = getattr(response, "parsed", None)
        if isinstance(parsed, response_schema):
            return parsed
        # Fallback: parse raw text as JSON if ``parsed`` is missing.
        return response_schema.model_validate(json.loads(response.text))

    def usage_summary(self) -> dict:
        """Aggregate tokens + USD estimate over every query since the last analyze()."""
        input_tokens = sum((u.prompt_token_count or 0) for _, u in self.usage_log)
        output_tokens = sum((u.candidates_token_count or 0) for _, u in self.usage_log)
        total_tokens = input_tokens + output_tokens

        rates = GEMINI_PRICING_USD_PER_MTOK.get(self.model)
        if rates is None:
            input_usd = output_usd = total_usd = None
        else:
            input_usd = input_tokens / 1_000_000 * rates["input"]
            output_usd = output_tokens / 1_000_000 * rates["output"]
            total_usd = input_usd + output_usd
        return {
            "model": self.model,
            "calls": len(self.usage_log),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "input_usd": input_usd,
            "output_usd": output_usd,
            "total_usd": total_usd,
            "per_query": [
                {
                    "name": name,
                    "input_tokens": u.prompt_token_count or 0,
                    "output_tokens": u.candidates_token_count or 0,
                }
                for name, u in self.usage_log
            ],
        }

    def analyze(self, pdf_path: str | Path, verbose: bool = True) -> PaperProfile:
        """Run the full five-query pipeline on a PDF and return a PaperProfile."""
        pdf_path = Path(pdf_path)
        self.usage_log = []  # reset per-run usage tracking
        if verbose:
            print(f"Uploading {pdf_path.name} to Gemini Files API...")
        file_handle = self.upload_pdf(pdf_path)

        queries: list[tuple[str, str, Type[BaseModel]]] = [
            ("header", PROMPT_HEADER, PaperHeader),
            ("methodology", PROMPT_METHODOLOGY, MethodologyResponse),
            ("datasets", PROMPT_DATASETS, DatasetsResponse),
            ("artefacts", PROMPT_ARTEFACTS, ArtefactsResponse),
            ("figures_tables", PROMPT_FIGURES_TABLES, FiguresTablesResponse),
            ("parameters", PROMPT_PARAMETERS, ParametersResponse),
        ]

        results: dict[str, BaseModel] = {}
        for name, prompt, schema in queries:
            if verbose:
                print(f"  querying: {name} ...", flush=True)
            results[name] = self.query(file_handle, prompt, schema, query_name=name)

        header: PaperHeader = results["header"]  # type: ignore[assignment]
        methodology: MethodologyResponse = results["methodology"]  # type: ignore[assignment]
        datasets: DatasetsResponse = results["datasets"]  # type: ignore[assignment]
        artefacts: ArtefactsResponse = results["artefacts"]  # type: ignore[assignment]
        figtab: FiguresTablesResponse = results["figures_tables"]  # type: ignore[assignment]
        params: ParametersResponse = results["parameters"]  # type: ignore[assignment]

        return PaperProfile(
            pdf_path=str(pdf_path),
            extraction_model=self.model,
            title=header.title,
            authors=header.authors,
            methodology_steps=methodology.steps,
            datasets=datasets.datasets,
            repository_links=artefacts.repository_links,
            supplementary_materials=artefacts.supplementary_materials,
            figures_to_reproduce=figtab.figures,
            tables_to_reproduce=figtab.tables,
            hyperparameters=params.hyperparameters,
            stated_software_versions={sv.name: sv.version for sv in params.software_versions},
            hardware_requirements=artefacts.hardware_requirements or params.hardware,
        )


def analyze_pdf(
    pdf_path: str | Path,
    api_key: str | None = None,
    model: str = "gemini-2.5-flash",
) -> PaperProfile:
    """Convenience wrapper: one-shot PDF -> PaperProfile."""
    return GeminiPaperAnalyst(api_key=api_key, model=model).analyze(pdf_path)
