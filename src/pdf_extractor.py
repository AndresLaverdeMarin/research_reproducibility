"""Read ReScience C PDFs using MarkItDown and extract clean Markdown files."""

import hashlib
import re
import warnings
from pathlib import Path

import pandas as pd
import requests
from markitdown import MarkItDown

# Suppress SSL warnings (some GitHub raw URLs fail cert verification)
warnings.filterwarnings("ignore", message="Unverified HTTPS request")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_rescience_table(xlsx_path: str | Path) -> pd.DataFrame:
    """Load the ReScience bibtex table and normalise column names."""
    df = pd.read_excel(xlsx_path)
    df = df.iloc[1:].reset_index(drop=True)

    rescience_cols = [
        "idx",
        "rescience_authors", "rescience_title", "rescience_journal",
        "rescience_year", "rescience_month", "rescience_volume",
        "rescience_number", "rescience_doi", "rescience_url",
        "code_url", "code_doi", "data_url", "data_doi",
        "language", "domain", "keywords", "rescience_filename",
        "original_authors", "original_title", "original_journal",
        "original_year", "original_month", "original_volume",
        "original_number", "original_doi", "original_filename",
    ]
    df.columns = rescience_cols[: len(df.columns)]
    return df


# ---------------------------------------------------------------------------
# PDF download
# ---------------------------------------------------------------------------

def normalise_pdf_url(url: str) -> str:
    """Convert GitHub blob URLs to raw URLs so we get the actual PDF."""
    return re.sub(r"github\.com/(.+)/blob/", r"github.com/\1/raw/", url)


def download_pdf(url: str, dest: Path) -> Path:
    """Download a PDF to a local path."""
    url = normalise_pdf_url(url)
    resp = requests.get(url, timeout=60, verify=False)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(resp.content)
    return dest


# ---------------------------------------------------------------------------
# Markdown cleanup
# ---------------------------------------------------------------------------

# ReScience page footers — several formats across journal eras
_FOOTER_RE = re.compile(
    r"^ReScience\s+(?:C\s+)?\d+\.\d+\s*\(#\d+\)\s*[–—-]\s*.+$", re.MULTILINE
)
_FOOTER_OLD_RE = re.compile(
    r"^ReScience\s+j\s+rescience\.github\.io\s+\d+\s+\w+\s+\d+\s+j\s+Volume\s+\d+\s+j\s+Issue\s+\d+$",
    re.MULTILINE,
)

# Standalone page numbers on their own line
_PAGE_NUMBER_RE = re.compile(r"^\d{1,3}$", re.MULTILINE)

# Copyright / correspondence boilerplate
_COPYRIGHT_RE = re.compile(
    r"^Copyright © \d{4} .+$|"
    r"^Correspondence should be addressed to .+$|"
    r"^The authors have declared that no competing interests exist\.$",
    re.MULTILINE,
)

# Numbered section headings: "1 Introduction", "3.2 Datasets"
# Section numbers must start with 1-9 (not 0.x which are table values),
# and the title must start with a capitalized word (not a month/date).
_MONTH_NAMES = (
    "January|February|March|April|May|June|July|August|"
    "September|October|November|December"
)
# Section numbers: 1–99 top-level, subsections like 3.1 or 3.2.1 (digits ≤99 at each level)
# Title must be a real word (≥4 letters), not short tokens like "SGD" from tables
_SECTION_HEADING_RE = re.compile(
    rf"^([1-9]\d?(?:\.\d{{1,2}})*)\s+(?!{_MONTH_NAMES}\b)([A-Z][A-Za-z]{{3,}}.*)$",
    re.MULTILINE,
)

# Title repeated as a running header (e.g. "Learning with Noisy Labels [~Re]visited")
# We detect lines that appear 3+ times and are short — likely running headers
def _find_running_headers(text: str) -> set[str]:
    """Find short lines that repeat many times (running headers).

    Skips lines that look like section headings (start with a number + title)
    or are common structural elements.
    """
    from collections import Counter
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    counts = Counter(lines)
    headers = set()
    for line, count in counts.items():
        if count < 4 or not (5 < len(line) < 120):
            continue
        # Skip lines that look like numbered sections
        if re.match(r"^\d+(?:\.\d+)*\s+[A-Z]", line):
            continue
        headers.add(line)
    return headers


