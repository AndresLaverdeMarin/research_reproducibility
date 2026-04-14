| Spike     | Timing |     | Dependent |     |     |            | Plasticity |     | Finds | the    | Start |     | of  |

| Repeating |        |     | Patterns  |     | in  | Continuous |            |     | Spike | Trains |       |     |     |
Timothe´eMasquelier1,2*,RudyGuyonneau1,2,SimonJ.Thorpe1,2
1CentredeRechercheCerveauetCognition,Universite´ Toulouse3,CentreNationaldelaRechercheScientifique(CNRS),Faculte´ deMe´decinede
Rangueil,Toulouse,France,2SpikeNetTechnologySARL,Prologue1LaPyre´ne´enne,Labe`ge,France
ExperimentalstudieshaveobservedLongTermsynapticPotentiation(LTP)whenapresynapticneuronfiresshortlybeforea
postsynapticneuron,andLongTermDepression(LTD)whenthepresynapticneuronfiresshortlyafter,aphenomenonknown
as Spike Timing Dependant Plasticity (STDP). When a neuron is presented successively with discrete volleys of input spikes
STDPhasbeenshowntolearn‘earlyspikepatterns’,thatistoconcentratesynapticweightsonafferentsthatconsistentlyfire
early,withtheresultthatthepostsynapticspikelatencydecreases,untilitreachesaminimalandstablevalue.Here,weshow
thattheseresultsstillstandinacontinuousregimewhereafferentsfirecontinuouslywithaconstantpopulationrate.Assuch,
STDPisabletosolveaverydifficultcomputationalproblem:tolocalizearepeatingspatio-temporalspikepatternembedded
inequallydense‘distractor’spiketrains.STDPthusenablessomeformoftemporalcoding,evenintheabsenceofanexplicit
timereference.Giventhatthemechanismexposedhereissimpleandcheapitishardtobelievethatthebraindidnotevolve
to use it.
Citation: MasquelierT,GuyonneauR,ThorpeSJ(2008)SpikeTimingDependentPlasticityFindstheStartofRepeatingPatternsinContinuousSpike
Trains.PLoSONE3(1):e1377.doi:10.1371/journal.pone.0001377
INTRODUCTION theoretical observation is in accordance with recordings in rat’s
|                      |     |        |     |           |              |     |         | hippocampus | showingthat | theso | called‘placecells’fire |     | earlier – |

| Electrophysiologists |     | report | the | existence | of repeating |     | spatio- |             |             |       |                        |     |           |
relativetothecycleofthethetaoscillationinhippocampus–after
| temporal | spike | patterns | with millisecond |     | precision, | both | in vitro |            |                |           |     |               |           |

|          |       |          |                  |     |            |      |          | the animal | has repeatedly | traversed | the | corresponding | area[19]. |
andinvivo,lastingfromafewtensofmstoseveralseconds[1–3].
|     |     |     |     |     |     |     |     | STDP has | also been | studied | in an oscillatory | mode, | and was |

Inthisstudyweassessthedifficultproblemofdetectingthem,and
showntobeabletoselectonlyphase-lockedinputsamongabroad
| suggest | how neurons | could | solve | it. The | problem |     | is made |     |     |     |     |     |     |

particularlydifficultwhenonlyafractionoftherecordedneurons population with random phases, turning the postsynaptic neuron
areinvolvedinthepattern.Fig.1illustratessuchasituation.There into acoincidence detector[20].
is a pattern of spikes (indicated by the red dots) that repeats at The mainlimitation of these studies istheassumption that the
inputspikesarriveindiscretevolleys(sometimesalsocalled‘spike
| irregular | intervals, | but is     | hidden | within the | variable   | background  |      |              |                          |             |              |                |               |

|           |            |            |        |            |            |             |      | waves’).     | They assume              | an explicit | time         | reference      | – usually the |
| firing of | the whole  | population | (shown | in         | blue).     | The problem | is   |              |                          |             |              |                |               |
|           |            |            |        |            |            |             |      | presentation | of a stimulus[15,17,18], |             |              | or the maximum | (or           |
| made hard | because    | nothing    | in     | terms of   | population | firing      | rate |              |                          |             |              |                |               |
|           |            |            |        |            |            |             |      | minimum)     | of an oscillatory        |             | drive[20,21] | – that         | allows the    |
characterizestheperiodswhenthepatternispresent,noristhere
anythingunusualaboutthefiringratesoftheneuronsinvolvedin specification of a time-to-first spike (or latency) for the afferents,
the pattern. In such a situation detecting the pattern clearly which could be used by the brain to encode information[22,23].
requires taking the spike times into account. However direct Activity between the volleys is assumed to be spontaneous and
comparison of each spike time to one another over the entire much weaker. Furthermore, many studies[15,17,20] also require
recordingperiodandacrosstheentiresetofafferentsisextremely thepatterntobepresentinallvolleysfortheSTDPtolearnit,that
isno‘distractor’volleysareinsertedbetweenpatternpresentations.
computationallyexpensive.Inthisarticlewewillseehowasingle
Butwhathappenswhenthepopulationofafferentsiscontinuously
neuronequippedwithSTDPcansolvetheprobleminadifferent
firingwithaconstantpopulationfiringrate,sothatnoexplicittime
manner,takingadvantageofthefactthatapatternisasuccession
of spike coincidences. reference is available? Is STDP still able to find and learn spike
STDP is now a widely accepted physiological mechanism of patterns among the inputs? Is the learning robust if, more
| activity-driven | synaptic |     | regulation. | It has | been | observed | exten- |     |     |     |     |     |     |

sivelyinvitro[4–7],andmorerecentlyinvivoinXenopus’svisual
system[8,9], in the locust’s mushroom body[10], and in the rat’s AcademicEditor:OlafSporns,IndianaUniversity,UnitedStatesofAmerica
visual cortex[11] and barrel cortex[12]. An exponential update Received October 8,2007;AcceptedDecember7,2007;PublishedJanuary2,
2008
| rule fits | well the | synaptic | modifications |     | observed | experimental- |     |     |     |     |     |     |     |

ly[13] (see Fig. 2). Very recently, it has also been shown that Copyright: (cid:1) 2008 Masquelier etal. Thisis an open-access article distributed
cortical reorganization in cat primary visual cortex is in under the terms of the Creative Commons Attribution License, which permits
accordance with STDP[14]. Note that STDP is in agreement unrestricted use, distribution, and reproduction in any medium, provided the
originalauthorandsourcearecredited.
| with Hebb’s | postulate | because | it  | reinforces | the connections |     | with |     |     |     |     |     |     |

thepresynapticneuronsthatfiredslightlybeforethepostsynaptic Funding: This project was supportedby the CNRS, STREP Decisions-in-Motion
neuron, which are those that ‘took part in firing it’. It thereby (IST-027198), ANR projects Natstats and Hearing in Time, and SpikeNet
| reinforces | causality | links. |     |     |     |     |     | TechnologySARL. |     |     |     |     |     |

Whenaneuronispresentedsuccessivelywithsimilarvolleysof Competing Interests: The authors have declared that no competing interests
exist.
| input spikes | STDP    | is known     | to have | the          | effect of | concentrating |          |     |     |     |     |     |     |

| synaptic     | weights | on afferents | that    | consistently | fire      | early,        | with the |     |     |     |     |     |     |
*Towhomcorrespondenceshouldbeaddressed.E-mail:timothee.masquelier@
| result that | the postsynaptic |                   | spike | latency | decreases[15–18]. |     | This | alum.mit.edu |     |     |         |              |           |

| PLoSONE     |                  | | www.plosone.org |       |         |                   |     |      | 1            |     |     | January | 2008 | Issue | 1 | e1377 |


tnereffa #

)zH( etar gniriF
| 100 |     |     | 0 50 | 100 |     |     |     |     |     |

Firing rate (Hz)


| 0 0.1 | 0.2 0.3 | 0.4 0.5 | 0.6 |     |     |     |     |     |     |

t (s)
Figure1.Spatio-temporalspikepattern.Hereweshowinredarepeating50mslongpatternthatconcerns50afferentsamong100.Thebottom
panelplotsthepopulation-averagedfiringratesover10mstimebins(wechose10msbecauseitisthemembranetimeconstantoftheneuronused
laterinthesimulations),anddemonstratesthatnothingcharacterizestheperiodswhenthepatternispresent.Therightpanelplotstheindividual
firingratesaveragedoverthewholeperiod.Neuronsinvolvedinthepatternareshowninred.Again,nothingcharacterizesthemintermsoffiring
rates.Detectingthepatternthusrequirestakingthespiketimesintoaccount.
doi:10.1371/journal.pone.0001377.g001
realistically, pattern presentations occur at unpredictable times, population of 2,000 afferents firing continuously for 450s (see
separated by long ‘distractor’ periods and if the pattern does not Materials and Methods for details). Most of the time (3/4 of the
involvealltheafferents?Doesitmakesensetousethebeginningof
|     |     |     | time in the | baseline | simulation) | the | afferents | fired | according to a |

the pattern as a time reference, and does the postsynaptic spike Poisson process with variable instantaneous firing rates. Spiking
latencywithrespecttothisreferencestilldecrease? activity in the brain is usually assumed to follow roughly Poisson
To answer these questions we inserted an arbitrary pattern at statistics,hencethischoice,buthereitisnotcrucial:whatmatters
varioustimesintorandomly generated‘distractor’spiketrains,as isthattheafferentsfirestochasticallyandindependently.Butevery
in Fig 1, and investigated whether a single receiving STDP now and then, at random times, half of these afferents left the
neuron,witha10msmembranetimeconstant,wasabletolearn stochastic mode for 50ms and adopted a precise firing pattern.
it in an unsupervised manner. To be precise, we simulated a This repeated pattern had roughly the same spike density as the
|     |     |     | stochastic    | distractor | part,      | so as to | make   | it invisible  | in terms of |

|     |     |     | firing rates. | To         | be precise | the      | firing | rate averaged | over the    |
0.03
|     |     |     | population | and | estimated | over 10ms | time | bins | has a mean of |

0.02 64Hzandastandarddeviationoflessthan2 Hz(thisfiringrateis
evenmoreconstantthaninthe100afferentcaseofFig.1because
0.01 of the law of large numbers). We further increased the difficulty
w ∆ by adding a permanent 10Hz Poissonian spontaneous activity

|     |     |     | to all the | neurons, | and by | adding | a 1 ms | jitter | to the pattern. |

−0.01 Intriguingly, we will see that one single Leaky Integrate-and-Fire
|     |     |     | (LIF) neuron | receiving | inputs | from | all the | afferents, | acting as a |

−0.02 coincidence detector (see Fig. 3), and implementing STDP, is
|     |          |     | perfectly   | able         | to solve     | the problem |          | and learns | to respond |

|     |          |     | selectively | tothestartof | therepeating |             | pattern. |            |            |
| −50 | 0 50 100 |     |             |              |              |             |          |            |            |
∆ t (ms)
RESULTS
Figure 2. The STDP modification function. We plotted the additive At the beginning of a first simulation the 2,000 synaptic weights
weightupdatesasafunctionofthedifferencebetweenthepresynaptic are all equal to 0.475 (arbitrary units normalized in the range
spiketimeandthepostsynapticone.Weusedanexponentiallaw(see
Materials and Methods). The left part corresponds to Long Term [0,1]).Theneuronisthereforenon-selective.Sincethepresynaptic
Potentiation(LTP)andtherightparttoLongTermDepression(LTD). spike density – on its 10ms time scale – is almost constant, it
doi:10.1371/journal.pone.0001377.g002 discharges periodically (see Fig. 4a). The greater are the initial
| PLoSONE | www.plosone.org |     |     | 2   |     |     |     | January | 2008 | | Issue 1 | e1377 |

−1
−2
−3
0 10 20 30 40 50 60 70 80
t(ms)
weights(orthelowerthethreshold),thesmalleristheperiod(here reinforcestheconnectionswiththepresynapticneuronsthatfired
itisabout16ms,theinitialfiringrateisthusabout63Hz).Each slightly before in the pattern. As a result next time the pattern is
timeadischargeoccursweupdate thesynapticweightsusingthe presentedtheneuronisnotonlymorelikelytodischargetoit,but
STDPruleofFig.2,andclipthemintherange[0,1].Atthisstage, it will also tend to discharge earlier. In other words, the
the neuron discharges both outside and inside the pattern postsynapticspikelatencylocksitselftothepatternanddecreases
(represented by grey rectangles on Fig. 4). In the first case steadily(withrespecttothebeginningofthepattern).However,it
presynaptic and postsynaptic spike times are uncorrelated, and cannot decrease endlessly. There is a convergence by saturation
since a2t2.a+t+ (where a2 and t2 are respectively the LTD when all the spikes in the pattern that precede the postsynaptic
learning rate and time constant, and a+ and t+ are the same spike already correspond to maximally potentiated synapses, and
parameters forLTP, see Materials and Methods), STDP leads to allarenecessarytoreachthethreshold.Thisusuallyoccurswhen
an overall weakening of synapses[15] (note: if no repeating the latency is already very short, the value depending on the
patterns were inserted STDP would thus gradually decrease the threshold,althoughitcouldoccurevenearlierifthepatternhasa
synaptic weights until the threshold would not be reached any zone with low spike density. Spikes outside the pattern cannot
longer). But in the second case, by reinforcing the synaptic contributeefficientlytothemembranepotential:sincetheirtimes
connectionswiththeafferentsthattookpartinfiringtheneuron, are stochastic, STDP usually depresses the corresponding
STDP increases the probability that the neuron fires again next synapses. We end up with a bimodal weight distribution with
timethepatternispresented(reinforcementofcausalitylink).Asa synapses either maximally potentiated or fully depressed (as
result, selectivity to the pattern emerges, here after about 13.5s predicted by vanRossum etal[24]).
(see Fig. 4b)that isafter only about 70pattern presentations and Here this convergence occurs after about 2000 discharges. At
700discharges:theneurongraduallystopsdischargingoutsidethe this stage, the postsynaptic spike latency (with respect to the
pattern(nofalsealarms),whileitdoesdischargemostofthetime beginning of the pattern) is about 4 ms (see Fig. 4c). After
when the pattern is presented (high hit rate), and can even fire convergence the hit rate is then 99.1% with no false alarms
twiceperpatternasinthecaseillustratedhere.Chancedetermines (estimatedonthelast150s).Noticethatthesignal/noiseratiohas
whichpart(s)ofthepatterntheneuronbecomesselectivetoatthis increased with respect to the situation in Fig. 4b, that is the
stage (i.e. the postsynaptic spike latency(ies), with respect to the potential reached on distractor periods is farther from the
beginning of the pattern here about 5 ms and 40ms). However threshold. Among the 2,000 synapses, 383 are fully potentiated
the increase in selectivity usually rapidly leads to only one (weight<1),whiletherestofthemarealmostcompletelydepressed
discharge per pattern, here at about40ms. (weight<0).Allofthepotentiatedsynapsescorrespondtoafferents
OnceselectivitytothepatternhasemergedSTDPhasanother involved in the pattern. The fact that there is no false alarms
major effect. Each time the neuron discharges in the pattern, it meansoncethelearninghasbeendone,aneuronjustwaitsforits
)stinu
yrartibra(


potential
threshold
resting pot.
input spike times
Figure3.LeakyIntegrate-and-Fire(LIF)neuron.Hereisanillustrativeexamplewithonly6inputspikes.Thegraphplotsthemembranepotentialas
afunctionoftime,andclearlydemonstratestheeffectsofthe6correspondingExcitatoryPostSynapticPotentials(EPSP).Becauseoftheleak,forthe
thresholdtobereachedtheinputspikesneedtobenearlysynchronous.TheLIFneuronisthusactingasacoincidencedetector.Whenthethreshold
isreached,apostsynapticspikeisfired.Thisisfollowedbyarefractoryperiodof1msandanegativespike-afterpotential.
doi:10.1371/journal.pone.0001377.g003
PLoSONE | www.plosone.org 3 January 2008 | Issue 1 | e1377

1000


0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
t (s)
preferredstimulus,andneedneverforgetwhatithaslearned.The We performed 100 similar simulations with different pseudo-
model thus predicts that fully specified neurons might actually randomly generated spike trains and patterns. Our criteria for a
have very low spontaneous rates, whereas higher rates might ‘successful’ simulation were: convergence to a state with a
characterize lesswell specified cells. postsynaptic latency inferior to10ms, a hit rate superior to98%
Fig.5showsthelatencyreduction(withrespecttothebeginning and no false alarms. This occurred in 96% of the cases. For the
of the pattern) during the learning stage until it stabilizes at a remaining 4%, the neurons stopped firing when too many
minimum of about 4 ms. Apart from the initial part (before discharges occurred outside the pattern in a row (leading to an
selectivity emerges) the curve looks similar to those observed in overall weakening of synapses, so the threshold was no longer
earlier work with discrete spike volleys[17]. By convention the reached).
latencyis0whentheneurondischargedoutsidethepattern,thatis We ran other batches of 100 simulations to systematically
whenitgeneratedafalsealarm.Therearenofalsealarmsafterthe investigate the impact on this 96% success performance of five
676thdischarge, that isforthelast 436sof simulation. parameters.
Fig.6 illustratesthesituationafterconvergence. Itcanbeseen Thefirstoneisthepatternrelativefrequency(i.esumofpattern
thatSTDPhaspotentiatedmostofthesynapsesthatcorrespondto durations over total duration ratio, assuming a fixed pattern
the earliest spikes of the pattern (Fig. 6a), and depressed most of duration of 50ms), 1/4 in the baseline condition, and Fig. 7a
the synapses that correspond to presynaptic spikes which follow showsitseffect.Weseethatwhiletheperformanceisveryhighas
thepostsynapticone,asinthepreviousworkwithdiscretevolleys longastheratioisabove15%,withsmallervaluestheprobability
[15,17,18]. This results in a sudden increase in membrane of success drops. This means the pattern needs to be consistently
potential when the neuron starts integrating the pattern, and the presentfortheSTDPtolearnit.However,thisappliesonlyatthe
thresholdisquicklyreached(Fig.6b).Noticethatallthesynaptic beginning (say during the first 1000 discharges). Here we used a
connections with afferents not involved in the pattern have been constantpatternfrequency,butaftertheinitialparttheneuronhas
completely depressed. already become selective to the pattern, so presenting longer
).u
.a(

a
potential
threshold
resting pot.
b
1000


13.3 13.4 13.5 13.6 13.7 13.8 13.9 14 14.1 14.2
t (s)
).u
.a(

c
1000


449 449.1 449.2 449.3 449.4 449.5 449.6 449.7 449.8 449.9 450
t (s)
).u
.a(


Figure4.Overviewofthe450ssimulation.Hereweplottedthemembranepotentialasafunctionofsimulationtime,atthebeginning,middle,and
endofthesimulation.Greyrectanglesindicatepatternpresentations.(a)Atthebeginningofthesimulationtheneuronisnon-selectivebecausethe
synapticweightsareallequal.Itthusfiresperiodically,bothinsideandoutsidethepattern.(b)Att<13.5s,afterabout70patternpresentationsand
700discharges,selectivitytothepatternisemerging:graduallytheneuronalmoststopsdischargingoutsidethepattern(nofalsealarms),whileit
doesdischargemostofthetimethepatternispresent(highhitrate),hereeventwice(c)Endofthesimulation.Thesystemhasconverged(by
saturation).Postsynapticspikelatencyisabout4ms.Hitrateis99.1%withnofalsealarms(estimatedonthelast150s).
doi:10.1371/journal.pone.0001377.g004
PLoSONE | www.plosone.org 4 January 2008 | Issue 1 | e1377


0 500 1000 1500 2000 2500
# discharges
)sm(
ycnetal
ekips
citpanytsoP

Figure5.Latencyreduction.Hereweplottedthepostsynapticlatencyasafunctionofthenumberofdischarges(byconventionthelatencyis0
whentheneurondischargedoutsidethepattern,i.e.whenitgeneratedafalsealarm).Weclearlydistinguish3periods:thebeginning,whenthe
neuronisnon-selective;themiddle,whenselectivityhasemergedandSTDPis‘trackingback’throughthepattern;andtheend,whenthesystemhas
convergedtowardsafastandreliablepatterndetector.
doi:10.1371/journal.pone.0001377.g005
Figure6.Convergedstate(a)werepresentedthespiketrainsofthe2,000afferents.WehavereorderedtheafferentswithrespecttoFig.1sothat
afferents1–1000areinvolvedinthepattern,andafferents1001–2000arenotandweuseacolorcoderangingfromblackforspikesthatcorrespond
tocompletelydepressedsynapses(weight=0)towhiteforspikesthatcorrespondtomaximallypotentiatedsynapses(weight=1).Thisallowsthe
visualizationofthespikeswhichgenerateasignificantEPSPandthosewhichdonot.Thepatternisrepresentedwithagreylinerectangle.Noticethe
clusterofwhitespikesatthebeginningofit:STDPhaspotentiatedmostofthesynapsesthatcorrespondtotheearliestspikesofthepattern.Note
thatvirtuallyallthesynapticconnectionswithafferentsnotinvolvedinthepatternhavebeencompletelydepressed.(b)Themembranepotentialis
plottedasafunctionoftime,overthesamerangeasabove.Weclearlyseethesuddenincreasethatcorrespondstotheabove-mentionedcluster.
doi:10.1371/journal.pone.0001377.g006
PLoSONE | www.plosone.org 5 January 2008 | Issue 1 | e1377


distractor periods does not perturb the learning at all. We also experimental values. But first after only 13s selectivity has
triedtochangethepatterndurationwhilemaintainingitsrelative emerged,andtheneuronfiresataratebetween5and10Hz.Itis
frequency at 1/4. It turns out that what makes the detection conceivablethatelectrophysiologistsrarelyrecordsuchshortvery
difficult is the delay between two pattern presentations, not the activeinitialphases.Second,weconsiderherethatthepopulation
ofafferentsisconstantlyfiringwithameanrateof64Hz.Thisisto
patterndurationitself.Sincewekeptthepatternrelativefrequency
constant, this delay increased with the pattern duration so the maketheproblemofpatterndetectionharder,butiftheafferents
performance dropped: 97% with a 40ms pattern, 96% with havelessactiveperiods,whichislikelytooccurinthebrain,sowill
50ms,93%with60ms,59%with100msand46%with150ms. have the post-synaptic neuron. We also added Gaussian noise to
However we think this delay is more naturally investigated by the initial weights, with increasing standard deviation until 0.475
changing thepattern relative frequency asin Fig.7a. (thusequaltothemean).Followingthisnoiseadditiontheweights
The second parameter we investigated is the amount of jitter were clipped in [0,1]. This had no significant impact on the
(1 ms in the baseline condition), and Fig. 7b shows its influence. performance, at least in the present case when the initial weights
| We see | that the performance |     | is very | good for | jitter levels | lower | are relatively | high. |     |     |     |     |     |

Thefifthparameteristheproportionofmissingspikes(0inthe
than3ms.Forlargeramountsofjitterthespikecoincidencesare
baselinecondition).Thethresholdwasscaledproportionally.Not
lost,andtheSTDPweightupdatesareinaccurate,sothelearning
is impaired. In the brain millisecond spiking precision has been surprisinglythenumberofsuccessfullylearnedpatternsdecreases
reported in many structures, including the retina[25,26], the with the proportion of spikes deleted. However with a 10%
Lateral Geniculate Nucleus[27,28], the visual cortex[29,30], the deletion the pattern was correctly learnt 82% of the time,
somatosensory system[31,32] and the auditory system[33]. Some demonstrating that thesystem isquite robust tospike deletion.
authors report higher variability, but this could result from non Wealsotriedchangingthemembranetimeconstantt (10 ms
m
controlled variables ratherthan intrinsicnoise(see Discussion). in the baseline condition), scaling the threshold proportionally.
|           |           |     |                |              |          |     | This had         | little impact | on the                           | performance |     | (79% success | with |

| The third | parameter | is  | the proportion | of afferents | involved | in  |                  |               |                                  |             |     |              |      |
|           |           |     |                |              |          |     | t =5 ms,88%witht |               | =20ms),butitdidhaveanimpactonthe |             |     |              |      |
the pattern (1/2 in the baseline condition), and Fig. 7c shows its m m
minimallatencythatisreachedafterconvergence.Asmallertime
| influence.  | The threshold   |     | was scaled | proportionally. | Not | surpris- |          |                  |           |     |           |          |            |

|             |                 |     |            |                 |     |          | constant | (and the smaller | threshold |     | that goes | with it) | causes the |
| ingly, with | fewer afferents |     | involved   | in the pattern, | it  | becomes  |          |                  |           |     |           |          |            |
hardertodetect,butitisstilldetectedmorethanhalfofthetimes neuron to be interested in more coincident spikes. The system
when only 1/3 of the afferents are involved in the pattern. Note converges when the very few nearly coincident first spikes of the
that the other 2/3 of afferents are discarded by STDP. This patternallcorrespondtomaximallypotentiatedsynapses,andthe
suggests that activity-driven mechanisms could select a small set postsynapticspikesisfiredjustafterthem.Thefinallatencyisthus
of ‘interesting’ afferents among a much bigger set of initially shorter than the onewe have with a longer time constant, which
enablestheneurontointegratespikesoveralongertimewindow.
connectedafferents,probablyspecifiedgenetically,aphenomenon
|              |                           |     |             |     |             |     | Taken          | together these | results   | demonstrate |                 | that the        | learning is |

| known        | as ‘developmental         |     | exuberance’ | for | which there | is  |                |                |           |             |                 |                 |             |
|              |                           |     |             |     |             |     | amazingly      | robust to      | the model | parameters. |                 | We thus believe | that        |
| considerable | experimentalevidence[34]. |     |             |     |             |     |                |                |           |             |                 |                 |             |
|              |                           |     |             |     |             |     | wehavecaptured | amechanism     |           | than        | emergesfromSTDP |                 | rather      |
Thefourthparameteristheinitialweight(0.475inthebaseline
thanfromapreciseneuralmodelconfiguration.Whileweadmitit
| condition) | and Fig. | 7d shows | its influence. | Recall | discharges |     |                   |             |     |           |      |           |           |

|            |          |          |                |        |            |     | is still somewhat | speculative |     | to affirm | that | a similar | mechanism |
outsidethepatternleadtoanoveralldecreaseofsynapticweights.
Iftoomanyofthemoccurinarowthethresholdmaynolongerbe takesplace in thebrain,it isat leastvery plausible.
| reachable. | Thus a        | high initial | value | for the weights  | increases | the      |            |     |     |     |     |     |     |

| resistance | to discharges | outside      | the   | pattern, leading | to        | a better | DISCUSSION |     |     |     |     |     |     |
performance. High initial weights also cause the neuron to Our first claim is that the main results previously obtained for
discharge at a high rate at the beginning of the learning process, STDPbasedlearningwiththehighlysimplifiedschemeofdiscrete
when it is non-selective: 63Hz for an initial weight of 0.475, spikevolleys[15–18]stillstandinthismorechallengingcontinuous
38Hz for 0.325. These values may seem high in regard to usual framework.Thismeansthatglobaldiscontinuitiessuchassaccades
|     | a   |     |     | b   |     |     | c   |     | d   |     |     | e   |     |

| 100 |     |     | 100 |     | 100 |     |     | 100 |     |     | 100 |     |     |
sseccus fo %
| 50  |     |     | 50  |     |     | 50  |     | 50  |     |     | 50  |     |     |

| 0   |     |     | 0   |     |     | 0   |     | 0   |     |     | 0   |     |     |
0.10.20.30.40.5 0 2 4 6 0.2 0.4 0.6 0.30.350.40.45 0 0.1 0.2 0.3
Pattern frequency Jitter (ms) Prop. of aff. in pattern Initial weight Spike deletion
Figure7.Resistancetodegradations(100trials).(a)Percentageofsuccessfultrialsasafunctionofthepatternfrequency(patternduration/thetotal
duration,givenafixedpatternlengthof50ms).Thepatternneedstobeconsistentlypresent,atleastatthebeginning,fortheSTDPtostartthe
learningprocess.(b)Percentageofsuccessfultrialsasafunctionofjitter.Forjittergreaterthan3msspikecoincidencesarelostandtheSTDPweight
updatesareinaccurate,sothelearningisimpaired(c)Percentageofsuccessfultrialsasafunctionoftheproportionofafferentsinvolvedinthe
pattern.Performanceisgoodifthisproportionisabove1/3(d)Percentageofsuccessfultrialsasafunctionoftheinitialweights.Withahighvalue
theneuroncanhandlemoredischargesoutsidethepattern.(e)Percentageofsuccessfultrialsasafunctionoftheproportionofspikesdeleted.With
a10%deletionthepatternwascorrectlylearntin82%ofthecases.
doi:10.1371/journal.pone.0001377.g007
| PLoSONE | | www.plosone.org |     |     |     |     |     | 6   |     |     | January |     | 2008 | Issue | 1 | e1377 |

or micro-saccades in vision and sniffs in olfaction[35], or brain the spike times. Some claim that spike times can be very reliable
oscillations in general[23] are not necessary for STDP-based whileothersaremoreskeptical(seeref[22,44]forreviews).Given
learning of temporal patterns (although they will almost certainly that the simple and cheap mechanism exposed here reliably
help).Temporalcodeskepticsoftenpointoutthefactthatneurons detectsspatio-temporalspikepatterns,itishardtobelievethatthe
|     |     |     |     |     |     |     | brain did | not evolve | to  | use at | least the | form of | temporal | coding |

wouldneedtoknowatimereferencetodecodeatemporalcode,
and we see here that this is not necessary: as long as there are exposed above (‘successive coincidences’), unless there is an
recurrent spike patterns in the inputs, and even if they are unavoidable intrinsic source of noise in the integrate-and-fire
embedded in equally dense ‘distractor’ spike trains, a neuron mechanismthatmakesallspiketimesunreliable.Themainsource
equippedwithSTDPcanpotentiallyfindtheminonlyafewtens for this sort of noise is probably at the level of synaptic
of pattern presentations, and will gradually respond faster and transmission[45], since neurons stimulated directly by current
fasterwhenthepatternispresented,bypotentiatingsynapsesthat injection in the absence of synaptic input give highly stereotyped
correspondtotheearliestspikesofthepatterns,anddepressingall and precise responses[46]. However, spike times can be very
the others. This last point strongly reinforces the idea that a reliable in some experiments[22,44], particularly in the auditory
substantialamountofinformationcouldbeavailableveryrapidly, cortex, proving that reliable synapses do exist. So we argue that
variabilityinotherrecordedspiketimes,inparticularinthevisual
| in theveryfirst | spikesevoked |     | bya | stimulus[36]. |     |     |     |     |     |     |     |     |     |     |

system,couldcomefromnon-controlledvariablesthatmightalso
Itisworthmentioningthattheproposedlearningschemeisfully
unsupervised. No teaching signal tells the neuron when to learn affect neuronal activation, such as attention, eye movements,
nor labels the inputs. Biologically plausible mechanisms for mental imagery, top-down effects etc. As Barlow wrote about
supervisedlearningofspikepatternshavealsobeenproposed[37]. neural responses in 1972, ‘‘their apparently erratic behavior was
It is also surprising to see how such a simple mechanism can caused by ourignorance, not theneuron’sincompetence.’’[47]
solve a problem as complex as spike pattern detection. However, We would like to emphasize the fact that the approach
thereisnoconsensusonthedefinitionofaspikepattern,andwe presented here is generic. It is not limited to sensory systems,
anditcouldbeappliedtoeitherexperimentalormodel-generated
admitoursisquitesimple:hereapatternisseenasasuccessionof
data.ThefirststepwouldbetoseeifSTDPfindsspikepatternsin
coincidences.ALeakyIntegrateandFire(LIF)neuronisknownto
thedata.Providingitdoes,thesecondstepwouldbetounderstand
| be capable  | of        | coincidence | detection, |              | and it has        | even been   |            |          |      |     |             |               |     |         |

|             |           |             |            |              |                   |             | what those | patterns | mean | by  | solving the | corresponding |     | inverse |
| proposed    | that this | is its main | function   | in           | the brain[38,39]. | Here        |            |          |      |     |             |               |     |         |
| themembrane | time      | constant(10 |            | ms)isshorter | than              | theduration | problem.   |          |      |     |             |               |     |         |
of the pattern (50 ms), and so the LIF neuron can never be What happens if there is more than one repeating pattern
selective to the whole pattern. Instead, it is selective to ‘one present in the input? We verified that as the learning progresses,
coincidence’ofthepatternatatime,thatis,selectivetothenearly the increasing selectivity of the postsynaptic neuron rapidly
simultaneous arrival of certain spikes, just as it occurs in one prevents it from responding to several patterns. Instead, it picks
subdivisionofthepattern.Atthebeginningofthelearningprocess one (chance determines which one), and becomes selective to it
|     |     |     |     |     |     |     | and only | to it. | To learn | the | other patterns |     | other neurons | are |

STDPwillcausetheLIFneurontobecomeselectivetoonesuch
needed.
coincidence(chancedetermineswhichone).ThenSTDPwilltrack
Acompetitivemechanismcouldensuretheyoptimallycoverall
| back through | the         | pattern,    | from | one coincidence |     | to the previous |               |          |     |       |          |          |       |        |

|              |             |             |      |                 |     |                 | the different | patterns | and | avoid | learning | the same | ones. | Such a |
| one, until   | the initial | coincidence |      | is reached      | and | the chain       | of            |          |     |       |          |          |       |        |
causalityisstopped.Atthispointtheneuronisselectiveonlytothe mechanism could be implemented through inhibitory horizontal
simultaneousarrivalofthepattern’searliestspikes,andcanserve connections between neurons, such that as soon as one neuron
as ‘earliest predictor’ of thesubsequent spike events[15,16,19], at fires,itcouldpreventothercellsfromlearningthesamepattern,as
theriskoftriggeringafalsealarmifthesesubsequenteventsdon’t in previous work[48]. The neural population would then self-
occur, butwith thebenefit ofbeing very reactive. organize to cover all the input patterns. The ‘coverage’ could be
|                |      |                 |           |           |                    |                  | optimized              | using              | neurons    | that      | differ   | in their        | parameters | (for |

| This contrasts |      | with approaches |           | where     | the whole          | pattern needs    |                        |                    |            |           |          |                 |            |      |
|                |      |                 |           |           |                    |                  | example                | their thresholds), |            | leading   | to more  | robust          | learning   | and  |
| to be taken    | into | account,        | sometimes | including |                    | finer structural |                        |                    |            |           |          |                 |            |      |
|                |      |                 |           |           |                    |                  | detection.Furthermorea |                    |            | longinput | pattern  | canbecodedbythe |            |      |
| aspects such   | as   | spike orders    | or        | relative  | delays[2,3,40,41]. |                  | But                    |                    |            |           |          |                 |            |      |
|                |      |                 |           |           |                    |                  | successive             | firings            | of several | STDP      | neurons, | each            | selective  | to a |
neuronalmechanismsabletoreliablydecodesuchstructureshave
differentpartofthepattern,andcompetitionwouldpreventthem
| to be proposed |     | and looked | for | in the | brain. | One appealing |     |     |     |     |     |     |     |     |

candidate mechanism isthesynfire chain[42] butdirect evidence all from tracking back through the pattern and clustering at the
for their existence is still fairly limited[43]. Here we limit the beginning. Note that within such a competitive framework a
notion of pattern to successive coincidences, and suggest a way patterndetectionprobabilityof50%ishardlyadisaster:itmeans
such patterns could be decoded, using widely accepted neuro- that with 2 neurons the risk that one pattern is not detected is
physiological mechanisms, namely coincidence detection and 25%,with3neurons12.5%,with4neurons6.25%andsoon.The
|     |     |     |     |     |     |     | system could | then | work | with suboptimal |     | parameters | (highlighted |     |

STDP.
|         |            |         |      |        |                 |         | inFig. 7),forexample |      |           | weakerinitial | weights. |           |                |     |

| Another | limitation | of this | work | is the | excitatory-only | scheme. |                      |      |           |               |          |           |                |     |
|         |            |         |      |        |                 |         | Further              | work | is needed | to            | evaluate | this form | of competitive |     |
Consequently,somethinglike‘afferentAmustnotspike’cannotbe
|              |           |           |     |               |     |          | network. | However | in this | paper | we wanted | to  | stress the | fact that |

| learnt, only | ‘positive | patterns’ |     | can. However, |     | evidence | for      |         |         |       |           |     |            |           |
onesingleLIFneuronequippedwithSTDPisconsistentlyableto
plasticityininhibitorysynapsesinthebrainisweakandinhibition
|                  |     |                      |     |       |         |           | detect one | arbitrary | repeating |     | spatio-temporal |     | spike | pattern |

| is often assumed |     | to be non-selective. |     | So we | propose | that most | of         |           |           |     |                 |     |       |         |
theselectivitycouldbeachievedusingonlyexcitatorysynapses,as embedded in equally dense ‘distractor’ spike trains, which is a
in thismodel. remarkable demonstration ofthepotential for sucha scheme.
Whetherspiketimescontainadditionalinformationwithrespect
|              |       |          |     |           |            |        | MATERIALS |     | AND | METHODS |     |     |     |     |

| to discharge | rates | has been | the | object of | an ongoing | debate | for       |     |     |         |     |     |     |     |
sometime.Electrophysiologistshavetriedtoanswerthisquestion The simulations were performed using MATLAB R14 (Math-
mostlybyrecordingneuronsinsensoryandmotorsystemswitha works 2005, Natick MA). The source code is available from the
repeatingstimulusoraction,andlookingatinter-trialvariabilityof authors uponrequest.
| PLoSONE |     | | www.plosone.org |     |     |     |     | 7   |     |     |     | January | 2008 | | Issue 1 | | e1377 |

Poisson spike trains onthemembranepotential.Eachpresynapticspikej,witharrival
timet,issupposedtoaddtothemembranepotentialanExcitatory
The spike trains were prepared before the simulation (Fig. 1 j
Post-Synaptic Potential (EPSP)of theform:
illustrates the type of spike trains we used, though with a smaller
set of neurons). For memory issues instead of using spike trains
definedovera450secondsperiod,wepastedthesame150slong e (cid:1) t{t (cid:2)~K: (cid:3) exp (cid:3) { t{t j (cid:4) {exp (cid:3) { t{t j (cid:4)(cid:4) :H (cid:1) t{t (cid:2)
pattern three times (this repetition had no impact on the results). j t t j
m s
Each afferent emits spikes independently using a Poisson process
with a variable instantaneous firing rate r, that varies randomly where t m is the membrane time constant (here 10ms), t s is the
between0and90Hz.Themaximalratechangeswaschosenso synapse time constant (here 2.5ms), H is the Heavyside step
thattheneuroncouldgofrom0to90Hzin50ms.Tobeprecise, function:
time was discretized using a time step dt of 1ms. At each time
step: (cid:5)1 if s§0
HðsÞ~
0 if sv0
1. theafferenthasaprobabilityofr.dtofemittingaspike(whose
exact dateisthenpicked randomly inthe1 mstimebin)
andKisjustamultiplicativeconstantchosensothatthemaximum
2. itsinstantaneousfiringrateismodified:dr=s.dtwheresisthe valueofthekernelis1(thevoltagescaleisarbitraryinthispaper).
speed of ratechange (inHz/s), andclipped in[0, 90]Hz. The last emitted postsynaptic spike i has an effect on the
3. its speed of rate change is modified by ds, randomly picked membrane potential modeled asfollows:
from a uniform distribution over [2360+360]Hz/s, and
clipped in [21800+1800] Hz/s (cid:3) (cid:3) t{t(cid:4)
gðt{tÞ~T: K :exp { i {
Notethatwechosetoapplytherandomchangetosasopposed i 1 t m
to r so as to have a continuous s function and a smoother r (cid:3) (cid:3) t{t(cid:4) (cid:3) t{t(cid:4)(cid:4)(cid:4)
function. K 2 : exp { t i {exp { t i :Hðt{t i Þ
m s
AsmentionedintheDiscussion,alimitationofthisworkisthe
excitatory-only scheme. Consequently, something like ‘afferent A whereTisthethresholdoftheneuron(here500,arbitraryunits).
mustnotspike’cannotbelearnt,only‘positivepatterns’can.We The first term models the positive pulse and the second one the
thuswantedapatterninwhichalltheafferentsspikeatleastonce. negative spike-afterpotential that follows the pulse (see Fig. 3).
Wecouldhavemadeupsuchapattern,butwewantedthepattern Here we used K =2 and K =4. For simplicity, the resting
1 2
tohaveexactlythesamestatisticsasthePoissondistractorpart(to potentialissupposedtobezero,butanonzerovaluewouldsimply
make the pattern detection harder), so we preferred to randomly shiftthekernel,andshiftingthethresholdbythesamevaluewould
pick a 50ms period of the original Poisson spike trains and to leadtothesame computation.
‘copy-paste’ it (see below). To make sure this randomly selected Both e and g kernels were rounded to zero when respectively
period did contain a spike from each afferent we implemented a t2t andt2t were greater than 7?t .
j i m
mechanism that triggers a spike whenever an afferent has been Atanytime themembrane potential is:
silent for more than 50ms (leading to a minimal firing rate of
20Hz). Clearly, such mechanism is NOT implemented in the p~gðt{tÞz X w:e (cid:1) t{t (cid:2)
brain. It is just an artifice we used here to make the pattern i j j
detection harder. As a result the average firing rate was 54Hz, j=tj wti
and not the 45Hz we would have without this additional
wherethew aretheexcitatorysynapticweights,between0and1
mechanism. j
(arbitrary units).
Once the random spike train has been generated, a part of it,
This SRM formulation allows us touse event-driven program-
definedasthe‘pattern’toberepeated,is‘copy-pasted’.This‘copy-
ming: we only compute the potential when a new presynaptic
paste’doesnotinvolvethelast1000afferents(obviouslytheindices
spike is integrated. We then estimate numerically if the
are arbitrary), which conserve their original spike trains. But we
corresponding EPSP will cause the threshold to be reached in
discretize the spike trains of the first 1000 afferents into 50ms
thefutureandatwhatdate.Ifitisthecase,apostsynapticspikeis
sections. We randomly pick one of these sections and copy the
scheduled. Such postsynaptic spike events cause all the EPSPs to
correspondingspikes.Thenwerandomlypickacertainnumberof be flushed, and a newt is used for theg kernel. There is then a
i
thesesections(1/4inthebaselinecondition),avoidingconsecutive
refractoryperiodof1ms,duringwhichtheneuronisnotallowed
ones, and replace the original spikes by the copied ones. A jitter
to fire.
was added before the pasting operation, picked from a Gaussian
distribution with mean zero and standard deviation 1 ms (in the
Spike Timing Dependent Plasticity
baseline condition).
An exponential update rule (see Fig.2):
After this ‘copy-paste’ operation a 10Hz Poissonian spontane-
ous activity was added, to all neurons and all the time. The total
activity was thus 64Hz on average, and spontaneous activity ( az:exp (cid:1)tj {ti (cid:2) if tƒt ðLTPÞ
represented about16% ofit. Dw j ~ {a{:exp t (cid:1) z {tj {ti (cid:2) j if i twt ðLTDÞ
t{ j i
Leaky Integrate and Fire (LIF) neuron (see Fig. 3) withthetimeconstantst+=16.8msandt2=33.7ms,providesa
For computational reasons we modeled the LIF neuron using reasonable approximation of the synaptic modification observed
Gerstner’s Spike Response Model (SRM)[16,49]. That is instead experimentally[13].We restricted the learning window to
of solving the membrane potential differential equation we used [t27?t+,t]forLTPandto[t,t+7?t2]forLTD.Foreachafferent,
i i i i
kernels tomodel the effect of presynaptic and postsynaptic spikes we also limited LTP (respectively LTD) to the last (first)
PLoSONE | www.plosone.org 8 January 2008 | Issue 1 | e1377


presynapticspikebefore(after)thepostsynapticone(‘nearestspike’ ACKNOWLEDGMENTS
| approximation). | We did not | take the effects | of  | finer triplet | of       |                 |                            |     |        |

|                 |            |                  |     |               | We thank | Rufin VanRullen | for reading the manuscript | and | making |
spikes[50] intoaccount.
|     |     |     |     |     | pertinent comments | and Pierre | Bayerl for his participation | in an | earlier |

stageofthisproject.
| It was    | found that small | learning rates | led to     | more robust |     |     |     |     |     |

|           | a+=0.03125       |                | a2=0.85?a+ |             |     |     |     |     |     |
| learning. | We used          | and            |            | Following   |     |     |     |     |     |
learning the weights were clipped to [0,1]. Note that all synapses Author Contributions
| remain excitatory: | there isno | inhibitioninall | these | simulations. |           |                  |                    |               |     |

|                    |            |                 |       |              | Conceived | and designed the | experiments: ST TM | RG. Performed | the |
experiments:TM.Analyzedthedata:TM.Wrotethepaper:STTMRG.
REFERENCES
1. FrostigRD,FrysingerRC,HarperRM(1990)Recurringdischargepatternsin 24. VanRossumMCW,BiGQ,TurrigianoGG(2000)StableHebbianLearning
multiplespiketrains.II.Applicationinforebrainareasrelatedtocardiacand from Spike Timing-Dependent Plasticity. The Journal of Neuroscience 20:
| respiratory | control during different | sleep-waking | states. | Biol Cybern | 62: 8812–8821. |     |     |     |     |

495–502. 25. BerryMJ2nd,MeisterM(1998)Refractorinessandneuralprecision.JNeurosci
| 2. Prut Y, | Vaadia E, Bergman | H, Haalman | I, Slovin | H, et al. (1998) | 18:2200–2211. |     |     |     |     |

Spatiotemporal structure of cortical activity: properties and behavioral 26. Uzzell VJ, Chichilnisky EJ (2004) Precision of spike trains in primate retinal
relevance.JNeurophysiol79:2857–2874. ganglioncells.JNeurophysiol92:780–789.
3. FellousJM,TiesingaPH,ThomasPJ,SejnowskiTJ(2004)Discoveringspike 27. Reinagel P, Reid RC (2000) Temporal coding of visual information in the
patternsinneuronalresponses.JNeurosci24:2989–3001. thalamus.JNeurosci20:5392–5400.
4. MarkramH,LubkeJ,FrotscherM,SakmannB(1997)Regulationofsynaptic 28. LiuRC,TzonevS,RebrikS,MillerKD(2001)Variabilityandinformationina
efficacybycoincidenceofpostsynapticAPsandEPSPs.Science275:213–215. neuralcodeofthecatlateralgeniculatenucleus.JNeurophysiol86:2789–2806.
5. Bi GQ, Poo MM (1998) Synaptic modifications in cultured hippocampal 29. BairW,KochC(1996)Temporalprecisionofspiketrainsinextrastriatecortex
neurons:dependenceonspiketiming,synapticstrength,andpostsynapticcell ofthebehavingmacaquemonkey.NeuralComput8:1185–1202.
type.JNeurosci18:10464–10472. 30. Buracas GT, Zador AM, DeWeese MR, Albright TD (1998) Efficient
6. ZhangLI,TaoHW,HoltCE,HarrisWA,PooM(1998)Acriticalwindowfor discrimination of temporal patterns by motion-sensitive neurons in primate
cooperationand competitionamong developing retinotectal synapses. Nature visualcortex.Neuron20:959–969.
395:37–44. 31. Johansson RS, Birznieks I (2004) First spikes in ensembles of human tactile
7. FeldmanDE(2000)Timing-basedLTPandLTDatverticalinputstolayerII/ afferentscodecomplexspatialfingertipevents.NatNeurosci7:170–177.
IIIpyramidalcellsinratbarrelcortex.Neuron27:45–56. 32. Boloori AR, Stanley GB (2006) The dynamics of spatiotemporal response
8. Vislay-MeltzerRL,KampffAR,EngertF(2006)Spatiotemporalspecificityof integrationinthesomatosensorycortexofthevibrissasystem.JNeurosci26:
| neuronalactivitydirectsthemodificationofreceptivefieldsinthedeveloping |     |     |     |     | 3767–3782. |     |     |     |     |

retinotectalsystem.Neuron50:101–114. 33. WehrM,ZadorAM(2003)Balancedinhibitionunderliestuningandsharpens
9. MuY,PooMM(2006)SpikeTiming-DependentLTP/LTDMediatesVisual spiketiminginauditorycortex.Nature426:442–446.
Experience-DependentPlasticityinaDevelopingRetinotectalSystem.Neuron 34. Innocenti GM, Price DJ (2005) Exuberance in the development of cortical
| 50:115–125. |     |     |     |     | networks.NatRevNeurosci6:955–965. |     |     |     |     |

10. CassenaerS,LaurentG(2007)HebbianSTDPinmushroombodiesfacilitates 35. UchidaN,KepecsA,MainenZF(2006)Seeingataglance,smellinginawhiff:
thesynchronousflowofolfactoryinformationinlocusts.Nature. rapidformsofperceptualdecisionmaking.NatRevNeurosci7:485–491.
11. Meliza CD, Dan Y (2006) Receptive-field modification in rat visual cortex 36. VanRullenR,ThorpeSJ(2001)Ratecodingversustemporalordercoding:what
induced by paired visual stimulation and single-cell spiking. Neuron 49: theretinalganglioncellstellthevisualcortex.NeuralComput13:1255–1283.
183–189. 37. Gutig R, Sompolinsky H (2006) The tempotron: a neuron that learns spike
12. JacobV,BrasierDJ,ErchovaI,FeldmanD,ShulzDE(2007)SpikeTiming- timing-baseddecisions.NatNeurosci9:420–428.
DependentSynapticDepressionintheInVivoBarrelCortexoftheRat.The 38. AbelesM(1982)Roleofthecorticalneuron:integratororcoincidencedetector?
| JournalofNeuroscience27:1271–1284. |     |     |     |     | IsrJMedSci18:83–92. |     |     |     |     |

13. BiGQ,PooMM(2001)Synapticmodificationbycorrelatedactivity:Hebb’s 39. KonigP,EngelAK,SingerW(1996)Integratororcoincidencedetector?The
postulaterevisited.AnnRevNeurosci24:139–166. roleofthecorticalneuronrevisited.TrendsNeurosci19:130–137.
14. Young JM, Waleszczyk WJ, Wang C, Calford MB, Dreher B, et al. (2007) 40. Frostig RD, Frostig Z, Harper RM (1990) Recurring discharge patterns in
Cortical reorganization consistent with spike timing–but not correlation- multiplespiketrains.I.Detection.BiolCybern62:487–493.
dependentplasticity.NatNeurosc10:887–895. 41. AbelesM,GatI(2001)Detectingprecisefiringsequencesinexperimentaldata.
15. SongS,MillerKD,AbbottLF(2000)Competitivehebbianlearningthrough JNeurosciMethods107:141–154.
spike-timing-dependentsynapticplasticity.NatNeurosci3:919–926. 42. AbelesM(1991)Corticonics:neuralcircuitsofthecerebralcortex.Cambridge;
16. GerstnerW,KistlerWM(2002)Spikingneuronmodels.CambridgeUniversity NewYork:CambridgeUniversityPress.ppxiv,280.
Press. 43. AbelesM(2004)Neuroscience.Timeisprecious.Science304:523–524.
17. GuyonneauR,VanRullenR,ThorpeSJ(2005)Neuronstunetotheearliest 44. SteinRB,GossenER,JonesKE(2005)Neuronalvariability:noiseorpartofthe
spikesthroughSTDP.NeuralComput17:859–879. signal?NatRevNeurosci6:389–397.
18. Masquelier T, Thorpe S (2007) Unsupervised Learning of Visual Features 45. MovshonJA(2000)Reliabilityofneuronalresponses.Neuron27:412–414.
throughSpikeTimingDependentPlasticity.PLoSComputBiol3. 46. Mainen ZF, Sejnowski TJ (1995) Reliability of Spike Timing in Neocortical
19. MehtaMR,QuirkMC,WilsonMA(2000)Experience-dependentasymmetric Neurons.Science268:1503–1506.
shapeofhippocampalreceptivefields[seecomments].Neuron25:707–715. 47. BarlowHB(1972)Singleunitsandsensation:aneurondoctrineforperceptual
20. Gerstner W, Kempter R, van Hemmen JL, Wagner H (1996) A neuronal psychology?Perception1:371–394.
learningruleforsub-millisecondtemporalcoding.Nature383:76–81. 48. Guyonneau R, VanRullen R, Thorpe SJ (2004) Temporal codes and sparse
21. HopfieldJJ(1995)Patternrecognitioncomputationusingactionpotentialtiming representations:akeytounderstandingrapidprocessinginthevisualsystem.
forstimulusrepresentation.Nature376:33–36. JPhysiolParis98:487–497.
22. VanRullenR,GuyonneauR,ThorpeSJ(2005)Spiketimesmakesense.Trends 49. GerstnerW(1995)Timestructureoftheactivityinneuralnetworkmodels.Phys
| Neurosci28:1–4. |     |     |     |     | RevE51:738–758. |     |     |     |     |

23. FriesP,NikolicD,SingerW(2007)Thegammacycle.TrendsNeurosci30: 50. Pfister J, Gerstner W (2006) Triplets of Spikes in aModel of Spike Timing-
309–316. DependentPlasticity.TheJournalofNeuroscience26:9673–9682.
| PLoSONE | | www.plosone.org |     |     |     | 9   |     | January 2008 | | Issue 1 | | e1377 |

---
**Source PDF:** `2018_01_article.pdf`
