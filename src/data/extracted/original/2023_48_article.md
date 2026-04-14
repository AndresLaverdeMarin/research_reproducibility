Compositional Generalization and Natural Language Variation:
Can a Semantic Parsing Approach Handle Both?
PeterShaw Ming-WeiChang PanupongPasupat KristinaToutanova
GoogleResearch
{petershaw,mingweichang,ppasupat,kristout}@google.com
Abstract PREDOMINANTAPPROACHES
Sequence-to-sequence models excel at han-
Specialized
dlingnaturallanguagevariation,buthavebeen
architectures Under-explored
shown to struggle with out-of-distribution withstrong
compositional generalization. This has mo- compositionalbias
tivated new specialized architectures with
stronger compositional biases, but most of General-purpose
theseapproacheshaveonlybeenevaluatedon pre-trainedmodels
(e.g.seq2seq)
synthetically-generateddatasets,whicharenot
representativeofnaturallanguagevariation.In SYNTHETIC NON-SYNTHETIC
this work we ask: can we develop a semantic
NATURALLANGUAGEVARIATION
parsingapproachthathandlesbothnaturallan-
guagevariationandcompositionalgeneraliza-
tion? To better assess this capability, we pro-
posenewtrainandtestsplitsofnon-synthetic
datasets. We demonstrate that strong exist-
ing approaches do not perform well across a
broad set of evaluations. We also propose
NQG-T5,ahybridmodelthatcombinesahigh-
precisiongrammar-basedapproachwithapre-
trainedsequence-to-sequencemodel.Itoutper-
formsexistingapproachesacrossseveralcom-
positional generalization challenges on non-
synthetic data, while also being competitive
with the state-of-the-art on standard evalua-
tions.Whilestillfarfromsolvingthisproblem,
ourstudyhighlightstheimportanceofdiverse
evaluationsandtheopenchallengeofhandling
bothcompositionalgeneralizationandnatural
languagevariationinsemanticparsing.
## 1 Introduction
Sequence-to-sequence(seq2seq)modelshavebeen
widely used in semantic parsing (Dong and Lap-
ata, 2016; Jia and Liang, 2016) and excel at han-
dling the natural language variation1 of human-
generated queries. However, evaluations on syn-
thetic2 tasks such as SCAN (Lake and Baroni,
1Weusethetermnaturallanguagevariationinabroad
sensetorefertothemanydifferentwayshumanscanexpress
thesamemeaninginnaturallanguage,includingdifferences
inwordchoiceandsyntacticconstructions.
2Wemakeacoarsedistinctionbetweensyntheticdatasets,
wherenaturallanguageutterancesaregeneratedbyaprogram,

Proceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguistics
andthe11thInternationalJointConferenceonNaturalLanguageProcessing,pages922–938
August1–6,2021.©2021AssociationforComputationalLinguistics
LANOITISOPMOC NOITAZILARENEG
Figure 1: We study whether a semantic parsing ap-
proach can handle both out-of-distribution composi-
tional generalization and natural language variation.
Existing approaches are commonly evaluated across
onlyonedimension.
2018)haveshownthatseq2seqmodelsoftengener-
alizepoorlytoout-of-distributioncompositionalut-
terances,suchas“jumptwice”whenonly“jump”,
“walk”,and“walktwice”areseenduringtraining.
Thisabilitytogeneralizetonovelcombinationsof
theelementsobservedduringtrainingisreferredto
ascompositionalgeneralization.
This has motivated many specialized architec-
turesthatimprovepeformanceonSCAN(Lietal.,
2019;Russinetal.,2019;Gordonetal.,2019;Lake,
2019;Liuetal.,2020;Nyeetal.,2020;Chenetal.,
2020). However,mostapproacheshaveonlybeen
evaluated on synthetic datasets. While synthetic
datasetsenableprecise,interpretableevaluationof
specific phenomena, they are less representative
ofthenaturallanguagevariationthatareal-world
semanticparsingsystemmusthandle.
Inthispaper,weask: canwedevelopasemantic
parsing approach that handles both natural lan-
guagevariationandcompositionalgeneralization?
andnon-syntheticdatasets,wherenaturallanguageutterances
arecollectedfromhumans.

Surprisingly,thisquestionisunderstudied. Asvisu- TRAINANDTESTSPLITS
alizedinFigure1,mostpriorworkevaluateseither
MCD
| out-of-distributioncompositionalgeneralizationon |     |     |     |     |     |     |     |     |     |     | TMCD |     |     |

(Keysersetal.,2020)
NOITAZILARENEG
syntheticdatasets,orin-distributionperformance LANOITISOPMOC AddPrimitive Template
|                          |     |     |                      |     |     |     |     | (LakeandBaroni,2018) |        |     | (Finegan-Dollaketal.,2018) |     |     |

| onnon-syntheticdatasets. |     |     | Notably,designingap- |     |     |     |     |                      |        |     |                            |     |     |
|                          |     |     |                      |     |     |     |     |                      | Length |     | Length                     |     |     |
proachesthatcanhandlebothcompositionalgen-
| eralization   | and | the natural | language      |     | variation    | of  |     |     |     |     |     |     |     |

| non-synthetic |     | datasets    | is difficult. |     | For example, |     |     |     |     |     |     |     |     |
Random
largepre-trainedseq2seqmodelsthatperformwell
|     |     |     |     |     |     |     |     | SYNTHETIC |     |     | NON-SYNTHETIC |     |     |

onin-distributionevaluationsdonotaddressmost
NATURALLANGUAGEVARIATION
ofthecompositionalgeneralizationchallengespro-
| posedin | SCAN | (Furreretal.,2020). |     |     |     |     |           |             |          |     |         |            |     |

|         |      |                     |     |     |     |     | Figure 2: | We evaluate | semantic |     | parsing | approaches |     |
Ourresearchquestionhastwoimportantmotiva-
|     |     |     |     |     |     |     | across a | diverse set | of evaluations |     | focused | on  | natu- |

tions. First,humanshavebeenshowntobeadept rallanguagevariation,compositionalgeneralization,or
|                                        |     |     |     |     |         |     | both. We | add TMCD | splits | to  | complement | existing |     |

| compositionallearners(Lakeetal.,2019). |     |     |     |     | Several |     |          |          |        |     |            |          |     |
authors have argued that a greater focus on com- evaluations. Orderingwithineachcellisarbitrary.
| positional      | generalization |                | is an | important | path | to    |         |         |        |     |                  |     |      |

| more human-like |                | generalization |       | and       | NLU  | (Lake |         |         |        |     |                  |     |      |
|                 |                |                |       |           |      |       | DER (Yu | et al., | 2018). | Our | results indicate |     | that |
et al., 2017; Battaglia et al., 2018). Second, it NQG-T5isastrongbaselineforourchallengeof
ispracticallyimportanttoassessperformanceon
developingapproachesthatperformwellacrossa
| non-synthetic |     | data and | out-of-distribution |     |     | exam- |     |     |     |     |     |     |     |

diversesetofevaluationsfocusingoneithernatural
| ples, as | random | train | and test | splits | can overesti- |     |     |     |     |     |     |     |     |

languagevariation,compositionalgeneralization,
matereal-worldperformanceandmissimportant
|                                |               |     |      |                 |          |     | or both.    | Comparing  | five | approaches    |             | across   | eight |

| errorcases(Ribeiroetal.,2020). |               |     |      | Therefore,weare |          |     |             |            |      |               |             |          |       |
|                                |               |     |      |                 |          |     | evaluations | on SCAN    |      | and GEOQUERY, |             | its      | aver- |
| interested                     | in approaches |     | that | do well         | not only | on  |             |            |      |               |             |          |       |
|                                |               |     |      |                 |          |     | age rank    | is 1, with | the  | rank          | of the best | previous |       |
controlledsyntheticchallengesofcompositionality approach(T5)being2.9;performanceisalsocom-
orin-distributionnaturalutterances,butacrossall
|     |     |     |     |     |     |     | petitiveacrossseveralevaluationson |     |     |     | SPIDER. |     |     |

ofthediversesetofevaluationsshowninFigure2.
Whilestillfarfromaffirmativelyansweringour
| Our | contributions |     | are two-fold. |     | First, | on the |     |     |     |     |     |     |     |

researchquestion,ourstudyhighlightstheimpor-
evaluation front, we show that performance on tanceofadiversesetofevaluationsandtheopen
SCAN is not well-correlated with performance challengeofhandlingbothcompositionalgeneral-
izationandnaturallanguagevariation.3
| onnon-synthetictasks. |     |             | Inaddition,strongexisting |        |     |        |     |     |     |     |     |     |     |

| approaches            | do  | not perform | well                      | across | all | evalu- |     |     |     |     |     |     |     |
ations in Figure 2. We also propose new Target 2 BackgroundandRelatedWork
MaximumCompoundDivergence(TMCD)train
|     |     |     |     |     |     |     | In this section, | we  | survey | recent | work | related | to  |

andtestsplits,extendingthemethodologyofKey-
compositionalgeneralizationinsemanticparsing.
sersetal.(2020)tocreatechallengingevaluations
ofcompositionalgeneralizationfornon-synthetic Evaluations Toevaluateamodel’sabilitytogen-
datasets. WeshowthatTMCDsplitscomplement eralizetonovelcompositions, previousworkhas
| existing | evaluations |     | by focusing | on  | different | as- |     |     |     |     |     |     |     |

proposedseveralmethodsforgeneratingtrainand
pectsoftheproblem.
testsplits,aswellasseveralsyntheticdatasets.
Second,onthemodelingfront,weproposeNQG, A widely used synthetic dataset for assessing
asimpleandgeneralgrammar-basedapproachthat compositionalgeneralizationisSCAN(Lakeand
solves SCAN andalsoscalestonaturalutterances, Baroni,2018),whichconsistsofnaturallanguage
obtaininghighprecisionfornon-syntheticdata. In commands(e.g.,“jumptwice”)mappingtoaction
addition, we introduce and evaluate NQG-T5, a sequences(e.g.,“I_JUMP I_JUMP”).Onesplitfor
hybrid model that combines NQG with T5 (Raf- SCANisthelengthsplit,whereexamplesaresepa-
fel et al., 2020), leading to improvements across ratedbylengthsuchthatthetestsetcontainslonger
| several | compositional |     | generalization |     | evaluations |     |      |          |      |        |     |           |     |

|         |               |     |                |     |             |     | 3Our | code and | data | splits | are | available | at  |
whilealsobeingcompetitiveonthestandardsplits
https://github.com/google-research/
ofGEOQUERY(ZelleandMooney,1996)andSPI- language/tree/master/language/nqg.


examplesthanthetrainingset. Anotheristheprim- SCAN-inspired architectures. Oren et al. (2020)
itive split, where a given primitive (e.g., “jump”) andZhengandLapata(2020)alsoexploredcompo-
is seen by itself during training, but the test set sitional generalization on non-synthetic datasets
consists of the primitive recombined with other by focusing on the template splits proposed by
elements observed during training (e.g., “jump Finegan-Dollak et al. (2018), demonstrating im-
twice”). Other synthetic datasets have been de- provementsoverstandardseq2seqmodels.
velopedtoevaluateaspectsofcompositionalgen- Theeffectoflarge-scalepre-trainingoncompo-
eralizationbeyondSCAN,includingNACS(Bast- sitionalgeneralizationabilityhasalsobeenstudied.
ingsetal.,2018),CFQ(Keysersetal.,2020),and Furreretal.(2020)findsthatpre-trainingalonecan-
COGS(KimandLinzen,2020). notsolveseveralcompositionalgeneralizationchal-
InadditiontointroducingtheCFQdataset, Key- lenges,despiteitseffectivenessacrossNLPtasks
sers et al. (2020) propose Maximum Compound suchasquestionanswering(Raffeletal.,2020).
Divergence(MCD)splitsbasedonthenotionofa Whileourworkfocusesonmodelingapproaches,
compounddistribution. Theiralgorithmgenerates compositionaldataaugmentationtechniqueshave
trainandtestsplitsthatmaximizethedivergence alsobeenproposed(JiaandLiang,2016;Andreas,
of their respective compound distributions while 2020). NQG-T5outperformspreviouslyreported
boundingthedivergenceoftheirrespectiveatom resultsforthesemethods,butmorein-depthanaly-
| distributions. | Weextendtheirmethodologytocre- |     |     |     |     | sisisneeded. |     |     |     |     |     |     |     |

atenewTMCDsplitsfornon-syntheticdatasets.
## 3 TargetMaximumCompound
| Another | method | for | generating | train | and test |     |     |     |     |     |     |     |     |

