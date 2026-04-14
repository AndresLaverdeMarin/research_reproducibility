R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Don’t Judge an Object by Its Context: Learning to
Overcome Contextual Bias

Sunnie S. Y. Kim1, ID , Sharon Zhang1, ID , Nicole Meister1, ID , and Olga Russakovsky1, ID
1Princeton University, New Jersey, USA

Edited by
Koustuv Sinha,
Sasha Luccioni

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4834352

Reproducibility Summary

Scope of Reproducibility

Singh et al. [1] point out the dangers of contextual bias in visual recognition datasets.
They propose two methods, CAM-based and feature-split, that better recognize an object
or attribute in the absence of its typical context while maintaining competitive within-
context accuracy. To verify their performance, we attempted to reproduce all 12 tables
in the original paper, including those in the appendix. We also conducted additional
experiments to better understand the proposed methods, including increasing the reg-
ularization in CAM-based and removing the weighted loss in feature-split.

Methodology

As the original code was not made available, we implemented the entire pipeline from
scratch in PyTorch 1.7.0. Our implementation is based on the paper and email exchanges
with the authors. We spent approximately four months reproducing the paper, with the
first two months focused on implementing all 10 methods studied in the paper and the
next two months focused on reproducing the experiments in the paper and refining
our implementation. Total training times for each method ranged from 35–43 hours
on COCO-Stuff [2], 22–29 hours on DeepFashion [3], and 7–8 hours on Animals with At-
tributes [4] on a single RTX 3090 GPU.

Results

We found that both proposed methods in the original paper help mitigate contextual
bias, although for some methods, we could not completely replicate the quantitative
results in the paper even after completing an extensive hyperparameter search. For
example, on COCO-Stuff, DeepFashion, and UnRel, our feature-split model achieved an
increase in accuracy on out-of-context images over the standard baseline, whereas on
AwA, we saw a drop in performance. For the proposed CAM-based method, we were able
to reproduce the original paperʼs results to within 0.5% mAP.

What was easy

Overall, it was easy to follow the explanation and reasoning of the experiments. The im-
plementation of most (7 of 10) methods was straightforward, especially after we received


Code is available at https://github.com/princetonvisualai/ContextualBias. – SWH swh:1:dir:bc41dd1d3cbd9c97754c3da0ee20ba2273b742fd.
Open peer review is available at https://openreview.net/forum?id=PRXM8-O9PKd.




additional details from the original authors.

What was difﬁcult

Since there was no existing code, we spent considerable time and effort re-implementing
the entire pipeline from scratch and making sure that most, if not all, training/evalua-
tion details are true to the experiments in the paper. For several methods, we went
through many iterations of experiments until we were confident that our implementa-
tion was accurate.

Communication with original authors

We reached out to the authors several times via email to ask for clarifications and addi-
tional implementation details. The authors were very responsive to our questions, and
we are extremely grateful for their detailed and timely responses.

## 1 Introduction

Most prominent vision datasets are afflicted by contextual bias. For example, “microwave”
typically is found in kitchens, which also contain objects like “refrigerator” and “oven.”
Such co-occurrence patterns may inadvertently induce contextual bias in datasets, which
could consequently seep into models trained on them. When models overly rely on con-
text, they may not generalize to settings where typical co-occurrence patterns are ab-
sent. The original paper by Singh et al. [1] proposes two methods for mitigating such
contextual biases and improving the robustness of the learnt feature representations.
The paper demonstrates their methods on multi-label object and attribute classification
tasks, using the COCO-Stuff [2], DeepFashion [3], Animals with Attributes (AwA) [4], and
UnRel [5] datasets. Our exploration centers on four main directions:

First, we trained the baseline classifier presented in the paper (Section 2.1 for imple-
mentation and training details; Sections 2.3-2.4 for results). Due to likely implemen-
tation discrepancies, our results differed from the original paper by 0.6–3.1% mAP on
COCO-Stuff, by 0.7–1.4% top-3 recall on DeepFashion, and by 0.1–3.2% mAP on AwA
(Table 2). We ran a hyperparameter search (Appendix C), which yielded a significant
(1.4–3.6%) improvement on DeepFashion.

Next, we identified the biased categories in each dataset, i.e., visual categories that suffer
from contextual bias. We followed the proposed method of using the baseline classi-
fier to identify these categories, and discovered that the classifier implementation has a
non-trivial effect. For COCO-Stuff, 18 of the top-20 categories we identified matched the
original paperʼs top-20 categories (10 on DeepFashion, 18 on AwA; Section 2.2). Neverthe-
less, the categories we identified appear reasonable (e.g., “fork” co-occurs with “dining
table”; Appendix B). As training and evaluation of most methods depend on the biased
categories, we used the paperʼs biased categories for subsequent experiments.

Third, we checked the main claim of the paper, that the proposed CAM-based and feature-
split methods help improve recognition of biased categories in the absence of their con-
text (Section 3). On COCO-Stuff, DeepFashion, and UnRel, we were able to reproduce the
improvements gained from the proposed feature-split method towards reducing contex-
tual bias, whereas on AwA, we saw a drop in performance. The proposed 
method, which was only applied to COCO-Stuff, also helped reduce contextual bias,
though not as significantly as the feature-split method. For the method, we reproduced
the original paperʼs results to within 0.5% mAP (Section 3.5). We also successfully re-
produced the paperʼs weight similarity analysis, as well as the qualitative analyses with




class activation maps (CAMs) [6].

Lastly, we ran additional experiments and ablation studies (Section 3.6). These revealed
that the regularization term in the CAM-based method and the weighted loss in the
feature-split method are central to the methodsʼ performance. We also observed that
varying the feature subspace size influences the feature-split methodʼs accuracy.

## 2 Reproducing the standard baseline and the biased category pairs

The first step in reproducing the original paper is doing “stage 1” training. This stage
involves training a standard multi-label classifier with the binary cross entropy loss on
the COCO-Stuff, DeepFashion, and AwA datasets. We describe how we obtained and
processed the datasets in Appendix A. The standard model is used to identify the biased
categories and serves as a starting point for all “stage 2” methods, i.e., the proposed CAM-
based and feature-split methods and 7 other strong baselines introduced in Section 3.

### 2.1 Implementation and training details

According to the original paper, all models use ResNet-50 [7] pre-trained on ImageNet [8]
as a backbone and are optimized with stochastic gradient descent (SGD) and a batch
size of 200. Each standard model is optimized with an initial learning rate of 0.1, later
dropped to 0.01 following a standard step decay process. The input images are randomly
resize-cropped to 224×224 and randomly flipped horizontally during training. We also
received additional details from the authors that SGD is used with a momentum of 0.9
and no weight decay. The COCO-Stuff standard model is trained for 100 epochs with the
learning rate reduced from 0.1 to 0.01 after epoch 60. The DeepFashion standard model
is trained for 50 epochs with the learning rate reduced after epoch 30. The AwA 
model is trained for 20 epochs with the learning rate reduced after epoch 10.

After training with the paperʼs hyperparameters, we found that our reproduced stan-
dard models for COCO-Stuff and AwA were consistently underperforming against the re-
sults in the paper. Thus, we also tried varying the learning rate, weight decay, and the
epoch at which the learning rate is dropped to achieve the best possible results. Further
details can be found in Appendix C. On both COCO-Stuff and AwA, our hyperparame-
ter search ended up reconfirming the original paperʼs hyperparameters as the optimal
ones; for DeepFashion, we were able to find a significant improvement. The original,
reproduced and tuned results are shown in Table 1, following explanations of biased
categories identification (Section 2.2) and evaluation details (Section 2.3).

### 2.2 Biased categories identiﬁcation

The paper identifies the top-20 (b, c) pairs of biased categories for each dataset, where
b is the category suffering from contextual bias incurred by c, the associated context
category. This identification is crucial as it concretely defines the contextual bias the
paper aims to tackle, and influences the training of the “stage 2” models and evaluation
of all models.

The paper defines bias between two categories b and z as the ratio between the average
prediction probabilities of b when it occurs with and without z. Note that this definition
of bias requires a trained model, unlike the more common definition of bias that only re-
quires co-occurrence counts in a dataset [9]. Following the paper description, we used a
standard model trained on an 80-20 split for COCO-Stuff and one trained on the full train-
ing set for DeepFashion and AwA. For each category b in a given dataset, we calculated
the bias between b and its frequently co-occuring categories, and defined category c as




the context category that most biases b, i.e. has the highest bias value. Bias is calculated
on the 20 split for COCO-Stuff, the validation set for DeepFashion, and the test set for
AwA.1 After the bias calculation, we identified 20 (b, c) pairs with the highest bias values.
The paper emphasizes that this definition of bias is directional; it only captures the bias
c incurs on b and not the other way around.

