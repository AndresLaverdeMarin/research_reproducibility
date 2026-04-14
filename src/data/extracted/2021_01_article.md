R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Explaining Groups of Points in Low-Dimensional
Representations

Rajeev Verma1, ID , Jim J. O. Wagemans1, Paras Dahal1, ID , and Auke Elfrink1
1University of Amsterdam, The Netherlands

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4835602

Reproducibility Summary

Scope of Reproducibility

This report covers our reproduction of the paper ʼExplaining Low dimensional Repre-
sentationʼ [1] by Plumb et al. In this paper, a method (Transitive Global Translations,
TGT) is proposed for explaining different clusters in low dimensional representations of
high dimensional data. They show their method outperforms the Difference Between
the Means (DBM) method, is consistent in explaining differences with few features and
matches real patterns in data. We verify these claims by reproducing their experiments
and testing their method on new data. We also investigate the use of more complex
transformations to explain differences between clusters.

Methodology

We reproduce the original experiments using their source code. We also replicate their
findings by re-implementing the authorsʼ method in PyTorch [2] and evaluating on two
of the dataset used in the paper and two new ones. Furthermore, we compare TGT with
our own extension of TGT, which uses a larger class of transformations.

Results

We were able to reproduce their results using their code, yielding mostly similar results.
TGT generally outperforms DBM, especially when explanations use few features. TGT
is consistent in terms of the features to which it attributes cluster differences, across
different sparsity levels. TGT matches real patterns in data. When extending the types of
functions used for explanations, performance did not improve significantly, suggesting
translations make for adequate explanations. However, the scaling extension shows
promising performance on the modified synthetic data to recover the original signal.

What was easy

The easiest part was running the existing code with the pre-trained model files. The
original authors had set up their code base in an organized manner with clear instruc-
tions.


Code is available at https://github.com/elfrink1/FACT. – SWH swh:1:dir:445130f59283e6dce7df5eb72dd346a5c57c9230.
Open peer review is available at https://openreview.net/forum?id=cqAHExg2f.




What was difﬁcult

The first difficulty that we encounter was finding the right environment. The source
code depends on deprecated functionality. The clustering method they used, had to be
re-implemented for us to use it in our replication. Another difficulty was the selection
of clusters. The authors did not prove a consistent method for selecting clusters in a
latent space representation. When retraining the provided models, we get a latent space
representation different to the original experiments. The clusters have to be manually
selected. The metrics that they used to evaluate their explanations are also depend on
the clustering. This means that there is some variability in the exact verification of
reproducibility.

Communication with original authors

We asked the original authors for clarification on how to choose the ϵ hyper-parameter.
However, it became apparent that we had misread, and the procedure is indeed ade-
quately reported in the paper.




## 1 Introduction

The curse of dimensionality [3] is a long-standing problem in Machine Learning. Data in
many domains and applications (e.g. Bioinformatics) has high-dimensional represen-
tations. Finding patterns in such high-dimensional data is a challenging task. To this
end, dimensionality reduction [4] techniques have greatly helped in data-analysis, infor-
mation extraction, building computational models, and in doing inference. Given an
r(x) 2 Rm,
input x 2 Rd, dimensionality reduction learns a function r : x 7! r(x),
where m << d. Such a dimensionality reduction function r naturally arises in deep
learning due to the expressivity and representational power of neural networks. The
goal of r is to encode useful knowledge about the input space, thus providing distinc-
tive information in the transformed output r(x). This results in “clusters” or “groups
of points” in the transformation space. The downside of this exercise, however, is that
the output space is usually non-interpretable. There is usually no easy way to know
what information is present in the transformed points r(x) and what sort of distinctive
knowledge they contain.
In this work, we reproduce the paper ʻExplaining Groups of Points in Low-Dimensional
Representationsʼ by Plumb et al. [1]. This paper proposes a method for explaining differ-
ent clusters in latent space representation. They look at the problem of explaining the
points in the latent space representation through the lens of Interpretability in Machine
Learning. We reproduce their findings and expand upon their work with our an exten-
sion. We extend their research by applying their method to a larger class of explanation
functions and testing their method on new dataset. We further investigate the efficacy
of the explanations using a probing classifier [5].

