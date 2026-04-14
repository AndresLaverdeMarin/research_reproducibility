R E S C I E N C E C

Replication / Computer Vision


Jarl Lemmens1, ID , Pavol Jancura1, Gijs Dubbelman1, Hala Elrofai1
1Eindhoven University of Technology, Eindhoven, Netherlands

Edited by
Benoît Girard ID

Reviewed by
Hirak Kashyap ID
Stéphane Herbin ID

Received
08 October 2021

Published
31 March 2023

DOI
10.5281/zenodo.7788556

A replication of Y. Fang, K. Kuan, J. Lin, C. Tan, and V. Chandrasekhar. “Object detection meets knowledge graphs.”
In: Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI-17. International
Joint Conferences on Artificial Intelligence, 2017, pp. 1661–1667.

Summary of reproducibility

Scope of reproducibility

‘Object Detection meets Knowledge Graphs’ [1] by Fang et al. describes a framework
which integrates external knowledge from knowledge graphs, or background knowledge, into object detection. They apply two different approaches to quantify background
knowledge as semantic consistency. An existing object detection algorithm is re‐optimized
with this knowledge to get updated knowledge‐aware detections. The authors of [1]
claim that this framework can be applied to any existing object detection algorithm
and that this approach can increase recall, while maintaining mean Average Precision
(mAP). In this work, the framework is implemented and the experiments are conducted
as described in [1], such that the claims can be validated.

Methodology

The authors in [1] describe a framework where a frequency based approach and a knowledge graph based approach are used to determine semantic consistency. A knowledgeaware re‐optimization function updates the detections of a baseline Machine Learning
object detection algorithm. Both the baseline and its re‐optimized correlates are evaluated on two publicly available benchmark datasets, namely PASCAL VOC 2007 and MS
COCO 2014. The replication of the experiments was completed using the information
in [1] and clarifications of the author, as no source code was available. The framework
was implemented in PyTorch and evaluated on the same benchmark datasets.

Results

We were able to successfully implement the framework from scratch as decribed in [1].
We have bench‐marked the developed framework on two datasets and replicated the
results of all matrices as described in [1]. The claim of the authors of [1] can not be
confirmed for both described approaches. The results either showed an increase of
recall at the cost of a decrease in mAP, or a maintained mAP, without an improvement
in recall. Three different backbone models show similar behavior after re‐optimization,


The authors have declared that no competing interests exists.
Code is available at https://github.com/tue-mps/rescience-ijcai2017-230.
Data is available at https://zenodo.org/record/7385730.Y73csnbMJPY – DOI 10.5281/zenodo.7385730.
Open peer review is available at https://github.com/ReScience/submissions/issues/59.




concluding that the knowledge‐aware re‐optimization does not benefit object detection
algorithms.

What was easy

The methodology was well described and easy to understand conceptually.

What was difficult

There was no source code available, which made it difficult to understand some technicalities of the implementation. The authors failed to mention a number of crucial
details and assumptions of this implementation in the paper, which are essential for
reproducing the methodology without making fundamental assumptions.

Communication with the authors

We contacted the authors to elaborate on missing details, however no contact was found
with the contact‐information on the paper. Fortunately, a different email address of
Yuan Fang was found online, to which he did respond fast and with clear explanations,
for which we would like to express our gratitude.

## 1 Introduction

Object detection is one of the key tasks in computer vision. The PASCAL Visual Object
Classes (VOC) challenge is one of the most accepted benchmarks for object detection.
This challenge reads: ”Where are the instances of a particular object class in the image
(if any)?” [2]. In other words, the goal is to find a set of locations, or bounding boxes,
in an image and to classify each instance with a label from a predefined set of classes
[3]. Most state‐of‐the‐art methods for object detection, such as Faster R‐CNN [4], only
use the visual features that are present in the images, while ignoring the vast amount of
background information that is available.

Figure 1. Toy example of an object detection.




