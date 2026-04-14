[Re] Spike Timing Dependent Plasticity Finds the
Start of Repeating Patterns in Continuous Spike Trains
Pamela Hathway1 and Dan F. M. Goodman,1
1Department of Electrical and Electronic Engineering, Imperial College, London, UK
p.hathway16@imperial.ac.uk
Editor
Nicolas P. Rougier
A reference implementation of
Reviewers
→ Spike Timing Dependent Plasticity Finds the Start of Repeating Patterns in
Damien Drix
Continuous Spike Trains, Masquelier T, Guyonneau R, Thorpe SJ, PLoS ONE
Julien Vitay
3(1): e1377, 2008. https://doi.org/10.1371/journal.pone.0001377
Received May, 29, 2018
Accepted Jul, 5, 2018
Published Aug, 3, 2018
Introduction
Licence CC-BY
Neurons communicate through repeated, specifically timed action potential sequences
Competing Interests: (spike patterns) to convey information [3, 8]. Since neuronal activity is noisy and
The authors have declared that neurons are likely involved in a multitude of spike patterns of various lengths and
no competing interests exist.
extent, it can be hard to find spike patterns at first glance. The more neurons are
recorded,themoredifficultthetaskbecomesduetotheexponentialincreaseofpossible
combinations of spikes that could make up a pattern [2]. It is unclear how neurons
 Article repository
in the brain may extract relevant information from such input. In a 2008 paper,
Masquelier and colleagues demonstrated that a single neuron with afferent synapses
 Code repository
