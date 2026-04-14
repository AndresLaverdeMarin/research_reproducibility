DialSummEval: Revisiting Summarization Evaluation for Dialogues
MingqiGao,XiaojunWan
WangxuanInstituteofComputerTechnology,PekingUniversity
TheMOEKeyLaboratoryofComputationalLinguistics,PekingUniversity
{gaomingqi,wanxiaojun}@pku.edu.cn
|     |     | Abstract |     |     |     |     | datasetandadoptROUGE(Lin,2004),ann-gram- |     |     |     |     |     |     |

basedautomaticevaluationmetricusingreference
| Dialogue | summarization |     | is  | receiving | increas- |     |     |     |     |     |     |     |     |

ing attention from researchers due to its ex- summaries, as the overall evaluation criterion for
|             |            |     |            |     |             |     | summary | quality, | complemented |     |     | by manual | eval- |

| traordinary | difficulty |     | and unique |     | application |     |         |          |              |     |     |           |       |
value. We observe that current dialogue sum- uation. Schluter (2017) and Graham (2015) illus-
marizationmodelshaveflawsthatmaynotbe
tratethelimitationsofROUGEinevaluatingsum-
well exposed by frequently used metrics such marization tasks. Also the manual evaluation pro-
| as ROUGE. | In  | our paper, |     | we re-evaluate |     | 18  |     |     |     |     |     |     |     |

tocolsvaryfromoneresearchtoanotherbasedon
| categories | of  | metrics | in terms | of  | four dimen- |     |     |     |     |     |     |     |     |

ourobservations.
| sions: | coherence,consistency,fluencyandrel- |     |     |     |     |     |     |     |     |     |     |     |     |

evance, aswellasaunifiedhumanevaluation We argue that the inadequate evaluation mech-
of various models in dialogue summarization anism may have become a major obstacle to the
for the first time. Some noteworthy trends progress of dialogue summarization researches.
whicharedifferentfromtheconventionalsum- Many studies, such as Chen and Yang (2020)
marizationtasksareidentified.Wewillrelease
|               |     |                 |     |             |     |        | and Tang          | et al.   | (2021),       | have                   | pointed | out | that the   |

| DialSummEval, |     | a multi-faceted |     | dataset     |     | of hu- |                   |          |               |                        |         |     |            |
|               |     |                 |     |             |     |        | current           | dialogue | summarization |                        | models  |     | still have |
| man judgments |     | containing      |     | the outputs |     | of 14  |                   |          |               |                        |         |     |            |
|               |     |                 |     |             |     |        | manyshortcomings, |          |               | suchaswrongreferences, |         |     | in-        |
modelsonSAMSum.1
|     |     |     |     |     |     |     | correct | reasoning | and | improper | gender |     | pronouns, |

## 1 Introduction
|                |      |        |             |     |          |         | and ROUGE  |         | may not  | reflect | these   | problems | ef-    |

|                |      |        |             |     |          |         | fectively. | For     | example, |         | Gabriel | et al.   | (2021) |
| Neural network |      | based  | approaches  |     | and      | sizable |            |         |          |         |         |          |        |
|                |      |        |             |     |          |         | note that  | ROUGE-1 |          | and     | ROUGE-L | fail     | to ac- |
| datasets       | have | led to | significant |     | progress | in      |            |         |          |         |         |          |        |
researches towards conventional summarization curately measure factual inconsistency across do-
tasks such as news and scientific papers (Lin and mains. Our case study in Table 1 also illustrates
|            |          |     |      |              |     |      | this point. | However, |     | it is | impractical | to  | perform |

| Ng, 2019). | Compared |     | with | conventional |     | sum- |             |          |     |       |             |     |         |
marization tasks, dialogue summarization has re- frequent time-consuming and costly manual eval-
ceived increasing attention from researchers due uation. The alternative is to introduce or propose
morereliableautomaticevaluationmetricstoeval-
toitsgreatdifficultyanduniqueapplicationvalue
uatethemodelsinamorecomprehensiveandfine-
| (Fengetal.,2021a).                      |     | Withtheproposalofdialogue |     |     |     |     |                |     |     |     |     |     |     |

| summarydatasetssuchasSAMSum(Gliwaetal., |     |                           |     |     |     |     | grainedmanner. |     |     |     |     |     |     |
2019), DialogSum (Chen et al., 2021) and Medi- Although there are automatic evaluation met-
aSum (Zhu et al., 2021), a number of models for rics for measuring the quality of all aspects of
| automatic | generation | of  | dialogue | summaries |     | have |           |     |              |     |               |     |        |

|           |            |     |          |           |     |      | summaries | on  | conventional |     | summarization |     | tasks, |
emerged(Fengetal.,2021b;LiuandChen,2021; especially for factual consistency (Huang et al.,
Zou et al., 2021; Qi et al., 2021; Chen and Yang, 2021), it is difficult to guarantee that they will
2020;ChenandYang,2021;Zhaoetal.,2020;Liu stillperformwellondialoguesummarizarion. Re-
etal.,2021). cently proposed automatic metrics for evaluating
There is no denying that these studies have generic natural language generation tasks such as
made promising progress, but it remains a chal- BERTScore (Zhang* et al., 2020), BARTScore
| lenge to | evaluate | these | advances |     | comprehen- |     |          |      |       |      |          |      |         |

|          |          |       |          |     |            |     | (Yuan et | al., | 2021) | have | also not | been | experi- |
sively. CurrentstudiesgenerallyusetheSAMSum mented on dialogue summarization. The high ab-
|     |     |     |     |     |     |     | straction | level, | low | extraction | rate, | and | the re- |

1Codeanddatawillbeavailableathttps://github.
com/kite99520/DialSummEval quirement for complex reasoning power of the
5693
Proceedingsofthe2022ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
HumanLanguageTechnologies,pages5693-5709
July10-15,2022©2022AssociationforComputationalLinguistics

| Dialogue            |     | ReferenceSummary | GeneratedSummary |     | R-1 R-2 | R-L |

| Kirsten: Youthgroup |     |                  |                  |     |         |     |
thisFriday,don’tbelate.
| Alex: Whattime?       |            | KirstenremindsAlex | Kirstenisgoing |     |           |      |

| Kirsten: 7pm.         | We’regoing | thattheyouthgroup  | bowlingwithher |     |           |      |
|                       |            |                    |                |     | 0.69 0.44 | 0.61 |
| bowling,sowe’llmeetup |            | meetsthisfridayat  | youthgroupthis |     |           |      |
| andthenallgotogether. |            | 7pmandgobowling.   | Fridayat7pm.   |     |           |      |
| Alex: Cool.           | Seeyou.    |                    |                |     |           |      |
| Kirsten: Bye          |            |                    |                |     |           |      |
Olawillbelate.
| Ola: Heyrunninglate |     | Olashouldbefree |     |     |     |     |

Sheshouldbe
| Ola: Ishouldbefreeby8   |     | by8. Kurtwantsher |          |      | 0.69 0.42 | 0.67 |

|                         |     |                   | freeby8. | Kurt |           |      |
| Kurt: Surenoprob,callme |     | tocallhim.        |          |      |           |      |
willcallher.
Table1:CasestudyofsomeoutputsofBARTonSAMSum.TheROUGEvaluesoftheseoutputshavesubstantially
exceededthestateoftheartonSAMSum. Thesummaryinthefirstrowfailsinrelevance, andthesecondhasa
factualerror.
dialogue summarization task present new chal- andPassonneau,2004),awidelyusedhumaneval-
lenges to automatic evaluation metrics. There uation method on several conventional summa-
havebeenanumberofmanualevaluationdatasets rization datasets to obtain relevance scores for
andanalyticalstudiesforconventionalsummariza- some of the system outputs and re-evaluated the
tion tasks ((Dang and Owczarzak, 2008); Fabbri metrics in 6 categories. Similarly, Fabbri et al.
etal.,2021b;Bhandarietal.,2020),butverylittle (2021b) used CNN/DailyMail dataset (Hermann
work has been done on systematic analysis of di- etal.,2015)andtheoutputofsomemodelsforhu-
aloguesummarizationmodelsandevaluationmet- man evaluation covering four facets of relevance,
rics. Our work will fill the gap in this area and consistency, fluency, and coherence, and then re-
includes the following contributions: 1) We iden- evaluated the metrics in 14 categories. None of
tify evaluation problems in the field of dialogue these involved dialogue summarization datasets.
summarizationandpointouttheurgentneedofau- Pagnoni et al. (2021) made a careful categoriza-
tomaticevaluationmetricsthatbetteradapttodia- tion of factual errors and benchmarked factuality
logue summarization. 2) We collect and provide metricsusinghumanannotationstheycollectedon
a sizable, multi-faceted dataset of manual evalua- CNN/DailyMailandXSumdataset(Narayanetal.,
tions for dialogue summarization, which contains 2018). Notably, Gabriel et al. (2021) is one of
the output of 14 models, and the dataset will be thefewcurrentstudiesusingthedialoguesumma-
released. 3)Were-evaluatetheperformanceof18 rization dataset SAMSum (Gliwa et al., 2019) for
typesofautomaticevaluationmetricsondialogue meta-evaluation, but it focuses on factual consis-
summarization. 4) We evaluate a variety of dia- tencyandselectsasmallnumberofmetrics.
| logue summarization | models | (extractive, abstrac- |     |     |     |     |

tive, and recently based on pre-trained language Analysis and Evaluation for Dialogue Sum-
models)inaunifiedmanner. marization Models Tang et al. (2021) and Chen
|     |     |     | and Yang  | (2020) sampled | the output | of models  |

|     |     |     | on SAMSum | and analyzes   | the error  | types when |
## 2 RelatedWork
|     |     |     | proposinganewmodel. |     | Duetothedifferentman- |     |

