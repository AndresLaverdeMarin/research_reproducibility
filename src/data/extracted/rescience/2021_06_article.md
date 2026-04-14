R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Reproducing Learning to Deceive With
Attention-Based Explanations

Rahel Habacker1, ID , Andrew Harrison1„ ID , Mathias Parisot1„ ID , and Ard Snijders1„ ID
1University of Amsterdam, Amsterdam, The Netherlands

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
10.5281/zenodo.4834146

Reproducibility Summary

Scope of Reproducibility

Based on the intuition that attention in neural networks is what the model focuses on, at-
tention is now being used as an explanation for a modelsʼ prediction (see Galassi, Lippi,
and Torroni1 for a survey). Pruthi et al.2 challenge the usage of attention-based expla-
nation through a series of experiments using classification and sequence-to-sequence
(seq2seq) models. They examine the modelʼs use of impermissible tokens, which are
user-defined tokens that can introduce bias e.g. gendered pronouns. Across multiple
datasets, the authors show that with the impermissible tokens removed the model accu-
racy drops, implying their usage in prediction. And then by penalising attention paid
to the impermissible tokens but keeping them in, they train models that retain full ac-
curacy hence must be using the impermissible tokens, but that does not show attention
being paid to the impermissible tokens. As the paperʼs claims have such significant
implications for the use of attention-based explanations, we seek to reproduce their re-
sults.

Methodology

Using the authorsʼ code, for classifiers we attempt to reproduce their embedding, BiL-
STM, and BERT results across the occupation prediction, gender identify, and SST + wiki
datasets. Further, we reimplemented BERT using HuggingFaceʼs transformer library [3]
with restricted self-attention (information cannot flow between permissible and imper-
missible tokens). For seq2seq we used the authorsʼ code to reproduce results across
Bigram Flip, Sequence Copy, Sequence Reverse, and English-German (En-De) machine
translation datasets. We performed refactoring on the authorsʼ code aiming toward a
more uniformly usable code style as well as porting across to PyTorch Lightning. All ex-
periments were run in approximately 130 GPU hours on a computing cluster with nodes
containing Titan RTX GPUs.

Results

We reproduced the authorsʼ results across all models and all available datasets, confirm-
ing their findings that attention-based explanations can be manipulated and that mod-


Code is available at https://github.com/MatPrst/deceptive-attention-reproduced – DOI 10.5281/zenodo.4692668..
Data is available at https://github.com/MatPrst/deceptive-attention-reproduced/tree/main/deceptive-attention/src/classiﬁcation/data – DOI
10.5281/zenodo.4686793.
Open peer review is available at https://openreview.net/forum?id=-rn9m0Gt6AQ.




els can learn to deceive. We also replicated their BERT results using our reimplemented
model. There was only one result not as strongly (> 1 S.D.) in their experimental direc-
tion.

What Was Easy

The authorsʼ methods were largely well described and easy to follow, and we could
quickly produce the first results as their code worked straightaway with minor adjust-
ments. They were also extremely responsive and helpful via email.

What Was Difﬁcult

Re-implementing the BERT-based classification model to perform replicability, with fur-
ther specification details on model architecture, penalty mechanism, and training pro-
cedure needed. Also, porting code across to PyTorch Lightning.

Communication With Original Authors

There was a continuous email chain with the authors for several weeks during the re-
producibility work. They made additional code and datasets available per our requests,
along with providing detailed responses and clarifications to our emailed questions.
They encouraged the work and we wish to thank them for their time and support.

## 1 Introduction

Attention is a mechanism to automatically learn the relevance of different elements of
the input to a model, rather than relying on manual feature engineering, allowing com-
putational learning to focus on important elements [1]. Originally introduced to nat-
ural language processing (NLP) for neural machine translation [4] its usage has since
expanded. Vaswani et al.5 termed it ”all you need”, having removed recurrence and
convolutions and relied on attention in their Transformer architecture. Transformers
are now in wide use, with Devlin et al.6ʼs Bidirectional Encoder Representations from
Transformers (BERT) a commonly used model in NLP.
Because neural networks are subsymbolic with knowledge stored numerically, it is chal-
lenging to understand their inner workings [1]. With interpretability a growing concern
in NLP, there is a body of work on attention-based explanations of neural architectures
using visualisation of attention weights [7]. However, there is a rich and ongoing de-
bate about whether attention is an explanation or not [8, 9]. Acknowledging the debate,
Pruthi et al.2 whose work we seek to reproduce, examine whether models can learn to
deceive, by adding a penalty to the loss function that punishes the model when attention
is paid to impermissible tokens. These tokens are user-defined and may refer inter alia
to terms for protected traits such as gender (the pronouns she, her etc.), sexual orienta-
tion, or race. Their research indicates that the impermissible tokens are still being used
by the model as there is no accuracy drop seen, while there is one when these tokens
are instead fully removed. Thus, the model is both able to use the impermissible tokens
in learning and inference, but not pay attention to them. Hence bringing into question
the validity of using attention in the explanation of a modelʼs decision.

## 2 Scope of Reproducibility

