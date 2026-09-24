---
title: "Generating Multi-label Discrete Patient Records using GANs (medGAN)"
authors: "networks"
year: 2017
arxiv_id: "1703.06490"
original_file: "1703.06490.pdf"
pdf_path: "docs/papers\2017_networks_generating_multilabel_discrete_pati.pdf"
---

# Generating Multi-label Discrete Patient Records using GANs (medGAN)

**Authors:** Networks et al.  
**Year:** 2017 | **arXiv:** [`1703.06490`](https://arxiv.org/abs/1703.06490)  
**Local PDF:** [`2017_networks_generating_multilabel_discrete_pati.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2017_networks_generating_multilabel_discrete_pati.pdf)

---

JMLR W&C Track Volume 68 

Proceedings of Machine Learning for Healthcare 2017 

## **Generating Multi-label Discrete Patient Records using Generative Adversarial Networks** 

**Edward Choi**<sup>1</sup> MP2893@GATECH.EDU **Siddharth Biswal**<sup>1</sup> SBISWAL7@GATECH.EDU **Bradley Malin**<sup>2</sup> BRADLEY.MALIN@VANDERBILT.EDU **Jon Duke**<sup>1</sup> JON.DUKE@GATECH.EDU **Walter F. Stewart**<sup>3</sup> STEWARWF@SUTTERHEALTH.ORG **Jimeng Sun**<sup>1</sup> JSUN@CC.GATECH.EDU 

1GEORGIA INSTITUTE OF TECHNOLOGY 2 VANDERBILT UNIVERSITY 3 SUTTER HEALTH 

### **Abstract** 

Access to electronic health record (EHR) data has motivated computational advances in medical research. However, various concerns, particularly over privacy, can limit access to and collaborative use of EHR data. Sharing synthetic EHR data could mitigate risk. 

In this paper, we propose a new approach, medical Generative Adversarial Network (medGAN), to generate realistic synthetic patient records. Based on input real patient records, medGAN can generate high-dimensional discrete variables (e.g., binary and count features) via a combination of an autoencoder and generative adversarial networks. We also propose minibatch averaging to efficiently avoid mode collapse, and increase the learning efficiency with batch normalization and shortcut connections. To demonstrate feasibility, we showed that medGAN generates synthetic patient records that achieve comparable performance to real data on many experiments including distribution statistics, predictive modeling tasks and a medical expert review. We also empirically observe a limited privacy risk in both identity and attribute disclosure using medGAN. 

### **1. Introduction** 

The adoption of electronic health records (EHR) by healthcare organizations (HCOs), along with the large quantity and quality of data now generated, has led to an explosion in _computational health_ . However, the wide adoption of EHR systems does not automatically lead to easy access to EHR data for researchers. One reason behind limited access stems from the fact that EHR data are composed of personal identifiers, which in combination with potentially sensitive medical information, induces privacy concerns. As a result, access to such data for secondary purposes (e.g., research) is regulated, as well as controlled by the HCOs groups that are at risk if data are misused or breached. The review process by legal departments and institutional review boards can take months, with no guarantee of access (Hodge Jr et al., 1999). This process limits timely opportunities to use data and may slow advances in biomedical knowledge and patient care (Gostin et al., 2009). 

HCOs often aim to mitigate privacy risks through the practice of de-identification (for Civil Rights, 2013), typically through the perturbation of potentially identifiable attributes (e.g., dates of birth) via generalization, suppression or randomization. (El Emam et al., 2015) However, this approach is not impregnable to attacks, such as linkage via residual information to re-identify the individuals to whom the data corresponds (El Emam et al., 2011b). An alternative approach to de-identification is to generate synthetic data (McLachlan et al., 2016; Buczak et al., 2010; Lombardo and Moniz, 2008). However, realizing this goal in practice has been challenging because the resulting synthetic data are often not sufficiently realistic for machine learning tasks. Since many machine learning models for EHR data use aggregated discrete features derived from longitudinal EHRs, we concentrate our effort on generating such aggregated data in this study. Although it is ultimately 

_⃝_ c 2017. 

desirable to generate longitudinal event sequences, in this work we focus on generating high-dimensional discrete variables, which is an important and challenging problem on its own. 

Generative adversarial networks (GANs) have recently been shown to achieve impressive performance in generating high-quality synthetic images (Goodfellow et al., 2014; Radford et al., 2015; Goodfellow, 2016). To understand how, it should first be recognized that a GAN consists of two components: a _generator_ that attempts to generate realistic, but fake, data and a _discriminator_ that aims to distinguish between the generated fake data and the real data. By playing an adversarial game against each other, the generator can learn the distribution of the real samples - provided that both the generator and the discriminator are sufficiently expressive. Empirically, a GAN outperforms other popular generative models such as variational autoencoders (VAE) (Kingma and Welling, 2013) and PixelRNN/PixelCNN (van den Oord et al., 2016b,a) on the quality of data (i.e., fake compared to real), in this case images, and on processing speed (Goodfellow, 2016). However, GANs have not been used for learning the distribution of discrete variables. 

To address this limitation, we introduce medGAN, a neural network model that generates high-dimensional, multi-label discrete variables that represent the events in EHRs (e.g., diagnosis of a certain disease or treatment of a certain medication). Using EHR source data, medGAN is designed to learn the distribution of discrete features, such as diagnosis or medication codes via a combination of an autoencoder and the adversarial framework. In this setting, the autoencoder assists the original GAN to learn the distribution of multi-label discrete variables. The specific contributions of this work are as follows: 

- We define an efficient algorithm to generate high-dimensional multi-label discrete samples by combining an autoencoder with GAN, which we call medGAN. This algorithm is notable in that it handles both binary and count variables. 

- We propose a simple, yet effective, method called _minibatch averaging_ to cope with the situation where GAN overfits to a few training samples (i.e., mode collapse), which outperforms previous methods such as _minibatch discrimination_ . 

- We demonstrate a close-to-real data performance of medGAN using real EHR datasets on a set of diverse tasks, which include reporting distribution statistics, classification performance and medical expert review. 

- We empirically show that medGAN leads to acceptable privacy risks in both presence disclosure (i.e., discovery that a patient’s record contributed to the GAN) and attribute disclosure (i.e., discovery of a patient’s sensitive medical data). 

### **2. Related work** 

In this section, we begin with a discussion of existing methods for generating synthetic EHR data. This is followed by a review recent advances in generative adversarial networks (GANs). Finally, we summarize specific investigations into generating discrete variables using GANs. 

**Synthetic Data Generation for Health Data:** De-identification of EHR data is currently the most generally accepted technical method for protecting patient privacy when sharing EHR data for research in practice (Johnson et al., 2016). However, de-identification does not guarantee that a system is devoid of risk. In certain circumstances, re-identification of patients can be accomplished through residual distinguishable patterns in various features (e.g., demographics (Sweeney, 1997; El Emam et al., 2011a), diagnoses (Loukides et al., 2010), lab tests (Atreya et al., 2013), visits across healthcare providers (Malin and Sweeney, 2004), and genomic variants (Erlich and Narayanan, 2014)) To mitigate re-identification vulnerabilities, researchers in the statistical disclosure control community have investigated how to generate synthetic datasets. Yet, historically, these approaches have been limited to summary statistics for only several variables at a time (e.g., (Dreschsler, 2011; Reiter, 2002). For instance McLachlan et al.(2016) used clinical practice guidelines and health incidence statistics with a state transition machine to generate synthetic patient datasets. 

There is some, but limited, work on synthetic data generation in the healthcare domain and, the majority that has, tend to be disease specific. For example, Buczak et al. (2010) generated EHRs to explore questions related to the outbreak of specific illnesses, where care patterns in the source EHRs were applied to generate synthetic datasets. Many of these methods often rely heavily upon domain-specific knowledge along with actual data to generate synthetic EHRs (Lombardo and Moniz, 2008). More recently, and most related to our 

2 

work, a privacy-preserving patient data generator was proposed based on a perturbed Gibbs sampler (Park et al., 2013). Still, this approach can only handle binary variables and its utility was assessed with only a small, low-dimensional dataset. By contrast, our proposed medGAN directly captures general EHR data without focusing on a specific disease, which makes it suitable for a greater diversity of applications. 

**GAN and its Applications:** Attempts to advance GANs (Goodfellow et al., 2014) include, but are not limited to, using convolutional neural networks to improve image processing capacity (Radford et al., 2015), extending GAN to a conditional architecture for higher quality image generation (Mirza and Osindero, 2014; Denton et al., 2015; Odena et al., 2016), and text-to-image generation (Reed et al., 2016). We, in particular, pay attention to the recent studies that attempted to handle discrete variables using GANs. 

One way to generate discrete variables with GAN is to invoke reinforcement learning. SeqGAN (Yu et al., 2016) trains GAN with REINFORCE (Williams, 1992) and Monte-Carlo search to generate word sequences. Although REINFORCE enables an unbiased estimation of the gradients of the model via sampling, the estimates come with a high variance. Moreover, SeqGAN focuses on sampling one word ( _i.e._ one-hot) at each timestep, whereas our goal is to generate multi-label binary/count variables. Alternatively, one could use specialized distributions, such as the Gumbel-softmax (Jang et al., 2016; Kusner and Hernandez-Lobato, 2016),´ a concrete distribution (Maddison et al., 2016) or a soft-argmax function (Zhang et al., 2016) to approximate the gradient of the model from discrete samples. However, since these approaches focus on the softmax distribution, they cannot be directly invoked for multi-label discrete variables, especially in the count variable case. Yet another way to handle discrete variables is to generate distributed representations, then decode them into discrete outputs. For example, Glover (2016) generated document embeddings with a GAN, but did not attempt to simulate actual documents. 

To handle high-dimensional multi-label discrete variables, medGAN generates the distributed representations of patient records with a GAN. It then decodes them to simulated patient records with an autoencoder. 

### **3. Method** 

This section begins with a formalization of the structure of EHR data and the corresponding mathematical notation we adopt in this work, This is followed by a detailed description of the medGAN algorithm. 

#### **3.1 Description of EHR Data and Notations** 

We assume there are _|C|_ discrete variables ( _e.g._ , diagnosis, medication or procedure codes) in the EHR data that can be expressed as a fixed-size vector **x** _∈_ Z<sup>_|C|_</sup> +<sup>, where the value of the</sup><sup>_ith_dimension indicates the number of</sup> occurrences ( _i.e._ , counts) of the _i_ -th variable in the patient record. In addition to the count variables, a visit can also be represented as a binary vector **x** _∈{_ 0 _,_ 1 _}_<sup>_|C|_</sup> , where the _i_<sup>_th_</sup> dimension indicates the absence or occurrence of the _i_<sup>_th_</sup> variable in the patient record. It should be noted that we can also represent demographic information, such as age and gender, as count and binary variables, respectively. 

Learning the distribution of count variables is generally more difficult than learning the distribution of binary variables. This is because the model needs to learn more than simple co-occurrence relations between the various dimensions. Moreover, in EHR data, certain clinical concepts tend to occur much more frequently (e.g., essential hypertension) than others. This is problematic because it can skew a distribution around different dimensions. 

#### **3.2 Preliminary: Generative Adversarial Network** 

In a GAN, the generator _G_ ( **z** ; _θg_ ) accepts a random prior **z** _∈_ R<sup>_r_</sup> and generates synthetic samples _G_ ( **z** ) _∈_ R<sup>_d_</sup> , while the discriminator _D_ ( **x** ; _θd_ ) determines whether a given sample is real or fake. The optimal discriminator _D_<sup>_∗_</sup> would perfectly distinguish real samples from fake samples. The optimal generator _G_<sup>_∗_</sup> would generate fake samples that are indistinguishable from the real samples so that _D_ is forced to make random guesses. Formally, _D_ and _G_ play the following minimax game with the value function _V_ ( _G, D_ ): 



3 

Figure 1: Architecture of medGAN: The discrete **x** comes from the source EHR data, **z** is the random prior for the generator _G_ ; _G_ is a feedforward network with shortcut connections (right-hand side figure); An autoencoder (i.e, the encoder _Enc_ and decoder _Dec_ ) is learned from **x** ; The same decoder _Dec_ is used after the generator _G_ to construct the discrete output. The discriminator _D_ tries to differentiate real input **x** and discrete synthetic output _Dec_ ( _G_ ( **z** )). 



<!-- Start of picture text -->
Real or Fake?<br>D<br>Dec(G( z ))<br>Dec(Enc( x )) G( z )<br>Enc( x ) z<br>x<br><!-- End of picture text -->

where _pdata_ is the distribution of the real samples and _p_ **z** is the distribution of the random prior, for which _N_ (0 _,_ 1) is generally used. Both _G_ and _D_ iterate in optimizing the respective parameters _θg_ and _θd_ as follows, 



where _m_ is the size of the minibatch and _α_ the step size. In practice, however, _G_ can be trained to maximize log( _D_ ( _G_ ( **z** )) instead of minimizing log(1 _− D_ ( _G_ ( **z** )) to provide stronger gradients in the early stage of the training (Goodfellow et al., 2014) as follows, 



Henceforth, we use Eq.(1) as it showed significantly more stable performance in our investigation. We also assume throughout the paper that both _D_ and _G_ are implemented with feedforward neural networks. 

#### **3.3 medGAN** 

Since the generator _G_ is trained by the error signal from the discriminator _D_ via backpropagation, the original GAN can only learn to approximate discrete patient records **x** _∈_ Z<sup>_|C|_</sup> +<sup>with continuous values.We alleviate</sup> this limitation by leveraging the autoencoder. Autoencoders are trained to project given samples to a lower dimensional space, then project them back to the original space. Such a mechanism leads the autoencoder to learn salient features of the samples and has been successfully used in certain applications, such as image processing (Goodfellow et al., 2016; Vincent et al., 2008). 

In this work, We apply the autoencoder to learn the salient features of discrete variables that can be applied to decode the continuous output of _G_ . This allows the gradient flow from _D_ to the decoder _Dec_ to enable the end-to-end fine-tuning. As depicted by Figure 1, an autoencoder consists of an encoder _Enc_ ( **x** ; _θenc_ ) that compresses the input **x** _∈_ Z<sup>_|C|_</sup> +<sup>to</sup><sup>_Enc_(</sup><sup>**x**)</sup><sup>_∈_R</sup><sup>_h_, and a decoder</sup><sup>_Dec_(</sup><sup>_Enc_(</sup><sup>**x**);</sup><sup>_θdec_) that decompresses</sup> _Enc_ ( **x** ) to _Dec_ ( _Enc_ ( **x** )) as the reconstruction of the original input **x** . The objective of the autoencoder is to minimize the reconstruction error: 





where _m_ is the size of the mini-batch. We use the mean squared loss (Eq.(2)) for count variables and cross entropy loss (Eq.(3)) for binary variables. For count variables, we use rectified linear units (ReLU) as the 

4 

activation function in both _Enc_ and _Dec_ . For binary variables, we use tanh activation for _Enc_ and the sigmoid activation for _Dec_ .<sup>1</sup> 

With the pre-trained autoencoder, we can allow GAN to generate distributed representation of patient records (i.e., the output of the encoder _Enc_ ), rather than generating patient records directly. Then the pretrained decoder _Dec_ can pick up the right signals from _G_ ( **z** ) to convert it to the patient record _Dec_ ( _G_ ( **z** )). The discriminator _D_ is trained to determine whether the given input is a synthetic sample _Dec_ ( _G_ ( **z** )) or a real sample **x** . The architecture of the proposed model medGAN is depicted in Figure 1. medGAN is trained in a similar fashion as the original GAN as follows, 



It should be note that we can round the values of _Dec_ ( _G_ ( **z** )) to their nearest integers to ensure that the discriminator _D_ is trained on discrete values instead of continuous values. We experimented both with and without rounding and empirically found that training _D_ in the latter scenario led to better predictive performance in section 4.2. Therefore, we assume, for the remainder of this paper, that _D_ is trained without explicit rounding. 

We fine-tune the pre-trained parameters of the decoder _θdec_ while optimizing for _G_ . Therefore, the generator _G_ can be viewed as a neural network with an extra hidden layer pre-trained to map continuous samples to discrete samples. We used ReLU for all of _G_ ’s activation functions, except for the output layer, where we used the tanh function<sup>2</sup> . For _D_ , we used ReLU for all activation functions except for the output layer, where we used the sigmoid function for binary classification. 

#### **3.4 Minibatch Averaging** 

Since the objective of the generator _G_ is to produce samples that can fool the discriminator _D_ , _G_ could learn to map different random priors **z** to the same synthetic output, rather than producing diverse synthetic outputs. This problem is denoted as _mode collapse_ , which arises most likely due to the GAN’s optimization strategy often solving the max-min problem instead of the min-max problem (Goodfellow, 2016). Some methods have been proposed to cope with mode collapse (e.g., minibatch discrimination and unrolled GANs), but they require _ad hoc_ fine-tuning of the hyperparameters and scalability is often neglected (Salimans et al., 2016; Metz et al., 2016). 

By contrast, medGAN offers a simple and efficient method to cope with mode collapse when generating discrete outputs. Our method, _minibatch averaging_ , is motivated by the philosophy behind minibatch discrimination. It allows the discriminator _D_ to view the minibatch of real samples **x** 1 _,_ **x** 2 _, . . ._ and the minibatch of the fake samples _G_ ( **z** 1) _, G_ ( **z** 2) _, . . ._ , respectively, while classifying a real sample and a fake sample. Given a sample to discriminate, minibatch discrimination calculates the distance between the given sample and every sample in the minibatch in the latent space. Minibatch averaging, by contrast, provides the average of the minibatch samples to _D_ , modifying the objective as follows: 



where _m_ denotes the size of the minibatch. Specifically, the average of the minibatch is concatenated on the sample and provided to the discriminator _D_ . 

> 1. We considered a denoising autoencoder (dAE) (Vincent et al., 2008) as well, but there was no discernible improvement in performance. 

> 2. We also applied tanh activation for the encoder _Enc_ for consistency. 

5 

**Binary variables:** When processing binary variables **x** _∈{_ 0 _,_ 1 _}_<sup>_|C|_</sup> , the average of minibatch samples **x** ¯ and **x** ¯ **z** are equivalent to the maximum likelihood estimate of the Bernoulli success probability _p_ ˆ _k_ of each dimension _k_ . This information makes it easier for _D_ to ascertain whether a given sample is real or fake, if _p_ ˆ _k_ ’s of fake samples are considerably different from those of real samples. This is especially likely when mode collapse occurs because the _p_ ˆ _k_ ’s for most dimensions of the fake samples become dichotomized (either 0 or 1), whereas the _p_ ˆ _k_ ’s of real samples generally take on a value between 0 and 1. Therefore, if _G_ wants to fool _D_ , it will have to generate more diverse examples within the minibatch _Dec_ ( _G_ ( **z** 1 _,_ **z** 2 _, . . ._ )). 

**Count variables:** Count variables are a more accurate description of clinical events. They can indicate the number of times a certain diagnosis was made or a certain medication was prescribed over multiple hospital visits. For count variables **x** _∈_ Z<sup>_|C|_</sup> +<sup>, the average of minibatch samples</sup><sup>**x**¯ and</sup><sup>**x**¯</sup><sup>**z**can be viewed as the estimate</sup> of the binomial distribution mean _n_ � _pk_ of each dimension _k_ , where _n_ is the number of hospital visits. Hence minibatch averaging for the count variables also provides helpful statistics to the discriminator _D_ , guiding the generator _G_ to generate more diverse and realistic samples. As our experiments show, minibatch averaging works surprisingly well and does not require additional parameters like minibatch discrimination. As a consequence, it has minimal impact to the training time. It is further worth mentioning that, for both binary and count variables, a minibatch that is larger than usual is recommended to properly capture the statistics of the real data. We use 1,000 records for a minibatch in this investigation. 

#### **3.5 Enhanced Generator Training** 

Similar to image processing GANs, we observed that balancing the power of _D_ and _G_ in the multi-label discrete variable setting was quite challenging (Goodfellow, 2016). Empirically, we observed that training medGAN with minibatch averaging demonstrated _D_ consistently overpowering _G_ after several iterations. While _G_ still managed to learn under such situation, the performance seemed suboptimal, and updating _θg_ and _θdec_ more often than _θd_ in each iteration only degraded performance. Considering the importance of an optimal _D_ (Goodfellow, 2016), we chose not to limit the discriminative power of _D_ , but rather improve the learning efficiency of _G_ by applying batch normalization (Ioffe and Szegedy, 2015) and shortcut connection (He et al., 2016). _G_ ’s _k_<sup>_th_</sup> layer is now formulated as follows: 

#### **x** _k_ = ReLU(BN _k_ ( **W** _k_ **x** _k−_ 1)) + **x** _k−_ 1 

where ReLU is the rectified linear unit, BN _k_ is the batch normalization at the _k_ -th layer, **W** _k_ is the weight matrix of the _k_ -th layer, and **x** _k−_ 1 is the input from the previous layer. The right-hand side of Figure 1 depicts the first two layers of _G_ . Note that we do not incorporate the bias variable into each layer because batch normalization negates the necessity of the bias term. Additionally, batch normalization and shortcut connections could be applied to the discriminator _D_ , but the experiments showed that _D_ was consistently overpowering _G_ without such techniques, and we empirically found that a simple feedforward network was sufficient for _D_ . We describe the overall optimization algorithm in the Appendix A. 

#### **3.6 Privacy Consideration** 

When EHRs are de-identfied via methods such generalization or randomization, there often remains a 1-to-1 mapping to the underlying records from where they were derived. However, in our case, the mapping between the generated data from medGAN and the training data of specific patients is not explicit. Intuitively, this seems to imply that the privacy of the patients can be better preserved with medGAN; however, it also begs the question of how to evaluate the privacy in the system. We perform a formal assessment of medGAN’s privacy risks based on two definitions of privacy. 

**Presence disclosure** occurs when an attacker can determine that medGAN was trained with a dataset including the record from patient _x_ . (Nergiz and Clifton, 2010) Presence disclosure for medGAN happens when a powerful attacker, one who already possesses the complete records of a set of patients _P_ , can determine whether anyone from _P_ are in the training set by observing the generated patient records. More recently, for machine learned models, this has been referred to as an _membership inference attack_ (Shokri et al., 2017). the knowledge gained by the attacker may be limited, if the dataset is well balanced in its clinical concepts. **Attribute disclosure** occurs when attackers can derive additional attributes such as diagnoses and medications about patient _x_ based on a subset of attributes they already know about _x_ . (Matwin et al., 2015) We believe 

6 

Table 1: Basic statistics of datasets A, B and C 

|**Dataset**|**(A) Sutter PAMF**|**(B) MIMIC-III**|**(C) Sutter Heart Failure**|
|---|---|---|---|
|# of patients|258,559|46,520|30,738|
|# of unique codes|615|1071|569|
|Avg. # of codes per patient|38.37|11.27|53.02|
|Max # of codes for a patient|198|90|871|
|Min # of codes for a patient|1|1|2|



that attribute disclosure for medGAN could be a more prominent issue because the attacker only needs to know a subset of attributes of a patient. Moreover, the goal of the attacker is to gain knowledge of the unknown attributes by observing similar patients generated by medGAN. 

Considering the difficulty of deriving analytic proof of privacy for GANs and simulated data, we report the empirical analysis of both risks to understand the extent to which privacy can be achieved, as commonly practiced in the statistical disclosure control community. (Domingo-Ferrer and Torra, 2003) 

### **4. Experiments** 

We evaluated medGAN with three distinct EHR datasets. First, we describe the datasets and baseline models. Next, we report the quantitative evaluation results using both binary and count variables. We then perform a qualitative analysis through medical expert review. Finally, we address the privacy aspect of medGAN. The source code of medGAN is publicly available at https://github.com/mp2893/medgan. 

#### **4.1 Experimental Setup** 

**Source data:** The datasets in this study were from A) Sutter Palo Alto Medical Foundation (PAMF), which consists of 10-years of longitudinal medical records of 258K patients, B) the MIMIC-III dataset (Johnson et al., 2016; Goldberger et al., 2000), which is a publicly available dataset consisting of the medical records of 46K intensive care unit (ICU) patients over 11 years old and C) a heart failure study dataset from Sutter, which consists of 18-months observation period of 30K patients. From dataset A and C, we extracted diagnoses, medications and procedure codes, which were then respectively grouped by Clinical Classifications Software (CCS) for ICD-9<sup>3</sup> , Generic Product Identifier Drug Group<sup>4</sup> and for CPT<sup>5</sup> . From dataset B, we extracted ICD9 codes only and grouped them by generalizing up to their first 3 digits. Finally, we aggregate a patient’s longitudinal record into a single fixed-size vector **x** _∈_ Z<sup>_|C|_</sup> +<sup>, where</sup><sup>_|C|_equals 615, 1071 and 569 for dataset A,</sup> B and C respectively. Note that datasets A and B are binarized for experiments regarding binary variables while dataset C is used for experiments regarding count variables. A summary of the datasets are in Table 1. **Models for comparison:** To assess the effectiveness of our methods, we tested multiple versions of medGAN: 

- **GAN:** We use the same architecture as medGAN with the standard training strategy, but do not pre-train the autoencoder. 

- **GAN** _P_ **:** We pre-train the autoencoder (in addition to the GAN). 

- **GAN** _P D_ **:** We pre-train the autoencoder and use minibatch discrimination (Salimans et al., 2016). 

- **GAN** _P A_ **:** We pre-train the autoencoder and use minibatch averaging. 

- **medGAN:** We pre-train the autoencoder and use minibatch averaging. We also use batch normalization and a shortcut connection for the generator _G_ . 

We also compare the performance of medGAN with several popular generative methods as below. 

- **Random Noise (RN):** Given a real patient record **x** , we invert the binary value of each code (i.e., dimension) with probability 0.1. This is not strictly a generative method, but rather it is a simple implementation of a privacy protection method based on randomization. 

- **Independent Sampling (IS):** For the binary variable case, we calculate the Bernoulli success probability of each code in the real dataset, based on which we sample binary values to generate the synthetic dataset. For the count variable case, we use the kernel density estimator (KDE) for each code then sample from that distribution. 

> 3. https://www.hcup-us.ahrq.gov/toolssoftware/ccs/ccs.jsp 

> 4. http://www.wolterskluwercdi.com/drug-data/medi-span-electronic-drug-file/ 

> 5. https://www.hcup-us.ahrq.gov/toolssoftware/ccs ~~s~~ vcsproc/ ccssvcproc.jsp 

7 



<!-- Start of picture text -->
GAN GANP GANPD GANPA medGAN<br>(a) Dimension-wise probability performance of various versions of medGAN.<br>RN IS DBM VAE medGAN<br>(b) Dimension-wise probability performance of baseline models and medGAN.<br><!-- End of picture text -->

Figure 2: Scatterplots of dimension-wise probability results. Each dot represents one of 615 codes. The x-axis represents the Bernoulli success probability for the real dataset A, and y-axis the probability for the synthetic counterpart generated by each model. The diagonal line indicates the ideal performance where the real and synthetic data show identical quality. 

- **Stacked RBM (DBM):** We train a stacked Restricted Boltzmann Machines (Hinton and Salakhutdinov, 2006), then, using Gibbs sampling, we can generate synthetic binary samples. There are studies that extend RBMs beyond binary variables (Hinton and Salakhutdinov, 2009; Gehler et al., 2006; Tran et al., 2011). In this work, however, as our goal is to study medGAN’s performance in various aspects, we use the original RBM only. 

- **Variational Autoencoder (VAE):** We train a variational autoencoder (Kingma and Welling, 2013) where the encoder and the decoder are constructed with feed-forward neural networks. 

**Implementation details:** We implemented medGAN with TensorFlow 0.12 (Team, 2015). For training models, we used Adam (Kingma and Ba, 2014) with the learning rate set to 0.001, and a mini-batch of 1,000 patients on a machine equipped with Intel Xeon E5-2630, 256GB RAM, four Nvidia Pascal Titan X’s and CUDA 8.0. The hyperparameter details are provided in Appendix B. 

#### **4.2 Quantitative Evaluation for Binary Variables** 

We evaluate the model performance for binary variables in this section, and provide the evaluation results of count variables in Appendix D. For all evaluations, we divide the dataset into a training set _R ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> and a test set _T ∈{_ 0 _,_ 1 _}_<sup>_n×|C|_</sup> by 4:1 ratio. We use _R_ to train the models, then generate synthetic samples _S ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> that are assessed in various tasks. For medGAN and VAE, we round the values of the generated dataset to the nearest integer values. 

- **Dimension-wise probability:** This is a basic sanity check to confirm the model has learned each dimension’s distribution correctly. We use the training set _R_ to train the models, then generate the same number of synthetic samples _S_ . Using _R_ and _S_ , we compare the Bernoulli success probability _pk_ of each dimension _k_ . 

- **Dimension-wise prediction:** This task indirectly measures how well the model captures the interdimensional relationships of the real samples. After training the models with _R_ to generate _S_ , we choose one dimension _k_ to be the label **y** _Rk ∈{_ 0 _,_ 1 _}_<sup>_N_</sup> and **y** _Sk ∈{_ 0 _,_ 1 _}_<sup>_N_</sup> . The remaining _R\k ∈{_ 0 _,_ 1 _}_<sup>_N×|C|−_1</sup> and _S\k ∈{_ 0 _,_ 1 _}_<sup>_N×|C|−_1</sup> are used as features to train two logistic regression classifiers LR _Rk_ and LR _Sk_ to predict **y** _Rk_ and **y** _Sk_ , respectively. Then, we use the model LR _Rk_ and LR _Sk_ to predict label **y** _Tk ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> of the test set _T_ . We can assume that the closer the performance of LR _Sk_ to that of LR _Rk_ , the better the quality of the synthetic dataset _S_ . We use F1-score to measure the prediction performance, with the threshold set to 0.5. 

To mitigate the repetition of results, we present our evaluation of dataset A in this section and direct the reader to Appendix C for the results from dataset B. 

8 



<!-- Start of picture text -->
GAN GANP GANPD GANPA medGAN<br>(a) Dimension-wise prediction performance of various versions of medGAN.<br>RN IS DBM VAE medGAN<br>(b) Dimension-wise prediction performance of baseline models and medGAN.<br><!-- End of picture text -->

Figure 3: Scatterplots of dimension-wise prediction results. Each dot represents one of 615 codes. The x-axis represents the F1-score of the logistic regression classifier trained on the real dataset A. The y-axis represents the F1-score of the classifier trained on the synthetic counterpart generated by each model. The diagonal line indicates the ideal performance where the real and synthetic data show identical quality. 

#### 4.2.1 DIMENSIONS-WISE PROBABILITY 

There are several notable findings that are worth highlighting. The dimension-wise probability performance increased as we used more advanced versions of medGAN, where the full medGAN shows the best performance as depicted by figure 2a. Note that minibatch averaging significantly increases the performance. Since minibatch averaging provides Bernoulli success probability information of real data to the model during training, it is natural that the generator learns to output synthetic data that follow a similar distribution. Minibatch discrimination does not seem to improve the results. This is most likely due to the discrete nature of the datasets. Improving the learning efficiency of the generator _G_ with batch normalization and shortcut connection clearly helped improve the results. 

Figure 2b compares the dimension-wise probability performance of baseline models with medGAN. Independent sampling (IS) naturally shows great performance as expected. DBM, given its stochastic binary nature, shows comparable performance as medGAN. VAE, although slightly inferior to DBM and medGAN, seems to capture the dimension-wise distribution relatively well, showing specific weakness at processing codes with low probability. Overall, we can see that medGAN clearly captures the independent distribution of each code. 

#### 4.2.2 DIMENSIONS-WISE PREDICTION 

Figure 3a shows the dimension-wise prediction performance of various versions of medGAN. The full medGAN again shows the best performance as it did in the dimension-wise probability task. Although the advanced versions of medGAN do not seem to dramatically increase the performance as they did for the previous task, this is due to the complex nature of inter-dimensional relationship compared to the independent dimension-wise probability. Figure 3b shows the dimension-wise prediction performance of baseline models compared to medGAN. As expected, IS is incapable of capturing the inter-dimensional relationship, given its naive sampling method. VAE shows similar behavior as it did in the previous task, showing weakness at predicting codes with low occurrence probability. Again, DBM shows comparable, if not slightly better performance to medGAN, which seems to come from its binary nature. 

#### **4.3 Qualitative Evaluation for Count Variables** 

We conducted a qualitative evaluation of medGAN with the help from a medical doctor. A discussion with the doctor taught us that count data are easier to assess its _realistic-ness_ than binary data. Therefore we use dataset C to train medGAN and generate synthetic count samples. In this experiment, we randomly pick 50 records from real data and 50 records from synthetic data, randomly shuffle the order, present them to a medical doctor (specialized in internal medicine) who is asked to score how realistic each record is using scale 1 to 10 (10 being most realistic). Here the human doctor is served as the role of discriminator to provide the quality assessment of the synthetic data generated by medGAN. 

9 



<!-- Start of picture text -->
Real medGAN<br>10<br>8<br>6<br>4<br>2<br>0<br><!-- End of picture text -->

Figure 4: Boxplot of the impression scores from a medical expert. 

The results of this assessment is shown in Figure 4. The findings suggest that medGAN’s synthetic data are generally indistinguishable to a human doctor except for several outliers. In those cases, the fake records identified by the doctor either lacked appropriate medication codes, or had both male-related codes ( _e.g._ prostate cancer) and female-related codes ( _e.g._ menopausal disorders) in the same record. The former issue also existed in some of the real records due to missing data, but the latter issue demonstrates a current limitation in medGAN which could potentially be alleviated by domain specific heuristics. In addition to medGAN’s impressive performance in statistical aspects, this medical review lends credibility to the qualitative aspect of medGAN. 

#### **4.4 Privacy Risk Evaluation** 



<!-- Start of picture text -->
1.0 1.0<br>.75 (a) .75 (b)<br>.50 .50<br>.25 .25<br>0.0 0.0<br>2 0 2 1 2 2 2 3 2 4 2 5 2 6 2 7 2 8 2 0 2 1 2 2 2 3 2 4 2 5 2 6 2 7 2 8<br>Number of known attributes Number of known attributes<br>1.0 1.0<br>.75 (c) .75 (d)<br>.50 .50<br>.25 .25<br>0.0 0.0<br>3k 9k 15k 21k 27k 33k 37k 3k 9k 15k 21k 27k 33k 37k<br>Size of the synthetic dataset Size of the synthetic dataset<br>Sensitivity Precision<br>Sensitivity Precision<br><!-- End of picture text -->

Figure 5: **a,b:** Sensitivity and precision when varying the number of known attributes. The total number of attributes ( _i.e._ codes) of dataset B is 1,071. **c,d:** Sensitivity and precision when varying the size of the synthetic dataset. The maximum size of the synthetic dataset _S ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> is matched to the size of the training set _R ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> . 

We evaluate both presence and attribute disclosure using dataset B with binary variables. Due to the space constraint, we present the results of the attribute disclosure in the main paper and leave out the results of presence disclosure in Appendix F. 

**Experiment setup:** We randomly sample 1% of the training set _R_ as the compromised records, which is approximately 370 records. For each record _r_ , we randomly choose _s_ attributes as those which are known to the attacker. Next, the attacker performs _k_ -nearest neighbor classifications to estimate the values of unknown attributes based on the synthetic records. More specifically, based on the known attributes, _k_ -nearest neighbors in the synthetic dataset _S_ are retrieved for each compromised record. Then, _|C| − s_ unknown attributes are estimated based on the majority vote of the _k_ nearest neighbors. Finally, for each unknown attribute, we calculate classification metrics in the form of precision and sensitivity. We repeat this process for all records of the 1% samples and obtain the mean precision and mean sensitivity. We vary the number of known attributes _s_ and the number of neighbors _k_ to study the attribute disclosure risk of medGAN. Note that the _s_ attributes are randomly sampled across patients, so the attacker may know different _s_ attributes for different patients. 

**Impact of attacker’s knowledge:** Figures 5a and 5b depict the sensitivity (i.e., recall) and the precision of the attribute disclosure test when varying the number of attributes known to the attacker. In this case, _x_ % sensitivity means the attacker, using the known attributes of the compromised record and the synthetic data, can correctly estimate _x_ % of the positive unknown attributes (i.e., attribute values are 1). Likewise, _x_ % precision means the positive unknown attributes estimated by the attacker are on average _x_ % accurate. Both figures show that an attacker who knows approximately 1% of the target patient’s attributes (8 to 16 attributes) will estimate the target’s unknown attributes with less than 10% sensitivity and 20% precision. 

**Impact of synthetic data size:** Next, we fixed the number of known attributes to 16 and varied the number of records in the synthetic dataset _S_ . Figures 5c and 5d show that the size of the synthetic dataset has little 

10 

influence on the effectiveness of the attack. In general, 1 nearest neighbor seems to be the most effective attack, although the sensitivity is still below 25% at best. 

Overall, our privacy experiments indicate that medGAN does not simply remember the training samples and reproduce them. Rather, medGAN generates diverse synthetic samples that reveal little information to potential attackers unless they already possess significant amount of knowledge about the target patient. 

### **5. Conclusion** 

In this work, we proposed medGAN, which uses generative adversarial framework to learn the distribution of real-world multi-label discrete electronic health records (EHR). Through rigorous evaluation using real datasets, medGAN showed impressive results for both binary variables and count variables. Considering the difficult accessibility of EHRs, we expect medGAN to make a contribution for healthcare research. We also provided empirical evaluation of privacy, which demonstrates very limited risks of medGAN in attribute disclosure. For future directions, we plan to explore the sequential version of medGAN, and also try to include other modalities such as lab measures, patient demographics, and free-text medical notes. 

### **Acknowledgments** 

This work was supported by the National Science Foundation, award IIS-#1418511 and CCF-#1533768, Children’s Healthcare of Atlanta, Google Faculty Award, UCB and Samsung Scholarship. Dr. Malin was supported by the National Science Foundation, award IIS-#1418504. 

11 

### **References** 

- R. V. Atreya, J. C. Smith, A. B. McCoy, B. Malin, and R. A. Miller. Reducing patient re-identification risk for laboratory results within research datasets. _Journal of the American Medical Informatics Association_ , 20(1): 95–101, 2013. 

- Anna Buczak, Steven Babin, and Linda Moniz. Data-driven approach for creating synthetic electronic medical records. _BMC Medical Informatics and Decision Making_ , 10(1):59, 2010. 

- Emily Denton, Soumith Chintala, Rob Fergus, et al. Deep generative image models using a laplacian pyramid of adversarial networks. In _NIPS_ , pages 1486–1494, 2015. 

- Josep Domingo-Ferrer and Vicenc¸ Torra. Disclosure risk assessment in statistical microdata protection via advanced record linkage. _Statistics and Computing_ , 13(4):343–354, 2003. ISSN 1573-1375. doi: 10.1023/A:1025666923033. URL http://dx.doi.org/10.1023/A:1025666923033. 

- J Dreschsler. _Synthetic datasets for statistical disclosure control_ . Springer Press, 2011. 

- K. El Emam, D. Buckeridge, R. Tamblyn, A. Neisa, E. Jonker, and A. Verma. The re-identification risk of canadians from longitudinal demographics. _BMC Medical Informatics and Decision Making_ , 11:46, 2011a. 

- K. El Emam, E. Jonker, L. Arbuckle, and B. Malin. A systematic review of re-identification attacks on health data. _PLoS ONE_ , 6(12):e28071, 2011b. 

- K. El Emam, S. Rodgers, and B. Malin. Anonymising and sharing individual patient data. _British Medical Journal_ , 350:h1139, 2015. 

- Y. Erlich and A. Narayanan. Routes for breaching and protecting genetic privacy. _Nature Reviews Genetics_ , 15(6):409–421, 2014. 

- Office for Civil Rights. _Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule_ . U.S. Department of Health and Human Services, 2013. 

- Peter V Gehler, Alex D Holub, and Max Welling. The rate adapting poisson model for information retrieval and object recognition. In _Proceedings of the 23rd international conference on Machine learning_ , pages 337–344. ACM, 2006. 

- John Glover. Modeling documents with generative adversarial networks. _arXiv:1612.09122_ , 2016. 

- Ary Goldberger et al. Physiobank, physiotoolkit, and physionet components of a new research resource for complex physiologic signals. _Circulation_ , 2000. 

- Ian Goodfellow. Nips 2016 tutorial: Generative adversarial networks. _arXiv:1701.00160_ , 2016. 

- Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative adversarial nets. In _NIPS_ , pages 2672–2680, 2014. 

- Ian Goodfellow, Yoshua Bengio, and Aaron Courville. _Deep Learning_ . MIT Press, 2016. 

- Lawrence Gostin, Laura Levit, Sharyl Nass, et al. _Beyond the HIPAA Privacy Rule: Enhancing Privacy, Improving Health Through Research_ . National Academies Press, 2009. 

- Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In _CVPR_ , pages 770–778, 2016. 

- Geoffrey Hinton and Ruslan Salakhutdinov. Reducing the dimensionality of data with neural networks. _Science_ , 313(5786):504–507, 2006. 

12 

- Geoffrey E Hinton and Ruslan R Salakhutdinov. Replicated softmax: an undirected topic model. In _Advances in neural information processing systems_ , pages 1607–1614, 2009. 

- James Hodge Jr, Lawrence O Gostin, and Peter Jacobson. Legal issues concerning electronic health information: privacy, quality, and liability. _Jama_ , 282(15):1466–1471, 1999. 

- Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. _arXiv:1502.03167_ , 2015. 

- Eric Jang, Shixiang Gu, and Ben Poole. Categorical reparameterization with gumbel-softmax. _arXiv:1611.01144_ , 2016. 

Alistair Johnson et al. Mimic-iii, a freely accessible critical care database. _Scientific Data_ , 3, 2016. 

- Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv:1412.6980_ , 2014. 

- Diederik Kingma and Max Welling. Auto-encoding variational bayes. _arXiv:1312.6114_ , 2013. 

- Matt J Kusner and Jose Miguel Hern´ andez-Lobato.´ Gans for sequences of discrete elements with the gumbelsoftmax distribution. _arXiv:1611.04051_ , 2016. 

- Joseph S Lombardo and Linda J Moniz. Ta method for generation and distribution. _Johns Hopkins APL Technical Digest_ , 27(4):356, 2008. 

- G. Loukides, J. C. Denny, and B. Malin. The disclosure of diagnosis codes can breach research participants’ privacy. _J Am Med Inform Assoc_ , 17(3):322–327, 2010. 

- Chris Maddison, Andriy Mnih, and Yee Whye Teh. The concrete distribution: A continuous relaxation of discrete random variables. _arXiv:1611.00712_ , 2016. 

- B. Malin and L. Sweeney. How (not) to protect genomic data privacy in a distributed network: using trail re-identification to evaluate and design anonymity protection systems. _Journal of Biomedical Informatics_ , 37(3):179–192, 2004. 

- Stan Matwin, Jordi Nin, Morvarid Sehatkar, and Tomasz Szapiro. _A Review of Attribute Disclosure Control_ , pages 41–61. Springer International Publishing, Cham, 2015. ISBN 978-3-319-09885-2. doi: 10.1007/ 978-3-319-09885-2 ~~4~~ . URL http://dx.doi.org/10.1007/978-3-319-09885-2_4. 

- Scott McLachlan, Kudakwashe Dube, and Thomas Gallagher. Using the caremap with health incidents statistics for generating the realistic synthetic electronic healthcare record. In _Healthcare Informatics (ICHI), 2016 IEEE International Conference on_ , pages 439–448. IEEE, 2016. 

- Luke Metz, Ben Poole, David Pfau, and Jascha Sohl-Dickstein. Unrolled generative adversarial networks. _arXiv:1611.02163_ , 2016. 

- Mehdi Mirza and Simon Osindero. Conditional generative adversarial nets. _arXiv:1411.1784_ , 2014. 

- Mehmet Nergiz and Chris Clifton. _δ_ -presence with complete world knowledge. _IEEE Transactions on Knowledge Engineering_ , 22:868–883, 2010. 

- Augustus Odena, Christopher Olah, and Jonathon Shlens. Conditional image synthesis with auxiliary classifier gans. _arXiv:1610.09585_ , 2016. 

- Yubin Park, Joydeep Ghosh, and Mallikarjun Shankar. Perturbed gibbs samplers for generating large-scale privacy-safe synthetic health data. In _Healthcare Informatics (ICHI), 2013 IEEE International Conference on_ , pages 493–498. IEEE, 2013. 

13 

- Alec Radford, Luke Metz, and Soumith Chintala. Unsupervised representation learning with deep convolutional generative adversarial networks. _arXiv:1511.06434_ , 2015. 

- Scott Reed, Zeynep Akata, Xinchen Yan, Lajanugen Logeswaran, Bernt Schiele, and Honglak Lee. Generative adversarial text to image synthesis. In _ICML_ , 2016. 

- J. Reiter. Satisfying disclosure restrictions with synthetic datasets. _Journal of Official Statistics_ , 18(4):531–543, 2002. 

- Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved techniques for training gans. In _NIPS_ , pages 2226–2234, 2016. 

- Reza Shokri, Marco Stronati, Congzheng Song, and Vitaly Shmatikov. Membership inference attacks against machine learning models. In _IEEE Security & Privacy Conference_ , page in press, 2017. 

- L. Sweeney. Weaving technology and policy together to maintain confidentiality. _Journal of Law, Medicine, and Ethics_ , 25(2-3):98–110, 1997. 

- TensorFlow Team. TensorFlow: Large-scale machine learning on heterogeneous systems, 2015. URL http://tensorflow.org/. Software available from tensorflow.org. 

- Truyen Tran, Dinh Phung, and Svetha Venkatesh. Mixed-variate restricted boltzmann machines. In _Asian Conference on Machine Learning_ , pages 213–229, 2011. 

- Aaron van den Oord, Nal Kalchbrenner, Lasse Espeholt, Oriol Vinyals, Alex Graves, et al. Conditional image generation with pixelcnn decoders. In _NIPS_ , pages 4790–4798, 2016a. 

- Aaron van den Oord, Nal Kalchbrenner, and Koray Kavukcuoglu. Pixel recurrent neural networks. _arXiv:1601.06759_ , 2016b. 

- Pascal Vincent, Hugo Larochelle, Yoshua Bengio, and Pierre-Antoine Manzagol. Extracting and composing robust features with denoising autoencoders. In _ICML_ , pages 1096–1103, 2008. 

- Ronald Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. _Machine learning_ , 8(3-4):229–256, 1992. 

- Lantao Yu, Weinan Zhang, Jun Wang, and Yong Yu. Seqgan: Sequence generative adversarial nets with policy gradient. _arXiv:1609.05473_ , 2016. 

- Yizhe Zhang, Zhe Gan, and Lawrence Carin. Generating text via adversarial training. _NIPS Workshop on Adversarial Training_ , 2016. 

14 

**Algorithm 1** medGAN Optimization 

_θd, θg, θenc, θdec ←_ Initialize with random values. **repeat** // Pre-train the autoencoder Randomly sample **x** 1 _,_ **x** 2 _, . . . ,_ **x** _m_ from **X** Update _θenc, θdec_ by minimizing Eq.(2) (or Eq.(3)) **until** convergence or fixed iterations **repeat for** _k_ steps **do** // Update the discriminator. Randomly sample **z** 1 _,_ **z** 2 _, . . . ,_ **z** _m_ from _p_ **z** Randomly sample **x** 1 _,_ **x** 2 _, . . . ,_ **x** _m_ from **X xz** _i ← Dec_ ( _G_ ( **z** _i_ )) **x** ¯ **z** _← m_<sup><u>1</u></sup> � _mi_ =1<sup>**xz**</sup> _i_ **x** ¯ _← m_<sup><u>1</u></sup> <u>�</u> _mi_ =1<sup>**x**</sup><sup>_i_</sup> Ascend _θd_ by the gradient: _∇θd m_ <u>1</u> � _mi_ =1<sup>log</sup><sup>_D_(</sup><sup>**x**</sup><sup>_i,_¯</sup><sup>**x**) + log(1</sup><sup>_−D_(</sup><sup>**xz**</sup> _i_<sup>_,_¯</sup><sup>**xz**))</sup> **end for** // Update the generator and the decoder. Randomly sample **z** 1 _,_ **z** 2 _, . . . ,_ **z** _m_ from _p_ **z xz** _i ← Dec_ ( _G_ ( **z** _i_ )) **x** ¯ **z** _← m_<sup><u>1</u></sup> � _mi_ =1<sup>**xz**</sup> _i_ Ascend _θg, θdec_ by the gradient: _∇θg,dec m_ <u>1</u> � _mi_ =1<sup>log</sup><sup>_D_(</sup><sup>**xz**</sup> _i_<sup>_,_¯</sup><sup>**xz**)</sup> **until** convergence or fixed iterations 

# **Appendices** 

### **Appendix A. medGAN training algorithm** 

Algorithm 1 describes the overall optimization process of medGAN. Note that _θd_ is updated _k_ times per iteration, while _θg_ and _θdec_ are updated once per iteration to ensure optimality of _D_ . However, typically, a larger _k_ has not shown a clear improvement (Goodfellow, 2016). And we set _k_ = 2 in our experiments. 

### **Appendix B. Hyperparameter details** 

We describe the architecture and the hyper-parameter values used for each model. We tested all models by varying the number of hidden layers (while matching the number of parameters used for generating synthetic data), the size of the minibatch, the learning rate, the number of training epochs, and we report the best performing configuration for each model. 

- **medGAN** : Both the encoder _Enc_ and the decoder _Dec_ are single layer feedforward networks, where the original input **x** is compressed to a 128 dimensional vector. The generator _G_ is implemented as a feedforward network with two hidden layers, each having 128 dimensions. For the batch normalization in the generator _G_ , we use both the scale parameter _γ_ and the shift parameter _β_ , and set the moving average decay to 0.99. The discriminator _D_ is also a feedforward network with two hidden layers where the first layer has 256 dimensions and the second layer has 128 dimensions. medGAN is trained for 1,000 epochs with the minibatch of 1,000 records. 

- **DBM** : In order to match the number of parameters used for data generation in medGAN ( _G_ + _Dec_ ), we used four layers of Restricted Boltzmann Machines where the first layer is the input layer. All hidden layers used 128 dimensions. We performed layer-wise greedy persistent contrastive divergence (20-step 

15 

Gibbs sampling) to train DBM. We used 0.01 for learning rate and 100 samples per minibatch. All layers were separately trained for 100 epochs. Synthetic samples were generated by performing Gibbs sampling at the two two layers then propagating the values down to the input layer. We ran Gibbs sampling for 1000 iterations per sample. Using three stacks showed small performance degradation. 

- **VAE** : In order to match the number of parameters used for data generation in medGAN ( _G_ + _Dec_ ), both the encoder and the decoder were implemented with feedforward networks, each having 3 hidden layers. The encoder accepts the input **x** and compresses it to a 128 dimensional vector and the decoder reconstructs it to the original dimension space. VAE was trained with Adam for 1,000 iterations with the minibatch of 1,000 records. Using two hidden layers for the encoder and the decoder showed similar performance. 

### **Appendix C. Quantitative evaluation results for binary dataset B** 



<!-- Start of picture text -->
GAN GANP GANPD GANPA medGAN<br>(a) Dimension-wise probability performance of various versions of medGAN.<br>RN IS DBM VAE medGAN<br>(b) Dimension-wise probability performance of baseline models and medGAN.<br><!-- End of picture text -->

Figure 6: Scatterplots of dimension-wise probability results. Each dot represents one of 1,071 codes. The x-axis represents the Bernoulli success probability for the real dataset B, and y-axis the probability for the synthetic counterpart generated by each model. The diagonal line indicates the ideal performance where the real and synthetic data show identical quality. 



<!-- Start of picture text -->
GAN GANP GANPD GANPA medGAN<br>(a) Dimension-wise prediction performance of various versions of medGAN.<br>RN IS DBM VAE medGAN<br>(b) Dimension-wise prediction performance of baseline models and medGAN.<br><!-- End of picture text -->

Figure 7: Scatterplots of dimension-wise prediction results. Each dot represents one of 1,071 codes. The x-axis represents the F1-score of the logistic regression classifier trained on the real dataset B. The y-axis represents the F1-score of the classifier trained on the synthetic counterpart generated by each model. The diagonal line indicates the ideal performance where the real and synthetic data show identical quality. 

16 

#### **C.1 Dimension-wise probability** 

Figure 6a shows the consistent superiority of the full version of medGAN compared other versions. The effect of minibatch averaging is even more dramatic for dataset B. Figure 6b shows that VAE has some difficulty capturing the dimension-wise distribution of dataset B. Again, DBM shows comparable performance to medGAN, slightly outperforming medGAN for low-probability codes, but slightly underperforming for high-probability codes. Overall, dimension-wise probability performance is somewhat weaker for dataset B than for dataset A, most likely due to smaller data volume and sparser code distribution. 

#### **C.2 Dimension-wise prediction** 

Figure 7a shows the dimension-wise predictive performance for different versions of medGAN where the full version outperforms others. Figure 7b shows similar pattern as Figure 3b. Independent sampling completely fails to make any meaningful prediction. VAE demonstrates weakness at predicting low-probability codes. DBM seems to slightly outperform medGAN, especially for highly predictable codes. Again, due to the nature of the dataset, all models show weaker predictive performance for dataset B than they did for dataset A. 

### **Appendix D. Quantitative results for count variables** 

In order to evaluate for count variables, we use dataset C, consisting of 30,738 patients whose records were taken for exactly 18 months. The same subset was used to perform qualitative evaluation in section 4.3. The details of constructing dataset C for heart failure studies are described in Appendix E. Note that each patient’s number of hospital visits within the 18 months period can vary, which is a perfect test case for count variables. Again, we aggregate the dataset into a fixed-size vector and divide it into the training set _R ∈_ Z<sup>_N_</sup> +<sup>_×|C|_</sup> and the test set _T ∈_ Z<sup>_n_</sup> +<sup>_×|C|_</sup> in 4:1 ratio. Since we have confirmed the superior performance of full medGAN compared to other versions of GANs in binary variables evaluation, we focus on the comparison with baseline models in this section. Note that, to generate count variables, we replaced all activation functions in both VAE and medGAN (except the discriminator’s output) to ReLU. We also use kernel density estimator with Gaussian kernel (bandwidth=0.75) to perform the independent sampling (IS) baseline. We no longer test random noise (RN) method in this section as it is difficult to determine how much noise should be injected to count variables to keep them sufficiently realistic but different enough from the training set. 

For count variables, we conduct similar quantitative evaluations as binary variables with slight modifications. We first calculate dimension-wise average count instead of dimension-wise probability. For dimension-wise prediction, we use the binary labels **y** _Rk ∈{_ 0 _,_ 1 _}_<sup>_N_</sup> and **y** _Sk ∈{_ 0 _,_ 1 _}_<sup>_N_</sup> as before, but we train the logistic regression classifier with count samples _R\k ∈_ Z<sup>_N_</sup> +<sup>_×|C|−_1</sup> and _S\k ∈_ Z+<sup>_N×|C|−_1</sup> . The classifiers use count features as oppose to binary features while the evaluation metric is still F1-score. 

D.0.1 DIMENSIONS-WISE AVERAGE COUNT 



<!-- Start of picture text -->
5k<br>Essention Disorder of Connective Cardiac Skin<br>2.5k hypertension lipid metabolism tissue disease dysrhythmias disorders<br>0<br>5k<br>2.5k<br>0<br>0 25 50 0 25 50 0 25 50 0 25 50 0 25 50<br><!-- End of picture text -->

Figure 8: Histogram of counts of five most frequent codes from dataset C. The top row was plotted using the training dataset, the bottom row using medGAN’s synthetic dataset. 

Figure 9 shows the performance of baseline models and medGAN. The discontinuous behavior of VAE is due to its extremely low-variance synthetic samples. We found that, on average, VAE’s synthetic samples had 

17 



<!-- Start of picture text -->
IS-KDE VAE medGAN<br><!-- End of picture text -->

Figure 9: Scatterplot of dimension-wise average count of the training dataset (x-axis) versus the synthetic counterpart (y-axis). 



<!-- Start of picture text -->
IS-KDE VAE medGAN<br><!-- End of picture text -->

Figure 10: Scatterplot of dimension-wise prediction F1-score of logistic regression trained on the training dataset (x-axis) versus the classifier trained on the synthetic counterpart (y-axis). 

nine orders of magnitude smaller standard deviation than medGAN’s synthetic samples. medGAN, on the other hand, shows good performance with just a simple substitution of the activation functions. 

Figure 8 shows the count histograms of five most frequent codes from the count dataset, where the top row was plotted with the training dataset and the bottom row with medGAN’s synthetic dataset. We can see that medGAN’s synthetic counterpart has very similar distribution as the real data. This tells us that medGAN is not just trying to match the average count of codes ( _i.e._ binomial distribution mean), but learns the actual distribution of the data. 

#### D.0.2 DIMENSIONS-WISE PREDICTION 

Figure 10 shows the performance of baseline models and medGAN. We can clearly see that medGAN shows superior performance. The experiments on count variables is especially interesting, as medGAN seems to make a smooth transition from binary variables to count variables, with just a replacement of the activation function. We also speculate that the medGAN’s dimension-wise prediction performance will increase with more training data, as the count dataset used in this section consists of only 30,738 samples. 

### **Appendix E. Dataset construction for heart failure studies** 

Case patients were 40 to 85 years of age at the time of HF diagnosis. HF diagnosis (HFDx) is defined as: 1) Qualifying ICD-9 codes for HF appeared in the encounter records or medication orders. Qualifying ICD-9 codes are displayed in Table 2. 2) a minimum of three clinical encounters with qualifying ICD-9 codes had to occur within 12 months of each other, where the date of diagnosis was assigned to the earliest of the three dates. If the time span between the first and second appearances of the HF diagnostic code was greater than 12 months, the date of the second encounter was used as the first qualifying encounter. The date at which HF diagnosis was given to the case is denoted as HFDx. Up to ten eligible controls (in terms of sex, age, location) were selected for each case, yielding an overall ratio of 9 controls per case. Each control was also assigned an index date, which is the HFDx of the matched case. Controls are selected such that they did not meet the operational criteria for HF diagnosis prior to the HFDx plus 182 days of their corresponding case. Control subjects were required to have their first office encounter within one year of the matching HF case patients first office visit, and have at least one office encounter 30 days before or any time after the cases HF diagnosis date to ensure similar duration of observations among cases and controls. 

### **Appendix F. Presence disclosure** 

We performed a series of experiments to assess the extent to which medGAN leaks the presence of a patient. To do so, we randomly sample _r_ patient records from each of the training set _R ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> and the test set 

18 

Table 2: Qualifying ICD-9 codes for heart failure 



19 

_T ∈{_ 0 _,_ 1 _}_<sup>_n×|C|_</sup> . We assume the attacker has complete knowledge on those 2 _r_ records. Then for each record, we calculate its hamming distance to each sample from the synthetic dataset _S ∈{_ 0 _,_ 1 _}_<sup>_N×|C|_</sup> . If there is at least one synthetic sample within a certain distance, we treat that as its claimed match. Now, since we sample from both _R_ and _T_ , the match could be a true positive (i.e., attacker correctly claims their targeted record is in the GAN training set), false positive (i.e., attacker incorrectly claims their targeted record is in the GAN training set), true negative (i.e., attacker correctly claims their targeted record is not in the GAN training set), or false negative (i.e., attacker incorrectly claims their targeted record is not in the GAN training set). 

We varied the number of patients _r_ and the hamming distance threshold and calculated the sensitivity and precision. 



<!-- Start of picture text -->
(a) (b)<br>2k 4k 6k 8k 10k 2k 4k 6k 8k 10k<br>Number of patients known to attacker Number of patients known to attacker<br>(d)<br>(c)<br>5k 10k 15k 20k 25k 30k 35k 5k 10k 15k 20k 25k 30k 35k<br>Number of synthetic patients Number of synthetic patients<br>Number of synthetic patients Number of synthetic patients<br><!-- End of picture text -->

Figure 11: **a,b:** Sensitivity and precision while varying the number of patients known to the attacker. **c,d:** Sensitivity and precision while varying the number of synthetic patients. 

**Impact of attacker’s knowledge:** Figures 11a and 11b depict the sensitivity ( _i.e._ recall) and the precision of the presence disclosure test when varying the number of real patient the attacker knows. In this setting, _x_ % sensitivity means the attacker has successfully discovered that _x_ % of the records that he/she already knows were used to train medGAN. Similarly, _x_ % precision means, when an attacker claims that a certain number of patients were used for training medGAN, only _x_ % of them were actually used. Figure 11a shows that with low threshold of hamming distance (e.g. hamming distance of 0) attacker can only discover 10% percent of the known patients to attacker were used to train medGAN. Figure 11b shows that, the precision is mostly 50% except when the number of known patients are small. This indicates that the attacker’s knowledge is basically useless for presence disclosure attack unless the attacker is focusing on a small number of patients (less than a hundred), in which case the precision is approximately 80%. 

We conducted an additional experiment to evaluate the impact of the size of the synthetic data on presence disclosure risk. In this experiment, we fix the number of known real patients to 100 and varied the number of records in the synthetic dataset _S_ . Figures 11c and 11d show that the size of the generated synthetic dataset has almost no impact on presence disclosure. 

20 

