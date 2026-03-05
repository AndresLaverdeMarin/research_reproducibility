###############################################################################
### Reproduce Main Figures from:
### "Towards zero CO2 emissions: Insights from EU vehicle on-board data"
### Suarez, Tansini, Ktistakis, Marin, Komnos, Pavlovic & Fontaras (2025)
###############################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

FIGURES_DIR = "figures"
import os
os.makedirs(FIGURES_DIR, exist_ok=True)

###############################################################################
# Load and Prepare Data
###############################################################################
print("Loading data (7.7M vehicles)...")
df = pd.read_csv('obfcm_data.csv', low_memory=False)
print(f"  Loaded: {len(df):,} rows")

def get_fuel_simple(ft):
    if pd.isna(ft):
        return ft
    if 'PETROL' in ft:
        return 'Petrol'
    if 'DIESEL' in ft:
        return 'Diesel'
    return ft

df['fuel'] = df['EEA_Ft'].apply(get_fuel_simple)
pt_map = {'M': 'ICEV', 'H': 'HEV', 'P': 'PHEV'}
df['powertrain'] = df['EEA_Fm'].map(pt_map)
df['pt_fuel'] = df['powertrain'] + ' ' + df['fuel']

df['age_years'] = df['OBFCM_ReportingPeriod'] - df['EEA_year'] + 0.5
df['annual_mileage_km'] = df['OBFCM_TotLifetimeDist_km'] / df['age_years']
df.loc[df['annual_mileage_km'] > 200000, 'annual_mileage_km'] = np.nan
df.loc[df['annual_mileage_km'] < 100, 'annual_mileage_km'] = np.nan
df.loc[df['RW_eds'] > 100, 'RW_eds'] = np.nan
df['power_to_mass'] = df['EEA_Ep'] / df['EEA_M'] * 1000  # W/kg

mask_icevhev = df['EEA_Fm'].isin(['M', 'H'])
mask_outlier = (df['RW_CO2'] > (df['EEA_Ewltp'] - 30)) & (df['RW_CO2'] < 3 * df['EEA_Ewltp'])
df_clean = df[~mask_icevhev | mask_outlier].copy()
print(f"  After outlier filter: {len(df_clean):,} rows")

# Paper colors: Blue=Petrol, Red=Diesel, Grey=TA, Green=PHEV RW
colors = {'Petrol': '#1f77b4', 'Diesel': '#d62728'}
colors_light = {'Petrol': '#aec7e8', 'Diesel': '#ff9896'}
pt_order = ['ICEV', 'HEV', 'PHEV']

print("Data ready.\n")


###############################################################################
# FIGURE 1: RW CO2 and TA CO2 distributions
# Overlaid histograms + inline box plots + vertical average lines
###############################################################################
print("Generating Figure 1...")

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle('Figure 1: Real-world (RW CO$_2$) and official (TA CO$_2$) emissions distributions',
             fontsize=13, fontweight='bold', y=0.98)

for j, pt in enumerate(pt_order):
    for i, fuel in enumerate(['Petrol', 'Diesel']):
        ax = axes[i, j]
        subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]
        if len(subset) == 0:
            ax.set_visible(False)
            continue

        rw = subset['RW_CO2'].clip(0, 400)
        ta = subset['EEA_Ewltp'].clip(0, 400)
        rw_color = '#2ca02c' if pt == 'PHEV' else '#1f77b4'

        bins = np.linspace(0, 400, 80)

        # Histograms
        ax.hist(ta, bins=bins, density=True, alpha=0.4, color='grey',
                label=f'TA CO$_2$')
        ax.hist(rw, bins=bins, density=True, alpha=0.5, color=rw_color,
                label=f'RW CO$_2$')

        # Vertical average lines
        ax.axvline(ta.mean(), color='grey', linestyle='--', linewidth=1.5,
                   label=f'TA avg: {ta.mean():.0f}')
        ax.axvline(rw.mean(), color=rw_color, linestyle='--', linewidth=1.5,
                   label=f'RW avg: {rw.mean():.0f}')

        # Inline box plots (within histogram area, at ~80-90% of y range)
        ylim = ax.get_ylim()[1]
        ax.set_ylim(top=ylim * 1.4)
        bp_y_ta = ylim * 1.25
        bp_y_rw = ylim * 1.1
        bp_w = ylim * 0.08

        bp = ax.boxplot([ta.values], positions=[bp_y_ta], vert=False,
                       widths=bp_w, patch_artist=True, showfliers=False,
                       medianprops=dict(color='black', linewidth=1.5),
                       whiskerprops=dict(color='grey'),
                       capprops=dict(color='grey'))
        bp['boxes'][0].set_facecolor('grey')
        bp['boxes'][0].set_alpha(0.5)

        bp2 = ax.boxplot([rw.values], positions=[bp_y_rw], vert=False,
                        widths=bp_w, patch_artist=True, showfliers=False,
                        medianprops=dict(color='black', linewidth=1.5),
                        whiskerprops=dict(color=rw_color),
                        capprops=dict(color=rw_color))
        bp2['boxes'][0].set_facecolor(rw_color)
        bp2['boxes'][0].set_alpha(0.5)

        ax.set_title(f'{fuel} {pt} (n={len(subset):,})', fontsize=11)
        ax.set_xlabel('CO$_2$ emissions [g/km]')
        if j == 0:
            ax.set_ylabel('Probability Density')
        ax.legend(fontsize=6, loc='upper right', framealpha=0.8)
        ax.set_xlim(0, 400 if pt != 'PHEV' else 400)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f"{FIGURES_DIR}/Figure_1_rw_ta_distributions.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 1 saved.")