We compare our pairs to the paperʼs in Tables A1 (COCO-Stuff), A2 (DeepFashion), and
A3 (AwA) in the Appendix. Out of 20 biased categories, 2 of ours differed from the paperʼs
for COCO-Stuff, 10 differed for DeepFashion, and 2 differed for AwA. The variability is
expected, as bias is defined as a ratio of a trained modelʼs average prediction probabili-
ties which will vary across different models. Nonetheless, we found our pairs to also be
reasonable, as our biased categories occur frequently with their context categories and
rarely without them. See Appendix B for details.

### 2.3 Evaluation details

The paper does not specify image preprocessing or model selection. Following com-
mon practice, we resize an image so that its smaller edge is 256 and then apply one of
two 224×224 cropping methods: a center-crop or a ten-crop. Both are deterministic pro-
cedures. We observed that results with center-crop are consistently better and closer to
the paperʼs results, hence for all experiments, we report results using center-crop. In
our email communications, the authors also specified that they use the model at the end
of training as the final model. We confirmed that this is a reasonable model selection
method after trying three other selection methods, described in Appendix D.

We emphasize that model evaluation is dependent on the identified biased category
pairs. For each (b, c) pair, the test set can be divided into three sets: co-occurring images
that contain both b and c, exclusive images that contain b but not c, and other images that
do not contain b. Then for each (b, c) pair, the paper constructs two test distributions: 1)
the “exclusive” distribution containing exclusive and other images and 2) the “co-occur”
distribution containing co-occurring and other images. We suspect that other images are
included in both distributions because otherwise, both distributions would have small
sizes and only consist of positive images where b occurs, disabling the mAP calculation.

The test distribution sizes can be calculated from the co-occurring and exclusive im-
age counts in Tables A1, A2, A3 in the Appendix. As an example, for the (ski, person)
pair in COCO-Stuff, there are 984 co-occuring, 9 exclusive, and 39,511 other images in the
test set. Hence, there are 9+39,511=39,520 images in the “exclusive” distribution and

1We received additional information from the original authors that they restricted their COCO-Stuff biased

categories to the 80 object categories and performed manual cleaning of the DeepFashion (b, c) pairs.

Dataset

Model

COCO-Stuff

DeepFashion

AwA

Paper
Ours (paper params∗)
Paper
Ours (paper params)
Ours (tuned params)
Paper
Ours (paper params∗)


Paper BC Our BC Paper BC Our BC Paper BC Our BC

Non-biased

24.5
23.9
4.9
5.6
7.0
19.4
19.5

-
20.6
-
5.0
6.3
-
21.7

66.2
65.0
17.8
19.2
22.8
72.2
69.0

-
63.7
-
15.0
18.4
-
69.9

75.4
72.3
-
-
-
-
-

-
72.9
-
-
-
-
-

All

57.2
55.7
-
-
-
-
-

Table 1. Reproduced standard baseline results on three datasets. We evaluate the models on differ-
ent subsets of categories/images (“exclusive” and “co-occur” distributions for the 20 biased cate-
gories and the entire test set for non-biased and all categories; Section 2.3), both using the paperʼs
and our identified biased category (BC) pairs. *On COCO-Stuff and AwA, hyperparameter tuning
did not improve on the original paperʼs hyperparameters.




984+39,511=40,495 images in the “co-occur” distribution. For COCO-Stuff, we also re-
port results on the entire test set (40,504 images) for 60 non-biased object categories and
for all 171 categories, following the paper.

For COCO-Stuff and AwA, we calculate the average precision (AP) for each biased cat-
egory b, and report the mean AP (mAP) for each test distribution. For DeepFashion, we
calculate the per-category top-3 recall and report the mean value for each test distribu-
tion. Higher values indicate a better classifier for both metrics.

### 2.4 Results

In Table 1, we report the original, reproduced, and tuned results with the paperʼs and
our 20 most biased category pairs. Evaluated on the paperʼs pairs, our best COCO-Stuff
model underperforms the paperʼs by 1-3%, our best DeepFashion model outperforms
by 2-5%, and our best AwA underperforms on the “co-occur” distribution by 3.2% and
matches the “exclusive” distribution within 0.1%. When we evaluate the same models
on our biased category pairs, we get similar results for the AwA model, slightly worse
results for the DeepFashion model, and significantly worse results for the COCO-Stuff
model. Due to this big drop in performance for COCO-Stuff, which we suspect is caused
by the discrepancy in the identified biased category pairs, we choose to use the paperʼs
pairs for training and evaluation in the subsequent sections. Overall, we conclude that
the paperʼs standard baseline results are reproducible as we were able to train models
within a reasonable margin of error.

## 3 Reproducing the “stage 2” methods: CAM-based, feature-split, and

strong baselines

In this section, we describe our efforts in reproducing methods that aim to mitigate con-
textual bias: namely, the CAM-based and feature-split methods proposed by the original
authors (Figure 1) and 7 other strong baselines. These are referred to as “stage 2” meth-
ods because they are trained on top of the “stage 1” standard model (except for one strong
baseline). Apart from the feature-split method, which we discussed with the authors, all
other implementations were based entirely on our interpretation of their descriptions
in the original paper.

Figure 1. Overview of the proposed methods. The CAM-based methods enforces a minimal overlap
between the (b, c) CAMs, while preventing them from drifting too far from CAMpre (CAMs of the
standard model). The feature-split method suppresses context for exclusive images by disabling
backpropagation through Ws and setting xs to a constant value; for non-exclusive images, it uses
everything as usual.

3.1 The ﬁrst proposed CAM-based method

The CAM-based method operates on the following premise: as b almost always co-occurs
with c, the network may learn to inadvertently rely on pixels corresponding to c to pre-


x!x""""!x!x""""!!: skateboard": person!: skateboardSuppress x!/$!and only leverage x"/$"Leverage all xand $as usualCAM#$%(),!)CAM#$%(),")CAM(),!)CAM(),")standardCAM-basedfeature-splitExclusive image (!occurs without ")Non-exclusive image": person

dict b. The paper hypothesizes that one way to overcome this issue is to explicitly force
the network to rely less on cʼs pixel regions. This method uses class activation maps
(CAMs) [6] as a proxy for object localization information. For an image I and category r,
CAM(I, r) indicates the discriminative image regions used by a deep network to identify
r. For each biased category pair (b, c), a minimal overlap of their CAMs is enforced via
the loss term:

LO =

I∈Ib∩Ic CAM(I, b) ⊙ CAM(I, c),

(1)
where ⊙ denotes element-wise multiplication and Ib ∩ Ic is a set of images where both b
and c appear. To prevent a trivial solution where the CAMs of b and c drift apart from the
actual pixel regions, the paper uses a regularization term to keep the categoryʼs CAMs
close to CAMpre, produced using a separate network trained offline:

∑

LR =

∑

I∈Ib∩Ic

|CAMpre(I, b) − CAM(I, b)| + |CAMpre(I, c) − CAM(I, c)|.

(2)

In our implementation, we separate a batch into two small batches during training, one
with and one without co-occurrences. A sample is put into the co-occurrence batch if
any of the 20 biased categories co-occurs with its context. For the co-occurrence batch,
we compute CAM with the current model being trained and CAMpre with the trained
standard model, using the official CAM implementation: https://github.com/zhoubolei/CAM.
We update the model parameters with the following loss, where LBCE is the binary cross
entropy loss:

LCAM = λ1LO + λ2LR + LBCE.

(3)

For the other batch without any co-occurrences, we update the model parameters with
LBCE. With the hyperparameters reported in the paper, λ1=0.1 and λ2=0.01, we got un-
derwhelming results and degenerate CAMs that drifted far from the actual pixel regions.
Hence, we tried increasing the regularization weight λ2 (0.01, 0.05, 0.1, 0.5, 1.0, 5.0) and
achieved the best results with λ2=0.1, which are reported in Table 2.

3.2 The second proposed feature-split method

By discouraging mutual spatial overlap, the CAM-based approach may not be able to
leverage useful information from the pixel regions surrounding the context. Thus, the
paper proposes a second method that splits the feature space into two subspaces to sep-
arately represent category and context, while posing no constraints on their spatial ex-
tents. Specifically, they propose using a dedicated feature subspace to learn examples
of biased categories appearing without their context.

Given a deep neural network, let x denote the D-dimensional output of the final pool-
ing layer just before the fully-connected (fc) layer. Let the weight matrix associated
with fc layer be W ∈ RD×M , where M denotes the number of categories given a multi-
label dataset. The predicted scores inferred by a classifier (ignoring the bias term) are
ˆy = W T x. To separate the feature representations of a biased category from its con-
text, the paper does a random row-wise split of W into two disjoint subsets: Wo and Ws
(dimension D
s xs.

When a biased category occurs without its context, the paper disables backpropagation
through Ws, forcing the network to learn only through Wo, and set xs to ¯xs (the average
of xs over the last 10 mini-batches).

× M ).2 Consequently, x is split into xo and xs, and ˆy = W T

o xo + W T

We implemented the feature-split method based on additional discussions with the orig-
inal authors, to ensure that we replicated their method as closely as possible. For a

