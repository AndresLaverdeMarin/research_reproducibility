R E S C I E N C E C

Replication / Education Policy


Tristan Allard1, ID , Louis Béziaud1,2, ID , and Sébastien Gambs2, ID
1Univ Rennes, CNRS, IRISA, Rennes, France – 2Université du Québec à Montréal, Montréal, Canada

Edited by
Olivia Guest ID

Reviewed by
Lukas Wallrich ID
Cosima Meyer ID

Received
17 March 2022

Published
16 November 2023

DOI
10.5281/zenodo.10255347

Abstract

Assessing the impact of public policies, e.g., affirmative actions for college admission, is crucial to understand the impact of high stake decisions on society but
real‐life experiments are complex and can pose ethical challenges hard to overcome.
Statistical models and computerized simulations might be valuable tools for circumventing both the complexity and the ethical issues in these contexts. Reardon et al.
have recently proposed a statistical agent‐based model for observing the impact of
affirmative actions on college admissions. In this paper, we present the results obtained by trying to re‐implement their model and to replicate their results. In a nutshell, while we have been able to replicate the main trends observed in the original
paper, the original results and the replicated results diverge slightly, at least partly
due to unspecified or inconsistent parameters. The reproduction task has been made
harder by the unavailability of the code. Our code is written in Python and fully documented. We make it available online for facilitating additional experiments with
this sociotechnical system.

## 1 Introduction

The work of Reardon et al. [1] assesses the impact of different college admission policies
on the probability of various ethnic groups to be admitted using an agent‐based simulation model with parameters “grounded in real‐world”. Real‐life experiments over such
sociotechnical systems are complex and costly to setup and run over a long time period
(e.g., years) and can in general only be done over limited pilot projects. By enabling computational experiments over college admission policies, Reardon et al. provides a useful
environment for researchers focusing on the fairness issues related to the deployment
and use of artificial intelligence algorithms. The proposed model is discussed in great
length in the original paper, thus providing a solid basis for understanding it. However, the code of this simulation model is not publicly available. In addition, when
re‐implementing the model, we have faced several issues related to important parts of
the model. First, some values of parameters were missing–e.g., initial colleges’ quality–
while others were used inconsistently along the paper–such as affirmative actions. For
example, the weight of socioeconomic affirmative action is either applied linearly in accordance with the student’s resources or with each decrease of one standard deviation
in students’ resources. Second, some parameters described–in natural language–in the
paper were actually unused by the model. We tried to guess the appropriate formulas
to fit the results and the model description of the original paper. Nonetheless, we were
able to guess their probable values in most cases by trying and comparing our results
with those reported in the paper, thus following a trial and error strategy. Although we


Code is available at https://github.com/lbeziaud/mosaic. – SWH swh:1:rev:4691a01b439094fc2460717d1a6944ce80c27d09.
Open peer review is available at https://github.com/ReScience/submissions/issues/64.




did not succeed in replicating all the results, the experiments present similar overall
trends. This paper describes in details our replication attempt.

## 2 Model of college admissions

Reardon et al. [1] proposes an agent‐based simulation of the college admission process,
mainly based on the model described in previous work [2], with the addition of a racial
attribute to students and the inclusion of positive discrimination policies. Note that data
of [1], [2], and of our replication is fully simulated. We provide below a brief overview of
the model, referring the interested reader to the original paper for more details. Tables 2
and 3 list the main constants and parameters of the model.
The model consists in two sets of agents: colleges and students. A new population of
10,000 students is randomly drawn (see Table 1) at each iteration, in which one iteration
corresponds to one year. The 40 colleges are kept for the complete simulation and evolve
according to the admissions.
Each iteration is composed of three steps:

Application step. Students decide on the “best” subset of colleges to apply by taking into
account their probability of admission depending on their academic achievement
and on each college’s quality, with a noisy perception of variables varying with financial resources. That is, “high‐resources families have better information about
college quality” ([1]). To mimic societal biases, both academic achievements and
financial resources depend on the race attribute.

Admission step. Colleges rank applications based on noisy version of academic achievements and accept a number of top students based on the historical acceptance rate.
College aim at enrolling 150 students.

Enrollment step. Students enroll into the best college in which they are admitted.

