R E S C I E N C E C

Replication / Machine Learning


Valter Hudovernik1, ID , Žiga Rot1, ID , Klemen Vovk1, ID , Luka Škodnik1, ID , and Luka Čehovin Zajc1, ID
1University of Ljubljana, Faculty of Computer and Information Science, Večna pot 113, 1000 Ljubljana

Edited by
Nicolas P. Rougier ID

Reviewed by
anonymous
anonymous

Received
15 October 2025

Published
28 January 2026

Abstract Learning with noisy labels (LNL) is a subfield of supervised machine learning investigating scenarios in
which the training data contain errors. While most research has focused on synthetic noise, where labels are ran-
domly corrupted, real-world noise from human annotation errors is more complex and less understood. Wei et al.
(2022) introduced CIFAR-N, a dataset with human-labeled noise and claimed that real-world noise is fundamentally
more challenging than synthetic noise. This study aims to reproduce their experiments on testing the characteris-
tics of human-annotated label noise, memorization dynamics, and benchmarking of LNL methods. We successfully
reproduce some of the claims but identify some quantitative discrepancies. Notably, our attempts to reproduce the
reported benchmark reveal inconsistencies in the reported results. To address these issues, we develop a unified
framework and propose a refined benchmarking protocol that ensures a fairer evaluation of LNL methods. Our find-
ings confirm that real-world noise differs structurally from synthetic noise and is memorized more rapidly by deep
networks. By open-sourcing our implementation, we provide a more reliable foundation for future research in LNL.

DOI
10.5281/zenodo.18401497

## 1 Introduction

Learning with noisy labels (LNL) is a fundamental challenge in supervised machine
learning, where errors in training data labels can significantly degrade model performance [1]. Deep neural networks, in particular, are prone to memorizing mislabeled
examples [2], leading to overfitting and poor generalization [3]. Addressing this issue is
crucial for real‐world applications, where high‐quality labeled data is expensive and human annotation errors are inevitable. Most of the research in LNL has focused on synthetic noise, where labels are artificially corrupted under controlled conditions, such
as random class swaps. Although this provides a straightforward experimental setup, it
fails to capture the complexity of real‐world label noise [4].

A wide range of techniques have been developed to mitigate the effects of noisy labels.
The problem setup shared among all of them involves training an underlying classifier
(e.g., a ResNet [5]) with a learning strategy robust to label noise. Figure 1 illustrates the
general setup. Common approaches in the field include using loss functions robust to
noise [6, 7, 8], adding specialized regularization [9, 10], adjusting loss based on noise
estimations [11, 12, 13], filtering noisy samples [14, 15, 16], and adding additional layers
to the base classifier [17, 18]. For a detailed survey of LNL approaches, we refer the
reader to [19].

Despite significant progress, most of these methods have been evaluated under synthetic noise assumptions, which do not fully reflect real‐world annotation errors. Unlike
synthetic noise, real‐world noise tends to be instance‐dependent [20], correlating with
visual similarity between classes and annotator biases [21].

To bridge the gap between synthetic and real‐world label noise, Wei et al.[21] introduced
CIFAR‐N, a dataset containing human‐annotated label noise based on CIFAR‐10 and


Code is available at https://github.com/KlemenVovk/noisy-labels. – SWH swh:1:dir:22222955c66aeb7e379a16b45d208fcf3d64a11d.
Open peer review is available at https://openreview.net/forum?id=GKZ2leags0.




Figure 1. An illustration of a setup for learning with noisy labels. During the training phase (left
side), the model is trained using samples with potentially corrupted labels. The LNL algorithm
tries to mitigate this noise. During the evaluation phase (right side), the trained model is evaluated
with uncorrupted labels.

CIFAR‐100 [22]. They investigate how real‐world noise impacts learning and whether
existing LNL methods remain effective in practical scenarios and claim that learning
with real‐world noise is fundamentally more challenging than with synthetic noise. Finally, they evaluate 20 state‐of‐the‐art LNL methods on the proposed dataset.

Their key findings suggest that real‐world noise differs structurally from synthetic noise,
as it is feature‐dependent and often reflects human annotation tendencies rather than
random corruption. Additionally, deep networks memorize real‐world noise more rapidly, overfitting human‐labeled noise faster than synthetic noise, leading to different learning dynamics. Consequently, the benchmark results indicate that real‐world noise poses
a harder challenge for LNL methods, as models trained on synthetic noise often achieve
significantly higher accuracy on clean data than those trained on human‐annotated
noisy labels.

Despite these contributions, the original work has several limitations. The code used to
conduct the experiments is not publicly available, and key methodological details are insufficiently described, making their claims difficult to verify. Moreover, the benchmark
results are published on public leaderboards and used as is in subsequent works [23, 24,
25], even though flaws in the testing methodology prevent direct and fair comparisons.
To address these issues, we make the following contributions:

1. We reproduce the experiments described by [21] and open‐source the code, so the
experiments can be replicated by others. Our source code is publicly available at
https://github.com/KlemenVovk/noisy-labels.

2. We implement a framework to benchmark LNL methods under controlled conditions. With it, we are able to establish unified noising and testing pipelines for all
methods. To our knowledge, our framework is the first such attempt in the LNL
field.

3. We benchmark LNL methods in a controlled environment, fixing the appropriate

parameters and enabling a fair comparison of LNL methods on CIFAR‐N.


ClassifierLNL MethodNoise ProcessClassifierEvaluation(Accuracy)CleanLabelsImagesNoisyLabelsTrainTest

## 2 Scope of Reproducibility

The original paper by [21] introduces the CIFAR‐N dataset, arguing that real‐world human annotation noise differs significantly from synthetic noise and presents a more
challenging learning problem. Their findings are based on a series of experiments comparing the characteristics of real and synthetic noisy labels, analyzing the memorization behavior of deep networks, and benchmarking 20, at the time, state‐of‐the‐art LNL
methods.

During their analysis of CIFAR‐N, the authors make several key observations: (1) the
noise distribution in CIFAR‐N is imbalanced, favoring similar‐looking classes, (2) misannotations primarily occur between visually similar categories, (3) the noise exhibits a
mix of symmetric and asymmetric patterns, (4) some noisy labels may reflect multiple
valid annotations rather than errors, and (5) learning on real‐world label noise is more
challenging than learning on synthetic noise. Based on these observations, they make
three central claims: (i) human annotation noise is feature‐dependent, (ii) deep networks memorize real‐world noisy labels faster than synthetic ones, and (iii) LNL methods more easily model synthetic noise than real‐world human annotation noise.

In this work, we aim to reproduce and validate these claims by conducting an independent evaluation of the key findings from the original study. Specifically, we investigate:

i. Differences Between Real‐World and Synthetic Noise: We replicate the hypothesis testing methodology to quantitatively compare human annotation noise with
synthetic noise. We assess whether real‐world noise is feature‐dependent and
whether label transitions exhibit different structural properties (Section 3.2).

ii. Memorization of Noisy Labels by Deep Networks: We reproduce the memorization
effect experiment to examine whether deep neural networks overfit real‐world
noisy labels faster than synthetic ones. We analyze the impact of different noise
levels and label sets on memorization trends (Section 3.3).

iii. Benchmarking of LNL Methods: We attempt to reproduce the benchmark results
reported for 10 of the 20 LNL methods, evaluating their performance on both realworld and synthetic noise. We investigate inconsistencies in the reported results
and assess whether the stated training methodology leads to the same outcomes
(Section 3.4).

iv. Evaluation of Benchmarking Methodology: We examine whether the benchmarking approach used in the original paper is fair and consistent across methods (Section 3.5).

