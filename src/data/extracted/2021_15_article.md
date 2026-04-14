R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Improving Multi-hop Question Answering over
Knowledge Graphs using Knowledge Base Embeddings

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4834942

Jishnu Jaykumar P1, ID and Ashish Sardana1, ID
1NVIDIA, Bengaluru, India

## 1 Reproducibility Summary

### 1.1 Scope of Reproducibility

Our work consists of four parts:

1. Reproducing the results from [1].

2. Exploring the effect of various knowledge graph embedding models in the Knowl-

edge Graph Embedding module.

3. Exploring the effect of various transformer models in the Question Embedding

module.

4. Verifying the importance of the Relation Matching (RM) module.

Based on the code shared by the authors, we have reproduced the results for Embed-
KGQA[1]. We have not performed relation matching deliberately to validate point-4.

### 1.2 Methodology

We have used the code provided by [1] with some customization for reproducibility. In
addition to making the codebase more modular and easy to navigate, we have made
changes to incorporate different transformers in the question embedding module. Question-
Answering models were trained from scratch as no pre-trained models were available
for our particular dataset. The code for this work is available on GitHub (See page footer
for the link).

### 1.3 Results

We were able to reproduce the Hits@1 to be within ±2.4% of the reported value (in most
cases). Anomalies were observed in 2 cases.

1. In MetaQA-KG-Full (3-hop) dataset.

2. WebQSP-KG-Full dataset.


Code
available
swh:1:dir:c95bc4fec7023c258c7190975279b5baf6ef6725.
Open peer review is available at https://openreview.net/forum?id=VFAwCMdWY7.

https://github.com/jishnujayakumar/MLRC2020-EmbedKGQA.

at

is

–

SWH




From our experiments on the QA model, we have found that a recent transformer archi-
tecture, SBERT[2] produced better accuracy than the original paper. Replacing RoBERTa[3]
with SBERT[2] increased the absolute accuracy by ≈3.4% and ≈0.6% in the half KG and
the full KG case respectively. (KG: Knowledge Graph, ”≈”: Approximately)

### 1.4 What was easy

As the code was open-sourced, we didnʼt have to implement the paper giving us the
liberty to customize the codebase to focus on the authorʼs claim validation, perform
extended experiments and explore shared as well as new models. In addition to this,
pretrained KG embedding models were shared which helped in the reproduction exper-
iment.

### 1.5 What was difﬁcult

The lack of comprehensive documentation along with missing comments defining func-
tions/classes/attributes etc. made it laborious to review the code and modify it. In ad-
dition to large training times for question answering models, the knowledge graph em-
beddings also required a significant amount of computing resources.

### 1.6 Communication with original authors

We had a couple of virtual meetings with Apoorv Saxena1, the primary author of Em-
bedKGQA[1].

## 2 Introduction

Knowledge is the key to question answering task. Knowledge Graph (KG) is a multi-
relational graph consisting of entities as nodes and relations among them as typed edges.
KGs can accommodate a wide variety of facts, making them one of the potential candi-
dates for intelligent decision-making. Question Answering over KG (KGQA) task aims to
answer natural language queries posed over the KG. Multi-hop KGQA is a trending topic
and has gained traction from both academia and industry recently. Multi-hop KGQA
task involves reasoning over multiple edges of the KG to arrive at the correct answer.
Earlier works on KGs(e.g. [4], [5], [6], [7]) have some element of sparsity, i.e. they do
not capture all the facts available in the real world. Recent research on multi-hop KGQA
has attempted to reduce this sparsity with the help of relevant external textual resources
that are not readily available. On the other side, KG embeddings have emerged as an ef-
fective tool to overcome the KG sparsity by predicting missing links in the KG. Although
effective, KG embeddings have not been explored for the multi-hop KGQA task. [1] fills
this gap with the proposed EmbedKGQA method. This work intends to reproduce and
perform an ablation (removing relation matching module) as well as an extended study
on EmbedKGQA[1]. EmbedKGQA claims to be the first of its kind to use KG embeddings
for multi-hop KGQA and improves over other state-of-the-art (SOTA) baselines.