At the end of each iteration, the colleges’ admission rate and quality as well as their
probability of admission are updated.
Starting from year 15 (the previous years are used for model convergence), positive discrimination policies are put in place by a subset of colleges. More precisely, three type
of policies can be introduced:

Socioeconomic‐based affirmative action. During admission, colleges favor low‐income

students by increasing their perceived academic achievement.

Race‐based recruiting. During application, students from minority groups favor colleges by increasing their perceived quality, increasing the likelihood of an application.

Race‐based affirmative action. During admission, colleges favor students from minor‐

ity groups by increasing their perceived academic achievement.

The original experiments are concerned with the impact of using socioeconomic‐based
(SES) affirmative action combined with race‐based recruiting instead of race‐based affirmative action. The former two are therefore mostly used together by the colleges.

## 3 Method

We have mostly followed the detailed description of the model given in [1, Appendix C].
We have also referred to [2], which is often cited by the authors as an inspiration for
this work. Code for this latter model is available in the (proprietary) Stata programming




Race

Achievement,
Resources

P(Admission)

Applications

Quality

Admissions

Enrollment

Figure 1. Simplified causal model of [1] with most of the variables being abstracted away. Students’
variables are orange , colleges’ variables are purple , while final variables defined for pairs of
student and college have both colors. Dashed arrows represent dependency over past iterations.

Race

Asian
Black
Hispanic
White

Weight

Resources
Achievement
5% N (1038, 2022)
N (0.012, 0.8332)
15% N (869, 1692) N (−0.224, 0.6662)
20% N (895, 1852) N (−0.447, 0.6912)
N (0.198, 0.6572)
60% N (1052, 1862)

corr(Ach, Res)

0.441
0.305
0.373
0.395

Table 1. Student population

Description

Value

Number of colleges
Number of students
College capacity
Expected yield window
Admission probability window
Introduction of policies


10000
150 students / college
up to 3 years (after first year)
5 years (after 5th year)
15th year

Table 2. Fixed model parameters

language [3]. We have read this code for clarification but we were not able to run it1. We
have contacted the first two authors of [1] (Sean F. Reardon and Rachel Baker) in May
2021 but got no answer as of May 2022.
For our implementation, we have used the Python programming language, with most
of the processing done using NumPy. We use scikit‐learn for the logistic regression2.
We have experimented with the Xarray library, which provides labeled multidimensional arrays. Our motivation was to deduplicate the join between students and colleges.
However, we have achieved no storage or time improvement by doing so.
In addition to the replication effort, we focused on execution speed to be able to use the
model as a synthetic data generator in other works. For this purpose, random data for
all future iterations is drawn at initialization.

1Executing this model seems to require Stata version 11, but the dependency “college sorting

napps.do” is not distributed in the archive.

2We also used statsmodels during development however its interface was less suitable to a pre‐

parametrized model, which we require for the first 5 iterations.




## 4 Difficulties

In this section, we present the main issues encountered with respect to the description
of the model in the original paper [1]. Hereafter, inconsistent descriptions are quoted
but we refer the reader to the full paper for more context. Afterwards, we describe the
interpretation that we have followed for the results presented in this paper.

Socioeconomic status (SES)‐based affirmative action.

• “It is during the calculation of A∗∗

cs that colleges with an affirmative action policy
apply additional weight to a student’s perceived admissions desirability in accordance with that policy. This additional weight is captured by the term Tc × [G ×
(Blacks | Hispanics)+H ×resourcess]. In this term, Tc indicates whether a college
has an affirmative action policy, […] H is the size of the weight given to students
under SES‐based affirmative action policies, which is applied linearly in accordance
with the student’s resources, resourcess.” ([1, Section 3])

• “SES‐affirmative action (corresponding to an increase in admissions consideration
of 0, 50, 100 and 150 achievement points for each decrease of one standard deviation in
applicants’ resources);” ([1, Section 4]).

