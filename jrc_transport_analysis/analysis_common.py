###############################################################################
# Shared utilities for sectioned analysis scripts
###############################################################################
import os
import json
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis_outputs")
PREPROCESSED_PATH = os.path.join(OUTPUT_DIR, "preprocessed.pkl")

PT_ORDER = ['ICEV', 'HEV', 'PHEV']

os.makedirs(OUTPUT_DIR, exist_ok=True)

missing_input_warnings = []


def warn_missing(msg):
    print(f"  WARNING: {msg}")
    missing_input_warnings.append(msg)


def load_preprocessed(clean_only=True):
    """Load preprocessed pickle. Returns df_clean by default, or full df."""
    if not os.path.exists(PREPROCESSED_PATH):
        print(f"ERROR: {PREPROCESSED_PATH} not found.")
        print("Run analysis_s0_data_prep.py first.")
        raise SystemExit(1)
    df = pd.read_pickle(PREPROCESSED_PATH)
    if clean_only:
        return df[df['is_clean']].copy()
    return df


def build_model_data(df_clean):
    """Add dummy variables needed for MLR models. Returns (df_model, country_cols)."""
    df_model = df_clean.copy()
    df_model['fuel_petrol'] = (df_model['fuel'] == 'Petrol').astype(float)
    df_model['pt_hev'] = (df_model['EEA_Fm'] == 'H').astype(float)
    country_dummies = pd.get_dummies(
        df_model['EEA_MS'], prefix='c', drop_first=True, dtype=float)
    country_cols = sorted(country_dummies.columns.tolist())
    df_model = pd.concat([df_model, country_dummies[country_cols]], axis=1)
    return df_model, country_cols


def save_results(section_name, results_dict):
    """Save section results to JSON."""
    path = os.path.join(OUTPUT_DIR, f"{section_name}_results.json")
    clean = {}
    for k, v in results_dict.items():
        if isinstance(v, (np.integer,)):
            clean[k] = int(v)
        elif isinstance(v, (np.floating,)):
            clean[k] = float(v) if not np.isnan(v) else None
        else:
            clean[k] = v
    with open(path, 'w') as f:
        json.dump(clean, f, indent=2)
    print(f"\n  Results saved to: {path}")


def load_results(section_name):
    """Load section results from JSON."""
    path = os.path.join(OUTPUT_DIR, f"{section_name}_results.json")
    if not os.path.exists(path):
        print(f"  WARNING: Results not found: {path}")
        return {}
    with open(path) as f:
        return json.load(f)