Background information can be beneficial for classifying the detected objects [5]. For a
human classifier, who has this background information at its disposal, it can be common
sense that certain classes happen to co‐occur more often than others. Figure 1 shows a
scenario where a student is holding a drink. A human will classify the drink as a beer
more likely than a water (assuming these are the only options), even though the liquid
can not be identified directly. For machines, this ‘common sense’ is not self‐evident. As
a result, the machine is uncertain about the class of the drink and might even (wrongly)
classify it as a water. One way to represent this background knowledge in a machinereadable way, is a knowledge graph. A knowledge graph nowadays has many different
definitions [6]. In this paper it is defined as the original semantic network. This network
is a knowledge base that represents semantic relations between concepts in a network
such that the nodes represent the concepts and the edges represent the relationships
between the nodes [7]. Figure 2 shows a toy example of such a knowledge graph, which
would help identify the drink in Figure 1 as a beer rather than a water. It is expected
that employing a large‐scale knowledge graph as external background knowledge will
improve the classification capabilities of the object detectors.

Figure 2. A toy knowledge graph modeling seven concepts as nodes (e.g., student and beer), as well
as their relationships as edges (e.g., ”student drinks beer”).

In this work we aim to replicate the findings of a knowledge‐aware object detection
framework, as described in ‘Object Detection meets Knowledge Graphs’ [1]. The proposed framework combines ‘traditional’ deep learning methods with the semantic consistency of a knowledge graph. The goal is to quantify and generalize the knowledge
from the ConceptNet knowledge graph [8], and apply this semantic consistency to the
object detection output of a Faster R‐CNN [4] network to get an updated object prediction. Additionally, a frequency based method to determine semantic consistency directly from the datasets is applied. A custom re‐optimization function is used to update
the detections from a baseline object detection algorithm. The system is evaluated on
the PASCAL VOC 2007 [2] and MS COCO 2014 [3] benchmark datasets.

## 2 Scope of reproducibility

The authors of [1] claim that any existing knowledge detection algorithm can be reoptimized by their proposed knowledge‐aware detections. They propose two methods
to extract semantic consistency between different classes from background information
that are used to define the knowledge‐aware detections. The first method is a frequencybased approach that uses information directly from the datasets and the second method
is based on the information from a knowledge graph.
We aim to reproduce the claims that integrating background knowledge to conventional
deep learning object detection algorithms will improve the recall while maintaining the
same level of mean Average Precision (mAP).




## 3 Methodology

### 3.1 Model descriptions

The authors of [1] used a Caffe implementation of the Faster R‐CNN network with a VGG16 backbone pretrained on ImageNet.1 Our work utilizes the readily available PyTorch
implementation of the Faster R‐CNN network with a pretrained ResNet50 backbone.2
The model was trained separately on each dataset for evaluation on the specific dataset.
Additionally, a VGG‐16 backbone as well as a ResNet18 backbone were implemented and
trained for supplementary experiments.

### 3.2 Datasets

VOC — The method is tested on two widely accepted benchmark datasets for object detection. The first is the PASCAL VOC 2007 dataset [2]. The VOC dataset consists of 10k
images that are divided into 2.5k training set, 2.5k validation set and 5k test set.3 The
data is annotated for 20 different classes. The test set contains a number of objects that
are annotated as ’difficult to detect’. For the challenge evaluation such objects are discarded, although no penalty is incurred for detecting them [2].

COCO — The second benchmark is the Microsoft COCO dataset [3]. COCO is an annual
challenge that at times updates the dataset. For this approach, the 2014 dataset is used.
This dataset consists of 165k images split into 83k for training, 41k for validation and
41k for testing.4 For this (and the author’s) approach, the training and validation set are
combined for training, except for a subset of 5k images, that is divided again into 1k
for validation and 4k for offline testing. The ground truth of the test set is not publicly
available, thus evaluation is limited to the offline test set. COCO consists of 91 different classes, however 11 classes were later removed from annotation, which leaves 80
effective classes. This results in some images in the set being ’empty’. These images are
ignored during training/inference. To align with the indexing of annotation, the model
maintains the 91 classes, but the 11 redundant classes are ignored during evaluation.
The 20 classes in the VOC dataset are a subset of the COCO classes.

