R E S C I E N C E C

Replication / ML Reproducibility Challenge 2022
[Re] Exploring the Representation of Word Meanings in
Context

Edited by
Koustuv Sinha,
Maurits Bleeker,
Samarth Bhargav

Received
04 February 2023

Published
20 July 2023

DOI
10.5281/zenodo.8173658

Matteo Brivio1, ID and Çağrı Çöltekin1, ID
1University of Tübingen, Tübingen, Germany

Reproducibility Summary

This report summarizes our reproduction of the ACL2021 paper Exploring the Representation
of Word Meanings in Context: A Case Study on Homonymy and Synonymy by Garcia[1].

Scope of Reproducibility — The original author looks at both static and contextualized word
embeddings to assess their ability to adequately represent different lexical‐semantic relations, such as homonymy and synonymy. While the author describes experiments
with a number of contextualized and static models, we limit our reproducibility attempt
to the results reported for BERT and fastText. We also extend the original experiment
by compiling a new Italian dataset and report our findings for this additional resource.

Methodology — We rely on the existing code‐base, modifying it where necessary and integrating it with a few additional scripts for data preparation and statistics computation.
Our code is available at https://github.com/matteobrv/repro-homonymy-acl21.

Results — We only manage to partially reproduce the original scores. Nonetheless, the
hypothesis formulated in the original paper are still corroborated.

What was easy — Overall, the paper is clear and provides a good overview of the experiments. It outlines the structure of the data‐sets and how they were compiled. The code
and the data are available at https://github.com/marcospln/homonymy_acl21.

What was difficult — An amended version of the original paper with additional details
about the experiments is available on arXiv [2]. We initially relied on the ACL [1] version which led to some minor issues during the reproducibility attempt. The code‐base
does not include the script used to compute the reported statistics, but upon request the
author provided a preliminary version which we re‐implemented. Lastly, due to some
minor bugs and lack of information about the version of the libraries being used, some
minor changes to the original code‐base were necessary.

Communication with original authors — We exchanged a number of emails with the author
to discuss implementation details and discrepancies in the reproducibility results. We
received prompt and helpful responses to all of our questions.


Code
swh:1:dir:c0cbb81bf15ace80d98da9d95fed3440046539f9.
Open peer review is available at https://openreview.net/forum?id=Od5dD58libt.

https://github.com/matteobrv/repro-homonymy-acl21

available

DOI

at

is

–

10.5281/zenodo.7886291.

–

SWH




## 1 Introduction

The distributional hypothesis, the idea that the statistical distribution of linguistic items
in context plays a key role in characterizing their semantic behavior [3, 4], lies at the
heart of modern word representation models. When trained on large enough data‐sets,
these models allow to project linguistic items into a unified vector space [5], producing
distributional vectors commonly referred to as word embeddings.
A major distinction can be made between static and contextualized word embeddings.
Static word vector representations obtained through models such as Word2Vec [6] and
fastText [7] are context independent, that is to say a single word is always mapped to the
same vector, irrespective of its context. On the other hand, in contextualized representations, produced by models such as BERT [8], each word vector is dependent on and
embeds at least some information about its particular context of occurrence [9].
The paper we examine [1] investigates whether and to what extent both static and contextualized embeddings are able to adequately represent different lexical‐semantic relations, such as homonymy and synonymy. In other words, it evaluates whether such
models can discriminate between unrelated meanings represented by the same word
form (homonymy) and identify the same sense conveyed by different words (synonymy).
To this end the author compiles data‐sets for four language varieties – English, Spanish,
Portuguese and Galician – and carries out four experiments (see section 2). We manage
to partially reproduce the original results and further test the author’s hypotheses on a
newly‐compiled Italian data‐set. Despite some discrepancies, our observations validate
the claims of the original author.

## 2 Scope of reproducibility

For each language variety Garcia[1] carries out four experiments and reports the results
in Table 4 of the original paper. We try to reproduce these results and in doing so to
verify the hypothesis formulated for each of the four experiments.

• Experiment 1: given a target‐word and three identical words in different contexts,
two of them synonyms of the target, we test whether the model correctly discriminates the outlier. As an example, consider rows 1.1 and 1.2 in Table 1. Hypothesis:
static embeddings are expected to fail, producing three identical vectors, while
contextualized models should correctly identify the outlier.

