###############################################################################
# Section 6: MLR Models & Variable Importance (Figures 7-8)
#
# Trains models and saves them for sections 7 and 8.
###############################################################################
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *
from collections import OrderedDict
from itertools import combinations
from math import factorial
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

print("=" * 70)
print("SECTION 6: MLR Models & Variable Importance (Figures 7-8)")
print("=" * 70)

df_clean = load_preprocessed(clean_only=True)
df_model, country_cols = build_model_data(df_clean)
del df_clean  # free memory -- use df_model from here

results = {}


# =========================================================================
# 6a. VIF Analysis
# =========================================================================
print("\n  6a. VIF Analysis (Variable Selection)")

def compute_vif(X):
    """Compute VIF for each column in X (DataFrame)."""
    vif_data = {}
    X_arr = X.values.astype(float)
    for i, col in enumerate(X.columns):
        y_i = X_arr[:, i]
        X_i = np.delete(X_arr, i, axis=1)
        X_i = np.column_stack([np.ones(len(X_i)), X_i])
        beta, _, _, _ = np.linalg.lstsq(X_i, y_i, rcond=None)
        y_pred = X_i @ beta
        ss_res = np.sum((y_i - y_pred) ** 2)
        ss_tot = np.sum((y_i - y_i.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        vif_data[col] = 1 / (1 - r2) if r2 < 1 else np.inf
    return vif_data

# VIF for non-PHEV
vif_cols_noPhev = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
                   'fuel_petrol', 'pt_hev', 'EEA_year',
                   'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp']
sub_vif = df_model[df_model['EEA_Fm'].isin(['M', 'H'])][vif_cols_noPhev].dropna()
if len(sub_vif) > 200000:
    sub_vif = sub_vif.sample(200000, random_state=42)

vif_noPhev = compute_vif(sub_vif)
print(f"\n  VIF -- Non-PHEV vehicle-level (threshold: <5, exceptions <10):")
for col, v in sorted(vif_noPhev.items(), key=lambda x: -x[1]):
    flag = " HIGH" if v >= 10 else (" (exception)" if v >= 5 else "")
    print(f"    {col:<35} VIF = {v:>8.2f}{flag}")
del sub_vif

# VIF for PHEV
vif_cols_phev = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
                 'fuel_petrol', 'EEA_year', 'EEA_Zr',
                 'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp', 'RW_eds']
sub_vif_phev = df_model[df_model['EEA_Fm'] == 'P'][vif_cols_phev].dropna()
if len(sub_vif_phev) > 200000:
    sub_vif_phev = sub_vif_phev.sample(200000, random_state=42)

if len(sub_vif_phev) > 100:
    vif_phev = compute_vif(sub_vif_phev)
    print(f"\n  VIF -- PHEV vehicle-level (threshold: <5, exceptions <10):")
    for col, v in sorted(vif_phev.items(), key=lambda x: -x[1]):
        flag = " HIGH" if v >= 10 else (" (exception)" if v >= 5 else "")
        print(f"    {col:<35} VIF = {v:>8.2f}{flag}")
del sub_vif_phev


# =========================================================================
# 6b. Model III-a: ICEV/HEV MLR
# =========================================================================
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

print(f"  R2 = {r2_3a:.4f} ({r2_3a * 100:.1f}%)")
results['r2_model_3a'] = float(r2_3a)

coef_3a = dict(zip(features_3a, model_3a.coef_))
print(f"  Key coefficients:")
for var in ['EEA_Ewltp', 'EEA_Ep', 'EEA_M']:
    print(f"    {var:<35} = {coef_3a[var]:>10.4f}")
print(f"    {'Intercept':<35} = {model_3a.intercept_:>10.4f}")
results['coef_3a_ta'] = float(coef_3a['EEA_Ewltp'])
results['coef_3a_power'] = float(coef_3a['EEA_Ep'])
results['coef_3a_mass'] = float(coef_3a['EEA_M'])

del X_3a, y_3a, y_pred_3a, df_3a  # free before next model


# =========================================================================
# 6c. Model III-b: PHEV MLR
# =========================================================================
print("\n  6c. Model III-b: PHEV MLR")

features_3b = ['EEA_Ep', 'EEA_M', 'volume', 'vdb_front_tyre_radius',
               'fuel_petrol', 'EEA_year', 'EEA_Zr',
               'OBFCM_TotLifetimeDist_km', 'EEA_Ewltp', 'RW_eds'] + country_cols

df_3b = df_model[df_model['EEA_Fm'] == 'P'][features_3b + ['RW_CO2']].dropna()
print(f"  Observations: {len(df_3b):,}")

