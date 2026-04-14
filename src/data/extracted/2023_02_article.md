R E S C I E N C E C

Replication / Computational Neuroscience
[Re] Inter-areal Balanced Amplification Enhances Signal
Propagation in a Large-Scale Circuit Model of the
Primate Cortex

Vinicius Lima1,2, ID , Renan O. Shimoura3,2, ID , Nilton L. Kamiji3, ID , Demian Battaglia1,4, ID , and Antonio C.
Roque1,4, ID
1Aix-Marseille University, Institute for Systems Neuroscience (INS UMR 1106, Inserm), Marseille, France – 2These authors
contributed equally to this work, Gif sur Yvette, France – 3Department of Physics, School of Philosophy, Sciences and Letters of
Ribeirão Preto (FFCLRP), University of São Paulo„ Ribeirao Preto, Brazil – 4University of Strasbourg Institute for Advanced
Studies (USIAS), Strasbourg, France

Edited by
Benoit Girard ID

Reviewed by
Marcel Stimberg ID
Stephan Grein ID

Received
05 May 2023

Published
04 December 2023

DOI
10.5281/zenodo.10257800

## 1 Introduction

Information processing in the cortex relies on stable and, at the same time, reconfigurable signal propagation among its areas, i.e.: first, the signal is neither attenuated
nor amplified as it propagates across the cortical hierarchy of areas; second, the extent
to which signal propagate through hierarchically connected regions must be regulated
by context. Despite numerous studies done on inter‐area signal propagation in the mammalian cortex [1, 2, 3], the underlying mechanisms that could allow a simultaneously
reliable and flexible signal transmission are not yet completely understood. In computational neuroscience, many models address this question, however most of them make
unrealistic assumptions such as perfect identity of all areas, homogeneity of connection
weights across all stages of the hierarchy, and strictly feedforward network architecture,
even though cortical networks are rich in recurrent connections and feedback loops [4].
Here we replicate a recent modelling study by Joglekar et. al., [5]. In this work, the authors address the problem of reliable and flexible signal propagation in a large‐scale network model embedding a realistic multi‐regional connectome. The network structure of
the model is prescribed by an empiricaly‐determined directed and weighted inter‐areal
connectivity matrix for the macaque cortex, containing 29 areas distributed across the
occipital, temporal, parietal, and frontal lobes [4]. Furthermore, regions have heterogeneous time constants, due to a phenomenological reproduction of varying number of
excitatory spines across the cortical hierarchy [6]. The dynamics of network nodes are
described initially in terms of a population‐level mean‐field rate model [7, 8]. In a second
part of the article, a spiking network model of leaky integrate‐and‐fire neurons is used as
well to study synchrony modulations within each region. One of the key contributions
of Joglekar et. al. [5] study is to reveal the important role of a mechanism named global
balanced amplification (GBA). Briefly, this mechanism consists of increasing inter‐areal
excitation to facilitate signal propagation to different areas, combined simultaneously
with an increase of local inhibition to assure network stability. Modulating GBA provides thus a way to enable stable signal propagation or to disable it, thus conditionally
switching on or off the access to regions distant from the site of input injection.


The authors have declared that no competing interests exists.
Code is available at https://github.com/ViniciusLima94/ReScience-Joglekar/tree/master/code..
Data is available at https://github.com/ViniciusLima94/ReScience-Joglekar/tree/master/code/interareal.
Open peer review is available at https://github.com/ReScience/submissions/issues/72.


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

As mentioned in the Methods section of Joglekar et. al. [5], the original large‐scale spiking neuron network was implemented in the Brian 2 simulator [9]. Here, we provide an
original implementation of both the rate based, and the spike based model in the NEST
simulator [10, 11], which allows parallel execution of the network simulation, making
the code particularly easy to run in super‐computers. In addition, our implementation
of the model also provides an optimized open code for any researcher willing to use or
adapt the model for other scientific projects.
The selection of results we have chosen to reproduce provides a rich overview of the
main contents of the original paper. We obtained qualitatively similar results and we
checked under what conditions their robustness and validity were kept.

Availability of code implementations for the original model

In the original publication, the authors do not link any associated code repository with
their implementation of the models described. However, we found a repository with
Matlab and Python (Brian 2) scripts in the following address: github.com/xjwanglab/Jogle
karEtAl2018_Neuron. Despite the fact that those scripts helped to detect discrepancies and
non‐specified parameters in the original article, for the spiking model, not all parameters could be directly “plugged‐in” into Nest without conversion, and some adjustment
was often required in order to obtain the firing rate regimes specified in the original
paper, as we elaborated throughout this replication paper.

## 2 Methods

In this section we describe the models used in the original implementations [5]. We
start by briefly presenting the data used to construct the network connectivity, and to
estimate the synaptic weights among different cortical regions [4]. Next, we describe
the rate based model, and lastly the spiking neuron model. For the last two, we make a
bottom‐up description, i.e., starting from single population/neuron dynamics, the local
network structure, to the large‐scale network structure for each model. In this section
we focus on the general description of each model, specific parameters will be given in
the Results section, since they change depending on the specific replicated result.

### 2.1 Network connectivity data

