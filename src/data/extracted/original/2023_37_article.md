|     |     |        | Automatic |                   |            | Multi-Label |          | Prompting:      |                |     |     |     |     |

|     |     | Simple |           | and Interpretable |            |             | Few-Shot |                 | Classification |     |     |     |     |
|     |     |        | HanWang1  |                   | ,CanwenXu2 |             |          | ,JulianMcAuley2 |                |     |     |     |     |
|     |     |        |           |                   | ∗          |             |          | ∗†              |                |     |     |     |     |
1NewYorkUniversity,2UniversityofCalifornia,SanDiego
1hwang@nyu.edu,2{cxu,jmcauley}@ucsd.edu
|     |     | Abstract |     |     |     |     | tokens,andthenusethepretrainedlanguagemodel |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ------------------------------------------- 
tofillthesemaskedtokens,andfinallythetokens
Prompt-basedlearning(i.e.,prompting)isan
filledintotheseslotsaremappedtothecorrespond-
emergingparadigmforexploitingknowledge
|         |     |              |          |     |        |     | ing    | labels | as the  | final | output. | In prompting, | the   |

| learned | by  | a pretrained | language |     | model. | In  |        |        |         |       |         |               |       |
|         |     |              |          |     |        |     | design | of     | prompts | often | plays   | an important  | role. |
thispaper,weproposeAutomaticMulti-Label
Prompting (AMuLaP), a simple yet effective Many attempts have been made in this emerging
directionofpromptengineering(Shinetal.,2020;
methodtoautomaticallyselectlabelmappings
for few-shot text classification with prompt- Gaoetal.,2021). Meanwhile,findingagoodmap-
ing. Our method exploits one-to-many label ping from the original task labels to tokens (i.e.,
| mappings |     | and a statistics-based |     | algorithm |     | to  |     |     |     |     |     |     |     |
| -------- | --- | ---------------------- | --- | --------- | --- | --- | --- 
labelengineering)isalsocriticaltofew-shotper-
| select | label                             | mappings | given | a prompt |     | tem- |           |             |          |          |          |                |     |

|        |                                   |          |       |          |     |      | formance, |             | as found | in       | Schick   | et al. (2020); | Gao |
| plate. | OurexperimentsdemonstratethatAMu- |          |       |          |     |      |           |             |          |          |          |                |     |
|        |                                   |          |       |          |     |      | et        | al. (2021). |          | However, | manually | assigning      | the |
LaPachievescompetitiveperformanceonthe
labelmappingrequireshumanexpertisewithtrial
GLUEbenchmarkwithouthumaneffortorex-
|     |     |     |     |     |     |     | anderror. |     | Onemayarguethatthesameeffortcan |     |     |     |     |

ternalresources.1
|     |     |     |     |     |     |     | be  | used | to label | more | supervised | data for | a con- |

## 1 Introduction ventionaldeeplearningpipeline. Thus,anefficient
automaticlabelmappingmethodisdesirable.
| Since the | release | of GPT-3 |         | (Brown        | et al., | 2020), |     |               |        |        |        |                 |      |

|           |         |          |         |               |         |        |     | In this       | paper, | we aim | to     | design a method | that |
| several   | studies | have     | focused | on exploiting |         | pre-   |     |               |        |        |        |                 |      |
|           |         |          |         |               |         |        | can | automatically |        | find   | a good | label mapping   | to   |
trainedlanguagemodelswithonlyafewtraining
examples (Brown et al., 2020; Gao et al., 2021; save human effort from label engineering. We
proposeAutomaticMulti-LabelPrompting(AMu-
| Shin et | al., 2020). | These | works | demonstrate |     | the |       |     |        |               |     |                  |     |

|         |             |       |       |             |     |     | LaP), | a   | simple | yet effective |     | method to tackle | the |
potentialofusingnaturallanguagepromptstoen-
couragethemodeltorecallsimilarpatternsinits labelselectionproblemforfew-shotclassification.
training corpus and thus make accurate predic- AMuLaPisaparameter-freestatisticaltechnique
thatcanidentifythelabelpatternsfromafew-shot
| tions. This | setting | of  | few-shot | learning |     | is closer |          |     |           |          |     |           |        |

|             |         |     |          |          |     |           | training |     | set given | a prompt |     | template. | AMuLaP |
tohowhumanslearntosolveatask,oftenwithout
many examples as in a traditional deep learning exploitsmultiplelabelstosuppressthenoiseand
inherentlyextendthetrainingsetforprompt-based
| paradigm. | Theuseofpromptscanstrengthenthe |     |     |     |     |     |              |     |          |     |      |                |       |

|           |                                 |     |     |     |     |     | fine-tuning. |     | Compared |     | with | a hand-crafted | label |
explicitconnectionbetweeninputandoutput,help-
ingthemodelexploittheknowledgelearnedfrom mapping and previous works on automatic label
pretraining in a better way. Furthermore, recent mapping (Schick et al., 2020; Gao et al., 2021),
|               |     |              |     |          |     |         | AMuLaP |     | achieves | competitive |     | performance | de- |

| works (Schick |     | and Schütze, |     | 2021a,b; | Gao | et al., |        |     |          |             |     |             |     |
spitebeingsimpleranddoesnotrequireaccessto
2021)showthatpromptscanalsohelpthemodel
generalizebetterinfine-tuning. theweightsofthebackbonemodel,orfinetunean
externalpretrainedlanguagemodelforsearching
Prompt-basedlearning(i.e.,prompting)aimsto
|                |     |            |     |          |       |      | labelmapping. |     |     | Weconductextensiveexperiments |     |     |     |

| use a template |     | to convert | the | original | input | into |               |     |     |                               |     |     |     |
a prompt-based input with some unfilled masked and demonstrate the effectiveness of our method
|     |     |     |     |     |     |     | undermultiplesettings. |     |     |     | Moreover,weattemptto |     |     |

∗Equalcontribution. scaleAMuLaPwithdifferentsizesofthetraining
†Towhomcorrespondenceshouldbeaddressed.
|      |         |           |                        |     |     |     | set | and | find AMuLaP |     | to work | surprisingly | well |

| 1The | code is | available | at https://github.com/ |     |     |     |     |     |             |     |         |              |      |
HanNight/AMuLaP. even with one or two shots. We further analyze
5483
Proceedingsofthe2022ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
HumanLanguageTechnologies,pages5483-5492
July10-15,2022©2022AssociationforComputationalLinguistics

whydoesAMuLaPworkanddiscusstheprosand bymanuallywritingprompttemplatesandshows
consofpromptingasanewparadigm. thatalargelanguagemodelwithmultitasktraining
cangeneralizetounseentasks.
## 2 RelatedWork
Inparallelwithtext-based
ContinuousPrompts
|                 |                         |     |     | discrete prompts, | there is | also a line of | work fo- |

| DiscretePrompts | ThereleaseofGPT-3(Brown |     |     |                   |          |                |          |
etal.,2020)hasledtointerestinprompting,anew cusedontuningonlyafractionofparametersofan
waytoleveragepretrainedlanguagemodels(PLM). LMwiththehelpofcontinuousprompts(i.e.,soft
|     |     |     |     | prompts). | Zhongetal.(2021)andQinandEisner |     |     |

Brownetal.(2020)proposesanintuitivein-context
(2021)proposecontinuouspromptsforknowledge
learningparadigmbyconcatenatingafewinputand
outputexamplesandfeedingthemtothelanguage probing by tuning some trainable vectors in the
|     |     |     |     | input sequence | while fixing | the rest of | the input. |

modelandletthemodelautoregressivelygenerate
LiandLiang(2021)appliesasimilarmethodfor
| answersfornewexamples. |     | Recentworks(Petroni |     |     |     |     |     |

etal.,2019;Davisonetal.,2019;Jiangetal.,2020) naturallanguagegenerationandachievescompara-
designpromptstoprobethefactualandcommon- bleperformancetofine-tuningwhileupdatingonly
|                 |         |               |        | 0.1%ofmodelparameters. |     | Lesteretal.(2021)re- |     |

