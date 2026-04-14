R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Replication Study of ’Generative causal explanations
of black-box classiﬁers’

Ivo Verhoeven1, ID , Xinyi Chen1, ID , Qingzhi Hu1, ID , and Mario Holubar1, ID
1University of Amsterdam, Amsterdam, the Netherlands

Edited by
Koustuv Sinha

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

DOI
10.5281/zenodo.4835600

Reproducibility Summary

Scope of Reproducibility

We verify the outcome of the methodology proposed in the article, which attempts to
provide post-hoc causal explanations for black-box classifiers through causal reference.
This is achieved by replicating the code step by step, according to the descriptions in
the paper. All the claims in the paper have been examined, and we provide additional
metric to evaluate the portability, expressive power, algorithmic complexity and the data
fidelity of their framework. We have further extended their analyses to consider all
benchmark datasets used, confirming results.

Methodology

We use the same architecture and (hyper)parameters for replication. However, the code
has a different structure and we provide a more efficient implementation for the mea-
sure of information flow. In addition, Algorithm 1 in the original paper is not imple-
mented in their repository, so we have also implemented Algorithm 1 ourselves and
further extend their framework to another domain (text data), although unsuccessfully.
Furthermore, we make a detailed table in the paper to show the time used to produce
the results for different experiments reproduced. All models were trained on Nvidia
GeForce GTX 1080 GPUs provided by Surfsaraʼs LISA cluster computing service at uni-
versity of Amsterdam1.

Results

We reproduced the framework in the original paper and verified the main claims made
by the authors in the original paper. However, the GCE model in extension study did
not manage to separate causal factors and non-causal factors for a text classifier due to
the complexity of fine-tuning the model.

1This is our course project for the master course Fairness, Accountability, Confidentiality and Transparency

in AI at the University of Amsterdam. Lisa cluster: https://userinfo.surfsara.nl/systems/lisa.


Code is available at https://github.com/shin-ee-chen/UvA_FACT_2021. – SWH swh:1:dir:9d960937f2b11bb67b53bbe4eaa940c14cadf9d1.
Open peer review is available at https://openreview.net/forum?id=Vqtf4kZg2j.




What was easy

The original paper comes with extensive appendices, many of which contain crucial
details for implementation and understanding of the intended function. The authors
provide code for most of the experiments presented in the paper. Although at the begin-
ning their code repository was not functional, we use it as a reference to re-implement
our code. The author also updated their code two weeks after we start our own imple-
mentation, which made it easy for us to verify the correctness of our re-implementation.

What was difﬁcult

The codebase the authors provided was initially unusable, with missing or renamed
imports, hardcoded filepaths and an all-around convoluted structure. Additionally, the
description of Algorithm 1 is quite vague and no implementation of it was given. Beyond
this, computational expense was a serious issue, given the need for inefficient training
steps, and re-iterating training several times for hyperparameter search.

Communication with original authors

This reproducibility study is part of a course on fairness, accountability, confidentiality
and transparency in AI. Since it is a course project where we interacted with other group
in the forum, and another group also working with this paper has reached out to the
authors about problems with the initial repository, we did not find necessary to do it
again.

## 1 Introduction

Machine learning is increasingly used in different applications. The wide-scale spread
of these methods places more emphasis on transparent algorithmic decision making,
which has the potential to mitigate the potential for disruptive social effects. Yet, despite
reliable results of complex black boxes, their internal reasoning and inner workings are
not necessarily apparent to end-users or even designers. As a result, not even trained
experts can grasp the reasoning behind forecasts. Moreover, modern legislation have
necessitated the opportunity challenging these systems, especially in heavily regulated
domains, increasing the need for machine learning systems that are (post-hoc) inter-
pretable [1].

Black-box artificial intelligence approaches like Deep Neural Networks have often proven
to be able to capture complex dependencies within data, and allow for making accurate
predictions. However, the actual internal logic used by systems dependent on such ap-
proaches is often nebulous or totally unclear. In this paper, we will reproduce the paper
which focuses on the explainability aspect of AI.

