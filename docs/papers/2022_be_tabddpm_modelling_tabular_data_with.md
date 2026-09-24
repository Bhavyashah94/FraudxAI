---
title: "TabDDPM: Modelling Tabular Data with Diffusion Models"
authors: "be-"
year: 2022
arxiv_id: "2209.15421"
original_file: "2209.15421.pdf"
pdf_path: "docs/papers\2022_be_tabddpm_modelling_tabular_data_with.pdf"
---

# TabDDPM: Modelling Tabular Data with Diffusion Models

**Authors:** Be- et al.  
**Year:** 2022 | **arXiv:** [`2209.15421`](https://arxiv.org/abs/2209.15421)  
**Local PDF:** [`2022_be_tabddpm_modelling_tabular_data_with.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_be_tabddpm_modelling_tabular_data_with.pdf)

---

## **TabDDPM: Modelling Tabular Data with Diffusion Models** 

**Akim Kotelnikov**<sup>1 2</sup> **Dmitry Baranchuk**<sup>2</sup> **Ivan Rubachev**<sup>1 2</sup> **Artem Babenko**<sup>2</sup> 

### **Abstract** 

Denoising diffusion probabilistic models are becoming the leading generative modeling paradigm for many important data modalities. Being the most prevalent in the computer vision community, diffusion models have recently gained some attention in other domains, including speech, NLP, and graph-like data. In this work, we investigate if the framework of diffusion models can be advantageous for general tabular problems, where data points are typically represented by vectors of heterogeneous features. The inherent heterogeneity of tabular data makes it quite challenging for accurate modeling since the individual features can be of a completely different nature, i.e., some of them can be continuous and some can be discrete. To address such data types, we introduce TabDDPM — a diffusion model that can be universally applied to any tabular dataset and handles any feature types. We extensively evaluate TabDDPM on a wide set of benchmarks and demonstrate its superiority over existing GAN/VAE alternatives, which is consistent with the advantage of diffusion models in other fields. The source code of TabDDPM is available at GitHub. 

### **1. Introduction** 

Denoising diffusion probabilistic models (DDPM) (SohlDickstein et al., 2015; Ho et al., 2020) have recently become an object of great research interest in the generative modeling community since they often outperform the alternative approaches both in terms of the realism of individual samples and their diversity (Dhariwal & Nichol, 2021). The most impressive successes of DDPM were demonstrated in the domain of natural images (Dhariwal & Nichol, 2021; Saharia et al., 2022; Rombach et al., 2022), where the advantages of diffusion models are successfully exploited in 

1HSE university, Moscow, Russia 2Yandex, Moscow, Russia. Correspondence to: Akim Kotelnikov _<_ ya@akotelnikov.ru _>_ . 

_Proceedings of the 40_<sup>_th_</sup> _International Conference on Machine Learning_ , Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright 2023 by the author(s). 

applications, such as colorization (Song et al., 2021), inpainting (Song et al., 2021), segmentation (Baranchuk et al., 2021), super-resolution (Saharia et al., 2021; Li et al., 2021), semantic editing (Meng et al., 2021) and others. Beyond computer vision, the DDPM framework is also investigated in other fields, such as NLP (Austin et al., 2021; Li et al., 2022), waveform signal processing (Kong et al., 2020; Chen et al., 2020b), molecular graphs (Jing et al., 2022; Hoogeboom et al., 2022), time series (Tashiro et al., 2021), testifying the universality of diffusion models across a wide range of problems. 

Our work aims to investigate if the universality of DDPM can be extended to the case of general tabular problems, which are ubiquitous in various industrial applications that include data described by a set of heterogeneous features. For many such applications, the demand for high-quality generative models is especially acute because of the modern privacy regulations, like GDPR, which prevent publishing real user data, while the synthetic data produced by generative models can be shared. However, training a highquality model of tabular data can be more challenging than in computer vision or NLP due to the heterogeneity of individual features and relatively small sizes of typical tabular datasets. This paper shows that despite these two intricacies, the diffusion models can successfully approximate typical distributions of tabular data, leading to state-of-the-art performance on most of the benchmarks. In more detail, the main contributions of this work are the following: 

1. We introduce TabDDPM — a simple design of DDPM for tabular problems that can be applied to any tabular task and work with mixed data types, including numerical and categorical features. 

2. We demonstrate that TabDDPM outperforms the alternative approaches designed for tabular data, including GAN-based and VAE-based methods, and illustrate the sources of this advantage on several datasets. 

3. We observe that shallow interpolation-based methods, e.g., SMOTE (Chawla et al., 2002), produce surprisingly effective synthetic data that provides competitively high ML efficiency. Compared with SMOTE, we show that TabDDPM’s data is preferable for privacy-concerned scenarios when synthetic data is used to substitute the real user data that cannot be shared. 

1 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

### **2. Related Work** 

**Diffusion models** (Sohl-Dickstein et al., 2015; Ho et al., 2020) is a paradigm of generative modeling that aims to approximate the target distribution by the endpoint of the Markov chain, which starts from a given parametric distribution, typically a standard Gaussian. Each Markov step is performed by a deep neural network that effectively learns to invert the diffusion process with a known Gaussian kernel. Ho et al. demonstrated the equivalence of diffusion models and score matching (Song & Ermon, 2019; 2020), showing them to be two different perspectives on the gradual conversion of a simple known distribution into a target distribution via the iterative denoising process. Several recent works (Nichol, 2021; Dhariwal & Nichol, 2021) have developed more powerful model architectures as well as different advanced learning protocols, which led to the “victory” of DDPM over GANs in terms of generative quality and diversity in the computer vision field. In this work, we demonstrate that one can also successfully use diffusion models for tabular problems. 

**Generative models for tabular problems** are currently an active research direction in the machine learning community since high-quality synthetic data is in great demand for many tabular tasks. First, the tabular datasets are often limited in size, unlike in vision or NLP problems, for which massive “extra” data is available on the Internet. Second, proper synthetic datasets do not contain actual user data. Therefore, they are not subject to GDPR-like regulations and can be publicly shared without violating anonymity. The recent works have developed a large number of models, including tabular VAEs (Xu et al., 2019) and GAN-based approaches (Xu et al., 2019; Engelmann & Lessmann, 2021; Jordon et al., 2018; Fan et al., 2020; Torfi et al., 2022; Zhao et al., 2021; Kim et al., 2021; Zhang et al., 2021; Nock & Guillame-Bert, 2022; Wen et al., 2022). By extensive evaluations on a large number of public benchmarks, we show that TabDDPM surpasses the existing alternatives, often by a large margin. 

**“Shallow” synthetics generation.** Unlike unstructured images or natural texts, tabular data is typically structured, i.e., the individual features are often interpretable and it is unclear if their modeling requires several layers of “deep” architectures. Therefore, the simple interpolation techniques, like SMOTE (Chawla et al., 2002) (originally proposed to address class imbalance) can serve as simple and powerful solutions as demonstrated in (Camino et al., 2020), where SMOTE is shown to outperform tabular GANs for minor class oversampling. In the experiments, we demonstrate the advantage of TabDDPM’s synthetics over synthetics produced with interpolation techniques from the privacypreserving perspective. 

### **3. Background** 

**Diffusion models** (Sohl-Dickstein et al., 2015; Ho et al., 2020) are likelihood-based generative models that handle the data through forward and reverse Markov processes. The forward process _q_ ( _x_ 1: _T |x_ 0) =<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_q_(</sup><sup>_xt|xt−_1) gradually</sup> adds noise to an initial sample _x_ 0 from the data distribution _q_ ( _x_ 0) sampling noise from the predefined distributions _q_ ( _xt|xt−_ 1) with variances _{β_ 1 _, ..., βT }_ . 

The reverse process _p_ ( _x_ 0: _T_ ) =<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_p_(</sup><sup>_xt−_1</sup><sup>_|xt_) gradually</sup> denoises a latent variable _xT ∼q_ ( _xT_ ) and allows generating new data samples from _q_ ( _x_ 0). Distributions _p_ ( _xt−_ 1 _|xt_ ) are usually unknown and approximated by a neural network with parameters _θ_ . These parameters are learned from the data by optimizing a variational lower bound: 



**Gaussian diffusion models** operate in continuous spaces ( _xt ∈_ R<sup>_n_</sup> ) where forward and reverse processes are characterized by Gaussian distributions: 



Ho et al. (2020) suggest using diagonal Σ _θ_ ( _xt, t_ ) with a constant _σt_ and computing _µθ_ ( _xt, t_ ) as a function of _xt_ and _ϵθ_ ( _xt, t_ ): 



where _αt_ := 1 _− βt, α_ ¯ _t_ :=<sup>�</sup> _i≤t_<sup>_αi_and</sup><sup>_ϵθ_(</sup><sup>_xt, t_) predicts a</sup> “groundtruth” noise component _ϵ_ for the noisy data sample _xt_ . In practice, the objective Equation 1 can be simplified to the sum of mean-squared errors between _ϵθ_ ( _xt, t_ ) and _ϵ_ over all timesteps _t_ : 



**Multinomial diffusion models** (Hoogeboom et al., 2021) are designed to generate categorical data where _xt ∈ {_ 0 _,_ 1 _}_<sup>_K_</sup> is a one-hot encoded categorical variable with _K_ values. The multinomial forward diffusion process defines _q_ ( _xt|xt−_ 1) as a categorical distribution that corrupts the data by uniform noise over _K_ classes: 



2 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Figure 1._ TabDDPM scheme for classification problems; _t_ , _y_ and _ℓ_ denote a diffusion timestep, a class label, and logits, respectively. 



<!-- Start of picture text -->
0.8<br>Quantile<br>-3.0<br>Transformer<br>1.2<br>MLP<br>A Softmax<br>One-hot<br>Encoder<br><!-- End of picture text -->

From the equations above, the posterior _q_ ( _xt−_ 1 _|xt, x_ 0) can be derived: 





The reverse distribution _pθ_ ( _xt−_ 1 _|xt_ ) is parameterized as _q_ ( _xt−_ 1 _|xt,_ ˆ _x_ 0( _xt, t_ )), where _x_ ˆ0 is predicted by a neural network. Then, the model is trained to maximize the variational lower bound Equation 1. 

### **4. TabDDPM** 

In this section, we describe the design of TabDDPM as well as its main hyperparameters, which affect the model’s effectiveness. 

**TabDDPM** uses the multinomial diffusion to model the categorical and binary features, and the Gaussian diffusion to model the numerical ones. In more detail, for a tabular data sample _x_ = [ _x_ num _, x_ cat1 _, ..., x_ cat _C_ ], that consists of _N_ num numerical features _x_ num _∈_ R<sup>_N_num</sup> and _C_ categorical features _x_ cat _i_ with _Ki_ categories each, our model takes onehot encoded versions of categorical features as an input (i.e. _x_<sup>ohe</sup> cat _i_<sup>_∈{_0</sup><sup>_,_1</sup><sup>_}Ki_) and normalized numerical features.There-</sup> fore, the input _x_ 0 has a dimensionality of ( _N_ num +<sup>�</sup> _Ki_ ). For preprocessing, we use the gaussian quantile transformation from the scikit-learn library (Pedregosa et al., 2011). Each categorical feature is handled by a separate forward diffusion process, i.e., the noise components for all features are sampled independently. The reverse diffusion step in TabDDPM is modeled by a multi-layer neural network that has an output of the same dimensionality as _x_ 0, where the first _N_ num coordinates are the predictions of _ϵ_ for the Gaussian diffusion and the rest are the predictions of _x_<sup>ohe</sup> cat _i_<sup>for the</sup> multinomial diffusions. 

The TabDDPM model for the classification problems is schematically presented on Figure 1. The model is trained 

by minimizing a sum of mean-squared error _L_<sup>simple</sup> _t_ (Equation 2) for the Gaussian diffusion term and the KL divergences _L_<sup>_i_</sup> _t_<sup>for each multinomial diffusion term (Equation 1).</sup> The total loss of multinomial diffusions is additionally divided by the number of categorical features. 



For classification datasets, we use a class-conditional model, i.e., _pθ_ ( _xt−_ 1 _|xt, y_ ) is learned. For regression datasets, we consider a target value as an additional numerical feature, and the joint distribution is learned. 

To model the reverse process, we use a simple MLP architecture adapted from (Gorishniy et al., 2021): 

MLP( _x_ ) = Linear (MLPBlock ( _. . ._ (MLPBlock( _x_ )))) MLPBlock( _x_ ) = Dropout(ReLU(Linear( _x_ ))) 



As in (Nichol, 2021; Dhariwal & Nichol, 2021), a tabular input _xin_ , a timestep _t_ , and a class label _y_ are processed as follows: 

_t_ _~~e~~ mb_ = Linear(SiLU(Linear(SinTimeEmb( _t_ )))) _y_ _~~e~~ mb_ = Embedding( _y_ ) _x_ = Linear( _xin_ ) + _t_ _~~e~~ mb_ + _y_ _~~e~~ mb_ 



where SinTimeEmb refers to a sinusoidal time embedding as in (Nichol, 2021; Dhariwal & Nichol, 2021) with a dimension of 128. All Linear layers in Equation 5 have a fixed projection dimension 128. 

**Hyperparameters** in TabDDPM are essential since, in the experiments, we observed them having a strong influence on the model effectiveness. Table 1 lists the main hyperparameters and the search spaces for each of them, which we recommend using. The process of tuning is described in detail in the experimental section. 

3 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Table 1._ The list of main hyperparameters for TabDDPM. 

|Hyperparameter|Search space|
|---|---|
|Learning rate|LogUniform[0_._00001_,_0_._003]|
|Batch size|Cat_{_256_,_4096_}_|
|Diffusion timesteps|Cat_{_100_,_1000_}_|
|Training iterations|Cat_{_5000_,_10000_,_20000_}_|
|# MLP layers|Int_{_2_,_4_,_6_,_8_}_|
|MLP width of layers|Int_{_128_,_256_,_512_,_1024_}_|
|Proportion of samples|Float_{_0_._25_,_0_._5_,_1_,_2_,_4_,_8_}_|
|Dropout|0.0|
|Scheduler|cosine (Nichol,2021)|
|Gaussian diffusion loss|MSE|
|Number of tuning trials|50|



_Table 2._ Details on the datasets used in the evaluation. 

|Abbr|Name|# Train #|Validation|# Test|# Num|# Cat|Task type|
|---|---|---|---|---|---|---|---|
|AB|Abalone|2672|669|836|7|1|Regression|
|AD|Adult|26048|6513|16281|6|8|Binclass|
|BU|Buddy|12053|3014|3767|4|5|Multiclass|
|CA|California Housing|13209|3303|4128|8|0|Regression|
|CAR|Cardio|44800|11200|14000|5|6|Binclass|
|CH|Churn Modeling|6400|1600|2000|7|4|Binclass|
|DE|Default|19200|4800|6000|20|3|Binclass|
|DI|Diabetes|491|123|154|8|0|Binclass|
|FB|Facebook Comm. Vol.|157638|19722|19720|50|1|Regression|
|GE|Gesture Phase|6318|1580|1975|32|0|Multiclass|
|HI|Higgs Small|62751|15688|19610|28|0|Binclass|
|HO|House 16H|14581|3646|4557|16|0|Regression|
|IN|Insurance|856|214|268|3|3|Regression|
|KI|King|13832|3458|4323|17|3|Regression|
|MI|MiniBooNE|83240|20811|26013|50|0|Binclass|
|WI|Wilt|3096|775|968|5|0|Binclass|



### **5. Experiments** 

In this section, we extensively evaluate TabDDPM against existing alternatives. 

**Datasets.** For systematic investigation of the performance of tabular generative models, we consider a diverse set of 15 real-world public datasets. These datasets have various sizes, nature, number of features, and their distributions. Most datasets were previously used for tabular model evaluation in (Zhao et al., 2021; Gorishniy et al., 2021). The full list of datasets and their properties are presented in Table 2. 

**Baselines.** Since the number of generative models proposed for tabular data is enormous, we evaluate TabDDPM only against the leading approaches from each paradigm of generative modeling. Also, we consider only the baselines with the published source code. 

- **TVAE** (Xu et al., 2019) — the state-of-the-art variational auto-encoder for tabular data generation. To the best of our knowledge, there are no alternative VAElike models that outperform TVAE and have public source code. 

- **CTGAN** (Xu et al., 2019) — arguably the most popular and well-known GAN-based model for synthetic data generation. 

- **CTABGAN** (Zhao et al., 2021) — a recent GAN-based model that is shown to outperform the existing tabular GANs on a diverse set of benchmarks. This approach cannot handle regression tasks. 

- **CTABGAN+** (Zhao et al., 2022) — an extension of the **CTABGAN** model that was published in the very recent preprint. We are unaware of the GAN-based model for tabular data proposed after **CTABGAN+** and has a public source code. 

- **SMOTE** (Chawla et al., 2002) — a “shallow” interpolation-based method that ”generates” a synthetic point as a convex combination of a real data point and its _k_ -th nearest neighbor from the dataset. This method was originally proposed for minor class oversampling. Here, we generalize it to synthetic data generation as a simple sanity check, i.e., a new synthetic sample is ”generated” by interpolating two samples from the same class. For regression problems, we split data into two classes by the median of the target variable. 

**Evaluation measure.** Our primary evaluation measure is _machine learning (ML) efficiency_ (or utility) (Xu et al., 2019). In more detail, ML efficiency quantifies the performance of classification or regression models trained on synthetic data and evaluated on the real test set. Intuitively, models trained on high-quality synthetics should be competitive (or even superior) to models trained on real data. In our experiments, we use two evaluation protocols to compute ML efficiency. In the first protocol, which is more common in the literature (Xu et al., 2019; Zhao et al., 2021; Kim et al., 2022), we compute an average efficiency w.r.t. a set of diverse ML models (logistic regression, decision tree, and others). In the second protocol, we evaluate ML efficiency only w.r.t. the CatBoost model (Prokhorenkova et al., 2018), which is arguably the leading GBDT implementation providing state-of-the-art performance on tabular tasks (Gorishniy et al., 2021). In our experiments in subsection 5.2, we show that it is crucial to use the second protocol, while the first one can often be misleading. 

**Tuning process.** To tune the hyperparameters of TabDDPM and the baselines, we use the Optuna library (Akiba et al., 2019). The tuning process is guided by the values of the ML efficiency (w.r.t. Catboost) of the generated synthetic data on a hold-out validation dataset (the score is averaged over five different sampling seeds). The search spaces for all hyperparameters of TabDDPM are reported in Table 1 (for baselines — in Appendix E). Additionally, we demonstrate that tuning the hyperparameters using the CatBoost guidance does not introduce any sort of “Catboost-biasedness”, 

4 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Figure 2._ The individual feature distributions for the real data and the data generated by TabDDPM, CTABGAN+, and TVAE. TabDDPM produces more realistic feature distributions than alternatives in most cases. 



<!-- Start of picture text -->
CA. num_feature №0 BU. cat_feature №0<br>CH. num_feature №3 HI. num_feature №19<br>AD. cat_feature №3 CH. num_feature №4<br>HO. num_feature №15 FB. num_feature №26<br>Real TabDDPM Real CTABGAN+ Real TVAE Real TabDDPM Real CTABGAN+ Real TVAE<br><!-- End of picture text -->

_Figure 3._ Absolute difference between correlation matrices computed on real and synthetic datasets. A more intensive red color indicates a higher difference between the real and synthetic correlation values. In most cases, TabDDPM captures feature correlations better. 



<!-- Start of picture text -->
AB AD BU CA CH HO<br>TabDDPM<br>CTABGAN+<br>TVAE<br><!-- End of picture text -->

and the Catboost-tuned TabDDPM produces synthetics that are also superior for other models, like MLP. These results are reported in Appendix A. 

#### **5.1. Qualitative comparison** 

Here, we qualitatively investigate the ability of TabDDPM to model the individual and joint feature distributions compared with the TVAE and CTABGAN+ baselines. In particular, for each dataset, we produce synthetic datasets from TabDDPM, TVAE, and CTABGAN+ of the same size as 

a real train set in a particular dataset. For classification datasets, each class is sampled according to its proportion in the real dataset. Then, we visualize the typical individual feature distributions for real and synthetic data in Figure 2. For completeness, the features of different types and distributions are presented. 

In most cases, TabDDPM produces more realistic feature distributions compared with TVAE and CTABGAN+. The advantage is more pronounced (1) for numerical features, which are uniformly distributed, (2) for categorical features with high cardinality, and (3) for mixed-type features that combine continuous and discrete distributions. Then, we also visualize the differences between the correlation matrices computed on real and synthetic data for different datasets, see Figure 3. To compute the correlation matrices, we use the Pearson correlation coefficient for numericalnumerical correlations, the correlation ratio for categoricalnumerical cases, and Theil’s U statistic between categorical features. In comparison with CTABGAN+ and TVAE, TabDDPM generates synthetic datasets with more realistic pairwise correlations. These illustrations indicate that our TabDDPM model is more flexible than alternatives and produces superior synthetic data. We also follow (Zhao et al., 2021) and measure the Wasserstein distance between numerical features and the Jensen–Shannon divergence between categorical ones. Additionally, we report an L2 distance between correlation matrices (quantitative results for Fig- 

5 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Table 3._ Average ranks (lower is better) over all datasets in terms of Wasserstein distance (WD) between numerical features, Jensen–Shannon divergence between categorical features and L2 distance between correlation matrices. Distances are calculated between generated data and real data. 

||WD (Num.)|JS (Cat.)|L2 (Corr. matrix)|
|---|---|---|---|
|CTGAN|3.33|4.77|3.47|
|TVAE|4.20|3.92|4.40|
|CTABGAN+|3.87|2.54|3.40|
|SMOTE|**1.67**|2.15|2.00|
|TabDDPM|1.93|**1.62**|**1.73**|



ure 3). The results are presented in Table 3 as an average rank across all datasets (lower is better). Lower rank indicates lower WD, JS divergence and L2 distance. The exact numbers can be found in Appendix B. 

#### **5.2. Machine Learning efficiency** 

In this section, we compare TabDDPM to alternative generative models in terms of machine learning efficiency. From each generative model, we sample a synthetic dataset with the size of a real train set in proportion from Table 1. This synthetic data is then used to train a classification/regression model, which is then evaluated using the real test set. In our experiments, classification performance is evaluated by the F1 score, and regression performance is evaluated by the R2 score. We use two protocols: 

1. First, we compute average ML efficiency for a diverse set of ML models, as performed in previous works (Xu et al., 2019; Zhao et al., 2021; Kim et al., 2022). This set includes Decision Tree, Random Forest, Logistic Regression (or Ridge Regression) and MLP models from the scikit-learn library (Pedregosa et al., 2011) with the default hyperparameters except for: “maxdepth” equals to 28 for Decision Tree and Random Forest, “maximum iterations” equals to 500 for Logistic and Ridge regressions, and “maximum iterations” equals to 100 for MLPs. 

2. Second, we compute ML efficiency w.r.t. the current state-of-the-art model for tabular data. Specifically, we consider CatBoost (Prokhorenkova et al., 2018) and MLP architecture from (Gorishniy et al., 2021) for evaluation. CatBoost and MLP hyperparameters are thoroughly tuned on each dataset using the search spaces from (Gorishniy et al., 2021). We argue that this evaluation protocol demonstrates the practical value of synthetic data more reliably since in most real scenarios practitioners are not interested in using weak and suboptimal classifiers/regressors. 

**Main results.** The ML efficiency values computed by both protocols are presented in Tables 4, 5. The ML efficiency for 

the tuned MLP is reported in Appendix A. To compute each value, we average the results over five random seeds for synthetics generation, and for each generated dataset, we average over ten random seeds for training classifiers/regressors. The key observations are described below: 

- In both evaluation protocols, TabDDPM significantly outperforms TVAE and CTABGAN+ on most datasets, which highlights the advantage of diffusion models for tabular data as well as demonstrated for other domains in prior works. 

- The interpolation-based SMOTE method demonstrates the performance competitive to TabDDPM and often significantly outperforms the GAN/VAE approaches. Interestingly, most of the prior works on generative models for tabular data do not compare against SMOTE, while it appears to be a simple baseline, which is challenging to beat. 

- While many prior works use the first evaluation protocol to compute the ML efficiency, we argue that the second one (which uses the state-of-the-art model) is more appropriate. Tables 4, 5 show that the absolute values of classification/regression performance are much lower for the first protocol, i.e., weak classifiers/regressors are substantially inferior to CatBoost on the considered benchmarks. Therefore, one can hardly use these suboptimal models instead of CatBoost and their performance values are uninformative for practitioners. Moreover, in the first protocol, training on synthetic data is often advantageous compared to training on real data. This creates an impression that the data produced by generative models are more valuable than the real ones. However, it is not the case when one uses the tuned ML model, as in most practical scenarios. Appendix A confirms this observation for the properly tuned MLP model. 

Overall, TabDDPM provides state-of-the-art generative performance and can be used as a source of high-quality synthetic data. Interestingly, in terms of ML efficiency, a simple “shallow” SMOTE method is competitive to TabDDPM, which raises the question if sophisticated deep generative models are needed. In the section below, we provide an affirmative answer to this question. 

#### **5.3. Privacy** 

Here, we investigate TabDDPM in privacy-concerned settings, e.g., sharing the data without disclosure of personal or sensitive information. In these setups, one is interested in high-quality synthetic data that does not reveal the records from the original dataset. 

We measure the privacy of the generated data as a mean Dis- 

6 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Table 4._ The values of machine learning efficiency computed w.r.t. five weak classification/regression models. Negative scores denote negative R2, which means that performance is worse than an optimal constant prediction. 

||AB (_R_2)|AD (_F_1)|BU (_F_1)|CA (_R_2)|CAR (_F_1)|CH (_F_1)|DE (_F_1)|DI (_F_1)|
|---|---|---|---|---|---|---|---|---|
|TVAE|0_._238_±._012|0_._742_±._001|0_._779_±._004|_−_13_._0_±_1_._51|0_._693_±._002|0_._684_±._003|0_._643_±._003|0_._712_±._010|
|CTABGAN|–|0_._737_±._007|0_._786_±._008|–|0_._684_±._003|0_._636_±._010|0_._614_±._007|0_._655_±._015|
|CTABGAN+|0_._316_±._024|0_._730_±._007|0_._837_±._006|_−_7_._59_±._645|**0**_._**708**_±._**002**|0_._650_±._008|0_._648_±._008|**0**_._**727**_±._**023**|
|SMOTE|**0**_._**400**_±._**009**|0_._750_±._004|0_._842_±._003|0_._667_±._006|0_._693_±._001|0_._690_±._003|0_._649_±._003|0_._677_±._013|
|TabDDPM|**0**_._**392**_±._**009**|**0**_._**758**_±._**005**|**0**_._**851**_±._**003**|**0**_._**695**_±._**002**|0_._696_±._001|**0**_._**693**_±._**003**|**0**_._**659**_±._**003**|0_._675_±._011|
|Real|0_._423_±._009|0_._750_±._006|0_._845_±._004|0_._663_±._002|0_._683_±._002|0_._679_±._003|0_._648_±._003|0_._699_±._012|
||FB (_R_2)|GE (_F_1)|HI (_F_1)|HO (_R_2)|IN (_R_2)|KI (_R_2)|MI (_F_1)|WI (_F_1)|
|TVAE|_≪_0|0_._372_±._006|0_._590_±._004|0_._174_±._012|0_._470_±._024|0_._666_±._006|**0**_._**880**_±._**002**|0_._497_±._001|
|CTABGAN|–|0_._339_±._009|0_._539_±._006|–|–|–|0_._856_±._003|0_._656_±._011|
|CTABGAN+|_≪_0|0_._373_±._009|0_._598_±._004|0_._222_±._042|0_._669_±._018|0_._197_±._051|0_._867_±._002|0_._653_±._027|
|SMOTE|**0**_._**651**_±._**002**|**0**_._**478**_±._**005**|0_._664_±._003|0_._394_±._006|0_._709_±._008|**0**_._**751**_±._**005**|0_._860_±._001|**0**_._**793**_±._**004**|
|TabDDPM|0_._527_±._005|0_._462_±._005|**0**_._**670**_±._**002**|**0**_._**426**_±._**007**|**0**_._**734**_±._**007**|0_._611_±._013|0_._850_±._004|**0**_._**792**_±._**004**|
|Real|0_._645_±._005|0_._431_±._005|0_._663_±._002|0_._415_±._007|0_._708_±._007|0_._768_±._013|0_._850_±._004|0_._684_±._004|



_Table 5._ The values of machine learning efficiency computed w.r.t. the state-of-the-art tuned CatBoost model. 

||AB (_R_2)|AD (_F_1)|BU (_F_1)|CA (_R_2)|CAR (_F_1)|CH (_F_1)|DE (_F_1)|DI (_F_1)|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._420_±._004|0_._789_±._001|0_._867_±._003|0_._686_±._003|0_._730_±._001|0_._723_±._006|**0**_._**699**_±._**002**|0_._459_±._096|
|TVAE|0_._433_±._008|0_._781_±._002|0_._864_±._005|0_._752_±._001|0_._717_±._001|0_._732_±._006|0_._656_±._007|**0**_._**714**_±._**039**|
|CTABGAN|–|0_._783_±._002|0_._855_±._005|–|0_._717_±._001|0_._688_±._006|0_._644_±._011|**0**_._**731**_±._**022**|
|CTABGAN+|0_._467_±._004|0_._772_±._003|0_._884_±._005|0_._525_±._004|0_._733_±._001|0_._702_±._012|0_._686_±._004|**0**_._**734**_±._**020**|
|SMOTE|**0**_._**549**_±._**005**|0_._791_±._002|0_._891_±._003|**0**_._**840**_±._**001**|0_._732_±._001|0_._743_±._005|0_._693_±._003|0_._683_±._037|
|TabDDPM|**0**_._**550**_±._**010**|**0**_._**795**_±._**001**|**0**_._**906**_±._**003**|0_._836_±._002|**0**_._**737**_±._**001**|**0**_._**755**_±._**006**|0_._691_±._004|**0**_._**740**_±._**020**|
|Real|0_._556_±._004|0_._815_±._002|0_._906_±._002|0_._857_±._001|0_._738_±._001|0_._740_±._009|0_._688_±._003|0_._785_±._013|
||FB (_R_2)|GE (_F_1)|HI (_F_1)|HO (_R_2)|IN (_R_2)|KI (_R_2)|MI (_F_1)|WI (_F_1)|
|CTGAN|0_._443_±._005|0_._333_±._013|0_._575_±._006|0_._433_±._005|0_._745_±._009|0_._772_±._005|0_._783_±._005|0_._749_±._015|
|TVAE|0_._685_±._003|0_._434_±._006|0_._638_±._003|0_._493_±._006|0_._784_±._010|0_._824_±._003|0_._912_±._001|0_._501_±._012|
|CTABGAN|–|0_._392_±._006|0_._575_±._004|–|–|–|0_._889_±._002|**0**_._**906**_±._**019**|
|CTABGAN+|0_._509_±._011|0_._406_±._009|0_._664_±._002|0_._504_±._005|0_._797_±._005|0_._444_±._014|0_._892_±._002|0_._798_±._021|
|SMOTE|**0**_._**803**_±._**002**|**0**_._**658**_±._**007**|**0**_._**722**_±._**001**|0_._662_±._004|**0**_._**812**_±._**002**|**0**_._**842**_±._**004**|0_._932_±._001|**0**_._**913**_±._**007**|
|TabDDPM|0_._713_±._002|0_._597_±._006|**0**_._**722**_±._**001**|**0**_._**677**_±._**010**|0_._809_±._002|**0**_._**833**_±._**014**|**0**_._**936**_±._**001**|**0**_._**904**_±._**009**|
|Real|0_._837_±._001|0_._636_±._007|0_._724_±._001|0_._662_±._003|0_._814_±._001|0_._907_±._002|0_._934_±._000|0_._898_±._006|



tance to Closest Record (DCR) (Zhao et al., 2021). Specifically, for each synthetic sample, we get the minimum L2 distance to the real records. Mean DCR averages these distances over all generated samples. 

Low DCR values indicate that synthetic samples essentially mimic some real datapoints and can violate privacy requirements. Higher DCR values denote that the generative model can produce “new” records rather than just near duplicates of the real data. Note that out-of-distribution data, e.g., random noise, will also provide high DCR. Therefore, DCR needs to be considered along with ML efficiency together. 

Table 7 presents the DCR values for TabDDPM, SMOTE, CTABGAN+ and TVAE. We observe that TabDDPM is more private than SMOTE and less private than GAN/VAE alternatives. We attribute this to significantly lower ML utility of GAN/VAE-based baselines. 

Since SMOTE computes convex combinations of the real records, the original DCR measure can pessimize SMOTE’s privacy. To address this issue, we pretrain an MLP model on each dataset using real data. Then, we use this model to extract features from synthetic data and measure DCR in the latent space of the pretrained model. Table 14 provides mean DCR values on MLP features. The results are mostly consistent with Table 7 and do not alter our conclusions. 

We also visualize histograms of the minimal synthetic-toreal distances in Figure 4. For SMOTE, most distance values are concentrated around zero, while TabDDPM samples are noticeably farther from real datapoints. 

In addition, following (Chen et al., 2020a; Lee et al., 2021), we measure a success rate of a full black-box privacy attack (see Table 6). The attack aims to infer whether a record belongs to its original training data. The results show that 

7 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

TabDDPM is more resistant to this full black-box attack than SMOTE. All these experiments confirm that TabDDPM significantly outperforms SMOTE in privacy-concerned scenarios and still provides state-of-the-art ML efficiency. 

_Figure 4._ Histograms of minimal synthetic-to-real distances for TabDDPM and SMOTE. SMOTE values are concentrated around zero and, thus, SMOTE generates less private synthetic data. 



<!-- Start of picture text -->
AB DI<br>TabDDPM<br>SMOTE<br>CA CH<br>HO BU<br>HI IN<br><!-- End of picture text -->

### **Limitations and discussion** 

The proposed method does not pretend to be an all-in-one solution providing high privacy and high ML utility. Our experiments show that TabDDPM is more private than “shallow” SMOTE but do not give a definite answer if TabDDPM’s data can satisfy real-world privacy-concerned applications. Therefore, the privacy problem of the DDPMproduced data needs to be further investigated. Moreover, DCR, used in this paper, is not an ultimate privacy measure and does not cover some critical use cases. For example, the L2 distance between records does not consider the importance of individual features and cannot detect leakage if some sensitive features coincide. 

Also, in our work, we process categorical features using multinomial diffusion. However, alternative approaches exist, e.g., (Chen et al., 2022; Campbell et al., 2022; Zheng & Charoenphakdee, 2022). Each of these techniques is applicable to TabDDPM and can be an interesting direction to 

_Table 6._ Success rate of a full black-box privacy attack in terms of ROCAUC. A higher score indicates the higher success of attack. TabDDPM is significantly more robust than SMOTE. 

||SMOTE|TabDDPM|
|---|---|---|
|AB<br>|0_._967<br>|0_._505<br>|
|AD|0_._619|0_._511|
|BU|0_._710|0_._569|
|CA|0_._986|0_._516|
|CAR|0_._721|0_._506|
|CH|0_._891|0_._721|
|DE|0_._679|0_._497|
|DI|0_._610|0_._510|
|GE|0_._864|0_._533|
|HI|0_._999|0_._527|
|HO|0_._826|0_._546|
|IN|0_._712|0_._868|
|KI|0_._748|0_._517|
|MI|0_._990|0_._500|
|WI|0_._954|0_._516|



_Table 7._ Comparison in terms of mean Distance to Closest Record (DCR) (higher is better). TabDDPM provides better DCR values compared with SMOTE but underperforms compared with TVAE and CTABGAN+. We attribute this to significantly lower ML efficiency of GAN/VAE-based alternatives. 

||AB|AD|BU|CA|CAR|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|TVAE|0_._088|0_._220|0_._226|0_._056|0_._010|0_._241|0_._096|0_._146|
|CTABGAN+|0_._081|0_._400|0_._242|0_._070|0_._020|0_._235|0_._131|0_._204|
|SMOTE|0_._018|0_._082|0_._080|0_._016|0_._007|0_._099|0_._054|0_._074|
|TabDDPM|0_._061|0_._295|0_._168|0_._045|0_._016|0_._166|0_._061|0_._308|
||FB|GE|HI|HO|IN|KI|MI|WI|
|TVAE|1_._418|0_._171|0_._497|0_._127|0_._102|0_._200|0_._025|0_._020|
|CTABGAN+|0_._666|0_._169|0_._533|0_._129|0_._124|0_._390|10_._761|0_._027|
|SMOTE|0_._264|0_._041|0_._209|0_._066|0_._050|0_._090|0_._012|0_._009|
|TabDDPM|0_._785|0_._076|0_._473|0_._096|0_._050|0_._252|0_._574|0_._023|



investigate. As for numerical features, the possible extension of TabDDPM can be inspired by (Nazabal et al., 2020) that distinguish different types of numerical variables, i.e., real-valued, positive real-valued or ordinal. 

### **6. Conclusion** 

In this paper, we have investigated the prospect of the diffusion modeling framework in the field of tabular data. In particular, we describe the DDPM design that can handle mixed data types consisting of numerical and categorical features. For the most considered benchmarks, the synthetic data produced by TabDDPM has consistently higher quality compared with the GAN/VAE-based rivals. Interestingly, shallow interpolation techniques like SMOTE have demonstrated competitive ML utility and need to be considered as a simple yet effective baseline. Nevertheless, TabDDPM outperforms SMOTE for the setups where the privacy of the data must be ensured. 

8 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

### **References** 

- Akiba, T., Sano, S., Yanase, T., Ohta, T., and Koyama, M. Optuna: A next-generation hyperparameter optimization framework. In _Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining_ , pp. 2623–2631, 2019. 

- Austin, J., Johnson, D. D., Ho, J., Tarlow, D., and van den Berg, R. Structured denoising diffusion models in discrete state-spaces. _Advances in Neural Information Processing Systems_ , 34:17981–17993, 2021. 

- Baldi, P., Sadowski, P., and Whiteson, D. Searching for exotic particles in high-energy physics with deep learning. _Nature Communications_ , 5, 2014. 

- Baranchuk, D., Rubachev, I., Voynov, A., Khrulkov, V., and Babenko, A. Label-efficient semantic segmentation with diffusion models. _arXiv preprint arXiv:2112.03126_ , 2021. 

- Camino, R. D., Hammerschmidt, C. A., et al. Oversampling tabular data with deep generative models: Is it worth the effort? 2020. 

- Campbell, A., Benton, J., De Bortoli, V., Rainforth, T., Deligiannidis, G., and Doucet, A. A continuous time framework for discrete denoising models. _Advances in Neural Information Processing Systems_ , 35:28266–28279, 2022. 

- Chawla, N. V., Bowyer, K. W., Hall, L. O., and Kegelmeyer, W. P. Smote: synthetic minority over-sampling technique. _Journal of artificial intelligence research_ , 16:321–357, 2002. 

- Chen, D., Yu, N., Zhang, Y., and Fritz, M. Gan-leaks: A taxonomy of membership inference attacks against generative models. In _Proceedings of the 2020 ACM SIGSAC conference on computer and communications security_ , pp. 343–362, 2020a. 

- Chen, N., Zhang, Y., Zen, H., Weiss, R. J., Norouzi, M., and Chan, W. Wavegrad: Estimating gradients for waveform generation. _arXiv preprint arXiv:2009.00713_ , 2020b. 

- Chen, T., Zhang, R., and Hinton, G. Analog bits: Generating discrete data using diffusion models with selfconditioning. _arXiv preprint arXiv:2208.04202_ , 2022. 

- Dhariwal, P. and Nichol, A. Diffusion models beat gans on image synthesis. 2021. 

- Engelmann, J. and Lessmann, S. Conditional wasserstein gan-based oversampling of tabular data for imbalanced learning. _Expert Systems with Applications_ , 174:114582, 2021. 

- Fan, J., Liu, T., Li, G., Chen, J., Shen, Y., and Du, X. Relational data synthesis using generative adversarial networks: A design space exploration. _arXiv preprint arXiv:2008.12763_ , 2020. 

- Gorishniy, Y., Rubachev, I., Khrulkov, V., and Babenko, A. Revisiting deep learning models for tabular data. _Advances in Neural Information Processing Systems_ , 34: 18932–18943, 2021. 

- Ho, J., Jain, A., and Abbeel, P. Denoising diffusion probabilistic models. 2020. 

- Hoogeboom, E., Nielsen, D., Jaini, P., Forre, P., and Welling,´ M. Argmax flows and multinomial diffusion: Learning categorical distributions. _Advances in Neural Information Processing Systems_ , 34:12454–12465, 2021. 

- Hoogeboom, E., Satorras, V. G., Vignac, C., and Welling, M. Equivariant diffusion for molecule generation in 3d. In _International Conference on Machine Learning_ , pp. 8867–8887. PMLR, 2022. 

- Jing, B., Corso, G., Chang, J., Barzilay, R., and Jaakkola, T. Torsional diffusion for molecular conformer generation. _arXiv preprint arXiv:2206.01729_ , 2022. 

- Jordon, J., Yoon, J., and Van Der Schaar, M. Pate-gan: Generating synthetic data with differential privacy guarantees. In _International conference on learning representations_ , 2018. 

- Kelley Pace, R. and Barry, R. Sparse spatial autoregressions. _Statistics & Probability Letters_ , 33(3):291–297, 1997. 

- Kim, J., Jeon, J., Lee, J., Hyeong, J., and Park, N. Oct-gan: Neural ode-based conditional tabular gans. In _Proceedings of the Web Conference 2021_ , pp. 1506–1515, 2021. 

- Kim, J., Lee, C., Shin, Y., Park, S., Kim, M., Park, N., and Cho, J. Sos: Score-based oversampling for tabular data. In _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , pp. 762–772, 2022. 

- Kohavi, R. Scaling up the accuracy of naive-bayes classifiers: a decision-tree hybrid. In _KDD_ , 1996. 

- Kong, Z., Ping, W., Huang, J., Zhao, K., and Catanzaro, B. Diffwave: A versatile diffusion model for audio synthesis. _arXiv preprint arXiv:2009.09761_ , 2020. 

- Lee, J., Hyeong, J., Jeon, J., Park, N., and Cho, J. Invertible tabular gans: Killing two birds with one stone for tabular data synthesis. _Advances in Neural Information Processing Systems_ , 34:4263–4273, 2021. 

9 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

- Li, H., Yang, Y., Chang, M., Feng, H., Xu, Z., Li, Q., and Chen, Y. Srdiff: Single image super-resolution with diffusion probabilistic models. 2021. 

- Li, X. L., Thickstun, J., Gulrajani, I., Liang, P., and Hashimoto, T. B. Diffusion-lm improves controllable text generation. _arXiv preprint arXiv:2205.14217_ , 2022. 

- Madeo, R. C. B., Lima, C. A. M., and Peres, S. M. Gesture unit segmentation using support vector machines: segmenting gestures from rest positions. In _Proceedings of the 28th Annual ACM Symposium on Applied Computing, SAC_ , 2013. 

- Meng, C., Song, Y., Song, J., Wu, J., Zhu, J.-Y., and Ermon, S. Sdedit: Image synthesis and editing with stochastic differential equations. 2021. 

- Naeem, M. F., Oh, S. J., Uh, Y., Choi, Y., and Yoo, J. Reliable fidelity and diversity metrics for generative models. In _International Conference on Machine Learning_ , pp. 7176–7185. PMLR, 2020. 

- Nazabal, A., Olmos, P. M., Ghahramani, Z., and Valera, I. Handling incomplete heterogeneous data using vaes. _Pattern Recognition_ , 107:107501, 2020. 

- Nichol, Alex & Dhariwal, P. Improved denoising diffusion probabilistic models. _ICML_ , 2021. 

- Nock, R. and Guillame-Bert, M. Generative trees: Adversarial and copycat. _ICML_ , 2022. 

- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., and Duchesnay, E. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. 

- Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., and Gulin, A. Catboost: unbiased boosting with categorical features. _Advances in neural information processing systems_ , 31, 2018. 

- Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and Ommer, B. High-resolution image synthesis with latent diffusion models. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 10684–10695, 2022. 

- Saharia, C., Ho, J., Chan, W., Salimans, T., Fleet, D. J., and Norouzi, M. Image super-resolution via iterative refinement. 2021. 

- Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., Ghasemipour, S. K. S., Ayan, B. K., Mahdavi, S. S., Lopes, R. G., et al. Photorealistic text-to-image diffusion 

models with deep language understanding. _arXiv preprint arXiv:2205.11487_ , 2022. 

- Singh, K., Sandhu, R. K., and Kumar, D. Comment volume prediction using neural networks and decision trees. In _IEEE UKSim-AMSS 17th International Conference on Computer Modelling and Simulation, UKSim_ , 2015. 

- Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., and Ganguli, S. Deep unsupervised learning using nonequilibrium thermodynamics. In _ICML_ , 2015. 

- Song, Y. and Ermon, S. Generative modeling by estimating gradients of the data distribution. In _NeurIPS_ , 2019. 

- Song, Y. and Ermon, S. Improved techniques for training score-based generative models. _NeurIPS_ , 2020. 

- Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., and Poole, B. Score-based generative modeling through stochastic differential equations. 2021. 

- Tashiro, Y., Song, J., Song, Y., and Ermon, S. Csdi: Conditional score-based diffusion models for probabilistic time series imputation. _Advances in Neural Information Processing Systems_ , 34:24804–24816, 2021. 

- Torfi, A., Fox, E. A., and Reddy, C. K. Differentially private synthetic medical data generation using convolutional gans. _Information Sciences_ , 586:485–500, 2022. 

- Vanschoren, J., van Rijn, J. N., Bischl, B., and Torgo, L. Openml: networked science in machine learning. _arXiv_ , 1407.7722v1, 2014. 

- Wen, B., Cao, Y., Yang, F., Subbalakshmi, K., and Chandramouli, R. Causal-tgan: Modeling tabular data using causally-aware gan. In _ICLR Workshop on Deep Generative Models for Highly Structured Data_ , 2022. 

- Xu, L., Skoularidou, M., Cuesta-Infante, A., and Veeramachaneni, K. Modeling tabular data using conditional gan. _Advances in Neural Information Processing Systems_ , 32, 2019. 

- Zhang, Y., Zaidi, N. A., Zhou, J., and Li, G. Ganblr: a tabular data generation model. In _2021 IEEE International Conference on Data Mining (ICDM)_ , pp. 181–190. IEEE, 2021. 

- Zhao, Z., Kunar, A., Birke, R., and Chen, L. Y. Ctab-gan: Effective table data synthesizing. In _Asian Conference on Machine Learning_ , pp. 97–112. PMLR, 2021. 

- Zhao, Z., Kunar, A., Birke, R., and Chen, L. Y. Ctabgan+: Enhancing tabular data synthesis. _arXiv preprint arXiv:2204.00401_ , 2022. 

- Zheng, S. and Charoenphakdee, N. Diffusion models for missing value imputation in tabular data. _arXiv preprint arXiv:2210.17128_ , 2022. 

10 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

# **Appendix** 

### **A. MLP evaluation and tuning** 

Here, we show that tuning the hyperparameters using the CatBoost guidance results in the TabDDPM models that produce synthetics that is also optimal for other classifiers/regressors. The results for a subset of datasets are presented on Table 8. The methods denoted with ”-CB” and ”-MLP” denote the CatBoost guidance and different types of evaluation (CatBoost and MLP, respectively). The ”-MLP-tune” suffix stands for the MLP guidance tuning and MLP evaluation. 

_Table 8._ ML utility score with MLP evaluation and MLP tuning compared with CatBoost evaluation and CatBoost tuning. The table shows that tuning with CatBoost model provides useful synthetic for MLP. 

||AB(_R_2)|AD(_F_1)|BU(_F_1)|CA(_R_2)|CAR(_F_1)|CH(_F_1)|DE(_F_1)|DI(_F_1)|
|---|---|---|---|---|---|---|---|---|
|TabDDPM-CB<br>Real-CB|0_._550_±._010<br>0_._556_±._004|0_._795_±._001<br>0_._815_±._002|0_._906_±._003<br>0_._906_±._002|0_._836_±._002<br>0_._857_±._001|0_._737_±._001<br>0_._738_±._001|0_._755_±._006<br>0_._740_±._009|0_._691_±._004<br>0_._688_±._003|0_._740_±._020<br>0_._785_±._013|
|TabDDPM-MLP<br>Real-MLP|0_._569_±._010<br>0_._581_±._005|0_._794_±._002<br>0_._795_±._001|0_._903_±._003<br>0_._905_±._003|0_._809_±._003<br>0_._808_±._002|0_._737_±._001<br>0_._739_±._001|0_._750_±._005<br>0_._741_±._006|0_._679_±._008<br>0_._688_±._004|0_._754_±._020<br>0_._754_±._017|
|TabDDPM-MLP-tune|0_._559_±._009|0_._792_±._002|0_._901_±._003|0_._803_±._004|0_._737_±._001|0_._749_±._006|0_._674_±._013|0_._741_±._018|
||FB(_R_2)|GE(_F_1)|HI(_F_1)|HO(_R_2)|IN(_R_2)|KI(_R_2)|MI(_F_1)|WI(_F_1)|
|TabDDPM-CB<br>Real-CB|0_._713_±._002<br>0_._837_±._001|0_._597_±._006<br>0_._636_±._007|0_._722_±._001<br>0_._724_±._001|0_._677_±._010<br>0_._662_±._003|0_._809_±._002<br>0_._814_±._001|0_._833_±._014<br>0_._907_±._002|0_._936_±._001<br>0_._934_±._000|0_._904_±._009<br>0_._898_±._006|
|TabDDPM-MLP|–|0_._595_±._006|0_._717_±._002|0_._643_±._010|0_._794_±._008|0_._804_±._015|0_._938_±._001|0_._921_±._006|
|Real-MLP|–|0_._607_±._007|0_._717_±._002|0_._614_±._006|0_._800_±._003|0_._882_±._004|0_._936_±._001|0_._905_±._006|
|TabDDPM-MLP-tune|–|–|–|0_._626_±._009|0_._800_±._004|0_._799_±._018|–|0_._914_±._006|



### **B. Additional results** 

Here, we follow (Zhao et al., 2021) and provide an additional quantitative comparison that shows how well individual feature distributions are modeled (Table 9, Table 10, Table 11). Also, we include density and coverage metrics from (Naeem et al., 2020) that are improved alternatives of precision and recall, respectively (Table 12, Table 13). 

_Table 9._ Wasserstein distance between numerical features. 

||AB|AD|BU|CA|CAR|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._008|0_._010|0_._015|0_._004|0_._004|0_._009|0_._004|0_._085|
|TVAE|0_._020|0_._016|0_._039|0_._007|0_._027|0_._049|0_._009|0_._044|
|CTABGAN+|0_._008|0_._011|0_._016|0_._019|0_._003|0_._046|0_._022|0_._016|
|SMOTE|**0**_._**002**|0_._003|0_._005|**0**_._**002**|0_._001|0_._006|**0**_._**002**|0_._020|
|TabDDPM|0_._005|**0**_._**002**|**0**_._**003**|**0**_._**002**|**0**_._**000**|**0**_._**005**|0_._012|**0**_._**008**|
||FB|GE|HI|HO|IN|KI|MI|WI|
|CTGAN|0_._004|0_._010|**0**_._**003**|0_._005|0_._021|0_._022|0_._004|0_._013|
|TVAE|0_._008|0_._009|0_._076|0_._007|0_._025|0_._012|0_._004|0_._016|
|CTABGAN+|0_._078|0_._007|0_._052|0_._008|0_._025|0_._021|0_._006|0_._006|
|SMOTE|**0**_._**000**|**0**_._**004**|0_._009|0_._005|0_._011|**0**_._**004**|**0**_._**000**|**0**_._**002**|
|TabDDPM|0_._089|0_._011|0_._003|**0**_._**004**|**0**_._**006**|0_._014|0_._001|**0**_._**002**|



11 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Table 10._ Jensen-Shannon divergence between categorical features. 

||AB|AD|BU|CA|CA|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._276|0_._085|0_._168|_nan_|0_._076|0_._039|0_._120|_nan_|
|TVAE|0_._027|0_._095|0_._072|_nan_|0_._181|0_._019|0_._157|_nan_|
|CTABGAN+|0_._035|0_._052|0_._037|_nan_|**0**_._**009**|0_._018|0_._030|_nan_|
|SMOTE|**0**_._**005**|0_._074|0_._072|_nan_|0_._069|0_._030|0_._058|_nan_|
|TabDDPM|0_._007|**0**_._**019**|**0**_._**026**|_nan_|0_._011|**0**_._**017**|**0**_._**009**|_nan_|
||FB|GE|HI|HO|IN|KI|MI|WI|
|CTGAN|**0**_._**017**|_nan_|_nan_|_nan_|0_._071|0_._296|_nan_|_nan_|
|TVAE|0_._246|_nan_|_nan_|_nan_|0_._033|0_._098|_nan_|_nan_|
|CTABGAN+|0_._051|_nan_|_nan_|_nan_|0_._023|**0**_._**044**|_nan_|_nan_|
|SMOTE|0_._027|_nan_|_nan_|_nan_|0_._013|0_._102|_nan_|_nan_|
|TabDDPM|0_._046|_nan_|_nan_|_nan_|**0**_._**008**|0_._060|_nan_|_nan_|



_Table 11._ L2 distance between correlation matrices. 

||AB|AD|BU|CA|CA|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._471|0_._390|0_._492|0_._606|0_._712|0_._239|1_._355|1_._735|
|TVAE|0_._517|0_._636|0_._569|0_._753|2_._437|0_._564|1_._965|0_._736|
|CTABGAN+|0_._283|0_._576|0_._164|0_._749|0_._738|0_._727|1_._496|**0**_._**435**|
|SMOTE|**0**_._**185**|0_._482|0_._245|0_._127|0_._599|**0**_._**147**|**0**_._**642**|0_._838|
|TabDDPM|0_._333|**0**_._**133**|**0**_._**068**|**0**_._**090**|**0**_._**202**|0_._161|0_._934|0_._186|
||FB|GE|HI|HO|IN|KI|MI|WI|
|CTGAN|5_._651|5_._301|1_._413|0_._742|0_._196|1_._530|43_._815|0_._538|
|TVAE|5_._960|2_._996|2_._759|0_._902|0_._224|1_._004|44_._692|0_._550|
|CTABGAN+|6_._782|1_._977|1_._241|0_._978|0_._207|3_._898|31_._704|0_._319|
|SMOTE|**1**_._**596**|**0**_._**560**|0_._354|0_._452|0_._301|**0**_._**569**|**0**_._**258**|**0**_._**059**|
|TabDDPM|16_._120|1_._192|**0**_._**233**|**0**_._**336**|**0**_._**077**|3_._623|9_._185|0_._375|



_Table 12._ Density of synthetic data. 

||AB|AD|BU|CA|CA|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._224|0_._708|0_._780|0_._586|0_._938|0_._865|0_._698|0_._238|
|TVAE|0_._347|1_._126|1_._032|0_._746|0_._845|1_._043|0_._808|**1**_._**565**|
|CTABGAN+|0_._380|0_._867|0_._998|0_._569|0_._957|0_._974|0_._730|0_._974|
|SMOTE|**1**_._**389**|**1**_._**415**|**1**_._**226**|**1**_._**329**|**1**_._**200**|**1**_._**238**|**1**_._**282**|1_._413|
|TabDDPM|0_._904|1_._008|1_._116|1_._027|1_._011|1_._148|0_._810|0_._831|
||FB|GE|HI|HO|IN|KI|MI|WI|
|CTGAN|0_._147|0_._035|0_._702|0_._467|0_._927|0_._719|0_._361|0_._763|
|TVAE|0_._005|0_._248|0_._960|0_._604|1_._072|0_._868|0_._747|0_._919|
|CTABGAN+|0_._187|0_._448|0_._730|0_._565|1_._052|0_._186|0_._110|0_._831|
|SMOTE|**0**_._**926**|**1**_._**531**|**1**_._**682**|**1**_._**595**|**1**_._**213**|**1**_._**335**|**1**_._**308**|**1**_._**251**|
|TabDDPM|0_._633|1_._460|1_._152|1_._195|1_._150|0_._884|0_._972|1_._009|



_Table 13._ Coverage of synthetic data. 

||AB|AD|BU|CA|CA|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|CTGAN|0_._654|0_._948|0_._966|0_._759|0_._920|1_._000|0_._777|0_._572|
|TVAE|0_._769|0_._886|0_._585|0_._922|0_._208|0_._991|0_._672|0_._978|
|CTABGAN+|0_._960|0_._951|0_._999|0_._459|0_._960|0_._830|0_._841|**1**_._**000**|
|SMOTE|**1**_._**000**|0_._970|0_._968|**1**_._**000**|0_._866|1_._000|0_._962|0_._841|
|TabDDPM|**1**_._**000**|**0**_._**994**|**1**_._**000**|0_._998|**0**_._**978**|**1**_._**000**|**0**_._**967**|0_._955|
||FB|GE|HI|HO|IN|KI|MI|WI|
|CTGAN|0_._238|0_._029|0_._871|0_._839|0_._986|0_._739|0_._576|0_._986|
|TVAE|0_._014|0_._669|0_._255|0_._875|0_._987|0_._874|0_._823|0_._867|
|CTABGAN+|0_._222|0_._640|0_._557|0_._952|**1**_._**000**|0_._479|0_._241|0_._994|
|SMOTE|**0**_._**928**|**1**_._**000**|**0**_._**999**|**1**_._**000**|0_._995|0_._945|**0**_._**991**|**1**_._**000**|
|TabDDPM|0_._782|0_._997|0_._980|**1**_._**000**|**1**_._**000**|**0**_._**969**|0_._956|**1**_._**000**|



12 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

### **C. Additional visualizations** 

_Figure 5._ The individual feature distributions for the real data and the data generated by TabDDPM, CTABGAN+, and TVAE. TabDDPM often models feature distributions more accurately than CTABGAN+ and TVAE. 



<!-- Start of picture text -->
AD. num_feature №1 AB. num_feature №0<br>CH. cat_feature №1 HI. num_feature №0<br>CAR. cat_feature №1 KI. num_feature №0<br>CAR. num_feature №0 GE. num_feature №5<br>WI. num_feature №0 DE. num_feature №2<br>Real TabDDPM Real CTABGAN+ Real TVAE Real TabDDPM Real CTABGAN+ Real TVAE<br><!-- End of picture text -->

_Figure 6._ The absolute difference between correlation matrices computed on real and synthetic datasets. More intense red color indicates higher difference. Overall, TabDDPM captures correlations better. 



<!-- Start of picture text -->
DI GE HI IN MI WI<br>TabDDPM<br>CTABGAN+<br>TVAE<br><!-- End of picture text -->

13 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

### **D. Distance to Closest Record using pretrained MLP features** 

This section addresses the problem that DCR in the original feature space can be an unsuitable privacy measure for SMOTE. We pretrain the feature extractor on each dataset and compute DCR in the latent space of the MLP model. According to the results in Table 14, DCR calculated on MLP features brings similar conclusions to Table 7. SMOTE still significantly underperforms compared with TabDDPM. 

_Table 14._ Comparison in terms of mean Distance to Closest Record (DCR) calculated on pretrained MLP features (higher is better). The results are consistent with Table 7. 

||AB|AD|BU|CA|CAR|CH|DE|DI|
|---|---|---|---|---|---|---|---|---|
|TVAE|0_._282|1_._055|0_._381|0_._373|0_._173|2_._869|0_._271|0_._508|
|CTABGAN+|0_._257|1_._466|0_._382|0_._332|0_._177|2_._998|0_._366|0_._669|
|SMOTE|0_._081|0_._526|0_._216|0_._200|0_._147|1_._367|0_._172|0_._409|
|TabDDPM|0_._195|1_._246|0_._330|0_._290|0_._160|2_._240|0_._168|1_._232|
||FB|GE|HI|HO|IN|KI|MI|WI|
|TVAE|3_._642|5_._484|3_._256|0_._393|0_._276|0_._513|0_._449|0_._45|
|CTABGAN+|11_._44|5_._375|4_._396|0_._365|0_._305|0_._833|12_._026|0_._76|
|SMOTE|1_._045|1_._673|2_._657|0_._332|0_._162|0_._294|0_._374|0_._377|
|TabDDPM|30_._46|3_._85|3_._557|0_._336|0_._172|0_._889|7_._993|0_._620|



### **E. Hyperparameters Search Spaces** 

_Table 15._ CatBoost hyperparameters space from (Gorishniy et al., 2021) 

|Parameter|Distribution|
|---|---|
|Max depth|UniformInt[3_,_10]|
|Learning rate|LogUniform[1_e_-5_,_1]|
|Bagging temperature|Uniform[0_,_1]|
|L2 leaf reg|LogUniform[1_,_10]|
|Leaf estimation iterations|UniformInt[1_,_10]|
|Number of tuning trials|100|



_Table 16._ MLP hyperparameters space from (Gorishniy et al., 2021) 

|Parameter|Distribution|
|---|---|
|# Layers|UniformInt[1_,_8]|
|Layer size|Int_{_64_,_128_,_256_,_512_,_1024_}_|
|Dropout|_{_0_,_Uniform[0_,_0_._5]_}_|
|Learning rate|LogUniform[1_e_-5_,_1_e_-2]|
|Weight decay|_{_0_,_LogUniform[1_e_-6_,_1_e_-3]_}_|
|Number of tuning trials|100|



_Table 17._ SMOTE hyperparameters search space. _λrange_ denotes the range of interpolation coefficient to sample from 

|Parameter|Distribution|
|---|---|
|k<br>~~n~~eighbours|Int[5_,_20]|
|_λrange_|Float[0_,_1]|
|Proportion of samples|Float_{_0_._25_,_0_._5_,_1_,_2_,_4_,_8_}_|
|Number of tuning trials|50|



4https://github.com/Team-TUD/CTAB-GAN-Plus 

4https://github.com/sdv-dev/CTGAN 

14 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

_Table 18._ CTABGAN and CTABGAN+ hyperparameters search space. See an official implementation<sup>2</sup> 

|Parameter|Distribution|
|---|---|
|# claassif. layers|UniformInt[1_,_4]|
|Classif. layer size|Int_{_64_,_128_,_256_}_|
|Training iterations|Cat_{_1000_,_5000_,_10000_}_|
|Batch Size|Int_{_512_,_1024_,_2048_}_|
|random<br>~~d~~im|Int_{_16_,_32_,_64_,_128_}_|
|num<br>~~c~~hannels|Int_{_16_,_32_,_64_}_|
|Proportion of samples|Float_{_0_._25_,_0_._5_,_1_,_2_,_4_,_8_}_|
|Number of tuning trials|35|



_Table 19._ TVAE hyperparameters search space. See an official implementation<sup>4</sup> 

|Parameter|Distribution|
|---|---|
|# claassif. layers|UniformInt[1_,_6]|
|Classif. layer size|Int_{_64_,_128_,_256_,_512_}_|
|Training iterations|Cat_{_5000_,_20000_,_30000_}_|
|Batch Size|Cat_{_456_,_4096_}_|
|embedding<br>~~d~~im|Int_{_16_,_32_,_64_,_128_,_256_,_512_,_1024_}_|
|loss factor|LogUniform[0_._01_,_10]|
|Proportion of samples|Float_{_0_._25_,_0_._5_,_1_,_2_,_4_,_8_}_|
|Number of tuning trials|50|



### **F. Datasets** 

We used the following datasets: 

- Abalone (OpenML) 

- Adult (income estimation, (Kohavi, 1996)) 

- Buddy (Kaggle) 

- California Housing (real estate data, (Kelley Pace & Barry, 1997)) 

- Cardiovascular Disease dataset (Kaggle) 

- Churn Modeling (Kaggle) 

- Diabetes (OpenML) 

- Facebook Comments Volume (Singh et al., 2015) 

- Gesture Phase Prediction (Madeo et al., 2013) 

- Higgs (simulated physical particles, (Baldi et al., 2014); we use the version with 98K samples available at the OpenML repository (Vanschoren et al., 2014)) 

- House 16H (OpenML) 

- Insurance (Kaggle) 

- King (Kaggle) 

- MiniBooNE (OpenML) 

- Wilt (OpenML) 

15 

**TabDDPM: Modelling Tabular Data with Diffusion Models** 

### **G. Environment and Runtime** 

Experiments were conducted under Ubuntu 20.04 on a machine equipped with GeForce RTX 2080 Ti GPU and Intel(R) Core(TM) i7-7800X CPU @ 3.50GHz. We used Pytorch 10.1, CUDA 11.3, scikit-learn 1.1.2 and imbalanced-learn 0.9.1 (for SMOTE). 

As for runtime of the proposed method, it depends on the dataset and hyperparameters. We provide 3 examples below. All three examples use _T_ = 1000 and _batch_ _~~s~~ ize_ = 4096. Note that hyperparameters tuning contains 50 runs and takes usually 8-10 hours. ”Sample time” is for the all _n_ _~~t~~ o_ _~~s~~ ample_ number of samples. 

_Table 20._ Training and sampling time for TabDDPM. 

|Dataset|input<br>dim|model<br>~~l~~ayers|train<br>~~s~~teps|n<br>to<br>~~s~~ample|train<br>~~t~~ime|sample<br>time|
|---|---|---|---|---|---|---|
|CH|16|[256,1024,1024, 1024,1024,512]|30k|26k|670s|6s|
|HI|28|[512,1024,1024, 1024,1024,512]|30k|502k|502s|430s|
|FB|146|[512,1024]|30k|1264k|783s|470s|



16 

