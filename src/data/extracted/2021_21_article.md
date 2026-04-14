R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020


Varun Sundar1, ID and Rajat Vadiraj Dwaraknath2, ID
1University of Wisconsin Madison, Wisconsin, USA – 2Stanford University, California, USA

Edited by
Koustuv Sinha,
Jesse Dodge

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4835564

Reproducibility Summary

Scope of Reproducibility

For a fixed parameter count and compute budget, the proposed algorithm (RigL) claims
to directly train sparse networks that match or exceed the performance of existing dense-
to-sparse training techniques (such as pruning). RigL does so while requiring constant
Floating Point Operations (FLOPs) throughout training. The technique obtains state-of-
the-art performance on a variety of tasks, including image classification and character-
level language-modelling.

Methodology

We implement RigL from scratch in Pytorch using boolean masks to simulate unstruc-
tured sparsity. We rely on the description provided in the original paper, and referred
to the authorsʼ code for only specific implementation detail such as handling overflow
in ERK initialization. We evaluate sparse training using RigL for WideResNet-22-2 on
CIFAR-10 and ResNet-50 on CIFAR-100, requiring 2 hours and 6 hours respectively per
training run on a GTX 1080 GPU.

Results

We reproduce RigLʼs performance on CIFAR-10 within 0.1% of the reported value. On
both CIFAR-10/100, the central claim holds—given a fixed training budget, RigL sur-
passes existing dynamic-sparse training methods over a range of target sparsities. By
training longer, the performance can match or exceed iterative pruning, while consum-
ing constant FLOPs throughout training. We also show that there is little benefit in tun-
ing RigLʼs hyper-parameters for every sparsity, initialization pair—the reference choice
of hyperparameters is often close to optimal performance.

Going beyond the original paper, we find that the optimal initialization scheme depends
on the training constraint. While the Erdos-Renyi-Kernel distribution outperforms Ran-
dom distribution for a fixed parameter count, for a fixed FLOP count, the latter performs
better. Finally, redistributing layer-wise sparsity while training can bridge the perfor-
mance gap between the two initialization schemes, but increases computational cost.


Code is available at https://github.com/varun19299/rigl-reproducibility. – SWH swh:1:dir:0707870fafa16ef60dc64071e1aed482e373e75f.
Open peer review is available at https://openreview.net/forum?id=riCIeP6LzEE.




What was easy

The authors provide code for most of the experiments presented in the paper. The code
was easy to run and allowed us to verify the correctness of our re-implementation. The
paper also provided a thorough and clear description of the proposed algorithm without
any obvious errors or confusing exposition.

What was difﬁcult

Tuning hyperparameters involved multiple random seeds and took longer than antic-
ipated. Verifying the correctness of a few baselines was tricky and required ensuring
that the optimizerʼs gradient (or momentum) buffers were sparse (or dense) as specified
by the algorithm. Compute limits restricted us from evaluating on larger datasets such
as Imagenet.

Communication with original authors

We had responsive communication with the original authors, which helped clarify a
few implementation and evaluation details, particularly regarding the FLOP counting
procedure.




## 1 Introduction

Sparse neural networks are a promising alternative to conventional dense networks—
having comparatively greater parameter efficiency and lesser floating-point operations
(FLOPs) (Han et al., Ashby et al., Srinivas, Subramanya, and Venkatesh Babu1,2,3). Un-
fortunately, present techniques to produce sparse networks of commensurate accuracy
involve multiple cycles of training dense networks and subsequent pruning. Conse-
quently, such techniques offer no advantage over training dense networks, either com-
putationally or memory-wise.

In the paper Evci et al.4, the authors propose RigL, an algorithm for training sparse net-
works from scratch. The proposed method outperforms both prior art in training sparse
networks, as well as existing dense-to-sparse training algorithms. By utilising dense gra-
dients only during connectivity updates and avoiding any global sparsity redistribution,
RigL can maintain a fixed computational cost and parameter count throughout training.

As a part of the ML Reproducibility Challenge, we replicate RigL from scratch and in-
vestigate if dynamic-sparse training confers significant practical benefits compared to
existing sparsifying techniques.

## 2 Scope of reproducibility

In order to verify the central claims presented in the paper we focus on the following
target questions:

• Does RigL outperform existing sparse-to-sparse training techniques—such as SET
(Mocanu et al.5) and SNFS (Dettmers and Zettlemoyer6)—and match the accuracy
of dense-to-sparse training methods such as iterative pruning (Zhu and Gupta7)?

• RigL requires two additional hyperparameters to tune. We investigate the sensitiv-
ity of final performance to these hyperparameters across a variety of target sparsi-
ties (Section 5.3).

• How does the choice of sparsity initialization affect the final performance for a

fixed parameter count and a fixed training budget (Section 6.1)?