Meta-Evaluation with Human Judgments Au- ual evaluation protocols and the small number of
tomatic evaluation Metrics such as ROUGE (Lin, modelsincluded,itisdifficulttocomprehensively
2004) and BERTScore (Zhang* et al., 2020)) compare the strengths and weaknesses of differ-
werecomparedwithothermetricswhenproposed. ent models. Khalifa et al. (2021) designed sev-
However,theyarebasicallynotusingthedialogue eraltrickstoaddressthespecialchallengesindia-
summarization dataset as an experimental corpus, logue summarization and analysized their effects,
and rarely provide new human judgments data. such as using name substitution to cope with the
Bhandari et al. (2020) used pyramid (Nenkova presenceofmultiplespeakersindialogues. Zhang
5694

et al. (2021) focused on the problem of lengthy Metrics based on pre-trained language models
| inputandrelevantinformationlocationinlongdi- |     |     |     |     |     |     | include: |     |     |     |     |     |     |

alogue summarization, and compared the perfor- BERTScore(Zhang*etal.,2020)measuresthe
manceofsomemodelsandstrategies. Nomanual soft-overlapbetweentwotextsattokenlevelusing
contextualembeddingsfromBERT.5
evaluationwasinvolvedinthesestudies.
|                 |     |     |     |     |     |     | MoverScore                                 |     | (Zhao | et al., | 2019) | applies | the se- |

| 3 Preliminaries |     |     |     |     |     |     | manticdistancebetweentwotextsatn-gramlevel |     |       |         |       |         |         |
usingn-gramembeddingspooledfromBERT.6
In this section, we introduce the involved dataset, (Yuan et al., 2021) treats evalua-
BARTScore
metricsandmodels.
|     |     |     |     |     |     |     | tion as | a nature  | language | generation |     | task      | and as- |

|     |     |     |     |     |     |     | sumes   | that when | the      | quality    | of  | generated | text is |
### 3.1 Dataset
better,theconditionallanguagemodelhasahigher
SAMSum (Gliwa et al., 2019) is the first man- probability of generating it from the source text
ually annotated, high-quality chat summarization or the reference, or is more likely to generate the
dataset, containing over 16k dialogues. We use reference from it. It can be flexibly applied to
it in this study as it is most widely used and has evaluation of text from different perspectives us-
| greatly | promoted | the | research | in  | the field | of dia- | ingBART.7 |     |     |     |     |     |     |

logue summarization, and we are able to collect BLANC (Vasilyev et al., 2020) is a reference-
theoutputsofvariousmodelsonthisdataset.
|     |     |     |     |     |     |     | less metric.  | It  | hypothesizes |             | that | a good   | summary |

|     |     |     |     |     |     |     | is beneficial |     | for a        | pre-trained |      | language | model   |
### 3.2 EvaluationMetrics to conduct language understanding tasks on the
We selected a number of evaluation metrics that sourcedocument. Specifically,itmeasurestheper-
formanceboostofthemaskedlanguagemodeling
arefrequentlyusedonsummarizationorothernat-
|                              |     |     |     |                 |     |     | for BERT | utilizing | the | summary |     | in two | different |

| urallanguagegenerationtasks. |     |     |     | Someareforover- |     |     |          |           |     |         |     |        |           |

ways.
allquality;othersarespecifictoaparticularaspect.
Some require reference summaries or source doc- PPL, namely perplexity, is often used to evalu-
|                                      |     |     |     |     |     |      | ate the          | quality | of a language |       | model | or the   | fluency |

| uments;someonlyneedthesummaryitself. |     |     |     |     |     | Here |                  |         |               |       |       |          |         |
|                                      |     |     |     |     |     |      | of an utterance. |         | We            | adopt | GPT-2 | (Radford | et al., |
isabriefcategorizationanddescription.
|     |     |     |     |     |     |     | 2019) as | the | language | model | for | computing | the |

Metricsbasedonn-gramoverlapinclude:
|     |       |       |     |          |        |      | perplexityforthewholesummary. |     |     |     |     | 9   |     |

|     | (Lin, | 2004) | is  | the most | widely | used |                               |     |     |     |     |     |     |
ROUGE
| automaticevaluationmetricinsummarization. |     |     |     |     |     | Re- |     |     |     |     |     |     |     |

Metricsbasedonwordembeddingsinclude:
searchersmainlyadoptROUGE-1,ROUGE-2and
|          |       |         |     |     |                  |     | SMS   | (Clark      | et al., | 2019), | namely |        | Sentence |

| ROUGE-L, | which | measure |     | the | unigram-overlap, |     |       |             |         |        |        |        |          |
|          |       |         |     |     |                  |     | Mover | Similarity, | extends |        | Word   | Movers | Distance |
bigram-overlapandlongestcommonsequencebe-
|                            |     |     |     |     |     |     | (Kusner | et al., | 2015) | to measure |     | the distance | be- |

| tweentwotextsrespectively. |     |     |     | 2   |     |     |         |         |       |            |     |              |     |
tweentwotextswhicharerepresentedasabagof
| BLEU                                   | (Papineni |     | et al., | 2002) | is the | primary  |                     |     |         |           |     |     |         |

|                                        |           |     |         |       |        |          | sentenceembeddings. |     |         | 10        |     |     |         |
| evaluationmetricformachinetranslation. |           |     |         |       |        | Itcalcu- |                     |     |         |           |     |     |         |
|                                        |           |     |         |       |        |          | Embedding           |     | average | (Landauer |     | and | Dumais, |
latesn-gramoverlapbetweentextsusingprecision
|                                   |           |           |         |        |          |        | 1997) is   | an embedding |                | based          | metric    |            | computing |

| scoresandincludesabrevitypenalty. |           |           |         |        | 3        |        |            |              |                |                |           |            |           |
|                                   |           |           |         |        |          |        | the cosine | similarity   |                | between        | the       | embeddings | of        |
| METEOR                            |           | (Banerjee | and     | Lavie, | 2005)    | com-   |            |              |                |                |           |            |           |
|                                   |           |           |         |        |          |        | two texts. | A            | sentence-level |                | embedding |            | is repre- |
| putes an                          | alignment | by        | mapping |        | unigrams | in two |            |              |                |                |           |            |           |
|                                   |           |           |         |        |          |        | sented     | by averaging |                | the embeddings |           | of         | the words |
texts,basedonsurfaceforms,stemmedforms,and
composingthesentence.
meanings.
Vectorextrema(Forguesetal.,2014)isalsoan
| CHRF | (Popovic´, |     | 2015) | computes |     | character |     |     |     |     |     |     |     |

embeddingbasedmetricsimilartoEmbeddingav-

basedn-gramoverlapbetweentwotexts.
5https://github.com/Tiiiger/bert_score
6https://github.com/AIPHES/
| 2https://github.com/Diego999/py-rouge |      |                                |     |     |     |     | emnlp19-moverscore                   |     |     |     |     |     |     |

| 3Used                                 |      |                                |     |     |     |     | 7https://github.com/neulab/BARTScore |     |     |     |     |     |     |
|                                       | code | at https://github.com/Maluuba/ |     |     |     |     |                                      |     |     |     |     |     |     |
8https://github.com/PrimerAI/blanc
| nlg-eval, | the | same for | Embedding |     | average, | Vector ex- |     |     |     |     |     |     |     |

9https://huggingface.co/docs/
trema,GreedymatchingandMETEOR,providedby(Sharma
| etal.,2017) |     |     |     |     |     |     | transformers/perplexity |     |     |     |     |     |     |

4https://github.com/m-popovic/chrF 10https://github.com/eaclark07/sms
5695

erage. The metric computes a sentence-level em- to FactCC. When a sentence cannot be parsed by

bedding by taking the most extreme value of the themetric,wedefaultitfactuallyinconsistent.
embeddingsofthewordscomposingthesentence
|     |     |     |     |     |     |     | 3.3 SummarizationModels |     |     |     |     |     |     |

foreachdimensionoftheembedding.
Greedy matching (Rus and Lintean, 2012) We select some representative models and get the
is another embedding based metric. The metric outputs of them on the test set of SAMSum. We
does not compute a sentence-level embedding. It choose LEAD-3 and LONGEST-3 as representa-
directlycomparestheembeddingsofwordsinthe tives of the simple extractive approaches. PGN
(Seeetal.,2017)andTransformer(Vaswanietal.,
| two sentences |     | using | a greedy | matching | algorithm |     |     |     |     |     |     |     |     |

tocalculatesimilarity. 2017)areselectedasrepresentativesoftheearlier
|     |     |     |     |     |     |     | neural summarization |     |     | models. |     | For generic | pre- |

Metricsbasedonquestion-answeringinclude: trained generative models, we use BART (Lewis
|      |         |     |            |         |     |         | et al., 2020), | PEGASUS |     | (Zhang |     | et al., | 2020) and |

| FEQA | (Durmus | et  | al., 2020) | employs |     | a BERT- |                |         |     |        |     |         |           |
based question-answering model to answer ques- UniLM(Dongetal.,2019). Weretrainthesemod-
tionsusingsourcedocument. Questionsaregener- els above to obtain the outputs and the automatic
|     |     |     |     |     |     |     | evaluation | results | are | close | to Gliwa | et  | al. (2019) |

atedbyafine-tunedBARTmodelusinggenerated
|           |      |        |       |          |     |         | and Wu | et al. | (2021) | in default | settings. |     | For mod- |

| summaries | with | masked | named | entities | as  | inputs. |        |        |        |            |           |     |          |
The metric reports F1 scores against the gold an- els specifically designed for dialogue summariza-
swer, which are often regarded as a measure of tion, we choose CODS (Wu et al., 2021), Con-
|     |     | 11  |     |     |     |     | voSumm | (Fabbri | et  | al., 2021a), | MV-BART |     | (Chen |

factualconsistency.
andYang,2020),PLM-BART(Fengetal.,2021c),
SummaQA(Scialometal.,2019)isalsoaQA-
basedmetric. UnlikeFEQA,itgeneratesquestions Ctrl-DiaSumm (Liu and Chen, 2021), S-BART
(ChenandYang,2021)andtheoutputsareallpro-
| from source  | documents |          | instead | of        | summaries | to     |          |       |          |     |      |        |            |

|              |           |          |         |           |           |        | vided by | their | authors. | We  | also | regard | the refer- |
| be evaluated |           | and then | uses    | summaries | to        | answer |          |       |          |     |      |        |            |
them. The F1 overlap score and QA-model confi- encesummaryasakindofmodeloutput.
| dencearereported. |     | 12       |     |            |            |     |                  |     |     |     |     |     |     |

|                   |     |          |     |            |            |     | 4 DataAnnotation |     |     |     |     |     |     |
| QuestEval         |     | (Scialom | et  | al., 2021) | is another | a   |                  |     |     |     |     |     |     |
QA-based metric. This metric can be considered 4.1 AnnotationSetup
| as a combination |         | of  | FEQA   | and      | SummaQA. | It   |             |     |            |     |              |     |           |

|                  |         |     |        |          |          |      | Since human |     | evaluation |     | is expensive |     | and time- |
| takes into       | account | the | scores | obtained | from     | both |             |     |            |     |              |     |           |
consuming,wedecidetorandomlysample100di-
| styles. | For | comparison |     | purposes, | We  | use the |     |     |     |     |     |     |     |

aloguesfromthetestsetofSAMSumandevaluate
reference-lessmode.13
thesummariesgeneratedbyallmodelsonthesedi-
|         |       |     |            |                |     |     | alogues.   | Tocomprehensivelyevaluateeachmetric |         |       |            |     |         |

| Metrics | based | on  | entailment | classification |     | in- |            |                                     |         |       |            |     |         |
|         |       |     |            |                |     |     | and model, | we                                  | perform | human | evaluation |     | in four |
clude:
aspects,asinKryscinskietal.(2019):
FactCC (Kryscinski et al., 2020) is a metric measures the quality of all sen-
Coherence
| based on                     | entailment |     | classification. |                | We follow | the |           |             |     |     |          |            |     |

|                              |            |     |                 |                |           |     | tences in | the summary |     | as  | a whole. | It focuses | on  |
| wayPagnonietal.(2021)usedit. |            |     |                 | Eachsentenceof |           |     |           |             |     |     |          |            |     |
whetherthesummaryiscoherentandnatural.
thesummaryisfedintotheclassifiertogetherwith
|              |     |                |     |               |           |      | Consistency |     | measures |     | how well | the        | summary |

| the document |     | to determine   |     | whether       | the facts | are  |             |     |          |     |          |            |         |
|              |     |                |     |               |           |      | aligns with | the | dialogue | in  | facts.   | It focuses | on      |
| consistent,  | and | the proportion |     | of consistent |           | sen- |             |     |          |     |          |            |         |
whetherthesummarycontainsfactualerrors.
| tences is | used | to indicate | how | consistent | the | sum- |     |     |     |     |     |     |     |

Fluencymeasuresthequalityofindividualsen-

| maryis. |     |     |     |     |     |     | tencesinthesummarycomparedtoCoherence. |     |     |     |     |     | It  |

DAE(GoyalandDurrett,2020;GoyalandDur-
focusesonwhetherthesentencesarewell-written
| rett, 2021) | is  | an entailment |     | classification |     | metric |     |     |     |     |     |     |     |

andgrammaticallycorrect.
| basedondependencies. |     |     | Weuseitinasimilarway |     |     |     |                                    |     |          |     |      |     |           |

|                      |     |     |                      |     |     |     | Relevance                          |     | measures | how | well | the | summary   |
|                      |     |     |                      |     |     |     | capturesthekeypointsofthedialogue. |     |          |     |      |     | Itfocuses |
11https://github.com/esdurmus/feqa
12https://github.com/ThomasScialom/ on whether all and only the important aspects are
| summa-qa |     |     |     |     |     |     | containedinthesummary. |     |     |     |     |     |     |

13https://github.com/ThomasScialom/
| QuestEval                              |     |     |     |     |     |     | 15https://github.com/tagoyal/ |     |     |     |     |     |     |

| 14https://github.com/salesforce/factCC |     |     |     |     |     |     | factuality-datasets           |     |     |     |     |     |     |
5696

Toensurethequalityoftheannotation,wetried We required each annotator to annotate all data
|     |     |     |     |     |     |     | (100 | 14 = | 1400 |     |     |     |     |

to annotate some of the data ourselves at the be- annotations)toensurethecon-
×
ginning to judge the difficulty of the task and the sistency within the annotator. 3) During the anno-
approximatetimespent. tation process, we kept in touch with the annota-
|                       |     |     |     |     |     |     | tors via                 | email | or instant | messaging |     | app to | answer |

