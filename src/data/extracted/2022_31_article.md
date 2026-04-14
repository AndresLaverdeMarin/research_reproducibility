Replication/MLReproducibilityChallenge2021
R E S C I E N C E C [Re] Value Alignment Verification
SibaSmarakPanigrahi1,2,ID andSohanPatnaik1,2,ID
1EqualContributions–2IndianInstituteofTechnologyKharagpur,India
Editedby
KoustuvSinha,
SharathChandraRaparthy Reproducibility Summary
Reviewedby
AnonymousReviewers ScopeofReproducibility
Received
Themaingoalofthepaper”ValueAlignmentVerification”[1]istotestthealignmentof
04February2022
arobot’sbehaviorefficientlywithhumanexpectationsbyconstructingaminimalsetof
Published questions. Toaccomplishthis,theauthorsproposealgorithmsandheuristicstocreate
23May2022 the above questionnaire. They choose a wide range of gridworld environments and a
continuousautonomousdrivingdomaintovalidatetheirputforthclaims. Weexplore
DOI
value alignment verification for gridworlds incorporating a non‐linear feature reward
10.5281/zenodo.6574687
mappingaswellasanextendedactionspace.
Methodology
Were‐implementedthepipelinewithPythonusingmathematicallibrariessuchas
numpyandscipy. Wespentapproximatelytwomonthsreproducingthetargetedclaims
inthepaperwiththefirstmonthaimedatreproducingtheresultsforalgorithmsand
heuristicsforexactvaluealignmentverification. Thesecondmonthfocusedonextending the action space, additional experiments, and refining the structure of our code.
Sinceourexperimentswerenotcomputationallyexpensive,wecarriedouttheexperimentsonCPU.Thecodeisavailableathttps://github.com/AIExL/vav_rc2021.
Results
Thetechniquesproposedbyauthorsin[1]cansuccessfullyaddressthevaluealignment
verificationproblemindifferentsettings. Weempiricallydemonstratetheeffectiveness
oftheirproposalsbyperformingexhaustiveexperimentswithseveralvariationstotheir
originalclaims. Weshowhighaccuracyandlowfalsepositiveandfalsenegativeratesin
thevaluealignmentverificationtaskwithaminimumnumberofquestionsfordifferent
algorithmsandheuristics.
Whatwaseasy
The problem statement, as well as the implementation of algorithms and heuristics,
werestraightforward. Wealsotookaidfromtheoriginalrepositorypublishedwiththe
paper. However, we implemented the entire pipeline from scratch and incorporated
severalvariationstoourcodetoperformadditionaldesignedexperiments.
Copyright©2022S.S.PanigrahiandS.Patnaik,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoSibaSmarakPanigrahi(sibasmarak.p@gmail.com)
Theauthorshavedeclaredthatnocompetinginterestsexist.
Codeisavailableathttps://github.com/AIExL/vav_rc2021.–SWHswh:1:dir:4d43ea96458cc573dd2b57208fae0b12f8da896f.
Openpeerreviewisavailableathttps://openreview.net/forum?id=BFLM3nMmhCt.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 1


Whatwasdifficult
Comprehendingdifferentalgorithmsandheuristicsproposedinpriorworksalongwith
their mathematical formulation and reasoning for their success in the given task was
considerablydifficult. Additionally,theoriginalcodebasehadseveralredundantfiles,
whichcreatedinitialconfusion. Weiteratedanddiscussedtheargumentsinthepaper
andpriorworkseveraltimestothoroughlyunderstandthepipeline. Nevertheless,once
thebasicswereclear,theimplementationwascomparativelysimple.
Communicationwithoriginalauthors
Wereachedouttotheauthorsnumeroustimesviaemailtoseekclarificationsandadditionalimplementationdetails. Theauthorswereincrediblyreceptivetoourinquiries,
andweappreciatetheirthoroughandpromptresponses.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 2


## 1 Introduction
Autonomous agents are used for complex, challenging, riskier, and dangerous tasks
whichbringsuptheneedofverifyingwhethertheagentsactinawaythatisbothoptimal
andsafew.r.tanotheragentthathasalreadybeenperformingthesaidtask(example,a
humanagent). Thisproblemofverifyingthealignmentofoneagent’sbehaviorw.r.tanotheragentisknownasValueAlignmentVerification. Theoriginalpaper[1]proposesa
framework for efficient value alignment verification. They discuss three different settingsofincreasingdifficultyintermsofverification:
1. explicithuman,explicitrobot: whereboththeagentsarecompletelyawareoftheir
rewardfunctions.
2. explicithuman,implicitrobot: wherethehumanagentisawareofitsrewardfunctionbuttherobotagentcanonlybequeriedaboutitsactionpreferencesondifferentstates.
3. implicithuman,implicitrobot: wheretheonlybasisofvaluealignmentisthrough
preferencesovertrajectories.
Dependingonthesetting,valuealignmentcanbeeitherexactorapproximate. Wetryto
reproduceandvalidatetheresultsfortheproposedframeworkonthefirstandsecond
setting,i.e.,(explicithuman,explicitrobot)and(explicithuman,implicitrobot). Theexperimentsinvolvegridworldenvironmentswithadeterministicactionspace. Theaimof
valuealignmentverificationistocreateaquestionnaireusingthehumanagent’sknowledge(rewardfunctionortrajectorypreferences)thatcanbegiventoanyagentinorder
to verify alignment. Efficient verification aims to minimize the number of queries in
the questionnaire. While few works on value alignment discuss qualitative evaluation
oftrust[2]orasymptoticalignmentofanagent’sperformanceviainteractionsandactivelearning[3][4][5],[1]solelyfocusesonverifyingvaluealignmentfortwoormore
agentswithalearnedpolicy. Theobjectiveistoefficientlytestcompatibilityofdifferent
robotswithhumanagents. Inthefollowingsections,wereiteratetheformaldefinition
ofvaluealignmentasstatedbytheoriginalauthors(ValueAlignmentVerificationinSection3andExactValueAlignmentVerificationinSection4),followedbyourexperiment
settingsinSection7andsubsequentobservationsinSection8.
## 2 Notation
Weusethenotationproposedin[6],whereaMarkovDecisionProcess(MDP)M isdefinedbyanenvironmentEandarewardfunctionR. AnenvironmentE=(S,A,P,S ,γ)

|                                         |     |     |     |     |                         |     |     |     | :S×A×S | →   |

| whereSisasetofstates,Aisasetofactions,P |     |     |     |     | isatransitionfunction,P |     |     |     |        |     |
[0,1], γ ∈ [0,1)isdiscountfactorandadistributionoverinitialstatesS . Thereward

|     |     | → R. |     | ×A  | →   |     |     |     |     |     |

functionR : S Apolicyπ : S [0,1]fromstatestoadi∑stributionoverac‐
∞
t i o n s. T h e s t a te a nd sta ∑te‐ acti o n v al u e so fa p o lic yπ a r e V π (s )= E [ γ tR (s )| s =
|     |     |     |     |     |     | R   |     | π t= | 0   | t 0 |

s ] Q π ( s , a ) = E [ ∞ γ t R (s ) | s = s , a = a ] s ∈ S a ∈ A
| a n d | R   | π   | t=0   | t   | 0 0 | f o r   | a   | n d | .   | T h e o p‐ |

|       |     |     | V∗(s) |     |     | Q∗(s,a) |     |     |     |            |
timal value functions are, = max Vπ(s) and = max Qπ(s,a). Let
|     |     |     | R   |     | π R | R   |     | π   | R   |     |

A (s) = argmax Q∗ (s,a′) denote the set of optimal actions at a state s under the
| R   |     | a′∈A | R   |     |     |     |     |     |     |     |

(s)={a∈A|π∗(a|s)>0}.
| rewardfunctionR. |     | ThenA | R   |     |     | Itisassumedthatrewardfunc‐ |     |     |     |     |

R
tion is linear under state features ([7], [8], [9]) ϕ : S → Rk, such that R(s) = wTϕ(s),
|     | ∈ Rk. |     |     |     |     |     |     | ϕ,  |     |     |

where w Note that there is no restriction on the features therefore these
features could be complex non‐linear functions of the state as well. The state‐action
|             | oncanbewrittenintermsoffeatures([10])asQπ |     |     |     |     |     |       | wTΦ( | s,a) |       |

