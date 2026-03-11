###############################################################################
# Implementation of all analyses from paper_analyses.md
# "Towards zero CO2 emissions: Insights from EU vehicle on-board data"
# Suarez, Tansini, Ktistakis, Marin, Komnos, Pavlovic & Fontaras (2025)
#
# Follows the structure of paper_analyses.md sections 1–10.
# Missing inputs trigger warnings; final table compares paper vs computed.
###############################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
from collections import OrderedDict
from itertools import combinations
from math import factorial
import warnings as _warnings
_warnings.filterwarnings('ignore')
import os
import sys

OUTPUT_DIR = "analysis_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Track all warnings for missing inputs
missing_input_warnings = []

def warn_missing(msg):
    print(f"  ⚠ WARNING: {msg}")
    missing_input_warnings.append(msg)

###############################################################################
# 0. DATA LOADING & PREPROCESSING
###############################################################################
print("=" * 70)
print("SECTION 0: Data Loading & Preprocessing")
print("=" * 70)

print("Loading OBFCM data...")
df = pd.read_csv('obfcm_data.csv', low_memory=False)
print(f"  Loaded: {len(df):,} rows, {len(df.columns)} columns")

# --- Derived columns (same as reproduce_figures.py) ---
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

# Volume
df['volume'] = (df['vdb_vehicle_length']
                * df['vdb_vehicle_width']
                * df['vdb_vehicle_height'])

# --- Outlier filtering (paper: CO2_RW < CO2_TA - 30 or CO2_RW > 3*CO2_TA) ---
n_before = len(df)
mask_icevhev = df['EEA_Fm'].isin(['M', 'H'])
mask_outlier = (df['RW_CO2'] > (df['EEA_Ewltp'] - 30)) & (df['RW_CO2'] < 3 * df['EEA_Ewltp'])
df_clean = df[~mask_icevhev | mask_outlier].copy()
n_after = len(df_clean)
print(f"  Outlier filter: {n_before:,} → {n_after:,} ({n_before - n_after:,} removed)")

# Convenience subsets
df_icev = df_clean[df_clean['powertrain'] == 'ICEV']
df_hev = df_clean[df_clean['powertrain'] == 'HEV']
df_phev = df_clean[df_clean['powertrain'] == 'PHEV']
df_noPhev = df_clean[df_clean['EEA_Fm'].isin(['M', 'H'])]

pt_order = ['ICEV', 'HEV', 'PHEV']
print(f"  ICEV: {len(df_icev):,} | HEV: {len(df_hev):,} | PHEV: {len(df_phev):,}")
print()

# ============================================================================
# Store results for final comparison table
# ============================================================================
results = {}

###############################################################################
# 1. REPRESENTATIVENESS ANALYSIS (Appendix A)
###############################################################################
print("=" * 70)
print("SECTION 1: Representativeness Analysis (Appendix A)")
print("=" * 70)
warn_missing("FleetEU (full 24.5M registration dataset) not available — "
             "representativeness comparison done within OBFCM sample only.")

# What we CAN compute: sample composition statistics
print("\n  Sample composition (OBFCM):")
pt_counts = df_clean['powertrain'].value_counts()
pt_pct = pt_counts / len(df_clean) * 100
for pt in pt_order:
    n = pt_counts.get(pt, 0)
    pct = pt_pct.get(pt, 0)
    print(f"    {pt}: {n:>10,} ({pct:.1f}%)")

fuel_counts = df_clean['fuel'].value_counts()
fuel_pct = fuel_counts / len(df_clean) * 100
for f in ['Petrol', 'Diesel']:
    n = fuel_counts.get(f, 0)
    pct = fuel_pct.get(f, 0)
    print(f"    {f}: {n:>10,} ({pct:.1f}%)")

year_counts = df_clean['EEA_year'].value_counts().sort_index()
print("\n  Registration year distribution:")
for yr, n in year_counts.items():
    print(f"    {yr}: {n:>10,} ({n / len(df_clean) * 100:.1f}%)")

# Average mass and TA CO2 per powertrain (Table A2 equivalent)
print("\n  Average mass and TA CO2 by powertrain (Table A2 — sample only):")
print(f"  {'Powertrain':<12} {'Avg Mass [kg]':>14} {'Avg TA CO2 [g/km]':>18}")
print("  " + "-" * 46)
for pt in pt_order:
    sub = df_clean[df_clean['powertrain'] == pt]
    avg_mass = sub['EEA_M'].mean()
    avg_ta = sub['EEA_Ewltp'].mean()
    print(f"  {pt:<12} {avg_mass:>14.1f} {avg_ta:>18.1f}")

results['sample_size'] = len(df_clean)
results['coverage_pct'] = 31.5  # paper value — cannot verify without FleetEU
print()


###############################################################################
# 2. POISSON MODEL FOR READOUT TIMING (Appendix B)
###############################################################################
print("=" * 70)
print("SECTION 2: Poisson Model for Readout Timing (Appendix B)")
print("=" * 70)

# Filter: 2021-registered vehicles with 2023 readouts
df_poisson = df_clean[
    (df_clean['EEA_year'] == 2021) &
    (df_clean['OBFCM_ReportingPeriod'] == 2023)
].copy()

if len(df_poisson) == 0:
    warn_missing("No 2021-registered vehicles with 2023 readouts found for Poisson model.")
