TheThirty-FifthAAAIConferenceonArtificialIntelligence(AAAI-21)
|     |     |     | If  | You | Like | Shapley  | Then              | You’ll | Love | the | Core |     |     |     |     |

|     |     |     |     |     |      | TomYan,1 | ArielD.Procaccia2 |        |      |     |      |     |     |     |     |
1CarnegieMellonUniversity
2HarvardUniversity
tyyan@cmu.edu,arielpro@seas.harvard.edu
Abstract assignedpayoffsinawaythatsatisfiesfouraxioms;roughly
speaking,aplayer’spayoffistheiraveragemarginalcontri-
Theprevalentapproachtoproblemsofcreditassignmentin
butiontoacoalitionconsistingofotherplayers.
| machinelearning |     | —suchasfeatureanddatavaluation—is |     |     |     |     |     |     |     |     |     |     |     |     |     |

tomodeltheproblemathandasacooperativegameandap-
plytheShapleyvalue.Butcooperativegametheoryoffersa This intense focus on the Shapley value is surprising,
rich menu of alternative solution concepts, which famously however, as—once we have accepted that problems of
includesthecoreanditsvariants.Ourgoalistochallengethe credit assignment in machine learning can be modeled as
machinelearningcommunity’scurrentconsensusaroundthe cooperative games—there are a plethora of other solution
Shapley value, and make a case for the core as a viable al- concepts (Peleg and Sudho¨lter 2007). In particular, there is
ternative.Tothatend,weprovethatarbitrarilygoodapprox-
|     |     |     |     |     |     |     |     | a seminal | solution | concept |     | in cooperative |     | game | theory that |

imationstotheleastcore—acorerelaxationthatisalways
|     |     |     |     |     |     |     |     | is as prominent |     | as the | Shapley | value: | the | core. | This solu- |

feasible—canbecomputedefficiently(butproveanimpos-
tionconceptseekstoachievemaximalstabilityamongstall
| sibility | for a more | refined | solution | concept, |     | the nucleolus). |     |     |     |     |     |     |     |     |     |

possiblecoalitionsoftheplayersinthegame—anideathat
Wealsoperformexperimentsthatcorroboratethesetheoreti-
datesbacktothewritingsofEdgeworthonmarketequilib-
calresultsandshedlightonsettingswheretheleastcoremay
bepreferabletotheShapleyvalue. rium theory in 1881. Since then, it has found extensive ap-
plicationsineconomicsandbeyond(Telser1994).
Introduction
Specifically,accordingtothecore,thetotalpayofftoeach
Asmachinelearningsystemsbecomemorecapable,theyare
coalitionshouldbeatleastitsvalue.Whenthisisnotpossi-
increasinglyusedinoursocietytoautomatetasksandgen-
ble,themaximumdeficit(differencebetweenvalueandpay-
eratevalue.Thishasleadtoasurgeintheattentiongivento
|                |     |         |           |     |              |     |          | off) of | any coalition |     | should  | be minimized—this |        |         | is known |

| explainability | for | machine | learning: |     | how features |     | and data |         |               |     |         |                   |        |         |          |
|                |     |         |           |     |              |     |          | as the  | least core.   | The | (least) | core              | can be | seen as | a notion |
contributetotheperformanceofMLmodels.ToensureML of group fairness, in that each group of players (or coali-
modelsarefunctioningasintended,muchworkhasbeende-
|     |     |     |     |     |     |     |     | tion)gets | itsdues.Moreover, |     |     | itisespecially |     | aptinthe | val- |

votedtostudyingfeatureattribution:howthefeaturesused
uationsetting,wherethedatavendorsorfeatureannotators
torepresentthedatainfluencethemodel’spredictions(Co-
|     |     |     |     |     |     |     |     | are paid | in a | way that | disincentivizes |     | (to | the extent | possi- |

Sˇtrumbelj
hen, Dror, and Ruppin 2007; and Kononenko ble) any coalition of vendors from choosing to opt out and
2010; Datta et al. 2015; Datta, Sen, and Zick 2016; Lund- not contribute; if a coalition S if not paid at least its value
| berg and | Lee 2017; | Chen | et  | al. 2019). | Related | to  | feature |     |     |     |     |     |     |     |     |

v(S)thenthecoalitionwouldbebetteroffseparatingfrom
| attribution     | is data | valuation  |        | (Ghorbani | and          | Zou 2019; | Jia   |               |        |        |                  |         |           |             |            |

|                 |         |            |        |           |              |           |       | the so-called |        | grand  | coalition.       | Indeed, | the       | core values | may        |
| et al. 2019a,b; |         | Ohrimenko, | Tople, | and       | Tschiatschek |           | 2019; |               |        |        |                  |         |           |             |            |
|                 |         |            |        |           |              |           |       | be seen       | as the | set of | all economically |         | plausible |             | payoffs to |
Agarwal,Dahleh,andSarkar2019),whichstudieshowdata participantsthatcompensatethemfortheircontributions.
| points contribute |          | to model | performance.      |               | With               | ML        | models    |             |          |               |         |               |        |             |          |

| now generating    |          | profit   | for enterprises,  |               | this understanding |           | is        |             |          |               |         |               |        |             |          |
|                   |          |          |                   |               |                    |           |           | In this     | paper,   | we            | provide | a much        | needed | comparison  | of       |
| important         | in order | to       | fairly compensate |               | data               | suppliers | for       |             |          |               |         |               |        |             |          |
|                   |          |          |                   |               |                    |           |           | the two     | solution | concepts      | and     | show          | that   | the (least) | core is, |
| their training    | data.    | Central  | to                | both pursuits |                    | is an     | equitable |             |          |               |         |               |        |             |          |
|                   |          |          |                   |               |                    |           |           | practically | and      | conceptually, |         | an attractive |        | alternative | to the   |
meansofcreditassignment. Shapleyvalueforcreditassignmentinmachinelearning.In
| Virtually | all | papers, | including | every | single | paper | cited |     |     |     |     |     |     |     |     |

