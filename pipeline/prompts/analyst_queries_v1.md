# Paper Analyst -- NotebookLM Query Sequence v1

Targeted queries sent to NotebookLM via MCP. Each query extracts one
facet of the PaperProfile. NotebookLM only answers from the uploaded
document, eliminating hallucinated tools, datasets, or methodology steps.

---

## Query: methodology

List every step of the research methodology in sequential order.
For each step, state:
- A description of what is done
- Any software tools, libraries, or frameworks used (with version numbers if stated)
- The input data required
- The expected output produced
Only include information explicitly stated in the paper. If a version number
is not mentioned, say "version not stated".

Return the result as a JSON array where each element is an object with keys: step_number, description, software_tools, input_data, expected_output. Return only the JSON, no other text.

---

## Query: datasets

List every dataset referenced in this paper. For each dataset, state:
- The dataset name
- The URL or DOI (if provided)
- A description of what it contains
- The approximate size (if stated)
- The licence (if stated)
- Whether it is described as openly available, available upon request,
  or not mentioned

Return the result as a JSON array where each element is an object with keys: name, url, description, approximate_size, licence, availability. Use null for unknown fields. Return only the JSON, no other text.

---

## Query: artefacts

List all code repositories, supplementary materials, and external resources
mentioned anywhere in this paper, including in the references, footnotes,
acknowledgements, and data availability statement. Include URLs, GitHub
links, Zenodo DOIs, and institutional repository references.

Return the result as a JSON object with keys: repository_links (array of URLs), supplementary_materials (array of other resources), hardware_requirements (string or null). Return only the JSON, no other text.

---

## Query: figures_tables

For each figure and table in the results section, describe:
- What data it visualises or presents
- What computation or analysis produces it
- What input data is needed to generate it

Return the result as a JSON object with keys: figures (array of objects with keys: id, caption, type, data_source) and tables (array of objects with keys: id, caption, columns, data_source). Return only the JSON, no other text.

---

## Query: parameters

List all parameters, hyperparameters, configuration values, and
hardware requirements mentioned in this paper. Include numerical
values, ranges, and any stated defaults.

Return the result as a JSON object with keys: software_versions (object mapping name to version), hyperparameters (array of objects with keys: name, value, context), hardware (string or null). Return only the JSON, no other text.