else:
    print(f"  Vehicles for Poisson model: {len(df_poisson):,}")
    print(f"    (2021-registered, 2023 readout)")

    # Paper formula: N_vehicles = N * (1 - exp(-p * (3*365 - t)))
    # We approximate by computing annual mileage stability
    # Since we lack exact readout dates, we validate the annual mileage estimates

    # Annual mileage for 2021 vehicles recorded in 2023 (paper's "unbiased" subset)
    mileage_2021_2023 = df_poisson['annual_mileage_km'].dropna()

    for fuel in ['Petrol', 'Diesel']:
        sub = df_poisson[df_poisson['fuel'] == fuel]['annual_mileage_km'].dropna()
        if len(sub) > 0:
            med = sub.median()
            mean = sub.mean()
            print(f"  {fuel}: median annual mileage = {med:,.0f} km, "
                  f"mean = {mean:,.0f} km (n={len(sub):,})")

    # Paper values for comparison
    results['poisson_p'] = 3.7e-3  # paper value
    results['poisson_r2'] = 0.9    # paper value
    results['mileage_petrol'] = df_poisson[df_poisson['fuel'] == 'Petrol']['annual_mileage_km'].median()
    results['mileage_diesel'] = df_poisson[df_poisson['fuel'] == 'Diesel']['annual_mileage_km'].median()

    # Poisson model fit on registration date distribution
    # We simulate by looking at registration period distribution
    print(f"\n  Poisson model parameters (from paper):")
    print(f"    p = {results['poisson_p']}")
    print(f"    R² = {results['poisson_r2']}")
    warn_missing("Exact readout dates not in dataset — Poisson fitting uses "
                 "paper parameters. Annual mileage validated from data.")
print()


###############################################################################
# 3. DESCRIPTIVE EMISSIONS ANALYSIS (Figures 1-3)
###############################################################################
print("=" * 70)
print("SECTION 3: Descriptive Emissions Analysis (Figures 1–3)")
print("=" * 70)

# --- Figure 1: RW vs TA distributions ---
print("\n  Emission distribution statistics (Figure 1):")
print(f"  {'PT+Fuel':<16} {'RW Mean':>8} {'RW Std':>8} {'TA Mean':>8} "
      f"{'Gap Mean':>9} {'Gap Std':>8} {'N':>10}")
print("  " + "-" * 74)

for pt in pt_order:
    for fuel in ['Petrol', 'Diesel']:
        sub = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]
        if len(sub) < 100:
            continue
        rw_mean = sub['RW_CO2'].mean()
        rw_std = sub['RW_CO2'].std()
        ta_mean = sub['EEA_Ewltp'].mean()
        gap_mean = sub['gap'].mean()
        gap_std = sub['gap'].std()
        print(f"  {pt + ' ' + fuel:<16} {rw_mean:>8.1f} {rw_std:>8.1f} "
              f"{ta_mean:>8.1f} {gap_mean:>9.1f} {gap_std:>8.1f} {len(sub):>10,}")
        results[f'rw_mean_{pt}_{fuel}'] = rw_mean
        results[f'ta_mean_{pt}_{fuel}'] = ta_mean
        results[f'gap_mean_{pt}_{fuel}'] = gap_mean
        results[f'gap_pct_{pt}_{fuel}'] = sub['gap_percentage'].mean()

# PHEV gap range (paper: 99-121 g/km)
phev_gap = df_phev['gap'].describe()
print(f"\n  PHEV gap range: median={phev_gap['50%']:.1f}, "
      f"Q1={phev_gap['25%']:.1f}, Q3={phev_gap['75%']:.1f} g/km")

# --- Figure 2: Country-level emissions ---
print("\n  Country-level average RW CO2 (Figure 2 — top 5 countries by sample size):")
country_stats = (df_clean.groupby('EEA_MS')
                 .agg(RW_CO2=('RW_CO2', 'mean'),
                      TA_CO2=('EEA_Ewltp', 'mean'),
                      Gap=('gap', 'mean'),
                      N=('RW_CO2', 'count'))
                 .sort_values('N', ascending=False))
print(country_stats.head(5).to_string())

# --- Figure 3: Annual mileage by country ---
print("\n  Annual mileage by fuel (Figure 3 — fleet medians):")
for fuel in ['Petrol', 'Diesel']:
    sub = df_clean[df_clean['fuel'] == fuel]['annual_mileage_km'].dropna()
    print(f"    {fuel}: median = {sub.median():,.0f} km, mean = {sub.mean():,.0f} km")
print()


###############################################################################
# 4. VEHICLE CHARACTERISTIC CORRELATION (Figure 4)
###############################################################################
print("=" * 70)
print("SECTION 4: Vehicle Characteristic Correlation (Figure 4)")
print("=" * 70)

ta_bin_size = {'ICEV': 15, 'HEV': 15, 'PHEV': 10}

