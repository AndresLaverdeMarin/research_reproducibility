Non-Additive Coupling Enables Propagation of
Synchronous Spiking Activity in Purely Random
Networks

Raoul-Martin Memmesheimer1*, Marc Timme2

## 1 Department for Neuroinformatics, Radboud University Nijmegen, Nijmegen, Netherlands, 2 Network Dynamics Group, Max Planck Institute for Dynamics & Self-
Organization, and Bernstein Center for Computational Neuroscience, Go¨ ttingen, Germany

Abstract

Despite the current debate about the computational role of experimentally observed precise spike patterns it is still
theoretically unclear under which conditions and how they may emerge in neural circuits. Here, we study spiking neural
networks with non-additive dendritic interactions that were recently uncovered in single-neuron experiments. We show
that supra-additive dendritic interactions enable the persistent propagation of synchronous activity already in purely
random networks without superimposed structures and explain the mechanism underlying it. This study adds a novel
perspective on the dynamics of networks with nonlinear interactions in general and presents a new viable mechanism for
the occurrence of patterns of precisely timed spikes in recurrent networks.

Citation: Memmesheimer R-M, Timme M (2012) Non-Additive Coupling Enables Propagation of Synchronous Spiking Activity in Purely Random Networks. PLoS
Comput Biol 8(4): e1002384. doi:10.1371/journal.pcbi.1002384

Editor: Lyle J. Graham, Universite´ Paris Descartes, Centre National de la Recherche Scientifique, France

Received July 14, 2011; Accepted December 29, 2011; Published April 19, 2012

Copyright: (cid:2) 2012 Memmesheimer, Timme. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which
permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Funding: This work was supported by the Federal Ministry of Education and Research (BMBF), Germany, grant number 01GQ105B, and the Max Planck Society.
The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing Interests: The authors have declared that no competing interests exist.

* E-mail: r.memmesheimer@science.ru.nl

Introduction

Patterns of spikes that are precisely timed within the millisecond
range have been investigated and observed in a series of neuro-
physiological studies [1–9]. This supports the ongoing debate
whether cortical neurons are capable of precisely coordinating the
timing of their action potentials across recurrent networks and
whether only the neurons’ firing rate or also the precise timing of
their spikes encode key information that is intimately related to
external stimuli and internal events [2,3,10–14].

During the last two decades, a branch of theoretical research has
focused on the question how such precise timing could emerge. One
prominent, possible explanation for the occurrence of precisely
coordinated spiking is the existence of excitatorily coupled feed-
forward structures, ‘synfire-chains’, which are superimposed on a
network of otherwise random connectivity, e.g. through strongly
enhanced synaptic connectivity [10,15–18]. Under certain condi-
tions, these additional feed-forward structures enable the persistent
propagation of groups of spiking activity that is synchronous on a
time scale of down to one millisecond [17,19–24]. So far, however,
experimental research did not provide anatomical evidence for such
structures. Other studies proposed that asynchronous propagation
along paths with matching inhomogeneous delays [25] or the
dynamics of
local recurrent networks [26,27] might underlie
precisely timed spike patterns.

Here we show that nonlinear dendritic interactions, recently
uncovered in neurophysiological experiments, offer a viable
mechanism to support stable propagation of synchrony through
random cortical circuits without additionally superimposed struc-
tures: Excitatory synaptic stimuli may not only superimpose linearly