### 3.3 Metrics

The main performance metrics that are used are recall@100 and mean Average Precision
(mAP)@100. As stated in the COCO evaluation description, “all metrics are computed
allowing for at most 100 top‐scoring detections per image (across all categories)”.5 Both
recall and AP are calculated per class and averaged at the end. The recall is determined
per class according to

recall =

T P
T P + F N

,

(1)

where T P is the number of true positives, and F N is the number of false negatives. To
simplify the implementation, the number of FN is not directly determined, but the sum
of TP and FN is equal to the number of ground truth objects.
The AP is a precision‐recall curve metric that calculates the weighted mean of precisions
achieved at each recall threshold.6 The cumulative number of true‐positives (TP) and

1https://github.com/rbgirshick/py‐faster‐rcnn
2https://pytorch.org/vision/stable/models.html
3http://host.robots.ox.ac.uk/pascal/VOC/voc2007/index.html
4https://cocodataset.org/download
5https://cocodataset.org/detection‐eval
6https://blog.roboflow.com/mean‐average‐precision/




false‐positives (FP) are determined for the whole test set per class, in descending order
of the confidence score. Subsequently, the recall is segmented into 101 equal parts, and
for each segment the interpolated precision is determined, which is the maximum precision value for a given recall. A detection is considered to be a TP when the Intersection
over Union (IoU) with the ground truth (of the correct class) is at least 0.5 for the VOC
dataset. For the COCO dataset the mAP is calculated for different IoU thresholds {0.50,
0.55, . . . , 0.95} and then averaged. Besides recall@100, the recall@10 is determined
for the COCO dataset, as well as the recall@100 specifically for small, medium and large
objects.

### 3.4 Notation

Consider a set of pre‐defined labels L = {1, 2, ..., L}. Let an existing object detection algorithm output a set of bounding boxes B = {1, 2, ..., B} for each image. Each bounding
box b ∈ B is assigned a label ℓ ∈ L with probability p(ℓ|b). Per image, these probabilities
can be encoded by a matrix P of size B × L. The goal is to construct a knowledge‐aware
matrix ˆP based on the semantic consistency knowledge. A bounding box is potentially
assigned a new label ˆℓ = argmaxℓ( ˆPb,ℓ).

### 3.5 Semantic consistency

To quantify background knowledge that is fundamentally symbolical and logical, it is
proposed to determine a numerical degree of semantic consistency for each pair of concepts. The more likely that two concepts appear in the same image, the higher the degree of semantic consistency.
The matrix S, of size L × L, is defined such that Sℓ,ℓ′ captures the degree of semantic
consistency between the two concepts ℓ and ℓ′, ∀(ℓ, ℓ′) ∈ L2. The matrix is symmetrical,
and the diagonal contains the self‐consistency of a concept (a concept can occur more
than once in the same image).
Two methods to determine semantic consistency are applied, in the same manner as
the original paper.

Frequency based method — The simple way to compute S is to use the frequency of cooccurrences for each pair of concepts. In this work, both the VOC and COCO datasets
are used to identify the co‐occurences. The semantic consistency is calculated, based
on point‐wise mutual information [9] using the following equation.

(cid:18)

Sℓ,ℓ′ = max

log

n (ℓ, ℓ′) N
n(ℓ)n (ℓ′)

(cid:19)

, 0

(2)

Here n(ℓ, ℓ′) denotes the frequency of co‐occurrences for concepts ℓ and ℓ′, n(ℓ) denotes
the frequency of ℓ and N is the total number of instances in the background data.
To determine the frequency of co‐occurrences, the number of unique combinations of
objects are counted for each image in both datasets. Then the results are summed for all
images, before applying equation 2. The co‐occurrences are given by the multiplication
of n(ℓ) and n(ℓ′). For self‐occurrences the ‘handshake’ equation

n(ℓ, ℓ) = n(ℓ) × n(ℓ) − 1


