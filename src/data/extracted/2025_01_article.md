R E S C I E N C E C

Replication / Computational Neuroscience
[Re] Model of thalamocortical slow-wave sleep
oscillations and transitions to activated states

Mathilde Reynes1,2, ID and Amélie Aussel1,2, ID
1INRIA Bordeaux Sud-Ouest, Bordeaux, France – 2Institut des Maladies Neurodégénératives, Université de Bordeaux, Centre
National de la Recherche Scientifique, UMR 5293, Bordeaux, France

Edited by
Nicolas P. Rougier ID

Reviewed by
Hans Ekkehard Plesser ID
Andrew P. Davison ID

A replication of Bazhenov M, Timofeev I, Steriade M, Sejnowski TJ. Model of thalamocortical slow‐wave sleep oscillations and transitions to activated states. J Neurosci. 2002
Oct 1;22(19):8691‐704
This articles reuses some of the figures from the original article [1], Copyright 2002 Society for Neuroscience.

Received
27 August 2024

Published
17 July 2025

DOI
10.5281/zenodo.16529268

## 1 Reproducibility Summary

Scope of Reproducibility — ‘Model of thalamocortical slow‐wave sleep oscillations and transitions to activated States’ by the original paper [1] portrays a biologically realistic model
of the thalamo‐cortical system exhibiting the oscillatory and cellular activity characteristic of deep‐sleep stages and transition to activated states. Our goal is to reproduce the
model and its claims.

Methodology — In order to replicate the paper’s results and validate its claims, we use the
free open source simulator for spiking neural networks Brian2 [2] and recreate the model
from the ground up using material provided in the original manuscript [1]. The full code
is available on the following GitHub Repository and the dataset used for plotting was
made accessible on Zenodo [3].

Results — As expected from the replication of a 20 years old paper, some variability was
observed although the main behavior was duplicated. As a result, most of the claims
from the original paper could be reproduced.

Discussion — While the equations were given in the original paper, some inaccuracies and
omissions made the reproduction more complex than expected. Indeed, while the code
available on ModelDB [4, 5] immensely helped the reproduction, it was not matching
some of the paper’s statements.

Communication with the authors — During the replication process, we have been in contact
with the first author of the original paper. He was supportive of our work and pointed us
to the current Git repository of his team, which includes more recent models developed
on the basis of the one we present here. He accepted to read this manuscript before
submission (though we did not get comments or other feedback from him to this date).


Code is available at https://github.com/Mathilde-Reynes/ReynesAussel2024.git. – SWH swh:1:dir:1c5cf4c4cdd6d63f6819b3dad65231465f85e42e.
Data is available at https://doi.org/10.5281/zenodo.13376370.
Open peer review is available at https://github.com/ReScience/submissions/issues/87.




## 2 Abstract

During sleep, distinct electrophysiological rhythms can be observed, which form the basis for classifying sleep into various stages: rapid eye movement (REM) sleep, and nonREM sleep stages N1 (Stage 1), N2 (Stage 2), and N3 (Stage 3, also known as slow wave
sleep or SWS) [6, 7]. Although a definitive consensus on the precise role of SWS in memory consolidation remains elusive [8], substantial evidence suggests that SWS‐rich sleep
is crucial for the consolidation of both declarative (hippocampus‐dependent) memories
[9, 10, 11] but also non‐declarative memories (hippocampus‐independent) ones [12, 13,
14]. While these findings can sometimes appear contradictory, they largely converge on
the ‘sequential hypothesis’ which posits that the optimal consolidation of both declarative and non‐declarative memories occurs when SWS and rapid eye movement (REM)
sleep sequentially follow one another [15]. Consolidation refers to the process wherein,
after an experience is initially encoded, a series of automatic and unconscious changes
at the cellular, molecular, and systems levels occur, leading to the transformation of
recently acquired, unstable memories into stable, long‐term ones [16, 17, 18, 19]. The
features of memory consolidation can be attributed to the specific patterns of the brain
electrical activity as well as their precise coordination during the various stages of sleep.
During SWS, slow oscillations are predominantly observed, characterized by alternating active (Up) and silent (Down) cortical states at a frequency of 0.2–1 Hz. These oscillations are prominently visible in EEG, as well as in extracellular and intracellular
recordings [20, 21, 22]. During Up states, most cortical cells are relatively depolarized
and capable of generating action potentials. Conversely, during Down states, most cortical neurons are hyperpolarized and remain inactive [20, 23, 22]. Additionally, these
slow oscillations may nest faster spindles, commonly occurring during down‐to‐Up state
transitions and observed in the thalamus [24, 25]. Such slow oscillations are believed to
establish a supra‐ordinate temporal framework for communication between areas, unifying cortical, thalamic and hippocampal structures, promoting a synchronized reactivation of memory representations [26, 27, 28, 29]. Timofeev and colleagues [22] as well
as Bazhenov et al. [1] conducted seminal research investigating the thalamo‐cortical
system during slow wave sleep, with an integrated approach combining experimental
and modeling work. These two papers laid the groundwork for a series of publications
geared towards the elucidation of the role of the thalamo‐cortical system in memory
consolidation and the interaction between the different subsystems involved [30, 31, 32,
33, 34]. The robustness of these papers stems from their commitment to achieving biological plausibility, evident in the attention given to both the connectivity and anatomical features of the modeled areas, as well as the precision of neuronal modeling which
included a wide range of distinct ionic currents. Because this specific model successfully depicted two areas involved in memory consolidation and replicated the associated
oscillations during SWS (cortical slow wave and thalamic spindles), it holds particular
relevance in the pursuit of developing a biologically realistic system for studying memory processes. Thus, we decided to work towards the reproduction of this model and
its results. We chose to develop in Brian2 [2], ensuring ease of use regardless of one’s
background. As a Python‐based simulator specifically designed for neural simulations,
Brian2 allowed us to write concise and readable code, with an easier and straightforward
syntax, while leveraging well‐known and widely used scientific libraries. Additionally,
the extensive support provided by the Brian2 team, its rich community and the comprehensive documentation are also enormous advantages over C++. Replication of the
original results was hindered due to the paper’s omissions and inconsistencies with the
provided code on ModelDB [5]. Furthermore, while the authors have made some efforts
in commenting few sections of the code, the code readability could be enhanced by
reviewing the implementation in light of current coding standards. Replication is still
considered successful as we were able to reproduce most of the original paper’s claims
and results. We believe our work can help facilitate access to this important original




piece of work.

## 3 Scope of Reproducibility

This report explores the replicability of the study conducted by Bazhenov and colleagues
[1] with the goal of substantiating its main assertions. These assertions can be arranged
in 6 categories.

Concerning the spontaneous behavior of cortical cells:

• Claim 1: Mechanism of Up‐state initiation. Random summation of miniature excitatory postsynaptic potentials (miniEPSPs) is sufficient to depolarize a cell to the
level where persistent sodium channels (Na(p)) are activated, which, followed by
a spike, initiates spread of activity over the whole network.

• Claim 2: Sustained up‐state activity. Network activity is maintained by Na(p) activation and pyramidal (PY) to pyramidal cells AMPA and NMDA mediated synaptic
interconnections.

• Claim 3: Up‐state termination. PY to PY depression and slow calcium‐dependent
potassium current terminated firing (but a sufficiently high level of inhibition
from cortical inhibitory interneurons (IN) is also required)

• Claim 4: Firing frequency of Pyramidal cells. PY cells fire at higher frequency

during the initial phase of depolarized state, and is lessened afterwards.

With respect to the spatiotemporal pattern of the cortical slow oscillations:

• Claim 5: Size of the network. The frequency of slow oscillations increases with

the number of PY neurons.

• Claim 6: MiniEPSPs amplitude. The frequency of slow oscillations increases with

the amplitude of the miniEPSPs.

• Claim 7: Shape of the miniEPSPs rate function. The shape of the function delineating the average rate of the miniEPSPs has minimal impact on the dynamics of
the network.

• Claim 8: Coupling strengh of PY to PY and PY to IN. Increasing the maximal conductance between PY neurons extended the duration of active states, while decreasing the AMPA‐mediated conductance from PY to IN cells enhanced the regularity of SWS oscillations.

• Claim 9: Velocity of spiking patterns. Spiking patterns propagate with a velocity
that depends on the maximal conductances for synaptic interconnections PY–PY
and PY–IN.

• Claim 10: Impact of thalamic input on pattern of slow oscillations. Reticular (RE)
and thalamic relay cells (TC) are not necessary to maintain slow oscillations but
change their spatiotemporal pattern of activity. TC‐PY AMPA interactions increase
the duration of cortical Up states.

Concerning the spontaneous behavior of thalamic cells:

• Claim 11: Thalamic spindle initiation. In TC cells, activity consistently begins
with hyperpolarization. This hyperpolarization is initiated by spiking in PY cells,
which leads to bursting in RE cells and subsequently hyperpolarizes TC cells. Following this, there is de‐inactivation of the low‐threshold calcium current, leading
to a rebound low‐threshold spike. Most TC cells do not frequently fire sodium