exhibiting spike timing dependent plasticity (STDP) is able to find the start of a
repeating pattern in noisy (artificial) data [6].
Masquelier,Guyonneau,andThorpe[6]useasimplefeedforwardnetworkinwhich
2000inputneuronsconnecttooneoutputneuronviaexcitatorySTDPsynapses. Half
of the input neurons spike according to a spike pattern of 50 ms length for about 25%
ofthetime. Findingthepatternismademoredifficultbyjitteringthepatternspikes,
addingrandomnoisespikestoallneurons, andensuringaconstantpopulationrateas
well as no differences in overall firing rate between neurons.
WereplicatedtheirfindingsusingthespikingneuralnetworksimulatorBrian[5,9],
whereas the the original study implemented the simulations in Matlab, with the main
functions being computed in C/C++ through mex files. In addition, we examined
some of the implementation details and parameters and investigated whether they
were essential to the success of the algorithm.
Methods
All simulations were performed using the spiking neural network simulator Brian
(Brian2, version 2.0, http://briansimulator.org/). We attempted to stay as true as
possible to the original study. Simulation parameters were taken from the text and
we additionally obtained the source code for the standard parameter configuration
from the authors to ensure equivalency of the implementations. The source code for
deleting spikes within the pattern (Fig. 5 E) was not provided.
ReScience j rescience.github.io 6 - 1 Aug 2018 j Volume 4 j Issue 1


| Running | simulations |     |     |     |     |     |

Brian calculates neuron properties such as membrane voltage at discrete time steps.
The time step for these simulations was 10(cid:0)4 s unless otherwise indicated. Each
parameter combination was run 100 times and the success of a run determined as in
the original study: a hit rate of over 98%, no false alarms and an average latency of
| under 10   | ms (as calculated | over     | the      | last 150 s | of the simulation). |            |

|            |                   |          | Table 1: | Parameter  | variations          |            |
| parameters |                   | standard |          |            |                     | variations |
| w          |                   |          | 0.475    | 0.275,     | 0.325, 0.375,       | 0.425      |
initial
| jitter (sd)       | [ms]       |     | 1    |     | 0, 2,      | 3, 4, 5, 6 |

| pattern frequency |            |     | 0.25 |     | 0.05, 0.1, | 0.15, 0.5  |
| prop. neurons     | in pattern |     | 0.5  |     | 0.3,       | 0.4, 0.6   |
| spike deletion    |            |     | 0    |     | 0.1,       | 0.2, 0.3   |
Spike trains
The spike trains of the 2000 input neurons were created in the same way as in the
original study: a Poisson process with a variable instantaneous firing rate (30-90 Hz,
| 64 Hz on | average) with | no refractory |     | period. |     |     |

The absence of a refractory period in the input neurons has the effect that inter
10(cid:0)9
spike intervals can be as small as s in some cases. The original implementation
usesanevent-basedsimulationmethodinwhichthesimulationvariables(outputneu-
ron voltage etc.) are calculated at every input neuron or output neuron spike, and so
| such small | inter spike intervals |     | are not | a problem. |     |     |

Brianontheotherhandusesdiscretetimestepsforitssimulationsandupdatesits
simulation variables once per time step. In order to convert the original spike trains
into Brian, we had to modify the spike trains slightly: whenever two spikes from the
same neuron happened in the same time step, we deleted the second spike. At a
10(cid:0)4
resolution of s (standard time step) this affected 0.25% of all spikes, and at a
resolutionof10(cid:0)6 sitaffected0.0025%. Deletingspikesdoesnotaffecttheinputdrive
totheneuronsignificantlysincetheinitialfiringrateoftheoutputneuronisthesame
| with or without | the close | spikes. |        |     |     |     |

| Leaky Integrate | and       | Fire    | neuron |     |     |     |
TheoriginalstudymodelsthepotentialoftheoutputneuronwiththeGerstner’sSpike
Responsemodel(SRM)[4],whichuseskernelstocalculatetheeffectofincomingspikes
on the postsynaptic voltage. Brian on the other hand uses differential equations to
model the system parameters and evaluates those equations for each time step. The
SRMkernelscan bemodelled using alphafunctions [1], so weconvertedthekernelsof
the postsynaptic potential and the spike afterpotential into the following differential
equations:
Xx(cid:0)u
|     |     |     | du  |          | Aa       |     |

|     |     |     | =   |          | +        | (1) |
|     |     |     | dt  | (cid:28) | (cid:28) |     |
|     |     |     |     | m        | s        |     |
|     |     |     |     | dx       | x        |     |
=(cid:0) (2)
|     |     |     |     | dt (cid:28) |     |     |

syn
|     |     |     |     | da  | A   |     |

=(cid:0) (3)
|     |     |     |     | dt (cid:28) | s   |     |

The values for the parameters can be found in Tbl. 1. We chose the exact method
for integrating the differential equations (called ‘linear’ in Brian). Eq. 1 describes
j j j
ReScience rescience.github.io 6 - 2 Aug 2018 Volume 4 Issue 1


|     |     |     | A   |     |     | B   |     |

 original  replication
|     | 6   |     |     |     |     | 6   |     |

potential
input spikes
|     | ].u.a[ laitnetoP 4 |     |     |     |     | 4   |     |

threshold
rest. potential
|     | 2   |     |     |     |     | 2       |       |

|     | 0   |     |     |     |     | 0       |       |
|     | 2   |     |     |     |     | 2       |       |
|     | 0   | 20  | 40  | 60  | 80  | 0 20 40 | 60 80 |
times [ms] times [ms]
Figure 1: Postsynaptic potential. The postsynaptic potential of the replication implementation
behaves the same as in the original study. Both show the same EPSP shapes and the negative
afterpotential after a postsynaptic spike. A) The postsynaptic potential of the original study
was calculated using the equations given in the original paper. B) The postsynaptic potential in
the replication implementation was calculated from the differential equations specified in section
| Leaky | Integrate | and Fire | neuron |     |     |     |     |

the postsynaptic membrane potential, which is influenced by presynaptic excitatory
postsynaptic potentials(EPSPs, first term) and a negativeafterpotentialafter a spike
(second term). In the event of a presynaptic spike at neuron i, x is increased by the
(x x+w
respecitve synaptic weight w ), which initiates the voltage increase in the
|     |     |     |     | i   | i   |     |     |

postsynaptic neuron. When the postsynaptic voltage reaches the threshold, a spike

occurs: the voltage u is set to twice the threshold (u 2T), all EPSPs are flushed
(all x set to 0, x 0) and the negative afterpotential is set into motion (a is set to 1,
a   1). Presynaptic spikes had the same effect on the postsynaptic neuron potential
| as in           | the original | publication |       | as shown        | in Fig.    | 1.         |     |