for pt in pt_order:
    sub = df_clean[df_clean['powertrain'] == pt].copy()
    if len(sub) < 200:
        continue

    bsize = ta_bin_size[pt]
    ta_min = int(sub['EEA_Ewltp'].quantile(0.01) // bsize * bsize)
    ta_max = int(sub['EEA_Ewltp'].quantile(0.99) // bsize * bsize) + bsize
    bins = np.arange(ta_min, ta_max + bsize, bsize)
    sub['ta_bin'] = pd.cut(sub['EEA_Ewltp'], bins=bins)

    bin_medians = sub.groupby('ta_bin', observed=True)['RW_CO2'].median().dropna()
    bin_positions = [interval.mid for interval in bin_medians.index]

    if len(bin_positions) > 2:
        slope, intercept, r_val, p_val, std_err = stats.linregress(bin_positions, bin_medians.values)
        r2 = r_val ** 2
        print(f"  {pt}: R² = {r2:.4f} (slope = {slope:.4f}, intercept = {intercept:.1f})")
        results[f'ta_rw_r2_{pt}'] = r2
    else:
        print(f"  {pt}: insufficient bins for regression")
print()


###############################################################################
# 5. VEHICLE AGEING & MILEAGE TRENDS (Figures 5, 6)
###############################################################################
print("=" * 70)
print("SECTION 5: Vehicle Ageing & Mileage Trends (Figures 5, 6)")
print("=" * 70)

# --- Figure 5: RW CO2 vs lifetime distance ---
print("\n  RW CO2 change with mileage (Figure 5):")
dist_bins = np.arange(0, 105000, 5000)

for pt in pt_order:
    sub = df_clean[df_clean['powertrain'] == pt].copy()
    sub['dist_bin'] = pd.cut(sub['OBFCM_TotLifetimeDist_km'], bins=dist_bins)

    low_mileage = sub[sub['OBFCM_TotLifetimeDist_km'] < 10000]['RW_CO2'].median()
    high_mileage = sub[sub['OBFCM_TotLifetimeDist_km'].between(90000, 100000)]['RW_CO2'].median()

    if not np.isnan(low_mileage) and not np.isnan(high_mileage):
        delta = high_mileage - low_mileage
        print(f"  {pt}: RW CO2 at <10k km = {low_mileage:.1f}, "
              f"at 90-100k km = {high_mileage:.1f}, delta = {delta:+.1f} g/km")
        results[f'mileage_delta_{pt}'] = delta

# --- Figure 6: Three-year tracking sample ---
print("\n  Three-year tracking sample (Figure 6):")
# Vehicles registered in 2021 appearing in multiple reporting years
df_2021 = df[df['EEA_year'] == 2021].copy()
tracking_veh = df_2021.groupby('veh_id')['OBFCM_ReportingPeriod'].nunique()
multi_year = tracking_veh[tracking_veh >= 2].index

if len(multi_year) > 0:
    df_tracking = df_2021[df_2021['veh_id'].isin(multi_year)].copy()
    print(f"  Vehicles with multiple readouts: {len(multi_year):,}")

    for yr in sorted(df_tracking['OBFCM_ReportingPeriod'].unique()):
        sub_yr = df_tracking[df_tracking['OBFCM_ReportingPeriod'] == yr]
        for pt in pt_order:
            sub_pt = sub_yr[sub_yr['powertrain'] == pt]
            if len(sub_pt) > 50:
                rw = sub_pt['RW_CO2'].median()
                print(f"    {pt} in {yr}: median RW CO2 = {rw:.1f} g/km (n={len(sub_pt):,})")
else:
    warn_missing("No vehicles found with multiple reporting years for tracking analysis. "
                 "Dataset may contain only deduplicated (most recent) records.")
print()


###############################################################################
# 6. MLR MODELS & VARIABLE IMPORTANCE (Figures 7-8)
###############################################################################
print("=" * 70)
print("SECTION 6: MLR Models & Variable Importance (Figures 7–8)")
print("=" * 70)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# --- Prepare features ---
df_model = df_clean.copy()
df_model['fuel_petrol'] = (df_model['fuel'] == 'Petrol').astype(float)
df_model['pt_hev'] = (df_model['EEA_Fm'] == 'H').astype(float)

# Country dummies
country_dummies = pd.get_dummies(df_model['EEA_MS'], prefix='c', drop_first=True, dtype=float)
country_cols = list(country_dummies.columns)
df_model = pd.concat([df_model, country_dummies], axis=1)

# ---------- VIF Analysis (Section 7 of paper_analyses.md) ----------
print("\n  6a. VIF Analysis (Variable Selection)")

def compute_vif(X):
    """Compute VIF for each column in X (DataFrame)."""
    from numpy.linalg import lstsq
    vif_data = {}
    X_arr = X.values.astype(float)
    for i, col in enumerate(X.columns):
        y_i = X_arr[:, i]
        X_i = np.delete(X_arr, i, axis=1)
        X_i = np.column_stack([np.ones(len(X_i)), X_i])
        beta, _, _, _ = lstsq(X_i, y_i, rcond=None)
        y_pred = X_i @ beta
        ss_res = np.sum((y_i - y_pred) ** 2)
        ss_tot = np.sum((y_i - y_i.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        vif_data[col] = 1 / (1 - r2) if r2 < 1 else np.inf
    return vif_data

# VIF for non-PHEV vehicle-level predictors
vif_cols_noPhev = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
                   'fuel_petrol', 'pt_hev', 'EEA_year',
                   'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp']
sub_vif = df_model[df_model['EEA_Fm'].isin(['M', 'H'])][vif_cols_noPhev].dropna()
if len(sub_vif) > 200000:
    sub_vif = sub_vif.sample(200000, random_state=42)

vif_noPhev = compute_vif(sub_vif)
print(f"\n  VIF — Non-PHEV vehicle-level (threshold: <5, exceptions <10):")
for col, v in sorted(vif_noPhev.items(), key=lambda x: -x[1]):
    flag = " ⚠ HIGH" if v >= 10 else (" (exception)" if v >= 5 else "")
    print(f"    {col:<35} VIF = {v:>8.2f}{flag}")

# VIF for PHEV vehicle-level predictors
vif_cols_phev = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
                 'fuel_petrol', 'EEA_year', 'EEA_Zr',
                 'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp', 'RW_eds']
sub_vif_phev = df_model[df_model['EEA_Fm'] == 'P'][vif_cols_phev].dropna()
if len(sub_vif_phev) > 200000:
    sub_vif_phev = sub_vif_phev.sample(200000, random_state=42)

if len(sub_vif_phev) > 100:
    vif_phev = compute_vif(sub_vif_phev)
    print(f"\n  VIF — PHEV vehicle-level (threshold: <5, exceptions <10):")
    for col, v in sorted(vif_phev.items(), key=lambda x: -x[1]):
        flag = " ⚠ HIGH" if v >= 10 else (" (exception)" if v >= 5 else "")
        print(f"    {col:<35} VIF = {v:>8.2f}{flag}")

# ---------- Model III-a: ICEV/HEV MLR ----------
print("\n  6b. Model III-a: ICEV/HEV MLR")

features_3a = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
               'fuel_petrol', 'pt_hev', 'EEA_year',
               'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp'] + country_cols

df_3a = df_model[df_model['EEA_Fm'].isin(['M', 'H'])][features_3a + ['RW_CO2']].dropna()
print(f"  Observations: {len(df_3a):,}")

X_3a = df_3a[features_3a].values
y_3a = df_3a['RW_CO2'].values

model_3a = LinearRegression()
model_3a.fit(X_3a, y_3a)
y_pred_3a = model_3a.predict(X_3a)
r2_3a = r2_score(y_3a, y_pred_3a)

print(f"  R² = {r2_3a:.4f} ({r2_3a * 100:.1f}%)")
results['r2_model_3a'] = r2_3a

# Key coefficients
coef_3a = dict(zip(features_3a, model_3a.coef_))
print(f"  Key coefficients:")
for var in ['EEA_Ewltp', 'EEA_Ep', 'EEA_M']:
    print(f"    {var:<35} = {coef_3a[var]:>10.4f}")
print(f"    {'Intercept':<35} = {model_3a.intercept_:>10.4f}")
results['coef_3a_ta'] = coef_3a['EEA_Ewltp']
results['coef_3a_power'] = coef_3a['EEA_Ep']
results['coef_3a_mass'] = coef_3a['EEA_M']

# ---------- Model III-b: PHEV MLR ----------
print("\n  6c. Model III-b: PHEV MLR")

features_3b = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
               'fuel_petrol', 'EEA_year', 'EEA_Zr',
               'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp', 'RW_eds'] + country_cols

