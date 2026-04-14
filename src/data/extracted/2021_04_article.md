R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020


Tobias Teule1, ID , Nienke Reints1, ID , Chris Al Gerges1, ID , and Pauline Baanders1, ID
1University of Amsterdam, Amsterdam, Netherlands

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4833547

Reproducibility Summary

Scope of Reproducibility

Deep Fair Clustering (DFC) aims to provide a clustering algorithm that is fair, clustering-
favourable, and which can be used on high-dimensional and large-scale data. In existing
frameworks there is a trade-off between clustering quality and fairness. In this report we
aim to reproduce a selection of the results of DFC; using two of four datasets and all four
metrics that were used in the original paper, namely accuracy, Normalized Mutual In-
formation (NMI), balance and entropy. We use the authorsʼ implementation and check
whether it is consistent with the description in the paper. As extensions to the original
paper we look into the effects of 1) using no pretrained cluster centers, 2) using differ-
ent divergence functions as clustering regularizers and 3) using non-binary/corrupted
sensitive attributes.

Methodology

The open source code of the authors has been used. The datasets and data-preprocessing
has been done with our code, since the authors did not provide the datasets in their code.
Also the pretrained Variational Autoencoder (VAE) dataset had to be re-implemented for
the Color Reverse MNIST . For the extensions we wrote extra functions. For measuring
the influence of discarding the pretrained cluster centers, the code was already provided
by the authors.

Results

For the MNIST-USPS dataset, we report similar accuracy and NMI values that are within
1.2% and 0.5% of the values reported in the original paper. However, the balance and
entropy differed significantly, where our results were within 73.1% and 30.3% of the orig-
inal values respectively. For the Color Reverse MNIST dataset, we report similar values
on accuracy, balance and entropy, which are within 5.3%, 2.6% and 0.2% respectively.
Only the value of the NMI differed significantly, name within 12.9% of the original value
In general, our results still support the main claim of the original paper, even though
on some metrics the results differ significantly.


Code is available at https://github.com/topteulen/UVA-FACT. – SWH swh:1:dir:7058002f161d29f18e52a18ebe326b7911b1b616;.
Open peer review is available at https://openreview.net/forum?id=DXVAJGohUKs.




What was easy

The open source code of the authors was beneficial; it was well structured and ordered
into multiple files. Furthermore, the code to use randomly initialized instead of pre-
trained cluster centers was already provided.

What was difﬁcult

First of all, the main difficulty in reproducing the paper was caused by the coding style;
due to the lack of comments it was difficult to get a good understanding of the code.
Secondly, we were required to download the data ourselves. However, these filenames
and labels did not correspond to the included txt-files by the authors. Therefore, the
model did not learn and we regenerated train_mnist.txt and train_usps.txt.
Finally, the authors only included pretrained models for the MNIST-USPS dataset. As a
consequence, we had to pre-train some parts of the DFC algorithm for the Color Reverse
MNIST dataset.




## 1 Introduction

With the increased application of Machine Learning in automated systems, particularly
in decision making systems, it has become desirable that individuals are treated equally
in such automated environments. However, there exists a trade-off between the fairness
and the performance of machine learning algorithms in a given task [1]. In current fair
clustering algorithms, fair and effective representations are learned by mainly using
small-scale and low-dimensional data. In this paper, we consider representations to be
ʼeffectiveʼ if they yield good performance in clustering tasks. In addition, representa-
tions are considered to be ʼfairʼ when the algorithm is able to achieve great performance
without using attributes like race and gender.
Deep Fair Clustering (DFC) is an algorithm that aims to learn fair and clustering-favorable
representations for large-scale and high-dimensional data. In this context, feature rep-
resentations are considered to be fair if they are statistically independent of sensitive
attributes. Whether a particular attribute is sensitive or not; that is a cultural question
that lies outside the scope of the paper. The aim of the paper is to show that we can pick
an arbitrary attribute of an image, e.g. whether it comes from dataset X or dataset Y ,
and make sure that the feature representation is independent of the specific attribute.
DFC consists of an encoder that produces the representations, and a discriminator that
tries to predict the value of the sensitive attribute of a representation. A minimax game
is used to learn fair representations in an adversarial manner. In order to preserve the
utility of the representations, clustering is performed on all datapoints with the same
sensitive attribute. This component is called ʼstructural preservationʼ because it pre-
serves the clustering structure in each sensitive attribute. Finally, The KL-divergence is
used as a clustering regularizer to prevent the formation of large clusters.
All code is available on Github [2].

