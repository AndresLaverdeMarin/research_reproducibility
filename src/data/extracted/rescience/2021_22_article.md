R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Reproducibility study - Does enforcing diversity in
hidden states of LSTM-Attention models improve
transparency?

Pieter Bouwman1, ID , Yun Li1, ID , Rogier van der Weerd1, ID , and Frank Verhoef1, ID
1University of Amsterdam, Amsterdam, The Netherlands

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4835592

Reproducibility Summary

It has been shown [1] that the weights in attention mechanisms do not necessarily offer
a faithful explanation of the modelʼs predictions. In the paper Towards Transparent and
Explainable Attention Models Mohankumar et al.2 propose two methods to enhance faith-
fulness and plausibility of the explanations provided by an LSTM model combined with
a basic attention mechanism.

Scope of Reproducibility — For this reproducibility study, we focus on the main claims made
in this paper:

• The attention weights in standard LSTM attention models do not provide faith-
ful and plausible explanations for its predictions. This is potentially because the
conicity of the LSTM hidden vectors is high.

• Two methods can be applied to reduce conicity: Orthogonalization and Diversity
Driven Training. When applying these methods, the resulting attention weights
offer more faithful and plausible explanations of the modelʼs predictions, without
sacrificing model performance.

Methodology — The paper includes a link to a repository with the code used to generate
its results. We follow four investigative routes: (i) Replication: we rerun experiments
on datasets from the paper in order to replicate the results, and add the results that are
missing in the paper; (ii) Code review: we scrutinize the code to validate its correctness;
(iii) Evaluation methodology: we extend the set of evaluation metrics used in the paper
with the LIME method, in an attempt to resolve inconclusive results; (iv) Generalization
to other architectures: we test whether the authorsʼ claims apply to variations of the base
model (more complex forms of attention and a BiLSTM encoder).

Results — We confirm that the Orthogonal and Diversity LSTM achieve similar accura-
cies as the Vanilla LSTM, while lowering conicity. However, we cannot reproduce the
results of several of the experiments in the paper that underlie their claim of better trans-
parency. In addition, a close inspection of the code base reveals some potentially prob-
lematic inconsistencies. Despite this, under certain conditions, we do confirm that the


Code is available at https://github.com/MotherOfUnicorns/FACT_AI_project. – SWH swh:1:dir:19a8073757cc142f8f50eb44014aca87cad0b8bf.
Open peer review is available at https://openreview.net/forum?id=lE0wqKGROKa.




Orthogonal and Diversity LSTM can be useful methods to increase transparency. How
to formulate these conditions more generally remains unclear and deserves further re-
search. The single input sequence tasks appear to benefit most from the methods. For
these tasks, the attention mechanism does not play a critical role for achieving perfor-
mance.

What was easy/difﬁcult — The codebase of the authors is accessible and can be run easily,
with good facilities to prepare datasets and define configurations. The Orthogonaliza-
tion and Diversity Training methods are well explained in the paper and mostly cleanly
implemented. The larger datasets (Amazon and CNN) are difficult to run due to mem-
ory requirements and compute times. The codebase can be hard to navigate, a conse-
quence of the choice to accommodate a large variation of models and datasets in one
framework.

Communication with original authors — We reached out to the authors on a fundamental but
unexplained choice in the model architecture but unfortunately did not hear back be-
fore the deadline of our assignment.




## 1 Introduction

The popularity of attention models has sparked many studies on the interpretability of
the attention distributions, with often conflicting claims [1, 3, 4]. Mohankumar et al.2
argue that the reason why attention weights do not always provide a faithful explanation
of the modelʼs predictions is that the learned hidden states of the LSTM based encoder
are very similar across time steps, which is expressed by high conicity of these vectors.
As a result, random permutation of the attention weights leads to a similar final context
vector, which implies the weights do not provide a faithful explanation. The authors
propose two methods that force the hidden states of the LSTM to be more diverse. Or-
thogonal LSTM ensures low conicity by orthogonalizing the hidden state at time t with
respect to the mean of the previous hidden states. In Diversity LSTM the model is trained
to jointly maximize the log-likelihood of the training data and to minimize the conicity
of the hidden states.

## 2 Scope of reproducibility

In this reproducibility study we focus on the authorsʼ main claim that the 
and Orthogonal LSTM lead to more faithful and plausible explanations, while maintain-
ing accuracy of the predictions. The authors support their claim by evaluating a series
of metrics that are assumed to be indicative of levels of faithfulness and plausibility. We
follow four investigative routes:

• Replication: The main part of our study is focused on reproducing the results on
the metrics in Mohankumar et al.2, and to validate whether we can confirm their
observations and conclusions. Furthermore, as the original paper only presents
the results of a selection of models and datasets, we complement the results where
possible. Most notably, we add results on the Orthogonal LSTM that were not in
the original paper. Models, code and datasets are described in Section 3. Our
replication results are presented in Section 4;

• Code review: As the authorsʼ code1 is publicly available, we use their code for the
reproduction. In Section 5 we investigate whether the implementation is consis-
tent with the description of the algorithms in the paper;

• Evaluation methodology: In Section 6 we report on our attempt to resolve inconclu-
sive results we found on the attribution methods by extending the set of evaluation
metrics used in the paper with the LIME method;

• Generalization to other architectures: In Section 7 we test whether the authorsʼ
claims apply to variations of the base model (more complex forms of 
and a BiLSTM encoder).

We conclude this paper in Section 8 with a discussion on the conditions under which
the proposed methods are most likely to be effective, and a reflection on our replication
study.

## 3 Methodology

Code — The code accompanying the paper is an extension based on the code2 first devel-
oped by Jain and Wallace1. The entry point of the code is clear and well documented
and allows a user to define specific jobs using command line arguments for hyperpa-
rameters. Preprocessing routines for the most datasets are included.

1https://github.com/akashkm99/Interpretable-Attention
2https://github.com/successar/AttentionExplanation




Datasets — We reran the experiments on 11 of the 14 datasets used in the paper. The
nature and size of the datasets covers a wide range, from relatively simple binary sen-
timent classification tasks with single input sequence (abbreviated: SS) (e.g. SST with
average input sentence length of 20 words), to complex question answering tasks with
dual input sequences (abbreviated: DS)3 (e.g. CNN with average document size of 760
words and an average of 26 answer categories). Some illustrations of data points can
be found in Appendix D. The code repository includes links to the datasets, as well as
the pre-processing routines used by the authors. We excluded the Amenia and Diabetes
datasets because they were not accessible in time. The Amazon dataset caused mem-
ory issues when running the experiments. Despite these issues we were able to get the
accuracies and conicity values for this dataset.

Model descriptions — The baseline model (Vanilla LSTM) used in the paper is shown in
Figure 1. For DS tasks, it consists of two uni-directional LSTM encoders that act on a
P-path (for document input phrases) and a Q-path (for question input phrases). When
applied on SS tasks in the paper, only the P-path is used. An attention decoder is applied
to the hidden states of the P-path LSTM to form the context vector cα on which the model
calculates its output. The last hidden state of the Q-path is used as the query term for
DS tasks.
The Diversity and Orthogonal LSTM that Mohankumar et al.2 propose are variants of
the baseline model. The Orthogonal LSTM applies an orthogonalization procedure to
the LSTM hidden state vectors during training: the hidden state in timestep t is set to
the component that is orthogonal to the mean of previous hidden states. This enforces
low conicity of the hidden state vectors hp
t . The Diversity LSTM uses a standard LSTM
cell with no explicit orthogonalization, but minimizes conicity jointly with the standard
loss.

Figure 1. The LSTM+attention model as defined in the paper

Hyperparameters — Given the wide variety of tasks and datasets, there is an elaborate set
of model- and optimization hyperparameters. Not all parameter values are indicated in
the original paper, some were retrieved by inspecting the code (an overview is presented
in Appendix A). For all parameters, we used the defaults provided in the original code.
We do not engage in further hyperparameter optimization to stay close to the 
paperʼs approach. Note that we are interested in transparency and explainability of the
models, not their optimal performance.

3These distinctions are differently named in the code: SS is referred to as BC and DS as QA


