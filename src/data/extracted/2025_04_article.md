Replication/ComputationalNeuroscience
R E S C I E N C E C [Re] The Discriminative Kalman Filter for Bayesian
Filtering with Nonlinear and Non-Gaussian Observation
Models
JosueCasco-Rodriguez1,ID,CalebKemere1,ID,andRichardG.Baraniuk1,ID
1RiceUniversity,Houston,Texas,USA
Editedby
BenoîtGirardID Abstract
KalmanfiltersprovideastraightforwardandinterpretablemeanstoestimatehidReviewedby
OzanCaglayanID denorlatentvariables,andhavefoundnumerousapplicationsincontrol,robotics,
signalprocessing,andmachinelearning. Onesuchapplicationisneuraldecoding
Received for neuroprostheses. In 2020, Burkhart et al. thoroughly evaluated their new ver19June2023 sionoftheKalmanfilterthatleveragesBayes’theoremtoimprovefilterperformance
forhighlynon‐linearornon‐Gaussianobservationmodels. Thisworkprovidesan
Published
open‐sourcePythonalternativetotheauthors’MATLABalgorithm. Specifically,we
08April2025
reproducetheirmostsalientresultsforneuroscientificcontextsandfurtherexamDOI inetheefficacyoftheirfilterusingmultiplerandomseedsandpreviouslyunused
10.5281/zenodo.15172014 trialsfromtheauthors’dataset. Allexperimentswereperformedofflineonasingle
computer.
## 1 Introduction
Brain‐computerinterfaces(BCIs)havelongbeenasubjectofsciencefiction[1].Detailed
communication with a machine through mere thought has become more technologicallyfeasiblewithtime,butstillremainsinfeasibleforthegeneralpublic. However,for
certaingroupsofpeople,BCIsareanecessarymeanstocircumventdebilitatingcircumstances. For example, people experiencing quadriplegia or locked‐in syndrome have
very little means through which to communicate or interact with the outside world,
and thus stand to benefit from thought‐controlled interfaces through which they can
operate robotic limbs or computers [1, 2]. As another example, people with impaired
controlorlossofalimbalsobenefitfromroboticprostheticlimbsthatcanbecontrolled
throughthoughtalone[3]. IntheaforementionedapplicationsofBCIs,oneofthekey
algorithmicchallengesistoaccuratelyestimatesomerelevantaspectoftheuser’scognition. Specifically,BCIsandneuroprostheticsoftenseektodecodeaquantifiablemotor
intention signal that can be used to control robots or cursors, such as the velocity of
anintendedarm,hand,orfingermovement[1,2]. Suchneuraldecodingsareusually
madeusinginformationfromasubsetoftheuser’sneurons,madeaccessiblethrough
invasiveelectrodetechnologiesorthroughothernon‐invasivemeans[4].
TheKalmanfilter[5]isacommonbasisuponwhichpracticionersdevelopBCIdecoding
methods[6,7,8]. Burkhartetal. (2020)[9]soughttoimproveKalmanfilterperformance
Copyright©2025J.Casco-Rodriguez,C.KemereandR.G.Baraniuk,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoJosueCasco-Rodriguez(jc135@rice.edu)
Theauthorshavedeclaredthatnocompetinginterestsexist.
Code is available at https://github.com/Josuelmet/Discriminative-Kalman-Filter-4.5-Python. – SWH
swh:1:dir:859cfa9e3d94c2aa580211c9de5d7a28d43a7fe2.
Dataisavailableathttps://portal.nersc.gov/project/crcns/download/dream/data_sets/Flint_2012–DOI10.1088/1741-2560/9/4/046006.
Openpeerreviewisavailableathttps://github.com/ReScience/submissions/issues/74.
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 1


KalmanFilter
nonlinearobservationorprocess
stronglynonlinear
| differentiable | largeornon‐differentiable |     |     |     |     |

ornon‐Gaussian
| Extended |     | Unscented | Discriminative |     |     |

Figure1. SummaryofhowtheobservationandprocessmodelsofvariousBayesianfilteringmethodsrelaxthoseoftheKalmanfilter.
inneuraldecodingeffortsbydevelopingtheDiscriminativeKalmanFilter(DKF),which
leverages Bayes’s theorem to facilitate Bayesian filtering in contexts involving highly
non‐linearornon‐Gaussianobservations. TheauthorspresentedfivedifferentexperimentsverifyingtheefficacyoftheDKF:thefirstthreeexperiments(4.2–4.4)consisted
ofintricatetoyexampleswithknownobservationmodels,whilethefinaltwowereBCIfocused experiments with observations consisting of neural recordings. The last two
experiments(4.5and4.6)arethemostsalienttoBCIapplicationsbecausethemapping
from neural activity to thoughts or intentions is highly nonlinear [10] and usually unknowntopracticioners. WechosetosolelyreplicateExperiment4.5becauseitwasthe
most BCI‐oriented experiment whose data and code were publicly available, since Experiment4.6involvedhumandata.
| 2 Kalman Filter Variations |     |     |     |     |     |

### 2.1 KalmanFilter
Kalman filters [5] are a family of algorithms whose purpose is to estimate a set of un‐
|     | {Z  | }   |     | {X  | }.  |

observable latent states ,Z ,...,Z given a set of observations ,X ,...,X
|     | 1 2 | T   |     | 1 2 | T   |

KalmanfiltersoperateundertheMarkovassumption:anyobservationX dependsonly
i
onitscorrespondingstateZ i ,andanystateZ i dependsonlyontheimmediatelyprecedingstateZ .UnlikeHiddenMarkovmodels[11],whichalsooperateundertheMarkov
i−1
| assumption,thelatentstates{Z |     | }T                                                |     |     |     |

|                              | i   | i=1 arenotdiscrete,insteadhavingcontinuousvalues. |     |     |     |
Forreal‐timeneuraldecodingapplications,theprimaryroleofKalmanfiltersistopredictthelatestlatentstate(e.g.,afingervelocity)Z whengiventhepreviouslatentstate
T
Z T−1 andthelatestobservation(e.g.,neuralelectrodesignals)X T . Outsideofreal‐time
control, otherapplicationsofKalmanfiltersincludesmoothing(predictingZ forany
i
1≤i≤T whengiven{X }T )andprojectionintothefuture(predicting{Z }∞
|     | i i=1 |     |     | i i=T | given |

{X }T
).
i i=1
The original Kalman Filter (KF) is a linear, Gaussian, and stationary model, and thus
assumesthefollowing:
| 1. LinearGaussianobservations:   |     | p(X |Z )∼N | (HZ ,R)              |     |     |

