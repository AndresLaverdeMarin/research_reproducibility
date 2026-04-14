R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Spatial-Adaptive Network for Single Image
Denoising

Sami Menteş1, ID , Furkan Kınlı1, ID , Barış Özcan1, ID , and Furkan Kıraç1, ID
1Video, Vision and Graphics Lab, Özyeğin University, Istanbul, Turkey

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4834672

Reproducibility Summary

In this study, we present our results and experience during replicating the paper titled ”Spatial-
Adaptive Network for Single Image Denoising”. This paper proposes novel spatial-adaptive de-
noising architecture for efficient noise removal by leveraging the deformable convolutions to
adapt spatial information (i.e. edges and textures). We have implemented the model from
scratch in PyTorch framework, and then have conducted real and synthetic noise experiments on
the corresponding datasets. We have achieved to reproduce the results qualitatively and quanti-
tatively.

Scope of Reproducibility

The original paper proposes an encoder-decoder structure exploiting a residual spatial-
adaptive block and a context block to capture multi-scale information for achieving the
state-of-the-art on real and synthetic noise removal.

Methodology

We have implemented the model, namely SADNet, from scratch in PyTorch as described
in the paper, and also adopted the training loop and proposed blocks from the authorʼs
code. Since the weight initialization of proposed blocks was not implicitly defined in the
paper, we have decided to use the default initialization method for convolutional layers
in PyTorch (i.e. Kaiming). Experiments have been completed on a single RTX 2080 Ti in
3 days for each, and it requires ∼3GB GPU memory for training, and ∼8GB CPU memory
for loading the data, due to the file structure of datasets.

Results

We have achieved to reproduce the results qualitatively and quantitatively on synthetic
and noise removal tasks. SADNet has the capacity to learn to remove the synthetic and
real noise in images, and it produces visually-plausible outputs even after a few epochs.
Moreover, we have employed SSIM and PSNR metrics to measure the quantitative perfor-
mance for all settings. The quantitative results on both tasks are on-par when compared
to the reported results in the paper.


Code is available at https://github.com/sami-automatic/SADNet_Replication. – SWH swh:1:dir:1c60d43a0fe927c1f1287adefd252804c2f273b9.
Open peer review is available at https://openreview.net/forum?id=yiAI9QN9nYt&noteId=SMFjCY6qG8.




What was easy

The code was open-source, and implemented in PyTorch, hence adopting the training
loop and proposed blocks to our implementation facilitated our reproduction study. The
loss function is straightforward and the architecture has a U-Net-like structure, so that
we could achieve to implement the architecture in a fair time.

What was difﬁcult

Due to the lack of compatibility with the current versions of PyTorch and TorchVision
and the dependency on an external CUDA implementation of deformable convolutions,
we have encountered several issues during our implementation. Then, we have consid-
ered to re-implement residual spatial-adaptive block and context block from scratch for
deferring these dependencies, however, we could not achieve it just by referring to the
paper in limited time. Therefore, we have decided to directly use the provided blocks
as in the authorʼs code.

Communication with original authors

We did not make any contact with the authors since we achieved to solve the issues
encountered during the implementation of SADNet by examining the authorʼs code.

## 1 Introduction

Recent works [1, 2, 3, 4] have shown that the previous assumption of an identically-
distributed additive white Gaussian noise (AWGN) is not an accurate representation of
the real noise occurring in images. Traditional denoiser architectures lack the ability
to adapt textures and edges, and thus miss the details while denoising, due to the over-
smoothing behaviour of CNNs. A workaround to this problem is implementing a deeper
network, however, such a practice introduces a more complex model with its computa-
tional burden.
In the original paper [5], an encoder-decoder architecture consisting a residual spatial-
adaptive block, namely RSAB, is proposed for removing spatially-variant and channel-
dependent noise while processing larger regions in each step by utilizing deformable
convolutions. As the main claim of the paper, this method produces better performance
than the compared methods in given benchmark, and also for the synthetic noise re-
moval task.
In this reproducibility report, we studied SADNet architecture for both real and syn-
thetic noise removal in detail, which contains implementing the architecture described
in the paper, running the experiments, reporting the important details about certain
issues encountered during reproducing, and comparing the obtained results with the
ones reported in the original paper.

## 2 Scope of reproducibility

