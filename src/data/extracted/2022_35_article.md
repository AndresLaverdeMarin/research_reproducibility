R E S C I E N C E C

Replication / ML Reproducibility Challenge 2021


Nick Rucks1, ID , Tobias Uelwer1, ID , and Stefan Harmeling1, ID
1Heinrich Heine University, Düsseldorf, Germany

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
10.5281/zenodo.6574695

Reproducibility Summary

Scope of Reproducibility

This report reproduces the experiments and validates the results of the ECCV 2020 paper
”Solving Phase Retrieval with a Learned Reference” by Hyder et al. [1]. The authors consider the task of recovering an unknown signal from its Fourier magnitudes, where the
measurements are obtained after a reference image is added onto the signal. In order
to solve this task a novel, iterative phase retrieval algorithm, presented as an unrolled
network, that can train a such reference on a small amount of data is proposed. It is
shown that the learned reference generalizes well to unseen data distributions and is
robust to spatial data augmentation like shifting and rotation.

Methodology

We use the provided original code to reproduce the experiments from Hyder et al. [1]
that validate the proposed claims. Nevertheless, we refactor the code base to accelerate
the performance and we extent it to carry out experiments where no code is available.
We perform a hyperparameter search to investigate the influence and optimal values
of the learning rates in both the training and retrieval process. Additionally, we do an
ablation study to evaluate the necessary parts of the proposed algorithm. For our experiments we use a single NVIDIA TESLA P100 GPU with 16GB RAM and approximately 100
computational hours for all experiments together.

Results

In general, we are able to reproduce the results of Hyder et al. [1]. Because of the hyperparameter search, we are certain that the results are not cherry‐picked and mostly
reproducible using the authors’ implementation of the algorithm. With our additional
experiments, we further strengthen the validity of the proposed method and help future
researchers and practitioners by providing additional information on the learning rates
in the training and retrieval process.

What Was Easy

The authors provide an implementation of their algorithm that is executable in our environment after exchanging deprecated functions. The considered datasets are open


Code
swh:1:dir:0a7ba3d1b8f4d4e2ee09a62ddfbe2e8a124d6b1e.
Open peer review is available at https://openreview.net/forum?id=rlWzUnM72RF.

https://github.com/tuelwer/machine-learning-reproducibility-challenge-2021.

available

at

is

–

SWH




access, hence easy to use. Furthermore, the computational cost is fairly low such that
we could run extensive experiments and even compare different hyperparameter settings.

What Was Difficult

We spend some effort to understand the authors’ implementation, as it is marginally
documented and the used computational tricks are not explained in detail. Moreover,
it contains some redundant code which slows down computation. Beyond refactoring,
we had to extent the implementation to be able to run our experiments. The lack of
information about the learning rates slowed down the reproduction of the results, as
we first had to investigate the influences on the training and retrieval process before we
could adjust the parameters effectively.

Communication With Original Authors

We were in contact with the authors via mail and we would like to thank the authors for
helping us. Especially, we thank Rakib Hyder who kindly answered all our questions
regarding implementation details and hyperparameters and Salman Asif who was open
for our implementation suggestions and provided useful feedback for this report.

## 1 Introduction

Many optical detection devices can only measure the Fourier magnitude of a signal (e.g.,
the intensity of light) but not its Fourier phase. This systematic loss of information is
known as the phase problem and often arises in X‐ray crystallography [2], microscopy [3],
astronomical imaging [4] and coherent diffraction imaging [5]. The goal of phase retrieval algorithms is to efficiently recover the phase of a signal from its phaseless magnitude measurements. A special problem instance is Fourier phase retrieval, where amplitudes of a Fourier transformed signal are measured and the task is to recover the
original real or complex valued signal.
In general, there is no unique mapping from the magnitude to the target signal, thus
there exist various approaches to solve it. Mainly inspired by solving holographic phase
retrieval using a reference signal by Barmherzig et al. [6], the authors apply a similar
approach to Fourier phase retrieval. Therefore, they assume a setting where the target
signal x and the reference signal u are additive and overlapping, i.e.,

y = |F (x) + F (u)| + η,

(1)

where F is the n‐dimensional Fourier transformation and η is the measurement noise.
For this particular setting, Hyder et al. [1] propose a novel, data‐driven retrieval algorithm as an unrolled network with a fixed number of layers. It is capable to learn a
reference signal u and subsequently solve the phase retrieval problem utilizing u to recover the target signal x solely from the measurements y.