## 3 Scope of reproducibility

According to [1], using ComplEx [8] KG embeddings significantly improves Hits@1 for
multi-hop KGQA task and it has been proved with the help of the results on MetaQA [9]
and WebQSP [10] datasets. This reproducibility work tries to test this claim and conducts

1https://apoorvumang.github.io




Figure 1. Overview of EmbedKGQA, the proposed method for Multi-hop KGQA. Image source: [1].

experiments as mentioned in table:{2,3} of the original paper. Section 5.1 contains the
corresponding results which support the claim with some anomalies.

## 4 Methodology

The authors of the original paper have open-sourced the code along with the data and
pre-trained ComplEx KG embedding models. We have used the same codebase (com-
mit:5d8fdbd4) and customized it for our purposes. In addition to this, we have added
comprehensive documentation to make it more interpretable. Moreover, a command-
line functionality is also added to easily configure various transformers models in the
training workflow.

### 4.1 Model descriptions

As shown in Figure:1, EmbedKGQA has three modules:

1. KG Embedding Module - This module contains a KG embedding model called Com-
plEx [8] to learn embeddings for all entities in the input KG. 4 pretrained models
have been shared by the author which contains 2 models for MetaQA-KG-{Full, 50}
as well as 2 models WebQSP-KG-{Full,50} dataset. Details about the dataset are
mentioned in section:4.2.

2. Question Embedding Module: Given a question q, head entity h and set of answer
entities A, this module learns the question embeddings based on the score func-
tion defined by the KG embedding method used in 1.

3. Answer Selection Module: This module uses the outputs of module:1 and 2 to se-
lect the final answer by scoring the <head-entity, question> pair against all possi-
ble answers. The strategy is mentioned in section:{4.4, 4.4.1} of the original paper
respectively.

### 4.2 Datasets

There are two datasets used in the original paper. MetaQA [9] and WebQSP [10]. Both
datasets have two portions. (1) KG data (2) QA data. KG data for both are further divided
into two categories. (1) Using the full KG (indicated by suffix KG-Full) and (2) Using




Dataset

Train

MetaQA 1-hop

96,106

Dev

9,992

Test

9.947

MetaQA 2-hop

118,948

14,872

14,872

MetaQA 3-hop

114,196

14,274

14,274

WebQSP

2,998


1,639

Table 1. QA data statistics for each dataset according to [1]

Dataset

Triples

Entities

Relations

Experiment-Alias


135k

43k

WebQSP-KG-Full

5.7 million

1.8 million


WebQSP-KG-50

ϕ

ψ

-

-


γ

-

-

MetaQA_full

fbwq_full

MetaQA_half

fbwq_half

Table 2. KG data statistics for each dataset. Refer2 for more details.

Experiment-Alias is the name used for the respective datasets in experiments.

γ = Contains all facts that are within 2-hops of any entity mentioned in the questions of WebQSP.

ϕ = Contains only 50% of the triples (randomly selected without replacement).

ψ = Contains 50% of the edges sampled randomly from fbwq_full.

only 50% of the facts in the respective KGs (indicated by suffix KG-50). The details of
generating custom KG datasets are discussed here2. Both datasets are taken from here3.
Statistics for table:{1, 2} have been taken from [1]. For generating question embeddings
the question is placed between <s> and </s> tags for all transformers except Sentence-
Transformer as it takes the input sentence in its pure form. The preprocessing used in
the original code has been used here. No additional preprocessing has been performed
from our end.

### 4.3 Hyper-Parameters

Hyper-parameters used to train the models arenʼt explicitly shared in the codebase or the
paper, hence we decided to use the default values provided in codebase2 to compensate
for the lack of time. For reproduction, a pretrained model shared along with the data
was used; ComplEx[8] was used as the knowledge graph embedding method for all the
KG types, i.e., full and half of both datasets types. For reproducibility, hyper-parameters
for training MetaQA and WebQSP QA models have been taken from section:{MetaQA4,
WebQuestionsSP5} of the original codebase respectively. For RoBERTa [3], a pretrained
model roberta-base has been taken from HuggingFace transformers package [11]. Other
hyper-parameters are populated by default values in codebase2.