spikes; instead, they often exhibit a few cycles of sub‐threshold ≈ 10 Hz oscillations, followed by a few cycles with low‐threshold spikes that culminate in action
potentials.

• Claim 12: Spindle termination. Powerful PY‐RE AMPA interactions lead to depolarization of RE, inactivation of low‐threshold calcium current and eventually termination of rebound oscillations.

Regarding the transition to awake state:

• Claim 13: Critical role of potassium leak and PY‐PY conductance. Simultaneously
blocking potassium leak current in PY and TC and changing PY‐PY synaptic current eliminates the silent phases of SWS oscillations. This results in PY cells firing
at 30‐40Hz, while RE and TC cells remain silent.

• Claim 14: Neuron’s input resistance. The changes mentioned in Claim 12 can alter

the input resistance of PY cells.

With respect to electrical stimulation:

• Claim 15: Cortical response during thalamic stimulation. The thalamocortical
network’s ability to transmit sensory input is diminished during SWS compared to
awake state. Intrinsic network oscillations mask low‐frequency stimulation more
severely than higher‐frequency input.

## 4 Methodology

### 4.1 Model description

The original model [1] incorporated a representation of the thalamus with both thalamic
relay (TC) and reticular (RE) neurons, in conjunction with a model of a cortical column
of the prefrontal cortex containing pyramidal neurons (PY) and inhibitory interneurons
(IN). All neurons modeled adhere to the Hodgkin–Huxley formalism [35]. Unless explicitly mentioned, the equations and parameters governing this model are identical to the
original paper, and only the most important ones are recalled here.

Cortical model — Pyramidal cells (PY) and inhibitory interneurons (IN) were modeled as
two‐compartments such that

Cm

dVD
dt

= −gL(VD − EL) − IS→D − I int
D

− I syn,

describes the membrane potential of the dendritic compartment and

Cm

dVS
dt

= −ID→S − I int
S

(1)

(2)

defines the membrane potential of the axosomatic compartment.
I int
D and I int
S allude to the sums of active intrinsic currents of the two compartments, and
I syn to the sum of synaptic currents. IS→D and ID→S describe the interaction between
the two compartments of the cells.

The axosomatic compartment include a fast Na+ current INa, a persistent Na+ current
INa(p) and a fast delayed rectifier K+ current IK. The dendritic compartment include
INa, INa(p) as well as a slow voltage‐dependent non‐inactivating K+ current,IKm, a highthreshold Ca2+ current IHVA, a slow Ca2+‐dependent K+ current IKCa and a K+ leak current.
These are defined as

I int
D = INa + INa(p) + IKm + IHVA + IKCa + IKL,


(3)




I int
S = INa + INa(p) + IK,
IS→D = gS→D(VD − VS),
gS→D = 1/(r × areadend),
ID→S = gD→S(VS − VD),
gD→S = 1/(r × areasoma)
(8)
with r the resistance between compartments = 10 MΩ, areasoma = 10−6 cm2 the area
of the axosomatic compartment for both PY & IN cells, areadendPY = 165 × areasoma for
the area of the dendritic compartment for PY cells and areadendIN = 50 × areasoma for IN
cells.

(4)

(7)

(6)

(5)

Thalamic model — Thalamic relay cells (TC) and reticular neurons (RE) are both modeled
as a single compartment such that

Cm

dVD
dt

= −gL(V − EL) − I int − I syn,

(9)

These cells include the previously described INa, IK, IKL but also a low‐threshold Ca2+
current It and for TC a hyperpolarization‐activated cation current Ih.

I int
RE = INa + IK + It + IKL,
I int
TC = INa + IK + It + IKL + Ih

(10)

Synaptic currents — In this model, synaptic currents GABAA, AMPA and NMDA are described as

Isyn = gsyn[O]f (V )(V − Esyn)
(11)
where gsyn is the maximal synaptic conductance, Esyn the reversal potential (EAMPA and
ENMDA = 0 mV, EGABAA = ‐70 mV for synapses to PY/IN/RE, EGABAA = ‐83 mV for synapses
to TC and [O] the concentration of open channels. Dependence of postsynaptic voltage
for NMDA receptor was represented as f (V ) = 1/(1+exp(Vpost+25 mV)/12.5 mV)) (f (V ) =
1 for GABAA and AMPA).
The fraction of open channels ([O], in mM) is defined as

(12)

d[O]
= αx(1 − [O])[T ] − βx[O],
dt
[T ] = Aθ(t0 + tmax − t)θ(t − t0)
with θ as the Heavyside function, t0 the time of the last presynaptic spike, A = 0.5 the
amplitude of the neurotransmitter pulse of duration tmax = 0.3 ms. αx and βx are rate
constants; αx quantifies how the rate of production of open channels [O] depending on
the concentration of [T] and the saturation or availability of a binding site (1‐[O]), βx
quantifies the rate at which the fraction of open channels decays over time.
[T] is a pulse time‐dependent function that models neurotransmitter release.
GABAB is a metabotropic receptor, or G‐protein‐coupled receptor, which generates slow
and extended inhibitory signals through the activation of G proteins and second messengers [36]. Therefore, GABAB dynamics are very different than those previously described
for ionotropic receptors.

IGABAB = gGABAB ([G]4/([G]4 + K))(V − EK),

d[G]
dt

= K3[R] − K4[G],

d[R]
dt

= K1(1 − [R])[T ] − K2

(13)

[R] being the fraction of activated receptors (in mM), [G] the concentration of G‐proteins
(in mM), gGABAB = 0.04 µS and EK = ‐95 mV. Rate constants are defined as K1 = 0.52
mM−1ms−1, K2 = 0.0013 ms−1, K3 = 0.098 ms−1 and K = 100 µM4.




Miniature excitatory and inhibitory postsynaptic potentials — Theory states that, even in the
absence of nerve stimulation, there exists spontaneous release of neurotransmitter in
the synaptic cleft: miniature excitatory/inhibitory postsynaptic potentials (mEPSPs/mIPSPs) [37]. Mathematically speaking, the arrival time of those miniature postsynaptic
potentials can be modeled by a Poisson process with an remarkably small rate [38], so
that releases remain somewhat rare. In this model, the time‐dependent rate increases
over time elapsed from the last pre‐synaptic spike, and is defined as µ = log((t−t0 +
F )/F )/400 with F = 50 ms and where t0 is the time of the last pre‐synaptic spike and
the parameter F describes the time constant of the increasing rate.

Parameter randomization — In order to strictly reproduce the original model, we introduced
random variability in some parameters. Bazhenov and colleagues, in an earlier article
[39], mention some of the intrinsic parameters of the neurons in the network (gKL, gh
for TC cells and gKL for RE cells) were initialized with some random variability (variance
σ ~20% for gKL and σ ~10% for gh) to diminish the effect of lateral inhibition between
reticular neurons and to ensure robustness of the results. In [1], the parameters’ variability is mentioned briefly as ‘Some of the intrinsic parameters of the neurons in the
network were initialized with random variability (Gaussian distribution with ς = 5–10%)
to ensure the robustness of the result’. However, The modelDB code [5] gives us a more
precise definition of the variability, which is actually not restricted to thalamic cells but
also cortical ones and is not following a Gaussian distribution. The code introduces variability to several key parameters of the neurons in the network, namely gKL in RE and
TC cells, El in IN cells, gNa in both the axomatic and denditric compartments of IN cells
and gK in IN cells, by adding small random changes to them. The changes are based on a
random variable R, which is uniformly distributed between ‐1 and 1, thus not Gaussian.
Each parameter is updated by adding a scaled version of R to the existing value (0.001
for gKL in RE and TC cells, 0.5 for El in IN cells, 500 for gNa in the axomatic compartment
and 0.5 in the denditric compartment of IN cells and 50 for gK in IN cells). A constraint
is imposed on the sign of the variable R. More precisely, R is re‐sampled if it shares
the same sign as the two previous random values generated. This prevents correlated
changes between parameters, for instance ensuring close neurons do not get the same
variability. We implemented this exact parameters’ variability for our implementation
of the model, though it does not appear to have a critical influence on the results.

Geometry of the model — As per [1], the thalamocortical model is structured as four onedimensional layers containing N PY cells, N/4 IN cells, N/2 RE cells and N/2 TC cells
respectively. Unless otherwise specified, N was set to 100.

Cells connect to the ones that are spatially close to them (Figure 1). In our model, as
in [1], each cell type is organized in a 1D layer of similar width, each cell given an index
along this layer. Thus, given a neuron of index i in a population of source cells of size
Nsource and a neuron of index j in a population of target cells of size Ntarget, projections
of radius r can be defined according to a condition set on the indices such that

(cid:18)


i ·

Ntarget
Nsource

(cid:19)


(cid:12) ≤ r

− j

It is to be noted that, as our implementation does not include a mirror nor a periodic
boundary condition, the neurons at the edges of the layers do not receive as many synapses
as the neurons in the middle. Examples of the extent of the connection between the cells
is detailed in Table 1.




Table 1. Connectivity radii

Source

Target

Type of synapses

Connectivity radius Maximum synapses received/cell

Intracortical connections

PY
PY
PY
PY
IN

RE
RE
RE
TC