###############################################################################
# FIGURE 2: Country-specific RW and TA CO2 emissions
# 3 rows x 1 col, grouped bars, proportional circles, EU-avg dashed lines
# Countries ordered by average temperature (approximated by latitude proxy)
###############################################################################
print("Generating Figure 2...")

# Approximate temperature ordering (south -> north) for EU countries
temp_order = ['MT', 'CY', 'GR', 'PT', 'ES', 'IT', 'HR', 'SI', 'BG', 'RO',
              'HU', 'SK', 'CZ', 'AT', 'FR', 'BE', 'LU', 'DE', 'NL', 'PL',
              'IE', 'DK', 'LT', 'LV', 'EE', 'SE', 'FI', 'NO', 'IS']

fig, axes = plt.subplots(3, 1, figsize=(16, 14))
fig.suptitle('Figure 2: Country-specific real-world (dark) and official CO$_2$ emissions (light)',
             fontsize=13, fontweight='bold', y=0.99)

for j, pt in enumerate(pt_order):
    ax = axes[j]
    subset = df_clean[df_clean['powertrain'] == pt]

    # Get country stats for both fuels
    country_data = {}
    for fuel in ['Petrol', 'Diesel']:
        fsub = subset[subset['fuel'] == fuel]
        if len(fsub) < 50:
            continue
        cs = fsub.groupby('EEA_MS').agg(
            rw_median=('RW_CO2', 'median'),
            ta_median=('EEA_Ewltp', 'median'),
            count=('RW_CO2', 'size')
        ).reset_index()
        cs = cs[cs['count'] >= 30]
        country_data[fuel] = cs

    # Get ordered list of countries present in data
    all_countries_in_data = set()
    for fuel in country_data:
        all_countries_in_data.update(country_data[fuel]['EEA_MS'].tolist())
    ordered_countries = [c for c in temp_order if c in all_countries_in_data]

    x = np.arange(len(ordered_countries))
    total_width = 0.8
    n_fuels = len(country_data)
    bar_width = total_width / (n_fuels * 2)  # 2 bars per fuel (TA + RW)

    for fi, fuel in enumerate(['Petrol', 'Diesel']):
        if fuel not in country_data:
            continue
        cs = country_data[fuel].set_index('EEA_MS')
        offset = (fi - 0.5) * total_width / n_fuels

        ta_vals = [cs.loc[c, 'ta_median'] if c in cs.index else 0 for c in ordered_countries]
        rw_vals = [cs.loc[c, 'rw_median'] if c in cs.index else 0 for c in ordered_countries]
        counts = [cs.loc[c, 'count'] if c in cs.index else 0 for c in ordered_countries]

        # TA bars (light)
        ax.bar(x + offset - bar_width / 2, ta_vals, bar_width,
               color=colors_light[fuel], edgecolor='white', linewidth=0.3)
        # RW bars (dark)
        ax.bar(x + offset + bar_width / 2, rw_vals, bar_width,
               color=colors[fuel], edgecolor='white', linewidth=0.3)

        # Proportional circles for sample size on top of RW bars
        max_count = max(counts) if max(counts) > 0 else 1
        for k, c in enumerate(ordered_countries):
            if counts[k] > 0:
                size = max(8, 80 * (counts[k] / max_count))
                ax.scatter(x[k] + offset + bar_width / 2, rw_vals[k] + 3,
                          s=size, color=colors[fuel], alpha=0.6,
                          edgecolors='black', linewidths=0.3, zorder=5)

    # EU-average dashed lines
    for fuel in ['Petrol', 'Diesel']:
        fsub = subset[subset['fuel'] == fuel]
        if len(fsub) > 100:
            eu_avg_rw = fsub['RW_CO2'].median()
            ax.axhline(eu_avg_rw, color=colors[fuel], linestyle='--',
                      linewidth=1, alpha=0.7, label=f'{fuel} EU median: {eu_avg_rw:.0f}')

    ax.set_xticks(x)
    ax.set_xticklabels(ordered_countries, rotation=45, ha='right', fontsize=8)
    ax.set_ylabel('CO$_2$ emissions [g/km]')
    ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(axis='y', alpha=0.3)

    # Custom legend
    patches = []
    for fuel in ['Petrol', 'Diesel']:
        if fuel in country_data:
            patches.append(mpatches.Patch(color=colors_light[fuel], label=f'{fuel} TA'))
            patches.append(mpatches.Patch(color=colors[fuel], label=f'{fuel} RW'))
    ax.legend(handles=patches + ax.get_legend_handles_labels()[0][-2:],
             fontsize=7, loc='upper left', ncol=3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_2_country_emissions.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 2 saved.")


###############################################################################
# FIGURE 3: Annual mileage by country
# Horizontal bars, vertical median lines, fleet-size circles
###############################################################################
print("Generating Figure 3...")

fig, axes = plt.subplots(3, 1, figsize=(14, 16))
fig.suptitle('Figure 3: Average annual mileages for different countries of registration',
             fontsize=13, fontweight='bold', y=0.99)

for j, pt in enumerate(pt_order):
    ax = axes[j]
    subset = df_clean[(df_clean['powertrain'] == pt) & df_clean['annual_mileage_km'].notna()]

    fuel_data = {}
    for fuel in ['Petrol', 'Diesel']:
        fsub = subset[subset['fuel'] == fuel]
        if len(fsub) < 50:
            continue
        cm = fsub.groupby('EEA_MS').agg(
            median_km=('annual_mileage_km', 'median'),
            count=('annual_mileage_km', 'size')
        ).reset_index()
        cm = cm[cm['count'] >= 20]
        fuel_data[fuel] = cm.set_index('EEA_MS')

    # Merge countries and sort by petrol median
    all_c = set()
    for fd in fuel_data.values():
        all_c.update(fd.index.tolist())
    sort_fuel = 'Petrol' if 'Petrol' in fuel_data else 'Diesel'
    sorted_countries = sorted(all_c,
        key=lambda c: fuel_data[sort_fuel].loc[c, 'median_km'] if c in fuel_data[sort_fuel].index else 0)

    y = np.arange(len(sorted_countries))
    bar_h = 0.35

    for fi, fuel in enumerate(['Petrol', 'Diesel']):
        if fuel not in fuel_data:
            continue
        fd = fuel_data[fuel]
        vals = [fd.loc[c, 'median_km'] / 1000 if c in fd.index else 0 for c in sorted_countries]
        counts = [fd.loc[c, 'count'] if c in fd.index else 0 for c in sorted_countries]
        offset = -bar_h / 2 if fuel == 'Petrol' else bar_h / 2

        ax.barh(y + offset, vals, height=bar_h, color=colors[fuel], alpha=0.8, label=fuel)

        # Fleet-size circles at end of bars
        max_count = max(counts) if max(counts) > 0 else 1
        for k in range(len(sorted_countries)):
            if counts[k] > 0:
                size = max(10, 120 * (counts[k] / max_count))
                ax.scatter(vals[k] + 0.3, y[k] + offset, s=size,
                          color=colors[fuel], alpha=0.5, edgecolors='black',
                          linewidths=0.3, zorder=5)

    # Fleet median vertical dashed lines
    for fuel in ['Petrol', 'Diesel']:
        if fuel not in fuel_data:
            continue
        fsub = subset[subset['fuel'] == fuel]
        fleet_median = fsub['annual_mileage_km'].median() / 1000
        ax.axvline(fleet_median, color=colors[fuel], linestyle='--',
                  linewidth=1.5, alpha=0.7,
                  label=f'{fuel} median: {fleet_median:.1f}k')

    ax.set_yticks(y)
    ax.set_yticklabels(sorted_countries, fontsize=8)
    ax.set_xlabel('Annual distance [10$^3$ km/year]')
    ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
    ax.legend(fontsize=8, loc='lower right')
    ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_3_annual_mileage_country.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 3 saved.")


###############################################################################
# FIGURE 4: RW CO2 and gap vs official TA CO2
# Binned BOX PLOTS + linear regression lines + gap=0 line
###############################################################################
print("Generating Figure 4...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Figure 4: Real-world CO$_2$ (top) and gap (bottom) vs. official CO$_2$ emissions',
             fontsize=13, fontweight='bold', y=0.99)

for j, pt in enumerate(pt_order):
    if pt == 'PHEV':
        ta_bins = np.arange(0, 120, 10)
    else:
        ta_bins = np.arange(50, 300, 15)

    for row, y_col, ylabel in [(0, 'RW_CO2', 'RW CO$_2$ [g/km]'),
                                (1, 'gap', 'Gap [g/km]')]:
        ax = axes[row, j]

        for fuel in ['Petrol', 'Diesel']:
            subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)].copy()
            if len(subset) < 200:
                continue

            subset['ta_bin'] = pd.cut(subset['EEA_Ewltp'], bins=ta_bins)
            subset = subset.dropna(subset=['ta_bin'])

            # Group into bins for box plots
            groups = []
            positions = []
            for b in sorted(subset['ta_bin'].unique()):
                grp = subset[subset['ta_bin'] == b][y_col].dropna()
                if len(grp) >= 20:
                    groups.append(grp.values)
                    positions.append(b.mid)

            if not groups:
                continue

            # Offset positions for petrol vs diesel
            offset = -2 if fuel == 'Petrol' else 2
            pos_shifted = [p + offset for p in positions]

            bp = ax.boxplot(groups, positions=pos_shifted, widths=4,
                           patch_artist=True, showfliers=False,
                           medianprops=dict(color='black', linewidth=1),
                           whiskerprops=dict(color=colors[fuel], alpha=0.6),
                           capprops=dict(color=colors[fuel], alpha=0.6))
            for box in bp['boxes']:
                box.set_facecolor(colors[fuel])
                box.set_alpha(0.5)

            # Linear regression line through medians
            medians = [np.median(g) for g in groups]
            if len(positions) > 2:
                z = np.polyfit(positions, medians, 1)
                xfit = np.linspace(min(positions), max(positions), 50)
                ax.plot(xfit, np.polyval(z, xfit), '-', color=colors[fuel],
                       linewidth=2, label=fuel, zorder=10)

        # gap=0 reference line (top panels: diagonal 1:1; bottom: horizontal 0)
        if row == 0:
            lims = ax.get_xlim()
            ax.plot(lims, lims, '--', color='grey', alpha=0.5, label='gap = 0')
        else:
            ax.axhline(0, color='grey', linestyle='--', alpha=0.5)

        # Average TA vertical dotted line
        for fuel in ['Petrol', 'Diesel']:
            fsub = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]
            if len(fsub) > 100:
                avg_ta = fsub['EEA_Ewltp'].mean()
                ax.axvline(avg_ta, color=colors[fuel], linestyle=':', alpha=0.4)

        ax.set_ylabel(ylabel)
        if row == 0:
            ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
        if row == 1:
            ax.set_xlabel('Official CO$_2$ emissions [g/km]')
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_4_rw_gap_vs_ta.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 4 saved.")