Explainable Artificial Intelligence (XAI) refers to systems that seek to clarify how a black-
box AI model achieves its performance. Post-hoc XAI achieves the desired explainability
be generating reasons for decisions after having trained a black-box classifier. This is
often achieved by extracting correlations between input features and the eventual fore-
casts [2]. This paper aims to reproduce such a post-hoc XAI algorithm, capable of pro-
viding clear and interpretable explanations for complex black-box classifiers [3]. The
central contribution made by [3] is placing explanations in a causal-generative frame-
work. By using a variational auto-encoder (VAE) [4] , low dimensional representations
of the data can be achieved. By further incorporating a mutual information loss between
the classifier and the latent variables, the latent space is decorrelated into factors that




actively influence the classifierʼs prediction, and those that capture superfluous varia-
tion in the underlying dataset. The causal-VAE , dubbed a generative causal explainer
(GCE) by [3] can be studied and intervened with to provide a powerful framework for
inducing explainability.

There exists literature suggesting that some studies cannot be replicated [5]. This is
valid also for the most respected journals and conferences in AI. Steps must be taken
to ensure high trustworthiness of AI algorithms [6]. In the experiments presented here,
we re-implement the framework used by [3], extend their analyses to all benchmark
datasets discussed and provide an extension to a novel domain.
When beginning our process, the officially provided code repository corresponding to
the authorsʼ publication was not capable of running in all discussed scenarios, nor pro-
ducing results similar to those presented 2. However, our re-implementation has ascer-
tained all results, and been extended to incorporate all analyses, and can report their
framework to be reproducible. All code has been made publicly available via a Github
repository3.

## 2 Scope of Reproducibility

The original paper establishes a causal inference framework. While intuitive, this intro-
duces the additional challenge of balancing causal intervention with expressive latent
variables. To overcome this hurdle, [3] integrate causal inference into the VAE learning
objective. This system consists of two basic components: a way to describe the data dis-
tribution, and a method of generating a consistent classification model. In order to get
a clear objective of the reproduction, we consider the the main claim(s) of the original
paper as:

• Claim 1: creating a generative framework that describes a black-box classifier, and
a process that achieves this while maintaining latent descriptions that result in
high data fidelity and scalability of the overall system

• Claim 2: their objective function helps the generative model disentangle the latent
variables into causal and non-causal factors for the classifier. Their approach is
sufficient for any black-box classifier that can provide class gradients and proba-
bilities with respect to the classifier input

• Claim 3: the resulting explanations show what is important to the accompanying

classifier

• Claim 4: the learned representation may also be used to explain counterfactual

explanations as it incorporates both generative and causal modelling

The standard of reproducibility demands that machine learning methods be routinely
evaluated on the verifiability of their results. The following additional metrics (proper-
ties) will be used as measurement of reproducibility:

• Portability: the modelling domains and types of machine learning models that can

benefit from their framework

• Expressive Power: the explanation structure that can be produced by their frame-

work

• Algorithmic Complexity: the computational complexity of their algorithm

2Since, the authors have responded to suggestions and rewritten their code base substantially.
3https://github.com/shin-ee-chen/UvA_FACT_2021




• Data Fidelity: the degree of precision of the data will range from low to high fidelity.
In cases where high-faithfulness data to train the model are not necessary, low-
faithfulness data often may be used. The small amount of usable data will greatly
influence the modelʼs ability to yield accurate estimates.

## 3 Project Description

As stated, we evaluate the performance of the method proposed in paper[3] as a causal
post-hoc explainer of black-box classifiers by reproducing the code necessary. At the
beginning of this project, the code provided by the authors was not in a usable state.
Hence, we decided to reimplement the code for the necessary architectures and con-
duct experiments with the implementation details provided in the paper. By the time
we finished our implementation, the project repository had been updated to be able to
reproduce the initial claims in the paper.
Beyond just re-implementing already existing code, two extensions were considered.
First, the paper suggests a technique for selecting the K, L and λ hyperparameters used
to train the generative model (Algorithm 1). However, no implementation of this al-
gorithm is present in the authorsʼ code. To test its validity and because of the tedious
and time-consuming nature of manual hyper-parameter search, we implemented the
automated algorithm using reasonable assumptions.
Second, in an effort to verify the robustness of this method, similar experiments for im-
age classification were also conducted using a textual domain. Compared to the simple
image benchmark datasets used in the initial experiments, text classification and gener-
ation are considerably more complex. These models will be used to test the scalability
of the proposed framework.