## 2 Scope of Reproducibility

In this paper we reproduce the most important experiments using the method proposed
by Hyder et al. [1]. We examine, refactor and extend the original code which we incorporate into our scripts to run our experiments.




### 2.1 Addressed Claims From the Original Paper

We validate in this paper the following claims from Hyder et al. [1]:

• The presented iterative algorithm is able to learn a reference signal and can utilize
it in Fourier phase retrieval to improve the recovery of the target signal. Moreover,
it requires only a small amount of training data to learn a reference.

• The learned reference is (i) robust to data augmentation in spatial space, (ii) it
generalizes well to unseen data distribution and (iii) it is better than other types
of references, e.g., random references.

2.2 Our Contribution

Our contributions in this report are:

1. We redo the experiments on phase retrieval with a learned reference with all datasets

and report all used parameters.

2. We reproduce the generalization study with a subset of the data and report all used

parameters.

3. We validate the robustness claims with our experiments and use furthermore an

additional dataset.

4. We reproduce the experiments on the benefits of a learned references and also

extend them with further types of references and new images.

5. We validate and extend the comparison with some baseline phase retrieval algo‐

rithms.

6. We perform an extensive hyperparameter search to analyze the influence of the
learning rates on the reconstruction. We show that the performance of the algorithm can be improved by tuning the learning rates.

7. We investigate on the necessity of a reference and on the amount of oversampling

in the training and recovery process.

## 3 Methodology

Mainly, we use the Algorithm 1 and 2 from [1] which are implemented in PyTorch [7]
to validate the proposed claims and we mostly follow the restrictions and approaches
described in the paper.

### 3.1 Model Description

In order to reconstruct the target signal x∗ given a reference signal u and measurements
y = |F (x∗) + F (u)|, Hyder et al. [1] propose to minimize the loss function

Lx(x; y, u) = ∥y − |F (x) + F (u)|∥2


using a gradient descent algorithm

xk+1 = xk − α∇xLx(xk; y, u),

(2)

(3)

where α > 0 is the learning rate and xk is the reconstruction of the k‐th iteration (with
x0 being properly initialized). The authors interpret the K iterations as an unrolled
network with K layers, such that each layer of the network represents a single gradient




descent update step. So, the input to the network is y and u and the output can be written
as a function xK(y, u).
The reference signal u is learned from a training dataset of images x1, …, xN and corresponding measurements (magnitudes) y1, …, yN for a given reference u, which could
be written as

yi = |F (xi) + F (u)|.

(4)

Since for the training images and their magnitudes are known, a good reference image
u can by learned by minimizing the least‐squares error

Lu(u; x1, . . . , xn, y1, . . . , yn) =

N∑

i=1

∥xi − xK(yi, u)∥2


(5)

between signals from the training dataset x1, . . . , xN and their corresponding reconstructions xK(y1, u), . . . , xK(yN , u) using the unrolled network, Eq. (3).
This loss is minimized by gradient descent

uj+1 = uj − β∇uLu(uj; x1, . . . , xn, y1, . . . , yn),

(6)

where β > 0 is the learning rate for the reference and uj is the reference in the j‐th
iteration (with u0 being properly initialized). The gradient ∇uLu can be calculated via
backpropagation. The update rule Eq. (6) is applied for fixed number of iterations J.

### 3.2 Datasets

Throughout our experiments, we use the same datasets as in the original work [1], i.e.,
MNIST [8], EMNIST [9], FMNIST [10], CIFAR‐10 [11], SVHN [12], CelebA [13] and also 6
additional standard benchmark images 1. Three of these images were also used in the
original work [1] and three are new.
Mainly, we access the data via provided code by the authors. For training a reference,
we use always 32 images from the training datasets and we test on the same amount of
data as proposed by Hyder et al. [1]: We use 10000 test images from MNIST, FMNIST and
CIFAR‐10, 24800 for EMNIST, 26032 from SVHN and 1000 from CelebA, if not mentioned
otherwise. Furthermore, our preprocessing pipeline is similar to the original work [1]:
All used images are converted to greyscale, have intensity values in range [0, 1] and we
reshape images from MNIST, EMNIST, FMNIST, CIFAR‐10, SVHN to 32×32, images from
CelebA to 200 × 200 and the standard benchmark images to 512 × 512.