df_3b = df_model[df_model['EEA_Fm'] == 'P'][features_3b + ['RW_CO2']].dropna()
print(f"  Observations: {len(df_3b):,}")

if len(df_3b) > 100:
    X_3b = df_3b[features_3b].values
    y_3b = df_3b['RW_CO2'].values

    model_3b = LinearRegression()
    model_3b.fit(X_3b, y_3b)
    y_pred_3b = model_3b.predict(X_3b)
    r2_3b = r2_score(y_3b, y_pred_3b)

    print(f"  R² = {r2_3b:.4f} ({r2_3b * 100:.1f}%)")
    results['r2_model_3b'] = r2_3b

    coef_3b = dict(zip(features_3b, model_3b.coef_))
    print(f"  Key coefficients:")
    for var in ['EEA_Ewltp', 'EEA_Ep', 'RW_eds']:
        print(f"    {var:<35} = {coef_3b[var]:>10.4f}")
    print(f"    {'Intercept':<35} = {model_3b.intercept_:>10.4f}")
    results['coef_3b_ta'] = coef_3b['EEA_Ewltp']
    results['coef_3b_power'] = coef_3b['EEA_Ep']
    results['coef_3b_eds'] = coef_3b['RW_eds']
else:
    warn_missing("Insufficient PHEV data for Model III-b regression.")
    r2_3b = np.nan

# ---------- LMG Decomposition (Figure 7) ----------
print("\n  6d. LMG Decomposition — Variable Importance (Figure 7)")

def compute_lmg(data, predictor_groups, target, sample_size=200000):
    """LMG R² decomposition using covariance-matrix approach."""
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
    X = X - X.mean(axis=0)
    yc = y - y.mean()
    ss_tot = yc @ yc

    XtX = X.T @ X
    Xty = X.T @ yc

    gnames = list(predictor_groups.keys())
    p = len(gnames)

    def r2_sub(gi_set):
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

    cache = {}
    for sz in range(p + 1):
        for combo in combinations(range(p), sz):
            cache[frozenset(combo)] = r2_sub(combo)

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