or sublinearly [28,29], but may also induce strongly nonlinear,
supra-additive coupling enhancement due to dendritic spikes [30–
32]. Fast dendritic sodium spikes strongly enhance the effects of
stimulus-evoked post-synaptic potentials in a supra-additive way
and induce precisely timed and sharply peaked depolarizations in
the somatic membrane potential. Remarkably, this enhancement
occurs reliably only if the stimuli are synchronous in time with
temporal difference of less than 1{3ms [33–36], cf. also [37]. If the
resulting depolarization triggers an action potential, it is highly
precise in time up to less than 0:2 ms [33–35]. Other types of much
slower dendritic spikes are mediated by voltage gated Ca2z or
NMDA channels. They have longer time courses up to several
hundreds of milliseconds and do not depend on synchronous
stimulation (see, e.g., [38,39], and, for reviews, [32,40]).

In the following, we study consequences of coupling nonlinearities
that are due to fast dendritic spikes onto the collective dynamics of
recurrent neural networks. We find that, in contrast to linearly
coupled networks, propagating synchronous activity may persist
already in networks of simple neurons that have purely random
connectivity and exhibit no additional structures. We conclude that
the characteristic features of dendritic nonlinearity, in particular the
amplification of
(only) synchronous input and the induction of
temporally precise output, predestine them to support the generation
and propagation of persistent, highly synchronous spiking activity.

Results

Neurons coupled via nonlinear dendrites

We investigate networks of integrate-and-fire neurons in the
fast response to incoming spikes and with nonlinear

limit of


Author Summary

to the neuronal

Most nerve cells in neural circuits communicate by sending
and receiving short stereotyped electrical pulses called
action potentials or spikes. Recent neurophysiological
experiments found that under certain conditions the
neuronal dendrites (branched projections of the neuron
that transmit inputs from other neurons to the cell body
(soma)) process input spikes in a nonlinear way:
If the
inputs arrive within a time window of a few milliseconds,
the dendrite can actively generate a dendritic spike that
propagates
to a
nonlinearly amplified response. This response is temporally
highly precise. Here we consider an analytically tractable
model of spiking neural circuits and study the impact of
such dendritic nonlinearities on network activity. We find
that synchronous spiking activity may robustly propagate
through the network, even if it exhibits purely random
connectivity without additionally superimposed structures.
Such propagation may contribute to the generation of
spike patterns that are currently discussed to encode
information about internal states and external stimuli in
neural circuits.

soma and leads

interactions (see Methods). Similar models with linear interactions
are widely used for studying the dynamics of networks of spiking
neurons (see, e.g., [16,41–43], [44,45] for recent reviews) because
they capture essential features of cortical neurons and at the same
time allow to investigate the mechanisms underlying the dynamics
of networks without obscuring them by a many-parameter, many-
variable single neuron description (see, e.g., [44,46–48]). In this
study they allow to interpret the dynamical regimes of the network
activity qualitatively and to analytically assess them quantitatively.
We assume that the delay t between sending of a spike by a
presynaptic neuron and postsynaptic (somatic) response is identical
for all neurons. This is appropriate for the description of responses
mediated by fast dendritic spikes because these evoke a fast and
precise rise with sub-millisecond rise time constant in the somatic
potential [33,36]. Moreover,
is
generated by fast dendritic spikes as observed in [33], this occurs
t~5ms after presynaptic axonal
stimulation with only sub-
millisecond inter- and intra-neuronal
jitter, while the action
potential timing strongly varies in time if no dendritic spike is
elicited. This is well resembled by our model dynamics where
nonlinearly enhanced inputs yield fast, jump-like responses in the
membrane potential and firing due to supra-threshold excitation
occurs precisely after the delay time t. For simplicity, we further
assume that all postsynaptic responses to spikes occur after this
delay time.
‘Imprecise’ spiking is generated due to a constant
supra-threshold input current.

if a somatic action potential

To account

for nonlinear enhancement and saturation of
synchronous excitatory inputs, we modulate the linear sum of the
amplitudes of excitatory post-synaptic potentials (EPSPs) that arise
simultaneously from different synapses by a nonlinear function s.
This covers the main features of experimentally found nonlinear
dendritic amplification (cf. [33,36,38–40]), thus effectively modeling
a neuron with one, nonlinear dendrite. For the neuron model
considered, s has a straightforward interpretation: It maps the peak
EPSP amplitude e expected from linearly adding the coupling
strengths of synchronously received excitatory signals to the actual
value s(e) (cf. Fig. 1b). Such a modulation function has been directly
[39] and indirectly [33] measured in experiments. It has a sigmoid
shape, with linear summation for small summed amplitudes e and
saturation at high e. We thus model the non-additive coupling using


a function s that is the identity s(e)~e at low values eƒVa, has a
constant saturation s(e)~Vc at high values e§Vb, and linearly
in between, cf. Fig. 1b. Inhibitory post-synaptic
interpolates
potentials (IPSPs) at
the same neuron are linearly summed,
independent on whether or not the synaptic signals are simulta-
neous, because there is no experimental evidence for supra-linear
enhancement. If s is the identity function (Fig. 1a), the same holds
for excitatory coupling and we recover a ‘‘conventional’’ network of
linearly coupled neurons.

Propagation of synchrony

irregular

In both additively and non-additively coupled sparse random
spiking activity
recurrent networks, asynchronous
constitutes a dynamical
for a wide range of
state typical
parameters [42,43,49,50]. Sequences of groups of synchronously
spiking neurons may spontaneously occur starting with a single
neuron, or they can be initiated by a group of neurons that was
excited to synchronous spiking by external input. If a single neuron
or a group of neurons send spikes at one given time, a subset of
neurons in the network will receive a synchronous pulse of spikes a
delay time t thereafter. All neurons for which the induced
postsynaptic response leads to a supra-threshold depolarization in
turn spike simultaneously so that another synchronous pulse of
spikes is generated which can excite a further group of neurons
and so on. Spontaneous chains are part of the background activity.
They usually involve only small numbers of synchronously spiking
neurons and quickly extinguish, cf. supporting Fig. S1.

How does a sparse random network respond to induced
synchronous activity,
initiated, e.g., by external stimuli? We
compared the responses in networks with purely linear, additive
coupling to those where the excitatory inputs cooperate supra-
additively. For linearly coupled networks we find that pulse sizes in
chains of synchronous spiking activity quickly reduce to the level of
spontaneous synchronization and the chains rapidly die out (cf.
Fig. 2a). Propagation of synchrony is therefore short-lived in
studies
linearly coupled networks, consistent with previous
[16,17,51]. In contrast, for nonlinearly coupled networks, in a
wide range of parameters (cf. Fig. 3), a chain initiated by a large
enough, but not too large synchronous group after a few steps
fluctuate around some typical value,
reaches pulse-sizes that
Fig. 2b. These sizes are substantially larger than the sizes of
synchronous pulses occurring in the background activity (cf. Fig.
S1b), which persists while synchrony is propagating on top of it.
Only if the initial group size is too large, the chain of synchronous
activity is again short-lived. Taken together, we find persistent
propagation of synchrony in non-linearly coupled networks.

the network size (red coloring if

Persistent propagation of synchrony is robust against parameter
changes. We estimate a range of coupling strengths where persistent
propagation of synchrony occurs in linearly and in nonlinearly
coupled networks in Fig. 3. Background activity is here considered
stable if it contains at no time any synchronous pulse of more than
10% of
it became unstable
spontaneously, i.e. before initiation of synchronous activity, yellow
coloring if it became unstable thereafter, cf. also supporting Fig. S1).
Propagation of synchrony is considered persistent if background
activity is stable and if at least m~10 synchronized groups within
the chain are distinguishable from background activity, i.e. the
0, 0ƒiƒm, is larger than the largest group size
minimal group size gi
stable
occurring in background activity (green coloring for
background activity but short-lived propagation of synchrony, blue
coloring for stable background activity and persistent propagation of
synchrony). In nonlinearly coupled networks, propagation of
synchrony is persistent in a wide range of parameters, while it is
usually short-lived in linearly coupled networks.




Figure 1. Dendritic modulation function for (a) additive and (b) non-additive coupling. The modulation function maps the somatic peak
EPSP expected from linear summation of inputs to the actual peak EPSP strength. In networks with additively coupled neurons (a), the modulation
function is the identity.
In networks with nonlinear dendritic enhancement of inputs (b), the modulation function is sigmoidal as found in
physiological experiments. Supra-additivity sets in when the expected (linearly added) input strength reaches a threshold Va; at some strength Vb
the response saturates at a level Vc.
doi:10.1371/journal.pcbi.1002384.g001

Figure 2. Non-additive coupling enables persistent propagation of synchronous spiking. The figure illustrates the temporal evolution of
propagating synchrony as typical for large ranges of parameters in conventional networks (a,b,c) and in networks incorporating nonlinear dendritic
interactions (d,e,f). Panels (c,f) show the spiking activity of the first 200 neurons in a network of N~1000 neurons versus time. A chain of synchronous
pulses is initiated by applying external supra-threshold inputs to the first 100 neurons at time t0~150ms (red colored spikes, grey vertical lines
indicate times where spikes occur as part of the chain). Panels (a,d) show the total size g’ of synchronized groups within the chain. In the linearly
coupled network, the chain of synchronous activity extinguishes after a few steps. In the network with nonlinear dendritic integration, synchronized
spiking activity propagates persistently. The presence of large synchronous pulses is reflected in the network rate, see panels (b,e) (rate in kHz, bin
size 1ms).
doi:10.1371/journal.pcbi.1002384.g002




Figure 3. While propagation of synchrony is usually short-lived in linearly coupled networks (a), it is persistent for a wide range of
coupling parameters if the neurons are nonlinearly coupled (b,c). The parameter scans illustrate this by varying the mean total input
strengths (cid:2)eeEx,ges,(cid:2)eeIn,ges of the excitatory and the inhibitory input in a network of N~1000 neurons with 30% connectivity. For each combination,
synchronous activity was initiated with 100 neurons (a,b) or 75 neurons (c) and the stability of the temporal evolution was assessed. Blue coloring
indicates stable propagation of synchrony, red and yellow coloring refers to unstable background activity before and after onset of propagation, and
green coloring indicates unstable propagation (see Methods for details). White squres in (a) and (b) indicate the coupling strengths employed in
Fig. 2a) and b), respectively. The large blue areas in the scans for nonlinearly coupled networks indicate that propagation of synchrony is stable in a
wide range of parameters for such networks. This area is absent for linearly coupled networks as shown in (a), for smaller initial pulse sizes (e.g. 75
neurons) the number of successful trials is even smaller. In nonlinearly coupled networks with larger coupling strengths, an initial pulse size of 100
neurons can be larger than the upper bound of the propagation zone so that the chain is unstable (b) while for the same coupling parameters an
initial pulse of size 75 neurons starts a stable chain (c). For smaller coupling strengths, an initial pulse size of 75 neurons can be insufficient to initiate
stable propagation in contrast to a pulse of size 100 neurons.
doi:10.1371/journal.pcbi.1002384.g003

