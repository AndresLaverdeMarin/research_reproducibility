|     | Bad | Seeds:             | Evaluating        |     |     | Lexical | Methods       | for               | Bias Measurement |     |     |     |

|     |     |                    | MariaAntoniak     |     |     |         |               | DavidMimno        |                  |     |     |     |
|     |     |                    | CornellUniversity |     |     |         |               | CornellUniversity |                  |     |     |     |
|     |     | maa343@cornell.edu |                   |     |     |         |               | mimno@cornell.edu |                  |     |     |     |
|     |     |                    |                   |     |     |         | TargetConcept |                   | HighlightedSeeds |     |     |     |
Abstract
|     |     |     |     |     |     |     | Unpleasant |     | divorce,jail,poverty,cancer,... |     |     |     |

A common factor in bias measurement meth- AfricanAmerican Tanisha,Tia,Lakisha,Latoya,...
ods is the use of hand-curated seed lexicons, DomesticWork mom,mum,...
butthereremainslittleguidancefortheirselec-
|     |     |     |     |     |     |     | Ugliness |     | fat,chubby,obese,fatty, |     |     |     |

tion.Wegatherseedsusedinpriorwork,docu-
overweight,disformed,disfigured,
|     | mentingtheircommonsourcesandrationales, |              |          |                  |       |     |          |          | wrinkle,wrinkled,... |       |      |           |

|     | and in                                  | case studies | of three | English-language |       |     |          |          |                      |       |      |           |
|     | corpora,                                | we enumerate |          | the different    | types | of  |          |          |                      |       |      |           |
|     |                                         |              |          |                  |       |     | Table 1: | Examples | of real seed         | terms | used | in recent |
socialbiasesandlinguisticfeaturesthat,once
worktomeasurebiasesincorpora.
|     | encoded            | in the seeds, |       | can affect | subsequent |        |     |     |     |     |     |     |

|     | bias measurements. |               | Seeds | developed  |            | in one |     |     |     |     |     |     |
contextareoftenre-usedinothercontexts,but
documentation and evaluation remain neces- questions about the biases in a corpus and its au-
sary precursors to relying on seeds for sensi- thors. This work often involves comparing bias
tivemeasurements.
measurementsacrossdifferentcorpora,whichre-
quiresreliable,fine-grainedmeasurements.
## 1 Introduction
|     |     |     |     |     |     |     | While | there | is a wide | range | of bias | measure- |

TherehasbeenincreasingconcernintheNLPcom- ment methods, every one of them relies on lexi-
consofseedtermstospecifystereotypesordimen-
munityoverbiasandstereotypescontainedinmod-
|     |         |              |     |             | downstream |     | sions of | interest. | But the | rationale | for | choosing |

| els | and how | these biases |     | can trickle |            |     |          |           |         |           |     |          |
to practical applications, such as serving job ad- specific seeds is often unclear; sometimes seeds
arecrowd-sourced,sometimeshand-selectedbyre-
| vertisements. |     | In particular, |     | there | has been | much |     |     |     |     |     |     |

searchers,andsometimesdrawnfrompriorwork
recentscrutinyofwordrepresentations,withmany
studiesfindingharmfulassociationsencodedinem- in thesocial sciences. The impactof the seeds is
beddingmodels. Combatingsuchbiasesrequires notwell-understood,andmanypreviousseedsets
|     |     |     |     |     |     |     | haveseriouslimitations. |     | AsshowninTable1,the |     |     |     |

measuringthebiasencodedinamodelsothatre-
|           |     |               |               |     |     |          | seeds used | for | bias measurement |     | can themselves |     |

| searchers |     | can establish | improvements, |     |     | and many |            |     |                  |     |                |     |
variants of embedding-based measurement tech- exhibit cultural and cognitive biases (e.g., reduc-
tivedefinitions),andinaddition,linguisticfeatures
niqueshavebeenproposed(Bolukbasietal.,2016;
oftheseeds(e.g.,frequency)canaffectbiasmea-
Caliskanetal.,2017;Manzinietal.,2019).
Thesemeasurementshavehadtheadditionalup- surements(Ethayarajhetal.,2019). Thoughthey
stream benefit of providing computational social areoftenre-used,thesuitabilityoftheseseedsto
novelcorporaisuncertain,andwhileevaluations
scienceanddigitalhumanitiesscholarswithanew
sometimesincludepermutationtests,distinctsets
meansofquantifyingbiasindatasetsofsocial,po-
litical,orliteraryinterest. Researchersincreasingly ofseedsarerarelycompared.
useembeddings(Gargetal.,2018;Knocheetal., Weuseamixtureofliteraturesurvey,qualitative
2019a;Hoyleetal.,2019)andotherlexicon-based analysis of seed terms, and analytic methods to
methods (Saez-Trumper et al., 2013; Fast et al., exploretheuseofseedsetsforbiasmeasurement
2016;Rudingeretal.,2017)toprovidequantitative through two overarching research questions. (1)
answers to otherwise elusive political and social Weexplorehowseedsareselectedandfromwhich
1889
Proceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguistics
andthe11thInternationalJointConferenceonNaturalLanguageProcessing,pages1889–1904
August1–6,2021.©2021AssociationforComputationalLinguistics

sourcestheyaredrawntobetterunderstandratio- andacombinationofoddsratios,embeddings,and
nales and assumptions underlying common seed crowd-sourcing (Fast et al., 2016). All of these
sets. (2) We explore which features of seeds can methods rely on sets of seed terms. While much
causeinstability,includingbothsocialbiasesand recentNLPworkhasfocusedoncontextualembed-
linguisticdimensionsinouranalysis. dings,mostrecentbias-detectionworkhasfocused
Ourworkprovidesthefollowingcontributions. on vocabulary-based embeddings and word rep-
Documentation: Wedocumentandtest178seed resentations. Researchershave increasingly used
setsusedinpriorwork,andwereleasethisdocu- embedding-basedmethodstomeasurebiasesand
mentation as a resource for the research commu- drawcomparisonsintrainingcorporaofsocialin-
| nity.1 |           |     |            |              |        | terest (Kim | et al., | 2014; | Hamilton | et  | al., 2016; |

|        | Analysis: |     | We provide | a systematic | frame- |             |         |       |          |     |            |
work for understanding the different sources of Kulkarni et al., 2016; Phillips et al., 2017; Ko-
instabilityinseedsetsthatcanaffectbiasmeasure- zlowski et al., 2019). For example, Bhatia et al.
ments. We compare the gathered seeds to larger (2018)trainembeddingmodelsonnewssourcesto
setsofartificiallycreatedseedsets,andweinvesti- comparetraitassociationsforpoliticalcandidates.
gatethereliabilityofseedtermsusedfortwopopu- Webelievethatourresultsshouldextendtocontex-
larembedding-basedbiasmeasurementmethodsin tualembeddingmethods(Zhaoetal.,2019;Sedoc
casestudiesonthreedatasets. Recommendations: and Ungar, 2019), but vocabulary-based embed-
Withthislargerperspective,wediscusshowseed dingsareeasiertoanalyze.
setsshouldbeexaminedversushowthesesetsare We discuss several recent studies that include
popularlyconsideredandwhatkindofdocumenta- analysisofseedsets(Kozlowskietal.,2019;Etha-
tionbestpracticesshouldbefollowed. Seedsarea yarajhetal.,2019;SedocandUngar,2019)in§8.
brittlebutunavoidableelementofcurrentbiasmea-
surement algorithms, with weaknesses that need 3 DataDescription
probingevenforembedding-basedmeasurements.
|     |     |     |     |     |     | Training | Corpora. | Our | dataset | choices | are |

## 2 BackgroundandRelatedWork guided by our focus on the upstream use case,
whereembeddingsaretrainedonrelativelysmall,
Theterm“bias”hasmanydefinitions,fromavalue-
|     |     |     |     |     |     | special-purpose |     | collections | to  | answer social | and |

neutralmeaninginstatisticstoamorenormative humanistquestionsaboutthetrainingcorpus. The
| meaninginsocio-culturalstudies. |     |     |     | Inthebiasmea- |     |     |     |     |     |     |     |

scopeofthesedatasetsfitstheusecaseofasocial
surementliteratureinNLP,lackofprecisedefini-
scientistinterestedinmeasuringbiasduringasmall
tions and problem specifications (Blodgett et al., timewindow,acrossspecificgenres,orinapartic-
2020) has led to many of the errors we explore ularsetofauthors. Table2showsanoverviewof
| in  | this paper. | In  | general, | “bias” in | NLP most of- |     |     |     |     |     |     |

thedata,andmoredetailsareintheAppendix.
tenrepresentsharmfulprejudices(Caliskanetal.,
|     |     |     |     |     |     | Our datasets |     | include: | New | York Times | arti- |

2017) whose spurious and undesirable influence cles from April 15th-June 30th, 2016; high qual-
| canaffectmodeloutputs. |     |     |     | Whilethesedownstream |     |     |     |     |     |     |     |

ityWikiTextarticles,usingthefullWikiText-103
effectshaveinspiredworkon“removing”biasfrom
trainingset(Merityetal.,2016);andGoodreads
embeddingmodels(Bolukbasietal.,2016),there bookreviewsfortheromanceandhistoryandbi-
havealsobeencritiquesoftheseefforts(Gonenand
|     |     |     |     |     |     | ography | genres, | sampled | from | the UCSD | Book |

Goldberg,2019),andwedonotfocusonthisuse
Graph(WanandMcAuley,2018;Wanetal.,2019).
| caseinourstudy. |     |     | Instead, | wefocusonbiasmea- |     |     |     |     |     |     |     |

Foraddedvalidity,wealsoreplicateexistingstud-
surementasatoolusedindiversesettingstomake ies, using a pre-trained model on a large Google
comparisonsacrossspecificcorporaofinterest.
Newscorpus(Mikolovetal.,2013).
|      | Unsupervised |     | methods   | for bias | measurement |          |          |     |           |           |       |

|      |              |     |           |          |             | For each | dataset, | we  | lowercase | all text, | parse |
| have | included     |     | pointwise | mutual   | information |          |          |     |           |           |       |
andobtainPOStagsusingspaCy(Honnibaletal.,
(Rudinger et al., 2017), normalized frequencies 2020), tokenize the text into unigrams, and filter
| and | cosine | similarity | of  | TF-IDF weighted | word |     |     |     |     |     |     |

wordsthatoccurfewerthan10timesinthetraining
| vectors | (Saez-Trumper |     |     | et al., 2013), | generative |     |     |     |     |     |     |

dataset. Lowercasingcontrolsforthevaryinglevels
models (Joseph et al., 2017; Hoyle et al., 2019), of capitalization used in the gathered seeds. We
leaveanalysisofbigramseedstofutureworkand
1Seedsanddocumentationareavailableathttps://gi
thub.com/maria-antoniak/bad-seeds relyonunigramsasasimplifyingassumption.
1890

| Dataset |     |     |     |     | Total         |     | TotalWords     |     | VocabularySize     |     |     | Mean           |     |

|         |     |     |     |     | Documents     |     |                |     |                    |     |     | DocumentLength |     |
| NYT     |     |     |     |     | 8,888articles |     | 7,244,457words |     | 162,998uniquewords |     |     | 815words       |     |
WikiText 28,472articles 99,197,146words 546,828uniquewords 3,484words
Goodreads(Romance) 197,000reviews 24,856,924words 214,572uniquewords 126words
Goodreads(History/Biography) 136,000reviews 14,324,947words 163,171uniquewords 105words
Table2:Summarystatisticsforourtestdatasets.Incontrasttothelarge,genericdatasetsoftenusedfordownstream
applications,thesedatasetsaresmallandculturallyspecific.
|     |     |     |     |     |     |     |     | of these | seeds  | and the   | rationales | for          | using them |

|     |     |     |     |     |     |     |     | are not  | always | explained | by         | researchers, | but in     |
|     | 0   | 20  | 40  | 60  | 80  | 100 |     |          |        |           |            |              |            |
Number of Seeds per Set caseswherewewereabletodetermineasourceor
|     |     |     |       |     |     |     |     | rationale, | we                                   | group them | into | the following | cate- |