2In an email, the authors noted that a random split is not critical; they obtained similar results with a
random split and a middle split. We observed that a middle split of W yields better results for COCO-Stuff and
DeepFashion, but the opposite for AwA. As the gains from using a middle split for COCO-Stuff and DeepFashion
were larger than the losses for AwA, we use a middle split throughout our experiments.




o xo + W T

o xo + W T

single training batch, we first forwarded the entire batch through the model to obtain
one set of scores ˆynon-exclusive = W T
s xs and the corresponding features from the
avgpool layer, which directly precedes the fc layer. We made a separate copy of these
features and replaced xs with ¯xs, then calculated a new set of output scores ˆyexclusive =
W T
s ¯xs. Separate loss tensors for each of these outputs were computed, and
elements corresponding to the exclusive and non-exclusive examples in the unmodi-
fied and modified loss tensors were zeroed out, respectively. The final loss tensor was
obtained by adding these two together, and standard backpropagation was done using
this final loss tensor. The gradients were calculated with respect to a weighted binary
cross entropy loss:

LWBCE = −α

]
[
t log(σ(ˆy)) + (1 − t) log(1 − σ(ˆy))

,

(4)

where t is the ground-truth label, σ is the sigmoid function, and α is the ratio between
the number of training images in which a biased category occurs in the presence of its
context and the number of images in which it occurs in the absence of its context. A
higher value of α indicates more data skewness.3

### 3.3 Strong baselines

In addition to the standard model, the paper compares the proposed methods with sev-
eral competitive strong baselines.

1. Remove co-occur labels: For each b, remove the c label for images in which b and

c co-occur.

2. Remove co-occur images: Remove training instances where any b and c co-occur.
For COCO-Stuff, this process removes 29,332 images and leaves 53,451 images in
the training set.

3. Split-biased: Split each b into two classes: 1) b \ c and 2) b ∩ c. Unlike other “stage
2” models, this model is trained from scratch rather than on top of the 
baseline because it has 20 additional classes. We later confirmed with the authors
that they did the same.

4. Weighted loss: For each b, apply 10 times higher weight to the loss for class b when

b occurs exclusively.

5. Negative penalty: For each (b, c), apply a large negative penalty to the loss for class
c when b occurs exclusively. In our email communication, the authors said that
the negative penalty means a 10 times higher weight to the loss.

6. Class-balancing loss [10]: For each b, put the images in three groups: exclusive,
co-occurring, and other. The weight for each group is (1 − β)/(1 − βn) where n is
the number of images for each group and β is a hyperparameter. The authors said
they set β = 0.99 in our email communication.

7. Attribute decorrelation [11]: Use the proposed method, but replace the hand-crafted
features used in [11] with deep network features (i.e., conv5 features of a trained
“stage 1” ResNet-50).

3In practice, the paper ensures α is at least αmin, which they set to 3 for COCO-Stuff and AwA and 5 for
DeepFashion. However, we found that most of the paperʼs biased category pairs have α smaller than αmin.
Out of 20 pairs, 13 pairs for COCO-Stuff, 20 pairs for DeepFashion, and 19 pairs for AwA had α smaller than
αmin. We also tried using higher values of αmin but didnʼt gain meaningful improvements, so we report results
with the original authorsʼ αmin.




Table 2. Performance of different methods on COCO-Stuff, DeepFashion, AwA, and UnRel on “ex-
clusive” and “co-occur” distributions with best results in bold. We compare our results to the pa-
perʼs results, specifically its Table 2, 3, 4, 5, 8, 9. Per-category results can be found in Appendix H.


standard4
remove labels
remove images
split-biased
weighted
negative penalty
class-balancing
attribute decorr.


COCO-Stuff (mAP)


23.9
24.5
24.5
25.2
29.0
28.4
25.4
19.1
28.5
30.4
23.9
23.8
24.6
25.0
-
-
26.9
26.4
28.1
28.8


65.0
66.2
64.6
65.9
59.6
28.7
64.7
64.3
60.0
60.8
64.7
66.1
64.7
66.1
-
-
64.2
64.9
64.8
### 66.0 DeepFashion (top-3 recall)


22.8
17.8
7.0
24.4
20.4
7.5
13.0
5.4
5.6
11.1
14.3
4.9
43.6
-
29.5
23.8
18.9
7.8
24.8
19.4
8.0
-
-
-
-
-
-
27.1
20.1
12.2

4.9
6.0
4.2
3.5
-
5.5
5.2
-
-
9.2

AwA (mAP)


19.5
19.4
18.9
19.1
21.7
22.7
18.2
19.7
20.0
-
19.6
19.2
19.9
20.4
20.6
18.4
-
-
19.2
20.8


69.0
72.2
63.2
62.9
65.2
58.3
64.2
66.8
67.7
-
69.0
68.4
68.2
68.4
69.8
70.2
-
-
68.6
### 72.8 UnRel (mAP)
3 categories

43.0
42.0
42.7
-
48.6
-
29.2
-
44.4
-
42.5
-
42.3
-
-
-
46.8
45.3
49.9
### 52.1 Figure 2. A visual comparison of the COCO-Stuff results from Table 2. The blue and red lines
mark the paperʼs and our standard mAPs. Similar plots for DeepFashion and AwA can be found in
Appendix F.

### 3.4 Training details and computational requirements

We trained all “stage 2” models on top of the standard model for 20 epochs using a learn-
ing rate of 0.01, a batch size of 200, and SGD with 0.9 momentum. The exceptions are
split-biased which is not trained on top of the standard model and is thus trained for an
additional 20 epochs to ensure a fair comparison; and CAM-based which uses a batch
size of 100 due to memory limits. All models were trained on a single RTX 3090 GPU and
evaluated on the last epoch. On COCO-Stuff, the single-epoch training time was around
12.9 minutes for standard, remove labels, split-biased, weighted, negative penalty, and class-
balancing. It took 8.4 minutes to train remove images, and 17.3 minutes and 13.3 minutes
to train CAM-based and feature-split, respectively. Thus, we reach a different conclusion
from the paperʼs claim that the “overall training time of both proposed methods is very
close to that of a standard classifier.” We suspect that this difference is due to the differ-
ence in implementation. Overall, the total training time for each method range from
35-43 hours on COCO-Stuff, 22-29 hours on DeepFashion, and 7-8 hours on AwA. For in-
ference, the paper reports that a single forward pass of an image takes 0.2ms on a single
Titan X GPU for the standard, CAM-based, and feature-split methods. We confirmed that
it takes the same amount of time for the three methods. See Appendix E for detailed
training and inference times.

### 3.5 Results

In Table 2, we compare the performance of the ten methods, evaluated with the paperʼs
biased category pairs for consistency. Additional figures and per-category results can
be found in Appendix F and H.

4To ensure a fair comparison with the ”stage 2” models, we tried training the standard model for an addi-

tional 20 epochs but did not see improvements; hence, we report the standard results from Table 1.




COCO-Stuff: Since our standard model underperforms the paperʼs by 0.6-3.1% (Section 2),
we focus on the ordering between the different methods visualized in Figure 2. In the
paper, all but split-biased and negative penalty improve upon the standard baselineʼs “ex-
clusive” mAP; whereas in our experiments, only negative penalty fails to improve on stan-
dardʼs “exclusive” mAP. Different from the paper, remove images has the highest “exclu-
sive” mAP in our experiments, followed by weighted and the paperʼs proposed methods,
feature-split and CAM-based. For feature-split, we observed a similar tradeoff between
“exclusive” and “co-occur” mAPs compared to the paper. All methods have similar per-
formance of 55.0–55.7 mAP when evaluated on the full test set for all 171 categories.

DeepFashion: Consistent with the paper, all methods except remove images and split-
biased improve upon standardʼs “exclusive” top-3 recall. We found the weighted method
performs the best out of all the methods with +22.5% for “exclusive” and +20.8% for “co-
occur.” However, it has a relatively low top-3 recall when evaluated on the full test set for
all 250 categories: 23.3 compared to other methodsʼ top-3 recall in the range of 23.8–24.3.

Animals with Attributes: Unlike the result reported in the paper, our reproduced feature-
split model had a -0.3% drop in “exclusive” mAP and a -0.4% drop in “co-occur” mAP
compared to the standard model. In Section 3.6, when we experimented with differ-
ent subspace sizes, we observed that the feature-split model trained with xo of size 1,792
improves upon the standard model on both test distributions. Among all the methods,
remove images improves the “exclusive” mAP the most; however, this method also suf-
fers from a noticeable decrease in “co-occur” performance. When evaluated on the full
test set for all 85 categories, most methods have similar mAP in the range of 72.5–73.0,
except for remove labels that has 70.6 mAP and remove images that has 69.7 mAP.

UnRel: The paper includes a cross-dataset experiment where the models trained on
COCO-Stuff are applied without any fine-tuning on UnRel, a dataset that contains im-
ages of objects outside of their typical context. The paper evaluates the models only on
the 3 categories of UnRel that overlap with the 20 most biased categories of COCO-Stuff,
which we determined to be skateboard, car, and bus. While the paper does not report
results from the remove images baseline, for us it had the highest mAP of the 3 categories,
followed by the feature-split and CAM-based methods.

