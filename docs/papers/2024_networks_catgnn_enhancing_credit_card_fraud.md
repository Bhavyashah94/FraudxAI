---
title: "CaT-GNN: Enhancing Credit Card Fraud Detection via Causal Temporal Graph Neural Networks"
authors: "networks"
year: 2024
arxiv_id: "2402.14708"
original_file: "2402.14708.pdf"
pdf_path: "docs/papers\2024_networks_catgnn_enhancing_credit_card_fraud.pdf"
---

# CaT-GNN: Enhancing Credit Card Fraud Detection via Causal Temporal Graph Neural Networks

**Authors:** Networks et al.  
**Year:** 2024 | **arXiv:** [`2402.14708`](https://arxiv.org/abs/2402.14708)  
**Local PDF:** [`2024_networks_catgnn_enhancing_credit_card_fraud.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2024_networks_catgnn_enhancing_credit_card_fraud.pdf)

---

# **CaT-GNN: Enhancing Credit Card Fraud Detection via Causal Temporal Graph Neural Networks** 

**Yifan Duan**<sup>1</sup> , **Guibin Zhang**<sup>3</sup> , **Shilong Wang**<sup>1</sup> , **Xiaojiang Peng**<sup>4</sup> , **Wang Ziqi**<sup>1</sup> , **Junyuan Mao**<sup>1</sup> , **Hao Wu**<sup>1</sup><sup>_∗_</sup> , **Xinke Jiang**<sup>2</sup><sup>_∗_</sup> , **Kun Wang**<sup>1</sup><sup>_∗_</sup> 

1University of Science and Technology of China, Hefei China, 2Peking University, Beijing, China, 

3Tongji University, Shanghai, China, 4Shenzhen Technology University, Shenzhen, China 

- _{_ Yifan Duan, Shilong Wang, Wang Ziqi, Hao Wu, wk520529, maojunyuan _}_ @mail.ustc.edu.cn bin2003@tongji.edu.cn, pengxiaojiang@sztu.edu.cn, thinkerjiang@foxmail.com 

## **Abstract** 

Credit card fraud poses a significant threat to the economy. While Graph Neural Network (GNN)based fraud detection methods perform well, they often overlook the causal effect of a node’s local structure on predictions. This paper introduces a novel method for credit card fraud detection, the **<u>Ca</u>** usal **<u>T</u>** emporal **<u>G</u>** <u>raph</u> **<u>N</u>** <u>eural</u> **N** etwork (CaTGNN), which leverages causal invariant learning to reveal inherent correlations within transaction data. By decomposing the problem into discovery and intervention phases, CaT-GNN identifies causal nodes within the transaction graph and applies a causal mixup strategy to enhance the model’s robustness and interpretability. CaT-GNN consists of two key components: Causal-Inspector and CausalIntervener. The Causal-Inspector utilizes attention weights in the temporal attention mechanism to identify causal and environment nodes without introducing additional parameters. Subsequently, the Causal-Intervener performs a causal mixup enhancement on environment nodes based on the set of nodes. Evaluated on three datasets, including a private financial dataset and two public datasets, CaT-GNN demonstrates superior performance over existing state-of-the-art methods. Our findings highlight the potential of integrating causal reasoning with graph neural networks to improve fraud detection capabilities in financial transactions. 

## **1 Introduction** 

The substantial damages wrought by financial fraud continue to garner ongoing focus from academic circles, the business sector, and regulatory bodies [Jiang _et al._ , 2016; Aleksiejuk and Hołyst, 2001]. Fraudsters masquerade as ordinary users and attack transactions made with credit cards [Ileberi _et al._ , 2022], which may inflict substantial economic losses and pose a severe threat to sustainable economic growth [AlFalahi and Nobanee, 2019]. Consequently, effective detection of financial fraud is imperative for safeguarding the economy and consumer security. 



<!-- Start of picture text -->
? Environment 0.12 ?<br>Stage 1: Discover 0.14<br>Attention  ? 0.03<br>temporal network  𝒇(∗) ?<br>Attention Score<br>Abstract Financial Graph  Attention Score Map<br>Causal Mix-up<br>Stage 2:<br>Intervention<br>Graph netwrok<br>update  ↑<br>...<br>0.35<br>0.45<br><!-- End of picture text -->

Figure 1: The model overview. First Stage (discovery): we utilize an attention map in the attention temporal network to identify causal nodes and environment nodes. Second Stage: Intervention, we apply causal mix-up enhancement to the environment nodes. 

In the financial deception realm, identifying credit card fraud has garnered considerable attention among both industry and academia [Bhattacharyya _et al._ , 2011]. Traditional approaches to detecting fraudulent activities typically entail meticulous examination of each transaction for irregularities, employing predefined criteria such as verification against lists of compromised cards or adherence to established transaction thresholds [Maes _et al._ , 2002; Fu _et al._ , 2016]. However, the aforementioned anti-fraud systems, based on expert prior and rules, are often susceptible to exploitation by fraudsters, who can circumvent detection by crafting ingenious transaction methods that elude the system’s scrutiny of illicit activities. Toward this end, predictive modeling has been introduced, aiming to autonomously identify patterns that suggest fraudulent activity and calculate a corresponding risk score. 

Currently, state-of-the-art predictive models are focused on using deep learning methods, capturing potential illegal patterns in a data-driven manner [Fu _et al._ , 2016; Dou _et al._ , 2020]. For instance, [Liu _et al._ , 2021] introduces PC-GNN, a Graph Neural Network approach that effectively handles class imbalance in graph-based fraud detection by selectively sampling nodes and edges, particularly focusing on the minority class. Moreover, [Xiang _et al._ , 2023] leverages transaction records to construct a temporal transaction graph, apply- 

> _∗_ Corresponding Authors 

ing a Gated Temporal Attention Network to effectively learn transaction representations and model fraud patterns. Unfortunately, **i)** these methods often overlook the intrinsic patterns and connections within the data due to a lack of consideration for local structure consistency; **ii)** they lack the ability to uncover <u>the causal nature of each</u> specific case, which leads to inadequate differentiation between the attributes of causal nodes and environment nodes, thereby impairing the model’s generalization capabilities; **iii)** they lack interpretability in making specific predictions. 

In this paper, we introduce a novel **<u>Ca</u>** <u>usal</u> **<u>T</u>** <u>emporal</u> **<u>G</u>** <u>raph</u> **<u>N</u>** <u>eural</u> **N** etwork, termed CaT-GNN, aiming at providing an interpretable paradigm for credit card fraud detection. Guided by the currently popular causal invariant learning techniques [Chang _et al._ , 2020; Liu _et al._ , 2022], CaTGNN’s primary objective is to _unveil the inherent correlations in the transaction attribute data of nodes within available temporal transaction graphs_ , thereby offering interpretability for complex transaction fraud problems. 

To unravel causal correlations, specifically, we decompose the algorithmic process of CAT-GNN into two stages - **discovery** and **intervention** . The goal of the discovery stage is to identify potential causal components within observed temporal graph data, where we introduce a causal temporal graph neural network for modeling. Utilizing the popular node-attention metrics [Veliˇckovi´c _et al._ , 2017; Xiang _et al._ , 2023], we employ attention score to locate key nodes, designated as causal and environment nodes. In the intervention process, we aim to reasonably enhance potential environment nodes. This approach is designed to align with and perceive the underlying distribution characteristics in explicit fraud networks, thereby boosting our temporal GNN’s ability to identify and understand problematic nodes. Furthermore, drawing inspiration from [Wang _et al._ , 2020], to ensure that causal interventions between nodes do not interfere with each other, we create parallel universes for each node. Consequently, the model is exposed to a wider potential data distribution, providing insights for fraud prediction with a causal perspective. This process can further be understood as a back-door adjustment in causal theory [Pearl, 2009; Pearl and Mackenzie, 2018]. The contributions of this paper are summarized as follows: 

- We propose a novel method, CaT-GNN, that embodies both causality and resilience for the modeling of credit card fraud detection. By harnessing causal theory, known for its interpretability, CaT-GNN enables the model to encompass a wider potential data distribution, thereby ensuring its exceptional performance in this task. 

- CaT-GNN, characterized by its refined simplicity, initially identifies causal nodes and subsequently refines the model into a causally coherent structure. It aims to achieve invariance in attribute information and temporal features through semi-supervised learning, thereby providing a bespoke and robust foundation for targeted tasks. 

- We evaluate CaT-GNN on three representative datasets, including a **<u>private</u>** financial benchmark, and the other two are public settings. Extensive experiments show that our proposed method outperforms the compared state-of-the- 

art baselines in credit card fraud detection, thanks to the casual intervention of the node causal augment. 

## **2 Preliminaries** 

**_Definition 1. (Multi-Relation Graph)_** The Multi-Relation Financial Graph _G_ is defined as _G_ = ( _V, E, X , Y_ ), where _V_ = _{v_ 1 _, v_ 2 _, · · · , vN }_ represents the set of nodes, with _N_ = _|V|_ indicates the total number of nodes. _X ∈_ R<sup>_N×d_</sup> denotes the node features with _xi ∈_ R<sup>_d_</sup> as its entry for node _vi_ , _d_ is the feature dimension. Each node _vi_ is assigned a label _yi ∈Y_ , which is a binary variable with the value in _{_ 0 _,_ 1 _}_ . _E_ = _{E_ 1 _, · · · , ER}_ signifies the set of edges, partitioned into _R_ distinct types of relations. 

**_Definition 2. (Graph-based Fraud Detection)_** The graphbased fraud detection problem is defined on the multirelation graph _G_ = ( _V, E, X , Y_ ). For such a problem, each node _vi_ represents the target entity such as a transaction record, and has a label _yi ∈ Y_ , where _yi_ = 0 represents benign and _yi_ = 1 represents fraud. The objective of graph-based fraud detection is to identify fraud nodes that stand out distinctly from the non-fraudulent, or benign, nodes within a multi-relational graph _G_ . This task is effectively approached as a binary classification problem focused on nodes within the graph _G_ . And the surprised Binary Cross-Entropy Loss function is: minΘ _L_ = _− B_<sup><u>1</u></sup> � _Bu_ =1 _yi_<sup>_⊤_log (ˆ</sup><sup>_yi_) + (1</sup><sup>_−yi_)</sup><sup>_⊤_log (1</sup><sup>_−y_ˆ</sup><sup>_i_)</sup> + _η||_ Θ _||_<sup>2</sup> _,_ � � where _B_ is the batch size, _y_ ˆ _i ∈_ [0 _,_ 1] is the predicted probability, and _yi ∈{_ 0 _,_ 1 _}_ is the ground truth. Θ is the parameter of the GNN predictor. 

## **3 Methodology** 

In Section 3.1, we explore the motivation behind our approach, emphasizing the crucial role of understanding the local structure and causal relationships within transaction data to improve detection accuracy. Section 3.2 introduces our two-phase method: discovery and intervention. Section Section 3.2 provides the causal theory support. 

### **3.1 Motivation** 



<!-- Start of picture text -->
1 2 0 1 1 2 0 1 1 2 0 1<br>1 1 1<br>𝑥𝑖 2 𝑥𝑖 2 𝑥𝑖 2<br>0 1 0 1 0 1 0 1 0 1 0 1<br>1 1 1<br>1 2 0 1 1 2 0 1 1 2 0 1<br>0 0 0<br>Original prediction :           1 GTAN prediction:           1 Post-intervention prediction :            2<br><!-- End of picture text -->

Figure 2: **_Motivation._** The original prediction incorrectly identifies a fraudster (central node labeled _xi_ ) as benign, as does the state-ofthe-art GTAN model. Following our causal intervention, the prediction is correctly adjusted to identify _xi_ as a fraudster. _Green: benign users, red: fraudsters, gray: unlabeled nodes._ 

Taking the arXiv [Hu _et al._ , 2020] dataset as an example, real-world graphs often exhibit locally variable structures, 



<!-- Start of picture text -->
Input Graph  𝑮 x<br>Skip-connection Output Benefits<br>+ + +<br>Explainability<br>c e<br>Generalizability<br>Iterative<br>Stacking Accuracy y Theoretical support<br>CT-GAT: Causal Temporal GAT  Block<br>Attention Score 𝛼𝑥𝑖 , 𝑥𝑗<br>Causal Inspector 𝑥𝑖 𝑥𝑖 Causal Intervener ′ 𝑥𝑖<br>𝑥𝑖 𝑥𝑗 𝑥𝑗 ′<br>𝑁 𝑥𝑖 𝑥𝑗 𝑥𝑗 𝑥𝑗 𝑘 𝑥𝑗<br>𝐼𝑗 = 𝛼𝑥𝑖,𝑥𝑗ൗ ෍ 𝛼𝑥𝑖,𝑥𝑗 𝑥𝑗′ = 𝑎𝑗𝑥𝑗 + ෍ 𝑎𝑖𝑥𝑐𝑖<br>𝑗=1 𝑖=1<br>MLP<br>Embedding CT-GAT CT-GAT CT-GAT<br><!-- End of picture text -->

Figure 3: The depiction of the proposed model’s architecture, featuring a causal temporal graph attention mechanism, alongside the theoretical support for backdoor adjustment. 

that is, the distribution of node attributes differs from the distribution of local structural properties [Feng _et al._ , 2021]. We observe that this phenomenon is also prevalent in the financial sector, where cunning fraudsters may disguise themselves through various means (such as feature camouflage and relationship disguise) to connect with users who have a good credit transaction history [Dou _et al._ , 2020]. _In such scenarios, if we simply aggregate node information and neighbor information together, it is likely to obscure the suspiciousness of the fraudsters, which contradicts our objective._ This situation tends to yield poorer training outcomes, especially in a semi-supervised learning environment with limited labeled data. Existing methods do not incorporate causal factors into credit card fraud modeling, <u>resulting in mod-</u> els that fail to learn the intrinsic connections of node attributes. This oversight further leads to the neglect of causal attribute structure differences on test nodes, thereby reducing the model’s generalizability. By comprehensively examining the confounding variables, we are able to significantly alleviate the aforementioned issue, as illustrated in Figure 2. This strategy is the cornerstone of our framework and is also known as the “backdoor adjustment” technique [Pearl, 2009; Pearl and Mackenzie, 2018]. 

### **3.2 Discovering & Intervention** 

Based on the motivation, we adopt a causal perspective to analyze the attribute aggregation process and formalize principles for distinguishing between causal and non-causal elements within local structures. We first introduce the discovery process to effectively examine the causal and environment nodes within the current node’s local structure. In response, we refine the temporal attention graph network mechanism[Xiang _et al._ , 2022] into _a causal temporal GAT mechanism_ as shown in the upper half of Figure 3. This refinement introduces two key components designed to accurately identify both environmental and causal nodes, which enhances our ability to understand and manipulate the local structural dynamics more effectively. 

In the context of temporal transaction graphs, we main- 

tain a set of transaction records, denoted as _R_ = [ _rt_ 1 _, rt_ 2 _, · · · , rti_ ], alongside their embeddings _X_ = [ _xt_ 1 _, xt_ 2 _, · · · , xti_ ] obtained via a projection layer. As demonstrated in [Shi _et al._ , 2020], GNNs are capable of concurrently propagating attributes and labels. Consequently, we integrate fraud labels as an embedded feature within the attribute embedding _xti_ , employing masking techniques to prevent label leakage [Xiang _et al._ , 2023]. However, this aspect does not constitute the primary focus of our research. 

**Causal-Inspector:** We design a Causal-Inspector to identify causal and environment nodes as shown in the bottom left corner of Figure 3. To aggregate information efficiently, we employ the aforementioned causal temporal graph attention mechanism, which allows for dynamic information flow based on the temporal relationships among transactions. Leveraging a multi-head attention mechanism, we compute temporal attention scores that serve as weights for each neighboring node, facilitating the assessment of each neighbor’s causal importance, which can be formulated as follows: 



where _Wa_ is a learnable weight matrix, _αxi,xj_ represents the attention weight of node _xi_ with respect to node _xj_ in one head, which determines the importance of node _xi_ relative to node _xj_ . The _⊕_ symbol represents the concatenation operation. _N_ ( _xi_ ) is the set of temporal neighboring nodes of node _xi_ . In order to quantify the importance of each node _xj_ we aggregate the attention weights _αx_<sup>_h_</sup> _i,xj_<sup>from each attention</sup> head and compute the average to determine the final weight of the node. Then, based on its final weight, we calculate its normalized importance: 



node with respect to _xi_ . This formula calculates the normalized importance weight _Ij_ , representing the importance of node _xj_ by compiling the contributions from all attention heads, thus providing a comprehensive measure of node significance. To segregate the nodes into environmental and causal categories, we introduce a proportion parameter _re_ , ranging between 0 and 1, which denotes the fraction of nodes to be earmarked as environment nodes. This approach affords us the flexibility to select environment nodes tailored to the specific exigencies of the graph. We use the argmin( _·_ ) function to select the _⌈reN ⌉_ nodes with the lowest importance scores as environment nodes. Therefore, a ranking function _R_ is defined to map _Ij_ to its rank among all node importance scores. Then, we determine the environment set _Se_ as: 



The remaining nodes, those not in _Se_ , naturally form the set of causal nodes _Sc_ .This method ensures that nodes with the lowest importance scores are precisely selected as environmenta nodes according to the proportion _re_ , while the rest serve as causal nodes. Due to the differences between test and training distributions [Feng _et al._ , 2021], CaT-GNN is dedicated to perceiving the essence of temporal graph data, thereby enhancing generalization capabilities and robustness. 

**Causal-Intervener:** We design a Causal Intervener as shown in the bottom right corner of Figure 3, which employs a transformative mixup strategy known as a causal mixup, that blends environment nodes with a series of causally significant nodes. Given an environmental node _xj ∈ Se_ , We select the causal nodes _{xc_ 1 _, xc_ 2 _, · · · , xck}_ with the highest importance scores, which are computed as outlined in the CausalInspector, from the causal set _Sc_ at a proportion of _rc_ . The _causal mixup_ is then executed by linearly combining the environmental node with the selected causal nodes, weighted by their respective coefficients _{aj, a_ 1 _, a_ 2 _, · · · , ak}_ , which are learned through a dedicated linear layer: 



where _x_<sup>_′_</sup> _j_<sup>is the causally mixed environmental node,</sup><sup>_k_is the</sup> number of selected causal nodes, _aj_ is the self-weight of the environmental node reflecting its inherent causal significance, and _ai_ is the causal node weight. These weights are normalized such that _aj_ +<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_ai_=1.Theincorporationofthe</sup> causal mixup enhances the robustness of the model against distributional shifts by embedding a richer causal structure within the environmental node. By adapting the causal structure to the environmental context, the Causal-Intervener aims to mitigate the disparity between training and test distributions, thus bolstering the model’s generalizability. Finally, we aggregate the information, and the outputs of multiple attention heads are concatenated to form a more comprehensive representation: 



where _Wc_ is a learnable weight matrix, _H_ is a attention head, _M_ denotes the aggregated embeddings. It is important to highlight that the causal intervention result _x_<sup>_′_</sup> _j_<sup>onanenvi-</sup> ronmental node _xj_ with respect to _xi_ is essentially a duplicate of _xj_ and does not modify _xj_ itself. This distinction is crucial as it guarantees that the process of augmenting central nodes within individual local structures remains mutually non-disruptive. By preserving the original state of _xj_ , we ensure that enhancements applied to central nodes in one local structure do not adversely affect or interfere with those in another, maintaining the integrity and independence of local structural enhancements [Wang _et al._ , 2020]. 

### **3.3 Causal Support of CaT-GNN** 

In elucidating the causal backbone of CaT-GNN, we invoke causal theory to formulate a Structural Causal Model (SCM) as propounded by [Pearl, 2009]. This framework scrutinizes four distinct elements: the inputs node attribute _X_ , the truth label _Y_ decided by both the attribute of causal nodes of _X_ symbolized as _C_<sup>˜</sup> , and the confounder _E_ , emblematic of the attribute of environment nodes. The causal interplay among these variables can be articulated as follows: 

- _C_<sup>˜</sup> _←−_ X _−→_ E. The local structure of node attribute _X_ is composed of causal nodes attributes _C_<sup>˜</sup> and environment nodes attributes _E_ . 

- _C_<sup>˜</sup> _−→_ Y _←−_ E. The causal attributes _C_<sup>˜</sup> actually determine the true value _Y_ , however, the environmental attributes _E_ also affect the prediction results, causing spurious associations. 

Do-calculus [Pearl, 2009] is a trio of rules within the causal inference framework that facilitates the mathematical deduction of causal effects from observed data. These rules enable manipulation of do( _·_ ) operator expressions, essential for implementing interventions in causal models: 



Typically, a model _Mθ_ that is trained using Empirical Risk Minimization (ERM) may not perform adequately when generalizing to test data distribution _Ptest_ . These shifts in distribution are often a result of changes within environment nodes, necessitating the need to tackle the confounding effects. As illustrated in Figure 3, we apply causal intervention to enhance the model’s generalizability and robustness. To this end, our approach utilizes do-calculus [Pearl, 2009] on the variable _C_ to negate the influence of the backdoor path _E → Y_ by estimating _P_ � _Y |_ do( _C_<sup>ˆ</sup> )�= _Pm_ ( _Y |C_<sup>ˆ</sup> ): 



Table 1: Statistics of the three datasets. 

|Dataset|#Node|#Edge|#Fraud|#benigh|
|---|---|---|---|---|
|YelpChi|45,954|7,739,912|6,677|39,277|
|Amazon|11,948|8,808,728|821|11,127|
|S-FFSD|130,840|3,492,226|2,950|17,553|



where _Ne_ signifies the count of environment nodes, with _Ei_ indicating the _i_ -th environmental variable. The environmental enhancement of Cat-GNN is in alignment with the theory of backdoor adjustment, thereby allowing for an effective exploration of possible test environment distributions. 

## **4 Experiments** 

In this section, we critically assess the CaT-GNN model on a series of research questions (RQs) to establish its efficacy in graph-based fraud detection tasks. The research questions are formulated as follows: 

- **RQ1** : Does CaT-GNN outperform the current state-of-theart models for graph-based anomaly detection? 

- **RQ2:** What is the effectiveness of causal intervention in the aggregation of neighboring information? 

- **RQ3:** What is the performance with respect to different environmental ratios _re_ ? 

- **RQ4:** Is CaT-GNN equally effective in semi-supervised settings, and how does it perform with limited labeled data? 

- **RQ5:** Does the causal intervention component lead to a significant decrease in efficiency? 

### **4.1 Experimental Setup** 

**Datasets.** we adopt one open-source **f** inacial **f** raud **s** emisupervised **d** ataset [Xiang _et al._ , 2023], termed S-FFSD<sup>1</sup> , with the partially labeled transaction records. Same with the definition in section 2, if a transaction is reported by a cardholder or identified by financial experts as fraudulent, the label _yv_ will be 1; otherwise, _yv_ will be 0. In addition, we also validate on two other public fraud detection datasets **Yelpchi** and **Amazon** . **Yelpchi** [Rayana and Akoglu, 2015] compiles a collection of hotel and restaurant reviews from Yelp, in which nodes represent reviews. And there are three kinds of relationship edges among these reviews. **Amazon** : The Amazon graph [McAuley and Leskovec, 2013] comprises reviews of products in the musical instruments category, in which nodes represent users, and the edges are the corresponding three kinds of relationships among reviews. The statistics of the above three datasets are shown in Table 1. 

**Baselines.** To verify the effectiveness of our proposed CaTGNN, we compare it with the following state-of-the-art methods. ❶ _Player2Vec_ . Attributed Heterogeneous Information Network Embedding Framework [Zhang _et al._ , 2019]. ❷ _Semi-GNN_ . A semi-supervised graph attentive network for financial fraud detection that adopts the attention mechanism to aggregate node embed dings across graphs [Wang _et al._ , 2019]. ❸ _GraphConsis_ . The GNN-based fraud detectors aim 

1https://github.com/AI4Risk/antifraud 

at the inconsistency problem [Liu _et al._ , 2020]. ❹ _GraphSAGE_ . The inductive graph learning model is based on a fixed sample number of the neighbor nodes [Hamilton _et al._ , 2017]. ❺ _CARE-GNN_ The camouflage-resistant GNN-based model tackling fraud detection [Dou _et al._ , 2020]. ❻ _PC-GNN_ . A GNN-based model to address the issue of class imbalance in graph-based fraud detection [Liu _et al._ , 2021]. ❼ _GTAN_ . A semi-supervised GNN-based model that utilizes a gated temporal attention mechanism to analyze credit card transaction data [Xiang _et al._ , 2023]. ❽: _CaT-GNN (PL)_ . This variant of the CaT-GNN framework selects environment nodes based on a proportion _re_ and determines mixup weights _ai_ via a learnable linear layer. ❾: _CaT-GNN (PI)_ . This version employs a proportional selection of environment nodes and leverages the nodes’ importance scores to inform mixup weights _ai_ = _Ii/_<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_Ii_.❿:</sup><sup>_CaT-GNN(FL)_.Thisvariantusesa</sup> fixed number of environment nodes. Mixup weights are determined by a learnable linear layer. ❿: _CaT-GNN (FI)_ . Combining fixed environmental node selection with importancebased weighting for mixup. 

**Reproducibility** In our experiment, the learning rate _lr_ is set to 0.003, and the batch size batch _Nbatch_ is established at 256. Moreover, the input dropout ratio _rdropout_ is determined to be 0.2, with the number of attention heads _Nhead_ set to 4, and the hidden dimension _d_ to 256. We employed the Adam optimizer to train the model over _Nepoch_ = 100 epochs, incorporating an early stopping mechanism to prevent overfitting. In GraphConsis, CARE-GNN, PC-GNN and GTAN, we used the default parameters suggested by the original paper. In Semi-GNN and Player2Vec, We set the learning rate to 0.01. In YelpChi and Amazon datasets, the train, validation, and test ratio are set to be 40%, 20%, and 40% respectively. In the S-FFSD dataset, we use the first 7 months’ transactions as training data, and the rest as test data. Similar to previous work [Liu _et al._ , 2021], we repeat experiments with different random seeds 5 times and we report the average and standard error. Experimental results are statistically significant with _p <_ 0 _._ 05. Cat-GNN and other baselines are all implemented in Pytorch 1.9.0 with Python 3.8. All the experiments are conducted on Ubuntu 18.04.5 LTS server with 1 NVIDIA Tesla V100 GPU, 440 GB RAM. 

**Metrics.** We selected three representative and extensively utilized metrics: **AUC** (Area Under the ROC Curve), **F1macro** and **AP** (averaged precision). The first metric AUC is the area under the ROC Curve and as a single numerical value, AUC succinctly summarizes the classifier’s overall performance across all thresholds. The second metric F1macro is the macro average of F1 score which can be formulated as _F_ 1 _macro_ = 1 _/_ ( _l_<sup>�</sup><sup>_l_</sup> _i_ =1 <u>2</u> _<u>×PPi</u>_ + _<u>i×RRi i</u>_<sup>),andthethird</sup> metric AP is averaged precision that can be formulated as _AP_ =<sup>�</sup><sup>_l_</sup> _i_ =1<sup>(</sup><sup>_Ri−Ri−_1)</sup><sup>_Pi_,where</sup><sup>_Pi_stands for the Preci-</sup> sion and _Ri_ stands for recall. 

### **4.2 Performance Comparison (RQ1)** 

In the experiment of credit card fraud detection across three distinct datasets, Cat-GNN showcases superior performance metrics compared to its counterparts. <u>First of all,</u> Cat-GNN achieves the highest AUC in all three datasets, 

Table 2: Performance Comparison (in percent ± standard deviation) on YelpChi, Amazon and S-FFSD datasets across five runs. The best performances are marked with **bold font** , and the second-to-best are shown underlined. 

|Dataset||YelpChi|||Amazon|||S-FFSD||
|---|---|---|---|---|---|---|---|---|---|
|Metric|AUC|F1|AP|AUC|F1|AP|AUC|F1|AP|
|Player2Vec|0.7012_±_0.0089|0.4120_±_0.0142|0.2477_±_0.0161|0.6187_±_0.0152|0.2455_±_0.0091|0.1301_±_0.0117|0.5284_±_0.0101|0.2149_±_0.0136|0.2067_±_0.0155|
|Semi-GNN|0.5160_±_0.0154|0.1023_±_0.0216|0.1809_±_0.0205|0.7059_±_0.0211|0.5486_±_0.0105|0.2248_±_0.0142|0.5460_±_0.0125|0.4393_±_0.0152|0.2732_±_0.0207|
|GraphSAGE|0.5414_±_0.0029|0.4516_±_0.0954|0.1806_±_0.0866|0.7590_±_0.0053|0.5926_±_0.0087|0.6597_±_0.0079|0.6534_±_0.0095|0.5396_±_0.0101|0.3881_±_0.0089|
|GraphConsis|0.7046_±_0.0287|0.6023_±_0.0195|0.3269_±_0.0186|0.8761_±_0.0317|0.7725_±_0.0319|0.7296_±_0.0301|0.6554_±_0.0412|0.5436_±_0.0376|0.3816_±_0.0341|
|CARE-GNN|0.7745_±_0.0281|0.6252_±_0.0091|0.4238_±_0.0151|0.8998_±_0.0925|0.8468_±_0.0085|0.8117_±_0.0114|0.6589_±_0.1078|0.5725_±_0.0096|0.4004_±_0.0090|
|PC-GNN|0.7997_±_0.0021|0.6429_±_0.0205|0.4782_±_0.0194|0.9472_±_0.0019|0.8798_±_0.0084|0.8442_±_0.0096|0.6707_±_0.0031|0.6051_±_0.0230|0.4479_±_0.0210|
|GTAN|0.8675_±_0.0036|0.7254_±_0.0197|0.6425_±_0.0154|0.9580_±_0.0014|0.8954_±_0.0095|0.8718_±_0.0083|0.7496_±_0.0041|0.6714_±_0.0089|0.5709_±_0.0097|
|Cat-GNN(FI)|0.8721_±_0.0044|0.7336_±_0.0295|0.6528_±_0.0209|0.9643_±_0.0026|0.9011_±_0.0129|0.8794_±_0.0102|0.7643_±_0.0078|0.6907_±_0.0198|0.5925_±_0.0174|
|Cat-GNN(FL)|0.8910_±_0.0026|0.7692_±_0.0182|0.6687_±_0.0135|0.9705_±_0.0016|0.9125_±_0.0099|0.8942_±_0.0081|0.8023_±_0.0067|0.7031_±_0.0154|0.6145_±_0.0169|
|Cat-GNN(PI)|0.8895_±_0.0041|0.7706_±_0.0223|0.6701_±_0.0181|0.9669_±_0.0021|0.9077_±_0.0113|0.8896_±_0.0095|0.8145_±_0.0061|0.7096_±_0.0149|0.6294_±_0.0166|
|Cat-GNN(PL)|**0.9035**_±_**0.0035 **|**0.7783**_±_**0.0209 **|**0.6863**_±_**0.0127 **|**0.9706**_±_**0.0015 **|**0.9163**_±_**0.0104 **|**0.8975**_±_**0.0089 **|**0.8281**_±_**0.0054 **|**0.7211**_±_**0.0115 **|**0.6457**_±_**0.0156**|



with values of 0.9035, 0.9706, and 0.8281 for YelpChi, Amazon, and S-FFSD, respectively. This indicates that **Cat-GNN consistently outperforms other methods in distinguishing between classes across diverse datasets** . Focusing on the F1 Score, which balances the precision _Pi_ <u>and recall</u> _<u>Ri</u>_ <u>, Cat-GNN</u> again tops the charts with scores of 0.7783, 0.9163, and 0.7211 for YelpChi, Amazon, and S- FFSD. This reflects the model’s robustness in achieving high precision while not compromising on recall, which is essential where both false positives and false negatives carry significant consequences. Finally, Cat-GNN’s superiority extends to the AP metric, with <u>the</u> improvement of at least 6.82%, 2.86%, and 13.10% for YelpChi, Amazon and S-FFSD respectively. 

The comparative performance of Cat-GNN is particularly significant when contrasted with previous methods such as Player2Vec, Semi-GNN, and GraphSAGE. For the Amazon dataset, existing state-of-the-art models, like CARE-GNN, PC-GNN, and GTAN, have already proven effective at capturing the inherent correlations within the data. In this context, the benefits of causal intervention may not be as pronounced, possibly due to the dataset’s simpler local structures and more uniform distribution. However, for the S-FFSD dataset, our methodology exhibits significant performance improvements. This enhancement is attributed to the complex local structures and the prevalence of unlabeled nodes within the dataset. In such scenarios, causal intervention adeptly learns the inherent attribute connections, thereby boosting the model’s generalization. Additionally, learning mixup weights with a linear layer is more reasonable than weighting with importance scores. Similarly, selecting environment nodes based on proportions is more sensible than choosing a fixed number of environment nodes, and the effect is also slightly better. All in all, This superior performance can be _ascribed to the integration of causal theory within the Cat-GNN_ , enhancing its capacity to comprehend the inherent principles of graph attributes, allowing it to discern complex patterns and interactions that other models are unable to effectively capture. 

### **4.3 Ablation Study (RQ2)** 

In this section, we evaluate the effectiveness of causal interventions in the aggregation within graph structures. Initially, we explore a variant without any causal intervention, termed N-CaT, which aggregates all neighboring information indiscriminately. Secondly, we introduce D-CaT, a method 

that omits environment nodes entirely during the aggregation phase, and directly aggregates all neighboring information in the learning process. Finally, our proposed method, CaT, integrates a causal intervention approach, simultaneously considering both causal nodes and environment nodes during aggregation to refine the learning representations. 

The results shown in Figure 4 highlight the importance of causal intervention in information aggregation. N-CaT, which lacks causal discernment, performs worse across all datasets compared to CaT because it does not account for causal relationships. D-CaT, which simply deletes environmental factors, shows a significant drop in performance, as the mere deletion of environment nodes prevents the model from fully learning valuable information. Our CaT method consistently outperforms the other variants across all datasets, achieving the highest AUC scores. This superior performance underscores the value of our causal intervention technique, which effectively balances the influence of causal and environment nodes, resulting in a more generalizable model. 

### **4.4 Parameter Sensitivity Analysis (RQ3, RQ4)** 

In this section, we study the model parameter sensitivity with respect to the environment nodes ratio and the training ratio. The corresponding results are reported in Figure 5. 

As demonstrated in the left of Figure 5, using the YelpChi dataset as an example, the performance of Cat-GNN (measured by AUC as the performance metric) significantly surpasses other competitive models, including PC-GNN and CARE-GNN, across all training ratios, from 10% to 70%. Particularly at lower training ratios (such as 10%), Cat-GNN remains effective for semi-supervised learning and exhibits more robust performance compared to other models. 

In our sensitivity analysis of the environmental ratio as demonstrated in the right of Figure 5, we observed that CatGNN’s performance on the Amazon dataset is less affected by variations in the training ratio, with AUC fluctuations not exceeding 2%. Conversely, on the S-FFSD dataset, as the training ratio increases from 5% to 40%, there is a larger fluctuation in Cat-GNN’s performance. This can be attributed to the characteristics of the dataset or the differences in the distribution of labeled data. 

### **4.5 Model Efficiency (RQ5)** 

In this section, we present a comprehensive analysis of the efficiency of CaT-GNN. Our causal intervention aims to boost 



<!-- Start of picture text -->
(a) YelpChi<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) Amazon (c) FFSD<br><!-- End of picture text -->

Figure 4: The ablation study results on three datasets. Gray bars represent the D-CaT variant, blue bars represent the N-CaT variant, and orange bars represent the CaT-GNN model. 



<!-- Start of picture text -->
0.93 0.97<br>0.89 0.93<br>0.85 0.89<br>0.81 0.85<br>0.77 0.81<br>CaT-GNN PC-GNN Amazon FFSD<br>GTAN CARE-GNN YelpChi<br>0.73 0.77<br>10 20 30 40 50 60 70 5 10 15 20 25 30 35 40<br>Training Ratio (%) Environment Ratio (%)<br>AUC AUC<br><!-- End of picture text -->

Figure 5: Sensitivity analysis with respect to different training ratios ( **Left** ) and environment ratios ( **Right** ). 

performance while maintaining computational efficiency. Table 3 shows that the performance enhancements are achieved without imposing significant additional computational costs. The results indicate that the execution time with causal intervention experienced only a marginal increase. This negligible rise in time is a testament to the algorithm’s ability to retain its computational efficiency while incorporating our advancements. Thus, our algorithm stands as a robust solution that can cater to the needs of high-performance computing while facilitating enhancements that do not compromise on efficiency. 

Table 3: Experimental run times with and without causal intervention on three datasets. The experiments were conducted on a Tesla V100 40GB GPU, with the execution times measured in seconds. 

|Dataset|YelpChi|Amazon|S-FFSD|
|---|---|---|---|
|No-intervention|126.676|110.518|208.085|
|Causal-intervention|129.481(+2.21%)|113.660(+2.84%)|213.341(+2.52%)|



## **5 Related Works** 

**Graph Neural Network and its Variants.** Graph neural networks have been widely used in structured data prediction [Abadal _et al._ , 2021; Wu _et al._ , 2020; Jiang _et al._ , 2024] by integrating graph structure and attribute. With the development of GNNs, there are several types of GNNs nowadays. **1)** : **_Recurrent Graph Neural Networks_** (RecGNNs) aim to learn node representations with recurrent neural architectures: [Scarselli _et al._ , 2008; Gallicchio and Micheli, 2010; Li _et al._ , 2015; Dai _et al._ , 2018]. **2)** : **_Convolutional Graph Neural Networks_** (ConvGNNs) generalize the operation of convolution from grid data to graph data: [Li _et al._ , 2018; Zhuang and Ma, 2018; Xu _et al._ , 2018; Chiang _et al._ , 2019]. **3)** : **_Spatial–Temporal Graph Neural Networks_** (STGNNs) aim to learn complex hidden patterns from spatial-temporal 

graphs: [Yan _et al._ , 2018; Wu _et al._ , 2019; Guo _et al._ , 2019; Jiang _et al._ , 2023; Li _et al._ , 2022]. 

**Machine-learning based credit card fraud detection.** Recently, numerous efforts have been dedicated to integrating machine learning methodologies into the research of credit card fraud detection. For instance, [Maes _et al._ , 2002] successfully applied Bayesian Belief Networks and MLP to the Europay International dataset. [S¸ahin and Duman, 2011] utilized decision trees and support vector machines on data from a major national bank. [Fu _et al._ , 2016] demonstrates that convolutional neural networks outperform traditional approaches in pattern recognition for higher accuracy. However, their models were limited as they only considered individual transactions or cardholders, missing out on the potential of unlabeled data in real-world transactions [Xiang _et al._ , 2023]. 

**GNN-based credit card fraud detection.** More recently, the focus has shifted towards graph-based approaches as the use of graph convolutional networks on datasets with partial labels has been effective for predicting node attributes within citation networks so that many GNN-based fraud detectors have been proposed to detect fraud [Wang _et al._ , 2019; Liu _et al._ , 2018]. Concretely, [Dou _et al._ , 2020] introduces CARE-GNN for fraud detection on relational graphs, while [Liu _et al._ , 2021] develops PC-GNN for managing imbalanced learning on graphs. Additionally, [Fiore _et al._ , 2019] presents a generative adversarial network to enhance classification capabilities. [Cheng _et al._ , 2020] suggested a joint feature learning model, concentrating on spatial and temporal patterns. However, these methods often lack the capability to uncover the **causal nature** of each specific case and are easily influenced by the surrounding neighbors due to the aggregation mechanism inherent in GNNs. Towards this end, we _take the first step_ to propose a structural causal GNN model, which introduces causal intervention and data augmentation mechanism into the aggregation process of GNN. 

## **6 Conclusion & Future Work** 

In this work, we introduce the Causal Temporal Graph Neural Network (CaT-GNN), a causal approach in the domain of credit card fraud detection. Our model innovates by integrating causal learning principles to discern and leverage the intricate relationships within transaction data. We validate the effectiveness of CaT-GNN through comprehensive experiments on diverse datasets, where it consistently outperforms existing techniques. Notably, CaT-GNN not only enhances detection accuracy but also maintains computational 

efficiency, making it viable for large-scale deployment. Future directions will explore extending this methodology to a broader range of fraudulent activities, with the aim of fortifying the integrity of financial systems globally. 

## **References** 

- [Abadal _et al._ , 2021] Sergi Abadal, Akshay Jain, Robert Guirado, Jorge L´opez-Alonso, and Eduard Alarc´on. Computing graph neural networks: A survey from algorithms to accelerators. _ACM Computing Surveys (CSUR)_ , 54(9):1–38, 2021. 

- [Aleksiejuk and Hołyst, 2001] Agata Aleksiejuk and Janusz A Hołyst. A simple model of bank bankruptcies. _Physica A: Statistical Mechanics and its Applications_ , 299(1-2):198–204, 2001. 

- [AlFalahi and Nobanee, 2019] Latifa AlFalahi and Haitham Nobanee. Conceptual building of sustainable economic growth and corporate bankruptcy. _Available at SSRN 3472409_ , 2019. 

- [Bhattacharyya _et al._ , 2011] Siddhartha Bhattacharyya, Sanjeev Jha, Kurian Tharakunnel, and J Christopher Westland. Data mining for credit card fraud: A comparative study. _Decision support systems_ , 50(3):602–613, 2011. 

- [Chang _et al._ , 2020] Shiyu Chang, Yang Zhang, Mo Yu, and Tommi Jaakkola. Invariant rationalization. In _International Conference on Machine Learning_ , pages 1448– 1458. PMLR, 2020. 

- [Cheng _et al._ , 2020] Dawei Cheng, Xiaoyang Wang, Ying Zhang, and Liqing Zhang. Graph neural network for fraud detection via spatial-temporal attention. _IEEE Transactions on Knowledge and Data Engineering_ , 34(8):3800– 3813, 2020. 

- [Chiang _et al._ , 2019] Wei-Lin Chiang, Xuanqing Liu, Si Si, Yang Li, Samy Bengio, and Cho-Jui Hsieh. Cluster-gcn: An efficient algorithm for training deep and large graph convolutional networks. In _Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining_ , pages 257–266, 2019. 

- [Dai _et al._ , 2018] Hanjun Dai, Zornitsa Kozareva, Bo Dai, Alex Smola, and Le Song. Learning steady-states of iterative algorithms over graphs. In _International conference on machine learning_ , pages 1106–1114. PMLR, 2018. 

- [Dou _et al._ , 2020] Yingtong Dou, Zhiwei Liu, Li Sun, Yutong Deng, Hao Peng, and Philip S Yu. Enhancing graph neural network-based fraud detectors against camouflaged fraudsters. In _Proceedings of the 29th ACM international conference on information & knowledge management_ , pages 315–324, 2020. 

- [Feng _et al._ , 2021] Fuli Feng, Weiran Huang, Xiangnan He, Xin Xin, Qifan Wang, and Tat-Seng Chua. Should graph convolution trust neighbors? a simple causal inference method. In _Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval_ , pages 1208–1218, 2021. 

- [Fiore _et al._ , 2019] Ugo Fiore, Alfredo De Santis, Francesca Perla, Paolo Zanetti, and Francesco Palmieri. Using generative adversarial networks for improving classification effectiveness in credit card fraud detection. _Information Sciences_ , 479:448–455, 2019. 

- [Fu _et al._ , 2016] Kang Fu, Dawei Cheng, Yi Tu, and Liqing Zhang. Credit card fraud detection using convolutional neural networks. In _Neural Information Processing: 23rd International Conference, ICONIP 2016, Kyoto, Japan, October 16–21, 2016, Proceedings, Part III 23_ , pages 483–490. Springer, 2016. 

- [Gallicchio and Micheli, 2010] Claudio Gallicchio and Alessio Micheli. Graph echo state networks. In _The 2010 international joint conference on neural networks (IJCNN)_ , pages 1–8. IEEE, 2010. 

- [Guo _et al._ , 2019] Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. Attention based spatialtemporal graph convolutional networks for traffic flow forecasting. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 33, pages 922–929, 2019. 

- [Hamilton _et al._ , 2017] Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. _Advances in neural information processing systems_ , 30, 2017. 

- [Hu _et al._ , 2020] Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. Open graph benchmark: Datasets for machine learning on graphs. _Advances in neural information processing systems_ , 33:22118–22133, 2020. 

- [Ileberi _et al._ , 2022] Emmanuel Ileberi, Yanxia Sun, and Zenghui Wang. A machine learning based credit card fraud detection using the ga algorithm for feature selection. _Journal of Big Data_ , 9(1):1–17, 2022. 

- [Jiang _et al._ , 2016] Meng Jiang, Peng Cui, and Christos Faloutsos. Suspicious behavior detection: Current trends and future directions. _IEEE intelligent systems_ , 31(1):31– 39, 2016. 

- [Jiang _et al._ , 2023] Xinke Jiang, Dingyi Zhuang, Xianghui Zhang, Hao Chen, Jiayuan Luo, and Xiaowei Gao. Uncertainty quantification via spatial-temporal tweedie model for zero-inflated and long-tail travel demand prediction. In _CIKM_ , 2023. 

- [Jiang _et al._ , 2024] Xinke Jiang, Zidi Qin, Jiarong Xu, and Xiang Ao. Incomplete graph learning via attributestructure decoupled variational auto-encoder. In _WSDM_ , 2024. 

- [Li _et al._ , 2015] Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard Zemel. Gated graph sequence neural networks. _arXiv preprint arXiv:1511.05493_ , 2015. 

- [Li _et al._ , 2018] Ruoyu Li, Sheng Wang, Feiyun Zhu, and Junzhou Huang. Adaptive graph convolutional neural networks. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 32, 2018. 

- [Li _et al._ , 2022] Rongfan Li, Ting Zhong, Xinke Jiang, Goce Trajcevski, Jin Wu, and Fan Zhou. Mining spatio-temporal 

relations via self-paced graph contrastive learning. In _SIGKDD_ , 2022. 

- [Liu _et al._ , 2018] Ziqi Liu, Chaochao Chen, Xinxing Yang, Jun Zhou, Xiaolong Li, and Le Song. Heterogeneous graph neural networks for malicious account detection. In _Proceedings of the 27th ACM international conference on information and knowledge management_ , pages 2077– 2085, 2018. 

- [Liu _et al._ , 2020] Zhiwei Liu, Yingtong Dou, Philip S Yu, Yutong Deng, and Hao Peng. Alleviating the inconsistency problem of applying graph neural network to fraud detection. In _Proceedings of the 43rd international ACM SIGIR conference on research and development in information retrieval_ , pages 1569–1572, 2020. 

- [Liu _et al._ , 2021] Yang Liu, Xiang Ao, Zidi Qin, Jianfeng Chi, Jinghua Feng, Hao Yang, and Qing He. Pick and choose: a gnn-based imbalanced learning approach for fraud detection. In _Proceedings of the web conference 2021_ , pages 3168–3177, 2021. 

- [Liu _et al._ , 2022] Yuejiang Liu, Riccardo Cadei, Jonas Schweizer, Sherwin Bahmani, and Alexandre Alahi. Towards robust and adaptive motion forecasting: A causal representation perspective. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 17081–17092, 2022. 

- [Maes _et al._ , 2002] Sam Maes, Karl Tuyls, Bram Vanschoenwinkel, and Bernard Manderick. Credit card fraud detection using bayesian and neural networks. In _Proceedings of the 1st international naiso congress on neuro fuzzy technologies_ , volume 261, page 270, 2002. 

- [McAuley and Leskovec, 2013] Julian John McAuley and Jure Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. In _Proceedings of the 22nd international conference on World Wide Web_ , pages 897–908, 2013. 

- [Pearl and Mackenzie, 2018] Judea Pearl and Dana Mackenzie. _The book of why: the new science of cause and effect_ . Basic books, 2018. 

- [Pearl, 2009] Judea Pearl. _Causality_ . Cambridge university press, 2009. 

- [Rayana and Akoglu, 2015] Shebuti Rayana and Leman Akoglu. Collective opinion spam detection: Bridging review networks and metadata. In _Proceedings of the 21th acm sigkdd international conference on knowledge discovery and data mining_ , pages 985–994, 2015. 

- [S¸ahin and Duman, 2011] Yusuf G S¸ahin and Ekrem Duman. Detecting credit card fraud by decision trees and support vector machines. 2011. 

- [Scarselli _et al._ , 2008] Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini. The graph neural network model. _IEEE transactions on neural networks_ , 20(1):61–80, 2008. 

- [Shi _et al._ , 2020] Yunsheng Shi, Zhengjie Huang, Shikun Feng, Hui Zhong, Wenjin Wang, and Yu Sun. Masked label prediction: Unified message passing model 

for semi-supervised classification. _arXiv preprint arXiv:2009.03509_ , 2020. 

- [Veliˇckovi´c _et al._ , 2017] Petar Veliˇckovi´c, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. _arXiv preprint arXiv:1710.10903_ , 2017. 

- [Wang _et al._ , 2019] Daixin Wang, Jianbin Lin, Peng Cui, Quanhui Jia, Zhen Wang, Yanming Fang, Quan Yu, Jun Zhou, Shuang Yang, and Yuan Qi. A semi-supervised graph attentive network for financial fraud detection. In _2019 IEEE International Conference on Data Mining (ICDM)_ , pages 598–607. IEEE, 2019. 

- [Wang _et al._ , 2020] Yiwei Wang, Wei Wang, Yuxuan Liang, Yujun Cai, Juncheng Liu, and Bryan Hooi. Nodeaug: Semi-supervised node classification with data augmentation. In _Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , pages 207–217, 2020. 

- [Wu _et al._ , 2019] Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, and Chengqi Zhang. Graph wavenet for deep spatial-temporal graph modeling. _arXiv preprint arXiv:1906.00121_ , 2019. 

- [Wu _et al._ , 2020] Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long, Chengqi Zhang, and S Yu Philip. A comprehensive survey on graph neural networks. _IEEE transactions on neural networks and learning systems_ , 32(1):4– 24, 2020. 

- [Xiang _et al._ , 2022] Sheng Xiang, Dawei Cheng, Chencheng Shang, Ying Zhang, and Yuqi Liang. Temporal and heterogeneous graph neural network for financial time series prediction. In _Proceedings of the 31st ACM International Conference on Information & Knowledge Management_ , pages 3584–3593, 2022. 

- [Xiang _et al._ , 2023] Sheng Xiang, Mingzhi Zhu, Dawei Cheng, Enxia Li, Ruihui Zhao, Yi Ouyang, Ling Chen, and Yefeng Zheng. Semi-supervised credit card fraud detection via attribute-driven graph representation. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 37, pages 14557–14565, 2023. 

- [Xu _et al._ , 2018] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? _arXiv preprint arXiv:1810.00826_ , 2018. 

- [Yan _et al._ , 2018] Sijie Yan, Yuanjun Xiong, and Dahua Lin. Spatial temporal graph convolutional networks for skeleton-based action recognition. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 32, 2018. 

- [Zhang _et al._ , 2019] Yiming Zhang, Yujie Fan, Yanfang Ye, Liang Zhao, and Chuan Shi. Key player identification in underground forums over attributed heterogeneous information network embedding framework. In _Proceedings of the 28th ACM international conference on information and knowledge management_ , pages 549–558, 2019. 

- [Zhuang and Ma, 2018] Chenyi Zhuang and Qiang Ma. Dual graph convolutional networks for graph-based semi- 

supervised classification. In _Proceedings of the 2018 world wide web conference_ , pages 499–508, 2018. 

