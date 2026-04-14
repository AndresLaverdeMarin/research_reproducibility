R E S C I E N C E C

Replication / Computational Neuroscience
[Re] Context-Dependent Encoding of Fear and Extinction
Memories in a Large-Scale Network Model of the Basal
Amygdala

Tawan T. A. Carvalho1, ID , Luana B. Domingos2, ID , Renan O. Shimoura3, ID , Nilton L. Kamiji3, ID , Vinicius L.
Cordeiro4, ID , Mauro Copelli1, ID , and Antonio C. Roque3, ID
1Department of Physics, Federal University of Pernambuco, Recife, Brazil – 2Department of Pharmacology, Ribeirão Preto
Medical School (FMRP), University of São Paulo, Ribeirão Preto, Brazil – 3Department of Physics, School of Philosophy, Sciences
and Letters of Ribeirão Preto (FFCLRP), University of São Paulo, Ribeirão Preto, Brazil – 4Systems Neuroscience Institut (INS,
UMR 1106), Aix-Marseille University, Marseille, France

Edited by
Etienne B. Roesch ID

Reviewed by
Etienne B. Roesch ID

Received
03 May 2021

Published
11 September 2021

DOI
10.5281/zenodo.5657320

Abstract The basal nucleus of the amygdala (BA) is related to the process of creating memories of conditioned
fear and extinction that are both dependent on the context. Vlacho and collaborators developed two models of
neural networks to study the effect of plasticity based on a specific phenomenological rule in BA excitatory neurons.
When an excitatory subpopulation receives conditioned stimulus (CS) and contextual inputs in narrow time windows,
synaptic weights are potentiated by this effect, increasing the subpopulation’s firing rate related to the specified
context. In this replication, we implemented the models using Python (for the mean-field model) and Brian 2 (for
the spiking neuron model), and we were able to reproduce the original results qualitatively. In order to replicate the
model, it was necessary to estimate a considerable amount of parameters and to adapt some of the protocols that
were either ambiguous or absent in the methodological descriptions of the original work.
A replication of Vlachos2011.


The authors have declared that no competing interests exists.
Code is available at https://github.com/tawantayron/RE-Fear-and-extinction-in-a-BA-net-model..
Open peer review is available at https://github.com/ReScience/submissions/issues/49.




Introduction

The basal nucleus of the amygdala (BA) plays a central role in context‐dependent fear associations [1], and computational modeling constitutes an important tool to understand
the mechanisms involved. A neural network model of the basal amygdala could be used
to simulate the differential recruitment of two distinct subpopulations of neurons during conditioning and extinction of fear memory [2]. Differential activation of neurons
may result from the simultaneous association of the conditioned and unconditioned
stimuli (CS − U S) in the conditioning context, and weakened association in the extinction context. For a specific context, neurons are stimulated by different contextual
inputs (CT X) [1]. Vlachos et al. [2] developed two models to study this dynamics in the
BA: a mean‐field model and a large‐scale network of leaky integrate‐and‐fire (LIF) neurons with conductance‐based synapses. The original implementation used MATLAB for
the mean‐field model and the NEST simulator [3] for the spiking network model. Here,
we reimplemented the models using Python and the Brian 2 simulator [4], and provided
information about parameter values and simulation conditions not explicitly described
in the main article.

Methods

In the present work we replicate the main results from Vlachos et. al. [2]. In this section,
we explain the details of the implementations of the two models. We start by describing
the mean‐field model, then we move to the spiking network model and the measures and
methodological procedures adopted in the original work. Here, we refer to the CS − U S
input as only CS, since there is no explicit distinction between them in the reference
work.

Mean-field model

The mean‐field model is described by a Wilson‐Cowan type rate dynamics [5], and consists of two neural populations with dynamics described by

τi

dRi
dt

= −Ri + ξ(t) + (ki − riRi)Φ(Ii),

(1)

where the subindex i (i ∈ {A, B}) indicates the neural population, Ri is the time‐dependent
population firing rate, ξ is a Gaussian white noise input ξ(t) = N (µ, σ), ki is the maximum firing rate, ri is the refractoriness parameter, and Φ is the transfer function defined by

Φ(x) =


1 + e−p(x−θ)

.

(2)

The function in Equation 2 is a sigmoid with values in the range [0, 1], and the parameters p and θ determine its steepness and point of maximum slope, respectively. The
input received by population i is represented by Ii, and consists of synaptic and external inputs,

Ii = wijRj
| {z }
synaptic

|