### 3.6 Additional analyses

Cosine similarity between Wo and Ws: The paper computes the cosine similarity be-
tween Wo and Ws to investigate if they capture distinct sets of information. It reports
that the proposed methods yield a lower similarity score compared to the standard model,
and concludes that the biased class b is less dependent on c for prediction in their meth-
ods. To reproduce their results, for feature-split, we calculated the cosine similarity be-
tween Wo[:, b] and Ws[:, b] (dimensions D
2 ) for each b of the 20 (b, c) pairs and reported
their average. On the other hand, Wo and Ws are not specified for standard and CAM-
based. Hence, we randomly split W in half and defined one as Wo and the other as Ws.


COCO-Stuff

0.08
0.21
0.07
0.19
0.04
0.17

DeepFashion

0.12
-
0.05

-
-
-

AwA

0.02
-
0.02

-
-
-

Table 3. Cosine similarity between Wo and Ws for the 20 most biased categories. We compare
our reproduced results to those in the paperʼs Table 7. The paper does not report results for the
DeepFashion and AwA datasets.




In Table 3, we compare our reproduced results with the paperʼs results. Consistent with
the paperʼs conclusion, we find that the proposed methods have weights with similar or
lower cosine similarity. On the interpretation of the results, we agree that feature-splitʼs
low cosine similarity suggests that the corresponding feature subspaces xo and xs cap-
ture different information, as intended by the method. However, we donʼt understand
why the cosine similarity of CAM-based would be lower than standard, as there is noth-
ing in CAM-based that encourages the feature subspaces to be distinct.

Qualitative analysis: Following Section 5.1.2 of the original paper, we used CAMs to
visually analyze the proposed methods. In general, our observations are in line with
those of the original paper. For example, in Figure 3, we see that CAM-based tends to
only focus on the object pixel regions (e.g., skateboard, microwave) compared to stan-
dard, while feature-split also makes use of context (e.g., person, oven). More qualitative
analyses are available in Appendix G.

Figure 3. Biased category CAMs for (skateboard, person) and (microwave, oven) pairs.

4 Our additional experiments

To better understand the proposed CAM-based and feature-split methods, we conducted
several ablation studies (Table 4).

What is the effect of the regularization term in the CAM-based method? As mentioned
in Section 3.1, we tried varying the weight for the regularization term LR (λ2) in the
CAM-based method that prevents the CAMs of the biased category pairs from drifting
apart from the pixel regions of CAMpre. We observed that weak regularization allows
for highly localized, degenerate CAMs that donʼt resemble CAMpre, while overly strong
regularization makes the method less effective. We were able to strike an ideal balance
with λ2=0.1, higher than the paperʼs λ2=0.01.

What is the effect of the weighted loss in the feature-split method? To understand the
effect of the weighted loss in the feature-split method, we tried training a 
model without it and a baseline model with the feature-split weighted loss. Both varia-
tions have lower “exclusive” mAPs, suggesting that both the feature-splitting framework
and the weighted loss are important components of the method. We highlight that the
feature-split model trained without the weighted loss is worse than the standard model,
suggesting that the weighted loss is central for the feature-split method to achieve good
performance. However, we also observed that the feature-split methodʼs weighted loss
by itself is not sufficient for improving the performance of the standard model on the
“exclusive” distribution.

Does the size of the feature-split subspace matter? In the feature-split method, the orig-
inal paper allocates half of the 2,048 feature dimensions in the fc layer for learning
exclusive image examples. We explored whether a smaller or larger xo subspace may




strike a better balance and improve both “exclusive” and “co-occur” performance, as
the number of exclusive images is only a small fraction of the entire training data. For
COCO-Stuff, the performance peaks on “exclusive” and dips on “co-occur” at the 1,024
dimension split. For DeepFashion, performance on both distributions peak at the 1,024
dimension split. For AwA, however, the performance on both distributions improves as
the subspace size increases. Lastly for UnRel, the model trained on COCO-stuff with a
xo of size 768 performs best. Overall, we did not find a clear trend between 
performance and subspace size.

Table 4. (Top) Ablation studies of CAM-based and feature-split on COCO-Stuff. (Bottom) Additional
feature-split results with varying xo subspace sizes. Best results are in bold.


CAM-based with λ2 = 0 (no regularization)
CAM-based with λ2 = 0.01 (paper params)
CAM-based with λ2 = 0.1 (tuned params)

feature-split without weighted loss
baseline with feature-split weighted loss


23.9
24.4
24.6
26.9
28.1
23.6
24.0

65.0
64.6
64.6
64.2
64.8
65.4
64.8

All
55.7
55.5
55.5
55.5
55.6
55.6
55.5

xo size

COCO-Stuff (mAP)


1,024
1,280
1,536
1,792

23.8
26.7
27.2
28.1
24.8
23.0
21.7

65.9
65.9
65.8
64.8
66.0
66.1
### 66.2 DeepFashion (top-3 recall)

3.2
3.4
4.6
12.2
4.0
2.7
2.3


12.5
12.9
14.3
27.1
13.7
13.9
14.1

AwA (mAP)


18.5
18.7
19.1
19.2
19.3
19.5
19.7

69.7
69.0
69.2
68.6
69.9
70.3
70.8

Non-biased
72.3
72.0
72.0
72.2
72.1
72.1
### 72.1 UnRel (mAP)
3 categories
47.8
50.1
50.4
49.9
45.8
44.2
40.6

## 5 Discussion

We found that the proposed CAM-based and feature-split methods help mitigate contex-
tual bias, although we could not completely replicate the quantitative results in the
original paper even after completing an extensive hyperparameter search. As an ef-
fort to check our conclusions, we tried several different approaches in how we choose
our best models, train the baselines, and performed evaluation. We also conducted
additional analyses of the proposed methods to check our implementations and train
them to achieve their best possible performance. In all cases, decreasing contextual
bias frequently came with the cost of decreasing performance on non-biased categories.
Ultimately, we believe deciding what method is best depends on the trade-offs a user is
willing to make in a given scenario, and the original paperʼs proposed methods seem to
strike a good balance for the tested datasets.

Recommendations for reproducibility: Overall, the paper was clearly written and it was
easy to follow the explanation and reasoning of the experiments. Still, we ran into sev-
eral obstacles while re-implementing the entire pipeline from scratch. Our biggest con-
cern was making sure that most, if not all, training/evaluation details were true to the
experiments in the paper. We are extremely grateful to the original authors who gave
swift responses to our questions. Nevertheless, it would have been easier to reproduce
the results with code or a README file listing design decisions. Given the limited in-
formation, it took us over a month to lock in various details on data processing, hyper-
parameter optimization, and training the standard model, before we could move onto
reproducing the “stage 2” methods. Moreover, each method had its intricacies and we




inevitably ran into ambiguities along the way. For example, the attribute decorrelation
method took considerable time to reproduce because no hyperparameters or code were
given in the paper or the original work [11]. We hope our report and published code
help future use of the paper.

Recommendations for reproducing papers: In closing, we would like to share a few
things that we found helpful as suggestions for future reproducibility efforts. First, writ-
ing the mandatory reproducibility plan (provided in Appendix I) at the beginning of the
challenge was helpful, as it forced us to define concrete steps for reproducing the experi-
ments. We suggest putting together a similar plan because the order in which materials
are presented in the paper can be different from the order in which experiments should
be run. Additionally, we recommend communicating early with the original authors
to determine undisclosed parameters and pin down the experimental setup. Lastly, for
reproducing training processes in particular, we suggest checking how training is pro-
gressing in as many different ways as possible. In our process, this involved looking
at the progression of CAMs and examining training curves for individual loss function
terms, both of which helped us pinpoint our issues.

Acknowledgements

This work is supported by the National Science Foundation under Grant No. 1763642 and
the Princeton First Year Fellowship to SK. We thank the authors of the original paper,
especially the lead author Krishna Kumar Singh, who gave detailed and swift responses
to our questions. We also thank Angelina Wang, Felix Yu, Vikram Ramaswamy, Vivien
Nguyen, Zeyu Wang, and Zhiwei Deng for helpful comments and suggestions.

References

1.

K. K. Singh, D. Mahajan, K. Grauman, Y. J. Lee, M. Feiszli, and D. Ghadiyaram. “Don’t Judge an Object by Its
Context: Learning to Overcome Contextual Bias.” In: Conference on Computer Vision and Pattern Recognition
(CVPR). 2020.

2. H. Caesar, J. Uijlings, and V. Ferrari. “COCO-Stuff: Thing and Stuff Classes in Context.” In: Conference on Com-

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

