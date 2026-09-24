---
title: "BRIGHT: Graph Neural Networks in Real-Time Fraud Detection"
authors: "unknown"
year: 2022
arxiv_id: "2205.13084"
original_file: "2205.13084.pdf"
pdf_path: "docs/papers\2022_unknown_bright_graph_neural_networks_in_rea.pdf"
---

# BRIGHT: Graph Neural Networks in Real-Time Fraud Detection

**Authors:** Unknown et al.  
**Year:** 2022 | **arXiv:** [`2205.13084`](https://arxiv.org/abs/2205.13084)  
**Local PDF:** [`2022_unknown_bright_graph_neural_networks_in_rea.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_unknown_bright_graph_neural_networks_in_rea.pdf)

---

**BRIGHT - Graph Neural Networks in Real-Time Fraud Detection** 

# Zhichao Han 

# Susie Xi Rao 

Mingxuan Lu Shanghai Jiao Tong University Shanghai, China mingxuan.lu@sjtu.edu.cn 

Swiss Federal Institute of Technology in Zurich (ETHZ) Zurich, Switzerland raox@inf.ethz.ch 

eBay Inc. Shanghai, China zhihan@ebay.com 

Zitao Zhang eBay Inc. Shanghai, China zitzhang@ebay.com 

Yang Zhao eBay Inc. Shanghai, China yzhao5@ebay.com 

Yinan Shan eBay Inc. Shanghai, China yshan@ebay.com 

Ramesh Raghunathan eBay Inc. Shanghai, China raraghunathan@ebay.com 

Ce Zhang Swiss Federal Institute of Technology in Zurich (ETHZ) Zurich, Switzerland ce.zhang@inf.ethz.ch 

Jiawei Jiang School of Computer Science, Wuhan University Wuhan, China jiawei.jiang@whu.edu.cn 

## **ABSTRACT** 

inference), BRIGHT can reduce the P99 latency by >75%. For the inference stage, our speedup is on average 7.8× compared to the traditional GNN. 

Detecting fraudulent transactions is an essential component to control risk in e-commerce marketplaces. Apart from rule-based and machine learning filters that are already deployed in production, we want to enable efficient real-time inference with graph neural networks (GNNs), which is useful to catch multihop risk propagation in a transaction graph. However, two challenges arise in the implementation of GNNs in production. First, future information in a dynamic graph should not be considered in message passing to predict the past. Second, the latency of graph query and GNN model inference is usually up to hundreds of milliseconds, which is costly for some critical online services. To tackle these challenges, we propose a Batch and Real-time Inception GrapH Topology (BRIGHT) framework to conduct an end-to-end GNN learning that allows efficient online real-time inference. 

## **CCS CONCEPTS** 

• **Computing methodologies** → **Neural networks** ; • **Information systems** → **Enterprise applications** ; • **Theory of computation** → _Dynamic graph algorithms_ . 

## **KEYWORDS** 

graph neural networks, fraud detection, heterogeneous graph, dynamic graph, graph inference 

### **ACM Reference Format:** 

Mingxuan Lu, Zhichao Han, Susie Xi Rao, Zitao Zhang, Yang Zhao, Yinan Shan, Ramesh Raghunathan, Ce Zhang, and Jiawei Jiang. 2022. BRIGHT - Graph Neural Networks in Real-Time Fraud Detection. In _Proceedings of the 31st ACM International Conference on Information and Knowledge Management (CIKM ’22), October 17–21, 2022, Atlanta, GA, USA._ ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3511808.3557136 

BRIGHT framework consists of a graph transformation module (Two-Stage Directed Graph) and a corresponding GNN architecture (Lambda Neural Network). The Two-Stage Directed Graph guarantees that the information passed through neighbors is only from the historical payment transactions. It consists of two subgraphs representing historical relationships and real-time links, respectively. The Lambda Neural Network decouples inference into two stages: batch inference of entity embeddings and real-time inference of transaction prediction. Our experiments show that BRIGHT outperforms the baseline models by >2% in average w.r.t. precision. Furthermore, BRIGHT is computationally efficient for real-time fraud detection. Regarding end-to-end performance (including neighbor query and 

## **1 INTRODUCTION** 

Fraudulent transaction is one of the most serious threats to online financial services today. This problem is exacerbated by the growing sophistication of business transactions using online payment applications (e.g., eBay and Alipay) and payment cards [13, 26]. Fraudsters use a range of tactics, including paying with stolen credit cards, chargeback fraud involving complicit cardholders, selling fake e-gift cards, or creating schemes to create fraud ring attacks against multiple merchants<sup>1</sup> . In this work, our goal is to detect risky transactions on a real-world e-commerce platform. 

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _CIKM ’22, October 17–21, 2022, Atlanta, GA, USA_ 

In e-commerce marketplaces, unauthenticated transactions are a major part of buyer risk. In our previous generation of detection engine, it is observed that the _entities_ linked to transactions, such as shipping addresses and device machine IDs, are key clues in 

© 2022 Association for Computing Machinery. ACM ISBN 978-1-4503-9236-5/22/10...$15.00 https://doi.org/10.1145/3511808.3557136 

1https://www.verifi.com/in-the-news/need-know-fraud-rings/ (last accessed: April 22, 2022). 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

Lu, et al. 

detecting frauds. Based on these entities, hundreds of patterns are summarized as features in machine learning models or as rules in decision engines. However, the feature engineering of these linkage patterns, which are designed by human experts, is only feasible within 1-hop horizon in the graph. Beyond 1-hop, it is still quite inefficient for human experts to explore and interpret, due to the huge amount of derived features generated by aggregating original features along risk propagation paths. 

**Characteristics of Transaction Graphs** . Two vital characteristics of fraudulent transactions have been raised [18] in a similar application of massive suspicious registration detection. First, transactions and relevant entities naturally form a graph with hetero- <u>geneous</u> nodes (e.g., IP address, email, accounts). Those fraudulent transactions tend to share certain common risky entities, such as the device and IP address. Second, fraud detection in transaction graphs should consider the problem of temporal dynamic because the accounts used by fraudsters and legitimate users usually generate distinctive activity events in separate time periods. 

**Challenge 1: Prevention of learning from future transactions** . _In a temporally dynamic graph, can we use information flowing from vertices whose timestamps are different from the current vertex?_ For the problem of fraud detection, claim, chargeback, and suspension histories are usually considered top-ranking features in fraud detection models, in which timestamp is an important property. For a specific time, if timestamp is considered, there are two categories of events, historical and future events. Intuitively, the feature patterns of the upcoming events linked by entities may allow models to foresee the risk. However, this assumption is impractical in real-time applications, as future vertices have not appeared in the graph yet. Therefore, in this work, we strictly constrain the model to utilize only the past transaction. 

**Challenge 2: Efficiency of Graph Inference** . During graph inference, different financial applications entail diverse latency requirements. Some use cases, such as Know-Your-Customer (KYC) procedures during account registration and post-transaction evaluation for anti-money laundry detection, may tolerate relatively high latency. However, detecting fraud transactions requires a quick response, since end users are often sensitive to latency. Generally, graph neural network (GNN) models aggregate information from neighbors within at least 2-hops in the graph; therefore, each inference typically takes hundreds of milliseconds or even several seconds, which cannot meet internal requirements and user-side expectation on system latency. 

To address the aforementioned challenges, we propose the BRIGHT (Batch and Real-time Inception GrapH Topology) framework. 

- (1) We propose a novel graph transformation method for temporally dynamic transaction graphs, yielding a Two-Stage Directed (TD) Graph storage strategy. This construction is time-sensitive, and can be utilized to perform time-aware message passing in real-time. 

- (2) Based on the transformed TD graph, we introduce a Lambda<sup>2</sup> Neural Network (LNN) architecture that supports both batch processing and real-time processing. LNN leverages snapshot 

> 2Lambda architecture is a hybrid data processing approach that handles a large amount of data both in batch and in streaming fashion. For an overview on Lambda architecture in data processing, we refer readers to https://en.wikipedia.org/wiki/Lambda_ architecture (last accessed: April 22, 2022). 

aggregation and avoids foreseeing future information during training. We have also improved the efficiency of real-time inference using the Lambda architecture. 

- (3) Our experiments show that BRIGHT outperforms the baseline models by more than 2% w.r.t. average precision. Additionally, it is computationally efficient for real-time fraud detection. BRIGHT reduces more than 75% P99<sup>3</sup> end-to-end inference latency (including neighbor query and graph inference), compared to traditional GNN inference frameworks. For the inference stage, our speedup is on average 7.8× over the traditional GNN. 

## **2 PRELIMINARIES** 

In our previous works, DHGReg [18] and DyHGN [16], we have studied the dynamics of graph modeling in account and transaction networks.<sup>4</sup> Specifically, DHGReg [18] is designed to detect massive suspicious registrations through a dynamic heterogeneous graph neural network. DHGReg is composed of two types of subgraphs: (1) structural subgraphs in each timestamp that reflect the links between different types of entity; and (2) a temporal subgraph that links the structural subgraphs via temporal edges. As such, the time dimensions are unrolled in a large graph together with structural edges. With this graph construction technique, DHGReg outperforms simple baselines such as GCN and GAT in capturing suspicious registrations on time. 

DyHGN [16] is built on top of DHGReg [16] and has studied to incorporate diachronic temporal embeddings [6] while still keeping structural subgraphs. It also explores the replacement of simple convolution layers with more complex ones, such as a heterogeneous transformer layer [10]. We also discuss graph structure and data distribution over time, as well as their influence on GNN modeling dynamics. 

However, we notice three issues when deploying these prototype models in production: 

- **(I1)** The bi-graph structure (transactions and entities) tends to deplete GPU memory when the graph scales up to millions of vertices and edges; 

- **(I2)** There is future information leakage in the training of predictive models. In the GNN message passing, features or embeddings from future events are also included when evaluating the risk of past events. 

- **(I3)** The latency of the neighbor query is more than hundreds of milliseconds or even seconds, which is not ideal for a realtime responsive system. 

## **3 RESEARCH QUESTION AND METHODOLOGY** 

In this work, we propose BRIGHT (Two-Stage Directed Graph transformation + Lambda Neural Network) to tackle these remaining issues when deploying GNN in production. 

3The P99 (99th percentile) latency is the worst latency that was observed by 99% of all requests. 

> 4We have discussed fraud detection with heterogeneous GNNs in an industrial billionscale dataset, and conducted human evaluations against GNN predictions in xFraud [17]. There, we did not include the discussion of temporal aspects. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

BRIGHT - Graph Neural Networks in Real-Time Fraud Detection 

- To solve **(I1)** , we keep the structural subgraphs of DHGReg and partition the graphs to support both batch and online learning. 

- To solve **(I2)** , we strictly control that only historical reference transaction information is used to predict target transactions. 

- To reduce the overhead of querying neighbors in **(I3)** , we enable batch inference and store entity embeddings in a keyvalue store. These entity embeddings are then used in online inference to decrease inference latency. 

In this section, we introduce the research questions we want to answer with BRIGHT (Sec. 3.1), illustrate the graph transformation module (Sec. 3.2), and explain the Lambda Neural Network (Sec. 3.3). 

## **3.1 Research Question** 

With BRIGHT, our goal is to answer these two research questions. 

- **(Q1)** How could we construct a dynamic graph that allows us to control the direction of the information flow and effectively support online inference? 

- **(Q2)** How could we design a graph neural network architecture that is efficient for online inference? 

## **3.2 Time-sensitive Graph Construction** 

In this work, transaction fraud detection is treated as a binary classification problem in an inductive setting on a dynamic heterogeneous graph. In a static transaction graph G (Fig. 1 (a)), a vertex _𝑣_ ∈V has a type _𝜏_ ( _𝑣_ ) ∈A, where A := { _𝑡𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛,𝑒𝑛𝑡𝑖𝑡𝑦_ }. An edge _𝑒_ ∈E links from a _𝑡𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛_ vertex ( _𝑡𝑥𝑛_ for short hereafter) to an _𝑒𝑛𝑡𝑖𝑡𝑦_ vertex. 

Nodes _𝑡𝑥𝑛_ with unauthenticated chargeback claims from the customer system are marked as 1, which are considered fraudulent transactions. The others are marked as 0, which represents legitimate transactions. These labels are used in our binary classification task. These _𝑡𝑥𝑛_ with labels are called **target** transactions in our setting. The historical transactions that share the same entities _𝑒𝑛𝑡𝑖𝑡𝑦_ used in the target transaction, such as emails and shipping addresses, we call them **reference** transactions, which do not have any labels in our experiments. 

To construct a Two-Stage Directed Graph (TD Graph) to support Lambda Neural Network (LNN), our graph construction consists of the following steps, as illustrated in Fig. 1. 

- **(a) Static Graph.** The static graph is constructed from months of transaction logs by transforming them into a bi-graph (transaction-entity graph). Note that the edges here are bidirectional. 

- **(b) Snapshot Graph.** Each node in the static graph is placed in its corresponding timestamp snapshot. Reference transactions are linked to entities that are on the same timestamp snapshot as the corresponding target transactions. 

- **(c) Two-Stage Directed Graph.** A TD Graph is stored in target transaction partitions. A partition is made up of several timestamps that are the temporal snapshots in which all related transactions and entities are. A TD graph is equivalent to not only a snapshot graph, but also a simplified topology view for target transactions in the partition. The TD Graph is used for LNN learning and inference. 

**Table 1: Notations.** 

|**Notation**|**Description**|
|---|---|
|G|Static graph|
|V|Vertices on the static graph|
|E|Edges on static graph|
|_𝑣_|Transaction or entity on the<br>static graph|
|_𝑒_|Transaction-entity linkage on the<br>static graph|
|_𝑡𝑥𝑛_|Transaction vertex on the static graph|
|_𝑒𝑛𝑡𝑖𝑡𝑦_|Entity vertex on the static graph|
|T|Timestamp set/Time window in a partition,<br>T := {0_,_1_, ...,𝑡_}|
|GT|Snapshot graph where<br>each vertex has a timestamp|
|G<sup>_𝑅𝑇_</sup><br>_𝑇_|Real-Time (RT) Graph, used in real-time inference|
|G<sup>_𝐵𝑎𝑡𝑐ℎ_</sup><br>_𝑇_|Batch Graph for batch inference|
|G<sup>_𝑇𝐷_</sup><br>_𝑇_|Two-Stage Directed Graph,<br>union ofG<sup>_𝑅𝑇_</sup><br>_𝑇_<br>andG<sup>_𝐵𝑎𝑡𝑐ℎ_</sup><br>_𝑇_|
|_𝑡_|Time period snapshot_𝑡_, a time duration (day)|
|G<sup>_𝑅𝑇_</sup><br>_𝑡_|Subgraph of Real-Time (RT) Graph on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|
|G<sup>_𝐵𝑎𝑡𝑐ℎ_</sup><br>_𝑡_|Subgraph of Batch Graph on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|
|_𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑡_|Time period snapshot_𝑡_∈T|
|_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|Time period partition_𝑡_∈T,|
||which is the partition of target transaction<br>at time_𝑡_that also contains reference transaction<br>from historical time snapshots|
|_𝑋𝑡_|Feature embeddings of transactions on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|
|_𝑡𝑥𝑛𝑡_|Transaction on_𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑡_|
|_𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<br>|Entity nodes on_𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑡_|
|_𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup><br>_𝑡_<br>|Target transaction on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|
|_𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup><br>_𝑡_<br>|Historical reference transaction on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|
|_𝑒𝑛𝑡𝑖𝑡𝑦_<sup>_𝑡𝑔𝑡_</sup><br>_𝑡_|Entity nodes on_𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_|



We now discuss in detail how the three types of graphs are constructed in Fig. 1. 

_3.2.1_ **Static Graph Construction** _._ To collect neighbor features to assess the risks of transaction fraud, multiple entities used in the checkout sessions are considered neighbors of _𝑡𝑥𝑛_ nodes. These entities, including shipping address, E-mail, IP address, device ID, contact phone, payment token, and user account, are represented as _𝑒𝑛𝑡𝑖𝑡𝑦_ nodes in G. 

Each _𝑡𝑥𝑛_ vertex represents a checkout transaction along with a unique transaction ID, linked with multiple _𝑒𝑛𝑡𝑖𝑡𝑦_ vertices such as shipping addresses, E-mails, contact phones that buyers need to confirm on checkout pages. Most of the _𝑒𝑛𝑡𝑖𝑡𝑦_ vertices are also linked to multiple _𝑡𝑥𝑛_ vertices. 

Given a set of target transactions, a static graph G can be constructed from their records. A transaction record could be broken down into a _𝑡𝑥𝑛_ vertex and several _𝑒𝑛𝑡𝑖𝑡𝑦_ vertices. Edges _𝑒_ are placed between entities and transactions that use these entities. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

Lu, et al. 



<!-- Start of picture text -->
Transaction Log (a) Static Graph<br>   Transaction Phone Buyer Time<br>1 1234567 Bob t<br>2 7654321 Alice t-1 t-1 t<br>3 7654321 Alice t-2<br>4 1234567 Bob t-3 t-2 t-3<br>t-3 t-2 t-1 t<br>t-3 t-2 t-1 t<br>Target Transaction<br>(c) Two-Stage Directed Graph Reference Transaction (b) Snapshot Graph<br><!-- End of picture text -->

**Figure 1: Graph Transformation in BRIGHT. RT: Real-Time.** 

Reference transactions within a given observation window are extracted if they share the same entities. Edges are also added between reference transactions and common entities. 

_3.2.2_ **Snapshot Graph Construction** _._ A time snapshot _𝑡_ ∈T , where T := {0 _,_ 1 _, ...,𝑡_ }, represents a period of time duration, e.g., hour or day. T is the time window in one Snapshot Graph. In our experiments, the time period for each snapshot is one day. A snapshot vertex _𝑣𝑡_ ∈VT represents the static vertex. The snapshot vertex _𝑣𝑡_ is a transformation of _𝑣_ at snapshot _𝑡_ . The workflow to construct a snapshot graph is described below. 

- (1) For each _𝑡𝑥𝑛_ node on the static graph G, we construct _𝑡𝑥𝑛𝑡_ on _𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑡_ , which is the time period in which the transaction was created. 

- (2) For each _𝑒𝑛𝑡𝑖𝑡𝑦_ node directly linked to the transaction nodes _𝑡𝑥𝑛𝑡_ , we create the node _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_ on _𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑡_ , sharing the same transaction creation time. There may be multiple instances of the same entity in the snapshot graph GT if it is linked to transactions created in various snapshots. 

- (3) Create edges between the target transaction nodes _𝑡𝑥𝑛𝑡_ and the 1-hop entity neighbor _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_ . 

- (4) Create edges between the reference transaction nodes _𝑡𝑥𝑛𝑖_ and 1-hop entity neighbor _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_ , where 0 ≤ _𝑖_ ≤ _𝑡_ . 

On Snapshot Graph G _𝑇_ , a transaction node may have two roles. One is the target transaction; the other is the reference transaction if it shares the same entity as another target transaction. In Fig. 1 (b), the transaction in snapshot _𝑡_ − 3 is a reference transaction to the transaction in snapshot _𝑡_ . Meanwhile, it can also be a target transaction in snapshot _𝑡_ − 3 when we predict its label. 

Potential roles for a single _𝑡𝑥𝑛𝑡_ node make it difficult to isolate future information from message passing if there is no further filtering or sampling based on transaction timestamps. Some edges can be in G _𝑇_<sup>_𝑅𝑇_</sup> and G _𝑇_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> (which we will introduce in Sec. 3.2.3), 

which leads to future information leakage. We want to avoid neighbor sampling due to the high latency in existing SAGE neighbor sampling approaches, as shown in [30]. This brings us to our design of Two-Stage Directed Graph shown in the next section. 

_3.2.3_ **Two-Stage Directed Graph** _._ Two-Stage Directed (TD) graph simplifies the topology view from the target transaction side, making it easy to split the graph into Real-Time Graph G _𝑇_<sup>_𝑅𝑇_</sup> and Batch Graph G _𝑇_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> . We show in Fig. 1 (c) these two parts of the graphs that are taken later by LNN as input for various parts of the network. G _𝑇_<sup>_𝑅𝑇_</sup> is the subgraph with thick directed edges (the dark red circle), while G _𝑇_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> is the subgraph with bidirectional edges (the light red circle). 

The partition of target transaction is introduced to isolate transaction roles, because a transaction can act as both a target/reference transaction, as we discuss above. All reference transaction nodes sharing common entities are stored with the target transactions in the same partition. On the TD graph, there is only one role for transactions, either a target transaction or a reference transaction. There are multiple snapshots _𝑠𝑛𝑎𝑝𝑠ℎ𝑜𝑡𝑖_ in one target partition _𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_ , _𝑖_ ≤ _𝑡_ , as illustrated in Fig. 2 (a). The workflow to construct a TD graph is described below. 

- (1) Place target transactions _𝑡𝑥𝑛𝑡_ , their corresponding 1-hop entities _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_ , and the reference transactions _𝑡𝑥𝑛𝑖_ , where 0 ≤ _𝑖_ ≤ _𝑡_ into _𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑡_ . These transactions are represented as _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ and _𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup> _𝑡_ . The entities are represented as _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> . Reference transactions may be put into multiple partitions if their related target transactions are in different time snapshots. 

- (2) Link _𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup> _𝑡_ and _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> with bi-directed edges, which forms the Batch Graph G _𝑡_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> . It is used for batch inference of entity representations. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

BRIGHT - Graph Neural Networks in Real-Time Fraud Detection 

**Table 2: Two-Stage Directed Graph Edge Types.** 

|**Edge Type**|**Description**|
|---|---|
|_𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup><br>_𝑡_<br>↔_𝑒𝑛𝑡𝑖𝑡𝑦_<sup>_𝑡𝑔𝑡_</sup><br>_𝑡_<br>_𝑒𝑛𝑡𝑖𝑡𝑦_<sup>_𝑡𝑔𝑡_</sup><br>_𝑡_<br>→_𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup><br>_𝑡_|Bi-directed edges between reference<br>transactions and entities on<br>the Batch GraphG<sup>_𝐵𝑎𝑡𝑐ℎ_</sup><br>_𝑡_<br>Directed edges from entities to target<br>transaction nodes on<br>the Real-Time GraphG<sup>_𝑅𝑇_</sup><br>_𝑡_|



- (3) Link _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> and _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ with directed edges from the entity to the target transaction, which forms the Real-Time Graph G _𝑡_<sup>_𝑅𝑇_</sup> . It is used for real-time inference of transaction risk. 

The edges on Batch Graph are bi-directed, which enables bidirectional inference with deep GNN models on Batch Graph. The edge types for the TD Graph are represented in Tab. 2. The edges on Real-Time Graph are uni-directed, which are always from entities to the target transactions. The number of layers in Real-Time Net is set to 1 for inference efficiency, so it is not necessary to make the edges bi-directed. Furthermore, with this setting, we ensure that no message is passed between target transactions across multiple timestamps even if they are on the same target partition. 

Note that the design of the TD graph is in line with the Lambda Neural Network, which enables batch and online inference in the same framework. We elaborate the design of the LNN architecture in the following Sec. 3.3. In Fig. 2 (a), we show an illustrative example of the risk assessment of the transaction on _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ using TD Graph. The features of historical reference transactions _𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup> _𝑡_ are sent to _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> (phone and buyer in this example). They are the entity nodes 1-hop away from the target transaction. After bi-directed message-passing through the dotted edges, the embeddings (for phone and buyer in this example) of 1-hop neighbors are obtained. Then these embeddings are sent to the target transaction _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ through the directed edges (in red), which forms the graph used in real-time inference. With transformation into a TD Graph, the messages passed only from historical entities/transactions prior to _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ are guaranteed, which addresses the research question **(Q1)** . 

## **3.3 Network Architecture** 

We propose a Lambda Neural Network (LNN) architecture, which treats the last hop edges in Real-Time Graph differently from those edges in Batch Graph from TD. This is illustrated in Fig. 2 (b). 

Lambda Architecture is a hybrid data processing approach that handles a large amount of data in both batch and streaming fashion. One of the benefits from Lambda Architecture is the balance between the data processing scalability and the data access latency. LNN architecture handles message passing from Batch Graph and Real-Time Graph in separate GNN blocks. Message passing on Batch Graph is conducted in batch jobs through Batch Net. Message passing on the Real-Time Graph is conducted in real-time inference through the Real-Time (RT) Net, deployed in online services. 

Similar to the two-“tower" model architecture [5, 24, 25, 27–29] (see Sec. 6), we design LNN to support two stages of processing 



<!-- Start of picture text -->
(a) Two-Stage Directed Graph<br>t t-1 t-2 t-3<br>Target Transaction<br>Reference Transaction<br>RT Inference Phone Entity<br>Batch Inference Buyer Entity<br>GConv GConv<br>... L<br>Decoder GConv<br>Risk Score ...<br>Entity Embeddings<br>RT Inference Key-Value DB<br>Batch Inference<br>RT Net Batch Net<br>(b) Lambda Neural Networks<br><!-- End of picture text -->

**Figure 2: Two-Stage Directed Graph (a) and Lambda Neural Network (b). RT: Real-Time, GConv: Graph convolution.** 

(batch and real-time inference). The LNN architecture, together with the TD graph, addresses the research question **(Q2)** , which is our proposed solution for online inference in a dynamic setting. 

As illustrated in Fig. 2, LNN consists of a Batch Net (in blue) and a Real-Time (RT) Net (in orange). Batch Net is a stack of GNN layers, similar to DeepGCNs [14]. RT Net consists of a graph convolutional layer and a decoder, which could simply be a fully connected linear layer. The two stages are divided at the neighboring entities in one hop to _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> (phone and buyer in this example). The first stage is Batch Net inference, after which we obtain the entity embeddings learned from historical transactions and flush them into a key-value store. In the second stage, the RT Net fetches the entity embeddings from the key-value store, also takes the raw features from the target transactions, and then computes the transaction risk scores. 

_3.3.1_ **End-to-end Training** _._ In the training phase, both the Batch Graph and the RT Graph are used for end-to-end LNN training. In each mini-batch, we sample one partition for the time window T , where T := {0 _,_ 1 _, ...,𝑡_ }. The timestamp of each target transaction is within the partition time window. All timestamps for reference transactions are prior to those for target transactions. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

Lu, et al. 

Similar to traditional GNNs, the inputs of Batch Net include the features of reference transactions _𝑋𝑡_ and Batch Graph _𝐺𝑡_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> , as illustrated in Eq. 1: 



Each graph convolutional layer of Batch Net is generic with a hidden state _ℎ_<sup>_𝑙_</sup> of the layer _𝑙_ , as illustrated in Eq. 2. N ( _𝑣_ ) is all the neighbors of the vertex _𝑣_ , which is _𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup> _𝑡_ or _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> . ⊙ is a generalized node aggregation function. ∪ represents concatenation, _𝑊_ weight matrices. 

_ℎ_<sup>_𝑙_</sup> _𝑣_<sup>+1</sup> = _𝜎_ ( _𝑊_ · ⊙({ _ℎ_<sup>_𝑙_</sup> _𝑣_<sup>} ∪{</sup><sup>_ℎ_</sup> _𝑢_<sup>_𝑙,_∀</sup><sup>_𝑢_∈N(</sup><sup>_𝑣_)})) +</sup><sup>_ℎ𝑙_</sup> _𝑣_ (2) 

As input, RT Net takes features from target transactions and entity embeddings learned from Batch Net inference. The graph convolutional layer of RT Net shares the same form as that of Batch Net, as is illustrated in Eq. 3. One difference is that there is only one convolutional layer in the RT Net for the sake of inference efficiency.<sup>5</sup> Furthermore, RT Net isolates the aggregation of messages between different target transaction nodes _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ within the same target snapshot partition. _𝜙_ is a linear projection for the transaction features, which assures that the transaction features and the embeddings have the identical dimensions. 



The risk score for target transaction _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ is decoded from the real-time transaction embedding _ℎ_<sup>_𝑅𝑇_</sup> through a fully connected _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ linear layer, which is illustrated in Eq. 4. 



_3.3.2_ **Efficient Graph Inference** _._ As described above, end-toend learning uses the complete LNN architecture. When deployed in a production environment, LNN inference is decoupled into batch inference and real-time inference. 

**(Batch Inference Stage.)** For batch inference stage, the embeddings _ℎ𝑡_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> of entities _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> are periodically generated according to Eq. 1. In our current design, the time period is one day. Finally, entity embeddings are generated and stored in a distributed key-value database for multiple downstream purposes. In our paper, these embeddings are used to detect fraud transactions. The embeddings are refreshed daily to serve real-time transaction risk evaluation. 

**(Real-Time Inference Stage.)** For real-time risk assessment, the second stage of LNN (namely RT Net) calculates the score by Eq. 4. The results are equivalent to end-to-end inference with the complete LNN adopted in the learning stage. The inference latency is further significantly reduced due to the 1-layer RT Graph. 

> 5In consideration of both inference efficiency and the prevention of data leakage, a single layer is chosen for RT Net. (1) Obviously, one convolutional layer provides lower inference latency. (2) Currently, only one-hop neighbours to the target transactions are linked by unidirectional edges, the other neighboring nodes are connected by bidirectional edges. Therefore, if there are more than one convolutional layers, we would have a data leakage problem, where the future information could be used to predict nodes in the past. 

**Table 3: Cypher Queries for Different Number of Hops (in the Extended Graph) in the RT Net. RT: Real-Time.** 

|**Number of Hops**|**Cypher Query**|
|---|---|
|**2**|**MATCH**<br>(target:transaction)-[]->(:entity)->[]->(nbr2:transaction)<br>**WHERE**transaction=$transaction_id<br>**RETURN**nbr2|
|**4**|**MATCH**<br>(target:transaction) -[]->(:entity)->[]->(nbr2:transaction)<br>-[]->(:entity)->[]->(nbr4:transaction)<br>**WHERE**transaction=$transaction_id<br>**RETURN**nbr2, nbr4|
|**6**|**MATCH**<br>(target:transaction)-[]->(:entity)->[]->(nbr2:transaction)<br>-[]->(:entity)->[]->(nbr4:transaction)<br>-[]->(:entity)->[]->(nbr6:transaction)<br>**WHERE**transaction=$transaction_id<br>**RETURN**nbr2, nbr4, nbr6|



**Table 4: Dataset Summary ("M": Million). *The fraud ratios are only reported on the sampled datasets. TD: Two-Stage.** 

|**Split**|**Graph**|**#Nodes**|**#Edges**|**Fraud%***|
|---|---|---|---|---|
||Static|56.7M|153.9M||
|**Training**|Snapshot|56.7M|274.5M|2.70%|
||TD|66.4M|332.0M||
||Static|9.63M|18.42M||
|**Testing**|Snapshot|9.63M|30.39M|2.30%|
||TD|10.28M|32.88M||





<!-- Start of picture text -->
Tabular Feature Input<br>tree tree<br>Tree Splits<br>node node node node<br>Transformed<br>Features<br>GBDT Output<br><!-- End of picture text -->

**Figure 3: GBDT as Feature Encoder.** 

Since RT Graph only requires 1-hop neighbors, which are already available in the transaction request, a graph query is not necessary during real-time inference. Graph query refers to fetching nodes and their features from a graph database such as Neo4j. Illustrative queries in Cypher<sup>6</sup> are given in Tab. 3. For a single layer RT Net, the number of hops is set to 2. It is possible to include more hops in the RT Net, as we have discussed in Sec. 5.3. In the experiments of multiple hops, we also use one convolution layer for RT Net, to refrain from data leakage. 

6https://neo4j.com/developer/cypher/. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

BRIGHT - Graph Neural Networks in Real-Time Fraud Detection 

## **4 FRAUD DETECTION EXPERIMENT** 

In this section, we perform an evaluation of BRIGHT’s performance in the fraud detection task. 

## **4.1 Dataset and Preprocessing** 

We conduct experiments on real-world transaction records sampled from eBay marketplace to evaluate the proposed framework. Our dataset contains 7 million labeled transactions.<sup>7</sup> Downsampling is conducted on legitimate transactions due to the label imbalance, as in [17]. The sampling ratio for fraud transactions is kept at ard. 2.5%, which is empirically determined, as in other use cases at eBay. Entities in G include shipping addresses, device IDs, phones, payment tokens, IPs, and buyer accounts. 

The data set is divided by the creation time of the target transactions into training and testing datasets. The first 80% target transactions are used as a training dataset, and the last 20% transactions are used for testing. The validation set for early stopping check is 10%, randomly chosen from the training dataset. The statistics for the graph are illustrated in the Tab. 4. 

## **4.2 Baselines** 

LightGBM (LGB) [11] is chosen as the baseline. There are two baseline models in our experiments built upon LightGBM. One is fully trained, namely, LGB (Bench), with 10k + trees, and was early-stopped after 32 iterations if the validation metrics have not improved. The other is a light version with 512 trees. The light model, namely the LGB (FE), is also utilized as a feature encoder (FE) for the LNN input. 

## **4.3 Feature Encoder** 

Gradient Boosting Decision Tree (GBDT) models such as LightGBM [11] dominate many tabular dataset applications [7], compared to existing popular deep model architectures designed specifically for tabular dataset, such as AutoInt [21] and TabNet [1]. For fraud detection on payment transactions, where most datasets are tabular, boosting models are widely used [3, 31]. For simplicity, a pre-trained GBDT model is used as the feature encoder for tabular features. Similarly to Logistic Regression models on top of Decision Trees [9], the values of the chosen leaf nodes are used as encoded embeddings from the feature encoder, as illustrated in Fig. 3. 

## **4.4 Experiment Setup** 

The transaction records sampled as described in Sec. 4.1 are transformed into graphs using our method proposed in Sec. 3.2. 

**(Data Loader.)** The mini-batch strategy is used in GNN learning. In each mini-batch, there is only one target partition. The maximum number of historical time snapshots (T ) in the target partition is set to 30. The size of the mini-batch depends on the merged community<sup>8</sup> node size, which is close to 32k. The transformed TD 

> 7Note that in our experiments, only these 7 million transaction records have labels, the graphs in Tab. 4 contain more transaction nodes yet without labels (reference transactions). It is common that not every transaction has a label, which could be due to delay in third-party service, as we elaborated in [17]. 

> 8Similar to ClusterGCN [4], graph clustering structure is used in the BRIGHT training process. Historical neighboring reference transactions are 2 hops away from the target transactions. For the connected components, whose node sizes are larger than 32k, they are cut into smaller communities through Louvain [2]. Before training, small 

**Table 5: LNN Performances in Fraud Detection (Test Set). LGB: LightGBM, LNN: Lambda Neural Network.** 

|**Model**|**ROC AUC**|**Average Precision**|
|---|---|---|
|**LGB (FE)**|0.9255±0.0003|0.3984±0.0007|
|**LGB (Bench)**|0.9247±0.0005|0.4201±0.0013|
|**BRIGHT-LNN (GAT)**|**0.9286**±**0.0005**|0.4394±0.0009|
|**BRIGHT-LNN (GCN)**|0.9276±0.0016|**0.4420**±**0.0035**|





<!-- Start of picture text -->
1.0<br>LGB (FE)<br>LGB (BENCH)<br>0.8<br>LNN (GCN)<br>LNN (GAT)<br>0.6<br>0.4<br>0.2<br>0.0<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Recall<br>Precision<br><!-- End of picture text -->

**Figure 4: Precision-Recall Curves.** 

graph is used as input to the LNN model. G _𝑡_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> and G _𝑡_<sup>_𝑅𝑇_</sup> are fed separately for LNN models (Batch Net and RT Net, respectively). **(Feature Encoding.)** The features of _𝑡𝑥𝑛_<sup>_𝑟𝑒𝑓_</sup> _𝑡_ and _𝑡𝑥𝑛_<sup>_𝑡𝑔𝑡_</sup> _𝑡_ are first encoded by LGB (FE). The embeddings _𝑋_<sup>_𝑡_</sup> generated by LGB (FE) are then fed to LNN, together with G _𝑡_<sup>_𝐵𝑎𝑡𝑐ℎ_</sup> and G _𝑡_<sup>_𝑅𝑇_</sup> . The features of _𝑒𝑛𝑡𝑖𝑡𝑦𝑡_<sup>_𝑡𝑔𝑡_</sup> are set to zero. The vector size of the transaction embeddings and entity embeddings is 512 (equal to the number of trees). The remaining parameters to train GBDT are default values. 

**(Model Architecture.)** As in DeepGCN [14], we choose GCN [12] and GAT [23] for Batch Net, and GCN for RT Net. 

**(Hyperparameters.)** We grid search for the number of GNN layers for Batch Net and the number of hidden units for both Batch Net and RT Net. The numbers of GNN layers are chosen from {4 _,_ 6 _,_ 8 _,_ 16}. The numbers of hidden units are chosen from {256 _,_ 512}. The learning rate is set to 0.001 for all experiments. The maximal epochs for training are 128. Regarding early stopping, we terminate the training if the loss over the validation dataset does not decrease within 16 epochs. For each group of hyperparameters, we execute three runs and report the average results in Tab. 5. 

## **4.5 Quantitative Results on Fraud Detection** 

We report the results of Average Precision (AP) and Area Under the Receiver Operating Characteristic Curve (ROC AUC) on the testing data in Tab. 5. As can be seen, LNN outperforms LGB (FE) in terms 

communities are merged in the same target partition. The node sizes of the merged communities are close to 32k. The batch size is chosen by experience to balance disk IO and GPU memory. The impact of batch size in both efficiency and fraud detection performance could be investigated in our future work. Different batches are not overlapping in terms of target transactions that are predicted. But the features and nodes used for each prediction could be overlapping if they are used/linked in the neighborhood of the target transactions. 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

Lu, et al. 

of both ROC AUC and AP, by aggregating features through graph topology. LNN (GCN) has an average precision of 44.2%. Compared to LGB (Bench), which is the state-of-the-art model for tabular data, LNN (GCN) achieves an improvement of 2.2%. We also plot the precision-recall curves in Fig. 4, and the curves show that LNN models can capture more fraud transactions with higher precision if we prioritize precision over recall. In our previous work [17], we have discussed that in fraud detection tasks, we generally maintain a balance between precision and recall, while favoring precision over recall. This is because we try to reduce the workload of the business unit in examining false positives while trying to catch as many frauds as possible. 

## **5 LAMBDA NEURAL NETWORK ARCHITECTURE EFFICIENCY** 

Optimizing inference efficiency is another goal in our BRIGHT framework, which aims to minimize neighbor queries during GNN inference. In this evaluation, we compare LGB (Bench), end-to-end LNN (GCN), and RT Net. 

## **5.1 Experiment Setup** 

For LNN (GCN) and RT Net, we use both CPU and GPU devices. In each test, a target transaction is evaluated and the system evaluates its risk of fraud. We report the real-time inference latency, which is decoupled into three stages – _graph query_ , _feature collection_ , and _model inference_ . 

**(Graph Query.)** For GNN inference, neighboring reference transactions are required for graph construction and feature collection. Theoretically, key-value databases could be used to support query services for neighbor lookup. However, they are not good choices due to the complexity of the service implantation. Graph databases are natural choices as they provide a standard graph query language. In our experiments, Neo4j Community Edition<sup>9</sup> is used as our graph query service. 

We set up the database for one target partition, which is randomly selected from the test set. There are 0.7 million nodes and 3.8 million edges loaded into the graph DB. The default configuration is used for the Neo4j server. For LGB (Bench) and RT Net, there is no graph query test. LGB (Bench) does not need relational data for inference. In RT Net, the 1-hop entity IDs for embedding collection are in the request to predict the label of target transaction. 

**(Feature Collection.)** Both raw features and entity embeddings are stored in a key-value database in our experiments. For simplicity, Redis<sup>10</sup> is chosen as our key-value database. For these 0.7 million records, we store their raw features and embeddings on the Redis server with the default configuration. 

**(Model Inference.)** LGB (Bench) inference is conducted on CPU only. LNN (E2E) inference is an end-to-end full GNN inference, where we do not separate the Batch Net and RT Net. LNN (E2E) is equivalent to a traditional GNN inference workflow. The graph convolutional layers chosen for LNN is GCN. For the tests of RT Net inference, there is no Batch Net inference. Entity embeddings from batch inference are obtained from the key-value store. Both CUDA and CPU devices are tested for LNN and RT Net inference. 

> 9https://neo4j.com/ 

> 10https://redis.io/ 

Both models are implemented in PyTorch. For simplicity, there is no further optimization of the inference for the LNN models and RT Net models. We randomly choose 10k payment transactions for the latency test, recorded in milliseconds. We use one machine for the database server and inference client. Regarding hardware, the machine is equipped with 32 Intel Xeon Gold 6230 CPUs, 64 GB memory, and one Nvidia Tesla V100 GPU. 

## **5.2 Experimental Results** 

As can be seen in Tab. 6, we compare LNN (E2E) and RT Net. The end-to-end inference 99% latency (99th percentile latency, a.k.a. P99) is significantly reduced from 251.35 ms to 72.57 ms using RT Net, that is, 71.13% latency saving on CUDA devices. In CPU devices, the latency saving is even greater (76.67%). The reason for the performance improvement is that the graph query and Batch Net inference are omitted in RT Net. Compared to LGB, although RT Net introduces a more complex model architecture, only around 1.6% overhead of P99 inference latency is introduced in the inference stage. Note that our latency numbers (<100ms) resonate the results reported by previous benchmarking papers in the GNN inference optimization [30, 32]. 

## **5.3 Discussion on Extended Graph Inference** 

In our previous experiments, we only choose two-hop neighbors (i.e., entities and their reference transactions) for the target transaction. As readers might suspect, _what if neighbors of more hops are considered?_ To answer this question, we perform experiments to evaluate inference latency with 4-hop and 6-hop neighbors. We take a daily partition with up to 6-hop neighbors (i.e., extended graph), which has 10.5 million nodes and 41.3 million edges. As illustrated in the Tab. 7, as the neighbor hops increase, our RT-Net architecture achieves larger inference speedups. For example, LNN on CPU devices for the 6-hop neighbor graph is 1335.98 ms, while RT Net only costs 58.44 ms — a 22.86× improvement. 

## **5.4 Discussion on Using BRIGHT in Other Production Scenarios** 

We can use the Two-Stage Directed Graph in scenarios such as fraud detection for payment transaction, where we require constant update of the transaction snapshots (the frequency should be less than one day). In this use case, the current design in BRIGHT would not be optimal, as Batch Net embeddings are not updated frequently enough due to the low update frequency of data warehouse. We can mitigate this problem by the integration with graph database in data warehousing. 

## **6 RELATED WORK** 

We discuss previous work that is relevant to BRIGHT. 

**(Graph Neural Network.)** GNN [8, 12, 22] has become increasingly popular in learning from graphs. Through message passing, aggregation and self-attention, it has a powerful capacity to grasp the graph structure, as well as the complex relations between nodes. Recent work on GNN has also focused on heterogeneous graphs [10, 15], where nodes and edges can be of various types. 

**(Modelling Dynamics with GNN.)** Dynamic graphs can also be represented as a sequence of time events. There are several works 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

BRIGHT - Graph Neural Networks in Real-Time Fraud Detection 

**Table 6: Inference Latency (recorded in millisecond). Numbers in brackets refer to speedups compared to LNN (E2E). In LNN (E2E) there is no separation of the Batch Net and RT Net. LGB: LightGBM, LNN: Lambda Neural Network, RT: Real-Time.** 

|**Model**|**LG**|**B**|**LNN (E2**|**E, CUDA)**|**LNN (E**|**2E, CPU)**|**BRIGHT-RT**|**Net (CUDA)**|**BRIGHT-R**|**T Net (CPU)**|
|---|---|---|---|---|---|---|---|---|---|---|
|**Step**|**Avg**|**P99**|**Avg**|**P99**|**Avg**|**P99**|**Avg**|**P99**|**Avg**|**P99**|
|**Graph Query**|-|-|114.42|177.60|114.42|177.60|-|-|-|-|
|**Feature Collection**|0.06|0.13|0.08|0.20|0.08|0.20|0.06 (1.33×)|0.11 (1.82×)|0.06 (1.33×)|0.11 (1.82×)|
|**Feature Encoding**|-|-|51.88|72.16|51.88|72.16|51.70 (1.00×)|71.93 (1.00×)|51.70 (1.00×)|71.93 (1.00×)|
|**Model Inference**|52.12|71.33|15.26|29.86|150.98|365.83|1.94 (7.87×)|6.22 (4.80×)|20.74 (7.28×)|63.81 (5.73×)|
|**Total**|52.18|71.40|181.64|251.35|317.36|532.69|53.70 (3.38×)|72.57 (7.34×)|72.44 (4.38×)|124.26 (4.29×)|



**Table 7: Model Inference Latency in Extended Graph (recorded in milliseconds). Numbers in brackets refer to speedups compared to LNN (E2E). In LNN (E2E) there is no separation of the Batch Net and RT Net. LGB: LightGBM, LNN: Lambda Neural Network, RT: Real-Time.** 

|**Mod**|**el**|**LNN**|**(E2E)**|**BRIGHT**|**-RT Net**|
|---|---|---|---|---|---|
|**Device**|**Hop**|**Avg**|**P99**|**Avg**|**P99**|
||2|15.26|29.86|1.94 (7.87×)|6.22 (4.80×)|
|**CUDA**|4|14.65|30.66|1.84 (7.96×)|5.90 (5.20×)|
||6|16.14|57.03|2.01 (8.01×)|6.46 (8.83×)|
||2|150.98|365.83|20.74 (7.28×)|63.81 (5.73×)|
|**CPU**|4|171.69|1044.73|16.21 (10.59×)|49.86 (20.95×)|
||6|216.36|1335.98|19.00 (11.39×)|58.44 (22.86×)|



along this line and mostly on homogeneous graphs. Temporal Graph Networks (TGN) [19] applied memory modules and graph-based operators. The TGN framework is computationally efficient based on event update. Asynchronous Propagation Attention Network (APAN) [26] adopted a temporal encoding similar to TGN and decoupled graph computation and inference. However, for TGN, only a few neighbors are accessible by the graph module due to memory constraints. One typical work is DySAT [20] which applies self-attention networks to learn low-dimensional embeddings of nodes in a dynamic homogeneous graph. One notable difference in our setting is that we need to distinguish between two types of entities (historical and future), while DySAT assumes that all entities can be added or removed in the graph at any time point. 

**(Dynamic GNN on Fraud Detection.)** As discussed on Sec. 2, we have done previous work on flagging frauds in a dynamic setting (DHGReg [18] and DyHGN [16]). However, these approaches are not efficient in online deployment due to three issues that we analyzed in Sec. 2. In BRIGHT, we design modules to address these issues so that GNN is deployable in real-time. 

**(Two-Tower Models.)** We have surveyed the literature on twotower / stage models that attempt to incorporate batch and streaming processing in a Lambda architecture. In [5, 28], a two-tower model is proposed to pair users and items in the video recommendation system. One tower is for user embedding generation, and the other tower is adopted for item embedding generation. The Dual Augmented Two-tower Model (DAT) [29] customizes an augmented vector for each query and item to tackle imbalanced category data. Attention layers are utilized in [24] to improve the recommendation of warm- and cold-start items in online video services. Cross-Batch 

Negative Sampling (CBNS) techniques [25] are used to increase training of the two-tower model. Mixed Negative Sampling (MNS) [27] uses a mix of batch and uniform sample strategies to reduce selection bias during training for the app recommendation system. These applications focus on deep models on recommendation systems, with user embeddings and item embeddings precalculated. We setup a similar framework in BRIGHT, the neighbor embeddings are learned by a Batch Net and stored in a key-value store, which reduces the cost in online GNN deployment. 

**(Model Inference Acceleration on GNN.)** Recently, people started looking at the efficiency of online GNN inference. [32] applies channel pruning to speed up real-time GNN inference, by reducing Multiplication-and-ACcumulation (MAC) operations. They have also explored precomputation and storing of node representations to boost performance. GLNN [30] applied knowledge distillation (KD) to teach multi-layer perceptrons (MLPs) from trained GNN models. The performance of GLNN is competitive. However, the graph neighbor information is not utilized in inference. Our work focuses on relation modeling, so our model is still a vanilla GNN model. In BRIGHT, during real-time inference, neighbor information is still accessed from our precalculated entity embeddings. Our BRIGHT framework is among the first to scale dynamic GNN into an industrial dataset (>60 million nodes and >160 million edges as we show in Tab. 6 for static graph) and has provided an industrial benchmark in system deployment. 

## **7 CONCLUSION** 

In this paper, we explore how to apply GNN for fraud detection. We present a novel BRIGHT framework for efficient end-to-end learning and real-time inference without the leakage of future information. We designed a graph transformation approach to avoid future information leakage. Furthermore, a Lambda neural network architecture was proposed to support both batch and real-time processing. Our empirical study showed that BRIGHT outperformed baselines by 2% w.r.t. average precision and significantly reduced inference latency by 7.8× on average. 

## **ACKNOWLEDGMENTS** 

CZ and the DS3Lab gratefully acknowledge the support from the Swiss State Secretariat for Education, Research and Innovation (SERI) under contract number MB22.00036 (for European Research Council (ERC) Starting Grant TRIDENT 101042665), the Swiss National Science Foundation (Project Number 200021_184628, and 

CIKM ’22, October 17–21, 2022, Atlanta, GA, USA 

Lu, et al. 

197485), Innosuisse/SNF BRIDGE Discovery (Project Number 40B20_187132), European Union Horizon 2020 Research and Innovation Programme (DAPHNE, 957407), Botnar Research Centre for Child Health, Swiss Data Science Center, Alibaba, Cisco, eBay, Google Focused Research Awards, Kuaishou Inc., Oracle Labs, Zurich Insurance, and the Department of Computer Science at ETH Zurich. 

## **REFERENCES** 

- [1] Sercan O Arık and Tomas Pfister. 2021. Tabnet: Attentive interpretable tabular learning. In _AAAI_ , Vol. 35. 6679–6687. 

- [2] Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre. 2008. Fast unfolding of communities in large networks. _Journal of Statistical Mechanics: Theory and Experiment_ 2008, 10 (oct 2008), P10008. https: //doi.org/10.1088/1742-5468/2008/10/p10008 

- [3] Shaosheng Cao, XinXing Yang, Cen Chen, Jun Zhou, Xiaolong Li, and Yuan Qi. 2019. Titant: Online real-time transaction fraud detection in ant financial. _arXiv preprint arXiv:1906.07407_ (2019). 

- [4] Wei-Lin Chiang, Xuanqing Liu, Si Si, Yang Li, Samy Bengio, and Cho-Jui Hsieh. 2019. Cluster-GCN. In _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ . ACM. https://doi.org/10.1145/ 3292500.3330925 

- [5] Paul Covington, Jay Adams, and Emre Sargin. 2016. Deep neural networks for youtube recommendations. In _Proceedings of the 10th ACM conference on recommender systems_ . 191–198. 

- [6] Rishab Goel, Seyed Mehran Kazemi, Marcus Brubaker, and Pascal Poupart. 2020. Diachronic embedding for temporal knowledge graph completion. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , Vol. 34. 3988–3995. 

- [7] Yury Gorishniy, Ivan Rubachev, Valentin Khrulkov, and Artem Babenko. 2021. Revisiting deep learning models for tabular data. _Advances in Neural Information Processing Systems_ 34 (2021). 

- [8] William L. Hamilton, Z. Ying, and J. Leskovec. 2017. Inductive Representation Learning on Large Graphs. In _NIPS_ . 

- [9] Xinran He, Junfeng Pan, Ou Jin, Tianbing Xu, Bo Liu, Tao Xu, Yanxin Shi, Antoine Atallah, Ralf Herbrich, Stuart Bowers, et al. 2014. Practical lessons from predicting clicks on ads at facebook. In _Proceedings of the eighth international workshop on data mining for online advertising_ . 1–9. 

- [10] Ziniu Hu, Yuxiao Dong, Kuansan Wang, and Yizhou Sun. 2020. Heterogeneous graph transformer. In _Proceedings of The Web Conference 2020_ . 2704–2710. 

- [11] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. 2017. Lightgbm: A highly efficient gradient boosting decision tree. _Advances in neural information processing systems_ 30 (2017), 3146– 3154. 

- [12] Thomas Kipf and M. Welling. 2017. Semi-Supervised Classification with Graph Convolutional Networks. _ArXiv_ abs/1609.02907 (2017). 

- [13] Ivan Launders and Simon Polovina. 2013. Chapter 13 - A Semantic Approach to Security Policy Reasoning. In _Strategic Intelligence Management_ , Babak Akhgar and Simeon Yates (Eds.). Butterworth-Heinemann, 150–166. https://doi.org/10. 1016/B978-0-12-407191-9.00013-2 

- [14] Guohao Li, Matthias Müller, Ali Thabet, and Bernard Ghanem. 2019. DeepGCNs: Can GCNs Go as Deep as CNNs? arXiv:1904.03751 [cs.CV] 

- [15] Qingsong Lv, Ming Ding, Qiang Liu, Yuxiang Chen, Wenzheng Feng, Siming He, Chang Zhou, Jianguo Jiang, Yuxiao Dong, and Jie Tang. 2021. Are we really making much progress? Revisiting, benchmarking and refining heterogeneous graph neural networks. In _Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining_ . 1150–1160. 

- [16] Susie Xi Rao, Clémence Lanfranchi, Shuai Zhang, Zhichao Han, Zitao Zhang, Wei Min, Mo Cheng, Yinan Shan, Yang Zhao, and Ce Zhang. 2022. Modelling graph dynamics in fraud detection with “Attention". arXiv:2204.10614 [cs.LG] 

- [17] Susie Xi Rao, Shuai Zhang, Zhichao Han, Zitao Zhang, Wei Min, Zhiyao Chen, Yinan Shan, Yang Zhao, and Ce Zhang. 2021. xFraud: explainable fraud transaction detection. _Proceedings of the VLDB Endowment_ 15, 3 (2021), 427–436. 

- [18] Susie Xi Rao, Shuai Zhang, Zhichao Han, Zitao Zhang, Wei Min, Mo Cheng, Yinan Shan, Yang Zhao, and Ce Zhang. 2020. Suspicious Massive Registration Detection via Dynamic Heterogeneous Graph Neural Networks. arXiv:2012.10831 [cs.LG] 

- [19] Emanuele Rossi, Ben Chamberlain, Fabrizio Frasca, Davide Eynard, Federico Monti, and Michael Bronstein. 2020. Temporal graph networks for deep learning on dynamic graphs. _arXiv preprint arXiv:2006.10637_ (2020). 

- [20] Aravind Sankar, Yanhong Wu, Liang Gou, Wei Zhang, and Hao Yang. 2020. Dysat: Deep neural representation learning on dynamic graphs via self-attention networks. In _Proceedings of the 13th International Conference on Web Search and Data Mining_ . 519–527. 

- [21] Weiping Song, Chence Shi, Zhiping Xiao, Zhijian Duan, Yewen Xu, Ming Zhang, and Jian Tang. 2019. Autoint: Automatic feature interaction learning via selfattentive neural networks. In _Proceedings of the 28th ACM International Conference on Information and Knowledge Management_ . 1161–1170. 

- [22] Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is All you Need. _ArXiv_ abs/1706.03762 (2017). 

- [23] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. 2017. Graph attention networks. _arXiv preprint arXiv:1710.10903_ (2017). 

- [24] Jianling Wang, Ainur Yessenalina, and Alireza Roshan-Ghias. 2021. Exploring Heterogeneous Metadata for Video Recommendation with Two-tower Model. _arXiv preprint arXiv:2109.11059_ (2021). 

- [25] Jinpeng Wang, Jieming Zhu, and Xiuqiang He. 2021. Cross-Batch Negative Sampling for Training Two-Tower Recommenders. In _Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval_ . 1632–1636. 

- [26] Xuhong Wang, Ding Lyu, Mengjian Li, Yang Xia, Qi Yang, Xinwen Wang, Xinguang Wang, Ping Cui, Yupu Yang, Bowen Sun, and et al. 2021. APAN: Asynchronous Propagation Attention Network for Real-time Temporal Graph Embedding. _Proceedings of the 2021 International Conference on Management of Data_ (Jun 2021). https://doi.org/10.1145/3448016.3457564 

- [27] Ji Yang, Xinyang Yi, Derek Zhiyuan Cheng, Lichan Hong, Yang Li, Simon Xiaoming Wang, Taibai Xu, and Ed H Chi. 2020. Mixed negative sampling for learning two-tower neural networks in recommendations. In _Companion Proceedings of the Web Conference 2020_ . 441–447. 

- [28] Xinyang Yi, Ji Yang, Lichan Hong, Derek Zhiyuan Cheng, Lukasz Heldt, Aditee Ajit Kumthekar, Zhe Zhao, Li Wei, and Ed Chi (Eds.). 2019. _Sampling-BiasCorrected Neural Modeling for Large Corpus Item Recommendations_ . 

- [29] Yantao Yu, Weipeng Wang, Zhoutian Feng, and Daiyue Xue. 2021. A Dual Augmented Two-tower Model for Online Large-scale Recommendation. (2021). 

- [30] Shichang Zhang, Yozen Liu, Yizhou Sun, and Neil Shah. 2021. Graph-less neural networks: Teaching old mlps new tricks via distillation. _arXiv preprint arXiv:2110.08727_ (2021). 

- [31] Hao Zhou, Hong-feng Chai, and Mao-lin Qiu. 2018. Fraud detection within bankcard enrollment on mobile device based payment using machine learning. _Frontiers of Information Technology & Electronic Engineering_ 19, 12 (2018), 1537– 1545. 

- [32] Hongkuan Zhou, Ajitesh Srivastava, Hanqing Zeng, Rajgopal Kannan, and Viktor Prasanna. 2021. Accelerating large scale real-time GNN inference using channel pruning. _arXiv preprint arXiv:2105.04528_ (2021). 