Using H ×resourcess as in the first quote would advantage high‐income students, which
is the opposite of the objective. Moreover, the weight would not follow the description
of the next two quotes, which involve the standard deviation. In our implementation, a
weight H × max(−zscore(resourcess), 0) is added to the score of low‐income students,
with zscore being the standard score3 with respect to resources, and H the size of the
weight (e.g., 0, 50, 100 and 150). We keep only negative values of the standard score (see
Figure 13 for a version without truncation) to impact only low‐income students (“for
each decrease of one standard deviation”). Note that our interpretation is not totally
satisfactory (see Section 6), however we had no success either with the formula of the
first quote (see Figure 12).

Quality and own achievement reliability.

• “Quality reliability and own achievement reliability bounded by minimum values of

0.5 and maximum values of 0.9.” ([1, Table 1])

• “the reliability of student perceptions of their own achievement, is a function of

student resources and bounded between 0.5 and 0.9” ([1, Appendix C])

• “the reliability of student perceptions of college quality, is a function of student

resources and bounded between 0.5 and 0.7” ([1, Appendix C])

We assume that 0.7 is a typo and clip the values between 0.5 and 0.9. The impact is
however quite negligible (compare Figures 4 and 14).

“Colleges’ binary recruitment statuses (Sc)—which had preRace‐targeted recruiting.
viously all been 0—are set based on model parameters that determine which colleges will
use recruitment […] Utility is then calculated using model‐specific recruitment magnitude values (L): U ∗
There is no use of Sc in the document apart from the definition, and Rsc is also not
defined. We assume that it is a typo and that Sc is to be understood as Rsc. The recruitment magnitude value L is not used (but is an experimental parameter later). No
specific definition of race‐targeted recruitment is given but from “Recruitment efforts

cs + Rsc. ” ([1, Appendix C])

cs = as + bs × Q∗

3The zscore variable is the number of standard deviations by which the value of a raw score is above or

below the mean value of what is being observed or measured




work in part by making students aware of specific colleges and by making these colleges
seem more appealing to prospective students through additional, targeted contact with
those students.” ([1, Section 3]) our understanding is that targeted groups have an increased chance of applying to colleges using race‐targeted recruitment. However, the
race attribute is not used in conjunction with L.
We assume that the race‐targeted recruitment weight is added to the perceived utility of
attending colleges for minority students, such that

cs = as + bs × Q∗
U ∗

cs + R × (Blacks | Hispanics) × T ′

c

in which T ′
recruitment weight.

c indicates whether a college uses race‐targeted recruitment and R is the

Quality update window.
the previous year or on the past five years:

It is unclear whether the quality of colleges depends only on

• “Colleges’ quality values (Qc) are updated based on the incoming class of enrolled stu-
dents before the next year’s cohort of students begins the application process” ([1,
Appendix C]).

• “College quality is calculated as the five-year running average of enrolled student cal‐

iber.” ([1, Figure C5])

The later point is given in the caption of a figure, whereas the first is part of the model
description. Using only the previous year to update colleges’ quality gives satisfying
results (see Figure 5). Thus, we assume that the five‐year running average is not used
for the model but only to smooth the plots.

Initial college quality.
but the values of the mean and variance are not given. We relied on the values from [2]:
Q ∼ N (1070, 1302).

“Initial college quality (Q) is normally distributed” ([1, Appendix C]),

Admission probability estimation. After the fifth iteration, each iteration requires fitting a logistic model on submitted application over the past five years. This allows students to estimate their probability of admission into each colleges, which is required for
them to select a subset to apply to.
Apart from a significant speed increase, we observe no difference when fitting on the
previous year only (and using the previously fitted model’s parameters to initialize the
new fit). However, our code still uses the past five years.

Weights of affirmative actions and targeted recruitment.
“moderate SES‐based affirmative action and moderate race‐based recruitment, which corresponds to a weight of 100
and 75, respectively.” ([1, Figure C3])
“strong SES‐based affirmative action and strong race‐based recruitment, which corresponds to a weight of 100 and 75, respectively.” ([1, Figure C3])

## 5 Experiments

Figures 2 to 11 present side by side examples of reproduction, with plots taken from the
preprint version [4] of the original paper [1] (due to copyright issues) along with our replication results. We attempt to replicate a representative subset of the plots, covering the
gist of the model: impact of race‐based affirmative action (Figures 3, 10, 11) and impact
of SES‐based affirmative action and race‐based recruitment (Figures 4 to 9). Additional




