Learning to Deceive with Attention-Based Explanations
DanishPruthi†,MansiGupta‡,BhuwanDhingra†,GrahamNeubig†,ZacharyC.Lipton†
†CarnegieMellonUniversity,Pittsburgh,USA
‡Twitter,NewYork,USA
ddanish@cs.cmu.edu,mansig@twitter.com,
{bdhingra, gneubig, zlipton}@cs.cmu.edu
Abstract Attention Biography Label
Attention mechanisms are ubiquitous compo- Ms.Xpracticesmedicine in
Original Memphis,TNand...Ms.X Physician
nentsinneuralarchitecturesappliedtonatural
speaksEnglishandSpanish.
language processing. In addition to yielding
gainsinpredictiveaccuracy,attentionweights Ms.Xpracticesmedicine in
Ours Memphis,TNand...Ms.X Physician
are often claimed to confer interpretability,
speaksEnglish andSpanish.
purportedlyusefulbothforprovidinginsights
topractitionersandforexplainingwhyamodel
Table 1: Example of an occupation prediction task
makes its decisions to stakeholders. We call
where attention-based explanation (highlighted) has
the latter use of attention mechanisms into
beenmanipulatedtowhitewashproblematictokens.
question by demonstrating a simple method
for training models to produce deceptive at- sometimes thought of intuitively as indicating
tentionmasks. Ourmethoddiminishestheto- which tokens the model focuses on when making
tal weight assigned to designated impermis-
a particular prediction. Based on this loose intu-
sible tokens, even when the models can be
ition, attention weights are often claimed to ex-
shown to nevertheless rely on these features
plainamodel’spredictions. Forexample,arecent
to drive predictions. Across multiple models
andtasks, ourapproachmanipulatesattention surveyonattention(Galassietal.,2019)remarks:
weightswhilepayingsurprisinglylittlecostin
“By inspecting the networks attention,
accuracy. Through a human study, we show
... one could attempt to investigate and
thatourmanipulatedattention-basedexplana-
understand the outcome of neural net-
tionsdeceivepeopleintothinkingthatpredic-
tions from a model biased against gender mi- works. Hence, weight visualization is
norities do not rely on the gender. Conse- nowcommonpractice.”
quently, our results cast doubt on attention’s
In another work, De-Arteaga et al. (2019) study
reliability as a tool for auditing algorithms in
gender bias in machine learning models for occu-
thecontextoffairnessandaccountability.1
pation classification. As machine learning is in-
## 1 Introduction
creasingly used in hiring processes for tasks in-
cluding resume filtering, the potential for bias
Since their introduction as a method for aligning
raises the spectre that automating this process
inputs and outputs in neural machine translation,
could lead to social harms. De-Arteaga et al.
attention mechanisms (Bahdanau et al., 2014)
(2019) use attention over gender-revealing tokens
have emerged as effective components in various
(e.g., ‘she’, ‘he’, etc.) to verify the gender bias
neural network architectures. Attention works by
in occupation classification models—stating that
aggregating a set of tokens via a weighted sum,
where the attention weights are calculated as a “the attention weights indicate which tokens are
most predictive”. Similar claims about atten-
function of both the input encodings and the state
tion’s utility for interpreting models’ predictions
ofthedecoder.
are common in the literature (Li et al., 2016; Xu
Because attention mechanisms allocate weight
et al., 2015; Choi et al., 2016; Xie et al., 2017;
among the encoded tokens, these coefficients are
MartinsandAstudillo,2016;LaiandTan,2019).
1The code and the datasets used in paper are
In this paper, we question whether attention
available at https://github.com/danishpruthi/
deceptive-attention scores necessarily indicate features that influence
4782
Proceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,pages4782–4793
July5-10,2020.(cid:13)c2020AssociationforComputationalLinguistics

a model’s predictions. Through a series of exper- tify alternate adversarial attention weights after
iments on diverse classification and sequence-to- the model is trained that nevertheless produce the
sequence tasks, we show that attention scores are samepredictions,andhenceclaimthatattentionis
surprisinglyeasytomanipulate. Wedesignasim- notexplanation. However,theseattentionweights
ple training scheme whereby the resulting mod- are chosen from a large (infinite up to numerical
els appear to assign little attention to a specified precision) set of possible values and thus it is not
set of impermissible tokens while continuing to surprisingthatmultipleweightsproducethesame
rely upon those features for prediction. The ease prediction. Moreoversincethemodeldoesnotac-
with which attention can be manipulated without tuallyproducetheseweights,theywouldneverbe
significantly affecting performance suggests that relied on as explanations in the first place. Simi-
even if a vanilla model’s attention weights con- larly, Serrano and Smith (2019) modify attention
ferred some insight (still an open and ill-defined valuesofatrainedmodelpost-hocbyhard-setting
question), these insights would rely on knowing thehighestattentionvaluestozero. Theyfindthat
theobjectiveonwhichmodelsweretrained. the number of attention values that must be ze-
Our results present troublesome implications roedouttoalterthemodel’spredictionisoftentoo
for proposed uses of attention in the context of large,andthusconcludethatattentionisnotasuit-
fairness,accountability,andtransparency. Forex- abletooltofordeterminingwhichelementsshould
ample,maliciouspractitionersaskedtojustifyhow be attributed as responsible for an output. In con-
theirmodelsworkbypointingtoattentionweights trasttothesetwopapers,wemanipulatetheatten-
couldmisleadregulatorswiththisscheme. Forin- tionviathelearningprocedure,producingmodels
stance,lookingatmanipulatedattention-basedex- whoseactualweightsmightdeceiveanauditor.
planation in Table 1, one might (incorrectly) as- In parallel work to ours, Wiegreffe and Pinter
sume that the model does not rely on the gen- (2019) examine the conditions under which at-
der prefix. To quantitatively study the extent of tentioncanbeconsideredaplausibleexplanation.
such deception, we conduct studies where we ask They design a similar experiment to ours where
human subjects if the biased occupation classi- they train an adversarial model, whose attention
fication models (like the ones audited by De- distribution is maximally different from the one
Arteaga et al. (2019)) rely on gender related in- produced by the base model. Here we look at
formation. We find that our manipulation scheme a related but different question of how attention
is able to deceive human annotators into believ- can be manipulated away from a set of impermis-
ing that manipulated models do not take gender sible tokens. Using human studies we show that
into account, whereas the models are heavily bi- our training scheme leads to attention maps that
asedagainstgenderminorities(see§5.2). are more deceptive, since people find them to be
Lastly,practitionersoftenoverlookthefactthat more believable explanations of the output (see
attention is typically not applied over words but §5.2). We also extend our analysis to sequence-
overfinallayerrepresentations,whichthemselves to-sequencetasks,andabroadersetofmodels,in-
capture information from neighboring words. We cludingBERT,andidentifymechanismsbywhich
investigatethemechanismsthroughwhichthema- themanipulatedmodelsrelyontheimpermissible
nipulated models attain low attention values. We tokensdespiteassigninglowattentiontothem.
note that (i) recurrent connections allow informa- Lastly, several papers deliberately train atten-
tiontoflow easily toneighboringrepresentations; tion weights by introducing an additional source
(ii) for cases where the flow is restricted, models ofsupervisiontoimprovepredictiveperformance.
tend to increase the magnitude of representations In some of these papers, the supervision comes
corresponding to impermissible tokens to offset from known word alignments for machine trans-
thelowattentionscores;and(iii)modelsaddition- lation (Liu et al., 2016; Chen et al., 2016), or by
ally rely on several alternative mechanisms that aligning human eye-gaze with model’s attention
varyacrossrandomseeds(see§5.3). forsequenceclassification(Barrettetal.,2018).
## 2 RelatedWork 3 ManipulatingAttention
Many recent papers examine whether attention is LetS = w ,w ,...,w denoteaninputsequence
1 2 n
avalidexplanationornot. Jainetal.(2019)iden- of n words. We assume that for each task, we are
4783