### 4.4 Experimental setup and code

Experiments have been performed on the NVIDIA DGX-1 server with 8xV100 GPUs, out
of which 6 were used in this work. The metric used for validating the claims is Hits@1.
According to [12], Hits@k is the proportion of test triples ranking in the top-k results.
The code for this work is open-sourced on GitHub6. In addition to this, we have shared
a couple of Docker images7 for easy kick-starting of experiments without the hassle of

2https://github.com/malllabiisc/EmbedKGQA
3https://drive.google.com/drive/folders/1RlqGBMo45lTmWz9MUPTq-0KcjSd3ujxc (As of January, 2021)
4https://github.com/malllabiisc/EmbedKGQA#metaqa
5https://github.com/malllabiisc/EmbedKGQA#webquestionssp
6https://github.com/jishnujayakumar/MLRC2020-EmbedKGQA
7https://github.com/jishnujayakumar/MLRC2020-EmbedKGQA#helpful-pointers




Type


1-hop

2-hop

3-hop

1-hop

2-hop

3-hop

Train (t)

350 seconds

380 seconds

380 seconds

280 seconds

330 seconds

320 seconds

Validation (v)

42 seconds

95 seconds

147 seconds

47 seconds

108 seconds

182 seconds

T

10.89 hours

13.19 hours

14.64 hours

9.08 hours

12.16 hours

13.94 hours

Type

WebQSP-KG-Full WebQSP-KG-50

Train (t)

280 seconds

300 seconds

Validation (v)

95 seconds

105 seconds

T

10.42 hours

10.92 hours

Table 3.
tal_epochs=100)

Time for training/validation.

Refer section:4.3 for hyper-parameters.

(r=1,

to-

For table:3, validate_every = The number of train routines before validation for a single epoch
Total runs (r) = Number of times the training has been performed for a particular task
Total train time (GPU hours) excluding early stopping, T = (total_epochs × (t + v)) × r

setting up the environment. Following trained models are made available in our Docker
image7, chosen based on better performance in our extended study.

• TuckER KG embedding model for Meta-QA-{Full, 50}

• QA models trained using ComplEx as KG embedding model and SBERT mentioned

in table:4 as question embedding model for WebQSP-KG-{Full, 50}

### 4.5 Computational requirements

This work has been performed on 6 V100-16GB GPUs connected via NVLink. NVLink
reduced multi-GPU training time by 1/4. The time required for various reproductions
are mentioned in table:{3}.

### 4.6 Extended Experiments

Apart from reproducing the results mentioned in the original paper, a couple of ex-
tended experiments have been performed to find answers to the following two ques-
tions:

1. Can recent KG embedding methods like TuckER [13] give higher accuracy on higher
levels of hops, i.e., 3-hop scenario to be specific compared to [8] used in the origi-
nal paper?

2. Can other transformer architectures like ALBERT [14], XLNet [15], Longformer [16]

and SBERT [2]) improve the results on WebQSP [10]?

Details of hyper-parameters used for these experiments are available in our GitHub
repository6. Various transformer models used for experiment-2 are mentioned in ta-
ble:4.

## 5 Results

We report results for reproducibility as well as our extended experiments. The results
of reproduction have a mixed nature while the ones for our extended experiments show




Transformer

RoBERTa

XLNet

ALBERT

Pretrained-Model

roberta-base

xlnet-base-cased

albert-base-v2

SentenceTransformer (SBERT)

sentence-transformers/bert-base-nli-mean-tokens

Longformer

allenai/longformer-base-4096

Table 4. Pretrained models from HuggingFace transformers package [11]

Model

RM


EmbedKGQA

EmbedKGQA (Reproduced)

∆


-

1-hop

2-hop

3-hop

1-hop

2-hop

3-hop

97.5

95.4

98.8

96.4

94.8

72.3

83.9

83.2

91.8

91.6

70.3

71.2

−2.1

−2.4 −22.5 −0.7

−0.2

0.9