|                                  |     | i i        | i                    |     |     |
| 2. LinearGaussianlatentdynamics: |     | p(Z |Z     | i−1 )∼N (AZ i−1 ,G)1 |     |     |
i
1SomepractitionersprefertowriteAasF,andGasQ.
| ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 |     |     |     |     | 2   |

### 2.2 ExtendedandUnscentedKalmanFilters
TheKFistheoptimalestimatorforlineardynamicsystemswithGaussianobservation
andprocessnoise,butneuralprocessingsystemsareusuallyhighlynonlinear[10]. The
simplestmodificationforhandlingnonlinearobservationmodelsistheExtendedKalman
Filter(EKF)[12],whichmakesthefollowingmodificationstotheoriginalKFmodel:
|     |     |     |     | (   | )   |

1. NonlineardifferentiableGaussianobservations: p(Z |X )∼N f−1(X ),R
|     |     |     | i i |     | i   |

2. NonlineardifferentiableGaussianlatentdynamics: p(Z |Z )∼N (h(Z ),G)
|     |     |     | i   | i−1 | i−1 |

f−1(·)
3. The observation and process transformations and h(·) cannot be applied
directly to the latent state covariance. Instead, their Jacobians evaluated at the
| currentlatentvalueZ | i areappliedtothelatentcovarianceattimestepi. |     |     |     |     |

While the EKF can perform well with sufficient knowledge of the system, it can also
performpoorlywithoutsuchknowledge,orwhenstrongnonlinearitiesareinvolvedin
the system. Another nonlinear Kalman filter algorithm is the Unscented Kalman Filter (UKF) [13]. The UKF differs from the EKF by using a deterministic sampling techniqueknownastheunscentedtransformtopickaminimalsetofsamplepoints(sigma
points)aroundthemean. Byincorporatingsamplingtechniques,theUKFallowsusage
oftransformationswhoseJacobiansaredifficultorimpossibletocalculate(i.e.,largeor
non‐differentiablefunctions).
### 2.3 DiscriminativeKalmanFilter
The Discriminative Kalman Filter (DKF) [14] keeps the following model assumptions
fromtheKalmanFilter:
| 1. LinearGaussianlatentdynamics: |     | p(Z |Z         | )∼N (AZ | ,G) |     |

|                                  |     | i              | i−1 i−1 |     |     |
| 2. Theobservationmodelp(X        | |Z  | )isstationary. |         |     |     |
i i
However,unliketheKalmanFilter,theDKFdoesnotassumealinearobservationmodel
p(X |Z ).Instead,theDKFapproximatestheobservationmodelp(X |Z )≈p(Z |X )/p(Z )
| i i |     |     |     | i i | i i i |

viaBayes’theorem. Suchasubstitutioncanproveusefulif(a)theobservationdistributionp(X |Z )isstronglynonlinearornon‐Gaussian,or(b)thedimensionalityofobseri i
vationsX ismuchlargerthanthedimensionalityoflatentsZ;inneuralsignalprocess‐
|     |     |     | |X  |     | |X ∼ |

ing, both are often true. The DKF further models p(Z i i ) as Gaussian: p(Z i i )
N(f(X ),Q(X )), where f(·) and Q(·) are nonlinear functions that map the observai i
tionX toitscorrespondingelementsinthestatespaceRdandthecovariancespaceSd,
i
respectively. Burkhartetal. (2020)[9]formulatethattheobservation‐to‐statetransformationf(·)andtheobservation‐to‐covariancetransformationQ(·)aretheconditional
| meanandcovarianceofZ | i givenX | i : |     |     |     |

)=E(Z|X
|     | f(X |     | =X ) |     | (1) |

|     | i   |     | i    |     |     |
)=Var(Z|X
|     | Q(X |     | =X ) |     | (2) |

|     | i   |     | i    |     |     |
)∼N(0,S),whereS(alsowritten
| TheDKFalsomakesthestationarityassumptionp(Z |     |     | i   |     |     |

asV orT)isthecovarianceofZ whennotconditionedonanyZ . Definingtheini‐
| Z   | i   |     |     | i−1 |     |

tiallatentstateestimateµ = 0andtheinitiallatentcovarianceestimateΣ = S
|     | 0   |     |     |     | 0 (the |

latentcovarianceΣisalsowrittenasP intraditionalfilteringliterature),eachiteration
oftheDKFalgorithmproceedsasfollows:
|     |     | v =Aµ |     |     |     |

|     |     | i     | i−1 |     | (3) |
AT
|                                                          | M i | =AΣ i−1 | +G  |     | (4) |

| ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 |     |         |     |     | 3   |


|     |     |     |       | (      |          |         | )     |     |     |

|     |     |     |       | −1+Q(X |          | −1−S    | −1 −1 |     |     |
|     |     |     | Σ i = | M      |          | i )     |       |     | (5) |
|     |     |     |       | ( i    |          |         | )     |     |     |
|     |     |     | µ =Σ  | M      | −1v +Q(x | ) −1f(X | )     |     |     |
|     |     |     | i     | i      | i i      | i       | i     |     | (6) |
Inpractice,thefollowingadditionalchangesaremadetotheDKFalgorithm,withpseudo‐
| inverseswrittenas |     | † : |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- 
|                   |     |     |     |     |     |     | (   |     | )   |
−1
1. Q(X )−1−S−1mustbepositivedefinite.Ifitisnot,setQ(X )−1 = Q(X )−1+S−1 .
|     | i   |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- 
|     | (   |     |     | )   |     |     |     |     |     |
†
| Σ    | = M † | +Q(X   | )†−S† |     |     |     |     |     |     |
| ---- | ----- | ------ | ----- 
| 2.   | i i   |        | i     |     |     |     |     |     |     |
|      | (     |        |       | )   |     |     |     |     |     |
|      |       | †      | )†f(X |     |     |     |     |     |     |
| 3. µ | =Σ M  | v +Q(X |       | )   |     |     |     |     |     |
|      | i i   | i i    | i     | i   |     |     |     |     |     |
AnotherformulationoftheDKFmoresuitableforreal‐timeapplicationsistheRobust
DKF,whichmakestheassumptionthattheeigenvaluesofS−1aresosmallthatthe−S−1
terminEquation5isnegligibleandcanthusberemoved. Additionally,theRobustDKF
places an improper prior on Z 0 , and modeling starts from t = 1. Specifically, µ 1 =
f(X )andΣ =Q(X ),anditerativecalculationsstartatt=2insteadoft=1.
| 1   | 1   | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- 
## 3 Methods
### 3.1 Data
The data that Burkhart et al. (2020) [9] used in their most salient and practical opensource experiment for neuroscientific applications (4.5) came from Flint et al. (2012)
[15]. Specifically, thedataisfroma96‐channelmicroelectrodearrayimplantedinthe
primary motor cortex of one rhesus macaque (Monkey C, center‐out from [15]). The
macaquewastaughttoearnjuicerewardsbymovingamanipulanduminacenter‐out
reachingtask. A128‐channelacquisitionsystemrecordedtheresultingsignals,which
weresampledat30kHz, highpass‐filteredat300Hz, andthenthresholdedandsorted
into spikes offline. The data is made publicly available by Walker and Kording (2013)
[16]undertheDatabaseforReachingExperimentsandModels(DREAM)2
### 3.2 Preprocessing
The five .mat files from the Flint et al. (2012) manipulandum manipulation trials [15]
arefirstplacedinthesamedirectoryasflint_preprocess_data.ipynbfororganizationand
preprocessing. Eachfilehasvariousrecordingsessions(henceforthreferredtoastrials),
whereeachsession(trial)inagivenfilewasrecordedonthesameday[15].Sincethetrial
dataisstoredasMATLABstructs,extraattentionhadtobepaidduringimplementation
toensurethatthePythondataorganizationmatchedtheoriginalMATLABorganization
method. Eachofthefivefilesareprocessedasfollows:
1. Isolatealldatafromthen‐thtrialofthefile(somefilesonlyhaveonetrial,while
otherfilehaveuptofourtrials).
2. Foreachtrialinthefile:
a)Stackeachtimestamp’s3Dmanipulandumvelocityvertically.
b)Discretizetheactivityofeachneuroninthetrialintobinsof 1 ≈33μs.
30kHz
Stacktheneurons’spikebinsvertically.
2Dataisavailableathttps://portal.nersc.gov/project/crcns/download/dream/data_sets/Flint_2012
| ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 |     |     |     |     |     |     |     |     | 4   |
| -------------------------------------------------------- | --- | --- | --- 


