|     |     | [Re]     | How | Attention   |         |     | Can      | Create |                | Synaptic      | Tags | for   | the |

|     |     | Learning |     | of          | Working |     | Memories |        |                | in Sequential |      | Tasks |     |
|     |     | Erwan    | Le  | Masson1,2,3 |         | and | Frédéric |        | Alexandre2,1,3 |               |      |       |     |
1LaBRI, Université de Bordeaux, Bordeaux INP, CNRS, UMR 5800, Talence, France 2INRIA
Bordeaux Sud-Ouest, 200 Avenue de la Vieille Tour, 33405 Talence, France 3IMN, Université
|     |     | de Bordeaux, |     | CNRS, | UMR | 5293, | Bordeaux, | France |     |     |     |     |     |

frederic.alexandre@inria.fr
Editor
Olivia Guest
|     |     | A   | reference | implementation |     |     | of  |     |     |     |     |     |     |

Reviewers
|     |     |     | → How | Attention | Can | Create | Synaptic | Tags | for | the Learning | of Working | Memories |     |

Julien Vitay
|     |     |     | in  | Sequential | Tasks, | J. Rombouts, |     | M.  | Bohte | and P. Roelfsema | (2015), | PLoS |     |

Etienne Roesch
|                |         |     | Computational |     | Biology |     | 11.3, e1004060. |     | DOI: | 10.1371/journal.pcbi.1004060 |     |     |     |

| Received Aug,  | 9, 2016 |     |               |     |         |     |                 |     |      |                              |     |     |     |
| Accepted Dec,  | 1, 2016 |     |               |     |         |     |                 |     |      |                              |     |     |     |
| Published Dec, | 9, 2016 |     |               |     |         |     |                 |     |      |                              |     |     |     |
Introduction
Licence CC-BY
Thereferencepaper[2]introducesanewreinforcementlearningmodelcalledAttention-
Competing Interests: Gated MEmory Tagging (AuGMEnT). The results presented suggest new approaches
| The authors | have declared that |     |     |     |     |     |     |     |     |     |     |     |     |

in understanding the acquisition of tasks requiring working memory and attentional
| no competing | interests exist. |     |     |     |     |     |     |     |     |     |     |     |     |

feedback, as well as biologically plausible learning mechanisms. The model also im-
proves on previous reinforcement learning schemes by allowing tasks to be expressed
|           |            | more | naturally | as  | a sequence |     | of inputs | and | outputs. |     |     |     |     |

|  Article | repository |      |           |     |            |     |           |     |          |     |     |     |     |
A Python implementation of the model is available on the author’s GitHub page
[1] which helped to verify the correctness of the computations. The script written for
 Code repository
|     |     | this | replication | also | uses | Python | along | with | NumPy. |     |     |     |     |

 Data repository
Methods
Model
The model is composed of three layers: sensory, association and motor or Q-value.
The association layer has specialized memory units keeping trace of the sensory sig-
nal variation to build an internal state of the environment. By implementing the
SARSA((cid:21)) algorithm, the model is capable of predicting the reward as a function of
all its possible actions. Attentional feedback is used during learning, meaning only
synapses participating in the decision are updated. All computations are done locally
at the unit’s level, which is a strong argument to present AuGMEnT as biologically
plausible.
Theinitialintentionwastoimplementthemodelusinganartificialneuralnetwork
simulator. The simulation tool ANNarchy [5] was considered for its ability to simu-
late rate-coded networks. Unfortunately, there were several incompatibilities with
AuGMEnT. The fixed order of evaluation between entities, i.e. connections then pop-
ulations, and the unspecified order of evaluation between different populations make
it difficult to implement cascading evaluations. The use of ANNarchy was abandoned
and it was instead decided to write a custom script to simulate the network.
|           | j                   |     |     |     |     |     |     |     |     |     |          | j      | j         |

| ReScience | rescience.github.io |     |     |     |     | 1   |     |     |     |     | Dec 2016 | Volume | 2 Issue 1 |


The paper’s description of the model details update functions for all populations
and connections and is relatively straight forward to implement. Some informations
are however missing for equation 17: the initial value for q (t(cid:0)1) is not provided and
a
thearticleomitsthatq a′(t)needstobesetto0whenreceivingtheend-trialsignal,only
mentioning a (cid:14) that reflects the transition to the terminal state. This information can
actually be found in the 2012 conference paper about AuGMEnT [4]. Also, when it is
(t(cid:0)1)istheonlyvaluewhich
|     |     | saidthatQ-values | are | set to zeroattheendofatrial,q |     |     | a   |     |