• Does redistributing layer-wise sparsity during connection updates (Dettmers and
Zettlemoyer6) improve RigLʼs performance? Can the final layer-wise distribution
serve as a good sparsity initialization scheme (Section 6.2)?

## 3 Methodology

The authors provide publicly accessible code1 written in Tensorflow (Abadi et al.8). To
gain a better understanding of various implementation aspects, we opt to replicate RigL
in Pytorch (Paszke et al.9). Our implementation extends the open-source code2 of Dettmers
and Zettlemoyer6 which uses a boolean mask to simulate unstructured sparsity. Our
source code is publicly accessible on Github3 with training plots available on WandB4
(Biewald10).

1https://github.com/google-research/rigl
2https://github.com/TimDettmers/sparse_learning
3https://github.com/varun19299/rigl-reproducibility
4https://wandb.ai/ml-reprod-2020




Mask Initialization — For a network with L layers and total parameters N , we associate
each layer with a random boolean mask of sparsity sl, l ∈ [L]. The overall sparsity of the
network is given by S =
, where Nl is the parameter count of layer l. Sparsities
sl are determined by the one of the following mask initialization strategies:

l slNl
N

∑

• Uniform: Each layer has the same sparsity, i.e., sl = S ∀l. Similar to the original

authors, we keep the first layer dense in this initialization.

(

)

• Erdos-Renyi (ER): Following Mocanu et al.5, we set sl ∝

, where
Cin, Cout are the in and out channels for a convolutional layer and input and output
dimensions for a fully-connected layer.

1 − Cin+Cout
×Cout
Cin

• Erdos-Renyi-Kernel (ERK): Modifies the sparsity rule of convolutional layers in ER

(

)

initialization to include kernel height and width, i.e., sl ∝
a convolutional layer with Cin × Cout × w × h parameters.

1 − Cin+Cout+w+h
×Cout×w×h

Cin

, for

We do not sparsify either bias or normalization layers, since these have a negligible effect
on total parameter count.

Mask Updates — Every ∆T training steps, certain connections are discarded, and an equal
number are grown. Unlike SNFS (Dettmers and Zettlemoyer6), there is no redistribution
of layer-wise sparsity, resulting in constant FLOPs throughout training.

Pruning Strategy — Similar to SET and SNFS, RigL prunes f fraction of smallest magnitude
weights in each layer. As detailed below, the fraction f is decayed across mask update
steps, by cosine annealing:

f (t) =

(

α


1 + cos

))