Going beyond the original study, we propose a revised benchmarking protocol that ensures comparability across different LNL techniques. Throughout our study, we carefully document any deviations from the original methodology and highlight areas where
ambiguities in the original paper may have impacted reproducibility. By open‐sourcing
our implementation (https://github.com/KlemenVovk/noisy-labels), we aim to provide a transparent framework for future research in learning with noisy labels.

## 3 Methodology

We follow the authors’ described methodology for all experiments except when reproducing their LNL benchmark, which we justify in Section 3.4. Where the procedures are
originally not well described or are ambiguous, we describe our selected methodology
in greater detail. We also present why their benchmark results should not be used as a
benchmark and provide improvements that enable a fairer comparison.




### 3.1 Datasets

We use the CIFAR‐N datasets provided by the benchmark authors [21]. Their work is
based on the standard CIFAR‐10 and CIFAR‐100 datasets [22], consisting of 50, 000 train
and 10, 000 test images with image‐level class annotations. As the names suggest, CIFAR10 includes 10 label categories, while CIFAR‐100 has 100. The authors propose noisy extensions for both datasets, which keep the original images but replace the labels with
real‐world noisy annotations. Only the training sets of both datasets have these, while
the 10, 000 testing labels are kept from the original CIFAR‐10 and ‐100 datasets and are
considered noise‐free. The 50, 000 training labels from the original CIFAR datasets are
considered ground truth clean labels. The CIFAR‐10N extension includes five sets of
noisy labels obtained from different annotators with varying degrees of noise. Specifically, the authors present the following label sets:

• Random1, Random2, Random3: These directly include the labels submitted by
different annotators. These have a medium noise level, with 17.23%, 18.12%, and
17.64% noise ratios, respectively.

• Aggregate: Labels in this set are obtained from Random1, Random2 and Random3
via majority voting. Whenever there is a 3‐way disagreement, the label is selected
randomly. Due to the aggregation, the noise level here is the lowest at 9.03%.

• Worst: Similarly, as in the Aggregate set, labels here are also obtained from the
three Random sets but are aggregated so that incorrect labels are taken wherever
possible. As such, the noise level here is the highest, with 40.21% incorrect labels.

Clean‐to‐noisy label transition matrices in Figure 2 indicate percentages of misassigned
labels and common mistakes (e.g., mislabeling truck as an automobile).

Figure 2. Transition matrices of CIFAR10‐N for Aggregate, Random1 and Worst label sets. A single
row denotes the percentages of transitions of the row label to any of the column labels. Missing
numbers indicate that no such transition was found in the provided noisy label set. The color bar
is log‐norm transformed to highlight noise levels.

Similarly, the CIFAR‐100N extension includes two sets of real‐world noisy labels. Besides
the original 100 categories, the authors also present a new set of coarse annotations of 20
super‐classes to help the annotators during annotation. The annotators are first asked
to assign a super‐class, from which they then later select the fine‐grained class. The two
noisy label sets are then defined as follows:

• Coarse: consists of the 20 super‐class labels with a noise rate of 25.60%.

• Fine: consists of all 100 fine categories and has 40.20% of noisy labels.

The authors observe that in CIFAR‐100N some label noise may not necessarily indicate
incorrect annotations but rather the presence of multiple valid labels within an image.
We visualize some examples in Figure 3.


airplaneautomobilebirdcatdeerdogfroghorseshiptruckAggregated noisy labelsairplaneautomobilebirdcatdeerdogfroghorseshiptruckClean label0.940.010.010.000.000.000.000.000.030.000.010.950.000.00nannannan0.000.000.040.020.010.930.010.010.010.010.000.010.000.020.020.040.830.010.060.010.000.010.010.020.020.040.010.830.020.000.040.010.010.010.010.020.050.000.890.000.000.000.000.010.010.030.020.010.010.90nan0.010.010.010.000.010.000.010.01nan0.960.000.000.010.010.000.000.00nan0.00nan0.970.010.020.07nannannannan0.000.000.010.90airplaneautomobilebirdcatdeerdogfroghorseshiptruckRandom noisy labelsairplaneautomobilebirdcatdeerdogfroghorseshiptruckClean label0.850.030.030.010.010.010.010.010.040.010.010.850.000.010.010.000.010.000.010.100.020.020.840.020.030.020.020.020.010.010.020.020.040.740.020.110.020.020.010.010.010.020.030.020.760.050.020.080.010.010.010.010.020.080.020.820.010.010.000.000.010.010.040.040.020.020.830.010.010.010.010.010.010.010.020.020.010.900.010.000.030.030.010.010.010.010.010.010.880.020.020.130.000.010.010.010.010.010.010.81airplaneautomobilebirdcatdeerdogfroghorseshiptruckWorst noisy labelsairplaneautomobilebirdcatdeerdogfroghorseshiptruckClean label0.650.070.070.020.020.020.020.020.080.030.040.590.020.030.020.020.010.010.020.250.060.040.630.050.060.050.050.030.020.020.040.030.080.490.040.210.050.020.020.020.040.030.070.040.490.110.040.150.020.010.030.030.050.180.040.580.030.030.010.010.040.040.080.080.050.060.590.030.020.010.040.030.020.020.050.060.020.720.020.010.080.070.020.010.020.020.020.020.680.050.040.280.020.020.020.020.010.010.030.55101100

(a) A reproduction of Figure 4 by [21].

(b) Images to which their noisy labels might be better suited than their original labels.

Figure 3. Examples of training images with multiple valid labels from CIFAR‐100N. The first caption
contains the clean CIFAR‐100 label, and the bottom one is the human‐annotated ”noisy” label.

They provide examples of such cases, with the frequent case being a fisherman holding
a flatfish in his hands. We reproduce their exemplar images in Figure 3a. During our
analysis, we even observed that some noisy annotations actually describe the images
better than their original labels.

### 3.2 Reproducing Noise Hypothesis Testing

Wei et al.[21] qualitatively and quantitatively show that real‐world human noise differs
from synthetic noise with hypothesis testing. We follow the same procedure while taking note of certain ambiguous decisions.

We start by fitting a ResNet‐34 model on clean CIFAR‐10 train labels. The authors do not
explicitly explain how the model was trained, so we use the default training methodology presented in Section 3.4. Once trained, we use the classifier to get image embeddings for all 50, 000 training images.

Next, for each of the N = 10 classes, we cluster its embeddings into ν = 5 clusters
Cn,v, ∀n ∈ N, ∀v ∈ ν using a K‐Means model. As all cluster members belong to the
same clean class, we can then obtain a N ‐dimensional transition vector for each cluster: pn,v = [P( eY = j|Y = n, X ∈ Cn,v)]j∈[N ]. We do this for both real‐world and
synthetic labels, specifically the Random1 label set and its synthetic counterpart. We
generate the synthetic label set by sampling from an asymmetric transition matrix estimated from the CIFAR‐N noisy labels. Following the approach in the original paper, we
compute this matrix by counting class‐wise label flips between the human‐annotated
(noisy) labels and the clean labels. The resulting transition matrix (visualized in Figure 2) is then used to synthesize new noisy labels, producing a synthetic counterpart
following the same transition matrix but without instance‐dependence. At this point,
we plot the resulting transition vectors in each class and cluster and qualitatively check
for differences between the real‐world and synthetic transition vectors.

We repeat the previous steps E = 10 times, generating a new set of synthetic labels
and embeddings each time. To get different embeddings, we randomly augment the
images with horizontal flips and random crops. This gives us a set of transition vectors
{pe,k,v}e∈[E],k∈[K],v∈[ν] for both synthetic and human noise. From this data, we can obtain the two sets of l2 distances between the transition vectors – the human‐synthetic
distances:

e,k,v = ||phuman
and the synthetic‐synthetic distances:

{d(1)

e,k,v

− psynthetic
e,k,v

||2


}e∈[E],k∈[K],v∈[ν]

{d(2)

e,k,v = ||psynthetic

e,k,v

− psynthetic

(e+1)%E,k,v

||2


}e∈[E],k∈[K],v∈[ν].


lawn_mowermanbicyclemanplaincloudbeesunflowerbutterflypoppyflatfishmanpalm_treeseamountaincloudbeavermantablechairhousewillow_treeboybabymanboygirlbabycloudcanboybabycouchchairboybabymanboyboybaby

From here on, we use the same formulation and procedures for the hypothesis test as
in the original work [21].

### 3.3 Reproducing Noise Memorization

To further investigate the differences between artificial and real‐world noise,
[21], inspect the learning behavior of a classifier trained on both sets of noisy labels. Specifically, they compare the learning behavior on Aggregate, Random1, and Worst sets of
real‐world labels with their synthetic counterparts. The procedure to obtain synthetic
labels remains the same as described in Section 3.2. They check whether the ratio of
memorized examples increases faster for synthetic or real‐world noisy labels. In a Kclass classification task, given a classifier f , a feature x and confidence threshold η, x is
memorized by f if ∃i ∈ [K] s.t. P (f (x) = i) > η.

The authors do not explain the training setup beyond the fact that ResNet‐34 [5] is used
as a classifier with the confidence threshold η = 0.95. From the figures in the original paper, we deduce that each experiment was run for 150 epochs. Furthermore, we assume
that a smooth learning rate schedule was used, based on the shape of the memorization
curves. We obtain the rest of the hyperparameters from the memorization experiments
by [3] using the SGD optimizer without momentum and setting the initial learning rate
to γ = 1, weight decay to 1e − 4 and a smooth version of their learning rate 
(γt = γ · 0.1 t

50 ).

### 3.4 Reproducing the Benchmark

Due to the large computation cost (see Appendix E), we select a subset of 10 methods
that show good performance in the original results: CE (baseline), Co-Teaching [14], Co-
Teaching+ [15], ELR, ELR+ [26], Divide-Mix [27], VolMinNet [28], CAL [29], PES (semi) [18],
SOP, and SOP+ [30]. Here, we note that the author’s reported performance for the SOP
method is most likely SOP+, so we include both methods in our benchmark.

The authors do not describe the evaluation procedure for the benchmark, but we have
reproduced it based on GitHub issues and personal correspondence. During training
with each LNL method, the classifier is evaluated in terms of micro‐averaged accuracy
on a clean test set every epoch. At the end, the highest achieved accuracy is reported.
Each run is repeated three times to obtain the mean accuracy and the standard deviation.

While being a crucial part of many learning strategies, the benchmark authors do not
discuss the hyperparameters for each method in full detail. Therefore, we reference
their official implementations as a starting point and, as described by the authors, fix
the following1: training time to 100 epochs, a stochastic gradient descent optimizer with
momentum (0.9), weight decay (5e − 4), an initial learning rate of 0.1 which decreases to
0.01 at the 60th epoch, and a minibatch size of 128. The authors also note that the ELR
(+) and DivideMix methods received special treatment and were run using their original configurations. We observe that for SOP the pre‐activation ResNet‐18 was used2,
and based on the authors’ discussion with reviewers, that the low noise configuration
(λu = 0) was used for DivideMix3. Following these findings, we use ResNet‐34 for most
of the learning strategies and a pre‐activation ResNet‐18 for SOP, ELR+, and DivideMix,
consistent with the described setup.

1See [21] Appendix E.3.
2See [21] caption of Table 2 .
3See https://openreview.net/forum?id=TBWA6PLJZQm discussion with reviewer EZud.




As we later show in Section 4.3, following the methodology inferred from the original
study, we do not reach the same results. We argue that fixing the learning rate, optimizer, and the number of epochs without redoing the hyperparameter search reduces
the performance of methods (in a possibly uneven way). Instead, when using the original hyperparameter configurations for each LNL method along with the optimizers,
learning rates, and training durations, most of the methods perform close to the original reported accuracy.

Given these findings, it is likely that the original authors followed a methodology closer
to our reverse‐engineered approach rather than the one explicitly described in their paper. However, due to inconsistencies between the paper and the available implementation, as well as the discontinued correspondence with the original authors (see Appendix D.1), we are unable to verify this assumption with certainty.

### 3.5 Making the Benchmark Fair

We argue that this approach is flawed in several aspects and present a better evaluation
procedure. When benchmarking LNL methods, the authors use a clean test set to measure accuracy every epoch, selecting the highest one at the end. This overestimates the
real‐world performance and is thus unreliable in practice [31].

During our experiments, we observed that the underlying classifier strongly influences
the final performance. Given that the authors do not use the same ResNet model for all
LNL methods (e.g., special treatment of DivideMix, ELR, and SOP), one cannot directly
compare the entries on the benchmark. This is an issue as their results are currently
published on a public leaderboard4, making users unfamiliar with the testing methodology believe that the results are directly comparable between the entries. To ensure
a fair comparison with state‐of‐the‐art methods we also include two newer methods:
ProMix[24] and DISC [32].

To address these flaws, we adapt the benchmarking procedure as follows. We use the
official hyperparameters for each LNL method and fix only the underlying classifier.
We use the PyTorch implementation of ResNet‐34 with random weight initialization. Instead of testing every epoch, we use 5% of the noisy training data as a validation set to
compute accuracy. We report the accuracy on the clean test set corresponding to the
checkpoint with the highest validation accuracy. We present our argument on why accuracy on noisy data is a good metric for model selection in Appendix B. We repeat each
run three times and report the average accuracy along with the standard deviation.

### 3.6 Experimental Setup and Code

We implement our framework using PyTorch5 and Lightning [33] for easier reproducibility, distributed training, and robust, identical testing of all methods. The modularity of
the framework enables easier implementation and comparison of future LNL methods.
The code is publicly available at (https://github.com/KlemenVovk/noisy-labels).

## 4 Results

In this section, we describe the results obtained using the previously specified methodology. Each subsection corresponds to one of the reproducibility claims outlined in
Section 2.

4https://paperswithcode.com/task/learning-with-noisy-labels
5https://pytorch.org




### 4.1 Reproduced Noise Hypothesis Testing

We confirm the original claim that human‐noisy labels in CIFAR‐N differ from synthetic
ones obtained from the same transition matrix. We do not match the reported p‐value
entirely, ours being higher at 9.5 · 10−28 versus 1.8 · 10−36, reported by the original authors. Qualitatively, the differences between the human and synthetic cluster transition
vectors in Figure 4 are also not as prominent as in the original work. However, they still
exhibit a similar pattern, with human noise varying more along the cluster dimension,
which implies feature dependence. We attribute the differences to possibly different
training regimes, since the original one is not described in full detail.

(a) Human noise (Random 1): noise level ≈ 17.23%.

(b) Synthetic class‐dependent noise with the same T.

Figure 4. Transition vectors within ν = 5 clusters for the first 5 classes for real‐world human
noise and corresponding synthetic noise. Qualitatively, human noise shows a greater diversity of
transition vectors between the clusters in each class. We use the Euclidean distance for k‐means
clustering on ℓ2‐normalized embeddings, which is proportional to the negative cosine similarity
used by the authors.

### 4.2 Reproduced Noise Memorization

Our reimplementation of the noise memorization experiments also supports the claims
of [21]. Figure 5 presents the memorization dynamics across three label sets with increasing noise levels. The full lines lying above the dashed ones indicate that models begin memorizing real‐world noisy labels more rapidly than synthetic ones. While
the effect is less pronounced than in Figure 6 of [21], our results consistently demonstrate that models overfit human‐labeled noise faster than synthetic noise, especially
under higher noise levels (Worst label). Notably, the memorization of real‐world noise
remains somewhat consistent across noise levels, while synthetic labels are memorized
with a higher frequency at lower noise levels. The observed discrepancies can again be
attributed to differences in training configurations, as certain implementation details
were either missing from the original paper or remained unclear despite our correspondence with the authors. We perform additional experiments using different types of
synthetic noise and SGD parameters in Appendix C. While the memorization dynamics
differ under different synthetic noises and hyperparameters, the observations of the
original authors hold: deep neural nets memorize features more easily when learning
with real‐world human annotations than synthetic ones.

### 4.3 Reproduced Benchmark

Table 1 shows the results obtained using the evaluation methodology described in [21]
on the Aggregate label set. There are significant differences between the results reported
in the original paper and those obtained when following the methodology fully (fixing
the same optimizer, learning rate schedule, and number of epochs for all methods).


1234567891012345class: 1 (airplane)1234567891012345class: 2 (automobile)1234567891012345class: 3 (bird)1234567891012345class: 4 (cat)1234567891012345class: 5 (deer)01cluster1234567891012345class: 1 (airplane)1234567891012345class: 2 (automobile)1234567891012345class: 3 (bird)1234567891012345class: 4 (cat)1234567891012345class: 5 (deer)01cluster

Figure 5. Noise memorization effects. The red line denotes the proportion of memorized (wrongly
labeled) samples, and the blue line denotes that of correctly annotated ones. The models start to
memorize the human noisy labels (full line) faster than the synthetic ones (dashed line).

Table 1. Comparison with the reported results on the Aggregate label. We report the results
(accuracy±std) obtained using our reimplementation of the configuration described by the authors, the original configuration for each method, and the reported results. Only the results for
which the authors use original configurations (denoted by

) are close to the reported ones.

∗


Described Config

Original Config

Reported

CE


ELR∗
ELR+∗
DivideMix∗

CAL

SOP+

91.70±0.07
90.25±0.13
86.20±0.88
93.00±0.19
95.32±0.06
95.62±0.09
84.02±6.61
91.76±0.22
91.53±0.44
93.17±0.66

91.70±0.07
91.93±0.25
91.15±0.08
93.00±0.19
95.32±0.06
95.62±0.09
90.47±0.17
91.84±0.23
94.64±0.05
96.04±0.15

87.77±0.38
91.20±0.13
90.61±0.22
92.38±0.64
94.83±0.10
95.01±0.71
89.70±0.21
91.97±0.32
94.66±0.18
95.61±0.13

Upon further investigation, we repeat the experiments using the methods’ original configurations. The results are closer to those reported by [21].
We reproduce the authors’ results on the CIFAR‐N dataset using the configurations specific to each evaluated method. We compare our results with those reported by [21]
(Tables 2 and 8). Table 2 shows the results of the reimplemented methods for all label
sets in CIFAR‐N.

Table 2. Results based on the original methods’ configurations. Results for most of the methods
match those reported in the original work. We report the average best test set accuracy and standard deviation of three runs.

*


CE


ELR
ELR+


CAL

SOP+
SOP

Clean

Aggregate

Random 1

Random 2

Random 3

Worst

Clean

Noisy


94.21±0.12
92.15±0.11
92.90±0.22
93.97±0.12
95.81±0.16
95.51±0.00
92.71±0.02
93.78±0.18
94.75±0.16
96.53±0.05
93.76±0.26

91.70±0.07
91.93±0.25
91.15±0.08
93.00±0.19
95.32±0.06
95.62±0.09
90.47±0.17
91.84±0.23
94.64±0.05
96.04±0.15
91.69±0.76

90.20±0.04
90.69±0.07
89.82±0.13
92.20±0.10
94.89±0.11
95.72±0.11
88.90±0.51
91.10±0.26
95.20±0.08
95.70±0.07
89.83±0.24

90.12±0.13
90.51±0.14
89.64±0.19
92.05±0.12
94.88±0.08
95.78±0.10
88.81±0.17
90.60±0.10
95.26±0.13
95.62±0.18
90.57±0.46

90.08±0.05
90.56±0.22
89.77±0.26
92.18±0.17
94.93±0.07
95.71±0.09
88.67±0.10
90.61±0.12
95.20±0.11
95.75±0.14
90.88±0.15

83.91±0.08
80.92±0.43
82.36±0.04
87.89±0.14
91.75±0.06
93.10±0.10
80.87±0.25
84.82±0.23
92.58±0.05
92.89±0.09
83.66±0.64

76.23±0.19
72.24±0.44
70.39±0.45
75.64±0.21
78.82±0.24
78.22±0.06
72.73±0.65
74.53±0.21
77.77±0.33
77.90±0.29
72.97±1.15

61.19±0.51
54.48±0.27
55.46±0.34
63.72±0.38
67.87±0.07
70.91±0.09
58.30±0.05
60.13±0.33
70.32±0.28
63.88±0.32
56.17±1.02

For most of the methods, we are able to reproduce the results reported by the authors.
One notable difference is that the baseline CE method performs much better in our


0501001500.000.250.500.751.00Clean labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Clean labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Clean labels (Worst)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Worst)RealSyntheticEpochFraction of memorized samples

experiments. The discrepancy between our and the reported baseline results is investigated in Appendix A. Some methods use noise rate as an input parameter [14, 15, 27].
The parameter is fixed to the default value obtained from the original implementations.
The justification for such a decision is that one does not always know how many labels
are noisy in a real‐world scenario. This way, the experimental protocol remains consistent, and the comparison is fair to all the methods. The decision to fix the noise level
parameter could explain the difference in the Co‐teaching(+) methods’ performance on
the CIFAR‐100N noisy label set. Similarly, in the case of SOP(+) methods, symmetric
noise type was assumed as an input parameter, which might explain the gap in performance on CIFAR‐100N.

Human Noise vs. Synthetic Noise — Following the protocol described by the original authors,
we rerun the experiment with synthetic noisy labels and compare the differences in accuracy for each entry. We subtract the real accuracies from the newly obtained synthetic
ones and report the difference in Table 3.

Table 3. Differences between the real‐world and synthetic test accuracies: accsyn−accreal. Negative
gaps representing the method performed better when training on human noise are highlighted in
red. For CIFAR‐10N, most of the methods perform better on synthetic noise, indicating a harder
learning task when learning from human‐assigned labels. For CIFAR‐100N, this is not the case.
We report the expected difference in best test set accuracy and standard deviation.


CE


ELR
ELR+
DivideMix∗

CAL

SOP+
SOP

Aggregate

Random 1


Random 2

Random 3

Worst

0.93±0.39
0.46±0.08
1.24±0.14
0.31±0.18
0.31±0.13
0.47±0.12
1.15±0.51

3.06±0.21
1.01±0.26
0.71±0.10
1.40±0.85
0.09±0.15
0.89±0.27
2.92±0.31
1.12±0.19
1.05±0.16
−3.82±0.91
0.50±0.13
0.12±0.21
−0.66±2.48
0.32±0.08
0.20±0.08
1.94±0.11
0.54±0.10
0.56±0.10
3.68±0.67
1.14±0.18
0.89±0.17
−0.09±0.37 −0.76±0.31 −0.23±0.36 −0.25±0.19 −0.34±0.23
1.71±0.26
0.41±0.23
0.29±0.30
2.07±0.09
0.48±0.18
0.25±0.16
2.73±1.29
0.17±0.46
0.70±0.99

1.10±0.05
0.34±0.23
1.19±0.34
0.31±0.18
0.33±0.08
0.44±0.11
1.41±0.11

0.39±0.11
0.45±0.15
0.86±0.29

0.31±0.10
0.38±0.08
1.20±0.83


Noisy

1.89±0.51
−2.26±0.36
−1.94±1.10
−0.71±0.49
−0.28±0.10
1.08±0.48
3.11±0.15
−0.57±0.33
0.09±0.77
0.89±0.36
2.44±1.02

We can see that, for the most part, LNL methods perform better on synthetic data. This
is at least the case for CIFAR‐10N, while for CIFAR‐100N, the results are evenly split, with
5 methods performing better and 5 methods performing worse. This matches observations reported in [21], indicating that learning on real‐world noise is more difficult to
handle.

### 4.4 Fair LNL Benchmark

We now report the performance of the methods when using our benchmark as described
in Section 3.5. In our evaluation, we separate the methods that train two classifiers to
make a fairer comparison. In this case, we follow the original implementations and use
both models and average their final predictions when calculating the accuracies. The
results are summarized in Table 4. We report the test set accuracy on the clean test for
the checkpoint that achieved the highest accuracy on the noisy validation set. A similar
approach to be used in practice was suggested by [4]. For details on our choice, please
refer to Appendix B.

Looking at the results in Table 4, we first observe that all methods perform worse than
in Table 2. This is because we use the PyTorch ResNet‐34 implementation here instead
of the modified one used by the authors (more on that in Appendix F). Otherwise, the
model ranking remains similar, with DivideMix [27] and SOP+ [30] performing best from




the methods used in the original work. The state‐of‐the‐art method ProMix consistently
outperforms all methods on CIFAR‐10N. However, on CIFAR‐100N, DivideMix retains
the top ranking. Among the methods that use a single model, SOP+ outperforms the
newer DISC method on CIFAR‐10N, while the latter achieves the best performance on
CIFAR‐100N. We still observe that baseline CE training performs better than previously
reported, consistently beating CAL [29], VolMinNet [28], and SOP [30].

Table 4. Fair LNL Benchmark. To ensure a fair comparison, all methods utilize a ResNet‐34 backbone and are evaluated using their original hyperparameter configurations. We report the test
accuracy for the model checkpoint that achieves the highest validation accuracy on noisy labels.
Since some methods train two classification models, we identify the best‐performing method
within each group (underlined) and the overall best‐performing method (bolded). The top group
utilizes a single model, and the bottom group two. For all methods, we report the mean and standard deviation across three runs.

*


CE
ELR+

CAL

SOP
SOP+
DISC


ELR+

ProMix

Clean

Aggregate

Random 1

Random 2

Random 3

Worst

Clean

Noisy


85.50±0.25
88.56±0.23
82.57±0.20
83.38±0.47
87.08±0.08
82.12±0.43
90.09±0.03
89.12±0.12

86.56±0.08
86.59±0.12
88.56±0.23
89.59±0.12
91.53±0.26

83.50±0.23
87.76±0.16
80.42±0.36
81.51±0.21
86.62±0.23
79.78±0.85
89.50±0.11
88.12±0.24

86.56±0.27
85.16±0.32
87.76±0.16
89.36±0.22
90.72±0.14

81.96±0.77
86.75±0.15
79.18±0.10
79.64±0.45
87.63±0.11
79.22±0.57
88.82±0.43
87.31±0.28

85.26±0.15
83.71±0.28
86.75±0.15
89.34±0.10
90.57±0.20

82.00±0.13
86.94±0.07
78.54±0.30
79.50±0.31
87.47±0.20
79.37±0.29
88.99±0.16
87.55±0.25

85.11±0.27
84.20±0.21
86.94±0.07
89.61±0.10
90.61±0.13

82.19±0.31
86.97±0.07
78.56±0.13
79.67±0.26
86.80±0.66
78.66±0.57
88.72±0.19
87.44±0.33

84.56±0.22
83.92±0.15
86.97±0.07
89.28±0.31
90.61±0.25

75.48±0.30
81.50±0.12
72.07±0.49
73.08±0.88
84.12±0.34
71.76±1.98
85.18±0.59
83.04±0.13

75.62±0.32
76.71±0.50
81.50±0.12
86.82±0.17
88.99±0.14

59.18±0.18
61.80±0.25
51.27±0.18
58.02±0.17
60.51±0.14
52.61±0.43
61.27±0.39
62.13±0.37

57.07±0.16
54.76±0.58
61.80±0.25
64.21±0.02
63.53±0.03

49.51±0.39
52.91±0.27
42.39±0.74
47.37±0.49
52.95±0.47
40.98±0.28
50.85±0.06
53.09±0.47

43.26±0.43
44.25±0.34
52.91±0.27
56.21±0.38
55.67±0.10

## 5 Discussion

We managed to reproduce the hypothesis testing and noise memorization effects. Due
to a partially unclear description of the experiment protocol, we do not obtain the same
results as the authors, but the results nevertheless lead to the same conclusions. The
real‐world label noise is indeed different from its synthetic counterpart, and the classifiers start to overfit on it faster, which indicates a harder learning task.
While the authors describe the benchmarking experiment in some detail, we fail to
reach the same results using their methodology. Instead, when we use the original
hyperparameter configurations for each LNL method, we obtain results closer to the
reported accuracy for most of the methods. Perhaps most interesting is that the baseline cross‐entropy training performs significantly better than expected, outperforming
several methods designed explicitly for LNL scenarios even in the most difficult noise
settings. This behavior also persists outside our framework, even in the original code
provided by the authors, as we show in Appendix A. This finding leaves an avenue for
possible future work. We provide additional comments on reproducibility and our correspondence with the authors in Appendix D.

### 5.1 Additional Observations

During our implementation of several LNL methods, we noticed that the original implementations incorrectly generate synthetic noise. This raises the question of their reported performances. The symmetric noise produced by the official DivideMix [27] implementation6 uses a biased noise rate. For a given noise rate r, their implementation

6https://github.com/LiJunnan1992/DivideMix/blob/39740b267147466bac0779de91d969909ab3b65f/dataloader_cifar.py#

L58-L74




randomly selects a fraction r of clean labels. The noisy labels are sampled uniformly
from all classes k. This results in 1
k of the samples agreeing with the original label, resulting in the actual noise rate being er = r − 1
k r instead of r. This is especially evident in
high‐noise scenarios where DivideMix performs best. We observe an even bigger error
in the ELR [26] implementation of synthetic noise. The method uses two models trained
on separate datasets, which are both noised independently, while also producing noisy
labels with a decreased noise rate er7 described above. Here, without loss of generality,
we treat the sample as noisy and as having the wrong label in the first dataset. This
results in the probability of at least one of the models observing the correct label for a
sample given that the sample is noisy, being 1 − er instead of 0.

This brings into question the results reported in the respective original works. However, for our benchmark reproduction, where human noise is used and synthetic noise
pipelines are unified, the results are unaffected, and both methods rank among the topperforming ones.

### 5.2 Conclusion

This reproducibility study examined the claims made by [21] regarding real‐world label noise. We successfully replicated the original noise structure hypothesis testing
and noise memorization experiments with minor quantitative discrepancies likely stemming from undisclosed training details. Despite these discrepancies, our results support the authors’ claim that learning on datasets with real‐world noisy labels is more
challenging than with synthetic noise. However, our attempts to reproduce the benchmark results revealed significant deviations. Through a detailed review and reverse
engineering of the original codebase, we identified inconsistencies in the paper’s description, particularly regarding hyperparameter configurations. We then developed a
unified framework for LNL methods, accompanied by an improved benchmarking procedure, incorporating a validation set on noisy data and consistent use of the ResNet‐34
architecture. This framework provides a more robust platform for evaluating LNL methods, especially in scenarios where clean validation data is unavailable. Our findings
highlight the need for comprehensive documentation and transparency in scientific research to ensure reproducibility and foster progress in the field.

References

1.

2.

3.

4.

5.

6.

7.

8.

D. F. Nettleton, A. Orriols-Puig, and A. Fornells. “A study of the effect of different types of noise on the precision
of supervised learning techniques.” In: Artificial intelligence review 33 (2010), pp. 275–306.
C. Zhang, S. Bengio, M. Hardt, B. Recht, and O. Vinyals. “Understanding deep learning requires rethinking gen-
eralization.” In: International Conference on Learning Representations. 2017.
Z. Xie, F. He, S. Fu, I. Sato, D. Tao, and M. Sugiyama. “Artificial neural variability for deep learning: On overfitting,
noise memorization, and catastrophic forgetting.” In: Neural computation 33.8 (2021), pp. 2163–2192.
L. Jiang, D. Huang, M. Liu, and W. Yang. “Beyond synthetic noise: Deep learning on controlled noisy labels.” In:
International conference on machine learning. PMLR. 2020, pp. 4804–4815.
K. He, X. Zhang, S. Ren, and J. Sun. “Deep residual learning for image recognition.” In: Proceedings of the IEEE
conference on computer vision and pattern recognition. 2016, pp. 770–778.
A. Ghosh, H. Kumar, and P. S. Sastry. “Robust loss functions under label noise for deep neural networks.” In:
Proceedings of the AAAI conference on artificial intelligence. Vol. 31. 2017.
Z. Zhang and M. Sabuncu. “Generalized cross entropy loss for training deep neural networks with noisy labels.”
In: Advances in neural information processing systems 31 (2018).
Y. Wang, X. Ma, Z. Chen, Y. Luo, J. Yi, and J. Bailey. “Symmetric cross entropy for robust learning with noisy
labels.” In: Proceedings of the IEEE/CVF international conference on computer vision. 2019, pp. 322–330.

7https://github.com/shengliu66/ELR/blob/909687a4621b742cb5b8b44872d5bc6fce38bdd3/ELR/data_loader/cifar10.py#

L73-L80




9. M. Lukasik, S. Bhojanapalli, A. Menon, and S. Kumar. “Does label smoothing mitigate label noise?” In: Interna-

10.

tional Conference on Machine Learning. PMLR. 2020, pp. 6448–6458.
J. Wei, H. Liu, T. Liu, G. Niu, M. Sugiyama, and Y. Liu. “To Smooth or Not? When Label Smoothing Meets Noisy
Labels.” In: International Conference on Machine Learning. PMLR. 2022, pp. 23589–23614.

12.

13.

11. G. Patrini, A. Rozza, A. Krishna Menon, R. Nock, and L. Qu. “Making deep neural networks robust to label
noise: A loss correction approach.” In: Proceedings of the IEEE conference on computer vision and pattern
recognition. 2017, pp. 1944–1952.
X. Xia, T. Liu, N. Wang, B. Han, C. Gong, G. Niu, and M. Sugiyama. “Are anchor points really indispensable in
label-noise learning?” In: Advances in neural information processing systems 32 (2019).
S. Reed, H. Lee, D. Anguelov, C. Szegedy, D. Erhan, and A. Rabinovich. Training Deep Neural Networks on Noisy
Labels with Bootstrapping. 2015. arXiv:1412.6596 [cs.CV].
B. Han, Q. Yao, X. Yu, G. Niu, M. Xu, W. Hu, I. Tsang, and M. Sugiyama. “Co-teaching: Robust training of deep
neural networks with extremely noisy labels.” In: Advances in neural information processing systems 31
(2018).
X. Yu, B. Han, J. Yao, G. Niu, I. Tsang, and M. Sugiyama. “How does disagreement help generalization against
label corruption?” In: International conference on machine learning. PMLR. 2019, pp. 7164–7173.

14.

15.

17.

16. H. Wei, L. Feng, X. Chen, and B. An. “Combating noisy labels by agreement: A joint training method with co-
regularization.” In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition.
2020, pp. 13726–13735.
J. Goldberger and E. Ben-Reuven. “Training deep neural-networks using a noise adaptation layer.” In: Interna-
tional Conference on Learning Representations. 2017.
Y. Bai, E. Yang, B. Han, Y. Yang, J. Li, Y. Mao, G. Niu, and T. Liu. “Understanding and improving early stopping for
learning with noisy labels.” In: Advances in Neural Information Processing Systems 34 (2021), pp. 24392–
24403.

18.

20.

21.

19. H. Song, M. Kim, D. Park, Y. Shin, and J.-G. Lee. “Learning from noisy labels with deep neural networks: A
survey.” In: IEEE transactions on neural networks and learning systems 34.11 (2022), pp. 8135–8153.
P. Chen, J. Ye, G. Chen, J. Zhao, and P.-A. Heng. “Beyond class-conditional assumption: A primary attempt to
combat instance-dependent label noise.” In: Proceedings of the AAAI Conference on Artificial Intelligence.
Vol. 35. 2021, pp. 11442–11450.
J. Wei, Z. Zhu, H. Cheng, T. Liu, G. Niu, and Y. Liu. “Learning with Noisy Labels Revisited: A Study Using Real-
World Human Annotations.” In: International Conference on Learning Representations. 2022.
A. Krizhevsky, G. Hinton, et al. Learning multiple layers of features from tiny images. 2009.

22.
23. H. Chen, A. Shah, J. Wang, R. Tao, Y. Wang, X. Li, X. Xie, M. Sugiyama, R. Singh, and B. Raj. “Imprecise label
learning: A unified framework for learning with various imprecise label configurations.” In: Advances in Neural
Information Processing Systems 37 (2024), pp. 59621–59654.
R. Xiao, Y. Dong, H. Wang, L. Feng, R. Wu, G. Chen, and J. Zhao. “ProMix: combating label noise via maximiz-
ing clean sample utility.” In: Proceedings of the Thirty-Second International Joint Conference on Artificial
Intelligence. 2023, pp. 4442–4450.

24.

25. Q. Zhang, Y. Zhu, F. R. Cordeiro, and Q. Chen. “PSSCL: A progressive sample selection framework with con-

26.

27.

28.

29.

30.

trastive loss designed for noisy labels.” In: Pattern Recognition 161 (2025), p. 111284.
S. Liu, J. Niles-Weed, N. Razavian, and C. Fernandez-Granda. “Early-learning regularization prevents memoriza-
tion of noisy labels.” In: Advances in neural information processing systems 33 (2020), pp. 20331–20342.
J. Li, R. Socher, and S. C. Hoi. “DivideMix: Learning with Noisy Labels as Semi-supervised Learning.” In: Inter-
national Conference on Learning Representations. 2020.
X. Li, T. Liu, B. Han, G. Niu, and M. Sugiyama. “Provably end-to-end label-noise learning without anchor points.”
In: International conference on machine learning. PMLR. 2021, pp. 6403–6413.
Z. Zhu, Y. Song, and Y. Liu. “Clusterability as an alternative to anchor points when learning with noisy labels.”
In: International Conference on Machine Learning. PMLR. 2021, pp. 12912–12923.
S. Liu, Z. Zhu, Q. Qu, and C. You. “Robust Training under Label Noise by Over-parameterization.” In: Proceedings
of the 39th International Conference on Machine Learning. Ed. by K. Chaudhuri, S. Jegelka, L. Song, C. Szepes-
vari, G. Niu, and S. Sabato. Vol. 162. Proceedings of Machine Learning Research. PMLR, 2022, pp. 14153–
14172.

31. G. C. Cawley and N. L. Talbot. “On over-fitting in model selection and subsequent selection bias in performance

32.

evaluation.” In: The Journal of Machine Learning Research 11 (2010), pp. 2079–2107.
Y. Li, H. Han, S. Shan, and X. Chen. “Disc: Learning from noisy labels via dynamic instance-specific selection
and correction.” In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition.
2023, pp. 24070–24079.

33. W. Falcon and The PyTorch Lightning team. PyTorch Lightning. Version 1.4. Mar. 2019. DOI: 10.5281/zen-

odo.3828935. URL: https://github.com/Lightning-AI/lightning.




34.

J. Wei and Y. Liu. “When Optimizing f -Divergence is Robust with Label Noise.” In: International Conference
on Learning Representations. 2021.

35. M. G. Kendall. “A New Measure of Rank Correlation.” In: Biometrika 30.1/2 (1938), pp. 81–93. (Visited on

36.

37.

02/14/2025).
S. Yuan, L. Feng, and T. Liu. “Early Stopping Against Label Noise Without Validation Data.” In: The Twelfth
International Conference on Learning Representations. 2024.
K. He, X. Zhang, S. Ren, and J. Sun. “Identity mappings in deep residual networks.” In: Computer Vision–ECCV
2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part
IV 14. Springer. 2016, pp. 630–645.

A Baseline Performance Results

The largest discrepancy between our and the authors’ results comes from the baseline
(CE) training. [21], do not describe the exact procedure for obtaining their results. In our
correspondence (see Appendix D.1), they clarify that they used the best test set performance and report the mean and standard deviation across five random seeds. This procedure results in a discrepancy between our reproduced results and the ones reported
in the original work [21]. We visualize the discrepancy in Figure 6.

We can see that the accuracy of the best checkpoint in our experiments is higher than
their reported performance across all runs. We were not alone in noticing this discrepancy, as at the time of investigation, there were two open issues on the authors’ official
Github repository with the same question. Authors of the issues report the last obtained
accuracies on the Worst label set:≈ 68% 8 and ≈ 67% 9, which are also in line with our
last epoch accuracy (68 ± 0.88).

B Argument For Using Accuracy On Noisy Data

Since testing every epoch and reporting the highest result overestimates performance
and is thus considered a bad practice, we have to find an alternative. We want to use
the established train‐validation‐test split in this case. The first problem in LNL setting
arises when we need to decide whether the validation set is noisy or not, since practices
for this are not yet established in the field. Given the nature of the task, we argue that
the validation set should be noisy as well [4]. If one has non‐noisy data, one can train on
it, implicitly changing the noise ratio of the data. Additionally, some LNL methods [11,
34] use validation data to estimate parameters for loss functions that are later used to
train. If validation data were to be clean, there would be a direct data leak in such cases.

Consequently, we must decide on a proxy metric for the accuracy on clean data. We
consider two options: using validation losses of each LNL method or validation accuracy. Given that losses vary between the LNL methods (some have no upper bounds)
and are not as stable (see Figure 7), we propose to use accuracy on noisy validation
data for model selection. We propose this, as it remains stable across all tested methods
and strongly correlates with final test performance, preserving model ranking with high
probability.

We verify our claims empirically by testing how well our approach ranks the models in
comparison to the rankings of their best test set accuracies. For each method, we select
the best performance on the test data and the test performance corresponding to the
best validation checkpoint. We average the results across three runs and compute the
Kendall rank correlation coefficient [35] for method rankings. For all label sets we obtain

8https://github.com/UCSC-REAL/cifar-10-100n/issues/5
9https://github.com/UCSC-REAL/cifar-10-100n/issues/8




Figure 6. Differences between the authors’ reported (dotted) baseline performance and accuracy
obtained in reproduction (full blue) as well as using the original code (orange, red, green). The
performance obtained using a reimplemented framework perfectly aligns with the original code.
However, on all the noise labels, their reported accuracy does not coincide with the best accuracy
for any of the runs.

(a) Validation loss.

(b) Validation accuracy.

Figure 7. Validation performance on noisy labels from our benchmark implementations on the
Worst label set. Some methods may assign near‐zero probabilities to noisy labels, and due to the
unbounded nature of the cross‐entropy loss, this leads to high and unstable loss values (a). However, noisy validation accuracy remains stable across runs and serves as a reliable predictor of
clean test‐set performance (b).

statistically significant results, indicating a strong relationship between the ordering
based on noisy validation accuracy and clean test set performance. We report all the
orderings with their corresponding p‐value and Kendall‐τ statistics below, where we
underline all changes in rank:


020406080100405060708090100CleanOursStdOriginal (0)Original (42)Original (1337)Reported Best020406080100405060708090100AggregateOursStdOriginal (0)Original (42)Original (1337)Reported Best020406080100405060708090100Random 1OursStdOriginal (0)Original (42)Original (1337)Reported Best020406080100405060708090100Random 2OursStdOriginal (0)Original (42)Original (1337)Reported Best020406080100405060708090100Random 3OursStdOriginal (0)Original (42)Original (1337)Reported Best020406080100405060708090100WorstOursStdOriginal (0)Original (42)Original (1337)Reported BestEpochsTest Accuracy0255075100125150175200101Validation Loss300400ELRELR+SOPSOP+Co-teachingCo-teaching+PES (semi)DivideMix*CALVolMinNetCEEpochs0255075100125150175200102030405060Validation Accuracy300400ELRELR+SOPSOP+Co-teachingCo-teaching+PES (semi)DivideMix*CALVolMinNetCEEpochs

CIFAR 100 ‐ Clean (τ = 1.00, p = 5.01e − 08)

Val: DivideMix, ELR+, SOP+, PES semi, CE, ELR, CAL, Co‐Te., Co‐Te.+, SOP, 

Test: DivideMix, ELR+, SOP+, PES semi, CE, ELR, CAL, Co‐Te., Co‐Te.+, SOP, 

CIFAR 100N ‐ Noisy (τ = 1.00, p = 5.01e − 08)

Val: DivideMix, PES semi, ELR+, SOP+, CE, ELR, CAL, Co‐Te.+, Co‐Te., VolMinNet, SOP

Test: DivideMix, PES semi, ELR+, SOP+, CE, ELR, CAL, Co‐Te.+, Co‐Te., VolMinNet, SOP

CIFAR 10 ‐ Clean (τ = 1.0, p = 5.01e − 08)

Val: SOP+, DivideMix, ELR+, PES semi, Co‐Te.+, Co‐Te., CE, ELR, CAL, VolMinNet, SOP

Test: SOP+, DivideMix, ELR+, PES semi, Co‐Te.+, Co‐Te., CE, ELR, CAL, VolMinNet, SOP

CIFAR 10N ‐ Aggregate (τ = 0.82, p = 1.32e − 04)

Val: SOP+, DivideMix, ELR+, PES semi, Co‐Te, Co‐Te.+, ELR, CE, CAL, VolMinNet, SOP

Test: SOP+, DivideMix, ELR+, Co‐Te., PES semi, Co‐Te.+, ELR, CE, CAL, VolMinNet, SOP

CIFAR 10N ‐ Random 1 (τ = 0.6, p = 9.95e − 03)

Val: DivideMix, SOP+, PES semi, ELR+, Co‐Te., ELR, Co‐Te.+, CE, CAL, SOP, 

Test: DivideMix, SOP+, PES semi, ELR+, Co‐Te., Co‐Te.+, ELR, CE, CAL, SOP, 

CIFAR 10N ‐ Random 2 (τ = 1.0, p = 5.01e − 08)

Val: DivideMix, SOP+, PES semi, ELR+, Co‐Te., Co‐Te.+, ELR, CE, CAL, SOP, 

Test: DivideMix, SOP+, PES semi, ELR+, Co‐Te., Co‐Te.+, ELR, CE, CAL, SOP, 

CIFAR 10N ‐ Random 3 (τ = 0.64, p = 5.71e − 03)

Val: DivideMix, SOP+, ELR+, PES semi, Co‐Te., Co‐Te.+, ELR, CE, CAL, SOP, 

Test: DivideMix, SOP+, PES semi, ELR+, Co‐Te., Co‐Te.+, ELR, CE, CAL, VolMinNet, SOP

CIFAR 10N ‐ Worst (τ = 1.0, p = 5.01e − 08)

Val: DivideMix, SOP+, PES semi, ELR+, ELR, Co‐Te.+, Co‐Te., CE, CAL, VolMinNet, SOP

Test: DivideMix, SOP+, PES semi, ELR+, ELR, Co‐Te.+, Co‐Te., CE, CAL, VolMinNet, SOP

Yuan, Feng, and Liu[36] propose LabelWave, a model selection criterion for training with
noisy labels that eliminates the need for a validation set. We consider LabelWave a
promising alternative to our current model selection strategy based on noisy validation
accuracy. Benchmarking existing LNL methods using LabelWave as the selection criterion represents an interesting and valuable direction for future work.

C Additional Memorization Experiments

We extend the memorization experiments to include a broader range of synthetic noise
types and hyperparameter configurations. These experiments follow the procedure described in Section 3.3.
To evaluate the effect of different types of synthetic noise, we replace the asymmetric
transition matrix used in Section 4.2 with symmetric and pair‐flipping noise matrices.
The transition matrices are constructed following the definitions in [14], and the overall
noise rate ρ is estimated from the corresponding real‐world noisy labels.

For symmetric noise, we set the diagonal elements of the transition matrix to 1 − ρ and
all off‐diagonal elements to ρ
C−1 , where C is the number of classes. For pair‐flipping
noise, we again set the diagonal entries to 1 − ρ, and assign the entire off‐diagonal mass
ρ to the most common transition class observed in the real‐world noise.




We present the results in Figure 8. While synthetic noise types lead to varying memorization behaviors, we observe that the models still overfit human noisy labels faster
than synthetic ones.

(a)

(b)

Figure 8. Effects of different types of synthetic noise on memorization. (a) Pair‐flipping noise constructed based on the most common transitions observed in human‐labeled data. (b) Symmetric
noise applied uniformly across all incorrect classes. In both cases, models begin to memorize
human‐labeled noise earlier than synthetic noise, despite different memorization dynamics.

We also investigate how different training hyperparameters influence memorization dynamics. Building on the setup described in Section 3.3, we vary one hyperparameter at
a time while keeping the others fixed.

In the first experiment, we replace the exponential learning rate decay with a step decay,
reducing the learning rate by a factor of γ = 0.1 at epoch 50. In the second experiment,
we increase the initial learning rate to 0.1. In the third, we raise the weight decay to
5e − 4.

The results, shown in Figure 9, indicate that while these hyperparameter changes do
affect memorization behavior, the model still consistently memorizes real‐world human label noise faster than synthetic noise. This further supports our conclusion that
human‐labeled, instance‐dependent noise is inherently more susceptible to early memorization than instance‐independent synthetic noise.


0501001500.000.250.500.751.00Clean labels (Aggregate)RealPairflip0501001500.000.250.500.751.00Clean labels (Random 1)RealPairflip0501001500.000.250.500.751.00Clean labels (Worst)RealPairflip0501001500.000.250.500.751.00Wrong labels (Aggregate)RealPairflip0501001500.000.250.500.751.00Wrong labels (Random 1)RealPairflip0501001500.000.250.500.751.00Wrong labels (Worst)RealPairflipEpochFraction of memorized samples0501001500.000.250.500.751.00Clean labels (Aggregate)RealSymmetric0501001500.000.250.500.751.00Clean labels (Random 1)RealSymmetric0501001500.000.250.500.751.00Clean labels (Worst)RealSymmetric0501001500.000.250.500.751.00Wrong labels (Aggregate)RealSymmetric0501001500.000.250.500.751.00Wrong labels (Random 1)RealSymmetric0501001500.000.250.500.751.00Wrong labels (Worst)RealSymmetricEpochFraction of memorized samples

(a) Step learning rate scheduler with a decay at epoch 50.

(b) Lower initial learning rate set to 0.1.

(c) Increased weight decay set to 5e − 4.

Figure 9. Effect of hyperparameters on memorization. We observe different memorization dynamics across hyperparameter setups. However, models consistently memorize human‐labeled noise
earlier than synthetic noise

D Comments on Reproducibility

In this section, we document our efforts to reproduce the key experiments by [21], highlighting both successes and challenges. Table 5 summarizes the classification of reproducibility outcomes, indicating where discrepancies arose. We also detail our communication with the original authors, the aspects of the reproduction process that were
straightforward, and the challenges we faced, particularly regarding undocumented hyperparameters, inconsistent training protocols, and unclear benchmarking procedures.


0501001500.000.250.500.751.00Clean labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Clean labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Clean labels (Worst)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Worst)RealSyntheticEpochFraction of memorized samples0501001500.000.250.500.751.00Clean labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Clean labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Clean labels (Worst)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Worst)RealSyntheticEpochFraction of memorized samples0501001500.000.250.500.751.00Clean labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Clean labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Clean labels (Worst)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Aggregate)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Random 1)RealSynthetic0501001500.000.250.500.751.00Wrong labels (Worst)RealSyntheticEpochFraction of memorized samples