def _promote_sections(text: str) -> str:
    """Turn numbered section headings into proper markdown headings.

    1 Foo        -> # 1 Foo
    2.1 Bar      -> ## 2.1 Bar
    3.2.1 Baz    -> ### 3.2.1 Baz
    A Appendix   -> # A Appendix
    """
    def _replace(m: re.Match) -> str:
        number = m.group(1)
        title = m.group(2)
        depth = number.count(".") + 1
        level = min(depth + 1, 4)  # ## for top-level sections, ### for subsections
        return f"{'#' * level} {number} {title}"

    return _SECTION_HEADING_RE.sub(_replace, text)


def _rejoin_hyphenated(text: str) -> str:
    """Rejoin words split by soft hyphens at line breaks."""
    return re.sub(r"(\w)‐\n(\w)", r"\1\2", text)


def _collapse_blank_lines(text: str) -> str:
    """Reduce runs of 3+ blank lines to 2."""
    return re.sub(r"\n{4,}", "\n\n\n", text)


def _clean_table_artifacts(text: str) -> str:
    """Remove markdown table rows that are just empty cells (MarkItDown artifacts)."""
    # Tables where every cell is empty or whitespace
    text = re.sub(
        r"^(\|[\s|]*\|\s*\n)+(\|[\s\-|]*\|\s*\n)(\|[\s|]*\|\s*\n)*",
        "",
        text,
        flags=re.MULTILINE,
    )
    # Table rows that are just separators with no content rows around them
    text = re.sub(
        r"^\|[\s\-]+\|[\s\-|]*\|\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )
    return text


def clean_markdown(raw_text: str) -> str:
    """Post-process MarkItDown output into clean, well-structured markdown."""
    text = raw_text

    # Remove running headers
    for header in _find_running_headers(text):
        text = text.replace(header + "\n", "\n")

    # Remove page footers
    text = _FOOTER_RE.sub("", text)
    text = _FOOTER_OLD_RE.sub("", text)

    # Remove standalone page numbers
    text = _PAGE_NUMBER_RE.sub("", text)

    # Remove copyright boilerplate
    text = _COPYRIGHT_RE.sub("", text)

    # Clean table artifacts from older PDFs
    text = _clean_table_artifacts(text)

    # Rejoin hyphenated words
    text = _rejoin_hyphenated(text)

    # Promote section headings to markdown headings
    text = _promote_sections(text)

    # Collapse excessive blank lines
    text = _collapse_blank_lines(text)

    return text.strip()


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def process_paper(pdf_url: str, rescience_filename: str, output_dir: Path) -> Path:
    """Download PDF -> convert to markdown -> clean -> save.

    The source footer maps the output back to the cached PDF file.
    """
    cache_dir = output_dir.parent / "pdf_cache"
    url_hash = hashlib.sha256(pdf_url.encode()).hexdigest()[:12]
    cache_name = f"{url_hash}.pdf"
    local_pdf = cache_dir / cache_name

    if not local_pdf.exists():
        download_pdf(pdf_url, local_pdf)

    md = MarkItDown(enable_plugins=False)
    result = md.convert(str(local_pdf))

    cleaned = clean_markdown(result.text_content)

    # Append source mapping: cached PDF name + original filename + URL
    cleaned += (
        f"\n\n---\n"
        f"**Source PDF:** `{cache_name}` ({rescience_filename})  \n"
        f"**URL:** {pdf_url}\n"
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(rescience_filename).stem
    md_file = output_dir / f"{stem}.md"
    md_file.write_text(cleaned)
    return md_file


def main():
    xlsx_path = Path(__file__).parent / "data" / "rescience_bibtex_table.xlsx"
    output_dir = Path(__file__).parent / "data" / "extracted"
    df = load_rescience_table(xlsx_path)

    total = len(df)
    failed = []

    for i, row in df.iterrows():
        url = row["rescience_url"]
        filename = row["rescience_filename"]
        title = row["rescience_title"]

        if pd.isna(url) or not str(url).startswith("http"):
            print(f"[{i+1}/{total}] SKIP (no URL): {title}")
            failed.append((i, title, "no URL"))
            continue

        existing_md = output_dir / f"{Path(str(filename)).stem}.md"
        if existing_md.exists():
            print(f"[{i+1}/{total}] SKIP (already extracted): {existing_md.name}")
            continue

        print(f"[{i+1}/{total}] {title}", flush=True)
        try:
            md_file = process_paper(str(url), str(filename), output_dir)
            print(f"         -> {md_file.name}", flush=True)
        except Exception as e:
            print(f"         FAILED: {e}", flush=True)
            failed.append((i, title, str(e)))

    print(f"\nDone: {total - len(failed)}/{total} extracted")
    if failed:
        print(f"Failed ({len(failed)}):")
        for idx, title, reason in failed:
            print(f"  [{idx}] {title}: {reason}")


if __name__ == "__main__":
    main()