###############################################################################
# FIGURE 5: RW CO2 and gap vs total driven distance
# Binned BOX PLOTS + sample size annotations + green EDS=50% line for PHEV
###############################################################################
print("Generating Figure 5...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Figure 5: Real-world CO$_2$ (top) and gap (bottom) vs. total driven distance',
             fontsize=13, fontweight='bold', y=0.99)

dist_bins = np.arange(0, 100000, 5000)

for j, pt in enumerate(pt_order):
    for row, y_col, ylabel in [(0, 'RW_CO2', 'RW CO$_2$ [g/km]'),
                                (1, 'gap', 'Gap [g/km]')]:
        ax = axes[row, j]

        for fuel in ['Petrol', 'Diesel']:
            subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)].copy()
            if len(subset) < 200:
                continue

            subset['dist_bin'] = pd.cut(subset['OBFCM_TotLifetimeDist_km'], bins=dist_bins)
            subset = subset.dropna(subset=['dist_bin'])

            groups = []
            positions = []
            counts_per_bin = []
            for b in sorted(subset['dist_bin'].unique()):
                grp = subset[subset['dist_bin'] == b][y_col].dropna()
                if len(grp) >= 20:
                    groups.append(grp.values)
                    positions.append(b.mid)
                    counts_per_bin.append(len(grp))

            if not groups:
                continue

            offset = -1000 if fuel == 'Petrol' else 1000
            pos_shifted = [p + offset for p in positions]

            bp = ax.boxplot(groups, positions=pos_shifted, widths=2000,
                           patch_artist=True, showfliers=False,
                           medianprops=dict(color='black', linewidth=1),
                           whiskerprops=dict(color=colors[fuel], alpha=0.6),
                           capprops=dict(color=colors[fuel], alpha=0.6))
            for box in bp['boxes']:
                box.set_facecolor(colors[fuel])
                box.set_alpha(0.5)

            # Sample size annotations (top row only, for petrol)
            if row == 0 and fuel == 'Petrol':
                for k, (p, cnt) in enumerate(zip(positions, counts_per_bin)):
                    if k % 2 == 0:  # every other bin to avoid crowding
                        ax.text(p, ax.get_ylim()[1] * 0.98 if ax.get_ylim()[1] > 0 else 300,
                               f'{cnt//1000}k' if cnt >= 1000 else str(cnt),
                               ha='center', fontsize=5, color='grey', alpha=0.7)

        # Green line for PHEV EDS=50% ± 5%
        if pt == 'PHEV' and row == 0:
            phev_sub = df_clean[(df_clean['powertrain'] == 'PHEV') &
                               (df_clean['RW_eds'] >= 45) & (df_clean['RW_eds'] <= 55)].copy()
            if len(phev_sub) > 50:
                phev_sub['dist_bin'] = pd.cut(phev_sub['OBFCM_TotLifetimeDist_km'], bins=dist_bins)
                eds_medians = phev_sub.groupby('dist_bin', observed=True)['RW_CO2'].median().dropna()
                eds_positions = [interval.mid for interval in eds_medians.index]
                ax.plot(eds_positions, eds_medians.values, 's-', color='green',
                       markersize=4, linewidth=1.5, label='EDS ~50%', zorder=10)

        ax.set_ylabel(ylabel)
        if row == 0:
            ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
        if row == 1:
            ax.set_xlabel('Lifetime mileage [km]')
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x/1000:.0f}k'))
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_5_rw_gap_vs_mileage.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 5 saved.")