Table 5. Classification of reproducibility results.

Experiment

Discrepancy

Result

Noise hypothesis testing
Memorization effects
Baseline performance
LNL Benchmark

Missing details in experimental setup.
Missing details in experimental setup.
Difference in reported vs. observed results.
Ambiguities in paper descriptions.

Reproduced
Reproduced
Different
Reimplemented

D.1 Communication with Original Authors

We contacted the authors two times during our implementation effort. The first time,
we inquired about several inconsistencies between the paper and the provided code.
We also asked about the hyperparameter selection protocol, which backbone models
were used, which checkpoints were selected, and some general evaluation and methodspecific questions. The authors responded with a short email, answering some of our
questions but avoiding our questions about inconsistencies.

After some time, we contacted the authors for the second time. We inquired how the
validation sets were handled, as some methods could not be properly trained without
them. We also asked about the specifics of the hypothesis testing setup and the differences between the original and our reproduced results. This time, the authors did not
respond.

D.2 What was easy

Using the baseline code and the datasets provided by the benchmark authors was easy
and only required minimal tweaking to run. Running most of the LNL strategies’ repositories was also straightforward, as most authors include instructions for basic use cases
and experiment reproduction in the source code repository.

D.3 What was difficult

Throughout the reproduction attempt, we encountered several problems, most of them
stemming from unclear and ambiguous descriptions of the benchmark. Many evaluated methods rely on algorithm‐specific hyperparameters, which the authors did not
list. Therefore, an effort was made to try to recover them by experimentally trying out
different combinations in an attempt to match the reported results. The learning rate
schedule for all methods was said to follow a multi‐step schedule with a single decay at
the 50th epoch. In the original source code, the switch happens at the 60th epoch.
Several LNL methods use different warm‐up training techniques. Some fully reset the
model, while others use the warm‐up epochs to find a set of weights that perform best
on the validation set and later continue the training from the pre‐trained checkpoint.
A shared checkpoint was supposed to be used for the benchmark. However, the paper
does not mention how such a checkpoint was obtained. After communication with the
authors, they clarified that the warmup checkpoint was obtained by training the model
with cross‐entropy loss for 200 epochs.

