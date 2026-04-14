Replication/MLReproducibilityChallenge2022
R E S C I E N C E C [Re] Reproducibility Study of ”Focus On The Common
Good: Group Distributional Robustness Follows”
WalterSimoncini1,ID,IoannaGogou1,ID,MartaFreixoLopes1,ID,andRonKremer1,ID
1UniversityofAmsterdam,Amsterdam,TheNetherlands
Editedby
KoustuvSinha,
MauritsBleeker, Reproducibility Summary
SamarthBhargav
Received ScopeofReproducibility—Thispaperattemptstoreproducethemainclaimsof“FocusOn
04February2023
TheCommonGood: GroupDistributionalRobustnessFollows”byPiratlaetal.,which
introduces Common Gradient Descent (CGD), a novel optimization algorithm for hanPublished
20July2023 dlingspuriouscorrelationsandsub‐populationshifts. Wehaveidentifiedthreecentral
claims: (I) CGD is more robust than Group-DRO and leads to the largest average loss
DOI
decreaseacrossallgroups(II)CGDgeneralizesbetteracrossallgroupsincomparisonto
10.5281/zenodo.8173707
ERM,and(III)CGDmonotonicallydecreasesthegroup‐averageloss.
Methodology—Theexperimentsofthispaperarebasedontheopensourceimplementationof CGDreleasedbytheauthors, whichrequiredsomemodificationstoworkwith
thelatestversionoftheWILDSframework.
Results—Theresultsfromourexperimentswereoverallinlinewiththepaper. Weshow
thatCGDoutperformsGroup-DROonsyntheticdatasetswithinducedspuriouscorrelations, butthebenefitsof CGDarenotclearinareal‐worldsetting. Beyondtheresults
of the original paper, our attempt to empirically verify the mathematical proof of the
authorsthatCGDmonotonicallydecreasesthelosswasnotconclusive.
Whatwaseasy—The implementation from the original paper was available on GitHub
withdetailedinstructionsprovidedinthedocumentation. Itwasalsorelativelyeasyto
introduceadditionaldatasetsandalgorithmstotheWILDScodebase.
Whatwasdifficult—TheCGDimplementationandseveralexperimentscouldnotberun
out‐of‐the‐boxandrequiredmajormodificationstorunwiththelatestversionofWILDS.
Themajorityofthehyperparametervaluesfortheexperimentswerenotclearlystated.
Lastly,theexperimentswerecomputationallyexpensiveandrequired440GPUhours.
Communicationwithoriginalauthors—Wereachedouttotheoriginalauthorstorequestadditionalinformationaboutthehyperparametervaluesandtheimplementationofsome
experiments. Theauthorspromptlyrespondedwithsourcesforthehyperparameters,
usefulinformationaboutWILDSandprovidedsomemissingpartsofthecode. Overall,
thecommunicationsweretimelyandeffective.
Copyright©2023W.Simoncinietal.,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoWalterSimoncini(walter.simoncini@student.uva.nl)
Theauthorshavedeclaredthatnocompetinginterestsexist.
Code is available at https://github.com/WalterSimoncini/CGD-Reproduction – DOI 10.5281/zenodo.7998663. – SWH
swh:1:dir:4a89288fc050158c419caee05af572cad7b71a12.
Openpeerreviewisavailableathttps://openreview.net/forum?id=ye8PftiQLQ.
ReScienceC9.2(#23)–Simoncinietal.2023 1


## 1 Introduction
Inrecentyears,deepneuralnetworkshavebecomestate‐of‐the‐artsolutionsformany
tasks. However,forsome,theytendtoachievehighoverallpredictionaccuracyatthe
costofmispredictingsamplesfromminoritygroups. Thisisdangerousforautomatic
decisionsystemsthatmakecriticaldecisions. Forinstance,modelstrainedwithEmpiricalRiskMinimization(ERM)areparticularlysusceptibletothisissue. Oneofthe key
reasonsforthisbehavior,identifiedbybothSagawaetal.[1] andKohetal.[2], istheexistenceofspuriouscorrelationsbetweenthefeaturesandlabelsofthemajoritygroup,
whichmaynotexistorcorrelatenegativelyforminoritygroups. Toovercomethis,several new algorithms have been proposed, such as Group Distributionally Robust Optimization(Group‐DROorG-DRO)[1],andCommonGradientDescent(CGD)[3]. Thefirst
tacklestheproblembytrainingonthegroupwiththelargesttrainingloss. Nevertheless,
Piratla,Netrapalli,andSarawagi[3]observedthatthismightleadtoimbalancedtraining
duetoincreasedlossintheothergroups. Incontrast, CGDtrainsonthegroupwhich
minimizesthelossacrossallgroups. Theauthorsclaimthatsuchanapproachmodels
inter‐group interactions and addresses spurious correlations. This report aims to verifytheclaimsoftheauthorsbyreproducingtheirfindingsandperformingadditional
experiments. Ourcontributioncanbesummarizedasfollows:
• Wereproduceboththequalitativeandquantitativeexperimentstoidentifywhich
claimscanbeverified. Wealsoquantifythecomputationalanddevelopmentcost
needed.
• WeupdatetheCGDcodetomakeitcompatiblewiththelatestversionoftheWILDS
framework[2]anddocumentthestepstakentoreproducethepaper, makingfuturereproductionseasierandmoreaccessible.
• WeimplementedthecoderequiredtorunexperimentsontheMultiNLI[4]dataset.
## 2 Scope of reproducibility
Thepaper“FocusOnTheCommonGood: GroupDistributionalRobustnessFollows”[3]
attemptstotackletheproblemsofspuriouscorrelationsandsub‐populationshiftwith
a new optimization algorithm: Common Gradient Descent (CGD). CGD optimizes the
model using the group “whose gradients lead to the largest decrease in average training loss over all groups” [3]. In this reproducibility study, we attempt to validate the
followingclaimsmadebytheauthors:
• CGDismorerobustthanGroup-DROinthepresenceofspuriousfeatures: byfocusingonthegroupthatleadstothelargestlossdecreaseacrossallgroups,CGD
isrobustagainstspuriousfeatures.
• CGD generalizes better across all groups in comparison to ERM: a model trained
withCGDshouldperformbetteronminoritygroupswhileachievingacomparable
averageaccuracy.
• CGD monotonically decreases the macro/group‐average loss: the authors prove
this claim mathematically, showing that CGD finds first‐order stationary points.
Weattempttovalidatethisclaimempiricallyoverthreedatasetsusedbythepaper.
Inthisreproducibilitystudy,duetoresourceandtimeconstraints,wedecidedtocompare the performance of CGD only against ERM and Group-DRO. This decision is also
motivatedbythefactthattheotherrobustnessalgorithmsmentionedinthepaperwere
notdiscussedasthoroughly. Weconsiderthissubsetofalgorithmssufficienttovalidate
ReScienceC9.2(#23)–Simoncinietal.2023 2


theclaimsstatedabove. Moreover,forthereal‐worlddatasetsfromtheWILDSbenchmark [2], we only trained with CGD, given that the documented results with the other
algorithmswerehighlycorrelatedwiththevaluesreportedintheofficialWILDSpaper
[2] and the WILDS benchmark. Therefore, we felt these two were reliable sources for
validatingtheseresults.
## 3 Methodology
To conduct our experiments we utilized the code for CGD which was released by the
authors on their GitHub repository 1. The available implementation was designed to
be run using version 1.2.2 of the WILDS framework [2]. In the months following the
coderelease,WILDSunderwentamajorupdate[5]toversion2.0. InordertomakeCGD
compatiblewiththenewframeworkversion,wehadtoimplementsomeminortweaks,
especiallyfordatasetswithdisjointgroupsforthetraining,validation,andtestsets. The
authorsalsoprovidedtheinitializationcodeforthedatasetsusedinthequalitativeevaluationofthealgorithm. Thecodeforthedatasetsusedinthequantitativeevaluation
wasincludedintheWILDSrepository,exceptforMultiNLI,whichweimplementedusingthecodeintheGroup-DROrepository[1]asindicatedbytheauthors.
### 3.1 Algorithmdescriptions
Thissectiondescribesthealgorithmsusedtovalidatetheclaimsmadebytheauthors,
namely ERM, Group-DRO, and CGD. We closely follow the notation used in the paper,
| whichdefinesX,Y |     | asthefeatureandlabelspaces,andG |     |     |     |     |     |     |     |     |

asasetofnon‐overlappingk
groups,eachcomposedofn observationsdistributedasP (X,Y). Foreachgroupi,we
|         |     |               | i       |               |     |        | i   |                |        |     |

| defineℓ | (θ) | = E           | L(x,y;f | )asgrouploss, |     | wheref |     |                | θ      |     |
|         | i   | (x,y)∼Pi(X,Y) |         | θ             |     |        | θ   | isaclassifier, | arethe |     |
modelparametersandLisanappropriateloss.
ThebaselinealgorithmisERM,which
minimizestheexpectedtrainingloss.
|     |     |     | θt+1 =argmin{E |     |          | [ℓ(θt)]}, |     |     |     |     |

|     |     |     | ERM            |     | (x,y)∼Pˆ |           |     |     |     | (1) |
θ
wherePˆ istheempiricaldistributionoverthetrainingdataandℓthelossforthewhole
trainingsetwithoutconsideringthegroups. TheERMformulationimplicitlyassignsa
higherweighttomajoritygroups. Italsoencouragesthemodeltoexploitspuriouscorrelationsthatworkwellforpredictingthelabelofmajoritygroups,achievinghighaverage
testaccuraciesattheexpenseofminoritygroups.Toovercomethisissue,Sagawaetal.[1]
proposedGroup-DRO,which,ateachstep,trainsonthegroupwiththeworsttraining
lossj∗
:
∗
|     |     | j =arg | m axℓ (θ) |     | ⇒   | t+ 1 =θt−η∇ℓ |     | j∗(θt) |     |     |

|     |     |        | i         |     |     | θ            |     |        |     | (2) |
|     |     |        | i∈ G      |     |     | G -D RO      |     |        |     |     |
While Group-DRO has a better performance on minority groups when compared to
ERM, it may overfit on them, jeopardizing the average loss over all groups. To solve
thisproblem,Piratla,Netrapalli,andSarawagi[3]
proposedCommonGradientDescent
(CGD),which,ateachstep,picksthegroupwhichminimizestheoveralllossacrossall
groupsasfollows:
|     |            | ∑        |     |        |     |              |     | ∑      |         |     |

| j   | ∗ =argmin{ | ℓ [θt−η∇ | ℓ   | (θt)]} |     | θ t+ 1 =θt−η |     | α t+1∇ | ℓ (θt), |     |
|     |            | i        | θ j |        | ⇒   |              |     | i      | θ i     | (3) |
|     |            |          |     |        |     | C GD         |     |        |         |     |
|     | j          | i        |     |        |     |              |     | i      |         |     |
whereα istheweightforgroupi. Amorethoroughexplanationofthisformulaandthe
i
CGDalgorithmisprovidedintheoriginalpaper. Thealgorithmsabovewereevaluated
onvariousmodel/datasetcombinationsasshowninTable9ofAppendixA.
1https://github.com/vihari/CGD
| ReScienceC9.2(#23)–Simoncinietal.2023 |     |     |     |     |     |     |     |     |     | 3   |

### 3.2 Datasets
Thepaperusestwogroupsofdatasets: onecomposedof2synthetictoydatasetstocomparethequalitativeperformanceofCGDagainstGroup-DRO,andasecondoneconsistingof2syntheticdatasetsandsixreal‐worlddatasets.
QualitativeEvaluation—ThequalitativeperformanceofCGDwasevaluatedontwotoydatasets:
a2‐featuredatasetsampledfromastandardnormaldistribution,andMNIST.Onthese
datasetsweappliedthreemulti‐groupsetups:
• LabelNoiseSetup‐where20%ofthefirstgrouplabelswereflippedforSimpleand
50%forMNIST.
• RotationSetup‐wherelabels(ortheimagesforMNIST)wererotatedby30degrees
pergroup,suchthatthedistancesfromthefirstandthirdgrouptothesecondis
thesame.
• SpuriousSetup‐whereeachsamplehasathirdfeature(thedigitcolorforMNIST),
whichhasan80%correlationwiththelabel.
QuantitativeEvaluation—Forthequantitativeevaluationof thealgorithm, weusedeight
datasetscategorizedintosyntheticorreal‐worldandbasedonwhethertheyincludespuriouscorrelations(non‐WILDS)orsub‐populationshift(WILDS).ThedatasetsaresummarizedinTable1.
| Dataset(non‐WILDS) | Type Classes       | SpuriousVariable      |

| CMNIST[6]          | S Digits           | DigitColor            |
| WaterBirds[1]      | S Water/landbird   | Background            |
| CelebA[7]          | R Blond/Non‐Blond  | Gender                |
| MultiNLI[4]        | R NLIa             | NegationWords         |
| Dataset(WILDS)     | Type Classes       | Groups                |
| Camelyon17[8]      | R Tumor/Non‐Tumor  | SourceHospital        |
| PovertyMap[9]      | R Wealth‐Index     | Country&Rural/Urban   |
| FMoW[10]           | R Building/Landuse | Year&Region           |
| CivilComments[11]  | R Toxic/Non‐Toxic  | MentionedDemographics |
a
NaturalLanguageInference
Table1. Summaryofthedatasetsusedforthequantitativeevaluation. Datasetsarecategorizedintosynthetic(S)orreal(R)andbasedonwhethertheyincludespuriouscorrelations
(non‐WILDS)or sub‐populationshift (WILDS). The rightmost column showsthe spurious
variableforthenon‐WILDSdatasetandthegroupsinwhichsamplesarepartitionedforthe
WILDSdatasets.MultiNLIandCivilCommentsaretextdatasets,whiletheothersareimage
datasets.
### 3.3 Hyperparameters
QualitativeEvaluation—themodelsforthequalitativeevaluationaretrainedusingSGDfor
400epochs,withalearningrateof0.1asindicatedinthepaper. Thebatchsizeandthe
weightdecayarenotspecified,andweusedrespectively128and0.01,thelatterofwhich
wasselectedfromtheset{1,0.1,0.01,0.001,0}bymanuallyinspectingtheCGDtraining
weights(α)plotsandchoosingthevaluewhichproducesaplotresemblingFigure1of
theoriginalpaper.
ReScienceC9.2(#23)–Simoncinietal.2023 4


| Dataset       | lr WeightDecay | Epochs | BatchSize | C StepSize |      |

| CMNIST        | 1e‐3           | 1e‐1   | 10        | 32 0       | 0.05 |
| WaterBirds    | 1e‐3           | 1e‐1   | 300       | 128 2      | 0.05 |
| CelebA        | 1e‐3           | 1e‐4   | 10        | 8 2        | 0.05 |
| MultiNLI      | 1e‐3           | 1e‐4   | 3         | 8 2        | 0.05 |
| CivilComments | 1e‐5           | 1e‐2   | 5         | 16 0       | 0.05 |
| PovertyMap    | 1e‐3           | 0      | 10        | 64 0       | 0.05 |
| FMoW          | 1e‐4           | 0      | 5         | 32 0       | 0.2  |
| Camelyon17    | 1e‐3           | 1e‐2   | 5         | 32 0       | 0.05 |
Table2.Hyperparametersusedforeachdatasetandallalgorithmsinourexperiments.Candstep
sizeareonlyrelevantforCGD.IfahyperparameterisnotincludedthenthedefaultvalueinWILDS
shouldbeassumed.
QuantitativeEvaluation—followingPiratla,Netrapalli,andSarawagi[3] themodelsforthe
qualitativeevaluationaretrainedusingSGDwithamomentumof0.9,exceptforPoverFortheWILDSdatasets,wefollowedthesetupinKohetal.[2],
tyMap,whichusesAdam.
withsomeexceptionsforthenumberofepochsandthebatchsizeduetocomputational
| CGD, |     |     | C   |     |     |

limitations. For the group‐adjustment parameter is 0 following Piratla, Netrapalli, andSarawagi[3] andthestepsizeη isselectedfromtheWILDSleaderboard2. As
forthenon‐WILDSdatasets,theauthorsranagridsearchoverthelearningrate,weight
decay, batchsize, andC (setto0forCMNIST),butonlyprovidedthehyperparameter
rangesandnottheselectedvalues. Duetocomputationalconstraints,weusedthevaluesprovidedintheGroup-DROpaper[1],butifthevaluewasoutoftherangedefinedby
theauthors,weselectedtheclosestoneinthatrange. ForCGD,Cwassetto2according
toSagawaetal.[1],andηaccordingtotheWILDSleaderboard. ThehyperparametervaluesaresummarizedinTable2. ThesensitivityofCGDwithregardstohyperparameters
C andηisexploredinAppendixC.
### 3.4 Experimentalsetupandcode
To make our study reproducible, we provide a guide on setting up a conda environmentwithalltherequireddependenciesinourGitHubrepository. Theinstructionsare
foraGoogleComputeEngine(GCE)virtualmachinewithpreinstalledNVIDIAdrivers.
However,theyarehighlyflexibleandshouldworkonanymachinewithminortweaks
(namely the CUDA version). We also provide a modified version of the WILDS repositorywhichcanruntheCGDexperimentsoutofthebox. Thecompleteinstructionson
reproducingourexperimentsareavailableintheREADME.mdfileoftherepository.
### 3.5 Computationalrequirements
Theexperimentswereexecutedonthreemachines,whosehardwareconfigurationsare
listedinTable3. Theestimatedruntimeofeachmodel/datasetpaironaGoogleComputeEngineVirtualMachine(GCE)islistedinTable4,andeachpairwasrunwiththree
differentseeds. Thereforethetotalcomputationtimewasapproximately440hours.
## 4 Results
### 4.1 Resultsreproducingoriginalpaper
QualitativeEvaluation—We replicated the qualitative comparison in Section 4 of the paperforboththeSimpleandMNISTdatasets. FortheSimpledataset,CGDoutperforms
2https://wilds.stanford.edu/leaderboard/
| ReScienceC9.2(#23)–Simoncinietal.2023 |     |     |     |     | 5   |

| Machine | CPU            |     | RAM(GB) |     | GraphicsCard    |     | VRAM(GB) |     |

| GCEVM   | IntelXeon8173M |     |         | 16  | TeslaT4         |     |          | 16  |
| LaptopA | AMDRyzen75800h |     |         | 16  | RTX3050TiMobile |     |          | 4   |
| LaptopB | Inteli5‐9300H  |     |         | 16  | GTX1660TiMobile |     |          | 6   |
Table3.Hardwareconfigurationofthemachinesusedtorunexperiments.
| Algorithm     |     | CMNIST        |     | WaterBirds | CelebA |      | MultiNLI   |      |

| ERM,Group-DRO |     |               | 1h  |            | 7h     | 8h   |            | 4h   |
| CGD           |     |               | 2h  |            | 15h    | 31h  |            | 4.5h |
| Algorithm     |     | CivilComments |     | PovertyMap |        | FMoW | Camelyon17 |      |
| ERM,Group-DRO |     |               | 16h |            | 0.3h   | 2h   |            | 3h   |
| CGD           |     |               | 17h |            | 8h     | 20h  |            | 10h  |
Table4.EstimatedruntimeinhoursofeachmodelanddatasetcombinationonaGoogleCompute
EngineVirtualMachinewithaTeslaT4GPU.Theruntimesof ERMandGroup-DROaresimilar
foralldatasets.
Group-DRO,albeitwithasmallergapthantheresultsofthepaper, ascanbeseenin
AninspectionofthegroupweightsαoverepochsasshowninFigure1reveals
Table5.
theCGDeffectivelybehavesasdescribedinthepaper:
• LabelNoisesetup‐CGDavoidstrainingonlyonthenoisymajority.
• RotationSetup‐CGD,onaverage,focusesonthecentergroup,whichhastheoptimalclassifier. However,thisselectionvariesfromseedtoseed(AppendixB).
• SpuriousSetup‐CGDcorrectlyidentifiesthecleanmajorityandassignsitamuch
strongerweightthaninthepaper.
FortheMNISTdataset,wewerenotabletoreplicatethepaperresults.AsshowninTable
6,weachievedsimilaraverageandworst‐groupaccuraciesbetweenCGDandGroup-DRO,
exceptfortheRotationsetup,whereGroup-DROfailedtoachievereasonableaccuracy.
WesuspecttheremightbeanissuewiththeexperimentalsetupforGroup-DRObecause
theoriginalpaperachievedsignificantlybetterresults.
Figure1.ThecomparisonofgroupweightsαforGroup-DRO(top)andCGD(bottom)fortheSimple
datasetsetups:labelnoise,rotationandspurious.
| ReScienceC9.2(#23)–Simoncinietal.2023 |     |     |     |     |     |     |     | 6   |

Algorithm NoisySimple RotationSimple SpuriousSimple
G-DRO 0.26(0.02) 0.47(0.04) 0.42(0.03)
CGD 0.22(0.01) 0.46(0.06) 0.32(0.01)
Table5. Worstgrouplossesonthetestsplitofthesimpledataset,averagedoversixseeds. The
standarddeviationisshowninparentheses.
Algorithm Metric NoisyMNIST RotationMNIST SpuriousMNIST
G-DRO Avg. Acc. 77.36(10.02) 30.58(3.82) 92.47(2.63)
W.g. Acc. 77.25(9.95) 28.02(4.42) 91.75(2.68)
CGD Avg. Acc. 76.35(7.8) 92.51(1.78) 92.51(1.78)
W.g. Acc. 76.24(7.81) 91.7(2.35) 91.7(2.35)
Table6.AverageandworstgroupaccuraciesonthetestsplitofMNIST,averagedoverthreeseeds.
Thestandarddeviationisshowninparentheses.
QuantitativeEvaluation—Wereproducedtheexperimentsonthenon‐WILDSandWILDS
datasetsandcomparedtheperformanceof CGDagainstERMandGroup-DRO.Table7
summarizes the results on the four non‐WILDS datasets. CGD outperforms the other
algorithms on the synthetic datasets with spurious correlations (CMNIST and WaterBirds),butfailstoimproveinthereal‐worlddatasetswithspuriouscorrelations(CelebA
andMultiNLI)overERMandGroup-DRO.AsfortheWILDSdatasetswhoseresultsare
shown in Table 8, CGD is the best algorithm only on Camelyon17 (albeit with a larger
standard deviation than ERM) and on the in‐domain evaluation of PovertyMap, while
ERMhasasignificantadvantageontheout‐of‐domainevaluationagainstCGD,showing
a larger gap than what claimed by the paper. Overall, the results are in line with the
paper,whichshowsthatCGDisbetterinsomesetupsandachievescomparableperformancesinothers,butitssuperiorityisnotclear.
CMNIST WaterBirds
Algorithm Avg. Acc. W.g. Acc. Avg. Acc. W.g. Acc.
ERM 55.3(2.23) 10.5(4.47) 97.1(0.03) 52.2(1.18)
G-DRO 97.6(0.49) 96.8(0.69) 97.3(0.06) 71.7(0.55)
CGD 98.0(0.34) 97.0(0.4) 97.3(0.13) 73.2(0.39)
CelebA MultiNLI
Algorithm Avg. Acc. W.g. Acc. Avg. Acc. W.g. Acc.
ERM 96.0(0.12) 36.3(6.04) 62.2(11.27) 16.1(18.59)
G-DRO 94.9(0.11) 59.1(1.72) 49.9(0.76) 27.5(2.62)
CGD 95.0(0.13) 59.8(8.72) 50.2(1.01) 27.1(1.36)
Table7.Averageandworst‐groupaccuraciesonthetestsplitsofthenon‐WILDSdatasets.Inparenthesesarethestandarddeviations.
ReScienceC9.2(#23)–Simoncinietal.2023 7


Camelyon17 PovertyMap FMoW CivilComments
Avg. Acc. W.r. PearsonR W.r. Acc. W.g. Acc.
Algorithm OOD ID OOD OOD ID
ERM 70.3(6.4) 0.57(0.07) 0.45(0.06) 32.3(1.2) 56.0(3.6)
G-DRO 68.4(7.3) 0.54(0.11) 0.39(0.06) 30.8(0.8) 70.0(2.0)
CGD 70.4(7.56) 0.63(0.03) 0.38(0.07) 29.8(1.46) 69.7(1.09)
Table8. ResultsfordifferentmetricsonthetestsplitsoftheWILDSdatasets. Inparenthesesare
thestandarddeviations.w.r.andw.gstandforworstregionandworstgroupaccuracy.Thevalues
weretakenfromtheoriginalpaperwiththeexceptionofCGDwhichwetrainedourselves.
### 4.2 Resultsbeyondoriginalpaper
The paper does not discuss the runtime of the algorithms, which we documented in
Table 4. We find that CGD is often 2 to 26 times slower than the other algorithms dependingonthedataset. AsseeninTable4,theruntimeincreasevariesacrossdatasets:
forWaterBirds,wehaveanincreaseof50%,whileforPovertyMap,theincreaseisover
2000%. Thecomputationofthegradientsforeachgroupateachtrainingstep(Equation
3)mightbeonepossiblereason. Thishypothesisissupportedbythefactthatdatasets
withmanygroups,suchasPovertyMap,FMoW,andCamelyon,with13,16,and5groups
respectively, had the largest increase in training time (the other datasets do not have
morethanfourgroups). CelebAisanexception,buttheruntimeincreasemaybedue
tothesmallbatchsize(8). Inviewoftheabove,weconcludedthatthesmallgainsin
accuracymaynotjustifytheincreasedtrainingtime. Moreover,theauthorsmathematicallyprovedthatCGDisasoundoptimizationalgorithmasitdecreasesthemacro/groupaveragelossmonotonically. Wetestthisempiricallybyplottingthelosscurvesforthe
non‐WILDS datasets (except for MultiNLI, since it only has 3 epochs) in Figure 2 for
Group-DRO and CGD. Weobservethat the validationloss curveis notmonotonic. Instead,itfluctuatesandseemstoincreaseforalldatasets. Thisisparticularlyevidentin
WaterBirds. Onereasonforthisbehaviormaybetheuseofbatchestotoapproximate
thegradients,whereastheproofassumesthatthewholedatasetisusedateachtraining
step. Duetotheselimitations,wecannotconfirmordisprovetheclaim,sowecompare
therelativemonotonicityandstabilitybetweenCGDandGroup-DRO.ForCMNIST,both
showsimilardegreesofmonotonicity. OnWaterBirds,CGDhasamorestabletraining
than Group-DRO, whose validation loss has large fluctuations between epochs. This
maybeasideeffectoffocusingonthegroupwiththelargesttraininglossasidentified
by [3]. With regards to CelebA, the validation loss of CGD increases whereas the loss
of Group-DRO appears to be decreasing. In conclusion, we cannot clearly show that
thelossof CGDdecreasesmonotonically,butourfindingssuggestthatitismorestable
thanGroup-DRO.Futureresearchmayfurtherinvestigatethisclaimbyrunningexperimentsthatcomeclosertotheassumptionsoftheauthors,namelyabiggerbatchsize
andmoreepochs.
Figure2.LosscurvesforCGDandGroup-DROonthreenon‐WILDSdatasets.
ReScienceC9.2(#23)–Simoncinietal.2023 8


## 5 Discussion
Overall, the majority of the claims in the paper were reproducible. CGD indeed performedcomparablyorbetterthanERMandGroup-DROdependingonthedataset. However,theincreasedruntimeofCGDmightoutweightheminoraccuracygain. Theclaim
oftheauthorsaboutthemonotonicityofCGDcouldnotbereproducedempiricallyina
reliableway,andfurtherresearchisneeded. Lastly,CGDappearstohaveamorestable
trainingincomparisontoGroup-DRO.
### 5.1 Whatwaseasy
The methods used in the paper and the results were described clearly and intuitively.
Moreover,thecodeforCGDwaspublishedbytheauthorsalongsideclearinstructionson
integratingitintotheWILDSframework. Finally,theframeworkchosenbytheauthors
ismodular,andadditionaldatasetsandalgorithmscouldbeeasilyintegrated.
### 5.2 Whatwasdifficult
• Resources: Model training required a massive amount of GPU time due to the
datasetsizeandthesheernumberofexperiments.
• Code: TheC parameterfortheWILDSimplementationof Group-DROcouldnot
belocatedinthecode,sowecouldnotselectavalueforit. Wesuspectthatthere
mightbeaninconsistencybetweenthetheoryandthecode.Eventhoughthecode
forCGDandWILDSwasavailable,wecouldnotrunexperimentsoutofthebox:the
CDGcodehadtobeupdatedtoworkwiththelatestversionofWILDSandrequired
somemodifications. Moreover,thedatasetcodeforMultiNLIwasmissing,sowe
implementeditfollowing[1]andtheadviceoftheauthors.
• Hyperparameters: Collectingthecorrecthyperparametervalueswaschallenging
becausethepaperonlyprovidedarange,andthereweremultipleconflictingsources:
thepaper,therepository,andtheWILDSleaderboard(thelattersuggestedbythe
authors in our correspondence). Moreover, some values did not lead to the expectedaccuracyaccordingtothepaper,sowehadtoexperimentwithadditional
values, e.g., the weight decay for CMNIST and Waterbirds. Finally, The best valuesfortheCGDstepsizeηintheWILDSleaderboard(0.05and0.2)werenotinthe
rangedescribedinthepaper.
### 5.3 Communicationwithoriginalauthors
We reached out to the original authors to obtain more information about the chosen
hyperparametervalues. Theypromptlyreplied,specifyingthatfortheWILDSdatasets,
thehyperparametersareasconfiguredbydefaultinWILDS1.2.2. Fortheiralgorithm,
CGD, they informed us that its hyperparameters could be found in the WILDS leaderboard. Inaddition,theygaveushelpfulinformationaboutsomepartsoftheircodethat
weremissing,suchastheMultiNLIdataset.
ReScienceC9.2(#23)–Simoncinietal.2023 9


References
1. S.Sagawa,P.W.Koh,T.B.Hashimoto,andP.Liang.“Distributionallyrobustneuralnetworksforgroupshifts:
Ontheimportanceofregularizationforworst-casegeneralization.”In:ProceedingsoftheInternationalCon-
ferenceonLearningRepresentations(2020).
2. P.W.Koh,S.Sagawa,H.Marklund,S.M.Xie,M.Zhang,A.Balsubramani,W.Hu,M.Yasunaga,R.L.Phillips,
I.Gao,etal.“Wilds:Abenchmarkofin-the-wilddistributionshifts.”In:ProceedingsoftheInternationalCon-
ferenceonMachineLearning(2021).
3. V.Piratla,P.Netrapalli,andS.Sarawagi.“FocusontheCommonGood:GroupDistributionalRobustnessFol-
lows.”In:ProceedingsoftheInternationalConferenceonLearningRepresentations(2022).
4. A.Williams,N.Nangia,andS.R.Bowman.“Abroad-coveragechallengecorpusforsentenceunderstanding
throughinference.”In:ProceedingsoftheConferenceoftheNorthAmericanChapteroftheAssociationfor
ComputationalLinguistics:HumanLanguageTechnologies(2018).
5. S.Sagawa,P.W.Koh,T.Lee,I.Gao,S.M.Xie,K.Shen,A.Kumar,W.Hu,M.Yasunaga,H.Marklund,etal.
“Extendingthewildsbenchmarkforunsupervisedadaptation.”In:arXivpreprintarXiv:2112.05090(2021).
6. I.GulrajaniandD.Lopez-Paz.“Insearchoflostdomaingeneralization.”In:ProceedingsoftheInternational
ConferenceonLearningRepresentations(2021).
7. Z.Liu,P.Luo,X.Wang,andX.Tang.“Deeplearningfaceattributesinthewild.”In:ProceedingsoftheIEEE
internationalconferenceoncomputervision(2015).
8. P.Bandi,O.Geessink,Q.Manson,M.VanDijk,M.Balkenhol,M.Hermsen,B.E.Bejnordi,B.Lee,K.Paeng,A.
Zhong,etal.“Fromdetectionofindividualmetastasestoclassificationoflymphnodestatusatthepatient
level:thecamelyon17challenge.”In:IEEETransactionsonMedicalImaging(2019).
9. C.Yeh,A.Perez,A.Driscoll,G.Azzari,Z.Tang,D.Lobell,S.Ermon,andM.Burke.“Usingpubliclyavailable
satelliteimageryanddeeplearningtounderstandeconomicwell-beinginAfrica.”In:Naturecommunications
11.1(2020),p.2583.
10. G.Christie,N.Fendley,J.Wilson,andR.Mukherjee.“Functionalmapoftheworld.”In:(2018).
11. D.Borkan,L.Dixon,J.Sorensen,N.Thain,andL.Vasserman.“Nuancedmetricsformeasuringunintendedbias
withrealdatafortextclassification.”In:Companionproceedingsofthe2019worldwidewebconference.
2019,pp.491–500.
A Model Specifications
The optimization algorithms evaluated in this study were applied on several models/‐
datasetcombinations,asshowninTable9. Adifferentmodelwasusedforeachdataset,
dependingonthetask.
| Dataset       | Model                  | Pretrained | Parameters |

| Simple        | LinearBinaryClassifier | False      | 6          |
| MNIST         | ResNet18               | False      | 11M        |
| CMNIST        | ResNet18               | True       | 11M        |
| WaterBirds    | ResNet50               | True       | 25M        |
| CelebA        | ResNet50               | True       | 25M        |
| MultiNLI      | DistilBERT‐uncased     | True       | 66M        |
| CivilComments | DistilBERT‐uncased     | True       | 66M        |
| PovertyMap    | Resnet18               | True       | 11M        |
MS
| FMoW       | DenseNet121 | True | 76M |

| Camelyon17 | DenseNet121 | True | 76M |
Table9.Thedatasets,alongsidethemodelselection,iftheyuseornotpretrainedweightsandthe
| numberparameters.Resnet18 | referstoResnet18Multi‐Spectral. |     |     |

MS
ReScienceC9.2(#23)–Simoncinietal.2023 10


B Training Group Selection
EventhoughCGDisgenerallyconsistentwiththegroupchoice,intheSimple‐Rotation
setup,thegroupthealgorithmfocusesonvaries,asshowninFigure3plots. Whilefor
seed3CGDcorrectlyidentifiesthecentergroupforseeds13and42, itfocusesonthe
leftgroup. Incomparison,Group‐DROshowsamoreconsistentgroupchoice.
Figure3.Group-DROandCGDgroupweightsαforseeds3,13,and42overepochsfortheSimple
datasetandtheRotationsetup.WhileGroup-DROshowsaconsistentbehaviorCGDeitherfocuses
onthecentergroupasexpected(seed3)oronamixofthecenterandleftgroups
C Hyperparameter Sensitivity
We evaluated the hyperparameter sensitivity for CGD with respect to the group adjustmentparameterCandthestepsizeη,usingthevaluesinTable2fortheotherhyperparameters. Whileamorethroughoutevaluationonreal‐worlddatasetsisrecommended,
theevaluationwasconductedusingCMNIST,whichallowedustotestmultiplevalues
andaveragetheresultsoverthreeseedswithlimitedcompute.
Figure4.TheaverageandworstgroupaccuraciesobtainedbyCGDonCMNISTwithrespecttothe
groupadjustmentparameterC.Theresultsareaveragedoverthreeseeds.
ReScienceC9.2(#23)–Simoncinietal.2023 11


|     |     |     | C   |     | η 0.05 |     |

To evaluate the effect of we fixed the step size to and trained the model us‐
|     | ∈ {0,1,2,5,10,20}. |     |     |     |     |     |

ing C By observing the plots in Figure 4 we can notice that large
increasesofC leadtoadegradationoftrainingperformancefortheaverageandworst
groupaccuracybut,interestingly,thiseffectisnotreplicatedinthevalidationset,which
insteadrevealsthatbothsmallandlargevaluesofCcauseinstabilitiesinthevalidation
C ∈ {5,10}
| metrics. | This is | confirmed | by the | test set results | in Table 10, | for which |

performbestwithregardstotheaverageandworstgroupaccuracies.
|     |           |       |           |      | C Avg. Acc. | W.g. Acc. |

|     | StepSizeη | Avg.  | Acc. W.g. | Acc. |             |           |
|     |           |       |           |      | 0 0.974     | 0.964     |
|     | 0.001     | 0.973 | 0.968     |      |             |           |
|     |           |       |           |      | 1 0.974     | 0.962     |
|     | 0.01      | 0.978 | 0.973     |      |             |           |
|     |           |       |           |      | 2 0.976     | 0.963     |
|     | 0.05      | 0.976 | 0.963     |      |             |           |
|     |           |       |           |      | 5 0.975     | 0.972     |
|     | 0.1       | 0.980 | 0.972     |      |             |           |
|     |           |       |           |      | 10 0.976    | 0.972     |
|     | 1         | 0.978 | 0.971     |      |             |           |
|     |           |       |           |      | 20 0.974    | 0.966     |
Table10.TheaverageandworstgroupaccuraciesforthetestsetofCMNISTobtainedbyCGDwith
respecttothegroupadjustmentparameterCandthestepsizeη
|     |     |     |     | η C | = 2 |     |

As for the step size hyperparameter we fixed and evaluted the performance
CGDovertheset{1,0.1,0.05,0.01,0.001}.
| of  |     |     |     | Withregardstothetrainingperformance |     |     |

thedifferentvaluesperformedsimilarly,butascanbeseeninfigure5thevalidationset
accuracyshowsthatsmallervaluesresultinamoreunstabletraining,and,asconfirmed
| bythetestsetmetricsinTable10,η |     |     |     | ∈{0.1,1}workbestforthisdataset. |     |     |

Figure5.TheaverageandworstgroupaccuraciesobtainedbyCGDonCMNISTwithrespecttothe
stepsizeparameterη.Theresultsareaveragedoverthreeseeds.
ReScienceC9.2(#23)–Simoncinietal.2023 12

---
**Source PDF:** `1addad35ab04.pdf` (2023_27_article.pdf)  
**URL:** https://zenodo.org/record/8173707/files/article.pdf
