"""Render tables and figures for the consistency check experiment.

Reads every JSON in data/experiments/consistency_checks/, parses the
filename to extract (paper, temperature, sample, model), and computes
sample-to-sample stability metrics per (paper, model, temperature) cell:

  - Jaccard similarity of node_ids across the N samples for each layer
    (sources / processes / sinks);
  - mean and standard deviation of the analyst's reproducibility_score
    (averaged over all nodes within each profile).

Aggregates those into three tables saved as CSV under
data/experiments/figures/, plus one figure (PNG):

  Table 1 -- consistency across temperatures (averaged over model, paper)
  Table 2 -- consistency across paper lengths (averaged over model, temperature)
  Table 3 -- consistency across models       (averaged over temperature, paper)

Usage (from src/):
    uv run python _figures_tables/consistency_check.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

INPUT_DIR = Path("data/experiments/consistency_checks")
OUT_DIR = Path("data/experiments/figures")

# Manual page / token survey for the 10-paper consistency suite.
# (pages, tokens) -- used for paper-length grouping in Table 2.
PAPER_LENGTHS: dict[str, tuple[int, int]] = {
    "2017_04_article": (4, 3372),
    "2020_26_article": (8, 3701),
    "2017_01_article": (15, 6436),
    "2025_03_article": (20, 8930),
    "2017_08_article": (11, 9237),
    "2022_30_article": (18, 9800),
    "2021_34_article": (28, 13493),
    "2023_17_article": (24, 14733),
    "2023_15_article": (30, 16170),
    "2022_38_article": (34, 22917),
}

# Filename schema written by run_consistency_experiment.py:
#   <paper>_T<t>_exe<n>_<model_slug>.profile.json
# t is encoded with 'p' for the decimal point (T0p5, T1, T1p5).
NAME_RE = re.compile(
    r"^(?P<paper>.+?)"
    r"_T(?P<t>\d+(?:p\d+)?)"
    r"_exe(?P<sample>\d+)"
    r"_(?P<model_slug>.+?)"
    r"\.profile\.json$"
)


def parse_filename(name: str) -> dict | None:
    m = NAME_RE.match(name)
    if not m:
        return None
    return {
        "paper": m.group("paper"),
        "temperature": float(m.group("t").replace("p", ".")),
        "sample": int(m.group("sample")),
        "model": m.group("model_slug").replace("_", "."),
        "model_slug": m.group("model_slug"),
    }


def _mean_repro(prof: dict) -> float:
    """Mean reproducibility_score across every node in the profile, in [0, 100]."""
    scores: list[int] = []
    for layer in ("nodes_source", "nodes_process", "nodes_sink"):
        for n in prof.get(layer, []):
            scores.append(int(n.get("reproducibility_score", 0)))
    return sum(scores) / len(scores) if scores else 0.0


def _jaccard(sets: list[frozenset]) -> float:
    """Jaccard similarity across a list of sets; 1.0 if all empty or identical."""
    if not sets:
        return 1.0
    union = set().union(*sets)
    if not union:
        return 1.0
    inter = set(sets[0])
    for s in sets[1:]:
        inter &= s
    return len(inter) / len(union)


def collect() -> pd.DataFrame:
    """One row per profile JSON under INPUT_DIR."""
    rows: list[dict] = []
    for path in sorted(INPUT_DIR.glob("*.profile.json")):
        meta = parse_filename(path.name)
        if meta is None:
            continue
        try:
            prof = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        rows.append(
            {
                **meta,
                "n_sources": len(prof.get("nodes_source", [])),
                "n_processes": len(prof.get("nodes_process", [])),
                "n_sinks": len(prof.get("nodes_sink", [])),
                "src_ids": frozenset(
                    n["node_id"] for n in prof.get("nodes_source", []) if n.get("node_id")
                ),
                "proc_names": frozenset(
                    (n.get("node_name") or n.get("node_id", "")).strip().lower()
                    for n in prof.get("nodes_process", [])
                ),
                "sink_ids": frozenset(
                    n["node_id"] for n in prof.get("nodes_sink", []) if n.get("node_id")
                ),
                "mean_repro": _mean_repro(prof),
            }
        )
    return pd.DataFrame(rows)


def consistency_per_group(df: pd.DataFrame) -> pd.DataFrame:
    """Sample-to-sample stability per (paper, model, temperature)."""
    rows = []
    for (paper, model_slug, t), grp in df.groupby(["paper", "model_slug", "temperature"]):
        if len(grp) < 2:
            continue
        rows.append(
            {
                "paper": paper,
                "model": grp["model"].iloc[0],
                "model_slug": model_slug,
                "temperature": t,
                "n_samples": len(grp),
                "src_jaccard": _jaccard(list(grp["src_ids"])),
                "proc_jaccard": _jaccard(list(grp["proc_names"])),
                "sink_jaccard": _jaccard(list(grp["sink_ids"])),
                "mean_repro_mean": grp["mean_repro"].mean(),
                "mean_repro_std": grp["mean_repro"].std(),
                "n_processes_mean": grp["n_processes"].mean(),
                "n_processes_std": grp["n_processes"].std(),
            }
        )
    out = pd.DataFrame(rows)
    if not out.empty:
        out["overall_jaccard"] = out[["src_jaccard", "proc_jaccard", "sink_jaccard"]].mean(axis=1)
    return out


def table_temperature(consist: pd.DataFrame) -> pd.DataFrame:
    """Table 1: stability vs temperature, averaged over (model, paper)."""
    return (
        consist.groupby("temperature")[
            [
                "src_jaccard",
                "proc_jaccard",
                "sink_jaccard",
                "overall_jaccard",
                "mean_repro_mean",
                "mean_repro_std",
            ]
        ]
        .mean()
        .round(3)
    )


def table_paper_length(consist: pd.DataFrame) -> pd.DataFrame:
    """Table 2: stability vs paper length, averaged over (model, temperature)."""
    df = consist.copy()
    df["pages"] = df["paper"].map(lambda p: PAPER_LENGTHS.get(p, (None, None))[0])
    df["tokens"] = df["paper"].map(lambda p: PAPER_LENGTHS.get(p, (None, None))[1])
    return (
        df.groupby(["paper", "pages", "tokens"])[
            [
                "src_jaccard",
                "proc_jaccard",
                "sink_jaccard",
                "overall_jaccard",
                "mean_repro_mean",
                "mean_repro_std",
            ]
        ]
        .mean()
        .sort_values("tokens")
        .round(3)
    )


def table_model(consist: pd.DataFrame) -> pd.DataFrame:
    """Table 3: stability vs model, averaged over (temperature, paper)."""
    return (
        consist.groupby("model")[
            [
                "src_jaccard",
                "proc_jaccard",
                "sink_jaccard",
                "overall_jaccard",
                "mean_repro_mean",
                "mean_repro_std",
            ]
        ]
        .mean()
        .round(3)
    )


def render_figure(consist: pd.DataFrame, out_path: Path) -> None:
    """One panel: overall Jaccard vs paper tokens, line per model."""
    import matplotlib.pyplot as plt

    df = consist.copy()
    df["tokens"] = df["paper"].map(lambda p: PAPER_LENGTHS.get(p, (None, None))[1])
    df = df.dropna(subset=["tokens"])

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for model, grp in df.groupby("model"):
        agg = grp.groupby("tokens")["overall_jaccard"].mean().sort_index()
        ax.plot(agg.index, agg.values, marker="o", label=model)
    ax.set_xlabel("paper length (tokens)")
    ax.set_ylabel("overall Jaccard stability")
    ax.set_ylim(0, 1.02)
    ax.set_title("Consistency vs paper length, per model")
    ax.legend(loc="best", fontsize=8, frameon=False)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main() -> int:
    if not INPUT_DIR.is_dir():
        print(f"No input directory: {INPUT_DIR}")
        return 1
    df = collect()
    if df.empty:
        print(f"No profile JSONs found under {INPUT_DIR}")
        return 1

    consist = consistency_per_group(df)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    t1 = table_temperature(consist)
    t2 = table_paper_length(consist)
    t3 = table_model(consist)

    print("Table 1: consistency across temperatures")
    print(t1.to_string())
    print()
    print("Table 2: consistency across paper lengths")
    print(t2.to_string())
    print()
    print("Table 3: consistency across models")
    print(t3.to_string())
    print()

    t1.to_csv(OUT_DIR / "table1_consistency_temperature.csv")
    t2.to_csv(OUT_DIR / "table2_consistency_paper_length.csv")
    t3.to_csv(OUT_DIR / "table3_consistency_model.csv")
    consist.to_csv(OUT_DIR / "consistency_per_group.csv", index=False)
    print(f"Wrote: {OUT_DIR}/table{{1,2,3}}_*.csv  +  consistency_per_group.csv")

    try:
        render_figure(consist, OUT_DIR / "fig_consistency_vs_length.png")
        print(f"Wrote: {OUT_DIR / 'fig_consistency_vs_length.png'}")
    except Exception as exc:
        print(f"Figure rendering skipped: {type(exc).__name__}: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
