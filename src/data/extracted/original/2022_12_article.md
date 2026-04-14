A Cluster-based Approach for Improving Isotropy
in Contextual Embedding Space
SaraRajaee1 and MohammadTaherPilehvar1,2
## 1 IranUniversityofScienceandTechnology,Tehran,Iran
## 2 TehranInstituteforAdvancedStudies,Tehran,Iran
sara rajaee@comp.iust.ac.ir
mp792@cam.ac.uk
Abstract Tobetterunderstandtherepresentationdegener-
ationprobleminpre-trainedmodels,weanalyzed
The representation degeneration problem in
the embedding space of GPT-2 (Radford et al.,
Contextual Word Representations (CWRs)
hurts the expressiveness of the embedding 2019),BERT(Devlinetal.,2019),andRoBERTa
space by forming an anisotropic cone where (Liu et al., 2019). We found that, despite being
evenunrelatedwordshaveexcessivelypositive extremelyanisotropicinallnon-inputlayersfrom
correlations. Existing techniques for tackling aglobalsight,theembeddingspaceissignificantly
thisissuerequirealearningprocesstore-train
more isotropic from a local point of view (when
models with additional objectives and mostly
embeddingsareclusteredandeachclusterismade
employ a global assessment to study isotropy.
zero-mean). Motivated by this observation and
Our quantitative analysis over isotropy shows
that a local assessment could be more accu- based on previous studies that highlight the clus-
rate due to the clustered structure of CWRs. teredstructureofCWRs(Reifetal.,2019;Michael
Basedonthisobservation,weproposealocal et al., 2020), we extend the technique of Mu and
cluster-basedmethodtoaddressthedegenera- Viswanath (2018) with a further clustering step.
tionissueincontextualembeddingspaces.We
In our proposal, we cluster embeddings and ap-
show that in clusters including punctuations
ply PCA on individual clusters to find the corre-
and stop words, local dominant directions en-
sponding principal components (PCs) which in-
code structural information, removing which
dicate the dominant directions for each specific
can improve CWRs performance on semantic
tasks. Moreover, we find that tense informa- cluster. NullingoutthesePCsforeachclusterren-
tion in verb representations dominates sense ders a more isotropic space. We evaluated our
semantics. We show that removing dominant cluster-based method on several tasks, including
directions of verb representations can trans- Semantic Textual Similarity (STS) and Word-in-
formthespacetobettersuitsemanticapplica-
Context(WiC).Experimentalresultsindicatethat
tions. Our experiments demonstrate that the
ourcluster-basedmethodiseffectiveinenhancing
proposed cluster-based method can mitigate
the isotropy of different CWRs, reflected by the
thedegenerationproblemonmultipletasks.1
significantperformanceimprovementsinmultiple
## 1 Introduction
evaluationbenchmarks.
Despitetheiroutstandingperformance,CWRsare In addition, we provide an analysis on the rea-
known to suffer from the so-called representa- sonsbehindtheeffectivenessofourcluster-based
tiondegenerationproblemthatmakestheembed- technique. The empirical results show that most
ding space anisotropic (Gao et al., 2019). In an clusters contain punctuation tokens, such as peri-
anisotropicembeddingspace,wordvectorsaredis- odsandcommas. ThePCsoftheseclustersencode
tributedinanarrowcone,inwhichevenunrelated structuralinformationaboutcontext,suchassen-
wordsaredeemedtohavehighcosinesimilarities. tence style; hence, removing them can improve
Thisundesirablepropertyhamperstherepresenta- CWRsperformanceonsemantictasks. Asimilar
tivenessoftheembeddingspaceandlimitsthedi- structure exists in other clusters containing stop
versityofencodedknowledge(Ethayarajh,2019). words. The other important observation is about
verbdistributioninthecontextualembeddingspace.
1The code for our experiments is available at https:
Our experiments reveal that verb representations
//github.com/Sara-Rajaee/clusterbased_
isotropy_enhancement/ areseparatedacrossthetensedimensionindistinct

Proceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguistics
andthe11thInternationalJointConferenceonNaturalLanguageProcessing(ShortPapers),pages575–584
August1–6,2021.©2021AssociationforComputationalLinguistics

| sub-spaces. |     | Thisbringsaboutanunwantedpecu- |     |        |                 |     |     |     |     |     |     |     |     |

| liarity     | in  | the semantic                   |     | space: | representations |     | for |     |     |     |     |     |     |
differentsensesofaverbtendtobeclosertoeach
otherinthespacethantherepresentationsforthe
samesensethatareassociatedwithdifferenttenses
| ofthesameverb. |         |         | Indeed,removingsuchPCsim- |               |     |       |      |     |     |     |     |     |     |

| proves         | model’s | ability |                           | in downstream |     | tasks | with |     |     |     |     |     |     |
dominantsemanticflavor.
## 2 IsotropyinCWRs
Isotropyisadesirablepropertyofwordembedding
spacesandarguablyanyothervectorrepresentation
| of           | data in | general                       | (Huang | et  | al., 2018; | Cogswell |     |           |               |                 |     |               |         |

|              |         |                               |        |     |            |          |     | Figure    | 1: Layer-wise | isotropy        |     | for different | CWRs on |
| etal.,2016). |         | Fromthegeometricpointofview,a |        |     |            |          |     |           |               |                 |     |               |         |
|              |         |                               |        |     |            |          |     |           |               | (↑log-isotropy: |     | ↑isotropy).   |         |
|              |         |                               |        |     |            |          |     | the STS-B | dev           | set             |     |               | Given   |
spaceiscalledisotropicifthevectorswithinthat
thelargedifference,BERTandRoBERTaareshownon
| space | are | uniformly | distributed |     | in  | all directions. |     |     |     |     |     |     |     |

theleftaxisandGPT-2ontheright.
| Lacking |     | isotropy | in the | embedding |     | space | affects |     |     |     |     |     |     |

notonlytheoptimizationprocedure(e.g.,model’s
theisotropyofGPT-2decreasesconsistentlyinup-
accuracyandconvergencetime)butalsotheexpres-
sivenessoftheembeddingspace;hence,improving per layers, that for RoBERTa has a semi-convex
theisotropyoftheembeddingspacecanleadtoper- form in which the last layer (except for the input
|     |     |     |     |     |     |     |     | layer)hasthehighestisotropy. |     |     |     | Also,interestingly, |     |