# Predictor groups for extended models (Model III)
rw_ext_icevhev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Powertrain',          ['pt_hev']),
    ('Year',                ['EEA_year']),
    ('Country',             country_cols),
    ('Mileage [km]',        ['OBFCM_TotLifetimeDist_km']),
    ('TA CO2 [g/km]',       ['EEA_Ewltp']),
])

rw_ext_phev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m³]',         ['volume']),
    ('Tyre radius [m]',     ['vdb_front_tyre_radius']),
    ('Fuel type',           ['fuel_petrol']),
    ('Electric range [km]', ['EEA_Zr']),
    ('Year',                ['EEA_year']),
    ('Country',             country_cols),
    ('Mileage [km]',        ['OBFCM_TotLifetimeDist_km']),
    ('TA CO2 [g/km]',       ['EEA_Ewltp']),
    ('EDS [%]',             ['RW_eds']),
])

print("\n  Computing LMG for ICEV/HEV (Model III-a)...")
lmg_3a, lmg_r2_3a = compute_lmg(df_model[df_model['EEA_Fm'].isin(['M', 'H'])],
                                  rw_ext_icevhev, 'RW_CO2')
print(f"  Full R² = {lmg_r2_3a * 100:.1f}%")
print(f"  {'Variable':<25} {'Importance':>12}")
print("  " + "-" * 39)
for var, imp in sorted(lmg_3a.items(), key=lambda x: -x[1]):
    print(f"  {var:<25} {imp * 100:>11.1f}%")
results['lmg_3a_ta_co2'] = lmg_3a.get('TA CO2 [g/km]', 0) * 100
results['lmg_3a_power'] = lmg_3a.get('Engine power [kW]', 0) * 100
results['lmg_3a_mass'] = lmg_3a.get('Mass [kg]', 0) * 100

print("\n  Computing LMG for PHEV (Model III-b)...")
lmg_3b, lmg_r2_3b = compute_lmg(df_model[df_model['EEA_Fm'] == 'P'],
                                  rw_ext_phev, 'RW_CO2')
print(f"  Full R² = {lmg_r2_3b * 100:.1f}%")
print(f"  {'Variable':<25} {'Importance':>12}")
print("  " + "-" * 39)
for var, imp in sorted(lmg_3b.items(), key=lambda x: -x[1]):
    print(f"  {var:<25} {imp * 100:>11.1f}%")
results['lmg_3b_eds'] = lmg_3b.get('EDS [%]', 0) * 100
results['lmg_3b_ta_co2'] = lmg_3b.get('TA CO2 [g/km]', 0) * 100

# ---------- Country-level models (Figure 8) ----------
print("\n  6e. Country-Level Variable Importance (Figure 8)")
warn_missing("Eurostat data (population density, temperature, GDP, speed limits) "
             "not available — country-level models (IV, V) cannot be fully replicated. "
             "Using country-aggregated OBFCM variables only.")

# What we CAN compute: country-level aggregation of available variables
country_agg = (df_clean.groupby('EEA_MS')
               .agg(RW_CO2=('RW_CO2', 'mean'),
                    mass=('EEA_M', 'mean'),
                    power=('EEA_Ep', 'mean'),
                    ta_co2=('EEA_Ewltp', 'mean'),
                    mileage=('annual_mileage_km', 'mean'),
                    n=('RW_CO2', 'count'))
               .dropna())
country_agg = country_agg[country_agg['n'] >= 30]  # min 30 vehicles

if len(country_agg) >= 5:
    X_country = country_agg[['mass', 'power', 'ta_co2', 'mileage']].values
    y_country = country_agg['RW_CO2'].values
    lr_country = LinearRegression().fit(X_country, y_country)
    r2_country = r2_score(y_country, lr_country.predict(X_country))
    print(f"  Country-level R² (partial model, no Eurostat vars) = {r2_country:.4f}")
    results['r2_country_partial'] = r2_country
else:
    warn_missing("Fewer than 5 countries with sufficient data for country-level model.")
print()


###############################################################################
# 7. STATISTICAL ROBUSTNESS (Appendix E)
###############################################################################
print("=" * 70)
print("SECTION 7: Statistical Robustness (Appendix E)")
print("=" * 70)

# --- Breusch-Pagan test for heteroscedasticity ---
print("\n  7a. Breusch-Pagan Test for Heteroscedasticity")

def breusch_pagan_test(X, y, y_pred):
    """Breusch-Pagan test for heteroscedasticity."""
    residuals = y - y_pred
    resid_sq = residuals ** 2
    resid_sq_norm = resid_sq / resid_sq.mean()
    X_with_const = np.column_stack([np.ones(len(X)), X])
    beta, _, _, _ = np.linalg.lstsq(X_with_const, resid_sq_norm, rcond=None)
    resid_sq_pred = X_with_const @ beta
    ss_reg = np.sum((resid_sq_pred - resid_sq_norm.mean()) ** 2)
    lm_stat = ss_reg / 2.0
    df = X.shape[1]
    p_value = 1 - stats.chi2.cdf(lm_stat, df)
    return lm_stat, p_value

# Vehicle-level: Model III-a
bp_stat_3a, bp_p_3a = breusch_pagan_test(X_3a, y_3a, y_pred_3a)
print(f"  Model III-a (ICEV/HEV): LM stat = {bp_stat_3a:.2f}, p = {bp_p_3a:.6f}")
print(f"    {'→ Heteroscedasticity present (p < 0.001)' if bp_p_3a < 0.001 else '→ No heteroscedasticity detected'}")
results['bp_p_3a'] = bp_p_3a

