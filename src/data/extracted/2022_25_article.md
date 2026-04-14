R E S C I E N C E C

Replication / ML Reproducibility Challenge 2021
[Re] Projection-based Algorithm for Updating the
TruncatedSVD of Evolving Matrices

Andy Chen1, ID , Shion Matsumoto1, ID , and Rohan Sinha Varma1, ID
1University of Michigan, Ann Arbor, Michigan, USA

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
10.5281/zenodo.6574675

Reproducibility Summary

Scope of Reproducibility

Kalantzis et al. [1] present a method to update the rank‐k truncated SVD of matrices
where the matrices are subject to periodic additions of rows or columns. The main
claim of the original paper states that the presented algorithms outperform other stateof‐the‐art approaches in terms of accuracy and speed. However, no results were given
comparing the proposed methods to other state‐of‐the‐art methods. Accordingly, we
reproduce their results and compare it to the state‐of‐the‐art FrequentDirections
streaming algorithm [2].

Methodology

We re‐implemented the algorithm in Python and evaluated the performance on five
datasets. All experiments were run on a MacBook Pro and the code is available on
GitHub1. The accuracy of the methods were evaluated using the same metrics as in
the paper.

Results

We successfuly reproduced the task‐agnostic experiments of the original paper, finding
our results to strongly match with the original results. We also carried out a comparison
with FrequentDirections but found the evaluation metrics of the original paper to
be ill‐suited to compare ‐ setting up for further work on developing fair comparisons.

What was easy

The benchmark algorithm was fairly simple to implement. Furthermore, running the
experiments did not place any computational resource burden as all experiments could
be run on a laptop.

1https://github.com/andyzfchen/truncatedSVD


Code is available at https://github.com/andyzfchen/truncatedSVD. – SWH swh:1:dir:4116fecf6ec4ac207cdad025ec62b25839a75678.
Open peer review is available at https://openreview.net/forum?id=HN2xWpMQ30K.




What was difficult

The most difficult part of the reproduction study was understanding the justification
underlying the construction of the algorithm as it involved several complex proofs from
numerical linear algebra to provide bounds on the accuracy. Demystifying the specifics
of constructing the projection matrix for the main algorithm the author’s propose was
also initially difficult until we gained access to their code.

Communication with original authors

We contacted one of the authors by email and received their data and MATLAB implementation of the algorithm and experiments.




## 1 Introduction

The singular value decomposition (SVD) remains a fundamental dimensionality reduction technique in machine learning and continues to be used in a variety of applications.
In a traditional formulation, the entirety of the matrix to be decomposed is available
at the time of application of the SVD. However, certain applications, such as latent semantic indexing (LSI) and recommender systems, have matrices that are subject to the
periodic addition of new rows and/or columns. A naïve solution is to recalculate the
SVD each time the matrix is updated, but such an approach quickly becomes impractical when updates are frequent. For this reason, algorithms that exploit information on
the previous SVD of the matrix to calculate the SVD of the updated matrix are crucial.
Such schemes have been proposed for both the full SVD and rank‐k SVD. The algorithm
presented in [1], which is the focus of our study, is for the rank‐k truncated SVD case.
Following the notation introduced in [1], the problem of updating the rank‐k truncated
SVD of an updated matrix is as follows. Let B ∈ Cm×n be a matrix for which a rank‐k SVD
k
j=1 σju(j)(v(j))H where Uk = [u(1), . . . , u(k)], Vk = [v(1), . . . , v(k)],
Bk = UkΣkV H
and Σk = diag(σ1, . . . , σk) where σ1 ≥ σ2 ≥ · · · ≥ σk > 0 is known. The goal is
P
bΣk
to approximate the rank‐k SVD Ak = bUk
bσj bu(j)(bv(j))H of the updated
matrix

k =

k
j=1

P


bV H
k =


A =

, or A =

B E

B
E