E Computational Requirements

We run all our experiments on a system with 8 Nvidia Titan X Pascal GPUs running
Ubuntu 20.04.2 LTS and CUDA version 12.2. With this setup, it takes approximately 1.5
GPU hours to reproduce the noise hypothesis testing experiment and approximately 27
GPU hours to reproduce the noise memorization experiment. Reproducing benchmark
results on the selected subset of the LNL methods takes approximately 52.5 GPU hours




per label set; we present a breakdown of the training times in Table 6. It takes approximately 2, 000 GPU hours to reproduce our results fully (eight label sets, each with three
repeats, and six synthetic runs with two repeats).

Table 6. Runtimes of the 10 selected methods, for a single repeat of a single noise label.


Runtime (h)

CE
Co‐teaching (+)
ELR
ELR+


CAL

SOP+
SOP
total

1.5
5.6
1.8
7.9
14.0
1.3
1.5
12.2
5.5
1.2
52.5

F Hyperparameters

In this section, we report the hyperparameters for all the methods included in our reproduced evaluation to enable the replication of our results. Table 8 describes the hyperparameters of methods using the PreActResNet18 [37] backbone, and Table 9 for the
methods using the ResNet-34 [5] backbone. Here we note that most of the methods’ original implementations as well as the model implementation provided by the authors 10 use
ResNet implementations that use stride of 1 instead of 2 in the first layer, resulting in a
four times increase in activation volumes. The modified implementation also excludes
the first max pooling layer (see [5] Table 1), resulting in another four‐times increase in
activation volumes, for a total of 16 times bigger activation volumes. Modifying these
layers increases the baseline performance significantly (10% when comparing baselines
in Tables 2 and 4).