The mechanisms underlying this persistent propagation of
synchrony can be intuitively understood. Sequences with small
groups of synchronized neurons behave as for linear, additive
coupling, i.e. they usually extinguish after a few steps, so there is no
persistent spontaneous propagation and irregular background
dynamics for the entire network is stable. If larger groups of
neurons send spikes simultaneously, their postsynaptic neurons
receive sufficiently many excitatory inputs so that the nonlinea-
rities become effective. Since the inhibitory couplings add only
linearly, excitatory input surpasses inhibitory input for a larger
than in a linearly coupled
fraction of postsynaptic neurons
network. This causes more neurons to fire in response to the
synchronous pulse; the number of neurons synchronized in each
step of the chain grows. If synchronous pulses become too large,
saturation becomes important and excitation becomes less efficient
compared to inhibition. Further, many neurons are refractory.
This implies that less neurons are excited in response to overly
large groups of synchronously spiking neurons; consequently the
group size is reduced. In addition, fluctuations in groups sizes
occur due to the randomness of the network connectivity and the
distribution of membrane potentials during pulse reception. These
qualitative mechanisms keep the group sizes substantially large
and fluctuating within a certain range.

Quantitative analysis of the non-propagating and the
propagating state

To quantitatively understand the mechanisms underlying
persistent propagation of synchrony and to determine the group
sizes which initiate and take part in persistent propagation, we
studied the evolution of propagating synchrony both analytically
and numerically (see Methods and Fig. 4). Approximating the
dynamics of group sizes by a Markov process, we derived the
transition probabilities P(giz1Dgi) for the transitions from the sizes
of the ith pulse to those of the (iz1)th. Here gi,giz1, i[N, are


of
Dgi~gi

neurons
0)
is

the
the probability that