|                 |              |             |       | Table 2:        | Simulation | parameters |     |
| LIF neuron      |              | value       | …………… | STDP            |            | value      |     |
| (cid:28) m [ms] |              |             | 10    | (cid:28)        | + [ms]     | 16.8       |     |
| (cid:28) [ms]   |              | 2.5         |       | (cid:28)(cid:0) | [ms]       | 33.7       |     |
s
| (cid:28) [ms] |     | 2.5 |     | a        |     | 2(cid:0)5 |     |

| syn           |     |     |     |          | +   |           |     |
| T [a.u.]      |     | 500 |     | a(cid:0) |     | 0.85 a    |     |
+
|     |     | (cid:28) (cid:28) m           |     |     |     |     |     |

| X   |     | s (cid:28)s (cid:0) (cid:28)m |     | w   | min | 0   |     |
(cid:28) m
| A   |     | -3  | T   | w   |     | 1   |     |

max
| ∆x    |        |           | 1   | -          |     | -   |     |

| ∆a    |        |           | 1   | -          |     | -   |     |
| Spike | Timing | Dependent |     | Plasticity |     |     |     |
Forsynapticplasticity,theoriginalstudyusesthereducednearestneighborrule(RNN)
[7]-amorerestrictiveversionofthenearestneighbor(NN)STDPrule. Inthestandard
NN rule, every spike causes a weight change (with the amount depending on the
timing of the nearest spike), while for RNN a weightchangeonly happens for the first
postsynaptic spike immediately following a presynaptic spike (or vice versa). This
means that for NN, there can be a series of potentiations or depressions, whereas for
| RNN | potentiations | and | depressions | strictly |     | alternate. |     |

AvisualisationofthreeSTDPrulesisshowninFig.2: theRNN,thestandardNN
and the all-to-all (ATA) rule, in which all pairs of spikes are considered to calculate
j j j
ReScience rescience.github.io 6 - 3 Aug 2018 Volume 4 Issue 1


A B C
ATA NN RNN
spikes pre
spikes post
weight
Figure 2: Effect of different learning rules on synaptic weight. We compare the all-to-all (ATA,
A), nearest neighbor (NN, B), and reduced nearest neighbor (RNN, C) learning rules for a case
in which the presynaptic neuron (green dots) spikes more often than the postsynaptic neuron
(bluedots). Greylinesindicatewhichspikepairsaretakenintoaccountforthecalculationofthe
synaptic weight change; the sign denotes a corresponding increase (+) or decrease (-) in weight
atthatspike. ThesynapticweightinATA(A)andNN(B)experiencemoreweightchangesand
also a net decrease in weight after only a few spikes. Under the RNN rule (C), there are fewer
changes and — in this example — no visible net weight change.
the weight change. A case is considered in which the presynaptic neuron (the input
neurons in this study) spikes more often than the postsynaptic neuron (the output
neuron in this study), leading to synaptic weight decreases for ATA and NN, but no
visible net change under RNN (Fig. 2 C).
Results
The ability to find repeating patterns was reproduced in the replication implemen-
tation. We could qualitatively reproduce all results of the original paper and show
thereproducedfiguresrelevanttothemodelbehaviour: latencydevelopment(Fig.3),
pattern specificity after convergence (Fig. 4), and robustness (Fig. 5). In addition, we
commentonsomeimplementationdetailsthatturnedouttoberelevanttoreplicating
the original study successfully: simulation time step, learning rule, EPSP shape.
Pattern finding
The latency measures the time of the output neuron spike relative to the start of the
pattern. If the spike occurs outside of the pattern (>50 ms after the start of the
pattern), the latency for that spike is set to 0 as in the original paper.
Inordertoassessthetimeofpatternfinding,weusedthesamespiketrain(standard
conditions) as input for both the original code and in the replication implementation.
Thelatencydevelopmentlookssimilarinbothimplementations(seeFig.3). Thetime
until a stable state arises is longer in the replication implementation (1400 discharges
instead of 700 or 20 s instead of 13.5 s). This discrepancy is due to the size of the
discrete time steps used (see section Implementation details).
At the end of the simulation, the synaptic weights that are maximally potentiated
(close to w = 1) belong exclusively to neurons involved in the pattern, whereas
max
weightsfromneuronsnotinvolvedinthepatternaredepressednearlycompletely(see
Fig. 4). Neurons that spike at the beginning of the pattern are potentiated, causing
the postsynaptic neuron to spike at a low latency.
Both latency development and the potentiation of only synaptic weights of pat-
tern neurons in the converged state were successfully reproduced by the replication
implementation.
ReScience j rescience.github.io 6 - 4 Aug 2018 j Volume 4 j Issue 1