| sense knowledge | encoded | within a PLM. | Recent |                        |     |                      |     |
vealsthatprompttuningismorecompetitivewhen
| works (Schick | and Schütze, | 2021a,b; | Gao et al., |     |     |     |     |

2021) demonstrate that even smaller PLMs have scaledupandcanachieveidenticalperformanceto
conventionalfine-tuningwhenthemodelislarge
| similar | few-shot learning | capacity. | Le Scao and |     |     |     |     |

enough. Guoetal.(2021)introducesQ-Learning
Rush(2021)analyzestheeffectofpromptingand
concludesthatasinglepromptmaybeworth100 to optimize the soft prompt. Notably, different
fromdiscreteprompting,theseworksoftenuseall
trainingexamplesinfine-tuning.
|         |             |           |         | training data | to update model | weights. | Different |

| Instead | of manually | designing | prompts |               |                 |          |           |
fromtheseworks,AMuLaPisadiscreteprompting
| (i.e., prompt | engineering), | some | recent stud- |     |     |     |     |

ies also explore automatic prompt generation. method that has better interpretability and works
wellinthefew-shotsetting.
| PETAL      | (Schick et al., | 2020) augments | Pattern  |     |     |     |     |

| Exploiting | Training (PET,  | Schick and     | Schütze, |     |     |     |     |
## 3 PromptingforFew-ShotClassification
2021a,b)withautomaticallyidentifiedlabelwords;
Gao et al. (2021) uses re-ranking to find the best WefollowthesetupinLM-BFF(Gaoetal.,2021)
labelwordsbyfine-tuningaRoBERTamodelon forfew-shottextclassification. Givenapretrained
thecandidatessearchedbyRoBERTa,andusingan language model , a task and its defined label
|     |     |     |     |     | L   | D   |     |
| --- | --- 
external generation model for data augmentation space , we have n training examples per class
Y
of prompt templates; AutoPrompt (Shin et al., forthetrainingset . AspointedoutinPerez
train
D
2020) uses a gradient-based search to determine etal.(2021),usingthefulldevelopmentsetmaybe
both prompts and label words. However, these misleadingtoclaimafew-shotsetting. Thus, we
methodsrequireparameterupdateswithgradient useafew-shotdevelopmentsetwiththesamesize
descent,whichisinfeasiblewithoutaccesstothe as the training set (i.e., = ), to be
|     |     |     |     |     | |D  | train | |D dev | |   |

modelweights(e.g.,GPT-3). PETanditsvariants consistentwithGaoetal.(2021)andconstitutea
also require a large unlabeled set and need to “truefew-shot”setting(Perezetal.,2021).
be fine-tuned multiple times. AutoPrompt uses For an input example x (a single sentence or
discretizationtechniquestoapproximatelymapa a sentence pair), we first use a task-specific tem-
toconvertittox,
continuousvectorbacktotokensinthevocabulary plate ′ atokensequencewith
T
(i.e., “vocablization”). These searched prompts a[MASK]token. Wethenmaptheoriginallabel
and labels are often uninterpretable by humans. spacetoasetofselectedwordsfromthevocabu-
Different from these prior studies, our proposed lary,denotedas : ′ . Someexamplesof
|     |     |     |     |     | M Y → | V   |     |

AMuLaPisasimpleandinterpretablemethodfor and areshowninTable1. Notethatsincewe
T M
few-shot prompting that can work well with and focusonautomaticallyfindingthelabelmapping
without access to model weights. Concurrently ,weusethemanualtemplates fromGaoetal.
|     |     |     |     | M   |     | T   |     |
| --- | --- 
to our work, Hu et al. (2021) propose a method (2021)throughoutthispaper. Since istrainedto
L
that exploits an external knowledge base to find completethe[MASK]tokeninaninputsequence,
labelmapping. T0(Sanhetal.,2022;Bachetal., we can directly make zero-shot prediction of the
2022)constructsadatasetofdifferentNLPtasks probabilityofclassy bythemaskedlanguage
|     |     |     |     |     | ∈ Y |     |     |
| --- | --- 
5484

| Task | Template |     |     |     | Class      |     |     | Manual(2021) |     | LabelsselectedbyAMuLaP    |     |     |     |

|      |          |     |     |     | entailment |     |     | Yes          |     | Yes,Indeed,Also,Currently |     |     |     |
MNLI <S >?[MASK],<S > neutral Maybe Historically,Suddenly,Apparently,And
|     |     | 1   |     | 2   |               |     |     |     |     |                                  |     |     |     |

|     |     |     |     |     | contradiction |     |     | No  |     | No,However,Instead,Unfortunately |     |     |     |
positive
|       | <S  | >Itwas[MASK].  |     |     |                 |     |     | great     |     | great,perfect,fun,brilliant         |     |     |     |

| SST-2 |     | 1              |     |     | negative        |     |     |           |     |                                     |     |     |     |
|       |     |                |     |     |                 |     |     | terrible  |     | terrible,awful,disappointing,not    |     |     |     |
|       |     |                |     |     | entailment      |     |     | Yes       |     | Yes,Historically,Overall,Indeed     |     |     |     |
| QNLI  | <S  | 1 >?[MASK],<S  |     | 2   | >               |     |     |           |     |                                     |     |     |     |
|       |     |                |     |     | not_entailment  |     |     | No        |     | Well,First,However,Unfortunately    |     |     |     |
|       |     |                |     |     | entailment      |     |     | Yes       |     | Yes,Today,Specifically,Additionally |     |     |     |
| RTE   | <S  | 1 >?[MASK],<S  |     | 2   | >               |     |     |           |     |                                     |     |     |     |
|       |     |                |     |     | not_entailment  |     |     | No        |     | However,Ironically,Also,Indeed      |     |     |     |
|       |     |                |     |     | equivalent      |     |     | Yes       |     | </s>,Currently,Additionally,Today   |     |     |     |
| MRPC  | <S  | >[MASK],<S     |     | >   |                 |     |     |           |     |                                     |     |     |     |
|       |     | 1              |     | 2   | not_equivalent  |     |     | No        |     | However,Meanwhile,Overall,Finally   |     |     |     |
|       |     |                |     |     | equivalent      |     |     | Yes       |     | Or,So,Specifically,Actually         |     |     |     |
| QQP   | <S  | >[MASK],<S     |     | >   |                 |     |     |           |     |                                     |     |     |     |
|       |     | 1              |     | 2   | not_equivalent  |     |     | No        |     | Also,And,Finally,Well               |     |     |     |
|       |     |                |     |     | grammatical     |     |     | correct   |     | why,true,her,amazing                |     |     |     |
| CoLA  | <S  | >Thisis[MASK]. |     |     |                 |     |     |           |     |                                     |     |     |     |
|       |     | 1              |     |     | not_grammatical |     |     | incorrect |     | it,ridiculous,interesting,sad       |     |     |     |
Table1: ThemanualandautomaticallyselectedlabelsbyAMuLaP.Thetemplatesusedforpromptingarefrom
Gaoetal.(2021).
| modeling: |     |     |     |     |     |     |     | Similarly,ifweneedtofine-tune |     |     |     |     | withsuper- |

L
visedpairs,insteadofoptimizingthecross-entropy
|               | p(y x) | = p           | [MASK]  | =                   | (y)       | x           | .   |                    |     |                         |     |          |             |

|               |        |               |         |                     |           | ′           | (1) | loss between       | the | gold label              | and | a single | token,      |
|               | |      |               |         |                     | M         | |           |     |                    |     |                         |     |          |             |
|               |        |               |         |                     |           |             |     | we optimize        | the | loss between            | the | sum      | of the out- |
| Alternately,  |        | one(cid:0)can | further |                     | fine-tune | (cid:1)with | su- |                    |     |                         |     |          |             |
|               |        |               |         |                     |           | L           |     | putprobabilitiesof |     | (y)andthegoldlabelwitha |     |          |             |
| pervisedpairs |        | x             | , (y)   | toachieveevenbetter |           |             |     |                    |     | S                       |     |          |             |
|               |        | {             | ′ M     | }                   |           |             |     |                    |     |                         |     |          |             |
cross-entropyloss:
performance.
## 4 AutomaticMulti-LabelPrompting l = [1[y = yˆ] logp(y x)] (3)
|     |     |     |     |     |     |     |     | −   |     |     |     | ·   | |   |
| --- | --- | --- | --- | --- | --- | --- | --- 
x ∈XDtrainy
| 4.1 | ExploitingMultipleLabels |     |     |     |     |     |     |     |     | X∈Y |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | --- 
Selecting one label word can be insufficient for where yˆ is the ground truth label for the input x
some complicated tasks, as mentioned in Schick andp(y x)isdefinedinEquation2.
|
| etal.(2020). |     | Wealsoarguethatselectingonlyone |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------- | --- | --- | --- | --- | --- 
label (especially automatically) may bring noise. 4.2 AutomaticLabelSelection
| This      | can be | resolved                          | by  | introducing |     | multiple | la- |                          |     |                             |     |                   |     |

