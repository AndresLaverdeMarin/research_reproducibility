|     |     | [Re]      | Speed/accuracy |               |        |     | trade-off | between   |     | the       | habitual |     |

|     |     | and       | the            | goal-directed |        |     | processes |           |     |           |          |     |
|     |     | Guillaume |                | Viejo1,       | Benoît |     | Girard1,  | and Mehdi |     | Khamassi1 |          |     |
1Sorbonne Universités, UPMC Univ Paris 06, CNRS, Institute of Intelligent Systems and
|     |     | Robotics | (ISIR), | F-75005 |     | Paris, France |     |     |     |     |     |     |

guillaume.viejo@isir.upmc.fr
Editor
Nicolas P. Rougier
|     |     | A   | reference | implementation |     |     | of  |     |     |     |     |     |

Reviewers
|     |     |     | → Speed/accuracy |     | trade-off |     | between the | habitual | and the | goal-directed | processes, |     |

Julien Vitay
|     |     |     | M.  | Keramati, | A.  | Dezfouli, | P. Piray, PLoS | computational |     | biology, | 7, 2011 |     |

Georgios Detorakis
| Received Jan, | 20, 2016 |     |     |     |     |     |     |     |     |     |     |     |

| Accepted Feb, | 9, 2016  |     |     |     |     |     |     |     |     |     |     |     |
Introduction
| Published Feb, | 10, 2016 |     |     |     |     |     |     |     |     |     |     |     |

Licence CC-BY This study is a reference implementation of Keramati, Dezfouli, and Piray [2] that
proposed an arbitration mechanism between a goal-directed strategy and a habitual
Competing Interests:
strategy, used to model the behavior of rats in instrumental conditionning tasks. The
The authors have declared that habitualstrategyistheKalmanQ-LearningfromGeist,Pietquin,andFricout[1]. We
| no competing | interests exist. |     |     |     |     |     |     |     |     |     |     |     |

replicate the results of the first task, i.e. the devaluation experiment with two states
and two actions. The implementation is in python with numpy, scipy and matplotlib
 library. The authors couldn’t provide the original implementation and we are not
| Article | repository |       |          |                 |     |     |            |     |     |     |     |     |

|         |            | aware | of other | implementations |     |     | elsewhere. |     |     |     |     |     |
 Code repository
Methods
Weusedthedescriptionofthemodelfromtheoriginalarticleexceptfortheimplemen-
tationoftheKalmanQ-LearningwhichwetookfromGeist,Pietquin,andFricout[1].
We used the same parameters as the original article except for the update rate of the
transition function ϕ, the initialization of the covariance matrice and an uncentered
transform parameter (cid:20) that were not mentionned in the original article. The largest
uncertaintyaboutthemodelconcernedthedevaluationprocedure. Besidessettingthe
rewardrtonull,theauthorsstatedthat“Formodelingthedevaluationoftheoutcome
in the first two simulations, R(S ;EM) is set to -1.” As this notation (R(S ;EM))
|     |     |     |     |     |     |     | 1   |     |     |     |     | 1   |

is not defined in the rest of the article, we assumed that it is R^(S ;EM) updated by

|     |     | equation | (14)           | in       | the original |             | article.       |             |        |     |        |     |

|     |     |          | The parameters |          | are          | as follows  | :              |             |        |     |        |     |
|     |     |          |                | Name     |              | Description |                |             |        |     | Value  |     |
|     |     |          |                | (cid:27) |              | Updating    | rate of        | the average | reward |     | 0.02   |     |
|     |     |          |                | (cid:17) |              | Variance    | of evolution   | noise       |        |     | 0.0001 |     |
|     |     |          |                | P        |              | Variance    | of observation | noise       |        |     | 0.05   |     |
n
|           |                     |     |     | (cid:12) |     | Rate     | of exploration |        |          |      | 1.0    |           |

