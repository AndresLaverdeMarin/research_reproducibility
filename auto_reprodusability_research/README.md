# autoreproducibility

Autonomous pipeline for evaluating the reproducibility of computational research papers. Adapted from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) for a meta-science study on research reproducibility across 14 transportation/energy journals (~46,015 articles).

Part of a NeurIPS 2026 submission with collaborators Michalis (ETH) and Kevin.

## Research Questions

| RQ | Question | Pipeline output |
|----|----------|-----------------|
| RQ1 | How prevalent is code sharing? | Reproducibility level distribution |
| RQ2 | How does it vary across venues? | Journal-level comparison |
| RQ3 | Has it improved over time? | Year-over-year trends |
| RQ4 | What are the barriers? | Failure mode taxonomy |

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
cd auto_reprodusability_research
uv sync
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `markitdown[pdf]` | PDF-to-Markdown conversion for full-text URL extraction (uses pdfminer-six, pypdfium2) |
| `pandas` / `pyarrow` | Article metadata handling (parquet) |
| `requests` | DOI resolution, PDF download, API calls |
| `matplotlib` / `seaborn` | Publication-quality result figures |

## Pipeline Stages

Each article is evaluated through four stages:

1. **Repository Discovery** (2 min) -- Download the paper PDF, convert to Markdown with MarkItDown, and regex-search the full text for repository URLs (GitHub, GitLab, Zenodo, etc.). Falls back to abstract-only search if the PDF is paywalled. Also queries GitHub API and Papers With Code.
2. **Repository Assessment** (3 min) -- Clone the repo and assess documentation, dependency declarations, code completeness, data availability, and last activity.
3. **Lightweight Reproduction** (5 min) -- Install dependencies in an isolated environment and attempt to run the main script. Checks structural runnability, not result reproduction.
4. **Classification** (1 min) -- Assign a reproducibility level (0-5):

| Level | Label | Description |
|-------|-------|-------------|
| 0 | `no_code` | No code repository found |
| 1 | `link_only` | Link is dead/private/empty |
| 2 | `code_available` | Public repo with some code |
| 3 | `code_documented` | Code + README + dependency declarations |
| 4 | `code_installable` | Dependencies install successfully |
| 5 | `code_runnable` | Main script executes without crash |

## Project Structure

```
program.md                 -- Agent instructions for running the evaluation pipeline
pyproject.toml             -- Project dependencies (managed by uv)
data/
  rescience_bibtex_table.xlsx  -- ReScience bibtex reference data
  articles_metadata.parquet    -- Full article metadata (DOIs, titles, abstracts) [to be created]
src/
  discover.py              -- Repository discovery logic (read-only)
  evaluate.py              -- Evaluation pipeline (editable by agent)
  utils.py                 -- Shared utilities (read-only)
results/
  progress.json            -- Evaluation state tracker
  session_<tag>.tsv        -- Per-session evaluation logs
  figures/                 -- Generated charts for the paper
  pipeline_changelog.md    -- Log of pipeline improvements
```

## Running an Evaluation Session

Evaluation sessions run autonomously on dedicated git branches. See `program.md` for the full agent protocol. The short version:

```bash
git checkout -b autorepro/<tag>    # e.g. autorepro/apr8-ieee-its
# Agent runs the evaluation loop, committing results per article
```

Expected pace: ~6 articles/hour, ~48 per overnight run, ~250 for statistical significance.

## Outputs

After >= 100 articles, the pipeline generates:
- `results/figures/repro_by_journal.png` -- Reproducibility levels by journal
- `results/figures/repro_by_year.png` -- Temporal trends
- `results/figures/failure_modes.png` -- Failure mode frequencies
- `results/summary_stats.json` -- Aggregate statistics for the paper draft