formanceimprovements(Wangetal.,2020;Ioffe
andSzegedy,2015). the input layer in GPT-2 is more isotropic than
We measure the isotropy of embedding space those for the other two models. This observation
usingthepartitionfunctionofAroraetal.(2016): contradictswithwhathasbeenpreviouslyreported
|     |     |     |     |     |     |     |     | by Ethayarajh(2019). |     |     |     |     |     |

𝑁
(cid:213) 𝑒𝑢𝑇𝑤
|       |     | 𝐹(𝑢)      | =       |     | 𝑖      |               | (1) |           |             |               |        |                       |           |

|       |     |           |         |     |        |               |     | Local     | assessment. |               | In the | light of the          | clustered |
|       |     |           |         | 𝑖=1 |        |               |     | structure | of          | the embedding |        | space in CWRs         | (Reif     |
|       | 𝑢   |           |         | 𝑤   |        |               |     | et al.,   | 2019),      | we carried    | out    | a local investigation |           |
| where |     | is a unit | vector, | 𝑖   | is the | corresponding |     |           |             |               |        |                       |           |
embeddingforthe𝑖𝑡ℎ wordintheembeddingma- of isotropy. To this end, we clustered the space
using𝑘-meansandmeasuredisotropyaftermaking
| trix | W ∈ | IRN×D, | N is the | number | of  | words | in the |     |     |     |     |     |     |

eachclusterzero-mean(MuandViswanath,2018).
| vocabulary, |     | and D | is the | embedding |     | size. | Arora |     |     |     |     |     |     |

etal.(2016)showedthat𝐹(𝑢)canbeapproximated Table 1 shows the results for different number of
using a constant for isotropic embedding spaces. clusters(eachbeingtheaverageoffiveruns). When
Therefore,fortheset𝑈,whichisthesetofeigen- theembeddingspaceisviewedclosely,thedistri-
𝑇 W,inthefollowingequation,I(W) butionofCWRsisnotablymoreisotropic. Cluster-
vectorsofW
wouldbeclosetooneforaperfectlyisotropicspace ingsignificantlyenhancesisotropyforBERTand
(MuandViswanath,2018). RoBERTa,makingtheirembeddingspacesalmost
|     |     |      |     |     |      |     |     | isotropic. | However,                            |     | GPT-2isstillfarfrombeing |     |     |

|     |     |      | 𝑚𝑖𝑛 | 𝑢∈𝑈 | 𝐹(𝑢) |     |     |            |                                     |     |                          |     |     |
|     |     | I(W) | =   |     |      |     | (2) | isotropic. | Thiscontradictswiththeobservationof |     |                          |     |     |
|     |     |      | 𝑚𝑎𝑥 | 𝑢∈𝑈 | 𝐹(𝑢) |     |     |            |                                     |     |                          |     |     |
Caietal.(2021).
Apossibleexplanationforthesecontradictions
### 2.1 AnalyzingIsotropyinpre-trainedCWRs
|     |     |     |     |     |     |     |     | isthedifferentmetricusedby |     |     |     | Ethayarajh(2019) |     |

Usingtheabovemetric,weanalyzedtherepresen-
|     |     |     |     |     |     |     |     | and Cai | et al. | (2021) | for measuring | isotropy: | co- |

tationdegenerationproblemgloballyandlocally.
|     |     |     |     |     |     |     |     | sine similarity. |     | Randomly |     | sampled words | in an |

Globalassessment. Wequantifiedisotropyinall anisotropicembeddingspaceshouldhavehighco-
layers for GPT-2, BERT, and RoBERTa on the sine similarities (a near-zero similarity denotes
development set of STS-Benchmark (Cer et al., isotropy). However, there are exceptional cases
2017). Figure1showsthetrendofisotropyinall wherethismightnothold(ananisotropicembed-
layers based on I(W). Clearly, all CWRs are ex- ding space where sampled words have near-zero
tremelyanisotropicinallnon-inputlayers. While cosinesimilarities). InFigure2,weillustrateGPT-


GPT-2 BERT RoBERTa to this as the global approach. This method was
|          |     |           |          |     |          |     | proposed | for static | embeddings.    |     | Hence,      | it  | might |

| Baseline |     | 5.02E-174 | 5.05E-05 |     | 2.70E-06 |     |          |            |                |     |             |     |       |
|          |     |           |          |     |          |     | not be   | optimal    | for contextual |     | embeddings, |     | espe- |
𝑘
| =1   |     | 2.49E-220 | 0.010 |     | 0.015 |     |           |           |      |            |       |     |        |

|      |     |           |       |     |       |     | cially in | the light | that | the latter | tends | to  | have a |
| 𝑘 =3 |     | 9.42E-66  | 0.040 |     | 0.290 |     |           |           |      |            |       |     |        |
𝑘 =6 1.40E-41 0.125 0.453 clusteredstructure. Forinstance,recentworksug-
𝑘
=9 1.18E-41 0.131 0.545 geststhatwordtypes(e.g.,verbs,nouns,punctua-
𝑘 =20 4.06E-47 0.262 0.603 tions),entities(e.g.,personhood,nationalities,and
dates),andevenwordsenses(Michaeletal.,2020;
| Table 1: | CWRs | isotropy | after | clustering | and | making |     |     |     |     |     |     |     |

Loureiroetal.,2021;Reifetal.,2019)createlocal
eachclusterzero-meanseparately(resultsfordifferent
distinctclusteredareasinthecontextualembedding
numberofclusters(𝑘)onSTS-Bdevset).
|     |     |     |     |     |     |     | space. Moreover,ourlocalassessmentshowsthat |     |     |     |     |     |     |

itisnotnecessarilythecasethatallclustersshare
|     |     |     |     |     |     |     | thesamedominantdirections. |     |     |     | Hence,discarding |     |     |

dominantdirectionsthatarecomputedgloballyis
notefficientforremovinglocaldegenerateddirec-
|     |     |     |     |     |     |     | tions. Consequently, |     | it  | is more | logical | to  | have a |

cluster-specificdroppingofdominantdirections.
|     |     |     |     |     |     |     | Based | on these | observations, |     | we  | propose | a   |

cluster-basedapproachforisotropyenhancement.
Specifically,insteadofdeterminingdominantdirec-
tionsglobally,weobtainthemseparatelyfordiffer-
entsub-spacesanddiscardforeachclusteronlythe
| Figure2: | GPT-2embeddingsonSTS-Bdevsetbefore |     |     |     |     |     |     |     |     |     |     |     |     |