The main idea of the paper is to present a spatial-adaptive architecture with encoder-
decoder structure which captures the relevant features from the complex image content
while removing real noise appearing in images. Residual spatial-adaptive block (RSAB)
makes it possible to achieve this in an efficient manner.
The proposed model, namely SADNet, claims to outperform the state-of-the-art perfor-
mances in SSIM and PSNR metrics with a moderate run-time. To validate these claims,
we try to investigate the following questions:




Figure 1. Representation of the SADNet architecture. Obtained from the paper [5].

• Is the implementation details described in the paper and provided code sufficient

for replicating the quantitative results reported in the paper?

• Are the qualitative results visually-plausible?

• Are the replicated quantitative results competitive enough?

• Could our replication obtain a proximate denoising duration compared to the re-

ported results in the original paper?

## 3 Methodology

We have implemented the model, namely SADNet, from scratch in PyTorch [6], as de-
scribed in the paper by adopting RSAB, Context block and Offset block from the authorʼs
code. The implementation of residual blocks (ResBlock) in the authorʼs code differs
from the common residual block implementation [7] by not using the output activation.
In contrast to the common practice of applying a nonlinear activation function to the
output, their ResBlock implementation directly forwards its output to the next level lay-
ers. At this point, the authors handle those activations at the model scope. We also
removed Batch Normalization [8] from the residual blocks as proposed by the original
paper. To enhance the readability of the model structure in our implementation, we
imported those activation functions back in to ResBlock.
The deformable convolutions in RSAB are implemented in CUDA, hence we used NVIDIA
GPUs with the relevant CUDA driver.
For validating the reported results on real noisy images, we have implemented the data
loaders, which are missing in the authorʼs code. Furthermore, we integrated WandB [9]
library to the training loop in order to track our experiments during training.

### 3.1 SADNet

SADNet is an encoder-decoder architecture with skip connections which favors spatial
adaptability and large receptive field over deeper networks for the well-studied denois-
ing task. The proposed model aims to achieve the state-of-the-art denoising perfor-
mance while maintaining the computational complexity by exploiting residual spatial-
adaptive block (RSAB), Context Block and Offset Block. The visual representation of
SADNet architecture is shown in Figure 1, and also the structural details about our im-
plementation of SADNet can be seen in Table 1.




Regions with the sharp texture changes in an image, typically edges and corners, raise
difficulties for training the regular convolutions, due to its fixed-size weighting mecha-
nism. Such regions, where different textures co-occur in a particular receptive field of
the regular convolutions, are simply ignored during the weighting process, due to the
fixed size kernels. To address this issue, self-similarity weighting is attained via modu-
lated deformable convolutions [10] in RSAB. The kernels of the deformable convolutions
have a learnable offset for each location in an image, and thus it has the capacity to adapt
to the spatial texture changes. The formula of modulated deformable convolutions can
be seen as follows

y(p) =

∑

pi∈N (p)

wi · x(pi + ∆pi) · ∆mi

(1)

where ∆pi denotes the learnable offset for location pi, and ∆mi is the extra degree of
freedom for adjusting the modulation scalar between [0, 1].
The nature of the decoder architectures enforces to transform the feature maps from
coarse to fine at each scale. For learning the offsets more accurately in RSABs, the offsets
∆ps−1 and the modulation scalars ∆ms−1 from the previous scale are further transferred
into the current scale s with the help of Offset Blocks. The offset transfer is formulated
as

(∆ps, ∆ms) = Fof f set

(

((

x, Fup

∆ps−1, ∆ms−1

)))

(2)

where Fup denotes the up-sampling operation. RSAB receive the extracted features and
the reconstructed features from the previous scale conveyed by the Offset Block. The
inputs are then fused through a modulated deformable convolution layer with a sub-
sequent regular convolution layer. Moreover, a skip connection similar to ResBlock is
employed to enhance the information transferring. At this point, RSAB can be formu-
lated as,

FRSAB(x) = Fcn(Fact(Fdcn(x))) + x

(3)