3. Onlykeepthefirsttwodimensionsofthevelocities,sincethethirddimensionis
notrelevantforoperationofthemanipulandum.
4. Save the resulting 2D array of manipulandum velocities from the i‐th trial as a
uniqueentryinalistof2Dvelocityarrays. Inequivalentfashion,storethearray
ofspikebinsinalistof2Dbinarrays.
5. Repeatallearlierstepsforeachtrialfromeachfile. Thereareatotalof12trials
acrossallfiles,treatingeachtrialasindependentfromtheothers.
Onceorganized,thelistsoftrialvelocitiesandspikebinsarepreprocessedinthesame
mannerasBurkhartetal. (2020)[9]:
1. Isolatethevelocitiesandspikebinsfromthen‐thtrial.
2. Downsamplethespikebinsamplesfrom33μsintervalsto100msintervals.
3. Replacethespikebindatawithamovingsum(withawindowlengthof10entries)
ofthespikebindata.
4. Downsamplethevelocitydatasamplesintointervalsof100ms—specifically,keep
entrieswhoseindicesarehalfwaybetweentheindicesthatwereusedtodownsamplethespikebindataearlier.
5. Replacethespikebindatawiththez‐scores(using1degreeoffreedomcorrection,
asperMATLAB’szscorefunction)ofitstop10principalcomponents.
6. Asduringorganization,storethe2Darrayofprocessedspikebinsandthe2Darray
ofprocessedvelocitiesinalistof2Dspikearraysandalistof2Dvelocityarrays,
respectively.
7. Repeatallpreviousstepsforeachofthe12trials.
In similar fashion as Burkhart et al. (2020) [9], data preprocessing yields an array of
processedvelocities3 andanarrayofprocessedspikebins4. Theresultinglatentstates
(manipulandumvelocities)are2‐dimensional,whiletheobservations(z‐scoredprincipalcomponentscoresofneuralactivity)are10‐dimensional.
### 3.3 Computation
Paper_Script_45.ipynbreproducesExperiment4.5fromBurkhartetal.(2020)[9]inPython,
basedontheauthors’originalMATLABimplementation. Whilethereareatotalof12
trials,theauthorsonlyconductedanalysisonthefirst6trials’data. Thefollowinganalysesandprocedureswereperformedseparatelyoneachoftheaforementionedtrials.See
Table1foranoverviewofthesimilaritiesanddifferencesbetweenourcomputational
implementationsandthoseofBurkhartetal. (2020)[9].
Training,Validation,andTestDataSplit—Beforeperforminganyregression, the datafrom
thecurrenttrialisisolatedandsplitintotrainingandtestdata. Recallthateachtrialrepresentsarecordedsessionofamacaquecenter‐outreachingtask[15],andhasseveral
thousand 100ms samples (approximately 10 minutes of recorded data) [15]. The first
5,000 samples are used as training data, while the subsequent 1,000 samples are used
astestdata. Variousmethodsareusedforlearningeithertheobservation‐to‐statetransformation f : R10 → R2 or the state‐to‐observation transformation f−1 : R2 → R10.
3https://github.com/Josuelmet/Discriminative‐Kalman‐Filter‐4.5‐Python/blob/main/flint‐datapreprocessing/procd_velocities.npy
4https://github.com/Josuelmet/Discriminative‐Kalman‐Filter‐4.5‐Python/blob/main/flint‐datapreprocessing/procd_spikes.npy
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 5


| Algorithm     | Burkhartetal. | (2020) | PythonReproduction |

