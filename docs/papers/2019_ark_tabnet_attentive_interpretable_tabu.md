---
title: "TabNet: Attentive Interpretable Tabular Learning"
authors: "arık"
year: 2019
arxiv_id: "1908.07442"
original_file: "1908.07442.pdf"
pdf_path: "docs/papers\2019_ark_tabnet_attentive_interpretable_tabu.pdf"
---

# TabNet: Attentive Interpretable Tabular Learning

**Authors:** Arık et al.  
**Year:** 2019 | **arXiv:** [`1908.07442`](https://arxiv.org/abs/1908.07442)  
**Local PDF:** [`2019_ark_tabnet_attentive_interpretable_tabu.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_ark_tabnet_attentive_interpretable_tabu.pdf)

---

# **TabNet: Attentive Interpretable Tabular Learning** 

## **Sercan O. Arık, Tomas Pfister**<sup>**¨**</sup> 

Google Cloud AI Sunnyvale, CA soarik@google.com, tpfister@google.com 

#### **Abstract** 

We propose a novel high-performance and interpretable canonical deep tabular data learning architecture, TabNet. TabNet uses sequential attention to choose which features to reason from at each decision step, enabling interpretability and more efficient learning as the learning capacity is used for the most salient features. We demonstrate that TabNet outperforms other variants on a wide range of non-performance-saturated tabular datasets and yields interpretable feature attributions plus insights into its global behavior. Finally, we demonstrate self-supervised learning for tabular data, significantly improving performance when unlabeled data is abundant. 

## **Introduction** 

Deep neural networks (DNNs) have shown notable success with images (He et al. 2015), text (Lai et al. 2015) and audio (Amodei et al. 2015). For these, canonical architectures that efficiently encode the raw data into meaningful representations, fuel the rapid progress. One data type that has yet to see such success with a canonical architecture is tabular data. 

Despite being the most common data type in real-world AI (as it is comprised of any categorical and numerical features), (Chui et al. 2018), deep learning for tabular data remains under-explored, with variants of ensemble decision trees (DTs) still dominating most applications (Kaggle 2019a). Why? First, because DT-based approaches have certain benefits: (i) they are representionally efficient for decision manifolds with approximately hyperplane boundaries which are common in tabular data; and (ii) they are highly interpretable in their basic form (e.g. by tracking decision nodes) and there are popular post-hoc explainability methods for their ensemble form, e.g. (Lundberg, Erion, and Lee 2018) – this is an important concern in many real-world applications; (iii) they are fast to train. Second, because previously-proposed DNN architectures are not well-suited for tabular data: e.g. stacked convolutional layers or multi-layer perceptrons (MLPs) are vastly overparametrized – the lack of appropriate inductive bias often causes them to fail to find optimal solutions for tabular decision manifolds (Goodfellow, Bengio, and Courville 2016; Shavitt and Segal 2018; Xu et al. 2019). 

Why is deep learning worth exploring for tabular data? One obvious motivation is expected performance improve- 

Copyright © 2021, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 

ments particularly for large datasets (Hestness et al. 2017). In addition, unlike tree learning, DNNs enable gradient descentbased end-to-end learning for tabular data which can have a multitude of benefits: (i) efficiently encoding multiple data types like images along with tabular data; (ii) alleviating the need for feature engineering, which is currently a key aspect in tree-based tabular data learning methods; (iii) learning from streaming data and perhaps most importantly (iv) endto-end models allow representation learning which enables many valuable application scenarios including data-efficient domain adaptation (Goodfellow, Bengio, and Courville 2016), generative modeling (Radford, Metz, and Chintala 2015) and semi-supervised learning (Dai et al. 2017). 

We propose a new canonical DNN architecture for tabular data, TabNet. The main contributions are summarized as: 

1. _TabNet inputs raw tabular data without any preprocessing_ and is _trained using gradient descent-based optimization_ , enabling flexible integration into end-to-end learning. 

2. _TabNet uses sequential attention to choose which features to reason from at each decision step_ , enabling interpretability and better learning as the learning capacity is used for the most salient features (see Fig. 1). This feature selection is _instance-wise_ , e.g. it can be different for each input, and unlike other instance-wise feature selection methods like (Chen et al. 2018) or (Yoon, Jordon, and van der Schaar 2019), TabNet employs a _single deep learning architecture for feature selection and reasoning_ . 

3. Above design choices lead to two valuable properties: (i) _TabNet outperforms or is on par with other tabular learning models_ on various datasets for classification and regression problems from different domains; and (ii) _TabNet enables two kinds of interpretability_ : local interpretability that visualizes the importance of features and how they are combined, and global interpretability which quantifies the contribution of each feature to the trained model. 

4. Finally, _for the first time for tabular data_ , we show significant performance improvements by using unsupervised pre-training to predict masked features (see Fig. 2). 

## **Related Work** 

**Feature selection:** Feature selection broadly refers to judiciously picking a subset of features based on their usefulness for prediction. Commonly-used techniques such as for- 



<!-- Start of picture text -->
Input features<br>Professional occupation related Investment related<br>Feedback from  Feedback to<br>Feature selection Input processing Feature selection Input processing<br>previous step next step<br>… …<br>Aggregate information<br>Predicted output (whether the income level >$50k)<br><!-- End of picture text -->

Figure 1: TabNet’s sparse feature selection exemplified for Adult Census Income prediction (Dua and Graff 2017). Sparse feature selection enables interpretability and better learning as the capacity is used for the most salient features. TabNet employs multiple decision blocks that focus on processing a subset of input features for reasoning. Two decision blocks shown as examples process features that are related to professional occupation and investments, respectively, in order to predict the income level. 



<!-- Start of picture text -->
Unsupervised pre-training Supervised fine-tuning<br>Age Cap. gain Education Occupation Gender Relationship Age Cap. gain Education Occupation Gender Relationship<br>53 200000 ? Exec-managerial F Wife 60 200000 Bachelors Exec-managerial M Husband<br>19 0 ? Farming-fishing M ? 23 0 High-school Farming-fishing M Unmarried<br>? 5000 Doctorate Prof-specialty M Husband 45 5000 Doctorate Prof-specialty M Husband<br>25 ? ? Handlers-cleaners F Wife 23 0 High-school Handlers-cleaners F Wife<br>59 300000 Bachelors ? ? Husband 56 300000 Bachelors Exec-managerial M Husband<br>33 0 Bachelors ? F ? 38 10000 Bachelors Prof-specialty F Wife<br>? 0 High-school Armed-Forces ? Husband 23 0 High-school Armed-Forces M Husband<br>TabNet encoder TabNet encoder<br>TabNet decoder Decision making<br>Age Cap. gain Education Occupation Gender Relationship Income > $50k<br>Masters True<br>High-school Unmarried False<br>43 True<br>0 High-school F False<br>Exec-managerial M True<br>Adm-clerical Wife True<br>39 M False<br><!-- End of picture text -->

Figure 2: Self-supervised tabular learning. Real-world tabular datasets have interdependent feature columns, e.g., the education level can be guessed from the occupation, or the gender can be guessed from the relationship. Unsupervised representation learning by masked self-supervised learning results in an improved encoder model for the supervised learning task. 

ward selection and Lasso regularization (Guyon and Elisseeff 2003) attribute feature importance based on the entire training data, and are referred as _global_ methods. _Instance-wise_ feature selection refers to picking features individually for each input, studied in (Chen et al. 2018) with an explainer model to maximize the mutual information between the selected features and the response variable, and in (Yoon, Jordon, and van der Schaar 2019) by using an actor-critic framework to mimic a baseline while optimizing the selection. Unlike these, TabNet employs _soft feature selection with controllable sparsity in end-to-end learning_ – a single model jointly performs feature selection and output mapping, resulting in superior 

performance with compact representations. 

**Tree-based learning:** DTs are commonly-used for tabular data learning. Their prominent strength is efficient picking of global features with the most statistical information gain (Grabczewski and Jankowski 2005). To improve the performance of standard DTs, one common approach is ensembling to reduce variance. Among ensembling methods, random forests (Ho 1998) use random subsets of data with randomly selected features to grow many trees. XGBoost (Chen and Guestrin 2016) and LightGBM (Ke et al. 2017) are the two recent ensemble DT approaches that dominate most of the recent data science competitions. Our experimental results 



<!-- Start of picture text -->
!#<br>+ Softmax<br>!" < % !" > %<br>ReLU ReLU !# > & & !# > &<br>$"!" −$"% −1<br>−$"!" + $"% −1<br>−1 $#!# −$#& %<br>−1 −$#!# + $#& !"<br>FC FC<br>W : [$", - $", 0, 0] W : [0, 0, $# , - $# ] !" < %<br>b : [- a  $" , a  $" , -1, -1 ] b : [-1 , -1, -d  $# , d  $# ] !# < & !" > %<br>!# < &<br>[!"] [!#]<br>Mask Mask<br>M : [1, 0] M : [0, 1]<br>[!", !#]<br><!-- End of picture text -->

Figure 3: Illustration of DT-like classification using conventional DNN blocks (left) and the corresponding decision manifold (right). Relevant features are selected by using multiplicative sparse masks on inputs. The selected features are linearly transformed, and after a bias addition (to represent boundaries) ReLU performs region selection by zeroing the regions. Aggregation of multiple regions is based on addition. As _C_ 1 and _C_ 2 get larger, the decision boundary gets sharper. 

for various datasets show that tree-based models can be outperformed when the representation capacity is improved with deep learning while retaining their feature selecting property. **Integration of DNNs into DTs:** Representing DTs with DNN building blocks as in (Humbird, Peterson, and McClarren 2018) yields redundancy in representation and inefficient learning. Soft (neural) DTs (Wang, Aggarwal, and Liu 2017; Kontschieder et al. 2015) use differentiable decision functions, instead of non-differentiable axis-aligned splits. However, losing automatic feature selection often degrades performance. In (Yang, Morillo, and Hospedales 2018), a soft binning function is proposed to simulate DTs in DNNs, by inefficiently enumerating of all possible decisions. (Ke et al. 2019) proposes a DNN architecture by explicitly leveraging expressive feature combinations, however, learning is based on transferring knowledge from gradient-boosted DT. (Tanno et al. 2018) proposes a DNN architecture by adaptively growing from primitive blocks while representation learning into edges, routing functions and leaf nodes. TabNet differs from these as it embeds soft feature selection with controllable sparsity via sequential attention. 

**Self-supervised learning:** Unsupervised representation learning improves supervised learning especially in small data regime (Raina et al. 2007). Recent work for text (Devlin et al. 2018) and image (Trinh, Luong, and Le 2019) data has shown significant advances – driven by the judicious choice of the unsupervised learning objective (masked input prediction) and attention-based deep learning. 

## **TabNet for Tabular Learning** 

DTs are successful for learning from real-world tabular datasets. With a specific design, conventional DNN building blocks can be used to implement DT-like output manifold, e.g. see Fig. 3). In such a design, individual feature selection is key to obtain decision boundaries in hyperplane form, which can be generalized to a linear combination of features where coefficients determine the proportion of each feature. TabNet is based on such functionality and it outperforms DTs while reaping their benefits by careful design which: (i) uses sparse instance-wise feature selection learned from data; (ii) 

constructs a sequential multi-step architecture, where each step contributes to a portion of the decision based on the selected features; (iii) improves the learning capacity via nonlinear processing of the selected features; and (iv) mimics ensembling via higher dimensions and more steps. 

Fig. 4 shows the TabNet architecture for encoding tabular data. We use the raw numerical features and consider mapping of categorical features with trainable embeddings. We do not consider any global feature normalization, but merely apply batch normalization (BN). We pass the same _D_ - dimensional features **f** _∈ℜ_<sup>_B×D_</sup> to each decision step, where _B_ is the batch size. TabNet’s encoding is based on sequential multi-step processing with _Nsteps_ decision steps. The _i_<sup>_th_</sup> step inputs the processed information from the ( _i −_ 1)<sup>_th_</sup> step to decide which features to use and outputs the processed feature representation to be aggregated into the overall decision. The idea of top-down attention in the sequential form is inspired by its applications in processing visual and text data (Hudson and Manning 2018) and reinforcement learning (Mott et al. 2019) while searching for a small subset of relevant information in high dimensional input. 

**Feature selection:** We employ a learnable mask **M** [ **i** ] _∈ ℜ_<sup>_B×D_</sup> for soft selection of the salient features. Through sparse selection of the most salient features, the learning capacity of a decision step is not wasted on irrelevant ones, and thus the model becomes more parameter efficient. The masking is multiplicative, **M** [ **i** ] _·_ **f** . We use an attentive transformer (see Fig. 4) to obtain the masks using the processed features from the preceding step, **a** [ **i** _−_ **1** ]: **M** [ **i** ] = sparsemax( **P** [ **i** _−_ **1** ] _·_ h _i_ ( **a** [ **i** _−_ **1** ])) _._ Sparsemax normalization (Martins and Astudillo 2016) encourages sparsity by mapping the Euclidean projection onto the probabilistic simplex, which is observed to be superior in performance and aligned with the goal of sparse feature selection for explainability. Note that<sup>�</sup><sup>_D_</sup> _j_ =1<sup>**M**[</sup><sup>**i**]</sup><sup>**b**</sup><sup>_,_</sup><sup>**j**=1. h</sup><sup>_i_is a trainable func-</sup> tion, shown in Fig. 4 using a FC layer, followed by BN. **P** [ **i** ] is the prior scale term, denoting how much a particular feature has been used previously: **P** [ **i** ] =<sup>�</sup><sup>_i_</sup> _j_ =1<sup>(</sup><sup>_γ −_</sup><sup>**M**[</sup><sup>**j**])</sup><sup>_,_where</sup><sup>_γ_</sup> is a relaxation parameter – when _γ_ = 1, a feature is enforced 



<!-- Start of picture text -->
Step 1 Step 2<br>+ … FC Output<br>ReLU ReLU<br>Split Split Split<br>Feature  Feature  Feature  Encoded representation<br>transformer transformer transformer …<br>…<br>transformerAttentive  Mask transformerAttentive  Mask Step 1 Step 2<br>Feature  Feature<br>BN transfor me r transformer …<br>Agg. Agg.<br>Features FC FC<br>+ … attributesFeature + … Reconstructed features<br>(a) TabNet encoder architecture (b) TabNet decoder architecture<br>Feature<br>transformer Attentive<br>transformer<br>Shared a cr os s d ecision steps D ec isi on  step dep en dent Prior scales<br>0.5 0.5 0.5<br>(c) (d)<br>+ +<br>FC BN GLU FC BN GLU + FC BN GLU + FC BN GLU +<br>FC BN<br>Sparsemax<br>+<br>+<br><!-- End of picture text -->

Figure 4: (a) TabNet encoder, composed of a feature transformer, an attentive transformer and feature masking. A split block divides the processed representation to be used by the attentive transformer of the subsequent step as well as for the overall output. For each step, the fe ~~ature~~ selection mask provides interpretable information about the model’s functionality, and the masks can be aggregated to obtain global feature important attribution. (b) TabNet decoder, composed of a feature transformer block at each step. (c) A feature transformer block example – 4-layer network is shown, where 2 are shared across all decision steps and 2 are decision step-dependent. Each <mark>layer is co</mark> ~~<mark>m</mark> po~~ sed of a fully-connected (FC) layer, BN and GLU nonlinearity. (d) An attentive transformer block example – a single layer mapping is modulated with a prior scale information which aggregates how much each feature has been used before the current decision step. sparsemax (Martins and Astudillo 2016) is used for normalization of the coefficients, resulting i ~~n~~ sp ~~ar~~ se ~~se~~ lec ~~tion~~ of the salient features. 

to be used only at one decision step and as _γ_ increases, more flexibility is provided to use a feature at multiple decision steps. **P** [ **0** ] is initialized as all ones, **1**<sup>_B×D_</sup> , without any prior on the masked features. If some features are unused (as in selfsupervised learning), corresponding **P** [ **0** ] entries are made 0 to help model’s learning. To further control the sparsity of the selected features, we propose sparsity regularization in the form of entropy (Grandvalet and Bengio 2004), _Lsparse_ = _−_ **Mb** _<u>,</u>_ **<u>j</u>** <u>[</u> **i** <u>] log(</u> **Mb** _<u>,</u>_ **<u>j</u>** <u>[</u> **i** <u>]+</u> _ϵ_ <u>)</u> � _Ni_ =1 _steps_ � _Bb_ =1 � _Dj_ =1 _Nsteps·B ,_ where _ϵ_ is a small number for numerical stability. We add the sparsity regularization to the overall loss, with a coefficient _λsparse_ . Sparsity provides a favorable inductive bias for datasets where most features are redundant. 

**Feature processing:** We process the filtered features using a feature transformer (see Fig. 4) and then split for the decision step output and information for the subsequent step, [ **d** [ **i** ] _,_ **a** [ **i** ]] = f _i_ ( **M** [ **i** ] _·_ **f** ), where **d** [ **i** ] _∈ℜ_<sup>_B×Nd_</sup> and **a** [ **i** ] _∈ℜ_<sup>_B×Na_</sup> . For parameter-efficient and robust learning with high capacity, a feature transformer should comprise layers that are shared across all decision steps (as the same features are input across different decision steps), as well as decision step-dependent layers. Fig. 4 shows the implementation as concatenation of two shared layers and two decision step-dependent layers. Each FC layer is followed by BN and gated linear unit (GLU) nonlinearity (Dauphin et al. 2016), eventually connected to a normalized residual connection with normalization. Normalization with _√_ 0 _._ 5 helps to stabilize learning by ensuring that the variance throughout the network does not change dramatically (Gehring et al. 2017). For faster training, we use large batch sizes with BN. Thus, except the one applied to the input features, we use ghost BN (Hoffer, Hubara, and Soudry 2017) form, using a virtual batch size _BV_ and momentum _mB_ . For the input features, we observe the benefit of low-variance averaging and hence avoid ghost BN. Finally, inspired by decision-tree like aggregation as in Fig. 3, we construct the overall decision embedding 

as **dout** =<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_steps_</sup> ReLU( **d** [ **i** ]). We apply a linear mapping **Wfinaldout** to get the output mapping.<sup>1</sup> 

**Interpretability:** TabNet’s feature selection masks can shed light on the selected features at each step. If **Mb** _,_ **j** [ **i** ] = 0, then _j_<sup>_th_</sup> feature of the _b_<sup>_th_</sup> sample should have no contribution to the decision. If f _i_ were a linear function, the coefficient **Mb** _,_ **j** [ **i** ] would correspond to the feature importance of **fb** _,_ **j** . Although each decision step employs non-linear processing, their outputs are combined later in a linear way. We aim to quantify an aggregate feature importance in addition to analysis of each step. Combining the masks at different steps requires a coefficient that can weigh the relative importance of each step in the decision. We simply propose _η_ **b** [ **i** ] = � _Nc_ =1 _d_<sup>ReLU(</sup><sup>**db**</sup><sup>_,_</sup><sup>**c**[</sup><sup>**i**]) to denote the aggregate decision con-</sup> tribution at _i_<sup>_th_</sup> decision step for the _b_<sup>_th_</sup> sample. Intuitively, if **db** _,_ **c** [ **i** ] _<_ 0, then all features at _i_<sup>_th_</sup> decision step should have 0 contribution to the overall decision. As its value increases, it plays a higher role in the overall linear combination. Scaling the decision mask at each decision step with _η_ **b** [ **i** ], we 

1For discrete outputs, we additionally employ softmax during training (and argmax during inference). 

propose the aggregate feature importance mask, **Magg** _−_ **b** _,_ **j** = � _Ni_ =1 _stepsη_ **b** [ **i** ] **Mb** _,_ **j** [ **i** ]�� _jD_ =1� _Ni_ =1 _stepsη_ **b** [ **i** ] **Mb** _,_ **j** [ **i** ] _._<sup>2</sup> 

**Tabular self-supervised learning:** We propose a decoder architecture to reconstruct tabular features from the TabNet encoded representations. The decoder is composed of feature transformers, followed by FC layers at each decision step. The outputs are summed to obtain the reconstructed features. We propose the task of prediction of missing feature columns from the others. Consider a binary mask **S** _∈{_ 0 _,_ 1 _}_<sup>_B×D_</sup> . The TabNet encoder inputs ( **1** _−_ **S** ) _·_<sup>**ˆ**</sup> **f** and the decoder outputs the reconstructed features, **S** _·_<sup>**ˆ**</sup> **f** . We initialize **P** [ **0** ] = ( **1** _−_ **S** ) in encoder so that the model emphasizes merely on the known features, and the decoder’s last FC layer is multiplied with **S** to output the unknown features. We consider the reconstruction loss in self-supervised phase: 



with the population standard deviation of the ground truth is beneficial, as the features may have different ranges. We sample **Sb** _,_ **j** independently from a Bernoulli distribution with parameter _ps_ , at each iteration. 

## **Experiments** 

We study TabNet in wide range of problems, that contain regression or classification tasks, _particularly with published benchmarks_ . For all datasets, categorical inputs are mapped to a single-dimensional trainable scalar with a learnable embedding<sup>3</sup> and numerical columns are input without and preprocessing.<sup>4</sup> We use standard classification (softmax cross entropy) and regression (mean squared error) loss functions and we train until convergence. Hyperparameters of the TabNet models are optimized on a validation set and listed in Appendix. TabNet performance is not very sensitive to most hyperparameters as shown with ablation studies in Appendix. In Appendix, we also present ablation studies on various design and guidelines on selection of the key hyperparameters. For all experiments we cite, we use the same training, validation and testing data split with the original work. Adam optimization algorithm (Kingma and Ba 2014) and Glorot uniform initialization are used for training of all models.<sup>5</sup> 

### **Instance-wise feature selection** 

Selection of the salient features is crucial for high performance, especially for small datasets. We consider 6 tabular datasets from (Chen et al. 2018) (consisting 10k training samples). The datasets are constructed in such a way that only a subset of the features determine the output. For Syn1Syn3, salient features are same for all instances (e.g., the 

2Normalization is used to ensure<sup>�</sup> _Dj_ =1<sup>**Magg**</sup><sup>_−_</sup><sup>**b**</sup><sup>_,_</sup><sup>**j**= 1.</sup> 

3In some cases, higher dimensional embeddings may slightly improve the performance, but interpretation of individual dimensions may become challenging. 

4Specially-designed feature engineering, e.g. logarithmic transformation of variables highly-skewed distributions, may further improve the results but we leave it out of the scope of this paper. 

5An open-source implementation will be released. 

Table 1: Mean and std. of test area under the receiving operating characteristic curve (AUC) on 6 synthetic datasets from (Chen et al. 2018), for TabNet vs. other feature selection-based DNN models: No sel.: using all features without any feature selection, Global: using only globally-salient features, Tree Ensembles (Geurts, Ernst, and Wehenkel 2006), Lasso-regularized model, L2X (Chen et al. 2018) and INVASE (Yoon, Jordon, and van der Schaar 2019). Bold numbers denote the best for each dataset. 

|_Mdl_|||_Test_|_AUC_|||
|---|---|---|---|---|---|---|
|_oe_|Syn1|Syn2|Syn3|Syn4|Syn5|Syn6|
|No selection|.578_±_.004|.789_±_.003|.854_±_.004|.558_±_.021|.662_±_.013|.692_±_.015|
|Tree|.574_±_.101|.872_±_.003|.899_±_.001|.684_±_.017|.741_±_.004|.771_±_.031|
|Lasso-regularized|.498_±_.006|.555_±_.061|.886_±_.003|.512_±_.031|.691_±_.024|.727_±_.025|
|L2X|.498_±_.005|.823_±_.029|.862_±_.009|.678_±_.024|.709_±_.008|.827_±_.017|
|INVASE|**.690**_±_**.006**|.877_±_.003|**.902**_±_**.003**|**.787**_±_**.004**|.784_±_.005|.877_±_.003|
|Global|.686_±_.005|.873_±_.003|.900_±_.003|.774_±_.006|.784_±_.005|.858_±_.004|
|_TabNet_|.682_±_.005|**.892**_±_**.004**|.897_±_.003|.776_±_.017|**.789**_±_**.009**|**.878**_±_**.004**|



output of Syn2 depends on features _X_ 3- _X_ 6), and global feature selection, as if the salient features were known, would give high performance. For Syn4-Syn6, salient features are instance dependent (e.g., for Syn4, the output depends on either _X_ 1- _X_ 2 or _X_ 3- _X_ 6 depending on the value of _X_ 11), which makes global feature selection suboptimal. Table 1 shows that TabNet outperforms others (Tree Ensembles (Geurts, Ernst, and Wehenkel 2006), LASSO regularization, L2X (Chen et al. 2018)) and is on par with INVASE (Yoon, Jordon, and van der Schaar 2019). For Syn1-Syn3, TabNet performance is close to global feature selection - _it can figure out what features are globally important_ . For Syn4-Syn6, eliminating instance-wise redundant features, TabNet improves global feature selection. All other methods utilize a predictive model with 43k parameters, and the total number of parameters is 101k for INVASE due to the two other models in the actorcritic framework. TabNet is a single architecture, and its size is 26k for Syn1-Syn3 and 31k for Syn4-Syn6. The compact representation is one of TabNet’s valuable properties. 

### **Performance on real-world datasets** 

Table 2: Performance for Forest Cover Type dataset. 

|_Model_|_Test accuracy (%)_|
|---|---|
|XGBoost|89.34|
|LightGBM|89.28|
|CatBoost|85.14|
|AutoML Tables|94.95|
|_TabNet_|**96.99**|



**Forest Cover Type (Dua and Graff 2017):** The task is classification of forest cover type from cartographic variables. Table 2 shows that TabNet outperforms ensemble tree based approaches that are known to achieve solid performance (Mitchell et al. 2018). We also consider AutoML Tables (AutoML 2019), an automated search framework based on ensemble of models including DNN, gradient boosted DT, AdaNet (Cortes et al. 2016) and ensembles (AutoML 2019) with very thorough hyperparameter search. A single TabNet without fine-grained hyperparameter search outperforms it. 

Table 3: Performance for Poker Hand induction dataset. 

|_Model_|_Test accuracy (%)_|
|---|---|
|DT|50.0|
|MLP|50.0|
|Deepneural DT|65.1|
|XGBoost|71.1|
|LightGBM|70.0|
|CatBoost|66.6|
|_TabNet_|**99.2**|
|Rule-based|100.0|



**Poker Hand (Dua and Graff 2017):** The task is classification of the poker hand from the raw suit and rank attributes of the cards. The input-output relationship is deterministic and hand-crafted rules can get 100% accuracy. Yet, conventional DNNs, DTs, and even their hybrid variant of deep neural DTs (Yang, Morillo, and Hospedales 2018) severely suffer from the imbalanced data and cannot learn the required sorting and ranking operations (Yang, Morillo, and Hospedales 2018). Tuned XGBoost, CatBoost, and LightGBM show very slight improvements over them. TabNet outperforms other methods, as it can perform highly-nonlinear processing with its depth, without overfitting thanks to instance-wise feature selection. 

Table 4: Performance on Sarcos dataset. Three TabNet models of different sizes are considered. 

|_Model_|_Test MSE_|_Model size_|
|---|---|---|
|Random forest|2.39|16.7K|
|Stochastic DT|2.11|28K|
|MLP|2.13|0.14M|
|Adaptive neural tree|1.23|0.60M|
|Gradient boosted tree|1.44|0.99M|
|_TabNet-S_|**1.25**|**6.3K**|
|_TabNet-M_|**0.28**|**0.59M**|
|_TabNet-L_|**0.14**|**1.75M**|



**Sarcos (Vijayakumar and Schaal 2000):** The task is regressing inverse dynamics of an anthropomorphic robot arm. 

(Tanno et al. 2018) shows that decent performance with a very small model is possible with a random forest. In the very small model size regime, TabNet’s performance is on par with the best model from (Tanno et al. 2018) with 100x more parameters. When the model size is not constrained, TabNet achieves almost an order of magnitude lower test MSE. 

Table 5: Performance on Higgs Boson dataset. Two TabNet models are denoted with -S and -M. 

|_Model_|_Test acc._ (%)|_Model size_|
|---|---|---|
|Sparse evolutionaryMLP|**78.47**|**81K**|
|Gradient boosted tree-S|74.22|0.12M|
|Gradient boosted tree-M|75.97|0.69M|
|MLP|78.44|2.04M|
|Gradient boosted tree-L|76.98|6.96M|
|_TabNet-S_|78.25|81K|
|_TabNet-M_|**78.84**|**0.66M**|



**Higgs Boson (Dua and Graff 2017):** The task is distinguishing between a Higgs bosons process vs. background. Due to its much larger size (10.5M instances), DNNs outperform DT variants even with very large ensembles. TabNet outperforms MLPs with more compact representations. We also compare to the state-of-the-art evolutionary sparsification algorithm (Mocanu et al. 2018) that integrates non-structured sparsity into training. With its compact representation, TabNet yields almost similar performance to sparse evolutionary training for the same number of parameters. Unlike sparse evolutionary training, the sparsity of TabNet is structured – it does not degrade the operational intensity (Wen et al. 2016) and can efficiently utilize modern multi-core processors. 

Table 6: Performance for Rossmann Store Sales dataset. 

|_Model_|_Test MSE_|
|---|---|
|MLP|512.62|
|XGBoost|490.83|
|LightGBM|504.76|
|CatBoost|489.75|
|_TabNet_|**485.12**|



**Rossmann Store Sales (Kaggle 2019b):** The task is forecasting the store sales from static and time-varying features. We observe that TabNet outperforms commonly-used methods. The time features (e.g. day) obtain high importance, and the benefit of instance-wise feature selection is observed for cases like holidays where the sales dynamics are different. 

### **Interpretability** 

**Synthetic datasets:** Fig. 5 shows the aggregate feature importance masks for the synthetic datasets from Table 1.<sup>6</sup> The output on Syn2 only depends on _X_ 3- _X_ 6 and we observe that 

6For better illustration here, the models are trained with 10M samples rather than 10K as we obtain sharper selection masks. 

the aggregate masks are almost all zero for irrelevant features and TabNet merely focuses on the relevant ones. For Syn4, the output depends on either _X_ 1- _X_ 2 or _X_ 3- _X_ 6 depending on the value of _X_ 11. TabNet yields accurate instance-wise feature selection – it allocates a mask to focus on the indicator _X_ 11, and assigns almost all-zero weights to irrelevant features (the ones other than two feature groups). 

**Real-world datasets:** We first consider the simple task of mushroom edibility prediction (Dua and Graff 2017). TabNet achieves 100% test accuracy on this dataset. It is indeed known (Dua and Graff 2017) that “Odor” is the most discriminative feature – with “Odor” only, a model can get _>_ 98 _._ 5% test accuracy (Dua and Graff 2017). Thus, a high feature importance is expected for it. TabNet assigns an importance score ratio of 43% for it, while other methods like LIME (Ribeiro, Singh, and Guestrin 2016), Integrated Gradients (Sundararajan, Taly, and Yan 2017) and DeepLift (Shrikumar, Greenside, and Kundaje 2017) assign less than 30% (Ibrahim et al. 2019). Next, we consider Adult Census Income. TabNet yields feature importance rankings consistent with the wellknown (Lundberg, Erion, and Lee 2018; Nbviewer 2019) (see Appendix) For the same problem, Fig. 6 shows the clear separation between age groups, as suggested by “Age” being the most important feature by TabNet. 

### **Self-supervised learning** 

Table 7: Mean and std. of accuracy (over 15 runs) on Higgs with Tabnet-M model, varying the size of the training dataset for supervised fine-tuning. 

|_Training_|_Test acc_|_uracy_ (%)|
|---|---|---|
|_dataset size_|_Supervised_|_Withpre-training_|
|1k|57.47_±_1.78|**61.37**_±_**0.88**|
|10k|66.66_±_0.88|**68.06**_±_**0.39**|
|100k|72.92_±_0.21|**73.19**_±_**0.15**|



Table 7 shows that unsupervised pre-training significantly improves performance on the supervised classification task, especially in the regime where the unlabeled dataset is much larger than the labeled dataset. As exemplified in Fig. 7 the model convergence is much faster with unsupervised pretraining. Very fast convergence can be useful for continual learning and domain adaptation. 

## **Conclusions** 

We have proposed TabNet, a novel deep learning architecture for tabular learning. TabNet uses a sequential attention mechanism to choose a subset of semantically meaningful features to process at each decision step. Instance-wise feature selection enables efficient learning as the model capacity is fully used for the most salient features, and also yields more interpretable decision making via visualization of selection masks. We demonstrate that TabNet outperforms previous work across tabular datasets from different domains. Lastly, we demonstrate significant benefits of unsupervised pre-training for fast adaptation and improved performance. 



<!-- Start of picture text -->
Syn2 dataset<br>Magg M[1] M[2] M[3] M[4]<br>X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11<br>/<br>Syn4 dataset<br>Magg M[1] M[2] M[3] M[4] M[5]<br>Test samples<br><!-- End of picture text -->

Figure 5: Feature importance masks **M** [ **i** ] (that indicate feature selection at _i_<sup>_th_</sup> step) and the aggregate feature importance mask **Magg** showing the global instance-wise feature selection, on Syn2 and Syn4 (Chen et al. 2018). Brighter colors show a higher value. E.g. for Syn2, only _X_ 3- _X_ 6 are used. 



Figure 6: First two dimensions of the T-SNE of the decision manifold for Adult and the impact of the top feature ‘Age’. 



Figure 7: Training curves on Higgs dataset with 10k samples. 

## **Acknowledgements** 

Discussions with Jinsung Yoon, Kihyuk Sohn, Long T. Le, Ariel Kleiner, Zizhao Zhang, Andrei Kouznetsov, Chen Xing, Ryan Takasugi and Andrew Moore are gratefully acknowledged. 

## **Performance on KDD datasets** 

Table 8: Performance on KDD datasets. 

|_Mdl_||_Test acc_|_uracy (%)_||
|---|---|---|---|---|
|_oe_|_Appetency_|_Churn_|_Upselling_|_Census_|
|XGBoost|**98.2**|92.7|**95.1**|**95.8**|
|CatBoost|**98.2**|**92.8**|**95.1**|95.7|
|_TabNet_|**98.2**|92.7|95.0|95.5|



Appetency, Churn and Upselling datasets are classification tasks for customer relationship management, and KDD Census Income (Dua and Graff 2017) dataset is for income prediction from demographic and employment related variables. These datasets show saturated behavior in performance (even simple models yield similar results). Table 8 shows that TabNet achieves very similar or slightly worse performance than XGBoost and CatBoost, that are known to be robust as they contain high amount of ensembles. 

## **Comparison of feature importance ranking of TabNet** 

Table 9: Importance ranking of features for Adult Census Income. TabNet yields feature importance rankings consistent with the well-known methods. 

|_Feature_|_SHAP_|_Skater_|_XGBoost_|_TabNet_|
|---|---|---|---|---|
|Age|1|1|1|1|
|Capitalgain|3|3|4|6|
|Capital loss|9|9|6|4|
|Education|5|2|3|2|
|Gender|8|10|12|8|
|Hoursper week|7|7|2|7|
|Marital status|2|8|10|9|
|Native country|11|11|9|12|
|Occupation|6|5|5|3|
|Race|12|12|11|11|
|Relationship|4|4|8|5|
|Work class|10|8|7|10|



We observe the commonality of the most important features (“Age”, “Capital gain/loss”, “Education number”, “Relationship”) and the least important features (“Native country”, “Race”, “Gender”, “Work class”). 

## **Self-supervised learning on Forest Cover Type** 

## **Experiment hyperparameters** 

For all datasets, we use a pre-defined hyperparameter search space. _Nd_ and _Na_ are chosen from _{_ 8 _,_ 16 _,_ 24 _,_ 32 _,_ 64 _,_ 128 _}_ , 

Table 10: Self-supervised tabular learning results. Mean and std. of accuracy (over 15 runs) on Forest Cover Type, varying the size of the training dataset for supervised fine-tuning. 

|_Training_|_Test acc_|_uracy_ (%)|
|---|---|---|
|_dataset size_|_Supervised_|_Withpre-training_|
|1k|65.91_±_1.02|**67.86**_±_**0.63**|
|10k|78.85_±_1.24|**79.22**_±_**0.78**|



_Nsteps_ is chosen from _{_ 3 _,_ 4 _,_ 5 _,_ 6 _,_ 7 _,_ 8 _,_ 9 _,_ 10 _}_ , _γ_ is chosen from _{_ 1 _._ 0 _,_ 1 _._ 2 _,_ 1 _._ 5 _,_ 2 _._ 0 _}_ , _λsparse_ is chosen from _{_ 0 _,_ 0 _._ 000001 _,_ 0 _._ 0001 _,_ 0 _._ 001 _,_ 0 _._ 01 _,_ 0 _._ 1 _}_ , _B_ is chosen from _{_ 256 _,_ 512 _,_ 1024 _,_ 2048 _,_ 4096 _,_ 8192 _,_ 16384 _,_ 32768 _}_ , _BV_ is chosen from _{_ 256 _,_ 512 _,_ 1024 _,_ 2048 _,_ 4096 _}_ , the learning rate is chosen from _{_ 0 _._ 005 _,_ 0 _._ 01 _._ 0 _._ 02 _,_ 0 _._ 025 _}_ , the decay rate is chosen from _{_ 0 _._ 4 _,_ 0 _._ 8 _,_ 0 _._ 9 _,_ 0 _._ 95 _}_ and the decay iterations is chosen from _{_ 0 _._ 5 _k,_ 2 _k,_ 8 _k,_ 10 _k,_ 20 _k}_ , and _mB_ is chosen from _{_ 0 _._ 6 _,_ 0 _._ 7 _,_ 0 _._ 8 _,_ 0 _._ 9 _,_ 0 _._ 95 _,_ 0 _._ 98 _}_ . If the model size is not under the desired cutoff, we decrease the value to satisfy the size constraint. For all the comparison models, we run a hyperparameter tuning with the same number of search steps. **Synthetic:** All TabNet models use _Nd_ = _Na_ =16, _B_ =3000, _BV_ =100, _mB_ =0 _._ 7. For Syn1 we use _λsparse_ =0 _._ 02, _Nsteps_ =4 and _γ_ =2 _._ 0; for Syn2 and Syn3 we use _λsparse_ =0 _._ 01, _Nsteps_ =4 and _γ_ =2 _._ 0; and for Syn4, Syn5 and Syn6 we use _λsparse_ =0 _._ 005, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. All models use Adam with a learning rate of 0.02 (decayed 0.7 every 200 iterations with an exponential decay) for 4k iterations. For visualizations, we also train TabNet models with datasets of size 10M samples. For this case, we choose _Nd_ = _Na_ = 32, _λsparse_ =0 _._ 001, _B_ =10000, _BV_ =100, _mB_ =0 _._ 9. Adam is used with a learning rate of 0.02 (decayed 0.9 every 2k iterations with an exponential decay) for 15k iterations. For Syn2 and Syn3, _Nsteps_ =4 and _γ_ =2. For Syn4 and Syn6, _Nsteps_ =5 and _γ_ =1 _._ 5. 

**Forest Cover Type:** The dataset partition details, and the hyperparameters of XGBoost, LigthGBM, and CatBoost are from (Mitchell et al. 2018). We re-optimize AutoInt hyperparameters. TabNet model uses _Nd_ = _Na_ =64, _λsparse_ =0 _._ 0001, _B_ =16384, _BV_ =512, _mB_ =0 _._ 7, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision stepdependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.02 (decayed 0.95 every 0.5k iterations with an exponential decay) for 130k iterations. For unsupervised pre-training, the decoder model uses _Nd_ = _Na_ =64, _B_ =16384, _BV_ =512, _mB_ =0 _._ 7, and _Nsteps_ =10. For supervised fine-tuning, we use the batch size _B_ = _BV_ as the training datasets are small. 

**Poker Hands:** We split 6k samples for validation from the training dataset, and after optimization of the hyperparameters, we retrain with the entire training dataset. DT, MLP and deep neural DT models follow the same hyperparameters with (Yang, Morillo, and Hospedales 2018). We tune the hyperparameters of XGBoost, LigthGBM, and CatBoost. TabNet uses _Nd_ = _Na_ =16, _λsparse_ =0 _._ 000001, _B_ =4096, _BV_ =1024, _mB_ = 0 _._ 95, _Nsteps_ =4 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision step- 

dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.01 (decayed 0.95 every 500 iterations with an exponential decay) for 50k iterations. **Sarcos:** We split 4.5k samples for validation from the training dataset, and after optimization of the hyperparameters, we retrain with the entire training dataset. All comparison models follow the hyperparameters from (Tanno et al. 2018). TabNet-S model uses _Nd_ = _Na_ =8, _λsparse_ =0 _._ 0001, _B_ =4096, _BV_ =256, _mB_ =0 _._ 9, _Nsteps_ =3 and _γ_ =1 _._ 2. Each feature transformer block uses one shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.01 (decayed 0.95 every 8k iterations with an exponential decay) for 600k iterations. TabNet-M model uses _Nd_ = _Na_ =64, _λsparse_ =0 _._ 0001, _B_ =4096, _BV_ =128, _mB_ =0 _._ 8, _Nsteps_ =7 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision stepdependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.01 (decayed 0.95 every 8k iterations with an exponential decay) for 600k iterations. The TabNet-L model uses _Nd_ = _Na_ =128, _λsparse_ =0 _._ 0001, _B_ =4096, _BV_ =128, _mB_ =0 _._ 8, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision stepdependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.02 (decayed 0.9 every 8k iterations with an exponential decay) for 600k iterations. **Higgs:** We split 500k samples for validation from the training dataset, and after optimization of the hyperparameters, we retrain with the entire training dataset. MLP models are from (Mocanu et al. 2018). For gradient boosted trees (Tensorflow 2019), we tune the learning rate and depth – the gradient boosted tree-S, -M, and -L models use 50, 300 and 3000 trees respectively. TabNet-S model uses _Nd_ =24, _Na_ =26, _λsparse_ =0 _._ 000001, _B_ =16384, _BV_ =512, _mB_ =0 _._ 6, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.02 (decayed 0.9 every 20k iterations with an exponential decay) for 870k iterations. TabNet-M model uses _Nd_ =96, _Na_ =32, _λsparse_ =0 _._ 000001, _B_ =8192, _BV_ =256, _mB_ =0 _._ 9, _Nsteps_ =8 and _γ_ =2 _._ 0. Feature transformers use two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.025 (decayed 0.9 every 10k iterations with an exponential decay) for 370k iterations. For unsupervised pre-training, the decoder model uses _Nd_ = _Na_ =128, _B_ =8192, _BV_ =256, _mB_ =0 _._ 9, and _Nsteps_ =20. For supervised fine-tuning, we use the batch size _B_ = _BV_ as the training datasets are small. 

**Rossmann:** We use the same preprocessing and data split with (Catboost 2019) – data from 2014 is used for training and validation, whereas 2015 is used for testing. We split 100k samples for validation from the training dataset, and after optimization of the hyperparameters, we retrain with the entire training dataset. The performance of the comparison models are from (Catboost 2019). Obtained with hyperparameter tuning, the MLP is composed of 5 layers of FC (with a hidden unit size of 128), followed by BN and ReLU nonlinearity, trained with a batch size of 512 and a learning rate of 0.001. TabNet model uses _Nd_ = _Na_ =32, _λsparse_ =0 _._ 001, _B_ =4096, _BV_ =512, _mB_ =0 _._ 8, _Nsteps_ =5 and _γ_ =1 _._ 2. Feature trans- 

formers use two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.002 (decayed 0.95 every 2000 iterations with an exponential decay) for 15k iterations. 

**KDD:** For Appetency, Churn and Upselling datasets, we apply the similar preprocessing and split as (Prokhorenkova et al. 2018). The performance of the comparison models are from (Prokhorenkova et al. 2018). TabNet models use _Nd_ = _Na_ =32, _λsparse_ =0 _._ 001, _B_ =8192, _BV_ =256, _mB_ =0 _._ 9, _Nsteps_ =7 and _γ_ =1 _._ 2. Each feature transformer block uses two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.01 (decayed 0.9 every 1000 iterations with an exponential decay) for 10k iterations. For Census Income, the dataset and comparison model specifications follow (Oza 2005). TabNet model uses _Nd_ = _Na_ =48, _λsparse_ =0 _._ 001, _B_ =8192, _BV_ =256, _mB_ =0 _._ 9, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision stepdependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.02 (decayed 0.7 every 2000 iterations with an exponential decay) for 4k iterations. 

**Mushroom edibility:** TabNet model uses _Nd_ = _Na_ =8, _λsparse_ =0 _._ 001, _B_ =2048, _BV_ =128, _mB_ =0 _._ 9, _Nsteps_ =3 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision step-dependent FC layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.01 (decayed 0.8 every 400 iterations with an exponential decay) for 10k iterations. **Adult Census Income:** TabNet model uses _Nd_ = _Na_ =16, _λsparse_ = 0 _._ 0001, _B_ =4096, _BV_ =128, _mB_ =0 _._ 98, _Nsteps_ =5 and _γ_ =1 _._ 5. Feature transformers use two shared and two decision step-dependent layer, ghost BN and GLU blocks. Adam is used with a learning rate of 0.02 (decayed 0.4 every 2.5k iterations with an exponential decay) for 7.7k iterations. 85.7% test accuracy is achieved. 

## **Ablation studies** 

Table 11 shows the impact of ablation cases. For all cases, the number of iterations is optimized on the validation set. Obtaining high performance necessitates appropriatelyadjusted model capacity based on the characteristics of the dataset. Decreasing the number of units _Nd_ , _Na_ or the number of decision steps _Nsteps_ are efficient ways of gradually decreasing the capacity without significant degradation in performance. On the other hand, increasing these parameters beyond some value causes optimization issues and do not yield performance benefits. Replacing the feature transformer block with a simpler alternative, such as a single shared layer, can still give strong performance while yielding a very compact model architecture. This shows the importance of the inductive bias introduced with feature selection and sequential attention. To push the performance, increasing the depth of the feature transformer is an effective approach. While increasing the depth, parameter sharing between feature transformer blocks across decision steps is an efficient way to decrease model size without degradation in performance. We indeed observe the benefit of partial parameter sharing, compared to fully decision step-dependent blocks or fully shared blocks. We also observe the empirical benefit of GLU, compared to conventional nonlinearities like ReLU. 

Table 11: Ablation studies for the TabNet encoder model for the forest cover type dataset. 

|_Ablation cases_|_Test_<br>_accuracy %_<br>(difference)|_Model_<br>_size_|
|---|---|---|
|Base (_Nd_ =_Na_ = 64,_γ_ = 1_._5,_Nsteps_ = 5,_λsparse_ = 0_._0001, feature<br>transformer block composed of two shared and two decision<br>step-dependent layers,_B_ = 16384)|96.99<br>|470k|
|Decreasing capacity via number of units (with_Nd_ =_Na_ = 32)|94.99<br>(-2.00)|129k|
|Decreasing capacity via number of decision steps (with_Nsteps_ = 3)|96.22<br>(-0.77)|328k|
|Increasing capacity via number of decision steps (with_Nsteps_ = 9)|95.48<br>(-1.51)|755k|
|Decreasing capacity via all-shared feature transformer blocks|96.74<br>(-0.25)|143k|
|Increasing capacity via decision step-dependent feature transformer<br>blocks|96.76<br>(-0.23)|703k|
|Feature transformer block as a single shared layer|95.32<br>(-1.67)|35k|
|Feature transformer block as a single shared layer, with ReLU instead of<br>GLU|93.92<br>(-3.07)|27k|
|Feature transformer block as two shared layers|96.34<br>(-0.66)|71k|
|Feature transformer block as two shared layers and 1 decision<br>step-dependent layer|96.54<br>(-0.45)|271k|
|Feature transformer block as a single decision-step dependent layer|94.71<br>(-0.28)|105k|
|Feature transformer block as a single decision-step dependent layer,<br>with_Nd_=_Na_=128|96.24<br>(-0.75)|208k|
|Feature transformer block as a single decision-step dependent layer,<br>with_Nd_=_Na_=128and replacingGLU with ReLU|95.67<br>(-1.32)|139k|
|Feature transformer block as a single decision-step dependent layer,<br>with_Nd_=_Na_=256and replacingGLU with ReLU|96.41<br>(-0.58)|278k|
|Reducing the impact of prior scale (with_γ_ = 3_._0)|96.49<br>(-0.50)|470k|
|Increasing the impact of prior scale (with_γ_ = 1_._0)|96.67<br>(-0.32)|470k|
|No sparsity regularization (with_λsparse_ = 0)|96.50<br>(-0.49)|470k|
|High sparsity regularization (with_λsparse_ = 0_._01)|93.87<br>(-3.12)|470k|
|Small batch size (_B_ = 4096)|96.42<br>(-0.57)|470k|



The strength of sparse feature selection depends on the two parameters we introduce: _γ_ and _λsparse_ . We show that optimal choice of these two is important for performance. A _γ_ close to 1, or a high _λsparse_ may yield too tight constraints on the strength of sparsity and may hurt performance. On the other hand, there is still the benefit of a sufficient low _γ_ and sufficiently high _λsparse_ , to aid learning of the model via a favorable inductive bias. 

Lastly, given the fixed model architecture, we show the benefit of large-batch training, enabled by ghost BN (Hoffer, Hubara, and Soudry 2017). The optimal batch size for TabNet seems considerably higher than the conventional batch sizes used for other data types, such as images or speech. 

## **Guidelines for hyperparameters** 

We consider datasets ranging from _∼_ 10K to _∼_ 10M samples, with varying degrees of fitting difficulty. TabNet obtains high performance on all with a few general principles on hyperparameters: 

- For most datasets, _Nsteps ∈_ [3 _,_ 10] is optimal. Typically, when there are more information-bearing features, the optimal value of _Nsteps_ tends to be higher. On the other hand, increasing it beyond some value may adversely affect training dynamics as some paths in the network becomes deeper and there are more potentially-problematic ill-conditioned matrices. A very high value of _Nsteps_ may suffer from overfitting and yield poor generalization. 

- Adjustment of _Nd_ and _Na_ is an efficient way of obtaining a trade-off between performance and complexity. _Nd_ = _Na_ is a reasonable choice for most datasets. A very high value of _Nd_ and _Na_ may suffer from overfitting and yield poor generalization. 

- An optimal choice of _γ_ can have a major role on the performance. Typically a larger _Nsteps_ value favors for a larger _γ_ . 

- A large batch size is beneficial – if the memory constraints permit, as large as 1-10 % of the total training dataset size can help performance. The virtual batch size is typically much smaller. 

- Initially large learning rate is important, which should be gradually decayed until convergence. 

## **References** 

Amodei, D.; Anubhai, R.; Battenberg, E.; Case, C.; Casper, J.; et al. 2015. Deep Speech 2: End-to-End Speech Recognition in English and Mandarin. _arXiv:1512.02595_ . 

AutoML. 2019. AutoML Tables – Google Cloud. URL https://cloud.google.com/automl-tables/. 

Catboost. 2019. Benchmarks. https://github.com/catboost/ benchmarks. Accessed: 2019-11-10. 

Chen, J.; Song, L.; Wainwright, M. J.; and Jordan, M. I. 2018. Learning to Explain: An Information-Theoretic Perspective on Model Interpretation. _arXiv:1802.07814_ . 

Chen, T.; and Guestrin, C. 2016. XGBoost: A Scalable Tree Boosting System. In _KDD_ . 

Chui, M.; Manyika, J.; Miremadi, M.; Henke, N.; Chung, R.; et al. 2018. Notes from the AI Frontier. _McKinsey Global Institute_ . 

Cortes, C.; Gonzalvo, X.; Kuznetsov, V.; Mohri, M.; and Yang, S. 2016. AdaNet: Adaptive Structural Learning of Artificial Neural Networks. _arXiv:1607.01097_ . 

Dai, Z.; Yang, Z.; Yang, F.; Cohen, W. W.; and Salakhutdinov, R. 2017. Good Semi-supervised Learning that Requires a Bad GAN. _arxiv:1705.09783_ . 

Dauphin, Y. N.; Fan, A.; Auli, M.; and Grangier, D. 2016. Language Modeling with Gated Convolutional Networks. _arXiv:1612.08083_ . 

Devlin, J.; Chang, M.; Lee, K.; and Toutanova, K. 2018. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. _arXiv:1810.04805_ . 

Dua, D.; and Graff, C. 2017. UCI Machine Learning Repository. URL http://archive.ics.uci.edu/ml. 

Gehring, J.; Auli, M.; Grangier, D.; Yarats, D.; and Dauphin, Y. N. 2017. Convolutional Sequence to Sequence Learning. _arXiv:1705.03122_ . 

Geurts, P.; Ernst, D.; and Wehenkel, L. 2006. Extremely randomized trees. _Machine Learning_ 63(1): 3–42. ISSN 1573-0565. 

Goodfellow, I.; Bengio, Y.; and Courville, A. 2016. _Deep Learning_ . MIT Press. 

Grabczewski, K.; and Jankowski, N. 2005. Feature selection with decision tree criterion. In _HIS_ . 

Grandvalet, Y.; and Bengio, Y. 2004. Semi-supervised Learning by Entropy Minimization. In _NIPS_ . 

Guyon, I.; and Elisseeff, A. 2003. An Introduction to Variable and Feature Selection. _JMLR_ 3: 1157–1182. 

He, K.; Zhang, X.; Ren, S.; and Sun, J. 2015. Deep Residual Learning for Image Recognition. _arXiv:1512.03385_ . 

Hestness, J.; Narang, S.; Ardalani, N.; Diamos, G. F.; Jun, H.; Kianinejad, H.; Patwary, M. M. A.; Yang, Y.; and Zhou, Y. 2017. Deep Learning Scaling is Predictable, Empirically. _arXiv:1712.00409_ . 

Ho, T. K. 1998. The random subspace method for constructing decision forests. _PAMI_ 20(8): 832–844. 

Hoffer, E.; Hubara, I.; and Soudry, D. 2017. Train longer, generalize better: closing the generalization gap in large batch training of neural networks. _arXiv:1705.08741_ . 

Hudson, D. A.; and Manning, C. D. 2018. Compositional Attention Networks for Machine Reasoning. _arXiv:1803.03067_ 

Humbird, K. D.; Peterson, J. L.; and McClarren, R. G. 2018. Deep Neural Network Initialization With Decision Trees. _IEEE Trans Neural Networks and Learning Systems_ . 

Ibrahim, M.; Louie, M.; Modarres, C.; and Paisley, J. W. 2019. Global Explanations of Neural Networks: Mapping the Landscape of Predictions. _arxiv:1902.02384_ . 

Kaggle. 2019a. Historical Data Science Trends on Kaggle. https://www.kaggle.com/shivamb/data-science-trendson-kaggle. Accessed: 2019-04-20. 

Kaggle. 2019b. Rossmann Store Sales. https://www.kaggle. com/c/rossmann-store-sales. Accessed: 2019-11-10. Ke, G.; Meng, Q.; Finley, T.; Wang, T.; Chen, W.; et al. 2017. LightGBM: A Highly Efficient Gradient Boosting Decision Tree. In _NIPS_ . 

Ke, G.; Zhang, J.; Xu, Z.; Bian, J.; and Liu, T.-Y. 2019. TabNN: A Universal Neural Network Solution for Tabular Data. URL https://openreview.net/forum?id=r1eJssCqY7. Kingma, D. P.; and Ba, J. 2014. Adam: A Method for Stochastic Optimization. In _ICLR_ . 

Kontschieder, P.; Fiterau, M.; Criminisi, A.; and Bulo, S. R.` 2015. Deep Neural Decision Forests. In _ICCV_ . 

Lai, S.; Xu, L.; Liu, K.; and Zhao, J. 2015. Recurrent Convolutional Neural Networks for Text Classification. In _AAAI_ . 

Lundberg, S. M.; Erion, G. G.; and Lee, S. 2018. Consistent Individualized Feature Attribution for Tree Ensembles. _arXiv:1802.03888_ . 

Martins, A. F. T.; and Astudillo, R. F. 2016. From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification. _arXiv:1602.02068_ . 

Mitchell, R.; Adinets, A.; Rao, T.; and Frank, E. 2018. XGBoost: Scalable GPU Accelerated Learning. _arXiv:1806.11248_ . 

Mocanu, D.; Mocanu, E.; Stone, P.; Nguyen, P.; Gibescu, M.; and Liotta, A. 2018. Scalable training of artificial neural networks with adaptive sparse connectivity inspired by network science. _Nature Communications_ 9. 

Mott, A.; Zoran, D.; Chrzanowski, M.; Wierstra, D.; and Rezende, D. J. 2019. S3TA: A Soft, Spatial, Sequential, TopDown Attention Model. URL https://openreview.net/forum? id=B1gJOoRcYQ. 

Nbviewer. 2019. Notebook on Nbviewer. URL https://nbviewer.jupyter.org/github/dipanjanS/data ~~s~~ cience for ~~a~~ ll/blob/master/tds ~~m~~ odel interpretation ~~x~~ ai/HumaninterpretableMachineLearning-DS.ipynb#. Oza, N. C. 2005. Online bagging and boosting. In _IEEE Trans Conference on Systems, Man and Cybernetics_ . Prokhorenkova, L.; Gusev, G.; Vorobev, A.; Dorogush, A. V.; and Gulin, A. 2018. CatBoost: unbiased boosting with categorical features. In _NIPS_ . 

Oza, N. C. 2005. Online bagging and boosting. In _IEEE Trans Conference on Systems, Man and Cybernetics_ . 

Yang, Y.; Morillo, I. G.; and Hospedales, T. M. 2018. Deep Neural Decision Trees. _arXiv:1806.06988_ . 

Yoon, J.; Jordon, J.; and van der Schaar, M. 2019. INVASE: Instance-wise Variable Selection using Neural Networks. In _ICLR_ . 

Radford, A.; Metz, L.; and Chintala, S. 2015. Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks. _arXiv:1511.06434_ . 

Raina, R.; Battle, A.; Lee, H.; Packer, B.; and Ng, A. Y. 2007. Self-Taught Learning: Transfer Learning from Unlabeled Data. In _ICML_ . 

Ribeiro, M.; Singh, S.; and Guestrin, C. 2016. “Why Should I Trust You?”: Explaining the Predictions of Any Classifier. In _KDD_ . 

Shavitt, I.; and Segal, E. 2018. Regularization Learning Networks: Deep Learning for Tabular Datasets. Shrikumar, A.; Greenside, P.; and Kundaje, A. 2017. Learning Important Features Through Propagating Activation Differences. _arXiv:1704.02685_ . 

Sundararajan, M.; Taly, A.; and Yan, Q. 2017. Axiomatic Attribution for Deep Networks. _arXiv:1703.01365_ . 

Tanno, R.; Arulkumaran, K.; Alexander, D. C.; Criminisi, A.; and Nori, A. V. 2018. Adaptive Neural Trees. _arXiv:1807.06699_ . 

Tensorflow. 2019. Classifying Higgs boson processes in the HIGGS Data Set. URL https://github.com/tensorflow/ models/tree/master/official/boosted ~~t~~ rees. 

Trinh, T. H.; Luong, M.; and Le, Q. V. 2019. Selfie: Self-supervised Pretraining for Image Embedding. _arXiv:1906.02940_ . 

Vijayakumar, S.; and Schaal, S. 2000. Locally Weighted Projection Regression: An O(n) Algorithm for Incremental Real Time Learning in High Dimensional Space. In _ICML_ . Wang, S.; Aggarwal, C.; and Liu, H. 2017. Using a random forest to inspire a neural network and improving on it. In _SDM_ . 

Wen, W.; Wu, C.; Wang, Y.; Chen, Y.; and Li, H. 2016. Learning Structured Sparsity in Deep Neural Networks. _arXiv:1608.03665_ . 

Xu, L.; Skoularidou, M.; Cuesta-Infante, A.; and Veeramachaneni, K. 2019. Modeling Tabular data using Conditional GAN. _arXiv:1907.00503_ . 