(

tπ
Tend

(1)

where, α is the initial pruning rate and Tend is the training step after which mask updates
are ceased.

Growth Strategy — RigLʼs novelty lies in how connections are grown: during every mask
update, k connections having the largest absolute gradients among current inactive
weights (previously zero + pruned) are activated. Here, k is chosen to be the number
of connections dropped in the prune step. This requires access to dense gradients at
each mask update step. Since gradients are not accumulated (unlike SNFS), RigL does
not require access to dense gradients at every step. Following the paper, we initialize
newly activated weights to zero.

## 4 Experimental Settings

### 4.1 Model descriptions

For experiments on CIFAR-10 (Alex Krizhevsky11), we use a Wide Residual Network (Zagoruyko
and Komodakis12) with depth 22 and width multiplier 2, abbreviated as WRN-22-2. For
experiments on CIFAR-100 (Alex Krizhevsky11), we use a modified variant of ResNet-50
(He et al.13), with the initial 7 × 7 convolution replaced by two 3 × 3 convolutions (archi-
tecture details provided in the supplementary material).




Table 1. Test accuracy of reference and our implementations on CIFAR-10, tabulated for three dif-
ferent sparsities. Note that the runs listed here do not use a separate validation set while training.


Dense


Static (ERK)
Pruning


91.6
93.2
### 93.2 Ours

94.6


93.2
93.6
93.8

1 − s = 0.5


94.3
94.3
94.4

91.6
93.3
### 93.1 Original

94.1


92.9
93.5
93.8

1 − s = 0.5

94.2
94.1
94.3

### 4.2 Datasets and Training descriptions

We conduct our experiments on the CIFAR-10 and CIFAR-100 image classification datasets.
For CIFAR-10, we use a train/val/test split of 45k/5k/10k samples. In comparison, the au-
thors use no dedicated validation set, with 50k samples and 10k samples comprising
the train set and test set, respectively. This causes a slight performance discrepancy be-
tween our reproduction and the metrics reported by the authors (dense baseline has a
test accuracy of 93.4% vs 94.1% reported). However, our replication matches the paperʼs
performance when 50k samples are used for the train set (Table 4). We use a validation
split of 10k samples for CIFAR-100 as well.

On both datasets, we train models for 250 epochs each, optimized by SGD with momen-
tum. Our training pipeline uses standard data augmentation, which includes random
flips and crops. When training on CIFAR-100, we additionally include a learning rate
warmup for 2 epochs and label smoothening of 0.1 (Goyal et al.14). We also initialize
the last batch normalization layer (Ioffe and Szegedy15) in each BottleNeck block to 0,
following He et al.16.

### 4.3 Hyperparameters

RigL includes two additional hyperparameters (α, ∆T ) in comparison to regular dense
network training. In Sections 5.1 and 5.2, we set α = 0.3, ∆T = 100, based on the orig-
inal paper. Optimizer specific hyperparameters—learning rate, learning rate schedule,
and momentum—are also set according to the original paper. In Section 5.3, we tune
these hyperparameters with Optuna (Akiba et al.17). We also examine whether indivdu-
ally tuning the learning rate for each sparsity value offers any significant benefit.

### 4.4 Baseline implementations

We compare RigL against various baselines in our experiments: SET (Mocanu et al.5),
SNFS (Dettmers and Zettlemoyer6), and Magnitude-based Iterative-pruning (Zhu and
Gupta7). We also compare against two weaker baselines, viz., Static Sparse training and
Small-Dense networks. The latter has the same structure as the dense model but uses
fewer channels in convolutional layers to lower parameter count. We implement iter-
ative pruning with the pruning interval kept same as the masking interval for a fair
comparison.

### 4.5 Computational requirements

We run our experiments on a SLURM cluster node—equipped with 4 NVIDIA GTX1080
GPUs and a 32 core Intel CPU. Each experiment on CIFAR-10 and CIFAR-100 consumes
about 1.6 GB and 7 GB of VRAM respectively and is run for 3 random seeds to capture
performance variance. We require about 6 and 8 days of total compute time to produce




Table 2. WideResNet-22-2 on CIFAR10, tabulated for two density (1 − s) values. We group methods
by their FLOP requirement and in each group, we mark the best accuracy in bold. Similar to
Evci et al.4, we assume that algorithms utilize sparsity during training. All results are obtained by
methods implemented in our unified codebase.


Small Dense
Static
SET
RigL

SET (ERK)


Static2×
Lottery
SET2×
SNFS
SNFS (ERK)
SNFS2×
RigL2×
Pruning
RigL2× (ERK)

Dense Baseline


89.0 ± 0.35
89.1 ± 0.17
91.3 ± 0.47

92.2 ± 0.04

89.15 ± 0.17
90.4 ± 0.09
83.3 ± 15.33
92.4 ± 0.43
92.2 ± 0.2
92.3 ± 0.33
92.3 ± 0.25
92.6 ± 0.08
92.7 ± 0.37
93.4 ± 0.07


0.11x, 0.11x


0.17x, 0.17x
0.17x, 0.17x


0.45x, 0.13x

0.51x, 0.27x
0.52x, 0.28x
1.02x, 0.27x

0.32x,0.13x
0.34x, 0.17x


91.0 ± 0.07
91.2 ± 0.16
92.7 ± 0.28
92.6 ± 0.10
92.9 ± 0.16

91.2 ± 0.16
92.0 ± 0.31
93.0 ± 0.22
92.7 ± 0.20
92.8 ± 0.07
93.2 ± 0.14
93.0 ± 0.21
93.2 ± 0.27
93.3 ± 0.09


0.20x,0.20x


0.35x, 0.35x
0.35x, 0.35x

0.40x, 0.20x
0.68x,0.27x
0.41x, 0.20x
0.66x, 0.49x
0.66x, 0.49x
1.32x, 0.98x
0.41x, 0.20x
0.41x,0.27x
0.70x, 0.35x

9.45e8, 3.15e8

-

-

all results, including hyper-parameter sweeps and extended experiments, on CIFAR-10
and CIFAR-100 respectively.

## 5 Results

Given a fixed training FLOP budget, RigL surpasses existing dynamic sparse training
methods over a range of target sparsities, on both CIFAR-10 and 100 (Sections 5.1, 5.2).
By training longer, RigL matches or marginally outperforms iterative pruning. However,
unlike pruning, its FLOP consumption is constant throughout. This a prime reason for
using sparse networks, and makes training larger networks feasible. Finally, as evalu-
ated on CIFAR-10, the original authorsʼ choice of hyper-parameters are close to optimal
for multiple target sparsities and initialization schemes (Section 5.3).

### 5.1 WideResNet-22 on CIFAR-10

Results on the CIFAR-10 dataset are provided in Table 2. Tabulated metrics are averaged
across 3 random seeds and reported with their standard deviation. All sparse networks
use random initialization, unless indicated otherwise.

While SET improves over the performance of static sparse networks and small-dense
networks, methods utilizing gradient information (SNFS, RigL) obtain better test accu-
racies. SNFS can outperform RigL, but requires a much larger training budget, since it
(a) requires dense gradients at each training step, (b) redistributes layer-wise sparsity
during mask updates. For all sparse methods, excluding SNFS, using ERK initialization
improves performance, but with increased FLOP consumption. We calculate theoreti-
cal FLOP requirements in a manner similar to Evci et al.4 (exact procedure is described




Figure 1. Test Accuracy vs Sparsity on CIFAR-10, plotted for Random initialization (left), ERK initial-
ization (center), and for training 2× longer (right). Owing to random growth, SET can be unstable
when training for longer durations with higher sparsities. Overall, RigL2× (ERK) achieves highest
test accuracy.

in the appendix).

Figure 1 contains test accuracies of select methods across two additional sparsity values:
(0.5, 0.95). At lower sparsities (higher densities), RigL matches the performance of the
dense baseline. Performance further improves by training for longer durations. Par-
ticularly, training RigL (ERK) twice as long at 90% sparsity exceeds the performance of
iterative pruning while requiring similar theoretical FLOPs. This validates the original
authorsʼ claim that RigL (a sparse-to-sparse training method) outperforms pruning (a
dense-to-sparse training method).

### 5.2 ResNet-50 on CIFAR100

Table 3 & Figure 2. Benchmarking sparse ResNet-
tabulated by performance
50s on CIFAR-100,
and cost (below), and plotted across densities
(right).
In each group below, RigL outperforms
or matches existing sparse-to-sparse and dense-
to-sparse methods. Notably, RigL3× at 90% spar-
sity and RigL2× at 80% sparsity surpass iterative
pruning with similar FLOP consumption. RigL2×
(ERK) further improves performance but requires
a larger training budget.


Static
Small Dense
SET
RigL

Static (ERK)
SET (ERK)


SNFS
SNFS (ERK)
Pruning
RigL2×
Lottery
RigL3×
RigL2× (ERK)

Dense Baseline


69.7 ± 0.42
70.8 ± 0.22
71.4 ± 0.35
71.8 ± 0.33
71.5 ± 0.18
72.3 ± 0.39
72.6 ± 0.37
72.3 ± 0.20
73.0 ± 0.33
73.1 ± 0.32
73.1 ± 0.71
73.6 ± 0.32
73.7 ± 0.16
73.6 ± 0.05
74.7 ± 0.38


0.11x, 0.11x


0.22x, 0.22x
0.22x, 0.22x
0.23x, 0.22x

0.58x, 0.37x
0.59x, 0.38x
0.36x,0.11x

0.62x,0.11x
0.30x, 0.10x
0.46x, 0.22x


72.3 ± 0.30
72.6± 0.93
73.4 ± 0.45
73.5 ± 0.04
73.2 ± 0.39
73.5 ± 0.25
73.4 ± 0.15
73.9 ± 0.20
73.9 ± 0.27
73.8 ± 0.23
74.0 ± 0.24
74.2 ± 0.41
74.2 ± 0.23
74.4 ± 0.10


0.20x,0.20x


0.70x, 0.55x
0.69x, 0.54x
0.45x,0.25x
0.41x, 0.20x
0.81x,0.25x
0.61x, 0.20x
0.76x, 0.38x

7.77e9, 2.59e9

-

-

We see similar trends when training sparse variants of ResNet-50 on the CIFAR-100 dataset
(Table 3, metrics reported as in Section 5.1). We also include a comparison against sparse
networks trained with the Lottery Ticket Hypothesis (Frankle and Carbin18) in Table
3—we obtain tickets with a commensurate performance for sparsities lower than 80%.


(a) Random initialization(b) ERK initialization(c) 2x longer(a) Random initialization(b) ERK initialization,  Extended training

Finally, the choice of initialization scheme affects the performance and FLOP consump-
tion by a greater extent than the method used itself, with the exception of SNFS (groups
1 and 2 in Table 3).

### 5.3 Hyperparameter Tuning

Table 4. Reference vs Optimal (α, ∆T ) on CIFAR-10. Optimal hyperparameters are obtained by
tuning with a TPE sampler in Optuna. The difference between the reference and optimal perfor-
mance is small, indicating that there is not a significant benefit in tuning (α, ∆T ) individually for
each initialization and sparsity configuration.

Density

Reference

Optimal

Initialization

(1 − s)

(α, ∆T )

Random
Random
Random

ERK
ERK
ERK

0.1
0.2
0.5

0.1
0.2
0.5


92.6 ± 0.10
93.3 ± 0.07


93.4 ± 0.14

(α, ∆T )

0.197, 50
0.448, 150
0.459, 550

0.416, 200
0.381, 950
0.287, 500


91.8 ± 0.17
92.8 ± 0.16
93.3 ± 0.18
92.4 ± 0.23
93.1 ± 0.21
93.8 ± 0.06

(α, ∆T ) vs Sparsities — To understand the impact of the two additional hyperparameters
included in RigL, we use a Tree of Parzen Estimator (TPE sampler, Bergstra et al.19) via
Optuna to tune (α, ∆T ). We do this for sparsities (1 − s) ∈ {0.1, 0.2, 0.5}, and a fixed
learning rate of 0.1. Additionally, we set the sampling domain for α and ∆T as [0.1, 0.6]
and {50, 100, 150, ..., 1000} respectively. We use 15 trials for each sparsity value, with our
objective function as the validation accuracy averaged across 3 random seeds.

Figure 3. Learning Rate vs Sparsity on CIFAR-10. Runs using a learning rate > 0.1 do not converge
and are not plotted here. There is little benefit in tuning the learning rate for each sparsity, and
0.1, 0.05 are good choices overall.


(a) ERK, 1−𝑠=0.1(b) ERK, 1−𝑠=0.2(c) ERK, 1−𝑠=0.5(d) Random, 1−𝑠=0.1(e) Random, 1−𝑠=0.2(f) Random, 1−𝑠=0.5

Table 4 shows the test accuracies of tuned hyperparameters. While the reference hyper-
parameters (original authors, α = 0.3, ∆T = 100) differ from the obtained optimal hy-
perparameters, the difference in performance is marginal, especially for ERK initializa-
tion. This in agreement with the original paper, which finds α ∈ {0.3, 0.5}, ∆T = 100 to
be suitable choices. We include contour plots detailing the hyperparameter trial space
in the supplementary material.

Learning Rate vs Sparsities — We further examine if the final performance improves by tun-
ing the learning rate (η) individually for each sparsity-initialization pair. We employ a
grid search over η ∈ {0.1, 0.05, 0.01, 0.005} and (α, ∆T ) ∈ {(0.3, 100), (0.4, 200), (0.4, 500),
(0.5, 750)}. As seen in Figure 3, η = 0.1 and η = 0.05 are close to optimal values for a
wide range of sparsities and initializations. Since these learning rates also correspond
to good choices for the Dense baseline, one can employ similar values when training
with RigL.

## 6 Results beyond Original Paper

### 6.1 Sparsity Distribution vs FLOP Consumption

Figure 4. Test Accuracy vs FLOP consumption of WideResNet-22-2 on CIFAR-10 and ResNet-50 on
CIFAR-100, compared for Random and ERK initializations. For the same FLOP budget, models
trained with ERK initialization must be more sparse, resulting in inferior performance.

While ERK initialization outperforms Random initialization consistently for a given tar-
get parameter count, it requires a higher FLOP budget. Figure 4 compares the two initial-
ization schemes across fixed training FLOPs. Theoretical FLOP requirement for Random
initialization scales linearly with density (1 − s), and is significantly lesser than ERKʼs
FLOP requirements. Consequently, Random initialization outperforms ERK initializa-
tion for a given training budget.

### 6.2 Effect of Redistribution

One of the main differences of RigL over SNFS is the lack of layer-wise redistribution dur-
ing training. We examine if using a redistribution criterion can be beneficial and bridge
the performance gap between Random and ERK initialization. Following Dettmers and
Zettlemoyer6, during every mask update, we reallocate layer-wise density proportional
to its average sparse gradient or momentum (RigL-SG, RigL-SM).

Table 5 shows that redistribution significantly improves RigL (Random), but not RigL
(ERK). We additionally plot the FLOP requirement against training steps and the final
sparsity distribution in Figure 5. The layer-wise sparsity distribution largely becomes
constant within a few epochs. The final distribution is similar, but more “extreme” than
ERK—wherever ERK exceeds/falls short of Random, redistribution does so by a greater


(a) WRN-22-2 on CIFAR 10(b) ResNet-50 on CIFAR100

Table 5. Effect of redistribution during RigL updates, evaluated on CIFAR10 and CIFAR100. By
utilising sparse gradient or sparse momentum based redistribution, RigL (Random) matches RigL
(ERK)ʼs performance. Among Random and ERK initialized experiments, we mark the best metrics
under each sparsity and dataset in bold.


Redistribution


CIFAR-10

CIFAR-100


RigL
RigL-SG
RigL-SM

-
Sparse Grad
Sparse Mmt


92.2 ± 0.17
92.2 ± 0.20


Random Initialization
92.9 ± 0.10
92.7 ± 0.25
92.9 ± 0.21


0.49x, 0.49x


ERK Initialization

71.8 ± 0.33
72.3 ± 0.12
72.6 ± 0.27


0.36x,0.35x
0.36x,0.36x

73.5 ± 0.04
73.7 ± 0.15
73.7 ± 0.35


RigL
RigL-SG
RigL-SM

-
Sparse Grad
Sparse Mmt


92.1 ± 0.19
92.27 ± 0.01

0.17x, 0.17x


92.7 ± 0.19
93.0 ± 0.13

0.35x, 0.35x
0.49x, 0.49x


72.6 ± 0.37
73.0 ± 0.13
72.6 ± 0.27

0.23x, 0.22x
0.37x,0.36x
0.37x, 0.37x

73.4 ± 0.15
74.2 ± 0.26
74.2 ± 0.13


RigL


-
-

90.3 ± 0.34
90.2 ± 0.57


91.0 ± 0.38
90.6 ± 0.56


67.6 ± 0.28
67.8 ± 0.73

0.36x, 0.36x
0.37x, 0.37x

68.9 ± 0.65
68.9 ± 0.47


Re-Initialization with RigL-SM (Random, ERK)

extent.

By allocating higher densities to 1 × 1 convolutions (convShortcut in Figure 5), redis-
tribution significantly increases the FLOP requirement—and hence, is not a preferred
alternative to ERK. Surprisingly, initializing RigL with the final sparsity distribution in a
manner similar to the Lottery Ticket Hypothesis results in subpar performance (group
3, Table 5).

Figure 5. Effect of redistribution on RigLʼs performance, evaluated using WideResNet-22-2 on
CIFAR10 at 80% sparsity.
(left) FLOPs required per forward pass, shown relative to the dense
baseline, rises quickly and saturates within a few epochs (~10k steps) for both sparse gradient
and sparse momentum based redistribution. (right) Comparison of the final density distribution
against Random and ERK counterparts. “b” refers to block and “l” layer here.

## 7 Discussion

Evaluated on image classification, the central claims of Evci et al.4 hold true—RigL out-
performs existing sparse-to-sparse training methods and can also surpass other dense-
to-sparse training methods with extended training. RigL is fairly robust to its choice of
hyperparameters, as they can be set independent of sparsity or initialization. We find
that the choice of initialization has a greater impact on the final performance and com-
pute requirement than the method itself. Considering the performance boost obtained
by redistribution, proposing distributions that attain maximum performance given a
FLOP budget could be an interesting future direction.


(b) Layer-wise density distribution(a) FLOP consumption vs train steps

For computational reasons, our scope is restricted to small datasets such as CIFAR-10/100.
RigLʼs applicability outside image classification—in Computer Vision and beyond (ma-
chine translation etc.) is not covered here.

What was easy — The authorsʼ code covered most of the experiments in their paper and
helped us validate the correctness of our replicated codebase. Additionally, the original
paper is quite complete, straightforward to follow, and lacked any major errors.

What was difﬁcult — Implementation details such as whether momentum buffers were ac-
cumulated sparsely or densely had a substantial impact on the performance of SNFS.
Finding the right ϵ for ERK initialization required handling of edge cases—when a layerʼs
capacity is exceeded. Hyperparameter tuning (α, ∆T ) involved multiple seeds and was
compute-intensive.

Communication with original authors — We acknowledge and thank the original authors for
their responsive communication, which helped clarify a great deal of implementation
and evaluation specifics. Particularly, FLOP counting for various methods while taking
into account the changing sparsity distribution. We also discussed experiments extend-
ing the original paper—as to whether the authors had carried out a similar study before.

References

1.

S. Han, X. Liu, H. Mao, J. Pu, A. Pedram, M. A. Horowitz, and W. J. Dally. “EIE: efﬁcient inference engine on
compressed deep neural network.” In: ACM SIGARCH Computer Architecture News 44.3 (2016), pp. 243–
254.

2. M. Ashby, C. Baaij, P. Baldwin, M. Bastiaan, O. Bunting, A. Cairncross, C. Chalmers, L. Corrigan, S. Davis, N. van

3.

4.

5.

6.

Doorn, et al. “Exploiting Unstructured Sparsity on Next-Generation Datacenter Hardware.” In: (2017).
S. Srinivas, A. Subramanya, and R. Venkatesh Babu. “Training Sparse Neural Networks.” In: Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops. July 2017.
U. Evci, T. Gale, J. Menick, P. S. Castro, and E. Elsen. “Rigging the Lottery: Making All Tickets Winners.” In:
Proceedings of Machine Learning and Systems (ICML). July 2020.
D. C. Mocanu, E. Mocanu, P. Stone, P. H. Nguyen, M. Gibescu, and A. Liotta. “Scalable Training of Artiﬁcial Neural
Networks with Adaptive Sparse Connectivity inspired by Network Science.” In: Nature Communications (2018).
DOI: 10.1038/s41467-018-04316-3.
T. Dettmers and L. Zettlemoyer. Sparse Networks from Scratch: Faster Training without Losing Performance.
2020. URL: https://openreview.net/forum?id=ByeSYa4KPS.

7. M. Zhu and S. Gupta. “To Prune, or Not to Prune: Exploring the Efﬁcacy of Pruning for Model Compression.” In:

Proceedings of the International Conference on Learning Representations (ICLR). Apr. 2018.

8. M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, M. Isard, et al. “Ten-
sorflow: A system for large-scale machine learning.” In: 12th {USENIX} Symposium on Operating Systems
Design and Implementation ({OSDI} 16). 2016, pp. 265–283.
A. Paszke et al. “PyTorch: An Imperative Style, High-Performance Deep Learning Library.” In: Advances in Neu-
ral Information Processing Systems. Dec. 2019.
L. Biewald. Experiment Tracking with Weights and Biases. Software available from wandb.com. 2020. URL:
https://www.wandb.com/.

9.

10.

11. G. H. Alex Krizhevsky. Learning multiple layers of features from tiny images. Tech. rep. 2009.
12.

S. Zagoruyko and N. Komodakis. “Wide Residual Networks.” In: Proceedings of the British Machine Vision
Conference (BMVC). Sept. 2016.
K. He, X. Zhang, S. Ren, and J. Sun. “Deep Residual Learning for Image Recognition.” In: Proceedings of the
IEEE Conference on Computer Vision and Pattern Recognition (CVPR). June 2016.
P. Goyal, P. Dollár, R. Girshick, P. Noordhuis, L. Wesolowski, A. Kyrola, A. Tulloch, Y. Jia, and K. He. “Accurate,
large minibatch sgd: Training imagenet in 1 hour.” In: arXiv preprint arXiv:1706.02677 (2017).
S. Ioffe and C. Szegedy. “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Co-
variate Shift.” In: International Conference on Machine Learning (ICML). July 2015.

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

T. He, Z. Zhang, H. Zhang, Z. Zhang, J. Xie, and M. Li. “Bag of Tricks for Image Classiﬁcation with Convolutional
Neural Networks.” In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR). June 2019.
T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama. “Optuna: A Next-generation Hyperparameter Optimization
Framework.” In: Proceedings of the 25rd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining. Aug. 2019.
J. Frankle and M. Carbin. “The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks.” In: Pro-
ceedings of the International Conference on Learning Representations (ICLR). Apr. 2018.
J. Bergstra, R. Bardenet, Y. Bengio, and B. Kégl. “Algorithms for Hyper-Parameter Optimization.” In: Advances
in Neural Information Processing Systems. Dec. 2011.
O. Russakovsky et al. “ImageNet Large Scale Visual Recognition Challenge.” In: International Journal of Com-
puter Vision (IJCV) 115.3 (2015), pp. 211–252. DOI: 10.1007/s11263-015-0816-y.
S. Gray, A. Radford, and D. P. Kingma.
arXiv:1711.09224 3 (2017).
D. Teja Vooturi, G. Varma, and K. Kothapalli. “Dynamic Block Sparse Reparameterization of Convolutional Neu-
ral Networks.” In: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Work-
shops. Oct. 2019.

