TheThirty-FifthAAAIConferenceonArtificialIntelligence(AAAI-21)
Variational Fair Clustering
ImtiazMasudZiko1,JingYuan2,EricGranger1 andIsmailBenAyed1
1E´TSMontreal,Canada
2XidianUniversity,China
imtiaz-masud.ziko.1@etsmtl.ca
Abstract ofembeddingfairnessconstraintsthatencourageclustersto
havebalanceddemographicgroupspertainingtosomesensi-
Weproposeageneralvariationalframeworkoffairclustering, tiveattributes(e.g.,sex,gender,race,etc.),soastocounteract
whichintegratesanoriginalKullback-Leibler(KL)fairness
anyformofdata-inherentbias.
termwithalargeclassofclusteringobjectives,includingproto-
AssumethatwearegivenN datapointstobeassignedto
typeorgraphbased.Fundamentallydifferentfromtheexisting
asetofK clusters,andletS 2 f0;1gN denotesabinary
combinatorial and spectral solutions, our variational multi- k
indicator vector whose components take value 1 when the
termapproachenablestocontrolthetrade-offlevelsbetween
the fairness and clustering objectives. We derive a general pointiswithinclusterk,and0otherwise.Alsosupposethat
tightupperboundbasedonaconcave-convexdecomposition thedatacontainsJ differentdemographicgroups,withV j 2
ofourfairnessterm,itsLipschitz-gradientpropertyandthe f0;1gN denotingabinaryindicatorvectorofdemographic
Pinsker’sinequality.Ourtightupperboundcanbejointlyop- groupj.Theauthorsof(Chierichettietal.2017;Kleindessner
timizedwithvariousclusteringobjectives,whileyieldinga
etal.2019)suggestedtoevaluatefairnessintermsofcluster-
scalablesolution,withconvergenceguarantee.Interestingly,
balancemeasures,whichtakethefollowingform:
ateachiteration,itperformsanindependentupdateforeach
a l t a o s r s g e ig x e- n p s m l c o a e r l e n e t d d v i a f a f t r a e ia s re e b n t l s e t . . t T T ra h h d i e s e r - e s o c f f o a f r la e le b , v i i l t e i l c t s y an b is e b t i e w m e e p a e o s n r i t l t a y h n d e t i f a s a t s r i i r i b t n u e e t n s e s a d b a f l n e o d s r balance(S k )= j m 6= i j n 0 V V j j t t 0 S S k k 2[0;1] (1)
clusteringobjectives.Unlikespectralrelaxation,ourformula- Thehigherthismeasure,thefairerthecluster.Theoverall
tiondoesnotrequirecomputingitseigenvaluedecomposition. clusteringbalanceisdefinedbytheminimumofEq.(1)over
Wereportcomprehensiveevaluationsandcomparisonswith
k.Thisnotionoffairnessinclustershasrecentlygivenrise
state-of-the-art methods over various fair clustering bench-
to a new line of research that was introduced, mostly, for
marks,whichshowthatourvariationalformulationcanyield
prototype-basedclustering,e.g.,K-center,K-mediansandK-
highlycompetitivesolutionsintermsoffairnessandclustering
means(Chierichettietal.2017;Backursetal.2019;Schmidt,
objectives.
Schwiegelshohn,andSohler2018;Beraetal.2019).Also,
veryrecently,fairnesshasbeeninvestigatedinthecontext
Introduction ofspectralgraphclustering(Kleindessneretal.2019).The
general problem raises several interesting questions. How
Machinelearningmodelsareimpactingourdailylife,forin-
toembedfairnessinpopularclusteringobjectives?Canwe
stance,inmarketing,finance,education,andeveninsentenc-
control the trade-off between some “acceptable” fairness
ingrecommendations(Kleinbergetal.2017).However,these
level(ortolerance)andthequalityoftheclusteringobjective?
models may exhibit biases towards specific demographic
What is the cost of fairness with respect to the clustering
groupsdueto,forinstance,thebiasesthatexistwithinthe
objectiveandcomputationalcomplexity?
data.Forexample,ahigherleveloffacerecognitionaccu-
Chierichetti et al. (Chierichetti et al. 2017) investigated
racymaybefoundwithwhitemales(BuolamwiniandGebru
combinatorialapproximationalgorithmsformaximizingthe
2018).Thesebiaseshaverecentlytriggeredsubstantialinter-
thefairnessmeasuresinEq.(1),forK-centerandK-medians
estindesigningfairalgorithmsforthesupervisedlearning
clustering,andforbinarydemographicgroups(J =2).They
setting (Hardt, Price, and Srebro 2016; Zafar et al. 2017;
computefairlets,whicharegroupsofpointsthatarefair,and
Doninietal.2018).Also,veryrecently,thecommunityhas
cannotbesplitfurtherintomoresubsetsthatarealsofair.
started to investigate fairness constraints in unsupervised
Then,theyconsidereachfairletasadatapoint,andcluster
learning(Chierichettietal.2017;Kleindessneretal.2019;
themwithapproximateK-centerorK-mediansalgorithms.
Backursetal.2019;Samadietal.2018;Celisetal.2018).
Unfortunately,asreportedintheexperimentsin(Chierichetti
Specifically,Chierichettietal.(Chierichettietal.2017)pio-
etal.2017),obtainingfairsolutionswiththesefairlets-based
neeredtheconceptoffairclustering.Theproblemconsists
algorithmscomesatthepriceofasubstantialincreaseinthe
Copyright(cid:13)c 2021,AssociationfortheAdvancementofArtificial clusteringobjectives.Also,thecostforfindingfairletswith
Intelligence(www.aaai.org).Allrightsreserved. perfectmatchingisquadraticw.r.tthenumberofdatapoints,
11202