|           |        |                                   |     |             |     |          |     | Findingagoodlabelmapping |     |                             |     | isnon-trivial,es- |     |
| belwords. |        | Schicketal.(2020)usemultiplelabel |     |             |     |          |     |                          |     |                             | M   |                   |     |
|           |        |                                   |     |             |     |          |     | peciallywhen             |     | mapsanoriginallabeltoasetof |     |                   |     |
′
| combinationsforPET(SchickandSchütze,2021a) |          |      |             |     |     |         |     |                         | M     |                      |                     |       |         |

|                                            |          |      |             |     |     |         |     | labelwordsinsteadofone. |       |                      | Selectingagoodlabel |       |         |
| and                                        | ensemble | them | afterwards. |     | We  | instead | use |                         |       |                      |                     |       |         |
|                                            |          |      |             |     |     |         |     | mapping                 | often | requires significant |                     | human | effort, |
a straightforward sum to consider multiple label including domain knowledge and trial-and-error.
| wordswhenmakingpredictions. |     |     |     |     | Thisdesignhas |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ------------- | --- | --- 
Previously,SchickandSchütze(2021a,b)bothuse
| a similar | advantage |     | of  | exploiting |     | multiple | labels |              |       |          |       |        |        |

|           |           |     |     |            |     |          |        | hand-crafted | label | mappings | while | Schick | et al. |
withouttrainingandensemblingmultiplemodels.
(2020)exploresautomaticlabelmappingsearching
Insteadofaone-to-onemappingfromtheorig-
butitstillrequiresmanualpre-filteringandsignifi-
| inal            | label space |     | to     | , we   | map each | y           | to  |                                      |          |         |            |     |        |

|                 |             |     |        |        |          |             |     | cantlyunderperformsthemanualmapping. |          |         |            |     | (Gao   |
|                 |             |     | Y V    |        |          |             | ∈ Y |                                      |          |         |            |     |        |
| itslabelwordset |             |     | (y)ofk | words. |          | Wedenotethe |     |                                      |          |         |            |     |        |
|                 |             |     | S      |        |          |             |     | et al., 2021)                        | exploits | a large | pretrained |     | masked |
|                 |             |     |        | :      |          | k.          |     |                                      |          |         |            |     |        |
mapping function as ′ For class language model (RoBERTa, Liu et al., 2019) to
|     |     |     | M   |     | Y → | V   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- 
y ,thepredictedprobabilityiscalculatedas:
constructaprunedsetoflabelwordsandthende-
∈ Y
terminethefinalmappingbyfine-tuningonallof
|     | p(y x) | =   | p   | [MASK] | =   | v x | (2) |     |     |     |     |     |     |
| --- | ------ | --- | --- | ------ | --- | --- | --- 
′
|     | |   |     |     |     |     | |   |     | them and | selecting | the best | one | with | dev . We |

|     |     | v   | (y) |     |     |     |     |          |           |          |     |      | D        |
∈XS (cid:0) (cid:1) introduceanewselectionalgorithmforlabelmap-
Then,wecansimplymakepredictionsbyselecting pingthatachievescompetitiveresultscomparedto
| thelabelwiththelargestlikelihood. |     |     |     |     |     |     |     | previousefforts. |     |     |     |     |     |

5485

awful
| Label : Negative             |     |     |     |      | great      |     |       |     |     |     | Top-k token for  |     |

| Trainingsampleswith template |     |     |     | MLM  | p e r f e  | c t |       |     |     |     |                  |     |
|                              |     |     |     | Head |            |     |       |     |     |     | label: negative  |     |
|                              |     |     |     |      | te r r i b | le  | awful |     |     |     |                  |     |
[CLS] Noreasontowatch .It was [MASK] .[SEP] … awful t e rr i b le
|     |     |     |     |     |     |     | sum great |     |     |     | sort | a w f u l |

[CLS] It is a waste of tim e . It was [MASK] .[SEP] … … p e r f e c t t errible
|     |     |     |     |     |       | normalize | t e | r r i b le | …   |     |     | …   |

|     | …   |     |     |     | awful |           | …   |            |     |     |     | …   |
|     |     |     |     | MLM | great |           |     |            |     |     |     |     |
perfect
|     |     |     |     | Head | terrible |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | -------- | --- 
awful
…
|     |     |     |     |     |     |     | great |     | Assign each token to the class  |     |     |     |

perfect
|                                |     |     |     |      |           |     | terrible |     | with the highest probability |     |     |     |

|                                |     |     |     |      | awful     |     | …        |     |                              |     |     |     |
| Label : Positive               |     |     |     |      | great     |     |          |     |                              |     |     |     |
|                                |     |     |     | MLM  | p e r f e | c t |          |     |                              |     |     |     |
| Training samples with template |     |     |     | Head |           |     |          |     |                              |     |     |     |
te r r i b le
[ C L S ]   It  i s   w o r t h   w a tc h i n g  . I t   w a s   [ M A S K ]   . [ S E P ] … a w f u l g r e a t g r e a t
|     |     |     |     |     |     |     | s um g | r e a t |     |     | sort | p e r fe ct |

[ C L S ]   T h e   p l o t  i s   at tr a ct i v e .  I t   w a s   [ M A S K ]   . [ S E P ] … … p e r f e c t p e r fe ct
|     |     |     |     |     |        | nor | m alize t e | r r i b le |     |     |     | …                |

|     | …   |     |     |     |        |     |             |            | …   |     |     | …                |
|     |     |     |     |     | a wful |     | …           |            |     |     |     |                  |
|     |     |     |     | MLM | great  |     |             |            |     |     |     | Top-k token for  |
perfect
|     |     |     |     | Head | terrible |     |     |     |     |     |     | label: positive |

…
Figure1: TheillustrationofimplementingAMuLaPonabinarysentimentclassificationtask(SST-2). Eachtraining
samplewiththetask-specifictemplate(theunderlinedtext)isfedintoapretrainedlanguagemodel togetitsown
L
probabilitydistributionoverthevocabulary . Alltheobtainedprobabilitydistributionsaresummedbyclassand
V
normalizedtogettheprobabilitydistributionofeachclass. Theneachtokenin isassignedtotheclasswiththe
V
highestprobability(e.g.,thetokenterribleisassignedtotheclassnegative,thetokengreatisassignedtotheclass
| positive). | Finally,foreachclass,wechoosethetop-ktokensaslabelwords. |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------------------------------------------------------- | --- | --- | --- | --- | --- 
Weaimtoachievetwogoals: (1)Selectingthe averageofthepredictedprobabilitiesofthen
mostlikelylabelmappingbasedonthetraining examples to be z , where z is a vector over
|     |     |     |     |     |     |     |     |     | i   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- 
set. Forexample,inasentimentclassificationtask, thewholevocabulary.
| we would                                    | like to | see positive | words | in           | the label |     |          |         |                             |     |     |     |

|                                             |         |              |       |              |           | 2.  | Foreachy |         | ,initializeanemptycandidate |     |     |     |
| setofthe“positive”classwhilenegativewordsin |         |              |       |              |           |     |          | i       |                             |     |     |     |
|                                             |         |              |       |              |           |     |          | ˜(y ∈ Y |                             |     |     |     |
|                                             |         |              |       |              |           |     | tokenset | ).      |                             |     |     |     |
| thelabelsetofthe“negative”class.            |         |              |       | Asimplesolu- |           |     |          | S i     |                             |     |     |     |
tionistoselectthek
mostlikelytokenspredicted 3. Foreachv where isthevocabularyof
| forthe[MASK]tokeninthetrainingexamplesof |                                |      |          |       |          |     |          | ∈ V                            |     | V   |     |     |