TC
TC

PY
PY

PY
IN
PY
IN
PY

TC
RE
TC
RE

PY
IN

TC
RE

AMPA
AMPA
NMDA
NMDA
GABAA

GABAA
GABAA
GABAB
AMPA

AMPA
AMPA

AMPA
AMPA


Intrathalamic connections


Thalamo‐cortical connections


Cortico‐thalamic connections


Figure 1. Example of connectivity between population varying in size. The green arrows show
the target neurons to which a source neuron in the middle of the source population can project.
A. Connectivity from a source population (TC) smaller than the Target Population (PY). B. Connectivity with source and target populations (PY) of equal sizes. C. Connectivity from a source
population (PY) bigger than target Population (TC).

### 4.2 Parameter choices that differ from the original paper

Table 2 presents the parameters and model features that were ill‐defined or absent from
the original paper, yet appeared in the code available on ModelDB [5].
While some elements of this table may not have a significant impact on the model per
se, it highlights a critical issue: the paper itself does not provide sufficient detail to accurately reproduce the model. Several parameters were either ill‐defined or absent, and
the equations were dispersed across various papers. Although the majority of equations
aligned with the papers cited in [1], it appears some have been specifically adapted for
this model, thus resulting in slight variations that could deeply influence the simulation results. We were able to resolve the vast majority of omissions and errors using the


Number of connections received for          30 = 22‘radius’ = 5cells connected = 10Radius = 5Radius = 5Radius = 10Number of connections received for          60 = 11Number of connections received for          55 = 11A.Source population (TC) smaller than Target Population (PY)B.Source and target populations (PY) of equal sizeC.Source population (PY) bigger than Target Population (TC)

code available on ModelDB [5], that we took as the ‘ground truth’. It is important to note,
however, that we would not have been able to reproduce the model and its results without this code. All the values in the ‘Value in the Present Model’ column of Table 2 are
directly derived from the ModelDB code. In that sense, the paper does not encourage
reproducibility, a crucial element in producing meaningful results.

Table 2. Inaccuracies, omissions and rounding

Parameter, equation

Value in the original manuscript

Value in the present model

Steady‐state value of m
for INa(p)


INa(p)

Q10 temperature
coefficient for IKCa, IKm,
IK, INa & IHVA


IKCa

Time constant of m and
h for IKm, IK, INa & IHVA

Ionic currents equations for cortical cells

1/(1 + exp(−(v + 42)/5)) [22]

0.02/(1 + exp(−(v + 42)/5))

0.2 ms [22]

2.95 [22]

34/([Ca] + 2) [22]

0.34/(a + b) [22]

0.8/(2.7(14/10)) (≈ 0.1991 ms)

2.3(13/10) (≈ 2.9529)

(1/2.3(13/10))(1/0.01[Ca] + 0.02)
(≈ 33.86/([Ca] + 2))

(1/(a + b))/2.3(13/10)
(≈ 0.3386/(a + b))

Ionic currents equations for thalamic cells


I T(TC)

0.22/(exp(−(v + 132)/16.7) +
exp((v + 16.8)/18.2)) + 0.13 [39]

(1/(exp(−(v + 131.6)/16.7) +
exp((v + 16.8)/18.2)) +
0.612)/3.5512/10

Time constant of h for
I T(TC)

8.2 + (56.6 + 0.27 exp((v +
115.2)/5))/(1 + exp((v + 86)/3.2))
[39]

(30.8 + (211.4 + exp((v +
115.2)/5))/(1 + exp((v +
86)/3.2)))/312/10


I h

5.3 + 267/(exp((v + 71.5)/14.2) +
exp(−(v + 89)/11.6)) [39]

20 + 1000/(exp((v + 71.5)/14.2) +
exp(−(v + 89)/11.6))

Ih constant rate k1

2.5 × 107 mM−4 · ms−1 [39]

0.0004 × ([Ca]i/0.0015)4 Hz

I h constant rate k3

0.1 ms−1 [39]

0.001×([P 1]/0.007) Hz


I T(RE)

1 + 0.33/(exp((v + 27)/10) +
exp(−(v + 102)/15)) [39]

(3 + 1/(exp((v + 27)/10) +
exp(−(v + 102)/15)))/5(12/10)

Time constant of h for
I T(RE)

22.7 + 0.27/(exp((v + 48)/4) +
exp(−(v + 407)/50)) [39]

(85 + 1/(exp((v + 48)/4) +
exp(−(v + 407)/50)))/3(12/10)

Rate and time constants
for INa(TC & RE) and
I K(TC & RE)

Absent from [39, 1]

see code for full equations

Time constant INa(p)

0.2 ms [22]

0.1991 ms

Calcium dynamics

Calcium constant A
(PY&IN)

2 × 10–4 mM · cm2/(ms · μA) [22]

5.1819 × 10−5 mM · cm2/(ms · μA)

Calcium constant A (TC)

5.18 × 10−5 mM · cm2/(ms · μA) [39]

5.1819 × 10−5 mM · cm2/(ms · μA)




Table 2. Inaccuracies, omissions and rounding (continued)

Parameter, equation

Value in the original manuscript

Value in the present model

Time constant calcium
dynamics (PY&IN)

Calcium equilibrium
concentration [Ca2+
0 ]

160 ms [22]

3 mM [40]

165 ms

2 mM

Ionic currents conductances and equilibrium potentials

Conductance gK(TC)

10 mS/cm2 [1]

12 mS/cm2

Conductance gKl(TC)

0−0.03 mS/cm2 for TC cells [1]

0.03 mS/cm2

Conductance gNa(p)(PY)

0.07 mS/cm2 for axosomatic
compartment [1]

15 mS/cm2

Conductance gKl

0−0.0025 mS/cm2 [1]

0 for IN, 0.0025 for PY

Conductance gNa(PY&IN
axosomatic)

1.5 mS/cm2 [1]

Conductance gNa(p)(PY
axosomatic)

Equilibrium potential
El(IN)

0.07 mS/cm2 [1]

−68 mV [1]

0.8 mS/cm2

3.5 mS/cm2

−70 mV

Random variability of
some parameters

gKl(TC), gKl(RE),gh(TC) concerned
[39]

gNa(IN, soma & dendrites), gKv(IN),
El(IN), gKl(TC), gl(RE) concerned

Miniature post‐synaptic potentials

MiniEPSPs PY‐PY
amplitude

MiniEPSPs PY‐IN
amplitude

MiniIPSPs IN‐PY
amplitude

MiniEPSPs & IPSPs
mean rate of arrival

≈ 0.75 mV [1]

≈ 0.75 mV [1]

≈ 0.75 mV [1]

0.06 μS

0.025 μS

gGABAAIN−PY /10

two possible values in the
manuscript [1] and no condition on
the arrival rate

µ = log((t−t0 + 50)/50)/400 if
t − t0 > 70 ms, else μ = 0

Synaptic conductances and equilibrium potentials

Synaptic conductance
gAMPA(PY‐PY)

Synaptic conductance
gAMPA(PY‐TC)

Equilibrium potential
EsynGABAA (TC)

0.08–0.15 μS

0.08–0.025 μS

−80 mV

Synaptic rates and resources

Fraction of resources
used per action potential
U for AMPA

0.07

0.15 μS

0.025 μS

−83 mV

0.073




Table 2. Inaccuracies, omissions and rounding (continued)

Parameter, equation

Value in the original manuscript

Value in the present model

Fraction of resources
used per action potential
U for NMDA

0.07


AMPA rate constants

α = 0.94 ms, β = 0.18 ms

α = 0.94 kHz, β = 0.18 kHz

GABAA rate constants

α = 10 ms, β = 0.25 ms

α(PY&IN) = 10 kHz, β(PY&IN)
= 0.25 kHz, α(TC&RE) = 10.5 kHz,
β(TC&RE) = 0.166 kHz

NMDA rate constants

Absent from [22] & [39]

α = 1 kHz, β = 0.0067 kHz

Addition of a constant in
the soma currents

Parameters at the cells and network levels

Absent from the article

6.74172 μA.cm

−2

Normalization of all
synaptic currents

Absent [1]

Division by number of incoming
synapses

Boundary connectivity
conditions

Absent from [1], multiple choices
in [5]: mirror, periodic, or none. As
the manuscript does not explicitly
mention it, we cannot confirm the
type of condition applied, we chose
to have no mirror or periodic
boundaries.

Synaptic depression
term

Appears to be concerning all
synapses [1]

Only for cortico‐cortical
connections AMPA and GABAA, not
present for other synapses

### 4.3 Computational specificities

