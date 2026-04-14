|     |     |     | Object |     | Detection | Meets | Knowledge |     | Graphs |     |     |     |     |     |

YuanFang,KingsleyKuan,JieLin,ChestonTan and VijayChandrasekhar
InstituteforInfocommResearch,A*STAR,Singapore
yfang@i2r.a-star.edu.sg,kingsley.kuan@gmail.com,flin-j,cheston-tan,vijayg@i2r.a-star.edu.sg
|        |           |     | Abstract |              |     |         | (a)Detectingcatandtable |     |     |     | (b)Detectingbear |     |     |     |

| Object | detection | in  | images   | is a crucial |     | task in |                         |     |     |     |                  |     |     |     |
computervision,withimportantapplicationsrang-
| ing      | from security                              | surveillance |            | to autonomous   |              | ve-     |     |     |     |     |     |     |     |     |

| hicles.  | Existingstate-of-the-artalgorithms,includ- |              |            |                 |              |         |     |     |     |     |     |     |     |     |
| ing      | deep neural                                | networks,    |            | only focus      | on utilizing |         |     |     |     |     |     |     |     |     |
| features | within                                     | an image     |            | itself, largely | neglecting   |         |     |     |     |     |     |     |     |     |
| the      | vast amount                                | of           | background | knowledge       |              | about   |     |     |     |     |     |     |     |     |
| the real | world.                                     | In this      | paper,     | we propose      |              | a novel |     |     |     |     |     |     |     |     |
framework of knowledge-aware object detection, Figure1:ObjectdetectiononimagesfromMSCOCO15.
| which | enables | the | integration | of external |     | knowl- |     |     |     |     |     |     |     |     |

edgesuchasknowledgegraphsintoanyobjectde-
tectionalgorithm. Theframeworkemploystheno- Recent advances in deep convolutional neural networks
|     |     |     |     |     |     |     | [Sermanet | et al., | 2013; | Girshick | et  | al., 2014], | in particular |     |

tionofsemanticconsistencytoquantifyandgener-
|       |            |       |          |        |           |     | Fast or    | Faster  | R-CNN | [Girshick, | 2015;      | Ren      | et al., | 2015],    |

| alize | knowledge, | which | improves | object | detection |     |            |         |       |            |            |          |         |           |
|       |            |       |          |        |           |     | show great | promise | in    | object     | detection. | However, |         | like pre- |
throughare-optimizationprocesstoachievebetter
consistency with background knowledge. Finally, vious approaches, these methods only account for patterns
empirical evaluation on two benchmark datasets present in the training images, without leveraging much of
|      |      |              |     |               |          |     | theknowledgeanaveragepersonwouldhave. |     |     |     |     |     | Forexample, |     |

| show | that | our approach | can | significantly | increase |     |                                       |     |     |     |     |     |             |     |
humanshavethecommonsenseorimplicitknowledgethata
| recall | by up | to 6.3 | points | without | compromising |     |     |     |     |     |     |     |     |     |

domesticcatsometimessitsonatable,butabeardoesnot
| mean | average | precision, |     | when compared |     | to the |     |     |     |     |     |     |     |     |

barringveryrarecircumstances.Thisbackgroundknowledge
state-of-the-artbaseline.
wouldnatruallyhelpreinforcethesimultaneousdetectionsof
catandtable(e.g.inFigure1a),evenifnoneofthetrain-
## 1 Introduction ing images portrays a cat together with a table. On the
otherhand,ifanimageispredictedtocontainbothbearand
| Many computer |     | vision tasks | ultimately | seek | to  | interpret the |     |     |     |     |     |     |     |     |

table,whichconflictswithourbackgroundknowledge,the
| worldthroughimagesandvideos. |     |     |     | Whilesignificantprogress |     |     |     |     |     |     |     |     |     |     |

hasbeenmadeinthepastdecade,therestillexistsastriking detectionsaremorepronetobefalse.
|                                      |          |             |     |           |                  |     | While     | such         | background | knowledge |      | appears   | random   | and |

| gapbetweenhowhumansandmachineslearn. |          |             |     |           | Althoughcur-     |     |           |              |            |           |      |           |          |     |
|                                      |          |             |     |           |                  |     | difficult | to organize, | there      | have      | been | extensive | research | and |
| rent machine                         | learning | approaches, |     | including | state-of-the-art |     |           |              |            |           |      |           |          |     |
commercialeffortstoencodeitintomachinereadableforms
| deep learning | algorithms, |     | can | effectively | find patterns | from |     |     |     |     |     |            |        |     |

|               |             |     |     |             |               |      |     |     |     |     |     | [Paulheim, | 2017]. |     |
the training data, they fail to leverage what an average per- often known as knowledge graphs A
son has at his or her disposal—the vast amount of back- knowledgegraphisagraphthatmodelssemanticknowledge,
whereeachnodeisareal-worldconcept,andeachedgerep-
| ground knowledge |     | about | the real | world. | Given | that images |         |                |     |         |               |     |     |           |

|                  |     |       |          |        |       |             | resents | a relationship |     | between | two concepts. |     | For | instance, |
andvideosarereflectionsoftheworld,exploitingbackground
|           |     |                   |     |           |         |        | Figure2showcasesatoyknowledgegraph. |      |      |           |            |     | Inparticular,the |     |

| knowledge | can | have a tremendous |     | advantage | towards | inter- |                                     |      |      |           |            |     |                  |     |
|           |     |                   |     |           |         |        | relationship                        | “cat | sits | on table” | reinforces |     | the detections   |     |
pretingthesedata.
|     |     |     |     |     |     |     | of cat | and table | in  | Figure | 1a. We | note | that knowledge |     |

Taskandinsight graphsalreadydemonstrateconsiderablesuccessinotherdo-
Inthispaper,westudythekeycomputervisiontaskofobject mainssuchasWebsearchandsocialnetworks[Dongetal.,
detection[Everinghametal.,2010].Givenanimage,thegoal 2014]. Beyondatoygraph,large-scaleknowledgegraphsare
istoidentifyasetofregionsorboundingboxes,andtofurther often constructed through crowdsourcing or automated ex-
classifyeachboundingboxwithoneofthepre-definedobject traction from semi-structured and unstructured data, which
| labels,asillustratedinFigure1. |     |     |     |     |     |     | arebeyondthescopeofthispaper. |     |     |     |     |     |     |     |

1661


|     |     |        | hunts |     |      |     |     | 2 RelatedWork  |     |                                       |     |     |     |     |     |

|     |     | person |       |     | bear |     |     |                |     |                                       |     |     |     |     |     |
|     |     |        |       |     |      |     |     | Inrecentyears, |     | deepconvolutionalneuralnetworks(CNNs) |     |     |     |     |     |
havebecomethede-factobaselineforcomputervisiontasks
|     |     |     |     |     |     |     |     | such as | image | classification |     | and object | detection. |     | Their |

cat
|     | house |     |     |     |     |     |     | strongperformancestemsfromtheabilitytolearnhigh-level |     |     |     |     |     |     |     |

tree
|     |     |     |     |     |     |     |     | image features |       | [Krizhevsky | et      | al., 2012; | Simonyan |             | and Zis- |

|     |     |     |     |     |     |     |     | serman,        | 2014; | Szegedy     | et al., | 2015;      | He et    | al., 2016]. | For      |
objectdetection,earlierresearchsuchasRegionswithCNN
placed on
table plate features (R-CNN) [Girshick et al., 2014] and its fast vari-
|     |     |     |     |     |     |     |     | [Girshick, |     | 2015]   |     |      |             |          |     |