acomplexitythatincreasesformorethantwodemographic decomposition of our fairness term, its Lipschitz-gradient
groups.Severalcombinatorialsolutionsfollowed-uponthe propertyandthePinsker’sinequality.Ourtightupperbound
workin(Chierichettietal.2017)toreducethiscomplexity. canbejointlyoptimizedwithvariousclusteringobjectives,
Forinstance,Backursetal.(Backursetal.2019)proposed whileyieldingascalablesolution,withconvergenceguaran-
asolutiontomakethefairletdecompositionin(Chierichetti tee. Interestingly, at each iteration, our general variational
etal.2017)scalableforJ =2,byembeddingtheinputpoints fair-clustering algorithm performs an independent update
inatreemetric.Ro¨snerandSchmidt(Ro¨snerandSchmidt foreachassignmentvariable.Therefore,itcaneasilybedis-
2018)designeda14-approximatealgorithmforfairK-center. tributedforlarge-scaledatasets.Thisscalibilityisimportant
(Schmidt,Schwiegelshohn,andSohler2018;Huang,Jiang, as it enables to explore different trade-off levels between
andVishnoi2019)proposedfairK-means/K-mediansbased fairnessandtheclusteringobjective.Unliketheconstrained
on coreset – a reduced proxy set for the full dataset. Bera spectralrelaxationin(Kleindessneretal.2019),ourformula-
et al. (Bera et al. 2019) provided a bi-criteria approxima- tiondoesnotrequirecomputingitseigenvaluedecomposition.
tionalgorithmforfairprototype-basedclustering,enabling Wereportcomprehensiveevaluationsandcomparisonswith
multiplegroups(J > 2).Itisworthnotingthat,forlarge- state-of-the-artmethodsovervariousfair-clusteringbench-
scaledatasets,(Chierichettietal.2017;Ro¨snerandSchmidt marks, which show that our variational method can yield
2018;Beraetal.2019)sub-sampletheinputstomitigatethe highlycompetitivesolutionsintermsoffairnessandcluster-
quadraticcomplexityw.r.tN.Moreimportantly,thecombi- ingobjectives,whilebeingscalableandflexible.
natorialalgorithmsdiscussedabovearetailoredforspecific
prototype-basedobjectives.Forinstance,theyarenotappli- ProposedFormulation
cable to the very popular graph-clustering objectives, e.g.,
Let X = fx 2 RM;p = 1;:::;Ng denote a set of N
Ratio Cut or Normalized Cut (Von Luxburg 2007), which p
data points to be assigned to K clusters, and S is a soft
limitsapplicabilityinabreadthofgraphproblems,inwhich
cluster-assignment vector: S = [s ;:::;s ] 2 [0;1]NK.
datatakestheformofpairwiseaffinities. 1 N
For each point p, s = [s ] 2 [0;1]K is the probability
Kleindessneretal.(Kleindessneretal.2019)integrated p P p;k
simplexvectorverifying s =1.Supposethatthedata
fairness into graph-clustering objectives. They embedded k p;k
set contains J different demographic groups, with vector
linear constraints on the assignment matrix in spectral re-
V =[v ]2f0;1gN indicatingpointassignmenttogroup
laxation.Then,theysolvedaconstrainedtraceoptimization j j;p
j: v = 1 if data point p is in group j and 0 otherwise.
viafindingtheK smallesteigenvaluesofsometransformed p;j
We propose the following general variational formulation
Laplacian matrix. However, it is well-known that spectral
foroptimizinganyclusteringobjectiveF(S)withafairness
relaxationhasheavytimeandmemoryloadssinceitrequires
penalty,whileconstrainingeachs withintheK-dimensional
storinganN (cid:2)N affinitymatrixandcomputingitseigen- p
probabilitysimplexr =fy2[0;1]K j1ty=1g:
valuedecomposition–thecomplexityiscubicw.r.tN fora K
straightforwardimplementation,andsuper-quadraticforfast X
minF(S)+(cid:21) D (UjjP ) s.t. s 2r 8p (2)
implementations (Tian et al. 2014). In the general context KL k p K
S
ofspectralrelaxationandgraphpartitioning,issuesrelated k
tocomputationalscalabilityforlarge-scaleproblemsisdriv- D (UjjP )denotestheKullback-Leibler(KL)divergence
KL k
inganactivelineofrecentwork(Shahametal.2018;Ziko, betweenthegiven(required)demographicproportionsU =
Granger,andAyed2018;VladymyrovandCarreira-Perpin˜a´n [(cid:22) ] and the marginal probabilities of the demographics
j
2016). withinclusterk:
Theexistingfairclusteringalgorithms,suchasthecom-
VtS
binatorialorspectralsolutionsdiscussedabove,donothave P =[P(jjk)]; P(jjk)= j k 8j; (3)
mechanisms that control the trade-off levels between the k 1tS k
fairness and clustering objectives. Also, they are tailored
whereS = [s ] 2 [0;1]N istheN-dimensionalvector1
either to prototype-based (Backurs et al. 2019; Bera et al. k p;k
containingpointassignmentstoclusterk,andtdenotesthe
2019;Chierichettietal.2017;Schmidt,Schwiegelshohn,and
transposeoperator.Noticethat,attheverticesofthesimplex
Sohler2018)orgraph-basedobjectives(Kleindessneretal.
(i.e.,forhardbinaryassignments),VtS countsthenumber
2019). Finally, for a breadth of problems of wide interest, j k
ofpointswithintheintersectionofdemographicjandcluster
suchaspairwisegraphdata,thecomputationandmemory
k,whereas1tS isthetotalnumberofpointswithincluster
loadsmaybecomeanissueforlarge-scaledatasets. k
k.
Contributions: We propose a general, variational and
Parameter(cid:21)controlsthetrade-offbetweentheclustering
bound-optimizationframeworkoffairclustering,whichinte-
objectiveandfairnesspenalty.Theproblemin(2)ischalleng-
gratesanoriginalKullback-Leibler(KL)fairnesstermwitha
ingduetotheratiosofsummationsinthefairnesspenaltyand
largeclassofclusteringobjectives,includingbothprototype-
thesimplexconstraints.ExpandingKLtermD (UjjP )and
based (e.g., K-means/K- medians) and graph-based (e.g., KL k
NormalizedCutorRatioCut).Fundamentallydifferentfrom
1ThesetofN-dimensionalvectorsS andthesetofsimplex
theexistingcombinatorialandspectralsolutions,ourvaria- k
vectors s are two equivalent ways for representing assignment
p
tionalmulti-termapproachenablestocontrolthetrade-off variables.However,weuseS hereforaclearerpresentationofthe
k
levelsbetweenthefairnessandclusteringobjectives.Wede- problem,whereas,aswillbeclearerlater,simplexvectorss will
p
riveageneraltightupperboundbasedonaconcave-convex bemoreconvenientinthesubsequentoptimizationpart.
11203

discardingconstant(cid:22) log(cid:22) ,ourobjectivein(2)becomes additiveandmultiplicativeconstants,andforcurrentsolu-
|     |     |     | j   | j   |     |     |     |     |     |     |     |     |     |     |     |

equivalent to minimizing the following functional with re- tionsinwhicheachdemographicisrepresentedbyatleast
onepointineachcluster(i.e.,VtSi
specttotherelaxedassignmentvariables,andsubjecttothe (cid:21)18j;k):
|     |     |     |     |     |     |     |     |     |     |     |     | j   | k   |     |     |

simplexconstraints:
PN
|     |       |            |           |     |                           |     |     |     | G (S) | /   | st(bi   | +logs     | (cid:0)logsi)         |          |     |

