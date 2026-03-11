###############################################################################
# Section 1: Representativeness Analysis (Appendix A)
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *

print("=" * 70)
print("SECTION 1: Representativeness Analysis (Appendix A)")
print("=" * 70)

df_clean = load_preprocessed(clean_only=True)
results = {}

warn_missing("FleetEU (full 24.5M registration dataset) not available -- "
             "representativeness comparison done within OBFCM sample only.")

# Sample composition
print("\n  Sample composition (OBFCM):")
pt_counts = df_clean['powertrain'].value_counts()
pt_pct = pt_counts / len(df_clean) * 100
for pt in PT_ORDER:
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
print("\n  Average mass and TA CO2 by powertrain (Table A2 -- sample only):")
print(f"  {'Powertrain':<12} {'Avg Mass [kg]':>14} {'Avg TA CO2 [g/km]':>18}")
print("  " + "-" * 46)
for pt in PT_ORDER:
    sub = df_clean[df_clean['powertrain'] == pt]
    avg_mass = sub['EEA_M'].mean()
    avg_ta = sub['EEA_Ewltp'].mean()
    print(f"  {pt:<12} {avg_mass:>14.1f} {avg_ta:>18.1f}")

results['sample_size'] = len(df_clean)
results['coverage_pct'] = 31.5  # paper value -- cannot verify without FleetEU

save_results('s1', results)
print("\nDone.")
