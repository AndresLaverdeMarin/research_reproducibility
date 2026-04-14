R E S C I E N C E C

Replication / ML Reproducibility Challenge 2022
[¬Re] A Reproducibility Case Study of “Fairness
Guarantees under Demographic Shift”

Dennis Agafonov1,†, ID , Jelke Matthijsse1,†, ID , Noa Nonkes1,†, ID , and Zjos van de Sande1,†, ID
1University of Amsterdam, Amsterdam, The Netherlands – †Equal contributions

Edited by
Koustuv Sinha,
Maurits Bleeker,
Samarth Bhargav

Received
04 February 2023

Published
20 July 2023

DOI
10.5281/zenodo.8206607

Reproducibility Summary

Scope of Reproducibility — This work studies the reproducibility of the paper Fairness guar-
antees under demographic shift (2022) by Giguere et al. Specifically, the authors discuss
Shifty, an algorithm that provides high‐confidence guarantees that a user‐specified
fairness constraint will hold in the case of a demographic shift between training and deployment data. The authors claim that Shifty achieves this without any significant loss
of accuracy when compared to a number of other baseline algorithms.

Methodology — Using the open‐source code provided by the authors, experiments were
conducted to collect the results of Shifty and a number of other baseline algorithms
when deployed on three different datasets. Results were collected in the form of accuracy, failure rate, and the probability of not finding a fair solution. The experiments in
this reproducibility study were conducted on a total of 115 CPU hours.

Results — The claim that Shifty guarantees fairness with high confidence is strongly
confirmed by the reproduction results of this study. It was also found in this reproducibility study that Shifty achieves accuracy scores comparable to those of other
fairness algorithms.

What was easy — The open‐source code was structured in a way that allowed us to make alterations to the experimental setup or the implementations of the models. The original
datasets were also provided in a structured manner and were already standardized.

What was difficult — Modifications to the code were necessary in order to run this code
efficiently and without errors; in the original code, there were packages missing, redundant functions and files, and mistakes in the handling of the user‐specified fairness
constraints.

Communication with original authors — The authors did not respond to our inquiries, resulting in no communication with the original authors.


Code is available at https://github.com/noanonkes/fact-guarantee. – SWH swh:1:dir:c769bc1fc87a24b6811f318d7ad56ea9a70954e7.
Open peer review is available at https://openreview.net/forum?id=MMuv-v99Hy.




## 1 Introduction

Recent work in the field of AI concerned with bias in machine learning has been focused
on creating fair algorithms [2, 3]. However, if demographic shifts occur within the data
the model was trained on, such a model can often not maintain its fairness [1]. A demographic shift occurs when certain subgroups in a population are found more or less
frequently in deployment. This can result in the model being biased towards certain
groups, even if the model was originally trained to be equally fair to all groups [4]. It
is therefore crucial to not only ensure the fairness of the model, but to also take into
account possible shifts occurring after deployment. This encourages that the models
are still making fair and accurate predictions in a possibly shifted population.
To train models that are not only fair during training, but also have high‐confidence
fairness guarantees after deployment, Giguere et al. introduce a new type of learning algorithm called Shifty. This algorithm ensures fairness after known and unknown demographic shifts in the data [1]. According to the authors, Shifty provides a high probability of the fairness constraints being met when deployed on data that is distributed
differently, with respect to a demographic group, than it was during training. In the
case of a known shift, the exact demographic shift is known, while with an unknown
shift this is approximated by user‐specified intervals.
The main contributions of this work are:

• Determining the degree of reproducibility, by recreating the main experiments
conducted by Giguere et al., and concluding whether claims made in their research are factual, while considering what resources, such as computational power,
are needed to come to this conclusion.

• Improving the efficiency and workings of the code by resolving errors, cleaning

up the structure, and removing redundancies.

• Examining the validity of the claims by introducing an unseen dataset with an

unknown demographic shift.

• As the authors mention that Shifty in practice works with any learning algorithm, the original research is expanded by using a different training algorithm
than the one examined in the original paper.

## 2 Scope of reproducibility

The central claim introduced in this paper is that Shifty returns a machine learning algorithm that has a high probability of performing fair classification, before and after deployment, given a user‐specified fairness constraint. This constraint is defined to maintain fairness concerning a sensitive attribute such as race or sex. Importantly, Shifty
does not require access to the deployment data to ensure these guarantees. More specifically, the authors claim the following:

