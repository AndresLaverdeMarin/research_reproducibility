# autoreproducibility

This is an autonomous research pipeline for evaluating the reproducibility of computational research papers. Adapted from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) for a meta-science study on research reproducibility across 14 transportation/energy journals (~46,015 articles).

**Context**: This is part of a NeurIPS 2026 submission (deadline: early May) with collaborators Michalis (ETH) and Kevin. The goal is to systematically assess how many published papers provide accessible, functional, and reproducible code.

## Setup

To set up a new evaluation session, work with the user to:

1. **Agree on a session tag**: propose a tag based on today's date and scope (e.g. `apr8-ieee-its`, `apr9-trb`). The branch `autorepro/<tag>` must not already exist.
2. **Create the branch**: `git checkout -b autorepro/<tag>` from current main.
3. **Read the in-scope files**: Read these files for full context:
   * `README.md` — project overview and research questions.
   * `config.yaml` — journal list, API keys, search parameters, evaluation criteria.
   * `src/discover.py` — repository discovery logic (GitHub API, paper metadata parsing). Do not modify.
   * `src/evaluate.py` — the file you modify. Contains the reproducibility evaluation pipeline.
   * `src/utils.py` — shared utilities (logging, API helpers, file I/O). Do not modify.
   * `data/articles_metadata.parquet` — the full article metadata (DOIs, titles, abstracts, authors, years, journals).
4. **Check state**: Read `results/progress.json` to see which articles have already been evaluated. Never re-evaluate already-completed articles.
5. **Initialize session log**: Create `results/session_<tag>.tsv` with the header row.
6. **Confirm and go**: Confirm setup looks good, then begin the evaluation loop.

## The Reproducibility Evaluation Pipeline

Each article evaluation follows a fixed sequence of stages. The agent works through them autonomously, one article at a time.

### Stage 1: Repository Discovery (budget: 2 min)

Given an article's metadata (DOI, title, authors, abstract):

1. **PDF full-text extraction**: Resolve the DOI to the publisher page, download the PDF, and convert it to Markdown using MarkItDown. Then regex-search the full text for repository URLs (GitHub, GitLab, Bitbucket, Zenodo, Figshare). This catches URLs in footnotes, acknowledgements, and "Data Availability" sections that don't appear in abstracts.
   ```python
   from markitdown import MarkItDown
   import re

   md = MarkItDown(enable_plugins=False)
   result = md.convert("paper.pdf")
   url_pattern = r'https?://(?:github\.com|gitlab\.com|bitbucket\.org|zenodo\.org|figshare\.com)/[^\s\)\]>\"\']*'
   repo_urls = re.findall(url_pattern, result.text_content)
   ```
   If PDF download fails (paywall, 403, timeout >30s), fall back to abstract-only search.
2. Search GitHub via API: `author_lastname + keyword_from_title`.
3. Search Papers With Code for the DOI or title.
4. Check if the DOI resolves to a page with supplementary materials.
5. Record: `repo_url` (or `NOT_FOUND`), `discovery_method`, `confidence` (high/medium/low). When the URL was found via PDF full-text, set `discovery_method` to `pdf_fulltext`.

**What you CAN do:**
* Modify `src/evaluate.py` — this is the only file you edit. Evaluation logic, heuristics, classification rules, output formatting.
* Add new discovery heuristics or classification criteria within `evaluate.py`.

**What you CANNOT do:**
* Modify `src/discover.py`, `src/utils.py`, or `config.yaml`. They are read-only.
* Install new packages. Use only what's in `pyproject.toml`.
* Modify the article metadata. `data/articles_metadata.parquet` is ground truth.
* Make more than 30 GitHub API calls per article (rate limit budget).

### Stage 2: Repository Assessment (budget: 3 min, skip if no repo found)

If a repository was found:

1. **Exists & accessible**: Can the repo be cloned? Is it public?
2. **Documentation**: Does it have a README? Requirements file? Installation instructions?
3. **Dependencies declared**: Is there a `requirements.txt`, `environment.yml`, `pyproject.toml`, `setup.py`, `Dockerfile`, or equivalent?
4. **Code completeness**: Does the repo contain what appears to be the full pipeline (data loading → model → evaluation), or just fragments?
5. **Data availability**: Are datasets included, linked, or described? Are they accessible?
6. **Last activity**: When was the last commit? Is the repo archived/abandoned?

Record a structured assessment with scores for each dimension.

### Stage 3: Lightweight Reproduction Attempt (budget: 5 min, skip if no repo or no dependencies)

If the repo has declared dependencies:

1. Create an isolated environment (venv or conda).
2. Attempt `pip install -r requirements.txt` or equivalent.
3. Log: did installation succeed? Which dependencies failed?
4. If installation succeeds, attempt to run the main script or entry point.
5. Log: did it start? Did it crash? What was the error?

**DO NOT** attempt full training runs or download large datasets. This stage only checks whether the code is *structurally runnable*, not whether it *reproduces results*.

### Stage 4: Classification (budget: 1 min)

Classify each article into one of these reproducibility levels:

| Level | Label | Description |
|-------|-------|-------------|
| 0 | `no_code` | No code repository found anywhere |
| 1 | `link_only` | Paper mentions code but link is dead/private/empty |
| 2 | `code_available` | Public repo exists with some code |
| 3 | `code_documented` | Code + README + dependency declarations |
| 4 | `code_installable` | Dependencies install successfully |
| 5 | `code_runnable` | Main script executes without immediate crash |

Also tag with failure modes when applicable:
`dead_link`, `private_repo`, `missing_deps`, `python2_only`, `missing_data`, `undeclared_deps`, `version_conflict`, `import_error`, `runtime_error`, `gpu_required`, `platform_specific`