r2_3b = np.nan
model_3b = None
if len(df_3b) > 100:
    X_3b = df_3b[features_3b].values
    y_3b = df_3b['RW_CO2'].values

    model_3b = LinearRegression()
    model_3b.fit(X_3b, y_3b)
    y_pred_3b = model_3b.predict(X_3b)
    r2_3b = r2_score(y_3b, y_pred_3b)

    print(f"  R2 = {r2_3b:.4f} ({r2_3b * 100:.1f}%)")
    results['r2_model_3b'] = float(r2_3b)

    coef_3b = dict(zip(features_3b, model_3b.coef_))
    print(f"  Key coefficients:")
    for var in ['EEA_Ewltp', 'EEA_Ep', 'RW_eds']:
        print(f"    {var:<35} = {coef_3b[var]:>10.4f}")
    print(f"    {'Intercept':<35} = {model_3b.intercept_:>10.4f}")
    results['coef_3b_ta'] = float(coef_3b['EEA_Ewltp'])
    results['coef_3b_power'] = float(coef_3b['EEA_Ep'])
    results['coef_3b_eds'] = float(coef_3b['RW_eds'])

    del X_3b, y_3b, y_pred_3b, df_3b
else:
    warn_missing("Insufficient PHEV data for Model III-b regression.")


# =========================================================================
# 6d. LMG Decomposition (Figure 7)
# =========================================================================
print("\n  6d. LMG Decomposition -- Variable Importance (Figure 7)")

def compute_lmg(data, predictor_groups, target, sample_size=200000):
    """LMG R2 decomposition using covariance-matrix approach."""
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

# Predictor groups for Model III
rw_ext_icevhev = OrderedDict([
    ('Engine power [kW]',   ['EEA_Ep']),
    ('Mass [kg]',           ['EEA_M']),
    ('Volume [m3]',         ['volume']),
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
    ('Volume [m3]',         ['volume']),
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
lmg_3a, lmg_r2_3a = compute_lmg(
    df_model[df_model['EEA_Fm'].isin(['M', 'H'])], rw_ext_icevhev, 'RW_CO2')
print(f"  Full R2 = {lmg_r2_3a * 100:.1f}%")
print(f"  {'Variable':<25} {'Importance':>12}")
print("  " + "-" * 39)
for var, imp in sorted(lmg_3a.items(), key=lambda x: -x[1]):
    print(f"  {var:<25} {imp * 100:>11.1f}%")
results['lmg_3a_ta_co2'] = lmg_3a.get('TA CO2 [g/km]', 0) * 100
results['lmg_3a_power'] = lmg_3a.get('Engine power [kW]', 0) * 100
results['lmg_3a_mass'] = lmg_3a.get('Mass [kg]', 0) * 100

print("\n  Computing LMG for PHEV (Model III-b)...")
lmg_3b, lmg_r2_3b = compute_lmg(
    df_model[df_model['EEA_Fm'] == 'P'], rw_ext_phev, 'RW_CO2')
print(f"  Full R2 = {lmg_r2_3b * 100:.1f}%")
print(f"  {'Variable':<25} {'Importance':>12}")
print("  " + "-" * 39)
for var, imp in sorted(lmg_3b.items(), key=lambda x: -x[1]):
    print(f"  {var:<25} {imp * 100:>11.1f}%")
results['lmg_3b_eds'] = lmg_3b.get('EDS [%]', 0) * 100
results['lmg_3b_ta_co2'] = lmg_3b.get('TA CO2 [g/km]', 0) * 100


# =========================================================================
# 6e. Country-Level Variable Importance (Figure 8)
# =========================================================================
print("\n  6e. Country-Level Variable Importance (Figure 8)")
warn_missing("Eurostat data (population density, temperature, GDP, speed limits) "
             "not available -- country-level models (IV, V) cannot be fully "
             "replicated. Using country-aggregated OBFCM variables only.")

country_agg = (df_model.groupby('EEA_MS')
               .agg(RW_CO2=('RW_CO2', 'mean'),
                    mass=('EEA_M', 'mean'),
                    power=('EEA_Ep', 'mean'),
                    ta_co2=('EEA_Ewltp', 'mean'),
                    mileage=('annual_mileage_km', 'mean'),
                    n=('RW_CO2', 'count'))
               .dropna())
country_agg = country_agg[country_agg['n'] >= 30]

if len(country_agg) >= 5:
    X_country = country_agg[['mass', 'power', 'ta_co2', 'mileage']].values
    y_country = country_agg['RW_CO2'].values
    lr_country = LinearRegression().fit(X_country, y_country)
    r2_country = r2_score(y_country, lr_country.predict(X_country))
    print(f"  Country-level R2 (partial model, no Eurostat vars) = {r2_country:.4f}")
    results['r2_country_partial'] = float(r2_country)
else:
    warn_missing("Fewer than 5 countries with sufficient data.")


# =========================================================================
# Save models for sections 7 and 8
# =========================================================================
models_path = os.path.join(OUTPUT_DIR, "s6_models.pkl")
with open(models_path, 'wb') as f:
    pickle.dump({
        'model_3a': model_3a,
        'model_3b': model_3b,
        'features_3a': features_3a,
        'features_3b': features_3b,
        'country_cols': country_cols,
        'r2_3a': r2_3a,
        'r2_3b': float(r2_3b) if not np.isnan(r2_3b) else None,
    }, f)
print(f"\n  Models saved to: {models_path}")

save_results('s6', results)
print("\nDone.")