correspondingcluster-specificdominantdirections.
(top)andafter(bottom)alocalzero-meanoperation.
Tothisend,weemployPrincipalComponentAnal-
ysis(PCA)tocomputelocaldominantdirections
2embeddingspaceasanexampleforsuchanex- in clusters. Geometrically, principal components
ceptional cases. Making individual clusters zero- (PCs)representthosedirectionsinwhichembed-
|     |     |     |     |     |     |     | dings have | the most | variance |     | (maximum |     | elonga- |

mean(bottom)improvesisotropyoverthebaseline
(top). However,theembeddingsarestillfarfrom tion). Inourproposedmethod,wefirstclusterword
embeddingsusingasimple𝑘-meansalgorithm.
| being uniformly |     | distributed |     | in all | directions. | In- |     |     |     |     |     |     | Af- |

stead,theyaredistributedaroundahorizontalline. ter making each cluster zero-mean, the top PCs
Thisleadstoanear-zerocosinesimilarityforran- ofeveryclusterareremovedseparately. Addinga
domlysampledwordswhiletheembeddingspace clusteringstephelpsustoeliminatethelocaldom-
isanisotropic. Hence,cosinesimilaritymightnot inant directions of each cluster. We will show in
Section5thatdifferentlinguisticknowledgeisen-
beapropermetricforcomputingisotropy.
codedinthedominantdirectionsofvariousclusters.
## 3 Cluster-basedIsotropyEnhancement Moreover,numericalresultsshowthatincompari-
sonwiththeglobalapproach,ourmethodcanmake
Thedegenerationproblemintheembeddingspace
|        |            |        |          |           |     |        | the embedding |     | space more | isotropic, |     | even | when |

| can be | attributed | to the | training | procedure |     | of the |               |     |            |            |     |      |      |
thefewernumberofPCsarenulledout.
underlyingmodels,whichareoftenlanguagemod-
| elstrainedthroughlikelihoodmaximizationwith |       |       |      |         |        |       | 4 Experiments |     |     |     |     |     |     |

| the weight                                  | tying | trick | (Gao | et al., | 2019). | Maxi- |               |     |     |     |     |     |     |
mizing the likelihood of a specific word embed- Wecarriedoutexperimentsonthefollowingbench-
ding(minimizingthatforothers)requirespushing marks. AsforSemanticTextualSimilarity(STS),
| it towards | the | direction | of the | corresponding |     | hid- |     |     |     |     |     |     |     |

whichisthemainbenchmarkforourexperiments,
denstate,whichresultsintheaccumulationofthe we experimented with STS 2012-2016 datasets
learntwordembeddingsintoanarrowcone. (Agirreetal.,2012,2013,2014,2015,2016),the
Previousworkhasshownthatnullingoutdomi- SICK-Relatednessdataset(SICK-R)(Marellietal.,
nantdirectionsofananisotropicembeddingspace 2014), and the STS benchmark (STS-B). For the
can make the space isotropic and improve its ex- STStask,wereportresultsforGPT-2,BERT,and
pressiveness(MuandViswanath,2018). Werefer RoBERTa. We also experimented witha number


|          |     | Model        |     | STS2012 | STS2013 |       | STS2014 |     | STS2015 | STS2016 |       | SICK-R STS-B |

|          |     | GPT-2        |     | 26.49   |         | 30.25 | 35.74   |     | 41.25   |         | 46.40 | 45.05 24.8   |
| Baseline |     | BERT-base    |     | 42.87   |         | 59.21 | 59.75   |     | 62.85   |         | 63.74 | 58.69 47.4   |
|          |     | RoBERTa-base |     | 33.09   |         | 56.44 | 46.76   |     | 55.44   |         | 60.88 | 61.28 56.0   |
|          |     | GPT-2        |     | 51.42   |         | 69.71 | 55.91   |     | 60.35   |         | 62.12 | 59.22 55.7   |
Globalapproach BERT-base 54.62 70.39 60.34 63.73 69.37 63.68 65.5
|     |     | RoBERTa-base |     | 51.59 |     | 73.57 | 60.70 |     | 66.72 |     | 69.34 | 65.82 70.1 |

|     |     | GPT-2        |     | 52.40 |     | 72.71 | 59.23 |     | 62.19 |     | 64.26 | 59.51 62.3 |
Cluster-basedapproach BERT-base 58.34 75.65 63.55 64.37 69.63 63.75 66.0
|     |     | RoBERTa-base |     | 54.87 |     | 76.70 | 64.18 |     | 67.05 |     | 69.28 | 66.93 71.4 |

Table2: Spearmancorrelationperformanceofthreepre-trainedmodels(baseline)ontheSemanticTextualSimi-
laritydatasets,beforeandafterisotropyenhancementwiththeglobalandcluster-based(our)approach.
|                       |     |     | RTE  | CoLA |     | SST-2 | MRPC |      | WiC  |     | BoolQ | Average |

| Baseline              |     |     | 54.4 | 38.0 |     | 80.1  |      | 70.2 | 60.0 |     | 64.7  | 61.2    |
| Globalapproach        |     |     | 56.2 | 38.8 |     | 80.2  |      | 72.1 | 60.7 |     | 64.9  | 62.1    |
| Cluster-basedapproach |     |     | 56.5 | 40.7 |     | 82.5  |      | 72.4 | 61.0 |     | 66.4  | 63.2    |
Table3: Resultsontheclassificationtasks(BERT)intermsofaccuracy(exceptforCoLA:Matthew’scorrelation).
of classification tasks: Recognizing Textual En- outtheoptimalnumberoftopdominantdirections
tailmentfromtheGLUEbenchmark(Wangetal., (tuned separately, cf. Appendix B), but the latter
2018,RTE),theCorpusofLinguisticAcceptability identifiesthembasedonthespecificstructureofa
(Warstadtetal.,2019,CoLA),StanfordSentiment sub-regionintheembeddingspace(whichmight
Treebank(Socheretal.,2013, SST-2), Microsoft notbesimilartoothersub-regions).
| Research | Paraphrase | Corpus | (Dolan | and | Brock- |     |            |     |     |     |     |     |

|          |            |        |        |     |        | 5   | Discussion |     |     |     |     |     |
ett,2005,MRPC),Word-in-Context(Pilehvarand
Camacho-Collados,2019,WiC),andBoolQ(Clark
|              |                                   |     |     |     |     | In  | this | section, | we  | provide | a brief | explanation |

| etal.,2019). | Fortheclassificationtasks,welimit |     |     |     |     |     |      |          |     |         |         |             |
forreasonsbehindtheeffectivenessofthecluster-
| our experiments |     | to BERT | and extract | features | to  |     |     |     |     |     |     |     |