|     |                       | A         |     |     |             | B            |      |

|     |                       |  original |     |     |             |  replication |      |
|     | 50                    |           |     | 50  |             |              |      |
|     | ]sm[ ycnetal ekips 40 |           |     | 40  |             |              |      |
|     | 30                    |           |     | 30  |             |              |      |
|     | 20                    |           |     | 20  |             |              |      |
|     | 10                    |           |     | 10  |             |              |      |
|     | 0                     |           |     | 0   |             |              |      |
|     | 0 1000                | 2000      |     | 0   | 1000        | 2000         | 3000 |
|     | # discharge           |           |     |     | # discharge |              |      |
Figure 3: Latency. Comparing the latency development of the original study (A) and the repli-
cation implementation (B). In both implementations, the timing of the output spike in relation
to the start of the pattern (vertical axis, set to latency=0 if output spike happens outside the
pattern) is random at first, but becomes selective after a few hundred discharges. From then on
the postsynaptic neuron always spikes only within the pattern (no spikes at latency = 0). The
number of discharges until this happens is smaller in the original paper than in the replication
implementation.
|     |           | A   |      |     | B            |     |                     |

|     |  original |     |      |     |  replication |     |                     |
|     | 2000      |     | 2000 |     |              |     | 1.0                 |
|     | 1500      |     | 1500 |     |              |     | 0.8 thgiew citpanys |
tnereffa #
0.6
|     | 1000 |     | 1000 |     |     |     |     |

0.4
|     | 500 |     | 500 |     |     |     |     |

0.2
|     | 0        |        | 0   |        |          |     | 0.0 |

|     | 449.85   | 449.90 |     | 449.85 | 449.90   |     |     |
|     | time [s] |        |     |        | time [s] |     |     |
Figure 4: Weights at converged state. This figure shows a raster plot of the input spikes at
the end of the simulation (converged state) with the color of the dots indicating the synaptic
weight(seecolorbar). Thefinalweightsintheconvergedstatelookverysimilarinthetheoriginal
study (A)) and the replication implementation (B)). Weights from neurons not involved in the
pattern are close to 0 (black, neurons 1000-1999), whereas weights from some neurons involved
in the pattern (neurons 0-999) are close to 1 (white, maximum value). The weights of neurons
that spike at the beginning of the pattern are nearly all close to 1 and their added postsynaptic
| potentials | cause a spike at | the beginning | of the | pattern (blue | rectangle). |     |     |

| j          |                  |               |        |               |             | j   | j   |
ReScience rescience.github.io 6 - 5 Aug 2018 Volume 4 Issue 1


|     | A   |     | B   | C   |     | D   |     | E   |
| --- 

sseccus fo %


|     |     |     |     |     |     | rep 10 | 4   |     |

|     | 25  |     |     |     |     | rep 10 | 6   |     |
orig rerun
orig paper

|     | 0.1 0.3 0.5  | 0              | 2 4 | 6 0.2 0.4        | 0.6 | 0.3 0.4        | 0.5 0.0        | 0.1 0.2 0.3 |