### 3.3 Hyperparameter

According to [1], we restrict the intensity values of the reference signal u to be within
the interval [0, 1] throughout all experiments. Furthermore, we oversample four times
in spatial domain by padding the input image with a black border, as this makes the
problem more well‐behaved. Additionally, our unrolled network always consists of 50
layers and we consider a noise free setting for training and retrieval. However, we provide detailed parameter configurations for all our experiments in the results section of
the respective experiment.

### 3.4 Experimental Setup

To run the original code, we replaced deprecated functions from the algorithm and imported MNIST and CelebA manually. We use PyTorch 1.5.0 [7], scikit‐image 0.18.1 [14]

1https://homepages.cae.wisc.edu/~ece533/images/ (Accessed on June 25, 2021)




Dataset

Hyder et. al. [1]

MNIST
EMNIST

SVHN

CelebA

66.54
58.72
57.81
57.51
41.60
39.00

Our reproduced results

Provided reference
66.54 ± 24.15 (α = 1.348)
58.73 ± 15.71 (α = 1.010)
57.83 ± 13.64 (α = 1.052)
57.50 ± 9.66 (α = 1.520)
41.61 ± 12.37 (α = 1.315)
39.12 ± 10.78 (α = 1.400)

Our trained reference
66.53 ± 14.98 (α = 1.177)
58.71 ± 19.31 (α = 1.160)
57.88 ± 19.36 (α = 1.320)
57.55 ± 11.58 (α = 1.660)
41.68 ± 12.78 (α = 1.720)
39.06 ± 11.21 (α = 1.870)

Table 1. Comparison of mean PSNR values reported in the original work [1] and reproduced results
using the provided reference and references that were trained from scratch. The learning rates
were tuned so that our results match the reported values from the paper.

and NumPy 1.21.0 [15] as environment and conduct our experiments in Jupyter notebooks. To compare our results with the original ones, we mainly focus on the peaksignal‐noise‐ration (PSNR) over the test images. The used code is available on GitHub
2.

### 3.5 Computational Requirements

The original implementation requires a GPU with CUDA. Therefore, we use a single
NVIDIA TESLA P100 GPU with 16 GB memory for our experiments. Overall, we used approximately 100 GPU hours but it is possible to verify the proposed claims within about
3 GPU hours, if all parameters are known. Moreover, by finding and removing unused
code we are able to decrease the runtime of the algorithm by 15 to 30 times, depending
on the shape of the image. For example, retrieving 26032 images with shape 32 × 32
takes approximately 9 seconds instead of 180 seconds.

## 4 Results

### 4.1 Reconstruction Using Learned References

In our first experiment we reproduce the mean PSNR values on MNIST, EMNIST, FMNIST, SVHN, CIFAR‐10 and CelebA that are reported in Fig. 2 of [1], see our Tab. 1. We use
the provided pre‐trained references and additionally self‐trained references and compare the mean peak‐signal‐noise‐ratio (PSNR) values as the performance criterion. For
matching results we tune both β (the learning rate for the reference u) 3 and α (the learning rate for the recovery) in the training and reconstruction process. We explain these
hyperparameters more detailed in Sec. 4.6. However, in reconstruction we keep β = 1
fixed and provide the α values used in the retrieval process additional to the results also
shown in Tab. 1.
By adjusting the learning rate α in the recovery process, we are able to reproduce all
reported mean PSNR values within a deviation of 1% using the provided references and
also our self‐trained references. For MNIST, EMNIST and FMNIST we train for 5 epochs
with α = 1 and β = 1, for CelebA we need to train for at least 15 epochs with the same
learning rates. To reproduce the reported mean PSNR for CIFAR‐10 we set α = 1.3 during
training and train for 5 epochs. For SVHN we need to set α = 1.3 and β = 10 while we
train for 10 epochs to receive the reported mean PSNR values.

2https://anonymous.4open.science/r/Machine_Learning_Reproducibility_Challenge_Spring_2021-3910/
3Note: β is called lr_u in the implementation provided by the authors.




Trained
on

Evaluated on

66.53 ± 14.98 (α = 1.177) 40.62 ± 12.66 (α = 0.795) 31.71 ± 9.00 (α = 0.950)
MNIST
40.75 ± 14.45 (α = 0.730) 57.88 ± 19.36 (α = 1.320) 40.72 ± 16.93 (α = 1.870)