Table 5. Hits@1 results for original and reproduced experiments using MetaQA-KG-{Full, 50}
datasets. ∆ = (Reproduced Hits@1 without RM) - (Original Hits@1 with RM)

.

Model

EmbedKGQA

EmbedKGQA

EmbedKGQA (Reproduced)

∆original

∆

RM WebQSP-KG-Full WebQSP-KG-50


66.6

53.2


-

-

48.1

54.9

18.5

6.8

47.4

41.3

5.8

-6.1

Table 6. Hits@1 results for original and reproduced experiments using WebQSP-KG-{Full, 50}
datasets. ∆=(Reproduced Hits@1 without RM) - (Original Hits@1 without RM), ∆original = (Origi-
nal Hits@1 with RM) - (Original Hits@1 without RM).

For table:{5, 6}, KG-Embedding-Model=ComplEx. RM=Relation Matching, 4= inclusion, 8=
exclusion. The original values for EmbedKGQA are taken from [1]. Underline indicates anomaly
due to the absence of RM module.

positive signs to support claim-1, 2. Detailed discussion about the results can be found
in section:6. For all tables in this report, bold values indicate better performance.

### 5.1 Results reproducing original paper

We perform two experiments based on the two datasets introduced in section:4.2. These
experiments provide vital information about the results mentioned in table:{2,5} of the
original paper. The results of the two are reported in table:{5, 6} respectively. From the
results of table:5 in [1] and table:6 in this report, it is evident that relation matching(RM)
is an important component in multi-hop KGQA when the given KG is considerably large,
i.e. {MetaQA, WebQSP} KG-Full; Definitely, WebQSP-KG-50 also shows improvement in
presence of RM but the performance significantly improves when applied to KG-Full
setting. The author of [1] had also expressed the same opinion in one of the virtual
meetings. For table:{7, 8}, ∆= (TuckER Hits@k) - (ComplEx Hits@k).




KG-Model

1-hop


2-hop

3-hop

Hits@1 Hits@5 Hits@10 Hits@1 Hits@5 Hits@10 Hits@1 Hits@5 Hits@10

ComplEx

TuckER

95.39

95.51

99.83

99.81

99.97

99.97

96.46

93.13

99.02

98.7

99.27

99.28

72.33

73.81

93.27

93.6

95.66

96.09

∆

0.12

-0.02


-3.33

-0.32

0.01

1.48

0.33

0.43

Table 7. Comparison of ComplEx with TuckER based on Hits@k results for MetaQA-KG-Full dataset.
k ∈ {1, 5, 10}.

KG-Model

1-hop


2-hop

3-hop

Hits@1 Hits@5 Hits@10 Hits@1 Hits@5 Hits@10 Hits@1 Hits@5 Hits@10

ComplEx

### 83.24 TuckER


89.83

89.36

91.22

90.41

91.63

86.07

97.08

94.66

98.04

96.4

71.2

71.96

90.77

91.16

93.72

93.94

∆

-0.24

-0.47

-0.81

-5.56

-2.42

-1.64

0.76

0.39

0.22

Table 8. Comparison of ComplEx with TuckER based on Hits@k results for MetaQA-KG-50 dataset.
k ∈ {1, 5, 10}.

### 5.2 Results beyond the original paper

We have conducted two additional experiments from our end to find an answer to claim:{1,2}.
The results in table:{7,8} support claim-1 but with a caveat. On the other hand, values
in table:9 improve upon the results reported by the original paper creating a new SOTA
baseline. Additional experiments ingest custom hyper-parameters mentioned in our
codebase in absence of the original hyper-parameters. None of these experiments in-
clude the RM module.

## 6 Discussion

The reproducibility results from table:{5,6} corroborate the claims mentioned in sec-
tion:3 to some extent. Reproduced version is within the ±2.4 range (positive value indi-
cates better performance and vice-versa) except for the MetaQA-KG-Full datasetʼs 3-hop
and WebQSP-KG-Full scenario which has a significant drop of 22.5% and 18.5% respec-

Model

WebQSP-KG-Full

WebQSP-KG-50