To determine the inter‐regional connectome and the number of projections originating
from each cortical area, the original model uses high‐quality retrograde tracing data
by Markov et. al., [4], encompassing 29 areas from the macaque cerebral cortex. Restricted to these 29 areas, the connectome is edge‐complete, i.e. there are no missing
inter‐regional connections that have not been characterized [12]. The directed weight
from a source to a target area is estimated to be proportional to the Fraction of Labeled
Neurons (FLN). The FLN is defined as the number of labeled neurons in a source area
divided by the total number of labeled neurons in all source areas. As retrograde tracers
are used, the FLN can be considered as an indication of the relative of neurons sending
long‐range projections from one source area to a target.
In Fig. 1(a) we show the logarithms of the FLN values between areas used for the simulations here reproduced. The delay between regions is estimated using wiring distances
between the different regions in the macaque cortex, which are shown in Fig. 1(b), and
assuming a propagation velocity of v = 3.5 m/s [13]. Finally in Fig. 1(c), we show the
hierarchical rank of the different regions in the connectome. The quantities in Fig. 1
are the ones on which later simulations are going to be constructed.
Henceforth, we will denote a pair of cortical areas by the indexes i, and j, in such a
way that FLNij is the FLN from area i to area j. Note that, since the graph given by


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

Figure 1. Data from Markov et. al., [4] used to build the large‐scale networks. In (a) we show the
FLN in logarithmic scale due to the large range of values encountered (non‐existent connections
are shown in black), in (b) the wiring distance between cortical areas, and in (c) the normalized
anatomical hierarchy of each cortical area.

the weighted matrix in Fig. 1(a) is asymmetric, FLNij ̸= FLNji. The delay will be represent by the letter D, and Dij = Dji is the delay between area i and j. Similarly, the
anatomical hierarchy of area i is denoted by hi.
The data used to build the network is available with the code related to this article in:
github.com/ViniciusLima94/ReScience-Joglekar/blob/master/code/interareal (the original data
can be obtained from core-nets.org, however it is necessary to properly organize it in
order to be able to run the model; in our repository, all the necessary preprocessing is
done).

### 2.2 Rate based models

Here we describe the rate based model. We reproduce two sets of results from the original paper in which this model is used: namely, Fig. 1, and Fig. 3 from [5].

Population dynamics — The population dynamics of the rate based model is given by Eq. 1

τE,I

drE,I (t)
dt

= −rE,I (t) + βE,I ϕ[Iext(t)],

(1)

where r(t) is the firing rate of each specific population, the sub‐index E, I indicates
whether the population is excitatory or inhibitory, τ is the time constant, β is the slope
of the frequency‐current curve, Iext is the net external input which is the sum of synaptic
(Isyn), injected (Iinj), and any other input current, and ϕ[x] = max(x, 0) is a thresholdlinear transfer function.


V1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24cV1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24c1010108106104102100Connection StrengthDistances [mm]FromFromToToV1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24cV1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24c01020304050V1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24c0.000.250.500.751.00Hierarchy Index[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

Local circuit — The local circuit is composed of an excitatory and an inhibitory populations, coupled by an excitatory to inhibitory connection (E → I), and an inhibitory
to excitatory connection (I → E). In addition, each population is connected to itself,
via an E → E and an I → I couplings. The local circuit described is schematized in
Fig. 2(a), and can be written as:

τE

τI

drE(t)
dt
drI (t)
dt

= −rE(t) + βEϕ[ωEErE(t) − ωIErI (t) + Iinj,E(t)],

= −rI (t) + βI ϕ[ωEI rE(t) − ωII rI (t) + Iinj,I(t)],

(2)

where ωij is the local synaptic weight from i to j. Iinj,E, and Iinj,I are external currents
injected in the excitatory, and inhibitory populations, respectively.

Large-scale circuit — The local dynamics of regions within the large‐scale network model
follows Eq. 2. However, regions are now heterogeneous and each of them sees its local
weights modulated according to the hierarchical rank of each area. Specifically, the
components of the local synaptic currents in area i, are given by the following equations:


EE = ωEE(1 + ηhi)ri
E,


IE = −ωIEri
I ,


EI = ωEI (1 + ηhi)ri

E


II

= −ωII ri
I ,

(3)

(4)

(5)

(6)

Intra‐regional excitatory currents are increased by a hierarchy dependent gain factor,
in which a parameter η multiplies the hierarchical rank index of the considered areas.
Consequently, regions with a higher hierarchical order are more excitable.
The long‐range synaptic projections are considered to be purely excitatory and their
strength are determined by the weighted graph presented in Section 2.1. In practice, if
the FLN between area i and j is greater than zero (FLNij > 0), those areas are connected.
The total long‐range synaptic currents that the excitatory and inhibitory populations of
area i receive are given by Eqs. 7‐8.


EE = µEE(1 + ηhi)


EI = µEI (1 + ηhi)

FLNjirj
E,

FLNjirj
E,

Nareas∑

j=0
i̸=j

Nareas∑

j=0
i̸=j

(7)

(8)

where µ represents the long‐range synaptic weights, and Nareas is the number of cortical
areas. Note that the long‐range connections are scaled by the hierarchical position of
the target regions.
The total current received by the excitatory and inhibitory populations in an area i can
be expressed by combining Eqs. 3‐8, as follows:

E = 
I i

EE + 

EE + 

IE + I i

inj,E,

+ 

EI + 

II + I i

inj,I,

I = 
I i

EI


(9)

(10)


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

The transmission delay (Dij) between areas i and j is neglected and considered to be
instantaneous (Dij = 0, ∀ i and j), so that no use is made of the tract length matrix of
Fig. 1b, but only of the FLN matrix of Fig. 1a and the hierarchical order of Fig. 1c.

### 2.3 Spiking neuron models

In this section, we describe the spiking neuron network models. Based on them, we
reproduced the results of Fig. 5, and Fig. 6 from the original paper.

Single neuron — Neurons were modeled using the leaky integrate‐and‐fire (LIF) model as
follows.

dV (t)
dt

= − V (t) − Vr

τE,I

+

Iext(t)
CE,I

,

(11)

where V (t) is the time‐dependent membrane potential, Vr is the resting potential, τ is
the membrane time constant, and C is the membrane capacitance. The external current
is given by Iext = Isyn + Iinj, where Isyn is the synaptic, and Iinj the injected currents.
A spike is emitted following the spike‐and‐reset rule in Eq. 12:

{

V (t) ≥ Vth

⇒

Spike at time t
V (t + τref) = Vreset,

(12)

where Vth is the spike threshold, τref is the refractory period, and Vreset is the reset value
of the membrane potential. In Table 1, we show the parameters used for the LIF neuron.

Vr [mV]
‐70.0

Vreset [mV]
‐60.0

V (0) [mV]
‐70.0

τE [ms]
20.0

τI [ms]
10.0

τref [ms] CE [pA] CI [pA]
200.0
400.0

### 2.0 Table 1. Parameters for the LIF neuron model in Eqs. 11‐12.

Local circuit — The local circuit in each spiking region is composed of N = NE + NI =
2000 LIF neurons, where NE = 1600 are excitatory, and NI = 400 are inhibitory. Connections are random and sparse, established with a fixed probability for each pair of
neurons set as p = 0.1. The synaptic current received by the neuron i is given by:

I i
syn =

∑

∑

ωji

j

k


j

− d),

(13)

where ωji is the synaptic weight from neuron j to neuron i, tk
j is the time of the kth
spike from neuron j, and d is the local delay. The input spike‐trains are mathematically
represented as the sum of Dirac delta terms.
The local synaptic currents are obtained by replacing the rates rE, and rI in Eqs. 3‐6
with the input spike trains from Eq. 13. The total local synaptic current received by an
excitatory neuron in area i is obtained by combining Eqs. 14‐15:


EE =

N pre
E∑

j=0

ωEE(1 + ηhi)

∑

k


j

− d),