| Preprocessing | SeeSection3.2 |        | Same,tothebest     |
ofourability
| KalmanFilter | Fullydeterministic |     | Same |

matriximplementation
| NeuralNetwork   | Onehiddenlayer         |     | Twohiddenlayers         |

|                 | of10tanhneurons        |     | of10tanhneurons         |
|                 | optimiziedviaBayesian‐ |     | optimiziedviaRM‐        |
|                 | regularizedLevenberg‐  |     | SPropwithl2weight       |
|                 | Marquardtmethod        |     | penaltyand4,000epochs   |
| Nadaraya‐Watson | Kernelbandwidth        |     | Kernelbandwidth         |
|                 | optimizationviatheMAT‐ |     | optimizationviathescipy |
|                 | LABfminuncfunction     |     | minimize_scalarfunction |
| GaussianProcess | FittingviaGPMLpack‐    |     | Fittingviascikitlearn   |
|                 | agewithRBFkernel       |     | GaussianProcessRegres‐  |
sorwithRBFkernel
| LongShort‐TermMemory | One20‐dimensional    |     | One20‐dimensional    |

|                      | LSTMlayerandone      |     | LSTMlayerandone      |
|                      | fully‐connectedlayer |     | fully‐connectedlayer |
|                      | optimizedviaAda‐     |     | optimizedviaAdam     |
|                      | Gradwithdropout      |     | withanl2weight       |
penaltyandnodropout
| ExtendedandUn‐       | NativeMATLABimple‐     |     | FilterPyimplementa‐ |

| scentedKalmanFilters | mentationusingthe      |     | tionusingtheearlier |
|                      | earlierone‐layerneural |     | two‐layerneuralnet‐ |
|                      | networkarchitecture    |     | workarchitecture    |
Table1.ThesummarizeddifferencesbetweenthealgorithmicimplementationsinBurkhartetal.
(2020)[9]andthisstudy.
However, only Nadaraya‐Watson (NW) kernel regression [17] is used for learning the
transformation Q : R10 → S2 that estimates the conditional covariance of the latent
Z i giventheobservationX i . FollowingBurkhartetal. (2020)[9], weused70%ofthe
training data (3,500 samples) purely to train regression models, while the remaining
30%(1,500 samples)areusedto learnQ(x)usingNW regression; thus. The aforementioned 3,5000 samples will be referred to as training data, the next 1,500 samples will
bereferredtoasvalidationdata,andthelast1,000sampleswillbereferredtoastesting
data,forclarity. Whiletheindicesofthe5,000(training+validation)and1,000(testing)
samplesarenotrandomizedduetothetemporallysensitivenatureofBCIdecoding,the
indices of the 3,500 (training) and the 1,500 (validation) samples are randomly drawn
(withoutreplacement)fromthe5,000samples.
LinearKalmanFilter—Thefirstregressionmethodisthefundamentalbaselineuponwhich
to compare all subsequent algorithms: the traditional Kalman filter. It uses all 5,000
trainingandvalidationsamplesastrainingdata,sinceitdoesnotneedavalidationset
withwhichtolearnaQ(x)covariancefunction. Asidefromestimatedlatentstatemeans
andcovariances,theKalmanfilteralsoyieldsthetransitionmatrixA,theprocessnoise
covarianceQ(namedGinthenotebook),andtheinitialestimatecovarianceV (also
Z
referredtoasV 0 orP 0 ).
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 6


NeuralNetworkRegression—ThenextregressionmethodistheDiscriminativeKalmanFilter(DKF)usingneuralnetwork(NN)regression. RecallthatallDKFmethodsmustlearn
theobservation‐to‐statetransformationf : R10 → R2. Neuralnetworkregressionestimatesf(·)withafeedforwardnetworkthatlearnsfromthetrainingdata(3,500samples).
Burkhartetal. (2020)[9]usedaneuralnetworkwithonehiddenlayerof10hyperbolic
tangentneurons. However,theauthorstrainedtheirsmallernetworkusingacombinationofLevenberg‐Marquardt(LM)optimizationalgorithmandBayesianregularization
(BR)[18],whichautomaticallycalculatel2weightpenaltiesiterativelyandincorporate
information from the inverse Hessian of the loss function. However, since resources
forsecond‐orderoptimizationarescarceinPython,weusedamoretraditionalneural
networkarchitecture—2hiddenlayersof10hyperbolictangentneuronseach—andoptimizationmethod—4,000epochsusingRMSProp[19]withalearningrateof10−3
and
anl2regularizationpenaltyof10−4.
Afterestimatingthefunctionf : R10 → R2, thenetworkpredictsthelatentstates(velocities)correspondingtothevalidationdataobservations(1,500samplesofprocessed
neuralrecordings). Theoptimalbandwidthoftheradialbasiskernelforcovarianceestimationisthenfoundbyminimizingtheleave‐one‐outmeansquarederrorofNadarayaWatson (NW) kernel regression using the validation set and the outer product of the
validationresiduals(Z −f(X )forall{Z ,X }pairsinthevalidationdata). Next,the
i i i i
networkpredictsthelatentstatescorrespondingtothetestdataobservations(1,000samples), whileNWkernelregressionpredictsthelatentstateestimatecovariancesusing
thetestdata,validationdata,andvalidationresiduals.ThefinalDKF‐NNpredictionsare
madebypassingthenetwork’spredictedstatesandcovariances, alongwiththeaforementioned Kalman filter parameters A (state transition matrix), G (the process noise
covariance,alsowrittenasQ),andV (thestationarycovarianceofZ withoutcondiZ i
tioningonanyZ i−1 ).
Nadaraya-WatsonKernelRegression—DiscriminativeKalmanfilteringviaNadaraya‐Watson
(NW) kernel regression functions similarly to how NW regression estimated the state
covariancefunctionQ : R10 → S2 inthecaseofneuralnetworkregression. First,the
bandwidthoftheradialbasiskernelisoptimizedtominimizetheleave‐oneoutmean
squarederrorintheestimatedfunctionf :R10 →R2usingthe(3,500)trainingsamples.
Next,f(·)predictsthelatentstates(velocities)ofthe(1,5000)validationsamples. Q(·)is
thenestimatedfromtheresultingvalidationresidualsinthesamefashionasinneural
network regression. For the (1,000) test sample observations, f(·) and Q(·) then predictthelatentstatesandstatecovariances,whichareprocessedintothefinalDKF‐NW
estimatesinthesamemannerasintheneuralnetworkregressioncase.
GaussianProcessRegression—ThefinalfilteringmethoddependentontheDiscriminative
Kalman Filter involves estimating f : R10 → R2 via Gaussian process (GP) regression
[20]. AswithneuralnetworkandNadaraya‐Watson(NW)regression,theresidualsofthe
estimatedfunctionf(·)arecalculatedonthevalidationdataandthenusedtoestimate
Q(·). Afterwards,f(·)andQ(·)predictthelatentstatesandcovariancesofthetestdata.
ThepredictionsundergotheDKFalgorithmtoproduceafinalDKF‐GPestimateinthe
samemannerasearlierDKFregressions.
TheauthorsutilizedtheGPMLMATLABpackagetotraintheirGaussianprocessmodels [20, 21]. However, due to the lack of modern Python ports of GPML, we instead
usedtheGaussianProcessRegressor(GPR)classfromscikit‐learn5. WhiletheGPRclass
andGPMLpackagebothusealgorithmsfromthesamework[20],GPRregressionisless
5sklearn.gaussian_process.GaussianProcessRegressor
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 7