CIFAR‐10 31.76 ± 8.31 (α = 0.405) 36.45 ± 9.30 (α = 0.550) 41.68 ± 12.78 (α = 1.720)


MNIST

Table 2. Comparison of mean PSNR of the generalization study using tuned learning rate α. Again,
the learning rates were tuned so that our results match the reported values from the paper.

Trained on

MNIST


MNIST
59.76 ± 13.27
49.44 ± 18.11
52.04 ± 14.26

Evaluated on

45.77 ± 15.31
49.07 ± 15.16
49.63 ± 15.20


32.07 ± 9.26
28.58 ± 11.65
37.20 ± 9.89

Table 3. Comparison of mean PSNR of the generalization study using fixed learning rate α = 1 in
recovery.

### 4.2 Generalization Study

We verify that our self‐trained references also have a generalization property by reproducing a subset of the original generalization study from [1]. We use MNIST, 
and CIFAR‐10 as a representation for each type of images, i.e., artificial and real‐world
images. Our reproduced results are presented in Tab. 2. We find that with our selftrained references all reported values except for one are reproducible within 1% deviation by tuning α in reconstruction. Nevertheless, recovery of CIFAR‐10 test images with
a self‐trained FMNIST reference results in a maximum mean PSNR of 33.75dB using
α = 1.855 but Hyder et al. [1] report 42.85dB instead. With the provided FMNIST reference, we obtain only a maximum mean PSNR of 40.72dB using α = 1.870 (found via
hyperparameter search).
Additionally, we examine the same experiment with fixed learning rate α = 1 in the
recovery process to investigate if the described trends of the references behavior, hold
for our self‐trained references as well. We present our experimental results in Tab. 3.
While MNIST and FMNIST references are reasonable reference signals for each other,
the performance drops on CIFAR‐10 which supports the observation of the authors. In
contrast, the CIFAR‐10 reference is more valuable for the other datasets than for itself
while this is not the case in the original study. Moreover, it performs better than reported by Hyder et al. [1] as it is even better than the FMNIST reference on FMNIST. In
conclusion, we observe slightly different behaviour in our experiments but overall, the
learned references generalizes well, as claimed in the paper.

### 4.3 Robustness to Data Augmentation

These experiments validate that our self‐trained references are robust against shifts, flips
and rotations in the spatial domain as it is reported in [1]. We use MNIST and 
for reproduction according to the authors’ choice and SVHN as an additional dataset.
Throughout the experiment, the learning rate in reconstruction is fixed to α = 1 and we
evaluate our experiment only on 1000 test images from each dataset. A summary of our
results is presented in Tab. 4.
While we observe that flipping and rotating in the spatial domain barely decrease the
mean PSNR on all evaluated datasets, only MNIST is fairly robust to shifting. Hence,
for SVHN the mean PSNR drops by 29% while for CIFAR‐10 it falls off by nearly 40%.
That means, their recovery results are equal or worse than the results using a random
reference. We consider the loss of information from shifting with the associated zero




Dataset

No augmentation

Shift
(5 pixel left and up)

Flip

Rotation

(90◦

clockwise)

MNIST

SVHN

59.59 ± 13.33
47.27 ± 10.14
37.04 ± 9.94

60.89 ± 14.11
28.48 ± 11.73
26.50 ± 7.20

49.71 ± 17.09
47.10 ± 9.88
38.08 ± 9.24

49.65 ± 17.43
41.18 ± 13.00
38.13 ± 10.13

Table 4. Analysis of the robustness to different data augmentation methods. Results are reported
in mean PSNR with standard deviation.

padding to be the cause for this, as it has less impact on the dark‐edged MNIST images.
However, since Hyder et al. [1] also show a decreased mean PSNR for shifting in Fig. 4
of their paper, we can validate their results.

4.4 On the Benefit of a Learned Reference