The original model was coded with the C++ language and a GCC compiler, and equations
were integrated with a custom‐coded Runge‐Kutta 4 method and a simulation time step
of 0.02 ms. Additional information on the ModelDB repository of the file suggested the
‘‐O4’ and ‘‐ffast‐math’ optimization flags were used with the compiler [5]. The model was
run on a single computer.
Our replicated model was coded in Python using the open source Brian2 library [2] and
compiled with gcc. More precisely, Brian2 runs the simulation loop in Python but compiles and executes the modules in C++, which can increase the speed of simulations.
Requirements thus include a C++ compiler and Cython. Equations were integrated with
Brian2’s Runge‐Kutta 4 method and a simulation time step of 0.02ms. Brian2’s default
optimization flags ‘‐O3’ and ‘‐ffast‐math’ were used (since ‘‐O4’ is now deprecated). Individual simulations were run on a single computer. We verified that these simulations
could be conducted on two different computer models, with different operating systems (Linux and Windows), Brian2 versions (2.5 and 2.7), and Python versions (3.8.19
and 3.11.7), ensuring accurate replication across diverse hardware and software configurations, including the most recent ones at the date of submission.
Finally, while it is anticipated given the 20‐year technological advancements — specifically in processor speed — since the original model, our model runs significantly faster.
According to the ModelDB page, the original model requires approximately 7.5 hours to
simulate 25 seconds [5]. In contrast, our model does the same in less than 22 minutes,




despite recording more variables.

## 5 Results

### 5.1 Replication of individual cells’ and network’s general behavior

Single-cell and single-synapse dynamics —

Cortical cells — In order to confirm that the ionic channels’ equations and parameters
were recreating [1] behavior, we recorded parameters of interest using [1] C++ code
(membrane potentials or ionic current values for instance), plugged these values as input to our model, and checked the resulting behavior. For example, we recorded the
membrane potential of the pyramidal cell axosomatic compartment from [1] and used
it as input to our own axosomatic compartment equations. If both models are identical, the ionic currents should match exactly, as the same membrane potential over time
should produce identical dynamics. This systematic verification allowed us to reproduce most of the ionic and synaptic currents described in [1] and available on ModelDB
[5]. To the extent of our analysis however, some differences remain, due to the simulation methods used.
One of the most notable differences lies in the values of the sodium (Na) current in the
axosomatic compartment of pyramidal cells and cortical interneurons. Although the
equations to compute this current, and particularly the opening and closing variables
m and h, are the same, the resulting current in the replicated model is significantly
smaller, missing a peak in the current at the initiation of each spike (Figure 2).
Our best understanding of this discrepancy is that in the original model, the membrane
voltage equations for the axosomatic compartments of pyramidal cells and inhibitory interneurons are not in differential equation form and are always updated first. All other
variables are then updated immediately after, using the newly computed axosomatic
current. This introduces a one‐time‐step difference in the computation of the axosomatic membrane potential compared to most other variables. In most ionic currents,
this difference is hardly noticeable, but it is not the case for axosomatic sodium currents
which have very fast dynamics. Since we believe this timing discrepancy in the original
model was unintentional, we did not replicate it in our model, where all variables are
updated simultaneously. Regardless, we recognize that this could influence the overall
behavior of the full model. Additionally, this one‐time‐step difference in the computation of axosomatic membrane potentials also causes spikes originating from cortical
cells axosomatic compartment to trigger synaptic currents one time step earlier compared to other neuron types in the model (see for example the synaptic current from
cortical pyramidal cells to thalamic relay cells, Figure 3).
However, we do not believe this discrepancy makes a significant difference in the behavior of the full model.




(A)

(B)

Figure 2. Fast currents dynamics INa and IK in the axosomatic compartment of pyramidal cells
and cortical interneurons. A. Top panel shows one axosomatic interneuron membrane potential
v retrieved from simulation of the original C++ code. We used these values of v to compute INa
and IK across time and compare them with the original model ones. Should the equations and
their integration be the same, a perfect match between the two will be observed. This is the case
for IK but not INa. B. Zoom in on INa during on spike and the different variables used to compute
it (m, h, and (v − ENa)), as well as IK. The main discrepancy between the two model lies in a one
time‐step difference in the value used in (v − ENa).




(a) AMPA‐mediated synapse from PY to TC during
one cortical up‐state

(b) AMPA‐mediated synapse from PY to TC during
one PY spike

Figure 3. AMPA current dynamics from pyramidal to thalamic cells. A. Top two panels show the
axosomatic membrane potential v of one pyramidal cell and the membrane potential v of one
thalamic relay cell, retrieved from simulation of the original C++ code. Last panel shows a comparison of AMPA currents in the original versus our model, which looks like a match. B. Zoom in
on AMPA current, showing one timestep difference between the original model and ours.

Thalamic cells — We extended this analysis to the thalamic relay and reticular cells, identifying another minor inconsistency in the fast sodium Na+ and potassium K+ currents
(Figure 4A). While the rate constants governing the dynamics of the activation variable
m (αm, βm) and h (αh, βh), the steady‐state activation and inactivation variables (m∞,
h∞) and the time constants τh and τm were identical (Figure 4CD), the resulting activation and inactivation variables m and h were different between our model and the original C++ model (Figure 4B). According to us, that can only be explained by a difference in
the solver chosen. While we both used a basic form of the Runge‐Kutta method of order
4, practical differences might arise due to error handling, accuracy and optimization.
Lower level implementation in C++ may be faster and more memory efficient but also
very sensitive to issues like numerical stability. Python implementation within Brian2
is evidently more recent and has been well‐tested. Either way, both solvers are highly
suitable for the purpose at hand, and the we believe the slight difference observed does
not considerably impact the behavior of the model.




(a)

(b)

(c)

Figure 4. Currents dynamics in thalamic relay cells (TC). A. Top panel shows one TC cell membrane potential v retrieved from simulation of the original C++ code. We used these values of v
to compute the values of all currents across time (INa, IK, It, IKL, IL and Ih) and compare them
with the original model ones. Should the equations and their integration be the same, a perfect
match between the two will be observed. This is the case for all currents except INa. B. Left: Zoom
in on the opening and closing variables m and h of the sodium current INa, which do not match
between the two models. Right: the different variables used to compute them (αm, βm, τm, m∞,
αh, βh, τh, h∞), which are a perfect match.




Full network dynamics — The reproduced model displays dynamics qualitatively similar to
those described by [1]. Like the original model, it exhibits activity akin to that observed
during slow‐wave sleep. This activity is characterized first by slow oscillations in all the
pyramidal cells of the network, marked by the presence of periods of intense spiking
activity (‘up’ states) followed by periods of resting activity (‘down’ states) (top panel of
Figure 5).

Figure 5. Colormaps of membrane potentials showing cortical and thalamic relay cells’ activity.
The left panels represent our model, while the right panels correspond to the original Figure 6
from [1]. Both show 18‐second‐long simulation on top and a zoom on three seconds of the same
simulation on the bottom.

From our standpoint, we were concerned about the absence of a color bar in Figure 6
of [1] (right panel of Figure 5). However we eventually clarified the color map parameters by consulting a more recent paper building on the original model [32]. Using this
information, we plotted a colormap for membrane potentials thresholded between ‐75
mV and ‐60 mV. Nonetheless, our figure still differs because the original figure likely
used two different colorbars for pyramidal and thalamic cells, resulting in internal mismatches that naturally explain the differences with our figure which uses a consistent
colorbar across all plots. This claims is supported by the cellular activity shown in Figure 7. We would also like to precise that, while this information was not specified in the
original paper, further investigation of the code and data confirmed that it is the axosomatic compartment of PY and IN that is plotted, and not the dendritic compartment,
which exhibits different spike shapes and overall dynamics (Figure S2). Otherwise specified, following plots will show axosomatic compartments results.
That being said, our model’s up‐states appear shorter, resulting in more oscillations
during a typical 30‐second simulation. Moreover, in the original model, the initiation
of up‐states appears sharper and often originates from a single neuron, whereas in our
implementation, this mechanism is often less organized. Despite this, the frequency of
our slow oscillations, approximately 1 Hz in this instance, is consistent with the conventional definition of slow oscillations.
Following thorough investigation, we have yet to properly elucidate this inconsistency
in our model. Running the original C++ code from ModelDB yielded dynamics more
closely resembling those reported in the original study (Figure 6), suggesting that the
implementation differences partly underlie the observed discrepancy. We explored several parameter modifications in our Python reproduction to bridge this gap: (1) reducing




thalamo‐cortical synaptic conductances (gAMPATC−PY and gAMPATC−IN) (Figure S3C), (2) decreasing recurrent pyramidal‐to‐pyramidal connectivity (Figure S3D), and (3) lowering
the calcium‐activated potassium conductance (Figure S3E). These adjustments either
slowed the cortical oscillations by prolonging the down‐state or by extending the duration of the up‐state (Figure S3 for details). That being said, none of the changes fully
recapitulated the original oscillatory dynamics. As the original C++ code seems to better
capture the published dynamics, further investigations comparing it with the proposed
implementation may help clarify the underlying causes of the observed differences.
Additionally, our model does not produce the very long depolarized state in the beginning of a simulation as observed in the figure in ModelDB [5] (Figure 6), but it also seems
like this is not the case in the rest of the figures from the original paper either. Furthermore, as this sustained depolarized activity appears to be but a transitory state following
initialization, we did not try to replicate it in our model, and focused instead on steadystate behavior.

(a)

(b)

(c)

Figure 6. Colormaps of membrane potentials showing cortical cells’ activity for the first 25 seconds
of the simulation. A. Figure displayed on the ModelDB page. B. Result of a simulation using
the C++ code available on ModelDB on one of our computer. C. Result of a simulation with the
proposed reproduced model in Python.

