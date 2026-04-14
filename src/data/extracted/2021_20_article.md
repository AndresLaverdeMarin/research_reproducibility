R E S C I E N C E C

Replication / ML Reproducibility Challenge 2020
[Re] Reproducibility report of ”Interpretable
Complex-Valued Neural Networks for Privacy Protection”

Arsen Sheverdin1, ID , Alko Knijff1, ID , Noud Corten1, ID , and Georg Lange1, ID
1University of Amsterdam, Amsterdam, The Netherlands

Edited by
Koustuv Sinha,
Jesse Dodge

Reviewed by
Anonymous Reviewers

Received
29 January 2021

Published
27 May 2021

Reproducibility Summary

Scope of Reproducibility

The original work by Xiang et al.1 claimed (1) that complex-valued DNNs effectively in-
crease the difficulty of inferring inputs for the adversary attacks compared to the base-
line. In addition, Xiang et al.1 stated that the (2) proposed privacy-protecting complex-
valued DNN effectively preserves the accuracy when compared to the baseline.

DOI
10.5281/zenodo.4835431

Methodology

Since the original paperʼs code was not published, all of the codebase was written in-
dependently from scratch, based solemnly on how it was described in the paper. We
mostly used a Nvidiaʼs RTX 2060 Super as the GPU and a AMD Ryzen 3600x as the CPU.
The runtime of each model was highly dependant on the architecture used. The run-
times for each model can be found in Table 2.

Results

In contrast to the first claim, we have discovered that for most of the architectures, re-
construction errors for the attacks are quite low, which means that in our models the
first claim is not supported. We also found that for most of the models, the classifica-
tion error is somewhat higher than those provided in the paper. However, these indeed
relate to the original work and partially support the second claim of the authors.

What was easy

Authors of the original paper utilized famous architectures for some of architecturesʼ
parts, such as ResNet and LeNet, that were well explained and defined in the litera-
ture. In addition, authors, provided formulas on the modified rotation-invariant Com-
plex DNN modules (ReLU, max pooling etc.), implementation of which was relatively
straightforward. The paper was based on the openly available datasets.


Code is available at https://github.com/GANA-FACT-AI/gana-fact-ai. – SWH swh:1:dir:16f75580c3619b9e0b00b6dceef8e5bf2f5a47c4.
Open peer review is available at https://openreview.net/forum?id=P30M7d9DyXw.




What was difﬁcult

The paper did not provide any information on the architecture of the critic for the WGAN,
along with the architecture of the angle discriminator utilized in inversion attack 1. It
also does not provide any information about crucial hyperparameters, such as the k
value used for k-anonimity.

Communication with original authors

We did not contact the original authors of the publication.




## 1 Introduction

Deep Neural Networks (DNNs) can process a massive data volume but require great com-
puting power to process this data. Therefore it is an interesting option for small devices
like smartphones or IoT devices to use a cloud operator for these computationally ex-
pensive tasks. Although this is an efficient way to process data, the cloud operator is
susceptible to privacy threats. A potential attacker could reconstruct or infer private
properties of the data. Possible solutions are subject of current research.
Xiang et al.1 proposed a possible solution using encryption and complex-valued neural
networks to address this problem. They showed that their approach increases the diffi-
culty of inferring inputs or properties from intermediate layer features. Our paper aims
at reproducing their findings.
Xiang et al.1 extended the standard DNN by encrypting the intermediate layer features
using complex-valued DNNs (Trabelsi et al.2). The local device encodes the original in-
put into intermediate features. Those features are encrypted and sent to a processing
unit, a complex-valued neural net located in the cloud. It does the computationally ex-
pensive operations while not being able to infer properties of its input. The result is sent
back to the local device and decrypted.
Ideally, the local device is able to decrypt the encoded data using the secret key. However,
an adversary shouldnʼt be able to decrypt the features without the key. Xiang et al.1
achieved this by rotating intermediate layer features into the complex plane using a
random angle. The angle acts as a key and can be used to reverse the rotation. The
processing unit consists of rotation-invariant operations only. Thus, the local device can
reverse the rotation after receiving the results from the processing unit. To make it hard
to deduce the angle, a generative adversarial network is trained to alter the intermediate
features to introduce obfuscation whilst keeping important information.