| 4.2 AnnotationProcess |     |     |     |     |     |     | theirquestionsatanytime. |       |            |           |     |        |        |
Weinitiallytriedtoannotatethedatausingcrowd- It took around 10 days to finish the annotation.
| sourcing | platforms. |            | We published |      | the | annotation |                   |     |        |                          |          |             |     |

|          |            |            |              |      |     |            | We received       |     | 100 14 |                          | 3 = 4200 | annotations |     |
|          |            |            |              |      |     |            |                   |     | ×      | ×                        |          |             |     |
| task on  | Amazon     | Mechanical |              | Turk | 16. | The in-    |                   |     |        |                          |          |             |     |
|          |            |            |              |      |     |            | foreachperspectiv |     | e.     | Fo reachaspectofeachsum- |          |             |     |
terface contained instructions and definitions of mary, if two scores were the same and the other
| the four | aspects. | A   | dialogue | and | a correspond- |     |     |     |     |     |     |     |     |

wasdifferentfromthem,weconsideredthediffer-
| ing summary |     | were included |     | in the | interface, | and |                |     |                            |     |     |     |     |

|             |     |               |     |        |            |     | entoneasnoise. |     | Foreachdimension,weremoved |     |     |     |     |
thesummariesofdifferentmodelsonthesamedi- the noise separately and calculated the the Krip-
alogue were presented to the annotators in a se- pendorff’s alpha coefficient (Krippendorff, 2011).
| quence | to facilitate |     | comparison. |     | For each | dimen- |          |     |                 |     |          |        |     |

|        |               |     |             |     |          |        | We found | the | inter-annotator |     | interval | metric | to  |
sion/aspect,annotatorswereaskedtoratethesum-
|     |     |     |     |     |     |     | be within | an  | acceptable | range | -   | from 0.5621 | to  |

mary on a Likert scale from 1 to 5. Each sum- 0.7564, as detailed in Table 2. The raw anno-
marywasevaluatedby5differentannotators,and
tateddatawillbereleasedandweusethecleaned
| For each | dimension |     | we would | receive |     | a total of |          |           |     |       |        |             |     |

|          |           |     |          |         |     |            | data for | analysis. | At  | last, | we use | the average | of  |
100 14 5 = 7000humanannotations. Thean- thecleaneddatatorepresentthehumanevaluation
| ×   | ×   |     |     |     |     |     |     |     |     |     |     |     |     |

notationwasdonequicklyinoneday,butthequal- scoreofansummaryonadimension.
| itywasnotsatisfactory. |     |     | Wecalculatedtheaverage |     |     |     |     |     |     |     |     |     |     |

scoreofeachmodelineachaspectbasedonthese
annotation data and found that the scores of the 5 MetricEvaluation
| models                         | are close    | in         | each dimension, |     | which         | is not      |          |                 |         |           |             |         |         |

| intheaccordancewiththereality. |              |            |                 |     | Forexample,in |             |          |                 |         |           |             |         |         |
|                                |              |            |                 |     |               |             | In this  | section,        | we will | introduce |             | several | defini- |
| terms of                       | consistency, |            | the reference   |     | summary       | and         |          |                 |         |           |             |         |         |
|                                |              |            |                 |     |               |             | tions in | meta-evaluation |         | and       | re-evaluate | the     | met-    |
| the extractive                 |              | approaches | should          |     | have          | had a defi- |          |                 |         |           |             |         |         |
niteadvantage,butthisfailedtobereflectedfrom ricsmentionedinSection3.2.
| thedata. | TheresultisshowninTable5. |     |     |     |     | Forrelia- |     |     |     |     |     |     |     |

bilityreasons,wedonotusetheseannotationsfor
| ouranalysis. |     |     |     |     |     |     | 5.1 TaskFormulation |     |     |     |     |     |     |

Then,wedecidedtorecruitannotatorsfromthe
|        |       |         |          |     |       |            | As mentioned |     | by Bhandari |         | et al. (2020), | there       | are |

| school | forum | who are | required |     | to be | capable of |              |     |             |         |                |             |     |
|        |       |         |          |     |       |            | two common   |     | ways to     | measure | the            | correlation | of  |
readingdailyconversationsandarticlesinEnglish
fluently. We recruited three annotators, using a automaticevaluationmetricstomanualevaluation:
similar annotation interface and approach as in system-levelandsummary-level.
the crowd-sourcing platforms. These annotators Assuming there are N dialogues, the i-th dia-
| were college | students        |     | and  | they | are fluent     | in En- |                       |     |           |     |               |         |        |

|              |                 |     |      |      |                |        | logueisrepresentedasd |     |           | .   | Foradialogued |         | ,there |
|              |                 |     |      |      |                |        |                       |     |           | i   |               |         | i      |
| glish.       | The differences |     | with | the  | crowd-sourcing |        |                       |     |           |     |               |         |        |
|              |                 |     |      |      |                |        | are J summaries       |     | generated |     | by J          | models, | and we |
platform annotation are as follows: 1) For a stu- denote each of them as s ,j = 1 J. There
ij
···
dent who wanted to participate in the annotation, are K evaluation metrics (or human evaluation)
| we would | ask | him to | annotate | all | models | on the |           |       |        |       |           |            |     |

|          |     |        |          |     |        |        | in total, | and m | refers | to an | automatic | evaluation |     |
k
| first10conversations(10 |     |     |     | 14 = | 140annotations), |     |                                             |     |     |     |     |     |     |

|                         |     |     | ×   |      |                  |     | metricorhumanevaluationofacertaindimension. |     |     |     |     |     |     |
andlether/himcontinuetheannotationonlywhen m (s ) means the score of k-th metric towards
k ij
theseannotationresultswerecheckedbyustocon-
|     |     |     |     |     |     |     | a pair of | dialogue | and | summary | (d  | ,s ). | We use |

i ij
| firm that | the | annotator | had | understood |     | the task |          |                                         |     |     |     |     |     |

|           |     |           |     |            |     |          | R(m i ,m | j )todenotethecorrelationcoefficientbe- |     |     |     |     |     |
correctly and could finish the annotation respon- tweentwometricsm andm .
|                                            |     |     |      |               |     |          |                                 |     |             | i   | j          |           |          |

| sibly. Otherwise,                          |     | we  | paid | the annotator |     | directly |                                 |     |             |     |            |           |          |
|                                            |     |     |      |               |     |          | System-level                    |     | correlation |     | is defined | as        | follows. |
| forthispartandterminatedhisannotationtask. |     |     |      |               |     | 2)       |                                 |     |             |     |            |           |          |
|                                            |     |     |      |               |     |          | The corresponding               |     | p-value     |     | which      | indicates | statis-  |
| 16https://www.mturk.com                    |     |     |      |               |     |          | ticalsignificancecanbeobtained: |     |             |     |            |           |          |
5697

|     |     |                     |      |         |     | Coherence                                    | Consistency                         |           | Fluency | Relevance   |           |                |        |

|     |     | cleaned             |      |         |     | 3161                                         | 3360                                |           | 3050    | 3439        |           |                |        |
|     |     | total               |      |         |     | 4200                                         | 4200                                |           | 4200    | 4200        |           |                |        |
|     |     | Krippendorff’salpha |      |         |     | 0.7564                                       | 0.6709                              |           | 0.6782  | 0.5621      |           |                |        |
|     |     |                     |      | Table2: |     | Theinter-annotatoragreementforeachdimension. |                                     |           |         |             |           |                |        |
|     |     |                     |      |         |     |                                              | evaluationfordialoguesummarization. |           |         |             |           | Acrossdi-      |        |
|     |     |                     |      |         |     |                                              | mensions,                           | almost    | all     | metrics     | correlate | better         | with   |
|     | R   | (m                  | ,m ) | = R(    |     |                                              |                                     |           |         |             |           |                |        |
|     | sys | p                   | q    |         |     |                                              | human                               | judgments | at      | the system  | level     | than           | at the |
|     |     |                     |      |         |     |                                              | summary                             | level,    | and     | both showed |           | good agreement |        |
|     | 1   | N                   |      |         | 1 N |                                              |                                     |           |         |             |           |                |        |
[ m (s ), , m (s )], with each other. This indicates that the summary-
|     | N   |     | p i1 | ··· | N   | p iJ |                                              |      |         |           |     |              |     |

|     |     | i=1 |      |     | i=1 |      | levelcorrelationsarealsoworthreferringtowhen |      |         |           |     |              |     |
|     |     | ∑   |      |     | ∑   |      |                                              |      |         |           |     |              |     |
|     |     | N   |      |     | N   |      |                                              |      |         |           |     |              |     |
|     | 1   |     |      |     | 1   |      | enough                                       | data | are not | available | for | system-level |     |
[ m q (s i1 ), , m q (s iJ )]) analysis. In addition, metrics such as BLEU and
|     | N   |       |     | ··· | N     |     |                 |            |                |        |                |            |          |