|     |     |     |     |     |     |     |     | ant        |     | employs |     | CNNs | to classify | objects, | but |
Figure2:Atoyknowledgegraphmodelingsevenconceptsasnodes depends on precomputed region proposals for object local-
(e.g.,catandtable),aswellastheirrelationshipsasedges(e.g.,
|     |     |     |     |     |     |     |     | ization. | Subsequently, |     | networkssuchasOverfeat[Sermanet |     |     |     |     |

“catsitsontable”).
|     |     |     |     |     |     |     |     | et al., 2013] | and | Faster | R-CNN | [Ren | et al., | 2015] | leverages |

CNNsfornotonlyobjectclassificationbutalsoobjectlocal-
Challengesandapproach ization. FasterR-CNNinparticularintroducesaregionpro-
|     |     |     |     |     |     |     |     | posal network |     | that efficiently |     | shares | convolutional |     | features |

Evenwithanexistingknowledgegraph,toeffectivelylever-
|         |           |         |     |        |            |     |       | forbothregionproposalandclassification. |     |             |      |     |        | Furthermore,us- |          |

| age the | knowledge | therein | for | object | detection, | two | major |                                         |     |             |      |     |        |                 |          |
|         |           |         |     |        |            |     |       | ing contextual                          |     | information | from | the | entire | image           | has also |
technicalchallengesstillremain.
|     |     |     |     |     |     |     |     | been explored |     | to improve | object | detection, |     | by generating | a   |

First, how do we quantify and generalize knowledge? contextfeaturetoenhancetheclassificationofindividualre-
Quantificationisnecessaryasknowledgegraphsentailsym-
gions[Belletal.,2016].
bolicrepresentationsbutmostobjectdetectionalgorithmsop-
Thereisalsoanemergingtrendtoexploitinformationout-
| erate over | subsymbolic    |     | or numerical | representations. |          |        | More- |                |     |                          |     |     |                 |     |     |

|            |                |     |              |                  |          |        |       | sideof images, |     | i.e., externalbackground |     |     | knowledgesuchas |     |     |
| over, the  | quantification |     | shall not    | only             | apply to | images | with  |                |     |                          |     |     |                 |     |     |
textsandknowledgegraphs,forcertaincomputervisiontasks
contextsmatchingdirectlyobservedknowledge,butalsogen-
suchasimageclassification[Dengetal.,2014],visualmoti-
| eralizetoimageswithnewcontexts. |     |     |     | Inourapproach,forev- |     |     |     |     |     |     |     |     |     |     |     |

vationprediction[Vondricketal.,2016],visualquestionan-
| ery pair  | of concepts | on          | the knowledge |     | graph, | we compute | a       |                 |        |                                       |     |        |              |     |            |

|           |             |             |               |     |        |            |         | swering         | [Wu et | al., 2016]                            | and | visual | relationship |     | extraction |
| numerical | degree      | of semantic | consistency   |     | for    | them.      | For ex- |                 |        |                                       |     |        |              |     |            |
|           |             |             |               |     |        |            |         | [Luetal.,2016]. |        | However,todate,usingexternalknowledge |     |        |              |     |            |
ample,sincetherelationship“catsitsontable”ispresent
hasreceivedlimitedattentionforthetaskofobjectdetection.
|                                           |              |         | cat | table   |             |              |     |          |        |             |       |               |            |               |        |

| on the knowledge                          |              | graph,  |     | and     | are         | semantically |     |          |        |             |       |               |            |               |        |
|                                           |              |         |     |         |             |              |     | An early | work   | [Rabinovich |       | et al., 2007] | introduces |               | a con- |
| consistentconcepts,butbearandtablearenot. |              |         |     |         |             | Concepts     |     |          |        |             |       |               |            |               |        |
|                                           |              |         |     |         |             |              |     | ditional | random | field       | model | to maximize   |            | the agreement | of     |
| can also                                  | be connected | through |     | a chain | of indirect | relation-    |     |          |        |             |       |               |            |               |        |
labelsandsemanticcontextsfromtheirowntrainingdata,as
| ships, such | as   | “cat licks | plate” | and            | “plate | placed     | on  |                |     |          |         |          |        |        |           |

|             |      |            |        |                |        |            |     | well as from   | an  | external | online  | service  | called | Google | Sets1     |
| table”.     | This | gives rise | to the | generalization |        | ability—we |     |                |     |          |         |          |        |        |           |
|             |      |            |        |                |        |            |     | which returned |     | a set of | similar | concepts | based  | on     | a few in- |
caninferthatcatandtabletendtoappeartogetherwith-
Onerecentwork[Hongetal.,2017]usesco-
putexamples.
outdirectlyobserving“catsitsontable”.
|                                        |     |       |             |          |              |             |     | occurrence  | statistics                               | to  | re-weight | the      | detection | scores | in in-   |

| Second,                                | how | do we | incorporate | semantic |              | consistency | to  |             |                                          |     |           |          |           |        |          |
|                                        |     |       |             |          |              |             |     | doorscenes. | Notethatbothmethodscannotgeneralizetoim- |     |           |          |           |        |          |
| achieveknowledge-awareobjectdetection? |     |       |             |          | Wehingeonthe |             |     |             |                                          |     |           |          |           |        |          |
|                                        |     |       |             |          |              |             |     | ages with   | contexts                                 | not | observed  | in their | training  | or     | external |
keyconstraintthatmoresemanticallyconsistentconceptsare
data,whileourknowledgegraph-basedapproachhasabetter
morelikelytooccurinanimagewithcomparableprobability.
generalizationpotential.
Forinstance,letting(o,p)denoteaboundingboxcontaining
|          |      |             |          |      |           |         |     | Finally, | background |     | knowledge | can | often | be organized | as  |

| object o | with | probability | p, it is | more | plausible | to have | two |          |            |     |           |     |       |              |     |
aknowledgegraph,whichisadatastructurecapableofmod-
| bounding                            | boxes | (cat, | 0.8) and | (table, | 0.9)             | in the | same |                                                  |     |     |     |     |     |     |        |

|                                     |       |       |          |         |                  |        |      | elingbothreal-worldconceptsandtheirinteractions. |     |     |     |     |     |     | Theuse |
| image,than(bear,0.8)and(table,0.9). |       |       |          |         | Inparticular,for |        |      |                                                  |     |     |     |     |     |     |        |
thelatter,itismorelikelytohave(bear,0.8)and(table, of knowledge graphs have become widespread and largely
|          |        |       |             |     |               |     |         | successful | in many | data-driven |     | applications |         | including | Web    |

| 0.01) or | (bear, | 0.01) | and (table, |     | 0.9) instead. |     | We cast |            |         |             |     |              |         |           |        |
|          |        |       |             |     |               |     |         | search and | social  | networks    |     | [Dong        | et al., | 2014].    | Numer- |
suchaconstraintasanoptimizationproblem.
ousresearchandcommercialeffortshavebeenspenttocon-
structlarge-scaleknowledgegraphs[Paulheim,2017],which
Contribution
We make three major contributions in this paper. First, we often require continuous expansion and refinement. Typi-
advocate incorporating knowledge into object detection, an cally, knowledge graphs are constructed through human cu-
emerging paradigm still limited in visual tasks. Second, we ration [Lenat, 1995], crowdsourced contribution [Liu and
|           |                   |     |           |     |      |            |     | Singh, 2004], |     | as well | as automatic |     | extraction | from | semi- |

