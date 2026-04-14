| A Multi-Functional |     |            |     |     | Synthetic | Gene   | Network: | A Frequency |     |

| Multiplier,        |     | Oscillator |     |     | and       | Switch |          |             |     |
Oliver Purcell1*, Mario di Bernardo2,3, Claire S. Grierson4, Nigel J. Savery5
1Department of Engineering Mathematics, Bristol Centre for Complexity Sciences, University of Bristol, Bristol, United Kingdom, 2Department of Engineering
Mathematics,UniversityofBristol,Bristol,UnitedKingdom,3DepartmentofSystemsandComputerEngineering,UniversityofNaplesFedericoII,Napoli,Italy,4Schoolof
BiologicalSciences,UniversityofBristol,Bristol,UnitedKingdom,5SchoolofBiochemistry,UniversityofBristol,Bristol,UnitedKingdom
Abstract
Wepresentthedesignandanalysisofasyntheticgenenetworkthatperformsfrequencymultiplication.Ittakesoscillatory
transcriptionfactorconcentrations,suchasthoseproducedfromthecurrentlyavailablegeneticoscillators,asaninput,and
produces oscillations with half the input frequency as an output. Analysis of the bifurcation structure also reveals novel,
programmablemulti-functionality;inadditiontofunctioningasafrequencymultiplier,thenetworkisabletofunctionasa
switch or an oscillator, depending on the temporal nature of the input. Multi-functionality is often observed in neuronal
networks, where it is suggested to allow for the efficient coordination of different responses. This network represents a
| significant | theoretical | additionthatextends |     |     | the capabilitiesof | syntheticgenenetworks. |     |     |     |

Citation:PurcellO,diBernardoM,GriersonCS,SaveryNJ(2011)AMulti-FunctionalSyntheticGeneNetwork:AFrequencyMultiplier,OscillatorandSwitch.PLoS
ONE6(2):e16140.doi:10.1371/journal.pone.0016140
Editor:JeanPeccoud,VirginiaTech,UnitedStatesofAmerica
ReceivedAugust16,2010;AcceptedDecember13,2010;PublishedFebruary17,2011
Copyright: (cid:2)2011 Purcell et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits
unrestricteduse,distribution,andreproductioninanymedium,providedtheoriginalauthorandsourcearecredited.
Funding:FundingwasprovidedbytheEngineeringandPhysicalSciencesResearchCouncil(EPSRC).Thefundershadnoroleinstudydesign,datacollectionand
analysis,decisiontopublish,orpreparationofthemanuscript.
CompetingInterests:Theauthorshavedeclaredthatnocompetinginterestsexist.
*E-mail:enoep@bristol.ac.uk
Introduction developmentofnetworkswithprogrammablefunctionality.Further
|     |     |     |     |     |     | analysis | of the bifurcation structure | reveals that | our network is in |

Overthe past decadesyntheticbiologists haveengineered gene fact multi-functional, where the function is programmed by the
networkstoperformavarietyoffunctions[1–3],includingswitches temporal characteristics of the input. In addition to acting as a
| [4–8] and | oscillators | [6,9–13]. | Oscillators | have | been a focus | of  |     |     |     |

frequencymultiplierforanoscillatinginput,thenetworkiscapable
researchandanumberofexamplesnowexist;forareviewofthe ofactingasaswitchoranoscillatorwhentheinputisheldconstant
availablesyntheticoscillatorssee[14].Alogicalandnecessarynext betweencertainranges.Allthreefunctionsareavailableforasingle
step is the development of gene networks that are capable of set of parameters. This is a more sophisticated approach than
capturingandusingtheinformationcontainedintheseoscillations. requiringexternalinterventiontoeitherselectfunctionalityortune
Frequency multiplication is one such operation; input oscillations single functions [15,16]. Multi-functionality is a novel attribute in
areprocessedtogiveanoscillatoryoutputwithamultiplefrequency syntheticgenenetworks.Condensingmultiplefunctionsintoasingle
| of the input. | Networks | capable        | of performing |     | frequency multipli- |         |                             |          |                    |

|               |          |                |               |     |                     | network | offers potential advantages | for both | efficiency and the |
| cation, and   | their    | various linear | combinations, |     | would allow         | a       |                             |          |                    |
coordinationofseparatefunctions.
numberofcellularprocessesorsyntheticsystemstobetemporally The outline of the paper is as follows: We first discuss the
coordinated on different time scales. This coordination could be network design and the conceptual basis for its function as a
with reference to each other, or a single ‘master clock’. A single frequencymultiplier.Wethenpresentthemodelusedtorepresent
master clock is an efficient way of ‘keeping time’ within a large thenetwork.Simulationsdemonstratingthefrequencymultiplica-
network,andcouldbedrivenautonomously,orrespondtoexternal tion behaviour follow, and a bifurcation analysis of the model is
| stimuli. A | recently | published | GRN (Gene | Regulatory | Network) |     |     |     |     |

presentedtoexplainthemathematicalbasisforitsbehaviour.The
| designed as | a push-on | push-off | switch | [8] | displays frequency |                  |           |                     |               |

|             |           |          |        |     |                    | multi-functional | nature of | the network is then | discussed and |
multiplicationwithinitsdynamics,butitisnotdesignedtoprocess related to the bifurcation analysis. The potential for an in vivo
an internal input, or one that is continuously oscillating. Both of implementationisthenexamined.Itisshownthatdespiteitssize,
these features are requirements for integration with current almost the entire network can be constructed from well
oscillators.WepresenttheinsilicodesignofanovelGRNcapable characterised components. Finally we discuss the utility and
of functioning as a frequency multiplier of one half for a significanceof thenetwork.
continuouslyoscillatinginternalinput,specificallytheconcentration
| of a transcription |     | factor. We | construct | an Ordinary | Differential |     |     |     |     |

Results
| Equation (ODE)modelofthenetwork |     |     |     | and explainthe | frequency |         |        |     |     |

|                                 |     |     |     |                |           | Network | design |     |     |
multiplierfunctionalitythroughabifurcationanalysisofthismodel.
Lu et al. recently set out the challenges and goals for the next Thedesignofthenetworkisshowninfigure1A.Thenetwork
generation of synthetic gene networks [2]. A central aim was the comprises 4 gene types, encoding the transcriptional repressors
PLoSONE | www.plosone.org 1 February2011 | Volume 6 | Issue 2 | e16140


R1,R2,R3andR4.Eachofthesegenesispresentintwocopies, input),sothereisnotranscriptionfromP1.Thedegradationof
with each copy regulated by a different promoter. However, one R4 then allows production of R2 from P4. There have been
copyeachofR1andR4istranscribedasasingletranscript,under two oscillations in the input concentration, but only one in
thecontrolofthepromoterP1.Similarly,onecopyeachofR2and
eachofR1,R2R3andR4.Hencethenetworkhasactedasa
| R3 is transcribed |     | as  | a single | transcript | under | the | control of |     |           |            |            |     |     |