𝑤(cid:2869)(cid:3043)=‘Jane’𝑒(𝑤(cid:2869)(cid:3043))𝐿𝑆𝑇𝑀(cid:3017)𝒉(cid:2868)(cid:3043)𝒉(cid:2869)(cid:3043)𝒉(cid:2870)(cid:3043)𝒉(cid:2871)(cid:3043)𝒉(cid:3040)(cid:3043)𝛼(cid:2869)𝛼(cid:2870)𝛼(cid:2871)𝛼(cid:2872)+𝒄(cid:3080)𝑓(𝒄(cid:3080))𝒚(cid:3549)(cid:3080)𝒄(cid:2868)(cid:3043)𝒄(cid:3040)(cid:3043)𝒉(cid:3047)(cid:3043)=𝐿𝑆𝑇𝑀(cid:3017)(𝒆𝑤(cid:3047)(cid:3043),𝒉(cid:3047)(cid:2879)(cid:2869)(cid:3043))∀𝑡∈[1,𝑚]𝒉(cid:3047)(cid:3044)=𝐿𝑆𝑇𝑀(cid:3018)(𝒆𝑤(cid:3047)(cid:3044),𝒉(cid:3047)(cid:2879)(cid:2869)(cid:3044))∀𝑡∈[1,𝑛]𝛼(cid:3556)(cid:3047)=𝒗(cid:3021)tanh𝑊(cid:2869)𝒉(cid:3047)(cid:3043)+𝑊(cid:2870)𝒉(cid:3041)(cid:3044)+𝒃∀𝑡∈[1,𝑚]𝛼(cid:3047)=𝑠𝑜𝑓𝑡𝑚𝑎𝑥 (𝛼(cid:3556)(cid:3047))𝒄(cid:3080)=(cid:3533)𝛼(cid:3047)𝒉(cid:3047)(cid:3043)(cid:3040)(cid:3047)(cid:2880)(cid:2869) 𝑤(cid:2870)(cid:3043)=‘went’𝑒(𝑤(cid:2870)(cid:3043))𝑤(cid:2871)(cid:3043)=‘to’𝑒(𝑤(cid:2871)(cid:3043))𝑤(cid:2872)(cid:3043)=‘London’𝑒(𝑤(cid:2872)(cid:3043))P-Path𝑤(cid:2869)(cid:3044)=‘Where’𝑒(𝑤(cid:2869)(cid:3044))𝒉(cid:2868)(cid:3044)𝒄(cid:2868)(cid:3044)𝒄(cid:3041)(cid:3044)𝑤(cid:2870)(cid:3044)=‘is’𝑒(𝑤(cid:2870)(cid:3044))𝑤(cid:2871)(cid:3044)=‘Jane’𝑒(𝑤(cid:2871)(cid:3044))𝒚(cid:3549)(cid:3080)=𝑠𝑜𝑓𝑡𝑚𝑎𝑥(𝑊(cid:2868)𝒄(cid:3080)) 𝐿𝑆𝑇𝑀(cid:3017)𝐿𝑆𝑇𝑀(cid:3017)𝐿𝑆𝑇𝑀(cid:3017)𝐿𝑆𝑇𝑀(cid:3018)𝐿𝑆𝑇𝑀(cid:3018)𝐿𝑆𝑇𝑀(cid:3018)Q-PathLearnableParameters𝑊(cid:2868)∈ℝ(cid:3038)×(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)Equations𝑊(cid:2869)∈ℝ(cid:3031)(cid:3117)×(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝑊(cid:2870)∈ℝ(cid:3031)(cid:3117)×(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝒃∈ℝ(cid:3031)(cid:3117)𝑊(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3043)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)×(cid:3031)(cid:3280)(cid:3288)(cid:3277)𝑈(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3043)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)×(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝒃(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3043)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝑊(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3044)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)×(cid:3031)(cid:3280)(cid:3288)(cid:3277)𝑈(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3044)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)×(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝒃(cid:3034)(cid:3028)(cid:3047)(cid:3032)(cid:3044)∈ℝ(cid:3031)(cid:3283)(cid:3284)(cid:3279)(cid:3279)(cid:3280)(cid:3289)𝒉(cid:3041)(cid:3044)𝒗∈ℝ(cid:3031)(cid:3117)‘Document’‘Question’Embeddings𝑊(cid:3032)∈ℝ(cid:3031)(cid:3297)(cid:3290)(cid:3278)×(cid:3031)(cid:3280)(cid:3288)(cid:3277)For allgates (f,i,o,c):

Experimental setup and computational requirements — We strictly follow the code environment
as dictated by the requirements file that accompanies the code. All our experiments
with this code are conducted on GPU nodes of the Lisa Cluster at SURFsara4. We had
access to two Nvdia GTX1080Ti GPUs (11Gb VRAM).
Train and evaluation times varied between datasets and model variations, from ca. 5
minutes (SST dataset) to more than 40 hours (CNN dataset). We ran multiple seeds only
on a selection of critical datasets to verify that differences we observed w.r.t. the results
in the original paper were significant. Due to resource constraints, all other compar-
isons are based on single seeding, as was done in the original paper. This means that
our observations are indicative, not conclusive.

## 4 Replication of the paper’s results

### 4.1 Core replication results

Our reproduction study reveals numerous differences in results reported by Mohanku-
mar et al.2, for all datasets where we ran the experiments. Despite the differences, we
support the observation that Diversity and Orthogonal LSTM reach similar accuracies
as Vanilla LSTM, and lower conicity values, with the same exception reported in the pa-
per (CNN). However, we find the claim that Diversity LSTM leads to more transparent
attention distributions is not consistently supported. For Orthogonal LSTM, some re-
sults were omitted in the original paper, and we find conflicting results about the effect
on faithfulness and plausibility. We present an overview of the comparisons by metric,
and the impact our findings have on the main claims of the authors.

Accuracy and conicity — Of all accuracy and conicity values reported by Mohankumar et
al.2, we are able to reproduce 86% within a 3%-point margin. Models and datasets that
produced the most notable differences are highlighted in Table 1. Despite the different
values, the observation that Diversity and Orthogonal LSTM reach similar accuracies as
Vanilla LSTM still holds, except for the CNN dataset. Also, we can confirm that conicity
values are much lower in Diversity and Orthogonal LSTM, except for CNN in the Diver-
sity LSTM. The largest difference in accuracy we observe for bAbI3, but the output files
reveal that the model was not done training after the default 200 epochs.

Importance of hidden representation — Mohankumar et al.2 analyse the importance of hid-
den representations using intermediate representation erasure [4] and also by examin-
ing the effect of permuting the attentions weights [1].
A visual comparison of the box plots about representation erasure in the paper with box
plots in our reruns shows similar results in 25 of the 30 boxes. Despite the fact that our
rerun shows lower medians for the box plots for the LSTM in IMDB and 20News dataset,
the observation still holds that Diversity LSTM and Orthogonal LSTM reach a quicker
decision flip for SS tasks. We concur with the authorsʼ observations on the paraphrase
detection (QQP) and Q&A task (bAbI1). In our rerun we see that the quick decision flip
that is shown in bAbI1 also occurs in bAbI2 and bAbI3. Mohankumar et al.2 do not report
on SNLI and CNN, where our rerun shows no improvement of the Diversity LSTM and
Orthogonal LSTM models over Vanilla LSTM.
The impact of permuting attention weights is difficult to compare with our results as
Mohankumar et al.2 only report a graphical representation (violin plots) of median out-
put difference. After visual comparison we judge that the overall results are similar for
IMDB, 20News and Yelp. We also evaluate the median output difference for datasets not
reported by Mohankumar et al.2. We observe that the results for SST and Tweets show a
similar ʻshift to the rightʼ as reported for other binary classification tasks. For DS tasks

4https://userinfo.surfsara.nl/systems/lisa/description





Accuracy%


81.79
89.49
95.60
93.55
87.02
78.23
78.74
99.10
40.10
47.70
63.07

rerun
80.3
89.3
94.5
90.8
83.3
77.3
78.4
100.0
54.4
21.1
59.5


79.95
88.54
95.40
91.03
87.04
76.96
78.40
100.00
40.20
50.90
### 58.19 Conicity

rerun
80.0
87.8
93.8
90.8
85.4
74.0
78.2
100.0
54.6
56.3
46.3


0.68
0.69
0.53
0.77
0.77
0.56
0.59
0.56
0.48
0.43
0.45

rerun
0.71
0.60
0.54
0.76
0.78
0.59
0.58
0.77
0.43
0.93
0.40


0.20
0.08
0.06
0.15
0.24
0.12
0.04
0.07
0.05
0.10
0.06

rerun
0.19
0.09
0.35
0.14
0.23
0.04
0.03
0.07
0.13
0.11
0.38


SST
IMDB
Yelp


SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN


SST
IMDB
Yelp


SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN


rerun

77.6
80.05
88.3
88.71
94.5
96.00
91.9
92.15
83.9
83.20
76.6
76.46
78.6
78.61
99.9
99.90
59.0
56.10
57.7
51.20
53.6
54.30


rerun

0.28
0.28
0.16
0.18
0.19
0.18
0.24
0.23
0.26
0.27
0.31
0.27
0.32
0.33
0.23
0.22
0.17
0.21
0.13
0.12
0.10
0.07

Table 1. Comparison of reported accuracy and conicity values (differences > 0.03 are highlighted).

we observe that Vanilla LSTM already has relatively high median output difference, and
the Diversity LSTM and Orthogonal LSTM provide less improvement.
We conclude that in our experiments, the Diversity and Orthogonal LSTM do result in
quicker decision flips and higher output difference for SS tasks, but not consistently for
the other tasks.

Comparison with rationales — Our rerun of rationale length and rationale attention shows
very different results as reported by Mohankumar et al.2, see Table 2. Although we can
confirm that Diversity LSTM results in shorter rationales, we cannot support the claim
that Diversity LSTM provides much higher attention to the rationale than Vanilla LSTM.
In our rerun this only holds for 20News.
The data for the Orthogonal LSTM, which were not reported by Mohankumar et al.2,
show much shorter rationale length, consistent with the paperʼs claim. However, impact
on the share of attention on the rationale is mixed: it is higher for Yelp and 20 News,
similar for IMDB and Tweets, but lower for SST.
For DS tasks, the rationale comparison is not implemented by the authors, we suspect
because of the high computational costs involved for calculating rationales in tasks with
multiple output categories.

Comparison with attribution methods — The rerun of the correlation metrics shows numer-
ous differences in both Pearson correlation and JS Divergence. After studying Pearson
correlation, we support the authorsʼ claim that compared with Vanilla LSTM, Diversity
LSTM produces attention weights that better correlate with gradients and integrated
gradients, although in our results the relative increase of correlation with gradients is
smaller: 13%5 instead of the 65% reported by Mohankumar et al.2. However, we do not
see the claimed reduction in JS Divergence. In fact, for all datasets the 
produces similar or even higher JS Divergence values than Vanilla LSTM, except JS Di-
vergence with Integrated Gradients for 20News, see Table 3. The Orthogonal LSTM, for
which no correlation data is reported in the paper, is in line with the Diversity LSTM in
this respect.

5This percentage represents the average of the increases over all datasets.




Rationale 


SST
IMBD
Yelp


0.348
0.472
0.438
0.627
0.284

rerun
0.74
0.97
0.43
0.62
0.82


0.624
0.761
0.574
0.884
0.764

rerun
0.55
0.91
0.27
0.94
0.59

Rationale length


SST
IMBD
Yelp


0.240
0.217
0.173
0.215
0.225

rerun
0.72
0.92
0.38
0.59
0.81


0.175
0.169
0.160
0.173
0.306

rerun
0.18
0.22
0.19
0.27
0.32

Orthogonal
LSTM


-
-
-
-
-

rerun
0.35
0.92
0.55
0.86
0.79

Orthogonal
LSTM


-
-
-
-
-

rerun
0.10
0.27
0.11
0.24
0.39

Table 2. Comparison of reported rationales (differences > 0.05 are highlighted)

JS Divergence Gradients


0.10
0.09
0.15
0.15
0.08
0.11
0.15
0.33
0.53
0.46
0.22

rerun
0.09
0.08
0.12
0.18
0.07
0.11
0.10
0.12
0.39
0.26
0.16


0.08
0.09
0.13
0.06
0.12
0.10
0.10
0.21
0.23
0.37
0.17

rerun
0.09
0.11
0.17
0.17
0.09
0.11
0.11
0.23
0.40
0.36
0.34

JS Divergence Integrated Gradients


0.12
0.13
0.19
0.21
0.08
0.16
0.19
0.43
0.58
0.64
0.30

rerun
0.10
0.11
0.18
0.22
0.08
0.14
0.15
0.25
0.51
0.35
0.23


0.09
0.13
0.19
0.07
0.15
0.13
0.15
0.24
0.19
0.41
0.21

rerun
0.10
0.15
0.19
0.13
0.10
0.14
0.14
0.22
0.58
0.64
0.51


rerun

0.14
-
0.13
-
0.16
-
0.17
-
0.18
-
0.12
-
0.12
-
0.21
-
0.38
-
0.43
-
0.39
-


rerun

0.15
-
0.18
-
0.17
-
0.15
-
0.19
-
0.15
-
0.14
-
0.28
-
0.54
-
0.64
-
0.44
-

SST
IMDB
Yelp


SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN


SST
IMDB
Yelp


SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN

Table 3. Comparison of correlation metrics. Differences > 0.03 are highlighted

Analysis by POS tags — A comparison of the importance that is attributed to various POS
tags shows similar importance and ranking for the SST, 20News and Tweets datasets.
For Yelp and QQP we get different outcomes. Most notably, with vanilla LSTM model for
Yelp we see no attention given to punctuations (PUNC), for which Mohankumar et al.2
reports highest attention. For QQP, Mohankumar et al.2 reports 23% on PUNC, while we
find only 9%. Our results indicate the improvements shown in POS tags are less clear
than reported by Mohankumar et al.2.

Human evaluation — We could not reproduce the human evaluation within the four-week
time frame of our research. Mohankumar et al.2 reports convincing results, and we also
believe human interpretation should play a key role in judging whether their methods
improve transparency. We include some examples in Appendix D for this purpose.

### 4.2 Conclusion regarding reproducibility

Our findings are summarized in Table 4. We conclude that it is not immediately clear
that Diversity LSTM and Orthogonal LSTM provide better transparency for all the stud-




ied datasets.

Metric

Accuracy and conicity

Fraction of hidden rep-
resentation
required
for decision flip (box
plots)
dif-
Median Output
ference on randomly
permuting

weights (violin charts)
Rationale 

Rationale length

correlation
Pearson
divergence
and
JS
between
distribu-
tion of attention and
(integrated) gradients
Attention given to POS
tags

Human evaluation of
plausibility

Claim (with reference to paragraph number in Mo-
hankumar et al.2)
Diversity LSTM and Orthogonal LSTM achieve sim-
ilar accuracies as Vanilla LSTM, but much lower
conicity (§5.2)
Diversity LSTM and Orthogonal LSTM reach
quicker decision flip (§5.3)

Supported af-
ter rerun

Notes

Yes

Except CNN in Diver-
sity LSTM

Yes (for mod-
els in paper)

Especially for BC tasks,
somewhat for QQP; not
for SNLI and QA tasks

Diversity LSTM and Orthogonal LSTM are more
sensitive to random permutation of weights than
Vanilla LSTM (§5.3)

Yes (for mod-
els in paper)

Diversity LSTM provides much higher attention to
rationales than Vanilla LSTM across the 8 Text clas-
sification datasets (§5.4)
Diversity LSTM often provides shorter rationales
than Vanilla LSTM (§5.4)
Attention weights in Diversity LSTM better agree
with gradients and integrated gradients than
Vanilla LSTM (§5.5)

Attention given to punctuation marks is signifi-
cantly reduced on the Yelp, Amazon and QQP
datasets (§5.6)
Diversity LSTM gives much more attention to adjec-
tives than Vanilla LSTM in the four sentiment anal-
ysis tasks (SST, IMDB, Yelp, Amazon) (§5.6)
Human evaluators prefer attention distribution of
Diversity LSTM over Vanilla LSTM for Yelp, SNLI,
QQP and bAbI1 (§5.7)

No

Yes

Mixed

No

Yes

Clear difference for BC
tasks, mixed picture
for the dual-sequence
tasks.
Only true for 20News;
No results reported on
QA tasks
No results reported on
QA tasks
Diversity LSTM has
higher Pearson corre-
lation, but similar or
higher JS Divergence

Not for Yelp, less clear
for QQP

True for SST and IMDB,
but not for Yelp

Not
duced

repro-

Evaluation by only 15
people

Table 4. Evidence for authorsʼ claims after rerun

• The Orthogonal LSTM clearly leads to lower conicity than Vanilla LSTM, but Mo-
hankumar et al.2 show little evidence with other metrics that indicate higher faith-
fulness: of the 14 datasets, only 6 boxplots and 4 violin charts are included. The
results observed in our rerun are mixed. For example, Orthogonal LSTM works
well for 20News, but for SNLI there is hardly any effect on the box plot, and also
correlation/JSD with (integrated) gradients is worse.

• For Diversity LSTM, Mohankumar et al.2 show convincing evidence with substan-
tial data. We observe similar trends in conicity, and the impact of diversity train-
ing is clear in the box plots and violin charts for the binary classification tasks.
However, for the tasks that require two input sequences like SNLI, bAbI2, CNN our
rerun shows that Diversity LSTM does not contribute much to faithfulness and can
lead to lower correlation with (integrated) gradients and higher JS Divergence.

## 5 Code Review

As part of the reproduction study, we familiarized ourselves with the code to understand
how the model and the experiments had been implemented. We also scrutinized the
code to check whether we could find a cause for the differences we found in the reported
metrics. The codeʼs class architecture can accommodate a wide range of tasks, datasets
and model configurations. While convenient, this also makes the codebase complex
and susceptible to errors. The code review revealed several debatable choices, of which
the main ones are described below.

Orthogonalization of Q-path in dual input sequence tasks — For DS tasks, we expect the orthogo-
nalization procedure to only be activated in the P-path (the path of the input document)




of the model, as this is the path on which the attention mechanism applies its weights
αt. However, in the code, orthogonalization is also applied to the Q-path (the path of
the question phrase in the Q&A tasks, or the second input phrase in SNLI and QQP).
In our view, this introduces a potentially problematic effect. The attention mechanism
uses only the last hidden state vector hq
t as the query term. This representation for the
last word in the sequence will only retain the vector component orthogonal to the mean
of the previous word representations, as a result of orthogonalization. We argue that the
direction of hq
t in the hidden space will represent the exclusive ʻchange of meaningʼ that
the last word adds to the sequence. This is not a problem in the bAbI tasks, where the
prompt word in the question phrase is always the last word (e.g., ʻWhere is Janeʼ). But
for longer questions where the prompt words appear earlier in the question, this may
impede the attention mechanism from finding the right prompt words.
In order to test this sensitivity, we conduct an experiment for the simpler SS tasks. We
apply orthogonalization during training and compare model performance when i) atten-
tion weights are left unconstrained vs. ii) all attention weights are set to zero, except for
the last hidden state. The result is shown in Table 5.


