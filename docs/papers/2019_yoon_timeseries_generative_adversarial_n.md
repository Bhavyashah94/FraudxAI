---
title: "Time-series Generative Adversarial Networks"
authors: "yoon"
year: 2019
arxiv_id: "1910.08260"
original_file: "1910.08260.pdf"
pdf_path: "docs/papers\2019_yoon_timeseries_generative_adversarial_n.pdf"
---

# Time-series Generative Adversarial Networks

**Authors:** Yoon et al.  
**Year:** 2019 | **arXiv:** [`1910.08260`](https://arxiv.org/abs/1910.08260)  
**Local PDF:** [`2019_yoon_timeseries_generative_adversarial_n.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_yoon_timeseries_generative_adversarial_n.pdf)

---

# **Time-series Generative Adversarial Networks** 

**Jinsung Yoon Daniel Jarrett** University of California, Los Angeles, USA University of Cambridge, UK `jsyoon0823@g.ucla.edu daniel.jarrett@maths.cam.ac.uk` 

**Mihaela van der Schaar** University of Cambridge, UK University of California, Los Angeles, USA Alan Turing Institute, UK `mv472@cam.ac.uk` , `mihaela@ee.ucla.edu` 

## **Abstract** 

A good generative model for time-series data should preserve _temporal dynamics_ , in the sense that new sequences respect the original relationships between variables across time. Existing methods that bring generative adversarial networks (GANs) into the sequential setting do not adequately attend to the temporal correlations unique to time-series data. At the same time, supervised models for sequence prediction—which allow finer control over network dynamics—are inherently deterministic. We propose a novel framework for generating realistic time-series data that combines the flexibility of the unsupervised paradigm with the control afforded by supervised training. Through a learned embedding space jointly optimized with both supervised and adversarial objectives, we encourage the network to adhere to the dynamics of the training data during sampling. Empirically, we evaluate the ability of our method to generate realistic samples using a variety of real and synthetic time-series datasets. Qualitatively and quantitatively, we find that the proposed framework consistently and significantly outperforms state-of-the-art benchmarks with respect to measures of similarity and predictive ability. 

## **1 Introduction** 

What is a good generative model for time-series data? The temporal setting poses a unique challenge to generative modeling. A model is not only tasked with capturing the distributions of features _within_ each time point, it should also capture the potentially complex dynamics of those variables _across_ time. Specifically, in modeling multivariate sequential data **x** 1: _T_ = ( **x** 1 _, ...,_ **x** _T_ ), we wish to accurately capture the conditional distribution _p_ ( **x** _t|_ **x** 1: _t−_ 1) of temporal transitions as well. 

On the one hand, a great deal of work has focused on improving the temporal dynamics of autoregressive models for sequence prediction. These primarily tackle the problem of compounding errors during multi-step sampling, introducing various training-time modifications to more accurately reflect testing-time conditions [1, 2, 3]. Autoregressive models explicitly factor the distribution of sequences into a product of conditionals<sup>�</sup> _t_<sup>_p_(</sup><sup>**x**</sup><sup>_t|_</sup><sup>**x**1:</sup><sup>_t−_1).However, while useful in the context of</sup> forecasting, this approach is fundamentally deterministic, and is not truly _generative_ in the sense that new sequences can be randomly sampled from them without external conditioning. On the other hand, a separate line of work has focused on directly applying the generative adversarial network (GAN) framework to sequential data, primarily by instantiating recurrent networks for the roles of generator and discriminator [4, 5, 6]. While straightforward, the adversarial objective seeks to model _p_ ( **x** 1: _T_ ) directly, without leveraging the autoregressive prior. Importantly, simply summing the standard GAN loss over sequences of vectors may not be sufficient to ensure that the dynamics of the network efficiently captures stepwise dependencies present in the training data. 

33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 

In this paper, we propose a novel mechanism to tie together both threads of research, giving rise to a generative model explicitly trained to preserve temporal dynamics. We present Time-series Generative Adversarial Networks (TimeGAN), a natural framework for generating realistic time-series data in various domains. First, in addition to the _unsupervised_ adversarial loss on both real and synthetic sequences, we introduce a stepwise _supervised_ loss using the original data as supervision, thereby explicitly encouraging the model to capture the stepwise conditional distributions in the data. This takes advantage of the fact that there is more information in the training data than simply whether each datum is real or synthetic; we can expressly learn from the transition dynamics from real sequences. Second, we introduce an _embedding network_ to provide a reversible mapping between features and latent representations, thereby reducing the high-dimensionality of the adversarial learning space. This capitalizes on the fact the temporal dynamics of even complex systems are often driven by fewer and lower-dimensional factors of variation. Importantly, the supervised loss is minimized by jointly training both the embedding and generator networks, such that the latent space not only serves to promote parameter efficiency—it is specifically conditioned to facilitate the generator in learning temporal relationships. Finally, we generalize our framework to handle the mixed-data setting, where both static and time-series data can be generated at the same time. 

Our approach is the first to combine the flexibility of the unsupervised GAN framework with the control afforded by supervised training in autoregressive models. We demonstrate the advantages in a series of experiments on multiple real-world and synthetic datasets. Qualitatively, we conduct t-SNE [7] and PCA [8] analyses to visualize how well the generated distributions resemble the original distributions. Quantitatively, we examine how well a post-hoc classifier can distinguish between real and generated sequences. Furthermore, by applying the "train on synthetic, test on real (TSTR)" framework [5, 9] to the sequence prediction task, we evaluate how well the generated data preserves the predictive characteristics of the original. We find that TimeGAN achieves consistent and significant improvements over state-of-the-art benchmarks in generating realistic time-series. 

## **2 Related Work** 

TimeGAN is a generative time-series model, trained adversarially and jointly via a learned embedding space with both supervised and unsupervised losses. As such, our approach straddles the intersection of multiple strands of research, combining themes from autoregressive models for sequence prediction, GAN-based methods for sequence generation, and time-series representation learning. 

Autoregressive recurrent networks trained via the maximum likelihood principle [10] are prone to potentially large prediction errors when performing multi-step sampling, due to the discrepancy between _closed-loop_ training ( _i.e._ conditioned on ground truths) and _open-loop_ inference ( _i.e._ conditioned on previous guesses). Based on curriculum learning [11], Scheduled Sampling was first proposed as a remedy, whereby models are trained to generate output conditioned on a mix of both previous guesses and ground-truth data [1]. Inspired by adversarial domain adaptation [12], Professor Forcing involved training an auxiliary discriminator to distinguish between free-running and teacher-forced hidden states, thus encouraging the network’s training and sampling dynamics to converge [2]. Actor-critic methods [13] have also been proposed, introducing a critic conditioned on target outputs, trained to estimate next-token value functions that guide the actor’s free-running predictions [3]. However, while the motivation for these methods is similar to ours in accounting for stepwise transition dynamics, they are inherently deterministic, and do not accommodate explicitly sampling from a learned distribution—central to our goal of synthetic data generation. 

On the other hand, multiple studies have straightforwardly inherited the GAN framework within the temporal setting. The first (C-RNN-GAN) [4] directly applied the GAN architecture to sequential data, using LSTM networks for generator and discriminator. Data is generated recurrently, taking as inputs a noise vector and the data generated from the previous time step. Recurrent Conditional GAN (RCGAN) [5] took a similar approach, introducing minor architectural differences such as dropping the dependence on the previous output while conditioning on additional input [14]. A multitude of applied studies have since utilized these frameworks to generate synthetic sequences in such diverse domains as text [15], finance [16], biosignals [17], sensor [18] and smart grid data [19], as well as renewable scenarios [20]. Recent work [6] has proposed conditioning on time stamp information to handle irregularly sampling. However, unlike our proposed technique, these approaches rely only on the binary adversarial feedback for learning, which by itself may not be sufficient to guarantee specifically that the network efficiently captures the temporal dynamics in the training data. 

2 

Finally, representation learning in the time-series setting primarily deals with the benefits of learning compact encodings for the benefit of downstream tasks such as prediction [21], forecasting [22], and classification [23]. Other works have studied the utility of learning latent representations for purposes of pre-training [24], disentanglement [25], and interpretability [26]. Meanwhile in the static setting, several works have explored the benefit of combining autoencoders with adversarial training, with objectives such as learning similarity measures [27], enabling efficient inference [28], as well as improving generative capability [29]—an approach that has subsequently been applied to generating discrete structures by encoding and generating entire sequences for discrimination [30]. By contrast, our proposed method generalizes to arbitrary time-series data, incorporates stochasticity at each time step, as well as employing an embedding network to identify a lower-dimensional space for the generative model to learn the stepwise distributions and latent dynamics of the data. 

Figure 1(a) provides a high-level block diagram of TimeGAN, and Figure 2 gives an illustrative implementation, with C-RNN-GAN and RCGAN similarly detailed. For purposes of expository and experimental comparison with existing methods, we employ a standard RNN parameterization. A table of related works with additional detail can be found in the Supplementary Materials. 

## **3 Problem Formulation** 

Consider the general data setting where each instance consists of two elements: static features (that do not change over time, e.g. gender), and temporal features (that occur over time, e.g. vital signs). Let _S_ be a vector space of static features, _X_ of temporal features, and let **S** _∈S,_ **X** _∈X_ be random vectors that can be instantiated with specific values denoted **s** and **x** . We consider tuples of the form ( **S** _,_ **X** 1: _T_ ) with some joint distribution _p_ . The length _T_ of each sequence is also a random variable, the distribution of which—for notational convenience—we absorb into _p_ . In the training data, let individual samples be indexed by _n ∈{_ 1 _, ..., N }_ , so we can denote the training dataset _D_ = _{_ ( **s** _n,_ **x** _n,_ 1: _Tn_ ) _}n_<sup>_N_</sup> =1<sup>.Going forward, subscripts</sup><sup>_n_are omitted unless explicitly required.</sup> 

Our goal is to use training data _D_ to learn a density _p_ ˆ( **S** _,_ **X** 1: _T_ ) that best approximates _p_ ( **S** _,_ **X** 1: _T_ ). This is a high-level objective, and—depending on the lengths, dimensionality, and distribution of the data—may be difficult to optimize in the standard GAN framework. Therefore we additionally make use of the autoregressive decomposition of the joint _p_ ( **S** _,_ **X** 1: _T_ ) = _p_ ( **S** )<sup>�</sup> _t_<sup>_p_(</sup><sup>**X**</sup><sup>_t|_</sup><sup>**S**</sup><sup>_,_</sup><sup>**X**1:</sup><sup>_t−_1)</sup> to focus specifically on the conditionals, yielding the complementary—and simpler—objective of learning a density _p_ ˆ( **X** _t|_ **S** _,_ **X** 1: _t−_ 1) that best approximates _p_ ( **X** _t|_ **S** _,_ **X** 1: _t−_ 1) at any time _t_ . 

**Two Objectives** . Importantly, this breaks down the sequence-level objective (matching the joint distribution) into a series of stepwise objectives (matching the conditionals). The first is global, 



where _D_ is some appropriate measure of distance between distributions. The second is local, 



for any _t_ . Under an ideal discriminator in the GAN framework, the former takes the form of the Jensen-Shannon divergence. Using the original data for supervision via maximum-likelihood (ML) training, the latter takes the form of the Kullback-Leibler divergence. Note that minimizing the former relies on the presence of a perfect adversary (which we may not have access to), while minimizing the latter only depends on the presence of ground-truth sequences (which we do have access to). Our target, then, will be a combination of the GAN objective (proportional to Expression 1) and the ML objective (proportional to Expression 2). As we shall see, this naturally yields a training procedure that involves the simple addition of a supervised loss to guide adversarial learning. 

## **4 Proposed Model: Time-series GAN (TimeGAN)** 

TimeGAN consists of four network components: an embedding function, recovery function, sequence generator, and sequence discriminator. The key insight is that the autoencoding components (first two) are trained jointly with the adversarial components (latter two), such that TimeGAN simultaneously learns to _encode_ features, _generate_ representations, and _iterate_ across time. The embedding network provides the latent space, the adversarial network operates within this space, and the latent dynamics of both real and synthetic data are synchronized through a supervised loss. We describe each in turn. 

3 

### **4.1 Embedding and Recovery Functions** 

The embedding and recovery functions provide mappings between feature and latent space, allowing the adversarial network to learn the underlying temporal dynamics of the data via lower-dimensional representations. Let _HS , HX_ denote the latent vector spaces corresponding to feature spaces _S, X_ . Then the embedding function _e_ : _S ×_<sup>�</sup> _t_<sup>_X→HS×_�</sup> _t_<sup>_HX_takes static and temporal features to</sup> their latent codes **h** _S ,_ **h** 1: _T_ = _e_ ( **s** _,_ **x** 1: _T_ ). In this paper, we implement _e_ via a recurrent network, 



where _eS_ : _S →HS_ is an embedding network for static features, and _eX_ : _HS × HX × X →HX_ a recurrent embedding network for temporal features. In the opposite direction, the recovery function _r_ : _HS ×_<sup>�</sup> _t_<sup>_HX→S ×_�</sup> _t_<sup>_X_takes static and temporal codes back to their feature representations</sup> ˜ **s** _,_ ˜ **x** 1: _T_ = _r_ ( **h** _S ,_ **h** 1: _T_ ). Here we implement _r_ through a feedforward network at each step, 



where _rS_ : _HS →S_ and _rX_ : _HX →X_ are recovery networks for static and temporal embeddings. Note that the embedding and recovery functions can be parameterized by any architecture of choice, with the only stipulation being that they be autoregressive and obey causal ordering ( _i.e._ output(s) at each step can only depend on preceding information). For example, it is just as possible to implement the former with temporal convolutions [31], or the latter via an attention-based decoder [32]. Here we choose implementations 3 and 4 as a minimal example to isolate the source of gains. 

### **4.2 Sequence Generator and Discriminator** 

Instead of producing synthetic output directly in feature space, the generator first outputs into the embedding space. Let _ZS , ZX_ denote vector spaces over which known distributions are defined, and from which random vectors are drawn as input for generating into _HS , HX_ . Then the generating function _g_ : _ZS ×_<sup>�</sup> _t_<sup>_ZX→HS×_�</sup> _t_<sup>_HX_takes a tuple of static and temporal random vectors to</sup> synthetic latent codes **h**<sup>ˆ</sup> _S ,_ **h**<sup>ˆ</sup> 1: _T_ = _g_ ( **z** _S ,_ **z** 1: _T_ ). We implement _g_ through a recurrent network, 



where _gS_ : _ZS →HS_ is an generator network for static features, and _gX_ : _HS ×HX ×ZX →HX_ is a recurrent generator for temporal features. Random vector **z** _S_ can be sampled from a distribution of choice, and **z** _t_ follows a stochastic process; here we use the Gaussian distribution and Wiener process respectively. Finally, the discriminator also operates from the embedding space. The discrimination function _d_ : _HS ×_<sup>�</sup> _t_<sup>_HX→_[0</sup><sup>_,_1]</sup><sup>_×_�</sup> _t_<sup>[0</sup><sup>_,_1]receivesthestaticandtemporalcodes,returning</sup> classifications _y_ ˜ _S ,_ ˜ _y_ 1: _T_ = _d_ ( **h**<sup>˜</sup> _S ,_ **h**<sup>˜</sup> 1: _T_ ) . The **h**<sup>˜</sup> _∗_ notation denotes either real ( **h** _∗_ ) or synthetic ( **h**<sup>ˆ</sup> _∗_ ) embeddings; similarly, the _y_ ˜ _∗_ notation denotes classifications of either real ( _y∗_ ) or synthetic ( _y_ ˆ _∗_ ) data. Here we implement _d_ via a bidirectional recurrent network with a feedforward output layer, 





<!-- Start of picture text -->
Reconstructions Classifications Unsupervised ˜ s ,  ˜ x 1: T y ˜ S,  ˜ y 1: T<br>2 S ⇥ Q t X 2  [0 ,  1]  ⇥ . . . Loss @L R @L U<br>Learn distribution @✓r @✓d<br>p ˆ( S ,  X 1: T  ) directly r d<br>Latent Codes Supervised<br>2 HS ⇥ Q t Ht Loss h S,  h 1: T h ˆ S,  ˆ h 1: T<br>Learn conditionals @L R @L S @L S @L U<br>p ˆ( X t| S ,  X 1: t− 1)<br>@✓e @✓e @✓g @✓g<br>e g<br>Reconstruction<br>Real Sequences Random Vectors Loss<br>2 S ⇥ Q t X 2 ZS ⇥ Q t Zt Provide Latent<br>s ,  x 1: T z S,  z 1: T<br>Embedding Space<br>(a) Block Diagram (b) Training Scheme<br>Recovery<br>Embedding<br>Discriminate<br>Generate<br><!-- End of picture text -->

Figure 1: (a) Block diagram of component functions and objectives. (b) Training scheme; solid lines indicate forward propagation of data, and dashed lines indicate backpropagation of gradients. 

4 

where _⃗_ **u** _t_ = _⃗cX_ ( **h**<sup>˜</sup> _S ,_ **h**<sup>˜</sup> _t,⃗_ **u** _t−_ 1) and _⃗_ **u** _t_ = _⃗cX_ ( **h**<sup>˜</sup> _S ,_ **h**<sup>˜</sup> _t,⃗_ **u** _t_ +1) respectively denote the sequences of forward and backward hidden states, _⃗cX ,⃗cX_ are recurrent functions, and _dS , dX_ are output layer classification functions. Similarly, there are no restrictions on architecture beyond the generator being autoregressive; here we use a standard recurrent formulation for ease of exposition. 

### **4.3 Jointly Learning to Encode, Generate, and Iterate** 

First, purely as a reversible mapping between feature and latent spaces, the embedding and recovery functions should enable accurate reconstructions ˜ **s** _,_ ˜ **x** 1: _T_ of the original data **s** _,_ **x** 1: _T_ from their latent representations **h** _S ,_ **h** 1: _T_ . Therefore our first objective function is the _reconstruction loss_ , 



In TimeGAN, the generator is exposed to two types of inputs during training. First, in pure openloop mode, the generator—which is autoregressive—receives synthetic embeddings **h**<sup>ˆ</sup> _S ,_ **h**<sup>ˆ</sup> 1: _t−_ 1 ( _i.e._ its own previous outputs) in order to generate the next synthetic vector **h**<sup>ˆ</sup> _t_ . Gradients are then computed on the _unsupervised loss_ . This is as one would expect—that is, to allow maximizing (for the discriminator) or minimizing (for the generator) the likelihood of providing correct classifications _y_ ˆ _S ,_ ˆ _y_ 1: _T_ for both the training data **h** _S ,_ **h** 1: _T_ as well as for synthetic output **h**<sup>ˆ</sup> _S ,_ **h**<sup>ˆ</sup> 1: _T_ from the generator, 

_L_ U = E **s** _,_ **x** 1: _T ∼p_ � log _yS_ +<sup>�</sup> _t_<sup>log</sup><sup>_yt_</sup> � + E **s** _,_ **x** 1: _T ∼p_ ˆ� log(1 _− y_ ˆ _S_ ) +<sup>�</sup> _t_<sup>log(1</sup><sup>_−y_ˆ</sup><sup>_t_)</sup> � (8) Relying solely on the discriminator’s binary adversarial feedback may not be sufficient incentive for the generator to capture the stepwise conditional distributions in the data. To achieve this more efficiently, we introduce an additional loss to further discipline learning. In an alternating fashion, we also train in closed-loop mode, where the generator receives sequences of embeddings of actual data **h** 1: _t−_ 1 ( _i.e._ computed by the embedding network) to generate the next latent vector. Gradients can now be computed on a loss that captures the discrepancy between distributions _p_ ( **H** _t|_ **H** _S ,_ **H** 1: _t−_ 1) and _p_ ˆ( **H** _t|_ **H** _S ,_ **H** 1: _t−_ 1). Applying maximum likelihood yields the familiar _supervised loss_ , 



where _gX_ ( **h** _S ,_ **h** _t−_ 1 _,_ **z** _t_ ) approximates E **z** _t∼N_ [ˆ _p_ ( **H** _t|_ **H** _S ,_ **H** 1: _t−_ 1 _,_ **z** _t_ )] with one sample **z** _t_ —as is standard in stochastic gradient descent. In sum, at any step in a training sequence, we assess the difference between the actual next-step latent vector (from the embedding function) and synthetic next-step latent vector (from the generator—conditioned on the actual historical sequence of latents). While _L_ U pushes the generator to create realistic sequences (evaluated by an imperfect adversary), _L_ S further ensures that it produces similar stepwise transitions (evaluated by ground-truth targets). 



<!-- Start of picture text -->
L R L U L U L U<br>Recovery Discriminate Discriminate Discriminate<br>˜ s x ˜ t y ˜ t y ˜ S y ˜ t y ˜ t<br>rS rX dX dS dX dX<br> − u t −! u t  − u t −! u t u t s<br> − −!  − −!<br>cX cX cX cX cX<br>h S h t L S h ˆ t h ˆ S x ˆ t x ˆ t<br>rX rX<br>eS eX gX gS h ˆ t h ˆ t s<br>gX gX<br>s x t z t z S<br>z t z t<br>Embedding Generate Generate Generate<br>(a) TimeGAN (b) C-RNN-GAN (c) RCGAN<br><!-- End of picture text -->

Figure 2: (a) TimeGAN instantiated with RNNs, (b) C-RNN-GAN, and (c) RCGAN. Solid lines denote function application, dashed lines denote recurrence, and orange lines indicate loss computation. 

5 

**Optimization** . Figure 1(b) illustrates the mechanics of our approach at training. Let _θe, θr, θg, θd_ respectively denote the parameters of the embedding, recovery, generator, and discriminator networks. The first two components are trained on both the reconstruction and supervised losses, 



where _λ ≥_ 0 is a hyperparameter that balances the two losses. Importantly, _L_ S is included such that the embedding process not only serves to reduce the dimensions of the adversarial learning space—it is actively conditioned to facilitate the generator in learning temporal relationships from the data. Next, the generator and discriminator networks are trained adversarially as follows, 



where _η ≥_ 0 is another hyperparameter that balances the two losses. That is, in addition to the unsupervised minimax game played over classification accuracy, the generator additionally minimizes the supervised loss. By combining the objectives in this manner, TimeGAN is simultaneously trained to encode (feature vectors), generate (latent representations), and iterate (across time). 

In practice, we find that TimeGAN is not sensitive to _λ_ and _η_ ; for all experiments in Section 5, we set _λ_ = 1 and _η_ = 10. Note that while GANs in general are not known for their ease of training, we do not discover any additional complications in TimeGAN. The embedding task serves to regularize adversarial learning—which now occurs in a lower-dimensional latent space. Similarly, the supervised loss has a constraining effect on the stepwise dynamics of the generator. For both reasons, we do not expect TimeGAN to be _more_ challenging to train, and standard techniques for improving GAN training are still applicable. Algorithm pseudocode and illustrations with additional detail can be found in the Supplementary Materials. 

## **5 Experiments** 

**Benchmarks and Evaluation** . We compare TimeGAN with RCGAN [5] and C-RNN-GAN [4], the two most closely related methods. For purely autoregressive approaches, we compare against RNNs trained with teacher-forcing (T-Forcing) [33, 34] as well as professor-forcing (P-Forcing) [2]. For additional comparison, we consider the performance of WaveNet [31] as well as its GAN counterpart WaveGAN [35]. To assess the quality of generated data, we observe three desiderata: (1) _diversity_ —samples should be distributed to cover the real data; (2) _fidelity_ —samples should be indistinguishable from the real data; and (3) _usefulness_ —samples should be just as useful as the real data when used for the same predictive purposes (i.e. train-on-synthetic, test-on-real). 

**(1) Visualization** . We apply t-SNE [7] and PCA [8] analyses on both the original and synthetic datasets (flattening the temporal dimension). This visualizes how closely the distribution of generated samples resembles that of the original in 2-dimensional space, giving a qualitative assessment of (1). 

**(2) Discriminative Score** . For a quantitative measure of similarity, we train a post-hoc time-series classification model (by optimizing a 2-layer LSTM) to distinguish between sequences from the original and generated datasets. First, each original sequence is labeled _real_ , and each generated sequence is labeled _not real_ . Then, an off-the-shelf (RNN) classifier is trained to distinguish between the two classes as a standard supervised task. We then report the classification error on the held-out test set, which gives a quantitative assessment of (2). 

**(3) Predictive Score** . In order to be useful, the sampled data should inherit the predictive characteristics of the original. In particular, we expect TimeGAN to excel in capturing conditional distributions over time. Therefore, using the synthetic dataset, we train a post-hoc sequence-prediction model (by optimizing a 2-layer LSTM) to predict next-step temporal vectors over each input sequence. Then, we evaluate the trained model on the original dataset. Performance is measured in terms of the mean absolute error (MAE); for event-based data, the MAE is computed as _|_ 1 _−_ estimated probability that the event occurred _|_ . This gives a quantitative assessment of (3). 

The Supplementary Materials contains additional information on benchmarks and hyperparameters, as well as further details of visualizations and hyperparameters for the post-hoc evaluation models. 

6 

### **5.1 Illustrative Example: Autoregressive Gaussian Models** 

Our primary novelties are twofold: a supervised loss to better capture temporal dynamics, and an embedding network that provides a lower-dimensional adversarial learning space. To highlight these advantages, we experiment on sequences from autoregressive multivariate Gaussian models as follows: **x** _t_ = _φ_ **x** _t−_ 1 + **n** _,_ where **n** _∼N_ ( **0** _, σ_ **1** + (1 _− σ_ ) **I** ). The coefficient _φ ∈_ [0 _,_ 1] allows us to control the correlation across time steps, and _σ ∈_ [ _−_ 1 _,_ 1] controls the correlation across features. 

As shown in Table 1, TimeGAN consistently generates higher-quality synthetic data than benchmarks, in terms of both discriminative and predictive scores. This is true across the various settings for the underlying data-generating model. Importantly, observe that the advantage of TimeGAN is greater for higher settings of temporal correlation _φ_ , lending credence to the motivation and benefit of the supervised loss mechanism. Likewise, observe that the advantage of TimeGAN is also greater for higher settings of feature correlation _σ_ , providing confirmation for the benefit of the embedding network. 

Table 1: Results on Autoregressive Multivariate Gaussian Data (Bold indicates best performance). 

||Temporal C i<br>|orrelations (fi<br>|ixing_σ_ = 0_._8)<br>|Feature Cor i<br>|relations (fixi<br>|ing_φ_= 0_._8)<br>|
|---|---|---|---|---|---|---|
|Settings|_φ_= 0_._2|_φ_= 0_._5|_φ_= 0_._8|_σ_ = 0_._2|_σ_ = 0_._5|_σ_ = 0_._8|
|||Discriminativ<br>|e Score (Lower<br>|the better)<br>|||
|TimeGAN|**.175**_±_**.006**|**.174**_±_**.012**|**.105**_±_**.005**|**.181**_±_**.006**|**.152**_±_**.011**|**.105**_±_**.005**|
|RCGAN|.177_±_.012|.190_±_.011|.133_±_.019|.186_±_.012|.190_±_.012|.133_±_.019|
|C-RNN-GAN|.391_±_.006|.227_±_.017|.220_±_.016|.198_±_.011|.202_±_.010|.220_±_.016|
|T-Forcing|.500_±_.000|.500_±_.000|.499_±_.001|.499_±_.001|.499_±_.001|.499_±_.001|
|P-Forcing|.498_±_.002|.472_±_.008|.396_±_.018|.460_±_.003|.408_±_.016|.396_±_.018|
|WaveNet|.337_±_.005|.235_±_.009|.229_±_.013|.217_±_.010|.226_±_.011|.229_±_.013|
|WaveGAN|.336_±_.011|.213_±_.013|.230_±_.023|.192_±_.012|.205_±_.015|.230_±_.023|
|||Predictive S<br>|core (Lower th<br>|e better)<br>|||
|TimeGAN|**.640**_±_**.003**|**.412**_±_**.002**|**.251**_±_**.002**|**.282**_±_**.005**|**.261**_±_**0.002**|**.251**_±_**.002**|
|RCGAN|.652_±_.003|.435_±_.002|.263_±_.003|.292_±_.003|.279_±_.002|.263_±_.003|
|C-RNN-GAN|.696_±_.002|.490_±_.005|.299_±_.002|.293_±_.005|.280_±_.006|.299_±_.002|
|T-Forcing|.737_±_.022|.732_±_.012|.503_±_.037|.515_±_.034|.543_±_.023|.503_±_.037|
|P-Forcing|.665_±_.004|.571_±_.005|.289_±_.003|.406_±_.005|.317_±_.001|.289_±_.003|
|WaveNet|.718_±_.002|.508_±_.003|.321_±_.005|.331_±_.004|.297_±_.003|.321_±_.005|
|WaveGAN|.712_±_.003|.489_±_.001|.290_±_.002|.325_±_.003|.353_±_.001|.290_±_.002|



### **5.2 Experiments on Different Types of Time Series Data** 

We test the performance of TimeGAN across time-series data with a variety of different characteristics, including periodicity, discreteness, level of noise, regularity of time steps, and correlation across time and features. The following datasets are selected on the basis of different combinations of these properties (detailed statistics of each dataset can be found in the Supplementary Materials). 

**(1) Sines** . We simulate multivariate sinusoidal sequences of different frequencies _η_ and phases _θ_ , providing continuous-valued, periodic, multivariate data where each feature is independent of others. For each dimension _i ∈{_ 1 _, ...,_ 5 _}_ , _xi_ ( _t_ ) = sin(2 _πηt_ + _θ_ ), where _η ∼U_ [0 _,_ 1] and _θ ∼U_ [ _−π, π_ ]. 

**(2) Stocks** . By contrast, sequences of stock prices are continuous-valued but aperiodic; furthermore, features are correlated with each other. We use the daily historical Google stocks data from 2004 to 2019, including as features the volume and high, low, opening, closing, and adjusted closing prices. 

**(3) Energy** . Next, we consider a dataset characterized by noisy periodicity, higher dimensionality, and correlated features. The UCI Appliances energy prediction dataset consists of multivariate, continuous-valued measurements including numerous temporal features measured at close intervals. 

**(4) Events** . Finally, we consider a dataset characterized by discrete values and irregular time stamps. We use a large private lung cancer pathways dataset consisting of sequences of events and their times, and model both the one-hot encoded sequence of event types as well as the event timings. 

7 































<!-- Start of picture text -->
(a) TimeGAN (b) RCGAN (c) CRNNGAN (d) T-Forcing (e) P-Forcing (f) WaveNet (g) WaveGAN<br><!-- End of picture text -->

Figure 3: t-SNE visualization on Sines (1<sup>st</sup> row) and Stocks (2<sup>nd</sup> row). Each column provides the visualization for each of the 7 benchmarks. Red denotes original data, and blue denotes synthetic. Additional and larger t-SNE and PCA visualizations can be found in the Supplementary Materials. 

**Visualizations with t-SNE and PCA** . In Figure 3, we observe that synthetic datasets generated by TimeGAN show markedly better overlap with the original data than other benchmarks using t-SNE for visualization (PCA analysis can be found in the Supplementary Materials). In fact, we (in the first column) that the blue (generated) samples and red (original) samples are almost perfectly in sync. 

**Discriminative and Predictive Scores** . As indicated in Table 2, TimeGAN consistently generates higher-quality synthetic data in comparison to benchmarks on the basis of both discriminative (posthoc classification error) and predictive (mean absolute error) scores across all datasets. For instance for Stocks, TimeGAN-generated samples achieve 0.102 which is 48% lower than the next-best benchmark (RCGAN, at 0.196)—a statistically significant improvement. Remarkably, observe that the predictive scores of TimeGAN are almost on par with those of the original datasets themselves. 

Table 2: Results on Multiple Time-Series Datasets (Bold indicates best performance). 

|Metric|Method|Sines|Stocks|Energy|Events|
|---|---|---|---|---|---|
||TimeGAN|**.011**_±_**.008**|**.102**_±_**.021**|**.236**_±_**.012**|**.161**_±_**.018**|
||RCGAN|.022_±_.008|.196_±_.027|.336_±_.017|.380_±_.021|
|Discriminative|C-RNN-GAN|.229_±_.040|.399_±_.028|.499_±_.001|.462_±_.011|
|Score|T-Forcing|.495_±_.001|.226_±_.035|.483_±_.004|.387_±_.012|
||P-Forcing|.430_±_.027|.257_±_.026|.412_±_.006|.489_±_.001|
|(Lower the Better)|WaveNet|.158_±_.011|.232_±_.028|.397_±_.010|.385_±_.025|
||WaveGAN|.277_±_.013|.217_±_.022|.363_±_.012|.357_±_.017|
||TimeGAN|**.093**_±_**.019**|**.038**_±_**.001**|**.273**_±_**.004**|**.303**_±_**.006**|
||RCGAN|.097_±_.001|.040_±_.001|.292_±_.005|.345_±_.010|
|Predictive|C-RNN-GAN|.127_±_.004|**.038**_±_**.000**|.483_±_.005|.360_±_.010|
|Score|T-Forcing|.150_±_.022|**.038**_±_**.001**|.315_±_.005|.310_±_.003|
||P-Forcing|.116_±_.004|.043_±_.001|.303_±_.006|.320_±_.008|
|(Lower the Better)|WaveNet|.117_±_.008|.042_±_.001|.311_±_.005|.333_±_.004|
||WaveGAN|.134_±_.013|.041_±_.001|.307_±_.007|.324_±_.006|
||Original|.094_±_.001|.036_±_.001|.250_±_.003|.293_±_.000|



### **5.3 Sources of Gain** 

TimeGAN is characterized by (1) the supervised loss, (2) embedding networks, and (3) the joint training scheme. To analyze the importance of each contribution, we report the discriminative and predictive scores with the following modifications to TimeGAN: (1) without the supervised loss, (2) without the embedding networks, and (3) without jointly training the embedding and adversarial networks on the supervised loss. (The first corresponds to _λ_ = _η_ = 0, and the third to _λ_ = 0). 

We observe in Table 3 that all three elements make important contributions in improving the quality of the generated time-series data. The supervised loss plays a particularly important role when the data is characterized by high temporal correlations, such as in the Stocks dataset. In addition, we find that the embedding networks and joint training the with the adversarial networks (thereby aligning the targets of the two) clearly and consistently improves generative performance across the board. 

8 

Table 3: Source-of-Gain Analysis on Multiple Datasets (via Discriminative and Predictive scores). 

|Metric|Method|Sines|Stocks|Energy|Events|
|---|---|---|---|---|---|
||TimeGAN|**.011**_±_**.008**|**.102**_±_**.021**|**.236**_±_**.012**|**.161**_±_**.018**|
|Discriminative|w/o Supervised Loss|.193_±_.013|.145_±_.023|.298_±_.010|.195_±_.013|
|Score|w/o Embedding Net.|.197_±_.025|.260_±_.021|.286_±_.006|.244_±_.011|
|(Lower the Better)|w/o Joint Training|.048_±_.011|.131_±_.019|.268_±_.012|.181_±_.011|
||TimeGAN|**.093**_±_**.019**|**.038**_±_**.001**|**.273**_±_**.004**|**.303**_±_**.006**|
|Predictive|w/o Supervised Loss|.116_±_.010|.054_±_.001|.277_±_.005|.380_±_.023|
|Score|w/o Embedding Net.|.124_±_.002|.048_±_.001|.286_±_.002|.410_±_.013|
|(Lower the Better)|w/o Joint Training|.107_±_.008|.045_±_.001|.276_±_.004|.348_±_.021|



## **6 Conclusion** 

In this paper we introduce TimeGAN, a novel framework for time-series generation that combines the versatility of the unsupervised GAN approach with the control over conditional temporal dynamics afforded by supervised autoregressive models. Leveraging the contributions of the supervised loss and jointly trained embedding network, TimeGAN demonstrates consistent and significant improvements over state-of-the-art benchmarks in generating realistic time-series data. In the future, further work may investigate incorporating the differential privacy framework into the TimeGAN approach in order to generate high-quality time-series data with differential privacy guarantees. 

## **Acknowledgements** 

The authors would like to thank the reviewers for their helpful comments. This work was supported by the National Science Foundation (NSF grants 1407712, 1462245 and 1533983), and the US Office of Naval Research (ONR). 

## **References** 

- [1] Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. Scheduled sampling for sequence prediction with recurrent neural networks. In _Advances in Neural Information Processing Systems_ , pages 1171–1179, 2015. 

- [2] Alex M Lamb, Anirudh Goyal Alias Parth Goyal, Ying Zhang, Saizheng Zhang, Aaron C Courville, and Yoshua Bengio. Professor forcing: A new algorithm for training recurrent networks. In _Advances In Neural Information Processing Systems_ , pages 4601–4609, 2016. 

- [3] Dzmitry Bahdanau, Philemon Brakel, Kelvin Xu, Anirudh Goyal, Ryan Lowe, Joelle Pineau, Aaron Courville, and Yoshua Bengio. An actor-critic algorithm for sequence prediction. _arXiv preprint arXiv:1607.07086_ , 2016. 

- [4] Olof Mogren. C-rnn-gan: Continuous recurrent neural networks with adversarial training. _arXiv preprint arXiv:1611.09904_ , 2016. 

- [5] Cristóbal Esteban, Stephanie L Hyland, and Gunnar Rätsch. Real-valued (medical) time series generation with recurrent conditional gans. _arXiv preprint arXiv:1706.02633_ , 2017. 

- [6] Giorgia Ramponi, Pavlos Protopapas, Marco Brambilla, and Ryan Janssen. T-cgan: Conditional generative adversarial network for data augmentation in noisy time series with irregular sampling. _arXiv preprint arXiv:1811.08295_ , 2018. 

- [7] Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. _Journal of machine learning research_ , 9(Nov):2579–2605, 2008. 

- [8] Fred B Bryant and Paul R Yarnold. Principal-components analysis and exploratory and confirmatory factor analysis. 1995. 

- [9] Jinsung Yoon, James Jordon, and Mihaela van der Schaar. PATE-GAN: Generating synthetic data with differential privacy guarantees. In _International Conference on Learning Representations_ , 2019. 

9 

- [10] Ronald J Williams and David Zipser. A learning algorithm for continually running fully recurrent neural networks. _Neural computation_ , 1(2):270–280, 1989. 

- [11] Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston. Curriculum learning. In _Proceedings of the 26th annual international conference on machine learning_ , pages 41–48. ACM, 2009. 

- [12] Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario Marchand, and Victor Lempitsky. Domain-adversarial training of neural networks. _The Journal of Machine Learning Research_ , 17(1):2096–2030, 2016. 

- [13] Vijay R Konda and John N Tsitsiklis. Actor-critic algorithms. In _Advances in neural information processing systems_ , pages 1008–1014, 2000. 

- [14] Mehdi Mirza and Simon Osindero. Conditional generative adversarial nets. _arXiv preprint arXiv:1411.1784_ , 2014. 

- [15] Yizhe Zhang, Zhe Gan, and Lawrence Carin. Generating text via adversarial training. In _NIPS workshop on Adversarial Training_ , volume 21, 2016. 

- [16] Luca Simonetto. Generating spiking time series with generative adversarial networks: an application on banking transactions. 2018. 

- [17] Shota Haradal, Hideaki Hayashi, and Seiichi Uchida. Biosignal data augmentation based on generative adversarial networks. In _2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)_ , pages 368–371. IEEE, 2018. 

- [18] Moustafa Alzantot, Supriyo Chakraborty, and Mani Srivastava. Sensegen: A deep learning architecture for synthetic sensor data generation. In _2017 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops)_ , pages 188–193. IEEE, 2017. 

- [19] Chi Zhang, Sanmukh R Kuppannagari, Rajgopal Kannan, and Viktor K Prasanna. Generative adversarial network for synthetic time series data generation in smart grids. In _2018 IEEE International Conference on Communications, Control, and Computing Technologies for Smart Grids (SmartGridComm)_ , pages 1–6. IEEE, 2018. 

- [20] Yize Chen, Yishen Wang, Daniel Kirschen, and Baosen Zhang. Model-free renewable scenario generation using generative adversarial networks. _IEEE Transactions on Power Systems_ , 33(3):3265–3275, 2018. 

- [21] Andrew M Dai and Quoc V Le. Semi-supervised sequence learning. In _Advances in neural information processing systems_ , pages 3079–3087, 2015. 

- [22] Xinrui Lyu, Matthias Hueser, Stephanie L Hyland, George Zerveas, and Gunnar Raetsch. Improving clinical predictions through unsupervised time series representation learning. _arXiv preprint arXiv:1812.00490_ , 2018. 

- [23] Nitish Srivastava, Elman Mansimov, and Ruslan Salakhudinov. Unsupervised learning of video representations using lstms. In _International conference on machine learning_ , pages 843–852, 2015. 

- [24] Otto Fabius and Joost R van Amersfoort. Variational recurrent auto-encoders. _arXiv preprint arXiv:1412.6581_ , 2014. 

- [25] Yingzhen Li and Stephan Mandt. Disentangled sequential autoencoder. _arXiv preprint arXiv:1803.02991_ , 2018. 

- [26] Wei-Ning Hsu, Yu Zhang, and James Glass. Unsupervised learning of disentangled and interpretable representations from sequential data. In _Advances in neural information processing systems_ , pages 1878–1889, 2017. 

- [27] Anders Boesen Lindbo Larsen, Søren Kaae Sønderby, Hugo Larochelle, and Ole Winther. Autoencoding beyond pixels using a learned similarity metric. _arXiv preprint arXiv:1512.09300_ , 2015. 

- [28] Vincent Dumoulin, Ishmael Belghazi, Ben Poole, Olivier Mastropietro, Alex Lamb, Martin Arjovsky, and Aaron Courville. Adversarially learned inference. _arXiv preprint arXiv:1606.00704_ , 2016. 

- [29] Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. _arXiv preprint arXiv:1511.05644_ , 2015. 

- [30] Yoon Kim, Kelly Zhang, Alexander M Rush, Yann LeCun, et al. Adversarially regularized autoencoders. _arXiv preprint arXiv:1706.04223_ , 2017. 

10 

- [31] Aäron Van Den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew W Senior, and Koray Kavukcuoglu. Wavenet: A generative model for raw audio. _SSW_ , 125, 2016. 

- [32] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. _arXiv preprint arXiv:1409.0473_ , 2014. 

- [33] Alex Graves. Generating sequences with recurrent neural networks. _arXiv preprint arXiv:1308.0850_ , 2013. 

- [34] Ilya Sutskever, James Martens, and Geoffrey E Hinton. Generating text with recurrent neural networks. In _Proceedings of the 28th International Conference on Machine Learning (ICML-11)_ , pages 1017–1024, 2011. 

- [35] Chris Donahue, Julian McAuley, and Miller Puckette. Adversarial audio synthesis. _arXiv preprint arXiv:1802.04208_ , 2018. 

11 