(3)

is used. Figure 3 and Table 1 show a sample image to provide an example on how the
(co‐)occurrences are counted.




Table 1. Frequency of (co)‐occurrences
as counted from Figure 3

n(person)
n(bike)
n(person, bike)
n(bike, person)
n(person, person)
n(bike, bike)
N


Figure 3. Annotated VOC image

Knowledge Graph based — A more generalizing method to determine semantic consistency
is to use a large‐scale knowledge graph. A knowledge graph can also capture one or multiple chains of relations between concepts that are not directly connected to each other,
which will increase robustness. To quantify these relations as semantic consistency,
the ‘random walk with restart’ (RWR) approach is utilized [10]. From a starting node/‐
concept, the algorithm ‘walks’ through the graph via neighbouring nodes. After every
step there is a chance to teleport back to the starting node, to prevent from getting stuck
in small localities. The probabilities of reaching certain nodes, eventually converge to
a steady state. Equation 4 shows the iterative implementation of this approach.

⃗r ← (1 − c)fW ⃗r + c⃗e

(4)
fW is a normalHere ⃗r is the relatedness vector with respect to the starting node/seed ⃗e.
ized weighted matrix that represents the weighted knowledge graph and c is the restart
probability constant.
For this approach, a readily available implementation of the RWR algorithm is utilized.
[11] As knowledge graph, the MIT ConceptNet version 5.7 is employed.7 A list of assertions (two concepts and a relation between them) is filtered to only include the English
segment. Also all negative relations (NotDesires, NotHasProperty, NotCapableOf, NotUsedFor, Antonym, DistinctFrom and ObstructedBy) and self‐loops (when the relation
directly connects a concept to the same concept) are ignored. The resulting graph has
1.16 million unique concepts and 3.35 million relations. To conform to the requirements
of the RWR implementation, the graph is converted from concept strings to integers,
using Pandas Dataframe structure. Note that the ConceptNet relations are directed,
and when a bi‐directional relation exists, these are added separately in the assertions
list. Each relation comes with a weight corresponding to the significance of the relation, which is included in the RWR. The relatedness vector is computed for all 20 and 91
classes of the VOC and COCO dataset respectively. The matrix values of the 11 redundant
COCO classes are set to 0.

3.6 Re-optimization

The re‐optimization function is a result of optimizing the cost function given in equation
5.

7https://github.com/commonsense/conceptnet5/wiki/Downloads




E( bP ) =(1 − ϵ)

BX

BX

LX

LX

b=1

b′=1
b′ ̸=b

ℓ=1

ℓ′=1

(cid:16)

Sℓ,ℓ′

bPb,ℓ − bPb′,ℓ′

(cid:17)2

+ ϵ

BX

LX

b=1

ℓ=1

B ∥Sℓ,∗∥


(cid:16)

bPb,ℓ − Pb,ℓ

(cid:17)2

(5)

Here, the first term captures the constraint on semantic consistency that for two different bounding boxes b and b′ in the same image, Pb,ℓ and Pb′,ℓ′ should not be too different for a large value of Sℓ,ℓ′. The second term captures the constraint such that the
knowledge‐aware detections do not diverge too much from the original detections. The
B ∥Sℓ,∗∥
1 coefficient balances both terms, because of the different number of summations. Optimizing this cost function 5 results in the re‐optimization function given in
equation 6 [1].

bP (i)
b,ℓ = (1 − ϵ)

P

B
b′=1,b′̸=b
P

P

b′=1,b′̸=b

ℓ′=1 Sℓ,ℓ′ bP (i−1)
L
P
L
ℓ′=1 Sℓ,ℓ′

b′,ℓ′

+ ϵPb,ℓ

(6)

bP (0)
b,ℓ ,

