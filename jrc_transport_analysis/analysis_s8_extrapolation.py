###############################################################################
# Section 8: Fleet Extrapolation (Tables 3-4)
#
# Requires section 6 to have run first (loads saved models).
###############################################################################
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *
from sklearn.metrics import r2_score

print("=" * 70)
print("SECTION 8: Fleet Extrapolation (Tables 3-4)")
print("=" * 70)

# --- Load models from section 6 ---
models_path = os.path.join(OUTPUT_DIR, "s6_models.pkl")
if not os.path.exists(models_path):
    print("ERROR: s6_models.pkl not found. Run analysis_s6_mlr_models.py first.")
    raise SystemExit(1)

with open(models_path, 'rb') as f:
    m = pickle.load(f)

model_3a = m['model_3a']
model_3b = m['model_3b']
features_3a = m['features_3a']
features_3b = m['features_3b']
del m

# --- Load and prepare data ---
df_clean = load_preprocessed(clean_only=True)
df_model, _ = build_model_data(df_clean)
results = {}

warn_missing("FleetEU dataset (25M full registrations) not available -- "
             "fleet extrapolation uses OBFCM sample with model predictions. "
             "Stochastic imputation for unobserved fleet cannot be performed.")


# =========================================================================
# 8a. Table 3: Average RW CO2 and Gap
# =========================================================================
print("\n  8a. Table 3 -- Average RW CO2 and Gap (from OBFCM sample):")
print(f"  {'PT+Fuel':<16} {'RW CO2':>8} {'TA CO2':>8} {'Gap':>8} "
      f"{'Gap%':>8} {'N':>10}")
print("  " + "-" * 60)

for pt in PT_ORDER:
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


# =========================================================================
# 8b. Model-predicted RW CO2 (in-sample)
# =========================================================================
print("\n  8b. Model-predicted RW CO2 (in-sample prediction):")
print(f"  {'PT+Fuel':<16} {'Actual':>8} {'Predicted':>10} {'Diff':>8}")
print("  " + "-" * 46)

# Prepare model subsets
df_3a = df_model[df_model['EEA_Fm'].isin(['M', 'H'])][
    features_3a + ['RW_CO2', 'powertrain', 'fuel']].dropna(
    subset=features_3a + ['RW_CO2'])
df_3b = df_model[df_model['EEA_Fm'] == 'P'][
    features_3b + ['RW_CO2', 'fuel']].dropna(
    subset=features_3b + ['RW_CO2'])

del df_model  # free memory

for pt in PT_ORDER:
    for fuel in ['Petrol', 'Diesel']:
        if pt in ['ICEV', 'HEV']:
            sub_pf = df_3a[(df_3a['powertrain'] == pt) & (df_3a['fuel'] == fuel)]
            if len(sub_pf) < 100:
                continue
            actual = sub_pf['RW_CO2'].mean()
            predicted = model_3a.predict(sub_pf[features_3a].values).mean()
        else:
            if len(df_3b) < 100 or model_3b is None:
                continue
            sub_pf = df_3b[df_3b['fuel'] == fuel]
            if len(sub_pf) < 100:
                continue
            actual = sub_pf['RW_CO2'].mean()
            predicted = model_3b.predict(sub_pf[features_3b].values).mean()

        diff = predicted - actual
        print(f"  {pt + ' ' + fuel:<16} {actual:>8.1f} {predicted:>10.1f} "
              f"{diff:>+8.2f}")
        results[f'pred_rw_{pt}_{fuel}'] = float(predicted)


# =========================================================================
# 8c. Table 4: Estimated Annual Tailpipe Emissions
# =========================================================================
print("\n  8c. Table 4 -- Estimated Annual Tailpipe Emissions (OBFCM sample only):")
warn_missing("Total EU emissions (Table 4) require FleetEU data for full "
             "extrapolation. Computing sample-based estimate only.")

for year in [2021, 2022, 2023]:
    sub_yr = df_clean[df_clean['EEA_year'] == year]
    if len(sub_yr) == 0:
        continue

    rw_avg = sub_yr['RW_CO2'].mean()
    mileage_avg = sub_yr['annual_mileage_km'].mean()
    n_veh = len(sub_yr)

    mt_sample = rw_avg * mileage_avg * n_veh / 1e12  # g -> Mt
    print(f"  {year}: {n_veh:,} vehicles, avg RW = {rw_avg:.1f} g/km, "
          f"avg mileage = {mileage_avg:,.0f} km -> {mt_sample:.2f} Mt (sample only)")
    results[f'mt_sample_{year}'] = float(mt_sample)

save_results('s8', results)
print("\nDone.")