# Vehicle-level: Model III-b
if len(df_3b) > 100:
    bp_stat_3b, bp_p_3b = breusch_pagan_test(X_3b, y_3b, y_pred_3b)
    print(f"  Model III-b (PHEV):     LM stat = {bp_stat_3b:.2f}, p = {bp_p_3b:.6f}")
    print(f"    {'→ Heteroscedasticity present (p < 0.001)' if bp_p_3b < 0.001 else '→ No heteroscedasticity detected'}")
    results['bp_p_3b'] = bp_p_3b

# --- HC1 Robust Standard Errors ---
print("\n  7b. HC1 Robust Standard Errors (Model III-a)")

def hc1_robust_se(X, y, y_pred, add_const=True):
    """Compute HC1 robust standard errors."""
    n = len(y)
    if add_const:
        X_c = np.column_stack([np.ones(n), X])
    else:
        X_c = X
    k = X_c.shape[1]
    resid = y - y_pred

    # (X'X)^-1
    XtX_inv = np.linalg.inv(X_c.T @ X_c)

    # HC1: (n/(n-k)) * (X'X)^-1 X' diag(e^2) X (X'X)^-1
    scale = n / (n - k)
    meat = X_c.T @ np.diag(resid ** 2) @ X_c
    V_hc1 = scale * XtX_inv @ meat @ XtX_inv
    se_hc1 = np.sqrt(np.diag(V_hc1))

    # Regular OLS SE for comparison
    sigma2 = np.sum(resid ** 2) / (n - k)
    V_ols = sigma2 * XtX_inv
    se_ols = np.sqrt(np.diag(V_ols))

    return se_ols, se_hc1

# Sample for performance (HC1 with diag is O(n*k²))
n_sample_hc1 = min(len(X_3a), 500000)
idx_sample = np.random.RandomState(42).choice(len(X_3a), n_sample_hc1, replace=False)
X_3a_sample = X_3a[idx_sample]
y_3a_sample = y_3a[idx_sample]
y_pred_3a_sample = model_3a.predict(X_3a_sample)

se_ols, se_hc1 = hc1_robust_se(X_3a_sample, y_3a_sample, y_pred_3a_sample)

# Show key variables (skip intercept at index 0, then features_3a order)
print(f"  {'Variable':<30} {'OLS SE':>10} {'HC1 SE':>10} {'Ratio':>8}")
print("  " + "-" * 60)
key_vars_idx = {'EEA_Ewltp': features_3a.index('EEA_Ewltp'),
                'EEA_Ep': features_3a.index('EEA_Ep'),
                'EEA_M': features_3a.index('EEA_M')}
for var_name, var_idx in key_vars_idx.items():
    se_idx = var_idx + 1  # +1 for intercept
    ratio = se_hc1[se_idx] / se_ols[se_idx] if se_ols[se_idx] > 0 else np.nan
    print(f"  {var_name:<30} {se_ols[se_idx]:>10.6f} {se_hc1[se_idx]:>10.6f} {ratio:>8.3f}")

# --- Tyre radius significance for PHEV ---
if len(df_3b) > 100:
    print("\n  7c. Tyre radius significance for PHEV:")
    tyre_idx = features_3b.index('vdb_front_tyre_radius')
    coef_tyre = model_3b.coef_[tyre_idx]

    # Quick p-value via t-test
    n_phev = len(X_3b)
    resid_3b = y_3b - y_pred_3b
    sigma2_3b = np.sum(resid_3b ** 2) / (n_phev - X_3b.shape[1] - 1)
    X_3b_c = np.column_stack([np.ones(n_phev), X_3b])
    try:
        XtX_inv_3b = np.linalg.inv(X_3b_c.T @ X_3b_c)
        se_tyre = np.sqrt(sigma2_3b * XtX_inv_3b[tyre_idx + 1, tyre_idx + 1])
        t_stat = coef_tyre / se_tyre
        p_tyre = 2 * (1 - stats.t.cdf(abs(t_stat), n_phev - X_3b.shape[1] - 1))
        print(f"  Tyre radius coef = {coef_tyre:.4f}, SE = {se_tyre:.4f}, "
              f"t = {t_stat:.4f}, p = {p_tyre:.4f}")
        results['p_tyre_phev'] = p_tyre
    except np.linalg.LinAlgError:
        warn_missing("Could not compute tyre radius p-value (singular matrix).")
print()


###############################################################################
# 8. FLEET EXTRAPOLATION (Tables 3-4)
###############################################################################
print("=" * 70)
print("SECTION 8: Fleet Extrapolation (Tables 3–4)")
print("=" * 70)
warn_missing("FleetEU dataset (25M full registrations) not available — "
             "fleet extrapolation uses OBFCM sample with model predictions. "
             "Stochastic imputation for unobserved fleet cannot be performed.")

# --- Table 3: Fleet-wide average RW CO2 and gap ---
print("\n  8a. Table 3 — Average RW CO2 and Gap (from OBFCM sample):")
print(f"  {'PT+Fuel':<16} {'RW CO2':>8} {'TA CO2':>8} {'Gap':>8} "
      f"{'Gap%':>8} {'N':>10}")
