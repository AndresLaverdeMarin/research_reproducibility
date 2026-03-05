# reproduce_figures.py -- Code Documentation

Generates all figures from "Towards zero CO2 emissions: Insights from EU vehicle on-board data" (Suarez et al., 2025).

## Dependencies

- matplotlib, pandas, numpy, seaborn, scipy, scikit-learn
- Input: `obfcm_data.csv` (~2.2GB, 7.7M vehicle records)
- Output: `figures/` directory (8 PNG files at 200 DPI)

## Data Preparation (Lines 26-61)

Loads the full OBFCM dataset and derives computed columns:

| Derived Column     | Formula / Logic                                                  |
|--------------------|------------------------------------------------------------------|
| `fuel`             | Simplified fuel type from `EEA_Ft`: 'Petrol' or 'Diesel'        |
| `powertrain`       | Mapped from `EEA_Fm`: M->ICEV, H->HEV, P->PHEV                 |
| `pt_fuel`          | Concatenation of powertrain + fuel (e.g. "ICEV Petrol")          |
| `age_years`        | `OBFCM_ReportingPeriod - EEA_year + 0.5`                        |
| `annual_mileage_km`| `OBFCM_TotLifetimeDist_km / age_years` (capped 100-200,000)     |
| `power_to_mass`    | `EEA_Ep / EEA_M * 1000` (W/kg)                                  |

Outlier filtering (line 51-53): For ICEV/HEV, keeps only rows where RW_CO2 is within [TA-30, 3*TA]. PHEV rows are unfiltered.

Color scheme: Petrol=#1f77b4 (blue), Diesel=#d62728 (red), PHEV RW=#2ca02c (green), TA=grey.

## Figures

### Figure 1 (Lines 64-133): RW vs TA CO2 Distributions
- 2x3 subplot grid (rows: Petrol/Diesel, cols: ICEV/HEV/PHEV)
- Overlaid histograms (80 bins, 0-400 g/km) with probability density
- Inline horizontal box plots at top of each panel
- Vertical dashed lines for RW and TA averages

### Figure 2 (Lines 136-234): Country-Specific Emissions
- 3x1 subplot grid (one per powertrain)
- Grouped bars: light=TA, dark=RW, per fuel type
- Countries ordered by approximate temperature (south to north)
- Proportional circles for sample size, EU-median dashed lines
- Minimum sample: 30 vehicles per country-fuel group

### Figure 3 (Lines 237-313): Annual Mileage by Country
- 3x1 subplot grid (one per powertrain)
- Horizontal bars showing median annual mileage (in 10^3 km)
- Countries sorted by petrol median mileage
- Fleet-size circles at bar ends, fleet median vertical lines

### Figure 4 (Lines 316-402): RW CO2 and Gap vs Official TA CO2
- 2x3 subplot grid (rows: RW CO2/Gap, cols: ICEV/HEV/PHEV)
- Binned box plots along TA CO2 axis (bins: 15 g/km for ICEV/HEV, 10 for PHEV)
- Linear regression through bin medians
- 1:1 diagonal reference (top row) and gap=0 horizontal line (bottom row)

### Figure 5 (Lines 405-486): RW CO2 and Gap vs Lifetime Mileage
- 2x3 subplot grid (rows: RW CO2/Gap, cols: ICEV/HEV/PHEV)
- Binned box plots along distance axis (5,000 km bins, 0-100k)
- For PHEV top panel: green line showing vehicles with EDS ~50% (45-55%)
- Sample size annotations every other bin

### Figure 7 (Lines 489-): Variable Importance (LMG Decomposition)
- 2x2 subplot grid (rows: TA/RW CO2, cols: ICEV+HEV/PHEV)
- LMG (Lindeman, Merenda, Gold) R² decomposition — equivalent to R's
  `relaimpo::calc.relimp(type="lmg")` (Grömping, 2015)
- Averages each predictor group's marginal R² contribution across all p!
  orderings using the covariance-matrix shortcut (2^p subset fits in O(p³))
- Top row (TA CO2): Model I predictors (blue bars) — engine power, mass,
  volume, tyre radius, fuel type, powertrain/electric range, year
- Bottom row (RW CO2): baseline Model II (blue) vs extended Model III (red)
- Extended adds: TA CO2 (ICEV/HEV), TA CO2 + EDS (PHEV)
- Country treated as one predictor group (28 dummy columns)
- Sampled to 200k rows for performance (covariance-matrix approach)

### Figure A1 (Lines 590-632): Fleet Composition
- 1x2 subplot grid
- Left: Stacked horizontal bars by registration year (2021/2022/2023) per country
- Right: Stacked horizontal bars showing powertrain share (%) per country

### Figure C1 (Lines 635-722): RW CO2 vs Vehicle Mass
- 2x3 subplot grid (rows: RW CO2/Gap, cols: ICEV/HEV/PHEV)
- Binned box plots along mass axis (100 kg bins, 900-2800 kg)
- Regression lines with slope annotation (g/km per 100 kg)

### Figure C2 (Lines 725-793): RW CO2 vs Power-to-Mass Ratio
- 2x3 subplot grid (rows: RW CO2/Gap, cols: ICEV/HEV/PHEV)
- Binned box plots along power-to-mass axis (10 W/kg bins, 30-200)
- Linear trend for petrol, quadratic for diesel

### Figure C3 (Lines 796-868): PHEV CO2 vs Electric Range
- 2x1 subplot grid (rows: RW CO2/Gap)
- PHEV only, binned by official electric range (5 km bins, 10-130 km)
- Proportional circles for sample size in top panel

## Validation Table (Lines 871-901)

Reproduces Table 3 from the paper: fleet-wide average RW CO2, TA CO2, absolute gap, and gap percentage by powertrain and fuel type. Compares computed values against paper-reported values.