,
+ wi,CSCSi + wi,CTXCT Xi
}
{z
external

(3)

where, wij indicates the weight of the synaptic connection from population j to i. CSi
and CT Xi are the conditioning and contextual inputs to population i with their respective synaptic weights wi,CS and wi,CTX. Equations 1 to 3 shown above are equivalent to
Equations 1 and 2 in the original article, we just opted for a more general presentation
of the Wilson‐Cowan type rate dynamics.




The CS input consists of a sequence of short square pulses of 50 ms duration each, and
the CT X input is a longer square pulse applied continuously. When CT X is active for
population i it is silent for population j and vice‐versa (see Figure 1).
The weight wi,CTX is fixed but the weight wi,CS varies with time according to the following
learning rule

dwi,CS
dt

= αiCS CT Xi,

(4)

where αi is the learning rate. All parameters used in the simulations of the mean‐field
model are shown in Table 1.

Table 1. Parameters of the mean‐field model (Equations 1‐ 4) used in our simulations.

Rate model parameters
p
Steepness of Φ
θ
Maximum slope of Φ
ki
Maximum firing rate
ri
Refractoriness parameter
α
Learning rate
CS
CS input strength
CT XA,B
CT X input strength
wCTX
CT X synaptic weight
Initial CS synaptic weight
wCS
Population coupling synaptic weight wij

1.2 s
2.8 Hz
0.97 Hz
10−3
0.15 s
0.5
0.3
1.0
1.0
−1.0

Figure 1. Schematic representation of the mean‐field model. Populations A and B are mutually
synaptically connected. The two populations receive the same CS input (short pulses), and population A receives a CT XA continuous input and population B receives a CT XB continuous input.
The colored time axis indicates when each of such stimuli is active. Excitatory connections are
represented by arrows and inhibitory ones by circles. This figure corresponds to Figure 2A from
the original work, in which we added a timeline representing when each stimulus is activated.

Spiking network model

Neurons of the spiking network model were described by the leaky‐integrate‐and‐fire
(LIF) model. The subthreshold dynamics of neuron i is given by


=

Gl

E0 − vi

(cid:1)


+ Gi

exc

Eexc − vi

(cid:1)


+ Gi

inh

Einh − vi

(cid:1)(cid:1)

/Cm,

(5)

dvi
dt

where vi is the membrane potential, Gl is the membrane (leakage) conductance, Gexc is
the total excitatory synaptic conductance, Ginh is the total inhibitory synaptic conductance, E0 is the resting potential, Eexc is the reversal potential of the excitatory synapse,




Einh is the reversal potential of the inhibitory synapse, and Cm is the membrane capacitance [6]. When vi(t) ≥ θ, where θ is the spike threshold, the neuron emits a spike and
the voltage is reset to Ek and remains fixed at this value for a refractory period τref . The
parameters of the neuron model in Equation 5 are given in Table 2. In the simulations,
the initial conditions of the voltages v of all neurons were drawn from a normal distribution with mean E0 and standard deviation 3.0 mV. Note that Equation 5 shown here
is different from Equation 5 in the original work, since it is dimensionally incompatible. More details about this choice can be seen in the section “Important information
needed during replication”.

Table 2. Parameters of the spiking neuron model (Equation 5) used in our simulations (extracted
from [6]).

Spiking neuron parameters
Gl
E0
Ek

Membrane conductance
Resting potential
Reset voltage
Excitatory synaptic reversal potential Eexc
Inhibitory synaptic reversal potential Einh
Membrane capacitance
Spike threshold
Refractory period

Cm
θ
τref

16.7 nS
‐70.0 mV
‐70.0 mV
0.0 mV
‐80.0 mV
250.0 pF
‐50.0 mV
2.0 ms

The network is composed of 4,000 neurons, of which NE = 3, 400 are excitatory and
NI = 600 are inhibitory. The neurons are randomly connected with probabilities that
depend on the types (exc or inh) of the pre‐ and postsynaptic cells. Synapses from a
neuron onto itself (autapses) are allowed. The connection probabilities are given in
Table 3.

Table 3. Probabilities of the four types of connections between neurons and their respective synaptic weights. The synaptic weights are drawn from normal distributions with mean µ and standard
deviation σ [2] as indicated in the table.

Connection type
Excitatory to excitatory
Excitatory to inhibitory
Inhibitory to excitatory
Inhibitory to inhibitory

Probability
pEE
0.01
pIE
0.15
pEI
0.15
pII
0.10

Synaptic weights

µ = 1.25 nS
µ = 1.25 nS
µ = 2.50 nS
µ = 2.50 nS


The synaptic conductances obey the equations

dG
dt
dGaux
dt

,

= Gaux − G
τr
= − Gaux
+ W δ(t − t′ − D),
τd

(6)

(7)

where G is used to represent either Gexc or Ginh, Gaux is an auxiliary variable, and τr
and τd are the rise and the decay time constants, respectively. We will use τr = τd =
0.326 ms [6], so that G is an alpha function.
In Equation 7, W is the synaptic weight added to the variable Gaux at time t due to a
spike in the presynaptic neuron at time t′, and D is the transmission delay from pre‐ to
postsynaptic neuron. The value of D is drawn from a normal distribution with mean
µ = 2 ms and standard deviation σ = 0.1 ms. The value of the synaptic weight W
depends on the type of synapse and is indicated in Table 3.




Table 4. Parameters (rates of Poisson processes and synaptic weights) and types of synaptic inputs
applied to the network neurons. The weights of all BKG and CS to IN H (inhibitory neurons)
inputs are fixed, while the weights of the CS to EXC (excitatory neurons) and CT X inputs are
plastic and have their initial values drawn from normal distributions with parameters (mean µ
and standard deviation σ) indicated in the table.

Inputs parameters

Connection
BKG to EXC
BKG to IN H
CS to IN H
CS to EXC

Type
Static
Static
Static
Plastic
CT X to subpop. A/B Plastic

Weight
Rate
1.25 nS
5 Hz
1.25 nS
6 Hz
µ = 0.9 nS, 
500 Hz
µ = 0.9 nS, 
500 Hz
300 Hz µ = 0.4 nS, σ = 0.05 nS

Spiking network inputs

Besides recurrent connections from other network neurons, each neuron of the spiking
network model receives three kinds of input: background (BKG), consisting of 1,000
inputs per neuron representing external synapses received from neurons in other brain
areas; conditioned stimulus (CS), consisting of short pulses of 50 ms of duration; and
contextual input (CT X). All these inputs are modeled as excitatory synapses activated
by independent Poisson processes with specific rates.
The rates of the BKG inputs to excitatory and inhibitory neurons are distinct. These
rates were adjusted so that the baseline network spiking activity was lower than 1 Hz
for excitatory neurons and between 10‐15 Hz for inhibitory neurons, as observed experimentally [7]. The rates of the CS and CT X inputs are the same for all neurons. The
input rates and their respective synaptic weights are shown in Table 4.
To model conditioning and extinction of fear memories in the BA, two subpopulations
of excitatory neurons containing 20% of NE, i.e. 680 neurons, were chosen without overlap. The first subpopulation (popA) represents the fear neurons which receive contextA
input (CT XA), and the second (popB) represents the extinction neurons which receive
contextB input (CT XB).
Figure 2 shows all the inputs described above with emphasis on subpopulations A and
B that are formed exclusively by excitatory neurons. The first stage of the simulation
represents the conditioning phase in which CT XA and CS are activated (CT XB is deactivated), and the second stage represents the extinction phase, in which CT XB and
CS are activated (CT XA is deactivated).




Figure 2. Schematic diagram of the spiking network model. Excitatory and inhibitory populations
are represented by rectangles with the two excitatory subpopulations (A and B) that receive CT X
inputs highlighted as colored circles. The excitatory and inhibitory populations receive BKG
and CS (short pulses) inputs and the subpopulations A and B receive aditional CT XA and CT XB
inputs, respectively. The colored time axis indicates when CT XA and CT XB inputs are active.
Excitatory connections are represented by arrows and inhibitory ones by circles. This figure corresponds to Figure 2B of the original work, and a timeline representing when each stimulus is
activated was added.

Plasticity

The synaptic weights of all network connections are static, except the ones of the connections from the CS and CT X inputs to the excitatory neurons, which are modified
according to the following phenomenological rule:

(

w+ =

w− + α1 · h · m · c · |wmax − w−|
w− − α2 · m · c · |wmin − w−|

if CS and CT X temporally overlap
otherwise,

(8)

where w− is the synaptic weight before the update, w+ is the synaptic weight after the
update, α1 and α2 are the learning rates, wmax (wmim) is the maximum (minimum) value
of the synaptic weight, m is a binary number that represents the action of a neuromodulator, and c and h are auxiliary variables that encode the recent activity in the synapse
that receives input from CS and CT X, respectively.
The overlap described in Equation 8 refers to when there is a temporal superposition of
CS and CT X inputs for the same neuron on a time window of up to 100 ms. If the temporal overlap occurs, the synapses that connect the CS and CT X to the target neuron
are strengthened; otherwise, both synapses are weakened.
The dynamics of the variables c and h are described by

˙c = − c
τc
˙h = − h
τh

+ cu · δ(t − tpre−CS)

+ hu · δ(t − tpre−CT X ),

(9)

(10)

where τc and τh are time constants and cu (hu) is an increase in variable the c (h) when a
spike is emitted by the CS (CT X) source at t = tpre. The values of the parameters used
to model synaptic plasticity are shown in Table 5.




Table 5. Synaptic plasticity parameters

Synaptic plasticity

α1, α2
m

Learning rates
Neuromodulator present/absent
Maximum value of synaptic weight wmax
wmin
Mininum value of synaptic weight
τc
Time constant for variable c
Time constant for variable h
τh
Increment to variable c
cu
Increment to variable h
hu

1.6 × 10−3
0 or 1
4.0 nS
0.4 nS
10 ms
10 ms
0.35
0.35

Simulation protocols

In this section we define the protocols used for the simulations of the spiking network
model. In all cases described below, the BGK input is always active.

Spontaneous Activity — The network was simulated only with the BKG input during 1 second to evaluate the spontaneous activity generated by the model.

Dynamics of conditioning and extinction processes — After 50 ms of initial transient period, the
conditioning phase begins with the activation of the input CT XA and the application of
5 CS pulses (50 ms each) intercalated at intervals of 150 ms. After CT XA is turned off,
a transient period of 100 ms follows and the same protocol is repeated for CT XB but
with 6 CS pulses instead of 5.
During each presentation of CS (both in the conditioning phase and in the extinction
phase), the variable m in Equation 8 takes the value 1, and otherwise the value 0. Thus,
the synaptic weights CS and CT X vary during the simulation due to synaptic plasticity,
starting with the initial values given in Table 4.

Fear renewal — The fear renewal stage starts by repeating the previous protocol followed
by the reactivation of CT XA at the end of the extinction phase, together with a single
presentation of the CS.

High connectivity introduces gamma oscillations — In this protocol the pii (see Table 3) is increased from 0.1 to 0.5 and only the conditioning phase is activated with the application
of 10 CS pulses.

Blockage of inhibition — This protocol follows the same procedure described in Dynamics
of conditioning and extinction processes, but two different conditions are simulated: either
50% or 90% of inhibitory neurons are deactivated during the extinction phase.

Measures

In this section we show how the measures used in our replication of the original study
are defined:

• Throughout the simulation, we recorded the firing times for the construction of

raster plots of neuronal activity.

• During CS presentations to popA and popB, we counted the total number of spikes
in each subpopulation and divided it by the CS duration (50 ms) to calculate the
average firing rate.




• We recorded the time series of CS and CT X synaptic strengths to popA and popB
throughout the simulations. With that, we calculated the averages of these weights
separately during each presentation of CS.

• The population spiking activity is the average spike count within a time window

∆t = 1 ms, unless otherwise stated.

• We estimated the power spectrum density (P SD) of the population spiking activity

using the Welch’s method (from python package SciPy).

• The synchrony index was calculated as the variance of the population spiking activity divided by its mean. This measure is a simplification of the normalized synchrony index introduced by Golomb and Rinzel [8, 9].

Important information needed during replication

The general information necessary for the replication done here was available in the
original article. However, some details were not found neither in the reference paper
nor in the supplementary material. Here we list these details and describe the considerations we made to replicate the results.

Missing parameter values —

• Almost every parameter for the mean‐field model is not present in the original

work, namely the strength of the CS and CT X inputs, wij, and wCTX.

• The values of the spiking neuron parameters τm, E0, Eexc, Einh, θ and EK in Equation 5 are said to be given in Table S1F of the supplementary material of the reference [2] paper. However, the only parameter value given in Table S1F is the one
of τref . The value of θ is given in the caption of Figure 5 as −57 mV and the other
are missing. Furthermore, the initial value of v is not mentioned.

• The synapse model used is defined in the main text only as a conductance‐based
synapse with no mention to the conductance dynamics. Looking at the supplementary material, we found that the conductance time‐course was described by a
difference of exponentials. The equation is described in Table S1G [2] but is not
cited in the main text. Nevertheless, the values of the parameters τr, τd and tpeak
are not given.

• Some parameters are also not given in the main text for the synaptic plasticity
model described by equations 6‐8. These parameters are: wmax, wmin, A, B, τc
and τh. Moreover, but less important, parameters α1 and α2 are written in Table
S1H as a1 and a2.

• Table S1I from the supplementary material [2] defines BKG current injections to
excitatory and inhibitory neurons) with DC and AC amplitude values. However,
there is no information about the frequency or phase for the AC currents.

• In Figures 5, 7, and 8 of the original work [2], the authors used spike activity histograms to obtain the firing rate time series that characterize the population activity. However, the bin sizes used are different and not informed.

• The High connectivity introduces gamma oscillations protocol adopted in the original article was not clear if only the conditioning phase was considered, and the
number of CS presentations was not specified.




Approximations done to replicate the results —

• In the mean‐field model we considered the inputs CS and CT XA/B as square
pulses with the same heights as used for the spiking network model (500 and
300 Hz, respectively), but we divided them by 1000 so that they remain below 1.
We considered the synaptic weights as unitary, i.e., wi,CS = wi,CT X = −wij = 1.

• The neuron model equation used in the original text (Equation 5 of [2]) has a dimensional inconsistency. By reviewing the references cited by the authors, we found
our Equation 5 in reference [6], which describes the same neuronal dynamics. We
adopted this equation here with the same parameters given in [6] and shown in
Table 2.

• The description of the synaptic model was also extracted from reference [6], where
the synaptic conductances are given by a difference of exponentials with τr = τd =
0.326 ms. To implement the difference of exponentials in Brian 2, it was necessary
to use two ordinary differential equations as shown in Equations 6 and 7.

• Due to the lack of details on the application of AC and DC currents to model the
BKG input, we opted for the use of Poisson train generators (Table 4), which
promoted a spontaneous activity compatible with what was experimentally expected [7].

• To replicate the results obtained in the evolution of synaptic weights, we used the
values of CS and CT X shown in Table 4, which differ from those described in the
supplementary material of the reference article [2].

• In Equations 9 and 10, we named the parameters cu and hu instead of A and B as in
the reference article [2] to avoid misunderstandings in relation to subpopulations
A and B. We also specified in these equations tpre−CS and tpre−CT X , which indicate
when increments in auxiliary variables occur.

• In assessing how the increase in network connectivity introduces gamma oscillations, the authors did not clearly show how the frequency of population activity
and the synchrony index were determined. In our replication, we used P SD to
check the frequency of oscillations in the spiking activity of the network and chose
population Fano Factor as the synchrony index.

• In Figure 9, we used 10 CS presentations which was the minimum number of

presentation necessary to reproduce the original result.

Results

In this section, we present the results obtained from our simulations as described in
Methods, which qualitatively reproduce the main results of the reference article.

Mean-field model

Despite the lack of information provided by the authors for this model, we have reproduced qualitatively the expected dynamics for the conditioning and extinction phases
as shown in Figure 3A.
The external inputs CS and CT X were generated beforehand for the whole simulation
time (Figure 3C). Therefore, we studied the evolution of the synaptic weights wA/B,CS
by simply using the stimuli arrays and Equation 4 without simultaneously simulating
the inputs. The synaptic weights evolution in Figure 3B is in accordance with what was
reported in the reference paper (Figures 4C‐D of [2]).




Figure 3. Dynamics of the mean‐field model.(A) Firing rates of popA and popB at each CS application. The vertical red dashed line marks the transition from application of CT XA to CT XB.
(B) Time evolution of wA,CS, and wB,CS. (C) Time evolution of the external inputs CS, CT XA,
CT XB. This figure is equivalent to Figure 4 of the original work, in which we additionally show
the temporal evolution of external inputs.

Spiking neuron network model of BA

Spontaneous Activity — In Figure 4 we show the raster plot of the simulated spontaneous
activity of the network. The firing rates measured were 0.03 and 10.54 Hz per neuron
for the excitatory and the inhibitory populations, respectively. This is compatible with
the firing rates observed experimentally [7]. This consistency test was not presented in
the original work.

Figure 4. Raster plot of network spiking activity when there is only background input as external stimulus. The red dots represent spikes from the inhibitory population and the black dots
represent spikes from the excitatory population. This figure is not present in the original work.

Dynamics of conditioning and extinction processes — In Figure 5A we show the raster plot
of spiking activity during the conditioning and extinction processes. The activities of
subpopulations A and B, which represent fear and extinction neurons, respectively, are




highlighted. After each presentation of CS during the conditioning phase, there is an
increase in the firing rate of popA. On the other hand, in the extinction phase, after the
first presentations of CS the popA firing rate gradually decreases while the firing rate of
popB increases (Figure 5B). During these phases, the activity of the inhibitory neurons
slightly fluctuated for each presentation of CS as shown in Figure 5C.

Figure 5. Dynamics of the spiking network model of BA. This figure should be compared to Figures 5A‐C of the reference paper. (A) Raster plot of simulated spiking network activity during the
conditioning and extinction phases. The amber and cyan dots represent popA and popB, respectively, while the red dots represent the inhibitory neuron population and the black dots represent
the other excitatory neurons. (B) Firing rate per neuron of popA and popB (same colors as in A).
(C) Firing rate per neuron of the inhibitory population. In (B) and (C) we used ∆t = 15 ms. The
loosely dashed horizontal lines symbolize the CS presentations during the simulation and the
vertical dashed line marks the transition from conditioning to extinction phase.

In the caption of Figure 5 of the reference article, the authors explain that popA and
popB, each one, corresponds to 50% of the total excitatory neurons. However, this is in
disagreement with the methodology presented by them. In our study, we considered
20% of the total excitatory neurons for each subpopulation as described in the original
methodology and shown in Figure 2.
We evaluated 30 simulations for the conditioning and extinction dynamics, and in all
of them it was possible to verify the same scenario presented in Figure 5. In general,
after each presentation of CS there is an increase in synaptic weights associated with
the CT X applied followed by a decay when this CT X is inactivated. Thus, the results
relative to the average firing rates and synaptic weights (Figure 6) are consistent as expected from the synaptic plasticity rules applied (Equation 8), and compatible with the
original study.




Figure 6. Figure to be compared to Figures 5E‐J of the reference paper. (A) Evolution of the firing
rates of popA and popB neurons during fear conditioning (left) and extinction (right). Firing rates
were evaluated over 30 simulations. (B) Evolution of synaptic weights of CS inputs to popA and
popB neurons during fear conditioning (left) and extinction (right). (C) Same as in (B) for the
synaptic weights of CT X inputs during CS presentations. Here we chose to maintain the same
acronym HPC used in the main reference, which refers to CT X.

Fear renewal — The results for these simulations are shown in Figures 7 and 8, and should
be compared to Figures 7A‐C and Figures 7E‐H of the reference paper, respectively. In
Figure 7A we show the spiking raster plot for the simulation, and in Figure 7B‐C the activities of the excitatory and inhibitory populations, respectively. During the transition
from the extinction to the renewal phase: i) the change of CT X causes a sudden modification in the firing rates of popA and popB neurons (Figures 7B and 8A); but ii) this
effect barely influences the CS and CT X synaptic weights due to the synaptic plasticity
rules (Figures 8B and 8C).
In accordance with the reference article, the rapid change in the activity of subpopulations is a network phenomenon and not an effect of synaptic plasticity, although it plays
an important role in the whole dynamics that precedes the renovation. Additionally, we
observed a slight change in CS and CT X weights in the transition from extinction to
renewal, which might be related to the difference between the time constants used in
our replication and the original model (this could indicate that our τh/c is slightly faster)
to simulate the synaptic plasticity.




