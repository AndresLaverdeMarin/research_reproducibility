###############################################################################
# Section 3: Descriptive Emissions Analysis (Figures 1-3)
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *

print("=" * 70)
print("SECTION 3: Descriptive Emissions Analysis (Figures 1-3)")
print("=" * 70)

df_clean = load_preprocessed(clean_only=True)
results = {}

# --- Figure 1: RW vs TA distributions ---
print("\n  Emission distribution statistics (Figure 1):")
print(f"  {'PT+Fuel':<16} {'RW Mean':>8} {'RW Std':>8} {'TA Mean':>8} "
      f"{'Gap Mean':>9} {'Gap Std':>8} {'N':>10}")
print("  " + "-" * 74)

for pt in PT_ORDER:
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
        results[f'rw_mean_{pt}_{fuel}'] = float(rw_mean)
        results[f'ta_mean_{pt}_{fuel}'] = float(ta_mean)
        results[f'gap_mean_{pt}_{fuel}'] = float(gap_mean)
        results[f'gap_pct_{pt}_{fuel}'] = float(sub['gap_percentage'].mean())

# PHEV gap range
df_phev = df_clean[df_clean['powertrain'] == 'PHEV']
phev_gap = df_phev['gap'].describe()
print(f"\n  PHEV gap range: median={phev_gap['50%']:.1f}, "
      f"Q1={phev_gap['25%']:.1f}, Q3={phev_gap['75%']:.1f} g/km")

# --- Figure 2: Country-level emissions ---
print("\n  Country-level average RW CO2 (Figure 2 -- top 5 by sample size):")
country_stats = (df_clean.groupby('EEA_MS')
                 .agg(RW_CO2=('RW_CO2', 'mean'),
                      TA_CO2=('EEA_Ewltp', 'mean'),
                      Gap=('gap', 'mean'),
                      N=('RW_CO2', 'count'))
                 .sort_values('N', ascending=False))
print(country_stats.head(5).to_string())

# --- Figure 3: Annual mileage by country ---
print("\n  Annual mileage by fuel (Figure 3 -- fleet medians):")
for fuel in ['Petrol', 'Diesel']:
    sub = df_clean[df_clean['fuel'] == fuel]['annual_mileage_km'].dropna()
    print(f"    {fuel}: median = {sub.median():,.0f} km, mean = {sub.mean():,.0f} km")

save_results('s3', results)
print("\nDone.")