|     |     |     |       |     |     |     |     | gories.    | Table3overviewsthesourcefrequencies. |            |      |               |       |
|     | 0   | 5   | 10 15 | 20  | 25  | 30  | 35  |            |                                      |            |      |               |       |
Number of Sets per Paper We emphasize that each source comes with risks
andbenefits;thereisnoonecorrectmethodtose-
| Figure1: |     | Overviewofthegatheredseedsets,showing |     |     |     |     |     |     |     |     |     |     |     |

lectingseeds,butawarenessofprosandconscan
| quartiles |     | and medians. |     | Outliers | are truncated |     | on the |     |     |     |     |     |     |

helpguidedecisionsandevaluationmethods.
plotshowingthenumberofseedsperset;themaximum
numberis1,460seeds.
|     |     |     |     |     |     |     |     | Borrowed | from | Social | Sciences. | Seed | sets are |

oftenborrowedfrompriorworkinpsychologyand
|     | Corpus-Derived |     |     |     |     | 7/18papers |     |     |     |     |     |     |     |

othersocialsciences,usuallyinanefforttoeither
|     | Re-Used |     |     |     |     | 7/18papers |     |     |     |     |     |     |     |

BorrowedfromSocialSciences 6/18papers replicate results or build confidence from previ-
|     | Curated                     |     |     |     |     | 5/18papers |     |                     |     |     |                          |     |     |

|     |                             |     |     |     |     |            |     | ouslyvalidatedwork. |     |     | Forexample,Caliskanetal. |     |     |
|     | AdaptedfromLexicalResources |     |     |     |     | 3/18papers |     |                     |     |     |                          |     |     |
Crowd-Sourced 2/18papers (2017)validatepromptsfromtheImplicitAssocia-
Population-Derived 2/18papers tionTest(Greenwaldetal.,1998),whileGargetal.
(2018)andHoyleetal.(2019)usepersonalitytraits
|     | Table3: | Overviewofthesurveyedseedsources. |     |     |     |     |     |     |     |     |     |     |     |

fromWilliamsandBennett(1975);Williamsand
|          |     |       |       |           |     |      |      | Best (1977, |     | 1990). Sometimes |     | the seeds | appeal |

| Gathered |     | Seeds | Sets. | We gather | 178 | seed | sets |             |     |                  |     |           |        |
forvalidityviahighlycitedresources,likeLIWC
usedinarepresentativesampleof18highly-cited
|     |     |     |     |     |     |     |     | (Pennebaker |     | et al., 2001), | despite | critiques | about |

prior works on bias measurement. Seeds include unreliability(Panger,2016;Forscheretal.,2017).
bothembedding-basedandnon-embedding-based Borrowingseedsdoesnotabsolveresearchersfrom
biasdetectionmethodsasthereisoftencrossover
examiningandvalidatingseeds.
| andre-useofseedsets. |     |        |         | Becauseweusewordem- |     |     |        |                |     |        |     |           |             |

|                      |     |        |         |                     |     |     |        | Crowd-Sourced. |     | Custom |     | seed sets | can be cre- |
| bedding              |     | models | trained | on unigrams,        |     | we  | do not |                |     |        |     |           |             |
includebigramseedsinouranalysis,andineach ated through crowd-based annotation. Fast et al.
(2016)useMechanicalTurktovalidatetheinclu-
experiment,weomitwordsthatwerenotpresent
sionoftermsintheirseedsets;thefinaltermsare
| in  | our training | set. | While | these | choices | could | be  |     |     |     |     |     |     |

thenincludedinpackagedcodeforresearchersand
seenaslimitations,weseethemasrealisticappli-
cationsofseedstoconstraineddatasets,reflecting practitioners. Kozlowskietal.(2019)useMechan-
|     |     |     |     |     |     |     |     | ical Turk | to  | gather ratings | of  | items scaled | along |

thescenarioinwhichbiasesarecomparedacross
|                  |     |     |                              |     |     |     |     | gender, | race, | and class. | Crowd-sourcing |     | can aid |

| specificcorpora. |     |     | Figure1overviewstheseedsets, |     |     |     |     |         |       |            |                |     |         |
examplesusedinthepaperaredocumentedinthe ingatheringcontemporaryassociationsandstereo-
|           |     |         |      |            |     |        |        | types. | However,controllingforcrowddemograph- |     |     |     |     |

| Appendix, |     | and the | full | collection | is  | shared | in the |        |                                       |     |     |     |     |
icscanbedifficult,andcrowd-sourcingcanresult
supplementarymaterialsandisavailableonline.
|     |     |     |     |     |     |     |     | in alarming |     | errors, in | which | popular | stereotypes |

## 4 HowAreSeedsSelected?
arehard-codedintotheseeds(asinTable1).
Howdoresearchersselectseeds,andfromwhich Population-Derived. Someseedsetsarederived
sourcesaretheypopularlydrawn? Weexplorethis from government-collected population datasets.
question using the gathered seed sets from prior PopularsourcesincludeU.S.censusdata(Boluk-
worksonunsupervisedbiasdetection. Theorigins basietal.,2016;Caliskanetal.,2017),theU.S.Bu-
1891

reauofLaborStatistics(Caliskanetal.,2017),and Re-Used. Finally,manypapersrelyonpriorbias
theU.S.SocialSecurityAdministration(Gargetal., measurement research for seed terms. The most
2018). These sources are usually used to gather popularsourcesinoursurveyincludeearlypapers
namesandoccupationscommontocertaindemo- on bias in embeddings such as Bolukbasi et al.
graphic groups. These sources tend to be U.S.- (2016)andCaliskanetal.(2017). Thisrepetition
centric, though the training data for the embed- meansthattheseedsaretestedonmanydifferent
dingdoesnotalwaysmatch(e.g.,largeWikipedia datasets,buttheyshouldnotbetrustedwithoutval-
datasetsarenotguaranteedtohaveU.S.authors). idation;therecanbemismatchesinfrequencyand
Relianceonthesesourcesisparticularlyvulnerable contextualmeaningbetweendatasets.
toreductivedefinitionsofthetargetconcepts—e.g.,
|     |     |     |     |     |     |     | 5 BiasMeasurementAlgorithms |     |     |     |     |     |     |

gender(Keyes,2017)—andassumesaleveloftrust
andrepresentationinthedatacollectionthatmight
|     |     |     |     |     |     |     | In the upstream |     | use | case, | locally | trained | word |

notexistevenlyacrossgroups. embeddings remain state of the art because fine-
|         |      |         |            |     |      |      | tuned pre-trained |     | contextual   |     | models | might           | intro- |

| Adapted | from | Lexical | Resources. |     | Some | seed |                   |     |              |     |        |                 |        |
|         |      |         |            |     |      |      | duce extrinsic    |     | information, |     | and it | is not feasible |        |
setsaredrawnfromexistingdictionaries,lexicons,
topre-traincontemporarycontextualembeddings
andotherpublicresources,suchasSemEvaltasks
|          |            |     |            |     |       |         | on such | small | collections. |     | Here, | we focus | on  |

| (Zhao et | al., 2018) | and | ConceptNet |     | (Fast | et al., |         |       |              |     |       |          |     |
twopopularseed-basedmethodstodetectbiasin
2016). Pre-packagedsentimentlexiconsareapopu-
|     |     |     |     |     |     |     | word embeddings. |     | Bolukbasi |     | et  | al. (2016) | and |

larsource(Saez-Trumperetal.,2013;Sweeneyand
Caliskanetal.(2017)bothintroduceembedding-
Najafian,2019);theselexiconsincludetheAffec-
basedmethodsforbiasdetectionthatrelyonsets
tiveNormsforEnglishWords(ANEW)(Bradley
|                          |       |                       |     |                |           |     | of seed    | words.   | Each    | of these | methods | requires |         |

| and Lang,                | 1999) | and negative/positive |     |                | sentiment |     |            |          |         |          |         |          |         |
|                          |       |                       |     |                |           |     | two sets   | of seed  | words,  | X        | and     | Y, and   | one ad- |
| wordsfromHuandLiu(2004). |       |                       |     | Theseseedshave |           |     |            |          |         |          |         |          |         |
|                          |       |                       |     |                |           |     | ditionally | requires | matched |          | pairs   | of seed  | words   |
theadvantageofpreviousroundsofvalidation,but
|                                            |     |              |       |         |     |        | {(X ,Y   | ),(X      | ,Y ),...}. |              |     |             |     |

| thisdoesnotguaranteevalidityfornewdomains. |     |              |       |         |     |        | 1 1      | 2         | 2          |              |     |             |     |
|                                            |     |              |       |         |     |        | WEAT.    | Given     | a set      | of embedding |     | vectors     | w,  |
| Corpus-Derived.                            |     | Quantitative |       | methods |     | can be |          |           |            |              |     |             |     |
|                                            |     |              |       |         |     |        | the Word | Embedding |            | Association  |     | Test (WEAT) |     |
| used to extract                            |     | seed terms   | froma | corpus  | of  | inter- |          |           |            |              |     |             |     |
(Caliskanetal.,2017)definesavectorbasedonthe
est. Forexample,Saez-Trumperetal.(2013)use
differencebetweenthemeanvectorofthetwotar-
sortedlistsofnamedentitiesextractedfromatar-
getsets,andthenmeasuresthecosinesimilarityof
getdatasettocreateseedsetsforpersonasofinter-
|     |     |     |     |     |     |     | asetofattributewordstothatvector. |     |     |     |     | Thestrength |     |

est. Similarly,SweeneyandNajafian(2019)extract
|     |     |     |     |     |     |     | oftheassociationbetweenthetargetsetsX |     |     |     |     |     | andY, |

highfrequencyidentitytermsfromaWikipediacor-
andthesetsofattributes,A,andB,isgivenby
pus. Thesemethodshavetheadvantageofensuring
highfrequencytermsinthetargetdataset,butthey (cid:88) (cid:88)
|     |     |     |     |     |     |     | s(X,Y,A,B) | =   |     | s(x,A,B)− |     | s(y,A,B) |     |

posesimilarriskstocrowd-sourcing;unlessanex-
|     |     |     |     |     |     |     |     |     | x∈X |     |     | y∈Y |     |

traroundofcleaningandcurationiscompletedby
theresearchers,termswithunintendedeffectscan where s(w,A,B) is equal to the difference in av-
beincludedintheseedsets. erage cosine similarities between a query w and
|          |                                   |     |     |     |     |     | each term | in A | and | w and | each | term in | B. To |

| Curated. | Seedsetsaresometimeshand-selected |     |     |     |     |     |           |      |     |       |      |         |       |
testwhethertheresultingdifferences(X,Y,A,B)
| by the authors, |           | usually | after    | close    | reading | of the |                 |      |        |             |     |        |      |

|                 |           |         |          |          |         |        | is significant, | this | result | is compared |     | to the | same |
| corpus of       | interest. | For     | example, | Rudinger |         | et al. |                 |      |        |             |     |        |      |
functionappliedtorandomlypermutedsetsdrawn
| (2017) hand-select |     | a set | of seed | terms | that | corre- |       |       |                            |     |     |     |     |

|                    |     |       |         |       |      |        | fromX | andY. | Caliskanetal.(2017)useWEAT |     |     |     |     |
spondtoasetofdemographiccategoriesofinterest,
tomeasurestereotypicalassociationsbetweensets
andJosephetal.(2017)hand-selectasetofidentity
|     |     |     |     |     |     |     | of targets | and attributes, |     | where, | for | example, | the |

seedsbasedontheirfrequencyinaTwitterdataset.
targettermsmightbeartsandscienceterms,and
Often,evenwhenpapersrelyonotherseedsources,
theattributetermsmightbemaleandfemaleterms.
| manual curation |     | is included |     | as a step | in the | seed |     |     |     |     |     |     |     |