customizableandflexiblethanGPMLregression, resultinginworseaccuracy(butimprovedruntime)comparedtoBurkhartetal. (2020)[9],despiteourusageofthesame
kerneltype(radialbasisfunction/squaredexponential). Unliketheauthors,whouse
twoseparateR10 → RGaussianprocessregressionstocomposef : R10 → R2,weuse
asingleR10 → R2 Gaussianprocessregression,sincewedidnotobserveanyimprovementsinperformancefromusingtheformermethod(likelydueinparttoourusageof
anisotropickernel). Wealsodidnotfindanyimprovementsfromusingananisotropic
kernel.
LongShort-TermMemoryRegression—Unlikeallotherregressionmethods,LongShort‐Term
Memory (LSTM) regression [22] does not use any explicit Kalman filtering framework
anddoesnotlearnf(·)inthesamemannerasdescribedinEquation1. Instead,weand
Burkhartetal. (2020)[9]usedanLSTMrecurrentnetworkthatlearnsf(·)conditioned
onX i anditsprevioustwoobservationsX i−1 andX i−2 .
Weweresuccessfullyabletoreplicatetheauthors’LSTMnetwork,sincetheyalsowrote
theirsinPython. However,becauseweusedmodernPyTorchwhiletheyusedtheolder
TensorFlowV1framework,westillhadtotranslatetheirarchitecturalmethodstoour
newerframework. Inaccordancewiththeauthors’work, ourmodelconsistedofone
LSTMlayerofhiddendimensionality20thatrecurrentlyprocesses3observationsfrom
R10 beforeitshiddenstateundergoesalinearprojectionontoR20. Unliketheauthors,
we used Adam optimization (with a learning rate of 10−3 and an l2 weight penalty of
10−4)andnodropout,sincetheLSTMperformedbetterwiththoseadjustmentsmade.
NotethattheLSTMhadsignificantlyfewerparametersthandatapoints,whichislikely
whydropoutdidnotimproveperformance.
Unlike the DKF, EKF, and UKF methods, LSTM regression partitions the training and
validationdifferently. Recallthatthereare5,000observationsinthetrainingandvalidationdata. TheLSTMtrainingandvalidationdataarenotdrawnrandomly; i.e., the
first3,500observationsarefortraining,whilethelast1,500areforvalidation.
As in all previous methods, Q : R10 → S2 is learned via Nadaraya‐Watson kernel regression. Interestingly, Burkhart et al. (2020) did not apply the DKF to process LSTMestimatedstates. Uponfurtherinvestigation,wefoundthattheirchoicemadeempiricalsense,sinceDKFprocessingworsenedLSTMperformance,ascanbeseeninTables
4and5. Inordertofurtherinvestigatetheinteractionsbetweensequencemodelsand
DKFmethods,wealsotriedusingaTransformer[23]modeltoestimatef(X i ,X i−1 ,X i−2 ).
However,givenoursmallinputtimestepsizeof3,wefoundthattheLSTMarchitecture
hadsuperiorperformanceinboththenormalizedrootmeansquareerror(nRMSE)and
meanabsoluteangleerror(MAAE)metricswithwhichwevaluatefilteringmethods,requiredatleast10xfewerparameters,andwaseasiertotrain.
Extended and Unscented Kalman Filters—Burkhart et al. (2020) [9] used the existing nativeMATLABimplementationsoftheExtendedandUnscentedKalmanfilters,whilewe
usedtheFilterPylibrary[24]. UsageoftheExtendedKalmanFilter(EKF)[12]andUnscentedKalmanFilter(EKF)[13]beginswithlearningthestate‐to‐observationfunction
f−1 :R2 →R10,unlikethepreviousDKFmethods.Tolearnf−1(·),weusedaneuralnetworkwiththesamearchitecture(albeitwithflippedinputandoutputdimensionalities)
asthatoftheDKF‐NNmethod(2hiddenlayersof10hyperbolictangentneurons),since
theauthors’originalf−1(·)networkfacedthesameissuesofreproductioninPythonas
theirf(·)network. Wealsousedthesameoptimizationmethod,hyperparameters,and
trainingdataasintheDKF‐NNmethod(4000iterations,10−3 learningrate,anda10−4
l2weightpenalty). ForboththeEKFandtheUKF,theobservationnoiseRisestimated
asthecovarianceoftheresidualsevaluatedoverthevalidationdata(i.e.,thecovariance
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 8


| ofX −f(Z | )forall{X | ,Z }pairsinthevalidationdata). |     |     |     |     |     |

