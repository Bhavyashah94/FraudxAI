---
title: "Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection (THGT-FD)"
authors: "yan"
year: 2026
arxiv_id: "2609.07100"
original_file: "2609.07100.pdf"
pdf_path: "docs/papers\2026_yan_temporal_heterogeneous_graph_transf.pdf"
---

# Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection (THGT-FD)

**Authors:** Yan et al.  
**Year:** 2026 | **arXiv:** [`2609.07100`](https://arxiv.org/abs/2609.07100)  
**Local PDF:** [`2026_yan_temporal_heterogeneous_graph_transf.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2026_yan_temporal_heterogeneous_graph_transf.pdf)

---

# **Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection** 

Qinwen Yan 

florayan@g.ucla.edu 

University of California, Los Angeles Los Angeles, California, USA 

## **Abstract** 

Credit card fraud detection typically relies on tabular features, while repeated attributes can also provide useful relational signals. This paper proposes THGT-FD, a Temporal Heterogeneous Graph Transformer for Fraud Detection. Each transaction is represented using one transaction token and six types of relation tokens and incorporates Time2Vec encoding into the transaction representation. A Transformer learns the interactions among these tokens within each individual transaction and then outputs a fraud probability. Experiments were conducted on 150,000 transactions sampled from the IEEE-CIS Fraud Detection dataset and chronologically partitioned according to TransactionDT. On the test set, THGT-FD achieved an AUC-ROC of 0.8536, an average precision of 0.4164, and a Recall@5% of 0.4708. The class-weighted histogram-based gradient-boosting baseline achieved an AUC-ROC of 0.8722. The results indicate that relation tokens provide useful information for fraud-risk ranking, although the current model does not yet incorporate entity-level historical aggregation. 

## **Keywords** 

fraud detection, heterogeneous graph, Transformer, Time2Vec, class imbalance 

## **1 Introduction** 

The continued expansion of online payments has placed increasing pressure on financial institutions to identify fraudulent transactions. Fraudulent transactions usually account for a small proportion of all transactions and may closely resemble legitimate ones. Fraud detection models that rely solely on individual transaction records, such as transaction amounts, often struggle to detect risk in a timely manner. Some risk patterns will not become apparent until repeated attributes associated with transactions are considered. Therefore, effectively leveraging relational signals in high-dimensional transaction data has become an important research problem in credit card fraud detection [1–3]. 

The IEEE-CIS Fraud Detection dataset provides a challenging experimental setting for solving this problem [4]; it contains many high-dimensional anonymized variables and substantial missing data. Recent studies on this benchmark have consequently examined high-cardinality categorical encoders and generative priors for noisy, imbalanced transactions [5, 6]. Gradient-boosting models can effectively capture nonlinear interactions, making them strong baselines for tabular data [7–9]. However, these models mostly generate predictions from individual transaction records. Although repeated attributes can be encoded as categorical features, their underlying relational meaning is only indirectly represented. More 

explicit relational information generally requires manually engineered aggregation features [10]. 

Graph neural networks provide an alternative approach to modeling transaction relationships. GCN and GraphSAGE learn node representations by aggregating information from neighboring nodes [11, 12]. Network-based fraud detection, R-GCN, and heterogeneous graph transformers further account for relational structure or differences among relation types [13–15]. Nevertheless, in anonymized transaction data, repeated values do not necessarily correspond to verified real-world entities. Connections with ambiguous meanings may reduce representation quality, while constructing a complete transaction graph can substantially increase computational costs. Temporal modeling introduces an additional challenge, as fraud risk may evolve with transaction order and may also be influenced by the pace of transaction activity; recent financial-risk studies have addressed related dependencies using improved sequence models and joint Transformer–graph architectures [16, 17]. 

Here, we propose THGT-FD, a Temporal Heterogeneous GraphToken Transformer for credit card fraud detection. Each transaction is represented by one transaction token and six relation tokens derived from anonymized fields. Time2Vec is used to encode the relative temporal position of each transaction [18], while a Transformer encoder learns interactions between the transaction token and relation tokens [19]. Using the IEEE-CIS dataset as a case study, model performance is evaluated with fraud-risk ranking metrics, with a class-weighted histogram-based gradient-boosting model serving as the baseline. Overall, this study presents a compact approach to modeling relational information in anonymized transaction data, thereby improving the framework’s ability to capture evolving behavioral patterns and support more robust fraud detection. 

## **2 Method** 

## **2.1 Data Processing and Relation Tokens** 

The transaction table contains the target label, TransactionDT, TransactionAmt, product codes, card attributes, and address attributes. The identity table contains device and browser information. The merged data are temporally divided into training, validation, and test sets. All preprocessing parameters are estimated from the training set. 

Features whose missing rates exceed a predefined threshold are removed. Numerical features are imputed with training-set medians and standardized using training-set means and standard deviations. Categorical features not used to construct relation tokens are frequency-encoded. For a categorical value _𝑐_ , the encoding is 

1 

Qinwen Yan 

defined as 

**Table 1: Pilot experimental setting on the IEEE-CIS dataset.** 



where _𝑁_ train ( _𝑐_ ) denotes the frequency of _𝑐_ in the training set. Relative day and hour features are also derived from TransactionDT. 

Six relation types are constructed. The card relation is jointly defined by card1–card6, and the address relation by addr1 and addr2. The product relation is defined by ProductCD. Purchaser and recipient email domains form two separate relations. The device relation is jointly defined by DeviceType and DeviceInfo. 

Each relation value is mapped to an integer identifier and transformed using a relation-specific embedding table. For relation type _𝑘_ of transaction _𝑖_ , the relation token is computed as 



where _𝑟𝑖_<sup>_𝑘_is the relation identifier, E</sup><sup>_𝑘_is the embedding table for</sup> relation type _𝑘_ , and e _𝑘_<sup>type</sup> is the corresponding type embedding. 

## **2.2 Model Architecture and Training** 

The transaction token is constructed from the processed transaction features and temporal representation. The normalized timestamp _𝑡𝑖_ is encoded using Time2Vec with one linear component and _𝑚_ periodic components: 



The transaction features x _𝑖_ are concatenated with the temporal representation and projected into the hidden space: 



The input sequence Z _𝑖_ consists of one transaction token and six relation tokens in a fixed order. It is processed by a two-layer Transformer encoder with four attention heads per layer. Let H _𝑖_ denote the encoder output. The representation at the first position, H _𝑖_<sup>0, is passed through a multilayer perceptron to estimate the fraud</sup> probability: 



The model is trained using AdamW [20] and class-weighted focal loss [21, 22]. Let _𝑝𝑡_ denote the predicted probability of the ground-truth class. The loss for each sample is defined as 



where _𝛾_ is the focusing parameter and _𝑤_ ( _𝑦_ ) is the class weight. The positive-class weight is computed from the ratio of legitimate to fraudulent transactions in the training set. Model checkpoints are selected according to validation AUC-ROC, and the classification threshold is calibrated on the validation set [23]. 

## **3 Experiment** 

The pilot evaluation demonstrates that THGT-FD can extract informative fraud signals from heterogeneous transaction relations and temporal context. The experiment used 150,000 chronologically ordered IEEE-CIS transactions while preserving the original fraud ratio of 3.499%. This temporal protocol provides a realistic evaluation because the test transactions occur later than those used for model training. 

Given the substantial class imbalance, we focus primarily on AUC-ROC, Average Precision, Recall@1%, and Recall@5%. These 

|Experimental setting|Value|
|---|---|
|Sample size|150,000|
|Fraud ratio|3.499%|
|Training transactions|105,000|
|Validation transactions|22,500|
|Test transactions|22,500|
|Processed transaction features|412|
|Numerical features|390|
|Frequency-encoded categorical features|22|
|Transformer layers|2|
|Attention heads|4|
|Hidden dimension|64|
|Time2Vec dimension|16|
|Epochs|15|



metrics characterize both global ranking quality and fraud coverage under constrained review budgets. F1 and Accuracy are reported as complementary threshold-dependent metrics. Average Precision is especially informative for imbalanced classification [24], while top-ranked recall reflects fraud coverage under constrained investigation capacity [25]. 

THGT-FD achieved an AUC-ROC of 0.8506 on the validation set and 0.8536 on the test set. Its Average Precision reached 0.4475 and 0.4164, respectively. The test Average Precision remains substantially above the positive-class prevalence of 3.499%, showing that THGT-FD effectively concentrates fraudulent transactions near the top of the ranked list. Moreover, the nearly identical validation and test AUC-ROC values indicate stable ranking performance across the temporal split. 

The strongest advantage of THGT-FD appears in the high-risk review setting. On the test set, Recall@1% reached 0.2414, meaning that the highest-risk 1% of transactions contained 24.14% of all fraudulent cases. Recall@5% further increased to 0.4708, indicating that a review queue containing only 5% of the transactions captured nearly half of the fraud. This concentration is particularly valuable in operational environments where investigation resources are limited and analysts must prioritize a small set of high-risk transactions. 

HistGradientBoosting achieved the highest aggregate scores, with a test AUC-ROC of 0.8722 and an Average Precision of 0.4681. Nevertheless, THGT-FD remained highly competitive, with an AUCROC difference of only 0.0186. More importantly, the difference in high-risk retrieval was limited to 0.0265 for both Recall@1% and Recall@5%. These results show that THGT-FD approaches the strong tabular baseline in the practically important task of identifying transactions that warrant immediate review. Validation-stage fusion of a small, diverse set of classifiers offers a complementary direction for improving imbalanced fraud detection [26]. 

This performance is notable because the two models exploit different sources of predictive structure. HistGradientBoosting is well suited to nonlinear interactions and threshold effects in anonymized numerical variables. THGT-FD complements this feature-centric view by explicitly representing card, product, address, email, device, and temporal information as interacting tokens. The model 

2 

Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection 



**Figure 1: Transaction-centered heterogeneous graph representation and prediction pipeline of THGT-FD.** 

**Table 2: Validation and test results for the tabular baseline and THGT-FD.** 

|Model|Split|AUC-ROC|AP|R@1%|R@5%|F1|Accuracy|
|---|---|---|---|---|---|---|---|
|HistGradientBoosting|Validation|0.8652|0.4700|0.2447|0.5155|0.2933|0.8801|
|HistGradientBoosting|Test|**0.8722**|**0.4681**|**0.2679**|**0.4973**|**0.2525**|**0.8595**|
|THGT-FD|Validation|0.8506|0.4475|0.2410|0.4795|0.1371|0.6124|
|THGT-FD|Test|0.8536|0.4164|0.2414|0.4708|0.1315|0.6127|



can therefore evaluate each transaction together with the heterogeneous relational context implied by its repeated attributes. 

The competitive test performance suggests that relation tokens provide a compact and effective mechanism for incorporating relational information without constructing a full transaction graph. Relation-specific embeddings preserve the semantics of different entity types, while self-attention models their interactions with the transaction representation. Time2Vec further introduces a learnable temporal signal, allowing the model to represent both gradual changes and recurring activity patterns along the relative transaction timeline. 

The threshold-dependent results provide an additional opportunity for deployment-oriented improvement. THGT-FD already produces informative risk rankings, as demonstrated by its AUCROC and top-ranked recall. Its binary prediction performance can therefore be further strengthened through probability calibration and validation-based threshold selection. In practice, selecting the threshold according to review capacity may better align the model output with the operational objective than applying a fixed threshold of 0.5. This emphasis on downstream utility is consistent with risk-aware stochastic decision policies and cost-sensitive hierarchical fusion in adjacent financial applications [27, 28]. More broadly, 



**Figure 2: Validation AUC-ROC across THGT-FD training epochs.** 

work on tabular foundation models for discrete choice shows that predictive accuracy alone need not guarantee economically valid decisions and that structural constraints can preserve domainconsistent behavior [29, 30]. 

3 

Qinwen Yan 

The training curve shows rapid initial learning followed by moderate epoch-to-epoch fluctuations. Validation AUC-ROC increased from 0.3623 before optimization to 0.8206 after the first epoch and reached its maximum of 0.8506 at epoch 13. The subsequent decline supports retaining the epoch-13 checkpoint rather than the final training state. 

Focal loss and positive-class weighting contribute to the model’s sensitivity to rare fraudulent transactions. By assigning greater importance to difficult and minority-class examples, these components support the strong fraud coverage observed in the highestrisk review groups. Further tuning of the focal parameter and class weights may provide an even better balance between ranking quality, probability calibration, and threshold-based performance; recent dollar-metric evidence also suggests that class weighting, amountconditioned weighting, and post-training alert reranking can produce different operational trade-offs [31]. 

A particularly promising aspect of THGT-FD is that its current performance is obtained using a compact transaction-centered architecture. The model does not yet require explicit multi-hop graph propagation or historical aggregation across all transactions connected to an entity. Even under this lightweight formulation, it captures meaningful interactions among cards, devices, addresses, email domains, products, and temporal signals. This provides a scalable foundation for extending relational modeling without abandoning the efficiency of token-based processing. 

Entity-level historical aggregation represents a natural next step. Incorporating recent activity associated with a card, device, address, or email domain could enrich each relation token with behavioral context. Such information may strengthen the representation of repeated device use, emerging card-device combinations, and shortterm transaction bursts. Tail-sensitive summaries of extreme activity may also be worth testing, given evidence that jump tail risk can improve prediction in the distinct but related task of financialdistress assessment [32]. Multi-hop relational interactions could further propagate risk information across transactions connected through shared entities. Beyond transaction histories, knowledgeenhanced financial forecasting distinguishes graph-based and nongraph-based context and provides useful designs for fusing external knowledge with historical features [33]. 

The pilot sample may capture only a subset of the recurrence patterns available in the complete IEEE-CIS dataset. Larger-scale training would provide more observations for low-frequency relation values and support more stable entity embeddings. It would also allow the model to learn a broader range of interactions between transaction attributes, temporal behavior, and heterogeneous relations. Under shifts across time periods or deployment populations, sparse causal discovery and graph-domain adaptation could help separate stable signals from domain-specific correlations [34]. Component-level ablations could then quantify the individual contributions of relation tokens, Time2Vec, and attention-based interaction modeling. 

Overall, THGT-FD provides a promising framework for integrating heterogeneous relations and temporal information into transaction fraud detection. It delivers competitive AUC-ROC, strong fraud coverage under restricted review budgets, and stable ranking performance across the temporal split. These findings demonstrate the value of transaction-centered relational modeling and establish 

a strong basis for richer historical aggregation, calibrated decisionmaking, and large-scale evaluation. 

## **4 Conclusion** 

This paper introduced THGT-FD, a temporal heterogeneous Transformer for credit card fraud detection on the IEEE-CIS dataset. Each transaction is encoded as a compact sequence that combines a feature token with a Time2Vec representation. Relation tokens describe the shared entities associated with the transaction. This formulation incorporates relational context while retaining efficient token-based processing. In the pilot experiment, THGT-FD achieved a test AUC-ROC of 0.8536 and captured 47.08% of fraudulent transactions within the highest-risk 5%. These findings demonstrate the viability of temporal heterogeneous relation modeling for riskprioritized fraud screening. The model also remained competitive with a strong class-weighted gradient-boosting baseline. 

Future work will enrich relation tokens with entity histories and rolling temporal statistics. Multi-hop propagation could further support information exchange between transactions connected through shared entities. Full-data training will provide broader relational coverage, while targeted ablations can quantify each component’s contribution. Probability calibration will also align the decision threshold with operational review capacity. 

## **References** 

- [1] Richard J. Bolton and David J. Hand. Statistical fraud detection: A review. _Statistical Science_ , 17(3):235–249, 2002. 

- [2] Andrea Dal Pozzolo, Giacomo Boracchi, Olivier Caelen, Cesare Alippi, and Gianluca Bontempi. Credit card fraud detection: A realistic modeling and a novel learning strategy. _IEEE Transactions on Neural Networks and Learning Systems_ , 29(8):3784–3797, 2018. 

- [3] Johannes Jurgovsky, Michael Granitzer, Konstantin Ziegler, Sylvie Calabretto, Pierre-Edouard Portier, Liyun He-Guelton, and Olivier Caelen. Sequence classification for credit-card fraud detection. _Expert Systems with Applications_ , 100:234– 245, 2018. 

- [4] IEEE Computational Intelligence Society. IEEE-CIS Fraud Detection. Kaggle Competition, 2019. 

- [5] Xiao Han, Jingjing Liu, Moxuan Zheng, Zhen Zhang, and Chenyu Wu. Interpretable vs learned encoders for high-cardinality fraud detection, 2026. 

- [6] Zhen Xu, Kewei Cao, Yihan Zheng, Mingfan Chang, Xinyi Liang, and Jialu Xia. Generative distribution modeling for credit card risk identification under noisy and imbalanced transactions. In _Proceedings of the 2025 6th International Conference on Big Data Economy and Information Management_ , BDEIM ’25, pages 829–836. Association for Computing Machinery, 2026. 

- [7] Jerome H. Friedman. Greedy function approximation: A gradient boosting machine. _The Annals of Statistics_ , 29(5):1189–1232, 2001. 

- [8] Tianqi Chen and Carlos Guestrin. XGBoost: A scalable tree boosting system. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 785–794, 2016. 

- [9] Fabian Pedregosa et al. Scikit-learn: Machine learning in python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. 

- [10] Christopher Whitrow, David J. Hand, Piotr Juszczak, David Weston, and Niall M. Adams. Transaction aggregation as a strategy for credit card fraud detection. _Data Mining and Knowledge Discovery_ , 18(1):30–55, 2009. 

- [11] Thomas N. Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. In _International Conference on Learning Representations_ , 2017. 

- [12] William L. Hamilton, Rex Ying, and Jure Leskovec. Inductive representation learning on large graphs. In _Advances in Neural Information Processing Systems_ , volume 30, 2017. 

- [13] Veronique Van Vlasselaer, Cristián Bravo, Olivier Caelen, Tina Eliassi-Rad, Leman Akoglu, Monique Snoeck, and Bart Baesens. APATE: A novel approach for automated credit card transaction fraud detection using network-based extensions. _Decision Support Systems_ , 75:38–48, 2015. 

- [14] Michael Schlichtkrull, Thomas N. Kipf, Peter Bloem, Rianne van den Berg, Ivan Titov, and Max Welling. Modeling relational data with graph convolutional networks. In _The Semantic Web–ESWC 2018_ , pages 593–607, 2018. 

4 

Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection 

- [15] Ziniu Hu, Yuxiao Dong, Kuansan Wang, and Yizhou Sun. Heterogeneous graph transformer. In _Proceedings of The Web Conference 2020_ , pages 2704–2710, 2020. 

- [16] Zhen Xu, Jialu Xia, Yingnan Yi, Mingfan Chang, and Ziwei Liu. Discrimination of financial fraud in transaction data via improved mamba-based sequence modeling. In _Proceedings of the 2025 International Symposium on Machine Learning and Social Computing_ , MLSC ’25, pages 519–524. Association for Computing Machinery, 2025. 

- [17] Xinyi Liang, Ruizhe Zhou, Yinghao Zhao, Kewei Cao, Mingfan Chang, and Yihan Zheng. Spatiotemporal risk representation learning using transformers and graph structure. In _Proceedings of the 2026 International Conference on Generative Artificial Intelligence and Education_ , GAIE ’26, pages 38–43. Association for Computing Machinery, 2026. 

- [18] Seyed Mehran Kazemi et al. Time2Vec: Learning a vector representation of time. _arXiv preprint arXiv:1907.05321_ , 2019. 

- [19] Ashish Vaswani et al. Attention is all you need. In _Advances in Neural Information Processing Systems_ , volume 30, 2017. 

- [20] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In _International Conference on Learning Representations_ , 2019. 

- [21] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár. Focal loss for dense object detection. In _Proceedings of the IEEE International Conference on Computer Vision_ , pages 2980–2988, 2017. 

- [22] Haibo He and Edwardo A. Garcia. Learning from imbalanced data. _IEEE Transactions on Knowledge and Data Engineering_ , 21(9):1263–1284, 2009. 

- [23] Alexandru Niculescu-Mizil and Rich Caruana. Predicting good probabilities with supervised learning. In _Proceedings of the 22nd International Conference on Machine Learning_ , pages 625–632, 2005. 

- [24] Takaya Saito and Marc Rehmsmeier. The precision-recall plot is more informative than the roc plot when evaluating binary classifiers on imbalanced datasets. _PLOS ONE_ , 10(3):e0118432, 2015. 

_the Operational Research Society_ , 59(7):956–962, 2008. 

   - [26] Xiao Han and Chenyu Wu. Validation-stage combinatorial fusion analysis for imbalanced credit-card fraud detection, 2026. 

   - [27] Zitao Song, Yining Wang, Pin Qian, Sifan Song, Frans Coenen, Zhengyong Jiang, and Jionglong Su. From deterministic to stochastic: An interpretable stochastic model-free reinforcement learning framework for portfolio optimization. _Applied Intelligence_ , 53(12):15188–15203, 2023. 

   - [28] Zhizhuo Kou, Zhiqiang Qian, Zhenghao Zhu, Jiyuan Xin, Yakun Cui, Yuyao Zhang, Yanting Zhang, Haoran Li, Jian Xie, Shuaishuai Gong, Sirui Han, and Yike Guo. Learning to fuse: Cost-sensitive credit assessment via hierarchical multi-agent reinforcement learning. Preprints, 2026. 

   - [29] Yingshuo Wang, Xian Sun, Yanhang Li, Zhichao Fan, and Zexin Zhuang. Auditing and fixing economic validity in tabular foundation models for discrete choice, 2026. 

   - [30] Yingshuo Wang, Xian Sun, Yanhang Li, Zhichao Fan, and Zexin Zhuang. Embedding foundation model predictions in discrete-choice models with structural guarantees, 2026. 

   - [31] Chenyu Wu. Class weighting versus amount conditioning in credit-card fraud detection: A dollar-metric study with a temporal explanation audit, 2026. 

   - [32] Xiaoqun Liu, Yuchen Zhang, Mengqiao Tian, and Youcong Chao. Financial distress and jump tail risk: Evidence from china’s listed companies. _International Review of Economics & Finance_ , 85:316–336, 2023. 

   - [33] Liping Wang, Jiawei Li, Lifan Zhao, Zhizhuo Kou, Xiaohan Wang, Xinyi Zhu, Hao Wang, Yanyan Shen, and Lei Chen. Methods for acquiring and incorporating knowledge into stock price prediction: A survey. _ACM Computing Surveys_ , 58(7):1–37, 2026. 

   - [34] Junyu Luo, Yuhao Tang, Yiwei Fu, Xiao Luo, Zhizhuo Kou, Zhiping Xiao, Wei Ju, Wentao Zhang, and Ming Zhang. Sparse causal discovery with generative intervention for unsupervised graph domain adaptation, 2025. 

- [25] David J. Hand, Christopher Whitrow, Niall M. Adams, Piotr Juszczak, and David Weston. Performance criteria for plastic card fraud detection tools. _Journal of_ 

5 