###############################################################################
# FIGURE 7: Variable importance – LMG R² decomposition (Grömping, 2015)
# Equivalent to R's relaimpo::calc.relimp(type="lmg").
# Uses the covariance-matrix approach for computational efficiency.
# Blue=baseline (Model II), Red=extended (Model III), with R² annotations.
###############################################################################
print("Generating Figure 7...")
from collections import OrderedDict
from itertools import combinations
from math import factorial


def compute_lmg(data, predictor_groups, target, sample_size=200000):
    """
    LMG (Lindeman, Merenda, Gold) R² decomposition.

    Averages each predictor group's marginal R² contribution across all p!
    orderings of group entry.  Uses the covariance-matrix shortcut so that
    the 2^p subset R² values are each computed in O(p³) instead of O(n·p²).

    Parameters
    ----------
    data : DataFrame
    predictor_groups : OrderedDict  {group_name: [column_names]}
    target : str
    sample_size : int

    Returns
    -------
    lmg : dict  {group_name: R² contribution}   (values sum to full R²)
    full_r2 : float
    """
    # Map group names to column-index ranges
    all_cols = []
    grp_idx = {}
    ci = 0
    for name, cols in predictor_groups.items():
        grp_idx[name] = list(range(ci, ci + len(cols)))
        all_cols.extend(cols)
        ci += len(cols)

    sub = data[all_cols + [target]].dropna()
    if len(sub) < 200:
        return {n: 0.0 for n in predictor_groups}, 0.0
    if len(sub) > sample_size:
        sub = sub.sample(sample_size, random_state=42)

    X = sub[all_cols].values.astype(np.float64)
    y = sub[target].values.astype(np.float64)

    # Centre (equivalent to fitting with intercept)
    X = X - X.mean(axis=0)
    yc = y - y.mean()
    ss_tot = yc @ yc

    # Precompute cross-products — O(n·p²), done once
    XtX = X.T @ X
    Xty = X.T @ yc

    gnames = list(predictor_groups.keys())
    p = len(gnames)

    def r2_sub(gi_set):
        """R² for a subset of predictor groups."""
        if not gi_set:
            return 0.0
        ci_list = []
        for g in gi_set:
            ci_list.extend(grp_idx[gnames[g]])
        ci_arr = np.array(ci_list)
        A = XtX[np.ix_(ci_arr, ci_arr)]
        b = Xty[ci_arr]
        try:
            beta = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            beta = np.linalg.lstsq(A, b, rcond=None)[0]
        return max(0.0, float(b @ beta) / ss_tot)

    # Cache R² for every 2^p subset
    cache = {}
    for sz in range(p + 1):
        for combo in combinations(range(p), sz):
            cache[frozenset(combo)] = r2_sub(combo)

    # LMG: weighted average of marginal contributions
    lmg = {}
    for i in range(p):
        val = 0.0
        others = [j for j in range(p) if j != i]
        for sz in range(p):
            for S in combinations(others, sz):
                fs = frozenset(S)
                marginal = cache[fs | {i}] - cache[fs]
                w = factorial(sz) * factorial(p - sz - 1) / factorial(p)
                val += w * marginal
        lmg[gnames[i]] = val

    return lmg, cache[frozenset(range(p))]