creationprocess. Hand-curationcanresultinhigh PCA. Theprincipalcomponentanalysis(PCA)
precision seeds, but this method relies on the au- method tests how much variability there is in the
thors’correctionfortheirownsocialbiases. difference vectors between pairs of word vectors
1892

| (Bolukbasi | et al., | 2016). | If the | vector | difference |     |     |     |     |     |     |     |

woman, women, she, her, her,...
(Kozlowski et al 2019)
betweenpairsofseedtermscanbeapproximated
sister, female, woman, girl, daughter,...
wellbyasingleconstantvectorc,thenthisvector (Caliskan et al 2017)
woman, girl, she, mother, gal,...
represents a bias subspace. In this case, the sub- sdeeS (Bolukbasi et al 2016)
woman, girl, mother, daughter, sister,...
| spaceissimplyaonedimensionalvector,though |     |     |     |     |     |     |     |     | (Hoyle et al 2019) |     |     |     |

lady, nun, heroine, actress, businesswoman,...
thisprocesscouldbeextendedtomoredimensions. (Zhao et al 2018)
Foreachpairofembeddingvectorscorresponding baker, counselor, nanny, librarians, socialite,...
(Zhao et al 2018)
| tooneseedwordfromsetX |     |     | andonefromsetY, |     |     |     |     |     |     |     |         |     |

|                       |     |     |                 |     |     |     |     |     |     |     | 0.0 0.2 | 0.4 |
Similarity to Unpleasantness Vector
Bolukbasietal.(2016)calculatethemeanvector
of those two vectors and then include the two re- romance history + biography
sultinghalfvectorsfromthatmeantothetwoseed
|     |     |     |     |     |     | Figure2: | Biasmeasurementsdependonseeds. |     |     |     |     | Wecal- |

vectorsascolumnsintheinputmatrix. culate the cosine similarities between different female
|     |     |     |     |     |     | seed | sets and | an averaged |     | upleasantness |     | vector from |

## 6 QuantifyingVariationfromSeeds
|     |     |     |     |     |     | two | embedding | models. | Results |     | are consistent | across |

seedsforromancereviewembeddings,butvarywidely
Toquantifyhowlargeaneffectseedfeaturescan
betweensetsforhistoryandbiography.Wefindsimilar
haveonbiasmeasurements,wecalculateasetof variationevenforapretrainedGoogleNewsmodel.
metricsforbothPCAandWEATmethodsthatsum-
marizeshowwellthebiassubspacerepresentsthe
tothebiassubspace,andwemeasuretheabsolute
| target seeds. | For | each dataset, |     | we use | the popu- |     |     |     |     |     |     |     |

lar skip-gramwith negativesampling (SGNS)al- differenceinmeanrankofthepairedseedsets:
| gorithm | to train a  | word2vec | model.      |       | We use the |     |             |     |     |     |       |     |

|         |             |          | (Rˇehu˚ˇrek |       |            |     | Coherence(X |     | ,Y  | ) = | |R −R | |,  |
| gensim  | package for | training |             |       | and Sojka, |     |             |     | 1   | 2   | 1     | 2   |
| 2010).  | We use a    | window   | size        | of 5, | a minimum  |     |             |     |     |     |       |     |
wordcountof10,andavectorsizeof100forall whereX 1 andY 2 areseedsetsandR 1 andR 2 are
|              |                                  |     |     |     |     | theirmeanranksinthebiassubspace. |     |     |     |     |     | Finally,we |

| experiments. | Werepeatthisprocessacross20boot- |     |     |     |     |                                  |     |     |     |     |     |            |
|              |                                  |     |     |     |     | normalizethescorestoa[0,1]range. |     |     |     |     |     | Higherco-  |
strappedsamplesofeachdataset.
ForPCA,wecalculatethedifferencevectorbe- herencescoresindicatethattheseedsetshavevery
tweentheembeddingvectorsforeachpairofwords differentmeanranks,i.e.,theseedsareseparated
|            |            |     |      |        |             | by more | of  | the vocabulary. |     | For | example, | in Fig- |

| in the two | seed sets. | For | each | set of | paired seed |         |     |                 |     |     |          |         |
sets,werunPCAandplotthepercentofvariance ure 4, ordered seeds (a) produce a subspace with
explained by each component. For the gathered greatercoherence(setsarefurtherapartinthebias
subspace)thanshuffledseeds(b).
| seeds, we | only use | pairings | documented |     | in prior |     |     |     |     |     |     |     |

work. Weperformamanualconfirmationthatthe
|                 |     |        |            |     |           | GeneratedSeedSets. |     |     |     | Inordertocontrolforfre- |     |     |

| first component | g   | indeed | represents | the | bias sub- |                    |     |     |     |                         |     |     |
quencyandPOSwhenmeasuringinstabilitiesdue
spacebyrankingallthewordsinthevocabularyby
tosemanticsimilarityandwordorder,wegenerate
theircosinesimilaritytog.
alargecollectionofartificial,randomizedseedsets.
ForWEAT,weholdtheattributetermsconstant,
Weselectatargettermatrandomfromthemodel’s
| whereA | = [“good”]andB |     | =   | [“bad”],whileour |     |     |     |     |     |     |     |     |

vocabulary,filteredbyPOS.Eachseedsetconsists
| generated | seed sets      | take        | the           | place of | the target |                           |        |      |         |                     |         |            |

|           |                |             |               |          |            | of this                   | target | term | and its | four                | nearest | neighbors, |
| terms X   | and Y. Holding |             | the attribute |          | terms con- |                           |        |      |         |                     |         |            |
|           |                |             |               |          |            | rankedbycosinesimilarity. |        |      |         | Werepeatthisprocess |         |            |
| stant isa | simplifying    | assumption; |               | ourgoal  | is not     |                           |        |      |         |                     |         |            |
foreachofthemodelstrainedonthebootstrapped
totestallpossibleattributetermsbuttoshowthat
|                                 |     |     |     |                 |     | samples | of  | the corpus. | We  | choose | seed | sets that |

| significantvariationispossible. |     |     |     | Wethencalculate |     |         |     |             |     |        |      |           |
aresemanticallysimilar(ratherthanrandomlyse-
theWEATteststatisticandsignificance.
lectingseeds)becauseweexpectthatseedsetsof
Coherence. In addition to the PCA explained realistic research interest would be coherent. We
variance and WEAT test statistic, we also mea- emphasizethatresearchershaveusedbiasmeasure-
surethecoherenceofeachpairingofseedsetsafter ment methods for increasingly creative purposes,
beingmappedtothebiassubspace. Ideally,when movingbeyondgenderandrace,andsimilarbias
weprojectallthewordsinthevocabularyontothe measurementtechniquescanbeusedforaspectde-
subspace,thetwosetswouldbedrawnasfarapart tectionandotherseed-basedtasks. Exampleseeds
aspossible. Werankallwordsbycosinesimilarity areshowninTable4.
1893

| Coherence |     |     | GeneratedSeedSetA |     | GeneratedSeedSetB |     |     |     |     |     |

1.000 distinctions,similarities,friction,parallels,similarity murder,rape,manslaughter,felony,assault
1.000 mile,miles,yards,yard,feet example,instance,purposes,explanation,shorthand
1.000 shop,restaurant,kitchen,cafe,store sports,soccer,football,competitions,basketball
| ... |     |     |     |     | ... ... |     |     |     |     |     |

0.711 ambush,bombardment,escalation,altercation,militiamen corruption,terrorism,graft,bribery,abuses
0.689 entrance,terrace,subway,cafe,lawn courtside,bamboo,freeway,shorts,sailboat
0.552 sticks,onions,tops,banana,mozzarella potatoes,onions,lemon,herbs,meats
| Coherence |     |     | GatheredSeedSetA |     | GatheredSeedSetB |     |     |     |     |     |

0.933 CAREER:executive,management,professional... FAMILY:home,parents,children,family,cousins...
0.910 ASIAN:asian,asian,asian,asia,china... CAUCASIAN:caucasian,caucasian,white,america...
0.909 FEMALE:sister,mother,aunt,grandmother... MALE:brother,father,uncle,grandfather,son...
| ... |     |     |     |     | ... ... |     |     |     |     |     |

0.375 FEMALE:countrywoman,sororal,witches... MALE:countryman,fraternal,wizards,manservant...
0.110 NAMESASIAN:cho,wong,tang,huang,chu... NAMESCHINESE:chung,liu,wong,huang,ng...
0.050 NAMESBLACK:harris,robinson,howard... NAMESWHITE:harris,nelson,robinson...
Table4:Whentwoseedsetsaremoresemanticallydistincttheyaremoredistinguishableintheresultinggeometric
subspace. Thetoptableshowspairsofartificiallygeneratedseedsets,rankedbytheircoherenceforWEATinthe
NYTdataset.Thebottomtableshowspairsofseedsetsgatheredfrompublishedpapers,rankedbytheircoherence
forWEATintheWikiTextdataset. Scoresareaveragedacross20bootstrappedsamplesofthetrainingdata,and
valuesarerounded;nocoherencescoresareexactly1.0.Highercoherencescoresindicatethattheseedspairswere
projectedfartherapartinthebiassubspace.
## 7 SeedChoiceAffectsBiasMeasurement 8 FactorsCausingInstability
|     |     |     |     |     | Sometimes | seeds | can | reflect | the curator’s | (or |

Beforemovingtospecificseedfeatures,wepresent
|     |     |     |     |     | crowd’s)personalbiases. |     |     | Instabilitiescanalsoarise |     |     |

somegeneralresultsshowingtheinstabilityofmea-
fromtheorganizationoftheseedsandseemingly
| surementsusingseeds. | Figure2showsamotivating |     |     |     |           |            |           |     |             |       |

|                      |                         |     |     |     | innocuous | linguistic | features. |     | We describe | a se- |
example,inwhichweimagineadigitalhumanities
|                    |              |     |         |       | ries of distinct |     | sources | of instability | that | can be |

| scholar interested | in measuring |     | whether | women |                  |     |         |                |      |        |
encodedinseedsetsanddiscusstheimplications
areportrayedmorenegativelyindifferentgenres
|                |                            |     |     |     | of each. | We rely | on a | combination | of  | literature |

| ofbookreviews. | AsintheWEATtest,eachseedis |     |     |     |          |         |      |             |     |            |
review,qualitativeclosereadingofexampleseeds,
plottedaccordingtoitscosinesimilaritytoanaver-
|     |     |     |     |     | andquantitativetestsofseedfeatures. |     |     |     |     | Weiterated |

agedunpleasantnessvector(Caliskanetal.,2017).
|     |     |     |     |     | throughtheseeds, |     | flaggingproblematicsets, |     |     | and |

Forsomesets,nosignificantdifferenceisvisible,
thenmanuallyclusteredandlabeledthefactorsthat
| while for other | sets, there | are much | larger | differ- |     |     |     |     |     |     |

couldcauseinstability.
ences,causingtheresearchertodrawdifferentcon-
Ouridentifiedfactorscanbecategorizedasdefi-
clusionswhencomparingbiasesacrossdatasets.
nitionalfactors(reductivedefinitions,inclusionof
Table4showsboththegeneratedandgathered
confoundingconcepts),lexicalfactors(frequency,
seedsetsorderedbytheircoherenceafterusingthe POSofindividualseeds),andsetfactors(number
WEATmethodtodiscoverabiassubspace. These andorderofseeds,similarityofseedsets).
| examples highlight | factors | contributing |     | to lower |     |     |     |     |     |     |

coherence(e.g.,similarityoftheseedsets)which ReductiveDefinitions. Theseedscanbereduc-
wediscussin§8. Theyalsohighlightthegeneral tiveandessentializing,codifyinglifeexperiences
difficulty in constructing seed sets; e.g., as noted intotraditionalcategories. Usingnamesasplace-
by Garg et al. (2018), the final row demonstrates holdersforconceptslikerace(Nguyenetal.,2014;
thatsomeU.S.racialcategoriesarenotdistinguish- Sen and Wasow, 2016) or reducing gender to a
ablefromavailablecensusdata. Similarchallenges binarywithtwoextremes(Bolukbasietal.,2016;
arisewhenseedsdonotoccurinthetargetdataset, Caliskanetal.,2017)cancreateadistortedviewof
whichisoftentruefornames. Thewidevariation thesourcedata. Sometimesthesearesimplifying
in coherence scores, especially for the generated assumptions,madeinanefforttomeasurebiases
seedswhicharelesslikelytocontainoverlapping that would otherwise go unexamined. However,
terms, indicates that different seed sets can have thesedecisionsruntheriskoffurtherentrenching
widelydiffering“success”forbiasmeasurement. these category definitions—e.g., see discussions
1894