doingso,wehopetoraiseawarenessofthecoreasanatu-
above,deemtheShapleyvalue(orclosevariantsthereof)to
ralsolutionconceptforfaircreditassignment,challengethe
bethe“right”waytocarryoutcreditassignment.TheShap-
wide-rangingusageoftheShapleyvalueandinspireacloser
leyvalueisasolutionconceptfromcooperativegametheory
examinationofcaseswhereonesolutionconceptshouldbe
inwhichplayers—inthiscasefeaturesordatapoints—are preferredovertheother.Itisworthemphasizingthat,tothe
Copyright©2021,AssociationfortheAdvancementofArtificial bestofourknowledge,wearethefirsttoconsiderusingthe
Intelligence(www.aaai.org).Allrightsreserved. coreforexplainabilityofmachinelearningmodels.
5751

OurResults bounds on the sample complexity of three approximations
MuchliketheShapleyvalue,theprimaryobstacleinapply- ofthecore.
ing the concept of least core is computational complexity. Onatechnicallevel,ourdefinitionofapproximatenotions
Indeed,itisthesolutiontoalinearprogramwhosenumber ofleastcore(Theorems1and2)followthoseofBalkanskiet
ofconstraintsisexponentialinthenumberofplayers.Nev- al.(2017)forthecore,byeschewingtheassumptionthatthe
ertheless,weconstructaMonteCarloalgorithmthatrunsin core is nonempty; our proofs of these results directly build
polynomialtimeand(withgivenconfidence)outputsapay- on theirs. Our interpretation of these results is quite differ-
off allocation in the (cid:14)-probable least core—a slightly re- ent, though, because in our setting coalition values can be
laxedversionoftheleastcorewherethepayoffconstraints queried—for example, one can run a black-box predictor
may be violated by up to a (cid:14)-fraction of coalitions. When withaspecificsubsetoffeaturesandmeasureitsaccuracy—
thenumberofplayersislarge,though,thismaystillbein- sowethinkofourresultsasguaranteesontheperformance
tractable;wethereforeshowthatitispossibletofindasolu- of Monte Carlo algorithms. Balkanski et al. (2017) did not
tion in the ((cid:15);(cid:14))-probably approximate least core—whose study the nucleolus, so our negative result for the nucleo-
constraintsareadditionallyrelaxedby(cid:15)each—intimethat lus (Theorem 3)—which we view as our main theoretical
ispolylogarithmicinthenumberofplayers. result—isentirelynewandhasnoanalogintheirwork.Fi-
We also study a well-known refinement of the least core nally,theworkofBalkanskietal.(2017)ispurelytheoreti-
called the nucleolus. However, it turns out that results that cal,whereasourempiricalresultsstudyanddemonstratethe
are analogous to those for the least core are essentially applicability of the least core to credit assignment in ma-
unattainable.Informally,weprovethatanyalgorithmwould chinelearning.
havetorequireaccesstothevaluesofanexponentiallylarge
number of coalitions to compute a payoff allocation in the Preliminaries
((cid:15);(cid:14))-probablyapproximatenucleolus,whichagainrelaxes A cooperative game consists of a set of players N =
all relevant constraints by (cid:15) and allows a (cid:14)-fraction of the f1;:::;ngandacharacteristicfunctionv :2N !Rwhich
constraints to be violated. The juxtaposition of the positive assignsavaluetoeachcoalitionS (cid:18)N,suchthatv(;)=0;
computationalresultsfortheleastcoreandthenegativere- weassumethatv(S) (cid:21) 0andv(S) (cid:20) 1forallS (cid:18) N for
sult for the nucleolus provides a strong endorsement of the easeofexposition.Wethinkofv(S)asthepayoffthecoali-
former(somewhatcoarser)notionoverthelatter. tion S could obtain if it went it alone. Given such a game,
Inourexperiments,weverifythesetheoreticalresultsand weareinterestedinfindingapayoffallocation(alsoknown
confirm that our algorithm can compute the least core eas- asanimputation)x = (x ;:::;x ),wherex isthepayoff
1 n i
ily and that the nucleolus is difficult to compute. Next, we ofplayeri2N.Thepayoffallocationmustbeefficient,that
comparealgorithmsonewouldusetocomputetheShapley is,
valueagainstourleastcorealgorithmindatavaluationtasks. X
x =v(N):
i
Our results suggest that the least core algorithm compares
i2N
favorably with those of the Shapley value in low-resource
Apayoffallocationisinthee-coreifandonlyifthetotal
settingsthataretypicalofanalystswithoutaccesstolarge-
payoffofeachcoalitionisatleastitsvalue,uptoe:
scalecomputationalresources.
X
8S (cid:18)N; x +e(cid:21)v(S):
RelatedWork i
i2S
Thereisanentireareaofalgorithmicgametheorydevotedto
thecomputationofsolutionsofcooperativegames(Chalki- The core itself, by this definition, satisfies these con-
adakis,Elkind,andWooldridge2011).Inparticular,aslew straints with e = 0. Unfortunately, there are coopera-
ofpapershavestudiedthecomplexityofthecore,theleast tive games whose core is empty. But clearly the e-core is
core, and the nucleolus in specific classes of cooperative nonemptyifeislargeenough.
games (Deng and Papadimitriou 1994; Conitzer and Sand- The idea behind the least core (Maschler, Peleg, and
holm 2006; Bachrach and Rosenschein 2008; Elkind and Shapley 1979) is to choose the smallest e possible. It may
Pasechnik2009;Elkindetal.2009). bedefinedasthesetofallsolutionstothefollowinglinear
Our work is most closely related to that of Balkanski et program.
al. (2017). They study settings where solutions to cooper-
min e
ative games—specifically, the Shapley value and the core P
s.t. x =v(N) (1)
—are learned from samples consisting of coalitions and Pi2N i
x +e(cid:21)v(S) 8S (cid:18)N
their values. Like Balcan et al. (2015), they are motivated i2S i
by the observation that in classical applications of coop- Onecanthinkoftheleastcoreasthesetofpayoffallocations
erative games values of coalitions cannot be accessed via that require the smallest subsidy e? (the value of e in the
queries; for example, if the game represents company em- optimalsolutionto(1))toeachcoalitionsothat,ifthepayoff
ployees working together to complete tasks, it is impossi- toeachcoalitionwasboostedbye?,theallocationwouldbe
bletoknowwhichtaskswouldbecompletedhadaspecific inthecore.Thecoreisnonemptyifandonlyife? (cid:20)0.
coalition worked alone. Importantly, they do not consider We next consider a refinement of the least core, the nu-
explainabilityatall.Undertheassumptionthattheunderly- cleolus, first proposed by (Schmeidler 1969). Define the
inggamehasanonemptycore,Balkanskietal.(2017)give deficit of a payoff allocation x for a coalition S (cid:18) N to
5752