|                   |     |     |          |            |       |     |            |     | frequency | multiplier | ofonehalf. |     |     |
promoterP2.Therearesixpromoters(P1–P6)intotal.Controlof
| gene expression |         | mainly | occurs | through | repression, |              | depicted by |           |     |     |     |     |     |

| flat-headed     | arrows. | Input  | is     | defined | as          | the presence | of a        | Modelling |     |     |     |     |     |
transcriptional activator, but could equally be the absence of a Amodelofthenetworkwasconstructedtoobtainaqualitative
transcriptional repressor, andactsupon P1and P2. understandingofthenetworkdynamicsandassessitsfunctionality.
A node diagram of the network is shown in figure 1B. Each ThenetworkwasmodelledusingODEsandmass-actionkinetics,
node is a single repressor, and the node is divided into the two withHillfunctionsusedtorepresenttranscriptionalactivationand
| promoters    | which | control | the   | production  |     | of each       | repressor’s |             |     |                 |        |               |                 |

|              |       |         |       |             |     |               |             | repression. |     | The use of ODEs | allows | a bifurcation | analysis of the |
| transcripts. | The   | role of | input | is captured | by  | ‘I’, attached | to the      |             |     |                 |        |               |                 |
networktobeperformed,apowerfulwayofobtainingaqualitative
| promoters | it acts | upon. | The | structure | and | symmetries | of the |     |     |     |     |     |     |

understandingofthenetworkbehaviour.Afullmodelcomprising
networkareclear,forinstancethemutualrepressionbetweenR2 12 ODEs was simplified using the quasi-steady-state assumption
and R4,andtherepression of R1byR2and R3byR4. on mRNA levels [17], resulting in the following model equations
Adiscreteviewofhowthefrequencymultiplierbehaviourarises (see FileS1 forderivation):
whentheinputisasquarewavecanbeseeninfigure2.Thestages
| of thesystemsdynamics |        |        | areas          | follows:    |        |         |             |     |              |                                         |     |                  |                 |