Hits@1 Hits@5 Hits@10 Hits@1 Hits@5 Hits@10

RoBERTa [3]

XLNet [15]

ALBERT [14]

Longformer [16]

SBERT [2]

54.96

51.98

47.31

54.9

55.55

67.62

64.44

59.83

66.77

68.98

71.97

69.11

63.98

70.47

72.74

41.27

39.33

31.15

41.92

44.65

51.14

49.25

42.31

51.98

53.86

54.19

52.04

45.68

54.83

56.13

∆

0.59

1.36

0.77

3.38

2.72

### 1.94 Table 9. Hits@k results for recent transformer models by [11] used for generating question embed-
dings. KG-Embedding-Method=ComplEx, ∆= (SBERT_Hits@k - RoBERTa_Hits@k), k ∈ {1, 5, 10}




tively. The absence of RM module has been reported and discussed here8,9,10. For a
given question, the RM module uses itʼs context to extract useful information from the
available edges present in the KG. This information is further plugged into the answer
selection module to select more relevant answers. Thus, relation matching is a vital
component in multi-hop question answering, especially in the KG-Full setting where
more edges are present w.r.t. KG-50 setting or any smaller KG w.r.t. the KG-Full setting.
Results from table:{5,6} corroborates the previous statement. Moreover, 
3-hop outperforms the original model by a margin of +0.9% without using RM which is
an interesting observation. Apart from one reported anomaly, the reproduced results
are pretty close to the original results in the case of the MetaQA dataset. The default set
of hyper-parameters mentioned in the original codebase(Refer section: 4.3) were used
in the reproducibility study. The anomaly in WebQSP-KG-Full,i.e. 18.5% drop bolsters
the importance of RM in the KG-Full setting. The reproduced results for WebQSP-KG-
50 are within the ±7% range. The use of different hyper-parameters can be one of the
possible answers to this variation. This value is significant but not w.r.t. WebQSP-KG-
Fullʼs drop of 18.5% which again strengthens the importance of RM in the KG-Full set-
ting. As mentioned in 5.1, RM is highly useful when the KG is considerably large. From
table:{7, 8}, it is clear that TuckER [13] performs better than ComplEx [8] for the 3-hop
scenario for both MetaQA-KG datasets, i.e., Full and 50. Though these results strengthen
claim-1, a more comprehensive set of tests may lead to a concrete conclusion (e.g., ex-
periments employing a broader set of hyper-parameters). According to table:9, in all
the cases, SBERT [2] outperforms RoBERTa [3] used in the original paper creating a new
SOTA benchmark which supports claim-2. Some experiments didnʼt work out due to
the lack of time. E.g. Using RelationalTucker3 [17] and SimplE [18] to test claim-1. Fur-
thermore, the hyper-parameter search couldnʼt be done due to the same reason hence
we had to pick the default ones mentioned in the codebase. All these create room for
further experiments and improvements.

### 6.1 What was easy

The paper was straightforward to understand. The open-sourced codebase helped us
get kick-started.

### 6.2 What was difﬁcult

The structure of the codebase made it difficult to navigate it. Since the code relied upon
different techniques for the two datasets, the development of one function that trains
different kinds of KG embeddings and another function that trains different kinds of QA
models for both datasets was difficult. MetaQA uses LSTM/GRU [19] / [20] while WebQSP
uses RoBERTa [3] to perform the same task of generating question embeddings. Also,
training KG embeddings for MetaQA yields files in the form of NumPy [21] files while
WebQSP uses LibKGE [22] for the same purpose which produces LibKGE specific KG
embedding(KGE) models. Reproduction and the extensive study were a bit hard in the
beginning as KGE and question embedding methodology varied for both datasets. After
having a couple of virtual meetings with the author and code review, it became easier to
conduct the planned experiments. The unavailability of hyper-parameters used to train
each module increased the experiment cycle multi-fold.

### 6.3 Communication with original authors

We had a couple of virtual meetings with the primary author of [1]. Though it was daunt-
ing to understand the codebase due to the reasons mentioned in section:6.2 with the