bP (i)
For any arbitrary initialization
b,ℓ converges to the same solution eventually (usually within 30 iterations). To speed up the computation, an approximation is applied
where the Bk nearest bounding boxes and Lk nearest concepts are considered. This
means that for a bounding box b, the nearest Bk boxes to b (shortest distance center‐tocenter), b′ are considered. For a concept ℓ, only the top Lk concepts ℓ′ with the largest
semantic consistency to ℓ are considered. To increase the efficiency for computing equation 6, matrix multiplication is used. Using the Lk approximation, a sparse consistency
matrix can be constructed.

### 3.7 Hyper-parameters

All hyper‐parameters are kept identical as described in the original paper. The models
(for VOC and for COCO), are trained using Stochastic Gradient Decent with a momentum
of 0.9, a weight‐decay of 5e‐4 and a batch‐size of 2. A learning rate of 1e‐3 is used for the
first 50k/350k iterations, followed by 1e‐4 for another 10k/140k iterations on VOC/COCO
respectively.
The default parameters of the Faster R‐CNN model are kept, except the (maximum) number of detections per image is set to 500, and the score threshold of the bounding boxes
is decreased to 1e‐5. The random walk restarting probability C is set to 0.15. The hyperparameter ϵ in equation 6 is chosen between {0.1, 0.25, 0.5, 0.75, 0.9} on the validation
sets. After contact with the author, ϵ was set to 0.9 for the VOC dataset and 0.75 for the
COCO dataset. The updates of equation 6 are performed for 10 iterations, and Bk and
Lk are both set to 5.

### 3.8 Experimental setup & code

Figure 4 shows a flowchart of the implementation during inference. A test image is fed
to the Faster R‐CNN network, where the ResNet‐50 backbone produces a set of region
proposal bounding boxes (1000 boxes by default, the objectness score threshold is 0.0)
that are classified such that each class gets a probability score Pb,ℓ. The bounding box
proposals are updated by a regression layer such that each class gets a separate bounding box with the corresponding class score. During post‐processing the bounding boxes
are filtered on a score‐threshold (1e‐5 in this approach). Double detections are filtered
out by applying a class‐wise Non‐Maxima‐Suppression (NMS). Next, a maximum of 500
top scoring boxes are kept. It is important to note that at this point for each bounding
box only the highest score probability remains. For the baseline approach, the top 100




Figure 4. Flowchart of the knowledge aware re‐optimization during inference.

highest scores are selected and used for evaluation. For the knowledge aware approach,
the probabilities of all classes other than the highest scoring class of that bounding box
are set to 0 initially. Then the re‐optimization function 6 is applied. This was not mentioned in the published paper, however it is crucial for implementation. For each detection, the maximum of ˆPb,ℓ will be the (updated) score for that bounding box, and there
is a chance that the label will be updated as well. Again the top 100 highest scores are
considered for evaluation.
Three different variants of the semantic consistency matrix are constructed and evaluated. First, the frequency based method is applied on both datasets. To conform to
the published results, we keep the same naming, so this approach is called KF‐All. A
second approach uses only 250 images of each dataset to show the relevance of background quality. We call this approach KF‐500. The third approach utilizes the ConceptNet knowledge graph and is called KG‐CNet57, which refers to as the version 5.7 of the
graph. Additionally we check the difference between this version and an older graph
(version 5.5), which we call KG‐CNet55. The baseline Faster R‐CNN results are called
FRCNN. As no source code was available from [1], the methodology was implemented
from scratch based on the descriptions in the paper and contact with the author.

## 4 Results

4.1 VOC

The obtained results support the claims presented in [1], only in one specific case. Table
2 shows the originally published results as well as our results on the VOC dataset for the
different backbone models, namely ResNet‐50, ResNet‐18 and VGG‐16. The first observation is that for the ResNet‐50 frequency based approaches, the mAP is maintained at
70.1, which is in line with the claims of [1], as discussed shortly. However, the recall is
only increased by 0.1 for the KF‐All, which is not comparable to the published benefits in
[1]. For the knowledge graph based approaches, both mAP and recall are decreased with
0.3 using the re‐optimization process. The ResNet‐18 results show a maintenance or decrease for both mAP and recall similar to the results of ResNet‐50 for both the frequency
based and the knowledge graph based approaches. This shows that there is hardly any
difference in the effect of re‐optimization between a relatively ’worse’ or ’better’ backbone. The VGG‐16 results again show similar behavior of decrease in mAP, while in the
best case maintaining recall. The difference between published results and our VGG‐16
baseline results can be attributed to the re‐implementation of the original Caffe model
to the PyTorch environment. This is done to the best of our knowledge, but there might
be some operational discrepancies.




