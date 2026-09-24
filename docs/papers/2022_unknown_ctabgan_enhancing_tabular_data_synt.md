---
title: "CTAB-GAN+: Enhancing Tabular Data Synthesis"
authors: "unknown"
year: 2022
arxiv_id: "2204.00401"
original_file: "2204.00401.pdf"
pdf_path: "docs/papers\2022_unknown_ctabgan_enhancing_tabular_data_synt.pdf"
---

# CTAB-GAN+: Enhancing Tabular Data Synthesis

**Authors:** Unknown et al.  
**Year:** 2022 | **arXiv:** [`2204.00401`](https://arxiv.org/abs/2204.00401)  
**Local PDF:** [`2022_unknown_ctabgan_enhancing_tabular_data_synt.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_unknown_ctabgan_enhancing_tabular_data_synt.pdf)

---

1 

# CTAB-GAN+: Enhancing Tabular Data Synthesis 

Zilong Zhao<sup>_∗_§</sup> , Aditya Kunar<sup>_∗_§</sup> , Robert Birke<sup>_†_</sup> , Lydia Y. Chen<sup>_∗_</sup> 

> _∗_ TU Delft, Netherlands _{_ z.zhao-8, a.kunar, y.chen-10 _}_ @tudelft.nl 

> _†_ ABB Research, Switzerland _{_ robert.birke _}_ @ch.abb.com 

**_Abstract_ —While data sharing is crucial for knowledge development, privacy concerns and strict regulation (e.g., European General Data Protection Regulation (GDPR)) limit its full effectiveness. Synthetic tabular data emerges as alternative to enable data sharing while fulfilling regulatory and privacy constraints. State-of-the-art tabular data synthesizers draw methodologies from Generative Adversarial Networks (GAN). As GANs improve the synthesized data increasingly resemble the real data risking to leak privacy. Differential privacy (DP) provides theoretical guarantees on privacy loss but degrades data utility. Striking the best trade-off remains yet a challenging research question.** 

**We propose CTAB-GAN+ a novel conditional tabular GAN. CTAB-GAN+ improves upon state-of-the-art by (i) adding downstream losses to conditional GANs for higher utility synthetic data in both classification and regression domains; (ii) using Wasserstein loss with gradient penalty for better training convergence; (iii) introducing novel encoders targeting mixed continuouscategorical variables and variables with unbalanced or skewed data; and (iv) training with DP stochastic gradient descent to impose strict privacy guarantees. We extensively evaluate CTABGAN+ on data similarity and analysis utility against stateof-the-art tabular GANs. The results show that CTAB-GAN+ synthesizes privacy-preserving data with at least 48.16% higher utility across multiple datasets and learning tasks under different privacy budgets.** 

**_Index Terms_ —GAN; Data synthesis; Tabular data; Differential privacy; Imbalanced distribution** 

## I. INTRODUCTION 

Many companies nowadays discover valuable insights from various internal and external data sources. However, the deep knowledge behind big data often violates personal privacy and leads to an unjustified analysis [22]. To prevent the abuse of data and the risks of privacy breaching, the European Commission introduced the European General Data Protection Regulation (GDPR) and enforced strict data protection measures. This however instills a new challenge in data-driven industries to look for new scientific solutions that can empower big discoveries while respecting the constraints of data privacy and governmental regulation. 

An emerging solution is to leverage synthetic data [21], which statistically resembles real data and can comply with GDPR due to its synthetic nature. Generative Adversarial Network (GAN) [12] is one of the emerging data synthesizing methodologies. Beyond its success in generating images [26], [21], [25], [33], [39] have recently applied GAN to generate tabular data. However, recent studies have shown that GANs may fall prey to membership inference attacks which greatly endanger the personal information present in the real training 

data [7], [27]. Therefore, it is imperative to safeguard the training of tabular GANs such that synthetic data can be generated without causing harm. To address these issues, prior work [16], [19], [28], [29] relies on differential privacy (DP) [9]. DP is a mathematical framework that provides theoretical guarantees bounding the statistical difference between any resulting ML model trained with or without a particular individual’s information in the original training dataset. Typically, this can be achieved by injecting calibrated statistical noise while updating the parameters of a network during back-propagation, i.e., DP Stochastic Gradient Descent (DP-SGD) [1], [6], [32], or by injecting noise while aggregating teacher ensembles using the PATE framework [16], [24]. 

However, state-of-the-art (SOTA) tabular GAN algorithms only focus on two types of variables, namely continuous and categorical, overlooking an important class of mixed data type. In addition, it is unclear if existing solutions can efficiently handle highly imbalanced or skewed variables. Furthermore, most SOTA DP GANs are evaluated on images and their efficacy on tabular datasets needs to be verified. Existing DP GANs do not provide a well-defined consensus on which DP framework (i.e., DP-SGD or PATE) is optimal for training tabular GANs. Moreover, DP GAN algorithms such as [6] (GSWGAN), [16] (PATE-GAN) change the original GAN structure from one discriminator to multiple discriminators, which increases the complexity of the algorithm. And [32] (DPWGAN) and [28](RDP-GAN) use the weight clipping to bound gradients which introduces instability for GAN training. 

In this paper, we extend CTAB-GAN [39] to a new algorithm CTAB-GAN+. The objectives of CTAB-GAN+ are twofolds: (1) further improve the synthetic data quality in terms of machine learning utility and statistical similarity; and (2) implement efficient DP into tabular GAN training to control its performance under different privacy budgets. To achieve the first goal, CTAB-GAN+ introduces a new feature encoder used with variables following single Gaussian distribution. Moreover, CTAB-GAN+ adopts the Wasserstein distance plus gradient penalty (hereinafter referred to as Was+GP) loss [13] to further enhance the stability and effectiveness of GAN training. Finally, CTAB-GAN+ adds a new auxiliary component to improve the synthesis performance for regression tasks. To achieve the second goal, CTAB-GAN+ uses DP-SGD algorithm to train a single instead of multiple discriminators as in PATE-GAN and GS-WGAN. This reduces the complexity of the algorithm. Additionally, CTAB-GAN+ reduces the privacy cost by accounting for sub-sampling [31] of smaller subsets from the full dataset used to train the discriminator. 

We rigorously evaluate CTAB-GAN+ using two setups: (1) 

> §Equal contribution 

2 











<!-- Start of picture text -->
(a) bmi in Insurance (b) Mortgage in Loan (c) Amount in Credit (d) Hours-per-week in Adult<br><!-- End of picture text -->

Figure 1: Challenges of modeling industrial dataset using existing GAN-based table generator: (a) single Gaussian (b) mixed type, (c) long tail distribution, and (d) skewed data 

without DP to generate data as realistic as possible; and (2) with DP under different privacy budgets to show the trade-off with data realism. Both setups rely on machine learning utility and statistical similarity of the synthetic data as evaluation metrics. Specifically, CTAB-GAN+ is tested on 7 widely used machine learning datasets: Adult, Covertype, Credit, Intrusion, Loan, Insurance and King against 7 SOTA GAN-based tabular data generation algorithms: CTGAN, TableGAN, CWGAN and MedGAN used in setup one, and PATE-GAN, DP-WGAN and GS-WGAN used in setup two. In setup one, CTABGAN+ outperforms all baselines on average by at least 41.2% on accuracy and 56.4% on AUC. in setup two under the same privacy budget (i.e., _ϵ_ = 1 and _ϵ_ = 100 ), CTABGAN+ outperforms all SOTA DP GANs on average by at least 48.16% on accuracy and 38.05% on F1-Score for the classification problem. 

The main contributions of this study can be summarized as follows: (1) Novel conditional adversarial network which introduces a classifier/regressor providing additional supervision to improve the utility for ML applications. (2) Efficient modelling of continuous, categorical, and **mixed** variables via novel data encoding. (3) Improved GAN training using well-designed information, downstream, generator losses along with Was+GP to enhance stability and effectiveness. (4) Constructed a simpler and more stable DP GAN algorithm for tabular data to control its performance under different privacy budgets. 

## _A. Motivation_ 

We empirically demonstrate how the prior SOTA methods fall short in solving challenges in industrial data sets. The detailed experimental setup can be found in Sec. IV-A. 

**Single Gaussian variables** . Single mode Gaussian distributions are very common. Fig. 1(a) shows the histogram of variable _bmi_ (i.e., body mass index) in the Insurance dataset and synthetic data generated by 4 SOTA algorithms for this variable. The distribution of real data is close to a single mode Gaussian distribution. But except TableGAN, none of 

the SOTA algorithms can recover this distribution in their synthetic data. CTGAN uses variational Gaussian mixture (VGM) to model all continuous variables. However, VGM is a complicated method to deal with single mode Gaussian distributions as it initially approximates the distribution with multiple Gaussian mixtures by default. CWGAN and MedGAN use min-max normalization to scale the original data to [0, 1]. TableGAN also uses min-max normalization but scales the original data to [-1, 1] to better match the output of the generator using _tanh_ as activation function. The reason that min-max normalization works for TableGAN but not MedGAN and CWGAN is because the training convergence for both algorithms is less stable than for TableGAN. However, since TableGAN applies min-max normalization on all variables, it suffers from a disadvantage modelling column with complex multi-modal Gaussian distributions. 

**Mixed data type variables** . To the best of our knowledge, existing GAN-based tabular generators only consider table columns as either categorical or continuous. However, in reality, a variable can be a mix of these two types, and often variables have missing values. The _Mortgage_ variable from the Loan dataset is a good example of mixed variable. Fig. 1(b) shows the distribution of the original and synthetic data generated by 4 SOTA algorithms for this variable. According to the data description, a loan holder can either have no mortgage (0 value) or a mortgage (any positive value). In appearance, this variable is not a categorical type due to the numeric nature of the data. So all 4 SOTA algorithms treat this variable as continuous type without capturing the special meaning of the value zero. Hence, all 4 algorithms generate a value around 0 instead of exact 0. And the negative values for Mortgage have no/wrong meaning in the real world. 

**Long tail distributions** . Many real world data can have long tail distributions where most of the occurrences happen near the initial value of the distribution, and rare cases towards the end. Fig. 1(c) plots the cumulative frequency for the original (top) and synthetic (bottom) data generated by 4 SOTA algorithms for the _Amount_ in the Credit dataset. This variable 

3 

represents the transaction amount when using credit cards. One can imagine that most transactions have small amounts, ranging from a few bucks to thousands of dollars. However, there definitely exists a very small number of transactions with large amounts. Note that for ease of comparison both plots use the same x-axis, but Real has no negative values. Real data clearly has 99% of occurrences happening at the start of the range, but the distribution extends until around 25000. In comparison none of the synthetic data generators is able to learn and imitate this behavior. 

**Skewed multi-mode continuous variables** . The term _multimode_ is extended from Variational Gaussian Mixtures (VGM). More details are given in Sec. III-C. The intuition behind using multiple modes can be easily captured from Fig. 1(d). The figure plots in each row the distribution of the working _Hours-per-week_ variable from the Adult dataset. This is not a typical Gaussian distribution. There is an obvious peak at 40 hours but with several other lower peaks, e.g. at 50, 20 and 45. Also the number of people working 20 hours per week is higher than those working 10 or 30 hours per week. This behavior is difficult to capture for the SOTA data generators (see subsequent rows in Fig.1(d)). The closest results are obtained by CTGAN which uses Gaussian mixture estimation for continuous variables. However, CTGAN loses some modes compared to the original distribution. 

The above examples show the shortcomings of current SOTA GAN-based tabular data generation algorithms and motivate the design of our proposed CTAB-GAN+. 

## II. RELATED WORK 

We divide the related work using GAN to generate tabular data into three: (i) based on GAN, (ii) based on conditional GAN, and (iii) based on DP GAN. 

**GAN-based generator** . Several studies extend GAN to accommodate categorical variables by augmenting GAN architecture. MedGAN [8] combines an auto-encoder with a GAN. It can generate continuous or discrete variables, and has been applied to generate synthetic electronic health record (EHR) data. CrGAN-Cnet [21] uses GAN to conduct Airline Passenger Name Record Generation. It integrates the Cram´er Distance [4] and Cross-Net architecture [30] into the algorithm. In addition to generating with continuous and categorical data types, CrGAN-Cnet can also handle missing value in the table by adding new variables. TableGAN [25] introduces information loss and a classifier into GAN framework. It specifically adopts Convolutional Neural Network (CNN) for generator, discriminator and classifier. Although aforementioned algorithms can generate tabular data, they cannot specify how to generate from a specific class for particular variable. For example, it is not possible to generate health record for users whose sex is female. 

**Conditional GAN-based generator** . Due to the limitation of controlling generated data via GAN, Conditional GAN is increasingly used, and its conditional vector can be used to specify to generate a particular class of data. This feature is important when our available data is limited and highly skewed, and we need synthetic data of a specific class to re-balance 

the distribution. For instance, for preparing starting dataset of online learning scenarios [35], [37], [38]. CW-GAN [11] applies the Wasserstein distance [2] into the conditional GAN framework. It leverages the usage of conditional vector to oversample the minority class to address imbalanced tabular data generation. CTGAN [33] integrates PacGAN [18] structure in its discriminator and uses Generator loss and WGAN loss plus gradient penalty (GP) [13] to train a conditional GAN framework. It also adopts a strategy called training-bysampling, which takes advantage of conditional vector, to deal with the imbalanced categorical variable problem. 

CTAB-GAN+ not only focuses on modelling both continuous and categorical variables, but also covers the mixed data type (i.e., variables that contain both categorical and continuous values, or even missing values). We effectively combine the strengths of the prior art, such as Was+GP, classifier, information and generator losses along with an effective encoding. Furthermore, we proactively address the pain points of single Gaussian and long tail variable distributions and propose a new conditional vector structure to better deal with imbalanced datasets. 

**Differential Private Tabular GANs** . To avoid leaking sensitive information on single individuals, previous studies explore multiple differential private learning techniques applied to GANs. Table I provides an overview. PATE-GAN [16] uses PATE [24] which relies on output sanitization by perturbing the output of an ensemble of teacher discriminators via Laplacian noise to train a student discriminator scoring the generated samples. One key limitation is that the student discriminator only sees synthetic data. Since this data is potentially unrealistic, the provided feedback can be unreliable. [32] (DPWGAN), [6] (GS-WGAN) and [28](RDP-GAN) use differential private stochastic gradient descent (DP-SGD) coupled with the Wasserstein loss. Moreover, DP-WGAN uses a momentum accountant whereas GS-WGAN and RDP-GAN use a R´enyi Differential Privacy (RDP) accountant. The Wasserstein loss is known to be more effective against mode-collapse compared to KL divergence [3]. The RDP accountant provides tighter bounds on the privacy costs improving the privacy-utility trade-off. To incorporate differential privacy guarantees and make the training compatible with the Wasserstein Loss, [28], [32] use weight clipping to enforce the Lipschitz constraint. The drawback is the need for careful tuning of the clipping parameter (see Sec. III-G). To overcome this issue, [6] enforces the Lipschitz constraint via a gradient penalty term as suggested by [14], but addresses only images which are a better fit for GANs and studies its efficacy only for training the generator network. 

The proposed CTAB-GAN+ leverages RDP-based privacy accounting comparing to PATE used by PATE-GAN. Same as DP-WGAN, CTAB-GAN+ uses one discriminator instead of multiple ones trained by PATE-GAN and GS-WGAN. Since CTAB-GAN+ adopts Was+GP loss, it intrinsically constraints the gradient norm allowing to forgo the weight clipping used in DP-WGAN. This leads to a more stable training. In a nutshell, CTAB-GAN+ by training only one discriminator with Was+GP loss results in a more stable DP GAN algorithm compared to the SOTA algorithms. 

4 

Table I: Overview of DP GANs 

|**Model**|**DP Algo**|**Loss**|**WC**|**DP Site**|**Single** _D_|**Noise**|**Account.**|**Data Format**|
|---|---|---|---|---|---|---|---|---|
|PATE-GAN|PATE|KL Diver.|No|_D_|No|Lap.|PATE|Table|
|DP-WGAN|DP-SGD|Was.|Yes|_D_|Yes|_N_<br>|Moment|Image & Table|
|GS-WGAN|DP-SGD|Was. + GP|No|_G_|No|_N_|RDP|Image|
|RDP-GAN|DP-SGD|Was.|Yes|_D_|Yes|_N_|RDP|Table|
|CTAB-GAN+|DP-SGD|Was. + GP|No|_D_|Yes|_N_|RDP|Table|
|_∗_Was. (Wasser|stein), WC (|Weight Clippin|g), GP|(Gradient Pe|nalty), Lap. (|Laplacian|noise)||
|_∗N_ (Gaussian|noise), _G_ (G|enerator), _D_ (|Discrimi|nator)|||||



## III. CTAB-GAN+ 

CTAB-GAN+ is a tabular data generator designed to overcome the challenges outlined in Sec. I-A. CTAB-GAN+ adopts a re-designed min-max scaler to normalize single Gaussian variable. We also propose a novel _Mixed-type Encoder_ which can better represent mixed categorical-continuous variables as well as missing values. CTAB-GAN+ is based on a conditional GAN (CGAN) to efficiently treat minority classes, with the addition of Was+GP, downstream, information and generator losses ( [13], [23], [25], [33]) to improve data quality and training stability. Moreover, we leverage a log-frequency sampler to overcome the mode collapse problem for imbalanced variables. Finally, differential private SGD training is implemented for the discriminator to achieve strict privacy guarantees. 

## _A. Technical Background_ 

_1) Tabular GAN:_ GANs are a popular method to generate synthetic data first applied with great success to images [17] and later adapted to tabular data [34]. GANs leverage an adversarial game between a generator trying to synthesize realistic data and a discriminator trying to discern synthetic from real samples. 

To address the problem of dataset imbalance, we leverage _conditional generator_ and _training-by-sampling_ methods from CTGAN. The idea behind this is to use an additional vector, termed conditional vector, to represent the classes of categorical variables. This vector is both fed to the generator and used to bound the sampling of the real training data to subsets satisfying the condition. We can leverage the condition to resample all classes giving higher chances to minority classes to train the model. To improve the stability of GAN training, CTAB-GAN+ adopts Was+GP [13] loss. Previous study WGAN [2] offers stability in training GAN. However, the use of gradient clipping leads to issues such as exploding and vanishing gradients. Comparing to WGAN [2], WGANGP replaces weight clipping with a constraint on the gradient norm of the discriminator to enforce Lipschitz continuity. This further stabilizes the training of the network and requires less hyper-parameter tuning. Another unique feature of WGANGP is that its discriminator updates 5 times per mini-batch data comparing to only 1 time of generator. This influences our differential privacy budget (see details in Sec. III-G). To enhance the generation quality, we incorporate three extra terms into the loss function of the generator: information [25], downstream (referred as classification loss in [23] for classification problems) and generator loss [33]. The information loss penalizes the discrepancy between statistics of the generated data and the real data. This helps to generate data which is statistically closer to the real one. The downstream loss requires adding to the GAN architecture an auxiliary classifier 

(or regressor) in parallel to the discriminator. For each synthesized value the classifier (or regressor) outputs a predicted value. The downstream loss quantifies the discrepancy between the synthesized and predicted values in the downstream analysis. This helps increase the semantic integrity of synthetic records. For instance, for a classification dataset, (sex=female, disease=prostate cancer) is not a semantically correct record as women do not have a prostate, and no such record should appear in the original data and is hence not learnt by the classifier. The generator loss measures the difference between the given conditions and the output classes of the generator. This loss helps the generator to learn to produce the exact same classes as the given conditions. Downstream loss is used by TableGAN but not by CTGAN, since CTGAN does not contain a classifier. Whereas, the generator loss is implemented by CTGAN but not by TableGAN, as TableGAN is not a conditional GAN. Both only treat classification problems. 

To counter complex distributions in continuous variables we embrace the _Mode-Specific Normalization (MSN)_ idea [33] which encodes each value as a value-mode pair stemming from the Gaussian mixture model. 

_2) Differential Privacy:_ DP is becoming the standard solution for privacy protection and has even been adopted by the US census department to bolster privacy of citizens [15]. DP protects against privacy attacks by minimizing the influence of any individual data point based on a given privacy budget. In this work, we leverage the R´enyi Differential Privacy (RDP) [20] as it provides stricter bounds on the privacy budget. A randomized mechanism _M_ is ( _λ, ϵ_ )-RDP with order _λ_ , if _Dλ_ ( _M_ ( _S_ ) _||M_ ( _S_<sup>_′_</sup> )) = _λ−_ <u>1</u> 1<sup>_log_E</sup><sup>_x∼M_(</sup><sup>_S_)</sup> �� _PP_ [[ _MM_ (( _SS_<sup>_<u>′</u>_</sup> <u>))==</u> _xx_ <u>]]</u> �� _λ−_ 1 _≤ ϵ_ holds for any adjacent datasets _S_ and _S_<sup>_′_</sup> , where _Dλ_ ( _P ||Q_ ) = _λ−_ <u>1</u> 1<sup>_log_E</sup><sup>_x∼Q_[(</sup><sup>_P_(</sup><sup>_x_)</sup><sup>_/Q_(</sup><sup>_x_))</sup><sup>_λ_]representstheR´enyidivergence.</sup> In addition, a ( _λ, ϵ_ )-RDP mechanism _M_ can be expressed as: 



For the purpose of this work _M_ corresponds to a tabular GAN model with privacy budget ( _λ, ϵ_ ). 

RDP is a strictly stronger privacy definition than DP as it provides tighter bounds for tracking the cumulative privacy loss over a sequence of mechanisms via the Composition theorem [20]. Let _◦_ denote the composition operator. For _M_ 1,..., _Mk_ all being ( _λ, ϵi_ )-RDP, the composition _M_ 1 _◦...◦Mk_ is 



Additionally, for a Gaussian Mechanism [10] _Mσ_ parameterized by _σ_ as: 



where _f_ denotes an arbitrary function with sensitivity ∆2 _f_ = max _S,S′ ||f_ ( _S_ ) _− f_ ( _S_<sup>_′_</sup> ) _||_ 2 over all adjacent datasets _S_ and _S_<sup>_′_</sup> , and _N_ represents a Gaussian distribution with zero mean and covariance _σ_<sup>2</sup> _I_ (where _I_ is the identity matrix), _Mσ_ satisfies ( _λ, λ_ 2∆ _σ_<sup>2</sup> 2<sup>2</sup> _<u>f</u>_<sup>)-RDP[20].</sup> Lastly, two more theorems are key to this work. The post processing theorem [10] states that if _M_ satisfies ( _ϵ, δ_ )-DP, 

5 



Figure 2: Synthetic Tabular Data Generation via CTAB-GAN+ 

_F ◦M_ will satisfy ( _ϵ, δ_ )-DP, where _F_ can be any arbitrary randomized function. Hence, it suffices to train one of the two networks in the GAN architecture with DP guarantees to ensure that the overall GAN is compatible with differential privacy. RDP for subsampled mechanisms [31] computes the reduction in privacy budget when sub-sampling private data. Formally, let _X_ be a dataset with _n_ data points and **subsample** return _m ≤ n_ subsamples without replacement from _X_ (subsampling rate _γ_ = _m/n_ ). For all integers _λ ≥_ 2, if a randomized mechanism _M_ is ( _λ, ϵ_ ( _λ_ ))-RDP, then _M◦_ **subsample** is 





## _B. Architecture of CTAB-GAN+_ 

The structure of CTAB-GAN+ is shown in Fig. 2. It comprises three blocks: Generator _G_ , Discriminator _D_ and an auxiliary component (either a classifier or a regressor) _C_ . Since our algorithm is based on conditional GAN, the generator requires a noise vector plus a conditional vector. Details on the conditional vector are given in Sec. III-D. Before feeding data to _D_ and _C_ , variables are encoded via different feature encoders depending on the variable type and characteristics. Details of the used encoders are provided in Sec. III-C, III-E and III-F. 

GANs are trained via a zero-sum min-max game where the discriminator tries to maximize the objective, while the generator tries to minimize it. The game can be seen as a mentor ( _D_ ) providing feedback to a student ( _G_ ) on the quality of his work. Here, we introduce additional feedback for _G_ based on the information loss, downstream loss and generator loss. The information loss matches the first-order (i.e., mean) and second-order (i.e., standard deviation) statistics of synthesized and real records. This leads the synthetic records to have the same statistical characteristics as the real records. The downstream loss equates the correlation between target variable and the other variable values. This helps to 

check the semantic integrity, and penalizes synthesized records where the combination of values are semantically incorrect. Finally, the generator loss is the cross-entropy between the given conditional vector and the generated output classes. It enforces the conditional generator to produce the same classes as the given conditional vector. These three losses add to the default loss term (i.e., Was+GP) of _G_ during training. _G_ and _D_ are implemented using CNNs with the same structure as in [25]. CNNs are good at capturing the relation between pixels within an image, which in our case, can help to increase the semantic integrity of synthetic data. To process row records stored as vectors with CNN, we wrap the row data into the closest square matrix dimensions, i.e. _d × d_ where _d_ is the ceiled square root of the row data dimensionality and pad missing values with zeros. _C_ uses a multi-layer-perceptron (MLP) with four 256-neuron hidden layers. The classifier is trained on the original data to better interpret the semantic integrity. Hence synthetic data are reverse transformed from their matrix encoding to vector (details in Sec. III-C). Real data is encoded (details in Sec. III-C and III-F) before being used as input for _C_ to create the class label predictions. 

Let _fx_ and _fG_ ( _z_ ) denote the features fed into the softmax layer of _D_ for a real sample _x_ and a sample generated from latent value _z_ , respectively. The **information loss** for _G_ is expressed as _L_<sup>_G_</sup> _info_<sup>=</sup><sup>_||_E[</sup><sup>_fx_]</sup><sup>_x∼p_</sup> _data_<sup>(</sup><sup>_x_)</sup><sup>_−_E[</sup><sup>_fG_(</sup><sup>_z_)]</sup><sup>_z∼p_(</sup><sup>_z_)</sup><sup>_||_2 +</sup> _||_ SD[ _fx_ ] _x∼pdata_ ( _x_ ) _−_ SD[ _fG_ ( _z_ )] _z∼p_ ( _z_ ) _||_ 2 where _pdata_ ( _x_ ) and _p_ ( _z_ ) denote prior distributions for real data and latent variable, E and SD denote the mean and standard deviations of the features, respectively. The **downstream loss** is given by _L_<sup>_G_</sup> _dstream_<sup>=E[</sup><sup>_|l_(</sup><sup>_G_(</sup><sup>_z_))</sup><sup>_−C_(</sup><sup>_fe_(</sup><sup>_G_(</sup><sup>_z_)))</sup><sup>_|_]</sup><sup>_z∼p_(</sup><sup>_z_)where</sup><sup>_l_(</sup><sup>_._)</sup> returns the target variable and _fe_ ( _._ ) returns the input features of a given row _x_ . Finally, the **generator loss** is given by _L_<sup>_G_</sup> _generator_<sup>=</sup><sup>_H_(</sup><sup>_mi,m_ˆ</sup><sup>_i_)where</sup><sup>_mi_and</sup><sup>_m_ˆ</sup><sup>_i_arethegivenand</sup> generated conditional vector bits corresponding to column _i_ and _H_ ( _._ ) is the cross-entropy loss. Columns are selected using the training-by-sampling procedure (see Sec. III-D for details). 

Let _L_<sup>_D_</sup> _default_<sup>and</sup><sup>_LG_</sup> _default_<sup>denotetheGANlossofdiscrim-</sup> inator and generator from Was+GP where its unique objective 

6 





(a) Mixed type variable distribution(b) Mode selection of single value in with VGM continuous variable 

Figure 3: Encoding for mix data type variable 

function of discriminator is defined as follows: 



where P _x_ ˆ is defined as sampling uniformly along straight lines between pairs of points sampled from the real data distribution P _r_ and the generator distribution P _g_ . For _G_ the complete training objective is _L_<sup>_G_</sup> = _L_<sup>_G_</sup> _default_<sup>+</sup><sup>_LG_</sup> _info_<sup>+</sup> _L_<sup>_G_</sup> _dstream_<sup>+</sup><sup>_LG_</sup> _generator_<sup>.Thetrainingobjectivefor</sup><sup>_D_isun-</sup> changed. Finally, the loss to train the auxiliary _C_ is similar to the downstream loss of the generator, i.e. _L_<sup>_C_</sup> _dstream_<sup>=</sup> E[ _|l_ ( _x_ ) _−C_ ( _fe_ ( _x_ )) _|_ ] _x∼pdata_ ( _x_ ). 

## _C. Mixed-type Encoder_ 

The tabular data is encoded variable by variable. We distinguish three types of variables: categorical, continuous and mixed. We define variables as mixed if they contain both categorical and continuous values or continuous values with missing values. We propose the new Mixed-type Encoder to deal with such variables. With this encoder, values of mixed variables are seen as concatenated value-mode pairs. We illustrate the encoding via the exemplary distribution of a mixed variable shown in red in Fig. 3(a). One can see that values can either be exactly _µ_ 0 or _µ_ 3 (the categorical part) or distributed around two peaks in _µ_ 1 and _µ_ 2 (the continuous part). We treat the continuous part by adapting the _Mode-Specific Normalization_ (MSN) idea from [33] in using a variational Gaussian mixture model (VGM) [5] to estimate the number of modes _k_ , e.g. _k_ = 2 in our example, and fit a Gaussian mixture. The learned Gaussian mixture is P =<sup>�2</sup> _k_ =1<sup>_ωkN_(</sup><sup>_µk, σk_),where</sup><sup>_N_isthenormaldistribution</sup> and _ωk_ , _µk_ and _σk_ are the weight, mean and standard deviation of each mode, respectively. 

To encode values in the continuous region of the variable distribution, we associate and normalize each value with the mode having the highest probability (see Fig. 3(b)). Given _ρ_ 1 and _ρ_ 2 being the probability density from the two modes in correspondence of the variable value _τ_ to encode, we select the mode with the highest probability. In our example _ρ_ 1 is higher and we use mode 1 to normalize _τ_ . The normalized value _α_ is: _α_ =<sup>_τ_</sup> 4<sup>_−_</sup> _σ_<sup>_<u>µ</u>_</sup> 1<sup><u>1</u>.Moreoverwekeeptrackofthemode</sup><sup>_β_used</sup> to encode _τ_ via one-hot encoding, e.g. _β_ = [0 _,_ 1 _,_ 0 _,_ 0] in our example. The final encoding is giving by the concatenation 



Figure 4: Conditional vector: example selects class 2 from third variable out of three 

of _α_ and _β_ : _α_<sup>�</sup> _β_ where<sup>�</sup> is the vector concatenation operator. The categorical part (e.g., _µ_ 0 or _µ_ 3 in Fig. 3(a)) is treated similarly, except _α_ is directly set to 0. Because the category is determined only by one-hot encoding part. For example, for a value in _µ_ 3, the final encoding is given by 0<sup>�</sup> [0 _,_ 0 _,_ 0 _,_ 1]. Categorical variables use the same encoding as the continuous intervals of mixed variables. Categorical variables are encoded via a one-hot vector _γ_ . Missing values are treated as a separate unique class and we add an extra bit to the one-hot vector for it. A row with [1 _, . . . , N_ ] variables is encoded by concatenation of the encoding of all variable values, i.e. either ( _α_<sup>�</sup> _β_ ) for continuous and mixed variables or _γ_ for categorical variables. Having _n_ continuous/mixed variables and _m_ categorical variables ( _n_ + _m_ = _N_ ) the final encoding is: 



## _D. Counter Imbalanced Training Datasets_ 

In CTAB-GAN+, we use conditional GAN to counter imbalanced training datasets using training-by-sampling [33], but extended to include the modes of continuous and mixed columns. When we sample real data, we use the conditional vector to filter and rebalance the training data. The conditional vector _V_ is a bit vector given by the concatenation of all mode one-hot encodings _β_ (for continuous and mixed variables) and all class one-hot encodings _γ_ (for categorical variables) for all variables present in Eq. (5). Each conditional vector specifies a single mode or a class. More in detail, _V_ is a zero vector with a single one in correspondence to the selected variable with selected mode/class. Fig. 4 shows an example with three variables, one continuous ( _C_ 1), one mixed ( _C_ 2) and one categorical ( _C_ 3), with class 2 selected on _C_ 3. 

To rebalance the dataset, each time we need a conditional vector during training, we first randomly choose a variable with uniform probability. Then we calculate the probability distribution of each mode (or class for categorical variables) in that variable using frequency as proxy and sample a mode based on the logarithm of its probability. Using the log probability instead of the original frequency gives minority modes/classes higher chances to appear during training. This helps to alleviate the collapse issue for rare modes/classes. Extending the conditional vector to include the continuous and mixed variables helps to deal with imbalance in the frequency of modes used to represent them. Moreover, since generator is conditioned on all data-types during training, this enhances the learned correlation between all variables. 

7 

## _E. General Transform_ 

CTAB-GAN originally adopts the mode-specificnormalization (MSN) from CTGAN to encode all continuous variables. MSN uses VGM to estimate the distribution of continuous variables. Fig. 1(a) shows that VGM is not suitable for simple distributions such as single Gaussian. Another problem is the dimensionality explosion caused by using one-hot-encoding for categorical variables with a high number of categories. To counter both problems we propose the general transform (GT). GT is an effective approach to minimize the complexity of our algorithm. 

The main idea of GT is to encode columns in the range of ( _−_ 1 _,_ 1). This makes the encoding directly compatible with the output range of the generator using _tanh_ activation function. This is achieved via a shifted and scaled minmax normalization. Mathematically, given a data point _xi_ of a continuous variable _x_ , the transformed value, _x_<sup>_t_</sup> _i_<sup>=</sup> _xi−min_ <u>(</u> _x_ <u>)</u> 2 _∗ max_ ( _x_ ) _−min_ ( _x_ )<sup>_−_1where</sup><sup>_min_(</sup><sup>_x_)and</sup><sup>_max_(</sup><sup>_x_)represents</sup> the minimum and maximum values of the continuous variable. Inversely an encoded or generated value _x_<sup>_t_</sup> _i_<sup>maybereverse</sup> transformed as _Xi_ = ( _max_ ( _x_ ) _− min_ ( _x_ )) _∗_<sup>_X_</sup> _<u>i</u>_<sup>_t_</sup> 2<sup>+1</sup> + _min_ ( _x_ ). Continuous variable can be directly treated with the above formulas for normalization and denormalization. Categorical variables are first encoded using integers before using the above normalization and rounded to integers after using the above denormalization. 

A similar transform was first introduced by TableGAN, but it applies this transformation on all variables. This choice is not optimal. From our experiments, we find that this technique only works well for continuous columns with simple distributions such as a single-mode Gaussian and does not cater to more complex distributions. By default, CTAB-GAN+ deals with continuous variable with MSN and only selectively uses GT for processing single-mode Gaussian variables. Similarly, categorical columns should prefer MSN as encoding rather than GT. Using GT loses the mode indicator, i.e. _β_ 1 in Fig. 4, from the conditional vector forgoing the ability to enhance the correlation between variables for specific categories. Moreover, using integers instead of one-hot vectors can impose artificial distances between the different categories which do not reflect the reality. Therefore, we recommend to use GT for categorical variables only if the categorical variables contain so many categories that the available machines can not train with the encoded data. 

values with lower bound _l_ , we replace each value _τ_ with compressed _τ_<sup>_c_</sup> : 



The log-transform allows to compress and reduce the distance between the tail and bulk data making it easier for VGM to encode all values, including tail ones. We show the effectiveness of this simple yet performant method in Sec. IV-E. 

## _G. Differential Privacy_ 

DP-SGD [1] is the central framework to provide DP guarantees in this work. DP-SGD uses noisy stochastic gradient descent to limit the influence of individual training samples _xi_ . After computing the gradient _g_ ( _xi_ ), the gradient is clipped based on a clipping parameter _C_ and its L2 norm _g_ ¯( _xi_ ) _← g_ ( _xi_ ) _/_ max(1 _,_<sup>_<u>||g</u>_</sup><sup><u>(</u></sup><sup>_x_</sup> _C_<sup>_i_</sup><sup><u>)</u></sup><sup>_<u>||</u>_2</sup> ), and Gaussian noise is added _g_ ˜( _xi_ ) _← g_ ¯( _xi_ )+ _N_ (0 _, σ_<sup>2</sup> _C_<sup>2</sup> _I_ )). _g_ ˜ is then used in place of _g_ to update the network parameters as in traditional SGD. 

One of the biggest challenges with DP-SGD is tuning the clipping parameter _C_ since clipping greatly degrades the information stored in the original gradients [6]. Choosing an optimal clipping value that does not significantly impact utility is crucial. However, tuning the clipping parameter is laborious as the optimal value fluctuates depending on network hyperparameters (i.e. model architecture, learning rate) [1]. To avoid an intensive hyper-parameter search, [6] proposes to use the Wasserstein loss with a gradient penalty term. This term ensures that the discriminator generates bounded gradient norms which are close to 1 under real and generated distributions. Therefore, an optimal clipping threshold of _C_ = 1 is obtained implicitly. 

CTAB-GAN+ trains the discriminator using differential private-SGD where the number of training iterations is determined based on the total privacy budget ( _ϵ_ , _δ_ ). Thus, to compute the number of iterations, the privacy budget spent for every iteration must be bounded and accumulated. For this purpose we use the subsampled RDP analytical moments accountant technique. 

**Corollary 1.** _Each discriminator update satisfies_ ( _λ,_ 2 _Bλ/σ_<sup>2</sup> ) _-RDP where B is the batch size._ 

**Proof 1.** _Let f_ = _clip_ (¯ _gD, C_ ) _be the clipped gradient of the discriminator before adding noise. The sensitivity is derived via the triangle inequality:_ 



## _F. Treat Long Tails_ 

We encode continuous values using variational Gaussian mixtures to treat multi-mode data distributions (details in Sec. III-C). However, Gaussian mixtures can not deal with all types of data distribution, notable distributions with long tail where few rare points are far from the bulk of the data. VGM has difficulty to encode the values towards the tail. To counter this issue we pre-process variables with long tail distributions with a logarithm transformation. For such a variable having 

_Since C_ = 1 _as a consequence of the Wasserstein loss with gradient penalty, and by using_ (3) _, the gaussian mechanism used within the DP-SGD procedure denoted as Mσ parameterized by noise scale σ may be represented as being_ ( _λ,_ 2 _λ/σ_<sup>2</sup> ) _-RDP._ 

_Furthermore, each discriminator update for a batch of real data points {xi, .., xB} can be represented as_ 



8 

_where g_ ˜ _D and θD represent the perturbed gradients and the weights of the discriminator network, respectively. This may be regarded as a composition of B Gaussian mechanisms and treated via_ (2) _. The privacy cost for a single gradient update step for the discriminator can be expressed as_ ( _λ,_<sup>�</sup><sup>_B_</sup> _i_ =1<sup>2</sup><sup>_λ/σ_2)</sup><sup>_orequivalently_(</sup><sup>_λ,_2</sup><sup>_Bλ/σ_2)</sup><sup>_._</sup> 

Note that _Mσ_ is only applied for those gradients that are computed with respect to the real training dataset [1], [36]. Hence, the gradients computed with respect to the synthetic data and the gradient penalty term are left undisturbed. Next, to further amplify the privacy protection of the discriminator, we rely on (4) with subsampling rate _γ_ = _B/N_ where _B_ is the batch size and _N_ is the size of the training dataset. Intuitively, subsampling adds another layer of randomness and enhances privacy by decreasing the chances of leaking information about particular individuals who are not included in any given subsample of the dataset. 

Lastly, it is worth mentioning that the Was+GP training objective has one major pitfall with respect to the privacy cost. This is because, it encourages the use of a stronger discriminator network to provide more meaningful gradient updates to the generator. This requires performing multiple updates to the discriminator for each corresponding update to the generator leading to a faster consumption of the overall privacy budget. 

## IV. EXPERIMENTAL ANALYSIS FOR DATA UTILITY 

To show the efficacy of the proposed CTAB-GAN+, we select seven commonly used machine learning datasets, and compare with four SOTA GAN based tabular data generators and CTAB-GAN. We evaluate the effectiveness of CTABGAN+ in terms of the resulting ML utility, statistical similarity to the real data. Moreover, we provide ablation analyses to highlight the efficacy of the unique components of CTABGAN+. 

## _A. Experimental Setup_ 

**Datasets** . Our algorithm is tested on seven commonly used machine learning datasets. Three of them **Adult** , **Covertype** and **Intrusion** are from the UCI machine learning repository<sup>1</sup> . **Credit** and **Loan** are from Kaggle<sup>2</sup> . The above five tabular datasets are used for classification tasks using as target a categorical variable. To consider also regression tasks we use two more datasets, **Insurance** and **King** from Kaggle<sup>3</sup> where the target variable is continuous. 

Due to computing resource limitations, 50K rows of data are sampled randomly in a stratified manner with respect to the target variable for the Covertype, Credit and Intrusion datasets. The Adult, Loan, Insurance and King datasets are taken in their entirety. The details of each dataset are shown in Tab. II. We assume that the data type of each variable is known before training. [33] holds the same assumption. 

> 1http://archive.ics.uci.edu/ml/datasets 

> 2https://www.kaggle.com/ _{_ mlg-ulb/creditcardfraud,itsmesunil/ 

> bank-loan-modelling _}_ 

**Baselines** . Our CTAB-GAN+ is compared with CTABGAN and 4 other SOTA GAN-based tabular data generators: CTGAN, TableGAN, CWGAN and MedGAN. To have a fair comparison, all algorithms are coded using Pytorch, with the generator and discriminator structures matching the descriptions provided in their respective papers. For Gaussian mixture estimation of continuous variables, we use the same settings as the evaluation of CTGAN, i.e. 10 modes. All algorithms are trained for 150 epochs for Adult, Covertype, Credit and Intrusion datasets, whereas the algorithms are trained for 300 epochs on Loan, Insurance and King datasets. The reason is these three datasets are smaller than the others and require more epochs to converge. Lastly, each experiment is repeated 3 times. 

**Environment** . Experiments are run under Ubuntu 20.04 on a machine equipped with 32 GB memory, a GeForce RTX 2080 Ti GPU and a 10-core Intel i9 CPU. 

## _B. Evaluation Metrics_ 

The evaluation is conducted on two dimensions: (1) machine learning (ML) utility, and (2) statistical similarity. They measure if the synthetic data can be used as a good proxy of the original data. 

_1) Machine Learning Utility:_ The ML utility of classification and regression tasks is quantified differently. For classification, we quantify the ML utility via the performance, i.e, accuracy, F1-score and AUC, achieved by 5 widely used machine learning algorithms on real versus synthetic data: decision tree classifier, linear support-vector-machine (SVM), random forest classifier, multinomial logistic regression and MLP. Fig. 5 shows the evaluation process for classification datasets. The training dataset and synthetic dataset are of the same size. The aim is to show the difference in ML utility when a ML model is trained on synthetic vs real data. We use different classification performance metrics. Accuracy is the most commonly used, but does not cope well with imbalanced target variables. F1-score and AUC are more stable metrics for such cases. AUC ranges from 0 to 1. For regression tasks, we quantify the ML utility in a similar manner but using 4 common regression algorithms – linear regression, ridge regression, lasso regression and Bayesian ridge regression – and 3 regression metrics – mean absolute percentage error (MAPE), explained variance score (EVS) and _R_<sup>2</sup> score. All algorithms are implemented using scikit-learn 0.24.2 with default parameters except max-depth 28 for decision tree and random forest, and 128 neurons for MLP. For a fair comparison, hyper-parameters are fixed across all datasets. Due to this our results can slightly differ from [33] where the authors use different ML models and hyper-parameters for different datasets. 

_2) Statistical Similarity:_ Three metrics are used to quantify the statistical similarity between real and synthetic data. 

**Jensen-Shannon divergence (JSD)** . The JSD provides a measure to quantify the difference between the probability mass distributions of individual categorical variables belonging to the real and synthetic datasets, respectively. Moreover, this metric is bounded between 0 and 1 and is symmetric allowing for an easy interpretation of results. 

> 3https://www.kaggle.com/ _{_ mirichoi0218/insurance,harlfoxem/ housesalesprediction _}_ 

9 

Table II: Description of Datasets 

|**Dataset**|**Problem**|**Train/Test Split**|**Target variable**|**Continuous**|**Binary**|**Multi-class**|**Mixed-type**|**Long-tail**|**General Transform**|
|---|---|---|---|---|---|---|---|---|---|
|Adult|Classification|39k/9k|’income’|3|2|7|2|0|1|
|Covertype|Classification|45k/5k|’Cover<br>Type’|10|44|1|0|0|47|
|Credit|Classification|40k/10k|’Class’|30|1|0|0|1|29|
|Intrusion|Classification|45k/5k|’Class’|22|6|14|0|2|6|
|Loan|Classification|4k/1k|’PersonalLoan’|5|5|2|1|0|9|
|Insurance|Regression|1k/300|’charges’|13|3|2|2|0|1|
|King|Regression|17.3k/4.3k|’price’|1|6|2|0|0|6|





Figure 5: Evaluation flows for ML utility of Classification 

**Wasserstein distance (WD)** . In a similar vein, the Wasserstein distance is used to capture how well the distributions of individual continuous/mixed variables are emulated by synthetically produced datasets in correspondence to real datasets. We use WD because we found that the JSD metric was numerically unstable for evaluating the quality of continuous variables, especially when there is no overlap between the synthetic and original dataset. Hence, we resorted to utilize the more stable Wasserstein distance. 

**Difference in pair-wise correlation (Diff. Corr.)** . To evaluate how well feature interactions are preserved in the synthetic datasets, we first compute the pair-wise correlation matrix for the columns within real and synthetic datasets individually. Pearson correlation coefficient is used between any two continuous variables. It ranges between [ _−_ 1 _,_ +1]. Similarly, the Theil uncertainty coefficient is used to measure the correlation between any two categorical features. It ranges between [0 _,_ 1]. And the correlation ratio between categorical and continuous variables is used. It also ranges between [0 _,_ 1]. Note that the dython<sup>4</sup> library is used to compute these metrics. Finally, the difference between pair-wise correlation matrices for real and synthetic datasets is computed. 

## _C. Results Analysis_ 

We first discuss the results in ML utility before addressing stochastic similarity. 

**ML Utility** . Tab. III shows the results for the classification datasets. A better synthetic dataset is expected to have small differences in d ML utility for classification tasks trained on real and synthetic data. It can be seen that CTAB-GAN+ outperforms all other SOTA methods and CTAB-GAN in all 

> 4http://shakedzy.xyz/dython/modules/nominal/#compute <u>associations</u> 

Table III: Difference of ML Utility and Statistical Similarity for Classification between original and synthetic data, averaged on five datasets 

|**Method**|**ML Ut**|**ility Differe**|**nce**|**Statistica**|**l Similarity **|**Difference**|
|---|---|---|---|---|---|---|
||**Accuracy**|**F1-score**|**AUC**|**Avg JSD**|**Avg WD**|**Diff. Corr.**|
|CTAB-GAN+|**5.23**%|**0.090**|**0.041**|**0.039**|**484**|**2.03**|
|CTAB-GAN|8.90%|0.107|0.094|0.062|1197|2.09|
|CTGAN|21.51%|0.274|0.253|0.070|1769|2.73|
|TableGAN|11.40%|0.130|0.169|0.080|2117|2.30|
|MedGAN|14.11%|0.282|0.285|0.214|46257|5.48|
|CW-GAN|20.06%|0.354|0.299|0.132|238155|5.82|



Table IV: Difference of ML Utility and Statistical Similarity for Regression between original and synthetic data, averaged on two datasets 

|**Method**|**ML Uti**|**lity Diff**|**erence**<br>|**Statistica**|**l Similarity **|**Difference**|
|---|---|---|---|---|---|---|
||**MAPE**|**EVS**|_R_<sup>2</sup>|**Avg JSD**|**Avg WD**|**Diff. Corr.**|
|CTAB-GAN+|**0.04**|**0.03**|**0.04**|**0.040**|**856**|**0.65**|
|CTAB-GAN|0.06|0.05|0.06|0.119|3396|1.23|
|CTGAN|0.87|0.59|0.71|0.139|3030|2.60|
|TableGAN|0.34|0.43|0.48|0.317|2366|2.26|
|MedGAN|5.98|0.65|27.47|0.398|170307|7.27|
|CW-GAN|0.64|0.72|2.40|0.43|9.96E6|9.59|



the metrics. CTAB-GAN+ decreases the AUC difference from 0.094 (best baseline) to 0.041 (56.4% reduction), and the difference in accuracy from 8.9% (best baseline) to 5.23% (41.2% reduction). The improvement over CTAB-GAN shows that general transform and Was+GP loss indeed help enhance the feature representation and GAN training. Tab. IV shows the results for the regression datasets. The result of CTABGAN and CTAB-GAN+ are far better than all other baselines. This shows the effectiveness of the feature engineering. Additionally, as CTAB-GAN+ adds the auxiliary regressor which explicitly enhances the regression analysis, the overall downstream performance of CTAB-GAN+ is better than CTABGAN. We note that CTAB-GAN uses auxiliary classification loss for the classification analysis and disables it for the regression analysis. 

**Statistical similarity** . Statistical similarity results for the classification datasets are reported in Tab. III and for regression datasets in Tab. IV. CTAB-GAN+ stands out again across all baselines in both groups of datasets. For classification datasets, CTAB-GAN+ outperforms CTAB-GAN, CTGAN and TableGAN by 37.1%, 44.3% and 51.3% in average JSD. This is due to the use of the conditional vector, the log-frequency sampling and the extra losses, which work well for both balanced and imbalanced distributions. For continuous variables (i.e. average WD), the average WD column shows some extreme numbers such as 46257 and 238155 comparing to 484 of CTAB-GAN+. The reason is that these algorithms generate extremely large values for long tail variables. Comparing to CTAB-GAN, the significant improvement comes from the 

10 

use of general transform to model continuous columns with simple distributions which originally used MSN under CTABGAN and CTGAN. For regression datasets, CTAB-GAN+ outperforms CTAB-GAN by 63.4% and 74.5% in average JSD and average WD, respectively. Besides JSD and WD, the synthetic regression datasets maintain much better correlation than all the comparisons. This result confirms the efficacy of the usage of regressor. 

Table V: Ablation Analysis For CTAB-GAN (F1. diff.) 

|**Dataset**|**CTAB-GAN**|**w/o** _C_|**w/o I. Loss**|**w/o MSN**|**w/o LT**|
|---|---|---|---|---|---|
|Adult|0.704|-0.01|-0.037|-0.05|-|
|Covertype|0.532|-0.018|-0.184|-0.118|-|
|Credit|0.710|+0.011|-0.177|+0.06|+0.001|
|Intrusion|0.842|-0.031|-0.437|+0.003|-0.074|
|Loan|0.803|-0.044|+0.028|+0.013|-|



## _D. Ablation Analysis_ 

For the sake of simplicity, ablation analysis are only implemented for classification datasets. We focus on conducting an ablation study to analyse the impact of the different components of CTAB-GAN and CTAB-GAN+. 

_1) With CTAB-GAN:_ To illustrate the efficiency of each strategy we implement four ablation studies which cut off the different components of CTAB-GAN one by one: (1) **w/o** _C_ . In this experiment, Classifier _C_ and the corresponding classification loss for Generator _G_ are taken away from CTABGAN; (2) **w/o I. loss** (information loss). In this experiment, we remove information loss from CTAB-GAN; (3) **w/o MSN** . In this case, we substitute the mode specific normalization based on VGM for continuous variables with min-max normalization and use simple one-hot encoding for categorical variables. Here the conditional vector is the same as for CTGAN; (4) **w/o LT** (long tail). In this experiment, long tail treatment is no longer applied. This only affects datasets with long tailed columns, i.e. Credit and Intrusion. 

The results are compared with the reference CTAB-GAN implementing all strategies. All experiments are repeated 3 times, and results are evaluated on the same 5 machine learning algorithms introduced in Sec. IV-B1. The test datasets and evaluation flow are the same as shown in Sec. IV-A and Sec. IV-B. Tab. V shows the results in terms of F1-score difference between ablation and CTAB-GAN. Each part of CTAB-GAN has different impacts on different datasets. For instance, **w/o** _C_ has a negative impact for all datasets except Credit. Since Credit has only 30 continuous variables and one target variable, the semantic check can not be very effective. **w/o information loss** has a positive impact for Loan, but results degenerate for all other datasets. It can even make the model unusable, e.g. for Intrusion. **w/o MSN** performs bad for 

Table VI: Ablation Analysis For CTAB-GAN+ (F1. diff.) 

|**Dataset**|**CTAB-GAN+**|**w/o GT**|**w/o Was+GP**|
|---|---|---|---|
|Adult|0.684|+0.013|-0.029|
|Covertype|0.636|-0.196|-0.012|
|Credit|0.802|-0.303|-0.08|
|Intrusion|0.912|-0.041|-0.049|
|Loan|0.806|-0.001|+0.003|



Covertype, but has little impact for Intrusion. Credit w/o MSN performs better than original CTAB-GAN. This is because out of 30 continuous variables, 28 are nearly single mode Gaussian distributed. The initialized high number of modes, i.e. 10, for each continuous variable (same setting as in CTGAN) degrades the estimation quality. **w/o LT** has the biggest impact on Intrusion, since it contains 2 long tail columns which are important predictors for the target column. For Credit, the influence is limited. Even if the long tail treatment fits well the _amount_ column (see Sec. IV-E), this variable is not a strong predictor for the target column. 

_2) With CTAB-GAN+:_ To show the efficacy of the General Transform and Was+GP loss in CTAB-GAN+, we propose two ablation studies. (1) **w/o GT** which disables the general transform in CTAB-GAN+. All continuous variables use MSN and all the categorical variables use one-hot encoding. (2) **w/o Was+GP** which switches the default GAN training loss from Was+GP to the original GAN loss defined in [12]. It is worth noting that the information, downstream and generator losses are still present in this experiment. The other experimental settings are the same as in Sec. IV-D1. Tab. VI shows the results in terms of F1-score difference among different versions of CTAB-GAN+. For Covertype, Credit and Intrusion datasets, the effects of GT and Was+GP are all positive. GT significantly boosts the performance on Covertype and Credit datasets. But for Adult, it worsens the result. The reason is that the Adult dataset contains only one GT column: age. Since this column is strongly correlated with other columns, the original MSN encoding can better capture this interdependence. The positive impact of Was+GP on the other hand is limited but consistent across all datasets. The only exception is the Loan dataset, where GT and Was+GP have minor impacts. This is due to the fact that Loan has fewer variables comparing to other datasets, which makes it easier to capture the correlation between columns. CTAB-GAN already performs well on Loan, Therefore, GT and Was+GP cannot further improve performance on this dataset. 

## _E. Results for Motivation Cases_ 

After reviewing all the metrics, let us recall the four motivation cases from Sec. I-A. 

**Single Gaussian variables** . Fig. 6a(a) shows the real and CTAB-GAN+ generated _bmi_ variable. CTAB-GAN+ can reproduce the distribution with minor differences. This shows the effctiveness of general transform to better model variables with single Gaussian distribution. 

**Mixed data type variables** . Fig. 6(b) compares the real and CTAB-GAN+ generated variable _Mortgage_ in Loan dataset. CTAB-GAN+ encodes this variable as mixed type. We can see that CTAB-GAN+ generates clear 0 values and the frequency is close to real data. 

**Long tail distributions.** Fig. 6(c) compares the cumulative frequency graph for the _Amount_ variable in Credit. This variable is a typical long tail distribution. One can see that CTAB-GAN+ perfectly recovers the real distribution. Due to log-transform data pre-processsing, CTAB-GAN+ learns this structure significantly better than the SOTA methods shown in Fig. 1(c). 

11 











<!-- Start of picture text -->
(a) bmi in Insurrance (b) Mortgage in Loan (c) Amount in Credit (d) Hours-per-week in Adult<br><!-- End of picture text -->

Figure 6: Challenges of modeling industrial dataset using existing GAN-based table generator: (a) simple gaussian (b) mixed type, (c) long tail distribution, and (d) skewed data 

**Skewed multi-mode continuous variables** . Fig. 6(d) compares the frequency distribution for the continuous variable _Hours-per-week_ from Adult. Except the dominant peak at 40, there are many side peaks. Fig. 1(d), shows that TableGAN, CWGAN and MedGAN struggle since they can learn only a simple Gaussian distribution due to the lack of any special treatment for continuous variables. CTGAN, which also use VGM, can detect other modes. Still, CTGAN is not as good as CTAB-GAN. The reason is that CTGAN lacks the mode of continuous variables in the conditional vector. By incorporating the mode of continuous variables into conditional vector, we can apply the training-by-sample and logarithm frequency also to modes. This gives the mode with less weight more chance to appear in the training and avoids the mode collapse. 

## V. EXPERIMENT ANALYSIS FOR DIFFERENTIAL PRIVACY 

In this section, we show the effect of adding DP to CTABGAN+ and compare CTAB-GAN+ with three SOTA DP GAN algorithms. 

## _A. Experiment Setup_ 

**Datasets** . For sake of simplicity, we only use the classification datasets: Adult, Covertype, Intrusion, Credit and Loan. **Metrics** . We use the same ML utility metrics from Section IV-B under two privacy budgets, i.e., _ϵ_ = 1 and _ϵ_ = 100. 

**Baselines** . CTAB-GAN+ is compared against 3 SOTA architectures: PATE-GAN [16], DP-WGAN [32] and GSWGAN [6]. The code of PATE-GAN and DP-WGAN is taken from Private Data Generation Toolbox<sup>5</sup> which already adapts them for tabular data synthesis. We extend GS-WGAN to the tabular domain by converting each data row into a bitmap image. We first normalize all values to the range [0 _,_ 1] and re-shape rows in the form of square images filling missing entries (if any) with zeros. The re-shaped rows are fed into the algorithm and the generated images are transformed into data rows by reversing the previous two operations. All hyperparameters are kept to their default values except for the default network architecture which is adjusted according to 

the spatial dimensions of the tabular datasets. Lastly, note that to compute privacy cost fairly, the RDP accountant is used for all approaches that use DP-SGD as it provides tighter privacy guarantees than the moment accountant [31]. 

**Privacy accounting** . To compute the privacy cost in a fair manner, we use the RDP accountant for all approaches that employ DP-SGD: CTAB-GAN+, DP-WGAN and GS-WGAN. PATE-GAN uses moment accountant [31] by default. We set _δ_ = 10<sup>_−_5</sup> for all experiments. We follow the examples of DP-WGAN and set the exploration span of _λ_ to [2 _,_ 4096]. We use (1) to convert the overall cumulative privacy cost computed in terms of RDP back to ( _ϵ, δ_ )-DP. 

## _B. Results Analysis_ 

**ML Utility** Tab. VII presents the results for the differences ML utility between models trained on the original and synthetic data: lower is better. CTAB-GAN+ outperforms all other SOTA algorithms under both privacy budgets. With a looser privacy budget, i.e., higher _ϵ_ , almost all metrics for all algorithms improve. The only exception is AUC for GSWGAN, but the difference is minor. These results are in line with our expectation because higher privacy budgets mean training the model with less injected noise and more training epochs – before exhaustion of the privacy budget. The superior performance of CTAB-GAN+ compared to other baselines can be explained by its sophisticated neural network architecture, i.e., conditional GAN, which improves the training objective and capacity to better deal with the challenges of the tabular domain such as imbalanced categorical columns and mixed data-types. This also explains the poor results offered by GSWGAN which is not designed to handling these specific issues achieving the worst overall performance. 

**Statistical Similarity** . Tab. VIII summarizes the statistical similarity results. Among all DP models, CTAB-GAN+ and GS-WGAN consistently improve across all metrics when the privacy budget is increased. But the performance of GSWGAN is significantly worse than CTAB-GAN+. With a higher privacy budget, Avg WD of PATE-GAN is slightly increased. And the correlation difference of DP-WGAN increases too. This highlights the inability of this methods to capture the statistical distributions during training despite a 

5https://github.com/BorealisAI/private-data-generation 

12 

Table VII: Difference of accuracy (%), F1-score, AUC and AP between original and synthetic data: average over 5 ML models and 5 datasets with different privacy budgets _ϵ_ = 1 & _ϵ_ = 100. 

|**Mthd**||_ϵ_= 1|||_ϵ_= 100||
|---|---|---|---|---|---|---|
|**eo**|**Accuracy**|**F1-Score**|**AUC**|**Accuracy**|**F1-Score**|**AUC**|
|CTAB-GAN+|**19.12%**|**0.320**|**0.311**|**13.34**%|**0.311**|**0.299**|
|PATE-GAN|38.17%|0.513|0.447|37.96%|0.508|0.394|
|DP-WGAN|36.88%|0.536|0.510|27.27%|0.502|0.423|
|GS-WGAN|64.10%|0.668|0.492|58.22%|0.639|0.498|



Table VIII: Statistical similarity metrics between original and synthetic data: average on 5 datasets with different privacy budgets _ϵ_ = 1 & _ϵ_ = 100. 

|**Mthd**||_ϵ_= 1|||_ϵ_= 100||
|---|---|---|---|---|---|---|
|**eo**|**Avg JSD**|**Avg WD**|**Diff. Corr.**|**Avg JSD**|**Avg WD**|**Diff. Corr.**|
|CTAB-GAN+|**0.192**|**775**|**5.61**|**0.137**|**655**|**5.54**|
|PATE-GAN|0.356|8632|9.45|0.366|8634|8.94|
|DP-WGAN|0.362|8632|9.19|0.359|8632|9.49|
|GS-WGAN|0.624|4.07E+06|15.61|0.547|54574|13.74|



looser privacy budget. This can be explained by the lack of an effective training framework for dealing with complex statistical distributions present in the tabular domain which arise from imbalances in categorical columns and skews in continuous columns commonly found in real-world tabular datasets. 

## VI. CONCLUSION 

Motivated by the importance of data sharing and fulfillment of governmental regulations, we propose CTAB-GAN+, a conditional GAN based tabular data generator. CTAB-GAN+ advances beyond SOTA methods by modeling mixed variables and providing strong generation capability for imbalanced categorical variables, and continuous variables with complex distributions. The core features of CTAB-GAN+ include: (1) introduction of the auxiliary component, i.e., classifier or regressor, into conditional GAN, (2) effective data encodings for mixed and simple Guassian variables, (3) a novel construction of conditional vectors and (4) tailored DP discriminator for tabular GAN. We exhaustively evaluate CTAB-GAN+ against state-of-the-art baselines on seven tabular datasets under a wide range of metrics, namely for ML utility and statistical similarity. Results show that the synthetic data of CTABGAN+ results into higher ML utility and higher similarity. The overall improvement on classification datasets is at least 56.4% (AUC) and 41.2% (accuracy) compared to related work with no privacy guarantees. When turning on differential privacy, CTAB-GAN+ averagely outperforms at least 48.16% on accuracy and 38.05% on F1-Score than existing DP-GAN training under all privacy budgets. The substantial results of CTAB-GAN+ demonstrate its potential for a wide range of applications that greatly benefit from data sharing, such as banking, insurance, and manufacturing. 

## REFERENCES 

- [1] M. Abadi, A. Chu, I. Goodfellow, H. B. McMahan, I. Mironov, K. Talwar, and L. Zhang. Deep learning with differential privacy. In _ACM SIGSAC Conference on Computer and Communications Security (CCS)_ , 2016. 

- [2] M. Arjovsky, S. Chintala, and L. Bottou. Wasserstein generative adversarial networks. In _Proceedings of the 34th ICML - Volume 70_ , page 214–223. JMLR.org, 2017. 

- [3] M. Arjovsky, S. Chintala, and L. Bottou. Wasserstein generative adversarial networks. In _International Conference on Machine Learning (ICML)_ , 2017. 

- [4] M. G. Bellemare, I. Danihelka, W. Dabney, S. Mohamed, B. Lakshminarayanan, S. Hoyer, and R. Munos. The cramer distance as a solution to biased wasserstein gradients. _ArXiv_ , abs/1705.10743, 2017. 

- [5] C. M. Bishop. _Pattern Recognition and Machine Learning (Information Science and Statistics)_ . Springer-Verlag, Berlin, Heidelberg, 2006. 

- [6] D. Chen, T. Orekondy, and M. Fritz. Gs-wgan: A gradient-sanitized approach for learning differentially private generators. _arXiv preprint arXiv:2006.08265_ , 2020. 

- [7] D. Chen, N. Yu, Y. Zhang, and M. Fritz. Gan-leaks: A taxonomy of membership inference attacks against generative models. In _ACM SIGSAC Conference on Computer and Communications Security (CCS)_ , 2020. 

- [8] E. Choi, S. Biswal, B. Malin, J. Duke, W. F. Stewart, and J. Sun. Generating multi-label discrete patient records using generative adversarial networks. _arXiv preprint arXiv:1703.06490_ , 2017. 

- [9] C. Dwork. Differential privacy: A survey of results. In _International Conference on Theory and Applications of Models of Computation (TAMC)_ . Springer, 2008. 

- [10] C. Dwork, A. Roth, et al. The algorithmic foundations of differential privacy. _Foundations and Trends in Theoretical Computer Science_ , 2014. 

- [11] J. Engelmann and S. Lessmann. Conditional wasserstein gan-based oversampling of tabular data for imbalanced learning. _arXiv preprint arXiv:2008.09202_ , 2020. 

- [12] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio. Generative adversarial nets. In _Proceedings of the 27th NIPS - Volume 2_ , page 2672–2680, Cambridge, MA, USA, 2014. 

- [13] I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. Courville. Improved training of wasserstein gans. In _the 31st NIPS_ , page 5769–5779, 2017. 

- [14] I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. C. Courville. Improved training of wasserstein gans. In _Advances in Neural Information Processing Systems_ , 2017. 

- [15] M. B. Hawes. Implementing differential privacy: Seven lessons from the 2020 united states census. _Harvard Data Science Review_ , 4 2020. 

- [16] J. Jordon, J. Yoon, and M. van der Schaar. Pate-gan: Generating synthetic data with differential privacy guarantees. In _International Conference on Learning Representations (ICLR)_ , 2018. 

- [17] T. Karras, S. Laine, and T. Aila. A style-based generator architecture for generative adversarial networks. In _IEEE/CVF CVPR_ , pages 4396–4405, 2019. 

- [18] Z. Lin, A. Khetan, G. Fanti, and S. Oh. Pacgan: The power of two samples in generative adversarial networks. _IEEE JSAIT_ , 1(1):324–335, 2020. 

- [19] Y. Long, S. Lin, Z. Yang, C. A. Gunter, and B. Li. Scalable differentially private generative student model via pate. _arXiv preprint arXiv:1906.09338_ , 2019. 

- [20] I. Mironov. R´enyi differential privacy. In _Computer Security Foundations Symposium (CSF)_ . IEEE, 2017. 

- [21] A. Mottini, A. Lheritier, and R. Acuna-Agost. Airline Passenger Name Record Generation using Generative Adversarial Networks. In _workshop on Theoretical Foundations and Applications of Deep Generative Models. ICML_ , July 2018. 

- [22] A. Narayanan and V. Shmatikov. Robust de-anonymization of large sparse datasets. In _IEEE Symposium on Security and Privacy_ , pages 111–125, 2008. 

- [23] A. Odena, C. Olah, and J. Shlens. Conditional image synthesis with auxiliary classifier gans. In _The 34th ICML - Volume 70_ , page 2642–2651, 2017. 

- [24] N. Papernot, M. Abadi, U. Erlingsson, I. Goodfellow, and K. Talwar. Semi-supervised knowledge transfer for deep learning from private training data. _arXiv preprint arXiv:1610.05755_ , 2016. 

- [25] N. Park, M. Mohammadi, K. Gorde, S. Jajodia, H. Park, and Y. Kim. Data synthesis based on generative adversarial networks. _Proc. VLDB Endow._ , 11(10):1071–1083, June 2018. 

- [26] B. Proven-Bessel, Z. Zhao, and L. Chen. Comicgan: Text-to-comic generative adversarial network. _arXiv preprint arXiv:2109.09120_ , 2021. 

- [27] T. Stadler, B. Oprisanu, and C. Troncoso. Synthetic data–a privacy mirage. _arXiv preprint arXiv:2011.07018_ , 2020. 

13 

- [28] A. Torfi, E. A. Fox, and C. K. Reddy. Differentially private synthetic medical data generation using convolutional gans. _arXiv preprint arXiv:2012.11774_ , 2020. 

- [29] R. Torkzadehmahani, P. Kairouz, and B. Paten. Dp-cgan: Differentially private synthetic data and label generation. In _Conference on Computer Vision and Pattern Recognition (CVPR) Workshops_ , 2019. 

- [30] R. Wang, B. Fu, G. Fu, and M. Wang. Deep & cross network for ad click predictions. In _Proceedings of the ADKDD’17_ , New York, NY, USA, 2017. 

- [31] Y.-X. Wang, B. Balle, and S. P. Kasiviswanathan. Subsampled r´enyi differential privacy and analytical moments accountant. In _International Conference on Artificial Intelligence and Statistics (AISTATS)_ , 2019. 

- [32] L. Xie, K. Lin, S. Wang, F. Wang, and J. Zhou. Differentially private generative adversarial network. _arXiv preprint arXiv:1802.06739_ , 2018. 

- [33] L. Xu, M. Skoularidou, A. Cuesta-Infante, and K. Veeramachaneni. Modeling tabular data using conditional gan. In _NIPS_ , 2019. 

- [34] A. Yahi, R. Vanguri, and N. Elhadad. Generative adversarial networks for electronic health records: A framework for exploring and evaluating methods for predicting drug-induced laboratory test trajectories. In _NIPS workshop_ , 2017. 

- [35] T. Younesian, Z. Zhao, A. Ghiassi, R. Birke, and L. Y. Chen. Qactor: On-line active learning for noisy labeled stream data. _arXiv preprint arXiv:2001.10399_ , 2020. 

- [36] X. Zhang, S. Ji, and T. Wang. Differentially private releasing via deep generative model (technical report). _arXiv preprint arXiv:1801.01594_ , 2018. 

- [37] Z. Zhao, R. Birke, R. Han, B. Robu, S. Bouchenak, S. B. Mokhtar, and L. Y. Chen. Enhancing robustness of on-line learning models on highly noisy data. _IEEE Transactions on Dependable and Secure Computing_ , 18(5):2177–2192, 2021. 

- [38] Z. Zhao, S. Cerf, R. Birke, B. Robu, S. Bouchenak, S. B. Mokhtar, and L. Y. Chen. Robust anomaly detection on unreliable data. In _49th Annual IEEE/IFIP International Conference on Dependable Systems and Networks_ , 2019. 

- [39] Z. Zhao, A. Kunar, R. Birke, and L. Y. Chen. Ctab-gan: Effective table data synthesizing. In _Proceedings of The 13th Asian Conference on Machine Learning_ , volume 157, pages 97–112, 17–19 Nov 2021. 