needs to be reset. It might also be useful to clarify the nature of the feedback weights
w′ in equations 14 and 16: once an action is selected, only the feedback synapses
leaving the corresponding selected Q-value unit are activated to update tags, more
precisely: w′ = w (cid:2)z . The model could also have dedicated feedback connections
|     |     |                 | ij ij  | i     |                     |     |                    |     |

|     |     | but the simpler | method | is to | use the feedforward |     | synapses’ weights. |     |
To offer some discussion about the model and its limits, the first point to bring
forward would be its artificial time management. The extreme discretization of time
and explicit signals such as trial begin and end make it difficult to consider real-time
simulation or even realistic environments implementations. These constraints became
apparent when trying to use ANNarchy as it is not designed to work with large time
steps. In fact, the authors have published a “continuous” version of AuGMEnT [7],
as well as a “learning to reset” version [3] to address theses issues. As a whole, we
have found these mechanisms for artificial time management rather misleading when
reproducingthemodel,andprovidingadhocsolutions,notrobustnorgenericenough.
Wewouldconsequentlyrecommendtousethemwithparsimonyandonlywithastrong
justification.
Another possible weakness worth noting is the ambiguity of some memory traces.
Because the traces in memory units are defined as the sums of changes in input, there
exist sequences the model would be incapable of distinguishing. For example, the
sequences ((0, 0), (1, 0), (1, 1)) and ((0, 0), (0, 1), (1, 1)) have the
|     |     | same memory | traces | (1, 1). |     |     |     |     |

Tasks
The descriptions of the tasks used to test the network are somewhat minimal and it
was necessary to refer to other resources for more informations. In this section, some
|     |     | details of | implementation | are | exposed. |     |     |     |

Forthefixationtasks,i.e.saccade/anti-saccadeandprobabilisticdecisionmaking,
|     |     | the sequence | of phases    | is as listed: |           |     |     |     |

|     |     | 1. Begin:    | blank screen | for           | one step. |     |     |     |
2. Fixation: fixation point on screen for a maximum of 8 steps. Once the network
has fixated the point, it has to maintain fixation for an additional step before
|     |     | moving | on to the | next phase | with | a potential | reward. 1 |     |

3. Cues: all visual cues are displayed (over several steps when there are multiple
shapes).
|     |     | 4. Delay: | only the | fixation | points is | on screen | for two steps. |     |

5. Go: the screen appears blank for a maximum of 10 steps. The network has to
choose a direction to look at, if it chooses the intended target, it is rewarded.
6. End: extra step to give the final reward and signal the end of the trial with a
|     |     | blank | display. |     |     |     |     |     |

Additionalinformationswerefoundintheauthor’simplementationofthesaccade/anti-
saccade task: once the network has fixated the point in the Fixation phase, it has to
1Inthecode,thisphaseissplitinaWait
phasetowaitforthenetworktofixateonceandFixate
phasetoensureitmaintainsfixation.
|           | j                   |     |     |     |     |     | j               | j         |

| ReScience | rescience.github.io |     |     | 2   |     |     | Dec 2016 Volume | 2 Issue 1 |


maintain fixating until the Go signal when the screen turns off, otherwise the experi-
ment is failed. Moreover, during the Go phase, the gaze can only be chosen once, if it
is not the target, the trial fails.
The provided code did not implement the probabilistic decision making task but,
fortunately,theoriginalexperiment’sarticle[6]providedamorethoroughmethodology
description. The shaping strategy for the probabilistic decision making task consists
in gradually increasing the difficulty of the task. Table 3 in the article describes
all 8 levels of difficulty. The column # Input Symbols is the size of the subset of
shapes. The network is not presented all shapes immediately: first, the two shapes
withinfiniteweightsareused,thenshapeswiththesmallestabsoluteweightsareadded
asthedifficultyincreases. ThecolumnSequenceLengthisthenumberofshapesshown
duringatrial. Themoreshapesthereareonscreen,themoredifficultitistodetermine
which target should be chosen. A number of settings is randomized, such as which
shapes should appear, their order of apparition, but also their locations around the
fixation point. The first shape can appear in any of the 4 locations, the second in any
of the remaining 3 locations, etc. If the total weight of the input symbols is infinite
the corresponding target is guaranteed to give the reward. If the total weight is 0,
meaningbothtargetsareequallylikelytoberewarded, thenetworkcanlookineither
direction for the trial to be successful, but only one random target gives a reward.
Finally, the triangle and heptagon, shapes with infinite weights, cancel each other in
the computation of the total weight.
Results
Implementations Comparison
As both codes use NumPy and identical data structures, they function in very similar
way. Themaindifferenceistheirstructuressincethereplicationextensivelyusesobject
oriented paradigms for readability. The computations in [1] variate in two points: the
initial value of q
a
(t(cid:0)1) is set to q a′(t) whereas the replication script simply uses 0
and the Q-values are rounded to 5 decimals. From our tests these modifications do
not yield better results. The replication offers a 40% speedup, mostly from the way it
handles bias weights: they are created alongside the units’ activities instead of being
concatenated before every computation. A profiling of the author’s code indicates
most of its execution time is spent inside the function hstack.
Replicated Data
Only the saccade/anti-saccade task and the probabilistic decision making task were
implemented. For the probabilistic decision making task, the results are very similar.
However, the saccade/anti-saccade task results are slightly worse than announced in
the original article. The results presented in table 1 were obtained using the same
parameters as in tables 1 and 2 of the reference article. Success designates the ratio
of networks which successfully learned the task and Convergence the median number
of trials necessary to learn it over 10,000 networks for saccade/anti-saccade and 100
networks for probabilistic decision making. Since the results are fairly sensible to the
task’s protocol, it is possible the differences for the saccade tasks come from undoc-
umented changes in the experiments. Qualitative results such as the use of shaping
strategy to obtain better performances are confirmed by this replication. See also
figures 1and 2forthereplicatedactivitytracesoffigures2Dand4Cinthereference
article.


