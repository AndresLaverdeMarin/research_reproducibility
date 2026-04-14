Context-Dependent Encoding of Fear and Extinction
Memories in a Large-Scale Network Model of the Basal
Amygdala
Ioannis Vlachos1*, Cyril Herry2,3, Andreas Lu¨thi4, Ad Aertsen1,5, Arvind Kumar1,5*
1BernsteinCenterforComputationalNeuroscienceFrieburg,Freiburg,Germany,2NeurocentreMagendie,BordeauxCedex,France,3INSERMU862,BordeauxCedex,
France,4FriedrichMiescherInstituteforBiomedicalResearch,Basel,Switzerland,5DepartmentofNeurobiologyandBiophysics,FacultyofBiology,UniversityofFreiburg,
Freiburg,Germany
Abstract
Thebasalnucleusoftheamygdala(BA)isinvolvedintheformationofcontext-dependentconditionedfearandextinction
memories.Tounderstandtheunderlyingneuralmechanismswedevelopedalarge-scaleneuronnetworkmodeloftheBA,
composedofexcitatoryandinhibitoryleaky-integrate-and-fireneurons.ExcitatoryBAneuronsreceivedconditionedstimulus
(CS)-relatedinput from theadjacent lateralnucleus (LA) and contextual inputfromthe hippocampus or medialprefrontal
cortex(mPFC).WeimplementedaplasticitymechanismaccordingtowhichCSandcontextualsynapseswerepotentiatedifCS
andcontextualinputstemporallycoincidedontheafferentsoftheexcitatoryneurons.Oursimulationsrevealedadifferential
recruitment oftwodistinctsubpopulationsofBAneuronsduringconditioningandextinction,mimickingtheactivationof
experimentallyobservedcellpopulations.Weproposethatthesetwosubgroupsencodecontextualspecificityoffearand
extinction memories, respectively. Mutual competition between them, mediated by feedback inhibition and driven by
contextualinputs,regulatestheactivityinthecentralamygdala(CEA)therebycontrollingamygdalaoutputandfearbehavior.
Themodelmakesmultipletestablepredictionsthatmayadvanceourunderstandingoffearandextinctionmemories.
Citation:VlachosI,HerryC,Lu¨thiA,AertsenA,KumarA(2011)Context-DependentEncodingofFearandExtinctionMemoriesinaLarge-ScaleNetworkModelof
theBasalAmygdala.PLoSComputBiol7(3):e1001104.doi:10.1371/journal.pcbi.1001104
Editor:TimBehrens,JohnRadcliffeHospital,UnitedKingdom
ReceivedSeptember22,2010;AcceptedFebruary7,2011;PublishedMarch17,2011
Copyright:(cid:2)2011Vlachosetal.Thisisanopen-accessarticledistributedunder thetermsoftheCreativeCommons AttributionLicense,whichpermits
unrestricteduse,distribution,andreproductioninanymedium,providedtheoriginalauthorandsourcearecredited.
Funding:ThisworkwassupportedinpartsbytheGermanFederalMinistryofEducationandResearch(BMBFgrant01GQ0420toBCCNFreiburg),theSwiss
NationalScienceFoundation,theNovartisResearchFoundation,andaNeurex+grant.Thefundershadnoroleinstudydesign,datacollectionandanalysis,
decisiontopublish,orpreparationofthemanuscript.
CompetingInterests:Theauthorshavedeclaredthatnocompetinginterestsexist.
*E-mail:vlachos@bcf.uni-freiburg.de(IV);arvind.kumar@biologie.uni-freiburg.de(AK)
Introduction activity between fear and extinction neurons was correlated with
statesofhighandlowfear,respectively.Moreover,pharmacolog-
In classical fear conditioning an animal learns to associate an ical inactivation of the BA blocked the acquisition of fear
initially neutral stimulus (the conditioned stimulus, CS) with an extinction and context-dependent fear renewal, suggesting that
aversive stimulus (the unconditioned stimulus, US) after paired BA fear and extinction neurons may underlie the induction of
exposure to the CS and the US. Subsequent repeated non- behavioral changes and contribute to the formation of fear and
reinforcedpresentationsoftheCSaloneresultinadeclineofthe extinction memories.
conditioned response, a process called fear extinction [1]. Fear These findings raise the question of what the potential
extinction is a highly context-dependent process: the conditioned mechanisms underlying the differential activation of these two
fear response returns when the animal is exposed to an neuronalsub-populationsare.Here,weusedamodelingapproach
extinguished CSoutside theextinction context[2,3]. basedoninvivophysiologicaldatatoaddressthisspecificquestion
Studies over the last decades have identified the amygdaloid and to draw more general conclusions on potential neural
complexasakeybrainstructureinvolvedinbothfearconditioningand mechanisms involved infear andextinction memories in theBA.
extinction[4–6].Inthelateralnucleusoftheamygdala(LA),signals In vivo stimulation of identified fear and extinction neurons
carryinginformationabouttheCSandtheUSconvergeontothesame revealed that the two neuronal populations receive differential
neurons where they become associated through activity-dependent functional input from the hippocampus and from the medial
plasticity mechanisms [7–9]. The LA can directly or indirectly prefrontal cortex (mPFC) [17]. This finding could reflect
influenceactivityinthecentralnucleus(CEA)[10],themajoroutput anatomical specificity of inputs and/or selective functional
nucleus of the amygdala that can trigger fear responses via its plasticity of non-specific inputs. Independently of these two
projectionstothehypothalamusandtothebrainstem[11].Thebasal possibilities, in our model, we assume that anatomically and/or
nucleusoftheamygdala(BA)hasbeensuggestedtoplayanimportant functionally distinct inputs from the hippocampus or the mPFC
role in contextual fear conditioning [12,13], cued fear conditioning modulate the activity of BA fear and extinction neurons in a
[14],fearextinction[15–17]andcontext-dependentfearrenewal[17]. context-specific manner. That is, sub-populations of BA neurons
Recently,twodistinctfearandextinctionspecificneuronalsub- areinnervatedbyhippocampus/mPFCefferentsthatrepresentthe
populations in the BA have been identified [17]. The balance of current context. In addition, all BA neurons receive inputs from
PLoSComputationalBiology | www.ploscompbiol.org 1 March2011 | Volume 7 | Issue 3 | e1001104


