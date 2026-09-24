---
title: "Heterogeneous Graph Auto-Encoder for Credit Card Fraud Detection"
authors: "detection"
year: 2024
arxiv_id: "2410.08121"
original_file: "2410.08121.pdf"
pdf_path: "docs/papers\2024_detection_heterogeneous_graph_autoencoder_for.pdf"
---

# Heterogeneous Graph Auto-Encoder for Credit Card Fraud Detection

**Authors:** Detection et al.  
**Year:** 2024 | **arXiv:** [`2410.08121`](https://arxiv.org/abs/2410.08121)  
**Local PDF:** [`2024_detection_heterogeneous_graph_autoencoder_for.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2024_detection_heterogeneous_graph_autoencoder_for.pdf)

---

# Heterogeneous Graph Auto-Encoder for Credit Card Fraud Detection 

Moirangthem Tiken Singh<sup>1</sup> , Rabinder Kumar Prasad<sup>2</sup> , Gurumayum Robert Michael<sup>3</sup> , N K Kaphungkui<sup>4</sup> , N.Hemarjit Singh<sup>5</sup> 

> 1,2Department of Computer Science and Engineering, Dibrugarh University Institute of Engineering and Technology, Dibrugarh University, Dibrugarh, 786004, Assam, India. 

> 3,4,5Department of Electronic and Communication Engineering, Dibrugarh University Institute of Engineering and Technology, Dibrugarh University, Dibrugarh, 786004, Assam, India. 

Contributing authors: tiken.m@dibru.ac.in; rkp@dibru.ac.in; robertmichael@dibru.ac.in; pipizs.kaps@gmail.com; nhsingh@dibru.ac.in; 

#### **Abstract** 

The digital revolution has significantly impacted financial transactions, leading to a notable increase in credit card usage. However, this convenience comes with a trade-off: a substantial rise in fraudulent activities. Traditional machine learning methods for fraud detection often struggle to capture the inherent interconnectedness within financial data. This paper proposes a novel approach for credit card fraud detection that leverages Graph Neural Networks (GNNs) with attention mechanisms applied to heterogeneous graph representations of financial data. Unlike homogeneous graphs, heterogeneous graphs capture intricate relationships between various entities in the financial ecosystem, such as cardholders, merchants, and transactions, providing a richer and more comprehensive data representation for fraud analysis. To address the inherent class imbalance in fraud data, where genuine transactions significantly outnumber fraudulent ones, the proposed approach integrates an autoencoder. This autoencoder, trained on genuine transactions, learns a latent representation and flags deviations during reconstruction as potential fraud. This research investigates two key questions: (1) How effectively can a GNN with an attention mechanism detect and prevent credit card fraud when applied to a heterogeneous graph? (2) How does the efficacy of the autoencoder with attention approach compare to traditional methods? The results are promising, demonstrating that the proposed model outperforms 

1 

benchmark algorithms such as Graph Sage and FI-GRL, achieving a superior AUC-PR of 0.89 and an F1-score of 0.81. This research significantly advances fraud detection systems and the overall security of financial transactions by leveraging GNNs with attention mechanisms and addressing class imbalance through an autoencoder. 

**Keywords:** Credit card fraud detection, Graph Neural Networks, Auto-encoders, Heterogeneous graphs, Class imbalance. 

## **1 Introduction** 

Financial transactions, especially credit card usage, have experienced a surge due to the digital revolution. This has resulted in a vast amount of financial data, empowering companies to comprehend customer behavior and utilize data for decision-making. On the other hand, the convenience that comes with this has a downside - there is a noticeable rise in fraudulent activities. Traditional methods of fraud detection often struggle to keep pace with the evolving nature of these schemes. In order to tackle this challenge, the field of machine learning (ML) has surfaced as a potent tool that can effectively identify and prevent fraudulent transactions [1]. By leveraging ML algorithms, it becomes possible to analyze massive amounts of financial data, identify recurring patterns, and pinpoint potential fraud through anomaly detection. They enable financial institutions to automate the fraud detection process, facilitating real-time monitoring of transactions and activities. To detect fraud effectively, many professionals rely on techniques such as decision trees, random forests, and support vector machines [2, 3]. 

The conventional approaches to detecting fraud often face difficulties in capturing the intrinsic interrelationships that exist within financial data. Transactions typically involve multiple parties, including cardholders, merchants, banks, and various other entities. The representation of financial transactions as a graph enables us to take advantage of the connections among them, thereby enhancing the effectiveness of fraud detection measures. Despite their widespread use, it is important to acknowledge that traditional methods may face difficulties in accurately differentiating between relevant and irrelevant relationships within the graph, thus impacting their ability to effectively detect fraudulent activity. 

Graph Neural Networks (GNNs) excel at processing graph data and utilizing attention mechanisms to focus on the most relevant entities and relationships within the network structure [4]. This makes them well-suited for tasks like fraud detection, where identifying the most critical factors contributing to a transaction’s legitimacy is crucial. By applying attention, the GNN can prioritize information from neighboring nodes (e.g., cardholder’s spending habits, merchant’s location) that are most relevant to understanding the transaction’s nature. This refined focus on critical relationships improves the model’s ability to distinguish between normal transactions and those exhibiting suspicious patterns, potentially indicative of fraud. 

2 

In graph induction learning techniques, two types of graph representations of data are used: homogeneous graph [5] and heterogeneous graph [6]. Financial fraud data, especially involving credit cards, is inherently heterogeneous. It encompasses diverse entities like cardholders, merchants, and transactions, each with distinct attributes and relationships. Homogeneous graphs, which represent entities of the same type, may not fully capture this complexity. In contrast, heterogeneous graphs offer a more comprehensive representation, effectively capturing the multifaceted nature of financial transactions and the intricate relationships between entities within the financial ecosystem. 

For instance, a heterogeneous graph might include nodes representing credit card numbers ( `cc` ~~`n`~~ `um` ), merchants information ( `merchant` ~~`i`~~ `d` ), and transaction numbers ( `transaction` ~~`i`~~ `d` ), with edges connecting them based on the specific relationship (e.g., a transaction between a cardholder and a merchant). This allows us to analyze the network structure and identify suspicious patterns that might be missed by simpler models. For instance, in Figure 1, the relationships between different data points are illustrated. These relationships are often overlooked by homogeneous graph learning algorithms and their variants. 



**Fig. 1** : Relationships between different nodes. 

The varying characteristics of nodes and edges in heterogeneous graph data make it difficult to apply GNNs directly, thereby necessitating a more sophisticated approach for information aggregation than what is typically used for homogeneous graphs. In addition, the effectiveness of supervised learning is often hindered by class imbalance in fraud data. This imbalance is characterized by a significantly smaller number of fraudulent transactions compared to genuine transactions. As a result, traditional supervised learning models struggle to learn effectively from such imbalanced data [7]. 

This work suggests a new approach that effectively handles heterogeneous graph data by leveraging advanced GNN techniques for aggregating information from diverse 

3 

node and edge types. These techniques ensure that the varying attributes and relationships within the graph are adequately captured and utilized in the analysis process. 

Furthermore, to tackle the issue of class imbalance, common techniques such as oversampling and undersampling [8] are used. Balancing class distribution can be achieved through oversampling, which generates more instances of the minority class (fraud transactions), or through undersampling, which reduces instances of the majority class (genuine transactions). Nonetheless, these approaches may be complicated and possess their own limitations. 

To overcome these challenges, this approach integrates an autoencoder (AE) with a decoder that is trained on genuine transactions. By learning a latent representation, the AE can accurately reconstruct these transactions. The ability to detect fraudulent activities in complex heterogeneous graph data is enhanced by flagging deviations from the learned distribution during reconstruction, thereby addressing class imbalance. 

Considering all scenarios discussed, this work aims to answer the following research questions (RQs): 

- **RQ1: Effectiveness of GNNs with Attention for Fraud Detection:** How effectively can GNNs utilizing an attention mechanism detect and prevent credit card fraud when applied to a heterogeneous graph representation that captures the complex interrelationships within the financial ecosystem? 

- **RQ2: Comparison of Autoencoder with Attention vs. Traditional Methods:** How does the proposed autoencoder-based fraud detection approach, which leverages GNNs with attention and is trained on a non-fraudulent transaction graph dataset, compare to traditional methods in terms of accuracy, efficiency, and scalability, especially considering significant class imbalance? 

The methodology consists of several steps, one of which is the processing of a tabular dataset of financial transactions. This dataset is then transformed into a heterogeneous graph. As a result, the graph is subjected to analysis using autoencoders (AE) and graph neural networks (GNNs), which enables the identification of anomalies that can be linked to fraudulent activity. By focusing on the class imbalance problem, the proposed approach effectively tackles the challenge of fraud detection tasks. The results of this work have significant implications for businesses and financial institutions, empowering them to gain valuable insights into customer behavior and enhance their ability to identify and prevent fraudulent transactions. Ultimately, this work contributes to the advancement of fraud detection systems and the overall security of financial transactions in the digital era. 

This paper provides a comprehensive discussion of the relevant literature in Section 2. The problem statement is outlined in Section 3, aiming to address a specific problem. The methodology employed in this research is elucidated in Section 4. The results obtained from this methodology are analyzed and presented in Section 5. Finally, Section 6 concludes the paper by summarizing the key findings and implications. 

4 

## **2 Literature Review** 

In this section, we introduce a range of notable works that cover various topics such as probabilistic graphical models, machine learning algorithms (including deep learning models), and advanced graph neural networks and their various variants. Table 1 provides a summary of the articles related to the proposed model. 

Papers such as [9] and [10] aim to address the problem of fraud detection in credit card transactions by modeling these transactions using a Hidden Markov Model (HMM), a probabilistic graphical model. The primary difference between them lies in their approach: in the first paper, a card-centric HMM is employed to detect abnormalities in transactions, while the latter paper opts for a merchant-centric HMM model. Both methods have the capability to identify fraud in real-time for merchants, operating in conjunction with modern transaction processing systems that handle card transactions. 

Additionally, [11] models credit card transaction sequences using the HMM approach, considering three distinct perspectives: 

(i) Determining whether fraud is present or absent in the sequence. 

(ii) Crafting sequences by fixing either the cardholder or the payment terminal. 

(iii) Constructing sequences based on the spent amounts or the elapsed time between consecutive transactions. The combination of these three binary perspectives results in eight distinct sets of sequences derived from the training dataset of transactions. Each of these sequences is then represented using a Hidden Markov Model (HMM). Subsequently, each HMM assigns a likelihood to a transaction based on its sequence of preceding transactions. These likelihood values serve as additional features for the Random Forest classifier to detect fraud. In brief, this model provides a concept of sequential information flow during credit card transactions as part of a feature for a machine learning model. 

The paper [12] explores the issue of credit card fraud detection and conducts a comparative analysis of three machine learning algorithms: logistic regression, Na¨ıve Bayes, and K-nearest neighbor. To address the class imbalance, the authors utilize different proportions of the dataset and employ a random undersampling technique. They evaluate the algorithms based on various metrics. According to the results, the logistic regression-based model outperforms the prediction models derived from Na¨ıve Bayes and K-nearest neighbor. The paper also suggests that applying undersampling techniques to the data before model development can lead to improved results. In addition, several machine learning algorithms, such as support vector machine (SVM) [13], random forest (RF) [13, 14], AdaBoost, and Majority Voting [15], as well as artificial neural network (ANN) [16, 17], are being explored as models for controlling fraudulent transactions in credit cards. 

To enhance the performance of the above-mentioned models, [18] defines a model in an ML-driven credit card fraud detection system that uses the genetic algorithm (GA) for feature selection. After identifying optimal features, this detection system utilizes a range of ML classifiers, including Decision Tree (DT), Random Forest (RF), Logistic Regression (LR), Artificial Neural Network (ANN), and Naive Bayes (NB). 

5 

While the aforementioned models perform well, a significant class imbalance exists in the credit card fraud dataset, with non-fraudulent transactions vastly outnumbering fraudulent ones. As a result, these models tend to prioritize high precision by predominantly predicting the majority class. To address this issue, several machine learning models (referenced as [19]) employ one or a combination of oversampling and undersampling techniques (as mentioned in [20]). 

The study cited as [21] conducts a comparative investigation of various approaches to address class imbalance. The findings indicate that a combination of oversampling and undersampling methods performs well when applied to ensemble classification models, including AdaBoost, XGBoost, and Random Forest. Deep learning algorithms such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU), combined with a multilayer perceptron, are employed in the studies referenced as [19] and [22]. In [22], the authors use the Hybrid Synthetic Minority Oversampling Technique and Edited Nearest Neighbor (SMOTE-ENN) to balance the distribution of positive (fraud) and negative (non-fraud) instances in the dataset. However, the effectiveness of the SMOTE-ENN technique is crucial, as poor performance in resampling can significantly degrade the model’s overall performance. 

While oversampling and undersampling techniques can address class imbalance, they come with drawbacks like increased computational cost, potential for overfitting, and information loss (as discussed in [8, 23]). Additionally, they can be sensitive to noise [24] and have limited effectiveness for highly imbalanced datasets [25]. Therefore, [25] propose an approach for Chronic Kidney Disease (CKD) prediction using imbalanced data. Their method leverages information gain-based feature selection and a cost-sensitive AdaBoost classifier. However, this approach focuses on spatial data and might not be suitable for graph data due to potential loss of structural information and inadequate feature representation during feature selection. So, such models will often struggle to capture the full picture of fraudulent activity. As noted in [26], many methods focus solely on spatial data points representing financial transactions, neglecting the valuable insights from temporal relationships. This limitation hinders the ability of these models to identify evolving fraud patterns. Furthermore, many existing models rely solely on labeled data for training, restricting their ability to leverage the vast amount of unlabeled data available in real-world credit card transactions [27]. 

To address these issues, an increasing number of researchers are exploring graphbased techniques for fraud detection, as discussed in [26] and [28]. In this approach, datasets are transformed into graphs, providing a better understanding of the relationships among financial transactions. Graph Neural Network (GNN) algorithms, as detailed in [29], are applied to these graph datasets, allowing for efficient data aggregation from neighboring nodes and the extraction of node representations within the graph datasets. Among the popular GNN variants, GraphSAGE [30] and GAT [31] stand out, utilizing sampling methods and attention mechanisms to gather neighbor information. These techniques have shown promising results in the field of fraud detection. Furthermore, the paper [32] introduces an algorithm designed to tackle the class imbalance problem in graph-based fraud detection. It employs an algorithm known as Pick and Choose Graph Neural Network (PC-GNN) to perform imbalanced supervised learning on graphs. The PC-GNN algorithm selects neighbor candidates for each 

6 

node within the sub-graph using a neighborhood sampler. Ultimately, it aggregates information from the chosen neighbors and different relations to derive the final representation of a target node. The paper reports that PC-GNN surpasses state-of-the-art baselines in both benchmark and real-world graph-based fraud detection tasks. 

However, inconsistency issues arise in the aggregation process of GNN models when applied to fraud detection tasks [33]. The aggregation mechanism relies on the assumption that neighbors share similar features and labels. When this assumption breaks down, the aggregation of neighborhood information becomes ineffective in learning node embeddings. 

To address these challenges, researchers in [33] and [34] have employed a multirelational graph, known as a heterogeneous graph, for the classification of financial fraud. In [33], context inconsistency, feature inconsistency, and relation inconsistency in GNN are introduced. To tackle these inconsistencies, the authors propose a new GNN framework called GraphConsis. GraphConsis addresses these issues by combining context embeddings with node features to handle context inconsistency, designing a consistency score to filter inconsistent neighbors and generate corresponding sampling probabilities to address feature inconsistency, and learning relation attention weights associated with the sampled nodes to tackle relation inconsistency. 

In [34], the authors propose semi-supervised methods that operate with heterogeneous graph datasets to address class imbalance issues in online credit loans. This paper utilizes a Graph-Oriented Snorkel approach to incorporate external expert knowledge, ultimately improving the performance of the learning algorithm when dealing with imbalanced datasets. 

Another noteworthy work, [35], introduces a heterogeneous graph-based approach for detecting malicious accounts in financial transactions. The authors present an algorithm called GEM, which adapts to learn discriminative embeddings for various node types. GEM employs an aggregator to capture node patterns within each type and utilizes an attention mechanism to enhance algorithm efficiency. 

In [36], the authors endeavor to design heterogeneous graph embeddings. Their approach incorporates heterogeneous mutual attention and heterogeneous message passing, incorporating key, value, and query vector operations (self-attention mechanism). This work features both a detector and an explainer, capable of predicting the validity of incoming transactions and providing insightful, understandable explanations generated from graphs to aid in subsequent business unit procedures. 

The framework employed in [37] utilizes an algorithm for graph representation learning to create concise numerical vectors that capture the underlying network structure. The authors in this work assess the predictive capabilities of inductive graph representation learning with GraphSage and Fast Inductive Graph Representation Learning algorithms on credit card datasets characterized by significant data imbalance. 

7 

|**Model/Technique**|**Description**|**Strengths**|**Weaknesses**|
|---|---|---|---|
|Card-centric HMM<br>[9]|Focuses on cardholder<br>transaction patterns.|Specific to individual<br>cardholder behavior.|Limited<br>by<br>card-specific<br>anomalies.|
|Merchant-centric<br>HMM [10]|Focuses on merchant<br>transaction patterns.|Captures<br>merchant-<br>specific<br>fraud<br>patterns.|May miss cardholder-<br>specific fraud patterns.|
|HMM + Random<br>Forest [11]|Combines<br>HMM<br>for<br>sequence<br>modeling<br>with<br>Random<br>Forest<br>for classification.|Incorporates<br>sequen-<br>tial<br>information<br>into<br>machine learning.|Complex feature engi-<br>neering required.|
|Logistic Regression<br>[12]|Standard<br>ML<br>algo-<br>rithm<br>for<br>binary<br>classification.|Simplicity,<br>inter-<br>pretability,<br>outperforms<br>Na¨ıve<br>Bayes<br>and<br>KNN<br>in<br>study.|Limited<br>capacity<br>to<br>handle<br>complex<br>pat-<br>terns.|
|Na¨ıve Bayes [12]|Probabilistic<br>classi-<br>fier based on Bayes’<br>theorem.|Fast, easy to imple-<br>ment.|Assumes feature inde-<br>pendence, less effective<br>for complex data.|
||||Computationally|
|K-nearest Neighbor<br>(KNN) [12]|Instance-based<br>learn-<br>ing algorithm.|Simple,<br>effective<br>for<br>small datasets.|expensive, less effective<br>on<br>large/imbalanced<br>datasets.|
|Support<br>Vector<br>Machine<br>(SVM)<br>[13]|Supervised<br>learn-<br>ing<br>model<br>for<br>classification.|Effective<br>in<br>high-dimensional<br>spaces.|Memory-intensive,<br>challenging with large<br>datasets.|
|Random<br>Forest<br>(RF) [13, 14]|Ensemble<br>learning<br>method using multiple<br>decision trees.|High accuracy, robust-<br>ness to overfitting.|May<br>require<br>exten-<br>sive<br>computational<br>resources.|
|AdaBoost [15]|Boosting<br>algorithm<br>combining<br>weak<br>classifiers.|Improves<br>model<br>performance by focus-<br>ing<br>on<br>misclassified<br>instances.|Sensitive to noisy data<br>and outliers.|
|Artificial<br>Neural<br>Network<br>(ANN)<br>[16, 17]|Deep learning models<br>for<br>complex<br>pattern<br>recognition.|Can<br>model<br>complex<br>relationships,<br>high<br>accuracy.|Requires<br>large<br>datasets,<br>com-<br>putationally<br>intensive.|
|Genetic Algorithm<br>(GA) + ML [18]|Uses GA for feature<br>selection,<br>combined<br>with<br>various<br>ML<br>classifiers.|Optimizes feature set<br>for better model per-<br>formance.|Computationally<br>expensive,<br>complex<br>implementation.<br>Continued on next page|



8 

**Table 1 – continued from** **<u>previous page</u>** 

|**Model/Technique**|**Description**|**Strengths**|**Weaknesses**|
|---|---|---|---|
|Hybrid<br>SMOTE-ENN<br>[19, 22]|Combines<br>Synthetic<br>Minority<br>Oversam-<br>pling<br>Technique<br>and<br>Edited<br>Nearest<br>Neighbor<br>for<br>class<br>balancing.|Balances dataset effec-<br>tively, enhances model<br>performance.|Computationally<br>intensive,<br>potential<br>sensitivity to noise.|
|Graph Neural Net-<br>works (GNN) [29]|Leverages graph struc-<br>tures for node repre-<br>sentation and classifi-<br>cation.|Captures<br>relational<br>data effectively, scal-<br>able with GraphSAGE<br>and GAT.|Inconsistency<br>issues<br>in<br>node<br>aggrega-<br>tion,<br>complexity<br>in<br>implementation.|
|PC-GNN [32]|Pick and Choose GNN<br>for imbalanced learn-<br>ing on graphs.|Effective<br>for<br>imbal-<br>anced graph datasets,<br>state-of-the-art<br>performance.|Complex<br>neigh-<br>borhood<br>sampling<br>process.|
|GraphConsis [33]|Addresses<br>context,<br>feature,<br>and<br>rela-<br>tion inconsistencies in<br>GNN.|Enhances node repre-<br>sentation by resolving<br>inconsistencies.|High<br>complexity<br>in<br>designing and training.|
|Heterogeneous<br>Graph Embeddings<br>[36]|Utilizes<br>attention<br>mechanisms and mes-<br>sage passing for diverse<br>node types.|Effective in capturing<br>diverse<br>relationships,<br>provides explainability.|Computationally<br>intensive,<br>complex<br>attention mechanisms.|
|Autoencoder<br>[38, 39]|Neural network model<br>for<br>unsupervised<br>learning,<br>reconstruct-<br>ing inputs to detect<br>anomalies.|Effective for anomaly<br>detection,<br>dimension-<br>ality reduction.|May suffer from over-<br>fitting, requires careful<br>tuning.|
|GEM [35]|Heterogeneous<br>graph-<br>based<br>algorithm<br>for<br>malicious<br>account<br>detection.|Learns<br>discriminative<br>embeddings,<br>utilizes<br>attention mechanisms.|Complexity<br>in<br>implementation<br>and<br>training,<br>may<br>require<br>exten-<br>sive<br>computational<br>resources.|



**Table 1** : Comparison of various models and techniques for fraud detection in credit card transactions. 

While the methods discussed above claim to perform well with unbalanced heterogeneous graph datasets, techniques such as autoencoders and decoders, as presented in [38–40], offer alternative solutions. For instance, [40] successfully addressed imbalanced medical datasets using a modified Sparse Autoencoder (SAE) and Softmax regression for enhanced diagnosis. However, SAEs are less suitable for data with inherent relationships between elements, which is particularly relevant for fraud detection 

9 

in transactional networks, where connections between nodes are crucial for identifying suspicious activity. Similarly, [39] employed a Stacked SAE (SSAE) for credit card default prediction on imbalanced data. Nevertheless, SSAEs, like SAEs, lack the ability to explicitly prioritize information from relevant neighboring nodes. This limitation necessitates a different approach for this work, which leverages a transactional network to represent data and identify fraudulent activities. 

## **3 Problem Statement** 

A heterogeneous graph is a specialized graph data structure that comprises multiple types of nodes and edges, wherein each node or edge is uniquely associated with a distinct type. In essence, it represents a graph in which diverse node and edge types are interconnected. To provide a formal definition, the characteristics of a heterogeneous graph are delineated as follows: 

**Definition 3.1.** _A heterogeneous graph, also known as a heterogeneous information network or heterogeneous network, is mathematically defined as G_ = ( _V, E, T, R, X_ ) _, where:_ 

- _V represents the set of nodes in the graph, and each node v_<sup>_t_</sup> _∈ V is associated with a specific type t ∈ T , where T represents the set of node types._ 

- _E represents the set of edges in the graph, and each edge e_<sup>_r_</sup> _∈ E connects two nodes_ ( _v_<sup>_t_1</sup> _, v_<sup>_t_2</sup> ) _, where t_ 1 _and t_ 2 _are node types, and r ∈ R, where R represents the set of edge types or relationships._ 

- _X_ = _{Xv, Xe} represents attributes of nodes and edges, respectively, where Xv represents the set of node attributes, and each node v_<sup>_t_</sup> _∈ V can have a vector of attributes xvt, and Xe represents the set of edge attributes, where each edge e_<sup>_r_</sup> _∈ E can have a vector of attributes xer ._ 



<!-- Start of picture text -->
e r 2<br>v 5 t 3 v 3 t 2<br>e r 1<br>v 3 t 1 v 3 t 3 v 2 t 1 v 2 t 2<br>v 6 t 3 v 2 t 3<br>v 1 t 3 v 4 t 3<br>v 1 t 1 v 1 t 2<br>er 1<br>er 1 er 2<br>er 2<br>er 1 er 2<br>er 1<br>er 1<br>er 2<br>re 2<br><!-- End of picture text -->

**Fig. 2** : A heterogeneous graph illustrating different types of nodes and edges. 

By adhering to its definition, the financial fraud dataset can be depicted as a heterogeneous graph. These datasets encompass various entities, including customer or credit card numbers, merchants’ names, and transaction numbers. These entities are 

10 

represented as nodes in the graph, denoted by _V_ . Specifically, the nodes _v_<sup>_t_1</sup> , representing ‘customer’, _v_<sup>_t_2</sup> , representing ‘merchants’, and _v_<sup>_t_3</sup> , representing ‘transaction’, encapsulate the essence of this heterogeneous graph. Consequently, these nodes ( _v_<sup>_t_1</sup> , _v_<sup>_t_2</sup> , and _v_<sup>_t_3</sup> ) are distinguished by their respective types. 

The heterogeneous graph depicted in Figure 2 illustrates a network where nodes are categorized into three distinct types: ‘customers’ (in orange), ‘merchants’ (in blue), and ‘transactions’ (in green). Each node type is uniquely identified by an index ( _vi_<sup>_t_),where</sup><sup>_i_indexesdifferentinstancesofcustomers,merchants,andtransactions</sup> within the same type _t_ (e.g., _v_ 1<sup>_t_1forthefirstcustomer,</sup><sup>_v_</sup> 2<sup>_t_1forthesecondcustomer).</sup> The graph captures complex interactions: customers initiate transactions ( _e_<sup>_r_1</sup> ) that involve merchants ( _e_<sup>_r_2</sup> ). Notably, customers can engage in multiple transactions across different merchants, as represented by multiple transaction nodes ( _v_ 1<sup>_t_3</sup><sup>_, v_</sup> 2<sup>_t_3</sup><sup>_, . . . , v_</sup> 6<sup>_t_3).</sup> This structured representation facilitates the analysis of interconnected relationships within heterogeneous networks, essential for understanding dynamics financial transactions. 

**Problem 1.** _For the given graph G_ = ( _V, E, T, R, X_ ) _, the task is to determine whether it can be classified as fraudulent, considering that the transaction associated with the graph represents a fraudulent class._ 

## **4 Methodology** 

The primary objective of this paper is to develop an encoder capable of learning graph embeddings for a given graph _G_ = ( _V, E, T, R, X_ ). This encoder will be specifically designed to effectively capture the complex information present in a heterogeneous graph, including both its structure and its attributes. Subsequently, a decoder function _f_ dec will be introduced to reconstruct the graph. Figure 3 defines the model to be used in this paper. 



**Fig. 3** : Encoder Units and Decoder unit of the model 

In this model, there are _l_ encoder units. The first encoder unit takes ( _D_ ( _d_<sup>_t_</sup> ) _, ϕ, d_<sup>_t_</sup> ) as input, where _D_ ( _d_<sup>_t_</sup> ) represents the source nodes of _d_<sup>_t_</sup> _∈ V_ , and _ϕ_ represents edges _e_<sup>_r_</sup> for each source node to _d_<sup>_t_</sup> . Each encoder unit processes these inputs to produce intermediate representations. The final output of _Encoderl_ is fed into a decoder unit, which is implemented as a deep neural network. This decoder unit utilizes the encoded information to generate _d′t_ . 

Finally, the model will calculate the reconstruction error by comparing the reconstructed graph and the original graph. This error serves as a measure of the dissimilarity between the original input and the reconstructed output. Using this error, a 

11 

threshold for the reconstruction error is established to identify data points that deviate significantly from the normal patterns. Any data point with a reconstruction error that exceeds the threshold is classified as an anomaly, indicating a deviation from expected normal behavior. 

### **4.1 Encoder for Heterogeneous Graph** 

Based on the study by ([41]), a heterogeneous graph encoder for the auto-encoder has been designed (Figure 4). For each destination node _d_<sup>_t_</sup> _∈ V_ and _D_ ( _d_<sup>_t_</sup> ) _∈ V_ , which represents a list of source nodes for _d_<sup>_t_</sup> , the encoding process _f_<sup>enc</sup> is applied as follows: 



Here, _l_ = 1 _,_ 2 _, . . . , EL_ represents the encoder layer with a maximum of _EL_ layers, and the initial values are set as ( _h_<sup>0</sup> _v_<sup>_t_</sup> _, e_<sup>_r_</sup> _, h_<sup>0</sup> _d_<sup>_t_</sup> ) = ( _v_<sup>_t_</sup> _, e_<sup>_r_</sup> _, d_<sup>_t_</sup> ). Additionally, _Lineardt_ : _<u>dim</u>_ R _k →_ R<sup>_dim_</sup> denotes the linear projection. 



**Fig. 4** : Encoder Unit for Heterogeneous Graphs. _e_<sup>_r_1</sup> and _e_<sup>_r_2</sup> denote edges from source nodes _v_ 1<sup>_t_1and</sup><sup>_v_</sup> 2<sup>_t_2todestinationnode</sup><sup>_dt_.At</sup><sup>_l_=0,itrepresentstheinitialencoder</sup> layer, producing _h_<sup>1</sup> _d_<sup>_t_andsoon.</sup><sup>_k_rangesfrom1to</sup><sup>_H_and</sup><sup>_|_signifiesconcentration,</sup><sup>_⊕_</sup> denotes addition, and _⊗_ indicates dot product. 

The encoding process _f_<sup>_enc_</sup> can be broken down as: 



12 

In Equation (2), the graph attention mechanism is used and the graph message to embed the node feature of the descriptor node _dt_ on edges _e_<sup>_r_</sup> . The attention mechanism is defined as follows: 



Inspired by [42], the attention for each edge _e_<sup>_r_</sup> is calculated using _k_ -heads, based on the dot product of the linear projection of _v ∈ D_ ( _d_<sup>_t_</sup> ) and _d_<sup>_t_</sup> , with a matrix _Wr_<sup>_Att_</sup> that depends on the edge, as shown in Equation (4): 



For each attention head _k_ , _LinearSt_<sup>_k_</sup> _h_<sup>_l_</sup> _v_<sup>_−t_1</sup> _h_<sup>_l_</sup> _d_<sup>_−t_1</sup> perform linear � � and _LinearDt_<sup>_k_�</sup> � projections of the source node _v_<sup>_t_</sup> and _d_<sup>_t_</sup> , respectively, as well as their subsequent embedded forms. These projections map from R<sup>_dim_</sup> to R _<u>dimk</u>_ , where<sup>_<u>dim</u>_</sup> _k_ represents the vector dimension for each head. Finally, _Wr_<sup>_Att_</sup> _∈_ R _<u>dimk</u>_<sup>_×_</sup><sup>_<u>dim</u>_</sup> _k_ is a learnable edge matrix for the edge type _r_ connecting between _v_<sup>_t_</sup> and _d_<sup>_t_</sup> . The message passing function for each attention head _k_ is obtained by performing the dot product between the linear projection of the source node _v_<sup>_t_</sup> and a matrix _<u>dim</u> Wr_<sup>_Mssg_</sup> _∈_ R _k_ based on the edge type joining _v_<sup>_t_</sup> and _d_<sup>_t_</sup> . The linear projection is carried out by _LinearMt_<sup>_k_for each type of node, and thus the final projection is mapped</sup> from R<sup>_dim_</sup> to R _<u>dimk</u>_ , as shown in Equation (5): 



Finally, a function called _f_ reparam creates a probabilistic model by remodeling the latent variable _h_<sup>_l_</sup> _d_<sup>_t_usingprobabilisticdistributions,facilitatinggradient-basedopti-</sup> mization. This approach captures uncertainty and generates diverse samples. Following [43], the function is written as follows: 



where _ϵ_ = _N_ (0 _,_ 1) (sampled random noise). 

### **4.2 Decoder For Heterogeneous Graph** 

The graph decoder should account for the heterogeneous nature of the graph _G_ when reconstructing the original structure. It needs to reconstruct the specific types of nodes and edges, ensuring that the reconstructed graph maintains the semantic relationships and attributes associated with each type. This requires incorporating type-specific reconstruction mechanisms into the decoder. 

13 

For each node _d_<sup>_t_</sup> , a node decoder _f_ dec is applied to reconstruct the attributes _d′t_ based on the corresponding node embedding _h_<sup>_l_</sup> _d_<sup>_t_:</sup> 



Here, _d′t_ represents the reconstructed attribute of node _dt_ with the original attribute _h_<sup>0</sup> _d_<sup>_t_.</sup> 

The primary objective of the decoder is to reconstruct the original graph data, which is based on the graph embeddings generated by the encoder. The overall loss function for the autoencoder will be expressed as follows: 



The loss function _L_ represents the sum of losses calculated by the LOSS function between the original graph data and the reconstructed data. 

### **4.3 Algorithm** 

**Algorithm 1** Fraud Detection on a Heterogeneous Graph 

**Require:** Heterogeneous Graph _G_ **Ensure:** ‘Fraud’ or ‘Not Fraud’ 1: **for** _d_<sup>_t_</sup> _∈ G_ **do** 2: ( _h_<sup>0</sup> _v_<sup>_t, er, h_0</sup> _d_<sup>_t_)</sup><sup>_←_(</sup><sup>_vt, er, dt_)</sup> _▷_ Initialization 3: **for** _l ←_ 1 **to** _EL_ **do** _▷_ Message Passing Layers 4: **for** _v_<sup>_t_</sup> _∈ D_ ( _d_<sup>_t_</sup> ) **do** _▷_ Neighborhood of _d_<sup>_t_</sup> 5: _h_<sup>_l_</sup> _d_<sup>_t_= Linear</sup><sup>_dt_�</sup> _f_<sup>enc</sup> ( _h_<sup>_l_</sup> _v_<sup>_−t_1</sup><sup>_, er, hl_</sup> _d_<sup>_−t_1)</sup> � _⊕ h_<sup>0</sup> _d_<sup>_t_</sup> 6: **end for** 7: _h_<sup>_l_</sup> _d_<sup>_t_=</sup><sup>_f_reparam</sup> mean( _h_<sup>_l_</sup> _d_<sup>_t_)</sup><sup>_,_log(</sup><sup>_hl_</sup> _d_<sup>_t_)</sup> _▷_ Reparameterization � � 8: **end for** 9: _d′t_ = _f_ dec( _hld_<sup>_t_)</sup> _▷_ Output Layer 10: **end for** 11: _L_ = LOSS( _d_<sup>_t_</sup> _, d′t_ ) _▷_ Loss Calculation 12: **if** _L <_ Threshold() **then** 13: **return** ‘Non-Fraud’ 14: **else** 15: **return** ‘Fraud’ 16: **end if** 

The algorithm depicted in Algorithm 1, outlines the method for detecting fraud in a heterogeneous graph structure. Here’s a detailed breakdown of each step: 

1. Input (Heterogeneous Graph G): This represents the financial transaction network, containing nodes (customers, merchants, transactions) and edges (interactions) with their respective types. 

14 

2. Output: **“Fraud” or “Not Fraud”** : The algorithm classifies the transaction associated with the input graph as either fraudulent or legitimate. 

3. Algorithm Steps: 

   - For each node _d_<sup>_t_</sup> in the graph _G_ , node _d_<sup>_t_</sup> is initialized with ( _h_<sup>0</sup> _v_<sup>_t, er, h_0</sup> _d_<sup>_t_).It</sup> includes the features of the node itself _h_<sup>0</sup> _d_<sup>_t_,theconnectingedgetype</sup><sup>_er_,andthe</sup> initial representation of the source node _h_<sup>0</sup> _v_<sup>_t_.</sup> 

   - Message Passing Layers (L Layers): 

   - This loop iterates through a predefined number of layers ( _EL_ ) in the GNN architecture. 

   - Within each layer _l_ : 

   - ∗ For each node _v_<sup>_t_</sup> in the neighborhood of the current node _d_<sup>_t_</sup> : 

      - A message function _f_<sup>enc</sup> (Equation 2) aggregates information from the source node’s hidden representation _h_<sup>_l_</sup> _v_<sup>_−t_1,theedgetype</sup><sup>_er_,and</sup> the previous hidden representation of the destination node _h_<sup>_l_</sup> _d_<sup>_−t_1.</sup> The message undergoes a linear transformation with Linear _dt_ as per equations (3-5). 

      - By utilizing the attention mechanism, the messages undergo transformation and are subsequently combined with the initial hidden representation of the destination node _h_<sup>0</sup> _d_<sup>_t_throughelement-wise</sup> addition ( _⊕_ ). 

   - ∗ The message passing happens iteratively for all neighbors of _d_<sup>_t_</sup> . 

   - ∗ The updated hidden representation _h_<sup>_l_</sup> _d_<sup>_t_issubjectedto</sup><sup>_f_reparam(Equation</sup> 1) after message aggregation. Mean and logarithm are utilized in hidden representation to ensure greater stability during training. 

4. Output Layer: The final hidden representation _h_<sup>_l_</sup> _d_<sup>_t_ispassedthroughthedecoder</sup> function _f_ dec (Equation 6) to produce the prediction vector _d′t_ . 

5. Loss Calculation: The difference between the predicted output _d′t_ and the original node feature _d_<sup>_t_</sup> is evaluated using a loss function LOSS. The LOSS function can use a metric such as mean squared error or any other appropriate loss function. 

6. Fraud Classification: A threshold function Threshold() is used to determine the classification based on the calculated loss. If the loss is lower than the threshold (indicating a good fit), the algorithm outputs “Non-Fraud”. Conversely, if the loss is higher than the threshold (indicating a poor fit), it outputs “Fraud”. 

Algorithm 1 explains the entire framework of the model, which is designed to identify if a specific data point is linked to fraudulent behavior, resulting in one of two possible outcomes: ‘Fraud’ or ‘Not Fraud.’ The algorithm calculates a loss value to measure the difference between the original transaction node and its decoded version. The computation of this loss relies on a loss function that has been predetermined. The next step in the process is for the algorithm to compare the resulting loss with a predetermined threshold, once all the calculations have been completed. In the case where the loss falls below the designated threshold, the data point is classified as ‘Not Fraud’. The overall time complexity of the algorithm can be approximated as _O_ ( _nE_ ) 

15 

by summing up these components, with _n_ representing the number of nodes in the graph. 

## **5 Experiment** 

This paper assesses the effectiveness of the proposed model through a series of experiments on credit card fraud datasets and a comparison with other existing machine learning and deep learning models. 

### **5.1 Performance Metrics** 

In order to evaluate the performance of various models, this article employed evaluation metrics that include the precision rate (PR), the recall rate (RR), the ROC curve, and the F1 score. These metrics are defined as follows: 



In this context, true positive (TP) and false positive (FP) indicate the number of correctly and incorrectly predicted instances of fraud, respectively. Conversely, true negative (TN) and false negative (FN) correspond to the count of transactions accurately and inaccurately predicted as non-fraudulent. 

Meanwhile, the ROC curve illustrates the classifier’s ability to differentiate between fraud and non-fraud categories. This curve is created by plotting the true positive rate against the false positive rate at different threshold levels. The AUC, which ranges from 0 to 1, encapsulates the information from the ROC curve. A value of 0 signifies that all classifier predictions are erroneous, while a value of 1 indicates a perfect classifier. 

The F1 score represents the harmonic mean of precision and recall. Precision is the ratio of true positive predictions to the total predicted positives and recall is the ratio of true positive predictions to the total actual positives. It provides a single value that harmonizes precision and recall, facilitating a balanced evaluation of classifier performance. 



Given that the dataset is imbalanced, the F1 score is particularly valuable because it considers both precision and recall. This score provides a straightforward way to assess a classifier’s overall effectiveness in accurately identifying positive instances while minimizing false positives and false negatives. 

Another parameter used to gain insight into the model’s performance is the Precision-Recall curve (AUC-PR) [44]. This metric offers valuable insights, particularly in situations where class distribution is imbalanced [45]. 

16 

### **5.2 Datasets** 

The dataset ([46]) used in this article simulates credit card transactions and includes genuine and fraudulent activities that occurred between January 1, 2019, and December 31, 2020. The data encompass transactions carried out by 1000 customers using credit cards issued by a variety of banks, engaging in transactions with a pool of 800 different merchants. 

|**Types of Dataset**|**Normal Data**|**Abnormal Data**|
|---|---|---|
|Training Dataset|1842743|9651|
|Testing Dataset|553574|2145|



**Table 2** : Distribution of Fraudulent Transactions on Training and Testing Dataset 

Table 2 illustrates the distribution of fraudulent and non-fraudulent transactions in a dataset. It shows the number of occurrences of each type of transaction, with “1” representing fraudulent (Abnormal) transactions and “0” representing non-fraudulent (Normal) ones. This analysis gives an indication of the skewed and unbalanced ratio of fraudulent to non-fraudulent transactions. 

### **5.3 Analysis of Algorithms** 

In the article ([47]), some of the best machine learning algorithms that handle fraud datasets are listed. Here is the list used in the article: 

- Linear Regression 

- Logistic Regression 

- Decision Tree 

- SVM (Support Vector Machine) 

- ANN (Artificial Neural Network) 

- Na¨ıve Bayes 

- DNN (Deep Neural Network) 

- K-Means 

- Random Forest 

- Dimensionality Reduction Algorithms 

- Gradient Boosting (XGB) Algorithms 

These algorithms cover a wide range of machine learning (ML) aspects, including association analysis, clustering, classification, statistical learning, and link mining. They hold a crucial place among the essential topics explored in research and development within the field of machine learning. However, when evaluating these algorithms with datasets, their performance often falls short of expectations due to the inherent imbalance present in the data. 

Table 3 provides the performance metrics for a few machine learning algorithms. The table shows that the F1 score of all machine learning algorithms is too low, suggesting that these algorithms could not handle unbalanced datasets properly. Since 

17 

the F1 score is low and the AUC curve is high for all ML algorithms, it indicates that these algorithms are adept at distinguishing between abnormal and normal data, as evidenced by the high AUC value. However, the F1 score is low due to the models facing challenges in achieving both high precision and high recall, attributed to the imbalanced nature of the data. 

||Performance of Ma|chine learning (|ML) Al|gorithm|s||
|---|---|---|---|---|---|---|
|ML Algorithm|Testing<br>Accuracy|Testing F1<br>Score|Test <br>sion|Preci-|Test<br>Recall|AUC|
|Decision Tree|0_._99|0_._29|0_._22||0_._43|0_._82|
|XGB Classifier|0_._99|0_._33|0_._27||0_._43|**0.96**|
|ANN|0_._99|0_._33|0_._23||0_._32|0_._92|
|Deep NN|0_._99|0_._33|**0.40**||0_._26|0_._81|
|AE|_−_|**0.67**|0_._50||0_._99|0_._52|
|VAE|_−_|**0.67**|0_._50||0_._99|0_._54|
|Sparse AE|_−_|**0.67**|0_._50||0_._99|0_._54|



**Table 3** : Performance Measurement of Few Selected Machine Learning Algorithms 

These scenarios arise when the negative class dominates the dataset, creating a highly imbalanced situation. In such cases, models tend to classify instances as the majority class, resulting in high true negatives and low false positives but at the cost of missing true positives and having low recall. To address the challenges posed by unbalanced data, various algorithms are explored. One of the algorithms under consideration is the autoencoder algorithm. 

The exploration involves simple autoencoders (AE) using deep neural networks and their variations, such as variational autoencoders (VAE) and sparse autoencoders (Sparse AE). Table 3 also shows the performance of the autoencoders. Regardless of the specific type, the model’s performance is evaluated using key metrics. The F1 score, which harmonizes precision and recall, yielded a value of 0.67. This suggests that the models have achieved a reasonable balance between making accurate positive predictions and effectively capturing actual positive instances. Overall, the performance is decent, showing a well-rounded approach. 

However, the narrative changes when examining the Receiver Operating Characteristics (ROC) curve and its corresponding Area Under the Curve (AUC). With an AUC of 0.57, it implies that the models struggle to distinguish between fraud and normal classes. Their ability to classify effectively in this context appears limited and performs only slightly better than random guessing. 

In a deeper dive, the precision achieved by the autoencoder models in the test set is 0.50. This means that roughly half of the abnormal predictions it generates are accurate, while the other half are incorrect. On the other hand, the recall rate is impressive at 0.99. This means that the models excel at identifying almost all the actual abnormal instances present in the dataset. 

In summary, while autoencoder models demonstrate balanced performance in terms of the F1 score, with commendable recall and reasonable precision, the AUC 

18 

score and precision rates indicate room for improvement. Enhancing the discriminatory capacity of models and refining their positive prediction accuracy could be areas of focus to further elevate their performance in classification tasks. 

### **5.4 Analysis of the Proposed Model** 

|**Parameter Name**|**Value**|
|---|---|
|Size of Hidden Layers|64|
|Number of heads (_H_)|16|
|Number of Layers for the Encoder (_l_)|124|
|Number of Layers for the Decoder|64|
|Dropout Rate|0_._4|
|Regularization Rate|0_._01|



**Table 4** : Values for different parameters used in the model. 

After tuning the parameters for different hyperparameters, the performance of the model is represented as shown in Figure 5. Finally, the proposed model uses the parameters defined in Table 5 to evaluate the model’s performance. 

In Figure 5a, the training loss is compared with the validation loss for positive (fraud) and negative datasets. This plot provides insight into how effectively the model handles overfitting and underfitting of the data. The model, using the parameters from Table 5, demonstrates immunity to both overfitting and underfitting, effectively managing these issues. Figure 5b illustrates the loss distribution (histogram) generated by the model from the dataset. This distribution shows the loss values for both positive and negative data in the dataset. The figure reveals that the loss for negative instances is concentrated between 0 _._ 004 and 0 _._ 005, while the loss for positive instances is distributed beyond 0 _._ 006. 

Figure 5c defines the model’s F1 score versus the classification threshold value. From the figure, it can be seen that the F1 score reaches its highest value of 0.81 at a loss value of 0.005. Additionally, the ROC curve was plotted based on the threshold, resulting in the ROC curve shown in Figure 5d, and an AUC of 0.85 was obtained for the model. 

The Precision-Recall (PR) curve (Figure 5e) compares the performance of four algorithms: the Proposed Model, Graph Sage [37], FI-GRL [37], and Baseline [37]. The Proposed Model exhibits the highest performance with an AUC-PR of 0.89, indicating the best balance between precision and recall. Graph Sage follows closely with an AUC-PR of 0.87, showing strong but slightly inferior performance compared to the Proposed Model. Both FI-GRL and the Baseline models have an AUC-PR of 0.84, indicating moderate performance and similar effectiveness in maintaining precision and recall. Overall, the Proposed Model stands out as the most effective, followed by Graph Sage, with FI-GRL and Baseline performing similarly but less effectively. 

Again, Table 5 summarizes the performance of various graph learning algorithms on metrics including AUC-PR, F1-Score, and ROC-AUC. The proposed model achieves 

19 



<!-- Start of picture text -->
Distribution of Validation Loss for Negative and Positive Cases<br>Negative Cases<br>Positive Cases<br>800<br>600<br>400<br>200<br>0<br>0.004 0.005 0.006 0.007 0.008 0.009<br>Validation Loss<br>(a) Training loss and evaluation loss. (b) Distribution of validation loss.<br>F-score vs. Threshold Value Receiver Operating Characteristic (ROC) Curve<br>0.8 1.0<br>0.7<br>0.8<br>0.6<br>0.5 0.6<br>0.4<br>0.3 0.4<br>0.2<br>0.2<br>0.1<br>0.0 0.0 ROC curve (AUC = 0.85)<br>0.000 0.002 0.004 0.006 0.008 0.0 0.2 0.4 0.6 0.8 1.0<br>Threshold Value False Positive Rate (1 - Specificity)<br>(c) F Score vs Threshold graph. (d) ROC curve<br>Precision-Recall Curve<br>1.0<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>Proposed Model (AUC-PR = 0.89)<br>0.3 Graph Sage (AUC-PR = 0.87)<br>FI-GRL (AUC-PR = 0.84)<br>Baseline (AUC-PR = 0.84)<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Recall<br>(e) Precision-Recall curve of the model<br>with an AUC-PR of 0.89.<br>Frequency<br>F-score<br>True Positive Rate (Sensitivity)<br>Precision<br><!-- End of picture text -->

**Fig. 5** : Performance evaluations of the proposed model. 

the highest AUC-PR (0.89) and F1-Score (0.81) but has a lower ROC-AUC (0.85) compared to Graph Sage and XBoost, which achieve a ROC-AUC of 0.93. 

20 

|Perfor|mance of Graph L|earning Algotihm|s|
|---|---|---|---|
|**Graph Algorithm**|**AUC-PR**|**F1 Score**|**ROC-AUC**|
|Proposed Model|**0.89**|**0.81**|0.85|
|Graph<br>Sage<br>and<br>XBoost ([37])|0.86|0.80|**0.93**|
|FI-GRL([37])|0.84|0_._70|0_._92|
|Baseline([37])|0.84|0_._74|0_._91|



**Table 5** : Performance Measurement of Graph Learning Algorithms. AUC-PR provides sufficient information to assess performance due to the imbalanced nature of the dataset used. 



<!-- Start of picture text -->
Performance of Machine Learning and Graph Learning Algorithms<br>Proposed Model<br>Graph Sage and XBoost<br>FI- GRL<br>AUC-PR Baseline<br>Decision Tree<br>XGB Classifier<br>ANN<br>Deep NN<br>F1  Score<br>ROC-AUC<br><!-- End of picture text -->

**Fig. 6** : Performance Radar Chart. It compares several machine learning (ML) algorithms, including the Proposed Algorithm, using three key metrics: F1 Score, AUC-PR (Area Under the Precision-Recall Curve), and ROC-AUC (Area Under the Receiver Operating Characteristic Curve). This visualization highlights the strengths and weaknesses of each algorithm across these important performance metrics, providing a comprehensive view of their comparative effectiveness. 

Finally, Figure 6 showcases the following algorithms: Proposed Model, Graph Sage and XBoost, FI-GRL, Baseline, Decision Tree, XGB Classifier, ANN (Artificial Neural Network), and Deep NN (Deep Neural Network). This radar chart highlights the exceptional performance of the Proposed Model, with high scores in F1 score, AUCPR, and ROC-AUC, demonstrating a strong and balanced performance. 

While Graph Sage and XBoost show great performance in class discrimination with high ROC-AUC, their AUC-PR is slightly lower, suggesting a trade-off when dealing with imbalanced datasets. Both FI-GRL and Baseline demonstrate strong 

21 

classification performance with high ROC-AUC, but they may prioritize precision or recall at the expense of balance, resulting in a lower F1 score. 

The Decision Tree and XGB Classifier face challenges in their competition, as the Decision Tree exhibits overall weakness, and the XGB Classifier lacks balance despite its strong classification ability. Finally, ANN and Deep NN exhibit moderate performance across all metrics, lacking a clear specialization. With its balanced performance, the Proposed Model stands out as a strong candidate for general use, unlike other algorithms that focus on specific needs. 

## **6 Conclusion** 

In this paper, a novel approach is introduced that incorporates a heterogeneous graph autoencoder with an attention mechanism, designed to extract valuable information from the intricate graph structure. The encoded node information, produced by the encoder, is harnessed to create a probabilistic distribution using a variational autoencoder model, allowing for the capture of uncertainty and the generation of diverse samples of the embedded nodes. This model effectively addresses the first research question. Subsequently, the output of the encoder undergoes further processing by a deep learning neural network, leading to the regeneration of the original node embeddings. This process significantly enhances the embedded representations of the nodes within the heterogeneous graph. The errors generated by the decoder are carefully observed and recorded, playing a crucial role in classifying fraudulent from non-fraudulent transactions. To facilitate this, a straightforward search algorithm is employed to determine an efficient threshold, effectively addressing the second research question. The work is rigorously benchmarked against a selection of state-ofthe-art machine learning algorithms and compared with established methods, such as Graph-Sage and FI-GRL, serving as baselines. Remarkably, the approach consistently demonstrates superior performance, outperforming these baseline methods and thus effectively addressing the third research question. However, the model currently lacks the capability to effectively handle temporal data relationships, which is essential for addressing the dynamic nature of datasets, particularly in the context of fraudulent transactions. This issue will be a focal point for future research and development. 

## **Statements and Declarations** 

### **Competing Interests** 

The authors declare that there are no competing interests associated with this research work. 

### **Funding** 

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. 

22 

### **Informed Consent** 

Informed consent was obtained from all individual participants included in the study. 

### **Data Availability** 

The datasets generated and/or analyzed during the current study are available in upon reasonable request from the corresponding author. 

## **References** 

- [1] Ali, A. _et al._ Financial fraud detection based on machine learning: A systematic literature review. _Applied Sciences_ **12** , 9637 (2022). URL http://dx.doi.org/10. 3390/app12199637. 

- [2] Hussain, S. S., Reddy, E. S. C., Akshay, K. G. & Akanksha, T. _Fraud detection in credit card transactions using svm and random forest algorithms_ , 1013–1017 (IEEE, 2021). 

- [3] Jing, R. _et al. A gnn-based few-shot learning model on the credit card fraud detection_ , 320–323 (2021). 

- [4] Zhou, J. _et al._ Graph neural networks: A review of methods and applications. _AI open_ **1** , 57–81 (2020). 

- [5] Bo, D. _Homogeneous Graph Neural Networks_ , 27–59 (Springer International Publishing, Cham, 2023). URL https://doi.org/10.1007/978-3-031-16174-2 ~~3~~ . 

- [6] Shi, C., Wang, X. & Yu, P. S. _Structure-Preserved Heterogeneous Graph Representation_ , 29–69 (Springer Singapore, Singapore, 2022). URL https://doi.org/10. 1007/978-981-16-6166-2 ~~3~~ . 

- [7] Cheah, P. C. Y., Yang, Y. & Lee, B. G. Enhancing financial fraud detection through addressing class imbalance using hybrid smote-gan techniques. _International Journal of Financial Studies_ **11** (2023). URL https://www.mdpi.com/ 2227-7072/11/3/110. 

- [8] Brownlee, J. How to combine oversampling and undersampling for imbalanced classification. https://machinelearningmastery.com/ combine-oversampling-and-undersampling-for-imbalanced-classification/ (2021). Accessed: October, 2023. 

- [9] Srivastava, A., Kundu, A., Sural, S. & Majumdar, A. Credit card fraud detection using hidden markov model. _IEEE Transactions on Dependable and Secure Computing_ **5** , 37–48 (2008). 

- [10] Robinson, W. N. & Aria, A. Sequential fraud detection for prepaid cards using hidden markov model divergence. _Expert Systems with Applications_ 

23 

**91** , 235–251 (2018). URL https://www.sciencedirect.com/science/article/pii/ S0957417417305894. 

- [11] Lucas, Y. _et al._ Towards automated feature engineering for credit card fraud detection using multi-perspective hmms. _Future Generation Computer Systems_ **102** , 393–402 (2020). URL https://www.sciencedirect.com/science/article/pii/ S0167739X19300664. 

- [12] Itoo, F., Meenakshi & Singh, S. Comparison and analysis of logistic regression, na¨ıve bayes and knn machine learning algorithms for credit card fraud detection. _International Journal of Information Technology_ **13** , 1503–1511 (2021). URL https://doi.org/10.1007/s41870-020-00430-y. 

- [13] Saddam Hussain, S. K., Sai Charan Reddy, E., Akshay, K. G. & Akanksha, T. _Fraud detection in credit card transactions using svm and random forest algorithms_ , 1013–1017 (2021). 

- [14] Lin, T.-H. & Jiang, J.-R. Credit card fraud detection with autoencoder and probabilistic random forest. _Mathematics_ **9** (2021). URL https://www.mdpi. com/2227-7390/9/21/2683. 

- [15] Randhawa, K., Loo, C. K., Seera, M., Lim, C. P. & Nandi, A. K. Credit card fraud detection using adaboost and majority voting. _IEEE Access_ **6** , 14277–14284 (2018). 

- [16] RB, A. & KR, S. K. Credit card fraud detection using artificial neural network. _Global Transitions Proceedings_ **2** , 35–41 (2021). URL https://www.sciencedirect. com/science/article/pii/S2666285X21000066. 1st International Conference on Advances in Information, Computing and Trends in Data Engineering (AICDE - 2020). 

- [17] Akande, O. N., Misra, S., Akande, H. B., Oluranti, J. & Damasevicius, R. Florez, H. & Pollo-Cattaneo, M. F. (eds) _A supervised approach to credit card fraud detection using an artificial neural network_ . (eds Florez, H. & Pollo-Cattaneo, M. F.) _Applied Informatics_ , 13–25 (Springer International Publishing, Cham, 2021). 

- [18] Ileberi, E., Sun, Y. & Wang, Z. A machine learning based credit card fraud detection using the ga algorithm for feature selection. _Journal of Big Data_ **9** , 24 (2022). URL https://doi.org/10.1186/s40537-022-00573-8. 

- [19] Mienye, I. D. & Sun, Y. A deep learning ensemble with data resampling for credit card fraud detection. _IEEE Access_ **11** , 30628–30638 (2023). 

- [20] Branco, P., Torgo, L. & Ribeiro, R. P. A survey of predictive modeling on imbalanced domains. _ACM Comput. Surv._ **49** (2016). URL https://doi.org/10.1145/ 2907070. 

24 

- [21] Amit Singh, R. K. R. & Tiwari, A. Credit card fraud detection under extreme imbalanced data: A comparative study of data-level algorithms. _Journal of Experimental & Theoretical Artificial Intelligence_ **34** , 571–598 (2022). URL https://doi.org/10.1080/0952813X.2021.1907795. 

- [22] Esenogho, E., Mienye, I. D., Swart, T. G., Aruleba, K. & Obaido, G. A neural network ensemble with feature engineering for improved credit card fraud detection. _IEEE Access_ **10** , 16400–16407 (2022). 

- [23] Yang, F. _et al._ A hybrid sampling algorithm combining synthetic minority oversampling technique and edited nearest neighbor for missed abortion diagnosis. _BMC Medical Informatics and Decision Making_ **22** , 344 (2022). URL https: //doi.org/10.1186/s12911-022-02075-2. 

- [24] Zhang, Z.-L., Peng, R.-R., Ruan, Y.-P., Wu, J. & Luo, X.-G. Esmote: an overproduce-and-choose synthetic examples generation strategy based on evolutionary computation. _Neural Computing and Applications_ **35** , 6891–6977 (2023). URL https://doi.org/10.1007/s00521-022-08004-8. 

- [25] Ebiaredoh-Mienye, S. A., Swart, T. G., Esenogho, E. & Mienye, I. D. A machine learning method with filter-based feature selection for improved prediction of chronic kidney disease. _Bioengineering_ **9** , 350 (2022). 

- [26] Cheng, D., Wang, X., Zhang, Y. & Zhang, L. Graph neural network for fraud detection via spatial-temporal attention. _IEEE Transactions on Knowledge and Data Engineering_ **34** , 3800–3813 (2022). 

- [27] Sheng, X., Li, Y., Liu, Z. & Sun, M. _Semi-supervised credit card fraud detection via attribute-driven graph representation_ , Vol. 37, 1234–1241 (2023). 

- [28] Ling, Y., Zhang, R., Cen, M., Wang, X. & Jiang, M. _Cost-sensitive heterogeneous integration for credit card fraud detection_ , 750–757 (2021). 

- [29] Zhang, B. _et al._ The expressive power of graph neural networks: A survey (2023). 2308.08235. 

- [30] Hamilton, W. L., Ying, R. & Leskovec, J. Inductive representation learning on large graphs (2018). 1706.02216. 

- [31] Veliˇckovi´c, P. _et al._ Graph attention networks (2018). 1710.10903. 

- [32] Liu, Y. _et al. Pick and choose: A gnn-based imbalanced learning approach for fraud detection_ , WWW ’21, 3168–3177 (Association for Computing Machinery, New York, NY, USA, 2021). URL https://doi.org/10.1145/3442381.3449989. 

- [33] Liu, Z., Dou, Y., Yu, P. S., Deng, Y. & Peng, H. _Alleviating the inconsistency problem of applying graph neural network to fraud detection_ , SIGIR ’20, 1569–1572 

25 

(Association for Computing Machinery, New York, NY, USA, 2020). URL https: //doi.org/10.1145/3397271.3401253. 

- [34] Tang, H., Wang, C., Zheng, J. & Jiang, C. Enabling graph neural networks for semi-supervised risk prediction in online credit loan services. _ACM Trans. Intell. Syst. Technol._ (2023). URL https://doi.org/10.1145/3623401. Just Accepted. 

- [35] Liu, Z. _et al. Heterogeneous graph neural networks for malicious account detection_ , CIKM ’18, 2077–2085 (Association for Computing Machinery, New York, NY, USA, 2018). URL https://doi.org/10.1145/3269206.3272010. 

- [36] Rao, S. X. _et al._ Xfraud: Explainable fraud transaction detection. _Proc. VLDB Endow._ **15** , 427–436 (2021). URL https://doi.org/10.14778/3494124.3494128. 

- [37] Van Belle, R., Van Damme, C., Tytgat, H. & De Weerdt, J. Inductive graph representation learning for fraud detection. _Expert Systems with Applications_ **193** , 116463 (2022). URL https://www.sciencedirect.com/science/article/pii/ S0957417421017449. 

- [38] Tingfei, H., Guangquan, C. & Kuihua, H. Using variational auto encoding in credit card fraud detection. _IEEE Access_ **8** , 149841–149853 (2020). 

- [39] Ebiaredoh-Mienye, S. A., Esenogho, E. & Swart, T. G. Artificial neural network technique for improving prediction of credit card default: A stacked sparse autoencoder approach. _International Journal of Electrical and Computer Engineering_ **11** , 4392 (2021). 

- [40] Ebiaredoh-Mienye, S. A., Esenogho, E. & Swart, T. G. Integrating enhanced sparse autoencoder-based artificial neural network technique and softmax regression for medical diagnosis. _Electronics_ **9** , 1963 (2020). 

- [41] Hu, Z., Dong, Y., Wang, K. & Sun, Y. _Heterogeneous graph transformer_ , WWW ’20, 2704–2710 (Association for Computing Machinery, New York, NY, USA, 2020). URL https://doi.org/10.1145/3366423.3380027. 

- [42] Vaswani, A. _et al._ Guyon, I. _et al._ (eds) _Attention is all you need_ . (eds Guyon, I. _et al._ ) _Advances in Neural Information Processing Systems_ , Vol. 30 (Curran Associates, Inc., 2017). URL https://proceedings.neurips.cc/paper ~~f~~ iles/paper/ 2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf. 

- [43] Kingma, D. P. & Welling, M. An introduction to variational autoencoders. _Foundations and Trends® in Machine Learning_ **12** , 307–392 (2019). URL https://doi.org/10.1561%2F2200000056. 

- [44] Powers, D. M. W. Evaluation: from precision, recall and f-measure to roc, informedness, markedness and correlation. _ArXiv_ **abs/2010.16061** (2011). URL https://api.semanticscholar.org/CorpusID:3770261. 

26 

- [45] Neptune.ai. F1 score, accuracy, roc auc, pr auc: Evaluation metrics you need to know. https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc (2023). Accessed: 2024-05-25. 

- [46] Kartik2112. Credit card transactions fraud detection dataset. Retrieved 2023-0921 from https://www.kaggle.com/datasets/kartik2112/fraud-detection (2021). 

- [47] Arora, V., Leekha, R. S., Lee, K. & Kataria, A. Facilitating user authorization from imbalanced data logs of credit cards using artificial intelligence. _Mobile Information Systems_ **2020** , 8885269 (2020). URL https://doi.org/10.1155/2020/ 8885269. 

27 