basedapproachthroughinvestigatingthelinguistic
| train an MLP. | Further | details | on  | the datasets | and |           |     |         |     |        |          |              |

|               |         |         |     |              |     | knowledge |     | encoded |     | in the | dominant | local direc- |
systemconfigurationcanbefoundinAppendixB.
|     |     |     |     |     |     | tions. | We  | also | show | that | enhancing | isotropy re- |

Webenchmarkourcluster-basedapproachwith
ducesconvergencetime.
| the pre-trained | CWRs | (baseline) |     | and the | global |     |     |     |     |     |     |     |

method. Asitwasmentionedbefore,thismethod 5.1 Linguisticknowledge
| is similar | to ours    | in its elimination |          | of a       | few top |                           |     |     |     |     |                |     |

|            |            |                    |          |            |         | Punctuationsandstopwords. |     |     |     |     | Weobservedthat |     |
| dominant   | directions | but                | with the | difference | that    |                           |     |     |     |     |                |     |
localdominantdirectionsfortheclustersofpunctu-
thesedirectionsarecomputedglobally(incontrast
ationsandstopwordscarrystructuralandsyntactic
| toourlocalcluster-basedcomputation). |     |     |     | Thebest |     |     |     |     |     |     |     |     |

informationaboutthesentencesinwhichtheyap-
settingforeachmodelisselectedbasedonperfor-
|                        |     |     |                    |     |     | pear.    | For | example,              |     | the two | sentences | “A man is |

| manceontheSTS-Bdevset. |     |     | Thereportedresults |     |     |          |     |                       |     |         |           |           |
|                        |     |     |                    |     |     | crying.” |     | and“Awomanisdancing.” |     |         |           | fromSTS-B |
aretheaverageoffiveruns.
|     |     |     |     |     |     | donot | havemuch |     | incommon |     | interms | ofseman- |

ticsbutarehighlysimilarwithrespecttotheirstyle.
### 4.1 Results
|     |     |     |     |     |     | To  | quantitatively |     | analyze |     | the distribution | of this |

Tables2and3reportexperimentalresults. Ascan type of tokens in CWRs, we designed an experi-
be seen, globally increasing isotropy can make a mentbasedonthedatasetcreatedbyRavfogeletal.
significantimprovementforallthethreepre-trained (2020). The dataset consists of groups in which
models. However,ourcluster-basedapproachcan sentencesarestructurallyandsyntacticallysimilar
achievenotablyhigherperformancecomparedto buthavenosemanticsimilarity. Wepicked200dif-
theglobalapproach. Weattributethisimprovement ferentstructuralgroupsinwhicheachgrouphassix
toourcluster-specificdiscardingofdominantdirec- semanticallydifferentsentences. Then,usingthe
𝑘-NNalgorithm,wecalculatedthepercentageof
tions. Bothglobalandcluster-basedmethodsnull


|         |       | Baseline |       |          |       | RemovedPCs |       |          |

| Model   | ST-SM | ST-DM    | DT-SM | Isotropy | ST-SM | ST-DM      | DT-SM | Isotropy |
| GPT-2   | 48.82 | 48.19    | 50.86 | 2.26E-05 | 9.32  | 9.53       | 9.49  | 0.17     |
| BERT    | 13.44 | 14.24    | 14.87 | 2.24E-05 | 10.31 | 10.50      | 10.32 | 0.32     |
| RoBERTa | 5.89  | 6.31     | 6.86  | 1.22E-06 | 4.78  | 5.00       | 4.89  | 0.73     |
Table4: ThemeanEuclideandistanceofasampleoccurrenceofaverbtoallotheroccurrencesofthesameverb
with the Same-Tense and the Same-Meaning (ST-SM), the Same-Tense but Different-Meaning (ST-DM), and a
Different-TensebuttheSame-Meaning(DT-SM).Semantically,itisdesirableforDT-SMtobelowerthanST-DM.
|     |     |     |     | Figure4: | Theimpactofourcluster-basedisotropyen- |     |     |     |

hancementonper-epochperformancefortwotasks.
| Figure 3:     | The percentage | of nearest    | neighbours | that |     |     |     |     |

| share similar | structural     | and syntactic | knowledge, | be-  |     |     |     |     |
fore (lighter, pattern-filled) and after removing domi- ing. TheexperimentalresultsreportedinTable4
confirmthehypothesisandshowtheeffectiveness
nantdirectionsinpre-trainedCWRs.
ofthecluster-basedapproachinbringingtogether
|     |     |     |     | verb | representations | that | correspond | to the same |

nearestneighbourswhichareinthesamegroupbe-
sense,eveniftheyhavedifferenttense.
foreandafterremovinglocaldominantdirections.
Weevaluatedthisforperiodandcomma,whichare 5.2 Convergencetime
themostfrequentpunctuations,and“the”and“of”
|     |     |     |     | In  | the previous | experiments, | we  | showed that the |

asthemostcontextualizedstopwords(Ethayarajh,
contextualembeddingsareextremelyanisotropic
2019). ThereportedresultsinFigure3showthat
|     |     |     |     | andhighlycorrelated. |     | Suchembeddingscanslow |     |     |

therepresentationsforpunctuationsandstopwords
downthelearningprocessofdeepneuralnetworks.
arebiasedtowardstructuralandsyntacticinforma- Figure 4 shows the trend of convergence for the
tionofsentences;hence,removingtheirdominant
|     |     |     |     | BoolQandRTEtasks(devsets). |     |     | Bydecreasingthe |     |

directionsreducesthenumberofsame-groupnear-
correlationbetweenembeddings,ourmethodcan
est neighbours. The improvement from our local reduceconvergencetime.
isotropyenhancementcanbepartiallyattributedto
| attenuatingthistypeofbias. |     |     |     | 6   | Conclusions |     |     |     |

