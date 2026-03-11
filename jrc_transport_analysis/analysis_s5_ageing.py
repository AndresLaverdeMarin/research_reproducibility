###############################################################################
# Section 5: Vehicle Ageing & Mileage Trends (Figures 5, 6)
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *

print("=" * 70)
print("SECTION 5: Vehicle Ageing & Mileage Trends (Figures 5, 6)")
print("=" * 70)

# Need FULL df (unfiltered) for tracking analysis
df = load_preprocessed(clean_only=False)
df_clean = df[df['is_clean']]
results = {}

# --- Figure 5: RW CO2 vs lifetime distance ---
print("\n  RW CO2 change with mileage (Figure 5):")
dist_bins = np.arange(0, 105000, 5000)

for pt in PT_ORDER:
    sub = df_clean[df_clean['powertrain'] == pt].copy()
    sub['dist_bin'] = pd.cut(sub['OBFCM_TotLifetimeDist_km'], bins=dist_bins)

    low_mileage = sub[sub['OBFCM_TotLifetimeDist_km'] < 10000]['RW_CO2'].median()
    high_mileage = sub[sub['OBFCM_TotLifetimeDist_km'].between(90000, 100000)]['RW_CO2'].median()

    if not np.isnan(low_mileage) and not np.isnan(high_mileage):
        delta = high_mileage - low_mileage
        print(f"  {pt}: RW CO2 at <10k km = {low_mileage:.1f}, "
              f"at 90-100k km = {high_mileage:.1f}, delta = {delta:+.1f} g/km")
        results[f'mileage_delta_{pt}'] = float(delta)

# --- Figure 6: Three-year tracking sample ---
print("\n  Three-year tracking sample (Figure 6):")
df_2021 = df[df['EEA_year'] == 2021].copy()
tracking_veh = df_2021.groupby('veh_id')['OBFCM_ReportingPeriod'].nunique()
multi_year = tracking_veh[tracking_veh >= 2].index

if len(multi_year) > 0:
    df_tracking = df_2021[df_2021['veh_id'].isin(multi_year)].copy()
    print(f"  Vehicles with multiple readouts: {len(multi_year):,}")

    for yr in sorted(df_tracking['OBFCM_ReportingPeriod'].unique()):
        sub_yr = df_tracking[df_tracking['OBFCM_ReportingPeriod'] == yr]
        for pt in PT_ORDER:
            sub_pt = sub_yr[sub_yr['powertrain'] == pt]
            if len(sub_pt) > 50:
                rw = sub_pt['RW_CO2'].median()
                print(f"    {pt} in {yr}: median RW CO2 = {rw:.1f} g/km "
                      f"(n={len(sub_pt):,})")
else:
    warn_missing("No vehicles found with multiple reporting years for tracking "
                 "analysis. Dataset may contain only deduplicated records.")

save_results('s5', results)
print("\nDone.")
