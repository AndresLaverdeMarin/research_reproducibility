# reproduce_all_figures.py -- Code Documentation

Generates all figures and statistical validation from "Revisiting reproducibility in transportation simulation studies" (Riehl, Kouvelas & Makridis, 2025).

## Dependencies

- matplotlib, pandas, numpy, seaborn, scipy
- Inputs (relative to `code/` directory):
  - `../data/ArticleInformation/ArticleInfos.xlsx` -- 46,015 article metadata
  - `../data/Survey/Simulation_Reproducibility_in_Transportation_Science_Submissions.csv` -- 87 survey responses
  - `../data/JournalIndex_Top20/Journals_Top20.xlsx` -- Journal metadata
  - `../data/ClarivateJournalCitationReports/JIF_History.xlsx` -- Journal impact factors
- Output: `../figures/` directory (6 PNG files at 300 DPI)

## Key Constants (Lines 37-67)

| Constant               | Value | Purpose                                                    |
|-------------------------|-------|------------------------------------------------------------|
| `simulation_threshold`  | 5     | Min word count of "simulation" to classify as simulation study |
| `year_threshold`        | 2014  | Cutoff for "last 5 years" analyses (Figures 2-3)           |
| `year_threshold_detail` | 2017  | Cutoff for detailed repository trend analysis (Figure 3)   |

15 journals analyzed, mapped to display names in `journal_names` dict.

## Data Loading (Lines 20-32)

- `df_articleinfos`: Master article metadata (46,015 rows). Key columns: `article_year`, `wc_simulation` (simulation keyword count), `has_repository`, `has_valid_repository`, `repo_score` (1-5), `num_cits_per_year`.
- `df_survey`: Survey responses (87 rows). Columns are full survey question texts.
- `df_journal_infos`: Journal h5-index and h5-median.
- `df_jif_infos`: Journal Impact Factor history, melted to long format (Nr, year, value).

## Figures

### Figure 1 (Lines 70-122): Simulation Studies & Repository Availability Over Time
- 1x3 subplot grid
- Panel 1: Line plot of total articles, simulation studies, and studies with repository (2000-2023)
- Panel 2: Share of simulation studies as % of all articles
- Panel 3: Share of simulation studies that have a valid repository (%)

### Figure 2 (Lines 125-200): Repositories & Journal Impact
- 1x3 subplot grid
- Panel 1: Scatter plot of h5-median vs % with repository, with linear fit
- Panel 2: Bar chart of Crossref JIF (binned into 10 bins) vs % with repository
- Panel 3: Violin plot of JIF distribution by repository score (0-5)

Data filtered to articles from `year_threshold` (2014) onward. Repository scores filled with 0 for articles without repositories.

### Figure 3 (Lines 203-279): Repositories Over Time
- 1x3 subplot grid, from `year_threshold_detail` (2017) onward
- Panel 1: Line plots for % of repositories containing video, code, data, model, documentation, license
- Panel 2: Stacked area chart of repository score distribution (Levels 1-5)
- Panel 3: Average repository score trend over time

Repository attributes (`has_video`, `has_code`, `has_dataset`, `has_model`, `has_documentation`, `has_license`) are aggregated per year and divided by total repository count.

### Figure 4 (Lines 282-332): Survey Demographics
- 1x3 subplot grid
- Panel 1: Research experience distribution (1-2, 2-3, 3-4, 5-10, 10+ years)
- Panel 2: Current position distribution (Master to Senior Professor)
- Panel 3: Region distribution (7 regions)

Uses helper `drawQuestionBarPlotDemo()` which draws bars with count labels inside/above bars.

### Figure 5 (Lines 335-464): Survey Perception by Position & Region
- 2x4 subplot grid (rows: by position, by region)
- Columns: Reproducibility as significant issue, Need for transparency, Mandatory data availability, Implemented strategy (%)
- Horizontal bar charts with mean +/- std error bars (Likert scale 1-5)
- Strategy column shows % agreement with sample size annotations

### Figure 6 (Lines 467-647): Full Survey Questionnaire Results
- 5x4 subplot grid (20 panels)
- Row 1 (Q1.1-1.4): Perceived severity -- bar charts with average overlay
- Rows 2-3 (Q2.1-2.8): Factors influencing transparency -- includes two dual-bar comparisons (self vs others)
- Rows 4-5 (Q3.1-3.7): Suggestions for improvement -- includes one Yes/No panel

Helper functions:
- `drawQuestionBarPlot()`: Single Likert bar chart with average line
- `drawQuestionBarPlotYesNo()`: Yes/No bar chart with percentage labels
- `drawDoubleQuestionBarPlot()`: Side-by-side bars comparing "Me" vs "Others" responses

## Statistical Validation (Lines 653-793)

Reproduces the hypothesis tests from Section 2.3 of the paper:

### Comparison 1: Simulation vs Non-Simulation Studies (citation impact)
- Groups: articles with `wc_simulation >= 5` vs `< 5`
- Tests: one-sided T-test, one-sided Mann-Whitney U, Kruskal-Wallis H
- Paper finding: simulation studies have significantly higher citations/year (4.39 vs 3.55)

### Comparison 2: With Repository vs Without Repository (citation impact)
- Groups: simulation studies with `has_repository == True` vs `False`
- Tests: same three tests
- Paper finding: NO significant difference (p > 0.2 for all tests)

Validation output compares reproduced values against paper-reported values and reports MATCH/CLOSE/DIFFERS status for each metric.