Figure 7. ABA fear renewal. This scenario is equivalent to that shown in Figure 5 of the present
work (and is equivalent to Figure 7 of the original work), with the reactivation of CT XA and an
additional presentation of CS. (A) Raster plot of spiking activity of fear (amber), extinction (cyan),
inhibitory (red), and other excitatory (black) neurons. (B) Average firing rate of popA and popB
neurons. (C) Average firing rate of the inhibitory neurons. Dashed horizontal lines symbolize the
CS presentations during the simulation and dashed vertical lines mark the transitions between
conditioning and extinction and extinction and renewal. The exchange of CT X after the extinction phase causes an instantaneous change in activity between popA and popB neurons. In (B)
and (C) we used ∆t = 15 ms.




Figure 8. Figure to be compared to Figures 7E‐G of the reference paper. (A) Average firing rates of
popA and popB neurons during conditioning, extinction and renewal. Averages were performed
over 30 simulations of ABA renewal. (B) Synaptic weights of CS inputs to popA and popB neurons.
(C) Synaptic weights of CT X inputs during CS presentations. Here we chose to maintain the
same acronym HPC used in the reference article that refers to CT X. During renewal, the synaptic
weights undergo slight changes because of the synaptic plasticity rule applied. Despite a decline
in the synaptic weights of popA at the end of the extinction phase, these weights still have higher
values than at the beginning of the conditioning phase, thus when reactivating the CT XA, the
firing rate for popA increases sharply. Note that in Figure 7F of the original article the colors used
to indicated the populations are inverted.