|     | ecnairaV denialpxE |     |     |                |     | ecnairaV denialpxE |     |                |     | ecnairaV denialpxE |     |                |     |

|     | 0.4                |     |     | Setting        |     | 0.3                |     | Setting        |     | 0.2                |     | Setting        |     |
|     |                    |     |     | original order |     |                    |     | original order |     |                    |     | original order |     |
|     |                    |     |     | shuffled       |     | 0.2                |     | shuffled       |     |                    |     | shuffled       |     |
|     | 0.2                |     |     |                |     |                    |     |                |     | 0.1                |     |                |     |
0.1
|     | 0.0 |       |           |       |      | 0.0 |       |           |     | 0.0 |           |       |      |

|     |     |       |           |       |      |     | 1 2 3 | 4 5 6 7   | 8   | 1 2 | 3 4 5     | 6 7 8 | 9 10 |
|     |     | 1 2 3 | 4 5       | 6 7 8 | 9 10 |     |       |           |     |     |           |       |      |
|     |     |       | Component |       |      |     |       | Component |     |     | Component |       |      |
(a)GenderPairs (b)SocialClassPairs (c)Chinese-HispanicNamePairs
Figure3: Wereplicatepreviousgenderbiasresultsandexperimentonotherorderedpairs,usingtheNYTdataset.
ThefirstPCAcomponentdominatesfororderedgenderpairsbutnotforshuffledgenderpairs(a),whileshuffling
can produce a component that explains more variance for class (b) and pleasantness (c) pairs. We find similar
instabilities using the pretrained model used in Bolukbasi et al. (2016). Error bars show standard deviation over
| the20bootstrappedmodels. |     |     |     | SeedspairsarelistedintheAppendix. |     |     |     |     |     |     |     |     |     |

cancontainconfoundingterms(e.g.,inTable1,un-
|     | herself | 0.50 |     | likelihood | 0.36 | outcomes | 0.26 |                                             |     |     |     |     |     |

|     |         | 0.49 |     |            | 0.34 |          | 0.26 | pleasantcontains“cancer”whichinsomedatasets |     |     |     |     |     |
|     |         | ms   |     | eurozone   |      | son      |      |                                             |     |     |     |     |     |
|     |         | 0.49 |     |            | 0.34 |          | 0.26 |                                             |     |     |     |     |     |
her incentive father mightbemoreprevalentforcertaindemographic
|     |     | 0.41 |     |     | 0.31 |     | 0.26 |     |     |     |     |     |     |

she downturn mother groups)ortermsfromthetargetgroup(e.g.,domes-
|     |          | 0.40  |              |         | 0.30  |             | 0.25  |                                         |     |     |     |     |     |

|     | pregnant |       |              | setback |       | aunt        |       |                                         |     |     |     |     |     |
|     |          | -0.36 |              |         | -0.39 |             | -0.19 | ticworkincludesthegenderedterms“mom”and |     |     |     |     |     |
|     | pitching |       | photographed |         |       | potentially |       |                                         |     |     |     |     |     |
|     |          | -0.36 |              |         | -0.41 |             | -0.19 |                                         |     |     |     |     |     |
baseball tales male “mum”). Similarly,theseedscanmanifestcultural
|     | syndergaard | -0.38 |     | hood   | -0.42 | hood   | -0.29 |          |              |           |       |     |        |

|     |             |       |     |        |       |        |       | stigmas: | for example, | including | “fat” | and | “wrin- |
|     | himself     | -0.39 |     | garcia | -0.45 | garcia | -0.29 |          |              |           |       |     |        |
his -0.42 danced -0.59 md -0.39 kled” in an ugliness category (Fast et al., 2016)
resultsinaseedsetthatitselfcontainsstereotypes.
|     | (a)GenderPairs |     | (b)RandomPairs |     |     | (c)Shuffled |     |     |     |     |     |     |     |

Thesestigmasareharmfulandcaninteractwith
GenderPairs
otherdemographicfeatureslikegenderorage(Puhl
| Figure | 4:  | Ranking | word | vectors | by  | cosine | similarity |     |     |     |     |     |     |

andHeuer,2009),andunlesstheirinclusionisin-
| with | the | top principle |     | component | vector | for | the origi- |     |     |     |     |     |     |

nalgenderseedpairs(a)appearstoidentifyfemaleand tentional, they can accidentally inflate measure-
|     |     |     |     |     |     |     |     | mentstowardscertaingroups. |     |     | Predictingallsuch |     |     |

malegenderedwordsmuchbetterthanrandom(b).But
shufflingthepairingofseedwords(c)maintainscorre- errorsisimpossible,andtherecanbecaseswhere
lationwithgenderbuttoalesscleardegree.Resultsare researchersintentionallyincludesuchterms(e.g.,
shownfortheNYTcorpuswithafrequencythreshold tocaptureaparticularstereotype)—butthisshould
of100andbootstrapresampling.
beaconsciousdecisionbyeachresearcherusing
|     |     |     |     |     |     |     |     | the seeds, | and at | a minimum, | researchers |     | should |

clearlydefinetheirtargetconcepts.
| in  | Keyes | (2017); | Larson | (2017) |     | for the | mistakes |     |     |     |     |     |     |

andharmsthatcanbecausedbymappingnames
togenders—andthesetrade-offsshouldbeevalu-
|     |     |     |     |     |     |     |     | Lexical | Factors. | Prior | work examining |     | seeds |

atedanddocumented. Morebroadly,recentwork hasshownthatthefrequencyandpartofspeechof
has critiqued NLP and ML bias research for not seeds can affect the resulting bias measurements.
successfullyconnectingwiththeliteratureinsoci- Ethayarajhetal.(2019)showthattheWEATtest
ologyandcriticalracestudies(Hannaetal.,2020; requiresthatthepairedseedsoccuratsimilarfre-
Blodgett et al., 2020). Engaging with this litera- quenciesandthatseedsetscanbemanipulatedto
turewouldprovideabetterfoundationfordecision- producecertainmeasurements. Brunetetal.(2019)
making about seed sets and provide context for explore the effects of perturbing the training cor-
futureresearchers. pus,findingthat(1)second-orderneighborstothe
|     |     |     |     |     |     |     |     | seeds can | have | a strong impact | on  | the bias | mea- |

Imprecise Definitions. If the target concept is surement effect size and (2) effects are stronger
not well-defined, the resulting seed terms can be forrarerwords. Usingcontextualembeddings,Se-
too broad and include multiple concepts, risking docandUngar(2019)showthatdifferentclasses
thecreationofconfoundedorcirculararguments. ofwords(e.g.,namesvs. pronouns)canresultin
Similarly,theunexamineduseofpre-existingsets differentbiassubspacesandthatsometimesthese
andover-relianceonthecategorylabelsfromprior subspacesrepresentanunintendeddimension(e.g.,
work can result in a series of errors. The seeds ageinsteadofgender).
1895

| Set Size | and | Alignment. | The | number | of  | seeds |     |     |     |     |     |     |     |

0.8
| included | in each | set | can affect | the resulting |     | bias |     |     |     |     |     |     |     |

ecnairaV denialpxE
| subspace; | Kozlowski |     | et al. (2019) | find | small | in- |     |     |     |     |     |     |     |

0.6
creasesinperformancewhenusingmoreseedpairs.
Thealignmentoftheseedsinmatchedsets(i.e.,the
0.4
Black vs
| orderingorpairingofseedsinonesetwithseeds |     |     |     |     |     |     |     | Source |     |     |     |     |     |

White Roles
| inanotherset)canalsoaffectthebiassubspace. |     |     |     |     |     | In  |     | generated |     |     |     |     |     |

0.2
|               |     |                           |     |     |     |     |     | gathered |     |     |     | Black vs    |     |

| thePCAmethod, |     | eachterminoneseedsetisex- |     |     |     |     |     |          |     |     |     | White Names |     |
plicitlylinkedtoasingletermintheotherseedset. −0.2 0.0 0.2 0.4 0.6 0.8
Set Similarity
Thespecificalignmentbetweenpairedwordsmat-
ters;alteringthepairingcanresultindramatically Figure 5: Identifying bias is less effective when set
differentresults,evenforcaseslikegender,which pairs are similar. Generated seeds are frequency-
|           |             |     |          |     |         |      | controlled | nouns | from        | the WikiText | dataset. |        | We high- |

| is marked | in English. |     | However, | we  | observe | con- |            |       |             |              |          |        |          |
|           |             |     |          |     |         |      | light two  | sets  | of gathered | seeds;       | both     | target | similar  |
sciouspairingsofseedsonlyforobviouscases,and
racialcategoriesbutthename-basedsetsaremoresimi-
sometimes“obvious”pairingsproducesubspaces
|     |     |     |     |     |     |     | larandexplainlessvariance. |     |     | Wefindsimilartrendsfor |     |     |     |

thatexplainlessvariance.
WEAT,coherence,andtheothercorporaandPOS.
| We replicate |           | a study    | previously        | carried |             | out on |                 |         |            |           |        |           |           |

| embeddings   | trained   |            | on internet-scale |         | collections |        |                 |         |            |           |        |           |           |
|              |           |            |                   |         |             |        | Set Similarity. |         | By         | sampling  | random | seed      | sets      |
| (Bolukbasi   | et        | al., 2016) | using             | both    | a large,    | pre-   |                 |         |            |           |        |           |           |
|              |           |            |                   |         |             |        | we find         | that    | it is more | difficult | to     | represent | the       |
| trained      | embedding | and        | the relatively    |         | small       | NYT    |                 |         |            |           |        |           |           |
|              |           |            |                   |         |             |        | variance        | of seed | sets       | that are  | too    | close     | together. |
dataset. Figure3showshowmuchvarianceisex-
Figure5showsthatsetsimilarity(cosinesimilar-
| plained | by the | first | ten principal | components |     | of  |     |     |     |     |     |     |     |

threedifferencematrices. Whenweusetheorigi- ity between the set mean vectors) is significantly
|     |     |     |     |     |     |     | correlated | with | explained | variance |     | for generated |     |

nalpairedmale-femaleseedwordsfromBolukbasi
|               |        |            |     |          |     |        | sets(Pearsonr |     | = −0.67,p |     | < 0.05). | Wehighlight |     |

| et al. (2016) | (e.g., | man-woman, |     | he-she), |     | we see |               |     |           |     |          |             |     |
twocomparisonsbetweengatheredsetsintendedto
| a single | dominant | first | component, |     | suggesting | a   |     |     |     |     |     |     |     |

measureracialbiasthatexplaindifferentdegrees
| strong male-female |     |     | axis. As | previously | reported, |     |              |           |     |          |           |     |         |

|                    |     |     |          |            |           |     | of variance. | Synthetic |     | pairings | generally |     | explain |
thevariancesfalloffgraduallywhentheseedsarea
|                   |     |     |                         |     |     |     | more variance |     | than pairings |     | of gathered |     | sets of |

| setofrandomwords. |     |     | Whenweshuffletheorderof |     |     |     |               |     |               |     |             |     |         |
theseedwords,thedropoffissteeperthanforran- equalsimilarity,althoughforgatheredsetswecan-
|     |     |     |     |     |     |     | notcontrolforPOSandfrequency. |     |     |     |     | Table4shows |     |

dompairs,butthereisnolongerasingledominant
thegeneratedseedsetsrankedbycoherence,where
principalcomponent.
|     |     |     |     |     |     |     | higher scores |     | indicate | that | the bias | subspace | was |