| valuefuncti | ∑                                         |     |     |     |     |     | (s,a) | =    | π    | where |
R
| Φ( s,a) =E                                 | [ ∞   | γtϕ(s | )|s =s,a | =a]. |     |     |     |     |     |     |

| π                                          | π t=0 |       | t 0      | 0    |     |     |     |     |     |     |
| ReScienceC8.2(#31)–PanigrahiandPatnaik2022 |       |       |          |      |     |     |     |     |     | 3   |


| 3 Value Alignment | Verification |     |     |     |     |

Considertwoagents(forinstance,ahumanandarobot)wherethefirstagent’s(human)
reward function provides the ground truth for the value alignment verification of the
| secondagent(robot). | Thedefinitionisasfollows: |     |     |     |     |

GivenrewardfunctionR,apolicyπ′
| Definition1 |     |     | isϵ-valuealignedinenvironmentEifand |     |     |

onlyif
′
|     |     | V ∗ (s)−Vπ | (s)≤ϵ,∀s∈S |     | (1) |

|     |     | R          | R          |     |     |
The aim of the study [1] is efficient value alignment verification which, formally, is a
solutionforthefollowing:
′
|     |     |     | min|T|, s.t. ∀π | ∈Π,∀s∈S |     |

T⊆T
|     | ∗        | ′          | ′              |     |     |

|     | V (s)−Vπ | (s)>ϵ⇒Pr[π | passestestT]≤δ |     | (2) |
|     | R        | R          |                | fpr |     |
|     | ∗        | ′          | ′              |     |     |
|     | V (s)−Vπ | (s)≤ϵ⇒Pr[π | failstestT]≤δ  |     |     |
|     | R        | R          |                | fnr |     |
| T   |          |            | Π              |     |     |
where is the set of all possible queries, is set of all policies for which the test is
∈ [0,1]arethefalsenegativeandfalsepositiverates,and|T|isthe
| designed,δ | ,δ  |     |     |     |     |

fnr fpr
size of test T. When ϵ = δ = 0, the authors call this setting exact value alignment
fpr
verification.
| 4 Exact Value | Alignment | Verification |     |     |     |

Exact value alignment verification is not possible, even for finite MDPs, when we can
onlyquerytherobotagentforitsactionpreferences. Therefore,itispossibleonlyinthe
mostidealizedsetting,i.e.,explicithuman,explicitrobot.
Defineanagentπ′
| Definition2 |        | toberational([11])if: |     |       |     |

|             |        | ′                     |     | ∗     |     |
|             | ∀a∈A,π | (a|s)>0⇒a∈argmaxQ     |     | (s,a) | (3) |
R′
a
Q∗ (s,a)istheoptimalstate-actionvaluefunctionfortherewardfunctionR′
| whereargmax | R′  |     |     |     | .   |

a
Asthereexistinfinitelymanyrewardfunctionswhichcanreturnthesameoptimalpolicy([12]),determiningthat∃s ∈ S,R(s) ̸= R′(s)doesnotnecessarilyimplythatagents
withtherewardfunctionsR,R′
|     |     | arenotaligned. | WeprovideanexampleofthisinFig‐ |     |     |

ure1,wheretheoptimalpolicyforhumanandrobotisthesame;thus,theyarealigned.
However,therewardsaredifferent,asmentionedinTable1.
Figure1.Counterexamplewithsameoptimalpolicyforhumanandrobot
Definition3 DefinethesetofalltheoptimalpoliciesundertherewardfunctionRasOPT(R).
|     | OPT(R)={π|π(a|s)>0⇒a∈argmaxQ |     |     | ∗ (s,a)} |     |

R
a
| ReScienceC8.2(#31)–PanigrahiandPatnaik2022 |     |     |     |     | 4   |

Table1.Humanandrobotrewardsforgridworld(Figure1)
|     | StateColor | TerminalState | HumanReward | RobotReward |

|     | Blue       | No            | ‐0.6157     | ‐0.5316     |
|     | White      | No            | ‐0.3107     | ‐0.0694     |
|     | Green      | Yes           | +0.7242     | +0.8441     |
Looking at Definition 1 and Equation 3 simultaneously makes it evident that for a rational robot, if all of its optimal policies are also optimal under ground truth reward
functionR;therobotisexactlyalignedwiththehuman.
WehaveexactvaluealignmentinenvironmentE
| Corollary1      |                                     |     |     | betweenarationalrobotwith |

|                 | ′                                   |     |     | ′ )⊆OPT(R).               |
| rewardfunctionR | andahumanwithrewardfunctionRifOPT(R |     |     |                           |
Revisitingtheinspiration([12])oftheoriginalauthor’sproposedapproachforefficient
exactvaluealignmentGivenanenvironmentE,theconsistentrewardset(CRS)ofapolicyπinenviron-
Definition4
mentEisdefinedasthesetofrewardfunctionsunderwhichπisoptimal
|     |     | CRS(π)={R|π | ∈OPT(R)} |     |

(4)
WhenR(s)=wTϕ,theCRSisoftheform([12],[13]):
Corollary2 Given an environment E, the CRS(π) is given by the following intersection of
half-spaces:
|     | {w∈Rk|wT(Φ(s,a)−Φ(s,b))≥0,∀a∈argmaxQπ(s,a |     |     | ′ ),b∈A,s∈S} |

|     |                                           | π π | R   |              |
a′∈A
Since the boundaries of the CRS polytope is consistent with a policy that may not be
aligned with optimal policy (e.g. zero reward), we remove all such boundary cases to
obtainamodifiedsetcalledalignedrewardpolytope(ARP).
| 5 Reproducing | Exact | Value Alignment |     |     |

Inthissection, weexplaintheprocedureinordertoverifytheclaimsmadeinthepaper regarding sufficient conditions for provable verification of exact value alignment
(explainedinSection4). Weverifyexactvaluealignmentindisparatesettingsproposed
bytheauthorsforexplicithuman-explicitrobotsetting. Ifwehaveaccesstothevalueor
rewardfunctionofahuman,wetermitasexplicithuman. Asimilarnotionisapplicable
fortherobotaswell.
Theorem1 Undertheassumptionofarationalrobot(definedinSection4)thatshareslinear
rewardfeatureswiththehuman,efficientexactvaluealignmentverificationispossibleinthe
′
followingquerysettings: (1)Queryaccesstorewardfunctionweightsw , (2)Queryaccessto
′
samplesoftherewardfunctionR (s),(3)QueryaccesstoV∗ (s)andQ∗ (s,a),and(4)Query
R′ R′
accesstopreferencesovertrajectories.
| Case1 | RewardWeightQueries |     |     |     |

Abrute‐forceparadigmcanbeimplementedtoevaluateanexplicitrobotoptimalpolicy
underthehumanrewardfunction. However,thereexistsanothersuccinctverification
|     |     |     | ′   | ′ ′ |

test. Weneedtoquerytheweightvectorw oftherobot(here,R (s)=(w )Tϕ(s),ϕ(s)is
thefeaturevectorofstates). Thepaperassertsthatitispossibletoformatest(defined
′
later as ∆) that uses the obtained w to verify alignment. Additionally, this query to
′
the weight vector w is done in constant time, and the test is linear in the number of
questions.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 5


Definition5 GivenanMDPMcomposedofenvironmentEandrewardfunctionR,thealigned
rewardset(ARS)isdefinedasthefollowingsetofrewardfunctions:
ARS(R)={R ′|OPT(R ′ )⊆OPT(R)}
Westatethelemmawhichprovesthesufficientconditionforexactvaluealignmentand
directtheinterestedreadersfortheproofofthelemmatoreferthepaper.
′
Lemma1 Given an MDP M = (E, R), the human’s and robot’s reward function R and R
respectively can be represented as linear combinations of features ϕ(s) ∈ Rk, i.e., R(s) =
wTϕ(s),R ′ (s)=(w ′ )Tϕ(s),andgivenanoptimalpolicyπ∗ underR,wehave
R
w ′ ∈∩ (s,a,b)∈O H s R ,a,b ⇒R ′ ∈ARS(R)
where
HR ={w|wT(Φ(s,a))−Φ(s,b))>0}andO ={(s,a,b)|s∈S,a∈A (s),b̸=A (s)}
s,a,b π π R R
( )
Definition6 Theintersectionofhalf-spaces ∩ (s,a,b)∈O H s R ,a,b isdefinedastheAlignedRe-
wardPolytope(ARP).ThedesignofARPintheformof∆matrixisdefinedasfollows:
[ ]
Φ(s,a))−Φ(s,b)
π π
∆= .
.
.
Intheaboveequation,aisanoptimalactionatstates,andbisanon‐optimalaction.The
actionsinthetrajectoryfollowingaandbareoptimal. Eachrowof∆representsthenormalvectorforastricthalf‐spaceconstraintbasedonfeaturecountdifferencesbetween
′ ′
anoptimalandsub‐optimalaction. Therefore,forarobotweightvectorw ,if∆w >0,
therobotisaligned. Wefollowthestepsmentionedintheoriginalpapertoincludeonly
non‐redundanthalf‐spacenormalvectorsin ∆. Weenumerateallpossiblehalf‐space
normalvectorscorrespondingtoeachstates,optimalactiona,andnon‐optimalaction
b. Weaccumulateonlynon‐redundanthalf‐spacenormalvectors:
1. RemovalofDuplicateVectors: Toremoveduplicatevectors,wecomputethecosine
distancebetweenthehalf‐spacenormalvectors. Onevectorineachofthepairs
ofvectorswithcosinedistancewithinasmallprecisionvalue(weselect0.0001)is
retainedin∆,othersbeingdiscarded. Allzerovectorsarealsoremoved.
2. RemovalofRedundantVectors:Accordingtothepaper,thesetofredundantvectors
can be found efficiently using the Linear Programming approach. To check if a
constraintaTx≤bisnecessary,wefirstremovethatconstraintandsolvethelinear
programmingproblem. Iftheoptimalsolutionisstillconstrainedtobelessthan
or equal to b, that constraint can be safely discarded. After removing all such
redundantvectors,wegetonlyasetofnon‐redundanthalf‐spacenormalvectors.
Case2 RewardQueries
In this case, the tester seeks for the rewards of the robot. Here, a tester is same as a
user (human) who wishes to verify the alignment of a robot. Since it is assumed that
bothhumanandrobothaveaccesstotheirstatefeaturevectors,andfromtheequation
R(s)=wTϕ(s),weobtaintheweightvectorfortherobot,andthiscasereducestoCase1.
LetΦ bedefinedasthematrixwhereeachrowcorrespondstothefeaturevectorϕ(s)T
M
foradistinctstates ∈ S. Inordertosolvethesystemoflinearequationforobtaining
theweightvector,thenumberofqueriesneededisrank(Φ ).
M
Case3 ValueFunctionQueries
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 6