## 2 Scope of reproducibility

The goal of this work is to validate the reproducibility of the DFC algorithm proposed
by Li, Zhao, and Liu1 beyond the scope of the original paper. The main claims of the
original paper are as follows:

Claim 1: DFC produces a fair clustering partition on high dimensional and large-
scale visual data.

Claim 2: DFC produces clustering-favorable representations under a fairness con-
straint.

To test the validity of claim 1, the balance and entropy scores will be examined and com-
pared with the original paper. The validity of claim 2 will be tested similarly, where we
instead examine the accuracy and normalized mutual information (NMI) score. Impor-
tant to note is that the original paper mainly evaluated the DFC algorithm on binary
sensitive attributes. As an example, in Li, Zhao, and Liu1 a sensitive attribute was de-
fined as whether an image from the MNIST dataset has been reversed or not. Generally
speaking, in the original paper the sensitive attributes could only take one out of two
possible values. However, sensitive attributes in the real world, like race or gender, can
take on multiple variables.
To evaluate the robustness of claim 1, we will perform the DFC algorithm for non-binary
sensitive attributes. To do this, we modify one of the sensitive attributes chosen by the
authors, particularly whether an image belongs to the MNIST dataset or whether it is
a Color Reverse MNIST image. In the former case, all the pixels of the digit are white
and the background pixels are all black; in the latter case it is the other way around.
To make this attribute non-binary, images from both datasets will be corrupted; some




pixel values will be flipped, and it is not the case anymore that we can distinguish the
images purely on the background color. It would inspire confidence if DFC is still able
to function properly.
Furthermore, we will investigate the robustness of both claims by testing the DFC algo-
rithm on different model configurations. Specifically, we will test out different cluster-
ing regularizers by replacing the KL-divergence with other divergence measures, namely
the Jensen-Shannon divergence (JS-divergence) and the Cauchy-Schwarz divergence (CS-
divergence).
Finally, in the original paper it is mentioned that pretrained cluster centers were used in
the DFC algorithm. However, the motivation of using pretrained cluster centers in DFC
is omitted, which might suggest that pre-training cluster centers are not a necessary
part of the DFC pipeline. Therefore, we will examine the influence of pretrained cluster
centers in DFC.

## 3 Methodology

### 3.1 Model descriptions

Li, Zhao, and Liu1 use a pretrained convolutional variational autoencoder (VAE). The
available code only contained the pretrained encoder and decoder for the MNIST-USPS
dataset [3]. We implemented and pretrained a convolutional VAE for the Color Reverse
MNIST dataset. The encoder is build of four convolutional layers, followed by batch
normalization and a ReLU activation function. Moreover, the decoder is implemented
by reversing the layers of the encoder. Both the encoder and decoder contained 610K
and 58.9K parameters respectively. The VAE is trained using the Adam-optimizer and a
learning rate of 1e − 3.
Li, Zhao, and Liu1 also used pretrained cluster centers to start their DFC algorithm
off with high accuracy clusters. They only provided pretrained cluster centers for the
MNIST-USPS dataset: Therefore, in order to reproduce the results, we were required to
obtain pretrained cluster centers for the Color Reverse MNIST dataset. For this task we
used k-means clustering1 with k = 10. Because the original code of the authors used 64-
dimensional cluster centers, we first scaled our 32×32 images down with a max pooling
layer with 4 sized filters, so that the images would go from 32 × 32 to 8 × 8. After dimen-
sion reduction every image becomes a 1 × 64 vector. We then fit every image in the
dataset using MiniBatchKMeans from the sklearn package2. With max_iter = 1000
and batch_size = 512. This results in our pretrained cluster centers which can be
trained for every dataset.
To examine during clustering whether fair representations are reached, a discriminator
is used; when it cannot distinguish based on the sensitive attribute the representations
are fair. This discriminator is a multilayer perceptron (MLP) using three linear layers,
of which the first two are followed by a ReLU activation function and a dropout of 0.5:
the final layer is followed by a sigmoid activation function. The discriminator is trained
jointly with the encoder for 20000 epochs. Finally, the Adam optimizer is used with an
initial learning rate of lrinit = 1e − 4. The learning rate is adjusted with lr = lrinit(1 +
10t)−0.75, with t = 0 at the start of the training process; with every iteration t is linearly
increased to t = 1 at the end of the training process.
The objective function consists of three parts; the fairness-adversarial loss (Lf ), the
structural preservation loss (Ls) and the clustering regularizer term (Lc). The task of the
fairness-adversarial loss is to minimize the divergence between the cluster assignments
of the different subgroups. In this way the term promotes a similar cluster distribution
for all subgroups, hence, statistical independence between cluster assignments and the