|                                          |                                |      |          |       |          |     | themodel | ,weretrievev’sprobabilityvalue |     |     |     |     |
| eachclassy.                              | However,inpractice,wewouldfind |      |          |       |          |     | zv       | L                              |     |     |     |     |
|                                          |                                |      |          |       |          |     | fromz    | ofeachclass.                   |     |     |     |     |
|                                          |                                |      |          |       |          |     | i        | i                              |     |     |     |     |
| common                                   | words in                       | more | than one | label | set. For |     |          |                                |     |     |     |     |
example, if we simply take the 10 most likely to- 4. Weassignv tothemostlikelytokensetofthe
˜(y
kensfortheSST-2dataset(Socheretal.,2013),we m-thclass )wherem = argmax zv.
|     |     |     |     |     |     |     |     | m   |     |     |     | i i |
| --- | --- | --- | --- | --- | --- | --- 
S
| would find                                   | “good”        | in both | positive     | and  | negative |     |                                  |                   |     |     |            |        |

|                                              |               |         |              |      |          | 5.  | Fory i                           | ,wechoosethetop-k |     |     | tokensfrom |        |
| labelsets,althoughitisrankedsecondplaceinthe |               |         |              |      |          |     |                                  | ∈ Y               |     |     |            |        |
|                                              |               |         |              |      |          |     | ˜(y )withthelargestprobabilityzv |                   |     |     |            | andob- |
| positive                                     | set and ninth | in      | the negative | set. | Thus,    |     | i                                |                   |     |     |            | i      |
S
|         |         |           |     |            |      |     | tainthetruncatedwordset |     |     |     | (y ). |     |

| we want | to make | sure that | (2) | Each token | only |     |                         |     |     | S   | i     |     |
belongstoatmostonelabelsetwhereithasthe
TheentireworkflowisillustratedinFigure1.
| highest                                      | probability. | To  | ensure | this, we | have to |               |     |     |     |     |     |     |
| -------------------------------------------- | ------------ | --- | ------ | -------- | ------- | ------------- 
| iterateoverthevocabularyandcheckthatforevery |              |     |        |          |         | 5 Experiments |     |     |     |     |     |     |
token. Then,wecantruncatethecandidatesetsof
eachclassandselectthek mostlikelytokensfrom 5.1 ExperimentalSetting
eachset. Thetimecomplexityofthisalgorithmis Datasets Weevaluatesevenclassificationtasks
| O(k | ).  |     |     |     |     | of the | GLUE | benchmark |     | (Wang | et  | al., 2019). |

·|V|·|Y|
|              |           |     |     | k   |          | Specifically, |          | wetestonMicrosoftResearchPara- |       |        |     |           |

| Formally,    | we select |     | ′ : | by  | the fol- |               |          |                                |       |        |     |           |
|              |           | M   | Y   | → V |          |               |          |                                |       |        |     |           |
| lowingsteps: |           |     |     |     |          | phrase        | Matching | (MRPC)                         |       | (Dolan | and | Brockett, |
|              |           |     |     |     |          | 2005),        | Quora    | Question                       | Pairs | (QQP)  |     | for Para- |
Foreachy
1. i ,weiteratethroughalltrain- phrase Similarity Matching; Stanford Sentiment
∈ Y
ingsamplesx whosegroundtruth Treebank (SST-2) (Socher et al., 2013) for Sen-
|     |     | j   | train |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- 
|     |     | ∈ D |       |     |     |     |     |     |     |     |     |     |
labelyˆ = y . Weuse topredictthetoken timent Classification; Multi-Genre Natural Lan-
|     | j i |     | L   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- 
probabilityofthe[MASK]tokenandtakethe guageInferenceMatched(MNLI-m),Multi-Genre
5486

|     |     |     | MNLI  | MNLI-mm |     | SST-2 | QNLI  | RTE   | MRPC | QQP  | CoLA    |     | Avg. |

|     |     |     | (acc) | (acc)   |     | (acc) | (acc) | (acc) | (F1) | (F1) | (Matt.) |     |      |
Baselines
| Majority |     |     | 32.7 | 33.0 |     | 50.9 | 49.5 | 52.7 | 81.2 | 0.0 | 0.0 |     | 37.5 |

ManualLabel0-shot(2021) 50.8 51.7 83.6 50.8 51.3 61.9 49.7 2.0 50.2
| FullFine-tuning |     |     | 89.8 | 89.5 |     | 95.0 | 93.3 | 80.9 | 91.4 | 81.7 | 62.6 |     | 85.5 |

Dtrainonly;Noparameterupdate.
Setting1:
In-contextlearning(2020) 52.0(0.7) 53.4(0.6) 84.8(1.3) 53.8(0.4) 60.4(1.4) 45.7(6.0) 36.1(5.2) -1.5(2.4) 48.1(2.3)
AMuLaP(ours) 50.8(2.1) 52.3(1.8) 86.9(1.6) 53.1(2.8) 58.9(7.9) 56.3(5.0) 60.2(2.7) 2.3(1.4) 52.6(3.2)
| Setting2: | Dtrain+ | Ddev;Noparameterupdate. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ----------------------- | --- | --- | --- | --- | --- 
PETAL-CE(2020) 48.8(2.6) 49.7(2.3) 75.6(7.2) 49.5(0.0) 63.5(3.3) 28.9(39.6) 59.2(0.0) 1.3(3.0) 47.1(7.3)
PETAL-LR(2020) 38.6(2.0) 38.4(2.1) 85.3(3.3) 53.3(3.6) 54.7(6.4) 28.0(38.5) 55.6(2.8) 1.5(3.4) 44.4(7.8)
Auto-L(2021) 41.6(5.4) 42.3(6.2) 84.3(3.3) 57.9(3.9) 61.9(7.5) 67.7(7.9) 55.5(5.0) 1.2(4.8) 51.6(5.5)
AMuLaP(ours) 50.8(2.1) 52.2(1.9) 87.0(1.5) 53.5(2.3) 59.1(7.4) 56.7(5.7) 61.5(1.7) 2.6(1.8) 52.9(3.1)
Auto-L+AMuLaP(ours) 52.9(3.0) 54.2(2.7) 90.1(0.4) 57.9(2.6) 59.9(5.2) 66.0(3.0) 59.4(2.3) 2.7(5.7) 55.4(3.1)
|     | Dtrain+ | Ddev;Prompt-basedfine-tuning. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | ----------------------------- | --- | --- | --- | --- | --- 
Setting3:
Fine-tuning 45.8(6.4) 47.8(6.8) 81.4(3.8) 60.2(6.5) 54.4(3.9) 76.6(2.5) 60.7(4.3) 33.9(14.3) 57.6(6.1)
ManualLabelFT(2021) 68.3(2.3) 70.5(1.9) 92.7(0.9) 64.5(4.2) 69.1(3.6) 74.5(5.3) 65.5(5.3) 9.3(7.3) 64.3(3.9)
PETAL-CEFT(2020) 57.5(3.2) 57.7(2.6) 92.6(1.0) 50.5(0.0) 68.6(6.5) 32.1(42.5) 66.7(3.2) 3.8(8.4) 53.7(8.4)
PETAL-LRFT(2020) 64.0(6.5) 65.9(6.4) 92.9(1.7) 65.5(6.8) 63.3(7.7) 77.7(3.9) 65.7(4.2) 11.9(7.5) 63.4(5.6)
Auto-LFT(2021) 64.8(4.7) 67.3(4.3) 93.5(0.5) 69.8(3.0) 67.4(3.9) 76.2(4.8) 66.4(4.5) 23.2(17.1) 66.1(5.4)
AMuLaPFT(ours) 70.6(2.7) 72.5(2.4) 93.2(0.7) 65.1(5.9) 65.9(6.3) 79.3(4.0) 69.1(2.5) 18.3(9.4) 66.8(4.2)
Auto-L+AMuLaPFT(ours) 68.5(2.2) 71.1(2.3) 93.4(1.0) 69.6(1.1) 69.4(4.0) 75.5(5.6) 66.4(3.0) 14.2(14.0) 66.0(4.2)
Forfew-shotsettings,nissetto16
| Table2: | ExperimentalresultsunderthreesettingswithRoBERTa-largeas |     |     |     |     |     |     |     | .   |     |     |     |     |
| ------- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- 
L
perclass. Wereporttheaverageof5runsalongwiththeirstandarddeviationintheparentheses.
NaturalLanguageInferenceMismatched(MNLI- • Auto-L(Gaoetal.,2021): theautomaticlabel
mm)(Williamsetal.,2018),QuestionNaturalLan- searchingmethodwithanexternalpretrained
guage Inference (QNLI) (Rajpurkar et al., 2016) language model, RoBERTa-large (Liu et al.,
andRecognizingTextualEntailment(RTE)(Wang 2019). Thedetaileddescriptioncanbefound
et al., 2019) for the Natural Language Inference in Appendix A. Note that the results of this
(NLI)task;TheCorpusofLinguisticAcceptability baseline is different from those reported in
(CoLA)(Warstadtetal.,2019)forLinguisticAc- Table3ofGaoetal.(2021)sincetheysearch
ceptability. We use the manual templates in Gao forbothtemplatesandlabelmappingwhereas
etal.(2021),aslistedinTable1. Themetricsfor wefixthetemplatesandsearchforthelabel
eachdatasetareindicatedinTable2. mapping alone, for the sake of fair compari-
|           |     |         |     |        |     |         |     | son. | Weusetheofficiallyreleasedcodeand |     |     |     |     |