puter Vision and Pattern Recognition (CVPR). 2018.
Z. Liu, P. Luo, S. Qiu, X. Wang, and X. Tang. “DeepFashion: Powering Robust Clothes Recognition and Retrieval
with Rich Annotations.” In: Conference on Computer Vision and Pattern Recognition (CVPR). 2016.
Y. Xian, C. H. Lampert, B. Schiele, and Z. Akata. “Zero-Shot Learning—A Comprehensive Evaluation of the Good,
the Bad and the Ugly.” In: IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) (2019).
DOI: 10.1109/TPAMI.2018.2857768.
J. Peyre, I. Laptev, C. Schmid, and J. Sivic. “Weakly-Supervised Learning of Visual Relations.” In: International
Conference on Computer Vision (ICCV). 2017.
B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and A. Torralba. “Learning Deep Features for Discriminative Localiza-
tion.” In: Conference on Computer Vision and Pattern Recognition (CVPR) (2016).
K. He, X. Zhang, S. Ren, and J. Sun. “Deep Residual Learning for Image Recognition.” In: Conference on Com-
puter Vision and Pattern Recognition (CVPR). 2016. DOI: 10.1109/CVPR.2016.90.
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. “ImageNet: A Large-Scale Hierarchical Image
Database.” In: Conference on Computer Vision and Pattern Recognition (CVPR). 2009.
J. Zhao, T. Wang, M. Yatskar, V. Ordonez, and K.-W. Chang. “Men Also Like Shopping: Reducing Gender Bias
Ampliﬁcation using Corpus-level Constraints.” In: Conference on Empirical Methods in Natural Language
Processing (EMNLP). 2017.
Y. Cui, M. Jia, T.-Y. Lin, Y. Song, and S. Belongie. “Class-Balanced Loss Based on Effective Number of Samples.”
In: Conference on Computer Vision and Pattern Recognition (CVPR). 2019.
D. Jayaraman, F. Sha, and K. Grauman. “Decorrelating Semantic Visual Attributes by Resisting the Urge to
Share.” In: Conference on Computer Vision and Pattern Recognition (CVPR). 2014.
T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and L. Zitnick. “Microsoft COCO: Com-
mon Objects in Context.” In: European Conference on Computer Vision (ECCV). 2014. URL: https : / / www .
microsoft.com/en-us/research/publication/microsoft-coco-common-objects-in-context/.




Appendix

We dedicate the appendix to providing more details on certain parts of the main paper.

• In Section A, we describe how we obtained and processed the four datasets.
• In Section B, we provide additional details on biased categories identification.
• In Section C, we describe our hyperparameter search.
• In Section D, we discuss different model selection methods we tried while reproducing

the standard baseline.

• In Section E, we provide more details on computational requirements.
• In Section F, we provide visualizations of DeepFashion and AwA results.
• In Section G, we provide additional qualitative analyses with CAMs.
• In Section H, we provide per-category results for COCO-Stuff, DeepFashion, Animals

with Attributes, and UnRel.

• In Section I, we provide the reproducibility plan we wrote at the start of the project.

A Datasets

In this section, we describe how we obtained and processed the four datasets used in
the paper. COCO-Stuff [2] and UnRel [5] are used for the object classification task, and
DeepFashion [3] and Animals with Attributes [4] are used for the attribute classification
task. COCO-Stuff is the main dataset used for discussion of quantitative and qualita-
tive results. UnRel is used for cross-dataset experiments, i.e. testing models trained on
COCO-Stuff on UnRel without fine-tuning.

A.1 COCO-Stuff

We downloaded COCO-Stuff [2] from the official homepage: https://github.com/nightrome/
cocostuff. COCO-Stuff includes all 164K images from COCO-2017 (train 118K, val 5K, test-
dev 20K, test-challenge 20K), but only the training and validation set annotations are
publicly available. It covers 172 classes: 80 thing classes, 91 stuff classes and 1 class
designated ʻunlabeled.ʼ

COCO-Stuff (COCO-2017 with “stuff” annotations added) contains the same images as
COCO-2014 [12] but has different train-val-test splits. The original paper follows the
data split of COCO-2014 and uses 82,783 images for training and 40,504 images for eval-
uation. The image numbers are consistent between COCO-2014 and COCO-2017, so we
were able to map the “stuff” annotations from COCO-Stuff to the COCO-2014 images with
“thing” annotations. Excluding the ʻunlabeledʼ category, we have in total 171 categories.

In Table A1, we report the co-occurrence, exclusive, and other counts for the paperʼs
20 biased category pairs. The co-occurrence count is the number of images where b and
c co-occur; the exclusive count is the number of images where b occurs without c; the
other count is the number of remaining images where b doesnʼt occur.

During our data processing, we found a small typo in the original paper. Section 3 of
the paper says “COCO-Stuff has 2,209 images where ʻskiʼ co-occurs with ʻperson,ʼ but only
has 29 images where ʻskiʼ occurs without ʻperson.ʼ” On the other hand, we found 2,180
co-occurring and 29 exclusive images in the training set. We verified with the authors
that our data processing was correct. Merging COCO-2014 and COCO-Stuff annotations
is a nontrivial step in the pipeline. We hope our published code and the Table A1 help
future use.




A.2 DeepFashion

We downloaded DeepFashion [3] by following in the instructions on the official home-
page: http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html. The dataset consists of 5 bench-
marks, out of which we use the Category and Attribute Prediction Benchmark. This
benchmark consists of 209,222 training images, 40,000 validation images, and 40,000 test
images with 1,000 attribute classes in total. Per the procedure specified by the authors,
we only use the 250 most commonly appearing attributes. In Table A2, we report the co-
occur, exclusive and other counts for the paperʼs 20 biased category pairs. It should be
noted that the DeepFashion dataset was updated with additional “fine-grained attribute
annotations” in May 2020.

A.3 Animals with Attributes

Animals with Attributes (AwA) [4] is suspended and the images are no longer available
because of copyright restrictions, according to the official homepage: https://cvml.ist.ac.
at/AwA/. Hence we downloaded Animals with Attributes 2 (AwA2), which is described as
a “drop-in replacement” to AwA as it has the same class structure and almost the same
characteristics, from the AwA2 official homepage: https://cvml.ist.ac.at/AwA2/. We con-
firmed with the authors that they used AwA2 as well. AwA2 consists of 30,337 training
images with 40 animal classes and 6,985 test images with 10 other animal classes, with
pre-extracted feature representations for each image. The classes are aligned with Os-
hersonʼs classical class/attribute matrix, thereby providing 85 numeric attribute values
for each class. The images were collected from public sources, such as Flickr, in 2016.

In Table A3, we report the co-occurrence, exclusive, and other counts for the paperʼs
20 biased category pairs. Following the description in the paper, we trained all models
on the training set (40 classes) and evaluate on the test set (10 classes). For biased cate-
gories identification, following the paper description, we used the test set to determine
the biased categories as these two sets contain different attribute distributions.

A.4 UnRel

We downloaded UnRel [5] from the official homepage: https://github.com/jpeyre/unrel. This
dataset contains 1,071 images of objects out of their typical context and serves as a stress
test for the models trained on COCO-Stuff. According to the paper, there are only three
categories in UnRel that are shared with the 20 biased categories found in COCO-Stuff.
We determined these categories to be “skateboard,” “car” and “bus.” Only these three
categories were used in the evaluation.

B Biased categories identiﬁcation

In this section, we provide additional details on the biased categories identification pro-
cess discussed in Section 2.2 of the main paper.

For each dataset, the paper identifies the top-20 (b, c) pairs of biased categories, where
b is the category suffering from contextual bias and c is the associated context category.
For a given category z, let Ib ∩ Iz and Ib \ Iz denote sets of images where b occurs with
and without z respectively. Let ˆp(I, b) denote the prediction probability of an image I
for a category b obtained from a trained multi-class classifier. The bias between two

5We found this vague as there are two ceiling categories in COCO-Stuff: ceiling-other and ceiling-tile. We

interpreted it as ceiling-other as ceiling-tile doesnʼt frequently co-occur with toaster.




categories b and z is defined as follows:

bias(b, z) =


|Ib∩Iz|

|Ib\Iz|

∑

I∈Ib∩Iz

∑

I∈Ib\Iz

ˆp(I, b)

ˆp(I, b)

,

(5)

which is the ratio of average prediction probabilities of b when it occurs with and with-
out z. The category c that most biases b is determined as c = arg maxz bias(b, z), with a
condition that they co-occur frequently. Specifically, the paper defines that b must co-
occur at least 20% of the time with c for COCO-Stuff and AwA, and 10% for DeepFashion.
In short, a given category b is most biased by c if (1) b co-occurs frequently with c and (2)
the prediction probability of b drop significantly in the absence of c.

While this method can be applied to any number of biased category pairs, the paper
says using K=20 sufficiently captures biased categories in all datasets used the paper.
We report the 20 most biased category pairs weʼve identified and compare them to those


cup
wine glass
handbag
apple
car
bus
potted plant
spoon
microwave

skis
clock
sports ball
remote
snowboard
toaster
hair drier
tennis racket
skateboard
baseball glove


