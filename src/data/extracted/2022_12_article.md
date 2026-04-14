R E S C I E N C E C

Replication / ML Reproducibility Challenge 2021
[Re] A Cluster-based Approach for Improving Isotropy in
Contextual Embedding Space

Edited by
Koustuv Sinha,
Sharath Chandra Raparthy

Reviewed by
Anonymous Reviewers

Received
04 February 2022

Published
23 May 2022

DOI
10.5281/zenodo.6574649

Benjamin Džubur1, ID
1University of Ljubljana, Ljubljana, Slovenia

## 1 Reproducibility Summary

Scope of Reproducibility

The authors of the paper, which we reproduced, introduce a method that is claimed to
improve the isotropy (a measure of uniformity) of the space of Contextual Word Representations (CWRs), outputted by models such as BERT or GPT‐2. As a result, the method
would mitigate the problem of very high correlation between arbitrary embeddings of
such models. Additionally, the method is claimed to remove some syntactic information embedded in CWRs, resulting in better performance on semantic NLP tasks. To
verify these claims, we reproduce all experiments described in the paper.

Methodology

We used the authors’ Python implementation of the proposed cluster‐based method,
which we verified against our own implementation based on the description in the paper. We re‐implemented the global method based on the paper from Mu and Viswanath
[1], which the cluster‐based method was primarily compared with. Additionally, we
re‐implemented all of the experiments based on descriptions in the paper and our communication with the authors.

Results

We found that the cluster‐based method does indeed consistently noticeably increase
the isotropy of a set of CWRs over the global method. However, when it comes to semantic tasks, we found that the cluster‐based method performs better than the global
method in some and worse in other tasks, or that the improvements are within margin
of error. Additionally, the results of one side experiment, which analyzes the structural
information of CWRs, also contradict the authors’ findings for the GPT‐2 model.

What was easy

The described methods were easy to understand and implement, as they rely on PCA
and K‐Means clustering.


Code is available at https://github.com/Benidzu/isotropy_reproduction. – SWH swh:1:dir:407d517fb5299301bcfc7f8aa461a4c3bf7c36b0.
Open peer review is available at https://openreview.net/forum?id=rxWeB3zQ2CY.




What was difficult

There were many ambiguities in the paper: which splits of data were used, the procedures of the experiments were not described in detail, some hyperparameters values
were not disclosed. Additionally, running the approach on big datasets was too computationally expensive. There was an unhandled edge case in the authors’ code, causing
the method to fail in rare cases. Some results had to be submitted online, where there
is a monthly limit of submissions, causing delays.

Communication with original authors

We exchanged many e‐mails with the authors, which were very responsive and helpful in
describing the missing information required for reproduction. In the end, we still could
not completely identify the sources of some remaining discrepancies in the results, even
after ensuring the data, preprocessing and some other implementation details were the
same.




## 2 Introduction

Embeddings from popular contextual NLP models such as BERT [2], GPT‐2 [3], 
[4], etc. suffer from the so‐called representation degeneration problem [5], where the
individual tokens’ embeddings form an anisotropic cone‐like shape in the embedding
space. This means that even unrelated words can have excessively positive correlations.
Methods which study and attempt to improve the isotropy (a measure of uniformity) of
the space on a global level (e.g. [1]) have been predominantly used so far to tackle this
problem. However, due to the clustered structure of these Contextual Word Representations (CWRs), the authors of the chosen paper [6] propose a local, cluster‐based method,
which could further improve on the existing global approaches.
Apart from further improving isotropy, the method supposedly also removes some local
structural and syntactic information within the clusters, improving the CWRs performance on semantic tasks.

## 3 Scope of reproducibility

Throughout the paper, the authors use contextual embeddings of three models to support their claims: BERT, RoBERTa and GPT‐2. Various datasets are used to generate
these contextual embeddings, which are then enhanced with the proposed method,
evaulated and used to support claims about the performance of the method. Specifically, these claims are:

• Claim 1: The cluster‐based method outperforms the baseline and global method,
in all cases in terms of isotropy of CWRs as well as in almost all cases in terms of
Spearman correlation performance, on 7 Semantic Textual Similarity (STS) datasets.