Similarly,Figure4showsthatwhenweusedthe
|     |     |     |     |     |     |     | abletoseparatetheseedsets. |     |     |     | Similarseedsetsand |     |     |

orderedgenderpairs,therankedwordsroughlydi-
|     |     |     |     |     |     |     | sets with | duplicates | (e.g., | the | pairing | in  | the table |

videintogroupscorrelatedwithgender,whileifwe
|     |     |     |     |     |     |     | in which | both | generated | sets | contain | food | terms) |

useshuffledpairs,thelistsofhighandlowranked
havelowcoherencescores.
wordsarenotaseasilydistinguishableasmasculine
| orfeminine. | Wefindanoppositeeffectsocialclass |     |     |     |     |     |               |     |                     |     |     |     |     |

|             |                                   |     |     |     |     |     | 9 Conclusion: |     | BiasesAlltheWayDown |     |     |     |     |
pairs(Kozlowskietal.,2019);whenweshuffle,we
findasubspacethatexplainsmorevariancethanthe
Almostallrecentworkonbiasmeasurementrelies
explicitlyorderedpairs(e.g.,“richest”-“poorest”).
onsetsofseedtermstogroundculturalconceptsin
Wefindsimilardifferenceswhentestingsomeseed language. Ifwedonotpayattentiontotheseeds,
| setsthatlackintuitivepairings, |     |     |     | e.g., | thematched |     |     |     |     |     |     |     |     |

thesemethodswilllackfoundationandtheclaims
pleasantnessandunpleasantnessseeds(Caliskan
theysupportwillbeleftopentocriticismanddis-
etal.,2017)andthematchedChristianityandIslam missal. Seedsandtheirrationalesneedtobetested
seeds(Gargetal.,2018). and documented, rather than hidden in code or
Orderdoesnotalwaysaffectthesubspace—e.g, copiedwithoutexamination.
wefoundnosignificantdifferencewhenshuffling Some of the risks discussed in this paper may
setsofnames—butwehaveshownthatitcanaf- seemobviousinretrospect,butourliteraturesurvey
fect the subspace, and so to build confidence in suggeststherearewidelyvaryinglevelsofevalu-
measurements,testingisrequired. ation and documentation. Rationales for picking
1896

sources or seeds are not always explained, or the beaccessible,nothard-coded,withuniquelabels
reader is left to assume that prior work has ade- matchedtoexperiments.
quately validated the seeds. Tests for frequency, Ultimately, our goal is not to eliminate a prob-
semanticsimilarity,andotherfeaturesarerareor lembuttoilluminateit:2 tohelppractitionersthink
non-existent,andcleardefinitionsanddiscussionof throughthepotentialrisksposedbyseedsetsused
limitationsareoftenmissing. Permutationtestsare forbiasdetection. Weencouragethoughtful,criti-
sometimesused,butthesedonotaccountforseeds calstudies, butweobserveatrendinwhichseed
outsideofthosealreadyselected. Significantlydif- setsareusedinnewresearchandapplicationssim-
ferentresultscanbefoundusingalternativeseeds plybecausetheyhavebeenusedinpriorpublished
setsforthesametargetconcept,andfine-grained work,withoutadditionalvetting. Researchprece-
comparisonsrequirevalidationonmultiplesets. dentscantakeonalifeoftheirownandwehave
aresponsibilitytoexploreanddocumentpossible
| We faced |      | a number of | challenges      | in  | gathering |                 |                            |              |     |         |

|          |      |             |                 |     |           | sourcesoferror. | Webelievethatseedsetscanbe |              |     |         |
| 178 seed | sets | from prior  | work. Sometimes |     | seeds     |                 |                            |              |     |         |
|          |      |             |                 |     |           | useful and      | are probably               | unavoidable, | but | that no |
aresharedonlineatanundocumentedlocationand
technicaltoolcanabsolveresearchersfromtheduty
sometimeshard-codedintocoderepositories;this
tochooseseedscarefullyandintentionally.
| can significantly |     | obscure | the seeds | from | public |     |     |     |     |     |

view,whichistroublingfortoolsintendedforwide Acknowledgements
| use on | sensitive | topics. | Documentation |     | is often |     |     |     |     |     |

scattered across locations, and in more than one Thank you to our anonymous reviewers whose
commentssubstantiallyinfluencedandimproved
| case, we | found | contradictions | between |     | different |     |     |     |     |     |

sourcesforasingleproject. Inonecase,wewere this paper. Thank you to Rishi Bommasani, For-
unabletofindthefulllistofseedsusedinthepaper, restDavis,OsKeyes,LaurenKilgour,Rosamund
|     |     |     |     |     |     | Thalken, Marten |     | van Schijndel, | Melanie | Walsh, |

andinseveralcases,itwasunclearwhichseedsets
andGregoryYauneyfortheirmanyhelpfulsugges-
| were used | for | which experiments. |     | While | some |     |     |     |     |     |

authorswenttocommendablelengthstodocument tions. This work was funded through NSF grant
| theirmaterials,thereisaneedformoreconsistent |     |     |     |     |     | #1652536. |     |     |     |     |

andtransparentdocumentation.
| Werecommendthatresearcherscarefullytrace |     |               |      |            |        | References                              |     |                 |       |        |

| the origins                              |     | of seed sets, | with | attention  | to the |                                         |     |                 |       |        |
|                                          |     |               |      |            |        | Emily M. Bender                         | and | Batya Friedman. | 2018. | Data   |
| risksassociatedwiththeorigintype.        |     |               |      | Wealsorec- |        |                                         |     |                 |       |        |
|                                          |     |               |      |            |        | statementsfornaturallanguageprocessing: |     |                 |       | Toward |
ommend that researchers examine seed features. mitigating system bias and enabling better science.
POS, frequency, semantic similarity, and pairing Transactions of the Association for Computational
Linguistics,6:587–604.
ordercansignificantlyaffecttheresultsofbiasmea-
surements. Seeds should be both examined man- Sudeep Bhatia, Geoffrey P Goodwin, and Lukasz
|     |     |     |     |     |     | Walasek. | 2018. Trait | associations | for Hillary | Clin- |

uallyandtestedasshownin§8;importantly,they
shouldbecomparedtoalternativeseedswithdif- ton and Donald Trump in news media: A computa-
|                          |     |     |                       |     |     | tional analysis. | Social | Psychological | and | Personal- |

| ferentattributes,asin§7. |     |     | Toassistthiswerelease |     |     |                  |        |               |     |           |
ityScience,9(2):123–130.
| a compilation |     | of 178 seed | sets | from prior | work. |     |     |     |     |     |

These tests are particularly important when com- Su Lin Blodgett, Solon Barocas, Hal Daume´ III, and
|                             |     |     |                     |     |     | Hanna Wallach. |          | 2020. Language   | (technology) | is      |

| paringbiasesacrossdatasets. |     |     | Finally,researchers |     |     |                |          |                  |              |         |
|                             |     |     |                     |     |     | power: A       | critical | survey of “bias” | in NLP.      | In Pro- |
shoulddocumentallseedsandtherationalesun- ceedings of the 58th Annual Meeting of the Asso-
derlyingtheirdesign,includingconceptdefinitions.
|     |     |     |     |     |     | ciation for | Computational | Linguistics, | pages | 5454– |

Weaddtorecentcallsforbetterdocumentationand 5476, Online. Association for Computational Lin-
guistics.
problemspecificationinmachinelearning(Bender
andFriedman,2018;Gebruetal.,2018;Mitchell Tolga Bolukbasi, Kai-Wei Chang, James Y Zou,
etal.,2019;Blodgettetal.,2020)andinstudiesof Venkatesh Saligrama, and Adam T Kalai. 2016.
|     |     |     |     |     |     | Man is to | computer | programmer | as woman | is to |

socialbiasesintechnology(Olteanuetal.,2019).
Specifically,whentheseedsintentionallyencode 2“Allproblemscanbeilluminated;notallproblemscan
harmfulstereotypesorslurs,itcanbebeneficialto be solved.”—Ursula Franklin (quoted by M. Meredith via
Olteanuetal.(2019)inhttp://bb9.berlinbiennale
includeatriggerwarningornothighlighttheseeds
.de/all-problems-can-be-illuminated-not-
inthepaper;however,fullseedlistsshouldalways all-problems-can-be-solved/)
1897

homemaker? Debiasing word embeddings. In Ad- Anthony G Greenwald, Debbie E McGhee, and Jor-
vances in Neural Information Processing Systems, dan LK Schwartz. 1998. Measuring individual dif-
pages4349–4357. ferences in implicit cognition: the implicit associa-
|                                     |     |     |     |                   |     |           | tiontest.       | Journalofpersonalityandsocialpsychol- |     |     |     |     |     |

| MargaretMBradleyandPeterJLang.1999. |     |     |     |                   |     | Affective | ogy,74(6):1464. |                                       |     |     |     |     |     |
| normsforenglishwords(anew):         |     |     |     | Instructionmanual |     |           |                 |                                       |     |     |     |     |     |
WilliamL.Hamilton,JureLeskovec,andDanJurafsky.
| and affective |     | ratings. | Technical |     | report. | The Cen- |                  |     |      |            |     |        |           |

|               |     |          |           |     |         |          | 2016. Diachronic |     | word | embeddings |     | reveal | statisti- |
terforResearchinPsychophysiology,Universityof
|     |     |     |     |     |     |     | callawsofsemanticchange. |     |     |     | InProceedingsofthe |     |     |

Florida.
54thAnnualMeetingoftheAssociationforCompu-
|     |     |     |     |     |     |     | tationalLinguistics(Volume1: |     |     |     | LongPapers),pages |     |     |

Marc-EtienneBrunet,ColleenAlkalay-Houlihan,Ash-
|               |     |     |         |        |       |        | 1489–1501, | Berlin, | Germany.AssociationforCom- |     |     |     |     |

| ton Anderson, |     | and | Richard | Zemel. | 2019. | Under- |            |         |                            |     |     |     |     |
putationalLinguistics.
| standing | the | origins | of  | bias in word | embeddings. |     |     |     |     |     |     |     |     |

AlexHanna,EmilyDenton,AndrewSmart,andJamila
| In International |     | Conference |     | on Machine |     | Learning, |     |     |     |     |     |     |     |

pages803–811. Smith-Loud. 2020. Towards a critical race method-
|                 |     |        |           |           |               |        | ologyinalgorithmicfairness. |     |              |              | InProceedingsofthe |          |     |

|                 |     |        |           |           |               |        | 2020 Conference             |     | on Fairness, |              | Accountability,    |          | and |
| Aylin Caliskan, |     | Joanna |           | J Bryson, | and           | Arvind |                             |     |              |              |                    |          |     |
|                 |     |        |           |           |               |        | Transparency,               |     | FAT*’20,     | page501–512, |                    | NewYork, |     |
| Narayanan.      |     | 2017.  | Semantics | derived   | automatically |        |                             |     |              |              |                    |          |     |
NY,USA.AssociationforComputingMachinery.
| from | language | corpora |     | contain human-like |     | biases. |     |     |     |     |     |     |     |

Science,356(6334):183–186.
|     |     |     |     |     |     |     | Matthew Honnibal, |     | Ines    | Montani, | Sofie | Van | Lan-   |

|     |     |     |     |     |     |     | deghem,           | and | Adriane | Boyd.    | 2020. |     | spaCy: |
KawinEthayarajh,DavidDuvenaud,andGraemeHirst. Industrial-strength Natural Language Processing in
| 2019. | Understanding |     | undesirable |     | word | embedding |     |     |     |     |     |     |     |

Python.
| associations. |     | In              | Proceedings | of                | the 57th | Annual |           |          |        |          |     |              |     |

|               |     |                 |             |                   |          |        | Alexander | Miserlis | Hoyle, | Lawrence |     | Wolf-Sonkin, |     |
| Meeting       | of  | the Association |             | for Computational |          | Lin-   |           |          |        |          |     |              |     |
HannaWallach,IsabelleAugenstein,andRyanCot-
guistics,pages1696–1705,Florence,Italy.Associa-
tionforComputationalLinguistics. terell. 2019. Unsupervised discovery of gendered
|             |        |     |       |             |     |            | language | through           | latent-variable |              | modeling. |        | In Pro- |