where Fcn and Fdcn denote regular convolution and modular deformable convolution,
respectively. Lastly, Fact stands for the leaky ReLU activation function [11] with a nega-
tive slope of 0.2.
Another introduced block is the Context Block, which resides at the bottleneck of the
model. To increase the size of the receptive fields while preserving the spatial resolu-
tion, Context Block is employed for the model, just between the encoder and decoder
structures. Furthermore, unlike the common implementation of Context Block, Batch
Normalization layer is removed in the published code, and only four dilation rates are
used, which are 1, 2, 3 and 4.
Following the original paper, we used L1 loss for training our model on real-noise image
datasets, and L2 loss for training on synthetic image datasets.

### 3.2 Datasets

The original paper uses SIDD Medium [12] and RENOIR [13] datasets during training for
denoising real noisy images and reports the qualitative and quantitative results on DND
[14] and SIDD validation [12] datasets. Since the authorʼs code only provides the data
loader for synthetic image datasets, we have integrated our SIDD validation data loader
implementation and the DND test script provided by TU Darmstadt [14] to our pipeline.
For synthetic noise removal, additive white Gaussian noise with standard deviation of
30, 50 and 70 have been added to DIV2K dataset [15], which consists 800 high resolution
images. To validate the performance of SADNet on synthetic noise removal task, the
models are tested on BSD68 [16] and Kodak24 datasets processed with the same noise
addition mechanism.




Table 1. Details of our model implementation.

Module Name
Conv1
ResBlock1
Conv2
ResBlock2
Conv3
ResBlock3
Conv4
ResBlock4
Context Block
Offset Block Bottleneck
RSAB Bottleneck
TransposeConv1
Concat1 (/w ResBlock3)
Conv5
Offset Block 1
RSAB 1
TransposeConv2
Concat2 (/w ResBlock2)
Conv6
Offset Block 2
RSAB 2
TransposeConv3
Concat3 (/w ResBlock1)
Conv7
Offset Block 3
RSAB 3
Concat4 (/w input)
ConvOut

Kernel Size
1 × 1
3 × 3
2 × 2
3 × 3
2 × 2
3 × 3
2 × 2
3 × 3

2 × 2

1 × 1

2 × 2

1 × 1

2 × 2

1 × 1

3 × 3

# of Channels
3 → 32
32 →32
32 →64
64 → 64
64 →128
128 → 128
128 → 256


256 → 128
128 → 256
256 → 128
128 → 128
128 → 128
128 → 64
64 → 128
128 → 64
64 → 64
64 → 64
64 → 32
32 → 64
64 → 32
32→32
32→32
32→35
35 → 3

Stride


Non-linearity


Linear

Both test and validation data for all settings are composed of high resolution images.
Therefore, they are fed to the model as 128x128 patches cropped by fixed coordinates, as
described in the paper. We have applied 90◦ rotation, horizontal and vertical flipping to
the images during training, following the practice in the paper.

### 3.3 Hyperparameters

In our replication study, we used the ADAM optimizer [17] with β1 = 0.9, β2 = 0.999,
and ϵ = 1e − 8, with an initial learning rate of 1e − 4 during training, as described in the
paper. The provided code initializes the weights of the convolutional layers in all blocks
with Xavier Uniform method [18]. Since this choice has not been discussed in the paper,
we left each convolution layer initialized by the default weight initialization method in
PyTorch (i.e. Kaiming [19]) in our experiments.

Table 2. Quantitative results on SIDD sRGB validation dataset. Compared methods: CBM3D [20],
CDnCNN-B [21], CBDNet [3], PD [2], RIDNet [4], SADNet [5].

Method

CBM3D

CDnCNN-B CBDNet

Blind/NonBlind Non-blind

PSNR

### 30.88 Blind
### 26.21 Blind
30.78

PD
Blind
### 32.94 RIDNet
Blind
### 38.71 SADNet
Blind
### 39.46 SADNet (ours)
Blind
39.41




### 3.4 Experimental setup

In this study, we have followed the same training procedures for all setting, and em-
ployed SSIM and PSNR values as performance metrics, as described in the original pa-
per. The parameters for all training settings can be found in the configuration file in
our GitHub repository. Our implementation and the trained weights are open-sourced,
and can be accessed at https://github.com/sami-automatic/SADNet_Replication.

### 3.5 Computational requirements

The experiments have been conducted on a single RTX 2080Ti for approximately 3 days,
and only requires high GPU memory, mostly due to modulated deformable convolutions.
It requires ∼3GB GPU memory for training, and ∼8GB CPU memory for loading the data,
due to the file structure of datasets.