fruit
road
road
vase
bowl
oven
mouse

building


ceiling5
towel


Bias

1.85
1.76
1.59
1.80
2.25
1.81
2.12
1.91
1.73
1.94
1.79
1.94
1.73
1.99
1.75
2.04
1.59
2.08
2.11
2.25
2.21
2.28
1.97
2.39
3.61
2.45
1.89
2.45
2.40
2.86
1.98
3.70
3.49
4.00
1.26
4.15
3.41
7.36
31.32
339.15

Training (82,783)

Test (40,504)

Biased category pairs (Ours)

Co-occur Exclusive Co-occur 

3,186
1,151
4,380

5,794
2,283

1,314


2,180
1,410
2,607
1,469
1,146


2,336
2,473
1,834

3,140


2,806

2,152


1,691


1,449

2,035

2,842
1,090


1,269


1,180
1,068


1,514


1,331

1,058


car
potted plant
spoon
fork
bus
cup
mouse
remote
wine glass
clock

apple
skis
handbag
snowboard
skateboard
sports ball
hair drier
toaster
baseball glove


road
furniture-other
bowl

road


building-other
mouse
fruit
snow


sink
oven


Bias
1.73
1.75
1.75
1.78
1.79
1.85
1.87
1.89
1.94
1.97
2.11
2.12
2.22
2.25
2.40
3.41
3.61
6.11
8.56
### 31.32 Table A1. (Left) The paperʼs 20 most biased category pairs for COCO-Stuff and their bias values,
both whatʼs reported in the paper and what weʼve calculated with our trained model. (Middle) The
number of co-occuring and exclusive images for each pair. (Right) The 20 most biased categories
weʼve identified with our trained model.


bell
cut
animal
flare
embroidery
suede
jacquard
trapeze
neckline
retro
sweet
batwing
tassel
boyfriend
light
ankle
french
dark
medium
studded


lace
bodycon
print
fit

fringe
flare
striped
sweetheart


loose

distressed


terry
wash
wash
denim

Bias

Training (209,222)

Test (40,000)

Biased category pairs (Ours)

Paper Ours Co-occur Exclusive Co-occur 
3.15
3.30
3.31
3.31
3.44
3.48
3.68
3.70
3.98
4.08
4.32
4.36
4.48
4.50
4.53
4.56
5.09
5.13
7.45
7.80


2,960


2612


1,021


1,135
1,122


1,172
1,621


1,011


2.74
3.46
2.29
2.56
3.04
2.75
4.02
2.85
3.16
3.43
6.55
3.89
3.15
3.35
3.31
4.42
7.64
5.66
6.78
4.98


boyfriend
gauze
la
diamond
york
retro
cut
fitted
light
sequin
cuffed
lady
jacquard
bell
ankle
tiered
studded
dark
sweet
medium


distressed
embroidered

print
city

bodycon
sleeve
wash
mini
denim

fit
sleeve


denim
wash

wash

Bias
3.35
3.35
3.35
3.40
3.43
3.43
3.46
3.58
3.59
3.63
3.70
3.71
4.02
4.23
4.42
4.45
4.98
5.66
6.55
### 6.78 Table A2. (Left) The paperʼs 20 most biased category pairs for DeepFashion and their bias values,
both whatʼs reported in the paper and what weʼve calculated with our trained model. (Middle) The
number of co-occuring and exclusive images for each pair. (Right) The 20 most biased categories
weʼve identified with our trained model.




Table A3. (Left) The paperʼs 20 most biased category pairs for AwA and their bias values, both whatʼs
reported in the paper and what weʼve calculated with our trained model. (Middle) The number
of co-occuring and exclusive images for each pair. (Right) The 20 most biased categories weʼve
identified with our trained model.


white

forager
lean
fish
hunter
plains
nocturnal

jungle

meat
mountains
tree

spots
bush
buckteeth
slow
blue


ground


timid
big

white
meatteeth

black
fish
paws
tail
inactive

meat
smelly
strong
coastal

Bias

Training (30,337)

Test (6,985)

Biased category pairs (Ours)

Paper
3.67
3.71
4.02
4.46
5.14
5.34
5.40
5.84
5.92
6.26
6.39
7.12
9.24
10.98
11.77
20.15
29.47
34.01
76.59
319.98

Ours
4.08
6.55
4.04
3.91
6.30
8.99
1.81
6.97
8.14
9.15
4.63
10.17
14.74
11.48
11.02
12.50
31.26
51.25
125.19
1,393.25

Co-occur Exclusive Co-occur 

12,952
3,727
7,740
5,312
2,786
6,557
3,793
3,118
4,788
4,480
10,656
3,175
3,090
2,121
5,853
3,095
1,896
3,701
8,710


1,237
7,667
7,214
11,592
2,675
3,207
12,865
2,464
5,180

8,960
7,819
4,897
1,255
5,953
2,433
5,922
3,339
1,708


3,156

3,144

4,002
1,708


2,270
2,132
2,157
1,979
1,232
1,960
3,322

6,265

3,968


1,038
1,232


3,087
1,602


forager
white
hairless

insects
fish

nocturnal

hunter
jungle
meat

tree
spots
mountains
bush
buckteeth
slow
blue


ground
swims
black
gray
timid

white
meatteeth
big

fish
inactive
tail

paws
meat
smelly
strong
coastal

Bias
4.04
4.08
4.29
4.63
4.97
6.30
6.55
6.97
8.14
8.99
9.15
10.17
11.02
11.48
12.50
14.74
31.26
51.25
125.19
1,393.25

identified by the paper in Tables A1 (COCO-Stuff), A2 (DeepFashion), A3 (AwA). We dis-
cuss the results for each dataset in more detail below.

COCO-Stuff: Overall, the bias values of the paperʼs biased category pairs calculated with
our model are similar to the paperʼs values. Furthermore, most of our biased category
pairs match with the paperʼs pairs. 18 of the 20 biased categories overlap, although their
context categories sometimes differ.

DeepFashion: After manual cleaning per suggestion of the authors, 10 of our biased
category pairs match with the paperʼs. Still, the bias values of the paperʼs pairs calcu-
lated with our trained model are overall similar to the paperʼs values. It is worth noting
that there are fewer co-occurring and exclusive images for each of the biased category
pairs, compared to COCO-Stuff.

Animals with Attributes: Almost all of our biased categories match with those in the pa-
per. However, we observed in the process of determining the biased categories that for
each b, there were multiple categories c which had an equally biased effect on b. That is,
the bias value bias(b, c) was equal over each of these cʼs. We suspect that this is because
the images in AwA are labeled by animal class rather than per image, so many images
share the same exact labels. Moreover, we observed that for many image examples, the
baseline modelʼs highest prediction scores differ by less than 0.0001. The combination
of these two events may result in extremely similar bias scores. Since there were multi-
ple cʼs for each b, we listed the category which matched the paperʼs findings whenever
possible. In total, 18 of our biased categories overlapped with those in the paper.

C Hyperparameter search

In this section, we describe how we conducted our hyperparameter search. The paper
does not describe the hyperparameter search process, so we followed standard practice
and tuned the hyperparameters on the validation set. While DeepFashion has training,
validation and test sets, COCO-Stuff and AwA donʼt have validation sets, so we created
a random 80-20 split of the original training set and used the 80 split as the training set
and the 20 split as the validation set. We later confirmed with the authors that this is
how they did their hyperparameter search.




Search for the “stage 1” standard model: For COCO-Stuff, we tried varying the learning
rate (0.1, 0.05, 0.01), weight decay (0, 1e-5, 1e-4, 1e-3), and the epoch after which learn-
ing rate is dropped (20, 40, 60). We found that the paperʼs hyperparameters (0.1 learning
rate dropped to 0.01 after epoch 60 with no weight decay) produced the best results. For
DeepFashion, we varied the learning rate (0.1, 0.05, 0.01, 0.005, 0.001, 0.0001), weight
decay (0, 1e-6, 1e-5, 1e-4), and the epoch after which the learning rate dropped (20, 30).
We obtained the best results using a constant learning rate of 0.1 and weight decay of
1e-6. For AwA, we tried learning rates of 0.1 and 0.01, with various training schedules
such as dropping from 0.1 to 0.001, dropping from 0.01 to 0.001, and keeping a constant
learning rate of 0.01 throughout. We also tried varying weight decay (0, 1e-2, 1e-3, 1e-4,
1e-5), but the paperʼs hyperparameters (0.1 learning rate dropped to 0.01 after epoch 10
with no weight decay) led to the best results. We also tried training the models longer
but didnʼt find much improvement, so we trained for the same number of epochs as in
the paper (100 for COCO-Stuff, 50 for DeepFashion, 20 for AwA).