1https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
2https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html




particular protected subgroup that the sample belongs to. The fairness-adversarial loss
can be written as:

Lf := L(D ◦ A ◦ F(X), G),
(1)
where L denotes the cross-entropy loss and ◦ denotes the function composition: more-
over, D, A, F denotes the discriminator, cluster assignment and encoder respectively.
The fairness-adversarial loss encourages statistical independence of the cluster assign-
ments and the sensitive attribute G, however, only optimizing Lf is not enough as it
can lead to a degenerate solution, where the representations that are produced by the
encoder are all constant. Of course, such a constant representation cannot lead to good
clustering quality; it would hide, rather than illuminate, the fundamental structure in
the data. The structural preservation loss prevents such a solution by penalizing it when
the inner structure of a particular subgroup is altered in the DFC setting, as opposed to
clustering the subgroup individually. The preservation loss, which was proposed by the
authors [1] is given as follows:

Ls :=

X


(cid:12) ˆPg ˆP T
g

g∈[M ]


,

− PgP T
g

(2)

where [M ] denotes the set of sensitive attributes, ˆPg and Pg denote the (soft) assignments
of the g−th protected subgroup when individually clustered and clustered with DFC,
respectively.
Following other work in deep clustering, DFC employs a clustering regularizer to strengthen
prediction confidence and to prevent large cluster sizes [1]. Contrary to earlier work, the
clustering regularizer is chosen in such away that it encourages the members of a par-
ticular protected subgroup to be distributed equally over the clusters. To increase the
confidence of the prediction an auxiliary target distribution Q is defined. This target
distribution is defined in such a way that it favors current high confidence assignments
and is calculated as:

P

qk =

P