• Claim 2: A wide and shallow Multi‐Layer Perceptron (MLP) performs the best in
terms of accuracy on all 6 chosen binary classification tasks from the GLUE [7]
and SuperGLUE [8] benchmarks, when trained on BERT emebeddings which were
enhanced by the cluster‐based approach.

• Claim 3: A MLP described as in Claim 2 also converges to an optimum in fewer

epochs, when the embeddings are enhanced by the cluster‐based approach.

• Claim 4: Removing dominant directions from CWRs of punctuations and stop
words in sentences with the same syntactic structure (same group) results in fewer
nearest neighbors of the CWRs being from the same group, as syntactic information is discarded.

• Claim 5: The cluster‐based approach brings together verbs which have the same
meaning (sense) but different tense as seen in the SemCor corpus, by decreasing
the average euclidean distance between their CWRs, relative to the distance between verbs in the same tense but with a different sense.

In our reproduction, we verify all the listed claims by reproducing all the related experiments. Claims 1 and 2 are the most important ones as they directly address the performance of the cluster‐based method, while Claims 3, 4 and 5 are essentially attempted
explanations of different side effects of the proposed method.
In addition to these claims, the authors analyze the effect of the number of clusters
in the K‐Means algorithm on isotropy as well as evaluate the layer‐wise isotropy of the
contextual models. We have also reproduced these, purely statistical experiments for
the sake of completeness of our reproduction.




## 4 Methodology

The paper referenced a Github repository 1, in which we found a single Jupyter notebook with the implementation of the cluster‐based method, the isotropy metric, as well
as an example of evaluating the isotropy and Spearman correlation performance on the
STS‐B dataset. We first re‐implemented the cluster‐based method and verified that it
works the same way – however in the end we used the authors implementation due to
its slightly better runtime. There was an unhandled edge case in the original implementation however – if fewer embeddings belonged to some cluster than the number of PCs
to be removed, the original implementation would result in an out‐of‐bounds exception.
We fixed this by repeating the clustering step until each cluster was sufficiently represented. The method uses the Scipy library for K‐Means clustering and ScikitLearn for
PCA.
As the global method is simply a special case of the cluster‐based method with the number of clusters k = 1, its re‐implementation was trivial.
We did however have to re‐implement all of the experiments only from their descriptions
in the paper and based on the help we got from our correspondence with the authors.
We did not require a GPU for any of our experiments.

### 4.1 Model descriptions & hyperparameters

For the contextual models, we used the Transformers library and the default pre‐trained
weights were used (specifically the casings bert-base-uncased, gpt2 and roberta-base). These
models all output 768‐dimensional embeddings at each of their 12 layers.
As reported in the original paper, the hyperparameters of the global and local, clusterbased approach were set for each model separately, as seen in Table 1. These values
were used for all experiments.

Model

BERT
GPT‐2


k


Removed PCs
(local)


Removed PCs
(global)


Table 1. The number of clusters for the K‐Means clustering local method (k) and number of top
principal components removed for both the local and global method, for each contextual model.

When it comes to GLUE and SuperGLUE binary classification tasks, the contextual embeddings were used to train a fully‐connected MLP. It’s structure remains the same
across all tasks, using the hyperparameters communicated to us by the authors. Specifically, for a single data sample (which is either a sentence or a pair of sentences), we only
consider the first 64 tokens’ representations, which we flatten into a vector of length
64 × 768, which represents our input layer. The next layer is a 100‐dimensional hidden
layer with ReLU activation, followed by the output layer – a single neuron with sigmoid
activation. The MLP is trained using binary cross‐entropy loss and uses the Adam optimizer with step size 0.005, for a maximum of 10 epochs. The reported results are based
on the model which achieves the best validation set score.
For the experiment where we analyze the CWRs of punctuations and stop words, we use
the K‐nearest‐neighbor implementation by ScikitLearn with k = 6, which is exactly the
number of possible neighbors from the same structural group (we only use the first CWR
of the respective punctuation or stop word in a sentence). We then calculate the relative
part of nearest neighbors belonging to the same group for each individual embedding
and average the results. Note that each stop word or punctuation type (e.g. comma) is
analyzed separately and the search is performed only amongst CWRs of the same type.

1https://github.com/Sara-Rajaee/clusterbased_isotropy_enhancement/