## 4 Methodology

The Generative Causal Explainer (GCE), is at its core a generative model with aware-
ness of a discriminative black-box classifier. For the generative model, this paper exclu-
sively uses the Variational Auto-Encoder (VAE) [4]. While the VAE allows expression of
a dataset in terms of a low-dimensional posterior distribution, the addition of the classi-
fier allows for disentangling the proposed latent space into variable subsets that causally
influence decisions of the classifier and those that capture superfluous variance. The
former subset is denoted α, whereas the latter is denoted β, having cardinalities K and
L respectively.
The goal of this modelling framework is to learn a generative mapping g : (α, β) → X
that further satisfies the following criteria: p(g(α, β)) ≈ p(X), the factors (α, β) are
statistically independent and α has strong clausal influence on the classifierʼs output Y .
The proposed objective function of this framework is thus,

argmax
g∈G

C(α, Y ) + λ · D(p(g(α, β)), p(X))

(1)

where g is the GCE model that satisfies the constraints from the set of possible generative
models G, C(α, Y ) is a metric that quantifies the causal influence of α on Y and D is a
variational lower bound that measures the proximity of p(g(α, β)) to p(X). The inclusion
of the D(p(g(α, β)), p(X)) is necessary to ensure the generated explanations remain in,
and ideally closely approximate, the data distribution.
While there are several candidates for a causal influence metric, the original authors
opted for the information theoretic motivated mutual information (MI). OʼShaughnessy
et al. offer several reasons for choosing MI, including its compatibility with deep neural
networks, its ability to quantify indirect causal links between the GCEʼs latent space and




the classifier, and its equivalence to ʻinformation flowʼ in the proposed causal model
when considering do-calculus. Thus, in the above provided loss function,

C(α, Y ) = I(α; Y ) = Eα,Y

log

[

]

,

p(α, Y )
p(α)p(Y )

(2)

where I(α; Y ) is the aforementioned MI between the causal factors and the classifier. No
closed form solution computation for Eq. 2is provided. Rather, a Monte-Carlo estimator
is employed, using data samples drawn from the GCE posterior and their classifications
by the accompanying black-box classifier. For detailed explanation of the underlying
method, we direct the reader to Appendix D of [3]. Note that this estimation method
requires passing drawn samples through both the GCEʼs decoder network and the clas-
sifier, and for low variance estimates of I(α; Y ), numerous estimates are required. As
such, estimating this quantity at every training step is computationally expensive, espe-
cially when considering the cost of a vanilla VAE.

4.1 GCE Architectures

As VAEs do not explicitly limit the architectures used in the encoder and decoder net-
works, much like the classifiers in question, they can make use of the same inductive
knowledge encoded into the black-box classifiers. Thus, for image classification, given
the performance of convolutional neural networks, a similar set of networks can be
considered for the GCE. Naturally, while replicating and unspecified, the same archi-
tectures as used by OʼShaughnessy et al. are used here as well.
The image classification datasets used (see Sec. 5) are benchmark datasets of low com-
plexity. Hence, both the classification and generative models were limited to shallow
neural networks. The classifiers consisted of 2 ReLU activated convolutional layers fed
into a max-pooling layer before 2 ReLU activated linear classification layers. Drop-out
was present prior to either linear layer. In all instances, this sufficed for achieving near
perfect accuracy. Both the encoder and decoder used 3 layers of convolution (trans-
posed for the decoder), with additional linear layers for converting the feature maps.
Specifics for the models used are given in Table 3.
For text classification, the architecture is shown in Figure 4. The core architecture used
was the Long Short-Term Memory (LSTM) network [7]. The classifier consisted of a bi-
directional LSTM, whose hidden states at every time-step were concatenated and fed
into a 3 successive convolution/ReLU/max-pooling blocks, before being projected into
classification nodes via a linear layer. The embeddings used came from the 840b token
Common Crawl pre-trained 300 dimensional GloVe vectors, limited to the vocabulary
present in the SST dataset4. Ultimately, this model achieves 84% accuracy on the bi-
nary SST classification task. The encoder and decoder nets used a common VAE gen-
eration architecture [4], consisting of single layer LSTM, with embeddings not using
pre-initialised weights. The hidden and cell states at the last time-step were used for
predicting the input-dependent posterior statistics, with the posterior samples being
fed into the decoder as the initial hidden and cell states, while also being appended to
every embedding vector.
Posterior collapse, a situation where the decoder network essentially ignores the en-
coder output, proved a serious problem for text generation. To overcome this issue, an
aggressive training regiment was used [8]. Here, the encoder network is trained until
convergence before updating the decoder network, resulting in stable and informative
signals for the decoder network. This method of training is necessary for the first few
epochs, but quickly ameliorates the situation and allows for regular VAE training to con-
tinue. However, given the sheer computational expense of using aggressive training,
combining this with MC-estimation of I(α; Y ) would quickly prove intractable. As such,