These cortical slow oscillations can be more precisely observed when looking at single
cell activity (top panel of Figure 7). Additionally, we can observe from single thalamic
relay cell activity that the model reproduces the spindle‐like activity described in [1]
(bottom panel of Figure 7).
Replicating Figure 7 from the original paper (right panel of Figure 7) raised a few questions from our side. Indeed, spike shapes from the original paper appear to be more
irregular than in our replicated model, and have some variability in the maximum membrane potential reached. However, further investigation of the code provided on ModelDB revealed that this apparent discrepancy was only a matter of data recording and
plotting. Specifically, membrane potentials in the original paper were recorded and
plotted not for every simulation timestep (i.e. with a timestep of 0.02 ms), but rather at
intervals of 50 timesteps (hence data plotted every 1 ms). Recording and plotting data
of the original model at every timestep reveals significantly different activity from the
one presented in the paper, in accordance with our replicated model (Figure S1). We believe that this recording and plotting choice (which may have resulted from a constraint
on data storage) could also account for the discrepancy between the cellular activity presented in the top versus bottom panel of the original figure. However, it does not explain
the substantial disparity in spike amplitudes within pyramidal cells across these panels
(spike peak around +50 mV in the top panel and below 0 mV in the bottom one). We suspect this might be coming from a scaling issue for PY, IN and RE, a cropped membrane
voltage, or simply a forgotten appropriate scale bar.




Figure 7. Comparison of cellular activity of one cell for each type within the network. Left panels
show membrane potentials simulated by our replicated model, right panels are the original Figure
7 from [1]. Local field potential was not reproduced as the computation was not described in
the paper. The top part of the figure shows the results from 15 seconds out of a 30‐second long
simulation, while the bottom part of the figure shows a zoom in on 2.5 seconds.

From a reader’s standpoint, we advocate for more precision and details throughout the
paper’s figures. Throughout the paper, though the qualitative behavior of the model was
clear, imprecision or missing information (such as the missing scalebars above) sometimes left us uncertain about the precise results of simulations as well as the figure’s
generation details. In the same manner, the paper lacks information on the computation of local field potentials (Figure Figure 7).

### 5.2 Verification of original claims

The spontaneous behavior of cortical cells (claims 1-4) — Our implementation of the model
confirms that miniature EPSPs are the instigators of cortical slow oscillations (isolated
from thalamus), as the removal of these potentials eliminates cortical oscillations. Their
random summation and accumulation over one pyramidal cell is sufficient to depolarize it to a threshold that activates the persistent sodium current. This persistent sodium
current, in turn, triggers the fast sodium current, initiating a spike in the cell and subsequently inducing spikes in neighboring cells also depolarized by miniEPSPs.
During this ‘up’ state, the persistent sodium current activity maintains spiking activity
alongside PY to PY AMPA and NMDA mediated interconnections. When the persistent
sodium current is inactivated, only isolated spikes driven by the summation of miniEPSPs remain, and no oscillations can be observed.




Lastly, the transition to a down state is facilitated by the slow calcium‐dependent potassium current accumulation as well as inhibition from neighboring interneurons and
accumulation of synaptic depression in pyramidal cells. The oscillations are slowed
down, until extinction (Figure 8). Our tests show that removing AMPA synaptic depression alone is sufficient to induce continuous, unending pyramidal cell activity, while
removing the slow calcium‐dependent potassium is not.
We can also observe that pyramidal cells exhibit higher firing frequencies during the initial phase of the up state, followed by a gradual reduction in activity, which we believe
is due to the gradual accumulation of IKCa.
Thus claims 1‐4 are deemed confirmed.




Figure 8. Cortical up state mechanisms. A. Pyramidal cell membrane potential. Blue is the pyramidal cell triggering the up‐state and light blue represent the neighboring pyramidal cells, showing synchrony in the up‐states. B. Miniature excitatory and inhibitory post‐synaptic potentials.
Miniature excitatory post‐synaptic potentials accumulation eventually triggering the up‐state. C.
Sodium currents INa and INa(p). INa(p) current is accumulated by the miniature excitatory potentials until both INa & INa(p) spikes are triggered. D. Excitatory synaptic currents. AMPA and NMDA
mediated‐synapses maintaining up‐state activity. E. Calcium‐dependent potassium current IKCa
IKCa accumulation overtime slows down pyramidal cell spiking, eventually facilitating the transition to the down‐state. F. GABAA inhibition from interneurons to pyramidal cells. G. Synaptic
depression. The synaptic depression is a factor multiplying the AMPA current from PY to PY. Its
steady decrease here shows a strong accumulation of depression, resulting in a lower AMPA current from PY to PY.

The spontaneous behavior of cortical cells (claims 5-10) — Figure 4 in the original paper investigates the link between the production of slow waves in the isolated cortical model, the
number of cells and the characteristics of miniEPSPs. The relationship between the
amplitude of the miniEPSPs and number of slow oscillations in the isolated cortex is




preserved in our replication of the model, however the relationship between the number of neurons and the frequency of the slow oscillation does not seem to be the same
(Figure 9).
This is because in the model (by Bazhenov on ModelDB [5], see supplementary Figure S4,
and its replication by ourselves) the synaptic conductances (and miniEPSPs conductances) are scaled according to the number of synaptic targets, so reducing the number of neurons does not reduce the input effectively received by pyramidal cells. What
truly impacts the generation of the slow oscillation is the total input received by pyramidal cells and not the number of neurons: the EPSPs conductance parameter in the
model influences the number of slow oscillations, while scaling down the conductance
of synapses in the model reduces the duration of the up‐states (Figure 10).




(a) Cortical and thalamic subparts connected

(b) Cortical and thalamic subparts disconnected

Figure 9. Comparison of the effects of network size and miniature excitatory post‐synaptic potentials on cortical up‐state dynamics. Left panels of both A. and B. show behavior of our replicated
model, right panels are extracted from the original Figure 4 from [1]. A. Network size as defined by
the number of pyramidal cells. No significant difference can be observed across the conditions.
B. Miniature excitatory post‐synaptic potentials. The velocity of up‐state increases with APY−PY
in a network of N PY = 20.
Note: The scale bar in the original manuscript appears inconsistent with the oscillation frequencies described elsewhere in the original paper. Here, we assume a corrected time scale of 2.5
seconds instead of 25 seconds, in line with the dynamics presented in other figures of the original
manuscript. This was confirmed by running the code available on ModelDB with disconnected
cortex (Figure S4).




Figure 10. Dynamics of cortical up‐state based on cortical synapses conductance and miniEPSPs
conductance. Top panel: Synapse and mini conductances kept at their original values show regular alternation of up and down states at about 1.2 Hz. Middle panel: Reduction of the synaptic
conductance by 50% with normal miniEPSP conductance results in isolated cortical spikes instead
of up‐states, at about 1.2 Hz. Bottom panel: Reduction of the miniEPSPs conductance by 50% with
normal synaptic conductance results in up states but separated by longer down states (up states
appearing at about 0.13 Hz).

Just like in the original model, the function used to determine the probability of occurrence of miniEPSPs does not have a lot of influence on the slow oscillations (Figure 11).
Thus, claims 6 and 7 are deemed confirmed, while claim 5 is not.

Figure 11. Comparison of the effects of miniature excitatory post‐synaptic potential mean rate on
up‐state dynamics. Left panel show behavior of our replicated model, right panel is extracted
from the original Figure 4 from [1]. No significant difference was observed between the two conditions. Log‐based mean rate was defined as μlog = log((t−t0 + 50)/50)/400 ; exp‐based was defined
as μexp = (2/(1 + exp(−(t−t0)/400))−1)/100.
Note: The scale bar in the original manuscript appears inconsistent with the oscillation frequencies described elsewhere in the original paper. Here, we assume a corrected time scale of 2 seconds instead of 10 seconds, in line with the dynamics presented in other figures of the original
manuscript.

When it comes to the relationship between the conductance of synapses in the cortical
model (isolated from thalamus), the regularity of SWS oscillations and velocity of the
propagation of the up states, as reported in Figure 5 of the original paper, they are preserved in our replicated model, as shown in Figure (Figure 12). As the original paper did
not specify the exact method for calculating the velocity of the up states, we used the




following method:

• identify up states as spike trains with at least 30 ms lag between them

• determine the timing of the first spike for each neuron involved

• compute the propagation time by subtracting the timing of the first neuron to spike
in the up state to the last one, and compute the velocity by dividing the difference
of index between the first and last neuron to spike by the propagation time.

While computation following different steps may lead to different results, we believe the
general trend is conserved independent of the steps taken.
Thus, claims 8 and 9 are deemed confirmed.

(a) Membrane potential of pyramidal cells

(b) Mean propagation velocity of cortical up‐states