Lastly, for the verb tense experiment, we consider verbs with multiple meanings (senses)
and in two tenses – present simple and past simple (e.g. ”say” and ”said” correspond to
the same verb in different tenses by our definition). Then, for each verb, we calculate all
possible euclidean distances between representations of same tense and same meaning,
same tense and different meaning, different tense and same meaning. We then finally
average across all distances at the lowest level of hierarchy. We repeat the calculation
for the representations enhanced by the cluster‐based method.

### 4.2 Datasets

For the main experiment on which Claim 1 in Section 3 is based, 7 Semantic Textual
Similarity (STS) datasets were used. The STS‐2012 to STS‐2016 [9, 10, 11, 12, 13] as well
as STS‐B are available at: https://ixa2.si.ehu.eus/stswiki/index.php/Main_Page , while the SICKR [14] dataset is available at: https://marcobaroni.org/composes/sick.html. Individual data
samples of these datasets are comprised of two sentences, and their semantic similarity/relatedness score, which is a real value on the scale from 0 to 5. In Table 2, the total
number of data samples for each dataset after filtering is seen. Note that only the English test splits were used, as in the original paper. Four of the seven datasets had some
badly encoded samples (no more than 10), which we simply discarded, after preliminary
testing which showed that they do not noticeably affect the results. The two sentences
of each sample were sent through the contextual models separately.

Dataset Test data samples
STS‐2012
STS‐2013
STS‐2014
STS‐2015
STS‐2016
STS‐B
SICK‐R

3101
2250
3746
2983
1162
1095
9840

Task

Train split
(used / total)
RTE 2490 / 2490
CoLA 8551 / 8551
SST‐2 7000 / 67349
MRPC 3668 / 3668
WiC 5428 / 5428
BoolQ 6000 / 9427

Validation split
(used / total)
277 / 277
1043 / 1043
872 / 872
408 / 408
638 / 638
1500 / 3270

Test split

3000
1063
1821
1725
1400
3245

Total
(used)
5767
10657
9693
5801
7466
10745

Table 2. The number of used data
samples in each STS dataset.

Table 3. The number of used data samples in each
GLUE/SuperGLUE task.