4Available

at

https://gist.githubusercontent.com/bastings/b094de2813da58056a05e8e7950d4ad1/raw/

3fbd3976199c2b88de2ae62afc0ecc6f15e6f7ce/glove.840B.300d.sst.txt





(b) Sweep β1

(c) Sweep β2

(d) Sweep β3

Figure 1. Visualizations of learned latent factors for MNIST classifier trained on classes ʻ3ʼ and ʻ8ʼ.
The colour denotes the classifierʼs decision, with each adhering to a specific class. The axis gives
the additive value to each latent dimension. Complete results are in Figure 5 for MNIST 3-8, Figure
6 for MNIST 1-4-9, and Figure 7 for FMNIST 0-3-4.

both the classifier and generative model were first trained disjoint, resulting in a regular
VAE text-generator, before attempting to fine-tune into a functioning GCE.

### 4.2 Implementation

Upon start of this project, the original authorsʼ official code repository was non-functioning.
Hence, all models were implemented from scratch using the descriptions and guide-
lines provided in the original paper. The only exception to this was the MC-estimation
for information flow, although this was further optimised during the project. We ex-
clusively used PyTorch, PyTorch-Text and PyTorch-Lightning for implementation, and
all models were trained on Nvidia GeForce GTX 1080 GPUs provided by Surfsaraʼs LISA
cluster computing service.

## 5 Experimental Setup and Code

### 5.1 Datasets

Experiments using image classifiers are conducted on the traditional MNIST hand-written
digits [9] and the newer Fashion MNIST (fMNIST) datasets [10]. The official training set
of traditional MNIST was split into training and validation subsets of 50,000 and 10,000
images, respectively. The test set remained the same as the original dataset, composed
of 10,000 images. Only the images labelled ʻ3ʼ or ʻ8ʼ were used to train the binary 3/8 clas-
sifier, whereas images labelled ʻ1ʼ, ʻ4ʼ and ʻ9ʼ were selected to train the 1/4/9 classifier.
For fMNIST, the training set remains the same as the original dataset containing 60,000
images. The test set is divided into a validation set and a test set, containing 6,000 and
4,000 images, respectively. The t-shirt, dress, and coat images, labelled ʻ0ʼ,ʻ3ʼ, and ʻ4ʼ,
were used to train the 0/3/4 classifier. Both traditional MNIST and fMNIST were limited
to samples with the labels of interest. All images were scaled to size 28 × 28. In both
datasets, the train/validation/test splits was done using the file indices.
Experiments conducted using text classification used the Stanford sentiment treebank
[11] movie reviews corpus. Here the officially recommended train/validation/test splits
were used. Rather than using the 5-class fine-grained classification, only positive and
negative reviews were used, with the ʻvery-ʼ classes being converted to their less polar
alternatives.

### 5.2 Hyperparameters

In the reproduction experiments, hyperparameters are set to be the same as the original
paper. The lists of hyperparameters of CNN classifier and GCE model can be found in




