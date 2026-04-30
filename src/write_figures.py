"""Generate all publication figures from both analyses.

Figures produced
----------------
consistency_analysis_rescience_c  (Ch. 1)
  fig1_model_comparison.pdf/png
  fig2_temperature_sensitivity.pdf/png
  fig8_cross_validation.pdf/png
  figS1_repro_vs_paper_length.pdf/png

rescience_c_gemini3_1_pro_T0_analysis  (Ch. 2)
  gemini3_1_pro_T0_score_distribution.pdf/png
  gemini3_1_pro_T0_structural_vs_content.pdf/png
  gemini3_1_pro_T0_paper_ranking.pdf/png
  gemini3_1_pro_T0_repro_by_year.pdf/png
  gemini3_1_pro_T0_node_counts_vs_repro.pdf/png
  gemini3_1_pro_T0_wiring_metrics.pdf/png
  gemini3_1_pro_T0_layer_content.pdf/png
  gemini3_1_pro_T0_metadata_richness.pdf/png
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.patches import Patch

from repro_scoring import (
    build_graph,
    load_runs,
    score_profile,
    wiring_metrics,
)

PROFILE_DIR = Path("data/experiments/consistency_checks/rescience_c")
T0_DIR      = Path("data/experiments/rescience_c_gemini3_1_pro_T0")
FIGURE_DIR  = Path("figures")
FIGURE_DIR.mkdir(exist_ok=True)

# ── shared style ──────────────────────────────────────────────────────────────
OKABE_ITO = ["#0072B2", "#D55E00", "#009E73", "#CC79A7",
             "#E69F00", "#56B4E9", "#F0E442", "#000000"]
BLUE   = "#0072B2"
ORANGE = "#D55E00"
GREEN  = "#009E73"

plt.rcParams.update({
    "font.family":          "sans-serif",
    "font.sans-serif":      ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size":            12,
    "axes.labelsize":       13,
    "axes.titlesize":       14,
    "xtick.labelsize":      11,
    "ytick.labelsize":      11,
    "legend.fontsize":      11,
    "axes.linewidth":       0.8,
    "xtick.major.width":    0.8,
    "ytick.major.width":    0.8,
    "xtick.major.size":     3.5,
    "ytick.major.size":     3.5,
    "axes.spines.top":      False,
    "axes.spines.right":    False,
    "legend.frameon":       False,
    "savefig.dpi":          600,
    "savefig.bbox":         "tight",
})

def save(name: str) -> None:
    FIGURE_DIR.joinpath(f"{name}.pdf").unlink(missing_ok=True)
    FIGURE_DIR.joinpath(f"{name}.png").unlink(missing_ok=True)
    plt.savefig(FIGURE_DIR / f"{name}.pdf")
    plt.savefig(FIGURE_DIR / f"{name}.png")
    plt.close()
    print(f"  saved {name}")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — consistency analysis
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Chapter 1: loading consistency runs …")

PAPER_META = {
    "2017_04_article.pdf": (4,  3_372),
    "2020_26_article.pdf": (8,  3_701),
    "2017_01_article.pdf": (15, 6_436),
    "2025_03_article.pdf": (20, 8_930),
    "2017_08_article.pdf": (11, 9_237),
    "2022_30_article.pdf": (18, 9_800),
    "2021_34_article.pdf": (28, 13_493),
    "2023_17_article.pdf": (24, 14_733),
    "2023_15_article.pdf": (30, 16_170),
    "2022_38_article.pdf": (34, 22_917),
}
meta = (
    pd.DataFrame.from_dict(PAPER_META, orient="index", columns=["n_pages", "n_words"])
    .rename_axis("paper").reset_index()
)
long = pd.DataFrame(load_runs(PROFILE_DIR)).merge(meta, on="paper", how="left")
print(f"  runs: {len(long):,}   models: {sorted(long['model'].unique())}")

agg = (
    long.groupby(["model", "paper", "n_pages", "n_words"], as_index=False)["repro_index"]
    .agg(mean="mean", std="std", n="count")
    .sort_values(["model", "n_words"])
    .assign(std=lambda df: df["std"].fillna(0.0))
)

# gpt-4.1 profile files were deleted from disk; rows recovered from git-cached
# notebook output (commit c14933b). Partial dataset: 3 of 10 papers only.
_gpt_rows = pd.DataFrame([
    {"model": "gpt-4.1", "paper": "2017_04_article.pdf", "n_pages":  4, "n_words":  3_372, "mean": 0.480639, "std": 0.134418, "n": 50},
    {"model": "gpt-4.1", "paper": "2020_26_article.pdf", "n_pages":  8, "n_words":  3_701, "mean": 0.611100, "std": 0.199793, "n": 48},
    {"model": "gpt-4.1", "paper": "2017_01_article.pdf", "n_pages": 15, "n_words":  6_436, "mean": 0.717959, "std": 0.023423, "n": 10},
])
agg = pd.concat([agg, _gpt_rows], ignore_index=True).sort_values(["model", "n_words"]).reset_index(drop=True)
print(f"  agg rows after gpt-4.1 injection: {len(agg)}  (gpt-4.1 partial: 3/10 papers)")

models      = sorted(agg["model"].unique())
colors      = {m: OKABE_ITO[i % len(OKABE_ITO)] for i, m in enumerate(models)}
paper_list  = sorted(agg["paper"].unique())
cmap10      = plt.get_cmap("tab10")
paper_color = {p: cmap10(i / max(len(paper_list) - 1, 1)) for i, p in enumerate(paper_list)}

# ── Fig 1 — model comparison ──────────────────────────────────────────────────
print("\n── Fig 1: model comparison")

data_by_model = [agg[agg["model"] == m]["mean"].values for m in models]

fig, ax = plt.subplots(figsize=(9.0, 5.2), constrained_layout=True)
ax.boxplot(
    data_by_model,
    positions=range(len(models)),
    widths=0.40,
    patch_artist=True,
    showfliers=False,
    medianprops={"color": "black", "linewidth": 2.0},
    boxprops={"facecolor": "#CCDDEF", "edgecolor": BLUE, "linewidth": 1.2},
    whiskerprops={"color": BLUE, "linewidth": 1.0},
    capprops={"color": BLUE, "linewidth": 1.0},
)
rng = np.random.default_rng(42)
for xi, m in enumerate(models):
    sub    = agg[agg["model"] == m].sort_values("paper")
    jitter = rng.uniform(-0.13, 0.13, size=len(sub))
    for (_, row), jit in zip(sub.iterrows(), jitter):
        ax.scatter(xi + jit, row["mean"], color=paper_color[row["paper"]],
                   s=62, zorder=4, edgecolors="white", linewidths=0.5)
ax.set_xticks(range(len(models)))
ax.set_xticklabels(models, fontsize=10, rotation=12, ha="right")
ax.set_ylabel("Mean repro_index (pooled over T \u00d7 samples)")
ax.set_ylim(0.35, 1.02)
ax.margins(x=0.10)
ax.legend(
    handles=[Patch(facecolor=paper_color[p], edgecolor="none",
                   label=p.removesuffix(".pdf")) for p in paper_list],
    title="Paper", title_fontsize=9, loc="lower right",
    fontsize=8.5, ncol=2, borderaxespad=0.4, handlelength=1.2,
)
save("fig1_model_comparison")

# ── Fig 2 — temperature sensitivity ───────────────────────────────────────────
print("── Fig 2: temperature sensitivity")

var_table = (
    long.groupby(["model", "paper", "n_words", "temperature"], as_index=False)["repro_index"]
    .std()
    .rename(columns={"repro_index": "std_repro"})
    .dropna(subset=["std_repro"])
)
models_panel = sorted(var_table["model"].unique())
norm_w = Normalize(vmin=var_table["n_words"].min(), vmax=var_table["n_words"].max())
cmap_v = plt.get_cmap("viridis")

fig, axes = plt.subplots(2, 3, figsize=(12.0, 6.8),
                          sharex=True, sharey=True, constrained_layout=True)
axes_flat = axes.flatten()
for idx, m in enumerate(models_panel):
    ax = axes_flat[idx]
    for _, grp in var_table[var_table["model"] == m].groupby("paper"):
        grp = grp.sort_values("temperature")
        ax.plot(grp["temperature"], grp["std_repro"],
                marker="o", markersize=3.8, linewidth=1.1,
                color=cmap_v(norm_w(grp["n_words"].iloc[0])), alpha=0.9)
    ax.set_title(m, fontsize=11)
    ax.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)
for j in range(len(models_panel), len(axes_flat)):
    axes_flat[j].set_axis_off()
sm = ScalarMappable(norm=norm_w, cmap=cmap_v)
sm.set_array([])
fig.colorbar(sm, ax=axes_flat[:len(models_panel)],
             location="right", shrink=0.85, pad=0.02, label="Paper length (words)")
fig.supxlabel("Temperature", fontsize=12)
fig.supylabel("Std of reproducibility index", fontsize=12)
save("fig2_temperature_sensitivity")

# ── Fig S1 — repro vs paper length ────────────────────────────────────────────
print("── Fig S1: repro vs paper length")

fig, ax = plt.subplots(figsize=(7.2, 5.0), constrained_layout=True)
for m in models:
    sub = agg[agg["model"] == m].sort_values("n_words")
    x, y, e = sub["n_words"].to_numpy(), sub["mean"].to_numpy(), sub["std"].to_numpy()
    ax.fill_between(x, y - e, y + e, color=colors[m], alpha=0.18, linewidth=0)
    ax.plot(x, y, marker="o", markersize=5.0, linewidth=1.6,
            color=colors[m], label=m, clip_on=False)
ax.set_xlabel("Paper length (words)")
ax.set_ylabel("Reproducibility index")
ax.set_ylim(0.3, 1)
ax.margins(x=0.02)
ax.legend(loc="lower right", borderaxespad=0.4, handlelength=1.8)
save("figS1_repro_vs_paper_length")

# ── Fig 8 — cross-notebook validation ─────────────────────────────────────────
print("── Fig 8: cross-notebook validation")

STEM_T0 = re.compile(r"^(?P<year>\d{4})_(?P<num>\d+)_article_T0_(?P<model>.+)$")
consistency_papers = set(long["paper"].unique())
t0_scores: dict[str, float] = {}
for path in sorted(T0_DIR.glob("*.profile.json")):
    stem = path.stem.removesuffix(".profile")
    m_   = STEM_T0.match(stem)
    if m_ is None:
        continue
    paper = f"{m_['year']}_{m_['num']}_article.pdf"
    if paper not in consistency_papers:
        continue
    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        continue
    t0_scores[paper] = score_profile(profile)["repro_index"]

cons_t0 = (
    long[(long["model"] == "gemini-3.1-pro-preview") & (long["temperature"] == 0.0)]
    .groupby("paper")["repro_index"]
    .agg(mean="mean", std="std", n="count")
    .reset_index()
    .assign(std=lambda d: d["std"].fillna(0.0))
)
cons_t0["t0_single"] = cons_t0["paper"].map(t0_scores)
cons_t0 = cons_t0.dropna(subset=["t0_single"]).sort_values("mean").reset_index(drop=True)

fig, ax = plt.subplots(figsize=(9.5, 4.8), constrained_layout=True)
x = range(len(cons_t0))
ax.errorbar(x, cons_t0["mean"], yerr=cons_t0["std"],
            fmt="none", color=BLUE, capsize=4, linewidth=1.4, capthick=1.4,
            label="Consistency band (mean \u00b1 std, 10 samples, T = 0)")
ax.scatter(x, cons_t0["mean"], color=BLUE, s=55, zorder=4,
           edgecolors="white", linewidths=0.5)
ax.scatter(x, cons_t0["t0_single"], color=ORANGE, marker="D", s=65, zorder=5,
           edgecolors="white", linewidths=0.5,
           label="Single-run T = 0 (gemini-3.1-pro-preview)")
ax.set_xticks(list(x))
ax.set_xticklabels([p.removesuffix(".pdf") for p in cons_t0["paper"]],
                   rotation=38, ha="right", fontsize=10)
ax.set_ylabel("Reproducibility index")
ax.set_ylim(0.35, 1.05)
ax.legend(loc="lower right", fontsize=10, borderaxespad=0.4)
save("fig8_cross_validation")

within = (
    (cons_t0["t0_single"] >= cons_t0["mean"] - cons_t0["std"]) &
    (cons_t0["t0_single"] <= cons_t0["mean"] + cons_t0["std"])
).sum()
print(f"  {within}/{len(cons_t0)} single-run scores within \u00b11 std of consistency mean")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — full-corpus T0 analysis
# ══════════════════════════════════════════════════════════════════════════════
print("\n── Chapter 2: loading T0 profiles …")

STEM_RE = re.compile(r"^(?P<year>\d{4})_(?P<num>\d+)_article_T0_(?P<model>.+)$")

def _layer_mean(items: list[dict]) -> float | None:
    if not items:
        return None
    return sum(int(it.get("reproducibility_score", 0)) for it in items) / len(items) / 100.0

rows: list[dict] = []
for path in sorted(T0_DIR.glob("*.profile.json")):
    stem = path.stem.removesuffix(".profile")
    m_   = STEM_RE.match(stem)
    if m_ is None:
        continue
    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        continue
    scores     = score_profile(profile)
    wm         = wiring_metrics(build_graph(profile))
    meta_p     = profile.get("metadata", {})
    src_items  = profile.get("nodes_source", [])
    proc_items = profile.get("nodes_process", [])
    snk_items  = profile.get("nodes_sink", [])
    n_open     = sum(1 for s in src_items if s.get("availability") == "open")
    rows.append({
        "paper":         f"{m_['year']}_{m_['num']}_article.pdf",
        "year":          int(m_["year"]),
        "has_repo":      bool(meta_p.get("repository_links")),
        "n_hyperparams": len(meta_p.get("hyperparameters", [])),
        **scores,
        **wm,
        "content_source":  _layer_mean(src_items),
        "content_process": _layer_mean(proc_items),
        "content_sink":    _layer_mean(snk_items),
        "pct_src_open":    n_open / len(src_items) if src_items else None,
    })

df = pd.DataFrame(rows).sort_values("repro_index", ascending=False).reset_index(drop=True)
print(f"  papers: {len(df)}")

# ── score distribution ─────────────────────────────────────────────────────────
print("── gemini3_1_pro_T0_score_distribution")

fig, axes = plt.subplots(1, 3, figsize=(12, 4.5), constrained_layout=True)
for ax, (col, label) in zip(axes, [
    ("repro_index", "Reproducibility index"),
    ("structural",  "Structural score"),
    ("content",     "Content score"),
]):
    ax.hist(df[col].dropna(), bins=25, color=BLUE, edgecolor="white", linewidth=0.5, alpha=0.85)
    mv = df[col].mean()
    ax.axvline(mv, color=ORANGE, linewidth=1.5, linestyle="--", label=f"Mean = {mv:.3f}")
    ax.set_xlabel(label)
    if ax is axes[0]:
        ax.set_ylabel("Count")
    ax.legend(fontsize=10)
fig.suptitle("Score distributions — gemini-3.1-pro-preview, T = 0", fontsize=14)
save("gemini3_1_pro_T0_score_distribution")

# ── Fig 3 — structural vs content ─────────────────────────────────────────────
print("── gemini3_1_pro_T0_structural_vs_content  [Fig 3]")

fig, ax = plt.subplots(figsize=(6.5, 5.8), constrained_layout=True)
norm_r = Normalize(vmin=df["repro_index"].min(), vmax=df["repro_index"].max())
sc = ax.scatter(df["structural"], df["content"],
                c=df["repro_index"], cmap="viridis", norm=norm_r,
                s=60, alpha=0.8, edgecolors="none")
lo = min(df["structural"].min(), df["content"].min()) - 0.03
hi = max(df["structural"].max(), df["content"].max()) + 0.03
ax.plot([lo, hi], [lo, hi], "k--", linewidth=0.9, alpha=0.4, label="y = x")
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
ax.set_xlabel("Structural score")
ax.set_ylabel("Content score")
ax.set_title("Structural vs content (colour = repro_index)")
ax.legend(fontsize=10)
fig.colorbar(sc, ax=ax, label="Reproducibility index", shrink=0.85, pad=0.02)
save("gemini3_1_pro_T0_structural_vs_content")

# ── paper ranking ──────────────────────────────────────────────────────────────
print("── gemini3_1_pro_T0_paper_ranking")

N = 15
combo = (
    pd.concat([df.head(N), df.tail(N)])
    .drop_duplicates("paper")
    .sort_values("repro_index")
    .assign(label=lambda d: d["paper"].str.removesuffix(".pdf"))
)
median_val = df["repro_index"].median()
bar_colors = [ORANGE if v < median_val else BLUE for v in combo["repro_index"]]
fig, ax = plt.subplots(figsize=(8.5, 8.5), constrained_layout=True)
ax.barh(combo["label"], combo["repro_index"], color=bar_colors, height=0.72)
ax.axvline(median_val, color="black", linewidth=1.0, linestyle="--",
           alpha=0.55, label=f"Median = {median_val:.3f}")
ax.set_xlabel("Reproducibility index")
ax.set_title(f"Top & bottom {N} papers by reproducibility index")
ax.legend(fontsize=10)
save("gemini3_1_pro_T0_paper_ranking")

# ── Fig 6 — repro by year ─────────────────────────────────────────────────────
print("── gemini3_1_pro_T0_repro_by_year  [Fig 6 / Annex A4]")

years = sorted(df["year"].unique())
year_data = [df[df["year"] == y]["repro_index"].values for y in years]
fig, ax = plt.subplots(figsize=(12, 5), constrained_layout=True)
ax.boxplot(year_data, positions=range(len(years)), patch_artist=True, showfliers=True,
           medianprops={"color": "black", "linewidth": 1.5},
           boxprops={"facecolor": BLUE, "alpha": 0.55, "edgecolor": BLUE},
           whiskerprops={"color": BLUE, "linewidth": 0.9},
           capprops={"color": BLUE, "linewidth": 0.9},
           flierprops={"marker": "o", "markersize": 3, "color": BLUE, "alpha": 0.5})
means_y = [np.mean(d) for d in year_data]
ax.plot(range(len(years)), means_y, "o-", color=ORANGE,
        markersize=5, linewidth=1.5, label="Mean", zorder=3)
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, rotation=45)
ax.set_xlabel("Publication year")
ax.set_ylabel("Reproducibility index")
ax.set_title("Reproducibility index by publication year")
ax.legend(fontsize=10)
save("gemini3_1_pro_T0_repro_by_year")

# ── node counts vs repro ───────────────────────────────────────────────────────
print("── gemini3_1_pro_T0_node_counts_vs_repro")

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), constrained_layout=True)
for ax, (col, label) in zip(axes, [
    ("n_source",  "# Source nodes"),
    ("n_process", "# Process nodes"),
    ("n_sink",    "# Sink nodes"),
]):
    ax.scatter(df[col], df["repro_index"], color=BLUE, alpha=0.60, s=40, edgecolors="none")
    r = df[[col, "repro_index"]].corr().iloc[0, 1]
    ax.set_xlabel(label)
    if ax is axes[0]:
        ax.set_ylabel("Reproducibility index")
    ax.set_title(f"r = {r:.3f}")
fig.suptitle("Node counts vs reproducibility index", fontsize=14)
save("gemini3_1_pro_T0_node_counts_vs_repro")

# ── Fig 5 — wiring metrics ────────────────────────────────────────────────────
print("── gemini3_1_pro_T0_wiring_metrics  [Fig 5 / Annex A3]")

wiring_cols = ["sources_consumed_ratio", "sinks_produced_ratio", "resolved_input_ratio",
               "source_to_sink_reachability", "lwcc_fraction"]
wiring_labels = ["Sources\nconsumed", "Sinks\nproduced", "Resolved\ninputs",
                 "Src\u2192sink\nreach", "LWCC\nfraction"]
means_wm = df[wiring_cols].mean()
stds_wm  = df[wiring_cols].std()

fig, ax = plt.subplots(figsize=(9, 4.5), constrained_layout=True)
x = np.arange(len(wiring_cols))
ax.bar(x, means_wm, yerr=stds_wm, color=BLUE, alpha=0.80, capsize=4,
       error_kw={"linewidth": 1.0, "ecolor": "black", "capthick": 1.0})
# highlight the weakest metric
ax.patches[wiring_cols.index("source_to_sink_reachability")].set_facecolor(ORANGE)
for i, (v, s) in enumerate(zip(means_wm, stds_wm)):
    ax.text(i, v + s + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(wiring_labels)
ax.set_ylabel("Mean score")
ax.set_ylim(0, 1.18)
ax.set_title("Structural wiring metrics \u2014 mean \u00b1 std across all papers")
save("gemini3_1_pro_T0_wiring_metrics")

# ── Fig 4 — layer content scores ──────────────────────────────────────────────
print("── gemini3_1_pro_T0_layer_content  [Fig 4]")

layer_cols   = ["content_source", "content_process", "content_sink"]
layer_labels = ["Sources", "Processes", "Sinks"]
layer_colors = [BLUE, ORANGE, GREEN]
layer_data   = [df[c].dropna().values for c in layer_cols]

fig, ax = plt.subplots(figsize=(7, 4.8), constrained_layout=True)
bp = ax.boxplot(layer_data, patch_artist=True, showfliers=True,
                medianprops={"color": "black", "linewidth": 1.5})
for patch, wh1, wh2, cap1, cap2, flier, color in zip(
    bp["boxes"],
    bp["whiskers"][::2], bp["whiskers"][1::2],
    bp["caps"][::2],     bp["caps"][1::2],
    bp["fliers"],
    layer_colors,
):
    patch.set(facecolor=color, alpha=0.65, edgecolor=color)
    for elem in (wh1, wh2, cap1, cap2):
        elem.set_color(color)
    flier.set(marker="o", markersize=3, color=color, alpha=0.5)
for i, (col, color) in enumerate(zip(layer_cols, layer_colors)):
    mean_v = df[col].mean()
    ax.text(i + 1, mean_v + 0.01, f"\u03bc={mean_v:.2f}",
            ha="center", va="bottom", fontsize=10, color=color)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(layer_labels)
ax.set_ylabel("Content reproducibility score (0\u20131)")
ax.set_title("Content score by node layer")
save("gemini3_1_pro_T0_layer_content")

# ── Fig 7 — metadata richness ─────────────────────────────────────────────────
print("── gemini3_1_pro_T0_metadata_richness  [Fig 7]")

from scipy import stats as _stats

fig, axes = plt.subplots(1, 2, figsize=(11, 5), constrained_layout=True)

# Panel A — repository availability
ax = axes[0]
n_no  = (~df["has_repo"]).sum()
n_yes = df["has_repo"].sum()
grp_no  = df[~df["has_repo"]]["repro_index"].values
grp_yes = df[ df["has_repo"]]["repro_index"].values
bp = ax.boxplot([grp_no, grp_yes], patch_artist=True, showfliers=True,
                medianprops={"color": "black", "linewidth": 1.5})
for patch, color in zip(bp["boxes"], [ORANGE, BLUE]):
    patch.set(facecolor=color, alpha=0.65, edgecolor=color)
for wh, color in zip(bp["whiskers"], [ORANGE, ORANGE, BLUE, BLUE]):
    wh.set_color(color)
for cap, color in zip(bp["caps"], [ORANGE, ORANGE, BLUE, BLUE]):
    cap.set_color(color)
for flier, color in zip(bp["fliers"], [ORANGE, BLUE]):
    flier.set(marker="o", markersize=3, color=color, alpha=0.5)
_, p_val = _stats.mannwhitneyu(grp_no, grp_yes, alternative="less")
sig = "***" if p_val < 0.001 else ("**" if p_val < 0.01 else ("*" if p_val < 0.05 else "n.s."))
y_top = max(grp_no.max(), grp_yes.max()) + 0.03
ax.plot([1, 2], [y_top, y_top], color="black", linewidth=0.9)
ax.text(1.5, y_top + 0.01, sig, ha="center", va="bottom", fontsize=12)
ax.set_xticks([1, 2])
ax.set_xticklabels([f"No repo\n(n={n_no})", f"Has repo\n(n={n_yes})"])
ax.set_ylabel("Reproducibility index")
ax.set_title("Code repository availability")

# Panel B — hyperparameter count
ax = axes[1]
ax.scatter(df["n_hyperparams"], df["repro_index"], color=BLUE, alpha=0.65, s=45, edgecolors="none")
r = df[["n_hyperparams", "repro_index"]].corr().iloc[0, 1]
ax.set_xlabel("# Hyperparameters reported")
ax.set_ylabel("Reproducibility index")
ax.set_title(f"Hyperparameter reporting (r = {r:.3f})")

save("gemini3_1_pro_T0_metadata_richness")
print(f"  Mann-Whitney p = {p_val:.4f}  ({sig})")

print("\n\u2714 All figures written to", FIGURE_DIR.resolve())