SST: accuracy

IMDB: accuracy

20News: accuracy

Tweets: accuracy


Base

0.803
(0.713)
0.893
(0.602)
0.908
(0.761)
0.833
(0.776)

last_only

0.810
(0.763)
0.876
(0.885)
0.857
(0.831)
0.782
(0.798)


Base

0.776
(0.283)
0.883
(0.163)
0.919
(0.235)
0.839
(0.260)

last_only

0.583
(0.265)
0.784
(.141)
0.583
(0.395)
0.712
(0.330)

Table 5. Demonstration of adverse effect of orthogonalization on the information content of the
last hidden state vector (results reflect our experiments, not the original paper)

What is striking is the performance remains on par (marked in green) for 
when only attending to the last hidden state, indicating the model performs well with-
out the attention mechanism. However, we observe a performance drop of 10%-34%
(absolute) when attention is constrained for the Orthogonal LSTM (marked in red). In-
deed, it appears part of the information required for inference is lost. How this effect
impacts the results requires further study. It may explain the accuracy drop from 63%
(Vanilla LSTM) to 58%/54%(Diversity/Orthogonal LSTM) for CNN as reported in Table 2
by Mohankumar et al.2. We have contacted the authors to verify their intentions, but
did not receive a response prior to submission of this reproduction study.

Disparate calculation of ﬁnal prediction — For DS tasks, in the code the final prediction layer is
implemented as ˆy = softmax(Wr(tanh(Wpcα+bp+Wqhq
n+bq))+br). This deviates from
the prediction function ˆy = softmax(W0cα) described in Section 2.1 by Mohankumar et
al.26. However, this does not affect the core architecture, namely LSTM and attention,
so we did not modify the code or conduct further experiments.

Fine-tuning of embeddings — The models use pre-trained embeddings except for the bAbI
datasets. Words outside of the pre-trained embeddingsʼ vocabulary are initialized with
zero-vectors. All embeddings are fine-tuned (i.e. trainable), independently for the P-
and Q-paths for DS tasks. This is not mentioned in the original paper and this choice is
questionable as it leads to an excessive number of trainable parameters (e.g., >40M for
the CNN dataset, see Appendix A) and training time, while it is unlikely to be critical for
the tasks.

6https://github.com/akashkm99/Interpretable-Attention/blob/master/model/modules/Decoder.py#L101-L107




Deﬁnition of dev set for bAbI datasets — While pre-processing bAbI datasets, 15% of the train
set is randomly selected to be used as dev set, resulting in much higher similarity be-
tween these two splits compared to the test set. As a result, the trained model is overfit
on the train set, and we observe a large gap between dev and test accuracy.

## 6 Extension of the evaluation methods

As discussed in Section 4.1.4, our rerun of Pearsonʼs correlation and JS Divergence be-
tween attention weights and gradients/integrated gradients points towards a less con-
vincing conclusion. We therefore also used the LIME framework [5] as a third metric for
comparing how transparent the attention weights are as explanations, as well as how
much improvements are brought about by the Diversity and Orthogonal LSTM.

Pearsonʼs Correlation

Ortho.
0.33
0.70
0.38
0.22
0.67

Vanilla
0.42
0.30
0.13
0.24
0.69


IMDB


SNLI
bAbI1
Numbers that agree with expectations (higher correlation, lower JS
Divergence) are highlighted in green, numbers opposite to expectations
are highlighted in red.

Vanilla
0.26
0.22
0.07
0.15
0.42

Div.
0.42
0.45
0.18
0.12
0.46

Div.
0.42
0.71
0.43
0.23
0.58

JS Divergence
Ortho.
0.44
0.42
0.33
0.15
0.38

Table 6. Correlation and JS Divergence between attention weights and LIME scores

We use LIME to generate a score for the predicted class on each word-position in the
sentence, which can then be compared with the attention weights. For calculating JS
divergence we also rescaled the lime score so that the scores range from 0 to 1, and
sums to 1 per sentence (i.e. similar to attention scores). The results are shown in Table
6, where we experimented with only a representative selection of datasets due to time
and resource constraints.
Similar to our comparison of attention weights with gradient-based methods, Table 6
indicates Diversity and Orthogonal LSTM fail to produce explanations consistent with
LIME. It is also not clear which statistical measure is best for comparing whether two ex-
planation methods agree with each other. In several instances (e.g. 20News and Tweets),
we observe an increase in Pearsonʼs correlation and an increase in JS Divergence at the
same time when going from Vanilla LSTM to Orthogonal/Diversity LSTM models.

## 7 Generalization to other model architectures