The core finding of the paper is that attention-based explanations of models can be de-
ceptive by, for instance, hiding the modelʼs use of gendered pronouns at inference from
an auditor. Specifically, the authors show that attention weights can be manipulated




during training by penalising the allocation of attention to impermissible tokens, with-
out this affecting model performance. Any resulting attention-based explanation might
suggest that the model did not rely on impermissible tokens to make its predictions,
when in reality the model still uses these but not through the attention mechanism,
thereby making the model “deceptive”. The key findings can be decomposed into the
following claims which we are testing in our research:

1. The attention mass on impermissible tokens can be reduced without significantly
affecting the classification accuracy of Embeddings + Attention, BiLSTM + Atten-
tion, and BERT + Attention models across several tasks (see Tables 3 and 4).

2. The attention mass on impermissible tokens can be reduced without significantly
affecting the seq2seq performance on translation as measured by BLEU (see Table
7).

3. The attention mass on impermissible tokens can be reduced without significantly

affecting the seq2seq accuracy on synthetic data tasks (see Tables 5 and 6).

We chose not to perform the human study, testing whether visualised attention weights
could deceive NLP/ML trained and Transformer knowledgeable participants, as we deemed
that the small sample size does not add value to the results.

## 3 Methodology

Initially, we attempted to reproduce the findings from the provided repository with-
out contacting the authors. The authors use three classification models: embeddings
with attention; BiLSTM with attention; and a BERT-based model with attention. For the
seq2seq tasks, the model is an encoder-decoder architecture. Code for all models (ex-
cept BERT) was available in the authorsʼ repository, and aside from minor dependency
issues in the environment file, we were able to successfully run experiments to repro-
duce the results. We re-implemented the BERT-based model to replicate their results,
and after the BERT-based code was added to the repository, we also reproduced their
results. Lastly, we refactored the existing code-base and ported the PyTorch-based code
to PyTorch Lightning.

### 3.1 Attention Manipulation

To explicitly optimise the models to learn deceptive attention weights, the authors intro-
duce an auxiliary loss component that penalises the model for attending to impermis-
sible tokens. Impermissible tokens are user-defined from a corpus and are the set of
words I that a model should not use during training or inference, as they might intro-
duce bias or other ethical issues. An example is the use of gendered pronouns ”her, she,
Ms.” which might lead a model to discriminate against a specific gender. The remaining
words in the corpus are deemed permissible, and thus constitute the complement set
I c. Assuming an input sequence S = w1, w2, ..., wn of n tokens, the authors proceed to
define a binary attention mask vector m of length |S|, with each element denoting the
occurrence of an impermissible token:

{

mi =

1,


if wi ∈ I
otherwise

Furthermore, we assume an attention vector α ∈ [0, 1]n which denotes the allocated
attention for each token in the input sequence. From this, the authors construct the
additive task-agnostic penalty term R, such that L′ = L+R, where R captures the extent




to which a modelʼs attention layer is penalised for allocating attention to impermissible
tokens:

R = −λ log(1 − αT m)
Here, the αT m term denotes the attention allocated to impermissible words. Taking the
negative log of the complement of this term then allows us to minimise this quantity via
standard gradient descent. Furthermore, λ is a coefficient that is used to control the
extent to which impermissible attention allocation is penalised. Following the authorsʼ
methods, we consider values for λ = {0, 0.1, 1.0}. For models featuring multi-head at-
tention (such as BERT), the authors use two different penalty variants. Namely, Rmean
optimises the mean of the penalty over the set of all heads H, while Rmax instead only
considers the head which allocates the most attention to impermissible tokens:

Rmean = − λ
|H|

∑

h∈H

log(1 − αT

h m),

Rmax = −λ · min
h∈H

log(1 − αT

h m)

Note that for the multi-head penalties, only the heads from the modelʼs last layer are
considered, thus in BERT α is defined as the attention paid by the [CLS] token to the
other tokens.

### 3.2 Model Descriptions

Embedding + Attention This model serves as a baseline to the other models used for
classification. It contains between 2.7M and 6.5M parameters depending on the dataset
and consists of a dot-product attention mechanism applied on word embeddings. The
resulting attention vector is then passed into a linear classifier followed by a softmax
activation. The size of the embedding in the original paper was 128. We use cross-
entropy loss and the Adam optimizer with a learning rate of 0.001 and no weight de-
cay. Pruthi et al.2 argue that the accuracy of the Embedding and BiLSTM models could
have been greatly impacted by the lambda parameter because those models might be
under-parameterised for the SST-Wiki dataset. To study this we also train models with
embedding sizes of 256 and 512.
BiLSTM + Attention The model still uses word embeddings and consists of a dot-product
attention mechanism applied on the output of a bidirectional LSTM [10]. The resulting
attention vector is then passed into a linear classifier followed by a softmax activation.
Again, the size of the embedding is 128, but we also train models with embedding sizes
of 256 and 512. Its number of parameters is between 2.8M and 6.6M parameters depend-
ing on the size of the vocabulary of the given dataset. The BiLSTM was trained using the
same hyper-parameters as the Embedding model above, with the dimension of the hid-
den state being 64.
Transformer Models For the transformer-based architecture, we use BERT [6]. Specif-
ically, we use a pre-trained instance of the uncased BERT base model, which consists
of 12 transformer blocks (each with 12 heads) amounting to 109M trainable parameters.
We trained each model for 10 epochs, with a batch size of 32. All models were opti-
mised using Adam, with a learning rate of 5e−5. Furthermore, we applied dropout with
p = 0.3 to improve model generalisation. A sequence classification layer is added on
top of the architecture, to adapt the model for sentence classification. Following the au-
thorsʼ methods, we apply a self-attention mask M to the self-attention probabilities via
element-wise multiplication in the modelsʼ forward pass, to avoid information flowing
between the sets of impermissible tokens I and permissible tokens I c. Specifically, M
is a binary matrix of size n × n, where n denotes the sequence length, and where ele-
ments Mp,q are 1 if both tokens wp and wq belong to the same set (either I or I c), and
0 otherwise. Moreover, the first column of M , which denotes the extent to which all
other tokens attend to the [CLS] token, is zero also, as this further restricts the flow of
information between tokens from I and I c via the [CLS] token.




Task Type

Dataset

Examples

Train

Classification Occupation Pred.

Seq-to-Seq

Gender Identity
SST + Wiki


Sequence Copy
Sequence Reverse
En-De Translation

25185
11271
9613

300000
300000
300000
31016

17629
9017
6920


29001

Val

2519
1127


Test

Label Dist.

5037
1127
1821

68-32
50-50
48-52


1015


1000

-
-
-
-

Table 1. Details of datasets.

Seq2seq Pruthi et al.2 provide a bidirectional and unidirectional Gated Recurrent Unit
(GRU) with dot-product attention respectively for their encoder-decoder model tackling
seq2seq tasks. The input is passed through the encoder and decoder, where the final
hidden state from the bidirectional GRU fed through a linear layer is the initial hidden
state to the decoder. The embedding size was 256 and hidden size 512 for both encoder
and decoder. We also use a teacher forcing ratio of 0.5 as well as the top-1 greedy strategy
for decoding output sequences. For baseline experiments, this model is also trained
with no attention and uniform attention overall source tokens. It overall contains 8.7M
parameters for the synthetic datasets and 48.55M parameters for the Multi30K dataset,
which are both described in Section 3.3.

### 3.3 Datasets

The original work features 8 tasks with associated datasets. For the classification models,
these are Occupational Prediction, Gender Identity, SST + Wiki, and Reference Letters.
For the seq2seq experiments, three synthetic datasets were used; Bigram Flip, Sequence
Copy, and Sequence Reverse tasks. Additionally, the Multi30K dataset [11] was used for
English to German machine translation (MT). All of the datasets were available in the
authorsʼ repository except for Reference Letters, with the authors citing privacy con-
cerns. Consequently, we were not able to reproduce this experiment. For Occupation
Prediction the authors state that downsampling by a factor of 10 was done for minority
classes. As it was not clear from the data provided in the repository if downsampling
had already been applied, the authors confirmed via email that this was the case. No
further pre-processing was required, besides that already present in the authorsʼ code.
Details of the datasets used in our experiments are provided in Table 1.

### 3.4 Hyperparameters

Except for the λ coefficient (values 0.0, 0.1, and 1.0) as used in the computation of the
regularising component R, the original work did not provide details regarding hyper-
parameters and/or tuning thereof. Upon contacting the authors, we learned that no
hyperparameter tuning was performed, as the experimental findings could be achieved
with conventional parameters. Therefore, in reproducing their experiments we have
used the same standard configurations as the authors.

### 3.5 Experimental Setup and Code

The code used to reproduce the experiments can be found in this Github repository1.
The authorsʼ negative baseline, the first row of each model in Table 3 of the original
paper, was produced by removing the impermissible tokens (anonymising or deleting).

1https://github.com/MatPrst/FACT




They show that the performance of the model dropped. This drop was in comparison
to the true baseline in row two, which provides the modelsʼ performance when imper-
missible words are freely used with no manipulation penalty applied i.e. λ = 0.0. The
third and fourth rows provide results for adjusting the penalty coefficient to 0.1 and
1.0 respectively. To reproduce the experiments by anonymising or removing the imper-
missible tokens, we had to look deeper into their script. For the Occupation Prediction
and Gender Identity datasets, the authors provided an anonymisation functionality that
transformed all pronouns to gender-neutral ones. However, for the SST + Wiki dataset,
we had to implement the functionality to remove the SST sentence because it was not
present in the scripts. Similarly, we added the functionality to the training script for the
provided BERT implementation.
The repository contained a bash script to run the experiments with Embedding + At-
tention and BiLSTM + Attention without removing or anonymising the impermissible
tokens. We recreated the classification experiments using the seed values from this
script. The training outputs of those experiments were not as presented in the README
of the authorsʼ repository and did not contain a clear attention mass value. However, the
authors clarified that the “attention ratio” measure was used in the paper. From those
experimental runs, we could determine the average and standard deviation of the five
runs.
For the classification models, we chose to largely follow the authorsʼ experimental setup:
we run experiments with the same set of values for the loss coefficient λ ∈ 0, 0.1, 1.0.
Furthermore, all models are trained for 10 epochs and are evaluated on the development
set after each epoch. Here, we measure two metrics; the validation accuracy, and the
average attention mass over all examples. The model with λ = 0 serves as the baseline
for the ʼadversarialʼ models with λ = 0.1, 1.0, i.e. the models that are explicitly optimised
to learn deceptive attention maps. For the BERT replication, when evaluating models on
the test set, we follow the authorsʼ heuristic, i.e. we select the checkpoint which is within
2% of the baseline test accuracy, and which has the greatest reduction in attention mass
on the validation set.
As per the authorsʼ experimental setup we considered the four sequence-to-sequence
tasks: Bigram Flipping, Sequence Copying, and Sequence Reversal are synthetic tasks
that work with input-output-mappings with the respective gold alignments considered
as impermissible tokens. The models are trained on 100K random input sequences with
length 32 from a vocabulary of 1000 tokens and validated and tested on 100K unseen
random sequences. Machine translation from German to English acts as the fourth task
for which gold alignments are not available. Thus, the Fast Align toolkit [12] was used
by the authors to align target and source words. In this task, the aligned words are used
as impermissible tokens.
The seq2seq experimental results in Table 4 of the original paper provide the averaged
value over five runs. The different runs and their results were not available in the repos-
itory, however, after emailing the authors we were provided with the results for each of
the five experimental runs in each condition, along with the seeds used. This allowed
us to recreate the experiment using the same seeds, and to determine along with the
average, whether the standard deviation between our results also matched.
Pertaining to the English to German translations, the BLEU score was used, however,
this was not available in the repository. After contacting the authors, we were provided
with a link to the BLEU library they had used which is called “compare-mt” [13]. We had
meanwhile used the NLTK implementation [14], presuming it to be the most likely used.
Therefore, for translation, we have used two different BLEU implementations: compare-
mt for reproduction and NLTK for replication.




Classification

GPU Hours

Model

Batch size Occupation Pred. Gender Identity

SST + Wiki


BERT
BERT(HF)


Seq-to-Seq

0.62
0.94
3.1
4.8

0.56

1.5
1.9

GPU Hours

1.1
1.3
1.2
### 2.5 Model

Batch size


Seq. Copy

Seq. Reverse En-De

Enc-Dec


0.42

0.36

0.34

0.15

Table 2. Breakdown of approximate computational requirements for running experiments per task,
for a single seed.

### 3.6 Computational Requirements

All experiments were run on the LISA computing cluster provided by SURFsara, which
is available to University of Amsterdam Master students. The nodes used contained 4 x
Titan RTX GPUs. A breakdown of the computation is provided in Table 2.

## 4 Reproduction and Replication Results

### 4.1 Classiﬁcation

For the classification results, see Tables 3 and 4. As can be observed, our results support
claim 1, and we were able to reproduce the results from Table 3 in the original paper (ex-
cluding the Reference Letters dataset). Furthermore, we replicated the BERT(max) and
BERT(mean) results using our implementation. While the results for the BERT repli-
cation match the authorsʼ findings closely, there are also some noticeable differences;
particularly, for the SST+WIKI task, we can see that for both the mean and max models
for λ = 1.0, the replication of BERT does not manage to retain its performance, with a
drop in accuracy of 4 and 6 percent, respectively.

4.2 Seq2seq

The results in Tables 5, 6 and 7 support claims 2-3, and we were able to reproduce the re-
sults from Table 4 in the original paper. Especially the reported mean accuracy by Pruthi
et al.2 shows no significant difference to our reported values for all seq2seq tasks except
for the baseline experiments with uniform and no attention for the tasks sequence copy
and sequence reverse. Both have a mean difference of 3-14 % accuracy regarding the
authorsʼ accuracies. Pruthi et al.2 did not report accuracies for the translation task in
their original paper, but they provided us with additional raw data which also contained
the accuracy scores from their experiments. Therefore we also compare accuracies for
the En-De MT task.




Model


BERT


BERT


λ

I

X

Occupation Prediction
Accuracy 
93.8 ||| 93.4
0.0
0.0 ✓ 96.3 ||| 96.5
0.1 ✓ 96.2 ||| 96.3
1.0 ✓ 96.2 ||| 96.1
93.3 ||| 93.6
0.0
0.0 ✓ 96.4 ||| 96.7
0.1 ✓ 96.4 ||| 96.6
1.0 ✓ 96.7 ||| 96.5 < 10−2 ||| 0.015

-
51.4 ||| 56.4
4.6 ||| 5.70
1.3 ||| 1.50

-
50.3 ||| 44.1
0.08 ||| 3.70

X

X

95.0 ||| 95.8
0.0
0.0 ✓ 97.2 ||| 97.1
0.1 ✓ 97.2 ||| 97.3
1.0 ✓ 97.2 ||| 97.3 < 10−3 ||| 0.0007

-
13.9 ||| 9.10
0.001 ||| 0.007

X

95.0 ||| 95.8
0.0
0.0 ✓ 97.2 ||| 97.1
0.1 ✓ 97.1 ||| 97.1 < 10−3 ||| 0.007
1.0 ✓ 97.4 ||| 97.2 < 10−3 ||| 0.0008

-
99.7 ||| 65.5

X

95.0 ||| 95.2
-
0.0
13.9 ||| 23.16
0.0 ✓ 97.2 ||| 97.1
0.1 ✓ 97.2 ||| 96.8
0.001 ||| 0.006
1.0 ✓ 97.2 ||| 97.1 < 10−3 ||| 0.002

X

95.0 ||| 95.2
0.0
-
99.7 ||| 66, 88
0.0 ✓ 97.2 ||| 97.2
0.1 ✓ 97.1 ||| 97.0 < 10−3 ||| 0.003
1.0 ✓ 97.4 ||| 97.0 < 10−3 ||| 0.001

Gender Identity


-
99.2 ||| 90.1
3.4 ||| 8.8
0.8 ||| 4.6

-
96.8 ||| 95.5
< 10−6 ||| 0.07
< 10−6 ||| 0.0047


66.8 ||| 71.0

99.4 ||| 99.9
99.2 ||| 99.5
63.3 ||| 71.1


72.8 ||| 82.3
-

80.8 ||| 55.1
< 10−3 ||| 0.004
99.9 ||| 99.9
99.9 ||| 99.9 < 10−3 ||| 0.0003
72.8 ||| 82.3
-
99.7 ||| 99.8

< 10−3 ||| 0.003
99.9 ||| 99.9
99.8 ||| 99.9 < 10−4 ||| 0.0005
72.8 ||| 81.2

99.9 ||| 99.9
99.9 ||| 99.8
72.8 ||| 81.24

99.9 ||| 99.8
99.8 ||| 99.9

-
99.7 ||| 93.7
< 10−3 ||| 0.006
< 10−4 ||| 0.001

-
80.8 ||| 57.6
< 10−3 ||| 0.001
< 10−3 ||| 0.001

Table 3. Classification results from Table 3 in Pruthi et al.2 for datasets Occupation Prediction
and Gender Identity with cell scheme author | reproduced for all models except BERT(HgFc) which
follows cell scheme author | replicated. Our values are means over 5 different seeds.




Model


BERT


BERT


λ

I

X

-
48.4 ||| 49.9
36.4 ||| 16.9
8.70 ||| 12.9

SST + Wiki
Accuracy 
48.9 ||| 49.3
0.0
0.0 ✓ 70.7 ||| 68.1
0.1 ✓ 67.9 ||| 69.5
1.0 ✓ 48.4 ||| 51.8
49.1 ||| 48.9
0.0
0.0 ✓ 76.9 ||| 75.9
0.1 ✓ 60.6 ||| 65.1
1.0 ✓ 61.0 ||| 64.9
50.4 ||| 50.2
-
0.0
59.0 ||| 17.4
0.0 ✓ 90.8 ||| 91.8
< 10−2 ||| 0.04
0.1 ✓ 90.9 ||| 91.5
1.0 ✓ 90.6 ||| 91.9 < 10−3 ||| 0.005

-
77.7 ||| 81.5
0.04 ||| 0.99
0.07 ||| 0.035

X

X

X

50.4 ||| 50.2
0.0
-
0.0 ✓ 90.8 ||| 91.8
96.2 ||| 67.4
< 10−2 ||| 0.04
0.1 ✓ 90.7 ||| 91.9
1.0 ✓ 90.2 ||| 91.8 < 10−3 ||| 0.003

X

50.4 ||| 52.8
0.0
0.0 ✓ 90.8 ||| 91.2
0.1 ✓ 90.9 ||| 90.7 < 10−2 ||| 0.018
1.0 ✓ 90.6 ||| 85.4 < 10−3 ||| 0.019

-
59.0 ||| 68.66

X

50.4 ||| 52.8
0.0
0.0 ✓ 90.8 ||| 91.1
0.1 ✓ 90.7 ||| 89.8 < 10−2 ||| 0.007
1.0 ✓ 90.2 ||| 86.0 < 10−3 ||| 0.0007

-
96.2 ||| 93.94

Table 4. Classification results from Table 3 in Pruthi et al.2 for dataset SST + Wiki with cell scheme
author | reproduced for all models except BERT(HgFc) which follows cell scheme author | replicated.
Our values are means over 5 different seeds.


None


λ

0.0

0.0
0.0

0.1
### 1.0 Accuracy 

97.8 ||| 95.1
96.4 ||| 96.4
99.9 ||| 100
99.8 ||| 99.6

94.5 ||| 93.9
5.2 ||| 4.71
-
24.4 ||| 15.2
0.03 ||| 0.01

Sequence Copy


99.9 ||| 100
93.8 ||| 79.3
84.1 ||| 87.3
100.0 ||| 100
92.9 ||| 99.9


98.8 ||| 94.1
5.2 ||| 4.73
-
27.3 ||| 10.7
0.02 ||| 0.014

Table 5. Results for Seq2seq synthetic data tasks Bigram Flip and Sequence Copy from Table 4 in
Pruthi et al.2 with cell scheme author | reproduced. All values are means over 5 different seeds.
Standard deviations are presented in Tables 10 and 11 of the Appendix.





None


λ

0.0

0.0
0.0

0.1
### 1.0 Sequence Reverse


100.0 ||| 100
88.1 ||| 80.8
84.1 ||| 87.2

99.8 ||| 99.9


94.1 ||| 94.0
4.7 ||| 7.74
-
27.6 ||| 16.3
0.01 ||| 0.014

Table 6. Results for Seq2seq synthetic task Sequence Reverse from Table 4 in Pruthi et al.2 with cell
scheme author | reproduced. All values are means over 5 different seeds. Standard deviations are
presented in Tables 10 and 11 of the Appendix.


None


λ

0.0

0.0
0.0

0.1
1.0

### 24.89 BLEU (C-MT) BLEU (NLTK)
24.42 ||| 24.89
18.49 ||| 18.37
14.89 ||| 15.88
23.69 ||| 24.30
20.66 ||| 21.07

18.37
15.88

24.30
21.07


36.99 ||| 36.75
32.31 ||| 31.76
29.73 ||| 30.36
36.28 ||| 36.49
33.82 ||| 33.68


20.66 ||| 24.52
5.96 ||| 5.96
-
7.02 ||| 16.77
1.16 ||| 1.40

Table 7. Reproductions (means over 5 different seeds) En-De MT tasks from Table 4 in Pruthi et al.2
with cell scheme author | reproduced. The BLEU(NLTK) values are not contained in the original
paper, thus replicated. Standard deviations are presented in Table 12 of the Appendix.

## 5 Results Beyond Original Paper

The authors state that their seq2seq results in Table 4 of the original paper are based on
the average of 5 different seeds. Additional to their work we have examined the standard
deviations alongside the average for all the results, comparing their results and ours.
Further, while the authors do not state whether classification results from Table 3 in
their original paper are based on the average of 5 seeds, we have again completed 5 runs
of the experiments and provided the average.

### 5.1 Under-Parameterised Models

In the original paper, the classification results for the Embedding and BiLSTM mod-
els for the task on SST+Wiki are outliers because, while the attention mass over the
impermissible tokens decreases as λ increases, the test accuracy also decreases signif-
icantly. The authors speculate that this behavior is due to the models being under-
parameterised. We investigated this by training Embedding and BiLSTM models with
larger embedding dimensions. In particular, we compared embedding sizes of 128 (orig-
inal size), 256, and 512. The results are presented in Tables 8 and 9. Increasing the di-
mensionality of the embedding does not seem to prevent the accuracy from dropping
for larger values of λ. We speculate that the drop in accuracy is due to the way the imper-
missible tokens are defined for the SST+Wiki dataset. All the words belonging to the SST
sentence are labeled as impermissible and will therefore be penalised by the auxiliary
loss component. Because the Wikipedia sentence does not provide useful information
for the sentiment prediction, the model cannot rely on it and the accuracy reduces as the
penalty term increases. This behaviour does not occur for the other datasets because
only a few impermissible tokens were selected for the experiments, allowing the model
to find other proxy tokens carrying information about the respective classification tasks.
For example, words such as ”lesbian” or gendered names such as ”Mark” were not la-




beled as impermissible in the Occupation Prediction dataset. An alternative experiment
could have been to define the impermissible tokens of the SST+Wiki dataset as the words
in the SST sentence with the strongest positive or negative sentiment scores.

Model

λ

I


0.0
0.1
1.0

0.0
0.1
### 1.0 Embedding dimension


51.8 ± 3.2
41.4 ± 2.3
11.1 ± 2.2
76.8 ± 2.4
3.5 ± 1.9
0.13 ± 0.9


68.1 ± 2.4
68.3 ± 0.76
51.8 ± 2
76.2 ± 2.8
62.3 ± 4.1
57.3 ± 1.5

Table 9. Influence of the embedding size for Embedding and BiLSTM models on the SST + Wiki
dataset. The values reported are the means over 5 different seeds and the standard deviations.

## 6 Discussion

Our results reproduce Pruthi et al.2ʼs finding that models can learn to deceive. Jain and
Wallace8 note that for attention to be an explanation, a different configuration of atten-
tion weights for the same piece of text should lead to different predictions. The research
which we have reproduced implies that the same accuracy (hence prediction) can be
maintained while explicitly changing the configuration of attention weights. The impli-
cations are clear; either it is providing further evidence for why attention should not
be thought of as an explanation, supporting Serrano and Smith7ʼs findings that atten-
tion weights can be largely zeroed out without affecting accuracy. Or, if attention is an
explanation, then models can be still be trained to change the attention-based explana-
tion given and deceive algorithmic audit. This research thus provides a new vein of the
investigation into the attention-based explanation debate.
Examination of the standard deviations showed whether reproduction differences were
meaningful for seq2seq tasks. Regarding synthetic data, it showed some variance from
the authorsʼ values for attention mass, but it was more strongly in the experimental
direction, thus supporting their findings. For machine translation, one result at λ = 0.1
for attention mass was not as strong as their result, but still trending in the experimental
direction. While the standard deviation does show that there is some variance inherent
in the reduced attention masses under manipulation, it provides still further robustness

Model

λ

I


0.0
0.1
1.0

0.0
0.1
### 1.0 Embedding dimension

128 (original size)
Accuracy 
68.1 ± 1.6
69.5 ± 1.4
51.8 ± 1.1
76.4 ± 0.8
65.1 ± 4
64.9 ± 3.1

49.9 ± 2.2
17 ± 1
12.9 ± 2
81.5 ± 7.5
0.99 ± 1.3
0.035 ± 0.02


Accuracy 
69.1 ± 2
69.1 ± 1.6
51 ± 0.84
76 ± 2.7
65.4 ± 4.7
62.1 ± 2.5

50 ± 1.1
40.3 ± 0.48
12.3 ± 1.4
85.5 ± 3
0.94 ± 0.8
0.11 ± 0.09

Table 8. Influence of the embedding size for Embedding and BiLSTM models on the SST + Wiki
dataset. The values reported are the means over 5 different seeds and the standard deviations.




to the findings.
Finally, we obtain very similar results with our replication of the authorsʼ BERT-based
classification model, for both the mean and max penalties, for the majority of the tasks.
The only results which we did not manage to exactly replicate concern the test accura-
cies for SST+Wiki. However, given that we did manage to reproduce these results with
the authorsʼ implementation of BERT, it is more likely that the differences in test accu-
racies between the reproduction and replication experiments can be attributed to slight
differences in hyperparameter settings between the two - however, further investiga-
tion would be required to confirm this. Further to this, we observe somewhat large
differences between the attention masses - particularly for values where λ = 0. How-
ever, given that similar differences persist also for our reproduction results of BERT, it
may be the case that these quantities are simply more susceptible to stochasticity and/or
training dynamics, which would then explain the observed discrepancies with the au-
thorsʼ findings. Either way, these particular differences do not provide grounds to reject
the authorsʼ hypotheses; we still observe that for most replication runs, the accuracy is
not impacted despite substantial reductions in attention masses on the impermissible
tokens. To this end, our replication efforts provide further evidence for the authorsʼ
claims that attention-as-explanation can be deceptive.

### 6.1 What Was Easy

Overall, we could easily understand and follow the authorsʼ descriptions of their meth-
ods in the paper. An example of this is the way seq2seq tasks and the datasets used
were described in a short but comprehensive way. The provided bash scripts revealed
the basic setup and could almost immediately be used to run the experiments on our
infrastructure described in Section 3.6. Therefore, we were quickly able to reproduce
the first results. The codebase for seq2seq tasks was easily restructured into functions,
instead of keeping the train and evaluation functionality at a global code level. Besides
this, applying PEP8 to the codebase was an easy task - another positive is that restructur-
ing did not break the code massively at any point, which in our opinion testifies to an
already consistent architecture. The authorsʼ integration of the BLUE score implemen-
tation (compare-mt) was missing. However, we could easily add the NLTK BLEU score
implementation into the code. We could further observe robust BLEU score results, like
the ones we reproduced and replicated turned out to be not significantly different from
those reported by the authors.

### 6.2 What Was Difﬁcult

To a certain extent, it was achievable to re-implement the BERT-based model using
only the information provided in the original work. Nevertheless, in the process of re-
implementing, several ambiguities arose that we were initially unable to resolve and
which had to be clarified by the authors. For instance, the penalty mechanism used to
compute R by default assumed an attention vector α, while BERT, by default, outputs
self-attention matrices. We were initially unsure how to obtain a vector from this ma-
trix; only after contacting the authors, we learned that α can be obtained from BERTʼs
self-attention matrices by only considering the first row of the matrix (for a given self-
attention head), which represents the extent to which the [CLS] token attends to all
other tokens in the sentence. The authors also further clarified that they only used the
attention output of the last (12th) transformer block of the model, whereas we initially
understood from the paper that all layers should be taken into account.
Additionally, there was some brief confusion relating to the evaluation procedure. In
their papersʼ Section 5.1, the authors provide a heuristic to “pick” the best deceptive
model. Based on how this procedure was formulated, we initially believed that multiple
models were trained for a given epoch sequentially, after which the best model (as eval-
uated by admissible accuracy and largest reduction in attention mass) was selected for




the next epoch. However, after corresponding with the authors, we learned that rather,
a single model is simply trained for 10 epochs, and only then the selection heuristic is
applied manually to determine which model checkpoint will be used for evaluation on
the test set. In these respects, replicating the model architecture, penalty mechanism,
and training procedure might have been easier, had the original work been more precise
and explicit regarding its methods.
We also chose to port the code to PyTorch Lightning to make it easier to reproduce the
research in the future, but this necessitated changes to data loading, pre-processing, and
batching. A specific challenge was PyTorch lightning not yet supporting checkpointing
over multiple metrics out-of-the-box, meaning we had to implement the authorsʼ multi-
metric heuristic ourselves.

### 6.3 Communication With Original Authors

Following our initial contact email, the authors made themselves readily available, quickly
responding to a series of emails over multiple weeks, answering all questions clearly,
and providing access to everything we required to reproduce their results. We have also
provided the authors with this full report.




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

10.

11.

12.

A. Galassi, M. Lippi, and P. Torroni. “Attention in natural language processing.” In: IEEE Transactions on Neural
Networks and Learning Systems (2020).
D. Pruthi, M. Gupta, B. Dhingra, G. Neubig, and Z. C. Lipton. “Learning to Deceive with Attention-Based Explana-
tions.” In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. Online:
Association for Computational Linguistics, July 2020, pp. 4782–4793. DOI: 10.18653/v1/2020.acl-main.432.
URL: https://www.aclweb.org/anthology/2020.acl-main.432.
T. Wolf et al. “HuggingFace’s Transformers: State-of-the-art Natural Language Processing.” In: CoRR
abs/1910.03771 (2019). arXiv:1910.03771. URL: http://arxiv.org/abs/1910.03771.
D. Bahdanau, K. Cho, and Y. Bengio. “Neural machine translation by jointly learning to align and translate.” In:
arXiv preprint arXiv:1409.0473 (2014).
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. “
is all you need.” In: arXiv preprint arXiv:1706.03762 (2017).
J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. “Bert: Pre-training of deep bidirectional transformers for
language understanding.” In: arXiv preprint arXiv:1810.04805 (2018).
S. Serrano and N. A. Smith. “Is Attention Interpretable?” In: Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics. 2019, pp. 2931–2951.
S. Jain and B. C. Wallace. “Attention is not Explanation.” In: Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies, Vol-
ume 1 (Long and Short Papers). 2019, pp. 3543–3556.
S. Wiegreffe and Y. Pinter. “Attention is not not Explanation.” In: Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP). 2019, pp. 11–20.
A. Graves and J. Schmidhuber. “Framewise phoneme classiﬁcation with bidirectional LSTM networks.” In: Pro-
ceedings. 2005 IEEE International Joint Conference on Neural Networks, 2005. Vol. 4. 2005, 2047–2052 vol.
4. DOI: 10.1109/IJCNN.2005.1556215.
D. Elliott, S. Frank, K. Sima’an, and L. Specia. Multi30K: Multilingual English-German Image Descriptions.
2016. arXiv:1605.00459 [cs.CL].
C. Dyer, V. Chahuneau, and N. A. Smith. “A Simple, Fast, and Effective Reparameterization of IBM Model 2.”
In: Proceedings of the 2013 Conference of the North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies. Atlanta, Georgia: Association for Computational Linguis-
tics, June 2013, pp. 644–648. URL: https://www.aclweb.org/anthology/N13-1073.