| i        | i         | i i                            |     |     |     |     |     |
TheEKFusesthelearnedf−1(·)asitsobservationfunction. TheJacobianofthefunctionisavailablethroughPyTorch,andissuppliedtotheEKFalgorithm. Alongwiththe
f−1(·),
aforementioned information from the EKF uses the residual‐estimated R and
theKalmanfilterparametersA(thestatetransitionmatrix),G(theprocessnoise,also
writtenasQ),andaninitialcovarianceestimateP =V toiterativelycalculatepredic‐
|     |     |     |     | 0   | Z   |     |     |
| --- | --- 
tionsoverthetestdata.
TheUKFusesthesameobservationfunctionf−1(·)astheEKF.WhiletheUKFcanoperatewithexplicitlynonlinearstatetransitionsF : R2 →R2 (unliketheEKF),thestate
transitionfunctionusedhere(inaccordancewiththeauthors’work)issetasmultiplication by the Kalman state transition matrix: F(Z ) = AZ . The UKF uses the same
|     |     |     |        | i     | i   |     |     |

|     |     |     | (G, R, | P = V |     |     |     |
Kalman parameters as the EKF and 0 Z ) and generates predictions over
the test data in the same fashion as the EKF. One key difference between the UKF algorithmhereandtheUKFalgorithmusedbyBurkhartetal. (2020)[9]isthatMATLAB
differsfromFilterPyinhowthenumberofsample(sigma)pointsarecalculated.
## 4 Results
|     | Trial1 | Trial2 | Trial3 | Trial4 | Trial5 | Trial6 | Average |

Kalman 0.765|0.765 0.945|0.942 0.788|0.788 0.792|0.793 0.779|0.780 0.761|0.765 0.805|0.805
DKF‐NW –19%|–21% –18%|–18% –9%|–17% –21%|–23% –19%|–20% –20%|–23% –18%|–20%
DKF‐GP –7%|–21% –11%|–19% –8%|–15% –9%|–20% –12%|–18% –9%|–20% –9%|–19%
DKF‐NN –23%|–19% 0%|–15% –7%|–13% –15%|–13% –19%|–13% –22%|–17% –14%|–15%
LSTM –22%|–15% –1%|–19% –21%|–16% –19%|–13% –21%|–16% –25%|–11% –18%|–15%
| EKF | –1%|2% | 7%|24% | 8%|12% | 18%|18% | 11%|12% | 6%|3% | 8%|12% |

| UKF | 1%|2%  | 1%|31% | 6%|18% | 11%|18% | 5%|15%  | 3%|6% | 4%|15% |
Table2. NormalizedRMSE(nRMSE)betweenthepredictedandtruetestvelocitiesusingonerandomseed,asinTable1fromBurkhartetal. (2020)[9]. Boldedvaluesindicatetheauthors’publishedresults,whilehighlightedvaluesdenoteourbestresultforeachtrial.Notethatpredicting
identicallyzerowouldyieldanRMSEof1.
|     | Trial1 | Trial2 | Trial3 | Trial4 | Trial5 | Trial6 | Average |

Kalman 0.884|0.889 0.957|0.955 1.026|1.025 0.930|0.933 0.966|0.964 0.926|0.926 0.948|0.949
DKF‐NW –14%|–15% 0%|–1% –21%|–20% –15%|–17% –25%|–25% –29%|–28% –17%|–18%
DKF‐GP –5%|–11% 10%|7% –19%|–22% –7%|–16% –17%|–24% –21%|–25% –10%|–15%
DKF‐NN –9%|–7% 11%|–2% –15%|–17% –11%|–16% –19%|–21% –21%|–23% –11%|–14%
LSTM –6%|–2% 13%|–2% –18%|–12% –12%|–6% –20%|–10% –20%|–8% –11%|–7%
| EKF | 1%|4%  | 12%|3% | 2%|–2% | 5%|–4% | –8%|–8%  | –1%|–7% | 2%|–2%  |

| UKF | –1%|0% | 9%|3%  | 1%|–3% | 2%|–3% | –10%|–8% | –6%|–6% | –1%|–3% |
Table3. MeanAbsoluteAngleError(MAAE,inradians)ofthepredictedandtruetestvelocities
usingonerandomseed,asinTable2fromBurkhartetal. (2020)[9]. Boldedvaluesindicatethe
authors’publishedresults,whilehighlightedvaluesdenoteourbestresultforeachtrial.Notethat
chancepredictionwouldyieldaMAAEofπ/2≈1.57radians.TheauthorsarguedthatMAAEmay
beamoresalientmetricforneuroprostheticapplications.
AfterreproducingtheregressionmethodsimplementedbyBurkhartetal. (2020)[9],we
evaluated their performance on the held‐out 1,000 samples of test data of the first six
oftwelvetrials,inthesamemannerastheoriginalauthorsandwiththesamerandom
seed. Specifically, wecalculatedthenormalizedroot‐meansquareerror(nRMSE)and
mean absolute angle error (MAAE) between the predicted and ground truth test data
velocities,asshowninTables2and3,respectively. Boldedvaluesindicatetheauthors’
| ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 |     |     |     |     |     |     | 9   |
| -------------------------------------------------------- | --- 


originalresults. Whilewewereunabletoreplicatemostoftheexactnumericalresults
fromBurkhartetal. (2020)[9],wefaithfullyreproducedthetrendsinperformancefrom
theauthors’work. NotableexceptionsincludeworsenedDKF‐GPperformance(dueto
thedifficultyoftranslatingGPMLcomputationstoPython)andheightenedLSTMperformance(duetoaddedhyperparametertuning). AlthoughtheDKF‐NWandLSTMregressionmethodshadthesameaverageperformanceoverthesixtrials,ourresultsagreed
withthoseofBurkhartetal. (2020)[9]inthattheDKF‐NWtriumphedasthebestregressionmethodduetoitssuperiorperformancewithrespecttotheMAAEmetric.
|          | Trial1 | Trial2 | Trial3 | Trial4 | Trial5 | Trial6 | Trial9 | Trial10 | Average |