|     |     | ∑ i=1 |     |     | ∑ i=1 |     | CHRF,           | which      | are frequently |        | used           | in other   | natural  |
|     |     |       |     |     |       |     | language        | generation |                | tasks  | (e.g., machine |            | transla- |
|     |     |       |     |     |       |     | tion, dialogue, |            | etc.),         | do not | show           | advantages | on       |
Summary-levelcorrelationisdefinedasfollows,
dialoguesummarization.
andthep-valuecannotbederivedherebecausethe
|     |     |     |     |     |     |     | The characteristics |     |     | presented | by  | the automatic |     |

Summary-levelcorrelationisanaveragevalue:
evaluationmetricsonthedialoguesummarization
|     |     |     |     |     |     |     | differ from | those | of     | the conventional |         | summariza-      |     |

|     |     |     |     |     |     | N   | tion tasks. | For   | ROUGE, |                  | we find | that increasing |     |

|     |     | R   | (m  | ,m ) | =   | R(  |                                           |     |     |     |     |     |     |

|     |     | sum | p   | q    |     |     | thesizeofninROUGE-nisnotbetterinalmostall |     |     |     |     |     |     |
N
|     |     |     |     |     |     | i=1 | dimensions, | which | is  | different | from | the findings |     |

∑
[m p (s i1 ), ,m p (s iJ )], of Rankel et al. (2013) and Fabbri et al. (2021b).
···
[m (s ), ,m (s )]) The ability of ROUGE to reflect content selec-
|     |            | q   | i1  |     | q iJ |     |                                      |            |          |       |             |          |         |

|     |            |     |     | ··· |      |     | tion, i.e.,                          | relevance, |          | as we | usually     | believe, | is also |
|     |            |     |     |     |      |     | questionable.                        |            | Compared | to    | the results | of       | Fabbri  |
|     |            |     |     |     |      |     | et al. (2021b),                      |            | metrics  | based | on          | n-gram   | overlap |
| 5.2 | Discussion |     |     |     |      |     | suchasROUGEandCHRFperformworseondia- |            |          |       |             |          |         |
loguesummarization,whilesomemetricsthatuse
Comparingtheperformanceofvariousmetricsre-
sourcedocumentssuchasBLANCperformbetter.
| veals | some | trends | in  | Table | 3. In | each dimension, |         |          |     |     |             |          |     |

|       |      |        |     |       |       |                 | We need | to focus | on  | the | limitations | of ROUGE |     |
metricswhicharestronglycorrelatedwithhuman
|           |     |        |     |             |     |                  | and the | role of | the source |     | dialogues | in evaluating |     |

| judgments |     | exist, | but | few metrics |     | show significant |         |         |            |     |           |               |     |
dialoguesummaries.
| strengths |     | in all | four | dimensions. |     | Of all the met- |     |     |     |     |     |     |     |

rics, QuestEval has the most comprehensive ca- We have also observed some interesting phe-
pabilities at the system level. Generally metrics nomena. Entailment classification metrics such
that perform better on coherence and fluency per- as FactCC and DAE outperform many metrics
formworseonconsistencyandrelevance,andvice in terms of consistency, but not as well as
versa. Thiscanbeattributedtothedefinitionofthe BARTScore and QA-based metrics. This may be
dimensions,i.e. thereissomecorrelationbetween due to the large gap between the corpus used in
the four dimensions themselves, which is shown training and dialogues, and the need to slice the
in Figure 4. In all dimensions, automatic evalu- summaries by sentence when using them. FEQA,
ation metrics based on pre-trained language mod- whichisdesignedforfactualconsistency,however,
elsgenerallyoutperformmetricsbasedonn-gram performsbestincoherenceandfluency,andrather
overlapandcontext-independentwordembedding. poorly in consistency and relevance. Comparing
Among them, the recently proposed BARTScore its performance with QuestEval and SummaQA,
and the increasingly popular QA-based metrics generating questions from the original dialogue
perform the best. This suggests that both direc- may be more reliable in measuring consistency,
tionshavethepotentialtobeexploredintermsof whichcorroborateswiththepointsofGabrieletal.
5698

|                | Coherence |      | Consistency | Fluency |      | Relevance |       |

| Metrics        | sys       | sum  | sys sum     | sys     | sum  | sys       | sum   |
|                |           |      | 0.42 0.33   |         |      | 0.40      | 0.30  |
| ROUGE-1        | 0.59∗     | 0.30 |             | 0.58∗   | 0.27 |           |       |
| ROUGE-2        | 0.47      | 0.26 | 0.41 0.32   | 0.43    | 0.22 | 0.41      | 0.30  |
| ROUGE-3        | 0.39      | 0.22 | 0.39 0.30   | 0.33    | 0.17 | 0.40      | 0.30  |
| ROUGE-4        | 0.33      | 0.20 | 0.37 0.27   | 0.27    | 0.14 | 0.38      | 0.28  |
| ROUGE-L        | 0.57∗     | 0.32 | 0.39 0.30   | 0.54∗   | 0.27 | 0.37      | 0.27  |
| BERTScore-p    | 0.57∗     | 0.37 | 0.11 0.10   | 0.50    | 0.31 | 0.08      | 0.06  |
| BERTScore-r    | 0.43      | 0.21 | 0.45 0.38   | 0.42    | 0.20 | 0.46      | 0.39  |
|                | 0.53      |      | 0.28 0.24   | 0.48    |      | 0.27      | 0.22  |
| BERTScore-f1   |           | 0.31 |             |         | 0.27 |           |       |
| MoverScore     | 0.50      | 0.28 | 0.39 0.32   | 0.46    | 0.25 | 0.38      | 0.31  |
| SMS            | 0.33      | 0.18 | 0.38 0.28   | 0.27    | 0.14 | 0.40      | 0.29  |
| BARTScore-s-h+ | 0.09      | 0.08 | 0.62∗ 0.44  | 0.24    | 0.15 | 0.60∗     | 0.42  |
| BARTScore-h-   | 0.08      | 0.05 | -0.09 -0.09 | 0.16    | 0.13 | -0.18     | -0.12 |
| BARTScore-h-r  | 0.50      | 0.21 | 0.55∗ 0.46  | 0.51    | 0.21 | 0.56      | 0.46  |
∗
| BARTScore-r-h | 0.67∗∗ | 0.42  | 0.31 0.23 | 0.67∗∗ | 0.40  | 0.26  | 0.17 |

| BLANC-help+   | -0.32  | -0.21 | 0.54 0.45 | -0.13  | -0.08 | 0.60∗ | 0.50 |
| BLANC-tune+   | -0.37  | -0.23 | 0.50 0.38 | -0.18  | -0.10 | 0.56  | 0.43 |
∗
| FEQA+         | 0.82∗∗ | 0.27  | 0.32 0.16   | 0.84∗∗ | 0.26  | 0.25   | 0.10 |

| QuestEval+    | 0.50   | 0.15  |             |        | 0.20  |        | 0.37 |
|               |        |       | 0.85∗∗ 0.39 | 0.75∗∗ |       | 0.83∗∗ |      |
| SummaQA-conf+ | -0.08  | -0.03 | 0.64∗ 0.39  | 0.03   | -0.01 | 0.67∗∗ | 0.39 |
SummaQA-fscore+ -0.26 -0.11 0.58∗ 0.26 -0.06 -0.06 0.62∗ 0.29
| PPL-   | -0.13 | -0.01 | -0.49 -0.30 | -0.34 | -0.15 | -0.43 | -0.30 |

| CHRF   | 0.42  | 0.20  | 0.46 0.38   | 0.41  | 0.20  | 0.47  | 0.39  |
| BLEU-1 | 0.35  | 0.15  | 0.34 0.29   | 0.30  | 0.13  | 0.36  | 0.30  |
| BLEU-2 | 0.31  | 0.16  | 0.35 0.29   | 0.25  | 0.12  | 0.37  | 0.30  |
|        | 0.28  | 0.15  | 0.33 0.27   | 0.21  | 0.11  | 0.36  | 0.28  |
BLEU-3
| BLEU-4           | 0.25  | 0.14  | 0.33 0.25 | 0.17  | 0.09  | 0.36 | 0.28 |

| METEOR           | 0.37  | 0.19  | 0.42 0.35 | 0.33  | 0.17  | 0.43 | 0.35 |
| Embeddingaverage | 0.43  | 0.17  | 0.17 0.20 | 0.52  | 0.22  | 0.15 | 0.19 |
| Vectorextrema    | 0.47  | 0.22  | 0.35 0.28 | 0.43  | 0.21  | 0.35 | 0.26 |
| Greedymatching   | 0.43  | 0.21  | 0.35 0.31 | 0.43  | 0.21  | 0.36 | 0.30 |
| FactCC+          | -0.29 | -0.09 | 0.46 0.19 | -0.23 | -0.09 | 0.49 | 0.19 |
| DAE+             | -0.24 | -0.07 | 0.50 0.29 | -0.15 | -0.02 | 0.54 | 0.29 |
∗
Table 3: The correlation (Pearson’s r) of annotations computed on system level and summary level along four
qualitydimensionsbetweenautomaticmetricsandhumanjudgments. Forevaluation, allmetricsrequireatleast
thesummariestobeevaluatedasinput. Metricswith+indicatethatthesourcedialoguesareused,metricswith-
meansnootherinputarerequired, othersneedtousethereferencesummaries. Thefivemost-correlatedmetrics
in each column are bolded (For system level, **=significant for p 0.01, *=significant for p 0.05). We add
|     |     |     |     | ≤   |     |     | ≤   |

suffixestodistinguishthedifferentvariantsofmetrics.ForBARTScore,h,randsareabbreviationsofhypothesises,
references and source dialogues respectively. BARTScore-s-h measure the probability to generate hypothesises
usingsourcedialoguesasinputs, whileBARTScore-hmeasurestheprobabilitytogeneratehypothesiseswithout
other inputs, and so on. For BLANC, BLANC-tune refers to the way of fine-tuning on a generated summary
and then conducting nature language understanding tasks on source dialogues, while BLANC-help refers to the
wayofinferringwithageneratedsummaryconcatenatedtogether.ForSummaQA,SummaQA-fscoremeasuresthe
averageoverlapbetweenpredictionsandgroundtruthanswers,andSummaQA-confcorrespondstotheconfidence
ofthepredictions.
5699

| Models           |     |     | Coherence |     | Consistency |       | Fluency | Relevance |     | R-1   | R-2   |       | R-L |

