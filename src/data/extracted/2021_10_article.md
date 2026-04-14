R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020


Toomas Liiv1,2, ID , Einar Lennelöv1,2, ID , and Aron Norén1,2, ID
1Equal contribution – 2KTH Royal Institute of Technology, Stockholm, Sweden

Edited by
Koustuv Sinha,
Jessica Zosa Forde

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4834516

Reproducibility Summary

Scope of Reproducibility

The authors claim that their proposed method is able to, given an ensemble of deep
neural networks, capture the uncertainty estimation and decomposition capabilities of
the ensemble into a single model. The authors also claim that this only results in a small
reduction in classification performance compared to the ensemble. We examine these
claims by reproducing most of the authorsʼ experiments on the CIFAR-10 dataset.

Methodology

The proposed method was re-implemented in tf.keras. The surrounding data pipelines,
pre-processing, and experimentation code were also re-implemented. As in the original
paper, the models were based on VGG-16 networks trained from scratch with random
initialization. Training and evaluation was done on two consumer-grade GPUs, for a
total of 273 hours.

Results

Our findings support the authorsʼ central claims. In terms of uncertainty estimation our
EnD2 achieved (99 ± 1) % of the AUC-ROC of our ensemble on the OOD-detection task.
The corresponding value in the original paper was (100 ± 1) %. In terms of classification
our EnD2 had (16 ± 1)% higher error than our ensemble. The corresponding values in
the original paper was (11 ± 6)%. Other metrics showed similar agreement, but, signifi-
cantly, in the OOD-detection task our EnD performed at least as well as our EnD2. This
is in stark contrast with the original paper.
We also took a novel approach to visualizing the uncertainty decomposition by plotting
the resulting distributions on a simplex, offering a visual explanation to some surprising
results in the original paper, while mostly supporting the authorsʼ intuitive justifications
for the model.

What was easy

The original paper features a thorough mathematical formulation of the method, aiding
conceptual understanding. The datasets used by the authors are publicly available. The


Code is available at https://github.com/lennelov/endd-reproduce. – SWH swh:1:dir:2c366708175b2ed7c83ce6b33a80dd43c8aad915.
Open peer review is available at https://openreview.net/forum?id=p1BXNUcTFsN.




use of the simpler datasets also meant that it was computationally feasible for us to re-
produce these results. The base model used is well known with several implementation
available, allowing us to focus on the novel aspects of the method.

What was difﬁcult

While the theoretical explanations of the method are excellent, we initially found it hard
to translate this into an implementation. Our difficulty was likely caused by our inex-
perience with the subject matter. Nonetheless, a pseudocode, such as the one we have
provided, would havee simplified the re-implementation. We were not able to reproduce
the results on some of the datasets due to limited computational resources.

Communication with original authors

We did not contact the original authors directly, but we did refer to a public GitHub and
blog post created by one of the authors. At the same time as submitting this report to
the ML Reproducibility Challenge 2020 we also sent a copy to the authors and asked for
their feedback.




## 1 Introduction

Uncertainty estimation can help to make deep learning safer and more usable by allow-
ing the model to identify cases it is not suitable to handle. There are different kinds
of uncertainty, however, and it is especially interesting to separate uncertainty caused
by ambiguities or contradictions in the data from the uncertainty that arises when a
model faces a situation it has not been trained for. Ensemble-based methods of uncer-
tainty estimation are capable of making this distinction but suffer from computational
requirements at the evaluation phase [1]. The authors of Ensemble Distribution Distillation
(EnD2) [2] address this issue by using the output of an ensemble to train a so-called Prior
Network (PN) [3], distilling the ensemble down to a single model while also preserving
its uncertainty decomposition abilities. This can be contrasted with regular ensemble
distillation models [4] (EnD), which are not able to decompose uncertainty. The repro-
duced paper was accepted to ICLR2020.

## 2 Scope of reproducibility

We consider the setting of using CIFAR10 [5] as an in-distribution dataset, and LSUN [6]
as an out-of-distribution dataset. Our supplementary material also examines the setting
of using a synthetic dataset in R2 for visualization.
The claims from the original article that this reproduction is testing are as follows:

1. Classification performance: In terms of error rate, prediction rejection rate, and
negative log-likelihood EnD2has worse performance than the ensemble, but simi-
lar performance to EnD and PriorNet, and better performance than the individual
model. In terms of expected calibration error, EnD2 has worse performance than
the ensemble, but better performance than the other methods. On CIFAR-10 in
particular, EnD2 has the best expected calibration error of all models. This claim
corresponds to Table 3 in the original paper.