replications are available in Appendix B. Table 3 describes the available parameters and
the values used in the experiments.
Figures 8 to 11 present the impact of the different strategies on the final (years 25 to
29) composition–racial and socioeconomic4–of enrolled students in colleges. Our replication effort involved experimenting with the full set of plots presented in the original paper. We also resorted to additional plots (not presented in the original paper or
the current one) to assess the correlation between admission probability and academic
achievement. Every experiment results from an average of 10 runs.

Description

Domain

Number of years
Number of top colleges implementing policy
Race‐based affirmative action weight
SES‐based affirmative action weight
Race‐based recruiting weight

30, 50
0, 4
0, 150, 300, 260
0, 50, 75, 100, 150
0, 25, 50, 100

Table 3. Experimental parameters

## 6 Results

Our objective was to replicate the overall tendencies of the model. We compare below
our replicated results to the original results.

Figure 2: success. The results without using positive discrimination policy presented
on Figure 2 are similar to the original paper. The first years appear to exhibit a
reversed trend. This could be due to difference in the way the logistic regression
is being fitted.

Figure 3: partial success. Figure 3 shows that we replicated the main trends but still
indicates an issue with race‐based affirmative action: our replication leads to a
greater impact on minority students.

Figure 4: partial success. Looking at Figure 4, the combination of SES‐based affirmative
action and race‐based recruitment is satisfactory in terms of range but the average
impact on minority students is lower than the original. This is also the case with
Figure 15 in Appendix B which considers the same parameters. However, racebased and SES‐based affirmative actions use the same mechanism, which leads us
to believe that race‐based recruitment is successfully replicated with a potential
issue for SES‐based affirmative (as with Figure 3).

Figure 5: success. The behavior of quality on Figure 5 is similar to the original paper,
indicating the adequacy of our quality initialization. A strong claim in the original
paper is the decline in quality of colleges using policies, which is not as clear in
our replication as only two of the four active colleges suffer such decline. This
might be attributed to the lower impact of our actions, as highlighted by the other
figures.

Figure 6: partial success. Figure 6 suffers from the same issue of affirmative actions as
Figure 3, but the general behavior is similar to the paper. Figures 16 and 17 in Appendix B present the same plot for minority and low‐income students with varying
number of active colleges.

4Our socioeconomic distribution is represented by the quintiles of the full students’ resources distribution

(not only the enrolled students) as doing otherwise results in incomparable categories.




(a) Original (reprinted from [4, Figure C1])


Figure 2. Minority enrollment without using affirmative action or recruiting.

(a) Original (reprinted from [4, Figure C2])


Figure 3. Minority enrollment with the top four colleges using real‐world race‐based affirmative
action (weight of 260).

(a) Original (reprinted from [4, Figure C4])


Figure 4. Minority enrollment with the top four colleges using strong SES‐based affirmative action
(weight of 150) and strong race‐based recruitment (weight of 100).


01020304050Year0.050.100.150.200.250.300.350.40Percent minority01020304050Year0.050.100.150.200.250.300.350.40Percent minority01020304050Year0.00.10.20.30.4Percent minority

(a) Original (reprinted from [4, Figure C5])


Figure 5. College quality with the top four colleges using strong SES‐based affirmative action
(weight of 150) and strong race‐based recruitment (weight of 100).

(a) Original (reprinted from [4, Figure D1])


Figure 6. Mean achievement and proportion low‐income with top four colleges using (respectively
not using) strong SES‐based affirmative action (weight of 150) and strong race‐based recruitment
(weight of 100) on the left sides, and real‐world race‐based affirmative action (weight of 260) on the
right sides. Arrows start at a college’s position in year 14 when it was not using affirmative action,
and end at the college’s position in year 29. The left‐most arrow (in red on our figures) captures
students who do not enroll.


01020304050Year80090010001100120013001400College quality8001000120014000.00.10.20.30.40.50.64 schools use SES AA and race recruiting8001000120014004 schools use race AAMean achievement of enrolled studentsProportion low-income students

(a) Original (reprinted from [4, Figure 2])