P
be v(S)(cid:0) x . The nucleolus is the payoff allocation onthesample;theprobableleastcoreguaranteewouldthen
i2S i
whosesortedlistofdeficitsacrossallcoalitionslexicograph- holdwithrespecttothatsameD.Inparticular,iftheuniform
ically dominates the list of deficits for any other payoff al- distributionovercoalitionsisused,theguaranteeholdswith
location. That is, the largest deficit (which will be positive respecttoa(1(cid:0)(cid:14))-fractionofallcoalitions.
if the core is empty) should be as small as possible; sub- WhileTheorem1isencouraging,apotentialdrawbackis
ject to that, the second largest deficit should be as small as thatthealgorithm’srunningtimeispolynomialinthenum-
possible,andsoon.Noticethat,inparticular,thenucleolus berofplayersn.Whilethisisanexponentialimprovement
minimizesthelargestdeficitandsoitsallocationdoesliein overna¨ıveleastcorecomputation,itcanstillbeanonstarter
theleastcore.Incontrasttotheleastcore,whichmaycon- whentheplayersarefeaturesinahigh-dimensionalspaceor
tain multiple payoff allocations, the nucleolus is known to datapoints.Wethereforedefinethe((cid:15);(cid:14))-probablyapprox-
beunique(Schmeidler1969). imateleastcoretobepayoffallocationssuchthat
" #
TheoreticalResults Pr X x +e?+(cid:15)(cid:21)v(S) (cid:21)1(cid:0)(cid:14):
i
Exact computation of the least core and the nucleolus re- S(cid:24)D
i2S
quires solving linear programs with as many constraints as
With this additional relaxation, we can obtain running
therearecoalitions,whichwouldtypicallybeprohibitively
time that is polynomial in log(n); the proof is relegated to
expensive. Our strategy, therefore, is to sample a relatively
thefullversionofthepaper.
smallnumberofcoalitionsfromanunderlyingdistribution,
and compute the desired solution concept on the sampled Theorem2. Givenacooperativegame(N;v),distribution
coalitions—this can be done in time that is polynomial in
D over2N,and(cid:14);(cid:1);(cid:15) > 0,solvingthelinearprogram(1)
over
t
l
h
ea
e
st
n
c
u
o
m
re
b
,
e
a
r
n
o
d
f
v
s
i
a
a
m
a
p
se
le
q
s
u
,
e
v
n
i
c
a
e
t
o
h
f
e
su
li
c
n
h
ea
li
r
n
p
ea
ro
r
g
p
r
r
a
o
m
gra
(
m
1)
s
f
f
o
o
r
r
t
t
h
h
e
e
(cid:28)2(cid:0)
logn+log
(cid:0)1(cid:1)(cid:1)!
O (cid:1)
nucleolus (Kopelowitz 1967). The hope is that this Monte (cid:15)2(cid:14)2
Carlo algorithm would give us a payoff allocation that ap-
proximates the desired one with respect to the underlying coalitions sampled from D, where (cid:28) = maxSv(S) , gives
minS6=;v(S)
distribution. apayoffallocationinthe((cid:15);(cid:14))-probablyapproximateleast
corewithprobabilityatleast1(cid:0)(cid:1).
ComputingtheLeastCore
We note that (cid:28) may be considered a constant in general.
WeknowfromtheworkofBalkanskietal.(2017)thatcom-
Forexample,inmulticlassclassificationitisnobiggerthan
putingtheleastcoreexactlyisanonstarter—theyprovean 1 =m,wheremisthenumberofclasses.
impossibilityevenforthecore,undertheassumptionthatit 1=m
isnonempty.Wethereforeconsiderapproximateversionsof ComputingtheNucleolus
theleastcore.
Theprobablyapproximateleastcorecanbeseenasrequir-
Given a cooperative game, let D be a distribution over
ing the deficit of “most” coalitions to be approximately at
2N,andlete?bethesubsidydefinedbytheleastcore—the
most the maximum deficit e? that defines the least core. In
optimalsolutiontoEquation(1).Apayoffallocationxisin
the(unique)nucleolus,though,thatdeficitisassociatedonly
the(cid:14)-probableleastcoreifandonlyif
withtheworst-offcoalition.Itisnaturaltoask,instead,that
" #
the deficit of “most” coalitions be approximately their own
X
Pr x i +e? (cid:21)v(S) (cid:21)1(cid:0)(cid:14): deficitunderthenucleolusallocation.
S(cid:24)D
i2S Formally, as before fix a cooperative game and a distri-
bution D. Denote by d?(S) the deficit of coalition S (cid:18) N
Thatis,theleastcoreconstraintisviolatedwithprobability
undertheuniquenucleolusallocation.Apayoffallocationx
atmost(cid:14)whencoalitionsaredrawnfromD.
isinthe((cid:15);(cid:14))-probablyapproximatenucleolusifandonlyif
Wehavethefollowingresult,whoseproofappearsinthe
fullversionofthepaper. "(cid:12) (cid:12)X (cid:12) (cid:12) #
Pr (cid:12) x +d?(S)(cid:0)v(S)(cid:12)(cid:20)(cid:15) (cid:21)1(cid:0)(cid:14):
Theorem 1. Given a cooperative game (N;v), distribu- (cid:12) i (cid:12)
S(cid:24)D (cid:12) (cid:12)
tion D over 2N, and (cid:14);(cid:1) > 0, solving the linear program i2S
(1)overO((n+log(1=(cid:1)))=(cid:14)2)coalitionssampledfromD Unfortunately, it turns out that any algorithm that com-
gives a payoff allocation in the (cid:14)-probable least core with putes the probably approximate nucleolus requires a num-
probabilityatleast1(cid:0)(cid:1). ber of samplesthat is exponential in the numberof players
n —a doubly exponential increase over the probably ap-
Itmayseemsurprisingthatsolvingthelinearprogram(1)
proximateleastcore!—asthefollowingtheoremshows.
with respect to a subset of the coalitions gives a guarantee
with respect to the unknown subsidy e?. But the estimated Theorem3. Letn(cid:21)9,(cid:15)<1=50,(cid:14) <1=200and(cid:1)<4=5.
deficite^withrespecttoasubsetofcoalitions(thatis,asub- Thenanydeterministicalgorithmthatforallgames(N;v)
setofconstraints)satisfiese^(cid:20)e?duetomonotonicity. onnplayers,andalldistributionsDonN,computesapay-
Also note that the choice of D rests with the algorithm off allocation in the ((cid:15);(cid:14))-probably approximate nucleolus
designer.Inotherwords,wecansamplecoalitionsfromany withprobabilityatleast1(cid:0)(cid:1)requiresaccesstothevalues
distribution D and compute an allocation in the least core of(cid:10)(2n=3)coalitionssampledfromD.
5753