| referencesummary |     |     | 4.500     |     |             | 4.370 | 4.560   | 4.210     |     | 1.000 | 1.000 | 1.000 |     |
| LONGEST-3        |     |     | 3.230     |     |             | 4.393 | 4.100   | 4.363     |     | 0.304 | 0.099 | 0.267 |     |
| LEAD-3           |     |     | 4.370     |     |             | 4.093 | 4.200   | 3.843     |     | 0.309 | 0.092 | 0.296 |     |
| PGN              |     |     | 3.568     |     |             | 2.103 | 3.657   | 2.293     |     | 0.356 | 0.126 | 0.357 |     |
| Tranformer       |     |     | 3.403     |     |             | 1.573 | 3.673   | 1.650     |     | 0.329 | 0.098 | 0.319 |     |
| BART             |     |     | 4.480     |     |             | 3.667 | 4.667   | 3.500     |     | 0.533 | 0.299 | 0.520 |     |
| PEGASUS          |     |     | 4.590     |     |             | 3.730 | 4.640   | 3.417     |     | 0.508 | 0.254 | 0.476 |     |
| UniLM            |     |     | 4.303     |     |             | 3.320 | 4.523   | 3.290     |     | 0.489 | 0.232 | 0.470 |     |
| CODS             |     |     | 4.268     |     |             | 3.637 | 4.567   | 3.397     |     | 0.523 | 0.278 | 0.509 |     |
| ConvoSumm        |     |     | 4.507     |     |             | 3.743 | 4.643   | 3.437     |     | 0.532 | 0.268 | 0.498 |     |
| MV-BART          |     |     | 4.320     |     |             | 3.937 | 4.660   | 3.747     |     | 0.539 | 0.290 | 0.513 |     |
|                  |     |     | 4.360     |     |             | 3.717 |         | 3.500     |     | 0.533 | 0.284 | 0.507 |     |
| PLM-BART         |     |     |           |     |             |       | 4.680   |           |     |       |       |       |     |
| Ctrl-DiaSumm     |     |     | 4.320     |     |             | 3.893 | 4.650   | 3.670     |     | 0.564 | 0.312 | 0.549 |     |
| S-BART           |     |     | 4.227     |     |             | 3.307 | 4.520   | 3.337     |     | 0.497 | 0.244 | 0.472 |     |
Table 4: Human ratings of summaries along four evaluation dimensions using cleaned annotations from campus
recruitment. Scoresareaveragedoverannotatorsforasummary,andscoresareaveragedoverallsummariesfora
model.ThetableisbrokendownbytheapproximateclassificationinSection3.3.Forcomparison,ROUGEvalues
calculatedusingoursamplingdataarealsoshown. Pleasenotethatthismaydifferfromtheresultsintheoriginal
| literature. | Thetwohighest-ratedmodelsineachcolumnareinbold. |     |     |     |     |     |     |     |     |     |     |     |     |

(2021). It is surprising that metrics based on the sistency. Since the average length of dialogues
language model such as PPL, BARTScore-h per- in SAMSum is small, extracting a few sentences
formspoorlyinmeasuringbothcoherenceandflu- from it can generally include important contents,
ency. Theexactreasonsforthisneedfurtherinves- sotherelevanceisalsohigh. Theevaluationofthe
| tigation. |     |     |     |     |     |     | extractive | models | raises | a qustion: |     | what | kind of |

summariesdoreadersactuallywant?
## 6 ModelEvaluation The early neural summrization models repre-
|         |            |     |          |      |       |      | sented        | by PGN | and | Transformer |          | perform | rela-  |

| In each | dimension, | we  | evaluate | each | model | men- |               |        |     |             |          |         |        |
|         |            |     |          |      |       |      | tively poorly | in     | all | dimensions  | compared |         | to the |
tioned in Section 3.3 using the average of the hu- reference summaries, especially consistency and
man evaluation scores of all summaries. Analyz- relevance. This is to be expected because of the
ingTable4,weconcludethefollowing.
|               |     |           |     |           |     |         | high difficulty |     | of dialogue | summarization |     |     | and the |

| The reference |     | summaries |     | in SAMSum |     | are not |                 |     |             |               |     |     |         |
smallsizeofSAMSumdataset.
perfect, and the annotators felt that they also con- An important finding is that the generic pre-
tained some factual inconsistencies compared to trained language models represented by BART,
| the source | dialogues, |     | as well | as  | important | ele- |         |     |        |     |         |          |      |

|            |            |     |         |     |           |      | PEGASUS | and | UniLM, | and | various | recently | pro- |
ments of the dialogues that were not all captured posed models specifically designed on the dia-
by them. However, comparing the human evalua- logue summarization task do not have significant
tionscoresofthereferencesummariesinCNNDM differences in each dimension. They are already
| (Fabbri | et al., 2021b), |     | the quality |     | is already | supe- |              |     |             |            |         |        |        |

|         |                 |     |             |     |            |       | comparable,  | and | in          | some cases | better, | in     | terms  |
| rior.   |                 |     |             |     |            |       | of coherence |     | and fluency | compared   |         | to the | refer- |
Extractive models produce summaries that dif- ence summaries. They have improved dramati-
fer in style from abstractive models, and many cally compared to earlier neural summarization
conversations contain ungrammatical utterances, models with respect to consistency and relevance,
which can affect the reading experience and im- but there is still some room for enhancement. On
pair their fluency and coherence. In particular, theonehand,thisfindingaffirmsthecapabilityof
LONGEST-3,whichextractssomepotentiallydis- these models; On the other hand, it urges us to re-
continuous sentences from dialogues, has low co- flect on how much these recently proposed com-
herence. However, since they do not modify the plex models or fancy techniques are an improve-
content, they still perform well in terms of con- ment over the generic pre-trained language mod-
5700

| els. |     |     |     |     |     |     | for their | helpful | comments. |     | Xiaojun | Wan | is the |

correspondingauthor.
## 7 Conclusion
| We point        | out | the             | problems | with    | the       | evaluation | References   |          |        |      |               |     |          |

| in the dialogue |     | summarization   |          | and     | introduce | Di-        |              |          |        |      |               |     |          |
|                 |     |                 |          |         |           |            | Satanjeev    | Banerjee | and    | Alon | Lavie.2005.   |     | METEOR:  |
| alSummEval,     |     | a multi-faceted |          | dataset |           | containing |              |          |        |      |               |     |          |
|                 |     |                 |          |         |           |            | An automatic |          | metric | for  | MT evaluation |     | with im- |
the output of various models and the correspond- proved correlation with human judgments. In Pro-
ing human judgments. Based on this dataset, we ceedings of the ACL Workshop on Intrinsic and Ex-
provide a comprehensive re-evaluation and analy- trinsic Evaluation Measures for Machine Transla-
|                         |                 |              |           |                       |      |           | tion and/or     | Summarization, |             |            | pages             | 65–72, | Ann Ar-   |

| sis of the              | performance     |              | of        | widely                | used | automatic |                 |                |             |            |                   |        |           |
|                         |                 |              |           |                       |      |           | bor, Michigan.  |                | Association |            | for Computational |        | Lin-      |
| evaluation              | metrics         |              | and each  | model.                |      | There are | guistics.       |                |             |            |                   |        |           |
| threeimportantfindings: |                 |              |           | 1)Fewmetricsareexcel- |      |           |                 |                |             |            |                   |        |           |
|                         |                 |              |           |                       |      |           | Manik Bhandari, |                | Pranav      | Narayan    | Gour,             | Atabak | Ash-      |
| lent in                 | all dimensions, |              | and       | the recently          |      | proposed  |                 |                |             |            |                   |        |           |
|                         |                 |              |           |                       |      |           | faq, Pengfei    | Liu,           | and         | Graham     | Neubig.           |        | 2020. Re- |
| BARTScore               |                 | and QA-based |           | metrics               | are  | compara-  |                 |                |             |            |                   |        |           |
|                         |                 |              |           |                       |      |           | evaluating      | evaluation     |             | in text    | summarization.    |        | In        |
| tively outstanding      |                 |              | and worth | exploring.            |      | 2) The    |                 |                |             |            |                   |        |           |
|                         |                 |              |           |                       |      |           | Proceedings     | of             | the 2020    | Conference |                   | on     | Empirical |
automatic evaluation metrics and their variants MethodsinNaturalLanguageProcessing(EMNLP),
pages9347–9359,Online.AssociationforComputa-
| present | some | trends | that | differ from | conventional |     |     |     |     |     |     |     |     |

tionalLinguistics.
| summarization.  |     | 3)  | A variety | of            | models | specif- |                            |     |     |     |                     |     |     |

| ically designed |     | for | dialogue  | summarization |        | per-    |                            |     |     |     |                     |     |     |
|                 |     |     |           |               |        |         | JiaaoChenandDiyiYang.2020. |     |     |     | Multi-viewsequence- |     |     |
formcomparablytoreferencesummariesinterms to-sequence models with conversational structure
|                                |             |              |           |           |               |            | forabstractivedialoguesummarization. |          |            |             |                 |               | InProceed- |

| of coherence                   |             | and fluency, |           | but still | have          | shortcom-  |                                      |          |            |             |                 |               |            |
|                                |             |              |           |           |               |            | ings of                              | the 2020 | Conference |             | on Empirical    |               | Methods    |
| ingsinconsistencyandrelevance. |             |              |           |           | Wehopethatre- |            |                                      |          |            |             |                 |               |            |
|                                |             |              |           |           |               |            | in Natural                           | Language |            | Processing  |                 | (EMNLP),      | pages      |
| searchers                      | in the      | field        | recognize | the       | importance    | of         |                                      |          |            |             |                 |               |            |
|                                |             |              |           |           |               |            | 4106–4118,                           | Online.  |            | Association | for             | Computational |            |
| evaluation                     | in          | current      | research, | choose    |               | some other | Linguistics.                         |          |            |             |                 |               |            |
| metrics                        | in addition |              | to ROUGE  |           | when          | evaluating |                                      |          |            |             |                 |               |            |
|                                |             |              |           |           |               |            | Jiaao Chen                           | and Diyi | Yang.      | 2021.       | Structure-aware |               | ab-        |
models,proposeautomaticevaluationmetricsthat
|     |     |     |     |     |     |     | stractive | conversation |     | summarization |     | via | discourse |

canbebetteradaptedtothefieldofdialoguesum-
|     |     |     |     |     |     |     | andactiongraphs. |     | InProceedingsofthe2021Con- |     |     |     |     |

marizationbasedonourwork. ferenceoftheNorthAmericanChapteroftheAsso-
|     |     |     |     |     |     |     | ciationforComputationalLinguistics: |     |     |       |            | HumanLan- |             |

|     |     |     |     |     |     |     | guage Technologies,                 |     |     | pages | 1380–1391, |           | Online. As- |
## 8 EthicalConsiderations
sociationforComputationalLinguistics.
| Whether | recruiting |     | annotators |     | through | Amazon |              |      |      |       |       |     |            |

|         |            |     |            |     |         |        | Yulong Chen, | Yang | Liu, | Liang | Chen, | and | Yue Zhang. |
MechanicalTurkorcampus,wepaidthem15dol-
|     |     |     |     |     |     |     | 2021. | DialogSum: |     | A real-life |     | scenario | dialogue |

lars per hour, more than the local average mini- summarization dataset. In Findings of the Associ-
|            |                                 |     |          |             |     |           | ation for   | Computational |            | Linguistics: |         | ACL-IJCNLP  |     |