Despite the differences we found between our observations and the observations re-
ported by [2], we still see the potential value of the methods they propose. This is be-
cause we did observe sparser attention weights when using Diversity and Orthogonal
LSTM, and because of the strong preference expressed for the Diversity LSTM in the
human evaluations conducted by Mohankumar et al.2.
We therefore investigate how well these methods work in alternative settings. So far
the Orthogonalization and Diversity Training methods are only tested on one-layer uni-
directional LSTM models with attention. However, in many recent studies, BiLSTM-
based attention models or Transformer models are used [6, 7, 8]. Similarly, more com-
plex attention mechanisms such as self-attention and multi-head attention [9] gained
popularity due to their superior performance. For this reason, we investigate whether
the proposed methods can be extended to more complex models and whether the au-
thorsʼ two main claims still apply.




Extending to other attention mechanisms — The application of more advanced attention mech-
anisms (such as multi-head attention) poses a challenge because they produce more
than one attention weight per word. It is not straightforward to generate explanations
and word importance based on these weights. As a consequence, several of the evalu-
ation metrics used by the authors cannot be applied in their current form. This would
require making non-trivial design choices on how to combine multiple distributions of
the attention weights. Further research is required to investigate this and whether exist-
ing methods such as Attention Flow and Attention Rollout [10] can provide a resolution.

Extending to other architectures: BiLSTM Experiments — We replace the uni-directional LSTM
in the model (Figure 1) with a bi-directional LSTM. We choose the BiLSTM architecture,
and not a Transformer based architecture, as the latter requires dealing with the more
advanced attention mechanisms discussed above.
In order to maintain the decoderʼs complexity (the attention mechanism), we preserve
the output dimension of the LSTM. This requires halving the dimension of the hidden
states, which also ensures that the number of trainable weights of the BiLSTM is com-
parable to that of the unidirectional LSTM. For the Diversity BiLSTM, the same diver-
sity weights are used as in Mohankumar et al.2. The conicity term present in the loss
function of the Diversity BiLSTM is calculated based on the concatenated forward and
backward hidden representations. Orthogonalization for the Ortho BiLSTM is applied
before concatenation of the forward and backward hidden states.
Results show that the application of the two methods proposed by Mohankumar et al.2
do not result in performance loss and do lower conicity. However, on other metrics and
across datasets, the picture is mixed like we saw in our reproducibility results for the
unidirectional LSTM, indicating the methods do not unconditionally improve explana-
tions. We will not discuss these results in detail, but conclude that it is indeed possible
to extend the proposed methods to BiLSTM attention models. Full results are included
in Appendix C for completeness.

## 8 Discussion

Our reproduction shows that enforcing low conicity between the hidden states of an
LSTM encoder does not guarantee improved transparency in the studied datasets, at
least not on the metrics used by Mohankumar et al.2. We find the authorsʼ claim about
improved transparency not generally applicable and under certain conditions their meth-
ods even hurt accuracy. Still, the Diversity LSTM and Orthogonal LSTM do lead to im-
proved metrics on some datasets, and the human evaluation Mohankumar et al.2 con-
ducted shows strong preference for the Diversity LSTM over Vanilla LSTM. This raises
the question under what conditions these methods should be applied.

Conditions underlying effectiveness — One pattern that seems to emerge is that the benefits
of orthogonalizing or diversity training are most apparent for the relatively simpler SS
tasks. The potential to improve faithfulness of the weights might be high in those cases
as it not a given that attention weights carry any meaning for these tasks.
For some tasks, the LSTM does not strictly need the attention mechanism to perform
well, as is shown in Table 7 when the attention mechanism is constrained to be either
uniform or attending to the last word only. In contrast, the more difficult DS tasks do
require the attention mechanism in order to reach higher accuracies. This pattern is
similar to that described by Wiegreffe and Pinter3.
We suspect that there is a relation between a) how crucial the attention mechanism is for
performance in a given task, b) how much improvement Orthogonal/Diversity LSTM can
offer w.r.t. plausibility of the attention weights for explaining the modelʼs outputs. This





SST
IMDB
Yelp


SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN
∗

Base 

Reported
.818 .895
.956 .936
.870 .782
.787 .991
.401 .477
.631 Repr.
.803 .893
.949 .908
.833 .773
.784 1.00
.544 ∗
.211 .595

Constrained 
last_only
uniform
.810 .800
.876 .883
.949 .950
.857 .898
.782 .833
.759 .755
.792 .789
.729 .485
.441 .315
-
-
.367 .424

Reproduction failed, comparisons not applicable

Table 7. Impact on performance of the Vanilla LSTM when forcing uniform, first- and last only


relationship, and the conditions under which orthogonalization and diversity training
offer the best results, deserves additional investigation.

Reflection on our replication study — A key insight we have gained is that even with access
to the original code, exact reproduction of the results is not guaranteed. We have not
been able to find the cause of several differences in results. The available time and
hardware limited our possibilities to repeat these experiments with multiple seeds to
find an estimate of the variance of outcomes.
Another insight we gained is that the metrics concerning faithfulness and plausibility
can be hard to interpret, as it is deeply entangled with the nature of the dataset as well as
the model implementation. To enable scalable development of transparent AI models,
reliable quantitative metrics are needed that can accurately approximate real humansʼ
judgement. We believe further development of transparency metrics is an important
area for further research to help build more transparent models.

Acknowledgement

Weʼd like to thank Stefan Schouten for his guidance and insightful discussions.

References

3.

2.

1.

S. Jain and B. C. Wallace. “Attention is not Explanation.” In: Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies, Vol-
ume 1 (Long and Short Papers). Minneapolis, Minnesota: Association for Computational Linguistics, June
2019, pp. 3543–3556. DOI: 10.18653/v1/N19-1357. URL: https://www.aclweb.org/anthology/N19-1357.
A. K. Mohankumar, P. Nema, S. Narasimhan, M. M. Khapra, B. V. Srinivasan, and B. Ravindran. “Towards Trans-
parent and Explainable Attention Models.” In: Proceedings of the 58th Annual Meeting of the Association
for Computational Linguistics. Online: Association for Computational Linguistics, July 2020, pp. 4206–4216.
DOI: 10.18653/v1/2020.acl-main.387. URL: https://www.aclweb.org/anthology/2020.acl-main.387.
S. Wiegreffe and Y. Pinter. “Attention is not not Explanation.” In: Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP). Hong Kong, China: Association for Computational Linguistics, Nov.
2019, pp. 11–20. DOI: 10.18653/v1/D19-1002. URL: https://www.aclweb.org/anthology/D19-1002.
S. Serrano and N. A. Smith. “Is Attention Interpretable?” In: Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics. Florence, Italy: Association for Computational Linguistics, July
2019, pp. 2931–2951. DOI: 10.18653/v1/P19-1282. URL: https://www.aclweb.org/anthology/P19-1282.
5. M. T. Ribeiro, S. Singh, and C. Guestrin. “” Why should I trust you?” Explaining the predictions of any classiﬁer.” In:
Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining.
2016, pp. 1135–1144.

4.




8.

7.

6. Q. Zhou and H. Wu. “NLP at IEST 2018: BiLSTM-attention and LSTM-attention via soft voting in emotion clas-
siﬁcation.” In: Proceedings of the 9th Workshop on Computational Approaches to Subjectivity, Sentiment
and Social Media Analysis. 2018, pp. 189–194.
L.-H. Lee, Y. Lu, P.-H. Chen, P.-L. Lee, and K.-K. Shyu. “NCUEE at MEDIQA 2019: medical text inference using
ensemble BERT-BiLSTM-Attention model.” In: Proceedings of the 18th BioNLP Workshop and Shared Task.
2019, pp. 528–532.
A. Aziz Sharfuddin, M. Naﬁs Tihami, and M. Saiful Islam. “A Deep Recurrent Neural Network with BiLSTM model
for Sentiment Classiﬁcation.” In: 2018 International Conference on Bangla Speech and Language Processing
(ICBSLP). 2018, pp. 1–4. DOI: 10.1109/ICBSLP.2018.8554396.
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin. “Attention
is all you need.” In: Proceedings of the 31st International Conference on Neural Information Processing
Systems. NIPS’17. Red Hook, NY, USA: Curran Associates Inc., Dec. 2017, pp. 6000–6010.
S. Abnar and W. Zuidema. “Quantifying Attention Flow in Transformers.” In: Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics. Online: Association for Computational Linguistics,
July 2020, pp. 4190–4197. DOI: 10.18653/v1/2020.acl-main.385. URL: https://www.aclweb.org/anthology/
2020.acl-main.385.

9.

10.




Appendix A: Details of models and datasets

Table 8. Model- and hyperparameters for standard configurations per dataset


Description

train (%pos)

dev (%pos)

test (%pos)

Document

Question

Number of datapoints

Avg seq. length (train)

Avg.no.answer
categories

Vocab. size
(train, docs)

Single input sequence tasks

SST
IMDB
Yelp
Amazon
Anemia
Diabetes


∗
∗
∗


Diagnosis prediction
Diagnosis prediction
Topic classification
Topic classification

Dual input sequence tasks

6,355 (52%)
17,200 (50%)
345,285 (54%)
1,528,080 (52%)
-
-
1,145 (50%)
13,938 (12%)

821 (52%)
4,297 (49%)
4,790 (54%)
4,456 (52%)
-
-
278 (50%)
2,447 (13%)

1,725 (50%)
4,356 (50%)
26,866 (54%)
331,774 (52%)
-
-
357 (50%)
4,123 (12%)

SNLI
QQP
bAbI1
bAbI2
bAbI3
CNN

Natural language inference
Paraphrase detection


549,367
327,460 (37%)
8,500
8,500
8,500
380,298

9,842
36,384 (37%)
1,500
1,500
1,500
3,924

9,824
40,430 (37%)
1,000
1,000
1,000
3,198


-
-


n/a
n/a
n/a
n/a
-
-
n/a
n/a


-
-


26.1

13,703
12,486
63,304
49,881
-
-
5,904
6,841

17,943
26,172


>70,000

∗

Replication could not be performed for these datasets due to either availability or memory size limits

Table 9. Characteristics of the datasets


