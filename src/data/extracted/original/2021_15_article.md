Improving Multi-hop Question Answering over Knowledge Graphs using
|     |     |               |     | Knowledge |                 | Base Embeddings |                |     |     |     |     |

|     |     | ApoorvSaxena∗ |     |           | AditayTripathi∗ |                 | ParthaTalukdar |     |     |     |     |
IndianInstituteofScience,Bangalore
{apoorvsaxena,aditayt,ppt}@iisc.ac.in
Abstract
| Knowledge |     | Graphs | (KG) | are multi-relational |     |     |     |     |     |     |     |

graphsconsistingofentitiesasnodesandrela-
| tionsamongthemastypededges.   |           |           |          | Goalofthe     |           |           |            |      |           |         |        |

| Question                      | Answering |           | over     | KG (KGQA)     | task      |           |            |      |           |         |        |
| is to                         | answer    | natural   | language | queries       | posed     |           |            |      |           |         |        |
| over                          | the KG.   | Multi-hop |          | KGQA requires | rea-      |           |            |      |           |         |        |
| soning                        | over      | multiple  | edges    | of the        | KG to     | ar-       |            |      |           |         |        |
| rive                          | at the    | right     | answer.  | KGs are       | often     | in-       |            |      |           |         |        |
| completewithmanymissinglinks, |           |           |          |               | posingad- |           |            |      |           |         |        |
|                               |           |           |          |               |           | Figure 1: | Challenges | with | Multi-hop | QA over | Knowl- |
ditional challenges for KGQA, especially for edge Graphs (KGQA) in sparse and incomplete KGs:
multi-hop KGQA. Recent research on multi- Absenceoftheedgehas genre(GangsterNo.1,Crime)
| hop | KGQA | has attempted |     | to handle | KG spar- |     |     |     |     |     |     |

intheincompleteKGmakesitmuchhardertoanswer
sityusingrelevantexternaltext,whichisn’tal- theinputNLquestion,astheKGQAmodelpotentially
| ways | readily | available. |     | In a separate | line | of  |     |     |     |     |     |

needstoreasonoveralongerpathovertheKG(marked
research, KG embedding methods have been by bold edges). Existing multi-hop KGQA methods
proposed to reduce KG sparsity by perform- also impose heuristic neighborhood limits (shaded re-
| ing | missing | link | prediction. | Such | KG em- |     |     |     |     |     |     |

gioninthefigure),whichoftenmakesthetrueanswer
beddingmethods,eventhoughhighlyrelevant, (Crime in this example) out of reach. EmbedKGQA,
have not been explored for multi-hop KGQA our proposed method, overcomes these limitations by
so far. We fill this gap in this paper and pro- utilizingembeddingsoftheinputKGduringmulti-hop
pose EmbedKGQA. EmbedKGQA is particu- KGQA.Formoredetails,pleasereferFigure2andSec-
larlyeffectiveinperformingmulti-hopKGQA
tion4.
| over | sparse | KGs. | EmbedKGQA | also | relaxes |     |     |     |     |     |     |

therequirementofanswerselectionfromapre-
| specified | neighborhood, |     |     | a sub-optimal | con- |              |                                |     |     |     |     |

|           |               |     |     |               |      | etal.,2018). | QuestionAnsweringoverKnowledge |     |     |     |     |
straintenforcedbypreviousmulti-hopKGQA
Graphs(KGQA)hasemergedasanimportantre-
| methods.    |           | Through       | extensive | experiments    | on     |                       |      |          |                     |        |         |

|             |           |               |           |                |        | search area           | over | the last | few years           | (Zhang | et al., |
| multiple    | benchmark |               | datasets, | we demonstrate |        |                       |      |          |                     |        |         |
|             |           |               |           |                |        | 2018;Sunetal.,2019a). |      |          | InKGQAsystems,given |        |         |
| EmbedKGQA’s |           | effectiveness |           | over other     | state- |                       |      |          |                     |        |         |
of-the-artbaselines. a natural language (NL) question and a KG, the
|                |     |     |     |     |     | right answer                 | is  | derived | based | on analysis | of the |

| 1 Introduction |     |     |     |     |     | questioninthecontextoftheKG. |     |         |       |             |        |
Inmulti-hopKGQA,thesystemneedstoperform
| Knowledge | Graphs |     | (KG) | are multi-relational |     |     |     |     |     |     |     |

reasoningovermultipleedgesoftheKGtoinferthe
graphsconsistingofmillionsofentities(e.g.,San
|                   |     |       |     |               |       | rightanswer. | KGsareoftenincomplete,whichcre- |     |     |     |     |

| Jose, California, |     | etc.) | and | relationships | among |              |                                 |     |     |     |     |
them (e.g., San Jose-cityInState-California). Ex- atesadditionalchallengesforKGQAsystems,espe-
ciallyincaseofmulti-hopKGQA.Recentmethods
| amples | of a | few large |     | KGs include | Wikidata |           |             |      |        |           |     |

|        |      |           |     |             |          | have used | an external | text | corpus | to handle | KG  |
(Google,2013),DBPedia(Lehmannetal.,2015),
Yago(Suchaneketal.,2007),andNELL(Mitchell sparsity(Sunetal.,2019a,2018). Forexample,the
methodproposedin(Sunetal.,2019a)constructs
∗Equalcontribution
aquestion-specificsub-graphfromtheKG,which
| EmbedKGQA’s |     | source |     | code is | available | at  |     |     |     |     |     |

https://github.com/malllabiisc/EmbedKGQA isthenaugmentedwithsupportingtextdocuments.
4498
Proceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,pages4498–4507
July5-10,2020.(cid:13)c2020AssociationforComputationalLinguistics

Figure2: OverviewofEmbedKGQA,ourproposedmethodforMulti-hopQAoverKnowledgeGraphs(KGQA).
EmbedKGQA has three modules: (1) KG Embedding Module (Section 4.2) learns embeddings for all entities in
theinputKG,(2)QuestionEmbeddingModule(Section4.3)learnsanembeddingforthequestion,and(3)theAn-
swerSelectionModule(Section4.4)selectsthefinalanswerbyincorporatingthequestionandrelationsimilarity
scores. EmbedKGQA’suseofembeddingsmakesitmoreeffectiveinhandlingKGsparsity. Moreover,sinceEm-
bedKGQAconsidersallentitiesascandidateanswers,itdoesn’tsufferfromthelimitedneighborhoodout-of-reach
issuesofexistingMulti-hopKGQAmethods. PleasereferSection4fordetaileddescriptionofEmbedKGQA.
Graph CNN (Kipf and Welling, 2016) is then ap- 2016;Yangetal.,2014a;Nickeletal.,2011). KG
plied over this augmented sub-graph to arrive at embedding methods learn high-dimensional em-
the final answer. Unfortunately, availability and beddingsforentitiesandrelationsintheKG,which
identificationofrelevanttextcorporaisachallenge arethenusedforlinkprediction. Inspiteofitshigh
onitsownwhichlimitsbroad-coverageapplicabil- relevance,KGembeddingmethodshavenotbeen
ityofsuchmethods. Moreover,suchmethodsalso usedformulti-hopKGQA–wefillthisgapinthis
imposepre-specifiedheuristicneighborhoodsize paper. Inparticular,weproposeEmbedKGQA,a
limitationfromwhichthetrueanswerneedstobe novelsystemwhichleveragesKGembeddingsto
selected. Thisoftenmakesthetrueansweroutof performmulti-hopKGQA.Wemakethefollowing
| reachofthemodeltoselectfrom. |     |     |     | contributionsinthispaper: |     |     |     |     |