• High‐confidence fairness guarantees: In the case of a known or unknown demographic shift, Shifty provides high‐confidence guarantees that a certain userspecified fairness constraint will hold even after the shift.

• Minor loss of accuracy: In the case of a known or unknown demographic shift, if
enough data is provided, Shifty is able to train models, whose resulting accuracy
is then comparable to that of models which do not account for demographic shift,
such as Fairness Constraints [5] and Seldonian [2].

• Finding a solution: As the amount of training data increases, the probability of

Shifty returning No Solution Found (NSF) decreases.




The remainder of this paper is structured as follows: In section 3, we give a detailed
description of Shifty and the fairness algorithms it was compared to. In section 4, the
methods that were used to verify the claims of the authors are set out. This includes
an explanation of the datasets, the hyperparameters, the experimental setup and code,
and lastly the computational requirements needed to come to the results. Moreover,
we elaborate on the steps taken to conduct additional research. Then, the results of
this study are discussed and compared to the original results in section 5. Finally, we
conclude this study by discussing and evaluating the used approach.

## 3 Model descriptions

### 3.1 Shifty

The Shifty algorithm is made up of three main parts of which a short overview is given
below and which are later discussed more elaborately:

1. The first step consists of partitioning the dataset D = {(Xi, Yi, Si, Ti)}n

i=1 into two
parts. Each sample in D is uniformly distributed and consists of a feature, label,
fairness attribute, and demographic attribute respectively. One part of D is used
for candidate model selection, called Dc and the other is used to perform a fairness
test, called Df .

2. Secondly, the candidate model, denoted as θc, is trained using Dc, which can be
any classification model, while a user‐specified fairness constraint is taken into
account, also denoted by a function of g. During training, the features, labels,
and fairness attributes are used. The candidate model is deemed fair if g(θc) ≤ 0.
This is calculated by inverting Student’s t‐test [6] and is given by Equation 1, where
E[H|ξ] − τ = g(θc).

3. Lastly, a high‐confidence upper bound (HCUB) on the candidate model is calculated after it is deployed in an environment affected by a demographic shift, which
is simulated using the demographic attribute. g′(θc) denotes the fairness of θc after
deployment and should also be less or equal to zero with high confidence, which
then again is calculated using the inverted t‐test.

For the third step, the description of the possible demographic shifts is defined by Q :=
{(at, bt)}t∈T . It is a user‐defined set of upper and lower boundaries on the marginal
probability of each demographic attribute value after deployment. If the demographic
shift is known then ∀t∈T [at = bt = P r(T ′ = t)], where P r(T ′ = t) is the probability of
demographic attribute t occurring after deployment.

P r(E[H|ξ] ≤ Uttest(g, D, θ, δ)) ≥ 1 − δ, where δ ∈ [0, 1]

(1)

### 3.2 Baselines

To assess Shifty’s effectiveness, it was compared to other algorithms, namely Fairness
Constraints [5], Seldonian, Quasi-Seldonian [2], Fairlearn [3], and 
[7]. The features of these algorithms are summarized in Table 1. Of these algorithms,
Shifty is thus the first algorithm to provide fairness guarantees under demographic
shift.

### 3.3 Fairness Constraints

The fairness constraints that Shifty uses are user‐specified. In this study and in the
original paper, two fairness constraints are utilized, namely Demographic Parity (DP)




Algorithm
FC
Seldonian
Q‐Seldonian


Classifier
Decision boundary
Linear decision boundary
Linear decision boundary
Linear SVC
Logistic regression

Difference with Shifty


Does not provide fairness guarantees

Table 1. Algorithms overview. For each algorithm, its classifier and its difference with Shifty are
specified. ‘FC’ stands for Fairness Constraints and ‘Q‐Seldionian’ is the Quasi-Seldonian
algorithm.

and Disparate Impact (DI). Equations 2 and 3 show the definitions of DP and DI, respectively. In these equations, g represents the function to define unfair behaviour, θ(X) the
model, ϵ the fairness constraint tolerance hyperparameter, and S the sensitive fairness
attribute. In the case of S being the attribute sex, s0 and s1 would represent male and
female.
gDP := |E[θ(X)|S = s0] − E[θ(X)|S = s1]| − ϵDP

(2)

gDI := − min(

E[θ(X)|S = s0]
E[θ(X)|S = s1]

,

E[θ(X)|S = s1]
E[θ(X)|S = s0]

) + ϵDI

(3)

## 4 Methodology