Thetesterseekstheactionvaluefunctionandthevaluefunctionforeachstateinthis
casesetting. Subsequently,therewardweightsfortherobotareobtainedwiththeaid
ofthefollowingequations:
R ′ (s)=(w ′ )TxandR ′ (s)=Q ∗
R′
(s,a)−γE s′[V
R
∗
′
(s ′ )]
This case also boils down to Case 1 as we obtain the weight vector for the robot. Accordingtothepaper,ifwedefinethemaximumdegreeoftheMDPtransitionfunction
as
d = max |{s ′ ∈S|P(s,a,s ′ )>0}|,
max
s∈S,a∈A
then at most d possible next state queries are needed to evaluate the expectation.
max
Therefore,atmostrank(Φ )(d +1)queriesarerequiredtorecovertherobot’sweight
M max
vector.
Case4 PreferenceQueries
We obtain preference over trajectories ξ as judged by the human. Ea∑ch preference
ξ >ξ ,inducesaconstraint(w ′ )T(Φ(ξ )−Φ(ξ ))>0,whereΦ(ξ)= n γiϕ(s )is
A B A B i=1 i
thecumulativediscountedrewardfeatures(linearcombinationofstatefeatures)along
a trajectory. Therefore, we construct ∆ where each row corresponds to a half‐space
normalresultingfrompreferenceoverindividualtrajectories. Inthiscase, onlyalogarithmicnumberoftrajectoriesareneededfromallpossibletrajectoryspacetoobtain
∆matrixandproceedtoverifyalignmentofrobot. Weobtainallvalidtrajectories,performpreprocessing(removeduplicate&redundantvectors),andobservethatthetotal
number of queries is bounded by logarithmic number of trajectories we started with
([14]).
## 6 Value Alignment Verification Heuristics
Whentherobotactsasablackboxandcanprovidestateactionpreferencesinsteadof
apolicy,theauthorsproposethreeheuristics;CriticalStates,MachineTeachingandARP
Heuristic. Eachheuristicconsistsofamethodforselectingthestatesatwhichtherobot
istestedandqueriesforanaction,subsequentlycheckingiftheactionisoptimalunder
human’srewardfunction. Itisimportanttonotethatfortheseheuristics,δ > 0,as
fpr
thereisnoguaranteefortherobottoalwaystakethesameactionatagivenstate.
1. CriticalStatesHeuristic: Inspiredbythenotionofcritic∑alstates(CS)[2],theheuristictestconsistsofstatesforwhichQ∗(s,π∗(s))− 1 Q∗(s,a) > t, where
R R |A| a∈A R
tisathresholdvalue. Thisintuitivelystatestheimportanceofaparticularstate
andtendstomaketheverificationefficient.
2. MachineTeachingHeuristic: ThisheuristicisbasedonSetCoverOptimalTeaching (SCOT) [13], which approximates the minimal set of state‐action trajectories
necessary to teach a specific reward function to an IRL agent. [13] show that in
theintersectionofhalf‐spacesthatdefinetheCRS(Corollary2),thelearnerrecovers a reward function. The authors use SCOT to create informative trajectories
andcreatealignmenttestsbyseekingarobotactionateachstatealongthetrajectory. Producing a test with SCOT takes longer than CS heuristic, but unlike CS,
SCOTpreventsrepetitiveinquiriesbyreasoningaboutrewardfeaturesoveraset
oftrajectories.
3. ARPHeuristic: This heuristic is a black‐box alignment heuristic (ARP‐bb) based
ontheARPdefinition. ARP‐bbfirstcomputes∆,thenuseslinearprogrammingto
removeduplicatehalf‐spaceconstraints,subsequentlyasksforrobotactionsfrom
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 7


thestatescorrespondingtothenon‐redundantconstraints(rows)in∆. Intuitively,
thestatesprobedbyARP‐bbaresignificantbecausedifferentactionsdisclosevital
information about the reward function. ARP‐bb approximates testing each halfspaceconstraintbyusingsingle‐stateactionqueries. Asaresult,ARP‐bbtradesoff
increasedapproximationerrorinexchangeforalowerqueryandcomputational
complexity.
## 7 Experiments
Inthissection,wedescribeseveralexperimentscarriedoutinordertoinvestigatethe
following:
1. AlgorithmsandHeuristics: Comparisonofdifferentalgorithmsandheuristicsin
differentgridworlds. Wetabulatetheperformanceoftesters(accuracy,falsepositiverate,falsenegativerate,andthenumberofqueriespresentedtotherobotfor
verification)w.r.tdifferentgridworldwidthsrangingfrom4to8andfeaturesize
from3to8. Thedimensionoffeatureforastateistermedasnumberoffeaturesor
featuresize. Ourexperimentsconfinethesestatefeaturesϕtobeone‐hotvectors
only.
2. Diagonal Actions: Comparison of algorithms and heuristics in gridworlds with
anextendedactionspace. Weallowdiagonalmovementbetweenstandardmovements. This increases the standard 4 actions (left, up, right, and down) to 8 actions(left‐up‐diag,up‐right‐diag,right‐down‐diag,anddown‐left‐diag). Here,diag
referstodiagonalmovement. Again,wetabulatetheperformanceoftestersw.r.t
differentgridworldwidths.
3. Non‐linearrewardandstate‐featurerelationships: Comparisonofdifferentalgorithmsandheuristicswithnon‐linear(cubicandexponential)rewardRandstatefeature ϕ(s) relationships. In cubic, we approximate the linear behavior when
wTϕ(s) ≈ 0,elsenot. TheexactrelationshipweconsiderisR = x3 +10xwhere
x=wTϕ(s). Inexponential,wecompletelyremovethelinearrelationshipbetween
Randϕ(s)andconsiderR=ewTϕ(s).
Wetabulatetheperformanceoftestersw.r.t
differentgridworldwidthsinbothcases.
4. CriticalStatesTesterfordifferentthresholds: ComparisonofCriticalStatesTester
performancewithdifferentthresholdvalues(0.0001,0.2and,0.8)forastatetobe
critical.
Section8providestheresultsforonealgorithm(RewardWeightTester)andoneheuristic(CriticalStateTester)andplotsrelevanttotheiraccuracyandnumberoftestqueries.
We redirect readers to Section 2 of Supplementary Material for the detailed tabulated
performance of all algorithms, heuristics, and the plots related to false positive and
falsenegativerates. Also,notethatthedefaultgridworldrowsare4,gridworldwidthis
8,numberofactionsis4,featuresizeis5,rewardandstate‐featurerelationshipislinear
(R=wTϕ(s)),andthresholdvalueofCriticalStatesTesteris0.2.
Wecreated100differenthumanagentsforeachexperiment,andforeachhumanagent,
we created 100 different robots to check their alignment. Each human agent correspondstoadifferenthumanweightvectorwhoseeachelementissampledfromanormaldistributionwithmean0andvariance1. Differentrobotagentscorrespondtodifferentrobotweightsthatareobtainedbyaddingarandomnormalnoisevectortothe
correspondinghumanweightvector.Theelementsofthenoisevectoraresampledfrom
thesamenormaldistribution. Further,wenormalizetherobotandhumanweightvectortohaveaunitnorm. Intotal,werun1.32millionexperimentstoaddressthepoints
mentionedabove.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 8