| mumwage.   | Weremovedallcontentinthedataset |     |          |             |     |           |             |               |            |              |         |             |     |
|            |                                 |     |          |             |     |           | 2021, pages |               | 5062–5074, |              | Online. | Association | for |
| that might | contain                         |     | personal | information |     | about the |             |               |            |              |         |             |     |
ComputationalLinguistics.
annotators.
ElizabethClark,AsliCelikyilmaz,andNoahA.Smith.
Acknowledgements 2019. Sentencemover’ssimilarity: Automaticeval-
|     |     |     |     |     |     |     | uation | for multi-sentence |     | texts. |     | In Proceedings | of  |

the57thAnnualMeetingoftheAssociationforCom-
| We thank | all       | authors | for      | providing |     | the sum- |            |              |     |       |            |     |           |

|          |           |         |          |           |     |          | putational | Linguistics, |     | pages | 2748–2760, |     | Florence, |
| maries   | generated |         | by their | models.   |     | We thank |            |              |     |       |            |     |           |
Italy.AssociationforComputationalLinguistics.
| Baizhou | Huang | for | his | help in | the | process of |     |     |     |     |     |     |     |

retraining some models. This work was sup- Hoa Trang Dang and Karolina Owczarzak. 2008.
Overviewofthetac2008updatesummarizationtask.
| ported | by National |     | Science | Foundation |     | of China |     |     |     |     |     |     |     |

InTAC.
| (No. 62161160339), |                      |     | National | Key | RD    | Program  |          |           |     |        |       |      |          |

| of China           | (No.2018YFB1005100), |     |          |     | State | Key Lab- |          |           |     |        |       |      |          |
|                    |                      |     |          |     |       |          | Li Dong, | Nan Yang, |     | Wenhui | Wang, | Furu | Wei, Xi- |
oratory of Media Convergence Production Tech- aodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou,
|        |             |     |     |                |     |         | and Hsiao-Wuen |     | Hon. | 2019. |     | Unified | language |

| nology | and Systems |     | and | Key Laboratory |     | of Sci- |                |     |      |       |     |         |          |
modelpre-trainingfornaturallanguageunderstand-
| ence, Technology |     | and        | Standard    |           | in Press | Industry  |                   |     |                            |        |     |            |       |

|                  |     |            |             |           |          |           | ingandgeneration. |     | InAdvancesinNeuralInforma- |        |     |            |       |
| (Key Laboratory  |     | of         | Intelligent | Press     | Media    | Tech-     |                   |     |                            |        |     |            |       |
|                  |     |            |             |           |          |           | tion Processing   |     | Systems,                   | volume |     | 32. Curran | Asso- |
| nology).         | We  | appreciate | the         | anonymous |          | reviewers | ciates,Inc.       |     |                            |        |     |            |       |
5701

EsinDurmus,HeHe,andMonaDiab.2020. FEQA:A summarization. InProceedingsofthe2ndWorkshop
question answering evaluation framework for faith- on New Frontiers in Summarization, pages 70–79,
fulnessassessmentinabstractivesummarization. In Hong Kong, China. Association for Computational
Proceedingsofthe58thAnnualMeetingoftheAsso-
Linguistics.
| ciation for   | Computational |             | Linguistics, |                   | pages | 5055– |             |     |      |          |       |            |      |

|               |               |             |              |                   |       |       | Tanya Goyal | and | Greg | Durrett. | 2020. | Evaluating | fac- |
| 5070, Online. |               | Association |              | for Computational |       | Lin-  |             |     |      |          |       |            |      |
guistics. tuality in generation with dependency-level entail-
|     |     |     |     |     |     |     | ment. | In Findings | of  | the Association |     | for | Computa- |

Alexander Fabbri, Faiaz Rahman, Imad Rizvi, Borui tionalLinguistics: EMNLP2020,pages3592–3603,
Wang, Haoran Li, Yashar Mehdad, and Dragomir Online.AssociationforComputationalLinguistics.
| Radev. 2021a.                 |           | ConvoSumm: |          | Conversation |                 | summa- |                                |              |     |            |     |                |     |

|                               |           |            |          |              |                 |        | TanyaGoyalandGregDurrett.2021. |              |     |            |     | Annotatingand  |     |
| rization                      | benchmark | and        | improved |              | abstractive     | sum-   |                                |              |     |            |     |                |     |
|                               |           |            |          |              |                 |        | modeling                       | fine-grained |     | factuality | in  | summarization. |     |
| marizationwithargumentmining. |           |            |          |              | InProceedingsof |        |                                |              |     |            |     |                |     |
InProceedingsofthe2021ConferenceoftheNorth
the59thAnnualMeetingoftheAssociationforCom-
putational Linguistics and the 11th International American Chapter of the Association for Computa-
Joint Conference on Natural Language Processing tional Linguistics: Human Language Technologies,
|           |                                    |     |     |     |     |     | pages | 1449–1462, | Online. | Association |     | for | Compu- |

| (Volume1: | LongPapers),pages6866–6880,Online. |     |     |     |     |     |       |            |         |             |     |     |        |
tationalLinguistics.
AssociationforComputationalLinguistics.
|                      |            |        |           |               |               |       | Yvette Graham. |      | 2015.  | Re-evaluating |            | automatic | sum-    |

| Alexander            | R. Fabbri, |        | Wojciech  | Krys´cin´ski, |               | Bryan |                |      |        |               |            |           |         |
|                      |            |        |           |               |               |       | marization     | with | BLEU   | and           | 192 shades | of        | ROUGE.  |
| McCann,              | Caiming    | Xiong, |           | Richard       | Socher,       | and   |                |      |        |               |            |           |         |
|                      |            |        |           |               |               |       | In Proceedings |      | of the | 2015          | Conference | on        | Empiri- |
| DragomirRadev.2021b. |            |        | SummEval: |               | Re-evaluating |       |                |      |        |               |            |           |         |
calMethodsinNaturalLanguageProcessing,pages
| summarizationevaluation. |     |     | TransactionsoftheAsso- |     |     |     |                 |     |                               |     |     |     |     |

|                          |     |     |                        |     |     |     | 128–137,Lisbon, |     | Portugal.AssociationforCompu- |     |     |     |     |
ciationforComputationalLinguistics,9:391–409.
tationalLinguistics.
XiachongFeng,XiaochengFeng,andBingQin.2021a.
KarlMoritzHermann,TomasKocisky,EdwardGrefen-
| A survey | on  | dialogue | summarization: |     |     | Recent ad- |     |     |     |     |     |     |     |

stette,LasseEspeholt,WillKay,MustafaSuleyman,
| vances                       | and new | frontiers. |     | Computing |     | Research |                      |     |          |                        |           |             |     |

|                              |         |            |     |           |     |          | andPhilBlunsom.2015. |     |          | Teachingmachinestoread |           |             |     |
| Repository,arXiv:2107.03175. |         |            |     | Version1. |     |          |                      |     |          |                        |           |             |     |
|                              |         |            |     |           |     |          | and comprehend.      |     | Advances |                        | in neural | information |     |
Xiachong Feng, Xiaocheng Feng, Bing Qin, and Xin- processingsystems,28:1693–1701.
wei Geng. 2021b. Dialogue discourse-aware graph YichongHuang,XiachongFeng,XiaochengFeng,and
| model and   | data  | augmentation   |     | for | meeting       | sum-     |           |             |      |                |               |     |           |

|             |       |                |     |     |               |          | Bing Qin. | 2021.       | The  | factual        | inconsistency |     | prob-     |
| marization. |       | In Proceedings |     | of  | the Thirtieth | In-      |           |             |      |                |               |     |           |
|             |       |                |     |     |               |          | lem in    | abstractive | text | summarization: |               |     | A survey. |
| ternational | Joint | Conference     |     | on  | Artificial    | Intelli- |           |             |      |                |               |     |           |
ComputingResearchRepository,arXiv:2104.14839.
| gence, | IJCAI-21, | pages | 3808–3814. |     | International |     |     |     |     |     |     |     |     |

Version2.
| Joint Conferences |     | on  | Artificial | Intelligence |     | Organi- |     |     |     |     |     |     |     |

zation. MainTrack. MuhammadKhalifa,MiguelBallesteros,andKathleen
|     |     |     |     |     |     |     | McKeown.2021. |     | Abagoftricksfordialoguesum- |     |     |     |     |

XiachongFeng,XiaochengFeng,LiboQin,BingQin, InProceedingsofthe2021Conference
marization.
| and Ting | Liu. | 2021c. | Language |     | model | as an an- |     |     |     |     |     |     |     |

onEmpiricalMethodsinNaturalLanguageProcess-
| notator:                                       | Exploring      | DialoGPT |     | for      | dialogue | summa- |                      |           |             |                     |     |               |     |

|                                                |                |          |     |          |          |        | ing, pages8014–8022, |           |             | OnlineandPuntaCana, |     |               | Do- |
| rization.                                      | In Proceedings |          | of  | the 59th | Annual   | Meet-  |                      |           |             |                     |     |               |     |
|                                                |                |          |     |          |          |        | minican              | Republic. | Association |                     | for | Computational |     |
| ingoftheAssociationforComputationalLinguistics |                |          |     |          |          |        | Linguistics.         |           |             |                     |     |               |     |
andthe11thInternationalJointConferenceonNat-
uralLanguageProcessing(Volume1:LongPapers), Klaus Krippendorff. 2011. Computing krippendorff’s
| pages1479–1491,Online.AssociationforComputa- |     |     |     |     |     |     | alpha-reliability. |     |     |     |     |     |     |

tionalLinguistics.
WojciechKryscinski,NitishShirishKeskar,BryanMc-
|         |          |        |     |         |     |            | Cann, | Caiming | Xiong, | and | Richard | Socher. | 2019. |

| Gabriel | Forgues, | Joelle |     | Pineau, |     | Jean-Marie |       |         |        |     |         |         |       |
Larchevêque, and Réal Tremblay. 2014. Boot- Neuraltextsummarization: Acriticalevaluation. In
strapping dialog systems with word embeddings. Proceedings of the 2019 Conference on Empirical
In Nips, modern machine learning and natural Methods in Natural Language Processing and the
languageprocessingworkshop,volume2. 9th International Joint Conference on Natural Lan-
|                 |          |                   |       |                   |            |            | guage              | Processing | (EMNLP-IJCNLP), |             |     | pages | 540–     |

| Saadia Gabriel, |          | Asli Celikyilmaz, |       |                   | Rahul      | Jha, Yejin |                    |            |                 |             |     |       |          |
|                 |          |                   |       |                   |            |            | 551, Hong          | Kong,      | China.          | Association |     | for   | Computa- |
| Choi, and       | Jianfeng | Gao.              | 2021. |                   | GO FIGURE: | A          | tionalLinguistics. |            |                 |             |     |       |          |
| meta evaluation |          | of factuality     |       | in summarization. |            | In         |                    |            |                 |             |     |       |          |
Findings of the Association for Computational Lin- WojciechKryscinski,BryanMcCann,CaimingXiong,
guistics: ACL-IJCNLP 2021, pages 478–487, On- and Richard Socher. 2020. Evaluating the factual
line.AssociationforComputationalLinguistics. consistency of abstractive text summarization. In
|     |     |     |     |     |     |     | Proceedings | of  | the 2020 | Conference |     | on  | Empirical |

