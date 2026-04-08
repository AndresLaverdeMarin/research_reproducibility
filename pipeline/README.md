# Reproducibility Pipeline

Agentic AI system that ingests published research papers and extracts structured information needed to assess and reproduce their results.

## Current status

**Agent 1 (Paper Analyst)** is implemented. The NotebookLM client wraps the `notebooklm` skill via subprocess and is fully functional. The Gemini API fallback is stubbed. DOI resolution via CrossRef works.

Future agents (Artefact Retriever, Environment Builder, Execution Runner, Validation Auditor) are not yet implemented. See `agentic_reproducibility_architecture.md` in the project root for the full design.

## How it works

The Paper Analyst takes a notebook reference and optional DOI, then:

1. **Connects** to Google NotebookLM via the `notebooklm` skill (Patchright browser automation with persistent auth)
2. **Queries** NotebookLM with 5 targeted prompts (methodology, datasets, artefacts, figures/tables, parameters) -- responses are source-grounded, so only information in the paper is returned
3. **Resolves** the DOI via CrossRef for metadata enrichment (authors, references, links)
4. **Parses** all responses into a typed `PaperProfile` (Pydantic model)

If NotebookLM is unavailable, it falls back to the Gemini API with the paper PDF attached (not yet implemented).

Every action is logged to an append-only JSON-lines ledger for audit.

**Important:** Papers must be manually uploaded to a NotebookLM notebook via the web UI before the analyst can query them. NotebookLM does not support programmatic file upload.

## Package structure

```
pipeline/
├── pyproject.toml           # uv/pip project metadata and dependencies
├── uv.lock                  # Pinned dependency lockfile
├── __init__.py              # Package metadata (v0.1.0)
├── analyst.py               # Paper Analyst agent -- main entry point
├── schemas.py               # Pydantic models (PaperProfile, Dataset, etc.)
├── ledger.py                # Append-only JSON-lines audit log
├── notebooklm_client.py     # NotebookLM client (wraps notebooklm skill)
└── prompts/
    ├── analyst_queries_v1.md    # 5-query sequence for NotebookLM
    └── analyst_fallback_v1.md   # Consolidated prompt for Gemini API fallback
```

## Environment setup

The pipeline uses [uv](https://docs.astral.sh/uv/) for dependency management. A `uv.lock` lockfile is checked in for reproducible installs.

```bash
cd pipeline/

# Create venv and install dependencies (first time)
uv sync

# Activate the environment
source .venv/bin/activate

# Run from the project root (one directory up)
cd ..
python -c "from pipeline.analyst import extract_profile"
```

To add a dependency:

```bash
cd pipeline/
uv add <package>   # updates pyproject.toml and uv.lock
```

### NotebookLM authentication

The `notebooklm` skill must be installed at `~/.claude/skills/notebooklm/` with authentication set up:

```bash
# Check auth status
python ~/.claude/skills/notebooklm/scripts/run.py auth_manager.py status

# Set up auth (opens browser for Google login)
python ~/.claude/skills/notebooklm/scripts/run.py auth_manager.py setup
```

## Usage

### Step 1: Upload the paper to NotebookLM

Open [notebooklm.google.com](https://notebooklm.google.com), create a notebook, and upload the paper PDF. Copy the notebook URL.

### Step 2: Register the notebook

```python
from pipeline.notebooklm_client import NotebookLMClient

client = NotebookLMClient()
client.connect()

# Register the notebook in the skill's library
client.add_notebook(
    url="https://notebooklm.google.com/notebook/...",
    name="Riehl 2025 Reproducibility",
    description="Meta-analysis of reproducibility in transportation simulation",
    topics=["reproducibility", "transportation", "simulation"],
)

# Or via CLI:
# python ~/.claude/skills/notebooklm/scripts/run.py notebook_manager.py add \
#   --url "https://..." --name "..." --description "..." --topics "..."
```

### Step 3: Extract a paper profile

```python
from pipeline.analyst import extract_profile

# By notebook URL
profile = extract_profile(
    "paper.pdf",
    doi="10.1186/s12544-025-00718-9",
    notebook_url="https://notebooklm.google.com/notebook/...",
)

# Or by notebook ID from the library
profile = extract_profile(
    "paper.pdf",
    doi="10.1186/s12544-025-00718-9",
    notebook_id="riehl-2025-reproducibility",
)

# Or use the skill's active notebook (no URL/ID needed)
profile = extract_profile("paper.pdf", doi="10.1186/s12544-025-00718-9")

print(profile.title)
print(profile.methodology_steps)
print(profile.datasets)
```

### Query NotebookLM directly

```python
from pipeline.notebooklm_client import NotebookLMClient

client = NotebookLMClient()
client.connect()

response = client.query(
    prompt="What datasets are used in this paper?",
    notebook_id="riehl-2025-reproducibility",
)
print(response.text)

client.close()
```

### Resolve DOI metadata only

```python
from pipeline.analyst import resolve_doi

metadata = resolve_doi("10.1186/s12544-025-00718-9")
print(metadata["title"])
print(metadata["authors"])
```

### Manage notebooks

```python
from pipeline.notebooklm_client import NotebookLMClient

client = NotebookLMClient()
client.connect()

# List all registered notebooks
for nb in client.list_notebooks():
    print(f"{nb.id}: {nb.name} -- {nb.description}")

# Get the active notebook
active = client.get_active_notebook()

# Set a notebook as active
client.activate_notebook("riehl-2025-reproducibility")
```

## What is implemented vs stubbed

| Component | Status |
|---|---|
| `PaperProfile` schema (Pydantic) | Implemented |
| `resolve_doi()` via CrossRef | Implemented |
| `Ledger` (append-only log) | Implemented |
| Confidence scoring logic | Implemented |
| Query loading from prompt files | Implemented |
| NotebookLM client (query, library management) | Implemented |
| NotebookLM auth validation | Implemented |
| Gemini API fallback | Stubbed (`NotImplementedError`) |
| Response-to-schema parsing | Stubbed (returns empty profile) |

## Prompt templates

The `prompts/` directory contains versioned prompt files:

- **`analyst_queries_v1.md`** -- Five separate queries sent sequentially to NotebookLM. Each targets one facet of the PaperProfile (methodology, datasets, artefacts, figures/tables, parameters).
- **`analyst_fallback_v1.md`** -- All five queries consolidated into a single prompt with the PaperProfile JSON schema, used when NotebookLM is unavailable.

## Architecture reference

See `agentic_reproducibility_architecture.md` in the project root for the full 5-agent pipeline design, scoring model, state machine, and implementation roadmap.