print("  " + "-" * 60)

for pt in pt_order:
    for fuel in ['Petrol', 'Diesel']:
        sub = df_clean[(df_clean['powertrain'] == pt) & (df_clean['fuel'] == fuel)]
        if len(sub) < 100:
            continue
        rw = sub['RW_CO2'].mean()
        ta = sub['EEA_Ewltp'].mean()
        gap_abs = sub['gap'].mean()
        gap_pct = sub['gap_percentage'].mean()
        print(f"  {pt + ' ' + fuel:<16} {rw:>8.1f} {ta:>8.1f} "
              f"{gap_abs:>8.1f} {gap_pct:>7.1f}% {len(sub):>10,}")

# --- Model-predicted RW CO2 (within sample) ---
print("\n  8b. Model-predicted RW CO2 (in-sample prediction):")
print(f"  {'PT+Fuel':<16} {'Actual':>8} {'Predicted':>10} {'Diff':>8}")
print("  " + "-" * 46)

for pt in pt_order:
    for fuel in ['Petrol', 'Diesel']:
        if pt in ['ICEV', 'HEV']:
            sub = df_3a.copy()
            sub['powertrain'] = df_model.loc[sub.index, 'powertrain']
            sub['fuel'] = df_model.loc[sub.index, 'fuel']
            sub_pf = sub[(sub['powertrain'] == pt) & (sub['fuel'] == fuel)]
            if len(sub_pf) < 100:
                continue
            actual = sub_pf['RW_CO2'].mean()
            predicted = model_3a.predict(sub_pf[features_3a].values).mean()
        else:
            if len(df_3b) < 100:
                continue
            sub = df_3b.copy()
            sub['fuel'] = df_model.loc[sub.index, 'fuel']
            sub_pf = sub[sub['fuel'] == fuel]
            if len(sub_pf) < 100:
                continue
            actual = sub_pf['RW_CO2'].mean()
            predicted = model_3b.predict(sub_pf[features_3b].values).mean()

        diff = predicted - actual
        print(f"  {pt + ' ' + fuel:<16} {actual:>8.1f} {predicted:>10.1f} "
              f"{diff:>+8.2f}")
        results[f'pred_rw_{pt}_{fuel}'] = predicted

# --- Table 4: Total annual emissions estimate ---
print("\n  8c. Table 4 — Estimated Annual Tailpipe Emissions (OBFCM sample only):")
warn_missing("Total EU emissions (Table 4) require FleetEU data for full "
             "extrapolation. Computing sample-based estimate only.")

for year in [2021, 2022, 2023]:
    sub_yr = df_clean[df_clean['EEA_year'] == year]
    if len(sub_yr) == 0:
        continue

    # Emission estimate: avg_RW_CO2 (g/km) * avg_annual_mileage (km) * n_vehicles / 1e9 (→ Mt)
    rw_avg = sub_yr['RW_CO2'].mean()
    mileage_avg = sub_yr['annual_mileage_km'].mean()
    n_veh = len(sub_yr)

    # Sample-based estimate (not scaled to full fleet)
    mt_sample = rw_avg * mileage_avg * n_veh / 1e12  # g → Mt
    print(f"  {year}: {n_veh:,} vehicles, avg RW = {rw_avg:.1f} g/km, "
          f"avg mileage = {mileage_avg:,.0f} km → {mt_sample:.2f} Mt (sample only)")
    results[f'mt_sample_{year}'] = mt_sample
print()


###############################################################################
# 9. FINAL COMPARISON TABLE: Paper vs Computed Values
###############################################################################
print("=" * 70)
print("SECTION 9: FINAL COMPARISON — Paper Values vs Computed Values")
print("=" * 70)

comparison = []

# --- Table 3: RW CO2 averages ---
paper_rw = {
    'ICEV_Petrol': 166.2, 'ICEV_Diesel': 170.1,
    'HEV_Petrol': 149.1, 'HEV_Diesel': 189.6,
    'PHEV_Petrol': 131.4, 'PHEV_Diesel': 149.5,
}
paper_gap = {
    'ICEV_Petrol': 27.3, 'ICEV_Diesel': 28.1,
    'HEV_Petrol': 24.9, 'HEV_Diesel': 31.7,
    'PHEV_Petrol': 97.6, 'PHEV_Diesel': 116.6,
}

for key in paper_rw:
    pt, fuel = key.split('_')
    rw_key = f'rw_mean_{pt}_{fuel}'
    gap_key = f'gap_mean_{pt}_{fuel}'
    computed_rw = results.get(rw_key, np.nan)
    computed_gap = results.get(gap_key, np.nan)
    comparison.append({
        'Metric': f'{pt} {fuel} — RW CO2 [g/km]',
        'Paper': paper_rw[key],
        'Computed': round(computed_rw, 1) if not np.isnan(computed_rw) else 'N/A',
        'Diff': round(computed_rw - paper_rw[key], 1) if not np.isnan(computed_rw) else 'N/A',
    })
    comparison.append({
        'Metric': f'{pt} {fuel} — Gap [g/km]',
        'Paper': paper_gap[key],
        'Computed': round(computed_gap, 1) if not np.isnan(computed_gap) else 'N/A',
        'Diff': round(computed_gap - paper_gap[key], 1) if not np.isnan(computed_gap) else 'N/A',
    })