Inordertoillustratethesepoints,pleaseconsider
|             |          |           |                  |     | 1. We propose | EmbedKGQA, |      | a novel method    |

| the example | shown in | Figure 1. | In this example, |     |               |            |      |                   |
|             |          |           |                  |     | for the       | multi-hop  | KGQA | task. To the best |
LouisMellisistheheadentityintheinputNLques-
|                |              |                   |           |     | of our | knowledge, | EmbedKGQA     | is the first   |

| tion, and      | Crime is the | true answer       | we expect | the |        |            |               |                |
|                |              |                   |           |     | method | to use     | KG embeddings | for this task. |
| modeltoselect. | Iftheedgehas | genre(GangsterNo. |           |     |        |            |               |                |
EmbedKGQAisparticularlyeffectiveinper-
1,Crime)werepresentintheKG,thenthequestion
formingmulti-hopKGQAoversparseKGs.
| couldhavebeenansweredrathereasily. |     |     | However, |     |     |     |     |     |

sincethisedgeismissingfromtheKG,asisoften 2. EmbedKGQArelaxestherequirementofan-
thecasewithsimilarincompleteandsparseKGs, swer selection from a pre-specified local
theKGQAmodelhastopotentiallyreasonovera neighborhood, an undesirable constraint im-
longerpathovertheKG(markedbyboldededges posedbypreviousmethodsforthistask.
| in the graph). | Moreover, | the | KGQA model | im- |            |           |             |             |

|                |           |     |            |     | 3. Through | extensive | experiments | on multiple |
posedaneighborhoodsizeof3-hops,whichmade
real-worlddatasets,wedemonstrateEmbed-
thetrueanswerCrimeoutofreach.
|               |         |           |                |     | KGQA’s | effectiveness | over | state-of-the-art |

| In a separate | line of | research, | there has been | a   |        |               |      |                  |
baselines.
largebodyofworkthatutilizesKGembeddingsto
predictmissinglinksintheKG,therebyreducing WehavemadeEmbedKGQA’ssourcecodeavail-
KGsparsity(Bordesetal.,2013;Trouillonetal., abletoencouragereproducibility.
4499

| 2 RelatedWork |     |     |     |     |     | (KazemiandPoole,2018)andTuckER(Balazˇevic´ |     |     |     |     |

etal.,2019)arebasedonCanonicalPolyadic(CP)
KGQA: In prior work (Li et al., 2018) TransE, decomposition (Hitchcock, 1927) and Tucker de-
(Bordesetal.,2013)embeddingshavebeenusedto
composition(Tucker,1966)respectively.
| answerfactoidbasedquestions. |     |     | However,thisre- |     |     |     |     |     |     |     |

TransE(Bordesetal.,2013)embedsentitiesin
quiresgroundtruthrelationlabelingforeachques-
highdimensionalrealspaceandrelationastransla-
| tion and   | it does not                        | work | for multi-hop |     | question |                                       |     |     |     |        |

|            |                                    |      |               |     |          | tionbetweentheheadandthetailentities. |     |     |     | RotatE |
| answering. | Inanotherlineofwork(Yihetal.,2015) |      |               |     |          |                                       |     |     |     |        |
(Sunetal.,2019b)ontheotherhandprojectsenti-
and(Baoetal.,2016)proposedextractingapartic-
tiesincomplexspaceandrelationsarerepresented
| ularsub-graphtoanswerthequestion. |     |     |     | Themethod |     |     |     |     |     |     |

asrotationsinthecomplexplane.
presentedin(Bordesetal.,2014a),thesub-graph
ConvE(Dettmersetal.,2018)utilizesConvolu-
| generated | for a head | entity | is projected |     | in a high |     |     |     |     |     |

tionalNeuralNetworkstolearnascoringfunction
| dimensionalspaceforquestionanswering. |      |           |      |          | Mem- |           |            |         |                |               |

|                                       |      |           |      |          |      | between   | the head   | entity, | tail entity    | and relation. |
| ory Networks                          | have | also been | used | to learn | high |           |            |         |                |               |
|                                       |      |           |      |          |      | InteractE | (Vashishth | et al., | 2019) improves | upon          |
dimensionalembeddingsofthefactspresentinthe
ConvEbyincreasingfeatureinteraction.
| KGtoperformQA(Bordesetal.,2015).             |              |     |         |               | Methods |              |     |     |     |     |

| like(Bordesetal.,2014b)learnasimilarityfunc- |              |     |         |               |         | 3 Background |     |     |     |     |
| tion between                                 | the question |     | and the | corresponding |         |              |     |     |     |     |
tripleduringtraining,andscorethequestionwith In this section, we formally define a Knowledge
Graph(KG)andthendescribelinkpredictiontask
| allthecandidatetriplesatthetesttime. |     |     |     | (Yangetal., |     |     |     |     |     |     |

2014b)and(Yangetal.,2015)utilizeembedding onincompleteKGs. WethendescribeKGembed-
basedmethodstomapnaturallanguagequestions dingsandexplaintheComplExembeddingmodel.
| to logical | forms. Methods |     | like (Dai | et  | al., 2016; |     |     |     |     |     |

### 3.1 KnowledgeGraph
| Dong et | al., 2015; Hao | et  | al., 2017; | Lukovnikov |     |     |     |     |     |     |

etal.,2017;Yinetal.,2016)utilizeneuralnetworks GivenasetofentitiesE andrelationsR,aKnowl-
tolearnascoringfunctionstorankthecandidatean- edge Graph G is a set of triples K such that K ⊆
|     |     |     |     |     |     | E × R × | E   |     |     | (h,r,t), |

swers. Someworkslike(Mohammedetal.,2017; . A triple is represented as
TureandJojic,2016)considereachrelationasala- withh,t ∈ E denotingsubjectandobjectentities
belandmodelQAtaskasaclassificationproblem. respectivelyandr ∈ Rtherelationbetweenthem.
Extendingthesekindsofapproachesformulti-hop
| questionansweringisnon-trivial. |     |     |     |     |     | 3.2 LinkPrediction |     |     |     |     |

Recently, there has been some work in which Inlinkprediction,givenanincompleteKnowledge
textcorpusisincorporatedasaknowledgesource Graph,thetaskistopredictwhichunknownlinks
inadditiontoKGtoanswercomplexquestionson are valid. KG Embedding models achieve this
KGs (Sun et al., 2018, 2019a). Such approaches scoring function φ
|     |     |     |     |     |     | through a |     |     | that assigns | a score |

areusefulincasetheKGisincomplete. However, s = φ(h,r,t) ∈ R, which indicates whether a
this leads to another level of complexity in the tripleis true, withthe goalof beingable to score
QAsystem,andtextcorporamightnotalwaysbe allmissingtriplescorrectly.
available.
### 3.3 KnowledgeGraphEmbeddings
| KG completion | methods: |     | Link | prediction | in  |     |     |     |     |     |

KnowledgeGraphsusingKGembeddingshasbe- For each e ∈ E and r ∈ R, Knowledge Graph
Rde
come a popular area of research in recent years. Embedding (KGE) models generate e ∈
e
Thegeneralframeworkistodefineascorefunction and e ∈ Rdr, where e and e are d and d
|     |     |     |     |     |     | r   |     | e   | r   | e r |

forasetoftriples(h,r,t)inaKGandconstraining dimensional vectors respectively. Each of the
theminsuchawaythatthescoreforacorrecttriple embedding methods also has a scoring function
ishigherthanthescoreforanincorrecttriple. Rtoassignsomescoreφ(h,r,t)
|     |     |     |     |     |     | φ : E×R×E | →   |     |     |     |

RESCAL (Nickel et al., 2011) and DistMult to a possible triple (h,r,t), h,t ∈ E and r ∈ R.
(Yangetal.,2015)learnascorefunctioncontain- Models are trained in a way such that for every
ing a bi-linear product between head entity and correct triple (h,r,t) ∈ K and incorrect triple
tailentityvectorsandarelationmatrix. ComplEx (h(cid:48),r(cid:48),t(cid:48)) (cid:54)∈ K the model assign scores such that
(Trouillon et al., 2016) represents entity vectors φ(h,r,t) > 0 and φ(h(cid:48),r(cid:48),t(cid:48)) < 0. A scoring
andrelationmatricesinthecomplexspace. SimplE functionisgenerallyafunctionof(e ,e ,e ).
|     |     |     |     |     |     |     |     |     |     | h r t |

4500

| 3.3.1 ComplExEmbeddings |     |     |     |     |     | 4.2 KGEmbeddingModule |     |     |     |     |     |     |

ComplEx(Trouillonetal.,2016)isatensorfactor-
|     |     |     |     |     |     | ComplExembeddingsaretrainedforallh,t |     |     |     |     |     | ∈ E |

izationapproachthatembedsrelationsandentities
|     |     |     |     |     |     | and all | r ∈ | R in the | KG such | that | e h ,e | r ,e t ∈ |

in complex space. Given h,t ∈ E and r ∈ R, Cd. The entity embeddings are used for learning
| ComplEx | generates | e   | ,e ,e ∈ | Cd and | defines a |          |         |          |         |     |      |         |

|         |           | h   | r t     |        |           | a triple | scoring | function | between | the | head | entity, |
scoringfunction:
|     |     |     |     |     |     | question,andanswerentity. |     |     | Basedonthecoverage |     |     |     |

oftheKGentitiesintheQAtrainingset,theentity
φ(h,r,t) = Re((cid:104)e ,e ,e¯(cid:105)) embeddingslearnedhereareeitherkeptfrozenor
|     |     |     | h r | t   |     |                                            |     |     |     |     |     |     |

|     |     |     | d   |     |     | allowedtobefine-tunedinthesubsequentsteps. |     |     |     |     |     |     |
(1)
|     |     |       | (cid:88) (k) | e(k)e¯(k)) |     |                             |     |     |     |     |     |     |

