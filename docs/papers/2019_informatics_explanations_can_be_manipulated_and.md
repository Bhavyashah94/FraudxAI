---
title: "Explanations can be manipulated and geometry is to blame"
authors: "informatics"
year: 2019
arxiv_id: "1906.07983"
original_file: "1906.07983.pdf"
pdf_path: "docs/papers\2019_informatics_explanations_can_be_manipulated_and.pdf"
---

# Explanations can be manipulated and geometry is to blame

**Authors:** Informatics et al.  
**Year:** 2019 | **arXiv:** [`1906.07983`](https://arxiv.org/abs/1906.07983)  
**Local PDF:** [`2019_informatics_explanations_can_be_manipulated_and.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_informatics_explanations_can_be_manipulated_and.pdf)

---

# **Explanations can be manipulated and geometry is to blame** 

**Ann-Kathrin Dombrowski**<sup>1</sup> **, Maximilian Alber**<sup>1</sup> **, Christopher J. Anders**<sup>1</sup> **, Marcel Ackermann**<sup>2</sup> **, Klaus-Robert Müller**<sup>1,3,4</sup> **, Pan Kessel**<sup>1</sup> 

   - 1Machine Learning Group, EE & Computer Science Faculty, TU-Berlin 

- 2Department of Video Coding & Analytics, Fraunhofer Heinrich-Hertz-Institute 

         - 3Max Planck Institute for Informatics 

   - 4Department of Brain and Cognitive Engineering, Korea University 

      - `{klaus-robert.mueller, pan.kessel}@tu-berlin.de` 

#### **Abstract** 

Explanation methods aim to make neural networks more trustworthy and interpretable. In this paper, we demonstrate a property of explanation methods which is disconcerting for both of these purposes. Namely, we show that explanations can be manipulated _arbitrarily_ by applying visually hardly perceptible perturbations to the input that keep the network’s output approximately constant. We establish theoretically that this phenomenon can be related to certain geometrical properties of neural networks. This allows us to derive an upper bound on the susceptibility of explanations to manipulations. Based on this result, we propose effective mechanisms to enhance the robustness of explanations. 



<!-- Start of picture text -->
Original Image Manipulated Image<br><!-- End of picture text -->

Figure 1: Original image with corresponding explanation map on the left. Manipulated image with its explanation on the right. The chosen target explanation was an image with a text stating "this explanation was manipulated". 

1 

## **1 Introduction** 

Explanation methods have attracted significant attention over the last years due to their promise to open the black box of deep neural networks. Interpretability is crucial for scientific understanding and safety critical applications. 

Explanations can be provided in terms of explanation maps [1–19] that visualize the relevance attributed to each input feature for the overall classification result. In this work, we establish that these explanation maps can be changed to an _arbitrary target map_ . This is done by applying a visually hardly perceptible perturbation to the input. We refer to Figure 1 for an example. This perturbation does not change the output of the neural network, i.e. in addition to the classification result also the vector of all class probabilities is (approximately) the same. 

This finding is clearly problematic if a user, say a medical doctor, is expecting a robustly interpretable explanation map to rely on in the clinical decision making process. 

Motivated by this unexpected observation, we provide a theoretical analysis that establishes a relation of this phenomenon to the geometry of the neural network’s output manifold. This novel understanding allows us to derive a bound on the degree of possible manipulation of the explanation map. This bound is proportional to two differential geometric quantities: the principle curvatures and the geodesic distance between the original input and its manipulated counterpart. Given this theoretical insight, we propose efficient ways to limit possible manipulations and thus enhance resilience of explanation methods. 

In summary, this work provides the following key contributions: 

- We propose an algorithm which allows to manipulate an image with a hardly perceptible perturbation such that the explanation matches an arbitrary target map. We demonstrate its effectiveness for six different explanation methods and on four network architectures as well as two datasets. 

- We provide a theoretical understanding of this phenomenon for gradient-based methods in terms of differential geometry. We derive a bound on the principle curvatures of the hypersurface of equal network output. This implies a constraint on the maximal change of the explanation map due to small perturbations. 

- Using these insights, we propose methods to undo the manipulations and increase the robustness of explanation maps by smoothing the explanation method. We demonstrate experimentally that smoothing leads to increased robustness not only for gradient but also for propagation-based methods. 

### **1.1 Related work** 

In [20], it was demonstrated that explanation maps can be sensitive to small perturbations in the image. Their results may be thought of as untargeted manipulations, i.e. perturbations to the image which lead to an unstructured change in the explanation map. Our work focuses on targeted manipulations instead, i.e. to reproduce a given target map. Another approach [21] adds a constant shift to the input image, which is then eliminated by changing the bias of the first layer. For some methods, this leads to a change in the explanation map. Contrary to our approach, this requires to change the network’s biases. In [22], explanation maps are changed by randomization of (some of) the network weights. This is different from our method as it does not aim to change the explanation in a targeted manner and modifies the weights of the network. 

## **2 Manipulating explanations** 

We consider a neural network _g_ : R<sup>_d_</sup> _→_ R<sup>_K_</sup> with relu non-linearities which classifies an image _x ∈_ R<sup>_d_</sup> in _K_ categories with the predicted class given by _k_ = arg max _i g_ ( _x_ ) _i_ . The 

2 

explanation map is denoted by _h_ : R<sup>_d_</sup> _→_ R<sup>_d_</sup> and associates an image with a vector of the same dimension whose components encode the relevance score of each pixel for the neural network’s prediction. For a given explanation method and specified target _h_<sup>_t_</sup> _∈_ R<sup>_d_</sup> , a manipulated image _xadv_ = _x_ + _δx_ has the following properties: 

1. The output of the network stays approximately constant, i.e. _g_ ( _xadv_ ) _≈ g_ ( _x_ ). 

2. The explanation is close to the target map, i.e. _h_ ( _xadv_ ) _≈ h_<sup>_t_</sup> . 

3. The norm of the perturbation _δx_ added to the input image is small, i.e. _∥δx∥_ = _∥xadv − x∥≪_ 1 and therefore not perceptible. 

Throughout this paper, we will use the following explanation methods: 

- **Gradient** : The map _h_ ( _x_ ) = _∂x_<sup>_∂g_(</sup><sup>_x_)isusedandquantifieshowinfinitesimalperturba-</sup> tions in each pixel change the prediction _g_ ( _x_ ) [1,2]. 

- **Gradient** _×_ **Input** : This method uses the map _h_ ( _x_ ) = _x ⊙ ∂x_<sup>_∂g_(</sup><sup>_x_)[14].Forlinear</sup> models, this measure gives the exact contribution of each pixel to the prediction. 

- _∂g_ <u>(</u> _x_ ¯+ _t_ <u>(</u> _x−x_ ¯)) 

- _•_ **Integrated Gradients** : This method defines _h_ ( _x_ ) = ( _x−x_ ¯) _⊙_ �01 _∂x_ d _t_ where _x_ ¯ is a suitable baseline. See the original reference [13] for more details. 

- **Guided Backpropagation (GBP)** : This method is a variation of the gradient explanation for which negative components of the gradient are set to zero while backpropagating through the non-linearities [4]. 

- **Layer-wise Relevance Propagation (LRP)** : This method [5, 16] propagates relevance backwards through the network. For the output layer, relevance is defined by<sup>1</sup> 



which is then propagated backwards through all layers but the first using the _z_<sup>+</sup> rule 



where ( _W_<sup>_l_</sup> )<sup>+</sup> denotes the positive weights of the _l_ -th layer and _x_<sup>_l_</sup> is the activation vector of the _l_ -th layer. For the first layer, we use the _z_<sup>_B_</sup> rule to account for the bounded input domain 



where _li_ and _hi_ are the lower and upper bounds of the input domain respectively. 

- **Pattern Attribution (PA)** : This method is equivalent to standard backpropagation upon element-wise multiplication of the weights _W_<sup>_l_</sup> with learned patterns _A_<sup>_l_</sup> . We refer to the original publication for more details [17]. 

These methods cover two classes of attribution methods, namely _gradient-based_ and _propagationbased_ explanations, and are frequently used in practice [23,24]. 



3 



<!-- Start of picture text -->
Original Map Target Map Manipulated Map Perturbed Image Perturbations<br>Gradient<br>Gradient Original Image<br>x<br>Input<br>Layerwise<br>Relevance<br>Propagation Image used to<br>produce Target<br>Integrated<br>Gradients<br>Guided<br>Backpropagation<br>Pattern<br>Attribution<br><!-- End of picture text -->

Figure 2: The explanation map of the cat is used as the target and the image of the dog is perturbed. The red box contains the manipulated images and the corresponding explanations. The first column corresponds to the original explanations of the unperturbed dog image. The target map, shown in the second column, is generated with the cat image. The last column visualizes the perturbations. 

### **2.1 Manipulation Method** 

Let _h_<sup>_t_</sup> _∈_ R<sup>_d_</sup> be a given target explanation map and _x ∈_ R<sup>_d_</sup> an input image. As explained previously, we want to construct a manipulated image _xadv_ = _x_ + _δx_ such that it has an explanation very similar to the target _h_<sup>_t_</sup> but the output of the network stays approximately constant, i.e. _g_ ( _xadv_ ) _≈ g_ ( _x_ ). We obtain such manipulations by optimizing the loss function 



with respect to _xadv_ using gradient descent. We clamp _xadv_ after each iteration so that it is a valid image. The first term in the loss function (4) ensures that the manipulated explanation map is close to the target while the second term encourages the network to have the same output. The relative weighting of these two summands is controlled by the hyperparameter _γ ∈_ R+. 

The gradient with respect to the input _∇h_ ( _x_ ) of the explanation often depends on the vanishing second derivative of the relu non-linearities. This causes problems during optimization of the loss (4). As an example, the gradient method leads to 



4 



<!-- Start of picture text -->
× 10 − 9 Similarities Explanations × 10 − 3 Similarities Images<br>0 . 75 0 . 75<br>0 . 50 0 . 50<br>0 . 25 0 . 25<br>0 . 00 0 . 00<br>0 . 9<br>0 . 95<br>0 . 8<br>0 . 7 0 . 90<br>0 . 6<br>1 . 000<br>0 . 9<br>0 . 995<br>0 . 8<br>0 . 7<br>0 . 990<br>Gradient Gradient Integrated LRP GBP PA Gradient Gradient Integrated LRP GBP PA<br>xInput Gradients xInput Gradients<br>MSE MSE<br>SSIM SSIM<br>PCC PCC<br><!-- End of picture text -->

Figure 3: Left: Similarity measures between target _h_<sup>_t_</sup> and manipulated explanation map _h_ ( _xadv_ ). Right: Similarity measures between original _x_ and perturbed image _xadv_ . For SSIM and PCC large values indicate high similarity while for MSE small values correspond to similar images. 

We therefore replace the relu by softplus non-linearities 



For large _β_ values, the softplus approximates the relu closely but has a well-defined second derivative. After optimization is complete, we test the manipulated image with the original relu network. 

**Similarity metrics:** In our analysis, we assess the similarity between both images and explanation maps. To this end, we use three metrics following [22]: the structural similarity index (SSIM), the Pearson correlation coefficient (PCC) and the mean squared error (MSE). SSIM and PCC are relative similarity measures with values in [0 _,_ 1], where larger values indicate high similarity. The MSE is an absolute error measure for which values close to zero indicate high similarity. We normalize the sum of the explanation maps to be one and the images to have values between 0 and 1. 

### **2.2 Experiments** 

To evaluate our approach, we apply our algorithm to 100 randomly selected images for each explanation method. We use a pre-trained VGG-16 network [25] and the ImageNet dataset [26]. For each run, we randomly select two images from the test set. One of the two images is used to generate a target explanation map _h_<sup>_t_</sup> . The other image is perturbed by our algorithm with the goal of replicating the target _h_<sup>_t_</sup> using a few thousand iterations of gradient descent. We sum over the absolute values of the channels of the explanation map to get the relevance per pixel. Further details about the experiments are summarized in Supplement A. 

**Qualitative analysis:** Our method is illustrated in Figure 2 in which a dog image is manipulated in order to have an explanation of a cat. For all explanation methods, the target is closely emulated and the perturbation of the dog image is small. More examples can be found in the supplement. 

5 

**Quantitative analysis:** Figure 3 shows similarity measures between the target _h_<sup>_t_</sup> and the manipulated explanation map _h_ ( _xadv_ ) as well as between the original image _x_ and perturbed image _xadv_ .<sup>2</sup> All considered metrics show that the perturbed images have an explanation closely resembling the targets. At the same time, the perturbed images are very similar to the corresponding original images. We also verified by visual inspection that the results look very similar. We have uploaded the results of all runs so that interested readers can assess their similarity themselves<sup>3</sup> and will provide code to reproduce them. In addition, the output of the neural network is approximately unchanged by the perturbations, i.e. the classification of all examples is unchanged and the median of _∥g_ ( _xadv_ ) _− g_ ( _x_ ) _∥_ is of the order of magnitude 10<sup>_−_3</sup> for all methods. See Supplement B for further details. 

**Other architectures and datasets:** We checked that comparable results are obtained for ResNet-18 [27], AlexNet [28] and Densenet-121 [29]. Moreover, we also successfully tested our algorithm on the CIFAR-10 dataset [30]. We refer to the Supplement C for further details. 

## **3 Theoretical considerations** 

In this section, we analyze the vulnerability of explanations theoretically. We argue that this phenomenon can be related to the large curvature of the output manifold of the neural network. We focus on the gradient method starting with an intuitive discussion before developing mathematically precise statements. 

We have demonstrated that one can drastically change the explanation map while keeping the output of the neural network constant 



using only a small perturbation in the input _δx_ . The perturbed image _xadv_ = _x_ + _δx_ therefore lies on the hypersurface of constant network output _S_ = _{p ∈_ R<sup>_d_</sup> _|g_ ( _p_ ) = _c}_ .<sup>4</sup> We can exclusively consider the winning class output, i.e. _g_ ( _x_ ) := _g_ ( _x_ ) _k_ with _k_ = arg max _i g_ ( _x_ ) _i_ because the gradient method only depends on this component of the output. Therefore, the hyperplane _S_ is of co-dimension one. The gradient _∇g_ for every _p ∈ S_ is normal to this hypersurface. The fact that the normal vector _∇g_ can be drastically changed by slightly perturbing the input along the hypersurface _S_ suggests that the curvature of _S_ is large. 

While the latter statement may seem intuitive, it requires non-trivial concepts of differential geometry to make it precise, in particular the notion of the second fundamental form. We will briefly summarize these concepts in the following (see e.g. [31] for a standard textbook). To this end, it is advantageous to consider a normalized version of the gradient method 



This normalization is merely conventional as it does not change the relative importance of any pixel with respect to the others. For any point _p ∈ S_ , we define the tangent space _TpS_ as the vector space spanned by the tangent vectors _γ_ ˙ (0) = _dt_<sup>_<u>d</u>γ_(</sup><sup>_t_)</sup><sup>_|t_=0ofallpossiblecurves</sup> _γ_ : R _→ S_ with _γ_ (0) = _p_ . For _u, v ∈ TpS_ , we denote their inner product by _⟨u, v⟩_ . For any _u ∈ TpS_ , the _directional derivative_ is uniquely defined for any choice of _γ_ by 



> 2Throughout this paper, boxes denote 25th and 75th percentiles, whiskers denote 10th and 90th percentiles, solid lines show the medians and outliers are depicted by circles. 

> 3 `https://drive.google.com/drive/folders/1TZeWngoevHRuIw6gb5CZDIRrc7EWf5yb?usp=sharing` 

> 4It is sufficient to consider the hypersurface _S_ in a neighbourhood of the unperturbed input _x_ . 

6 

We then define the _Weingarten map_ as<sup>5</sup> 



where the unit normal _n_ ( _p_ ) can be written as (7). This map quantifies how much the unit normal changes as we infinitesimally move away from _p_ in the direction _u_ . The _second fundamental form_ is then given by 



It can be shown that the second fundamental form is bilinear and symmetric _L_ ( _u, v_ ) = _L_ ( _v, u_ ). It is therefore diagonalizable with real eigenvalues _λ_ 1 _, . . . λd−_ 1 which are called _principle curvatures_ . 

We have therefore established the remarkable fact that the sensitivity of the gradient map (7) is described by the principle curvatures, a key concept of differential geometry. 

In particular, this allows us to derive an upper bound on the maximal change of the gradient map _h_ ( _x_ ) = _n_ ( _x_ ) as we move slightly on _S_ . To this end, we define the _geodesic distance dg_ ( _p, q_ ) of two points _p, q ∈ S_ as the length of the shortest curve on _S_ connecting _p_ and _q_ . In the supplement, we show that: 

**Theorem 1** _Let g_ : R<sup>_d_</sup> _→_ R _be a network with softplusβ non-linearities and Uϵ_ ( _p_ ) = _{x ∈_ R<sup>_d_</sup> ; _∥x − p∥ < ϵ} an environment of a point p ∈ S such that Uϵ_ ( _p_ ) _∩ S is fully connected. Let g have bounded derivatives ∥∇g_ ( _x_ ) _∥≥ c for all x ∈Uϵ_ ( _p_ ) _∩ S. It then follows for all p_ 0 _∈Uϵ_ ( _p_ ) _∩ S that_ 



_where λmax is the principle curvature with the largest absolute value for any point in Uϵ_ ( _p_ ) _∩ S and the constant C >_ 0 _depends on the weights of the neural network._ 

This theorem can intuitively be motivated as follows: for relu non-linearities, the lines of equal network output are piece-wise linear and therefore have kinks, i.e. points of divergent curvature. These relu non-linearities are well approximated by softplus non-linearities (5) with large _β_ . Reducing _β_ smoothes out the kinks and therefore leads to reduced maximal curvature, i.e. _|λmax| ≤ β C_ . For each point on the geodesic curve connecting _p_ and _p_ 0, the normal can at worst be affected by the maximal curvature, i.e. the change in explanation is bounded by _|λmax| dg_ ( _p, p_ 0). 

There are two important lessons to be learned from this theorem: the geodesic distance can be substantially greater than the Euclidean distance for curved manifolds. In this case, inputs which are very similar to each other, i.e. the Euclidean distance is small, can have explanations that are drastically different. Secondly, the upper bound is proportional to the _β_ parameter of the softplus non-linearity. Therefore, smaller values of _β_ provably result in increased robustness with respect to manipulations. 

## **4 Robust explanations** 

Using the fact that the upper bound of the last section is proportional to the _β_ parameter of the softplus non-linearities, we propose _β-smoothing_ of explanations. This method calculates an explanation using a network for which the relu non-linearities are replaced by softplus 

> 5The fact that _Dun_ ( _p_ ) _∈ TpS_ follows by taking the directional derivative with respect to _u_ on both sides of _⟨n, n⟩_ = 1 . 

7 



<!-- Start of picture text -->
h ( xadv ) & h t Softplus Softplus Softplus Softplus<br>Image ReLU β = 5 β = 0 . 8 Image ReLU β = 5 β = 0 . 8<br>h ( xadv ) & h ( x )<br>1.0<br>0.5<br>0.0<br>1.0<br>0.5<br>0.0<br>10 0 10 1 10 2<br>β<br>Original Original<br>PCCGradient<br>Manipulated Manipulated<br>PCCLRP<br>Target Target<br><!-- End of picture text -->

Figure 4: Left: _β_ dependence for the correlations of the manipulated explanation (here Gradient and LRP) with the target and original explanation. Lines denote the medians, 10<sup>_th_</sup> and 90<sup>_th_</sup> percentiles are shown in semitransparent colour. Center and Right: network input and the respective explanation maps as _β_ is decreased for Gradient (center) and LRP (right). 

with a small _β_ parameter to smooth the principle curvatures. The precise value of _β_ is a hyperparameter of the method, but we find that a value around one works well in practice. 

As shown in the supplement, a relation between SmoothGrad [12] and _β_ -smoothing can be proven for a one-layer neural network: 

**Theorem 2** _For a one-layer neural network g_ ( _x_ ) = _relu_ ( _w_<sup>_T_</sup> _x_ ) _and its β-smoothed counterpart gβ_ ( _x_ ) = _softplusβ_ ( _w_<sup>_T_</sup> _x_ ) _, it holds that_ 





Since _pβ_ ( _x_ ) closely resembles a normal distribution with variance _σ_ = log(2) _~~<u>√</u>~~ β_ <u>2</u> _<u>π</u>_<sup>,</sup><sup>_β_-smoothing</sup> can be understood as _N →∞_ limit of SmoothGrad _h_ ( _x_ ) = _N_ <u>1</u> � _Ni_ =1<sup>_∇g_(</sup><sup>_x −ϵi_)where</sup> _ϵi ∼ gβ ≈N_ (0 _, σ_ ). We emphasize that the theorem only holds for a one-layer neural network, but for deeper networks we empirically observe that both lead to visually similar maps as they are considerably less noisy than the gradient map. The theorem therefore suggests that SmoothGrad can similarly be used to smooth the curvatures and can thereby make explanations more robust.<sup>6</sup> 

**Experiments:** Figure 4 demonstrates that _β_ -smoothing allows us to recover the orginal explanation map by lowering the value of the _β_ parameter. We stress that this works for all considered methods. We also note that the same effect can be observed using SmoothGrad by successively increasing the standard deviation _σ_ of the noise distribution. This further underlines the similarity between the two smoothing methods. 

If an attacker knew that smoothing was used to undo the manipulation, they could try to attack the smoothed method 



<!-- Start of picture text -->
unsmoothed smoothed<br><!-- End of picture text -->



directly. However, both _β_ -smoothing and SmoothGrad are substantially more robust than their non-smoothed counterparts, see Figure 5. It is important to note that _β_ -smoothing achieves this at considerably lower computational cost: _β_ -smoothing only requires a single forward and backward pass, while SmoothGrad requires as many as the number of noise samples (typically between 10 to 50). 

We refer to Supplement D for more details on these experiments. 

> 6For explanation methods _h_ ( _x_ ) other than gradient, SmoothGrad needs to be used in a slightly generalized form, i.e. _N_ <u>1</u> � _Ni_ =1<sup>_h_(</sup><sup>_x −ϵi_).</sup> 

8 



<!-- Start of picture text -->
PCC between h t and h ( xadv ) PCC between h t and h ( xadv ) Runtime<br>0 . 100<br>0 . 8 0 . 8<br>0 . 075<br>0 . 6 0 . 6<br>0 . 050<br>0 . 4 0 . 4<br>0 . 025<br>0 . 2 0 . 2<br>0 . 000<br>0 . 25 0 . 50 0 . 75 0 . 25 0 . 50 0 . 75<br>β -smoothed Gradient β -smoothed Gradient<br>β -smoothed SmoothGrad<br>Gradient seconds<br>SmoothGrad<br><!-- End of picture text -->

Figure 5: Left: markers are clearly left of the diagonal, i.e. explanations are more robust to manipulations when _β_ -smoothing is used. Center: SmoothGrad has comparable results to _β_ -smoothing, i.e. markers are distributed around the diagonal. Right: _β_ -smoothing has significantly lower computational cost than SmoothGrad. 

## **5 Conclusion** 

Explanation methods have recently become increasingly popular among practitioners. In this contribution we show that dedicated imperceptible manipulations of the input data can yield arbitrary and drastic changes of the explanation map. We demonstrate both qualitatively and quantitatively that explanation maps of many popular explanation methods can be arbitrarily manipulated. Crucially, this can be achieved while keeping the model’s output constant. A novel theoretical analysis reveals that in fact the large curvature of the network’s decision function is one important culprit for this unexpected vulnerability. Using this theoretical insight, we can profoundly increase the resilience to manipulations by smoothing _only_ the explanation process while leaving the model itself unchanged. 

Future work will investigate possibilities to modify the training process of neural networks itself such that they can become less vulnerable to manipulations of explanations. Another interesting future direction is to generalize our theoretical analysis from gradient to propagation-based methods. This seems particularly promising because our experiments strongly suggest that similar theoretical findings should also hold for these explanation methods. 

## **References** 

- [1] David Baehrens, Timon Schroeter, Stefan Harmeling, Motoaki Kawanabe, Katja Hansen, and Klaus-Robert Müller. How to explain individual classification decisions. _Journal of Machine Learning Research_ , 11(Jun):1803–1831, 2010. 

- [2] Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. Deep inside convolutional networks: Visualising image classification models and saliency maps. In _2nd International Conference on Learning Representations, ICLR 2014, Banff, AB, Canada, April 14-16, 2014, Workshop Track Proceedings_ , 2014. 

- [3] Matthew D. Zeiler and Rob Fergus. Visualizing and understanding convolutional networks. In _Computer Vision - ECCV 2014 - 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part I_ , pages 818–833, 2014. 

- [4] Jost Tobias Springenberg, Alexey Dosovitskiy, Thomas Brox, and Martin A. Riedmiller. Striving for simplicity: The all convolutional net. In _3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Workshop Track Proceedings_ , 2015. 

9 

- [5] Sebastian Bach, Alexander Binder, Grégoire Montavon, Frederick Klauschen, KlausRobert Müller, and Wojciech Samek. On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. _PloS one_ , 10(7):e0130140, 2015. 

- [6] Ramprasaath R. Selvaraju, Abhishek Das, Ramakrishna Vedantam, Michael Cogswell, Devi Parikh, and Dhruv Batra. Grad-cam: Why did you say that? visual explanations from deep networks via gradient-based localization. _CoRR_ , abs/1610.02391, 2016. 

- [7] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why should i trust you?: Explaining the predictions of any classifier. In _Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining_ , pages 1135–1144. ACM, 2016. 

- [8] Luisa M. Zintgraf, Taco S. Cohen, Tameem Adel, and Max Welling. Visualizing deep neural network decisions: Prediction difference analysis. In _5th International Conference on Learning Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Conference Track Proceedings_ , 2017. 

- [9] Avanti Shrikumar, Peyton Greenside, and Anshul Kundaje. Learning important features through propagating activation differences. In _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_ , pages 3145–3153, 2017. 

- [10] Scott M Lundberg and Su-In Lee. A unified approach to interpreting model predictions. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems 30_ , pages 4765–4774. Curran Associates, Inc., 2017. 

- [11] Piotr Dabkowski and Yarin Gal. Real time image saliency for black box classifiers. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems 30_ , pages 6967–6976. Curran Associates, Inc., 2017. 

- [12] Daniel Smilkov, Nikhil Thorat, Been Kim, Fernanda B. Viégas, and Martin Wattenberg. Smoothgrad: removing noise by adding noise. _CoRR_ , abs/1706.03825, 2017. 

- [13] Mukund Sundararajan, Ankur Taly, and Qiqi Yan. Axiomatic attribution for deep networks. In _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_ , pages 3319–3328, 2017. 

- [14] Avanti Shrikumar, Peyton Greenside, and Anshul Kundaje. Learning important features through propagating activation differences. In _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_ , pages 3145–3153, 2017. 

- [15] Ruth C Fong and Andrea Vedaldi. Interpretable explanations of black boxes by meaningful perturbation. In _2017 IEEE international conference on computer vision (ICCV)_ , pages 3449–3457. IEEE, 2017. 

- [16] Grégoire Montavon, Sebastian Lapuschkin, Alexander Binder, Wojciech Samek, and Klaus-Robert Müller. Explaining nonlinear classification decisions with deep taylor decomposition. _Pattern Recognition_ , 65:211–222, 2017. 

- [17] Pieter-Jan Kindermans, Kristof T Schütt, Maximilian Alber, Klaus-Robert Müller, Dumitru Erhan, Been Kim, and Sven Dähne. Learning how to explain neural networks: Patternnet and patternattribution. _International Conference on Learning Representations_ , 2018. `https://openreview.net/forum?id=Hkn7CBaTW` . 

10 

- [18] Been Kim, Martin Wattenberg, Justin Gilmer, Carrie Cai, James Wexler, Fernanda Viegas, and Rory Sayres. Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (tcav). _arXiv preprint arXiv:1711.11279_ , 2017. 

- [19] Sebastian Lapuschkin, Stephan Wäldchen, Alexander Binder, Grégoire Montavon, Wojciech Samek, and Klaus-Robert Müller. Unmasking clever hans predictors and assessing what machines really learn. _Nature communications_ , 10(1):1096, 2019. 

- [20] Amirata Ghorbani, Abubakar Abid, and James Y. Zou. Interpretation of neural networks is fragile. _CoRR_ , abs/1710.10547, 2017. 

- [21] Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne, Dumitru Erhan, and Been Kim. The (un)reliability of saliency methods. _CoRR_ , abs/1711.00867, 2017. 

- [22] Julius Adebayo, Justin Gilmer, Michael Muelly, Ian J. Goodfellow, Moritz Hardt, and Been Kim. Sanity checks for saliency maps. _CoRR_ , abs/1810.03292, 2018. 

- [23] Maximilian Alber, Sebastian Lapuschkin, Philipp Seegerer, Miriam Hägele, Kristof T. Schütt, Grégoire Montavon, Wojciech Samek, Klaus-Robert Müller, Sven Dähne, and Pieter-Jan Kindermans. innvestigate neural networks! _Journal of Machine Learning Research_ **_20_** , 2019. 

- [24] Marco Ancona, Enea Ceolini, Cengiz Oztireli, and Markus Gross. Towards better understanding of gradient-based attribution methods for deep neural networks. In _6th International Conference on Learning Representations (ICLR 2018)_ , 2018. 

- [25] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. _International Conference on Learning Representations_ , 2014. 

- [26] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. _International Journal of Computer Vision (IJCV)_ , 115(3):211–252, 2015. 

- [27] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. _CoRR_ , abs/1512.03385, 2015. 

- [28] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton. Imagenet classification with deep convolutional neural networks. In _Proceedings of the 25th International Conference on Neural Information Processing Systems - Volume 1_ , NIPS’12, pages 1097–1105, USA, 2012. Curran Associates Inc. 

- [29] Gao Huang, Zhuang Liu, and Kilian Q. Weinberger. Densely connected convolutional networks. _CoRR_ , abs/1608.06993, 2016. 

- [30] Alex Krizhevsky. Learning multiple layers of features from tiny images, 2009. 

- [31] Loring W Tu. _Differential geometry: connections, curvature, and characteristic classes_ , volume 275. Springer, 2017. 

11 

# **Supplement** 

## **Contents** 

|**A **|**Details on experiments**|**12**|
|---|---|---|
||A.1 Beta growth . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>13|
|**B **|**Difference in network output**|**14**|
|**C **|**Generalization over architectures and data sets**|**15**|
||C.1 Additional architectures . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>15|
||C.2 Additional datasets . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>16|
|**D **|**Smoothing explanation methods**|**20**|
|**E **|**Proofs**|**25**|
||E.1<br>Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>25|
||E.2<br>Theorem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>27|
|**F **|**Additional examples for VGG**|**28**|
|**A**|**Details on experiments**||



We provide a _run_attack.py_ file in our reference implementation which allows one to produce manipulated images. The hyperparameter choices used in our experiments are summarized in Table 1. We set _β_ 0 = 10 and _βe_ = 100 for beta growth (see section below for a description). The column ’factors’ summarizes the weighting of the mean squared error of the heatmaps and the images respectively. 

|method|iterations|lr|factors|
|---|---|---|---|
|Gradient|1500|10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|Grad x Input|1500|10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|IntGrad|500|5_×_10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|LRP|1500|2_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|GBP|1500|10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|PA|1500|2_×_10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|



Table 1: Hyperparameters used in our analysis. 

The patterns for explanation method PA are trained on a subset of the ImageNet training set. The baseline _x_ ¯ for explanation method IG was set to zero. To approximate the integral, we use 30 steps for which we verified that the attributions approximately adds up to the score at the input. 

12 

### **A.1 Beta growth** 

In practise, we observe that we get slightly better results by increasing the value of _β_ of the softplus _sp_ ( _x_ ) = _β_<sup><u>1</u>ln (1 +</sup><sup>_eβx_)duringtrainingastartvalue</sup><sup>_β_0toafinalvalue</sup><sup>_βe_using</sup> 



where _t_ is the current optimization step and _T_ denotes the total number of steps. Figure 6 shows the MSE for images and explanation maps during training with and without _β_ -growth. This strategy is however not essential for our results. 



<!-- Start of picture text -->
β = 10 β ∈ [10 ,  100] β = 100 β = 1000<br>× 10 − 4 × 10 − 10<br>6<br>2 . 5<br>5<br>2 . 0<br>4<br>1 . 5<br>1 . 0 3<br>0 . 5 2<br>0 . 0 1<br>0 1000 2000 0 1000 2000<br>Iterations Iterations<br>MSEImages<br>MSEExplanations<br><!-- End of picture text -->

Figure 6: MSE between _x_ and _xadv_ (left) and between _h_<sup>_t_</sup> and _h_ ( _xadv_ ) (right) for various values for _β_ . 

We use beta growth for all methods except LRP for which we do not find any speed-up in the optimization as the LRP rules do not explicitly depend on the second derivative of the relu activations. Figure 7 demonstrates that for large beta values the softplus networks approximate the relu network well. Figure 8 and Figure 9 show this for an example for the gradient and the LRP explanation method. We also note that for small beta the gradient explanation maps become more similar to LRP/GPB/PA explanation maps. 



<!-- Start of picture text -->
1e 9<br>2.0 1.0 1.0<br>1.5 0.8<br>0.8<br>1.0 0.6<br>0.4<br>0.5<br>0.6<br>0.2<br>0.0<br>10 0 10 1 10 2 10 3 10 0 10 1 10 2 10 3 10 0 10 1 10 2 10 3<br>beta<br>MSE SSIM PCC<br><!-- End of picture text -->

Figure 7: Error measures between the gradient explanation map produced with the original network and explanation maps produced with a network with softplus activation functions using various values for _β_ . 

13 



<!-- Start of picture text -->
Image ReLU β = 10 β = 3 β = 2 β = 1<br><!-- End of picture text -->

Figure 8: Gradient explanation map produced with the original network and a network with softplus activation functions using various values for _β_ . 



<!-- Start of picture text -->
Image ReLU β = 10 β = 3 β = 2 β = 1<br><!-- End of picture text -->

Figure 9: LRP explanation map produced with the original network and a network with softplus activation functions using various values for _β_ . 

## **B Difference in network output** 

Figure 10 summarizes the change in the output of the network due to the manipulation. We note that all images have the same classification result as the orginals. Furthermore, we note that the change in confidence is small. Last but not least, norm of the vector of all class probabilities is also very small. 

14 



<!-- Start of picture text -->
× 10 1<br>1<br>2<br>0 0<br>× 10 − 6 × 10 − 6<br>1 0 . 5<br>0 0 . 0<br>1 1<br>0 0<br>× 10 1<br>2 . 5<br>0<br>0 . 0<br>− 1<br>× 10 − 2 2 × 10 − 2<br>1<br>0 0<br>Gradient Gradient Integrated LRP GBP PA<br>x Input Gradients<br>2<br>12 ∥ ()()˜ gxgxadv −N<br>2<br>12 ∥ ()() gxgxadv −N<br>log(()) gxadv− c<br>()()˜ gxgxadv −c<br>()() gxgxadv −c<br><!-- End of picture text -->

Figure 10: Error analysis of Network output. _g_ ˜( _x_ ) denotes pre-activation of the last layer. _g_ ( _x_ ) is the network output after applying the softmax function to the pre-activation _g_ ˜( _x_ ). 

## **C Generalization over architectures and data sets** 

Manipulable explanations are not only a property of the VGG-16 network. In this section, we show that our algorithm to manipulate explanations can also be applied to other architectures and data sets. For the experiments, we optimize the loss function given in the main text. We keep the pre-activation for all network architectures approximately constant, which also leads to approximately constant activation. 

### **C.1 Additional architectures** 

In addition to the VGG architecture we also analyzed the explanation’s susceptibility to manipulations for the AlexNet, Densenet and ResNet architectures. The hyperparameter choices used in our experiments are summarized in Table 2. We set _β_ 0 = 10 and _βe_ = 100 for beta growth. Only for Densenet we set _β_ 0 = 30 and _βe_ = 300 as for smaller beta values the explanation map produced with softplus does not resemble the explanation map produced with relu. Figure 12 and 11 show that the similarity measures are comparable for all network architectures for the gradient method. 

Figure 13, 15, 16 and 14 show one example image for each architecture. 

|network|iterations|lr|factors|
|---|---|---|---|
|VGG16|1500|10<sup>_−_3</sup>|1e11, 10|
|AlexNet|4000|10<sup>_−_3</sup>|1e11, 10|
|Densenet-121|2000|5_×_10<sup>_−_4</sup>|1e11, 10|
|ResNet-18|2000|10<sup>_−_3</sup>|1e11, 10|



Table 2: Hyperparameters used in our analysis for all networks. 

15 



<!-- Start of picture text -->
× 10 − 2<br>3<br>2<br>1<br>× 10 − 6<br>2 . 5<br>0 . 0<br>2<br>0<br>× 10 − 1<br>0 . 0<br>− 2 . 5<br>× 10 − 2<br>2 . 5<br>0 . 0<br>− 2 . 5<br>VGG-16 ResNet-18 AlexNet Densenet-121<br>2<br>12 ∥∥ ()()˜˜ gxgxadv −N<br>2<br>12 ∥∥ ()() gxgxadv −N<br>log(()) gxadv− c<br>()()˜ gxgxadv −c<br>()() gxgxadv −c<br><!-- End of picture text -->

Figure 11: . Change in output for various architectures. 

### **C.2 Additional datasets** 

We trained the VGG-16 architecture on the CIFAR-10 dataset<sup>1</sup> . The test accuracy is approximately 92%. We then used our algorithm to manipulate the explanations for the LRP method. The hyperparameters are summarized in Table 3. Two example images can be seen in Figure 17. 

|method|iterations|lr|factors|
|---|---|---|---|
|LRP|1500|2_×_10<sup>_−_4</sup>|10<sup>7</sup>, 10<sup>2</sup>|



Table 3: Hyperparameters used in our analysis for the CIFAR-10 Dataset. 

> 1code for training VGG on CIFAR-10 from `https://github.com/chengyangfu/pytorch-vgg-cifar10` 

16 



<!-- Start of picture text -->
× 10 − 10 Errors Explanations × 10 − 3 Errors Images<br>3 . 0<br>0 . 8<br>2 . 5<br>0 . 6<br>2 . 0<br>0 . 4<br>1 . 5 0 . 2<br>0 . 8<br>0 . 95<br>0 . 6<br>0 . 90<br>0 . 4<br>0 . 85<br>× 10 − 1<br>1 . 0000<br>8<br>0 . 9975<br>7<br>0 . 9950<br>6<br>0 . 9925<br>5<br>0 . 9900<br>4<br>VGG-16 ResNet-18 AlexNet Densenet-121 VGG-16 ResNet-18 AlexNet Densenet-121<br>MSE MSE<br>SSIM SSIM<br>PCC PCC<br><!-- End of picture text -->

Figure 12: Similarity measures for gradient method for various architectures. 



Figure 13: Gradient explanation maps produced with VGG-16 model. 

17 



Figure 14: Gradient explanation maps produced with ResNet-18 model. 



Figure 15: Gradient explanation maps produced with AlexNet model. 

18 



Figure 16: Gradient explanation maps produced with Densenet-121 model. 





Figure 17: LRP Method on CIFAR-10 dataset 

19 

## **D Smoothing explanation methods** 

One can achieve a smoothing effect when substituting the relu activations for softplus _β_ activations and then applying the usual rules for the different explanation methods. 

A smoothing effect can also be achieved by applying the smoothgrad explanation method, see Figure 18. That is adding random perturbation to the image and then averaging over the resulting explanation maps. We average over 10 perturbed images with different values for the standard deviation _σ_ of the Gaussian noise. The noise level _n_ is related to _σ_ as _σ_ = _n ·_ ( _xmax − xmin_ ), where _xmax_ and _xmin_ are the maximum and minimum values the input image can have. 



<!-- Start of picture text -->
h ( xadv ) & h t Smoothgrad Smoothgrad Smoothgrad Smoothgrad<br>Image ReLU noise: 0 . 5% noise: 5 . 0% Image ReLU noise: 0 . 5% noise: 5 . 0%<br>h ( xadv ) & h ( x )<br>1.0<br>0.5<br>0.0<br>1.0<br>0.5<br>0.0<br>10 − 1 10 0 10 1<br>noise in %<br>Original Original<br>PCCGradient<br>Manipulated Manipulated<br>PCCLRP<br>Target Target<br><!-- End of picture text -->

Figure 18: Recovering the original explanation map with SmoothGrad. Left: _β_ dependence for the correlations of the manipulated explanation (here Gradient and LRP) with the target and original explanation. Line denotes median, 10<sup>_th_</sup> and 90<sup>_th_</sup> percentile are shown in semitransparent colour. Center and Right: network input and the respective explanation maps as _β_ is lowered for Gradient (center) and LRP (right). 

The _β_ -smoothing or SmoothGrad explanation maps are more robust with respect to manipulations. Figure 19, 20 and 21 show results (MSE, SSIM and PCC) for 100 targeted attacks on the original explanation, the SmoothGrad explanation and the _β_ -smoothed explanation for explanation methods Gradient and LRP. 

For manipulation of SmoothGrad we use beta growth with _β_ 0 = 10 and _βe_ = 100. For manipulation of _β_ -Smoothing we set _β_ = 0 _._ 8 for all runs. The hyperparameters for SmoothGrad and _β_ -Smoothing are summarized in Table 4 and Table 5. 

|method|iterations|lr|factors|
|---|---|---|---|
|Gradient|1500<br>3|_×_10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|LRP|1500<br>3|_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|



Table 4: Hyperparameters used in our analysis for SmoothGrad. 

|method|iterations|lr|factors|
|---|---|---|---|
|Gradient|500|2_._5_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|Grad x Input|500|2_._5_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|IntGrad|200|2_._5_×_10<sup>_−_3</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|LRP|1500|2_._0_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|GBP|500|5_._0_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|
|PA|500|5_._0_×_10<sup>_−_4</sup>|10<sup>11</sup>, 10<sup>6</sup>|



Table 5: Hyperparameters used in our analysis for _β_ -smoothing. 

20 



<!-- Start of picture text -->
× 10 − 9 MSE Explanation MSE Images<br>5<br>0.001<br>4<br>3 0.000<br>2<br>0.000<br>1<br>2 4 0 . 0002 0 . 0004 0 . 0006<br>Smoothed Gradient × 10 − 9 Smoothed Gradient<br>× 10 − 9<br>1 . 5 0.001<br>1 . 0 0.000<br>0 . 5 0.000<br>0 . 5 1 . 0 1 . 5 0 . 0002 0 . 0004 0 . 0006<br>Smoothed LRP × 10 − 9 Smoothed LRP<br>β -smoothed SmoothGrad<br>Gradient Gradient<br>LRP LRP<br><!-- End of picture text -->

Figure 19: Left: Similarities between explanations. Markers are mostly right of the diagonal, i.e. the MSE for the smoothed explanations is higher than for the unsmoothed explanations which means the manipulated smoothed explanation map does not closely resemble the target _h_<sup>_t_</sup> . Right: Similarities between Images. The MSE for the smoothed methods is higher (right of the diagonal) or comparable (on the diagonal), i.e. bigger or comparable perturbations in the manipulated Images when using smoothed explanation methods. 

In Figure 22 and Figure 23, we directly compare the original explanation methods with the _β_ -smoothed explanation methods. An increase in robustness can be seen for all methods: explanation maps for _β_ -smoothed explanations have higher MSE and lower SSIM and PCC than explanation maps for the original methods. The similarity measures for the manipulated images are of comparable magnitude. 

21 



<!-- Start of picture text -->
SSIM Explanations SSIM Images<br>1 . 0 1.000<br>0.950<br>0 . 8<br>0.900<br>0 . 6<br>0.850<br>0 . 4 0.800<br>0 . 4 0 . 6 0 . 8 1 . 0 0 . 8 0 . 9 1 . 0<br>Smoothed Gradient Smoothed Gradient<br>1 . 0 1.000<br>0.950<br>0 . 8<br>0.900<br>0 . 6<br>0.850<br>0 . 4 0.800<br>0 . 4 0 . 6 0 . 8 1 . 0 0 . 8 0 . 9 1 . 0<br>Smoothed LRP Smoothed LRP<br>β -smoothed SmoothGrad<br>Gradient Gradient<br>LRP LRP<br><!-- End of picture text -->

Figure 20: Left: Similarities between explanations. Markers are mostly left of the diagonal, i.e. the SSIM for the smoothed explanations is lower than for the unsmoothed explanations which means the manipulated smoothed explanation map does not closely resemble the target _h_<sup>_t_</sup> . Right: Similarities between Images. The SSIM for the smoothed methods is lower (left of the diagonal) or comparable (on the diagonal), i.e. bigger or comparable perturbations in the manipulated Images when using smoothed explanation methods. 

22 



<!-- Start of picture text -->
PCC Explanations PCC Images<br>1 . 0 1.000<br>0 . 8 0.998<br>0 . 6<br>0.995<br>0 . 4<br>0.993<br>0 . 2<br>0.990<br>0 . 25 0 . 50 0 . 75 1 . 00 0 . 990 0 . 995 1 . 000<br>Smoothed Gradient Smoothed Gradient<br>1 . 0 1.000<br>0 . 8 0.998<br>0 . 6<br>0.995<br>0 . 4<br>0.993<br>0 . 2<br>0.990<br>0 . 25 0 . 50 0 . 75 1 . 00 0 . 990 0 . 995 1 . 000<br>Smoothed LRP Smoothed LRP<br>β -smoothed SmoothGrad<br>Gradient Gradient<br>LRP LRP<br><!-- End of picture text -->

Figure 21: Left: Similarities between explanations. Markers are mostly left of the diagonal, i.e. the PCC for the smoothed explanations is lower than for the unsmoothed explanations which means that the manipulated smoothed explanation map does not closely resemble the target _h_<sup>_t_</sup> . Right: Similarities between Images. The PCC for the smoothed methods is lower (left of the diagonal) or comparable (on the diagonal), i.e. bigger or comparable perturbations in the manipulated Images when using smoothed explanation methods. 



<!-- Start of picture text -->
× 10 − 9<br>4<br>2<br>0<br>0 . 8<br>0 . 6<br>0 . 4<br>1 . 00<br>0 . 75<br>0 . 50<br>0 . 25<br>Gradient Gradient Integrated LRP GBP PA<br>β -smoothedG xInput β -smoothedGxI Gradients β -smoothedIG β -smoothedLRP β -smoothedGBP β -smoothedPA<br>MSE<br>SSIM<br>PCC<br><!-- End of picture text -->

Figure 22: Comparison of Similarities of Explanation Maps for the original Explanation Methods and the _β_ -smoothed Explanation Methods. Targeted attacks do not work very well on _β_ -smoothed explanations, i.e. MSE is higher and SSIM and PCC are lower for the _β_ -smoothed explanations than for the original explanations. 

23 



<!-- Start of picture text -->
× 10 − 3<br>1 . 0<br>0 . 5<br>0 . 0<br>0 . 9<br>0 . 8<br>1 . 000<br>0 . 995<br>0 . 990<br>Gradient Gradient Integrated LRP GBP PA<br>β -smoothedG xInput β -smoothedGxI Gradients β -smoothedIG β -smoothedLRP β -smoothedGBP β -smoothedPA<br>MSE<br>SSIM<br>PCC<br><!-- End of picture text -->

Figure 23: Comparison of Similarities between original and manipulated images. The similarity measures for images for the _β_ -smoothed explanation methods are of comparable size or slightly worse (higher MSE, lower SSIM and lower PCC) than for the original explanation method, i.e. the manipulations are more visible for the _β_ -smoothed explanation methods. 



<!-- Start of picture text -->
= 1<br><!-- End of picture text -->

Figure 24: Contour plot of a 2-Layer Neural Network _f_ ( _x_ ) = _V_<sup>_⊤_</sup> softplus( _W_<sup>_⊤_</sup> _x_ ) with _x ∈_ [ _−_ 1 _,_ 1]<sup>2</sup> , _W ∈_ R<sup>2</sup><sup>_×_50</sup> , _V ∈_ R<sup>50</sup> and _Vi, Wij ∼_ U( _−_ 1 _,_ 1). Using a softplus activation with _β_ = 1 visibly reduces curvature compared to a ReLU activation with _β →∞_ . 

24 

## **E Proofs** 

In this section, we collect the proofs of the theorems stated in the main text. 

### **E.1 Theorem 1** 

**Theorem 3** _Let f_ : R<sup>_d_</sup> _→_ R _be a network with softplusβ non-linearities and Uϵ_ ( _p_ ) = _{x ∈_ R<sup>_d_</sup> ; _∥x − p∥ < ϵ} an environment of a point p ∈ S such that Uϵ_ ( _p_ ) _∩ S is fully connected. Let f have bounded derivatives ∥∇f_ ( _x_ ) _∥≥ c for all x ∈Uϵ_ ( _p_ ) _∩ S. It then follows for all p_ 0 _∈Uϵ_ ( _p_ ) _∩ S that_ 



_where λmax is the principle curvatures with the largest absolute value for any point in Uϵ_ ( _p_ ) _∩S and the constant C >_ 0 _depends on the weights of the neural network._ 

**Proof:** This proof will proceed in four steps. We will first bound the Frobenius norm of the Hessian of the network _f_ . From this, we will deduce an upper bound on the Frobenius norm of the second fundamental form. This in turn will allow us to bound the largest principle curvature _|λmax|_ = max _{|λ_ 1 _| . . . |λd−_ 1 _|}_ . Finally, we will bound the maximal and minimal change in explanation. 

**Step 1:** Let softplus<sup>(</sup><sup>_l_)</sup> ( _x_ ) = softplus( _W_<sup>(</sup><sup>_l_)</sup> _x_ ) where _W_<sup>(</sup><sup>_l_)</sup> are the weights of layer _l_ .<sup>2</sup> We note that 





where 



The activation at layer _L_ is then given by 



Its derivative is given by 



We therefore obtain 



> 2We do not make the dependence of softplus on its _β_ parameter explicit to ease notation. 

25 

Deriving the expression for _∂ka_<sup>(</sup> _i_<sup>_L_)</sup> again, we obtain 



We now restrict to the case for which the index _i_ only takes a single value and use _|σ_ ( _•_ ) _| ≤_ 1. The Hessian _Hij_ = _∂i∂ja_<sup>_L_</sup> ( _x_ ) is then bounded by 



where the constant is given by 



**Step 2:** Let _e_ 1 _. . . ed−_ 1 be a basis of the tangent space _TpS_ . Then the second fundamental form for the hypersurface _f_ ( _x_ ) = _c_ at point _p_ is given by 



We now use the fact that _⟨∇f_ ( _p_ ) _, ej⟩_ = 0, i.e. the gradient of _f_ is normal to the tangent space. This property was explained in the main text. This allows us to deduce that 



**Step 3:** The Frobenius norm of the second fundamental form (considered as a matrix in the sense of step 2) can be written as 



where _λi_ are the principle curvatures. This property follows from the fact that the second fundamental form is symmetric and can therefore be diagonalized with real eigenvectors, e.g. the principle curvatures. Using the fact that the derivative of the network is bounded from below, _∥∇f_ ( _p_ ) _∥≥ c_ , we obtain 



**Step 4:** For _p, p_ 0 _∈Uϵ_ ( _p_ ) _∩S_ , we choose a curve _γ_ with _γ_ ( _t_ 0) = _p_ 0 and _γ_ ( _t_ ) = _p_ . Furthermore, we use the notation _u_ ( _t_ ) = _γ_ ˙ ( _t_ ). It then follows that 



26 

Using the fact that _Du_ ( _t_ ) _n_ ( _γ_ ( _t_ )) _∈ Tγ_ ( _t_ ) _S_ and choosing an orthonormal basis _ei_ ( _t_ ) for the tangent spaces, we obtain 





The second fundamental form _L_ is bilinear and therefore 



We now use the notation _Lij_ ( _t_ ) = _L_ ( _ej_ ( _t_ ) _, ei_ ( _t_ )) and choose its eigenbasis for _ei_ ( _t_ ). We then obtain for the difference in the unit normals: 



where _λi_ ( _t_ ) denote the principle curvatures at _γ_ ( _t_ ). By orthonormality of the eigenbasis, it can be easily checked that 



Using this relation and the triangle inequality, we then obtain by taking the norm on both sides of (28): 



This inequality holds for any curve connecting _p_ and _p_ 0 but the tightest bound follows by choosing _γ_ to be the shortest possible path in _Uϵ_ ( _p_ ) _∩ S_ with length � _tt_ 0<sup>_∥γ_˙(</sup><sup>_t_)</sup><sup>_∥dt_,i.e.the</sup> geodesic distance _dg_ ( _p, p_ 0) on _Uϵ_ ( _p_ ) _∩ S_ . The second inequality of the theorem is obtained by the upper bound on the largest principle curvature _λmax_ derived above, i.e. (23). 

### **E.2 Theorem 2** 

**Theorem 4** _For one layer neural networks g_ ( _x_ ) = _relu_ ( _w_<sup>_T_</sup> _x_ ) _and gβ_ ( _x_ ) = _softplusβ_ ( _w_<sup>_T_</sup> _x_ ) _, it holds that_ 



_where pβ_ ( _ϵ_ ) = ( _e_<sup>_βϵ/_2</sup> + _<u>βe</u>_<sup>_−βϵ/_2</sup> )<sup>2</sup><sup>_._</sup> 

**Proof:** We first show that 



for a scalar input _x_ . This follows by defining _p_ ( _ϵ_ ) implicitly as 



27 

Differentiating both sides of this equation with respect to _x_ results in 



where Θ( _x_ ) = I( _x >_ 1) is the Heaviside step function and _σβ_ ( _x_ ) = (1+ _e_ <u>1</u><sup>_−βx_</sup> )<sup>.Differentiating</sup> both sides with respect to _x_ again results in 



Therefore, (31) holds. For a vector input _⃗x_ , we define the distribution of its perturbation _⃗ϵ_ by 



where _ϵi_ denotes the components of _⃗ϵ_ . We will suppress any arrows denoting vector-valued variables in the following in order to ease notation. We choose an orthogonal basis such that 



This allows us to rewrite 



By changing the integration variable to _ϵ_ = _∥w∥ ϵp_ and using (31), we obtain 



The theorem then follows by deriving both sides of the equation with respect to _x_ . 

## **F Additional examples for VGG** 

28 





Figure 25: Explanation map produced with the Gradient Explanation Method on VGG. 

29 





Figure 26: Explanation map produced with the Gradient _×_ Input Explanation Method on VGG. 

30 





Figure 27: Explanation map produced with the Integrated Gradients Explanation Method on VGG. 

31 





Figure 28: Explanation map produced with the LRP Explanation Method on VGG. 

32 





Figure 29: Explanation map produced with the Guided Backpropagation Explanation Method on VGG. 

33 





Figure 30: Explanation map produced with the Pattern Attribution Explanation Method on VGG. 

34 