We reproduced the original results from the paper using the open‐source implementation of the code as provided by the authors on GitHub [8]. This code was analyzed to
understand how the results were achieved. The provided code is partly based on the
papers that cover the different fairness algorithms that Shifty is compared to (section
3.2). A code coverage analysis revealed that a large fraction of the code was not used to
obtain the results corresponding to the experiments as discussed in the paper.

### 4.1 Datasets

To verify the results, this reproducibility study used the same data to conduct the experiments. The authors provided the pre‐processed datasets and the code to pre‐process
the original data. This pre‐processing resulted in datasets with zero mean and unit variance. For the non‐Seldonian algorithms, both datasets were split up into a 6:4 ratio of
train and test data. For the Seldonian algorithms, the ratio was a 6:4 of data for the
candidate selection (Dc) and fairness testing (Df ) subsets.
The original paper conducted experiments on the UCI Adult Census dataset [9] and the
UFRGS Entrance Exam and GPA dataset [10]. To further validate the claims made by the
authors, an additional dataset was acquired containing approximately 50k diabetic patient encounters collected over a period of 10 years from 130 US hospitals [11]. This
dataset will subsequently be referred to as Diabetes. Each encounter recorded several
statistics to help determine the relationship between the probability of readmission and
hbA1c measurement depending on primary diagnosis. For all datasets, we present the
relevant statistics and their main purpose in Table 2.

Datasets
UCI Adult Census [9]
UFRGS [10]

Task
Predict income above $50k
Predict GPA above 3.0

Diabetes [11]

Predict readmission


43k
43k
47k
49k

Fairness attr.
Race
Sex
Race
Sex

Demographic attr.
Sex
Race
Sex
Race

Table 2. Datasets overview. All three datasets were used for binary classification tasks. In the UCI
Adult Census and Diabetes datasets, the samples were filtered down to only include white and black
individuals, when race is considered the fairness attribute.




### 4.2 Hyperparameters

The original authors’ code included a batch file to run the experiments with specified hyperparameters (shown in Table 3 for the UCI Adult Census dataset; for UFRGS results, see
Appendix 7). The provided code contained pre‐determined values for the fairness constraint tolerance hyperparameter ϵ (used in equations 2 and 3). It also provided the split
ratio for training data and test data, and the split ratio for candidate data and fairness
data for the Seldonian algorithms. The batch file also included the number of iterations
considered for the training algorithm a, and the confidence bound δ (Eq. 1). Lastly,
for the unknown distributional shift the width of the intervals around true marginals
representing the valid demographic shifts is given by an α‐value.

Constraint
DI
DP

ϵ
‐0.8
0.1

train / test
0.4
0.4

Dc / Df
0.4
0.4

n‐iters
2000
2000

δ
0.05
0.05

α*
0.5
0.5

Table 3. Hyperparameter values for the experiments run with the UCI Adult Census dataset specified
for DI or DP for both an unknown demographic shift and a known demographic shift. The α is
only used in the case of an unknown shift.

### 4.3 Experimental setup and code

In the original experiments, each algorithm was trained with different‐sized subsets of
the data to determine how much data was needed to maintain a fairness guarantee under demographic shift. For a known demographic shift, we used subset sizes ranging
from 10k to 60k points, in intervals of 5k datapoints. For an unknown demographic
shift, we increased the intervals to 10k while the range remained the same. In a single
trial for an user‐specified constraint, the results per subset size were collected for each
algorithm for both cases of a known and unknown demographic shift.
The original paper specified that 25 trials were executed for each fairness constraint in
both cases of a known or unknown demographic shift and for each dataset mentioned
in section 4.1. In our experiments, due to a lack of computational resources, we only
executed 10 trials for each case.
The original classifier that we used for the three Seldonian algorithms was a linear decision boundary. Additionally, we implemented a multi‐layer perceptron (MLP) as a
classification model that works with the Seldonian algorithms. The preferred classifier
and the sizes of the hidden layers can be specified within the batch file and we used an
MLP with 2 hidden layers of sizes 16 and 8. Furthermore, we instantiated the weight
parameters according to the normal distribution and optimized these in the same way
as the original Shifty implementation. This experiment was run for 2 trials for each
constraint mentioned previously, for a known and unknown demographic shift.
After every single trial, we saved the results for each algorithm and subset size. These
results contained the probability of a NSF, the accuracy of the original model and the
accuracy of the deployed model, as well as the failure rate of the original model and the
failure rate of the deployed model. After completing all the trials, the mean and standard
error were determined for each of these measurements. The code of this reproducibility
study can be found here.