2. Out-of-distribution detection performance: In terms of AUC-ROC on CIFAR-10 vs.
LSUN, EnD2 without auxiliary dataset performs worse than the ensemble and the
PriorNet, similar to the individual model, and better than EnD. With the auxiliary
dataset, however, EnD2 performs as well as the ensemble, almost as well as Pri-
orNet, and better than EnD. Using knowledge uncertainty as opposed to total un-
certainty on CIFAR-10 vs. LSUN does not yield an improved AUC-ROC. This claim
corresponds to Table 4 in the original paper.

3. Dependency on ensemble size: Using 20 models in the ensemble does better than
using 5 models, but there is no conclusive gain when using more than 20 models.

4. Dependency on temperature: It is necessary to use temperature of at least 5 to
successfully distribution-distill the ensemble. Using higher initial temperatures
do not result in conclusive improvement.

5. Uncertainty decomposition: EnD2 trained with an auxiliary dataset is able to re-

construct the uncertainty decomposition made possible by ensembles.

We reproduce all experiments of the main article and most of the appendix, except for
the use of CIFAR100 and Tiny Imagenet datasets. Some of these results can be found
in our supplementary material. From their appendix, we do not reproduce Table 7 in
appendix B. We did not recreate the OOD-detection plots when reproducing the ablation
study.




Table 1. Datasets used in the CIFAR-10 setting.

Dataset
CIFAR-10 train
CIFAR-100 train
CIFAR-10 test
LSUN test

Samples Classes Dimensions

50000
50000
10000
10000


32x32x3
32x32x3
32x32x3
256x256x3

Link
https://www.cs.toronto.edu/ kriz/cifar.html
https://www.cs.toronto.edu/ kriz/cifar.html
https://www.cs.toronto.edu/ kriz/cifar.html
https://www.yf.io/p/lsun

## 3 Methodology

### 3.1 Model description

We consider the same seven models as the original authors:

• IND: A single classification model.

• ENSM: An ensemble of independently trained IND models.

• EnD: A single model distilling ENSM trained according to [4].

• EnD2: A single model distribution-distilling ENSM trained according to [2].

• EnD+AUX: Like EnD, but trained with auxiliary data.

• EnD2

+AUX: Like EnD2, but trained with auxiliary data.

• PN+AUX: A PriorNet model with auxiliary data trained according to [3]

These models are all based on almost identical VGG16 architectures [7], adapted to CIFAR-
10 data as in [3] by adding dropout, batch normalization and reducing the size of the fully
connected layers. The only exception being that batch normalization is not used for PN.

### 3.2 Dataset

The training set of CIFAR-10 was used as the primary training dataset. The training set
of CIFAR-100 was used as an auxiliary dataset. For evaluating the classification task the
test set of CIFAR-10 was used. For evaluating the out-of-distribution detection task the
CIFAR-10 test set was used as in-domain dataset, while the LSUN test set was used as the
out-of-domain dataset. Information about the datasets is listed in Table 1.
Each image x was normalized according to x′ = x/127.5 − 1 where the operations are
elementwise, causing all values to lie in the range (-1, 1). The LSUN images were also
scaled down to 32x32. Furthermore, dataset augmentation was used for all models, con-
sisting of rotations with 15◦ range, horizontal flips, width and height shifts of up to 4
pixels in each direction, and using nearest-neighbour interpolation.

### 3.3 Hyperparameters

The models were trained with the hyperparameters listed in Table 2.

### 3.4 Experimental setup and code

Using these models and dataset we ran a number of experiments, as detailed below. The
full code is available on https://github.com/lennelov/endd-reproduce. Our implementa-
tion was made in TensorFlow Keras, as opposed to the original implementation which
was made in PyTorch.
Classification: The classification task was evaluated on the test set of CIFAR-10. We use
the same four metrics as in the original paper, ERR, PRR, ECE, and NLL. ERR is the mean




Table 2. Training parameters in the CIFAR-10 setting

Model

Epochs Cycle

DNN
EnD

EnD2
EnD2
PN

+AUX


η0
10−3
10−3
10−3
10−3
10−3
0.5 · 10−3

ηmax
10−2
10−2
10−2
10−2
10−2
0.5 · 10−2

ηmin
10−6
10−6
10−6
10−6
10−6
0.5 · 10−6

Dropout

0.5
0.7
0.7
0.7
0.7
0.7

T0

-
2.5
2.5


-

Anneal

AUX data

-
No
No
Yes
Yes
No

-
-
CIFAR-100
-
CIFAR-100
CIFAR-100