SSTIMDBYelpAmazon20NewsTweetsSNLIQQPBabi1Babi2Babi3CNNModel configurationModel LSTM variationVanillaVanillaVanillaVanillaVanillaVanillaVanillaVanillaVanillaVanillaVanillaVanillaAttention typetanhtanhtanhtanhtanhtanhtanhtanhtanhtanhtanhtanhEmbedding dim300300300300300300300300505050300Embedding voc13.82612.48763.32849.8836.5156.84520.98126.63524383970.190Pre-embedFastTextFastTextFastTextFastTextFastTextFastTextGLOVEGLOVENoneNoneNoneFastTextLSTM hidden dim25625625625625625625625664128128256Output size1111113236 (6)*36 (6)*36 (6)*584 (26)*Optimizer hyperparametersDiversity weight (if applicable)0.50.50.50.50.50.50.10.50.50.50.50.2Batch size32323232323212812832646490OptimizerAdamAdamAdamAdamAdamAdamAdamAdamAdamAdamAdamAdamLR0.0010.0010.0010.0010.0010.0010.0010.0010.0010.0010.0010.001Weight decay1,E-051,E-051,E-051,E-051,E-051,E-051,E-051,E-051,E-051,E-051,E-051,E-05Epochs888888252510020020012Trainable weights, including fine-tuning of embeddingsPencoder4.719.1924.317.49219.569.79215.536.2922.525.8922.624.8926.865.6928.480.89230.89694.06094.11021.628.392Qencoder0000006.865.6928.480.89230.89694.06094.11021.628.392Decoder33.28133.28133.28133.28133.28133.281132.099131.9709.54035.42835.428207.048Total4.752.4734.350.77319.603.07315.569.5732.559.1732.658.17313.863.48317.093.75471.332223.548223.64843.463.832Trainable weights, without fine-tuning of embeddingsPencoder571.392571.392571.392571.392571.392571.392571.392571.392n/an/an/a571.392Qencoder000000571.392571.392n/an/an/a571.392Decoder33.28133.28133.28133.28133.28133.281132.099131.970n/an/an/a207.048Total604.673604.673604.673604.673604.673604.6731.274.8831.274.754n/an/an/a1.349.832                  * Output size is numer of total entities in the dataset, part of which is masked in each datapoint (numer of categories used on average per data point)Single input sequence tasksDual input sequence tasks

Appendix B: Full replication results

Figure 2. Replication results for single sequence tasks


Color coding:datasetdatasetdatasetdatasetdatasetdatasetRelative difference between test runs and original experimentSSTimdbYelpAmazon20NewsTweetsMODELPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNIndicatorSource of inforel%AVGrel%AVGrel%AVGrel%AVGrel%AVGrel%AVGTABLE 2vanilla lstmtest accuracy best modelevaluate.json0,818-2%0,8030,8950%0,8930,956-1%0,9490,9370%0,9370,936-3%0,9080,870-4%0,833Benchmark dataconicity_meanevaluate.json0,6805%0,7130,690-13%0,6020,5301%0,5360,500-9%0,4570,770-1%0,7610,7701%0,776conicity_stdevaluate.jsonn/avail-0,173n/avail-0,135n/avail-0,121n/avail-0,084n/avail-0,189-0,159ortho lstmtest accuracy best modelevaluate.json0,801-3%0,7760,8870%0,8830,960-2%0,9450,9301%0,9360,9220%0,9190,8321%0,839conicity_meanevaluate.json0,2801%0,2830,180-9%0,1630,1803%0,1860,1607%0,1710,2302%0,2350,270-4%0,260conicity_stdevaluate.jsonn/avail-0,058n/avail-0,041n/avail-0,044n/avail-0,032n/avail-0,068-0,062diversity lstmtest accuracy best modelevaluate.json0,8000%0,8000,885-1%0,8780,954-2%0,9380,9290%0,9320,9100%0,9080,870-2%0,854conicity_meanevaluate.json0,200-6%0,1880,08011%0,0890,060478%0,3470,050-2%0,0490,150-10%0,1350,240-4%0,231conicity_stdevaluate.jsonn/avail-0,050n/avail-0,021n/avail-0,014n/avail-0,024n/avail-0,046-0,067FIGURE 3IndicatorSource of info-Fraction of hidden representationsvanilla lstm - ATTNmedianimportance_ranking_MAvDY_all.png -0,8200,75-27%0,5500,90-6%0,850,90--0,60-38%0,3701,000Box plots1st quartileimportance_ranking_MAvDY_all.png -0,4800,18-33%0,1200,90-6%0,850,65--0,60-38%0,3701,000visual inspection paper3rd quartileimportance_ranking_MAvDY_all.png -1,0001,000%1,0001,000%1,001,00--1,000%1,0001,000RANDOMmedianimportance_ranking_MAvDY_all.png -0,8500,98-1%0,9700,93-3%0,901,00--0,935%0,9800,9301st quartileimportance_ranking_MAvDY_all.png -0,8500,88-6%0,8300,93-3%0,900,93--0,935%0,9800,9303rd quartileimportance_ranking_MAvDY_all.png -1,0001,000%1,0001,000%1,001,00-1,000%1,0001,000-orth lstm - ATTNmedianimportance_ranking_MAvDY_all.png -0,2200,05-20%0,0400,25-28%0,1800,30--0,15-20%0,1200,5301st quartileimportance_ranking_MAvDY_all.png -0,1000,020%0,0200,13-8%0,1200,20--0,07-43%0,0400,1903rd quartileimportance_ranking_MAvDY_all.png -0,3500,12-17%0,1000,33-18%0,2700,40--0,2245%0,3200,750RANDOMmedianimportance_ranking_MAvDY_all.png -0,7800,92-5%0,8700,93-1%0,9200,90--0,93-1%0,9200,9301st quartileimportance_ranking_MAvDY_all.png -0,5700,73-15%0,6200,83-10%0,7500,80--0,80-8%0,7400,7503rd quartileimportance_ranking_MAvDY_all.png -1,0000,98-1%0,9701,00-2%0,9800,97-0,99-1%0,9801,000-diversity lstm - ATTNmedianimportance_ranking_MAvDY_all.png -0,1800,07-29%0,0500,13246%0,4500,17--0,10-20%0,0800,3701st quartileimportance_ranking_MAvDY_all.png -0,0800,020%0,0200,08125%0,1800,10--0,04-25%0,0300,2003rd quartileimportance_ranking_MAvDY_all.png -0,3900,14-29%0,1000,18383%0,8700,25--0,2313%0,2600,530RANDOMmedianimportance_ranking_MAvDY_all.png -0,7700,880%0,8800,906%0,9500,90--0,93-3%0,9000,8801st quartileimportance_ranking_MAvDY_all.png -0,5000,625%0,6500,7312%0,8200,70--0,75-1%0,7400,6803rd quartileimportance_ranking_MAvDY_all.png -1,0000,98-1%0,9700,955%1,0001,00-1,00-3%0,9701,000FIGURE 4IndicatorSource of info-Comparisonvanilla lstm - [0.00-0.25]medianPermutation.png -0,0500,1613%0,1800,0367%0,050,05--0,05-60%0,020-0,030Violin plots[0.25-0.50]medianPermutation.png -0,0800,1718%0,2000,0540%0,070,07--0,15-47%0,080-0,050visual inspection paper[0.50-0.75]medianPermutation.png -0,230n/appl--0,20-25%0,150,15--0,23---0,100[0.75-1.00]medianPermutation.png --n/appl--n/appl--0,15-0,28-----ortho lstm - [0.00-0.25]medianPermutation.png -0,1200,427%0,4500,3716%0,4300,37--0,49-12%0,430-0,180[0.25-0.50]medianPermutation.png -0,2300,4312%0,4800,3321%0,4000,33--0,49-6%0,460-0,200[0.50-0.75]medianPermutation.png -0,3300,4321%0,5200,35-6%0,3300,40--0,48-10%0,430-0,250[0.75-1.00]medianPermutation.png -0,3600,3754%0,5700,47-36%0,300n/appl-0,50-6%0,470-0,300-diversity lstm - [0.00-0.25]medianPermutation.png -0,1000,3910%0,4300,43-30%0,300,3--0,462%0,470-0,200[0.25-0.50]medianPermutation.png -0,2300,447%0,4700,47-38%0,290,4--0,48-2%0,470-0,250[0.50-0.75]medianPermutation.png -0,3500,486%0,5100,53-45%0,290,5--0,464%0,480-0,300[0.75-1.00]medianPermutation.png -0,420n/appl--0,55-27%0,40n/appl-0,49-4%0,470-0,350TABLE 3IndicatorSource of info-Mean attention given to rationalesvanilla lstmRationale attentionrationale_summary_test.txt0,348113%0,7420,472105%0,9680,44-2%0,4300,35--0,63-2%0,6170,28189%0,820Rationale lengthrationale_summary_test.txt0,240200%0,7190,217324%0,9200,17120%0,3800,16-0,22173%0,5880,23260%0,809-ortho lstmRationale attentionrationale_summary_test.txt -0,354-0,921-0,535--0,860-Rationale lengthrationale_summary_test.txt -0,102-0,269-0,114-0,240--diversity lstmRationale attentionrationale_summary_test.txt0,624-12%0,5500,7620%0,9120,57-54%0,2660,40--0,886%0,9400,76-23%0,591Rationale lengthrationale_summary_test.txt0,1753%0,1800,1733%0,2240,1619%0,1910,24-0,1753%0,2650,314%0,319TABLE 4IndicatorSource of info-Comparison to gradient methodsvanilla lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv0,71-13%0,6190,808%0,8630,5525%0,6900,43-0,72-29%0,5130,65-7%0,605CorrelatonsStd Pearson corrAttn_Gradient_X_val_pearsonr.csv0,210,070,160,19-0,280,24We use std.dev in paper to judge replication scores (colors)Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,62-19%0,5030,6817%0,7930,4015%0,4580,43-0,65-40%0,3900,56-14%0,483Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,240,090,190,19-0,320,25Overall mean JS divAttn_Gradient_X_val_jsd.csv0,10-10%0,0900,09-11%0,0800,15-19%0,1210,17-0,1521%0,1820,08-6%0,075Std JS divAttn_Gradient_X_val_jsd.csv0,040,020,040,04-0,070,03Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv0,12-18%0,0990,13-13%0,1140,19-7%0,1770,21-0,216%0,2220,08-5%0,076Std JS divAttn_Integrated_Gradient_X_val_jsd.csv0,050,020,050,060,060,04-ortho lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv -0,726n/avail-0,903n/avail-0,686n/avail--0,878n/avail-0,747Std Pearson corrAttn_Gradient_X_val_pearsonr.csv -Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv -0,689n/avail-0,714n/avail-0,668n/avail--0,858n/avail-0,708Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csv -Overall mean JS divAttn_Gradient_X_val_jsd.csv -0,143n/avail-0,126n/avail-0,163n/avail--0,174n/avail-0,184Std JS divAttn_Gradient_X_val_jsd.csv -Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv -0,148n/avail-0,183n/avail-0,170n/avail--0,152n/avail-0,186Std JS divAttn_Integrated_Gradient_X_val_jsd.csv -diversity lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv0,832%0,8490,893%0,9170,79-18%0,6450,77-0,96-5%0,9140,80-3%0,780Std Pearson corrAttn_Gradient_X_val_pearsonr.csv0,190,040,120,14-0,080,21Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,793%0,8150,781%0,7890,79-29%0,5590,77-0,6729%0,8670,74-5%0,707Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,220,070,140,14-0,110,22Overall mean JS divAttn_Gradient_X_val_jsd.csv0,0818%0,0940,0917%0,1050,1333%0,1730,12-0,06180%0,1680,12-24%0,091Std JS divAttn_Gradient_X_val_jsd.csv0,050,010,040,04-0,040,07Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv0,0912%0,1010,1313%0,1470,19-2%0,1870,12-0,0791%0,1340,15-31%0,103Std JS divAttn_Integrated_Gradient_X_val_jsd.csv0,050,020,050,040,050,06FIGURE 5IndicatorSource of infoDistribution of cumul. attention to POS tagsvanilla lstmOrder of POS prevalencequant_pos_attn.png[NOUN,ADJ,VERB,ADP,ADP] [NOUN,ADJ,VERB,ADP,ADV] [PUNC,NOUN,ADJ,VERB,ADV,DET] [NOUN,VERB,ADJ,ADV,DET] [NOUN,VERB,ADJ,ADP,DET] [NOUN,VERB,ADJ,ADP,DET] [NOUN,VERB,ADJ,PUNC,ADP] [NOUN,VERB,PUNC,ADJ,ADP]%attention PUNC0% 0%0%28%0%2%3%10%11%%attention ADJ20% 17%28%17%17%11%8%12%10%ortho lstm Order of POS prevalencequant_pos_attn.png [NOUN,ADJ,VERB,ADV,PRON] [NOUN,ADJ,VERB,ADV,ADP] [NOUN,ADJ,VERB,PRON,ADV]%attention PUNC 0%0%-0%3%%attention ADJ 25%35%-10%14%diversity lstmOrder of POS prevalencequant_pos_attn.png[NOUN,ADJ,VERB,ADV,ADP] [NOUN,ADJ,VERB,ADV,ADP] [ADJ,NOUN,VERB,ADV,DET] [NOUN,VERB,ADJ,ADV,PRON] [NOUN,ADJ,VERB,ADV,ADP]  [NOUN,ADJ,VERB,ADV,...] [NOUN,ADJ,VERB,PRON,ADV] [NOUN,VERB,ADJ,PRON,ADV]%attention PUNC00%0%3%0%0%0%3%5%%attention ADJ28%25%35%30%17%10%8%13%12%%Change%attention PUNC%attention ADJ40%47%25%76%0%-9%0%8%20%TABLE 5IndicatorSource of infoPreference given to vanilla vs diversity models (human annotators)