|             |        |     |       |             |     |            | ceedings | of the            | 57th            | Annual       | Meeting   | of the | Asso-   |
| Ethan Fast, | Binbin |     | Chen, | and Michael | S.  | Bernstein. |          |                   |                 |              |           |        |         |
|             |        |     |       |             |     |            | ciation  | for Computational |                 | Linguistics, |           | pages  | 1706–   |
2016. Empath:Understandingtopicsignalsinlarge-
1716,Florence,Italy.AssociationforComputational
| scale | text. In | Proceedings |     | of the | 2016 CHI | Confer- |     |     |     |     |     |     |     |

Linguistics.
enceonHumanFactorsinComputingSystems,CHI
’16,page4647–4657,NewYork,NY,USA.Associ- Minqing Hu and Bing Liu. 2004. Mining and sum-
ationforComputingMachinery. marizing customer reviews. In Proceedings of the
|     |     |     |     |     |     |     | Tenth ACM | SIGKDD |     | International |     | Conference | on  |

Patrick S Forscher, Calvin K Lai, Jordan R Axt, Knowledge Discovery and Data Mining, KDD ’04,
Charles R Ebersole, Michelle Herman, Patricia G page168–177,NewYork,NY,USA.Associationfor
Devine,andBrianANosek.2017. Ameta-analysis ComputingMachinery.
| ofchangeinimplicitbias. |       |       |              | PsychologicalBulletin. |           |          |                 |           |             |        |               |     |         |

|                         |       |       |              |                        |           |          | Kenneth Joseph, |           | Wei Wei,    | and    | Kathleen      | M   | Carley. |
|                         |       |       |              |                        |           |          | 2017.           | Girls     | rule, boys  | drool: | Extracting    |     | seman-  |
| Nikhil Garg,            | Londa |       | Schiebinger, | Dan                    | Jurafsky, | and      |                 |           |             |        |               |     |         |
|                         |       |       |              |                        |           |          | tic and         | affective | stereotypes |        | from twitter. |     | In Pro- |
| James                   | Zou.  | 2018. | Word         | embeddings             |           | quantify |                 |           |             |        |               |     |         |
ceedingsofthe2017ACMConferenceonComputer
| 100 years | of  | gender | and | ethnic | stereotypes. | Pro- |     |     |     |     |     |     |     |

SupportedCooperativeWorkandSocialComputing,
| ceedings | of  | the | National | Academy | of  | Sciences, |     |     |     |     |     |     |     |

pages1362–1374.ACM.
115(16):E3635–E3644.
|     |     |     |     |     |     |     | Os Keyes. | 2017. | Stop | mapping | names | to  | gender. |

https://ironholds.org/names-gender/.
| Timnit Gebru, |     | Jamie | Morgenstern, |     | Briana | Vecchione, |     |     |     |     |     |     |     |

Jennifer Wortman Vaughan, Hanna Wallach, Hal Accessed: 2021-05-26.
| Daume´III,andKateCrawford.2018. |     |     |     |     | Datasheetsfor |     |     |     |     |     |     |     |     |

YoonKim,Yi-IChiu,KentaroHanaki,DarshanHegde,
| datasets. | Proceedings     |     | of  | the 5th Workshop |     | on Fair-   |                                   |         |       |          |          |            |         |

|           |                 |     |     |                  |     |            | and Slav                          | Petrov. | 2014. | Temporal | analysis |            | of lan- |
| ness,     | Accountability, |     | and | Transparency     |     | in Machine |                                   |         |       |          |          |            |         |
|           |                 |     |     |                  |     |            | guagethroughneurallanguagemodels. |         |       |          |          | InProceed- |         |
Learning,PMLR.
ingsoftheACL2014WorkshoponLanguageTech-
|            |     |      |           |       |          |      | nologies | and | Computational |     | Social | Science, | pages |

| Hila Gonen | and | Yoav | Goldberg. | 2019. | Lipstick | on a |          |     |               |     |        |          |       |
61–65,Baltimore,MD,USA.AssociationforCom-
| pig: Debiasingmethodscoverupsystematicgender |     |     |     |     |     |     | putationalLinguistics. |     |     |     |     |     |     |

biasesinwordembeddingsbutdonotremovethem.
InProceedingsofthe2019ConferenceoftheNorth Markus Knoche, Radomir Popovic´, Florian Lem-
American Chapter of the Association for Computa- merich,andMarkusStrohmaier.2019a. Identifying
tional Linguistics: Human Language Technologies, biases in politically biased wikis through word em-
Volume 1 (Long and Short Papers), pages 609–614, beddings. In Proceedings of the 30th ACM Confer-
Minneapolis, Minnesota. Association for Computa- enceonHypertextandSocialMedia,HT’19,pages
| tionalLinguistics. |     |     |     |     |     |     | 253–257,NewYork,NY,USA.ACM. |     |     |     |     |     |     |

1898

Markus Knoche, Radomir Popovic´, Florian Lem- Alexandra Olteanu, Carlos Castillo, Fernando Diaz,
merich,andMarkusStrohmaier.2019b. Identifying and Emre Kıcıman. 2019. Social data: Bi-
biases in politically biased wikis through word em- ases,methodologicalpitfalls,andethicalboundaries.
beddings. In Proceedings of the 30th ACM Confer- FrontiersinBigData,2:13.
enceonHypertextandSocialMedia,pages253–257.
| ACM. |     |     |     |     |     |     | GalenPanger.2016. |     | ReassessingtheFacebookexperi- |     |     |     |     |

ment:criticalthinkingaboutthevalidityofBigData
|                   |     |            |     |                 |     |     | research. | Information, |     | Communication |     | &   | Society, |

| AustinCKozlowski, |     | MattTaddy, |     | andJamesAEvans. |     |     |           |              |     |               |     |     |          |
19(8):1108–1126.
2019. Thegeometryofculture:Analyzingthemean-
| ings of | class through | word | embeddings. |     | American |     |     |     |     |     |     |     |     |

SociologicalReview,84(5):905–949. James W Pennebaker, Martha E Francis, and Roger J
|                 |     |                |     |     |        |         | Booth.     | 2001. | Linguistic | inquiry  | and | word    | count: |

|                 |     |                |     |     |        |         | Liwc 2001. |       | Mahway:    | Lawrence |     | Erlbaum | Asso-  |
| Vivek Kulkarni, |     | Bryan Perozzi, |     | and | Steven | Skiena. |            |       |            |          |     |         |        |
ciates,71(2001):2001.
| 2016. | Freshman | or fresher? |     | Quantifying | the | geo- |     |     |     |     |     |     |     |

graphicvariationoflanguageinonlinesocialmedia.
|             |     |                   |     |      |            |     | Lawrence | Phillips, | Kyle         | Shaffer, | Dustin |       | Arendt, |

| Proceedings | of  | the International |     | AAAI | Conference |     |          |           |              |          |        |       |         |
|             |     |                   |     |      |            |     | Nathan   | Hodas,    | and Svitlana | Volkova. |        | 2017. | Intrin- |
onWebandSocialMedia,10(1).
|               |       |        |     |            |             |     | sic and         | extrinsic | evaluation | of       | spatiotemporal |                | text |

|               |       |        |     |            |             |     | representations |           | in Twitter | streams. |                | In Proceedings |      |
| Brian Larson. | 2017. | Gender | as  | a variable | in natural- |     |                 |           |            |          |                |                |      |
ofthe2ndWorkshoponRepresentationLearningfor
| languageprocessing:Ethicalconsiderations. |        |           |          |     |           | InPro- | NLP,pages201–210. |     |     |     |     |     |     |

| ceedings                                  | of the | First ACL | Workshop |     | on Ethics | in     |                   |     |     |     |     |     |     |
NaturalLanguageProcessing,pages1–11,Valencia, Rebecca M Puhl and Chelsea A Heuer. 2009. The
Spain.AssociationforComputationalLinguistics.
|     |     |     |     |     |     |     | stigma | of obesity: | a   | review | and update. |     | Obesity, |

17(5):941–964.
| Thomas Manzini, |     | Lim Yao | Chong, |     | Alan W | Black, |     |     |     |     |     |     |     |

and Yulia Tsvetkov. 2019. Black is to criminal RadimRˇehu˚ˇrekandPetrSojka.2010. SoftwareFrame-
as caucasian is to police: Detecting and removing work for Topic Modelling with Large Corpora. In
multiclass bias in word embeddings. In Proceed- Proceedings of the LREC 2010 Workshop on New
ingsofthe2019ConferenceoftheNorthAmerican ChallengesforNLPFrameworks,pages45–50,Val-
Chapter of the Association for Computational Lin- letta,Malta.ELRA. http://is.muni.cz/publi
| guistics: | Human | Language | Technologies, |     | Volume | 1   | cation/884893/en. |     |     |     |     |     |     |

(LongandShortPapers),pages615–621,Minneapo-
lis, Minnesota. Association for Computational Lin- Rachel Rudinger, Chandler May, and Benjamin
| guistics. |     |     |     |     |     |     | VanDurme.2017.    |     | Socialbiasinelicitednaturallan- |             |     |           |     |

|           |     |     |     |     |     |     | guage inferences. |     | In                              | Proceedings | of  | the First | ACL |
StephenMerity,CaimingXiong,JamesBradbury,and Workshop on Ethics in Natural Language Process-
RichardSocher.2016. Pointersentinelmixturemod- ing, pages 74–79, Valencia, Spain. Association for
ComputationalLinguistics.
els.
DiegoSaez-Trumper,CarlosCastillo,andMouniaLal-
TomasMikolov,IlyaSutskever,KaiChen,GregSCor-
|           |      |             |     |             |             |     | mas. 2013. | Social | media | news | communities: |     | gate- |

| rado, and | Jeff | Dean. 2013. |     | Distributed | representa- |     |            |        |       |      |              |     |       |
Pro-
|     |     |     |     |     |     |     | keeping, | coverage, | and | statement |     | bias. | In  |

tionsofwordsandphrasesandtheircompositional-
ceedingsofthe22ndACMinternationalconference
| ity. In | Advances | in Neural | Information |     | Processing |     |                |     |             |     |             |     |       |

|         |          |           |             |     |            |     | on Information |     | & Knowledge |     | Management, |     | pages |
Systems,pages3111–3119.
1679–1684.ACM.
Margaret Mitchell, Simone Wu, Andrew Zaldivar, Joa˜o Sedoc and Lyle Ungar. 2019. The role of pro-
Parker Barnes, Lucy Vasserman, Ben Hutchinson, tected class word lists in bias identification of con-
| Elena Spitzer, |       | Inioluwa    | Deborah | Raji, | and        | Timnit |                                 |     |     |     |                 |     |     |

|                |       |             |         |       |            |        | textualizedwordrepresentations. |     |     |     | InProceedingsof |     |     |
| Gebru.         | 2019. | Model cards | for     | model | reporting. | In     |                                 |     |     |     |                 |     |     |
theFirstWorkshoponGenderBiasinNaturalLan-
ProceedingsoftheConferenceonFairness,Account-
guageProcessing,pages55–61,Florence,Italy.As-
ability,andTransparency,FAT*’19,page220–229,
sociationforComputationalLinguistics.
| New York,  | NY, | USA. | Association |     | for Computing |     |           |                                       |        |       |      |     |          |

| Machinery. |     |      |             |     |               |     | Maya Sen  | and Omar                              | Wasow. | 2016. | Race | as  | a bundle |
|            |     |      |             |     |               |     | ofsticks: | Designsthatestimateeffectsofseemingly |        |       |      |     |          |
DongNguyen,DolfTrieschnigg,A.SezaDog˘ruo¨z,Ri-
|                                             |       |       |            |     |         |         | immutablecharacteristics. |     |     | AnnualReview |     |     | of Politi- |