High connectivity introduces gamma oscillations — In the corresponding section of the reference article, the connection probability pII (defined here in Table 3) was increased to
the experimentally reported value of 0.5 [10] to study the effect of this high connectivity
on the behavior of the spiking network model. The authors reported that this change
in the network did not affect the qualitative behavior of the model but a new aspect
emerged in the dynamics: gamma oscillations in the network firing rate.
With a careful inspection of Figure 8A of the main reference, we noted that the authors
studied this phenomenon only for the conditioning phase and, to obtain a similar result, we increase the amount of CS presentations to 10 (this result is dependent on the
number of CS presentations). The results for this procedure are shown in Figure 9.

Figure 9. Gamma oscillations for high network connectivity. (A) Raster plot of spiking activity for
the last 4 presentations of CS during the conditioning phase. Amber dots represent the fear neurons, red dots the inhibitory neurons, and black dots the other excitatory neurons. (B) Histogram
(smoothed) of population activity. During each presentation of CS (horizontal black lines), it is
possible to notice signatures of gamma oscillations. (C) Power spectrum density of the time series
in (B). The peak at 66.41 Hz (in the gamma band) is indicated by an arrow. This figure corresponds
to Figure 8A of the original work, in which we additionally show the detection of gamma oscillations (30‐80 Hz).