# --- Prepare additional columns for LMG ------------------------------------
print("  Preparing variables for LMG decomposition...")
df_fig7 = df_clean.copy()

# Vehicle volume [m³] — dimensions already in metres
df_fig7['volume'] = (df_fig7['vdb_vehicle_length']
                     * df_fig7['vdb_vehicle_width']
                     * df_fig7['vdb_vehicle_height'])

# Binary dummies
df_fig7['fuel_petrol'] = (df_fig7['fuel'] == 'Petrol').astype(float)
df_fig7['pt_hev'] = (df_fig7['EEA_Fm'] == 'H').astype(float)

# Country dummies (drop_first → reference category)
country_dummies = pd.get_dummies(df_fig7['EEA_MS'], prefix='c',
                                 drop_first=True, dtype=float)
country_cols = list(country_dummies.columns)
df_fig7 = pd.concat([df_fig7, country_dummies], axis=1)

# --- Predictor groups per model (match paper's Table E1 / Fig. 7) ----------

# Model I-a: TA CO2 (ICEV/HEV)
ta_icevhev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Powertrain',          ['pt_hev']),
    ('Year',                ['EEA_year']),
])

# Model I-b: TA CO2 (PHEV)
ta_phev = OrderedDict([
    ('Electric range [km]', ['EEA_Zr']),
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Year',                ['EEA_year']),
])

# Model II-a: RW CO2 baseline (ICEV/HEV)
rw_base_icevhev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Powertrain',          ['pt_hev']),
    ('Year',                ['EEA_year']),
    ('Country',             country_cols),
    ('Mileage [km]',        ['OBFCM_TotLifetimeDist_km']),
])

# Model III-a: RW CO2 extended (ICEV/HEV) = baseline + TA CO2
rw_ext_icevhev = OrderedDict(list(rw_base_icevhev.items()) + [
    ('TA CO$_2$ [g/km]',    ['EEA_Ewltp']),
])

# Model II-b: RW CO2 baseline (PHEV)
rw_base_phev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Electric range [km]', ['EEA_Zr']),
    ('Year',                ['EEA_year']),
    ('Country',             country_cols),
    ('Mileage [km]',        ['OBFCM_TotLifetimeDist_km']),
])

# Model III-b: RW CO2 extended (PHEV) = baseline + TA CO2 + EDS
rw_ext_phev = OrderedDict(list(rw_base_phev.items()) + [
    ('TA CO$_2$ [g/km]',    ['EEA_Ewltp']),
    ('EDS [%]',             ['RW_eds']),
])