• Experiment 2: given a target‐word and three different words in different contexts,
two of them synonyms of the target, we test whether the model is biased towards
one specific sense. For example, consider rows 2.1 and 2.2 in Table 1. The targetword coach can either mean bus or trainer. If the model were biased towards the
latter sense, it would always represent coach closer to trainer even in sentences
where this would not make sense. Hypothesis: biased models will not identify the
outlier sense. However, incorporating contextual information might be helpful.

• Experiment 3: given a target‐word and three words in different contexts, two of
them synonyms of the target, we test whether the model correctly discriminates
the outlier. In this experiment the outlier is an homonym of one of the two synonyms. For example, consider rows 3.1 and 3.2 in Table 1. Hypothesis: static
embeddings are likely to incorrectly represent homonyms closer than synonyms,
while contextualized embeddings should model the three words correctly.

• Experiment 4: given a target‐word and three different words, two of them synonyms of the target, we test whether the model correctly discriminates the outlier.
In this experiment the outlier has to be in the same context as at least one of the
two synonyms. As an example, consider rows 4.1 and 4.2 in Table 1. Hypothesis:




static embeddings may pass the test as they tend to represent type‐level synonyms
closely. Contextualized models, on the other hand, might be puzzled at targets
with different meanings occurring in the same context.

## 3 Methodology

### 3.1 Datasets

We work with the four data‐sets provided by Garcia[1] and with an additional Italian
data‐set that we compiled ourselves. Each of the five data‐sets is composed of triples,
where each triple is characterized by a specific target‐word and three sentences. Two of
the sentences contain synonyms of the target‐word or the target itself. The remaining
sentence might contain either an homonym of the target, an homonym of one of the
synonyms or an unrelated word. For each triple three features are given: POS, Context
and Overlap.
The three features are obtained through a comparison between Sent.1 and Sent.2,
Sent.1 and Sent.3 as well as Sent.2 and Sent.3. This allows to control for context,
word and POS‐tag overlap. As an example, consider row 4.2 in Table 1. For this triple the
value of Context is false|true|false, as the first and last word occur in the same
context, thus making the second comparison (Sent.1 vs Sent.3) true. As another
example, consider row 3.2. In this triple the value of Overlap is false|false|true,
as the words in Sent.2 and Sent.3 share the same form. Lastly, looking at the same
triple, the value of POS is same|same|same, as the three words are all nouns.

Target

Sent. 1
### 1.1 Coach He was appointed as

the new coach.

### 1.2 Match He watched the foot‐

ball match.

### 2.1 Coach We go to the airport

### 2.2 Bank

by coach.
I used to work in a
bank.

### 3.1 Spring We planted flowers in

### 3.2 Lead

### 4.1 Drop

### 4.2 Duck

spring.
They have an advantage of 28 points.
Temperatures
to freezing at night.
I duck to dodge the
ball.

drop

Sent. 2
She joined the team
as coach.
Chelsea have a match
with United.
They traveled by bus.

Banks are financial
institutions.
Cherry trees bloom
in the springtime.
Before his goal, the
team had the lead.
Temperatures fall to
freezing at night.
She lowers her gaze.

Sent. 3
We go to the airport
by coach.
He lit the match on
his shoe.
She was appointed as
the new trainer.
They camped on the
shores of the lake.
The spring in the fuel
pump is broken.
The detectives are
chasing a new lead.
Temperatures rise to
freezing at night.
I raise to dodge the
ball.

Table 1. Triples examples, two for each experiment. For each triple, two sentences contain words
with the same meaning as the target, while the remaining one does not.

The English, Spanish, Portuguese and Galician data‐sets consist of 709, 645, 358 and 1365
triples, respectively. The Italian data‐set is smaller and comprises 243 samples. Following Garcia[1], we only consider triples containing words with the same POS‐tag. We
report the total number of such triples and their distribution per experiment in Table 2.

### 3.2 Model descriptions

We work with two types of models, BERT monolingual and fastText. BERT models are
loaded through the Transformers library [10]. For English, we rely on the base‐uncased




Language
Galician
English
Portuguese
Spanish
Italian

E1


E2


E3


E4


Total


Table 2. Total number of triples in which the POS feature is same|same|same together with their
distribution per experiment.