In Figure 9A, we show a raster plot of the spiking activity for the last four CS presentations. At each presentation the neurons fire in a more synchronous fashion as can be
seen in Figure 9B. The P SD of this synchronous activity is shown in Figure 9C and it displays a peak at 66.41 Hz, within the gamma oscillation range (30‐80 Hz). Thus, through
our approximation, we obtained a similar result to that observed in Figure 8A of the
original work.
Further, the authors investigated how the network properties impact the overall syn‐




chrony. To illustrate the meaning of the synchrony index used in this replication, in
Figure 10 we show time series of the synchrony index for three different types of activity
of the inhibitory population (obtained with different values of pII ). As gamma oscillations emerge, the synchrony index increases. In particular, we show that the oscillatory
power of the network is positively correlated with the synchrony index. Specifically for
this network the characteristic oscillations are always within the gamma band. We will
assume that a synchrony index greater than 4.5 characterizes the presence of gamma
oscillations.

Figure 10. Synchrony index and gamma oscillations. (A) Non‐synchronized case. (B) Synchronized case with emergence of gamma oscillations.
(C) Synchronized case with strong gamma
oscillations. The synchronization index shown above each plot was calculated using the activity
of the inhibitory population obtained with a histogram of bin size ∆t = 1 ms, delay distributed
uniformly between [1.0 − 2.0] for an inhibitory synaptic weight of 2 nS. The times series were
generated with three different values of connection probability among inhibitory neurons: (A)
pII = 0.1, (B) pII = 0.6, and (C) pII = 0.7. This figure is not present in the original work.