Divergence(TMCD)Splits
| splitsisthetemplate4 |        | split(Finegan-Dollaketal., |     |              |     |     |          |             |     |           |     |               |     |

| 2018).               | Unlike | the aforementioned         |     | evaluations, |     |     |          |             |     |           |     |               |     |
|                      |        |                            |     |              |     | The | existing | evaluations |     | targeting |     | compositional |     |
templatesplitshavebeenappliedtonon-synthetic generalizationfornon-synthetictasksaretemplate
| datasets,   | primarily | for      | text-to-SQL. | In  | template   |                        |        |       |         |                      |         |     |           |

|             |           |          |              |     |            | splitsandlengthsplits. |        |       |         | Hereweproposeanaddi- |         |     |           |
| splits, any | parse     | template | (defined     | as  | the target |                        |        |       |         |                      |         |     |           |
|             |           |          |              |     |            | tional                 | method | which | expands |                      | the set | of  | available |
SQLquerywithentitiesanonymized)appearingin evaluationsbygeneratingdatasplitsthatmaximize
| the training | set | cannot | appear in | the test | set. We |     |     |     |     |     |     |     |     |

compounddivergenceovernon-syntheticdatasets,
analyzeanddiscusstemplatesplitsin§6.1.
|          |                                    |     |     |     |     | termed        | Target | Maximum |                           | Compound |     | Divergence |     |

| Finally, | HerzigandBerant(2019)studiesbiases |     |     |     |     |               |        |         |                           |          |     |            |     |
|          |                                    |     |     |     |     | (TMCD)splits. |        |         | Asweshowin§6,itresultsina |          |     |            |     |
resulting from methods for efficiently collecting generalizationproblemwithdifferentcharacteris-
human-labeleddata,providingfurthermotivation
ticsthatcanbemuchmorechallengingthantem-
forout-of-distributionevaluations.
platesplits,andcontributestothecomprehensive-
nessofevaluation.
| Approaches | Many |     | specialized | architectures |     |     |          |     |        |          |     |         |        |

|            |      |     |             |               |     | In  | standard | MCD | splits | (Keysers |     | et al., | 2020), |
havebeendevelopedtoaddressthecompositional
thenotionofcompoundsrequiresthatbothsource
| generalization | challenges |     | of SCAN. | Several | of  |     |     |     |     |     |     |     |     |

themhaverecentlyreached100%accuracyacross and target are generated by a rule-based proce-
|     |     |     |     |     |     | dure, | and | therefore | cannot | be  | applied | to  | existing |

multipleSCANchallenges(Liuetal.,2020;Nye
non-syntheticdatasetswherenaturallanguageut-
| et al., 2020; | Chen | et al., | 2020). | Similarly | to the |     |     |     |     |     |     |     |     |

NQG-T5approachweproposein§4,allofthese terances are collected from humans. For TMCD,
weproposeanewnotionofcompoundsbasedonly
| models | incorporate | discrete | structure. |     | However, |        |        |                  |     |     |     |          |       |

|        |             |          |            |     |          | on the | target | representations. |     |     | We  | leverage | their |
unlikeNQG-T5,theyhaveonlybeenevaluatedon
knownsyntacticstructuretodefineatomsandcom-
syntheticparsingtasks.
Recently,HerzigandBerant(2020)alsobegins pounds. Forinstance,exampleatomsinFunQLare
|     |     |     |     |     |     | longest |     | and river, |     | and an | example | compound |     |

toaddressourresearchquestion,proposinganap-
|        |          |             |         |      |       | islongest(river). |     |     | Detaileddefinitionsofatoms |     |     |     |     |

| proach | that not | only solves | several | SCAN | chal- |                   |     |     |                            |     |     |     |     |
lengesbutalsoachievesstrongperformanceonthe andcompoundsforeachdatasetwestudycanbe
foundinAppendixB.3.
| standard | and template |     | splits of | the non-synthetic |     |     |     |     |     |     |     |     |     |

Giventhisdefinitionofcompounds,ourdefini-
| dataset                                   | GEOQUERY. | However,theirapproachre- |     |     |     |                            |     |     |     |     |              |     |     |

|                                           |           |                          |     |     |     | tionofcompounddivergence,D |     |     |     |     | ,isthesameas |     |     |
| quiressomemanualtask-specificengineering. |           |                          |     |     | We  |                            |     |     |     |     | C            |     |     |
compare NQG-T5 with this approach and other thatofKeysersetal.(2020). Specifically,
| 4Alsoreferredtoasaquerysplit. |     |     |     |     |     |     | D   | = 1 | − C | (F        | (cid:107)F | ),   |     |

|                               |     |     |     |     |     |     |     | C   |     | 0.1 TRAIN |            | TEST |     |


| whereF | andF  | aretheweightedfrequency |     |     |     |     |     |        |     |     |

|        | TRAIN | TEST                    |     |     |     |     |     |        | no  |     |
|        |       |                         |     |     |     |     | Run | NQGhas |     | Run |
distributions of compounds in the training and Start NQG output?
T5
| test sets, | respectively. | The | Chernoff | coefficient |     |     |     |     |     |     |

(cid:80)
C (P(cid:107)Q) = pαq1−α (Chung et al., 1989) is yes ReturnT5output
| α         |        | k k k |     |     |     |     |     |                 |     |     |

| usedwithα | = 0.1. |       |     |     |     |     |     | ReturnNQGoutput |     |     |
ForTMCD,weconstrainatomdivergencebyre-
quiringthateveryatomappearatleastonceinthe Figure 3: Overview of how predictions are generated
trainingset. Anatomconstraintisdesirablesothat by NQG-T5, a simple yet effective combination of
T5(Raffeletal.,2020)withahigh-precisiongrammar-
themodelknowsthepossibletargetatomstogener-
|     |     |     |     |     |     | basedapproach, |     | NQG. |     |     |

ate. AgreedyalgorithmsimilartotheoneofKey-
sersetal.(2020)isusedtogeneratesplitsthatap-
proximatelymaximizecompounddivergence. First, etal.,2015). NQGcombinesaQCFGinductional-
werandomlysplitthedataset. Then,weswapex- gorithmwithaneuralparsingmodel. Trainingisa
amplesuntiltheatomconstraintissatisfied. Finally, two-stageprocess. First,weemployacompression-
wesequentiallyidentifyexamplepairsthatcanbe based grammar induction technique to construct
swappedbetweenthetrainandtestsetstoincrease ourgrammar. Second,basedontheinducedgram-
compounddivergencewithoutviolatingtheatom mar, we build the NQG semantic parsing model
constraint,breakingwhenaswapcannolongerbe via a discriminative latent variable model, using
| identified. |     |     |     |     |     | apowerfulneuralencodertoscoregrammarrule |     |     |     |     |

applicationsanchoredinthesourcestringx.
| 4 ProposedApproach: |     |     | NQG-T5 |     |     |     |     |     |     |     |

#### 4.1.1 NQGGrammarInduction
We propose NQG-T5, a hybrid semantic parser Grammar Formalism Synchronous context-
| that combines | a                            | grammar-based |     | approach | with a |                                        |     |         |               |          |

|               |                              |               |     |          |        | free grammars                          |     | (SCFGs) | synchronously | generate |
| seq2seqmodel. | Thetwocomponentsaremotivated |               |     |          |        |                                        |     |         |               |          |
|               |                              |               |     |          |        | stringsinbothasourceandtargetlanguage. |     |         |               | Com-     |
bypriorworkfocusingoncompositionalgeneral- paredtorelatedworkbasedonSCFGsformachine
izationandnaturallanguagevariation,respectively,
|        |         |          |                   |     |        | translation | (Chiang, | 2007) | and semantic | parsing, |

| and we | show in | § 5 that | their combination |     | sets a |             |          |       |              |          |
NQGusesaslightlymoregeneralgrammarformal-
strongbaselineforourchallenge. ismthatallowsrepetitionofanon-terminalwiththe
Thegrammar-basedcomponent,NQG,consists sameindexonthetargetside. Therefore,weadopt
| of a discriminative |     | Neural | parsing | model | and a |     |     |     |     |     |

theterminologyofquasi-synchronouscontext-free
| flexible | Quasi-synchronous |     | Grammar |     | induction |          |        |     |                |           |

|          |                   |     |         |     |           | grammars | (Smith | and | Eisner, 2006), | or QCFGs, |
algorithm which can operate over arbitrary pairs to refer to our induced grammar G.5 Our gram-
ofstrings. Likeothergrammar-basedapproaches, marG containsasinglenon-terminalsymbol,NT.
NQGcanfailtoproduceanoutputforcertainin-
Werestrictsourcerulestoonescontainingatmost
puts. As visualized in Figure 3, in cases where 2 non-terminal symbols, and do not allow unary
NQGfailstoproduceanoutput,wereturntheout- productionsassourcerules. Thisenablesefficient
| put from | T5 (Raffel | et  | al., 2020), | a pre-trained |     |     |     |     |     |     |

parsingusinganalgorithmsimilartoCKY(Cocke,
| seq2seqmodel. | Thissimplecombinationcanwork |     |     |     |     |     |     |     |     |     |

1969;Kasami,1965;Younger,1967)thatdoesnot
wellbecauseNQGoftenhashigherprecisionthan requirebinarizationofthegrammar.
T5forcaseswhereitproducesanoutput,especially
inout-of-distributionsettings. Induction Procedure To induce G from the
trainingdata,weproposeaQCFGinductionalgo-
| WetrainNQGandT5separately. |     |     |     | Trainingdata |     |     |     |     |     |     |

rithmthatdoesnotrelyontask-specificheuristics
forbothcomponentsconsistsofpairsofsourceand
targetstrings,referredtoasxandy,respectively. or pre-computed word alignments. Notably, our
approachmakesnoexplicitassumptionsaboutthe
| 4.1 NQGComponent |          |         |             |            |     | sourceortargetlanguages,beyondthoseimplicit |     |     |                     |     |