|     | Dataset |     |     |     |     |     |     |     |     | ImpermissibleTokens |     |     |

InputExample
|     | (Task) |     |     |     |     |     |     |     |     |     | (Percentage) |     |

CommonCrawlBiographies Ms.XpracticesmedicineinMemphis,TN GenderIndicators
(PhysicianvsSurgeon) andisaffiliatedwith... Ms.XspeaksEnglishandSpanish. (6.5%)
WikipediaBiographies Afterthat,Austenwaseducatedathomeuntil GenderIndicators
(GenderIdentification) shewenttoboardingschoolwithCassandraearlyin1785 (7.6%)
Goodfun,goodaction,goodacting,gooddialogue,goodpace,good
| SST+Wikipedia |     |     |     |     |     |     |     |     |     |     | SSTsentence |     |

cinematography.HelenMaxineLamondReddy(born25
| (SentimentAnalysis) |     |     |     |     |     |     |     |     |     |     | (45.5%) |     |

October1941)isanAustraliansinger,actress,andactivist.
ItiswithpleasurethatIamwritingthisletterinsupport
| ReferenceLetters       |     |     |     |     |                                          |     |     |     |     | Percentile,Rank |        |     |

|                        |     |     |     |     | of... Ihighlyrecommendherforaplaceinyour |     |     |     |     |                 |        |     |
| (AcceptancePrediction) |     |     |     |     |                                          |     |     |     |     |                 | (1.6%) |     |
institution.Percentile:99.0Rank:Extraordinary.
Table2:Examplesentencesfromeachclassificationtask,withhighlightedimpermissibletokensandtheirsupport.
given a pre-specified set of impermissible words etal.,2017)wecanoptimizethemeanvalueofour
I,forwhichwewanttominimizethecorrespond- penaltyasassessedoverthesetofattentionheads
| ingattentionweights. |     |     | Forexample,thesemayin- |     |     |     | Hasfollows: |     |     |     |     |     |

cludegenderwordssuchas“he”,“she”,“Mr.”,or
|        |                                   |     |     |     |     |     |     |     | λ   | (cid:88)     |     |     |

| “Ms.”. | Wedefinethemaskmtobeabinaryvector |     |     |     |     |     |     | R = | −   | log(1−αTm)). |     |     |
h
| ofsizen,suchthat |     |     |     |     |     |     |     |     | |H| |     |     |     |

h∈H
(cid:40)
|     |     |     | 1, ifw | ∈   | I   |     | Whenamodelhasmanyattentionheads,anau- |     |     |     |     |     |

|     |     | m = |        | i   |     |     |                                       |     |     |     |     |     |
i
|     |     |     | 0 otherwise. |     |     |     | ditormightnotlookatthemeanattentionassigned |       |     |              |      |         |

|     |     |     |              |     |     |     | to certain                                  | words | but | instead look | head | by head |
[0,1]n
| Further, | let     | α ∈  |      | denote      | the attention | as-       |              |              |               |              |              |        |

|          |         |      |      |             |               |           | to see       | if any among |               | them assigns | a large      | amount |
| signed   | to each | word | in S | by a model, |               | such that |              |              |               |              |              |        |
|          |         |      |      |             |               |           | of attention | to           | impermissible | words.       | Anticipating |        |
(cid:80)
| α   | = 1. Foranytask-specificlossfunctionL, |     |     |     |     |     |                                            |     |     |     |     |     |

| i i |                                        |     |     |     |     |     | this,wealsoexploreavariantofourapproachfor |     |     |     |     |     |
L(cid:48)
| we define | a new | objective |     | function |     | = L + R |     |     |     |     |     |     |

manipulatingmulti-headedattentionwherewepe-
| where   | R is an     | additive | penalty | term | whose      | pur-   |        |             |     |                     |     |         |

|         |             |          |         |      |            |        | nalize | the maximum |     | amount of attention |     | paid to |
| pose is | to penalize | the      | model   | for  | allocating | atten- |        |             |     |                     |     |         |
impermissiblewords(amongallheads)asfollows:
| tiontoimpermissiblewords. |     |     |     | Forasingleattention |     |     |     |     |                   |     |     |     |

| layer,wedefineRas:        |     |     |     |                     |     |     |     | R = | −λ·minlog(1−αTm). |     |     |     |
h
h∈H
−λlog(1−αTm)
R =
Forcaseswheretheimpermissiblesetoftokens
| and λ  | is a penalty | coefficient |          | that             | modulates | the |            |          |     |                   |     |         |

