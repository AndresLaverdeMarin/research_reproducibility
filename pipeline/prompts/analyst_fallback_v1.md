# Paper Analyst -- Gemini API Fallback Prompt v1

Used when NotebookLM is unavailable (service outage, auth failure, or
batch processing). The five queries are consolidated into a single prompt
sent to the Gemini API with the paper PDF attached.

---

## Task

You are analysing a research paper for reproducibility. Extract a structured
PaperProfile by answering the following questions using ONLY information
present in the attached paper. If information is not stated, respond with null.

### 1. Methodology

List every step of the research methodology in sequential order.
For each step, state:
- A description of what is done
- Any software tools, libraries, or frameworks used (with version numbers if stated)
- The input data required
- The expected output produced
Only include information explicitly stated in the paper. If a version number
is not mentioned, say "version not stated".

### 2. Datasets

List every dataset referenced in this paper. For each dataset, state:
- The dataset name
- The URL or DOI (if provided)
- A description of what it contains
- The approximate size (if stated)
- The licence (if stated)
- Whether it is described as openly available, available upon request,
  or not mentioned

### 3. Reproducibility Artefacts

List all code repositories, supplementary materials, and external resources
mentioned anywhere in this paper, including in the references, footnotes,
acknowledgements, and data availability statement. Include URLs, GitHub
links, Zenodo DOIs, and institutional repository references.

### 4. Figures and Tables

For each figure and table in the results section, describe:
- What data it visualises or presents
- What computation or analysis produces it
- What input data is needed to generate it

### 5. Parameters and Configuration

List all parameters, hyperparameters, configuration values, and
hardware requirements mentioned in this paper. Include numerical
values, ranges, and any stated defaults.

## Output Schema

Respond with a valid JSON object conforming to the PaperProfile schema:

```json
{
  "doi": "string or null",
  "title": "string",
  "authors": ["string"],
  "methodology_steps": [
    {
      "order": 1,
      "description": "string",
      "tools_mentioned": ["Python 3.9", "pandas"],
      "data_inputs": ["article_corpus.csv"],
      "expected_outputs": ["figure_1.png"],
      "confidence": 0.0
    }
  ],
  "datasets": [
    {
      "name": "string",
      "url": "string or null",
      "description": "string",
      "size_estimate": "string or null",
      "licence": "string or null",
      "availability": "open | upon_request | not_mentioned"
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
  "hardware_requirements": "string or null",
  "stated_software_versions": {}
}
```