In our reproduction experiments, we use this version of ResNet since it was provided
in the author’s original repository. For our benchmark (Section 4.4) we use the same
hyperparameters as described in tables 9 and 8 with the exception of using the official
PyTorch implementation of ResNet 11. We report the parameters for newer methods not
used in the original benchmark: DISC and ProMix in Table 7.

10https://github.com/UCSC-REAL/cifar-10-100n/blob/main/models/resnet.py
11https://pytorch.org/vision/main/models/resnet.html




Table 7. Hyperparameters for newer methods.


Hyperparameter

CIFAR10N

CIFAR100N

DISC

ProMix


lr

SGD 


alpha
start_epoch
sigma

lambda_ce
lambda_h

lr


rampup_
noise_type
rho_start, rho_end
debias_beta_pl
alpha_output
tau
start_expand
threshold
bias_m
temperature 0.5
feat_dim

SGD
0.1
0.001


SGD
0.1
0.001


MultiStepLR ([80, 160], 0.1) MultiStepLR ([80, 160], 0.1)


5.0

0.5
0.99
1.0
1.0
SGD
0.05

0.9
CosineAnnealingLR


symmetric
(0.5, 0.5)
0.8
0.8
0.99

0.9
0.9999
0.5


5.0

0.5
0.99
1.0
1.0
SGD
0.05