| formulate | a knowledge-aware |     | framework |     | that | quantifies | se- |               |     |         |              |     |            |      |       |
structured[Suchaneketal.,2007]orunstructureddata[Fang
| mantic | consistency | based | on knowledge |     | graphs | in a | gener- |     |     |     |     |     |     |     |     |

2011].
alizablemanner,andfurtherre-optimizesobjectdetectionto and Chang, More recently, knowledge has also been
achievebetterconsistency. Last,weconductextensiveexper- systematicallyharvestedfrommultimodaldataincludingim-
iments on two benchmark datasets, which significantly im- ages[Krishnaetal.,2017].
provesrecallbyupto6.3pointswhilekeepingthesamelevel
| ofmeanaverageprecision. |     |     |     |     |     |     |     | 1Theproductwasdiscontinuedin2011. |     |     |     |     |     |     |     |

1662


| 3 ProposedApproach |     |     |     |     |     |     |     | Training images |     | Existing model |     | Test image |     |     |     |

(e.g., Faster R-CNN)
Wedescribeourknowledge-awareframeworkinthissection,
| starting | with the | notations | and | problem | statement, |     | followed |     |     |     |     |     |     |     |     |

bythenotionofsemanticconsistency,aswellastheintegra-
tionofknowledgeintoobjectdetection.
### 3.1 NotationsandProblem
|     |     |     |     |     |     |     |     |     |     |     |                      | 0.6 | 0.4 |                                | 0.4 0.6 |

|     |     |     |     |     |     |     |     |     |     |     | (cid:1842)(cid:3404) |     |     | (cid:1842)(cid:3552)(cid:3404) |         |
Consider a set of pre-defined concepts or object labels L = 0.2 0.8 0.1 0.9
semantic
f1;2;:::;Lg.2 Weassumeanexistingobjectdetectionalgo- consistency Existing
Knowledge-
|            |         |             |             |     |        |               |          | Knowledge |     |     | model output |     |     | aware output |     |

| rithm that | outputs | a set       | of bounding | box | B      | = f1;2;:::;Bg |          |           |     |     |              |     |     |              |     |
| for each   | image,  | and assigns | a label     | ‘   | 2 L to | each          | bounding |           |     |     |              |     |     |              |     |
Figure3:Overviewofknowledge-awareframework.
| box b 2 | B with | probability | p(‘jb). |     | For each | image, | these |     |     |     |     |     |     |     |     |

probabilitiescanbeencodedbyaB(cid:2)LmatrixP,suchthat
P =p(‘jb). independently, or they co-occur less frequently than if they
b;‘
weretooccurindependently,thevaluewouldbezero;other-
| Our goal | is  | to produce | a new | matrix | Pb based | on  | not only |     |     |     |     |     |     |     |     |

the initial matrix P, but also the semantic consistency be- wise,thevalueispositive. Inparticular,themorelikelytwo
tweenconceptswhicharederivedfromgivenknowledge. In concepts co-occur than if they were independent, the more
|                                                |                |     |                             |     |     |     |     | positivethevalue,boundedbylogN |     |           |          | fromtheabove. |          |     |     |

| otherwords,Pbisaknowledge-awareenhancementofP. |                |     |                             |     |     |     | Ul- |                                |     |           |          |               |          |     |     |
|                                                |                |     |                             |     |     |     |     |                                |     |           | (cid:18) | n(‘;‘0)N      | (cid:19) |     |     |
| timately,                                      | thenewmatrixPb |     | enablesustoimproveobjectde- |     |     |     |     |                                |     |           |          |               |          |     |     |
|                                                |                |     |                             |     |     |     |     |                                | S   | ‘;‘0 =max | log      |               | ;0       |     | (1) |
tection, such that a bounding box b is assigned a potentially n(‘)n(‘0)
| newlabel‘b=argmax |     |     | Pbb;‘ . Theoverallframeworkissum- |     |     |     |     |     |     |     |     |     |     |     |     |

‘
WhileitisstraightforwardtocomputeEq.(1),thereistwo
marizedinFig.3.
|     |     |     |     |     |     |     |     | major drawbacks. |     | First, | collecting | enough | background |     | data |

### 3.2 SemanticConsistency withhigh-qualityannotationsisoftendifficultandexpensive,
|                                             |     |            |     |          |     |             |          | especially | when    | the baseline     | detection |          | model | is given | as a    |

| Knowledgeisfundamentallysymbolicandlogical. |     |            |     |          |     |             | However, |            |         |                  |           |          |       |          |         |
|                                             |     |            |     |          |     |             |          | blackbox   | without | its accompanying |           | training |       | data.    | Second, |
| most state-of-the-art                       |     | algorithms |     | function | on  | subsymbolic | or       |            |         |                  |           |          |       |          |         |
theresultingmatrixS
numericalrepresentations.Thus,towardsaknowledge-aware onlyworksforknownco-occurrences
inthebackgrounddata,butdoesnotgeneralizetounseenco-
framework,thefirststepistoquantifysuchknowledge,espe-
|           |          |      |                |     |           |      |       | occurrences | in  | new images. | In  | other | words, if | two | concepts |

| cially in | a manner | that | can generalize |     | to images | with | unob- |             |     |             |     |       |           |     |          |
neverco-occurinthebackgrounddata,theirsemanticconsis-
servedcontexts.Tothisend,weproposetomeasureanumer-
tencywouldbeexactlyzero,andthusarenothelpfultonew
icaldegreeofsemanticconsistencyforeachpairofconcepts.
imagescontainingthesetwoconcepts.
Ahighdegreeofsemanticconsistencybetweentwoconcepts
impliesthatthetwoconceptsarelikelytoappeartogetherin Graph-basedknowledge
thesameimage. Next,weconsideraknowledgegraphformodelingsemantic
Formally, let S be an L(cid:2)L matrix such that S is de- consistency.UnlikethetoyexampleinFigure2,atypicaloff-
‘;‘0
finedasthedegreeofsemanticconsistencybetweenconcepts
the-shelfknowledgegraphoftencapturesatleastmillionsof
| ‘and‘0,8(‘;‘0) |     | 2 L2. | Naturally,S | shallbesymmetric,i.e., |     |     |     |     |     |     |     |     |     |     |     |

conceptsandtheircomplexrelationships,providingimmense
‘0,S
S ‘;‘0 = S ‘0;‘ . Notethat,when‘ = ‘;‘0 capturestheself- backgroundknowledgeexternaltotheimages.
consistency,whichismeaningfulsincemultipleinstancesof Using a large-scale knowledge graph has a significant
thesameconceptcanappearinthesameimage. advantage—itcanbettergeneralizetoapairofconceptseven
| In other | words, | additional | background |     | knowledge |     | about |     |     |     |     |     |     |     |     |

iftheyarenotconnectedbyanyedge.Inparticular,whentwo
| various | concepts | can be | quantified | and | modeled | by  | the ma- |     |     |     |     |     |     |     |     |