|           |                     |     |     | (cid:26) |     | Update   | rate of the    | reward | function |      | 0.1    |           |
|           |                     |     |     | (cid:13) |     | Discount | factor         |        |          |      | 0.95   |           |
|           | j                   |     |     |          |     |          |                |        |          |      | j      | j         |
| ReScience | rescience.github.io |     |     |          |     | 1        |                |        | Feb      | 2016 | Volume | 2 Issue 1 |


|     |     |     | Name     |     | Description    |               |                |             | Value |     |

|     |     |     | (cid:28) |     | Time           | step of graph | exploration    |             | 0.08  |     |
|     |     |     | depth    |     | Depth          | of search     | in graph       | exploration | 3     |     |
|     |     |     | ϕ        |     | Update         | rate of       | the transition | function    | 0.5   |     |
|     |     |     | init     | cov | Initialisation | of            | covariance     | matrice     | 1.0   |     |
|     |     |     | (cid:20) |     | Unscentered    | transform     |                | parameters  | 0.1   |     |
We describe the algorithm of our implementation in details. The process of action
|     |     | selection | and reward | update | are | separated | for | clarity. |     |     |

Initialization
|     |     |     | Q(s;a)Goal(cid:0)Directed |                    |                    | =f0;:::g     |                      |     |     |     |

|     |     |     | Q(s;a)Habitual            |                    | =f0;:::g           |              |                      |     |     |     |
|     |     |     | # Covariance              |                    | matrix             |              |                      |     |     |     |
|     |     |     |                           | 0                  |                    |              |                      | 1   |     |     |
|     |     |     |                           | cov(cid:2)(cid:17) |                    | 0 :::        | 0                    |     |     |     |
|     |     |     |                           | B                  |                    |              | .                    | C   |     |     |
|     |     |     |                           | B                  | cov(cid:2)(cid:17) |              | .                    | C   |     |     |
|     |     |     |                           | B 0                |                    | :::          | .                    | C   |     |     |
|     |     |     | (cid:6)=B                 |                    |                    |              |                      | C   |     |     |
|     |     |     |                           | .                  |                    | ...          |                      |     |     |     |
|     |     |     |                           | @ .                |                    |              |                      | A   |     |     |
|     |     |     |                           | .                  |                    | :::          | 0                    |     |     |     |
|     |     |     |                           | 0                  |                    | :::          | 0 cov(cid:2)(cid:17) |     |     |     |
|     |     |     | R(S1;EM)=1                |                    | #                  | Reward value |                      |     |     |     |
|     |     |     | R(cid:22) =0              | # Reward           | rate               |              |                      |     |     |     |
R^(s;a)=f0;:::g
|     |     |      |      |     | #   | Reward | function |     |     |     |

|     |     | Main | Loop |     |     |        |          |     |     |     |
FOR i=1:T
|     |     |     |     | s t =S 0 | # Initial | state      |     |             |          |     |

|     |     |     |     | IF i=T   |           | # Moderate |     | / Extensive | training |     |
devaluation
R(S1;EM)=0
R^(S1;EM)=(cid:0)1
∧
|     |     |     |     |                | ̸=S1          | ̸=EM           |      |     |     |     |

|     |     |     |     | WHILE          | s t           | a t            |      |     |     |     |
|     |     |     |     | a =Selection(s |               | )              |      |     |     |     |
|     |     |     |     | t              |               | t              |      |     |     |     |
|     |     |     |     | r =R(s         | ;a            | )              |      |     |     |     |
|     |     |     |     | t              | t             | t              |      |     |     |     |
|     |     |     |     | s              | =transition(s |                | ;a ) |     |     |     |
|     |     |     |     | t+1            |               |                | t t  |     |     |     |
|     |     |     |     | Update(s       | t             | ;a t ;s t+1 ;r | t )  |     |     |     |
Selection
|           |                     |     | # Sort | the Q-values          |            | in descending | order |     |                 |           |