IE = −

N pre
I∑

∑

ωIE

j=0

k


j

− d), ,

(14)

(15)

and the total local synaptic current received by an inhibitory neuron in area i is given
by Eqs. 16‐17.


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex


EI =

N pre
E∑

j=0

ωEI (1 + ηhi)

∑

k


j

− d),


II

= −

N pre
I∑

∑

ωII

j=0

k


j

− d),

(16)

(17)

In the expression above, N pre
pre‐synaptic neurons, respectively.

E , and N pre

I

are the number of excitatory and inhibitory

Large-scale circuit — Each region is modeled as the local circuit described above. Their
long‐range synaptic currents received by excitatory and inhibitory neurons in area i
from neurons in area j, are given by:


EE =


EI =

N pre
E∑

j=0

N pre
E∑

j=0

µEE(1 + ηhi)FLNji

µEI (1 + ηhi)FLNji

∑

k

∑

k


j

− D

′

ji),


j

− D

′

ji),

(18)

(19)

′

′

ji are sampled from normal distribution with mean Dji, and standard deji = N (Dji, 0.1Dji)). These delays were estimated dividing the tract

The delays D
viation 0.1Dij (D
lengths (Fig. 2b) by the propagation velocity of v = 3.5 m/s.
The hierarchical order of the targeted region is scaled via a gain parameter η. All the parameters used in the model of a large‐scale circuit described above are given in Table 5.

### 2.4 Balanced amplification

As we briefly mentioned in Section 1, the models described above were used to study
signal propagation in the cortical system. In Joglekar et. al., [5], the mechanism of bal-
anced amplification, is hypothesised to contribute to reliable signal propagation through
the cortical hierarchy.
For the local circuits, and 2.3.2) this mechanism is refereed to as local balanced amplification (LBA), and consists of increasing the recurrent excitation (ωEE), and the lateral
inhibition (ωIE). For the large‐scale circuits this mechanism is referred to as global balanced amplification (GBA), and consists of increasing the long‐range E → E excitation
(µEE), and the local lateral inhibition (ωIE).
These balanced amplification mechanisms, when activated, can achieve two effects:
first, through the increase of excitatory couplings, signal transmission among areas is
enhanced; and, second, increasing the lateral inhibition within local circuits, network
instability is avoided, despite the overall increase in excitation.
In the results we will compare signal propagation in the models above in two alternative
regimes, corresponding to two distinct functional states of the brain network: (i) Weak
LBA/GBA, and (ii) Strong LBA/GBA. The transition from regime (i) to (ii) is done via increasing ωEE/µEE, and ωIE, as described above. The parameters used in each regime
are specified in the specifically associated results section.

## 3 Results

In this Section we will present the results we choose to replicate from the original article. These results give an outlook of the mechanism of global balanced amplification


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

(Section 2.4). In Sections 3.1‐3.3 we replicate the result in Figures 1, 3, 5 and 6 from
Joglekar et. al. [5]. For each result we also highlight the issues we had replicating it,
such as the parameters values not informed in the original publication. The name of
those parameters will be coloured red in the parameter Tables 2‐5.

### 3.1 Local Balanced Amplification in an Inhibition-Stabilized Local Circuit

To reproduce a first result in Figure 1 of the original [5] paper, we use the local circuit
described by the rate based model of Eq. 2. In Fig. 2(a), we show a schematic representation of this simple circuit. The parameters for the used model are given in Table 2 of this
article. All parameters were copied from the original publication, apart from τE and τI
for which we could not find an explicit value in the original publication. However, in
line with descriptions and Equation 1 therein, we set τE = τI = τ and adjusted this
common value τ to get figures looking similar to the original ones. The estimated value
is the one we report in Table 2, together with the other parameters.
This first result we reproduce exemplify the mechanism of balanced amplification within
a local circuit. In Fig. 2(b), we show the evolution of the excitatory rate rE(t), starting
from the initial condition rE(0) = 1, and rI (0) = 0. This initial condition emulates the
state in which the E population is already active due to a transient input. The green and
violet curves correspond to the E rate evolution in a weak and strong LBA conditions.
Note that the response of the system is indeed enhanced in the strong LBA case, leading
to evoked activity which has both a stronger peak amplitude and an enhanced transient.