|     |       |            |           | XX  |                           |     |     |     | i     |     | p=1     | p p       | p                     | p        |     |
|     | E(S)= | F(S)       | +(cid:21) |     | (cid:0)(cid:22) logP(jjk) |     | (4) |     |       |     |         |           |                       |          |     |
|     |       |            |           |     | j                         |     |     |     | with  |     | bi =[bi | ;:::;bi   |                       | ]        |     |
|     |       | |{z}       |           |     |                           |     |     |     |       |     | p       | p;1       | p;K                   |          |     |
|     |       |            |           | k j |                           |     |     |     |       |     |         |           |                       |          |     |
|     |       | clustering |           | |   | {z                        |     | }   |     |       |     |         | X(cid:16) |                       | (cid:17) |     |
|     |       |            |           |     |                           |     |     |     |       | bi  | = 1     | (cid:22)j | (cid:0) (cid:22)jvj;p |          | (9) |
|     |       |            |           |     | fairness                  |     |     |     |       |     | p;k L   | 1tSi      | VtSi                  |          |     |
|     |       |            |           |     |                           |     |     |     |       |     |         |           | k                     | j k      |     |
j
Observethat,inEq.(4),thefairnesspenaltybecomesacross-
entropy between the given (target) proportion U and the whereLissomepositiveLipschitz-gradientconstantverify-
| marginalprobabilitiesP |     |     | ofthedemographicswithincluster |     |     |     |     | ingL(cid:20)N. |     |     |     |     |     |     |     |

k
k.Noticethatourfairnesspenaltydecomposesintoconvex
Proof:Weprovideadetailedproofinthesupplementalma-
andconcaveparts:
terial.Here,wegivethemaintechnicalingredientsforob-
(cid:0)(cid:22) logP(jjk)=(cid:22) log1tS (cid:0)(cid:22) logVtS (5) tainingourbound.WeuseaquadraticboundandaLipschitz-
|     |     | j   |     | j   | k j | j   | k   |     |     |     |     |     |     |     |     |

| {z }| gradientpropertyfortheconvexpart,andafirst-orderbound
|     |     |     |     |     |     | {z  | }   |     |     |     |     |     |     |     |     |

concave convex on the concave part. We further bound the quadratic dis-
tancesbetweensimplexvariableswiththePinsker’sinequal-
Thisenablesustoderivethefollowingtightbounds(auxiliary
functions)forminimizingourgeneralfair-clusteringmodelin ity(CsiszarandKo¨rner2011).Thisstepavoidscompletely
(4)usingaquadraticboundandLipschitz-gradientproperty point-wiseLagrangian-dualprojectionsandinneriterations
forhandlingthesimplexconstraints,yieldingscalable(paral-
| of the | convex | part, | along with | Pinsker’s |     | inequality, | and a |     |     |     |     |     |     |     |     |

lel)updates,withconvergenceguarantee.
first-orderboundontheconcavepart.
|             |     |       |       |           |          |     |           | Proposition2(Boundontheclusteringobjective) |     |     |     |     |     |     | Given |

| Definition1 |     | A (S) | is an | auxiliary | function | of  | objective |                                             |     |     |     |     |     |     |       |
|             |     | i     |       |           |          |     |           |                                             |     |     |     | Si  |     |     |       |
E(S)ifitisatig htupperboundatcurrentsolutionSi,i.e.,it current clustering solution at iteration i, the auxiliary
satisfiesthefollowingconditions: functions for several popular clustering objectives F(S)
takethefollowinggeneralform:
|     |     |     | E(S) (cid:20) | A (S); | 8S  |     | (6a) |     |     |     |        |     |      |     |      |

|     |     |     |               | i      |     |     |      |     |     |     |        | PN  |      |     |      |
|     |     |     |               |        |     |     |      |     |     |     | H (S)= |     | stai |     | (10) |
|     |     |     | E(Si)=A       | (Si)   |     |     | (6b) |     |     |     | i      | p=1 | p p  |     |      |
i
|                            |     |     |     |     |     |     |     | wherepoint-wise(unary)potentialsai |     |     |     |     | aregiveninTable1. |     |     |

| whereiistheiterationindex. |     |     |     |     |     |     |     |                                    |     |     |     |     | p                 |     |     |
Proofs:Wegivedetailedproofsinthesupplementalmaterial.
Boundoptimizers,alsocommonlyreferredtoasMajorize-
Here,weprovidethemaintechnicalaspects:FortheNcut
Minimize(MM)algorithms(Zhang,Kwok,andYeung2007),
updatethecurrentsolutionSitothenextbyoptimizingthe objective,thederivationoftheauxiliaryfunctionisbasedon
thefactthat,forpositivesemi-definiteaffinitymatrixW,the
auxiliaryfunction:
Ncutobjectiveisconcave(Tangetal.2019).Therefore,the
|     |     |     | Si+1     |     |       |     |     | first-orderapproximationatthecurrentsolutionisanauxil- |     |     |     |     |     |     |     |

|     |     |     | =argminA |     | i (S) |     | (7) |                                                        |     |     |     |     |     |     |     |
S
iaryfunction.Fortheprototype-basedobjectives,deriving
Whentheseupdatescorrespondtotheglobaloptimaofthe anauxiliaryfunctionfollowsfromtheobservationthatthe
auxiliaryfunctions,MMproceduresenjoyastrongguarantee: optimal parameters c , i.e., those that minimize the objec-
k
tiveinclosed-form,correspondtothesamplemeans/medians
TheoriginalobjectivefunctionE(S)doesnotincreaseateach
withintheclusters.Theseauxiliaryfunctionscorrespondto
iteration:
thestandardK-meansandK-mediansprocedures,whichcan
|     | E(Si+1)(cid:20)A |     | (Si+1)(cid:20)A |     | (Si)=E(Si) |     | (8) |                                           |     |     |     |     |     |     |     |

|     |                  |     | i               |     | i          |     |     | beviewedasboundoptimizers(Tangetal.2019). |     |     |     |     |     |     |     |
Thisgeneralprincipleiswidelyusedinmachinelearningas Proposition3(Boundonthefair-clusteringfunctional)
ittransformsadifficultproblemintoasequenceofeasiersub- Given current clustering solution Si, at iteration i, and
|     |     |     |     |     |     |     |     | bringing | back | the | trade-off | parameter |     | (cid:21), we have | the |

problems(Zhang,Kwok,andYeung2007).Examplesofwell-
followingauxiliaryfunctionforthegeneralfair-clustering
knownboundoptimizersincludeconcave-convexprocedures
(CCCP)(YuilleandRangarajan2001),expectationmaximiza- objectiveE(S)inEq.(4):
tion(EM)algorithmsandsubmodular-supermodularproce-
PN
dures(SSP)(NarasimhanandBilmes2005),amongothers. A (S)= st (ai +(cid:21)bi +logs (cid:0)logsi ) (11)
|     |     |     |     |     |     |     |     |     | i   | p=1 | p   | p   | p   | p   | p   |

Themaintechnicaldifficultyinboundoptimizationishow
|     |     |     |     |     |     |     |     | Proof: | It is | straightforward |     | to check | that | sum of | auxiliary |