|     | (a)Accuracy |     | (b)NumberofTestQueries |     |

Figure2.Testerperformancefordifferentgridworldwidths(numfeatures=5)
## 8 Results
Intheplotsandfollowingdiscussion,rwtindicatesRewardWeightQueriesTester,rt
indicatesRewardQueriesTester,vftindicatesValueFunctionQueriesTester,pttindicatesPreferenceTrajectoryQueriesTester,cstindicatesCriticalStatesTester,scott
indicatesSCOTTester,andarpbbtindicatesARPBlackBoxTester.
### 8.1 AlgorithmsandHeuristics
Thecomparisonbetweentheperformanceofdifferentalgorithmsandheuristicsispresented in Table 2, and Figure 2 (for different gridworld widths), Table 3 and Figure 3
(fordifferentfeaturesizes). Theplotsobtainedaresimilartotheplotspresentedin[1].
Weaveragedtheaccuracyover10000experiments(100differenthumanagentsand100
differentrobotscorrespondingtoeachhumanagent)androundupto3decimalplaces.
We notice that scott takes the maximum time to verify 100 different robots whereas
rwttakestheminimumtime. ThedetailsarepresentinSection2oftheSupplementary
Material. Weobservethat,ingeneral,thealgorithmsforexactvaluealignmentverificationhaveslightlyhigheraccuracy. Wealsoobservethattheaccuraciesandnumberof
testqueriesincreasewithincreasingfeaturesizes. Notethat,in[1],theaccuracyinvariousplotsisconsideredas(1‐falsepositiverate),whilewehavedifferentplotsforboth.
Weattributethecomparativelylowaccuracywithptttocomparativelybadtrajectory
queries.
Table2.Differenttestersversusgridworldwidths
| Tester | Width Accuracy | False        | False        | Numberof |