### 4.4 Computational requirements

The code provided by the original authors contains an elaborate launcher that allows the
experiments to be run with CPU multiprocessing. The CPU used to obtain the results
was an AMD Ryzen 7 3800X processor, utilizing 8 cores simultaneously.
During the process, the time required per trial was recorded. This was done for each
dataset, as well as for each constraint for both the known and unknown demographic




shift. These times were then averaged. For the UFRGS dataset this resulted in 15.5 minutes per trial, while the UCI Adult Census dataset resulted in 24 minutes per trial. The
total (CPU) time required, resulted in 26 hours for the reproduction of the original experiments. The additional experiments entail 28 additional hours for the experiments
run with the Diabetes dataset, and 60 hours for the experiments run with MLP classifier,
concluding to roughly 115 hours total needed for the considered experiments.

## 5 Results

In this section, we discuss the reproduction results from the original paper and the results from the additional experiments. To verify the claims set out in section 2, the experiments were executed as described in section 4.3. The results of these experiments
include the probabilities that the Seldonian algorithms return NSF, and the accuracies
and failure rates of the algorithms before and after deployment. The graphs of these
results show the means and standard errors. The resulting accuracies and failure rates
of the models can be found in Appendix 7.2 & 7.3.
The two fairness constraints, DP and DI, were examined for both datasets. As in the
original paper, only the reproduced results of the UCI Adult Census dataset are shown.
The results of the UFRGS dataset can be found in Appendix 7.1.

### 5.1 Results reproducing original paper

The following section showcases the results of the experiments as discussed in section
4.3. In the sections 5.1.1, and 5.1.2 the specific results for the known and unknown
demographic shift are considered, respectively.

Result 1: Known Demographic Shift — Figure 1 plots the probability that the Seldonian,
the Quasi-Seldonian, and Shifty algorithms return NSF for a known demographic
shift for the fairness constraints DP and DI, per data subset size.


Figure 1. Probabilities of returning NSF per number of training samples when enforcing fairness
constraints DP and DI using the UCI Adult Census dataset under known demographic shift.

Result 2: Unknown Demographic Shift — Figure 2 plots the probability that the Seldonian,
the Quasi-Seldonian, and Shifty algorithms return NSF for an unknown demographic shift for the fairness constraints DP and DI, per data subset size.





Figure 2. Probabilities of returning NSF per number of training samples when enforcing fairness
constraints DP and DI using the UCI Adult Census dataset under unknown demographic shift.

### 5.2 Results beyond original paper

Additional experiments were conducted using a different dataset to substantiate the
claims made by the authors. Further experiments were carried out to validate whether
Shifty is successful independent of the classifier used. In the following section additional results will be discussed, using the Diabetes dataset as specified in section 4.1 and
the MLP classifier as specified in section 4.3.

Additional Results 1 — Using the Diabetes dataset, Figure 3 shows the probability that the
Seldonian, the Quasi-Seldonian, and Shifty algorithms return NSF for an unknown demographic shift under the fairness constraint DI, per data subset size. In the
left plot race is considered the demographic attribute, and in the right plot sex is considered the demographic attribute.

(a) Sex as demographic variable

(b) Race as demographic variable

Figure 3. Results when enforcing fairness constraint DI using the Diabetes dataset under unknown
demographic shift, with either the sex or race as demographic attribute.

Additional Result 2 — For the experiments run with an MLP classifier, the accuracies of the
Seldonian, the Quasi-Seldonian, and Shifty algorithms are shown before and
after deployment in Table 4, using the UCI Adult Census dataset. In case the algorithm
was not able to return a fair model in any trial, the results show a NaN‐value.




Accuracy ‐ Known Demographic Shift ‐ Demographic Parity


10k

15k

20k

25k

30k

35k

40k

45k

50k

55k

60k


nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

nan
nan
nan

53.99
54.86
0.87

nan
nan
nan

62.80
60.54
‐2.26

55.11
55.71
0.60

nan
nan
nan

40.99
40.66
‐0.33

nan
nan
nan

72.87
70.25
‐2.62

62.98
59.87
‐3.11

63.40
63.72
0.32

50.04
47.76
‐2.28

68.80
68.60
‐0.20

62.07
63.29
1.22

73.24
70.77
‐2.47

71.24
70.81
‐0.43

nan
nan
nan

54.11
53.04
‐1.07

65.09
65.67
0.58

