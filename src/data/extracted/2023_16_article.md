Replication/MLReproducibilityChallenge2022
R E S C I E N C E C [Re] FOCUS: Flexible Optimizable Counterfactual
Explanations for Tree Ensembles
KyosukeMorita1,ID
1HeidelbergUniversity,Heidelberg,Germany
Editedby
KoustuvSinha,
MauritsBleeker, Reproducibility Summary
SamarthBhargav
Received ScopeofReproducibility—Thisstudyaims to reproducethe resultsof the paper’FOCUS:
04February2023
FlexibleOptimizableCounterfactualExplanationsforTreeEnsembles’byLucicetal.[1].
The main claims of the original paper are that FOCUS is able to (i) generate counterPublished
20July2023 factual explanations for all the instances in a dataset; and (ii) find counterfactual explanationsthatareclosertotheoriginalinputfortree‐basedalgorithmsthanexisting
DOI
methods.
10.5281/zenodo.8173678
Methodology—Thisstudyreplicatestheoriginalexperimentsusingthecode, data, and
models provided by the authors. Additionally, this study re‐implements code and retrains the models to evaluate the robustness and generality of FOCUS. All the experimentswereconductedonapersonallaptopwithaquad‐coreCPUwith8GBofRAMand
itapproximatelytook33hoursintotal.
Results—Thisstudywasabletoreplicatetheresultsoftheoriginalpaperintermsoffinding counterfactual explanations for all instances in datasets. Additional experiments
wereconductedtovalidatetherobustnessandgeneralityoftheconclusion. Whilethere
wereslightdeviationsintermsofgeneratingsmallermeandistances,halfofthemodels
stilloutperformedtheresultsoftheexistingmethod.
Whatwaseasy—TheimplementationoftheoriginalpaperispubliclyavailableonGitHub.
Therepositorycontainsthemodelsanddatausedintheoriginalexperiments. Also,the
authorsprovidedatechnicalappendix,whichincludesallhyperparametersthatwere
usedfortheexperimentsforreproductionuponrequest.
Whatwasdifficult—Althoughtheimplementationcodewasavailable,itemploysoutdated
packagesandthecodestructureiscomplex. Also,thecommentsinthefunctionsand
thedocumentationofthecodearesparseornonexistent,whichmadeitdifficulttofollowthecode.
Copyright©2023K.Morita,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoKyosukeMorita(kyosuke1029@icloud.com)
Theauthorshavedeclaredthatnocompetinginterestsexist.
Code is available at https://github.com/kyosek/focus-reproducibility – DOI 10.5281/zenodo.7931344. – SWH
swh:1:dir:e096a518285f9ee2f9ee2c5943293ba30f7e17b0.
Dataisavailableathttps://github.com/a-lucic/focus.
Openpeerreviewisavailableathttps://openreview.net/forum?id=n1q-iz83S5&noteId=60kzDmcWau.
ReScienceC9.2(#12)–Morita2023 1


Communicationwithoriginalauthors—I reached out to the authors to obtain the hyperparameters used in the experiments. The authors responded promptly with a detailed
technicalappendixoftheoriginalpaper.
## 1 Introduction
Theimportanceofinterpretabilityinmachinelearningmodelsisgrowingastheyare
increasingly being applied in real‐world scenarios. Understanding how models make
decisions not only benefitsthe users of the model, but also those whoare affected by
thedecisionsmadebythemodel. Counterfactualexplanationshavebeendevelopedto
copewiththisissue,astheyallowindividualstounderstandhowtheywouldachievea
desirableoutcomewithminimalchangestotheiroriginaldata. Lucicetal.[1]proposed
amethodcalledFOCUS,whichisdesignedtogenerateoptimaldistancecounterfactual
explanations to the original data for all the instances in tree‐based machine learning
models. This study aims to reproduce and evaluate their findings, as well as conduct
additionalexperiments.
## 2 Scope of reproducibility
The generation of counterfactual explanations is a problem that has been addressed
byseveralexistingmethods. Wachter,Mittelstadt,andRussell[2]formulatedthisproblemintoanoptimisationframework,however,thisapproachislimitedtodifferentiable
models. Theoriginalpaperaimedtoextendtheframeworktonon‐differentiablemodels,specificallytree‐basedalgorithms,byintroducingaprobabilisticmodelapproximation. A crucial aspect of this method is the approximation of a pretrained tree‐based
model, representedas f, achievedbyreplacingeach splitin eachtreewith a sigmoid
functionwithaparameterσthatisdefinedas:
sig(z)=(1+exp(σ·z)) −1, (1)
whereσ ∈ R . Thissigmoidfunctionisincorporatedintothefunctiont˜(x)thatap‐
>0 j
proximatesthenodejactivationt (x)ofthetree‐basedmodelfforagiveninputx. This
j
functionisdefinedas:

1,
ifjistheroot,
t˜ j (x)=  t˜ pj (x)·sig(θ j −x fj ), ifjisleftchild, (2)
t˜ (x)·sig(x −θ ), ifjisrightchild,
pj fj j
whereθ isathresholdforactivationofnodej.
j
ThismethodapproximatesasingledecisiontreeT.Atreeapproximationcanbedefined
as:
∑
T˜(y|x)= t˜(x)·T(y|j). (3)
j
j∈T
leaf
Additionally,thismethodreplacesthemaximumoperationoff,whichisanensemble
ofM manytreeswithweightsω ∈Rbyasoftmaxfunctionwithtemperatureτ ∈R .
m >0
Thus,theapproximationf˜
canbeexpressedas:
∑
exp(τ · M ω ·T˜ (y|x))
f˜(y|x)= ∑ m∑=1 m m (4)
exp(τ · M ω·T˜ (y′|x)
y′ m=1 m
Itisimportanttonotethatthisapproximationmethodcanbeappliedtoanytree‐based
model.
ThemainclaimsoftheoriginalpaperarethatFOCUSisableto:
ReScienceC9.2(#12)–Morita2023 2


• generatecounterfactualexplanationsforallinstancesinadataset‐Reliability.
• findcounterfactualexplanationsthatareclosertotheoriginalinputfortree‐based
algorithmsthanexistingframeworks‐Effectiveness.
## 3 Methodology
This study uses the code, data, and models provided by the original authors to reproduce their original experiments. In addition, to evaluate the robustness and generalityofFOCUS,severalmodificationsweremadetotheoriginalimplementation. These
modificationsinclude: (i)updatingtheversionsofTensorflowfrom1.14.0to2.11.0and
scikit‐learnfrom0.21.3to1.0.2,(ii)reorganisingthecodebyremovingredundantfunctionsandsimplifyingthecodestructureand(iii)addingunittests. Furthermore, this
studyconductsanadditionalexperimentson”Germancredit”dataset[3].
### 3.1 Modeldescriptions
ThepretrainedmodelsincludeDecisionTree(DT),RandomForest(RF),andAdaptive
Boosting(AB)withDTasabaselearner. Inaddition,thisstudyretrainedallmodels. The
setsofemployedhyperparametersarereportedinTable6inAppendixA.Inthecases
wherehyperparameterswerenotspecified,thedefaultvalueswereused. Theaccuracy
oftheretrainedmodelsisreportedinTable8inAppendixC.
### 3.2 Datasets
Thefourbinaryclassificationdatasetsusedintheoriginalexperimentsare:
• WineQuality[4]‐Thisdatasetcontains4,898datapointswith11features. Theoriginaldatasetpresentsthewinequalityonascaleof0‐10,buttheoriginalauthors
modifieditintobinaryclassification. Themodifieddatasetadaptsa”highquality”
wineifthequalityishigherthanorequalto7. Thereare1,060positiveclassdata
(22%).
• HELOC [5] ‐ This dataset contains 10,459 data points with 23 features. There are
5,000positiveclassdata(48%).
• COMPAS [6] ‐ This dataset contains 6,172 data points with 6 features. There are
2,990positiveclassdata(48%).
• Shopping [7]‐Thisdatasetcontains12,330datapointswith9features. Thereare
1,908positiveclassdata(15%).
Theoriginalpaperstatesthatallfeaturesinthedatasetsweretransformedintotherange
of0and1,andallcategoricalfeatureswereremoved.Thesedatasetswerepre‐processed
bytheoriginalauthors. Inadditiontothosedatasets, thisstudyemploystheGerman
creditdatasettotestthegeneralityofFOCUS.ThisGermanCreditdatasetaimstoclassifyindividualsintotwocategories,thosewithgoodcreditriskandthosewithbadcredit
risk. Itcontains999datapointswith49features,including7numericaland42categoricalfeatures. Insteadofremovingallthecategoricalfeatures,thisstudyusedone‐hot
encodingforallcategoricalfeatures. Furthermore,toruntheexperiments,thisstudy
normalisedthenumericalfeatures,sothatallthevaluesarebetween0and1. Thereare
300badcreditriskdatapoints(30%)inthisdataset.
Allmodelsusedintheexperimentsaretrainedon70%ofeachdatasetandtherestof
30%wereusedtofindcounterfactualexamples.
ReScienceC9.2(#12)–Morita2023 3


### 3.3 Hyperparameters
There are four hyperparameters of FOCUS, specifically, sigma (Equation 1), temperature(Equation4),distanceweight,whichisatrade‐offparameterbetweendistanceloss
andpredictionlossandlearningrateofAdam[8]. Thisstudyusedthehyperparameters
providedbytheoriginalauthorstoreproducetheoriginalexperiments.
Additionally, this study conducted a hyperparameter tuning using the Optuna package[9]’s Bayesian optimisation for the retrained models. The search spaces of hyperparameterscanbefoundinTable9intheAppendixD.Thesearchwasconductedfor
100trials. ItisworthnotingthatsinceDTmodelsdonotusethetemperatureparameter,
thesearchfortemperaturewasdisabledwhentuningDTmodels.
Duetoresourceandtimeconstraints,thisstudywasunabletorunhyperparametertuningforallmodelsanddatasetcombinations,particularlyforlargermodelssuchasRF
andABmodels. Theusedhyperparametersforalltheretrainedmodelsarereportedin
Table10,11,12and13inAppendixE.
### 3.4 Experimentalsetupandcode
Experiment1—Thisstudyaimstoreproduceexperimentsfromtheoriginalpaper,with
theexceptionofotherpapers’proposedmethods. Theexperimentsinclude(i)producingcounterfactualexplanationsforalldatasetsbyusingpretrainedmodelstoexamine
thereliabilityclaimand(ii)evaluatingeffectivenessclaimbycomparingtheaveragedistanceofcounterfactualexplanationsagainsttheexistingmethodscalledDACE[10].
The same evaluation metric as the original paper will be utilised in this study. Let X
be the set of N original data points and X¯ be the set of N generated counterfactual
explanations. Themeandistancemetriccanbederivedas:
∑N

d (X,X)= d(x(n),x(n)). (5)
mean N
N=1
Four distance functions are used for evaluation: Euclidean, Cosine, Manhattan, and
Mahalanobis. TheresultsoftheseexperimentscanbefoundinTable1and3.
Experiment 2—This study conducts additional experiments to provide further support
fortheclaims. Theseexperimentsaimtoevaluatetherobustnessandgeneralityofthe
FOCUS.Robustnessistestedbyupdatingthecodeimplementationandmodels,andgeneralityistestedbyapplyingtheupdatedFOCUSimplementationonadifferentdataset.
TheresultsoftheseexperimentscanbefoundinTable4and5.
### 3.5 Computationalrequirements
Alltheexperimentsinthisstudywereconductedonalaptopwitha1.4GHzQuad‐core
Intel Core i5 processor and 8 GB of RAM. The run time to rerun the experiments on
themodelswas: DecisionTree(DT)modelstookunderaminute,RandomForest(RF)
modelstookapproximately20minutesandAdaptiveBoosting(AB)modelstookapproximately15minutesonaverage. Toruntheretrainedmodels, DTmodelstookundera
minute,RFmodelstookapproximately30minutesandABmodelstook15minuteson
average. ThestudyalsoconductedhyperparametertuningonafewDTmodels,which
tookaround3hourspermodel.Intotal,rerunningtheexperimentstookaround8hours,
running the retrained models took around 9 hours, and hyperparameter tuning took
around16hours.
ReScienceC9.2(#12)–Morita2023 4


## 4 Results
### 4.1 Resultsreproducingoriginalpaper
Experiment1evaluatesthemainclaims,specificallyReliabilityandEffectiveness. Asdescribed in Section 3.4.1, experiment 1 reruns the published code by the authors and
comparestheresultstothereportedresultsintheoriginalpaper.
Reliability—Table1validatestheReliabilityclaimofFOCUSfornearlyallmodels,datasets
anddistancefunctioncombinations. Therearetwooutcomesthatfailedtofindcounterfactualexplanationsforallinstances‐RFandABmodelsonCOMPASdatasetusing
Manhattan distance. Based on the fact that the majority of outcomes align with the
original results, it is conjectured that the two unsuccessful outcomes were caused by
misreportedhyperparameters. Toevaluatethishypothesis,thisstudyconductedhyperparametertuningforthosetwomodels. Table2reportsthemeanManhattandistance
andfoundhyperparametersforthosetwocases. Afterthehyperparametertuning,both
experimentswereabletofindcounterfactualexplanationsforalltheinstancesandalso
themeandistancewasclosertotheoriginalresults. Althoughthereareslightdiscrepanciesinthererunresultsintermsofthemeandistances,thisstudywasabletoproduce
similarresultstotheoriginalpaperanddrawthesameconclusion‐rerunningtheoriginalexperimentwasabletofindacounterfactualexplanationforallinstances.
The results presented above demonstrate that the hyperparameters of FOCUS have a
strongimpactontheoutcomeoftheexperiments. Toprovidemoreinsightonthispoint,
section 4.2 discusses how the choice of hyperparameters affects the results and their
tendencies.
Effectiveness—The results that support the Effectiveness claim are presented in Table 3.
This table provides the mean Mahalanobis distance of the rerun models, the original
models, andtheexistingframework, DACE.Thererunmodels’resultsslightlydeviate
fromtheoriginalresults.SeveralmeanMahalanobisdistancesofthererunmodelswere
foundtobelargerthanthereportedresultsofDACE.Thisstudyattemptedtoreplicate
theresultsthroughhyperparametertuning,however,nosetofhyperparameterswasdiscoveredthatwouldproducetheresultsasoriginallyreported. AnotherpotentialexplanationforthedeviationofresultscouldberelatedtothecalculationoftheMahalanobis
distance, yetthoroughunittestsoftherelevantfunctionsdidnotrevealanyproblematic areas. Further investigation and experimentation may be necessary to fully comprehend the source of the discrepancy observed in this experiment. Despite this, the
studystillprovidesevidencethathalfofthererunmodelsexhibitedbetterresultsthan
thoseproducedbytheoriginalDACEframework, lendingpartialsupporttotheclaim
ofeffectiveness.
### 4.2 Resultsbeyondoriginalpaper
As described in 3.4, this study conducts additional experiments to test the robustness
andgeneralityofFOCUSintermsoftheReliabilityclaim. Thisisexaminedbyretraining
modelsontheupdatedcodeimplementationandapplyingFOCUSonthosemodelson
alldatasetsincludingtheGermancreditdataset.
RobustnessandGenerality—TherobustnessandgeneralityofFOCUSarepresentedthrough
theoutcomesoftheexperiment,asillustratedinTables4and5. Thefindingsrevealthat
all DT models are capable of generating counterfactual explanations for all instances,
while a limited number of RF and AB models were able to do so. Additionally, a significant proportion of the RF models encountered difficulties running due to limited
computationalresources,whichhaveimpactedtheabilitytoperformhyperparameter
ReScienceC9.2(#12)–Morita2023 5


|     | Dataset Distancefunction |     | DT    | RF AB       |     |

|     |                          |     | 0.268 | 0.188 0.268 |     |

|     |     |     | (0.268) | (0.188) (0.188) |     |

Wine
|     |     |     | 0.003 | 0.009 0.026 |     |


|     |     |     | (0.003) | (0.008) (0.014) |     |

|     |     |     | 0.268   | 0.312 0.528     |     |

|     |     |     | (0.268) | (0.312) (0.360) |     |

|     |     |     | 0.133   | 0.186 0.136     |     |

|     |     |     | (0.133) | (0.186) (0.136) |     |

HELOC
|     |     |     | 0.001 | 0.002 0.001 |     |


|     |     |     | (0.001) | (0.002) (0.001) |     |

|     |     |     | 0.152   | 0.284 0.203     |     |

|     |     |     | (0.152) | (0.284) (0.203) |     |

|     |     |     | 0.015   | 0.079 0.076     |     |

|     |     |     | (0.092) | (0.079) (0,076) |     |

COMPAS
|     |     |     | 0.008 | 0.011 0.007 |     |


|     |     |     | (0.008) | (0.011) (0.007) |     |

|     |     |     | 0.102   | 0.002* 0.072*   |     |

|     |     |     | (0.093) | (0.085) (0.090) |     |

|     |     |     | 0.142   | 0.023 0.028     |     |

|     |     |     | (0.142) | (0.025) (0.028) |     |


|     |     |     | 0.055 | 0.013 0.006 |     |


|     |     |     | (0.055) | (0.013) (0.006) |     |

|     |     |     | 0.128   | 0.026 0.047     |     |

|     |     |     | (0.128) | (0.026) (0.046) |     |

Table1. MeanEuclidean,CosineandManhattandistanceforalltheoriginaldatasetsandmodel
combinations.Thenumbersintheparenthesesarethemeandistanceofthereporteddistancein
theoriginalpaper.*denotesthatitfailedtoproducecounterfactualexplanationsforallinstances.
Model Meandistance sigma temperature distanceweight learningrate
| RF  | 0.116 | 6   | 12  | 0.01 | 0.002 |

| AB  | 0.090 | 4   | 1   | 0.05 | 0.001 |
Table2.FoundnewhyperparametersandManhattanmeandistances.
tuningformostoftheRFandABmodels. Thislimitationisfurtherexploredinfollowingsection.
Overall,theexperimentresultsprovideadditionalevidenceoftherobustnessandgeneralityofFOCUS’sreliabilityclaims.Althoughtheconclusionsdrawnfromtheexperiment
arelimitedtoDTmodels,theydemonstratethatFOCUScandrawthesameconclusions
astheoriginalstudy,evenwhenmodelsareretrainedonupdatedcodebasesandapplied
to a different dataset. However, further research couldextend these findings to other
modeltypes.
Impactofhyperparametersonresults—Duringtheexperiments,thisstudylearnedthathyperparameters affect results strongly. Theoretically, the hyperparameters of FOCUS
(sigmaandtemperature)influencethequalityofthemodelapproximationf˜
,off. As
sigmaincreases,theprobabilisticapproximationofthenodeactivationbecomesanexact approximation of the indicator functions (as per Equation 1), and increasing temperature leads the maximum operation of f to a unimodal softmax distribution (per
Equation4).
Empirically,thisstudyfoundthatthequalityoftheapproximationoftheoriginalmodel
f
has a significant effect on the results. For instance, the number of counterfactual
ReScienceC9.2(#12)–Morita2023 6


| Dataset | Model | Reproduction | Original OriginalDACE |       |

| Wine    | DT    | 2.354        | 0.542                 | 1.325 |
| HELOC   | DT    | 1.128        | 0.810                 | 1.427 |
|         | DT    | 0.938        | 0.776                 | 0.814 |
COMPAS
|     | AB  | 0.756 | 0.636 | 1.570 |

|     | DT  | 1.424 | 0.023 | 0.050 |

|     | AB  | 0.148 | 0.303 | 3.230 |

Table3.MeanMahalanobisdistanceforalltheoriginaldatasetsandmodelcombinations.
| Dataset | Distancefunction |        | DT RF       | AB    |

|         |                  |        | 0.358       | 0.197 |
|         | Euclidean        |        | ‐           |       |
|         |                  |        | (0)         | (954) |
| Wine    |                  |        | 0.006       | 1.458 |
|         |                  | Cosine | ‐           |       |
|         |                  |        | (0)         | (1)   |
|         |                  |        | 0.358       | 0.578 |
|         | Manhattan        |        | ‐           |       |
|         |                  |        | (0)         | (431) |
|         |                  |        | 4.069       | 4.436 |
|         | Mahalanobis      |        | ‐           |       |
|         |                  |        | (0)         | (435) |
|         |                  |        | 0.122       | 0.110 |
|         | Euclidean        |        | ‐           |       |
|         |                  |        | (0)         | (794) |
| HELOC   |                  |        | 0.001 1.248 | 1.213 |

|     |     |     | (0) (0)     | (0)   |

|     |     |     | 0.139 0.327 | 0.366 |

|     |             |     | (0) (0)     | (207) |

|     |             |     | 0.876       | 0.913 |
|     | Mahalanobis |     | ‐           |       |
|     |             |     | (0)         | (719) |
|     |             |     | 0.083 0.099 | 0.054 |

|        |     |     | (0) (8)     | (37)  |

| COMPAS |     |     | 0.012 1.273 | 1.088 |

|     |           |     | (0) (13)    | (14)   |

|     |           |     | 0.118       | 0.053  |
|     | Manhattan |     | ‐           |        |
|     |           |     | (0)         | (1330) |
|     |           |     | 1.158 0.470 | 0.479  |
Mahalanobis
|          |             |        | (0) (181) | (37)  |

|          |             |        | 0.0352    | 0.041 |
|          | Euclidean   |        | ‐         |       |
|          |             |        | (0)       | (280) |
| Shopping |             |        | 0.013     | 1.161 |
|          |             | Cosine | ‐         |       |
|          |             |        | (0)       | (40)  |
|          |             |        | 0.043     | 0.067 |
|          | Manhattan   |        | ‐         |       |
|          |             |        | (0)       | (305) |
|          |             |        | 0.460     | 0.734 |
|          | Mahalanobis |        | ‐         |       |
|          |             |        | (0)       | (317) |
Table4. MeanEuclidean,CosineandManhattandistanceforalltheoriginaldatasetsandmodel
combinations.‐denotesthatfailedtorun.Thenumbersintheparenthesesindicatethenumber
ofinstancesthatareunabletofindacounterfactualexplanation.
ReScienceC9.2(#12)–Morita2023 7


|     |     | Distancefunction | DT RF       | AB    |     |

|     |     |                  | 0.003 0.112 | 0.003 |     |

|     |     |     | (0) (0)     | (63)  |     |

|     |     |     | 1.001 1.424 | 1.502 |     |

|     |     |     | (0) (0)     | (6)   |     |

|     |     |     | 0.003 0.082 | 0.006 |     |

|     |     |             | (0) (9) | (40)  |     |

|     |     |             | 62.074  | 1.852 |     |
|     |     | Mahalanobis | ‐       |       |     |
|     |     |             | (0)     | (47)  |     |
Table5.MeanEuclidean,Cosine,ManhattanandMahalanobisdistanceofeachmodelontheGermancreditdataset. ‐denotesthatfailedtorun. Thenumbersintheparenthesesindicatethe
numberofinstancesthatareunabletofindacounterfactualexplanation.
Figure1.Foundcounterfactualexplanations%
Figure2.Hyperparameterimportanceforeach
| onCOMPASdataset. | Thisdatawascollected |     |                                         |     |     |

|                  |                      |     | dataset. Thisdatawascollectedwhenhyper‐ |     |     |
whenhyperparametertuningwasrunfor100
parametertuningforDTmodelsbyusingMatrialsontheDTmodelbyusingMahalanobis halanobis distance was run. Note that DT
| distance. | The Hyperparameter | tuning algo‐ |           |                     |             |

|           |                    |              | models do | not use temperature | hyperparam‐ |
rithmfoundoptimalsolutionsforover90%of
eters,thusthereareonlythreehyperparame‐
| instances | in most cases | (86 instances), there‐ |     |     |     |

terstunedforthosemodels.
fore,thefigurehasbeenscaledforimproved
visualisation.
ReScienceC9.2(#12)–Morita2023 8


explanationsfoundcanrangefrom20%to100%basedonthechosenhyperparameters
as demonstrated in Figure 1. The analysis of the hyperparameter importance for DT
models, as presented in Figure 2, indicates that the approximation of node activation
(sigma)hasastrongeffectonboththemeanMahalanobisdistanceandthenumberof
counterfactualexplanationsfoundonalldatasets.Conversely,changestotheprediction
loss‐distancelosstrade‐offparameter(distanceweight)andthelearningrateofAdam
did not exhibit a significant impact on the results. These findings are limited to DT
models,andfuturestudiescouldextendthesefindingstoothermodeltypes.
Modelsizeconsideration—This study encountered difficulties in running RF models for
more than half of the experiments. Initially, it was suspected that this difficulty was
causedmainlyduetolimitedcomputationalresources. Also,theoriginalpaper’sexperimentswereconductedonamachinewitha48‐coreCPUand256GBofRAM,whilethis
study’sexperimentswereconductedonacomputerwithaquad‐coreCPUand8GBof
RAM.
However, Table 7 in Appendix B shows that the majority of the retrained models are
smallerinsizeonthediskthantheoriginalones. Despitethis,thestudywasunableto
runtheretrainedmodelsbutwasabletoruntheoriginalones. Thissuggeststhatthe
inabilitytoexecutetheretrainedmodelsmaynotbesolelyattributedtotheirsize,and
otherfactorsmaybecontributing.
## 5 Discussion
This study aimed to assess the reliability and effectiveness claims of FOCUS and has
drawnseveralconclusionsbasedontheresultsoftwoexperiments.
Firstly, inregardstothereliability claim, theexperiments’resultsvalidatetheoriginal
paper’sresults. Also,theadditionalexperimentdemonstratedthatFOCUSisrobustand
generalisable. The additional experiment was limited to DT models, however, future
studiescouldexpandtheinvestigationtoothertree‐basedmodelssuchasXGBoost[11]
andLightGBM[12].
Moreover, this study sheds light on the impact of hyperparameters on the results of
FOCUS.ItwasdemonstratedthattheselectionofhyperparameterscansignificantlyinfluencetheabilityofFOCUStogeneratecounterfactualexplanations,thusemphasising
theimportanceofhyperparametertuninginfuturestudies.
Additionally,thestudyalsohighlightedtheissueofrunninglargermodelsasdescribed
in Section 4.2. This study suggests that this difficulty may not be solely due to model
size,butotherfactorsmayalsobecontributing. Furtherresearchisneededtoinvestigatethesefactorsandfindwaystoovercomethesechallenges,toenabletheapplication
ofFOCUSonlargermodels.
Theeffectivenessclaimispartiallysupportedbythisstudy. WhileFOCUSwasableto
generatethecounterfactualexplanationsforallinstances, themeanMahalanobisdistanceswerenotconsistentwiththeresultsreportedintheoriginalpaper. Thisdeviation
raisesquestionsaboutthereproducibilityoftheresultsandhighlightstheneedforfurtherinvestigationtodeterminethecause.
### 5.1 Whatwaseasy
Theoriginalpaper’simplementationisaccessibleonGitHub. Therepositoryincludes
themodelsanddatautilisedintheexperiments. Theauthorshavealsomadeavailablea
technicalappendix,whichcanberequestedandprovidesallthenecessaryinformation,
includinghyperparameterstoreproducetheexperiments.
ReScienceC9.2(#12)–Morita2023 9


### 5.2 Whatwasdifficult
Thecodefortheimplementationwasavailable,however,itutilisesoutdatedpackages
andthecodestructureiscomplex,makingitdifficulttofollowthecode. Additionally,
thecommentsanddocumentationwithinthecodeareminimalorabsent. Addingunit
tests to the codebase helped me to improve my understanding of the structure. Furthermore, for stronger support on the claims made in the paper, it would have been
beneficialtorunthepreviouslydevelopedframework,DACE,however,duetotimeconstraintsandthecomplexityofusingtheCPLEXOptimizer1,thisstudywasunabletodo
so.
### 5.3 Communicationwithoriginalauthors
I contacted the authors to obtain the hyperparameters used in the experiments, and
theyrespondedpromptlywithadetailedtechnicalappendixoftheoriginalpaper.
References
1. A.Lucic,H.Oosterhuis,H.Haned,andM.deRijke.“FOCUS:Flexibleoptimizablecounterfactualexplanationsfor
treeensembles.”In:ProceedingsoftheAAAIConferenceonArtificialIntelligence.Vol.36.5.2022,pp.5313–
5322.
2. S.Wachter,B.Mittelstadt,andC.Russell.“Counterfactualexplanationswithoutopeningtheblackbox:Auto-
mateddecisionsandtheGDPR.”In:Harv.JL&Tech.31(2017),p.841.
3. D.DuaandC.Graff.UCIMachineLearningRepository.2017.URL:http://archive.ics.uci.edu/ml.
4. P.Cortez,A.Cerdeira,F.Almeida,T.Matos,andJ.Reis.“Modelingwinepreferencesbydataminingfrom
physicochemicalproperties.”In:Decisionsupportsystems47.4(2009),pp.547–553.
5. FICO2017.HELOCDataset.2017.URL:https://community.fico.com/s/explainable-machine-learning-
challenge?tabset-158d9=3(visitedon01/08/2023).
6. D.Ofer.“COMPASDataset.”In:Kaggle:https://www.kaggle.com/danofer/compass(2017),p.19.
7. C.O.Sakar,S.O.Polat,M.Katircioglu,andY.Kastro.“Real-timepredictionofonlineshoppers’purchasing
intentionusingmultilayerperceptronandLSTMrecurrentneuralnetworks.”In:NeuralComputingandAppli-
cations31.10(2019),pp.6893–6908.
8. D.P.KingmaandJ.Ba.“Adam:Amethodforstochasticoptimization.”In:arXivpreprintarXiv:1412.6980
(2014).
9. T.Akiba,S.Sano,T.Yanase,T.Ohta,andM.Koyama.“Optuna:Anext-generationhyperparameteroptimization
framework.”In:Proceedingsofthe25thACMSIGKDDinternationalconferenceonknowledgediscovery&
datamining.2019,pp.2623–2631.
10. K.Kanamori,T.Takagi,K.Kobayashi,andH.Arimura.“DACE:Distribution-AwareCounterfactualExplanation
byMixed-IntegerLinearOptimization.”In:IJCAI.2020,pp.2855–2862.
11. T.ChenandC.Guestrin.“XGBoost:AScalableTreeBoostingSystem.”In:Proceedingsofthe22ndACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.KDD’16.SanFrancisco,Cal-
ifornia,USA:ACM,2016,pp.785–794.DOI:10.1145/2939672.2939785.URL:http://doi.acm.org/10.1145/
2939672.2939785.
12. G.Ke,Q.Meng,T.Finley,T.Wang,W.Chen,W.Ma,Q.Ye,andT.-Y.Liu.“Lightgbm:Ahighlyefficientgradient
boostingdecisiontree.”In:Advancesinneuralinformationprocessingsystems30(2017).
1http://www.ibm.com/analytics/cplex‐optimizer
ReScienceC9.2(#12)–Morita2023 10


| A   | Hyperparameters | for retrained |     | models |     |     |     |     |     |

Table 6 reports the hyperparameters that were used to retrain each model for each
dataset. Retrained DT models still employ the same hyperparameters as the original
models,buttheothermodels,mostofthemhaveasmallerstructurethantheoriginal
models.
|     |     | Dataset | Hyperparameter |     | DT  | RF  | AB  |     |     |

|     |     |         |                |     |     | 2 4 | 2   |     |     |

|     |     | Wine |     |     | (2) | (4)   | (4) |     |     |

|     |     |      |     |     |     | 1 100 | 100 |     |     |


|     |     |     |     |     |     | 4 2   | 1     |     |     |

|     |     | HELOC |     |     | (4) | (4)   | (8) |     |     |

|     |     |       |     |     |     | 1 100 | 100 |     |     |


|     |     |     |     |     |     | 4 2   | 1     |     |     |

|     |     | COMPAS |     |     | (4) | (4)   | (2) |     |     |

|     |     |        |     |     |     | 1 100 | 100 |     |     |


|     |     |     |     |     |     | 4 4   | 1     |     |     |

|     |     | Shopping |     |     | (4) | (8)   | (2) |     |     |

|     |     |          |     |     |     | 1 100 | 100 |     |     |


|     |     |     |     |     |     | 2 3   | 2     |     |     |

|     |     | German |     |     | (‐) | (‐)   | (‐) |     |     |

|     |     |        |     |     |     | 1 100 | 100 |     |     |

|     |     |     |     |     | (‐) | (‐) | (‐) |     |     |

Table6. Hyperparametersofretrainedmodels. Numbersintheparenthesesarethehyperparametersoftheoriginalmodels.
| B   | Model size | comparison |     |     |     |     |     |     |     |

Table7reportsthemodelsizesofretrainedandoriginalmodelsonthedisk. Mostretrainedmodelshaveasmallersizeassmallerhyperparameterswereusedcomparedto
theoriginalmodels.
|     |     | DT  |     |     | RF  |     |     | AB  |     |

Dataset Retrained Original Retrained Original Retrained Original
|     | Wine     | 3   | 2   | 263 |     | 711 | 48  |     | 131 |

|     | HELOC    | 4   | 2   | 94  |     | 703 | 34  |     | 148 |
|     | COMPAS   | 2   | 2   | 94  |     | 467 | 34  |     | 85  |
|     | Shopping | 4   | 2   | 265 |     | 143 | 34  |     | 89  |
|     | German   | 2   | ‐   | 144 |     | ‐   | 48  |     | ‐   |
Table7.Sizeofmodelsonthedisk.TheunitofthistableisKB.
|     | ReScienceC9.2(#12)–Morita2023 |     |     |     |     |     |     |     | 11  |

| C Accuracy | of retrained | models |     |     |     |

Thisstudyretrainedmodelswithnewhyperparametersinordertoconductfurtherexperiments. The train/test split method used in this study follows the original paper,
where70%ofthedatasetwasusedfortrainingand30%wasusedfortest. Thisstudy
employstheaccuracyscoreasametric. Theaccuracyscorecanbederivedas
|     |     |          | TP +TN     |     |     |

|     |     | Accuracy | =          | ,   | (6) |
|     |     |          | TP +TN +FP | +FN |     |
whereTPistruepositive,TNistruenegative,FPisfalsepositiveandFNisfalsenegative.
|     |     | Dataset  | DT RF       | AB    |     |

|     |     | Wine     | 0.796 0.788 | 0.771 |     |
|     |     | HELOC    | 0.679 0.692 | 0.701 |     |
|     |     | COMPAS   | 0.651 0.677 | 0.675 |     |
|     |     | Shopping | 0.890 0.893 | 0.892 |     |
|     |     | German   | 0.700 0.713 | 0.723 |     |
Table8.Accuracyofallthemodels
| D Hyperparameter |     | tuning |     |     |     |

In this study, hyperparameter tuning was performed on a few pretrained models and
retrained DT models by using Optuna’s Bayesian optimisation. Table 9 illustrates the
searchspacesofhyperparameters. ItisworthnotingthatsinceDTmodelsdonotuse
the temperature parameter, the search for temperature was disabled when tuning DT
modelstosavesomecomputationalcosts.
Searchspace
|     |     | Hyperparameter | Min   | Max Step   |     |

|     |     | sigma          | 1     | 20 1       |     |
|     |     | temperature    | 1     | 20 1       |     |
|     |     | distanceweight | 0.01  | 0.1 0.01   |     |
|     |     | learningrate   | 0.001 | 0.01 0.001 |     |
Table9.Hyperparametersandtheirsearchspaces
| E FOCUS | hyperparameters |     |     |     |     |

Table10,11,12and13reportusedhyperparametersforretrainedmodels. AsDTmodels
donotusetemperature,itisnotreported.
| ReScienceC9.2(#12)–Morita2023 |     |     |     |     | 12  |

|         | DT 1                    | ‐              | 0.05 | 0.001        |
Wine
|     | AB 5 | 1   | 0.05 | 0.005 |

|     | DT 2 | ‐   | 0.05 | 0.001 |
HELOC
|        | AB 10 | 1   | 0.05 | 0.001 |

|        | DT 4  | ‐   | 0.01 | 0.009 |
| COMPAS | RF 7  | 3   | 0.01 | 0.001 |
|        | AB 10 | 1   | 0.01 | 0.005 |
|        | DT 2  | ‐   | 0.05 | 0.005 |

|        | AB 10 | 1   | 0.05 | 0.001 |

|        | DT 7  | ‐   | 0.01 | 0.001 |
| German | RF 7  | 3   | 0.01 | 0.001 |
|        | AB 7  | 3   | 0.01 | 0.001 |
Table10.FOCUShyperparametersforusingEuclideandistance


|         | DT 1                    | ‐              | 0.05 | 0.005        |
Wine
|        | AB 1  | 1   | 0.01 | 0.005 |

|        | DT 2  | ‐   | 0.05 | 0.005 |
| HELOC  | RF 5  | 5   | 0.05 | 0.005 |
|        | AB 1  | 1   | 0.05 | 0.005 |
|        | DT 10 | ‐   | 0.05 | 0.005 |
| COMPAS | RF 10 | 6   | 0.01 | 0.005 |
|        | AB 10 | 1   | 0.05 | 0.005 |
|        | DT 10 | ‐   | 0.05 | 0.001 |

|        | AB 10 | 5   | 0.05 | 0.001 |

|        | DT 7  | ‐   | 0.01 | 0.001 |
| German | RF 7  | 3   | 0.01 | 0.001 |
|        | AB 7  | 3   | 0.01 | 0.001 |
Table11.FOCUShyperparametersforusingCosinedistance


|         | DT 1                    | ‐              | 0.05 | 0.001        |
Wine
|       | AB 6 | 1   | 0.01 | 0.005 |

|       | DT 2 | ‐   | 0.05 | 0.001 |
| HELOC | RF 5 | 5   | 0.01 | 0.005 |
|       | AB 4 | 1   | 0.05 | 0.001 |
|       | DT 6 | ‐   | 0.01 | 0.005 |
COMPAS
|     | AB 5 | 10  | 0.05 | 0.005 |

|     | DT 2 | ‐   | 0.05 | 0.005 |

|        | AB 10 | 1   | 0.05 | 0.001 |

|        | DT 7  | ‐   | 0.01 | 0.001 |
| German | RF 7  | 3   | 0.01 | 0.001 |
|        | AB 7  | 3   | 0.01 | 0.001 |
Table12.FOCUShyperparametersforusingManhattandistance
ReScienceC9.2(#12)–Morita2023 13


|         | DT 4                    | ‐              | 0.01 | 0.003        |
Wine
|     | AB 10 | 1   | 0.01 | 0.005 |

|     | DT 7  | ‐   | 0.01 | 0.002 |
HELOC
|        | AB 10 | 1   | 0.01 | 0.005 |

|        | DT 4  | ‐   | 0.01 | 0.008 |
| COMPAS | RF 10 | 1   | 0.01 | 0.005 |
|        | AB 4  | 2   | 0.05 | 0.001 |
|        | DT 20 | ‐   | 0.02 | 0.003 |

|     | AB 10 | 1   | 0.01 | 0.001 |

|     | DT 18 | ‐   | 0.01 | 0.003 |
German
|     | AB 7 | 3   | 0.01 | 0.001 |

Table13.FOCUShyperparametersforusingMahalanobisdistance
ReScienceC9.2(#12)–Morita2023 14

---
**Source PDF:** `7bbe8ec603ef.pdf` (2023_16_article.pdf)  
**URL:** https://zenodo.org/record/8173678/files/article.pdf