BERT model by Devlin et al.[8]. For Portuguese and Spanish we use the base‐cased models released by Souza, Nogueira, and Lotufo[11] and Cañete et al.[12], respectively. For
Galician, we rely on the small‐cased model trained by the original author while for Italian we use the base‐cased model originally provided by Schweter[13].
For fastText we use models of 300 dimensions and experiment with three architectures:
skip‐gram [7], CBOW [14] and MCBOW, a variation of the latter [15]. Specifically, for
English we work both with the official MCBOW1 and skip‐gram2 versions. For Spanish
we use both the official skip‐gram3 and CBOW4 models. For Portuguese we rely on the
skip‐gram5 version by Hartmann et al.[16]. For Galician we use the skip‐gram6 model
trained by Garcia[1] and for Italian the official skip‐gram7 version.

### 3.3 Experimental setup and code

The four experiments described in section 2 rely on BERT and fastText embeddings. For
both architectures a number embedding creation strategies are explored. We only describe those for which a result is reported in Table 4 of the original paper. Note that
whenever a word consists of more than one token (e.g. financial institutions) the average
of the token embeddings is considered.
For BERT models the following three approaches are tested:

• Sentence vector (Sent): an embedding obtained by averaging the representations
of all the words in a given sentence, but the [CLS] and [SEP] tokens. Each representation is obtained by concatenating the vectors produced in the last four layers
of the model.

• Word vector sum (Add): an embedding of a specific word obtained by summing

its representations across the last four layers of the model.

• Word vector concatenation (Cat): an embedding of a specific word obtained by

concatenating its representations across the last four layers of the model.

For fastText models the following three approaches are tested:

• Word vector (WV ): an embedding of a specific word.

• Sentence vector (Sent): an embedding obtained by averaging the representations

of all the words in a given sentence.

1English MCBOW fastText: https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip
2English skip‐gram fastText: https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.en.vec
3Spanish skip‐gram fastText: https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.es.vec
4Spanish CBOW fastText: https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.es.300.vec.gz
5Portuguese skip‐gram fastText: http://143.107.183.175:22980/download.php?file=embeddings/fasttext/skip_s300.zip
6Galician skip‐gram fastText: https://zenodo.org/record/4481614/files/fasttext_sg_300d_w5.zip?download=1
7Italian skip‐gram fastText: https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.it.vec




• Syntax (Syn3): an embedding of a specific word obtained by adding the word representation to those of its syntactic head and dependents. The underlying assumption is that the syntactic context of a word would characterize its meaning. Generating this embedding requires converting each sentence in each triple to a CoNLLU format.

The output of each model is evaluated as follows: for each triple, where two words (a
and b) are synonyms and a third one (c) has a different meaning, three cosine similarities
between their embeddings are computed: sim1 = cos(a, b), sim2 = cos(a, c) and
sim3 = cos(b, c). Ultimately, the model should be able to discriminate the outlier c
i.e. the output for a specific triple is correct only if sim1 > sim2 and sim1 > sim3.
For each model and embedding creation strategy we compute four accuracy scores, one
per experiment, and provide macro‐ and micro‐average results across them. Lastly,
for each embedding creation strategy, we also report the micro‐average accuracy score
across the entire set of generated embeddings. It is worth noting that for each language
variety the corresponding data‐sets also contain triples of sentences that are not part of
any of the four experiments described in Section 2.
We only report results for triples in which the synonyms and homonyms belong to the
same word category (POS = same|same|same). This allows to focus on the semantic
knowledge encoded in their embeddings rather than on the morpho‐syntactic information.
We rely on the code‐base released by the original author, modifying it where necessary
and integrating it with a few additional scripts for statistics computation and data preparation.

### 3.4 Computational requirements

We work with pre‐trained BERT and fastText models, relying on a 3.10GHz Intel Core
i9‐7940X CPU. The total running‐time for the experiment is about 30 minutes.

## 4 Results

### 4.1 Results reproducing the original paper