## 2 Scope of reproducibility

The main problem Xiang et al.1 addresses is the danger of adversary attackers being able
to recover original inputs or hidden properties of the input. Xiang et al.1 claim their
complex-valued model to be robust against these kinds of adversary attacks and show
this by attacking their model with various inversion and inference attacks. Here, they
claim that attacking their complex-valued DNNs acquires greater reconstruction loss
than when they attack the original DNNs, meaning they are more resistant to adversary
attacks. Furthermore, even though the input is encoded, they claim that their complex-
valued DNNs have almost the same utility performance (classification error rates) as the
original DNNs.
In this paper, we test the following concrete claims:

1. Xiang et al.1 proposed complex-valued DNNs effectively boost the difficulty of infer-

ring inputs for the adversary compared to the baseline.

2. Xiang et al.1 proposed their privacy-preserving complex-valued DNN largely

preserves the accuracy when compared to the baseline.

## 3 Methodology

The paper from Xiang et al.1 was replicated 1 by solely using the methods described
in their paper, since there was no implementation available online. Our approach in-
volved implementing the models used by Xiang et al.1, which included the ResNet-α, β-
20/32/44/56/110 (He et al.3), the LeNet (Lecun et al.4), the VGG-16 (Simonyan and Zisser-

1Our implementation can be found at our GitHub (https://github.com/GANA-FACT-AI/gana-fact-ai)




man5) and the AlexNet (Krizhevsky, Sutskever, and Hinton6). Most of these papers had
implementations available online, which were adjusted slightly to be able to process
complex-valued intermediate layer features. Furthermore, these DNNs had to be dis-
assembled to create the complex-valued DNN structure proposed by Xiang et al.1 that
consists of an encoder, processing module and decoder.
The encoder is in principle the same as the first few layers of the used DNN, but at the
end of the encoder a complex rotation is applied (Eq. 1).

x = exp(iθ)[a + bi]

(1)

The value a represents the regular input that is put through the encoder. The value b
is the fooling counterpart that can be seen as a different input that is also put through
the encoder. Theta is picked to be random angle, which will act as the secret key we
mentioned earlier.
The resulting features are then fed to the processing unit. The processing unit consists
of the middle layers of the used DNN. The processing unit has to deal with complex fea-
tures, which means adjustments had to be made to the regular functions that the DNN
uses. We used the proposed functions in Trabelsi et al.2 to achieve this. Furthermore
it is important that the processing unit does not change the rotation of the features, be-
cause otherwise if we try to rotate it back with our randomly picked angle we will get
random results. Therefore we also had to make the used functions rotation invariant.
Methods for achieving this were described in Xiang et al.1.
Finally the features are put through the decoder, which consists of the final layers of the
used DNN. The decoder first rotates the features back with the randomly picked angle
(Eq. 2) and then feeds the result to the final layers.

ˆy = d(R[h exp(−iθ)])

(2)

The value h represents the output of the processing unit and the value ˆy is the prediction
that the decoder d made.
Xiang et al.1 also uses a Wasserstein Generative Adversarial Network which was pro-
posed by Arjovsky, Chintala, and Bottou7 and is part of the encoder. This WGAN consists
of a generator and a critic that use complex rotations to teach the network to generate
synthesized features to hide the original ones. Since no implementation with a WGAN
that works with complex-valued features was available online, this WGAN encoder had
to be completely remade.
Lastly, for the adversary attacks, Xiang et al.1 attacked the model with inversion and in-
ference attacks. For the inversion attacks, we adopted the U-net model proposed by Ron-
neberger, Fischer, and Brox8, which had similar variants online that had to be hardly
modified to fit their implementation. For the inference attack, a model had to be imple-
mented that functions as a classifier to predict hidden properties of the input.

### 3.1 Model descriptions

Complex-valued DNNs — In Xiang et al.1 approach, the DNN is split into two local parts
that are used to encode and decode the data (encoder and decoder, respectively) and a
middle part that performs all of the heavy data processing (processing module).
In the original work, two ResNet implementations were described: ResNet-α and ResNet-
β. In ResNet-α the input is transformed until the first 16x16 feature map, from where the
output is sent to the encoder. After the encoding, the processing module transforms the
data until the first 8x8 feature map. From that point on, all following layers constitute
to the decoder. The difference in ResNet-β is that the decoder was composed by the last
residual block and the layers following it.
For describing the other classical DNNs, we only specify the encoder and the decoder,
where all the remaining layers contribute to the processing unit. For the LeNet model,




the encoder consisted of the first convolutional layer and the WGAN, whereas the de-
coder contained only the softmax layer. In the VGG-16 all layers before the last 56x56
feature map constituted the encoder. Here, the decoder consisted of fully-connected
layers and the softmax layer. For the AlexNet, the first three convolutional layersʼ out-
put was fed into the encoder, where the decoder contained fully-connected layers and
the softmax layer.

WGAN — To introduce obfuscation and make it hard for the adversary to reconstruct the
original features, a WGAN is utilized. A WGAN is a variant of a generative adversarial
network known to be more resistant against hyperparameters or mode collapse com-
pared to the original approach. The WGANs encoder is used to introduce obfuscation to
the features. The critic is only used to train the generator, and its objective is to distin-
guish rotated features from those without rotation. The generator of the WGAN shares
the same network as the encoder we described earlier. This means that one part of
the network (the encoder/generator) is trained with two different purposes; One is for
classification and the other is for the WGAN. To train the generator, the encoded and
rotated (Eq. 1) features it produced are passed to the critic, which is trying to retrieve
the original features by rotating the given features back.

a′ = ℜ[x exp(−iθ′]

(3)

The critic creates k-1 fake samples and rotates them by k-1 randomly sampled angles θ′
(Eq. 3), where θ′ ̸= θ. The critic then discriminates whether these rotated features are
close to the original complex-valued features.
From Xiang et al.1, it was unclear whether the generator is only a part of the encoder
or whether the WGAN trains all encoder layers. Because no architecture was given for
the generator, we decided to train all the encoder layers with the WGAN loss and not
introduce a stand-alone generator after the encoder.
The original WGAN uses weight clipping for the critic network. However we found that
all the weights converged to the clipping values rather quickly. Because of this we cannot
train the WGAN appropriately. To fix this issue we used a gradient penalty which was
introduced in Gulrajani et al.9.

Adversary models — Inversion attacks
The objective of the inversion attack was to reconstruct the input images from the en-
coded intermediate features. Xiang et al.1 implemented two inversion attacks: in in-
version attack 1 a new discriminator (D′) is first trained to predict the most probable
features (a∗) by learning the most likely angle at which the intermediate layer features
are rotated (Eq. 4). The most probable features (Eq. 5) are then used to help train a
decoder model that tries to reconstruct the original images (Eq. 6). In inversion attack 2
the angle prediction discriminator is not included and the attacker only trains a decoder
that tries to reconstruct the original images from the given intermediate layer features.

ˆθ = max

θ

D′(ℜ[x exp(−iˆθ)

a∗ = ℜ[x exp(−iˆθ]
ˆI = dec(a∗)

(4)

(5)

(6)

The structure of the reconstruction model for both inversion attacks was based on a
modified U-Net (Ronneberger, Fischer, and Brox8) described in the original work. U-
Net is a neural network architecture widely used for image segmentation. It is based on
an Autoencoder architecture decorated by skip connections. The skip connections help
to reconstruct the exact low-level attributes such as the location of edges. Intermediate




Table 1. Relevant statistics for the used datasets

Dataset
CIFAR-10
CIFAR-100

Labels Number of examples


60.000
600.000

Split (train/dev/test)
50.000 / 0 / 10.000
500.000 / 0 / 100.000

layer features from the encoder are scaled up to the original input size and then fed into
the U-Net, aiming to reconstruct the original image.
Inference attacks
During inference attacks a classifier is trained on either similar raw images (inference
1), rotated features a∗ (inference 2) or fully reconstructed images ˆI (inference 3). Fur-
thermore, a model is trained using k-nearest neighbors (k-NNs), where the attacker com-
pares a∗ against features of each training example to find similarities in the training set.
We did not implement the inference attacks, because the results of the inversion attacks
showed that the privacy protection was not working properly. Instead of implementing
the inference attacks, which would yield similar poor results, we decided to investigate
further into why the privacy protection was not working.

### 3.2 Datasets

Xiang et al.1 used CIFAR-10/100 (Krizhevsky10) to train the ResNets and LeNet, CUB-200
(Welinder et al.11) to train VGG-16 and CelebA (Liu et al.12) for AlexNet. Since we did
not implement VGG-16 and AlexNet, we only used the CIFAR-10/100 datasets using the
train/test split described in Table 1. Each split was halved to create two smaller datasets
used for training/testing either the privacymodel or the adversary attacker. Before train-
ing, all datasets were normalized.

### 3.3 Hyperparameters

Unfortunately, none of the standard hyperparameters such as learning rate, optimizer,
weight decay, etc. were mentioned in the paper. Therefore we had to adapt and choose
them ourselves. For the WGAN, we used the hyperparameters given in the original im-
plementation by Arjovsky, Chintala, and Bottou7. We implemented weight clipping and
gradient penalty. For the first one, we used RMSprop with a learning rate of 5e−5 for
both the generator and the critic. Weights were clipped between −0.01 and 0.01 for the
Criticʼs weights.
As this learning rate was too low for the classification task, we used a different optimizer.
Adam was used with a learning rate of 5e−4. For the gradient penalty approach, we set
lambda to 10 and used Adam with a learning rate of 5e−4. We did not do an intensive
hyperparameter search to optimise these parameters.
Finally, another hyperparameter specific to this paper is called k. k represents the num-
ber of times the discriminator decides on an input per iteration. The discriminator al-
ways has to calculate a real score based on the real features a, so there are k-1 fake inputs
that determine the fake score. This hyperparameter is also never defined in the paper.
We set the k value on 8, and we have not been able to test other options, unfortunately.
We trained our adversary networks with the Adam optimizer and a learning rate of 5e−4.
For training the U-net we used the Mean Squared Error loss and for training the angle
predictor network we used the Absolute Mean loss.

### 3.4 Experimental setup and code

Since PyTorch currently does not fully support complex-valued tensors, we chose to split
up the ʼrealʼ part and the ʼimaginary partʼ into two tensors, where we have created new
complex functions to process these two tensors correctly.




We introduced complex and, most-importantly, rotation-invariant ReLU, BatchNorm,
and MaxPool layers according to the original workʼs formulae. In addition, we have
also discovered that for Complex Linear Layers, the bias term should not be involved in
matrix computations, even though it was only mentioned for the case Complex Convo-
lutional Layers in the original paper.
The architecture of processing unit is designed so that after the the features x from en-
coder are passed through processing unit, we could express the output as a complex
rotation of outputs of processing unit, i.e Φ(x), specifically it means:

To keep the equation 7 true for the Convolutional Linear Layers Φ(eiθx) and eiθΦ(x)
should be equal to each other, meaning that for:

Φ(eiθx) = eiθΦ(x)

(7)

Φ(eiθx) = w · (eiθx) + b

eiθΦ(x) = eiθ(w · x + b)

(8)

(9)

Given any θ, we see that the equality would hold only if b = 0, which would mean that
no bias term would be needed. This is exactly the objective of rotation invariance for
our network as it was mentioned in the publication.
In the original work, the Criticʼs architecture was not described, so some assumptions
regarding its architecture were made. We found that one linear layer is not sufficient.
Thus, we added a convolution, a ResNet block and another convolution. Since the LeNet
network looks very different from the ResNet networks we decided to change to the critic
architecture to look more like the generator of LeNet.
In the paper, they describe how the decoder of the AlexNet only consists of a softmax
layer. This is not possible, because they train the network on the attributes of CelebA
and since multiple attributes per image are used, introduction of a sigmoid function is
essential. The output of the last layer in the decoder is a sigmoid and the binary cross-
entropy loss is applied in order to estimate how well it assigns attributes to each image.
The paper implements inversion and inference attacks to test whether it is preserving
the privacy. For inversion attack 1 it uses a network to determine the angle that was most
likely used for rotation. We decided to implement this network by creating a network
that is identical to the critic that we used for that specific network.
The U-Net architecture used in the inversion attacks is constructed using 6 convolutional
layers per block, instead of the standard 2 convolutional layers per block. Furthermore,
the U-net architecture consisted of 4 down and 4 upsampling blocks. Each downsam-
pling block reduced the featuresʼ dimensions by 2, while the up-sampling ones doubled
the aforementioned dimensions. Thus, input and output image widths and heights were
preserved.
We found that the inversion attacks were reconstructing the images very well when we
used them on our trained networks. Adding a convolution layer without a ReLU acti-
vation function to our generator increased the overall reconstruction loss, effectively
making our network preserve the privacy better. This was further improved by ran-
domly swapping a and b in our generator, which lead to a significant increase in the
reconstruction loss.
From all the networks that were used in Xiang et al.1 we implemented LeNet and the
ResNet-32/44/56/110-α, β architectures. We did not implement the other architectures,
because the ResNet and LeNet architectures showed that the privacy protection was not
working as described. We decided to continue our investigation into ResNet and LeNet,
instead of implementing more networks which would face the same problems as ResNet
and LeNet.




Table 2. Average runtime for each model

Model
LeNet
ResNet-32-a
ResNet-32-b
ResNet-44-a
ResNet-44-b
ResNet-56-a
ResNet-56-b
ResNet-110-a
ResNet-110-b

Average Runtime
48 m
2h 29m
2h 41m
3h 15m
3h 08m
3h 34m
3h 23m
3h 20m
3h 12m

Table 3. Inversion attack 1 and 2 results

Inversion Attack 1

Inversion Attack 2

Paper
Model
0.2405
LeNet
ResNet-32-α
0.2569
ResNet-32-β
0.2515
ResNet-44-α
0.2746
ResNet-44-β
0.2511
ResNet-56-α
0.2804
ResNet-56-β
0.2585
ResNet-110-α 0.3081
ResNet-110-β
0.2582

Reproduced
0.1499
0.0277
0.0292
0.0256
0.0190
0.1031
0.0242
0.0292
0.0207

Paper
0.1027
0.2412
0.2425
0.2419
0.2397
0.2377
0.2358
0.2495
0.2414

Reproduced
0.1244
0.0464
0.0323
0.0293
0.0383
0.0399
0.0483
0.0447
0.0321

### 3.5 Computational requirements

We mostly used a RTX 2060 super for the GPU and a ryzen 3600x for the CPU. The runtime
of each model was highly dependant on the architecture used. The runtimes for each
model can be found in Table 2.

## 4 Results

### 4.1 Results reproducing original paper

In these sections we show the results produced by our network and relate them to the
claims introduced in section 2.

Increased difﬁculty of inferring inputs — In this section we show the results that relate to the
first claim (1) based on what our initial implementation of our networks produced. Ta-
ble 3 shows the reconstruction errors of multiple different networks with the old im-
plementation when attacked with inversion attack 1 and 2. The table shows that the
reconstruction errors of our networks are much lower than the reconstruction errors
of the paperʼs networks. We can therefore say that the first claim is not supported by
these networks. The reconstructed images that were created by inversion attack 1 on
the ResNet-32-α network can be seen in Figure 1b. The reconstructed images look very
similar to the original images, further proving that the first claim is not supported.
In Table 3 we can see the results of attacking our new implementation network with
inversion attack 1 and 2. Here we see that the results look a lot more similar and we
can therefore say that the first claim is supported under our new implementation. This
claim is further supported by Figure 1 where the reconstructed images can be seen of
the new implementation network.




LeNet-5 architecture

ResNet-32-α architecture

Figure 1. Image reconstruction after inversion attack 1. Original images on the left,
reconstructed images on the right of each atchitecture

Table 4. Classification Errors of the paperʼs
results (left) and the reproduced results (right)

Model
LeNet
ResNet-32-α
ResNet-32-β
ResNet-44-α
ResNet-44-β
ResNet-56-α
ResNet-56-β
ResNet-110-α
ResNet-110-β

Classification Error
Paper Reproduced
17.95
10.48
11.12
11.08
10.51
11.53
11.28
11.97
11.85

59.62
19.53
25.00
26.09
26.48
25.78
28.91
24.22
### 28.17 Figure 2. Image reconstructions, trained on
CIFAR10 and ResNet-22-α. a) Original im-
ages. b) Model without ReLU at the end of
the generator. c) Model with ReLU at the
end of the generator. d) Model trained while
randomly swapping a and b; The WGAN was
not trained, however, the adversary is not
able to reconstruct the inputs. Also, the ac-
curacy of the classifier didnʼt change using
this approach.

Preservation of accuracy — In this section we show the results that relate to the second
claim (2). Table 4 shows the classification errors of the old implementation of our net-
works. The table shows that our networkʼs classification errors are quite a bit higher
than the paperʼs classification errors. However our networkʼs classification errors are
still quite low, which is why the results partially support the second claim. In table 4
we can see the classification errors of the new implementation of our networks. We see
that the classification error is quite similar to the old implementation and therefore also
partially supports the second claim.

### 4.2 Results beyond original paper

Linear activation at the end of the generator — The encoded features are rotated in the com-
plex plane. Thus, their values can become negative. However, if a and b contain only
positive values due to a ReLU activation at the end of the WGANs generator, finding the
initial angle would be easy for an adversary. Therefore, we concluded that the ReLU
has to be replaced or omitted. Empirically, we confirmed this as we found that the
model spreads obfuscation and the adversary needs much more time to train. However,
when training until convergence, we werenʼt able to confirm a significant difference in
reconstruction error when compared to the model with ReLU. Reconstructed images
are compared in Figure 2a-c. This underlines our general concern regarding the WGAN
being too weak compared to the adversary. Again, we want to pay attention to the ad-
versaryʼs slow convergence rate when not using the ReLU activation. At first glance, the
model seems to converge with a high reconstruction error which might lead to a wrong
conclusion if training is stopped too early.




Figure 3. Training of the adversary model. Random swapping of a and b yields a significantly higher
reconstruction error. The models with and without ReLU have similar reconstruction errors, but
the model without ReLU needs much longer to train as it introduces better obfuscation.

K-anonymity is questionable — There is no good way to test how the GAN is performing ex-
cept training an adversary. If the adversary is trained poorly, there could be another
adversary that is able to reconstruct the images much better. To test the adversary, we
disabled the training of the WGAN and instead randomly swapped the encoded features
a with the randomly sampled feature b. The decoder had access to this information and
thus was able to perform as good as the normal classifier. Surprisingly, the adversary
performed really poor and was not able to reconstruct the images. Instead, the adver-
sary reconstructed an image that was very blurred and an interpolation between the two
images. Our results are shown in Figure 2.
Comparing the reconstructed images to the images of Xiang et al.1, we found that they
look really similar. This skepticism is further supported by the fact that the images
shown in appendix B of Xiang et al.1 seem to be an interpolation of two images. Fi-
nally the average angle errors shown in table 4 of Xiang et al.1 are all π/4 except for one
(VGG-16). This seems questionable since this is equal to the initial angle that lies ex-
actly in between a and b. These reasons combined make us doubt the k-anonimity that
is claimed and makes us contemplate that it is 2-anonimity instead. This 2-anonimity
means that the results are just interpolations of a and b, and the attacker just has to
deceiver on from the other.
All of this evidence suggests that an adversary could be able to reconstruct two images
if it would be designed to do so. However, this questions the k-anonymity, which could
be reduced to a 2-anonymity by selecting a better adversary.

## 5 Discussion

From the results of the initial implementation of the networks (without removing the
ReLU and adding the swapping of a and b in the generator) we can see that we do not re-
produce the results of Xiang et al.1. Our networks donʼt protect the privacy as the images
can be perfectly reconstructed and the properties can be perfectly inferred. Therefore
the first claim (1) is not supported by our results. The classification errors are however
quite low and even though they are higher than those from Xiang et al.1, we think that
with the right parameters we could have achieved the same classification errors as them.
Therefore we do think that the second claim (2) is supported even though our results only
show partial support.
The splitting of the networks in Xiang et al.1 is questionable. The whole idea of the pa-
per is to have a processing unit running on the cloud so small IoT devices do not have
to deal with the computational load themselves. This of course introduces privacy con-
cerns, which the paper aims to address. However when we look at the way Xiang et al.1




splits the networks into three parts, we see that a lot of computational effort is being
put on the encoder and decoder networks. When we look at how they split the ResNet
networks for example, approximately only one third of the computational effort is put
on the processing unit. If this way of splitting is the only way the privacy can be pro-
tected, then it is questionable whether networks like this can actually be used on IoT
devices. Also, the local device has to keep the dataset during inference in order to sam-
ple b. However, IoT devices lack storage capacity which could lead to major difficulties
in practice.
The way Xiang et al.1 show their results of the inference attacks is questionable as well.
They decided to evaluate the classification of the network performing the attack and the
evaluation of the privacy of their network on different parts of the datasets. From an
evaluation point of view, we do not understand why they did this. What is worse is that
it seems they chose the dataset parts in such a way that their results seem better than
they actually are. For example, they evaluate the classification on the 20 major super
classes of CIFAR-100, but they evaluate the privacy on all 100 classes. By definition this
means that the privacy error will be higher than the classification error, which is exactly
what they want, hence why it seems a bit like cheating.
The choice of the U-Net as the adversary is unclear to us. We donʼt see any value in
first upsampling the features followed by downsampling them in the first part of the
U-Net. In addition, the input of the U-Net has no important low-level features as they
are upscaled, so the value of the skip connections is questionable to us. We think itʼd
be sufficient if the adversary consists of a simple decoder that reconstructs images by
upsampling and applying convolutions.

### 5.1 What was easy

Overall we found Xiang et al.1 quite difficult to understand and reproduce, but what
did make it a lot easier was the different implementations that were already online. For
most networks that they used we found an implementation online that we could use and
especially the complex neural network implementations were very useful.

• Datasets, such as CIFAR-10/100 (Krizhevsky10) and CelebA (Liu et al.12) are publicly

available and are easy to get access to.

• Main architecture for the privacy model is based on the existing and well docu-
mented architectures such as ResNet (He et al.3), LeNet (Lecun et al.4), AlexNet
(Krizhevsky, Sutskever, and Hinton13), etc.

### 5.2 What was difﬁcult

Some crucial details such as discriminator architecture and major hyper-parameters
were not included in the publication, making it difficult to properly replicate the results
with sufficient precision. One of the main hyper-parameters that were missing were
the learning rates, optimizers and weight decay values that were used. This particu-
larly, made implementation of WGAN vague and we had to make a lot of assumptions.
This is especially a problem, since the WGAN is the only part that can provide the pri-
vacy protection, so if the WGAN does not work properly we cannot achieve the privacy
protection that they claim in the paper.
Description of the inversion attacks (1) and (2) mentioned in section 4.3 were not consis-
tent with the description of experiments in section 5. For example, the authors state in
the section 4.3 of the paper that inversion attack 1 implies estimation of proper angle ˆθ,
which would allow the estimation of original features a∗, which could be later passed
to inversion model. Additionally, the description also implies the discriminator that is
used to train the angle-prediction. In the implementation part of section 5, authors state




that the inversion model is based on the U-Net, however, there was no architecture de-
scription of the angle-estimator (which we assumed is an another neural network), nor
discriminator that is used for training of such estimator. What obfuscates it further is
the fact that the authors did not make clear distinctions between the aforementioned
attacks (1) and (2) in the ”implementation details” section, confusing as to which attack
and in what way does the aforementioned U-Net architecture actually relate.

References

1.

2.

3.

4.

5.

6.

L. Xiang, H. Ma, H. Zhang, Y. Zhang, J. Ren, and Q. Zhang. Interpretable Complex-Valued Neural Networks for
Privacy Protection. 2020. arXiv:1901.09546 [cs.LG].
C. Trabelsi, O. Bilaniuk, D. Serdyuk, S. Subramanian, J. F. Santos, S. Mehri, N. Rostamzadeh, Y. Bengio, and C. J.
Pal. “Deep Complex Networks.” In: CoRR abs/1705.09792 (2017). arXiv:1705.09792. URL: http://arxiv.org/abs/
1705.09792.
K. He, X. Zhang, S. Ren, and J. Sun. “Deep Residual Learning for Image Recognition.” In: CoRR abs/1512.03385
(2016). arXiv:1512.03385. URL: http://arxiv.org/abs/1512.03385.
Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner. “Gradient-Based Learning Applied to Document Recognition.” In:
Proceedings of the IEEE 86 (Dec. 1998), pp. 2278–2324. DOI: 10.1109/5.726791.
K. Simonyan and A. Zisserman. Very Deep Convolutional Networks for Large-Scale Image Recognition. 2015.
arXiv:1409.1556 [cs.CV].
A. Krizhevsky, I. Sutskever, and G. E. Hinton. “ImageNet Classiﬁcation with Deep Convolutional Neural Net-
works.” In: Advances in Neural Information Processing Systems. Ed. by F. Pereira, C. J. C. Burges, L. Bottou,
and K. Q. Weinberger. Vol. 25. Curran Associates, Inc., 2012, pp. 1097–1105. URL: https://proceedings.neurips.
cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf.

9.

8.

7. M. Arjovsky, S. Chintala, and L. Bottou. “Wasserstein Generative Adversarial Networks.” In: Proceedings of the
34th International Conference on Machine Learning. Ed. by D. Precup and Y. W. Teh. Vol. 70. Proceedings
of Machine Learning Research. International Convention Centre, Sydney, Australia: PMLR, 2017, pp. 214–223.
URL: http://proceedings.mlr.press/v70/arjovsky17a.html.
O. Ronneberger, P. Fischer, and T. Brox. “U-Net: Convolutional Networks for Biomedical Image Segmentation.”
In: CoRR abs/1505.04597 (2015). arXiv:1505.04597. URL: http://arxiv.org/abs/1505.04597.
I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. C. Courville. “Improved Training of Wasserstein GANs.”
In: CoRR abs/1704.00028 (2017). arXiv:1704.00028. URL: http://arxiv.org/abs/1704.00028.
A. Krizhevsky. “Learning multiple layers of features from tiny images.” In: CoRR (2009).
P. Welinder, S. Branson, T. Mita, C. Wah, F. Schroff, S. Belongie, and P. Perona. Caltech-UCSD Birds 200. Tech.
rep. CNS-TR-2010-001. California Institute of Technology, 2010.
Z. Liu, P. Luo, X. Wang, and X. Tang. “Deep Learning Face Attributes in the Wild.” In: Proceedings of International
Conference on Computer Vision (ICCV). 2015.
A. Krizhevsky, I. Sutskever, and G. E. Hinton. “ImageNet Classiﬁcation with Deep Convolutional Neural Net-
works.” In: Advances in Neural Information Processing Systems. Ed. by F. Pereira, C. J. C. Burges, L. Bottou,
and K. Q. Weinberger. Vol. 25. Curran Associates, Inc., 2012, pp. 1097–1105. URL: https://proceedings.neurips.
cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf.

10.
11.

12.

13.

---
**Source PDF:** `65bb5634dbaf.pdf` (2021_20_article.pdf)  
**URL:** https://zenodo.org/record/4835431/files/article.pdf