| Baselines | We  | compare | our | method | to  | various |     |      |                                   |     |     |     |     |
samehyperparametersforthisbaseline.
baselines:
|     |     |     |     |     |     |     | TaskSetup |     | WecloselyfollowthesetupinGao |     |     |     |     |

• Majority: always predict the majority class etal.(2021). Wesamplentrainingexamplesand
| inthetestset. |        |            |     |                |        |        | ndevelopmentexamplesperclass.       |          |                  |            | Wesetk  |          | = 16    |

|               |        |            |     |                |        |        | throughout                          |          | all experiments. |            | We use  | RoBERTa- |         |
| • GPT-3-style |        | in-context |     | learning       | (Brown |        |                                     |          |                  |            |         |          |         |
|               |        |            |     |                |        |        | large(Liuetal.,2019)asthebackboneLM |          |                  |            |         |          | . For   |
| et al.,       | 2020): | present    |     | a few examples |        | to the |                                     |          |                  |            |         |          | L       |
|               |        |            |     |                |        |        | each                                | reported | result,          | we measure | average |          | perfor- |
languagemodelandmakeitdirectlypredict
manceacross5differentrandomlysampled
train
| thenexttokenastheprediction. |     |     |     |     |     |     |     |     |                                  |     |     |     | D   |

|                              |     |     |     |     |     |     | and | dev | splits. FollowingGaoetal.(2021), |     |     |     | the |
D
originaldevelopmentsplitofeachdatasetisused
| • Manual |     | prompts: |     | we use | the | human- |                               |     |     |     |              |     |     |

|          |     |          |     |        |     |        | asthetestsetinourexperiments. |     |     |     | Wealsoreport |     |     |
designedpromptsinGaoetal.(2021).
|     |     |     |     |     |     |     | the | standard | deviation | for each | result. | To  | fairly |

comparewithdifferentbaselines,weconsiderthe
| • PETAL-CE(Schicketal.,2020): |     |     |     |     | thevariant |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ---------- | --- | --- 
followingthreesettings:
ofPETALusingthecross-entropymetric.
|     |     |     |     |     |     |     |     | • Setting1: | Weonlyuse |     | aloneforboth |     |     |

train
D
• PETAL-LR(Schicketal.,2020): thevariant labelselectionandtuningk. Theparameters
ofPETALusingthelikelihoodratiometric. of arenotupdated. dev isnotused. This
|     |     |     |     |     |     |     |     | L   |     | D   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- 
5487

Class PETAL-CE(Schicketal.,2020) PETAL-LR(Schicketal.,2020)
amazing,great,brilliant,perfect,fun, superb,fearless,acclaimed,addictive,visionary,
positive
wonderful,beautiful,fantastic,awesome,not immersive,irresistible,timely,unforgettable,gripping
not,awful,fun,funny,terrible, annoying,insulting,meaningless,lame,shitty,
negative
great,amazing,hilarious,awesome,good humiliating,childish,stupid,embarrassing,irritating
Class Auto-L(Gaoetal.,2021) AMuLaP(ours)
exquisite,perfection,effective,fabulous,intense great,perfect,fun,brilliant,amazing,
positive
inspiring,spectacular,sublime,astounding,thrilling good,wonderful,beautiful,excellent,fantastic
embarrassing,boring,frustrating,ridiculous,awkward terrible,awful,disappointing,not,horrible,
negative
silly,nothing,disgusting,ugly,confusing obvious,funny,inevitable,bad,boring
Table3: MostlikelylabelmappingfortheSST-2datasetobtainedbyPETAL(Schicketal.,2020),Auto-L(Gao
etal.,2021)andourAMuLaP.Suitablelabelsannotatedbythehumanannotatorareunderlined.
settingisforfaircomparisonwithIn-context outperforms GPT-3-style in-context learning by
learning. 4.5intermsoftheaveragescoreandoutperforms
zero-shotinferencewithmanuallydesignedlabels
• Setting 2: We use train for label selection by 2.4. Under Setting 2, compared to variants of
D
andanadditional fork tuning. Thepa-
dev PETAL(Schicketal.,2020),AMuLaPhasanad-
D
rametersof arenotupdated. Thissettingis
vantageof5.8and8.5intermsoftheaveragescore
L
for fair comparison with Auto-L (Gao et al.,
overCEandLR,respectively. Notably,AMuLaP
2021)andPETAL(Schicketal.,2020).
evenoutperformsAuto-Lby1.3withoutusingany
externalmodelordata. Additionally,weattemptto
• Setting 3: We use train and dev in the
D D replacethepredictedtokendistributionofAMuLaP
samewayasSetting2butfine-tunetheparam-
with the validation score of all fine-tuned assign-
eters of the language model . This setting
L ments(Gaoetal.,2021).2 Withthehelpofmany
isforfaircomparisonwithconventionalfine-
trials in automatic search, AMuLaP outperforms
tuning, prompt-based fine-tuning with man-
Auto-Lbyaconsiderablemarginof3.8intermsof
ual prompts, Auto-L (Gao et al., 2021) and
the average score, verifying the versatility of our
PETAL(Schicketal.,2020).
multi-label mechanism and label selection algo-
Implementation Details We implement AMu- rithm. UnderSetting3,AMuLaPFToutperforms
LaP based on Hugging Face Transformers (Wolf allbaselinesincludingAuto-L.Generallyspeaking,
et al., 2020). When selecting k, if there are mul- methods with parameter update (Setting 3) have
tiple k with identical performance (which hap- betterperformancethanthosethatdonotrequire
pens occasionally given there are only 16 exam- access to parameters. On all tasks except CoLA,
plesforeachclassin ),wealwayschoosethe AMuLaPoutperformsdirectfew-shotfine-tuning,
dev
D
largest k. For Settings 1 and 2, we search k over suggestingthatpromptingisapromisingmethod
1,2,4,...,1024 . Note that for settings that do forexploitinglargepretrainedLMs.
{ }
not update the parameters of , search over k is
L 6 Analysis
fast, as we only need to run the model once and
cache the distribution of the [MASK] token. For
### 6.1 CaseStudy
prompt-based fine-tuning (Setting 3), where we
As shown in Table 3, we list the 10 most likely
fine-tune the model , we search k in a smaller
L label mappings output by PETAL (Schick et al.,
space 1,2,4,8,16 due tothe increased compu-
{ } 2020), Auto-L (Gao et al., 2021) and AMuLaP
tational overhead. Following (Gao et al., 2021),
fortheSST-2dataset,respectively. Weshufflethe
wegridsearchthelearningratefrom{1e-5,2e-5,
labelsfromeachmodelandaskahumanannotator
5e-5}andbatchsizefrom{2,4,8}.
2The validation scores of all fine-tuned assignments
### 5.2 ExperimentalResults are obtained on , as described in Gao et al.
dev
D
(2021). No external data used. All of these we use
We demonstrate experimental results under three
are from https://github.com/princeton-nlp/
settings in Table 2. Under Setting 1, AMuLaP LM-BFF/tree/main/auto_label_mapping.
5488