8https://github.com/malllabiisc/EmbedKGQA/issues/1
9https://github.com/malllabiisc/EmbedKGQA/issues/51
10https://github.com/malllabiisc/EmbedKGQA/issues/56




help and support of the author, it became easier to navigate the codebase.

### 6.4 Future Scope

We think that there is a wide range of empirical analysis and experimentation that can
be performed for multi-hop QA task, out of which we are sharing a few here:

1. Using KG embedding compression techniques like [23] in KG Embedding Module.

2. Using recent transformer models like Performer [24], Reformer [25] etc. for gener-

ating question embeddings.

3. Using low-dimensional hyperbolic KG embeddings [26] in KG embedding module
along with hyperbolic word embeddings [27] for question embedding module.

4. A new approach for sentence embedding, SBERT-WK [28] instead of SBERT [2] can

be tried out.

References

1.

A. Saxena, A. Tripathi, and P. Talukdar. “Improving Multi-hop Question Answering over Knowledge Graphs
using Knowledge Base Embeddings.” In: Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics. Online: Association for Computational Linguistics, July 2020, pp. 4498–4507. DOI:
10.18653/v1/2020.acl-main.412. URL: https://www.aclweb.org/anthology/2020.acl-main.412.

3.

2. N. Reimers and I. Gurevych. “Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.” In: Pro-
ceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. Association for
Computational Linguistics, Nov. 2019. URL: https://arxiv.org/abs/1908.10084.
Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov. RoBERTa: A
Robustly Optimized BERT Pretraining Approach. 2019. arXiv:1907.11692 [cs.CL].
F. M. Suchanek, G. Kasneci, and G. Weikum. “Yago: A Core of Semantic Knowledge.” In: Proceedings of the 16th
International Conference on World Wide Web. WWW ’07. Banff, Alberta, Canada: Association for Computing
Machinery, 2007, pp. 697–706. DOI: 10.1145/1242572.1242667. URL: https : / / doi . org / 10 . 1145 / 1242572 .
1242667.

4.

5. Google. Freebase Data Dumps. 2013. URL: https://developers.google.com/freebase/data.
6.

“Never-Ending Learning.”

J. Lehmann, R. Isele, M. Jakob, A. Jentzsch, D. Kontokostas, P. N. Mendes, S. Hellmann, M. Morsey, P. Van Kleef,
S. Auer, et al. “Dbpedia–a large-scale, multilingual knowledge base extracted from wikipedia.” In: Semantic
web 6.2 (2015), pp. 167–195.
T. Mitchell et al.
10.1145/3191513. URL: https://doi.org/10.1145/3191513.
T. Trouillon, J. Welbl, S. Riedel, É. Gaussier, and G. Bouchard. “Complex Embeddings for Simple Link Prediction.”
In: Proceedings of the 33rd International Conference on International Conference on Machine Learning -
Volume 48. ICML’16. New York, NY, USA: JMLR.org, 2016, pp. 2071–2080.
Y. Zhang, H. Dai, Z. Kozareva, A. J. Smola, and L. Song. “Variational Reasoning for Question Answering with
Knowledge Graph.” In: AAAI. 2018.

In: Commun. ACM 61.5 (Apr. 2018), pp. 103–115. DOI:

7.

8.

9.

11.

10. W.-t. Yih, M. Richardson, C. Meek, M.-W. Chang, and J. Suh. “The Value of Semantic Parse Labeling for Knowl-
edge Base Question Answering.” In: Proceedings of the 54th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 2: Short Papers). Berlin, Germany: Association for Computational Linguistics,
Aug. 2016, pp. 201–206. DOI: 10.18653/v1/P16-2033. URL: https://www.aclweb.org/anthology/P16-2033.
T. Wolf et al. “Transformers: State-of-the-Art Natural Language Processing.” In: Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language Processing: System Demonstrations. Online: Associa-
tion for Computational Linguistics, Oct. 2020, pp. 38–45. URL: https://www.aclweb.org/anthology/2020.
emnlp-demos.6.
Y. Wang, D. Rufﬁnelli, R. Gemulla, S. Broscheit, and C. Meilicke. On Evaluating Embedding Models for Knowl-
edge Base Completion. 2019. arXiv:1810.07180 [cs.AI].
I. Balažević, C. Allen, and T. M. Hospedales. “Tucker: Tensor factorization for knowledge graph completion.” In:
arXiv preprint arXiv:1901.09590 (2019).
Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut. “Albert: A lite bert for self-supervised
learning of language representations.” In: arXiv preprint arXiv:1909.11942 (2019).