conceptsarenotinvolvedinadirectrelationship,potentially
trixS.
Inthefollowing,wedescribetwoalternativesofcon- wecanstillestablishachainofrelationshipsbetweenthem.
structingSfromadditionalknowledge:oneusingsimplefre- Forinstance,peopleandplateinFigure2arenotdirectly
quency,andtheotherbasedonaknowledgegraph. connected. This does not necessarily mean that they are not
Frequency-basedknowledge semantically consistent. Quite the contrary, they should en-
To compute semantic consistency, one immediate approach joy a fair degree of semantic consistency based on common
|     |     |     |     |     |     |     |     | sense. | Nonetheless, | despite | a   | missing | edge | between | them, |

istoutilizethefrequencyofco-occurrencesforeachpairof
thereisstillachainofedges“personpetscat”and“cat
| concepts.  | Such  | co-occurrences |        | can be      | identified | from        | given |              |         |              |      |          |              |        |           |

|            |       |                |        |             |            |             |       | licks plate” |         | to indicate  | that | they are | semantically |        | consis-   |
| background | data, | which          | can be | potentially |            | multi-modal | in-   |              |         |              |      |          |              |        |           |
|            |       |                |        |             |            |             |       | tent to some | extent. | Furthermore, |      | multiple |              | direct | relation- |
cludingtextcorporaandphotocollections.
Let n(‘;‘0) denote the frequency of co-occurrences for ships or chains of relationships can exist between two con-
|          |       | ‘0,    |              |     |                |     |           | cepts. In    | Figure | 2, cat          | and table |     | can be  | related  | through |

| concepts | ‘ and | and    | n(‘) denote  | the | frequency      |     | of ‘. Let |              |        |                 |           |     |         |          |         |
|          |       |        |              |     |                |     |           | the edge     | “cat   | sits on table”, |           | and | a chain | of edges | “cat    |
| N be the | total | number | of instances | in  | the background |     | data.     |              |        |                 |           |     |         |          |         |
|          |       |        |              |     |                |     |           | licks plate” |        | and “plate      | placed    | on  | table”. | Each     | rela-   |
Then,wedefinesemanticconsistencybelow,basedonpoint-
|             |              |     |        |      |      |       |          | tionshiporchainiscalledapathfromcattotable. |     |     |     |     |     |     | Dif- |

| wise mutual | information. |     | Simply | put, | when | ‘ and | ‘0 occur |                                             |     |     |     |     |     |     |      |
ferentpathsbetweenthetwoconceptscomplementeachother
2Inthispaper,weuse“concept”and“label”interchangeably. forincreasedrobustness.
1663


To quantify semantic consistency on a knowledge graph, existing algorithm, and fPbb;‘ : b 2 B;‘ 2 Lg represent our
we employ random walk with restart [Tong et al., 2006]. proposedknowledge-awaredetections.
Startingfromanodev onthegraph, wemovetoarandom
0 B B L L
neighboring node of v , and record it as v . Once at v , we XXXX (cid:16) (cid:17)2
repeatthisprocess.Ing

eneral,whenweare

atv ,wemo

veto
E(Pb)=(1(cid:0)(cid:15)) S
‘;‘0
Pbb;‘ (cid:0)Pbb0;‘0
t
one of its neighbors randomly, and denote the new node we b=1b0=1‘=1‘0=1
b06=b
havejustarrivedasv . Inaddition,toavoidbeingtrapped
t+1
B L
inasmalllocality,ateachmove,thereisaprobabilityof(cid:11)to XX (cid:16) (cid:17)2
restarttherandomwalkby“teleporting”tothestartingnode
+(cid:15) BkS
‘;(cid:3)
k

Pbb;‘ (cid:0)P
b;‘
(4)
v , instead of moving to one of the neighbors. Formally, a b=1‘=1

random walk is a sequence of nodes hv ;v ;v :::;v i, and On the one hand, the first term of Eq. (4) captures the
0 1 2 t
p(v = ‘0jv = ‘;(cid:11)) represents the probability of reaching constraint on the semantic consistency. For a pair of de-
t 0
theconcept‘0intstepsgiventhatwestartfrom‘. tected bounding boxes b and b0, if S is large, minimizing
‘;‘0
Thisprobabilitycanbeusedtoformulatesemanticconsis- theobjectivefunctionwouldforceP andP tobecome
b;‘ b0;‘0
tency, suchthatalargerprobabilityfrom‘to‘0 impliesthat smaller; if S is small, P and P are less constrained
‘;‘0 b;‘ b0;‘0
they are more semantically consistent. Intuitively, when the andcanbecomeverydifferent.
numberofpathsfrom‘to‘0 increasesorthelengthofthese On the other hand, the second term requires that
paths decreases, the semantic consistency between ‘ and ‘0 knowledge-awaredetectionsshouldnotdeparttoomuchfrom
becomeslarger,sodoestheprobabilityofreaching‘0from‘. detections of existing algorithms. Existing algorithms use
Interestingly,aswetakelongerrandomwalks,thisprobabil- features specific to each image which form the basis of our
ityeventuallyconvergestoauniquesteadystateasfollows. knowledge-aware approach. Note that the squared error has
a coefficient BkS k in order to balance different con-
R = lim p(r =‘0jr =‘;(cid:11)): (2) ‘;(cid:3) 1
‘;‘0 t 0 cepts. Without this coefficient, the cost function would give
t!1
more importance to the first term over summations involv-
NotethatR ‘;‘0 isnotsymmetricingeneral.Thus,inEq.(3) ing P
b;‘
;8b 2 B when kS
‘;(cid:3)
k is larger. The overall trade-
wedefineasymmetricmatrixSbasedonthegeometricmean.
offbetweenthetwotermsiscontrolledbyahyperparameter
Thegeometricmeanhasaroundtriprandomwalkinterpreta- (cid:15)2(0;1),whichcanbeselectedonavalidationset.
tion, and has been shown to be superior than the arithmetic
orharmonicmeans[Fangetal.,2013]. ThematrixS canbe Optimization
efficiently computed even on a very large knowledge graph To minimize Eq. (4), we find its stationary point where its
[Zhuetal.,2013]. gradientw.r.t.Pbb;‘ iszero,8b2B;‘2L.
p
S =S = R R (3) B L
‘;‘0 ‘0;‘ ‘;‘0 ‘0;‘ @E(Pb) X X (cid:16) (cid:17)
/(1(cid:0)(cid:15)) S
‘;‘0
Pbb;‘ (cid:0)Pbb0;‘0
One caveat is the huge effort required to build and refine @Pbb;‘
b0=1‘0=1
a large-scale knowledge graph, which is an active research b06=b
area itself. Fortunately, a suite of off-the-shelf solutions are (cid:16) (cid:17)
available, manyofwhichofferopendatasetsorAPIs. Fora
+(cid:15)BkS
‘;(cid:3)
k

Pbb;‘ (cid:0)P
b;‘
(5)
thorough discussion on this matter, we refer the reader to a
Setting the above to zero, we obtain below an equivalent
survey paper [Paulheim, 2017] and the citations therein. In
ourexperiments,weadoptMITConceptNet[LiuandSingh, configurationoveroptimalPbb;‘ .

m

i

ll

io
],
n
a
co
c
n
r
c
o
e
w
p
d
ts
so
a
u
n
r
d
ce

d
m
k
i
n
ll
o
io
w
n
le
r
d
e
g
la
e
tio
g
n
ra
s
p
h
h
ip
w
s.
ith more than 4
Pbb;‘ =(1(cid:0)(cid:15))
PB
b
P
0=
B
1;b06=b
PL
‘
P
0=
L