where E ∈ Cs×n or E ∈ Cm×s is the matrix containing the newly added rows or columns,
respectively. We focus on the row‐update case in this study as is the case in [1].
The remainder of this study is outlined as follows. In Section 2, we introduce the central
claim of the original paper that we tested in our study. Following that, in Section 3,
we introduce the necessary background prior to describing the proposed algorithm. In
Section 4, we describe the experimental setup: our implementation of the algorithm,
datasets used, and experiments run. We present the experimental results in Section 5
along with our interpretation of the results and thoughts on the overall study in Section
6.

## 2 Scope of reproducibility

In this study, we aimed to verify the central claim of the original paper, which stated
that the proposed algorithm outperforms other state‐of‐the‐art approaches at calculating the truncated SVD of evolving matrices. In particular, they claimed that the method
had especially high accuracy for the singular triplets with the largest modulus singular
values. We sought to verify this claim by evaluating two metrics using our implementation of the method as well as with FrequentDirections, a state‐of‐the‐art matrix
sketching and streaming algorithm [2]:

1. Relative approximation error rel_err of leading k singular values of A (Equation 1) is smaller when using the proposed algorithm compared to previous methods.

rel_err =


bσi − σi
σi


(1)

2. Scaled residual norm res_norm of leading k singular triplets {bu(i), bv(i), bσi} (Equation 2) is smaller when using the proposed algorithm compared to previous meth‐
(cid:13)
ods.
(cid:13)Abv(i) − bσibu(i)
bσi

res_norm =

(2)

(cid:13)
(cid:13)


Additionally, we also sought to verify the original paper’s claims about the runtime performance of the proposed algorithm.


Uk

=


Is

Σk
EVk RH


## 3 Projection-based update algorithm

In the following sections, we first introduce the original zha-simon algorithm, then
introduce the proposed projection‐based update algorithm. Note that there are two implementations to the proposed algorithm: one which uses the same projection matrix
as the zha-simon algorithm (Algorithm 2.1) and another that uses an enhanced projection matrix (Algorithm 2.2).

3.1 Zha-Simon algorithm

As motivated in the introduction, an update algorithm that uses prior knowledge regarding the SVD of the matrix is crucial for it to be useful in practice. The algorithm
proposed in [1] is based on an algorithm proposed in [3], the latter of which we will refer to as the zha-simon algorithm (Algorithm 1). Using zha-simon in the row‐update


B
E

, the QR decomposition of the row space of E that is not captured by the

case A =
range of the right singular vectors Vk can be expressed as (I − VkV H
this result and the previously known rank‐k SVD Bk = UkΣkV H
can be decomposed approximately as follows:


(cid:19) 

(cid:19) 


k )EH = QR. Using
k , the updated matrix A

A =

B
E

≈

UkΣkV H
k
E

Σk
EVk RH

V H
k
QH


(3)

If we let F ΘGH be the compact SVD of

, then Equation 3 can be further

decomposed as follows:


A ≈

Uk


F ΘGH


V H
k
QH


(cid:18)

=

Uk


F

Θ

Is

(cid:0)


(cid:1)H

G

Vk Q

(4)

Is

The key here is to notice that the approximation of the rank‐k truncated SVD of A using the zha-simon algorithm does not require access to the previous matrix B – only
the rank‐k SVD Bk = UkΣkV H
k of the matrix from the previous iteration is needed.
We can further simplify Equation 4 and see that it approximates the SVD of A as A ≈
(ZF )Θ(W G)H where Z =
and W H =
Is
with ranges that approximately capture range( bUk) and range( bV H

are orthonormal matrices

k ), respectively.

Vk Q

(cid:1)H

Uk


Is


Algorithm 1 zha-simon algorithm
Require: A, E, Uk, Σk, Vk, k
1: Z ←

Uk


k )EH