“Gpu kernels for block-sparse weights.”

In: arXiv preprint




A Architecture Speciﬁc Details—ResNet-50 on CIFAR100

Table 6. ResNet-50 architecture used on CIFAR100. Building blocks are shown in brackets, with
the numbers of blocks stacked. Downsampling is performed by conv3_1, conv4_1, and conv5_1
with a stride of 2.

Layer Name Output Size

conv1

conv2_x

32×32

32×32

conv3_x

16×16

conv4_x

conv5_x

8×8

4×4

1×1

ResNet-50
3×3, 64, no stride


















1×1, 64
3×3, 64
1×1, 256

1×1, 128
3×3, 128
1×1, 512

1×1, 256
3×3, 256
1×1, 1024

1×1, 512
3×3, 512
1×1, 2048

×3



×4



×6



×3

average pool, 100-d fc, softmax

FLOPs

2.59e9

We use a variant of the originally proposed ResNet architecture (He et al.13). Particularly,
we replace the initial 7 × 7 conv layer with a 3 × 3 conv layer. Here, “conv layer” refers
to convolution followed by batchnorm (Ioffe and Szegedy15) and ReLU activation. This
is intended to not excessively downsample the image—CIFAR-100 (Alex Krizhevsky11)
has images of dimensions 32 × 32, compared to Imagenetʼs (Russakovsky et al.20) 224 ×
224. Each block used (conv2_x, conv3_x, etc.) is a bottleneck block, and uses the conv-
batchnorm-ReLU ordering.