With this experiments we evaluate the advantages of a learned reference against (i) a
constant, (ii) a randomly sampled and (iii) a handcrafted reference. We consider the six
standard benchmark images. As references we use our self‐trained CelebA and 
references, which we resize to 512×512 by upscaling. The parameters are fixed in reconstruction to α = 1.92 (for best mean PSNR in recovery). Fig. 1 shows our experimental
reconstructions of the benchmark images together with the achieved PSNR values.
First, we can show that the reported results from Hyder et al. [1] are reproducible, as we
receive similar reconstruction results with our self‐trained CelebA reference. Additionally, we repeat the experiment with our self‐trained CIFAR‐10 reference but only obtain
reconstruction results between the result using a random and the CelebA reference.
To generate our random references we follow the description in [1], i.e., we draw from
a uniform distribution with range [0, 1]. Additionally, our random reference is drawn
with shape 30 × 30 and resized to 512 × 512, because this setup performs best. Finally,
we report the results of the best performing reference from 100 randomly sampled references also in Fig. 1. We observe that our experimental results are similar to the original
reconstructions results.
To show the advantage against a flat reference, we consider different flat references (all
entries set to the same value), where we obtain comparable results for different flat references. Similar to the observation of the authors, the recovery results are frequently
worse than results obtained with a random reference. We observe minor improvement
of some decibel in mean PSNR if we assemble squares or lines manually to common
figures like crosses, without any relation to the content of the pictures. However, the
reconstructed images are still less noisy if we use a random reference as shown in Fig. 1.
Overall, we can validate the reported results from [1], in particular the learned reference
performs best against all other evaluated types.

### 4.5 Comparison With Baseline Algorithms

In this section, we validate the reported results of the hybrid‐input‐output algorithm
(HIO) [16] and extend the experimental evaluation by including two more baseline phase
retrieval algorithms: Fienup’s input‐output (IO) and the Gerchberg‐Saxton (GS) algorithm [17]. We re‐implement all three algorithms from scratch using NumPy [15]. We
oversample the test images four times in spatial domain and run the algorithms for 100
iterations on each image with a step size of β = 0.8 for input‐output [16] and HIO [16].
Also, the reconstructions are clipped to intensity values in range [0, 1]. For each image,
we select the best PSNR from the cropped reconstruction and the cropped, flipped and
shifted one. Tab. 5 shows the results on the different datasets. Overall, we can validate
the claim by Hyder et al. [1], even though our HIO [16] implementation performs slightly
better than the one reported in the original work.




(a) Ground truth images

(b) Reconstruction using a rescaled reference trained on CelebA

(c) Reconstruction using a rescaled reference trained on 

(d) Reconstruction using a random reference with uniformly distributed entries

(e) Reconstruction using a handcrafted reference

Figure 1. Reconstruction results on benchmark images using different references (PSNR on top).
From top to bottom: ground truth, our trained CelebA reference, our trained CIFAR‐10 reference,
best random reference (uniform distributed, evaluation on 100 references per image), best handcrafted reference.

IO
9.80 ± 1.35
9.85 ± 1.46
8.74 ± 2.63
6.68 ± 1.85
7.80 ± 1.73

Ours

GS
9.82 ± 2.44
9.99 ± 2.41
11.25 ± 3.63
17.89 ± 3.77
16.34 ± 3.08

HIO
10.53 ± 3.81
10.81 ± 3.93
14.06 ± 8.54
31.90 ± 16.45
28.33 ± 13.92

MNIST
EMNIST

SVHN


Hyder et al. [1]

HIO

9.04
8.42
9.65
19.87
### 14.70 Table 5. Comparison of mean PSNR values (with standard deviation) by the baseline methods without use of a reference signal. In addition to the results of the HIO algorithm, we report the results
for the IO and the GS algorithm.


21.5822.5329.1025.4422.0233.17Reference18.9920.3622.5521.7619.0523.67Reference18.5019.8923.2219.1918.8819.14Reference18.8419.9721.9820.8518.9925.05Reference

Figure 2. Results from the hyperparameter search for variable learning rate α in reconstruction.

(a)

(b)

Figure 3. Results from the hyperparameter search for the learning rates: (a) mean PSNR of reconstructed images with with references trained using different learning rates α and (b) mean
PSNR of reconstructed images with references trained using different learning rates β. During
reconstruction a fixed learning rate α = 1 has been used.

### 4.6 Hyperparameter Search

