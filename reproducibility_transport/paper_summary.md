# Revisiting Reproducibility in Transportation Simulation Studies

**Authors:** Kevin Riehl, Anastasios Kouvelas, Michail A. Makridis
**Published in:** European Transport Research Review, 17, 22 (2025)
**DOI:** [10.1186/s12544-025-00718-9](https://doi.org/10.1186/s12544-025-00718-9)

---

## 1. Main Idea

This paper addresses the **lack of transparency and reproducibility** in computational simulation studies within transportation science. While simulations have become a dominant methodology -- used in more than every third study by 2024 -- most publications fail to provide the source code, data, or detailed models required for independent verification.

The research sets out to:
- Assess the current state of transparency across the field's top journals
- Determine whether providing repositories increases citation impact
- Survey the research community's perceptions of reproducibility as an issue
- Identify barriers preventing researchers from sharing materials
- Propose professional standards, best-practice templates, and repository management guidelines

The motivation stems from the principle of **scientific falsifiability**: if theories cannot be independently tested and replicated, the reliability of the field's findings is undermined. The authors argue that transportation science has not yet adopted the open-source professionality common in fields like computer science.

---

## 2. Results

### 2.1 Corpus Analysis

- **46,015 articles** analyzed from **14 journals** (out of the top 20 by h5-index), covering 2000 to August 2024
- **11,879** identified as simulation studies (~25.82% of total)
- By 2024, more than **every third study** (~33%) employs simulations
- In Transportation Research Part C, over **58%** of studies use simulations

### 2.2 Repository Availability

- Only **1.82%** of simulation studies (2000-2024) provided a repository
- By 2024, ~**5%** of simulation studies include repositories (sharp increase since 2014)
- Of 2,388 manually inspected links, only **672** were author-owned, non-empty repositories
- Average repository quality: between **Level 2 and 3** on a 5-point scale

**Repository quality distribution:**
| Level | Description | Share |
|-------|-------------|-------|
| 1 | Not empty | 17.21% |
| 2 | Multiple file types | 23.93% |
| 3 | Basic documentation/README | 28.03% |
| 4 | Reader-friendly documentation | 18.36% |
| 5 | Comprehensive (code, data, models, licenses) | 12.46% |

**Repository contents:** Datasets (67.70%), Source code (64.75%), Basic documentation (59.51%), Models (39.84%), Licenses (38.69%)

**Programming languages:** Python (48.86%), Jupyter Notebook (19.49%), R (16.46%), Matlab (6.58%)

**Platforms:** GitHub (80.33%), Zenodo (6.89%), YouTube (4.43%)

### 2.3 Statistical Tests

| Comparison | T-Test p-value | Mann-Whitney U p-value | Kruskal-Wallis H p-value |
|---|---|---|---|
| Non-Simulation vs. Simulation | 9.06 x 10^-45 | 1.93 x 10^-110 | 3.87 x 10^-110 |
| With vs. Without Repository | 0.324 | 0.218 | 0.437 |

- **Simulation studies receive significantly more citations** (mean 4.39/year) than non-simulation studies (mean 3.55/year)
- **No statistically significant difference** in citations between studies with repositories (mean 4.56) and those without (mean 4.39)

### 2.4 Regression Findings

Negative Binomial regression models (11 variants) with citations per year as the dependent variable:
- Having a repository (`has_repository`) or a high repository score **does not significantly increase citations**
- Providing source code, datasets, models, documentation, or licenses had **no significant impact**
- **Video material** was the only feature showing some positive association (significant at 5-10% level in some models), though results were inconclusive
- Models achieved up to 6.7% Pseudo R-squared (NB) and 36.8% Adjusted R-squared (OLS)

### 2.5 Survey Results (87 respondents)

**Perception of the issue:**
- Reproducibility is a significant issue: **avg 4.11/5**
- Need for more transparency: **avg 4.51/5**
- Spent unnecessary time reproducing studies: **avg 3.21/5**

**Primary impediments:**
- Time constraints: **64%**
- Legal issues (data privacy/IP): **54%**
- Only **35%** admitted to intentionally withholding materials, but **61%** believed others do so

**Recommendations supported:**
- Publish models: **80%**
- Publish software/source code: **78%**
- Funding agencies should require mandatory reproducibility plans: **74%**
- **52%** of respondents' groups have already implemented reproducibility strategies

---

## 3. Constraints and Limitations

1. **Journal selection bias:** Only 14 of the top 20 journals were analyzed. Conferences and non-API publishers were excluded. Conference papers (influenced by computer science norms) might be more transparent, while lower-impact journals might be even less reproducible.

2. **Short survey window:** The survey was live for only 30 days (November 1 - December 1, 2024), limiting the sample to 87 respondents.

3. **Premature phenomenon:** Repository sharing is relatively new in transportation science. The authors suggest repeating the study in 10 years for more definitive citation-impact results.

4. **Proxy for reproducibility:** The study reviewed indicators (presence of materials and repositories) rather than attempting actual reproduction by running code and verifying results.

5. **Platform scope:** Focused on major repository platforms (GitHub, Zenodo, etc.). Authors sharing materials on personal websites or other platforms may not have been captured.

6. **Omitted regression variables:** Author/institution reputation, which could significantly drive citation impact, was not included in the regression models.

---

## 4. Methodology

### 4.1 Literature Analysis Pipeline

1. **Journal selection:** Identified the 20 most impactful transportation journals using the Google Scholar h5-index
2. **Article retrieval:** Compiled article lists from 2000 to August 2024; downloaded full texts via text and data mining APIs from ScienceDirect, Wiley, and Taylor & Francis (14 of 20 journals)
3. **Corpus:** 46,015 articles in PDF, HTML, or XML format
4. **Metadata enrichment:** Citation counts, author counts, and reference lists retrieved via the CrossRef API; word and character counts extracted directly from full texts

### 4.2 Simulation Study Identification

- Keyword-based filtering: an article was classified as a simulation study if the keyword **"simulat"** appeared at least **5 times** in the full text
- This identified 11,879 simulation studies

### 4.3 Repository Identification and Evaluation

- **Link extraction:** Full texts were searched for data availability statements and URLs pointing to GitHub, BitBucket, Zenodo, Mendeley, YouTube, SourceForge, Google Drive, Google Docs, and Dropbox
- **Manual review:** 2,388 links manually inspected to verify they were author-owned and non-empty, yielding 672 relevant repositories
- **5-level scoring system:**
  - Level 1: Non-empty repository
  - Level 2: Multiple file types (e.g., code and data)
  - Level 3: Files plus basic documentation (README)
  - Level 4: Files plus reader-friendly documentation (installation instructions)
  - Level 5: Comprehensive code, data, models, licenses, and working examples

### 4.4 Statistical Analysis

- **Distribution testing:** Kolmogorov-Smirnov tests confirmed citation counts are not normally distributed
- **Group comparisons:** T-tests, Mann-Whitney U-tests, and Kruskal-Wallis H-tests to compare citation means across groups
- **Regression models:** Negative Binomial and OLS regressions with:
  - Dependent variable: citations per year (or its logarithm)
  - Independent variables: repository score, binary feature indicators (video, code, data, model, documentation, license)
  - Control variables: number of authors, number of references, publication length
  - Fixed effects: year and journal dummy variables
  - Outlier removal: Z-score threshold of 3.0 (removing <4% of records)
  - Multicollinearity check: Pearson correlation threshold < 50%

### 4.5 Researcher Survey

- **Design:** Anonymous 27-question survey on the Tally platform with 20 mandatory Likert-scale questions (1-5), demographic questions, and optional open-ended fields
- **Dissemination:** Circulated via the authors' networks, UTSG and TMIP mailing lists, and direct emails
- **Duration:** November 1 to December 1, 2024
- **Responses:** 87 transportation researchers across varying positions (Master to Senior Professor) and regions (Africa, Asia, Australia/Oceania, Europe, Middle East, North/South America)
