---
title: "Feature relevance quantification in explainable AI: A causal problem"
authors: "problem"
year: 2019
arxiv_id: "1910.13413"
original_file: "1910.13413.pdf"
pdf_path: "docs/papers\2019_problem_feature_relevance_quantification_in.pdf"
---

# Feature relevance quantification in explainable AI: A causal problem

**Authors:** Problem et al.  
**Year:** 2019 | **arXiv:** [`1910.13413`](https://arxiv.org/abs/1910.13413)  
**Local PDF:** [`2019_problem_feature_relevance_quantification_in.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_problem_feature_relevance_quantification_in.pdf)

---

# **Feature relevance quantification in explainable AI: A causal problem** 

Dominik Janzing, Lenon Minorics, and Patrick Bl¨obaum 

Amazon Research T¨ubingen, Germany 

_{_ janzind, minorics, bloebp _}_ @amazon.com 

25 November 2019 

## **Abstract** 

We discuss promising recent contributions on quantifying feature relevance using Shapley values, where we observed some confusion on which probability distribution is the right one for dropped features. We argue that the confusion is based on not carefully distinguishing between _observational_ and _interventional_ conditional probabilities and try a clarification based on Pearl’s seminal work on causality. We conclude that _unconditional_ rather than _conditional_ expectations provide the right notion of _dropping_ features in contradiction to the theoretical justification of the software package SHAP. Parts of SHAP are unaffected because unconditional expectations (which we argue to be conceptually right) are used as _approximation_ for the conditional ones, which encouraged others to ‘improve’ SHAP in a way that we believe to be flawed. 

## **1 Motivation** 

Despite several impressive success stories of deep learning, not only researchers in the field have been shocked more recently about lack of robustness for algorithms that were actually believed to be powerful. Image classifiers, for instance, fail spectacularly once the images are subjected to adversarial changes that appear minor to humans, see e.g. Goodfellow et al. (2015); Sharif et al. (2016); Kurakin et al. (2018); Eykholt et al. (2018); Brown et al. (2018). Understanding these failures is challenging since it is hard to analyze which features were decisive for the classification in a particular case. However, 

lack of robustness is only one of several different motivations for getting artificial intelligence _interpretable_ . Also the demand for getting _fair_ decisions, e.g., Dwork et al. (2012); Kilbertus et al. (2017); Barocas et al. (2018), requires understanding of algorithms. In this case, it may even be subject of legal and ethical discussions _why_ an algorithm came to a certain conclusion. 

To formalize the problem, we describe the input / output behaviour as a function _f_ : _X_ 1 _, . . . , Xn →_ R where _X_ 1 _, . . . , Xn_ denote the ranges of some input variables ( _X_ 1 _, . . . , Xn_ ) =: **X** (discrete or continuous), while we assume the target variable _Y_ to be real valued for reasons that will become clear later. Given one particular input **x** := ( _x_ 1 _, . . . , xn_ ) we want to quantify to what extent each _xj_ is ‘responsible’ for the output _f_ ( _x_ 1 _, . . . , xn_ ). This question makes only sense, of course, after specifying what should one input be _instead_ . Let us first consider the case where **x** is compared to some ‘baseline’ element **x**<sup>_′_</sup> , which has been studied in the literature mostly for the case of real-valued inputs and differentiable _f_ . Based on a hypothetical scenario where only some of the baseline values _x_<sup>_′_</sup> _j_<sup>arereplacedwith</sup><sup>_xj_whileothers arekept one</sup> wants to quantify to what extent each component _j_ contributes to the difference _f_ ( **x** ) _− f_ ( **x**<sup>_′_</sup> ). The focus of the present paper, however, is a scenario where the baseline is defined by the expectation E[ _f_ ( **X** )] over some distribution _P_ **X** . To explain the relevance of each _j_ for the difference _f_ ( **x** ) _−_ E[ _f_ ( **X** )] one considers a scenario where only some values are kept and the remaining ones are _averaged over some probability distribution_ . The main contribution of this paper is to discuss which distribution is 

1 

the right one. Recalling the difference between _interventional_ and _observational_ conditional distributions in the field of causality, we explain why we disagree with the interesting proposal of Lundberg and Lee (2017) in this regard. Further we argue that our criticism is irrelevant for any software that ‘approximates’ the conditional expectation (which we consider conceptually wrong) by the unconditional expectation, as proposed by Lundberg and Lee (2017). The paper is structured as follows. Section 2 summarizes results from the literature regarding axioms for feature attribution for the case where there is a unique baseline reference input. Here integrated gradients and Shapley values (as the generalization to discrete input) are the unique attribution functions for the stated set of axioms. Section 3 discusses the attribution problem for the case where one averages over unused features as in Lundberg and Lee (2017), and then we present our criticism. We think that the big overlap of the present paper with existing literature is justified by aiming at this clarification only, while keeping this clarification as selfconsistent as possible. In particular, the very general discussion of Datta et al. (2016) contains all the ideas of this work at least implicitly, but since it appeared before Lundberg and Lee (2017) it could not explicitly discuss the conceptual problems raised by the latter. Our view on marginalization over unused features is supported by Datta et al. (2016) for similar reasons. In Section 4 we present different experiments which illustrate our arguments. 

### **2.1 Integrated gradient** 

Sundararajan et al. (2017), investigated the attribution of _xi_ to the difference 



where **x**<sup>_′_</sup> is a given baseline. Under the assumption that _f_ is differentiable almost everywhere<sup>1</sup> , they defined the attribution of _xi_ to (1) as 



Contrary to LIME, DeepLIFT and LRP, this attribution method has the advantage that all of the following 5 properties are satisfied (see Sundararajan et al. (2017) and Aas et al. (2019)): 

_1. Completeness:_ If _atri_ ( **x** ; _f_ ) denotes the attribution of _xi_ to (1), then 



_2. Sensitivity:_ If _f_ does not depend on _xi_ , then _atri_ ( **x** ; _f_ ) = 0. 

_3. Implementation Invariance:_<sup>2</sup> If _f_ and _f_<sup>_′_</sup> are equal for all inputs, then 

_atri_ ( **x** ; _f_ ) = _atri_ ( **x** ; _f_<sup>_′_</sup> ) for all _i._ 

## **2 Prior Work** 

The growth of deep neural networks recently motivated many researchers to investigate feature attribution, see e.g. Shrikumar et al. (2016) for DeepLIFT, Binder et al. (2016) for Layer-wise Relevance Propagation (LRP), Ribeiro and Singh (2016) for Local Interpretable Modelagnostic Explanations (LIME), and for gradient based methods Chattopadhyay et al. (2019). For a summary of common architecture agnostic methods, see Molnar (2019). We first discuss two closely related concepts that arise from an axiomatic approach. 

_4. Linearity:_ For _a, b ∈_ R holds 



_5. Symmetry-Preserving:_ If _f_ is symmetric in component _i_ and _j_ and _xi_ = _xj_ and _xi_<sup>_′_=</sup><sup>_x′_</sup> _j_<sup>, then</sup> 



> 1see Sundararajan et al. (2017, Proposition 1) 

> 2Note that this axiom is pointless if it refers to properties of _functions_ rather than properties of _algorithms_ . We have listed it for completeness and for consistency with the literature. 

2 

Integrated gradients can be generalized by integrating over an arbitrary path _γ_ instead of the straight line. This attribution method is called _path method_ and the following theorem holds. 

**Theorem 1.** _((Friedman, 2004, Theorem 1) and (Sundararajan et al., 2017, Theorem 1)) If an attribution method satisfies the properties Completeness, Sensitivity, Implementation Invariance and Linearity, then the attribution method is a convex combination of path methods. Furthermore, integrated gradients is the only path method that is symmetry preserving._ 

Notice that convex combinations of path methods can also be symmetry preserving even if the attribution method is not given by integrated gradients. 

### **2.2 Shapley values** 

To assess feature relevance _relative to the average_ , Lundberg and Lee (2017) use a concept that relies on first defining an attribution for binary functions, or, equivalently, functions with subset as input (’set functions’). We first explain this concept and describe in Section 3 how it solves the attribution relative to the expectation. Assume we are given a set with _n_ elements, say _U_ := _{_ 1 _, . . . , n}_ and a function 



We then ask to what extent each single _j ∈ U_ contributes to _g_ ( _U_ ). A priori, the contribution of each _j_ depends on the order in which more elements are included. We can thus define the contribution of _j_ , given _T ⊆ U_ by 



(note that it can be negative and also exceed _g_ ( _U_ )). With 



it then holds 



The quantity _φi_ is called the _Shapley value_ (Shapley, 1953) of _i_ , which can be considered the average contribution of _i_ to _g_ ( _U_ ). At first glance, Shapley values only solve the attribution problem for binary inputs by canonically identifying subsets _T_ with binary words _{_ 0 _,_ 1 _}_<sup>_n_</sup> . To show that Shapley values also solve the above attribution problem, one can simply define a set function by 



for any subset _T ⊆{_ 1 _, . . . , n}_ . Here, _fT_ is the ‘simplified’ function with the reduced input **x** _T_ obtained from _f_ when all remaining features are taken from the baseline input **x**<sup>_′_</sup> , that is, _f∅_ ( **x** _∅_ ) = _f_ ( **x**<sup>_′_</sup> ). 

Since Shapley Values also satisfy Completeness, Sensitivity, Implementation Invariance and Linearity (Aas et al., 2019) with respect to the binary function defined by the set function _g_ , they are given by a convex combination of path methods. Furthermore, Shapley Values with respect to _g_ are Symmetry-perserving, but don’t coincide with integrated gradients. 

Different ways of feature attribution based on Shapley Values were recently investigated by Sundararajan and Najmi (2019). Their main consideration is feature relevance relative to an auxiliary baseline, but feature attribution relative to the expectation (according to an arbitrary distribution) is also mentioned. Furthermore, Sundararajan and Najmi (2019) already discussed that Shapley Values based on conditional distributions can assign unimportant features non-zero attribution. However, Sundararajan and Najmi (2019) didn’t consider the problem from a causal perspective. 

## **3 How should we sample the** _dropped_ **features?** 

We now want to attribute the difference between _f_ ( **x** ) and the expectation E[ _f_ ( **X** )] to individual features. Explaining _why_ the output for one particular input **x** deviates strongly from the average output is particularly interesting for understanding ‘outliers’. Let us introduce some notation first. For any _T ⊆ U_ let E[ _f_ ( **x** _T ,_ **X** ¯ _T_ ) _|_ **X** _T_ = **x** _T_ ] denote the conditional expectation of _f_ , given **X** _T_ = **x** _T_ . By E[ _f_ ( **x** _T ,_ **X** ¯ _T_ )] we denote the expectation of _f_ ( **x** _T ,_ **X** ¯ _T_ ) 

3 

with respect to the distribution of **X** ¯ _T without conditioning_ on **X** _T_ = **x** _T_ . Let us call this expression ‘marginal expectation’ henceforth. 

Accordingly, we now discuss two different options for defining ‘simplified functions’ _fT_ where all features from _T_ ¯ are dropped: 





Lundberg and Lee (2017) propose (3), but since it is difficult to compute they _approximate_ it by (4), which they justify by the simplifying assumption of feature independence. Using the set function _g_ ( _T_ ) := _fT_ ( **x** ) _− f∅_ ( **x** ), they compute Shapley values _φi_ according to (2). We will argue that using (4) rather than (3) is conceptually the right thing in the first place. Our clarification is supposed to prevent others from ‘improving’ SHAP by finding an approximation for the conditional expectation that is better than the marginal expectation, like, for instance Aas et al. (2019) and (Lundberg et al., 2018)<sup>3</sup> 

To explain our arguments, let us first explain why marginal expectations occur naturally in the field of causal inference. 

**Observational versus interventional conditional distributions** The main ideas of this paragraph can already be found in Datta et al. (2016) in more general and abstract form, see also Friedman (2001) and Zhao and Hastie (2019), but we want to rephrase them in a way that optimally prepares the reader to the below discussion. Assume we are given the causal structure shown in Figure 1. Further, assume we are interested in how the expectation of _Y_ changes when we manually set _X_ 1 to some value _x_ 1. This is _not_ given by E[ _Y |X_ 1 = _x_ 1] because observing _X_ 1 = _x_ 1 changes also the distribution of _X_ 2 _, X_ 3 due to the dependences between _X_ 1 and _X_ 2 _, X_ 3 (which are generated by the common cause _Z_ ). This way, the difference between E[ _Y_ ] and E[ _Y |X_ 1 = _x_ 1] is not only due to the influence of _X_ 1, but can also be caused by the influence of _X_ 2 _, X_ 3. The impact of setting _X_ 1 to _x_ 1 is captured by 



<!-- Start of picture text -->
Z<br><!-- End of picture text -->



<!-- Start of picture text -->
X 1 X 2 X 3<br>Y<br><!-- End of picture text -->

Figure 1: A simple causal structure where the observational conditional _p_ ( _y|x_ 1) does not correctly describe how _Y_ changes after _intervening_ on _X_ 1 because the common cause _Z_ ‘confounds’ the relation between _X_ 1 and _Y_ . 

Pearl’s do-operator Pearl (2000) instead, which yields 



This can be easily verified using the backdoor criterion Pearl (2000) since (phrased in Pearl’s language) the variables _X_ 2 _, X_ 3 ‘block the backdoor path’ _X_ 1 _← Z → Y_ . Observations from _Z_ are not needed, we may therefore assume _Z_ to be latent, which we have indicated by white color. 

For our purpose, two observations are important: first, (5) does not contain the conditional distribution, given _X_ 1 = _x_ 1. Replacing _p_ ( _x_ 2 _, x_ 3) with _p_ ( _x_ 2 _, x_ 3 _|x_ 1) in (5) would yield the _observational_ conditional expectation E[ _Y |X_ 1 = _x_ 1], which we are not interested in. In other words, the intervention on _X_ 1 breaks the dependences to _X_ 2 _, X_ 3. The second observation that is crucial for us is that the dependences between _X_ 2 _, X_ 3 are kept, they are unaffected by the intervention on _X_ 1. 

**Why observational conditionals are flawed** Let us start with a simple example. 

**Example 1** (irrelevant feature) **.** _Assume we have_ 



3Note that TreeExplainer in SHAP has meanwhile been changed accordingly. 

_Obviously, the feature X_ 2 _is irrelevant. Let both X_ 1 _, X_ 2 

4 

_be binaries and_ 



#### **(1) with conditional expectations:** 



_Therefore,_ 



_Hence, the Shapley value for X_ 2 _reads:_ 



#### **(2) with marginal expectations:** 



_We then obtain_ 



_which yields φ_ 2 = 0 _._ 

The example proves the follow result, which were already discussed in Sundararajan and Najmi (2019): 

**Lemma 1** (failure of Sensitivity) **.** _When the relevance of φi is defined by defining ‘simplified’ functions fT via conditional expectations_ 



_then φi̸_ = 0 _does not imply that f depends on xi._ 

The example is particularly worrisome because we mentioned earlier that Shapley values satisfy the axiom of sensitivity, while Lemma 1 seems to claim the opposite. The resolve this paradox, note that the Shapley values refer to binary functions (or set functions) and reading (6) to (8) as the values of a binary function _g_ ˜ with inputs ( _z_ 1 _, z_ 2) = 00 _,_ 10 _,_ 01 _,_ 11 we clearly observe that _g_ ˜ depends also on the second bit. This way, the Shapley values do not violate sensitivity for ˜ _g_ , but we certainly care about ‘sensitivity for _f_ ’. Note that this distinction between the binary function ˜ _g_ and _f_ is crucial although in our example _f_ is binary itself. Fortunately, the second bit is irrelevant for the binary function ˜ _g_ defined by (10) and (13) and we do not obtain the above paradox. 

To assess the impact of changing the inputs of _f_ , we now switch to a more causal language and state that we consider the inputs of an algorithm as _causes_ of the output. Although this remark seems trivial it is necessary to emphasize that we are not talking about the causal relation between any features in the real world outside the computer (where the attribute predicted by _Y_ may be the cause of the features), but only about causality of this technical input / output system<sup>4</sup> . To facilitate this view, we formally distinguish between the true features _X_<sup>˜</sup> 1 _, . . . , X_<sup>˜</sup> _n_ obtained from the objects and the corresponding features _X_ 1 _, . . . , Xn_ plugged into the algorithm. This way, we are able to talk about a hypothetical scenario where the inputs are changed compared to the true features. Let us first consider the causal structure in figure 2, top, where the inputs are determined by the true features. In contrast, figure 2, bottom, shows the causal structure after an intervention on _X_ 1 _, X_ 2 has adjusted these variables to fixed values _x_ 1 _, x_ 2. 

We now consider the impact of an hypothetical intervention, which leaves the remaining components _unaffected_ . They are therefore sampled from their natural joint distribution _without_ conditioning. Similar to the above paragraph, we then obtain 



Our formal separation between the _true_ values of the features _X_<sup>˜</sup> _j_ of some object and the corresponding _inputs Xj_ of the algorithms allows us to be agnostic about the causal relations between the true features in the real world, the 

> 4Accordingly, _Y_ is the output of the system and not a property of the external world. 

5 

fact that the inputs _X_ 1 _, . . . , Xn cause_ the output _Y_ is the only causal knowledge needed to compute (14). Since the interventional expectations coincide with the marginal expectations, we have thus justified the use of marginal expectations for the Shapley values from the causal perspective. 



<!-- Start of picture text -->
object with features<br>X ˜1 X ˜2 X ˜3 X ˜4 X ˜5<br>X 1 X 2 X 3 X 4 X 5<br>Y<br>object with features<br>X ˜1 X ˜2 X ˜3 X ˜4 X ˜5<br>x 1 x 2 X 3 X 4 X 5<br>Y<br><!-- End of picture text -->

Figure 2: Top: Causal structure of our prediction scenario: The output _Y_ is determined by the inputs _X_ 1 _, . . . , Xn_ . In the usual learning scenario these inputs coincide with features _X_<sup>˜</sup> 1 _, . . . , X_<sup>˜</sup> _n_ ob some object, that is _Xj_ = _X_<sup>˜</sup> _j_ . Bottom: To evaluate the impact of some inputs, say _X_ 1 _, X_ 2, for the output _Y_ we consider a hypothetical scenario where we adjust these inputs to some fixed values _x_ 1 _, x_ 2 and sample the remaining inputs from the usual joint distribution _PX_ 3 _,...,Xn_ . 

|Probability|_X_1|_X_2|_f_ =|_X_1+_X_2|
|---|---|---|---|---|
|(1_−p_)_·_(1_−q_)|1|1|2||
|(1_−p_)_· q_|1|2|3||
|(1_−q_)_· p_|2|1|3||
|_p · q_|2|2|4||



Figure 3: Table 3 from Sundararajan and Najmi (2019) which shows an example for alleged lack of symmetry of Shapley Values with respect to the marginal expectation. 

**The problem with the symmetry axiom** We briefly rephrase Example 4.9 of Sundararajan and Najmi (2019) showing that the symmetry axiom is violated when Shapley values are used for quantifying the influence relative to conditional or marginal expectations. Figure 3 shows values and probabilities of two random variables _X_ 1 and _X_ 2 and the values of the function _f_ ( _X_ 1 _, X_ 2) = _X_ 1 + _X_ 2. As explained by Sundararajan and Najmi (2019), for the input ( _x_ 1 _, x_ 2) = (2 _,_ 2) the value _x_ 1 gets attribution (1 _−p_ ) and _x_ 2 gets attribution (1 _−q_ ). Therefore, if _p̸_ = _q_ , _x_ 1 and _x_ 2 get different attribution, although _f_ is symmetric. They conclude that this is a violation of symmetry. Since _X_ 1 and _X_ 2 are independent, this problem occurs regardless of whether one defines the simplified function _fT_ with respect to marginal or conditional expectations. One can argue, however, that this result makes intuitively sense because the value _xj_ that is farther from its mean contributes _more_ to the fact that _f_ ( _x_ 1 _, x_ 2) deviates from its mean. If we have even _x_ 1 = E[ _X_ 1], we would certainly say that _x_ 1 does not contribute to the deviation from the mean at all. For this reason we do not follow Sundararajan and Najmi (2019) in regarding this phenomenon as a problem of this kind of attribution analysis. Recall furthermore that we have already mentioned that the symmetry axiom does hold for the corresponding binary function defined by including or not certain features (simply because symmetry holds for Shapley values). For the above example this binary function is indeed asymmetric. To check this, define 



where _T_ is the set of all _j_ for which _zj_ = 1. This function is not symmetric in _Z_ 1 and _Z_ 2, since we have, for instance, ˜ _g_ (1 _,_ 0) = _x_ 1 + E[ _X_ 2] _̸_ = _g_ ˜(0 _,_ 1) = _x_ 2 + E[ _X_ 1]. 

6 

## **4 Numerical Evidence** 

In this section, we show numerically that the marginal expectation E[ _f_ ( **x** _T ,_ **X** ¯ _T_ )] is a better choice than = E[ _f_ ( **x** _T ,_ **X** ¯ _T_ ) _|_ **X** _T_ **x** _T_ ] to quantify the attribution = of each observation _xj_ of a particular input **x** ( _x_ 1 _, . . . , xn_ ) to _f_ ( **x** ) _−_ E _f_ ( **X** ). 

### **4.1 Computation of Shapley Values** 

As explained by Aas et al. (2019, Section 2.3), the implementation of KernelSHAP (Lundberg and Lee, 2017) consists of two parts: 

1. Using a representation of Shapley Values as the solution of a weighted least square problem for a computationally tractable approximation. 

2. Approximation of _g_ ( _T_ ). 

#### **4.1.1 Shapley Values as solution of weighted least square problem** 

By Charnes et al. (1988), the Shapley Values to the set function _g_ are given as the solution ( _φ_ 1 _, . . . , φn_ ) of 



where _k_ ( _U, T_ ) = ( _|U | −_ 1) _/_ (� _||UT ||_ � _|T |_ ( _|U | −|T |_ )) are the _Shapley kernel weights_ . Since _k_ ( _U, U_ ) = _∞_ , we use the constraint<sup>�</sup> _j_<sup>_φj_=</sup><sup>_g_(</sup><sup>_U_),or,fornumericalcalculation,</sup> we set _k_ ( _U, U_ ) to a large number. 

Since the power set of _U_ consists of 2<sup>_n_</sup> elements, the computation time of the Sharpley Values increases exponentially. KernelSHAP therefore samples subsets of _U_ according to the probability distribution induced by the Shapley kernel weights. 

#### **4.1.2 Approximation of the set function** 

As discussed in the previous sections, Lundberg and Lee (2017) define 



To evaluate the conditional expectation, they assume feature independence (or weak dependence) to obtain E[ _f_ ( **x** _T ,_ **X** ¯ _T_ ) _|_ **X** _T_ = **x** _T_ ] _≈_ E[ _f_ ( **x** _T ,_ **X** ¯ _T_ )] and use the approximation 



where **x**<sup>_k_</sup> _T_ ¯<sup>,</sup><sup>_k_= 1</sup><sup>_, . . . , K_are our samples from</sup><sup>**X**¯</sup> _T_<sup>.</sup> 

### **4.2 Experiments** 

To show in an experimental setup that the marginal expectation is a better choice, we consider functions _f_ for which we can calculate analytically the attribution of _xj_ . This is possible for linear functions 



since 



and hence, the attribution of _xj_ is _αj_ ( _xj −_ E[ _Xj_ ]). Our experiments are divided into the following setups: 

1. We assume that the feature vector **X** follows a multivariate Gaussian distribution. 

2. We use a kernel estimation to approximate the conditional expectation. 

For the experiments, we use the KernelExplainer class of the python SHAP package from Lundberg and Lee (2017) to calculate Shapley Values with respect to the marginal expectation and the R package SHAPR, in which the methodology of Aas et al. (2019) is implemented, to calculate Shapley Values with respect to the conditional distribution. 

Notice that calculating Shapley Values is also possible for non-linear functions. Further, approximating the marginal expectation is computationally inexpensive compared to the approximation of the conditional expectation with kernel estimation. 

7 

#### **4.2.1 Multivariate Gaussian distribution** 

If **X** _∼ N_ ( **_µ_** _,_ **Σ** ) with some mean vector **_µ_** and covariance matrix **Σ** , it holds that 







(see (Aas et al., 2019, Section 3.1)), where 



with 



Hence, we can approximate the conditional expectation by sampling _XT_ ¯ directly from its distribution. 

We simulate Gaussian data and run the experiment for different number of features. For every experiment with multivariate Gaussian distribution, we set the intercept to 0, i.e. _α_ 0 = 0. 

**Dimension n=3.** In the first 3-dimensional experiment, we let _α_ 1 = 0 and choose in every run _α_ 1 and _α_ 2 independently from the standard normal distribution. Further, we let **_µ_** = (0 _,_ 0 _,_ 0)<sup>_T_</sup> and **Σ** = _cc_<sup>_T_</sup> , where we choose the entries of _c_ in every run independently from the standard normal distribution and **x** also randomly in every run. The number of runs and the sample size of **X** is 1000. Figure 4 shows the errors _φj −_ contr _j_ ( **x** ) of the Shapley Values _φj_ with respect to the set function _g_ ( _T_ ) = E[ _f_ ( **x** _T ,_ **X** ¯ _T_ )] _−_ E _f_ ( **X** ) (blue) and the set function _g_ ( _T_ ) = E[ _f_ ( **x** _T ,_ **X** ¯ _T_ ) _|_ **X** _T_ = **x** _T_ ] _−_ E _f_ ( **X** ) (red). The very precise results for the marginal expectation are mainly from feature 1. 

**Dimension n=10.** In 10-dimensions, we take almost the same setting with the difference that we set the first 3 coefficients to zero, i.e. _α_ 1 = _α_ 2 = _α_ 3 = 0. Again, the very precise results for the marginal expectation are from the features whose coefficient we set to 0. 

#### **4.2.2 Approximation via kernel estimation** 

If we have no information about the underlying distribution, it is hard to approximate the conditional distribution sufficiently. However, in low dimensions kernel estimates 

Figure 4: Histogram showing the error of the Shapley Values for multivariate Gaussian distribution in the 3- dimensional (left) and 10-dimensional (right) setting with _α_ 1 = 0. Blue: error using marginal expectation, Red: error using conditional expectation. 

can provide a good approximation. We take the kernel estimation method from Aas et al. (2019) to show how strongly the Shapley Values w.r.t. conditional expectation deviate from _αj_ ( _xj −_ E[ _Xj_ ]). Their approximation is as follows: 

1. Let Σ _T_ be the covariance matrix of our sample from **X** _T_ . To each point **x**<sup>_i_</sup> of the sample, calculate the Mahalanobis distance (see Mahalanobis (1936)) 



where ( **x** _T −_ **x**<sup>_i_</sup> _T_<sup>)</sup><sup>_′_denotesthetransposeof(</sup><sup>**x**</sup><sup>_T−_</sup> **x**<sup>_i_</sup> _T_<sup>).</sup> 

2. Calculate the _Kernel weights_ 



Hereby, _σ_<sup>2</sup> _>_ 0 is a bandwidth which has to be specified. 

3. Sort the weights _wT_ ( **x** _,_ **x**<sup>_i_</sup> ) in increasing order and let **x** ˜<sup>_i_</sup> be the corresponding ordered sampling instances. Then, approximate _g_ ( _T_ ) by 



For the experiment, we use the real data set _Human Activity Recognition Using Smartphones Data Set_ (see Anguita et al. (2013)) from the UCI repository. The data set 

8 

consists of 561 features with a training sample size of 7352 and test sample size of 2948. In this experiment, we merge these two samples together and therefore our sample size is 10299. We take randomly 4 features and train a linear model with 3 of these features as inputs and with the 4-th feature as target. We don’t consider the label (which is a daily activity performed by the human) of the data set, but the different features have the true label as a common cause. Notice that we are not interested in the quality of the model, but rather in a model for which the ground truth of the attribution is known (because we can certainly look at the linear model obtained). 

Afterwards, we calculate the Shapley Values with SHAP and SHAPR (with _σ_<sup>2</sup> set to 0.1 in SHAPR which is the default value) using the first 1000 samples and approximate the expected value E _Xj_ using the whole data set. The observation **x** is also randomly picked from the data and we run this experiment 1000 times. Figure 5 shows the histogram of the error _φj −_ contr _j_ ( **x** ) for the marginal expectation (blue) and conditional expectation (red). 

though the corresponding theory part of the paper suffers from this issue) since they ‘approximates’ the observational expectations by an expression that would have been the right one in the first place. We think that this clarification is important since other authors tried to ‘improve’ the SHAP package in a way that we consider conceptually flawed. Moreover, we revisited some properties that were stated as desirable in the context of attribution analysis. If stated in a too vague manner, there is some room for interpretation. We argued, for instance, why we think that our attribution method satisfies a reasonable symmetry property, since attribution via interventional probabilities has been criticised for violating alleged desirable symmetry properties. 

**Acknowledgements:** The authors would like to thank Scott Lundberg and Anders Løland for their valuable feedback and Atalanti Mastakouri for remarks on the presentation. 

## **References** 



Figure 5: Histogram showing the error of the Shapley Values for the data set _Human Activity Recognition Using Smartphones Data Set_ . Blue: error using marginal expectation, Red: error using conditional expectation. 

## **5 Conclusion** 

In this work we considered the problem of attributing the output from one particular multivariate input to individual features. We argued that there is a misconception also in recent proposals for feature attribution because they use observational conditional distributions rather than interventional distributions. Our arguments are phrased in terms of the causal language introduced by Pearl (2000). We argue that parts of the package SHAP from Lundberg and Lee (2017) are unaffected by this misconception (al- 

- K. Aas, M. Jullum, and A. Løland. Explaining individual predictions when features are dependent: More accurate approximations to Shapley values. ArXiv: 1903.10464, 2019. 

- D. Anguita, A. Ghio, L. Oneto, X. Parra, and J. L. ReyesOrtiz. A Public Domain Dataset for Human Activity Recognition Using Smartphones. In _21th European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning_ , pages 24– 26, April 2013. 

- S. Barocas, M. Hardt, and A. Narayanan. _Fairness and Machine Learning_ . fairmlbook.org, 2018. http:// www.fairmlbook.org. 

- A. Binder, G. Montavon, S. Lapuschkin, K. R. Mller, and W. Samek. Layer-Wise Relevance Propagation for Neural Networks with Local Renormalization Layers. In _Artificial Neural Networks and Machine Learning ICANN_ , volume 9887, 2016. 

- T. B. Brown, D. Man, A. Roy, M. Abadi, and J. Gilmer. Adversarial Patch. _arXiv:1712.09665_ , 2018. 

9 

- A. Charnes, B. Golany, M. Keane, and J. Rousseau. Extremal Principle Solutions of Games in Characteristic Function Form: Core, Chebychev and Shapley Value Generalizations. _Econometrics of Planning and Efficiency_ , 11:123–133, 1988. 

- A. Chattopadhyay, P. Manupriya, A. Sarkar, and V. Balasubramanian. Neural network attributions: A causal perspective. In K. Chaudhuri and R. Salakhutdinov, editors, _Proceedings of the 36th International Conference on Machine Learning_ , volume 97 of _Proceedings of Machine Learning Research_ , pages 981–990, Long Beach, California, USA, 09–15 Jun 2019. PMLR. 

- A. Datta, S. Sen, and Y. Zick. Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems. In _2016 IEEE Symposium on Security and Privacy (SP)_ , pages 598–617, 2016. 

- C. Dwork, M. Hardt, T. Pitassi, O. Reingold, and R. Zemel. Fairness through awareness. In _Proceedings of the 3rd Innovations in Theoretical Computer Science Conference_ , ITCS ’12, pages 214–226, New York, NY, USA, 2012. ACM. ISBN 978-1-4503-11151. doi: 10.1145/2090236.2090255. URL http:// doi.acm.org/10.1145/2090236.2090255. 

- K. Eykholt, I. Evtimov, E. Fernandes, B. Li, A. Rahmati, C. Xiao, A. Prakash, T. Kohno, and D. Song. Robust Physical-World Attacks on Deep Learning Visual Classification. In _The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 1625– 1634, 2018. 

- E. J. Friedman. Paths and consistency in additive cost sharing. _International Journal of Game Theory_ , 32(4): 501–518, 2004. 

- J. H. Friedman. Greedy function approximation: A gradient boosting machine. _Annals of statistics_ , pages 1189– 1232, 2001. 

- I. J. Goodfellow, J. Shlens, and C. Szegedy. Explaining and harnessing adversarial examples. In _3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings_ , 2015. URL http://arxiv. org/abs/1412.6572. 

- N. Kilbertus, M. Rojas-Carulla, G. Parascandolo, M. Hardt, D. Janzing, and B. Sch¨olkopf. Avoiding discrimination through causal reasoning. In _Proceedings from the conference ”Neural Information Processing Systems 2017_ , pages 656–666. Curran Associates, Inc., December 2017. 

- A. Kurakin, I. J. Goodfellow, and Samy Bengio. Adversarial examples in the physical world. In _Artificial Intelligence Safety and Security_ , pages 99–112. Chapman and Hall/CRC, 2018. 

- S. Lundberg and S. Lee. A unified approach to interpreting model predictions. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems 30_ , pages 4765–4774. Curran Associates, Inc., 2017. 

- S. Lundberg, G. Erion, and S. Lee. Consistent individualized feature attribution for tree ensembles. arXiv:1802.03888, 2018. 

- P. C. Mahalanobis. On the generalised distance in statistics. In _Proceedings of the National Institute of Sciences of India_ , April 1936. 

- C. Molnar. _Interpretable Machine Learning_ . Molnar, C., 2019. URL https://christophm.github. io/interpretable-ml-book/. 

- J. Pearl. _Causality_ . Cambridge University Press, 2000. 

- M. Ribeiro and C. Singh, S.and Guestrin. ”why should i trust you?”: Explaining the predictions of any classifier. In _Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’16, pages 1135–1144, New York, NY, USA, 2016. 

- L. Shapley. A value for n-person games. _Contributions to the Theory of Games (AM-28)_ , 2, 1953. 

- M. Sharif, S. Bhagavatula, L. Bauer, and M. K. Reiter. Accessorize to a Crime: Real and Stealthy Attacks on State-of-the-Art Face Recognition. In _Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security_ , pages 1528–1540, 2016. 

10 

- A. Shrikumar, P. Greenside, and A. Kundaje. Not Just A Black Box: Learning Important Features Through Propagating Activation Differences. _In ICML (arXiv:1605.01713)_ , 2016. 

- M. Sundararajan and A. Najmi. The many Shapley values for model explanation. _arXiv:1908.08474_ , 2019. 

- M. Sundararajan, A. Taly, and Q. Yan. Axiomatic Attribution for Deep Networks. In _Proceedings of the 34th International Conference on Machine Learning_ , volume 70, pages 3319–3328, August 2017. 

- Q. Zhao and T. Hastie. Causal interpretations of blackbox models. _Journal of Business & Economic Statistics_ , 2019. 

11 