toderiveanauxiliaryfunction.Inthefollowing,wederive
functions,eachcorrespondingtoatermintheobjective,is
auxiliaryfunctionsforourgeneralfair-clusteringobjectives
alsoanauxiliaryfunctionoftheoverallobjective.
in(4).
Noticethat,ateachiteration,ourauxiliaryfunctionin(11)
Proposition1(Boundonthefairnesspenalty) Givencur- isthesumofindependentfunctions,eachcorrespondingtoa
Si
rent clustering solution at iteration i, we have the fol- singledatapointp.Therefore,ourminimizationproblemin
lowingauxiliaryfunctiononthefairnesstermin(4),upto (4)canbetackledbyoptimizingeachtermovers ,subjectto
p
11204

ai =[ai
|     | Clustering |     |     | F(S) |     |     |     |     | ]; 8k |     |     | Where |     |     |

|     |            |     |     |      |     |     | p   | p;k |       |     |     |       |     |     |
K-means P P s (x (cid:0)c )2 ai =(x (cid:0)ci )2 ci = X t S i
|     |     |     | N   | k p;k | p      | k   | p;k | p    | k    |     |     | k          | i k    |     |

|     |     |     |     |       |        |     |     |      |      |     |     |            | 1t S k |     |
|     |     | K-  | P   | P s   | d(x ;c | )   | ai  | =d(x | ;ci) |     | ci  | =argmind(x | ;x     | ),  |
|     |     |     | N   | k     | p;k p  | k   | p;k |      | p k  |     | k   |            | p      | q   |
p6=q
medians
disadistancemetric
|     |     |     |     | P   | tW  |     |     | 2P  | w (x p; xq)si |     |     | i) t | i   |     |