Our results partially match those reported in the original study. In particular, we successfully reproduce the accuracy scores for the Galician BERT and fastText models, as
well as for the English BERT and Portuguese fastText ones. However, we also observe
a number of discrepancies across English, Spanish and Portuguese. We plot the difference between our results and the original ones in Figure 1 and report the exact values
in Table 4 in the Appendix. Galician results are not included as they match the original
ones but we provide them in our GitHub repository.
Looking at BERT, the scores we obtain for Portuguese and Spanish are mostly higher
than those originally indicated, with only two exceptions for Spanish in experiment 2
(BERT sent) and experiment 4 (BERT add). Turning to fastText, the results for the English and Spanish skip‐gram models also deviate from the original ones. Nonetheless,
relying on the MCBOW [15] and CBOW [14] implementations we manage to reproduce
the original English and Spanish scores, respectively (see Table 4).
Overall, BERT models perform consistently better than fastText in the first three experiments across all languages, while fastText models score higher accuracy values in the
fourth one.

### 4.2 Results beyond the original paper

We summarize our findings for the Italian data‐set in Table 3. Overall, the trend across
the four experiments is consistent with the one we observe for the original language




0.1


−0.1

0.2

0.1


0.2

0.1


English

Spanish

Portuguese

E1

E2
BERT sent

E3

BERT add

E4
skip sent

Ma
skip wv

Mi
skip syn3

F

Figure 1. Difference between our accuracy scores and those reported in the original paper computed across the four experiments, as well as for the macro (Ma), micro (Mi) and full (F) accuracy.
For each language, only the models for which a discrepancy is observed are considered.

varieties, with BERT achieving the highest accuracy in the first three experiments for at
least one embedding type (Vec) and fastText being the top performer in the last experiment. It is worth noting that the micro‐average results across the four experiments (Mi)
and the micro‐average values on the whole data‐set (F) are the same for each embedding
type.

Model

BERT

fastText

Vec
Sent
Add
Cat
Sent skip
WV skip
Syn 3 skip

E1
0.763
0.831
0.831
0.763

0.576

E2
0.8
0.888
0.875
0.863
0.462
0.75

E3
0.741
0.463
0.444
0.704

0.389

E4
0.14
0.3
0.24
0.16
0.62
0.22

Ma
0.611
0.620
0.597
0.622
0.271
0.484

Mi
0.642
0.658
0.638
0.658
0.28
0.519

F
0.642
0.658
0.638
0.658
0.28
0.519

Table 3. Summary of the BERT and fastText results for Italian. For each embedding type (Vec) we
report the accuracy scores of the four experiments, together with their macro‐ and micro‐average
results. Lastly, we indicate the micro‐average on the whole data‐set (F).

## 5 Discussion

For all five language varieties, our results support the hypotheses formulated in Section
2. Specifically, across all languages, BERT achieves higher accuracy scores in the first
three experiments, confirming that contextualized models are better at discriminating




an outlier sense when dealing with different sentences. At the same time, these models rely heavily on the surrounding context and struggle to tell apart target‐words with
different meanings that occur in similar sentences. This is confirmed by the poor performance of BERT models in the fourth experiment which also corroborates the last
hypothesis.
Despite confirming the original claims, our results partially deviate from those originally reported. With respect to BERT, the accuracy scores we observe for Spanish and
Portuguese are overall higher than the original ones. In this regard, it is worth mentioning the result we obtain for Portuguese in the second experiment. While the original
study indicates a highest score of 0.541 (Add(o)), which is too low to support the second
hypothesis, we register a score of 0.784 (Add(r)) which is better than the fastText ones.
We try to investigate the cause of these discrepancies, but the respective models show
no recent updates that could motivate them. However, it should be noted that the original contribution does not specify the version of the Transformers library [10] being used
and that we likely rely on a more recent version to carry out our experiment. Turning to
fastText, our results for English and Spanish are also inconsistent with those originally
reported. For these languages the original author claims to rely on 300‐dimensional vectors obtained through the skip‐gram model described in Bojanowski et al.[7]. However,
we only manage to reproduce the English and Spanish scores using vectors obtained
through the CBOW [14] and MCBOW [14] implementations, respectively.
Coming to the Italian results, we observe that the micro‐averages across the four experiments (Mi) and on the whole data‐set (F) are the same for each embedding type (Vec).
This is not the case for the language varieties considered in the original study. The reason for this is that the original data‐sets also contain triples of sentences that are not
contemplated in the four experiments, for example triples in which the synonyms and
homonyms belong to different word categories.
In summary, despite some discrepancies, our results are consistent with the findings of
the original paper and support the initial hypotheses.

References