# --- Compute LMG and plot --------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Figure 7: Variable importance (LMG decomposition) of official '
             '(top) and real-world (bottom) CO$_2$ emissions',
             fontsize=13, fontweight='bold', y=0.99)

for col_idx, (pt_mask, pt_label, ta_grp, base_grp, ext_grp) in enumerate([
    (df_fig7['EEA_Fm'].isin(['M', 'H']), 'ICEV / HEV',
     ta_icevhev, rw_base_icevhev, rw_ext_icevhev),
    (df_fig7['EEA_Fm'] == 'P', 'PHEV',
     ta_phev, rw_base_phev, rw_ext_phev),
]):
    subset = df_fig7[pt_mask].copy()
    print(f"  {pt_label}: {len(subset):,} vehicles")

    # --- Top row: TA CO2 (Model I) -----------------------------------------
    ax = axes[0, col_idx]
    print(f"    Computing LMG for TA CO$_2$ ...")
    lmg_ta, r2_ta = compute_lmg(subset, ta_grp, 'EEA_Ewltp')

    sorted_vars = sorted(lmg_ta, key=lambda k: lmg_ta[k])
    vals = [lmg_ta[v] * 100 for v in sorted_vars]
    y_pos = np.arange(len(sorted_vars))

    ax.barh(y_pos, vals, color='steelblue', alpha=0.85, height=0.6)
    for i, v in enumerate(vals):
        if v > 1:
            ax.text(v + 0.5, i, f'{v:.0f}%', va='center', fontsize=8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_vars, fontsize=9)
    ax.set_xlabel('Variability explained [%]')
    ax.set_title(f'TA CO$_2$ — {pt_label} (Model I)', fontsize=11,
                 fontweight='bold')
    ax.text(0.97, 0.05, f'R² = {r2_ta*100:.0f}%',
            transform=ax.transAxes, ha='right', fontsize=10,
            fontstyle='italic',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax.grid(axis='x', alpha=0.3)

    # --- Bottom row: RW CO2 baseline (II) + extended (III) -----------------
    ax = axes[1, col_idx]
    print(f"    Computing LMG for RW CO$_2$ baseline ...")
    lmg_base, r2_base = compute_lmg(subset, base_grp, 'RW_CO2')
    print(f"    Computing LMG for RW CO$_2$ extended ...")
    lmg_ext, r2_ext = compute_lmg(subset, ext_grp, 'RW_CO2')

    all_vars = list(ext_grp.keys())
    sorted_vars = sorted(all_vars, key=lambda k: lmg_ext.get(k, 0))
    y_pos = np.arange(len(sorted_vars))
    bar_h = 0.35

    base_vals = [lmg_base.get(v, 0) * 100 for v in sorted_vars]
    ext_vals = [lmg_ext.get(v, 0) * 100 for v in sorted_vars]

    ax.barh(y_pos - bar_h/2, base_vals, height=bar_h, color='steelblue',
            alpha=0.85, label=f'Baseline II (R²={r2_base*100:.0f}%)')
    ax.barh(y_pos + bar_h/2, ext_vals, height=bar_h, color='coral',
            alpha=0.85, label=f'Extended III (R²={r2_ext*100:.0f}%)')

    for i, v in enumerate(ext_vals):
        if v > 2:
            ax.text(v + 0.3, y_pos[i] + bar_h/2, f'{v:.0f}%',
                    va='center', fontsize=7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_vars, fontsize=9)
    ax.set_xlabel('Variability explained [%]')
    ax.set_title(f'RW CO$_2$ — {pt_label} (Models II & III)',
                 fontsize=11, fontweight='bold')
    ax.legend(fontsize=8, loc='lower right')
    ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_7_variable_importance.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure 7 saved.")


###############################################################################
# FIGURE A1: Fleet composition per country
# Stacked bars (left: by year, right: powertrain share)
###############################################################################
print("Generating Figure A1...")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Figure A1: Composition of the sampled fleet per country',
             fontsize=13, fontweight='bold', y=0.99)

ax = axes[0]
year_colors = {2021: '#1f77b4', 2022: '#ff7f0e', 2023: '#9467bd'}
country_year = df_clean.groupby(['EEA_MS', 'EEA_year']).size().unstack(fill_value=0)
for yr in [2021, 2022, 2023]:
    if yr not in country_year.columns:
        country_year[yr] = 0
country_year = country_year[[2021, 2022, 2023]]
country_year = country_year.loc[country_year.sum(axis=1).sort_values(ascending=True).index]
country_year.plot(kind='barh', stacked=True, ax=ax, color=[year_colors[y] for y in [2021, 2022, 2023]])
ax.set_xlabel('Number of vehicles')
ax.set_title('Total monitored vehicles by registration year')
ax.legend(title='Year')
ax.grid(axis='x', alpha=0.3)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x/1000:.0f}k'))

ax = axes[1]
country_pt = df_clean.groupby(['EEA_MS', 'powertrain']).size().unstack(fill_value=0)
for c in pt_order:
    if c not in country_pt.columns:
        country_pt[c] = 0