Search for the “stage 2” models: For “stage 2” models, we tried varying the learning
rate (0.005, 0.01, 0.05, 0.1, 0.5) and found that the paperʼs learning rate of 0.01 produces
the best results. We didnʼt find benefits from training the models longer, so following
the original authors, we train all “stage 2” models (except split-biased) for 20 epochs on
top of the standard model and use the model at the end of training as the final model.
For the CAM-based model, we conducted an additional hyperparameter search because
we got underwhelming results and degenerate CAMs with the paperʼs hyperparameters
(λ1=0.1, λ2=0.01). We tried varying the regularization weight λ2 (0.01, 0.05, 0.1, 0.5, 1.0,
5.0) and achieved the best results with λ2=0.1.

D Selecting the best model epoch

While reproducing the standard model in Section 2, we tried selecting the best model
epoch with four different selection methods: 1) lowest loss, 2) highest exclusive mAP,
3) highest combined exclusive and co-occur mAPs, and 4) last epoch (paperʼs method).
Note that method 4 does not require a validation set, while methods 1-3 do as they re-
quire examinations of the loss and the mAPs at every epoch. Hence for datasets like
COCO-Stuff and AwA that donʼt have a validation set, we can apply the first three meth-
ods only when we create a validation set by doing a random split of the original training
set (e.g., 80-20 split).

In Table A4, we show COCO-Stuff standard results with different epoch selection meth-
ods. For methods 1–3, the best epoch is selected based on the loss or the mAPs on the
validation set. For method 4, we simply select the last epoch. Note that all numbers in
the table are results on the unseen test set.

First considering the model trained on the 80 split, we see that selecting the epoch with
the lowest (BCE) loss yields the lowest mAP (row 1). The results of the other three meth-
ods (rows 2–4) are largely similar, with less than 0.4 mAP difference for all fields. When
we plot the progression of the losses and the mAPs (Figure A1), we see that the mAPs are
mostly consistent in the latter epochs. Hence, we decided that using the last epoch is a
reasonable epoch selection method. With this method we also benefit from training on
the full training set, which improves all four mAPs (row 5).




Table A4. COCO-Stuff standard baseline results with different model epoch selection methods. All
numbers are results on the test set. The best results are in bold.

Training data


Full training set

Selection method
1) Lowest loss
2) Highest exclusive mAP
3) Highest exclusive + co-occur mAP
4) Last epoch
4) Last epoch

Selected epoch


22.0
22.9
23.0
22.9
23.9

64.0
64.1
64.2
63.8
65.0

All
55.4
55.2
55.3
55.0
55.7

Non-biased
71.8
71.6
71.8
71.4
### 72.3 Figure A1. Losses and mAPs of the COCO-Stuff standard model trained on the 80 split of the original
training set. The validation loss and the four mAPs are calculated on the remaining 20 split which
we use as the validation set.

E Computational requirements

In Table A5, we report the single-epoch training time for each method trained with a
batch size of 200 using a single RTX 3090 GPU, except for CAM-based which is trained on
two GPUs due to memory constraints. Overall, the total training time for each method
range from 35-43 hours on COCO-Stuff, 22-29 hours on DeepFashion, and 7-8 hours on
AwA. For inference, a single image forward pass takes 9.5ms on a single RTX 3090 GPU.
Doing inference on the entire test with a batch size of 100 takes 5.6 minutes for COCO-
Stuff (40,504 images), 2.7 minutes for DeepFashion (40,000 images), 1.8 minutes for AwA
(6,985 images), and 18.2 seconds for UnRel (1,071 images).

Table A5. Single-epoch training time (in minutes) for different methods using a batch size of 200.


remove labels
remove images
split-biased
weighted
negative penalty
class-balancing
attribute decorrelation


COCO-Stuff DeepFashion AwA
8.8
8.8
0.5
8.8
8.8
8.8
8.8
12.8
-
10.0

16.8
16.8
16.1
16.7
16.8
16.8
16.9
-
-
20.9

12.9
12.8
8.4
12.9
12.9
12.8
12.8
-
17.3
13.3

F Additional results

In Figure A2, we show visual comparisons of our results and the paperʼs results reported
in Table 2 for the AwA and DeepFashion datasets. A similar plot for COCO-Stuff is pre-
sented in Figure 2 of the main paper.




Figure A2. Performance of different methods on DeepFashion and AwA. The blue and red lines
mark the paperʼs and our standard mAPs. All results can be found in Table 2.

G Additional qualitative analyses

In Figures 6 through 9 of the original paper, the CAMs produced by the CAM-based and
feature-split methods are compared to those of the standard model. Since the image IDs
of the images used in these figures were not made available, we attempted to find im-
ages that closely replicated those used in the paper.

Figures 6 and 7 of the original paper compare the CAMs of the CAM-based method against
those of the standard and feature-split method. The paperʼs comparison between the
CAM-based and feature-split models shows that the feature-split CAM regions cover both
b and c categories, whereas the CAM-based modelʼs CAM covers mostly the area of b. In
the majority of our examples, we found this distinction to be less clear (Figure A4). Like-
wise, the CAMs of our CAM-based method compared to the CAMs of our standard model
are also only slightly different, even on instances where the CAM-based model succeeds
but the standard model fails (Figure A3).

Figure 8 in the original paper gives several examples images in which the biased cate-
gories b appear away from their context c. Specifically, there are examples for which the
feature-split model was able to predict b correctly but the standard model failed to do so,
as well as some examples where both models failed. Figure A5 shows some of our own
examples. Several of the examples from the original paper also came up in our own anal-
ysis. Out of all the test images, we found 1 “skateboard” examples on which our feature-
split model was successful but our standard model failed, and 11 examples on which
both models failed. There were 3 “microwave” examples on which only feature-split was
successful and 131 examples on which neither model was successful. For “snowboard”,
there were 4 examples on which only the feature-split model was successful and 4 exam-
ples on which both failed.

Figure 9 of the original paper shows how the CAMs derived from Wo and Ws, the two
halves of the feature-split modelʼs feature subspace, focus on the object b and the context
c, respectively. We noticed the same trend in our qualitative observations (Figure A6).




Figure A3. CAMs of examples on which our CAM-based model succeeds and our standard model
fails. They are visually quite similar.

Figure A4. CAMs of examples on which our feature-split model succeeds and our CAM-based model
fails. They are visually quite similar.

Figure A5. Examples on which our feature-split model succeeds and our standard model fails are out-
lined in green (left box). Examples on which both models fail are outlined in red (right box). While
the original paper shows three examples of images containing skateboard on which the 
model succeeds but the CAM-based model fails, we only found one.




Figure A6. Interpreting the feature-split method by visualizing the CAMs with respect to Wo and
Ws. Consistent with the paperʼs observations, we see that Wo focuses on the actual category (e.g.,
handbag, snowboard, car, spoon, remote) while Ws looks at context (e.g.m person, road, bowl).




H Per-category results

In Table 2, we reported results aggregated over multiple categories. In this section, we
present per-category results for the standard, CAM-based, and feature-split methods in Ta-
bles A6 (COCO-Stuff), A7 (DeepFashion), and A8 (AwA), and compare them to the paperʼs
results. We also present our results on the UnRel dataset in Table A9.

Table A6. Per-category results on COCO-Stuff. This table together with Table A1 reproduce the
paperʼs Table 10.

Metric: mAP


cup
wine glass
handbag
apple
car
bus
potted plant
spoon
microwave

skis
clock
sports ball
remote
snowboard
toaster
hair drier
tennis racket
skateboard
baseball glove
Mean


fruit
road
road
vase
bowl
oven
mouse

building


ceiling
towel


-


29.5
33.0
34.8
35.0
2.8
3.8
24.6
29.2
36.4
36.7
41.0
40.7
38.7
37.2
13.8
14.7
41.0
35.3
44.3
44.6
5.4
2.8
49.4
49.6
3.2
12.1
22.2
23.7
5.0
2.1
6.4
7.6
1.3
1.5
55.1
53.5
21.1
14.8
2.2
12.3
23.9
24.5


30.9
35.4
38.3
36.3
3.8
5.1
25.5
29.8
39.2
38.2
43.8
41.6
40.2
37.8
14.9
16.3
43.4
36.6
46.9
42.9
14.1
7.0
50.5
50.5
6.5
14.7
24.8
26.9
11.6
2.4
6.5
7.7
1.3
1.3
58.5
59.7
30.5
22.6
7.2
14.4
26.9
26.4


23.2
27.4
36.3
35.1
4.0
2.8
25.6
30.7
36.5
36.6
43.3
43.9
37.8
36.5
13.3
14.3
41.8
39.1
45.2
47.1
26.8
27.0
43.6
45.5
22.5
9.5
20.4
21.2
12.7
6.5
6.2
6.4
1.7
1.5
61.6
61.7
42.0
34.4
31.7
34.0
28.1
28.8


61.7
68.1
55.9
57.9
40.6
42.8
65.6
64.7
79.1
79.7
85.1
86.0
48.7
50.0
35.6
42.7
60.2
60.9
84.4
85.0
90.6
91.5
84.7
84.5
70.9
75.5
70.3
70.5
75.6
73.0
6.1
5.0
7.6
6.2
97.4
97.6
91.7
91.3
88.9
91.0
65.0
66.2