(pk)2/
k′∈[K]((pk′)2/

x∈Xg
P

pk

x∈Xg

,

pk′

(3)

with pk the probability that sample x belongs to cluster k, and Xg the samples that be-
long to protected subgroup G. Then, the clustering regularizer loss is defined as the
KL-divergence between soft assignment P and auxiliary target distribution Q:

Lc := KL(P ||Q) =

X

X

X

g∈[M ]

x∈Xg

k∈[K]

pk log

pk
qk

.

(4)

Again following the literature, the authors have chosen to use the Student t-distribution
for soft cluster assignment [1]. The probability that the representation z (corresponding
to a particular sample x) belongs to cluster ck is then given by:

pk =

P

(1 + 1
α
k′∈[K](1 + 1
α

||z − ck||2)− α+1


||z − ck′||2)− α+1


,

(5)

with α the degree of freedom of the Studentʼs t-distribution. In conclusion, the overall
objective is defined as the following minimax strategy:

max
F ,A

min
D

αf Lf − αsLs − Lc,

αf Lf

with αf and αs as trade-off hyperparameters.


(6)

(7)




### 3.2 Datasets

In this study, we have used two publicly available datasets: Color Reverse MNIST and
MNIST-USPS datasets. Both datasets contain a collection of grey-scale images of hand-
written digits (0-9).
The first dataset, MNIST-USPS , is a combination of the MNIST3 and USPS4 dataset. Both,
MNIST and USPS are downloaded using the torch.vision.dataset package. The
label distributions and total number of examples in the training and test set can be found
in Table 1. The MNIST dataset contains approximately eight times more images than
USPS . In the MNIST-USPS dataset, the source, either MNIST or USPS , is chosen to be
the sensitive attribute.
The second dataset, Color Reverse MNIST , was constructed by reversing the images in the
MNIST dataset and concatenating them to the original. The color reversed images were
constructed with pixel = 255 - pixel. The label distributions and total number of examples
in the training and test set can also be found in Table 1. Equivalent to the MNIST-USPS
dataset, the sensitive attribute is the source of the image; in this case either MNIST or
Color Reverse MNIST .
The images in all datasets are padded to create images of the same size (32 × 32); this
implies a padding of 2 and 8 for the images of MNIST and USPS respectively.


MNIST train
USPS train


5923
1194


6742
1005


5958


6131


5842


5421


5918


6265


5851


5949


Total

60000
7291

Color Reverse MNIST train 11846
7117
MNIST-USPS train

13484
7747

11916
6689

12262
6789

11684
6494

10842
5977

11836
6582

12530
6910

11702
6393

11898
6593

120000
67291

Table 1. Label distribution per dataset

### 3.3 Extensions

Divergence Functions — As mentioned earlier in Section 2, we examined the effect of using
different divergence functions as clustering regularizers by replacing the KL-divergence
with either the Jensen-Shannon divergence (JS-divergence) or the Cauchy-Schwarz diver-
gence (CS-divergence).
The JS-divergence is the smoothed and symmetric version of the KL-divergence and is
calculated as follows:

JS(P ||Q) =


KL(P ||M ) +


KL(Q||M )

(8)

2 (P + Q) and KL(.||.) is the KL-divergence as defined in 4.

where M = 1
Furthermore, the CS-divergence is a divergence function that is inspired by information
theory. It is given by the following ([4]):

CS(P ||Q) = − log

qR

R

p(x)q(x)dx
R

p2(x)dx

q2(x)dx

(9)

The CS-divergence is, like the JS-divergence, a symmetric measure. Furthermore, the
CS-divergence has the range 0 ≤ CS(P ||Q) ≤ ∞, where the minimum value of 0 is
obtained if p(x) = q(x).

3http://yann.lecun.com/exdb/mnist/
4http://www.kaggle.com/bistaumanga/usps-dataset




Corrupted Sensitive Attribute — Another extension mentioned in Section 2 is that we con-
sider the influence of the corrupted sensitive attribute. In the Color Reverse MNIST dataset
the presence of this attribute is clear in background color, The numbers are black in the
case of MNIST-USPS and white in the case of Color Reverse MNIST , The background is
defined by everything that is not the colour of the number. Corrupting the sensitive
attribute in this dataset implies random modifications in the background color. We
compare two corruption rates (0.1 and 0.4) against the original images; for example, a
rate of 0.1 implies that a random 10% of the background pixels are changed from black
to white or vice versa.

Pretrained Cluster Centers — The final extension mentioned in Section 2 is that we would
examine the influence of pretrained cluster centers on the performance of DFC. If no
pretrained cluster centers were used, they would be randomly initialized with Xavier
initialisation using a uniform distribution.

### 3.4 Evaluation

To evaluate the models, we used the four metrics that were also used by Li, Zhao, and
Liu1: accuracy and Normalized Mutual Information (NMI) were used to evaluate the
cluster validity, while balance and entropy were calculated to evaluate the fairness of
DFC. Equations 10-13 are used to calculate the metrics: the NMI is calculated using
sklearn.

Accuracy =

P
n
i=1

Iyi=map(ˆyi)

n
P

N M I =

q
(

P

Balance = min

Entropy = −

i,j nij log n·nij
ni+·n+j
P
j n+j log n+j
i ni+ log ni+
n )
n )(
ming |Ci ∩ Xg|
ni+
|Ci ∩ Xg|
ni+

|Ci ∩ Xg|
ni+

+ ϵ

log

i
X

i

(10)

(11)

(12)

(13)

In Eq. 10, yi and ˆyi represent the correct and predicted cluster label respectively: map is
a function that maps the cluster label ˆyi to the correct label yi. In Eq. 11, nij denotes the
co-occurrence number; ni+ and n+j denote the cluster size of the i-th and j-th clusters,
in the obtained partition and ground truth, respectively. n is the total data instance
number. Furthermore, Ci represents the i-th cluster and Xg the g-th protected subgroup.
Finally, in Eq. 13, ϵ = 1e − 5, to ensure the log will always be defined.
As mentioned before, accuracy and NMI are measures for the clustering quality. More
specific, accuracy measures the correctness of clusters relative to a ground truth and
NMI measures the similarity between the clustering obtained by DFC and the ground
truth. For both metrics, a higher value indicates better clustering quality. Furthermore,
balance and entropy evaluate the fairness of the obtained clustering. In particular, bal-
ance measures the homogeneity of the clustering across multiple sensitive attributes.
A large value indicates that each cluster contains samples from multiple protected sub-
groups. If one cluster contains only instances of a particular protected subgroup, the
balance has a score of 0. Entropy is a softer fairness metric than balance that measures
the diversity of the clustering. Just like balance, a large entropy value indicates that
samples from a protected subgroup are present in almost every cluster, which indicates
a more fair clustering and thus more fair representations.




### 3.5 Computational requirements

The code was run locally on a GPU. The GPU in question is a GeForce GTX 970 with driver
version 456.71. The CPU in this machine is an Intel Core i7-4770K. The memory used was
16.0 GB DDR3. For the main training of the adversarial network with 20000 iterations
at 5000 iterations per evaluation the model ran in approximately 3.5 hours. This was
the same computational cost to run DFC with a different divergence function. For the
corruption extension we used 5000 iterations at 500 iterations per evaluation which took
about 1.5 hours. The training of the VAE for the Color Reverse MNIST dataset took roughly
1 hour. The k-means clustering to obtain the pretrained clusters took approximately
15 minutes. Taking all this into account, the reproduction of the 
results from scratch took a total of circa 6.25 hours to compute. Finally, evaluating all
the results with the saved models takes about 20 minutes. In conclusion, the code is
not fast but it can be run on a local machine. A GPU is heavily recommended, because
without one the code is about eight times slower.

## 4 Results

### 4.1 Reproduced Results

The original results from Li, Zhao, and Liu1 as well as the reproduced results can be
found in Table 2.


Method

Accuracy NMI


MNIST-USPS

Li, Zhao, and Liu1

Reproduced

Li, Zhao, and Liu1

Reproduced

0.577

0.548

0.825

0.835

0.679

0.763

2.294/2.301

0.591

0.783

2.301/2.299

0.789

0.067

2.301/2.265

0.785

0.018

2.301/1.579

Table 2. Reproduced and original quantitative results, for all metrics, on Color Reverse MNIST and
MNIST-USPS dataset.

First of all, the reproduced accuracies on both datasets are very similar to the origi-
nal values of Li, Zhao, and Liu1; differing 0.029 and 0.01 on Color Reverse MNIST and
MNIST-USPS respectively. Secondly, similar to accuracy, the original and reproduced
NMI values do not differ much; 0.88 on Color Reverse MNIST and 0.004 on MNIST-USPS .
Thirdly, the reproduced balance on Color Reverse MNIST is close to the original; differing
0.02: however, the difference is larger on the MNIST-USPS dataset (0.049). Finally, the
entropy values on Color Reverse MNIST are very similar in contrast to the original and
reproduced entropy on MNIST-USPS .

### 4.2 Results beyond original paper

Divergence Functions — Table 3 shows the results for different divergence functions as clus-
tering regularizers.





Divergence Function Accuracy NMI


MNIST-USPS

KL-divergence

JS-divergence

CS-divergence

KL-divergence

JS-divergence

CS-divergence

0.548

0.517

0.592

0.835

0.816

0.815

0.591

0.783

2.301/2.299

0.397

0.701

2.301/2.289

0.408

0.025

2.301/2.084

0.785

0.018

2.301/1.579

0.753

0.000

2.301/1.056

0.755

0.000

2.301/0.737

Table 3. Quantitative results for the Color Reverse MNIST and MNIST-USPS dataset, for all four met-
rics, with varying divergence measures.

In Table 3 it can be observed that the accuracy does not differ significantly on the Color
Reverse MNIST dataset. Furthermore, using the CS-divergence seems to yield the highest
accuracy. However, the NMI decreases significantly with JS- and CS-divergence as clus-
tering regularizer. On top of that, the balance and entropy decrease significantly with
CS-divergence. Using the JS-divergence also results in a decrease in balance and entropy
on the Color Reverse MNIST dataset, even though that decrease is minor compared to the
CS-divergence. In general, the KL-divergence outperforms the other two divergences
on three of the four metrics on the Color Reverse MNIST dataset. On the MNIST-USPS
dataset, it can be seen that the difference in accuracy and NMI is even less significant
compared to the Color Reverse MNIST dataset. However, on the MNIST-USPS dataset all
four metrics decrease when using the JS- or CS-divergence instead of the KL-divergence.
Moreover, the balance and entropy seem to decrease more significantly than the accu-
racy and NMI. In general, on the MNIST-USPS dataset the JS- and CS-divergence perform
worse than the KL-divergence.

Corrupted Sensitive Attribute — The results of the corruption extension can be found in Ta-
ble 4.


MNIST


Both

Corruption (in %) Accuracy NMI


0.1

0.4

0.1

0.4

0.1

0.4

0.451

0.342

0.635

0.474

0.446

0.313

0.487

0.639

2.301/2.288

0.314

0.001

0.837/2.258

0.606

0.645

2.301/2.289

0.483

0.002

2.164/2.198

0.531

0.659

2.299/2.285

0.213

0.000

1.615/1.583

Table 4. Quantitative results, on all four metrics, with varying corruption rates.

As can be seen in Table 4, both the accuracy and the NMI decrease when data has been
corrupted. However, the decrease in accuracy and NMI seem to be more significant
when the Color Reverse MNIST dataset is corrupted. Moreover, the balance and entropy
decrease when the data is corrupted. In general, a higher corruption leads to lower
values on all metrics. Finally, Table 4 shows that the balance drops significantly with a
higher corruption rate.

Pretrained Cluster Centers — The final extension researches the influence of the pretrained
cluster centers on the utility and fairness of the clusters. The results for both datasets




can be found in Table 5.


Pretrained Accuracy NMI


MNIST-USPS

Yes

No

Yes

No

0.548

0.468

0.835

0.822

0.591

0.783

2.301/2.299

0.494

0.872

2.301/2.302

0.785

0.018

2.301/1.579

0.770

0.000

2.301/1.568

Table 5. Quantitative results for all metrics, on Color Reverse MNIST and MNIST-USPS datasets, with
and without using pretrained cluster centers.

Most significantly, in Table 5, it is visible that the accuracy on the MNIST-USPS dataset is
significantly higher than that on Color Reverse MNIST , both with and without pretrained
cluster centers. Furthermore, for both datasets accuracy and NMI are higher when pre-
trained cluster centers are used. The difference in accuracy is larger on the MNIST-USPS
dataset, whereas the difference in NMI is smaller on this dataset, compared to Color
Reverse MNIST . Moreover, the difference in balance on MNIST-USPS is not significant
(0.018) while this difference is approximately five times larger (0.089) on the Color Reverse
MNIST dataset. Finally, the entropy does not change significantly on both datasets.

## 5 Discussion

Our experimental results support the main claims of the original paper; namely that
DFC is able to produce fair and clustering-favorable representations of large-scale and
high dimensional data, such as images. Furthermore, our extensions seem to add to
the robustness of the model and strengthen the choices made by the original paper.
First of all, the results of the different divergence functions show that both, CS- and
JS-divergence, work but the default, KL-divergence, outperforms the two researched al-
ternatives. Moreover, even though the Color Reverse MNIST dataset required the training
of a new VAE and k-means clustering the results were still comparable; this speaks to
the robustness of the algorithm that the original authors designed.

### 5.1 What was easy

The open source code of the authors was conveniently arranged. For example, the di-
vergence function was put in the utils file, which made it easy to test other divergence
functions as well. Also, the code had an implementation that randomly initialises clus-
ter centers; to discard the pretrained cluster centers only modifications in the main file
were needed. Once we understood the code base, the code structure became intuitive
and easy to work with.

### 5.2 What was difﬁcult

First of all, a difficulty while reproducing the research was caused by the coding style;
due to the lack of comments it was difficult at the start to get a good understanding of the
code. Secondly, we were required to download the data ourselves. However, these file-
names and labels did not correspond to the included .txt-files by the authors. Therefore,
the model did not learn and we were forced to produce our own train_mnist.txt
and train_usps.txt. Thirdly, the algorithm uses pretrained models, a pretrained
VAE, and a file with pretrained cluster centers. However, the authors solely provided
these for one of the four datasets, namely MNIST-USPS . Thus, for 
we had to build our own VAE based on their structure and calculate our own cluster




centers. The latter came with an extra difficulty since in the paper it is not stated how
the clustering was performed. Therefore, we had to guess and chose k-means cluster-
ing. This made the reproduction of the Color Reverse MNIST dataset much harder than
anticipated.

References

1.

2.

3.

4.

P. Li, H. Zhao, and H. Liu. “Deep Fair Clustering for Visual Learning.” In: The IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR). June 2020.
C. Al Gerges, P. Baanders, N. Reints, and T. Teule. Reproducing Deep Fair Clustering. URL: https://github.com/
topteulen/UVA-FACT.
P. Li, H. Zhao, and H. Liu. Deep Fair Clustering. URL: https : / / github . com / brandeis - machine - learning /
DeepFairClustering.
R. Jenssen, J. C. Principe, D. Erdogmus, and T. Eltoft. “The Cauchy-Schwarz divergence and Parzen window-
ing: Connections to graph theory and Mercer kernels.” In: Journal of the Franklin Institute 343.6 (Sept. 2006),
pp. 614–629.

---
**Source PDF:** `3f09a1480db0.pdf` (2021_04_article.pdf)  
**URL:** https://zenodo.org/record/4833547/files/article.pdf