Since we have no access to the original learning rates, we perform an extensive grid
search on the hyperparameters α and β. In this study we use 5 epochs during training
and evaluate on 1000 images.
We start with the learning rate α which is used to update the reconstruction in training
a reference and also in the retrieval process. For this, we use the self‐trained references
and keep β = 1 fixed while α is variable in recovery. Our results on all used datasets are
presented in Fig. 2. Surprisingly, there is a general increase of the mean PSNR among all
datasets for rising α values up to a peak in range α ∈ [1.75, 2.00]. Unfortunately, also the
standard deviation grows proportional to the higher mean PSNR values. Nevertheless,
these effects are stronger on artificial images than on real‐world images.
For our second experiment, we train with variable α on a logarithmic scale while we
keep β = 1 fixed in training and fix α = 1 in the recovery process. Fig. 3a shows our
results. Among the considered datasets SVHN has the smallest range but provides still
valuable reconstructions for α ∈ [0.1, 1]. However, for all datasets, an extensively small
or big α leads to learning a worse reference than a randomly sampled one, while the
best recovery results are mainly in α ∈ [0.1, 1].
Finally, we train with a variable reference learning rate β, while we keep α = 1 fixed.
Our results on a representative subset are shown in Fig. 3b. In general, choosing small
value for β leads to learning useless references. Nevertheless, we observe no general
pattern for optimizing the retrieval performance by adjusting β in training but valuable
results often ranges in the interval β ∈ [0.1, 10].


0.250.500.751.001.251.501.752.002.252.50Learning rate  in reconstruction only.020406080MNISTEMNISTFMNISTCIFAR-10SVHNCelebA14131211110131415Learning rate  in training.01020304050607080MNISTCIFAR-10SVHNrandom reference MNIST and SVHNrandom reference CIFAR1014131211110131415Learning rate  in training.01020304050607080MNISTCIFAR-10SVHNrandom reference MNIST and SVHNrandom reference CIFAR10

(a) No oversampling

(b) 2× oversampling

(c) 4× oversampling

(d) 8× oversampling

Figure 4. Reconstructions results with CelebA reference (trained with oversampling) and use of
different amount of oversampling during reconstruction (mean PSNR values on top of the images).

### 4.7 Ablation Study

For our ablation study we investigate whether a reference is really necessary for the
retrieval process and study how oversampling in spatial domain influences the reconstruction quality. For this experiment, we use MNIST, CIFAR‐10 with 1000 test images
as well as the common “cameraman” image in shape 512 × 512. The learning rates are
fixed to α = 1 and β = 1.
First, we run the reconstruction algorithm without using a reference. We observe that
the mean PSNR decreases drastically, e.g., for MNIST the mean PSNR is 8.92dB. We
observed similar results for other datasets such that we can conclude that a reference is
required to obtain reasonable reconstructions.
Second, we use a reference that was trained with 4× oversampling and we vary the
amount of oversampling during the recovery process. Fig. 4 shows our results for a
single benchmark image. We observe, that using no oversampling or 2× oversampling
during reconstruction leads to cloud‐like artifacts. Oversampling 4× in recovery is successful. Oversampling by a factor of 8 leads only to marginally improved performance.
Additionally, we find that we can obtain reasonable reconstructions with references that
were trained without any oversampling, if we use 4× oversampling in the retrieval process. For example, using this approach we receive a mean PSNR of 47.90dB on MNIST
which is just 6.38dB PSNR below the result with a reference that was trained using 4×
oversampling. Therefore, it might be a consideration to omit oversampling while training a reference, as it is a trade‐off between reconstruction quality and computational
requirements.

## 5 Discussion

In conclusion, we can verify that the unrolled network proposed by Hyder et al. [1] is
capable of learning a valuable reference that can be utilized to recover a signal from
its Fourier magnitude measurement. We trained our references from scratch and we
demonstrated that they are similar enough to the original ones. Moreover, we encountered no major contradiction in our experiments if we use new data, references or generative methods. However, an extensive hyperparameter search was necessary to match
the reported results. Also, the hyperparameter search reveals that one should focus on
tuning the learning rate α during reconstruction as it yields to performance improvements across all datasets. Our ablation study shows that oversampling during training
can be omitted to save computational resources.
Nonetheless, by providing an official implementation of their algorithm the authors enabled future researchers to utilize their method. Furthermore, we are grateful to the
authors for kindly answering all of our questions regarding the implementation and
providing feedback on our results.


12.0215.1830.0630.71

References

1.

2.