The importance of Theorem 3 lies in the practical guid- marketpaperssuchasthatofGhorbaniandZou(2019).Put
ance it provides. Indeed, the stark contrast between The- another way, if the goal is to output scores that reflect and
orem 2 and 3 suggests that we should focus on approxi- may be interpreted as economically plausible payments in
mations of the least core, as natural approximations of the a competitive market, then the scores should be such that
(strongernotionof)nucleolusareessentiallybeyondreach. everycoalitioniscompensatedforatleastitsmarketvalue.
Eventhoughthetheoreticalresultisworst-caseinnature,we This is so that the agents in the coalitions, who are ratio-
showinSection thatitsimplicationholdsinpractice. nal, do not elect to leave the grand coalition. Contrast this
Wealsonotethatthetheoremstatementdealswithalgo- with the Shapley value, which confers only a generic no-
rithmsthataredeterministic,uptotherandomsamplingof tion of “importance” (where relatively bigger means more
coalitionsfromD.However,itisnotdifficulttoextendthe “important”)andmaynotnecessarilycorrespondtoaneco-
theoremtodealwithrandomizedalgorithmstoo,atthecost nomically feasible set of payoffs (as we will see in the ex-
| ofcomplicatingtheprooffurther.Moreover,theconstantsin |     |     |     |     |     |     |     | periments). |     |     |     |     |     |     |     |

thetheoremstatementcancertainlybeimproved,butwedo
BehavioralStudies.Studiesinbehavioralgametheoryhave
notviewtheirexactvaluesasbeingimportant.
|     |     |     |     |     |     |     |     | found the | core | to be predictive |     | of payment | distribution |     | in  |

marketsettings,suggestingthatpeopleperceivethecoreas
Interlude:AComparisonoftheCoreandthe
afairschemefordividingupthetotalpayoffs;bycontrast,
ShapleyValue the Shapley value has received “weaker empirical support”
(Williams1988).Thisisanespeciallycompellingreasonto
Nowthatwehaveestablishedthatitisviabletocomputethe
preferthecoreovertheShapleyvalue:sincethestakehold-
| least core, | we  | turn to | the conceptual |     | part of | our argument. |     |     |     |     |     |     |     |     |     |

ersinvolvedwithmachinelearningareoftenpeople,itisim-
BeforegoingintohowtheleastcoreandtheShapleyvalue
perativetoemployasolutionconceptthatisconsistentwith
differ(weincludeacommentonwhenthetwoareknownto
theirbehaviorandintuition(Bhattetal.2019;Kumaretal.
coincideinSection),onethingtonoteabouttheleastcore
|            |          |               |     |         |             |     |          | 2020). Indeed, |     | while much | is  | still unclear | as  | to how | to as- |

| is that it | is a set | of solutions, |     | whereas | the Shapley |     | value is |                |     |            |     |               |     |        |        |
sign“importancescores”ininterpretabilitysoastotrulyaid
| a point | solution | concept. | To  | compare | the two | conceptually |     |     |     |     |     |     |     |     |     |

stakeholders,thereexistsampleeconomicliteratureonhow
(andexperimentallyaswell),webreaktiesbyselectingthe
toequitablypaypeopleandthecoreisonesuchprominent
| payoffallocationintheleastcorewiththesmallest‘ |     |     |     |     |     |     | norm. |          |       |             |     |                 |     |        |        |

|                                                |     |     |     |     |     |     | 2     | concept, | which | we champion |     | as a principled |     | way to | assign |
Thisisknownastheegalitarianleastcore.
thesescoresinthevaluationsetting.
| Axiomatic | Properties. |           | The     | Shapley | value          | has | almost |              |               |     |               |     |            |         |       |

|           |             |           |         |         |                |     |        | Negative     | Computational |     | Results       | for | Shapley.   | Similar | to    |
| always    | been        | justified | through | its     | four axiomatic |     | prop-  |              |               |     |               |     |            |         |       |
|           |             |           |         |         |                |     |        | our negative | result        | for | the nucleolus |     | in Theorem | 3,      | prior |
Sˇtrumbelj
erties (Cohen, Dror, and Ruppin 2007; and work has also produced negative results for the computa-
Kononenko2010;Datta,Sen,andZick2016;Lundbergand tionoftheShapleyvalue.Indeed,theShapleyvalueisdiffi-
Lee2017;Chenetal.2019):(i)efficiency(ii)symmetry(iii) culttoapproximate,nottomentioncomputeexactly.Infor-
nullplayer(iv)linearity.Ifweacceptthisargument,thenthe
mally,Bachrachetal.(2010)showthatnopolynomial-time
| egalitarian | least | core | is quite | attractive | in satisfying |     | all but |            |           |     |           |              |     |          |      |

|             |       |      |          |            |               |     |         | randomized | algorithm |     | can build | a confidence |     | interval | with |
thelastaxiom(linearity). smallaccuracy.AndBalkanskietal.(2017)showthatthere
Whiletheleastcore’slackoflinearityisostensiblyadis- existgamessuchthattheShapleyvaluecannotbeapproxi-
advantage, it is unclear to us why it is an essential prop- matedfromsamplesovertheuniformdistribution.
ertyforimportancescores.Thenecessityoflinearityiscom-
|     |     |     |     |     |     |     |     | In light | of these | negative |     | results, | the latest | state | of the |