Table 4. Results table showcasing the numerical mean accuracy (in percentages) of each Seldonian
algorithm using the MLP‐classifier and the UCI Adult Census dataset, for both the original and
deployment distribution when trained on a known demographic shift with the fairness constraint
DP. The decrease or increase in accuracy is shown in the rows named ‘difference’.

## 6 Discussion

### 6.1 Claim 1: High-confidence fairness guarantees

The results found in this reproducibility study validate the first claim made by the original authors, which asserts the high‐confidence fairness guarantee of Shifty. The
Shifty algorithm never returns an unfair model after deployment for both a known
and an unknown demographic shift, while other baseline algorithms do. The figures
portraying the results of the reproduction experiments supporting this claim can be
found in section 7.2 of the appendix.

### 6.2 Claim 2: Minor loss of accuracy

The results found in this reproducibility study show strong support for the second claim
made by the original authors, namely that there is only a minor loss of accuracy with
Shifty when compared to the other baseline algorithms. This is the case under both
a known and an unknown demographic shift, which can be seen in tables 6, 7, 8, and 9
in the appendix section 7.3.
What does stand out is that in the case of DI as the fairness constraint and under a known
demographic shift, Shifty achieves an accuracy that is approximately 10% lower than
that of RFLearn and Fairlearn.

### 6.3 Claim 3: Finding a solution

The results found in this reproducibility study do not show strong support for the third
claim, namely that Shifty avoids returning NSF when there is a reasonable amount
of training data available. Under a known demographic shift, the probability P r(NSF)
shows great fluctuations when altering the number of training samples, and thus showing no support for the third claim. This can be seen in Figures 1a and 1b.
The results under an unknown demographic shift, which can be seen in Figures 2a and
2b, are more stable compared to those under a known demographic shift. There are
fewer fluctuations in the probability P r(NSF) when the number of training samples
is increased, thus showing more support for the third claim. This is especially the case
with the fairness constraint being DP, which even results in Shifty having a probability
of 0% for 60K training samples. The results with DI as the fairness constraint show more
fluctuations, where the probability also increases when more training samples are used.




### 6.4 Additional Statements

The original paper mentions that the Shifty algorithm works with any underlying classification model. However, the additional experiments shown in Table 4 contain NaNvalues, meaning that Shifty accepted candidate models whilst they do not hold the
fairness constraints after deployment. From this, we conclude that when a non‐linear
model is implemented, the guarantee does not necessarily always hold. It is important
to note that we only ran 2 trials for each experiment with the MLP classifier.
Additionally, when we ran the experiments on the Diabetes dataset, the corresponding
results in Figure 3 show that there is no strong evidence for claim 3, which states that
larger subsets lead to a lower P r(NSF). While the results in Figure 3b show support for
this claim, Figure 3a displays strong fluctuations in the value of P r(NSF) and therefore
does not show strong evidence for the claim. However, for the two other claims in both
experiments, there are still strong indications that they are kept.

### 6.5 What was easy

Since the repository containing all the code used to run the experiments was made
available by the authors of the original paper, nothing needed to be implemented from
scratch. This also provided the tuned hyperparameters, resulting in no extra time needed
to search for these. The pre‐processed data was also supplied, avoiding any extra time
needed to match these to the implementation.

### 6.6 What was difficult

The code required a thorough analysis to determine its functioning and redundant parts,
and while the authors provided a file containing all the necessary requirements, multiple modules were not included. Furthermore, debugging was necessary to be able
to run the provided set‐up successfully, since the original code contained mistakes in
handling the fairness constraint expressions and loading the data.
The original paper did not present its results in numerical values but rather only showed
graphs. This made it complicated to fully validate whether the reproduced results approximate these, and thus to fully support the claims. Additionally, discrepancies were
found between the number of trials conducted according to the published code and the
amount mentioned in the paper. While the paper indicates to have run 25 trials for
each algorithm with each constraint per dataset, the code showed a lower number for
the experiments with an unknown demographic shift.

### 6.7 Communication with original authors

The original authors did not respond to our inquiry, so there was no communication.
It would have been useful to have received the numerical values of the figures in the
original paper, so that a quantitative comparison of the values could be performed.

References

1.

2.

3.

S. Giguere, B. Metevier, Y. Brun, P. S. Thomas, S. Niekum, and B. C. da Silva. “Fairness Guarantees under De-
mographic Shift.” In: International Conference on Learning Representations. 2022. URL: https://openreview.
net/forum?id=wbPObLm6ueA.
P. S. Thomas, B. Castro da Silva, A. G. Barto, S. Giguere, Y. Brun, and E. Brunskill. “Preventing undesirable
behavior of intelligent machines.” In: Science 366.6468 (2019), pp. 999–1004.
A. Agarwal, A. Beygelzimer, M. Dudı́k, J. Langford, and H. Wallach. “A reductions approach to fair classification.”
In: International Conference on Machine Learning. PMLR. 2018, pp. 60–69.