0.9
CosineAnnealingLR


symmetric
(0.5, 0.5)
0.5
0.5
0.95

0.9
0.9999


Table 8. Hyperparameters for methods using PreActResNet18 backbone.


Hyperparameter

CIFAR10N


ELR+

SOP+


lr


alpha
noise_type
p_thresh
temperature
lambda_u


lr


beta
lmbd
alpha
gamma
ema_step
coef_step

lr


lr_u
lr_v
overparam_mean
overparam_std
ratio_balance
ratio_consistency

SGD
0.02

0.9
LambdaLR


asymmetric
0.5
0.5


SGD
0.02

0.9

CIFAR100N

SGD
0.02

0.9
LambdaLR


asymmetric
0.5
0.5


SGD
0.02

0.9

MultiStepLR ([150], 0.1) MultiStepLR ([200], 0.1)


0.7


0.997
40000

SGD
0.02

0.9


0.0
1e‐08
0.1
0.9


0.9


0.997
40000
40000
SGD
0.02

0.9


0.0
1e‐08
0.1
0.9




Table 9. Hyperparameters for methods using ResNet‐34 backbone.


Hyperparameter


CAL

CE


ELR


SOP


lr


alpha
alpha_

alpha_list_warmup
milestones_warmup
alpha_list
milestones