.
s
l
e
d
o
m
e
n
o
b
k
c
a
b
s
u
o
i
r
a
v
r
o
f

t
e
s

t
s
e
t


C
O
V
L
A
C
S
A
P
e
h
t
n
o
s
t
n
a
i
r
a
v
e
r
a
w
a
‐
e
g
d
e
l
w
o
n
k
e
h
t
d
n
a
s
t
l
u
s
e
r
e
n

i
l
e
s
a
b
e
h
t

f
o
n
o
s
i
r
a
p
m
o
C

.

l


e
b
a
T

s
t
p
e
c
n
o
c
y
b


@

l
l
a
c
e
R

tv

train

sofa

sheep

plant

person

mbike

horse

dog

table

cow

chair

cat

car

bus

bottle

boat

bird

bike

aero

all


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


P
A
m


@


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


d
e
h
s
i
l
b
u
P

N
N
C
R
F


‐
F
K

l
l

A
‐
F
K


‐
t
e
N
s
e
R

t
e
N
C

‐

G
K

N
N
C
R
F


‐
F
K

l
l

A
‐
F
K


t
e
N
C

‐

G
K


t
e
N
C

‐

G
K


‐
t
e
N
s
e
R


t
e
N
C

‐

G
K


t
e
N
C

‐

G
K

N
N
C
R
F


‐
F
K

l
l

A
‐
F
K


‐
G
G
V

N
N
C
R
F


‐
F
K

l
l

A
‐
F
K


t
e
N
C

‐

G
K


t
e
N
C

‐

G
K




### 4.2 COCO

Similar to the VOC dataset, Table 3 shows the originally published results as well as our
results on the COCO dataset for different backbones, namely ResNet‐50 and VGG‐16.
The KF‐All based approach shows a decrease in mAP of 0.2 for both backbones, but an
increase in recall of 0.4 and 0.3 respectively. The authors of [1] claim that the knowledge
graph approaches perform better on the COCO dataset compared to the VOC dataset.
The results show a larger increase in recall (+0.7 compared to ‐0.3), but also a larger
decrease in mAP (‐0.7 compared to ‐0.3), so this claim can be argued as well. Additional
to the recall, the COCO dataset also looks at the recall per area of the objects, as well
as the recall@10. For the published results, the recall@10 shows improvements for all
different approaches as well, whereas for our results, the recall@10 stays more or less the
same. This is an indication that the knowledge aware approach mostly affects the lower
scoring detections. To test this, an extra set of experiments were performed. It can be
concluded that the KF‐All approach indeed performs better than the KF‐500 approach
for all backbones and datasets. It should be noted that the results for the two different
versions of the ConceptNet knowledge graph show no difference at all.

Table 3. Comparison of the baseline results and the knowledge‐aware variants on the MS COCO
2014 test split. Published results are marked with ‘*’.

mAP
@100 @100 @10

recall

recall@100 by area
small medium large

Published
FRCNN
KF‐500
KF‐All
KG‐CNet
ResNet‐50
FRCNN
KF‐500
KF‐All
KG‐CNet57
KG‐CNet55
VGG‐16
FRCNN
KF‐500
KF‐All
KG‐CNet57
KG‐CNet55

24.5
24.4
24.5
24.5

27.9
27.5
27.7
27.2
27.2

24.3
24.0
24.1
23.7
23.7

35.9
37.1
37.9
38.9

47.2
47.2
47.6
47.9
47.9

44.1
44.0
44.4
44.7
44.7

35.2
35.6
36.2
36.6

32.3
32.3
32.3
32.1
32.1

29.0
29.0
29.0
28.8
28.8