Figure 3. Replication results for dual sequence tasks


Color coding:datasetdatasetdatasetdatasetdatasetdatasetRelative difference between test runs and original experimentSNLIQQPBabi-1Babi-2Babi-3CNNMODELPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNIndicatorSource of inforel%AVGrel%AVGrel%AVGrel%AVGrel%AVGrel%AVGTABLE 2vanilla lstmtest accuracy best modelevaluate.json0,782-1%0,7730,7870%0,7840,9911%1,0000,40136%0,5440,477-56%0,2110,631-6%0,595Benchmark dataconicity_meanevaluate.json0,5605%0,5890,590-1%0,5830,56037%0,7660,480-10%0,4320,430116%0,9270,450-12%0,395conicity_stdevaluate.jsonn/avail-0,079n/avail-0,131n/avail-0,023n/avail-0,048n/avail-0,044n/avail-0,046ortho lstmtest accuracy best modelevaluate.json0,7650%0,7660,7860%0,7860,9990%0,9990,5615%0,5900,51213%0,5770,543-1%0,536conicity_meanevaluate.json0,27013%0,3060,330-4%0,3170,2205%0,2300,210-20%0,1690,12012%0,1350,07041%0,099conicity_stdevaluate.jsonn/avail-0,071n/avail-0,055n/avail-0,049n/avail-0,030n/avail-0,018n/avail--diversity lstmtest accuracy best modelevaluate.json0,770-4%0,7400,7840%0,7821,0000%1,0000,40236%0,5460,50911%0,5630,582-20%0,463conicity_meanevaluate.json0,120-64%0,0430,040-17%0,0330,0705%0,0730,050158%0,1290,1009%0,1090,060528%0,377conicity_stdevaluate.jsonn/avail-0,022n/avail-0,023n/avail-0,023n/avail-0,030n/avail-0,024n/avail--FIGURE 3IndicatorSource of infoFraction of hidden representationsvanilla lstm - ATTNmedianimportance_ranking_MAvDY_all.png0,3301,000%1,0000,06-33%0,040-0,020-0,030-0,020Box plots1st quartileimportance_ranking_MAvDY_all.png0,1000,66-39%0,4000,05-60%0,020-0,010-0,010-0,010visual inspection paper3rd quartileimportance_ranking_MAvDY_all.png0,8601,000%1,0000,10-40%0,060-0,030-0,050-0,030RANDOMmedianimportance_ranking_MAvDY_all.png0,8001,000%1,0001,00-50%0,500-0,550-0,550-0,6601st quartileimportance_ranking_MAvDY_all.png0,5300,85-18%0,7000,90-67%0,300-0,300-0,250-0,3303rd quartileimportance_ranking_MAvDY_all.png1,0001,000%1,0001,00-30%0,700-0,800-0,850-0,900orth lstm - ATTNmedianimportance_ranking_MAvDY_all.png0,3000,6017%0,7000,040%0,040-0,020-0,010-0,0501st quartileimportance_ranking_MAvDY_all.png0,1000,2025%0,2500,01100%0,020-0,010-0,000-0,0103rd quartileimportance_ranking_MAvDY_all.png0,8001,000%1,0000,07-14%0,060-0,030-0,020-0,200RANDOMmedianimportance_ranking_MAvDY_all.png0,7501,000%1,0000,4511%0,500-0,550-0,500-0,8301st quartileimportance_ranking_MAvDY_all.png0,4700,66-9%0,6000,2520%0,300-0,300-0,250-0,4703rd quartileimportance_ranking_MAvDY_all.png1,0001,000%1,0000,700%0,700-0,800-0,750-0,950diversity lstm - ATTNmedianimportance_ranking_MAvDY_all.png0,4600,809%0,8700,040%0,040-0,020-0,020-0,0201st quartileimportance_ranking_MAvDY_all.png0,1000,5010%0,5500,01100%0,020-0,010-0,010-0,0103rd quartileimportance_ranking_MAvDY_all.png0,8201,000%1,0000,08-25%0,060-0,030-0,030-0,030RANDOMmedianimportance_ranking_MAvDY_all.png0,8201,000%1,0000,70-29%0,500-0,550-0,500-0,7001st quartileimportance_ranking_MAvDY_all.png0,5000,80-6%0,7500,35-14%0,300-0,300-0,250-0,3303rd quartileimportance_ranking_MAvDY_all.png1,0001,000%1,0001,00-30%0,700-0,800-0,750-0,900FIGURE 4IndicatorSource of infoComparisonvanilla lstm - [0.00-0.25]medianPermutation.png---0,070---0,800-0,500-0,600Violin plots[0.25-0.50]medianPermutation.png---0,100-0,820-0,920-0,650-0,700visual inspection paper[0.50-0.75]medianPermutation.png---0,100-0,870-0,920-0,650-0,900[0.75-1.00]medianPermutation.png---0,100-0,900-0,970-0,700-0,950ortho lstm - [0.00-0.25]medianPermutation.png---0,070-0,400-0,750-0,700-0,600[0.25-0.50]medianPermutation.png---0,100-0,750-0,900-0,750-0,800[0.50-0.75]medianPermutation.png---0,100-0,980-0,900-0,850-0,950[0.75-1.00]medianPermutation.png---0,150-0,980-0,950-0,950--diversity lstm - [0.00-0.25]medianPermutation.png---0,070---0,820-0,750-0,550[0.25-0.50]medianPermutation.png---0,170-0,850-0,950-0,850-0,700[0.50-0.75]medianPermutation.png---0,250-0,870-0,970-0,900-0,900[0.75-1.00]medianPermutation.png---0,200-0,870-0,970-0,950-0,800TABLE 3IndicatorSource of infoMean attention given to rationalesvanilla lstmRationale attentionrationale_summary_test.txt-----------Rationale lengthrationale_summary_test.txt-----------ortho lstmRationale attentionrationale_summary_test.txt-----------Rationale lengthrationale_summary_test.txt-----------diversity lstmRationale attentionrationale_summary_test.txt-----------Rationale lengthrationale_summary_test.txt-----------TABLE 4IndicatorSource of infoComparison to gradient methodsvanilla lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv0,58-4%0,5560,19116%0,4100,5671%0,9590,16294%0,6300,3921%0,4700,5835%0,782CorrelatonsStd Pearson corrAttn_Gradient_X_val_pearsonr.csv0,330,340,340,230,240,25We use std.dev in paper to judge replication scores (colors)Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,381%0,384-0,06-240%0,0840,33138%0,7850,05432%0,266-0,01#####0,3620,4542%0,641Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,400,340,370,220,080,28Overall mean JS divAttn_Gradient_X_val_jsd.csv0,114%0,1140,15-33%0,1010,33-64%0,1200,53-27%0,3890,46-43%0,2630,22-29%0,157Std JS divAttn_Gradient_X_val_jsd.csv0,070,080,120,090,080,07Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv0,16-10%0,1430,19-22%0,1480,43-43%0,2470,58-12%0,5100,64-46%0,3480,30-25%0,225Std JS divAttn_Integrated_Gradient_X_val_jsd.csv0,090,100,130,090,050,10ortho lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csvn/avail-0,506n/avail-0,378n/avail-0,867n/avail-0,709n/avail-0,665n/avail-0,204Std Pearson corrAttn_Gradient_X_val_pearsonr.csvOverall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csvn/avail-0,365n/avail-0,238n/avail-0,709n/avail-0,227n/avail-0,044n/avail-0,099Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csvOverall mean JS divAttn_Gradient_X_val_jsd.csvn/avail-0,120n/avail-0,120n/avail-0,212n/avail-0,384n/avail-0,426n/avail-0,391Std JS divAttn_Gradient_X_val_jsd.csvOverall mean JS divAttn_Integrated_Gradient_X_val_jsd.csvn/avail-0,146n/avail-0,140n/avail-0,282n/avail-0,540n/avail-0,639n/avail-0,439Std JS divAttn_Integrated_Gradient_X_val_jsd.csvdiversity lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv0,51-2%0,4980,58-15%0,4940,91-7%0,8500,70-13%0,6120,6710%0,7360,75-50%0,375Std Pearson corrAttn_Gradient_X_val_pearsonr.csv0,350,310,100,130,190,20Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,265%0,2740,21-45%0,1160,91-9%0,8240,753%0,7710,47-44%0,2650,66-87%0,086Std Pearson corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,390,360,100,100,250,23Overall mean JS divAttn_Gradient_X_val_jsd.csv0,109%0,1090,1010%0,1100,217%0,2260,2372%0,3960,37-3%0,3590,17101%0,342Std JS divAttn_Gradient_X_val_jsd.csv0,060,050,080,060,078,00Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv0,1311%0,1440,15-6%0,1410,24-8%0,2210,19206%0,5820,4156%0,6410,21143%0,511Std JS divAttn_Integrated_Gradient_X_val_jsd.csv0,060,060,080,050,080,10FIGURE 5IndicatorSource of infoDistribution of cumul. attention to POS tagsvanilla lstmOrder of POS prevalencequant_pos_attn.png[NOUN, VERB, ADJ, DET, ADP, .] [NOUN, PUNC, VERB, ADP, ADJ, DET] [NOUN, VERB, . ADJ, ADP, DET, ADV] [NOUN] [NOUN] [NOUN, VERB, PRT, ., DET] [NOUN, VERB, ADJ, .]%attention PUNC23%9%0%1%8%3%%attention ADJ7%9%0%0%0%9%ortho lstm Order of POS prevalencequant_pos_attn.png[NOUN, VERB, DET, ADP, ADJ, .] [NOUN, VERB, ., ADJ, DET, ADP, ADV] [NOUN, DET] [NOUN] [NOUN] [PUNC, ADP, DET, NOUN, VERB]%attention PUNC17%0%0%0%20%%attention ADJ10%0%0%0%3%diversity lstmOrder of POS prevalencequant_pos_attn.png[NOUN, VERB, DET, ADP, ., ADJ] [NOUN, VERB, ADJ, ADP, PRON] [NOUN, VERB, ADJ, ADP, DET, ., ADV] [NOUN] [NOUN] [NOUN] [NOUN, VERB, ADJ, ADP, DET]%attention PUNC3%5%0%0%0%3%%attention ADJ10%9%0%0%0%9%%Change%attention PUNC%attention ADJ43%0%TABLE 5IndicatorSource of infoPreference given to vanilla vs diversity models (human annotators)