S
‘;
S
‘0
Pbb0;‘0
+(cid:15)P
b;‘
(6)
### 3.3 Knowledge-AwareRe-optimization
b0=1;b06=b ‘0=1 ‘;‘0
ItcanbeshownthattheexactsolutiontoEq.(6)isthelimit
Given a matrix that quantifies the semantic consistency be-
of the series in Eq. (7) for i 2 f1;2;:::g. In particular, for
tween pairwise concepts, we need to further integrate it
withanexistingmodeltoenableknowledge-awaredetection anyarbitraryinitializationPb b ( ; 0 ‘ ),Pb b ( ; i ‘ )alwaysconvergestothe
through a re-optimization process. In the following, we for- samesolutionasi!1.
m
fu
u
rt
l
h
a
e
te
rd
a
is
c
c
o
u
s
s
t
s
f
i
u
ts
nc
e
t
f
i
fi
o
c
n
ie
b
n
a
t
s
o
e
p
d
ti
o
m
n
iz
s
a
e
t
m
io
a
n
n
.
tic consistency, and
Pb
b
(
;
i
‘
) =(1(cid:0)(cid:15))
PB
b
P
0=1
B
;b06=b
PL
‘
P
0=1
L
S
‘;‘
S

Pb
b
(

i
;
(cid:0)
‘0
1)
+(cid:15)P
b;‘
(7)
Costfunction b0=1;b06=b ‘0=1 ‘;‘0
The key intuition is that two concepts with a higher degree Notethatthesolutioncanbecomputedinpolynomialtime.
ofsemanticconsistencyaremorelikelytoappearinthesame ThetheoreticalcomplexityisO(B2L2I),whereIisthenum-
imagewithcomparableprobability. Thatis,fortwodifferent berofiterations. Convergencetypicallyhappensveryfastin
boundingboxesbandb0 inoneimage,P andP should fewerthan30iterations.Tofurtherspeedupthecomputation,
b;‘ b0;‘0
notbetoodifferentwhenS islarge.Thisconstraintcanbe wecouldapplyanapproximationusingB nearestbounding
‘;‘0 k
formalizedbyminimizingthecostfunctioninEq.(4),where boxes and L nearest concepts. That is, a pair of bounding
k
fP : b 2 B;‘ 2 Lg represent the detections from any boxesbandb0 areconsideredonlyifeitherofthemisamong
b;‘
1664


| theB boundingboxeswithsmallestdistancestotheother;a |     |     |     |     |     |     |     |     |     |     |     |     | #Images |     |

k
pairofconcepts‘and‘0areconsideredonlyifeitherofthem Dataset #Concepts training validation test
|          |       |          |      |         |          |             |     | MSCOCO15 |     | 80  |     | 80K | 40K | 40K |

| is among | the L | k labels | with | largest | semantic | consistency | to  |          |     |     |     |     |     |     |
theother. Thus,thepracticalcomplexityisonlyO(BL),as- PASCAL07 20 2.5K 2.5K 5.0K
| sumingthatI;B |     | ;L  | aresmallconstants. |     |     |     |     |     |     |     |     |     |     |     |

k k
Table1:Summarystatisticsofbenchmarkdatasets.
## 4 Evaluation
|                    |     |                                   |     |          |     |          |        |     | mAP  |      | Recall | Recall@100byarea |        |       |

| We empirically     |     | evaluate                          | the | proposed |     | approach | on two |     |      |      |        |                  |        |       |
|                    |     |                                   |     |          |     |          |        |     | @100 | @100 | @10    | small            | medium | large |
| benchmarkdatasets. |     | Resultsofourknowledge-awaredetec- |     |          |     |          |        |     |      |      |        |                  |        |       |
minival-4k
| tion is | promising, | significantly |             | outperforming |          |       | the baseline |        |      |      |      |      |      |      |

|         |            |               |             |               |          |       |              |        | 24.5 | 35.9 | 35.2 | 14.2 | 41.5 | 55.6 |
| method  | in recall  | while         | maintaining |               | the same | level | of mean      | FRCNN  |      |      |      |      |      |      |
|         |            |               |             |               |          |       |              | KF-500 | 24.4 | 37.1 | 35.6 | 14.3 | 42.8 | 57.3 |
averageprecision.
|                       |     |     |     |     |     |     |     | KF-All  | 24.5 | 37.9 | 36.2 | 14.6 | 43.9 | 58.6 |

| 4.1 Experimentalsetup |     |     |     |     |     |     |     | KG-CNet | 24.4 | 38.9 | 36.6 | 14.4 | 45.2 | 60.0 |
test-dev
Datasets
|     |     |     |     |     |     |     |     |     | 24.2 | 34.6 | 34.0 | 12.0 | 38.5 | 54.4 |

FRCNN
| We use   | benchmark   | data | MSCOCO15 |             | [Lin       | et al., | 2014] and |        |      |      |      |      |      |      |

|          |             |      |          |             |            |         |           | KF-500 | 24.3 | 37.4 | 35.9 | 13.7 | 42.1 | 58.0 |
| PASCAL07 | [Everingham |      | et       | al., 2010], | summarized |         | in Ta-    |        |      |      |      |      |      |      |
|          |             |      |          |             |            |         |           | KF-All | 24.3 | 38.2 | 36.4 | 14.2 | 43.0 | 59.2 |
ble1.ForMSCOCO15,wecombinetheirtrainingandvalida-
|     |     |     |     |     |     |     |     | KG-CNet | 24.2 | 39.2 | 36.9 | 14.5 | 44.0 | 60.7 |

tionsetsfortrainingthebaseline,exceptforasubsetof5000
test-std
| imagesnamed“minival”.                       |                                          |       | Wefurthersplitminivalinto1000 |         |              |              |             |          |            |      |                     |      |          |          |

|                                             |                                          |       |                               |         |              |              |             | FRCNN    | 24.2       | 34.7 | 34.1                | 11.5 | 38.9     | 54.4     |
| and 4000                                    | images,                                  | named | “minival-1k”                  |         | and          | “minival-4k” | re-         |          |            |      |                     |      |          |          |
|                                             |                                          |       |                               |         |              |              |             | KG-CNet  | 24.1       | 39.2 | 37.0                | 14.2 | 44.4     | 60.5     |
| spectively.                                 | Weuseminival-1ktochoosehyperparameterfor |       |                               |         |              |              |             |          |            |      |                     |      |          |          |
| ourapproach,andminival-4kforofflinetesting. |                                          |       |                               |         |              |              | Onlineeval- |          |            |      |                     |      |          |          |
|                                             |                                          |       |                               |         |              |              |             | Table 2: | Comparison | of   | our knowledge-aware |      | variants | with the |
| uation on                                   | the MSCOCO15                             |       |                               | server3 | is performed |              | on the test |          |            |      |                     |      |          |          |
baselinemethodonMSCOCO15.
| set, since | its ground | truth | is  | not publicly |     | available. | The test |     |     |     |     |     |     |     |

setcontainstwosubsetsofroughlyequalsize,namely“test-
dev” and “test-std”, where the latter only allows for limited demonstrate that the accuracy of the results depend on the
submissions. For PASCAL07, we use their training set for qualityofthebackgrounddata,weconsiderasecondvariant
trainingthebaseline,validationsetforchoosingourhyperpa- namedKF-500,bysamplingonly500imagesfromthetrain-
ingsetsasthebackgrounddata.
rameter,andtestsetforevaluation.
|     |     |     |     |     |     |     |     | On the | other | hand, for | the | graph-based | knowledge, | we  |

