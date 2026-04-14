R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020


Balsells Rodas, Carles1, ID , Canal Anton, Oleguer1, ID , and Taschin, Federico1, ID
1KTH Royal Institute of Technology, CNRS UPR4301, Stockholm, Sweden

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
10.5281/zenodo.4835278

Abstract

Hamiltonʼs equations are widely used in classical and quantum physics. The Hamilto-
nian Generative Network (HGN) is the first approach that aims to ”learn the Hamilto-
nian dynamics of simple physical systems from high-dimensional observations without
restrictive domain assumptions”. To do so, a variational model is trained to reconstruct
the evolution of physical systems directly from images by integrating the learned Hamil-
tonian. New trajectories can be sampled and rollouts can be performed forward and
backward in time. In this work, we re-implement the HGN architecture and the phys-
ical environments (pendulum, body-spring system, and 2,3-bodies). We reproduce the
paper experiments and we further expand them by testing on two new environments
and one new integrator. Overall, we find that obtaining both good reconstruction and
generative capabilities is hard and sensitive to the variational parameters.

Reproducibility Summary

Scope of Reproducibility

The main objective of the paper is to ”learn the Hamiltonian dynamics of simple physical
systems from high-dimensional observations without restrictive domain assumptions”.
To do so, the authors train a generative model that reconstructs an inputted sequence of
images of the evolution of some physical system. For instance, they learn the dynamics
of a pendulum, a body-spring system, and 2,3-bodies. In addition to these environments,
we further expand the testing on two new environments and we explore architecture
tweaks looking for performance gains.

Methodology

We implement the project with Python using Pytorch [1] as a deep learning library. Pre-
vious to ours, there was no public implementation of this work. Thus, we had to write
the code of the simulated environments, the deep models, and the training process.
The code can be found in this repository: https://github.com/CampusAI/Hamiltonian-
Generative-Networks A single training takes around 4 hours and 1910MB of GPU mem-
ory (NVIDIA GeForce RTX2080Ti).


Code
swh:1:dir:7c7cee4b1c4dc7dfa46b4b4bf5c3b8b20deb5b26.
Open peer review is available at https://openreview.net/forum?id=Zszk4rXgesL.

at https://github.com/CampusAI/Hamiltonian-Generative-Networks – DOI 10.5281/zenodo.4673473.

available

is

– SWH




Results

We found the modelʼs input-output data slightly unclear in the original paper. First, it
seems that the model reconstructs the same sequence that has been inputted. Neverthe-
less, further discussion with the authors seems to indicate that they input the first few
frames to the network and reconstructed the rest of the rollout. We test both approaches
and analyze the results. We generally obtain comparable results to those of the original
authors when just reconstructing the input sequence (30% average absolute relative er-
ror w.r.t. to their reported values) and worse results when trying to reconstruct unseen
frames (107% error). In this report, we include our intuition on possible reasons that
would explain these observations.

What was easy

The architecture of the model and training procedure was easy to understand from the
paper. Besides, creating simulation environments similar to those of the original au-
thors was also straightforward.

What was difﬁcult

While the overall model architecture and data generation were easy to understand, we
encountered the optimization to be especially tricky to perform. In particular, finding a
good balance between the reconstruction loss and KL divergence loss was challenging.
We implemented GECO [2] to dynamically adapt the Lagrange multiplier but it proved to
be surprisingly brittle to its hyper-parameters, resulting in very unstable behavior. We
were unable to identify the cause of the problem and ended up training with simpler
techniques such as using a fixed Lagrange multiplier as presented in [3].

Communication with original authors

We exchanged around 6 emails with doubts and answers with the original authors.

## 1 Introduction

Consider an isolated physical system with multiple bodies interacting with each other.
Let q ∈ Rn be the vector of their positions, and p ∈ Rn the vector of their momenta.
The Hamiltonian formalism [4] states that there exists a function H : (q, p) ∈ Rn+n → R
representing the energy of the system which relates q and p as:

∂q
∂t

=

∂H
∂p

,

∂p
∂t

= − ∂H
∂q

(1)