|     | Pattern freq | Jitter SD [ms] |     | Prop. pat. neur. |     | Initial weight | Spike deletion |             |
Figure5: Robustness. Patternfindingabilitiesofthesystemweretestedagainstdifferentpattern
presentationfrequencies(A),jitter(B),numberofneuronsspikingaccordingtothepattern(C),
initialweights(D)anddeletionofspikesinthepattern(E).Foreachparametercombination100
simulations were run and the number of successful runs are reported as percentage of success.
Thereplicationimplementationwasrunattwodifferenttimesteps: 10(cid:0)4 s(solidblacklines)and
10(cid:0)6
s(dashedblacklines). Theresultsfromtheoriginalstudywerecalculatedusingthesource
codeprovided(solidgreenlinesinA,B,C,D)orestimatedfromtheoriginalpublication(dashed
| green line | in E). |     |     |     |     |     |     |     |

]s[ emit gnidnif nrettap


|     |     |     | 10 6 | 10  | 5   | 10 4 |     |     |

simulation time step [s]
Figure 6: Time until finding pattern. Using larger simulation time steps leads to the pattern
to be found later. The horizontal striped green line is the reported time when the pattern is
found by Masquelier, Guyonneau, and Thorpe [6]. Errorbars represent standard deviation from
| 100 successful | runs. |     |     |     |     |     |     |     |

Robustness
Our simulations showed largely the same resilience to degradations as in the original
paper, but despite the very similar implementations, there were some differences.
The replication implementation behaves the same as the original study when sub-
jectedtodifferentamountsofjitter(Fig.5B),variousproportionsofneuronsinvolved
in the pattern (Fig. 5 C), different initial weights (Fig. 5 D) and when a percentage
| of spikes | within the pattern |     | are deleted | (Fig. | 5 E). |     |     |     |

At a high pattern repetition frequency of 0.5 (Fig. 5 A), when the pattern is
presented every 100 ms for 50 ms, the performance of the replication differs from the
atlargertimestepsof10(cid:0)4
| original:        |           |      |         | sthereplicationversiondoesnotperformaswell |      |                   |     |     |

| as the original, | but shows | good | results | at smaller                                 | time | steps (10(cid:0)6 | s). |     |
| Implementation   | details   |      |         |                                            |      |                   |     |     |
We noticed that small implementation details can affect the behaviour of the network
| significantly. | We summarised |     | the relevant | details | in  | Table tbl. | 3.  |     |

| j              |               |     |              |         |     |            | j   | j   |
ReScience rescience.github.io 6 - 6 Aug 2018 Volume 4 Issue 1


| Simulation | time step |     |     |     |     |     |     |

In the standard parameter configuration, the time step chosen does not have an effect
onoverallpatternfindingsuccess,aslongasthetimestepislessthanorequalto10(cid:0)4
(10(cid:0)3
s. At larger time steps s), no specificity emerges. Instead there is a systematic
potentiation of all synaptic weights leading to very high firing rates in the output
neuron. In contrast, success rates are above 95% for 10(cid:0)4 s, 10(cid:0)5 s, 10(cid:0)6 s, and 10(cid:0)7
s.
Although the success rate stays roughly the same, the time until the pattern is
found(definedasthetimeafterwhichnooutputspikeshappenoutsideofthepattern)
increases with larger time step size. An example can be seen in Fig. 3: the pattern
is found after about 700 output neuron spikes in the original publication (left) and
10(cid:0)4
after about 1400 in the replication implementation (right) at a time step of s for
the same input. At smaller times steps (10(cid:0)6 s), the pattern is found after about 700
| discharges | - the same       | as in       | the original |                     | publication | (Fig. 6). |               |

|            |                  |             | Table        | 3: Implementation   |             | details   |               |
|            |                  |             |              | works               |             |           | does not work |
| simulation | time step        | continuous, |              | discrete            |             |           |               |
|            |                  |             |              | (cid:20) 10(cid:0)4 |             |           | 10(cid:0)4    |
| time step  | size             |             |              |                     | s           |           | > s           |
| learning   | rule             |             |              | RNN                 |             |           | ATA, NN       |
| EPSP shape |                  |             |              | kernel              | immediate   | voltage   | increase      |
| Version    | of STDP learning |             | rule         |                     |             |           |               |
The choice of learning rule is crucial for the pattern finding abilities of the network.
The RNN rule results in stable posystnaptic firing and reliable finding of the pattern.
| The use | of other learning | rules | does | not | result in | stable learning. |     |

The spike trains used here involve neurons with a continuously high firing rate
in the input neurons (on average 64 Hz, min 30 Hz, max 90 Hz) and a significantly
lower firing rate in the output neuron (63 Hz initially, 5Hz after reaching specificity).
This means that input neurons fire often in the time between output neuron spikes.
Therefore, with any other than the reduced NN learning rule, the input neurons will
experience a decrease in weight a lot more often (every time an input neuron spikes)
than an increase in weight (every time the postsynaptic neuron spikes). This leads
to a strong overall depression of the synaptic weights in the first few seconds of the
simulation. With the parameters specified in Masquelier, Guyonneau, and Thorpe
[6] and an ATA or a conventional NN learning rule, the output neuron stops firing
after a few seconds because the output neuron voltage does not reach the voltage
thresholdnecessarytoevokeanoutputneuronspikeanymore(seeFig.7). Inthecase
of the standard parameters, the output neuron stops firing after less than one second.
When no output neuron spikes occur, learning cannot take place and no specificity
can emerge.
In the case of an ATA learning rule, a behaviour resembling pattern finding can
be evoked under the right circumstances: reducing the learning rate by a factor of 5
and increasing the value of a + (the maximum weight increase) to double the value
of a(cid:0) (the maximum weight decrease). This setup works because the large amount
of depression (on every input spike) is counteracted by large potentiation (due to the
increased a + ). In such runs, the output neuron will correctly reach specificity and
trace back through the latency, but then starts firing outside of the pattern again.
This system is not stable since the ATA rule leads to “too much learning” as the
synaptic weights change after every single spike. A further reduction in the learning
| rule will | not result in | pattern | specificity |     | at all. |     |     |

We were unable to find parameters for the standard NN learning rule that allowed
j j j
ReScience rescience.github.io 6 - 7 Aug 2018 Volume 4 Issue 1


espanys rep thgiew egareva
|     |     | A   |     |     |     | B   |

|     | 0.5 |     |     | 0.5 |     | rNN |
NN
ATA
|     | 0.4                   |          |     | 0.4 |          |         |

|     | 0.3                   |          |     | 0.3 |          |         |
|     | 0.2                   |          |     | 0.2 |          |         |
|     | 0.0                   | 0.5      | 1.0 | 1   | 150      | 300 450 |
|     |                       | time [s] |     |     | time [s] |         |
|     |                       | C        |     |     |          | D       |
|     | ]sm[ ycnetal ekips 50 |          |     | 100 |          |         |
sekips tcerroc %

|     | 25  |     |     | 50  |     |     |

|     | 0      |             |      | 0   |          |         |

|     | 0 1000 | 2000        | 3000 | 0   | 150      | 300 450 |
|     |        | # discharge |      |     | time [s] |         |
Figure 7: Effect of learning rules on synaptic weights. A) Both the ATA and the NN rules lead
toaveryrapiddepressionofallsynapsesleadingtosilenceintheoutputneuron. B)Incontrast,
the average weight of all neurons declines at a much slower rate for the RNN rule. C) and D)
When tweaking the ATA rule (increasing a substantially) it is possible to achieve a behaviour
+
that resembles pattern finding. For a short amount of time the output neuron becomes specific
| to the | pattern, but loses | this ability again | and does | not regain | it. |     |