4.

J. Schrouff, N. Harris, O. Koyejo, I. Alabdulmohsin, E. Schnider, K. Opsahl-Ong, A. Brown, S. Roy, D. Mincu, C.
Chen, et al. “Maintaining fairness across distribution shift: do we have viable solutions for real-world applica-
tions?” In: arXiv preprint arXiv:2202.01034 (2022).

5. M. B. Zafar, I. Valera, M. G. Rogriguez, and K. P. Gummadi. “Fairness constraints: Mechanisms for fair classifi-

6.

cation.” In: Artificial intelligence and statistics. PMLR. 2017, pp. 962–970.
Student. “The Probable Error of a Mean.” In: Biometrika 6.1 (1908), pp. 1–25. URL: http : / / www . jstor . org /
stable/2331554 (visited on 02/02/2023).

7. W. Du and X. Wu. “Fair and robust classification under sample selection bias.” In: Proceedings of the 30th

8.

9.

10.

11.

ACM International Conference on Information & Knowledge Management. 2021, pp. 2999–3003.
S. Giguere, B. Metevier, Y. Brun, P. S. Thomas, S. Niekum, and B. C. da Silva. Fairness Guarantees under
Demographic Shift. https://github.com/sgiguere/Fairness-Guarantees-under-Demographic-Shift. 2022.
R. Kohavi and B. Becker. UCI Machine Learning Repository: Adult Data Set. 1996. URL: https://archive.ics.
uci.edu/ml/datasets/adult.
B. C. da Silva. UFRGS Entrance Exam and GPA Data. Version V2. 2019. DOI: 10.7910/DVN/O35FW8. URL:
https://doi.org/10.7910/DVN/O35FW8.
B. Strack, J. P. DeShazo, C. Gennings, J. L. Olmo, S. Ventura, K. J. Cios, and J. N. Clore. “Impact of HbA1c
measurement on hospital readmission rates: analysis of 70,000 clinical database patient records.” In: BioMed
research international 2014 (2014).

## 7 Appendix

### 7.1 UFRGS Entrance Exam and GPA dataset

The following section contains the results considering the second dataset used for reproduction of the original experiments as described in section 4.1 and 4.3. In this dataset
sex is used as the fairness attribute, and race as the demographic attribute.
The hyperparameters values used for these experiments are summarised in Table 5.

Constraint
DI
DP

ϵ
‐0.8
0.1

train / test
0.4
0.4

Dc / Df
0.4
0.4

n‐iters
2000
2000

δ
0.05
0.05

α*
0.25
0.25

Table 5. Hyperparameter values for the experiments run with the UFRGS GPA dataset specified for
Disparate Impact (DI) or Demographic Parity (DP) for both a known and unknown demographic
shift. α is only used in the case of an unknown shift.

Shown in figure 4 are the results under a known demographic shift with DP and DI as
the fairness constraints. Results under unknown demographic shift considering DP and
DI as the fairness constraints are shown in figure 5.

7.2 UCI - Adult Census Failure Rates

In this section, the failure rates for each algorithm with the UCI Adult Census dataset, as
mentioned in section 6.1, are provided in Figures 6 and 7.

### 7.3 Numerical Results

The tables in this section (tables 6, 7, 8, and 9) provide numerical results of the accuracy
scores on the experiments run with the UCI Adult Census dataset, as set out in section
6.2.





Figure 4. Results when enforcing fairness constraints under known demographic shift using the
UFRGS GPA dataset. For both fairness constraints DP and DI, the leftmost graph shows the probability of NO_SOLUTION_FOUND, the middle column shows the accuracies, and the rightmost
column shows the failure rates.





Figure 5. Results when enforcing fairness constraints under unknown demographic shift using the
UFRGS GPA dataset. For both fairness constraints DP and DI, the leftmost graph shows the probability of NO_SOLUTION_FOUND, the middle column shows the accuracies, and the rightmost
column shows the failure rates.


Figure 6. Failure rates for each algorithm under unknown demographic shift for fairness constraints DP and DI with the UCI Adult Census dataset. The confidence bound is indicated with
the dotted line.