In this work H is modeled with an artificial neural network and property 1 is exploited
to get the temporal derivatives of both q and p. One can then use a numerical integra-
tor (see Section 4.1) to solve the ODE and infer the system evolution both forward and
backward in time given some initial conditions (see Figure 2). These initial conditions
are inferred from a natural image sequence of the system evolution (see Figure 1). The
authors propose a generative approach to learn low-dimensional representations of the
positions and momenta (q0, p0). This allows us to sample new initial conditions and
unroll previously unseen system evolutions according to the learned Hamiltonian dy-
namics.




## 2 Scope of reproducibility

The main claim of the paper is that the proposed architecture is able to ”learn the Hamil-
tonian dynamics of simple physical systems from high-dimensional observations with-
out restrictive domain assumptions”. This means that the architecture is capable of
learning an abstract position and momentum in latent space from RGB images. Then,
with the help of an integrator, the architecture will be capable of reconstructing the sys-
tem evolution. Modifying the integrator time-step will result in a slow-motion or fast-
forward evolution. Moreover, the architecture can generate previously unseen system
evolutions through sampling. Briefly, we will evaluate the following claims:

• The architecture reconstructs RGB frames of a physical system evolution with an

error comparable to [5].

• The architecture can generate new samples qualitatively similar to the originals.

• The timescale of the predicted evolution can be tuned as an integrator parameter

without significant degradation of the resulting video sequence.

## 3 Methodology

To date (Jan 1st 2021), authors did not release their code. Therefore, we fully re-implement
the Hamiltonian architecture, the integrators, and the simulated environments. To
further evaluate the system, we implement two additional environments and one ad-
ditional integrator. We developed our implementation in Python3 using PyTorch [1]
machine learning library for the Hamiltonian architecture and the Scipy [6] ODE solver
for the simulated environments, as well as OpenCV [7] for image manipulation. Our
code can be found in this repository1. We run most of the experiments using an NVIDIA
GeForce RTX 2080Ti and some on an NVIDIA GTX 970.

### 3.1 Hamiltonian Generative Network (HGN)

The HGN [5] architecture can be split into two high-level components. The first (Figure
1) reads the initial k + 1 frames of an environment rollout and extracts the abstract posi-
tions and momenta (qk, pk) correspondent to the k-th step. Second, a recurrent model
takes (qk, pk) as first input and performs integration steps of a fixed ∆t, predicting the
evolution of the system in terms of abstract positions and momenta 2. For each step,
the abstract position is decoded into an RGB image. As figures 1, 2 depict, this model is
composed by four main networks:

• Encoder: Parametrized by: ϕ. 8-layer 64-filter Conv2D network with ReLU acti-
vations that takes a sampled video rollout from the environment and outputs the
mean and variance of the encoder distribution qϕ(z) parametrized as a diagonal
Gaussian with prior p(z) = N (0, I). The latent variable z is sampled from qϕ with
the reparametrization trick [8]. The input of this layer is constructed by concate-
nating all the rollout frames in the channel axis. Therefore, if working with RGB
images, the input has shape: H × W × 3 · N . Where H, W, N are Height, Width,
and Number of frames, respectively.

• Transformer: Parametrized by: ψ. Takes in the sampled latent variable z and
transforms it into a lower-dimensional initial state sk = (qk, pk), by applying 3
Conv2D layers with ReLU activations, stride 2, and 64 filters.

1https://github.com/CampusAI/Hamiltonian-Generative-Networks
2In addition, we test how the network performs when trained as an autoencoder, ie: fit the complete se-

quence and reconstruct it. (Section 4)




• Hamiltonian: Parametrized by: γ. It is a 6-layer 64-filter Conv2D network with Soft-
Plus activations which takes in the abstract positions and momenta (qt, pt) and
outputs the energy of the system et ∈ R. This network is used by the integrator
(Section 4.1) to compute the system state at the next time-step (qt+1, pt+1) exploit-
ing Eq. 1. Since Eq. 1 involves partial derivatives of H w.r.t. q and p, the train-
ing process involves second-order derivatives of the Hamiltonian network weights.
For this reason, SoftPlus activations are used instead of ReLU.

• Decoder: Parametrized by: θ. 3-residual block upsampling Conv2D network (as
in [9]) which converts the abstract position qt into an image close to the source
domain.