R. Hyder, Z. Cai, and M. S. Asif. Solving Phase Retrieval with a Learned Reference. 2020. arXiv:2007.14621
[eess.IV].
R. P. Millane. “Phase retrieval in crystallography and optics.” In: J. Opt. Soc. Am. A 7.3 (Mar. 1990), pp. 394–411.
DOI: 10.1364/JOSAA.7.000394. URL: http://josaa.osa.org/abstract.cfm?URI=josaa-7-3-394.

3. G. Zheng, R. Horstmeyer, and C. Yang. “Wide-field, high-resolution Fourier ptychographic microscopy (vol 7, pg

4.

5.

6.

7.

8.

739, 2013).” In: Nature Photonics 9 (Sept. 2015), pp. 621–621. DOI: 10.1038/NPHOTON.2015.148.
J. R. Fienup. “Phase Retrieval for Image Reconstruction.” In: Imaging and Applied Optics 2019 (COSI, IS, MATH,
pcAOP). Optical Society of America, 2019, CM1A.1. DOI: 10.1364/COSI.2019.CM1A.1. URL: http : / / www .
osapublishing.org/abstract.cfm?URI=COSI-2019-CM1A.1.
E. J. Candès, Y. C. Eldar, T. Strohmer, and V. Voroninski. “Phase Retrieval via Matrix Completion.” In: SIAM Review
57.2 (2015), pp. 225–251. DOI: 10.1137/151005099. eprint: https://doi.org/10.1137/151005099. URL: https:
//doi.org/10.1137/151005099.
D. A. Barmherzig, J. Sun, E. J. Candès, T. J. Lane, and P. Li. “Holographic Phase Retrieval and Optimal Reference
Design.” In: CoRR abs/1901.06453 (2019). arXiv:1901.06453. URL: http://arxiv.org/abs/1901.06453.
A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, A. Desmaison, L. Antiga, and A. Lerer.
“Automatic differentiation in pytorch.” In: (2017).
Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner. “Gradient-based learning applied to document recognition.” In:
Proceedings of the IEEE 86.11 (1998), pp. 2278–2324. DOI: 10.1109/5.726791.

9. G. Cohen, S. Afshar, J. Tapson, and A. Van Schaik. “EMNIST: Extending MNIST to handwritten letters.” In: 2017

International Joint Conference on Neural Networks (IJCNN). IEEE. 2017, pp. 2921–2926.

13.

11.
12.

10. H. Xiao, K. Rasul, and R. Vollgraf. “Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning
Algorithms.” In: CoRR abs/1708.07747 (2017). arXiv:1708.07747. URL: http://arxiv.org/abs/1708.07747.
A. Krizhevsky, G. Hinton, et al. “Learning multiple layers of features from tiny images.” In: (2009).
Y. Netzer, T. Wang, A. Coates, A. Bissacco, B. Wu, and A. Y. Ng. “Reading Digits in Natural Images with Unsu-
pervised Feature Learning.” In: NIPS Workshop on Deep Learning and Unsupervised Feature Learning. 2011. URL:
http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf.
Z. Liu, P. Luo, X. Wang, and X. Tang. “Deep Learning Face Attributes in the Wild.” In: Proceedings of International
Conference on Computer Vision (ICCV). Dec. 2015.
S. Van der Walt, J. L. Schönberger, J. Nunez-Iglesias, F. Boulogne, J. D. Warner, N. Yager, E. Gouillart, and T. Yu.
“scikit-image: image processing in Python.” In: PeerJ 2 (2014), e453.
C. R. Harris, K. J. Millman, S. J. van der Walt, R. Gommers, P. Virtanen, D. Cournapeau, E. Wieser, J. Taylor, S.
Berg, N. J. Smith, et al. “Array programming with NumPy.” In: Nature 585.7825 (2020), pp. 357–362.
J. R. Fienup. “Phase retrieval algorithms: a comparison.” In: Appl. Opt. 21.15 (Aug. 1982), pp. 2758–2769. DOI:
10.1364/AO.21.002758. URL: http://ao.osa.org/abstract.cfm?URI=ao-21-15-2758.
R. Gerchberg. “A practical algorithm for the determination of phase from image and diffraction plane pictures.”
In: Optik 35 (1972), pp. 237–246.

15.

14.

16.

17.

---
**Source PDF:** `1dbb9b168623.pdf` (2022_35_article.pdf)  
**URL:** https://zenodo.org/record/6574695/files/article.pdf