|                                           | MNLI MNLI-mm | SST-2 QNLI  | RTE MRPC   | QQP  | CoLA Avg. |

|                                           | (acc) (acc)  | (acc) (acc) | (acc) (F1) | (F1) | (Matt.)   |
| Setting2: Dtrain+ Ddev;Noparameterupdate. |              |             |            |      |           |
AMuLaP 50.8(2.1) 52.2(1.9) 87.0(1.5) 53.5(2.3) 59.1(7.4) 56.7(5.7) 61.5(1.7) 2.6(1.8) 52.9(3.1)
w/odedup. 45.4(2.7) 46.5(2.5) 87.9(1.0) 53.8(3.0) 54.6(6.0) 66.7(12.3) 57.2(2.1) 2.5(4.2) 51.8(4.2)
k=1 46.5(2.7) 48.4(2.6) 68.8(12.0) 51.9(1.6) 58.8(12.7) 55.0(4.8) 59.2(0.0) 5.6(2.1) 49.3(4.8)
| Setting3: Dtrain+ Ddev;Prompt-basedfine-tuning. |     |     |     |     |     |

AMuLaPFT 70.6(2.7) 72.5(2.4) 93.2(0.7) 65.1(5.9) 65.9(6.3) 79.3(4.0) 69.1(2.5) 18.3(9.4) 66.8(4.2)
w/odedup. 56.9(5.4) 58.2(5.2) 92.8(0.9) 50.6(0.4) 57.1(10.8) 79.2(3.6) 55.0(26.0) 5.6(7.1) 56.9(7.4)
k=1 67.7(4.1) 69.8(3.8) 92.6(1.0) 65.9(5.2) 63.1(8.0) 80.2(3.8) 66.7(3.2) 19.3(15.5) 65.7(5.6)
random 58.8(6.2) 61.1(6.2) 92.1(2.1) 62.1(7.1) 57.0(11.2) 74.7(9.2) 60.8(5.8) 31.0(13.9) 62.2(7.7)
M′
random M′(k=1) 52.6(7.8) 55.4(8.3) 89.0(4.9) 65.2(4.5) 55.2(6.2) 73.4(10.6) 60.7(3.7) 17.3(14.7) 58.6(7.6)
Table4: Experimentalresultsfortheablationstudy. Wereporttheaverageof5runsalongwiththeirstandard
deviationintheparentheses.
| MNLI |     | MNLI-mm | SST-2 |     | MRPC |

| 80   |     |         |       | 90  |      |


| 70  | 70  |     |     | 80  |     |


| 60  | 60  |     |     | 70  |     |


|     | 50  |     |     | 60  |     |

Fine-tuning
## 60 AMuLaP (no FT)
| 40  | 40  |     |     | 50  |     |

AMuLaP FT

1 2 4 8 16 32 64128256 1 2 4 8 16 32 64128256 1 2 4 8 16 32 64128256 1 2 4 8 16 32 64128256
Shots per class (n) Shots per class (n) Shots per class (n) Shots per class (n)
Figure2: ComparisonofAMuLaP,AMuLaPFTandfine-tuningonMNLI,SSTandMRPCwithdifferentnforthe
trainingsetandthedevelopmentset.
to annotate whether they are suitable mappings. maps to two classes, optimization would be dif-
PETAL-CE suffers from incorrect mappings for ficult due to the contradiction of supervision sig-
“negative”whilePETAL-LRoccasionallyoutputs nals. Also,ourmulti-labelstrategyisshowntobe
vague labels. AMuLaP achieves interpretability effective at improving the average GLUE scores
thatiscompetitivetoautomaticlabelsobtainedby by3.6and1.1fornon-finetuningandfine-tuning
afine-tunedpretrainedlanguagemodel,measured settings, respectively. Moreover, a random label
bythehumanagreementratio. AlthoughAMuLaP mappingoftenleadstolowerperformancethanala-
outputs three labels that are rated not suitable by belmappingselectedbasedonthetrainingset. An
the human annotator, it should be noted that all interestingexceptionisthatforCoLA,therandom
three tokens are ranked low in the candidate set. mappingoutperformsalllabelselectionmethodsin
Thus,introducingtop-k truncationcanresolvethe Table2(bothmanualandautomatic)andisclose
problem. Additionally,wewouldliketohighlight tothefine-tuningbaseline.
thatAMuLaPmainlycollectscommonwordswhile
### 6.3 ScalingFew-ShotLearning
| othermethodspreferrarewords. |     | Thismayexplain |     |     |     |

whyAMuLaPworkswell,especiallyforthenon- LeScaoandRush(2021)explorethescalinglawof
| finetuningsettings. |     | PET(SchickandSchütze,2021a)whenusingmore |     |                            |     |

|                     |     | examplesfortraining.                     |     | Similarly,inthissection,we |     |
### 6.2 AblationStudy
aimtotesthowAMuLaPscalestodifferenttrain-
AsshowninTable4,weevaluatetheeffectofeach ing set sizes n. Figure 2 illustrates how standard
designchoiceontheGLUEbenchmark. Forboth fine-tuningandourAMuLaPwithnon-finetuning
non-finetuning and prompt-based fine-tuning set- andfine-tuningcompareasnincreases. ForMNLI
tings,ourdeduplicationalgorithmcaneffectively and SST-2 task, AMuLaP outperforms standard
improve the overall performance by 1.1 and 9.9 fine-tuning when we use no more than 16 train-
intermsoftheGLUEaveragescore,respectively. ing examples for non-finetuning and fine-tuning
Notably,deduplicationisespeciallyimportantfor setting. Whenusingmorethan16trainingexam-
prompt-based fine-tuning since if the same label ples, AMuLaP under fine-tuning setting still out-
5489

performs standard fine-tuning. For an easier task of a larger k. In general, we do not observe a
clearlawforchoosingthebestk
| like SST-2, | although | only | 32  | training | examples |     |     |     |     |     |     | forAMuLaP.As |     |

are used, the performance of our AMuLaP with mentionedbefore,k caninfluenceboththeoverall
non-finetuning and fine-tuning is close to satura- quality of labels (in both ways) and the training
tionandcanbecomparabletostandardfine-tuning procedure(forfine-tuning). Thus,fortheoptimal
ontheentiredataset. ForahardertasklikeMNLI, performance,wefinditessentialtosearchk witha
| althoughtheperformanceofAMuLaPundernon- |     |     |     |     |     |     | developmentset. |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- 
finetuningsettinggraduallybecomessaturatedas
| n increases, | AMuLaP |     | under | fine-tuning |     | settings |             |     |        |     |            |     |             |

|              |        |     |       |             |     |          | Limitations | and | Future |     | Directions |     | In this pa- |
continuestoimproveasnincreasesandcontinues
|                                     |     |     |     |     |          |     | per, we | only | focus   | on the | selection | of  | the label |

| tooutperformthestandardfine-tuning. |     |     |     |     | ForMRPC, |     |         |      |         |        |           |     |           |
|                                     |     |     |     |     |          |     | mapping | with | a fixed | prompt | template. |     | There is  |
althoughtheperformanceofourAMuLaPandstan-
moretoexplorewhenconsideringtheprompttem-
dardfine-tuningfluctuateasnincreases,ingeneral,
|        |      |             |     |       |         |      | plate at | the same | time. | Similar |     | to our | paper, pre- |

| AMuLaP | with | fine-tuning | can | still | achieve | com- |          |          |       |         |     |        |             |
viousworks(Schicketal.,2020;Gaoetal.,2021)
| parable                                        | performance | to  | standard    | fine-tuning. |          | In   |                                    |     |     |          |       |     |           |

|                                                |             |     |             |              |          |      | separatelysearchforaprompttemplate |     |     |          |       |     | andthe    |
| addition,theresultsdemonstratetheeffectiveness |             |     |             |              |          |      |                                    |     |     |          |       |     | T         |
|                                                |             |     |             |              |          |      | label mapping                      |     | .   | However, | these | two | variables |
| of AMuLaP                                      | especially  |     | for extreme |              | few-shot | set- |                                    |     | M   |          |       |     |           |
arecloselyrelatedandgreedilysearchforthebest
tings. Withonlyoneexample,AMuLaPachieves
|     |     |     |     |     |     |     | template | thenthebestmappingunder |     |     |     |     | maybe |