Given an input sequence: (x0, ..., xT ) and a value k + 1 of input-length, the loss function
3 to optimize is:

L(ϕ, ψ, γ, θ; x0, ..., xT ) =

T∑

(

Eqϕ(z|x0,..xk)

[

log pψ,γ,θ(xt | qt)

])

(2)


T + 1 − k

− Λ · KL

(

t=k

)
qϕ(z) || p(z)

Notice that the loss is the combination of two terms: first, the error coming from the re-
construction of the images, and second, a term which forces the latent distribution qϕ to
be close to a standard Gaussian. It is interesting to see that there is no conditioning over
the behavior of latent positions and momenta during the rollout. The architecture con-
nections are enough to force qk to encode the position information and pk the momenta
information at timestep k.
We use the same optimizer as in [5]: Adam [10] with a constant learning rate of lr =
1.5e−4 with the GECO algorithm presented in [2] to adapt the Lagrange multiplier Λ
during training. This Lagrange multiplier is dynamically updated according to an expo-
nential moving average proportional to the reconstruction error of the assessed mini-
batch. The main parameters controlling the Lagrange multiplier are the exponential
moving average constant α, the initial Lagrange multiplier, and a parameter to control
its growth λ. The authors did not include the values used in the paper, so we performed
a grid search to find the most adequate ones for each environment (see Section 6). In
addition, we trained a version of the model with a fixed Lagrange multiplier.

Figure 1. HGN network architecture to find the final abstract position and momentum (qk, pk)
from the input sequence. Tensors are represented in blue and operations in black. The encoder
takes as input a sequence of k + 1 frames concatenated along channels and samples the latent
variable z ∼ qϕ(z|x0, ..., xk) with the reparametrization trick. The transformer network converts
z into the state sk = (qk, pk) from which the system evolution will be predicted.

3The formulation of the loss in Eq. 2 particularly w.r.t. the distribution qϕ is different from that of the
paper[5] where it was written as qϕ(z|x0, ..., xT ), which initially led us to think that the encoder had access
to the whole rollout. Discussion with the authors clarified that the encoder reads only the first k frames.
Therefore, we decided to slightly modify the loss notation in order to avoid confusion. Still, we show results
with both approaches to get a more complete idea of the differences.




Figure 2. Recurrent part of the HGN architecture. Blue cubes represent tensors. The integrator
takes the position and momentum for each time-step, computes H(qt, pt) and computes the ab-
stract state in the next time-step st+1 = (qt+1, pk+1) for t ≥ k exploiting the Hamiltonian equa-
tions of 1. The decoder takes the abstract position qt and decodes it into the original image xt.

### 3.2 Integrator Modelling

Since the Hamiltonian network always requires backpropagation, which is an expensive
operation, we compare it against a baseline network that does not require backprop-
agation at evaluation time. We test an architecture almost identical to the HGN, but
where the Hamiltonian Network is replaced by a CNN that directly computes ∆q and
∆p from qt and pt. Integration is then performed as an Euler step: qt+1 = qt + ∆t∆q and
pt+1 = pt + ∆t∆p. In this architecture, therefore, we do not learn Hamiltonian-like dy-
namics anymore, but we directly learn the system dynamics in the abstract space. This
approach achieves a similar reconstruction loss than HGN[5]. Results are presented in
the additional experiments section. 4.1.

### 3.3 Datasets

The datasets considered by the original authors consist of observations of the time evo-
lution of four physical systems: mass-spring, simple pendulum, and two-/three-body
systems [5]. Since the datasets are not available to us, we re-implement them following
as closely as possible the information provided in the paper and by the authors. More-
over, we introduce two new physical systems to experiment with: damped harmonic
oscillator and double pendulum (see Figure 3).
The procedure for data generation is analogous to the one used by [11]. Given a phys-
ical system, we first randomly sample an initial state (q0, p0) in the phase space and
generate a 30 step rollout following the Hamiltonian dynamics. Once the trajectory is
obtained, we add Gaussian noise with standard deviation σ = 0.1 to each phase-space
coordinate at each step and render 32x32 image observations. Objects in the systems
are represented as circles and we use different colors to represent different objects. We
generate 50000 train samples and 10000 test samples for each physical system. To sam-
ple the initial conditions (q0, p0), we first sample the total energy denoted as a radius r
in phase space and then (q0, p0) are sampled uniformly on the circle of radius r. Note
that here q and p represent the actual positions and momenta vectors of the bodies in
the system. These are only used to generate the sequence of images and are not made
available to the HGN architecture. The trajectories for each environment are computed
using the ground-truth Hamiltonian dynamics and SciPy ODE solver [6].