## 4 Results

We have implemented the model from scratch by following the descriptions presented in
the original paper, and then achieved to replicate the claimed results by referring to the
published code. Overall, our implementation of SADNet achieved on-par performances

(a) Noisy: 18.15 dB

(b) Clear: ∞ dB

(c) SADNet (ours): 34.67 dB

Figure 2. Real image denoising results on SIDD validation dataset. The results on the first two rows
are obtained from the paper [5], the third row represents our results on the same image.




(a) Noisy: 17.59 dB

(b) Clear: ∞ dB

(c) SADNet (ours): 35.62 dB

Figure 3. Real image denoising results on SIDD validation dataset. The results on the first two rows
are obtained from the paper [5], the third row represents our results on the same image.

in SSIM and PSNR metrics on test datasets, and we also validated the results on both
denoising tasks by examining their qualitative results.
As shown in Table 2, our quantitative results on SIDD sRGB validation dataset has 39.41
PSNR value, which is only 0.12% less than the one reported in the original paper. More-
over, the average duration of a single inference of SADNet is 26.7 ms. according to the
paper, while our implementation of SADNet completes the single inference on 25.9 ms.
The visual comparisons of real noise removal of the images are shown in Figure 2 and
Figure 3. The samples are from SIDD validation dataset, according to the ones reported
in the paper. The first two rows in these figures are directly taken from the original paper
for further comparison with our replication results, which can be seen in the third row.
On the results from the original paper, SADNet mainly differs from the compared meth-
ods by generating a distinct clear continuous stripe texture on the background while
preserving the object surface appearance. Our replication clearly shares the similar be-
haviour. Therefore, we can state that the replicated quantitative results on real noise
removal task are competitive enough, and also supports the main claim in the original
paper.
Similarly, Table 3 demonstrates that the results of our SADNet implementation achieves
on-par PSNR values with the ones reported in the paper for different noise levels (i.e.
σ ∈ {30, 50, 70}) on BSD68 and Kodak24 datasets. Particularly, we have obtained better
results than all other compared methods and the reported SADNet results on Kodak24
dataset for all noise levels. Moreover, the replicated SADNet model imitates the qualita-




(a) Clear

(b) Noisy: 14.65 dB

(c) SADNet (ours): 28.96 dB

Figure 4. Synthetic image denoising results on BSD68 dataset with noise level σ = 50. The results
on the first row are obtained from the paper [5], the second row represents our results on a similar
patch.

tive results of the original model on both datasets. Although the images from Kodak24
and BSD68 are heavily exposed to the synthetic noise, SADNet has the ability to remove
noise, and to generate well-defined textures when compared to the recent works. As
shown in Figure 4, all other compared methods have smoothed the texture and swept
away the feather details, meanwhile the original implementation of SADNet and ours
achieve to generate more plausible feather-like texture. Similar to the previous exam-
ple, in Figure 5, the clothing details are significantly preserved, especially pilling on the
top-left part of the cloth and the vertical texture details on the cloth.
The ground truth of DND validation set is private, and thus it is not possible to locally
validate the results on this dataset. Despite of several attempts to submit our results to
DND online validation system, we could not obtain SSIM and PSNR results, due to the
server error. We have tried to contact with DND Team, but we could not get any advice
for solving this issue.

Table 3. Average PSNR(dB) results on synthetic color noisy images.

Datasets

Models
CBM3D [20]
DnCNN [21]
MemNet [22]
FFDNet [23]
RNAN [24]
RIDNet [4]
SADNet [5]
SADNet (ours)

Kodak24 (σ)


BSD68 (σ)


30.89
31.39
29.67
31.39
31.86
31.64
31.86
32.06

28.63
29.16
27.65
29.10
29.58
29.25
29.64
29.86

27.27
27.64
26.40
27.68
28.16
27.94
28.28
28.47

29.73
30.40
28.39
30.31
30.63
30.47
30.64
30.58

27.38
28.01
26.33
27.96
28.27
28.12
28.32
28.30

26.00
26.56
25.08
26.53
26.83
26.69
26.93
26.91




(a) Clear

(b) Noisy: 15.48 dB

(c) SADNet (ours): 30.22 dB