j j j
ReScience rescience.github.io 6 - 8 Aug 2018 Volume 4 Issue 1


for pattern finding, despite this rule exhibiting slower learning when compared to
the ATA rule. In the case of both the ATA and NN learning rules, it seems likely
that stable pattern finding relies on a precise balance of a
+
and a(cid:0), with runaway
potentiation or depression likely if the balance is wrong. By contrast, the RNN rule
is automatically balanced and is not subject to this issue.
Effect of learning rule at ∆t=0
The spike times of the output neuron are slightly different in the original study and
the replication. In the original study spike times of the input and output neurons
are not restricted to fixed multiples of the timestep, so it is extremely unlikely that
two neurons will spike at the same time. In Brian, the output neuron spikes at the
beginningofatimestepandwillthereforehappeninthesametimebinassomeinput
neuron spikes leading to a time difference between the spikes of ∆t = 0 where the
STDP rule is undefined. Brian treats all of the input neuron spikesin this time bin as
iftheyhappenedjustbeforetheoutputneuronspike(∆t<0,duetotheschedulingof
eventsinBrian)andwillthereforeincreaseallthoseweightsinsteadofincreasingsome
anddecreasingothers. Thishighernumberofpotentiationsmakesitmoredifficultfor
thesystemtosystematicallydepressunimportantweightsinordertobecomeselective
to the pattern.
If the learning rule is modified so that the change in synaptic weight reflects that
on average half the input neurons spike before the output neuron and the other half
afterwards (by adding the mean of LTP and LTDtraces), the pattern is found earlier,
ataround17sor850spikes(foratimestepof10(cid:0)4s)whichisclosetotheperformance
for smaller time steps (10(cid:0)6s) and the original paper (both 14 s or 700 spikes). This
modified learning rule was only used to determine the time until finding (Fig. 6).
This difficulty to depress non-relevant input neurons is the reason for the lower
success rate at a high pattern presentation frequency at large time steps (10(cid:0)4 s) as
seen in Fig. 5 A). The time until the pattern is found during this condition is notably
longer(>30sinsteadof20s)andpointstowardstowardsthedifficultiesofthesystem
to properly depress the synaptic weights of the non-pattern neurons.
EPSP shape
The kernels used in the original study simulate a gradual increase of the postsynaptic
neuronvoltageascanbeseeninFig.1. Otherstudiessometimesalsomodeltheeffect
of the presynaptic spike as an immediate jump in postsynaptic voltage instead of that
gradual increase. In this system, using an immediate increase in postsynaptic voltage
does not lead to stable pattern finding. This might have to to with the fact that the
kernel shape and the immediate increase exhibit slightly different spike times as seen
in Fig. 8.
When modelling the immediate voltage increase, one needs to set the magnitude
of the voltage increase (for Fig. 8 ∆u was set to 1.2). It is very difficult to find the
∆u that corresponds to the same amount of voltage increase from the kernel. If the
value of ∆u is too small, then the output neuron stops firing after a short period of
time without having gained specificity for the pattern. If the value for ∆u is too high
all input neurons are potentiated and the output firing rate rockets. For the scope of
this paper, no value for ∆u was found to induce a stable pattern finding behaviour.
Conclusion
We could successfully replicate the results from Masquelier, Guyonneau, and Thorpe
[6] - a neuron with STDP synapses could reliably find a repeating spike pattern and
afterwards spike only when the pattern is presented. The time when the pattern is
found depends on the time step size chosen for the simulation, whereas the success
ReScience j rescience.github.io 6 - 9 Aug 2018 j Volume 4 j Issue 1