Figure 12. Spatiotemporal dynamics of cortical up‐states. Left panels of both A. and B. show behavior of our replicated model, right panels are extracted from the original Figure 5 from [1]. A.
Regularity of oscillations depends on PY to IN synapses. Increasing AMPA mediated synaptic
current from pyramidal cells to inhibitory interneurons better the spatial synchrony within the
cortical network. B. Velocity of up‐states propagation depends on PY to PY and PY to IN synapses.
Increasing AMPA mediated pyramidal cells to pyramidal cells synaptic conductivity increased the
velocity of the oscillations, while the opposite effect is produced when increasing AMPA mediated
synaptic current from pyramidal cells to inhibitory interneurons.

Lastly, as the original paper states, we confirmed that the thalamic network, composed
of RE and TC cells, is not necessary to maintain slow oscillations (Figure 13). Its presence solely changes the spatiotemporal pattern of activity so that the cortical up state
duration is increased. The thalamic system role will prove to be crucial in the electrical
stimulation subpart of this chapter.




(a) Cortical and thalamic subparts connected

(b) Cortical and thalamic subparts disconnected

Figure 13. Dynamics of cortical up‐states based on thalamic and cortical layer connectivity

Thus, claim 10 was confirmed.

The spontaneous behavior of thalamic cells (claims 11-12) — Spiking in pyramidal cells during
up‐states leads to bursting in reticular cells. In turn, reticular cells hyperpolarize thalamic relay cells, leading to de‐inactivation of the low‐threshold calcium current It and
a rebound low‐threshold spike (Figure 14). The thalamic relay cells do not, or in very
few instances, fire INa spikes, but instead fire It spikes. Without the latter, the thalamic
relay cells simply never spike. We could not frequently observe the few sub‐threshold
cycles described in [1] and that are characteristic of thalamic spindles. Lastly, powerful
AMPA mediated PY to RE synapses lead to depolarization or spiking in reticular cells,
eventually inactivating It and ending thalamic relay cell activity. Powerful PY‐RE AMPA
synapses lead to depolarization of RE, inactivation of low‐threshold calcium current and
eventually termination of rebound oscillations.




Figure 14. Spontaneous behavior of thalamic relay and reticular cells during a cortical up‐state. A.
Pyramidal cell membrane potential during an up‐state. B. Thalamic relay cell membrane potential. C. It current in thalamic relay cells. D. AMPA mediated‐synapses current from PY to RE.

Thus, claim 11 was partially confirmed while claim 12 was confirmed.

The transition to awake state (claims 13-14) — Figure 8 in the original article describes the
transition from slow oscillations (associated with slow‐wave sleep) to persistent cortical
firing (associated with wakefulness), arising from the suppression of leak potassium
current in pyramidal cells and thalamo‐cortical cells and some synaptic conductances.
Most aspects of this transition are captured by our replicated model, including the increased firing rate of pyramidal cells and the absence of down states (Figure 15). However, for the strong PY‐PY configuration (Figure 15), we observe sustained firing of reticular cells for a few seconds at the beginning of the simulation which then ceases totally.
This phenomenon remained unexplained and may also be present in the original work
of [1], although we did not confirm this.
Increased pyramidal cell to pyramidal cell synaptic conductance does increase the firing
rate of pyramidal cell in our replicated model, but this firing rate does not reach the
30‐40 Hz range reported in the original paper with the conductance values studied in
Figure 15‐D.
Finally, without any clear indication on how the ‘input resistance of PY neurons’ was
computed in the original paper, we did not study this aspect of cell activity in our work.




(a)

(c)

(b)

(d)

Figure 15. Dynamics of cellular activity of pyramidal, reticular and thalamic relay cells based on PYPY and RE‐TC‐RE conductances, with abolished potassium leak currents in PY and RE cells. For
each panel, the left plots show results from our replicated model and the right plots show extracts
of Figure 8 from the original paper. A. Strong PY‐PY condition: gPY−PY = 0.15 μS, gRE−TC = 0.2 μS,
gTC−RE = 0.4 μS. B. Weak PY‐PY condition: gPY−PY = 0.09 μS, gRE−TC = 0.2 μS, gTC−RE = 0.4 μS.
C. Weak PY‐PY and RE‐TC‐RE condition: gPY−PY = 0.09 μS, gRE−TC = 0.1 μS, gTC−RE = 0.2 μS. D.
Evolution of pyramidal cell mean firing frequency as a function of the conductance of PY to PY
AMPA synapses.

We were unable to replicate a transition to awake state as visually distinct as the one
presented in [1] using our model (Figure 16). Note that in the absence of indication of
the precise values used to obtain the intermediate states between slow‐wave sleep and
activated states, we varied all parameters linearly. Nonetheless, the changes observed in
the frequency domain during transition to activated state, are very similar across both
models. Notably, there is a significant reduction in power in the 0‐2 Hz frequency band,
which encompasses the cortical slow oscillations, indicating a substantial reduction in
these oscillations, nearly to the point of their disappearance. At higher frequencies, we
do observe a pronounced increase in power in the 10‐20 Hz range, coupled with a slight
decrease in the higher frequencies bands, indicating a general slowing of the firing rates
of cortical cells during activated states compared with up‐state during slow wave sleep
Figure 16‐B. Using the ‘Weak PY‐PY’ configuration as in Figure 15‐B as a proxy for the
activated state yields results closer to those reported in [1], as shown in supplementary
Figure S5.




(a) Cellular activity of pyramidal cells across conditions

(b) Integrated power across conditions

Figure 16. Transition from SWS oscillation to activated state. For each panel, the left plots show
results from our replicated model and the right plots show extracts of Figure 9 from the original
paper. A. Decrease of the conductance of IKL and IAMPAPY−PY reduced the presence of cortical
down‐states. SWS state: gPY−PY = 0.15 μS, gRE−TC = 0.2 μS, gTC−RE = 0.4 μS, gKL = 0.3 μS;
Activated state: gPY−PY = 0.09 μS, gRE−TC = 0.1 μS, gTC−RE = 0.2 μS, gKL = 0 μS B. Integrated
power across various frequency bands during the transition to the activated state. For each panel,
the left plots show results from our replicated model and the right plots show figures from the
original paper.

Thus, claim 13 was deemed partially confirmed. Claim 14 could not be investigated due
to the the lack of clear indication on how to compute the input resistance of cortical
neurons.

The response to electrical stimulation (claim 15) — Prethalamic electrical stimulation was applied as per [1], with 25% of thalamic relay cells in the center part of the cell layer stimulated by external AMPA synapses driven by Poisson‐distributed spike trains with mean
rate of arrival μ = 25 Hz, modulated by a sinusoidal function at 0.4, 1 or 2.5 Hz. Without
indications from the paper or code, we chose a conductance of 0.4 μS for these input




synapses, i.e. the same conductance as AMPA TC to RE synapses. Reproducing running
spike histograms (RSHs) allowed us to investigate in our model if the thalamus partially
blocked sensory input to the cerebral cortex during slow wave sleep as in [1].

Figure 17. Running spike histograms showing the response of the excitatory cells to the stimulation. For each panel, the left plots show results from our replicated model and the right plots
show Figure 10 from the original paper. A. Stimulation during activated state. Sensory input is
well transmitted in the awake state, as TC and PY cells spike histograms closely follow the stimulation. B. Stimulation during slow wave sleep activity. Sensory input is partially blocked due the
strong endogenous cortical oscillations. PY cells spike histograms do not follow the stimulation
for slower stimulation frequencies. For each panel, the left plots show results from our replicated
model and the right plots show figures from the original paper.




Figure 18. Accuracy of the response of pyramidal cells to thalamic stimulation. For each panel,
the left plots show results from our replicated model and the right plots show extracts of Figure
11 from the original paper. A. Stimulation during activated state. For both models, peaks in the
power spectra corresponding to the frequency of stimulation were observed for all simulation
conditions. B. Stimulation during slow wave sleep activity. For both models, peaks in the power
spectra corresponding to the frequency of stimulation were observed only for the 2.5 Hz condition.
For each panel, the left plots show results from our replicated model and the right plots show
figures from the original paper.

In the activated state, the electrical stimulus was clearly observable at the cortical level,
regardless of the stimulation condition, as shown on Figure 17. Cross‐correlations between the running spike histogram of the input and responses of pyramidal cells also
support these findings (Figure 18). Additionally, the power spectra of the electrical input
and the excitatory cells of the network were consistent, showing a peak at the envelope
frequency of the stimulation (Figure 18).
Conversely, during slow‐wave sleep, the cortical activity did not align with the electrical stimulation, due to significant interference from strong cortical up and down states
activity, especially in the lower frequency stimulation paradigm (Figure 17). At higher
frequencies, transmission of input to the cortical layer was apparent, although less efficient than in the awake condition (Figure 18). Thus, our model accurately replicates the
reduced ability of the thalamo‐cortical network to transmit electrical input to the cortical layer during slow‐wave sleep compared to awake state, as cortical slow‐wave sleep oscillations effectively mask low‐frequency stimulation. Furthermore, during slow‐wave
sleep, the efficacy of the transfer of higher frequency stimulation is influenced by the
distance between the cortical cell of interest and the stimulation (Figure 19).
Therefore, despite differences in our activated state compared to the original model [1],
our implementation of the model successfully replicates the effects of electrical stimulation in the thalamo‐cortical system.
Claim 15 was deemed confirmed.