|     |     | = Re( | e            |            |     |                             |     |     |     |     |     |     |
|     |     |       | h            | r t        |     |                             |     |     |     |     |     |     |
|     |     |       |              |            |     | 4.3 QuestionEmbeddingModule |     |     |     |     |     |     |
k=1
such that φ(h,r,t) > 0 for all true triples, and This module embeds the natural language ques-
| φ(h,r,t) | < 0forfalsetriples. |     | Redenotesthereal |     |     |        |            |           |        |     | Cd.   |      |

|          |                     |     |                  |     |     | tion q | to a fixed | dimension | vector |     | e q ∈ | This |
partofacomplexnumber. is done using a feed-forward neural network that
|     |     |     |     |     |     | first embeds |     | the question | q using | RoBERTa |     | (Liu |

## 4 EmbedKGQA:ProposedMethod
|     |     |     |     |     |     | etal.,2019)intoa768-dimensionalvector. |     |     |     |     |     | Thisis |

In this section, we first define the problem of thenpassedthrough4fullyconnectedlinearlayers
KGQAandthendescribeourmodel. withReLUactivationandfinallyprojectedontothe
complexspaceCd.
### 4.1 ProblemStatement
|     |     |     |     |     |     | Given | a question | q,  | topic | entity | h ∈ E | and set |

LetE andRbethesetofallentitiesandrelations
|     |     |     |     |     |     | of answer | entities | A   | ⊆ E, it | learns | the | question |

respectively in a KG G, and K ⊆ E ×R×E is embeddinginawaysuchthat
| the set of | all available |     | KG facts. | The problem | in  |     |     |     |     |     |     |     |

KGQAinvolves,givenanaturallanguagequestion
|                    |     |     |                         |     |     |     | φ(e | ,e ,e | ) > 0 | ∀a ∈ | A   |     |

|                    |     |     |                         |     |     |     |     | h q a |       |      |     |     |
| q andatopicentitye |     | ∈   | E presentinthequestion, |     |     |     |     |       |       |      |     |     |
h
| thetaskistoextractanentitye |     |     |     | ∈ E thatcorrectly |     |     |     |        |       |        |     |     |

|                             |     |     | t   |                   |     |     | φ(e | ,e ,e  | ) < 0 | ∀a¯ ∈/ | A   |     |
| answersthequestionq.        |     |     |     |                   |     |     |     | h q a¯ |       |        |     |     |
whereφistheComplExscoringfunction(1)and
#### 4.1.1 EmbedKGQAOverview
|     |     |     |     |     |     | e ,e | areentityembeddingslearntintheprevious |     |     |     |     |     |

a a¯
| We work | in a | setting | where | there is | no fine- |     |     |     |     |     |     |     |

step.
| grained         | annotation | present | in        | the dataset,    | such |     |                |     |           |      |               |     |

|                 |            |         |           |                 |      | For | each question, |     | the score | φ(.) | is calculated |     |
| as the question |            | type or | the exact | logic reasoning |      |     |                |     |           |      |               |     |
withallthecandidateanswerentitiesa(cid:48)
|            |          |          |     |               |     |       |            |               |     |     | ∈      | E. The |

| steps. For | example, | co-actor | is  | a combination | of  |       |            |               |     |     |        |        |
|            |          |          |     |               |     | model | is learned | by minimizing |     | the | binary | cross- |
actor−1andstarred
| starred |     |     |     | actorrelations,but |     |     |     |     |     |     |     |     |

entropylossbetweenthesigmoidofthescoresand
ourmodeldoesnotrequirethisannotation.
thetargetlabels,wherethetargetlabelis1forthe
| EmbedKGQA |     | uses | Knowledge | Graph | embed- |                              |     |     |     |                |     |     |

|           |     |      |           |       |        | correctanswersand0otherwise. |     |     |     | Labelsmoothing |     |     |
dingstoanswermulti-hopnaturallanguageques-
isdonewhenthetotalnumberofentitiesislarge.
| tions. First              | it learns | a      | representation    | of               | the KG |                           |     |     |     |     |     |     |

| in an embedding           |           | space. | Then              | given a question | it     |                           |     |     |     |     |     |     |
|                           |           |        |                   |                  |        | 4.4 AnswerSelectionModule |     |     |     |     |     |     |
| learnsaquestionembedding. |           |        | Finallyitcombines |                  |        |                           |     |     |     |     |     |     |
Atinference,themodelscoresthe(head,question)
theseembeddingtopredicttheanswer.
Inthefollowingsections,weintroducetheEm- pairagainstallpossibleanswersa(cid:48) ∈ E. Forrela-
bedKGQAmodel. Itconsistsof3modules: tivelysmallerKGslikeMetaQA,wesimplyselect
theentitywiththehighestscore.
1. KGEmbeddingModulecreatesembeddings
forallentitiesintheKG.
|     |     |     |     |     |     |     | e   | = argmaxφ(e |     | ,e  | ,e )      |     |

|     |     |     |     |     |     |     | ans |             |     | h q | a(cid:48) |     |
a(cid:48)∈E
2. QuestionEmbeddingModulefindstheem-
beddingofaquestion
Howeveriftheknowledgegraphislarge,prun-
3. AnswerSelectionModulereducesthesetof ingthecandidateentitiescansignificantlyimprove
candidateanswerentitiesandselectsthefinal the performance of EmbedKGQA. The pruning
| answer |     |     |     |     |     | strategyisdescribedinthefollowingsection. |     |     |     |     |     |     |

4501

|     |     |     | Train | Dev |     | Test | more | than | 400k questions |     | in  | the movie | do- |

MetaQA1-hop 96,106 9,992 9.947 main. It has 1-hop, 2-hop, and 3-hop ques-
|             |     |     |         |        |     |        | tions.                          | In  | our experiments, |     |     | we        | used the |

| MetaQA2-hop |     |     | 118,948 | 14,872 |     | 14,872 |                                 |     |                  |     |     |           |          |
|             |     |     |         |        |     |        | “vanilla”versionofthequestions. |     |                  |     |     | Alongwith |          |
| MetaQA3-hop |     |     | 114,196 | 14,274 |     | 14,274 |                                 |     |                  |     |     |           |          |
theQAdata,MetaQAalsoprovidesaKGwith
| WebQSP |     |     | 2,998 | 100 |     | 1,639 |     |     |     |     |     |     |     |

135ktriples,43kentities,andninerelations.
| Table 1: | Statistics | for | MetaQA | and | WebQuestionsSP |     |                   |     |     |      |        |            |      |

|          |            |     |        |     |                |     | 2. WebQuestionsSP |     |     | (tau | Yih et | al., 2016) | is a |
datasets. Pleaserefersection5.1formoredetails.
|     |     |     |     |     |     |     | smallerQAdatasetwith4,737questions. |     |     |     |     |     | The |

questionsinthisdatasetare1-hopand2-hop
|     |     |     |     |     |     |     | questions |     | and are | answerable |     | through | Free- |

#### 4.4.1 Relationmatching
baseKG.Foreaseofexperimentation,were-
| Similar | to PullNet |     | (Sun | et al., | 2019a) | we learn |     |     |     |     |     |     |     |

stricttheKBtobeasubsetofFreebasewhich
| a scoring | function |     | S(r,q)  | which    | ranks | each re- |          |     |       |          |        |        |     |

|           |          |     |         |          |       |          | contains | all | facts | that are | within | 2-hops | of  |
| r         | ∈        | R   |         |          |       | q.       |          |     |       |          |        |        |     |
| lation    |          | for | a given | question |       | Let      |          |     |       |          |        |        |     |
anyentitymentionedinthequestionsofWe-
| h be the | embedding |     | of  | a relation | r and | q(cid:48) = |     |     |     |     |     |     |     |

r
bQuestionsSP.Wefurtherpruneittocontain
| (< s >,w         | ,..,w | ,<  | /s >)                   | be  | the sequence | of  |                                         |                                 |     |     |     |     |     |

|                  | 1     | |q| |                         |     |              |     | onlythoserelationsthatarementionedinthe |                                 |     |     |     |     |     |
| wordsinquestionq |       |     | whichareinputtoRoBERTa. |     |              |     |                                         |                                 |     |     |     |     |     |
|                  |       |     |                         |     |              |     | dataset.                                | ThissmallerKBhas1.8millionenti- |     |     |     |     |     |
Thescoringfunctionisdefinedasthesigmoidof
tiesand5.7milliontriples.
| the dot             | product | of  | the final | output             | of the | last hid- |     |     |     |     |     |     |     |

| denlayerofRoBERTa(h |         |     |           | )andtheembeddingof |        |           |     |     |     |     |     |     |     |
q
| relationr | (h  | ).  |     |     |     |     | 5.2 Baselines |     |     |     |     |     |     |

r
WecompareourmodelwiththeKey-ValueMem-
RoBERTa(q(cid:48))
|     |     | h q = |     |     |     |     | oryNetwork(Milleretal.,2016),theGraftNet(Sun |     |     |     |     |     |     |

S(r,q) = sigmoid(hTh ) etal.,2018)andthePullnet(Sunetal.,2019a)for
q r
|     |     |     |     |     |     |     | WebQuestionsSPdataset. |     |     | ForMetaQAdatasetwe |     |     |     |

Amongalltherelations,weselectthoserelations
|     |     |     |     |     |     |     | also compare | with | the | VRN | (Zhang | et al., | 2018). |

which have score greater than 0.5 It is denoted Thesemethodsimplementmulti-hopKGQA,and
a(cid:48)
as the set R . For each candidate entity that exceptVRN,useadditionaltextcorpustomitigate
a
wehaveobtainedsofar(Section4.4),wefindthe
theKGsparsityproblem.
relationsintheshortestpathbetweenheadentity
|                |                          |     |     |     |     |        | • VRN | (Zhang | et al., | 2018) | uses | variational |     |

| handa(cid:48). | LetthissetofrelationsbeR |     |     |     | .   | Nowthe |       |        |         |       |      |             |     |
a(cid:48)
learningalgorithmtoperformMulti-HopQA
relationscoreforeachcandidateanswerentityis
| definedasthesizeoftheirintersection. |          |     |           |       |           |     | overKG.     |          |            |         |         |            |      |

|                                      |          |     |           |       |           |     | • Key-Value |          | Memory     | Network |         | (KVMem)    |      |
|                                      | RelScore |     | =         | |R ∩R | |         |     |             |          |            |         |         |            |      |
|                                      |          |     | a(cid:48) | a     | a(cid:48) |     |             |          |            |         |         |            |      |
|                                      |          |     |           |       |           |     | (Miller     | et       | al., 2016) | is      | one of  | the first  | mod- |
|                                      |          |     |           |       |           |     | els that    | attempts |            | to do   | QA over | incomplete |      |
Weusealinearcombinationoftherelationscore
|     |     |     |     |     |     |     | KBsbyaugmentingitwithtext. |     |     |     |     | Itmaintains |     |

andComplExscoretofindtheanswerentity.
amemorytablewhichstoresKBfactsandtext
e = argmaxφ(e ,e ,e )+γ ∗RelScore encodedintokey-valuepairsandusesthisfor
| ans |     |     | h q | a(cid:48) |     | a(cid:48) |     |     |     |     |     |     |     |

retrieval.
a(cid:48)∈N h
whereγ isatunablehyperparameter. • GraftNet(Sunetal.,2018)usesheuristicsto
createaquestion-specificsubgraphcontaining
## 5 ExperimentalDetails KGfacts,entitiesandsentencesfromthetext
corporaandthenusesavariantofgraphCNN
| In this section, |     | we  | first describe |     | the datasets | that |     |     |     |     |     |     |     |

(KipfandWelling,2016)toperformreasoning
weevaluatedourmethodon,andthenexplainthe
overit.
experimentalsetupandtheresults.
|              |     |     |     |     |     |     | • PullNet                                 | (Sun | et  | al., 2019a) |     | also | creates a |

| 5.1 Datasets |     |     |     |     |     |     | question-specificsub-graphbutinsteadofus- |      |     |             |     |      |           |
1. MetaQA (Zhang et al., 2018) dataset is a ingheuristics,itlearnsto“pull”factsandsen-
large scale multi-hop KGQA dataset with tencesfromthedatatocreateamorerelevant
4502

Model MetaQAKG-Full MetaQAKG-50
1-hop 2-hop 3-hop 1-hop 2-hop 3-hop
VRN 97.5 89.9 62.5 - - -
GraftNet 97.0 94.8 77.7 64.0(91.5) 52.6(69.5) 59.2(66.4)
PullNet 97.0 99.9 91.4 65.1(92.4) 52.1(90.4) 59.7(85.2)
KV-Mem 96.2 82.7 48.9 63.6(75.7) 41.8(48.4) 37.6(35.2)
EmbedKGQA(Ours) 97.5 98.8 94.8 83.9 91.8 70.3
Table2: ResultsonMetaQAdataset. AllbaselineresultsweretakenfromSunetal.(2019a). Wehaveconsidered
bothfullKG(MetaQAKG-Full)and50%KG(MetaQAKG-50)settings. Thenumbersreportedinthistableare
hits@1.NumbersinbracketscorrespondtoasettingwheretextwasusedtoaugmenttheincompleteKG(MetaQA
KG-50). Formoredetailspleaserefersection5.3.1.
sub-graph. ItalsousesagraphCNNapproach headnodeanditisabletolearnthecorresponding
toperformreasoning. relationembeddingfromthequestion. Ontheother
hand performance on 2-hop and 3-hop questions
The complete KG setting is the easiest setting
suggestthatEmbedKGQAisabletoinferthecor-
forQAbecausethedatasetsarecreatedinsucha
rect relation from the neighboring edges because
waythattheansweralwaysexistsintheKG,and
theKGembeddingscanmodelcompositionofrela-
there is no missing link in the path. However, it
tions. PullnetandGraftNetalsoperformsimilarly
isnotarealisticsetting,andtheQAmodelshould
wellbecausetheanswerentityliesinthequestion
alsobeabletoworkonanincompleteKG.Sowe
sub-graphmostofthetimes.
simulateanincompleteKBbyrandomlyremoving
We have also tested our method on the incom-
halfofthetriplesintheKB(werandomlydropa
pleteKGsetting,asexplainedintheprevioussec-
fact with probability = 0.5). We call this setting
tion. Herewefindthattheaccuracyofallbaselines
KG-50andwecallfullKGsettingKG-Fullinthe
decreasessignificantlycomparedtothefullKGset-
text.
ting,whileEmbedKGQAachievesstate-of-the-art
Inthenextsectionwewillanswerthefollowing
performance. ThisisbecauseMetaQAKGisfairly
questions:
sparse,withonly135ktriplesfor43kentities. So
Q1. CanKnowledgeGraphembeddingsbeused
when50%ofthetriplesareremoved(asisdonein
toperformmulti-hopKGQA?(Section5.3)
MetaQAKG-50),thegraphbecomesverysparse
Q2. CanEmbedKGQAbeusedtoanswerques-
withanaverageofonly1.66linksperentitynode.
tionswhenthereisnodirectpathbetweenthehead
This causes many head entity nodes of questions
entityandtheanswerentity? (Section5.4)
to have much longer paths (>3) to their answer
Q3. Howmuchdoestheanswerselectionmod-
node. Hencemodelsthatrequirequestion-specific
ule help in the final performance of our model?
sub-graphconstruction(GraftNet,PullNet)areun-
(Section5.5)
abletorecalltheanswerentityintheirgenerated
### 5.3 KGQAresults sub-graphandthereforeperformspoorly. However,
their performance improves only after including
Inthissection,wehavecomparedourmodelwith
additional text corpora. On the other hand, Em-
baselinemodelsonMetaQAandWebQuestionsSP
bedKGQAdoesnotlimititselftoasub-graphand
datasets.
utilizingthelinkpredictionpropertiestheKGem-
#### 5.3.1 AnalysisonMetaQA
beddings,EmbedKGQAisabletoinfertherelation
MetaQAhasdifferentpartitionsofthedatasetfor onmissinglinks.
1-hop,2-hop,and3-hopquestions. InthefullKG
#### 5.3.2 AnalysisonWebQuestionsSP
setting(MetaQAKG-Full)ourmodeliscompara-
bletothestate-of-the-artfor2-hopquestionsand WebQuestionsSPhasarelativelysmallnumberof
establishesthestate-of-the-artfor3-hopquestions. trainingexamplesbutusesalargeKG(Freebase)
EmbedKGQAperformssimilartothestate-of-the asbackgroundknowledge. Thismakesmulti-hop
in case of 1-hop question which is expected be- KGQA much harder. Since all the entities of the
causetheanswernodeisdirectlyconnectedtothe KGarenotcoveredinthetrainingset,freezingthe
4503

Model WebQSPKG-Full WebQSPKG-50 Model Accuracy
KV-Mem 46.7 32.7(31.6) ComplEx 20.1
GraftNet 66.4 48.2(49.7) EmbedKGQA 29.9
PullNet 68.1 50.1(51.9)
Table4: QAresultsonMetaQA1-hopfortheexperi-
EmbedKGQA 66.6 53.2
mentsinwhichthereisnolinkbetweenheadentityand
Table3: PerformanceonWebQuestionsSPdataset. All answer entity. We have compared the results with the
baselineresultsweretakenfromSunetal.(2019a).The KG completion methods in which gold relation of the
valuesreportedarehits@1. Numbersinbracketscorre- questionisknown. ThedetailsareprovidedinSection
spondtoasettingwheretextwasusedtoaugmentthe 5.4.
incomplete KG (WebQSP KG-50). For more details
pleasereferSection5.3.2.
WebQSP WebQSP
Model
KG-Full KG-50
EmbedKGQA 66.6 53.2
entityembeddingsafterlearningthemduringKG
{+2-hopfiltering} 72.5 51.8
embedding learning phase (Section 4.2) is neces- (cid:26) +2-hopfiltering, (cid:27)
58.7 48.5
sary. ResultsonWebQuestionsSP(Table3)high- –Relationmatching
{–Relationmatching} 48.1 47.4
light the fact that, even with a small number of
training examples EmbedKGQA can learn good
Table 5: This table show the importance of relation
questionembeddingsthatcaninferthemulti-hop matching module (Section 4.4.1) and effect of neigh-
pathrequiredtoanswerthequestions. bourhood based filtering on EmbedKGQA in the We-
OurmethodonWebQSPKG-50outperformsall bQuestionsSPdataset. EmbedKGQAinitselfcontains
the relation matching module. Here we try to see the
baselinesincludingPullNet,whichusesextratex-
effect of ablating the relation matching module and
tualinformationandisthestate-of-the-artmodel.
addinga2-hopneighbourhoodfilteringduringanswer
EventhoughWebQuestionsSPhasfewerquestions,
selection. PleasereferSection5.5formoredetails.
EmbedKGQA is able to learn good question em-
beddingsthatcaninfermissionlinksinKG.This
canbeattributedtothefactthatrelevantandnec- KnowledgeGraphEmbeddings.
essaryinformationisbeingcapturedthroughKG
So unlike other QA systems, even if there is
embeddings,implicitly.
no path between the head and answer entity, our
model should be able to answer the question if
### 5.4 QAonKGwithmissinglinks
thereissufficientinformationintheKGtobeable
State-of-the-art KGQA models like PullNet and topredictthatpath(SeeFig. 1).
GraftNetrequireapathbetweentheheadentityand We design an experiment to test this capabil-
theanswerentitytobepresentintheKnowledge ity of our model. For all questions in the vali-
Graph to answer the question. For example, in dation set of the MetaQA 1-hop dataset, we re-
PullNet, the answer is restricted to be one of the moved all the triples from the Knowledge Graph
entitiespresentintheextractedquestionsubgraph. that can be directly used to answer the question.
For the incomplete KG case where only 50% of For example, given the question ‘what language
theoriginaltriplesarepresent,PullNet(Sunetal., is [PK] in’ in the validation set, we removed the
2019a)reportsarecallof0.544ontheMetaQA1- triple (PK,in language,Hindi) from the KG.
hopdataset. Thismeansthatonlyfor54.4percent Thedatasetalsocontainsparaphrasesofthesame
ofquestions,alltheanswerentitiesarepresentin question, for, e.g., ‘what language is the movie
the extracted question subgraph, and this puts a [PK]in’and‘whatisthelanguagespokeninthe
hardlimit onhowmanyquestions themodel can movie[PK]’.Wealsoremovedallparaphrasesof
answerinthissetting. validation set questions from the training dataset
EmbedKGQA,ontheotherhand, usesKnowl- sinceweonlywanttoevaluatetheKGcompletion
edge Graph Embeddings rather than a localized propertyofourmodelandnotalinguisticgeneral-
sub-graphtoanswerthequestion. Itusesthehead ization.
embeddingandquestionembedding,whichimplic- In such a setting, we expect models that rely
itly captures the knowledge of all observed and only on sub-graph retrieval to achieve 0 hits@1.
unobserved links around the head node. This is However,ourmodeldeliversasignificantlybetter
possiblebecauseofthelinkpredictionpropertyof 29.9 hits@1 in this setting. This shows that our
4504

| model      | can capture |     | the KG | completion |     | property  | 6 Conclusion |        |            |            |     |     |         |

| of ComplEx | embeddings  |     |        | and apply  | it  | to answer |              |        |            |            |     |     |         |
|            |             |     |        |            |     |           | In this      | paper, | we propose | EmbedKGQA, |     |     | a novel |
questionswhichwasotherwiseimpossible.
|     |     |     |     |     |     |     | method | for Multi-hop |     | KGQA. | KGs | are often | in- |

Further,ifweknowtherelationcorresponding
completeandsparsewhichposesadditionalchal-
| to each | question, | then | the | problem | of  | 1-hop KG |                                |     |     |     |     |           |     |

|         |           |      |     |         |     |          | lengesformulti-hopKGQAmethods. |     |     |     |     | Recentre- |     |
QAisthesameasKGcompletioninanincomplete centforthisproblemhavetriedtoaddressthein-
| KnowledgeGraph. |     | UsingthesametrainingKGas |     |     |     |     |              |     |         |              |     |               |     |

|                 |     |                          |     |     |     |     | completeness |     | problem | by utilizing |     | an additional |     |
aboveandusingtheremovedtriplesasthetestset,
|     |     |     |     |     |     |     | text corpus. |     | However, | the | availability | of  | a rele- |

wedotailpredictionusingKGembeddings. Here vanttextcorpusisoftenlimited,therebyreducing
| we obtain | 20.1 | hits@1. | The | lesser | score | can be |                                           |     |     |     |     |     |     |

|           |      |         |     |        |       |        | broad-coverageapplicabilityofsuchmethods. |     |     |     |     |     | In  |
attributedtothefactthatComplExembeddinguses
|     |     |     |     |     |     |     | a separate | line | of research, |     | KG embedding |     | meth- |

onlytheKGwhileourmodelusestheQAdataas
odshavebeenproposedtoreduceKGsparsityby
| well - which | in  | itself | represents |     | knowledge. | Our |                                  |     |     |     |     |           |     |

|              |     |        |            |     |            |     | performingmissinglinkprediction. |     |     |     |     | EmbedKGQA |     |
modelisfirsttrainedontheKGandthenusesthese
utilizesthelinkpredictionpropertiesofKGembed-
embeddingstotraintheQAmodel,andthusitcan
dingstomitigatetheKGincompletenessproblem
leveragetheknowledgepresentinboththeKGand withoutusinganyadditionaldata. IttrainstheKG
QAdata.
|     |     |     |     |     |     |     | entity embeddings |           | and        | uses | it to       | learn question |        |

|     |     |     |     |     |     |     | embeddings,       |           | and during | the  | evaluation, | it             | scores |
|     |     |     |     |     |     |     | (head entity,     | question) |            | pair | again       | all entities,  | and    |
### 5.5 EffectofAnswerSelectionModule
thehighest-scoringentityisselectedasananswer.
|     |     |     |     |     |     |     | EmbedKGQA |     | also overcomes |     | the | shortcomings |     |

Weanalysetheeffectoftheanswerselectionmod-
|     |     |     |     |     |     |     | due to | limited | neighborhood |     | size | constraint | im- |

ule(Section4.4)onEmbedKGQAintheWebQues-
|     |     |     |     |     |     |     | posedbyexistingmulti-hopKGQAmethods. |     |     |     |     |     | Em- |

tionsSPdatasetbyablatingtherelationmatching
bedKGQAachievesstate-of-the-artperformancein
| module. | Furthermore, |     | in  | order | to compare | with |     |     |     |     |     |     |     |

multipleKGQAsettings,suggestingthatthelink
| other methods |     | that | restrict | the answer |     | to a neigh- |     |     |     |     |     |     |     |

predictionpropertiesofKGembeddingscanbeuti-
bourhoodintheKG(Sunetal.(2019a),Sunetal.
lizedtomitigatetheKGincompletenessproblem
(2018)),weexperimentedwithrestrictingthecandi-
inMulti-hopKGQA.
datesetofanswerentitiestoonlythe2-hopneigh-
| bourhood | of  | the head | entity. | The | results | can be |     |     |     |     |     |     |     |

Acknowledgements
| seeninTable5. |     | Aswecansee,relationmatching |     |     |     |     |          |      |          |     |           |     |         |

|               |     |                             |     |     |     |     | We would | like | to thank | the | anonymous |     | review- |
hasasignificantimpactontheperformanceofEm-
bedKGQAonbothWebQSPKG-fullandWebQSP ersfortheirconstructivefeedback,andAshutosh
| KG-50settings. |     |     |     |     |     |     | Kumar,AdityaRastogiandChandrahasfromthe |     |     |     |     |     |     |

IndianInstituteofSciencefortheirinsightfulcom-
Also,asmentionedearlier,WebQSPKG(Free-
ments. Thisresearchissupportedinpartbyagrant
basesubset)hasanorderofmagnitudemoreenti-
|     |     |     |     |     |     |     | from Intel | and | the Ministry |     | of Human | Resource |     |

tiesthanMetaQA(1.8Mversus134kinMetaQA)
Development,GovernmentofIndia.
| andthenumberofpossibleanswersislarge. |     |     |     |     |     | Sore- |     |     |     |     |     |     |     |

ducingthesetofanswerstoa2-hopneighbourhood
oftheheadentityshowedimprovedperformance
References
| in the case | of  | WebQSP | KG-Full. |     | However, | this |       |              |      |        |     |         |     |

|             |     |        |          |     |          |      | Ivana | Balazˇevic´, | Carl | Allen, | and | Timothy | M   |
causedadegradationinperformanceonWebQSP
|                                        |      |            |             |     |     |           | Hospedales.       |     | 2019. | Tucker:     | Tensor | factorization |          |

| KG-50.                                 | This | is because | restricting |     | the | answer to |                   |     |       |             |        |               |          |
|                                        |      |            |             |     |     |           | for knowledge     |     | graph | completion. |        | arXiv         | preprint |
| a2-hopneighbourhoodonanincompleteKGmay |      |            |             |     |     |           | arXiv:1901.09590. |     |       |             |        |               |          |
causetheanswertonotbepresentinthecandidates
(Pleasereferfigure1). Junwei Bao, Nan Duan, Zhao Yan, Ming Zhou, and
|     |     |     |     |     |     |     | Tiejun | Zhao. | 2016. | Constraint-based |     | question | an- |

In summary, we find that relation matching is swering with knowledge graph. In Proceedings of
|              |      |     |            |     |          |     | COLING | 2016, | the | 26th International |     | Conference |     |

| an important | part | of  | EmbedKGQA. |     | Morever, | we  |        |       |     |                    |     |            |     |
suggestthatn-hopfilteringduringanswerselection on Computational Linguistics: Technical Papers,
pages2503–2514.
maybeincludedontopofEmbedKGQAforKGs
whicharereasonablycomplete. Antoine Bordes, Sumit Chopra, and Jason Weston.
4505

2014a. Question answering with subgraph embed- So¨renAuer,etal.2015. Dbpedia–alarge-scale,mul-
dings. arXivpreprintarXiv:1406.3676. tilingual knowledge base extracted from wikipedia.
SemanticWeb,6(2):167–195.
| Antoine Bordes, |     | Nicolas | Usunier,    | Sumit  | Chopra, | and      |           |     |          |        |     |          |       |

|                 |     |         |             |        |         |          | Dingcheng | Li, | Jingyuan | Zhang, | and | Ping Li. | 2018. |
| Jason Weston.   |     | 2015.   | Large-scale | simple |         | question |           |     |          |        |     |          |       |
answering with memory networks. arXiv preprint Representation learning for question classification
arXiv:1506.02075. via topic sparse autoencoder and entity embedding.
In2018IEEEInternationalConferenceonBigData
Antoine Bordes, Nicolas Usunier, Alberto Garcia- (BigData),pages126–133.IEEE.
| Duran, | Jason | Weston, | and | Oksana | Yakhnenko. |     |     |     |     |     |     |     |     |

YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
| 2013. Translating |       | embeddings  |     | for modeling |             | multi- |            |       |       |      |       |      |        |

|                   |       |             |     |              |             |        | dar Joshi, | Danqi | Chen, | Omer | Levy, | Mike | Lewis, |
| relational        | data. | In Advances |     | in neural    | information |        |            |       |       |      |       |      |        |
processingsystems,pages2787–2795. Luke Zettlemoyer, and Veselin Stoyanov. 2019.
|     |     |     |     |     |     |     | Roberta: | A   | robustly optimized |     | bert | pretraining | ap- |

Antoine Bordes, Jason Weston, and Nicolas Usunier. proach. arXivpreprintarXiv:1907.11692.
| 2014b.                | Openquestionansweringwithweaklysuper- |     |                        |     |     |     |                   |       |              |               |      |          |          |

|                       |                                       |     |                        |     |     |     | Denis Lukovnikov, |       | Asja         | Fischer,      | Jens | Lehmann, | and      |
| visedembeddingmodels. |                                       |     | InJointEuropeanconfer- |     |     |     |                   |       |              |               |      |          |          |
|                       |                                       |     |                        |     |     |     | So¨ren            | Auer. | 2017. Neural | network-based |      |          | question |
enceonmachinelearningandknowledgediscovery
answeringoverknowledgegraphsonwordandchar-
indatabases,pages165–180.Springer.
|     |     |     |     |     |     |     | acterlevel. | InProceedingsofthe26thinternational |     |     |     |     |     |

Zihang Dai, Lei Li, and Wei Xu. 2016. Cfo: Con- conference on World Wide Web, pages 1211–1220.
ditional focused neural question answering with InternationalWorldWideWebConferencesSteering
Committee.
| large-scale | knowledge |     | bases. |     | arXiv | preprint |     |     |     |     |     |     |     |

arXiv:1606.01994.
|     |     |     |     |     |     |     | Alexander | Miller, | Adam | Fisch, | Jesse | Dodge, | Amir- |

HosseinKarimi,AntoineBordes,andJasonWeston.
| Tim Dettmers, | Pasquale |     | Minervini, | Pontus | Stenetorp, |     |     |     |     |     |     |     |     |

2016. Key-valuememorynetworksfordirectlyread-
| and Sebastian |     | Riedel. | 2018. | Convolutional |     | 2d  |     |     |     |     |     |     |     |

arXivpreprintarXiv:1606.03126.
| knowledge | graph | embeddings. |     | In  | Thirty-Second |     | ingdocuments. |     |     |     |     |     |     |

AAAIConferenceonArtificialIntelligence. Tom M. Mitchell, William W. Cohen, Estevam R. Hr-
|          |      |      |      |       |     |        | uschka   | Jr., Partha | P. Talukdar, |         | Bo Yang, | Justin | Bet-    |

| Li Dong, | Furu | Wei, | Ming | Zhou, | and | Ke Xu. |          |             |              |         |          |        |         |
|          |      |      |      |       |     |        | teridge, | Andrew      | Carlson,     | Bhavana |          | Dalvi  | Mishra, |
2015. Questionansweringoverfreebasewithmulti-
|                                    |            |                           |         |         |                 |          | Matt     | Gardner,   | Bryan Kisiel,   |        | Jayant    | Krishnamurthy, |       |

| columnconvolutionalneuralnetworks. |            |                           |         |         | InProceed-      |          |          |            |                 |        |           |                |       |
|                                    |            |                           |         |         |                 |          | Ni Lao,  | Kathryn    | Mazaitis,       | Thahir | Mohamed,  |                | Nda-  |
| ings of                            | the 53rd   | Annual                    | Meeting | of      | the Association |          |          |            |                 |        |           |                |       |
|                                    |            |                           |         |         |                 |          | pandula  | Nakashole, | Emmanouil       |        | A.        | Platanios,     | Alan  |
| for Computational                  |            | Linguistics               |         | and     | the 7th         | Interna- |          |            |                 |        |           |                |       |
|                                    |            |                           |         |         |                 |          | Ritter,  | Mehdi      | Samadi,         | Burr   | Settles,  | Richard        | C.    |
| tional Joint                       | Conference |                           | on      | Natural | Language        | Pro-     |          |            |                 |        |           |                |       |
|                                    |            |                           |         |         |                 |          | Wang,    | Derry      | Wijaya, Abhinav |        | Gupta,    | Xinlei         | Chen, |
| cessing(Volume1:                   |            | LongPapers),pages260–269. |         |         |                 |          |          |            |                 |        |           |                |       |
|                                    |            |                           |         |         |                 |          | Abulhair | Saparov,   | Malcolm         |        | Greaves,  | and            | Joel  |
|                                    |            |                           |         |         |                 |          | Welling. | 2018.      | Never-ending    |        | learning. | Commun.        |       |
| Google. 2013.                      |            | Freebase                  | data    | dumps.  | https://        |          |          |            |                 |        |           |                |       |
ACM,61(5):103–115.
developers.google.com/freebase/data.
|              |         |     |        |           |        |     | Salman | Mohammed, | Peng | Shi, | and Jimmy | Lin. | 2017. |

| Yanchao Hao, | Yuanzhe |     | Zhang, | Kang Liu, | Shizhu | He, |        |           |      |      |           |      |       |
Strongbaselinesforsimplequestionansweringover
| ZhanyiLiu,HuaWu,andJunZhao.2017. |     |     |     |     |     | Anend- |     |     |     |     |     |     |     |

knowledgegraphswithandwithoutneuralnetworks.
| to-end | model | for question |     | answering | over | knowl- |     |     |     |     |     |     |     |

arXivpreprintarXiv:1712.01969.
| edge base  | with                              | cross-attention |     | combining |     | global |            |         |        |        |     |            |     |

| knowledge. | InProceedingsofthe55thAnnualMeet- |                 |     |           |     |        |            |         |        |        |     |            |     |
|            |                                   |                 |     |           |     |        | Maximilian | Nickel, | Volker | Tresp, | and | Hans-Peter |     |
ingoftheAssociationforComputationalLinguistics
|     |     |     |     |     |     |     | Kriegel. | 2011. | A three-way |     | model | for collective |     |

(Volume1: LongPapers),pages221–231. learning on multi-relational data. In ICML, vol-
ume11,pages809–816.
| Frank L Hitchcock. |     | 1927. | The | expression | of  | a tensor |     |     |     |     |     |     |     |

orapolyadicasasumofproducts. JournalofMath- Fabian M Suchanek, Gjergji Kasneci, and Gerhard
ematicsandPhysics,6(1-4):164–189. Weikum.2007. Yago:acoreofsemanticknowledge.
InProceedingsofthe16thinternationalconference
| SeyedMehranKazemiandDavidPoole.2018. |     |     |     |     |     | Simple |     |     |     |     |     |     |     |

onWorldWideWeb,pages697–706.ACM.
embeddingforlinkpredictioninknowledgegraphs.
In Advances in Neural Information Processing Sys- Haitian Sun, Tania Bedrax-Weiss, and William W Co-
tems,pages4284–4295. hen.2019a. Pullnet: Opendomainquestionanswer-
|     |     |     |     |     |     |     | ing with | iterative | retrieval | on  | knowledge | bases | and |

Thomas N Kipf and Max Welling. 2016. Semi- text. arXivpreprintarXiv:1904.09537.
| supervised | classification |     | with | graph | convolutional |     |     |     |     |     |     |     |     |

networks. arXivpreprintarXiv:1609.02907. HaitianSun,BhuwanDhingra,ManzilZaheer,Kathryn
Mazaitis,RuslanSalakhutdinov,andWilliamWCo-
JensLehmann,RobertIsele,MaxJakob,AnjaJentzsch, hen. 2018. Open domain question answering using
Dimitris Kontokostas, Pablo N Mendes, Sebastian early fusion of knowledge bases and text. arXiv
Hellmann, Mohamed Morsey, Patrick Van Kleef, preprintarXiv:1809.00782.
4506

Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, and Jian
Tang. 2019b. Rotate: Knowledge graph embed-
dingbyrelationalrotationincomplexspace. arXiv
preprintarXiv:1902.10197.
The´oTrouillon,JohannesWelbl,SebastianRiedel,E´ric
Gaussier, and Guillaume Bouchard. 2016. Com-
plex embeddings for simple link prediction. In In-
ternationalConferenceonMachineLearning,pages
2071–2080.
Ledyard R Tucker. 1966. Some mathematical notes
on three-mode factor analysis. Psychometrika,
31(3):279–311.
Ferhan Ture and Oliver Jojic. 2016. No need to
pay attention: Simple recurrent neural networks
work!(for answering” simple” questions). arXiv
preprintarXiv:1606.05029.
Shikhar Vashishth, Soumya Sanyal, Vikram Nitin,
Nilesh Agrawal, and Partha Talukdar. 2019. In-
teracte: Improving convolution-based knowledge
graphembeddingsbyincreasingfeatureinteractions.
arXivpreprintarXiv:1911.00219.
Bishan Yang, Wen-tau Yih, Xiaodong He, Jianfeng
Gao, and Li Deng. 2014a. Embedding entities and
relations for learning and inference in knowledge
bases. arXivpreprintarXiv:1412.6575.
Min-Chul Yang, Nan Duan, Ming Zhou, and Hae-
ChangRim.2014b. Jointrelationalembeddingsfor
knowledge-based question answering. In Proceed-
ingsofthe2014conferenceonempiricalmethodsin
natural language processing (EMNLP), pages 645–
650.
Min-ChulYang,Do-GilLee,So-YoungPark,andHae-
Chang Rim. 2015. Knowledge-based question an-
swering using the semantic embedding space. Ex-
pertSystemswithApplications,42(23):9086–9104.
Scott Wen-tau Yih, Ming-Wei Chang, Xiaodong He,
and Jianfeng Gao. 2015. Semantic parsing via
stagedquerygraphgeneration: Questionanswering
withknowledgebase.
WentauYih,MatthewRichardson,ChristopherMeek,
Ming-WeiChang,andJinaSuh.2016. Thevalueof
semanticparselabelingforknowledgebasequestion
answering. InACL.
WenpengYin, MoYu, BingXiang, BowenZhou, and
Hinrich Schu¨tze. 2016. Simple question answering
by attentive convolutional neural network. arXiv
preprintarXiv:1606.03391.
Yuyu Zhang, Hanjun Dai, Zornitsa Kozareva, Alexan-
derJSmola,andLeSong.2018. Variationalreason-
ing for question answering with knowledge graph.
In Thirty-Second AAAI Conference on Artificial In-
telligence.
4507

---
**Source PDF:** `2021_15_article.pdf`