0 20 40 60 80
times [ms]
].u.a[
laitnetoP
kernel
imm. increase
Figure8: ChoiceofEPSP.Forthesamepresynapticspikes,thepostsynapticvoltagebehavessim-
ilarly, but the postsynaptic spike time is slightly different (/home/ph416/Documents/ReScience-
submission/article/figures/fig8_kernel_vs_imm.pdf).
of reliably finding the pattern requires the precise learning rule and the shape of the
EPSPs. Reproducingthepaperwasmadeeasybythefactthatsimulationparameters
werestatedinthetextandthesourcecodewassharedbytheauthorsofthepaperon
request.
Introducing discrete time steps. To run the simulations in Brian, we intro-
duced discrete time steps. This did not affect pattern finding abilities (as long as the
timestepsare10(cid:0)4 sorsmaller),butitdidincreasethetimeuntilapatternwasfound
for large time steps (10(cid:0)4 s), but not for small time steps (10(cid:0)6 s).
We verified that the delay in pattern finding did not stem from either the deletion
of some input spikes (to avoid input neurons spiking twice in one time step) or the
spike timing being at the start of each 0.1 ms time bin. When we fed those modified
input spikes to the original implementation, the timing of finding the pattern was not
affected. The delay therefore stems from forcing the output neuron to spike at the
beginning of a time step and the associated consequences for STDP learning.
Running the simulations using discrete time steps does not negatively impact pat-
tern finding abilities, but delays pattern finding for large time steps due to a larger
number of potentiations.
Choice of learning rule. The learning rule used is one specific version of a NN
STDP rule, which was not clearly stated in the original article. The comparison with
other learning rules shows that the use of this particular learning rule enables the
pattern finding behaviour.
TheusageoftheRNNrulehastwointerestingconsequences. Firstly,itslowsdown
therateofsynapticweightchange,sinceitconsidersfewerspike-spikeinteractionsthan
other learning rules. This slows down overall weight changes significantly and gives
the system more time to learn the spike sequences of the pattern. Neurons that spike
together during the pattern will experience similar weight changes more often than
non-pattern neurons. Over the course of hundreds of output neuron spikes - until
pattern specificity arises - these synchronised weight changes lead to higher synaptic
weights for the pattern neurons than for the non-pattern neurons.
Secondly, for this particular input the restrictions of the RNN STDP rule lead to
the weights alternating between increase and decrease. The stabilising effect of this is
mostclearduringtheconvergedphase. Theoutputneurononlyspikeswhenapattern
is presented more or less at the same latency. The input neurons (which are forced to
spike at least once every 50 ms) reliably spike at least once before or after or both. In
the latter case the input neurons will always experience the same increase or decrease
in synaptic weight per output neuron spike disregarding small changes due to jitter
andnoise. Iftheinputneurononlyspikesonceperpattern,theneithertheincreaseor
decrease of weight will be nearly constant whereas the respective decrease or increase
ReScience j rescience.github.io 6 - 10 Aug 2018 j Volume 4 j Issue 1


in weight will be random. On average the weights of all input neurons will slowly
increase to 1 or decrease to 0 over time, resulting in a very stable system.
Choice of EPSP shape. It seems to be essential to use a kernel EPSP shape
since using immediate voltage increases as the effect of an input neuron spike does
not lead to learning of the pattern. This might be due to the difficulty in finding the
correct parameters that create an equivalent voltage increase. It seems likely that the
EPSP shape is responsible for the decrease in success, since small changes in output
neuron spike times also occur when using different time step sizes and do not affect
pattern finding abilities under standard conditions.
References
[1] Romain Brette et al. Simulation of networks of spiking neurons: A review of tools and
strategies. Dec. 2007. doi: 10.1007/s10827-007-0038-6. arXiv: 0611089 [q-bio]. url:
http://www.ncbi.nlm.nih.gov/pubmed/17629781%20http://www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC2638500.
[2] DeanV.BuonomanoandWolfgangMaass.“State-dependentcomputations:spatiotemporal
processingincorticalnetworks”.In:NatureReviewsNeuroscience10.2(Feb.2009),pp.113–
125. issn: 1471-003X. doi: 10.1038/nrn2558. url: http://www.nature.com/articles/
nrn2558.
[3] Jean-Marc Fellous et al. “Discovering spike patterns in neuronal responses.” In: The Jour-
nal of Neuroscience 24.12 (Mar. 2004), pp. 2989–3001. issn: 1529-2401. doi: 10.1523/
JNEUROSCI.4649-03.2004. url: http://www.ncbi.nlm.nih.gov/pubmed/15044538%
20http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=PMC2928855.
[4] Wulfram Gerstner and Werner M. Kistler. Spiking neuron models. Cambridge University
Press, 2002.
[5] Dan F M. Goodman and Romain Brette. The brian simulator. Sept. 2009. doi: 10.3389/
neuro.01.026.2009. url: http://journal.frontiersin.org/article/10.3389/neuro.01.026.2009/
abstract.
[6] Timothée Masquelier, Rudy Guyonneau, and Simon J. Thorpe. “Spike timing dependent
plasticityfindsthestartofrepeatingpatternsincontinuousspiketrains”.In:PLoSONE 3.1
(2008). issn: 19326203. doi: 10.1371/journal.pone.0001377.
[7] Abigail Morrison, Markus Diesmann, and Wulfram Gerstner. “Phenomenological models of
synaptic plasticity based on spike timing”. In: Biological Cybernetics 98.6 (2008), pp. 459–
478. issn: 03401200. doi: 10.1007/s00422-008-0233-1.
[8] Yifat Prut et al. “Spatiotemporal structure of cortical activity: properties and behavioral
relevance.” In: Journal of neurophysiology 79.6 (1998), pp. 2857–2874. issn: 0022-3077.
doi: 10.1126/science.1529342. url: http://www.snl.salk.edu/%7B~%7Dzador/PDF/
JNP2857.pdf.
[9] Marcel Stimberg et al. “Equation-oriented specification of neural models for simulations”.
In: Frontiers in Neuroinformatics 8 (2014), p. 6. issn: 1662-5196. doi: 10.3389/fninf.2014.
00006. url: http://journal.frontiersin.org/article/10.3389/fninf.2014.00006/abstract%
20http://www.ncbi.nlm.nih.gov/pubmed/24550820%20http://www.pubmedcentral.nih.
gov/articlerender.fcgi?artid=PMC3912318.
ReScience j rescience.github.io 6 - 11 Aug 2018 j Volume 4 j Issue 1

---
**Source PDF:** `2018_01_article.pdf`
