###############################################################################
# Section 7: Statistical Robustness (Appendix E)
#
# Requires section 6 to have run first (loads saved models).
###############################################################################
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_common import *
from scipy import stats

print("=" * 70)
print("SECTION 7: Statistical Robustness (Appendix E)")
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
country_cols = m['country_cols']
del m

# --- Rebuild model data ---
df_clean = load_preprocessed(clean_only=True)
df_model, _ = build_model_data(df_clean)
del df_clean

results = {}


# =========================================================================
# Reconstruct model datasets
# =========================================================================
df_3a = df_model[df_model['EEA_Fm'].isin(['M', 'H'])][features_3a + ['RW_CO2']].dropna()
X_3a = df_3a[features_3a].values
y_3a = df_3a['RW_CO2'].values
y_pred_3a = model_3a.predict(X_3a)

df_3b = df_model[df_model['EEA_Fm'] == 'P'][features_3b + ['RW_CO2']].dropna()
X_3b = df_3b[features_3b].values if len(df_3b) > 100 else None
y_3b = df_3b['RW_CO2'].values if len(df_3b) > 100 else None
y_pred_3b = model_3b.predict(X_3b) if X_3b is not None and model_3b is not None else None

del df_model  # free memory


# =========================================================================
# 7a. Breusch-Pagan Test for Heteroscedasticity
# =========================================================================
print("\n  7a. Breusch-Pagan Test for Heteroscedasticity")

def breusch_pagan_test(X, y, y_pred):
    """Breusch-Pagan test for heteroscedasticity."""
    residuals = y - y_pred
    resid_sq = residuals ** 2
    resid_sq_norm = resid_sq / resid_sq.mean()
    X_with_const = np.column_stack([np.ones(len(X)), X])
    beta, _, _, _ = np.linalg.lstsq(X_with_const, resid_sq_norm, rcond=None)
    resid_sq_pred = X_with_const @ beta
    ss_reg = np.sum((resid_sq_pred - resid_sq_norm.mean()) ** 2)
    lm_stat = ss_reg / 2.0
    df = X.shape[1]
    p_value = 1 - stats.chi2.cdf(lm_stat, df)
    return lm_stat, p_value

bp_stat_3a, bp_p_3a = breusch_pagan_test(X_3a, y_3a, y_pred_3a)
print(f"  Model III-a (ICEV/HEV): LM stat = {bp_stat_3a:.2f}, p = {bp_p_3a:.6f}")
het_msg = ('Heteroscedasticity present (p < 0.001)' if bp_p_3a < 0.001
           else 'No heteroscedasticity detected')
print(f"    -> {het_msg}")
results['bp_p_3a'] = float(bp_p_3a)

if X_3b is not None:
    bp_stat_3b, bp_p_3b = breusch_pagan_test(X_3b, y_3b, y_pred_3b)
    print(f"  Model III-b (PHEV):     LM stat = {bp_stat_3b:.2f}, p = {bp_p_3b:.6f}")
    het_msg = ('Heteroscedasticity present (p < 0.001)' if bp_p_3b < 0.001
               else 'No heteroscedasticity detected')
    print(f"    -> {het_msg}")
    results['bp_p_3b'] = float(bp_p_3b)


# =========================================================================
# 7b. HC1 Robust Standard Errors (Model III-a)
# =========================================================================
print("\n  7b. HC1 Robust Standard Errors (Model III-a)")

def hc1_robust_se(X, y, y_pred, add_const=True):
    """Compute HC1 robust standard errors (memory-efficient)."""
    n = len(y)
    if add_const:
        X_c = np.column_stack([np.ones(n), X])
    else:
        X_c = X
    k = X_c.shape[1]
    resid = y - y_pred

    XtX_inv = np.linalg.inv(X_c.T @ X_c)

    # HC1: (n/(n-k)) * (X'X)^-1 X' diag(e^2) X (X'X)^-1
    # Memory-efficient: avoid creating n x n diagonal matrix
    scale = n / (n - k)
    resid_sq = resid ** 2
    meat = (X_c * resid_sq[:, np.newaxis]).T @ X_c
    V_hc1 = scale * XtX_inv @ meat @ XtX_inv
    se_hc1 = np.sqrt(np.diag(V_hc1))

    # Regular OLS SE for comparison
    sigma2 = np.sum(resid_sq) / (n - k)
    V_ols = sigma2 * XtX_inv
    se_ols = np.sqrt(np.diag(V_ols))

    return se_ols, se_hc1

# Sample for performance
n_sample_hc1 = min(len(X_3a), 500000)
idx_sample = np.random.RandomState(42).choice(len(X_3a), n_sample_hc1, replace=False)
X_3a_sample = X_3a[idx_sample]
y_3a_sample = y_3a[idx_sample]
y_pred_3a_sample = model_3a.predict(X_3a_sample)

se_ols, se_hc1 = hc1_robust_se(X_3a_sample, y_3a_sample, y_pred_3a_sample)

print(f"  {'Variable':<30} {'OLS SE':>10} {'HC1 SE':>10} {'Ratio':>8}")
print("  " + "-" * 60)
key_vars_idx = {'EEA_Ewltp': features_3a.index('EEA_Ewltp'),
                'EEA_Ep': features_3a.index('EEA_Ep'),
                'EEA_M': features_3a.index('EEA_M')}
for var_name, var_idx in key_vars_idx.items():
    se_idx = var_idx + 1  # +1 for intercept
    ratio = se_hc1[se_idx] / se_ols[se_idx] if se_ols[se_idx] > 0 else np.nan
    print(f"  {var_name:<30} {se_ols[se_idx]:>10.6f} {se_hc1[se_idx]:>10.6f} "
          f"{ratio:>8.3f}")


# =========================================================================
# 7c. Tyre radius significance for PHEV
# =========================================================================
if X_3b is not None and model_3b is not None:
    print("\n  7c. Tyre radius significance for PHEV:")
    tyre_idx = features_3b.index('vdb_front_tyre_radius')
    coef_tyre = model_3b.coef_[tyre_idx]

    n_phev = len(X_3b)
    resid_3b = y_3b - y_pred_3b
    sigma2_3b = np.sum(resid_3b ** 2) / (n_phev - X_3b.shape[1] - 1)
    X_3b_c = np.column_stack([np.ones(n_phev), X_3b])
    try:
        XtX_inv_3b = np.linalg.inv(X_3b_c.T @ X_3b_c)
        se_tyre = np.sqrt(sigma2_3b * XtX_inv_3b[tyre_idx + 1, tyre_idx + 1])
        t_stat = coef_tyre / se_tyre
        p_tyre = 2 * (1 - stats.t.cdf(abs(t_stat), n_phev - X_3b.shape[1] - 1))
        print(f"  Tyre radius coef = {coef_tyre:.4f}, SE = {se_tyre:.4f}, "
              f"t = {t_stat:.4f}, p = {p_tyre:.4f}")
        results['p_tyre_phev'] = float(p_tyre)
    except np.linalg.LinAlgError:
        warn_missing("Could not compute tyre radius p-value (singular matrix).")

save_results('s7', results)
print("\nDone.")