Bogdan Gliwa, Iwona Mochol, Maciej Biesek, and MethodsinNaturalLanguageProcessing(EMNLP),
Aleksander Wawer. 2019. SAMSum corpus: A pages9332–9346,Online.AssociationforComputa-
| human-annotated |     | dialogue |     | dataset | for | abstractive | tionalLinguistics. |     |     |     |     |     |     |

5702

Matt Kusner, Yu Sun, Nicholas Kolkin, and Kilian Artidoro Pagnoni, Vidhisha Balachandran, and Yulia
Weinberger. 2015. From word embeddings to doc- Tsvetkov.2021. Understandingfactualityinabstrac-
ument distances. In Proceedings of the 32nd In- tivesummarizationwithFRANK:Abenchmarkfor
ternational Conference on Machine Learning, InProceedingsofthe2021Con-
|     |     |     |     |     |     | vol- | factualitymetrics. |     |     |     |     |     |     |

ume 37 of Proceedings of Machine Learning Re- ferenceoftheNorthAmericanChapteroftheAsso-
search,pages957–966,Lille,France.PMLR. ciationforComputationalLinguistics: HumanLan-
|     |     |     |     |     |     |     | guage Technologies, |     | pages | 4812–4829, |     | Online. | As- |

Thomas K Landauer and Susan T. Dumais. 1997. A sociationforComputationalLinguistics.
| solutiontoplato’sproblem: |     |     |     | thelatentsemanticanal- |     |     |     |     |     |     |     |     |     |

ysis theory of acquisition, induction and represen- KishorePapineni,SalimRoukos,ToddWard,andWei-
|        |               |     |               |     |         |       | JingZhu.2002. |         | Bleu:        | amethodforautomaticeval- |     |             |     |

| tation | of knowledge. |     | Psychological |     | Review, | pages |               |         |              |                          |     |             |     |
|        |               |     |               |     |         |       | uation of     | machine | translation. |                          | In  | Proceedings | of  |
211–240.
the40thAnnualMeetingoftheAssociationforCom-
Mike Lewis, Yinhan Liu, Naman Goyal, Mar- putationalLinguistics,pages311–318,Philadelphia,
jan Ghazvininejad, Abdelrahman Mohamed, Omer Pennsylvania,USA.AssociationforComputational
| Levy, | Veselin | Stoyanov, |     | and | Luke | Zettlemoyer. | Linguistics. |     |     |     |     |     |     |

2020. BART:Denoisingsequence-to-sequencepre-
|     |     |     |     |     |     |     | Maja Popovic´. | 2015. | chrF: | character |     | n-gram | F-score |

trainingfornaturallanguagegeneration,translation,
|                   |         |        |                           |     |                   |     | forautomaticMTevaluation. |     |                |     | InProceedingsofthe  |     |     |

| andcomprehension. |         |        | InProceedingsofthe58thAn- |     |                   |     |                           |     |                |     |                     |     |     |
|                   |         |        |                           |     |                   |     | TenthWorkshop             |     | on Statistical |     | MachineTranslation, |     |     |
| nual              | Meeting | of the | Association               |     | for Computational |     |                           |     |                |     |                     |     |     |
Linguistics, pages 7871–7880, Online. Association pages 392–395, Lisbon, Portugal. Association for
| forComputationalLinguistics. |     |     |     |     |     |     | ComputationalLinguistics. |     |     |     |     |     |     |

Chin-Yew Lin. 2004. ROUGE: A package for auto- MengNan Qi, Hao Liu, YuZhuo Fu, and Ting Liu.
|                             |     |     |     |     |                  |     | 2021. | Improving | abstractive |     | dialogue | summariza- |     |

| maticevaluationofsummaries. |     |     |     |     | InTextSummariza- |     |       |           |             |     |          |            |     |
tionwithhierarchicalpretrainingandtopicsegment.
| tion Branches |     | Out, | pages | 74–81, | Barcelona, | Spain. |             |     |                 |     |     |               |     |

|               |     |      |       |        |            |        | In Findings | of  | the Association |     | for | Computational |     |
AssociationforComputationalLinguistics.
|     |     |     |     |     |     |     | Linguistics: | EMNLP2021,pages1121–1130,Punta |     |     |     |     |     |

HuiLinandVincentNg.2019. Abstractivesummariza- Cana,DominicanRepublic.AssociationforCompu-
| tion:  | A survey | of         | the state | of the        | art. | Proceedings   | tationalLinguistics. |         |     |       |        |       |       |

| of the | AAAI     | Conference |           | on Artificial |      | Intelligence, |                      |         |     |       |        |       |       |
|        |          |            |           |               |      |               | Alec Radford,        | Jeffrey | Wu, | Rewon | Child, | David | Luan, |
33(01):9815–9822.
|         |      |        |      |        |        |          | Dario Amodei, |     | Ilya             | Sutskever, | et        | al. 2019. | Lan-      |

|         |      |        |      |        |        |          | guage models  |     | are unsupervised |            | multitask |           | learners. |
| Junpeng | Liu, | Yanyan | Zou, | Hainan | Zhang, | Hongshen |               |     |                  |            |           |           |           |
OpenAIblog,1(8):9.
Chen,ZhuoyeDing,CaixiaYuan,andXiaojieWang.
| 2021.                      | Topic-aware |               | contrastive | learning           |     | for abstrac- |                                |     |         |                        |     |                |       |

|                            |             |               |             |                    |     |              | Peter A. Rankel,               |     | John M. | Conroy,                | Hoa | Trang          | Dang, |
| tivedialoguesummarization. |             |               |             | InFindingsoftheAs- |     |              |                                |     |         |                        |     |                |       |
|                            |             |               |             |                    |     |              | andAniNenkova.2013.            |     |         | Adecadeofautomaticcon- |     |                |       |
| sociation                  | for         | Computational |             | Linguistics:       |     | EMNLP        |                                |     |         |                        |     |                |       |
|                            |             |               |             |                    |     |              | tentevaluationofnewssummaries: |     |         |                        |     | Reassessingthe |       |
2021,pages1229–1243,PuntaCana,DominicanRe- Proceedings of the 51st Annual
|     |     |     |     |     |     |     | state of | the art. | In  |     |     |     |     |

public.AssociationforComputationalLinguistics.
|           |     |     |       |       |       |          | Meeting  | of the  | Association |          | for Computational |       | Lin-     |

|           |     |     |       |       |       |          | guistics | (Volume | 2: Short    | Papers), |                   | pages | 131–136, |
| Zhengyuan | Liu | and | Nancy | Chen. | 2021. | Control- |          |         |             |          |                   |       |          |
Sofia,Bulgaria.AssociationforComputationalLin-
| lable | neural | dialogue | summarization |     | with | personal |     |     |     |     |     |     |     |

guistics.
| named | entity | planning. | In  | Proceedings |     | of the 2021 |     |     |     |     |     |     |     |

Conference on Empirical Methods in Natural Lan- Vasile Rus and Mihai Lintean. 2012. An optimal as-
guageProcessing,pages92–106, OnlineandPunta sessment of natural language student input using
Cana,DominicanRepublic.AssociationforCompu- word-to-word similarity metrics. In International
tationalLinguistics.
|     |     |     |     |     |     |     | Conference | on  | Intelligent | Tutoring |     | Systems, | pages |

675–676.Springer.
| Shashi Narayan, |                        | Shay | B. Cohen, | and | Mirella         | Lapata. |                   |     |       |            |     |           |      |

| 2018.           | Don’tgivemethedetails, |      |           |     | justthesummary! |         |                   |     |       |            |     |           |      |
|                 |                        |      |           |     |                 |         | Natalie Schluter. |     | 2017. | The limits | of  | automatic | sum- |
topic-aware convolutional neural networks for ex- marisationaccordingtoROUGE. InProceedingsof
treme summarization. In Proceedings of the 2018 the15thConferenceoftheEuropeanChapterofthe
Conference on Empirical Methods in Natural Lan- Association for Computational Linguistics: Volume
guageProcessing, pages1797–1807, Brussels, Bel- 2, Short Papers, pages 41–45, Valencia, Spain. As-
gium.AssociationforComputationalLinguistics.
sociationforComputationalLinguistics.
AniNenkovaandRebeccaPassonneau.2004. Evaluat- ThomasScialom,Paul-AlexisDray,SylvainLamprier,
ing content selection in summarization: The pyra- Benjamin Piwowarski, Jacopo Staiano, Alex Wang,
mid method. In Proceedings of the Human Lan- and Patrick Gallinari. 2021. QuestEval: Summa-
guage Technology Conference of the North Ameri- rization asks for fact-based evaluation. In Proceed-
can Chapter of the Association for Computational ings of the 2021 Conference on Empirical Methods
Linguistics: HLT-NAACL 2004, pages 145–152, inNaturalLanguageProcessing,pages6594–6604,
Boston,Massachusetts,USA.AssociationforCom- OnlineandPuntaCana,DominicanRepublic.Asso-
| putationalLinguistics. |     |     |     |     |     |     | ciationforComputationalLinguistics. |     |     |     |     |     |     |

5703

Thomas Scialom, Sylvain Lamprier, Benjamin Pi- Yusen Zhang, Ansong Ni, Tao Yu, Rui Zhang, Chen-
wowarski, and Jacopo Staiano. 2019. Answers guang Zhu, Budhaditya Deb, Asli Celikyilmaz,
unite! unsupervised metrics for reinforced summa- Ahmed Hassan Awadallah, and Dragomir Radev.
|     |     |     | Proceedings |     | of the | 2019 Con- |     |     |     |     |     |     |     |

rization models. In 2021. An exploratory study on long dialogue
ferenceonEmpiricalMethodsinNaturalLanguage summarization: What works and what’s next. In
Processing and the 9th International Joint Confer- Findings of the Association for Computational Lin-
ence on Natural Language Processing (EMNLP- guistics: EMNLP 2021, pages 4426–4433, Punta
IJCNLP),pages3246–3256,HongKong,China.As- Cana,DominicanRepublic.AssociationforCompu-
| sociationforComputationalLinguistics. |     |     |     |     |     |     | tationalLinguistics. |     |     |     |     |     |     |

AbigailSee,PeterJ.Liu,andChristopherD.Manning. LuluZhao,WeiranXu,andJunGuo.2020. Improving
2017. Gettothepoint: Summarizationwithpointer- abstractivedialoguesummarizationwithgraphstruc-
generatornetworks. InProceedingsofthe55thAn- tures and topic words. In Proceedings of the 28th
nual Meeting of the Association for Computational InternationalConferenceonComputationalLinguis-
Linguistics (Volume 1: Long Papers), pages 1073– tics, pages 437–449, Barcelona, Spain (Online). In-
1083,Vancouver,Canada.AssociationforComputa- ternational Committee on Computational Linguis-
| tionalLinguistics. |     |     |     |     |     |     | tics. |     |     |     |     |     |     |