To explore mechanisms operating in BA that could dampen gamma oscillations, the authors of the original text investigated the measure of synchrony as a function of connectivity, synaptic weights and delays between inhibitory neurons. The pII connectivity
was analyzed from 0.1 to 0.9, at 0.1 intervals; synaptic weights wII were set to 1, 2 or
3 nS; and delays were divided in two groups: “higher”, uniformly distributed between
[1.0 − 2.0] ms, and “lower”, uniformly distributed between [0.2 − 1.0] ms.
Figure 11 shows the synchrony index for simulations with all possible combinations
of these three groups of parameters. Gamma oscillations are not present (regions bellow the purple dashed line in Figure 11) for both delay scenarios (“higher” and “lower”)
when one of the following conditions is true: (i) pII lower than 0.4, or (ii) wII = 1 nS
independently of pII . For delay type “lower”, there is a reduction of oscillations in all situations, which is compatible with the reference article. Thus, changes in the inhibitory
structure of the network are essential to obtain gamma oscillations in neuronal activity.




Figure 11. Effects of connectivity, synaptic weights and delays of the inhibitory population on
synchronization. The synchrony index used was the Fano factor calculated on the histogram of
inhibitory spikes during the presentation of the last four CS during the conditioning phase. The
combinations between synaptic weights and delays are indicated by different colors (gray, light
green and dark green) and line types (continuous or dashed) as indicated on the left‐hand top
corner. The purple dashed line indicates the threshold value 4.5 above which the synchrony index
indicates gamma oscillations according to our definition. This figure corresponds to Figure 8B of
the original work.