13. G. Neubig, Z.-Y. Dou, J. Hu, P. Michel, D. Pruthi, and X. Wang. “compare-mt: A Tool for Holistic Comparison of
Language Generation Systems.” In: Proceedings of the 2019 Conference of the North American Chapter of
the Association for Computational Linguistics (Demonstrations). Minneapolis, Minnesota: Association for
Computational Linguistics, June 2019, pp. 35–41. DOI: 10.18653/v1/N19-4007. URL: https://www.aclweb.org/
anthology/N19-4007.
S. Bird, E. Klein, and E. Loper. Natural Language Processing with Python: Analyzing Text with the Natural
Language Toolkit. Beijing: O’Reilly, 2009. DOI: http://my.safaribooksonline.com/9780596516499. URL: http :
//www.nltk.org/book.

14.




A Appendix


None


λ

0.0

0.0
0.0

0.1
### 1.0 Sequence Copy


0.27 ||| 1.90
0.94 ||| 0.95
0.004 ||| 0.00
0.12 ||| 0.67


1.36 ||| 0.21

-
22.6 ||| 7.50
0.04 ||| 0.03


0.004 ||| 0.00
2.52 ||| 4.20
2.91 ||| 6.40

10.5 ||| 0.005


1.06 ||| 0.11

-
9.85 ||| 9.70
0.04 ||| 0.01