|           |                     |     | fa     | ;:::;ai;:::g sort(Q(s |            |               | ;a )) |     |                 |           |
|           |                     |     | 1      |                       |            | t             | i     |     |                 |           |
|           |                     |     | # VPI  | : Value               | of Precise | Information   |       |     |                 |           |
|           | j                   |     |        |                       |            |               |       |     | j               | j         |
| ReScience | rescience.github.io |     |        |                       | 2          |               |       |     | Feb 2016 Volume | 2 Issue 1 |


|     |     | VPI(s             | ;a              | )=(Q(s   | ;a )H(cid:0)Q(s             |     | ;a )H)P(Q(s |     | ;a )H <Q(s  |      | ;a )H)+ |

|     |     |                   | t               | 1        | t 2                         |     | t 1         |     | t 1         | t    | 2       |
|     |     |                   |                 |          | H ;a1)H)2                   |     |             |     |             |      |         |
|     |     | (cid:27)(pst;at)e | (cid:0)(Q(st;a2 |          | ) (cid:0) Q ( s t           |     |             |     |             |      |         |
|     |     |                   |                 |          | 2 (cid:27) (s t; a ) 2      |     |             |     |             |      |         |
|     |     |                   | 2(cid:25)       |          | t                           |     |             |     |             |      |         |
|     |     |                   |                 |          | )H(cid:0)Q(s                |     | )H)P(Q(s    |     | )H          |      | )H)+    |
|     |     | VPI(s             | t ;a            | i )=(Q(s | t ;a i                      |     | t ;a 1      |     | t ;a i >Q(s | t ;a | 1       |
|     |     |                   | (cid:0)(Q(st;a1 |          | ) H (cid:0) Q ( s t ;ai)H)2 |     |             |     |             |      |         |
|     |     | (cid:27)(pst;at)e |                 |          | 2                           |     |             |     |             |      |         |
|     |     |                   |                 |          | 2 (cid:27) (s t; a t )      |     |             |     |             |      |         |
2(cid:25)
|     |     |     | i2fa |      | ;:::g      |     |     |     |     |     |     |

|     |     | FOR |      | 1 ;a | 2 ;:::;a i |     |     |     |     |     |     |
)(cid:21)(cid:28)R(cid:22)
|     |     |     | IF VPI(s | t       | ;a i |               |     |        |           |     |     |

|     |     |     | #        | Q-Value | from | Goal-directed |     | system | is evalu- |     |     |
ated
∑
|     |     |     | Q(s | ;a  | )=R^(s ;a | )+(cid:13) | p   | (fs;ag!s′)maxQ(s′;b)Goal(cid:0)directed |     |     |     |

|     |     |     |     | t   | i t       | i          | T   |                                         |     |     |     |
|     |     |     |     |     |           |            | s′  |                                         | b2A |     |     |
ELSE
|     |     |     | #            | Q-Value | from          | Habitual     | system |     | is retrieved |     |     |

|     |     |     | Q(s          | ;a      | )=Q(s         | ;a )Habitual |        |     |              |     |     |
|     |     |     |              | t       | i t           | i            |        |     |              |     |     |
|     |     | a   |  SoftMax(Q(s |         | ;a);(cid:12)) |              |        |     |              |     |     |
|     |     | t   |              |         | t             |              |        |     |              |     |     |
Update
|     |     | R(cid:22) | =(1(cid:0)(cid:27))R(cid:22)+(cid:27)r |     | # Reward |     | Rate |     |     |     |     |

t
|     |     | R^(s | ;a )=(1(cid:0)(cid:26))R^+(cid:26)r |     |                  | # Reward |       | function |                 |     |     |

|     |     |      | t t                                 |     |                  | t        |       |          |                 |     |     |
|     |     | p    | (s ;a ;s                            | )   | = (1 (cid:0) ϕ)p | (s       | ;a ;s | ) +      | ϕ # Probability |     | of  |
|     |     | T    | t t                                 | t+1 |                  | T        | t t   | t+1      |                 |     |     |
transition
|     |     | Specific          | to           | Kalman | Q-Learning      |     |     |     |     |     |     |

|     |     | #                 | Sigma-points |        | sampling        |     |     |     |     |     |     |
|     |     | (cid:2)=f(cid:18) | ;0(cid:21)j  |        | (cid:21)2jS:Ajg |     |     |     |     |     |     |
j
|     |     | W(cid:20) | =fw | ;0(cid:21)j | (cid:21)2jS:Ajg |     |     |     |     |     |     |

j
|     |     | R(cid:20) | =fr(cid:20) |     | )(cid:0)(cid:13)max(cid:18) |       |         | 0(cid:21)j | (cid:21)2jS:Ajg |     |     |

|     |     |           | =(cid:18)   | (s  | ;a                          |       | (s ;b); |            |                 |     |     |
|     |     |           | j           | j   | t t                         | b2A j | t+1     |            |                 |     |     |
2j∑S:Aj
|     |     | r predicted |     | =   | w j r(cid:20) j |     |     |     |     |     |     |

j=0
|     |     | #   | Covariance | computation |     |     |     |     |     |     |     |

2j∑S:Aj
|     |     |                       |     |     | (cid:0)QHabitual)(r(cid:20) |     | (cid:0)r |           |     |     |     |

|     |     | P (cid:18)jr(cid:20)j | =   | w   | j ((cid:18) j               |     | j        | predicted | )   |     |     |
t
j=0
2j∑S:Aj
|     |     | P          | =   | w (r(cid:20) | (cid:0)r    | )2+P |     |     |     |     |     |

|     |     | r(cid:20)j |     | j            | j predicted |      | n   |     |     |     |     |
j=0
(cid:0)1
|     |     | K   | =P                  | P          | # Kalman | gain |     |     |     |     |     |

|     |     | t   | (cid:18)jr(cid:20)j | r(cid:20)j |          |      |     |     |     |     |     |
(cid:0)r
|     |     | (cid:14)  | =r  |           | # Reward-prediction |     |     | error |     |     |     |

|     |     | t         | t   | predicted |                     |     |     |       |     |     |     |
|     |     | QHabitual |     | =QH       | +K (cid:14)         |     |     |       |     |     |     |
|     |     | t+1       |     | t         | t t                 |     |     |       |     |     |     |
(cid:0)K
|           |                     | PH  | =PH |     | P KT         |     |     |     |          |        |           |

|           |                     | t+1 |     | t   | t (cid:6)t t |     |     |     |          |        |           |
|           | j                   |     |     |     |              |     |     |     |          | j      | j         |
| ReScience | rescience.github.io |     |     |     | 3            |     |     |     | Feb 2016 | Volume | 2 Issue 1 |


Results
WeonlyreproducedtheresultsofFigure3A,B,G,Hinaqualitativemanner. Results
are presented in Figure 1. We can observe the strategy shift (from goal-directed to
habitual) after extensive training around 50 time steps. In the original article, the
|     |     | strategy | shift occurs | after | 100 | time steps. |     |     |     |     |

However we can observe a difference between the probabilities of action for the
|     |     | goal-directed | model. | In  | our implementation, |     |     |     |     |     |

;pl)≃0:7
p(s

and
;em)≃0:3
|     |     |        |              |     |              | p(s 0    |     |     |     |     |

|     |     | before | devaluation. | In  | the original | article, |     |     |     |     |
;pl)≃0:6
|     |     |     |     |     |     | p(s 0 |     |     |     |     |

and
|     |     |     |     |     |     | p(s ;em)≃0:4 |     |     |     |     |

Nevertheless, the probabilities of action from the Kalman Q-Learning after strategy
|     |     | shifting | are equivalent.                   |       |     |            |                                    |        |         |            |

|     |     |          | Moderate pre-devaluation training |       |     |            | Extensive pre-devaluation training |        |         |            |
|     |     |          | A                                 |       |     |            | B                                  |        |         |            |
|     |     |          | 0.10                              |       |     |            | 0.10                               |        |         |            |
|     |     |          |                                   |       |     | VPI(s0,pl) |                                    |        |         | VPI(s0,pl) |
|     |     |          |                                   |       |     | VPI(s0,em) |                                    |        |         | VPI(s0,em) |
|     |     |          | 0.08                              |       |     |            | 0.08                               |        |         |            |
|     |     |          |                                   |       |     | R*tau      |                                    |        |         | R*tau      |
|     |     |          | 0.06                              |       |     |            | 0.06                               |        |         |            |
|     |     |          | 0.04                              |       |     |            | 0.04                               |        |         |            |
|     |     |          | 0.02                              |       |     |            | 0.02                               |        |         |            |
|     |     |          | 0.00                              |       |     |            | 0.00                               |        |         |            |
|     |     |          | 0 20                              | 40    | 60  | 80 100     | 0                                  | 50 100 | 150 200 | 250 300    |
|     |     |          |                                   | Trial |     |            |                                    |        | Trial   |            |
|     |     |          | C                                 |       |     |            | D                                  |        |         |            |
|     |     |          |                                   |       |     | P(s0,pl)   |                                    |        |         | P(s0,pl)   |
|     |     |          | 0.8                               |       |     |            | 0.8                                |        |         |            |
|     |     |          |                                   |       |     | P(s0,em)   |                                    |        |         | P(s0,em)   |
|     |     |          | 0.7                               |       |     |            | 0.7                                |        |         |            |
|     |     |          | 0.6                               |       |     |            | 0.6                                |        |         |            |
|     |     |          | )a,s(P                            |       |     |            | )a,s(P                             |        |         |            |
|     |     |          | 0.5                               |       |     |            | 0.5                                |        |         |            |
|     |     |          | 0.4                               |       |     |            | 0.4                                |        |         |            |
|     |     |          | 0.3                               |       |     |            | 0.3                                |        |         |            |
|     |     |          | 0.2                               |       |     |            | 0.2                                |        |         |            |
|     |     |          | 0 20                              | 40    | 60  | 80 100     | 0                                  | 50 100 | 150 200 | 250 300    |
|     |     |          |                                   | Trial |     |            |                                    |        | Trial   |            |
Figure 1: A.ValueofPreciseInformation(fulllines)foractionpress-leverandentermagazinein
stateS andrewardrate(dashedline)inmoderatetraining. Verticallinerepresentsthetimingof

devaluation. B. In extensive training. C. Probability of actions in state S in moderate training.

|     |     | D.  | In extensive training. |     |     |     |     |     |     |     |

Conclusion
Wewereabletoqualitativelyreproducethefirstsimulationsofthearticle. Despitethe
small differences in the exact timing of the strategy shifting and in the probabilities
of action, the behavior of our implementation is similar to the original article. Thus,
|           |                     | we  | confirm the | correctness | of the | model presented | in  | the original | article. |           |

|           | j                   |     |             |             |        |                 |     |              | j        | j         |
| ReScience | rescience.github.io |     |             |             | 4      |                 |     | Feb 2016     | Volume   | 2 Issue 1 |


References
[1] Matthieu Geist, Olivier Pietquin, and Gabriel Fricout. “Kalman Temporal Differences: The
deterministiccase”.In:IEEESymposiumonAdaptiveDynamicProgrammingandReinforce-
ment Learning (2009), pp. 185–192.
[2] Mehdi Keramati, Amir Dezfouli, and Payam Piray. “Speed/accuracy trade-off between the
habitualandthegoal-directedprocesses”.In:PLoScomputationalbiology7.5(2011),e1002055.

---
**Source PDF:** `2016_07_article.pdf`