14.2
14.3
14.6
14.4

30.4
30.0
30.5
29.9
29.9

27.8
27.8
28.0
27.6
27.6

41.5
42.8
43.9
45.2

50.4
50.4
50.9
51.0
51.0

46.7
46.8
47.2
47.5
47.5

55.6
57.3
58.6


59.6
59.7
60.2
61.1
61.1

56.5
56.1
56.6
57.4
57.4

### 4.3 Results beyond the paper

To show the effects of the re‐optimization process, two more sets of experiments were
performed on the VOC dataset. Firstly, the effects of the bounding box score threshold
were experimented. A set of 6 different thresholds were tested in the range of 1e‐5, as
used in the published method, and 0.05, which is the default value for Faster R‐CNN
implementations. Even though the maximum detections per image is kept at 500, only
a handful of detections (averaged at 6.2 per image) surpass this threshold value. This
higher threshold experiment can show the effects of the re‐optimization from a more
practical point of view.




Figure 5 and 6 show the resulting mAP@100 and recall@100 (averaged per class) for the
different thresholds. Only one knowledge graph based (KG‐CNet57) and one frequency
based approach (KF‐All) were tested, in addition to the baseline. The results show that
for a practical threshold score the recall is not affected at all, meaning that there is no increase in True Positive detections. The decrease in mAP implies that the detections that
changed label after re‐optimization, on average, changed for the worse. This decrease
is present for the 0.05 threshold, but largest at the 1e‐2 mark.

Figure 5. mAP@100 for various box score thresholds

Figure 6. recall@100 for various box score thresholds

The second set of experiments were performed to show the effect of the re‐optimization
parameter ϵ. mAP@100 and recall@100 are again reported for the two re‐optimization
approaches for different values of ϵ. A range of [0.05, 1.0] in steps of 0.05 was reported.
The results are shown in Figure 7 and 8. It should be noted that an ϵ of 1 is the same
as using the FRCNN baseline. The results show that the chosen value of 0.9 is indeed
optimal compared to the other values, but it also shows that by increasing the knowledge
awareness part, the performance is affected negatively.

Figure 7. mAP@100 for various values of epsilon Figure 8. recall@100 for various values of epsilon

## 5 Discussion

As the source codes were not published for the original paper, the methods had to be
implemented from scratch. During implementation it became evident that some details
were missing in the description of the methodology. Mainly, the lack of parameters to
determine baseline results, the missing final hyper‐parameter ϵ, and the fact that the




non‐highest‐scoring class probabilities are set to 0. Without clarification on these details by the author of [1], the reproducibility of the paper would be based on our own
assumptions. Especially the latter is a crucial, non‐trivial implementation detail, since
the methodology clearly describes the use of different class probabilities for each bounding box. As Faster R‐CNN only outputs the one highest scoring probability per bounding
box, it is ambiguous where the other probabilities come from. For simplification these
probabilities were set to 0, an important fact that should have been mentioned in the
original paper.
Based on the results presented in Tables 2 and 3, none of the re‐optimization approaches
confirms the claim of maintaining mAP while increasing recall on both the VOC as
COCO dataset. A similar trend in re‐optimization effects is shown for two completely different backbone models (ResNet‐50 and VGG‐16). Additionally, a simpler version of the
used backbone model (ResNet‐18) also shows no benefits for either a ’better’ or ’worse’
object detection model, so it cannot be claimed that a better model infers the semantic
knowledge by itself.
It can be concluded that our reproduced results contradict the claims of the authors of
the original paper [1]. Their claim stated that the semantic consistency in background
knowledge can be applied to ‘any’ object detection model and increase performance. By
failing to produce similar results, for various models, including the one used in [1], the
claim cannot be reproduced and confirmed.
The results do show that the quality of background information matters, as the frequency based approach that uses all dataset images, consistently outperforms the same
approach that uses only 500 images. The fact that there is no difference at all between
two versions of the knowledge graphs shows that there might be more beneficial ways
to extract the semantic consistency matrices from the graphs. Additional experiments
were done to show the effects of the knowledge aware re‐optimization on different box
score thresholds. It can be concluded that for a more practical object detection situation with a threshold of 0.05 (default in object detection), there are no improvements in
performance. An additional experiment was done to show the effect of hyperparameter
ϵ as this was not presented by the original paper.