Modeltraining
|           |     |                  |     |        |       |     |        | employ                     | MIT ConceptNet |     | 55 as                       | our knowledge |     | graph. We |

| We employ | the | state-of-the-art |     | Faster | R-CNN | and | VGG-16 |                            |                |     |                             |               |     |           |
|           |     |                  |     |        |       |     |        | onlyuseitsEnglishsubgraph, |                |     | andfilterout“negative”rela- |               |     |           |
[Simonyan
as the baseline and Zisserman, 2014; Ren et al., tionships (NotDesires, NotHasProperty, NotCapableOf, No-
2015], using the public Python Caffe implementation4. We tUsedFor, Antonym, DistinctFrom and ObstructedBy) and
| callthisbaselineFRCNNhereafter. |     |     |     |     | Modelsaretrainedusing |     |     |             |                                           |     |     |     |     |     |

|                                 |     |     |     |     |                       |     |     | self-loops. | Theresultinggraphhas1.3millionconceptsand |     |     |     |     |     |
stochasticgradientdescentwithamomentumof0.9,amini-
|                                    |     |     |     |     |     |                 |     | 2.8 million            | relationships. |                                     | We  | set the | random | walk restart- |

| batchsizeof2andaweightdecayof5e-4. |     |     |     |     |     | Layerweightsare |     |                        |                |                                     |     |         |        |               |
|                                    |     |     |     |     |     |                 |     | ingprobability(cid:11) |                | = 0:15,atypicalvalueknowntobestable |     |         |        |               |
initialized from a VGG-16 model pre-trained on ImageNet. [Fangetal.,2013]. WecallthisvariantKG-CNet.
| New layers | defined    | by  | Faster       | R-CNN | are    | randomly | initial-  |                 |     |     |     |     |     |     |

| ized from  | a Gaussian |     | distribution |       | with a | standard | deviation | Accuracymetrics |     |     |     |     |     |     |
of0.01. Weusealearningrateof1e-3forthefirst350K/50K
Themainmetricsaremeanaverageprecision(mAP)andre-
iterationsonMSCOCO15/PASCAL07,followedby1e-4for
|     |     |     |     |     |     |     |     | call at top | 100. | On MSCOCO15, |     | we  | also report | recall at |

another140K/10Kiterations.
|     |     |     |     |     |     |     |     | top 10 and | by object | areas | (small, | medium | and | large); on |

For our knowledge-aware approach, we re-optimize the PASCAL07, we further report recall by concepts. In partic-
| output | of FRCNN. |     | We  | only retain | top | 500 | bounding |     |     |     |     |     |     |     |

ular,aboundingboxisjudgedcorrectonlyifitsintersection
| boxes whose |     | scores | are at | least | 1e-5. | On  | the valida- |     |     |     |     |     |     |     |

overunion(IoU)w.r.t.thegroundtruthisabovesomethresh-
| tion data, | we choose |     | the hyperparameter |     |     | (cid:15) in Eq. | (4) from |     |     |     |     |     |     |     |

old. WeusetheIoUthresholdasstandardizedineachbench-
| f0:1;0:25;0:5;0:75;0:9g. |     |     | To  | speed | up the | computation | of  |          |           |     |              |      |        |            |

|                          |     |     |     |       |        |             |     | mark: On | MSCOCO15, |     | it is varied | over | f0.50, | 0.55, ..., |
Eq. (7), we only consider 5 nearest neighbors for both the 0.95gandtheiraverageresultsarereported;forPASCAL07,
| boundingboxesandlabelsasanapproximation. |     |     |     |                         |     |     | Theupdates | itisfixedat0.5. |     |     |     |     |     |     |

| areperformedfor10iterations,             |     |     |     | whichalreadyshowconver- |     |     |            |                 |     |     |     |     |     |     |
gence. Wecompareseveralvariantsofourapproach.
### 4.2 Mainresults
| On the | one | hand, we | adopt | frequency-based |     |     | knowledge, |                                       |     |     |     |     |     |            |

|        |     |          |       |                 |     |     |            | WereporttheresultsonMSCOCO15inTable2. |     |     |     |     |     | BothKF-All |
combiningthetrainingsetsofbothbenchmarksastheback-
andKG-CNetsignificantlyincreaserecall@100overthebase-
| ground | data. We | name | this | variant | KF-All. | Furthermore, | to  |     |     |     |     |     |     |     |

linemethodFRCNNbyupto3.6and4.6points,respectively.
3http://mscoco.org/home/
4https://github.com/rbgirshick/py-faster-rcnn 5http://conceptnet-api-1.media.mit.edu/
1665


Recall@100byconcepts
|     |     |     |      |      |      | elttob |     |         |             |     | nosrep      |             |       |     |

|     |     |     |      |      |      |        |     |         | riahc elbat |     | esroh ekibm | tnalp peehs | niart |     |
|     |     |     | orea | ekib | drib | taob   |     |         |             |     |             |             | afos  |     |
|     | mAP |     |      |      |      |        | sub | rac tac | woc         | god |             |             |       |     |
vt
@100 lla
FRCNN 66.5 81.9 76.1 89.0 74.3 73.4 64.6 89.7 85.8 90.5 69.0 88.9 85.4 91.6 92.0 85.2 82.4 60.8 83.1 89.1 84.4 82.1
KF-500 66.6 83.8 80.0 91.7 79.1 76.0 67.0 89.7 88.8 92.5 69.7 92.6 85.9 90.8 94.0 86.8 82.0 59.6 87.2 90.0 89.7 82.8
KF-All 66.5 84.6 80.7 93.5 79.1 76.0 67.6 90.1 88.8 93.6 68.1 93.0 86.9 94.1 93.1 89.5 83.1 65.4 88.0 89.1 90.1 81.8
KG-CNet 66.6 85.0 80.4 92.3 78.6 76.0 67.6 90.1 89.1 92.2 74.2 93.0 86.4 93.0 92.2 88.6 87.7 66.9 87.6 90.4 89.7 83.4
Table3:Comparisonofourknowledge-awarevariantswiththebaselinemethodonPASCAL07.
|     |     |     |     |     |     |     |     |     | (a) Office scene: |     | (left) fails | to detect | keyboard, | but |

Other recall metrics, at top 10 and by areas, also show sig- FRCNN
KG-CNet(right)doesduetothepresenceoflaptop.
| nificant | improvement |     | up  | to 4.8 | and 6.3 | points, | respectively. |     |     |     |     |     |     |     |

Atthesametime,bothapproachesdonotcompromisemAP.
Moreover,comparingwithKF-All,KF-500attainssmallerim-
| provements |     | across | all recall | metrics, | which | is  | not surprising |     |     |     |     |     |     |     |

givenfewerbackgrounddata.
| Next,     | we   | present | the | results | on PASCAL07 |            | in  | Table 3. |     |     |     |     |     |     |

| Likewise, | both | KF-All  | and | KG-CNet |             | beat FRCNN |     | in re-   |     |     |     |     |     |     |
call@100by2.7and3.1points,respectively,withoutaffect-
ingmAP.Inparticular,KF-Alloutperformsthebaselinein17
| out of                   | the 20 | concepts, |     | whereas                    | KG-CNet | outperforms |     | the |                  |                                    |     |     |     |     |