## 2 Methodology

Counterfactual Explanations [6] have emerged as an active research area in the field of
Interpretable Machine Learning. A counterfactual explanation is defined as the small-
est perturbation to the input that would change the output of a machine learning model.
As such, these explanations are promising as they can provide suggestive recourse to the
beneficiary in a machine learning based decision system. As an interpretable machine
learning problem, Plumb et al. [1] aim to find such counterfactual explanations in order
to explain the differences between the groups in latent space. To this end, they employ
the function r itself to find what perturbation δ needs to be made to the input x 2 Rd
so that r(x + δ) belongs to the different target group. The goal is to find the global ex-
planations that apply to the whole group as opposed to the local explanations which ex-
plain only individual examples [7]. Furthermore, the explanations need to be sparse for
them to be interpretable by practitioners. Finally, these explanations should be be both
symmetric and transitive. To obtain these Global Counterfactual Explanations(GCE), the
authors propose the algorithm called, Transitive Global Translations (TGT), explained
hereafter.
Following the previous notation, let r : Rd ! Rm denote our dimensionality reduction
function, where d is the dimensionality of the input space and m is the latent spaceʼs
dimensionality. Suppose Xi, Xj (cid:26) Rd get mapped to the clusters Ri, Rj (cid:26) Rm respec-
tively. The goal is to define the transformation ti→j : Rd ! Rd on x 2 Xi as x
= ti→j(x),
′ 2 Xj.
so that r(x
The proposed algorithm TGT considers the transformations of the form ti→j(x) = x +
δi→j. To find the optimal parameters of the transformation function, authors imply a
compressed-sensing based objective function as below:

) 2 Rj, or equivalently x

′

′

l(δi→j) = kr(ti→j( ¯Xi)) (cid:0) ¯Rjk2

2 + λkδi→jk1

(1)

where λkδi→jk1 is a regularization term to incentivize sparser explanations, and ¯Xi 2




Rd and ¯Rj 2 Rm denote the means of the clusters in the input space and latent space
respectively. Given clusters 0, 1, . . . , n, we get a total of 1
2 n(n + 1) transformations. To
further increase sparsity, we can truncate δi→j to only the k features with the largest
absolute value, for some k. An issue with this is that the translation using the truncated
δi→j might no longer correctly transform inputs that get mapped to Ri into inputs that
get mapped to Rj.
Furthermore, the transformations ti→j have to adhere to several mathematical proper-
ties. Namely, for any clusters i, j, k these transformations should be : a) Symmetric, i.e.
−1 and b) Transitive, i.e. tj→k (cid:14) ti→j = ti→k. From these properties it follows
ti→j = tj→i
that ti→i is the identity function I as

ti→i = ti→0 (cid:14) t0→i = ti→0 (cid:14) ti→0

−1 = I

(2)

We define this condition as self-similarity. Furthermore, the group of translations is
uniquely defined by t0→1, . . . , t0→n, because for any i, j:

ti→j = t0→j (cid:14) ti→0 = t0→j (cid:14) t0→i

−1

(3)

Plumb et al. [1] compare their method against the naive baseline of Difference Between
the Means (DBM). With DBM, each transformation is still a translation: ti→j(x) = x +
δi→j. However, now δi→j = ( ¯Xj (cid:0) ¯Xi). We also use this as a baseline for comparison in
this report.
Since translations are a very narrow class of functions, we expanded upon the research
by investigating other transformations that still satisfy the GCE requirements. We inves-
tigate the transformations of the form t0→i(x) = exp(γ0→i) (cid:12) x + δ0→i. These always
−1(x) = exp((cid:0)γ0→i) (cid:12) (x (cid:0) δ0→i) and only
have a well defined inverse, given by t0→i
have O(d) parameters. The inclusion of scaling could enhance performance, while the
necessary components of GCE are maintained.