# --- Model R² ---
comparison.append({
    'Metric': 'Model III-a R² (ICEV/HEV)',
    'Paper': '75%',
    'Computed': f'{r2_3a * 100:.1f}%',
    'Diff': f'{(r2_3a * 100 - 75):+.1f}pp',
})
comparison.append({
    'Metric': 'Model III-b R² (PHEV)',
    'Paper': '82%',
    'Computed': f'{r2_3b * 100:.1f}%' if not np.isnan(r2_3b) else 'N/A',
    'Diff': f'{(r2_3b * 100 - 82):+.1f}pp' if not np.isnan(r2_3b) else 'N/A',
})

# --- Key coefficients ---
paper_coefs = {
    'Coef III-a: TA CO2': (1.0136, results.get('coef_3a_ta', np.nan)),
    'Coef III-a: Engine Power': (0.1473, results.get('coef_3a_power', np.nan)),
    'Coef III-a: Mass': (-0.0063, results.get('coef_3a_mass', np.nan)),
    'Coef III-b: TA CO2': (0.6518, results.get('coef_3b_ta', np.nan)),
    'Coef III-b: Engine Power': (0.1814, results.get('coef_3b_power', np.nan)),
    'Coef III-b: EDS': (-1.8606, results.get('coef_3b_eds', np.nan)),
}
for label, (paper_val, computed_val) in paper_coefs.items():
    comparison.append({
        'Metric': label,
        'Paper': paper_val,
        'Computed': round(computed_val, 4) if not np.isnan(computed_val) else 'N/A',
        'Diff': round(computed_val - paper_val, 4) if not np.isnan(computed_val) else 'N/A',
    })

# --- TA vs RW correlation R² ---
paper_ta_r2 = {'ICEV': 0.99, 'HEV': 0.99, 'PHEV': 0.94}
for pt, p_r2 in paper_ta_r2.items():
    c_r2 = results.get(f'ta_rw_r2_{pt}', np.nan)
    comparison.append({
        'Metric': f'TA-RW Correlation R² ({pt})',
        'Paper': p_r2,
        'Computed': round(c_r2, 4) if not np.isnan(c_r2) else 'N/A',
        'Diff': round(c_r2 - p_r2, 4) if not np.isnan(c_r2) else 'N/A',
    })

# --- LMG variable importance ---
lmg_paper = {
    'LMG III-a: TA CO2 [%]': (49.0, results.get('lmg_3a_ta_co2', np.nan)),
    'LMG III-a: Engine Power [%]': (18.0, results.get('lmg_3a_power', np.nan)),
    'LMG III-a: Mass [%]': (10.0, results.get('lmg_3a_mass', np.nan)),
    'LMG III-b: EDS [%]': (51.0, results.get('lmg_3b_eds', np.nan)),
}
for label, (paper_val, computed_val) in lmg_paper.items():
    comparison.append({
        'Metric': label,
        'Paper': f'{paper_val:.1f}%',
        'Computed': f'{computed_val:.1f}%' if not np.isnan(computed_val) else 'N/A',
        'Diff': f'{computed_val - paper_val:+.1f}pp' if not np.isnan(computed_val) else 'N/A',
    })

# --- Total emissions (paper values only — we can't fully replicate) ---
paper_mt = {2021: 20.9, 2022: 18.7, 2023: 20.5}
for yr, p_mt in paper_mt.items():
    c_mt = results.get(f'mt_sample_{yr}', np.nan)
    comparison.append({
        'Metric': f'Total Emissions {yr} [Mt]',
        'Paper': p_mt,
        'Computed': f'{c_mt:.2f} (sample)' if not np.isnan(c_mt) else 'N/A',
        'Diff': 'N/A — needs FleetEU',
    })

# --- Annual mileage ---
comparison.append({
    'Metric': 'Annual mileage Petrol [km]',
    'Paper': '~11,500',
    'Computed': f'{results.get("mileage_petrol", np.nan):,.0f}',
    'Diff': '',
})
comparison.append({
    'Metric': 'Annual mileage Diesel [km]',
    'Paper': '~22,700',
    'Computed': f'{results.get("mileage_diesel", np.nan):,.0f}',
    'Diff': '',
})

# --- Print comparison table ---
df_comp = pd.DataFrame(comparison)
print(f"\n{'Metric':<40} {'Paper':>14} {'Computed':>14} {'Diff':>18}")
print("-" * 88)
for _, row in df_comp.iterrows():
    print(f"{row['Metric']:<40} {str(row['Paper']):>14} {str(row['Computed']):>14} "
          f"{str(row['Diff']):>18}")

# Save to CSV
df_comp.to_csv(f"{OUTPUT_DIR}/comparison_table.csv", index=False)
print(f"\n  Comparison table saved to: {OUTPUT_DIR}/comparison_table.csv")


###############################################################################
# 10. SUMMARY OF WARNINGS
###############################################################################
print("\n" + "=" * 70)
print("SUMMARY: Missing Input Warnings")
print("=" * 70)
if missing_input_warnings:
    for i, w in enumerate(missing_input_warnings, 1):
        print(f"  {i}. {w}")
else:
    print("  No warnings — all inputs available.")

print(f"\nAll outputs saved to: {OUTPUT_DIR}/")
print("Done.")