|                          |        |           |     |                            |         |             |     |     | (b)Outdoorscene: | FRCNN(left)failstodetectsurfboard, |     |     |     | but |
| baselineinall20concepts. |        |           |     | Asusual,KF-500showssmaller |         |             |     |     |                  |                                    |     |     |     |     |
KG-CNet(right)doesduetothepresenceofperson.
improvementsthanKF-Allinmostcases.
| Note | that |     | generates |     | consistently |     | better | results |     |     |     |     |     |     |

KG-CNet
| than KF-All  |        | on MSCOCO15, |             | but    | to          | a much            | lesser         | extent |     |     |     |     |     |     |

| on PASCAL07. |        | We           | hypothesize |        | that        | the discrepancies |                | are    |     |     |     |     |     |     |
| caused       | by the | complexity   |             | of the | benchmarks. |                   | In particular, |        |     |     |     |     |     |     |
MSCOCO15aremorecomplexthanPASCAL07[Linetal.,
| 2014]:        | The | former      | contains | an         | average    | of 3.5      | concepts | and    |     |     |     |     |     |     |

| 7.7 instances |     | per image,  |          | whereas    | the latter | has         | fewer    | than 2 |     |     |     |     |     |     |
| concepts      | and | 3 instances |          | per image. |            | The simpler | scenes   | in     |     |     |     |     |     |     |
PASCAL07 would thus require less generalization, and the Figure 4: Two scenes from MSCOCO15 (best viewed in color).
frequency-basedvariantcouldbenefitfromthissituation. In each scene, the left image contains the output of the baseline
We also observe that both KF-All and KG-CNet deliver methodFRCNN,whereastherightimagecontainstheoutputofour
|           |             |              |     |          |             |     |        |         | proposed KG-CNet.  | Ground-truth |        | objects are | marked with | orange  |

| more      | significant | improvements |     |          | on MSCOCO15 |     |        | than on |                    |              |        |             |             |         |
|           |             |              |     |          |             |     |        |         | boxes, and correct | detections   | of IoU | at least    | 0.75 in top | 100 are |
| PASCAL07. |             | We believe   |     | that the | underlying  |     | reason | is sim- |                    |              |        |             |             |         |
markedwithblueboxes.
| ilar in | that the | knowledge-aware |     |     | variants | are | able to | benefit |     |     |     |     |     |     |

morefromthesemanticallyricherscenesinMSCOCO15.
| 4.3      | Casestudy |          |     |         |     |               |     |        | 5 Conclusion |     |     |     |     |     |

| Finally, | we        | showcase | the | ability | of  | the knowledge |     | graph- |              |     |     |     |     |     |
basedvariantindetectingadditionalobjectsandthusimprov-
ingrecall,onrealimagesfromMSCOCO15. In this paper, we study the problem of object detection in a
TheexampleinFigure4adepictsanofficescene,contain- novel knowledge-aware framework. Compared to existing
|     |     |     |     | keyboard |     | laptop, |     |     |     |     |     |     |     |     |

ing ground truth objects and among algorithms which only focus on features within an image,
others. Although the baseline misses the keyboard, it is we propose to leverage external knowledge such as knowl-
picked up by KG-CNet after re-optimization. The reason is edge graphs. Towards this goal, we derive and quantify se-
thattheprobabilityofkeyboardispromotedgiventhepres- manticconsistencyfromknowledgegraphsthatcangeneral-
enceoflaptop,sincethetwoconceptsshareveryhighse- ize to new images with unobserved contexts. Next, we in-
manticconsistency(135timesofthemedianvalueamongall tegrate knowledge into existing object detection algorithms,
pairwiseconcepts). Ofcourse, otherequipmentlikemouse byre-optimizingthedetectionstoattainbettersemanticcon-
mayalsohavecontributed. sistency. Finally, we demonstrate the superior performance
Another example in Figure 4b depicts an outdoor scene of our proposed approach through extensive experiments on
withgroundtruthobjectspersonandsurfboard. Like- twobenchmarkdatasets. Asfuturework,weplantoexplore
wise, thebaselinefailstodetectsurfboard, butKG-CNet or construct knowledge graphs that are specifically tailored
identifiesitcorrectly. Inparticular,thetwoconceptsarealso tovisualtasks,insteadofusingageneral-purposeknowledge
semanticallyconsistent(5timesofthemedianvalue). graphwithoutemphasizingonvisualrelationships.
1666


| References              |     |            |                    |          |          |           |        | Dolla´r,andC.LawrenceZitnick. |     |                            |     | MicrosoftCOCO:com- |     |     |

|                         |     |            |                    |          |          |           |        | monobjectsincontext.          |     | InECCV,PartV,pages740–755, |     |                    |     |     |
| [Belletal.,2016]        |     | Sean Bell, | C.                 | Lawrence | Zitnick, |           | Kavita |                               |     |                            |     |                    |     |     |
| Bala,andRossB.Girshick. |     |            | Inside-outsidenet: |          |          | Detecting |        | 2014.                         |     |                            |     |                    |     |     |
[LiuandSingh,2004]
objects in context with skip pooling and recurrent neural Hugo Liu and Push Singh.
networks. InCVPR,pages2874–2883,2016. ConceptNet—a practical commonsense reasoning
[Dengetal.,2014] tool-kit. BTTechnologyJournal,22(4):211–226,2004.
|     |     | Jia Deng, | Nan | Ding, | Yangqing | Jia, | An- |     |     |     |     |     |     |     |

dreaFrome,KevinMurphy,SamyBengio,YuanLi,Hart- [Luetal.,2016] Cewu Lu, Ranjay Krishna, Michael S.
mutNeven,andHartwigAdam. Large-scaleobjectclassi- Bernstein, and Fei-Fei Li. Visual relationship detection
ficationusinglabelrelationgraphs.InECCV,PartI,pages with language priors. In ECCV, Part I, pages 852–869,
48–64,2014.
2016.
| [Dongetal.,2014] |     | Xin | Dong, | Evgeniy |     | Gabrilovich, |     | [Paulheim,2017] |     |                |     |                       |     |     |

|                  |     |     |       |         |     |              |     |                 |     | HeikoPaulheim. |     | Knowledgegraphrefine- |     |     |
Geremy Heitz, Wilko Horn, Ni Lao, Kevin Murphy, ment:Asurveyofapproachesandevaluationmethods.Se-
Thomas Strohmann, Shaohua Sun, and Wei Zhang. manticWeb,8(3):489–508,2017.
| Knowledge        | vault: | a Web-scale              |     | approach | to  | probabilistic |     |                        |          |               |     |             |           |        |

|                  |        |                          |     |          |     |               |     | [Rabinovichetal.,2007] |          | Andrew        |     | Rabinovich, |           | Andrea |
| knowledgefusion. |        | InKDD,pages601–610,2014. |     |          |     |               |     |                        |          |               |     |             |           |        |
|                  |        |                          |     |          |     |               |     | Vedaldi,               | Carolina | Galleguillos, |     | Eric        | Wiewiora, | and    |
[Everinghametal.,2010] Mark Everingham, Luc J. Van Serge J. Belongie. Objects in context. In ICCV, pages
| Gool,           | Christopher | K.                       | I. Williams, |     | John M. | Winn,  | and     | 1–8,2007.       |      |              |            |     |            |           |