monlyjustifiedbydefiningacooperativegameforeachtest
|     |     |     |     |     |     |     |     | art algorithms | for | computing |     | the Shapley | value | (Ghorbani |     |

point with the coalitional value being the model accuracy and Zou 2019; Jia et al. 2019a) either turn to simpler
with respect to that point. And so, one would desire that Monte-Carloapproachesthatdonotenjoytheoreticalguar-
summing the importance scores across these games would antees(GhorbaniandZou2019)ormorecomplicatedalgo-
yieldthescoreofthegamecorrespondingtotheentiretest
|     |     |     |     |     |     |     |     | rithms that | leverage | assumptions |     | such | as sparsity | to  | obtain |

set(GhorbaniandZou2019).However,inthisvein,onecan
|     |     |     |     |     |     |     |     | sizablesavingsinsamplecomplexity |     |     |     |     | (Jiaetal.2019a).By |     |     |

simplydefineadifferentgame,withthecoalitionalvaluebe- contrast,weprovideasimpleralgorithmforcomputingthe
ingthemodelaccuracywithrespecttotheentiretestset,in approximateleastcorewithprobableguarantees.
theverybeginning,thusobviatingtheneedforthisproperty Butdothesetheoreticalresultstranslateintopractice?In
tohold.1 the next section we show, among other things, that in low-
| By contrast, |     | the stability |     | axiom, | which | the egalitarian |     |     |     |     |     |     |     |     |     |

resourcesettings(wherethealgorithmhaslimitedcomputa-
leastcoredoessatisfy,iscrucialifwearetoadopttheeco- tionalpower)ourleastcorealgorithmoutperformsstate-of-
nomicmotivationbehinddatavaluation,asdescribedindata the-artalgorithmsfortheShapleyvalue,therebybolstering
thecomputationalcaseinfavoroftheleastcore.
| 1We | do note | that the | core satisfies | “approximate |     | linearity” | in  |     |     |     |     |     |     |     |     |

the following sense: An e -core under coalition function v and EmpiricalResults
|                                          |     |     | 1   |     |                      |               | 1   |                                                      |     |     |     |     |     |     |     |

| ane -coreundercoalitionfunctionfunctionv |     |     |     |     |                      | canbecombined |     |                                                      |     |     |     |     |     |     |     |
| 2                                        |     |     |     |     | 2                    |               |     | Thepurposeofthissectionistwofold.First,Weempirically |     |     |     |     |     |     |     |
| intoanallocationthatsatisfiesthe(e       |     |     |     | +e  | )-coreundercoalition |               |     |                                                      |     |     |     |     |     |     |     |
|                                          |     |     |     | 1   | 2                    |               |     |                                                      |     |     |     |     |     |     |     |
function v +v (though certainly the least core could be better verifyourtheoreticalconclusionsaboutthecomputabilityof
|     | 1   | 2   |     |     |     |     |     |     |     |     |     |     |     |     |     |

thanjustsummingtheleastcoreallocationsacrossthetwogames). theleastcoreandnucleolus(whichareworstcaseinnature).
5754

(cid:14).
|     |     |     |     |     |     |     | Theorem | 3, by      | contrast, | asserts  | that        | many | samples are |

|     |     |     |     |     |     |     | needed  | to compute | the       | probably | approximate |      | nucleolus.  |
Sincethisisaworst-caseresult,onemaywonderwhetherit
holdsinpractice.Tocheckthis,weapplythesamemethod-
|     |     |     |     |     |     |     | ology as         | above. | As can     | be seen | in Figure | 1,      | even when a              |

|     |     |     |     |     |     |     | sizable fraction |        | of samples | are     | used to   | compute | the ((cid:15);(cid:14))- |
probablyapproximatenucleolus,mostcoalitionsdonotsat-
isfyitsconstraints.
DataValuation
Oursecondsetofexperimentsdealswithdatavaluation.We
focusonlow-resourcesettingsinwhichweassumethean-
|     |     |     |     |     |     |     | alyst who | is looking | to  | understand | data | importance | has ac- |

cesstolimitedcomputationalresources(e.g.,fewcores,no
|     |     |     |     |     |     |     | pun intended). | We         | examine | the         | performance | of   | existing al-  |

|     |     |     |     |     |     |     | gorithms       | that one   | would   | use.        | To compare, | we   | elect to fix  |
|     |     |     |     |     |     |     | the sample     | complexity |         | (the number | of          | v(S) | queries) that |
thealgorithmsarepermittedtouse.Thissidestepscompar-
|     |     |     |     |     |     |     | ing the | actual runtimes |     | of the | algorithms, | which | may vary |

Figure1:TopPanel:Leastcoreaccuracy(satisfactionofthe
|                  |     |                  |        |        |           |     | depending      | on the  | details | of the     | implementation. |     | The two     |

| core constraint) |     | over coalitions. | Bottom | Panel: | Nucleolus |     |                |         |         |            |                 |     |             |
|                  |     |                  |        |        |           |     | data valuation | Shapley |         | algorithms | we compare      |     | against are |
accuracy(satisfactionofthecoreconstraint)overcoalitions
TMC(GhorbaniandZou2019)andGroupTesting(Jiaetal.
((cid:15)=0:01).
2019a).Pleasenotethattheexperimentsweconductbelow
|     |     |     |     |     |     |     | emulate | thecurrent, | goldstandard |     | forevaluating |     | feature or |

datavaluationmethods,whichistoaddorremovefeatures
| Second, | we compare | the algorithms |     | that one | would | use to |     |     |     |     |     |     |     |

ordataasrankedbythemethodandusetheresultantmodel
approximatetheShapleyvaluewiththatforleastcore.
accuracyasanindicatorofthe“goodness”ofthevaluation.
| Our experiments |     | are conducted | on  | feature | valuation | and |     |     |     |     |     |     |     |

data valuation tasks. Following previous work in the area, Data Removal. We emulate the data removal experiments
our primary aim is to use these tasks to confirm that least asdescribedbyGhorbaniandZou(2019).Inthissetofex-
corevaluesarepredictiveofimportance,albeitinanindirect periments,thedataisrankedfrommostvaluabletotheleast
way(astheultimatetestofhuman-centeredAImustbehow
valuableusingthesolutionconcepts,andthemodelperfor-
thesysteminteractswithpeople). manceischartedasthemostvaluable/leastvaluablefiveper-
centofthedataisremovedatatime.Inadditiontothetwo
FeatureValuation Shapleyalgorithmswealsoincludetwobaselines:leaveone
|     |     |     |     |     |     |     | out(LOO),definedasv(N)(cid:0)v(N |     |     |     | nfig)foreachplayeri, |     |     |

