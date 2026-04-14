Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation
EmilyDinan∗,AngelaFan∗†,AdinaWilliams,JackUrbanek,DouweKiela,JasonWeston
FacebookAIResearch
†LaboratoireLorraind’InformatiqueetApplications(LORIA)
|        |           | Abstract |                 |     |       |      | Genderedwordcountsindialoguedatasets |     |     |             |     |           |     |

|        |           |          |                 |     |       |      | Dataset                              |     |     | %gend.words |     | %malebias |     |
| Social | biases    | present  | in data         | are | often | di-  |                                      |     |     |             |     |           |     |
|        |           |          |                 |     |       |      | LIGHT                                |     |     | 0.94        |     | 73.4      |     |
| rectly | reflected | in       | the predictions |     | of    | mod- |                                      |     |     |             |     |           |     |
|        |           |          |                 |     |       |      | Reddit                               |     |     | 1.32        |     | 69.76     |     |
els trained on that data. We analyze gender WizardofWikipedia 0.076 65.9
bias in dialogue data, and examine how this DailyDialog 1.02 59.04
|         |               |             |            |        |           |     | EmpatheticDialogues |     |     | 2.07 |     | 53.45 |     |

| bias is | not only      | replicated, |            | but    | is also   | am- |                     |     |     |      |     |       |     |
|         |               |             |            |        |           |     | ConvAI2             |     |     | 1.28 |     | 50.05 |     |
| plified | in subsequent |             | generative |        | chit-chat | di- |                     |     |     |      |     |       |     |
| alogue  | models.       | We          | measure    | gender | bias      | in  |                     |     |     |      |     |       |     |
six existing dialogue datasets before select- Table 1: Counts of gendered words in several di-
ingthemostbiasedone,themulti-playertext- alogue datasets. We report the percent of gendered
based fantasy adventure dataset LIGHT (Ur- words (% gend. words) as well as the percentage of
banek et al., 2019), as a testbed for bias mit- male-gendered words out of all gendered words (%
| igation | techniques. |     | We consider |     | three | tech- |             |          |     |          |     |            |       |

|         |             |     |             |     |       |       | male bias). | Datasets | are | arranged | in  | descending | order |
niquestomitigategenderbias: counterfactual with respect to % male bias. LIGHT has the most %
data augmentation, targeted data collection, malebias;thuswechoseitasourmaintestbed.
| andbiascontrolledtraining. |            |     |          | Weshowthatour |      |     |     |     |     |     |     |     |     |

| proposed                   | techniques |     | mitigate | gender        | bias | by  |     |     |     |     |     |     |     |
balancing the genderedness of generated dia- coreference resolution (Zhao et al., 2018a). Al-
logueutterances,andfindthattheyarepartic- thoughresearchintobiasinNLPwritlargeisma-
| ularly | effective | in combination. |     |     | We evaluate |     |              |     |          |            |     |     |          |

|        |           |                 |     |     |             |     | turing, bias | in  | dialogue | utterances |     | has | received |
modelperformancewithavarietyofquantita-
|                        |                 |            |        |             |      |      | somewhat        | less      | attention    | (Liu | et al.,     | 2019; | Sheng    |

| tive methods—including |                 |            | the    | quantity    | of   | gen- |                 |           |              |      |             |       |          |
|                        |                 |            |        |             |      |      | et al., 2019;   | Henderson |              | et   | al., 2018). |       | As real- |
| dered                  | words,          | a dialogue | safety | classifier, |      | and  |                 |           |              |      |             |       |          |
|                        |                 |            |        |             |      |      | world use-cases |           | for dialogue |      | agents,     | such  | as in-   |
| human                  | assessments—all |            | of     | which       | show | that |                 |           |              |      |             |       |          |
ourmodelsgeneratelessgendered,butequally teractiveassistants,arerapidlydeveloping,biasin
engagingchit-chatresponses. dialogue models has the very real potential to in-
vadedownstreamsystemsandexacerbateexisting
## 1 Introduction
|                |             |            |           |          |          |          | social biases.      | Thus,         | dialogue  |             | debiasing |         | is becom-  |

|                |             |            |           |          |          |          | ing an increasingly |               | important |             | problem   |         | in NLP. In |
| Machine        | learning    | algorithms |           | learn    | to model | pat-     |                     |               |           |             |           |         |            |
|                |             |            |           |          |          |          | this work,          | we foreground |           | dataset     |           | bias as | a crucial  |
| terns present  | in          | training   | datasets. |          | In       | particu- |                     |               |           |             |           |         |            |
|                |             |            |           |          |          |          | cause of            | gender        | bias      | in dialogue |           | models, | and ex-    |
| lar, they make | predictions |            | that      | directly | reflect  | the      |                     |               |           |             |           |         |            |
plorewaystoaddressit.
harmfulsocietalbiasespresentintrainingdatasets,
|     |     |     |     |     |     |     | Gender | bias | has been | found | in  | many | machine |

suchasracialbiasinsportsreports(Merulloetal.,
|             |           |      |         |         |      |         | learning      | datasets, | in   | both images |          | and text | (Stock   |

| 2019) and   | political | bias | in news | data    | (Fan | et al., |               |           |      |             |          |          |          |
|             |           |      |         |         |      |         | and Cisse´,   | 2017;     | Zhao | et al.,     | 2017).   | Here,    | we an-   |
| 2019). Such | biases    | are  | rife    | in NLP, | for  | exam-   |               |           |      |             |          |          |          |
|             |           |      |         |         |      |         | alyze several | existing  |      | dialogue    | datasets |          | for gen- |
ple,inlearnedwordembeddings(Bolukbasietal.,
derbias(seeTable1,and§3formorediscussion)
| 2016; Brunet     | et   | al., 2018; | Zhao | et      | al., 2019), | vi-    |                 |                                   |            |           |        |         |          |

|                  |      |            |      |         |             |        | for the purpose |                                   | of finding |           | a good | testbed | for a    |
| sual semantic    | role | labeling   |      | (Zhao   | et al.,     | 2017), |                 |                                   |            |           |        |         |          |
|                  |      |            |      |         |             |        | deeperdive.     | Ouranalysisrevealedthatthedataset |            |           |        |         |          |
| natural language |      | inference  | (He  | et al., | 2019),      | abu-   |                 |                                   |            |           |        |         |          |
|                  |      |            |      |         |             |        | from the        | LIGHT                             | text       | adventure |        | world   | (Urbanek |
sivelanguageclassification(Parketal.,2018),and
|     |     |     |     |     |     |     | et al., 2019) | was | the | most | biased | in our | sample. |

∗Jointfirstauthors. LIGHT is also an interesting dataset for measur-
8173
Proceedingsofthe2020ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages8173–8188,
November16–20,2020.(cid:13)c2020AssociationforComputationalLinguistics

PersonaExample(OriginalLIGHTDataset)
daughter: Ispendmostofmytimedoinghouseholdchores.Iwanttofindmeaninginlife.Iamenergeticandhappy.
chiefwife: Iamtheking’schiefwife. Ofallthewomenthathehasmarried, orwhoarehisconcubines, Iamthe
principalone. Irepresentthekingdomofmyfather,whoistheking’sbiggestally. Mysonsaretheones
whowillmostlikelybecomethekingafterthedeathofmyhusband.
women: Ilivewithmyhusbandand4childreninthevillage. Ispendmydayswashingclothingandcleaningour
home.Myhusbandworksfortheroyalarmydefendingouttown.
farmerBob’swife: IamfarmerBob’swife.Iliketotakecareofallouranimals.IhelpFarmerBobeverydayonthefarm.
mother: Iamamotherofeightchildren. Ilivewithmyfamilyinacottageinthecountryside. Ispendeveryday
tendingtotheneedsofallofmylittleoneswhichcanbeoverwhelming,butIalwaysmanagetomaintain
apleasingdispositionandahappysmile.
wife: Iamthewifeofafarmer.WhileImaynotbethemostattractivewomanever,Iamloyalandloving.My
husbandisagoodman,butonlyseemstostaywithmeoutofduty.
Table2: ExamplesofgenderbiasedpersonasinLIGHT.Inareviewthatweconductedinthiswork(section3),
noneofthesecharacterswereflaggedassexistoroffensive. Formaleexamples,seeAppendixTable11.
DialogueExample(OriginalLIGHTDataset) one of which is wholly novel, and another which
wife: Iwasmarriedoffbymyfamilyaboutfiveyearsago. is novel in its application to dialogue: (i) Coun-
Ispendmydayscookingandcleaningsomyhusbandwill terfactualDataAugmentation(CDA)(HallMaud-
havesomethingtoeatwhenhereturnsfromhisworkand
|     |     |     |     | slay et | al., 2019; | Zmigrod | et  | al., 2019), | (ii) a tar- |

canenjoyacleanhome.Ilovemyhusbanddearlybecause
heworksveryhardtoprovideforus. geteddatacollectionmethod,whichwerefertoas
|           |                            |     |     | Positive-Bias | Data | collection, |     | and (iii) | Bias Con- |

| merchant: | Whatagreatdayformoremoney. |     |     |               |      |             |     |           |           |
wife: Ohmy.Thatissomethickdust! trolled text generation. We show that these tech-
| merchant: | Indeed,itisveryold.                    |     |     |                 |          | effective |              |              |         |

|           |                                        |     |     | niques          | are most |           | in           | combination, | result- |
| wife:     | Thisroomisgoingtotakeawhiletoclean.You |     |     |                 |          |           |              |              |         |
|           |                                        |     |     | ing in dialogue |          | models    | that produce | engaging     | re-     |
mightwanttocomebacklater.
merchant: ItisfineIcansetmyboothuphere. sponses with measurably less gender bias and of-
| wife:     | Withallthefoottraffic? |     |     |         |         |           |        |          |         |

|           |                        |     |     | fensive | content | (see §5). | Models | and code | are re- |
| merchant: | Yesitshouldbeok.       |     |     |         |         |           |        |          |         |
wife: It doesn’t appear that anyone ever comes up leased at https://parl.ai/projects/genderation_
|           | here!                                   |     |     | bias/.        |                                |     |     |     |     |

| merchant: | WelltheywillwhentheyknowIamhere.        |     |     |               |                                |     |     |     |     |
| wife:     | IhavemydoubtsbutI’lljustgoaboutmyclean- |     |     |               |                                |     |     |     |     |
|           | ing.                                    |     |     | 2 RelatedWork |                                |     |     |     |     |
| merchant: | Yeasoundslikeagoodidea.                 |     |     |               |                                |     |     |     |     |
| wife:     | Whatisthatsupposedtomean?               |     |     |               |                                |     |     |     |     |
|           |                                         |     |     | Recently,     | theNLPcommunityhasfocusedonex- |     |     |     |     |
| merchant: | Iamsayingweshouldbothdoourjobs.         |     |     |               |                                |     |     |     |     |
wife: Don’ttakethattonewithme! ploring gender bias in NLP systems (Sun et al.,
|     |     |     |     | 2019), | uncovering | many | gender | disparities | and |