|        |                | positiverate | negativerate | queries  |
|        | 4 0.995±0.013  | 0.005±0.011  | 0.001±0.005  | 1        |
|        | 0.997±0.007    | 0.002±0.005  | 0.001±0.005  |          |
| rwt    | 6              |              |              | 1        |
|        | 8 0.999±0.004  | 0.001±0.004  | 0.000±0.002  | 1        |
|        | 0.973±0.043    | 0.000±0.000  | 0.027±0.043  |          |
|        | 4              |              |              | 13       |
| cst    | 6 0.987±0.018  | 0.000±0.000  | 0.013±0.018  | 24       |
|        | 8 0.996±0.007  | 0.000±0.001  | 0.004±0.007  | 29       |
As per Definition 1, we require δ = ϵ = 0 for Exact Value Alignment Verification;
fpr
hencefalsenegativescanbepresentinthecorrespondingalgorithms. Further,wediscussed with the authors the possibility of false positives in these algorithms, and we
concludedthatsincewedonotconsiderallpossibletrajectoriesinagridworld(which
is exponential in the number of actions), false positives can be present. However, we
observethatbothfalsepositiveandfalsenegativeratesarenegligiblysmall. ThesereReScienceC8.2(#31)–PanigrahiandPatnaik2022 9


sultsempiricallyshowthatindeedtheproposedalgorithmsandheuristicssuccessfully
identifythealignmentbetweenhumanagentsandrobots.
|     | (a)Accuracy |     | (b)NumberofTestQueries |     |     |

Figure3.Testerperformancefordifferentnumberoffeatures
InFigure2b,thenumberofqueriesindicatesthesizeofthequestionnaire,i.e.,|T|.
The
totalnumberofqueriesrequiredtoverifythevaluealignmentwithcstishigherthan
otherheuristicsowingtoitssimplermechanismforobtainingstatequeries. Weobserve
thatarpbbtisalsoboundedbythelogarithmofthetotalnumberofqueries,i.e.,trajectoriesofacertainmaximumlength(thisvalueissetat10),possibleinagridworld. The
numberofstatestobequeriedinscottisfixedatthemaximumlengthofatrajectory
possible(thisvalueissetat5forscott). Also,withtheincreaseinthesizeofthegridworld,thenumberofquerieswithcstincreases. Further,wehavenotpresentedthe
numberofqueriesforrtandvftinplotsbecausetheyhavewell‐definedmathematical
formulaetocalculate|T|.
Table3.Differenttestersversusfeaturessizes
| Tester | Feature     | Accuracy    | False                  | False        | Numberof |

|        | size        |             | positiverate           | negativerate | queries  |
|        | 3           | 0.951±0.051 | 0.037±0.045            | 0.012±0.034  | 1        |
|        |             | 0.999±0.004 | 0.001±0.004            | 0.000±0.002  |          |
| rwt    | 5           |             |                        |              | 1        |
|        | 7           | 1.000±0.001 | 0.000±0.000            | 0.000±0.001  | 1        |
|        |             | 0.876±0.097 | 0.000±0.002            | 0.124±0.097  |          |
|        | 3           |             |                        |              | 31       |
| cst    | 5           | 0.996±0.007 | 0.000±0.001            | 0.004±0.007  | 29       |
|        |             | 0.999±0.002 | 0.000±0.000            | 0.001±0.002  |          |
|        | 7           |             |                        |              | 28       |
|        | (a)Accuracy |             | (b)NumberofTestQueries |              |          |
Figure4.Testerperformancefordifferentgridworldwidthswithextendedactionspace
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 10


Table4.Differenttestersversusgridworldwidthswithextendedactionspace
| Tester | Width | Accuracy    |              | False |              | False | Numberof |     |

|        |       |             | positiverate |       | negativerate |       | queries  |     |
|        | 4     | 0.992±0.017 | 0.006±0.015  |       | 0.003±0.010  |       |          | 1   |
| rwt    | 6     | 0.994±0.013 | 0.005±0.011  |       | 0.001±0.004  |       |          | 1   |
|        |       | 0.996±0.008 | 0.002±0.005  |       | 0.002±0.005  |       |          |     |
|        | 8     |             |              |       |              |       |          | 1   |
|        | 4     | 0.945±0.055 | 0.000±0.001  |       | 0.055±0.055  |       |          | 9   |
|        |       | 0.984±0.017 | 0.000±0.001  |       | 0.016±0.017  |       |          |     |
| cst    | 6     |             |              |       |              |       |          | 12  |
|        | 8     | 0.992±0.011 | 0.000±0.000  |       | 0.008±0.011  |       |          | 21  |
### 8.2 DiagonalActions
TheperformancesummaryforrwtandheuristicsarepresentedinTable4andFigure4.
Weobservesimilartrendstogridworldwithsmalleractionspace‐theaccuracyishigh,
andthefalsepositiveandfalsenegativeratesareextremelysmall,thenumberofqueries
withcstishigherthanotherheuristics,andthenumberofqueriesforscottisfixed
atthemaximumpossiblelengthofatrajectory. Theseresultsempiricallyindicatethat
theproposedtestersaresuccessfullyabletoverifythealignmentofrobotsandhumans
ingridworldswithanextendedactionspace.
8.3 Non-linearrewardandstate-featurerelationships
TheperformancesummaryforrwtandcstispresentedinTable5andFigure5. We
observethatforcubicrelationship,theperformanceforbothrwtandcstisclosetothat
with linear relationship. Note that cubic approximates the linear relationship between
R and wTϕ(s), when wTϕ(s) ≈ 0. However, as expected for exponential relationship
(assumptionofLemma1isnolongertrue),theperformanceforrwtisexceedinglypoor
whileforcst thedeclineisnegligible. Thisempiricallyenforcestheimportanceand
independenceoflinearrelationshipassumptionbetweenrewardsandstatefeaturesfor
exactvaluealignmentalgorithms(rwt)andheuristics(cst),respectively.
Table5. Different testers versus gridworld widths with non‐linear reward state‐feature relationships
| Tester                                     | Width | Accuracy      |     | False        |     | False        |     | Numberof |

|                                            |       |               |     | positiverate |     | negativerate |     | queries  |
|                                            |       | 0.993±0.013   |     | 0.004±0.007  |     | 0.003±0.011  |     |          |
|                                            |       | 4             |     |              |     |              |     | 1        |
|                                            |       | 0.995±0.008   |     | 0.003±0.006  |     | 0.002±0.005  |     |          |
| rwt                                        |       | 6             |     |              |     |              |     | 1        |
| (cubic)                                    |       | 8 0.997±0.006 |     | 0.001±0.005  |     | 0.001±0.004  |     | 1        |
|                                            |       | 0.048±0.052   |     | 0.953±0.052  |     | 0.000±0.000  |     |          |
|                                            |       | 4             |     |              |     |              |     | 1        |
| rwt                                        |       | 6 0.017±0.021 |     | 0.983±0.021  |     | 0.000±0.000  |     | 1        |
|                                            |       | 0.006±0.012   |     | 0.994±0.012  |     | 0.000±0.000  |     |          |
| (exponential)                              |       | 8             |     |              |     |              |     | 1        |
|                                            |       | 4 0.968±0.040 |     | 0.000±0.000  |     | 0.032±0.040  |     | 16       |
| cst                                        |       | 6 0.991±0.015 |     | 0.000±0.000  |     | 0.010±0.015  |     | 24       |
|                                            |       | 0.995±0.010   |     | 0.000±0.000  |     | 0.005±0.010  |     |          |
| (cubic)                                    |       | 8             |     |              |     |              |     | 32       |
|                                            |       | 4 0.947±0.051 |     | 0.000±0.001  |     | 0.053±0.051  |     | 16       |
|                                            |       | 0.984±0.022   |     | 0.000±0.001  |     | 0.016±0.022  |     |          |
| cst                                        |       | 6             |     |              |     |              |     | 16       |
| (exponential)                              |       | 8 0.983±0.099 |     | 0.010±0.099  |     | 0.007±0.010  |     | 31       |
| ReScienceC8.2(#31)–PanigrahiandPatnaik2022 |       |               |     |              |     |              |     | 11       |


|     | (a)Accuracy(Cubic) | (b)Accuracy(Exponential) |     |     |

Figure5.Testerperformancefordifferentreward‐statefeaturesrelationship
### 8.4 CriticalStatesTesterwithdifferentthresholds
Theperformanceofcstwithdifferentthresholds(0.0001and0.8,0.2iscstrowinTable
2)ispresentedinTable6. ThecorrespondingfiguresarepresentedinSection2ofthe
SupplementaryMaterial. Weobservethattheaccuracyforlowthresholdvaluesishigh
whereastheaccuracydropsconsiderablywithhigherthresholdvalue. Thisisduetoa
decreaseinthenumberoftestquerieswithhigherthresholdsleadingtoadecreasein
alignmentverificationability. Thecomparisonbetweenthenumberoftestqueriesfor
differentthresholdsdisplaysanexpectedtrend,i.e.,thenumberofstatestobequeried
withlowerthresholdsishigherthanthosewithahigherthreshold.
Table6.Criticalstatestesterwithdifferentthresholds
| Tester     | Width Accuracy | False        | False        | Numberof |

|            |                | positiverate | negativerate | queries  |
| cst        | 4 0.971±0.036  | 0.000±0.000  | 0.029±0.036  | 16       |
|            | 0.987±0.018    | 0.000±0.000  | 0.013±0.018  |          |
| (threshold | 6              |              |              | 24       |
|            | 0.997±0.007    | 0.000±0.000  | 0.003±0.007  |          |
| =0.0001)   | 8              |              |              | 32       |
| cst        | 4 0.616±0.447  | 0.362±0.463  | 0.022±0.032  | 1        |
|            | 0.563±0.482    | 0.431±0.488  | 0.007±0.013  |          |
| (threshold | 6              |              |              | 4        |
| =0.8)      | 8 0.644±0.468  | 0.354±0.470  | 0.003±0.008  | 3        |
## 9 Discussion
Inthiswork,weimplementedthealgorithmsandheuristicsforExactValueAlignment
Verification. Weobservethatallthemethodsproposedin[1]canidentifythealignment
betweenarobotandahumanagentwithhighconfidenceintwodistinctscenarios,im-
plicit and explicit robot with an explicit human agent. In this work, we have not investigatedimplicitrobot,implicithuman(approximatevaluealignmentverification)setting
duetolackoftime. Additionally,wehavecarriedoutablationstudiestostudytheperformance of these proposed methods in different settings, including an extended deterministicactionspaceandnon‐linearrewardstate‐featurerelationship. Ultimately,a
humanagentcoulduseanyofthealgorithmsorheuristic(dependingontheabilityof
therobottoaccessitsrewards)tocreateadriver’stesttotesttherobot’salignment.
References
1. D.S.Brown,J.Schneider,A.Dragan,andS.Niekum.“ValueAlignmentVerification.”In:InternationalConference
onMachineLearning.PMLR.2021,pp.1105–1115.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 12


2. S.H.Huang,K.Bhatia,P.Abbeel,andA.D.Dragan.“Establishingappropriatetrustviacriticalstates.”In:2018
IEEE/RSJInternationalConferenceonIntelligentRobotsandSystems(IROS).IEEE.2018,pp.3929–3936.
3. D.Hadfield-Menell,S.J.Russell,P.Abbeel,andA.Dragan.“Cooperativeinversereinforcementlearning.”In:
Advancesinneuralinformationprocessingsystems29(2016),pp.3909–3917.
4. P.Christiano,J.Leike,T.B.Brown,M.Martic,S.Legg,andD.Amodei.“Deepreinforcementlearningfromhuman
preferences.”In:arXivpreprintarXiv:1706.03741(2017).
5. D.Sadigh,A.D.Dragan,S.Sastry,andS.A.Seshia.“Activepreference-basedlearningofrewardfunctions.”In:
(2017).
6. K.Amin,N.Jiang,andS.Singh.“Repeatedinversereinforcementlearning.”In:arXivpreprintarXiv:1705.05427
(2017).
7. B.D.Ziebart,A.L.Maas,J.A.Bagnell,A.K.Dey,etal.“Maximumentropyinversereinforcementlearning.”In:
Aaai.Vol.8.Chicago,IL,USA.2008,pp.1433–1438.
8. A.Barreto,W.Dabney,R.Munos,J.J.Hunt,T.Schaul,H.VanHasselt,andD.Silver.“Successorfeaturesfor
transferinreinforcementlearning.”In:arXivpreprintarXiv:1606.05312(2016).
9. D.Brown,R.Coleman,R.Srinivasan,andS.Niekum.“Safeimitationlearningviafastbayesianrewardinference
frompreferences.”In:InternationalConferenceonMachineLearning.PMLR.2020,pp.1165–1177.
10. P.AbbeelandA.Y.Ng.“Apprenticeshiplearningviainversereinforcementlearning.”In:Proceedingsofthe
twenty-firstinternationalconferenceonMachinelearning.2004,p.1.
11. S.RussellandP.Norvig.“Artificialintelligence:amodernapproach.”In:(2002).
12. A.Y.Ng,S.J.Russell,etal.“Algorithmsforinversereinforcementlearning.”In:Icml.Vol.1.2000,p.2.
13. D.S.BrownandS.Niekum.“Machineteachingforinversereinforcementlearning:Algorithmsandapplica-
tions.”In:ProceedingsoftheAAAIConferenceonArtificialIntelligence.Vol.33.01.2019,pp.7749–7758.
14. D.S.Brown,W.Goo,andS.Niekum.“Better-than-DemonstratorImitationLearningviaAutomatically-Ranked
Demonstrations.”In:Proceedingsofthe3rdConferenceonRobotLearning.2019.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 13


## 10 Sample Gridworld
Wepresentasamplegridworld(Figure6a),asamplehumanagent’soptimalpolicy(Figure 6b), a sample robot’s optimal policy (Figure 6c). In the gridworld, there are three
differentkindsofstate(blue,yellow,andwhite,withstateingreencolordenotingthe
terminalstate). Theboldarrowsshowthemovementsaspertheoptimalpolicy. Clearly,
therobotisnotalignedwiththehumanagent. Further,wealsodepictthestatequeries
(statesmarkedwith⋆)askedbydifferenttestersaspertheabovehumanagent. Query
statesasperCriticalStatesTesterinFigure7a,SetCoverOptimalTeachingTester(SCOT
Tester)inFigure7bandARPBlackBoxTesterinFigure7c. Additionally,withtheaidof
arrows,wedepictthecorresponding(maximallyinformative)trajectorywiththestate
queriesforSCOTTester.
(a)Samplegridworld (b)Humanpolicy (c)Robotpolicy
Figure6.SampleGridworldandPolicies
(b) Set Cover Optimal Teaching
(a)CriticalStatesTester (c)ARPBlackBoxTester
Tester
Figure7.Querystatesfordifferentheuristictestersonasamplegridworld
## 11 Additional Results
In the plots, tables, and following discussion, rwt indicates Reward Weight Queries
Tester,rtindicatesRewardQueriesTester,vftindicatesValueFunctionQueriesTester,
pttindicatesPreferenceTrajectoryQueriesTester,cstindicatesCriticalStatesTester,
scott indicates SCOT Tester, and arpbbt indicates ARP Black Box Tester. Also note
that,byperformancemetricswereferaccuracy,falsepositiverate,falsenegativerate,
andnumberoftestqueries. rwt,rt,rwt,andrtaretogetherreferredtoasalgorithms.
cst,scott,andarpbbtaretogetherreferredtoasheuristics.
### 11.1 AlgorithmsandHeuristics
Table7detailstheperformancemetricsforallalgorithmsandheuristics. Wefixedthe
featuresizeat5. Thefeaturesize(orthenumberoffeatures)isequaltothedimension
ofstate‐featureϕ. Therefore,ifϕ:S →Rk ⇒featuresize=k.
Weobservedthatthevaryingwidthofagridworlddidnotaffectsignificantlytheaccuracy(Figure8a),falsepositive(Figure8b),andfalsenegativerates(Figure8c),whilethe
numberoftestqueries(Figure8d)increasedforheuristicsexceptforscott,because
the number of test queries for scott is equal to the maximum length of a trajectory
(here,itisequalto5). Theaccuracyforallthetestersisextremelyhigh,whilethefalse
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 14


positivesandfalsenegativesareexceedinglylow, whichindicatestheabilityofthealgorithmsandheuristicstoidentifyalignment(ormisalignment)betweenarobotanda
humanagent.
Intable8,wevarythefeaturesizefrom3to8. Wefixedthegridworldwidthat8. We
observednosignificantvariationinaccuracy(Figure9a),falsepositive(Figure9b),and
false negative rates (Figure 9c). The trend for the number of test queries (Figure 9d)
increases for rt, vft, and arpbbt while stays the same for rwt and scott. Unlike
withdifferentgridworldwidths,thenumberoftestqueriesstayssimilarwithdifferent
featuresizesforcst.
(a)Accuracy (b)FalsePositiveRate
(c)FalseNegativeRate (d)NumberofTestQueries
Figure8.Testerperformancefordifferentgridworldwidths
### 11.2 DiagonalActions
Table9detailstheperformancemetricsforrwtandallheuristicsinagridworldwith
diagonalmovementsallowed. Again,sincewevariedthewidthofagridworld,wefixed
thefeaturesizeat5. Wedidnotperformadditionalexperimentswithrt,vft,andptt,
sincetheyarereducibletorwt.Weconcludedthereisnoobservabledifferencefromthe
resultsingridworldswithoutthediagonalmovements,i.e.,theaccuracy(Figure10a)is
extremelyhigh,andthefalsepositive(Figure10b),andfalsenegativerates(Figure10c)
aresignificantlylow. Additionally,thenumberoftestqueries(Figure10d)increasesfor
cstwithanincreaseinthewidthofagridworld.
11.3 Non-linearrewardandstate-featurerelationship
Table 10 details the performance metrics for rwt and cst in gridworlds of different
widthsandnon‐linearrelationshipbetweenrewardandstate‐feature. Thecorresponding plot can be found in Figure 11 for cubic and Figure 12 for exponential relationship.
Theseplotsandtablescontainallthegridworldwidthsrangingfrom4to8(naturally,
thefeaturesizeisfixedat5),whicharenotpresentintheResultssectionofthepaper.
Notethat,incubicweapproximatethelinearrelationshiponlywhenwTϕ(s) ≈ 0while
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 15


Table7.0
| Tester | Width Accuracy | False        | False        | Numberof |

|        |                | positiverate | negativerate | queries  |
|        | 4 0.995±0.013  | 0.005±0.011  | 0.001±0.005  | 1        |
|        | 5 0.997±0.008  | 0.002±0.006  | 0.006±0.004  | 1        |
|        | 0.997±0.007    | 0.002±0.005  | 0.001±0.005  |          |
| rwt    | 6              |              |              | 1        |
|        | 7 0.997±0.008  | 0.002±0.005  | 0.002±0.006  | 1        |
|        | 0.999±0.004    | 0.001±0.004  | 0.000±0.002  |          |
|        | 8              |              |              | 1        |
|        | 4 0.992±0.015  | 0.007±0.014  | 0.001±0.004  | 5        |
|        | 0.994±0.013    | 0.005±0.012  | 0.001±0.004  |          |
|        | 5              |              |              | 5        |
|        | 0.994±0.012    | 0.004±0.010  | 0.002±0.007  |          |
| rt     | 6              |              |              | 5        |
|        | 7 0.997±0.006  | 0.002±0.005  | 0.001±0.004  | 5        |
|        | 0.998±0.005    | 0.002±0.004  | 0.000±0.002  |          |
|        | 8              |              |              | 5        |
|        | 4 0.990±0.019  | 0.008±.017   | 0.002±0.007  | 25       |
|        | 0.996±0.008    | 0.003±.007   | 0.001±0.004  |          |
|        | 5              |              |              | 25       |
|        | 0.995±0.011    | 0.003±.007   | 0.003±0.009  |          |
| vft    | 6              |              |              | 25       |
|        | 7 0.995±0.021  | 0.004±.017   | 0.002±0.007  | 25       |
|        | 0.998±0.005    | 0.001±.005   | 0.001±0.002  |          |
|        | 8              |              |              | 25       |
|        | 4 0.956±0.041  | 0.013±0.028  | 0.031±0.034  | 4        |
|        | 0.969±0.035    | 0.010±0.026  | 0.021±0.027  |          |
|        | 5              |              |              | 5        |
|        | 0.970±0.039    | 0.018±0.039  | 0.011±0.019  |          |
| ptt    | 6              |              |              | 10       |
|        | 7 0.971±0.040  | 0.023±0.041  | 0.005±0.012  | 8        |
|        | 0.957±0.054    | 0.040±0.055  | 0.003±0.006  |          |
|        | 8              |              |              | 4        |
|        | 4 0.973±0.043  | 0.000±0.000  | 0.027±0.043  | 13       |
|        | 0.978±0.048    | 0.000±0.000  | 0.022±0.048  |          |
|        | 5              |              |              | 16       |
|        | 0.987±0.018    | 0.000±0.000  | 0.013±0.018  |          |
| cst    | 6              |              |              | 24       |
|        | 7 0.980±0.100  | 0.010±0.099  | 0.009±0.019  | 26       |
|        | 0.996±0.007    | 0.000±0.001  | 0.004±0.007  |          |
|        | 8              |              |              | 29       |
|        | 4 0.960±0.041  | 0.002±0.005  | 0.040±0.041  | 5        |
|        | 0.979±0.024    | 0.002±0.005  | 0.019±0.023  |          |
|        | 5              |              |              | 5        |
| scott  | 6 0.988±0.017  | 0.001±0.004  | 0.010±0.017  | 5        |
|        | 7 0.993±0.010  | 0.002±0.005  | 0.005±0.009  | 5        |
|        | 0.994±0.010    | 0.002±0.005  | 0.004±0.008  |          |
|        | 8              |              |              | 5        |
|        | 4 0.985±0.036  | 0.015±0.036  | 0.000±0.000  | 7        |
|        | 0.987±0.040    | 0.013±0.040  | 0.000±0.000  |          |
|        | 5              |              |              | 6        |
| arpbbt | 6 0.991±0.027  | 0.009±0.027  | 0.000±0.000  | 7        |
|        | 0.996±0.016    | 0.004±0.016  | 0.000±0.000  |          |
|        | 7              |              |              | 5        |
|        | 0.994±0.022    | 0.006±0.022  | 0.000±0.000  |          |
|        | 8              |              |              | 9        |
exponentialcompletelyignoresthelinearrelationship. Weobservedthatsincetheaccuracy is high for cubic and low for exponential relationships, the false positive rates are
lowandhighrespectively.
### 11.4 CriticalStatesTesterwithdifferentthresholds
Table11detailstheperformancemetricsforcstindifferentgridworldwidthsanddifferent threshold values (0.0001, 0.2, and 0.8). As noted earlier, we observed that the
number of queries decreases with strict threshold values such as 0.8, which results
inreducedverificationabilities. Thecorrespondingplotsforperformancemetricsare
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 16


(a)Accuracy (b)FalsePositiveRate
(c)FalseNegativeRate (d)NumberofTestQueries
Figure9.Testerperformancefordifferentnumberoffeatures
(a)Accuracy (b)FalsePositiveRate
(c)FalseNegativeRate (d)NumberofTestQueries
Figure10.Testerperformancefordifferentgridworldwidthswithanextendedactionspace
presentinFigure13.
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 17


Table8.Differenttestersversusfeaturessizes
| Tester | Feature Accuracy | False        | False        | Numberof |

|        | size             | positiverate | negativerate | queries  |
|        | 3 0.951±0.051    | 0.037±0.045  | 0.012±0.034  | 1        |
|        | 0.991±0.015      | 0.006±0.013  | 0.003±0.007  |          |
|        | 4                |              |              | 1        |
| rwt    | 5 0.999±0.004    | 0.001±0.004  | 0.000±0.002  | 1        |
|        | 0.999±0.006      | 0.000±0.002  | 0.001±0.005  |          |
|        | 6                |              |              | 1        |
|        | 1.000±0.001      | 0.000±0.000  | 0.000±0.001  |          |
|        | 7                |              |              | 1        |
|        | 8 1.000±0.002    | 0.000±0.001  | 0.000±0.001  | 1        |
|        | 0.945±0.065      | 0.040±0.056  | 0.015±0.04   |          |
|        | 3                |              |              | 3        |
|        | 4 0.989±0.017    | 0.008±0.013  | 0.003±0.010  | 4        |
|        | 0.998±0.005      | 0.002±0.004  | 0.000±0.002  |          |
| rt     | 5                |              |              | 5        |
|        | 6 0.998±0.007    | 0.001±0.003  | 0.001±0.006  | 6        |
|        | 7 1.000±0.002    | 0.000±0.001  | 0.000±0.002  | 7        |
|        | 1.000±0.004      | 0.000±0.004  | 0.000±0.000  |          |
|        | 8                |              |              | 8        |
|        | 3 0.940±0.069    | 0.050±0.068  | 0.010±0.030  | 15       |
|        | 0.989±0.018      | 0.006±0.012  | 0.004±0.014  |          |
|        | 4                |              |              | 20       |
| vft    | 5 0.998±0.005    | 0.001±0.005  | 0.001±0.002  | 25       |
|        | 0.999±0.004      | 0.000±0.002  | 0.001±0.004  |          |
|        | 6                |              |              | 30       |
|        | 1.000±0.002      | 0.000±0.002  | 0.000±0.001  |          |
|        | 7                |              |              | 35       |
|        | 8 1.000±0.001    | 0.000±0.001  | 0.000±0.001  | 40       |
|        | 0.809±0.094      | 0.091±0.109  | 0.101±0.080  |          |
|        | 3                |              |              | 3        |
|        | 4 0.923±0.075    | 0.055±0.073  | 0.022±0.040  | 3        |
|        | 0.957±0.054      | 0.040±0.055  | 0.003±0.006  |          |
| ptt    | 5                |              |              | 4        |
|        | 0.972±0.042      | 0.027±0.042  | 0.001±0.004  |          |
|        | 6                |              |              | 12       |
|        | 7 0.986±0.030    | 0.014±0.030  | 0.000±0.001  | 5        |
|        | 0.995±0.012      | 0.005±0.012  | 0.000±0.002  |          |
|        | 8                |              |              | 8        |
|        | 3 0.876±0.097    | 0.000±0.002  | 0.124±0.097  | 31       |
|        | 0.970±0.101      | 0.010±0.099  | 0.020±0.025  |          |
|        | 4                |              |              | 32       |
|        | 0.996±0.007      | 0.000±0.001  | 0.004±0.007  |          |
| cst    | 5                |              |              | 29       |
|        | 6 0.997±0.008    | 0.000±0.000  | 0.003±0.008  | 18       |
|        | 0.999±0.002      | 0.000±0.000  | 0.001±0.002  |          |
|        | 7                |              |              | 28       |
|        | 8 1.000±0.001    | 0.000±0.000  | 0.000±0.001  | 28       |
|        | 0.883±0.090      | 0.006±0.011  | 0.112±0.089  |          |
|        | 3                |              |              | 5        |
|        | 4 0.979±0.029    | 0.004±0.008  | 0.018±0.029  | 5        |
| scott  | 5 0.994±0.010    | 0.002±0.005  | 0.004±0.008  | 5        |
|        | 0.998±0.005      | 0.001±0.003  | 0.001±0.004  |          |
|        | 6                |              |              | 5        |
|        | 7 0.998±0.004    | 0.001±0.003  | 0.001±0.003  | 5        |
|        | 0.999±0.003      | 0.001±0.002  | 0.000±0.001  |          |
|        | 8                |              |              | 5        |
|        | 3 0.912±0.110    | 0.088±0.110  | 0.000±0.000  | 3        |
|        | 4 0.973±0.063    | 0.027±0.063  | 0.000±0.000  | 4        |
|        | 0.994±0.022      | 0.006±0.022  | 0.000±0.000  |          |
| arpbbt | 5                |              |              | 9        |
|        | 6 0.998±0.008    | 0.002±0.008  | 0.000±0.000  | 13       |
|        | 0.999±0.003      | 0.001±0.003  | 0.000±0.000  |          |
|        | 7                |              |              | 14       |
|        | 8 1.000±0.001    | 0.000±0.001  | 0.000±0.000  | 17       |
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 18


Table9.Differenttestersversusgridworldwidthswithextendedactionspace
| Tester | Width Accuracy       | False                  | False                | Numberof |

|        | &positiverate        | negativerate           | queries              |          |
|        | 4 0.992±0.017        | 0.006±0.015            | 0.003±0.010          | 1        |
|        | 0.994±0.013          | 0.004±0.009            | 0.002±0.007          |          |
|        | 5                    |                        |                      | 1        |
| rwt    | 6 0.994±0.013        | 0.005±0.011            | 0.001±0.004          | 1        |
|        | 0.997±0.008          | 0.002±0.006            | 0.001±0.003          |          |
|        | 7                    |                        |                      | 1        |
|        | 0.996±0.008          | 0.002±0.005            | 0.002±0.005          |          |
|        | 8                    |                        |                      | 1        |
|        | 0.945±0.055          | 0.000±0.001            | 0.055±0.055          |          |
|        | 4                    |                        |                      | 9        |
|        | 0.975±0.039          | 0.000±0.000            | 0.026±0.039          |          |
|        | 5                    |                        |                      | 14       |
| cst    | 6 0.984±0.017        | 0.000±0.001            | 0.016±0.017          | 12       |
|        | 0.987±0.022          | 0.000±0.000            | 0.013±0.022          |          |
|        | 7                    |                        |                      | 21       |
|        | 8 0.992±0.011        | 0.000±0.000            | 0.008±0.011          | 21       |
|        | 0.945±0.049          | 0.002±0.005            | 0.054±0.049          |          |
|        | 4                    |                        |                      | 5        |
|        | 0.969±0.036          | 0.003±0.009            | 0.029±0.034          |          |
|        | 5                    |                        |                      | 5        |
| scott  | 6 0.983±0.023        | 0.001±0.004            | 0.016±0.023          | 5        |
|        | 0.988±0.023          | 0.001±0.003            | 0.011±0.022          |          |
|        | 7                    |                        |                      | 5        |
|        | 8 0.989±0.017        | 0.002±0.005            | 0.010±0.017          | 5        |
|        | 0.974±0.068          | 0.026±0.068            | 0.000±0.000          |          |
|        | 4                    |                        |                      | 5        |
|        | 0.984±0.059          | 0.016±0.059            | 0.000±0.000          |          |
|        | 5                    |                        |                      | 6        |
| arpbbt | 6 0.991±0.039        | 0.009±0.039            | 0.000±0.000          | 8        |
|        | 0.993±0.029          | 0.007±0.029            | 0.000±0.000          |          |
|        | 7                    |                        |                      | 5        |
|        | 8 0.992±0.037        | 0.008±0.037            | 0.000±0.000          | 6        |
|        | (a)Accuracy          |                        | (b)FalsePositiveRate |          |
|        | (c)FalseNegativeRate | (d)NumberofTestQueries |                      |          |
Figure11.Testerperformanceforcubicreward‐statefeaturesrelationship
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 19


|     | (a)Accuracy          |                        | (b)FalsePositiveRate |     |

|     | (c)FalseNegativeRate | (d)NumberofTestQueries |                      |     |
Figure12.Testerperformanceforexponentialreward‐statefeaturesrelationship
Table10. Differenttestersversusgridworldwidthswithnon‐linearrewardstate‐featurerelationships
| Tester        | Width Accuracy | False        | False        | Numberof |

|               |                | positiverate | negativerate | queries  |
|               | 4 0.993±0.013  | 0.004±0.007  | 0.003±0.011  | 1        |
|               | 0.995±0.011    | 0.004±0.009  | 0.001±0.005  |          |
|               | 5              |              |              | 1        |
| rwt           | 6 0.995±0.008  | 0.003±0.006  | 0.002±0.005  | 1        |
|               | 0.995±0.008    | 0.003±0.006  | 0.002±0.005  |          |
| (cubic)       | 7              |              |              | 1        |
|               | 0.997±0.006    | 0.001±0.005  | 0.001±0.004  |          |
|               | 8              |              |              | 1        |
|               | 4 0.048±0.052  | 0.953±0.052  | 0.000±0.000  | 1        |
|               | 0.027±0.037    | 0.973±0.037  | 0.000±0.000  |          |
|               | 5              |              |              | 1        |
| rwt           | 6 0.017±0.021  | 0.983±0.021  | 0.000±0.000  | 1        |
|               | 0.012±0.019    | 0.988±0.019  | 0.000±0.000  |          |
| (exponential) | 7              |              |              | 1        |
|               | 0.006±0.012    | 0.994±0.012  | 0.000±0.000  |          |
|               | 8              |              |              | 1        |
|               | 4 0.968±0.040  | 0.000±0.000  | 0.032±0.040  | 16       |
|               | 0.977±0.031    | 0.000±0.000  | 0.023±0.031  |          |
|               | 5              |              |              | 20       |
| cst           | 6 0.991±0.015  | 0.000±0.000  | 0.010±0.015  | 24       |
|               | 0.988±0.019    | 0.000±0.000  | 0.012±0.019  |          |
| (cubic)       | 7              |              |              | 28       |
|               | 8 0.995±0.010  | 0.000±0.000  | 0.005±0.010  | 32       |
|               | 0.947±0.051    | 0.000±0.001  | 0.053±0.051  |          |
|               | 4              |              |              | 16       |
|               | 0.976±0.023    | 0.000±0.001  | 0.024±0.023  |          |
|               | 5              |              |              | 20       |
| cst           | 6 0.984±0.022  | 0.000±0.001  | 0.016±0.022  | 16       |
|               | 0.985±0.027    | 0.000±0.001  | 0.015±0.027  |          |
| (exponential) | 7              |              |              | 28       |
|               | 8 0.983±0.099  | 0.010±0.099  | 0.007±0.010  | 31       |
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 20


|                      | (a)Accuracy |     | (b)FalsePositiveRate   |     |

| (c)FalseNegativeRate |             |     | (d)NumberofTestQueries |     |
Figure13.Criticalstatestesterwithdifferentthresholds
Table11.Criticalstatestesterwithdifferentthresholds
| Tester     | Width Accuracy | False        | False        | Numberof |

|            |                | positiverate | negativerate | queries  |
|            | 0.971±0.036    | 0.000±0.000  | 0.029±0.036  |          |
|            | 4              |              |              | 16       |
|            | 0.985±0.023    | 0.000±0.000  | 0.015±0.023  |          |
| cst        | 5              |              |              | 20       |
| (threshold | 6 0.987±0.018  | 0.000±0.000  | 0.013±0.018  | 24       |
|            | 0.992±0.016    | 0.000±0.000  | 0.008±0.016  |          |
| =0.0001)   | 7              |              |              | 28       |
|            | 8 0.997±0.007  | 0.000±0.000  | 0.003±0.007  | 32       |
|            | 0.973±0.043    | 0.000±0.000  | 0.027±0.043  |          |
|            | 4              |              |              | 13       |
|            | 0.978±0.048    | 0.000±0.000  | 0.022±0.048  |          |
| cst        | 5              |              |              | 16       |
| (threshold | 6 0.987±0.018  | 0.000±0.000  | 0.013±0.018  | 24       |
|            | 0.980±0.100    | 0.010±0.099  | 0.009±0.019  |          |
| =0.2)      | 7              |              |              | 26       |
|            | 8 0.996±0.007  | 0.000±0.001  | 0.004±0.007  | 29       |
|            | 0.616±0.447    | 0.362±0.463  | 0.022±0.032  |          |
|            | 4              |              |              | 1        |
|            | 0.557±0.469    | 0.426±0.483  | 0.017±0.031  |          |
| cst        | 5              |              |              | 4        |
| (threshold | 6 0.563±0.482  | 0.431±0.488  | 0.007±0.013  | 4        |
|            | 0.575±0.485    | 0.421±0.488  | 0.004±0.009  |          |
| =0.8)      | 7              |              |              | 0        |
|            | 8 0.644±0.468  | 0.354±0.470  | 0.003±0.008  | 3        |
### 11.5 Timeprofileforalgorithmsandheuristics
Table 12 details the time taken by all algorithms and heuristics to verify 100 different
robotsforasinglehumanagent. WeobservedthatduetothecomplexityofSetCover
OptimalTeachingHeuristic,scotttakesthemaximumtimetocompletetheverificationwhilerwttakesminimumtime. Also,asexpected,withtheincreaseinthewidth
ofagridworld,thetimetakentoverifyincreases. FormostofthealgorithmsandheurisReScienceC8.2(#31)–PanigrahiandPatnaik2022 21


tics,thetimetakenincreases2Xwhenwidthofagridworldincreasesfrom4to8while
forscott,thetimetakenincreasesbyatleast3X.
Table12.Differenttestersversustimetaken
Tester Width Time(insec)
4 15.980
5 21.966
rwt 6 30.335
7 31.186
8 35.093
4 34.399
5 53.089
rt 6 54.039
7 66.959
8 73.450
4 39.110
5 55.968
vft 6 41.702
7 69.879
8 70.993
4 21.164
5 23.315
ptt 6 29.121
7 33.048
8 40.644
4 18.714
5 24.487
cst 6 30.871
7 32.206
8 36.563
4 95.301
5 143.555
scott 6 195.014
7 257.184
8 322.146
4 20.763
5 25.800
arpbbt 6 28.041
7 34.407
8 38.532
ReScienceC8.2(#31)–PanigrahiandPatnaik2022 22

---
**Source PDF:** `f75a60c87862.pdf` (2022_31_article.pdf)  
**URL:** https://zenodo.org/record/6574687/files/article.pdf
