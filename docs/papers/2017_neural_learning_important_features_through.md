---
title: "Learning Important Features Through Propagating Activation Differences"
authors: "neural"
year: 2017
arxiv_id: "1704.02685"
original_file: "1704.02685.pdf"
pdf_path: "docs/papers\2017_neural_learning_important_features_through.pdf"
---

# Learning Important Features Through Propagating Activation Differences

**Authors:** Neural et al.  
**Year:** 2017 | **arXiv:** [`1704.02685`](https://arxiv.org/abs/1704.02685)  
**Local PDF:** [`2017_neural_learning_important_features_through.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2017_neural_learning_important_features_through.pdf)

---

**Learning Important Features Through Propagating Activation Differences** 

**Avanti Shrikumar**<sup>1</sup> **Peyton Greenside**<sup>1</sup> **Anshul Kundaje**<sup>1</sup> 

# **Abstract** 

The purported “black box” nature of neural networks is a barrier to adoption in applications where interpretability is essential. Here we present DeepLIFT (Deep Learning Important FeaTures), a method for decomposing the output prediction of a neural network on a specific input by backpropagating the contributions of all neurons in the network to every feature of the input. DeepLIFT compares the activation of each neuron to its ‘reference activation’ and assigns contribution scores according to the difference. By optionally giving separate consideration to positive and negative contributions, DeepLIFT can also reveal dependencies which are missed by other approaches. Scores can be computed efficiently in a single backward pass. We apply DeepLIFT to models trained on MNIST and simulated genomic data, and show significant advantages over gradient-based methods. Video tutorial: http://goo.gl/qKb7pL, ICML slides: bit.ly/deeplifticmlslides, ICML talk: https://vimeo.com/238275076, code: http://goo.gl/RM8jvH. 

# **1. Introduction** 

As neural networks become increasingly popular, their black box reputation is a barrier to adoption when interpretability is paramount. Here, we present DeepLIFT (Deep Learning Important FeaTures), a novel algorithm to assign importance score to the inputs for a given output. Our approach is unique in two regards. First, it frames the question of importance in terms of differences from a ‘reference’ state, where the ‘reference’ is chosen according to the problem at hand. In contrast to most gradient-based methods, using a difference-from-reference allows DeepLIFT to propagate an importance signal even in situations where the gradient is zero and avoids artifacts caused by discontinuities in the gradient. Second, by optionally giving separate consideration to the effects of posi- 

> 1Stanford University, Stanford, California, USA. Correspondence: A Kundaje _<_ akundaje@stanford.edu _>_ . 

tive and negative contributions at nonlinearities, DeepLIFT can reveal dependencies missed by other approaches. As DeepLIFT scores are computed using a backpropagationlike algorithm, they can be obtained efficiently in a single backward pass after a prediction has been made. 

# **2. Previous Work** 

This section provides a review of existing approaches to assign importance scores for a given task and input example. 

## **2.1. Perturbation-Based Forward Propagation Approaches** 

These approaches make perturbations to individual inputs or neurons and observe the impact on later neurons in the network. Zeiler & Fergus (Zeiler & Fergus, 2013) occluded different segments of an input image and visualized the change in the activations of later layers. “In-silico mutagenesis” (Zhou & Troyanskaya, 2015) introduced virtual mutations at individual positions in a genomic sequence and quantified the their impact on the output. Zintgraf et al. (Zintgraf et al., 2017) proposed a clever strategy for analyzing the difference in a prediction after marginalizing over each input patch. However, such methods can be computationally inefficient as each perturbation requires a separate forward propagation through the network. They may also underestimate the importance of features that have saturated their contribution to the output ( **Fig. 1** ). 



_Figure 1._ **Perturbation-based approaches and gradient-based approaches fail to model saturation** . Illustrated is a simple network exhibiting saturation in the signal from its inputs. At the point where _i_ 1 = 1 and _i_ 2 = 1, perturbing either _i_ 1 or _i_ 2 to 0 will not produce a change in the output. Note that the gradient of the output w.r.t the inputs is also zero when _i_ 1 + _i_ 2 _>_ 1. 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

## **2.2. Backpropagation-Based Approaches** 

Unlike perturbation methods, backpropagation approaches propagate an importance signal from an output neuron backwards through the layers to the input in one pass, making them efficient. DeepLIFT is one such approach. 

## 2.2.1. GRADIENTS, DECONVOLUTIONAL NETWORKS AND GUIDED BACKPROPAGATION 

Simonyan et al. (Simonyan et al., 2013) proposed using the gradient of the output w.r.t. pixels of an input image to compute a “saliency map” of the image in the context of image classification tasks. The authors showed that this was similar to deconvolutional networks (Zeiler & Fergus, 2013) except for the handling of the nonlinearity at rectified linear units (ReLUs). When backpropagating importance using gradients, the gradient coming into a ReLU during the backward pass is zero’d out if the input to the ReLU during the forward pass is negative. By contrast, when backpropagating an importance signal in deconvolutional networks, the importance signal coming into a ReLU during the backward pass is zero’d out if and only if it is negative, with no regard to sign of the input to the ReLU during the forward pass. Springenberg et al., (Springenberg et al., 2014) combined these two approaches into Guided Backpropagation, which zero’s out the importance signal at a ReLU if either the input to the ReLU during the forward pass is negative or the importance signal during the backward pass is negative. Guided Backpropagation can be thought of as equivalent to computing gradients, with the caveat that any gradients that become negative during the backward pass are discarded at ReLUs. Due to the zero-ing out of negative gradients, both guided backpropagation and deconvolutional networks can fail to highlight inputs that contribute negatively to the output. Additionally, none of the three approaches would address the saturation problem illustrated in **Fig. 1** , as the gradient of _y_ w.r.t. _h_ is negative (causing Guided Backprop and deconvolutional networks to assign zero importance), and the gradient of _h_ w.r.t both _i_ 1 and _i_ 2 is zero when _i_ 1 + _i_ 2 _>_ 1 (causing both gradients and Guided Backprop to be zero). Discontinuities in the gradients can also cause undesirable artifacts ( **Fig. 2** ). 

## 2.2.2. LAYERWISE RELEVANCE PROPAGATION AND GRADIENT _×_ INPUT 

Bach et al. (Bach et al., 2015) proposed an approach for propagating importance scores called Layerwise Relevance Propagation (LRP). Shrikumar et al. and Kindermans et al. (Shrikumar et al., 2016; Kindermans et al., 2016) showed that absent modifications to deal with numerical stability, the LRP rules for ReLU networks were equivalent within a scaling factor to an elementwise product between the saliency maps of Simonyan et al. and the input (in other 

words, gradient _×_ input). In our experiments, we compare DeepLIFT to gradient _×_ input as the latter is easily implemented on a GPU, whereas (at the time of writing) LRP did not have a GPU implementation available to our knowledge. 

While gradient _×_ input is often preferable to gradients alone as it leverages the sign and strength of the input, it still does not address the saturation problem in **Fig. 1** or the thresholding artifact in **Fig. 2** . 

## 2.2.3. INTEGRATED GRADIENTS 

Instead of computing the gradients at only the current value of the input, one can integrate the gradients as the inputs are scaled up from some starting value (eg: all zeros) to their current value (Sundararajan et al., 2016). This addressess the saturation and thresholding problems of **Fig. 1** and **Fig. 2** , but numerically obtaining high-quality integrals adds computational overhead. Further, this approach can still give misleading results (see **Section 3.4.3** ). 

## **2.3. Grad-CAM and Guided CAM** 

Grad-CAM (Selvaraju et al., 2016) computes a coarsegrained feature-importance map by associating the feature maps in the final convolutional layer with particular classes based on the gradients of each class w.r.t. each feature map, and then using the weighted activations of the feature maps as an indication of which inputs are most important. To obtain more fine-grained feature importance, the authors proposed performing an elementwise product between the scores obtained from Grad-CAM and the scores obtained from Guided Backpropagation, termed Guided Grad-CAM. However, this strategy inherits the limitations of Guided Backpropagation caused by zero-ing out negative gradients during backpropagation. It is also specific to convolutional neural networks. 

# **3. The DeepLIFT Method** 

## **3.1. The DeepLIFT Philosophy** 

DeepLIFT explains the difference in output from some ‘reference’ output in terms of the difference of the input from some ‘reference’ input. The ‘reference’ input represents some default or ‘neutral’ input that is chosen according to what is appropriate for the problem at hand (see **Section 3.3** for more details). Formally, let _t_ represent some target output neuron of interest and let _x_ 1 _, x_ 2 _, ..., xn_ represent some neurons in some intermediate layer or set of layers that are necessary and sufficient to compute _t_ . Let _t_<sup>0</sup> represent the reference activation of _t_ . We define the quantity ∆ _t_ to be the difference-from-reference, that is ∆ _t_ = _t − t_<sup>0</sup> . DeepLIFT assigns contribution scores _C_ ∆ _xi_ ∆ _t_ to ∆ _xi_ s.t.: 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 



We call **Eq. 1** the **summation-to-delta** property. _C_ ∆ _xi_ ∆ _t_ can be thought of as the amount of difference-fromreference in _t_ that is attributed to or ‘blamed’ on the difference-from-reference of _xi_ . Note that when a neuron’s transfer function is well-behaved, the output is locally linear in its inputs, providing additional motivation for **Eq. 1** . 

_C_ ∆ _xi_ ∆ _t_ can be non-zero even when _∂x∂ti_<sup>iszero.Thisal-</sup> lows DeepLIFT to address a fundamental limitation of gradients because, as illustrated in **Fig. 1** , a neuron can be signaling meaningful information even in the regime where its gradient is zero. Another drawback of gradients addressed by DeepLIFT is illustrated in **Fig. 2** , where the discontinuous nature of gradients causes sudden jumps in the importance score over infinitesimal changes in the input. By contrast, the difference-from-reference is continuous, allowing DeepLIFT to avoid discontinuities caused by bias terms. 



_Figure 2._ **Discontinuous gradients can produce misleading importance scores** . Response of a single rectified linear unit with a bias of _−_ 10. Both gradient and gradient _×_ input have a discontinuity at _x_ = 10; at _x_ = 10 + _ϵ_ , gradient _×_ input assigns a contribution of 10 + _ϵ_ to _x_ and _−_ 10 to the bias term ( _ϵ_ is a small positive number). When _x <_ 10, contributions on _x_ and the bias term are both 0. By contrast, the difference-from-reference (red arrow, top figure) gives a continuous increase in the contribution score. 

## **3.2. Multipliers and the Chain Rule** 

## 3.2.1. DEFINITION OF MULTIPLIERS 

For a given input neuron _x_ with difference-from-reference ∆ _x_ , and target neuron _t_ with difference-from-reference ∆ _t_ that we wish to compute the contribution to, we define the multiplier _m_ ∆ _x_ ∆ _t_ as: 



In other words, the multiplier _m_ ∆ _x_ ∆ _t_ is the contribution of ∆ _x_ to ∆ _t_ divided by ∆ _x_ . Note the close analogy to the 

idea of partial derivatives: the partial derivative _∂x_<sup>_<u>∂t</u>_isthe</sup> infinitesimal change in _t_ caused by an infinitesimal change in _x_ , divided by the infinitesimal change in _x_ . The multiplier is similar in spirit to a partial derivative, but over finite differences instead of infinitesimal ones. 

## 3.2.2. THE CHAIN RULE FOR MULTIPLIERS 

Assume we have an input layer with neurons _x_ 1 _, ..., xn_ , a hidden layer with neurons _y_ 1 _, ..., yn_ , and some target output neuron _t_ . Given values for _m_ ∆ _xi_ ∆ _yj_ and _m_ ∆ _yj_ ∆ _t_ , the following definition of _m_ ∆ _xi_ ∆ _t_ is consistent with the summation-to-delta property in **Eq. 1** (see **Appendix A** for the proof): 



We refer to **Eq. 3** as the **chain rule for multipliers** . Given the multipliers for each neuron to its immediate successors, we can compute the multipliers for any neuron to a given target neuron efficiently via backpropagation - analogous to how the chain rule for partial derivatives allows us to compute the gradient w.r.t. the output via backpropagation. 

## **3.3. Defining the Reference** 

When formulating the DeepLIFT rules described in **Section 3.5** , we assume that the reference of a neuron is its activation on the reference input. Formally, say we have a neuron _y_ with inputs _x_ 1 _, x_ 2 _, ..._ such that _y_ = _f_ ( _x_ 1 _, x_ 2 _, ..._ ). Given the reference activations _x_<sup>0</sup> 1<sup>_, x_0</sup> 2<sup>_, ..._of the inputs, we</sup> can calculate the reference activation _y_<sup>0</sup> of the output as: 



i.e. references for all neurons can be found by choosing a reference input and propagating activations through the net. 

The choice of a reference input is critical for obtaining insightful results from DeepLIFT. In practice, choosing a good reference would rely on domain-specific knowledge, and in some cases it may be best to compute DeepLIFT scores against multiple different references. As a guiding principle, we can ask ourselves “what am I interested in measuring differences against?”. For MNIST, we use a reference input of all-zeros as this is the background of the images. For the binary classification tasks on DNA sequence inputs (strings over the alphabet _{_ A,C,G,T _}_ ), we obtained sensible results using either a reference input containing the expected frequencies of ACGT in the background ( **Fig. 5** ), or by averaging the results over multiple reference inputs for each sequence that are generated by shuffling each original sequence ( **Appendix J** ). For CIFAR10 data, we found that using a blurred version of the original image as the 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

reference highlighted outlines of key objects, while an allzeros reference highlighted hard-to-interpret pixels in the background ( **Appendix L** ). 

It is important to note that gradient _×_ input implicitly uses a reference of all-zeros (it is equivalent to a first-order Taylor approximation of gradient _×_ ∆input where ∆ is measured w.r.t. an input of zeros). Similary, integrated gradients ( **Section 2.2.3** ) requires the user to specify a starting point for the integral, which is conceptually similar to specifying a reference for DeepLIFT. While Guided Backprop and pure gradients don’t use a reference, we argue that this is a limitation as these methods only describe the local behaviour of the output at the specific input value, without considering how the output behaves over a range of inputs. 

## **3.4. Separating Positive and Negative Contributions** 

We will see in **Section 3.5.3** that, in some situations, it is essential to treat positive and negative contributions differently. To do this, for every neuron _y_ , we will introduce ∆ _y_<sup>+</sup> and ∆ _y_<sup>_−_</sup> to represent the positive and negative components of ∆ _y_ , such that: 





Which leads to the following choice for the contributions: _C_ ∆ _x_ + _i_<sup>∆</sup><sup>_y_+= 1</sup><sup>_{wi_∆</sup><sup>_xi>_0</sup><sup>_}wi_∆</sup><sup>_x_</sup> _i_<sup>+</sup> _C_ ∆ _x−i_<sup>∆</sup><sup>_y_+= 1</sup><sup>_{wi_∆</sup><sup>_xi>_0</sup><sup>_}wi_∆</sup><sup>_x_</sup> _i_<sup>_−_</sup> _C_ ∆ _x_ + _i_<sup>∆</sup><sup>_y−_= 1</sup><sup>_{wi_∆</sup><sup>_xi<_0</sup><sup>_}wi_∆</sup><sup>_x_</sup> _i_<sup>+</sup> _C_ ∆ _x−i_<sup>∆</sup><sup>_y−_= 1</sup><sup>_{wi_∆</sup><sup>_xi<_0</sup><sup>_}wi_∆</sup><sup>_x_</sup> _i_<sup>_−_</sup> 

We can then find multipliers using the definition in **Section 3.2.1** , which gives _m_ ∆ _x_ + _i_<sup>∆</sup><sup>_y_+=</sup><sup>_m_∆</sup><sup>_x_</sup> _i_<sup>_−_∆</sup><sup>_y_+= 1</sup><sup>_{wi_∆</sup><sup>_xi>_</sup> 0 _}wi_ and _m_ ∆ _x_ + _i_<sup>∆</sup><sup>_y−_=</sup><sup>_m_∆</sup><sup>_x−_</sup> _i_<sup>∆</sup><sup>_y−_= 1</sup><sup>_{wi_∆</sup><sup>_xi<_0</sup><sup>_}wi_.</sup> 

What about when ∆ _xi_ = 0? While setting multipliers to 0 in this case would be consistent with summation-to-delta, it is possible that ∆ _x_<sup>+</sup> _i_<sup>and∆</sup><sup>_x−_</sup> _i_<sup>arenonzero(andcancel</sup> each other out), in which case setting the multiplier to 0 would fail to propagate importance to them. To avoid this, we set _m_ ∆ _x_ + _i_<sup>∆</sup><sup>_y_+=</sup><sup>_m_∆</sup><sup>_x_+</sup> _i_<sup>∆</sup><sup>_y−_=0</sup><sup>_._5</sup><sup>_wi_when∆</sup><sup>_xi_is0</sup> (similarly for ∆ _x_<sup>_−_</sup> ). See **Appendix B** for how to compute these multipliers using standard neural network ops. 

## 3.5.2. THE RESCALE RULE 

For linear neurons, ∆ _y_<sup>+</sup> and ∆ _y_<sup>_−_</sup> are found by writing ∆ _y_ as a sum of terms involving its inputs ∆ _xi_ and grouping positive and negative terms together. The importance of this will become apparent when applying the RevealCancel rule ( **Section 3.5.3** ), where for a given target neuron _t_ we may find that _m_ ∆ _y_ +∆ _t_ and _m_ ∆ _y−_ ∆ _t_ differ. However, when applying only the Linear or Rescale rules ( **Section 3.5.1** and **Section 3.5.2** ), _m_ ∆ _y_ ∆ _t_ = _m_ ∆ _y_ +∆ _t_ = _m_ ∆ _y−_ ∆ _t_ . 

## **3.5. Rules for Assigning Contribution Scores** 

We present the rules for assigning contribution scores for each neuron to its immediate inputs. In conjunction with the chain rule for multipliers ( **Section 3.2** ), these rules can be used to find the contributions of any input (not just the immediate inputs) to a target output via backpropagation. 

## 3.5.1. THE LINEAR RULE 

This applies to Dense and Convolutional layers (excluding nonlinearities). Let _y_ be a linear function of its inputs _xi_ such that _y_ = _b_ +<sup>�</sup> _i_<sup>_wixi_.Wehave∆</sup><sup>_y_=�</sup> _i_<sup>_wi_∆</sup><sup>_xi_.</sup> We define the positive and negative parts of ∆ _y_ as: 



This rule applies to nonlinear transformations that take a single input, such as the ReLU, tanh or sigmoid operations. Let neuron _y_ be a nonlinear transformation of its input _x_ such that _y_ = _f_ ( _x_ ). Because _y_ has only one input, we have by summation-to-delta that _C_ ∆ _x_ ∆ _y_ = ∆ _y_ , and consequently _m_ ∆ _x_ ∆ _y_ = ∆<sup>∆</sup> _x_<sup>_<u>y</u>_.For the Rescale rule, we set ∆</sup><sup>_y_+</sup> and ∆ _y_<sup>_−_</sup> proportional to ∆ _x_<sup>+</sup> and ∆ _x_<sup>_−_</sup> as follows: 



Based on this, we get: 



In the case where _x → x_<sup>0</sup> , we have ∆ _x →_ 0 and ∆ _y →_ 0. The definition of the multiplier approaches the derivative, i.e. _m_ ∆ _x_ ∆ _y → dx_<sup>_dy_,wherethe</sup> _dx_<sup>_dy_isevaluatedat</sup><sup>_x_=</sup><sup>_x_0.</sup> We can thus use the gradient instead of the multiplier when _x_ is close to its reference to avoid numerical instability issues caused by having a small denominator. 

Note that the Rescale rule addresses both the saturation and the thresholding problems illustrated in **Fig. 1** and **Fig. 2** . In the case of **Fig. 1** , if _i_<sup>0</sup> 1<sup>=</sup><sup>_i_0</sup> 2<sup>=0,then</sup> at _i_ 1 + _i_ 2 _>_ 1 we have ∆ _h_ = _−_ 1 and ∆ _y_ = 1, giving 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

_m_ ∆ _h_ ∆ _y_ = ∆<sup>∆</sup> _h_<sup>_<u>y</u>_=</sup><sup>_−_1 even though</sup> _dh_<sup>_dy_= 0 (in other words,</sup> using difference-from-reference allows information to flow even when the gradient is zero). In the case of **Fig. 2** , assuming _x_<sup>0</sup> = _y_<sup>0</sup> = 0, at _x_ = 10 + _ϵ_ we have ∆ _y_ = _ϵ_ , giving _m_ ∆ _x_ ∆ _y_ = 10+ _<u>ϵ</u> ϵ_<sup>and</sup><sup>_C_∆</sup><sup>_x_∆</sup><sup>_y_=∆</sup><sup>_x × m_∆</sup><sup>_x_∆</sup><sup>_y_=</sup><sup>_ϵ_.</sup> By contrast, gradient _×_ input assigns a contribution of 10+ _ϵ_ to _x_ and _−_ 10 to the bias term (DeepLIFT never assigns importance to bias terms). 

As revealed in previous work (Lundberg & Lee, 2016), there is a connection between DeepLIFT and Shapely values. Briefly, the Shapely values measure the average marginal effect of including an input over all possible orderings in which inputs can be included. If we define “including” an input as setting it to its actual value instead of its reference value, DeepLIFT can be thought of as a fast approximation of the Shapely values. At the time, Lundberg & Lee cited a preprint of DeepLIFT which described only the Linear and Rescale rules with no separate treatment of positive and negative contributions. 

## 3.5.3. AN IMPROVED APPROXIMATION OF THE SHAPELY VALUES: THE REVEALCANCEL RULE 

While the Rescale rule improves upon simply using gradients, there are still some situations where it can provide misleading results. Consider the min( _i_ 1 _, i_ 2) operation depicted in **Fig. 3** , with reference values of _i_ 1 = 0 and _i_ 2 = 0. Using the Rescale rule, all importance would be assigned either to _i_ 1 or to _i_ 2 (whichever is smaller). This can obscure the fact that both inputs are relevant for the min operation. 

To understand why this occurs, consider the case when _i_ 1 _> i_ 2. We have _h_ 1 = ( _i_ 1 _− i_ 2) _>_ 0 and _h_ 2 = max(0 _, h_ 1) = _h_ 1. By the Linear rule, we calculate that _C_ ∆ _i_ 1∆ _h_ 1 = _i_ 1 and _C_ ∆ _i_ 2∆ _h_ 1 = _−i_ 2. By the Rescale rule, the multiplier _m_ ∆ _h_ 1∆ _h_ 2 is <u>∆∆</u> _<u>hh</u>_ <u>21</u> = 1, and thus _C_ ∆ _i_ 1∆ _h_ 2 = _m_ ∆ _h_ 1∆ _h_ 2 _C_ ∆ _i_ 1∆ _h_ 1 = _i_ 1 and _C_ ∆ _i_ 2∆ _h_ 2 = _m_ ∆ _h_ 1∆ _h_ 2 _C_ ∆ _i_ 2∆ _h_ 1 = _−i_ 2. The total contribution of _i_ 1 to the output _o_ becomes ( _i_ 1 _− C_ ∆ _i_ 1∆ _h_ 2) = ( _i_ 1 _− i_ 1) = 0, and the total contribution of _i_ 2 to _o_ is _−C_ ∆ _i_ 2∆ _h_ 2 = _i_ 2. This calculation is misleading as it discounts the fact that _C_ ∆ _i_ 2∆ _h_ 2 would be 0 if _i_ 1 were 0 - in other words, it ignores a dependency induced between _i_ 1 and _i_ 2 that comes from _i_ 2 canceling out _i_ 1 in the nonlinear neuron _h_ 2. A similar failure occurs when _i_ 1 _< i_ 2; the Rescale rule results in _C_ ∆ _i_ 1∆ _o_ = _i_ 1 and _C_ ∆ _i_ 2∆ _o_ = 0. Note that gradients, gradient _×_ input, Guided Backpropagation and integrated gradients would also assign all importance to either _i_ 1 or _i_ 2, because for any given input the gradient is zero for one of _i_ 1 or _i_ 2 (see **Appendix C** for a detailed calculation). 

One way to address this is by treating the positive and negative contributions separately. We again consider the nonlinear neuron _y_ = _f_ ( _x_ ). Instead of assuming that ∆ _y_<sup>+</sup> and ∆ _y_<sup>_−_</sup> are proportional to ∆ _x_<sup>+</sup> and ∆ _x_<sup>_−_</sup> and that 

_m_ ∆ _x_ +∆ _y_ + = _m_ ∆ _x−_ ∆ _y−_ = _m_ ∆ _x_ ∆ _y_ (as is done for the Rescale rule), we define them as follows: 



In other words, we set ∆ _y_<sup>+</sup> to the average impact of ∆ _x_<sup>+</sup> after no terms have been added and after ∆ _x_<sup>_−_</sup> has been added, and we set ∆ _y_<sup>_−_</sup> to the average impact of ∆ _x_<sup>_−_</sup> after no terms have been added and after ∆ _x_<sup>+</sup> has been added. This can be thought of as the Shapely values of ∆ _x_<sup>+</sup> and ∆ _x_<sup>_−_</sup> contributing to _y_ . 

By considering the impact of the positive terms in the absence of negative terms, and the impact of negative terms in the absence of positive terms, we alleviate some of the issues that arise from positive and negative terms canceling each other out. In the case of **Fig. 3** , RevealCancel would assign a contribution of 0 _._ 5 min( _i_ 1 _, i_ 2) to both inputs (see **Appendix C** for a detailed calculation). 

While the RevealCancel rule also avoids the saturation and thresholding pitfalls illustrated in **Fig. 1** and **Fig. 2** , there are some circumstances where we might prefer to use the Rescale rule. Specifically, consider a thresholded ReLU where ∆ _y >_ 0 iff ∆ _x ≥ b_ . If ∆ _x < b_ merely indicates noise, we would want to assign contributions of 0 to both ∆ _x_<sup>+</sup> and ∆ _x_<sup>_−_</sup> (as done by the Rescale rule) to mitigate the noise. RevealCancel may assign nonzero contributions by considering ∆ _x_<sup>+</sup> in the absence of ∆ _x_<sup>_−_</sup> and vice versa. 



_Figure 3._ Network computing _o_ = min( _i_ 1 _, i_ 2). Assume _i_ 1<sup>0=</sup> _i_<sup>0</sup> 2<sup>=0.When</sup><sup>_i_</sup> 1<sup>_<i_</sup> 2<sup>then</sup> _didy_ 2<sup>=0,andwhen</sup><sup>_i_2</sup><sup>_<i_1then</sup> _dido_ 1<sup>= 0.Using any of the backpropagation approaches described</sup> in **Section 2.2** would result in importance assigned either exclusively to _i_ 1 or _i_ 2. With the RevealCancel rule, the net assigns 0 _._ 5 min( _i_ 1 _, i_ 2) importance to both inputs. 

## **3.6. Choice of Target Layer** 

In the case of softmax or sigmoid outputs, we may prefer to compute contributions to the linear layer preceding the final nonlinearity rather than the final nonlinearity itself. This would be to avoid an attentuation caused by the 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

summation-to-delta property described in **Section 3.1** . For example, consider a sigmoid output _o_ = _σ_ ( _y_ ), where _y_ is the logit of the sigmoid function. Assume _y_ = _x_ 1 + _x_ 2, where _x_<sup>0</sup> 1<sup>=</sup><sup>_x_0</sup> 2<sup>=0.When</sup><sup>_x_1=50and</sup><sup>_x_2=0,the</sup> output _o_ saturates at very close to 1 and the contributions of _x_ 1 and _x_ 2 are 0 _._ 5 and 0 respectively. However, when _x_ 1 = 100 and _x_ 2 = 100, the output _o_ is still very close to 1, but the contributions of _x_ 1 and _x_ 2 are now both 0 _._ 25. This can be misleading when comparing scores across different inputs because a stronger contribution to the logit would not always translate into a higher DeepLIFT score. To avoid this, we compute contributions to _y_ rather than _o_ . 

## **Adjustments for Softmax Layers** 

If we compute contributions to the linear layer preceding the softmax rather than the softmax output, an issue that could arise is that the final softmax output involves a normalization over all classes, but the linear layer before the softmax does not. To address this, we can normalize the contributions to the linear layer by subtracting the mean contribution to all classes. Formally, if _n_ is the number of classes, _C_ ∆ _x_ ∆ _ci_ represents the unnormalized contribution to class _ci_ in the linear layer and _C_ ∆<sup>_′_</sup> _x_ ∆ _ci_<sup>representsthe</sup> normalized contribution, we have: 



As a justification for this normalization, we note that subtracting a fixed value from all the inputs to the softmax leaves the output of the softmax unchanged. 

# **4. Results** 

## **4.1. Digit Classification (MNIST)** 

We train a convolutional neural network on MNIST (LeCun et al., 1999) using Keras (Chollet, 2015) to perform digit classification and obtain 99.2% test-set accuracy. The architecture consists of two convolutional layers, followed by a fully connected layer, followed by the softmax output layer (see **Appendix D** for full details on model architecture and training). We used convolutions with stride _>_ 1 instead of pooling layers, which did not result in a drop in performance as is consistent with previous work (Springenberg et al., 2014). For DeepLIFT and integrated gradients, we used a reference input of all zeros. 

To evaluate importance scores obtained by different methods, we design the following task: given an image that originally belongs to class _co_ , we identify which pixels to erase to convert the image to some target class _ct_ . We do this by finding _Sxi_ diff = _Sxico − Sxict_ (where _Sxic_ is the score for pixel _xi_ and class _c_ ) and erasing up to 157 pixels (20% of the image) ranked in descending order of _Sxi_ diff for which 

_Sxi_ diff _>_ 0. We then evaluate the change in the log-odds score between classes _co_ and _ct_ for the original image and the image with the pixels erased. 

As shown in **Fig. 4** , DeepLIFT with the RevealCancel rule outperformed the other backpropagation-based methods. Integrated gradients ( **Section 2.2.3** ) computed numerically over either 5 or 10 intervals produced results comparable to each other, suggesting that adding more intervals would not change the result. Integrated gradients also performed comparably to gradient*input, suggesting that saturation and thresholding failure modes are not common on MNIST data. Guided Backprop discards negative gradients during backpropagation, perhaps explaining its poor performance at discriminating between classes. We also explored using the Rescale rule instead of RevealCancel on various layers and found that it degraded performance ( **Appendix E** ). 



_Figure 4._ **DeepLIFT with the RevealCancel rule better identifies pixels to convert one digit to another.** Top: result of masking pixels ranked as most important for the original class (8) relative to the target class (3 or 6). Importance scores for class 8, 3 and 6 are also shown. The selected image had the highest change in log-odds scores for the 8 _→_ 6 conversion using gradient*input or integrated gradients to rank pixels. Bottom: boxplots of increase in log-odds scores of target vs. original class after the mask is applied, for 1K images belonging to the original class in the testing set. “Integrated gradients-n” refers to numerically integrating the gradients over _n_ evenly-spaced intervals using the midpoint rule. 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 



_Figure 5._ **DeepLIFT with RevealCancel gives qualitatively desirable behavior on TAL-GATA simulation** . (a) Scatter plots of importance score vs. strength of TAL1 motif match for different tasks and methods (see **Appendix G** for GATA1). For each region, top 5 motif matches are plotted. X-axes: log-odds of TAL1 motif match vs. background. Y-axes: total importance assigned to the match for specified task. Red dots are from regions where both TAL1 and GATA1 motifs were inserted during simulation; blue have GATA1 only, green have TAL1 only, black have no motifs inserted. “DeepLIFT-fc-RC-conv-RS” refers to using RevealCancel on the fully-connected layer and Rescale on the convolutional layers, which appears to reduce noise relative to using RevealCancel on all layers. (b) proportion of strong matches (log-odds _>_ 7) to TAL1 motif in regions containing both TAL1 and GATA1 that had total score _≤_ 0 for task 0; Guided Backprop _×_ inp and DeepLIFT with RevealCancel have no false negatives, but Guided Backprop has false positives for Task 1 (Panel (a)) 

## **4.2. Classifying Regulatory DNA (Genomics)** 

Next, we compared the importance scoring methods when applied to classification tasks on DNA sequence inputs (strings over the alphabet _{_ A,C,G,T _}_ ). The human genome has millions of DNA sequence elements ( 200-1000 in length) containing specific combinations of short functional words to which regulatory proteins (RPs) bind to regulate gene activity. Each RP (e.g. GATA1) has binding affinity to specific collections of short DNA words (motifs) (e.g. GATAA and GATTA). A key problem in computational genomics is the discovery of motifs in regulatory DNA elements that give rise to distinct molecular signatures (labels) which can be measured experimentally. Here, in order to benchmark DeepLIFT and competing methods to uncover predictive patterns in DNA sequences, we design a simple simulation that captures the essence of the motif discovery problem described above. 

Background DNA sequences of length 200 were generated by sampling the letters ACGT at each position with 

probabilities 0 _._ 3 _,_ 0 _._ 2 _,_ 0 _._ 2 and 0 _._ 3 respectively. Motif instances were randomly sampled from previously known probabilistic motif models (See **Appendix F** ) of two RPs named GATA1 and TAL1 ( **Fig. 6a** )(Kheradpour & Kellis, 2014), and 0-3 instances of a given motif were inserted at random non-overlapping positions in the DNA sequences. We trained a multi-task neural network with two convolutional layers, global average pooling and one fullyconnected layer on 3 binary classification tasks. Positive labeled sequences in task 1 represented “both GATA1 and TAL1 present”, task 2 represented “GATA1 present” and in task 3 represented “TAL1 present”.<sup><u>1</u></sup> 4<sup>of sequences had</sup> both GATA1 and TAL1 motifs (labeled 111),<sup><u>1</u></sup> 4<sup>hadonly</sup> GATA1 (labeled 010), 4<sup><u>1</u>had only TAL1 (labeled 001), and</sup> <u>14</u><sup>hadnomotifs(labeled000).Detailsofthesimulation,</sup> network architecture and predictive performance are given in **Appendix F** . For DeepLIFT and integrated gradients, we used a reference input that had the expected frequencies of ACGT at each position (i.e. we set the ACGT channel axis to 0 _._ 3 _,_ 0 _._ 2 _,_ 0 _._ 2 _,_ 0 _._ 3; see **Appendix J** for results using 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

shuffled sequences as a reference). For fair comparison, this reference was also used for gradient _×_ input and Guided Backprop _×_ input (“input” is more accurately called ∆input where ∆ measured w.r.t the reference). For DNA sequence inputs, we found Guided Backprop _×_ input performed better than vanilla Guided Backprop; thus, we used the former. 

Given a particular subsequence, it is possible to compute the log-odds score that the subsequence was sampled from a particular motif vs. originating from the background distribution of ACGT. To evaluate different importancescoring methods, we found the top 5 matches (as ranked by their log-odds score) to each motif for each sequence from the test set, as well as the total importance allocated to the match by different importance-scoring methods for each task. The results are shown in **Fig. 5** (for TAL1) and **Appendix E** (for GATA1). Ideally, we expect an importance scoring method to show the following properties: (1) high scores for TAL1 motifs on task 2 and (2) low scores for TAL1 on task 1, with (3) higher scores corresponding to stronger log-odds matches; analogous pattern for GATA1 motifs (high for task 1, low for task 2); (4) high scores for both TAL1 and GATA1 motifs for task 0, with (5) higher scores on sequences containing both kinds of motifs vs. sequences containing only one kind (revealing cooperativity; corresponds to red dots lying above green dots in **Fig. 5** ). 

We observe Guided Backprop _×_ input fails (2) by assigning positive importance to TAL1 on task 1 (see **Appendix H** for an example sequence). It fails property (4) by failing to identify cooperativity in task 0 (red dots overlay green dots). Both Guided Backprop _×_ input and gradient _×_ input show suboptimal behavior regarding property (3), in that there is a sudden increase in importance when the log-odds score is around 7, but little differentiation at higher logodds scores (by contrast, the other methods show a more gradual increase). As a result, Guided Backprop _×_ input and gradient _×_ input can assign unduly high importance to weak motif matches ( **Fig. 6** ). This is a practical consequence of the thresholding problem from **Fig. 2** . The large discontinuous jumps in gradient also result in inflated scores (note the scale on the y-axes) relative to other methods. 

We explored three versions of DeepLIFT: Rescale at all nonlinearities (DeepLIFT-Rescale), RevealCancel at all nonlinearities (DeepLIFT-RevealCancel), and Rescale at convolutional layers with RevealCancel at the fully connected layer (DeepLIFT-fc-RC-conv-RS). In contrast to the results on MNIST, we found that DeepLIFT-fc-RC-convRS reduced noise relative to pure RevealCancel. We think this is because of the noise-suppression property discussed in **Section 3.5.3** ; if the convolutional layers act like motif detectors, the input to convolutional neurons that do not fire may just represent noise and importance should not be propagated to them (see **Fig. 6** for an example sequence). 

Gradient _×_ inp, integrated gradients and DeepLIFT-Rescale occasionally miss relevance of TAL1 for Task 0 ( **Fig. 5b** ), which is corrected by using RevealCancel on the fully connected layer (see example sequence in **Fig. 6** ). Note that the RevealCancel scores seem to be tiered. As illustrated in **Appendix I** , this is related to having multiple instances of a given motif in a sequence (eg: when there are multiple TAL1 motifs, the importance assigned to the presence of TAL1 is distributed across all the motifs). 



_Figure 6._ **RevealCancel highlights both TAL1 and GATA1 motifs for Task 0** . (a) PWM representations of the GATA1 motif and TAL1 motif used in the simulation (b) Scores for example sequence containing both TAL1 and GATA1 motifs. Letter height reflects the score. Blue box is location of embedded GATA1 motif, green box is location of embedded TAL1 motif. Red underline is chance occurrence of weak match to TAL1 (CAGTTG instead of CAGATG). Both TAL1 and GATA1 motifs should be highlighted for Task 0. RevealCancel on only the fully-connected layer reduces noise compared to RevealCancel on all layers. 

# **5. Conclusion** 

We have presented DeepLIFT, a novel approach for computing importance scores based on explaining the difference of the output from some ‘reference’ output in terms of differences of the inputs from their ‘reference’ inputs. Using the difference-from-reference allows information to propagate even when the gradient is zero ( **Fig. 1** ), which could prove especially useful in Recurrent Neural Networks where saturating activations like sigmoid or tanh are popular. DeepLIFT avoids placing potentially misleading importance on bias terms (in contrast to gradient*input - see **Fig. 2** ). By allowing separate treatment of positive and negative contributions, the DeepLIFT-RevealCancel rule can identify dependencies missed by other methods ( **Fig. 3** ). Open questions include how to apply DeepLIFT to RNNs, how to compute a good reference empirically from the data, and how best to propagate importance through ‘max’ operations (as in Maxout or Maxpooling neurons) beyond simply using the gradients. 

**DeepLIFT: Learning Important Features Through Propagating Activation Differences** 

# **6. Appendix** 

The appendix can be downloaded at: http://proceedings.mlr.press/v70/ shrikumar17a/shrikumar17a-supp.pdf 

# **References** 

- Bach, Sebastian, Binder, Alexander, Montavon, Gr´egoire, Klauschen, Frederick, M¨uller, Klaus-Robert, and Samek, Wojciech. On Pixel-Wise explanations for Non-Linear classifier decisions by Layer-Wise relevance propagation. _PLoS One_ , 10(7):e0130140, 10 July 2015. 

- Chollet, Franois. keras. https://github.com/ fchollet/keras, 2015. 

- Kheradpour, Pouya and Kellis, Manolis. Systematic discovery and characterization of regulatory motifs in encode tf binding experiments. _Nucleic acids research_ , 42 (5):2976–2987, 2014. 

- Kindermans, Pieter-Jan, Schtt, Kristof, Mller, KlausRobert, and Dhne, Sven. Investigating the influence of noise and distractors on the interpretation of neural networks. _CoRR_ , abs/1611.07270, 2016. URL https: //arxiv.org/abs/1611.07270. 

- LeCun, Yann, Cortes, Corinna, and Burges, Christopher J.C. The mnist database of handwritten digits. http://yann.lecun.com/exdb/mnist/, 1999. 

- Lundberg, Scott and Lee, Su-In. An unexpected unity among methods for interpreting model predictions. _CoRR_ , abs/1611.07478, 2016. URL http://arxiv. org/abs/1611.07478. 

- Selvaraju, Ramprasaath R., Das, Abhishek, Vedantam, Ramakrishna, Cogswell, Michael, Parikh, Devi, and Batra, Dhruv. Grad-cam: Why did you say that? visual explanations from deep networks via gradient-based localization. _CoRR_ , abs/1610.02391, 2016. URL http: //arxiv.org/abs/1610.02391. 

- Shrikumar, Avanti, Greenside, Peyton, Shcherbina, Anna, and Kundaje, Anshul. Not just a black box: Learning important features through propagating activation differences. _arXiv preprint arXiv:1605.01713_ , 2016. 

2014. URL http://arxiv.org/abs/1412. 6806. 

- Sundararajan, Mukund, Taly, Ankur, and Yan, Qiqi. Gradients of counterfactuals. _CoRR_ , abs/1611.02639, 2016. URL http://arxiv.org/abs/1611.02639. 

- Zeiler, Matthew D. and Fergus, Rob. Visualizing and understanding convolutional networks. _CoRR_ , abs/1311.2901, 2013. URL http://arxiv.org/ abs/1311.2901. 

- Zhou, Jian and Troyanskaya, Olga G. Predicting effects of noncoding variants with deep learning-based sequence model. _Nat Methods_ , 12:931–4, 2015 Oct 2015. ISSN 1548-7105. doi: 10.1038/nmeth.3547. 

- Zintgraf, Luisa M, Cohen, Taco S, Adel, Tameem, and Welling, Max. Visualizing deep neural network decisions: Prediction difference analysis. _ICLR_ , 2017. URL https://openreview.net/pdf? id=BJ5UeU9xx. 

# **7. Acknowledgements** 

We thank Anna Shcherbina for early experiments applying DeepLIFT to image data and beta-testing. We thank Sinhan Kang of Korea University for identifying a typing error in Section 3.6. 

# **8. Funding** 

AS was supported by a Howard Hughes Medical Institute International Student Research Fellowship and a Bio-X Bowes Fellowship. PG was supported by a Bio-X Stanford Interdisciplinary Graduate Fellowship. AK was supported by NIH grants DP2-GM-123485 and 1R01ES025009-02. 

# **9. Author Contributions** 

AS & PG conceptualized DeepLIFT. AS implemented DeepLIFT. AS ran experiments on MNIST. AS & PG ran experiments on genomic data. AK provided guidance and feedback. AS, PG and AK wrote the manuscript. 

- Simonyan, Karen, Vedaldi, Andrea, and Zisserman, Andrew. Deep inside convolutional networks: Visualising image classification models and saliency maps. _arXiv preprint arXiv:1312.6034_ , 2013. 

- Springenberg, Jost Tobias, Dosovitskiy, Alexey, Brox, Thomas, and Riedmiller, Martin A. Striving for simplicity: The all convolutional net. _CoRR_ , abs/1412.6806, 