Appendix C: Results of BiLSTM extension

Figure 4. Performance of BiLSTM on evaluation metrics


Color coding:datasetdatasetdatasetdatasetRelative difference vs. Vanilla Bi-LSTMimdb20NewsQQPBabi-1(green = expected improvement)MODELPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNPAPERdeltaTEST RUNIndicatorSource of inforel%AVGrel%AVGrel%AVGrel%AVGTABLE 2vanilla lstmtest accuracy best modelevaluate.json0,8950,8930,9360,9080,7870,7840,9911,000Benchmark dataconicity_meanevaluate.json0,6900,6020,7700,7610,5900,5830,5600,766conicity_stdevaluate.jsonn/avail0,135n/avail0,189n/avail0,131n/avail0,023bi lstmtest accuracy best modelevaluate.json-0,905-0,919-0,790-0,997conicity_meanevaluate.json-0,590-0,818-0,610-0,692conicity_stdevaluate.json-0,118-0,136-0,103-0,042ortho bi lstmtest accuracy best modelevaluate.json-1%0,893-4%0,885-1%0,7850%1,000conicity_meanevaluate.json-70%0,176-54%0,373-44%0,341-68%0,220conicity_stdevaluate.json-0,045-0,156-0,068-0,055diversity bi lstmtest accuracy best modelevaluate.json-1%0,8921%0,924-1%0,7860%1,000conicity_meanevaluate.json-76%0,144-80%0,164-94%0,035-93%0,046conicity_stdevaluate.json-0,025-0,074-0,019-0,016FIGURE 3IndicatorSource of infobi lstm - ATTNmedianimportance_ranking_MAvDY_all.png -0,980 -0,520 -0,830 0,0301st quartileimportance_ranking_MAvDY_all.png -0,670 -0,520 -0,380 0,0203rd quartileimportance_ranking_MAvDY_all.png -1,000 -1,000 -1,000 0,080RANDOMmedianimportance_ranking_MAvDY_all.png -0,920 -0,980 -0,740 0,6001st quartileimportance_ranking_MAvDY_all.png -0,920 -0,980 -0,740 0,3203rd quartileimportance_ranking_MAvDY_all.png -1,000 -1,000 -1,000 0,820ortho bi lstm - ATTNmedianimportance_ranking_MAvDY_all.png -93%0,070 -52%0,250 -19%0,670 -33%0,0201st quartileimportance_ranking_MAvDY_all.png -97%0,020 -92%0,040 -39%0,230 -50%0,0103rd quartileimportance_ranking_MAvDY_all.png -87%0,130 -61%0,390 0%1,000 -50%0,040RANDOMmedianimportance_ranking_MAvDY_all.png 0%0,920 -3%0,950 -15%0,630 -13%0,5201st quartileimportance_ranking_MAvDY_all.png -22%0,720 -17%0,810 -15%0,630 -16%0,2703rd quartileimportance_ranking_MAvDY_all.png -3%0,970 0%1,000 0%1,000 -7%0,760diversity bi lstm - ATTNmedianimportance_ranking_MAvDY_all.png -93%0,070 -88%0,060 -40%0,500 -33%0,0201st quartileimportance_ranking_MAvDY_all.png -97%0,020 -94%0,030 32%0,500 -50%0,0103rd quartileimportance_ranking_MAvDY_all.png -67%0,330 -87%0,130 0%1,000 -50%0,040RANDOMmedianimportance_ranking_MAvDY_all.png 0%0,920 -8%0,900 -1%0,730 -13%0,5201st quartileimportance_ranking_MAvDY_all.png -24%0,700 -27%0,720 -1%0,730 -16%0,2703rd quartileimportance_ranking_MAvDY_all.png -2%0,980 -2%0,980 0%1,000 -6%0,770FIGURE 4IndicatorSource of infoComparisonvanilla lstm - [0.00-0.25]medianPermutation.png0,160,1800,050,0200,070-Violin plots[0.25-0.50]medianPermutation.png0,170,2000,150,0800,1000,820visual inspection paper[0.50-0.75]medianPermutation.pngn/appl-0,23-0,1000,870[0.75-1.00]medianPermutation.pngn/appl-0,28-0,1000,900bi lstm - [0.00-0.25]medianPermutation.png-0,100-0,010-0,020--[0.25-0.50]medianPermutation.png-0,090-0,200-0,080-0,570[0.50-0.75]medianPermutation.png---0,270-0,210-0,920[0.75-1.00]medianPermutation.png---0,730-0,430-0,970ortho bi lstm - [0.00-0.25]medianPermutation.png330%0,4304100%0,420-50%0,010--[0.25-0.50]medianPermutation.png422%0,47095%0,3900%0,08075%1,000[0.50-0.75]medianPermutation.png-0,49059%0,430-10%0,1909%1,000[0.75-1.00]medianPermutation.png-0,420-44%0,410-42%0,2503%1,000diversity bi lstm - [0.00-0.25]medianPermutation.png300%0,4004500%0,460150%0,050--[0.25-0.50]medianPermutation.png367%0,420135%0,47088%0,150--[0.50-0.75]medianPermutation.png-0,52074%0,4705%0,220-5%0,870[0.75-1.00]medianPermutation.png---33%0,490-23%0,330-10%0,870TABLE 4IndicatorSource of infoComparison to gradient methodsvanilla lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv0,800,8630,720,5130,190,4100,560,959Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv0,680,7930,650,390-0,060,0840,330,785Overall mean JS divAttn_Gradient_X_val_jsd.csv0,090,0800,150,1820,150,1010,330,120Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv0,130,1140,210,2220,190,1480,430,247bi lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv 0,8170,5350,3450,867Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv 0,6800,4110,0180,643Overall mean JS divAttn_Gradient_X_val_jsd.csv 0,0910,1160,1550,210Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv 0,1470,1410,2130,343ortho bi lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv 14%0,930-35%0,34632%0,457-1%0,862Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv 25%0,849-4%0,3941894%0,35915%0,738Overall mean JS divAttn_Gradient_X_val_jsd.csv -5%0,086258%0,415-14%0,133-5%0,199Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv -29%0,105174%0,386-31%0,148-15%0,292diversity bi lstmOverall mean Pear. corrAttn_Gradient_X_val_pearsonr.csv 11%0,90879%0,96050%0,516-65%0,307Overall mean Pear. corrAttn_Integrated_Gradient_X_val_pearsonr.csv 25%0,847114%0,8801756%0,334-11%0,571Overall mean JS divAttn_Gradient_X_val_jsd.csv 19%0,108-16%0,097-34%0,103106%0,433Overall mean JS divAttn_Integrated_Gradient_X_val_jsd.csv -16%0,124-23%0,108-39%0,1305%0,359

Appendix D: Selected data examples and illustration of model behavior

Figure 5. Examples of single input sequence tasks