### 2.1 Metrics to evaluate Global Counterfactual Explanations

To measure the efficacy of the transformation function ti→j, the authors propose two
metrics, Coverage and Correctness.

1. The Coverage (cv(ti→j)) is the fraction of points a 2 Rj for which there is a point

b 2 Xi such that kr(ti→j(b)) (cid:0) ak2 < ϵ, i.e.

I [9b 2 Xijkr(ti→j(b) (cid:0) ak2 < ϵ]

(4)

cv(ti→j) =


jRjj

∑

a∈Rj

cr(ti→j) =


jXij

∑

a∈Rj

2. The Correctness (cr(ti→j)) is the fraction of points b 2 Xi for which there is some

a 2 Rj such that kr(ti→j(b)) (cid:0) ak2 < ϵ, i.e.

I [9a 2 Rjjkr(ti→j(b) (cid:0) ak2 < ϵ]

(5)

Note that both these metrics have the hyperparameter ϵ which is to be chosen carefully.
When i = j we do not count the point itself, there must be some other point within
distance ϵ. 1
Furthermore, the Similarity metric measures the consistency of the explanations at dif-
ferent sparsity levels. Given two explanations e1, e2 where e1 is more sparse than e2, the
similarity of e1 and e2 is defined as

∑
i

sim(e1, e2) =

je1[i]j1(e2[i] 6= 0)

ke1k1

(6)

This is equal to 1 if e1 uses a subset of the features that e2 uses. By definition, DBM
always has similarity 1.

1We use this definition to set the value for epsilon, as explained in the Methodology section of the original

Paper.




## 3 Scope of Reproducibility

We investigate the following claims from the original paper:

1. In terms of the average correctness and coverage, TGT performs equally well or
better than the DBM method. This remains true, especially for sparser explana-
tions.

2. TGT explanations have similarity close to 1. It is consistent in which features it

uses for explanations across different sparsities.

3. TGT correctly identifies known causal structure in data.

4. Furthermore, TGT explanations are consistent. When altering the dataset by adding
a copy of a cluster with a specific feature altered, TGT recovers the modification
with little change to the other explanations.

## 4 Methodology of Reproducibility

We make use of the code made available by the original authors 2 for our pilot inves-
tigative study. We first verify that the provided models and explanations stay true to the
claims made in the paper. We further retrain their models on the provided dataset. We
also made our own PyTorch [2] implementation to to further verify the claims, and to
perform experiments with the proposed extension.

### 4.1 Model description

We assert that the scope of the original paper is to explain clusters in the low-dimensional
representations. However, obtaining meaningful and discernible low-dimensional rep-
resentations is an active area of research. The original authors employ a t-SNE [8] objec-
tive based Variational Autoencoder (called, henceforth, as scVIS) [9] as the r function.
They make use of library3 by the original scVIS authors in their implementation. We
also implement this model in Pytorch for our experiments. However, we deliberately
decide not to match the model implementation exactly. This is done to study the model-
agnosticism of the TGT algorithm. By design, TGT should be able to explain the clusters
for any differentiable r function. However, we maintain that r should give discernible
latent representations with preserved global structure in the data. In our implemen-
tation of the scVIS library, we therefore do not employ the hyperparameters and the
training settings from the original library.

### 4.2 Dataset Description

We reproduce the findings of the authors on four datasets that they used. We use two of
these datasets as well as two new ones to test our PyTorch implementation.

1. Single cell RNA [10]: This dataset has 13166 features. We use the same number of

clusters at the original authors, 18 in this case.

2. UCI Boston housing This dataset has 506 entries with 13 features. We use 6 clusters

for both reproduction and replication.

3. UCI Heart disease This dataset has 303 entries with 13 features and 1 binary la-
bel. We used 8 clusters in the reproduction and 4 in the replication. The data was
normalized to be in the range [0, 1].

2https://github.com/GDPlumb/ELDR
3https://github.com/shahcompbio/scvis




4. UCI Iris This dataset has 150 entries with 4 features and 1 ternary label. Ran in the

reproduction with 3 clusters. N = 150

5. Breast Cancer Wisconsin (Diagnostic) 4 This dataset has 569 entries with 30 fea-

tures and 1 binary label. We use 3 clusters in the replication.

6. Pima Indians Diabetes Database 5 This dataset has 768 entries with 8 features and
1 binary label. We used 3 clusters in the replication. The data was normalized to
be in the range [0, 1].

Note that the number of clusters depend on the latent-space representation, and
thus, are user dependent.

### 4.3 Hyperparameters

Tensorflow [11] Experiments For the reproduction of the original experiments, we use
the same hyperparameters as the original authors.

Pytorch For our implementation of the scVIS model, we use l2 regularization of 0.001,
learning rate 0.01, and perplexity of 10. Furthermore, the degree-of-freedom for the stu-
dentT distribution is set to 2.0. Perplexity and the degree-of-freedom is used same as
the original scVIS implementation. We use validation set to monitor the training pro-
cess of the scVIS model, and stop training when the ELBO(Evidence Lower BOund)[12]
stops improving. For training the TGT explanations, we closely follow the settings from
Plumb et al. [1]. We initialize the deltasδs as zero vectors. We tune the regularization
parameter λ by grid search over a fixed range [0.0, 5.0] incremented by 0.5. Defining
the metrics for TGT requires careful setting of the ϵ hyper-parameter. We follow the
self-similarity condition (transformations of clusters to themselves should, theoretically,
have correctness and coverage to be 1.0), and increase the ϵ in the range [0.0, 2.0] with
increments of 0.02 until the correctness and coverage metrics are greater than 0.95. Fur-
thermore, we use the truncation values(TV)(refer Table 1) to evaluate on the sparsity of
the explanations. For the Pima Indians Diabetes Database and Breast Cancer Wiscon-
sin(Diagnostic) dataset, we use the same truncation values as for UCI Boston Housing
dataset.

Dataset

Truncation Values(TV)

Single Cell RNA 50, 100, 250, 500, 1000, 15000
Heart Disease
Housing
Iris

1, 3, 5, 7, 9, 11, 13
1, 3, 5, 7, 9, 11, 13
1, 2, 3, 4

ϵ
0.75
1.0
1.5
0.75

Table 1. Truncation Values (TV) and ϵ value used for each of the dataset.

### 4.4 Experimental setup and code

We closely follow the experimental setup in the original paper for our experiments. We
make our Pytorch code available 6 to further support the reproducible research. We
reran the code of the original authors with new clustering models and new explanations.
We optimize the compressed-sensing based objective function for the TGT algorithm
using the gradient descent algorithm. Our scaling extension is easily integrated in the
source code, and can be optimized in a similar way. We train the scVIS models on the
Lisa computing cluster 7. We use approximately 30 hours of GPU time. We train the TGT

4https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
5https://www.kaggle.com/uciml/pima-indians-diabetes-database
6https://github.com/elfrink1/FACT
7https://userinfo.surfsara.nl/systems/lisa




Explanation
0 ! 1
0 ! 1
0 ! 3

x1
-1.01
-1.05
0.00

x2
-0.02
0.99
0.89

x3
0.00
0.00
0.00

x4
-0.88
-0.88
0.00

Table 2. Explanations for the synthetic dataset as given by our implementation. Note that both
DBM and TGT are able to infer that the x3 is not causing any cluster. However, the authorsʼ claim
that TGT also discovers that x4 doesnʼt cause any cluster cannot be verified.

explanations on CPU (Intel i5).

## 5 Results

For the reproduction of the authorsʼ experiments, we achieve approximately similar re-
sults to the original paper. The TGT method does seem to outperform DBM method.
The TGT explanations also have high similarity across sparsity levels. However, the
TGT algorithm is unable to identify known causal structure in synthetic data with as
good precision as reported in the original paper. We are also unable to match the re-
sults on the modified and corrupted data to a good precision. We describe the results in
the following sections:

### 5.1 Results reproducing original paper

Coverage, Correctness and similarity — In figure 1, we can see a comparison between the
correctness, coverage and similarity of the TGT and DBM methods. Note that the DBM
always has similarity 1. The similarity of TGT stays between 1 and 0.9, which supports
claim 2.
We see that the coverage and correctness are similar for the UCI Heart disease dataset.
On the UCI Iris dataset, the coverage is comparable but the correctness is better for TGT.
In both housing and RNA, the coverage and correctness are better at less features and
similar for more features. Overall, these results support claim 1, especially for a small
amount of features.

Figure 1. Comparison of the metrics(Correctness, Coverage, and Similarity) across different
datasets for reproduction experiments.

### 5.2 Explaining Causal Structure in the Synthetic Data

We verify the claim that TGT identifies the causal structure in the data (claim 3). The syn-
thetic dataset is generated same as the original paper, i.e. x1, x2 (cid:24) N (0, 0.2)+ Bern(0.5),
x2 (cid:24) N (0, 0.05), x4 (cid:24) x1 + N (0, 0.05). Note that this dataset has four different clusters,
caused by the first two dimensions x1 and x2, x3 is noise, and x4 is correlated with x1 and
x2. The authors claim that for this synthetic data, TGT is able to find that x4 is not the
cause for any group. However, the said claim cannot be re-verified. Interestingly, the
re-run of their code doesnʼt provide the justification either to the degree as mentioned




in the paper. We observe that both TGT and DBM are able to identify x3 is not causing
any groups. Thus, in this scenario, both TGT and DBM are comparable. Refer table 2
for the explanations obtained. We, hereby note, that the explanations vary across multi-
ple runs and we use the experimental setup same as the original authors. However, the
values across the third dimension are consistently approximately 0.

Feature modiﬁcations — For each of the UCI datasets, the original authors add a ʻcorruptedʼ
version where an extra cluster is added with artificial feature modification. With the
exception of the modified features, the corrupted class is a copy of a chosen target
class. They train TGT explanations using both the original scVIS model for the respec-
tive dataset and a model retrained on the corrupted dataset. We reproduce these experi-
ments to see if TGT correctly attributes the difference between the target and corrupted
class to the right features. Refer to Appendix 7.1 for the illustrated figures and descrip-
tion. Overall, we observe that TGT is unable to identify the modifications to as good a
precision as reported in the original paper. TGT is able to identify the modification for
the UCI Iris dataset. For UCI Heart Disease Dataset (figure 7), it does not identify the
features modified and on the UCI Boston Housing Dataset (figure 6), it identifies noisy
modifications. However, with the retrained scVIS model and new representations, TGT
is consistent in identifying the modifications across all the datasets.

### 5.3 Results beyond original paper

PyTorch replication — We also replicate the TGT algorithm in PyTorch. Our Pytorch im-
plementation includes the entire method along with the scVIS clustering method. In
our implementation, we use the Scikit learn 8 kmeans module for our cluster selection
as opposed to the manual clustering in the Tensorflow implementation. However, our
number of clusters argument to the kmeans algorithm was informed by the learned
low-dimensional representations for each dataset. Due to differences in the clustering
model and cluster selection, we cannot directly compare the coverage and correctness
metrics between our Pytorch replication and the TensorFlow reproduction. We addi-
tionally experiment with our scaling extension to the TGT algorithm. In the scaling ex-
tension of the TGT algorithm, along with the δ (δ) parameters, each cluster now has a γ
(γ) parameters. The transformation from cluster 0 to i is now given by: t0→i = eγi (cid:12)x+δi
The gammas(γs) are truncated just like the deltas and their L1 norm is added to the reg-
ularization term. Note that these transformations are strictly more expressive. If γ is
the zero vector, these transformations reduce to regular TGT.

UCI Heart Disease and UCI Boston Housing Dataset — In figure 2 we see the results of our repli-
cation on the UCI Boston Housing and UCI Heart Disease dataset. For the UCI Boston
Housing data, the TGT method seems to slightly outperform DBM both with and with-
out scaling. This supports claim 1. The deltas(δs) and gammas(γs) show high similarity,
supporting claim 2. For the UCI Heart Disease dataset, we do not see a difference in
performance without scaling while TGT with scaling performs slightly worse.

Figure 2. Results for the PyTorch replication for UCI Boston Housing and UCI Heart Disease dataset.

8https://scikit-learn.org/stable/index.html




Breast Cancer Wisconsin (Diagnostic) and Pima Indians Diabetes Database — In figure 3 we see
the results for the Pima Indians Diabetes and Breast Cancer Wisconsin (Diagnostic)
dataset. For the diabetes dataset, TGT with and without scaling outperforms DBM when
more than one feature is used. This supports claim 1. Since the delta (δ) similarity is
close to 1, claim 2 is also supported. For the Breast Cancer dataset, we see similar per-
formance for DBM and TGT and slightly worse performance with scaling. The deltas
(δs) still have high similarity, supporting claim 2.

Figure 3. Results of the PyTorch replication on PIMA Indians Diabetes and Breast Cancer Wisconsin
(Diagnostic) Dataset.

=

Scaling extension — In figure 2, we can see the difference in performance on two dataset
included in the original experiments. Scaling does not seem to improve performance on
the UCI Boston Housing dataset and slightly decreases performance on the UCI Heart
Disease dataset. The similarity of the gammas (γs) is mostly above 0.9.
In figure 3, we see the same metrics for the Breast Cancer and Pima Indians Diabetes
Dataset. For the Diabetes dataset, the performance improves slightly and the gammas(γs)
show high similarity. For the Breast Cancer dataset, the performance is about the same
but the gammas(γs) show relatively low similarity.
Altogether, these results suggest that the addition of scaling does not significantly im-
prove the accuracy and correctness while making the transformations more complex.
Based on our experiments, we do not recommend the addition of scaling in the expla-
nation functions, and conclude that the original TGT is expressive enough.

′

′

) should form a different group of its own. b) G