VerbTense. Ourexperimentsshowthattenseis Inthispaper,weproposedacluster-basedmethod
moredominantinverbrepresentationsthansense- to address the representation degeneration prob-
levelsemanticinformation. Tohaveapreciseexam- leminCWRs. Weempiricallyanalyzedtheeffect
inationofthishypothesis,weusedSemCor(Miller of clustering and showed that, from a local sight,
et al., 1993), a dataset comprising around 37K most clusters are biased toward structural infor-
sense-annotatedsentences. Wecollectedrepresen- mation. Moreover,wefoundthatverbrepresenta-
tationsforpolysemousverbsthathadatleasttwo tionsaredistributedbasedontheirtenseindistinct
sensesoccurringaminimumof10times. Then,for sub-spaces. Weevaluatedourmethodondifferent
eachindividualverb,wecalculatedEuclideandis- semantictasks,demonstratingitseffectivenessin
tancetothecontextualrepresentationofthesame removinglocaldominantdirectionsandimproving
verb: (1)withthesametenseandthesamemean- performance. Asfuturework,weplantostudythe
ing,(2)withthesametensebutadifferentmeaning, effectoffine-tuningonisotropyandontheencoded
and(3)withadifferenttenseandthesamemean- linguisticknowledgeinlocalregions.


| References    |        |       |                  |        |         |        | task1: Semantictextualsimilaritymultilingualand |               |             |          |     |             |     |

|               |        |       |                  |        |         |        | crosslingual                                    | focused       | evaluation. |          | In  | Proceedings |     |
| Eneko Agirre, | Carmen |       | Banea,           | Claire | Cardie, | Daniel |                                                 |               |             |          |     |             |     |
|               |        |       |                  |        |         |        | of the 11th                                     | International |             | Workshop |     | on Semantic |     |
| Cer, Mona     | Diab,  | Aitor | Gonzalez-Agirre, |        |         | Weiwei |                                                 |               |             |          |     |             |     |
Evaluation(SemEval-2017),pages1–14,Vancouver,
Guo,In˜igoLopez-Gazpio,MontseMaritxalar,Rada
Canada.AssociationforComputationalLinguistics.
Mihalcea,GermanRigau,LarraitzUria,andJanyce
Wiebe. 2015. SemEval-2015 task 2: Semantic tex- Christopher Clark, Kenton Lee, Ming-Wei Chang,
tual similarity, English, Spanish and pilot on inter- Tom Kwiatkowski, Michael Collins, and Kristina
pretability. In Proceedings of the 9th International Toutanova. 2019. BoolQ: Exploring the surprising
| Workshop       | on Semantic |         | Evaluation |     | (SemEval    | 2015), |            |            |        |            |     |             |     |

|                |             |         |            |     |             |        | difficulty | of natural | yes/no | questions. |     | In Proceed- |     |
| pages 252–263, |             | Denver, | Colorado.  |     | Association | for    |            |            |        |            |     |             |     |
ingsofthe2019ConferenceoftheNorthAmerican
ComputationalLinguistics. Chapter of the Association for Computational Lin-
|     |     |     |     |     |     |     | guistics: | Human | Language | Technologies, |     | Volume | 1   |

Eneko Agirre, Carmen Banea, Claire Cardie, Daniel (Long and Short Papers), pages 2924–2936, Min-
| Cer, Mona | Diab, | Aitor | Gonzalez-Agirre, |     |     | Weiwei |     |     |     |     |     |     |     |

neapolis,Minnesota.AssociationforComputational
| Guo, Rada | Mihalcea, |     | German | Rigau, | and | Janyce |     |     |     |     |     |     |     |

Linguistics.
| Wiebe.   | 2014.   | SemEval-2014 |     | task           | 10: Multilingual |        |                   |     |       |        |      |              |     |

| semantic | textual | similarity.  |     | In Proceedings |                  | of the |                   |     |       |        |      |              |     |
|          |         |              |     |                |                  |        | Michael Cogswell, |     | Faruk | Ahmed, | Ross | B. Girshick, |     |
8thInternationalWorkshoponSemanticEvaluation Larry Zitnick, and Dhruv Batra. 2016. Reducing
(SemEval 2014), pages 81–91, Dublin, Ireland. As- overfitting in deep networks by decorrelating rep-
sociationforComputationalLinguistics. resentations. In 4th International Conference on
|     |     |     |     |     |     |     | Learning | Representations, |     | ICLR | 2016, | San | Juan, |

EnekoAgirre,CarmenBanea,DanielCer,MonaDiab,
PuertoRico,May2-4,2016,ConferenceTrackPro-
| Aitor Gonzalez-Agirre, |     |     | Rada | Mihalcea, |     | German |     |     |     |     |     |     |     |

ceedings.
| Rigau, | and Janyce | Wiebe. |     | 2016. | SemEval-2016 |     |     |     |     |     |     |     |     |

task 1: Semantic textual similarity, monolingual Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
and cross-lingual evaluation. In Proceedings of the Kristina Toutanova. 2019. BERT: Pre-training of
10th International Workshop on Semantic Evalua- deep bidirectional transformers for language under-
| tion (SemEval-2016), |     |     | pages | 497–511, | San | Diego, |           |                |     |        |      |            |     |

|                      |     |     |       |          |     |        | standing. | In Proceedings |     | of the | 2019 | Conference |     |
California. Association for Computational Linguis- of the North American Chapter of the Association
| tics. |     |     |     |     |     |     | for Computational |        | Linguistics: |         | Human | Language       |     |

|       |     |     |     |     |     |     | Technologies,     | Volume |              | 1 (Long | and   | Short Papers), |     |
Eneko Agirre, Daniel Cer, Mona Diab, and Aitor pages4171–4186,Minneapolis,Minnesota.Associ-
| Gonzalez-Agirre. |     | 2012. | SemEval-2012 |     |     | task 6: A |     |     |     |     |     |     |     |

ationforComputationalLinguistics.
| pilotonsemantictextualsimilarity. |       |            |     |            | In*SEM2012: |        |                                      |     |     |     |     |           |     |

| The First                         | Joint | Conference |     | on Lexical | and         | Compu- |                                      |     |     |     |     |           |     |
|                                   |       |            |     |            |             |        | WilliamB.DolanandChrisBrockett.2005. |     |     |     |     | Automati- |     |
tational Semantics – Volume 1: Proceedings of the callyconstructingacorpusofsententialparaphrases.
main conference and the shared task, and Volume InProceedingsoftheThirdInternationalWorkshop
2: ProceedingsoftheSixthInternationalWorkshop onParaphrasing(IWP2005).
onSemanticEvaluation(SemEval2012),pages385–
393, Montre´al, Canada. Association for Computa- Kawin Ethayarajh. 2019. How contextual are contex-
tionalLinguistics. tualizedwordrepresentations? comparingthegeom-
|     |     |     |     |     |     |     | etry of BERT, |     | ELMo, | and GPT-2 | embeddings. |     | In  |