Table 4 and Table 5, see Appendix 8.
Beyond just the values provided, however, Algorithm 1 from the original paper was also
implemented to conduct a hyperparameter search for K, L and λ. This procedure was
not rigorously defined in the original paper, using terms that are left open for interpre-
tation, such as ”plateaus” or ”approaches”. Due to this, some assumptions were made in
the process:

• “Plateauing” was defined as the value in question achieving a local optimum, with

the next iteration reversing its trend.

• “Approaching the value from step 1” was defined as either coming within a certain
percentage threshold of the target value, or being closer to the target value than
the next iteration.

• D and C were defined as loss values subject to minimization.

This technique requires three parameters to be chosen:

1. ξ: a factor that dictates how close to the D obtained in step 1 a value must be to be

considered as having approached D.

2. λ0: the value of λ to start with.

3. κ: the factor by which to increase λ.

In our hyperparameter search experiments, we use ξ = 0.05, λ0 = 10−3 and κ = 100.5.

### 5.3 Model Training

In reproduction experiments, we trained a GCE model to generate explanation factors
for image classifier outputs. The CNN classifier was trained for image recognition task
using SGD as optimizer. The network architecture is shown in Table 2 and the hyper-
paramters settings are listed in Table 5. The GCE model is trained to maximize the ob-
jective 1 with Adam optimizer. We use the values of K, L and λ suggested in the original
paper. Hyperparameter details can be found in Table 4.

Figure 2. High-resolution transition regions of the first causal factor in explaining the MNIST 1/4/9
classifier.

## 6 Results

### 6.1 Results reproducing original paper

Using the GCE model described in Section 4.1, explanations for the CNN classifiers
trained on MNIST and fMNIST datasets were found. The latent factors α and β are visu-
alized in Figure 1, showing exactly how g(α, β) and the classifier output change as the




(a) Information flow.

(b) Removal of latent factors.

(c) Sweep of α1.

(d) Sweep of β1.

Figure 3. Ablation study for training FMNIST dataset: (a) each latent factor affecting the classifier
performance measured by information flow. (b) comparison of classifier accuracies when data as-
pects regulated by the individual latent factors are eliminated. Figure 5(c-d) visualizes the aspects
learned by α1 and β1. The figures here are generated using the FMNIST data-set.

latent factors are modified for the 3-8 classifier. One can observe that α1 influences the
features that separate the digits 3 and 8 (the classifierʼs output being given by the colour
surrounding the digits) while retaining stylistic features unrelated to the classifier such
as skew and thickness. By contrast, non-causal factors βi controls features irrelevant to
classifier outputs. As shown in Figure 1(b-d), changing βi leads to stylistic changes of
digits but does not affect classifier predictions.
By visualizing high-resolution latent factor sweeps in Figure 2, the GCE model can assist
a practitioner in identifying important data features for classification results. As shown
in the first row from the top in Figure2, the digits ʻ4ʼ smoothly transition into ʻ9ʼ by com-
pleting the loop of the digit ʻ9ʼ while the digit stem remains fixed. Finally, the ʻ9ʼ digit
gradually transitions to a ʻ1ʼ.
To verify the causal influence of the GCE on the classifier, the information flow is studied,
along with an ablation study of individual factors on classifier performance. Figure 3(a)
shows the information flow from α factors to Y is high while the information flow from β
factors to Y is low. For the ablation study, we delete individual data points from the data
by fixing individual latent factors in each validation data set to different random values
taken from the prior N (0, 1). This decrease in the precision of the classification is seen
in Figure 3 (b). Note that modifying aspects influenced by causal factors degrades the
accuracy of the classifier substantially, whereas elimination of non-causal aspects only
has a marginal effect on the accuracy of the classifier. In the original paper, the ablation
study was only implemented for 0/3/4 classifier with FMNIST dataset. In addition, we
also plot the information flow and accuracyʼs plot for MNIST dataset (in Figure 9).
Our implementation reproduces the results in the original paper and supports the au-
thorsʼ claim that their method is able to separate causal and non-causal factors of a clas-
sifier. The learned latent factors can then be applied to explain classification decisions
of a classifier.