1. M. Garcia. “Exploring the Representation of Word Meanings in Context: A Case Study on Homonymy and Syn-
onymy.” In: Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and
the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers). Online:
Association for Computational Linguistics, Aug. 2021, pp. 3625–3640. DOI: 10.18653/v1/2021.acl-long.281.
URL: https://aclanthology.org/2021.acl-long.281.

2. M. Garcia. “Exploring the Representation of Word Meanings in Context: A Case Study on Homonymy and Syn-

3.

4.

5.

6.

7.

8.

pp.

(1954),

10.2–3

146–162.

Structure.”

In: Word

S. Harris.

“Distributional

onymy.” In: CoRR (2021). DOI: 10.48550/ARXIV.2106.13553. URL: https://arxiv.org/abs/2106.13553.
Z.
DOI:
10.1080/00437956.1954.11659520. eprint: https : / / doi . org / 10 . 1080 / 00437956 . 1954 . 11659520.
URL: https://doi.org/10.1080/00437956.1954.11659520.
A. Lenci. “Distributional Models of Word Meaning.” In: Annual Review of Linguistics 4.1 (2018), pp. 151–171.
DOI: 10.1146/annurev-linguistics-030514-125254. URL: https://doi.org/10.1146/annurev-linguistics-030514-
125254.
Z. Liu, Y. Lin, and M. Sun. “Representation Learning and NLP.” In: Representation Learning for Natural Lan-
guage Processing. Springer Singapore, 2020, pp. 1–11. DOI: 10.1007/978-981-15-5573-2_1. URL: https://doi.
org/10.1007/978-981-15-5573-2_1.
T. Mikolov, K. Chen, G. Corrado, and J. Dean. “Distributed representations of words and phrases and their
compositionality.” In: Advances in neural information processing systems 26 (2013).
P. Bojanowski, E. Grave, A. Joulin, and T. Mikolov. “Enriching Word Vectors with Subword Information.” In:
Transactions of the Association for Computational Linguistics 5 (2017), pp. 135–146.
J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. “BERT: Pre-training of Deep Bidirectional Transformers
for Language Understanding.” In: Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers). Minneapolis, Minnesota: Association for Computational Linguistics, 2019, pp. 4171–4186. DOI:
10.18653/v1/N19-1423. URL: https://aclanthology.org/N19-1423.




9.

10.

11.

12.

13.

14.

15.

A. Rogers, O. Kovaleva, and A. Rumshisky. “A Primer in BERTology: What We Know About How BERT
Works.” In: Transactions of the Association for Computational Linguistics 8 (2021), pp. 842–866. DOI:
10.1162/tacl_a_00349. eprint: https : / / direct . mit . edu / tacl / article - pdf / doi / 10 . 1162 / tacl \ _a \ _00349 /
1923281/tacl\_a\_00349.pdf. URL: https://doi.org/10.1162/tacl%5C_a%5C_00349.
T. Wolf et al. “Transformers: State-of-the-Art Natural Language Processing.” In: Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language Processing: System Demonstrations. Online: Associa-
tion for Computational Linguistics, 2020, pp. 38–45. URL: https://www.aclweb.org/anthology/2020.emnlp-
demos.6.
F. Souza, R. Nogueira, and R. Lotufo. “BERTimbau: pretrained BERT models for Brazilian Portuguese.” In: 9th
Brazilian Conference on Intelligent Systems, BRACIS, Rio Grande do Sul, Brazil, October 20-23 (to appear).
2020.
J. Cañete, G. Chaperon, R. Fuentes, J.-H. Ho, H. Kang, and J. Pérez. “Spanish Pre-Trained BERT Model and
Evaluation Data.” In: PML4DC at ICLR 2020. 2020.
S. Schweter. Italian BERT and ELECTRA models. Version 1.0.1. 2020. DOI: 10.5281/zenodo.4263142. URL:
https://doi.org/10.5281/zenodo.4263142.
E. Grave, P. Bojanowski, P. Gupta, A. Joulin, and T. Mikolov. “Learning Word Vectors for 157 Languages.” In:
Proceedings of the International Conference on Language Resources and Evaluation (LREC 2018). 2018.
T. Mikolov, E. Grave, P. Bojanowski, C. Puhrsch, and A. Joulin. “Advances in Pre-Training Distributed Word
Representations.” In: Proceedings of the International Conference on Language Resources and Evaluation
(LREC 2018). 2018.