| K        | 0.76   | 0.94   | 0.79   | 0.79   | 0.78   | 0.76   | 1.01   | 0.92    | 0.84    |
| NW       | ‐15%   | ‐18%   | ‐18%   | ‐24%   | ‐20%   | ‐21%   | ‐5%    | 3%      | ‐15%    |
| DKF‐NW   | ‐18%   | ‐18%   | ‐12%   | ‐19%   | ‐18%   | ‐20%   | ‐5%    | 2%      | ‐14%    |
| GP       | ‐3%    | ‐9%    | ‐7%    | ‐8%    | ‐10%   | ‐6%    | ‐7%    | ‐14%    | ‐8%     |
| DKF‐GP   | ‐6%    | ‐11%   | ‐8%    | ‐8%    | ‐12%   | ‐8%    | ‐8%    | ‐16%    | ‐10%    |
| NN       | ‐19%   | ‐17%   | ‐21%   | ‐23%   | ‐20%   | ‐23%   | ‐5%    | ‐7%     | ‐17%    |
| DKF‐NN   | ‐20%   | ‐11%   | ‐12%   | ‐16%   | ‐17%   | ‐20%   | ‐4%    | ‐9%     | ‐14%    |
| LSTM     | ‐22%   | 12%    | ‐23%   | ‐21%   | ‐23%   | ‐25%   | ‐7%    | ‐12%    | ‐15%    |
| DKF‐LSTM | ‐15%   | 84%    | ‐8%    | ‐7%    | ‐15%   | ‐14%   | ‐4%    | ‐12%    | 1%      |
| EKF      | 2%     | 10%    | 11%    | 18%    | 14%    | 8%     | 5%     | 12%     | 10%     |
| UKF      | ‐1%    | ‐1%    | 6%     | 15%    | 10%    | 4%     | ‐5%    | 2%      | 4%      |
Table4. AverageNormalizedRMSE(nRMSE)betweenthepredictedandtruetestvelocities,with
andwithoutDKFfiltering,evaluatedovertendifferentrandomseeds.Thebestresultsfromeach
trialarehighlighted.Trials7,8,11,and12didnothavetherequisitenumberofsamplesandwere
thusnotincluded.
|          | Trial1 | Trial2 | Trial3 | Trial4 | Trial5 | Trial6 | Trial9 | Trial10 | Average |

| K        | 0.88   | 0.96   | 1.03   | 0.93   | 0.97   | 0.93   | 0.97   | 1.03    | 0.96    |
| NW       | ‐8%    | 1%     | ‐21%   | ‐15%   | ‐21%   | ‐25%   | ‐1%    | ‐6%     | ‐12%    |
| DKF‐NW   | ‐14%   | ‐1%    | ‐21%   | ‐16%   | ‐25%   | ‐28%   | ‐5%    | ‐5%     | ‐14%    |
| GP       | 2%     | 12%    | ‐18%   | ‐3%    | ‐13%   | ‐16%   | 6%     | ‐4%     | ‐4%     |
| DKF‐GP   | ‐5%    | 11%    | ‐19%   | ‐7%    | ‐19%   | ‐20%   | 0%     | ‐8%     | ‐8%     |
| NN       | 1%     | 3%     | ‐17%   | ‐7%    | ‐15%   | ‐15%   | 4%     | 3%      | ‐5%     |
| DKF‐NN   | ‐6%    | 2%     | ‐17%   | ‐10%   | ‐19%   | ‐20%   | ‐3%    | 1%      | ‐9%     |
| LSTM     | ‐6%    | 15%    | ‐20%   | ‐13%   | ‐20%   | ‐20%   | ‐3%    | ‐5%     | ‐9%     |
| DKF‐LSTM | ‐6%    | 24%    | ‐18%   | ‐12%   | ‐20%   | ‐20%   | ‐2%    | ‐5%     | ‐7%     |
| EKF      | 0%     | 8%     | 1%     | 1%     | ‐4%    | ‐2%    | 3%     | 19%     | 3%      |
| UKF      | ‐4%    | 6%     | 0%     | 0%     | ‐8%    | ‐7%    | ‐1%    | 13%     | 0%      |
Table5.AverageMeanAbsoluteAngleError(MAAE)betweenthepredictedandtruetestvelocities,
withandwithoutDKFfiltering,evaluatedovertendifferentrandomseeds,asinTable4.Thebest
resultsfromeachtrialarehighlighted.
TobringfurtherinsightintotheperformanceoftheDiscriminativeKalmanfilterinneuroscientific contexts, we evaluated the aforementioned regression methods with and
without DKF filtering applied. Specifically, we measured their average performance
(seeTables4and5)onalleightofthetwelvetrialsthathadtherequisitenumberofsamples (at least 6,000) using ten different random seeds. To our surprise, we found that
unfilteredneuralnetworkregressionbestminimizednRMSE,butthattheDKF‐NWhad
thelowestMAAE.Interestingly,DKFapplicationforneuralnetworksincreasesnRMSE
whiledecreasingMAAE.
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 10