|                       |        |        |                |             |        |         |             |     | (cid:2) RR_1 | (cid:3)~a hz(½I(cid:2))h{(½R2(cid:2))za |     | h{(½R3(cid:2)){d | ½R1(cid:2), ð1Þ |
| N                     |        |        |                |             |        |         |             |     |              | 1                                       |     | 2                | R1              |
| Stage                 | 1. The | system | is initialised |             | with a | certain | level of R1 |     |              |                                         |     |                  |                 |
| and                   | R2 and | no     | input.         | The initial | R1     | and     | R2 repress  |     |              |                                         |     |                  |                 |
transcription fromP1,P5 andP6. (cid:2) RR_2 (cid:3)~b hz(½I(cid:2))h{(½R4(cid:2))zb h{(½R3(cid:2))h{(½R4(cid:2)){d ½R2(cid:2), ð2Þ
| N          |        |       |             |          |          |          |              |     | 1   |     | 2   |     | R2  |

| Stage      | 2. The | input | is applied. | The      | presence | of       | input causes |     |     |     |     |     |     |
| production | of     | R2    | and R3      | from the | P2       | promoter | to occur.    |     |     |     |     |     |     |
RepressionofP1ismaintainedbyR2.R1levelsdegradetoa (cid:2) RR_3 (cid:3)~c hz(½I(cid:2))h{(½R4(cid:2))zc h{(½R1(cid:2)){d ½R3(cid:2), ð3Þ
|       |              |     |              |     |           |     |     |     |     | 1   |     | 2   | R3  |

| level | whichpermits |     | productionof |     | R3fromP5. |     |     |     |     |     |     |     |     |
N
| Stage       | 3. The  | input           | is removed |            | (there | has now    | been one   |              |           |                               |                                |     |                    |

| oscillation | in      | theinput).      | No         | production | of     | R2 or      | R3 from P2 |              |           |                               |                                |     |                    |
|             |         |                 |            |            |        |            |            | (cid:2) RR_4 | (cid:3)~d | hz(½I(cid:2))h{(½R2(cid:2))zd | h{(½R1(cid:2))h{(½R2(cid:2)){d |     |                    |
|             |         |                 |            |            |        |            |            |              | 1         |                               | 2                              |     | R4 ½R4(cid:2), ð4Þ |
| now         | occurs, | and degradation |            | of R2      | allows | production | of R4      |              |           |                               |                                |     |                    |
from P6.R3ismaintainedfromP5.
N
Stage4.Theinputisappliedagain,activatingproductionof hz(½X(cid:2)) h{(½X(cid:2))
|        |     |          |             |     |               |      |        | where |           | and                  | represent | activating | and repressing |

| R1 and | R4  | from P1. | R4 prevents |     | transcription | from | P2. R1 |       |           |                      |           |            |                |
|        |     |          |             |     |               |      |        | Hill  | functions | respectively,defined |           | as:        |                |
repressesproductionofR3fromP5,allowingproductionofR1
from P3.
| N   |     |     |     |     |     |     |     |     |     |     |     | ½X(cid:2)N |     |

Stage 1. The system completes a full cycle: The input is hz(½X(cid:2)): ð5Þ
kNz½X(cid:2)N
| removed | again | (there | have | now been | two | oscillations | in the |     |     |     |     |     |     |

A
Figure1.Networkdesign.A.Physicalrepresentation.R1–R4aretranscriptionalrepressors,andP1–P6denotepromoters.‘Input’isatranscriptional
activator.Flat-headedarrowsrepresentrepression.B.Nodediagramrepresentation.Eachnodeisarepressor,dividedintoitstwopromotersources.
Inputisrepresentedby‘I’.
doi:10.1371/journal.pone.0016140.g001
PLoSONE | www.plosone.org 2 February2011 | Volume 6 | Issue 2 | e16140


Figure2.Adiscreteviewofthefrequencymultiplierbehaviour.Thedynamicscanbesplitintofourstages,startingatstage1andcycling
round clockwise. As the level of input switches on and off twice, each of the repressors has only made one oscillation. The network therefore
functionsasafrequencymultiplierofonehalf.Seemaintextforanexplanationofthenetworkstateateachstage.
doi:10.1371/journal.pone.0016140.g002
|     |                | 1                 |          |     |     |     | k b   |     |     |

|     | h{(½X(cid:2)): |                   |          |     |     |     | a~ tl |     |     |
|     |                |                   |          | ð6Þ |     |     | ,     |     | ð7Þ |
|     |                | (cid:4) ½X(cid:2) | (cid:5)N |     |     |     | d     |     |     |
|     |                | 1z                |          |     |     |     | m     |     |     |
kA
and ½X(cid:2) istheconcentration ofthespecific repressor X,N is the andk isthetranslationrate,bisthemaximumtranscriptionrate
tl
Hillcoefficientandk istheconcentrationofX atwhichbinding and d is the mRNA degradation rate. We also assume
|                 | A                     |       |                |            | m       |              |     |     |     |

|                 |                       | 1     |                |            | a ~b ~c | ~d ~c,where: |     |     |     |
| is half maximal | i.e. hz={(½X(cid:2))~ | . The | external input | ‘I’ is the | 2 2     | 2 2          |     |     |     |

| only activator | within             | the network. d | denotes the              | protein |     |     |          |     |     |

|                |                    |                | X                        |         |     |     | k P      |     |     |
|                |                    | X.             |                          |         |     |     | c~ tl tc |     | ð8Þ |
| degradation    | rate for repressor | Where          | regulation of transcrip- |         |     |     |          |     |     |
d m
| tion by multiple | transcriptional   | regulators      | occurs, the product | is     |     |     |     |     |     |

| taken. This      | is justified from | a probabilistic | standpoint [18];    | for    |     |     |     |     |     |
| transcription    | to occur a        | repressor must  | not be bound,       | and to |     |     |     |     |     |
increase the transcription rate an activator must be bound. The and P is the unrepressed transcription rate. The current model
tc
probabilityofanactivatororrepressorbeingboundandunbound makes the assumption of zero transcription from promoters P1
respectively at any given time is defined by their respective Hill andP2 intheabsence of input.
| functions. | Binding is assumed | to be independent | and therefore |     |             |            |                      |         |          |

|            |                    |                   |               |     | For further | simplicity | the Hill coefficient | and k A | are also |
taking the product gives the desired probability. The parameters assumed to be the same for each Hill function. This simplified
i~1,2
a i , b i , c i and d i , where are derived in File S1. We will model uses 8 parameters, given in table 1. A discussion of the
|     | ~b ~c ~d | ~a, |     |     |     |     |     |     |     |

assume that a 1 1 1 1 where: parameter ranges usedisgiveninFile S2.
PLoSONE | www.plosone.org 3 February2011 | Volume 6 | Issue 2 | e16140


However,inordertointegratewithexistinggeneticoscillatorsin
| Table1. Networkparameters | used | insimulations. |     |     |                |                   |            |             |               |        |           |

|                           |      |                |     |     | vivo the       | network must      | be capable |             | of performing |        | frequency |
|                           |      |                |     |     | multiplication | on a continuously |            | oscillating |               | input. | Numerical |
Parameter Value Units simulations showed the network performing frequency multiplica-
|                      |     |        |     |     | tion of one       | half on an | oscillating | input | with      | a period | of 90000  |

| Translationrate(ktl) |     | 6E{4   |     | s21 |                   |            |             |       |           |          |           |
|                      |     |        |     |     | seconds (25hours) | (see       | File S3).   | We    | confirmed | that     | frequency |
|                      |     | 2:5E{3 |     | s21 |                   |            |             |       |           |          |           |
mRNAdegradationrate(dm) multiplicationwasalsopossiblewithaslightlyweakerrepressork
A
Proteindegradationrate(dX) 4E{4 s21 of*4:6E{9M(datanotshown)(theparametersusedaregivenin
FileS2).Furthermore,theoscillatorsconstructedsofarinvivodonot
| Hillcoefficient(N) |     | 1.3 |     | scalar |     |     |     |     |     |     |     |

generallyreachazerolevelinbetweenoscillations[14].Afrequency
| kAforactivator |     | *2E{8 |     | M   |            |                |            |     |         |      |              |

|                |     |       |     |     | multiplier | must therefore | be capable | of  | working | with | oscillations |
*6E{10
| kAforrepressor |     |     |     | M   |     |     |     |     |     |     |     |

thathaveanon-zerominimum,oroffset.Figure4demonstratesthe
| Maximumtranscriptionrate(P1andP2)(b) |     | 4E{10 |     | M.s21 |     |     |     |     |     |     |     |

networkperformingfrequencymultiplicationonanoscillatinginput
|     |     | 4E{10 |     | M.s21 |     |     |     |     |     |     |     |

Unrepressedtranscriptionrate(P3–P6)(Ptc) withaninputminimumof6nM.Thisisapproximately10%ofthe
p p m a x im um l e v el , c o m p a r a b l e t o o s c ill a t io n s generated by the
| ExactvaluesforactivatorandrepressorkAare |     | 1 :3ffi 1 ffiffiEffiffiffi{ffiffiffiffiffi 1 ffiffiffi 0 ffiffi and | 1 :3ffi 1 ffiffi E ffiffiffi{ffiffiffiffiffi | 1 ffiffiffi 2 ffiffi |                 |                       |             |             |           |     |     |

|                                          |     |                                                                     |                                              |                      | rec e n tly con | s t ru c te d r o b u | s t o s cil | l ato r i n | [ 1 1 ] . |     |     |
respectively.
doi:10.1371/journal.pone.0016140.t001
|                      |                        |           |           |     | Bifurcation | analysis              |     |               |     |            |          |

| Frequency multiplier | behaviour              |           |           |     |             |                       |     |               |     |            |          |
|                      |                        |           |           |     | In order    | to investigate        | the | origin        | and | robustness | of the   |
| We first confirmed   | the discrete switching | behaviour | described | in  |             |                       |     |               |     |            |          |
|                      |                        |           |           |     | frequency   | multiplier behaviour, |     | a bifurcation |     | analysis   | of model |
figure2.Numericalsimulationsinfigure3showthenetworkperfor- (1)–(4) was performed under variation of a constant and then
mingfrequencymultiplicationofonehalfonasquarewaveinput,i.e. periodicinput.Inordertopreservecorrespondencetothephysical
theperiodoftheoscillationsinR1toR4istwicethatoftheinput. system, we performed the analysis on the dimensionalised
Figure3.Frequencymultiplicationforadiscretesquarewaveinput.TimeseriesfortherepressorsR1–R4andtheinputareshowninthetop
andbottompanelsrespectively.TheconcentrationsofR1,R2,R3andR4arerepresentedbypink,black,orangeandgreenlinesrespectively.The
stagescorrespondingtofigure2areshowninthetoppanel.Initialconditions:R1~R2~50nM,R3~R4~0nM.Parametersfromtable1areused.
doi:10.1371/journal.pone.0016140.g003
PLoSONE | www.plosone.org 4 February2011 | Volume 6 | Issue 2 | e16140


Figure4.Frequencymultiplicationforasineinputwithanoffset.TimeseriesfortherepressorsR1–R4andtheinputareshowninthetop
andbottompanelsrespectively.TheconcentrationsofR1,R2,R3andR4arerepresentedbypink,black,orangeandgreenlinesrespectively.Initial
2p
conditions:R1~R2~50nM,R3~R4~0nM.Theinputisthefollowingfunction:½I(cid:2)(t)~a{acos(Pt)za,whereP~ ,pistheperiod,tistime,ais
p
amplitudeandaistheminimumoftheinput.a~6nM.Parametersfromtable1areused.
doi:10.1371/journal.pone.0016140.g004
equations. The software package AUTO [19] was used to carry 1.A region of coexistence of two stable and three unstable
| out allcontinuations. |               |             |     |      |            | equilibria | forI [ [0,*0.4]. |          |             |         |          |

| Six continuation      | of equilibria | experiments |     | were | performed, |            |                  |          |             |         |          |
|                       |               |             |     |      |            | 2.A region | where a single   | unstable | equilibrium | exists, | together |
using automatic branch switching where appropriate. Initial with stable undamped oscillations emerging from a Hopf
estimatesofthemodelequilibriawereobtainedthroughnumerical bifurcation forI [ [*0.4,*7].
| integration | in MATLAB        | (The Mathworks, |            | Natick, | MA) and the  |                                             |                   |     |            |     |              |

|             |                  |                 |            |         |              | 3.Aregionwhereasinglestablefocusexists,forI |                   |     |            |     | [[*7,*9].    |
| numerical   | solvers in MAPLE | (Maplesoft,     | Waterloo,  |         | ON) and are  |                                             |                   |     |            |     |              |
|             |                  |                 |            |         |              | 4.A region                                  | of coexistence    | of  | two stable | and | one unstable |
| summarised  | in table 2. Two  | stable          | equilibria | (‘a’    | and ‘b’) are |                                             |                   |     |            |     |              |
|             |                  |                 |            |         |              | equilibrium                                 | for I [ [*9,§60]. |     |            |     |              |
characterisedbyzeroconcentrationsofR1andR2(a)orR3and
R4 (b) respectively, while equilibrium ‘c 1 ’ is characterised by low Iftheinputconcentrationisheldconstant,suchthatthesystem
concentrations of all repressors except R3. Figure 5 depicts a 1- is in the region of the bifurcation structure between the saddle-
dimensional schematic bifurcation diagram summarising the node bifurcation and the Hopf bifurcation, a stable limit cycle
| results ofall   | thecontinuation | runs.        |     |              |           |            |              |                  |         |     |             |

|                 |                 |              |     |              |           | exists and | the dynamics | are oscillatory. | Figures | 6A  | and 6B show |
| The bifurcation | structure       | has a number |     | of important | features. |            |              |                  |         |     |             |
howtheoscillationperiodandamplitudechangeoverthe*7nM
As the concentration of the input is increased we detect two rangewhereoscillationsareobserved.Themostnotablefeatureis
simultaneous saddle-node bifurcations of equilibria a and b at I the near-vertical increase in oscillation period as the input
*0.4 nM, leading to their disappearance. Continuation of approaches the concentration at which the saddle-node bifurca-
equilibria c shows the occurrence of a supercritical Hopf tionsoccur.Thissuggeststhataninfinite-periodbifurcationtakes

| bifurcation | at I *7 nM | and a | pitchfork | bifurcation | at I | place [20]. |     |     |     |     |     |

*9 nM. The model behaviour can be divided into four distinct Toinvestigatethefrequencymultiplierbehaviour,continuation
dynamical regions,corresponding tolabels 1–4infigure 5: oflimitcyclesofaperiodicallyforcedsystemwasperformedona
| Table2. | Networkparameters | used | insimulations. |     |     |     |     |     |     |     |     |

Associatedapproximateconcentrations
| Equilibrium                              |     |     |                                            | (nM)({R1,R2,R3,R4})      |                                                                                 |     |     |     | Bifurcationsuncovered  |     |     |

| a.[I] =0.1nM                             |     |     |                                            | {144,144,0,0}            |                                                                                 |     |     |     | Saddle-nodebifurcation |     |     |
| b.[I] =0.1nM                             |     |     |                                            | {0,0,144,144}            |                                                                                 |     |     |     | Saddle-nodebifurcation |     |     |
| C1.[I] =0.1nM                            |     |     |                                            | {4,8,27,3}               |                                                                                 |     |     |     | PitchforkandHopf       |     |     |
|                                          |     |     | p                                          |                          | p                                                                               |     |     |     |                        |     |     |
| ExactvaluesforactivatorandrepressorkAare |     |     | 1 :3ffi 1 ffiffiEffiffiffi{ffiffiffiffiffi | 1 ffiffiffi 0 ffiffi and | 1 :3ffi 1 ffiffi E ffiffiffi{ffiffiffiffiffi 1 ffiffiffi 2 ffiffi respectively. |     |     |     |                        |     |     |
doi:10.1371/journal.pone.0016140.t002
PLoSONE | www.plosone.org 5 February2011 | Volume 6 | Issue 2 | e16140


Figure 5. 1-dimensional sketch summarising the bifurcation structure. The three main features are two simultaneous saddle-node
bifurcations,aHopfbifurcationandapitchforkbifurcation.Theseoccuratinputconcentrationsof*0.4nM,*7nMand*9nMrespectively.The
analysiscoverstheinputconcentrationrange0–60nM,andtracesoutthreebranchesofequilibria,A,BandC.Thestructurecanbedividedintofour
dynamicalregionscorrespondingtolabels1–4.Thedynamicsateachlabelareshowninthesetofsimulationsabove.Atposition1and4twostable
equilibriaexistsimultaneously.Inallsimulationpanelsthehorizontalaxisistime(seconds)andtheverticalaxisisconcentration.Allsimulationsare
PLoSONE | www.plosone.org 6 February2011 | Volume 6 | Issue 2 | e16140


for1:5E6seconds.Theconcentrationrangeontheverticalaxisinpanels1aand1b,2,3and4c and4c ,are0–150nM,0–90nM,0–140nMand0–
1 2
180nMrespectively.Simulationpanels4c and4c usedinitialconditionsR1~R2~0nM,R3~R4~50nM.Allotherpanelsusedinitialconditions
1 2
R1~R2~50nM,R3~R4~0nM.Panels1aand1b,2,3and4c

and4c

useaconstantinputconcentration½I(cid:2)~0:1nM,5nM,7.5nMand10nM
(4c and4c )respectively.Allsimulationsusetable1parameters.Reddashedlinesdelineatetheoscillatoryregion,whichliesinbetweentwostable
1 2
regionsinwhichtrajectoriesdecaytoequilibriumlevels.Thisdiagramisintendedtoconveythequalitativeaspectsofthephaseportrait.Assuch
thereisnoscaleontheverticalaxis.
doi:10.1371/journal.pone.0016140.g005
Figure6. Effectof inputconcentrationon oscillationcharacteristics. I [ [*0:4, *7].A. Relationshipbetweeninput concentration and
period(seconds).B.RelationshipbetweeninputconcentrationandtheL2-norm(inthiscasethenormofavectorrepresentingtheamplitudeofR1
toR4).
doi:10.1371/journal.pone.0016140.g006
PLoSONE | www.plosone.org 7 February2011 | Volume 6 | Issue 2 | e16140


modified set of equations with the oscillating input (forcing) these high frequency oscillators may be possible under different
| defined autonomously |           | (see   | File          | S4). Numerical |          | time series | data     | parameter           | regimes. |     |     |

| describing           | a single  | period | of a period-1 |                | solution | of the      | modified |                     |          |     |     |
| system of            | equations | was    | used          | as an          | initial  | condition   | for      | Multi-functionality |          |     |     |
continuation. Continuation was performed using the period of To date, synthetic gene networks have possessed single
theinputasthebifurcationparameter(theamplitudeoftheinput functions.Theprecedinginvestigationofthebifurcationstructure
was 50nMas insimulations). suggests that our networkpossesses other functions in additionto
Continuations demonstrate that the frequency multiplier frequency multiplication. Specifically, the networkis also capable
| functionality | is a   | consequence | of       | a period-doubling |            | bifurcation |          |                 |                   |                          |              |

|               |        |             |          |                   |            |             |          | of functioning  | asan oscillatoror | aswitch.                 |              |
| as the period | of     | the input   | crosses  | a certain         | threshold. | Figure      | 7A       |                 |                   |                          |              |
|               |        |             |          |                   |            |             |          | The oscillatory | behaviour         | in figure 5 demonstrates | that, if the |
| shows the     | period | of the      | ‘output’ | i.e. proteins     |            | R1 to       | R4, as a |                 |                   |                          |              |
inputconcentrationisheldconstantwithinacertainrange(*0:4
| function | of the | input | period. | Prior | to the | period-doubling |     |          |                       |                   |           |

|          |        |       |         |       |        |                 |     | to 7nM), | the network functions | as an oscillator. | While the |
bifurcation the output period is equal to the input period (blue explanation of the oscillator function is straightforward from a
line). A period-doubling bifurcation occurs at *27500 seconds mathematical perspective, it is decidedly more complicated in
(*8 hours), after which (red line) the output period is twice the terms of gene interactions, but can be understood by examining
| period of | the input. | Equivalently |     | the | output | frequency | is half |     |     |     |     |

simulationsofthefullmodel(datanotshown).Thestepsofasingle
| the input    | frequency.            | The       | existence |              | of a    | period      | doubling |                |                        |                         |              |

|              |                       |           |           |              |         |             |          | cycleare       | described sequentially | below.                  |              |
| bifurcation  | is further            | confirmed |           | in figure    | 7B,     | which shows | the      |                |                        |                         |              |
| relationship | between               | the       | input     | period,      | and the | L2-Norm.    | As       |                |                        |                         |              |
|              |                       |           |           |              |         |             |          | 1.Thesystem    | isinitialised          | with someR1andR2.       |              |
| expected     | for a period-doubling |           |           | bifurcation, | the     | L2-Norm     | of the   |                |                        |                         |              |
|              |                       |           |           |              |         |             |          | 2.Depending    | on their               | initial concentrations, | R1 and R2    |
| period-2     | limit cycle           | is equal  | to        | the period-1 | limit   | cycle       | at the   |                |                        |                         |              |
|              |                       |           |           |              |         |             |          | concentrations | increase               | due to production from  | P3 and P4 as |
| bifurcation  | point.                |           |           |              |         |             |          |                |                        |                         |              |
|              |                       |           |           |              |         |             |          | there isno     | R3orR4present          | withinthesystem.        |              |
| This result  | shows                 | that      | for the   | parameter    | values  | in          | table 1, |                |                        |                         |              |
3.Althoughtheinputispositive,thereisnoproductionfromP1
| frequency | multiplication |     | can be | performed | on  | a wide | range of |     |     |     |     |

asR2ispresent.HoweverR3increasesfromP2andswitches
| input periods, | from | *8  | hours | (figure 7A) | to at | least 140hours |     |     |     |     |     |

offproductionofR1andR2fromP3andP4respectively.This
(datanotshown).Ournetworkisthereforetheoreticallycapableof
|             |      |          |             |     |             |         |     | state issimilar | tostage | 1 offigure 2. |     |

| interfacing | with | existing | long-period |     | oscillators | [6,13]. | The |                 |         |               |     |
majority of currently available oscillators exhibit oscillations with 4.ThiscausesR1andR2levelstodrop.R1dropsrapidlyasP3was
periodsshorterthan8 hours[14],andfrequencymultiplicationon itsonlysource.R2dropsmoreslowlyasitisstillproducedfromP2.
Figure7.Existenceofaperiod-doublingbifurcation.Aperiod-doublingisobservedataninputperiodof*27500seconds(*8hours).The
period-doublingpointislabelledas‘PD’.Bluelinesandredlinesrepresentperiod-1andperiod-2solutionsrespectively.A.Relationshipbetween
inputperiodand‘output’period,whereoutputdenotestheproteinsR1toR4.B.RelationshipbetweeninputperiodandL2-Norm.
doi:10.1371/journal.pone.0016140.g007
PLoSONE | www.plosone.org 8 February2011 | Volume 6 | Issue 2 | e16140


5.R3 from P5 increases as R1 is its only repressor. This state is input, above the oscillatory range, the system remains at step 5 as
similar tostage 2 offigure 2. thereisenoughR2beingproducedfromP2tomaintainrepressionof
6.Although there is repression of P6 from P2 R2, a positive R4productionfromP1andP6,whichpreventsthepositivefeedback
feedback loopis formed, whereby R4 fromP6 represses P2, loop in step 6 from occurring. At an intermediate constant input,
reducing the level of R2, which reduces repression on P6, within the oscillatory range of figure 5, the level of input is high
furtherincreasingR4andrepressingP2,andsoon.AssuchR2 enoughtomovethesystemonfromstep3to4,butlowenoughto
decreasesandR4fromP6increases,towardsomeequilibrium. allowprogressionfromstep5to6.Thesystemcanthenfreelyprogress
throughstep1to9sequentially,generatingoscillatorydynamics.
7.R2isnowatalowlevel.ThisallowsinputtoswitchonP1and
increase R1 and R4, causing R3 and R4 from P5 and P6 The bifurcation structure also reveals that if the input is held
respectively toberepressed. constant between either the concentrations 0 to 0.4 nM or 9 to
|           |                    |     |          |                |      | 60nM, the   | network exhibits | bi-stability. | This allows      | the network   |

| 8.R1 then | increases rapidly, | as  | with low | R3, production | also |             |                  |               |                  |               |
|           |                    |     |          |                |      | to function | as a toggle      | switch if the | binding affinity | of particular |
| increases | through P3.        |     |          |                |      |             |                  |               |                  |               |
repressorsistemporarilylowered.Thiscanbedoneinvivobysmall
| 9.R2 increases | from P4 | with another | positive | feedback | loop |     |     |     |     |     |

moleculestermed‘inducers’[4].Thistoggleswitchbehaviourcan
existingbetweenP4andP1wherebyR2switchesoffP1which
decreases R4 which allows further R2 increase, and so on, beachievedforaverylowconcentration(figures8Aand8B)anda
|              |                   |     |               |       |         | highconcentration(figures |     | 8Cand8D).Itislikelythat |     | switching |

| again toward | some equilibrium. |     | This increase | in R1 | from P3 |                           |     |                         |     |           |
canbeachievedforarangeofconstantinputvaluesfarexceeding
| and R2 | from P4 brings | the | system back | toward | stage 1, |     |     |     |     |     |

60nM.IfweconsiderthenetworkwithinE.coli,onecanusethe
| completing | acycle.        |           |           |                    |     |                   |                                        |             |               |             |

|            |                |           |           |                    |     | approximationthat | 1moleculecorrespondstoaconcentrationof |             |               |             |
|            |                |           |           |                    |     | 1 nM. Then        | the low                                | input range | for switching | is probably |
| At a low   | constant level | of input, | below the | oscillatory range, | the |                   |                                        |             |               |             |
systemremainsatstep3asthelevelofinputisnothighenoughto physicallyirrelevantastheconcentrationcorrespondstolessthata
produceenoughR3fromP2tosignificantlyrepressP3andP4and singlemolecule.However,incellswithlargervolumestheselower
movethesystemontostep4.Alternatively,atahighconstantlevelof concentrations willbecomemore relevant.
Figure 8. Demonstration of switch function. In each case the system is allowed to reach equilibrium under a constant level of input. The
concentrationsofR1,R2,R3andR4arerepresentedbypink,black,orangeandgreenlinesrespectively.A.Switchfrom[R1&R2high,R3&R4low]to
[R3&R4high,R1&R2low],ataninputof0.1nM.B.Switchfrom[R3&R4high,R1&R2low]to[R1&R2hightoR3&R4low],ataninputof0.1nM.
C.Switchfrom[R2&R3high,R1&R4low]to[R1&R4high,R2&R3low],ataninputof50nM.D.Switchfrom[R1&R4high,R2&R3low]to[R2&R3
hig h p , R 1 & R 4 lo w ] , a t an i np u to f5 0 n M .I n A a n d C t h e s w itc h i s p e rf o rm ed b y inc re a s in g t he k A f o r R 1 a n d R 2 b i n d i n g f r o m *6 E { 10 M t o * 4 E { 6
1 : 3 ffi ffi ffi ffiffiffi {ffiffiffiffi ffi ffi ffiffi
M ( 1 E 7 e xa c t ly ) b et w e en th e ti m es 1 :5 E 5 a n d 1 : 55 E 5 s ec o n d s . In B an d D th e s w i tc h is p e r fo r m e d b y i nc r e a s i n g t h e k A fo r R3 an d R 4 b in d ing
bythesameamountandduration.InitialconditionsofR1~R2~50nM,R3~R4~0nMforAandC,andR1~R2~0nM,R3~R4~50nMforBand
D.Parametersfromtable1areused.
doi:10.1371/journal.pone.0016140.g008
PLoSONE | www.plosone.org 9 February2011 | Volume 6 | Issue 2 | e16140


In summary,thethree functions of thenetworkare: function was observed (see File S6), demonstrating the function is
robusttointrinsicnoise.
1.Frequency multiplier of onehalf.When theinput tothe Apossibleimplementationofthenetworkisgiveninfigure9.It
network is oscillatory the output of the network is oscillatory is based on constructing the network in E. coli, a tried and tested
| with afrequency | halfthat | of theinput. |     |                           |     |             |     |

|                 |          |              |     | host forsyntheticnetworks |     | [4,6,9–11]. |     |
2.Oscillator. When the input is maintained within a certain Theimplementationproposedhereusesthebacterialtranscrip-
range thenetworkoscillates. tion repressors LexA, LacI, lcI and TetR, and the bacterial
3.Switch.Whentheinputismaintainedwithinacertainrange, transcriptionalactivatorAraC.Thesehaveallbeenusedbeforein
external modulation of particular repressive strengths allows the construction of synthetic networks [4,6,8,9,11], as have the
|     |     |     |     | promotersP | [11],lP | [9]andpNOR[8].Thepromoters |     |

switching betweendifferent steady-state protein levels. lac=ara{1 R
|           |                            |     |     | Fx have all   | been constructed | and characterised                 | [21], but the |

|           |                            |     |     | modified pNOR | wouldrequire     | construction andcharacterisation. |               |
| Prospects | for in vivo implementation |     |     |               |                  |                                   |               |
Arabinose,whichbindstoAraCallowingittoactivatetranscription,
| The model | uses symmetric | parameters. | However, some |     |     |     |     |

asymmetrywillinevitablyexistinaninvivoimplementation,even hasalsobeenpreviouslyused[11].However,inthisimplementation
with well matched components. We therefore used numerical itwouldalignbetterwithmodellingifArabinosewasmaintainedat
simulations to investigate the effect of various sample forms of asaturatinglevel,andAraCusedasthevaryinginput.
asymmetryoneachofthethreefunctions.Ineachsimulationthe Despite the availability of components, a functional in vivo
|     |     |     |     | construction | of the network | poses two main | challenges. Firstly, |

valueofasingleparameterwaschangedfromthevaluestatedin
noneofthepromoterssofarusedintheconstructionofsynthetic
table1,whilstallotherparameterswerekeptatthevaluesstatedin
|             |                      |                |                    | networks have | been characterised | for control             | by an externally |

| table 1. We | found that all three | functions were | robust to at least |               |                    |                         |                  |
|             |                      |                |                    | controlled    | oscillating input. | Methods for controlling | gene expres-     |
someformsofasymmetry(seeFileS5),andwethereforeconclude
that the network’s functions do not depend on the use of a sion,suchasanoscillatingarabinoseconcentration(figure9),light
completely symmetrical parameter set. The failure to observe [22]andtemperature[23]couldbeexplored,asthesearecapable
functionality in some of our asymmetric simulations does not of regulating gene expression in a reversible manner. Secondly,
necessarily indicate that the parameters in question must be evenifthenetworkwasshowntobetheoreticallycompatiblewith
symmetrical in order for the network to function, as it might be theoutputfromanexistingoscillator,therepertoireofrepressors
possibletorestorefunctionalitybycompensatorychangesinother thathavebeenusedandcharacterised inthecontextofsynthetic
networksisnotextensiveenoughtoallowforconstructionofboth
parametersinthenetwork.Amuchfullerdescriptionofparameter
space is required to properly understand the parameter depen- networks without an overlapping use of components. Other
dence of the three functions, and would direct the choice of naturally occurring repressors could be used, but these are
components usedina invivo implementation. untestedandaddmoreuncertaintytotheconstruction.Ultimate-
Intrinsicnoiseisanotherphysicalrealitythatmustbeconsidered. ly, the design and construction of large networks with functions
StochasticsimulationsintheformofChemicalLangevinEquations only available within specific parameter regimes will require
(CLEs) were performed to assess the robustness of the three libraries of well characterised artificial transcription factors [24–
functionstonoise(parametersfromtable1used).Ineachcasethe 27]that are orthogonal tothehostsystem.
fR1,R2,R3,R4g~flexA,lacI,lcI,tetRg.
Figure 9. Possible invivoimplementation of the network. The repressors used are the set The
promotersusedare:Fxe.g.F23[21],P [35],pNOR[8]andlP .ModifiedpNORisthepNORpromoterwithrepressionbyLacIremoved.The
|     |     | lac=ara{1 | R   |     |     |     |     |

inputtothenetworkisarabinose+AraC,whichformacomplexthatcanactivatetranscription.
doi:10.1371/journal.pone.0016140.g009
PLoSONE | www.plosone.org 10 February2011 | Volume 6 | Issue 2 | e16140


Discussion increasing frequently as synthetic networks become larger and
|     |     |     |     |     |     |     |     | more complex. |     | The challenge | will | then be | to ensure | that the |

A theoretical synthetic gene regulatory network has been design process identifies and exploits any benefits that multi-
presented, and a possible in vivo implementation discussed. The functionality brings ifandwhenitarises.
| network | iscapable | of performing |     | frequency |     | multiplication | of one |     |     |     |     |     |     |     |

Thenetworkpresentedhereisnovelintworespects.Firstly,itis
| half on an     | oscillating | transcription |           | factor    | concentration, |             | such as   |         |               |     |                          |     |                   |     |

|                |             |               |           |           |                |             |           | capable | of performing |     | frequency multiplication |     | on a sinusoidally |     |
| those produced |             | by the        | currently | available |                | oscillators | [14]. The |         |               |     |                          |     |                   |     |
oscillatinginput,suggestingitiscapableofintegratingwithcurrent
| network   | takes an | oscillating | transcription |             | factor | concentration | as       |              |           |     |                        |     |                   |     |

|           |          |             |               |             |        |               |          | oscillators. | Secondly, | it  | possesses programmable |     | multi-functional- |     |
| an input, | and      | produces    | an            | oscillatory | output | with          | half the |              |           |     |                        |     |                   |     |
ity,specificallytheabilitytoselectbetweenoneofthreefunctions
| frequency       | of the     | input, | in the      | form | of the   | concentration | of a |             |               |        |                      |               |                     |         |

|                 |            |        |             |      |          |               |      | by changing | the           | nature | of the input.        | Collectively, | this                | network |
| transcriptional | repressor. |        | Bifurcation |      | analysis | demonstrates  | that |             |               |        |                      |               |                     |         |
|                 |            |        |             |      |          |               |      | represents  | a significant |        | theoretical addition |               | to the capabilities | of      |
the frequency multiplier functionality is a result of a period- current synthetic genenetworks.
| doubling       | bifurcation. | This           | is  | the first | synthetic     | gene  | network   |           |     |         |     |     |     |     |

| presented      | that is      | theoretically  |     | capable   | of performing |       | frequency |           |     |         |     |     |     |     |
|                |              |                |     |           |               |       |           | Materials | and | Methods |     |     |     |     |
| multiplication | on           | a continuously |     |           | oscillating   | input | from an   |           |     |         |     |     |     |     |
intracellular source. The development of genetic frequency NumericalsimulationswereperformedusingcustomMATLAB
multipliers could allow cellular processes and synthetic systems (The Mathworks, Natick, MA) scripts and the ode45 numerical
existing on various different time scales to be temporally integrator. Stochastic simulations used the fixed step numerical
coordinated, either with reference to each other, or a single integrator ode4. Continuations of bothequilibria andlimitcycles
‘master clock’ that keeps timeforthenetwork. wereperformedinAUTO07p[19],usingtheconstantinputlevel
Bifurcationanalysisrevealsthatthenetworkismulti-functional.
andperiodofinputasbifurcationparametersrespectively.Ranges
Forasinglesetofparametersthenetworkcandisplayoneofthree
|     |     |     |     |     |     |     |     | for steady-state | values | of  | the system | for a constant | level | of input |

functions, which can be selected by changing the temporal were obtained by simulation in MATLAB (The Mathworks,
characteristicsoftheinput.Parallelscanbedrawnwiththefieldof Natick,MA).MAPLE(Maplesoft,Waterloo,ON)wasthenusedto
neuroscience where multi-functional circuits are widespread in numerically solve within the range to obtain steady-state values
both invertebrates and vertebrates [28–31] (see [32] for a recent with aprecision adequate forstarting continuations.
| review). | Multi-functionality |     | has | also recently |     | been observed | on a |     |     |     |     |     |     |     |

basic level in both coherent and incoherent feed-forward-loops Supporting Information
| [33,34],             | which are | small      | regulatory | motifs           | present | in    | some gene   |        |       |             |     |     |     |     |

| and proteinnetworks. |           |            |            |                  |         |       |             | FileS1 | Model | derivation. |     |     |     |     |
| The obvious          |           | benefit    | of using   | multi-functional |         |       | networks is | (PDF)  |       |             |     |     |     |     |
| efficiency;          | network   | components |            | are              | re-used | under | different   |        |       |             |     |     |     |     |
dynamic,functionalregimes[32].Thisallowsanumber ofsingle FileS2 Model parameterisation.
(PDF)
| function | networks   | to       | be condensed |                  | into | one multi-functional |       |     |     |     |     |     |     |     |

| network. | It is also | proposed | that         | multi-functional |      | networks             | allow |     |     |     |     |     |     |     |
FileS3 Frequencymultiplicationforanoscillatinginput
functionstobebettercoordinated.InthemarinemolluskTritonia,
returningtozero.
| crawling, | withdrawal | and | swimming |     | are all | part of | the escape |     |     |     |     |     |     |     |

(PDF)
| response.    | The   | use of   | a single     | multi-functional |            | neural     | network |        |              |     |                 |     |     |     |

| ensures this | vital | response | is correctly |                  | temporally | integrated | [31].   |        |              |     |                 |     |     |     |
|              |       |          |              |                  |            |            |         | FileS4 | Continuation |     | oflimit cycles. |     |     |     |
Multi-functionalityisnotapropertyoftenascribedtonaturalgene
(PDF)
| networks,     | probably  | because  |                   | natural | networks | are        | rarely fully |         |             |     |               |           |         |     |

| characterised | and       | inputs   | and               | outputs | are      | difficult  | to define.   |         |             |     |               |           |         |     |
|               |           |          |                   |         |          |            |              | File S5 | Simulations |     | investigating | parameter | asymme- |     |
| Despite       | this, the | size and | interconnectivity |         |          | of natural | networks     |         |             |     |               |           |         |     |
try.
| may mean | that | multi-functionality |     | can | readily | be found | at some |     |     |     |     |     |     |     |

(PDF)
level.Indeed,theworkinneuralsystemsdemonstratesthatmulti-
functionality isapropertyselectedforinevolution,andtherefore FileS6 Stochasticsimulations.
| would beexpectedtoarise |                 |      | inother   | biological |           | contexts.  |             | (PDF) |     |     |     |     |     |     |

| The                     | single-function |      | synthetic | networks   |           | considered | in the      |       |     |     |     |     |     |     |
| literature              | so far          | have | been      | rationally | designed, |            | with larger |       |     |     |     |     |     |     |
networkssettobeconstructedinamodularfashionbyconnecting
Acknowledgments
upthesenetworks[8].Ofthethreefunctionsofournetwork,only
frequencymultiplicationwasrationallydesigned,whiletheswitch We thank David A.W. Barton, Univ. of Bristol, for assistance with
and oscillator functions were discovered. In particular, the performingcontinuations.
oscillatorfunctionisdifficulttounderstandintermsofgene-gene
interactions,andwouldarguablybeimpossibletorationallydesign Author Contributions
usingcurrentmethodologies.Thisworksuggeststhatwhilemulti- Conceivedanddesignedtheexperiments:OPMdBCSGNJS.Performed
functionality may be difficult to design on purpose, it may be the experiments: OP. Analyzed the data: OP. Wrote the paper: OP.
difficulttoavoidbychance,andmaybeapropertythatemerges Reviewedthemanuscript:MdBCSGNJS.
References
1. Purnick PEM, Weiss R (2009) The second wave of synthetic biology: from 3. KhalilAS,CollinsJJ(2010)Syntheticbiology:applicationscomeofage.NatRev
| modulestosystems.NatRevMolCellBiol10:410–22. |     |     |     |     |     |     |     | Genet11:367–79. |     |     |     |     |     |     |

2. LuTK,KhalilAS,CollinsJJ(2009)Next-generationsyntheticgenenetworks. 4. Gardner TS, Cantor CR, Collins JJ (2000) Construction of a genetic toggle
NatBiotech27:1139–50. switchinEscherichiacoli.Nature403:339–42.
PLoSONE | www.plosone.org 11 February2011 | Volume 6 | Issue 2 | e16140


5. KramerBP,VirettaAU,Daoud-El-BabaM,AubelD,WeberW,etal.(2004) 21. Kinkhabwala A, Guet CC (2008) Uncovering cis regulatory codes using
Anengineeredepigenetictransgeneswitchinmammaliancells.NatBiotech22: syntheticpromotershuffling.PLoSONE3:e2030.
867–70. 22. DeitersA(2009)Lightactivationasamethodofregulatingandstudyinggene
6. Atkinson MR, Savageau MA, Myers JT, Ninfa AJ (2003) Development of expression.CurrOpinChemBiol13:678–86.
geneticcircuitryexhibitingtoggleswitchoroscillatorybehaviorinEscherichia 23. Neupert J, Karcher D, Bock R (2008) Design of simple synthetic RNA
coli.Cell113:597–607. thermometers for temperature-controlled gene expression in Escherichia coli.
7. Deans TL, Cantor CR, Collins JJ (2007) A tunable genetic switch based on NucleicAcidsRes36:e124.
RNAiandrepressorproteinsforregulatinggeneexpressioninmammaliancells. 24. LeeJY,SungBH,YuBJ,LeeJH,LeeSH,etal.(2008)Phenotypicengineering
Cell130:363–72. byreprogramminggenetranscriptionusingnovelartificialtranscriptionfactors
8. LouC,LiuX,NiM,HuangY,HuangQ,etal.(2010)Synthesizinganovel inEscherichiacoli.NucleicAcidsRes36:e102.
geneticsequentiallogiccircuit:apush-onpush-offswitch.MolSystBiol6:350. 25. GommansWM,HaismaHJ,RotsMG(2005)Engineeringzincfingerprotein
9. ElowitzMB,LeiblerS(2000)Asyntheticoscillatorynetworkoftranscriptional transcription factors: the therapeutic relevance of switching endogenous gene
regulators.Nature403:335–8. expressiononoroffatcommand.JournalofMolecularBiology354:507–19.
10. FungE,WongWW,SuenJK,BulterT,LeeS,etal.(2005)Asyntheticgene-
26. ParkKS,JangYS,LeeH,KimJS(2005)Phenotypicalterationandtargetgene
metabolicoscillator.Nature435:118–22.
identificationusingcombinatoriallibrariesofzincfingerproteinsinprokaryotic
11. StrickerJ,CooksonS,BennettMR,MatherWH,TsimringLS,etal.(2008)A
cells.JournalofBacteriology187:5496–9.
fast,robustandtunablesyntheticgeneoscillator.Nature456:516–U39.
27. Giesecke AV,FangR, Joung JK (2006) Synthetic protein-protein interaction
12. Tigges M, Marquez-Lago TT, Stelling J, Fussenegger M (2009) A tunable
domainscreatedbyshufflingcys2his2zinc-fingers.MolSystBiol2:2006.2011.
syntheticmammalianoscillator.Nature457:309–12.
28. Soffe SR (1997) The pattern of sensory discharge can determine the motor
13. TiggesM,De´nervaudN,GreberD,StellingJ,FusseneggerM(2010)Asynthetic
responseinyoungXenopustadpoles.JCompPhysiolA180:711–5.
low-frequencymammalianoscillator.NucleicAcidsRes38:2702–11.
29. Getting PA, Deken MS (1985) Model Neural Networks and Behavior. New
14. Purcell O, Savery NJ, Grierson CS, di Bernardo M (2010) A comparative
York:PlenumPress,chapterTritoniaswimming:amodelsystemforintegration
analysisofsyntheticgeneticoscillators.JRSocInterface7:1503–24.
withinrhythmicmotorsystems.pp3–20.
15. SohkaT,HeinsRA,PhelanRM,GreislerJM,TownsendCA,etal.(2009)An
externally tunable bacterial band-pass filter. Proc Natl Acad Sci USA 106: 30. Getting PA (1989) Emerging principles governing the operation of neural
10135–40. networks.AnnuRevNeurosci12:185–204.
16. ConradE,MayoAE,NinfaAJ,ForgerDB(2008)Rateconstantsratherthan 31. Popescu IR, Frost WN (2002) Highly dissimilar behaviors mediated by a
biochemical mechanism determine behaviour of genetic clocks. J R Soc multifunctionalnetworkinthemarinemolluskTritoniadiomedea.JNeurosci
Interface5Suppl1:S9–15. 22:1985–93.
17. Polynikis A, Hogan SJ, di Bernardo M (2009) Comparing different ODE 32. BriggmanKL,KristanWB(2008)Multifunctionalpattern-generatingcircuits.
modelling approaches for gene regulatory networks. Journal of Theoretical AnnuRevNeurosci31:271–94.
Biology261:511–30. 33. TysonJJ,Nova´kB(2010)Functionalmotifsinbiochemicalreactionnetworks.
18. Alon U (2007) An Introduction to Systems Biology: Design Principles of AnnuRevPhysChem61:219–40.
BiologicalCircuits.ChapmanHall/CRC. 34. GuantesR,EstradaJ,PoyatosJF(2010)Trade-offsandnoisetoleranceinsignal
19. DoedelE(2007)AUTO07.Softwareforcontinuationandbifurcationproblems detectionbygeneticcircuits.PLoSONE5:e12314.
inordinarydifferentialequations. 35. Lutz R,Bujard H(1997) Independent and tight regulation of transcriptional
20. Kuznetsov YA (2004) Elements of Applied Bifurcation Theory (3rd Edition). units in Escherichia coli via the LacR/O, the TetR/O and AraC/I1-I2
Springer. regulatoryelements.NucleicAcidsRes25:1203–10.
PLoSONE | www.plosone.org 12 February2011 | Volume 6 | Issue 2 | e16140

---
**Source PDF:** `2022_50_article.pdf`