SST examples SST, Vanilla-LSTM, trained on default (tanh) attention (test acc=.805, conicity=.697) Sentence   : <SOS>     a     slick     skillful     little     horror     film     <EOS>      Attentions : 0.00      0.04  0.08      0.20         0.30       0.24       0.13     0.00       SM(||h_i||): 0.00      0.09  0.17      0.24         0.17       0.17       0.17     0.00 Label:  1 , Prediction:  [0.5812621] SST, Ortho-LSTM, trained on default (tanh) attention (test acc=.776, conicity=.283) Sentence   : <SOS>     a     slick     skillful     little     horror     film     <EOS>    Attentions : 0.00      0.00  0.03      0.64         0.18       0.04       0.11     0.00       SM(||h_i||): 0.00      0.15  0.14      0.21         0.10       0.16       0.25     0.00   Label:  1 , Prediction:  [0.7968075] SST, Diversity-LSTM, trained on default (tanh) attention (test acc=.800, conicity=.188) Sentence   : <SOS>     a     slick     skillful     little     horror     film     <EOS>  Attentions : 0.00      0.00  0.12      0.86         0.01       0.01       0.01     0.00       SM(||h_i||): 0.00      0.02  0.04      0.19         0.25       0.16       0.34     0.00   Label:  1 , Prediction:  [0.9623399]  Yelp examples Yelp, Vanilla-LSTM, trained on default (tanh) attention (test acc=.949, conicity=.536) Sentence   : <SOS>     Been     going     here     for     years.     A     great     place!     <EOS> Attentions : 0.00      0.35     0.09      0.06     0.01    0.01       0.04  0.18      0.26       0.00        SM(||h_i||): 0.00      0.08     0.07      0.10     0.08    0.09       0.06  0.18      0.35       0.00 Label:  1 , Prediction:  [0.984035] Yelp, Ortho-LSTM, trained on default (tanh) attention (test acc=.945, conicity=.186) Sentence   : <SOS>     Been     going     here     for     years.     A     great     place!     <EOS>  Attentions : 0.00      0.53     0.00      0.00     0.00    0.08       0.00  0.22      0.17       0.00       SM(||h_i||): 0.00      0.18     0.08      0.05     0.07    0.04       0.03  0.34      0.21       0.00 Label:  1 , Prediction:  [0.99045765] Yelp, Diversity-LSTM, trained on default (tanh) attention (test acc=.938, conicity=.347) Sentence   : <SOS>     Been     going     here     for     years.     A     great     place!     <EOS>  Attentions : 0.00      0.41     0.16      0.00     0.00    0.02       0.09  0.21      0.10       0.00       SM(||h_i||): 0.00      0.18     0.05      0.02     0.04    0.03       0.06  0.40      0.21       0.00    Label:  1 , Prediction:  [0.9969946] Yelp, Vanilla-LSTM, trained on last_only attention (test acc=0.949, conicity=0.760) Sentence   : <SOS>     Simply     a     bad     place.     Owner     has     no     clue.     Very     <UNK>     <EOS> Attentions : 0.00      0.00       0.00  0.00    0.00       0.00      0.00    0.00   0.00      0.00     1.00      0.00       SM(||h_i||): 0.00      0.03       0.03  0.09    0.07       0.08      0.06    0.15   0.15      0.15     0.20      0.00     Label:  0 , Prediction:  [0.00001468] Yelp, Vanilla-LSTM, trained on first_only attention (test acc=, conicity=0) Sentence   : <SOS>     Horrible!     Can't     even     describe     this     crap.     Nothing     was     what     I     ordered   <EOS> Attentions : 0.00      1.00          0.00      0.00     0.00         0.00     0.00      0.00        0.00    0.00     0.00  0.00      0.00 SM(||h_i||): 0.00      0.22          0.07      0.07     0.06         0.06     0.11      0.09        0.08    0.07     0.06  0.12      0.00  Label:  0 , Prediction:  [0.00556918] SNLI examples SNLI, Vanilla-LSTM, trained on equal attention (test acc=0.755, conicity=0.657) P path     : <SOS>     girl     in     red     jumping     up     <EOS>      Attentions : 0.00      0.20     0.20   0.20    0.20        0.20   0.00       SM(||h_i||): 0.00      0.21     0.16   0.21    0.24        0.18   0.00       Q path     : <SOS>  the  girl  is  sitting  on  the  grass  .  <EOS>   Answer: contradiction  Predicted: contradiction QQP examples QQP, Vanilla-LSTM, trained on tanh attention (test acc=0.785, conicity=0.577) P path     : <SOS>     what     is     alkali     ?     <EOS>      Attentions : 0.00      0.28     0.31   0.31       0.10  0.00      SM(||h_i||): 0.00      0.13     0.16   0.15       0.55  0.00       Q path     : <SOS>  what  mean  by  alkali  ?  <EOS>   Answer: 1  Predicted: 1 QQP, Vanilla-LSTM, trained on equal attention (test acc=0.789, conicity=0.603) P path     : <SOS>     what     is     alkali     ?     <EOS>      Attentions : 0.00      0.25     0.25   0.25       0.25  0.00       SM(||h_i||): 0.00      0.21     0.17   0.12       0.50  0.00       Q path     : <SOS>  what  mean  by  alkali  ?  <EOS>   Answer: 1  Predicted: 1 

Figure 6. Examples of dual input sequence tasks


bAbI-1 examples Babi_1, Vanilla-LSTM, trained on equal attention (test acc=0.477, conicity=0.450) P path     : <SOS>     Sandra     went     to     the     bedroom     .     Sandra     travelled     to     the     office     <EOS>      Attentions : 0.00      0.09       0.09     0.09   0.09    0.09        0.09  0.09       0.09          0.09   0.09    0.09       0.00       SM(||h_i||): 0.00      0.02       0.01     0.02   0.07    0.17        0.09  0.06       0.04          0.06   0.23    0.25       0.00       Q path     : <SOS>  Where  is  Sandra  <EOS>   Answer: office  Predicted: office bAbI-2 examples Babi_2, Vanilla-LSTM, trained on equal attention (test acc=0.315, conicity=0.334) P path       : <SOS>   Sandra     travelled     to     the     office    .     Daniel     moved     to     the     kitchen     .        Attentions : 0.00    0.03       0.03          0.03   0.03    0.03      0.03  0.03       0.03      0.03   0.03    0.03        0.03      Mary     travelled     to     the     bathroom   .     Sandra   took    the     football  there   .        0.03     0.03          0.03    0.03   0.03       0.03  0.03     0.03    0.03    0.03      0.03    0.03   Daniel    picked  up     the     apple   there  .     Sandra   went     back   to     the     kitchen   <EOS>   0.03      0.03    0.03   0.03    0.03    0.03   0.03  0.03     0.03     0.03   0.03   0.03    0.03      0.00   Q path     : <SOS>  Where  is  the  football  <EOS>   Answer: kitchen  Predicted: kitchen  CNN examples CNN, Vanilla-LSTM, trained with default (tanh) attention (test acc=.595, conicity=.395) P path     : <SOS>     (     @entity2     )     one   @entity1   citizen   was     killed   and     another   injured   in     what     Attentions : 0.00      0.00  0.00         0.00  0.04  0.06       0.08      0.01    0.00     0.00    0.00      0.00      0.00   0.00      police     are     calling     a     suspected     terror     attack   wednesday     night     near     @entity6   .     @entity8     0.00       0.00    0.00        0.00  0.00          0.00       0.00     0.00          0.00      0.00     0.00       0.00  0.07         spokesman     @entity7     said     a     37     -     year    -     old   @entity10   motorist    from   @entity11   struck     two     0.02          0.00         0.00     0.00  0.00   0.00  0.00    0.00  0.00  0.43        0.00        0.00   0.03        0.00       0.00    people   standing   at    a     bus     stop    in     the    @entity15   section   of     the   city     .     one     victim   , 0.00     0.00       0.00  0.00  0.00    0.00    0.00   0.00   0.00        0.00      0.00   0.00  0.00     0.00  0.00    0.00     0.00   identified   by    police   as   @entity18  ,     26    ,     died   at     the     hospital   .     a     20     -     year     -   0.00         0.00  0.00     0.00 0.20       0.00  0.00  0.00  0.00   0.00   0.00    0.00       0.00  0.00  0.00   0.00  0.00     0.00   old   woman   remains   in    serious   condition ,     according     to     @entity7     .     the     driver     has     been   0.00  0.00    0.00      0.00  0.00      0.00      0.00  0.00          0.00   0.00         0.00  0.00    0.00       0.00    0.00      arrested   and   is    under   investigation  by     the   @entity24     .     "     from     the     investigation     and     first    0.00       0.00  0.00  0.00    0.00           0.00   0.00  0.02          0.00  0.00  0.00     0.00    0.00              0.00    0.00       findings   ,    there  is    a     strong   suspicion  that   we     're     talking     about     a     terror     attack     ,    0.00       0.00 0.00   0.00  0.00  0.00     0.00       0.00   0.00   0.00    0.00        0.00      0.00  0.00       0.00       0.00   "     @entity7     said     .     amid   the   ongoing   investigation   ,     a     magistrate   court     has     issued     a    0.00  0.00         0.00     0.00  0.00   0.00  0.00      0.00            0.00  0.00  0.00         0.00      0.00    0.00       0.00   gag     order     on     details     of     the     incident     .     <EOS>     0.00    0.00      0.00   0.00        0.00   0.00    0.00         0.00  0.00      Q path     : <SOS>  the  suspect  is  a  37  -  year  -  old  @placeholder  from  @entity11  ,  @entity1  police  say  <EOS>   Answer: @entity10  Predicted: @entity10  CNN, Ortho-LSTM, trained with default (tanh) attention (test acc=.536, conicity=.099) P path     : <SOS>   (     @entity2   )     one     @entity1   citizen  was     killed     and     another   injured     in     what    Attentions : 0.00    0.00  0.19       0.00  0.00    0.00       0.00     0.01    0.00       0.02    0.00      0.00        0.02   0.00    police   are     calling     a     suspected     terror     attack     wednesday     night     near     @entity6     .     @entity8    0.00     0.00    0.00        0.00  0.00          0.00       0.00       0.00          0.01      0.00     0.00         0.03  0.00        spokesman   @entity7   said   a     37    -     year   -     old     @entity10     motorist     from   @entity11     struck     two    0.00        0.00       0.03   0.02  0.00  0.02  0.00   0.01  0.00    0.00          0.00         0.01   0.00          0.01       0.00   people   standing  at     a     bus   stop   in     the    @entity15   section  of     the     city   .     one     victim     ,    0.00     0.05      0.13   0.06  0.00  0.00   0.15   0.01   0.00        0.04     0.03   0.01    0.00   0.02  0.00    0.00       0.00 identified  by    police  as   @entity18  ,     26    ,     died   at     the     hospital     .     a     20     -     year     -    0.00        0.00  0.00    0.00 0.00       0.00  0.00  0.00  0.00   0.00   0.02    0.00         0.00  0.01  0.00   0.02  0.00     0.01 old   woman   remains   in     serious   condition     ,     according     to     @entity7     .     the     driver     has     been    0.00  0.00    0.00      0.00   0.00      0.00          0.00  0.00          0.00   0.00         0.01  0.00    0.00       0.00    0.00    arrested  and   is     under    investigation  by     the     @entity24  .     "     from     the     investigation     and     first    0.00      0.00  0.00   0.00     0.00           0.00   0.00    0.00       0.00  0.00  0.00     0.00    0.00              0.00    0.00     findings  ,     there  is     a     strong   suspicion  that    we     're     talking     about     a     terror     attack     ,    0.00      0.01  0.00   0.00   0.00  0.00     0.00       0.00    0.00   0.00    0.00        0.00      0.00  0.00       0.00       0.00 "     @entity7  said   .     amid   the    ongoing   investigation     ,     a     magistrate     court     has     issued     a    0.00  0.00      0.00   0.01  0.00   0.00   0.00      0.00              0.00  0.00  0.00           0.00      0.00    0.00       0.00 gag    order    on     details   of     the     incident     .     <EOS>      0.00   0.00     0.00   0.00      0.00   0.00    0.00         0.00  0.00       Q path     : <SOS>  the  suspect  is  a  37  -  year  -  old  @placeholder  from  @entity11  ,  @entity1  police  say  <EOS>   Answer: @entity10  Predicted: @entity10

---
**Source PDF:** `2021_22_article.pdf`
