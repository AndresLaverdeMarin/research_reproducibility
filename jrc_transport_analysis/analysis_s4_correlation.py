###############################################################################
# Section 4: Vehicle Characteristic Correlation (Figure 4)
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *
from scipy import stats

print("=" * 70)
print("SECTION 4: Vehicle Characteristic Correlation (Figure 4)")
print("=" * 70)

df_clean = load_preprocessed(clean_only=True)
results = {}

ta_bin_size = {'ICEV': 15, 'HEV': 15, 'PHEV': 10}

for pt in PT_ORDER:
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
        slope, intercept, r_val, p_val, std_err = stats.linregress(
            bin_positions, bin_medians.values)
        r2 = r_val ** 2
        print(f"  {pt}: R2 = {r2:.4f} (slope = {slope:.4f}, intercept = {intercept:.1f})")
        results[f'ta_rw_r2_{pt}'] = float(r2)
    else:
        print(f"  {pt}: insufficient bins for regression")

save_results('s4', results)
print("\nDone.")