|     |     |     |     |     |     |     |          | T                       |     |     |     |     | T     |
decentperformancewhilestandardfine-tuningis
|                |     |     |     |     |     |     | suboptimal. | Jointlysearchingfor |     |     |     | and | could |

| closetorandom. |     |     |     |     |     |     |             |                     |     |     |     | T   | M     |
beapromisingdirectionforfutureresearch.
Morebroadly,wewouldliketopointoutsome
## 7 Discussion
|                    |     |     |     |                   |     |     | limitation               | and | contradictions |     | within              | current | few- |

|                    |     |     |     |                   |     |     | shotpromptingtechniques. |     |                |     | Thereisanaturalcon- |         |      |
| WhyDoesAMuLaPWork? |     |     |     | Schicketal.(2020) |     |     |                          |     |                |     |                     |         |      |
arguesthatonesinglelabelsometimescannotrep- tradictionbetweenperformanceandaccesstothe
resent all examples in a class, and thus multiple model weights. Brown et al. (2020) highlights
few-shotpromptingasawaytomitigatetheirde-
| labelsareneeded. |     | However,wefindthisexplana- |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- 
tioninsufficientforunderstandingthemechanism cisiontonotreleasethemodelweights. However,
behind the improved performance with multiple asshowninourTable2,withthesamebackbone
|     |     |     |     |     |     |     | model | ,GPT-3-stylein-contextlearningandother |     |     |     |     |     |

labels. Underafew-shotsetting,thelimitednum-
L
|                 |     |          | n   |         |          |     | methodsthatdonotaccessthemodelweightsgen- |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | ------- | -------- | --- | ----------------------------------------- 
| ber of training |     | examples | and | complex | training |     |                                           |     |     |     |     |     |     |
procedureofthebackbonemodel canoftenbring erallyunderperformthosewithaccesstothemodel
|          |                |     |       | L         |     |        | weightsbyalargemargin. |     |     |     | Also,in-contextlearn- |     |     |

| noise to | both automatic |     | label | selection | and | infer- |                        |     |     |     |                       |     |     |
ingcannothandlemoretrainingexamplesdueto
ence. Oneexampleisthemeaningless</s>(end-
of-sequence marker) label found by AMuLaP, as themaximumlengthlimitofthemodelwhileAMu-
shown in Table 1. This is due to the format pro- LaPwithoutfine-tuninggetssaturatedquickly,as
showninFigure2.
| cessinginthepretrainingof |     |     |     | . Allowingmultiple |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------ | --- | --- | --- 
L
| labels can | resolve | mishaps | like | this | and thus | im- |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | ---- | ---- | -------- | --- | --- 
Inaddition,complicatedpromptingtechniques
provethefinalperformance. arenotpracticallyusefulforreal-worldscenarios.
Moreover,whenselectingmultiplelabelsinfine- Formosttechniques,therequiredeffortforfinding
tuning,itisequivalenttotrainingonanaugmented goodtemplatesandlabelmappings,andsometimes
trainingset,asmultiplelabelsincreasetheoverall training models outweighs the cost of simply la-
sizeofthesupervisionpairs(x,yˆ). Toverifythis belingmoretrainingexamples. AsshowninFig-
guess,wetestthefine-tuningperformanceofaran- ure 2, 64 examples per class are enough to bring
dom mapping with different labels selected. We theperformanceofstandardfine-tuningtothesame
findthatforrandommapping,morelabels(i.e.,a levelofprompting. Althoughrecentworksonau-
larger k) often leads to better performance. This tomatic selection of prompts and label mappings
suggestsourguessmaybecorrect. However,wedo aremakingmeaningfulcontributiontothepractica-
notobservesignificantimprovementwhencontinu- bilityoffew-shotlearning,webelievemorework
ingincreasingk withlabelsselectedbyAMuLaP. shouldbedonetosimplifythelearningprocedure
Asweanalyze,increasingkharmstheoverallqual- andeliminatehumaneffortwhileachievinggood
| ityofselectedlabelsandthusoverridesthebenefit |     |     |     |     |     |     | performance. |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ 
5490

Acknowledgements Teven Le Scao and Alexander M. Rush. 2021. How
|     |     |     |     |     |     | manydatapointsisapromptworth? |     |     | InNAACL-HLT, |     |

We would like to thank all reviewers for their in- pages 2627–2636. Association for Computational
| sightfulcomments. |     | Thisprojectispartlysupported |     |     |     | Linguistics. |     |     |     |     |

byNSFAward#1750063.
BrianLester,RamiAl-Rfou,andNoahConstant.2021.
|     |     |     |     |     |     | The power | of scale                       | for parameter-efficient |     | prompt |

|     |     |     |     |     |     | tuning.   | arXivpreprintarXiv:2104.08691. |                         |     |        |
References
|              |       |               |       |           |     | Xiang Lisa                                | Li and | Percy Liang. | 2021. Prefix-tuning: |       |

| Stephen H.   | Bach, | Victor Sanh,  | Zheng | Xin Yong, | Al- |                                           |        |              |                      |       |
|              |       |               |       |           |     | Optimizingcontinuouspromptsforgeneration. |        |              |                      | arXiv |
| bert Webson, |       | Colin Raffel, | Nihal | V. Nayak, | Ab- |                                           |        |              |                      |       |
preprintarXiv:2101.00190.
| heesht | Sharma, | Taewoon | Kim, | M. Saiful | Bari, |     |     |     |     |     |

Thibault Févry, Zaid Alyafeai, Manan Dey, An- YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
dreaSantilli,ZhiqingSun,SrulikBen-David,Can-
|     |     |     |     |     |     | dar Joshi, | Danqi | Chen, Omer | Levy, Mike | Lewis, |

wenXu,GunjanChhablani,HanWang,JasonAlan
|     |     |     |     |     |     | Luke Zettlemoyer, |     | and | Veselin Stoyanov. | 2019. |

Fries,MagedSaeedAlShaibani,ShanyaSharma,Ur-
|     |     |     |     |     |     | Roberta: | A robustly | optimized | BERT | pretraining |

mish Thakker, Khalid Almubarak, Xiangru Tang, approach. arXivpreprintarXiv:1907.11692.
MikeTian-JianJiang,andAlexanderM.Rush.2022.
Promptsource: Anintegrateddevelopmentenviron- EthanPerez,DouweKiela,andKyunghyunCho.2021.
| mentandrepositoryfornaturallanguageprompts. |     |     |     |     | In  |                                         |     |     |     |       |

|                                             |     |     |     |     |     | Truefew-shotlearningwithlanguagemodels. |     |     |     | arXiv |
ACL(Demos).
preprintarXiv:2105.11447.
TomB.Brown,BenjaminMann,NickRyder,Melanie Fabio Petroni, Tim Rocktäschel, Sebastian Riedel,
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Patrick S. H. Lewis, Anton Bakhtin, Yuxiang Wu,
Neelakantan,PranavShyam,GirishSastry,Amanda
|         |          |          |       |               |     | andAlexanderH.Miller.2019. |     |                           | Languagemodelsas |     |

| Askell, | Sandhini | Agarwal, | Ariel | Herbert-Voss, |     |                            |     |                           |                  |     |
|         |          |          |       |               |     | knowledgebases?            |     | InEMNLP-IJCNLP,pages2463– |                  |     |
Gretchen Krueger, Tom Henighan, Rewon Child, 2473.AssociationforComputationalLinguistics.
| Aditya | Ramesh, | Daniel | M. Ziegler, | Jeffrey | Wu, |     |     |     |     |     |
| ------ | ------- | ------ | ----------- | ------- 
ClemensWinter,ChristopherHesse,MarkChen,Eric GuanghuiQinandJasonEisner.2021. Learninghow
Sigler,MateuszLitwin,ScottGray,BenjaminChess,
|             |             |     |         |                 |     | toask: Queryinglmswithmixturesofsoftprompts. |     |     |     |     |

| Jack Clark, | Christopher |     | Berner, | Sam McCandlish, |     |                                              |     |     |     |     |
InNAACL-HLT,pages5203–5212.Associationfor
Alec Radford, Ilya Sutskever, and Dario Amodei. ComputationalLinguistics.
| 2020. Language |     | models | are few-shot | learners. | In  |                                                 |     |        |                      |     |