Table 10. Reproductions seq2seq synthetic tasks Bigram Flip and Sequence Copy from Table 4 in
Pruthi et al.2 with cell scheme author | reproduced. All values are standard deviations over 5 differ-
ent seeds.


None


λ

0.0

0.0
0.0

0.1
### 1.0 Sequence Reverse
Accuracy 

3.80 ||| 3.40
6.00 ||| 3.40

0.24 ||| 0.04

0.08 ||| 0.13

-
17.7 ||| 10.0
0.01 ||| 0.01

Table 11. Reproductions seq2seq synthetic task Sequence Reverse from Table 4 in Pruthi et al.2
with cell scheme author | reproduced. All values are standard deviations over 5 different seeds.


None


λ

0.0

0.0
0.0

0.1
### 1.0 BLEU (C-MT) BLEU (NLTK) Accuracy 

1.14 ||| 0.95
0.87 ||| 0.76
0.68 ||| 1.37
1.01 ||| 1.56
2.25 ||| 0.89

0.95

0.76
1.37

1.56
0.89

0.68 ||| 0.72
1.05 ||| 0.53
0.57 ||| 1.05
0.68 ||| 0.96
1.80 ||| 0.80

1.15 ||| 1.53

-
1.04 ||| 4.20
1.19 ||| 0.47

Table 12. Reproductions En-De MT tasks on Multi30K from Table 4 in [2] with cell scheme author
| reproduced. The BLEU(NLTK) values are replicated and were not provided by the authors. All
values are standard deviations over 5 different seeds.

---
**Source PDF:** `2021_06_article.pdf`