random variables that assume values in f0,1,:::,Ng, where N is
network. Accordingly,
the
in
number
P(giz1~giz1
the ith pulse
0 simultaneously spiking neurons causes a group
generated by gi
of giz1
neurons to spike simultaneously in response. From the
conditional (transition) probabilities, we derived the conditional
expectation E(giz1Dgi~gi
0),
the average size of a pulse
i.e.
0. Since the distributions P(giz1Dgi) are
following a pulse of size gi
similar to P(g1Dg0) also for later stages i§1, we assume stationarity
and approximate E(giz1Dgi)~E(g1Dg0) and P(giz1Dgi)~P(g1Dg0)
for all stages i of propagation. The points Ga, a[f0,1,2,3g,
where Ga&E(g1Dg0&Ga) for a[f0,1,2g and G1&E(g1Dg0&G3),
G3wG2, determine the range of typical group sizes occurring in
the networks (Fig. 4). The analytical predictions agree well with the
numerical results. The quantities E(giz1Dgi) and P(giz1Dgi) yield a
quantitative explanation of the mechanisms that lead to persistent
propagation of synchrony:

For networks of linearly coupled neurons, each synchronous
0§G0 neurons (G0 small, e.g. G0&4 in Fig. 4a) on
group with g0
average excites synchronous groups with less neurons. The smaller
groups in turn excite even smaller groups so that synchronous
activity rapidly decays to the level of a few synchronized neurons
and fluctuates near G0. Thereafter, due to the fluctuations from
the already small group size, propagating synchronous activity
rapidly extinguishes completely (group size zero). So the theory
predicts that in networks of linearly coupled neurons the chain of
synchronous activity quickly extinguishes even if excited by
external synchronous input, consistent with the above observations
(Fig. 2a). Since the shape of the transition matrix stays invariant
when network parameters like the coupling strengths are changed,
such a change will not lead to persistent propagation of synchrony.
If, e.g., the size of excitatory coupling strength is increased, only
the slope of the curve is increased. This predicts the transition to
unstable background activity shown in Fig. 3.




Figure 4. Evolution of synchronous pulses in linearly (a) and nonlinearly (b) coupled networks. Numerically derived probability
distributions P(g1Dg0~g’0), i.e. probabilities of pulse-sizes g1 in response to a pulse of size g0~g’0 are shown by gray shading; associated conditional
expectations E(g1Dg0~g’0), i.e. numerically derived mean response group sizes, are displayed by green squares. Error of the mean (confidence
intervals: two times standard deviation) has about the size of the plot symbol, larger errors are given by error bars. Analytical results for E(g1Dg0)
derived from diffusion approximation and statistics of the underlying network topology are given by blue dots, results from a semi-analytical
approach are given by red dots. Assuming stationarity and the Markov property, the probability distributions can be interpreted as stochastic iterated
map or transition matrix for the pulse-sizes in a chain of propagating synchronous activity. For linearly coupled neurons, there is no area from where
the pulse-sizes do not quickly converge with high probability to the level of spontaneously synchronized neuron groups. As an explicit example, the
light blue dotted lines display the dynamics from Fig. 2a as result of graphical iteration using the stochastic iterated map. In contrast, for nonlinearly
coupled networks, the probability for chains with pulse-sizes between G1 and G3 to converge to the level of spontaneously synchronized neuron
groups is rather low: There is a state of persistent propagation in the network located around E(g1Dg0&G2)&G2. As an explicit example for dynamics
assuming this state, the light blue dotted lines display the chain from Fig. 2b as a result of graphical iteration.
doi:10.1371/journal.pcbi.1002384.g004

In contrast, nonlinear

supra-additive excitatory coupling
enables persistent propagation of activity with a substantial
number of neurons synchronized. The sizes of the propagating
synchronous pulses are of the order of a typical size G2 and range
between G1 and G3, all of which are substantially larger than G0
(cf. Fig. 4b). Pulses of sizes between G1 and G3 usually evoke pulses
of sizes in the same range, i.e. between G1 and G3 again. Only
rarely, propagating synchronized activity becomes smaller than G1
or larger than G3; if so, the pulse size is likely to stay smaller than
G1 for longer, decay even further as for linearly coupled networks,
and the chain may cease to exist. A steeper and narrower peak can
lead to transiently increased activity and short-lived propagation of
larger synchronous groups [51].

The different dynamics for linearly and nonlinearly coupled
networks can also be understood by approximating the stochastic
dynamics by a deterministic iterative map derived from interpolat-
ing between the values of E(g1Dg0). For networks of linearly coupled
neurons, the map has only one stable fixed point G0 which is at
small pulse sizes of the order of spontaneous synchronization; it may
be distinct from the trivial fixed point zero. Any larger initial pulse
size will thus lead to a chain decaying to the level of spontaneous
synchronization. If coupling is non-additive, there can be two stable
fixed points G0 and G2, and an unstable fixed point G1 in between.
Chains starting with sizes in the basin of G2 between G1 and G3 then
evolve towards stable propagation with pulse-size G2. For different
parameter settings, stable propagation of synchrony is supported by
a stable periodic orbit close to an unstable fixed point G2.

Taken together, the theory for nonlinearly coupled networks
predicts persistent propagation of synchronous activity in a typical
range of pulse sizes and a decay that is possible only due to
fluctuations. This agrees with the numerical observations (Fig. 2b).

Discussion

recurrent networks of

In summary, we presented a theoretical analysis and numerical
spiking neurons with
simulations of
nonlinear dendritic interactions. The results indicate that networks
with nonlinear dendritic interactions are capable of generating
persistent propagation of synchronous spiking activity even if the
network is purely randomly connected and has no additional
structural features.

Theoretical studies on active dendrites mainly considered single
neurons. Simulations of neuron models with detailed channel
density and morphology showed dendritic spike generation in
agreement with neurobiological experiments [33,34,36,38]. For
neurons with slow dendritic spikes, which are largely insensitive to
temporal coincidence of
firing rate models have been
developed [52]. They reproduce the response properties of
detailed models to diverse stimuli and possess computational
capabilities comparable to multi-layered feed-forward networks of
simple rate neurons [38,39]. Based on this result, the computa-
tional abilities of simple circuits have been considered, also with
other types of neuron models (e.g. [32,53,54]). Refs. [55,56]
studied propagation of bursts in networks where the bursts can be
explained by slow dendritic spikes, and slow nonlinear dendrites

inputs,


were suggested to underlie the persistent activity observed in
working memory tasks [57]. Active dendrites generating fast
dendritic sodium spikes were studied in a two-neuron circuit and
in a simple feed-forward structure [58], and model neurons
incorporating such dendritic spikes were used as an output layer in
simulations of hippocampal network models [59]. Very recently,
fast dendritic spikes can lead to
ref.
intermittent, transiently increased propagation of synchrony and
it was suggested that they underlie hippocampal sharp wave/
ripples characteristic for slow wave sleep.

shown that

[51] has

The present study now shows that fast dendritic spikes can lead
to persistent propagation of synchrony in random neural networks.
In particular,
feed-forward structures based on large-scale
additional couplings [10,15,16] or strongly and systematically
adapted strengths of specific synapses and neuron properties [17]
may not be needed. As such, our results suggest an alternative
mechanism and a potential complementary explanation for the
occurrence of patterns of precisely timed spikes [1–5,7–9].

Our study uses a model that is appropriate for quantitative
numerical analysis of larger networks and at the same time allows
analytical predictions that yield further insights into the dynamics
of recurrent networks. The theoretical predictions made are based
on mean field arguments, strictly valid only in the limit of infinite
network size [42,49,60]. As our results indicate, these predictions
are in good agreement with simulation data already for networks
of finite size. The number of neurons participating in pulses of
synchronous activity as well as their number relative to the total
number of neurons may vary strongly with network features such
as the connectivity and the effective total input coupling strengths.
Additional external noise, e.g. due to further random spiking
inputs, is expected to be beneficial because it stabilizes background
activity and leads to a fast equilibration of the neurons’ potentials
after a synchronous pulse. Both facts support dynamical mixing
and thus are in favor of our approximation that the propagation of
synchronous activity does not further influence the statistics of the
background. We have demonstrated that nonlinear dendritic
interactions enable persistent propagation of synchrony even in
random neural networks. The results show that the nonlinear
interactions are in fact
the main ingredient controlling the
mechanism underlying the transition to persistent propagation
(Fig. 4a vs. 4b), so that the phenomenon is insensitive against
variations in parameters such as details of the individual neuron
dynamics, the exact form of nonlinearly modulated interactions
(Fig. 1), and the coupling strengths (see Fig. 3).

The current study contributes to a new field of research that
focuses on neural networks with supra-additive coupling. The
influence of different levels of individual neuron reliability, of
recurrent and feed-forward network topologies, of dynamic
connectivity (learning) and of slow dendritic spikes have to be
reconsidered in this context. Our study also suggests future
experiments on the propagation of synchrony due to nonlinear
dendritic interactions e.g. in cultured neurons [61]. Interestingly,
synchrony found here for nonlinearly
the propagation of
interacting neurons does not
follow any specific, predefined
propagation paths of synchronous activity across the network;
the propagation path will depend not only on the currently excited
group but also on which neurons in the background activity are
sufficiently depolarized when they receive synchronous spikes from
the current group. In a random network, the propagation of
synchrony will
reverberating high-frequency
oscillations involving highly synchronous spiking activity. The
shape the activity and lead to a
network structure might
significantly enhanced occurrence of
sequences of
specific
synchronous groups. These spike patterns, however, are noisy

resemble

thus


and less obvious
than those in synfire-chains [10,15–17,19–
21,23,24], where the propagation paths of synchronous activity
are predefined by the embedded feed-forward networks. These
different dynamics may provide an experimentally testable
distinction between synchronous events created by synfire chains
via additional
feed-forward structures and those created by
nonlinear dendritic interactions in largely or purely random
networks. Of course, a more specifically structured network
connectivity [62–64], the effects of synaptic location on different
dendritic branches [39], specific distributions of
transmission
delays [25,65–67] as well as strongly heterogeneous synaptic
further influence pulse propagation. As an
strengths [17] will
example, nonlinear interactions may facilitate or enable localized
persistent synchrony in Hebbian cell assemblies [18,68,69]. It will
thus be important
to extensively investigate to which degree
nonlinear interactions as well as non-random network structure
are contributing to creating collectively coordinated spiking
dynamics, in order to understand the computational capabilities
of cortical networks.

Methods

Neural network model

We considered networks of N leaky integrate-and-fire neurons
connected to form an Erdo¨s-Re´nyi random graph [70] where each
directed synaptic connection between two neurons is present
independently with probability p0. For each connection,
the
probabilities pEx and pIn~1{pEx specify whether the coupling is
excitatory or inhibitory. The dynamics of the membrane potential
Vl of neuron l obeys

dVl(t)
dt

~{clVl(t)z X

½s(

X

elj)z X

elj(cid:2)

f

j[MEx,l (f )

j[MIn,l (f )

ð1Þ

(cid:2)
d t{tf {t

(cid:3)zI0,l,

where tf denotes times at which spike are sent within the network,
the inverse membrane time constant cl~1=tmem,l measures the
dissipation of the neuron and t is the transmission delay. We
further introduced the set

MEx,l(f )~fj : (eljw0 ^ Ak : ts
jk

~tf )g

ð2Þ

of neurons sending at time tf an excitatory spike to neuron l,
where ts
jk is the kth spike time of neuron j and elj is the coupling
strength from neuron j to neuron l. The set

MIn,l(f )~fj : (eljv0 ^ Ak : ts
jk

~tf )g

ð3Þ

lists the neurons sending at time tf an inhibitory spike to neuron l.
s is the possibly nonlinear dendritic modulation function mapping
the input strength expected from linear addition of excitatory
inputs to the actual input strength. Each neuron receives some
constant external input I0,l. When the membrane potential reaches
or exceeds the threshold, Vl(t{)ze§HU,l, where e is the possibly
arriving total input at time t, it is reset to Vl(t)~Vr,l and a spike is
emitted. See supporting Table S1 for a tabular description of our
model following ref. [71].

The parameters used in the given examples are Va~2mV for
the onset of supra-additivity, Vb~4mV for the onset of saturation
and Vc~6mV for the level of saturation, in agreement with a
direct experimental measurement of s given in [39] for slow


i.e.

nonlinear interactions. In [33], the onset of nonlinearity and the
level of saturation lie higher. For comparison with linearly coupled
networks, we take an identity s(e)~e modulating function,
effectively choosing Va~Vb~Vc~?,
there is no supra-
additivity and no saturation. The analytical methods presented
below and the theory presented in the main text are valid for
arbitrary parameter choices and hold as long as the background
activity stays asynchronous, irregular and sufficiently uncorrelated.
In the simulations,
the remaining network parameters are
N~1000, p0~0:3, pEx~pIn~0:5, tmem,l~8ms~1=cl, t~5ms,
I0,ltmem,l~17:6mV, HU,l~HU ~16mV, Vr,l~0mV. If not stated
otherwise, elj~0:2mV, if the coupling strength from neuron j to
neuron l is excitatory and elj~{0:2mV, if it is inhibitory.

Numerical methods

ð

ð

IF,l UIF,l(w)ze

Network simulations were done in phase representation [72]. For
this, the membrane potential Vl and its threshold HU,l are mapped
one-to-one to a phase wl and a phase-threshold Hl using the inverse
of the transfer function UIF,l(w)~I0,l=cl 1{ exp ({clw)
Þ of the
leaky integrate-and-fire neuron, as elaborated in ref. [27]. wl evolves
linearly with slope 1 between spike sendings and spike receivings.
Spike sendings occur when the phase reaches or exceeds its
threshold Hl. When neuron l receives input of total strength e at
time t, its phase wl(t{) is updated according to wl(t)~H(l)
e (wl(t{)),
where H(l)
e (:) is the response function of the leaky integrate-and-fire
e (w)~U {1
neuron, H (l)
Þ for subthreshold total inputs e
e (w)~0 for suprathreshold ones which evoke spike sending.
and H(l)
The numerical simulations were implemented using an event
based algorithm which may be outlined as follows [41,50,73,74]:
We keep track of the ‘‘pseudo-spike time’’ [75] of each neuron l,
i.e. of the time Hl{wl remaining to the next hypothetical spike of
the neuron without interaction. Further, we keep track of the spike
arrival times together with the neurons that sent the spikes. In each
step, the smallest pseudo-spike time is compared with the time
remaining until the next spikes arrive. If the next event is (i) a spike
sending event, the dynamics is linearly evolved to this event and
the pseudo-spike time of each sending neuron l is reset to Hl. The
newly sent spikes are stored in the spike list. If the next event is (ii)
a spike receiving event, the dynamics is linearly evolved to this
event and the excitatory and inhibitory input strengths to each
neuron l are determined. We apply s to the excitatory input
strength and add the inhibition. The resulting total input strength
e determines the update of the phase via H(l)
e (:) and therewith the
new pseudo-spike time as well as immediate spiking responses.

For the spike-train analysis, propagating chains initiated at some
time t0 can be separated from background activity because
synchronized groups which are part of the chain by construction
send spikes precisely at t0znt, n[N, while spikes which are part of
background activity are sent at times which are at least slightly
different.

0Dg0~g0

0) and the conditional expectations E(g1Dg0~g0

Fig. 4 shows the numerically derived frequency of occurrence of
0 and its mean
0 when the initial group had size g0
a group size g1
value, which are approximations to the conditional probability
P(g1~g1
0),
respectively. For the numerical measurements, synchronous pulses
0[f1,7,13,:::,181g were initiated twice after equilibration of
of size g0
the dynamics (initial phases were randomly drawn from a uniform
distribution on ½{Hw,Hw(cid:2) where Hw is the phase threshold, and
1{50 random initial spikes were added) in 50 different random
0 of the subsequent pulse was measured.
networks and the size g1
0~100.
Fig. 2 shows two single simulations with g0

For Fig. 3, the mean total input strengths (cid:2)eeEx,ges,(cid:2)eeIn,ges of the
excitatory and the inhibitory input were varied in steps of


0:375mV by changing eEx and eIn, from (cid:2)eeEx,ges~24mV (corre-
sponding to eEx~0:16mV) to (cid:2)eeEx,ges~60mV (eEx~0:4mV) and
from (cid:2)eeIn,ges~{24mV (eIn~{0:16mV)
to (cid:2)eeIn,ges~{60mV
(eIn~{0:4mV). For each data point, the stability of background
activity and the persistence of propagating synchrony was checked
in 20 different random networks with different random initial
conditions, initial phases were drawn from a uniform distribution
on ½{Hw,Hw(cid:2) where Hw is the phase threshold, and 1{50
random spikes initially in transit were added. The stability of
background activity without propagating synchrony was checked
for simulated time t[½0ms,t0(cid:2), where t0[½300ms,330ms(cid:2). At t0,
synchronous activity was initiated by external stimulation of a
group of 100 neurons. Stability of propagating synchrony was
checked for 10 steps after initiation (corresponding to 55ms of
propagation) and stability of background activity after t0 was
checked for an interval of 105ms after pulse initiation. We note
for stable irregular background activity finally (for time
that
tending to infinity) every chain will die out with probability one,
because the group size has finite probability to leave the zone of
propagation and to reach the absorbing fixed point zero.

We implemented the network dynamics simulations in C and
embedded them with MathLink into Mathematica. We used
Mathematica to implement user interfaces, control programs and
data analysis.

Analytical methods

We computed the transition probabilities for the group-sizes
analytically and semi-analytically. In the analytical approach, the
probability distribution for the membrane potentials P(V ) was
derived in diffusion approximation, also approximating the actual
number of synaptic connections by its mean and describing the
background activity as consisting of independent Poissonian spike
trains [42,44]. To eliminate errors due to these approximations in
a semi-analytical approach, P(V ) was derived by direct measure-
the relative frequency of occurrences of membrane
ments of
potentials at different times in 1000 numerical network simula-
tions, 10 simulations in 100 different random networks with
different random initial conditions as described above. In both
approaches, we computed from P(V ) the cumulative probability
distribution from the right,

ðHU

F (e)~

HU {e

P(V )dV ,

ð4Þ


which yields the average probability F (e) that a neuron is excited
above threshold when it receives an input of strength e. We further
assumed (a) that previous groups with jvi do not influence giz1
,
i.e. the sequence of group sizes is a realization of a Markov chain,
(b) that the propagating synchrony does not change the statistics of
the background dynamics of the non-participating neurons, and (c)
that neurons which spiked in the ith step are refractory while the
other neurons are equilibrated at the time of the iz1th pulse. The
validity of the approximations depends on the network parameters
these
and was
assumptions,
the neural network
topology allow to compute the probabilities that a neuron receives
an input of strength e at time tizt under the condition that a
0 has sent spikes simultaneously at
synchronized group of size gi
time ti. Together with F (e), the conditional probability distribu-
tions P(giz1Dgi) and the conditional expectations E(giz1Dgi) can
be derived. P(giz1~giz1
0), the probability that a group
size giz1~giz1
0, follows
a binomial distribution,

0 occurs in response to a group size gi~gi

the statistical properties of

checked by numerical

simulations. Under

Dgi~gi


P(giz1~g0

iz1jgi~g0

i)~

N{g0
i

g0
iz1

!

Ps(g0

i)g0

iz1

(1{Ps(g0

i))N{g0

i

{g0

iz1 ,

where

Ps(g0

g0
{j1
i
X

g0
i
i)~ X
~1
j1
(p0pEx)j1 (p0pIn)j2 (1{p0)g0

F (e(j1,j2))

~0

j1!j2!(g0
i

j2

i

g0
i!
{j1{j2)!

{j1

{j2

ð5Þ

ð6Þ


spikes. e(j1,j2)~s(j1eEx)zj2eIn is the total

is the probability that a neuron spikes in response to a synchronous
pulse of gi
input
strength due to j1 excitatory and j2 inhibitory inputs and eExw0
and eInv0 are the strengths of excitatory and inhibitory
connections. According to Eq. (5), E(giz1Dgi~gi
0), the average
next group size giz1 given a current group size of gi~gi
0, is


Supporting Information

Figure S1 Distribution of sizes of synchronous pulses in the
background activity, where spikes belonging to the externally
initiated propagating chain of pulses have been removed. The
distributions are similar in linearly (a) and in nonlinearly (b)
coupled networks. The figure exemplarily displays the sizes of
spontaneously synchronized pulses in the background activity
within the interval ½100ms,200ms(cid:2) for the dynamics shown in
Fig. 2a and 2b in the main text, respectively. While small pulse
sizes of the order of G0&4 (see Fig. 3 in the main text) are
relatively common, large pulses do not occur on relevant time
scales. The chain of synchronous activity excited in the linearly
coupled network quickly decays to this level of spontaneous
synchronization. In contrast, in the nonlinearly coupled network,
the pulse-sizes of propagating chains are of the order of 100
neurons and thus clearly separated from the spontaneously
occurring pulses: The propagation of synchrony is persistent.
(TIF)

Table S1 Tabular description of our model following ref. [71].
(PDF)

E(giz1Dgi~gi

0)~(N{gi

0)Ps(gi

0):

ð7Þ

Acknowledgments

E(g1Dg0) as derived from the diffusion approximation and from the
semi-analytical approach is illustrated in Fig. 4 for linearly and
nonlinearly coupled networks. The values agree well with the
results of the explicit numerical measurements, deviations are due
to the specified approximations. The critical pulse-sizes G0, G1
and G2
interpolated
are
intersection points of
E(g1Dg0~g0
0)-values with the diagonal, G3 denotes
the size
0)-values equal G1.
g0
If present, G1 and G3 roughly bound the pulse-sizes in persistently
propagating chains of synchronous activity.

0wG2, where the interpolated E(g1Dg0~g0

the

the

References

1.

Lestienne R, Strehler B (1987) Time structure and stimulus dependence of
precisely replicating patterns present in monkey cortical neuronal spike trains.
Brain Res 437: 214–238.

2. Abeles M, Bergman H, Margalit F, Vaadia E (1993) Spatiotemporal firing
in the frontal cortex of behaving monkeys. J Neurophysiol 70:

patterns
1629–1638.

3. Riehle A, Gru¨n S, Diesmann M, Aertsen A (1997) Spike synchronization and
rate modulation differentially involved in motor function. Science 278:
1950–1953.

5.

4. Oram M, Wiener M, Lestienne R, Richmond B (1999) Stochastic nature of
precisely timed spike patterns in visual system neuronal responses. J Neurophysiol
81: 3021–3033.
Ikegaya Y, Aaron G, Cossart R, Aronov D, Lampl I, et al. (2004) Synfire chains
and cortical songs: Temporal modules of cortical activity. Science 304: 559–564.
Johansson RS, Birznieks I (2004) First spikes in ensembles of human tactile
afferents code complex spatial fingertip events. Nat Neurosci 7: 170–177.
7. Gansel K, Singer W (2005) Replay of second-order spike patterns with

6.

millisecond precision in the visual cortex. Soc Neurosci Abstr 276.8.
8. Mokeichev A, Okun M, Barak O, Katz Y, Ben-Shahar O, et al.

(2007)
Stochastic emergence of repeating cortical motifs in spontaneous membrane
potential fluctuations in vivo. Neuron 53: 413–425.
Pipa G, Riehle A, Gru¨n S (2007) Validation of task-related excess of spike
coincidences based on NeuroXidence. Neurocomputing 70: 2064–2068.
10. Abeles M (1982) Local Cortical Circuits: An Electrophysiological Study. Berlin:

9.

Springer.

11. Bienenstock E (1996) Composition. In: Aertsen A, Braitenberg V, eds. Brain

Theory: Biological Basis and Computational Principles Elsevier.

12. Nowak L, Sanchez-Vivez M, McCormick D (1997) Influence of low and high
frequency inputs on spike timing in visual cortical neurons. Cereb Cortex 7:
487–501.

13. Prut Y, Vaadia E, Bergman H, Haalman I, Slovin H, et al. (1998) Spatio-
temporal structure of cortical activity: Properties and behavioral relevance.
J Neurophysiol 79: 2857–2874.

14. Singer W (2004) Time as coding space in the cerebral cortex. In: Kanwisher N,
Duncan J, eds. Functional Neuroimaging of Visual Cognition Oxford Univ.
Press.

We thank M. Both, A. Draguhn, K. Gansel, T. Geisel, M. Herrmann, S.
Jahnke, N. Maier, A. Morrison, S. Reichinnek, J. Schiller, D. Schmitz, W.
Singer and F. Wolf for fruitful discussions.

Author Contributions

Wrote the paper: RMM MT. Designed research: RMM MT. Performed
research: RMM MT.

15. Herrmann M, Hertz J, Pru¨gel-Bennett A (1995) Analysis of synfire chains.

Network 6: 403–414.

16. Diesmann M, Gewaltig MO, Aertsen A (1999) Stable propagation of

synchronous spiking in cortical neural networks. Nature 402: 529–533.

17. Vogels T, Abbott L (2005) Signal propagation and logic gating in networks of

integrate-and-fire neurons. J Neurosci 25: 10786–10795.

18. Aviel Y, Horn D, Abeles M (2005) Memory capacity of balanced networks.

Neural Comp 17: 691–713.

19. Gewaltig MO, Diesmann M, Aertsen A (2001) Propagation of cortical synfire
activity: Survival probability in single trials and stability of the mean. Neural
Netw 14: 657–673.

20. van Rossum M, Turrigiano G, Nelson S (2002) Fast propagation of firing rates

through layered networks of noisy neurons. J Neurosci 2: 1956–1966.

21. Mehring C, Hehl U, Kubo M, Diesmann M, Aertsen A (2003) Activity dynamics
and propagation of synchronous spiking in locally connected random networks.
Biol Cybern 88: 395–408.

22. Tetzlaff T, Morrison A, Geisel T, Diesmann M (2004) Consequences of realistic
network size on the stability of embedded synfire chains. Neurocomputing 58–
60: 117–121.

23. Hayon G, Abeles M, Lehmann D (2003) A model for representing the dynamics

of a system of synfire chains. J Comp Neurosci 18: 41–53.

24. Kumar A, Rotter S, Aertsen A (2008) Conditions for propagating synchronous
spiking and asynchronous firing rates in a cortical network model. J Neurosci 28:
5268–5280.
Izhikevich E (2006) Polychronization: Computation with spikes. Neural Comp
18: 245–282.

25.

26. Memmesheimer R, Timme M (2006) Designing the dynamics of spiking neural

networks. Phys Rev Lett 97: 188101.

27. Memmesheimer R, Timme M (2006) Designing complex networks. Physica D

224: 182–201.

28. Urban N, Barrionuevo G (1998) Active summation of excitatory postsynaptic
potentials in hippocampal CA3 pyramidal neurons. Proc Natl Acad Sci U S A
95: 11450–11455.

29. Cash S, Yuste R (1999) Linear summation of excitatory inputs by CA1

pyramidal neurons. Neuron 22: 383–394.


30. Spruston N, Stuart G, Ha¨ usser M (2002) Dendritic integration. In: Spruston N,

53. Morita K (2008) Possible role of dendritic compartmentalization in the spatial

Stuart G, Ha¨ usser M, eds. Dendrites Oxford Univ. Press.

working memory circuit. J Neurosci 28: 7699–7724.

31. Ha¨ usser M, Spruston N, Stuart G (2000) Diversity and dynamics of dendritic

54. Rhodes P (2008) Recoding patterns of sensory input: Higher order features and


signaling. Science 290: 739–744.

32. London M, Ha¨ usser M (2005) Dendritic computation. Annu Rev Neurosci 28:

503–532.

33. Ariav G, Polsky A, Schiller J (2003) Submillisecond precision of the input-output
transformation function mediated by fast sodium dendritic spikes in basal
dendrites of CA1 pyramidal neurons. J Neurosci 23: 7750–7758.

34. Gasparini S, Migliore M, Magee J (2004) On the initiation and propagation of
dendritic spikes in CA1 pyramidal neurons. J Neurosci 24: 11046–11056.
35. Gasparini S, Magee J (2006) State-dependent dendritic computation in

hippocampal CA1 pyramidal neurons. J Neurosci 26: 2088–2100.

36. Nevian T, Larkum M, Polsky A, Schiller J (2007) Properties of basal dendrites of
layer 5 pyramidal neurons: A direct patch-clamp recording study. Nat Neurosci
10: 206–214.

37. Softky W (1994) Sub-millisecond coincidence detection in active dendritic trees.

Neuroscience 58: 13–41.

38. Poirazi P, Brannon T, Mel B (2003) Pyramidal neuron as two-layer network.

Neuron 37: 989–999.

39. Polsky A, Mel B, Schiller J (2004) Computational subunits in thin dendrites of

pyramidal cells. Nat Neurosci 7: 621–627.

40. Mel B (1999) Why have dendrites? A computational perspective. In: Stuart G,

Spruston N, Ha¨ usser M, eds. Dendrites Oxford University Press.

41. Ernst U, Pawelzik K, Geisel T (1995) Synchronization induced by temporal

delays in pulse-coupled oscillators. Phys Rev Lett 74: 1570–1573.

42. Brunel N (2000) Dynamics of sparsely connected networks of excitatory and

43.

inhibitory spiking neurons. J Comp Neurosci 8: 183–208.
Jahnke S, Memmesheimer RM, Timme M (2008) Stable irregular dynamics in
complex neural networks. Phys Rev Lett 100: 048102.

44. Burkitt A (2006) A review of

the integrate-and-fire neuron model: I.

Homogeneous synaptic input. Biol Cybern 95: 1–19.

45. Burkitt A (2006) A review of

the integrate-and-fire neuron model: II.
Inhomogeneous synaptic input and network properties. Biol Cybern 95: 97–112.
46. Rauch A, LaCamera G, Lu¨scher H, Senn W, Fusi S (2003) Neocortical
pyramidal cells respond as integrate-and-fire neurons to in vivo like input
currents. J Neurophysiol 90: 1598–1612.
Jolivet R, Rauch A, Lu¨scher HR, Gerstner W (2006) Integrate-and-fire models
with adaptation are good enough: Predicting spike times under random current
injection. In: Taketani M, Baudry M, eds. Advances in network electrophys-
iology using multi-electrode arrays Springer.

47.

48. Dayan P, Abbott L (2001) Theoretical Neuroscience: Computational and

Mathematical Modeling of Neural Systems. Cambridge: MIT Press.

49. van Vreeswijk C, Sompolinsky H (1996) Chaos in neuronal networks with

balanced excitatory and inhibitory activity. Science 274: 1724–1726.

50. Timme M, Wolf F, Geisel T (2002) Coexistence of regular and irregular
dynamics in complex networks of pulse-coupled oscillators. Phys Rev Lett 89:
258701.

51. Memmesheimer RM (2010) Quantitative prediction of

intermittent high-
frequency oscillations in neural networks with supralinear dendritic interactions.
Proc Natl Acad Sci U S A 107: 11092–11097.

52. Mel B (1992) The clusteron: Toward a simple abstraction for a complex neuron.
In: Moody J, Hanson S, Lippmann R, eds. Advances in Neural Information
Processing Morgan Kaufmann. pp 35–42.

the function of nonlinear dendritic trees. Neural Comp 20: 2000–2036.

55. Traub R, Wong R (1982) Cellular mechanism of neuronal synchronization in

epilepsy. Science 216: 745–747.

56. Long M, Jin D, Fee M (2010) Support for a synaptic chain model of neuronal

sequence generation. Nature 468: 394–399.

57. Wang XJ (1999) Synaptic basis of cortical persistent acitivity: The importance of

NMDA receptors to working memory. J Neurosci 19: 9587–9603.

58. Poznanski R (2002) Dendritic integration in a recurrent network. J Integr

Neurosci 1: 69–99.

59. Katz Y, Kath W, Spruston N, Hasselmo M (2007) Coincidence detection of
place and temporal context in a network of spiking hippocampal neurons. PLoS
Comp Biol 3: 2432–2445.

60. Helias M, Deger M, Rotter S, Diesmann M (2010) Instantaneous non-linear
processing by pulsecoupled threshold units. PLoS Comp Biol 6: e1000929.
61. Feinerman O, Moses E (2006) Transport of information along unidimensional
layered networks of dissociated hippocampal neurons and implications for rate
coding. J Neurosci 26: 4526–4534.

62. Milo R, Shen-Orr S, Itzkovitz S, Kashtan N, Chklovskii D, et al. (2002) Network
motifs: Simple building blocks of complex networks. Science 298: 824–827.

63. Sporns O, Ko¨tter R (2004) Motifs in brain networks. PLoS Biol 2: e369.
64. Song S, Sjo¨stro¨m P, Reigl M, Nelson S, Chklovskii D (2005) Highly nonrandom

features of synaptic connectivity in local cortical circuits. PLoS Biol 3: 0507.

65. Roxin A, Brunel N, Hansel D (2005) Role of delays in shaping spatiotemporal
dynamics of neuronal activity in large networks. Phys Rev Lett 94: 238103.
66. Wang Q, Perc M, Duan Z, Chen G (2009) Synchronization transitions on scale-
free neuronal networks due to finite information transmission delays. Phys Rev E
80: 026206.

67. Wang Q, Chen G, Perc M (2011) Synchronous bursts on scale-free neuronal

networks with attractive and repulsive coupling. PLoS one 6: e15851.

68. Hebb D (1949) The organization of behavior. New York: Wiley.
69. Amit D, Brunel N (1997) Model of global spontaneous activity and local
structured activity during delay periods in the cerebral cortex. Cereb Cortex 7:
237–252.

70. Holmgren C, Harkany T, Svennenfors B, Zilberter Y (2003) Pyramidal cell
communication within local networks in layer 2/3 of rat neocortex. J Physiol
551.1: 139–153.

71. Nordlie E, Gewaltig MO, Plesser H (2009) Towards reproducible descriptions of

neuronal network models. PLoS Comp Biol 5: e100456.

72. Mirollo R, Strogatz S (1990) Synchronization of pulse coupled biological

oscillators. SIAM J Appl Math 50: 1645–1662.

73. Timme M (2002) Collective dynamics in networks of pulse coupled oscillators
[Doctoral thesis]. Go¨ttingen (Germany): Department of Physics, Georg-August
University of Go¨ttingen.

74. Memmesheimer R (2008) Precise spike timing in complex neural networks
[Doctoral thesis]. Go¨ttingen (Germany): Department of Physics, Georg-August
University of Go¨ttingen.
Jin D (2002) Fast convergence of spike sequences to periodic patterns in
recurrent networks. Phys Rev Lett 89: 208102.

75.

---
**Source PDF:** `2018_04_article.pdf`