For the classification experiment on which Claim 2 in Section 3 is based, a selection
of tasks (datasets) from GLUE [7] (https://gluebenchmark.com/) and SuperGLUE [8] (https://
super.gluebenchmark.com/) were used. In some cases, data samples were composed of pairs
of sentences, while in others, a single sentence was given. In the first case, the pairs
of sentences were encoded together, by concatenating their tokens and adding special
tokens in the following way: [CLS]<sentence1>[SEP]<sentence2>[SEP]. The embeddings
of these special tokens were also considered by the MLP classifier. Note that for the
purpose of this experiment, we first merged the train, validation and test splits before
applying the global or local enhancement method, as did the authors originally. Due
to the big size of SST‐2 and BoolQ datasets, we had to limit the size of training and/or
validation splits by random sub‐sampling. The number of samples for each task are seen
in Table 3. We found that 10745 × 64 was near the maximum number of embeddings
that we could affoard to run PCA on, given our hardware.
For the punctuation / stop word experiment, the authors provided a dataset based on
Ravfogel et al. [15] (available at https://nlp.biu.ac.il/~ravfogs/resources/syntax_distillation/) which
consists of 150000 groups of 6 sentences, where sentences from each group have the
same syntactic structure but different semantics. For each of the tokens of interest separately (”the”, ”of”, ”,” and ”.”), we randomly sampled 200 groups, where each group contained at least one appearance of the token per sentence.
For the verb tense experiment, we used the SemCor corpus [16], available at http://web.
eecs.umich.edu/~mihalcea/downloads.html#semcor. Out of over 30000 sentences, we used 11838




of them, which contained the verbs we were interested in. Specifically, these were verbs
that appeared in present and past tense and also occurred in at least 2 different senses
at least 10 times.
The analysis of layer‐wise isotropy and the number of clusters in K‐Means is done on
the STS‐B dev split.

### 4.3 Experimental setup and code

The code of our reproduction is available at https://github.com/Benidzu/isotropy_reproduction.
The isotropy measure (as defined in the original paper), Spearman performance (which
is just the Spearman coefficient multiplied by 100) and accuracy were the main metrics
used to evaluate our experiments. In order to evaluate the uncertainty in some of the
main results, we resorted to bootstrap as well estimation of variance across multiple
re‐runs of procedures containing stochasticity (e.g. initial positions of centroids in KMeans, initial weights of MLP classifiers).

### 4.4 Computational requirements

The experiments were reproduced on a sytem with the 8‐core, 16‐thread Ryzen 3700x
processor, 16GB of RAM and RTX3060Ti GPU (which was not explicitly used for any experiment).
On a set of 30000 768‐dimensional embeddings, the global method ran for 12.5 seconds
and the local, cluster‐based method for 14 seconds. On a bigger set of 200000 embeddings, the global method ran for 98.9 seconds and the local method ran for 79.8 seconds.
In addition, the local method requires a lot less memory at once, as it performs PCA for
each cluster of embeddings separately.
The training of MLP classifiers for the classification experiments required no more than
a minute on average.

## 5 Results

The reproduced results support some of the claims of the original paper. Specifically,
the cluster‐based method indeed consistently outperforms the global and baseline in
terms of isotropy. However, when it comes to Spearman performance on Semantic Textual Similarity tasks, the local method performs better than the global method on some
datasets and worse on others. Similar is true for the classification tasks, where the difference in performance is mostly within margin of error. Analyzing verb tense, the Claim
5 from Section 3 is fully supported by our reproduction, while some discrepancies are
observed when it comes to Claim 4.

### 5.1 Results reproducing original paper

Semantic Textual Similarity experiment — In this section we address Claim 1 from Section 3.
In Figure 1 we plot the Spearman correlation performance for each method, contextual
model and STS dataset. Due to the random nature of K‐Means, we repeat the experiment with the local method 5 times. We plot the results for each of the five repetitions
individually. Additionally, we report the averages of these five repetitions in Table 4.
Compared to the numbers in Table 2 of the original paper, our results are slightly more
pessimistic. Embeddings enhanced by the local method perform noticeably better than
those, enhanced by the global method, on some datasets and worse on others. There
are also many cases where the difference in performance is within margin of error.
In Table 5 we report the isotropy values of CWRs from each of the STS datasets, for each
contextual model and enhancement method. These results support the original results
achieved by the authors, as seen in Table 6 of the original paper.




Figure 1. Spearman correlation performance on STS tasks. The error bars mark ±1 SE, based on
50 bootstrap replications.

GPT‐2

Model STS‐2012 STS‐2013 STS‐2014 STS‐2015 STS‐2016 SICK‐R STS‐B
64.47
± 0.26
68.18
± 0.71
71.73
± 0.17

62.82
± 0.17
62.83
± 1.87
67.87
± 0.35

57.59
± 0.29
55.65
± 1.20
60.67
± 0.25

65.66
± 0.09
73.96
± 0.53
72.83
± 0.46

50.21
± 0.53
48.29
± 3.03
54.78
± 0.51

52.36
± 0.26
62.7
± 0.27
64.98
± 0.34

57.17
± 0.16
64.37
± 0.29
64.63
± 0.1

BERT


Table 4. Average Spearman correlation performance of 5 repetitions of the local method ± standard
deviation across these repetitions. The results in bold and black represent cases where the local
method outperforms the global method with high probability and the results in red vice‐versa.

GLUE & SuperGLUE classification tasks — In this section we address Claim 2 from Section 3.
In Table 6 we report average scores (accuracy / Matthew’s correlation) of the MLP classifier on the test set based on 5 repetitions. Each repetition, we re‐ran the corresponding
embedding enhancement method and randomly re‐initialized and re‐trained the MLP,
accounting for both sources of variance.
It seems that the classifier trained on locally enhanced embeddings achieves the best
scores on most of the tasks, however, due to the high uncertainty and small differences
between methods, we cannot confidently argue that one method is better than the other.
Due to this uncertainty, our results do not fully support the original findings as seen in
Table 3 in the paper.

Convergence time — In this section we address Claim 3 from Section 3. In Figure 2, we plot
the per‐epoch performance of the MLP for two SuperGLUE tasks on the validation split.
Our results support the original claim, as the MLP converges to an optimum in only a
few iterations when trained on enhanced embeddings, while the same does not hold for
baseline embeddings.

Punctuation and stop word experiment — In this section we address Claim 4 from Section 3.
In Figure 3, we plot the percentage of nearest neighbors from the same structural (syn‐


RoBERTaBERTGPT−2STS−2012STS−2013STS−2014STS−2015STS−2016SICK−RSTS−B020406002040600204060DatasetSpearman performanceEnhancement methodBaselineGlobal methodLocal method

STS 2012 STS 2013 STS 2014 STS 2015 STS 2016 SICK‐R STS‐B
Model
9.3e‐16 1.4e‐120 1.5e‐79
GPT‐2
1.1e‐4
1.0e‐4
BERT
2.5e‐5
4.0e‐6
3.5e‐6
RoBERTa 5.7e‐6
0.51
0.59
0.56
GPT‐2
0.55
0.50
0.46
BERT
0.89
0.88
0.89

0.71
0.70
0.71
GPT‐2
0.73
0.71
0.75
BERT
0.91
0.90
0.91


1.5e‐14 2.1e‐121 3.7e‐116
1.1e‐4
8.6e‐5
5.3e‐4
6.2e‐6
5.8e‐6
4.3e‐6
0.56
0.56
0.58
0.52
0.26
0.45
0.89
0.90
0.87
0.69
0.79
0.72
0.76
0.79
0.72
0.92
0.95
0.91

5.9e‐92
3.8e‐5
5.9e‐6
0.57
0.45
0.88
0.73
0.76
0.92


Global
appraoch

Clusterbased
approach

Table 5. Isotropy of contextual word embeddings before and after enhancement with the global
and local method.


Global approach

Cluster‐based approach

RTE
54.7
± 1.4
54.3
± 2.0
55.1
± 1.6

CoLA SST‐2 MRPC WiC BoolQ Average

7.4
± 16.5
39.9
± 1.7
40.1
± 1.8

84.0
± 0.3
79.7
± 0.3
83.7
± 0.8

66.8
± 0.7
69.6
± 0.8
70.2
± 1.2

53.3
± 5.7
61.5
± 0.8
61.9
± 0.8

62.3
± 0.05
63.4
± 0.5
62.7
± 0.6

54.75
± 4.1
61.4
± 1.0
62.3
± 1.1

Table 6. Results on classification tasks (BERT) in terms of accuracy (except for CoLA: Matthew’s
correlation). Results are based on averages and standard deviations of 5 runs on the official test
set. In bold we mark the highest average score in each column.

tactical) group, for baseline and enhanced embeddings. The results line up with the
authors’ results (Figure 3 in original paper) for BERT and RoBERTa embeddings, where
the removal of dominant directions via the method decreases the percentage of neighbors from the same group. However, this does mostly not hold for GPT‐2 embeddings
in our reproduction.

Impact of cluster‐based
Figure 2.
enhancement on per‐epoch performance.

Figure 3. Percentage of nearest neighbours that share similar
structural and syntactic knowledge, before and after removing dominant directions.

Verb tense experiment — In this section we address Claim 5 from Section 3. In Table 7,
we report the results of the corresponding experiment, described in Section 4.1. The
results support the claim, as they are very similar to authors’ results in Table 4 of the
original paper.

Additional isotropy analysis — In this last section, we report the reproduction results of the
additional isotropy analysis of the contextual models’ embeddings. The results, ana‐


0.500.550.600.6512345678910EpochAccuracyEmbeddingsBaselineIsotropy enhancedTaskBoolQRTEPeriodComma'the''of'GPT−2BERTRoBERTaGPT−2BERTRoBERTaGPT−2BERTRoBERTaGPT−2BERTRoBERTa0.00.20.40.60.8Part of neighbors from same groupEmbeddingsBaselineIsotropy enhanced

Model
GPT‐2
BERT


ST‐SM ST‐DM DT‐SM Isotropy
39.62
2.3e‐05
2.41e‐05
13.43
6.2e‐06
6.20

38.12
13.69
6.39

42.18
14.04
### 7.09 Removed PCs
ST‐SM ST‐DM DT‐SM Isotropy
5.06
10.74
4.10

0.708
0.72
0.82

5.43
11.35
4.46

5.56
11.50
### 4.48 Table 7. Mean Euclidean distance of each occurrence of a verb to all other occurrences of the same
verb with same tense and same meaning (ST‐SM), the same tense and different meaning (ST‐DM),
and different tense but same meaning (DT‐SM). It is desirable that DT‐SM is lower than ST‐DM.

lyzing the impact of number of clusters in K‐Means and the layer‐wise isotropy of the
contextual models are seen in Tables 8a and 8b respectively. Our results support the
original results, as seen in Tables 1 and 5 in the original paper.

Table 8. Additional isotropy analysis. In 8a, we report CWRs isotropy after clustering and zerocentering for different number of clusters (k). In 8b we report per‐layer isotropy.

(a)


k=1
k=3
k=6
k=9
k=20

GPT‐2
1.27e‐126
3.62e‐220
1.21e‐73
3.36e‐61
7.06e‐54
8.42e‐101

BERT
4.91e‐05
1.91e‐05
1.15e‐04
2.97e‐03
0.148
0.265


2.69e‐06
0.015
0.318
0.512
0.549
0.579

(b)

BERT
4.7e‐04
9.4e‐06
1.0e‐06
8.7e‐05
7.4e‐06
4.8e‐06
3.8e‐06
5.1e‐06
1.1e‐05
2.5e‐05
4.3e‐06
2.3e‐07
4.9e‐05

GPT‐2
8.8e‐03
9.4e‐24
1.3e‐24
5.9e‐26
1.5e‐27
2.9e‐30
1.5e‐32
1.3e‐37
3.3e‐45
5.0e‐55
7.0e‐34
1.9e‐132
1.3e‐126

Layer


9.0e‐03
2.5e‐07
8.6e‐10
4.2e‐09
5.4e‐12
4.9e‐10
3.1e‐10
1.3e‐10
1.4e‐10
1.4e‐10
6.5e‐11
1.4e‐10
2.7e‐06

## 6 Discussion

In general, many of the original authors’ claims are supported by our experimentation.
The achieved isotropy scores across the reproduced experiments are similar to the original ones, implying that the cluster‐based method is working as intended. However,
even in situations with seemingly no randomness (extracting baseline embeddings of
datasets and evaluating isotropy), we could not perfectly reproduce the original results.
This might imply discrepancies on hardware‐level computation or due to different versioning of used libraries (e.g. Transformers). Consequently, this perhaps implies that
the local method is not robust enough to such variations, to consistently outperform
the global method (e.g. in terms of Spearman coefficient performance on STS tasks), as
originally claimed.
Similarly, for the classification tasks, after our own re‐implementation, we found out
that authors used Keras for the MLP classifier, while we used ScikitLearn (albeit with all
hyperparameters set equivalently). This was another source of potential discrepancies,
but the similar results reflect that this was not a real issue. A more likely reason for some
differences in this experiment might be the fact that, while the authors stated that they
re‐trained the MLP multiple times before submitting and reporting the results of the
best classifier (chosen by validation set performance), we opted for the more robust and




less biased score estimation via averaging across multiple submissions and additionally
estimating the errors of our estimates.
When it comes to Claims 3 and 5 from Section 3, our results fully support these claims,
although again, we are unable to get exactly the same numbers, perhaps due to the
reasons listed above or due to minor differences in implementation.
Finally, with the punctuation and stop word experiment, we were surprised by the fact
that by removing local dominant directions of CWRs from the GPT‐2 model, we actually increased the percentage of neighbors from the same structural group. Since the
percentage of nearest neighbors with the same syntactical structure was relatively low
to begin with in this case (compared to BERT and RoBERTa), we believe the dominant
directions carried mostly semantic information, and by removing them, the syntactical
information in the embeddings became more dominant.

### 6.1 Recommendations for further experimentation

Unfortunately, due to various limitations and our budget, we could not afford much additional experimentation beyond the scope of the paper. However, during our analysis,
we came up with some ideas and experiments, which could be further looked into. We
list some of these ideas the following.
Firstly, for the GLUE & SuperGLUE classification tasks, the authors first merge train and
test splits and then run the embedding enhancement method and then train the MLP.
In a practical scenario, where we would like to predict the class for a completely new
data sample, repeating this whole process becomes computationally infeasible.
Therefore, the following experimental procedure, where the learning step is performed
only once (and updated on a less regular basis), could be evaluated and compared to the
original one:

1. Run the cluster‐based method on contextual embeddings of the training set. Save
the centroids of each cluster in original space as well as its corresponding top principal components to be removed.

2. Train the MLP on the enhanced embeddings.

3. At prediction time (for test data), extract the contextual embeddings of the new
data sample. For each CWR, enhance it by doing the following: assign it to the
nearest cluster, based on the saved centroids in step 1, then subtract the centroid
and remove the corresponding PCs.

4. Pass the enhanced embeddings of the data sample to the MLP for prediction.

Other additional ideas include experimenting with different MLP architectures, or some
of the remaining GLUE / SuperGLUE tasks, namely COPA, QNLI, QQP, etc. Additionally,
using a different clustering algorithm or distance measure could prove to be beneficial.

### 6.2 What was easy

The explanations of the methods and experiments in the original paper were easy to follow. The cluster‐based method relies on K‐Means clustering and PCA, both of which we
were already familiar with. The code present in the referenced repository was therefore
easy to understand.

### 6.3 What was difficult

Some key implementation details of various experiments and hyperparameters of algorithms were not disclosed in the original paper, making exact re‐implementation of
the experiments more difficult. Even after receiving the necessary information, there




were discrepancies in results which could not be attributed to randomness, differences
in data, or some differences in implementation (assuming authors used the published
code).
Due to some big datasets used in some experiments, we had to subsample the number of data samples to be able to run the described algorithms. Our system would in
some cases completely freeze due our CPU usage reaching 100% because of PCA computations. Additionally, extracting embeddings, re‐running the methods multiple times
and performing expensive procedures such as bootstrap took a lot of time.
The most time‐consuming step by far was estimating the performance and error of our
estimates on GLUE and SuperGLUE classification tasks. In order to get test split results,
one has to manually submit the predictions through the official website. This was an
issue in our case due to the restrictions of submissions – a team is only allowed to make
up to two submissions a day and six per month, which dragged out our collection of
results.

### 6.4 Communication with original authors

We exchanged many e‐mails with the main author of the paper, in order to enquire about
various hyperparameters and other implementation details of each experiment and to
ensure we set up our experiments the same way. The author was quite helpful and responsive. Unfortunately, we had to accept that some discrepancies between our results
would still be present (see Sections 6 and 6.3 for our comments on these discrepancies),
after much time spent attempting to reduce them.

References

1.

2.

3.

4.

5.

6.

7.

8.

J. Mu and P. Viswanath. “All-but-the-Top: Simple and Effective Postprocessing for Word Representations.”
In: International Conference on Learning Representations. 2018. URL: https : / / openreview . net / forum ? id =
HkuGJ3kCb.
J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. “BERT: Pre-training of Deep Bidirectional Transformers for
Language Understanding.” In: Proceedings of the 2019 Conference of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). Minneapo-
lis, Minnesota: Association for Computational Linguistics, June 2019, pp. 4171–4186. DOI: 10.18653/v1/N19-
1423. URL: https://aclanthology.org/N19-1423.
A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. “Language Models are Unsupervised Multitask
Learners.” In: 2019.
Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov. RoBERTa: A
Robustly Optimized BERT Pretraining Approach. 2019. arXiv:1907.11692 [cs.CL].
J. Gao, D. He, X. Tan, T. Qin, L. Wang, and T. Liu. “Representation Degeneration Problem in Training Natural
Language Generation Models.” In: CoRR abs/1907.12009 (2019). arXiv:1907.12009. URL: http://arxiv.org/abs/
1907.12009.
S. Rajaee and M. T. Pilehvar. “A Cluster-based Approach for Improving Isotropy in Contextual Embedding
Space.” In: Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the
11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers). Online: Associa-
tion for Computational Linguistics, Aug. 2021, pp. 575–584. DOI: 10.18653/v1/2021.acl-short.73. URL: https:
//aclanthology.org/2021.acl-short.73.
A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. Bowman. “GLUE: A Multi-Task Benchmark and Analysis
Platform for Natural Language Understanding.” In: Proceedings of the 2018 EMNLP Workshop BlackboxNLP: An-
alyzing and Interpreting Neural Networks for NLP. Brussels, Belgium: Association for Computational Linguistics,
Nov. 2018, pp. 353–355. DOI: 10.18653/v1/W18-5446. URL: https://aclanthology.org/W18-5446.
A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. “SuperGLUE: A
Stickier Benchmark for General-Purpose Language Understanding Systems.” In: CoRR abs/1905.00537 (2019).
arXiv:1905.00537. URL: http://arxiv.org/abs/1905.00537.