16. N. Hartmann, E. Fonseca, C. Shulby, M. Treviso, J. Silva, and S. Aluı́sio. “Portuguese Word Embeddings: Evalu-
ating on Word Analogies and Natural Language Tasks.” In: Proceedings of the 11th Brazilian Symposium in
Information and Human Language Technology. Uberlândia, Brazil: Sociedade Brasileira de Computação, Oct.
2017, pp. 122–131. URL: https://aclanthology.org/W17-6615.




h
s
i
l
g
n
E

h
s
i
n
a
p
S

e
s
e
u
g
u
t
r
o
P


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

F

i

M

a
M


E


E


E


E

F

i

M

a
M


E


E


E


E

F

i

M

a
M


E


E


E


E

.
c
e
V

l
e
d
o
M


.


.


.


.


‐


.


.


.


.


‐


.


.


.


.


‐


.


.


.


.


‐


.


.


.


.


‐


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐


.


.


.


.


.


‐


.


.


‐

‐

‐


.


.


.


.


.


.


.


‐

‐

‐

‐


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


‐


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


.


‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐


‐

‐


.


.


.


.


)
o
(
p
i
k
s
V
W

)
r
(
p
i
k
s
V
W

‐

‐

‐

‐

)
r
(

W
O
B
C
M
V
W

)
r
(

W
O
B
C
V
W

‐

‐

‐

‐

)
r
(

W
O
B
C
M

t
n
e
S

)
r
(

W
O
B
C
t
n
e
S


.


.


.


.


.


.


.


.


.


.


.


.


.


.


)
o
(
p
i
k
s

n
y
S

)
r
(
p
i
k
s

n
y
S

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

‐

)
r
(

W
O
B
C
M

n
y
S

)
r
(

W
O
B
C

n
y
S

t
x
e
T
t
s
a
f

)
o
(

t
n
e
S

)
r
(

t
n
e
S

)
o
(

t
a
C

)
r
(

t
a
C

)
o
(
d
d
A

)
r
(
d
d
A

)
o
(
p
i
k
s

t
n
e
S

)
r
(
p
i
k
s

t
n
e
S

T
R
E
B

e
p
y
t
g
n
i
d
d
e
b
m
e
h
c
a
e
r
o
F

.
y
d
u
t
s

l
a
n
i
g
i
r
o
e
h
t
n

i
d
e
t
r
o
p
e
r
e
s
o
h
t

m
o
r
f
e
t
a
i
v
e
d
s
t
l
u
s
e
r
e
s
o
h
w
s
e
i
t
e
i
r
a
v
e
g
a
u
g
n
a
l
e
h
t

r
o
f

s
e
r
o
c
s

t
x
e
T
t
s
a
f
d
n
a
T
R
E
B
e
h
t

f
o
y
r
a
m
m
u
S

.

l


e
b
a
T

e
t
a
c
i
d
n

i

e
w

,
y
l
t
s
a
L

.
s
t
l
u
s
e
r

e
g
a
r
e
v
a
‐
o
r
c
i
m
d
n
a

‐
o
r
c
a
m

r
i
e
h
t
h
t
i

w
r
e
h
t
e
g
o
t

,
s
t
n
e
m

i
r
e
p
x
e

r
u
o
f

e
h
t

f
o
s
e
r
o
c
s

y
c
a
r
u
c
c
a

)
r
(
d
e
c
u
d
o
r
p
e
r
d
n
a

)
o
(

l
a
n
i
g
i
r
o
e
h
t

t
r
o
p
e
r

e
w

)
c
e
V

(

.
d
e
t
r
o
p
e
r
y
l
l
a
n
i
g
i
r
o
e
s
o
h
t
h
c
t
a
m
y
e
h
t

s
a
d
e
d
u
l
c
n

i

t
o
n
e
r
a
n
a
i
c
i
l
a
G
r
o
f

s
t
l
u
s
e
R

.
)
F
(

t
e
s
‐
a
t
a
d
e
l
o
h
w
e
h
t
n
o
e
g
a
r
e
v
a
‐
o
r
c
i
m
e
h
t

---
**Source PDF:** `755e8e3a9963.pdf` (2023_09_article.pdf)  
**URL:** https://zenodo.org/record/8173658/files/article.pdf