Table 1. Training time of classifiers, GCE models and vanilla VAE models (GCE models trained
without the causal loss term).

Dataset

K+L

Classifier

Duration (hrs)
VAE

MNIST
MNIST
FMNIST
SST

3, 8
1, 4, 9
0, 3, 4
Pos, Neg


00:01:11
00:02:47
00:02:59
00:02:49

00:05:24
00:05:17
00:03:58
05:15:09

GCE

00:34:25
00:25:04
00:23:40
-

Duration (relative to classifier)
VAE
Classifier

GCE

1.00
1.00
1.00
1.00

4.56
1.90
1.33
111.89

29.08
9.01
7.93
-

### 6.2 Results beyond original paper

Figure 8 shows results from the hyperparameter search using the version of Algorithm
1 described above with the 3/8 classifier. This corresponds to Figure 11 in the original
paper. Results for varying λ are computed for all values of K but only shown for K = 1.
The final parameter values selected by the procedure are K = 1, L = 9 and λ = 0.001.
While the parameters found here differ from the ones presented in the original paper,
the difference in results obtained when they are used is not significant.
As a final extension, an attempt was made at using an altered GCE set-up on a text-
domain. While the individual components of the GCE performed well, fine-tuning the
combination into a functioning explainer was not successful.
Table 1 shows the amount of time required to train each model. It is clear that training a
vanilla VAE takes more computational power than training a classifier on the same data.
However, an even larger cost is induced by the causal loss calculation required for the
GCE; GCE models consistently took more than five times longer to train than their VAE
counterparts with the same architecture.

## 7 Discussion

Given the results presented above, and their proximity to those presented in the orig-
inal paper, we tentatively verify all claims presented in Sec. 2. The GCE model pro-
duces high-quality examples that seem to align with the classifierʼs internal decision-
making process. Furthermore, by using interventions in the GCEʼs posterior, informa-
tion regarding features important to the black-box classifier were made apparent. Such
a framework also clearly supported the use of counterfactuals, with alterations in the
causal factors seeing the class change, and the stylistic interpretation of the produced
examples remaining unaltered. Lastly, the computation of information flow to individ-
ual factors and the performed ablation study (now extended to all initial experiment
domains), clearly show the success of mutual information in disentangling the GCEʼs
latent space into causal and non-causal factors.
However, upon implementing GCEs for simple classification models, the scalability of
the proposed framework can already be drawn into question. As mentioned in 4.1, the
introduction of a MC-estimated quantity like mutual information has significant impact
on the computational expense required for training, essentially forcing significantly
more passes of data through the decoder and classifier networks for a single weight up-
date. Even for the relatively sparse CNN-based GCE and classifier, the suggested number
of α and β estimates in conjunction with current implementation, implied 2500 addi-
tional forward passes for a single backward pass. All our experiments indicated this
being the bottleneck of the modelling pipeline. Future research into optimising this
process, for example by ensuring lower variance estimates or mixing of new sample es-
timates with older generations, could prove valuable in extending the original research.
The issues with computational efficiency were strongly exacerbated by the requirement
of a more complex generative model for the text domain. In fact, given the use of an al-




ternative training regiment, incorporating information flow to induce causal disentan-
glement would have made training until convergence virtually intractable. While the
eventual failure to fine-tune from a functioning language generation model to a GCE
could be an artefact of the pathologies plaguing text generation using auto-regressive
architectures, it also speaks to the potential of portability for this framework. Using a
classifier to produce interpretable understanding of the latent space in such a language
generation model could prove tremendously interesting, allowing for a causal frame-
work similar to the work of [12]. Furthermore, being able to fine-tune pre-trained VAEs
into GCEs would provide the suggested framework far more flexibility, essentially ad-
dressing the computational efficiency issues mentioned before.

### 7.1 Shortcomings of the original paper

The greatest shortcoming found in the original paper is the failure to address the scal-
ability problem of the approach, along with the lack of rigour when describing the hy-
perparameter selection technique.

### 7.2 Reflection: What was easy? What was difﬁcult?