| lanaGravel,Marie¨tTheune,TheoMeder,andFran- |       |       |            |     |         |         | calScience,19.            |     |     |              |     |     |            |
| ciska de                                    | Jong. | 2014. | Why gender |     | and age | predic- |                           |     |     |              |     |     |            |
tion from tweets is hard: Lessons from a crowd- Chris Sweeney and Maryam Najafian. 2019. A trans-
sourcing experiment. In Proceedings of COLING parent framework for evaluating unintended demo-
2014,the25thInternationalConferenceonCompu- graphicbiasinwordembeddings. InProceedingsof
tationalLinguistics: TechnicalPapers,pages1950– the57thAnnualMeetingoftheAssociationforCom-
1961, Dublin, Ireland. Dublin City University and putational Linguistics, pages 1662–1667, Florence,
AssociationforComputationalLinguistics. Italy.AssociationforComputationalLinguistics.
1899

Mengting Wan and Julian J. McAuley. 2018. Item
recommendationonmonotonicbehaviorchains. In
Proceedings of the 12th ACM Conference on Rec-
ommender Systems, RecSys 2018, Vancouver, BC,
Canada,October2-7,2018,pages86–94.ACM.
MengtingWan,RishabhMisra,NdapaNakashole,and
Julian J. McAuley. 2019. Fine-grained spoiler de-
tection from large-scale review corpora. In Pro-
ceedings of the 57th Conference of the Association
forComputationalLinguistics,ACL2019,Florence,
Italy, July 28- August 2, 2019, Volume 1: Long Pa-
pers, pages 2605–2610. Association for Computa-
tionalLinguistics.
JohnEWilliamsandSusanMBennett.1975. Thedef-
initionofsexstereotypesviatheadjectivechecklist.
SexRoles,1(4).
JohnEWilliamsandDeborahLBest.1977. Sexstereo-
typesandtraitfavorabilityontheadjectivechecklist.
EducationalandPsychologicalMeasurement.
John E Williams and Deborah L Best. 1990. Measur-
ingsexstereotypes: Amultinationstudy,Rev. Sage
Publications,Inc.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Ryan Cot-
terell, Vicente Ordonez, and Kai-Wei Chang. 2019.
Genderbiasincontextualizedwordembeddings. In
Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), pages 629–634,
Minneapolis, Minnesota. Association for Computa-
tionalLinguistics.
JieyuZhao,YichaoZhou,ZeyuLi,WeiWang,andKai-
Wei Chang. 2018. Learning gender-neutral word
embeddings. InProceedingsofthe2018Conference
onEmpiricalMethodsinNaturalLanguageProcess-
ing, pages 4847–4853, Brussels, Belgium. Associa-
tionforComputationalLinguistics.
1900

| A Appendix |     |     |     |     |     |     | A.2 SeedTerms |     |     |     |     |     |

BecauseoftheAppendixpagelimit,wecannotlist
A.1 Datasets
|     |     |     |     |     |     |     | herealltheseedsetsgatheredfrompriorwork. |     |     |     |     | In- |

stead,thefullseedsetsinadditiontotherationales
| NewYorkTimes. |     |     | Thisdatasetcontains165,900 |     |     |     |     |     |     |     |     |     |

paragraphsfromarticlespublishedbetweenApril andsourcesusedfortheircurationarereleasedas
|                        |     |     |     |                     |     |     | asupplementaryJSONfile. |     |     | Afterpublication,the |     |     |

| 15thandJune30th,2016.3 |     |     |     | Thearticlesaredrawn |     |     |                         |     |     |                      |     |     |
seedswillalsobedocumentedatapublicwebsite.
fromallsectionsoftheEnglishlanguagenews,in-
|     |     |     |     |     |     |     | Below, | we list | all the | seeds used as | examples | (in |

cludingMovies,Sports,Technology,World,U.S.,
Arts, Business, Books, NY Region, Health, Sci- figuresortext)inthemainpaper. TheseedIDscor-
respondtoamatchingIDfieldinthesupplementary
| ence,andFashion. |     | Thisdatasetissmallincompar- |     |     |     |     |     |     |     |     |     |     |

JSONfile.
| ison to | the large | training | datasets |          | used | for down- |     |     |     |     |     |     |

| stream  | features; | its      | scope    | fits the | use  | case of a |     |     |     |     |     |     |
socialscientistinterestedinmeasuringbiasduring
Table1
asmalltimewindowataparticularpublication.

| WikiText. |     | The WikiText |     | training | corpus | con- |                     |     |     |            |     |     |

|           |     |              |     |          |        |      | unpleasant-Caliskan |     |     | et al 2017 |     |     |
tains the texts of 28,000 manually verified high- UsedIn: Caliskanetal.(2017)
qualityarticlesfromWikipedia.org(Merityetal., Seeds: [abuse, crash, filth, murder, sick-
2016). Listshavebeenremoved,alongwithHTML ness,accident,death,grief,poison,stink,as-
errors, math, and code. We use the full training sault, disaster, hatred, pollute, tragedy, di-
dataset,WikiText-103.4 Thisdatasetismuchlarger vorce, jail, poverty, ugly, cancer, kill, rotten,
than the NYT dataset but is still of focused inter- vomit,agony,prison]
| est in a | particular | online | community |     | (Wikipedia |     |     |     |     |     |     |     |

authors).
|            |       |                             |             |     |         |     | african  | american |                     | names-       |           |     |

|            |       |                             |             |     |         |     | Caliskan |          | et al               | 2017         |           |     |
| Goodreads. |       | Wesample500Goodreadsbookre- |             |     |         |     |          |          |                     |              |           |     |
|            |       |                             |             |     |         |     | UsedIn:  |          | Caliskanetal.(2017) |              |           |     |
| views for  | books | in                          | the romance | and | history | and |          |          |                     |              |           |     |
|            |       |                             |             |     |         |     | Seeds:   |          | [Alonzo,            | Jamel, Theo, | Alphonse, |     |
biographygenres,removingbookswithfewerthan
Jerome,Leroy,Torrance,Darnell,Lamar,Li-
500reviewsandreviewscontainingfewerthan20
onel,Tyree,Deion,Lamont,Malik,Terrence,
| characters. | We  | use | the provided |     | genre | samples |     |     |     |     |     |     |

Tyrone,Lavon,Marcellus,Wardell,Nichelle,
fromtheUCSDBookGraph(WanandMcAuley,
Shereen,Ebony,Latisha,Shaniqua,Jasmine,
2018;Wanetal.,2019).5
|     |     |     |     |     |     |     | Tanisha, |     | Tia, | Lakisha, Latoya, |     | Yolanda, |

Malika,Yvette]
| GoogleNews.  |                      | Forsomeofourexperiments, |         |           |        | as       |            |     |                 |            |     |     |

| a comparison |                      | for the                  | smaller | datasets, |        | we use a | • SeedsID: |     |                 |            |     |     |
| model        | pre-trained          | on                       | part    | of the    | Google | News     |            |     |                 |            |     |     |
|              |                      |                          |         |           |        |          | domestic   |     | work-Fast       | et al 2016 |     |     |
| dataset.6    | Thisisapopularmodel, |                          |         |           | usedin | Boluk-   |            |     |                 |            |     |     |
|              |                      |                          |         |           |        |          | UsedIn:    |     | Fastetal.(2016) |            |     |     |
basi et al. (2016) and many other studies. This Seeds: [chore, mom, vacuum, scrubbing,
| data originates |     | from | an internal |     | Google | dataset |     |     |     |     |     |     |

cook,washing,baking,wash,morning,meal,
| (Mikolov | et  | al., 2013), | and | we could | not | find a |     |     |     |     |     |     |

house,chef,laundry,bake,organizing,cook-
comprehensivedescriptionofthedatabeyondits
ing,spotless,mum,washer,remodeling,par-
vocabularysize: 3millionuniquewordsand100 ent, job, nanny, kitchen, dishwasher, clean-
billiontokens.
|     |     |     |     |     |     |     | ing, | family,      | cleaner, | bathroom,            | errand, | sit-  |

|     |     |     |     |     |     |     | ter, | housekeeper, |          | serve, housekeeping, |         | tidy, |
3https://www.kaggle.com/nzalake52/new
|     |     |     |     |     |     |     | cleaned, |     | housework, | scrub, organize, |     | home, |

-york-times-articles
clean]
4https://blog.einstein.ai/the-wikitex
t-long-term-dependency\-language-modelin
| g-dataset/ |     |     |     |     |     |     | • SeedsID: |     |     |     |     |     |

5https://sites.google.com/eng.ucsd.ed ugliness-Fast et al 2016
u/ucsdbookgraph/home
|     |     |     |     |     |     |     | UsedIn: |     | Fastetal.(2016) |     |     |     |

6https://code.google.com/archive/p/wo
| rd2vec/ |     |     |     |     |     |     | Seeds: |     | [despise, | balding, | slimy, | acne, |

1901

grotesque,degrading,horrible,fat,diseased, dowry,hostesses,airwomen,menopause,cli-
repulsive, awful, nasty, brutish, grotesquely, toris,princess,governesses,abbess,women,
distasteful,unworthy,scruffy,chubby,gross, widow, ladies, sorceresses, madam, brides,
insulting, crooked, revolting, unappealing, baroness, housewives, godesses, niece, wid-
hairy, pathetic, cockroach, abnormally, un- ows,lady,sister... (seeSupplementaryMateri-
| sightly, | crippled, | lousy, wrinkled, | freakish, | alsforfulllist)] |     |     |     |

disfigured, disgusting, pudgy, tacky, obese, Seeds 2: [countryman, fraternal, wizards,
disgust, degrade, horrid, deformed, hideous, manservant, fathers, divo, actor, bachelor,
bloated,ugly,scum,demeaning,pig,obnox- papa,dukes,barman,countrymen,brideprice,
ious,blob,wart,disgraceful,fatty,bald,over- hosts,airmen,andropause,penis,prince,gov-
weight,disgusted,unattractive,wrinkle,filthy, ernors,abbot,men,widower,gentlemen,sor-
| loathsome] |     |     |     | cerers, | sir, bridegrooms, |     | baron, househus- |

bands,gods,nephew,widowers,lord,brother,
| Table4          |                     |            |     | (seeSupplementaryMaterialsforfulllist)] |                 |       |         |

| • UsedIn:       | Caliskanetal.(2017) |            |     | • UsedIn:                               | Gargetal.(2018) |       |         |
| SeedsID1:       |                     |            |     | SeedsID1:                               |                 |       |         |
| career-Caliskan |                     | et al 2017 |     | names                                   | asian-Garg      | et al | 2018    |
| SeedsID2:       |                     |            |     | SeedsID2:                               |                 |       |         |
| family-Caliskan |                     | et al 2017 |     | names                                   | chinese-Garg    | et    | al 2018 |
Seeds 1: [executive, management, profes- Seeds1: [cho,wong,tang,huang,chu,chung,
sional, corporation, salary, office, business, ng,wu,liu,chen,lin,yang,kim,chang,shah,
| career] |     |     |     | wang,li,khan,singh,hong] |     |     |     |

Seeds 2: [home, parents, children, family, Seeds 2: [chung, liu, wong, huang, ng, hu,
cousins,marriage,wedding,relatives] chu, chen, lin, liang, wang, wu, yang, tang,
chang,hong,li]
| • UsedIn: | Manzinietal.(2019) |     |     |           |                 |     |     |

| SeedsID1: |                    |     |     | • UsedIn: | Gargetal.(2018) |     |     |
SeedsID1:
| asian-Manzini |     | et al 2019 |     |       |            |       |      |

|               |     |            |     | names | black-Garg | et al | 2018 |
SeedsID2:
| caucasian-Manzini |     | et al 2019 |     | SeedsID2: |     |     |     |

Seeds1: [asian,asian,asian,asia,china,asia] names white-Garg et al 2018
|         |                                  |     |     | Seeds1: | [harris,robinson,howard,thompson, |     |     |

| Seeds2: | [caucasian,caucasian,white,amer- |     |     |         |                                   |     |     |
moore,wright,anderson,clark,jackson,tay-
ica,america,europe]
lor,scott,davis,allen,adams,lewis,williams,
| • UsedIn: | Caliskanetal.(2017) |     |     | jones,wilson,martin,johnson] |                                   |     |     |