Figure 19. Pyramidal cell’s activity at varying distances from the stimulation site. The left panel
show results from our replicated model and the right shows Figure 12 from the original paper.
PY cells membrane potentials show that persistent slow wave activity is present away from the
stimulation site (PY cell number 0 is displayed). Slow waves are perturbed in neurons closer to
the stimulation site (PY cell number 50 is displayed).

## 6 Discussion

We believe that [1] work is of great interest for the community, as can be assessed by its
numerous citations, and the multiple computational models that were based on it in the
author’s team in the subsequent years. This motivated us to try to replicate this model
in a more accessible programming language (Python) and modern neural simulation
library (Brian2).
As can be expected from a work published in 2002, reproducibility by an external research team was probably not a priority for the writers at that time. However, we salute
their effort to publicly share their code online on the ModelDB platform in 2018, which
made it possible to reproduce their model and verify most of their claims, despite missing information or typos in the original paper’s ‘Methods’ section and figures. We regret
however that some of the more recent works based on this model (like [32]) do not have
their code available online and would therefore be very hard to replicate as of today.
One of the main concern that arises from our side involves the discrepancy in sodium
channel ionic currents in cortical cells between the original model and our replication,
due to what we think is an incorrect integration and update of some of the original
model’s internal variables. This discrepancy has a direct impact on cortical cells spiking activity and could therefore also have a large impact on the model’s global behavior,
such as the frequency of slow oscillations and the transition to the awake state. These
differences may appear as minor, as we were still able to verify the model’s qualitative
behavior. However, since this work is at the basis of multiple other models in the authors’ research team, we cannot rule out the possibility that some of their more recent
results could also be impacted by this issue.




## 7 Appendix

(a) Plotted every dt (50 000Hz)

(b) Plotted every 50 dt (1 000Hz)

Figure S1. Thalamo‐cortical network cellular activity sampled at different rates.

Figure S2. Compartment activity of cortical cells. Membrane potentials in pyramidal and interneurons axosomatic and dendritic compartments are shown during a 10‐second‐long simulation.




(a)

(c)

(b)

(d)

(e)

Figure S3. Testing parameter adjustments to better match cortical oscillations observed in the original paper [1]. A. Simulation using the C++ code available on ModelDB on one of our computers.
B. Simulation with the proposed reproduced model in Python. C. Simulation with the proposed
reproduced model in Python with only 10% of the original synaptic conductance between the thalamus and the cortical layer (gAMPATC−PY = 0.01 μS and gAMPATC−IN = 0.01 μS) D. Simulation with
the proposed reproduced model in Python, with APY−PY = 0.048 μS instead of APY−PY = 0.06 μS.
−2 instead
E. Simulation with the proposed reproduced model in Python, with gKCa = 0.06 mS · cm
of gKCa = 0.3mS · cm

−2

.




(a) Spatiotemporal dynamics of cortical up‐states.

(b) Cellular activity of one pyramidal cell
within the network.

Figure S4. Cortical network activity, disconnected from the thalamic network, obtained by running
the original C++ code available on ModelDB [4, 5]. In order to run the simulation, we modified the
file input27, setting the simulation duration to 20 seconds and setting the conductances between
the thalamus and the cortex to 0 in both directions. We then varied the variables Mcx and Min
to run the model with different numbers of pyramidal and inhibitory : 20 PY–5 IN cells, 60 PY–
15 IN cells and 100 PY–25 IN cells. From these results, we cannot conclude, as per the original
publication stated, that a network size increase lead to higher frequency of spontaneous bursting
and increased its regularity.




(a)

(b)

Figure S5. Transition from the SWS to the activated state, with the activated state corresponding
to the parameters from the Weak PY‐PY panel (B) from (Figure 15). For each panel, the left plots
show results from our replicated model and the right plots show extracts of Figure 9 from the
original paper.

References

1. M. Bazhenov, I. Timofeev, M. Steriade, and T. J. Sejnowski. “Model of thalamocortical slow-wave sleep oscilla-
tions and transitions to activated States.” In: The Journal of Neuroscience 22 (19 Oct. 2002), pp. 8691–8704.
DOI: 10.1523/JNEUROSCI.22-19-08691.2002.

2. M. Stimberg, R. Brette, and D. F. Goodman. “Brian 2, an intuitive and efficient neural simulator.” In: eLife 8 (Aug.

2019). DOI: 10.7554/elife.47314. URL: http://dx.doi.org/10.7554/eLife.47314.

3. M. Reynes. [Re], Reynes & Aussel [Dataset]. Data set available at: https://doi.org/10.5281/zenodo.13376370.

2024. DOI: 10.5281/zenodo.13376369. URL: https://doi.org/10.5281/zenodo.13376370.




4.

R. A. McDougal, T. M. Morse, T. Carnevale, L. Marenco, R. Wang, M. Migliore, P. L. Miller, G. M. Shepherd, and M. L.
Hines. “Twenty years of ModelDB and beyond: building essential modeling tools for the future of neuroscience.”
In: Journal of Computational Neuroscience 42.1 (2017), pp. 1–10. DOI: 10.1007/s10827-016-0630-z.

6.

5. M. Bazhenov, I. Timofeev, M. Steriade, and T. J. Sejnowski. Model of thalamocortical slow-wave sleep os-
cillations and transitions to activated states. https://modeldb.science/28189?tab=1. ModelDB accession
number: 28189; Simulation Environment: C++ program; Implementer: Maxim Bazhenov (Bazhenov@Salk.edu).
2002. URL: https://pubmed.ncbi.nlm.nih.gov/11826256/.
A. Kales, A. Rechtschaffen, L. A. B. I. S. University of California, and N. N. I. N. (U.S.) A Manual of Standardized
Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects: Allan Rechtschaffen
and Anthony Kales, Editors. NIH publication. U. S. National Institute of Neurological Diseases and Blindness,
Neurological Information Network, 1968. URL: https://books.google.fr/books?id=Z41IvQEACAAJ.
C. Iber, S. Ancoli-Israel, A. Chesson, and S. Quan. “The AASM Manual for the Scoring of Sleep and Associated
Events: Rules, Terminology and Technical Specifications.” In: Westchester, IL: American Academy of Sleep
Medicine (Jan. 2007).
S. Diekelmann and J. Born. “The memory function of sleep.” In: Nature Reviews Neuroscience 11.2 (Jan. 2010),
pp. 114–126. DOI: 10.1038/nrn2762. URL: http://dx.doi.org/10.1038/nrn2762.

8.

7.

10.

11.

9. W. Plihal and J. Born. “Effects of Early and Late Nocturnal Sleep on Declarative and Procedural Memory.” In:
Journal of Cognitive Neuroscience 9.4 (July 1997), pp. 534–547. DOI: 10.1162/jocn.1997.9.4.534. URL: http:
//dx.doi.org/10.1162/jocn.1997.9.4.534.
P. Maquet. “The Role of Sleep in Learning and Memory.” In: Science 294.5544 (Nov. 2001), pp. 1048–1052. DOI:
10.1126/science.1062856. URL: http://dx.doi.org/10.1126/science.1062856.
S. Diekelmann, I. Wilhelm, and J. Born. “The whats and whens of sleep-dependent memory consolidation.” In:
Sleep Medicine Reviews 13.5 (Oct. 2009), pp. 309–321. DOI: 10.1016/j.smrv.2008.08.002. URL: http://dx.doi.
org/10.1016/j.smrv.2008.08.002.
R. Huber, M. Felice Ghilardi, M. Massimini, and G. Tononi. “Local sleep and learning.” In: Nature 430.6995 (June
2004), pp. 78–81. DOI: 10.1038/nature02663. URL: http://dx.doi.org/10.1038/nature02663.

12.

14.

13. H. Johannes, P. Hannah, F. Bernd, S. Kai, B. Chiara, R. Dieter, and N. Christoph. “Spindles and Slow Waves in
Humans: EEG sigma and slow-wave activity during NREM sleep correlate with overnight declarative and pro-
cedural memory consolidation.” In: Journal of Sleep Research 21.5 (2012), pp. 612–619. DOI: 10.1111/j.1365-
2869.2012.01017.x. URL: https://doi.org/10.1111/j.1365-2869.2012.01017.x.
D. Menicucci, A. Piarulli, M. Laurino, A. Zaccaro, J. Agrimi, and A. Gemignani. “Sleep slow oscillations favour
local cortical plasticity underlying the consolidation of reinforced procedural learning in human sleep.” In: Jour-
nal of Sleep Research 29.5 (June 2020). DOI: 10.1111/jsr.13117. URL: http://dx.doi.org/10.1111/jsr.13117.
A. Giuditta, M. V. Ambrosini, P. Montagnese, P. Mandile, M. Cotugno, G. G. Zucconi, and S. Vescia. “The sequen-
tial hypothesis of the function of sleep.” In: Behavioural Brain Research 69.1–2 (July 1995), pp. 157–166. DOI:
10.1016/0166-4328(95)00012-i. URL: http://dx.doi.org/10.1016/0166-4328(95)00012-i.

15.