| NeurIPS.       |     |        |              |           |     | PranavRajpurkar,JianZhang,KonstantinLopyrev,and |     |        |                      |     |
|                |     |        |              |           |     | PercyLiang.2016.                                |     | Squad: | 100,000+questionsfor |     |
JoeDavison,JoshuaFeldman,andAlexanderM.Rush.
|     |     |     |     |     |     | machinecomprehensionoftext. |     |     | InEMNLP. |     |

2019. Commonsenseknowledgeminingfrompre-
trained models. In EMNLP-IJCNLP, pages 1173– Victor Sanh, Albert Webson, Colin Raffel, Stephen
1178.AssociationforComputationalLinguistics. Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
|                                      |     |     |     |           |     | Chaffin, | Arnaud | Stiegler, | Arun Raja, | Manan Dey, |

| WilliamB.DolanandChrisBrockett.2005. |     |     |     | Automati- |     |          |        |           |            |            |
|                                      |     |     |     |           |     | M Saiful | Bari,  | Canwen    | Xu, Urmish | Thakker,   |
callyconstructingacorpusofsententialparaphrases. ShanyaSharmaSharma,ElizaSzczechla,Taewoon
| InIWP@IJCNLP. |     |     |     |     |     | Kim, Gunjan | Chhablani, |     | Nihal Nayak, | Debajyoti |

Datta,JonathanChang,MikeTian-JianJiang,Han
Tianyu Gao, Adam Fisch, and Danqi Chen. 2021. Wang,MatteoManica,ShengShen,ZhengXinYong,
Makingpre-trainedlanguagemodelsbetterfew-shot
HarshitPandey,RachelBawden,ThomasWang,Tr-
learners. InACL-IJCNLP.AssociationforComputa- ishala Neeraj, Jos Rozen, Abheesht Sharma, An-
tionalLinguistics. dreaSantilli,ThibaultFevry,JasonAlanFries,Ryan
Teehan,TevenLeScao,StellaBiderman,LeoGao,
HanGuo, BowenTan, ZhengzhongLiu, EricPXing, ThomasWolf,andAlexanderMRush.2022. Multi-
| andZhitingHu.2021. |     | Textgenerationwithefficient |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------------------------- | --- | --- 
taskpromptedtrainingenableszero-shottaskgener-
| (soft)q-learning. |     | arXivpreprintarXiv:2106.07704. |     |     |     | alization. | InICLR. |     |     |     |

Shengding Hu, Ning Ding, Huadong Wang, Zhiyuan Timo Schick, Helmut Schmid, and Hinrich Schütze.
Liu, Juanzi Li, and Maosong Sun. 2021. Knowl- 2020. Automaticallyidentifyingwordsthatcanserve
edgeableprompt-tuning: Incorporatingknowledge aslabelsforfew-shottextclassification. InCOLING,
intopromptverbalizerfortextclassification. arXiv pages5569–5578.InternationalCommitteeonCom-
| preprintarXiv:2108.02035. |     |     |     |     |     | putationalLinguistics. |     |     |     |     |

ZhengbaoJiang,FrankF.Xu,JunAraki,andGraham TimoSchickandHinrichSchütze.2021a. Exploiting
Neubig. 2020. How can we know what language cloze-questionsforfew-shottextclassificationand
models know. Trans. Assoc. Comput. Linguistics, naturallanguageinference. InEACL,pages255–269.
| 8:423–438. |     |     |     |     |     | AssociationforComputationalLinguistics. |     |     |     |     |

5491

TimoSchickandHinrichSchütze.2021b. It’snotjust overtheprunedspacethatmaximizezero-shotac-
|     | size that         | matters: | Small                       | language | models | are | also     |                                      |

|     |                   |          |                             |          |        |     | curacyon | train tofurthernarrowthesearchspace. |
|     | few-shotlearners. |          | InNAACL-HLT,pages2339–2352. |          |        |     |          | D                                    |
Thentheyfine-tunenassignmentsandre-rankto
AssociationforComputationalLinguistics.
findthebestlabelwordsmappingon .
D dev
| Taylor | Shin,                            | Yasaman | Razeghi, |     | Robert | L. Logan    | IV, |     |

|        | EricWallace,andSameerSingh.2020. |         |          |     |        | Autoprompt: |     |     |
Elicitingknowledgefromlanguagemodelswithau-
|     | tomatically | generated | prompts. |     | In EMNLP, |     | pages |     |

4222–4235.AssociationforComputationalLinguis-
tics.
| Richard | Socher,                   | Alex        | Perelygin, |                   | Jean   | Wu, | Jason  |     |

|         | Chuang,                   | Christopher | D.         | Manning,          | Andrew |     | Y. Ng, |     |
|         | andChristopherPotts.2013. |             |            | Recursivedeepmod- |        |     |        |     |
elsforsemanticcompositionalityoverasentiment
|      | treebank.                            | InEMNLP.     |            |        |            |          |       |     |

| Alex | Wang,                                | Amanpreet    | Singh,     | Julian | Michael,   |          | Felix |     |
|      | Hill, Omer                           | Levy,        | and Samuel |        | R. Bowman. |          | 2019. |     |
|      | GLUE:                                | A multi-task | benchmark  |        | and        | analysis | plat- |     |
|      | formfornaturallanguageunderstanding. |              |            |        |            | InICLR.  |       |     |
AlexWarstadt,AmanpreetSingh,andSamuelR.Bow-
|     | man.2019. | Neuralnetworkacceptabilityjudgments. |     |     |     |     |     |     |
| --- | --------- | ------------------------------------ 
TACL.
| Adina | Williams,    | Nikita        | Nangia,        |         | and Samuel | R.         | Bow-   |     |

|       | man. 2018.   | A             | broad-coverage |         | challenge  |            | corpus |     |
|       | for sentence | understanding |                | through |            | inference. | In     |     |
NAACL-HLT.
| Thomas | Wolf, | Lysandre | Debut, |     | Victor | Sanh, | Julien |     |

Chaumond,ClementDelangue,AnthonyMoi,Pier-
ricCistac,TimRault,RémiLouf,MorganFuntowicz,
JoeDavison,SamShleifer,PatrickvonPlaten,Clara
Ma,YacineJernite,JulienPlu,CanwenXu,TevenLe
|     | Scao, Sylvain                                   | Gugger, |     | Mariama | Drame, | Quentin    |     |     |

|     | Lhoest,andAlexanderM.Rush.2020.                 |         |     |         |        | Transform- |     |     |
|     | ers: State-of-the-artnaturallanguageprocessing. |         |     |         |        |            | In  |     |
EMNLP(Demos),pages38–45.AssociationforCom-
putationalLinguistics.
ZexuanZhong,DanFriedman,andDanqiChen.2021.
Factualprobingis[MASK]:learningvs.learningto
recall. InNAACL-HLT,pages5017–5033.Associa-
tionforComputationalLinguistics.
A AutomaticLabelSelection(Auto-L)in
LM-BFF
Gaoetal.(2021)proposedamethodtoautomati-
| cally | construct | a label | word | mapping |     | given | a   |     |

M
| fixed | template | .   | They | construct | a   | pruned | label |     |

T
| wordset |     | c ofthetopk |     | wordsbasedontheir |     |     |     |     |

|         | V   | ∈ V         |     |                   |     |     |     |     |
conditionallikehoodusingthepretrainedlanguage
| model           | foreachclassc |             |                            | .   | Theytake |      | c as |     |

|                 | L             |             |                            | ∈ Y |          | V    |      |     |
| Top-k           |               | logp([MASK] |                            |     | = v      | (x)) |      |     |
|                 | v            |             |                            |     |          | | T  |     |     |
|                 | x            | c           |                            |     |          |      |     |     |
|                 | ∈V            | ∈XDt rain   |                            |     |          |      |      |     |
| where           | t c          |             | denotesthesubsetofallex-  |     |          |      |      |     |
|                 | D rain        | ⊂ D train   |                            |     |          |      |      |     |
| amplesofclassc. |               |             | Theyfindthetopnassignments |     |          |      |      |     |
5492

---
**Source PDF:** `2023_37_article.pdf`