Experiment with Modiﬁed Synthetic Data — In order to study the efficacy of the proposed
scaling function, we perform experiments on the synthetic dataset. We modify one of
the groups of points G by performing the operation axk
i + b, where i corresponds to
the group number and k denotes the feature dimension which we modify. We define
a (cid:24) U (1.0, 2.0) and b (cid:24) U ((cid:0)0.5, 1.0). We add modified group G′ into the original data D
to get the new data D
. We follow the experiment setup from the original paper as: a)
r(G
should be within the distribution of
the original D. In this study, we want to investigate whether the TGT with scaling is able
to recover the modifications, and if in doing so it affects the explanations between other
groups. The sampling procedure gave a=2.0, b=0.60 and we keep k=0. We observe that
the explanations with scaling are able to recover the modification to an approximate
degree(scaling factor eγ (cid:25) 2.38, actual a=2.0), and give better correctness as compared
to the regular TGT (refer figure 3). Interestingly, the translations explanations of the
scaling extension are approximately equal to the deltas of the regular TGT. The exact
results can be found in Table 3. Figures 8 and 9 in the appendix show the data spread
and resulting translations.

′

Experiments with Probing Classiﬁer — To further investigate the efficacy of TGT explanations,
we use a probing-classifier [5] as a proxy to study the qualitative differences of the fea-
tures selected by TGT and DBM. For each cluster, we train a binary classifier with fea-
tures ranked highest by TGT and DBM at different sparsity levels K. We compute the
overall accuracy at each sparsity level using the ensemble of these binary classifiers.




0 to 1

1 to 0

Cr


Cv
0.529
0.529

Cr
0.333
0.520

Cv
1.000
1.000

TGT
Scaling

δ1

2.581
2.608

δ2

0.014
0.023

δ3

0.001
-0.001

δ4

0.842
0.927

γ1

-
0.879

γ2

-
0.009

γ3

-
0.002

γ4

-
0.007

Table 3. The deltas(δs) and gammas(γs) for the mapping from group 0 to group 1 on the modi-
fied synthetic dataset for regular TGT and TGT with scaling. Cr and Cv indicate correctness and
coverage, respectively.

Figure 4. Classification accuracy of probing classifier at different sparsity levels for Housing (left)
and Iris (right) dataset.

As can be seen in Figure 4, the results demonstrate that for sparser explanations, TGT
selects features that lead to higher accuracy of the ensemble classifier than those se-
lected by DBM. This further validates the paperʼs claim that TGT leads to better sparse
explanations as compared to DBM. Furthermore, we also use the probing classifier to un-
derstand the differences between the groups. For each pair of group, we train a Binary
Linear Classifier to predict the group of a test point. We, then, investigate the feature
importances of the classifier towards decision making. We ascertain that the features
classifier give more importance to while decision making are the defining property of
the class. Interestingly, we find that the more important features according to the clas-
sifier correspond to the explanations provided by the TGT algorithm. Refer to figure
11. This provides further evidence that TGT is able to find real distinctive signals as
explanations.

## 6 Discussion

Based on the reproduction of the original experiments, claims 1 and 2 seem to hold, the
experiments for claim 4 do not all support it, but the claim does seem to hold. Claim 1
and 2 seem to hold in particular for sparse explanations. The evidence for claim 3 is in-
conclusive. The coverage and correctness in our reproduction were not always the same
as in the original paper. It is difficult to compare these metrics for different clustering
outcomes, as they depend on the ϵ parameter which depends on the clustering.
A major difficulty in reproduction is the cluster selection. When retraining the scVIS
model, the latent space representation structure changes. The authors provide deter-
mine the different clusters by visual inspection. Cluster selection could be an explana-
tion for the differences in results between the original experiments and our reproduc-
tion. To verify the results with more confidence, a robust method for cluster selection
might be required.

References

1. G. Plumb, J. Terhorst, S. Sankararaman, and A. Talwalkar. Explaining Groups of Points in Low-Dimensional

Representations. 2020. arXiv:2003.01640 [cs.LG].




2.

A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, et al.
“Pytorch: An imperative style, high-performance deep learning library.” In: arXiv preprint arXiv:1912.01703
(2019).
C. M. Bishop. Pattern Recognition and Machine Learning. Springer, 2006.

3.
4. H. Xie, J. Li, and H. Xue. A survey of dimensionality reduction techniques based on random projection. 2018.

5.

6.

7.

8.

9.

10.

arXiv:1706.04371 [cs.LG].
Y. Belinkov, S. Gehrmann, and E. Pavlick. “Interpretability and Analysis in Neural NLP.” In: Proceedings of the
58th Annual Meeting of the Association for Computational Linguistics: Tutorial Abstracts. Online: Asso-
ciation for Computational Linguistics, July 2020, pp. 1–5. DOI: 10.18653/v1/2020.acl-tutorials.1. URL: https:
//www.aclweb.org/anthology/2020.acl-tutorials.1.
S. Verma, J. Dickerson, and K. Hines. Counterfactual Explanations for Machine Learning: A Review. 2020.
arXiv:2010.10596 [cs.LG].
D. V. Carvalho, E. M. Pereira, and J. S. Cardoso. “Machine learning interpretability: A survey on methods and
metrics.” In: Electronics 8.8 (2019), p. 832.
L. Van der Maaten and G. Hinton. “Visualizing data using t-SNE.” In: Journal of machine learning research
9.11 (2008).
J. Ding, A. Condon, and S. P. Shah. “Interpretable dimensionality reduction of single cell transcriptome data with
deep generative models.” In: bioRxiv (2017). DOI: 10.1101/178624. eprint: https://www.biorxiv.org/content/
early/2017/09/01/178624.full.pdf. URL: https://www.biorxiv.org/content/early/2017/09/01/178624.
K. Shekhar et al. “Comprehensive Classiﬁcation of Retinal Bipolar Neurons by Single-Cell Transcriptomics.” In:
Cell 166 (Aug. 2016), 1308–1323.e30. DOI: 10.1016/j.cell.2016.07.054.

11. M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen, C. Citro, G. S. Corrado, A. Davis, J. Dean, M. Devin,
et al. “Tensorflow: Large-scale machine learning on heterogeneous distributed systems.” In: arXiv preprint
arXiv:1603.04467 (2016).
D. P. Kingma and M. Welling. Auto-Encoding Variational Bayes. 2014. arXiv:1312.6114 [stat.ML].

12.

## 7 Extra ﬁgures

### 7.1 Experiments on Corrupted datasets

Figure 5. Explanation for corrupted features on UCI Iris dataset. Feature modified is 1(Sepal Width).
Left: Visualization of the TGT explanations on the modified dataset. Right: Visualization of the
TGT explanations with scVIS retrained on the modified dataset. We observe that the TGT explana-
tions are robust to the modifications.




Figure 6. Explanation for corrupted features on UCI Boston Housing dataset. We modify the fea-
tures 1(ZN) and 9(TAX). Left: Visualization of the TGT explanations on the modified dataset. We
observe that TGT returns noisy explanations in this case. Right: Visualization of the TGT expla-
nations with scVIS retrained on the modified dataset. With retrained scVIS model, TGT is able to
recover the modifications.

Figure 7. Explanation for corrupted features on UCI Heart Disease dataset. Left: Visualization of
the TGT explanations on the modified dataset. We modified the 6(restecg) and 8(exang). However,
the TGT recovers modifications in features 2(cp), 5(fbs), and 10(slope) instead. Right: Visualiza-
tion of the TGT explanations with scVIS retrained on the modified dataset. With retrained scVIS
model, TGT recovers the modified features along with 10(slope) feature. This observation does
not entirely support the claim 4.




### 7.2 Synthetic data

Figure 8. a) Synthetic data b) Synthetic data with the modification applied. We modify the data
from group 1 across the 0th dimension by ax0

1 + b. Here a and b are 2.0, 0.60 respectively.

Figure 9. We compare the explanations from the TGT algorithm (left) and the TGT with scaling
extension algorithm(right) on the modified synthetic data. We can observe that the TGT with
scaling extension has better correctness, and is able to identify the scaling we have applied across
the first dimension (i.e. k=0). The γ for this dimension is 0.87, which means the scaling factor is
eγ ≈ 2.38. Moreover, the translation parameters are approximately same in both the variants of
the TGT.




Figure 10. Explanations between different groups for the Pima Indians Diabetes Database.

### 7.3 Probing Classiﬁer and Feature Importance




Figure 11. Feature Importance by the binary classifier for the Pima Indians Diabetes Database. a)
(top-left): Feature importance for the classifier between groups 0 and 1. b) (top-right): Feature
importance for the classifier between groups 0 and 2. c) (bottom-left): Feature importance for the
classifier between groups 1 and 2. We note that the classifiers give significant feature importances
to the features which correspond to the deltas (refer fig. 10).

---
**Source PDF:** `dbdb45cacad3.pdf` (2021_01_article.pdf)  
**URL:** https://zenodo.org/record/4835602/files/article.pdf