16. G. E. Mueller and A. Pilzecker. “Experimentelle beiträge zur lehre vom gedächtniss.” In: Zeitschrift fuer Psy-

chologie 1 (1900).

18.

17. H. A. Lechner, L. R. Squire, and J. H. Byrne. “100 Years of Consolidation— Remembering Müller and Pilzecker.”
In: Learning & Memory 6.2 (Mar. 1999), pp. 77–87. DOI: 10.1101/lm.6.2.77. URL: http://dx.doi.org/10.1101/
lm.6.2.77.
R. Stickgold. “Sleep-dependent memory consolidation.” In: Nature 437 (7063 Oct. 2005), pp. 1272–8. DOI:
10.1038/nature04286.
L. R. Squire, L. Genzel, J. T. Wixted, and R. G. Morris. “Memory Consolidation.” In: Cold Spring Harbor Perspec-
tives in Biology 7.8 (Aug. 2015), a021766. DOI: 10.1101/cshperspect.a021766. URL: http://dx.doi.org/10.
1101/cshperspect.a021766.

19.

21.

20. M. Steriade, A. Nunez, and F. Amzica. “A novel slow (<1 Hz) oscillation of neocortical neurons in vivo: depo-
larizing and hyperpolarizing components.” In: The Journal of Neuroscience 13.8 (Aug. 1993), pp. 3252–3265.
DOI: 10.1523/jneurosci.13-08-03252.1993. URL: http://dx.doi.org/10.1523/JNEUROSCI.13-08-03252.1993.
E. Werth, P. Achermann, and A. A. Borbély. “Brain topography of the human sleep EEG: antero-posterior shifts
of spectral power.” In: NeuroReport 8.1 (Dec. 1996), pp. 123–127. DOI: 10.1097/00001756-199612200-00025.
URL: http://dx.doi.org/10.1097/00001756-199612200-00025.
I. Timofeev. “Origin of Slow Cortical Oscillations in Deafferented Cortical Slabs.” In: Cerebral Cortex 10.12 (Dec.
2000), pp. 1185–1199. DOI: 10.1093/cercor/10.12.1185. URL: http://dx.doi.org/10.1093/cercor/10.12.1185.
D. Contreras and M. Steriade. “Cellular basis of EEG slow rhythms: a study of dynamic corticothalamic re-
lationships.” In: The Journal of Neuroscience 15.1 (Jan. 1995), pp. 604–622. DOI: 10.1523/jneurosci.15-01-
00604.1995. URL: http://dx.doi.org/10.1523/jneurosci.15-01-00604.1995.

23.

22.




25.

24. M. Mölle, L. Marshall, S. Gais, and J. Born. “Grouping of Spindle Activity during Slow Oscillations in Human
Non-Rapid Eye Movement Sleep.” In: The Journal of Neuroscience 22.24 (Dec. 2002), pp. 10941–10947. DOI:
10.1523/jneurosci.22-24-10941.2002. URL: http://dx.doi.org/10.1523/JNEUROSCI.22-24-10941.2002.
Z. Clemens, M. Molle, L. Eross, P. Barsi, P. Halasz, and J. Born. “Temporal coupling of parahippocampal
ripples, sleep spindles and slow oscillations in humans.” In: Brain 130.11 (Apr. 2007), pp. 2868–2878. DOI:
10.1093/brain/awm146. URL: http://dx.doi.org/10.1093/brain/awm146.
A. Sirota, J. Csicsvari, D. Buhl, and G. Buzsáki. “Communication between neocortex and hippocampus during
sleep in rodents.” In: Proceedings of the National Academy of Sciences 100.4 (Feb. 2003), pp. 2065–2069.
DOI: 10.1073/pnas.0437938100. URL: http://dx.doi.org/10.1073/pnas.0437938100.
A. Sirota and G. Buzsáki. “Interaction between neocortical and hippocampal networks via slow oscillations.”
In: Thalamus and Related Systems 3.04 (Dec. 2005), p. 245. DOI: 10.1017/s1472928807000258. URL: http:
//dx.doi.org/10.1017/S1472928807000258.

27.

26.

28. M. Navarrete, M. Valderrama, and P. A. Lewis. “The role of slow-wave sleep rhythms in the cortical-hippocampal
loop for memory consolidation.” In: Current Opinion in Behavioral Sciences 32 (Apr. 2020), pp. 102–110. DOI:
10.1016/j.cobeha.2020.02.006. URL: http://dx.doi.org/10.1016/j.cobeha.2020.02.006.
P. Sanda, P. Malerba, X. Jiang, G. P. Krishnan, J. Gonzalez-Martinez, E. Halgren, and M. Bazhenov. “Bidirectional
Interaction of Hippocampal Ripples and Cortical Slow Waves Leads to Coordinated Spiking Activity During
NREM Sleep.” In: Cerebral Cortex 31.1 (Sept. 2020), pp. 324–340. DOI: 10.1093/cercor/bhaa228. URL: http :
//dx.doi.org/10.1093/cercor/bhaa228.

29.

30. M. Bonjean, T. Baker, M. Bazhenov, S. Cash, E. Halgren, and T. Sejnowski. “Interactions between Core and Ma-
trix Thalamocortical Projections in Human Sleep Spindle Synchronization.” In: The Journal of Neuroscience
32.15 (Apr. 2012), pp. 5250–5263. DOI: 10.1523/jneurosci.6141-11.2012. URL: http://dx.doi.org/10.1523/
JNEUROSCI.6141-11.2012.

31. M. Lemieux, J.-Y. Chen, P. Lonjers, M. Bazhenov, and I. Timofeev. “The Impact of Cortical Deafferentation on
the Neocortical Slow Oscillation.” In: The Journal of Neuroscience 34.16 (Apr. 2014), pp. 5689–5703. DOI:
10.1523/jneurosci.1156-13.2014. URL: http://dx.doi.org/10.1523/JNEUROSCI.1156-13.2014.
Y. Wei, G. P. Krishnan, and M. Bazhenov. “Synaptic Mechanisms of Memory Consolidation during Sleep Slow
Oscillations.” In: The Journal of Neuroscience 36.15 (Apr. 2016), pp. 4231–4247. DOI: 10.1523/jneurosci.3648-
15.2016. URL: http://dx.doi.org/10.1523/JNEUROSCI.3648-15.2016.

32.

34.

35.

33. G. P. Krishnan, S. Chauvette, I. Shamie, S. Soltani, I. Timofeev, S. S. Cash, E. Halgren, and M. Bazhenov. “Cel-
lular and neurochemical basis of sleep stages in the thalamocortical network.” In: eLife 5 (Nov. 2016). DOI:
10.7554/elife.18607. URL: http://dx.doi.org/10.7554/eLife.18607.
Y. Wei, G. P. Krishnan, M. Komarov, and M. Bazhenov. “Differential roles of sleep spindles and sleep slow
oscillations in memory consolidation.” In: PLOS Computational Biology 14.7 (July 2018), e1006322. DOI:
10.1371/journal.pcbi.1006322. URL: https://doi.org/10.1371/journal.pcbi.1006322.
A. L. Hodgkin and A. F. Huxley. “A quantitative description of membrane current and its application to conduc-
tion and excitation in nerve.” In: The Journal of Physiology 117.4 (Aug. 1952), pp. 500–544. DOI: 10.1113/j-
physiol.1952.sp004764. URL: http://dx.doi.org/10.1113/jphysiol.1952.sp004764.
B. Bettler, K. Kaupmann, J. Mosbacher, and M. Gassmann. “Molecular structure and physiological functions
of GABA(B) receptors.” In: Physiol. Rev. 84 (2004).
P. Fatt and B. Katz. “Spontaneous subthreshold activity at motor nerve endings.” In: The Journal of Physiology
117.1 (May 1952), pp. 109–128. DOI: 10.1113/jphysiol.1952.sp004735. URL: http : / / dx . doi . org / 10 . 1113 /
jphysiol.1952.sp004735.
C. F. Stevens. “Quantal Release of Neurotransmitter and Long-Term Potentiation.” In: Cell 72.10 Suppl. (Jan.
1993), pp. 55–63. DOI: 10.1016/S0092-8674(05)80028-5.

36.

38.

37.

39. M. Bazhenov, I. Timofeev, M. Steriade, and T. J. Sejnowski. “Cellular and Network Models for Intrathalamic
Augmenting Responses During 10-Hz Stimulation.” In: Journal of Neurophysiology 79.5 (May 1998), pp. 2730–
2748. DOI: 10.1152/jn.1998.79.5.2730. URL: http://dx.doi.org/10.1152/jn.1998.79.5.2730.
J. R. Huguenard and D. A. McCormick. “Simulation of the currents involved in rhythmic oscillations
In: Journal of Neurophysiology 68.4 (Oct. 1992), pp. 1373–1383. DOI:
in thalamic relay neurons.”
10.1152/jn.1992.68.4.1373. URL: http://dx.doi.org/10.1152/jn.1992.68.4.1373.

40.

---
**Source PDF:** `8b305b8c47e0.pdf` (2025_01_article.pdf)  
**URL:** https://zenodo.org/record/16529268/files/article.pdf