Figure 7. Black and Hispanic enrollment in colleges using SES‐based affirmative action and racebased recruitment, as a share of estimated enrollment under race‐based affirmative action (using
estimated real‐world affirmative action weight 260).

(a) Original (reprinted from [4, Figure A2])

(b) Reproduction

Figure 8. Racial composition of colleges using SES‐based affirmative action and race‐based recruitment, by affirmative action and recruitment weights.


0.00.20.40.60.81.01.21.4Relative enrollmentRace recruit=0Race recruit=25Race recruit=50SES AA=150Race recruit=1000.00.20.40.60.81.01.21.4Relative enrollmentSES AA=1000.00.20.40.60.81.01.21.4Relative enrollmentSES AA=50BlackHispanicRace0.00.20.40.60.81.01.21.4Relative enrollmentBlackHispanicRaceBlackHispanicRaceBlackHispanicRaceSES AA=0025050010075257550751001502515050150100SES AA / race recruit020406080100PercentBlackHispanicAsianWhite

(a) Original (reprinted from [4, Figure A3])

(b) Reproduction

Figure 9. Socioeconomic composition of colleges using SES‐based affirmative action and racebased recruitment, by affirmative action and recruitment weights.

(a) Original (reprinted from [4, Figure A4])

(b) Reproduction: racial composition

Figure 10. Racial composition of colleges using SES‐based and racial affirmative actions, by affirmative action weights.

(a) Original (reprinted from [4, Figure A5])

(b) Reproduction

Figure 11. Socioeconomic composition of colleges using SES‐based and racial affirmative actions,
by affirmative action weights.


025050010075257550751001502515050150100SES AA / race recruit020406080100PercentQ1Q2Q3Q4Q5000150030075075150753001500150150150300SES AA / Race AA020406080100PercentBlackHispanicAsianWhite000150030075075150753001500150150150300SES AA, Race AA020406080100PercentQ1Q2Q3Q4Q5

It is important to note that this figure corresponds to an average over 10 runs (as
the original paper), which requires the colleges to be sorted by quality.

The additional left‐most arrow covers students who do not enroll. It is unspecified however whether it captures students who do not enroll while having applied,
being admitted or without condition. We use the latter (see Appendix C).

Figure 7: partial success. Figure 7 shows a successful replication of the general tendency
of the model (i.e., the relative values) and a failure in replicating the absolute numbers, probably due to the issue related to the affirmative action observed above.

Figures 8 and 9: partial success. Figures 8 and 9 shows a successful replication regarding the racial impact of targeted recruiting and SES‐based affirmative action strategies, but highlight an issue with the socioeconomic composition (Figure 9). Indeed
the impact of our SES‐based affirmative action is higher than the original paper.

Figures 10 and 11: partial success. Figures 10 and 11 lead to the same observation that
SES‐based affirmative action is not behaving as the original paper. However racebased affirmative action is satisfactory. Note that the combinations (race weight =
150, SES weight = 150) and (race weight = 300, SES weight = 75) are not presented
in the original paper.

## 7 Conclusion

In this paper, we presented our attempt at replicating the model presented by Reardon
et al. [1]. The overall behavior is successfully reproduced, with discrepancies regarding
the impact of positive discrimination policies. We attribute the later to issues with our
understanding of the paper, thus highlighting the difficulties of describing and understanding complex systems, and the need for open‐access to code. The resulting implementation, while not producing results entirely faithful to the ones from the original
paper, can still be useful to simulate data grounded in real‐world in the context of college admission. An extension of this work might consider studying other policies and
their interactions, for example with change in policy over time. We believe however that
more efforts are required for this replication to be completely successful–particularly
on identifying the sources of the discrepancies–however we hope that this goes towards
bridging the gap between computer science and social sciences.

Acknowledgments

We would like to warmly thank the reviewers for their thoughtful comments and efforts
towards improving our code and manuscript. This work was partially funded by the
PROFILE‐INT project funded by the LabEx CominLabs (ANR‐10‐LABX‐07‐01). Sébastien
Gambs is supported by the Canada Research Chair program, a Discovery Grant from
NSERC as well as the NSERC‐RDC DEEL project.




A SES-based affirmative action with alternative assumptions

