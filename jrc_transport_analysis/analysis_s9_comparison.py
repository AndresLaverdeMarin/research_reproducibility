###############################################################################
# Section 9: Final Comparison Table -- Paper vs Computed Values
#
# Reads results from all section JSON files. No data loading required.
###############################################################################
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *

print("=" * 70)
print("SECTION 9: FINAL COMPARISON -- Paper Values vs Computed Values")
print("=" * 70)

# --- Load all section results ---
r = {}
for s in ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']:
    r.update(load_results(s))

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
    computed_rw = r.get(f'rw_mean_{pt}_{fuel}')
    computed_gap = r.get(f'gap_mean_{pt}_{fuel}')
    comparison.append({
        'Metric': f'{pt} {fuel} -- RW CO2 [g/km]',
        'Paper': paper_rw[key],
        'Computed': round(computed_rw, 1) if computed_rw is not None else 'N/A',
        'Diff': round(computed_rw - paper_rw[key], 1) if computed_rw is not None else 'N/A',
    })
    comparison.append({
        'Metric': f'{pt} {fuel} -- Gap [g/km]',
        'Paper': paper_gap[key],
        'Computed': round(computed_gap, 1) if computed_gap is not None else 'N/A',
        'Diff': round(computed_gap - paper_gap[key], 1) if computed_gap is not None else 'N/A',
    })

# --- Model R2 ---
r2_3a = r.get('r2_model_3a')
r2_3b = r.get('r2_model_3b')

comparison.append({
    'Metric': 'Model III-a R2 (ICEV/HEV)',
    'Paper': '75%',
    'Computed': f'{r2_3a * 100:.1f}%' if r2_3a else 'N/A',
    'Diff': f'{(r2_3a * 100 - 75):+.1f}pp' if r2_3a else 'N/A',
})
comparison.append({
    'Metric': 'Model III-b R2 (PHEV)',
    'Paper': '82%',
    'Computed': f'{r2_3b * 100:.1f}%' if r2_3b else 'N/A',
    'Diff': f'{(r2_3b * 100 - 82):+.1f}pp' if r2_3b else 'N/A',
})

# --- Key coefficients ---
paper_coefs = {
    'Coef III-a: TA CO2': (1.0136, r.get('coef_3a_ta')),
    'Coef III-a: Engine Power': (0.1473, r.get('coef_3a_power')),
    'Coef III-a: Mass': (-0.0063, r.get('coef_3a_mass')),
    'Coef III-b: TA CO2': (0.6518, r.get('coef_3b_ta')),
    'Coef III-b: Engine Power': (0.1814, r.get('coef_3b_power')),
    'Coef III-b: EDS': (-1.8606, r.get('coef_3b_eds')),
}
for label, (paper_val, computed_val) in paper_coefs.items():
    comparison.append({
        'Metric': label,
        'Paper': paper_val,
        'Computed': round(computed_val, 4) if computed_val is not None else 'N/A',
        'Diff': round(computed_val - paper_val, 4) if computed_val is not None else 'N/A',
    })

# --- TA vs RW correlation R2 ---
paper_ta_r2 = {'ICEV': 0.99, 'HEV': 0.99, 'PHEV': 0.94}
for pt, p_r2 in paper_ta_r2.items():
    c_r2 = r.get(f'ta_rw_r2_{pt}')
    comparison.append({
        'Metric': f'TA-RW Correlation R2 ({pt})',
        'Paper': p_r2,
        'Computed': round(c_r2, 4) if c_r2 is not None else 'N/A',
        'Diff': round(c_r2 - p_r2, 4) if c_r2 is not None else 'N/A',
    })

# --- LMG variable importance ---
lmg_paper = {
    'LMG III-a: TA CO2 [%]': (49.0, r.get('lmg_3a_ta_co2')),
    'LMG III-a: Engine Power [%]': (18.0, r.get('lmg_3a_power')),
    'LMG III-a: Mass [%]': (10.0, r.get('lmg_3a_mass')),
    'LMG III-b: EDS [%]': (51.0, r.get('lmg_3b_eds')),
}
for label, (paper_val, computed_val) in lmg_paper.items():
    comparison.append({
        'Metric': label,
        'Paper': f'{paper_val:.1f}%',
        'Computed': f'{computed_val:.1f}%' if computed_val is not None else 'N/A',
        'Diff': (f'{computed_val - paper_val:+.1f}pp'
                 if computed_val is not None else 'N/A'),
    })

# --- Total emissions ---
paper_mt = {2021: 20.9, 2022: 18.7, 2023: 20.5}
for yr, p_mt in paper_mt.items():
    c_mt = r.get(f'mt_sample_{yr}')
    comparison.append({
        'Metric': f'Total Emissions {yr} [Mt]',
        'Paper': p_mt,
        'Computed': f'{c_mt:.2f} (sample)' if c_mt is not None else 'N/A',
        'Diff': 'N/A -- needs FleetEU',
    })

# --- Annual mileage ---
comparison.append({
    'Metric': 'Annual mileage Petrol [km]',
    'Paper': '~11,500',
    'Computed': (f'{r["mileage_petrol"]:,.0f}'
                 if r.get('mileage_petrol') is not None else 'N/A'),
    'Diff': '',
})
comparison.append({
    'Metric': 'Annual mileage Diesel [km]',
    'Paper': '~22,700',
    'Computed': (f'{r["mileage_diesel"]:,.0f}'
                 if r.get('mileage_diesel') is not None else 'N/A'),
    'Diff': '',
})

# --- Print comparison table ---
print(f"\n{'Metric':<40} {'Paper':>14} {'Computed':>14} {'Diff':>18}")
print("-" * 88)
for row in comparison:
    print(f"{row['Metric']:<40} {str(row['Paper']):>14} "
          f"{str(row['Computed']):>14} {str(row['Diff']):>18}")

# Save to CSV
df_comp = pd.DataFrame(comparison)
csv_path = os.path.join(OUTPUT_DIR, "comparison_table.csv")
df_comp.to_csv(csv_path, index=False)
print(f"\n  Comparison table saved to: {csv_path}")
print("\nDone.")