Figure 7. Failure rate (in percentages) for each algorithm under known demographic shift for fairness constraints DP and DI with the UCI Adult Census dataset. The confidence threshold is indicated with the dotted line.


10k

15k

20k

25k

30k

35k

40k

45k

50k

55k

60k

Accuracy ‐ Known Demographic Shift ‐ Demographic Parity


nan
nan
nan

76.75
73.60
‐3.15

76.70
73.47
‐3.23

74.03
70.91
‐3.12

80.99
78.51
‐2.48

80.99
78.67
‐2.32

nan
nan
nan

76.25
74.11
‐2.14

77.03
74.35
‐2.68

74.39
71.24
‐3.15

81.03
78.55
‐2.48

80.77
78.44
‐2.33

nan
nan
nan

76.31
74.15
‐2.16


76.59
75.30
‐1.29

76.05
72.80
‐3.25

77.17
74.37
‐2.80

77.80
75.19
‐2.61

76.59
74.72
‐1.87

77.91
75.62
‐2.29

77.34
74.66
‐2.68

77.56
74.99
‐2.57

78.10
75.70
‐2.40

78.56
76.60
‐1.96

78.20
75.66
‐2.54

77.38
74.56
‐2.82

74.78
71.76
‐3.02

81.01
78.56
‐2.45

80.71
78.38
‐2.33

78.31
75.96
‐2.35

74.36
71.23
‐3.13

81.05
78.56
‐2.49

74.40
71.25
‐3.15

81.00
78.52
‐2.48

74.11
71.04
‐3.07

80.92
78.46
‐2.46


80.63
78.28
‐2.35

80.60
78.23
‐2.37

80.58
78.23
‐2.35

74.13
71.05
‐3.08

81.03
78.58
‐2.45

80.64
78.29
‐2.35

77.75
75.58
‐2.17

77.99
75.44
‐2.55

78.56
76.43
‐2.13

74.15
71.06
‐3.09

81.04
78.59
‐2.45

80.49
78.15
‐2.34

78.05
75.98
‐2.07

77.99
75.53
‐2.46

78.68
76.42
‐2.26

74.41
71.25
‐3.16

81.12
78.68
‐2.44

80.51
78.19
‐2.32

78.11
76.06
‐2.05

77.93
75.72
‐2.21

78.81
76.67
‐2.14

74.40
71.25
‐3.15

81.02
78.59
‐2.43

80.52
78.17
‐2.35

78.19
76.05
‐2.14

77.95
75.73
‐2.22

78.86
76.69
‐2.17

74.43
71.26
‐3.17

80.98
78.53
‐2.45

80.52
78.16
‐2.36

Table 6. Results table showcasing the numerical mean accuracy percentage of each algorithm, for
both the original distribution and the deployed one when trained under a known demographic
shift with fairness constraint Demographic Parity. The decrease or increase in accuracy is shown
in the rows named ‘Difference’.





10k

15k

20k

25k

30k

35k

40k

45k

50k

55k

60k

Accuracy ‐ Known Demographic Shift ‐ Disparate Impact


65.00
65.65
0.65

67.31
67.30
‐0.01

66.72
66.92
0.20

80.10
77.54
‐2.56

81.00
78.58
‐2.42

81.04
78.70
‐2.34

69.93
69.75
‐0.18

68.49
66.93
‐1.56

71.57
69.32
‐2.25

79.77
77.20
‐2.57

81.05
78.64
‐2.41

81.14
78.81
‐2.33

74.40
73.32
‐1.08

73.60
72.22
‐1.38


74.96
73.57
‐1.39

73.23
71.53
‐1.70

71.50
69.81
‐1.69

76.98
75.45
‐1.53

75.30
73.95
‐1.35

77.01
75.49
‐1.52

74.58
72.79
‐1.79

74.14
72.72
‐1.42

76.02
74.55
‐1.47

76.90
74.91
‐1.99

77.65
75.77
‐1.88

72.95
72.21
‐0.74

79.94
77.35
‐2.59

81.07
78.64
‐2.43

80.66
78.33
‐2.33

75.96
74.05
‐1.91

80.58
78.12
‐2.46

81.01
78.58
‐2.43

80.68
78.16
‐2.52

81.00
78.54
‐2.46

80.60
78.09
‐2.51

81.08
78.67
‐2.41


80.61
78.27
‐2.34

80.64
78.28
‐2.36

80.64
78.27
‐2.37

80.61
78.11
‐2.50

80.98
78.54
‐2.44