classification error. PRR is the prediction rejection area ratio introduced in Appendix B
of [2]. ECE is the expected calibration error1. Finally, NLL is the negative log-likelihood.
This experiment tests Claim 1.
Out-of-distribution detection: The OOD-detection task was evaluated with the CIFAR-10
test set as the in-domain set, and the LSUN test set as the out-of-domain set. The AUC-
ROC was computed both when total uncertainty and when only knowledge uncertainty
is used to make rejection decisions. This experiment tests Claim 2.
Ensemble size ablation study: Our examination of the effect of ensemble size goes slightly
beyond the original authors. We extend the error analysis to also consider the sensitiv-
ity of EnD2 to variations in the underlying ensemble. We began by training a set of 400
VGG16 models on CIFAR-10. Next, we sampled randomly from this set to create 4 differ-
ent sets, each consisting of 100 models.
For each N ∈ {1, 2, 3, 4, 6, 8, 10, 13, 16, 20, 25, 30, 45, 60, 75, 100} we trained four EnD2
models on an ensemble consisting of the first N models in the first of the four sets,
corresponding to what was done in the original study. We also trained one model on an
ensemble consisting of the first N models for each of the three remaining sets, capturing
the sensitivity of EnD2 to changes in the underlying ensemble. All ensemble and EnD2
models were then evaluated on the classification task. This experiment tests Claim 3.
Temperature ablation study: We reproduce the temperature ablation study by training
EnD2 models for various initial temperatures. For each T ∈ {1, 2, 3, 4, 5, 7.5, 10, 15, 20}
we trained three EnD2 models with initial temperature T on an ensemble consisting of
100 VGG16 models. The EnD2 models were then evaluated on the classification task. In
this experiment, we have chosen to use a slightly finer spacing between the tempera-
tures than what the original authors used. This experiment tests Claim 4.
Simplex visualization: A key motivation for EnD2 is the idea that an ensemble can dis-
tinguish between knowledge uncertainty and data uncertainty, and that this distinction
is retained by the EnD2 model. This is communicated using a schematic figure show-
ing ensemble predictions on a simplex. A similar schematic figure can be found in [3],
depicting a Dirichlet PDF of a PriorNet on a simplex. We recreated these figures using
experimental data in order to examine Claim 5 from a novel perspective. A new training
set was created, consisting of all images from the CIFAR10 train set with one of three
labels chosen for their similarity: ʼdeerʼ, ʼhorseʼ, and ʼdogʼ. The remaining images were
reserved as out-of-distribution dataset for testing. CIFAR-100 was used as auxiliary data.
An ensemble and EnD2 was then trained on this data using the same architecture and
processed as before. We then selected various images from the test set and visualized
the ensemble predictions as well as the PDF of the EnD2 model. The simplex visualiza-
tion was created using open source code 2.

1We used the open-source implementation in https://github.com/google/uncertainty-metrics.
2http://blog.bogatron.net/blog/2014/02/02/visualizing-dirichlet-distributions/




Table 3. Classification metrics on CIFAR-10. Error bounds signify two standard deviations, taken
over three models. Up-arrow (↑) indicates that higher is better, down-arrow (↓) indicates that
lower is better.

Crit.
ERR↓
PRR↑
ECE↓
NLL↓

IND

ENSM

EnD

9.87±0.70
69.80±1.31
68.18±0.57
1.58±0.01

8.80±N A
80.30±N A
1.65±N A
0.25±N A

8.70±0.53
78.67±0.12
1.56±0.09
0.26±0.01

EnD2

9.90±0.20
76.97±0.83
2.39±0.22
0.33±0.00


9.90±0.20
78.37±1.21
1.77±0.31
0.29±0.00

EnD2

+AUX
10.17±0.12
77.20±0.72
3.04±0.49
0.34±0.00

PN+AUX

10.00±0.35
56.57±9.49
9.37±0.62
0.46±0.00

Table 4. OOD AUC-ROC↑ on CIFAR-10 (in) and LSUN (out). Error bounds signify two standard
deviations, taken over three models. Up-arrow (↑) indicates that higher is better, down-arrow (↓)
indicates that lower is better.

Unc.
Tot.↑
Know.↑

IND

ENSM

EnD

EnD2


86.63±0.31
-

90.00±N A
89.30±N A

89.87±0.46
-

88.33±0.42
84.70±1.25

90.60±0.20
-

EnD2

+AUX
90.23±0.12
88.07±0.46

PN +AUX

92.03±0.46
90.97±0.42

### 3.5 Computational requirements

Training and evaluation were performed on two mid-range consumer GPUs (RTX 2070,
GTX 1660s) locally. Regarding VRAM, at least 4711 MiB is required for the models. The
total number of GPU time required for the final results is 11.4 GPU days on an RTX 2070.
The accumulated GPU days during the reproduction is 3-5 times this amount. We pro-
vide detailed numbers in the supplementary materials.

## 4 Results

### 4.1 Classiﬁcation performance

The classification results are shown in Table 3. Overall, the ensemble seems to perform
best, and when it does not, it is still within error bounds. Curiously, EnD2
+AUX seems to
perform worse than the individual model in regards to ERR.