B FLOP Counting Procedure

Following Evci et al.4, we base our counting procedure on the Micronet Challenge5,
which was conducted as a part of NeurIPS 2019. Support for unstructured sparsity is
assumed while computing the number of additions and multiplication operations. The
sum of these two gives us the theoretical FLOPs for a single forward pass through the
model.

Concretely, let the FLOPs required for a forward pass through a dense model be fd and
the corresponding for a sparse model (or small-dense model) be fs. Then, the FLOPs for
training a dense model are 3fd—since the backward pass involves computing gradients
with respect to each weight and activation. fs can be computed for a model given its
sparsity distribution via the counting procedure. The FLOPs required to train a sparse
model depend on the technique used, as detailed below.

5https://micronet-challenge.github.io/




B.1 Inference FLOPs

Small-Dense, RigL, SET, Static — These methods involve constant layer-wise sparsity through-
out training, hence the FLOP count can be determined during any step. The FLOP count
for Random initialized models are (1 − s) times the Dense FLOPs.

SNFS, Pruning — Both methods involve varying layer-wise sparsity during training, and
hence non-constant FLOP consumption. The final weights are used to determine infer-
ence FLOPs in this case.

B.2 Train FLOPs

Small-Dense, Static — Dense gradients are not required by these models, and hence have
a train FLOP count of 3fs.