80.69
78.34
‐2.35

76.72
75.25
‐1.47

76.90
74.69
‐2.21

77.69
75.80
‐1.89

80.68
78.15
‐2.53

81.07
78.64
‐2.43

80.61
78.25
‐2.36

77.01
75.60
‐1.41

77.03
74.70
‐2.33

78.20
76.38
‐1.82

80.68
78.15
‐2.53

80.97
78.53
‐2.44

80.63
78.27
‐2.36

77.01
75.52
‐1.49

77.32
75.16
‐2.16

78.42
76.87
‐1.55

80.68
78.13
‐2.55

81.03
78.61
‐2.42

80.54
78.16
‐2.38

77.65
76.01
‐1.64

77.29
75.33
‐1.96

78.49
76.70
‐1.79

80.66
78.12
‐2.54

80.99
78.54
‐2.45

80.58
78.21
‐2.37

Table 7. Results table showcasing the numerical mean accuracy percentage of each algorithm, for
both the original distribution and the deployed one when trained under a known demographic
shift with fairness constraint Disparate Impact. The decrease or increase in accuracy are shown
per number of samples in the rows named ‘Difference’

Accuracy ‐ Unknown Demographic Shift ‐ Demographic Parity
60k


10k

20k

40k

30k

50k


79.40
77.49
‐1.91

77.23
76.31
‐0.92

78.74
77.06
‐1.68

79.54
77.67
‐1.87

79.75
77.93
‐1.82

79.66
77.71
‐1.95

78.39
76.95
‐1.44

79.32
77.39
‐1.93

79.23
77.29
‐1.94

79.65
77.61
‐2.04

80.49
78.29
‐2.20

79.70
77.68
‐2.02

78.85
76.65
‐2.20

75.03
72.17
‐2.86

80.28
78.16
‐2.12

74.38
71.47
‐2.91

80.94
78.70
‐2.24

80.92
78.66
‐2.26

80.67
78.47
‐2.20

80.69
78.51
‐2.18

74.40
71.47
‐2.93

80.86
78.61
‐2.25

80.63
78.46
‐2.17

80.61
78.36
‐2.25

75.07
72.19
‐2.88

80.86
78.61
‐2.25

80.60
78.42
‐2.18

75.03
72.17
‐2.86

80.97
78.73
‐2.24

81.02
78.84
‐2.18

80.08
78.03
‐2.05

79.83
77.88
‐1.95

80.68
78.46
‐2.22

75.05
72.19
‐2.86

80.89
78.62
‐2.27

80.58
78.41
‐2.17

Table 8. Results table showcasing the numerical mean accuracy percentage of each algorithm,
for both the original distribution and the deployed one when trained under an unknown demographic shift with fairness constraint Demographic Parity. The decrease or increase in accuracy
is shown in the rows named ‘Difference’.




Accuracy ‐ Unknown Demographic Shift ‐ Disparate Impact


10k

20k

30k

40k

50k

60k


64.66
65.43
0.77

71.92
71.93
0.01

75.22
75.63
0.41

75.74
76.54
0.80

77.17
80.18
3.01

75.61
74.40
‐1.21

52.97
52.36
‐0.61

nan
nan
nan

73.30
73.20
‐0.10

75.09
74.29
‐0.80

77.71
79.09
1.38

74.15
75.56
1.41

67.03
67.31
0.28

80.00
82.78
2.78

76.09
76.82
0.73

80.68
84.24
3.56

80.98
82.14
1.16

80.95
83.26
2.31

80.65
80.00
‐0.65

80.64
79.97
‐0.67

80.68
84.34
3.66

80.96
82.60
1.64

80.55
79.15
‐1.40

77.41
79.14
1.73

80.68
84.15
3.47

81.03
82.00
0.97

80.65
79.56
‐1.09

80.01
82.78
2.77

81.00
83.06
2.06

80.97
81.78
0.81

76.74
79.55
2.81

76.39
74.71
‐1.68

78.17
78.73
0.56

80.69
84.54
3.85

80.98
82.69
1.71

80.52
79.37
‐1.15

Table 9. Results table showcasing the numerical mean accuracy percentage of each algorithm,
for both the original distribution and the deployed one when trained under an unknown demographic shift with fairness constraint Disparate Impact. The decrease or increase in accuracy is
shown in the rows named ‘Difference’.

---
**Source PDF:** `bf6f73b398b7.pdf` (2023_22_article.pdf)  
**URL:** https://zenodo.org/record/8206607/files/article.pdf