Wechoosethreesmaller-scaleUCIdatasets(DuaandGraff
2017) that have 10–14 features: this makes it computation- andrandomscoreassignment.
allyfeasibletotrainalogisticregressionclassifieronallpos- For the synthetic data generation, we sample 200 data
sible subsets of features and to compute the exact Shapley points from 50-dimensional Gaussian, the 50-dimensional
and least core values. To define the cooperative game, the parametersaresampledfromauniformdistributionandthe
|     |     |     |     |     |     |     | feature-label | relationship |     | is set | to be linear. | To  | define the |

playersarethefeaturesandthevalueofacoalitionisthetest
accuracyofalogisticregressionclassifierthatistrainedon cooperative game, we take the players to be the data and
thosefeatures.Thethreereal-worlddatasetsareofdifferent thevalueofacoalitiontobethetestaccuracyofthemodel
domains:house(classifyingthepartyofCongressmenbased trained only on the data in the coalition. The model used
on their votes on issues), medical (predicting the presence hereislogisticregression;werelegateresultsforneuralnet-
images,andchemical workstothefullversionofthepaper.Werepeattheproce-
| ofbreast | cancerbased | onfeaturesof |     |     |     |     |     |     |     |     |     |     |     |

(classifyingtheoriginofwinebasedonchemicalanalysis). dure20timesandobtain95percentconfidenceintervalsfor
To empirically verify Theorem 1 from Section 3 (which themeanmodelperformance.
dealswiththeprobableleastcore),wesampleasmallfrac- Forthenaturaldataset,weusethedog-vs-fishclassifica-
tion of coalitions uniformly at random from all possible tion dataset as in the work of Koh and Liang (2017) and
coalitions, and compute the least core by restricting Equa- Ghorbani and Zou (2019). We randomly sample 600 data
tion(1)tothesecoalitions.Wethendeterminewhatfraction pointsandobtainfeaturesoftheimagesusingInceptionnet-
ofallcoalitionssatisfytheleastcoreconstraintswithrespect work.Themodelusedfortrainingislogisticregressionand
tothetruedeficite?—thatgivesusaccuracy1(cid:0)(cid:14),which,in wevarythebudgetasbefore.Thisentireprocessisrepeated
turn,leadsto(cid:14)-probableleastcore.Toobtainerrorbars,we fivetimestoobtaintheerrorbars.
repeatthistentimes.AscanbeseeninFigure1,evenwith Weexperimentwithabudgetof5K;10K;25K;50K for
a small fraction of sampled coalitions, the resultant alloca- samplesasinalow-resourcesetting.Asapointofreference,
tions are (cid:14)-probable least core allocations with very small forthesyntheticdataexperiment,computingtheexactleast
5755

(a)Syntheticdata,removebest,10Ksamples (b)Syntheticdata,removebest,50Ksamples
(c)Naturaldata,removebest,10Ksamples (d)Naturaldata,removebest,50Ksamples
(e)Syntheticdata,removeworst,10Ksamples (f)Syntheticdata,removeworst,50Ksamples
(g)Naturaldata,removeworst,10Ksamples (h)Naturaldata,removeworst,50Ksamples
Figure2:Curvesoflogisticregressiontestperformancewhenthebestandworstdatapointsrankedaccordingtothesolution
concepts are removed. In (a)–(d) the best data points are removed: the steeper the drop, the better. In (e)–(h) the worst data
pointsareremoved:thesharpertherise,thebetter.
5756

|     |     |     |     |     |     | to the noised | portion | and | compute | the | percentage | of  | utility |

allocatedbythecoretothecleandata.Asexpectedandseen
inFigure3,withhighernoise,thenoiseddatabecomeless
“valuable”andarethusallocatedalowerpercentageofthe
overallutilitybythecore.
FixingMislabeledData.Weperformanothersetofexper-
|     |     |     |     |     |     | iments to        | verify    | that the  | magnitude      | of     | the least | core        | values  |

|     |     |     |     |     |     | strongly         | correlate | with      | the importance |        | of the    | data point. | In      |
|     |     |     |     |     |     | this experiment, |           | we assume | we             | have a | dataset   | with        | flipped |
labelsandwouldliketousetheimportancescoresassigned
|     |     |     |     |     |     | to expedite       | the       | correction | of    | “flipped”      | data points, |        | which   |

|     |     |     |     |     |     | should correspond |           | to the     | lower | scores.        | The specific |        | dataset |
|     |     |     |     |     |     | we use is         | the Enron | Dataset,   |       | as in previous |              | work   | (Ghor-  |
|     |     |     |     |     |     | bani and          | Zou 2019; | Koh        | and   | Liang 2017).   | In           | total, | 1000    |
Figure3:Plottingnoiselevelagainstpercentageoftotalutil-
datapointsareusedfortrainingaNaiveBayesmodelwhich
ityassignedtocleandata.
|     |     |     |     |     |     | takes as input | a        | bag-of-words |            | representation | of  | emails.      | We  |

|     |     |     |     |     |     | randomly       | flip the | label        | for twenty | percent        | of  | the data     | and |
|     |     |     |     |     |     | allot a budget | of       | 5000         | samples    | for computing  |     | the solution |     |
concepts.Thecoalitionalvaluesaredefinedasperformance
|     |     |     |     |     |     | on the validation |             | set, and | then      | the final | performance |           | in the |

|     |     |     |     |     |     | plot is assessed  |             | on the   | test set. | As can    | be seen     | in Figure | 4,     |
|     |     |     |     |     |     | the least         | core values | are      | much      | better at | picking     | out       | lower  |
qualitydatapointsthanrandomselection.
|     |     |     |     |     |     | Is the Approximate |             | Shapley  |            | value in        | the Approximate |              |      |

|     |     |     |     |     |     | Least Core?        | It          | is known | that       | the Shapley     | value           | coincides    |      |
|     |     |     |     |     |     | with the           | egalitarian | core     | for convex | games,          | where           | there        | is   |
|     |     |     |     |     |     | a super-additive   |             | effect   | in players | coming          | together.       | This         | ef-  |
|     |     |     |     |     |     | fect is not        | typically   | present  | in         | what we         | call            | “supervised- |      |
|     |     |     |     |     |     | learning”          | games,      | in which | there      | are diminishing |                 | returns      | as   |
|     |     |     |     |     |     | more and           | more        | data or  | features   | are added       | and             | used.        | How- |
Figure 4: Test performance as we correct more and more ever, in theory it may still be the case that the two solu-
|     |     |     |     |     |     | tions usually | coincide, |     | which | would make | it  | redundant | to  |

trainingdataguidedbytheleastcorevs.randomselection.
|     |     |     |     |     |     | discuss the | core. | We therefore |     | test, in the | valuation |     | experi- |

mentsmentionedabove,whetherapproximateShapleyval-
coreuses2200samples.TheTMCAlgorithmwithastopping ues are close to being in the approximate least core. Our
resultssuggestthatthisisnotthecaseandthereforetheap-
| threshold | of less | than | one percent change | in  | the estimated |     |     |     |     |     |     |     |     |

proximateShapleycannotserveasaproxyfortheleastcore.
| Shapley | value uses | 2:17M | samples when | run | until conver- |     |     |     |     |     |     |     |     |

Detailsarerelegatedtothefullversionofthepaper.
| gence. For | the Group |         | Testing Algorithm, | using | the sample  |     |     |            |     |     |     |     |     |

| complexity | derived,  | running | till convergence   |       | uses 11:05M |     |     |            |     |     |     |     |     |
| samples.   |           |         |                    |       |             |     |     | Discussion |     |     |     |     |     |
AscanbeseeninFigure2(withsimilarfiguresforother
parametersettingsgiveninthefullversionofthepaper),the In our paper, we provide theoretical and empirical results,
| least core | algorithm | compares | favorably | with | the Shapley |            |      |            |           |     |          |         |      |

|            |           |          |           |      |             | along with | with | conceptual | arguments |     | (Section | ), that | sug- |
algorithmsintermsofpredictingthemostandleastimpor- gest the least core is a principled, alternative means of do-
tant (in a sense) data points in these settings. Specifically, ingcreditassignmentinML.Currently,itappearsthatvirtu-
the least core’s performance is significantly better than the allyallpapersonfeatureanddatavaluationusetheShapley
baselinesinthesyntheticsetting,whereasinthenaturalset- valueforthispurpose.Inlightofthemanyusesofthecore
tingitisslightlybetterthanShapleyvaluecomputationvia asaneconomicallyplausiblemethodofpayoffassignment,
thestrongerofthetwoalgorithms. weintroducethisalternativeapproachtotheAIcommunity
Itisworthpointingoutthattheformulationofleastcoreis in the hope invoking further discussion on when and why
suchthatitcapturesagroupmeasureofvalue,whereasthe onesolutionconceptistobepreferred.
Shapleyvalueismoreofanindividualmeasure.Therefore,
Lastly,wewishtonotethatoutsideofthecomparisonof
this data removal setup should conceptually favor Shapley, solution concepts, one limitation that is shared by both the
andyettheleastcoreoutperformsittosomedegree. core and the Shapley value is that they are not suitable for
As one more sanity check, we conduct an experiment non-additivemodels(Kumaretal.2020).Thisproblemisan
studying the percentage of utility allocated by the core to artifactofthegamesetupandnotthesolutionconcept.Itis
noisy data. We divide the dataset into two: a clean portion another important issue that the community would need to
andanoisedportion.WeincreasetheGaussiannoiseadded cometoaconsensuson.
5757

Acknowledgments Deng,X.;andPapadimitriou,C.H.1994. OntheComplex-
|           |     |           |           |     |              |         | ity of Cooperative |     | Solution |     | Concepts. | Mathematics |     | of Op- |

| This work | was | partially | supported | by  | the National | Science |                    |     |          |     |           |             |     |        |
Foundation under grants CCF-2007080, IIS-2024287 and erationsResearch19(2):257–266.
CCF-1733556; and by the Office of Naval Research un- Dua,D.;andGraff,C.2017. UCIMachineLearningRepos-
der grant N00014-20-1-2488. Tom Yan is supported by a itory. URLhttp://archive.ics.uci.edu/ml.
| U.S. National |     | Science Foundation |     | Graduate | Research | Fel- |         |               |     |     |     |           |     |         |

|               |     |                    |     |          |          |      | Elkind, | E.; Goldberg, |     | L.  | A.; | Goldberg, | P.  | W.; and |
lowship.
|     |     |     |     |     |     |     | Wooldridge,               | M.  | J. 2009. | On  | the Computational      |     |     | Complex- |

|     |     |     |     |     |     |     | ityofWeightedVotingGames. |     |          |     | AnnalsofMathematicsand |     |     |          |
References
ArtificialIntelligence56:109–131.
Agarwal,A.;Dahleh,M.A.;andSarkar,T.2019.AMarket-
|                                     |     |            |              |     |                 |             | Elkind,E.;andPasechnik,D.B.2009. |          |        |     |        | ComputingtheNu- |     |        |

| placeforData:AnAlgorithmicSolution. |     |            |              |     | InProceedingsof |             |                                  |          |        |     |        |                 |     |        |
|                                     |     |            |              |     |                 |             | cleolus of                       | Weighted | Voting |     | Games. | In Proceedings  |     | of the |
| the 20th                            | ACM | Conference | on Economics |     | and             | Computation |                                  |          |        |     |        |                 |     |        |
20thAnnualACM-SIAMSymposiumonDiscreteAlgorithms
(EC),701–726.
(SODA),327–335.
| Bachrach, | Y.; Markakis, |     | E.; Resnick, |     | E.; Procaccia, | A. D.; |           |     |          |          |     |               |     |           |

|           |               |     |              |     |                |        | Ghorbani, | A.; | and Zou, | J. 2019. |     | Data Shapley: |     | Equitable |
Rosenschein, J. S.; and Saberi, A. 2010. Approximat- Valuation of Data for Machine Learning. In Proceedings
| ing power | indices: | theoretical |     | and empirical | analysis. | Au- |             |               |     |            |     |            |     |          |

|           |          |             |     |               |           |     | of the 36th | International |     | Conference |     | on Machine |     | Learning |
tonomousAgentsandMulti-AgentSystems20(2):105–122.
(ICML),2242–2251.
Bachrach,Y.;andRosenschein,J.S.2008.CoalitionalSkills
Jia,R.;Dao,D.;Wang,B.;Hubis,F.A.;Hynes,N.;Gu¨rel,
Games. InProceedingsofthe7thInternationalConference
|     |     |     |     |     |     |     | N. M.; Li, | B.; | Zhang, | C.; Song, | D.; | and Spanos, |     | C. 2019a. |

onAutonomousAgentsandMulti-AgentSystems(AAMAS),
|     |     |     |     |     |     |     | Towards | Efficient | Data | Valuation |     | Based | on the | Shapley |

1023–1030. Value. InProceedingsofthe22ndInternationalConference
Balcan,M.-F.;Procaccia,A.D.;andZick,Y.2015. Learn- on Artificial Intelligence and Statistics (AISTATS), 1167–
| ing Cooperative |     | Games. | In Proceedings |     | of the | 24th Inter- | 1176. |     |     |     |     |     |     |     |

nationalJointConferenceonArtificialIntelligence(IJCAI),
Jia,R.;Dao,D.;Wang,B.;Hubis,F.A.;Hynes,N.;Gu¨rel,
475–482.
|     |     |     |     |     |     |     | N. M.; Li, | B.; | Zhang, | C.; Spanos, |     | C.; and | Song, | D. 2019b. |

Balkanski,E.;Syed,U.;andVassilvitskii,S.2017. Statisti- EfficientTask-SpecificDataValuationforNearestNeighbor
calCostSharing. InProceedingsofthe31stAnnualConfer- Algorithms. ProceedingsoftheVLDBEndowment 12(11):
| enceonNeuralInformationProcessingSystems(NeurIPS), |     |     |     |     |     |     | 1610–1623. |     |     |     |     |     |     |     |

6221–6230.
|     |     |     |     |     |     |     | Koh, P. | W.; and | Liang, | P.  | 2017. | Understanding |     | black- |

Bhatt, U.; Xiang, A.; Sharma, S.; Weller, A.; Taly, A.; Jia, box predictions via influence functions. In Proceedings
Y.; Ghosh, J.; Puri, R.; Moura, J. M. F.; and Eckersley, of the 34th International Conference on Machine Learning
P. 2019. Explainable Machine Learning in Deployment. (ICML),1885–1894.
arXiv:1909.06342. Kopelowitz, A. 1967. Computation of the kernels of sim-
Chalkiadakis, G.; Elkind, E.; and Wooldridge, M. 2011. ple games and the nucleolus of N-person games. RM
ComputationalAspectsofCooperativeGameTheory. Mor- 31, Department of Mathematics, the Hebrew University of
| gan&Claypool. |     |     |     |     |     |     | Jerusalem. |     |     |     |     |     |     |     |

Chen, J.; Song, L.; Wainwright, M. J.; and Jordan, M. I. Kumar,I.E.;Venkatasubramanian,S.;Scheidegger,C.;and
2019. L-Shapley and C-Shapley: Efficient Model Interpre- Friedler, S. 2020. Problems with Shapley-value-based ex-
tationforStructuredData. InProceedingsofthe7thInter- planationsasfeatureimportancemeasures. InProceedings
nationalConferenceonLearningRepresentations(ICLR). of the 37th International Conference on Machine Learning
(ICML).
| Cohen,S.;Dror,G.;andRuppin,E.2007. |     |     |     |     | FeatureSelection |     |     |     |     |     |     |     |     |     |

via Coalitional Game Theory. Neural Computation 19(7): Lundberg,S.M.;andLee,S.-I.2017.AUnifiedApproachto
1939–1961. InterpretingModelPredictions. InProceedingsofthe30th
|           |         |           |     |       |            |         | Annual Conference |     | on  | Neural | Information |     | Processing | Sys- |

| Conitzer, | V.; and | Sandholm, | T.  | 2006. | Complexity | of Con- |                   |     |     |        |             |     |            |      |
tems(NeurIPS),4768–4777.
structingSolutionsintheCoreBasedonSynergiesAmong
ArtificialIntelligence170(6–7):607–619.
Coalitions. Maschler,M.;Peleg,B.;andShapley,L.S.1979.Geometric
|            |        |                |     |        |           |          | Properties | of the                                   | Kernel, | Nucleolus, |     | and | Related | Solution |

| Datta, A.; | Datta, | A.; Procaccia, |     | A. D.; | and Zick, | Y. 2015. |            |                                          |         |            |     |     |         |          |
|            |        |                |     |        |           |          | Concepts.  | MathematicsofOperationsResearch4(4):303– |         |            |     |     |         |          |
InfluenceinClassificationviaCooperativeGameTheory.In
338.
| Proceedings | of  | the 24th | International |     | Joint Conference | on  |     |     |     |     |     |     |     |     |

ArtificialIntelligence(IJCAI),511–517. Ohrimenko, O.; Tople, S.; and Tschiatschek, S. 2019.
|            |      |         |          |       |             |        | Collaborative |     | Machine | Learning |     | Markets | with | Data- |

| Datta, A.; | Sen, | S.; and | Zick, Y. | 2016. | Algorithmic | Trans- |               |     |         |          |     |         |      |       |
parencyviaQuantitativeInputInfluence:TheoryandExper- Replication-RobustPayments. arXiv:1911.09052.
iments with Learning Systems. In Proceedings of the 37th Peleg,B.;andSudho¨lter,P.2007.IntroductiontotheTheory
IEEESymposiumonSecurityandPrivacy(S&P),598–617. ofCooperativeGames. Springer,2ndedition.
5758

| Schmeidler, | D.    | 1969. | The Nucleolus | of         | a Characteristic |     |

| Function    | Game. | SIAM  | Journal       | on Applied | Mathematics      |     |
17(6):1163–1170.
Sˇtrumbelj,
|           | E.;           | and Kononenko,  | I.  | 2010. | An Efficient | Ex-     |

| planation | of Individual | Classifications |     | using | Game         | Theory. |
JournalofMachineLearningResearch11:1–18.
| Telser,L.G.1994. |     | TheUsefulnessofCoreTheoryinEco- |     |     |     |     |

nomics. JournalofEconomicPerspectives8(2):151–164.
| Williams, | M.       | A. 1988.  | An empirical | test    | of cooperative |      |

| game      | solution | concepts. | Behavioral   | Science | 33(3):         | 224– |
237.
5759

---
**Source PDF:** `2023_36_article.pdf`