| SeedsID1: |                     |     |     | Seeds2:                      | [harris,nelson,robinson,thompson, |     |     |
female 2-Caliskan et al 2017 moore,wright,anderson,clark,jackson,tay-
| SeedsID2: |             |               |              | lor,scott,davis,allen,adams,lewis,williams, |     |     |     |

| male      | 2-Caliskan  | et al 2017    |              | jones,wilson,martin,johnson]                |     |     |     |
| Seeds     | 1: [sister, | mother, aunt, | grandmother, |                                             |     |     |     |
Figure2
daughter,she,hers,her]
| Seeds2: | [brother, | father, uncle, | grandfather, | • SeedsID:       |     |       |      |

|         |           |                |              | female-Kozlowski |     | et al | 2019 |
son,he,his,him]
|           |                 |     |     | Seeds:                      | [woman, | women, | she, her, her, hers, |

| • UsedIn: | Zhaoetal.(2018) |     |     | girl,girls,female,feminine] |         |        |                      |
SeedsID1:

| female | definition | words 1-Zhao | et al 2018 |        |            |       |      |

|        |            |              |            | female | 1-Caliskan | et al | 2017 |
SeedsID2:
|      |            |              |            | Seeds: | [sister,female,woman,girl,daughter, |     |     |

| male | definition | words 1-Zhao | et al 2018 |        |                                     |     |     |
she,hers,her]
| Seeds                                      | 1: [countrywoman, |     | sororal, witches, |            |     |     |     |

| maidservant,mothers,diva,actress,spinster, |                   |     |                   | • SeedsID: |     |     |     |
mama,duchesses,barwoman,countrywomen, definitional female-Bolukbasi et al 2016
1902

| Seeds:                       | [woman, | girl, | she, | mother, | daughter, |     | • Seeds2ID:          |                                       |     |            |     |     |

| gal,female,her,herself,Mary] |         |       |      |         |           |     | lowerclass-Kozlowski |                                       |     | et al 2019 |     |     |
| • SeedsID:                   |         |       |      |         |           |     | • Seeds1:            | [rich,richer,richest,affluence,afflu- |     |            |     |     |
female singular-Hoyle et al 2019 ent,expensive,luxury,opulent]
| Seeds: | [woman,girl,mother,daughter,sister, |        |          |        |           |     |           |                                  |     |     |     |     |

|        |                                     |        |          |        |           |     | • Seeds2: | [poor,poorer,poorest,poverty,im- |     |     |     |     |
| wife,  | aunt,                               | niece, | empress, | queen, | princess, |     |           |                                  |     |     |     |     |
poverished,inexpensive,cheap,needy]
| duchess, | lady, | dame, | waitress, |     | actress, | god- |     |     |     |     |     |     |

dess, policewoman, postwoman, heroine, • Seeds 1 Shuffled: [richer, opulent, luxury,
witch,stewardess,she] affluent,rich,affluence,richest,expensive]
| • SeedsID: |     |     |     |     |     |     | • Seeds | 2 Shuffled: | [poorer, |     | impoverished, |     |

female definition words 2-Zhao et al 2018 poorest, cheap, needy, poverty, inexpensive,
| Seeds:         | [lady,saleswoman,noblewoman,host- |      |          |     |          |        | poor] |     |     |     |     |     |

| ess, coquette, |                                   | nun, | heroine, |     | actress, | chair- |       |     |     |     |     |     |
Figure3(c)
woman,businesswoman,spokeswoman,wait-
ress, councilwoman, stateswoman, police- • UsedIn: Gargetal.(2018)
| woman,                                  | countrywomen, |     |     | horsewoman, |     | head- |             |              |     |         |     |     |

| mistress,governess,widow,witch,fiancee] |               |     |     |             |     |       | • Seeds1ID: |              |     |         |     |     |
|                                         |               |     |     |             |     |       | names       | chinese-Garg | et  | al 2018 |     |     |

• Seeds2ID:
| female | stereotype |            | words-Zhao |        | et al       | 2018 |       |               |     |            |     |     |

|        |            |            |            |        |             |      | names | hispanic-Garg |     | et al 2018 |     |     |
| Seeds: | [baker,    | counselor, |            | nanny, | librarians, |      |       |               |     |            |     |     |
socialite,assistant,tailor,dancer,hairdresser,
|            |              |     |        |               |     |       | • Seeds | 1: [chung, | liu,   | wong,     | huang, | ng, hu, |

| cashier,   | secretary,   |     | clerk, | stenographer, |     | op-   |         |            |        |           |        |         |
|            |              |     |        |               |     |       | chu,    | chen, lin, | liang, | wang, wu, | yang,  | tang,   |
| tometrist, | housekeeper, |     |        | bookkeeper,   |     | home- |         |            |        |           |        |         |
chang,hong,li]
maker,nurse,stylist,receptionist]
|            |     |     |     |     |     |     | • Seeds                                 | 2: [ruiz, | alvarez, | vargas, |     | castillo, |

| Figure3(a) |     |     |     |     |     |     | gomez,soto,gonzalez,sanchez,rivera,men- |           |          |         |     |           |
doza,martinez,torres,rodriguez,perez,lopez,
| • UsedIn: | Bolukbasietal.(2016) |     |     |     |     |     |     |     |     |     |     |     |

medina,diaz,garcia,castro,cruz]

|              |     |                  |     |     |            |     | • Seeds                 | 1 Shuffled: | [tang, | chang,     | chu,      | yang, |

| definitional |     | female-Bolukbasi |     |     | et al 2016 |     |                         |             |        |            |           |       |
|              |     |                  |     |     |            |     | wu, hong,               | huang,      | wong,  | hu,        | liu, lin, | chen, |
| • Seeds2ID:  |     |                  |     |     |            |     | liang,chung,li,ng,wang] |             |        |            |           |       |
| definitional |     | male-Bolukbasi   |     | et  | al 2016    |     |                         |             |        |            |           |       |
|              |     |                  |     |     |            |     | • Seeds                 | 2 Shuffled: | [ruiz, | rodriguez, |           | diaz, |
perez,lopez,vargas,alvarez,garcia,cruz,tor-
| • Seeds | 1: [she, | her, | woman, |     | Mary, | herself, |     |     |     |     |     |     |

res,gonzalez,soto,martinez,medina,rivera,
daughter,mother,gal,girl,female]
castillo,castro,mendoza,sanchez,gomez]
| • Seeds | 2: [he, | his, | man, | John, | himself, | son, |     |     |     |     |     |     |

Figure4(a)
father,guy,boy,male]
UsedIn:
|                                      |             |     |                          |      |          |      | •            | Bolukbasietal.(2016) |     |     |         |      |

| • Seeds1Shuffled:                    |             |     | [herself,woman,daughter, |      |          |      |              |                      |     |     |         |      |
| Mary,her,girl,mother,she,female,gal] |             |     |                          |      |          |      | • Seeds1ID:  |                      |     |     |         |      |
|                                      |             |     |                          |      |          |      | definitional | female-Bolukbasi     |     |     | et al   | 2016 |
| • Seeds                              | 2 Shuffled: |     | [man,                    | his, | he, son, | guy, |              |                      |     |     |         |      |
| himself,father,boy,male,John]        |             |     |                          |      |          |      | • Seeds2ID:  |                      |     |     |         |      |
|                                      |             |     |                          |      |          |      | definitional | male-Bolukbasi       |     | et  | al 2016 |      |
Figure3(b)
|     |     |     |     |     |     |     | • Seeds | 1: [she, | her, woman, |     | Mary, | herself, |

• UsedIn: Kozlowskietal.(2019) daughter,mother,gal,girl,female]
| • Seeds1ID:          |     |     |     |         |     |     | • Seeds              | 2: [he, his, | man, | John, | himself, | son, |

| upperclass-Kozlowski |     |     | et  | al 2019 |     |     | father,guy,boy,male] |              |      |       |          |      |
1903

| Figure4(b) |                  |     |     |     |     | shaniqua,tameisha,teretha,jasmine,latonya, |          |               |                  |

|            |                  |     |     |     |     | shanise,                                   | tanisha, | tia, lakisha, | latoya, sharise, |
| • UsedIn:  | N/A(randomseeds) |     |     |     |     |                                            |          |               |                  |
tashika,yolanda,lashandra,malika,shavonn,
tawanda,yvette,hakim,jermaine,kareem,ja-
• Seeds1ID:N/A
mal,rasheed,aisha,keisha,kenya,tamika]
• Seeds2ID:N/A
Figure5(BlackvsWhiteRoles)
| • Seeds1: | [negatives,vel,theirs,canoe,meet, |     |     |     |     |           |                    |     |     |

|           |                                   |     |     |     |     | • UsedIn: | Manzinietal.(2019) |     |     |
bilingual,mor,facets,fari,lily]

| • Seeds2: | [chun,brush,dictates,caesar,fewest, |     |     |     |     |       |               |     |         |

|           |                                     |     |     |     |     | black | roles-Manzini | et  | al 2019 |
breitbart,rod,heaped,julianna,longest]
| Figure4(c) |                      |     |     |     |     | • Seeds2ID: |               |           |                   |

|            |                      |     |     |     |     | caucasian   | roles-Manzini |           | et al 2019        |
| • UsedIn:  | Bolukbasietal.(2016) |     |     |     |     |             |               |           |                   |
|            |                      |     |     |     |     | • Seeds     | 1: [slave,    | musician, | runner, criminal, |

homeless]
| definitional | female-Bolukbasi |     |     | et  | al 2016 |         |              |            |                |

|              |                  |     |     |     |         | • Seeds | 2: [manager, | executive, | redneck, hill- |
• Seeds2ID:
billy,leader,farmer]
| definitional      | male-Bolukbasi |                        |     | et al | 2016 |     |     |     |     |

| • ShuffledSeeds1: |                | [female,she,woman,gal, |     |       |      |     |     |     |     |
her,daughter,girl,herself,mother,Mary]
| • Shuffled | Seeds | 2: [John, |     | man, | son, father, |     |     |     |     |

male,himself,guy,he,his]
Figure5(BlackvsWhiteNames)
| • UsedIn: | Knocheetal.(2019b) |     |     |     |     |     |     |     |     |

| white | names-Knoche |     | et al | 2019 |     |     |     |     |     |

• Seeds2ID:
| black   | names-Knoche |              | et al  | 2019    |        |     |     |     |     |

| • Seeds | 1: [adam,    | chip,        | harry, | josh,   | roger, |     |     |     |     |
| alan,   | frank,       | ian, justin, | ryan,  | andrew, | fred,  |     |     |     |     |
jack,matthew,stephen,brad,greg,jed,paul,
todd,brandon,hank,jonathan,peter,wilbur,
amanda,courtney,heather,melanie,sara,am-
| ber, crystal, |     | katie, meredith, |     | shannon, | betsy, |     |     |     |     |

donna,kristin,nancy,stephanie,bobbie-sue,
ellen,lauren,peggy,sue-ellen,colleen,emily,
| megan, | rachel, | wendy, | brendan, |     | geoffrey, |     |     |     |     |

brett,jay,neil,anne,carrie,jill,laurie,kristen,
sarah]
| • Seeds2: | [alonzo,jamel,lerone,percell,theo, |     |     |     |     |     |     |     |     |

alphonse,jerome,leroy,rasaan,torrance,dar-
| nell,      | lamar, lionel, | rashaun,  |         | tyree,  | deion, la- |     |     |     |     |

| mont,      | malik,         | terrence, | tyrone, | everol, | lavon,     |     |     |     |     |
| marcellus, | terryl,        | wardell,  |         | aiesha, | lashelle,  |     |     |     |     |
| nichelle,  | shereen,       | temeka,   |         | ebony,  | latisha,   |     |     |     |     |
1904

---
**Source PDF:** `2022_40_article.pdf`