EnekoAgirre,DanielCer,MonaDiab,AitorGonzalez- Proceedings of the 2019 Conference on Empirical
Agirre,andWeiweiGuo.2013. *SEM2013shared Methods in Natural Language Processing and the
task: Semantic textual similarity. In Second Joint 9th International Joint Conference on Natural Lan-
Conference on Lexical and Computational Seman- guage Processing (EMNLP-IJCNLP), pages 55–65,
| tics (*SEM), | Volume |            | 1: Proceedings |       | of       | the Main |              |        |             |     |     |               |     |

|              |        |            |                |       |          |          | Hong Kong,   | China. | Association |     | for | Computational |     |
| Conference   | and    | the Shared |                | Task: | Semantic | Textual  | Linguistics. |        |             |     |     |               |     |
Similarity,pages32–43,Atlanta,Georgia,USA.As-
sociationforComputationalLinguistics. JunGao,DiHe,XuTan,TaoQin,LiweiWang,andTie-
|     |     |     |     |     |     |     | Yan Liu. | 2019. | Representation |     | degeneration |     | prob- |

SanjeevArora,YuanzhiLi,YingyuLiang,TengyuMa, lem in training natural language generation models.
andAndrejRisteski.2016. Alatentvariablemodel CoRR,abs/1907.12009.
| approachtoPMI-basedwordembeddings. |     |     |     |     |     | Transac- |     |     |     |     |     |     |     |

tions of the Association for Computational Linguis- ChengyueGong,DiHe,XuTan,TaoQin,LiweiWang,
tics,4:385–399. and Tie-Yan Liu. 2018. Frage: Frequency-agnostic
|     |     |     |     |     |     |     | word representation. |     | In  | Advances | in  | Neural | Infor- |

Xingyu Cai, Jiaji Huang, Yuchen Bian, and Kenneth mationProcessingSystems,volume31,pages1334–
Church. 2021. Isotropy in the contextual embed- 1345.CurranAssociates,Inc.
InInternational
dingspace:Clustersandmanifolds.
LeiHuang,DaweiYang,BoLang,andJiaDeng.2018.
ConferenceonLearningRepresentations.
|     |     |     |     |     |     |     | Decorrelated | batch | normalization. |     | In  | Proceedings |     |

Daniel Cer, Mona Diab, Eneko Agirre, In˜igo Lopez- oftheIEEEConferenceonComputerVisionandPat-
Gazpio, and Lucia Specia. 2017. SemEval-2017 ternRecognition(CVPR).


Sergey Ioffe and Christian Szegedy. 2015. Batch nor- Alec Radford, Jeff Wu, Rewon Child, David Luan,
malization: Accelerating deep network training by DarioAmodei,andIlyaSutskever.2019. Language
reducing internal covariate shift. In Proceedings modelsareunsupervisedmultitasklearners.
| of the | 32nd | International | Conference |     | on  | Interna- |     |     |     |     |     |     |

tionalConferenceonMachineLearning-Volume37, Shauli Ravfogel, Yanai Elazar, Jacob Goldberger, and
ICML’15,page448–456.JMLR.org. Yoav Goldberg. 2020. Unsupervised distillation of
syntacticinformationfromcontextualizedwordrep-
Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, resentations. In Proceedings of the Third Black-
Yiming Yang, and Lei Li. 2020. On the sentence boxNLP Workshop on Analyzing and Interpreting
|     |     |     |     |     |     |     | Neural Networks |     | for NLP, |     |     |     |

embeddings from pre-trained language models. In pages 91–106, Online.
Proceedings of the 2020 Conference on Empirical AssociationforComputationalLinguistics.
MethodsinNaturalLanguageProcessing(EMNLP),
pages9119–9130,Online.AssociationforComputa- EmilyReif,AnnYuan,MartinWattenberg,FernandaB
| tionalLinguistics. |     |     |     |     |     |     | Viegas,AndyCoenen,AdamPearce,andBeenKim. |     |               |     |          |     |

|                    |     |     |     |     |     |     | 2019. Visualizing                        |     | and measuring | the | geometry | of  |
YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man- bert. InAdvancesinNeuralInformationProcessing
|            |              |       |         |           |      |        | Systems,      | volume | 32, pages | 8594–8603. | Curran | As- |

| dar Joshi, | Danqi        | Chen, | Omer    | Levy,     | Mike | Lewis, |               |        |           |            |        |     |
| Luke       | Zettlemoyer, | and   | Veselin | Stoyanov. |      | 2019.  | sociates,Inc. |        |           |            |        |     |
Roberta:ArobustlyoptimizedBERTpretrainingap-
proach. CoRR,abs/1907.11692. Richard Socher, Alex Perelygin, Jean Wu, Jason
|     |     |     |     |     |     |     | Chuang, | ChristopherD.Manning, |     | AndrewNg, |     | and |

Daniel Loureiro, Kiamehr Rezaee, Mohammad Taher Christopher Potts. 2013. Recursive deep models
Pilehvar, and Jose Camacho-Collados. 2021. Anal- forsemanticcompositionalityoverasentimenttree-
|          |            |     |          |        |     |          | bank. In | Proceedings | of the | 2013 | Conference | on  |

| ysis and | Evaluation | of  | Language | Models |     | for Word |          |             |        |      |            |     |
Sense Disambiguation. Computational Linguistics, EmpiricalMethodsinNaturalLanguageProcessing,
| pages1–57. |     |     |     |     |     |     | pages1631–1642,Seattle,Washington,USA.Asso- |     |     |     |     |     |

ciationforComputationalLinguistics.
| Marco Marelli, |     | Stefano | Menini, | Marco | Baroni, | Luisa |     |     |     |     |     |     |

Bentivogli,RaffaellaBernardi,andRobertoZampar- Alex Wang, Amanpreet Singh, Julian Michael, Fe-
|                                       |                                   |     |     |     |            |     | lix Hill, | Omer Levy, | and Samuel |     | Bowman.  | 2018. |

| elli.2014.                            | ASICKcurefortheevaluationofcompo- |     |     |     |            |     |           |            |            |     |          |       |
|                                       |                                   |     |     |     |            |     | GLUE: A   | multi-task | benchmark  | and | analysis | plat- |
| sitionaldistributionalsemanticmodels. |                                   |     |     |     | InProceed- |     |           |            |            |     |          |       |
Pro-
ings of the Ninth International Conference on Lan- form for natural language understanding. In
guageResourcesandEvaluation(LREC’14),pages ceedings of the 2018 EMNLP Workshop Black-
216–223, Reykjavik, Iceland. European Language boxNLP: Analyzing and Interpreting Neural Net-
ResourcesAssociation(ELRA). works for NLP, pages 353–355, Brussels, Belgium.
AssociationforComputationalLinguistics.
| Julian Michael,              |         | Jan A. Botha, |           | and Ian            | Tenney.    | 2020. |                |      |                     |        |       |         |