2: [Q, R] ← qr(I − VkV H
3: W ←
Vk Q
4: [Fk, Θk, Gk] ← svd(Z H AW, k)
5: U k ← ZFk
6: Σk ← Θk
7: V k ← W Gk
Ensure: U k ≈ bUk, Σk ≈ bΣk, V k ≈ bVk

Algorithm 2 Proposed row‐update algorithm
Require: B, E, k
1: [Uk, Σk, Vk] ← svd(B, k)
2: Construct projection matrix Z
3: [Fk, Θk] ← svd(Z H A, k) where A =


B
E

4: U k ← ZFk
5: Σk ← Θk
−1
6: V k ← AH U kΣ
k
Ensure: U k ≈ bUk, Σk ≈ bΣk, V k ≈ bVk

### 3.2 Proposed row-update algorithm

In practice, computing the rank‐k truncated SVD of A using Algorithm 1 is expensive due
to the QR (Step 2) and SVD (Step 4) steps and possibly inaccurate based on the structure




of A [1]. The cost of the QR decomposition can be mitigated by setting W = In by
observing that bv(i) ⊆ range(In) for i = 1, . . . , n. Therefore, Z H AW in Step 4 can be
replaced with Z H A and the QR decomposition in Step 2 can be eliminated. With these
modifications, we have the new proposed row‐update algorithm (Algorithm 2). Note that
Step 2 has intentionally not been specified as the authors proposed two options for the
construction of the projection matrix Z.
The first option (Algorithm 2.1) uses the same Z matrix as in Algorithm. Although the
construction of Z and Z H A are presented in two separate steps in Algorithm 2, Z H A for
Step 3 is directly computed as 1. Below are the expressions for Z and Z H A for Algorithm
2.1.


Z =

Z H A =

Uk


Is

ΣkV H
k
E

In the case where the rank of B is larger than k and the singular values σk+1, . . . , σmin(m,n)
are not small, the approximation returned by Algorithm 2.1 can be of poor accuracy. Algorithm 2.2 addresses this by using an enhanced version of the projection matrix by
adding a term −B(λ)BEH in the Z matrix such that


Z =

Uk −B(λ)BEH


Is

(6)

Setting X = −B(λ)BEH , the additional term is equal to the matrix X that satisfies the
equation

−(BBH − λIm)X = (Im − UkU H

k )BEH ,

(7)

which can be computed using the block conjugate gradient (BCG) method [4]. To ensure
that the matrix −(BBH − λIm) is positive definite for BCG, a lower bound of λ > σ2
1 is
imposed. The leading singular value can be estimated using a few iterations of truncated
SVD. However, to reduce the number of columns in X and keep Z manageable, the
randomized rank‐r SVD of X can be taken so that

−B(λ)BEH R ≈ Xλ,rSλ,rY H
λ,r

(8)

where R is a matrix with at least r columns whose entries are i.i.d. Gaussian random
variables with zero mean and unit variance. With Xλ,r, the Z and Z H A matrices can be
calculated as


(5a)

(5b)

(9a)

(9b)

Uk Xλ,r

Z =

Is


A


@

ΣkV H
k
X H
λ,rB
E

Z H A =

For more detailed explanations and derivations of the algorithms and their associated
proofs, we refer readers to [1].

## 4 Methodology

Professor Vassilis Kalantzis, who we contacted via email, generously provided us with
the relevant MATLAB code and data; however, we chose to re‐implement the algorithm
from scratch in Python with standard packages (NumPy [5], SciPy [6], and scikit‐learn
[7]) and used the MATLAB code to confirm our implementation. We compared the performance of Algorithms 2.1 and 2.2 with FrequentDirections [2], a state‐of‐the‐art
streaming algorithm. Experiments were conducted on a MacBook Pro with a 2.3 GHz




Dual‐Core Intel Core i5 processor with 16 GB of RAM, and the code is publicly available
on GitHub2. All plots were generated using Matplotlib [8].

### 4.1 Implementation

We chose to implement the three truncated SVD update algorithms as methods of an
EvolvingMatrix class, which we will refer to as EM from here on out. With each experiment, the EM class was initialized with various parameters (initial matrix, matrix to
be appended, number of batches, etc.) and updates were carried out using one of the update methods. A simplified version of the experiment is shown in Listing 1. Algorithms
2.1 and 2.2 were written based on the pseudo‐code presented in Algorithm 2, where the
Z and Z H A matrices were calculated using their respective formulas.

# Initialize EM object with initial matrix, number of batches, and

desired rank

model = EM(initial_matrix, n_batches, k_dim)

# Set entire matrix to be appended
model.set_append_matrix(E)

# Update over specified number of batches
for i in range(n_batches):

model.evolve()
model.update_svd()

# append rows to matrix
# update truncated SVD

# Calculate metrics for pre-selected updates
if model.phi in phis2plot:

model.calculate_true_svd()
model.save_metrics()

Listing 1. Simplified experiment structure

Algorithm 2.1 The Z and Z H A matrices were constructed as in Equations 5a and 5b,
respectively.

Algorithm 2.2 The main difficulty in implementing Algorithm 2.2 was in the calculation of Xλ,r. We chose to solve for X in Equation 7 using the block Conjugate Gradient method (BCG) [4] as recommended in [1]. Though [1] specified, at maximum, one
iteration of BCG, we found that the MATLAB code set the limit to two iterations. As
the additional iteration did not greatly increase the computational cost, we chose to
run BCG a maximum of two iterations as well. Once X was calculated, we calculated
Xλ,r as per Equation 8 using randomized SVD [9]. For this, we used the scikit‐learn
randomized_svd implementation [7]. Based on the description for calculating Xλ,r
in [1], we set n_components= r, n_oversamples= 2r, and n_iter= 0. The Xλ,r
returned was then used to calculate Z and Z H A as in Equations 9a and 9b, respectively.

Frequent Directions A modified version of FrequentDirections3 was incorporated
as an update method into the EM class. Since FrequentDirections is a line‐by‐line
update method as opposed to a batch update method, the update method in the EM class
was constructed to receive a matrix E containing the rows to be added and performs
the FrequentDirections algorithms for each row of the E. Any form of error metric

2https://anonymous.4open.science/r/truncatedSVD‐0162/
3https://github.com/edoliberty/frequent‐directions




calculation or subsequent update is performed only after the entire matrix E has been
processed using the line‐by‐line update method.
Since the updated matrix B for the FrequentDirections method has constant dimensions throughout the update process, the residual norm error calculation is modified to
measure the error between B and A′ where A′ is a truncated version of A that only holds
the first 2l singular vectors and values of A and where 2l is the number of rows in B.

### 4.2 Datasets

In total, we conducted experiments on five datasets. MED, CRAN, CISI, and Reuters21578 are term‐document matrices from latent semantic indexing applications [10, 11,
12, 13, 14] and ML1M is a movie rating dataset from MovieLens [15]. Table 1 lists the
dimensions of the matrices as well as the average number of nonzero (nnz) entries per
row and Figure 1 shows the leading 100 singular values for each matrix. It should be
noted that the matrices used for CISI, CRAN, and MED in [1] had slightly different dimensions compared to what was listed on [10]. We received these datasets along with
the MATLAB code and chose to use their versions of the data for ease of comparison; as
we were interested in the accuracy of singular value reconstruction we determined that
somewhat corrupted data merely introduced a different set of singular values to reconstruct. Furthermore, as the Reuters and ML1M datasets were intact, we used them as
controls against the corruption of the other sets.

Figure 1. Leading 100 singular values for each dataset.

Dataset

Rows Columns nnz(A)/row

CISI [10]
CRAN [10]
MED [10]
ML1M [15]
Reuters‐21578 [11, 12, 13, 14]

5609
4612
5831
6040
18933

1460
1398
1033
3952
8293

12.17
18.06
8.92
165.60
### 20.57 Table 1. Number of rows, columns, and average non‐zero elements in each row for datasets.




### 4.3 Experiments

We conducted two sets of experiments: one to confirm the results of [1] in a series of reproducibility studies and another to further measure the performance of the algorithms
using two additional metrics as well as observing the effect of the number of batches on
the runtime and performance.

Update method comparison As a first step, we sought to reproduce the results in Figures 3 and 4 of [1]. To do this, we conducted the sequence updates experiment. The
initial matrix B ≡ A(0) was set equal to the first µ rows of A ∈ Cm×n and the remaining m − µ rows of A were appended to the initial matrix over a sequence of ϕ updates,
each with τ = ⌊(m − µ)/ϕ⌋ rows. Following the notation of [1], the i‐th update would
yield A(i) =

with the exception of the last update

B ≡ A(i−1)
E ≡ A(µ + (i − 1)τ + 1 : µ + iτ, :)


which is likely to have fewer rows in E. After each update, the rank‐k truncated SVD
was calculated by one of the three algorithms.
The parameters used in [1], and thus in our experiments as well were µ = ⌈m/10⌉ rows,
ϕ = 10 updates, and rank k = 50. The relative errors and residual norms were reported
for the k = 50 leading singular triplets for ϕ = 1, 5, 10. For Algorithm 2.2, we set the
coefficient λ = 1.01bσ2

1 and r = 10.

Algorithm 2.2 r parameter study Next, we varied the r parameter in Algorithm 2.2 to
evaluate its effect on the accuracy as was presented in Table 4 by [1]. For this, we set
µ = ⌈m/10⌉, ϕ = 10, and k = 50 for all three update methods as with the previous
experiment and set r = 10, 20, 30, 40, 50 for Algorithm 2.2.

Runtime comparison We compared the runtimes of the algorithms for the CRAN, CISI,
and MED as a function of the rank k = 25, 25, 50, 75, 100, 125 and the total number of
updates ϕ = 2, 4, 6, 8, 10 (Figure 2 left and middle plots in [1]).

Varying number of batches and desired rank In addition to the experiments that we
replicated based on [1], we also varied the number of batches ϕ = 2, 4, 6, 8, 10 and the
desired rank k = 25, 50, 75, 100, 125 of the truncated SVD and evaluated the performance
of each of the update methods to further observe the effects of each of these parameters
on the methods’ performances.

## 5 Results

Relative error and residual norms of singular triplets The relative error and residual
norm of the leading k = 50 singular triplets for the CRAN dataset at ϕ = 1, 5, 10 using Algorithms 2.1, 2.2, and FrequentDirections are shown in Figure 2. Due to the
large number of figures, the complete set of plots for the standard experiments are presented in Sections A to E in the Supplementary Materials. When comparing the relative
error and residual norm plots for Algorithm 2.1 on CRAN, CISI, and MED, our results
matched those of [1] exactly. For Algorithm 2.2, the plots did not match exactly, though
the differences never exceeded half an order of magnitude and are attributable to the
randomness inherent in Algorithm 2.2.
Our comparison of the relative error and residual norm of the k = 50‐th singular triplet
for Algorithm 2.2 with various values of r revealed a similar result to [1] – across the
three methods, Algorithm 2.2 had the lowest errors, and within variations of Algorithm
2.2, larger values of r yielded higher accuracy.




(a) CRAN relative error (Alg. 2.1)

(b) CRAN relative error (Alg. 2.2)

(c) CRAN relative error (FD)

(d) CRAN residual norm (Alg. 2.1)

(e) CRAN residual norm (Alg. 2.2)

(f) CRAN residual norm (FD)

Figure 2. Relative errors and residual norms at ϕ = 1, 5, 10 for CRAN with Algorithm 2.1, Algorithm
2.2, and FD.

MED

CRAN

CISI

err.
0.037
0.028
0.021
0.015
0.013

res.
0.204
0.172
0.154
0.133
0.121

err.
0.031
0.021
0.012
0.010
0.008

res.
0.174
0.144
0.113
0.107
0.097

err.
0.038
0.019
0.014
0.011
0.009

res.
0.224
0.149
0.119
0.105
0.096

0.101

0.294

0.074

0.295

0.080

0.382

0.212

1.031

0.216

1.045

0.205

1.032

r


–

–


Z =

Uk Xλ,r


Uk

Z =

Is


Is


FrequentDirections

Table 2. Relative error and residual norm of approximation of the singular triplet (bu(50), bv(50), bσ50)

Runtime For all three of the datasets which we measured runtimes on, we found Algorithm 2.2 to require a substantially longer amount of time to complete all of its updates.
Algorithm 2.1 and FrequentDirections required a similar length of time, though
Algorithm 2.1 was consistently faster than FrequentDirections by a small margin.
The runtime plots for the standard experiments are shown in Section F of the Supplementary Materials.

Number of batches and rank Due to space‐related constraints, we chose to only include two examples from the array of plots generated (Figure 4). Despite the large variation in the parameters, we can see that the residual norm for overlapping update numbers and k share very similar values.




(a) Runtime vs. k

(b) Runtime vs. number of batches

Figure 3. CRAN runtimes as a function of rank k (left) and number of batch splits (right).

(a) 6 batches, k = 50

(b) 10 batches, k = 100

Figure 4. Examples of residual norm for experimental parameters outside of what was investigated
by [1].

## 6 Discussion

Ultimately, the reproduced results confirm the original results. Specifically, Table 2
verifies that Algorithm 2.2 outperforms Algorithm 2.1 in terms of accuracy. Furthermore, Figure 3 clearly demonstrates that Algorithm 2.1 far outperforms Algorithm 2.2
with respects to wall clock speed. However, as there were no benchmarks, we viewed
the comparison with FrequentDirections as a much stronger barometer. At first
glance, Table 2 and Figures 2c and 2f suggest that both Algorithm 2.1 and 2.2 outperform
FrequentDirections in terms of accuracy. However, upon considering the steps involved in FrequentDirections (namely the step involving the thresholding of the singular values), we realize that the relative error and residual norm of singular triplets may
not be an applicable metric for FrequentDirections. This is further demonstrated
by the irregular profile of the residual norm as a function of the singular value index
(Figure 2f)). Thus it cannot conclusively be said that FrequentDirections is significantly under‐performing the paper’s proposed algorithms. Consequently, the overall
conclusion becomes that while the results presented in the paper are sound, there is
still need for further benchmarking to determine where the proposed algorithms stand
relative to the state‐of‐the‐art in the field.