9.

10.

11.

12.

13.

E. Agirre, D. Cer, M. Diab, and A. Gonzalez-Agirre. “SemEval-2012 Task 6: A Pilot on Semantic Textual Similarity.”
In: *SEM 2012: The First Joint Conference on Lexical and Computational Semantics – Volume 1: Proceedings of
the main conference and the shared task, and Volume 2: Proceedings of the Sixth International Workshop on
Semantic Evaluation (SemEval 2012). Montréal, Canada: Association for Computational Linguistics, July 2012,
pp. 385–393. URL: https://aclanthology.org/S12-1051.
E. Agirre, D. Cer, M. Diab, A. Gonzalez-Agirre, and W. Guo. “*SEM 2013 shared task: Semantic Textual Simi-
larity.” In: Second Joint Conference on Lexical and Computational Semantics (*SEM), Volume 1: Proceedings of
the Main Conference and the Shared Task: Semantic Textual Similarity. Atlanta, Georgia, USA: Association for
Computational Linguistics, June 2013, pp. 32–43. URL: https://aclanthology.org/S13-1004.
E. Agirre, C. Banea, C. Cardie, D. Cer, M. Diab, A. Gonzalez-Agirre, W. Guo, R. Mihalcea, G. Rigau, and J. Wiebe.
“SemEval-2014 Task 10: Multilingual Semantic Textual Similarity.” In: Proceedings of the 8th International Work-
shop on Semantic Evaluation (SemEval 2014). Dublin, Ireland: Association for Computational Linguistics, Aug.
2014, pp. 81–91. DOI: 10.3115/v1/S14-2010. URL: https://aclanthology.org/S14-2010.
E. Agirre et al. “SemEval-2015 Task 2: Semantic Textual Similarity, English, Spanish and Pilot on Interpretabil-
ity.” In: Proceedings of the 9th International Workshop on Semantic Evaluation (SemEval 2015). Denver, Colorado:
Association for Computational Linguistics, June 2015, pp. 252–263. DOI: 10.18653/v1/S15-2045. URL: https:
//aclanthology.org/S15-2045.
E. Agirre, C. Banea, D. Cer, M. Diab, A. Gonzalez-Agirre, R. Mihalcea, G. Rigau, and J. Wiebe. “SemEval-2016 Task
1: Semantic Textual Similarity, Monolingual and Cross-Lingual Evaluation.” In: Proceedings of the 10th Interna-
tional Workshop on Semantic Evaluation (SemEval-2016). San Diego, California: Association for Computational
Linguistics, June 2016, pp. 497–511. DOI: 10.18653/v1/S16-1081. URL: https://aclanthology.org/S16-1081.

14. M. Marelli, S. Menini, M. Baroni, L. Bentivogli, R. Bernardi, and R. Zamparelli. “A SICK cure for the evaluation of

15.

compositional distributional semantic models.” In: LREC. 2014.
S. Ravfogel, Y. Elazar, J. Goldberger, and Y. Goldberg. “Unsupervised Distillation of Syntactic Information from
Contextualized Word Representations.” In: Proceedings of the Third BlackboxNLP Workshop on Analyzing and
Interpreting Neural Networks for NLP. Online: Association for Computational Linguistics, Nov. 2020, pp. 91–
106. DOI: 10.18653/v1/2020.blackboxnlp-1.9. URL: https://aclanthology.org/2020.blackboxnlp-1.9.

16. G. A. Miller, C. Leacock, R. Tengi, and R. T. Bunker. “A Semantic Concordance.” In: Human Language Technology:
Proceedings of a Workshop Held at Plainsboro, New Jersey, March 21-24, 1993. 1993. URL: https://aclanthology.
org/H93-1061.

---
**Source PDF:** `467dde029d3a.pdf` (2022_12_article.pdf)  
**URL:** https://zenodo.org/record/6574649/files/article.pdf
