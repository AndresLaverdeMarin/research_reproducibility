"""Extract markdown from paired ReScience C / original PDFs.

Runs MarkItDown + the cleanup pipeline from ``pdf_extractor`` on every row of the
bibtex table that has a filename in BOTH ``pdf_file`` columns. ReScience outputs go
to ``data/extracted/rescience/`` and original outputs to ``data/extracted/original/``.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from markitdown import MarkItDown

from pdf_extractor import clean_markdown

SCRIPT_DIR = Path(__file__).parent
XLSX_PATH = SCRIPT_DIR / "data" / "rescience_bibtex_table.xlsx"
RESCIENCE_PDFS = SCRIPT_DIR / "data" / "pdf_cache"
ORIGINAL_PDFS = SCRIPT_DIR / "data" / "pdf_original_cache"
RESCIENCE_OUT = SCRIPT_DIR / "data" / "extracted" / "rescience"
ORIGINAL_OUT = SCRIPT_DIR / "data" / "extracted" / "original"

# Column positions after the pdf_downloader run:
#   col 18 -> RESCIENCE C pdf_file
#   col 28 -> ORIGINAL    pdf_file
RESCIENCE_PDF_COL = 18
ORIGINAL_PDF_COL = 28


def paired_rows() -> pd.DataFrame:
    """Return rows that have both a RESCIENCE and an ORIGINAL pdf_file value."""
    df = pd.read_excel(XLSX_PATH)
    df = df.iloc[1:].reset_index(drop=True)
    r = df.iloc[:, RESCIENCE_PDF_COL]
    o = df.iloc[:, ORIGINAL_PDF_COL]
    return df[r.notna() & o.notna()].reset_index(drop=True)


def extract_pdf(pdf_path: Path, md_path: Path, md: MarkItDown) -> None:
    """Convert one local PDF to a cleaned markdown file."""
    result = md.convert(str(pdf_path))
    cleaned = clean_markdown(result.text_content)
    cleaned += f"\n\n---\n**Source PDF:** `{pdf_path.name}`\n"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(cleaned)


def main() -> None:
    df = paired_rows()
    total = len(df)
    print(f"Paired papers to extract: {total}\n")

    md = MarkItDown(enable_plugins=False)
    failures: list[tuple[str, str]] = []

    for i, row in df.iterrows():
        rescience_name = str(row.iloc[RESCIENCE_PDF_COL]).strip()
        original_name = str(row.iloc[ORIGINAL_PDF_COL]).strip()
        stem = Path(rescience_name).stem

        rescience_pdf = RESCIENCE_PDFS / rescience_name
        original_pdf = ORIGINAL_PDFS / original_name
        rescience_md = RESCIENCE_OUT / f"{stem}.md"
        original_md = ORIGINAL_OUT / f"{stem}.md"

        print(f"[{i+1}/{total}] {stem}")

        for label, pdf, out in (
            ("rescience", rescience_pdf, rescience_md),
            ("original", original_pdf, original_md),
        ):
            if out.exists():
                print(f"  {label}: cached -> {out.relative_to(SCRIPT_DIR)}")
                continue
            if not pdf.exists():
                print(f"  {label}: MISSING pdf {pdf}")
                failures.append((label, str(pdf)))
                continue
            try:
                extract_pdf(pdf, out, md)
                print(f"  {label}: saved  -> {out.relative_to(SCRIPT_DIR)}")
            except Exception as exc:
                print(f"  {label}: FAILED ({pdf.name}): {exc}")
                failures.append((label, str(pdf)))

    print(f"\nDone. Failures: {len(failures)}")
    for label, pdf in failures:
        print(f"  [{label}] {pdf}")


if __name__ == "__main__":
    main()