## 5 Conclusion
ThispartialreplicationstudyconfirmsthemostsalientresultsfromBurkhartetal.(2020)
[9]concerningtheperformanceoftheirDiscriminativeKalmanfilter(DKF)onpublicly
availableneuroprostheticdata. WenotonlysuccessfullyaffirmedthattheDKF‐NWhad
thebestoverallperformance,butwealsoconductedfurtherteststhatprovetheefficacy
oftheDKFwhileshowingthedifferencesthatmayoccurbetweendifferentmetricsfor
evaluatingfilterperformance.
WhileDKFmethodsimprovedovertheKalmanbaselines,theclosenessinperformance
ofKalmanandDKFmethodstothetrivialbaselineofpredictingidenticallyzero,especiallywhen using the nRMSEmetric, indicates that future workis needed to improve
such filters. For example, future endeavors could include Discriminative Kalman Filterincorporationintomoremodernapproachesinneurallatentstateestimation,such
assequential/dynamicalautoencoders,modernstate‐spacemodels, Kalmannetworks,
ortransformers[6,25,26]. Whilewedidnotfindourtransformerarchitectureoutperformed LSTMs, it is certainly possible that such an architecture could surpass LSTM
performance,especiallyintrialsofmuchlongerdurationswithlonger‐rangedependencies. Additionally,theeffectsofDKFapplicationonneuralnetworkorLSTMregression
arenotentirelyclear,andcouldstandtobeelucidatedinfutureworks.
## 6 Acknowledgements
WegivethankstoFlintetal. (2012)[15]andWalkerandKording(2013)[16]forcollecting
andhostingtheprimatereachdata,Burkhartetal. (2020)[9]fortheirmathematicalinsightsintoBayesianfiltering,andCalebKemereandRichardG.Baraniukfordiscussion
ofthisendeavor.
References
1. Y.S.Sonam.“AReviewPaperonBrainComputerInterface.”In:InternationalJournalofEngineeringResearch
&TechnologyNCETEMS3.10(2015).DOI:10.17577/IJERTCONV3IS10102.
2. F.R.Willett,D.T.Avansino,L.R.Hochberg,J.M.Henderson,andK.V.Shenoy.“High-performancebrain-to-text
communicationviahandwriting.”In:Nature593.7858(2021).
3. K.A.Yildiz,A.Y.Shin,andK.R.Kaufman.“Interfaceswiththeperipheralnervoussystemforthecontrolofa
neuroprostheticlimb:areview.”In:Journalofneuroengineeringandrehabilitation17.1(2020).
4. S.Saha,K.A.Mamun,K.Ahmed,R.Mostafa,G.R.Naik,S.Darvishi,A.H.Khandoker,andM.Baumert.“Progress
inbraincomputerinterface:Challengesandopportunities.”In:FrontiersinSystemsNeuroscience15(2021).
5. R.E.Kalman.“ANewApproachtoLinearFilteringandPredictionProblems.”In:JournalofBasicEngineering
82.1(1960).DOI:10.1115/1.3662552.
6. C.Pandarinath,D.J.O’Shea,J.Collins,R.Jozefowicz,S.D.Stavisky,J.C.Kao,E.M.Trautmann,M.T.Kauf-
man,S.I.Ryu,L.R.Hochberg,etal.“Inferringsingle-trialneuralpopulationdynamicsusingsequentialauto-
encoders.”In:Naturemethods15.10(2018).
7. A.K.Vaskov,Z.T.Irwin,S.R.Nason,P.P.Vu,C.S.Nu,A.J.Bullard,M.Hill,N.North,P.G.Patil,andC.A.Chestek.
“CorticaldecodingofindividualfingergroupmotionsusingReFITKalmanfilter.”In:Frontiersinneuroscience
12(2018).
8. N.Mudrik,Y.Chen,E.Yezerets,C.J.Rozell,andA.S.Charles.“DecomposedLinearDynamicalSystems(dLDS)
for learning the latent components of neural dynamics.” In: arXiv preprint arXiv:2206.02972 (2022). DOI:
10.48550/ARXIV.2206.02972.
9. M.C.Burkhart,D.M.Brandman,B.Franco,L.R.Hochberg,andM.T.Harrison.“TheDiscriminativeKalman
FilterforBayesianFilteringwithNonlinearandNongaussianObservationModels.”In:NeuralComputation
32.5(2020).DOI:10.1162/neco_a_01275.
10. T.M.McKenna,T.A.McMullen,andM.F.Shlesinger.“Thebrainasadynamicphysicalsystem.”In:Neuro-
science60.3(1994).
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 11


11. L.RabinerandB.Juang.“AnintroductiontohiddenMarkovmodels.”In:IEEEASSPMagazine3.1(1986).DOI:
10.1109/MASSP.1986.1165342.
12. M.I.Ribeiro.“Kalmanandextendedkalmanfilters:Concept,derivationandproperties.”In:InstituteforSys-
temsandRobotics43(2004).
13. E.A.WanandR.VanDerMerwe.“TheunscentedKalmanfilterfornonlinearestimation.”In:Proceedingsof
theIEEE2000AdaptiveSystemsforSignalProcessing,Communications,andControlSymposium.2000.
14. M.C.Burkhart,D.M.Brandman,C.E.Vargas-Irwin,andM.T.Harrison.“ThediscriminativeKalmanfilterfor
nonlinearandnon-GaussiansequentialBayesianfiltering.”In:arXivpreprintarXiv:1608.06622(2016).DOI:
10.48550/ARXIV.1608.06622.
15. R.D.Flint,E.W.Lindberg,L.R.Jordan,L.E.Miller,andM.W.Slutzky.“Accuratedecodingofreachingmove-
ments from field potentials in the absence of spikes.” In: Journal of Neural Engineering 9.4 (2012). DOI:
10.1088/1741-2560/9/4/046006.
16. B.WalkerandK.Kording.“TheDatabaseforReachingExperimentsandModels.”In:PLOSONE8.11(2013).
DOI:10.1371/journal.pone.0078747.
17. E.A.Nadaraya.“Onestimatingregression.”In:TheoryofProbability&ItsApplications9.1(1964).
18. F.D.ForeseeandM.T.Hagan.“Gauss-NewtonapproximationtoBayesianlearning.”In:Proceedingsofinter-
nationalconferenceonneuralnetworks(ICNN’97).Vol.3.1997.
19. S.Ruder.“Anoverviewofgradientdescentoptimizationalgorithms.”In: arXiv preprint arXiv:1609.04747
(2016).DOI:10.48550/ARXIV.1609.04747.
20. C.E.RasmussenandC.K.I.Williams.GaussianProcessesforMachineLearning.2005.DOI:10.7551/mit-
press/3206.001.0001.
21. C.E.RasmussenandH.Nickisch.“Gaussianprocessesformachinelearning(GPML)toolbox.”In:TheJournal
ofMachineLearningResearch11(2010).
22. S.HochreiterandJ.Schmidhuber.“Longshort-termmemory.”In:Neuralcomputation9.8(1997).
23. A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez,Ł.Kaiser,andI.Polosukhin.“Attention
isallyouneed.”In:Advancesinneuralinformationprocessingsystems30(2017).
24. R.Labbe.KalmanandBayesianfiltersinPython.2015.
25. L. Girin, S. Leglaive, X. Bie, J. Diard, T. Hueber, and X. Alameda-Pineda. “Dynamical Variational Autoen-
coders:AComprehensiveReview.”In:FoundationsandTrends®inMachineLearning15.1-2(2021).DOI:
10.1561/2200000089.
26. R.Liu,M.Azabou,M.Dabagia,J.Xiao,andE.L.Dyer.“Seeingtheforestandthetree:Buildingrepresentations
ofbothindividualandcollectivedynamicswithtransformers.”In:Advancesinneuralinformationprocessing
systems(2022).DOI:10.48550/ARXIV.2206.06131.
ReScienceC10.1(#3)–Casco-Rodriguez,KemereandBaraniuk2025 12

---
**Source PDF:** `531c2582ed6b.pdf` (2025_04_article.pdf)  
**URL:** https://zenodo.org/record/15172014/files/article.pdf