59.2
63.0
54.0
57.4
40.3
41.4
65.0
64.4
78.0
78.5
84.3
85.3
46.2
46.8
33.3
35.9
59.5
60.1
83.9
83.3
90.7
91.3
84.6
84.7
70.7
75.3
68.1
67.4
75.7
72.7
5.0
5.0
7.7
6.2
97.4
97.5
91.7
91.1
89.0
91.3
64.2
64.9


63.7
70.2
55.4
57.3
41.0
42.7
62.6
64.1
78.7
79.2
84.3
85.4
44.9
46.0
36.3
42.6
59.3
59.6
83.8
85.1
90.5
91.2
86.6
86.4
69.7
74.2
71.4
72.7
74.9
72.6
5.1
4.4
11.4
6.9
97.3
97.5
91.1
90.8
88.6
91.1
64.8
### 66.0 Table A7. Per-category results on DeepFashion. This table together with Table A2 reproduce the
paperʼs Table 11.

Metric: top-3 recall


bell
cut
animal
flare
embroidery
suede
jacquard
trapeze
neckline
retro
sweet
batwing
tassel
boyfriend
light
ankle
french
dark
medium
studded
Mean


lace
bodycon
print
fit

fringe
flare
striped
sweetheart


loose

distressed


terry
wash
wash
denim
-


14.1
10.9
0.0
19.4
5.4
18.5
0.0
16.5
0.6
0.0
0.0
7.0
15.3
17.7
4.0
7.3
0.0
0.5
0.0
2.1
7.0

5.4
8.6
0.0
18.4
4.1
12.0
0.0
8.7
0.0
0.0
0.0
11.0
13.0
11.6
2.0
1.0
0.0
2.6
0.0
0.0
4.9


21.7
22.8
15.2
12.5
11.5
1.9
29.1
32.0
3.6
1.8
22.8
19.6
6.5
0.9
30.7
29.9
1.3
0.0
1.3
0.4
3.7
0.5
14.0
12.0
23.7
16.8
20.0
11.6
6.4
1.3
11.5
14.6
6.6
0.8
3.1
2.1
0.00
0.0
10.5
3.2
12.2
9.2


9.4
37.9
1.9
41.9
4.8
65.2
9.1
35.7
0.0
0.0
3.5
22.5
62.5
57.1
17.0
35.3
20.2
2.9
5.7
24.0
22.8

3.1
29.3
1.9
56.0
4.8
65.2
0.0
42.9
0.0
0.0
0.0
27.5
25.0
49.2
14.9
13.2
9.6
8.7
0.0
4.0
17.8


15.6
44.8
9.4
56.2
0.00
73.9
18.2
64.3
0.0
0.0
3.5
20.0
62.5
50.8
12.8
32.4
30.9
15.9
2.9
28.0
27.1

9.4
36.2
2.8
62.0
0.0
73.9
9.1
50.0
0.0
0.0
0.0
15.0
25.0
38.1
8.5
27.9
7.9
13.0
0.0
24.0
### 20.1 Table A8. Per-category results on AwA. This table together with Table A3 reproduce the paperʼs
Table 12.

Metric: mAP


white

forager
lean
fish
hunter
plains
nocturnal

jungle

meat
mountains
tree

spots
bush
buckteeth
slow
blue
Mean


ground


timid
big

white
meatteeth

black
fish
paws
tail
inactive

meat
smelly
strong
coastal
-


27.5
24.8
12.0
18.5
30.9
33.6
12.3
11.5
54.6
60.2
3.4
4.1
13.4
6.4
12.0
13.3
14.3
13.4
30.4
33.3
10.1
9.3
3.7
4.5
9.8
10.9
42.7
36.5
13.1
11.9
46.9
43.8
20.1
19.8
9.1
7.8
15.0
15.5
8.2
8.4
19.5
19.4


31.5
24.6
9.4
29.1
30.5
33.4
10.9
12.0
54.4
57.4
3.2
3.6
7.6
6.0
13.2
13.1
15.0
14.9
32.2
31.3
10.0
9.3
3.3
3.8
8.3
10.0
41.1
55.0
13.2
13.1
49.7
45.2
19.7
22.1
9.3
8.9
15.0
14.6
7.6
8.2
19.3
20.8


86.3
85.8
79.8
89.4
95.5
96.6
51.9
54.5
97.8
98.3
34.8
32.9
39.8
44.7
55.5
71.2
62.1
62.8
86.3
88.6
79.3
76.6
67.7
76.1
51.6
49.9
93.8
93.2
71.7
73.7
42.6
61.8
43.1
70.2
49.1
27.1
96.4
95.8
94.8
94.2
69.0
72.2


82.6
86.2
75.3
89.3
94.6
96.5
55.4
55.8
97.8
98.3
42.4
30.0
55.3
59.9
48.7
60.5
57.1
67.6
86.7
86.6
81.5
73.6
65.0
73.6
48.5
39.9
91.4
92.7
75.2
76.6
39.3
59.1
41.7
75.1
40.0
45.3
96.6
93.3
97.0
95.8
68.6
### 72.8 Table A9. Per-category mAP results on UnRel. The paper doesnʼt report per-category results, so we
only report ours. Next to the category names are the numbers of images (out of 1,071) in which
the category appears.


remove labels
remove images
split-biased
weighted
negative penalty
class-balancing


car (198)
70.0
70.6
71.6
60.8
71.8
70.6
70.6
72.0
70.8

bus (11)
44.4
42.2
50.0
25.9
39.5
42.0
40.7
40.2
42.2

skateboard (12) Mean
43.0
42.7
48.6
29.2
44.4
42.5
42.3
46.8
49.9

14.5
15.2
24.3
0.9
22.0
15.0
15.5
28.2
36.7




I Reproducibility plan

For reference, we provide the reproducibility plan we wrote at the beginning of the
project. Writing this plan allowed us to define concrete steps for reproducing the experi-
ments and understand non-explicit dependencies within the paper. We suggest putting
together a similar plan as the order in which materials are presented in the paper can
be different from the order in which experiments should be run.

Reproducibility plan

The original paper points out the dangers of contextual bias and aims to accurately rec-
ognize a category in the absence of its context, without compromising on performance
when it co-occurs with context. The authors propose two methods towards this goal: (1)
a method that minimizes the overlap between the class activation maps (CAM) of the
co-occurring categories and (2) a method that learns feature representations that decor-
relate context from category. The authors apply their methods on two tasks (object and
attribute classification) and four datasets (COCO-Stuff, DeepFashion, Animals with At-
tributes, UnRel) and report significant boosts over strong baselines for the hard cases
where a category occurs away from its typical context.

As of October 20th, 2020, the authorsʼ code is not publicly available, so we plan to re-
implement the entire pipeline. Specifically, we would like to reproduce the paper in the
following order:

1. Data preparation: We will download the four datasets and do necessary processing.

2. Biased categories identification: The original paper finds a set of K=20 category pairs
that suffer from contextual bias. We would like to confirm that we identify the
same biased categories in COCO if we follow the process described in Section 3.1.
and Section 7 in the Appendix.

3. Baseline: We will train the standard classifier (baseline) by fine-tuning a pre-trained
ResNet-50 on all categories of COCO. The authors describe this part as stage 1 train-
ing.

4. CAM-based method: We will implement the proposed method which uses CAM for
weak local annotation. Then using the standard classifier as the starting point, we
will do stage 2 training with this method and check whether it outperforms the
standard classifier.

5. Feature splitting method: We will implement the proposed method which aims to
decouple representations of a category from its content. Then we will do stage 2
training with this method and check whether it outperforms the standard classifier
and the CAM-based method.

6. Qualitative analysis: Once we have trained standard, ours-CAM, and ours-feature-
split classifiers, we can re-create visualizations in Figures 6-9 using CAM as a visu-
alization tool. We will compare our visualizations with the figures in the paper.

Successfully finishing 1-6 will reproduce the main claim of the paper. Afterwards, we
plan to reproduce the remaining parts of the paper as time permits.

7. Strong baselines: In addition to the baseline standard classifier, the authors com-
pare their two proposed methods to the following strong baselines: class balanc-
ing loss, remove co-occur labels, remove co-occur images, weighted loss, and neg-
ative penalty. With these additional baselines, we will be able to reproduce Table
2 in full.




8. Cross dataset experiment on UnRel: The authors test the models trained on COCO
on 3 categories of UnRel that overlap with the 20 biased categories of COCO-Stuff.
This experiment should be straightforward to run once the UnRel dataset is ready.

9. Attribute classification on DeepFashion and Animals with Attributes: To reproduce
attribute classification experiments, we will compare performance of standard,
class balancing loss, attribute decorrelation, and ours-feature-split classifiers on
DeepFashion and Animals with Attributes datasets.

---
**Source PDF:** `f6dbf619213c.pdf` (2021_08_article.pdf)  
**URL:** https://zenodo.org/record/4834352/files/article.pdf
