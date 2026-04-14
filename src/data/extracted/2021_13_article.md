R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020


David Mizrahi1, ID , Oğuz Kaan Yüksel1, ID , and Aiday Marlen Kyzy1, ID
1EPFL, Lausanne, Switzerland

Edited by
Koustuv Sinha,
Sasha Luccioni

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

Reproducibility Summary

Scope of Reproducibility

The original paper proposes partially Huberised losses, which possess label noise robust-
ness. The authors claim that there exist label noise scenarios that defeat Huberised but
not partially Huberised losses, and that partially Huberised versions of existing losses
perform well on real-world datasets subject to symmetric label noise.

DOI
10.5281/zenodo.4834744

Methodology

All the experiments described in the paper were fully re-implemented using NumPy,
SciPy and PyTorch. The experiments on synthetic data were run on a CPU, while the
deep learning experiments were run using a Nvidia RTX 2080 Ti GPU. Running the ex-
perimentation necessary to gain some insight on some of the network architectures used
and reproducing the real-world experiments required over 550 GPU hours.

Results

Overall, our results mostly support the claims of the original paper. For the synthetic
experiments, our results differ when using the exact values described in the paper, al-
though they still support the main claim. After slightly modifying some of the experi-
ment settings, our reproduced figures are nearly identical to the figures from the original
paper. For the deep learning experiments, our results differ, with some of the baselines
reaching a much higher accuracy on MNIST, CIFAR-10 and CIFAR-100. Nonetheless,
with the help of an additional experiment, our results support the authorsʼ claim that
partially Huberised losses perform well on real-world datasets subject to label noise.

What was easy

The original paper is well written and insightful, which made it fairly easy to implement
the partially Huberised version of standard losses based on the information given. In ad-
dition, recreating the synthetic datasets used in two of the original paperʼs experiments
was relatively straightforward.


Code is available at https://github.com/dmizr/phuber. – SWH swh:1:dir:3363073199859b8bec0c4362e47aa1e786985793.
Open peer review is available at https://openreview.net/forum?id=TM_SgwWJA23.




What was difﬁcult

Even though the authors were very detailed in their feedback, finding the exact hyper-
parameters used in the real-world experiments required many iterations of inquiry and
experimentation. In addition, the CIFAR-10 and CIFAR-100 experiments can be difficult
to reproduce due to the high number of experiment configurations, resulting in many
training runs and a relatively high computational cost of over 550 GPU hours.

Communication with original authors

We contacted the authors on multiple occasions regarding some of the hyperparameters
used in their experiments, to which they promptly replied with very detailed explana-
tions.




## 1 Introduction

Gradient clipping is a well-established technique in machine learning, usually moti-
vated by its benefits in optimization. For example, clipping is used extensively to remedy
the well-known problem of exploding gradients [1], commonly faced when training re-
current neural networks. Intuitively, it ensures that the norm of the gradient behaves
well under iterates of optimization. Indeed, Zhang et al. [2] provide a theoretical expla-
nation of the improved convergence speed of gradient clipping over standard gradient
descent.
In this work, however, we reproduce the paper ”Can gradient clipping mitigate label
noise?” (referenced as ”the paper” or ”the original paper”) by Menon et al. [3] (referenced
as ”the authors”) which focuses on robustness properties of gradient clipping. Informally,
clipping caps the influence of any descent direction, which might help in the presence of
label noise. Starting with this intuition, the authors study whether clipping can alleviate
the problem of label noise studied in Ekholm and Palmgren [4], Menon et al. [5], and
Zhang and Sabuncu [6]. More specifically, they analyze the problem under symmetric
label noise with the following simple linear setting: stochastic gradient descent with a
linear model in a binary classification task.
Before turning our attention to the paperʼs experiments, which are the main focus of this
reproducibility work, we state two main theoretical findings in this linear setup and the
resulting novel extension of the cross-entropy loss function:

• Gradient clipping does not provide label noise robustness even in this simple lin-
ear setup. Specifically, clipping is linked to using a Huberised loss, which preserves
classification-calibration but is not robust to symmetric label noise.

• A new clipping variant for composite losses is proposed, where only the contribu-
tion from the base loss is considered for clipping. The equivalent partially Huberised
loss preserves classification-calibration and is robust to symmetric label noise.
• The resulting multi-class generalization of the partially Huberised cross-entropy
loss is given in Equation 1. Suppose we have softmax probability estimates pθ(x, y),
then the partially Huberised softmax cross-entropy loss (PHuber-CE) is defined for τ > 1
as:

{

ℓθ(x, y) =

−τ · pθ(x, y) + log τ + 1,
− log pθ(x, y),

if pθ(x, y) ≤ 1
τ


(1)

Then, the authors evaluate their partially Huberised loss in experiments on synthetic
data (referenced as ”synthetic experiments”) to demonstrate its behavior under symmet-
ric label noise. They show symmetric label noise scenarios that defeat the logistic loss
and the Huberised logistic loss, but not the partially Huberised logistic loss. Moreover,
they assess the effectiveness of partial Huberisation on real-world datasets subject to
symmetric label noise (referenced as ”real-world experiments”). They empirically ver-
ify that partially Huberised versions of existing losses behave well in the presence of
symmetric label noise, through deep-learning experiments on the MNIST, CIFAR-10 and
CIFAR-100 datasets.
We thoroughly reproduce the synthetic and real-world experiments in section 3 and sec-
tion 4 respectively. Then, we evaluate the experimental results in section 5 and conclude
with the assessment of empirical claims in section 6.

## 2 Background

Gradient clipping. Consider a supervised learning task with samples (x, y) ∈ (X × Y) ∼
D, and a loss function lθ : X × Y → R. For this setting the gradient g(θ) and the clipped
gradient ¯gτ (θ) are defined as follows:




g(θ) =


N

N∑

n=1

∇lθ(xn, yn)

{

¯gτ (θ) =

τ g(θ)
∥g(θ)∥2
g(θ)

if ∥g(θ)∥2 ≥ τ


Label noise. In classification under label noise, one has samples from a noisy distri-
bution P ¯D(x, y) instead of a clean distribution PD(x, y). For example, under symmetric
label noise, all instances have a constant probability of their labels being flipped uni-
formly to any of the other classes. The task remains to minimize risk over the clean
distribution D. Some recent loss-based proposals for learning under symmetric label
noise are the linear or unhinged loss [7] and the generalized cross-entropy loss [6].
Huberised losses. Huberised and partially Huberised losses, as defined in the paper,
are closely related to the Huber loss [8], which is widely employed in robust regression.
In the binary classification setting, for a predictor f : X → R and labels y ∈ {±1}, these
losses are derived from the logistic loss ϕ(f (x) · y) = ϕ(z) = log(1 + e−z), which can
also be written as ϕ(z) = φ(F (z)), with the base loss φ(u) = − log u and the link func-
tion F (z) = σ(z). The Huberised logistic loss ¯ϕτ (Equation 2) linearises the entire logistic
loss beyond a certain threshold, while the partially Huberised logistic loss ˜ϕτ (Equation 3)
linearises only the base loss but leaves the link function intact.

{

¯ϕτ (z) =

−τ · z − log(1 − τ ) − τ · σ−1(τ )
log (1 + e−z)

{

˜ϕτ (z) =

−τ · σ(z) + log τ + 1
log (1 + e−z)

if z ≤ σ−1


τ

if z ≤ −σ−1(τ )

(

)

(2)

(3)

The partially Huberised softmax cross-entropy loss (Equation 1) is obtained by applying that
same partial Huberisation to the softmax cross-entropy loss, in which the link function
is a softmax instead of a sigmoid. For more information on Huberised losses, we kindly
refer to the original paper [3].

## 3 Synthetic experiments

We now study two synthetic experiments proposed by the authors to show the existence
of label noise scenarios that defeat Huberised but not partially Huberised losses. We will
start by discussing the 2D setting proposed in Long and Servedio [9] and then discuss the
1D outliers setting given in Ding [10]. These experiments are fully re-implemented with
NumPy [11] and SciPy [12]. Experimental setups including methods and hyperparame-
ters are fully verified according to the original paper and in necessary cases, according
to the additional details obtained from the authors. Our experiments are configurable
through the Hydra framework [13]. Our code re-implementing both the synthetic and
real-world experiments is available at: https://github.com/dmizr/phuber

### 3.1 Long and Servedio dataset

Long and Servedio [9] consider a set of four positive labeled points: one large margin
example (1, 0), one puller example (γ, 5γ) and two penalizer examples (γ, −γ) where 0 <
γ < 1
6 , in a binary classification task with a linear model without a bias term. The
halfspace x1 > 0 correctly classifies all the samples. However, one can show that under
symmetric label noise, minimizing over a wide range of convex losses with a suitable γ
will result in a predictor equivalent to a random predictor.
The authors build on Long and Servedio [9], and consider a mixture of six isotropic Gaus-
sians N (µi, σ2I2), with σ = 0.01 and µi ∈ {±(1, 0), ±(γ, 5γ), ±(γ, −γ)} ⊂ R2, with
4 for the two Gaussians centered around ±(γ, −γ) and 1
γ = 1

for the rest. An instance (x1, x2) is labeled positive if x1 ≥ 0 and negative 

24 . Mixing weights are 1




N = 1000 random samples are drawn from this distribution, and the label of each sam-
ple is flipped with corruption probability ρ < 0.5. Then, a linear classifier is trained
using Scipyʼs SLSQP (Sequential Least Squares Programming) optimizer for a maximum
of 100 iterations with each of the following losses:

• the logistic loss
• the Huberised version of the logistic loss, with τ = σ(−1) ≈ 0.26
• the partially Huberised version of the logistic loss, with τ = 1 + e−1 ≈ 1.36

After contacting the authors, we found that the above τ values were used instead of the
values provided in the original paper, which were τ = 1.0 and τ = 2.0 for the Huberised
and the partially Huberised loss respectively.
Once trained, the classifier is evaluated on 500 clean test samples.
Figure 1a and Figure 1b show our results over 500 independent runs for ρ = 0.45 and
ρ = 0.2 respectively. When using ρ = 0.45, as stated in the original paper, we fail to
reproduce a figure that exactly matches the authorsʼ results. However, through experi-
mentation, we found that for a lower level of noise corruption such as ρ = 0.2, we get
results that are very similar to the original paper, with the partially Huberised loss al-
ways achieving perfect classification, while the logistic and Huberised losses succumb
to label noise and perform no better than chance.

### 3.2 Outliers dataset

The 1D setting from Ding [10] is composed of 10,000 linearly separable inliers: 5000 sam-
ples from the unit variance Gaussian N (1, 1) with positive label, and 5000 samples from
the mirror image N (−1, 1) with negative label. In addition, 50 outliers are added: 25
samples from N (−200, 1) with positive label, and 25 samples from N (200, 1) with nega-
tive label. Assuming a linear model characterized by a scalar θ ∈ R, we comparatively
evaluate the empirical risk with and without outliers. We use the same three losses as in
subsection 3.1 but with τ = 0.1 and τ = 1.1 for the Huberised and partially Huberised
loss respectively. 1
Figure 1c shows our results where dashed and solid curves represent the cases with
and without outliers respectively. As in the original paper, the optimal solutions for the
logistic and Huberised loss are changed from θ∗ = +∞ to θ∗ = 0 with the introduction
of outliers, whereas the partially Huberised loss remains intact.

(a) Long and Servedio (ρ = 0.45)

(b) Long and Servedio (ρ = 0.2)

(c) Effect of outliers

Figure 1. Reproduction of Long and Servedio [9] and Ding [10] experiments. In the Ding experi-
ment (c), the solid curve denotes empirical risk without outliers, while the dashed curve denotes
empirical risk with outliers.

1In the original paper, the τ values mistakenly reported as 1.0 and 2.0, along with the values in subsec-
tion 3.1. These updated values are obtained from the authors, after informing them τ = 1.0 for Huberisation
is equivalent to keeping base loss intact.


LogisticHuberisedPartial Huberised0.00.20.40.60.81.0Test accuracyLogisticHuberisedPartial Huberised0.50.60.70.80.91.0Test accuracy−2−10120.00.20.40.60.81.01.2()LogisticHuberPartial Huber

## 4 Real-world experiments

We now consider the deep learning experiments performed on three image classifica-
tion datasets: MNIST, CIFAR-10 and CIFAR-100. These experiments were fully re-implemented
with PyTorch [14], according to the description from the paper and implementation de-
tails obtained from the authors after contacting them. Configuration management for
these experiments was done with the help of the Hydra framework [13].

### 4.1 MNIST

Methodology — MNIST is a dataset of handwritten digits, consisting of a training set of
60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale
image associated with a label from 10 distinct classes. The dataset is normalized using
the mean and standard deviation from the training set, and no data augmentation is
applied. The training labels are then corrupted with symmetric noise at flip probability
ρ ∈ {0.0, 0.2, 0.4, 0.6}. As in the original paper, the same random seed is used to corrupt
the training labels across all trials.
We use a LeNet-5 [15], with a few modifications in order to reproduce the authorsʼ set-
tings as accurately as possible. Most notably, the tanh activation layers from the origi-
nal LeNet are changed to ReLU , and the weights are initialized according to a truncated
normal distribution with standard deviation σ = 0.1.
This model is trained for 20 epochs using Adam [16] with batch size N = 32, and weight
decay of 10−3. The initial learning rate is set to 0.001, and is lowered following an ex-
ponential decay schedule with decay rate 0.1 and decay steps of 10,000. That is, the
learning rate at iteration n is set to: ηn = η0 · rn/s, with η0 = 0.001, r = 0.1 and s = 104.
According to the authors, these hyperparameter values were chosen to obtain a good
baseline performance in a setting with no label noise.
For each level of label noise corruption, the test set accuracy of 6 different loss functions
is compared:

• the cross-entropy loss (CE)
• the linear or unhinged loss [7]
• the generalized cross-entropy loss (GCE), with α = 0.7 [6]
• the cross-entropy loss, with global gradient clipping applied using a max norm

threshold of τ = 0.1

• the partially Huberised version of the cross-entropy loss (PHuber-CE), with τ = 10
• the partially Huberised version of the generalized cross-entropy loss (PHuber-GCE),

with α = 0.7 and τ = 10.

The CE loss serves as a baseline, while the linear and GCE losses serve as representative
noise-robust losses. The model and hyperparameters used are identical for all losses
at all levels of label noise. For each of the real-world experiments and for each of the
partially Huberised losses, the authors selected τ ∈ {2, 10} so as to maximize accuracy
on a validation set, in a setting with flip probability ρ = 0.6.

Computational requirements — This LeNet model was trained with a Nvidia RTX 2080 Ti GPU.
Each run took roughly 2 minutes. Fully reproducing the authorsʼ experiments required
training this model 72 times, in order to do 3 trials for each combination of loss function
and level of label noise. This resulted in a total training time of around 2 hours.

Results — Our results are reported in Table 1, and a comparison with the original paperʼs
results can be found in Figure 2. Our reproduction matches the results from the original
paper for both the PHuber-CE and PHuber-GCE losses, although the CE, CE with gradi-
ent clipping and linear losses perform considerably better at high levels of label noise
than what was reported. As a consequence, the partially Huberised version of these
losses do not outperform the base losses at high levels of label noise, contrary to the




original paperʼs results. It is of note that in our reproduction, all losses, except for the
CE loss with gradient clipping, perform comparably, with a test accuracy higher than
97.5% at all levels of label noise.

Dataset

Loss function

MNIST

CE
CE + clipping
Linear
GCE
PHuber-CE τ = 10
PHuber-GCE τ = 10

ρ = 0.0
99.1 ± 0.1
97.0 ± 0.0
95.0 ± 3.5
98.8 ± 0.0
99.0 ± 0.0
98.9 ± 0.0

ρ = 0.2
98.8 ± 0.0
96.5 ± 0.0
98.5 ± 0.1
98.7 ± 0.0
98.8 ± 0.1
98.7 ± 0.0

ρ = 0.4
98.6 ± 0.0
95.7 ± 0.1
98.2 ± 0.0
98.5 ± 0.0
98.5 ± 0.1
98.4 ± 0.0

ρ = 0.6
98.0 ± 0.1
94.7 ± 0.1
97.6 ± 0.0
98.1 ± 0.0
97.6 ± 0.0


Table 1. Reproduction of the MNIST experiments. The mean and standard error of the test accuracy
over 3 trials is reported. The highlighted cells correspond to the best performing loss at a given ρ.

Figure 2. Test accuracy of LeNet-5 on MNIST

### 4.2 CIFAR-10 and CIFAR-100

Methodology — The CIFAR-10 and CIFAR-100 datasets [17] both consist of a training set
of 50,000 examples and a test set of 10,000 examples. Each example is a 32 × 32 color
image, associated with a label from 10 distinct classes for CIFAR-10, and 100 distinct
classes for CIFAR-100. Both datasets are normalized using per-channel mean and stan-
dard deviation, and the standard data augmentation for these datasets is applied, akin
to Zagoruyko and Komodakis [18]. That is, images are zero-padded with 4 pixels on each
side to obtain a 40 × 40 image, and then a random 32 × 32 crop is extracted and mirrored
horizontally with 50% probability. As in the MNIST experiment, the training labels are
corrupted with symmetric noise at flip probability ρ ∈ {0.0, 0.2, 0.4, 0.6}, with identical
noise seed across trials.
For both of these experiments, we use a ResNet-50 [19], as implemented in Liu [20]. This
implementation of the ResNet-50 differs from the one described by He et al. [19] to make
it more appropriate for classification on small images. The number of filters per layer
is identical, but the first layer, originally a 7x7 convolutional layer with stride 2 and
padding 3, is changed to a 3x3 convolutional layer with stride 1 and padding 1, and
the max-pooling layer that follows is removed. By removing these early downsampling
layers, this architecture performs better on CIFAR-10 and CIFAR-100 than the original
ResNet-50 2, which was designed for classification on ImageNet [21]. We decided to use
such an implementation for several reasons: First, it is used in many popular papers per-
forming classification on CIFAR with ResNets, such as DeVries and Taylor [22], Zhang et
al. [23], Li, Socher, and Hoi [24], and Zhang et al. [25]. Second, using the original ResNet-
50 yielded poor results, especially on partially Huberised losses. Third, after contacting
the authors about their implementation, they confirmed using a ResNet-50 with some of


CECE + clippingLinearGCEPHuber-CEPHuber-GCE7580859095100Accuracy98.798.698.398.898.598.699.197.095.098.899.098.9ρ = 0.0CECE + clippingLinearGCEPHuber-CEPHuber-GCE758085909510097.797.588.298.698.798.598.896.598.598.798.898.7ρ = 0.2CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function7580859095100Accuracy96.496.878.898.298.598.498.695.798.298.598.598.4ρ = 0.4CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function758085909510091.188.09.697.697.697.898.094.797.698.197.698.0ρ = 0.6paperours

the early downsampling layers removed, but could not provide more details as to which
layers were specifically changed or removed.
For CIFAR-10, this ResNet is trained for 400 epochs using SGD with Nesterov momentum
0.1 [26, 27], batch size N = 64, and weight decay of 5 × 10−4. 3 The initial learning rate
is set to 0.1 and is divided by 10 at the 160th, 300th and 360th epoch. For CIFAR-100,
this ResNet is trained for 200 epochs using SGD with Nesterov momentum 0.1, batch
size N = 128, and weight decay of 5 × 10−4. 4 The initial learning rate is set to 0.1
and is divided by 5 at the 60th, 120th and 160th epoch. According to the authors, these
hyperparameters were partially based on the setting from DeVries and Taylor [22], and
were chosen to obtain a good performance with CE in a setting with no label noise.
As in the MNIST experiment, the test set accuracy of the CE, CE with gradient clipping,
linear, GCE, PHuber-CE and PHuber-GCE losses are compared. The tunable parame-
ters for these losses are identical to the ones used in the MNIST experiment, except for
PHuber-CE for CIFAR-10, where τ = 2. The model and hyperparameters used are iden-
tical for all losses at all levels of label noise.
We also report an additional experiment, where we train a model on CIFAR-100 using the
PHuber-CE loss with τ = 50. This corresponds to linearizing the base loss at probability
threshold 0.02.

Computational requirements — We use a Nvidia RTX 2080 Ti GPU to train these models. With
full precision training, a run on CIFAR-10 takes approximately 11 hours, while a run on
CIFAR-100 takes approximately 4 hours, due to the lower amount of epochs and higher
batch size. In order to accelerate the training process, we implement mixed precision
training [28], which results in a 2x speed-up with no decrease in accuracy compared to
full precision training.
Fully reproducing the authorsʼ experiments required training each model 72 times, re-
sulting in a total training time of around 400 hours for the CIFAR-10 experiments, and
around 150 hours for the CIFAR-100 experiments.

Results — Our results are reported in Table 2, and a comparison with the original paperʼs
results can be found in Figure 3 and Figure 4.
On CIFAR-10, our reproduction achieves comparable or better results than the original
paper for nearly all configurations, except for the Linear, GCE and PHuber-GCE losses
which perform worse for ρ = 0.6. Surprisingly, the CE loss with gradient clipping per-
forms considerably better than what was reported in the presence of label noise, achiev-
ing the second-highest accuracy for ρ = 0.6, behind PHuber-CE. Similar to the original
paperʼs results, PHuber-CE with τ = 2 is competitive with CE in the absence of label
noise, and achieves very good results under label noise, outperforming all the other
losses. Notably, in our reproduction, PHuber-CE outperforms the linear loss for ρ = 0.4,
which was not the case in the original paper.
On CIFAR-100, our reproduction achieves better results than the original paper for nearly
all configurations. Most notably, the accuracy of the CE, GCE and PHuber-GCE losses
are noticeably better at all levels of noise corruption. As in the original paper, PHuber-
GCE with τ = 10 achieves the best accuracy out of all losses for ρ = 0.4 and ρ = 0.6,
and performs comparably to GCE for ρ = 0.0 and ρ = 0.2. Unlike the paperʼs results,
PHuber-CE with τ = 10 performs quite poorly compared to CE, even in settings with

2In the ResNet paper, He et al. also propose ResNet architectures suited for CIFAR-10 classification, such
as the ResNet-44 and ResNet-56, which have fewer filters per layer compared to the implementations from Liu
[20], resulting in faster training at the cost of lower accuracy. These ResNet architectures were not used in our
reproduction as the authors specifically mentioned using a ResNet-50.

3In the original paper, the weight decay is mistakenly reported as 5 × 10−3, and it was not specified that
the type of momentum used was Nesterov momentum. These updated hyperparameters were obtained from
the authors, after informing them of our difficulty reproducing their experiments with the values from the
paper.

4See previous footnote.




high levels of label noise where it should supposedly perform well. However, with our
additional experiment using PHuber-CE with τ = 50, we show that there exist values of
τ for which PHuber-CE performs comparably to CE in the noise-free case, and outper-
forms CE at high levels of label noise.

Dataset

Loss function

CIFAR-10

CIFAR-100

CE
CE + clipping
Linear
GCE
PHuber-CE τ = 2
PHuber-GCE τ = 10

CE
CE + clipping
Linear
GCE
PHuber-CE τ = 10
PHuber-GCE τ = 10
PHuber-CE τ = 50

ρ = 0.0
95.8 ± 0.1
89.3 ± 0.0
94.1 ± 0.1
95.3 ± 0.0
94.8 ± 0.0
95.4 ± 0.1
75.4 ± 0.3
23.5 ± 0.2
13.7 ± 0.7
73.3 ± 0.2
60.6 ± 1.1
72.7 ± 0.1
75.4 ± 0.2

ρ = 0.2
84.0 ± 0.3
82.6 ± 1.6
91.4 ± 0.5
92.5 ± 0.1
92.8 ± 0.2
92.2 ± 0.2
62.2 ± 0.4
20.4 ± 0.4
8.2 ± 0.3
68.5 ± 0.3
54.8 ± 1.2
68.4 ± 0.1
65.9 ± 0.2

ρ = 0.4
67.8 ± 0.3
78.7 ± 0.2
86.0 ± 2.4
82.4 ± 0.1
87.8 ± 0.2
81.5 ± 0.2
45.8 ± 0.9
16.2 ± 0.5
5.9 ± 0.7
59.5 ± 0.5
43.1 ± 1.1
60.2 ± 0.2
49.1 ± 0.2

ρ = 0.6
44.0 ± 0.2
67.6 ± 0.1
58.6 ± 5.2
53.3 ± 0.3
73.2 ± 0.2
54.3 ± 0.5
26.7 ± 0.1
12.9 ± 0.1
3.9 ± 0.3
40.3 ± 0.4
24.3 ± 0.8
42.2 ± 0.4
26.9 ± 0.0

Table 2. Reproduction of the CIFAR-10 and CIFAR-100 experiments. The mean and standard error
of the test accuracy over 3 trials is reported. The highlighted cells correspond to the best perform-
ing loss at a given ρ. CIFAR-100 PHuber-CE with τ = 50 is an additional experiment that was not
performed in the original paper.

Figure 3. Test accuracy of ResNet-50 on CIFAR-10

Figure 4. Test accuracy of ResNet-50 on CIFAR-100


CECE + clippingLinearGCEPHuber-CEPHuber-GCE020406080100Accuracy92.488.391.391.791.692.095.889.394.195.394.895.4ρ = 0.0CECE + clippingLinearGCEPHuber-CEPHuber-GCE02040608010072.468.788.288.488.688.584.082.691.492.592.892.2ρ = 0.2CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function020406080100Accuracy61.456.783.880.883.680.867.878.786.082.487.881.5ρ = 0.4CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function02040608010040.644.269.360.072.262.644.067.658.653.373.254.3ρ = 0.6paperoursCECE + clippingLinearGCEPHuber-CEPHuber-GCE020406080Accuracy66.628.812.170.166.269.875.423.513.773.360.672.7ρ = 0.0CECE + clippingLinearGCEPHuber-CEPHuber-GCE02040608049.720.66.663.956.264.462.220.48.268.554.868.4ρ = 0.2CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function020406080Accuracy29.914.75.752.044.452.445.816.25.959.543.160.2ρ = 0.4CECE + clippingLinearGCEPHuber-CEPHuber-GCELoss function02040608011.49.03.629.918.531.526.712.93.940.324.342.2ρ = 0.6paperours

## 5 Discussion

We now discuss whether our experimental results support the claims of the paper.
For the Long and Servedio experiment, when reusing exactly the parameters described
in the paper and in the authorsʼ clarifications, our results do not perfectly match those
from the original paper. After experimenting with some of the parameters, we did find
values that produce results nearly identical to those shown in the paper. Nonetheless,
these results still support the claim the authors made for the synthetic experiments,
namely, that there exist label noise scenarios for both the Long and Servedio [9] setting
and the Ding [10] setting which defeat a Huberised but not a partially Huberised loss.
While we made a considerable effort to ensure that our implementation matches the
paperʼs description, the difference in results could be due to some minor differences in
our implementations, or to a difference in the random seeds used to sample from the
mixture model and flip the labels.
For the MNIST experiment, all losses, except for CE with clipping, perform comparably,
achieving very high accuracy for all levels of label noise. This differs from the results
of the original paper, where CE and linear losses were affected by label noise. As a
result, it is difficult to support or reject any claim made regarding these losses with this
experiment.
For both the CIFAR-10 and CIFAR-100 experiments, our results differ even after fixing
the hyperparameters which were accidentally misreported in the original paper, with
our implementation yielding a noticeably higher test accuracy for the CE loss with clip-
ping on CIFAR-10, and the CE, GCE and PHuber-GCE losses on CIFAR-100. This is likely
due to the ResNet-50 architecture used, as the generally higher accuracy could be ex-
plained if our model happens to have a higher number of parameters than theirs. The
deep learning framework used could also lead to different results, as the authors men-
tioned using TensorFlow while we used PyTorch. Finally, this could also be caused by
the random seed used to add label noise, although we did not notice any significant
difference in results when changing this seed.
For the CIFAR-10 experiment, our reproduction supports the claim that for these specific
hyperparameters, partially Huberised losses are competitive with the base loss in the
noise-free case and can outperform it under label noise. In addition, this experiment
also shows that PHuber-CE can be very effective at mitigating symmetric label noise, as
it performs considerably better than the representative noise-robust losses at high levels
of label noise.
For the CIFAR-100 experiment, our reproduction shows that PHuber-GCE loss with τ =
10 is competitive with the base loss (GCE) in the noise-free case and can outperform it
at high levels of label noise, which supports the aforementioned claim. However, this
claim does not hold for the PHuber-CE loss with τ = 10, which performs worse than
CE in all cases. Despite that, we show with our additional experiment that there exists
a value of τ for which the PHuber-CE loss performs comparably to CE in the noise-free
case, and improves upon it under label noise.
Our additional experiment shows that the value of τ plays a crucial role in the perfor-
mance of partially Huberised losses. Both the PHuber-CE and GCE losses interpolate
between the linear and the CE loss. PHuber-CE and GCE mimic the linear loss for τ → 1
and α = 1 respectively, while for τ → +∞ and α → 0, they mimic the CE loss. As the
linear loss fails to train properly in our CIFAR-100 experiment, it is expected to obtain
poor results for these losses if the tunable parameter used makes them too similar to the
linear loss. As PHuber-GCE combines both of these losses, it can also perform poorly in
such a scenario. Furthermore, the CE loss with gradient clipping also has a tunable pa-
rameter which strongly affects performance, as our reproduction shows that for a max
norm τ = 0.1, CE with clipping can perform significantly better than CE on CIFAR-10,
and significantly worse on CIFAR-100.
In order to properly compare these losses, it would therefore be of interest to find, for




each level of label noise, the tunable parameter values for which they perform best, by
using random search or a hyperparameter tuning framework such as Optuna [29] on a
validation set. While such a hyper-parameter search has a high computational cost, it
would offer some valuable insights on how well each of these losses performs, and how
sensitive they are to changes to their tunable parameters. We leave such exploration for
future work.

## 6 Conclusion

In this work, we fully re-implement the experiments performed in Menon et al. [3]. For
the synthetic experiments, our results differ when using the exact values described in
the paper, although they still support the main claim, and by slightly modifying some ex-
periment settings, we obtain results almost identical to those of the original paper. Our
results also differ for the deep learning experiments, with some of the baselines per-
forming better than described. Nonetheless, these experiments still support the claim
that partially Huberised losses perform well on real-world datasets subject to label noise.
Our additional experiment also provides further insight on the performance of partially
Huberised losses, as it empirically shows that the value of τ can play an important role
in the performance of models trained with these losses. We thus believe it would be
of interest to perform further experiments focused on tuning these losses for different
levels of label noise, although this would incur a relatively high computational cost.

References

1.

2.

3.

4.

5.

6.

7.

8.

9.

Y. Bengio, P. Simard, and P. Frasconi. “Learning long-term dependencies with gradient descent is difﬁcult.” In:
IEEE transactions on neural networks 5.2 (1994), pp. 157–166.
J. Zhang, T. He, S. Sra, and A. Jadbabaie. “Analysis of Gradient Clipping and Adaptive Scaling with a Relaxed
Smoothness Condition.” In: arXiv preprint arXiv:1905.11881 (2019).
A. K. Menon, A. S. Rawat, S. Kumar, and S. Reddi. “Can gradient clipping mitigate label noise?” In: International
Conference on Learning Representations (ICLR). 2020.
A. Ekholm and J. Palmgren. “A model for a binary response with misclassiﬁcations.” In: GLIM 82: Proceedings
of the international conference on generalised linear models. Springer. 1982, pp. 128–143.
A. Menon, B. Van Rooyen, C. S. Ong, and B. Williamson. “Learning from corrupted binary labels via class-
probability estimation.” In: International Conference on Machine Learning. PMLR. 2015, pp. 125–134.
Z. Zhang and M. R. Sabuncu. “Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy
Labels.” In: arXiv:1805.07836 [cs, stat] (Nov. 2018). arXiv: 1805.07836. URL: http://arxiv.org/abs/1805.07836
(visited on 
B. van Rooyen, A. K. Menon, and R. C. Williamson. “Learning with Symmetric Label Noise: The Importance of
Being Unhinged.” In: arXiv:1505.07634 [cs] (May 2015). arXiv: 1505.07634. URL: http://arxiv.org/abs/1505.
07634 (visited on 
P. J. Huber. “Robust Estimation of a Location Parameter.” In: The Annals of Mathematical Statistics 35.1
(1964). Publisher: Institute of Mathematical Statistics, pp. 73–101. URL: https : / / www . jstor . org / stable /
2238020 (visited on 
P. M. Long and R. A. Servedio. “Random classiﬁcation noise defeats all convex potential boosters.” en. In:
Machine Learning 78.3 (Mar. 2010), pp. 287–304. DOI: 10.1007/s10994-009-5165-z. URL: https://doi.org/10.
1007/s10994-009-5165-z (visited on 

10. N. Ding. “Statistical machine learning in the t-exponential family of distributions.” PhD thesis. Jan. 2013. URL:

11.

12.

https://docs.lib.purdue.edu/dissertations/AAI3591196.
C. R. Harris et al. “Array programming with NumPy.” en. In: Nature 585.7825 (Sept. 2020). Number: 7825 Pub-
lisher: Nature Publishing Group, pp. 357–362. DOI: 10.1038/s41586-020-2649-2. URL: https://www.nature.
com/articles/s41586-020-2649-2 (visited on 
P. Virtanen et al. “SciPy 1.0: fundamental algorithms for scientiﬁc computing in Python.” en. In: Nature Meth-
ods 17.3 (Mar. 2020). Number: 3 Publisher: Nature Publishing Group, pp. 261–272. DOI: 10.1038/s41592-019-
0686-2. URL: https://www.nature.com/articles/s41592-019-0686-2 (visited on 




13.

14.

15.

16.

17.
18.

19.

20.

21.

22.

O. Yadan. Hydra - A framework for elegantly conﬁguring complex applications. 2019. URL: https://github.
com/facebookresearch/hydra.
A. Paszke et al. “PyTorch: An Imperative Style, High-Performance Deep Learning Library.” In: arXiv:1912.01703
[cs, stat] (Dec. 2019). arXiv: 1912.01703. URL: http://arxiv.org/abs/1912.01703 (visited on 
Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner. “Gradient-based learning applied to document recognition.” In:
Proceedings of the IEEE 86.11 (Nov. 1998). Conference Name: Proceedings of the IEEE, pp. 2278–2324. DOI:
10.1109/5.726791.
D. P. Kingma and J. Ba. “Adam: A Method for Stochastic Optimization.” In: arXiv:1412.6980 [cs] (Jan. 2017).
arXiv: 1412.6980. URL: http://arxiv.org/abs/1412.6980 (visited on 12/16/2020).
A. Krizhevsky and G. Hinton. “Learning Multiple Layers of Features from Tiny Images.” en. In: (2009), p. 60.
S. Zagoruyko and N. Komodakis. “Wide Residual Networks.” en. In: Procedings of the British Machine Vision
Conference 2016. York, UK: British Machine Vision Association, 2016, pp. 87.1–87.12. DOI: 10.5244/C.30.87.
URL: http://www.bmva.org/bmvc/2016/papers/paper087/index.html (visited on 12/16/2020).
K. He, X. Zhang, S. Ren, and J. Sun. “Deep Residual Learning for Image Recognition.” In: arXiv:1512.03385 [cs]
(Dec. 2015). arXiv: 1512.03385. URL: http://arxiv.org/abs/1512.03385 (visited on 
K. Liu. kuangliu/pytorch-cifar. original-date: 2017-01-21T05:43:20Z. Dec. 2017. URL: https : / / github . com /
kuangliu/pytorch-cifar (visited on 
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. “ImageNet: A Large-Scale Hierarchical Image
Database.” In: CVPR09. 2009.
T. DeVries and G. W. Taylor. “Improved Regularization of Convolutional Neural Networks with Cutout.” In:
arXiv:1708.04552 [cs] (Nov. 2017). arXiv: 1708.04552. URL: http : / / arxiv . org / abs / 1708 . 04552 (visited on


23. H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz. “mixup: Beyond Empirical Risk Minimization.” In:
arXiv:1710.09412 [cs, stat] (Apr. 2018). arXiv: 1710.09412. URL: http://arxiv.org/abs/1710.09412 (visited on

J. Li, R. Socher, and S. C. H. Hoi. “DivideMix: Learning with Noisy Labels as Semi-supervised Learning.” In:
arXiv:2002.07394 [cs] (Feb. 2020). arXiv: 2002.07394. URL: http : / / arxiv . org / abs / 2002 . 07394 (visited on


24.

26.

25. M. R. Zhang, J. Lucas, G. Hinton, and J. Ba. “Lookahead Optimizer: k steps forward, 1 step back.” In:
arXiv:1907.08610 [cs, stat] (Dec. 2019). arXiv: 1907.08610. URL: http://arxiv.org/abs/1907.08610 (visited on

Y. E. Nesterov. “A method for solving the convex programming problem with convergence rate O(1/k^2).” In:
Dokl. Akad. Nauk SSSR 269 (1983), pp. 543–547. URL: https://ci.nii.ac.jp/naid/10029946121/ (visited on
10/24/2020).
I. Sutskever, J. Martens, G. Dahl, and G. Hinton. “On the importance of initialization and momentum in deep
learning.” en. In: (2013), p. 14.
P. Micikevicius et al. “Mixed Precision Training.” en. In: (Oct. 2017). URL: https://arxiv.org/abs/1710.03740v3
(visited on 12/16/2020).
T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama. Optuna: A Next-generation Hyperparameter Optimiza-
tion Framework. 2019. arXiv:1907.10902 [cs.LG].

29.

27.

28.




A Decision boundaries in the Long and Servedio experiment

Huberised.png
Huberised.bb

(a) Logistic

(b) Huberised

(c) Partially Huberised

Figure 5. Decision boundaries in the reproduced Long and Servedio [9] experiment, with label
noise flip probability ρ = 0.2. The logistic and Huberised logistic loss misclassify samples gener-
ated from the two penalizer Gaussians centered around ±(γ, −γ), resulting in 50% test accuracy.
The partially Huberised logistic loss does not succumb to label noise, achieving near-perfect dis-
crimination.

B Effect of the label noise seed on the real-world experiments

In the original paper [3], all trials use the same corrupted dataset for each flip probability
ρ. Table 3 shows the results obtained on a subset of our experiments when varying the
random seed used to generate label noise.

Label
noise

Dataset

Loss function

Seed 0

Seed 1

Seed 2

Seed 3

MNIST

ρ = 0.6

CIFAR-10

CIFAR-100

CE
PHuber-GCE
CE
PHuber-GCE
CE
PHuber-GCE

98.0 ± 0.1

44.0 ± 0.2
54.3 ± 0.5
26.7 ± 0.1
42.2 ± 0.4

97.9 ± 0.0
97.8 ± 0.1
43.8 ± 0.5
54.0 ± 0.7
27.1 ± 0.1
43.0 ± 0.2

97.9 ± 0.0

44.1 ± 0.2
53.7 ± 0.5
27.0 ± 0.5
42.1 ± 0.6

97.9 ± 0.1

43.2 ± 0.3
54.3 ± 0.2
26.9 ± 0.1
41.9 ± 0.1

Original
paper
91.1 ± 0.6
97.8 ± 0.0
40.6 ± 0.3
62.6 ± 0.2
11.4 ± 0.2
31.5 ± 0.8

Table 3. Impact of the random seed used to generate label noise. The mean and standard error of
the test accuracy over 3 trials is reported. This subset of experiments was chosen to include both
a baseline and a partially Huberised loss, at the highest level of label noise. The results obtained
are consistent across seeds, and differ from the original paperʼs results.

---
**Source PDF:** `54f4f9dd2a9a.pdf` (2021_13_article.pdf)  
**URL:** https://zenodo.org/record/4834744/files/article.pdf