country_pt = country_pt[pt_order]
country_pt = country_pt.loc[country_year.index]  # same country order
country_pct = country_pt.div(country_pt.sum(axis=1), axis=0) * 100
country_pct.plot(kind='barh', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax.set_xlabel('Powertrain share [%]')
ax.set_title('Powertrain distribution per country')
ax.legend(title='Powertrain')
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_A1_fleet_composition.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure A1 saved.")


###############################################################################
# FIGURE C1: RW CO2 vs Vehicle Mass
# Binned box plots + regression lines + sample-size circles + avg mass lines
# 2 rows: top RW-CO2, bottom Gap
###############################################################################
print("Generating Figure C1...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Figure C1: Real-world CO$_2$ emission variability vs. vehicle mass',
             fontsize=13, fontweight='bold', y=0.99)

mass_bins = np.arange(900, 2800, 100)

for j, pt in enumerate(pt_order):
    for row, y_col, ylabel in [(0, 'RW_CO2', 'RW CO$_2$ [g/km]'),
                                (1, 'gap', 'Gap [g/km]')]:
        ax = axes[row, j]

        for fuel in ['Petrol', 'Diesel']:
            subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)].copy()
            if len(subset) < 200:
                continue

            subset['mass_bin'] = pd.cut(subset['EEA_M'], bins=mass_bins)
            subset = subset.dropna(subset=['mass_bin'])

            groups = []
            positions = []
            counts = []
            for b in sorted(subset['mass_bin'].unique()):
                grp = subset[subset['mass_bin'] == b][y_col].dropna()
                if len(grp) >= 20:
                    groups.append(grp.values)
                    positions.append(b.mid)
                    counts.append(len(grp))

            if not groups:
                continue

            offset = -20 if fuel == 'Petrol' else 20
            pos_shifted = [p + offset for p in positions]

            bp = ax.boxplot(groups, positions=pos_shifted, widths=35,
                           patch_artist=True, showfliers=False,
                           medianprops=dict(color='black', linewidth=1),
                           whiskerprops=dict(color=colors[fuel], alpha=0.6),
                           capprops=dict(color=colors[fuel], alpha=0.6))
            for box in bp['boxes']:
                box.set_facecolor(colors[fuel])
                box.set_alpha(0.5)

            # Regression line through medians
            medians = [np.median(g) for g in groups]
            if len(positions) > 2:
                z = np.polyfit(positions, medians, 1)
                xfit = np.linspace(min(positions), max(positions), 50)
                slope_100 = z[0] * 100  # per 100 kg
                ax.plot(xfit, np.polyval(z, xfit), '-', color=colors[fuel],
                       linewidth=2, label=f'{fuel} ({slope_100:+.1f} g/km per 100kg)',
                       zorder=10)

            # Sample size circles at top (row 0 only)
            if row == 0:
                max_c = max(counts) if max(counts) > 0 else 1
                ylim = ax.get_ylim()
                for k in range(len(positions)):
                    size = max(8, 80 * (counts[k] / max_c))
                    ax.scatter(positions[k] + offset, max(medians) + 20,
                              s=size, color=colors[fuel], alpha=0.3,
                              edgecolors='none', zorder=3)

            # Average mass vertical dotted line
            avg_mass = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]['EEA_M'].mean()
            if row == 0:
                ax.axvline(avg_mass, color=colors[fuel], linestyle=':', alpha=0.4)

        ax.set_ylabel(ylabel)
        if row == 0:
            ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
        if row == 1:
            ax.set_xlabel('Vehicle mass [kg]')
        ax.legend(fontsize=7, loc='upper left')
        ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_C1_co2_vs_mass.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure C1 saved.")


###############################################################################
# FIGURE C2: RW CO2 vs Power-to-Mass Ratio
# Binned box plots, 2 rows (RW-CO2 + Gap)
###############################################################################
print("Generating Figure C2...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Figure C2: Real-world CO$_2$ vs. power-to-mass ratio',
             fontsize=13, fontweight='bold', y=0.99)

ptm_bins = np.arange(30, 200, 10)

for j, pt in enumerate(pt_order):
    for row, y_col, ylabel in [(0, 'RW_CO2', 'RW CO$_2$ [g/km]'),
                                (1, 'gap', 'Gap [g/km]')]:
        ax = axes[row, j]

        for fuel in ['Petrol', 'Diesel']:
            subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)].copy()
            if len(subset) < 200:
                continue

            subset['ptm_bin'] = pd.cut(subset['power_to_mass'], bins=ptm_bins)
            subset = subset.dropna(subset=['ptm_bin'])

            groups = []
            positions = []
            for b in sorted(subset['ptm_bin'].unique()):
                grp = subset[subset['ptm_bin'] == b][y_col].dropna()
                if len(grp) >= 20:
                    groups.append(grp.values)
                    positions.append(b.mid)

            if not groups:
                continue

            offset = -2 if fuel == 'Petrol' else 2
            pos_shifted = [p + offset for p in positions]

            bp = ax.boxplot(groups, positions=pos_shifted, widths=3.5,
                           patch_artist=True, showfliers=False,
                           medianprops=dict(color='black', linewidth=1),
                           whiskerprops=dict(color=colors[fuel], alpha=0.6),
                           capprops=dict(color=colors[fuel], alpha=0.6))
            for box in bp['boxes']:
                box.set_facecolor(colors[fuel])
                box.set_alpha(0.5)

            # Trend line (polynomial for diesel as noted in paper)
            medians = [np.median(g) for g in groups]
            if len(positions) > 3:
                deg = 2 if fuel == 'Diesel' else 1
                z = np.polyfit(positions, medians, deg)
                xfit = np.linspace(min(positions), max(positions), 50)
                ax.plot(xfit, np.polyval(z, xfit), '-', color=colors[fuel],
                       linewidth=2, label=fuel, zorder=10)

        ax.set_ylabel(ylabel)
        if row == 0:
            ax.set_title(f'{pt}', fontsize=12, fontweight='bold')
        if row == 1:
            ax.set_xlabel('Power-to-mass [W/kg]')
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{FIGURES_DIR}/Figure_C2_co2_vs_power_to_mass.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure C2 saved.")


