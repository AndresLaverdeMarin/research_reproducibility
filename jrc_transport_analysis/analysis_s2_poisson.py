###############################################################################
# Section 2: Poisson Model for Readout Timing (Appendix B)
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *

print("=" * 70)
print("SECTION 2: Poisson Model for Readout Timing (Appendix B)")
print("=" * 70)

df_clean = load_preprocessed(clean_only=True)
results = {}

# Filter: 2021-registered vehicles with 2023 readouts
df_poisson = df_clean[
    (df_clean['EEA_year'] == 2021) &
    (df_clean['OBFCM_ReportingPeriod'] == 2023)
].copy()

if len(df_poisson) == 0:
    warn_missing("No 2021-registered vehicles with 2023 readouts found.")
else:
    print(f"  Vehicles for Poisson model: {len(df_poisson):,}")
    print(f"    (2021-registered, 2023 readout)")

    for fuel in ['Petrol', 'Diesel']:
        sub = df_poisson[df_poisson['fuel'] == fuel]['annual_mileage_km'].dropna()
        if len(sub) > 0:
            med = sub.median()
            mean = sub.mean()
            print(f"  {fuel}: median annual mileage = {med:,.0f} km, "
                  f"mean = {mean:,.0f} km (n={len(sub):,})")

    # Paper values for comparison
    results['poisson_p'] = 3.7e-3
    results['poisson_r2'] = 0.9
    results['mileage_petrol'] = float(
        df_poisson[df_poisson['fuel'] == 'Petrol']['annual_mileage_km'].median())
    results['mileage_diesel'] = float(
        df_poisson[df_poisson['fuel'] == 'Diesel']['annual_mileage_km'].median())

    print(f"\n  Poisson model parameters (from paper):")
    print(f"    p = {results['poisson_p']}")
    print(f"    R2 = {results['poisson_r2']}")
    warn_missing("Exact readout dates not in dataset -- Poisson fitting uses "
                 "paper parameters. Annual mileage validated from data.")

save_results('s2', results)
print("\nDone.")