4.2 Out-of-distribution detection performance

The OOD-detection results are shown in Table 4. The results suggest plain EnD2 per-
forms worse than ENSM, but that the addition of an auxiliary dataset brings the perfor-
mance up to at least the level of ENSM. More surprising, perhaps, is that EnD2 seems
to perform worse than EnD. In both metrics PN+AUX has a significant lead. Using knowl-
edge uncertainty instead of total uncertainty decreases the effectiveness of all tested
models. The supplemental material contains histograms showing the distribution of
estimated total and knowledge uncertainty over the images.

### 4.3 Ensemble size ablation study

Figure 1 shows the results of the ensemble size ablation study. The lines ʼENSM Paperʼ
and ʼEnD2 Paperʼ show the results of the original paper. The bands indicate two stan-
dard deviations. Two bands surround the ʼEnD2
+AUXʼ line, representing the two types of
variation we have examined. The purple band represents the variation of four EnD2
models each trained on a different ensemble. The orange band represents the varia-
tion of four EnD2 models all trained on the same ensemble. The band surrounding the
ʼEnD2

+AUX Paperʼ line corresponds to the latter type of variation.




There appears to be a trend of small improvement when the number of models is in-
creased, but the high level of uncertainty makes it difficult to draw conclusions from
the remaining points. Nonetheless, the results seem to generally indicate that EnD2 is
not particularly sensitive to ensemble size.

Figure 1. Ensemble size ablation study on CIFAR-10 classification.

### 4.4 Temperature ablation study

The results of our temperature ablation study are shown in Figure 2, along with the
results of the original paper. For initial temperature equal to 1 and 2 our models fail to
converge, resulting in poor classification performance. Raising the initial temperature
to 3 allows the model to converge. Increasing the initial temperature further has no
significant effect.
It is worth noting the negative PRR values for T = 2. The original authors mention this
possibility when they propose the metric, and offer the interpretation that this means
that the model is increasing the classification error by rejecting samples, performing
worse than simply rejecting at random.

### 4.5 Simplex visualization

Predictions for four images are visualized in Figure 3. These four images were selected
from the CIFAR10 dataset for respectively having the lowest total uncertainty, highest
data uncertainty, highest knowledge uncertainty, and highest total uncertainty, as mea-
sured by the ensemble. The third row shows the Dirichlet PDF of EnD2. There is a
strong tendency towards extremely sharp distributions, even when the ensemble has
high spread, making comparison difficult. For this reason the fourth row plots the PDF
after being transformed by the transformation log(x + 1). It is now possible to see that
the PDF is adapting to the distribution of the ensembles.




Figure 2. Temperature ablation study on CIFAR-10 classification.

Figure 3. Visualization of ensemble distribution and EnD2 PDF. The classes are, from left, to top,
to right, Deer, Horse and Dog.

Figure 4. Random images from in-domain.




Figure 5. Random images from out-of-domain.

We also plot randomly selected images from the in, out, and auxiliary datasets respec-
tively. The PDF has again been transformed using log(x + 1). Figure 4 shows images
from the in-domain dataset, and Figure 5 shows images from the out-of-domain dataset.
The PDF appears to follow the ensemble fairly well, but it is noteworthy that the ensem-
bles show such a low degree of spread despite encountering samples on which they have
not been trained.

## 5 Discussion

### 5.1 Comparison with original paper

We now revisit the six claims which we specified in Section 2.

1. Classification performance: When compared to the original table we see overall
worse performance. This is likely rooted in the fact that we were unable to achieve
as high accuracy on our base VGG16 as in the original article. We therefore instead
consider the relative performance between the models. Our supplementary ma-
terial contains a table allowing for easy comparison with the original results. For
example, we find that our EnD2 has 112.5% of the classification error of the ensem-
ble, while in the original paper this figure is 117.7%. The absolute difference is the
same in both papers, 1.1 percentage units. Our results generally agree well, with
those of the authors. There are some discrepancies in expected calibration error,
but our extremely high ECE for the individual model suggests that there might be
an issue in our computations of this metric. Overall our findings support Claim 1.

2. Out-of-distribution detection performance: For the most part, our results agree
with Claim 2. For instance, we found that using total uncertainty EnD2 without
auxiliary data had 98.1% of the AUC-ROC of the ensemble, while the correspond-
ing figure with auxiliary data was 100.0%. In the original paper, these figures were
96.8% and 99.8% respectively. There is one very significant discrepancy, however.
With auxiliary dataset, our EnD2had 99.6% of the AUC-ROC of our EnD, while in
the original paper this figure is 106.5%. A similar relationship exists without the
auxiliary dataset. It is worth noting that in the original paper EnD performs worse
than even the individual model, and the authors themselves note that this is odd.
Since EnD2 is designed to overcome certain shortcomings of EnD in terms of un-
certainty estimation we believe that this warrants further investigation.