###############################################################################
# FIGURE C3: PHEV CO2 vs Electric Range
# Binned box plots, 2 rows (RW-CO2 + Gap), proportional circles
###############################################################################
print("Generating Figure C3...")

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Figure C3: PHEV real-world CO$_2$ vs. official electric range',
             fontsize=13, fontweight='bold', y=0.99)

range_bins = np.arange(10, 130, 5)

for row, y_col, ylabel in [(0, 'RW_CO2', 'RW CO$_2$ [g/km]'),
                            (1, 'gap', 'Gap [g/km]')]:
    ax = axes[row]

    for fuel in ['Petrol', 'Diesel']:
        subset = df_clean[(df_clean['powertrain'] == 'PHEV') & (df_clean['fuel'] == fuel)].copy()
        if len(subset) < 50:
            continue

        subset['range_bin'] = pd.cut(subset['EEA_Zr'], bins=range_bins)
        subset = subset.dropna(subset=['range_bin'])

        groups = []
        positions = []
        counts = []
        for b in sorted(subset['range_bin'].unique()):
            grp = subset[subset['range_bin'] == b][y_col].dropna()
            if len(grp) >= 10:
                groups.append(grp.values)
                positions.append(b.mid)
                counts.append(len(grp))

        if not groups:
            continue

        offset = -1 if fuel == 'Petrol' else 1
        pos_shifted = [p + offset for p in positions]

        bp = ax.boxplot(groups, positions=pos_shifted, widths=2,
                       patch_artist=True, showfliers=False,
                       medianprops=dict(color='black', linewidth=1),
                       whiskerprops=dict(color=colors[fuel], alpha=0.6),
                       capprops=dict(color=colors[fuel], alpha=0.6))
        for box in bp['boxes']:
            box.set_facecolor(colors[fuel])
            box.set_alpha(0.5)

        # Trend line through medians
        medians = [np.median(g) for g in groups]
        if len(positions) > 3:
            ax.plot(positions, medians, '-', color=colors[fuel],
                   linewidth=2, label=f'{fuel} PHEV', zorder=10)

        # Proportional circles (top panel)
        if row == 0:
            max_c = max(counts) if max(counts) > 0 else 1
            for k in range(len(positions)):
                size = max(10, 100 * (counts[k] / max_c))
                ax.scatter(positions[k], max(medians) + 30, s=size,
                          color=colors[fuel], alpha=0.3, edgecolors='none')

    ax.set_ylabel(ylabel)
    if row == 1:
        ax.set_xlabel('Official electric range [km]')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f"{FIGURES_DIR}/Figure_C3_phev_co2_vs_range.png", dpi=200, bbox_inches='tight')
plt.close()
print("  -> Figure C3 saved.")


###############################################################################
# SUMMARY TABLE: Reproduce Table 3 values
###############################################################################
print("\n" + "=" * 70)
print("VALIDATION: Reproducing Table 3 - Fleet-wide average RW CO2 and gap")
print("=" * 70)

print(f"\n{'Powertrain':<12} {'Fuel':<10} {'RW CO2':>10} {'TA CO2':>10} {'Gap':>10} {'Gap%':>10} {'Count':>10}")
print("-" * 72)

for pt in pt_order:
    for fuel in ['Petrol', 'Diesel']:
        subset = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]
        if len(subset) < 100:
            continue
        rw = subset['RW_CO2'].mean()
        ta = subset['EEA_Ewltp'].mean()
        gap_abs = subset['gap'].mean()
        gap_pct = subset['gap_percentage'].mean()
        n = len(subset)
        print(f"{pt:<12} {fuel:<10} {rw:>10.1f} {ta:>10.1f} {gap_abs:>10.1f} {gap_pct:>9.1f}% {n:>10,}")

print("\nPaper-reported values (Table 3, 3-year average):")
print(f"  ICEV Petrol: RW=166.2, Gap=27.3 g/km")
print(f"  ICEV Diesel: RW=170.1, Gap=28.1 g/km")
print(f"  HEV Petrol:  RW=149.1, Gap=24.9 g/km")
print(f"  HEV Diesel:  RW=189.6, Gap=31.7 g/km")
print(f"  PHEV Petrol: RW=131.4, Gap=97.6 g/km")
print(f"  PHEV Diesel: RW=149.5, Gap=116.6 g/km")

print(f"\nAll figures saved to: {FIGURES_DIR}/")