lr


lr


forget_rate
exponent
num_gradual
epoch_decay_start

lr


init_epoch
forget_rate
exponent
num_gradual
epoch_decay_start

lr


beta
lmbd

lr


PES_lr

T2
lambda_u
temperature
alpha

lr


lr_u
lr_v
overparam_mean
overparam_std
ratio_balance
ratio_consistency

lr


lam
init_t
optimizer_transition_mtx

SGD
0.1

0.9


0.0
seg

[0.0, 2.0]
[10, 40]
[0.0, 1.0, 1.0]
[10, 40, 80]
SGD
0.1

0.9


Adam
0.001


0.2


Adam
0.001


0.2


SGD
0.02
0.001
0.9


0.7

SGD
0.02

0.9


0.5

SGD
0.02

0.9
MultiStepLR ([40, 80], 0.1)


0.0
1e‐08
0.0
0.0
SGD
0.01

0.9
MultiStepLR ([30, 60], 0.1)


SGD

SGD
0.1

0.9


0.0
seg

[0.0, 1.0]
[10, 40]
[0.0, 1.0, 1.0]
[10, 40, 80]
SGD
0.1

0.9


Adam
0.001


0.2


Adam
0.001


0.2


SGD
0.02
0.001
0.9
MultiStepLR ([80, 120], 0.01)

0.9

SGD
0.02

0.9


0.5

SGD
0.02

0.9
MultiStepLR ([40, 80], 0.1)


0.0
1e‐08
0.0
0.0
SGD
0.01

0.9
MultiStepLR ([30, 60], 0.1)


Adam

---
**Source PDF:** `de332936b0f5.pdf` (2026_01_article.pdf)  
**URL:** https://zenodo.org/record/18401497/files/article.pdf