3. Dependency on ensemble size: For prediction error and negative log-likelihood,
our results confirm the relative performance between ensembles and EnD2
+AUX,
with increased resolution. For expected calibration error, the relative performance
is confirmed for a large number of models, but for a small number of models, we
get contradictory results. Their results seem to suggest that smaller ensembles
have worse calibration, which is not expected, as per [1]. Our results confirm this
expectation. In their paper, they state this expectation, but we see no comment




for this discrepancy. For prediction rejection rate, we confirm the relative perfor-
mance, and also show that it starts to drop rapidly below their tested range.

4. Dependency on temperature annealing: Our results diverge heavily from the re-
sults in the paper for temperatures 1 and 2. While the original authors are able to
train working but sub-par models with these temperatures, we are unable to get
the models to converge at all. We re-did the experiments with a new ensemble,
and experimented with the smoothing factor and auxiliary data, but were unable
to find any explanation for this difference. Nevertheless, these findings support
the claim that temperature annealing is essential for successful use of the EnD2
method. The authors suggested temperature 5 as a minimum value beyond which
larger values make no difference. Our findings support this as well, although our
increased resolution reveals that the minimum value for the CIFAR-10 dataset is
closer to 3 than 5.

5. Uncertainty decomposition: Based on the description in [3] an image with a high
knowledge uncertainty should produce a Dirichlet PDF with a close to uniform
spread. Our simplex visualizations on the 3-class+AUX dataset shows that this is
not the case. This is not too surprising, given that high knowledge uncertainty
correlates with small alphas, and this in turn produces convex as opposed to flat
probability density surfaces. Overall, these plots suggest that EnD2can capture the
uncertainty decomposition of the ensemble.

The plots also show an interesting behaviour in the ensemble. The ensembles
agree to a surprising extent on the out-of-domain samples. In fact, when they do
disagree it normally takes the form of data uncertainty as opposed to knowledge
uncertainty. This could perhaps shed some light on the observation that knowl-
edge uncertainty does not seem to be useful for OOD-detection on CIFAR-10. The
original authors explain this as essentially being a property of the dataset. We feel,
based on the visualizations, that another possibility might be that the ensemble
models simply are not diverse enough to provide a useful measure of knowledge
uncertainty.

### 5.2 What was difﬁcult

Although the general idea of the paper is well formulated in mathematical terms, the
original paper does not provide many hints regarding how to implement the method. In
our case, this imposed a significant barrier to immediately reproducing the work, since
our inexperience meant that weʼre unable to immediately see how it could be imple-
mented in a modern deep learning framework. There is some code available in a public
repository hosted by one of the authors but this is not mentioned in the paper, and so
we could not treat it as an official implementation. We have provided a pseudocode in
our supplemental material, in order to hopefully assist future reproducers.
There are also some missing details regarding the models used. Most importantly, the
authors mention that they have used a modified VGG model, but do not specify what
these modifications are. The authors also do not specify the min and max value of the
cyclic LR. These details may explain the consistently worse performance of our models
despite the attempt of replication.

### 5.3 What was easy

The synthetic dataset was fairly easy to reconstruct, and the other datasets are well
known and publicly available. The data augmentation was straightforward and easy to
incorporate into a training pipeline. The base model (VGG16) used in most of the exper-
iments is well known and was computationally feasible to train. Similarly, the datasets
are not excessively demanding in terms of computation, although in our case training




time did become a limiting factor due to the amount of time we spent on implemen-
tation and experimentation. The mathematical formulation of the model is very good,
helping the conceptual understanding.

### 5.4 Communication with original authors

We did not communicate with the authors while reproducing their work, although we
did refer to some resources which one of the authors has made publicly available, in-
cluding an repository 3 made for [3] containing an implementation of EnD2. At the
same time as submitting this report, we also sent a copy to the authors and asked for
their comments.

References

1.

2.

3.

B. Lakshminarayanan, A. Pritzel, and C. Blundell. “Simple and Scalable Predictive Uncertainty Estimation using
Deep Ensembles.” In: Advances in Neural Information Processing Systems 30. 2017.
A. Malinin, B. Mlodozeniec, and M. Gales. “Ensemble Distribution Distillation.” In: International Conference on
Learning Representations (ICLR). 2020.
A. Malinin and M. Gales. “Predictive Uncertainty Estimation via Prior Networks.” In: Advances in Neural Infor-
mation Processing Systems 31. 2018.

4. G. Hinton, O. Vinyals, and J. Dean. “Distilling the Knowledge in a Neural Network.” In: NIPS Deep Learning and

5.
6.

7.