Shikhar Sharma, Layla El Asri, Hannes Schulz, and WeiZhao,MaximePeyrard,FeiLiu,YangGao,Chris-
Jeremie Zumer. 2017. Relevance of unsupervised tianM.Meyer,andSteffenEger.2019. MoverScore:
metricsintask-orienteddialogueforevaluatingnat- Text generation evaluating with contextualized em-
urallanguagegeneration. CoRR,abs/1706.09799. beddingsandearthmoverdistance. InProceedings
|     |     |     |     |     |     |     | of the | 2019 Conference |     | on Empirical |     | Methods | in  |

XiangruTang,ArjunNair,BoruiWang,BingyaoWang,
|             |       |         |        |          |          |           | Natural | Language         | Processing |            | and the  | 9th | Interna- |

| Jai Desai,  | Aaron | Wade,   | Haoran |          | Li, Asli | Celikyil- |         |                  |            |            |          |     |          |
|             |       |         |        |          |          |           | tional  | Joint Conference |            | on Natural | Language |     | Pro-     |
| maz, Yashar |       | Mehdad, | and    | Dragomir | Radev.   | 2021.     |         |                  |            |            |          |     |          |
|             |       |         |        |          |          |           | cessing | (EMNLP-IJCNLP),  |            | pages      | 563–578, |     | Hong     |
Confit: Toward faithful dialogue summarization Kong, China. Association for Computational Lin-
| with linguistically-informed |     |     |     | contrastive | fine-tuning. |     |     |     |     |     |     |     |     |

guistics.
ComputingResearchRepository,arXiv:2112.08713.
| Version1. |     |     |     |     |     |     | ChenguangZhu,YangLiu,JieMei,andMichaelZeng. |           |     |             |       |           |     |

|           |     |     |     |     |     |     | 2021.                                       | MediaSum: | A   | large-scale | media | interview |     |
OlegVasilyev,VedantDharnidharka,andJohnBohan-
|           |                                  |     |     |     |     |     | datasetfordialoguesummarization. |     |     |     | InProceedings |     |     |

| non.2020. | FillintheBLANC:Human-freequality |     |     |     |     |     |                                  |     |     |     |               |     |     |
ofthe2021ConferenceoftheNorthAmericanChap-
| estimationofdocumentsummaries. |     |     |     |     | InProceedings |     |     |     |     |     |     |     |     |

teroftheAssociationforComputationalLinguistics:
| of the | First Workshop |     | on Evaluation |     | and | Compari- |       |          |               |     |       |            |     |

|        |                |     |               |     |     |          | Human | Language | Technologies, |     | pages | 5927–5934, |     |
sonofNLPSystems, pages11–20, Online.Associa- Online.AssociationforComputationalLinguistics.
tionforComputationalLinguistics.
|                 |     |      |          |      |         |       | Yicheng       | Zou, Bolin | Zhu,                           | Xingwu | Hu, | Tao Gui, | and |

| Ashish Vaswani, |     | Noam | Shazeer, | Niki | Parmar, | Jakob |               |            |                                |        |     |          |     |
|                 |     |      |          |      |         |       | QiZhang.2021. |            | Low-resourcedialoguesummariza- |        |     |          |     |
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz tion with domain-agnostic multi-source pretraining.
| Kaiser,   | and Illia | Polosukhin. |     | 2017.  | Attention   | is all |                |     |             |            |     |     |         |

|           |           |             |     |        |             |        | In Proceedings |     | of the 2021 | Conference |     | on  | Empiri- |
| you need. | In        | Advances    | in  | neural | information | pro-   |                |     |             |            |     |     |         |
calMethodsinNaturalLanguageProcessing,pages
cessingsystems,pages5998–6008.
80–91,OnlineandPuntaCana,DominicanRepublic.
AssociationforComputationalLinguistics.
| Chien-Sheng | Wu, | Linqing | Liu,   | Wenhao | Liu,         | Pontus |     |     |     |     |     |     |     |

| Stenetorp,  | and | Caiming | Xiong. | 2021.  | Controllable |        |     |     |     |     |     |     |     |
A AnnotationInterface
| abstractive | dialogue |          | summarization |             | with | sketch su- |     |     |     |     |     |     |     |

| pervision.  | In       | Findings | of the        | Association |      | for Com-   |     |     |     |     |     |     |     |
Figure1andFigure2showtheinstructionsforan-
putational Linguistics: ACL-IJCNLP 2021, pages notation and definition of each aspect. They were
| 5108–5122, | Online. |     | Association | for | Computational |     |         |                 |     |        |         |     |        |

|            |         |     |             |     |               |     | read by | all annotators. |     | Figure | 3 shows | a   | source |
Linguistics.
dialogueandasummarytobeevaluated.
| Weizhe | Yuan, | Graham | Neubig, | and | Pengfei | Liu. |     |     |     |     |     |     |     |

2021. Bartscore: Evaluating generated text as B Correlationbetweendifferent
| text generation. |     | Computing |     | Research | Repository, |     |     |     |     |     |     |     |     |

dimensions
| arXiv:2106.11520. |     | Version2. |     |     |     |     |        |         |                  |     |             |     |     |

|                   |     |           |     |     |     |     | Figure | 4 shows | the system-level |     | correlation |     | be- |
JingqingZhang,YaoZhao,MohammadSaleh,andPe-
ter Liu. 2020. Pegasus: Pre-training with extracted tween coherence, consistency, fluency and rele-
| gap-sentencesforabstractivesummarization. |     |     |     |     |     | InIn- |                                                |     |     |     |     |     |     |

|                                           |     |     |     |     |     |       | vance. Consistencyisstronglycorrelatedwithrel- |     |     |     |     |     |     |
ternationalConferenceonMachineLearning,pages
evance.
11328–11339.PMLR.
TianyiZhang*,VarshaKishore*,FelixWu*,KilianQ. C Correlationbetweendifferentmetrics
| Weinberger,andYoavArtzi.2020.        |                 |     |      |       | Bertscore:       | Eval- |                        |         |                  |     |             |     |     |

|                                      |                 |     |      |       |                  |       | Figure                 | 5 shows | the system-level |     | correlation |     | be- |
| uating                               | text generation |     | with | bert. | In International |       |                        |         |                  |     |             |     |     |
| ConferenceonLearningRepresentations. |                 |     |      |       |                  |       | tweendifferentmetrics. |         |                  |     |             |     |     |
5704

D Reasonsfordiscardingdatafrom
AmazonMechanicalTurk
Table 5 shows the result of model evaluation us-
ing annotations from Amazon Mechanical Turk.
The performance of the models is indistinguish-
able,whichisnotconsistentwithourobservation.
E Theevaluationresultsforthemodels
wereproduced
Table 6 shows the value of ROUGE-1, ROUGE-
2 and ROUGE-L on the test set of SAMSum for
the models we reproduced. The results is close to
thoseinGliwaetal.(2019)andWuetal.(2021).
5705

Figure1: Instructionforannotatorsindatacollectioninterface.
Figure2: Definitionforannotatorsindatacollectioninterface.
5706

|                  | Figure3: Annotationexampleindatacollectioninterface. |           |             |                   |

| Models           |                                                      | Coherence | Consistency | Fluency Relevance |
| referencesummary |                                                      | 3.308     | 3.300       | 3.396 3.380       |
| LONGEST-3        |                                                      | 3.220     | 3.230       | 3.286 3.306       |
| LEAD-3           |                                                      | 3.256     | 3.228       | 3.312 3.334       |
| PGN              |                                                      | 3.260     | 3.206       | 3.336 3.280       |
| Tranformer       |                                                      | 3.240     | 3.248       | 3.294 3.320       |
| BART             |                                                      | 3.286     | 3.298       | 3.410 3.358       |
| PEGASUS          |                                                      | 3.354     | 3.360       | 3.356 3.302       |
| UniLM            |                                                      | 3.288     | 3.342       | 3.390 3.364       |
| CODS             |                                                      | 3.346     | 3.328       | 3.384 3.396       |
| ConvoSumm        |                                                      | 3.368     | 3.334       | 3.420 3.426       |
| MV-BART          |                                                      | 3.232     | 3.260       | 3.366 3.344       |
| PLM-BART         |                                                      | 3.302     | 3.284       | 3.360 3.432       |
| Ctrl-DiaSumm     |                                                      | 3.232     | 3.300       | 3.360 3.348       |
| S-BART           |                                                      | 3.358     | 3.400       | 3.354 3.380       |
Table5:HumanratingsofsummariesalongfourevaluationdimensionsusingdatafromAmazonMechanicalTurk.
Scoresareaveragedoverfiveannotators,brokendownbytheapproximateclassificationinSection3.3.
|     | Models     | ROUGE-1 | ROUGE-2 | ROUGE-L |

|     | LONGEST-3  | 30.60   | 9.61    | 27.96   |
|     | LEAD-3     | 30.89   | 8.97    | 29.86   |
|     | PGN        | 37.53   | 14.43   | 37.60   |
|     | Tranformer | 34.30   | 9.85    | 32.70   |
|     | BART       | 52.59   | 28.43   | 50.16   |
|     | PEGASUS    | 51.05   | 26.97   | 48.89   |
|     | UniLM      | 49.43   | 24.26   | 47.21   |
Table6: TheresultsofautomaticevaluationonthetestsetofSAMSum.
5707

Coherence Consistency Fluency Relevance
ecnerehoC
ycnetsisnoC
ycneulF
ecnaveleR
1.00
0.75
0.50
0.25
0.5
0.00
0.85 0.7
−0.25
−0.50
0.41 0.99 0.63
−0.75
−1.00
Figure4: Thecorrelation(Pearson’sr)betweendifferentdimensionsofhumanjudgmentsonsystemlevel.
5708

1-eguor 2-eguor 3-eguor 4-eguor l-eguor p_erocstreb r_erocstreb 1f_erocstreb erocsrevom sms h_s_erocstrab h_erocstrab r_h_erocstrab h_r_erocstrab pleh_cnalb enut_cnalb erocs_aqef lavetseuq borp_aqammus erocsf_aqammus lpp frhc 1_uelB 2_uelB 3_uelB 4_uelB ROETEM egarevA
gniddebmE
amertxE
rotceV
gnihctaM
ydeerG
slc_cctcaf ead
1.00
0.75
rouge-1
rouge-2
rouge-3
rouge-4
rouge-l
bertscore_p 0.50
bertscore_r
bertscore_f1
moverscore
sms
bartscore_s_h 0.25
bartscore_h
bartscore_h_r
bartscore_r_h
blanc_help
blanc_tune
0.00
feqa_score
questeval
summaqa_prob
summaqa_fscore
ppl
chrf −0.25
Bleu_1
Bleu_2
Bleu_3
Bleu_4
METEOR −0.50
Embedding Average
Vector Extrema
Greedy Matching
factcc_cls
dae
−0.75
−1.00
Figure5: Thecorrelation(Pearson’sr)betweendifferentautomaticevaluationmetricsonsystemlevel.
5709

---
**Source PDF:** `2023_18_article.pdf`