Figure 12. Minority enrollment with the top four colleges using strong SES‐based affirmative action
(weight of 150) and strong race‐based recruitment (weight of 100) using the formula provided in [1]
for the SES-based affirmative action. See Section 4

Figure 13. Minority enrollment with the top four colleges using strong SES‐based affirmative action
(weight of 150) and strong race‐based recruitment (weight of 100) with penalization of high-income
students (no truncation to ≥ 0). See Section 4


01020304050Year0.050.100.150.200.250.300.350.40Percent minority01020304050Year0.00.10.20.30.40.50.60.7Percent minority

Figure 14. Minority enrollment with the top four colleges using strong SES‐based affirmative action
(weight of 150) and strong race‐based recruitment (weight of 100) truncating reliability of student
perceptions of college quality to 0.7. See Section 4

B Additional figures

Figure 15. “Changes in Black and Hispanic Enrollment over Time with Top 4 Colleges using Moderate SES‐Based Affirmative Action and Moderate Race‐Based Recruiting” ([4, Figure C3])


01020304050Year0.00.10.20.30.4Percent minority01020304050Year0.050.100.150.200.250.300.350.40Percent minority

Figure 16. “The mean achievement and proportion minority by number of schools using admissions policies.” ([4, Figure D2])

Figure 17. “The mean achievement and proportion low‐income by number of schools using affirmative action.” ([4, Figure D3])


0.00.20.40.64 schools use SES AA and race recruiting10 schools use SES AA and race recruiting8001000120014000.00.20.40.620 schools use SES AA and race recruiting80010001200140040 schools use SES AA and race recruitingMean achievement of enrolled studentsProportion minority students0.00.20.40.64 schools use SES AA and race recruiting10 schools use SES AA and race recruiting8001000120014000.00.20.40.620 schools use SES AA and race recruiting80010001200140040 schools use SES AA and race recruitingMean achievement of enrolled studentsProportion low-income students

C Conditional un-enrollment

Condition Mean achievement

Prop. minority students

Prop. low‐income students

None
Applied
Admitted

Original

990.01
979.33
1177.59
∼ 800

0.35
0.36
0.17
∼ 0.6

0.60
0.59
0.40
∼ 0.5

Table 4. Values for Figure 6 (red arrow only) when considering students who do not enroll without
condition, while having applied, or while being admitted. The last row displays the values from
the original figures. Restricting to student having applied gives similar results as having no condition, while capturing only students with an admission gives values further to the original ones.




References

1.

2.

3.

4.

S. F. Reardon, R. Baker, M. Kasman, D. Klasik, and J. B. Townsend. “What Levels of Racial Diversity Can Be
Achieved with Socioeconomic-Based Affirmative Action? Evidence from a Simulation Model.” In: Journal of
Policy Analysis and Management 37.3 (2018), pp. 630–657. DOI: 10.1002/pam.22056. URL: https : / / cepa .
stanford.edu/content/what-levels-racial-diversity-can-be-achieved-socioeconomic-based-affirmative-action-
evidence-simulation-model.
S. F. Reardon, M. Kasman, D. Klasik, and R. Baker. “Agent-based simulation models of the college sorting pro-
cess.” In: Journal of Artificial Societies and Social Simulation 19.1 (2016), p. 8. DOI: 10.18564/jasss.2993. URL:
https://cepa.stanford.edu/content/agent-based-simulation-models-college-sorting-process.
S. F. Reardon, M. Kasman, D. Klasik, and R. Baker. Agent-based Simulation Models of the College Sorting
Process. Version 1.0.0. May 23, 2014. URL: https://www.comses.net/codebases/4220/releases/1.0.0/.
S. F. Reardon, R. Baker, M. Kasman, D. Klasik, and J. B. Townsend. “What Levels of Racial Diversity Can Be
Achieved with Socioeconomic-Based Affirmative Action? Evidence from a Simulation Model (CEPA Working
Paper No.15-04).” In: (Dec. 2017). Retrieved from Stanford Center for Education Policy Analysis. URL: http://
cepa.stanford.edu/wp15-04.

---
**Source PDF:** `c91776a2f2ba.pdf` (2023_03_article.pdf)  
**URL:** https://zenodo.org/record/10255347/files/article.pdf