### 6.1 Future Work

We believe a weakness of the paper to be the lack of benchmarking ‐ and as discussed
above, our results do not conclusively resolve this. However, they do motivate the need
for metrics that will allow for a fair comparison between the proposed algorithm and
state‐of‐the‐art algorithms such as FrequentDirections.

### 6.2 What was easy

Algorithm 1.1 was quite simple to understand and implement, and was exactly reproduced quite early on. Once we received code, implementation of Algorithm 2.2 and the
evaluation metrics was simplified.

### 6.3 What was difficult

In addition to the challenges constructing Xλ,r for Algorithm 2.2, another challenging/timeconsuming aspect was designing the experiments as sweeping through various combinations of the parameters required thorough planning for data management.

References

1.

V. Kalantzis, G. Kollias, S. Ubaru, A. N. Nikolakopoulos, L. Horesh, and K. L. Clarkson. “Projection techniques
to update the truncated SVD of evolving matrices with applications.” In: Proceedings of the 38th International
Conference on Machine Learning. Ed. by M. Meila and T. Zhang. PMLR, July 2021, pp. 5236–5246. URL: https:
//proceedings.mlr.press/v139/kalantzis21a.html.

2. M. Ghashami, E. Liberty, J. M. Phillips, and D. P. Woodruff. “Frequent Directions: Simple and Deterministic Matrix
Sketching.” In: SIAM Journal on Computing 45.5 (Jan. 2016), pp. 1762–1792. DOI: 10.1137/15M1009718. URL:
http://epubs.siam.org/doi/10.1137/15M1009718.