Figure 5. Synthetic image denoising results on Kodak24 dataset with noise level σ = 50. The results
on the first row are obtained from the paper [5], the second row represents our results on a similar
patch.

## 5 Discussion

The qualitative results generated with our replication strongly resemble to the presented
results, and differs from the other compared studies. According to these results, we can
state that our implementation of SADNet consistently yields visually-plausible results
on both real and synthetic noisy images, and supports the claims of the original paper.
In addition, our experiments firmly correlates with the reported PSNR values.
Overall, the paper and the provided code was sufficient for replicating the results on real
and synthetic noise removal. For re-implementing the model from scratch, we have only
referred to the paper, and ended up on-par performance with the ones in the paper on
all settings.
Lastly, to provide an insight for run-time on different hardware, our replication has 25.9
ms. inference run-time on real noise removal task, whereas the reported run-time du-
ration is 26.7 ms. Note that we used a single RTX 2080Ti GPU during our experiments,
while a single GTX 1080Ti GPU is used in the original study, and we assume that this is
the reason of this difference.

### 5.1 What was easy

The code was open-source, and implemented in PyTorch, hence adopting the training
loop and proposed blocks to our implementation facilitated our reproduction study. The
loss function is straightforward and the architecture has a U-Net-like structure, so that
we could achieve to implement the architecture in a fair time.

### 5.2 What was difﬁcult

Due to the lack of compatibility with the current versions of PyTorch and TorchVision
and the dependency on an external CUDA implementation of deformable convolutions,
we have encountered several issues during our implementation. Then, we have con-
sidered to re-implement residual spatial-adaptive block and context block from scratch
for deferring these dependencies, however, we could not achieve this just by referring




to the paper. Therefore, we have decided to directly use the provided blocks as in the
authorʼs code.

### 5.3 Communication with original authors

We did not make any contact with the authors since we achieved to solve the issues
encountered during the implementation of SADNet by examining the authorʼs code.

References

1.

2.

3.

4.

T. Plötz and S. Roth. “Neural Nearest Neighbors Networks.” In: Advances in Neural Information Process-
ing Systems. Ed. by S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett.
Vol. 31. Curran Associates, Inc., 2018. URL: https : / / proceedings . neurips . cc / paper / 2018 / file /
f0e52b27a7a5d6a1a87373dffa53dbe5-Paper.pdf.
Y. Zhou, J. Jiao, H. Huang, Y. Wang, J. Wang, H. Shi, and T. Huang. “When AWGN-Based Denoiser Meets Real
Noises.” In: Proceedings of the AAAI Conference on Artiﬁcial Intelligence 34.07 (Apr. 2020), pp. 13074–
13081. DOI: 10.1609/aaai.v34i07.7009. URL: https://ojs.aaai.org/index.php/AAAI/article/view/7009.
S. Guo, Z. Yan, K. Zhang, W. Zuo, and L. Zhang. “Toward convolutional blind denoising of real photographs.” In:
2019 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2019).
S. Anwar and N. Barnes. “Real Image Denoising with Feature Attention.” In: IEEE International Conference on
Computer Vision (ICCV-Oral) (2019).

8.

9.

7.

6.