| Andrew          | Zisserman.  | The                      | PASCAL       |     | visual  | object | classes |                 |      |              |            |     |            |           |
|                 |             |                          |              |     |         |        |         | [Renetal.,2015] |      | ShaoqingRen, | KaimingHe, |     | RossB.Gir- |           |
| (VOC)challenge. |             | IJCV,88(2):303–338,2010. |              |     |         |        |         |                 |      |              |            |     |            |           |
|                 |             |                          |              |     |         |        |         | shick, and      | Jian | Sun. Faster  | R-CNN:     |     | towards    | real-time |
[FangandChang,2011]
Yuan Fang and Kevin Chen-Chuan objectdetectionwithregionproposalnetworks. InNIPS,
Chang. Searchingpatternsforrelationextractionoverthe pages91–99,2015.
| web:rediscoveringthepattern-relationduality. |     |     |     |     |     | InWSDM, |     |                      |     |        |           |     |       |            |

|                                              |     |     |     |     |     |         |     | [Sermanetetal.,2013] |     | Pierre | Sermanet, |     | David | Eigen, Xi- |
pages825–834,2011.
|     |     |     |     |     |     |     |     | ang Zhang, | Michae¨l | Mathieu, |     | Rob Fergus, |     | and Yann |

[Fangetal.,2013] Yuan Fang, Kevin Chen-Chuan Chang, LeCun. Overfeat: Integrated recognition, localization
| andHadyWirawanLauw. |     |     | RoundTripRank: |     |     | Graph-based |     |               |     |                     |     |           |     |       |

|                     |     |     |                |     |     |             |     | and detection |     | using convolutional |     | networks. |     | CoRR, |
proximitywithimportanceandspecificity.InICDE,pages
arXiv:1312.6229,2013.
613–624,2013.
|     |     |     |     |     |     |     |     | [SimonyanandZisserman,2014] |     |     | Karen | Simonyan |     | and An- |

[Girshicketal.,2014]
Ross B. Girshick, Jeff Donahue, drew Zisserman. Very deep convolutional networks for
Trevor Darrell, and Jitendra Malik. Rich feature hierar- large-scale image recognition. CoRR, arXiv:1409.1556,
| chies for       | accurate                  | object  | detection |      | and semantic | segmen- |       | 2014.                |         |         |       |           |         |          |

| tation.         | InCVPR,pages580–587,2014. |         |           |      |              |         |       |                      |         |         |       |           |         |          |
|                 |                           |         |           |      |              |         |       | [Suchaneketal.,2007] |         | Fabian  | M.    | Suchanek, | Gjergji | Kas-     |
| [Girshick,2015] |                           | Ross B. | Girshick. | Fast | R-CNN.       | In      | ICCV, |                      |         |         |       |           |         |          |
|                 |                           |         |           |      |              |         |       | neci, and            | Gerhard | Weikum. | YAGO: | a         | core of | semantic |
pages1440–1448,2015.
|                |     |         |     |         |        |          |     | knowledge.          | InWWW,pages697–706,2007. |                                  |     |     |     |     |

| [Heetal.,2016] |     | Kaiming | He, | Xiangyu | Zhang, | Shaoqing |     |                     |                          |                                  |     |     |     |     |
|                |     |         |     |         |        |          |     | [Szegedyetal.,2015] |                          | ChristianSzegedy,WeiLiu,Yangqing |     |     |     |     |
Ren,andJianSun.Deepresiduallearningforimagerecog-
|     |     |     |     |     |     |     |     | Jia, Pierre | Sermanet, | Scott | E. Reed, | Dragomir |     | Anguelov, |

nition. InCVPR,pages770–778,2016. Dumitru Erhan, Vincent Vanhoucke, and Andrew Rabi-
[Hongetal.,2017] Jongkwang Hong, Yongwon Hong, novich. Goingdeeperwithconvolutions. InCVPR,pages
1–9,2015.
| Youngjung | Uh, | and Hyeran |     | Byun. | Discovering |     | over- |     |     |     |     |     |     |     |

lookedobjects:Context-basedboostingofobjectdetection [Tongetal.,2006] HanghangTong, ChristosFaloutsos, and
| inindoorscenes. |     | PatternRecogn.Lett.,86:56–61,2017. |     |     |     |     |     |            |                                         |     |     |     |     |     |

|                 |     |                                    |     |     |     |     |     | Jia-YuPan. | Fastrandomwalkwithrestartanditsapplica- |     |     |     |     |     |
[Krishnaetal.,2017] Ranjay Krishna, Yuke Zhu, Oliver tions. InICDM,pages613–622,2006.
| Groth,    | Justin | Johnson, | Kenji       | Hata, | Joshua | Kravitz,  |     |                      |     |                   |           |            |             |       |

|           |        |          |             |       |        |           |     | [Vondricketal.,2016] |     | Carl              | Vondrick, | Deniz      | Oktay,      | Hamed |
| Stephanie | Chen,  | Yannis   | Kalantidis, |       | Li-Jia | Li, David | A.  |                      |     |                   |           |            |             |       |
|           |        |          |             |       |        |           |     | Pirsiavash,          | and | Antonio Torralba. |           | Predicting | motivations |       |
Shamma, Michael S. Bernstein, and Li Fei-Fei. Visual ofactionsbyleveragingtext. InCVPR,pages2997–3005,
| genome:                       | Connecting |            | language | and                  | vision         | using      | crowd- | 2016.          |           |             |          |             |     |           |

| sourceddenseimageannotations. |            |            |          | IJCV,123:32–73,2017. |                |            |        |                |           |             |          |             |     |           |
|                               |            |            |          |                      |                |            |        | [Wuetal.,2016] |           | Qi Wu, Peng | Wang,    | Chunhua     |     | Shen, An- |
| [Krizhevskyetal.,2012]        |            |            | Alex     | Krizhevsky,          | Ilya           | Sutskever, |        |                |           |             |          |             |     |           |
|                               |            |            |          |                      |                |            |        | thony R.       | Dick,     | and Anton   | van      | den Hengel. |     | Ask me    |
| and Geoffrey                  |            | E. Hinton. | ImageNet |                      | classification |            | with   |                |           |             |          |             |     |           |
|                               |            |            |          |                      |                |            |        | anything:      | Free-form | visual      | question | answering   |     | based on  |
deepconvolutionalneuralnetworks.InNIPS,pages1106–
|     |     |     |     |     |     |     |     | knowledgefromexternalsources. |     |     |     | InCVPR,pages4622– |     |     |

1114,2012.
4630,2016.
| [Lenat,1995] | Douglas | B.  | Lenat. | CYC: | A   | large-scale | in- |                 |     |             |      |       |       |       |

|              |         |     |        |      |     |             |     | [Zhuetal.,2013] |     | Fanwei Zhu, | Yuan | Fang, | Kevin | Chen- |
vestment in knowledge infrastructure. Commun. ACM, Chuan Chang, and Jing Ying. Incremental and accuracy-
38(11):32–38,1995.
|                 |       |                                     |         |     |               |     |       | aware personalized               |     | pagerank | through | scheduled |     | approxi- |

| [Linetal.,2014] |       | Tsung-YiLin,MichaelMaire,SergeJ.Be- |         |     |               |     |       |                                  |     |          |         |           |     |          |
|                 |       |                                     |         |     |               |     |       | mation. PVLDB,6(6):481–492,2013. |     |          |         |           |     |          |
| longie,         | James | Hays, Pietro                        | Perona, |     | Deva Ramanan, |     | Piotr |                                  |     |          |         |           |     |          |
1667

---
**Source PDF:** `2023_04_article.pdf`
