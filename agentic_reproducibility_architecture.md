# Agentic AI Architecture for Standardised Research Reproduction

**Version:** 0.3 - Draft
**Date:** 2026-03-19
**Context:** Informed by findings from Riehl, Kouvelas & Makridis (2025) -- only 1.82% of transportation simulation studies provide reproducible repositories, and average repository quality scores 2.5/5.

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Design Principles](#2-design-principles)
3. [System Overview](#3-system-overview)
4. [Python Modules](#4-python-modules)
5. [Agent Definitions](#5-agent-definitions)
6. [Orchestration and Workflow](#6-orchestration-and-workflow)
7. [Reproducibility Scoring Model](#7-reproducibility-scoring-model)
8. [Data Model and Schemas](#8-data-model-and-schemas)
9. [Prompt Engineering](#9-prompt-engineering)
10. [Failure Modes and Fallback Strategies](#10-failure-modes-and-fallback-strategies)
11. [Security and Ethical Considerations](#11-security-and-ethical-considerations)
12. [Implementation Roadmap](#12-implementation-roadmap)
13. [Future: MCP as a Scaling Layer](#13-future-mcp-as-a-scaling-layer)

---

## 1. Problem Statement

Research reproducibility remains critically low across scientific domains. In transportation science alone:

- **1.82%** of simulation studies (2000-2024) provide a repository
- Only **12.46%** of existing repositories reach Level 5 quality (comprehensive code, data, models, licenses, working examples)
- **64%** of researchers cite time constraints as the primary barrier to sharing materials
- No statistically significant citation benefit exists for providing repositories -- removing the incentive

An automated system that can ingest a published paper and systematically attempt to reproduce its results would: (a) audit reproducibility at scale, (b) identify specific failure points, and (c) generate standardised reproducibility reports. The system is implemented as a **Python package** with one module per agent, keeping the architecture simple and accessible to researchers. For future community-scale deployment, the modules can be wrapped as MCP servers (see [Section 13](#13-future-mcp-as-a-scaling-layer)).

---

## 2. Design Principles

| Principle | Rationale |
|---|---|
| **Python-first** | A single Python package with modular components -- no protocol overhead, easy to install and extend |
| **Paper-first** | The input is always a published paper (PDF, DOI, or URL); the system derives everything else |
| **Zero-cost analysis** | The ANALYSE phase uses Google NotebookLM via MCP as the primary backend -- source-grounded, citation-backed, and free. No LLM API budget required |
| **Deterministic audit trail** | Every action, decision, and output is logged to a structured reproducibility ledger |
| **Graceful degradation** | When full reproduction is impossible (missing data, proprietary software), the system produces a partial report quantifying exactly what failed and why |
| **Human-in-the-loop gates** | Critical decisions (running untrusted code, large compute, licensing ambiguity) require human approval |
| **Domain-agnostic core, domain-specific plugins** | The orchestration layer is generic; domain knowledge (transportation, biology, ML) lives in specialised plugin modules |

---

## 3. System Overview

```
+------------------------------------------------------------------+
|                        ORCHESTRATOR                               |
|              (orchestrator.py -- state machine)                    |
+------------------------------------------------------------------+
        |            |            |            |            |
        v            v            v            v            v
  +-----------+ +-----------+ +-----------+ +-----------+ +-----------+
  |  Paper    | | Artefact  | |Environment| |Execution  | |Validation |
  |  Analyst  | | Retriever | |  Builder  | |  Runner   | |  Auditor  |
  +-----------+ +-----------+ +-----------+ +-----------+ +-----------+
  | analyst.py| |retriever.py| |builder.py | | runner.py | |auditor.py |
  +-----------+ +-----------+ +-----------+ +-----------+ +-----------+
        |            |            |            |            |
        v            v            v            v            v
  +-----------+ +-----------+ +-----------+ +-----------+ +-----------+
  | NotebookLM| | Libraries:| | Libraries:| | Libraries:| | Libraries:|
  | MCP server| | GitPython | | docker-py | | subprocess| | scikit-   |
  | (primary) | | requests  | | conda     | | Docker SDK| |  image    |
  |-----------|  | beautifulsoup| pip/uv  | | psutil    | | pandas    |
  | Gemini API| |           | |           | |           | | jinja2    |
  | (fallback)| |           | |           | |           | |           |
  +-----------+ +-----------+ +-----------+ +-----------+ +-----------+
                                    |
                              +------------+
                              | REPRO      |
                              | LEDGER     |
                              | (append-   |
                              |  only log) |
                              +------------+
```

### Package Structure

```
repro_pipeline/
├── __init__.py
├── orchestrator.py       # State machine, human-in-the-loop gates
├── analyst.py            # Paper analysis via NotebookLM MCP (+ Gemini fallback)
├── retriever.py          # Artefact discovery and download
├── builder.py            # Environment construction (Docker)
├── runner.py             # Sandboxed execution
├── auditor.py            # Output comparison and scoring
├── schemas.py            # PaperProfile, ArtefactInventory, ReproducibilityReport
├── ledger.py             # Append-only reproducibility log
├── notebooklm_client.py  # MCP client for NotebookLM server (upload, query, auth)
├── prompts/              # Versioned prompt templates (one per agent)
│   ├── analyst_queries_v1.md   # NotebookLM query sequence
│   ├── analyst_fallback_v1.md  # Gemini API consolidated prompt
│   ├── retriever_v1.md
│   ├── builder_v1.md
│   ├── runner_v1.md
│   └── auditor_v1.md
└── plugins/              # Domain-specific extensions
    ├── transportation.py
    └── ml.py
```

---

## 4. Python Modules

Each capability is implemented as a Python module with well-defined inputs, outputs, and dependencies.

### 4.1 Core Modules

| Module | Key Dependencies | Functions | Purpose |
|---|---|---|---|
| `analyst.py` | notebooklm-mcp, google-genai (fallback), requests | `upload_paper()`, `query_notebooklm()`, `extract_profile()`, `resolve_doi()`, `parse_response_to_schema()` | Source-grounded paper analysis via NotebookLM MCP; falls back to Gemini API |
| `retriever.py` | GitPython, requests, beautifulsoup4 | `clone_repo()`, `download_dataset()`, `check_url_alive()`, `scan_repo_structure()`, `detect_language()`, `find_entry_points()` | Retrieve and analyse code/data repositories |
| `builder.py` | docker-py, subprocess | `create_container()`, `install_dependencies()`, `resolve_conflicts()`, `snapshot_env()`, `detect_requirements()` | Environment construction and dependency resolution |
| `runner.py` | docker-py, subprocess, psutil | `execute_script()`, `run_pipeline()`, `capture_output()`, `enforce_timeout()`, `enforce_resource_limits()` | Isolated code execution with resource controls |
| `auditor.py` | scikit-image, pandas, jinja2 | `compare_figures()`, `compare_tables()`, `compare_statistics()`, `structural_similarity()`, `generate_report()` | Quantitative comparison and report generation |
| `schemas.py` | pydantic | `PaperProfile`, `ArtefactInventory`, `ExecutionResult`, `ReproducibilityReport` | Data validation and serialisation |
| `ledger.py` | json, datetime | `append()`, `read()`, `export()` | Append-only structured log |

### 4.2 Usage Example

```python
from repro_pipeline import orchestrator

# Full automated pipeline
report = orchestrator.run("10.1186/s12544-025-00718-9")

# Or step by step
from repro_pipeline.analyst import upload_paper, extract_profile
from repro_pipeline.retriever import clone_repo, download_dataset
from repro_pipeline.builder import create_container
from repro_pipeline.runner import run_pipeline
from repro_pipeline.auditor import compare_figures, generate_report

profile = extract_profile("paper.pdf")  # uses NotebookLM via MCP
artefacts = clone_repo(profile.repository_links[0])
container = create_container(artefacts)
results = run_pipeline(container, profile.methodology_steps)
report = generate_report(results, profile)
```

### 4.3 Module Communication

Modules communicate through typed dataclasses (defined in `schemas.py`). No serialisation protocol is needed -- objects are passed directly in memory:

```python
# orchestrator.py
profile: PaperProfile = analyst.analyse(paper_path)
inventory: ArtefactInventory = retriever.retrieve(profile)
container_id: str = builder.build(inventory)
results: ExecutionResult = runner.execute(container_id, profile)
report: ReproducibilityReport = auditor.validate(results, profile)
```

---

## 5. Agent Definitions

### 5.1 Paper Analyst Agent

**Module:** `analyst.py`

**Role:** Extract structured, source-grounded information from a research paper sufficient to plan a reproduction attempt.

**Backend (primary):** Google NotebookLM via MCP server -- the paper PDF is uploaded to a NotebookLM notebook, then queried with targeted prompts to extract each `PaperProfile` field. NotebookLM only answers from the uploaded document, which eliminates hallucinated tools, datasets, or methodology steps that the paper never mentioned.

**Backend (fallback):** Gemini API with PDF upload -- used when NotebookLM is unavailable (service outage, auth issues, or batch processing where browser automation is impractical).

**Inputs:** PDF file, DOI, or URL

**Outputs:** A `PaperProfile` object containing:
- Methodology steps (ordered)
- Software/tools mentioned (with versions if stated)
- Datasets referenced (with URLs/identifiers)
- Figures and tables to reproduce (with captions and data descriptions)
- Stated parameters and hyperparameters
- Data availability statements
- Repository links found in text
- Stated hardware requirements

**Decision logic:**
1. Upload paper PDF to NotebookLM via the MCP server (or Gemini API if unavailable)
2. Query for methodology: "List every step of the methodology in order, including software tools and versions"
3. Query for datasets: "List every dataset mentioned, including URLs, availability statements, and sizes"
4. Query for reproducibility artefacts: "List all repository links, code references, and supplementary materials"
5. Query for figures/tables: "For each figure and table, describe the data source and computation that produces it"
6. Resolve DOI via CrossRef to retrieve citing/cited papers and supplementary material links
7. Parse all NotebookLM responses into the `PaperProfile` JSON schema
8. Assign confidence scores per field -- NotebookLM's source citations enable traceability back to specific paper sections

### 5.2 Artefact Retriever Agent

**Module:** `retriever.py`

**Role:** Locate, download, and validate all artefacts (code, data, models, configs) needed for reproduction.

**Inputs:** `PaperProfile` from Paper Analyst

**Outputs:** An `ArtefactInventory` object containing:
- Downloaded repositories (with commit hashes)
- Downloaded datasets (with checksums)
- Missing artefacts with attempted sources
- Licence information per artefact
- File structure analysis (languages, entry points, README quality)

**Decision logic:**
1. For each repository link in `PaperProfile`, verify accessibility and clone
2. For datasets, check institutional repositories (Zenodo, Figshare, Dryad), data journals, and supplementary materials
3. If artefacts are missing, attempt discovery via: paper references, author profiles, Google Dataset Search, Papers With Code
4. Score each artefact against the 5-level repository quality scale from Riehl et al. (2025)
5. Flag licensing conflicts that would prevent reproduction

### 5.3 Environment Builder Agent

**Module:** `builder.py`

**Role:** Construct an isolated, reproducible execution environment from the retrieved artefacts.

**Inputs:** `ArtefactInventory`

**Outputs:** A container image or environment specification, plus a build log

**Decision logic:**
1. Detect language and dependency management (requirements.txt, environment.yml, Pipfile, renv.lock, Makefile, Dockerfile)
2. If explicit dependency files exist, attempt direct installation
3. If not, infer dependencies from import statements and known package registries
4. Resolve version conflicts using constraint solvers
5. Build a Docker/OCI container with pinned dependencies
6. Run smoke tests (import checks, help flags) to verify the environment
7. If build fails, attempt progressive relaxation: pin -> compatible range -> latest

### 5.4 Execution Runner Agent

**Module:** `runner.py`

**Role:** Execute the reproduction pipeline inside the sandboxed environment and capture all outputs.

**Inputs:** Container image, execution plan, `PaperProfile` (for expected outputs)

**Outputs:** An `ExecutionResult` object containing:
- Exit codes per script/step
- stdout/stderr logs
- Generated figures (as images)
- Generated tables (as structured data)
- Generated statistics/metrics
- Resource usage (time, memory, disk)
- Crash reports if applicable

**Decision logic:**
1. Determine execution order from README, Makefile, or pipeline numbering (e.g., `main_pipeline_1` through `main_pipeline_7`)
2. Execute each step sequentially, checking exit codes
3. If a step fails, attempt common fixes: missing file paths, hardcoded absolute paths, missing env vars
4. Capture all file outputs created during execution
5. Enforce resource limits and timeouts (configurable per domain)
6. Log every command and its result to the reproducibility ledger

### 5.5 Validation Auditor Agent

**Module:** `auditor.py`

**Role:** Compare reproduced outputs against published results and generate the final reproducibility report.

**Inputs:** `ExecutionResult`, `PaperProfile` (published figures/tables/statistics)

**Outputs:** A `ReproducibilityReport` containing:
- Per-figure visual similarity scores (SSIM, perceptual hash distance)
- Per-table numerical comparison (relative error, exact match rate)
- Per-statistic comparison (within tolerance bands)
- Overall reproducibility score (0-100)
- Categorised failure analysis
- Recommendations for the authors

**Decision logic:**
1. Match reproduced outputs to published results using captions and file names
2. For figures: compute structural similarity (SSIM) and perceptual hashing; flag if SSIM < 0.85
3. For tables: extract numeric values and compare with configurable tolerance (default: 1% relative error)
4. For statistics: compare p-values, coefficients, R-squared within domain-appropriate bands
5. Classify each result as: Reproduced, Partially Reproduced, Not Reproduced, or Not Attempted
6. Generate a structured JSON report and a human-readable PDF

---

## 6. Orchestration and Workflow

### 6.1 State Machine

```
                    +-------------+
                    |   INTAKE    |
                    | (paper DOI) |
                    +------+------+
                           |
                           v
                    +------+------+
                    |   ANALYSE   |
                    |  (extract)  |
                    +------+------+
                           |
              +------------+------------+
              |                         |
    [NotebookLM via MCP]      [Gemini API fallback]
     analyst.py uploads        analyst.py uploads
     paper and queries         paper to Gemini API
     NotebookLM (free)         (free tier / paid)
              |                         |
              +------------+------------+
                           |
                           v
                    +------+------+
                    |  RETRIEVE   |
                    | (artefacts) |
                    +------+------+
                           |
                 +---------+---------+
                 |                   |
           [artefacts found]   [artefacts missing]
                 |                   |
                 v                   v
          +------+------+    +------+------+
          |    BUILD    |    |   PARTIAL   |
          |   (env)     |    |   REPORT    |
          +------+------+    +-------------+
                 |
          +------+------+
          |   EXECUTE   |
          |  (pipeline) |
          +------+------+
                 |
          +------+------+
          |  VALIDATE   |
          | (compare)   |
          +------+------+
                 |
          +------+------+
          |   REPORT    |
          | (generate)  |
          +-------------+
```

#### ANALYSE Phase: NotebookLM via MCP

The ANALYSE phase uses **Google NotebookLM as the primary backend**, accessed programmatically through an MCP server that handles browser automation and persistent authentication.

**Why NotebookLM over a general-purpose LLM:**

- **Source grounding:** NotebookLM only answers from the uploaded document. When asked "what software tools are used?", it cites the exact passage -- it cannot hallucinate tools, versions, or datasets the paper never mentioned. This is critical for reproducibility, where a single fabricated dependency would derail the entire pipeline.
- **Zero cost:** No API budget required. The entire analysis phase runs for free.
- **Citation-backed:** Every response includes references to specific sections of the paper, which map directly to confidence scores in the `PaperProfile`.

**How it works:**

1. `analyst.py` connects to the NotebookLM MCP server
2. The MCP server uploads the paper PDF to a NotebookLM notebook (browser automation with persistent auth)
3. `analyst.py` sends a sequence of targeted queries (methodology, datasets, tools, figures) via the MCP `query` tool
4. Responses are parsed into the `PaperProfile` JSON schema, with NotebookLM's source citations preserved as confidence metadata
5. DOI resolution (via CrossRef) runs in parallel to enrich the profile with external metadata

**Fallback:** If NotebookLM is unavailable (service outage, auth failure, or batch processing at scale), `analyst.py` falls back to the Gemini API with PDF upload, which uses the same underlying model but without the source-grounding guarantee.

### 6.2 Parallel Execution Opportunities

| Phase | Parallelisable Tasks |
|---|---|
| ANALYSE | Section extraction, reference resolution, author repo search |
| RETRIEVE | Independent dataset downloads, repo cloning |
| EXECUTE | Independent pipeline branches (if DAG-structured) |
| VALIDATE | Per-figure comparison, per-table comparison, per-statistic comparison |

### 6.3 Human-in-the-Loop Gates

| Gate | Trigger Condition | Required Action |
|---|---|---|
| `LICENCE_REVIEW` | Non-OSI licence detected or no licence present | Human confirms permission to proceed |
| `COMPUTE_APPROVAL` | Estimated runtime > 1 hour or GPU required | Human approves resource allocation |
| `CODE_SAFETY` | Untrusted code with network calls, file system writes outside sandbox, or obfuscated logic | Human reviews flagged code sections |
| `AMBIGUITY_RESOLUTION` | Multiple candidate datasets/repos found; paper description insufficient to disambiguate | Human selects correct artefact |

---

## 7. Reproducibility Scoring Model

Adapted and extended from the 5-level scale in Riehl et al. (2025):

### 7.1 Dimension Scores (0-20 each, total 0-100)

| Dimension | Weight | Criteria |
|---|---|---|
| **Artefact Availability** | 20 | Code, data, models, configs all retrievable and accessible |
| **Environment Reproducibility** | 20 | Dependencies resolve, environment builds, no manual intervention needed |
| **Execution Success** | 20 | Pipeline runs to completion without errors |
| **Output Fidelity** | 20 | Reproduced results match published results within tolerance |
| **Documentation Quality** | 20 | README, comments, data dictionaries sufficient for independent reproduction |

### 7.2 Score Interpretation

| Range | Label | Meaning |
|---|---|---|
| 90-100 | Fully Reproducible | Automated reproduction succeeds with high fidelity |
| 70-89 | Largely Reproducible | Minor discrepancies or manual steps required |
| 40-69 | Partially Reproducible | Some results can be reproduced; significant gaps remain |
| 10-39 | Minimally Reproducible | Artefacts exist but execution fails or results diverge |
| 0-9 | Not Reproducible | Insufficient materials for any reproduction attempt |

---

## 8. Data Model and Schemas

### 8.1 PaperProfile

```json
{
  "doi": "10.1186/s12544-025-00718-9",
  "title": "string",
  "authors": ["string"],
  "methodology_steps": [
    {
      "order": 1,
      "description": "string",
      "tools_mentioned": ["Python 3.9", "pandas"],
      "data_inputs": ["article_corpus.csv"],
      "expected_outputs": ["figure_1.png"]
    }
  ],
  "datasets": [
    {
      "name": "string",
      "url": "string | null",
      "description": "string",
      "size_estimate": "string | null",
      "licence": "string | null"
    }
  ],
  "repository_links": ["string"],
  "figures_to_reproduce": [
    {
      "id": "fig_1",
      "caption": "string",
      "type": "bar_chart | line_plot | scatter | heatmap | other",
      "data_source": "string"
    }
  ],
  "tables_to_reproduce": [
    {
      "id": "table_1",
      "caption": "string",
      "columns": ["string"],
      "key_values": {}
    }
  ],
  "hardware_requirements": "string | null",
  "stated_software_versions": {}
}
```

### 8.2 ReproducibilityReport

```json
{
  "paper_doi": "string",
  "timestamp": "ISO-8601",
  "overall_score": 0-100,
  "dimension_scores": {
    "artefact_availability": 0-20,
    "environment_reproducibility": 0-20,
    "execution_success": 0-20,
    "output_fidelity": 0-20,
    "documentation_quality": 0-20
  },
  "per_figure_results": [
    {
      "figure_id": "fig_1",
      "status": "reproduced | partial | failed | not_attempted",
      "ssim_score": 0.0-1.0,
      "notes": "string"
    }
  ],
  "per_table_results": [],
  "execution_log_uri": "string",
  "failure_analysis": [
    {
      "phase": "RETRIEVE | BUILD | EXECUTE | VALIDATE",
      "description": "string",
      "severity": "blocking | degrading | cosmetic",
      "suggested_fix": "string | null"
    }
  ],
  "recommendations": ["string"]
}
```

---

## 9. Prompt Engineering

This section defines the prompt strategies for each agent. Prompts follow a layered structure: **system context** (role + constraints) -> **task framing** (what to do) -> **output schema** (structured response format) -> **chain-of-thought guidance** (reasoning scaffold).

### 9.1 General Prompt Architecture

```
+--------------------------+
|  SYSTEM CONTEXT          |  Role, capabilities, safety constraints, tools available
+--------------------------+
|  DOMAIN KNOWLEDGE        |  Injected from domain-specific plugin (e.g., transportation norms)
+--------------------------+
|  TASK INSTRUCTION        |  What the agent must accomplish in this step
+--------------------------+
|  INPUT DATA              |  Structured data from previous agent (PaperProfile, ArtefactInventory, etc.)
+--------------------------+
|  OUTPUT SCHEMA           |  JSON schema the agent must conform to
+--------------------------+
|  CHAIN-OF-THOUGHT GUIDE  |  Step-by-step reasoning scaffold
+--------------------------+
|  FEW-SHOT EXAMPLES       |  1-3 worked examples (optional, for complex tasks)
+--------------------------+
```

### 9.2 Paper Analyst — NotebookLM Query Sequence

Unlike the other agents, the Paper Analyst does not use a single monolithic prompt. Instead, `analyst.py` sends a **sequence of targeted queries** to NotebookLM via the MCP server. Each query extracts one facet of the `PaperProfile`, and NotebookLM's source-grounded responses ensure that only information present in the paper is returned.

#### Query 1: Methodology Extraction

```
List every step of the research methodology in sequential order.
For each step, state:
- A description of what is done
- Any software tools, libraries, or frameworks used (with version numbers if stated)
- The input data required
- The expected output produced
Only include information explicitly stated in the paper. If a version number
is not mentioned, say "version not stated".
```

#### Query 2: Dataset Inventory

```
List every dataset referenced in this paper. For each dataset, state:
- The dataset name
- The URL or DOI (if provided)
- A description of what it contains
- The approximate size (if stated)
- The licence (if stated)
- Whether it is described as openly available, available upon request,
  or not mentioned
```

#### Query 3: Reproducibility Artefacts

```
List all code repositories, supplementary materials, and external resources
mentioned anywhere in this paper, including in the references, footnotes,
acknowledgements, and data availability statement. Include URLs, GitHub
links, Zenodo DOIs, and institutional repository references.
```

#### Query 4: Figures and Tables

```
For each figure and table in the results section, describe:
- What data it visualises or presents
- What computation or analysis produces it
- What input data is needed to generate it
```

#### Query 5: Parameters and Configuration

```
List all parameters, hyperparameters, configuration values, and
hardware requirements mentioned in this paper. Include numerical
values, ranges, and any stated defaults.
```

#### Response Parsing

Each NotebookLM response is parsed by `analyst.py` into the corresponding `PaperProfile` fields. Source citations from NotebookLM (which reference specific sections of the paper) are mapped to confidence scores:

- Direct quote with section reference: confidence 1.0
- Paraphrased with section reference: confidence 0.8
- Inferred from context: confidence 0.5
- Not found: field set to null

#### Fallback: Gemini API Prompt

When NotebookLM is unavailable, the same queries are bundled into a single prompt sent to the Gemini API with the PDF attached:

```markdown
## Task
You are analysing a research paper for reproducibility. Extract a structured
PaperProfile by answering the following questions using ONLY information
present in the attached paper. If information is not stated, respond with null.

[Query 1-5 concatenated]

## Output Schema
Respond with a valid JSON object conforming to the PaperProfile schema.
```

### 9.3 Artefact Retriever Prompt

```markdown
## System Context
You are a research artefact discovery and retrieval agent. You have access to:
`clone_repo`, `download_dataset`, `check_url_alive`, `scan_repo_structure`,
`detect_language`, `find_entry_points`, `get_author_repos`,
`search_semantic_scholar`.

Constraints:
- Verify every URL before reporting it as accessible
- Record SHA256 checksums for all downloaded files
- Respect rate limits on APIs (Zenodo, GitHub, DataCite)
- Never execute downloaded code during this phase

## Task
Given the PaperProfile below, locate and download all artefacts needed for
reproduction. For each artefact, assess its quality level (1-5 scale).

## Input
{paper_profile}

## Output Schema
Respond with a valid JSON ArtefactInventory.

## Reasoning Steps
1. For each repository_link in the PaperProfile:
   a. Check if the URL is alive
   b. If alive, clone and analyse structure
   c. If dead, search archive.org, GitHub search, and author profiles
2. For each dataset:
   a. If URL provided, attempt download
   b. If "available upon request", mark as UNAVAILABLE_GATED
   c. If no URL, search: Zenodo, Figshare, Dryad, Google Dataset Search,
      Papers With Code, institutional repositories
3. For each software tool:
   a. Verify it exists and note the current latest version
   b. Check if the paper's stated version is still available
4. Assess repository quality using the 5-level scale:
   Level 1: Non-empty
   Level 2: Multiple file types
   Level 3: Basic documentation (README)
   Level 4: Reader-friendly documentation (install instructions)
   Level 5: Comprehensive (code, data, models, licences, examples)
5. Produce a completeness summary: what percentage of required artefacts
   were successfully retrieved?
```

### 9.4 Environment Builder Prompt

```markdown
## System Context
You are an environment construction agent that builds isolated, reproducible
execution environments for scientific code. You have access to:
`create_container`, `install_dependencies`, `resolve_conflicts`,
`snapshot_env`, `detect_requirements`.

Constraints:
- Always pin exact dependency versions in the final environment
- Never install packages with known CVEs above CVSS 7.0 without flagging
- Prefer official package registries (PyPI, CRAN, conda-forge)
- The container must be fully offline-capable after build

## Task
From the ArtefactInventory, construct a container that can execute the
reproduction pipeline.

## Input
{artefact_inventory}

## Reasoning Steps
1. Scan repository for dependency declarations:
   requirements.txt, setup.py, pyproject.toml, environment.yml,
   Pipfile, renv.lock, DESCRIPTION, Makefile, Dockerfile
2. If found: attempt direct installation in a clean base image
3. If not found: parse all source files for import statements; map
   imports to packages using a known import->package mapping
4. Resolve version conflicts:
   a. First attempt: use exact stated versions
   b. Second attempt: use compatible ranges (>=stated, <next_major)
   c. Third attempt: use latest versions with deprecation warnings
5. Install system-level dependencies (GROBID, LaTeX, SUMO, etc.)
6. Run smoke tests:
   - `python -c "import <each_package>"` for Python
   - `Rscript -e "library(<each_package>)"` for R
7. Snapshot the environment (pip freeze / conda list) and store manifest
8. If build fails after all attempts, produce a detailed failure report
   with the specific unresolvable conflicts
```

### 9.5 Execution Runner Prompt

```markdown
## System Context
You are a sandboxed execution agent that runs scientific pipelines and
captures their outputs. You have access to: `execute_script`,
`run_pipeline`, `capture_output`, `enforce_timeout`,
`enforce_resource_limits`.

Safety constraints:
- All execution happens inside an isolated container with no network access
- Maximum runtime: {max_runtime} seconds (default: 3600)
- Maximum memory: {max_memory} MB (default: 8192)
- No writes outside the designated output directory
- If a script attempts to access a path outside the container, log and skip

## Task
Execute the reproduction pipeline and capture all outputs.

## Input
{execution_plan}  <!-- derived from PaperProfile.methodology_steps -->
{container_id}    <!-- from Environment Builder -->

## Reasoning Steps
1. Determine execution order:
   a. If a Makefile or master script exists, use it
   b. If pipeline scripts are numbered (e.g., main_pipeline_1..7), run
      sequentially
   c. If no order is clear, use the order from PaperProfile.methodology_steps
2. Before each step:
   - Log the command to be executed
   - Verify input files exist
3. Execute each step:
   - Capture stdout, stderr, exit code, wall time, peak memory
   - Capture all files created/modified in the output directory
4. If a step fails:
   - Analyse the error message
   - Attempt common fixes:
     * FileNotFoundError: check for hardcoded paths, adjust to relative
     * ModuleNotFoundError: attempt pip install of missing module
     * MemoryError: retry with increased limits (if within bounds)
   - If fix succeeds, re-run; if not, log and continue to next step
5. After all steps complete, inventory all generated outputs:
   - Images (PNG, PDF, SVG)
   - Data files (CSV, JSON, HDF5)
   - Log files
   - Trained models
```

### 9.6 Validation Auditor Prompt

```markdown
## System Context
You are a validation agent that compares reproduced research outputs against
published results. You have access to: `compare_figures`, `compare_tables`,
`compare_statistics`, `structural_similarity`, `numeric_tolerance_check`,
`generate_report`, `score_reproducibility`.

Constraints:
- Use quantitative metrics, not subjective assessments
- Report both absolute and relative differences
- Tolerance bands must be stated explicitly for every comparison
- Never claim "reproduced" without a quantitative justification

## Task
Compare the execution results against the published paper and produce a
ReproducibilityReport.

## Input
{execution_result}
{paper_profile}

## Reasoning Steps
1. Match reproduced outputs to published figures/tables:
   - Use filename patterns, captions, and data descriptions
   - If ambiguous, attempt all plausible matches and report the best
2. For each figure:
   - Extract the reproduced image and the published image
   - Compute SSIM (Structural Similarity Index): threshold >= 0.85
   - Compute perceptual hash distance: threshold <= 10
   - Note visual differences (colour scheme, axis labels, scale)
   - Classify: REPRODUCED (SSIM >= 0.85), PARTIAL (0.5 <= SSIM < 0.85),
     FAILED (SSIM < 0.5)
3. For each table:
   - Extract numeric values from both reproduced and published
   - Compute per-cell relative error: threshold <= 1%
   - Report: percentage of cells within tolerance
4. For each statistic:
   - Compare p-values: within one order of magnitude
   - Compare coefficients: within 5% relative error
   - Compare R-squared: within 0.02 absolute difference
5. Compute dimension scores and overall score
6. For each failure, classify:
   - Root cause: DATA_MISSING | CODE_ERROR | ENV_MISMATCH |
     PARAMETER_UNCLEAR | STOCHASTIC_VARIANCE | HARDWARE_DEPENDENT
   - Severity: BLOCKING | DEGRADING | COSMETIC
7. Generate recommendations for the authors to improve reproducibility
```

### 9.7 Orchestrator Prompt

```markdown
## System Context
You are the orchestration agent coordinating a research reproducibility
pipeline. You manage five specialised agents (Paper Analyst, Artefact
Retriever, Environment Builder, Execution Runner, Validation Auditor)
by calling their Python modules and passing structured data between them.

You maintain a state machine with states: INTAKE, ANALYSE, RETRIEVE,
BUILD, EXECUTE, VALIDATE, REPORT, PARTIAL_REPORT, FAILED.

Constraints:
- Follow the state machine transitions strictly
- Never skip the ANALYSE phase
- Pause at human-in-the-loop gates and wait for approval
- If any phase produces a blocking failure, transition to PARTIAL_REPORT
  rather than halting silently
- Log every state transition to the reproducibility ledger

## Task
Given a paper (DOI, PDF, or URL), orchestrate a complete reproduction
attempt and produce a ReproducibilityReport.

## Reasoning Steps
1. INTAKE: Validate input. If DOI, resolve to PDF. If URL, fetch PDF.
2. ANALYSE: Invoke analyst module (NotebookLM via MCP; Gemini API fallback).
   Review PaperProfile for completeness. If critical fields are null
   (no methodology, no datasets), transition to PARTIAL_REPORT early.
3. RETRIEVE: Invoke retriever module. Check ArtefactInventory.
   If no code and no data retrieved, transition to PARTIAL_REPORT.
   If licence gate triggered, pause for human review.
4. BUILD: Invoke builder module. If environment fails to build after
   all fallback strategies, log failure and transition to PARTIAL_REPORT.
5. EXECUTE: If compute gate triggered, pause for human review.
   Invoke runner module. Log all outputs.
6. VALIDATE: Invoke auditor module. Generate final report.
7. REPORT: Publish ReproducibilityReport. Append to ledger.
```

### 9.8 Prompt Engineering Principles Applied

| Principle | How Applied |
|---|---|
| **Role assignment** | Each agent has an explicit identity and scope ("You are a scientific paper analysis agent...") |
| **Tool grounding** | Every prompt lists the exact tools available, preventing hallucinated tool calls. The Paper Analyst goes further: NotebookLM's source grounding prevents hallucinated paper content |
| **Structured output** | JSON schemas enforce deterministic, parseable responses |
| **Chain-of-thought** | Numbered reasoning steps guide the model through complex multi-step logic |
| **Constraint injection** | Safety rules and boundary conditions are stated before the task, not after |
| **Few-shot examples** | Used for the most ambiguous task (paper analysis) to calibrate extraction depth |
| **Graceful failure paths** | Every prompt includes "if X fails, do Y" logic to prevent silent failures |
| **Confidence scoring** | Agents report certainty levels, enabling the orchestrator to make informed decisions |
| **Separation of concerns** | Each prompt addresses exactly one phase; no prompt tries to do everything |
| **Domain injection via plugins** | Domain knowledge (e.g., transportation norms, biology standards) is loaded from plugin modules, not hardcoded in prompts |

### 9.9 Prompt Versioning and Evaluation

Prompts should be treated as code:

1. **Version control:** Store all prompts in a `prompts/` directory with semantic versioning
2. **Evaluation dataset:** Maintain a set of 20-50 papers with known reproducibility outcomes as a benchmark
3. **Metrics:** Track per-agent accuracy (did Paper Analyst extract all tools mentioned? did Artefact Retriever find the repo?) and end-to-end score correlation with human assessment
4. **A/B testing:** When modifying a prompt, run both versions against the evaluation set and compare
5. **Prompt registry:** A config file maps each agent to its active prompt version, enabling updates without code changes

---

## 10. Failure Modes and Fallback Strategies

| Failure | Likelihood | Impact | Fallback |
|---|---|---|---|
| NotebookLM MCP server unavailable (auth failure, UI change, outage) | Low-Medium | Blocks analysis | Fall back to Gemini API with PDF upload; same queries, less source grounding |
| Paper has no machine-readable methodology | High | Blocks analysis | NotebookLM/Gemini infers steps from prose; flag confidence as low |
| Repository link is dead (404/410) | High (given 1.82% repo rate) | Blocks retrieval | Search Wayback Machine, GitHub search, author profiles |
| Data is "available upon request" | Very High | Blocks execution | Log as `UNAVAILABLE_GATED`; attempt synthetic data if parameters are sufficient |
| Dependencies have conflicting versions | Medium | Blocks build | Progressive relaxation strategy (pin -> range -> latest) |
| Code uses proprietary/licensed software | Medium | Blocks execution | Check for open-source alternatives (e.g., SUMO instead of VISSIM); flag for human |
| Stochastic results differ across runs | Medium | Degrades validation | Run 5x with different seeds; compare distributions rather than point values |
| Paper figures are rasterised at low DPI | Medium | Degrades validation | Use structural comparison rather than pixel-level; increase tolerance thresholds |
| Execution exceeds resource limits | Low | Blocks execution | Scale up (with human approval) or attempt on a subset of data |

---

## 11. Security and Ethical Considerations

### 11.1 Code Safety
- All retrieved code runs inside a sandboxed container with no network access, no host filesystem access, and strict resource limits
- Static analysis (bandit for Python, semgrep) is run on all code before execution; flagged issues require human review
- No credentials or API keys are passed into the sandbox

### 11.2 Data Privacy
- The system never uploads paper content or research data to external services without explicit consent
- All processing happens locally or on controlled infrastructure
- GDPR and copyright considerations: the system processes papers for analysis purposes, not redistribution
- When using NotebookLM for the ANALYSE phase, researchers should be aware that paper content is uploaded to Google's servers; this may not be appropriate for embargoed or confidential manuscripts

### 11.3 Responsible Use
- Reports are descriptive, not punitive -- the goal is to help authors improve, not to publicly shame
- Low reproducibility scores may reflect field norms (e.g., data privacy constraints in medical research) rather than negligence
- Reports include contextual factors (data sensitivity, proprietary tools) alongside scores

---

## 12. Implementation Roadmap

### Phase 1: Core Pipeline (Months 1-3)
- Implement `analyst.py` with NotebookLM MCP integration (upload paper, query sequence, response parsing)
- Implement Gemini API fallback path in `analyst.py`
- Implement `schemas.py` (PaperProfile, ArtefactInventory, ReproducibilityReport as pydantic models)
- Implement `ledger.py` (append-only JSON log)
- Design and test the 5-query sequence for NotebookLM (methodology, datasets, artefacts, figures, parameters)
- Evaluation: test against 10 papers from the Riehl et al. (2025) corpus; compare NotebookLM vs Gemini API extraction accuracy

### Phase 2: Retrieval and Build (Months 3-5)
- Implement `retriever.py` (GitPython, requests, beautifulsoup4)
- Implement `builder.py` (docker-py based)
- Build Artefact Retriever and Environment Builder prompts
- Evaluation: attempt environment construction for 20 repositories from the corpus

### Phase 3: Execution and Validation (Months 5-7)
- Implement `runner.py` (Docker-based sandboxed execution)
- Implement `auditor.py` (scikit-image for SSIM, pandas for table comparison)
- Build Execution Runner and Validation Auditor prompts
- Evaluation: end-to-end reproduction of 5 known-reproducible papers

### Phase 4: Orchestration and Reporting (Months 7-9)
- Implement `orchestrator.py` with full state machine
- Build report generation (jinja2 templates for PDF/HTML output)
- Build web dashboard for report visualisation
- Evaluation: run against 50 papers across multiple domains

### Phase 5: Scale and Community (Months 9-12)
- Domain plugin system (`plugins/` directory with transportation, ML, biology extensions)
- Public API for submission of papers for reproducibility assessment
- Integration with journal submission systems (editorial tool)
- Community benchmark: open evaluation dataset with human-graded reproducibility scores

---

## 13. Future: MCP as a Scaling Layer

The Python-first architecture described above is designed for research teams and single-user workflows. The analyst module already uses MCP to connect to NotebookLM, proving the pattern works. If the system grows into a **community platform** with third-party contributors, the remaining Python modules can also be wrapped as MCP servers to enable:

- **Language-agnostic integration:** Contributors could write domain plugins in R, Julia, or Rust and expose them through the same protocol
- **Distributed execution:** Agents could run on different machines, communicating via MCP over HTTP/SSE
- **Tool discovery:** New capabilities (e.g., a biology-specific metadata resolver) could be registered dynamically without modifying the orchestrator
- **Composability:** External tools (Claude Code, Cursor, custom IDEs) could invoke individual pipeline stages as MCP tools

This migration path is straightforward: each module's public functions become MCP tool definitions, and `schemas.py` dataclasses become MCP resource schemas. The orchestrator switches from direct function calls to `tools/call` messages. No agent logic or prompt engineering changes are required.

Until that scale is needed, the Python package keeps things simple.