SET — Dense gradients are not required, and random growth can be implemented quite
efficiently. Thus, the train FLOP count is 3fs.

RigL — Dense gradients are required only every ∆T steps, hence the corresponding train
FLOP count is: 3∆T fs+2fs+fd
. We note that since ∆T is typically set between 100–1000,
∆T +1
the preceding expression is quite close to 3fs.

SNFS — Dense gradients are required at each training step, resulting in 2fs + fd FLOPs
consumed at each step. Since the sparse FLOP count varies as we train, the average
FLOP count is: 2E[fs,t] + fd, where fs,t is the sparse inference FLOPs at train step t.

Pruning — Does not require dense gradients, but the sparsity increases smoothly from 0%
to the target value as we train. The FLOP consumption here is 3E[fs,t], , where fs,t is the
sparse inference FLOPs at train step t.

To determine E[fs,t], we compute a running average of the FLOP consumption after ev-
ery epoch. Notably, we find that the inference cost of Pruning is often close to a Random
initialized sparse network, while SNFS, regardless of initiazation, is compute-intensive.

C Trial Space of Hyperparameter Tuning

Figure 6 shows the hyper-parameter study for tuning (α, ∆T ) as a contour plot. We
observe that for multiple initialization-density configurations, the reference choice (α =
0.3, ∆T = 100), is quite close to the optimal hyper-parameters. Furthermore, where they
differ, the difference is within standard deviation bounds (Table 4 of the main report).