|                              |         |               |           |                    |            |       | Lingxiao Wang, | Jing | Huang, Kevin        | Huang, | Ziniu | Hu,     |
| Asking                       | without | telling:      | Exploring | latent             | ontologies |       |                |      |                     |        |       |         |
|                              |         |               |           |                    |            |       | GuangtaoWang,  |      | andQuanquanGu.2020. |        |       | Improv- |
| incontextualrepresentations. |         |               |           | InProceedingsofthe |            |       |                |      |                     |        |       |         |
2020 Conference on Empirical Methods in Natural ing neural language generation with spectrum con-
Language Processing (EMNLP), pages 6792–6812, trol. In International Conference on Learning Rep-
resentations.
Online.AssociationforComputationalLinguistics.
AlexWarstadt,AmanpreetSingh,andSamuelR.Bow-
GeorgeA.Miller,ClaudiaLeacock,RandeeTengi,and
|          |          |             |     |             |              |      | man.2019.    | Neuralnetworkacceptabilityjudgments. |             |     |               |     |

| Ross T.  | Bunker.  | 1993.       | A   | semantic    | concordance. |      |              |                                      |             |     |               |     |
|          |          |             |     |             |              |      | Transactions | of the                               | Association | for | Computational |     |
| In Human | Language | Technology: |     | Proceedings |              | of a |              |                                      |             |     |               |     |
Workshop Held at Plainsboro, New Jersey, March Linguistics,7:625–641.
21-24,1993.
| Jiaqi Mu         | and Pramod       | Viswanath.                     |                | 2018.    | All-but-the- |          |     |     |     |     |     |     |

| top: Simple      |                  | and effective                  | postprocessing |          |              | for word |     |     |     |     |     |     |
| representations. |                  | In6thInternationalConferenceon |                |          |              |          |     |     |     |     |     |     |
| Learning         | Representations, |                                | ICLR           | 2018,    | Vancouver,   |          |     |     |     |     |     |     |
| BC, Canada,      |                  | April 30                       | - May          | 3, 2018, | Conference   |          |     |     |     |     |     |     |
TrackProceedings.OpenReview.net.
| Mohammad          | Taher | Pilehvar          |                     | and      | Jose            | Camacho-  |     |     |     |     |     |     |

| Collados.         | 2019. | WiC:              | the word-in-context |          |                 | dataset   |     |     |     |     |     |     |
| for evaluating    |       | context-sensitive |                     | meaning  |                 | represen- |     |     |     |     |     |     |
| tations.          | In    | Proceedings       | of                  | the 2019 | Conference      |           |     |     |     |     |     |     |
| of the            | North | American          | Chapter             | of       | the Association |           |     |     |     |     |     |     |
| for Computational |       | Linguistics:      |                     | Human    |                 | Language  |     |     |     |     |     |     |
| Technologies,     |       | Volume            | 1 (Long             | and      | Short           | Papers),  |     |     |     |     |     |     |
pages1267–1273,Minneapolis,Minnesota.Associ-
ationforComputationalLinguistics.


| A Isotropystatistics                         |     |         |           |       |        | SST-2.              | The Stanford |       | Sentiment |        | Treebank  |     |

|                                              |     |         |           |       |        | (Socher             | et al.,      | 2013) | is a      | binary | sentiment |     |
| Table 5showsisotropystatisticsforGPT-2,BERT, |     |         |           |       |        | classificationtask. |              |       |           |        |           |     |
| and RoBERTa.                                 |     | GPT-2’s | embedding | space | is ex- |                     |              |       |           |        |           |     |
tremelyanisotropicinupperlayers. Hence,more MRPC. TheMicrosoftResearchParaphraseCor-
PCsarerequiredtobeeliminatedtomakethisem- pus(DolanandBrockett,2005)consistsofpaired
sentences,andthegoalisdeterminingwhether,in
| bedding | space isotropic |     | in comparison |     | to BERT |     |     |     |     |     |     |     |

apair,sentencessharesimilarsemanticsornot.
andRoBERTa,bothinthecluster-basedapproach
| and the | global | one (Mu | and Viswanath, |     | 2018). |     |     |     |     |     |     |     |

WiC. Word-in-Context(PilehvarandCamacho-
| Also, in | almost | all layers, | BERT | has | higher a |           |       |             |                |     |     |         |

|          |        |             |      |     |          | Collados, | 2019) | is a binary | classification |     |     | task in |
isotropythanRoBERTa.
whichitshouldbedeterminedifatargetwordin
twodifferentcontextsreferstothesamemeaning.
| Model  | GPT-2   |     | BERT    |     | RoBERTa |            |                                     |           |                |          |          |       |

|        |         |     |         |     |         | BoolQ.     | BooleanQuestions(Clarketal.,2019)is |           |                |          |          |       |
| layer0 | 1.5E-02 |     | 4.6E-04 |     | 9.1E-03 |            |                                     |           |                |          |          |       |
|        |         |     |         |     |         | a Question | Answering                           |           | classification |          | task.    | Every |
| layer1 | 9.9E-24 |     | 9.9E-06 |     | 2.7E-07 |            |                                     |           |                |          |          |       |
|        |         |     |         |     |         | sample     | includes                            | a passage | and            | a yes/no | question |       |
| layer2 | 2.8E-23 |     | 6.3E-05 |     | 8.7E-10 |            |                                     |           |                |          |          |       |
aboutthepassage.
| layer3 | 6.1E-26 |     | 8.8E-05 |     | 4.2E-09 |                    |     |     |     |     |     |     |

| layer4 | 1.6E-27 |     | 9.2E-06 |     | 5.4E-12 |                    |     |     |     |     |     |     |
| layer5 | 3.0E-30 |     | 4.8E-06 |     | 2.4E-10 | B.2 Configurations |     |     |     |     |     |     |
layer6 1.6E-32 3.9E-06 3.1Ef-10 For the classification tasks, we trained a simple
| layer7 | 1.3E-37 |     | 1.1E-07 |     | 1.3E-10 |        |              |           |     |      |       |     |

