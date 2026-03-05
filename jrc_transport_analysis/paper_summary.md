# Towards Zero CO2 Emissions: Insights from EU Vehicle On-Board Data

**Authors:** Jaime Suarez, Alessandro Tansini, Markos A. Ktistakis, Andres L. Marin, Dimitrios Komnos, Jelica Pavlovic, and Georgios Fontaras
**Published in:** European Transport Research Review (2025)
**DOI:** [10.1186/s12544-025-00718-9](https://doi.org/10.1186/s12544-025-00718-9)
**Dataset:** [JRC OBFCM Dataset](https://data.jrc.ec.europa.eu/dataset/9528c82b-37fa-4da3-9b6b-b54eaf0ba4ac)

---

## 1. Main Idea

This paper presents a **data-driven methodology to assess real-world (RW) CO2 emissions** of European passenger cars using On-Board Fuel and Energy Consumption Monitoring (OBFCM) data. Transportation accounts for roughly one-quarter of total CO2 emissions, and despite the EU's ambitious target of zero-tailpipe-emission vehicles by 2035, a persistent **gap exists between official type-approval (TA) laboratory values and actual real-world performance**.

The study leverages a massive dataset of **7.7 million passenger cars** registered in the EU (plus Norway and Iceland) between 2021 and 2023 to:

- Quantify real-world emission factors for different powertrain technologies (ICEV, HEV, PHEV) and fuel types
- Identify the most influential factors driving real-world CO2 variability (vehicle attributes, driver behaviour, geography)
- Estimate total annual real-world CO2 emissions for the entire new EU vehicle fleet
- Assess how vehicle ageing and accumulated mileage affect fuel efficiency over time
- Provide environmental modellers and policymakers with measured, harmonised data for validating emission calculation models

---

## 2. Results

### 2.1 Real-World Emission Factors (g/km, 2021-2023 average)

| Powertrain | Petrol | Diesel |
|---|---|---|
| ICEV | 166.2 | 170.1 |
| HEV | 149.1 | 189.6 |
| PHEV | 131.4 | 149.5 |

### 2.2 Type-Approval vs. Real-World Gap

**Relative gap:** ICEVs and HEVs show a stable gap of **19-20%**. PHEVs show a dramatically larger gap of **280-320%**.

| Powertrain | Petrol (g/km) | Diesel (g/km) |
|---|---|---|
| ICEV | +27.3 | +28.1 |
| HEV | +24.9 | +31.7 |
| PHEV | +97.6 | +116.6 |

### 2.3 Total Annual Real-World CO2 Emissions (EU fleet)

| Year | Total (Mt CO2) |
|---|---|
| 2021 | 20.9 |
| 2022 | 18.7 |
| 2023 | 20.4 |

Petrol ICEVs are the largest emission source (~35%), while diesel's share fell from 34.8% (2021) to 26.2% (2023).

### 2.4 Key Drivers of Variability

- **Vehicle mass and engine power** are the primary drivers for ICEVs and HEVs
- Mass sensitivity: +15.2 g/km per 100 kg extra mass (petrol), +9.4 g/km (diesel)
- **Electric Driving Share (EDS)** is the dominant variable for PHEVs, explaining **51%** of their RW CO2 variance
- **Ageing/mileage effects:**
  - ICEV emissions *decrease* by ~10 g/km after 100,000 km (reduced friction, more highway driving)
  - PHEV emissions *increase* with mileage (up to +40 g/km for petrol) due to reduced battery use
- **Geography:** Northern countries (Finland, Norway, Sweden) show lower emissions; island nations (Cyprus, Malta) show the highest

### 2.5 Regression Model Results

| Model | R-squared |
|---|---|
| TA CO2 (ICEV/HEV) | 86% |
| TA CO2 (PHEV) | 80% |
| RW Baseline (ICEV/HEV) | 68% |
| RW Baseline (PHEV) | 36% |
| RW Extended incl. EDS/TA (ICEV/HEV) | 75% |
| RW Extended incl. EDS/TA (PHEV) | 82% |

Key coefficients: EDS (PHEV) = -1.8606 (higher electric share significantly lowers CO2); TA CO2 = 1.0136 (ICEV/HEV), 0.6518 (PHEV).

### 2.6 PHEV-Specific Findings

- PHEV emissions are lower than ICEVs but **vastly exceed TA values** because users charge less frequently than regulations assume
- PHEV owners drive **longer annual distances** than ICEV owners (15,100 km vs 11,600 km for petrol)
- Optimal efficiency (~100 g/km) reached at **~70 km electric range**; beyond this, emissions rise because these vehicles tend to be larger, high-end models

### 2.7 Annual Mileage (Median)

- Petrol ICEV/HEV: 11,200-11,600 km
- Diesel (all types): 22,700-25,500 km (nearly double petrol)

---

## 3. Constraints and Limitations

1. **Non-random sampling:** The OBFCM dataset may overrepresent certain fleet segments (e.g., corporate vehicles), potentially skewing emission estimates. The sample overestimates RW CO2 by an average of 1.8 g/km compared to full fleet extrapolation.

2. **No transient data:** OBFCM records lifetime cumulative values, so it cannot capture transient conditions such as weather fluctuations, road gradients, or individual trip dynamics.

3. **Readout timing uncertainty:** The exact date of data collection is unknown (only the year is recorded), requiring Poisson distribution models to estimate annual mileage.

4. **Early data bias:** The 2021 OBFCM sample had a bias toward larger vehicles that are driven longer distances.

5. **Heteroscedasticity:** Vehicle-level regression models exhibited unstable variance in residuals (country-level models did not).

6. **Country-level overfitting risk:** Only 29 country observations relative to the number of predictor variables increases overfitting risk in country-level analysis.

7. **Aggregation effects:** Country-level aggregation smooths within-country variability, potentially overestimating macro-level factor contributions.

8. **PHEV scope:** The study focuses on tailpipe CO2 only and does not integrate electricity use into a full well-to-wheel (WTW) energy analysis.

---

## 4. Methodology

### 4.1 Data Collection and Preprocessing

- **Source:** OBFCM datasets for 2021, 2022, and 2023 published by the European Environmental Agency (EEA)
- **Augmentation:** Merged with public vehicle databases (for dimensions and transmission details) and Eurostat statistics (for country-level infrastructure, population density, weather)
- **Deduplication:** For vehicles appearing in multiple reporting years, only the most recent entry was retained
- **Outlier filtering:** For ICEVs and HEVs, excluded vehicles where: `CO2_TA - 30 < CO2_RW < 3 * CO2_TA`
- **Final dataset:** 7.7 million vehicles covering 31% of total registrations

### 4.2 Real-World Calculations

- **RW Fuel Consumption** = Total lifetime fuel consumed / Total lifetime distance
- **RW CO2 Emissions** (g/km) = RW fuel consumption x fuel-dependent conversion factor
- **Electric Driving Share (EDS)** for PHEVs = proportion of useful traction energy delivered electrically relative to total energy from grid and combustion
- **Gap** = RW CO2 - TA CO2 (absolute, g/km) or (RW CO2 - TA CO2) / TA CO2 x 100 (relative, %)

### 4.3 Statistical Methods

- **Multivariable Linear Regression (MLR)** chosen for transparency and policy suitability
- **Variable selection:** Variance Inflation Factor (VIF) analysis (threshold < 5) and stepwise selection guided by Akaike Information Criterion (AIC)
- **Predictors:** Technical attributes (mass, engine power, tyre radius), categorical factors (fuel type, year, country), behavioural indicators (mileage, EDS)
- **Variance decomposition:** LMG (Lindeman, Merenda, Gold) method to attribute explained variance (R-squared) to individual predictors

### 4.4 Total Fleet Emissions Estimation

- Applied best-performing regression models (from OBFCM sample) to the official EEA CO2 monitoring dataset (full registry of new vehicles)
- **Stochastic imputation:** Mileage and EDS values imputed via stochastic sampling from OBFCM distributions, stratified by powertrain, country, and year
- **Aggregation formula:** Total CO2 = Average RW CO2 x Annual Mileage x Number of Vehicles / 10^9 (yielding million tonnes)