|                  |          |         |             |            |     | intheQCFGformalism.                         |     |     | Table1showsexamples |     |
| NQG is           | inspired | by more | traditional | approaches |     |                                             |     |     |                     |     |
ofinducedrules.
tosemanticparsingbasedongrammarformalisms
Ourgrammarinductionalgorithmisguidedby
suchasCCG(ZettlemoyerandCollins,2005,2007;
theprincipleofOccam’srazor,whichleadsusto
Kwiatkowskietal.,2010,2013)andSCFG(Wong
andMooney,2006,2007;Andreasetal.,2013;Li 5SeeAppendixA.1foradditionalbackgroundonQCFGs.


SCAN is the set of derivations that yield source string x
NT →(cid:104)turnright,I_TURN_RIGHT(cid:105) andanytargetstring. Theconstantsl
N
andl
T
can
NT →(cid:104)NT [1] afterNT [2] ,NT [2] NT [1] (cid:105) beinterpretedastheaveragebitlengthforencoding
NT →(cid:104)NT thrice,NT NT NT (cid:105)
[1] [1] [1] [1] non-terminal and terminal symbols, respectively.
GEOQUERY
Inpractice,thesearetreatedashyperparameters.
NT →(cid:104)namesofNT ,NT (cid:105)
[1] [1] We use a greedy search algorithm to find a
NT →(cid:104)towns,cities(cid:105)
grammarthatapproximatelyminimizesthiscode-
NT →(cid:104)NT haveNT runningthroughthem,
[1] [2]
intersection(NT ,traverse_1(NT ))(cid:105) lengthobjective. WeinitializeG bycreatingarule
[1] [2]
NT → (cid:104)x,y(cid:105) for every training example (x,y).
SPIDER-SSP
NT →(cid:104)reviewer,reviewer(cid:105) Byconstruction,theinitialgrammarperfectlyfits
NT →(cid:104)whatistheidoftheNT namedNT ?, thetrainingdata,butisalsoverylarge. Ouralgo-
[1] [2]
selectridfromNT wherename="NT "(cid:105)
[1] [2] rithmiterativelyidentifiesarulethatcanbeadded
to G that decreases our codelength objective by
Table 1: Examples of induced QCFG rules. The sub- enabling≥ 1rule(s)toberemoved,underthein-
script1inNT indicatesthecorrespondencebetween
[1] variantconstraintthatG canstillderivealltraining
sourceandtargetnon-terminals.
examples. Thesearchcompleteswhennorulethat
decreasestheobjectivecanbeidentified. Inprac-
seekthesmallest,simplestgrammarthatexplains tice, we use several approximations to efficiently
thedatawell. WefollowtheMinimumDescription select a rule at each iteration. Additional details
Length (MDL) principle (Rissanen, 1978; Grun- regardingthegrammarinductionalgorithmarede-
wald, 2004) as a way to formalize this intuition. scribedinAppendixA.2.
Specifically, we use standard two-part codes to
#### 4.1.2 NQGSemanticParsingModel
compute description length, where we are inter-
Based on the induced grammar G, we train a dis-
estedinanencodingoftargetsygiventheinputs
criminativelatentvariableparsingmodel,usinga
x,acrossadatasetD consistingofthesepairs. A
method similar to that of Blunsom et al. (2008).
two-part code encodes the model and the targets
Wedefinep(y | x)as:
encoded using the model; the two parts measure
thesimplicityofthemodelandtheextenttowhich (cid:88)
p(y | x) = p(z | x),
itcanexplainthedata,respectively.
Forgrammarinduction,ourmodelissimplyour z∈Zx G ,y
grammar,G. Thecodelengthcanthereforebeex- whereZG isthesetofderivationsofxandy in
(cid:80) x,y
pressed as H(G) − log P (y|x) where
x,y∈D 2 G G. Wedefinep(z | x)as:
H(G) corresponds to the codelength of some en-
coding of G. We approximate H(G) by counting exp(s(z,x))
p(z | x) = ,
terminal(C
T
)andnon-terminal(C
N
)symbolsin (cid:80) exp(s(z(cid:48),x))
the grammar’s rules, R. For P G , we assume a z(cid:48)∈Z x G ,∗
uniformdistributionoverthesetofpossiblederiva-
tions.6 Astheonlymutableaspectofthegrammar wheres(z,x)isaderivationscoreandthedenom-
inator is a global partition function. Similarly to
during induction is the set of rules R, we abuse
theNeuralCRFmodelofDurrettandKlein(2015),
notationslightlyandwriteourapproximatecode-
thescoresdecomposeoveranchoredrules. Unlike
lengthobjectiveasafunctionofRonly:
DurrettandKlein(2015),wecomputethesescores
L(R) = l C (R)+l C (R)− based on contextualized representations from a
N N T T
BERT(Devlinetal.,2019)encoder. Additionalde-
(cid:88) log |Z x G ,y | , tailsregardingthemodelarchitecturecanbefound
2 |ZG |
x,∗ inAppendixA.3.
(x,y)∈D
Attrainingtime,weuseaMaximumMarginal
where ZG is the set of all derivations in G that
x,y Likelihood(MML)objective. Wepreprocesseach
yieldthepairofstringsxandy,whileZ x G ,∗ ⊃ Z x G ,y example to produce parse forest representations
for both ZG and ZG , which correspond to the
6Thiscanbeviewedasaconservativechoice,asinpractice x,y x,∗
numeratoranddenominatorofourMMLobjective,
weexpectourneuralparsertolearnabettermodelforP(y|x)
thananaiveuniformdistributionoverderivations. respectively. By using dynamic programming to


efficientlysumderivationscoresinsidethetraining ustomakeclearcomparisonsbetweensyntheticvs.
| loop, we | can efficiently |     | compute | the | exact | MML | non-syntheticsetups. |     |     |     |     |     |     |

objectivewithoutrequiringapproximationssuchas
|     |     |     |     |     |     |     | Approaches |     | ForNQG-T5,toassesstheeffectof |     |     |     |     |

beamsearch.
modelsize,wecomparetwosizesoftheunderlying
Atinferencetime,weselectthehighestscoring
|     |     |     |     |     |     |     | T5model: | Base(220millionparameters)and3B(3 |     |     |     |     |     |

derivationusinganalgorithmsimilartoCKYthat
|           |          |      |        |           |     |        | billionparameters). |     |     | ToevaluateNQGindividually, |     |     |     |

| considers | anchored | rule | scores | generated |     | by the |                     |     |     |                            |     |     |     |
wetreatanyexamplewherenooutputisprovided
| neuralparsingmodel. |     |     | Weoutputthecorresponding |     |     |     |     |     |     |     |     |     |     |

asincorrectwhencomputingaccuracy.
targetifitcanbederivedbyaCFGdefiningvalid
|     |     |     |     |     |     |     | We select |     | strong | approaches | from | prior | work |

targetconstructionsforthegiventask.
|     |     |     |     |     |     |     | that have | performed |     | well | in at least | one | setting. |

#### 4.1.3 NQGDiscussion We group them into two families of approaches
|     |     |     |     |     |     |     | described | in Figure |     | 1. First, | for general-purpose |     |     |

WenotethatNQGiscloselyrelatedtoworkthat
|     |     |     |     |     |     |     | models | that have | shown | strong | ability |     | to handle |

usessynchronousgrammarsforhierarchicalstatis-
naturallanguagevariation,weconsiderT5,apre-
| tical machine | translation, |     | such | as Hiero | (Chiang, |     |     |     |     |     |     |     |     |

trainedseq2seqmodel,inbothBaseand3Bsizes.
| 2007).                            | Unlike | Hiero, | NQG | does | not rely  | on an |         |     |             |     |         |      |        |

|                                   |        |        |     |      |           |       | Second, | for | specialized |     | methods | with | strong |
| additionalwordalignmentcomponent. |        |        |     |      | Moreover, |       |         |     |             |     |         |      |        |
compositionalbiases,weconsiderapproachesthat
Hierosimplyusesrelativefrequencytolearnrule
|             |                                        |         |     |             |         |     | have been  | developed |      | for SCAN. |               | Some | previous |

| weights.    | Additionally,incontractwithtraditional |         |     |             |         |     |            |           |      |           |               |      |          |
|             |                                        |         |     |             |         |     | approaches | for       | SCAN | require   | task-specific |      | infor-   |
| SCFG models | for                                    | machine |     | translation | applied | to  |            |           |      |           |               |      |          |
mationsuchasthemappingofatoms(Lake,2019;
| semanticparsing |     | (WongandMooney,2006;An- |     |     |     |     |     |     |     |     |     |     |     |

Gordonetal.,2019)oragrammarmimickingthe
dreasetal.,2013),ourneuralmodelconditionson
trainingdata(Nyeetal.,2020),andassucharedif-
| global context | from | the | source | x   | via contextual |     |                                       |     |     |     |     |          |     |

|                |      |     |        |     |                |     | ficulttoadapttonon-syntheticdatasets. |     |     |     |     | Amongthe |     |
wordembeddings,andourgrammar’srulesdonot
approachesthatdonotneedtask-specificresources,
needtocarrysourcecontexttoaiddisambiguation.
|     |     |     |     |     |     |     | we evaluate                                   | two | models | with | publicly |     | available |

|     |     |     |     |     |     |     | code: SyntacticAttention(Russinetal.,2019)and |     |        |      |          |     |           |
4.2 T5Component
|     |     |     |     |     |     |     | CGPS(Lietal.,2019). |     |     | WereportresultsonSCAN |     |     |     |

T5(Raffeletal.,2020)isapre-trainedsequence-to-
fromtheoriginalpapersaswellasnewresultson
sequenceTransformermodel(Vaswanietal.,2017).
ourproposeddatasplits.
Wefine-tuneT5foreachtask.
|     |     |     |     |     |     |     | Datasets | Forthe | SCAN |     | dataset,weevaluateus- |     |     |

## 5 Experiments
ingthelengthsplitandtwoprimitivesplits,jump
andturnleft,includedintheoriginaldataset(Lake
| We evaluate | existing |        | approaches | and     | the    | newly  |             |                                  |     |         |          |     |           |

|             |          |        |            |         |        |        | and Baroni, | 2018).                           |     | We also | evaluate |     | using the |
| proposed    | NQG-T5   | across | a          | diverse | set of | evalu- |             |                                  |     |         |          |     |           |
|             |          |        |            |         |        |        | SCAN        | MCDsplitsfromKeysersetal.(2020). |     |         |          |     |           |
ationstoassesscompositionalgeneralizationand
GEOQUERY(ZelleandMooney,1996)contains
| handlingofnaturallanguagevariation. |     |                |     |         | Weaimto |         |           |          |           |       |       |               |       |

|                                     |     |                |     |         |         |         | natural   | language | questions |       | about | US geography. |       |
| understand                          | how | the approaches |     | compare |         | to each |           |          |           |       |       |               |       |
|                                     |     |                |     |         |         |         | Similarly | to prior | work      | (Dong | and   | Lapata,       | 2016, |
otherforeachtypeofevaluationandinaggregate,
2018),wereplaceentitymentionswithplacehold-
andhowtheperformanceofasingleapproachmay
|     |     |     |     |     |     |     | ers. We | use | a variant | of Functional |     | Query | Lan- |

varyacrossdifferentevaluationtypes.
guage(FunQL)asthetargetrepresentation(Kate
### 5.1 Experimentson SCAN and GEOQUERY et al., 2005). In addition to the standard split of
ZettlemoyerandCollins(2005),wegeneratemulti-
Forourmainexperiments,wefocusonevaluation
plesplitsfocusingoncompositionalgeneralization:
acrossmultiplesplitsoftwodatasetswithcompo-
|                  |     |      |                      |     |     |     | a new | split based | on  | query | length | and | a TMCD |

| sitionalqueries: |     | SCAN | (LakeandBaroni,2018) |     |     |     |       |             |     |       |        |     |        |
split,eachconsistingof440trainand440testex-
| and GEOQUERY |        | (ZelleandMooney,1996;Tang |     |          |      |      |         |     |               |     |       |          |       |

|              |        |                           |     |          |      |      | amples. | We  | also generate |     | a new | template | split |
| and Mooney,  | 2001). | The                       | two | datasets | have | been |         |     |               |     |       |          |       |
consistingof441trainand439testexamples.7
widelyusedtostudycompositionalgeneralization
and robustness to natural language variation, re- 7WegenerateanewtemplatesplitratherthanusetheGEO-
QUERYtemplatesplitofFinegan-Dollaketal.(2018)toavoid
| spectively. | Both | datasets | are | closed-domain |     | and |     |     |     |     |     |     |     |

overlappingtemplatesbetweenthetrainandtestsetswhen
haveoutputswithstraightforwardsyntax,enabling mappingfromSQLtoFunQL.


|     |     |     |     |     | SCAN |     |     | GEOQUERY |     |     | Avg. |

System Jump TurnLeft Len. MCD Standard Template Len. TMCD Rank
| LANE | (Liuetal.,2020)  |     |     | 100 | —   | 100 100 | —   | —   | —   | —   | —   |

| NSSM | (Chenetal.,2020) |     |     | 100 | —   | 100 —   | —   | —   | —   | —   | —   |
SyntacticAttn.(Russinetal.,2019) 91.0 99.9 15.2 2.9 77.5 70.6 23.6 0.0 3.9
| CGPS(Lietal.,2019) |     |     |     | 98.8 | 99.7 | 20.3 2.0 | 62.1  | 32.8 | 9.3 | 32.3 | 4.4 |

| GECA(Andreas,2020) |     |     |     | 87.0 | —    | — —      | 78.0† | —    | —   | —    | —   |
86.1†
| SBSP(HerzigandBerant,2020) |          |     |     | 100 | 100 | 100 100 |       | —   | —   | —   | —   |

| SBSP                       | −lexicon |     |     | 100 | 100 | 100 100 | 78.9† | —   | —   | —   | —   |
T5-Base(Raffeletal.,2020) 99.5 62.0 14.4 15.4 92.9 87.0 39.1 54.3 2.9
T5-3B(Raffeletal.,2020) 99.0 65.1 3.3 11.6 93.2 83.1 36.8 51.6 —
| NQG-T5-Base |     |     |     | 100 | 100 | 100 100 | 92.9 | 88.8 | 52.2 | 56.6 | 1.0 |

| NQG-T5-3B   |     |     |     | 100 | 100 | 100 100 | 93.7 | 85.0 | 51.4 | 54.1 | —   |
| NQG         |     |     |     | 100 | 100 | 100 100 | 76.8 | 61.9 | 37.4 | 41.1 | 2.3 |
Table 2: Main Results. Existing approaches do not excel on a diverse set of evaluations across synthetic and
non-synthetictasks, butNQG-T5obtainssignificantimprovements. Forcomparison, wereporttheaveragerank
among5approachesacrossall8evaluations. Graycellsarepreviouslyreportedresults. † indicatesdifferencesin
GEOQUERYsettings(seediscussionin§5.1). Boldfacedresultsarewithin1.0pointsofthebestresult.
We report exact-match accuracy for both on the (T)MCD splits of the two datasets. Sec-
datasets.8 Hyperparametersandpre-processingde- ond,theproposedNQG-T5approachcombinesthe
tailscanbefoundinAppendixB. strengths of T5 and NQG to achieve superior re-
|         |             |     |               |     |          | sultsacrossallevaluations. |     |     | ItimprovesoverT5on |     |     |

| Results | The results |     | are presented |     | in Table | 2.                         |     |     |                    |     |     |
compositionalgeneralizationforbothsyntheticand
| The results | for T5 | on  | SCAN | are | from Furrer |     |     |     |     |     |     |

non-syntheticdatawhilemaintainingT5’sperfor-
| et al. (2020). | Additionally, |     |     | we include | results |     |     |     |     |     |     |

manceonhandlingin-distributionnaturallanguage
| forGECA9                | (Andreas,2020),adataaugmentation |      |                   |         |           |                  |         |                           |         |         |          |

|                         |                                  |      |                   |         |           | variation,       | leading | to an                     | average | rank of | 1.0 com- |
| method,                 | as well as                       | LANE | (Liu              | et al., | 2020) and |                  |         |                           |         |         |          |
|                         |                                  |      |                   |         |           | paredto2.9forT5. |         | (Tothebestofourknowledge, |         |         |          |
| NSSM(Chenetal.,2020)10. |                                  |      | Wealsocomparewith |         |           |                  |         |                           |         |         |          |
bothT5andNQG-T5achievenewstate-of-the-art
| SpanBasedSP11 | (HerzigandBerant,2020). |     |       |           |           |                              |     |           |          |             |      |

|               |                         |     |       |           |           | accuracyonthestandardsplitof |     |           |          | GEOQUERY.)  |      |
| From          | the results,            | we  | first | note that | the rela- |                              |     |           |          |             |      |
|               |                         |     |       |           |           | Finally,                     | we  | note that | there is | substantial | room |
tiveperformanceofapproachesoncompositional
forimprovementonhandlingbothcompositional
| splitsof | SCAN isnotverypredictiveoftheirrela- |     |     |     |     |     |     |     |     |     |     |

generalizationandnaturallanguagevariation.
tiveperformanceoncompositionalsplitsofGEO-
QUERY. For example, GGPS is better than T5 5.2 Experimentson SPIDER
| on the length                 | split | of SCAN |     | but is    | significantly |                             |                                  |     |     |        |     |

|                               |       |         |     |           |               | Wenowcomparetheapproacheson |                                  |     |     | SPIDER | (Yu |
| worsethanT5onthelengthsplitof |       |         |     | GEOQUERY. |               |                             |                                  |     |     |        |     |
|                               |       |         |     |           |               | etal.,2018),                | anon-synthetictext-to-SQLdataset |     |     |        |     |
Similarly,therankingofmostmethodsisdifferent
thatincludesthefurtherchallengesofschemalink-
8ForGEOQUERYwereportthemeanof3runsforNQG,
ingandmodelingcomplexSQLsyntax.
withstandarddeviationsreportedinAppendix B.5 SPIDER contains 10,181 questions and 5,693
9GECAreportsGEOQUERYresultsonasettingwithPro-
|     |     |     |     |     |     | unique | SQL queries | across | 138 | domains. | The |

loglogicalformsandwithoutanonymizationofentities.Note
thattheperformanceofGECAdependsonboththequalityof primary evaluation is in the cross-database set-
thegenerateddataandtheunderlyingparser(JiaandLiang,
ting,wheremodelsareevaluatedonexamplesfor
2016),whichcancomplicatetheanalysis.
|     |     |     |     |     |     | databases | not | seen during | training. | The | primary |

10TheseSCAN-motivatedapproachesbothincludeaspects
ofdiscretesearchandcurriculumlearning,andhavenotbeen challenge in this setting is generalization to new
| demonstrated | to scale | effectively | to  | non-synthetic | parsing |                                     |     |     |     |     |        |

|              |          |             |     |               |         | databaseschemas,whichisnotourfocus. |     |     |     |     | There- |
tasks.Moreover,thecodeiseithernotyetreleased(NSSM)
|     |     |     |     |     |     | fore, we | use | a setting | where the | databases | are |

orspecializedtoSCAN(LANE).
11SpanBasedSPpreprocessesSCANtoaddprogram-level sharedbetweentrainandtestexamples.12 Wegen-
supervision.ForGEOQUERY,theysimilarlyuseFunQL,but
usesslightlydifferentdatapreprocessingandreportdenotation 12Thisissimilartothe“examplesplit”discussedin Yu
accuracy.WecomputedNQG-T5’sdenotationaccuracytobe et al. (2018). However, we only consider examples in the
2.1pointshigherthanexact-matchaccuracyonthestandard originaltrainingsetfordatabaseswithmorethan50examples
splitofGeoQuery. toensuresufficientcoverageovertableandcolumnnamesin


|             |         |       |        | SPIDER-SSP |      |                           |     |     |     | SPIDER-XSP |      |     |

|             |         |       |        |            |      | System                    |     |     |     |            | Dev  |     |
| System      |         | Rand. | Templ. | Len.       | TMCD |                           |     |     |     |            |      |     |
|             |         |       |        |            |      | RYANSQLv2(Choietal.,2020) |     |     |     |            | 70.6 |     |
| T5-Base     | −schema | 76.5  |        | 45.3 42.5  | 42.3 |                           |     |     |     |            |      |     |
| T5-Base     |         | 82.0  |        | 59.3 49.0  | 60.9 | T5-Base                   |     |     |     |            | 57.1 |     |
| T5-3B       |         | 85.6  |        | 64.8 56.7  | 69.6 | T5-3B                     |     |     |     |            | 70.0 |     |
| NQG-T5-Base |         | 81.8  |        | 59.2 49.0  | 60.8 | NQG-T5-Base               |     |     |     |            | 57.1 |     |
| NQG-T5-3B   |         | 85.4  |        | 64.7 56.7  | 69.5 | NQG-T5-3B                 |     |     |     |            | 70.0 |     |
| NQG         |         |       | 1.3    | 0.5 0.0    | 0.5  | NQG                       |     |     |     |            | 0.0  |     |
Table3: ResultsonSpider-SSP.Whilethetext-to-SQL Table4: AlthoughSpider-XSPisnotourfocus,T5and
taskisnotmodeledwellbytheNQGgrammardueto NQG-T5arecompetitivewiththestate-of-the-art.
SQL’scomplexsyntax,NQG-T5stillperformswellby
relyingonT5.
|     |     |     |     |     |     | theaccuracyofT5-Baseacrossvarioussplits. |     |     |     |     |     | For |

GEOQUERY,theTMCDsplitissignificantlymore
| erate 3                            | new      | splits consisting |     | of 3,282      | train and |                                  |              |                             |          |             |     |       |

|                                    |          |                   |     |               |           | challengingthanthetemplatesplit. |              |                             |          | However,for |     |       |
| 1,094 test                         | examples | each:             | a   | random split, | a split   |                                  |              |                             |          |             |     |       |
|                                    |          |                   |     |               |           | SPIDER,                          | the template |                             | and TMCD | splits      | are | simi- |
| basedonsourcelength,andaTMCDsplit. |          |                   |     |               | Wealso    |                                  |              |                             |          |             |     |       |
|                                    |          |                   |     |               |           | larlychallenging.                |              | Notably,templatesplitsdonot |          |             |     |       |
generateatemplatesplitbyanonymizingintegers
|            |           |            |          |                 |           | haveanexplicitatomconstraint. |          |     |                | Wefindthatfor |          |     |

| and quoted | strings,  | consisting |          | of 3,280        | train and |                               |          |     |                |               |          |     |
|            |           |            |          |                 |           | the SPIDER                    | template |     | split, T5-Base |               | accuracy | is  |
| 1,096 test | examples. |            | We adopt | the terminology |           |                               |          |     |                |               |          |     |
53.9%forthe30.3%oftestsetexamplesthatcon-
| of Suhr                              | et al. | (2020) | and use | SPIDER-SSP | to re-  |              |     |      |        |           |     |       |

|                                      |        |        |         |            |         | tain an atom | not | seen | during | training, | and | 61.6% |
| fertothesesame-databasesplits,anduse |        |        |         |            | SPIDER- |              |     |      |        |           |     |       |
ontheremainder,indicatingthatgeneralizationto
XSPtorefertothestandardcross-databasesetting.
|                    |     |                          |     |                     |     | unseen            | atoms | can contribute               |     | to the | difficulty | of  |

| We prepend         |     | the name                 | of  | the target database | to  |                   |       |                              |     |        |            |     |
|                    |     |                          |     |                     |     | templatesplits.13 |       | Lengthsplitsarealsoverychal- |     |        |            |     |
| thesourcesequence. |     | ForT5,wealsoserializethe |     |                     |     |                   |       |                              |     |        |            |     |
lenging,buttheyleadtoamorepredictableerror
| database | schema | as a | string | and append | it to the |     |     |     |     |     |     |     |

patternforseq2seqmodels,asdiscussednext.
| sourcesequencesimilarlytoSuhretal.(2020).    |     |     |     |     | We  |                |     |     |     |     |     |     |

| reportexactsetmatchwithoutvalues,thestandard |     |     |     |     |     | 6.2 T5Analysis |     |     |     |     |     |     |
Spiderevaluationmetric(Yuetal.,2018).
WeanalyzeNQG-T5’scomponents,startingwith
|         |       |           |        |                |        | T5. On      | length  | splits, | there   | is a consistent |      | pat-    |

| Results | Table | 3 shows   | the    | results of     | T5 and |             |         |         |         |                 |      |         |
|         |       |           |        |                |        | tern to the | errors. | T5’s    | outputs | on the          | test | set are |
| NQG-T5  | on    | different | splits | of SPIDER-SSP. |        |             |         |         |         |                 |      |         |
We also show T5-Base performance without the notsignificantlylongerthanthemaximumlength
schema string appended. The text-to-SQL map- observed during training, leading to poor perfor-
|                 |          |           |     |                    |      | mance.          | This phenomenon |     | was | explored | by  | New- |

| ping is         | not well | modeled   | by  | NQG. Nevertheless, |      |                 |                 |     |     |          |     |      |
| the performance |          | of NQG-T5 |     | is competitive     | with | manetal.(2020). |                 |     |     |          |     |      |
T5,indicatingastrengthofthehybridapproach. Diagnosingthelargegeneralizationgaponthe
(T)MCDsplitsismorechallenging,butwenoticed
| Table | 4 shows | the | results | on SPIDER-XSP, |     |     |     |     |     |     |     |     |

whichfocuses onhandling unseenschema rather several error patterns. For T5-Base on the GEO-
thancompositionalgeneralization. Tooursurprise, QUERY TMCD split, in 52 of the 201 incorrect
T5-3Bprovestobecompetitivewiththestate-of- predictions (26%), the first incorrectly predicted
symboloccurswhenthegoldsymbolhas0prob-
the-art(Choietal.,2020)forapproacheswithout
access to database contents beyond the table and ability under a trigram language model fit to the
columnnames. AsNQG-T5simplyusesT5’sout- trainingdata. Thissuggeststhatthedecoder’sim-
plicittargetlanguagemodelmighthaveover-fitted
putwhentheinducedgrammarlackscoverage,it
tooiscompetitive. tothedistributionoftargetsequencesinthetrain-
|     |     |     |     |     |     | ing data, | hampering | its | ability | to generate |     | novel |

## 6 Analysis
|     |     |     |     |     |     | compositions. |               | Non-exclusivelywiththeseerrors, |     |       |      |     |

|     |     |     |     |     |     | 53% of        | the incorrect | predictions                     |     | occur | when | the |
### 6.1 ComparisonofDataSplits
goldtargetcontainsanatomthatisseeninonly1
| Table 6 | compares | the | compound | divergence, | the |     |     |     |     |     |     |     |

number of test examples with unseen atoms, and 13Futureworkcouldexploredifferentchoicesforconstruct-
ingtemplateandTMCDsplits,suchasalternativecompound
thetrainingdata.Thisincludes51databases. definitionsandatomconstraints.


|     |     |     | SCAN |     |     | GEOQUERY |     |     | SPIDER-SSP |     |     |

Metric Jump TurnL. Len. MCD Stand. Templ. Len. TMCD Rand. Templ. Len. TMCD
NQGCoverage 100 100 100 100 80.2 64.5 43.3 43.7 1.5 0.5 0.0 0.6
NQGPrecision 100 100 100 100 95.7 95.8 86.4 94.1 87.5 83.3 — 85.7
Table5: NQGcoverageandprecision. NQG-T5outperformsT5whenNQGhashigherprecisionthanT5overthe
subsetofexamplesitcovers.
Dataset Split % D T5-Base increase the correspondence between source and
ZA C
| GEOQUERY |     | Standard | 0.3 | 0.03 92.9 |     | targetsyntax. |             |     |                  |     |     |

|          |     |          |     |           |     | Forboth       | GEOQUERYand |     | SPIDER,NQGislim- |     |     |
| GEOQUERY |     | Random   | 1.4 | 0.03 91.1 |     |               |             |     |                  |     |     |
GEOQUERY Template 0.9 0.07 87.0 itedbytheexpressivenessofQCFGsandthesimple
| GEOQUERY |     | Length | 4.3 | 0.17 39.1 |     |     |     |     |     |     |     |

greedysearchprocedureusedforgrammarinduc-
| GEOQUERY   |     | TMCD     | 0    | 0.19 54.3 |     |                               |          |     |             |               |            |

|            |     |          |      |           |     | tion, which                   | can lead | to  | sub-optimal |               | approxima- |
| SPIDER-SSP |     | Random   | 6.2  | 0.03 82.0 |     |                               |          |     |             |               |            |
|            |     |          |      |           |     | tionsoftheinductionobjective. |          |     |             | Notably,QCFGs |            |
| SPIDER-SSP |     | Template | 30.3 | 0.08 59.2 |     |                               |          |     |             |               |            |
cannotdirectlyrepresentrelationsbetweensource
| SPIDER-SSP |     | Length | 27.4 | 0.08 49.0 |     |     |     |     |     |     |     |

SPIDER-SSP TMCD 0 0.18 60.9 strings, such as semantic similarity, or relations
betweentargetstrings,suchaslogicalequivalence
Table6: Percentageoftestexampleswithatomsnotin-
|                          |     |     |                         |     |     | (e.g. intersect(a,b)              |     | ⇔   | intersect(b,a)), |              | that |

| cludedinthetrainingset(% |     |     | ZA ),compounddivergence |     |     |                                   |     |     |                  |              |      |
|                          |     |     |                         |     |     | couldenablegreatergeneralization. |     |     |                  | However,such |      |
(D ),andT5-Baseaccuracyforvariousdatasetsplits.
| C   |     |     |     |     |     | extensions | pose additional |     | scalability |     | challenges, |

requiringnewresearchinmoreflexibleapproaches
forbothlearningandinference.
exampleduringtraining,suggestingthatT5strug-
| gles with | single-shot | learning |     | of new atoms. | In  | 7 Conclusions |     |     |     |     |     |

othercases,theerrorsappeartoreflectover-fitting
tospuriouscorrelationsbetweeninputsandoutputs. Our experiments and analysis demonstrate that
|     |     |     |     |     |     | NQGandT5offerdifferentstrengths. |     |     |     |     | NQGgen- |

SomeerrorexamplesareshowninAppendixB.6.
erallyhashigherprecisionforout-of-distribution
### 6.3 NQGAnalysis
examples,butislimitedbythesyntacticconstraints
ofthegrammarformalismandbyrequiringexact
| To analyze | NQG, | we compute |     | its coverage | (frac- |     |     |     |     |     |     |

lexicaloverlapwithinducedrulesinordertopro-
tionofexampleswhereNQGproducesanoutput)
andprecision(fractionofexampleswithacorrect videaderivationatinferencetime. T5’scoverage
output among ones where an output is produced) isnotlimitedbysuchconstraints,butprecisioncan
besignificantlylowerforout-of-distributionexam-
| ondifferentdatasplits. |     | TheresultsinTable5show |     |     |     |     |     |     |     |     |     |

thatNQGhashighprecisionbutstrugglesatcover- ples. WithNQG-T5,weofferasimplecombination
ageonsomedatasplits. ofthesestrengths. Whileaccuracyisstilllimited
forout-of-distributionexampleswhereNQGlacks
Thereisasignificantdifferenceintheeffective-
|         |             |           |     |           |       | coverage, | we believe | it sets | a strong |     | and simple |

| ness of | the grammar | induction |     | procedure | among |           |            |         |          |     |            |
thethreedatasets. Inductionisparticularlyunsuc- baselineforfuturework.
cessfulfor SPIDER,asSQLhascomplicatedsyn- Morebroadly,ourworkhighlightsthatevaluat-
|     |     |     |     |     |     | ing on a | diverse set | of benchmarks |     | is  | important, |

taxandoftenrequirescomplexcoordinationacross
discontinuousclauses. Mostoftheinducedrules andthathandlingbothout-of-distributioncomposi-
are limited to simply replacing table and column tionalgeneralizationandnaturallanguagevariation
remainsanopenchallengeforsemanticparsing.
namesorvalueliteralswithnon-terminals,suchas
theruleshowninTable1,ratherthanrepresenting
Acknowledgements
| nestedsub-structures. |     | Thedegreeofspan-to-span |     |     |     |     |     |     |     |     |     |

correspondencebetweennaturallanguageandSQL We thank Kenton Lee, William Cohen, Jeremy
isseeminglylowerthanforotherformalismssuch Cole, and Luheng He for helpful discussions.
asFunQL,whichlimitstheeffectivenessofgram- ThanksalsotoEmilyPitler,JonathanHerzig,and
mar induction. Intermediate representations for theanonymousreviewersfortheircommentsand
| SQLsuchasSemQL(Guoetal.,2019)mayhelp |     |     |     |     |     | suggestions. |     |     |     |     |     |

EthicalConsiderations HLT,pages200–208,Columbus,Ohio.Association
forComputationalLinguistics.
| This paper | proposed |     | to expand |     | the set | of bench- |     |     |     |     |     |     |     |

marksusedtoevaluatecompositionalgeneraliza- Xinyun Chen, Chen Liang, Adams Wei Yu, Dawn
|         |          |          |     |       |         |          | Song,                                       | and Denny | Zhou. | 2020. | Compositional |     | gen- |

| tion in | semantic | parsing. |     | While | we hope | that en- |                                             |           |       |       |               |     |      |
|         |          |          |     |       |         |          | eralizationvianeural-symbolicstackmachines. |           |       |       |               |     | Ad-  |
suringsemanticparsingapproachesperformwell
|                                              |                     |      |            |               |      |            | vances        | in Neural | Information  |     | Processing   |     | Systems, |

| acrossadiversesetofevaluations,includingones |                     |      |            |               |      |            | 33.           |           |              |     |              |     |          |
| that test                                    | out-of-distribution |      |            | compositional |      | gener-     |               |           |              |     |              |     |          |
|                                              |                     |      |            |               |      |            | David Chiang. | 2007.     | Hierarchical |     | phrase-based |     | trans-   |
| alization,                                   | would               | lead | to systems |               | that | generalize |               |           |              |     |              |     |          |
lation. computationallinguistics,33(2):201–228.
| better to | languages | not | well | represented |     | in small |     |     |     |     |     |     |     |

trainingsets,wehaveonlyevaluatedourmethods DongHyunChoi,MyeongcheolShin,EungGyunKim,
|     |     |     |     |     |     |     | and Dong | Ryeol | Shin. | 2020. | RYANSQL: |     | recur- |

onsemanticparsingdatasetsinEnglish.
|     |        |        |     |      |               |     | sively           | applying | sketch-based    |     | slot | fillings   | for com- |

| Our | NQG-T5 | method |     | uses | a pre-trained | T5  |                  |          |                 |     |      |            |          |
|     |        |        |     |      |               |     | plex text-to-sql |          | in cross-domain |     |      | databases. | arXiv    |
model,whichiscomputationallyexpensiveinfine- preprintarXiv:2004.03125.
| tuning | and inference, |     | especially |     | for larger | mod- |           |     |            |     |        |     |           |

|        |                |     |            |     |            |      | JK Chung, | PL  | Kannappan, |     | CT Ng, | and | PK Sahoo. |
els(seeAppendixB.1fordetailsonrunningtime
1989. Measuresofdistancebetweenprobabilitydis-
| and compute |     | architecture). |     | Our | method | does not |             |                                     |     |     |     |     |     |

|             |     |                |     |     |        |          | tributions. | Journalofmathematicalanalysisandap- |     |     |     |     |     |
require pre-training of large models, as it uses plications,138(1):280–292.
| pre-existing | model |     | releases. | NQG-T5-base |     | out- |                 |     |                              |     |     |     |     |

|              |       |     |           |             |     |      | JohnCocke.1969. |     | Programminglanguagesandtheir |     |     |     |     |
performsoriscomparableinaccuracytoT5-3Bon
|                     |     |     |                          |     |     |     | compilers: | Preliminary |     | notes. | New | York | Univer- |

| thenon-SQLdatasets, |     |     | leadingtorelativesavings |     |     |     |            |             |     |        |     |      |         |
sity.
ofcomputationalresources.
|     |     |     |     |     |     |     | Jacob Devlin,      | Ming-Wei   |              | Chang, | Kenton |              | Lee, and |

|     |     |     |     |     |     |     | Kristina           | Toutanova. |              | 2019.  | BERT:  | Pre-training | of       |
|     |     |     |     |     |     |     | deep bidirectional |            | transformers |        | for    | language     | under-   |
References
|     |     |     |     |     |     |     | standing. | In  | Proceedings |     | of the | 2019 Conference |     |

Alfred V Aho and Jeffrey D Ullman. 1972. The the- of the North American Chapter of the Association
oryofparsing,translation,andcompiling,volume1. for Computational Linguistics: Human Language
Prentice-HallEnglewoodCliffs,NJ. Technologies, Volume 1 (Long and Short Papers),
pages4171–4186,Minneapolis,Minnesota.Associ-
ationforComputationalLinguistics.
| Jacob Andreas.     |     | 2020. | Good-enough    |     | compositional |          |     |     |     |     |     |     |     |

| data augmentation. |     |       | In Proceedings |     | of the        | 58th An- |     |     |     |     |     |     |     |
nual Meeting of the Association for Computational Li Dong and Mirella Lapata. 2016. Language to logi-
Linguistics, pages 7556–7566, Online. Association calformwithneuralattention. InProceedingsofthe
forComputationalLinguistics. 54thAnnualMeetingoftheAssociationforCompu-
|                |          |         |             |         |              |            | tationalLinguistics(Volume1: |             |         |     | LongPapers),pages |                |     |

| Jacob Andreas, |          | Andreas | Vlachos,    |         | and Stephen  | Clark.     | 33–43.                       |             |         |     |                   |                |     |
| 2013.          | Semantic | parsing | as          | machine | translation. | In         |                              |             |         |     |                   |                |     |
|                |          |         |             |         |              |            | Li Dong                      | and Mirella | Lapata. |     | 2018.             | Coarse-to-fine | de- |
| Proceedings    |          | of the  | 51st Annual |         | Meeting      | of the As- |                              |             |         |     |                   |                |     |
sociation for Computational Linguistics (Volume 2: codingforneuralsemanticparsing. InProceedings
ShortPapers),pages47–52,Sofia,Bulgaria.Associ- of the 56th Annual Meeting of the Association for
ationforComputationalLinguistics. ComputationalLinguistics(Volume1:LongPapers),
|     |     |     |     |     |     |     | pages | 731–742, | Melbourne, |     | Australia. | Association |     |

Jasmijn Bastings, Marco Baroni, Jason Weston, forComputationalLinguistics.
| Kyunghyun |     | Cho, and | Douwe | Kiela. | 2018. | Jump |     |     |     |     |     |     |     |

to better conclusions: Scan both left and right. In GregDurrettandDanKlein.2015. Neuralcrfparsing.
Proceedings of the 2018 EMNLP Workshop Black- In Proceedings of the 53rd Annual Meeting of the
boxNLP: Analyzing and Interpreting Neural Net- Association for Computational Linguistics and the
worksforNLP,pages47–55. 7th International Joint Conference on Natural Lan-
|         |                   |         |     |          |           |        | guage    | Processing | (Volume |     | 1: Long | Papers), | pages |

| Peter W | Battaglia,        | Jessica | B   | Hamrick, | Victor    | Bapst, | 302–312. |            |         |     |         |          |       |
| Alvaro  | Sanchez-Gonzalez, |         |     | Vinicius | Zambaldi, | Ma-    |          |            |         |     |         |          |       |
teuszMalinowski,AndreaTacchetti,DavidRaposo, Catherine Finegan-Dollak, Jonathan K. Kummerfeld,
Adam Santoro, Ryan Faulkner, et al. 2018. Rela- Li Zhang, Karthik Ramanathan, Sesh Sadasivam,
tionalinductivebiases,deeplearning,andgraphnet- Rui Zhang, and Dragomir Radev. 2018. Improving
arXivpreprintarXiv:1806.01261. text-to-SQL evaluation methodology. In Proceed-
works.
|     |     |     |     |     |     |     | ings of | the 56th | Annual | Meeting | of  | the Association |     |

PhilBlunsom,TrevorCohn,andMilesOsborne.2008. forComputationalLinguistics(Volume1: LongPa-
A discriminative latent variable model for statisti- pers), pages 351–360, Melbourne, Australia. Asso-
calmachinetranslation. InProceedingsofACL-08: ciationforComputationalLinguistics.


Daniel Furrer, Marc van Zee, Nathan Scales, and MarcvanZee,andOlivierBousquet.2020. Measur-
NathanaelSchärli.2020. Compositionalgeneraliza- ingcompositionalgeneralization: Acomprehensive
tioninsemanticparsing:Pre-trainingvs.specialized methodonrealisticdata. InICLR.
| architectures. | arXivpreprintarXiv:2007.08970. |     |     |     |     |     |         |     |         |         |       |       |        |

|                |                                |     |     |     |     |     | Najoung | Kim | and Tal | Linzen. | 2020. | COGS: | A com- |
Jonathan Gordon, David Lopez-Paz, Marco Baroni, positionalgeneralizationchallengebasedonseman-
and Diane Bouchacourt. 2019. Permutation equiv- tic interpretation. In Proceedings of the 2020 Con-
ariant models for compositional generalization in ferenceonEmpiricalMethodsinNaturalLanguage
| language. | InInternationalConferenceonLearning |     |     |     |     |     |     |     |     |     |     |     |     |

Processing(EMNLP),pages9087–9105,Online.As-
Representations.
sociationforComputationalLinguistics.
| PeterGrünwald.1995. |     | Aminimumdescriptionlength |     |     |     |     |     |     |     |     |     |     |     |

TomKwiatkowski,EunsolChoi,YoavArtzi,andLuke
approach to grammar inference. In International Zettlemoyer. 2013. Scaling semantic parsers with
| Joint Conference |     | on  | Artificial | Intelligence, |     | pages |                             |     |     |     |                    |     |     |

|                  |     |     |            |               |     |       | on-the-flyontologymatching. |     |     |     | InProceedingsofthe |     |     |
203–216.Springer.
|     |     |     |     |     |     |     | 2013 | conference | on  | empirical | methods |     | in natural |

languageprocessing,pages1545–1556.
| Peter Grunwald. |             | 2004. | A tutorial | introduction |     | to    |                  |     |      |              |     |        |       |

| the minimum     | description |       | length     | principle.   |     | arXiv |                  |     |      |              |     |        |       |
|                 |             |       |            |              |     |       | Tom Kwiatkowski, |     | Luke | Zettlemoyer, |     | Sharon | Gold- |
preprintmath/0406077.
|     |     |     |     |     |     |     | water, | and Mark | Steedman. |     | 2010. | Inducing | proba- |

Jiaqi Guo, Zecheng Zhan, Yan Gao, Yan Xiao, bilisticccggrammarsfromlogicalformwithhigher-
|            |      |      |      |             |     |        | order   | unification. | In  | Proceedings |     | of the  | 2010 con- |

| Jian-Guang | Lou, | Ting | Liu, | and Dongmei |     | Zhang. |         |              |     |             |     |         |           |
|            |      |      |      |             |     |        | ference | on empirical |     | methods     | in  | natural | language  |
2019. Towardscomplextext-to-sqlincross-domain
processing,pages1223–1233.AssociationforCom-
| database | with intermediate |      | representation. |         | In     | Pro-  |                        |          |         |               |         |               |       |

| ceedings | of the            | 57th | Annual          | Meeting | of the | Asso- | putationalLinguistics. |          |         |               |         |               |       |
| ciation  | for Computational |      | Linguistics,    |         | pages  | 4524– |                        |          |         |               |         |               |       |
| 4535.    |                   |      |                 |         |        |       | B. M. Lake,            | T.       | Linzen, | and M.        | Baroni. | 2019.         | Human |
|          |                   |      |                 |         |        |       | few-shot               | learning | of      | compositional |         | instructions. | In    |
Jonathan Herzig and Jonathan Berant. 2019. Don’t Proceedings of the 41st Annual Conference of the
CognitiveScienceSociety.
| paraphrase, | detect!  | rapid    | and | effective   | data | collec- |     |     |     |     |     |     |     |

| tion for    | semantic | parsing. | In  | Proceedings |      | of the  |     |     |     |     |     |     |     |
2019 Conference on Empirical Methods in Natu- BrendenLakeandMarcoBaroni.2018. Generalization
ral Language Processing and the 9th International without systematicity: On the compositional skills
Joint Conference on Natural Language Processing of sequence-to-sequence recurrent networks. In In-
ternationalConferenceonMachineLearning,pages
(EMNLP-IJCNLP),pages3801–3811.
2873–2882.
| Jonathan Herzig | and | Jonathan |     | Berant. | 2020. | Span- |     |     |     |     |     |     |     |

based semantic parsing for compositional general- BrendenMLake.2019. Compositionalgeneralization
ization. arXivpreprintarXiv:2009.06040. throughmetasequence-to-sequencelearning. InAd-
|         |         |             |     |         |       |      | vances | in Neural | Information |     | Processing |     | Systems, |

| Theo MV | Janssen | and Barbara | H   | Partee. | 1997. | Com- |        |           |             |     |            |     |          |
pages9788–9798.
| positionality. | In  | Handbook | of  | logic | and language, |     |     |     |     |     |     |     |     |

pages417–473.Elsevier.
|                             |          |          |     |                   |     |        | Brenden                       | M Lake,    | Tomer | D Ullman, |              | Joshua      | B Tenen-   |

|                             |          |          |     |                   |     |        | baum,andSamuelJGershman.2017. |            |       |           |              | Buildingma- |            |
| RobinJiaandPercyLiang.2016. |          |          |     | Datarecombination |     |        |                               |            |       |           |              |             |            |
|                             |          |          |     |                   |     |        | chines                        | that learn | and   | think     | like people. |             | Behavioral |
| for neural                  | semantic | parsing. |     | In Proceedings    |     | of the |                               |            |       |           |              |             |            |
andbrainsciences,40.
54thAnnualMeetingoftheAssociationforCompu-
| tationalLinguistics(Volume1: |     |     |     | LongPapers),pages |     |     |     |     |     |     |     |     |     |

KentonLee,LuhengHe,MikeLewis,andLukeZettle-
12–22.
|            |       |              |             |     |     |        | moyer.  | 2017.          | End-to-end |     | neural   | coreference | reso- |

|            |       |              |             |     |     |        | lution. | In Proceedings |            | of  | the 2017 | Conference  | on    |
| T. Kasami. | 1965. | An efficient | recognition |     | and | syntax |         |                |            |     |          |             |       |
EmpiricalMethodsinNaturalLanguageProcessing,
| analysisalgorithmforcontext-freelanguages. |     |     |     |                   |     | Tech- |               |     |     |     |     |     |     |

| nicalReportAFCRL-65-758,                   |     |     |     | AirForceCambridge |     |       | pages188–197. |     |     |     |     |     |     |
ResearchLaboratory,Bedford,MA.
|     |     |     |     |     |     |     | Junhui Li, | Muhua     | Zhu, | Wei      | Lu, and | Guodong | Zhou.    |

|     |     |     |     |     |     |     | 2015.      | Improving |      | semantic | parsing | with    | enriched |
RohitJKate,YukWahWong,andRaymondJMooney.
|                |                                      |              |     |         |           |      | synchronous |        | context-free    |     | grammar. |           | In Proceed- |

| 2005. Learning |                                      | to transform |     | natural | to formal | lan- |             |        |                 |     |          |           |             |
|                |                                      |              |     |         |           |      | ings        | of the | 2015 Conference |     | on       | Empirical | Meth-       |
| guages.        | InProceedingsoftheNationalConference |              |     |         |           |      |             |        |                 |     |          |           |             |
on Artificial Intelligence, volume 20, page 1062. ods in Natural Language Processing, pages 1455–
Menlo Park, CA; Cambridge, MA; London; AAAI 1465, Lisbon, Portugal. Association for Computa-
| Press;MITPress;1999. |     |     |     |     |     |     | tionalLinguistics. |     |     |     |     |     |     |

Daniel Keysers, Nathanael Schärli, Nathan Scales, YuanpengLi,LiangZhao,JianyuWang,andJoelHes-
Hylke Buisman, Daniel Furrer, Sergii Kashubin, tness.2019. Compositionalgeneralizationforprim-
Nikola Momchev, Danila Sinopalnikov, Lukasz itivesubstitutions. InProceedingsofthe2019Con-
Stafiniak,TiborTihon,DmitryTsarkov,XiaoWang, ferenceonEmpiricalMethodsinNaturalLanguage


Processing and the 9th International Joint Confer- Jorma Rissanen. 1978. Modeling by shortest data de-
ence on Natural Language Processing (EMNLP- scription. Automatica,14(5):465–471.
IJCNLP),pages4284–4293,HongKong,China.As-
sociationforComputationalLinguistics. JakeRussin,JasonJo,RandallCO’Reilly,andYoshua
|     |     |     |     |     |     |     | Bengio. | 2019. | Compositional |     | generalization |     | in a |

Qian Liu, Shengnan An, Jian-Guang Lou, Bei Chen, deepseq2seqmodelbyseparatingsyntaxandseman-
ZeqiLin,YanGao,BinZhou,NanningZheng,and tics. arXivpreprintarXiv:1904.09708.
| Dongmei | Zhang. | 2020. | Compositional |     | generaliza- |     |     |     |     |     |     |     |     |

MarkusSaers,KarteekAddanki,andDekaiWu.2013.
| tionbylearninganalyticalexpressions. |     |     |     |     | Advancesin |     |              |     |              |         |     |           |     |

|                                      |     |     |     |     |            |     | Unsupervised |     | transduction | grammar |     | induction | via |
NeuralInformationProcessingSystems,33.
|     |     |     |     |     |     |     | minimumdescriptionlength. |     |     |     | InProceedingsofthe |     |     |

Richard Montague. 1970. Universal grammar. Theo- SecondWorkshoponHybridApproachestoTransla-
ria,36(3):373–398. tion, pages 67–73, Sofia, Bulgaria. Association for
ComputationalLinguistics.
| Benjamin    | Newman, | John     | Hewitt, | Percy | Liang, | and      |         |       |           |         |       |     |        |

|             |         |          |         |       |        |          | David A | Smith | and Jason | Eisner. | 2006. |     | Quasi- |
| Christopher | D.      | Manning. | 2020.   | The   | EOS    | decision |         |       |           |         |       |     |        |
and length extrapolation. In Proceedings of the synchronous grammars: Alignment by soft projec-
ThirdBlackboxNLPWorkshoponAnalyzingandIn- tion of syntactic dependencies. In Proceedings on
|     |     |     |     |     |     |     | the Workshop |     | on Statistical |     | Machine | Translation, |     |

terpretingNeuralNetworksforNLP,pages276–291,
pages23–30.
Online.AssociationforComputationalLinguistics.
|            |      |         |               |       |        |        | MitchellStern,JacobAndreas,andDanKlein.2017. |            |        |              |     |         | A   |

| Maxwell I  | Nye, | Armando | Solar-Lezama, |       | Joshua | B      |                                              |            |        |              |     |         |     |
|            |      |         |               |       |        |        | minimal                                      | span-based | neural | constituency |     | parser. | In  |
| Tenenbaum, | and  | Brenden | M             | Lake. | 2020.  | Learn- |                                              |            |        |              |     |         |     |
ing compositional rules via neural program synthe- Proceedings of the 55th Annual Meeting of the As-
|     |     |     |     |     |     |     | sociation | for | Computational |     | Linguistics | (Volume | 1:  |

sis. arXivpreprintarXiv:2003.05562.
|     |     |     |     |     |     |     | Long | Papers), | pages 818–827, |     | Vancouver, |     | Canada. |

AssociationforComputationalLinguistics.
InbarOren,JonathanHerzig,NitishGupta,MattGard-
| ner, and    | Jonathan       | Berant.  | 2020.      | Improving |              | com- |              |          |                                   |     |             |          |      |

|             |                |          |            |           |              |      | Alane Suhr,  | Ming-Wei | Chang,                            |     | Peter Shaw, | and      | Ken- |
| positional  | generalization |          | in         | semantic  | parsing.     | In   |              |          |                                   |     |             |          |      |
|             |                |          |            |           |              |      | tonLee.2020. |          | Exploringunexploredgeneralization |     |             |          |      |
| Proceedings | of             | the 2020 | Conference |           | on Empirical |      |              |          |                                   |     |             |          |      |
|             |                |          |            |           |              |      | challenges   | for      | cross-database                    |     | semantic    | parsing. | In   |
MethodsinNaturalLanguageProcessing:Findings,
Proceedingsofthe58thAnnualMeetingoftheAsso-
pages2482–2495.
|     |     |     |     |     |     |     | ciation | for Computational |     | Linguistics, |     | pages | 8372– |

8388.
| Hoifung Poon, | Colin | Cherry, | and | Kristina | Toutanova. |     |     |     |     |     |     |     |     |

2009. Unsupervised morphological segmentation Lappoon R Tang and Raymond J Mooney. 2001. Us-
| with log-linear |               | models. | In  | Proceedings | of     | Human   |              |     |                     |          |     |             |       |

|                 |               |         |     |             |        |         | ing multiple |     | clause constructors |          | in  | inductive   | logic |
| Language        | Technologies: |         | The | 2009        | Annual | Confer- |              |     |                     |          |     |             |       |
|                 |               |         |     |             |        |         | programming  |     | for semantic        | parsing. |     | In European |       |
enceoftheNorthAmericanChapteroftheAssocia-
|          |               |     |              |     |                |     | Conference |     | on Machine | Learning, | pages | 466–477. |     |

| tion for | Computational |     | Linguistics, |     | pages 209–217, |     |            |     |            |           |       |          |     |
Springer.
| Boulder,     | Colorado. | Association |     | for | Computational |     |                                               |     |                 |     |          |       |         |

| Linguistics. |           |             |     |     |               |     | IuliaTurc,Ming-WeiChang,KentonLee,andKristina |     |                 |     |          |       |         |
|              |           |             |     |     |               |     | Toutanova.                                    |     | 2019. Well-read |     | students | learn | better: |
ColinRaffel,NoamShazeer,AdamRoberts,Katherine
|             |         |     |         |         |       |       | On the | importance | of  | pre-training | compact |     | models. |

| Lee, Sharan | Narang, |     | Michael | Matena, | Yanqi | Zhou, |        |            |     |              |         |     |         |
arXivpreprintarXiv:1908.08962.
| Wei Li, | and Peter | J   | Liu. 2020. | Exploring |     | the lim- |     |     |     |     |     |     |     |

its of transfer learning with a unified text-to-text Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
transformer. JournalofMachineLearningResearch, Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
21:1–67. Kaiser, and Illia Polosukhin. 2017. Attention is all
|                                |     |     |     |               |     |     | you need. | In  | Advances | in neural | information |     | pro- |

| SujithRaviandKevinKnight.2009. |     |     |     | Minimizedmod- |     |     |           |     |          |           |             |     |      |
cessingsystems,pages5998–6008.
| elsforunsupervisedpart-of-speechtagging. |     |     |     |     |     | InPro- |     |     |     |     |     |     |     |

ceedingsoftheJointConferenceofthe47thAnnual Yuk Wah Wong and Raymond Mooney. 2007. Learn-
Meeting of the ACL and the 4th International Joint ing synchronous grammars for semantic parsing
ConferenceonNaturalLanguageProcessingofthe with lambda calculus. In Proceedings of the 45th
AFNLP,pages504–512,Suntec,Singapore.Associ-
AnnualMeetingoftheAssociationofComputational
| ationforComputationalLinguistics. |     |     |     |     |     |     | Linguistics,pages960–967. |     |     |     |     |     |     |

MarcoTulioRibeiro,TongshuangWu,CarlosGuestrin, YukWahWongandRaymondJMooney.2006. Learn-
and Sameer Singh. 2020. Beyond accuracy: Be- ing for semantic parsing with statistical machine
havioraltestingofNLPmodelswithCheckList. In translation. In Proceedings of the main conference
Proceedingsofthe58thAnnualMeetingoftheAsso- onHumanLanguageTechnologyConferenceofthe
ciation for Computational Linguistics, pages 4902– NorthAmericanChapteroftheAssociationofCom-
4912, Online. Association for Computational Lin- putational Linguistics, pages 439–446. Association
| guistics. |     |     |     |     |     |     | forComputationalLinguistics. |     |     |     |     |     |     |

Daniel H Younger. 1967. Recognition and parsing of
context-freelanguagesintimen3. Informationand
control,10(2):189–208.
Tao Yu, Rui Zhang, Kai Yang, Michihiro Yasunaga,
Dongxu Wang, Zifan Li, James Ma, Irene Li,
Qingning Yao, Shanelle Roman, Zilin Zhang,
and Dragomir Radev. 2018. Spider: A large-
scale human-labeled dataset for complex and cross-
domain semantic parsing and text-to-SQL task. In
Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing, pages
3911–3921, Brussels, Belgium. Association for
ComputationalLinguistics.
John M Zelle and Raymond J Mooney. 1996. Learn-
ing to parse database queries using inductive logic
programming. In Proceedings of the thirteenth na-
tionalconferenceonArtificialintelligence-Volume2,
pages1050–1055.
Luke Zettlemoyer and Michael Collins. 2007. Online
learningofrelaxedccggrammarsforparsingtolog-
ical form. In Proceedings of the 2007 Joint Con-
ferenceonEmpiricalMethodsinNaturalLanguage
Processing and Computational Natural Language
Learning(EMNLP-CoNLL),pages678–687.
LukeSZettlemoyerandMichaelCollins.2005. Learn-
ingtomapsentencestologicalform:structuredclas-
sificationwithprobabilisticcategorialgrammars. In
Proceedings of the Twenty-First Conference on Un-
certainty in Artificial Intelligence, pages 658–666.
AUAIPress.
Hao Zheng and Mirella Lapata. 2020. Compositional
generalizationviasemantictagging. arXivpreprint
arXiv:2010.11818.


Appendix one-to-one alignment between source and target
non-terminals(SmithandEisner,2006).
Weorganizetheappendixintotwosections:
Compositionality Notably, grammar for-
• AdditionaldetailsforNQGinAppendixA.
malisms such SCFGs and QCFGs capture the
• Additionalexperimentaldetailsandanalysis formalnotionoftheprincipleofcompositionality
inAppendixB. as a homomorphism between source and target
structures (Montague, 1970; Janssen and Partee,
A NQGDetails
1997).
In this section we describe the NQG grammar
A.2 NQGGrammarInductionDetails
induction algorithm and parsing model in detail,
Having defined the codelength scoring function
startingwithrelevantbackgroundandnotationfor
thatweusetocomparegrammarsinsection4.1.1,
QCFGs.
wedescribeourgreedysearchalgorithmthatfinds
A.1 Background: SCFGsandQCFGs agrammarthatapproximatelyminimizesthisob-
jective.14
Synchronous Context-Free Grammars (SCFGs)
havebeenusedtomodelthehierarchicalmapping Initialization We initialize R to be {NT →
betweenpairsofstringsinareassuchascompiler (cid:104)x,y(cid:105) | x,y ∈ D}. We also add identity rules
theory (Aho and Ullman, 1972) and natural lan- for substrings that exactly match between source
guageprocessing. andtargetexamples,e.g. NT → (cid:104)k,k(cid:105)wherek is
Informally, SCFGs can be viewed as an exten- asubstringofbothxandyforsomex,y ∈ D.15
sion of Context-Free Grammars (CFGs) that syn-
OptimizationAlgorithm Ouralgorithmwasde-
chronously generate strings in both a source and
signedwithsimplicityinmind,andthereforeuses
targetlanguage. WewriteSCFGrulesas:
a simple greedy search process that could likely
S → (cid:104)α,β(cid:105) be significantly improved upon by future work.
At a high level, our greedy algorithm iteratively
Where S is a non-terminal symbol, and α and β identifies a rule to be added to R that decreases
arestringsofnon-terminalandterminalsymbols. the codelength by enabling ≥ 1 rules in R to be
An SCFG rule can be viewed as two CFG rules, removed while maintaining the invariant that G
S → α and S → β with a pairing between the allows for deriving all of the training examples,
occurrences of non-terminal symbols in α and β. i.e. (cid:104)NT,NT(cid:105) ⇒ ∗ (cid:104)x,y(cid:105)foreveryx,y ∈ D. The
This pairing is indicated by assigning each non- searchcompleteswhennorulethatdecreasesL(R)
terminalinαandβ anindex∈ N. Non-terminals canbeidentified.
sharingthesameindexarecalledlinked. Following Todescribetheimplementation,firstletusdefine
convention,wedenotetheindexforanon-terminal severaloperationsoverrulesandsetsofrules. We
using a boxed subscript, e.g. NT [1] . A complete define the set of rules that can be derived from a
SCFGderivationisapairofparsetrees,oneforthe givensetofrules,R:
source language and one for the target language.
∗
d(R) = {NT → (cid:104)α,β(cid:105) | (cid:104)NT,NT(cid:105) ⇒ (cid:104)α,β(cid:105)}
AnexamplederivationisshowninFigure 4.
The ⇒r operator refers to a derives relation,
We define an operation SPLIT that generates
such that (cid:104)α1,β1(cid:105) ⇒r (cid:104)α2,β2(cid:105) states that the
possiblechoicesforsplittingaruleinto2rules:
stringpair(cid:104)α2,β2(cid:105)canbegeneratedfrom(cid:104)α1,β1(cid:105)
by applying the rule r. We write ⇒ to leave the SPLIT(NT → (cid:104)α,β(cid:105)) = {g,h |
ruleunspecified,assumingthesetofpossiblerules (cid:104)NT,NT(cid:105) ⇒g⇒h (cid:104)α,β(cid:105)∨
isclearfromcontext. Wewrite⇒⇒toindicatea
(cid:104)NT,NT(cid:105) ⇒h⇒g (cid:104)α,β(cid:105)},
chainof2ruleapplications,omittingtheinterme-
∗
diatestringpair. Finally,wewrite⇒todenotethe 14Theinductionobjectivecontainshyperparametersrepre-
reflexivetransitiveclosureof⇒. sentingthebitlengthofterminalandnon-terminalsymbols.
Forallexperimentsweusel
N
= 1. For GEOQUERY and
Quasi-Synchronous Context-Free Grammars SPIDERweusel T =8,andusel T =32forSCAN.
15TheseinitializationrulesareusedforGEOQUERYand
(QCFGs) QCFGsgeneralizeSCFGsinvarious
SPIDER,butSCANdoesnotcontainanyexacttokenoverlap
ways, notably relaxing the restriction on a strict betweensourceandtargetlanguages.


NT →(cid:104)howmanyNT passthroughNT ,answer(count(intersection(NT ,loc_1(NT ))))(cid:105)
|     |     | [1] |     | [2] |     |     |     |     | [1] |     | [2] |     |     |

NT →(cid:104)rivers,river(cid:105)
| NT →(cid:104)thelargestNT |     | ,largest(NT |     | )(cid:105) |     |     |     |     |     |     |     |     |     |

|                           |     | [1]         |     | [1]        |     |     |     |     |     |     |     |     |     |
NT →(cid:104)state,state(cid:105)
NT
|     |     |     |     | how | many NT | pass | through |     | NT      |     |     |     |     |

|     |     |     |     |     |         | [1]  |         |     |         | [2] |     |     |     |
|     |     |     |     |     | rivers  |      |         | the | largest | NT  |     |     |     |
[1]
NT
state
|     |     | answer ( | count | ( intersection | ( NT  |     | , loc_1 | (       | NT  |        | ) ) ) | )   |     |

|     |     |          |       |                |       | [1] |         |         |     | [2]    |       |     |     |
|     |     |          |       |                | river |     |         | largest | (   | NT [1] | )     |     |     |
state
Figure4: AnexampleQCFGderivation. Eachnon-terminalinthesourcederivation(blue)correspondstoanon-
terminalinthetargetderivation(green). TheQCFGrulesusedinthederivationareshownabove.
where g and h is a pair of new rules that would Wecanthendefinethecodelengthreductionof
∗
maintain the invariant that (cid:104)NT,NT(cid:105) ⇒ (cid:104)x,y(cid:105) adding a particular rule, −∆L(R,f) = L(R)−
for every x,y ∈ D, even if the provided rule is L(R(cid:48))whereR(cid:48) = (R ∪ f)\ELIM(R,f).17 Fi-
eliminated.16
nally,wecanselecttherulewiththelargest−∆L:
| SPLIT     | can | be implemented |     | by    | consider- |     |        |     |     |        |          |     |     |

|           |     |                |     |       |           |     | MAX(R) |     | =   | argmax | −∆L(R,f) |     |     |
| ing pairs | of  | sub-strings    | in  | α and | β to re-  |     |        |     |     |        |          |     |     |
f∈NEW(R)
| place with | a   | new indexed |     | non-terminal | sym- |     |     |     |     |     |     |     |     |

bol. For example, the rule “NT → Conceptually,afterinitialization,thealgorithm
thenproceedsas:
(cid:104)largeststate,largest(state)(cid:105)”canbesplitintothe
| rules “NT | →                                 | (cid:104)largest | NT                 | ,largest( | NT )(cid:105)” |     |       |            |     |     |      |     |     |

|           |                                   |                  | [1]                |           | [1]            |     | while | |NEW(R)|   |     | >   | 0 do |     |     |
| and“NT    | → (cid:104)state,state(cid:105)”. |                  | Thisstepcanrequire |           |                |     |       |            |     |     |      |     |     |
|           |                                   |                  |                    |           |                |     |       | r ← MAX(R) |     |     |      |     |     |
re-indexingofnon-terminals.
|        |            |         |     |               |       |     |     | −∆L(R,r) |     | < 0 |      |     |     |

|        |            |         |     |               |       |     |     | if       |     |     | then |     |     |
| During | our greedy | search, |     | we only split | rules |     |     |          |     |     |      |     |     |
break
| when one | of the | two resulting |     | rules can | already |     |     |     |     |     |     |     |     |

endif
| bederivedgivenR. |                                   | Therefore, |     | wedefineafunc- |     |     |     |     |      |              |     |     |     |

|                  |                                   |            |     |                |     |     |     | R ← | (R ∪ | r)\ELIM(R,r) |     |     |     |
| tionNEW          | thatreturnsasetofcandidaterulesto |            |     |                |     |     |     |     |      |              |     |     |     |
endwhile
consider:
|     |     | NEW(R) | =   |     |     |     |                 |     |     |        |              |     |       |

|     |     |        |     |     |     |     | For efficiency, |     | we  | select | the shortest | N   | exam- |
{g | g,h ∈ SPLIT(f)∧f ∈ R∧h ∈ d(R)} ples from the training dataset, and only consider
|     |     |     |     |     |     | these | during |     | the induction |     | procedure. | Avoiding |     |

Similarly,wecancomputethesetofrulesthat
|     |     |     |     |     |     | longer |     | examples | is  | helpful | as the number | of  | can- |

aremaderedundantandcanbeeliminatedbyintro-
didatesreturnedbySPLITispolynomialwithre-
ducingonethesecandidaterules,f:
|     |     |           |     |     |     | specttosourceandtargetlength. |       |           |        |            | Onceinduction |           |     |

|     |     | ELIM(R,f) |     | =   |     |                               |       |           |        |            |               |           |     |
|     |     |           |     |     |     |                               | 17The | last term | of the | codelength | objective     | described | in  |
{h | f,g ∈ SPLIT(h)∧g ∈ d(R)∧h ∈ R} section 4.1.1 is related to the increase in the proportion of
incorrectderivationsduetointroducingf.Ratherthancom-
16WeoptionallyallowSPLITtointroducerepeatedtarget putingthisexactly,weestimatethisquantitybysamplingup
non-terminalswhenthetargetstringhasrepeatedsubstrings. tok examplesfromDthatcontainallofthesub-stringsof
Otherwise, we do not allow SPLIT to replace a repeated sourceterminalsymbolsinf suchthatf couldbeusedina
substringwithanon-terminal,asthiscanleadtoanambiguous derivation,andestimatingtheincreaseinincorrectderivations
choice.WeenablethisoptionforSCANandSPIDERbutnot overthissampleonly. Wesamplek = 10examplesforall
| forGEOQUERY,asFunQLdoesnotrequiresuchrepetitions. |     |     |     |     |     | experiments. |     |     |     |     |     |     |     |

has completed, we then determine which of the for T5 and NQG based on random splits of the
longer examples cannot be derived based on the training sets for GEOQUERY and SPIDER. We
setofinducedrules,andaddrulesfortheseexam- used the same hyperparameters for all splits of a
| ples.18 |     |     |     |     |     |     | givendataset. |     |     |     |     |     |

Ouralgorithmmaintainsasignificantamountof ForT5,weselectedalearningrateof1e−4 from
[1e−3,1e−4,1e−5],
statebetweeniterationstocachecomputationsthat which we used for all experi-
arenotaffectedbyparticularrulechanges,based ments. Otherwise,weusedthedefaulthyperparam-
onoverlapinterminalsymbols. Wedevelopedthe etersforfine-tuning. Wefine-tunefor3,000steps
algorithmandselectedsomehyperparametersby forGEOQUERYand10,000forSPIDER. T5-Base
assessing the size of the induced grammars over trainedwithalearningrateof1e−4
reached94.2%
thetrainingsetsof SCAN and GEOQUERY. accuracy at 3,000 steps on a random split of the
Ourgrammarinductionalgorithmissimilarto standard GeoQuery training set into 500 training
the transduction grammar induction method for and100validationexamples.
| machine |     | translation | by Saers | et  | al. (2013). | More |         |     |        |        |     |              |

|         |     |             |          |     |             |      | For the | NQG | neural | model, | we  | use the pre- |
broadly,compression-basedcriteriahavebeensuc- trained BERT Tiny model of Turc et al. (2019)
cessfullyusedbyavarietyofmodelsforlanguage (4.4M parameters) for SCAN and SPIDER, and
| (Grünwald, |     | 1995; | Tang | and Mooney, | 2001; | Ravi |                               |     |     |     |     |           |

|            |     |       |      |             |       |      | BERTBase(110.1Mparameters)for |     |     |     |     | GEOQUERY, |
andKnight,2009;Poonetal.,2009). wherethereismoreheadroomforimprovedscor-
|     |     |     |     |     |     |     | ing. We | do not | freeze | pre-trained | BERT | parame- |

A.3 NQGParsingModelDetails
|     |     |     |     |     |     |     | ters during | training. |     | For all | experiments, | we use |

Inthissectionweprovidedetailsonhowwegener- d = 256dimensionsforcomputinganchoredrule
atederivationscores,s(z,x),usinganeuralmodel, scores. Wefine-tunefor256stepsandusealearn-
| as  | introduced | in  | § 4.1. The | derivation |     | scores de- |                |     |                       |     |     |     |

|     |            |     |            |            |     |            | ingrateof1e−4. |     | Weuseabatchsizeof256. |     |     |     |
composeoveranchoredrulesfromourgrammar:
|     |     |     |     |     |     |     | WetrainNQGon8V100GPUs. |     |     |     | TrainingNQG |     |

takes<5minutesforSCANandSPIDER(BERT
(cid:88)
|     |     | s(z,x) | =   | φ(r,i,j,x), |     |     |     |     |     |     |     |     |

Tiny),andupto90minutesforGEOQUERY(BERT
(r,i,j)∈z
|     |     |     |     |     |     |     | Base). | We fine-tune |     | T5 on | 32 Cloud | TPU v3 |

cores.19
wherer isanindexforaruleinG andiandj are For GEOQUERY, fine-tuning T5 takes
indicesdefiningtheanchoringinx. Theanchored approximately 5 and 37 hours for Base and 3B,
rule scores, φ(r,i,j,x), are based on contextual- respectively. For SPIDER, fine-tuning T5 takes
ized representations from a BERT (Devlin et al., approximately 5 and 77 hours for Base and 3B,
respectively.
2019)encoder:
(cid:124)
φ(r,i,j,x) = f ([w ,w ])+e f ([w ,w ]), B.2 DatasetPreprocessing
|       |     |        | s i               | j   | r r | i j      |               |     |     |     |             |        |

|       | [w  | ,w ]   |                   |     |     |          | For GEOQUERY, |     | we  | use | the version | of the |
| where |     | i j is | the concatenation |     | of  | the BERT |               |     |     |     |             |        |
representationsforthefirstandlastwordpiecein dataset with variable-free FunQL logical
the anchored span, f is a feed-forward network forms (Kate et al., 2005), and expand certain
r
|                                    |     |     |     |     |     | Rd,f | functions | based | on  | their | logical | definitions, |

| withhiddensizedthatoutputsavector∈ |     |     |     |     |     | s is |           |       |     |       |         |              |
afeed-forwardnetworkwithhiddensizedthatout- such that state(next_to_1(state(all)))
putsascalar,ande isanembedding∈ Rd forthe becomes the more conventional
r
next_to_1(state)).
ruleindexr. Ourformulationforencodingspans intersection(state,
issimilartothatusedinotherneuralspan-factored Wereplaceentitymentionswithplaceholders(e.g.
models(Sternetal.,2017;Leeetal.,2017). “m0”,“m1”)inboththesourceandtarget.
ForSPIDER,weprependthenameofthetarget
B ExperimentalDetails databasetothesourcesequence. ForT5,wealsose-
rializethedatabaseschemaasastringandappend
B.1 ModelHyperparametersandRuntime
|     |     |     |     |     |     |     | it to the | source | sequence | similarly | to  | Suhr et al. |

Weselectedreasonablehyperparametervaluesand
(2020). Thisschemastringcontainsthenamesof
| performed |     | some | minimal | hyperparameter |     | tuning |            |        |           |     |           |        |

|           |     |      |         |                |     |        | all tables | in the | database, | and | the names | of the |
18WeuseN = 500for SCAN andN = 1000for SPI- columns for each table. As we use a maximum
DER.AstheGEOQUERYtrainingsetcontains<500unique
examples,weusetheentiretrainingset. 19https://cloud.google.com/tpu/


Source:howmanystatesarenexttomajorrivers
Target: answer ( count ( intersection ( state , next_to_2 ( intersection ( major ,
river ) ) ) ) )
Prediction: answer ( count ( intersection ( state , next_to_2 ( intersection ( major ,
intersection ( river , m0 ) ) ) ) ) )
Notes: Thetrigram“major , intersection”occurs28timesduringtraining,but“major , river”
occurs0times.Inthiscase,T5alsohallucinates“m0”despitenoentityplaceholderoccuringthesource.
Source:whichstatehasthehighestpeakinthecountry
Target:answer ( intersection ( state , loc_1 ( highest ( place ) ) ) )
Prediction:answer ( highest ( intersection ( state , loc_2 ( highest ( intersection (
mountain , loc_2 ( m0 ) ) ) ) ) )
Notes:Thetoken“highest”occursafter“answer (”in83%ofinstancesinwhich“highest”occursin
thetrainingset.NotethatT5alsohallucinates“m0”inthiscase.
Table7: ExamplepredictionerrorsforT5-BasefortheGEOQUERYTMCDsplit.
Dataset Examples InducedRules Ratio B.4 GrammarSizes
SCAN 16727 21 796.5 Inducedgrammarsizesforaselectedsplitofeach
GEOQUERY 600 234 2.6
dataset are shown in Table 8. For SPIDER, the
SPIDER-SSP 3282 4155 0.79
number of induced rules is larger than the origi-
Table8: Sizesofinducedgrammars. nal dataset due to the identity rules added during
initialization.
Std. Templ. Len. TMCD
B.5 GEOQUERYVariance
NQG-T5-3BAcc. 0.6 1.2 1.2 0.4
Intables2and5wereportthemeanof3runsfor
NQG-T5-BaseAcc. 0.5 1.4 1.1 0.4
NQGAcc. 1.2 4.5 1.5 0.4 NQGfor GEOQUERY. Thestandarddeviationsfor
NQGCoverage 0.7 3.4 1.8 0.1 these runs are reported in Table 9. The reported
NQGPrecision 0.7 1.9 1.7 1.2 standarddeviationsforNQG-T5usethesamefine-
tuned T5 checkpoint, so they do not reflect any
Table9: StandarddeviationofNQGforGEOQUERY.
additional variance from different fine-tuned T5
checkpoints.
source sequence length of 512 for T5, this leads
B.6 T5 GEOQUERYErrors
tosomeschemastringsbeingtruncated(affecting
WeincludeseveralexampleT5-Baseerrorsonthe
about5%oftrainingexamples).
GEOQUERYTMCDsplitinTable7.
SCAN didnotrequireanydataset-specificpre-
processing.
B.3 AtomandCompoundDefinitions
For GEOQUERY, the tree structure of FunQL is
given by explicit bracketing. We define atoms
asindividualFunQLsymbols,andcompoundsas
combinations between parent and child symbols
in the FunQL tree. Example atoms are longest,
river,andexcludeandexamplecompoundsare
longest(river)andexclude(longest(_), _).
For SPIDER, we tokenize the SQL string and
defineatomsasindividualtokens. Todefinecom-
pounds, we parse the SQL string using an unam-
biguousCFG,anddefinecompoundsfromthere-
sultingparsetree. Wedefinecompoundsoverboth
firstandsecondorderedgesintheresultingparse
tree.

---
**Source PDF:** `2023_48_article.pdf`