13.

12.

14.




15.

16.

17.

18.

19.

20.

21.

22.

Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, and Q. V. Le. “Xlnet: Generalized autoregressive
pretraining for language understanding.” In: Advances in neural information processing systems. 2019,
pp. 5753–5763.
I. Beltagy, M. E. Peters, and A. Cohan. Longformer: The Long-Document Transformer. 2020. arXiv:2004.05150
[cs.CL].
Y. Wang, S. Broscheit, and R. Gemulla. A Relational Tucker Decomposition for Multi-Relational Link Predic-
tion. 2019. arXiv:1902.00898 [cs.LG].
S. M. Kazemi and D. Poole. SimplE Embedding for Link Prediction in Knowledge Graphs. 2018.
arXiv:1802.04868 [stat.ML].
S. Hochreiter and J. Schmidhuber. “Long short-term memory.” In: Neural computation 9.8 (1997), pp. 1735–
1780. URL: https://www.bibsonomy.org/bibtex/2a4a80026d24955b267cae636aa8abe4a/dallmann.
J. Chung, C. Gulcehre, K. Cho, and Y. Bengio. Empirical Evaluation of Gated Recurrent Neural Networks on
Sequence Modeling. 2014. arXiv:1412.3555 [cs.NE].
C. R. Harris et al. “Array programming with NumPy.” In: Nature 585 (2020), pp. 357–362. DOI: 10.1038/s41586-
020-2649-2.
S. Broscheit, D. Rufﬁnelli, A. Kochsiek, P. Betz, and R. Gemulla. “LibKGE-A knowledge graph embedding library
for reproducible research.” In: Proceedings of the 2020 Conference on Empirical Methods in Natural Lan-
guage Processing: System Demonstrations. 2020, pp. 165–174.

23. M. Sachan. “Knowledge Graph Embedding Compression.” In: Proceedings of the 58th Annual Meeting of the

Association for Computational Linguistics. 2020, pp. 2681–2691.
K. Choromanski et al. Rethinking Attention with Performers. 2020. arXiv:2009.14794 [cs.LG].

24.
25. N. Kitaev, Ł. Kaiser, and A. Levskaya. Reformer: The Efﬁcient Transformer. 2020. arXiv:2001.04451

26.

27.

28.

[cs.LG].
I. Chami, A. Wolf, D.-C. Juan, F. Sala, S. Ravi, and C. Ré. “Low-Dimensional Hyperbolic Knowledge Graph Embed-
dings.” In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. Online:
Association for Computational Linguistics, July 2020, pp. 6901–6914. DOI: 10.18653/v1/2020.acl-main.617.
URL: https://www.aclweb.org/anthology/2020.acl-main.617.
B. Dhingra, C. Shallue, M. Norouzi, A. Dai, and G. Dahl. “Embedding Text in Hyperbolic Spaces.” In: Proceed-
ings of the Twelfth Workshop on Graph-Based Methods for Natural Language Processing (TextGraphs-
12). New Orleans, Louisiana, USA: Association for Computational Linguistics, June 2018, pp. 59–69. DOI:
10.18653/v1/W18-1708. URL: https://www.aclweb.org/anthology/W18-1708.
B. Wang and C. .-.-. J. Kuo. “SBERT-WK: A Sentence Embedding Method by Dissecting BERT-Based Word Mod-
els.” In: IEEE/ACM Transactions on Audio, Speech, and Language Processing 28 (2020), pp. 2146–2157.

---
**Source PDF:** `ed4b6afac9a3.pdf` (2021_15_article.pdf)  
**URL:** https://zenodo.org/record/4834942/files/article.pdf