It was not trivial to re-implement the proposed method because the specifics and some
details required for the implementation do not appear in the paper. However, we still
managed to reproduce the results in their paper. In order to extend the algorithm to
another domain, code modifications were required. No instruction is given in their
original repository on how this could be done, which makes it difficult to extend this
framework or apply it to other domains without reading their paper and code in depth.
Having access to the (updated) codebase was quite helpful however, as it includes some
implementation specifics that are not mentioned in their paper, which we made use of
as a source of reference when implementing and debugging our own repository.

## 8 Conclusion

While some issues and discrepancies were encountered while re-implementing, ulti-
mately we conclude that the original paper combined with the official repository are
enough to validate the claims of [3]. Results were comparable, and indeed led to high-
quality explanations. However, while the central idea is elegant and is now proven to
work, we bring into doubt the extensibility of their approach. Due to the computational
expense required, it is likely that the GCE models introduced will only function, in their
current implementation, for small datasets and simple classifiers. Finally, this project
confirms just how difficult it is to make implementations of AI transparent and repro-
ducible.

References

1.

D. V. Carvalho, E. M. Pereira, and J. S. Cardoso. “Machine learning interpretability: A survey on methods and
metrics.” In: Electronics 8.8 (2019), p. 832.

2. M. Moradi and M. Samwald. “Post-hoc explanation of black-box classiﬁers using conﬁdent itemsets.” In: Expert

Systems with Applications 165 (2021), p. 113941.

3. M. O’Shaughnessy, G. Canal, M. Connor, M. Davenport, and C. Rozell. Generative causal explanations of black-

box classiﬁers. 2020. arXiv:2006.13913 [cs.LG].
D. P. Kingma and M. Welling. Auto-Encoding Variational Bayes. 2014. arXiv:1312.6114 [stat.ML].
4.
5. M. Hutson. “Artiﬁcial intelligence faces reproducibility crisis.” In: Science 359.6377 (2018), pp. 725–726. DOI:
10.1126/science.359.6377.725. eprint: https://science.sciencemag.org/content/359/6377/725.full.pdf. URL:
https://science.sciencemag.org/content/359/6377/725.




7.

6.

O. E. Gundersen and S. Kjensmo. “State of the art: Reproducibility in artiﬁcial intelligence.” In: Proceedings of
the AAAI Conference on Artiﬁcial Intelligence. Vol. 32. 1. 2018.
S. Hochreiter and J. Schmidhuber. “Long short-term memory.” In: Neural computation 9.8 (1997), pp. 1735–
1780.
J. He, D. Spokoyny, G. Neubig, and T. Berg-Kirkpatrick. Lagging Inference Networks and Posterior Collapse
in Variational Autoencoders. 2019. arXiv:1901.05534 [cs.LG].
9.
Y. LeCun. “The MNIST database of handwritten digits.” In: http://yann. lecun. com/exdb/mnist/ (1998).
10. H. Xiao, K. Rasul, and R. Vollgraf. “Fashion-mnist: a novel image dataset for benchmarking machine learning

8.

11.

12.

algorithms.” In: arXiv preprint arXiv:1708.07747 (2017).
R. Socher, A. Perelygin, J. Wu, J. Chuang, C. D. Manning, A. Y. Ng, and C. Potts. “Recursive deep models for
semantic compositionality over a sentiment treebank.” In: Proceedings of the 2013 conference on empirical
methods in natural language processing. 2013, pp. 1631–1642.
Z. Hu, Z. Yang, X. Liang, R. Salakhutdinov, and E. P. Xing. “Toward controlled generation of text.” In: International
Conference on Machine Learning. PMLR. 2017, pp. 1587–1596.

APPENDIX

A. Text Explainer

Figure 4. Text-VAE architecture.