Mass-spring. Assuming no friction, the Hamiltonian of a mass-spring system is H =
p2
2m + 1
2 kq2, where m is the objectʼs mass and k is the springʼs elastic constant. We gen-




Figure 3. Representation and samples from the different physical systems considered in our ex-
periments. Notice that differing from [5], we also consider a damped mass-spring system and a
double pendulum.

erate our data considering m = 0.5, k = 2 and r ∼ U(0.1, 1.0).

Pendulum. An ideal pendulum is modelled by the Hamiltonian H = p2
2ml2 + 2mgl(1 −
cos q), where l is the length of the pendulum and g is the gravity acceleration. The data
is generated considering m = 0.5, l = 1, g = 3 and r ∼ U(1.3, 2.3).

Two-/three- body problem. The n-body problem considers the gravitational interac-
gmimj
tion between n bodies in space.
|| ,
−qj
||qi
where mi corresponds to the mass of object i. In this dataset, we set {mi = 1}n
i=1 and
g = 1. For the two-body problem, we modify the observation noise to σ = 0.05 and set
r ∼ U(0.5, 1.5). When considering three bodies, we set σ = 0.2 and r ∼ U(0.9, 1.2).

Its Hamiltonian is H =

∑
n
i̸=j

||2
||pi
2mi

∑
n
i

−

Dobule pendulum The double pendulum consists of a system where we attach a sim-
ple pendulum to the end of another simple pendulum. For simplicity, we conider both
simple pendulums with identical properties (equal mass and length). The Hamiltonian
of this system is H = 1
, where {q1, p1}
2ml2
and {q2, p2} refer to the phase state of the first and second pendulum respectively. Our
data is generated by setting m = 1, l = 1, g = 3 and r ∼ U(0.5, 1.3). In this scenario we
consider a very low intense source of noise σ = 0.05.

2+2p1p2cos(q1−q2)
1+sin2(q1−q2)

3−2 cos q1−cos q2

+mgl

1+p2
p2

(

)

)

Damped oscillator The damped mass-spring system is obtained by considering a dis-
sipative term in the equations of motion of the ideal mass-spring system. For such sys-
p2
tems, one can obtain its dynamics using the Caldirola-Kanai Hamiltonian H = eγt
2m +
2 kq2
[12], where γ is the damping factor of the oscillator. In our experiments, we
consider an underdamped harmonic oscillator and set γ = 0.3, m = 0.5, k = 2, r ∼
U(0.75, 1.4) and σ = 0.1.

