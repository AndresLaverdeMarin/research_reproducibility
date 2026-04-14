|     |     | Fluctuation       | Domains    | in Adaptive |          | Evolution     |     |     |     |

|     |     | Carl Boettigera,∗ | , Jonathan | Dushoffb,∗  | , Joshua | S. Weitzc,d,∗ |     |     |     |
aCenter
|     |     | for Population | Biology, | University of | California, | Davis, United | States |     |     |

bDepartment
|     |         |     | of Biology, McMaster       | University,    | Hamilton, | ON,    | Canada |     |     |

|     | cSchool | of  | Biology, Georgia Institute | of Technology, | Atlanta,  | United | States |     |     |
|     | dSchool | of  | Physics, Georgia Institute | of Technology, | Atlanta,  | United | States |     |     |
0102 rpA 32  ]EP.oib-q[  1v3324.4001:viXra
Abstract
We derive an expression for the variation between parallel trajectories in phenotypic evolution, extend-
ingthewellknownresultthatpredictsthemeanevolutionarypathinadaptivedynamicsorquantitative
genetics. We show how this expression gives rise to the notion of fluctuation domains – parts of the
fitness landscape where the rate of evolution is very predictable (due to fluctuation dissipation) and
parts where it is highly variable (due to fluctuation enhancement). These fluctuation domains are
determined by the curvature of the fitness landscape. Regions of the fitness landscape with positive
curvature, such as adaptive valleys or branching points, experience enhancement. Regions with neg-
ative curvature, such as adaptive peaks, experience dissipation. We explore these dynamics in the
ecological scenarios of implicit and explicit competition for a limiting resource.
Keywords: Evolution, fitness landscapes, fluctuation dissipation, fluctuation enhancement, canonical
equation
1. Introduction
Fitness landscapes have long been an important metaphor in evolution. Wright (1931) origi-
nally introduced the concept to explain his result that the mean rate of evolution of a quantitative
trait is proportional to gradient of its fitness. The result and its accompanying metaphor continue
to arise in evolutionary theory, having been derived independently in quantitative genetics (Lande,
1979), game-theoretic dynamics (Hofbauer and Sigmund, 1998; Abrams, 1993), and adaptive dynam-
ics (Dieckmann and Law, 1996). The metaphor creates a deterministic image of evolution as the slow
and steady process of hill climbing. Other descriptions of evolution have focused on its more stochastic
elements – the random chance events of mutations and the drift of births and deaths that underlie the
process (Kimura, 1984, 1968; Ohta, 2002). In this manuscript, we seek to characterize the deviations
or fluctuations of evolutionary trajectories around the expected evolutionary path.
Our main result is that the size of deviations of evolutionary trajectories is determined largely by
the curvature of the evolutionary landscape whose gradient is determining the mean rate of evolution.
The landscape metaphor can be used to understand the interplay of stochastic and deterministic forces
by identifying regimes where the selection will counterbalance or enhance such stochastic fluctuations.
Because curvaturecanbepositive(concave up)ornegative (concave down), theevolutionary landscape
can be divided into domains where fluctuations are enhanced or dissipated. To make this more precise,
we focus on a Markov model of evolution used in the theory of adaptive dynamics. This Markov
| ∗ Corresponding | author. |     |     |     |     |     |     |     |     |

Email addresses: cboettig@ucdavis.edu (Carl Boettiger), dushoff@mcmaster.ca (Jonathan Dushoff),
| jsweitz@gatech.edu | (Joshua     | S.Weitz) |     |     |     |     |     |          |          |

| Preprint submitted | to Elsevier |          |     |     |     |     |     | November | 19, 2018 |

model gives rise to the familiar gradient equation – like that which first inspired the fitness landscapes
metaphor – and also a more precise statement of the fluctuation dynamics. The adaptive dynamics
framework is general enough that we can consider how these results apply in a variety of ecological
scenarios. We illustrate the surprising consequence of bimodal distributions of expected phenotypes
among parallel trajectories emerging from a fixed starting point on a single-peak adaptive landscape
due to fluctuation enhancement. We also provide a landscape interpretation that suggests how the
ideas of fluctuation dynamics apply to other ecological and evolutionary models.
2. Theoretical construction
Various definitions of fitness landscape have been used in the study of evolutionary dynamics.
The conventional idea postulates a mapping between trait values and fitness (Levins, 1962, 1964;
Rueffler et al., 2004). The difficulty with this conception is that, in many cases, fitness of a given
populationtypeis mediatedlargely throughcompetition withotherpopulations,andisthusdependent
on the current distribution of populations and their respective phenotypes in the environment. This
dependence on densities or frequencies turns the static fitness landscape into a dynamic landscape,
whose shape changes as the number of individuals, and their corresponding traits, changes.
It is possible to depict the fitness landscape that emerges even in the face of density- or frequency-
dependent competition by returning to Wright’s notion of a landscape. To do so, consider a resident
populationofindividualsinanenvironment,eachofwhichhaveanidenticaltraitvalue,i.e.,amonomor-
phic population. Next, consider the per-capita fitness of a small number of mutant individuals with a
similar, butdifferenttrait. Theper-capita fitness of mutants in the environment may belarger, smaller
or identical to the per-capita fitness of residents. The gradient in fitness around the trait represented
by the resident is termed the selective derivative (Geritz et al., 1997) in adaptive dynamics (analogous
to the selective gradient in quantitative genetics). The fitness landscape is defined by integrating over
these derivatives in trait space, to obtain a local picture of how fitness changes. In the limit of small,
slow mutation, it can be shown that the population will evolve as predicted by the shape of the land-
scape: by climbing towards a peak most rapidly when the slope is steep (Rueffler et al., 2004), see
Fig. 1 for three illustrative examples. The trait on the horizontal axis is that of the resident, not the
mutant. The lower panels show the slope of the mutant fitness as a function of the resident trait (up
to a multiplicative factor)– the slope of the mutant fitness changes as the resident trait changes. The
trait of the resident population evolves in the direction given by that slope. Integrating the lower panel
along the resident trait axis reveals the fitness landscape the resident trait climbs in an evolutionary
process(toppanels). Notethatchanges inthemutantfitnessarecapturedinthechangesinslopeofthe
landscape; the fitness landscape itself remains fixed. We derive the expected evolutionary dynamics
of the phenotypic trait of the resident and its variation among parallel trajectories in the following
sections.
2.1. Model
Consider a population monomorphic for a particular phenotypic trait, x. The abundance of the
population, N(x,t) of trait x, is governed by its ecological dynamics:
dN(x)
= f(x,N,E), (1)
dt
which may depend on the trait, population abundance, and the environmental conditions, E. The
evolutionary dynamics proceed in three steps (Dieckmann and Law, 1996; Champagnat et al., 2006).
∗
First, the population assumes its equilibrium-level abundance N (x), determined by its phenotypic
trait x. Next, mutants occur in the population at a rate given by the individual mutation rate µ times


therate of birthsat equilibrium, b(x). Themutant phenotype, y, is determinedby amutational kernel,
M(x,y). Thesuccessof themutantstrategy dependson theinvasion fitness, s(y,x), definedas theper-
capita growth rate of a rare population. Mutants with negative invasion fitness die off, while mutants
with positive invasion fitness will invade with a probability that depends on this fitness (Geritz et al.,
1997).
The invasion fitness is calculated from the ecological dynamics, Eq. (1), and will in general depend
on the trait x of the resident population as well as that of the mutant, y. We assume that a successful
invasion results in replacement of the resident (Geritz et al., 1997, 2002), and the population becomes
monomorphically type y. The details of this formulation can be found in Appendix Appendix A. The
important observation is that such a model can be represented by a Markov process on the space of
possible traits, x. The population can jump from any position x to any other position y at a transition
rate w(y x) determined solely by the trait values x and y. The probability that the process is at state
|
| x at time | t then | obeys | the | master | equation |     | for the | Markov | process, |     |     |

d
|     |     |     |     | P(x,t) | =   | dy  | [w(x y)P(y,t) |     | w(y | x)P(x,t)]. | (2) |

|     |     |     |     | dt     |     | Z   | |             |     | −   | |          |     |
No general solution to the master equation (2) exists. However, if the jumps from state x to state
y are sufficiently small (i.e., if mutants are always close to the resident), we can obtain approximate
solutions for P(x,t) by applying a method known as the Linear Noise Approximation (van Kampen,
2001), Appendix Appendix B. Doing so yields a general solution for the probability P(x,t) in terms
of the transition rates, w(y x), Eq. (B.10). The linear noise approximation derives a diffusion equation
|
as an approximation to the original jump process, as is commonly postulated. While this diffusion can
be written as a partial differential equation (PDE), following Kimura, or as a stochastic differential
equation, the solution for the probability density can be proven to be Gaussian and hence it suffices to
write down ordinary differential equations for the first two moments (Kurtz, 1971).
| 2.2. The | Fluctuation |     | Equation |     |     |     |     |     |     |     |     |

WeassumethemutationalkernelM(y,x)isGaussianinthedifferencebetweenresidentandmutant
traits, y x, with width σ and that mutations occur at rate µ. A more thorough discussion of these
µ
−
quantities can be found in Appendix Appendix A, where they are developed in the process of deriving
the transition probability w(y x) that specifies the underlyingMarkov process. Using Eq. (B.10) which
|
results from the systematic expansion of the master equation (2), the mean trait xˆ obeys
|         |          |          |     |         | dxˆ   | 1    |         |         |      |         |     |

|         |          |          |     |         | =     | µσ2N | ∗ (xˆ)∂ | s(y,xˆ) |      | a (xˆ), | (3) |
|         |          |          |     |         |       | µ    | y       |         | y=xˆ | 1       |     |
|         |          |          |     |         | dt    | 2    |         |         | | ≡  |         |     |
| with an | expected | variance |     | σ2 that | obeys |      |         |         |      |         |     |
∂σ2
|     |     |     |     |     |     | = 2σ2∂ | a (xˆ)+2 |     | 2σ a | (xˆ) . | (4) |

|     |     |     |     |     |     |        | xˆ 1     |     | π µ  | 1      |     |
|     |     |     |     |     | ∂t  |        |          | q   | |    | |      |     |
Eq. (3) recovers the familiar canonical equation of adaptive dynamics (Dieckmann and Law, 1996)
for the mean trait. Eq. (4), which describes the variance, we term the fluctuation equation of adap-
tive dynamics. The linear noise approximation (see Appendix Appendix B) also predicts that the
probability distribution itself is Gaussian, so that Eqs. (3) and (4) determine the entire distribution of
possible trajectories in this approximation. To illustrate the local behavior of the model, we define the
| fitness landscape |     | as  | L(x)= | x   | a (y)dy. |     |     |     |     |     |     |

R


| yd)y(       | yd)y(       | yd)y(       |

| 1a          | 1a          | 1a          |
| x 0         | x 0         | x 0         |
| (cid:243) ı | (cid:243) ı | (cid:243) ı |
| )x(         | )x(         | )x(         |
| 1a          | 1a          | 1a          |
−3 −2 −1 Trait, x 0 1 2 3 2 4 Trait, x 6 8 −0.5 Trait, x 0.0 0.5
(a) Implicit Resource (b) Chemostat (c) Branching
Figure 1: Fluctuation domains. The lower panels show the rate of evolution given by Eq. (3) vs. the resident
trait x for three ecological models: (a) implicit competition for a limiting resource (Section 4), (b) explicit resource
competition(AppendixAppendix C),and(c)symmetricbranchingfordimorphicpopulations(witharesidentpopulation
−x,
of trait x and another at Appendix Appendix E). The horizontal dashed lines in the lower panel denote where
a (x)=0, i.e.,the selective derivative is zero, and correspond to evolutionarily singular points, e.g., adaptive peaks and

valleys. Shaded and unshaded regions in the lower panels correspond to trait values for which fluctuations are enhanced
(shaded) and dissipated (unshaded). The adaptive landscape is defined as the integral of this expression (upper panels)
– where populations climb the hills at a rate proportional to their steepness. Note that the adaptive landscape for the
symmetric branchingcase has two peaks, and so evolutionary trajectories will lead to astable dimorphism.


3. Fluctuation Domains
A closer look at Eq. (4) will help motivate our geometric interpretation of fluctuation domains.
The approximation requires that the mutational step size σ is very small, hence the second term will
µ
almost always be much smaller than the first (except when the fluctuations σ themselves are also very
small). Note that the second term resembles the right-hand side of (3), differing only by a small scalar
constant and the fact that it is always positive. Interestingly, this means that the second term vanishes
at thesingularpointwherea (xˆ) = 0andσ2 = 0: fluctuations cannot beintroducedat anevolutionary

equilibrium. That the first term is the gradient of the deterministic (mean) dynamics and the second
term is smaller by a factor of the small parameter in the expansion are general features of the linear
noise approximation.
The first term of (4) implies that the variance σ2 will increase or decrease exponentially at a rate
determined by ∂ a (x); i.e., the curvature of the fitness landscape. This landscape and its gradient
x 1
are depicted in Fig. 1 for several ecological scenarios. Plotting the gradient itself makes it easier to see
when fluctuations will increase or decrease. On the gradient plot the singular point is found where the
curve crosses the horizontal axis.
In the neighborhood of a singular point corresponding to an adaptive peak, the slope is negative,
hencethefirstterminEq.(4)(thecoefficient ofσ2)isnegative andfluctuationsdissipateexponentially.
This means that two populations starting with nearby trait values will converge to the same trajectory.
Inthisregionnopathwillstochasticallydriftfarfromthemeantrajectory,hencethecanonicalequation
will provide a good approximation of all observed paths. We term the part of the trait-space landscape
where∂ a (x) < 0thefluctuation-dissipationdomain, analogous tothefluctuation-dissipation theorem
x 1
found in other contexts (van Kampen, 2001).
Farther from the singular point corresponding to an adaptive peak, ∂ a (x) becomes positive (see
x 1
Fig. 1(a) and Fig. 1(b)). While this part of trait-space still falls within the basin of attraction of the
singular point, the variance σ2 between evolutionary paths will grow exponentially. Initially identical
populations starting with trait values in this region will experience divergent trajectories due to this
enhancement. The variation can become quite large, with evolutionary trajectories that differ signifi-
cantly fromthemean. Wecallthisregionoftrait-space where∂ a (x) > 0thefluctuationenhancement
x 1
domain. Eventually trajectories starting in this region will be carried into the fluctuation-dissipation
domain, where they will once again converge.
Evolutionary branching points (Dieckmann and Doebeli, 1999; Geritz et al., 1998) provide another
example of a fluctuation enhancement domain. Until now, we have assumed that successful mutants
replace the resident population, a result known as “invasion implies substitution” (Geritz et al., 2002).
However, at an evolutionary branching point, the mutant invader no longer replaces the resident pop-
ulation, and the population becomes dimorphic. In dealing with monomorphic populations, we have
been able to describe the evolutionary dynamics in terms of the change of a single trait, describing
a single resident population. For dimorphic populations, two resident populations coexist, and both
influence the shape of the landscape. Thus, an invader’s fitness, s(y;x ,x ), and its rate of evolution,
1 2
a (x ,x ), will depend on how it performs against both populations. The evolutionary dynamics after
1 1 2
branching are two-dimensional and require a multivariate version of Eq. (4). Despite this, we can still
gain qualitative insight using the intuition that connects fluctuation domains to curvature.
The existence of the stable dimorphism fundamentally distorts the landscape. While the popu-
lation was monomorphic, being closer to the singular point always ensured a higher fitness. Once a
resident population sits on either side of a branchingpoint though, the singular pointbecomes a fitness
minimum. This description of evolution towards points which become fitness minima after branching
has been addressed extensively elsewhere (Geritz et al., 1997, 1998; Geritz, 2004). Here, what inter-
ests us is the effect of branching on fluctuations. If the landscape is smooth, a minimum must have


positive curvature and therefore must be an enhancement domain. The farther a mutant gets from the
branching point, the faster it can continue to move away, thus enhancing the initially small differences
between mutational jumps. A rigorous description of this effect would require a multivariate version of
Eq.(4)which is beyondthescopeof this paper. Instead, weillustrate theenhancement effect by taking
a slice of the two-dimensional landscape by assuming that the dimorphic populations have symmetric
trait values about the singular strategy, x 1 = x 2 = x. The fitness landscape for the case of symmetric
−
branching is shown in Fig 1(c), and the derivation provided in Appendix Appendix D. Note that
the region around the branching point is a fluctuation enhancement regime and the two new fitness
maxima far from the branching point are in fluctuation dissipation regimes.
To provideamoreconcrete illustration of thefluctuation dynamics, we willfocus on thedescription
of the ecological competition model and compare the theoretical predictions of Eq. (3) and Eq. (4) to
| point-process |         | simulations | of             | the Markov |         | process | (Gillespie, | 1977).      |     |     |

| 4. An         | Example |             | of Fluctuation |            | Domains |         | in Resource | Competition |     |     |
4.1. An Ecological Model of Implicit Competition for a Limiting Resource
The logistic model of growth and competition in which populations compete for a limited resource
is a standard model in ecological dynamics (Dieckmann and Doebeli, 1999). Here, we consider the
| population | dynamics |     | of N(x,t) | individuals |     | each | with trait | x:           |     |     |

|            |          |     |           | dN(x,t)     |     |      |            | N(y,t)C(x,y) |     |     |
y
|     |     |     |     |     | = rN(x,t) |     | 1            |      | ,        | (5) |

|     |     |     |     | dt  |           |     | (cid:18) − P | K(x) | (cid:19) |     |
wherer isthebirthrateand rN(y)C(x,y)/K(x)isthedensity-dependentdeathrate. Inthemodel,
y
K(x)istheequilibriumpopuPlationdensity andC(x,y)isafunctionwhichdescribestherelative change
indeathrateofindividualsoftypexduetocompetitionbyindividualsoftypey. GivenC(x,x) = 1,the
∗
equilibriumdensity of a monomorphicpopulation is N (x) = K(x). Following Dieckmann and Doebeli
| (1999) | we assume |     | the following | Gaussian |     | forms, |         |     |     |     |

|        |           |     |               |          |     |        | −x2/(2σ | 2), |     |     |
|        |           |     |               |          |     | K(x)   | = K e   | k   |     | (6) |

and
|     |     |     |     |     | C(x,y)= |     | e −(x−y)2/(2σ | 2), |     | (7) |

c
whereσ and σ are scale factors for theresourcedistribution andcompetition kernels respectively. We
|     | k   | c   |     |     |     |     |     |     |     |     |

focus on the case σ > σ , for which the model has a convergence-stable evolutionarily stable strategy
|     |     |     | c k |     |     |     |     |     |     |     |

(ESS) at x = 0 (Geritz et al., 1998). Having specified the ecological dynamics, we must also specify
the evolutionary dynamics, which we assume occur on a much slower time scale. We assume that with
probability µ an individual birth results in a mutant offspring, and that the mutant trait is chosen
from a Gaussian distribution centered at the trait value of the parents and with a variance σ2. From
µ
this we can assemble w(y x), and compute equations (3) and (4) (see Appendix Appendix B).
|
| 4.2. Numerical |     | simulation |     | of stochastic |     | evolutionary | trajectories |     |     |     |

Therearemanywaystorepresentevolutionaryecologymodelsinnumericalsimulations,includingfi-
nitesimulations,fast-slowdynamics,andpointprocesses(Dieckmann and Doebeli,1999;Nowak and Sigmund,
2004; Champagnat et al., 2006; Champagnat and Lambert, 2007). We choose to model the evolution-
ary trajectories of the ecological model in Eq. (5) by explicitly assuming a separation of ecological
∗
and evolutionary time scales. First, given a trait x, the ecological equilibrium density N (x) is deter-
mined. Then, the time of the next mutant introduction is calculated based on a Poisson arrival rate of


∗
µrN (x). In essence, we are assuming that ecological dynamics occur instantaneously when compared
to evolutionary dynamics. The trait of the mutant, y, is equal to x plus a normal deviate with variance
σ2. The mutant replaces the resident with probability given by the standard branching process result,
µ
1 d(y,x)/b(y,x) where d and b are the per-capita birth and death rate of the mutant, respectively,
−
so long as b > d, and with probability 0 otherwise. The ecological steady state is recalculated and the
process continues. Simulations are done using Gillespie’s minimal process method (Gillespie, 1977).
Estimates of the mean phenotypic trait xˆ and the variance σ2 are calculated from ensemble averages
of at least 105 replicates.
4.3. Comparison of Theory and Simulation
We consider simulations with three different initial conditions: starting within the fluctuation-
dissipation domain (x = 1), just into the fluctuation-enhancement domain (x = 2), and deep into the
fluctuation enhancement regime (x = 3) insuccessive rows inFig. 2. For each condition, thesimulation
is repeated 105 times and we compare the resulting distribution of trajectories to that predicted by
theory. In the first column we plot the numerically calculated mean path taken to the ESS (shown
in circles), and compare to the theoretical prediction of Eq. (3). In the second column, we plot the
variance between paths, and compare to the predictions of Eq. (4). As each replicate begins under
identical conditions, theinitial variance is always zero. Inthe thirdcolumn, wepresentthe distribution
of traits among the replicates at a single instant in time. We chose the moment of maximum variance
so that deviations from the theoretically predicted Gaussian kernel will be most evident.
4.3.1. Fluctuation-Dissipation Domain
Startingattheedgeofthedissipationdomain,fluctuationsgrowforonlyashorttimebeforerapidly
decaying, inthefirstrowofFig.2. Sincethesimulationissampledatregulartimeintervals,thevertical
spacingofpointsindicatetherateofevolution. Theoreticalpredictionsclosely matchsimulation results
for both the mean and variance, and the resulting distribution matches the theoretically predicted
Gaussian. The variance represents an almost negligible deviation from the mean trajectory.
4.3.2. Fluctuation-Enhancement Domain
Our second ensemble at x = 2 begins clearly within the fluctuation-enhancement domain. In the
second row of Fig. 2, the variance plot (center panel) begins by growing exponentially. Once the
population crosses into the dissipation domain, at x = 1, at about t = 1000, the variance peaks
and then dissipates exponentially. This transition appears as an inflection point in the mean path
(left panel). Though the variation now represents significant deviations, the distribution still appears
Gaussian (right panel).
4.3.3. Strong Fluctuations
InthethirdrowofFig.2,startingdeepwithinthefluctuation-enhancementdomainatx = 3,theory
andsimulationagreeinitially. Remaininglongenoughinthisdomain,fluctuationsareeventuallyonthe
same order of magnitude as the macroscopic dynamics themselves, and the linear noise approximation
underlying the theory begins to break down. The theory and simulation variance diverge, while the
mean path is substantially slower than predicted by the canonical equation. In the right panel, the
reason for this becomes clear. At this point in the divergence, the distribution is far from Gaussian,
rather it has become bimodal, with some replicates having reached the stable strategy at x = 0 and
others having hardly left the initial state.
The mechanism behind the emergence of bimdal probability distributions for trajectories can be
seen in the final row of Fig. 2. The theoretical trajectory predicted by Eq. (3) is sigmoidal, comprised
of slow change at the beginning and end and rapid evolution in the middle. Ecologically, this arises at


Mean Trait Path Variance Between Paths Snapshot of Path Distribution
210.0
8.0
|     | ^x ,tiarT naeM |     |     |     | 800.0 |     |     | 3   |     |     |

|     |     |     |     |     |  s ,raV tiarT |     |     | ytisneD |     |     |

|     | 4.0 |     |     |     | 400.0 |     |     |     |     |     |

000.0
0.0

|     |     | 0 500   | 1500 |     | 0   | 500     | 1500 |     | 0.2 0.4  | 0.6 0.8 |

|     |     | Time, t |      |     |     | Time, t |      |     | Trait, x |         |

0.2
5.1
5.1
|     | ^x ,tiarT naeM |     |     |     | 2 ,sraV tiarT |     |     |     |     |     |

ytisneD 0.1
40.0
0.1
5.0
5.0
00.0
|     | 0.0 |         |           |     |     |         |           | 0.0 |          |     |

|     |     | 0 1000  | 2000 3000 |     | 0   | 1000    | 2000 3000 |     | 0.5 1.0  | 1.5 |
|     |     | Time, t |           |     |     | Time, t |           |     | Trait, x |     |

0.3
0.2
|     | ^x ,tiarT naeM |     |     |     | 2 ,sraV tiarT |     |     | 4.0 |     |     |

0.2
ytisneD
|     |     |     |     |     | 0.1 |     |     | 2.0 |     |     |

0.1
|     | 0.0 |         |      |     | 0.0 |         |      | 0.0 |          |         |

|     |     | 0 4000  | 8000 |     | 0   | 4000    | 8000 |     | 0.0 1.0  | 2.0 3.0 |
|     |     | Time, t |      |     |     | Time, t |      |     | Trait, x |         |
Figure 2: Simulations over fluctuation domains. The dynamics of the mean path, variance between paths, and
snapshots of thetrait distribution in time for threeinitial conditions: x =1, x =2, and x =3 (top to bottom succes-
|     |     |     |     |     |     |     | 0   | 0   | 0   |     |

sively). Thethreerowscorrespondtotrajectoriesexperiencingfluctuationdissipation(tow)andfluctuationenhancement
(bottom) along with an intermediate case (middle). The mean (first column) and variance (second column) among trait
valuesareplottedovertime. Circlesaresimulationaveragesfrom105 replicatesandlinesaretheoreticalpredictions. The
finalcolumnshowsthetheoreticalGaussiandistribution(solidline)atthepointintimeindicatedbythedashedlineand
closedcircleinthefirsttwocolumns,andtheactualhistogram(circles)ofpositionsacrossthereplicatesatthattime. The
Parameters:
bottom rightpanelshows abimodal distributionamongreplicates inthecaseoffluctuationenhancement.
| σ2  | σ2=1.01, |       |              |      |     |     | 8   |     |     |     |

| =1, | c        | r=10, | σ µ =0.0005, | µ=1. |     |     |     |     |     |     |
k

the beginning from the small population size available to generate mutations, and at the end from the
weakening selection gradient. Populations with intermediate trait values hence experience rapid trait
evolution, giving rise to this transiently bimodal distribution. The theory provides insight into this
case of strongfluctuations intwo ways –first, itis drivenby theexistence of afluctuation-enhancement
domain, and second, it is anticipated by the theoretical prediction of fluctuations that are on the same
orderas themacroscopic dynamics. We observethat thesemacroscopic fluctuations can arisewhenever
the population remains long enough in the enhancement regime, independent of other model details.
The fluctuation equation for the explicit resource competition (chemostat) model shown in Fig. 1(b)
anddescribedinAppendixAppendix Cnever predicts fluctuationsthat reach macroscopic values, and
simulations of this system (not shown) do not produce bimodal trait distributions.
5. Discussion
The metaphor of fitness landscapes has been a powerful tool for understanding evolutionary pro-
cesses (Wright, 1932; Lande, 1979; Abrams, 1993; Dieckmann and Law, 1996). The concept of a land-
scape arises naturally from describing the rate of change of the mean trait as being proportional to
the evolutionary gradient. We extend this metaphor to understand fluctuations away from this mean,
whereouranalysis of aMarkov processrepresentation ofevolution intheadaptive dynamicsframework
brings us back to the notion of a fitness landscape. In this case, it is the curvature of that landscape
whichinformsthedynamicsofthesefluctuationsaway fromtheexpectedevolutionary path. Ourresult
linking landscape curvature to fluctuation domains is consistent with similar results from quantitative
genetics that relate the sign and magnitude of the quadratic selection coefficient in the Price equation
to increases or decreases in trait variation (Lande and Arnold, 1983; Chevin and Hospital, 2008).
Though the mathematical analysis of the Markov process is somewhat technical, the result is gen-
erally intuitive. Graphs such as Fig. 1 provide a visualization of how fluctuations will behave on the
landscape, while our fluctuation equation, Eq. (4), provides a more explicit description of those fluctu-
ations. This result, like the gradient expression itself, relies on the underlying randomness being small
relative to the scale of evolutionary change. We have seen how these approximations can break down
in the case of very large fluctuations, resulting in a bimodal distribution of phenotypes. While Eq. (4)
fails to describe this case accurately, it predicts the breakdown of the approximation by the explosion
of fluctuations. Though we have focused on the adaptive dynamics model of evolution, we hope that
the approach taken here can be extended to other landscape representations. Further, we hope that
our model will be broadly applicable to assessing the repeatability of evolution in experimental studies
of microbes and viruses (Wichman et al., 1999; Cooper et al., 2003) and in ecological studies of rapid
phenotypic change caused by biotic interactions (Duffy and Sivars-Becker, 2007) and/or anthropogenic
factors (such as over-fishing) (Olsen et al., 2005).
Inthiswork,wehavecomparedtheoreticalpredictionstonumericalsimulations. Evenwhenaclosed
form expression such as (4) exists for the deviations, some of the most dramatic examples in Fig. 2
emerge only when the diffusion approximation breaks down and stochastic forces become macroscopic.
In the spirit of scientifically reproducible research (Gentleman and Lang, 2007; Schwab et al., 2000;
Stodden, 2009), we freely provide all the source code required to replicate the simulations and figures
shown in the text. Though the numerical simulations are written in C for computational efficiency, we
provide a user interface and documentation by releasing all the code, figures, text, and examples as a
software package for the widely used and freely available R statistical computing language.


6. Acknowledgements
We thank Sebastian Schreiber for many helpful discussions, and also thank Michael Turelli, G´eza
Mesz´ena and an anonymous reviewer for comments. This work is funded in part by the Defense
Advanced Research Projects Agency under grant HR0011-05-1-0057. Joshua S. Weitz, Ph.D., holds
a Career Award at the Scientific Interface from the Burroughs Wellcome Fund. Carl Boettiger is
supported by a Computational Sciences Graduate Fellowship from the Department of Energy under
| grant number | DE-FG02-97ER25308. |     |     |     |     |     |     |     |     |     |

Appendix A. Adaptive Dynamics and the Transition Probability w(y|x)
In this appendix we construct the Markov process w(y x) under the assumptions of adaptive dy-
|
namics (Dieckmann and Law, 1996). The probability per unit time of making the transition in trait
space from a monomorphic population with trait x to one with trait y is given by
|     |     |     |     | w(y | x) = | (y,x) | (y,x). |     |     | (A.1) |

|     |     |     |     |     | |    | M     | D      |     |     |       |
In the framework presented here, a monomorphicpopulation of residents with trait x generate mutants
with trait y, some of which survive. The rate at which a mutation is generated from a population is
|     |     |     |     | (y,x) | = µ(x)b(x)N |     | ∗ (x)M(x,y), |     |     | (A.2) |

M
∗
whereb(x)istheper-capitabirthrateatequilibrium,µ(x)themutationprobabilityperbirth,N (x)the
equilibriumpopulationsizeforapopulationwithtraitx,andM(x,y)isthedistributionfromwhichthe
mutant trait is drawn. The probability of surviving accidental extinction of a branching process given
the mean individualbirthrate b and mean death rate d for themutant y is (y,x) = 1 d(y,x)/b(y,x)
D −
if d(y,x) < b(y,x) and (y,x) = 0 otherwise (Feller, 1968). The terms b(y,x) and d(y,x) refer to the
D
birth and death rate, respectively, of a rare mutant with trait y in an equilibrium population of x.
| Given a mutant |     | strategy | y   | such that | (y,x) | > 0 | we have |     |     |     |

D
∗
|     |     | w(y | x) =µ(x)N |     | (x)b(x)M(x,y)[b(y,x) |     |     | d(y,x)]/b(y,x). |     | (A.3) |

|     |     |     | |         |     |                      |     |     | −               |     |       |
Expanding the fitness, b(y,x) d(y,x), to first order the transition rate is then
−
∗
|     |     |     | w(y | x) µ(x)N | (x)∂ | s(y,x) | M(x,y)[y |     | x], | (A.4) |

|     |     |     |     |          |      | y      | y=x      |     |     |       |
|     |     |     |     | | ≈      |      |        | |        |     | −   |       |
where ∂ y s(y,x) y=x is known as the selective derivative (Geritz et al., 1997). From Eq. (A.4) one can
|
apply a particular model by specifying expressions for the mutation rate µ(x), stationary population
∗
size, N (x), fitness function s(y,x) and mutational kernel M(x,y). In the competition for a limited
| resource model, | (Dieckmann |     | and | Doebeli, | 1999) | used | here, these | are: |     |     |

|                 |            |     |     | µ(x)=    | µ,    |      |             |      |     |     |
−(y−x)2
|     |     |     |     | M(y,x) | =   | 1 e | 2σµ 2 , |     |     |     |

√2πσ2
µ
−(x−y)2
|     |     |     |     |         |     |     | ∗    | 2   |     |     |

|     |     |     |     |         |     | N   | (y)e | 2σc |     |     |
|     |     |     |     | s(y,x)= | r1 |     |      | ,  |     |     |
N∗(x)
−
|     |     |     |     |     |    |     |     |    |     |     |

|     |     |     |     |     |    |     |     |    |     |     |
− x2
|     |     |     |     | ∗     |       | 2.     |     |     |     |       |

|     |     |     |     | N (x) | = K 0 | e 2σ k |     |     |     | (A.5) |


Consequently, the evolutionary transition rates in for this model are given by
−(y−x)2
x2
|     |     |     |     |     |      |     | −     | rxe | 2σµ 2  |       |

|     |     |     |     |     |      |     | 2σ 2  |     |        |       |
|     |     |     |     | w(y | x) = | µK  | 0 e k |     | [y x]. | (A.6) |
|     |     |     |     |     | |    | −   |       | σ 2 | −      |       |
|     |     |     |     |     |      |     |       | k   | 2πσ2   |       |
µ
q
The transition rate w(y x) for the explicit resource competition model is presented along with the
|
model details in Appendix Appendix C. Using the appropriate transition rate in the linear noise
approximation described in Appendix Appendix B, we recover the equations for the curves plotted in
Fig. 1 which are integrated to obtain the theoretical predictions of Fig. 2. These explicit expressions
| are given | in Appendix |        | Appendix          |     | E.            |     |     |     |     |     |

| Appendix  | B.          | Linear | Noise             |     | Approximation |     |     |     |     |     |
| Appendix  | B.1.        | About  | the approximation |     |               |     |     |     |     |     |
The linear noise approximation is a common approach for describing Markov processes. Though
often applied in discrete cases such as one-step (birth-death) processes, it can be generalized to the
continuous case we consider, where a population at trait x can jump to another trait value y. The
approximation transforms the Markov process specified by a master equation on the transition rates
w(y x) to an approximate partial differential equation (PDE) for the probability distribution. This
|
PDE resembles the Fokker-Planck equation for the process1, except that the PDE resulting from the
linear noise approximation is guaranteed to be linear and its solutions Gaussian. Consequently, solving
for the two moments, the mean and variance, will lead to a system of ordinary differential equations.
Substitutingtheformof w(y x)foundinAppendixAppendix Aintothis ODEsystem recovers Eq.(3)
|
| and (4) | in the | text. |     |     |     |     |     |     |     |     |

The approximation is straight-forward (involving a change of variables and a Taylor expansion),
if cumbersome. The approximation is rigorously justified over any fixed time interval T in the limit
of small step sizes (Kurtz, 1971), which parallels more modern justification of the Canonical equa-
tion (Champagnat et al., 2001). The original derivation of the canonical equation makes use of (un-
scaled)jumpmoments, introducedbyvan Kampen(2001). Wereviewthisapproachfirst,asitprovides
a good intuition for the fulllinear noise approximation. Theactual approximation relies on a change of
variableswhichmakes explicituseofthesmallstepsizes, andderives ratherthanassumestheGaussian
| character | of the   | distribution. |             |         |            |        |           |           |     |       |

| Appendix  | B.2.     | Original      | jump        | moments |            |        |           |           |     |       |
| The       | dynamics | of            | the average |         | phenotypic |        | trait are | given     | by  |       |
|           |          |               |             |         |            | dxˆ(t) |           | d         |     |       |
|           |          |               |             |         |            |        | = dx      | x P(x,t). |     | (B.1) |
|           |          |               |             |         |            | dt     | Z         | dt        |     |       |
| Using the | master   | equation      |             |         |            |        |           |           |     |       |
d
|     |     |     |     | P(x,t) | =   | dy  | [w(x y)P(y,t) |     | w(y x)P(x,t)], | (B.2) |

|     |     |     | dt  |        |     | Z   | |             |     | − |            |       |
dP(x,t)
| to replace |     | and | performing |     | a   | change | of variables, |     | we find, |     |

dt
dxˆ(t)
|     |     |     |     |     | =   | dx  | dy[y | x]w(y | x)P(x,t). | (B.3) |

|     |     |     |     |     | dt  | Z   | Z    | −     | |         |       |
1Indeed,they are equivalent if transition rates are linear – in which case thePDE is also exact.


Defining the kth jump moment as a = (y x)kw(y x)dy, the dynamics can be written as,
k
|     |     |     |     |     |     | −   | |   |     |     |     |

R
dxˆ(t)
|     |     |     |     |     |     |     | = a (x) | .   |     | (B.4) |

|     |     |     |     |     |     | dt  | h 1     | i   |     |       |
It is by no means obvious if or when the deterministic path approximation a (x) a ( x ) is valid,
1 1
h i ≈ h i
as a 1 will often be nonlinear. The justification lies in the linear noise approximation. Proceeding as
| above, | we also find | an expression |     | for | the second | moment, |       |       |       |       |

|        |              |               |     |     | d x2(t)    |         |       |       |       |       |
|        |              |               |     |     | h i        | = 2 xa  | 1 (x) | + a 2 | (x) . | (B.5) |
|        |              |               |     |     | dt         | h       | i     | h     | i     |       |
Which again, we will only be able to solve by means of the linear noise approximation.
| Appendix | B.3. The | linear | noise | approximation |     |     |     |     |     |     |

To justify this step we will change into variables where we can have an explicit parameter ε that
relates to the step size. The trait x is approximated by an average or macroscopic value φ and a
deviation ξ that scales with the mutational step size ε; x = φ+εξ. Defining r y x expand the
≡ −
| transition | rate w(y | x) in | powers | of  | ε,  |     |     |     |     |     |

|     |     |     | w(y | x) = f(ε) | Φ   | (εx;r)+εΦ |     | (εx;r)+ε2Φ | +... , | (B.6) |

|     |     |     |     |           | 0   |           | 1   |            | 2      |       |
|
(cid:2) (cid:3)
where the Φ terms in the expansion are functions in which ε appears only in terms of εx. The function
f(ε) indicates that we can rescale the entire process by some arbitrary factor of ε since it can always
be absorbed into the timescale. We can then define the transformed jump moments as moments of Φ
| rather | than w, |     |     |     |       |     |     |          |     |       |

|        |         |     |     |     | α (X) | =   | rνΦ | (X,r)dr. |     | (B.7) |
|        |         |     |     |     | ν,λ   |     | λ   |          |     |       |
Z
The probability P(x,t) is expressed in terms of the new variables P(φ(t)+εξ,t) = Π(ξ,t), and the
| master | equation (2) | becomes: |     |        |      |       |        |     |     |     |

|        |              |          | ∂   |        |      | dφ ∂  |        |     |     |     |
|        |              |          |     | Π(ξ,τ) | ε −1 |       | Π(ξ,τ) |     |     |     |
|        |              |          | ∂τ  |        | −    | dτ ∂ξ |        |     |     |     |
−1 ∂
|     |     |     |     |     | = ε | α   | (φ(τ)+εξ) |     | Π(ξ,τ) |     |

1,0
|     |     |     |     |     | −   | ∂ξ  |     |     | ·   |     |

∂2

|     |     |     |     |     | +    | α (φ(τ)+εξ) |     | Π(ξ,τ) |     |     |

|     |     |     |     |     | 2∂ξ2 | 2,0         |     |        |     |     |
·
∂3

|     |     |     |     |     | ε   | α (φ(τ)+εξ) |     | Π(ξ,τ) |     |     |

∂ξ3 3,0
|     |     |     |     |     | −3! |     |     | ·   |     |     |

∂
(ε2),
|     |     |     |     |     | +ε α | (φ(τ)+εξ) |     | Π(ξ,τ)+ |     | (B.8) |

|     |     |     |     |     | ∂ξ   | 1,1       |     | ·       | O   |       |
ε2f(ε)t
where we have rescaled time by = τ. Expanding the jump moments around the macroscopic
| variable | φ,  |     |     |     |     |     |     |     |     |     |

|     |     |     |           |     |       |         | ′   | ε2ξ2α | ′′ ε3, |     |

|     |     | α   | (φ(t)+εξ) |     | α     | (φ)+εξα |     | +     | (φ) +  |     |
|     |     |     | ν,λ       |     | ≈ ν,λ |         | ν,λ | 2     | ν,λ O  |     |
(where primes indicate derivatives with respect to φ), and collecting terms of leading order in ε we
have:
dφ
|     |     |     |     |     |     | =   | α (φ), |     |     | (B.9) |

1,0
dτ


which is a completely deterministic expression. Substituting the form of w(y x) from (A.4) recovers
|
the canonical equation of adaptive dynamics, Eq. (3). Observe that the fluctuations are an order ε
ε0
smaller, demonstrating that this is indeed a consistent approximation. Collecting terms of order we
| have the | partial differential |     | equation |     |     |     |     |     |        |        |

|          |                      |     | ∂        |     |     | ∂   |     | 1   | ∂2     |        |
|          |                      |     | Π(ξ,τ)   | =   | α ′ | (φ) | ξΠ+ | α   | (φ) Π, | (B.10) |
|          |                      |     |          |     | 1,0 |     |     | 2,0 |        |        |
|          |                      |     | ∂τ       |     | −   | ∂ξ  |     | 2   | ∂ξ2    |        |
while all other terms are order ε or smaller. This is a partial differential equation for the evolution
of the probability distribution of traits. It is a linear Fokker-Planck equation, hence its solution is
Gaussian and Π(ξ,t) can be described to this order of accuracy by its first two moments,
∂ ξ
′
|     |     |     |     | h   | i = α | (φ) ξ | ,   |     |     |     |

|     |     |     |     | ∂t  |       | 1,0 h | i   |     |     |     |
ξ2
|     |     |     |     | ∂   |        | ′   |       |      |     |     |

|     |     |     |     | h   | i = 2α | (φ) | ξ2 +α | (φ), |     |     |
|     |     |     |     |     |        | 1,0 |       | 2,0  |     |     |
|     |     |     |     | ∂t  |        |     | h i   |      |     |     |
′
where prime indicates derivative with respect to the trait x. If α (φ) < 0 or the initial fluctuations
1,0
ξ 0 arezero, thefirstmomentcanbeignored,andthevarianceoftheensembleisgivenbytransforming
h i
| back into | the original | variables: |     |     |     |          |     |      |     |        |

|           |              |            |     | ∂σ2 |     | ′        |     |      |     |        |
|           |              |            |     | ε2  | =   | 2α (φ)σ2 | +α  | (φ). |     | (B.11) |
|           |              |            |     |     |     | 1,0      |     | 2,0  |     |        |
∂t
Transformingbetween thescaled variables andtheoriginal variables requirestheappropriatechoice
of ε. The assumption that mutational steps are small provides a natural choice: ε = σ . Substituting
µ
Eq. (A.4) to compute the jump moments, this recovers the fluctuation expression (4) in the text. Note
that even before we perform this substitution that (B.11) has the same form as (4); fluctuations grow
or diminish at a rate determined by the sign of the gradient of the deterministic equation, Eq. (B.9).
| Appendix | C. Chemostat |     | Model |     |     |     |     |     |     |     |

The graphical model for a second scenario is also displayed in Fig. 1. This scenario describes
competition and evolution with explicit resource dynamics for a chemostat system. We consider a
resource Q that flows in at rate D from a reservoir fixed at concentration Q . To retain constant

volume in the chemostat, both biotic and biotic components are flushed from the system at constant
rate D. The chemostat contains populations with N organisms, each of which take up nutrients at a
i
| rate g and | convert these | into | reproductive |     | output | with | efficiency |     | η , |     |

| i          |               |      |              |     |        |      |            |     | i   |     |
Q˙
|     |     |     |     |     | = DQ | DQ  | g(Q)N, |     |     | (C.1) |

|     |     |     |     |     |      | 0 − | −      |     |     |       |
|     |     |     |     | N˙  | = DN | +η  | g (Q)N | .   |     | (C.2) |
|     |     |     |     |     | i    | i   | i i    | i   |     |       |
−
Assume that the uptake of nutrients is governed by Michaelis-Mentin dynamics, and also that a
trade-off exists between efficiency of nutrient take-up and conversion (imagining greater investment in
| foraging | means less energy |     | available | for | reproduction), |             |     |     |     |     |

|          |                   |     |           |     | g(Q)           | = Q/(1+hQ), |     |     |     |     |
|          |                   |     |           |     | η(x)           | = x,        |     |     |     |     |
x2,
|     |     |     |     |     | h(x) | =   |     |     |     |     |

| where | the trait x | may differ | between | populations. |     |     |     |     |     |     |     |

The associated equilibrium population size for a population with trait x is
DQ¯
|     |     |     |     |         | DQ      |     |     | xD    |     |     |     |

|     |     |     |     | N¯(x) = | 0 −     | =   | xQ  |       | .   |     |     |
|     |     |     |     |         | g(Q¯,x) |     | 0   |       |     |     |     |
|     |     |     |     |         |         |     | −   | x x2D |     |     |     |
−
Similarly, the resource uptake of a mutant with trait y in an environment at an equilibrium set by a
| resident | type with | trait | x is given | by  |     |     |     |     |     |     |     |

(Q¯
|     |     |     |     | g   | y x ) = |     |       | ,   |     |     |     |

|     |     |     |     |     |         | x/D | x2+y2 |     |     |     |     |
−
| from which | we find | the | invasion | fitness | function | and its | gradient, |     |     |     |     |

y
|     |     |     |     | s(y,x) | =   |     |       |     | D,  |     |     |

|     |     |     |     |        |     | x/D | x2+y2 | −   |     |     |     |
−
D
2D2.
|     |     |     |     | ∂ y s(y,x) | y=x = |     |     |     |     |     |     |

|     |     |     |     |            | |     | x − |     |     |     |     |     |
Assuming a Gaussian mutation kernel and constant mutation rate, from Eq. (A.4) the transition
| rate function | w(y | x) is |     |     |     |     |     |     |     |     |     |

−(y−x)2
2σµ 2
|     |     |     |     |            | xD                   | D   |     | e        |      |     |       |

|     |     | w(y | x)  | µ xQ       |                      |     | 2D2 |          | [y   | x]. | (C.3) |
|     |     |     |     | 0          | x2D(cid:21)(cid:20)x |     |     |          |      |     |       |
|     |     |     | | ≈ | (cid:20) − | x                    |     | −   | (cid:21) | 2πσ2 | −   |       |
|     |     |     |     |            | −                    |     |     |          | µ    |     |       |
q
| Appendix | D. Branching |     | Model |     |     |     |     |     |     |     |     |

The model of implicit competition for a limiting resource, Eqs. (5)-(7), is well known to exhibit
the phenomenon of evolutionary branching when the competition kernel is narrower than the resource
distribution, σ < σ (Dieckmann and Doebeli, 1999). Once branching occurs, the invasion fitness of
|     | c   | k   |     |     |     |     |     |     |     |     |     |

a rare mutant is no longer given by s(y,x) as in Eq. (A.5), but instead depends on the trait values
of each of the coexisting residents x and x , as in s(y,x ,x ). This invasion fitness can still be
|     |     |     |     | 1   | 2   |     | 1   | 2   |     |     |     |

calculated directly from the competition model, Eqs. (5)-(7). This mutant can either arise from the
x or x population and replace it. If we assume x = x = x, we have the case of a symmetrically
| 1   | 2   |     |     |     |     | 1   | − 2 |     |     |     |     |

branching population. While many realizations of branching may be close to symmetric, this is but a
one-dimensional slice through a two-dimensional trait space (x ,x ). In this case, we can express the
1 2
equilibrium density of each resident species by K (x) = K(x)/(1+C(x, x)). We then consider the
res
−
| initial | per capita | growth | rate of | a rare mutant | with          | trait | y:   |     |           |          |       |

|         |            |        |         |               | K (x)C(x,y)+K |       |      | (   | x)C( x,y) |          |       |
|         |            |        |         |               | res           |       |      | res |           |          |       |
|         |            | s(y,x, | x)      | = r 1         |               |       |      | −   | −         | .        | (D.1) |
|         |            |        | −       | (cid:18)      | −             |       | K(y) |     |           | (cid:19) |       |
Thisreplacesthes(y,x)functionforthemonomorphicpopulation,andweproceedasbeforetocalculate
∗
a 1 (x) in Eq. (3). That is, we evaluate ∂ y s(y,x, x) at y = x, take K res (x) N (x) to recover a closed-
|     |     |     |     |     | −   |     |     |     | ≡   |     |     |

form slice of the branching landscape that is depicted in Fig. 1(c). The expression itself is given in the
| Appendix | Appendix | E,  | Eq. (E.3). |     |     |     |     |     |     |     |     |

| Appendix | E.  | Explicit | solutions |     | for | examples |     |     |     |     |     |

For the example logistic competition in a monomorphic population, the evolution of the mean trait
| x is given | by: |     |     |     |     |      |     |       |     |     |       |

|            |     |     |     |     | dx  | x    |     |       |     |     |       |
|            |     |     |     |     |     |      | 2K  | −x/2σ | 2   |     |       |
|            |     |     |     |     |     | =    | rµσ | e     | k . |     | (E.1) |
|            |     |     |     |     | dt  | −2σ2 | µ   | 0     |     |     |       |
k
| In Fig. 1, | we choose | parameters |     | such | that | rµK | σ2/2 = | 1 and | σ2 = | 1.  |     |

0 µ
k
| For the | chemostat: |     |     |     |     |     |     |      |     |       |       |

|         |            |     |     | dx  | 1   |     | D   |      |     |       |       |
|         |            |     |     | =   | µσ2 | Qx  |     | (D/x |     | 2D2). | (E.2) |
µ(cid:18)
|     |     |     |     | dt  | 2   | −   | 1 xD(cid:19) |     | −   |     |     |

−
µσ2
In Fig. 1, we choose parameters such that = 1, D = 0.1, and Q = 0.1.
µ
| And for | the symmetrically |     |     | dimorphic |     | population, |     |     |     |     |     |

|         |                   |     |     |           |     | −x2 4       | 1   |     | 2x2 |     |     |
−
|     |     |     |     | rµσ | 2K  | e 2 (cid:18)σ | c 2 σ 2(cid:19)(σ | 2+e      | σ 2 σ | 2 2σ 2)x |       |

|     |     |     | dx  |     | µ   | 0             | k                 | c        | c     | c k      |       |
|     |     |     |     | = − |     |               |                   |          |       | − .      | (E.3) |
|     |     |     | dt  |     |     |               |                   | 2        |       |          |       |
|     |     |     |     |     |     | 1+e2x2/σ      |                   | c 2 σ 2σ | 2     |          |       |
|     |     |     |     |     |     |               |                   | c        | k     |          |       |
|     |     |     |     |     |     | (cid:0)       |                   | (cid:1)  |       |          |       |
Theparameters for thedimorphicpopulation plot of Fig. 1are chosen such that rµK σ2/4 = 1, σ2 = 2
0 µ k
σ2
| and = | 1.  |     |     |     |     |     |     |     |     |     |     |
| ----- 
c
The right-hand side of each of these expressions is the function a (x) from the text, Eq. (3). This

function also determines the fluctuation dynamics by way of Eq. (4). The respective plots of a (x) are

σ2(t)
used in Fig. 1, while solving the ODEs for xˆ(t) and gives the theoretical predictions of Fig. 2.
References
Abrams, P., 1993. Evolutionarily unstable fitness maxima and stable fitness minima of continuous
| traits. | Evolutionary |     | Ecology | 7,  | 467–487. |     |     |     |     |     |     |

Champagnat, N., Ferriere, R., G., B. A., 2001. The canonical equation of adaptive dynamics: a math-
| ematical | view. | Selection | 1–2, | 73–83. |     |     |     |     |     |     |     |

Champagnat, N., Ferri`ere, R., Meleard, S., 2006. Unifying evolutionary dynamics: From individual
stochastic processes to macroscopic models. Theor. Pop. Biol. 69, 297–321.
Champagnat, N., Lambert, A., 2007. Evolution of discrete populations and the canonical equation of
| adaptive | dynamics. | Ann. | Appl. |     | Prob. | 17, 102–155. |     |     |     |     |     |

Chevin,L.,Hospital,F.,2008.Selectivesweepataquantitativetraitlocusinthepresenceofbackground
| genetic | variation. | Genetics |     | 180, | 1645–1660. |     |     |     |     |     |     |

Cooper, T., Rozen, D., Lenski, R., 2003. Parallel changes in gene expression after 20,0000 generations
of evolution in Escherichia coli. Proceedings of the National Academy of Sciences, USA 100, 1072–7.
Dieckmann, U., Doebeli, M., 1999. On the origin of species by sympatric speciation. Nature 400,
354–357.
Dieckmann, U., Law, R., 1996. The dynamical theory of coevolution: a derivation from stochastic
| ecological | processes. |     | J. Math. | Biol. | 34, | 579–612. |     |     |     |     |     |

Duffy, M., Sivars-Becker, L., 2007. Rapid evolution and ecological host-parasite dynamics. Ecology
| Letters | 10, 44–53. |     |     |     |     |     |     |     |     |     |     |

Feller, W., 1968. An Introduction to Probability Theory and Its Applications. Vol. 1. Wiley, New York.
Gentleman, R., Lang, D. T., 2007. Statistical analyses and reproducible research.
Geritz, S.,Gyllenberg,M., Jacobs,F.,Parvinen,K.,2002.Invasiondynamicsandattractor inheritance.
| Journal | of Mathematical | Biology | 44, 548–560. |     |

Geritz, S. A. H., 2004. Resident-invader dynamics and the coexistence of similar strategies.
| J. Math. | Biol. 50, | 67–82. |     |     |

Geritz, S. A. H., Kisdi, E., Mesz´ena, G., Metz, J. A. J., 1998. Evolutionarily singular strategies and
the adaptive growth and branching of the evolutionary tree. Evol. Ecol. 12, 35–57.
Geritz, S. A. H., Metz, J. A. J., Kisdi, E., Mesz´ena, G., 1997. The dynamics of adaptation and
| evolutionary | branching. | Phys. | Rev. Lett. 78, | 2024–2027. |

Gillespie, D., 1977. Exact stochastic simulation of coupled chemical reactions. Journal of Physical
| Chemistry | 81.25, 2340–2361. |     |     |     |

Hofbauer,J.,Sigmund,K.,1998.EvolutionaryGamesandPopulationDynamics.CambridgeUniversity
| Press, | Cambridge, | U.K. |     |     |

Kimura, M., 1968. Evolutionary rate at the molecular level. Nature 217, 624–626.
Kimura, M., 1984. Theneutral theory of molecular evolution. CambridgeUniversity Press, Cambridge,
UK.
Kurtz, T., 1971. Limit theorems for sequences of jump Markov processes approximating ordinary
| differential | equations. | Journal | of Applied Probability | 8, 344–356. |

Lande, R., 1979. quantitative genetic analysis of multivariate evolution, applied to brain: body size
| allometry. | Evolution | 33, 402–416. |     |     |

Lande, R., Arnold, S. J., 1983. The measurement of selection on correlated characters. Evolution 37,
1210–1226.
Levins, R., 1962. Theory of fitness in a heterogeneous environment. i. the fitness set and adaptive
| function. | The American | Naturalist | 96 (891), | 361–373. |

Levins,R.,1964.Theoryoffitnessinaheterogeneousenvironment.iii.theresponsetoselection.Journal
| of Theoretical | Biology | 7, 224–240. |     |     |

Nowak, M. A., Sigmund, K., 2004. Evolutionary dynamics of biological games. Science 303, 793–9.
Ohta, T., 2002. Near-neutrality in revolution of genes and gene regulation. Proc. Natl. Acad. Sci. 99,
16134–7.
Olsen, E., Lilly, G., Heino, M., Morgan, M., Brattey, J., Dieckmann, U., 2005. Assessingchanges in age
and size at maturation in collapsing populations of atlantic cod (Gadus morhua). Canadian Journal
| of Fisheries | and Aquatic | Sciences | 62, 811–823. |     |

Rueffler, C., Dooren, T. V., Metz, J., 2004. Adaptive walks on changing landscapes: Levins’ approach
| extended. | Theoretical | Population | Biology | 65, 165–178. |

Schwab, M., Karrenbach,M., Claerbout,J.,2000. Makingscientificcomputationsreproducible.Science
| and Engineering | 2   | (6), 61–67. |     |     |

Stodden, V., 2009. The legal framework for reproducible scientific research: Licensing and copyright.
| Computing | in Science | and Engineering | 11 (1), | 35–40. |

van Kampen, N., 2001. Stochastic Processes in Physics and Chemistry. Elsevier Science.
Wichman, H., Badgett, M., Scott, L., Boulianne, C., Bull, J., 1999. Different trajectories of parallel
| evolution | during viral | adaptation. | Science 285, | 422–424. |

Wright, S., 1931. Evolution in mendelian populations. Genetics 16, 97159.
Wright, S., 1932. The roles of mutation, inbreeding, crossbreeding and selection in evolution. In: Pro-
ceedings of the 6th International Congress of Genetics. Vol. 1. pp. 356–66.

---
**Source PDF:** `2020_26_article.pdf`