4.

3. H. Zha and H. D. Simon. “Timely communication on updating problems in latent semantic indexing.” In: Society
for Industrial and Applied Mathematics 21.2 (1999), pp. 782–791. URL: http://www.siam.org/journals/sisc/21-
2/32926.html.
D. P. O’Leary. “The block conjugate gradient algorithm and related methods.” In: Linear Algebra and its Appli-
cations 29 (Feb. 1980), pp. 293–322. DOI: 10.1016/0024-3795(80)90247-5. URL: https://linkinghub.elsevier.
com/retrieve/pii/0024379580902475.
C. R. Harris et al. Array programming with NumPy. Sept. 2020. DOI: 10.1038/s41586-020-2649-2.
P. Virtanen et al. “SciPy 1.0: fundamental algorithms for scientific computing in Python.” In: Nature Methods
17.3 (Mar. 2020), pp. 261–272. DOI: 10.1038/s41592-019-0686-2.
F. Pedregosa et al. “Scikit-learn: Machine Learning in Python.” In: Journal of Machine Learning Research 12.85
(Oct. 2011), pp. 2825–2830.
J. D. Hunter. “Matplotlib: A 2D Graphics Environment.” In: Computing in Science Engineering 9.3 (2007), pp. 90–
95. DOI: 10.1109/MCSE.2007.55.