Blockage of inhibition — Inhibition plays an important role in controlling the firing rate of
the network as can be seen in Figure 5A, in which the firing rate of excitatory neurons
not belonging to subpopulations A and B (black dots) remains close to zero even with
presentations of CS. Based on this, we performed two additional sets of simulations
where we deactivated first 50% and then 90% of inhibitory neurons during the extinction
phase.




Figure 12. Blockage of 90% inhibitory activity during the extinction phase. The raster plot corresponds to the same situation (with the same color code) shown in Figure 5 with the difference that
in the extinction phase we set to zero the synaptic weights for 90% of the inhibitory population.
Although in our simulation these neurons fire, they do not affect other neurons. This figure is not
present in the original work.

In Figure 12, we show the raster plot of spiking neuronal activity for 90% of inhibitory
blockage. The firing rates of all excitatory neurons are abruptly increased when inhibitory neurons are deactivated during CT XB presentation. To highlight this effect,
in Figure 13 we show the firing rate during the last CS presentation (corresponding to
Figure 8C of the original paper). As expected, the increase in the fraction of “blocked”
inhibitory cells provokes an increase in the firing rate, and this effect is even stronger
for the extinction neurons (popB). This suggests that if the relative difference between
the activities of the fear and extinction neurons were crucial, extinction must be favored
by the blockage of inhibition in this scenario.