(


### 3.4 Hyperparameters

We set the same hyperparameters for all experiments as the original paper [5] except for
GECO parameters, which were not included. Thus, we perform a grid search on each
environment to find the most adequate ones (see Section 4.1).

### 3.5 Computational requirements

A standard training of 50K train samples using the Leapfrog integrator takes around 4
hours on an RTX 2080T GPU and requires around 1910MB.




MODEL

MASS-SPRING

PENDULUM

TWO-BODY

THREE-BODY

Orig. HGN (EULER) [5]
Orig. HGN (DETERM) [5]
Orig. HGN (LEAPFROG) [5]
HGN (EULER) ours
HGN (DETERM) ours
HGN (LEAPFROG) ours
HGN (EULER) ours 5-frame inference
HGN (DETERM) ours 5-frame inference
HGN (LEAPFROG) ours 5-frame inference

TRAIN
3.67 ± 1.09
0.23 ± 0.23
3.84 ± 1.07
9.05 ± 0.02
7.10 ± 0.01
7.11 ± 0.01
42.09 ± 0.14
13.00 ± 0.05
12.15 ± 0.05

TEST
6.2 ± 2.69
3.07 ± 1.06
6.23 ± 2.03
9.06 ± 0.05
7.10 ± 0.03
7.12 ± 0.03
41.98 ± 0.32
13.04 ± 0.11
12.21 ± 0.11

TRAIN
5.43 ± 2.53
0.79 ± 1.24
4.9 ± 1.86
17.79 ± 0.06
14.11 ± 0.05
14.89 ± 0.05
47.06 ± 0.17
45.06 ± 0.19
44.29 ± 0.19

TEST
10.93 ± 4.32
10.68 ± 3.19
11.72 ± 4.14
17.86 ± 0.13
14.14 ± 0.12
14.97 ± 0.1
47.03 ± 0.39
44.89 ± 0.42
44.12 ± 0.42

TRAIN
6.62 ± 3.93
2.34 ± 2.3
6.36 ± 3.29
3.84 ± 0.01
3.92 ± 0.02
3.36 ± 0.01
6.46 ± 0.03
10.95 ± 0.02
6.28 ± 0.03

TEST
15.06 ± 7.01
14.47 ± 5.24
16.47 ± 7.15
3.85 ± 0.02
3.93 ± 0.02
3.36 ± 0.02
6.52 ± 0.06
10.97 ± 0.05
6.33 ± 0.06

TRAIN
7.51 ± 3.49
4.1 ± 2.05
7.88 ± 3.55
1.99 ± 0.01
4.14 ± 0.01
8.81 ± 0.01
8.18 ± 0.01
3.72 ± 0.01
3.35 ± 0.01

TEST
9.4 ± 3.92
5.17 ± 1.96
9.8 ± 3.72
1.99 ± 0.01
4.13 ± 0.02
8.81 ± 0.01
8.17 ± 0.01
3.72 ± 0.02
3.35 ± 0.02

Table 1. Average pixel MSE of the reconstruction of a 30-frame rollout sequence on the test and train
datasets of the four physical systems presented by [5]. All the values are multiplied by 104. We
show our results (second and third group) along with the ones reported by the original authors
(first group). In the second group, we train to reconstruct the whole inputted sequence (as an
autoencoder) and in the third group, we train by inputting only the first 5 frames.

(a)

(b)

Figure 4. (a) Reconstruction of a sequence of the 2-body system along with a backward unroll of
the data from the final state, and a forward rollout of the HGN trained using state inference from
the first 5 frames. (b) Reconstruction of a sequence of the pendulum system along with a sped up
and a slowed down forward rollout.

## 4 Results

We first test whether the HGN [5] can learn the dynamics of the four presented phys-
ical systems by measuring the average mean squared error (MSE) of the pixel recon-
structions of each predicted frame. Furthermore, we test the original HGN architecture
along with different modifications: a version trained with Euler integration rather than
Leapfrog integration (HGN Euler), and a version that does not include sampling from
the posterior qϕ(z|x0...xT ) (HGN determ). Since we could not find suitable GECO[2]
hyperparameters, we use a fixed Lagrange multiplier[3] in all the experiments.
Table 1 shows the results of the experiments described previously along with the results
of the original authors. As it can be seen, we achieve average pixel reconstruction er-
rors that are similar (30% avg absolute error w.r.t. the reported values on the test set
using Leapfrog integrator) to the ones reported in the original paper when reconstruct-
ing the same sequence that is inputted (we call this version autoencode). However, when
attempting to train to reconstruct a rollout given only the first 5 frames our model per-
forms poorly, with 107% average absolute error on the test set, using Leapfrog integra-
tor.
In Figure 4, we show some qualitative examples of the reconstructions obtained by the
full version of HGN. The model can reconstruct the samples and its rollouts can be re-
versed in time, sped up, or slowed down by changing the value of the time step used in
the integrator. Since the HGN is designed as a generative model, we can sample from the
latent space to produce initial conditions and perform their time evolution. We show
some rollouts obtained this way in figure 5. We observe that our model is only able
to generate plausible and diverse samples in the mass-spring dataset. This behavior is
different than the one shown by [5] and might be caused by different hyper-parameter
configurations in the training procedure or some implementation mistake.
We achieve slightly larger MSE in the autoencode version and significantly larger in the




Figure 5. Examples of sample rollouts from the latent space for different physical systems.

Figure 6. Reconstruction loss and KL divergence for different GECO parameters in the Pendulum
environment.

5-frame inference problem on both the mass-spring and pendulum. The latter presents
roughly double MSE probably because of a wider span of movement. In general, these
two environments show worse results in comparison to two/three-bodies. For these last
cases, our implementation using the autoencode setting outperforms the original HGN
[5], and when using the 5-frame inference the results are similar. As we can see, these
two environments show much less average pixel MSE compared to the first ones (al-
most one order of magnitude). We believe this may be due to the differences when
rendering the instances of each dataset. The elements appearing in mass-spring and
pendulum (represented by a large yellow ball) are larger than the ones present in the
two/three bodies (two/three small coloured balls). Because of this, it would be reason-
able to assume that localization errors are more penalized in the first two environments,
since the total difference in areas is larger. Furthermore, the dynamics representing
mass-spring and pendulum show faster movements in comparison to two/three-bodies,
resulting in being harder to represent with our HGN. Consequently, we hypothesise the
following: larger elements and faster dynamics, produces higher average MSE on our
model regardless of the difficulty of the environment physics. However, this is not the
case for the original authorʼs results, who seem to struggle more on the two/three-bodies.
Surprisingly, it seems that our hyperparameter and architecture choices led to poorer
reconstruction capabilities (higher MSE) but learning better physics (qualitatively more
realistic movements).

### 4.1 Additional experiments

GECO parameter search The paper does not provide the values of GECO [2] used. In
GECO, the Lagrangian multiplier is optimized at each step with a rate γ. Figure 6 shows
the behavior of GECO for γ ∈ {0.1, 0.05, 0.01} in terms of reconstruction loss and KL
divergence. Higher values of β give a better reconstruction loss but greatly increase the
KL divergence. However, we found that hyperparameters were not consistent among
different environments and integrators. For this reason, we do not use GECO in our
experiments.

Integrators Performing the integration step is key to generate the time evolution of a
rollout given the initial state. In the HGN paper [5] the system is tested using Euler and




pixel MSE
H std
reconstr. time (s)

EULER
17.86 ± 0.13
3.81
0.32

RUNGE-KUTA 4
76.88 ± 0.08

### 1.89 LEAPFROG
14.97 ± 0.10
1961.93
0.96

YOSHIDA
14.70 ± 0.10
1893.05
### 1.61 Table 2. Comparison between four different integrators used to perform the time evolution in the
HGN. The results are measured on the simple pendulum test set. The pixel MSE values have been
multiplied by 104.

Leapfrog integration. We wonder if using higher order integration methods might boost
the performance of the rollout generation process. Therefore, we implement and test
the HGN architecture with two additional numerical integration methods: the Runge-
Kuttaʼs 4th-order integrator [13] and the 4th-order Leapfrog integrator (Yoshidaʼs algo-
rithm [14]). Table 2 shows a comparison of all four integrators on the Pendulum dataset.
Both Leapfrog and Yoshida are symplectic integrators: they guarantee to preserve the
special form of the Hamiltonian over time [15].
Table 2 shows the average pixel MSE, the averaged standard deviation of the output of
the Hamiltonian network during testing, and the reconstruction time of a single batch
(batch = 16) using the different integration methods that we have described previ-
ously. The model has been trained on the simple pendulum dataset. As we can see,
the reconstruction time increases when using higher-order integration methods, since
they require more integration steps. In general, we see that Euler integration offers a
fast and sufficiently reliable reconstruction of the rollouts. Moreover, we observe that
the fourth-order symplectic integrator (Yoshida) achieves the best performance. Sur-
prisingly, the symplectic integration methods show more variance in the output of the
Hamiltonian networks throughout a single rollout. This behavior is unexpected since
using a symplectic integration method should ideally keep the value of the Hamiltonian
invariant. We conclude that more experiments need to be performed to guarantee that
the implementation of both Leapfrog and Yoshida integration methods are faithful to
their formulation.

Integrator modelling We train the modified architecture of Section 3.2 on the Pendu-
lum dataset for 5 epochs. The architecture is the same as HGN, but the Hamiltonian Net-
work now outputs ∆q and ∆p. The average MSE error over the whole Pendulum dataset
is 1.485 × 10−3, while in the test set it is 1.493 × 10−3, which are both very close (∼ ±2%)
to those of autoencoding HGN (see Table 1). The modified architecture is still capable
of performing forward slow-motion rollouts by modifying ∆t. We set ∆t′ = ∆t
2 and we
compute the average MSE of the slow-motion reconstruction over 100 rollouts. The mod-
ified architecture achieved an error of 8x10−4, while the standard HGN achieved 9x10−4.
Note that reconstruction losses are smaller for slow-motion as the images change less
between timesteps.

Extra environments Apart from the four physical systems presented by [5] we test our
re-implementation of the HGN with physical systems that do not have a simple Hamil-
tonian expression. As described previously, these are the damped harmonic oscillator
and the double pendulum. On one hand, we are interested in a damped system since it
introduces a dissipative term to the equations of motion; a feature that differs from the
previous systems. On the other hand, the double pendulum is modelled by a non sepa-
rable Hamiltonian: H(q, p) ̸= K(p) + V (q) as described previously. In figure 7 we show
some visual examples of the reconstructions provided by the HGN trained on the two
systems. As we can see, HGN is able to reconstruct the damped oscillator with high re-
liability. Regarding the double pendulum, we observe that the model reconstructs well
small oscillations, but fails when the trajectory is too chaotic as expected. The average




Figure 7. Examples of reconstructions of the double pendulum (left) and the damped harmonic
oscillator (right).

pixel MSE of the reconstructions of the damped oscillator and the double pendulum are
6.39·10−4 and 6.91·10−4 respectively. The HGN is able to provide better reconstructions
for these systems in comparison to the mass-spring and pendulum systems.

## 5 Discussion

We were able to implement and train an Hamiltonian Generative Network with simi-
lar reconstruction performance of the ones of the original paper (30% average absolute
relative error wrt to their reported values when treating it as an autoencoder). These re-
sults show that the network is capable of exploiting the Hamiltonian equations to learn
dynamics of a physical system from RGB images. However, the value of the resulting
Hamiltonian does not remain constant throughout the system evolution. This means
that the network is learning something that is different from the Hamiltonian equations
described in Section 3.3.
To make the variational sampling work, we tried performing a grid search on the Geco[2]
hyperparameters and using a fixed Lagrange multiplier as in [3]. However, despite our
best efforts, the samples produced by the variational model have very poor quality. This
is generally due to the difficulty in minimizing both KL divergence and reconstruction
loss.
We believe that further experiments are needed to understand better the behavior of the
system and to improve it. Future work could include further testing on each network ar-
chitecture, probably smaller networks would also be able to encode the needed informa-
tion. Another next step is to try the approach on more challenging (and realistic-looking)
environments. In addition, it would be interesting to tackle the transfer learning capa-
bilities of such architecture between different environments. How re-usable each net-
work is? How much faster the system is able to learn the new dynamics? Finally, another
field which could benefit from this research is model-based reinforcement learning. A
generative approach from which to sample example rollouts could be very useful for
training agents without the need of directly interacting with the environment.

### 5.1 What was easy

Once we implemented the code it resulted quite easy to perform multiple experiments
on different environments, architectures and hyper-parameters due to the codeʼs mod-
ularity and flexibility. We can define the the previously mentioned experiments and
most common testing behaviors from a set of yaml files which can then be modified
from command-line arguments. While this required extra planning and work at the
beginning it really payed off when debugging and evaluating in later stages.




### 5.2 What was difﬁcult

The main challenge we encountered is finding the correct tools to debug a model com-
posed of so many interconnected networks. The fact that it has a variational component
with a dynamic Lagrange multiplier term makes it especially tricky to train. Further-
more, no public implementation existed and some details and parameters were missing
in the original paper leading to some necessary assumptions or parameter searches.

### 5.3 Communication with original authors

We first tried to understand and re-implement the code by ourselves. Nevertheless, at
some point we had gathered a significant set of doubts and we decided to email them to
the original authors, which they answered with great detail. From that point onwards,
we sent a couple more set of doubts, also receiving answers.

Most of our doubts were about network architecture clarifications (either of unclear or
missing descriptions from the original paper), and loss function evaluation. Further-
more, they provided us with some of their environment images so we could more easily
make our environments as similar as possible.

### 5.4 Improving reproducibility

Having worked in re-implementing the whole original work, we feel it is important to
share our experience as well as providing a recommendation on how it could be made
more easily reproducible. First, having the environments data or code to generate it
available online would save the effort and, most importantly, it would constitute a base-
line against which to compare future work. Secondly, publishing all the hyperparame-
ters and more details of the networks architecture would make the whole work much eas-
ier to reproduce and require less training attempts, especially for what concerns GECO.

Acknowledgements

We thank Stathi Fotiadis for voluntarily contributing with a GECO [2] implementation
draft to the public repo and his useful feedback on code structuring. We thank the KTH
Robotics, Perception, and Learning (RPL) Lab for the computational resources provided
to us. In addition, we would like to thank the original authors for providing further
details on the implementation.

References

1.

2.
3.

A. Paszke et al. “PyTorch: An Imperative Style, High-Performance Deep Learning Library.” In: Advances in Neu-
ral Information Processing Systems 32. Ed. by H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E.
Fox, and R. Garnett. Curran Associates, Inc., 2019, pp. 8024–8035. URL: http://papers.neurips.cc/paper/9015-
pytorch-an-imperative-style-high-performance-deep-learning-library.pdf.
D. J. Rezende and F. Viola. Taming VAEs. 2018. arXiv:1810.00597 [stat.ML].
I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner. “beta-VAE:
Learning Basic Visual Concepts with a Constrained Variational Framework.” In: ICLR. 2017.

4. H. Goldstein. Classical Mechanics. Addison-Wesley, 1980.
5.

P. Toth, D. J. Rezende, A. Jaegle, S. Racanière, A. Botev, and I. Higgins. Hamiltonian Generative Networks.
2020. arXiv:1909.13789 [cs.LG].
P. Virtanen et al. “SciPy 1.0: Fundamental Algorithms for Scientiﬁc Computing in Python.” In: Nature Methods
17 (2020), pp. 261–272. DOI: 10.1038/s41592-019-0686-2.

6.

7. G. Bradski. “The OpenCV Library.” In: Dr. Dobb’s Journal of Software Tools (2000).
8.

D. P. Kingma and M. Welling. Auto-Encoding Variational Bayes. 2014. arXiv:1312.6114 [stat.ML].




9.

10.
11.

12.

13.

T. Karras, T. Aila, S. Laine, and J. Lehtinen. Progressive Growing of GANs for Improved Quality, Stability, and
Variation. 2018. arXiv:1710.10196 [cs.NE].
D. P. Kingma and J. Ba. Adam: A Method for Stochastic Optimization. 2017. arXiv:1412.6980 [cs.LG].
S. Greydanus, M. Dzamba, and J. Yosinski. Hamiltonian Neural Networks. 2019. arXiv:1906.01563
[cs.NE].
F. Segovia-Chaves. “The one-dimensional harmonic oscillator damped with Caldirola-Kanai Hamiltonian.” In:
Revista mexicana de fı́sica E 64.1 (2018), pp. 47–51.
T. Hull, W. Enright, B. Fellen, and A. Sedgwick. “Comparing numerical methods for ordinary differential equa-
tions.” In: SIAM Journal on Numerical Analysis 9.4 (1972), pp. 603–637.

14. H. Yoshida. “Symplectic integrators for Hamiltonian systems: basic theory.” In: Symposium-International As-

15.

tronomical Union. Vol. 152. Cambridge University Press. 1992, pp. 407–411.
R. M. Neal et al. “MCMC using Hamiltonian dynamics.” In: Handbook of markov chain monte carlo 2.11 (2011),
p. 2.

---
**Source PDF:** `42323eb72f9d.pdf` (2021_18_article.pdf)  
**URL:** https://zenodo.org/record/4835278/files/article.pdf