5.
6.

8.

7.

9. N. Halko, P. G. Martinsson, and J. A. Tropp. “Finding structure with randomness: Probabilistic algorithms
for constructing approximate matrix decompositions.” In: SIAM Review 53.2 (2011), pp. 217–288. DOI:
10.1137/090771806.

12.

10. M. W. Berry and S. T. Dumais. Latent Semantic Indexing Web Site. URL: http://web.eecs.utk.edu/research/lsi/.
D. Cai, X. He, and J. Han. “Document clustering using locality preserving indexing.” In: IEEE Transactions on
11.
Knowledge and Data Engineering 17.12 (Dec. 2005), pp. 1624–1637. DOI: 10.1109/TKDE.2005.198.
D. Cai, X. He, W. V. Zhang, and J. Han. “Regularized locality preserving indexing via spectral regression.” In:
Proceedings of the sixteenth ACM conference on Conference on information and knowledge management - CIKM
’07. New York, New York, USA: ACM Press, 2007, p. 741. DOI: 10.1145/1321440.1321544.
D. Cai, Q. Mei, J. Han, and C. Zhai. “Modeling hidden topics on document manifold.” In: Proceeding of the 17th
ACM conference on Information and knowledge mining - CIKM ’08. New York, New York, USA: ACM Press, 2008,
p. 911. DOI: 10.1145/1458082.1458202.
D. Cai, X. Wang, and X. He. “Probabilistic dyadic data analysis with local and global consistency.” In: Proceedings
of the 26th Annual International Conference on Machine Learning - ICML ’09. New York, New York, USA: ACM
Press, 2009, pp. 1–8. DOI: 10.1145/1553374.1553388. URL: http : / / portal . acm . org / citation . cfm ? doid =
1553374.1553388.

13.

14.




15.

F. M. Harper and J. A. Konstan. “The movielens datasets: History and context.” In: ACM Transactions on Inter-
active Intelligent Systems 5.4 (Dec. 2015). DOI: 10.1145/2827872.

---
**Source PDF:** `7215de2b76e1.pdf` (2022_25_article.pdf)  
**URL:** https://zenodo.org/record/6574675/files/article.pdf