|        |              |             |          |                  |           |     | is unknown | apriori, |     | one can plausibly | use | the top |
| amount | of attention |             | assigned | to impermissible |           | to- |            |          |     |                   |     |         |
fewhighlyattendedtokensasaproxy.
αTm)
| kens. | The argument |     | of the | log term | (1  | −   |     |     |     |     |     |     |

capturesthetotalattentionweightassignedtoper-
## 4 ExperimentalSetup
| missible | words. | In  | contrast | to our | penalty | term, |     |     |     |     |     |     |

Wiegreffe and Pinter (2019) use KL-divergence We study the manipulability of attention on four
tomaximallyseparatetheattentiondistributionof binaryclassificationproblems,andfoursequence-
the manipulated model (α ) from the attention to-sequence tasks. In each dataset, (in some, by
new
distributionofthegivenmodel(α ): design)asubsetofinputtokensareknownapriori
old
tobeindispensableforachievinghighaccuracy.
|     | R(cid:48) | = −λKL(α |     | (cid:107) α | ).  | (1) |     |     |     |     |     |     |

|     |           |          |     | new         | old |     |     |     |     |     |     |     |
### 4.1 ClassificationTasks
| However, | their | penalty | term | is not | directly | appli- |     |     |     |     |     |     |

cabletoourcase: instantiatingα tobeuniform Occupation classification We use the biogra-
old
over impermissible tokens, and 0 over remainder phies collected by De-Arteaga et al. (2019) to
tokensresultsinanundefinedlossterm. studybiasagainstgender-minoritiesinoccupation
When dealing with models that employ multi- classificationmodels. Wecarveoutabinaryclas-
headed attention, which use multiple different at- sificationtaskofdistinguishingbetweensurgeons
tentionvectorsateachlayerofthemodel(Vaswani and(non-surgeon)physiciansfromthemulti-class
4784

occupation prediction setup. We chose this sub- racy improvements when using the rank and per-
task because the biographies of the two profes- centile features in addition to the reference let-
sions use similar words, and a majority of sur- ter. Thus, we consider percentile and rank labels
geons(> 80%)inthedatasetaremale. Wefurther (which are appended at the end of the letter text)
downsample minority classes—female surgeons, as impermissible tokens. An example from each
and male physicians—by a factor of ten, to en- classification task is listed in Table 2. More de-
couragemodelstousegenderrelatedtokens. Our tailsaboutthedatasetsareintheappendix.
| models | (described |     | in detail | later | in § | 4.2) attain |     |     |     |     |     |     |     |

### 4.2 ClassificationModels
| 96.4%     | accuracy    | on         | the task, | and      | are    | reduced to |           |     |           |     |     |              |      |

| 93.8%     | when        | the gender |           | pronouns | in the | biogra-    |           |     |           |     |     |              |      |
|           |             |            |           |          |        |            | Embedding | +   | Attention |     | For | illustrative | pur- |
| phies are | anonymized. |            | Thus,     | the      | models | (trained   |           |     |           |     |     |              |      |
poses,westartwithasimplemodelwithattention
| on unanonymized |     | data) | make | use | of gender | indi- |                             |     |     |     |     |               |     |

|                 |     |       |      |     |           |       | directlyoverwordembeddings. |     |     |     |     | Thewordembed- |     |
cators to obtain a higher task performance. Con- dings are aggregated by a weighted sum (where
sequently,weconsidergenderindicatorsasimper-
weightsaretheattentionscores)toformacontext
missibletokensforthistask.
vector,whichisthenfedtoalinearlayer,followed
Pronoun-based Gender Identification We byasoftmaxtoperformprediction. Forallourex-
periments,weusedot-productattention,wherethe
constructatoydatasetfromWikipediacomprised
|                 |     |     |       |                  |     |       | query vector | is  | a learnable |     | weight | vector. | In this |

| of biographies, |     | in  | which | we automatically |     | label |              |     |             |     |        |         |         |
biographieswithagender(femaleormale)based model,priortoattentionthereisnointeractionbe-
|           |              |     |     |        |           |       | tween the | permissible |     | and | impermissible |     | tokens. |

| solely on | the presence |     | of  | gender | pronouns. | To do |           |             |     |     |               |     |         |
Theembeddingdimensionsizeis128.
so,weuseapre-specifiedlistofgenderpronouns.
| Biographies   | containing |        | no       | gender         | pronouns,   | or         |                     |                |           |      |            |          |              |

|               |            |        |          |                |             |            | BiLSTM              | + Attention    |           | The  | encoder    |          | is a single- |
| pronouns      | spanning   |        | both     | classes        | are         | discarded. |                     |                |           |      |            |          |              |
|               |            |        |          |                |             |            | layer bidirectional |                |           | LSTM | model      | (Graves  | and          |
| The rationale |            | behind | creating | this           | dataset     | is that    |                     |                |           |      |            |          |              |
|               |            |        |          |                |             |            | Schmidhuber,        |                | 2005)     | with | attention, | followed | by           |
| due to        | the manner |        | in       | which          | the dataset | was        |                     |                |           |      |            |          |              |
|               |            |        |          |                |             |            | a linear            | transformation |           | and  | a softmax  |          | to perform   |
| created,      | attaining  |        | 100%     | classification |             | accuracy   |                     |                |           |      |            |          |              |
|               |            |        |          |                |             |            | classification.     | The            | embedding |      | and        | hidden   | dimen-       |
| is trivial    | if the     | model  | uses     | information    |             | from the   |                     |                |           |      |            |          |              |
sionsizearebothsetto128.
| pronouns. | However,withoutthepronouns,itmay |            |          |         |           |          |                |     |                 |     |     |      |            |

| not be    | possible                         | to achieve |          | perfect | accuracy. | Our      |                |     |                 |     |     |      |            |
|           |                                  |            |          |         |           |          | Transformer    |     | Models          | We  | use | the  | Bidirec-   |
| models    | trained                          | on         | the same | data    | with      | pronouns |                |     |                 |     |     |      |            |
|           |                                  |            |          |         |           |          | tional Encoder |     | Representations |     |     | from | Transform- |
anonymized,achieveatbest72.6%accuracy.
|               |          |        |         |            |             |           | ers (BERT) | model                                 | (Devlin    |        | et al., | 2019). | We use     |

|               |          |        |         |            |             |           | the base   | version                               | consisting |        | of 12   | layers | with self- |
| Sentiment     | Analysis |        | with    | Distractor |             | Sentences |            |                                       |            |        |         |        |            |
|               |          |        |         |            |             |           | attention. | Further,eachoftheself-attentionlayers |            |        |         |        |            |
| We use        | the      | binary | version | of         | Stanford    | Senti-    |            |                                       |            |        |         |        |            |
|               |          |        |         |            |             |           | consists   | of 12                                 | attention  | heads. | The     | first  | token of   |
| ment Treebank |          | (SST)  | (Socher | et         | al., 2013), | com-      |            |                                       |            |        |         |        |            |
prised of 10,564 movie reviews. We append every sequence is the special classification token
[CLS],whosefinalhiddenstateisusedforclassi-
| one randomly-selected |     |      | “distractor” |         | sentence  | to  |                |                               |     |     |     |     |     |

|                       |     |      |              |         |           |     | ficationtasks. | Toblocktheinformationflowfrom |     |     |     |     |     |
| each review,          |     | from | a set of     | opening | sentences | of  |                |                               |     |     |     |     |     |
Wikipediapages.2 Here,withoutrelyinguponthe permissible to impermissible tokens, we multi-
|        |        |                |     |     |       |            | ply attention | weights |      | at every | layer  | with | a self-  |

| tokens | in the | SST sentences, |     | a   | model | should not |               |         |      |          |        |      |          |
|        |        |                |     |     |       |            | attention     | mask    | M, a | binary   | matrix | of   | size n×n |
beabletooutperformrandomguessing.
|     |     |     |     |     |     |     | wherenisthesizeoftheinputsequence. |     |     |     |     |     | Anele- |

GraduateSchoolReferenceLetters Weobtain mentM representswhetherthetokenw should
|     |     |     |     |     |     |     |     | i,j |     |     |     |     | i   |

adatasetofrecommendationletterswrittenforthe attend on the token w . M is 1 if both i and j
j i,j
| purpose | of admission |     | to graduate |     | programs. | The |     |     |     |     |     |     |     |

belongtothesameset(eitherthesetofimpermis-
| task is | to predict | whether |     | the student, |     | for whom |               |     |        |            |     | Ic). |           |

|         |            |         |     |              |     |          | sible tokens, | I   | or its | complement |     |      | Addition- |
the letter was written, was accepted. The letters ally,the[CLS]tokenattendstoallthetokens,but
include students’ ranks and percentile scores as notokenattendsto[CLS]topreventtheinforma-
| marked | by their | mentors, |     | which | admissions | com- |           |         |     | Ic  |         |     |             |

|        |          |          |     |       |            |      | tion flow | between | I   | and | (Figure | 1   | illustrates |
mittee members rely on. Indeed, we notice accu- this setting). We attempt to manipulate attention
|          |           |     |         |                |            |     | from [CLS] | token | to  | other | tokens, | and | consider |

| 2Opening | sentences |     | tend to | be declarative | statements | of  |            |       |     |       |         |     |          |
factandtypicallyaresentiment-neutral. two variants: one where we manipulate the maxi-
4785

|     |     |     |     |     |     |     | arerestrictedtobeeven. |     |     | Weusetwosetsof100K |     |     |     |

unseenrandomsequencesfromthesamedistribu-
tionasthevalidationandtestset.
|     |     |     |     |     |     |     | Machine                   | Translation |        | (English |                  | to German) |        |

|     |     |     |     |     |     |     | Besides                   | synthetic   | tasks, | we       | also evaluate    |            | on En- |
|     |     |     |     |     |     |     | glishtoGermantranslation. |             |        |          | WeusetheMulti30K |            |        |
Figure1: Restrictedself-attentioninBERT.Theinfor- dataset, comprising of image descriptions (Elliott
mationflowthroughattentionisrestrictedbetweenim- etal.,2016). Sincethegoldtargettosourceword-
| permissible | and | permissible | tokens | for | every | encoder |     |     |     |     |     |     |     |

levelalignmentisunavailable,werelyontheFast
layer. Thearrowsrepresentthedirectionofattention. Align toolkit (Dyer et al., 2013) to align target
|     |     |     |     |     |     |     | words to | their | source | counterparts. |     | We use | these |

mumattentionacrossallheads,andonewherewe
alignedwordsasimpermissibletokens.
manipulatethemeanattention.
|     |     |     |     |     |     |     | For                | all sequence-to-sequence |     |               | tasks, |     | we use  |

|     |     |     |     |     |     |     | an encoder-decoder |                          |     | architecture. |        | Our | encoder |
### 4.3 Sequence-to-sequenceTasks
|           |         |            |     |                  |     |       | is a bidirectional |         | GRU, |          | and our     | decoder   | is a |

| Previous  | studies | analysing  | the | interpretability |     | of    |                    |         |      |          |             |           |      |
|           |         |            |     |                  |     |       | unidirectional     |         | GRU, | with     | dot-product | attention |      |
| attention | are all | restricted | to  | classification   |     | tasks |                    |         |      |          |             |           |      |
|           |         |            |     |                  |     |       | over source        | tokens, |      | computed | at each     | decoding  |      |
(Jainetal.,2019;SerranoandSmith,2019;Wiegr-
|           |         |            |          |           |            |       | timestep.4 | Wealsorunablationstudieswith(i)no |            |     |          |            |      |

| effe and  | Pinter, | 2019).     | Whereas, | attention |            | mech- |            |                                   |            |     |          |            |      |
|           |         |            |          |           |            |       | attention, | i.e.                              | just using | the | last (or | the first) | hid- |
| anism was | first   | introduced |          | for, and  | reportedly |       |            |                                   |            |     |          |            |      |
denstateoftheencoder;and(ii)uniformattention,
leadstosignificantgainsin,sequence-to-sequence
|     |     |     |     |     |     |     | i.e. allthesourcetokensareuniformlyweighted.5 |     |     |     |     |     |     |

tasks. Here,weanalysewhetherforsuchtasksat-
tentioncanbemanipulatedawayfromitsusualin-
|              |     |              |     |         |        |     | 5 ResultsandDiscussion |     |     |     |     |     |     |

| terpretation | as  | an alignment |     | between | output | and |                        |     |     |     |     |     |     |
input tokens. We begin with three synthetic Inthissectionweexaminehowloweringattention
sequence-to-sequence tasks that involve learning affects task performance (§ 5.1). We then present
simpleinput-to-outputmappings.3 experiments with human participants to quantify
|        |          |     |      |       |         |         | the deception |     | with manipulated |     | attention |     | (§ 5.2). |

| Bigram | Flipping | The | task | is to | reverse | the bi- |               |     |                  |     |           |     |          |
Lastly,weidentifyalternateworkaroundsthrough
| grams in  | the input | ({w        | ,w   | ...w     | ,w  | } →     |                                           |     |     |     |     |     |     |

|           |           |            | 1 2  | 2n−1     |     | 2n      | whichmodelspreservetaskperformance(§5.3). |     |     |     |     |     |     |
| {w 2 ,w 1 | ,...w     | 2n ,w 2n−1 | }).  |          |     |         |                                           |     |     |     |     |     |     |
|           |           |            |      |          |     |         | 5.1 Attentionmassandtaskperformance       |     |     |     |     |     |     |
| Sequence  | Copying   | The        | task | requires |     | copying |                                           |     |     |     |     |     |     |
the input sequence ({w 1 ,w 2 ...w n−1 ,w n } → For the classification tasks, we experiment with
{w ,w ...w ,w }). thelosscoefficientλ ∈ {0,0.1,1}. Ineachexper-
| 1 2       | n−1      | n      |      |      |       |         |                                              |        |      |     |        |               |        |

|           |          |        |      |      |       |         | iment,wemeasurethe(i)attentionmass:          |        |      |     |        |               | thesum |
| Sequence  | Reversal | The    | goal | here | is to | reverse |                                              |        |      |     |        |               |        |
|           |          |        |      |      |       |         | of attention                                 | values | over | the | set of | impermissible |        |
| the input | sequence | ({w    | ,w   | ...w | ,w    | } →     |                                              |        |      |     |        |               |        |
|           |          |        | 1    | 2    | n−1   | n       | tokensaveragedoveralltheexamples,and(ii)test |        |      |     |        |               |        |
| {w ,w     | ...w     | ,w }). |      |      |       |         |                                              |        |      |     |        |               |        |
n n−1 2 1 accuracy. During the course of training (i.e. after
| The motivation       |           | for evaluating |                         | on           | the synthetic |         |              |           |               |              |                   |              |        |

|                      |           |                |                         |              |               |         | each epoch), |           | we arrive     | at           | different         | models       | from   |
| tasks is             | that for  | any given      | target                  | token,       |               | we pre- |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | which        | we choose | the           | one          | whose performance |              | is     |
| cisely know          | the       | input tokens   |                         | responsible. |               | Thus,   |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | within       | 2% of     | the original  |              | accuracy          | and provides |        |
| for these            | tasks,    | the gold       | alignments              |              | act as        | imper-  |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | the greatest | reduction |               | in attention | mass              | on           | imper- |
| missible             | tokens    | in our         | setup                   | (which       | are different |         |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | missible     | tokens.   | This          | is done      | using             | the develop- |        |
| foreachoutputtoken). |           |                | Foreachofthethreetasks, |              |               |         |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | ment set,    | and       | the results   | on           | the test          | set from     | the    |
| we programmatically  |           | generate       |                         | 100K         | random        | in-     |              |           |               |              |                   |              |        |
|                      |           |                |                         |              |               |         | chosen       | model     | are presented |              | in Table          | 3.           | Across |
| put training         | sequences |                | (with                   | their        | corresponding |         |              |           |               |              |                   |              |        |
mosttasks,andmodels,wefindthatourmanipula-
targetsequences)oflengthupto32.
Theinputand
tionschemeseverelyreducestheattentionmasson
outputvocabularyisfixedtoa1000uniquetokens.
For the task of bigram flipping, the input lengths 4 Implementationdetails: theencoderanddecodertoken
|     |     |     |     |     |     |     | embedding | size | is 256, the | encoder | and decoder | hidden | di- |

3These tasks have been previously used in the literature mensionsizeis512,andtheteacherforcingratiois0.5. We
toassesstheabilityofRNNstolearnlong-rangereorderings usetop-1greedystrategytodecodetheoutputsequence.
andsubstitutions(Grefenstetteetal.,2015). 5Alldataandcodewillbereleasedonpublication.
4786

OccupationPred. GenderIdentify SST+Wiki Ref.Letters
Model λ I
Acc. A.M. Acc. A.M. Acc. A.M. Acc. A.M.
Embedding 0.0 (cid:55) 93.8 - 66.8 - 48.9 - 74.2 2.3
Embedding 0.0 (cid:51) 96.3 51.4 100 99.2 70.7 48.4 77.5 2.3
Embedding 0.1 (cid:51) 96.2 4.6 99.4 3.4 67.9 36.4 76.8 0.5
Embedding 1.0 (cid:51) 96.2 1.3 99.2 0.8 48.4 8.7 76.9 0.1
BiLSTM 0.0 (cid:55) 93.3 - 63.3 - 49.1 - 74.7 -
BiLSTM 0.0 (cid:51) 96.4 50.3 100 96.8 76.9 77.7 77.5 4.9
BiLSTM 0.1 (cid:51) 96.4 0.08 100 <10−6 60.6 0.04 76.9 3.9
BiLSTM 1.0 (cid:51) 96.7 <10−2 100 <10−6 61.0 0.07 74.2 <10−2
BERT 0.0 (cid:55) 95.0 - 72.8 - 50.4 - 68.2
BERT(mean) 0.0 (cid:51) 97.2 13.9 100 80.8 90.8 59.0 74.7 2.6
BERT(mean) 0.1 (cid:51) 97.2 0.01 99.9 <10−3 90.9 <10−2 76.2 <10−1
BERT(mean) 1.0 (cid:51) 97.2 <10−3 99.9 <10−3 90.6 <10−3 75.2 <10−2
BERT 0.0 (cid:55) 95.0 - 72.8 - 50.4 - 68.2
BERT(max) 0.0 (cid:51) 97.2 99.7 100 99.7 90.8 96.2 74.7 28.9
BERT(max) 0.1 (cid:51) 97.1 <10−3 99.9 <10−3 90.7 <10−2 76.7 0.6
BERT(max) 1.0 (cid:51) 97.4 <10−3 99.8 <10−4 90.2 <10−3 75.9 <10−2
Table3:Accuracyofvariousclassificationmodelsalongwiththeirattentionmass(A.M.)onimpermissibletokens
I, with varying values of the loss coefficient λ. The first row for each model class represents the case when
impermissibletokensI forthetaskaredeleted/anonymized. Formostmodels,andtasks,wecanseverelyreduce
attentionmassonimpermissibletokenswhilepreservingoriginalperformance(λ=0impliesnomanipulation).
BigramFlip SequenceCopy SequenceReverse En→DeMT
Attention λ
Acc. A.M. Acc. A.M. Acc. A.M. BLEU A.M.
Dot-Product 0.0 100.0 94.5 99.9 98.8 100.0 94.1 24.4 20.6
Uniform 0.0 97.8 5.2 93.8 5.2 88.1 4.7 18.5 5.9
None 0.0 96.4 0.0 84.1 0.0 84.1 0.0 14.9 0.0
Manipulated 0.1 99.9 24.4 100.0 27.3 100 27.6 23.7 7.0
Manipulated 1.0 99.8 0.03 92.9 0.02 99.8 0.01 20.6 1.1
Table4:Performanceofsequence-to-sequencemodelsandtheirattentionmass(A.M.)onimpermissibletokensI,
withvaryingvaluesofthelosscoefficientλ. Similartoclassificationtasks,wecanseverelyreduceattentionmass
onimpermissibletokenswhileretainingoriginalperformance. Allvaluesareaveragedoverfiveruns.
impermissibletokenscomparedtomodelswithout For sequence-to-sequence tasks, from Table 4,
any manipulation (i.e. when λ = 0). This reduc- weobservethatourmanipulationschemecansim-
tioncomesataminor,orno,decreaseintaskaccu- ilarly reduce attention mass over impermissible
racy. Notethatthemodelscannotachieveperfor- alignmentswhilepreservingoriginalperformance.
mance similar to the original model (as they do), To measure performance, we use token-by-token
unlesstheyrelyonthesetofimpermissibletokens. accuracy for synthetic tasks, and BLEU score for
Thiscanbeseenfromthegapbetweenmodelsthat English to German MT. We also notice that the
do not use impermissible tokens ( I (cid:55)) from ones models with manipulated attention (i.e. deliber-
thatdo(I (cid:51)). ately misaligned) outperform models with none
or uniform attention. This suggests that atten-
The only outlier to our findings is the SST+Wiki tionmechanismsaddvaluetothelearningprocess
sentimentanalysistask,whereweobservethatthe insequence-to-sequencetaskswhichgoesbeyond
manipulated Embedding and BiLSTM models re- theirusualinterpretationasalignments.
ducetheattentionmassbutalsoloseaccuracy. We
speculate that these models are under parameter-
ized and thus jointly reducing attention mass and 5.2 HumanStudy
retainingoriginalaccuracyisharder. Themoreex-
pressive BERT obtains an accuracy of over 90% To study the deceptiveness of attention maps
while reducing the maximum attention mass over trainedusingvarioustrainingschemes,wepresent
themoviereviewfrom96.2%to10−3%. a series of inputs and outputs from classification
4787

models to three human subjects.6 The models are Attention Example Q1 Q2
BiLSTMs that are trained to classify occupations Ms.Xpractices
66%
into either physician or surgeon given a short bi- Original medicine andspecializes 3.00
(yes)
inurologicalsurgery
ography. We highlight the input tokens as per
the attention scores from three different training Adversarial Ms.Xpractices
0%
(Wiegreffeand medicineandspecializes 1.00
schemes: (i) original dot-product attention, (ii) (yes)
Pinter,2019) inurologicalsurgery
adversarial attention from Wiegreffe and Pinter
Ms.Xpractices
(2019), and, (iii) our proposed attention manipu- 0%
Ours medicine andspecializes 2.67
(yes)
lation strategy. We ask human annotators (Q1): inurologicalsurgery
Do you think that this prediction was influenced
by the gender of the individual? Each participant Table 5: Results to questions posed to human partici-
answers either “yes” or “no” for a set of 50 ex- pants. Q1: Do you think that this prediction was in-
fluencedbythegenderoftheindividual? Q2: Doyou
amples from each of the three attention schemes.
believe the highlighted tokens capture the factors that
Weshuffledtheorderofsetsamongthethreepar-
drivethemodelsprediction? See§5.2fordiscussion.
ticipants to prevent any ordering bias. Addition-
ally, participants can flip through many examples
(out of 4), only slightly lower than the score for
before registering their answers. After looking
the original explanations, and significantly better
at 50 examples from a given attention scheme,
than the adversarial attention. We found that the
we inquire about trustworthiness of the attention
KL divergence term in training adversarial atten-
scores (Q2): Do you believe the highlighted to-
tion (Eq. 1) encourages all the attention mass to
kens capture the factors that drive the models’
concentrate on a single uninformative token for
prediction? They answer the question on a scale
most examples, and hence was deemed as less
of 1 to 4, where 1 denotes that the highlighted
trustworthy by the annotators (see Table 5, more
tokens do not determine the models’ prediction,
examples in appendix). By contrast, our manip-
whereas4impliestheysignificantlydeterminethe
ulation scheme only reduces attention mass over
models’ prediction. We deliberately ask partici-
problematictokens,andretainsattentionovernon-
pantsonce(towardstheend)aboutthetrustworthi-
problematic but predictive ones (e.g. “medicine”)
nessofattention-basedexplanations,incontrastto
making it more believable. We assess agreement
polling after each example, as it requires multiple
amongannotators,andcalculatetheFleiss’Kappa
examples to assess whether the explanations cap-
tobe0.97,suggestingalmostperfectagreement.
ture factors that are predictive. Participants were
kept unaware of the specifics of the classifier or
### 5.3 AlternativeWorkarounds
the explanation technique used. Detailed instruc-
We identify two mechanisms by which the mod-
tions presented to participants are available in the
elscheat,obtaininglowattentionvalueswhilere-
supplementarymaterial.
mainingaccurate.
Results Wefindthatfortheoriginaldot-product Models with recurrent encoders can simply
attention,annotatorslabeled66%ofpredictionsto pass information across tokens through recurrent
be influenced by gender. Whereas for the other connections, prior to the application of attention.
two attention schemes, none of the predictions To measure this effect, we hard-set the atten-
were marked to be influenced by gender (see Ta- tionvaluescorrespondingtoimpermissiblewords
ble 5). This is despite all three models achieving to zero after the manipulated model is trained,
roughly the same high accuracy (96%) which re- thus clipping their direct contributions for infer-
liesongenderinformation. Thisdemonstratesthe ence. ForgenderclassificationusingtheBiLSTM
efficacyofourmanipulationscheme—predictions model,wearestillabletopredictover99%ofin-
from models biased against gender minorities are stancescorrectly,thusconfirmingalargedegreeof
perceived(byhumanparticipants)asnotbeingin- information flow to neighboring representations.7
fluenced by gender. Further, our manipulated ex- In contrast, the Embedding model (which has no
planations receive a trustworthiness score of 2.67 means to pass the information pre-attention) at-
6Theparticipatingsubjectsarefirstandsecondyeargrad- 7Arecentstudy(Brunneretal.,2019)similarlyobserves
uatestudentsspecializinginNLP/MLandareknowledgeable a high degree of ‘mixing’ of information across layers in
aboutattentionmechanisms,butunawareaboutourwork. Transformermodels.
4788

(a)BigramFlipping
(b)SequenceCopying
(c)SequenceReversal
Figure 2: For three sequence-to-sequence tasks, we plot the original attention map on the left, followed by the
attentionplotsoftwomanipulatedmodels. Theonlydifferencebetweenthemanipulatedmodelsforeachtaskis
the(random)initializationseed. Differentmanipulatedmodelsresorttodifferentalternativemechanisms.
|     |     |     |     | ing to impermissible |         | words  | to compensate |                | for the |

|     |     |     |     | low attention        | values. | This   | effect        | is illustrated | in      |
|     |     |     |     | Figure 3,            | where   | the L2 | norm of       | embeddings     | for     |
impermissibletokensincreaseconsiderablyforthe
|     |     |     |     | Embedding     | model     | during      | training. | We             | do not |

|     |     |     |     | see increased | embedding |             | norms for | the BiLSTM     |        |
|     |     |     |     | model, as     | this is   | unnecessary | due       | to the model’s |        |
capabilitytomovearoundrelevantinformation.
| Figure 3: | For gender identification | task, | the norms |     |     |     |     |     |     |

Wealsonoticethatdifferentlyinitializedmod-
| of embedding | vectors corresponding | to impermissible |     |            |           |             |             |     |     |

|              |                       |                  |     | els attain | different | alternative | mechanisms. |     | In  |
tokensincreaseconsiderablyinEmbedding+Attention
Figure2,wepresentattentionmapsfromtheorig-
| model to | offset the low attention | values. This | is not |     |     |     |     |     |     |

inalmodel,alongsidetwomanipulatedmodelsini-
| the case | for BiLSTM+Attention | model as it | can pass |     |     |     |     |     |     |

informationduetorecurrentconnections. tializedwithdifferentseeds. Insomecases,theat-
tentionmapisoffbyoneortwopositionsfromthe
tains only about 50% test accuracy after zeroing goldalignments. Inothercases,alltheattentionis
the attention values for gender pronouns. We see confined to the first hidden state. In such cases,
similarevidenceofpassingaroundinformationin
|     |     |     |     | manipulated | models | are | similar to | a no-attention |     |

sequence-to-sequence models, where certain ma- model, yet they offer better performance. In pre-
nipulatedattentionmapsareoffbyoneortwopo- liminary experiments, we found a few such mod-
sitionsfromthegoldalignments(seeFigure2). elsthatoutperformtheno-attentionbaseline,even
Models restricted from passing information when the attention is turned off during inference.
prior to the attention mechanism tend to increase This suggests that attention offers benefits during
the magnitude of the representations correspond- training,evenifitisnotusedduringinference.
4789

| 6 Conclusion     |     |      |          |           |     |           | Maria De-Arteaga, |          | Alexey  | Romanov,  |     | Hanna      | Wal-    |

|                  |     |      |          |           |     |           | lach,             | Jennifer | Chayes, | Christian |     | Borgs,     | Alexan- |
| Amidst practices |     | that | perceive | attention |     | scores to |                   |          |         |           |     |            |         |
|                  |     |      |          |           |     |           | dra Chouldechova, |          | Sahin   | Geyik,    |     | Krishnaram | Ken-    |
beanindicationofwhatthemodelfocuseson,we thapadi, and Adam Tauman Kalai. 2019. Bias
|     |     |     |     |     |     |     | in bios: | A   | case study | of  | semantic |     | representa- |

characterizethemanipulabilityofattentionmech-
|           |                   |     |     |        |         |         | tion bias | in  | a high-stakes | setting. |     | arXiv | preprint |

| anism and | the (surprisingly |     |     | small) | cost to | be paid |           |     |               |          |     |       |          |
arXiv:1901.09451.
| for it in | accuracy. | Our | simple | training |     | scheme |               |     |          |        |        |     |          |

|           |           |     |        |          |     |        | Jacob Devlin, |     | Ming-Wei | Chang, | Kenton |     | Lee, and |
producesmodelswithsignificantlyreducedatten-
|                                         |      |        |       |          |       |        | KristinaToutanova.2019. |     |              | Bert:Pre-trainingofdeep |          |             |     |

| tion mass                               | over | tokens | known | a priori | to be | useful |                         |     |              |                         |          |             |     |
|                                         |      |        |       |          |       |        | bidirectional           |     | transformers | for                     | language | understand- |     |
| forprediction,whilecontinuingtousethem. |      |        |       |          |       | Fur-   |                         |     |              |                         |          |             |     |
ing. NorthAmericanChapteroftheAssociationfor
ther analysis reveals how the manipulated models ComputationalLinguistics(NAACL).
| cheat, and | raises | concerns |     | about the | potential | use |             |        |            |     |     |      |          |

|            |        |          |     |           |           |     | Chris Dyer, | Victor | Chahuneau, |     | and | Noah | A Smith. |
ofattentionasatooltoauditmodels.
|     |     |     |     |     |     |     | 2013.   | A simple, | fast, | and | effective | reparameter- |       |

|     |     |     |     |     |     |     | ization | of ibm    | model | 2.  | North     | American     | Chap- |
Acknowledgement
teroftheAssociationforComputationalLinguistics
(NAACL).
| TheauthorsthankDr. |     |     | JulianMcAuleyforprovid- |     |     |     |     |     |     |     |     |     |     |

ing, and painstakingly anonymizing the data for Desmond Elliott, Stella Frank, Khalil Sima’an, and
|                                             |           |     |      |             |        |         | Lucia             | Specia. | 2016. | Multi30k:     |     | Multilingual |          |

| reference                                   | letters.  | We  | also | acknowledge |        | Alankar |                   |         |       |               |     |              |          |
|                                             |           |     |      |             |        |         | english-german    |         | image | descriptions. |     | arXiv        | preprint |
| Jainforcarefullyreadingthemanuscriptandpro- |           |     |      |             |        |         | arXiv:1605.00459. |         |       |               |     |              |          |
| viding useful                               | feedback. |     | ZL   | thanks      | Amazon | AI,     |                   |         |       |               |     |              |          |
AndreaGalassi,MarcoLippi,andPaoloTorroni.2019.
| NVIDIA,   | Salesforce, |     | Facebook |         | AI, AbridgeAI, |     |             |         |         |          |             |           |        |

|           |             |     |          |         |                |     | Attention,  | please! | a       | critical | review      | of neural | atten- |
| UPMC, the | Center      |     | for      | Machine | Learning       | in  |             |         |         |          |             |           |        |
|           |             |     |          |         |                |     | tion models | in      | natural | language | processing. |           | arXiv  |
Health, the PwC Center, the AI Ethics and Gov- preprintarXiv:1902.02181.
| ernance Fund,     |     | and DARPA’s                |     | Learning | with | Less |              |     |                |              |      |               |        |

|                   |     |                            |     |          |      |      | Alex Graves  | and | Ju¨rgen        | Schmidhuber. |      | 2005.         | Frame- |
| LabelsInitiative, |     | fortheirsupportofACMILab’s |     |          |      |      |              |     |                |              |      |               |        |
|                   |     |                            |     |          |      |      | wise phoneme |     | classification |              | with | bidirectional | lstm   |
researchonrobustandsocietallyalignedmachine andotherneuralnetworkarchitectures. NeuralNet-
works,18(5-6):602–610.
learning.
|     |     |     |     |     |     |     | Edward    | Grefenstette, | Karl | Moritz   | Hermann, |          | Mustafa |

|     |     |     |     |     |     |     | Suleyman, | and           | Phil | Blunsom. | 2015.    | Learning | to      |
References
|     |     |     |     |     |     |     | transducewithunboundedmemory. |     |     |     |     | InAdvancesin |     |

neuralinformationprocessingsystems,pages1828–
DzmitryBahdanau,KyunghyunCho,andYoshuaBen-
1836.
| gio. 2014. | Neural   |     | machine    | translation | by    | jointly  |         |             |            |     |     |       |        |

| learning   | to align | and | translate. |             | arXiv | preprint |         |             |            |     |     |       |        |
|            |          |     |            |             |       |          | Sarthak | Jain, Ramin | Mohammadi, |     | and | Byron | C Wal- |
arXiv:1409.0473.
|                |     |         |         |      |              |     | lace.    | 2019.   | Attention | is not          | explanation. |     | North    |

|                |     |         |         |      |              |     | American | Chapter | of        | the Association |              | for | Computa- |
| Maria Barrett, |     | Joachim | Bingel, | Nora | Hollenstein, |     |          |         |           |                 |              |     |          |
tionalLinguistics(NAACL).
| Marek Rei,                        | and        | Anders | Søgaard. |               | 2018.         | Sequence |                              |                   |     |     |                |     |         |

| classificationwithhumanattention. |            |        |          |               | InProceedings |          |                              |                   |     |     |                |     |         |
|                                   |            |        |          |               |               |          | VivianLaiandChenhaoTan.2019. |                   |     |     | Onhumanpredic- |     |         |
| of the 22nd                       | Conference |        | on       | Computational |               | Natural  |                              |                   |     |     |                |     |         |
|                                   |            |        |          |               |               |          | tions                        | with explanations |     | and | predictions    | of  | machine |
LanguageLearning,pages302–312.
|     |     |     |     |     |     |     | learning | models:        | A case | study  | on         | deception | detec-   |

|     |     |     |     |     |     |     | tion.    | In Proceedings |        | of the | Conference |           | on Fair- |
Gino Brunner, Yang Liu, Damia´n Pascual, Oliver ness, Accountability, and Transparency, pages 29–
| Richter, | and Roger | Wattenhofer. |     | 2019. | On  | the va- |     |     |     |     |     |     |     |

38.ACM.
lidityofself-attentionasexplanationintransformer
| models.          | arXivpreprintarXiv:1908.04211. |        |          |         |     |           |             |                                |          |         |           |                |           |

|                  |                                |        |          |         |     |           | Jiwei Li,   | Will Monroe,                   |          | and Dan | Jurafsky. |                | 2016. Un- |
|                  |                                |        |          |         |     |           | derstanding | neural                         | networks |         | through   | representation |           |
| Wenhu Chen,      | Evgeny                         |        | Matusov, | Shahram |     | Khadivi,  |             |                                |          |         |           |                |           |
|                  |                                |        |          |         |     |           | erasure.    | arXivpreprintarXiv:1612.08220. |          |         |           |                |           |
| and Jan-Thorsten |                                | Peter. | 2016.    | Guided  |     | alignment |             |                                |          |         |           |                |           |
trainingfortopic-awareneuralmachinetranslation. Lemao Liu, Masao Utiyama, Andrew Finch, and
arXivpreprintarXiv:1607.01628. Eiichiro Sumita. 2016. Neural machine trans-
|                                            |        |      |          |     |        |          | lation            | with supervised |     | attention. |     | arXiv | preprint |

| EdwardChoi,MohammadTahaBahadori,JimengSun, |        |      |          |     |        |          | arXiv:1609.04186. |                 |     |            |     |       |          |
| Joshua                                     | Kulas, | Andy | Schuetz, | and | Walter | Stewart. |                   |                 |     |            |     |       |          |
2016. Retain: Aninterpretablepredictivemodelfor AndreMartinsandRamonAstudillo.2016. Fromsoft-
healthcare using reverse time attention mechanism. maxtosparsemax: Asparsemodelofattentionand
InAdvancesinNeuralInformationProcessingSys- multi-label classification. In International Confer-
| tems,pages3504–3512. |     |     |     |     |     |     | enceonMachineLearning,pages1614–1623. |     |     |     |     |     |     |

4790

| SofiaSerranoandNoahASmith.2019. |                                   |     |     | Isattentionin- |     |

| terpretable?                    | 57thannualmeetingoftheAssociation |     |     |                |     |
forComputationalLinguistics(ACL).
| Richard Socher, |             | Alex Perelygin, |           | Jean   | Wu, Jason |

| Chuang,         | Christopher | D               | Manning,  | Andrew | Ng, and   |
| Christopher     | Potts.      | 2013.           | Recursive | deep   | models    |
forsemanticcompositionalityoverasentimenttree-
| bank. In  | Proceedings |            | of the | 2013 conference | on          |

| empirical | methods     | in natural |        | language        | processing, |
pages1631–1642.
| Ashish Vaswani, |       | Noam Shazeer, |           | Niki Parmar,    | Jakob  |

| Uszkoreit,      | Llion | Jones,        | Aidan     | N Gomez,        | Łukasz |
| Kaiser, and     | Illia | Polosukhin.   |           | 2017. Attention | is all |
| you need.       | In    | Advances      | in neural | information     | pro-   |
cessingsystems,pages5998–6008.
| Sarah Wiegreffe |              | and Yuval   | Pinter. | 2019.  | Attention is |

| not not         | explanation. | Proceedings |         | of the | 2019 con-    |
ferenceonEmpiricalMethodsinNaturalLanguage
Processing,EMNLP.
QizheXie,XuezheMa,ZihangDai,andEduardHovy.
| 2017. An      | interpretable |                  | knowledge | transfer | model    |

| for knowledge |               | base completion. |           | arXiv    | preprint |
arXiv:1704.05908.
| Kelvin Xu,                  | Jimmy | Ba, Ryan | Kiros,         | Kyunghyun      | Cho,    |

| Aaron Courville,            |       | Ruslan   | Salakhutdinov, |                | Richard |
| Zemel,andYoshuaBengio.2015. |       |          |                | Show,attendand |         |
tell: Neuralimagecaptiongenerationwithvisualat-
| tention. | arXivpreprintarXiv:1502.03044. |     |     |     |     |

4791

SupplementaryMaterial
A Instructionsforhumanstudy
| In a series   | of         | examples,  |             | we present | the    | inputs  |     |     |     |

| and outputs   | of         | a machine  |             | learning   | (ML)   | model   |     |     |     |
| trained       | to predict | occupation |             | (physician |        | or sur- |     |     |     |
| geon) given   | a          | short      | bio (text). | In         | each   | bio, we |     |     |     |
| attempt       | to explain | the        | predictions |            | of the | model.  |     |     |     |
| Specifically, | we         | employ     | a           | technique  | that   | high-   |     |     |     |
lightswordsthat(perourexplanationmethod)are
| thought                                   | to be | responsible | for | a particular |     | predic- |     |     |     |

| tion(colloquially,whatthemodelfocuseson). |       |             |     |              |     | For     |     |     |     |
eachuniqueexamplebelow,answerthefollowing
| question: | Doyouthinkthatthispredictionwasin- |     |     |     |     |     |     |     |     |

fluencedbythegenderoftheindividual?
| • Yes, | I suspect | that | the | gender | influenced | the |     |     |     |

prediction.
| • No, | I have | no reason |     | to suspect | that | gender |     |     |     |

influencedtheprediction.
Dataset
|     |     |     |     |     |     |     |     | Train Val | Test |

(Task)
| Please | note | that, all | the | examples | in  | this file |     |     |     |

CommonCrawlBiographies
are input, output pairs from one specific model. 17629 2519 5037
(PhysicianvsSurgeon)
| Further, | darker | shades | of highlighting |     | indicate | a   |     |     |     |

WikipediaBiographies
| higheremphasisforthetoken(asperourexplana- |     |     |     |     |     |     |     | 9017 1127 | 1127 |

(GenderIdentification)
tionmethod).
SST+Wikipedia
|         |         |             |          |          |         |         |                     | 6920 872 | 1821 |

| After   | showing | 50          | examples | from     | a given | at-     | (SentimentAnalysis) |          |      |
| tention | scheme, | we inquire: |          | Overall, | do      | you be- |                     |          |      |
ReferenceLetters
|     |     |     |     |     |     |     |     | 32800 4097 | 4094 |

lievethehighlightedtokenscapturethefactorsthat (AcceptancePrediction)
drivethemodelsprediction?
Table6:Numberoftraining,validation,andtestexam-
1. The highlighted tokens capture factors that plesinvariousdatasetsusedforclassificationtasks.
donotdeterminethemodelsprediction.
| 2. The | highlighted |     | tokens | capture | factors | that |     |     |     |

marginallydeterminethemodelsprediction.
| 3. The     | highlighted |           | tokens | capture | factors | that    |     |     |     |

| moderately |             | determine |        | the     | models  | predic- |     |     |     |
tions.
| 4. The        | highlighted |           | tokens | capture | factors | that    |     |     |     |

| significantly |             | determine |        | the     | models  | predic- |     |     |     |
tions.
B DatasetDetails
| Details | about | the datasets |     | used for | classification |     |     |     |     |

tasksareavailableinTable6.
C QualitativeExamples
| A few | qualitative | examples |     | illustrating | three | dif- |     |     |     |

ferentattentionschemesarelistedinTable7.
4792

| Attention |     | InputExample |     |     | Prediction |

Original Ms.Xpracticesmedicine andspecializesinurologicalsurgery Physician

(Wiegreffeand Ms.Xpracticesmedicineandspecializesinurologicalsurgery Physician

Ours Ms.Xpracticesmedicine andspecializes inurologicalsurgery Physician
XpracticesmedicineinFortMyers,FLandspecializesinfamilymedicine
| Original | Ms. |     |     |     | Physician |

(Wiegreffeand Ms.XpracticesmedicineinFortMyers,FLandspecializesinfamilymedicine Physician

Ours Ms.Xpracticesmedicine inFortMyers,FLandspecializes infamily medicine Physician
|          | Havingstartedhissurgical | careerasageneralorthopaedic      |     | surgeon, |         |

|          | MrXretainsabroadpractice | whichincludeskneeandhandsurgery. |     |          |         |
| Original |                          |                                  |     |          | Surgeon |
Hestilldoesregulartraumaon-callfortheNorthHampshirehospital
andtreatsalltypesoforthopaedic problemsandtrauma.
Havingstartedhissurgicalcareerasageneralorthopaedicsurgeon,

MrXretainsabroadpracticewhichincludeskneeandhandsurgery.
| (Wiegreffeand |     |     |     |     | Surgeon |

Hestilldoesregulartraumaon-callfortheNorthHampshirehospital

andtreatsalltypesoforthopaedicproblemsandtrauma.
|     | Havingstartedhissurgical | careerasageneralorthopaedic |     | surgeon, |     |

MrXretainsabroadpracticewhichincludeskneeandhandsurgery.
| Ours |     |     |     |     | Surgeon |

Hestilldoesregulartraumaon-callfortheNorthHampshirehospital
andtreatsalltypesoforthopaedic problemsandtrauma.
|     | Ms. Xpracticesmedicine | in...andspecializesinpediatrics.Ms. |     | Xisaffiliated |     |

withchildrensofAlabama,SaintVincentshospitalBirminghamand
| Original |                            |     |                          |     | Physician |

|          | BrookwoodMedicalCenter.Ms. |     | XspeaksEnglishandArabic. |     |           |
Ms.Xpracticesmedicinein...andspecializesinpediatrics.Ms.Xisaffiliated

(Wiegreffeand withchildrensofAlabama,SaintVincentshospitalBirminghamand Physician
BrookwoodMedicalCenter.Ms.XspeaksEnglishandArabic.

|     | Ms.Xpracticesmedicine | in...andspecializes | inpediatrics.Ms.Xisaffiliated |     |     |

Ours withchildrensofAlabama,SaintVincentshospitalBirminghamand Physician
|     | BrookwoodMedicalCenter.Ms.Xspeaks |     | English | andArabic. |     |

Table7: Qualitativeexamples.
4793

---
**Source PDF:** `2021_06_article.pdf`