|        |         |     |         |     |         | MLP on | the features | extracted |     | from | BERT. | The |
| layer8 | 3.4E-45 |     | 1.0E-05 |     | 1.4E-10 |        |              |           |     |      |       |     |
proposedcluster-basedapproachhastwohyperpa-
| layer9 | 6.4E-55 |     | 2.5E-05 |     | 1.3E-10 |     |     |     |     |     |     |     |

layer10 4.1E-32 6.9E-05 6.7E-11 rameters: thenumberofclustersandthenumberof
layer11 1.8E-132 2.4E-07 1.4E-10 PCstoberemoved. Weselectedbothofthemfrom
layer12 5.0E-174 5.0E-05 2.7E-06 range[5,30]andtunedthemontheSTS-Bdevset.
|     |     |     |     |     |     | In the cluster-based |     | approach,The |     |     | optimal | num- |

Table5: Per-layerisotropyontheSTS-Bdevset.Num-
|     |     |     |     |     |     | ber of clusters | for | GPT-2, | BERT, |     | and RoBERTa |     |

bershavebeencalculatedbasedonI(W).
|     |     |     |     |     |     | are respectively |                                 | 10, 27,    | and | 27. For | BERT      | and |

|     |     |     |     |     |     | RoBERTa,         | 12topdominantdirectionshavebeen |            |     |         |           |     |
|     |     |     |     |     |     | removed,         | while                           | the number |     | is 30   | for GPT-2 | re- |
B ExperimentalSetup
gardingitsextremelyanisotropicembeddingspace.
ThetuningofthenumberofPCstobeeliminated
B.1 Datasetdetails
|     |     |     |     |     |     | in the global | method | has | been | done | similarly | to  |

STS. IntheSemanticTextualSimilaritytask,the thecluster-basedapproach(ontheSTS-Bdevset):
providedlabelsarebetween0and5foreachpaired 30, 15, and 25 for GPT-2, BERT, and RoBERTa,
| sentence. | Wefirstcalculatesentenceembeddings |     |     |     |     | respectively. |     |     |     |     |     |     |

byaveragingallwordrepresentationsineachsen-
tence and then compute the cosine similarity be- C IsotropyonSTSdatasets
| tween two | sentence | representations |     | as  | a score of |           |                                  |     |     |     |     |     |

|           |          |                 |     |     |            | InTable6, | wepresenttheisotropyofthecontex- |     |     |     |     |     |
semanticrelatednessofthepair.
|      |                 |     |         |     |            | tual embedding | spaces     |     | calculated |        | using I(W) | on     |

|      |                 |     |         |     |            | the STS        | benchmark. | The | results    | reveal | the        | effec- |
| RTE. | The Recognizing |     | Textual |     | Entailment |                |            |     |            |        |            |        |
tivenessoftheproposedmethodinenhancingthe
| dataset | is a classification |     | task | from | the GLUE |     |     |     |     |     |     |     |

isotropyoftheembeddingspace.
| benchmark(Wangetal.,2018). |      |           |         | Pairedsentences |            |     |     |     |     |     |     |     |

| are collected              | from | different | textual |                 | entailment |     |     |     |     |     |     |     |
D WordfrequencybiasinCWRs
| challenges  | and | labeled | as entailment |     | and not- |                                            |     |     |     |     |     |     |

| entailment. |     |         |               |     |          | CWRsarebiasedtowardstheirfrequencyinforma- |     |     |     |     |     |     |
tion,andwordswithsimilarfrequencycreatelocal
CoLA. The Corpus of Linguistic Acceptability regionsintheembeddingspace(Gongetal.,2018;
(Warstadtetal.,2019)isabinaryclassificationtask Lietal.,2020). Fromthesemanticpointofview,
in which sentences are labeled whether they are thisiscertainlyundesirablegiventhatwordswith
grammaticallyacceptable. similarmeaningsbutdifferentfrequenciescouldbe


| Model | STS2012 | STS2013 | STS2014 |     | STS2015 | STS2016 | SICK-R | STS-B |

Baseline
GPT-2 1.4E-178 1.0E-170 1.4E-172 2.9E-177 6.0E-174 9.9E-140 2.6E-105
| BERT | 3.1E-05 | 1.9E-04 | 2.6E-04 |     | 3.7E-07 | 2.8E-04 | 4.2E-05 | 1.1E-04 |

RoBERTa 3.1E-06 3.1E-07 3.8E-06 3.8E-06 3.5E-06 3.7E-07 2.9E-06
Globalapproach
| GPT-2   | 0.57 | 0.40 | 0.05 |     | 0.12 | 0.60 | 0.57 | 0.51 |

| BERT    | 0.48 | 0.41 | 0.55 |     | 0.72 | 0.65 | 0.63 | 0.58 |
| RoBERTa | 0.67 | 0.87 | 0.87 |     | 0.84 | 0.85 | 0.90 | 0.88 |
Cluster-basedapproach
| GPT-2   | 0.71 | 0.74 | 0.47 |     | 0.74 | 0.74 | 0.78 | 0.70 |

| BERT    | 0.68 | 0.61 | 0.77 |     | 0.81 | 0.75 | 0.82 | 0.73 |
| RoBERTa | 0.89 | 0.91 | 0.93 |     | 0.92 | 0.89 | 0.94 | 0.90 |
Table 6: Isotropy of CWRs on multiple STS datasets calculated based on I(W); a higher value indicates a more
isotropicembeddingspace. Ourcluster-basedmethodsignificantlyincreasestheisotropyofembeddingspaceon
alldatasets.
locatedfarfromeachotherintheembeddingspace.
| This phenomenon   | can | be seen      | in Figure | 5. The |     |     |     |     |

| encoded knowledge |     | in the local | dominant  | direc- |     |     |     |     |
tionspartlycorrespondtofrequencyinformation.
Theembeddingspacevisualizationrevealsthatour
| approach performs | a   | decent | job in removing | fre- |     |     |     |     |

quencybiasinpre-trainedmodels.


(a) GPT-2-Baseline (b) GPT-2-Globalapproach (c) GPT-2-Cluster-basedapproach
(d) BERT-Baseline (e) BERT-Globalapproach (f) BERT-Cluster-basedapproach
(g) RoBERTa-Baseline (h) RoBERTa-Globalapproach (i) RoBERTa-Cluster-basedapproach
Figure 5: Contextual Word Representations visualization using PCA on STS-B dev set. Colors indicate word
frequencyintheWikipediadump(thelighterpoint,themorefrequent).

---
**Source PDF:** `2022_12_article.pdf`
