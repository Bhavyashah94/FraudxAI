---
title: "The many Shapley values for model explanation"
authors: "sundararajan"
year: 2019
arxiv_id: "1908.08474"
original_file: "1908.08474.pdf"
pdf_path: "docs/papers\2019_sundararajan_the_many_shapley_values_for_model_e.pdf"
---

# The many Shapley values for model explanation

**Authors:** Sundararajan et al.  
**Year:** 2019 | **arXiv:** [`1908.08474`](https://arxiv.org/abs/1908.08474)  
**Local PDF:** [`2019_sundararajan_the_many_shapley_values_for_model_e.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_sundararajan_the_many_shapley_values_for_model_e.pdf)

---

The Many Shapley Values for Model Explanation 

Mukund Sundararajan Amir Najmi `mukunds@google.com amir@google.com` 

February 10, 2020 

### **Abstract** 

The Shapley value has become a popular method to attribute the prediction of a machine-learning model on an input to its base features. The use of the Shapley value is justified by citing [16] showing that it is the **unique** method that satisfies certain good properties ( **axioms** ). 

There are, however, a multiplicity of ways in which the Shapley value is operationalized in the attribution problem. These differ in how they reference the model, the training data, and the explanation context. These give very different results, rendering the uniqueness result meaningless. Furthermore, we find that previously proposed approaches can produce counterintuitive attributions in theory and in practice—for instance, they can assign non-zero attributions to features that are not even referenced by the model. 

In this paper, we use the axiomatic approach to study the differences between some of the many operationalizations of the Shapley value for attribution, and propose a technique called Baseline Shapley (BShap) that is backed by a proper uniqueness result. We also contrast BShap with Integrated Gradients, another extension of Shapley value to the continuous setting. 

# **1 Motivation and Related Work** 

We discuss the **attribution problem** , i.e., the problem of distributing the prediction score of a model for a specific input to its base features (cf. [15, 10, 19]); the attribution to a base feature can be interpreted as the importance of the feature to the prediction. For instance, when attribution is applied to a model that makes loan decisions, the attributions tell you how influential a feature was to the loan decision for a specific loan applicant. Attributions thus have explanatory value. 

One of the leading approaches to attribution is based on the Shapley value [16], a construct from cooperative game theory. In cooperative game theory, a group of players come together to consume a service, and this incurs some cost. The Shapley value distributes this cost among the players. There is a correspondence between cost-sharing and the attribution problem: The cost function is analogous to the model, the players to base features, and the cost-shares to the attributions. 

1 

The Shapley value is known to be the unique method that satisfies certain properties (see Section 2.1 for more details). The desirability of these properties, and the uniqueness result make a strong case for using the Shapley value. Unfortunately, despite the uniqueness result, there are a multiplicity of Shapley values that differ in how they refer to the model, the training data, and the explanation context. Here is a chronological sampling of the literature: 

1. There is literature (cf. [9, 8]) that uses the Shapley value to attribute the goodness of fit ( _R_<sup>2</sup> ) of a linear regression model to its features by retraining the model on different feature subsets. 

2. [12, 13] apply the Shapley value to study the importance of a feature to a given function, by using it to identify the ”variance explained” by the feature; no retraining involved . 

3. [17, 21] use the Shapley value to solve the attribution problem, i.e., feature importance for a specific prediction. The first paper applies the Shapley value by retraining the model on every possible subset of the features. The second paper applies the Shapley value to the conditional expectation of a specific model (no retraining) (see Section 2.2 for a formal definition of the conditional expectation approach). They assume that features are distributed uniformly and independently. 

4. [5] applies the Shapley value to the conditional expectations of the model’s function with a contrived distribution that is the product of the marginals of the underlying feature distribution. 

5. [10] also investigates the Shapley value with conditional expectations; it constructs various approximations that make assumptions about either the function, or the distribution, and applies it compositionally on modules of a deep network. 

6. [11] computes the Shapley value with conditional expectations efficiently for trees; however, it is not very clear about its assumptions on the feature distribution<sup>1</sup> . 

7. [1] generalizes one of the approaches in [10] to the case when the distributions are not independent, either by assuming that the features are generated by a mixture of Gaussians or by a non-parametric, heuristic approach that applies the Mahalanobis distance to the empirical distribution. 

8. Unlike the methods above that either delete or marginalize over a feature, [18, 19, 2] apply the Shapley value, by using a different approach to ‘turn features off’. This approach takes an auxiliary input called a baseline, and switches the explicand’s feature value to the value of the feature in the baseline (see Section 2.3 for details). 

> 1In an email exchange, Scott Lundberg clarified that the implicit assumption is that the features are distributed according to ”the distribution generated by the tree”. 

2 

9. [19] proposes a technique called Integrated Gradients, that is based on the Aumann-Shapley [4] cost-sharing technique. Aumann-Shapley is one of the several extensions of the discrete Shapley value to continuous settings. Relatedly, this technique is applicable only when the gradient of the prediction score with respect to the base features is well-defined, and is therefore not applicable to models like tree ensembles. 

The first and second approaches solve a different problem (of feature importance across all the training data), and we will ignore them for the most part. Notice that the rest are solving the same attribution problem, and are reflective of the non-uniqueness of the Shapley value for model explanation. [10] several of these methods (excluding Integrated Gradients) under a common framework based on certain conditional expectations over feature distributions. However, as we point out later in this paper, the choice of feature distribution influences the attributions significantly, not just in quantity, but also in quality. 

# **2 Preliminaries** 

We model the machine-learning model as a real-valued function _f_ that takes a vector of real-valued features as input. If the problem is a classification problem, the function models the **score** of a class. The set of features is denoted by _N_ . We designate the input to be explained, i.e., the **explicand** , by the vector _x_ of features; when we say _xS_ we mean the sub-vector of a vector _x_ restricted to the features in the set _S_ . 

At times, we may assume that the features are generated according to a distribution _D_ ; this distribution could be a posited distribution as in Section 4.3. Often, it is the empirical distribution of the training data, wherein it is written as _D_<sup>ˆ</sup> . Of special significance are independent feature distributions. The product of marginals of distribution _D_ is written as Π( _D_ ). The conditional expectation _E_ [ _f_ ( _x_ ) _|xS_ ] is the expected value of the function over the distribution with the features in _S_ fixed at the explicand’s value. 

## **2.1 Shapley value** 

The Shapley value takes as input a set function _v_ : 2<sup>_N_</sup> _→ R_ . The Shapley value produces attributions _si_ for each player _i ∈ N_ that add up to _v_ ( _N_ ). The Shapley value of a player _i_ is given by: 



There is an alternate permutation-based description of the Shapley value: Order the players uniformly at random, add them one at a time in this order, and assign to each player _i_ its expected marginal contribution _V_ ( _S ∪ i_ ) _− v_ ( _S_ ); here _S_ is the set of players that precede _i_ in the ordering. 

3 

In this paper, we study three extensions of the Shapley value to model explanation. 

## **2.2 Conditional Expectations Shapley (CES)** 

This approach takes three inputs: an explicand _x_ , a function _f_ , and a distribution _D_ . The set function is defined by the conditional expectation 



We denote the CES attribution for feature _i_ with explicand _x_ , distribution _D_ and function _f_ by _cesi_ ( _x, D, f_ ). This approach has been used by [21, 10, 5] and was proposed in this specific form by [10], where it is called Shapley Additive Explanations, or SHAP. When CES is carried out with the empirical distribution of the training _D_<sup>ˆ</sup> , it will be denoted as CES( _D_<sup>ˆ</sup> ). 

## **2.3 Baseline Shapley (BShap)** 

This approach takes as input an explicand _x_ , the function _f_ and an auxiliary input called the baseline _x_<sup>_′_</sup> . The set function is defined as: 



That is, we model a feature’s absence using its value in the baseline. We call this the Baseline Shapley (BShap) approach. We denote BShap attribution by _bsi_ ( _x, x_<sup>_′_</sup> _, f_ ). Variants of this approach have been used by [18, 2, 10]. 

## **2.4 Random Baseline Shapley (RBShap)** 

This approach is a variant of BShap that takes three inputs: An explicand _x_ , a function _f_ , and a distribution _D_ . The attributions are the expected BShap values, where the baseline _x_<sup>_′_</sup> is drawn randomly according to the distribution _D_ . This approach is implicit in [10] (see Equation 11). 



## **2.5 Integrated Gradients (IG)** 

This approach takes as input an explicand _x_ , the function _f_ and an auxiliary input called the baseline _x_<sup>_′_</sup> . We consider the straight-line path (in R<sup>_|N|_</sup> ) from the baseline _x_<sup>_′_</sup> to the input _x_ , and compute the gradients at all points along the path. The path can be parameterized as _γ_ ( _x, α_ ) = _x_<sup>_′_</sup> + _α ·_ ( _x − x_<sup>_′_</sup> ). Integrated gradients are obtained by accumulating these gradients. The integrated gradients attribution for an explicand _x_ and baseline _x_<sup>_′_</sup> , for a variable _xi_ is: 



IG is an analog of the Aumann-Shapley method from cost-sharing [4]. We will discuss the sense in which IG is an extension of the Shapley value in Section 4.1. 

4 

## **2.6 Axioms** 

We now list several desirable properties of an attribution technique and discuss why each property is desirable. Later, we will use these properties as a framework to compare and contrast various attribution methods. Variants of these axioms have appeared in prior cost-sharing literature (cf. [7]). 

An attribution method satisfies: 

- **Dummy** if dummy features get zero attributions. A feature _i_ is dummy in a function _f_ if for any two values _xi_ and _x_<sup>_′_</sup> _i_<sup>andeveryvalue</sup><sup>_xN\i_of</sup> the other features, _f_ ( _xi_ ; _xN \i_ ) = _f_ ( _x_<sup>_′_</sup> _i_<sup>;</sup><sup>_xN\i_);thisisjustaformalwayof</sup> saying that the feature is not referenced by the model, and it is natural to require such variables to get zero attributions. 

- **Efficiency** if for every explicand _x_ , and baseline _x_<sup>_′_</sup> , the attributions add up to the difference _f_ ( _x_ ) _− f_ ( _x_<sup>_′_</sup> ) for the baseline approach. For the conditional expectation approach, _f_ ( _x_<sup>_′_</sup> ) is replaced by _Ex_<sup>_′_</sup> _∼D_ [ _f_ ( _x_<sup>_′_</sup> )]. This axiom can be seen as part of the framing of the attribution problem; we would like to apportion blame of the entire difference _f_ ( _x_ ) _− f_ ( _x_<sup>_′_</sup> ) to the features. 

- **Linearity** if, feature by feature, the attributions of the linear combination of two functions _f_ 1 and _f_ 2 is the linear combination of the attributions for each of the two functions. Attributions represent a kind of forced linearization of the function. It is therefore desirable to preserve the existing linear structure in the function. 

- **Symmetry** if for every function _f_ that is symmetric in two variables _i_ and _j_ , if the explicand _x_ and baseline _x_<sup>_′_</sup> are such that _xi_ = _xj_ and _xi_<sup>_′_=</sup><sup>_x′_</sup> _j_<sup>, then</sup> the attributions for _i_ and _j_ should be equal. This is a natural requirement with obvious justification. 

- **Affine Scale Invariance (ASI)** if the attributions are invariant under a simultaneous affine transformation of the function and the features. That is, for any _c, d_ , if _f_ 1( _x_ 1 _, . . . , xn_ ) = _f_ 2( _x_ 1 _, ...,_ ( _xi − d_ ) _/c, ..., xn_ ), then for all _i_ we have _attri_ ( _x, x_<sup>_′_</sup> _, f_ 1) = _attri_ (( _x_ 1 _, . . . , c ∗ xi_ + _d, . . . xn_ ) _,_ ( _x_ 1<sup>_′, . . . , c ∗x′_</sup> _i_<sup>+</sup> _d, . . . x_<sup>_′_</sup> _n_<sup>)</sup><sup>_, f_2).ASIconveystheideathatthezeropointandtheunitsofa</sup> feature should not determine its attribution. Here is a concrete example: Imagine a model that takes temperature as a feature. ASI dictates that whether temperature is measured in Celsius or Farenheit, the attribution to the feature should be identical. 

- **Demand Monotonicity** if for every feature _i_ , and function _f_ that is non-decreasing in _i_ , the attribution of feature _i_ should only increase if the value of feature _i_ increases, with all else held fixed. This simply means that if the function is monotone in a feature, that feature’s attribution should only increase if the explicand’s value for that feature increases. 

- **Proportionality** If the function _f_ can be rewritten as a function of<sup>�</sup> _i_<sup>_xi_,</sup> and the baseline (x’) is zero, then the attributions are proportional to the explicand values(x). 

5 

## **2.7 An Empirical Case Study: Diabetes Prediction** 

While the bulk of this paper is axiomatic and theoretical, we will replicate some of our observations on a diabetes prediction task. The motivation is to show that many of the issues we identify theoretically show up in practice, and that too in the simplest possible setting, indicating that the issues are commonplace. We train our diabetes prediction models on a data set from the Scikit learning library [14]; this data set was originally used in [6]. The data has ten base features, age, sex, body mass index (BMI), average blood pressure (BP), and six blood serum measurements. Data is obtained for each of 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after the time of measurement of the base features. 

We train a linear model using Scikit’s implementation of Lasso regression [20]; we used the standard settings of the fitting algorithm and 75%-25% train-test split. The variance explained by the model is 35%. The model coefficients are 399 for BMI, 4.9 for BP and 291 for the fifth blood serum measurement (s5). The intercept is 154.15, which closely matches the data set average of response. 

# **3 An Analysis of CES** 

While CES was proposed by [10], and justified axiomatically (by citing the original Shapley axiomatization), the justification did not cover the choice of using conditional expectations as the set function (recall the definition of CES in Section 2.2). Furthermore, it appears that CES has only been applied with modification: For instance, [21], assumes an independent feature distribution while [10] applies it to modules of a deep network rather than end-to-end. Consequently, the properties have CES have not been carefully studied. This is what we remedy in this section. 

## **3.1 Comprehending CES(** _D_<sup>ˆ</sup> **)** 

As discussed in Sections 1 and 2.2, CES attributions depend crucially on the choice of the distribution _D_ . Arguably, the most obvious choice is to use the training data distribution _D_<sup>ˆ</sup> ; we call this CES( _D_<sup>ˆ</sup> ). 

Unfortunately, the properties of CES( _D_<sup>ˆ</sup> ) are not immediately apparent from its definition; the functional forms of the Shapley value and conditional expectations are sufficiently complex as to prevent direct understanding. We therefore begin by redefining CES( _D_<sup>ˆ</sup> ) as an intuitive procedure. 

The input is the (training) data, i.e., a list of examples _T_ = _{x_<sup>_t_</sup> _}_ . (We use superscripts to index examples and subscripts to index features.) Given an explicand _x_ , _TS_ is the subset of _T_ that agrees with _x_ on the features in the set _S_ , i.e., _TS_ = _{x_<sup>_t_</sup> _|∀i ∈ S, x_<sup>_t_</sup> _i_<sup>=</sup><sup>_xi}_.Noticethat</sup><sup>_T{}_=</sup><sup>_T_,and</sup><sup>_TN_=</sup><sup>_{xi}_.Thevalue</sup> of the set function _v_ ( _S_ ) is the average value of the function over inputs in the set _TS_ ; this corresponds to computing the conditional expectation _E_ [ _f_ ( _x_ ) _|xS_ )] in the CES approach (Section 2.2). 

6 

We now use the procedural definition of the Shapley value (see Section 2.1), i.e., we average the marginal contribution of ’adding’ variable _i_ (i.e., conditioning on it) over permutations of the variables. We notice that conditioning on an additional variable _i_ only reduces examples that ’agree’ with _x_ on the conditioned features. We call this the Downward Closure property<sup>2</sup> : 

**Lemma 3.1** (Downward Closure) **.** _For every pair of sets of features S, S_<sup>_′_</sup> _, if S ⊆ S_<sup>_′_</sup> _then TS′ ⊆ TS. (Proof in Appendix.)_ 

Putting these observations together, we have Algorithm 1. (If needed, the computation can be further sped up by sampling over permutations as is common with the Shapley value, and by caching values of the sets _Ti_ for all _i_ .) 

**Algorithm 1** Computing CES( _D_<sup>ˆ</sup> <u>)</u> 

Inputs: explicand _x_ and examples _T_ , each over feature set _N {_ Compute Shapley values via permutations _} sσi ←_ 0 for all _i_ **for all** permutations _σ_ of _N_ **do** <u>1</u> _vnew ← |T |_ � _x∈T_<sup>_f_(</sup><sup>_x_)</sup> _T_<sup>_′_</sup> _← T_ **for all** _i ∈_ 1 _. . . |N |_ **do** _vold ← vnew {_ Use the Downward Closure Lemma to update _T_<sup>_′_</sup> _}_ **for all** _t ∈ T_<sup>_′_</sup> **do** _{σi_ is the _i_ th feature in the ordering _σ}_ **if** _x_<sup>_t_</sup> _σi̸_<sup>=</sup><sup>_xi_</sup><sup>**then**</sup> delete _t_ from _T_<sup>_′_</sup> **end if end for** <u>1</u> _vnew ← |T_<sup>_′_</sup> _|_ � _x∈T_<sup>_′ f_(</sup><sup>_x_)</sup> _{_ Update Shapley value of _i_ th feature in ordering _σ} sσi ← sσi_ + _|N_ <u>1</u> _|_ !<sup>(</sup><sup>_vnew −vold_)</sup> **end for end for** 

## **3.2 The Effect of Sparsity on CES(** _D_<sup>ˆ</sup> **)** 

Our main motivation for providing a procedure for CES( _D_<sup>ˆ</sup> ) is to understand its properties. Our first observation is that CES( _D_<sup>ˆ</sup> ) is extremely sensitive to the degree of sparsity; sparsity arises naturally when the variables are continuous because it unlikely that data points share feature values precisely. 

> 2We borrow the term from the frequent itemset mining literature (cf. [3]). In itemset mining, the downward closure property reflects that every subset of a frequent itemset is also frequent. Analogously, for every feature set _S_ , every row in _TS_ is also in _TS′_ for every subset _S_<sup>_′_</sup> _⊆ S_ . 

7 

**Remark 3.2.** _Suppose we have an explicand x such that every feature value xi is unique, i.e., it does not occur elsewhere in the training data. Then, notice that TS_ = _{x} for all non-empty sets S. Therefore in each permutation, the first feature gets attribution f_ ( _x_ ) _− Ex′ D_ [ _f_ ( _x_<sup>_′_</sup> )] _while all the other features get an attribution of zero. Therefore all the variables get_ **_equal_** _attributions, even if the function is not symmetric in the variables!_ 

A practical implication of Example 3.2 is that the attributions would be very sensitive to noise in the data. For instance, Figure 1 shows the distribution of attributions across 20 explicands for CES( _D_<sup>ˆ</sup> ) (the second column in each plot) on the linear model. The attributions vary across features—for instance BMI has a larger variation than Sex. If we add a tiny amount of noise, and recompute attributions, then **all** the features (including BMI and Sex) will get **identical** attributions (we don’t show this in the figure). 

One way to deal with this sensitivity is to **smooth** the data. We can simulate smoothing within Algorithm 1. When we condition on a set _S_ of features in the computation of CES, we average the prediction over all the training data points that are **close** to the explicand in each of the features in _S_ ; two data points are close in a certain feature if their difference is within a certain fraction of the standard deviation. In our experiments, we use two settings 0 _._ 1 and 0 _._ 2. Figure 1 shows how different amounts of smoothing change the attributions (see for instance the attributions of the feature S2). Thus while smoothing mitigates sensitivity, it is still unclear how much smoothing to do. 

There are some other approaches to dealing with sparsity. One approach is to use the distribution Π( _D_<sup>ˆ</sup> ), i.e., the product of empirical marginal distributions, as in [5], or to assume that the function is somewhat smooth, and to compute the function’s value at a point outside the training data using a weighted sum of nearby points in the training data as in [1]. Again, these will undoubtedly give different results, and we cannot easily pick between them. 

## **3.3 An Axiomatic Analysis of CES(** _D_<sup>ˆ</sup> **)** 

As discussed in Section 2.1, the Shapley value and its variants were conceived in the context of cooperative game-theory where there is no analog of the feature distribution _D_ . The axioms (see Section 2.6) were meant to guarantee that if the set function has certain properties (the antecedent), then the Shapley values must have certain properties (the consequent). For instance, the Dummy axiom says that if a function is insensitive to a feature (the antecedent), then the feature should have zero attributions (the consequent). However, there are two functions at work here: the function _f_ whose value we wish to attribute, and the set function _v_ used to compute Shapley values. 

CES defines _v_ ( _S_ ) using conditional expectations that depend both on the function _f_ and the distribution _D_ . Consequently, even if the function _f_ satisfies certain properties, the consequent property of the axiom need not hold for _v_ . This gives rise to counter-intuitive attributions. We give several such examples in this section. These do not imply that prior axiomatizations (cf. [10] or [5]) 

8 

are incorrect. The various axioms still hold for the _v_ based on the conditional expectation (see Section 2.2). However, the axioms have no natural interpretation for this set function. In contrast, it is natural to seek interpret axioms as properties of the model function _f_ . 

In all our examples, each row of the table is a combination of feature values; the first column specifies the probability of this feature combination, the next two columns specify the feature values for two discrete, abstract features _T_ and _B_ , and the remaining columns specify the value of the function for this feature combination. Feature and function values used as explicand in the examples are in bold. 

**Example 3.3** (Failure of Dummy) **.** _See the function f_ 1 _in Table 1 modeled as a bivariate function of x and y. For the explicand x_ = 5 _, y_ = 5 _, the CES attributions are_<sup><u>22</u></sup> 2<sup>_<u>.</u>_</sup><sup><u>5</u></sup> _each for x and y (a consequence of Remark 3.2). Therefore the variable x gets a large attribution despite being dummy._ 

|Probability|_x_|_y_|_f_1=_y_<sup>2</sup>|_f_2 =_x_|_f_1+ _f_2|
|---|---|---|---|---|---|
|_ϵ_|**5**|**5**|**25**|**5**|**30**|
|1_−ϵ_|1|1|1|1|2|
|2<br>1_−ϵ_<br>2|1|2|4|1|5|



Table 1: Example for: (a) Dummy, correlated variables can have large CES attributions. (b) CES attributions are not linear in the function. 

The implication is this: Say, in the context of an analysis of fairness, we require that a certain feature play no role in the prediction model, and indeed, it does not. If we use CES, it may still be assigned significant attribution, leading us to incorrectly believe that the function is sensitive to the variable. In our diabetes prediction task, for the linear model (see Figure 1), we note that 7 of the 10 variables are dummy features. Despite this, CES assigns non-zero attributions to them. (In contrast, BShap assigns zero attributions to the dummy features.) 

**Example 3.4** (Failure of Linearity) **.** _See the functions f_ 1 _and f_ 2 _in Table 1; model them as univariate functions of y and x respectively. Consider the explicand x_ = 5 _, y_ = 5 _. Then the CES for the variable y with the function f_ 1 _is the difference between the function value at the explicand (_ 25 _) and the mean of the function (_ 2 _._ 5 _), i.e.,_ 22 _._ 5 _, and that for the function f_ 2 _is zero (y does not appear in the function). Now consider the attribution of y for the function f_ 1 + _f_ 2 _; both variables get an attribution of_<sup><u>30</u></sup><sup>_−_</sup> 2<sup><u>3</u></sup><sup>_<u>.</u>_</sup><sup><u>5</u></sup> _(again, a consequence of Remark 3.2), which is not_ 22 _._ 5 + 0 _._ 

Here is an implication: Imagine, if we were computing attributions for an ensemble of trees. Recall that the prediction of the forest is a uniform average over the trees, i.e., it is linear in the prediction of the trees. Therefore, we would expect the attributions to also be linear. But this is not the case. We saw large failures in linearity for the diabetes prediction task even for a two tree ensemble with trees of depth two. 

See Appendix C for how CES( _D_<sup>ˆ</sup> ) fails the Symmetry and Demand Monotonicity. 

9 



<!-- Start of picture text -->
age bmi bp s1 s2 s3 s4 s5 s6 sex<br>40 G<br>200 G GGGG G G G G G GGGGG G G GGG G G G G GG GGGG GGG GG G G G G G G GGG GGGGG G GGGG G GG GGGGGG G G G G GGG G GGG G G G G GG G G G GGGGGGGG G G GG G G G GG G G G G G G GGG GGG G GG G G GG G G G G GG GGGG G G GGG G GGG GGGG GG G G G G G G G G G GGG G G G GG G GG G G GGG G GGGG G G G GG GG G G GG G G G G G GG G G G G G G G GGG G G GG G G G G G G GGG G G G G G G GGGG GGGG G G G GG GG GGG G GGGG G G G G G G G GGGG GGGG G GG G G G G GG GG G G G G GG G GG G G GGG G GG G G GG GG GGG GG G G G G G GG GGG GG G G G G G GG GG GGGG G GGGGGG G G G G GGGG G G GG G G GGGGG G G G G GG G G G G G G G GGGG G GGGGGG GGG G G GG G GGG G G G GGG G G G GG GGG G G G GGGG G G GGG GGG GGGG GG G G GGGGGG G GGGG G G G G G G G G G G G G G G G G G Method GGG BSCESCES (0.1)<br>−20 G GGG G G G CES (0.2)<br>G<br>attribution<br><!-- End of picture text -->

Figure 1: Attribution distribution across 20 explicands for four methods, BShap, CES, CES (smoothing 0 _._ 1), CES (smoothing 0 _._ 2). 

# **4 Baseline Shapley and its Properties** 

In this section, we discuss the properties of BShap and provide a proper axiomatic result for it. (Recall the definition of Baseline Shapley (BShap) from Section 2.3.) As discussed in the introduction, prior axiomatization results from the machine learning literature (e.g. [5, 21, 10]) did not cover the choice of function input to the Shapley value, and consequently there are a multiplicity of methods that yield different results. 

## **4.1 BShap versus IG** 

The model explanation literature has largely built on top of the Shapley value from the binary cost-sharing literature. In this literature, players (features) are either present or absent. In contrast, machine learning tends to involve continuous features and deep learning involves only continuous features–even discrete/categorical are often turned into continuous features via embeddings. Therefore, it is worth connecting model explanation with the rich continuous cost-sharing literature. 

We begin by defining cost-sharing formally. 

A **cost-sharing problem** is an attribution problem with function _f_ , explicand _x_ and baseline _x_<sup>_′_</sup> such that the baseline _x_<sup>_′_</sup> = 0, the explicand _x_ is non-negative, and the function _f_ is non-decreasing in each variable, i.e., if two feature vectors _x_<sup>_−_</sup> _≤ x_<sup>+</sup> (point-wise for every feature), then _f_ ( _x_<sup>_−_</sup> ) _≤ f_ ( _x_<sup>+</sup> ).<sup>3</sup> 

There are several extensions of the Shapley value to the continuous cost sharing literature (see [7] for details). Two of these extensions correspond to BShap and IG. BShap is a generalization of a classic cost-sharing method called Shapley-Shubik (cf. [7]), and IG is a generalization of a cost-sharing method called Aumann-Shapley (cf. [4]). One can get Shapley-Shubik from BShap and Aumann-Shapley from IG by setting the baseline _x_<sup>_′_</sup> to zero; the explicand value 

> 3In [7], the function is defined to satisfy an additional property of being zero at _f_ (0); but this is only used to simplify the definition of the efficiency axiom (see Section 2.6 to not require the _f_ (0) term. 

10 

_xi_ corresponds to the demand of player _i_ , the function _f_ corresponds to the cost incurred, and the attributions to the cost-shares. 

It is relatively clear how Shapley-Shubik (BShap) is an extension of the binary Shapley value from its definition (see Section 2.3). 

However it is less clear how Aumann-Shapley (IG) (Equation 5) is an extension of the binary Shapley value. IG traverses a single, smooth path between the baseline and the explicand, and aggregates the gradients along this path. Whereas the Shapley value takes an average over several discrete paths—in each step of a discrete path, a variable goes from being ’off’ to ’on’ in one shot. To establish the connection, notice that the IG path can be seen to be the internal diagonal of a _N_ dimensional hypercube, and in contrast, the Shapley value is an average over the extremal paths over the edges of this hypercube. Suppose we partition every feature _i_ into _m_ micro features, where each micro feature represents a discrete change of the feature value of<sup>_xi_</sup> _m_<sup>_−x_</sup> _<u>i</u>_<sup>_′_</sup> . And then we apply the Shapley value on these _N ∗ m_ features. Notice that this is equivalent to creating a grid within the hypercube, and averaging over random, monotone walks from the baseline _x_<sup>_′_</sup> to the explicand _x_ in this grid. As _m_ increases, the density of the random walks converges to the diagonal of the hypercube, and if the function _f_ is smooth, then running Shapley on these micro-features is equivalent to running IG on the original features. 

Of course, in general, IG and BShap use different paths and hence give different attributions (see Example 4.5). 

The standard axiomatization of the Shapley value [16] only references (binary variants of) the first four axioms (Dummy, Efficiency, Linearity and Symmetry). However, in the continuous setting there are infinitely many methods that satisfy these four axioms. A uniqueness result requires further axioms, as we study in the next section. 

## **4.2 Axiomatizing BShap (and IG)** 

In this section, we provide axiomatizations for BShap and IG by formally reducing model explanation to cost-sharing: 

**Theorem 4.1** (Reducing Model Explanation to Cost-Sharing) **.** _Suppose there is an attribution method that satisfies Linearity and ASI. Then for every attribution problem with explicand x, baseline x_<sup>_′_</sup> _and function f (satisfying the minor technical condition that the derivatives are bounded) , then there exist two costsharing problems such that the resulting attributions for the attribution problem are the difference between cost-shares for the cost-sharing problems._ 

_Proof._ Given an attribution problem _f, x, x_<sup>_′_</sup> , we progressively transform it into equivalent cost-sharing problems. 

First, we transform the problem _f, x_<sup>_′_</sup> _, x_ into a problem _f_<sup>_n_</sup> _, x_<sup>_′n_</sup> _, x_<sup>_n_</sup> such that the baseline _x_<sup>_′n_</sup> is the zero vector, and _x_<sup>_n_</sup> is non-negative. The proof is inductive. The base case is by definition: we define _f_<sup>0</sup> _, x_<sup>0</sup> _, x_<sup>_′_0</sup> to be _f, x, x_<sup>_′_</sup> . In step _i_ we transform _f_<sup>_i−_1</sup> _, x_<sup>_i−_1</sup> _, x_<sup>_′i−_1</sup> into _f_<sup>_i_</sup> _, x_<sup>_i_</sup> _, x_<sup>_′i_</sup> by transforming along feature _i_ using 

11 

the transformation in the definition of ASI (see Section 2.6) using the _c_ = 1 if _xi_ is non-negative and _c_ = _−_ 1 otherwise, and _d_ = _−x_<sup>_′_</sup> _i_<sup>_∗c_.Theproofforthe</sup> inductive step: By ASI, the attribution for _f_<sup>_i−_1</sup> _, x_<sup>_i−_1</sup> _, x_<sup>_′i−_1</sup> should equal to that for _f_<sup>_i_</sup> _, x_<sup>_i_</sup> _, x_<sup>_′i_</sup> , and we have set the baseline value for this feature to 0, and its explicand value is non-negative. 

Next we express the function _f_<sup>_n_</sup> , as the difference of two non-decreasing functions _f_ 1 and _f_ 2. Let _p_ denote the infimum of the partial derivative<sup>_∂f_</sup> _∂x_<sup>_n_</sup><sup><u>(</u></sup> _i_<sup>_x_</sup><sup><u>)</u>,</sup> where _x_ ranges over the domain of the function _f_<sup>_n_</sup> , and _i_ ranges over all the variables. By the technical conditions, this infimum exists. If _p_ is zero or positive, then _f_<sup>_n_</sup> is itself non-decreasing—therefore set _f_ 1 to _f_<sup>_n_</sup> and _f_ 2 to the constant zero function. Otherwise, define _f_ 2 to be the linear function<sup>�</sup> _i_<sup>_−p ∗xi_;notice</sup> that _−p_ is positive and so the function is non-decreasing. Set _f_ 1 = _f_<sup>_n_</sup> + _f_ 2; by definition of _p_ , _f_ 1 is non-decreasing. By Linearity, the attributions for _f_<sup>_n_</sup> _, x_<sup>_n_</sup> _, x_<sup>_′n_</sup> , (which we have already shown are equal to the attributions for _f, x, x_<sup>_′_</sup> ) is the difference between the attributions of _f_ 1 _, x_<sup>_n_</sup> _, x_<sup>_′n_</sup> and _f_ 2 _, x_<sup>_n_</sup> _, x_<sup>_′n_</sup> . 

To complete the proof, notice that both _f_ 1 _, x_<sup>_n_</sup> _, x_<sup>_′n_</sup> and _f_ 2 _, x_<sup>_n_</sup> _, x_<sup>_′n_</sup> are costsharing problems. 

Both IG and BShap satisfy ASI and Linearity. Therefore **any** axiomatization that applies to Aumann-Shapley applies to IG and any axiomatization that applies to Shapley-Shubik applies to BShap. For instance, Corollary 1 from [7] reads: 

**Theorem 4.2.** _Shapley-Shubik is the unique method that satisfies the Efficiency, Linearity, Dummy, Affine Scale Invariance (ASI), Demand Monotonicity (DM) and Symmetry (plus some technical conditions we exclude for clarity) for all cost-sharing problems._ 

Therefore we have: 

**Corollary 4.3.** _BShap is the unique method that satisfies the Linearity, Dummy, Affine Scale Invariance (ASI), Demand Monotonicity (DM), and Symmetry (plus minor technical conditions) for all attribution problems. (See Proof in Appendix.)_ 

Analogously, we have the following corollary of Theorem 3 from [7]: 

**Corollary 4.4.** _IG is the unique method that satisfies the Linearity, Dummy, Affine Scale Invariance (ASI), Proportionality, and Symmetry (plus minor technical conditions) for all attribution problems._ 

**Remark 4.5** (BShap versus IG) **.** _A simple example where the IG and BShap differ is the min of two variables x_ 1 _and x_ 2 _. Suppose the baseline is x_<sup>_′_</sup> 1<sup>=</sup><sup>_x′_</sup> 2<sup>= 0</sup><sup>_,_</sup> _and the explicand is x_ 1 = 5 _, x_ 2 = 1 _. IG attributes the entire change in the function of_ 1 _to the arg min, i.e., x_ 2 _; this is intuitively reasonable if you see x_ 2 _as the critical variable. BShap on the other hand assigns attributions of_ 2 _._ 5 _to the first variable and −_ 1 _._ 5 _to the second; this is intuitively reasonable if you think of x_ 1 _as trying to increase the min and x_ 2 _as trying to decrease it. It is not immediately clear which interpretation is obviously superior._ 

12 

_Let us now consider the cube of the sum of two variables x_ 1 _and x_ 2 _. Suppose the baseline is x_<sup>_′_</sup> 1<sup>=</sup><sup>_x′_</sup> 2<sup>= 0</sup><sup>_,andtheexplicandisx_1= 5</sup><sup>_, x_2= 1</sup><sup>_.IGattributes_</sup> 180 _to x_ 1 _and_ 36 _to x_ 2 _, i.e., the attributions are in the ratio_ 5 : 1 _, a consequence of the proportionality axiom. BShap attributes_ 170 _to x_ 1 _and_ 46 _to x_ 2 _. The IG results appear a bit more principled. But there is a stronger consequence of the proportionality axiom: This axiom forces a smooth interpolation between the baseline and the explicand, i.e, the form of IG. For instance, a baseline of an entirely black image used in computer vision tasks results in intermediate inputs that are variants of the explicand with different intensities. In contrast, BShap is likely to construct more unrealistic inputs; in the vision examples, mixes of black pixels with the explicand pixels._ 

## **4.3 BShap fits in the CES framework** 

Thus far, we have studied the source of the difference between IG and BShap, both in terms of computation (they take different paths through a feature grid) and in terms of axioms (Corollary 4.3 versus Corollary 4.4). We now study the difference between BShap and CES. 

First, we show that one can **posit** a distribution _D_ such that the BShap approach coincides with CES under the distribution _D_<sup>4</sup> . This shows that BShap fits in the framework of CES. In this sense, any difference in the properties of BS and CES( _D_<sup>ˆ</sup> ) can be isolated to the choice of distribution on which to run CES. 

**Lemma 4.6.** _For any explicand x and baseline x_<sup>_′_</sup> _, there exists a feature distribution such that CES over that distribution results in attributions that are arbitrarily close to those produced by BShap. (Proof in Appendix)_ 

**Remark 4.7** (Explicit Comparison) **.** _Unlike CES(D_<sup>ˆ</sup> _), BShap does not depend on any distribution but requires an additional input (the baseline). We can use the baseline to model the explanation context. For instance, consider a model that makes loan decisions. If the applicant has been denied a loan, it is likely more useful to produce an explanation that only attributes to features that are in the applicant’s power to change (e.g. getting a high school diploma as opposed to reducing their age). Such an explanation is achievable by selecting a baseline that coincides with the explicand on immutable features. In this sense the baseline parameter is useful flexibility. It makes the attributions germane to the decision or actions of the person consuming the explanation. However, this does pose an additional cognitive load to select the baseline and interpret the dependence of the explanation on the baseline. There are also situations where there is no compelling choice of one baseline over another. In this situation, RBShap presents an alternative._ 

> 4[10] shows that CES reduces to BShap if the baseline is the feature means, **if** the features are independently distributed **and** the model is linear. Our reduction applies to non-linear models and baselines other than the feature means. 

13 

## **4.4 CES and RBShap** 

In Section 3, we saw that CES violates axioms like Dummy and Linearity. In contrast, Theorem 4.3 shows that BS satisfies these axioms. But since Lemma 4.6 shows that BS is a variant of CES, one could ask if there are other variants of CES that also satisfy some of the axioms. 

We first note that several axioms (Dummy, Linearity, Demand Monotonicity) also apply to RBShap, because these are satisfied by BShap and preserved by averaging the attributions over several baselines. (Symmetry requires that the distribution _D_ is symmetric in features over which the function _f_ is symmetric.) We now note that CES over an independent distribution _D_ is equal to RBShap where the baselines are drawn from distribution _D_ . Therefore, these axioms also carry over to CES **if** the feature distribution _D_ is independent. 

**Lemma 4.8.** _If the distribution D is an independent distribution over the features, then RBShap and CES coincide. (Proof in Appendix)_ 

**Remark 4.9.** _If the function f is linear and the distribution is independent, then, BShap with the baseline vector that has each feature set to its average across the data set, has the same attributions as CES (a consequence of Equation 9-12 from [10]) and hence RBShap (due to Lemma 4.8)._ 

**Remark 4.10.** _[5] runs CES over an independent feature distribution D_<sup>_′_</sup> _that is a product of the marginal distributions of the input feature distribution D. By Lemma 4.8, CES over D_<sup>_′_</sup> _is equivalent to RBShap over D_<sup>_′_</sup> _. One could ask if RBShap on the contrived feature distribution D_<sup>_′_</sup> _is equivalent to RBShap on the original feature distribution D. The following example proves that this is false, by showing that the sum of the attributions in the two cases differ: Suppose we are given two binary features x_ 1 _and x_ 2 _, function f_ ( _x_ 1 _, x_ 2) = _x_ 1 _∗ x_ 2 _and a distribution D such that P_ (0 _,_ 0) = _P_ (1 _,_ 1) = 0 _._ 5 _. Suppose that the explicand is x_ 1 = 1 _, x_ 2 = 1 _. Under D, E_ [ _f_ ( _x_ )] = 0 _._ 5 _. Under D_<sup>_′_</sup> _, E_ [ _f_ ( _x_ )] = 0 _._ 25 _. Recall that RBShap attributions sum to f_ ( _x_ ) _− E_ [ _f_ ( _x_ )] _; this completes our counterexample. This shows that forcing independence by constructing a marginal distribution is different from working with an independent distribution._ 

**Remark 4.11.** _Though CES over an independent distribution satisfies several axioms, it can fail Strong Monotonicity as the example in Table 4 shows; the distribution in this example is independent._ 

**Remark 4.12.** _The examples in Section 3.3, show that if the distribution is not independent, CES can fail Linearity, Dummy and Demand Monotonicity. However, it always satisfies Affine Scale Invariance (we omit the easy but technical proof)._ 

# **5 Conclusions** 

We show that Shapley with Conditional Expectations is highly sensitive to data sparsity, and can produce counterintuitive attributions. We produce proper 

14 

axiomatizations (uniqueness results) for Baseline Shapley and Integrated Gradients. 

# **References** 

- [1] Aas, K., Jullum, M., and Løland, A. Explaining individual predictions when features are dependent: More accurate approximations to Shapley values. _arXiv e-prints_ (Mar 2019), arXiv:1903.10464. 

- [2] Agarwal, A., Dhamdhere, K., and Sundararajan, M. A new interaction index inspired by the taylor series. _CoRR abs/1902.05622_ (2019). 

- [3] Agrawal, R., and Srikant, R. Fast algorithms for mining association rules. In _Proc. of 20th Intl. Conf. on VLDB_ (1994), pp. 487–499. 

- [4] Aumann, R. J., and Shapley, L. S. _Values of Non-Atomic Games_ . Princeton University Press, Princeton, NJ, 1974. 

- [5] Datta, A., Sen, S., and Zick, Y. Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems. In _2016 IEEE Symposium on Security and Privacy (SP)_ (Los Alamitos, CA, USA, may 2016), IEEE Computer Society, pp. 598–617. 

- [6] Efron, B., Hastie, T., Johnstone, I., and Tibshirani, R. Least angle regression. _Annals of Statistics 32_ (2004), 407–499. 

- [7] Friedman, E., and Moulin, H. Three methods to share joint costs or surplus. _Journal of Economic Theory 87_ , 2 (1999), 275 – 312. 

- [8] Gromping,¨ U. Estimators of relative importance in linear regression based on variance decomposition. _The American Statistician 61_ , 2 (2007), 139–147. 

- [9] Lindeman, R.H., P. M., and Gold., R. Introduction to bivariate and multivariate analysis. Tech. rep., 1980. 

- [10] Lundberg, S., and Lee, S.-I. A unified approach to interpreting model predictions. In _NIPS_ (2017). 

- [11] Lundberg, S. M., Erion, G. G., and Lee, S. Consistent individualized feature attribution for tree ensembles. _CoRR abs/1802.03888_ (2018). 

- [12] Owen, A. Sobol’ indices and shapley value. _SIAM/ASA Journal on Uncertainty Quantification 2_ , 1 (2014), 245–251. 

- [13] Owen, A., and Prieur, C. On shapley value for measuring importance of dependent inputs. _SIAM/ASA Journal on Uncertainty Quantification 5_ , 1 (2017), 986–1002. 

15 

- [14] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., and Duchesnay, E. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research 12_ (2011), 2825–2830. 

- [15] Ribeiro, M. T., Singh, S., and Guestrin, C. ”why should I trust you?”: Explaining the predictions of any classifier. _CoRR abs/1602.04938_ (2016). 

- [16] Shapley, L. S. A value of n-person games. _Contributions to the Theory of Games_ (1953), 307–317. 

- [17] Strumbelj,<sup>ˇ</sup> E., Kononenko, I., and Sikonja,<sup>ˇ</sup> M. R. Explaining instance classifications with interactions of subsets of feature values. _Data & Knowledge Engineering 68_ , 10 (2009), 886–904. 

- [18] Sun, Y., and Sundararajan, M. Axiomatic attribution for multilinear functions. _CoRR abs/1102.0989_ (2011). 

- [19] Sundararajan, M., Taly, A., and Yan, Q. Axiomatic attribution for deep networks. In _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_ (2017), D. Precup and Y. W. Teh, Eds., vol. 70 of _Proceedings of Machine Learning Research_ , PMLR, pp. 3319–3328. 

- [20] Tibshirani, R. Regression shrinkage and selection via the lasso. _Journal of the Royal Statistical Society: Series B (Methodological) 58_ , 1 (1996), 267–288. 

- [21] Strumbelj,<sup>ˇ</sup> E., and Kononenko, I. Explaining prediction models and individual predictions with feature contributions. _Knowl. Inf. Syst. 41_ , 3 (Dec. 2014), 647–665. 

- [22] Young, H. P. Monotonic solutions of cooperative games. _International Journal of Game Theory 14_ , 2 (Jun 1985), 65–72. 

16 

# **A Strong Monotonicity** 

We introdoce an additional axiom called Strong Monotonicity that plays a role in the results in the Appendix. 

**Strong Monotonicity** if for every two functions, _f_ 1 and _f_ 2, on the same domain, if for some feature _i_ , at all points _x_ in the domain,<sup>_∂f_</sup> _∂x_<sup>2(</sup> _i_<sup>_x_</sup><sup><u>)</u></sup> _≥_<sup>_∂f_</sup> _∂x_<sup>1(</sup> _i_<sup>_x_</sup><sup><u>)</u></sup> _≥_ 0, then the magnitude of attribution of feature _i_ for function _f_ 2 is at least as large as that for function _f_ 1<sup>5</sup> . A simple example will help clarify this axiom: Imagine that _f_ 1 and _f_ 2 are both linear models on an identical feature set. Moreover, the coefficients of all the features except one (call this feature _i_ ) are identical; say that _f_ 2 has a large positive coefficient for this feature _i_ , while _f_ 1 has a small positive coefficient. This satisfies the conditions on the partial derivative in the antecedent of the axiom. Since the coefficient of feature _i_ in function _f_ 2 is larger, it is reasonable for feature _i_ to have an attribution of greater magnitude for _f_ 2 than for _f_ 1. 

# **B Issues with prior Axiomatic Results** 

[10] claims to show that one of the standard axioms (Symmetry) used in the Shapley axiomatization is redundant within an earlier axiomatization of the Shapley value by [22]. It claims that Missingness, Local Accuracy and Consistency suffice. (The latter two axioms are called Efficiency and Strong Monotonicity by [22]). This claim is incorrect. Here is the counterexample: Suppose that the function is _x_ 1 _∗ x_ 2 _∗ x_ 3, with all three feature values identically 1 in the explicand. Assume that the features are independently and identically distributed over the discrete set _{_ 0 _,_ 1 _}_ , with a probabilities 1 _− ϵ_ and _ϵ_ for values 0 and 1 respectively. Shapley gives identical shares to all three variables, 1 _/_ 3. Now, consider an alternate attribution method: Take a fixed permutation of the three variables, _x_ 1 _→ x_ 2 _→ x_ 3 and define the attributions to be the marginals of this permutation as in Section 2.1. This method satisfies missingness, local accuracy, and consistency, but yields different attributions from Shapley values—the third variable gets an attribution of 1 and the rest get attributions of 0. 

The axiomatization for Deep Shap in [10] is problematic in a different way: In Deep Shap, the Shapley value is applied layer by layer rather than to the network as a whole. This destroys the guarantees of the Shapley axioms because the attributions become sensitive to the arrangement of parameters in the network, as opposed to the function that the network computes. Here is an an analogy using a simple function _x_ 1 _∗ x_ 2 _∗ x_ 3. Consider an ‘implementation’ of the function first computes _x_ 1 _∗ x_ 2 and then multiplies it with _x_ 3, i.e., (( _x_ 1 _∗ x_ 2) _∗ x_ 3). Let us say that the feature values are all identically 1 in the explicand and identically 0 in the baseline. Deep Shap would attribute half to _x_ 3 and half to the product _x_ 1 _∗ x_ 2, it would then redistribute the half equally among _x_ 1 and _x_ 2, resulting in attributions that are a 1 _/_ 4 each for _x_ 1 and _x_ 2 and 1 _/_ 2 for _x_ 3. If the ‘implementation’ was ( _x_ 1 _∗_ ( _x_ 2 _∗ x_ 3)) instead, then the attributions would be 

> 5A slight generalization of the cost-sharing axiom from [22]. 

17 

1 _/_ 2 for _x_ 1 and 1 _/_ 4 each for _x_ 2 and _x_ 3. Notice that both attributions are also a violation of the symmetry axiom. Applying the BShap end-to-end would result in attributions of<sup><u>1</u></sup> 3<sup>each.</sup> 

# **C How CES(** _D_<sup>ˆ</sup> **) fails other Axioms** 

**Example C.1** (Failure of Demand Monotonicity) **.** _See the example in Table 2. The CES attribution for feature y for the explicand x_ = 1 _, y_ = 0 _(a positive number) exceeds that for the explicand x_ = 1 _, y_ = 1 _(a negative number); Notice that the explicands differ only the value of feature y and the function f is monotone; therefore this is a failure of Demand Monotonocity._ 

|Probability|_x_|_y_|_f_=100_∗x_+ _y_|
|---|---|---|---|
|1_/_3|**1**|**1**|**101**|
|1_/_3|**1**|**0**|**100**|
|1_/_3|0|1|1|



Table 2: Increasing the feature value of _y_ , can reduce its CES attribution, even though _f_ is monotone. 

An implication of the above example is that it may lead the consumer of the explanation to believe that the function is non-monotone, even if this is not the case. 

**Example C.2** (Failure of Symmetry) **.** _In Table 3, the function is symmetric in both variables. Furthermore, the variables are distributed independently; variable T is_ 2 _with probability p and_ 1 _with the remaining probability; variable B is_ 2 _with probability q and_ 1 _with the remaining probability. For the symmetric explicand T_ = 2 _, B_ = 2 _, variable T gets attribution_ 1 _− p and variable B gets attribution_ 1 _− q, a violation of symmetry when p̸_ = _q._ 

|Probability|_x_|_y_|_f_ =|_x_+ _y_|
|---|---|---|---|---|
|(1_−p_)_∗_(1_−q_)|1|1|2||
|(1_−p_)_∗q_|1|2|3||
|_p ∗_(1_−q_)|2|1|3||
|_p ∗q_|**2**|**2**|**4**||



Table 3: CES can give symmetric variables unequal attributions, even if the distribution _D_ is independent. 

An implication of the above example is that it may lead the consumer of the explanation to believe the two variables are not symmetric, even if they actually are. 

**Example C.3** (Failure of Strong Monotonicity) **.** _Table 4 shows an example where the function f_ 2 _has larger partial derivatives for variable x than f_ 1 _at each point in its domain (the domain is x ≥_ 1 _, y ≥_ 1 _). Also, the two variables are independently distributed. Now consider the explicand x_ = 2 _, y_ = 2 _. The attribution to the_ 

18 

_variable x is lower for f_ 2 _than for f_ 1 _(going from_<sup><u>2</u></sup> _~~<u>√</u>~~_ <u>2</u> _−_ 31 _−_ _~~<u>√</u>~~_ <u>3</u> _≈_ 0 _._ 032 _to_ 0 _), a violation of Strong Monotonicity._ 

|Probability|_x_|_y_|_f_1 =|<sup>_~~√~~_</sup><br>_x_+ _y_|_f_2 =|_x_+ _y_|
|---|---|---|---|---|---|---|
|1_/_6|1|1|2||2||
|1_/_6|2|1|1 +|_~~√~~_<br>2|3||
|1_/_6|3|1|1 +|_~~√~~_<br>3|4||
|1_/_6|1|2|3||3||
|1_/_6|**2**|**2**|**2**+|_~~√~~_<br>**2**|**4**||
|1_/_6|3|2|2 +|_~~√~~_<br>3|5||



Table 4: Increasing a variable’s influence can reduce its CES attributions, even when the distribution is independent. 

An implication of this example is that even if we strengthen a variable’s influence, its CES attribution could nevertheless fall. This is because the function transformation influences the function value on points in the background distribution more strongly than at the explicand. 

We did not observe significant failures of Demand Monotonicity in this empirical study; both models we studied were asymmetric in the variables, so no failure of Symmetry was possible. 

# **D Proofs** 

## **D.1 Proof of Lemma 3.1** 

_Proof._ Consider an _x_<sup>_t_</sup> that belongs to _TS_<sup>_′_</sup> . We note that it also belongs to _TS_ . This is because an example that agrees with the explicand on a feature set _S_<sup>_′_</sup> also agrees with the explicand on every feature set _S_ that is a subset of _S_<sup>_′_</sup> . 

## **D.2 Proof of Lemma 4.6** 

_Proof._ We construct the feature distribution for CES as follows: the distribution for feature _i_ has two points in its support, _xi_ and _x_<sup>_′_</sup> _i_<sup>,wherePr(</sup><sup>_xi_)=</sup><sup>_ϵ_and</sup> Pr( _x_<sup>_′_</sup> _i_<sup>) = 1</sup><sup>_−ϵ_.ItsufficestoshowthatthesetfunctionsinputtotheShapley</sup> value for the two approaches have values that are arbirarily close when _ϵ →_ 0. The set function for CES is: 



Because _ϵ →_ 0, the numerator is dominated by the term where _S_<sup>_′_</sup> is empty, and the numerator tends to _f_ ( _xS_ ; _x_<sup>_′_</sup> _N \S_<sup>)</sup><sup>_∗_(1</sup><sup>_−ϵ_)</sup><sup>_|N\S|_.By an analogous argument,</sup> the denominator tends to (1 _− ϵ_ )<sup>_|N\S|_</sup> . Dividing, we get the set function for BShap. 

19 

## **D.3 Proof of Lemma 4.8** 

_Proof._ In the special case that the features follow an independent distribution we show that the set function _v_ ( _S_ ) for RBShap and CES are the same for all sets _S_ . Fix a set _S_ and consider _v_ ( _S_ ) for RBShap: 



where 8 follows because the expression is dummy in _x_<sup>_′_</sup> _S_<sup>;9isduetofeature</sup> independence; and the final expression is the set function for CES. 

## **D.4 Proof of Corollary 4.3** 

_Proof._ It is easy to show that BShap satisfies all the axioms (we skip this part). Now consider the reverse direction, i.e., we would like to show that no other method satisfies these axioms. By Theorem 4.1, and because the attribution method satisfies Linearity and ASI, the attributions for an attribution problem are the difference between the cost-shares for two cost-sharing problems, and these cost-shares are uniquely determined by Theorem 4.2. 

20 