Figure 13. Blockage of inhibitory neurons during the extinction phase leads to an increase in
the firing rates of popA (fear neurons, amber) and popB (extinction neurons, cyan). The relative
difference between the firing rates also increases. This figure corresponds to Figure 8C of the
original work.




Conclusions

We replicated two models proposed by Vlachos et al. (2011) [2] to study aspects related to
fear and extinction memories in the BA. These phenomena depend on the activation of
two subpopulations of neurons for different context stimuli. The models were originally
built in NEST and Matlab and here we reimplemented them using Python and Brian 2.
Due to lack of some parameter values, data analysis details, and simulation protocols
in the original article, we had to make some adaptations and successfully replicated the
following results:

• for the mean‐field model, the obtained result qualitatively replicates the original

result.

• for the spiking network model, the results obtained are qualitatively consistent
with the original work. In addition, we added descriptions and extra figures that
help to understand all the methodological procedures adopted.

Even though we did not replicate all results of the original paper, the qualitative replication described here suffices to give support to the claim of the authors of the original
article that their model captures the experimental observations.

Acknowledgements

This replication work started as a student project during the VIII Latin American School
on Computational Neuroscience (LASCON 2020).
This article was produced as part of the activities of FAPESP Research, Innovation and
Dissemination Center for Neuromathematics (Grant No. 2013/07699‐0, S. Paulo Research
Foundation). T.T.A.C. is supported by a scholarship from the National Council of Scientific and Technological Development (CNPq) (Grant No. 141579/2017‐0) and Fundação de
Amparo à Ciência e Tecnologia de Pernambuco (FACEPE) (Grant No. BFD‐0013‐1.05/20).
The authors also thank FAPESP support through Grants Nos. 2015/50122‐0, 2018/202770 (A.C.R.), 2016/03855‐5 (N.L.K.) and 2017/07688‐9 (R.O.S). V.L.C received a CAPES PhD
scholarship and L.B.D a Capes MSc scholarship. A.C.R. thanks financial support from
CNPq (Grant No. 306251/2014‐0). This study was financed in part by the Coordenação
de Aperfeiçoamento de Pessoal de Nível Superior ‐ Brasil (CAPES) ‐ Finance Code 001.

References

1.

2.

C. Herry, S. Ciocchi, V. Senn, L. Demmou, C. Müller, and A. Lüthi. “Switching on and off fear by distinct neuronal
circuits.” In: Nature 454 (2008), pp. 600–606.
I. Vlachos, C. Herry, A. Lüthi, A. Aertsen, and A. Kumar. “Context-dependent encoding of fear and extinction
memories in a large-scale network model of the basal amygdala.” In: PLoS Comput. Biol. 7 (2011), e1001104.

3. M.-O. Gewaltig and M. Diesmann. “NEST (NEural Simulation Tool).” In: Scholarpedia 2.4 (2007), p. 1430.
4. M. Stimberg, R. Brette, and D. F. Goodman. “Brian 2, an intuitive and efficient neural simulator.” In: eLife 8 (Aug.

2019).

5. H. R. Wilson and J. D. Cowan. “Excitatory and inhibitory interactions in localized populations of model neurons.”

6.

7.

8.

9.
10.

In: Biophys. J. 12 (1972), pp. 1–24.
A. Kumar, S. Schrader, A. Aertsen, and S. Rotter. “The high-conductance state of cortical networks.” In: Neural
Comput 20 (2008), pp. 1–43.
P. Sah, E. S. L. Faber, M. Lopez de Armentia, and J. M. J. P. R. Power. “The amygdaloid complex: anatomy and
physiology.” In: Physiol. Rev. 83 (2003), pp. 803–834.
D. Golomb and J. Rinzel. “Dynamics of globally coupled inhibitory neurons with heterogeneity.” In: Phys. Rev.
E 48 (1993), pp. 4810–4814.
D. Golomb. “Neuronal synchrony measures.” In: Scholarpedia 2.1 (2007), p. 1347.
A. R. Woodruff and P. Sah. “Networks of parvalbumin-positive interneurons in the basolateral amygdala.” In: J.
Neurosci. 27 (2007), pp. 553–563.

---
**Source PDF:** `2021_27_article.pdf`
