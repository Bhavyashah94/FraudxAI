---
title: "Relating the Partial Dependence Plot and Permutation Feature Importance to the Data-Generating Process"
authors: "process"
year: 2021
arxiv_id: "2109.01433"
original_file: "2109.01433.pdf"
pdf_path: "docs/papers\2021_process_relating_the_partial_dependence_plo.pdf"
---

# Relating the Partial Dependence Plot and Permutation Feature Importance to the Data-Generating Process

**Authors:** Process et al.  
**Year:** 2021 | **arXiv:** [`2109.01433`](https://arxiv.org/abs/2109.01433)  
**Local PDF:** [`2021_process_relating_the_partial_dependence_plo.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2021_process_relating_the_partial_dependence_plo.pdf)

---

**Relating the Partial Dependence Plot and Permutation Feature Importance to the Data Generating Process** 

**Christoph Molnar** **_·_ Timo Freiesleben** **_·_ Gunnar K¨onig** **_·_ Giuseppe Casalicchio** **_·_ Marvin N. Wright** **_·_ Bernd Bischl** 

**Abstract** Scientists and practitioners increasingly rely on machine learning to model data and draw conclusions. Compared to statistical modeling approaches, machine learning makes fewer explicit assumptions about data structures, such as linearity. However, their model parameters usually cannot be easily related to the data generating process. To learn about the modeled relationships, partial dependence (PD) plots and permutation feature importance (PFI) are often used as interpretation methods. However, PD and PFI lack a theory that relates them to the data generating process. We formalize PD and PFI as statistical estimators of ground truth estimands rooted in the data generating process. We show that PD and PFI estimates deviate from this ground truth due to statistical biases, model variance and Monte Carlo approximation errors. To account for model variance in PD and PFI estimation, we propose the learner-PD and the learner-PFI based on model refits, and propose corrected variance and confidence interval estimators. 

**Keywords** Interpretable Machine Learning, Explainable AI, Permutation Feature Importance, Partial Dependence Plot, Statistical Inference, Uncertainty Quantification 

This project is funded by the Bavarian State Ministry of Science and the Arts and coordinated by the Bavarian Research Institute for Digital Transformation (bidt) and supported by the German Federal Ministry of Education and Research (BMBF) under Grant No. 01IS18036A, by the German Research Foundation (DFG) – Emmy Noether Grant 437611051 to MNW, and by the Graduate School of Systemic Neurosciences (GSN) Munich. The authors of this work take full responsibilities for its content. 

C. Molnar, T. Freiesleben, G. K¨onig, G. Casalicchio, B. Bischl Ludwig-Maximilian University Munich, Germany 

G. K¨onig University of Vienna, Austria 

C. Molnar, M. Wright Leibniz Institute for Prevention Research and Epidemiology – BIPS, Bremen, Germany M. Wright University of Bremen, Germany 

Christoph Molnar et al. 

2 

# **1 Introduction** 

Statistical models such as linear or logistic regression models are frequently used to learn about relationships in data. Assuming that a statistical model reflects the data generating process (DGP) well, we may interpret the model coefficients in place of the DGP and draw conclusions about the data. An important part of interpreting the coefficients is the quantification of their uncertainty via standard errors, which allows to separate random noise (nonsignificant coefficients) from real effects. Statistical biases and violation of assumptions are well studied for many model classes, such as heterogeneous residuals, deviations from normality, and non-additivity for linear models (Fahrmeir et al., 2007). 

Increasingly, machine learning approaches such as gradient-boosted trees, random forests or neural networks are used instead of or in addition to statistical models. Compared to statistical models that are driven by considerations of the data generating process, the machine learning approaches often lack a mapping between model parameters and properties of the DGP. Due to the ability of many machine learning models to address highly non-linear relationships and interactions, they often outperform more restrictive statistical models. Scientific applications of machine learning are widespread and range from modeling volunteer labor supply (Bair et al., 2013), mapping fish biomass (Esselman et al., 2015), analyzing urban reservoirs (Obringer and Nateghi, 2018), identifying disease-associated genetic variants (Boulesteix et al., 2020), and inferring behavior from smartphone use (Stachl et al., 2020). In these scientific applications, the model is only the means to an end: a better understanding of the data generating process, in particular the conditional expectation of the target variables as a function of the features. 

Model-agnostic interpretation methods (Ribeiro et al., 2016) are a (partial) remedy to the lack of interpretable parameters of more complex models. Model-agnostic methods follow a general procedure of 1) sampling data, 2) manipulating this data, 3) predicting and 4) aggregating the predictions (Scholbeck et al., 2019). Since none of these steps depend on specific model properties, model-agnostic interpretation techniques allow us to study the behavior of arbitrary models. Partial dependence (PD) plots (Friedman, 1991) and permutation feature importance (PFI) (Breiman, 2001; Fisher et al., 2019) are popular model-agnostic methods for describing the relationship between input features and model outcome on a global level. PD plots visualize the average effect features have on the prediction, and PFI estimates how much each feature improves the model performance and therefore how relevant a feature is. However, PD and PFI merely describe the prediction (or classification) function, but lack a theory that connects them to the data generating process. Treating PD and PFI as statistical estimators (like coefficients in a regression model) would require a theoretical counterpart in the DGP: a ground truth estimand that these interpretation methods are supposed to retrieve. Furthermore, for proper inference about the DGP, we need to quantify the uncertainty of PD and PFI estimators. Linear regression models, for exam- 

Relating PDP and PFI to the Data Generating Process 

3 

ple, provide variance estimates for the coefficients, which help to distinguish true effects from randomness and allow confidence interval estimation and hypothesis testing. Most machine learning approaches, however, do not provide variance estimates for their predictions or model parameters. Yet, the training process itself can be a relevant source of variance as the trained model heavily depends on the specific training data. 

We propose to treat PD and PFI as statistical estimators of a ground truth, which allows us to relate the model interpretation to the data generating process. In Section 2, we introduce related work and in Section 3 we introduce notation and background on PD and PFI. In Section 4, we formulate PD and PFI as estimators of (proposed) ground truth estimands in the DGP. By treating PD and PFI as statistical estimators, we can apply the bias and variance decomposition and identify the different sources of uncertainty. To reflect the different uncertainty sources, we distinguish between model-PD/PFI and learner-PD/PFI. The model-PD/PFI (Section 6) follows the standards definitions of PD and PFI. We propose confidence intervals and variance estimators for model-PD/PFI and show that they neglect the model variance originating from the training process. In Section 7, we propose the learner-PD and learnerPFI which take the model variance into account, study their statistical biases and propose variance estimators and confidence intervals. For models that lack variance estimates, multiple model refits are required to capture the variance due to the learning process. Data size is often a limiting factor, so that model refits are based on resampled data with overlapping observations. This overlap can lead to an underestimation of variance and thus to confidence intervals that are too narrow. We leverage a variance correction approach from model performance estimation to improve the variance estimation. In Section 8, we analyze the coverage of the confidence intervals for learner-PD and learner-PFI with and without the correction. In the application in Section 9 we demonstrate the use of confidence intervals for PD and PFI and illustrate the importance of taking the model variance into account. 

# **2 Related Work** 

For PD plots, model-specific confidence intervals exist that rely on models with inherent variance estimators such as Bayesian additive regression trees (Cafri and Bailey, 2016; Zhao and Hastie, 2021). Furthermore, various applied articles contain computations of PD confidence bands (Bair et al., 2013; Grange and Carslaw, 2019; Esselman et al., 2015; Emrich and Pierdzioch, 2016; Page et al., 2018; Obringer and Nateghi, 2018). These approaches either quantify only the error due to Monte Carlo approximation or, when they cover model variance, they do not account for underestimation of the variance. This demonstrates the need for a theoretical underpinning of this inferential tool for practical research. For PFI and related approaches, multiple suggestions for confidence intervals and variance estimation are available. Some contributions are specific to the random forest PFI (Ishwaran and Lu, 2019; Archer and Kimes, 2008; 

Christoph Molnar et al. 

4 

Janitza et al., 2018), for which a test for null importance was proposed by Altmann et al. (2010). 

Model-agnostic PFI confidence intervals that are similar to ours are proposed by Watson and Wright (2019); Williamson et al. (2019, 2020). We additionally correct for variance underestimation arising from resampling (Nadeau and Bengio, 2003) and relate the estimators to the proposed ground truth PFI. An alternative approach for providing bounds on PFI is proposed by Fisher et al. (2019) via Rashomon sets, which are sets of models with similar near-optimal prediction accuracy. Furthermore, alternative approaches of “model-free” inference exist (Parr et al., 2020; Parr and Wilson, 2019; Zhang and Janson, 2020), which aim to infer properties of the data without an intermediary ML model. 

# **3 Background and Notation** 

We denote the joint distribution induced by the data generating process as P _XY_ , where _X_ is a _p_ -dimensional random variable and _Y_ a 1-dimensional random variable. We describe the true mapping from features _X_ to the target _Y_ with _f_ ( _X_ ) = E[ _Y |X_ = _x_ ]. We denote a single random draw from the DGP with _x_<sup>(</sup><sup>_i_)</sup> and _y_<sup>(</sup><sup>_i_)</sup> . A dataset consisting of multiple draws from P _XY_ will be called _Dn_ = _{_ ( _x_<sup>(1)</sup> _, y_<sup>(1)</sup> ) _, . . . ,_ ( _x_<sup>(</sup><sup>_n_)</sup> _, y_<sup>(</sup><sup>_n_)</sup> ) _}_ , where _n_ is the number of samples and with each ( _x_<sup>(</sup><sup>_i_)</sup> _, y_<sup>(</sup><sup>_i_)</sup> ) _∼_ P _XY_ , _i ∈{_ 1 _, . . . , n}_ . An ML model _f_<sup>ˆ</sup> is a function ( _f_<sup>ˆ</sup> : _X →Y_ ) that maps a feature vector to a prediction (e.g. _Y_ = R for regression). The model _f_<sup>ˆ</sup> is induced based on a dataset _Dn_ , using a loss function _L_ : _Y×_ R<sup>_p_</sup> _→_ R<sup>+</sup> 0<sup>. As the true function</sup><sup>_f_is unknown, the model</sup><sup>_f_ˆis interpreted</sup> instead of _f_ , for example, with PD plots and PFI. The model _f_<sup>ˆ</sup> is learned by an ML learner _I_ : _D × Λ →H_ that maps from the space of datasets and the space of hyperparameters _Λ_ to the function hypothesis space _H_ . The learning process contains two sources of randomness: the training data being a random sample from P _XY_ and (possibly) the inherent randomness of the training process (Bouthillier et al., 2021).<sup>1</sup> Thus, a model _f_<sup>ˆ</sup> can be seen as realization of a random variable _F_ with distribution P _F_ . We assume that the model is evaluated with a risk function _R_ ( _f_<sup>ˆ</sup> ) = E _XY_ [ _L_ ( _Y, f_<sup>ˆ</sup> ( _X_ ))] = � _L_ ( _y, f_<sup>ˆ</sup> ( _x_ ))dP _XY_ , based on a loss function _L_ . To get unbiased estimates of the risk, model training and evaluation use different datasets. The dataset _Dn_ is split into _Dn_ 1 for model training and _Dn_ 2 for evaluation, with _n_ 1 + _n_ 2 = _n_ . The empirical risk <u>1</u> is estimated with _R_<sup>ˆ</sup> ( _f_<sup>ˆ</sup> _Dn_ 2 _,λ_ ) := _n_ 2 � _ni_ =12<sup>_L_</sup> � _y_<sup>(</sup><sup>_i_)</sup> _, f_<sup>ˆ</sup> _Dn_ 2 _,λ_ ( _x_<sup>(</sup><sup>_i_)</sup> )�. 

We distinguish between the ”simulation” and the ”real world” scenario (Hothorn et al., 2005). In the simulation scenario, we can generate a quasiinfinite number of datasets, which allows us to refit the model multiple times using fresh data each time. In the real world setting, we assume that a single dataset of size _n_ is available. To fit multiple models (of the same class) and to 

> 1 For example, stochastic gradient descent and weight initialization in neural networks or bootstrap and feature sampling in random forests are sources of randomness. 

Relating PDP and PFI to the Data Generating Process 

5 

obtain multiple estimates of the risk, resampling techniques such as bootstrapping, cross-validation and repeated subsampling have to be used. We denote by _Bd_ the set of indices for the training data in the _d_ -th split repetition and with _B−d_ the corresponding test data indices, where _Bd ∪ B−d_ = _{_ 1 _, . . . , n}_ , _b ∈{_ 1 _, . . . , m}_ , and _m_ is the number of models trained with different data. 

We distinguish between the interpretation of a single model and the distribution of models produced by a learner. Often a fixed trained model _f_<sup>ˆ</sup> is the subject of interpretation. Any interpretation of a fixed model neglects the model variance originating from the learning process. Often we are interested in extending the interpretation to the distribution of models produced by a learner. For example, the importance of a feature in a decision tree might be zero because it was never selected for a split. However, if we were to train the tree on a slightly different sample from the same distribution, it might obtain a non-zero importance. A similar distinction between model and learner can be made for performance estimation, where model performance is estimated with a test set, but learner performance requires averaging performance over _m_ repetitions and thus model refits. 

# 3.1 Partial Dependence (PD) 

The partial dependence function (Friedman, 1991) of a model _f_<sup>ˆ</sup> describes the expected effect of a feature after marginalizing out the effects of all other features. Partial dependence of a feature set _XS_ , _S ⊆{_ 1 _, . . . , p}_ (usually _|S|_ = 1) is defined as: 



where _XC_ are the remaining features so that _S ∪C_ = _{_ 1 _, . . . , p}_ and _S ∩C_ = _∅_ . The PD is estimated using Monte Carlo integration: 



For simplicity, we write _PD_ instead of _PDS_ , and _PD_<sup>�</sup> instead of _PD_<sup>�</sup> _S_ when we refer to an arbitrary PD. The PD plot consists of a line connecting the points _{_ ( _x_<sup>(</sup><sup>_g_)</sup> _, PD_<sup>�</sup> _S_ ( _x_<sup>(</sup><sup>_g_)</sup> ) _}_<sup>_G_</sup> _g_ =1<sup>,with</sup><sup>_G_gridpointsthatareusuallyequidistant</sup> or quantiles of P _XS_ . See Figure 6 for an example of a PD plot. 

# 3.2 Permutation Feature Importance (PFI) 

The PFI (Breiman, 2001; Fisher et al., 2019) of a model _f_<sup>ˆ</sup> is defined as the increase in loss _L_ when the feature set _XS_ (usually just one feature) is permuted: 



Christoph Molnar et al. 

6 

where _X_<sup>˜</sup> _S_ is a random variable based on the distribution of _XS_ . There are two versions of PFI, the marginal PFI and the conditional PFI, which have different strategies to replace _XS_ and also different interpretations. The marginal PFI can be interpreted as the importance of the feature, ignoring dependencies with other features and also ignoring that the data used may differ greatly from the original joint distribution P _X_ (extrapolation). For the marginal PFI we take the expected value over the distribution P _XS ·_ P _XC Y_ , which means that _X_<sup>˜</sup> _S_ follows the marginal distribution of _XS_ and is independent of _XC_ and _Y_ ( _X_<sup>˜</sup> _S XC, Y_ ). This means that the marginal PFI breaks the association between the feature(s) _XS_ and the target _Y_ , but also between _XS_ and all other features _XC_ . For the conditional PFI (cPFI) (Molnar et al., 2020; Watson and Wright, 2019; Hooker and Mentch, 2019; Cand`es et al., 2018), the expectation is taken over the distribution P _XS |XC ·_ P _XC Y_ , so that _X_<sup>˜</sup> _S_ follows the conditional distribution of _XS_ given _XC_ but is still independent of _Y_ . The interpretation of the conditional PFI of a feature is therefore also conditional on all features that are correlated with the feature of interest. Conditional PFI may be interpreted as the _additional_ importance of a feature _given that we already know the other feature values_ . 

PFI and cPFI are estimated with Monte Carlo integration: 



where ˜ _x_<sup>(</sup> _S_<sup>_k,i_)</sup> with _k ∈{_ 1 _, . . . , l}_ is the _k_ -th sample of _xS_ for the _i_ -th observation. For the marginal PFI, ˜ _x_<sup>(</sup> _S_<sup>_k,i_)</sup> can be a permutation of the original vector _xS_ . The conditional PFI requires a conditional sampling mechanism for the feature, such as subgroups (Molnar et al., 2020) or knockoffs (Cand`es et al., 2018; Watson and Wright, 2019). The estimation of _PFI_<sup>�</sup> requires unseen data, so that the loss estimates deliver unbiased results (Zheng and van der Laan, 2011; Chernozhukov et al., 2018). If not stated otherwise, mathematical derivations in this paper apply to both marginal and conditional PFI. We assume that the loss used for PFI can be computed per instance, which excludes losses such as AUC. See Figure 6 for a PFI example. As with PD, we use _PFI_ instead of _PFIS_ and _PFI_<sup>�</sup> instead of _PFI_<sup>�</sup> _S_ s. 

# **4 Relating Model to Data Generating Process** 

The goal of statistical inference is to gain knowledge about the DGP. Therefore, the modeler aims to establish relationships between properties of the model and the DGP. For example, under certain assumptions, the coefficients of a generalized linear model (= model properties) can be related to parameters of the respective conditional distribution defined by the DGP, such as conditional mean and covariance structure (= DGP properties). Machine learning models such as random forests or neural networks lack such a mapping between learned 

Relating PDP and PFI to the Data Generating Process 

7 

model parameters and properties of the data generating process. This lack of counterparts in the DGP make it difficult to interpret complex machine learning models and to draw conclusions about the real world. Interpretation methods such as PD and PFI provide **external descriptors** of how features affect the model predictions. Howerver, PD and PFI are estimators that lack a counterpart estimand in the DGP. We propose an inference approach for these external descriptors. We define a ground truth version of PD and PFI directly on the DGP, namely the DGP-PD and the DGP-PFI. The DGP-PD and the DGP-PFI are defined as the PD and PFI, but applied to the true function _f_ instead of _f_<sup>ˆ</sup> . This means that the DGP-PD becomes the feature effect of features _XS_ on the underlying function _f_ : 

**Definition 1 (DGP-PD)** The DGP-PD is the PD applied to function _f_ : _X �→Y_ of the data generating process. 



Similarly, for the DGP-PFI we replace _f_<sup>ˆ</sup> for _f_ and compute the expected losses. We compute the difference between the loss for the permuted distribution and the loss on the joint distribution. Since we work with the true _f_ , the “original” loss is the aleatoric uncertainty (without any bias or variance). 

**Definition 2 (DGP-PFI)** The DGP-PFI is the PFI applied to function _f_ : _X �→Y_ of the data generating process. 



The function _f_ is usually unknown. If it were known in an application, we would not need machine learning in the first place. However, Definitions 1 and 2 immediately enable at least two useful applications: It allows scientists to compare the PD/PFI of a model with the PD/PFI of the DGP **in simulation studies** and research statistical biases. More importantly, the ground truth definitions of DGP-PD and DGP-PFI allow us to treat PD and PFI as statistical estimators of properties of the data generating process. 

This paper studies PD and PFI as statistical estimators of the ground truth DPG-PD and DGP-PFI, including bias and variance decompositions, and confidence interval estimators. Whether the estimands themselves are desirable in specific data scenarios and model choices is out-of-scope for this work. Others have done work in limitations of PFI and PD: For example Molnar et al. (2020); Hooker and Mentch (2019); Strobl et al. (2008) show that interpretation methods produce misleading results under strongly dependent features (e.g. large correlation between features), Zhao and Hastie (2021) assess whether PDs can be used to estimate causal effects, and Groemping (2020) studied whether PDs recover the linear relationship of the DGP when the relationship between target and features is linear. Extrapolation when features are dependent might be one of the biggest issue for PD and PFI. As one possible remedy, conditional variants of PDP and PFI (Molnar et al., 2020; Fisher 

Christoph Molnar et al. 

8 



<!-- Start of picture text -->
Bias Variance MC �<br>DGP-PD learner-PD model-PD PD<br>Model Bias Model Variance<br>f E[  f ˆ ] f ˆ<br>Bias Variance MC �<br>DGP-PFI learner-PFI model-PFI PFI<br><!-- End of picture text -->

**Figure** _PFI_ � estimates **1** A modeldeviate _f_<sup>ˆ</sup> deviatesfrom theirfromground _f_ due truthto modelversionsbias andDGP-PDvariance.and SimilarlyDGP-PFI _PD_<sup>�</sup> dueandto bias, variance, and Monte Carlo integration (MC). 

et al., 2019; Watson and Wright, 2019; Apley and Zhu, 2020) have been proposed. For PD, the conditional variant is also called M-Plot (Apley and Zhu, 2020) and weights predictions according to how likely their respective feature values are for a given PD grid point. Our proposed variance and confidence interval estimators and other results apply to both the original and conditional variants of PD and PFI, if not stated otherwise. 

# **5 Bias-Variance Decomposition** 

The definition of DGP-PD and DGP-PFI gives us a ground truth to which the PD and PFI of a model can be compared – at least in theory and simulation. The error of the estimation (mean squared error between estimator and estimand) can be decomposed into the systematic deviation from the true estimand (statistical bias) and the variance due to model variance. PD and PFI are both expectations over the – usually unknown – joint distribution of the data. The expectations are therefore usually estimated from data using Monte Carlo integration, which adds another source of variance to the PFI and PD estimates. Figure 1 visualizes the chain of errors that stand between the estimand (DGP-PD,DGP-PFI) and the estimates ( _PD_<sup>�</sup> , _PFI_<sup>�</sup> ). For the PD, we compare the MSE between the true DGP-PD ( _PDf_ as defined in Equation 1) with the theoretical PD of a model instance _f_<sup>ˆ</sup> ( _PDf_ ˆ<sup>)</sup> at position x. 



Here, _F_ is the distribution of the trained models, which can be treated as a random variable. The bias-variance decomposition of the MSE of estimators is a well known result (Geman et al., 1992). For completeness, we provide a proof in Appendix A. Figure 2 visualizes bias and variance of a PD curve, and the variance due to Monte Carlo integration. 

Similarly, the MSE of the theoretical PFI of a model (Equation 3) can be decomposed into squared bias and variance. The proof can be found in 

Relating PDP and PFI to the Data Generating Process 

9 



<!-- Start of picture text -->
Uncertainty due to Monte Carlo integration Bias and variance<br>6 6<br>4 4<br>2 2<br>0 0<br>0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0<br>x1 x1<br>PD PD<br><!-- End of picture text -->

**Figure 2** Illustration of bias, variance and Monte Carlo approximation for the PD. Left: Various PDPs using different data for the Monte Carlo integration, but keeping the model fixed. Right: The green dashed line shows the DGP-PD plot of a toy example. Each thin line is the PD plot for the model fitted with a different sample, and the thick blue line is the average thereof. Deviation of the expected PDP from the DGP-PDP are due to bias, deviations of the individual model-PDPs to the expected PDP are due to model variance. 

Appendix B. 



The model variance of PD/PFI stems from variance in the model fit, which depends on the training sample _D_ and on randomness in the model training such as weight initialization or feature and observation sampling. When constructing confidence intervals, we have to take into account the variance of PFI and PDP across model fits, and not just the error due to Monte Carlo integration. As we show in an application (Section 9), whether PD and PFI are based on a single model or are averaged across model refits can impact the interpretation, and especially the certainty of the interpretation. We therefore distinguish between model-PD/PFI and learner-PD/PFI, which are averaged over refitted models. Variance estimators for model-PD/PFI only account for variance due to Monte Carlo integration. 

# **6 Model-PD and Model-PFI** 

In this section, we study the model-PD and the model-PFI, and provide variance and confidence interval estimators. With model-PD and model-PFI, we refer to the original proposals for PD (Friedman, 1991) and PFI (Breiman, 2001; Fisher et al., 2019) for fixed models. Conditioning on a given model _f_<sup>ˆ</sup> ignores the model variance due to the learning process. Only the variance due to Monte Carlo integration can considered in this case. 

The model-PD estimator (Equation (2)) is unbiased regarding the theoretical model-PD (Equation (1)). Also, the estimated model-PFI (Equation 4) is unbiased with respect to the theoretical model-PFI (Equation 3). These 

Christoph Molnar et al. 

10 

findings are general properties of Monte Carlo integration, which state that Monte Carlo integration converges to the integral due to the law of large numbers. Proofs can be found in Appendix C and E. In addition, model-PD and model-PFI are unbiased estimator of the DGP-PD (Theorem 1) and DGP-PFI (Theorem 2), under certain conditions. 

To quantify the variance due to Monte Carlo integration and to construct confidence intervals, we calculate the variance across the test data instances. For the model-PD, the variance can be estimated with: 



Similarly, for the model-PFI the variance is: 



where _L_<sup>(</sup><sup>_i_)</sup> =<sup><u>1</u></sup> _l_ � _lk_ =1<sup>_L_(</sup><sup>_y_(</sup><sup>_i_)</sup><sup>_,f_ˆ(˜</sup><sup>_x_(</sup> _S_<sup>_k,i_)</sup> _, x_<sup>(</sup> _C_<sup>_i_)))</sup><sup>_−L_(</sup><sup>_y_(</sup><sup>_i_)</sup><sup>_,f_ˆ(</sup><sup>_x_(</sup><sup>_i_))).</sup> Model-PD and model-PFI are mean estimates of independent samples with estimated variance. As such, they follow a t-distribution with _n_ 2 _−_ 1 degrees of freedom. This allows us to construct point-wise confidence bands for the model-PD and confidence intervals for the model-PFI, that capture the Monte Carlo approximation uncertainty. We define point-wise _α_ -confidence bands around the estimated model-PD: 



where _t_ 1 _−_ _<u>α</u>_ 2<sup>isthe1</sup><sup>_−α/_2quantileofthet-distributionwith</sup><sup>_n_2</sup><sup>_−_1degrees</sup> of freedom. We proceed in the same manner for PFI: 



Confidence intervals for model-PD and model-PFI ignore the model variance. The interpretation, therefore, is limited to variance regarding the Monte Carlo approximation, and we cannot generalize results to the data generating process. Model-PD/PFI and its confidence bands/intervals are applicable when the focus is a fixed model (e.g. in a model audit). 

# **7 Learner-PD and Learner-PFI** 

To account for the model variance, we propose the learner-PD and the learnerPFI, which average the PD/PFI over _m_ model fits _f_<sup>ˆ</sup> _d, d ∈{_ 1 _, . . . , m}_ produced by the same learning algorithm, but trained on different data samples. The 

Relating PDP and PFI to the Data Generating Process 

11 

learner-variants are averages of the model-variants, where for each modelPD/PFI the model is repeatedly “sampled” from the distribution of models. 

The learner-PD is therefore the expected PD over the distribution of models generated by the learning process: E _F_ [ _PD_ ( _x_ )]. We estimate the learner-PD with: 



where _f_<sup>ˆ</sup> _d_ is trained on sample indices _Bd_ and the PD estimated using samples _B−d_ so that _Bd ∩ B−d_ = _∅_ . 

Following the PD, the learner-PFI is the expected PFI over the distribution of models produced by the learner: E _F_ [ _PFI_ ]. We propose the following estimator for the learner-PFI: 



where losses _L_<sup>(</sup> _d_<sup>_i_)</sup> = _L_ ( _y_<sup>(</sup><sup>_i_)</sup> _, f_<sup>ˆ</sup> _d_ ( _x_<sup>(</sup><sup>_i_)</sup> )) and _L_<sup>¯˜(</sup> _d_<sup>_i_)</sup> =<sup><u>1</u></sup> _l_ � _lk_ =1<sup>_L_(</sup><sup>_y_(</sup><sup>_i_)</sup><sup>_,f_ˆ</sup><sup>_d_(˜</sup><sup>_x_(</sup> _S_<sup>_k,i_)</sup> _, x_<sup>(</sup> _C_<sup>_i_)))</sup> are estimated with data _B−d_ for a model trained on data _Bd_ . Marginal and conditional versions can also be distinguished for the learner-PFI, depending on how _X_<sup>˜</sup> _S_ was sampled. A similar estimator has been proposed by Janitza et al. (2018) for random forests. 

# 7.1 Bias of Learner-PD 

The learner-PD is an unbiased estimator of the expected PD over the distribution of models _F_ , since E _F_ [ _PD_ �( _x_ )] = E _F_ � _m_ <u>1</u> � _md_ =1 _PD_<sup>�</sup> _d_ ( _x_ )� =<sup>_<u>m</u>_</sup> _m_<sup>E</sup><sup>_F_[</sup><sup>_PD_</sup> _f_<sup>ˆ(</sup><sup>_x_)] =</sup> E _F_ [ _PDf_ ˆ<sup>(</sup><sup>_x_)].Thebiasofthelearner-PD</sup><sup>_regardingtheDGP-PD_islinkedto</sup> the bias of the model. If the ML model is unbiased, the PDs are unbiased as well. 

**Theorem 1** _Model unbiasedness implies PD unbiasedness:_ E _F_ [ _f_<sup>ˆ</sup> ( _x_ )] = _f_ ( _x_ ) = _⇒_ E _F_ [E _XC_ [ _f_<sup>ˆ</sup> ]] = E _XC_ [ _f_ ] 

**Proof Sketch 1** _Applying Fubini’s Theorem allows us to switch the order of integrals. Further replacing_ E _F_ [ _f_<sup>ˆ</sup> ] _with f proves the unbiasedness. A full proof can be found in Appendix D._ 

By model bias, we refer to the deviation between the estimated _f_<sup>ˆ</sup> and _f_ . Inductive bias, i.e. the preference of one generalization over another, is necessary for learning (Mitchell, 1980). A wrong choice of inductive bias, such as assuming a linear _f_<sup>ˆ</sup> for a non-linear _f_ , leads to deviations of _f_<sup>ˆ</sup> from _f_ . But there are also other reasons why a bias of _f_<sup>ˆ</sup> from _f_ may occur, for example a too small training data size. We discuss the critical assumption of model unbiasedness further in Section 10. 

Christoph Molnar et al. 

12 

# 7.2 Bias of Learner-PFI 

The learner-PFI is unbiased regarding the expected learner-PFI over the distribution of models _F_ , since the learner-PFI is a simple mean estimate. However, unlike the learner-PD, model unbiasedness does not, in general, imply unbiasedness of the learner-PFI _regarding the DGP-PFI_ . In the following, we study the PFI bias when the squared error is used for loss _L_ (L2-loss). 

**Theorem 2** _If model f_<sup>ˆ</sup> _is unbiased with_ E _F_ [ _f_<sup>ˆ</sup> ] = _f and the L2-loss is used, then the conditional model-PFI and conditional learner-PFI are unbiased estimators of the conditional DGP-PFI._ 

**Corollary 1** _If model f_<sup>ˆ</sup> _is unbiased, the L2-loss is used and the features XS are independent of features XC, then the marginal model-PFI and marginal learner-PFI are unbiased estimators of the DGP-PFI. If the features are dependent, the following bias is introduced: PFIf_ ˆ<sup>_−DGP-PFI_= E</sup> _X_<sup>˜</sup> _S X_<sup>[V</sup><sup>_F_[ ˆ</sup><sup>_f_]]</sup><sup>_−_</sup> E _X_ [V _F_ [ _f_<sup>ˆ</sup> ]] _._ 

**Proof Sketch 2** _Both L and L_<sup>˜</sup> _can be decomposed into bias, variance, and irreducible error. Due to the subtraction, the irreducible error vanishes and the differences of biases and variances remain. Model unbiasedness sets the bias terms to zero, but the difference in variance only becomes zero if either XS XC or conditional PFI is used. The extended proof can be found in Appendix F._ 

Sampling feature _XS_ creates a new distribution ( _X_<sup>˜</sup> _S, XC_ ), with a (possibly) different variance for a given point across models. If the variance of _f_<sup>ˆ</sup> changes for _X_<sup>˜</sup> _S_ , this leads to a bias in the PFI estimate. Besides this bias due to the extrapolation variance, the assumption of model unbiasedness is critical or even unreasonable for regions outside of P _XY_ , since there is no feedback whether the model matches the DGP in these regions. Furthermore, the DGP might have a probability density of zero for regions of extrapolation. This means that the marginal PFI for dependent features can have a conceptual problem, as the permutation might create data points that are in conflict with the DGP (Hooker and Mentch, 2019; Molnar et al., 2020).<sup>2</sup> 

Intuitively, the model-PFI and learner-PFI should tend to have a negative bias and therefore underestimate the DGP-PFI. A model cannot use more information about the target than is encoded in the DGP (except for dependent features in combination with marginal PFI). However, as Theorem 3 shows the (conditional) PFI can be larger than the DGP-PFI. 

**Theorem 3** _The difference between the conditional PFI (cPFIf_ ˆ<sup>_) and the con-_</sup> _ditional DGP-PFI (cPFIf ) of a model f_<sup>ˆ</sup> _is given by:_ 



Relating PDP and PFI to the Data Generating Process 

13 

**Proof Sketch 3** _For the L2 loss, the expected loss of a model f_<sup>ˆ</sup> _can be decomposed into the expected loss between f_<sup>ˆ</sup> _and f and the expected variance of Ycangivenbe simplifiedX. Due usingto thethatsubtraction,Y X_ ˜ _S |theXClatterand Pterm_ ( _X_<sup>˜</sup> _S, Xvanishes.C_ ) = _P The_ ( _XS, XremainderC_ ) _. The extended proof can be found in Appendix G._ 

However, for an overestimation of the PFI to occur, the expected conditional variance of _f_<sup>ˆ</sup> must be greater than the one of _f_ . Moreover, _f_<sup>ˆ</sup> and _f_ must have a large expected conditional covariance, meaning that _f_<sup>ˆ</sup> has learned something about _f_ . 

# 7.3 Variance Estimation 

The learner-PD and learner-PFI vary due to model variance (refitted models), but also due to using different samples each time for the Monte Carlo integration. Their variance estimates therefore capture the entire modeling process. Insofar, learner-PD/PFI along with their variance estimators bring us closer to the DGP-PD/PFI and only the systematic bias remains unknown. 

We can estimate this point-wise variance of the learner-PD with: 



And equivalently for learner-PFI: 



The correction term _c_ depends on the data setting. In simulation settings that allow us to draw new training and test sets for each model, we can use _c_ = 0, yielding the standard variance estimators. In real world settings, we usually have a fixed dataset of size _n_ and models are refitted using resampling techniques. Consequently, data are shared by model refits and variance estimators will underestimate the true variance (Nadeau and Bengio, 2003). To correct the variance estimate of the generalization error for bootstrapped or subsampled models, Nadeau and Bengio (2003) suggested the correction term _c_ = _n_<sup>_<u>n</u>_</sup> 1<sup><u>2</u>(where</sup><sup>_n_2and</sup><sup>_n_1aresizesoftestandtrainingdata).However,</sup> the correction remains a rough correction, relying on the strongly simplifying assumption that the correlation between model refits depends only on the number of shared observations in the respective training datasets, and not on the specific observations that they share. While this assumption is usually wrong, we show in Section 8 that the correction term offers a vast improvement for variance estimation – compared to using no correction. 

Christoph Molnar et al. 

14 

# 7.4 Confidence Bands and Intervals 

Since learner-PD and learner-PFI are means with estimated variance, we can use the t-distribution with _m −_ 1 degrees of freedom to construct confidence bands/intervals, where _m_ is the number of model fits. The point-wise confidence band for learner-PD is: 



where _t_ 1 _−_ _<u>α</u>_ 2<sup>istherespective1</sup><sup>_−α/_2quantileofthet-distributionwith</sup> _m −_ 1 degrees of freedom. Equivalently, we propose a confidence interval for the learner-PFI: 



Respecting the model variance can make a difference in the interpretation as we show in the application, Section 9. Resampling strategies make better use of the data, in the sense that a bigger share of the data ends up being used as test data compared to the holdout strategy. 

# **8 Confidence Interval Coverage Simulation** 

In simulations we compared confidence interval performance between bootstrapping and subsampling, with and without variance correction. We simulated two data generating processes: a _linear_ DGP was defined as _y_ = _f_ ( _x_ ) = _x_ 1 _− x_ 2 + _ϵ_ and a _non-linear_ DGP as _y_ = _f_ ( _x_ ) = _x_ 1 _−_<sup>_√_</sup> 1 _− x_ 2 + _x_ 3 _· x_ 4 + ( _x_ 4 _/_ 10)<sup>2</sup> + _ϵ_ . All features were uniformly sampled from the unit interval [0; 1] and for both DGPs we set _ϵ ∼ N_ (0 _,_ 1). We studied the two settings “simulation” and “real world”. In both settings, we trained (each 15 times) linear models (lm), regression trees (tree) and random forests (rf), and computed confidence intervals for learner-PD and learner-PFI across the 15 refitted models. In the “simulation” setting, we sampled _n ∈{_ 100 _,_ 1 _,_ 000 _}_ fresh data points for each model refit, where 63 _._ 2% of the data were used for training and the remaining 36 _._ 8% for PDP and PFI estimation. 

In the “real world” setting, we sampled _n ∈{_ 100 _,_ 1 _,_ 000 _}_ data points **once** per experiment, and generated 15 training data sets using bootstrap (sample size _n_ with replacement, which yields 0 _._ 632 _· n_ unique data points in expectation) or subsampling (sample size 0 _._ 632 _· n_ without replacement). In both settings, learner-PD and learner-PFI plus their respective confidence intervals were computed over the 15 retrained models. We repeated the experiment 10,000 times and counted how often the estimated confidence intervals covered the expected PD or PFI (E ˆ _f_<sup>[</sup><sup>_PD_]andE ˆ</sup> _f_<sup>[</sup><sup>_PFI_])overthedistributionof</sup> 

Relating PDP and PFI to the Data Generating Process 

15 

**Table 1** Coverage Probability of the 95% PDP Confidence Bands. boot = bootstrap, subs = subsampling, * = with adjustment. 

|dgp|model|n|boot|boot*|subs|subs*|ideal|
|---|---|---|---|---|---|---|---|
|linear|lm|100|0.41|0.89|0.34|0.82|0.95|
|linear|lm|1000|0.41|0.89|0.33|0.80|0.95|
|linear|rf|100|0.39|0.86|0.36|0.83|0.95|
|linear|rf|1000|0.38|0.87|0.35|0.83|0.95|
|linear|tree|100|0.54|0.96|0.47|0.92|0.95|
|linear|tree|1000|0.57|0.96|0.48|0.91|0.95|
|non-linear|lm|100|0.43|0.90|0.36|0.84|0.95|
|non-linear|lm|1000|0.41|0.89|0.33|0.81|0.95|
|non-linear|rf|100|0.39|0.87|0.36|0.84|0.95|
|non-linear|rf|1000|0.38|0.86|0.36|0.83|0.95|
|non-linear|tree|100|0.58|0.98|0.51|0.95|0.95|
|non-linear|tree|1000|0.59|0.97|0.51|0.94|0.95|



**Table 2** Coverage Probability of the 95% PFI Confidence Intervals. boot = bootstrap, subs = subsampling, * = with adjustment. 

|dgp|model|n|boot|boot*|subs|subs*|ideal|
|---|---|---|---|---|---|---|---|
|linear|lm|100|0.27|0.70|0.23|0.63|0.94|
|linear|lm|1000|0.25|0.68|0.21|0.60|0.95|
|linear|rf|100|0.44|0.92|0.39|0.88|0.95|
|linear|rf|1000|0.42|0.90|0.38|0.86|0.95|
|linear|tree|100|0.52|0.97|0.42|0.90|0.95|
|linear|tree|1000|0.42|0.90|0.34|0.81|0.95|
|non-linear|lm|100|0.31|0.81|0.25|0.72|0.94|
|non-linear|lm|1000|0.25|0.67|0.21|0.59|0.95|
|non-linear|rf|100|0.47|0.94|0.43|0.91|0.95|
|non-linear|rf|1000|0.41|0.89|0.38|0.86|0.95|
|non-linear|tree|100|0.68|0.99|0.56|0.96|0.94|
|non-linear|tree|1000|0.58|0.97|0.46|0.92|0.95|



models _F_ .<sup>3</sup> These expected values were computed using 10,000 separate runs. The coverage estimates were averaged across features per scenario, and, for PD also across grid points ( _{_ 0 _._ 1 _,_ 0 _._ 3 _,_ 0 _._ 5 _,_ 0 _._ 7 _,_ 0 _._ 9 _}_ for all features. 

Table 2 and Table 1 show that in the “simulation” setting (“ideal”), we can recover confidence intervals using the standard variance estimation with the desired coverage probability. However, in the “real-world”, setting the confidence intervals for both learner-PD and learner-PFI are too narrow across all scenarios and both resampling strategies, when the intervals are based on naive variance estimates. Some coverage probabilities are especially low, such as for linear models with 30% _−_ 40%. 

The coverage probabilities drastically improve when the correction term is used, see Figure 3. However, in the simulated scenarios, they are still somewhat too narrow. For the linear model, the confidence intervals were the most narrow 

> 3 The coverage is not regarding the DGP-PD/PFI, but regarding the expected learnerPD/PFI, as we studied the choices of resampling and correction for the model variance. 

Christoph Molnar et al. 

16 



<!-- Start of picture text -->
PD PFI<br>1.0<br>Variance corrected?<br>0.8 FALSE<br>TRUE<br>0.6<br>Resampling<br>0.4 boot<br>subs<br>0.2<br>0.0 0.3 0.6 0.9 0.0 0.2 0.4 0.6<br>CI width<br>CI coverage<br><!-- End of picture text -->

**Figure 3** Confidence interval width vs. coverage for _boot_ strapping and _subs_ ampling, comparing before and after correction. Segments connect identical scenarios. 



<!-- Start of picture text -->
PD PFI<br>1.0<br>0.8<br>Resampling<br>0.6 boot<br>subs<br>0.4<br>0.2<br>0.3 0.6 0.9 0.2 0.4 0.6<br>CI width<br>CI coverage<br><!-- End of picture text -->

**Figure 4** Confidence interval width vs. coverage for _boot_ strap and _subs_ ampling, both with correction. Segments connect identical scenarios. 

with coverage probabilities of around 80% _−_ 90% for PD and 60% _−_ 80% for PFI across DGPs and sample sizes. The PD confidence bands were not much affected by increasing sample size _n_ , but the PFI estimates became slightly more narrow in most cases. In the case of decision trees, the adjusted confidence intervals were sometimes too large, especially for adjusted bootstrap. 

Except for trees on the _non-linear_ DGP, bootstrap outperformed subsampling in terms of coverage, meaning the coverage was closer to the 95% level and rather erred on the side of “caution” with wider confidence intervals (see Figure 4). As recommended in Nadeau and Bengio (2003), we used 15 refits. We additionally analyzed how the coverage and interval width changed by increasing refits from 2 to 30 and noticed that the coverage worsened with more refits, while the width of the confidence intervals decreased. Increasing the number of refits comes with an inherent trade-off between interval width and coverage: The more refits are considered, the more accurate the learner-PFI and learner-PD become and also the more certain the variance estimates become, scaling with 1 _/m_ . But there is a limit to the information in the data, so 

Relating PDP and PFI to the Data Generating Process 

17 



<!-- Start of picture text -->
1.00<br>adjusted<br>1.0 0.75 FALSE<br>TRUE<br>0.50<br>Sampling Strategy<br>0.5 boot<br>0.25 ideal<br>subs<br>0.0 0.00<br>10 20 30 10 20 30<br>Number of Model Refits Number of Model Refits<br>non−linear non−linear<br>Confidence Interval Width<br>Confidence Interval Coverage<br><!-- End of picture text -->

**Figure 5** Average PD confidence band width (left) and coverage (right) as a function of number of refitted models for the random forest on the _non-linear_ DGP. 

that additional refits falsely reduce the variance estimate and the confidence intervals become too narrow. To refit the model 10 - 20 times seemed to be an acceptable trade-off between coverage and interval width, see for example Figure 5. Below _∼_ 10 refits, the confidence intervals were large, and also the mean PD/PFI estimates have a high variance. Above _∼_ 20 refits, the widths did not decrease by much anymore. The figures for the other scenarios can be found in Appendix H. With our simulation results we could show that confidence intervals using the naive variance estimation (without correction) results in way too narrow intervals. While the simple correction term by Nadeau and Bengio (2003) does not always provide the desired coverage probability, it is a vast improvement over the naive approach. We therefore recommend using the correction when computing confidence intervals for learner-PD and learner-PFI – it is currently the best approach available. We also recommend refitting the model around 15 times. For more “cautious” confidence intervals we recommend using confidence intervals based on resampling with replacement (bootstrap) over sampling wihtout replacement (subsampling). However, beside wider confidence intervals, the bootstrap requires additional attention when model tuning with internal resampling is used, as data points may otherwise end up in both training and validation data. 

# **9 Application** 

We apply our proposed estimators to predict wine quality (Cortez et al., 2009) ( _n_ = 1599) from physicochemical features such as alcohol content and acidity. We compared the performance (mean squared error) of a linear regression model, a regression tree (CART) (Breiman et al., 1984) and a random forest (Breiman, 2001) using 15 bootstrap samples (sample size _n_ with replacement). The MSEs for the different models were: 0.425 (Linear regression), 0.342 (Random Forest) and 0.456 (Tree).The random forest was significantly better than the other models based on an adjusted t-test of the performance difference (Nadeau and Bengio, 2003), with a 95% confidence interval of [-0.098;-0.069] 

Christoph Molnar et al. 

18 



<!-- Start of picture text -->
learner−PFI model−PFI<br>alcohol<br>sulphates<br>vol.acid<br>total.SO2<br>density<br>citric.acid<br>chlorides<br>pH<br>fixed.acid<br>free.SO2<br>res.sugar<br>0.00 0.05 0.10 0.15 0.00 0.05 0.10 0.15<br>Permutation Feature Importance (MSE)<br>learner−PDP model−PDP<br>6.3<br>6.0<br>5.7<br>5.4<br>5.1<br>10 12 14 10 12 14<br>alcohol<br>PD<br><!-- End of picture text -->

**Figure 6** Top: Lerner-PFI and model-PFI with point-wise 95%-confidence intervals for the random forest. Bottom: Lerner-PDP and model-PDP with point-wise 95%-confidence bands for the random forest and feature ”alcohol”. 

for the difference to the linear model MSE and [-0.158;-0.071] for the difference to the decision tree. We reused the 15 random forests from the bootstrap to estimate the learner-PD and learner-PFI including their confidence intervals based on adjusted variance estimates. Figure 6, top row, shows that the most important features were alcohol, sulphates and volatile acidity. The model-PFI quantifies how important each feature was for a fixed random forest, and the confidence intervals show the variance of the approximation of the model-PFI due to Monte Carlo integration. The model-PFI, however, cannot tell us how much the estimate varies due to model variance. The learner-PFI quantifies this model variance. Both model-PFI and learner-PFI gave a similar ordering for the top features. The learner-PFI shows that alcohol is more important than sulphates (with no overlap in the confidence intervals), for which the model-PFI would suggest that the importance is almost equal. 

Figure 6, bottom row, shows both the model-PDP and the learner-PDP for the alcohol feature. Notably, the confidence bands of the learner-PDP are wider than of the model-PDP. Especially for very low and for high alcohol volumes the models have a high variance. Neglecting the model variance would mean being overconfident about the partial dependence curve. In particular, the Monte Carlo approximation error decreases with 1 _/n_ as the sample size _n_ for PD and PFI estimation increases. Wrongly interpreted, this can lead to a 

Relating PDP and PFI to the Data Generating Process 

19 

false sense of confidence in the estimated effects and importance, even though only one model is considered and model variance is ignored. 

# **10 Discussion** 

We related the PD and the PFI to the data generating process (DGP), proposed variance and confidence intervals, and discussed conditions for inference. Our derivations were motivated by taking an external view of the statistical inference process, and postulating that there is a ground truth counterpart to PD/PFI in the data generating process. To the best of our knowledge, statistical inference via model-agnostic interpretable machine learning is already used in practice, but under-explored in theory. 

A critical assumption for inference of effects and importance using interpretable machine learning is unbiasedness of the model. The model bias is difficult to test, and can be introduced by, e.g. choice of model class, regularization and feature selection. For example, regularization techniques such as LASSO introduce a small bias _on purpose_ (Tibshirani, 1996) to decrease model variance and improve predictive performance. We have to better understand how specific biases affect the prediction function and therefore PD and PFI estimates. Another crucial limitation for inference of PD and PFI is the underestimation of variance due to data sharing between model refits. While we could show that a simple correction of the variance (Nadeau and Bengio, 2003) vastly improves the coverage, a proper estimation of the variance remains an open issue. A promising approach relying on repeated nested cross validation to correctly estimate the variance was recently proposed by Bates et al. (2021). However, this approach is more computationally intensive by up to a factor of 1,000. 

# **References** 

- Altmann A, Tolo¸si L, Sander O, Lengauer T (2010) Permutation importance: a corrected feature importance measure. Bioinformatics 26(10):1340–1347 

- Apley DW, Zhu J (2020) Visualizing the effects of predictor variables in black box supervised learning models. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 82(4):1059–1086 

- Archer KJ, Kimes RV (2008) Empirical characterization of random forest variable importance measures. Computational Statistics & Data Analysis 52(4):2249–2260 

- Bair E, Ohrbach R, Fillingim RB, Greenspan JD, Dubner R, Diatchenko L, Helgeson E, Knott C, Maixner W, Slade GD (2013) Multivariable modeling of phenotypic risk factors for first-onset tmd: the oppera prospective cohort study. The Journal of Pain 14(12):T102–T115 

- Bates S, Hastie T, Tibshirani R (2021) Cross-validation: what does it estimate and how well does it do it? arXiv preprint arXiv:210400673 

Christoph Molnar et al. 

20 

Boulesteix AL, Wright MN, Hoffmann S, K¨onig IR (2020) Statistical learning approaches in the genetic epidemiology of complex diseases. Human Genetics 139(1):73–84 

Bouthillier X, Delaunay P, Bronzi M, Trofimov A, Nichyporuk B, Szeto J, Sepah N, Raff E, Madan K, Voleti V, et al. (2021) Accounting for variance in machine learning benchmarks. arXiv preprint arXiv:210303098 

Breiman L (2001) Random forests. Machine Learning 45(1):5–32 

Breiman L, Friedman JH, Olshen RA, Stone CJ (1984) Classification and Regression Trees. CRC Press, Boca Raton 

Cafri G, Bailey BA (2016) Understanding variable effects from black box prediction: Quantifying effects in tree ensembles using partial dependence. Journal of Data Science 14(1):67–95 

Cand`es E, Fan Y, Janson L, Lv J (2018) Panning for gold: ‘model-X’ knockoffs for high dimensional controlled variable selection. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 80(3):551–577 

Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, Robins J (2018) Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal 21(1):C1–C68 

Cortez P, Cerdeira A, Almeida F, Matos T, Reis J (2009) Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems 47(4):547–553 

Emrich E, Pierdzioch C (2016) Public goods, private consumption, and human capital: Using boosted regression trees to model volunteer labour supply. Review of Economics/Jahrbuch f¨ur Wirtschaftswissenschaften 67(3) 

Esselman PC, Stevenson RJ, Lupi F, Riseng CM, Wiley MJ (2015) Landscape 

prediction and mapping of game fish biomass, an ecosystem service of michigan rivers. North American Journal of Fisheries Management 35(2):302–320 Fahrmeir L, Kneib T, Lang S, Marx B (2007) Regression. Springer 

Fisher A, Rudin C, Dominici F (2019) All models are wrong, but many are use- 

ful: Learning a variable’s importance by studying an entire class of prediction models simultaneously. Journal of Machine Learning Research 20(177):1–81 Friedman JH (1991) Multivariate adaptive regression splines. The Annals of Statistics pp 1–67 

Geman S, Bienenstock E, Doursat R (1992) Neural networks and the bias/variance dilemma. Neural Computation 4(1):1–58 

Grange SK, Carslaw DC (2019) Using meteorological normalisation to detect interventions in air quality time series. Science of The Total Environment 653:578–588 

Groemping U (2020) Model-agnostic effects plots for interpreting machine learning models. Reports in Mathematics, Physics and Chemistry, Department II, Beuth University of Applied Sciences Berlin Report 1/2020 

Hooker G, Mentch L (2019) Please stop permuting features: An explanation and alternatives. arXiv preprint arXiv:190503151 

- Hothorn T, Leisch F, Zeileis A, Hornik K (2005) The design and analysis of benchmark experiments. Journal of Computational and Graphical Statistics 14(3):675–699 

Relating PDP and PFI to the Data Generating Process 21 

- Ishwaran H, Lu M (2019) Standard errors and confidence intervals for variable importance in random forest regression, classification, and survival. Statistics in Medicine 38(4):558–582 

- Janitza S, Celik E, Boulesteix AL (2018) A computationally fast variable importance test for random forests for high-dimensional data. Advances in Data Analysis and Classification 12(4):885–915 

- Mitchell TM (1980) The need for biases in learning generalizations. Department of Computer Science, Laboratory for Computer Science Research . . . 

- Molnar C, K¨onig G, Bischl B, Casalicchio G (2020) Model-agnostic feature importance and effects with dependent features–a conditional subgroup approach. arXiv preprint arXiv:200604628 

- Nadeau C, Bengio Y (2003) Inference for the generalization error. Machine Learning 52(3):239–281 

- Obringer R, Nateghi R (2018) Predicting urban reservoir levels using statistical learning techniques. Scientific Reports 8(1):1–9 

- Page WG, Wagenbrenner NS, Butler BW, Forthofer JM, Gibson C (2018) An evaluation of ndfd weather forecasts for wildland fire behavior prediction. Weather and Forecasting 33(1):301–315 

- Parr T, Wilson JD (2019) A stratification approach to partial dependence for codependent variables. arXiv preprint arXiv:190706698 

- Parr T, Wilson JD, Hamrick J (2020) Nonparametric feature impact and importance. arXiv preprint arXiv:200604750 

- Ribeiro MT, Singh S, Guestrin C (2016) Model-agnostic interpretability of machine learning. ICML WHI ’16 URL `http://arxiv.org/abs/1606.05386` , `1606.05386` 

Scholbeck CA, Molnar C, Heumann C, Bischl B, Casalicchio G (2019) Sampling, intervention, prediction, aggregation: A generalized framework for model agnostic interpretations. arXiv preprint arXiv:190403959 

- Stachl C, Au Q, Schoedel R, Gosling SD, Harari GM, Buschek D, V¨olkel ST, Schuwerk T, Oldemeier M, Ullmann T, Hussmann H, Bischl B, B¨uhner M (2020) Predicting personality from patterns of behavior collected with smartphones. Proceedings of the National Academy of Sciences 117(30):17680–17687 

- Strobl C, Boulesteix AL, Kneib T, Augustin T, Zeileis A (2008) Conditional variable importance for random forests. BMC Bioinformatics 9(1):307 

- Tibshirani R (1996) Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological) 58(1):267–288 

- Watson DS, Wright MN (2019) Testing conditional independence in supervised learning algorithms. arXiv preprint arXiv:190109917 

- Williamson BD, Gilbert PB, Carone M, Simon N (2019) Nonparametric variable importance assessment using machine learning techniques. Biometrics 

- Williamson BD, Gilbert PB, Simon NR, Carone M (2020) A unified approach for inference on algorithm-agnostic variable importance. arXiv preprint arXiv:200403683 

- Zhang L, Janson L (2020) Floodgate: inference for model-free variable importance. arXiv preprint arXiv:200701283 

Christoph Molnar et al. 

22 

- Zhao Q, Hastie T (2021) Causal interpretations of black-box models. Journal of Business & Economic Statistics 39(1):272–281 

- Zheng W, van der Laan MJ (2011) Cross-validated targeted minimum-lossbased estimation. In: Targeted Learning, Springer, pp 459–474 

Relating PDP and PFI to the Data Generating Process 

23 

# **Supplementary Material** 

# **A Bias and Variance of PD** 

The expected squared difference between model-PD and DGP-PD can be decomposed into bias and variance. 

_Proof_ 



# **B Bias and Variance of PFI** 

The expected squared difference between model-PFI and DGP-PFI can be decomposed into bias and variance. 

_Proof_ 



# **C Model-PD Unbiasedness Regarding Theoretical PD** 

_Proof_ By the law of large numbers, the Monte Carlo integration converges with _n_ 2 _→∞_ to the true integral. Assuming _n_ 2 identically distributed random draws _XC_<sup>(1)</sup><sup>_, . . . , X_</sup> _C_<sup>(</sup><sup>_n_2)</sup> _∼ XC_ 

Christoph Molnar et al. 

24 

and model _f_<sup>ˆ</sup> , the estimate is: 



and therefore unbiased for the interval, i.e., the theoretical PD of the model. 

# **D Model-PD Unbiasedness Regarding DGP-PD** 

_Proof_ Unbiasedness of the model _f_<sup>ˆ</sup> implies unbiasedness of the model-PD. 



Fubini’s theorem requires that � _F,XC_<sup>_|_ˆ</sup><sup>_f|d_P</sup><sup>_F_P</sup><sup>_X_</sup> _C_<sup>_<∞_.Thisisgivenwhenitcanbe</sup> guaranteed that the model predictions have an upper bound _c_ : _|f_<sup>ˆ</sup> ( _x_ ) _| < c < ∞_ . 

# **E Model-PFI Regarding theoretical PFI** 

_Proof_ As a function of random variables, the loss _L_ itself is a random variable. We assume that the loss _L_<sup>(</sup><sup>_i_)</sup> of observation _i_ is a sample from the distribution of losses: _L_<sup>(</sup><sup>_i_)</sup> _∼ L_ and, similarly for the permuted loss: _L_<sup>˜(</sup><sup>_k,i_)</sup> _∼ L_<sup>˜</sup> , where _L_<sup>(</sup><sup>_i_)</sup> = _L_ ( _y_<sup>(</sup><sup>_i_)</sup> _, f_<sup>ˆ</sup> ( _x_<sup>(</sup><sup>_i_)</sup> )) and _L_<sup>˜(</sup><sup>_k,i_)</sup> = _L_ ( _y_<sup>(</sup><sup>_i_)</sup> _, f_<sup>ˆ</sup> (˜ _xS_<sup>(</sup><sup>_k,i_)</sup> _, x_<sup>(</sup> _C_<sup>_i_))).</sup> 

The expectation of our estimator is: 



In expectation, we retrieve the theoretical PFI of the model. 

# **F PFI Biases for L2** 

We assume that _L_ is the squared loss _L_ ( _y, f_<sup>ˆ</sup> ) = ( _y − f_<sup>ˆ</sup> ( _x_ ))2 and that E[ _Y |X_ ] can be described by _f_ with some additive, irreducible, error _ϵ_ with E( _ϵ_ ) = 0 and V( _ϵ_ ) = _σ_<sup>2</sup> . To further examine the bias for PFI, we apply the Bias-Variance Decomposition also on the loss itself: In addition, we use that E _XY_ [ _Y_ ] = E _X_ [ _f_ ( _X_ )], V _Y_ [ _Y_ ] = _σ_<sup>2</sup> and E[ _A_<sup>2</sup> ] = V[ _A_ ] + E[ _A_ ]<sup>2</sup> . We 

Relating PDP and PFI to the Data Generating Process 

25 

first derive the bias-variance decomposition of (i) permuted loss and (ii) original loss and derive from that the expected PFI. 

For the permuted loss (i): 



For the original loss (ii): 



The expected PFI for feature _XS_ then is: 



We can derive the same L2 decomposition for the DGP-PFI by replacing _f_<sup>ˆ</sup> with _f_ in the equation above. This yields _PFIf_ = E _X_ ˜ _S X_<sup>[(</sup><sup>_f_(</sup><sup>_X_)</sup><sup>_−f_( ˜</sup> _XS , XC_ ))<sup>2</sup> ], since V _F_ [ _f_ ] = V _F_ [ _f_<sup>˜</sup> ] = 0 and E _F_ [ _f_ ] = _f_ and E _F_ [ _f_<sup>˜</sup> ] = _f_<sup>˜</sup> . 

The bias of the model-PFI, compared to the DGP-PFI, is: 



The permutation loss bias and the squared model bias from the equation above are zero when the model is not biased, i.e., _f_<sup>ˆ</sup> = _f_ . The variance inflation term is zero if _X_<sup>˜</sup> _S ∼ XS |XC_ , which is the case when conditional PFI is used, or when marginal PFI is used and features _XS_ are independent from features _XC_ . If the features in _XS_ and _XC_ are dependent, the marginal PFI might be biased, even when the underlying model is unbiased. 

Christoph Molnar et al. 

26 

# **G DGP-PFI minus model-PFI for L2** 



We know that for any _g_ : _X → Y_ holds: 

E _X,Y_ [( _Y − g_ )<sup>2</sup> ] = E _X_ [V _Y |X_ [ _Y_ ]] + E _X_ [(E _Y |X_ [ _Y_ ] _− g_ )<sup>2</sup> ] Since _f_ = E _Y |XS ,XC_ [ _Y_ ] we can conclude for our first term T1 that: 



We apply the same trick to T2. Moreover, _Y_ 

If we now set together the two terms again and use in the first step that _P_ ( _XS , XC_ ) = _P_ ( _X_<sup>˜</sup> _S , XC_ ), we get: 

At *, we use the fact that the random variable E _Y |XC_ [ _Y_ ] is measurable by the _σ_ -Algebra generated from _XC_ and we are inclined to pull it out of the expectation. In **, we use that from _f_ = E _Y |XS ,XC_ [ _Y_ ] follows E _XS |XC_ [ _f_ ] = E _Y |XC_ [ _Y_ ]. 

Relating PDP and PFI to the Data Generating Process 

27 



<!-- Start of picture text -->
lm rf tree<br>1.00<br>0.75<br>0.50<br>adjusted<br>0.25<br>FALSE<br>TRUE<br>0.00<br>1.00 Sampling Strategy<br>boot<br>ideal<br>0.75<br>subs<br>0.50<br>0.25<br>0.00<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>Figure 7 CI coverage for PD with n=100.<br>lm rf tree<br>6<br>4<br>2 adjusted<br>FALSE<br>TRUE<br>0<br>Sampling Strategy<br>boot<br>6<br>ideal<br>subs<br>4<br>2<br>0<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>linear<br>Confidence Interval Coverage<br>non−linear<br>linear<br>Confidence Interval Width<br>non−linear<br><!-- End of picture text -->

**Figure 8** CI width for PD with n=100. 

# **H CI simulation results** 

Christoph Molnar et al. 

28 



<!-- Start of picture text -->
lm rf tree<br>1.00<br>0.75<br>0.50<br>adjusted<br>0.25<br>FALSE<br>TRUE<br>0.00<br>1.00 Sampling Strategy<br>boot<br>ideal<br>0.75<br>subs<br>0.50<br>0.25<br>0.00<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>Figure 9 CI coverage for PD with n=1,000.<br>lm rf tree<br>2<br>1 adjusted<br>FALSE<br>TRUE<br>0<br>Sampling Strategy<br>boot<br>ideal<br>2 subs<br>1<br>0<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>linear<br>Confidence Interval Coverage<br>non−linear<br>linear<br>Confidence Interval Width<br>non−linear<br><!-- End of picture text -->

**Figure 10** CI width for PD with n=1,000. 

Relating PDP and PFI to the Data Generating Process 

29 



<!-- Start of picture text -->
lm rf tree<br>1.00<br>0.75<br>0.50<br>adjusted<br>0.25<br>FALSE<br>TRUE<br>0.00<br>1.00 Sampling Strategy<br>boot<br>ideal<br>0.75<br>subs<br>0.50<br>0.25<br>0.00<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>Figure 11 CI coverage for PFI with n=100.<br>lm rf tree<br>4<br>3<br>2<br>adjusted<br>1<br>FALSE<br>TRUE<br>0<br>4 Sampling Strategy<br>boot<br>ideal<br>3<br>subs<br>2<br>1<br>0<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>linear<br>Confidence Interval Coverage<br>non−linear<br>linear<br>Confidence Interval Width<br>non−linear<br><!-- End of picture text -->

**Figure 12** CI width for PFI with n=100. 

Christoph Molnar et al. 

30 



<!-- Start of picture text -->
lm rf tree<br>1.00<br>0.75<br>0.50<br>adjusted<br>0.25<br>FALSE<br>TRUE<br>0.00<br>1.00 Sampling Strategy<br>boot<br>ideal<br>0.75<br>subs<br>0.50<br>0.25<br>0.00<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>Figure 13 CI coverage for PFI with n=1,000.<br>lm rf tree<br>1.00<br>0.75<br>0.50<br>adjusted<br>0.25<br>FALSE<br>TRUE<br>0.00<br>1.00 Sampling Strategy<br>boot<br>ideal<br>0.75<br>subs<br>0.50<br>0.25<br>0.00<br>10 20 30 10 20 30 10 20 30<br>Number of Model Refits<br>linear<br>Confidence Interval Coverage<br>non−linear<br>linear<br>Confidence Interval Width<br>non−linear<br><!-- End of picture text -->

**Figure 14** CI width for PFI with n=1,000. 

