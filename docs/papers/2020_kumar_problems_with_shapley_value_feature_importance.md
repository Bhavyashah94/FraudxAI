---
title: "Problems with Shapley-value-based explanations as feature importance measures"
authors: "I. Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, Sorelle A. Friedler"
year: 2020
venue: "ICML 2020"
domain: "Mathematical Proof of Correlation Leakage in SHAP"
pdf_path: "docs/papers\2020_kumar_problems_with_shapley_value_feature_importance.pdf"
---

# Problems with Shapley-value-based explanations as feature importance measures

**Authors:** I. Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, Sorelle A. Friedler  
**Venue / Date:** ICML 2020 (2020)  
**Domain Focus:** Mathematical Proof of Correlation Leakage in SHAP  
**Original PDF:** [`2020_kumar_problems_with_shapley_value_feature_importance.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_kumar_problems_with_shapley_value_feature_importance.pdf)

---

**Problems with Shapley-value-based explanations as feature importance measures** 

## **I. Elizabeth Kumar**<sup>1</sup> **Suresh Venkatasubramanian**<sup>1</sup> **Carlos Scheidegger**<sup>2</sup> **Sorelle A. Friedler**<sup>3</sup> 

# **Abstract** 

Game-theoretic formulations of feature importance have become popular as a way to “explain” machine learning models. These methods define a cooperative game between the features of a model and distribute influence among these input elements using some form of the game’s unique Shapley values. Justification for these methods rests on two pillars: their desirable mathematical properties, and their applicability to specific motivations for explanations. We show that mathematical problems arise when Shapley values are used for feature importance, and that the solutions to mitigate these necessarily induce further complexity, such as the need for causal reasoning. We also draw on additional literature to argue that Shapley values are not a natural solution to the human-centric goals of explainability. 

# **1. Introduction** 

Machine learning models are increasingly being used to replace human decision-making for tasks involving some kind of prediction. As state-of-the-art predictive machine learning models become increasingly inscrutable, there has been an increase in concern that the black-box nature of these systems can obscure undesirable properties of the decision algorithm, such as illegal bias or signals accidentally learned from artifacts irrelevant to the task at hand. More recently, attempts have been made to “explain” the output of a complicated function in terms of its inputs to address these and other concerns. One of the more prominent tools in this literature has been the Shapley value, a method for additively attributing value among players of a cooperative game. In this setting, the “players” are the features used 

1School of Computing, University of Utah, Salt Lake City, UT, USA<sup>2</sup> Department of Computer Science, University of Arizona, Tucson, AZ, USA<sup>3</sup> Department of Computer Science, Haverford College, Haverford, PA, USA. Correspondence to: I. Elizabeth Kumar _<_ kumari@cs.utah.edu _>_ . 

_Proceedings of the 37_<sup>_th_</sup> _International Conference on Machine Learning_ , Vienna, Austria, PMLR 119, 2020. Copyright 2020 by the author(s). 

by the model, and the game is the prediction of the model. A variety of methods to assign feature influence using the Shapley value have recently been developed (Lipovetsky & Conklin, 2001; Strumbelj & Kononenko<sup>ˇ</sup> , 2014; Lundberg et al., 2018; Datta et al., 2016b; Merrick & Taly, 2019; Frye et al., 2019; Aas et al., 2019). 

In this paper, we demonstrate that Shapley-value-based explanations for feature importance fail to serve their desired purpose in general. We make this argument in two parts. Firstly, we show that applying the Shapley value to the problem of feature importance introduces mathematically formalizable properties which may not align with what we would expect from an explanation. Secondly, taking a humancentric perspective, we evaluate Shapley-value-based explanations through established frameworks of what people expect from explanations, and find them wanting. We find that the game theoretic problem formulation of Shapleyvalue-based explanations do not match the proposed use cases for its solution, and thus caution against their usage except in narrowly constrained settings where they admit a clear interpretation. 

We describe the different Shapley-value-based explanation frameworks in Section 2, and present our two-part critique in Sections 3 and 4. We discuss these results and provide some suggestions in Section 5. 

# **2. Background** 

In this section, we define the Shapley value and articulate the different ways in which it has been applied to the problem of feature importance. 

## **2.1. Classical Shapley values** 

In cooperative game theory, a coalitional game consists of a set of _N_ players and a characteristic function _v_ which maps subsets _S ⊆{_ 1 _,_ 2 _, ..., N }_ to a real value _v_ ( _S_ ), satisfying _v_ ( _∅_ ) = 0. The value function represents how much collective payoff a set of players can gain by “cooperating” as a set. The Shapley value is one way to allocate the total value of the grand coalition, _v_ ( _{_ 1 _,_ 2 _, ..., N }_ ), between the individual players. It is based on trying to answer the question: how much does player _i_ contribute to the coalition? 

**Problems with Shapley-value-based explanations as feature importance measures** 

The marginal contribution ∆ _v_ ( _i, S_ ) of player _i_ with respect to a coalition _S_ is defined as the additional value generated by including _i_ in the coalition: 



Intuitively, the Shapley value can be understood as a weighted average of a player’s marginal contributions to every possible subset of players. Let Π be the set of permutations of the integers up to _N_ , and given _π ∈_ Π let _Si,π_ = _{j_ : _π_ ( _j_ ) _< π_ ( _i_ ) _}_ represent the players preceding player _i_ in _π_ . The _Shapley value_ of player _i_ is then 



This can be rewritten in terms of the unique subsets _S ⊆ {_ 1 _,_ 2 _, ..., N }_ and the number of permutations for which some ordering of _S_ immediately precedes player _i_ : 



This value is the unique allocation of the _grand coalition v_ ( _{_ 1 _,_ 2 _, ..., N }_ ) which satisfies the following axioms: 

**Symmetry** : For two players _i, j_ , if ∆ _v_ ( _i, S_ ) = ∆ _v_ ( _j, S_ ) for any subset of players _S_ , then _φv_ ( _i_ ) = _φv_ ( _j_ ). 

**Dummy** : For a single player _i_ , if ∆ _v_ ( _i, S_ ) = 0 for all subsets _S_ , then _φ_ ( _i_ ) = 0. 

**Additivity** : For a single player _i_ and two value functions _v_ and _w_ , _φv_ ( _i_ ) + _φw_ ( _i_ ) = _φv_ + _w_ ( _i_ ). 

## **2.2. Shapley values for feature importance** 

Several methods have been proposed to apply the Shapley value to the problem of feature importance. Given a model _f_ ( _x_ 1 _, x_ 2 _, ..., xd_ ), the features from 1 to _d_ can be considered players in a game in which the payoff _v_ is some measure of the importance or influence of that subset. The Shapley value _φv_ ( _i_ ) can then be viewed as the “influence” of _i_ on the outcome. 

In this section, we describe methods which consist of defining a value function _vf_ with respect to a model _f_ , and computing (or approximating) the resulting Shapley values. We will use the following notation: 

_D_ : the set of features _{_ 1 _,_ 2 _, ..., d}_ **_X_** : a multivariate random variable _{X_ 1 _, X_ 2 _, ..., Xd}_ **_x_** : a set of values _{x_ 1 _, x_ 2 _, ..., xd}_ **_X_** _S_ : the set of random variables _{Xi_ : _i ∈ S}_ **_x_** _S_ : the set of values _{xi_ : _i ∈ S}_ 

## 2.2.1. VALUE FUNCTIONS 

Shapley values have a fairly long history in the context of feature importance. Kruskal (1987) and Lipovetsky & Conklin (2001) proposed using the Shapley value to analyze global feature importance in linear regression by using the value function _vf_ ( _S_ ) to represent the _R_<sup>2</sup> of a linear model _f_ built on predictors _S_ , to decompose the variance explained additively between the features. Owen & Prieur (2017) applied the Shapley value to the problem of sensitivity analysis, where the total variance of a function is the quantity of interest. 

Many recently proposed “local” methods (Ribeiro et al., 2016; Lundberg & Lee, 2017; Lundberg et al., 2018) define a value function _vf,x_ : 2<sup>_d_</sup> _→_ R that depends on a specific data instance **_x_** to explain how each feature contributes to the output of the function on this instance. The value of the grand coalition, in this setting, is the prediction of the model at **_x_** : _vf,x_ ( _D_ ) = _f_ ( **_x_** ). In addition, to use Shapley values as an “explanation” of the (grand coalition of) features in this way, these methods also need to specify how _vf,x_ acts on proper subsets of the features. 

The definitions of _Shapley sampling values_ (Strumbelj<sup>ˇ</sup> & Kononenko, 2014), as well as _SHAP values_ (Lundberg & Lee, 2017), are derived from defining _vf,x_ ( _S_ ) as the _conditional_ expected model output on a data point when only the features in _S_ are known: 



Quantitative Input Influence (QII) (Datta et al., 2016a) draws on ideas from causal inference to propose simulating an _intervention_ on the features not in _S_ , thus breaking correlations with the features in _S_ : 



where the distribution _D_ is derived from the product of the marginal distributions of the features in _S_<sup>¯</sup> . The approach of using a distribution other than that of the original data was further generalized by (Merrick & Taly, 2019), who also propose the Formulate, Approximate, Explain (FAE) framework, so as to unify a number of different approaches to Shapley value explanations. 

## 2.2.2. ALGORITHMS 

Methods based on the same value function can differ in their mathematical properties based on the assumptions and computational methods employed for approximation. TreeSHAP (Lundberg et al., 2018), an efficient algorithm for calculating SHAP values on additive tree-based models such as random forests and gradient boosting machines, can estimate _EXS_ ¯<sup>_|XS_[</sup><sup>_f_(</sup><sup>**_x_**</sup><sup>_S,_</sup><sup>**_X_**¯</sup><sup>_S_)] by observing what proportion</sup> 

**Problems with Shapley-value-based explanations as feature importance measures** 

|Method|_vf_|_,x_(_S_)||ˆ_vf,x_(_S_)|
|---|---|---|---|---|
|KernelSHAP, Shapley sampling values|_EX_¯<br>_S_<sup>_|XS_[</sup>|<sup>_f_(</sup><sup>**_x_**</sup><sup>_S,_</sup><sup>**_X_** ¯</sup><sup>_S_)]</sup>|_ED_[|_f_(**_x_**_S,_**_X_**¯_S_)]|
|QII, FAE, Interventional TreeSHAP|_ED_[_f_(|**_x_**_S,_**_X_**¯_S_)]|_ED_[|_f_(**_x_**_S,_**_X_**¯_S_)]|
|Conditional TreeSHAP,Frye et al. (2019),Aas et al. (2019)|_EX_¯<br>_S_<sup>_|XS_[</sup>|<sup>_f_(</sup><sup>**_x_**</sup><sup>_S,_</sup><sup>**_X_** ¯</sup><sup>_S_)]</sup>|_EX_¯<br>_S_<sup>_|X_</sup>|<sup>_S_[</sup><sup>_f_(</sup><sup>**_x_**</sup><sup>_S,_</sup><sup>**_X_** ¯</sup><sup>_S_)]</sup>|



_Table 1._ Proposed value function _vf,x_ for each method, compared with the quantity _v_ ˆ _f,x_ the algorithm actually approximates. The interventional distribution _D_ used depends on the method (i.e., for KernelSHAP it is the observational joint distribution of _X_<sup>¯</sup> ). 

of the samples in the training set matching the condition **_x_** _S_ fall into each leaf node, a method which does not rely on a feature independence assumption. In the algorithm for KernelSHAP (Lundberg & Lee, 2017), conditional expectations are estimated by assuming feature independence; samples of the features in _S_<sup>¯</sup> = _D \ S_ are drawn from the _marginal_ joint distribution of these variables. This effectively approximates an expectation over an _interventional_ distribution instead, though in a slightly different way from QII. 

In Table 1, we categorize each method based on how they _define_ a value function _vf,x_ ( _S_ ) and how they _estimate_ that value function _v_ ˆ _f,x_ ( _S_ ). In the rest of the paper, we will refer to these value functions as either interventional or conditional based on the estimation method. That is to say, KernelSHAP, Shapley sampling values, QII, and FAE are _interventional_ methods, while TreeSHAP as well as some other algorithms we will introduce later are _conditional_ . 

# **3. Mathematical issues** 

We now present a number of mathematically articulated problems that arise when we attempt to interpret Shapley values as feature importance measures. These problems arise from the estimation procedures that are in use as well as the fundamental axiomatic structure of Shapley values. 

## **3.1. Conditional versus interventional distributions** 

A fundamental difference between the interventional and conditional value functions is revealed by what we call the _indirect influence_ debate. Suppose _f_ is defined with domain R<sup>_d_</sup> , but for a certain feature _i_ , _f_ ( **_x_** ) = _f_ ( **_x_**<sup>_′_</sup> ) whenever _xj_ = _x_<sup>_′_</sup> _j_<sup>for all</sup><sup>_j̸_=</sup><sup>_i_; that is to say, intervening on the value</sup> of _xi_ alone does not change the output of _f_ . We call this a variable with _no interventional effect._ 

Should a feature with no interventional effect be considered an “input” to this function? We could define a new function _f_<sup>_′_</sup> with domain R<sup>_d−_1</sup> to perfectly capture the output, so perhaps not. What if, in the relevant input space, _xi_ is a statistical proxy for some _xj_ which _does_ affect the output of _f_ ? Shapley value based feature importance methods must grapple with these choices. 

Adler et al. (2018) take the information-theoretic position that “the information content of a feature can be estimated 

by trying to predict it from the remaining features.” This perspective can help diagnose situations where an undesirable proxy variable is being used by a model, as in the classic case of redlining. While Adler et al. go on to analyze how the _accuracy_ of a model depends on indirect information, the _conditional_ value function aligns with this information-theoretic principle as well: If a certain feature _i_ can help predict the features in _S_<sup>¯</sup> , then the quantities _vf,x_ ( _S ∪ i_ ) = _E_ [ _f_ ( **_X_** ) _|_ **_X_** _S∪i_ = **_x_** _S∪i_ ] and _vf,x_ ( _S_ ) = _E_ [ _f_ ( **_X_** ) _|_ **_X_** _S_ = **_x_** _S_ ] may be meaningfully different, meaning that the marginal contribution of feature _i_ is nonzero. For this reason the Shapley value of the conditional value function may attribute influence to features with no interventional effect, a positive thing from the perspective of Adler et al.. 

Merrick & Taly (2019), on the other hand, criticize the capacity to attribute indirect influence as being paradoxical, and show that interventional methods will _never_ attribute attribute influence to an _xi_ which has no interventional effect on _f_ , which they see as a desirable property. 

Unfortunately, the decision between the two types of value functions is a catch-22. Both methods introduce serious issues: Choosing a conditional method requires further modeling of how the features are interrelated, which we describe in 3.1.1, while choosing an interventional method induces an “out-of-distribution” problem which we address in 3.1.2. 

## 3.1.1. ISSUES WITH CONDITIONAL DISTRIBUTIONS 

The conditional value function induces two major difficulties. First, the exact computation of the Shapley value for a conditional value function would require knowledge of 2<sup>_d_</sup> different multivariate distributions, and so a significant amount of approximation or modeling is necessary. Second, since influence can be computed on an arbitrarily large set of features, it becomes necessary to choose a set that is meaningful because the explanations may change based on which features are considered. 

Solutions have been proposed to deal with the computational complexity of this problem. The TreeSHAP algorithm estimates the conditional expectations of any tree ensemble directly, without sampling, using information computed during model training. The algorithm utilizes information about the training instances which fall into each leaf node to model each conditional distribution. It is _not_ , however, 

**Problems with Shapley-value-based explanations as feature importance measures** 

set up to attribute influence to variables without an interventional effect, as the trees contain no information about the distribution of variables not in the model. 

For arbitrary types of models, estimating the conditional expectations requires a substantial amount of additional modeling of relationships in the data which are not necessarily captured by the model that one is trying to explain. Aas et al. (2019) and Frye et al. (2019) have developed methods that aim to generate in-distribution samples for the relevant calculations. 

Even if computational issues are resolved, there are additional inconsistencies introduced by the capacity of the Shapley value to attribute influence to an arbitrarily large feature set given a single function. The modeler must decide which features count as players in the cooperative game and which are redundant, and since the problem definition posits that the attributions add up to the value of _f_ ( _x_ ), this choice can affect the resulting explanations. 

Consider the addition of a redundant variable _C_ to a dataset with two features, _A_ and _B_ , so that _P_ ( _XC_ = _XB_ ) = 1. Suppose a model _f_ is trained on all three features. Intuitively, the features _B_ and _C_ should be equally informative to the model and so should have the same Shapley value under the conditional value function. Formally, the following properties will hold: 









so this means _vf,x_ ( _B_ ) = _vf,x_ ( _C_ ) = _vf,x_ ( _BC_ ) and _vf,x_ ( _AB_ ) = _vf,x_ ( _AC_ ) = _vf,x_ ( _ABC_ ). Therefore, for any data instance _x_ , 





Now consider what would happen if we defined a new function _f_<sup>_′_</sup> ( _xA, xB_ ) = _f_ ( _xA, xB, xB_ ). For any data instance, since _xB_ = _xC_ , _f_<sup>_′_</sup> ( **_x_** ) = _f_ ( **_x_** ). It is effectively the same model for all in-distribution data points, so the games _vf,x_ and _vf ′,x_ are the same for all subsets of variables. Yet if we choose to limit the scope of our explanation to two variables instead of three, the attribution for both _A_ and _B_ will come out to be different: 





Notice that _φ_<sup>_′_</sup> _v_<sup>(</sup><sup>_B_) is neither equal to</sup><sup>_φv_(</sup><sup>_B_),its assigned</sup> influence in the 3-variable setting, nor _φv_ ( _B_ ) + _φv_ ( _C_ ), the “total” influence of the two identical variables in the 3-variable setting. The relative apparent importances of _A_ and _B_ thus depend on whether _C_ is considered to be a third feature, even though the two functions are effectively the same. 

It is not obvious whether two statistically related features should be considered as separate “players” in the cooperative game, yet this choice has an impact on the output of these additive explanation models. Suppose, for instance, that _B_ is a sensitive feature, and _C_ is a non-sensitive feature that happens to perfectly correlate with it. Two different “fairness” audits of the same function would come out with quantitatively different results. 

Frye et al. (2019) propose to a solution to the problem in terms of incorporating causal knowledge: 

...If _xi_ is known to be the deterministic causal ancestor of _xj_ , one might want to attribute all the importance to _xi_ and none to _xj_ . 

They propose not only discounting fully redundant variables which are causal descendants of other variables in the model, but relaxing the symmetry axiom which uniquely defines the Shapley value. Instead of averaging marginal contributions over every permutation, they suggest defining a quasivalue which considers only certain permutations; for example, orderings which place causal ancestors before their descendants. 

In this framework, fully redundant features will receive zero attribution _and_ will not change the resulting value of the remaining features. For instance, in the above example, if variable _C_ were known to be a causal descendant of _B_ , the Asymmetric Shapley Values of _A_ and _B_ under _f_<sup>_′_</sup> will be the same as they were under _f_ . 

A fully specified causal model is not required to use this method: they “span the data-agnosticism continuum in the sense that they allow any knowledge about the data, however incomplete, to be incorporated into an explanation of the models behaviour.” The results in Frye et al. (2019) demonstrate, however, the _sensitivity_ of the game theoretic approach to the amount of prior knowledge about the relative agency of each feature, which we consider a significant limitation of the approach. 

There are thus both practical and epistemological challenges with computing the Shapley values of games with a conditional value function. 

**Problems with Shapley-value-based explanations as feature importance measures** 

_Figure 1._ Samples that might be drawn to estimate _E_ [ _f_ (1 _, Y_ )] and _E_ [ _f_ ( _X,_ 2)] to explain _f_ (1 _,_ 2) for some function _f_ , given correlated Gaussian distributions for _X_ and _Y_ , depending on whether the expectation is taken over _X|Y_ = 2 and _Y |X_ = 1 (left) or _X_ and _Y_ (right) 

## 3.1.2. ISSUES WITH INTERVENTIONAL DISTRIBUTIONS 

Conditional value functions introduce undesirable complexities to the feature importance problem, so those inclined against methods with the capacity for attributing indirect influence may prefer the methods interventional value functions instead. These methods, however, are highly sensitive to properties of the model which are not relevant to what it has learned about the data it was trained on. 

Methods which use an interventional value function fundamentally rely on evaluating a model on _out-of-distribution_ samples (Figure 1). Consider, for example, a model trained on a data set with three features: _X_ 1 and _X_ 2, both _N_ (0 _,_ 1), and an engineered feature _X_ 3 = _X_ 1 _X_ 2. To calculate _vf,x_ ( _{_ 1 _,_ 2 _}_ ) for some _x_ = _{x_ 1 _, x_ 2 _, x_ 3 _}_ , we would have to estimate _E_ ( _f_ ( _x_ 1 _, x_ 2 _, X_ 3)) over some distribution for _X_ 3 which does not depend on _x_ 1 or _x_ 2. Therefore we will almost certainly have to evaluate _f_ on some sample _{x_ 1 _, x_ 2 _, x_<sup>_′_</sup> 3<sup>_}_which</sup><sup>_does not respect x′_</sup> 3<sup>=</sup><sup>_x_1</sup><sup>_x_2- thus, it is</sup> well _outside_ the domain of the actual data distribution. The model _f_ has never seen an example like this in training, and has therefore not learned much about this part of the feature space. Its predictions on this feature space are not necessarily relevant to the task of explaining an in-distribution sample, yet the explanations will be affected by them. 

This “out-of-distribution” phenomenon has been explored recently by Hooker & Mentch (2019), who show why “permutation-based” methods to evaluate feature importance can be highly misleading: when values are substituted into feature set _S_<sup>¯</sup> that are unlikely or impossible when conditioned on feature set _S_ , the model _f_ is forced to _extrapolate_ to an unseen part of the feature space. They show that these feature importance methods are highly sensitive to the way in which the model extrapolates to these edge cases, which is undesirable information for a model “explanation” to capture. 

Slack et al. (2020) demonstrate how to exploit this sensitivity by devising models which illegally discriminate on some protected feature for in-distribution samples, but exhibit different behavior on the out-of-distribution samples used by KernelSHAP so as to simulate “fairness” in the resulting explanations. By manipulating the model’s behavior on unfamiliar parts of the feature space, they can twist the explanations on the familiar part to their will. 

These challenges illustrate that intervening on a subset of features of a data case before applying a model trained on a sample from a certain distribution is inherently misleading. 

## **3.2. Additivity constraints** 

In addition to the problems demonstrated above, which have to do with the choice between two families of value functions, we also identify problems which are common to both. These are linked to the axiomatic underpinnings of Shapley values. 

For any two of the axioms described in Section 2.1, there exists an alternative attribution between players which satisfies those two but not the other; the Shapley value is therefore only unique because it satisfies all three. Since the notion of the sum of two games is not especially meaningful, the **Additivity** axiom has been described by game theorists as “mathematically convenient” and “not nearly so innocent as the other two” (Osborne & Rubinstein, 1994). The choice to constrain the value to be unique in this way has implications for what kinds of models can be explained intuitively by the Shapley value. Even in simple cases where feature independence renders the interventional versus conditional debate irrelevant, we find the Shapley value conceptually limited for non-additive models. 

The Shapley value seems to intuitively align with what is considered important in an additive setting. Consider 

**Problems with Shapley-value-based explanations as feature importance measures** 

applying any of the expectation value functions to _f_ ( _x_ ) = _β_ 0+ _β_ 1 _x_ 1+ _..._ + _βdxd_ where the features _Xi_ are independent. For any subset _S_ , 

a model given by _f_ ( _x_ ) = Π<sup>_d_</sup> _j_ =1<sup>_xd_where the features are</sup> independent and centered at 0. Then for any subset _S_ , 





so the marginal contribution for feature _i̸ ∈ S_ is 











which, since _E_ [ _xj_ ] is 0, is always 0 unless _S_ = _D_ . Then the Shapley value for every feature _i_ is _d_<sup><u>1</u></sup><sup>_f_(</sup><sup>_x_), regardless of the</sup> value _xi_ . Even if, for instance, the magnitude of one of the variables is much higher than the other. This property will, in fact, hold for _all multiplicative functions_ of independently distributed, zero-centered data. 

Shapley values are touted for their “model-agnostic” quality, but under the lens of a particular interpretation, this is not the case. 



# **4. Human-centric issues** 

In this way, the Shapley value is supported by the common intuition that coefficient size, if variables are appropriately scaled, signals importance in a linear model. 

The additivity axiom is aligned with additive models in another way: the games resulting from two models sum to the expectation game of the sum of the two models. This seems reasonable when the models are additive in the first place. 

Now imagine if the additivity constraint were relaxed. We could use an alternative attribution _ψ_ which satisfies the other two axioms: _ψ_ : _ψ_ ( _i_ ) = _v_ ( _i_ ) for _i ∈ U_ and _ψ_ ( _i_ ) = _|U_ <u>1</u> _|_<sup>(</sup><sup>_v_(</sup><sup>_D_)</sup><sup>_−_�</sup> _j∈U_<sup>_v_(</sup><sup>_j_)) where</sup><sup>_U_is the set of dummy fea-</sup> tures. Using the expectation value function in this setting, any feature which did not satisfy _βi_ ( _xi − E_ [ _Xi_ ]) = 0 would get _the same attribution._ In this sense the additivity constraint seems necessary for a game-based feature attribution to provide any meaningful quantities about an additive model. Under an interventional interpretation of the attribution — using the values to assess which data changes produce the largest model prediction change — this is not a helpful property. 

Under an interventional interpretation, Shapley values are as uninformative for non-additive models as this alternative attribution is for linear ones. For instance, any value function which always evaluates to 0 except on the grand coalition will evenly distribute influence among players. Consider 

The analysis from Section 3 demonstrates the mathematical issues with feature importance methods derived from Shapley values and suggests how one might mitigate them. In this section we turn to the human side of the interaction between feature importance methods and the people who use them. This perspective is closer in spirit to the “humangrounded metrics” that Doshi-Velez & Kim (2017) describe in comparison with the “functionally-grounded evaluation” of the previous section. 

We use the framework set out by Selbst & Barocas (2018), who argue that there are three general motivations behind the call for explanations in AI. 

The first is a fundamental question of autonomy, dignity, and personhood. The second is a more instrumental value: educating the subjects of automated decisions about how to achieve different results. The third is a more normative questionthe idea that explaining the model will allow people to debate whether the models rules are justifiable. 

In this section, we attempt to reconcile the Shapley value feature importance formalization of machine learning “explanations” with these three goals. We argue that the theoretical properties of the Shapley value are not naturally well-suited to any one of these objectives. While we focus 

**Problems with Shapley-value-based explanations as feature importance measures** 

here on these issues in the context of Shapley values, many of these critiques also apply to other explanatory methods. 

## **4.1. Explanations as contrastive statements** 

The presence of the phrase “right to explanation” in the GDPR illustrates the sense many of us have that it is inherently unethical to make decisions about an individual without providing an explanation, in a way that Selbst & Barocas (2018) argue has more to do with “procedural justice” than “wanting an explanation for the purpose of vindicating certain specific empowerment or accountability goals.” 

It is not immediately clear how to formally evaluate a method that provides explanations merely because it should, rather than to improve on a particular metric or task. In this setting, Doshi-Velez & Kim suggest the empirical approach of running user tests where humans are provided with explanations and they evaluate their “quality”. But in fact, what humans consider a good explanation has been studied extensively in the social sciences, leading to several formal theories of how humans generate and select explanations. 

Miller (2019) provides an overview of this literature. One of his major findings is that the way humans explain phenomena to each other is through _contrastive_ statements: 

People do not explain the causes for an event per se, but explain the cause of an event relative to some other event that did not occur; that is, an explanation is always of the form “Why P rather than Q?”, in which P is the target event and Q is a counterfactual contrast case that did not occur. 

He attributes this insight to work by Lipton (1990). More recently, a similar argument has been made by Merrick & Taly (2019), referencing earlier work by Kahneman & Miller (1986). 

We now outline different ways in which Shapley values can be interpreted as contrastive explanations. 

## 4.1.1. SHAPLEY VALUE SETS AS A SINGLE CONTRASTIVE STATEMENT 

The above-mentioned research supports the hypothesis that people ask for explanations when the outcome, P, is “unexpected” compared to the outcome Q. In this sense, we can interpret Shapley-based explanations as a contrastive statement where the outcome to be explained is _v_ ( _D_ ) and the foil – the counterfactual case which did not happen – is implicitly set to be _v_ ( _∅_ ). In the “local” settings described earlier, _v_ ( _D_ ) is _f_ ( _x_ ) and _v_ ( _∅_ ) is _E_ ( _f_ ( _x_ )): 

_f_ ( _x_ ) = _E_ ( _f_ ( _x_ )) + _φ_ 1 + _φ_ 2 + _..._ + _φd_ 

Thus, the Shapley values can be thought of as a set of answers to the question, “Why _f_ ( _x_ ) rather than _E_ ( _f_ ( _x_ ))?” 

While the expected value of a function seems like a natural foil to an “unexpected” _f_ ( _x_ ), due to the properties of the expectation, there may not be a scenario in the data space of _X_ with the outcome _E_ ( _f_ ( _x_ )). Thus, the expected value may not be “expected” by anyone with a reasonable understanding of the situation at hand at all. 

If we are willing to consider intervention distributions (Section 2.2.1), then the framework provided by Merrick & Taly (2019) provides a slightly different contrastive explanation: in their setting, the Shapley value assignment can be thought of as a set of answers to the question, “Why _f_ ( _x_ ) rather than _f_ ( _r_ )?”, where _r_ is chosen from the reference distribution. This of course requires the specification of the reference distribution and carries with it the estimation issues described above in Section 3.1.2. 

## 4.1.2. MARGINAL CONTRIBUTIONS AS CONTRASTIVE STATEMENTS 

An alternate way to consider Shapley value-based methods as contrastive statements is by examining the marginal contribution of features. The set of _marginal contributions_ of each feature _i_ , which are averaged in a certain way over all subsets _S_ to calculate the Shapley value, can be thought of as a set of contrastive explanations. Each quantity ∆( _i, S_ ) represents a contrastive explanation for why feature _i_ is important: “Why choose a model with _S_ and _i_ rather than a model with just _S_ ? Because it improves _v_ by ∆( _i, S_ ) amount.” This quantity is an important part of _stepwise selection_ , a modeling procedure in which features which increase the _accuracy_ of a model are successively added to the modeling set. 

Note that regardless of what order features were actually added to the model in, all permutations are considered when the Shapley value is calculated. It is not clear that taking an average of quantities representing “all possible contrastive explanations” for a certain set of foils is a sensible way to summarize information. Instead, Miller (2019) argues that humans are _selective_ about explanations: certain contrasts are more meaningful than others. An example of this is the difference between _necessary_ and _sufficient_ causes: 

Lipton argues that necessary causes are preferred to sufficient causes. For example, consider mutations in the DNA of a particular species of beetle that cause its wings to grow longer than normal when kept in certain temperatures. Now, consider that there are two such mutations, _M_ 1 and _M_ 2, and either is sufficient to cause the mutation. To contrast with a beetle whose wings would not change, the explanation of temperature is preferred to either of the mutations _M_ 1 or _M_ 2, because neither _M_ 1 nor _M_ 2 are individually neces- 

**Problems with Shapley-value-based explanations as feature importance measures** 

sary for the observed event; merely that either _M_ 1 or _M_ 2. In contrast, the temperature is necessary, and is preferred, even if we know that the cause was _M_ 1. 

Consider, without specifying how to quantify the importance _v_ of a feature coalition, computing some kind of allocation for each feature to analyze the positive classification of a beetle with longer wings. Lipton’s argument above suggests that since all “yes” cases share a property _T_ , a contrastive statement highlighting this is more relevant than comparisons based on _M_ 1 or _M_ 2. This is fundamentally at odds with the idea that the “yes” prediction should be split additively between different coalitions of _M_ 1, _M_ 2 and _T_ , a property induced by the notion of the Shapley value. 

## **4.2. Using Shapley-valued based methods to enable action** 

One motivation for “explaining” a function is to enable individuals to figure out how to achieve a desirable outcome. For example, one might allow an individual to query the model for a specific contrastive explanation in which the person _p_ ’s outcome, _f_ ( _p_ ), is compared with a person _q_ with desirable outcome _f_ ( _q_ ) = _Q_ determined by the user, such that the user might be able to alter their own situation to approximate _q_ . This setup has been formalized as the “counterfactual explanation” problem by Wachter et al. (2017) (with an analysis of hidden assumptions by Barocas et al. (2020)). Ustun et al. (2019) further specify a way to model this problem by searching for changes within characteristics which are actually mutable; they call this the “actionable recourse” problem (with a corresponding analysis by Venkatasubramanian & Alfano (2020)). 

Unlike these methods, Shapley value based frameworks do not explicitly attempt to provide guidance how a user might alter one’s behavior in a desirable way. Further, observing that a certain feature carries a large influence over the model does not necessarily imply that changing that feature (even significantly) will change the outcome favorably. 

Suppose, in a very simple nonlinear example, that a univariate model is defined as _f_ ( _x_ ) = 2 _−_ ( _x −_ 1)<sup>2</sup> , for some _X ∼ N_ (0 _,_ 1). A person for whom _x_ = 1 will get _f_ (1) = 2, and _E_ ( _X_ ) = 0, so the Shapley value for this person’s single input is then _φ_ ( _x_ ) = 2. Suppose they were hoping for an even higher score. The fact that the value is positive, along with the general knowledge that 1 is a bit high with respect to an average value of _X_ , might make this person think that increasing their _x_ value even more will increase their score – but it will not. 

This problem stems from the fact that the contrastive quantity _E_ ( _f_ ( _x_ )) is not desirable, but even if _v_ ( _∅_ ) is chosen to be some desirable outcome _f_ ( _q_ ) of some _q_ , such as in Mer- 

rick & Taly (2019), the Shapley values themselves do not correspond to specific actions: the interventional effect of changing one input from _x_ to that from _q_ is just one of the marginal contributions that are averaged together to form the Shapley value of that input, as we discussed in Section 4.1.2. 

## **4.3. Shapley-based explanations for normative evaluation** 

Shapley-value-based explanations are primarily used for purposes of normative evaluation: deciding whether a model’s behavior is acceptable (Bhatt et al., 2020). This is done either at the development stage, to help a human evaluate a model, or at the decision-making stage, to help a human evaluate a specific decision made by a model. In this section we explore how the information content of the Shapley value is insufficient for evaluation. We marshal evidence to make three points. Firstly, data scientists do not have a clear mental model of what insights Shapley-value-based analysis brings. Secondly, in the face of this uncertainty, they tend to rely on narrative and confirmation biases. Thirdly, even if they do understand the analysis, it is not obvious that it can be operationalized for specific evaluation tasks. 

Since there is no standard procedure for converting Shapley values into a statement about a model’s behavior, developers rely on their own mental model of what the values represent. Kaur et al. (2020) conducted a contextual inquiry and survey of data scientists to observe their interpretation of interpretability tools including the SHAP Python package. They found that many participants did not have an accurate mental model of what a SHAP analysis represents, yet used them to make decisions on whether the model was ready for deployment, over-trusting and misusing the tool. 

Using feature importance during model development in this way is ripe for narrative and confirmation biases. Passi & Jackson (2018) conducted ethnographic fieldwork with a corporate data science team and described situations in which applying intuition to feature importance was a key component of the model development cycle. In one instance, when developers communicated the results of a modeling effort to project managers, the stakeholders immediately decided it was “useful” based entirely on the feature importance list: 

Certain highly-weighted features matched business intuitions, and everyone in the meeting considered this a good thing. ...Regarding counterintuitive feature importances, [a data scientist] reminded [the stakeholders] that machine-learning models do not approach data in the same way humans do. He pointed out that models use “a lot of complex math” to tell us things that we may not 

**Problems with Shapley-value-based explanations as feature importance measures** 

## know or fully understand. 

This suggests that even when an individual lacks a correct mental model of the meaning of Shapley values, they may use them to justify their evaluation anyway, whether or not this analysis is well-founded. 

In support of this hypothesis, empirical studies have shown that interpretability is not always helpful in task-specific settings. Poursabzi-Sangdeh et al. (2018), for instance, demonstrated that “interpretable” models may not be easier to evaluate: 

Participants who were shown a clear model with a small number of features were better able to simulate the models predictions. However, contrary to what one might expect when manipulating interpretability, we found no improvements in the degree to which participants followed the models predictions when it was beneficial to do so. Even more surprisingly, increased transparency hampered peoples ability to detect when the model makes a sizable mistake and correct for it, seemingly due to information overload. 

This suggests that common intuition for the benefits of interpretability (and the types of questions it can help answer) may be based on faulty assumptions, and these questions should instead be concretely specified and tested. For instance, data scientists might want to know: 

- Whether an error was made at any point in the data processing pipeline for a certain feature 

- Whether the model is acting upon spurious correlations or other artifacts of training data 

- Whether the model exhibits inappropriate biases 

- Whether the model’s accuracy will improve if a certain feature is included or excluded 

While Shapley-value-based methods might help qualitatively inform investigations that _lead_ to answers to these questions, it is not clear that they provide direct answers to any _specific_ question related to the points of interest above. Weerts et al. (2019), for instance, conducted a human-grounded evaluation of SHAP and did not find evidence that it helped users assess the correctness of predictions. 

# **5. Conclusion** 

Shapley values enjoy mathematically satisfying theoretical properties as a solution to game theory problems. However, 

applying a game theoretic framework does not automatically solve the problem of feature importance, and our work shows that in fact this framework is ill-suited as a general solution to the problem of quantifying feature importance. Rather than relying on notions of mathematical correctness, our work suggests that we need more focused approaches that stem from specific use cases and models, developed with human accessibility in mind. 

**Acknowledgments.** This research was supported in part by the National Science Foundation under grants IIS1633724, IIS-1633387, DMR-1709351, IIS-1815238, the DARPA SD2 Program, and the ARCS Foundation. 

# **References** 

- Aas, K., Jullum, M., and Lland, A. Explaining individual predictions when features are dependent: More accurate approximations to Shapley values. _arXiv:1903.10464 [cs, stat]_ , March 2019. URL http://arxiv.org/abs/ 1903.10464. arXiv: 1903.10464. 

- Adler, P., Falk, C., Friedler, S. A., Nix, T., Rybeck, G., Scheidegger, C., Smith, B., and Venkatasubramanian, S. Auditing black-box models for indirect influence. _Knowledge and Information Systems_ , 54(1):95–122, 2018. 

- Barocas, S., Selbst, A. D., and Raghavan, M. The hidden assumptions behind counterfactual explanations and principal reasons. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , FAT* 20, pp. 8089, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450369367. doi: 10.1145/3351095.3372830. URL https://doi. org/10.1145/3351095.3372830. 

- Bhatt, U., Xiang, A., Sharma, S., Weller, A., Taly, A., Jia, Y., Ghosh, J., Puri, R., Moura, J. M. F., and Eckersley, P. Explainable machine learning in deployment. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , FAT* 20, pp. 648657, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450369367. doi: 10. 1145/3351095.3375624. URL https://doi.org/ 10.1145/3351095.3375624. 

- Datta, A., Sen, S., and Zick, Y. Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems. In _2016 IEEE symposium on security and privacy (SP)_ , pp. 598–617. IEEE, 2016a. 

- Datta, A., Sen, S., and Zick, Y. Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems. In _2016 IEEE Symposium on Security and Privacy (SP)_ , pp. 598–617. IEEE, 2016b. 

**Problems with Shapley-value-based explanations as feature importance measures** 

- Doshi-Velez, F. and Kim, B. Towards A Rigorous Science of Interpretable Machine Learning. _arXiv:1702.08608 [cs, stat]_ , February 2017. URL http://arxiv.org/ abs/1702.08608. arXiv: 1702.08608. 

- Frye, C., Feige, I., and Rowat, C. Asymmetric shapley values: incorporating causal knowledge into model-agnostic explainability, 2019. 

- Hooker, G. and Mentch, L. Please stop permuting features: An explanation and alternatives. _arXiv preprint arXiv:1905.03151v1_ , 2019. 

- Kahneman, D. and Miller, D. T. Norm theory: Comparing reality to its alternatives. _Psychological review_ , 93(2): 136, 1986. 

- Kaur, H., Nori, H., Jenkins, S., Caruana, R., Wallach, H., and Wortman Vaughan, J. Interpreting interpretability: Understanding data scientists use of interpretability tools for machine learning. In _Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems_ , CHI 20, pp. 114, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450367080. doi: 10.1145/3313831.3376219. URL https://doi. org/10.1145/3313831.3376219. 

- Kruskal, W. Relative importance by averaging over orderings. _The American Statistician_ , 41(1):6–10, 1987. 

- Lipovetsky, S. and Conklin, M. Analysis of regression in game theory approach. _Applied Stochastic Models in Business and Industry_ , 17(4):319–330, 2001. 

- Lipton, P. Contrastive explanation. _Royal Institute of Philosophy Supplements_ , 27:247–266, 1990. 

- Lundberg, S. M. and Lee, S.-I. A unified approach to interpreting model predictions. In _Advances in Neural Information Processing Systems_ , pp. 4765–4774, 2017. 

- Lundberg, S. M., Erion, G. G., and Lee, S.-I. Consistent individualized feature attribution for tree ensembles. _arXiv preprint arXiv:1802.03888_ , 2018. 

- Merrick, L. and Taly, A. The explanation game: Explaining machine learning models with cooperative game theory. _arXiv preprint arXiv:1909.08128_ , 2019. 

- Miller, T. Explanation in artificial intelligence: Insights from the social sciences. _Artificial Intelligence_ , 267:1–38, 2019. 

- Osborne, M. J. and Rubinstein, A. _A course in game theory_ . 1994. 

- Owen, A. B. and Prieur, C. On shapley value for measuring importance of dependent inputs. _SIAM/ASA Journal on Uncertainty Quantification_ , 5(1):986–1002, 2017. 

- Passi, S. and Jackson, S. J. Trust in Data Science: Collaboration, Translation, and Accountability in Corporate Data Science Projects. _Proc. ACM Hum.-Comput. Interact._ , 2(CSCW):136:1–136:28, November 2018. ISSN 25730142. doi: 10.1145/3274405. URL http://doi.acm. org/10.1145/3274405. 

- Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Vaughan, J. W., and Wallach, H. Manipulating and measuring model interpretability. _arXiv preprint arXiv:1802.07810_ , 2018. 

- Ribeiro, M. T., Singh, S., and Guestrin, C. Why should i trust you?: Explaining the predictions of any classifier. In _Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining_ , pp. 1135–1144. ACM, 2016. 

- Selbst, A. D. and Barocas, S. The Intuitive Appeal of Explainable Machines. SSRN Scholarly Paper ID 3126971, Social Science Research Network, Rochester, NY, March 2018. URL https://papers.ssrn. com/abstract=3126971. 

- Slack, D., Hilgard, S., Jia, E., Singh, S., and Lakkaraju, H. Fooling lime and shap: Adversarial attacks on post hoc explanation methods. _AAAI/ACM Conference on Artificial Intelligence, Ethics, and Society (AIES)_ , 2020. 

- Strumbelj,ˇ E. and Kononenko, I. Explaining prediction models and individual predictions with feature contributions. _Knowledge and information systems_ , 41(3):647– 665, 2014. 

- Ustun, B., Spangher, A., and Liu, Y. Actionable recourse in linear classification. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pp. 10–19. ACM, 2019. 

- Venkatasubramanian, S. and Alfano, M. The philosophical basis of algorithmic recourse. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , FAT* 20, pp. 284293, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450369367. doi: 10.1145/ 3351095.3372876. URL https://doi.org/10. 1145/3351095.3372876. 

- Wachter, S., Mittelstadt, B., and Russell, C. Counterfactual explanations without opening the black box: Automated decisions and the gpdr. _Harv. JL & Tech._ , 31:841, 2017. 

- Weerts, H. J., van Ipenburg, W., and Pechenizkiy, M. A human-grounded evaluation of shap for alert processing. In _KDD workshop on Explainable AI (KDDXAI ’19’)_ , 2019. URL https://arxiv.org/abs/ 1907.03324. 