Representation Learning Workshop. 2015.
A. Krizhevsky. “Learning Multiple Layers of Features from Tiny Images.” In: University of Toronto (May 2012).
F. Yu, Y. Zhang, S. Song, A. Seff, and J. Xiao. “LSUN: Construction of a Large-scale Image Dataset using Deep
Learning with Humans in the Loop.” In: CoRR abs/1506.03365 (2015). arXiv:1506.03365. URL: http://arxiv.org/
abs/1506.03365.
K. Simonyan and A. Zisserman. “Very Deep Convolutional Networks for Large-Scale Image Recognition.” In:
International Conference on Learning Representations (ICLR). 2014.

3https://github.com/KaosEngineer/PriorNetworks/tree/master/prior_networks




A The EnD2 Algorithm

The original paper features an excellent description of the mathematical formulation of
the EnD2 model, but we did not find it immediately obvious how to translate this into
an implementation in a modern deep learning framework. For this reason, we will now
briefly describe it from an algorithmic-centred perspective using pseudocode and plain
English.
The process of training an EnD2 model is described in Algorithm 1. In practice, the opti-
mization in line 7 can easily be achieved using the standard ”fit” method of frameworks
such as Keras and PyTorch, by constructing an intermediate dataset and using a custom
loss function with a callback for annealing the temperature.
The intermediate dataset is constructed by first adding any auxiliary images to the train-
ing images, and then passing the extended image set as input to the ensemble. The
ensemble should output an array of logits as described in line 5 of Algorithm 1. The
new dataset is then formed by matching each image to its corresponding ensemble log-
its, using the latter as the target.
The custom loss function is described in Algorithm 2. This formulation includes temper-
ature annealing. This loss function is the only modification necessary to adapt a general
classification model into an EnD2 model, providing it is then trained on an intermediate
dataset as described in the previous paragraph. Note that this formulation assumes that
the model outputs logits. This output can be converted into Dirichlet probabilities by
applying the standard softmax operation.

Algorithm 1: Training algorithm for EnD2 given an ensemble
Input

:Ensemble En outputting logits, training data X (same as the ensemble is
trained on), (optional) Out of distribution data XOOD

Output :Trained EnD2 model

X = [X, XOOD] // append OOD data to training set

1 if XOOD not None then

3 end
4 ϕ = En.predict(X) // exp(ϕ) are the labels for EnD2
5 // ϕ is a tensor of logits corresponding to the true distribution, each row

corresponds to a model and each column a class. Each matrix corresponds to one
image

6 modelθ ← classif ier //create a new classifier model with weights θ, with logits as

output

7 EnD2 = argminθ{LossEnD2(ϕ, modelθ(X))} //train model backpropagation
8 return EnD2

B Experiments on Synthetic Data

B.1 Methodology

The goal with these experiments is to provide qualitative justification for Claim 5 and
illustrate the inner workings of EnD2. We also provide some new experiments on tem-
perature annealing and the size of the auxiliary dataset, to visualize their effect.

Dataset — To illustrate the model, Malinin et. al. use a synthetic dataset in R2. Our ren-
dering of this dataset can be seen in Figure 6. This is advantageous since it enables
plotting both knowledge and data uncertainty over the entire data manifold, giving a
qualitative understanding of whether the algorithm works or not, in contrast to higher


:Ensemble logits: ϕ, predicted logits: z, temperature: T = T (t), annealing


Algorithm 2: loss for EnD2
Input
Output :cost: C

1 ϵ = 10−8 // Smoothing factor
2 δ = 1 − 10−3 // Central smoothing factor
3 α = ez/T (t) // elementwise exponential
4 M = #models
5 N = #classes
6 for i ← 1 to M do
∑
α0,i =

8 end
9 PEn = sof tmax(ϕ/T (t)) // softmax over classes
10 PEn = δ(PEn − 1
∑
11 T IT =

N ) + 1

N

N

j αi,j // sum over the classes to produce the precision factor

i (log(Γ(αi + ϵ))) − log(Γ(α0 + ϵ)) // target independent term, where

log(Γ(x)) = log((x − 1)!)

∑

12 A = 1
M
13 T DT = −
14 return (T DT + T IT )T (t)2

N