D Dynamic Structured Sparsity

Present hardware accelerators lack efficient implementations for unstructured sparsity.
As a result, in practice, the reduced FLOP requirement of sparse methods rarely trans-
late to wall-clock improvements. In comparison, there are efficient implementations
available for structured (or block) sparsity which reach theoretical speedups (Gray, Rad-
ford, and Kingma, Teja Vooturi, Varma, and Kothapalli21,22).

Motivated by this, we try modifying RigL to explicitly work on structured sparsity. We
promote channel sparsity for convolutional layers and keep fully connected layers dense.




Figure 6. Trial space of tuning (α, ∆T ), shown as a countor plot. Here, black circle corresponds
to (α = 0.3, ∆T = 100), while black triangle corresponds to the optimal hyper-parameter pair
found. We plot the convex hull of the trial space, so in a few cases the reference point lies on the
border of this space.

Table 7. Modifying RigL for structured sparsity, compared on CIFAR-10 and CIFAR-100 datasets.
RigL-struct fails to match the accuracy of RigL and just matches Small-Dense in performance.


CIFAR-10

CIFAR-100


89.0 ± 0.35

Small-Dense

RigL
RigL-Struct


87.0 ± 0.09

RigL
RigL-Struct


89.6 ± 0.16

Wall Time ↓ 