### 5.1 What was easy

The methodology of the paper was written clearly, which made it conceptually easy to
comprehend what was going on. It was easy to understand which datasets, networks
and metrics were used for their experiments and their results gave a clear overview for
us to compare our reproductions.

### 5.2 What was difficult

The paper was not supported by any available code, which meant that the reproduction
had to be built from scratch. This was the main reason to choose for the PyTorch environment. Unfortunately there was no VGG16‐backboned Faster R‐CNN directly available in this environment. Therefor the closest related model was chosen, which was the
ResNet50‐backboned Faster R‐CNN. After reviewing the results, another attempt was
made to include the VGG‐16 backboned results as well, which was not a simple process.
During implementation of the methodology it became apparent that some crucial details were missing from the paper. Mainly the fact that other class probabilities were
set to 0 after extracting the highest scores from the model. Also the final used value of ϵ
was not mentioned and the lack of explanation of baseline parameters made it difficult
to get to the correct implementation.




### 5.3 Communication with the authors

The paper mentioned the email addresses of 5 authors, out of which 2 were rejected.
After contacting the others 3 times, there was still no response. By coincidence, a different email address of Yuan Fang was found online, to which he responded quickly and
provided us with the missing details and other further explanations.

References

1.

Y. Fang, K. Kuan, J. Lin, C. Tan, and V. Chandrasekhar. “Object detection meets knowledge graphs.” In: Proceed-
ings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, {IJCAI-17}. International
Joint Conferences on Artificial Intelligence, 2017, pp. 1661–1667.

3.

4.

2. M. Everingham, L. Van Gool, C. K. I Williams, J. Winn, A. Zisserman, M. Everingham, L. K. Van Gool Leuven, B.
CKI Williams, J. Winn, and A. Zisserman. “The PASCAL Visual Object Classes (VOC) Challenge.” In: Int J Comput
Vis 88 (2010), pp. 303–338.
T. Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollár, and C. L. Zitnick. “Microsoft COCO:
Common objects in context.” In: Lecture Notes in Computer Science (including subseries Lecture Notes in
Artificial Intelligence and Lecture Notes in Bioinformatics). Vol. 8693 LNCS. PART 5. Springer Verlag, May
2014, pp. 740–755.
S. Ren, K. He, R. Girshick, and J. Sun. “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal
Networks.” In: IEEE Transactions on Pattern Analysis and Machine Intelligence 39.6 (June 2017), pp. 1137–
1149.
E. Krupka and N. Tishby. “Incorporating prior knowledge on features into learning.” In: Journal of Machine
Learning Research. Vol. 2. 2007, pp. 227–234.
L. Ehrlinger and W. Wöß. “Towards a definition of knowledge graphs.” In: CEUR Workshop Proceedings. Vol. 1695.
2016.
J. F. Sowa. “Semantic Networks.” In: Encyclopedia of Artificial Intelligence (1992).
R. Speer, J. Chin, and C. Havasi. “ConceptNet 5.5: An Open Multilingual Graph of General Knowledge.” In: (Dec.
2016).

7.
8.

6.

5.

9. G. Bouma. “Normalized ( Pointwise ) Mutual Information in Collocation Extraction.” In: Proceedings of German

Society for Computational Linguistics (GSCL 2009) (2009), pp. 31–40.

10. H. Tong, C. Faloutsos, and J.-Y. Pan. Fast Random Walk with Restart and Its Applications. Tech. rep.
11.

J. Jung. Python Implementation for Random Walk with Restart (RWR). 2021.

---
**Source PDF:** `175adfd3b240.pdf` (2023_04_article.pdf)  
**URL:** https://zenodo.org/record/7800679/files/article.pdf