Figure 2. Replication of the result in Figure 1 of the original publication [5]. In (a) we show a
schematic depiction of the local circuit used to generate the results, in (b) we show the response
rate of the excitatory population after its initial value being set to 1 Hz (emulating application of a
brief destabilizing input), for weak (green) and strong (purple) local balanced amplification (LBA).
In (c), we show the peak rate of the excitatory population as a function of ωEE, and ωIE, where
the green and purple circles indicate the points used to produce the curves in (b) (corresponding,
respectively, to the used weak and strong LBA conditions)

To illustrate the mechanism of LBA, in Fig.2(c) we show the peak response of the excitatory population as a function of the internal couplings ωEE, and ωIE. The regions
where the excitatory rate diverge are shown in gray. As it can be seen, a high increase
of ωEE destabilizes the circuit making its rate explode, however as ωIE increases, larger
values of ωEE can be tolerated before triggering a rate instability. Remark that both the
weak and strong LBA working points lie at the slightly sub‐critical edge of this rate instability. We consider that the replication of this result was successful, despite one of the
parameters in Table 2 had to be estimated.


0.00.10.20.30.40.50.6Time (s)0123456Excitatory rate (Hz)weak LBAstrong LBAEI4.04.55.05.56.06.57.0Local E to E coupling4.55.05.56.06.57.07.5Local I to E coupling012345678[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

ωEI [pA/Hz]
ωII [pA/Hz]
βE
βI
rE(0) [Hz]
rI (0) [Hz]
τ [ms]
ωEE [pA/Hz]
ωIE [pA/Hz]

Weak LBA Strong LBA
4.29
4.71
1.00
1.00
1.00
0.00

20.0
4.45
4.70

30.0
6.00
### 6.70 Table 2. Parameters used in Eq. 2 to produce the results in Fig. 2. For the parameters in red we
could not find a value in the original publication and we had therefore to guess values allowing
the reproduction of the published results. Note that we have used τE = τI = τ .

Missing parameters: τ .

### 3.2 Global Balanced Amplification in the Large-Scale Model Improves Signal Propaga-

tion

Next, we study the propagation of an input pulse in the network composed of 29 cortical
areas [4] (Section 2.1), where each node comprises an E and I population of rate based
model (Section 2.2). All the parameters used for the model are given in Table 3.
In Fig. 3(a,b) we show a schematic representation of the connection between two cortical areas, for the weak and strong GBA cases. The increase in µEE and ωIE for the strong
GBA conditions is represented by the thickness of the arrows for these connections in
Fig. 3(b).
For each area i a background input is inject to the excitatory (I i
BG,E) and inhibitory
(I i
BG,I ) populations in order to maintain a background rate of rBG
E = 10 Hz in the first and
rBG
I = 35 Hz in the latter. The initial firing rates are set as being equal to the background
rate.
To compute I i
BG,I , first let WWW EE, WWW IE, WWW EI and WWW II be square matrices
with size Nareas. Then, using M ij to denote the element in row i and column j from a
given matrix M , we can compute each element from those matrices as:

BG,E and I i

{

W ij
EE

⇒

µEE(1 + ηhi)FLNji, if i ̸= j,
−1 + ωEE(1 + ηhi), if i = j,

{

0, if i ̸= j,
−ωIE, if i = j,

W ij
IE

⇒

{

W ij
EI

⇒

µEI (1 + ηhi)FLNji, if i ̸= j,
ωEI (1 + ηhi), if i = j,

{

W ij
II

⇒

0, if i ̸= j,
−1 + ωII , if i = j.

and,

Next we define the square matrix AAA with size 2Nareas:
]

[
WWW EE WWW IE
WWW EI WWW II

,

AAA =

(20)

(21)

(22)

(23)

(24)

and BBB a matrix with dimensions [2Nareas, 1], where Bi = rBG
Bi = rBG
I . The background currents are computed as:

E for i < Nareas, otherwise


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

where × is the matrix multiplication, I i

BG,I are given by:

III BG = −AAA × BBB,
BG,E, and I i

{

I i
BG,E = I i
I i−Nareas
BG,I = I i

BG, if i < Nareas,

BG, if i ≥ Nareas.

(25)

(26)

Such procedure lead to determine parameters associated to the steady‐state working
point of the network. For exact derivation, of Eq. 26 see [5] star methods section.
To simulate the signal propagation, an input is injected in the excitatory population of
the primary visual cortex (V1) for tdurr = 225 ms, from ti = 200 ms to tf = 225 ms. For

Figure 3. Reproduction of Figure 3 from the original paper [5]. In (a) and (b), we show inter‐regional
coupling within the large‐scale connectome model for the regimes of weak and strong Global
Balanced Amplification (GBA). In (c) and (d), we show propagating pulses of response to a stimulus
injected in region V1, in regions with increasing hierarchy. Responses in (d) are sustained for
longer times in certain regions and stronger in amplitude (the green lines in (d) correspond to
the lines in (c), remark the changed vertical time‐scale). The increase in peak response in strong
vs weak GBA is also visualized for all regions in (e), in (f) we show the maximum excitatory rate
at area 24c for weak (blue) and strong (black) GBA, the solid lines correspond to the simulations
using the correction given by Eq. 27.


EIEIEIEI110.073250 msWeak GBA109.916V1V1V2V4DPMT8m58lTEO2F1STPc7A46d109/46v9/46dF5TEpdPBr7m7BF2STPiPROmF78BSTPr24cAreas102100102Maximum firing rate [Hz]Weak GBAStrong GBA20253035404550Global E to E coupling108106104102100102104Maximum rate in 24c [Hz]Weak GBA, Eq. (2) + (27)Weak GBA, Eq. (2)Strong GBA, Eq. (2) + (27)Strong GBA, Eq. (2)250 msStrong GBA3.98971.98V40.0284.7868m0.1567.6778l1.1641.415TEO0.0483.3027A0.0616.3749/46d0.25313.95TEpd0.0071.11724c[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

inj,E = 41.90 pA/Hz and for the strong GBA

the weak GBA the input injected in V1 was I V1
I V1
inj,E = 21.93 pA/Hz.
The input injected to area V1 is attenuated of factor larger than 10, 000 times as it reaches
area 24c in the weak GBA, while for the strong GBA the attenuation is approximately of
only 100 times (Fig. 3(c,d)). The enhancement in signal propagation can also be tracked
by looking at the peak firing rate in each cortical area after the input was injected in V1.
In Fig. 3(e), we show the peak response rate in each region for both the weak and strong
GBA regimes. The plot is in logarithmic scale manifesting the large level of boosted
propagation to higher hierarchical order areas.
Finally, in Fig. 3(f), we measured the maximum response firing rate in area 24c (highest
hierarchical order) as a function of the long‐range coupling scale µEE, the the weak and
strong GBA cases. For both conditions, we use the same parameters as for the weak GBA
in Fig. 3(c), and the values of µEE used go from 20 pA/Hz to 50 pA/Hz with a step of
2 pA/Hz. For the strong GBA we have increased ωIE using the following rule: ωIE =
19.7 + 0.31µEE, that was set manually based on the ranges used in their Matlab source
code (see bellow).
The first result we obtained is shown by the dashed lines in Fig. 3(f). For values of µEE <
30 pA/Hz, the obtained result diverged from the original one and we obtained greater
peak firing rates in area 24c.
We were able to retrieve the original results, shown in solid lines in Fig. 3(f), by introducing the following condition while solving the rate equations numerically:

If rE,I (t) < rBG

E,I , then rE,I (t) = rBG

E,I .

(27)

This condition was not mentioned in the original article. However it was found in the
Matlab implementation of the model that we cited in the section “Availability of code
implementations for the original model”.
Such adjustment guarantees that the firing rates of any population in the model do
not go below their baseline activity, causing some of the populations to be effectively
“switched off”. In absence of this condition, some of the inhibitory populations would
become too silent, reducing the overall level of inhibition and thus causing some rates
to increase in an unbalanced way (hence the larger peak response rate in area 24c).
The condition in Eq. 27 was not mentioned in the original publication. In order to be
able to reproduce this result we made a modification to NEST source code, adding the
possibility to set the condition given in Eq. 27 as an option for the rate model available in NEST. This resulted in a pull‐request that was integrated as the model “threshold_lin_rate” in NEST from version 3.0 [14]. For this reason it is recommended to use
this updated version when attempting to run our simulation codes.
Overall, we were able to replicate the behavior of the reference model. However, concerning the specific result of Fig. 3(f), the original result could be reproduced only adding
the ad hoc but reasonable condition in Eq. 27.

### 3.3 Reliable Signal Propagation in a Spiking Network Model

Next, we continue the analysis of the propagation of an input signal in the large‐scale
model, but replacing the rate units with the regional spiking network model described
in Section 2.3.
We study signal propagation in the spiking large‐scale model for two different regimes
of the network: (i) asynchronous and (ii) synchronous. In both cases, we perform simulations in both the weak and strong GBA conditions. The parameters for (i) and for (ii)
are given in Table 5.
The activity of the network is driven by independent white noise background currents
injected in all neurons, and given by Eq. 28.


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

I i
BG,E,I = µV,E,I

CE,I
τE,I

+ σV

CE,I
τE,I

1 + e−dt/τE,I
1 − e−dt/τE,I

ξ(t),

(28)

where µV is the average value of the membrane potential, σV is the standard deviation of
the noise, both in mV, and ξ(t) is a Gaussian variable with zero mean and unit variance.
In the original paper, the authors mention that a background input was given to the network in order to maintain the spiking activity of the excitatory population between 0.75
and 1.5 Hz and the inhibitory population between 5 and6 Hz. Although the authors did
not specify the background noise parameters, the model equations found in their Brian2
code take the form dV /dt = f (V ) + (σ/τ )ξ(t) (“rishimodelpython_brian2_spiking.py”),
lines 137 and 141). We converted the values of σ set on their code using Eq. 28. However,
some adjustments of the parameters were required to reproduce the specified steadystate rates (Table 4).
To study signal propagation we injected an external current pulse into all excitatory neurons in V1 (I V1
inj,E). In the next two sessions we show the results for the asynchronous and
synchronous regimes.

inj,E = 126 pA.

inj,E for
inj,E = 300 pA, and

Asynchronous regime — For the asynchronous regime we injected an input pulse I V1
tdurr = 150 ms, from ti = 500 ms to tf = 650 ms. For the weak GBA I V1
for the strong GBA I V1
In Fig. 4(a,b) we show the raster plot (only excitatory neurons within each area are
shown) for the weak and strong GBA conditions. Our result is very similar to the original one. For the weak GBA condition, the signal propagates to a few areas only along
the ventral visual stream: V1, V2, V4, TEO and TEpd. In the strong GBA condition, the
response to the input injected in V1 is enhanced in those areas, and other areas are
reached as well such as: 7A, 46d, 7m and 7B. The arrival time in each area varies due to
the used synaptic inter‐areal delays in long‐range connections.
To show the propagation of the signal to other areas, in Fig. 4(c) we measure the peak
excitatory firing rate between ti and tf + 20 ms. The maximum firing rates are plot
in logarithmic scale and one can observe that they indeed increase for the strong GBA
condition, with a near‐perfect quantitative matching with the original figure in [5]. The
results about signal propagation in the large‐scale spiking network model in the asynchronous regime are reproduced in our NEST model.

inj,E = 200 pA.

inj,E for
inj,E = 200 pA and for

Synchronous regime — For the synchronous regime we injected an input pulse I V1
tdurr = 8 ms, from ti = 500 ms to tf = 508 ms. For the weak GBA I V1
the strong GBA I V1
We performed the same analyses as for the asynchronous case. In Fig. 5(a,b) we show
the raster plot for the weak and strong GBA conditions. Qualitatively we got a result
very similar to the original one, even though the maximum response rate per regions
in Fig. 5(c) had some quantitative differences. Notably, the response amplification we
obtained for hierarchically‐intermediate regions as STPc, 7a, 46d and 10 was less strong
than in the original model and we did not observe substantial amplification in the highest order regions as STPr and 24c. In general, all rates we obtained in early regions (V1,
V2, V4, DP, MT) were stronger than expected.
We report in Fig. 5 a simulation with a good semi‐quantitative match with the original
results. However, we also noticed that the network is highly sensitive to the random
seed used to initialize the simulation and this sensibility on initial conditions may explain the quantitative deviations between our response profile and the one shown in the
original paper. It is important to note that NEST assigns different seeds to each thread
used to simulate the network, therefore, using a different number of threads when running a parallel situation might change the result, making even more difficult to obtain


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

Figure 4. Signal propagation in the large‐scale spiking neuron network in the asynchronous regime.
In (a) we show the network response to a stimulus applied to V1 (I V1
inj,E = 300 pA) during 150 ms
in the weak GBA. In (b) we show the same but for the strong GBA condition (I V1
inj,E = 126 pA). In
(c) we show the peak response rate in each region along the cortical hierarchy, after the stimulus
injection in V1 for the weak (green), and strong GBA (purple) conditions.

exactly the same raster when repeating the simulation multiple times (for our simulation we have used 20 threads). Furthermore, we noticed the same phenomenon when
running the original Brian 2 code for this model (data not shown), which suggests this
is not an issue of incorrectly fitting parameters but rather an intrinsic property of the
model. Additionally, we noticed that in the authors’ script the seed was fixed (“rishimodelpython_brian2_spiking.py”, lines 30‐32).
Further investigations revealed that the network activity depends on the state set for
the random number generator. For Figs. 4‐5, we run the simulations for a range of random seed values to obtain the expected results. However, changing their values could
generate an unstable network. Especially, for the strong GBA and synchronous case,
activity can become epileptic‐like in some high‐order regions, as shown in an example
simulation in Fig. 6. Conversely, this dependence on initial conditions can generate instances in which the network is in a less excitable state, as a consequence activity may
not reach areas such as PROm. In other cases, activity will reach even area 24c, without
divergence of firing rates, if the network is in a slightly more excitable state.
This suggests, that the synchronous network may be sitting close to a rate instability.
Tuning the system to be slightly subcritical is crucial for access to high‐hierarchical


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

Figure 5. Signal propagation in the large‐scale spiking neuron network in the synchronous regime.
In (a) we show the network’s response to a stimulus applied to V1 (I V1
inj,E = 200 pA) during 8 ms in
the weak GBA condition. In (b) we show the same but for the strong GBA condition (I V1
inj,E = 200
pA). In (c), we show the peak frequency in each area after the stimulus injection in V1 for the weak
(green), and strong GBA (purple) conditions.

order regions to take place, as an effect of enhanced GBA. However, we may have been
using a too narrow safety margin, or an exceedingly strong input pulse. The simulations
we show have been done with parameter choices providing the best a posteriori match
we could find between reproduced and original simulations. However, some parameters
had to be guessed, as previously mentioned, since we could not find where they are
explicitly informed in the original paper, which makes our attempts of reproduction
more complication as systematic parameter search in such a large‐scale spiking model
is beyond reach (or, anyway, too carbon‐costly).
Notice that some in some early sensory regions (V1 to MT) the peak rates are an order of
magnitude stronger than in the original paper. However, even considering that some key
information to reproduce the model was missing (see Section 3.4) the main qualitative
features of the original results (amplification and selective access to high‐order ventral
stream regions) are reproduced, we consider that, even in the synchronous regime, we
have successfully reproduced the nature of results in the original paper.For


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

Figure 6. Raster plot for the synchronous regime network with strong GBA condition, with all parameters as in Fig. 5, but with a different choice of random seeds for the parallel simulation. This
example raster manifests that, depending on the seed used, the network may become exceedingly
unstable.

### 3.4 Important information needed during replication

In this section we list some information and parameter values that were needed to replicate the results, but were not found in the original article.

• The time constants τE and τI defined for the rate based model in Eq. 2 and used
for the weak and strong GBA were not informed. For this work we made the approximation that τ = τE = τI and then we adjusted them by hand. The values
that better fit the expected results are presented in Table 2.

• The values of ωIE used for the strong GBA in Fig. 3(f) were not cited in the main
reference and we estimated it by considering that ωIE increases linearly with µEE:
ωIE = 19.7+αµEE, where 19.7 is the ωIE used for the weak GBA and the parameter
α was adjusted in order to obtain a result close to the original one. The value of α
that gave the best approximation we could find was α ≈ 0.31.

• Another important information to reproduce the Figure 3 from the Joglekar et al.
(2018) is the fact that we can only obtain the expected results if we include the minimum activity condition defined in Eq. 27 when solving the Eq. 2. However, this
detail was not mentioned in the original article. In Fig. 3(f) we show the difference
of the results by considering or not the condition defined in Eq. 27.

• The background noise needed to activate the spiking network model were not
given in details in the reference article. The only information found were the mean
firing rate ranges in the absence of input which are: 0.75 to 1.5 Hz for the excitatory
population; and 5 to 6 Hz for the inhibitory population. To try to obtain these firing rates we used, by simplicity, white noise background currents independently
injected into every neuron, as described by Eq. 28 (the average firing rates of the
network in the absence of stimuli are shown in Table 4 for each condition, all the
values are in the range cited in the original publication). The parameters of this
white noise currents were adjusted manually (systematic optimization out of reach
for such a massive model) and the values are presented in Table 5.

• Considering the approximations made for the spiking network model, we found
that rate instabilities could eventually be induced by specific choices of seeds for


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

generating random numbers. And that in some conditions, the peak firing rate of
some areas could reach one order of magnitude more than the ones reported in the
original paper. This sensitivity is particularly evident in simulations conducted
in the high synchrony, strong GBA case. As we shown in Fig. 4 and 5 we were
nevertheless able to replicate the results of Figures 5 and 6 from Joglekar et al.
(2018). However, simulations were unstable for some random seeds.

• The results obtained may depend on both the Python and Nest version used, since
the RNG algorithms and C compiler used by NEST can influence the results. Since
the number of threads used to run the code also changes the seeds assigned to each
parallel executer, this can also impact on the results resulting in slightly different
outcomes.

## 4 Conclusion

Using the NEST simulator to re‐implement the original model we were able to reproduce
the main results of the original article [5], at least in their qualitative essence and, often,
also in precise quantitative match. In general, our results confirm the validity of the
central concepts of the original paper, notably about the role of balanced amplification
mechanisms in enhancing signal propagation while guaranteeing network stability.
In our replication, we also pointed some difficulties to reproduce the original model. All
of them suggest that the “sweet spot” needed for strong LBA and GBA to properly work
is more difficult than estimated to obtain, as variations in the exact rate of specific regions and transient loss of E/I balance within them could compromise the delicate equilibrium between excitatory boosting and inhibitory stabilization. Thus, from our reproduction attempts, we also learn that it may be important for physiological networks to
embed regulatory mechanisms that help maintaining the network operation point close
to this desired sweet‐spot. Such role may be played for instance by neuromodulatory or
homeostatic plasticity processes [15, 16], not included in simple mechanistic models as
the one we reproduce here.
In this context in which a careful fine tuning seems to be needed for perfect functionality, we suffered particularly of the lack of information about some of the parameters
(or, at least, of our unsuccessful attempts to find this information). We do not exclude
thus that with other, more adapted parameter choices the robustness of GBA‐mediated
signal propagation gets further strengthened.

## 5 Acknowledgements

DB acknowledges the organizers of the Latin American School on Computational Neuroscience (LASCON VIII, Sao Paulo, Brazil), since the idea of performing this replication
was born during discussions in the context of this school where he had kindly been invited. DB and VL are supported by the Maria Skłodowska‐Curie action program of the
European Union under the Innovative Training Network ”iConn” (H2020 ITN 859937).
R.O.S. thanks financial support from São Paulo Research Foundation (FAPESP), grant
2017/07688‐9. This study was financed in part by the Coordenação de Aperfeiçoamento
de Pessoal de Nível Superior ‐ Brasil (CAPES) ‐ Finance Code 001. ACR is supported
by the São Paulo Research Foundation (FAPESP) grant 2013/07699‐0 (CEPID NeuroMat)
and by Brazilian National Council for Scientific and Technological Development (CNPq)
Research Productivity Grant 303359/2022‐6. N.L.K. thanks financial support from São
Paulo Research Foundation (FAPESP), grant 2016/03855‐5.


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

References

2.

1. M. C. van Rossum, G. G. Turrigiano, and S. B. Nelson. “Fast propagation of firing rates through layered networks
of noisy neurons.” In: Journal of neuroscience 22.5 (2002), pp. 1956–1966. DOI: 10.1523/JNEUROSCI.22-05-
01956.2002. URL: https://doi.org/10.1523/JNEUROSCI.22-05-01956.2002.
A. Kumar, S. Rotter, and A. Aertsen. “Conditions for propagating synchronous spiking and asynchronous
firing rates in a cortical network model.” In: Journal of neuroscience 28.20 (2008), pp. 5268–5280. DOI:
10.1523/JNEUROSCI.2542-07.2008. URL: http://dx.doi.org/10.1523/JNEUROSCI.2542-07.2008.
A. Kumar, S. Rotter, and A. Aertsen. “Spiking activity propagation in neuronal networks: reconciling dif-
ferent perspectives on neural coding.” In: Nature reviews neuroscience 11.9 (2010), pp. 615–627. DOI:
10.1038/nrn2886. URL: http://dx.doi.org/10.1038/nrn2886.

3.

4. N. T. Markov, M. Ercsey-Ravasz, A. Ribeiro Gomes, C. Lamy, L. Magrou, J. Vezoli, P. Misery, A. Falchier, R. Quilo-
dran, M. Gariel, et al. “A weighted and directed interareal connectivity matrix for macaque cerebral cortex.” In:
Cerebral cortex 24.1 (2014), pp. 17–36. DOI: 10.1093/cercor/bhs270. URL: http://dx.doi.org/%2010.1093/cer
cor/bhs270.

5. M. R. Joglekar, J. F. Mejias, G. R. Yang, and X.-J. Wang. “Inter-areal balanced amplification enhances signal
propagation in a large-scale circuit model of the primate cortex.” In: Neuron 98.1 (2018), pp. 222–234. DOI:
10.1016/j.neuron.2018.02.031. URL: http://dx.doi.org/10.1016/j.neuron.2018.02.031.

7.

6. G. Elston. “Specialization of the Neocortical Pyramidal Cell during Primate Evolution.” In: Evolution of Nervous
Systems. Ed. by J. H. Kaas. Oxford: Academic Press, 2007, pp. 191–242. DOI: 10.1016/B0-12-370878-8/00164-
6. URL: http://dx.doi.org/10.1016/B0-12-370878-8/00164-6.
R. Chaudhuri, K. Knoblauch, M.-A. Gariel, H. Kennedy, and X.-J. Wang. “A large-scale circuit mechanism
for hierarchical dynamical processing in the primate cortex.” In: Neuron 88.2 (2015), pp. 419–431. DOI:
10.1016/j.neuron.2015.09.008. URL: http://dx.doi.org/10.1016/j.neuron.2015.09.008.
J. F. Mejias, J. D. Murray, H. Kennedy, and X. J. Wang. “Feedforward and feedback frequency-dependent inter-
actions in a large-scale laminar network of the primate cortex.” In: Sci. Adv, 2 (2016), e1601335. DOI: 10.1126/s-
ciadv.1601335. URL: http://dx.doi.org/10.1126/sciadv.1601335.

8.

9. M. Stimberg, R. Brette, and D. F. Goodman. “Brian 2, an intuitive and efficient neural simulator.” In: Elife 8 (2019).

DOI: 10.7554/eLife.47314. URL: http://dx.doi.org/10.7554/eLife.47314.

10. M.-O. Gewaltig and M. Diesmann. “Nest (neural simulation tool).” In: Scholarpedia 2.4 (2007), p. 1430.
11.

J. Jordan, R. Deepu, J. Mitchell, J. M. Eppler, S. Spreizer, J. Hahne, E. Thomson, I. Kitayama, A. Peyser, T. Fardet,
et al. NEST 2.18. 0. Tech. rep. Jülich Supercomputing Center, 2019.

12. N. T. Markov et al. “The role of long-range connections on the specificity of the macaque interareal cortical
network.” English. In: Proceedings of the National Academy of Sciences of the United States of America
110.13 (Mar. 2013), p. 5187 5192. DOI: 10.1073/pnas.1218972110.

14.

13. H. A. Swadlow. “Efferent neurons and suspected interneurons in S-1 forelimb representation of the awake
rabbit: receptive fields and axonal properties.” In: Journal of Neurophysiology 63.6 (1990), pp. 1477–1498.
DOI: 10.1152/jn.1990.63.6.1477. URL: http://dx.doi.org/10.1152/jn.1990.63.6.1477.
J. Hahne et al. NEST 3.0. Version 3.0. June 2021. DOI: 10.5281/zenodo.4739103. URL: https://doi.org/10.528
1/zenodo.4739103.
J. M. Shine. “Neuromodulatory Influences on Integration and Segregation in the Brain.” In: Trends in Cognitive
Sciences 23.7 (2019), pp. 572–583. DOI: 10.1016/j.tics.2019.04.002.
P. J. Sjöström, G. G. Turrigiano, and S. B. Nelson. “Rate, timing, and cooperativity jointly determine cortical
synaptic plasticity.” eng. In: Neuron 32.6 (Dec. 2001), pp. 1149–1164. DOI: 10.1016/s0896-6273(01)00542-6.

16.

15.


[Re] Inter-areal Balanced Amplification Enhances Signal Propagation in a Large-Scale Circuit Model of the Primate Cortex

ωEI [pA/Hz]
ωII [pA/Hz]
ωEE [pA/Hz]
µEI [pA/Hz]
βE/βI
E /rBG
rBG
[Hz]
I
rE(0)/rI (0) [Hz]
τE/τI [ms]
η
τi/τf [ms]
ωIE [pA/Hz]
µEE [pA/Hz]
I V 1
inj,E [pA/Hz]

Weak GBA Strong GBA
12.5
12.5
24.3
25.3
0.066/0.351
10/35
10/35
20/10
0.68
200/225

19.7
33.7
41.90

25.2
51.5
### 21.93 Table 3. Parameters used for the large‐scale rate based model described in Section 2.2.3, to produce
the results in Fig. 3.

Firing rate [Hz] Asynchronous

Weak GBA

Excitatory
Inhibitory

Excitatory
Inhibitory

1.30
### 5.59 Strong GBA
1.49
### 5.99 Synchronous
0.83
5.62

0.82
### 5.52 Table 4. Average firing rate for each cell population type and each network state.

Asynchronous

Synchronous

Weak GBA Strong GBA Weak GBA Strong GBA

ωEI [mV]
ωII [mV]
ωEE [mV]
µEI [mV]
d [ms]
η
µV,E [mV]
µV,I [mV]
σV [mV]
tdurr [ms]
ωIE [mV]
µEE [mV]
I V1
inj,E [pA]

0.075
0.075
0.01
0.19/4
2.0
4.0
284.0
314.0
2.12
150.0

0.3
0.3
0.04
0.19
2.0
4.0

308.0

320.0

280.0
2.12
8.0

0.0375
0.0375


0.05
0.05


0.56
0.16


0.98
0.25


Table 5. Parameters used for the spiking neuron networks in the asynchronous , and synchronous
regimes , and for strong, and weak GBA for both regimes. For the parameters indicated in red,
we could not find corresponding values in the original paper, therefore we had to estimate their
values to guarantee a semi‐quantitative matching between our reproduced and the original results.
Systematic optimization is out‐of‐reach for such a complex large‐scale spiking model.

Missing parameters: µV,E, µV,I , σV .

---
**Source PDF:** `724990bc1a61.pdf` (2023_02_article.pdf)  
**URL:** https://zenodo.org/record/10257800/files/article.pdf
