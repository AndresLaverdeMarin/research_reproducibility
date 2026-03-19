# A Deep Reinforcement Learning Approach for Ramp Metering Based on Traffic Video Data

**Authors:** Bing Liu, Yu Tang, Yuxiong Ji, Yu Shen, and Yuchuan Du

**DOI:** [https://doi.org/10.1155/2021/6669028](https://doi.org/10.1155/2021/6669028)
**Preprint:** [https://arxiv.org/abs/2012.12104](https://arxiv.org/abs/2012.12104)

---

## 1. Research Question and Objectives

The paper explores whether traffic video data can improve the efficiency of ramp metering through Deep Reinforcement Learning (DRL). Traditional ramp metering methods rely on predefined measurements from point detectors (e.g., loop detectors), which capture data at fixed locations. The authors investigate whether a DRL agent can learn optimal control strategies directly from high-dimensional visual inputs, extracting richer information such as vehicle locations, speeds, and headways over larger spatial areas than point detectors can provide.

## 2. Methodology

### 2.1 Overall Framework

The study proposes a DRL framework for local ramp metering with the following components:

- **State Representation:** Vehicle locations are extracted from raw video frames and reformed into position matrices. Matrices from N=3 consecutive time steps are stacked to capture vehicle dynamics, yielding a final state dimension of **(3, 4, 512)**.
- **Action Set:** A flexible two-phase control scheme where the agent decides whether the next time step will be **green (G)** or **red (R)**.
- **Reward Function:** Balances average speed in the merging area (mainline mobility) and average queue length at the on-ramp (vehicle delays):
  - `r_t = mu * v_bar_t + omega * q_bar_t`
  - `mu = 0.5` (positive, for speed improvement), `omega = -0.1` (negative, penalizing long queues)

### 2.2 Neural Network Architecture

A revised Deep Q-Network (~2 million weights) based on Mnih et al. (2013):

| Layer | Type | Details |
|---|---|---|
| Conv 1 | Convolutional | 32 filters, size 1x8, stride 1x4 |
| Conv 2 | Convolutional | 64 filters, size 1x4, stride 1x2 |
| Conv 3 | Convolutional | 64 filters, size 1x3, stride 1x1 |
| FC Branch 1 | Fully Connected | 256 units -> 2 outputs (Q-values for Green/Red) |
| FC Branch 2 | Fully Connected | 256 units -> 2 outputs (speed and queue predictions) |

- **Activation:** ReLU after every convolutional and fully connected layer
- **Stabilization:** Experience replay buffer and target network

### 2.3 Multitask Learning

The network simultaneously learns to maximize rewards (Q-values) and predict auxiliary traffic features (mean speed and queue length). The total loss function is:

`L = L1 + lambda * L2` where `lambda = 0.001`

### 2.4 Training Hyperparameters

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning rate | 2.5 x 10^-4 |
| Exploration strategy | epsilon-greedy (epsilon = 0.1) |
| Batch size | 32 |
| Training frames | 10^6 (convergence at ~400,000) |
| Decision step size | 4 seconds |
| Replay buffer size | 2 x 10^5 transitions |
| Target network freeze interval | 10^4 |
| Episode length | 4,200 decision time steps |

### 2.5 Simulation Setup

- **Simulator:** SUMO (Simulation of Urban MObility) -- open-source microscopic traffic simulator
- **Case Study:** Real-world freeway segment in Shandong, China (Qingdao-Huangdao route through a tunnel)

**Road Network Dimensions:**

| Segment | Length |
|---|---|
| Upstream mainline | 300 m |
| Merging area | 150 m |
| Downstream mainline | 1,000 m |
| On-ramp | 400 m |

Configuration: three-lane mainline, one-lane on-ramp.

### 2.6 Position Matrix Construction

1. Vehicles are represented as location points (x_i, y_i) extracted from video frames
2. A matrix `m_t` of size X x Y is constructed; cell (x_i, y_i) is set to a constant U_V if a vehicle is present, zero otherwise
3. The current signal state is embedded: the cell at the signal position is set to U_G (green) or U_R (red)
4. Raw data is down-sampled to 4 x 512 pixels
5. Matrices from 3 consecutive time steps are stacked to capture dynamics

## 3. Key Findings and Results

The DRL method was compared against a **no-control** scenario and **PI-ALINEA** (a state-of-the-practice feedback control law):

| Metric | DRL | PI-ALINEA | No Control |
|---|---|---|---|
| Median travel time reduction | **20%** | 11.7% | baseline |
| Max 75th-percentile queue length | **67 m** | 126 m | -- |

Additional findings:

- **Higher throughput:** During peak periods, the DRL method maintained higher and more stable traffic flows downstream of the merging area, better alleviating the "capacity drop" effect.
- **Information utilization:** A perturbation analysis confirmed that the DRL controller effectively utilizes spatio-temporal information from multiple subareas within the video frame, rather than just the specific locations where traditional sensors would be placed.

## 4. Main Contributions

1. **Visual-based control:** First study (to the authors' knowledge) to learn optimal ramp metering strategies directly from visual inputs rather than traditional traffic measurements.
2. **Advanced DRL framework:** Incorporates position matrices, multitask learning, and stabilization techniques to handle high-dimensional video data.
3. **Superior performance:** Outperforms traditional fine-tuned algorithms (PI-ALINEA) in mobility, stability, and queue control.
4. **Practical deployment:** The resulting model is lightweight and suitable for deployment using existing communication and camera infrastructure.

## 5. Code and Data Availability

### Source Code

No public source code repository (e.g., GitHub) is provided by the authors. Researchers interested in the implementation would need to contact the corresponding author.

### Dataset

The paper includes a data availability statement: **data used to support the study's results are available from the corresponding author upon request.**

- Simulation parameters and traffic volumes (mainline and on-ramp) were based on empirical data from the Qingdao-Huangdao freeway segment in Shandong, China.
- No direct link to SUMO configuration files is provided.

### Open-Source Tools Used

- **SUMO** (Simulation of Urban MObility): [https://eclipse.dev/sumo/](https://eclipse.dev/sumo/) -- open-source microscopic traffic simulator used for all experiments.

### Contact

- **Corresponding author:** Yu Shen (yshen@tongji.edu.cn)

---

*Summary generated from NotebookLM source-grounded research, March 2026.*