Wall Time ↓ 

Wall Time ↓ 


91.0 ± 0.07

0.20x


70.8 ± 0.22

Random Initialization

92.9 ± 0.10
90.4 ± 0.27

1.0x
0.20x

71.8 ± 0.33
69.1 ± 0.11

ERK Initialization


91.3 ± 0.18

1.0x
0.35x

72.6 ± 0.37
71.1 ± 0.15

0.11x

1.0x
0.10x

1.0x
0.23x

0.11x

1.0x
0.10x

1.0x
0.17x


72.6± 0.93

73.5 ± 0.04
71.9 ± 0.13

73.4 ± 0.15
72.9 ± 0.08

Wall Time ↓

0.20x

1.0x
0.20x

1.0x
0.38x

Mask update steps also operate at the channel level, based on RigLʼs growth and pruning
criterion. We name this method as RigL-struct. Such an approach is enticing, as we can
remove masked-out channels, and obtain practical speedups on accelerators without
needing support for unstructured sparsity.

Unfortunately, RigL-struct does not preserve the performance of originally proposed
RigL (Table 7). In fact, it performs only as good as Small-Dense models, which negates
the motivation behind such an experiment—Small-Dense models already achieve the
intended speedups.


(a) ERK, 1−𝑠=0.1(b) ERK, 1−𝑠=0.2(c) ERK, 1−𝑠=0.5(d) Random, 1−𝑠=0.1(e) Random, 1−𝑠=0.2(f) Random, 1−𝑠=0.5

---
**Source PDF:** `474b19bc0d13.pdf` (2021_21_article.pdf)  
**URL:** https://zenodo.org/record/4835564/files/article.pdf