5. M. Chang, Q. Li, H. Feng, and Z. Xu. “Spatial-Adaptive Network for Single Image Denoising.” In: Computer Vision
– ECCV 2020. Ed. by A. Vedaldi, H. Bischof, T. Brox, and J.-M. Frahm. Cham: Springer International Publishing,
2020, pp. 171–187.
A. Paszke et al. “PyTorch: An Imperative Style, High-Performance Deep Learning Library.” In: Advances in Neu-
ral Information Processing Systems 32. Ed. by H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E.
Fox, and R. Garnett. Curran Associates, Inc., 2019, pp. 8024–8035. URL: http://papers.neurips.cc/paper/9015-
pytorch-an-imperative-style-high-performance-deep-learning-library.pdf.
K. He, X. Zhang, S. Ren, and J. Sun. “Deep Residual Learning for Image Recognition.” In: 2016 IEEE Conference
on Computer Vision and Pattern Recognition (CVPR). 2016, pp. 770–778. DOI: 10.1109/CVPR.2016.90.
S. Ioffe and C. Szegedy. “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Co-
variate Shift.” In: Proceedings of the 32nd International Conference on Machine Learning. Ed. by F. Bach
and D. Blei. Vol. 37. Proceedings of Machine Learning Research. Lille, France: PMLR, July 2015, pp. 448–456.
URL: http://proceedings.mlr.press/v37/ioffe15.html.
L. Biewald. Experiment Tracking with Weights and Biases. Software available from wandb.com. 2020. URL:
https://www.wandb.com/.
X. Zhu, H. Hu, S. Lin, and J. Dai. “Deformable ConvNets V2: More Deformable, Better Results.” In: June 2019,
pp. 9300–9308. DOI: 10.1109/CVPR.2019.00953.
A. L. Maas, A. Y. Hannun, and A. Y. Ng. “Rectiﬁer nonlinearities improve neural network acoustic models.” In: in
ICML Workshop on Deep Learning for Audio, Speech and Language Processing. 2013.
A. Abdelhamed, S. Lin, and M. S. Brown. “A High-Quality Denoising Dataset for Smartphone Cameras.” In: IEEE
Conference on Computer Vision and Pattern Recognition (CVPR). June 2018.
J. Anaya and A. Barbu. “RENOIR - A Benchmark Dataset for Real Noise Reduction Evaluation.” In: CoRR
abs/1409.8230 (2014). arXiv:1409.8230. URL: http://arxiv.org/abs/1409.8230.
T. Plötz and S. Roth. “Benchmarking Denoising Algorithms with Real Photographs.” In: 2017 IEEE Conference
on Computer Vision and Pattern Recognition (CVPR). 2017, pp. 2750–2759. DOI: 10.1109/CVPR.2017.294.
E. Agustsson and R. Timofte. “NTIRE 2017 Challenge on Single Image Super-Resolution: Dataset and Study.”
In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops.
July 2017.
“A database of human segmented natural images and its application to evaluating segmentation algorithms
and measuring ecological statistics.” In: vol. 2. 2001, 416–423 vol.2. DOI: 10.1109/ICCV.2001.937655. URL:
http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=937655.
D. P. Kingma and J. Ba. “Adam: A method for stochastic optimization.” In: International Conference on Learn-
ing Representations (ICLR). 2015.
X. Glorot and Y. Bengio. “Understanding the difﬁculty of training deep feedforward neural networks.” In: AIS-
TATS. 2010.

10.

11.

12.

13.

14.

15.

16.

17.

18.




19.

20.

21.

22.

23.

24.

K. He, X. Zhang, S. Ren, and J. Sun. “Delving Deep into Rectiﬁers: Surpassing Human-Level Performance on Im-
ageNet Classiﬁcation.” In: 2015 IEEE International Conference on Computer Vision (ICCV) (2015), pp. 1026–
1034.
K. Dabov, A. Foi, V. Katkovnik, and K. Egiazarian. “Color Image Denoising via Sparse 3D Collaborative Filter-
ing with Grouping Constraint in Luminance-Chrominance Space.” In: 2007 IEEE International Conference on
Image Processing. Vol. 1. 2007, pp. I - 313-I –316. DOI: 10.1109/ICIP.2007.4378954.
K. Zhang, W. Zuo, Y. Chen, D. Meng, and L. Zhang. “Beyond a Gaussian denoiser: Residual learning of deep CNN
for image denoising.” In: IEEE Transactions on Image Processing 26.7 (2017), pp. 3142–3155.
Y. Tai, J. Yang, X. Liu, and C. Xu. “MemNet: A Persistent Memory Network for Image Restoration.” In: 2017 IEEE
International Conference on Computer Vision (ICCV). 2017, pp. 4549–4557. DOI: 10.1109/ICCV.2017.486.
K. Zhang, W. Zuo, and L. Zhang. “FFDNet: Toward a Fast and Flexible Solution for CNN based Image Denoising.”
In: IEEE Transactions on Image Processing (2018).
Y. Zhang, K. Li, K. Li, B. Zhong, and Y. Fu. “Residual Non-local Attention Networks for Image Restoration.” In:
International Conference on Learning Representations. 2019. URL: https : / / openreview . net / forum ? id =
HkeGhoA5FX.

---
**Source PDF:** `a107cf68f9d6.pdf` (2021_12_article.pdf)  
**URL:** https://zenodo.org/record/4834672/files/article.pdf