M
i (log(PEni + ϵ) // mean over ensemble
∑

i ((αi − 1)Ai) // target dependent term, sum over classes

Figure 6. The synthetic, spiral dataset.

dimensional data (images, etc.) that cannot be plotted. The dataset itself looks like a spi-
ral, divided into three classes shaped as spiralling arms of increasing radius. The spirals
are centred and almost symmetric around the origin. Furthermore, they have increased
noise and overlap with radius, which leads us to believe that uncertainty should vary as
well. In addition to the spiral data an OOD data-set, referred to as the AUX data-set is
also used, which takes the form of a ring slightly outside the spiral.
For the experiments, 1000 samples per ID class are used, both for training and test. The
number of AUX samples was also 1000. This is the same setting as the original paper.
The generation of the data uses the original paperʼs code, but the hyperparameters were
not specified. Our hyperparameters can be found in our code. We manually searched
for hyperparameters, so that our plot would look as close to theirs, but the exact corre-
spondence is probably not achieved.

Model description and hyperparameters — The original paper does not specify what type of
neural network was used for classification. We were also unable to find it in the (unoffi-
cial) code. Instead, we chose to use a simple DNN with four hidden layers, each of width




Table 5. Classification error on Spiral Dataset, compared with [2]. Error bars are 95%-confidence
intervals assuming normal distribution. Note that our results likely use a different base model
and training procedure than the original paper, since it was not specified there.

ERR↓

IND

ENSM

EnD

EnD2

Our results
Paper [2]

8.20±0.67
13.21

2.3±N A
12.37

3.90±0.65
12.39

3.86±0.70
12.47

EnD
+AUX
2.61±0.11
12.41

EnD2
+AUX
4.67±3.26
12.40

EnD2
+AUX,ANN
3.30±0.59
-

EnD2
+AUX,T=2.5
3.45±0.96
-

EnD2
+AUX20
5.0±1.54
-

64 with ReLu-activation functions, trained by minimizing the categorical cross-entropy
using the Adam-optimizer, all with standard tf.keras settings, for 85 epochs. EnD
and EnD2 used the same base model but was instead trained for 500 epochs.

Experimental setup and code — On the output of an ensemble of 100 models, all differently
randomly initialized, we train EnD and EnD2 both with and without auxiliary data, us-
ing an initial temperature of 1, as in the paper. Doing this, we observed that the training
diverges for many initialisations, mainly for EnD2
+AUX. Thus, we also used an initial tem-
perature of T = 2.5, both with and without annealing. The annealing schedule was
T = 2.5 between epoch 0 and 200, linearly decreasing to 1 between epoch 200 and 400
and 1 between epoch 400 and 500. Additionally, we also trained a model EnD2
+AUX20, with
only 20 samples from the auxiliary dataset.
All 7 models were trained 20 times, with different random initialisations. To make sure
they converged, the test error was calculated. In cases test error was above 10%, it was
deemed as non-convergence, and not taken into account. Among the converged ones,
the mean error and the 95%-confidence interval around the mean is calculated, assum-
ing a normal distribution. This means that for cases with fewer samples, the confidence
interval is larger.
The main goal of this experiment is to visually show the total uncertainty, the data un-
certainty and the knowledge uncertainty. They were calculated as specified in [2] and
[3], for the grid [−2000, 2000] × [−2000, 2000] at all coordinates divisible by four, for a
total of 106 points.
The full code is available at https://github.com/lennelov/endd-reproduce.

Computational requirements — The experiments were run on the CPU of a normal laptop
(2.7 GHz Dual-Core i5). The total time to reproduce the ensemble of 100 models and all
20 repetitions of all 7 tested distillation methods, is around 5 to 6 hours.

B.2 Results

Classiﬁcation accuracy — In Table 5, the classification accuracy from our experiment and
the original paper is reported. We see that

• the ensemble outperforms the individual models, and that all distillation methods

perform closer to the ensemble, than an individual model.

• the best performance is achieved by EnD with auxiliary data.

• using annealing or not when starting at T = 2.5 does not affect the final classifica-

tion accuracy.

Visualization of uncertainty — The total, data and knowledge uncertainty is plotted in Figure
7 for a grid of 106 points. In contrast to the original paper, we fix the scale of the colour
bar for better comparability between plots.
We observe that




Table 6. Computation requirements for major experiments, and which claims they test. GPU time
refers to time on an NVIDIA GeForce RTX 2070. Equivalent cost represents the cost if run on a
V100 on Google cloud, for $2.48 per hour.

Experiment
Ensemble, training
Ensemble, labeling
Ensemble, inference
Evaluation, claim 1 and 2
Size ablation, claim 3
Temperature ablation, claim 4
3-class ensemble, claim 5
Total

Models GPU min/model GPU days
4.44
0.13
0.06
0.53
3.97
0.96
0.36
11.413


0.45
0.23


5.25


Eqv. cost (USD)
91.53
2.57
1.32
10.94
81.69
19.69
7.51
235.06

• EnD2 is not able to emulate the uncertainty landscape of the ensemble, but EnD2

+AUX

can approximate it fairly well.

• Starting at a higher temperature (T = 2.5) and using annealing produces similar
results as starting at temperature 1, but starting at temperature 2.5 and keeping it
there for the entire training duration does not capture the true uncertainty.

• Using a smaller auxiliary dataset gives a worse approximation of the ensembleʼs

uncertainty landscape.

C Computational requirements for reproduction

In this section, we report the computational resources used for this reproduction. The
running time of the major experiments on CIFAR-10 is expressed in time on an RTX
2070. For easier comparison, we also report the equivalent cost when running on a V100
GPU on Google Cloud for $2.48 per hour, given a relative performance of 2.89 versus
an RTX 20704. Note that these figures represent the time to reproduce only the final
experiments. We estimate that the total GPU time used for this reproduction, including
experimentation and bug-hunting, to be 3 to 5 times as long. The full data can be seen
in Table 6.

D Histograms

To compare ensembles, EnD2 and EnD2
+AUX on the CIFAR-10 and 3-class CIFAR-10 datasets,
we provide histograms of data and knowledge uncertainty for in- and out-of-domain-
distribution, in Figure 8 and 9.

E Relative performance of EnD2 compared to ensemble and original ar-

ticle

In Tables 3 and 4 of the main report we report several measures for the 7 different mod-
els tested. For better comparability, we here also provide the values normalized to the
ensemblesʼ performance, both for our experiments, and for the original paper, in Table
8 and 7.

4Benchmark taken from https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/




(a) Ensm. Tot. Unct.

(b) Ensm. Data Unct.

(c) Ensm. Know. Unct.

(d) EnD2 Tot Unct.

(e) EnD2 Data Unct.

(f) EnD2 Know. Unct.

(g) EnD2

+AUX Tot Unct.

(h) EnD2

+AUX Data Unct. (i) EnD2

+AUX Know. Unct.

(j) EnD2
Unct.

+AUX,ANN Total

+AUX,ANN Data

+AUX,ANN Know.

(k) EnD2
Unct.

(l) EnD2
Unct.

(m) EnD2
Unct.

(n) EnD2
Unct.

+AUX,T=2.5 Tot.

+AUX,T=2.5 Data

+AUX,T=2.5 Know.

(o) EnD2
Unct.

EnD2

+AUX20

(p)
Unct.

Tot.

(q)
Unct.

EnD2

+AUX20 Data

(r) EnD2
Unct.

+AUX20 Know.

Figure 7. Recreation of Figure 3 in [2], showing uncertainties over entire data manifold.




Table 7. OOD ROC-AUC↑ on CIFAR-10 (in) and LSUN (out), normalized to ensemble results. Error
bounds signify two standard deviations, taken over three models.

Unc.

IND

ENSM

EnD

Tot. our
Tot. paper
Know., our
Know., paper

0.96±0.00
0.97±0.01
-
-


1.00±0.01
0.94±0.01
-
-

EnD2

0.98±0.00
0.97±0.01
0.95±0.01
0.98±0.01


1.01±0.00
0.94±0.01
-
-

EnD2

+AUX
1.00±0.00
1.00±0.01
0.99±0.01
0.99±0.01

PN +AUX

1.02±0.01
1.01±0.01
1.02±0.00
1.01±0.01

Figure 8. Data/knowledge uncertainty-distributions for ensemble, EnD2 and EnD2

+AUX.

Figure 9. Data/knowledge uncertainty-distributions for ensemble and EnD2
FAR10 dataset

+AUX on the 3-class CI-




Table 8. Classification metrics on CIFAR-10, normalized to ensemble results. Error bounds signify
two standard deviations, taken over three models.

Crit.
ERR↓, our
ERR↓, paper
PRR↑, our
PRR↑, paper
ECE↓, our
ECE↓, paper
NLL↓, our
NLL↓, paper

IND

ENSM

EnD

1.12±0.08
1.29±0.06
0.87±0.02
0.97±0.01
41.37±0.35
1.69±0.31
6.38±0.04
1.32±0.05


0.99±0.06
1.08±0.05
0.98±0.00
0.98±0.01
0.94±0.05
2.00±0.15
1.06±0.04
1.16±0.05

EnD2

1.13±0.02
1.18±0.03
0.96±0.01
0.98±0.01
1.45±0.13
0.77±0.15
1.35±0.02
1.32±0.05


1.13±0.02
1.08±0.03
0.98±0.02
0.98±0.00
1.08±0.19
2.00±0.46
1.19±0.01
1.16±0.05

EnD2

+AUX
1.16±0.01
1.11±0.06
0.96±0.01
0.99±0.00
1.85±0.29
1.69±0.31
1.38±0.01
1.26±0.00

PN+AUX

1.14±0.04
1.21±0.10
0.70±0.12
0.94±0.02
5.69±0.37
9.23±0.54
1.86±0.04
2.00±0.05

---
**Source PDF:** `9e4fa75037d4.pdf` (2021_10_article.pdf)  
**URL:** https://zenodo.org/record/4834516/files/article.pdf