Table 3: A crowdsourced persona and dialogue from harmful biases in algorithms and text (Cao and
theoriginalLIGHTdataset.
|     |     |     |     | Daume´ | III 2020; | Chang | et al. | 2019; | Chang and |

McKeown2019;Costa-jussa`2019;Duetal.2019;
|     |     |     |     | Emami | et al. 2019; | Garimella |     | et al. | 2019; Gaut |

ingandmitigatinggenderbiasforthreeadditional etal.2020;Habashetal.2019;Hashempour2019;
| reasons: | first, it has | multiple potential | sources | of       |           |     |        |        |            |

|          |               |                    |         | Hoyle et | al. 2019; | Lee | et al. | 2019a; | Lepp 2019; |
bias—not just dialogues, but also characters and Qian2019;Qianetal.2019;Sharifiradetal.2019;
personas—second, it was crowdsourced, and thus Sharifirad and Matwin 2019; Stanovsky et al.
| susceptible | to reflecting | the gender | biases known |              |       |          |     |              |        |

|             |               |            |              | 2019; O’Neil | 2016; | Blodgett |     | et al. 2020; | Nangia |
tobepresentincrowdworkers’annotations(Otter-
|     |     |     |     | et al. 2020). | Particular |     | attention | has | been paid |

bacheretal.,2018;BarbosaandChen,2019),and to uncovering, analyzing, and removing gender
third,LIGHT’smedieval,fantasysettingmighten- biases in word embeddings (Basta et al., 2019;
| courage       | crowdworkers | to impart | text with | their                       |                |     |       |                |            |

|               |              |           |           | Kaneko                      | and Bollegala, |     | 2019; | Zhao et        | al., 2019, |
| genderbiases. |              |           |           | 2018b;Bolukbasietal.,2016). |                |     |       | Thiswordembed- |            |
After selecting LIGHT for particular scrutiny, dingworkhasevenextendedtomultilingualwork
we then explore three bias mitigation techniques, on gender-marking (Gonen et al., 2019; Williams
8174

et al., 2019; Zhou et al., 2019; Williams et al., Wikipedia, Daily Dialog, Empathetic Dialogues,
efforts,
2020). Despite these many methods for and ConvAI2). We use this to calculate the per-
debiasingembeddingshaveonlysucceededinhid- centage of gendered words out of all words, and
ing word embedding biases as opposed to remov- the % male bias, that is the percentage of male
ing them (Gonen and Goldberg, 2019)—making gendered words among all gendered words in a
genderdebiasingstillanopenareaofresearch. dialogue. We find that LIGHT is the most gen-
|     |     |     |     |     |     |     | der imbalanced |     | dataset | among | all | datasets | in this |

Despitetherelativelyampleliteratureongender
debiasing for word-level representations, very lit- table,witha%malebiasof73%,althoughothers,
tle work has focused on sentence representations likeReddit,areclosebehind.
| (Liang et             | al., | 2020; Liu    | et                     | al., 2019; | Sheng | et al., |          |                  |        |            |       |          |          |

|                       |      |              |                        |            |       |         | Since    | LIGHT            | was    | found      | to be | the most | gender   |
| 2019;Leeetal.,2019b). |      |              | Untilthispoint,mostde- |            |       |         |          |                  |        |            |       |          |          |
|                       |      |              |                        |            |       |         | biased,  | we qualitatively |        | examine    |       | it more  | closely, |
| biasing               | work | on sentences |                        | mainly     | focus | on mea- |          |                  |        |            |       |          |          |
|                       |      |              |                        |            |       |         | and find | many             | biased | utterances |       | present  | in the   |
suringbias(Leeetal.,2019b;Shengetal.,2019).
|          |            |     |                  |     |     |          | trainingdata. |     | Forexample,thequeenpersonaad- |     |     |     |     |

| Very few | foreground |     | the contribution |     | of  | training |               |     |                               |     |     |     |     |
herestonegativelystereotypedgenderroleswhen
| datatogenderbiasinmodeloutputs. |             |     |        |         | Forexample, |             |          |          |         |      |      |         |         |

|                                 |             |     |        |         |             |             | uttering | the line | I spend | my   | days | doing   | embroi- |
| Kang et                         | al. collect | a   | corpus | of text | that        | is parallel |          |          |         |      |      |         |         |
|                                 |             |     |        |         |             |             | dery and | having   | a talk  | with | the  | ladies. | Another |
acrossmultiplestylisticcategories,oneofwhichis
|         |                          |     |     |     |              |     | character | admires  | a   | sultry | wench    | with | fire in her |

| gender. | Closertoourwork,Liuetal. |     |     |     | presentatest |     |           |          |     |        |          |      |             |
|         |                          |     |     |     |              |     | eyes. We  | conclude |     | from   | examples | like | this that   |
datasetfordialogueandfindthatmodelscanpro-
|           |         |           |     |      |          |      | presenting | crowdworkers |     | with | gender |     | biased per- |

| duce less | diverse | dialogues |     | when | prompted | with |            |              |     |      |        |     |             |
sonasoftenleadsthemtocreateevenmoregender
| sentences | containing       |     | words | describing |        | individu-  |                             |     |     |     |                  |     |     |

|           |                  |     |       |            |        |            | biaseddialogues(seeTable3): |     |     |     | forexample,awife |     |     |
| als from  | underrepresented |     |       | groups.    | Still, | it differs |                             |     |     |     |                  |     |     |
personacontainsthetextIspendmydayscooking
fromourworkinthatthedatawascreatedbycom-
|                  |     |     |              |     |       |          | and cleaning |     | so my | husband | will | have | something |

| bining templates |     | and | hand-created |     | lists | of word- |              |     |       |         |      |      |           |
toeatwhenhereturnsfromhiswork...,and,indi-
| pairs, rather |     | than using | real | dialogue | data. | Liu |                      |     |     |                  |     |     |        |

|               |     |            |      |          |       |     | aloguewithamerchant, |     |     | discussesonlyher |     |     | clean- |
etal.alsoproposestwomethodsfordebiasing,one
|                                           |         |        |            |     |                |            | ingduties.   | Themerchant |             | evenderisivelyrefersto |            |         |         |

| ofwhichwealsoemploy(i.e.,CDA),andtheother |         |        |            |     |                |            |              |             |             |                        |            |         | effect  |
|                                           |         |        |            |     |                |            | cleaning     | as the      | wife’s      | job.                   | This could | be      | an      |
| of which                                  | extends | to     | sentences  | a   | word-embedding |            |              |             |             |                        |            |         |         |
|                                           |         |        |            |     |                |            | of gender    | stereotype  |             | priming                | (Blair     | and     | Banaji, |
| post-processing                           |         | method | (Bolukbasi |     | et             | al., 2016) |              |             |             |                        |            |         |         |
|                                           |         |        |            |     |                |            | 1996; Steele |             | and Ambady, |                        | 2006;      | Oswald, | 2008;   |
ineffective
| that has | been | shown | to be |     | at  | removing |     |     |     |     |     |     |     |

Derksetal.,2011;Verhaeghenetal.,2011).
| gender | bias (Gonen |     | and Goldberg |     | 2019, | but see |     |     |     |     |     |     |     |

Wang et al. 2020 for a more recent, perhaps more Given this, we wonder how much biased char-
|           |           |             |     |     |      |            | acter names |     | and personas |     | themselves |     | lead to |

| effective | attempt). | Finally—and |     |     | as a | direct ex- |             |     |              |     |            |     |         |
LIGHTdialoguesbeingmorebiasedthantheoth-
| tension | of this | work—Dinan |     | et al. | (2020) | decom- |     |     |     |     |     |     |     |

posesgenderbiasalongthreesemantic-pragmatic ers. Thus, we focus on persona-based dialogue
dimensions,andshowthattrainmorefine-grained text in particular for the remainder of the paper.
|     |     |     |     |     |     |     | Dialogue | research | has | found | that, | while | incorpo- |

classifiersallowformoreaccurateclassificationof
|         |        |         |     |         |        |         | rating personas |     | increases |     | engagingness |     | and im- |

| dataset | gender | biases. | The | novelty | of the | present |                 |     |           |     |              |     |         |
contribution lies in how we measure bias, and in proves consistency (Zhang et al., 2018; Shuster
|     |     |     |     |     |     |     | et al., 2018; |     | Mazare´ | et al., | 2018; | Olabiyi | et al., |

thejointapplicationofourthreegenderdebiasing
|     |     |     |     |     |     |     | 2018; Li | et al., | 2016b), | they | can | also | crystallize |

methods.
|     |     |     |     |     |     |     | gender | bias (Clark | et  | al., 2019; |     | Henderson | et al., |

2018). Suchbiaspropagatestosubsequentlygen-
## 3 MeasuringBias
|     |     |     |     |     |     |     | erated conversations. |     |     | Crowdworkers |     | in  | particular |

Before one can mitigate bias, one must first mea- might imbue their annotations with their partic-
sure it. As a first pass, we measured the counts ular gender biases at every stage of dataset cre-
of gendered words used (using a word list from ation. Forexample,LIGHT(Urbaneketal.,2019)
Zhaoetal.2018b),andthepercentofthosewhich was created by crowdworkers in stages: crowd-
referred to male characters for six datasets (Ta- workerswerefirstassignedacharacter(withpre-
ble 1). We count the number of male and fe- viously crowdsourced names such as “farmer” or
male gendered words in the training sets of sev- “witch”), as well as a previously crowdsourced
eraldatasets(LIGHT,ConvAI2,Reddit,Wizardof persona, or short textual description of the char-
8175

|             |     |     | #Characters |      |           | #Ref. | BiasinPersonas. |             |           | Inadditiontothestarkunder- |              |              |          |

|             |     | F   | M           | N    | All       | F M   |                 |             |           |                            |              |              |          |
|             |     |     |             |      |           |       | representation  |             | of female | characters,                |              | the          | medieval |
| LIGHT       |     |     |             |      |           |       | setting         | in LIGHT    | is        | likely                     | to encourage |              | crowd-   |
| Orig.Data   |     | 159 | 258         | 1460 | 1877 439  | 1238  |                 |             |           |                            |              |              |          |
|             |     |     |             |      |           |       | workers         | to generate |           | dialogues                  |              | accentuating | his-     |
| SwapPersona |     | 336 | 230         | 694  | 1260 1419 | 1030  |                 |             |           |                            |              |              |          |
NewCharac. 151 120 1448 1719 357 275 torical biases and inequalities of the time period
| Total     |     | 646  | 608  | 3602 | 4856 2215 | 2543 |            |           |            |         |        |          |             |

|           |     |      |      |      |           |      | (Bowman,   | 2010;     | Garcia,    |         | 2017). | We       | investigate |
| ConvAI2   |     |      |      |      |           |      | the number | of        | references |         | to men | or women | in the      |
| Orig.Data |     | 1109 | 1048 | 4214 | 6371 1283 | 1148 |            |           |            |         |        |          |             |
|           |     |      |      |      |           |      | text of    | personas, | as         | another | source | of       | bias. Take  |
forexample,afemalepersonathatcontainsagen-
| Table 4: | Analysis | of  | gender | in LIGHT |     | and Con- |     |     |     |     |     |     |     |

deredreferencesuchasIwanttofollowinmyfa-
vAI2:TheLIGHTdatasetiscomparedtosimilarnovel
|     |     |     |     |     |     |     | ther’s footsteps |     | rather | than | in my | mother’s. | Al- |

datasetsobtainedaftereithergender-swappingcharac-
terandpersonasorcollectingwhollynewones.#Char- though using gendered relational nouns (Barker,
acters refers to the counts of gendered characters and 1992; Williams, 2018), such as father, doesn’t al-
# Ref. refers to counts of gendered references in per- ways signal sexism, if female characters are pre-
sonas. TheoriginalLIGHTdatasetisskewedtowards
|                  |     |       |         |          |     |           | dominantly | defined |            | in reference |     | to male | charac-     |

| male characters, |     | while | ConvAI2 | contains |     | both male |            |         |            |              |     |         |             |
|                  |     |       |         |          |     |           | ters, it   | becomes | a problem. |              | We  | count   | the appear- |
andfemaleinaroughlyequalproportions.
|     |     |     |     |     |     |     | ance of | gendered | words | in  | personas | using | the list |

compiledbyZhaoetal.(2018b),andfindthatmen
|              |      |      |        |     |            |      | are disproportionately |     |     | referred | to  | in the | personas: |

| acter. Then, | they | were | paired | up, | and tasked | with |                        |     |     |          |     |        |           |
therearenearly3xasmanymentionsofmenthan
generatingadialogueasthosecharacters.
|              |     |      |      |             |     |           | women, | which | suggests |     | that a | large | number of |

| To determine |     | with | more | granularity |     | precisely |        |       |          |     |        |       |           |
charactersaredefinedbytheirrelationshipstomen
| how bias | manifests |     | in persona-based |     |     | dialogue |     |     |     |     |     |     |     |

(seeTable2forexamples,andTable4forcounts).
| datasets, | we investigate |     | the | text | for (i) characters |     |        |      |     |        |     |         |            |

|           |                |     |     |      |                    |     | Gender | bias | and | sexism | are | clearly | present in |
suchasfisherman(Table1),and(ii)personassuch
|           |         |        |     |         |        |        | many dialogue |     | datasets  | (Henderson |        | et    | al., 2018), |

| as I love | fishing | (Table | 2). | We ask: | (i) do | crowd- |               |     |           |            |        |       |             |
|           |         |        |     |         |        |        | but finding   | a   | clear way | to         | define | these | terms (and  |
workersgeneratemaleandfemalecharactersatan
|     |     |     |     |     |     |     | others that | categorize |     | unsafe | text), | let | alone mea- |

equalrate,(ii)dotheyimbuecharacters’personas
|     |     |     |     |     |     |     | suretheireffectsatscale,isverychallenging. |     |     |     |     |     | For |

withsexismorundesirablegenderbiases?
|         |        |     |             |     |          |        | example,  | the      | persona     | for        | the character |          | girl con- |

|         |        |     |             |     |          |        | tains the | line     | I regularly |            | clean         | and cook | dinner    |
| Bias in | Number | of  | Characters. |     | We first | deter- |           |          |             |            |               |          |           |
|         |        |     |             |     |          |        | (seeTable | 2formore |             | examples), |               | which    | strikesus |
minewhethercrowdworkerscreateanequalnum-
asstereotypicalandsexist,butitmightnotbeno-
| ber of   | male and | female     | characters. |           | To         | quantify |                                   |         |             |      |               |         |             |

|          |          |            |             |           |            |          | ticed by                          | others. | In          | this | paper,        | we rely | on each     |
| this, we | asked    | annotators |             | on Amazon | Mechanical |          |                                   |         |             |      |               |         |             |
|          |          |            |             |           |            |          | annotator’s                       | own,    | subjective, |      | definition(s) |         | of the      |
| Turk to  | label    | the gender |             | of each   | character  | name     |                                   |         |             |      |               |         |             |
|          |          |            |             |           |            |          | termbutaggregatemultipleopinions. |         |             |      |               |         | Threena¨ıve |
basedonitspersonadescription(choosingneutral
annotatorsexaminedeachpersonaforunsafecon-
| if the gender |     | was not | explicit). | This | annotation | is  |     |     |     |     |     |     |     |

Ifannotatorsdetectedcontentwas‘offensive’
tent.
possiblebecausemanypersonasincludetextsuch
or‘maybeoffensive’,theywereaskedtoselectone
asIamayoungwoman.1
Sincethismeasurement
|                                   |             |     |             |          |          |           | offourcategories—racist, |             |          |          | sexist, | classist, | other—       |

| requires                          | personas,   | we  | consider    |          | the two  | persona-  |                          |             |          |          |         |           |              |
|                                   |             |     |             |          |          |           | and to                   | provide     | a reason | for      | their   | response. | Just         |
| baseddialoguedatasetsinoursample: |             |     |             |          | LIGHTand |           |                          |             |          |          |         |           |              |
|                                   |             |     |             |          |          |           | over 2%                  | of personas |          | were     | flagged | by        | at least one |
| ConvAI2                           | (Zhang      | et  | al., 2018). |          | LIGHT    | is highly |                          |             |          |          |         |           |              |
|                                   |             |     |             |          |          |           | annotator,               | and         | these    | personas | and     | their     | resulting    |
| gender                            | imbalanced: |     | there       | are over | 1.6      | times as  |                          |             |          |          |         |           |              |
dialogueswereremoved.
| many male | characters |     | as female |     | ones2. | LIGHT is |     |     |     |     |     |     |     |

alsoconsiderablylessgender-balancedthanConv-
## 4 MitigatingBiasinGenerativeDialogue
AI2,whichhasanearlyequalnumberofmaleand
femalegenderedpersonas(seeTable4).
|       |          |           |     |         |          |            | In this  | section,   | we  | present | a             | general | frame-    |

|       |          |           |     |         |          |            | work for | mitigating |     | bias    | in generative |         | dialogue. |
| 1Note | that our | procedure |     | doesn’t | preclude | annotators |          |            |     |         |               |         |           |
from implicitly assuming genders for ungendered personas, More specifically, we explore data augmentation
suchas“doctor”,whichmaywidenthegendergap. and other algorithmic methods to mitigate bias
| 2When | we  | use “female” |     | and | “male”—rather | than |               |     |             |     |         |     |            |

|       |     |              |     |     |               |      | in generative |     | Transformer |     | models. |     | We (i) ex- |
“woman”and“man”—wewantourreferencetoincludechar-
actersthatarebinarilygendered,butnotnecessarilyhuman. tendcounterfactualdataaugmentationtodialogue
8176

Figure1:Wecomparetheperformanceofvariousbiasmitigationmethods:CounterfactualDataAugmentation
(CDA),Positive-BiasDataCollection(Pos. Data),BiasControlModel(BiasCtrl),andcombiningthesemethods
|     |     |     |     | F0/+ M0/+ | X0  |     |     |     |

(ALL).Wesplittestsetacrossthefourgenderednessbins: . indicatestherearenoX-genderedwords
+
in the gold response, while X indicates that there is at least one. We measure the percent of gendered words
generatedinthedialogue(%gend. words)andthepercentofmalebias(%malebias), i.e. thepercentofmale-
gendered words out of all generated gendered words. While each of these methods yield some improvement,
combiningthemyieldsthebestcontroloverthegenderednessoftheutteranceswhileimprovingtheF1-score. The
orangeoutlinerepresentsthebestperformingmodel. For%Genderedwords, lowerisbetter. For%MaleBias,
| closerto50isbetter. | ForF1Score,higherisbetter. |     |     |     |     |     |     |     |

(HallMaudslayetal.,2019;Zmigrodetal.,2019) Positive-Bias Data Collection (Pos. Data) strat-
following (Liu et al., 2019), (ii) perform positive egy. Wefirstcollectadditionalpersonasbyhaving
datacollectionbyaugmentingtheexistingdataset humans(i)manuallyswapthegenderofthechar-
via targeted data collection with crowdworkers, acternameandallgenderedreferencesinthechar-
andlastly,(iii)applycontrollablegenerationtech- acter’s persona text (rather than relying on brit-
niques to gender bias to control how many male tlewordlists)and(ii)writeadditional,diversified
andfemalegenderedwordsmodelsproduce. personas. We then use these personas to seed the
collectionofadditional,positivelybiaseddialogue
### 4.1 CounterfactualDataAugmentation data,whichwerefertoasPos. Datathroughout.
| A straightforward | solution | for gender | bias in em- |     |     |     |     |     |

beddings is Counterfactual Data Augmentation New Characters & Personas. When a dataset
(CDA)(HallMaudslayetal.,2019;Zmigrodetal., contains more male characters and references to
| 2019; Liu | et al., 2019). | CDA swaps, | say, all in- |     |     |     |     |     |

malecharactersthanitcontainsfemalecharacters
stancesofgrandmotherwithgrandfather,shewith
|     |     |     |     | and references | to female | characters | (see | Table 4), |

he, etc. We apply this word-based augmentation we balance existing characters and personas with
to dialogue by first copying every dialogue, then gender swapping. For every gendered character-
| swapping | all gendered | words with | their counter- |     |     |     |     |     |

personapairing,annotatorscreateanewopposite-
part from the paired list in Zhao et al. (2018b). genderedcharacter-personapairingforwhichani-
The augmentation is limited to words on the list, mate nouns or pronouns are changed, but the rest
| andtheswappingisperformedautomatically. |     |     | The |                |         |            |     |          |

|                                         |     |     |     | of the persona | remains | unchanged. | For | example, |
model is then retrained on the augmented data. foreverypersonadescribingamalecharacterlike
WhileCDAissomewhateffectivestrategyformit-
|     |     |     |     | a king, annotators | will | create a | new one | describ- |

igating bias in word embeddings, this method has ing a female character like a queen. Annotators
| several pitfalls: | it may | result in | ungrammatical |                |         |               |     |            |

|                   |        |           |               | are instructed | to swap | the gender(s) | of  | other ani- |
sentences, and it relies on existing (and perhaps matereferencesinthetext(e.g.,ifanoriginalper-
incomplete)liststodetermineandswapgender. sona describes a woman in relation to her father,
|     |     |     |     | the new male | persona | will describe | a man | in re- |

### 4.2 Positive-BiasDataCollection
|     |     |     |     | lation to | his mother). | This method | ensures | that |

ToresolvetheissueswithCDA,weusehumansto the created sentences will be grammatical, unlike
collectadditionaldialoguedataviaatwo-pronged heuristicdataaugmentation.
8177

However, simply balancing references to men F0M0 F0M+ F+M0 F+M+
and women is insufficient, as female characters
%oftestset 60.65 27.21 7.61 4.63
mightbespecificallydescribedinsexistways(see
§3). As detecting sexism is challenging (also see Table 5: Percentage of dialogue examples in each
§3), we take our qualitative analysis to be suffi- of the four genderedness bins —F0/+ M0/+ — for the
cient motivation, and moved to further offset the LIGHTdialoguedatatestset.
bias by collecting a new set of interesting and in-
dependent female characters. We primed work-
Bias Control (Bias Ctrl) via conditional training.
ersbyshowingexamplesofgenderunderspecified
Previousconditionaltrainingmodelslearntoasso-
characternameslikeadventurerwithpersonaslike
ciatespecificcontroltokenswithsomedesiredtext
Iamawomanpassionateaboutexploringaworld
properties(Kikuchietal.,2016;Fanetal.,2018a;
Ihavenotyetseen. Iembarkonambitiousadven-
Oraby et al., 2018; See et al., 2019), but have not
tures. We also provided crowdworkers with addi-
beenappliedtoaddressbiasissues.
tional instruction to encourage them to create di-
We apply conditional training techniques to
versecharacters: We’relookingfor stronganddi-
control gender bias in generative dialogue by
verse descriptions. Avoid descriptions that could
learning to associate control tokens with proper-
be considered hateful, offensive, or stereotypical.
tiesofgenderbias. Anygeneralfunctionthattakes
Even with explicit instruction, annotators created
as input a dialogue utterance and outputs a con-
3 times as many male characters as female char-
tinuous or discrete value that provides informa-
acters, revealing the stubbornness of the inherent
tion about gender bias could be used as a control
gender biases of the available crowdworker pool.
variable. In our case, prior to training, each dia-
Weultimatelyexcludeallmale-genderedpersonas
logue response is binned into one of four bins—
createdinthisfashionfromthenewdataset,asin- F0/+ M0/+ —whereX0indicatesthattherearezero
cludingthemwouldworsenthegenderbalanceof +
X-gendered words in the response. X indicates
thedataset. Ournewdatasetisapproximatelybal-
the presence of one or more X-gendered word.
anced then in the number of male or female char-
The percentage of test set examples that fall into
acters and in the number of references to male or
each bin is in Table 5. Nouns and adjectives are
female characters (see Table 4). In total, we add
binned into gendered bins via an aggregation of
2,629 new characters and release the data for op-
existinggenderedwordlists(Zhaoetal.,2018b,a;
tionalinclusionintheLIGHTdataset.
Hoyle et al., 2019). Note that other functions
NewDialogues. Aftergender-balancingtheper- couldbeusedaswell,suchasabiasclassifier(Di-
sonas, wemovedontousingthegender-balanced nanetal.,2020).
personas to crowdsource additional, hopefully We append a special token to the input that in-
gender-balanced, dialogues. We selected more dicates which bin the response falls into. During
female-gendered characters for new dialogue col- Bias Ctrl training, the model should learn to as-
lection, and explicitly instructed annotators to be sociatethespecialtokenwiththegenderednessof
mindful of gender bias. In particular, we en- thedialogueresponse,suchthatatinferencetime,
couraged them to assume equality—social, eco- we could append different special tokens to con-
nomic, political, or otherwise—between genders trolthegenderednessofthemodeloutput. Forex-
(Note: this is uniquely possible with a dataset ample, a model trained with multiple gender con-
like LIGHT, which is situated in a fully fictional trolbinscouldbesettothegenderneutral(inthis
world). Wecollectedatotalof507newdialogues
case,F0M0)settingatinferencetime,toproducea
containing6,658utterances(approximately 6%of responsecontainingfew(orno)genderedwords.
the original dataset size). We refer to this addi-
### 4.4 ImplementationDetails
tionaldialoguedataasPos. Data.
Following Urbanek et al. (2019), we fine-tune a
### 4.3 BiasControlledTraining
large,pre-trainedTransformerencoder-decoderon
Gender bias in dialogue can take the form of im- thedialoguesintheLIGHTdatasetforallgenera-
balanced use of gendered words. To create dia- tionexperiments. FollowingHumeauetal.(2019),
logue models that can generate an equal number we pre-trained on Reddit conversations extracted
of gendered words, we control model output with and obtained by a third party, and made avail-
8178

Figure2: PerformanceoftheALLdebiasingmodelcontrolledbyindicatingspecificbinsforallexamplesattest
time. We report results for each possible conditioning bin choice. Across bins (at the top of graphs), the model
maintainsperformanceasmeasuredbyF1whilstradicallychangingthegenderednessofthelanguagegenerated.
ableonpushshift.io. Duringpre-training,models models not only reflect dataset biases, but also
learnedtogenerateacommentconditionedonthe theyamplifythem. Whenthemodelproducesgen-
precedingconversationthread. Allcommentsthat deredwords,itgeneratesmale-genderedwordsthe
containedURLsorwereshorterthan5characters vast majority of the time. Even when the gold la-
+ M0),
long were removed, along with child comments, belonlycontainsfemale-genderedwords(F
resulting in approximately 2.2 billion training ex- itstillgeneratesmale-genderedwordsnearly78%
| amples. | Similarlyduringfine-tuning,modelswere |     |     |     | ofthetime. |     |     |     |     |     |     |

conditionedonthefullprecedingdialoguehistory.
|     |     |     |     |     | Comparing | Debiasing |     | Methods |     | As shown | in  |

Allmodelsare8-layerencoders,8-layerdecoders,
|          |             |            |     |           | Figure 1, | each | method | improves | on  | the metrics— |     |

| with 512 | dimensional | embeddings | and | 16 atten- |           |      |        |          |     |              |     |
%genderedwords,%malebias,andF1—overthe
tionheadsbasedontheParlAItransformerimple-
|                              |     |     |               |     | baseline    | Transformer, |     | but we | find          | that combining |       |

| mentation(Milleretal.,2017). |     |     | Wedecodewitha |     |             |              |     |        |               |                |       |
|                              |     |     |               |     | all methods | (ALL)        | is  | most   | advantageous. |                | While |
beamsearchsizeof5.
ALLhasmoredatathanCDAandBiasCtrl,more
|     |     |     |     |     | data alone | is not | enough—the |     | Positive-Bias |     | Data |

## 5 Results
|          |                  |     |             |          | Collection   | model   | does | not         | achieve | as strong | re-  |

| We train | five Transformer |     | models: one | baseline |              |         |      |             |         |           |      |
|          |                  |     |             |          | sults as ALL | despite |      | also having | more    | data.     | Both |
trained only on original LIGHT without any mit- the BiasCtrl andALL models benefitfrom know-
igation techniques, one Transformer for each of ing the data split (F0M0, for example), and both
|     |     | §4.1 |     | §4.2 |     |     |     |     |     |     |     |

our three methods (see for CDA, for yieldagenderratioclosesttogroundtruth.
| Positive-Bias | Data | Collection, | and §4.3 | for Bias |                 |     |          |     |          |          |     |

|               |      |             |          |          | Bias Controlled |     | Training |     | Controls | Gendered |     |
Control),andafinalonecombiningallthreemeth-
|     |     |     |     |     | Words. | Our | Bias | Ctrl method | can | control | the |

ods(ALL)thatachievesthebestresults.
numberofgenderedwordsingenerateddialogues
BiasisAmplifiedinGeneration. Figure1com- (Figure 2). We examine the effect of Bias Ctrl by
pares the performance of the various techniques. generating responses conditioning the ALL model
We compare our methods to the gold labels from oneachbin. Weobservethatchangingthebinrad-
the test set and to the baseline. To do this, we ically changes the genderedness of generated text
differences
divide the test set into four genderedness bins with only small in overall F1, which
§4.3)—F0M0, F0M + + M0, showsthattheBiasCtrlmethodisefficacious.
| (as defined | in  |     | ,   | F and |     |     |     |     |     |     |     |

F + M + —and calculate: (i) the F1 word overlap Examplesofgeneratedtextfromboththebase-
withthegoldresponse,(ii)thepercentageofgen- line and the ALL model are shown in Table 6.
dered words generated (% gend. words), and (iii) Further examples are provided in the Appendix
thepercentageofmale-genderedwordsgenerated in Table 12. The baseline model generates male-
(relative to the sum total of gendered words gen- gendered words when the gold response con-
erated by the model). We find that Transformer tains no gendered words or only female-gendered
8179

GenerationExamples as offensive or safe following Liu et al. (2019).
offensive
|     | F0M0 |     |     |     |     |     | The classifier | was | fine-tuned |     | on an |     | lan- |

Bin
|         |       |                                  |     |     |     |     | guage | classification |     | task (Dinan |     | et al., | 2019), |

| Context | [P1:] | Idon’trememberanythingIwashoping |     |     |     |     |       |                |     |             |     |         |        |
youcouldfindout. and achieves state-of-the-art results. We apply
|     | [P2:] | Yourformisveryhazy. |     |     | Doyouremem- |     |                 |     |      |           |           |     |        |

|     |       |                     |     |     |             |     | this classifier | to  | each | utterance | generated |     | by the |
berifyouareamanorwoman?
Baseline: iamnotaman.iamamanoftheforest. ALLmodelandbaselinemodelsonthetestset,in
ALL: no,idon’tremember. additiontothegold(humangenerated)labelsfrom
Idon’tknowwhat’swrongwithme!
Gold:
|     |     |     |     |     |     |     | thetestset. | Thedialoguesafetyclassifierratesour |     |     |     |     |     |

F+M0
| Bin     |       |                                  |     |     |     |     |          |     |       |         | offensive |      |      |

|         |       |                                  |     |     |     |     | proposed | ALL | model | as less |           | than | both |
| Context | [P1:] | Idonotbelievemyeyes,foranangelis |     |     |     |     |          |     |       |         |           |      |      |
thebaselinemodelandthegroundtruth(gold)la-
uponme!Angel,pleasetellmeyourname.
[P2:] MynameisAbigail! bels, which argues in favor of the efficacy of our
| Baseline: | mynameisabigail.iamthekingofthis |     |     |     |     |     |     |     |     |     |     |     |     |

debiasingmethods.
kingdom.
| ALL:  | iamthequeen’sdaughter! |                     |     |     |           |     |                      |     |     |                |     |     |     |

| Gold: | Abigail!               | Suchabeautifulname. |     |     | TowhatdoI |     |                      |     |     |                |     |     |     |
|       |                        |                     |     |     |           |     | 5.2 HumanEvaluation: |     |     | BiasandQuality |     |     |     |
owethepleasureofmeetingyou?
|       |            |             |     |      |     |          | We compare | the   | quality     | of  | our debiasing |       | meth- |

| Table | 6: Example | generations |     | from | the | baseline |            |       |             |     |               |       |       |
|       |            |             |     |      |     |          | ods using  | human | evaluation. |     | One           | might | hy-   |
modelandtheproposeddebiasedmodels.Groundtruth pothesize that some gender debiasing methods
| (‘Gold’)        | either | contains | no  | gendered     | words | or only |               |           |               |     |       |        |         |

|                 |        |          |     |              |       |         | work by       | replacing | contentful    |     | words | (e.g., | witch)  |
| female-gendered |        | words,   | but | the baseline | model | still   |               |           |               |     |       |        |         |
|                 |        |          |     |              |       |         | with bleached | or        | uninteresting |     | ones  | (e.g., | person, |
generatesmale-genderedwords.
thing),effectivelytradingoffgenderbiaswithen-
|     |     |            |     |          |     |     | gagingness. | Generative |         | models  | in   | particular | are     |

|     |     | GoldLabels |     | Baseline | ALL |     |             |            |         |         |      |            |         |
|     |     |            |     |          |     |     | well-known  | to         | produce | generic | text | (Li        | et al., |
%Offensive
|           |           |           | 13.0     | 14.25          | 10.37     |       |         |              |         |            |      |              |          |

|           |           |           |          |                |           |       | 2016a;  | Fan et al.,  | 2018b), | which      | is   | often        | less en- |
|           |           |           |          |                |           |       | gaging. | Overreliance |         | on generic |      | text might   | in-      |
|           | Offensive | language  |          | classification |           |       |         |              |         |            |      |              |          |
| Table     | 7:        |           |          |                | of        | model |         |              |         |            |      |              |          |
|           |           |           |          |                |           |       | crease  | the chances  | of      | biases     | such | as androcen- |          |
| responses | on        | the LIGHT | dialogue |                | test set. | The   |         |              |         |            |      |              |          |
ALL model generates a lower percentage of offensive trism, or the propensity of societies to consider
|     |     |     |     |     |     |     | men central | but | women | peripheral |     | (Bem, | 1993; |

utterances.
|     |     |     |     |     |     |     | Bailey | et al., 2020); |     | in language, |     | male-gendered |     |

wordsoftenactasagender-neutralstandard(Bai-
words,evengeneratingunlikelysequencessuchas
|     |     |     |     |     |     |     | ley et | al., 2019), | as  | in Neil | Armstrong’s |     | 1969 |

my name is abigail. i am the king of this king- quote“onesmallstepforaman,onegiantleapfor
| dom. | For various | methods, |     | we compute |     | the top |           |                                  |     |     |     |     |     |

|      |             |          |     |            |     |         | mankind”. | Weusethedialogueevaluationsystem |     |     |     |     |     |
20wordsgeneratedonthetestset(afterremoving
|     |     |     |     |     |     |     | Acute-Eval | (Li | et al., | 2019) | to ask | evaluators | to  |

stop words), shown in Appendix Table 8. We de- compare pairs of conversations from models and
| notegenderednounsusinganasterisk. |     |     |     |     | Amongthe |     |     |     |     |     |     |     |     |

decidewhichmodelgenerates(i)morebiaseddia-
| top 20 | words | generated | by  | the baseline, | there | are |        |          |               |     |            |     |         |

|        |       |           |     |               |       |     | logues | and (ii) | more engaging |     | dialogues. |     | We col- |
onlytwogenderednouns—knightandking—both
|     |     |     |     |     |     |     | lect 100 | model | conversations |     | with | crowdworkers |     |

TheALL
male-gendered. modelgenerates similar per method. Then, we compare conversations be-
| words, | but | also features | queen | in  | its top | 20, an- |       |         |     |              |     |       |         |

|        |     |               |       |     |         |         | tween | a human | and | the baseline |     | model | to con- |
otherindicationthatgenderismorebalanced.
|     |     |     |     |     |     |     | versations | between | a   | human | and the | ALL | model |

withallgenerationssettotheF0M0gender-neutral
### 5.1 SafetyofGeneratedText
|     |     |     |     |     |     |     | control | bin. We | found | that asking |     | for predictions |     |

effective
To further evaluate our techniques, we investigate of speaker gender was more than asking
offen-
| whether         | the | ALL model | generates |           | fewer |          | aboutsexismdirectly. |     |     |     |     |     |     |

| sive utterances |     | than      | (i) the   | baseline, | and   | (ii) the |                      |     |     |     |     |     |     |
AsshowninFigure3,predictingthegenderac-
human-generatedgoldlabels. Ourbiasmitigation curately of ALL model generations is more chal-
techniqueshavetheancillarybenefitofproducing lenging (significant at p < 0.01 with a t-test), but
offen-
models that generate proportionately fewer theresponsesarejustasengagingaccordingtohu-
siveutterances;seeTable7forresults. manevaluators. Weconcludeourproposedmeth-
We use a Transformer-based dialogue safety ods are able to help mitigate gender bias without
classifier to classify model-generated utterances degradingdialoguequality.
8180

enilesaB revo LLA referp % 1.0 Nata˜ MBarbosaandMonchuChen.2019. Rehuman-
|     |     |     |     |     |     |     | izedcrowdsourcing: |     |     | Alabelingframeworkaddress- |     |     |     |

0.8
|     |     | 0.6 |     |     |     |     | ingbiasandethicsinmachinelearning.       |     |     |     |     | InProceed- |     |

|     |     | 0.4 |     |     |     |     | ingsofthe2019CHIConferenceonHumanFactors |     |     |     |     |            |     |
inComputingSystems,page543.ACM.
0.2
0.0
engagingness harder to  Chris Barker. 1992. Possessive descriptions. Ph.D.
 predict gender
thesis,UniversityofCalifornia,SantaCruz.
| Figure 3: | Human | Evaluation |     | of ALL | model | (F0M0) |     |     |     |     |     |     |     |

ChristineBasta,MartaR.Costa-jussa`,andNoeCasas.
| compared | to baseline |     | Transformer |     | generative | model. |     |     |     |     |     |     |     |

Evaluators choose which model output they prefer 2019. Evaluatingtheunderlyinggenderbiasincon-
|              |              |     |     | difficulty |     |            | textualized | word | embeddings. |     | In  | Proceedings | of  |

| for dialogue | engagingness |     | and |            | of  | predicting |             |      |             |     |     |             |     |
theFirstWorkshoponGenderBiasinNaturalLan-
| speaker | gender. | The | ALL model | produces |     | less gen- |     |     |     |     |     |     |     |

guageProcessing,pages33–39,Florence,Italy.As-
deredtextwhileengagingnessisnotaffected.
sociationforComputa
|     |     |     |     |     |     |     | SandraLBem.1993. |     |     | Thelensesofgender:Transform- |     |     |     |

## 6 Conclusion
|     |     |     |     |     |     |     | ingthedebateonsexualinequality. |     |     |     |     | YaleUniversity |     |

Press.
| We analyze | gender | bias        | in  | dialogue   | data | and re-    |         |                |          |           |           |            |       |

|            |        |             |     |            |      |            | Irene V | Blair and      | Mahzarin |           | R Banaji. | 1996.      | Auto- |
| sulting    | model  | generations |     | for models |      | trained on |         |                |          |           |           |            |       |
|            |        |             |     |            |      |            | matic   | and controlled |          | processes | in        | stereotype | prim- |
dialogue data. We propose general purpose tech- ing. Journal of personality and social psychology,
| niques | for reducing | gender |     | bias in | generated | text. |     |     |     |     |     |     |     |

70(6):1142.
Themethodsdescribedinthispapercombinedata
|                 |     |               |     |      |             |             | Su Lin | Blodgett,  | Solon  | Barocas, | Hal       | Daume´       | III, and |

| augmentation,   |     | positive-bias |     | data | collection, | and         |        |            |        |          |           |              |          |
|                 |     |               |     |      |             |             | Hanna  | Wallach.   | 2020.  |          | Language  | (technology) | is       |
| bias controlled |     | training.     | We  | note | that        | our results |        |            |        |          |           |              |          |
|                 |     |               |     |      |             |             | power: | A critical | survey |          | of “bias” | in NLP.      | In Pro-  |
showthatdatacollectiontechniqueshelpmitigate ceedings of the 58th Annual Meeting of the Asso-
issues, so when it is possible, bias should be con- ciationforComputationalLinguistics,pages5454–
|         |        |          |        |      |          |       | 5476, | Online. | Association |     | for Computational |     | Lin- |

| sidered | at the | earliest | stages | of a | project. | Newly |       |         |             |     |                   |     |      |
guistics.
| collected | or constructed |     | datasets |     | should | consider |     |     |     |     |     |     |     |

how to carefully craft the collection to mitigate Tolga Bolukbasi, Kai-Wei Chang, James Y Zou,
|                |          |           |             |        |         |             | Venkatesh       | Saligrama,     |           | and         | Adam        | T Kalai. | 2016.    |

| bias issues    | from     | the       | very start. | When   |         | this is not |                 |                |           |             |             |          |          |
|                |          |           |             |        |         |             | Man             | is to computer |           | programmer  |             | as woman | is to    |
| possible,      | however, | such      | as          | in the | case    | of using    |                 |                |           |             |             |          |          |
|                |          |           |             |        |         |             | homemaker?      |                | debiasing | word        | embeddings. |          | In Ad-   |
| real-world     | data     | or a      | dataset     | that   | already | exists,     |                 |                |           |             |             |          |          |
|                |          |           |             |        |         |             | vances          | in neural      |           | information | processing  |          | systems, |
| the techniques |          | presented | in          | this   | paper   | are shown   | pages4349–4357. |                |           |             |             |          |          |
effective
| to be          |     | at reducing |      | gender    | bias. | They    |               |         |                                 |       |     |           |          |

|                |     |             |      |           |       |         | Sarah Lynne   | Bowman. |                                 | 2010. | The | functions | of role- |
| are especially |     | effective   | when | combined, |       | produc- |               |         |                                 |       |     |           |          |
|                |     |             |      |           |       |         | playinggames: |         | howparticipantscreatecommunity, |       |     |           |          |
inglessgendered,morebalanced,saferutterances
|                                           |     |     |     |     |     |     | solveproblemsandexploreidentity. |     |     |     |     | McFarlandand |     |

| thatmaintaintheengagingnessofthedialogue. |     |     |     |     |     |     | Co.                              |     |     |     |     |              |     |
Marc-EtienneBrunet,ColleenAlkalay-Houlihan,Ash-
Acknowledgements
|     |     |     |     |     |     |     | ton Anderson, |     | and     | Richard | Zemel.  | 2018.       | Under- |

|     |     |     |     |     |     |     | standing      | the | origins | of bias | in word | embeddings. |        |
Thanks to Isabelle Kloumann, Ledell Wu, and arXivpreprintarXiv:1810.03611.
| Hila Gonen |     | for comments |     | and | advice | on this |                  |     |             |            |             |       |           |

| project.   |     |              |     |     |        |         | Yang Trista      | Cao | and         | Hal Daume´ | III.        | 2020. | Toward    |
|            |     |              |     |     |        |         | gender-inclusive |     | coreference |            | resolution. |       | In Pro-   |
|            |     |              |     |     |        |         | ceedings         | of  | the 58th    | Annual     | Meeting     | of    | the Asso- |
ciationforComputationalLinguistics,pages4568–
| References |     |     |     |     |     |     | 4595, | Online. | Association |     | for Computational |     | Lin- |

guistics.
| April H | Bailey, | Marianne | LaFrance,   |     | and    | John F Do- |         |        |       |              |     |             |     |

| vidio.  | 2019.   | Is man   | the measure |     | of all | things? a  |         |        |       |              |     |             |     |
|         |         |          |             |     |        |            | Kai-Wei | Chang, | Vinod | Prabhakaran, |     | and Vicente | Or- |
social cognitive account of androcentrism. Person- donez. 2019. Bias and fairness in natural language
alityandSocialPsychologyReview,23(4):307–331. processing. In Proceedings of the 2019 Confer-
|     |     |     |     |     |     |     | ence | on Empirical |     | Methods | in Natural |     | Language |

April H Bailey, Marianne LaFrance, and John F Do- Processing and the 9th International Joint Confer-
vidio. 2020. Implicit androcentrism: Men are hu- ence on Natural Language Processing (EMNLP-
man,womenaregendered. JournalofExperimental IJCNLP): Tutorial Abstracts, Hong Kong, China.
SocialPsychology,89:103980. AssociationforComputa
8181

Serina Chang and Kathy McKeown. 2019. Automat- Angela Fan, Mike Lewis, and Yann Dauphin. 2018b.
ically inferring gender associations from language. Hierarchical neural story generation. In Proceed-
InProceedingsofthe2019ConferenceonEmpirical ings of the 56th Annual Meeting of the Association
Methods in Natural Language Processing and the forComputationalLinguistics(Volume1: LongPa-
9thInternationalJointConferenceonNaturalLan- pers), pages 889–898, Melbourne, Australia. Asso-
guage Processing (EMNLP-IJCNLP), pages 5745– ciationforComputa
5751,HongKong,China.AssociationforComputa-
tionalLinguistics. Lisa Fan, Marshall White, Eva Sharma, Ruisi Su,
|     |     |     |     |     |     |     | Prafulla | Kumar Choubey, | Ruihong | Huang, | and |

Christopher Clark, Mark Yatskar, and Luke Zettle- LuWang.2019. Inplainsight: Mediabiasthrough
moyer.2019. Don’ttaketheeasywayout: Ensem- the lens of factual reporting. In Proceedings of the
ble based methods for avoiding known dataset bi- 2019 Conference on Empirical Methods in Natu-
ases. arXivpreprintarXiv:1909.03683. ral Language Processing and the 9th International
|     |     |     |     |     |     |     | Joint Conference | on Natural | Language | Processing |     |

MartaRCosta-jussa`.2019. Ananalysisofgenderbias (EMNLP-IJCNLP), pages 6342–6348, Hong Kong,
China.AssociationforComputa
| studiesinnaturallanguageprocessing. |     |     |     |     | NatureMa- |     |     |     |     |     |     |

chineIntelligence,pages1–2.
|     |     |     |     |     |     |     | Antero Garcia. | 2017. Privilege, |     | power, and | dungeons |

Belle Derks, Colette Van Laar, Naomi Ellemers, and & dragons: How systems shape racial and gender
|     |           |       |             |     |        |        | identities | in tabletop role-playing |     | games. | Mind, |

| Kim | De Groot. | 2011. | Gender-bias |     | primes | elicit |            |                          |     |        |       |
queen-bee responses among senior policewomen. Culture,andActivity,24(3):232–246.
Psychologicalscience,22(10):1243–1249.
|              |        |     |             |     |       |         | Aparna Garimella,  | Carmen                     | Banea, | Dirk Hovy, | and |

|              |        |     |             |     |       |         | RadaMihalcea.2019. | Women’ssyntacticresilience |        |            |     |
| Emily Dinan, | Angela |     | Fan, Ledell | Wu, | Jason | Weston, |                    |                            |        |            |     |
Douwe Kiela, and Adina Williams. 2020. Multi- and men’s grammatical luck: Gender-bias in part-
dimensionalgenderbiasclassification. InProceed- of-speechtagginganddependencyparsing. InPro-
ings of the 2020 Conference on Empirical Methods ceedings of the 57th Annual Meeting of the Asso-
inNaturalLanguageProcessing(EMNLP). ciationforComputationalLinguistics,pages3493–
|              |         |     |         |          |              |            | 3498, Florence,    | Italy. | Association | for Computa- |     |

| Emily Dinan, | Samuel  |     | Humeau, | Bharath  | Chintagunta, |            | tionalLinguistics. |        |             |              |     |
| and Jason    | Weston. |     | 2019.   | Build it | break it     | fix it for |                    |        |             |              |     |
dialoguesafety:Robustnessfromadversarialhuman Andrew Gaut, Tony Sun, Shirlyn Tang, Yuxin Huang,
|         |                |     |     |          |            |     | Jing Qian, | Mai ElSherief, |     | Jieyu Zhao, | Diba |

| attack. | In Proceedings |     | of  | the 2019 | Conference | on  |            |                |     |             |      |
Empirical Methods in Natural Language Process- Mirza, Elizabeth Belding, Kai-Wei Chang, and
ing and the 9th International Joint Conference on WilliamYangWang.2020. Towardsunderstanding
Natural Language Processing (EMNLP-IJCNLP), gender bias in relation extraction. In Proceedings
pages 4537–4546, Hong Kong, China. Association of the 58th Annual Meeting of the Association for
|     |     |     |     |     |     |     | Computational | Linguistics, | pages | 2943–2953, | On- |

forComputa
line.AssociationforComputa
| Yupei Du, | Yuanbin | Wu, | and | Man Lan. | 2019. | Explor- |     |     |     |     |     |

ing human gender stereotypes with word associa- Hila Gonen and Yoav Goldberg. 2019. Lipstick on a
InProceedingsofthe2019Conferenceon pig: Debiasingmethodscoverupsystematicgender
tiontest.
Empirical Methods in Natural Language Process- biasesinwordembeddingsbutdonotremovethem.
ing and the 9th International Joint Conference on InProceedingsofthe2019ConferenceoftheNorth
Natural Language Processing (EMNLP-IJCNLP), American Chapter of the Association for Computa-
pages 6133–6143, Hong Kong, China. Association tional Linguistics: Human Language Technologies,
forComputationalLinguistics. Volume1(LongandShortPapers),pages609–614,
|            |        |             |     |            |            |          | Minneapolis,       | Minnesota.AssociationforComputa- |     |     |     |

| Ali Emami, | Paul   | Trichelair, |     | Adam       | Trischler, | Kaheer   | tionalLinguistics. |                                  |     |     |     |
| Suleman,   | Hannes | Schulz,     |     | and Jackie | Chi        | Kit Che- |                    |                                  |     |     |     |
ung. 2019. The KnowRef coreference corpus: HilaGonen, YovaKementchedjhieva, andYoavGold-
|     |     |     |     |     |     | difficult |     |     |     |     | affect |

Removing gender and number cues for berg. 2019. How does grammatical gender
pronominalanaphoraresolution. InProceedingsof nounrepresentationsingender-markinglanguages?
the57thAnnualMeetingoftheAssociationforCom- In Proceedings of the 2019 Workshop on Widening
putational Linguistics, pages 3952–3961, Florence, NLP, pages 64–67, Florence, Italy. Association for
Italy.AssociationforComputationalLinguistics. Computa
AngelaFan,DavidGrangier,andMichaelAuli.2018a. NizarHabash, HoudaBouamor, andChristineChung.
Controllable abstractive summarization. In Pro- 2019. Automaticgenderidentificationandreinflec-
ceedings of the 2nd Workshop on Neural Machine tion in Arabic. In Proceedings of the First Work-
Translation and Generation, pages 45–54, Mel- shoponGenderBiasinNaturalLanguageProcess-
bourne, Australia. Association for Computational ing,pages155–165,Florence,Italy.Associationfor
| Linguistics. |     |     |     |     |     |     | ComputationalLinguistics. |     |     |     |     |

8182

Rowan Hall Maudslay, Hila Gonen, Ryan Cotterell, In Proceedings of the 2016 Conference on Empiri-
andSimoneTeufel.2019. It’sallinthename: Mit- calMethodsinNaturalLanguageProcessing,pages
igatinggenderbiaswithname-basedcounterfactual 1328–1338,Austin,Texas.AssociationforCompu-
| data | substitution. |     | In Proceedings |     | of the | 2019 Con- | tationalLinguistics. |     |     |     |     |     |

ferenceonEmpiricalMethodsinNaturalLanguage
Processing and the 9th International Joint Confer- Nayeon Lee, Yejin Bang, Jamin Shin, and Pascale
ence on Natural Language Processing (EMNLP- Fung. 2019a. Understanding the shades of sexism
|     |     |     |     |     |     |     | in popular | TV  | series. | In Proceedings |     | of the 2019 |

IJCNLP),pages5267–5275,HongKong,China.As-
|     |     |     |     |     |     |     | Workshop | on  | Widening | NLP, | pages | 122–125, Flo- |

sociationforComputa
rence,Italy.AssociationforComputationalLinguis-
| Reyhaneh | Hashempour.             |     | 2019. | A   | deep learning | ap-        | tics. |     |     |     |     |     |

| proach   | to language-independent |     |       |     | gender        | prediction |       |     |     |     |     |     |
on Twitter. In Proceedings of the 2019 Workshop Nayeon Lee, Andrea Madotto, and Pascale Fung.
onWideningNLP,pages92–94,Florence,Italy.As- 2019b. Exploring social bias in chatbots using
sociationforComputationalLinguistics. stereotype knowledge. In Proceedings of the 2019
|                                   |     |     |     |     |     |         | Workshop | on  | Widening | NLP, | pages | 177–180, Flo- |

| HeHe,ShengZha,andHaohanWang.2019. |     |     |     |     |     | Unlearn |          |     |          |      |       |               |
rence,Italy.AssociationforComputationalLinguis-
| dataset | bias | in natural | language |     | inference | by fitting |     |     |     |     |     |     |

tics.
| theresidual. |     | InProceedingsofthe2ndWorkshopon |     |     |     |     |     |     |     |     |     |     |

Deep Learning Approaches for Low-Resource NLP HaleyLepp.2019. Pardontheinterruption: Automatic
(DeepLo2019),pages132–142,HongKong,China. analysis of gender and competitive turn-taking in
AssociationforComputationalLinguistics. united states supreme court hearings. In Proceed-
ingsofthe2019WorkshoponWideningNLP,pages
| Peter Henderson, |     | Koustuv |     | Sinha, | Nicolas | Angelard- |     |     |     |     |     |     |

143–145,Florence,Italy.AssociationforComputa-
Gontier,NanRosemaryKe,GenevieveFried,Ryan

| Lowe,          | and | Joelle   | Pineau. | 2018.    | Ethical        | challenges |     |     |     |     |     |     |

| in data-driven |     | dialogue |         | systems. | In Proceedings | of         |     |     |     |     |     |     |
JiweiLi,MichelGalley,ChrisBrockett,JianfengGao,
AAAI/ACM
the 2018 Conference on AI, Ethics, and and Bill Dolan. 2016a. A diversity-promoting ob-
Society,AIES2018,NewOrleans,LA,USA,Febru- jective function for neural conversation models. In
ary02-03,2018,pages123–129.
|           |          |     |        |          |              |     | Proceedings | of           | the 2016 | Conference      |     | of the North  |

|           |          |     |        |          |              |     | American    | Chapter      | of       | the Association |     | for Computa-  |
| Alexander | Miserlis |     | Hoyle, | Lawrence | Wolf-Sonkin, |     |             |              |          |                 |     |               |
|           |          |     |        |          |              |     | tional      | Linguistics: | Human    | Language        |     | Technologies, |
HannaWallach,IsabelleAugenstein,andRyanCot-
|         |       |              |     |           |     |             | pages | 110–119, | San | Diego, California. |     | Association |

| terell. | 2019. | Unsupervised |     | discovery |     | of gendered |       |          |     |                    |     |             |
forComputa
| languagethroughlatent-variablemodeling. |     |          |        |         |     | InPro-    |          |               |     |                |     |             |

| ceedings                                | of  | the 57th | Annual | Meeting | of  | the Asso- |          |               |     |                |     |             |
|                                         |     |          |        |         |     |           | JiweiLi, | MichelGalley, |     | ChrisBrockett, |     | GeorgiosSp- |
ciationforComputationalLinguistics,pages1706–
|       |           |     |        |             |     |          | ithourakis,JianfengGao,andBillDolan.2016b. |     |        |              |        | A       |

| 1716, | Florence, |     | Italy. | Association | for | Computa- |                                            |     |        |              |        |         |
|       |           |     |        |             |     |          | persona-based                              |     | neural | conversation | model. | In Pro- |

ceedingsofthe54thAnnualMeetingoftheAssocia-
|        |         |      |          |            |     |          | tionforComputationalLinguistics(Volume1: |     |     |     |     | Long |

| Samuel | Humeau, | Kurt | Shuster, | Marie-Anne |     | Lachaux, |                                          |     |     |     |     |      |
Papers),pages994–1003,Berlin,Germany.Associ-
| and | Jason | Weston. | 2019. | Real-time | inference | in  |     |     |     |     |     |     |

multi-sentencetaskswithdeeppretrainedtransform- ationforComputa
ers. arXivpreprintarXiv:1905.01969.
|     |     |     |     |     |     |     | MargaretLi, | JasonWeston, |     | andStephenRoller.2019. |     |     |

Masahiro Kaneko and Danushka Bollegala. 2019. Acute-eval:Improveddialogueevaluationwithopti-
|                   |     |     |           |     |             |      | mizedquestionsandmulti-turncomparisons. |     |     |     |     | arXiv |

| Gender-preserving |     |     | debiasing | for | pre-trained | word |                                         |     |     |     |     |       |
preprintarXiv:1909.03087.
| embeddings. |     | In              | Proceedings | of                | the 57th | Annual |     |     |     |     |     |     |

| Meeting     | of  | the Association |             | for Computational |          | Lin-   |     |     |     |     |     |     |
guistics,pages1641–1650,Florence,Italy.Associa- Paul Pu Liang, Irene Mengze Li, Emily Zheng,
tionforComputationalLinguistics. Yao Chong Lim, Ruslan Salakhutdinov, and Louis-
|     |     |     |     |     |     |     | Philippe | Morency. | 2020. | Towards |     | debiasing sen- |

Dongyeop Kang, Varun Gangal, and Eduard Hovy. tence representations. In Proceedings of the 58th
2019. (male, bachelor) and (female, Ph.D) have Annual Meeting of the Association for Computa-
| different |               |     |     |            |           |         | tionalLinguistics, |     | pages5502–5515, |     |     | Online.Asso- |

|           | connotations: |     |     | Parallelly | annotated | stylis- |                    |     |                 |     |     |              |
tic language dataset with multiple personas. In ciationforComputa
| Proceedings |     | of the | 2019 | Conference | on  | Empirical |     |     |     |     |     |     |

Methods in Natural Language Processing and the Haochen Liu, Jamell Dacon, Wenqi Fan, Hui Liu, Zi-
9thInternationalJointConferenceonNaturalLan- tao Liu, and Jiliang Tang. 2019. Does gender mat-
guage Processing (EMNLP-IJCNLP), pages 1696– ter? Towards fairness in dialogue systems. CoRR,
abs/1910.10486.
1706,HongKong,China.AssociationforComputa-

|     |     |     |     |     |     |     | Pierre-Emmanuel |     | Mazare´, | Samuel | Humeau, | Martin |

Yuta Kikuchi, Graham Neubig, Ryohei Sasano, Hi- Raison, and Antoine Bordes. 2018. Training
royaTakamura,andManabuOkumura.2016. Con- millions of personalized dialogue agents. arXiv
trolling output length in neural encoder-decoders. preprintarXiv:1809.01984.
8183

Jack Merullo, Luke Yeh, Abram Handler, Alvin Gris- pages 48–53, Florence, Italy. Association for Com-
| som II, | Brendan | O’Connor, | and | Mohit | Iyyer. 2019. |     | putationalLinguistics. |     |     |     |     |     |     |

Investigatingsportscommentatorbiaswithinalarge
corpus of American football broadcasts. In Pro- Yusu Qian, Urwa Muaz, Ben Zhang, and Jae Won
ceedingsofthe2019ConferenceonEmpiricalMeth- Hyun. 2019. Reducing gender bias in word-level
odsinNaturalLanguageProcessingandthe9thIn- languagemodelswithagender-equalizinglossfunc-
ternational Joint Conference on Natural Language tion. InProceedingsofthe57thAnnualMeetingof
|            |                 |     |     |       |            |     | theAssociationforComputationalLinguistics: |     |     |     |     |     | Stu- |

| Processing | (EMNLP-IJCNLP), |     |     | pages | 6354–6360, |     |                                            |     |     |     |     |     |      |
Hong Kong, China. Association for Computational dentResearchWorkshop,pages223–228,Florence,
| Linguistics. |     |     |     |     |     |     | Italy.AssociationforComputationalLinguistics. |     |     |     |     |     |     |

Alexander Miller, Will Feng, Dhruv Batra, Antoine Abigail See, Stephen Roller, Douwe Kiela, and Ja-
Bordes, Adam Fisch, Jiasen Lu, Devi Parikh, and son Weston. 2019. What makes a good conversa-
JasonWeston.2017. ParlAI:Adialogresearchsoft- howcontrollableattributesaffecthumanjudg-
tion?
ware platform. In Proceedings of the 2017 Con- ments. In Proceedings of the 2019 Conference of
ferenceonEmpiricalMethodsinNaturalLanguage the North American Chapter of the Association for
Processing: System Demonstrations, pages 79–84, ComputationalLinguistics:HumanLanguageTech-
Copenhagen, Denmark. Association for Computa- nologies, Volume1(LongandShortPapers), pages

|     |     |     |     |     |     |     | 1702–1723, | Minneapolis, |     | Minnesota. |     | Association |     |

forComputa
| Nikita Nangia, |     | Clara Vania, | Rasika | Bhalerao, | and |     |     |     |     |     |     |     |     |

Samuel R. Bowman. 2020. Crows-pairs: A chal- SimaSharifirad,AlonJacovi,IsraelBarIlanUnivesity,
lengedatasetformeasuringsocialbiasesinmasked and Stan Matwin. 2019. Learning and understand-
| languagemodels. |            | arXivpreprintarXiv:2010.00133. |          |     |            |     | different                     |            |     |           |                    |                |     |

|                 |            |                                |          |     |            |     | ing                           | categories |     | of sexism |                    | using convolu- |     |
|                 |            |                                |          |     |            |     | tionalneuralnetwork’sfilters. |            |     |           | InProceedingsofthe |                |     |
| Oluwatobi       | O Olabiyi, | Anish                          | Khazane, |     | and Erik T |     |                               |            |     |           |                    |                |     |
2019WorkshoponWideningNLP,pages21–23.
| Mueller.2018. |     | Apersona-basedmulti-turnconver- |     |     |     |     |     |     |     |     |     |     |     |

sation model in an adversarial learning framework. Sima Sharifirad and Stan Matwin. 2019. Using
In201817thIEEEInternationalConferenceonMa- attention-based bidirectional LSTM to identify dif-
| chine Learning |     | and Applications |     | (ICMLA), | pages |     |                   |     | offensive |     |          |          |     |

|                |     |                  |     |          |       |     | ferent categories |     | of        |     | language | directed | to- |
489–494.IEEE.
|     |     |     |     |     |     |     | wardfemalecelebrities. |     |     | InProceedingsofthe2019 |     |     |     |

WorkshoponWideningNLP,pages46–48.
| Cathy O’Neil.     | 2016.          | Weapons           |            | of math     | destruction: |       |               |            |          |             |            |              |         |

| How big           | data           | increases         | inequality | and         | threatens    |       |               |            |          |             |            |              |         |
|                   |                |                   |            |             |              | Emily | Sheng,        | Kai-Wei    | Chang,   | Premkumar   |            | Natarajan,   |         |
| democracy.        | BroadwayBooks. |                   |            |             |              |       |               |            |          |             |            |              |         |
|                   |                |                   |            |             |              |       | and Nanyun    | Peng.      | 2019.    | The         | woman      | worked       | as      |
|                   |                |                   |            |             |              |       | a babysitter: | On         | biases   | in language |            | generation.  | In      |
| Shereen           | Oraby,         | Lena              | Reed,      | Shubhangi   | Tandon,      |       |               |            |          |             |            |              |         |
|                   |                |                   |            |             |              |       | Proceedings   | of         | the 2019 | Conference  |            | on Empirical |         |
| TS Sharath,       | Stephanie      |                   | Lukin,     | and Marilyn | Walker.      |       |               |            |          |             |            |              |         |
|                   |                |                   |            |             |              |       | Methods       | in Natural | Language |             | Processing |              | and the |
| 2018. Controlling |                | personality-based |            | stylistic   | varia-       |       |               |            |          |             |            |              |         |
9thInternationalJointConferenceonNaturalLan-
| tionwithneuralnaturallanguagegenerators. |     |     |     |     | arXiv |     |     |     |     |     |     |     |     |

preprintarXiv:1805.08352. guage Processing (EMNLP-IJCNLP), pages 3398–
3403,HongKong,China.AssociationforComputa-

| Debra L | Oswald. | 2008. | Gender | stereotypes | and |     |     |     |     |     |     |     |     |

women’sreportsoflikingandabilityintraditionally
|                                  |     |     |     |              |     | Kurt | Shuster,          | Samuel | Humeau,            |     | Antoine | Bordes, | and    |

| masculineandfeminineoccupations. |     |     |     | Psychologyof |     |      |                   |        |                    |     |         |         |        |
|                                  |     |     |     |              |     |      | JasonWeston.2018. |        | Engagingimagechat: |     |         |         | Model- |
WomenQuarterly,32(2):196–203.
|                    |           |            |               |               |           |         | ingpersonalityingroundeddialogue. |       |            |           |      | arXivpreprint |         |

| Jahna Otterbacher, |           | Alessandro | Checco,       | Gianluca      | De-       |         | arXiv:1811.00945.                 |       |            |           |      |               |         |
| martini,           | and Paul  | Clough.    | 2018.         | Investigating | user      |         |                                   |       |            |           |      |               |         |
|                    |           |            |               |               |           | Gabriel | Stanovsky,                        |       | Noah       | A. Smith, | and  | Luke          | Zettle- |
| perception         | of gender | bias       | in image      | search:       | the role  |         |                                   |       |            |           |      |               |         |
|                    |           |            |               |               |           |         | moyer.                            | 2019. | Evaluating | gender    | bias | in            | machine |
| of sexism.         | In        | The 41st   | International |               | ACM SIGIR |         |                                   |       |            |           |      |               |         |
ConferenceonResearch&DevelopmentinInforma- translation. InProceedingsofthe57thAnnualMeet-
tionRetrieval,pages933–936.ACM. ing of the Association for Computational Linguis-
|     |     |     |     |     |     |     | tics, pages | 1679–1684, |     | Florence, | Italy. | Association |     |

Ji Ho Park, Jamin Shin, and Pascale Fung. 2018. Re- forComputa
| ducing | gender | bias in | abusive | language | detection. |     |     |     |     |     |     |     |     |

In Proceedings of the 2018 Conference on Em- JenniferRSteeleandNaliniAmbady.2006. “Mathis
theeffectofgenderprimingonwomen’sat-
| pirical | Methods | in Natural | Language |     | Processing, |     | hard!” |     |     |     |     |     |     |

pages 2799–2804, Brussels, Belgium. Association titudes. JournalofExperimentalSocialPsychology,
| forComputationalLinguistics. |     |     |     |     |     |     | 42(4):428–436. |     |     |     |     |     |     |

Yusu Qian. 2019. Gender stereotypes differ between P. Stock and M. Cisse´. 2017. Convnets and im-
male and female writings. In Proceedings of the agenet beyond accuracy: Explanations, bias de-
57th Annual Meeting of the Association for Com- tection, adversarial examples and model criticism.
| putationalLinguistics: |     |     | StudentResearchWorkshop, |     |     |     | arXiv:1711.11443v2. |     |     |     |     |     |     |

8184

Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang, Jieyu Zhao, Tianlu Wang, Mark Yatskar, Ryan Cot-
Mai ElSherief, Jieyu Zhao, Diba Mirza, Elizabeth terell, Vicente Ordonez, and Kai-Wei Chang. 2019.
Belding, Kai-Wei Chang, and William Yang Wang. Genderbiasincontextualizedwordembeddings. In
2019. Mitigating gender bias in natural language Proceedings of the 2019 Conference of the North
processing: Literature review. In Proceedings of American Chapter of the Association for Computa-
the57thAnnualMeetingoftheAssociationforCom- tional Linguistics: Human Language Technologies,
putational Linguistics, pages 1630–1640, Florence, Volume1(LongandShortPapers),pages629–634,
Italy.AssociationforComputationalLinguistics. Minneapolis, Minnesota.AssociationforComputa-

| Jack Urbanek, |     | Angela Fan, | Siddharth |     | Karamcheti, |     |     |     |     |     |     |     |

Saachi Jain, Samuel Humeau, Emily Dinan, Tim Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Or-
Rockta¨schel, Douwe Kiela, Arthur Szlam, and Ja- donez, and Kai-Wei Chang. 2017. ”men also like
son Weston. 2019. Learning to speak and act in shopping: Reducing gender bias amplification us-
a fantasy text adventure game. In Proceedings ingcorpus-levelconstraints”. InProceedingsofthe
|             |            |     |              |     |         |     | 2017 | Conference | on Empirical | Methods |     | in Natu- |

| of the 2019 | Conference |     | on Empirical |     | Methods | in  |      |            |              |         |     |          |
Natural Language Processing and the 9th Interna- ralLanguageProcessing,pages2979–2989,Copen-
tional Joint Conference on Natural Language Pro- hagen, Denmark. Association for Computational
| cessing          | (EMNLP-IJCNLP), |             | pages     | 673–683,      |     | Hong  | Linguistics.             |             |            |                        |         |      |

| Kong, China.     |                 | Association | for       | Computational |     | Lin-  |                          |             |            |                        |         |      |
| guistics.        |                 |             |           |               |     |       | Jieyu Zhao,              | Tianlu      | Wang, Mark | Yatskar,               | Vicente | Or-  |
|                  |                 |             |           |               |     |       | donez,                   | and Kai-Wei | Chang.     | 2018a.                 | Gender  | bias |
|                  |                 |             |           |               |     |       | incoreferenceresolution: |             |            | Evaluationanddebiasing |         |      |
| Paul Verhaeghen, |                 | Shelley     | N Aikman, |               | and | Ana E |                          |             |            |                        |         |      |
Van Gulick. 2011. Prime and prejudice: Co- methods. In Proceedings of the 2018 Conference
occurrence in the culture as a source of automatic of the North American Chapter of the Association
stereotype priming. British Journal of Social Psy- for Computational Linguistics: Human Language
chology,50(3):501–518. Technologies, Volume 2 (Short Papers), pages 15–
|              |     |          |              |     |        |     | 20, New | Orleans, | Louisiana. | Association | for | Com- |

| Tianlu Wang, | Xi  | Victoria | Lin, Nazneen |     | Fatema | Ra- |         |          |            |             |     |      |
puta
| jani, Bryan | McCann, | Vicente |     | Ordonez, | and | Caim- |     |     |     |     |     |     |

ing Xiong. 2020. Double-hard debias: Tailoring JieyuZhao,YichaoZhou,ZeyuLi,WeiWang,andKai-
word embeddings for gender bias mitigation. In Wei Chang. 2018b. Learning gender-neutral word
Proceedingsofthe58thAnnualMeetingoftheAsso- embeddings. In Proceedings of the 2018 Confer-
ciationforComputationalLinguistics,pages5443– ence on Empirical Methods in Natural Language
5453, Online. Association for Computational Lin- Processing, pages 4847–4853, Brussels, Belgium.
| guistics. |     |     |     |     |     |     | AssociationforComputationalLinguistics. |     |     |     |     |     |

Adina Williams. 2018. Representing Relationality: Pei Zhou, Weijia Shi, Jieyu Zhao, Kuan-Hao Huang,
MEG Studies on Argument Structure. Ph.D. thesis, Muhao Chen, Ryan Cotterell, and Kai-Wei Chang.
NewYorkUniversity. 2019. Examining gender bias in languages with
|     |     |     |     |     |     |     | grammatical |     | gender. | In Proceedings |     | of the |

Adina Williams, Damian Blasi, Lawrence Wolf- 2019 Conference on Empirical Methods in Natu-
Sonkin, Hanna Wallach, and Ryan Cotterell. 2019. ral Language Processing and the 9th International
Quantifyingthesemanticcoreofgendersystems. In Joint Conference on Natural Language Processing
Proceedings of the 2019 Conference on Empirical (EMNLP-IJCNLP), pages 5275–5283, Hong Kong,
Methods in Natural Language Processing and the China.AssociationforComputa
9thInternationalJointConferenceonNaturalLan-
guage Processing (EMNLP-IJCNLP), pages 5733– RanZmigrod,SebastianJ.Mielke,HannaWallach,and
5738,HongKong,China.AssociationforComputa- RyanCotterell.2019. Counterfactualdataaugmen-
tationformitigatinggenderstereotypesinlanguages

|     |     |     |     |     |     |     | with | rich morphology. | In  | Proceedings | of  | the 57th |

Adina Williams, Ryan Cotterell, Lawrence Wolf- Annual Meeting of the Association for Computa-
Sonkin, Damia´n Blasi, and Hanna Wallach. tionalLinguistics,pages1651–1661,Florence,Italy.
2020. On the relationships between the gram- AssociationforComputa
| matical   | genders    | of inanimate |        | nouns | and their | co-      |     |     |     |     |     |     |

| occurring | adjectives | and          | verbs. | arXiv |           | preprint |     |     |     |     |     |     |
arXiv:2005.01204.
| Saizheng Zhang,                       |          | Emily Dinan,       | Jack          | Urbanek,          |          | Arthur |     |     |     |     |     |     |

| Szlam,DouweKiela,andJasonWeston.2018. |          |                    |               |                   |          | Per-   |     |     |     |     |     |     |
| sonalizing                            | dialogue | agents:            | I             | have a            | dog,     | do you |     |     |     |     |     |     |
| have pets                             | too?     | In Proceedings     |               | of                | the 56th | An-    |     |     |     |     |     |     |
| nual Meeting                          |          | of the Association |               | for Computational |          |        |     |     |     |     |     |     |
| Linguistics                           | (Volume  | 1:                 | Long Papers), |                   | pages    | 2204–  |     |     |     |     |     |     |
| 2213, Melbourne,                      |          | Australia.         | Association   |                   | for      | Com-   |     |     |     |     |     |     |
puta
8185

A Appendix
A.1 DiscussionofGenerationQuality
Generality of Gendered Words. The gendered
word lists used may not be comprehensive (Zhao
et al., 2018a,b; Hoyle et al., 2019). For example,
theydonotincludehagorwench,whicharecom-
moninLIGHT.Further,amorecontinuousrepre-
sentationofgendershouldbeusedinthefuture.
MoreFine-GrainedControl. Wepresentanef-
fective method to control the quantity of gen-
dered words generated by manipulating control
bins. This technique is general and could be used
tocontrolotherpropertiesofgeneratedutterances.
For example, a sexism or bias classifier could be
usedinsteadofthegenderedwordlist.
QualityofGeneratedDialogue. Generativedi-
aloguemodelsarepronetooverusefrequentwords
and produce generic utterances, the so-called I
don’t know problem (Li et al., 2016a). We also
observetheseeffectswhichcanaffectbias.
Model Top20generatedwords
Baseline sorry,hear,not,what,glad,doing,don,king*,
thank, sure, will, your, can, much, do, know,
but,knight*,blacksmith,going
ALL sorry, hear, sure, not, what, help, doing, your,
course,trying,glad,thank,queen*,don,good,
king*,but,yes,know,sir*
ALLF0M0 sorry,hear,sure,what,not,doing,glad,thank,
your, yes, course, but, don, do, know, help,
have,enjoying,fool,much
ALLF0M+ sorry,hear,help,trying,sure,good,king*,sir*,
not,your,day,course,father*,he*,don,thank,
happy,guard*,glad,have
ALLF+M0 sorry, hear, queen*, sure, miss*, not, your,
thank, how, hello, today, guard*, she*, yes,
course,kind,woman*,help,glad,what
ALLF+M+ sorry, queen*, hear, guard*, help, trying, your,
sure, good, course, day, knight*, not, protect,
yes,friend,king*,woman*,she*,thank
Table 8: Genderedness bins control the gendered-
ness of generated text. The top 20 words (test set)
withstopwordsremoved. *indicatesgenderednouns.
8186

DataSplit: F0M0 F0M+ F+M0 F+M+ All
%gend. %male F1 %gend. %male F1 %gend. %male F1 %gend. %male F1 F1
Model words bias score words bias score words bias score words bias score score
GoldLbl 0 0 - 4.11 100 - 4.03 0 - 6.67 50.71 - -
Baseline 2.37 88.39 11.24 3.66 90.26 11.77 2.44 77.99 11.54 3.05 80.05 11.43 11.42
ConvAI2FT 0.79 71.09 7.78 1.1 78.31 7.94 1.35 51.6 8.75 1.97 67.23 8.99 7.95
RedditBase 2.18 73.68 9.93 3.03 81.78 11.54 2.81 52.99 10.99 3.94 63.16 12.61 10.57
CDA 0.88 71.03 11.63 1.38 68.57 11.7 1.2 56.18 11.43 1.17 58.01 11.12 11.62
Pos.Data 2.76 82.44 10.46 3.68 86.43 10.07 4.59 72.1 10.07 4.43 86.5 9.88 10.44
BiasCtrl 0.14 68.75 10.72 5.83 98.08 13.01 4.8 2.69 10.84 4.05 45.86 11.35 11.38
ALL 0.14 64.19 11.72 6.59 97.94 12.77 5.84 7.13 11.28 8.81 50.94 12.22 11.99
Table9:Wecomparetheperformanceofvariousbiasmitigationmethods—CounterfactualDataAugmentation
(CDA),Positive-BiasDataCollection(Pos. Data),BiasControlModel(BiasCtrl),andcombiningthesemethods
(ALL)—onthetestset,splittingthetestsetacrossthefourgenderednessbins: F0/+ M0/+ . X0indicatesthereareno
+
X-genderedwordsinthegoldresponse, whileX indicatesthatthereisatleastone. Wemeasurethepercentof
genderedwordsinthegeneratedutterances(%gend. words)andthepercentofmalebias(%malebias),i.e. the
percent of male-gendered words among all gendered words generated. While each of these methods yield some
improvement,combiningallofthesemethodsinoneyieldsthebestcontroloverthegenderednessoftheutterances
whileimprovingtheF1-score.
DataSplit: F0M0 F0M+ F+M0 F+M+ All
%gend. %male F1 %gend. %male F1 %gend. %male F1 %gend. %male F1 F1
Model words bias score words bias score words bias score words bias score score
GoldLbl 0 0 - 4.11 100 - 4.03 0 - 6.67 50.71 - -
Baseline 2.37 88.39 11.24 3.66 90.26 11.77 2.44 77.99 11.54 3.05 80.05 11.43 11.42
ALLF0M0 0.14 64.19 11.72 0.24 80.11 11.51 0.22 25.0 11.63 0.23 81.58 10.72 11.61
ALLF0M+ 6.47 97.97 9.58 6.59 97.94 12.77 7.22 96.33 10.0 6.27 97.52 12.21 10.6
ALLF+M0 4.77 11.66 10.27 5.12 15.84 10.94 5.84 7.13 11.28 5.03 13.64 11.23 10.57
ALLF+M+ 9.53 53.34 8.89 9.6 55.35 11.19 9.42 48.65 10.5 8.81 50.94 12.22 9.79
Table10:PerformanceoftheALLdebiasingmodelcontrolledbyindicatingspecificbinsforallexamplesattest
time. Wereportresultsforeachpossibleconditioningbinchoice. Acrossbins,themodelmaintainsperformance
(F1)whilstradicallychangingthegenderednessofthelanguagegenerated.
PersonaExample(OriginalLIGHTDataset)
son: Iamspoiledandrich.Ienjoyrunninginthecastle.Ilikehideandseek.
men: Iamanaveragemaninthevillage.IdowhateverworkthatmyKingrequiresmetodo.Atnight,Ispend
mytimeinthelocalpubwithmyfellowmen.
farmerBob: Iwasborninapoorvillage.Ieatwhatwegrow.Ilovebeingclosetotheearth.
father: Iamarolemodelformychildren.IprovideforthefamilywithmeatandIkeeparoofovertheirheads.I
amstabilitytothefamily,andkeepthingstogetherandprovidesafetytomychildren.
husband: Itrytobegoodtomywife.Iwanttoprovideformyfamily.Itrytobestrong.
Table11: ExamplesofmalegenderbiasedpersonaswrittenforgenderedcharactersintheLIGHTdataset.
8187

GenerationExamples
Bin F0M+
Context [P1:] Yes,wemustgetstartedbutwhilewepaint,itwouldnotdoanyharmtokeepaneyeout
forpassagesandsecrets.
[P2:] Great!
[P1:] Iwillstartonthissideifyoulike.Iwillstarttapingtheareaforus.
[P2:] Ok,Ihavethisareacovered.Youdothiswithalevelofenviableprofessionalism.
Baseline: thankyousomuchforyourkindwords.
ALL: thankyou,sir.
Gold: Iamjustaworkerwithlotsofpatience. Butcomehereandsee, IbelieveImayhavefound
something.
Bin F0M+
Context [P1:] Justcalmdownyoumadfellow.
[P2:] Iamgoingtoslityourthroat,nobodyattacksme
Baseline: iwillkillyoufirst.
ALL: i’mjusttryingtoprotecttheking.
Gold: Youtooviolent.Letscallatruce
Bin F+M0
Context [P1:] youkilledmymotherandyouareabouttomarrythiswomantoreplaceher
[P2:] Thisisyournewmotherandyoumustrespecther!
Baseline: iamsorryfather
ALL: iamsorrymother
Gold: Heylady,howareyoudoing.
Bin F+M0
Context [P1:] Ithinkthatfearmixeswithmakinganypersonbrave.Therearesomethatarebraver
[P2:] Iheardthat”fearisthemindkiller”.Thankyouforkeepingussafe.
[P1:] Ifyoudonothavefearinsideyou,youwilldosomethingfoolishtryingtobebrave.
[P2:] Youaremyhero!
Baseline: youareabraveman!
ALL: youareabravewoman!
Gold: Youaresweet!
Table12: Additionalexamplegenerationsfromthebaselinemodelandtheproposeddebiasedmodels. Weshow
examplesforconditioningonboththeF + M0andF + M0bins.
8188

---
**Source PDF:** `2022_13_article.pdf`