correlation with the animal’s freezing behavior (Fig. 1). The
Author Summary
most parsimonious explanation suggests that the strength of a
Theamygdaloidcomplexisoneofthekeybrainstructures fractionofafferentscarryinginformationontheCS(CSinputs
involved in fear-related processes. A typical way to study from hereon) has been increased. Alternatively, changes in
neuralcorrelatesoffearexpression(e.g.freezingresponse) single neuron properties, e.g. excitability, or alterations in
in the amygdala is to perform a fear conditioning network activity states, e.g. reduced global inhibition, could
paradigm, which yields a conditioned fear response. This also accountforthisobservation.
responsecanbereversedbyanotherprocedurecalledfear
3.Duringextinctiontraininginadifferentcontext(context ),CS-
extinction.Thankstotheexperimentalapproachestodate B
induced activity of fear neurons progressively diminishes while
we have some understanding about the putative roles of
the activity of a new sub-population of neurons (extinction
specificsubnucleiwithintheamygdalaintheformationof
thesefearandextinctionmemories.Here,wecomplement neurons) increases. This suggests that during extinction, the
the experimental studies by providing a computational strengthofanewsubgroupofCSinputsisstrengthened,leading
model that addresses the question of how fear and to the increase in response of the extinction neurons.
extinction memories are encoded in the amygdala, and Furthermore, the second and third observations highlight the
specifically, in the basal nucleus (BA). We propose a importance of the context in the selective increase of the CS
specific neural mechanism to explain how the BA may inputs. They also suggest that the strength of the contextual
integrateinformationaboutasalient,conditionedstimulus inputstoBAneuronsmayincreaseaswell.
and the environment, thereby enabling it to switch the
4.The sudden and selective increase of activity of fear neurons
state of the animal from low to high fear and vice versa.
when the animal is put back in context after extinction
We also provide possible explanations for various other A
learning(i.e.renewal),revealsthatextinctioncannotbemerely
behavioralfindings,suchastherecoveryoffearafterithad
unlearning.Thus,themostsimpleexplanationfortheresponse
been extinguished (renewal). Finally, we make specific,
reduction of fear neurons in context is local inhibition
experimentally testable predictions that need to be B
generated by the increased response of extinction neurons. It
addressed infuture work.
cannot be excluded, though, that partial unlearning - i.e.
depotentiation of a certain fraction of previously strengthened
synapses -mayoccur inparallel.
US/CS responsive LA neurons during conditioning and extinc-
tion. Those sub-populations of BA neurons that receive simulta- To test the feasibility of the above observations and their
neous LA and context-specific inputs become responsive during inferences in explaining the emergence of fear and extinction
conditioning or extinction and, thus, emulate the ‘‘fear’’ and neurons in BA, we first studied the dynamics of a mean-field (or
‘‘extinction’’ neurons reported by Herry et al. [17]. Activation of firing rate) model of the BA. Subsequently, we constructed a
BAneuronsperse,however,isnotsufficienttocauseorpreventa spiking neuron network (SNN) model to examine our hypotheses
behavioral response, but the selective activation of BA neurons andtheir implicationsunder morerealistic conditions.
conveys important information about the context-CS relation to
theCEA. Althoughwedonot model heretheCEA, westipulate
Mean-field model of the BA
that context-dependent BA activity provides an instructive signal
The mean-field model of BA consisted of two neuron
toCEAneurons.IntheCEA,itislikelythatconditioning[18]and
populations, A and B, described by Wilson-Cowan type rate
possibly extinction learning-induced changes act upon this signal
dynamics [19] (Fig. 2A). Both populations were identical in their
in order to activate or suppress a fear response. If more
properties(Eqs.1–2)andreceivedbothCSinputandnon-specific
experimental data, sufficient to constrain the possible parameter
background input. There is ample experimental evidence that in
space,becomeavailable,thenourpresentmodeloftheBAcould
different contexts, different sets of hippocampal neurons (e.g. in
beextendedtostudytheimpactofcontext-dependentBAactivity
CA1)areactive[20–22].Thus,tomimiccontext-specificinputs-
on learning-induced changesin theCEAaswell.
either directly from hippocampus or indirectly via the mPFC or
We test the plausibility of context-dependent activation of BA
other brain structures such as entorhinal cortex - we provided
neuronsintwodifferentapproaches:first,inanabstractfiringrate
population A with additional input CTX reflecting context ,
model; second, in a more realistic spiking neuron network (SNN) A A
andlikewise,populationBwithadditionalinputCTX reflecting
model of the BA. Based on the results of our model we provide B
context .PopulationsAandBweremutuallyinterconnectedwith
plausibleexplanationsforseveralexperimentalobservationsinfear B
inhibitorysynapses.Thesystemofdifferentialequationsdescribing
andextinctionlearningandmakespecific,experimentallytestable
theactivity ofthepopulations Aand Bisas follows:
predictions.
Models
dA
t ~{Azg(t)z
Experimental observations A dt ð1Þ
The description of the evolution of the firing rates of BA (k {r A):S(j :CSzj :Bzj :CTX ),
neuronsduringfearconditioningandextinctionreportedby[17]
A A A,CS A,B A,CTXA A
provide certain simple, yet important, indications on the
underlying dynamicsintheBAnetwork:
dB
1.Innaiveanimals,theongoingactivityofBAneuronsdoesnot t B dt ~{Bzg(t)z ð2Þ
predict theexistence ofdifferent sub-populations ofneurons.
(k {r B):S(j :CSzj :Azj :CTX ),
2.As the animal learns to associate the CS with the US in B B B,CS B,A B,CTXB B
context (the conditioning context), the activity of a sub-
A 1
population of neurons in BA (fear neurons) increases, in where S(x)~ .
1ze{p(x{h)
PLoSComputationalBiology | www.ploscompbiol.org 2 March2011 | Volume 7 | Issue 3 | e1001104


|     |     |     |     |     |     |     | The evolutionof |     | theconnectionstrengths |     |     | isgivenby |     |     |

dj
|     |     |     |     |     |     |     |     |     | A,CS~a |     | :CSCTX | ,   |     | ð3Þ |

|     |     |     |     |     |     |     |     |     | dt     |     | A      | A   |     |     |
dj B,CS~a
|     |     |     |     |     |     |     |                 |                   |              |            | :CSCTX | :              |     | ð4Þ      |

|     |     |     |     |     |     |     |                 |                   | dt           |            | B      | B              |     |          |
|     |     |     |     |     |     |     | Here,           | j X,Y (X,YefA,Bg) |              | represents |        | the connection |     | strength |
|     |     |     |     |     |     |     | from population |                   | (or external | input)     | Y      | to population  | X,  | t is the |
X
|     |     |     |     |     |     |     | time constant | governing |     | the dynamics |     | of population | X,  | k is the |

X
|     |     |     |     |     |     |     | maximum | firing | rate | of population |     | X, and | r captures | the |

X
refractorinessofneuronsinX.ThetransferfunctionSisasigmoid
|     |     |     |     |     |     |     | function,              | integrating    | all        | inputs     | to population |             | X in a non-linear |            |

|     |     |     |     |     |     |     | fashion andproducing   |                | a          | bounded    | output        | rate.The    | parametersp       |            |
|     |     |     |     |     |     |     | and h of               | the sigmoid    | function   |            | determine     | the         | steepness         | and the    |
|     |     |     |     |     |     |     | position               | of its maximum |            | slope,     | respectively. |             | The term          | g(t), with |
|     |     |     |     |     |     |     | zero mean,             | reflects       | the        | stochastic | input         | to the      | two populations,  |            |
|     |     |     |     |     |     |     | mimickingthebackground |                |            | activity   | intheBA.      |             |                   |            |
|     |     |     |     |     |     |     | Equations              | 3 and          | 4 describe |            | the dynamics  |             | of the connection |            |
|     |     |     |     |     |     |     | strengths              | of the         | CS         | afferents  | onto          | populations | A                 | and B      |
|     |     |     |     |     |     |     | respectively.          | These          | weights    | were       | increased     |             | in an additive    | way        |
Figure1.Fearandextinctionneuronsinrodents.(A)CS-evoked
activity in the BA in pre-conditioning (left), post-conditioning (center) whenever the respective CS and CTX inputs were present
| and post-extinction | (right). | After conditioning |     | one | subpopulation | of  |     |     |     |     |     |     |     |     |

simultaneouslyandremainedconstantotherwise.Theparameters
neuronswithintheBA(fear-neurons,amber)increasedtheirfiringrates
|                                                          |     |     |     |     |     |     | a anda | specify | thelearning | rates(see |     | alsoEqs. | 6–8). |     |

| inresponsetotheCS.ThissubpopulationdidnotshowanyCSevoked |     |     |     |     |     |     | A B    |         |             |           |     |          |       |     |
WesimulatedfearconditioningandextinctionbyapplyingCS
| response after | extinction.     | A different |        | subpopulation | (extinction |      |          |                  |     |        |      |          |        |         |

|                |                 |             |        |               |             |      | input to | both populations |     | in the | form | of short | pulses | of 50ms |
| neurons, cyan) | did not respond |             | to the | CS during     | or after    | fear |          |                  |     |        |      |          |        |         |
conditioning, but showed a CS evoked response after extinction duration each, based on the experimental design used in [17].
training.(B)Populationactivitiesoffearandextinctionneuronsduring Contextualinputwasprovidedcontinuously.Notethatwedidnot
extinctiontrainingfordifferentblocksofCSpresentations.Inadifferent makeanyexplicitdistinctionbetweentheunconditionedstimulus
| context, extinction | training     | resulted     | in a | progressive  | decrease      | in the |          |             |          |     |       |          |            |      |

|                     |              |              |      |              |               |        | (US) and | conditioned | stimulus |     | (CS). | Instead, | we assumed | that |
| response of         | fear neurons | and increase | in   | the response | of extinction |        |          |             |          |     |       |          |            |      |
neurons.Theswitchofactivitywascorrelatedwithashiftinbehavior duringconditioning,neuronsintheLAinitiallyrespondedtothe
fromhightolowfreezing.Figureadaptedfrom[17]. US and eventually totheCS, whilecontinuing torespond tothe
doi:10.1371/journal.pcbi.1001104.g001 CS during extinction [23]. The output of these LA neurons was
thenfeddownstreamtotheBA.Inaddition,USorCSinputsfrom
thethalamusortheprimarysensorycortexmaydirectlytargetBA
|     |     |     |     |     |     |     | neurons | [24]. | In our | model, | we  | represented | those | inputs, |

Figure2.SchematicnetworkmodeldiagramsoftheBA.(A)Firingratemodel.TwoneuronpopulationsAandBaremutuallycoupledwith
negativeweights.BothpopulationsreceiveUS-CSandcontext-specific(CTX)inputs.TheseexternalinputscanexhibitLTP.(B)Spikingneuralnetwork
model.Thenetworkconsistsof3400excitatoryand600inhibitoryLIFneurons.Theneuronsareinterconnectedinarecurrentfashion.US-CSinputis
providedtoallneurons.CTXinputisfedonlytotwosubpopulationsofexcitatoryneurons.Theexternalinputs(CS,USandCTX)aremodeledasrate-
modulatedPoissonspiketrains.
doi:10.1371/journal.pcbi.1001104.g002
PLoSComputationalBiology | www.ploscompbiol.org 3 March2011 | Volume 7 | Issue 3 | e1001104


independently of their origin, as CS-US in the conditioning background inputs (BKG), representing activity originating in
context andCSintheextinction context. otherareas,eitherwithinoroutsidetheamygdaloidcomplex.The
|     |     |     |     |     |     |     |     | BKG | inputs | accounted | for the | baseline | spiking activity | of EXC |

Spiking neuron network model of BA andINHneurons at ,1 Hzand10–15Hz, respectively [24].
Theexacttemporalandspatialpatternsofthespikinginputsto
| For the | description | of  | the SNN | we  | adopted | the good | model |     |     |     |     |     |     |     |

descriptionpracticeproposedby[25],whichprovidesguidelinesfora theBAare not known.Here,weused independent Poissonspike
standardized way of describing complex neural networks. We generatorswithdifferentfiringratestoproducethespecificinputs.
share the authors’ belief that such model description facilitates ContextualandBKGinputsprovidedatonicdrivetoBAneurons.
reproducibility and direct comparisons between models. Within Bycontrast,theCSinputhadashortdurationof50ms,basedon
this framework, we organized the description in different the experimental design used in [17]. All external inputs formed
subsections, complemented by additional information on the excitatorysynapses ontotheir target neurons.
| model parameters.  |     | This    | collected | information | is            | presented | in an |          |           |     |                |     |     |     |

|                    |     |         |           |             |               |           |       | Neurons, | synapses, |     | and plasticity |     |     |     |
| easily accessible, |     | tabular | form      | in the      | Supplementary | Materials |       |          |           |     |                |     |     |     |
(Table S1). Neurons were modeled as leaky-integrate-and-fire (LIF) neu-
Our choice to use leaky-integrate-and-fire (LIF) neurons was rons. The subthreshold dynamics of each LIF neuron were
motivated by four major arguments: (i) multiple combinations of governed bythefollowing equation
sub-cellularparameterscanresultinthesamenetworkstate[26];
| (ii) even | simple | neuron | models | such | as LIF | with | minor |     |     |     |     |     |     |     |

dV
modifications are sufficient to reproduce complex in vivo spike t ~(E {V)zg (E {V)zg (E {V): ð5Þ
|                |            |                     |      |           |               |           |           |     | m dt  | 0             | exc      | exc | inh inh      |           |

| patterns [27]; | (iii)      | realistically-sized |      | large     | scale         | networks  | of LIF    |     |       |               |          |     |              |           |
| neurons        | can now    | be simulated        |      | with      | the currently | available |           |     |       |               |          |     |              |           |
| simulation     | technology | [28];               | this | is hardly | possible      | for       | similarly |     |       |               |          |     |              |           |
|                |            |                     |      |           |               |           |           | A   | spike | was generated | whenever |     | the membrane | potential |
largenetworksbuiltofdetailedcompartmentalmodelsand,finally,
|     |     |     |     |     |     |     |     | crossed | a predefined |     | static threshold | h in | upgoing direction. | The |

(iv) the extent to which sub-cellular properties of individual potential was then reset to a value E k and clamped for t ref ms
neurons influence the global network dynamics is presently not beforethesynapticintegrationstartedagain(TableS1F).Neurons
clear. Most importantly, however, here we are interested in made either excitatory or inhibitory connections onto their
understandingthekeynetworklevelpropertiesoftheBAwhichplay postsynaptic targets via conductance-based synapses [31–33].
a critical role in the formation of fear and extinction memories. The synapses of all connections were non-modifiable, except
For this purpose, the LIF neurons, although they are reduced thoseprovidingCSandcontextualinputtoEXCneurons.These
modelsofabiologicalcell,provideanadequatelevelofbiophysical latter, plastic synapses were modified according to the following
realism,sufficient toidentifythese key networkproperties. phenomenological rule:
| Network | composition |     | and connectivity |     |     |     |     |     |     |     |     |     |     |     |

WemodeledtheBAasarandomrecurrentnetwork,consisting
|            |            |     |       |       |      |            |       | wz  | ~          |        |     |     |     |        |

| of N ~3400 | excitatory |     | (EXC) | and N | ~600 | inhibitory | (INH) |     |            |        |     |     |     |        |
| E          |            |     |       |       | I    |            |       | (   | :h:m:jwmax | {w{j:c |     |     |     | ðð66ÞÞ |
neurons [24,29]. A total number of 4000 neurons corresponds w{ za1 ifCSandCTXtemporallyoverlapped
,
roughlyto10%ofallneuronsintheratBA[30].Theschematic w{ {a2 :m:jwmin {w{j:c
otherwise
diagramofthenetworkisshowninFig.2B.Eachconnectionfrom
| a pre- to | a post-synaptic |      | neuron | had an | assigned       | probability,     | the    |     |     |     |     |     |     |     |

| value of  | which depended  |      | on the | types  | of pre-        | and postsynaptic |        |     |     |     |     |     |     |     |
| neurons   | involved        | (EXC | and    | INH,   | respectively): | p                | ~0:01, |     |     |     |     |     |     |     |
EE
| p ~ 0 :15 | p ~ 0 | : 15 | p ~ | 0 :1 |     |     |     |     |     |     |     |     |     |     |

E I , I E , an d I I . T h u s , ea c h E X C n eu r on cc_~{ c zA:d(t
|     |     |     | ~   |     | ~   |     |     |     |     |     |     |     | ),  | ð7Þ |

r e c e iv ed o n a v e ra g e p EE (cid:2) N E 0: 0 1 (cid:2) 3, 4 0 0 3 4 e xc it ato ry a n d t pre
| ~0:15(cid:2)600~90inhibitoryconnections.Likewise,each |     |     |     |     |     |     |     |     |     |     | c   |     |     |     |

p EI (cid:2)N E
~0:15(cid:2)3,400~510
| INH neuron     | received           | p   | IE (cid:2)N | E          |              | excitatory |         |     |     |     |     |     |     |     |

| and p (cid:2)N | ~0:10(cid:2)600~60 |     |             | inhibitory | connections. |            | Neurons |     |     |     |     |     |     |     |
| II             | I                  |     |             |            |              |            |         |     |     |     |     |     |     |     |
wereallowedtoformrecurrentconnectionstothemselves.Forthe
| simulations | shown | in the | last figure, | we  | systematically | varied | the |     |     |     |                |     |     |     |

|             |       |        |              |     |                |        |     |     |     |     | hh_~{ h zB:d(t |     |     |     |
connectionprobabilityoftherecurrentinhibitionfrom0.1to1.0. pre ): ð8Þ
t
h
| Input, output, | and | free | parameters |     |     |     |     |     |     |     |     |     |     |     |

EXC and INH neurons received inputs encoding information Notethatthreevariableswereused:thesynapticweightwand
on the CS. Similarly to the rate model, these inputs represented the auxiliary variables c and h. Each time a presynaptic neuron
initial responses of LA neurons to combined CS and US fired, the value of c increased by a fixed amount. Afterward, this
presentations, later only to the CS. They might also reflect more value relaxed towards zero. Thus, variable c acted as a synaptic
peripheral,thalamicorcorticalresponsestoCS-US.Afractionof tag,encodingtherecentactivityinthesynapsereceivingCSinput.
BA EXC neurons (20%, randomly chosen) received inputs Likewise, variable h encoded information about recent activity in
representing CS and context . Similarly, another 20% of BA neighboring synapses receiving contextual input.
A
EXC neurons received inputs representing CS and context . AttheoffsetofeachCSpresentation,thevariablescandhwere
B
Thus, similar to the rate model, we assumed that BA EXC probed in the synapses of all EXC neurons and the strength of
neuronsreceivecontextualinformationdirectlyfromtheHPC(or each synapse was modified accordingly. The synaptic strengths
entorhinal cortex) and/or via the mPFC. Crucially, CS-US and before and after the update are denoted by w 2 and w + ,
contextual inputs converged onto the same neurons [8]. respectively. If CS and contextual inputs at the same neuron
Furthermore, EXC and INH neurons received unspecific coincided within a temporal window of ,100ms, then both
PLoSComputationalBiology | www.ploscompbiol.org 4 March2011 | Volume 7 | Issue 3 | e1001104


synapses were strengthened [34]. By contrast, if only one of the Thetermsjw
max
{w{jandjw
min
{w{jintheupdaterulewere
inputs was present, both synapses were weakened (Eq. 6). This introduced to provide upper and lower bounds to the synaptic
decrease of synaptic strength was based on studies reporting that weights, such that they did not increase or decrease indefinitely.
synapses in LA, which had been strengthened during fear They also controlled the step-size with which synapses were
conditioning, depotentiated after extinction training [35,36]. We modified:thecloseraweightwastow (w )thesmallerwereits
max min
assumed a similar mechanism to hold for the BA. This type of increments (decrements).
bidirectionalplasticityruleimplementedinourmodelissimilarto The parameter m represented the action of neuromodulators
theBCMrule[37],the‘‘calcium-controlhypothesis’’[38–40]and releasedduringfearconditioningandextinction.Itisknownthat
the ABS rule [41,42]. Common in all these rules is the many neuromodulators target the BA [5], possibly affecting
specification that the level of postsynaptic Ca2+ determines the synaptic plasticity in a complex way. Among the possible
directionofplasticity(forreviewsee[43]).AlargeincreaseinCa2+ candidates are norepinephrine (NE) [49–52], dopamine (DA)
causes LTP, whereas a moderate increase results in LTD. Low [53,54] and opioids [5]. Here, however, lacking more detailed
levelsofCa2+donotcauseanymodificationatall.Weessentially experimentaldata,wecannotbemorespecificaboutwhichexact
incorporated this bidirectional induction of plasticity in our rule neuromodulatorsareinvolvedandhowtheyinteract.Fortunately,
usingfixedthresholds(Fig.3C),ratherthanslidingones,asisthe this lack of knowledge does not pose a problem for the plasticity
case e.g. in the BCM rule. The parameters a and a denote the rulewepropose,becauseitisgeneralenoughtoaccommodateany
1 2
learningratesforpotentiationanddepotentiationofthesynapses, combinationofneuromodulatorsthatmayturnouttobeinvolved
respectively. inBAfear processing.
Ca2+ influx depends on NMDA receptor activation and The dynamics of the mean-field model were simulated in
sufficient postsynaptic depolarization. The latter can be caused MATLAB.TheSNNsimulationswerewritteninpython(http://
by coincident presynaptic input or by a backpropagating action www.python.org),usingthePyNNinterface[55,http://neuralensemble.
potential(BAP).However,inourmodel,aBAPwasnotrequired. org/trac/PyNN] to the NEST simulation environment [56,
Thatis,weassumedthatifthetotal presynapticfiringrateswere http://www.nest-initiative.org].
highenough,theycouldcausesufficientdepolarizationtounblock
NMDA receptors. This assumption is supported by experimental Results
evidenceshowingthataBAPisneithernecessarynorsufficientfor
synaptic plasticity [44,45]. Firing-rate model of BA
Note that this plasticity rule is also compatible with changes Fig. 4 shows the response of the mean-field model, i.e. the
induced purely in the presynaptic terminal. In fact, experimental firingratemodel,ofBAduringfearconditioningandextinction.
evidencesuggeststhatpresynapticinduction,completelyindepen- To simulate fear conditioning in context , we stimulated the
A
dent of postsynaptic activity, occurs in the LA [46]. Thus, the population A five times with CS, US and CTX inputs (Eqs.
A
plasticity rule implemented in our model incorporates both 1,2).ThisresultedinaprogressivestrengtheningofCSsynapses
changes that are dependent on post-synaptic depolarization, but onto population A (j ) (Fig. 4C), accompanied by a
cs,A
not postsynaptic spiking, and changes that are presynaptic and corresponding increase in the response of population A
entirely independent of post-synaptic depolarization or spiking. (Fig. 4A). To simulate fear extinction training in context , we
B
BecauseinourmodelthepresynapticspikingwascausedbyCS stimulated population A with CS input and population B with
andcontextualinputs,theirtotalactivityencodedinthevariablesc CSandCTX
B
inputsixtimestomimicadifferentcontext.Now,
and h, respectively, determined the direction of plasticity. Thus, incontext ,thesynapticstrengthoftheCSinputsynapses(j )
B cs,B
both c and h functioned as eligibility traces for synaptic onto population B progressively got stronger, whereas j
cs,A
modification [34,47]. They could be interpreted as describing remained unchanged (Fig. 4D). The slow increase in the
anyrelativelyslowprocessassociatedwiththeeffectsofCa2+,e.g. response of population B resulted in a small decrease in the
autophosphorylation of CaMK-II [39,48]. responseofpopulationA,duetotherecurrentinhibition.When
Figure3.Synapticplasticity.(A)and(B)SchematicconnectivitydiagramsoftypicalfearandextinctionneuronsintheBAnetworkmodel(cf.Fig.
2B).WeassumethatUS-CSandCTXsynapsesareplasticandspatiallyclusteredonthesameBAexcitatoryneuron(amberandcyanellipses;NM:
neuromodulator).(A)Duringfearconditioning,co-activationofCS,USandCTXafferents,strengthenedthesynapses(blackdots)onfearneuronsin
thepresenceofaneuromodulator.(B)Duringfearextinctiontraining,co-activationofCSandCTXafferentsstrengthenedthesynapses(blackdots)
on extinction neurons. Lack of CTX inputs resulted in a small depotentiation of CS synapses onto fear neurons (cf. Models). (C) The plasticity
mechanismthatdrivesthechangeinsynapticstrengthisessentiallyanimplementationofthecalcium-controlhypothesis[Eqs.6–8].IfCSandCTX
inputstemporallycoincide,thecalciuminfluxintheneuroncrossesthresholdH andLTPisinducedinbothCSandCTXsynapses.Bycontrast,ifonly
p
oneoftheCSandCTXinputsisactive,thetotalcalciuminfluxliesbetweenH andH andtheCSorCTXsynapsesexhibitLTD.Ifnoneoftheinputs
d p
isactive,thetotalcalciumlevelstaysbelowthresholdH andthesynapsesremainunaltered.
d
doi:10.1371/journal.pcbi.1001104.g003
PLoSComputationalBiology | www.ploscompbiol.org 5 March2011 | Volume 7 | Issue 3 | e1001104


|     |     |     |     |     |     |     | Spiking | neuron | network | model | of  | BA  |     |     |

Althoughasimplefiringratemodelwasabletoaccountforthe
|     |     |     |     |     |     |     | dynamic        | emergence    | of            | fear and            | extinction | neurons, |               | such mean-  |

|     |     |     |     |     |     |     | field models   | have         | only          | limited explanatory |            | and      | predictive    | power.      |
|     |     |     |     |     |     |     | For instance,  | they         | assume        | uncorrelated        |            | activity | in the        | underlying  |
|     |     |     |     |     |     |     | neuronal       | populations  | and,          | thus,               | cannot     | be used  | to            | predict any |
|     |     |     |     |     |     |     | correlations   | in firing    | rate          | or spike            | timing     | that     | may emerge    | in the      |
|     |     |     |     |     |     |     | network.       | In addition, | these         | models              | cannot     | be       | used to       | predict the |
|     |     |     |     |     |     |     | spike patterns |              | of individual | neurons.            |            | Thus,    | to understand | the         |
dynamicsoftheBAnetworkbeyondaveragefiringratesonly,we
|     |     |     |     |     |     |     | simulated                   | a biologically |            | realistic         | large-scale                      | network | composed   | of     |

|     |     |     |     |     |     |     | spiking neurons.            |                | Again,     | fear conditioning |                                  | and     | extinction | were   |
|     |     |     |     |     |     |     | simulated                   | by applying    | five       | CS-US             | presentations                    |         | in context | A and  |
|     |     |     |     |     |     |     | sixCSpresentationsincontext |                |            |                   | B respectively.Inthetwodifferent |         |            |        |
|     |     |     |     |     |     |     | environments                | tonic          | contextual |                   | input                            | was     | provided   | to EXC |
|     |     |     |     |     |     |     | neurons                     | (cf.Models).   |            |                   |                                  |         |            |        |
TheresultsofthesimulationarepresentedinFig.5.Initially,all
|     |     |     |     |     |     |     | EXCneuronsspikedatverylowfiringrates. |         |                 |          |        |        | Presentationsofthe |             |

|     |     |     |     |     |     |     | CS-US led                             | to      | a steady        | increase | in the | firing | rates              | of one sub- |
|     |     |     |     |     |     |     | population                            | (fear   | neurons)        | within   | the    | EXC    | population,        | which       |
|     |     |     |     |     |     |     | peaked at                             | the end | of conditioning |          | (Figs. | 5A,    | E amber            | dots). The  |
increaseinactivityoffearneuronswasadirectconsequenceofthe
Figure 4. Dynamics of the firing rate model of BA. Five US-CS potentiationofCSandcontextualinputsontofearneurons(Figs.5
stimulations were used for conditioning and six CS stimulations for G, I; amber triangles). In context B , the fear neurons still
| extinction. | (A) During conditioning, |     | LTP | at US-CS | and CTX | afferents |           |      |             |       |      |           |                  |     |

|             |                          |     |     |          |         |           | responded | with | high firing | rates | upon | the first | CS presentation, |     |
yieldedincreasedactivityofoneofthesub-populations(amberdots).
|              |                 |         |                |     |             |        | even though  | they | did not        | receive | contextual |     | inputs (Figs. | 5A, F). |

| The increase | in the activity | of this | sub-population |     | resulted in | a weak |              |      |                |         |            |     |               |         |
|              |                 |         |                |     |             |        | With further | CS   | presentations, |         | however,   | j   | synapses      | became  |
inhibition of the second sub-population (cyan dots). (B) During CS,B
|     |     |     |     |     |     |     | potentiated | (Eq. | 6, Figs. | 5H, | J; cyan | dots), | causing | a steady |

extinction,thesameplasticitymechanismresultedinagradualincrease
in the activity of the second subpopulation (cyan dots). This increase increaseinthefiringrateofthesecondsub-populationofneurons
inhibitedthefirstsubpopulation,whichalsoreceivedlessexcitationin (extinction neurons) (Figs. 5A, F; cyan dots). The increased
| the extinction | training. | The normalized |     | firing rates | represent | the |     |     |     |     |     |     |     |     |

recurrentinhibitioninthenetworkthencausedadecreaseinthe
averageover30simulations.Notethatthefiringrates,althoughthey
|     |     |     |     |     |     |     | activity | of the | fear neurons |     | (Figs. 5A–C, |     | F). At | the end of |

haveanupperbound,determinedbytherefractoryterminEqs.1–2,
remainfarfromsaturation.(C)Theevolutionofsynapticweightsj extinction, the population rate of the extinction neurons peaked,
CS,A
governingtheincreaseinthefiringrateofthefearneuronsduringfear whereas the firing rate of the fear neurons had returned to the
conditioning(amberD).(D)Evolutionofsynapticweightsj during initial, pre-conditioning values. The reduction of fear neurons
CS,B
extinction training (cyan D). A steady increase in the strength of activity was further facilitated by small depotentiation of CS and
synapses j CS,B resulted in a steady increase in the firing rate of contextualinputsynapsesontothefearneurons(Eq.6,Figs.4H,J;
| extinction | neurons. In the | firing | rate model | no  | depotentiation | of  |                   |     |      |                     |     |     |             |      |

|            |                 |        |            |     |                |     | amber triangles). |     | Note | that depotentiation |     | of  | CS synapses | onto |
synapseswasimplemented.
extinctionneuronsalsooccurredduringconditioning(Fig.5G)as
doi:10.1371/journal.pcbi.1001104.g004
|                |                   |     |     |                      |     |     | described     | by the | learning             | rule. | By contrast, | CTX | synapses      | were   |

|                |                   |     |     |                      |     |     | not decreased |        | during conditioning, |       | because      |     | their initial | values |
| thestrengthofj | becamelargerthanj |     |     | (Fig.4D),theactivity |     |     |               |        |                      |       |              |     |               |        |
cs,B cs,A wereclosetothelowerbound(w 2 )(Fig.5I).Duringconditioning
| of population | B dominated |     | and, | hence, | the response | of  |     |     |     |     |     |     |     |     |

andextinctionthebaselinefiringratesincreasedaswell(Fig.5A).
| population       | A was suppressed | (Fig. | 4B).         |                 |     |     |               |            |               |                     |                |     |                  |            |

|                  |                  |       |              |                 |     |     | Thisincrease  | wasinduced |               | by thestrengthening |                |     | of thecontextual |            |
| The differential | activation       | of    | two neuronal | sub-populations |     | in  |               |            |               |                     |                |     |                  |            |
|                  |                  |       |              |                 |     |     | inputs (Figs. | 5H,        | I), providing |                     | an explanation |     | for              | contextual |
twodifferentcontextscanbeinterpretedasfear(populationA)and conditioning. However, because only a small percentage of
extinction (population B) neurons as observed in [17]. This is neurons exhibited this increase in firing rates, this could make it
purely a functional characterization of the two sub-populations, difficult to measure it experimentally. This fact reveals a key
which are identical otherwise. That is, we used exactly the same advantage of network models which allow for simultaneously
parametersforbothsub-populationsandthedifferentialactivation sampling a large number of neurons. Based on this, predictions
results solely from differences in contextual inputs they receive. can beinferred whichotherwisewouldnot have beenpossible.
| Thus, the | two populations | were | not different |     | in terms | of their |            |        |     |            |     |        |         |         |

|           |                 |      |               |     |          |          | Note that, | again, | the | assignment | of  | BA EXC | neurons | in fear |
intrinsicproperties.Ofcourse,caseswherethetwosubpopulations
andextinctionsub-populationsispurelyafunctionalone.Thatis,
do have different properties can be easily accommodated in the neurons were characterized post-experiment as fear or extinction
model resulting in an enhancement of the differential activation. cells depending on whether they responded to the CS after
Tobeconsistentwith[17],weusedthetermsfearandextinction conditioningorafterextinctiontrainingrespectively.Inparticular,
neuronstorefertothosesubpopulationsthatareactiveincontex theywerenotpredeterminedintermsoftheirintrinsicproperties
A
and context respectively. andthetwosub-populationsresultedsolelyfromthedifferencesin
B
Note that we did not include any component that imitates thecontextual inputs theyreceived.
behavioraloutput,i.e.freezing.Instead,weassume,inagreement Also, it is important to emphasize that whereas the population
withexperimentalfindings[17],thathighactivityoffearneurons rates of fear and extinction neurons increased gradually during
directly corresponds to a high level of freezing whereas high conditioningandextinctiontrainingrespectively,thiswasnotthe
activity of extinction neurons and low activity of fear neurons caseforindividualneurons.Instead,theychangedtheirstatequite
corresponds tolow levels of freezing. abruptlyfromnon-respondingtoresponding(Fig.6A).Thefurther
PLoSComputationalBiology | www.ploscompbiol.org 6 March2011 | Volume 7 | Issue 3 | e1001104


Figure 5. Dynamics of the spiking network modelof BA. Five US-CS stimulations were used for conditioningand six CS stimulations for
extinction.(A)RasterplotofthespikingactivityintheSNN.Twodifferentsubpopulationsofexcitatoryneurons(EXC)withintheBAemergedduring
conditioning and extinction simulation, respectively. Neurons 1–1,700 correspond to the fear neurons (amber) and neurons 1,701–3,400 to the
extinctionneurons(cyan).Darkamberdotsshowtheactivityofinhibitoryneurons.Shorthorizontallines(black)atthebottomoftherasterplot
representUS-CSpresentations(50ms)infearconditioningandonlyCSinputduringextinctiontraining.Observethatactivityincreasedinthefear
neuronsduringconditioningandwasthensuppressedduringextinctiontrainingbyasteadyincreaseintheactivityoftheextinctionneurons.Note
thatincontrasttothefiringratemodel,inhibitoryneuronswereexplicitlysimulatedandplayedacriticalroleinthemutualcompetitionbetweenfear
andextinctionneuronsubpopulations.Thedeclineoffearneuronsactivityreflectsthecombinedeffectsofactiveinhibitionandunlearning(LTDat
CSandCTXafferents).Theincreaseofthebaselineratesprovidesanexplanationforcontextualconditioning.Only5outof6CSstimulationsshown
forextinctiontraining.(B)Firingratesoffear(amber)andextinction(cyan)neurons.(C)Firingrateofinhibitoryneurons.Similartotheratemodel,the
ratesofexcitatoryandinhibitoryneuronsremainedlowandfarbelowthesaturationlevel,determinedbytherefractorinessoftheneurons.(D)
Average free membranepotentials(spikingprohibited)of 100 randomlyrecorded fear (amber)and extinction(cyan) neurons.Twenty tracesfor
individualneuronsfromfear(lightamber)andextinctionneurons(lightcyan).Thedashedblacklineshowstheaveragespikingthreshold(257mV)
oftheexcitatoryneurons.(E,F)Evolutionofthefiringratesoffearandextinctionneuronsduringfearconditioning(E)andextinction(F).Firingrates
wereaveragedover30simulations.(G,H)EvolutionofsynapticweightsofCSafferentsontoEXCneuronsduringfear(G)andextinction(H)training,
forthesimulationshownin(A).(I,J)Sameasin(G)and(H)butfortheweightsofCTXafferentstoEXCneurons.
doi:10.1371/journal.pcbi.1001104.g005
| the training | advanced,   |             | the more | neurons       | started | to respond. |        |     |     |     |     |

| Hence,       | the gradual | increase    | in       | population    | rates   | (Figs.      | 5E, F) |     |     |     |     |
| reflects the | growing     | recruitment |          | of responding |         | neurons,    | rather |     |     |     |     |
thanagradualincreaseofsingleneuronactivityitself(Fig.6).The
| responsive   | neurons     | fired  | maximally    | two            | spikes per | CS presenta- |       |     |     |     |     |

| tion. The    | baseline    | firing | rates for    | the inhibitory | population |              | were  |     |     |     |     |
| normally     | distributed | with   | a mean       | of 10Hz,       | whereas    | the          | CS-   |     |     |     |     |
| evoked rates | shifted     | their  | distribution | towards        | a mean     | of           | 20Hz. |     |     |     |     |
Thisisconsistentwiththeneuronalfiringpatternsinvivoreported
by [17].
| Persistent | neurons |             |          |                  |     |                 |     |     |     |     |     |

| Although   | we      | performed   | our      | main simulations |     | using separated |     |     |     |     |     |
| contextual | inputs  | to distinct | neuronal | subpopulations   |     | within          | the |     |     |     |     |
BA(cf.Models),thisisnotanecessaryrequirementofthemodel.
Figure6.Single-neuronactivityduringfearandextinction.(A)
Infact,performingsimulationswithvaryingamountsofcontextual
Spikes(dots)ofexcitatoryneuronsforthreeconsecutiveCSpresenta-
inputoverlapshowedthatfearandextinctionneuronsstillexisted
tions(shortblacklines).Spikesfromthesameneuronsareconnected
| as distinct | populations, |     | even | when contextual |     | inputs had | an  |     |     |     |     |

bythinlines.DifferentneuronsstartedtorespondtotheCSwith1–2
overlap of around 50% (Fig. S1). In addition, the simulations spikesatdifferentpointsintime.Thus,thestateofindividualneurons
revealedtheexistenceofathirdsub-populationsofneurons.These didnotchangegradually,butquiteabruptlyfromnon-respondingto
weretheneuronsreceivinginputsinbothcontextsand,thus,were responding.(B)Thefiringratesofthreeneuronsfrom(A)(amber)that
|     |     |     |     |     |     |     |     | started responding | to the CS at three | different times. | The average |

activeduringbothfearconditioningandfearextinction(socalled
responseofthesethreeneuronsyieldedagradualincreaseofactivity
persistent neurons). Note that, similar to the case of fear and (green), which does not reflect the abrupt response changes at the
| extinction | neurons, | the characterization |     |     | of cells as | ‘‘persistent’’ | is  | single-neuronlevel. |     |     |     |

functionalanddenotesthefactthattheseneuronswereresponding doi:10.1371/journal.pcbi.1001104.g006
PLoSComputationalBiology | www.ploscompbiol.org 7 March2011 | Volume 7 | Issue 3 | e1001104


to the CS during both conditioning and extinction. Moreover, one of the populations continuously received a higher excitatory
these neurons had much stronger CS and CTX synapses, which driveduetotheadditionalcontextualinput.Switchingcontextsled
resulted in higher firing rates. This observation of the model is to a corresponding instantaneous switch in the assignment of the
consistent with the experimental data [17], suggesting that contextual input and, hence, in opposite shifts in the average
conditioning and extinction are not affected by overlapping membrane potentials of the two sub-populations, which was
inputs, unlesstheoverlap ishigh(.50%). immediatelyreflectedincorrespondingshiftsinthefiringrates.
We also modeled the case where the renewal context was
Renewal and extinction over-training different from both the conditioning and the extinction context
Following extinction training in context , presentations of the (ABCrenewal).Theresultsofthesimulationsrevealedthatifafter
B
CSintheoriginalfearconditioningcontext(context )resultedin extinction training the CS was presented in a third, different
A
context-dependent renewal (ABA renewal) of conditioned fear context C , fear neurons became rapidly active again and
responses[2].Thisrenewalphenomenonpointsattwoimportant suppressed extinction neurons (Fig. S2 middle). However, our
aspects of possible neural mechanisms underlying fear extinction: model also indicated that the absolute response of fear neurons -
(i)extinctionismainlynewlearningandonlypartlyunlearningof and thus the magnitude of the fear response- would be weaker
previously acquired fear memories ([57]; see also Discussion), (ii) than in the ABA case. The reason is that in context C CTX
extinction learning iscontext-dependent. synapses had not been strengthened during the conditioning
We simulated ABA renewal by changing context at the end of procedure. This provides an account for the experimentally
extinction (Fig. 7). This resulted in a sudden switch of activity observedABCrenewal[58,59]explainingwhyABCrenewalmay
between fear and extinction neuronal subpopulations. That is, occur in the first place and also why the effect may be weaker
although the activity of extinction neurons was high after compared toABArenewal.
extinction learning, the contextual switch caused the activation Moreover, our simulations also suggested that massive extinc-
of fear neurons and a significant drop in the extinction neurons tion (extinction over-training) in context B can abolish ABC
activity. These results are in complete accordance with the renewal, because depotentiation of CS and CTX A afferents onto
experimental findings reported by[17]. BAneuronsyieldlessexcitatoryinputtotheseneurons.Extinction
Itisimportanttonotethat thisrapidactivityswitchispurelya over-training can also impair ABA renewal, although to a lesser
networkphenomenonandnotaneffectofsynapticplasticity,asthe extent(Fig.S2right).ThereasonthatABArenewalismorerobust
change is much too fast for the plasticity mechanisms to act. We and ABC renewal more vulnerable to massive extinction stems
illustratethispointbydepictingtheaveragemembranepotentialsof fromthefactthatinthelattercasenotonlyCSsynapsesontofear
100randomlyselected fearandextinction neurons(Figs. 5D, 7D; neurons are weakened, but also potentiated CTX synapses are
amber and cyan traces respectively). It is evident that in either entirelymissing.Thesefindingsareinagreementwithandprovide
context there was a clear difference between the membrane a possible explanation for the experimentally observed effects of
potentialsofthetwocellpopulations,stemmingfromthefactthat massiveextinction [60].
Figure 7. ABA fear renewal. (A) Spiking activity of fear (amber), extinction (cyan) and inhibitory (dark amber) neurons during extinction and
renewal(grayshadedregion).(B)Averagefiringrateoffear(amber)andextinction(cyan)neurons.(C)Averagefiringrateofinhibitoryneurons.(D)
Freemembranepotentialoffearandextinctionneurons(cf.CaptionFig.5formoredetails).(E)Averagefiringratesoffearandextinctionneurons
duringextinctionandrenewal(grayshadedregion).(F)EvolutionofsynapticstrengthsofCSafferentsontofear(amber)andtheextinction(cyan)
neurons.(G)EvolutionofsynapticstrengthsofCTX afferentsontofear(amber)andCTX afferentsontotheextinction(cyan)neurons.Switching
A B
contextafterextinctionledtoaninstantaneousswitchofactivitiesbetweenfearandextinctionneurons(shadedgrayregionsinpanels(A,B,E).Inthe
initialconditioningcontext fearneuronsdominated(duetocontext specificadditionalexcitatorydrive)andsuppressedextinctionneurons.Note
A A
thattherewasnochangeofweightsduringrenewal(grayshadedareainpanelsF,G)revealingthattheswitchofactivitywaspurelyanetworkeffect.
doi:10.1371/journal.pcbi.1001104.g007
PLoSComputationalBiology | www.ploscompbiol.org 8 March2011 | Volume 7 | Issue 3 | e1001104


| Extinction | of contextual |     | conditioning |     |     |     |     |     |     |     |     |     |     |

Althoughwedidnotfocusonextinctionofcontextualfear,itis
| important | to note | that | our model | also | accounts | for this | specific |     |     |     |     |     |     |

conditioningphenomenon.Indeed,theplasticityruledictatesthat
intheabsenceoftheCSsynapticweightswilldecay.Thatis,CTX
| synapses, | which | had been | strengthened |     | during | conditioning | in  |     |     |     |     |     |     |

context andencodecontextualfear,willdepotentiateinthesame
A
| context | if the CS | is not | present. | This | will yield | decreased | fear |     |     |     |     |     |     |

neuronactivityand,thus,extinctionofcontextualfear.Notethat
withintheframeworkofourmodel,thisformofextinctionistruly
| unlearning         | andnot        | maskingof  |             | contextual     | fearmemories. |                    |             |     |     |     |     |     |     |

| High connectivity  |               | introduces |             | gamma          | oscillations  |                    |             |     |     |     |     |     |     |
| The experimentally |               |            | reported    | connection     |               | probabilities      | from        |     |     |     |     |     |     |
| excitatory         | to inhibitory |            | neurons     | as             | well as       | among              | inhibitory  |     |     |     |     |     |     |
| neurons            | in the        | BA are     | around      | 0.5 [61].      | This          | is a much          | higher      |     |     |     |     |     |     |
| value than         | the ones      | we         | used in     | our initial    | simulations   |                    | (Figs. 5–7, |     |     |     |     |     |     |
| Table S1E).        | To            | test the   | effects     | of such        | higher        | connectivity,      | we          |     |     |     |     |     |     |
| performed          | additional    |            | simulations | adopting       |               | the experimentally |             |     |     |     |     |     |     |
| reported           | values        | for the    | connection  | probabilities. |               | The                | qualitative |     |     |     |     |     |     |
behaviorofthemodeldidnotchange(datanotshown).However,
| a new aspect | in          | the network  | dynamics  |       | emerged.   | High    | frequency  |     |     |     |     |     |     |

| oscillations | - typically | in           | the gamma | range | (30–80Hz)  | -       | occurred   |     |     |     |     |     |     |
| throughout   | the         | simulation   | in        | both  | excitatory | and     | inhibitory |     |     |     |     |     |     |
| populations. | These       | oscillations |           | were  | present    | already | in the     |     |     |     |     |     |     |
ongoingactivitypatternsandCS-USpresentationenhancedthem
| even further | (Fig. | 8A). | They | resulted | from | the high | shared |     |     |     |     |     |     |

connectivityand,hence,largeamountofsharedinputsthatcaused
| correlated | spiking | in the | neurons. | The | oscillation | frequency | was |     |     |     |     |     |     |

determinedbysynaptictimeconstantsanddelaysinthenetwork.
| Gamma   | oscillations |          | in networks | of   | excitatory  | and     | inhibitory |     |     |     |     |     |     |

| neurons | have been    | reported | in          | many | experiments | [62–67] | and        |     |     |     |     |     |     |
Figure8.SynchronyandoscillationsintheBAnetworkmodel.
| discussed | in multiple |     | theoretical | studies | [68–75]. | Moreover, |     |             |                       |           |         |        |            |

|           |             |     |             |         |          |           |     | (A) Spiking | activity of a densely | connected | spiking | neural | network. A |
severalstudieshavereportedgammaoscillationsintheamygdala
highconnectionprobabilityfromEXCtoINHneuronsaswellasamong
undercertainconditions,e.g.inanesthetizedanimals[76],inslow
INHneuronsresultedinapopulationwidesynchronizationandgamma
wave-sleep[77],inthepresenceofrewardpredictingstimuli[78] rangeoscillations,whichweremoresalientduringCSstimulation(black
and in paradigms involving consolidation of emotional memories lines). (B) The effects of synaptic delays on the synchrony within the
[79]. Therefore, there is at least partial experimental and inhibitorypopulationshownforsynapticstrengthsof1nS,2nSand3
|             |         |     |           |       |              |     |          | nS in gray, | light and dark | green, respectively. | When     | synaptic   | delays  |

| theoretical | support | for | the gamma | range | oscillations |     | observed |             |                |                      |          |            |         |
|             |         |     |           |       |              |     |          | were drawn  | from a uniform | distribution         | [1–2ms], | increasing | connec- |
here inhigh connectivityBAnetworksimulations. tivity beyond 0.2 enhanced the oscillations and synchrony to their
Yet, in networks with high mutual connectivity between maximum(solidlines).Onlyforweakersynapses(1nS)synchronydid
excitatory and inhibitory neurons and within inhibitory neuron not increase with connection probabilities, because the network was
populations such as in the BA, oscillations should be a prevailing mainlyinputdriven.Synchronywassignificantlyreducedforallsynaptic
feature and should, therefore, be readily identifiable in vivo strengthswhensynapticdelaysweredrawnfromauniformdistribution
inalowerdelayrange[0.2–1ms](dashedlines).However,notethatfor
| recordings | under | all conditions |     | and not | only | in the special | cases |     |     |     |     |     |     |

highconnectivity(.0.4)andstrongsynapticcouplings,synchronywas
| mentioned | above. | It is, | thus, | possible | that certain | mechanisms |     |     |     |     |     |     |     |

alwayspresent.(C)InactivationofINHneuronsduringextinctionledto
operateintheBAthatcoulddampengammaoscillations(butsee
|     |     |     |     |     |     |     |     | increased | firing rates in both | fear | and extinction | neurons | (x-axis, |

Discussion).We,therefore,usedournetworkmodeltoinvestigate
|     |     |     |     |     |     |     |     | percentage | of inactive INH | neurons). | In context | B , extinction | neurons |

receivedadditionalcontextualinputand,thus,theiractivitywasmuch
thisissueinfurthersimulationsbyexploringtheparameterspace
higher(cyan)thanthatoffearneurons(amber).Independentlyofthe
| of the network |        | properties | that         | could | quench   | oscillations. | Two      |          |                    |         |          |           |          |

|                |        |            |              |       |          |               |          | behavior | of the animal, the | results | in panel | C suggest | a simple |
| mechanisms     | proved | to         | be effective | in    | reducing | the           | power of |          |                    |         |          |           |          |
experiment(i.e.blockingGABAergicsynapses)totestthevalidityofthe
| gamma | oscillations. | The | first | one | was the | introduction | of  |     |     |     |     |     |     |

mechanismweproposehere(seetext,blockageofinhibition).
heterogeneityintheinhibitorypopulation[80,81].Thisapproach doi:10.1371/journal.pcbi.1001104.g008
wasmotivatedbyexperimentaldatashowingthatinterneuronsin
the BA exhibit a large diversity in terms of their morphological BA:thefast-spiking(FS)andthedelayed-firing(DF)interneurons
andelectrophysiologicalproperties[24],similartointerneuronsin [24,61].Insuchheterogeneousnetworks,oscillationswereindeed
the cortex [82] and hippocampus [83]. In the latter case, the reduced, but nottotally eliminated[84].
diversitywasexpressedinawiderangeofvaluesforsynapticrise Asecond,moreeffectivewaytoreducethenetworkoscillations
times, reversal potentials, response latencies etc. In a preliminary was to decrease the synaptic delays between inhibitory neurons
study [84], we introduced heterogeneity in one of the neuronal (Fig. 8B). First, we studied the oscillations dynamics for different
propertiesinourmodel,thespikingthreshold,bydrawingvalues connection probabilities in a network of homogeneous neurons,
fromabimodaldistributionwithpeaksat235mVand228mV. withsynaptic delaysdrawnfroma uniformdistribution (1–2 ms).
Thiscorrespondstotheexperimentallymeasuredthresholdvalues In such networks, increasing connectivity (.0.2) enhanced the
of two subclasses of parvalbumin-expressing interneurons in the oscillationsandsynchronytotheirmaximum(Fig.8B,greensolid
PLoSComputationalBiology | www.ploscompbiol.org 9 March2011 | Volume 7 | Issue 3 | e1001104


lines). Only for very weak synapses (1 nS), that is, when the By contrast, when contextual inputs were removed after fear
network was mainly driven by external inputs, increasing the extinction, activity of neither fear nor extinction neurons was
connectivitydidnotaddtotheoscillations(Fig.8B,graysolidline). sufficiently strong to suppress the other neuron group (Fig. S3;
|            |           |     |              |     |                    |     |         | right). That | is, | because the | decisive | contextual | input | was | lacking |

| Increasing | the width | of  | the synaptic |     | delay distribution |     | did not |              |     |             |          |            |       |     |         |
reduce the synchrony and oscillations in high-connectivity and, thus, both groups were simultaneously active, although to a
networks (data not shown, Vlachos et al. in prep.). However, lesser degree than in case either group was active alone. The
choosing short delays from a narrow uniform distribution (0.2– behavioral consequences of these results are beyond the scope of
1 ms) considerably reduced the oscillations, up to connection our model, because here we did not model any downstream
probabilitiesof0.4(Fig.8B,greenandgraydashedlines).Thus,in structures such as the central amygdala that presumably further
a recurrent network, smaller delays have a powerful effect in processoutputfromfearandextinctionneurons.Thus,atpresent,
reducingsynchronyandoscillations.Thisfindingisinagreement we can only speculate that lesions of hippocampal or prefrontal
|                 |     |           |       |      |          |           |        | areas after | extinction  | training | may  | result  | in impaired |     | renewal, |

| with a previous |     | numerical | study | [69] | and also | with more | recent |             |             |          |      |         |             |     |          |
|                 |     |           |       |      |          |           |        | because     | fear neuron | activity | will | be both | decreased   |     | and also |
analyticalapproaches[74,75,85].Atfirstsight,synapticdelaysless
|           |       |        |                 |     |        |          |           | counteracted | by  | simultaneous | extinction |     | neuron | activity. | In fact, |

| than 1 ms | might | appear | unrealistically |     | small. | However, | delays as |              |     |              |            |     |        |           |          |
short as 0.5 ms have been reported among inhibitory neurons in experimentalevidencesupportsthisconclusion[88].However,itis
the hippocampus [66]. Moreover, the delays between inhibitory importanttopointoutasubtledifferencebetweenourmodeland
neuronsintheBAhavebeenreportedtobearound0.7ms[61], certain lesion experiments. In our model, removing CTX input
or even smaller (Lu¨thi, unpublished data). Therefore these short meansthattheBAnetworkdoesnotreceiveanycontextualinput
delays, might indeed account for the lack of gamma band atall.Bycontrast,insomeexperimentsinwhichthehippocampus
hadbeenlesionedorinactivated,contextualinformationmaystill
| oscillations | observed | under | baseline | conditions |     | in experimental |     |           |             |         |     |         |          |     |        |

|              |          |       |          |            |     |                 |     | have been | accessible, | because | the | context | in which | the | CS was |
recordings.
|          |               |       |            |      |        |        |           | presented   | wasstill | decisivefor | thebehavioral |     | outcome[89,90]. |     |     |

| Blockage | of inhibition |       |            |      |        |        |           |             |          |             |               |     |                 |     |     |
| Because  | inhibition    | plays | a critical | role | in our | model, | we tested | Predictions |          |             |               |     |                 |     |     |
Ourmodelenablesustomakeanumberofspecificpredictions
theeffectsofpartialinactivationofinhibitoryneurons.Forthis,we
that can betestedexperimentally:
| performed   | two            | additional | sets           | of simulations, |       | in which, | during |              |     |            |                |     |       |         |        |

| acquisition | of extinction, |            | we deactivated |                 | 50%   | and 90%   | of INH |              |     |            |                |     |       |         |        |
|             |                |            |                |                 |       |           |        | 1.We predict |     | that there | is convergence |     | of CS | and CTX | inputs |
| neurons,    | respectively.  | The        | results        | are             | shown | in Fig.   | 8C. As |              |     |            |                |     |       |         |        |
ontothesameBAEXCneurons.Thispredictioncanbetested
| expected, | with reduced |     | inhibition | the | activity | of both | fear and |             |     |           |     |       |      |                |     |

|           |              |     |            |     |          |         |          | in multiple |     | ways. One | way | is to | look | for anatomical |     |
extinctionneuronsincreased.Theincreaseofactivityofthelatter
|     |     |     |     |     |     |     |     | connectivity. |     | This can | be achieved |     | by employing |     | pathway |

populationwasmorepronounced,duetothefactthatitreceived
|     |     |     |     |     |     |     |     | tracing | studies. | Note, | however, | that | this approach | can | reveal |

context
additional excitatory drive from contextual inputs in B . stimulus convergence only on non-specific BA neurons,
This suggests that blockage of inhibitory activity should lead to because fear and extinction neurons are only behaviorally
| enhanced,    | context-specific |          | extinction. |     | This is    | consistent | with the   |            |                        |                         |     |         |       |                 |       |

|              |                  |          |             |     |            |            |            | determined |                        | in vivo. Alternatively, |     | one     | could | use optogenetic |       |
| finding that | GABA             | blockage | enhances    |     | extinction | of         | contextual |            |                        |                         |     |         |       |                 |       |
|              |                  |          |             |     |            |            |            | tools      | to activate/inactivate |                         |     | the LA, | HPC   | or PFC          | while |
freezing[86].However,thereisapotentialcaveathere.Activityof
|              |                |           |         |              |            |          |              | simultaneously |            | performing       | intracellular |              | recordings |                 | of BA  |

| both fear    | and extinction |           | neurons | is increased |            | upon     | blockage of  |                |            |                  |               |              |            |                 |        |
|              |                |           |         |              |            |          |              | neurons.       | If         | there is         | stimulus      | convergence, |            | then activation |        |
| inhibition   | and            | it is not | clear   | how          | downstream |          | structures,  |                |            |                  |               |              |            |                 |        |
|              |                |           |         |              |            |          |              | (inactivation) |            | of the connected |               | structures   | would      | result          | in an  |
| specifically | CEA            | neurons,  | would   | respond      | to         | this. If | the relative |                |            |                  |               |              |            |                 |        |
|              |                |           |         |              |            |          |              | increase       | (decrease) | of               | the mean      | and/or       |            | variance        | of the |
difference between fear and extinction neuron activity matters, membrane potential. A second way would be to test for
thenextinctionshouldbefacilitatedbyimpairedinhibition.If,by functional connectivity, e.g. by using an imaging technique
contrast, the ratio between fear and extinction neuron activity is akin to the one used in the LA [91]. Again, these approaches
morerelevant,thenextinctionmightbeimpaired.Notethatthese can only reveal convergence on non-specific BA neurons.
| two possibilities |     | apply | to both | blocking | of  | inhibition | during |     |     |     |     |     |     |     |     |

However,usingelectrophysiologicaltechniques,thecovariance
acquisitionofextinctiontrainingandblockingofinhibitionduring
ofthespikeratesbetweenLA,HPC/PFCandidentifiedBAfear
| expression | of fearextinction. |     |     |     |     |     |     |     |             |         |       |     |          |        |        |

|            |                    |     |     |     |     |     |     | and | extinctions | neurons | could | be  | measured | while, | again, |
selectivelyactivating/inactivatingLAorHPC/PFC.Function-
Removal of contextual input al convergence of CS and CTX inputs to BA fear and
Becausecontextualinputisoneofthekeyaspectsinourmodel extinctionneuronsshouldbereflectedinassociatedchangesof
| wetestedhowremovaloftheseinputswouldaffectthebehaviorof |        |             |      |         |            |           |            | thecovariances.                                         |     |     |     |     |     |     |     |

| the network.                                            | The    | simulations |      | yielded | two        | different | results    |                                                         |     |     |     |     |     |     |     |
|                                                         |        |             |      |         |            |           |            | 2.Extinctionover-traininghasadualeffect:(i)CSandcontext |     |     |     |     |     |     | B   |
| depending                                               | on the | exact       | time | point   | of removal | of        | contextual |                                                         |     |     |     |     |     |     |     |
afferentstoextinctionneuronswillbecomeverystrong,thereby
inputs. When contextual inputs were removed after fear enhancing the suppression of fear neurons. (ii) At the same
conditioning, fear neurons remained active during extinction time, depotentiation of CS and context afferents onto fear
A
training and no extinction neurons emerged (Fig. S3; left). This neuronswillsubstantiallydecreasetheexcitatoryinputtothese
resultisadirectconsequenceofoursynapticlearningrule,because neurons. This should be visible during renewal, where
strengthening of synapses requires temporal overlap of CS and presentation of the CS in context or context should lead
|     |     |     |     |     |     |     |     |     |     |     |     | A   |     | C   |     |

CTX inputs. Note that although fear neurons remained active, to only a weak fear response (Fig. S2; right). Existing
| their firing | rates | were | reduced, | because |     | they now | lacked |              |     |              |     |         |                |     |           |

|              |       |      |          |         |     |          |        | experimental |     | results seem | to  | support | this potential |     | effect of |
contextual input. Thus, our model suggests that lesions of massive extinction [60]. Here we predict, in addition to these
hippocampalorprefrontalareasafterfearconditioningmayresult behavioral findings, the state of ‘hidden’ or not directly
in impaired extinction. This conclusion is supported by experi- observable variables (large synaptic weights) and explain how
mental evidence[87]. they mayaffectdirect observables (enhanced extinction).
PLoSComputationalBiology | www.ploscompbiol.org 10 March2011 | Volume 7 | Issue 3 | e1001104


3.Conditioning and extinction training increase the excitatory memories, whereas non-contextual features, represented in LA
and inhibitory inputs to principal neurons in the BA. This or CEA,would remain unaffected [17].
| results | in stronger  | fluctuations |        | of their membrane | potentials. |           |         |               |     |        |     |     |     |

| Thus,   | the variance |              | of the | recorded          | membrane    | potential |         |               |     |        |     |     |     |
|         |              |              |        |                   |             |           | Sources | of contextual |     | inputs |     |     |     |
fluctuationsofBAneuronsintrainedanimalsshouldbehigher One core feature of our model is that contextual inputs are
than innaiveanimals. gated to the BA. In this framework, the precise origin of these
4.Blockageofinhibitionincontext resultsinelevatedactivityin inputs does not matter; as long as the BA neurons receive
B
both fear and extinction neurons, with extinction neurons differential inputs in two different contexts, the model behavior
spiking at a higher rate than fear neurons. It is not clear how remains unaltered. However, there are strong indications from
anatomical[29,93,94]andphysiological[93]studiesthattheHPC
| this may | impact | on downstream |     | structures | such as | the CEA. |     |     |     |     |     |     |     |

isamajorsourceofcontextualinformationtotheBA.Inaddition,
| Irrespective | of  | the behavioral |     | outcome, a | specific experiment |     |     |     |     |     |     |     |     |

addressingtheeffectsofGABAblockageonfearandextinction a previous report showed context-dependent modulation of
neurons activitywould providemore insightsinto thisissue. neuronalactivityintheLA[95].Bydesigningourmodeltohave
5.The strength of fear (extinction) memories is directly contextual input directly influencing the activity of excitatory
|              |                  |              |              |               |               |        | neurons                   | in the | BA, we           | have essentially |         | postulated | a similar   |

| proportional | to               | the strength |              | of contextual | inputs to     | the BA |                           |        |                  |                  |         |            |             |
|              |                  |              |              |               |               |        | mechanism                 | for    | this subnucleus. |                  | This    | assumption | is further  |
| during       | conditioning     |              | (extinction) | training,     | respectively. | If     |                           |        |                  |                  |         |            |             |
|              |                  |              |              |               |               |        | supported                 | by the | finding          | that fear        | neurons | show       | orthodromic |
| salience     | of environmental |              | features     | translates    | to higher     | firing |                           |        |                  |                  |         |            |             |
|              |                  |              |              |               |               |        | responsestoHPCstimulation |        |                  | [17].            |         |            |             |
ratesorincreasednumberofcontextualinputstotheBA,then
AsecondsourceofcontextualinputmaybethemPFC.Thereis
renewal(extinction)willbeenhanced.Alongthesamelines,the
|        |                 |     |         |              |     |            | anatomical | evidence | that     | the mPFC  | projects    | to  | the BA [29].   |

| bigger | the differences |     | between | conditioning | and | extinction |            |          |          |           |             |     |                |
|        |                 |     |         |              |     |            | Moreover,  | [17]     | reported | that mPFC | stimulation |     | induces ortho- |
context,themoreextinctionshouldbefacilitated,becausethe
overlap of contextual inputs to the BA between the two dromic responses in identified extinction neurons. Here, we
contextswillbe minimized. suggestthatpartoftheinformationconveyedbytheseprojections
|     |     |     |     |     |     |     | might be  | contextual.        | This | assumption |     | is based | on evidence  |

|     |     |     |     |     |     |     | reporting | extinction-related |      | induction  | of  | LTP on   | hippocampus- |
Discussion mPFC afferents [96]. In our model both fear and extinction
|     |     |     |     |     |     |     | neurons receive |     | context-specific | information |     | either | directly from |

Herewepresentedforthefirsttimealarge-scalenetworkmodel hippocampus or indirectly via the mPFC. This may also explain
of the BA addressing the question how contextual inputs may the ambiguous results that the hippocampus may or may not
shape the activity of distinct sub-populations of BA neurons. interact with themPFCduring extinctionlearning [97].
Although we started from a very specific experimental data-set Thecontext-specificmodulationofactivityintheBApresented
[17],weimplementedanetworkmodelthathasmorefar-reaching hereprovidesageneralframeworkthatcanexplainexperimental
| implications. | That | is, the | results | of the simulations | together | with |     |     |     |     |     |     |     |

findingsontheinvolvementofthehippocampusintheacquisition,
the model architecture provide, non-trivial and experimentally encoding, and context-dependent retrieval of both conditioning
testablenewinsightsintopotentialneuralmechanismsunderlying [13,98,99]andextinctionmemories[3,87].Futurerefinementsof
cued and contextual fear conditioning and extinction, ABA and the model, in combination with new experimental data are
ABCrenewal,andextinctionover-training.Inaddition,aspecific necessary for a better understanding of the detailed interactions
and important function of inhibition is sketched as a mechanism between hippocampus,mPFC andamygdala.
thatcouldenablemutualcompetitionbetweenfearandextinction
memories.Theseresultsallowustoprovideasynthesisofseveral Gamma oscillations
| experimental | findings | and | to propose | a role | for the | BA as a |           |      |      |              |         |     |                |

|              |          |     |            |        |         |         | We showed | that | high | connectivity | between |     | excitatory and |
nucleusthatintegratesinformationabouttheCSandthecontext.
|     |     |     |     |     |     |     | inhibitory | and within | inhibitory |     | neuron | populations | results in |

This brings it into the position to provide a context-dependent robust oscillations in the gamma range, characterized by high
instruction to downstream structures, enabling the switching of activity correlation among neurons. The main cause of these
states fromlow tohighfear andviceversa. oscillationswasthehighdegreeofsharedinputsamongneuronsas
Specifically, we propose that context modulates neuronal a result of the dense connectivity. We suggested two different,
activity within the BA, resulting in the formation of associations biologically plausible ways to reduce these oscillations: by either
between CS, US and context in this nucleus. During fear introducing heterogeneity in neuron properties and/or by
conditioning the CS{US{context representation signals reducing synaptic delays to sub-millisecond time scales. Yet
A
dangerandcausesahighfearstate.Duringextinction,thenewly
|                  |     |                                          |     |     |     |     | another | way would | be  | to have | synapses | exhibit | a certain |

| formedCS{context |     | representationsignalssafetyandsuppresses |     |     |     |     |         |           |     |         |          |         |           |
B transmissionfailurerate[100,101],resultinginactivitydependent
the fear state. Back in the conditioning context, the initial reductionoftheeffectiveconnectivity.However,wedonotwishto
representation dominates again (renewal). Thus, as far as neural imply that gamma oscillations do not exist in the BA. In fact, as
mechanisms within the BA are concerned, conditioning and noted earlier, gamma oscillations have been reported in the
extinction could be understood as mutual competition between amygdala under various conditions [76–79]. Here, we want to
different representations of fear and safety. Partial unlearning or emphasize the point that in networks with high connectivity,
erasure mayalso occur,althoughtoa limiteddegree. gamma range oscillations are a salient feature of the network
Memoriesareassumedtobestoredinadistributedmannerin dynamics. Therefore, they should be visible even in the ongoing
the brain [92]. Consistent with this view, fear-related memories activity, unless suppressing mechanisms, such as those elaborated
| may also | be distributed |     | among | different | nuclei within | the | here,are | ineffect. |     |     |     |     |     |

amygdala and brain regions connected to it [10]. Our model Severalsuggestionsforaspecificroleofgammaoscillationshave
suggests that context-related features of these distributed fear beenmadeinthepast.Forinstance,ithasbeenproposedthatin
memoriesarerepresentedintheBA.Thus,inactivationoftheBA the cortex or the hippocampus oscillations might contribute to
would impair context-related aspects of fear and extinction temporal encoding [102], sensory binding [103], attentional
PLoSComputationalBiology | www.ploscompbiol.org 11 March2011 | Volume 7 | Issue 3 | e1001104


selection[104]andmemoryformationorretrieval[105,106].Itis the SOP model, where US and CS have to coincide for
currently unclear whether these hypotheses also apply to the strengthening ofassociations totake place[115,116].
amygdala.Oscillationsinlowerfrequencyranges(deltaandtheta) Connectionist or parallel-distributed (PDP) models of fear
havealsobeenreported.Forexample,increasedthetaoscillations
|     |     |     |     |     |     |     |     | related | processes | go one | step further | than | symbolic | models | by  |

-thatsynchronizedwithhippocampalthetaactivity-wereshown
|     |     |     |     |     |     |     |     | introducing | networks | composed | of  | multiple, | mutually | connected |     |

to be related to conditioned freezing [107,108], whereas delta computationalunits.Onesuchmodel wassuccessfulincapturing
oscillations havebeen implicated in gating aversive stimuli [109]. certain features observed in fear conditioning studies [117]. Its
Gamma oscillations, on the other hand, have been suggested to main limitation, however, is the fact that it does not take into
facilitate interactions between the amygdala and connected account the different substructures within the amygdala, nor do
structures [78,110]. the computational units used in the model map to any
Here, because we modeled only the BA, we cannot give any biophysically realistic counterparts.
informed predictions about how gamma oscillations may affect Fortunately,thecomputationalpowerpresentlyavailableallows
| those various | interactions. |     | Moreover, | in  | our current | model, | we  |               |     |              |     |             |     |      |          |

|               |               |     |           |     |             |        |     | us to improve |     | these models | and | to overcome |     | many | of their |
haveusedplasticityonlyintheinputconnectionsandthosearenot
limitations.Themodelpresentedhereistoourknowledgethefirst
affectedbyoscillatoryactivityintherecurrentnetwork.However,
|     |     |     |     |     |     |     |     | large-scale | spiking | neuron | network | model | that | investigates | the |

beforeaddressingtheeffectsofgammaoscillationonthedynamics mechanisms of fear conditioning and extinction within the
of the BA network, it is of key importance to resolve amygdala using biologically realistic neurons in adequate detail.
experimentally whether gamma oscillations are indeed present in Themodelclosesttothisisacompartmentalmodelintroducedby
BAactivity and, ifso,underwhichconditions. [118]toinvestigatethefunctionoftheLAinfearconditioningand
extinction.However,[118]usedasmallnetworkcomposedofonly
Conditioned inhibition eighttwo-compartmentneuronsandfocusedonroleofthekinetics
| A well-known |     | behavioral | phenomenon |     | is conditioned |     | inhibi- |             |       |          |                      |     |     |             |     |

|              |     |            |            |     |                |     |         | of multiple | ionic | currents | in fear conditioning |     | and | extinction. | By  |
tion,referringtotheabilityofasecondCS(CS2)tosuppressthe
|     |     |     |     |     |     |     |     | contrast, | we modeled | the | BA using | a large | network | of 4000 | LIF |

conditioned response, after it has been paired several times with neurons, which enabled us to identify the network level
the first CS (CS+) in the absence of a US [57,111]. It is possible interactions involved in the formation of fear and extinction
| thattheCS2,referredtoasconditionedinhibitor,employssimilar |           |                 |            |                |       |             |        | memories.   |     |     |     |     |     |     |     |

| mechanisms                                                 | to        | those described |            | in our         | model | to suppress | the    |             |     |     |     |     |     |     |     |
| conditioned                                                | response. | That            | is, neural | subpopulations |       | in          | the BA | Conclusions |     |     |     |     |     |     |     |
encodingtheCS2might,similartoextinctionneurons,uselocal
|     |     |     |     |     |     |     |     | The | present | model provides | a   | plausible | explanation |     | for the |

inhibitorycircuitstosuppressfearneuronactivity.Futureworkis
|                  |     |             |                 |     |              |     |     | neural mechanisms |     | underlying | fear | conditioning |     | and extinction |     |

| needed toexplore |     | furtherthis | interestingline |     | ofreasoning. |     |     |                   |     |            |      |              |     |                |     |
withintheBA.Wedidnotaddressthequestionofhowtheneural
activitywithintheBAimpactsondownstreamstructures,suchas
| Conditioning | and | extinction |     | in the | same context |     |     |        |       |            |           |     |       |                  |     |

|              |     |            |     |        |              |     |     | CEA or | mPFC. | We neither | attempted | to  | model | the interactions |     |
Our model accounts for experimental paradigms that use a betweenhippocampusandmPFCinconditioningandextinction,
differentextinctioncontextfromtheconditioningone,butnotfor whichwouldrequireadditionalexperimentaldatatoconstrainthe
thoseinwhichfearconditioningandextinctionoccurinthesame possible models.Giventhese restrictions, weprovided aplausible
context.Forinstance,ifconditioningandextinctionbothoccurin
|         |        |            |         |      |         |        |         | mechanism | of  | how contextual | inputs | may | affect | the activity | of  |

| context | , then | only those | neurons | that | receive | inputs | in this |           |     |                |        |     |        |              |     |
A distinct neuronal subpopulations in the BA, enabling them to
| context will | be active. | Thus, | downstream |     | structures | will | not be |     |     |     |     |     |     |     |     |

controldownstreamstructuressuchastheCEA.Weproposedthat
| able to differentiate |      | between | fear     | conditioning |        | and extinction |      |                 |        |            |      |                |         |          |          |

|                       |      |         |          |              |        |                |      | context-related |        | aspects of | fear | and extinction |         | memories | are      |
| training solely       | from | spiking | activity | in the       | BA. It | is evident     | that |                 |        |            |      |                |         |          |          |
|                       |      |         |          |              |        |                |      | partially       | stored | in the BA  | and  | that they      | provide | a        | context- |
performingconditioningandextinctioninthesamecontextperse dependent instruction for the triggering or blocking of the fear-
increasesambiguity aboutthemeaningofthecontext.Thus, itis response. In addition, we showed how extinction training may
likely that circuits within the BA alone are not sufficient to solve mask previously acquired fear memories and, thus, provided an
thiscomputationalproblem.Both,adetaileddescriptionofneural account for renewal. Finally, our model, next to yielding several
activityduringthistypeofextinctionandamoredetailedanalysis
|                 |           |                |     |                |     |            |     | interesting       | predictions | discussed    |              | above,       | raises      | the important |         |

| of interactions | between   | the            | BA  | and downstream |     | structures | are |                   |             |              |              |              |             |               |         |
|                 |           |                |     |                |     |            |     | question          | of how      | downstream   | structures   |              | such        | as the        | CEA or  |
| required        | toaddress | thisbehavioral |     | phenomenon.    |     |            |     |                   |             |              |              |              |             |               |         |
|                 |           |                |     |                |     |            |     | mPFC discriminate |             | the activity | of           | the distinct | neuronal    |               | subpop- |
|                 |           |                |     |                |     |            |     | ulations          | within      | the BA.      | Is this      | problem      | solved      | purely        | on an   |
| Relation        | to other  | models         |     |                |     |            |     |                   |             |              |              |              |             |               |         |
|                 |           |                |     |                |     |            |     | anatomical        | level,      | e.g. by      | differential |              | projections | of            | the BA  |
Although a wealth of experimental studies exist on the subpopulations to specific target neurons? Or do specific features
amygdala and its role in fear conditioning and extinction, in the activity of the BA subpopulations, e.g. the statistical
computational or theoretical approaches to study amygdala structureofpairwiseorhigher-ordercorrelations,alsoplayarole,
function are largely lacking. Most of the previous theoretical providing downstream networks with a mechanism to distinguish
studies involve symbolic models [112,113], mainly based on the between them? These questions need to be addressed in future
| Rescorla-Wagner |     | rule [114]. | These | models | have | their merit | in  |               |     |                 |     |             |             |     |     |

|                 |     |             |       |        |      |             |     | workcombining |     | experimentaland |     | theoretical | approaches. |     |     |
describingbehavioralfindingssuchasgeneralization,blockingetc.
However,sincethesemodelstreattheamygdalaasa‘‘black-box’’,
|                                                                 |        |             |     |         |                     |     |     | Supporting |             | Information |            |         |     |      |         |

| it is not                                                       | within | their scope | to  | account | for neuroanatomical |     | or  |            |             |             |            |         |     |      |         |
|                                                                 |        |             |     |         |                     |     |     |            | Overlapping |             | contextual | inputs. | (A) | Venn | diagram |
| electrophysiologicaldata,thereforeprovidinglittleinsightintothe |        |             |     |         |                     |     |     | Figure     | S1          |             |            |         |     |      |         |
underlyingneuronalmechanismsinvolved.Despitetheseapparent illustrating overlap of CTX inputs. (B) Activity of BA neurons at
differences, it is still possible to draw some parallels to symbolic theendofextinctiontraining.VaryingtheoverlapofCTXinputs
models.Forinstance,inourmodel,potentiationofsynapsesoccurs toBAneuronsfrom0–100%resulted inathirdsubgroup, which
onlyifCSandCTXinputstemporallyoverlap.Thisissimilarto was active both during conditioning and extinction (persistent
PLoSComputationalBiology | www.ploscompbiol.org 12 March2011 | Volume 7 | Issue 3 | e1001104


neurons).Thehighertheoverlap,themoreneuronsinthisgroup conditioning.Thus,themodelpredictsthatlesionsofhippocampal
were active, as is reflected in the population rate. Note, that fear or prefrontal areas after conditioning may result in impaired
andextinctionneuronsstillexistedwiththelatteronessuppressing extinction. (right) When contextual inputs were removed after
theformer ones,even foran overlap of.50%. extinction,thenbothfearandextinctionneuronswereactiveand
Foundat:doi:10.1371/journal.pcbi.1001104.s001(0.13MBEPS) nogroupwasabletosuppresstheother.However,thefiringrates
of both groups were decreased, because contextual input was
FigureS2 ABCrenewalandextinctionover-training.Afterfear
lacking. The behavioral implication of these results may be
extinctionincontextBtheactivityofextinctionneurons(cyan)was
impairedABAas well asABC renewal (seemain text).
high,therebysuppressingtheactivityoffearneurons(amber)(left).
Foundat:doi:10.1371/journal.pcbi.1001104.s003(0.12MBEPS)
PresentingtheCSintheconditioningcontext-Aresultedinarapid
switchofactivity,withfearneuronssuppressingextinctionneurons Table S1 Model parameters. Parameters used in the rate and
activity(ABArenewal;seealsoFigure7andmaintext).Whenthe SNN model.
CSwaspresentedinadifferentcontext-C,thenagainfearneurons Foundat:doi:10.1371/journal.pcbi.1001104.s004(0.13MBPDF)
wereactive(ABCrenewal).However,theiractivitywasdecreased
compared to ABC renewal, because potentiated contextual input Acknowledgments
was now missing (middle). Our model suggests that extinction
over-training can abolish both ABA and ABC renewal (right; see We thank Philippe Gastrein and Francois Grenier for providing data
regardingtheelectrophysiologicalpropertiesofBAneurons.Wealsothank
text).
Man-Yi Yim and Ajith Padmanabhan for proof-reading the manuscript.
Foundat:doi:10.1371/journal.pcbi.1001104.s002(0.06MBEPS)
Finally, we would like to thank the two anonymous referees for their
Figure S3 Removal of CTX input. (left) Effects of removal of valuablecommentsthroughoutthereviewingprocess.
contextual input on fear and extinction neurons activity. When
contextual inputs were removed after conditioning, then during Author Contributions
extinctionsimulationnonewgroupofneuronsbecameactiveand,
Conceivedanddesignedtheexperiments:IVCHALAAAK.Performed
therefore, fear neurons remained active, as they were the only theexperiments:IVAK.Analyzedthedata:IVCHAK.Wrotethepaper:
groupofneuronsforwhichCSinputshadbeenpotentiatedduring IVCHALAAAK.
References
1. PavlovI(1927)Conditionedreflexes.Oxford,UK:OxfordUniversityPress. 20. Knierim JJ (2002) Dynamic interactions between local surface cues, distal
2. Bouton ME, Bolles RC (1979) Contextual control of the extinction of landmarks,andintrinsiccircuitryinhippocampalplacecells.JNeurosci22:
conditionedfear.LearnMotiv10:445–466. 6254–6264.
3. BoutonME,WestbrookRF,CorcoranKA,MarenS(2006)Contextualand 21. Kentros CG, Agnihotri NT, Streater S, Hawkins RD, Kandel ER (2004)
TemporalModulationofExtinction:BehavioralandBiologicalMechanisms. Increasedattentiontospatialcontextincreasesbothplacefieldstabilityand
BiolPsychiatry60:352–360. spatialmemory.Neuron42:283–295.
4. LeDouxJE(2000)Theamygdalaandemotion:aviewthroughfear.Oxford 22. LeutgebJK,LeutgebS,MoserMB,MoserEI(2007)Patternseparationinthe
UniversityPress,2ndedition.690p. dentategyrusandCA3ofthehippocampus.Science315:961–966.
5. MyersKM,DavisM(2007)Mechanismsoffearextinction.MolPsychiatry12: 23. Repa JC, Muller J, Apergis J, Desrochers TM, Zhou Y, et al. (2001) Two
120–150. different lateral amygdala cell populations contribute to the initiation and
6. QuirkGJ,MuellerD(2007)NeuralMechanismsofExtinctionLearningand storageofmemory.NatNeurosci4:724–731.
Retrieval.Neuropsychopharmacology33:56–72. 24. SahP,FaberESL,ArmentiaMLD,PowerJ(2003)Theamygdaloidcomplex:
7. RomanskiLM,ClugnetMC,BordiF,LeDouxJE(1993)Somatosensoryand anatomyandphysiology.PhysiolRev83:803–834.
auditoryconvergenceinthelateralnucleusoftheamygdala.BehavNeurosci 25. Nordlie E, Gewaltig MO, Plesser HE (2009) Towards Reproducible
107:444–450. DescriptionsofNeuronalNetworkModels.PLoSComputBiol5:e1000456.
8. Barot SK, Kyono Y, Clark EW, Bernstein IL (2008) Visualizing stimulus 26. PrinzAA,BucherD,MarderE(2004)Similarnetworkactivityfromdisparate
convergenceinamygdalaneuronsduringassociativelearning.ProcNatlAcad circuitparameters.NatNeurosci7:1345–1352.
SciUSA105:20959–20963. 27. GerstnerW,NaudR(2009)HowGoodAreNeuronModels?Science326:
9. SigurdssonT,Doye`reV,CainCK,LeDouxJE(2007)Long-termpotentiation 379–380.
in the amygdala: A cellular mechanism of fear learning and memory. 28. MorrisonA,MehringC,GeiselT,AertsenA,DiesmannM(2005)Advancing
Neuropharmacology52:215–227. the Boundaries of High-Connectivity Network Simulation with Distributed
10. Pare´D,QuirkGJ,LedouxJE(2004)NewVistasonAmygdalaNetworksin Computing.NeuralComput17:1776–1801.
ConditionedFear.JNeurophysiol92:1–9. 29. McDonald AJ (1998) Cortical pathways to the mammalian amygdala. Prog
11. LeDouxJE,IwataJ,CicchettiP,ReisDJ(1988)Differentprojectionsofthe Neurobiol55:257–332.
centralamygdaloidnucleus mediate autonomic and behavioral correlatesof 30. Tuunanen J, Pitka¨nen A (2000) Do seizures cause neuronal damage in rat
conditionedfear.JNeurosci8:2517–2529. amygdalakindling?EpilepsyRes39:171–176.
12. MullerJ,CorodimasKP,FridelZ,LedouxJE(1997)Functionalinactivationof 31. KuhnA,AertsenA,RotterS(2004)NeuronalIntegrationofSynapticInputin
thelateralandbasalnucleioftheamygdalabymuscimolinfusionpreventsfear theFluctuation-DrivenRegime.JNeurosci24:2345–2356.
conditioning to an explicit conditioned stimulus and to contextual stimuli. 32. Kumar A, Schrader S, Aertsen A, Rotter S (2008) The High-Conductance
BehavNeurosci111:683–691. StateofCorticalNetworks.NeuralComput20:1–43.
13. GoosensKA,MarenS(2001)ContextualandAuditoryFearConditioningare 33. KumarA,RotterS,AertsenA(2008)ConditionsforPropagatingSynchronous
MediatedbytheLateral,Basal,andCentralAmygdaloidNucleiinRats.Learn Spiking and Asynchronous Firing Rates in a Cortical Network Model.
Mem8:148–155. JNeurosci28:5268–5280.
14. Anglada-FigueroaD,QuirkGJ(2005)LesionsoftheBasalAmygdalaBlock 34. IzhikevichEM(2007)Solvingthedistalrewardproblemthroughlinkage of
ExpressionofConditionedFearButNotExtinction.JNeurosci25:9680–9685. STDPanddopaminesignaling.CerebCortex17:2443–2452.
15. Maren S, Poremba A, Gabriel M (1991) Basolateral amygdaloid multi-unit 35. KimJ,LeeS,ParkK,HongI,SongB,etal.(2007)Amygdaladepotentiation
neuronalcorrelatesofdiscriminativeavoidancelearninginrabbits.BrainRes andfearextinction.ProcNatlAcadSciUSA104:20955–20960.
549:311–316. 36. HongI,SongB,LeeS,KimJ,KimJ,etal.(2009)Extinctionofcuedfear
16. MuramotoK,OnoT,NishijoH,FukudaM(1993)Ratamygdaloidneuron memoryinvolvesadistinctformofdepotentiationatcorticalinputsynapses
responsesduringauditorydiscrimination.Neuroscience52:621–636. ontothelateralamygdala.EurJNeurosci30:2089–2099.
17. HerryC,CiocchiS,SennV,DemmouL,MullerC,etal.(2008)Switchingon 37. Bienenstock E, Cooper L, Munro P (1982) Theory for the development of
andofffearbydistinctneuronalcircuits.Nature454:600–606. neuron selectivity: orientation specificity and binocular interaction in visual
18. CiocchiS,HerryC,GrenierF,WolffSBE,LetzkusJJ,etal.(2010)Encodingof cortex.JNeurosci2:32–48.
conditioned fear in central amygdala inhibitory circuits. Nature 468: 277– 38. BearM,CooperL,EbnerF(1987)Aphysiologicalbasisforatheoryofsynapse
282. modification.Science237:42–48.
19. Wilson HR, Cowan JD (1972) Excitatory and Inhibitory Interactions in 39. Lisman J (1989) A mechanism for the Hebb and the anti-Hebb processes
LocalizedPopulationsofModelNeurons.BiophysJ12:1–24. underlyinglearningandmemory.ProcNatlAcadSciUSA86:9574–9578.
PLoSComputationalBiology | www.ploscompbiol.org 13 March2011 | Volume 7 | Issue 3 | e1001104


40. ShouvalHZ,BearMF,CooperLN(2002)AunifiedmodelofNMDAreceptor- 72. TraubRD,WhittingtonMA,StanfordIM,JefferysJGR(1996)Amechanism
dependent bidirectional synaptic plasticity. Proc Natl Acad Sci U S A 99: forgenerationoflong-rangesynchronousfastoscillationsinthecortex.Nature
10831–10836. 383:621–624.
41. ArtolaA,BrocherS,SingerW(1990)Differentvoltage-dependentthresholds 73. BrunelN,HakimV(1999)FastGlobalOscillationsinNetworksofIntegrate-
forinducinglong-termdepressionandlong-termpotentiationinslicesofrat and-FireNeuronswithLowFiringRates.NeuralComp11:1621–1671.
visualcortex.Nature347:69–72. 74. BrunelN,WangXJ(2003)WhatDeterminestheFrequencyofFastNetwork
42. Artola A, Singer W (1993) Long-term depression of excitatory synaptic Oscillations With Irregular Neural Discharges? I. Synaptic Dynamics and
transmissionanditsrelationshiptolong-termpotentiation.TrendsNeurosci Excitation-InhibitionBalance.JNeurophysiol90:415–430.
16:480–487. 75. Maex R, Schutter ED (2003) Resonant Synchronization in Heterogeneous
43. MalenkaRC,BearMF(2004)LTPandLTD:AnEmbarrassmentofRiches. NetworksofInhibitoryNeurons.JNeurosci23:10503–10514.
Neuron44:5–21. 76. Collins DR, Pelletier JG, Pare´ D (2001) Slow and fast (gamma) neuronal
44. LismanJ,SprustonN(2005)PostsynapticdepolarizationrequirementsforLTP oscillationsintheperirhinalcortexandlateralamygdala.JNeurophysiol85:
and LTD: a critique of spike timing-dependent plasticity. Nat Neurosci 8: 1661–1672.
839–841. 77. PonomarenkoAA,KorotkovaTM,HaasHL(2003)Highfrequency(200Hz)
45. HardieJ,SprustonN(2009)SynapticDepolarizationIsMoreEffectivethan oscillations and firing patterns in the basolateral amygdala and dorsal
Back-Propagating Action Potentials during Induction of Associative Long- endopiriformnucleusofthebehavingrat.BehavBrainRes141:123–129.
Term Potentiation in Hippocampal Pyramidal Neurons. J Neurosci 29: 78. PopescuAT,PopaD,PareD(2009)Coherentgammaoscillationscouplethe
3233–3241. amygdalaandstriatumduringlearning.NatNeurosci12:801–807.
46. Humeau Y, Shaban H, Bissiere S, Luthi A (2003) Presynaptic induction of 79. Pare´ D, Collins DR, Pelletier JG (2002) Amygdala oscillations and the
heterosynaptic associative plasticity in the mammalian brain. Nature 426: consolidationofemotionalmemories.TrendsCognSci6:306–314.
841–845. 80. NeltnerL,HanselD,MatoG,MeunierC(2000)SynchronyinHeterogeneous
47. Frey U, Morris RGM (1997) Synaptic tagging and long-term potentiation. NetworksofSpikingNeurons.NeuralComp12:1607–1641.
Nature385:533–536. 81. Denker M, Timme M, Diesmann M, Wolf F, Geisel T (2004) Breaking
48. BarriaA,MullerD,DerkachV,GriffithLC,SoderlingTR(1997)Regulatory SynchronybyHeterogeneityinComplexNetworks.PhysRevLett92:74103.
phosphorylationofAMPA-typeglutamatereceptorsbyCaM-KIIduringlong- 82. MarkramH,Toledo-RodriguezM,WangY,GuptaA,SilberbergG,etal.
termpotentiation.Science276:2042–2045. (2004)Interneuronsoftheneocorticalinhibitorysystem.NatRevNeurosci5:
49. HarleyCW(2004)Norepinephrineanddopamineaslearningsignals.Neural 793–807.
Plast11:191–204. 83. Jonas P, Bischofberger J, Fricker D, Miles R (2004) Interneuron Diversity
50. McGaughJL(2004)Theamygdalamodulatestheconsolidationofmemoriesof series:Fastin,fastout–temporalandspatialsignalprocessinginhippocampal
emotionallyarousingexperiences.AnnuRevNeurosci27:1–28. interneurons.TrendsNeurosci27:30–40.
51. TullyK,LiY,TsvetkovE,BolshakovVY(2007)Norepinephrineenablesthe 84. VlachosI,KumarA,LuthiA,AertsenA(2009)Dynamicalemergenceoffear
inductionofassociativelong-termpotentiationatthalamo-amygdalasynapses. andextinctioncellsintheamygdala-acomputationalmodel.BMCNeurosci
ProcNatlAcadSciUSA99104:14146–50. 10:P142.
52. Faber ESL, Delaney AJ, Power JM, Sedlak PL, Crane JW, et al. (2008) 85. RoxinA,BrunelN,HanselD(2005)RoleofDelaysinShapingSpatiotemporal
Modulation of SK Channel Trafficking by Beta Adrenoceptors Enhances Dynamics of Neuronal Activity in Large Networks. Phys Rev Lett 94:
ExcitatorySynapticTransmissionandPlasticityintheAmygdala.JNeurosci 238103–4.
28:10803–10813. 86. Berlau DJ, McGaugh JL (2006) Enhancement of extinction memory
53. Pinard C, Muller J, Mascagni F, McDonald A (2008) Dopaminergic consolidation:TheroleofthenoradrenergicandGABAergicsystemswithin
innervation of interneurons in the rat basolateral amygdala. Neuroscience thebasolateralamygdala.NeurobiolLearnMem86:123–132.
157:850–863. 87. Corcoran KA, Desmond TJ, Frey KA, Maren S (2005) Hippocampal
54. Muller J, Mascagni F, McDonald A (2009) Dopaminergic innervation of Inactivation Disrupts the Acquisition and Contextual Encoding of Fear
pyramidal cells in the rat basolateral amygdala. Brain Struct Funct 213: Extinction.JNeurosci25:8978–8987.
275–288. 88. Ji J, Maren S (2005) Electrolytic lesions of the dorsal hippocampus disrupt
55. DavisonAP,Bru¨derleD,EpplerJ,KremkowJ,MullerE,etal.(2008)PyNN:A renewalofconditionalfearafterextinction.LearnMem12:270–276.
CommonInterfaceforNeuronalNetworkSimulators.FrontNeuroinformatics 89. CorcoranKA,MarenS(2004)FactorsRegulatingtheEffectsofHippocampal
2:11. InactivationonRenewalofConditionalFearAfterExtinction.LearnMem11:
56. GewaltigMO,DiesmannM(2007)Nest(neuralsimulationtool).Scholarpedia 598–603.
2:1430. 90. JiJ,MarenS(2007)Hippocampalinvolvementincontextualmodulationof
57. Bouton ME (2004) Context and Behavioral Processes in Extinction. Learn fearextinction.Hippocampus17:749–758.
Mem11:485–494. 91. Barot SK, Chung A, Kim JJ, Bernstein IL (2009) Functional Imaging of
58. HarrisJA, JonesML,Bailey GK,WestbrookRF(2000)Contextualcontrol Stimulus Convergence in Amygdalar Neurons during Pavlovian Fear
overconditionedrespondinginanextinctionparadigm.JExpPsycholAnim Conditioning.PLoSOne4:e6156.
BehavProcess26:174–185. 92. Fuster JM (1998) Distributed Memory for Both Short and Long Term.
59. BoutonME(2002)Context,ambiguity,andunlearning:sourcesofrelapseafter NeurobiolLearnMem70:268–274.
behavioralextinction.BiolPsychiatry52:976–986. 93. MarenS,FanselowMS(1995)Synapticplasticityinthebasolateralamygdala
60. Denniston JC, Chang RC, Miller RR (2003) Massive extinction treatment induced by hippocampal formation stimulation in vivo. J Neurosci 15:
attenuatestherenewaleffect.LearnMotiv34:68–86. 7548–7564.
61. WoodruffAR,SahP(2007)Networksofparvalbumin-positiveinterneuronsin 94. Pitka¨nen A(2000) Connectivity of the rat amygdaloid complex. NewYork:
thebasolateralamygdala.JNeurosci27:553–563. AmygdalaAfunctionalanalysisOxfordUniversityPress.pp31–115.
62. Gray CM, Singer W (1989) Stimulus-specific neuronal oscillations in 95. Hobin JA, Goosens KA, Maren S (2003) Context-Dependent Neuronal
orientation columns of cat visual cortex. Proc Natl Acad Sci U S A 86: ActivityintheLateralAmygdalaRepresentsFearMemoriesafterExtinction.
1698–1702. JNeurosci23:8410–8416.
63. Buzsaki G, Horvath Z, Urioste R, Hetke J, Wise K (1992) High-frequency 96. HuguesS,GarciaR(2007)Reorganizationoflearning-associatedprefrontal
networkoscillationinthehippocampus.Science256:1025–1027. synaptic plasticity between the recall of recent and remote fear extinction
64. BraginA,JandoG,NadasdyZ,HetkeJ,WiseK,etal.(1995)Gamma(40–100 memory.LearnMem14:520–524.
Hz)oscillationinthehippocampusofthebehavingrat.JNeurosci15:47–60. 97. Farinelli M, Deschaux O, Hugues S, Thevenet A, Garcia R (2006)
65. WhittingtonMA,TraubRD,JefferysJGR(1995)Synchronizedoscillationsin Hippocampal train stimulation modulates recallof fear extinction indepen-
interneuron networks driven bymetabotropicglutamate receptor activation. dently of prefrontalcortex synaptic plasticity and lesions. Learn Mem 13:
Nature373:612–615. 329–334.
66. BartosM,VidaI,FrotscherM,MeyerA,MonyerH,etal.(2002)Fastsynaptic 98. Anagnostaras SG, Gale GD, Fanselow MS (2001) Hippocampus and
inhibition promotes synchronized gamma oscillations in hippocampal inter- contextualfearconditioning:Recentcontroversiesandadvances.Hippocam-
neuronnetworks.ProcNatlAcadSciUSA99:13222–13227. pus11:8–17.
67. BartosM,VidaI,JonasP(2007)Synapticmechanismsofsynchronizedgamma 99. Rudy JW, Huff NC, Matus-Amat P (2004) Understanding contextual fear
oscillationsininhibitoryinterneuronnetworks.NatRevNeurosci8:45–56. conditioning:insightsfromatwo-processmodel.NeurosciBiobehavRev28:
68. LyttonWW,SejnowskiTJ(1991)Simulationsofcorticalpyramidalneurons 675–685.
synchronizedbyinhibitoryinterneurons.JNeurophysiol66:1059–1079. 100. Hessler NA, Shirke AM, Malinow R (1993) The probability of transmitter
69. Erb M, Aertsen A (1992) Dynamics of activity in biology-oriented neural releaseatamammaliancentralsynapse.Nature366:569–572.
networkmodels:stabilityatlowfiringrates.In:AertsenA,BraitenbergV,eds. 101. Gulya´sAI,MilesR,SkA,To´thK,TamamakiN,etal.(1993)Hippocampal
Information Processing in the Cortex: Experiments and Theory. Berlin: pyramidalcellsexciteinhibitoryneuronsthroughasinglereleasesite.Nature
Springer.pp477. 366:683–687.
70. AertsenA,ArndtM(1993)Responsesynchronizationinthevisualcortex.Curr 102. Singer W, Gray CM (1995) Visual Feature Integration and the Temporal
OpinNeurobiol3:586–594. CorrelationHypothesis.AnnuRevNeurosci18:555–586.
71. VreeswijkC,AbbottLF,ErmentroutGB(1994)Wheninhibitionnotexcitation 103. vonderMalsburgC(1995)Bindinginmodelsofperceptionandbrainfunction.
synchronizesneuralfiring.JComputNeurosci1:313–321. CurrOpinNeurobiol5:520–526.
PLoSComputationalBiology | www.ploscompbiol.org 14 March2011 | Volume 7 | Issue 3 | e1001104


104. FriesP,ReynoldsJH,RorieAE,DesimoneR(2001)ModulationofOscillatory 111. RescorlaR(1969)Pavlovianconditionedinhibition.PsycholBull72:77–94.
| Neuronal Synchronization | by  | Selective Visual Attention. | Science 291: |     |     |     |     |

112. NewellA,SimonHA(1976)Computerscienceasempiricalinquiry:symbols
| 1560–1563. |     |     |     | andsearch.CommunACM19:113–126. |     |     |     |

105. Lisman JE, Idiart MA (1995) Storage of 7 +/2 2 short-term memories in 113. Schmajuk NA (2008) Computational models of classical conditioning.
oscillatorysubcycles.Science267:1512–1515.
Scholarpedia,3:1664.
106. MontgomerySM,Buzsa´kiG(2007)Gammaoscillationsdynamicallycouple 114. Rescorla R (2008) Rescorla-Wagner model. http://www.scholarpedia.org/
hippocampalCA3andCA1regionsduringmemorytaskperformance.Proc
article/Rescorla-Wagner.
NatlAcadSciUSA104:14495–14500.
115. WagnerA(1981)SOP:Amodelofautomaticmemoryprocessinginanimal
107. Seidenbecher T, Laxmi TR, Stork O, Pape HC (2003) Amygdalar and behavior.In:SpearNE,MillerRR,eds.Informationprocessinginanimals:
| hippocampal | theta rhythm synchronization | during | fear memory retrieval. |     |     |     |     |

Memorymechanisms.Hillsdale:Erlbaum.pp5–47.
Science301:846–850. 116. BrandonSE,VogelEH,WagnerAR(2003)StimulusrepresentationinSOP:I:
| 108. Pape HC, Narayanan | RT, Smid | J, Stork O, Seidenbecher | T (2005) Theta |     |     |     |     |

Theoreticalrationalizationandsomeimplications.BehavProcesses62:5–25.
| activity in neurons | and networks | of the amygdala related | to long-term fear |     |     |     |     |

117. ArmonyJL,Servan-SchreiberD,CohenJD,LeDouxJE(1997)Computational
memory.Hippocampus15:874–880. modelingofemotion:explorationsthroughtheanatomyandphysiologyoffear
109. CraneJW,WindelsF,SahP(2009)OscillationsintheBasolateralAmygdala:
conditioning.TrendsCognSci1:28–34.
| Aversive Stimulation | Is State | Dependent and Resets | the Oscillatory Phase. |     |     |     |     |

JNeurophysiol102:1379–1387. 118. LiG,NairSS,Quirk GJ(2009)ABiologicallyRealisticNetworkModel of
|     |     |     |     | Acquisition | and Extinction of Conditioned | Fear Associations | in Lateral |

110. BauerEP,PazR,PareD(2007)GammaOscillationsCoordinateAmygdalo-
AmygdalaNeurons.JNeurophysiol101:1629–1646.
RhinalInteractionsduringLearning.JNeurosci27:9369–9379.
PLoSComputationalBiology | www.ploscompbiol.org 15 March2011 | Volume 7 | Issue 3 | e1001104

---
**Source PDF:** `2021_27_article.pdf`