## Output Format

After each article evaluation, print a summary:

```
---
doi:                10.1109/TITS.2023.XXXXXXX
journal:            IEEE-TITS
year:               2023
repo_found:         yes
repo_url:           https://github.com/user/repo
discovery_method:   paper_text
repro_level:        3
failure_modes:      missing_data,version_conflict
eval_seconds:       285
notes:              README present, requirements.txt has pinned versions but numpy 1.x conflicts with Python 3.11
---
```

## Logging Results

When an article evaluation is done, log it to `results/session_<tag>.tsv` (tab-separated).

The TSV has a header row and these columns:

```
doi	journal	year	repo_found	repo_url	discovery_method	discovery_confidence	repro_level	failure_modes	eval_seconds	notes
```

Example:

```
doi	journal	year	repo_found	repo_url	discovery_method	discovery_confidence	repro_level	failure_modes	eval_seconds	notes
10.1109/TITS.2023.1234567	IEEE-TITS	2023	yes	https://github.com/user/repo	paper_text	high	3	missing_data	285	Good docs but dataset not public
10.1016/j.apenergy.2024.5678	AppliedEnergy	2024	no	NOT_FOUND	-	-	0	-	120	No code mentions in paper
10.1038/s41598-2022-9999	SciRep	2022	yes	https://github.com/user/repo2	github_search	medium	1	dead_link	90	404 on linked repo
```

## The Evaluation Loop

The evaluation runs on a dedicated branch (e.g. `autorepro/apr8-ieee-its`).

LOOP FOREVER:

1. Read `results/progress.json` to get the list of already-evaluated DOIs.
2. Select the next unevaluated article from `data/articles_metadata.parquet`. Prioritize by: (a) journals with fewest evaluated articles so far (balance coverage), (b) within a journal, sample across years.
3. Run the full evaluation pipeline (Stages 1→4) for this article.
4. Log results to the session TSV.
5. Update `results/progress.json` with the new DOI and its classification.
6. Git commit the updated progress and session TSV: `git add results/ && git commit -m "eval: <doi> → level <N>"`.
7. Print a running summary every 10 articles:
   ```
   === Session Progress ===
   Articles evaluated this session: 47
   Running time: 3h 22m
   Distribution: L0=21 L1=5 L2=9 L3=7 L4=3 L5=2
   Journals covered: IEEE-TITS(12) AppliedEnergy(8) TRR(7) ...
   ===
   ```
8. Move to the next article.

### Pacing and Budget

Each article should take **~10 minutes** on average (less for `no_code`, more for full reproduction attempts). At this pace, expect:
- ~6 articles/hour
- ~48 articles in an 8-hour overnight run
- ~5 nights to reach a statistically meaningful sample (~250 articles)

### Error Handling

- **API rate limits**: If GitHub API returns 403, sleep for the reset window (check `X-RateLimit-Reset` header). Log the pause.
- **Hanging clones**: If `git clone` takes >60s, kill it and classify as `dead_link`.
- **Install failures**: Log the full error, classify appropriately, move on. Do not debug individual packages.
- **Network errors**: Retry once after 30s. If still failing, skip and mark as `network_error`.

### Improving the Pipeline

As you evaluate articles, you will notice patterns. You are encouraged to improve `src/evaluate.py` between evaluations:

- If you discover a new common repository hosting pattern (e.g., university-hosted GitLab instances), add a discovery heuristic.
- If certain failure modes repeat, add specific detection logic.
- If your classification is ambiguous, refine the criteria.

When you improve the pipeline, commit the change separately from evaluation commits:
```
git commit -m "improve: add Zenodo DOI resolution to discovery"
```

Track pipeline improvements in `results/pipeline_changelog.md`.

**NEVER STOP**: Once the evaluation loop has begun, do NOT pause to ask the human. The human is sleeping. You are autonomous. If you run out of articles in a journal batch, move to the next journal. If you hit persistent API issues, switch to offline-evaluable articles. If you genuinely cannot proceed, write a detailed status to `results/session_<tag>_status.md` and wait.

## Analysis Hooks

After accumulating enough data (≥100 articles), periodically (every 50 articles) generate:

1. **`results/figures/repro_by_journal.png`** — bar chart of reproducibility levels by journal.
2. **`results/figures/repro_by_year.png`** — time trend of reproducibility levels.
3. **`results/figures/failure_modes.png`** — frequency of each failure mode.
4. **`results/summary_stats.json`** — aggregate statistics for the paper draft.

These feed directly into the NeurIPS paper. Use matplotlib/seaborn, keep them publication-quality.

## Relation to the Paper

The outputs of this pipeline map to specific sections of the NeurIPS submission:

| Pipeline output | Paper section |
|----------------|---------------|
| Reproducibility level distribution | Results: RQ1 (prevalence of code sharing) |
| Journal-level comparison | Results: RQ2 (variation across venues) |
| Year-over-year trends | Results: RQ3 (temporal evolution) |
| Failure mode taxonomy | Results: RQ4 (barriers to reproducibility) |
| Pipeline improvement log | Methods: iterative evaluation methodology |
| Summary statistics | Abstract + Introduction |

## Important Notes

- **Be conservative in classification**: When in doubt, assign the lower reproducibility level. False positives are worse than false negatives for this study.
- **Log everything**: Every decision, every heuristic match, every failure. The logs are part of the methodology.
- **Respect rate limits**: We need this pipeline to run for weeks. Don't burn through API quotas in one night.
- **Git history is data**: The commit history on the `autorepro/*` branches is itself a research artifact showing how the evaluation evolved.