The text classifier used a bi-directional LSTM of 256 units. As mentioned the embed-
dings had been initialised using pre-trained GLoVe embeddings. All hidden states were
then concatenated into a single feature map. Blocks of convolutional layers (32 filters
of kernel size 3), ReLU activations and max-pooling (kernel size of 2 and stide of 2) were
applied to reduce these feature map sizes. Ultimately all feature maps were projected
down into the required number of classes using a linear layer. Adam was used as the
optimizer, using an initial learning rate of 1e-3 and decaying this by a factor of 0.85 at
every epoch.
The text-VAE follows the proposed structure given in [8] as closely as possible. The em-
beddings used 512 dimensions and the single layer LSTM 1024. The last hidden and
cell states were projected down to 32 latent dimensions. Aggressive training was used
until the mutual information between the latent variables and the encoder input sta-
bilised (typically 5 epochs). For the inner loop in the aggressive training schedule, 250
iterations were allowed, after which it was assumed the encoder had converged. The




Kullback-Leibler divergence was weighted using a linear annealing schedule between
the first 10 epochs.
Fine-tuning was attempted using λ = 1 − 3 and lr = 1e − 3 using the standard GCE
training scheme. These hyperparameters empirically proved to induce lowest lowest
causal loss after a gridsearch. Ultimately, no model improved itʼs causal loss after more
than 3 epochs.

B. Neural network architectures

Table 2. Network architecture for CNN classifier

Network architecture for CNN classifier
Input (28×28)
Conv2 (32 channels, 3×3 kernels, stride 1, pad 0)
ReLU
Conv2 (64 channels, 3×3 kernels, stride 1, pad 0) ReLU
MaxPool (2×2 kernel)
Dropout (p = 0.5)
Linear (128 units)
ReLU
Dropout (p = 0.5)
Linear (M units) Softmax
Table 3. GCE network architecture used for MNIST and fMNIST experiments

Encoder
Input (28×28)
Conv2 (64 chan., 4×4 kernels, stride 2, pad 1)
ReLU

Decoder
Input (K + L)
Linear (3136 units)
ReLU

Conv2 (64 chan., 4×4 kernels, stride 2, pad 1) Conv2T (64 chan., 4×4, 1, 1)

Conv2 (64 chan., 4×4 kernels, stride 1, pad 0) Conv2T (64 chan., 4×4, 2, 2)

ReLU

ReLU

ReLU
Linear (K + L units for both µ and σ)

ReLU
Conv2T (1 chan., 4×4, 2, 1)
Sigmoid

Table 4. Hyperparameter settings for GCE
models

MNIST

3,8


0.05
8000
5 × 10−4


classes
K
L
λ
steps
lr
N α
N β

batch size

Dataset
MNIST

1,4,9


0.1
8000
5 × 10−4


FMNIST

0,3,4


0.05
8000
10−4


Table 5. Hyperparameter settings for CNN
classifier

Dataset
MNIST MNIST

FMNIST

classes
lr
mom.

batch size
epochs

3,8
0.1
0.5


1,4,9
0.1
0.5


0,3,4
0.1
0.5




C. Additional Reproduction results


(b) Sweep β1

(c) Sweep β2

(d) Sweep β3

(e) Sweep β4

(f) Sweep β5

(g) Sweep β6

(h) Sweep β7

Figure 5. Visualizations of learned latent factors for MNIST classifier trained on classes ʼ3ʼ & ʼ8ʼ


(b) Sweep α2

(c) Sweep β1

(d) Sweep β2

Figure 6. Visualizations of learned latent factors for MNIST classifier trained on classes ʼ1ʼ & ʼ4ʼ &
ʼ9ʼ





(b) Sweep α2

(c) Sweep β1

(d) Sweep β2

(e) Sweep β3

(f) Sweep β4

Figure 7. Visualizations of learned latent factors for fMNIST classifier trained on classes ʻt-shirt-top,ʼ
ʻdress,ʼ and ʻcoat.ʼ

Figure 8. Results of parameter selection technique for the 3/8 classifier.

(a) Information flow 3/8

(b) Ablation study 3/8

(c) Information flow 1/4/9

(d) Ablation study 1/4/9

Figure 9. Information flow and ablation study for MNIST dataset.

---
**Source PDF:** `f335c5e22e3a.pdf` (2021_23_article.pdf)  
**URL:** https://zenodo.org/record/4835600/files/article.pdf