Figure 1: Q-value units’ Activity for the Saccade/Anti-saccade Task (reproduction of figure
2D).The“Fixate”actiondominatesuntilthe“Go”phasewherethemodelcorrectlychoosesthe
direction to look at. As in the reference article, there is a noticeable reaction after the “Cue”
phase.
|     |     |                 |         | Table          | 1: Results |                    |             |

|     |     | Task            |         | Success in [2] | Success    | Convergence in [2] | Convergence |
|     |     | Saccade with    | shaping | 99.45%         | 90.55%     | 4100 trials        | 3970 trials |
|     |     | Saccade without | shaping | 76.41%         | 59.10%     | -                  | 4785 trials |
Probabilistic decision 99.0% 100.0% 55234 trials 55988 trials
Conclusion
Theresultsobtainedarecomparabletothoseannouncedinthearticle. Ambiguitiesin
the experiments’ descriptions could be the cause for worse performances, but do not
|           |                     | contradict | the article’s | overall conclusion. |     |                 |           |

|           | j                   |            |               |                     |     | j               | j         |
| ReScience | rescience.github.io |            |               | 4                   |     | Dec 2016 Volume | 2 Issue 1 |


Figure 2: Q-value units’ Activity for the Probabilistic Decision Making Task (reproduction of
figure 4C). For both trials, the green target in the best choice. Once again, the model maintains
|           |                     | fixation until | the “Go” phase | where it makes | the correct decision. |                 |           |

|           | j                   |                |                |                |                       | j               | j         |
| ReScience | rescience.github.io |                |                | 5              |                       | Dec 2016 Volume | 2 Issue 1 |


References
[1] J. Rombouts. Implementation of simple AuGMEnT network example. url: https://github.
com/JRombouts/augment.
[2] J. Rombouts, S. Bohte, and P. Roelfsema. “How Attention Can Create Synaptic Tags for
the Learning of Working Memories in Sequential Tasks”. In: PLoS Computational Biology
11.3 (2015), e1004060. doi: 10.1371/journal.pcbi.1004060.
[3] J.Rombouts,P.Roelfsema,andS.Bohte.“LearningResetsofNeuralWorkingMemory”.In:
22nd European Symposium on Artificial Neural Networks, Computational Intelligence And
Machine Learning. 2014. url: http://www.i6doc.com/en/livre/?GCOI=28001100432440.
[4] J. Rombouts, P. Roelfsema, and S. Bohte. “Neurally Plausible Reinforcement Learning of
Working Memory Tasks”. In: Advances in Neural Information Processing Systems 25. 2012.
url: http://papers.nips.cc/paper/4813-neurally-plausible-reinforcement-learning-of-
working-memory-tasks.
[5] J. Vitay, H. Dinklebach, and F. Hamker. “ANNarchy: a code generation approach to neural
simulationsonparallelhardware”.In:FrontiersNeuroinformatics 9.19(2015).doi:10.3389/
fninf.2015.00019.
[6] T.YangandM.Shalden.“Probabilisticreasoningbyneurons”.In:Nature 447.7148(2007),
pp. 1075–80. doi: 10.1038/nature05852.
[7] D.Zambrano,P.Roelfsema,andS.Bohte.“Continuous-timeon-policyneuralReinforcement
Learning of working memory tasks”. In: International Joint Conference on Neural Networks
(2015). doi: 10.1109/IJCNN.2015.7280636.

---
**Source PDF:** `2016_01_article.pdf`