Ncut K(cid:0) S k Sk ai =d z i (cid:0) q p;k z i = (S k W S k
|     |     |     |     |     | k d tSk |     | p;k p | k   | d tS i |     |        | k (d t S                    | i) 2  |         |

|     |     |     |     |     |         |     |       |     | k      |     |        |                             | k P   |         |
|     |     |     |     |     |         |     |       |     |        |     | d=[d   | ],withd                     | = w(x | ;x );8p |
|     |     |     |     |     |         |     |       |     |        |     | p      | p                           | q     | p q     |
|     |     |     |     |     |         |     |       |     |        |     | W=[w(x | p ;x q )]isanaffinitymatrix |       |         |
Table1:Auxiliaryfunctionsofseveralwell-knownclusteringobjectives.
thesimplexconstraint,andindependentlyoftheotherterms, and, for Ncut, it is O(N2K) for full affinity matrix W or
whileguaranteeingconvergence: muchlesserforasparseaffinitymatrix.Notethatai canbe
p
computedefficientlyinparallelforalltheclusters.
|     | min   | st(ai | +(cid:21)bi | +logs | (cid:0)logsi); | 8p  | (12) |     |                                                |     |     |     |     |     |

|     |       | p     | p           | p     | p              | p   |      |     |                                                |     |     |     |     |     |
|     | sp2rK |       |             |       |                |     |      |     | Convergenceandmonotonicityguarantees:Ourvaria- |     |     |     |     |     |
tionalmodelbelongstothefamilyofMMprocedures,whose
Also,noticethat,inourderivedauxiliaryfunction,weob-
theoreticalguaranteesarewell-studiedintheliterature,e.g.,
| tainedaconvexnegativeentropybarrierfunctions |       |      |     |        |             |          | logs     | ,   |               |     |           |              |     |                  |

|                                              |       |      |     |        |             |          | p        | p   | (Vaida 2005). | In  | fact, the | MM principle |     | can be viewed as |
| which                                        | comes | from | the | convex | part in our | fairness | penalty. |     |               |     |           |              |     |                  |
Thisentropytermisveryinterestingasitavoidscompletely a generalization of well-known expectation-maximization
expensiveprojectionstepsandLagrangian-dualinneritera- (EM).Therefore,ingeneral,MMalgorithmsinheritthemono-
tonicityandconvergenceguaranteesofEMalgorithms,as
tionsforthesimplexconstraintofeachpoint.Ityieldsclosed-
formupdatesforthedualvariablesofconstraints1ts detailedinthetheoreticaldiscussionin(Vaida2005).Theo-
|     |     |     |     |     |     |     | p =1 |     |     |     |     |     |     |     |

rem3in(Vaida2005)statesaconditionforconvergenceof
| andrestrictsthedomainofeachs |     |     |     |     | tonon-negativevalues, |     |     |     |     |     |     |     |     |     |

p
avoiding extra dual variables for constraints s (cid:21) 0. In- thegeneralMMproceduretoalocalminimum:Theauxil-
p
terestingly, entropy-based barriers are commonly used in iaryfunctionhasauniqueglobalminimum,whichshouldbe
obtainedateachiterationwhensolving(7).Thiscondition
Bregman-proximaloptimization(Yuanetal.2017),andhave
isimportanttoguarantee,forinstance,themonotonicityin
well-knowncomputationalbenefitswhenhandlingdifficult
(8).Ourformulationsatisfiesthiscondition.Inourcase,the
simplexconstraints(Yuanetal.2017).However,theyarenot
verycommoninthegeneralcontextofclustering. auxiliaryfunctionin(11)isstrictlyconvex,asitisthesumof
Theobjectivein(12)isthesumofconvexfunctionswith lineartermsandastrictlyconvexterm(thenegativeentropy),
affinesimplexconstraints1ts =1.Asstrongdualityholds andisoptimizedunderaffinesimplexconstraints.Therefore,
p
ateachiteration,theclosed-formsolutionsweobtainedin
fortheconvexobjectiveandtheaffinesimplexconstraints,
(13)correspondtotheuniqueglobalminimumofauxiliary
thesolutionsoftheKarush-Kuhn-Tucker(KKT)conditions
|                                                   |     |     |     |     |     |     |     |     | functionA | (S)in(11).OurplotsinFig.1confirmthecon- |     |     |     |     |

| minimizegloballytheauxiliaryfunction.TheKKTcondi- |     |     |     |     |     |     |     |     |           | i                                       |     |     |     |     |
tionsyieldaclosed-formsolutionforbothprimalvariabless vergenceandmonotonicityofourgeneralMMprocedurefor
p
andthedualvariables(Lagrangemultipliers)corresponding severalfair-clusteringobjectives.
tosimplexconstraints1ts Exploring different trade-off levels via multiplier (cid:21):
p =1.
|     |     |     |     |                |               |     |     |     | Our variational |     | multi-term | formulation | enables | to explore |

|     |     |     | si  | exp((cid:0)(ai | +(cid:21)bi)) |     |     |     |                 |     |            |             |         |            |
si+1 = p p p 8p (13) several levels of trade-off between the clustering and fair-
p
1t[si exp((cid:0)(ai +(cid:21)bi))] nessobjectivesviamultiplierparameter(cid:21),unliketheexisting
|     |     |     | p   |     | p   | p   |     |     |     |     |     |     |     |     |

fair-clusteringmethods.Inpractice,weruninparallelour
|     | Notice | that each | closed-form |     | update | in (13) | is within |     |           |             |        |             |            |              |

|     |        |           |             |     |        |         |           |     | algorithm | for several | values | of (cid:21) | and choose | the smallest |
thesimplex.Wegivethepseudo-codeoftheproposedfair-
(cid:21)
clusteringinAlgorithm1.Thealgorithmcanbeusedforany value of that satisfies a pre-defined level of fairness er-
|                                                      |     |           |     |               |     |     |           |     | ror, i.e.,                                             | D (UjjP | k ) (cid:20) | (cid:15). This is | conceptually | similar to |

| specificclusteringobjective,e.g.,K-meansorNcut,among |     |           |     |               |     |     |           |     |                                                        | KL      |              |                   |              |            |
|                                                      |     |           |     |               |     | ai. |           |     | standardpenaltyandaugmented-Lagrangianapproachesin     |         |              |                   |              |            |
| others,                                              | by  | providing | the | corresponding |     | The | algorithm |     |                                                        |         |              |                   |              |            |
|                                                      |     |           |     |               |     | p   |           |     | constrainedoptimization,wheretheweightsofthepenalties2 |         |              |                   |              |            |
consistsofaninnerandanouterloop.Theinneriterations
aregraduallyincreased,untilreachingacertainpre-defined
| updatessi+1 |     | using(13)untilA |     |     | (S)doesnotchange,with |     |     |     |     |     |     |     |     |     |

p i precision (or duality gap) for the constraints; see Chapter
theclusteringtermai
fixedfromtheouterloop.Theouter
|           |     |             | p   |      |             |        |          |     | Chapter17.1in(NocedalandWright2006).Thedifference      |     |     |     |     |     |

| iteration |     | re-computes | ai  | from | the updated | si +1. | The time |     |                                                        |     |     |     |     |     |
|           |     |             |     | p    |             | p      |          |     | hereisthatwerunindependentlyforeach(cid:21),whichcanbe |     |     |     |     |     |
complexity of each inner iteration is O(NKJ). Also, the implementedinparallel.AsillustratedbytheplotsinFig.2,
| updates     | are | independent |     | for each  | data   | p and,           | thus, can be |     |     |     |     |     |     |     |

| efficiently |     | computed    | in  | parallel. | In the | outer iteration, | the          |     |     |     |     |     |     |     |
2Instandardconstrainedoptimization,penaltiestypicallytakea
| timecomplexityofupdatingai                         |     |     |     |     | dependsonthechosenclus- |     |     |     |                                                       |     |     |     |     |     |

|                                                    |     |     |     |     | p                       |     |     |     | quadraticform,unlikeourmethod,whichisbasedonaKLdiver- |     |     |     |     |     |
| teringobjective.Forinstance,forK-means,itisO(NKM), |     |     |     |     |                         |     |     |     | gencepenalty.                                         |     |     |     |     |     |
11205

Figure 1: The convergence of the proposed bound optimizers for minimizing several fair-clustering objectives in (4): Fair
K-means,FairNcutandFairK-medians.TheplotsarebasedontheSyntheticdataset.
Figure2:Clustering/Fairnessobjectivesvs.(cid:21).
Algorithm1ProposedFair-clustering Wechoosethreewell-knownclusteringobjectives:K-means,
|     |                                    |     |     |     | K- medians |     | and Normalized | cut | (Ncut), | and | integrate our |

|     | Input:X,Initialseeds,(cid:21),U,fV |     | gJ  |     |            |     |                |     |         |     |               |
j j=1
|     |     |     |     |     | fairness-penalty |     | bound with | the | corresponding |     | clustering |

Output:Clusteringlabels2f1;::;KgN
|     |     |     |     |     | boundsa | p (seeTable1).Werefertoourbound-optimization |     |     |     |     |     |

Initializelabelsfrominitialseeds.
versionsas:FairK-means,FairK-mediansandFairNcut3.
InitializeSfromlabels.
Notethatourformulationcanbeusedforotherclustering
Initializei=1.
objectives(ifaboundcouldbederivedfortheobjective).
repeat
|     |           |                   |     |     | We                                                       | investigate | the effect | of fairness |     | on the | original dis- |

|     | Computeai | fromS(seeTable1). |     |     |                                                          |             |            |             |     |        |               |
|     |           | p                 |     |     | crete(i.e.,w.r.t.binaryassignmentvariables)clusteringob- |             |            |             |     |        |               |
Initializesi exp((cid:0)ai ) jectives, and compare with the existing methods. We eval-
|     |     | p = | p . |     |     |     |     |     |     |     |     |

1texp((cid:0)ai) p uate the results in terms of the balance of each cluster
repeat
Computesi+1using(13). S k in (1), and define the overall balance of the cluster-
p
|     |       |        |     |     | ing as                                            | balance | = min          | balance(S | ).      | We further | propose |

|     | si    |  si+1. |     |     |                                                   |         | Sk             |           | k       |            |         |
|     | p     | p      |     |     | toevaluatethefairnesserror,whichistheKLdivergence |         |                |           |         |            |         |
|     | S=[si |        |     |     | P                                                 |         |                |           |         |            |         |
|     |       | ]; 8p. |     |     |                                                   | D (UjjP | ) in (2). This | KL        | measure | becomes    | equal   |
|     |       | p      |     |     | k                                                 | KL      | k              |           |         |            |         |
untilA (S)in(11)doesnotchange to zero when the proportions of the demographic groups
i
i=i+1.
|     |     |     |     |     | within | all the | output clusters | match | the | target | distribution. |

untilE(S)in(4)doesnotchange For Ncut, we use 20-nearest neighbor affinity matrix, W:
l p =argmaxs p;k ;8p. w(x ;x )=1ifdatapointx iswithinthe20-nearestneigh-
|     |           |     |     |     |         | p q                                        |     | q   |     |     |     |

|     |           | k   |     |     | borsofx | ,andequalto0otherwise.Inalltheexperiments, |     |     |     |     |     |
|     | labels=fl | gN  |     |     |         | p                                          |     |     |     |     |     |
p p=1 . we fixed L = 2 and found that this does not increase the
objective(seethedetailedexplanationinthesupplemental
material).Westandardizeeachdatasetbymakingeachfea-
tureattributetohavezeromeanandunitvariance.Wethen
when(cid:21)increases,thefairnesserrordecreasesandtheclus-
|     |     |     |     |     | performed | L2-normalization |     | of  | the features, | and | used the |

teringobjectiveincreases,whichisintuitive.Asdiscussed
standardK-means++(ArthurandVassilvitskii2007)togen-
| in  | more details | below (Tables | 2, 3 and | 4), our variational |     |     |     |     |     |     |     |

formulationcanachievesmallfairnesserrors(competitive erateinitialpartitionsforallthemodels.
withtheexistingstate-of-the-artfair-clusteringmethods),but
Datasets
withmuchbetterclusteringobjectives,consistentlyacrossall
thedatasets. Synthetic datasets: We created two types of synthetic
datasetsaccordingtotheproportionsofthedemographics,
eachhavingtwoclustersandatotalof400datapointsin2D
Experiments
features(figuresinthesupplementalmaterial).TheSynthetic
Inthissection,wepresentcomprehensiveempiricalevalu-
ationsoftheproposedfair-clusteringalgorithm,alongwith 3Codeisavailableat:https://github.com/imtiazziko/Variational-
| comparisonswithstate-of-the-artfair-clusteringtechniques. |     |     |     |     | Fair-Clustering |     |     |     |     |     |     |

11206

FairK-medians
Datasets
|     |     |     |     |     |     |     |                  | Objective |      | fairnesserror/balance |     |      |     |

|     |     |     |     |     |     |     | Backursetal.2019 |           | Ours | Backursetal.2019      |     | Ours |     |
Synthetic(N =400; J =2; (cid:21)=10) 299.859 292.4 0.00/1.00 0.00/1.00
Synthetic-unequal(N =400; J =2; (cid:21)=10) 185.47 174.81 0.77/0.21 0.00/0.33
Adult(N =32;561; J =2;; (cid:21)=9000) 19330.93 18467.75 0.27/0.31 0.01/0.43
Bank(N =41;108; J =3; (cid:21)=9000) N/A 19527.08 N/A 0.02/0.18
CensusII(N =2;458;285; J =2; (cid:21)=500000) 2385997.92 1754109.46 0.41/0.38 0.02/0.78
Table2:ComparisonoftheproposedFairK-mediansto(Backursetal.2019).
FairK-means
|     | Datasets |     |     |     |     |     |               | Objective |      | fairnesserror/balance |     |      |     |

|     |          |     |     |     |     |     | Beraetal.2019 |           | Ours | Beraetal.2019         |     | Ours |     |
Synthetic(N =400; J =2; (cid:21)=10) 758.43 207.80 0.00/1.00 0.00/1.00
Synthetic-unequal(N =400; J =2; (cid:21)=10) 180.00 159.75 0.00/0.33 0.00/0.33
Adult(N =32;561; J =2; (cid:21)=9000) 10913.84 9984.01 0.018/0.41 0.018/0.41
Bank(N =41;108; J =3; (cid:21)=6000) 11331.51 9392.20 0.03/0.16 0.05/0.17
CensusII(N =2;458;285; J =2; (cid:21)=500000) 1355457.02 1018996.53 0.07/0.77 0.02/0.78
Table3:ComparisonoftheproposedFairK-meansto(Beraetal.2019).
datasetcontainstwoperfectlybalanceddemographicgroups, susrecorddatafrom1990.Thedatasetcontains2;458;285

each having an equal number of points. For this data records.Weusedthegenderstatusasthesensitiveattribute,
set,weimposedtargettargetproportionsU =[0:5;0:5].To which contains 1;191;601 females and 1;266;684 males.
experiment with ourfairnesspenalty with unequalpropor- We chose the 25 numeric attributes as features, similarly
tions,wealsousedSynthetic-unequaldatasetwith300and to (Backurs et al. 2019). We set the number of clusters to
100pointswithineachofthetwodemographicgroups.In K = 20,andimposedproportionsU = [0:48;0:52]within
| thiscase,weimposedtargetproportionsU |           |             |              |                 |      | =[0:75;0:25]. |           | eachcluster. |     |     |     |     |     |

| Real                                 | datasets: |             | We use three | datasets        | from | the           | UCI ma-   |              |     |     |     |     |     |
| chine                                | learning  | repository, |              | one large-scale |      | data          | set whose | Results      |     |     |     |     |     |
demographicsarebalanced(Census),alongwithtwoother
Inthissection,wediscusstheresultsofthedifferentexperi-
datasetswithvariousdemographicproportions:
Bank4datasetcontains41188numberofrecordsofdirect mentstoevaluatetheproposedgeneralvariationalframework
forFairK-means,FairK-mediansandFairNcut.Wefurther
| marketing |     | campaigns | of a | Portuguese | banking |     | institution |     |     |     |     |     |     |

reportcomparisonswith(Beraetal.2019),(Backursetal.
correspondingtoeachclientcontacted(Moro,Cortez,and
|     |     |     |     |     |     |     |     | 2019) and | (Kleindessner | et al. | 2019) | in terms of | discrete |

Rita2014).Notethat,thepreviousfairclusteringmethods
fairnessmeasuresandclusteringobjectives.
(Beraetal.2019;Backursetal.2019)usedamuchsmaller
versionofBankdatasetwithonly4520numberofrecords Trade-off between clustering and fairness objectives:
Weassesstheeffectofimposingfairnessconstraintsonthe
| withJ | = 2and3attributes.Instead,weutilizethemarital |     |     |     |     |     |     |     |     |     |     |     |     |

originalclusteringobjectives.IneachplotinFig.2,theblue
statusasthesensitiveattribute,whichcontainsthreegroups
curvedepictsthediscrete-valuedclusteringobjectiveF(S)
(J = 3)–single,marriedanddivorced–andremovedthe
‘’Unknown”maritalstatus.Thus,wehave41;108recordsin (K-means or Ncut) obtained at convergence as a function
total.Wechose6numericattributes(age,duration,euribor of (cid:21). The fairness error is depicted in red. Observe that,
whenmultiplier(cid:21)increases(startingfromacertainvalue),
| of 3 | month | rate, no. | of employees, |     | consumer | price | index |     |     |     |     |     |     |

thediscreteclusteringobjectiveincreaseswhilethefairness
andnumberofcontactsperformedduringthecampaign)as
|                                    |     |     |     |     |                   |     |     | error decreases,        | which | is intuitive.                | Also, | the fairness | error |

| features.WesetthenumberofclustersK |     |     |     |     | =10,andimpose     |     |     |                         |       |                              |       |              |       |
|                                    |     |     |     |     |                   |     |     | approaches0when(cid:21) |       | ! +1,andboththeclusteringand |       |              |       |
| thetargetproportionsofthreegroupsU |     |     |     |     | =[0:28;0:61;0:11] |     |     |                         |       |                              |       |              |       |
withineachcluster. fairnessobjectivestendtoreachaplateaustartingfromacer-
Adult5 tainvalueof(cid:21).Thescalabilityofourmodelishighlyrelevant
|     | is  | a US | census record | data | set | from 1994. | The |     |     |     |     |     |     |

becauseitenablesustoexploreseveralsolutions,eachcorre-
datasetcontains32;561records.Weusedthegenderstatus
spondingtoadifferentvalueofmultiplier(cid:21),andtochoose
asthesensitiveattribute,whichcontains10771femalesand
thesmallest(cid:21)(i.e.,thebestclusteringobjective)thatsatisfies
21790males.Wechosethe5numericattributesasfeatures,
P
setthenumberofclusterstoK =10,andimposeproportions apre-definedfairnesslevel D (UjjP k )(cid:20)(cid:15).Asdetailed
k KL
U =[0:33;0:67]withineachcluster. below,thisflexibilityenabledustoobtainbettersolutions,
Census6isalarge-scaledatasetcorrespondingtoaUScen- in terms of fairness and clustering objectives, than several
recentfair-clusteringmethods.Lowfairnesserrorsaretypi-
4https://archive.ics.uci.edu/ml/datasets/Bank+Marketing callyachievedwithlargevaluesof(cid:21).Thisisduetothefact
5https://archive.is.uci/ml/datasets/adult thatthescaleofthefairnesspenaltycouldbemuchsmaller
6https://archive.ics.uci.edu/ml/datasets/US+Census+Data+(1990) thantheclusteringobjectives.Noticethat,forrelativelysmall
11207

FairNCUT
Datasets Objective fairnesserror/balance
Kleindessneretal.2019 Ours Kleindessneretal.2019 Ours
Synthetic(N =400; J =2; (cid:21)=10) 0.0 0.0 0.00/1.00 0.0/1.00
Synthetic-unequal(N =400; J =2; (cid:21)=10) 0.03 0.06 0.00/0.33 0.00/0.33
Adult(N =32;561; J =2; (cid:21)=10) 0.47 0.74 0.06/0.32 0.08/0.30
Bank(N =41;108; J =3; (cid:21)=40) N/A 0.58 N/A 0.39/0.14
CensusII(N =2;458;285; J =2; (cid:21)=100) N/A 0.52 N/A 0.41/0.43
Table4:ComparisonoftheproposedFairNCutto(Kleindessneretal.2019).
Figure3:EffectofK ontheclusteringobjectivesforvanillaclusteringandourvariationalfairclusteringmethods,including
theK-means,K-mediansandNcutobjectives.TheresultsareshownfortheBankdataset.Notethat,foreachplot,thevalueof
multiplier(cid:21)isfixed.
valuesof(cid:21),theK-meansobjective(bluecurve)fortheAdult rithmforseveralvaluesof(cid:21)inascendingorder,andchoose
dataset has an oscillating behaviour. This might be due to the smallest (cid:21) that satisfies a pre-defined level of fairness
thefactthat,forsmall(cid:21),theK-meansobjectivedominates error.Thisflexibilityandscalabilityenabledustoobtainsig-
the KL fairness term. However, after a certain value of (cid:21) nificantlybetterclusteringobjectivesandfairness/minimum-
((cid:21) (cid:21) 4000),thecurvesbecomesmooth,withapredictable balancemeasuresincomparisonsto(Backursetal.2019);
behaviour(i.e.,thefairnesstermdecreasesandtheclustering SeeTable2.Itisworthnotingthat,fortheBankdataset,we
termincreases).Whentheclusteringobjectivedominates,the wereunabletorun(Backursetal.2019)asthenumberof
oscillating behaviour might be due to the local minima of demographicgroupis3(i.e.J >2).Incomparisonto(Bera
boundoptimizationfortheK-meansterm.Wehypothesize et al. 2019), our variational method achieves significantly
that,withhighervaluesof(cid:21),theKLfairnessterm“convexi- betterK-meansclusteringobjectives,withapproximatelythe
fies”thefunction,andfacilitatesoptimization.Withsmaller samefairnesslevels.Notethat,wecanobtainbetterfairness
valuesof(cid:21),theK-meanstermdominates,withpossibilities withlarger(cid:21)values.Theseresultshighlightthebenefitsof
ofbeingstuckinlocalminima(K-meansiswell-knownto ourproposedvariationalformulation,whichprovidescontrol
besensitivetotheinitialconditions). overthetrade-offbetweenthefairnesslevelandclustering
ClusteringcostwithrespecttoK:Fig.3depictshowthe objective.InthecaseoffairNCut,(Kleindessneretal.2019)
clusteringobjectivesbehavew.r.tthenumberofclustersK, achievedslightlybetterNcutobjectivesthanourmodel,while
withandwithoutthefairnessconstraints.Weplotthediscrete achievingsimilarfairnesslevels.However,wewereunable
clusteringobjectivevs.KforK-means,K-mediansandNcut, torunthespectralsolutionof(Kleindessneretal.2019)for
using the Bank dataset, with each plot corresponding to a large-scaleCensusIIdataset,andforBank,duetoitscompu-
fixedmultiplier(cid:21).Inbothcases(i.e.,withandwithoutthe tationalandmemoryload(asitrequirescomputingtheeigen
fairnessconstraints),theobtainedclusteringobjectivesde- valuesofthesquareaffinitymatrix).
creasewithK,withthegapbetweentheclusteringobjective
obtained under fairness constraints and the vanilla cluster-
ingincreasingwithK.Thoseexperimentalobservationsare
consistentwiththeobservationsin(Beraetal.2019). Our algorithm scales up to more than two demographic
Comparisons to state-of-the-art methods: Our algo- groups, i.e. when J > 2 (e.g. Bank), unlike many of the
rithmisflexibleasitcanbeusedinconjunctionwithdifferent existing approaches. Furthermore, for NCut graph cluster-
well-knownclusteringobjectives.Thisenabledustocompare ing,ourboundoptimizercandealwithlarge-scaledatasets,
ourFairK-medians,FairK-meansandFairNcutversionsto unlike(Kleindessneretal.2019),whichrequireseigende-
(Backursetal.2019),(Beraetal.2019)and(Kleindessner compositionforlargeaffinitymatrices.Finally,theparallel
etal.2019),respectively.Tables2,3and4reportcompar- structureofouralgorithmwithineachiteration(i.e.,indepen-
isonsintermsoftheoriginalclusteringobjectives,achieved dentupdatesforeachassignmentvariable)enablestoexplore
minimumbalancesandfairnesserrors,forFairK-medians, different values of (cid:21), thereby choosing the best trade-off
FairK-meansandFairNCut.Forourmodel,werunthealgo- betweentheclusteringobjectiveandfairnesserror.
11208

BroaderImpact Narasimhan, M.; and Bilmes, J. 2005. A Submodular-
|     |     |     |     |     |     |     | supermodular | Procedure | with Applications | to Discrimina- |     |

Thispaperdealswithensuringfairnesscriteriainclustering
decisions,soastoavoidunfairtreatmentofminoritygroups tive Structure Learning. In Conference on Uncertainty in
|            |               |     |           |      |         |              | ArtificialIntelligence(UAI),404–412. |     |     | ISBN0-9749039-1-4. |     |

| pertaining | toa sensitive |     | attribute | such | asrace, | gender, etc. |                                      |     |     |                    |     |
Thepaperisanendeavortopresentaflexiblemechanism,so Nocedal,J.;andWright,S.2006. Numericaloptimization.
| astorelativelycontroltherequiredfairness,whileensuring |     |     |     |     |     |     | Springer. |     |     |     |     |

clusteringqualityatthesametime.
|     |     |     |     |     |     |     | Ro¨sner,C.;andSchmidt,M.2018. |     | Privacypreservingclus- |     |     |

|     |     |     |     |     |     |     | teringwithconstraints.        |     | InICALP.               |     |     |
References
Samadi,S.;Tantipongpipat,U.T.;Morgenstern,J.H.;Singh,
Arthur,D.;andVassilvitskii,S.2007. k-means++:Thead- M.; and Vempala, S. 2018. The Price of Fair PCA: One
vantagesofcarefulseeding. InACM-SIAMsymposiumon InNeuralInformationProcessingSystems
Extradimension.
Discretealgorithms,1027–1035.SocietyforIndustrialand
(NeurIPS),10999–11010.
AppliedMathematics.
|     |     |     |     |     |     |     | Schmidt,M.;Schwiegelshohn,C.;andSohler,C.2018. |     |     |     | Fair |

Backurs,A.;Indyk,P.;Onak,K.;Schieber,B.;Vakilian,A.; CoresetsandStreamingAlgorithmsforFairk-MeansClus-
andWagner,T.2019. Scalablefairclustering. International tering. arXiv1304.6478abs/1812.10854.
conferenceonmachinelearning(ICML)405–413.
Shaham,U.;Stanton,K.;Li,H.;Basri,R.;Nadler,B.;and
Bera, S.; Chakrabarty, D.; Flores, N.; and Negahbani, M. Kluger,Y.2018.SpectralNet:SpectralClusteringusingDeep
2019. Fairalgorithmsforclustering. InAdvancesinNeural NeuralNetworks. InInternationalConferenceonLearning
InformationProcessingSystems,4955–4966. Representations(ICLR).
Buolamwini, J.; and Gebru, T. 2018. Gender shades: In- Tang,M.;Marin,D.;Ayed,I.B.;andBoykov,Y.2019.Kernel
tersectionalaccuracydisparitiesincommercialgenderclas- Cuts:KernelandSpectralClusteringMeetRegularization.
sification. In Conference on Fairness, Accountability and InternationalJournalofComputerVision127:477–511.
Transparency,77–91.
|           |              |     |               |     |                |     | Tian, F.;                                      | Gao, B.; Cui, | Q.; Chen, E.; | and Liu, T.-Y. | 2014. |

|           |              |     |               |     |                |     | Learningdeeprepresentationsforgraphclustering. |               |               | InAAAI         |       |
| Celis, L. | E.; Keswani, |     | V.; Straszak, |     | D.; Deshpande, | A.; |                                                |               |               |                |       |
ConferenceonArtificialIntelligence,1293–1299.
| Kathuria, | T.; and | Vishnoi, | N.  | K. 2018. | Fair | and Diverse |     |     |     |     |     |

DPP-BasedDataSummarization. InInternationalConfer- Vaida, F. 2005. Parameter convergence for EM and MM
enceonMachineLearning(ICML),715–724.
|     |     |     |     |     |     |     | algorithms. | StatisticaSinica15:831–840. |     |     |     |

Chierichetti,F.;Kumar,R.;Lattanzi,S.;andVassilvitskii,S.
|                                      |     |     |     |     |                  |     | Vladymyrov,M.;andCarreira-Perpin˜a´n,M.2016. |        |                 | TheVari-           |     |

| 2017. FairClusteringThroughFairlets. |     |     |     |     | InNeuralInforma- |     |                                              |        |                 |                    |     |
|                                      |     |     |     |     |                  |     | ational Nystrom                              | method | for large-scale | spectral problems. |     |
tionProcessingSystems(NeurIPS),5036–5044. InInternationalConferenceonMachineLearning(ICML),
211–220.
| Csiszar, I.; | and Ko¨rner, |     | J. 2011. | Information |     | theory: cod- |     |     |     |     |     |

ingtheoremsfordiscretememorylesssystems. Cambridge Von Luxburg, U. 2007. A tutorial on spectral clustering.
| UniversityPress. |     |     |     |     |     |     | Statisticsandcomputing17(4):395–416. |     |     |     |     |

Donini,M.;Oneto,L.;Ben-David,S.;Shawe-Taylor,J.;and Yuan, J.; Yin, K.; Bai, Y.; Feng, X.; and Tai, X. 2017.
Pontil,M.2018. EmpiricalRiskMinimizationUnderFair- Bregman-ProximalAugmentedLagrangianApproachtoMul-
nessConstraints. InNeuralInformationProcessingSystems tiphaseImageSegmentation. InScaleSpaceandVariational
| (NeurIPS),2796–2806. |     |     |     |     |     |     | MethodsinComputerVision(SSVM),524–534. |     |     |     |     |

Hardt,M.;Price,E.;andSrebro,N.2016. EqualityofOp- Yuille,A.L.;andRangarajan,A.2001.TheConcave-Convex
portunity in Supervised Learning. In Neural Information Procedure(CCCP). InNeuralInformationProcessingSys-
| ProcessingSystems(NeurIPS),3315–3323. |        |         |          |                    |       |              | tems(NIPS),1033–1040. |                   |                  |            |      |

|                                       |        |         |          |                    |       |              | Zafar, M.             | B.; Valera, I.;   | Gomez-Rodriguez, | M.; and    | Gum- |
| Huang, L.;                            | Jiang, | S.; and | Vishnoi, | N.                 | 2019. | Coresets for |                       |                   |                  |            |      |
|                                       |        |         |          |                    |       |              | madi, K.              | P. 2017. Fairness | Constraints:     | Mechanisms | for  |
| clusteringwithfairnessconstraints.    |        |         |          | InAdvancesinNeural |       |              |                       |                   |                  |            |      |
InformationProcessingSystems,7587–7598. FairClassification. InInternationalConferenceonArtificial
IntelligenceandStatistics(AISTATS),962–970.
Kleinberg,J.;Lakkaraju,H.;Leskovec,J.;Ludwig,J.;and
Mullainathan,S.2017.Humandecisionsandmachinepredic- Zhang,Z.;Kwok,J.T.;andYeung,D.-Y.2007. Surrogate
|     |     |     |     |     |     |     | maximization/minimizationalgorithmsandextensions. |     |     |     | Ma- |

tions. Thequarterlyjournalofeconomics133(1):237–293.
chineLearning69:1–33.
Kleindessner,M.;Samadi,S.;Awasthi,P.;andMorgenstern,
|          |            |     |          |            |      |          | Ziko,I.;Granger,E.;andAyed,I.B.2018. |     |     | ScalableLapla- |     |

| J. 2019. | Guarantees | for | Spectral | Clustering | with | Fairness |                                      |     |     |                |     |
cianK-modes.InAdvancesinNeuralInformationProcessing
| Constraints.         | InInternationalConferenceofMachineLearn- |         |       |          |               |     |                      |     |     |     |     |

| ing(ICML),3458–3467. |                                          |         |       |          |               |     | Systems,10041–10051. |     |     |     |     |
| Moro, S.;            | Cortez,                                  | P.; and | Rita, | P. 2014. | A data-driven | ap- |                      |     |     |     |     |
proachtopredictthesuccessofbanktelemarketing.Decision
SupportSystems62:22–31.
11209

---
**Source PDF:** `2022_14_article.pdf`
