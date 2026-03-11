###############################################################################
# Section 0: Data Loading & Preprocessing
#
# Loads the full CSV (selected columns only), computes derived columns,
# and saves a compact pickle. Run this FIRST before any other section.
###############################################################################
import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("SECTION 0: Data Loading & Preprocessing")
print("=" * 70)

# --- Load only the columns actually used across all sections ---
NEEDED_COLS = [
    'EEA_Ft', 'EEA_Fm', 'EEA_year', 'OBFCM_ReportingPeriod',
    'OBFCM_TotLifetimeDist_km', 'EEA_Ep', 'EEA_M', 'EEA_Ewltp',
    'EEA_Zr', 'EEA_MS', 'RW_CO2', 'RW_eds', 'gap', 'gap_percentage',
    'vdb_vehicle_length', 'vdb_vehicle_width', 'vdb_vehicle_height',
    'vdb_front_tyre_radius', 'veh_id',
]

csv_path = os.path.join(BASE_DIR, 'obfcm_data.csv')
print("Loading OBFCM data (selected columns only)...")
df = pd.read_csv(csv_path, usecols=NEEDED_COLS, low_memory=False)
print(f"  Loaded: {len(df):,} rows, {len(df.columns)} columns")

# --- Derived columns ---
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

df['volume'] = (df['vdb_vehicle_length']
                * df['vdb_vehicle_width']
                * df['vdb_vehicle_height'])

# --- Outlier filter flag ---
n_before = len(df)
mask_icevhev = df['EEA_Fm'].isin(['M', 'H'])
mask_outlier = ((df['RW_CO2'] > (df['EEA_Ewltp'] - 30))
                & (df['RW_CO2'] < 3 * df['EEA_Ewltp']))
df['is_clean'] = ~mask_icevhev | mask_outlier
n_after = df['is_clean'].sum()
print(f"  Outlier filter: {n_before:,} -> {n_after:,} "
      f"({n_before - n_after:,} removed)")

# --- Drop columns only used for derivation ---
df.drop(columns=['EEA_Ft', 'vdb_vehicle_length',
                  'vdb_vehicle_width', 'vdb_vehicle_height'], inplace=True)

# --- Convert strings to categoricals to save memory ---
for col in ['fuel', 'powertrain', 'pt_fuel', 'EEA_Fm', 'EEA_MS']:
    if col in df.columns:
        df[col] = df[col].astype('category')

# --- Summary ---
df_clean = df[df['is_clean']]
print(f"  ICEV: {(df_clean['powertrain'] == 'ICEV').sum():,} | "
      f"HEV: {(df_clean['powertrain'] == 'HEV').sum():,} | "
      f"PHEV: {(df_clean['powertrain'] == 'PHEV').sum():,}")
print(f"  Memory usage: {df.memory_usage(deep=True).sum() / 1e6:.0f} MB")

# --- Save ---
pkl_path = os.path.join(OUTPUT_DIR, "preprocessed.pkl")
df.to_pickle(pkl_path)
print(f"  Saved to: {pkl_path}")
print(f"  File size: {os.path.getsize(pkl_path) / 1e6:.0f} MB")
print("\nDone. Run analysis_s1 through analysis_s9 next.")
