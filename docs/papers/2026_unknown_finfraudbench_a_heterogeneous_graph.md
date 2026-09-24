---
title: "FinFraudBench: A Heterogeneous Graph Benchmark for Financial Fraud Detection"
authors: "unknown"
year: 2026
arxiv_id: "2608.15177"
original_file: "2608.15177.pdf"
pdf_path: "docs/papers\2026_unknown_finfraudbench_a_heterogeneous_graph.pdf"
---

# FinFraudBench: A Heterogeneous Graph Benchmark for Financial Fraud Detection

**Authors:** Unknown et al.  
**Year:** 2026 | **arXiv:** [`2608.15177`](https://arxiv.org/abs/2608.15177)  
**Local PDF:** [`2026_unknown_finfraudbench_a_heterogeneous_graph.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2026_unknown_finfraudbench_a_heterogeneous_graph.pdf)

---

Preprint. Under review. 

# FINFRAUDBENCH: A HETEROGENEOUS GRAPH BENCHMARK FOR FINANCIAL FRAUD DETECTION 

**Yixuan Chen**<sup>1</sup><sup>_,_2</sup><sup>_∗_</sup> **Hongyu Zhan**<sup>1</sup><sup>_∗_</sup> **Jie Sheng**<sup>3</sup> **Weiyu Han**<sup>3</sup> **Shuai Chen**<sup>3</sup> **Tianyi Zhang**<sup>3</sup> **Xiao Tan**<sup>3</sup><sup>_†_</sup> **Jun Xia**<sup>1</sup><sup>_,_4</sup><sup>_†_</sup> 1HKUST-GZ 2Jilin University 3Ant Group 4HKUST chenyx2123@mails.jlu.edu.cn, hzhan701@connect.hkust-gz.edu.cn _{_ shengjie.sheng, hanweiyu.hwy, shuai.cs _}_ @ant-intl.com _{_ zty113091, alex.tx _}_ @ant-intl.com junxia@hkust-gz.edu.cn 

## ABSTRACT 

The increasing complexity of digital financial systems has reshaped financial fraud detection from isolated transaction classification into relational risk reasoning over interconnected financial entities. This shift has motivated graph-based fraud detection, where models identify fraudulent nodes by exploiting dependencies among customers, cards, merchants, categories, and locations. However, despite rapid progress in graph-based methods, existing public benchmarks remain misaligned with real-world financial systems in two important aspects. First, they often simplify financial ecosystems into homogeneous or single-node-type multirelational graphs, failing to preserve the multi-entity and multi-relational nature of financial data. Second, they rarely provide large-scale heterogeneous financial graph datasets with realistic operating conditions such as extreme class imbalance and limited label availability, making it difficult to assess the practical effectiveness of current methods. To address these gaps, we present **FinFraudBench** , a heterogeneous graph benchmark for financial fraud detection. FinFraudBench contains two heterogeneous graph datasets ( **CreditCard-Fraud** and **BankTrans-Fraud** ) with up to 8.99M nodes and 89.23M directed typed edges. Each dataset preserves six financial entity types, fourteen directed edge types, and natural fraud rates that mirror deployment constraints. With these datasets, we establish a standardized evaluation protocol covering both ranking and imbalancesensitive classification metrics, and evaluate representative baselines. Extensive experiments yield empirical insights into current methods’ limitations and suggest promising avenues for future research. FinFraudBench is available at https://anonymous.4open.science/r/FinFraudBench-B002. 

## 1 INTRODUCTION 

Financial fraud detection is a central task in modern financial systems, where fraud can cause substantial economic loss and erode trust in digital payment services Bolton & Hand (2002); Phua et al. (2010). Fraud is rarely an isolated property of a single record. A suspicious transaction often becomes easier to identify when considered together with related financial entities and their interactions, such as the customer behind the transaction, the payment instrument, the receiving merchant, and the associated context. This relational nature has motivated graph-based fraud detection, where models can capture dependencies that are difficult to represent from tabular records alone in fraud analysis Akoglu et al. (2015); Ma et al. (2023); Liu et al. (2022). 

Existing public graph benchmarks for fraud detection, however, often simplify this financial ecosystem before learning begins. We distinguish three graph formulations in this paper. Here, each node represents an entity instance, such as a transaction, user, account, card, merchant, or location. In a homogeneous graph, transactions, users, or accounts are usually selected as the only node type, and 

> _∗_ Equal contribution. 

> _†_ Corresponding authors. 

1 

Preprint. Under review. 



<!-- Start of picture text -->
(A) Homogeneous Graph (B) Multi-relational Graph (C) Heterogeneous Graph<br><!-- End of picture text -->

Figure 1: Comparison of three graph formulations for financial fraud detection. Homogeneous graphs use one node type and one relation type; multi-relational graphs keep a single target node type while distinguishing multiple relation types; heterogeneous graphs preserve multiple entity types, multiple relation types, and type-specific attributes. 

all edges describe one broad relation, such as a transaction between users or a payment flow between transactions Weber et al. (2019); Huang et al. (2022). A multi-relational graph still keeps a single target node type, but its relation types are often induced by typed meta paths in the original heterogeneous ecosystem, such as two target nodes connected through a shared device, shared account, shared card, or shared merchant Shi et al. (2017); Dong et al. (2017); Rayana & Akoglu (2015); McAuley & Leskovec (2013); Liu et al. (2020); Dou et al. (2020). A heterogeneous graph contains multiple node types and multiple relation types, allowing financial entities and their interactions to be represented directly Shi et al. (2017); Hu et al. (2020b). Homogeneous and multi-relational formulations are useful abstractions and have supported important progress in graph-based fraud detection, but both lose part of the fraud entity-relation structure. 

This representation gap matters for benchmark design. Financial transactions naturally involve multiple entity types, multiple relation semantics, and type-specific attribute spaces. When typed entities are folded into features, converted into target–target edges, or omitted, benchmarks no longer directly test entity- and relation-aware fraud modeling. Figure 1 clearly illustrates this distinction among homogeneous graphs, multi-relational graphs, and heterogeneous graphs considered in this work. To address this gap, we present FinFraudBench, a benchmark consisting of two heterogeneous graph datasets constructed from public financial fraud data sources Shenoy (2020); ComputingVictor (2024); the original sources are transaction-level tables rather than pre-existing graphs. To the best of our knowledge, FinFraudBench is the first benchmark to construct comparatively large heterogeneous graphs specifically for financial fraud detection from public transaction-level sources. Both datasets use a unified schema with transaction nodes as prediction targets and additional typed financial entities as contextual information. FinFraudBench releases the heterogeneous graph as the canonical representation and supports deterministic projections for feature-only, homogeneous, or multi-relational methods. 

FinFraudBench also provides a reproducible evaluation protocol. Each dataset is organized into labeled training transactions, unlabeled training transactions, validation transactions, a full test split, and balanced mini-test subsets, supporting controlled comparison under limited labels and extreme class imbalance in realistic deployment settings. We further reproduce representative baselines across non-GNN, homogeneous GNN, multi-relation, fraud-oriented, and heterogeneous families. The results reveal a clear family-level pattern: methods designed for heterogeneous graphs are strongest overall, multi-relation and fraud-oriented methods remain competitive, and target-only non-GNN baselines are limited by their inability to use relational financial context encoded by the benchmark graph structure during practical financial fraud detection tasks. 

The main contributions of this work are summarized as follows: 

- **Heterogeneous financial fraud graph benchmarks.** We construct two heterogeneous graph datasets from public transaction-level fraud sources. The datasets preserve multiple financial entity types, multiple relation types, and type-specific attributes, while also supporting deterministic simplified views for methods that require homogeneous or multirelational graph inputs. 

- **Reproducible limited-label evaluation protocol.** We provide unified graph schemas, labeled and unlabeled training transactions, validation splits, balanced mini-test subsets, and 

2 

Preprint. Under review. 

standardized metrics to support controlled benchmarking under label scarcity and extreme class imbalance in a unified evaluation setting. 

- **Empirical insights for heterogeneous fraud detection.** Our experiments show that heterogeneous graph structures preserve rich signals encoded in typed financial entities and relations, which are essential for fraud modeling. These results point to a promising direction: extending fraud-oriented designs to heterogeneous architectures, so that typed structural information and domain-specific fraud cues can be jointly exploited. 

## 2 PRELIMINARIES AND RELATED WORK 

### 2.1 PRELIMINARIES 

**Homogeneous graphs.** We define the three graph formulations used in this paper. A homogeneous attributed graph is written as _G_ = ( _V, E,_ **X** ), where _V_ is the node set, _E_ is the edge set, and **X** _∈_ R<sup>_|V|×d_</sup> is a shared node feature matrix. It assumes one node type and one edge type. 

**Multi-relational graphs.** A multi-relational graph is a single-node-type graph with multiple relation types, written as _G_ = ( _V, E, R,_ **X** _, ϕ_ ), where _R_ is the relation-type set and _ϕ_ : _E →R_ assigns each edge to a relation type. Equivalently, _E_ =<sup>�</sup> _r∈R_<sup>_Er_with</sup><sup>_Er_=</sup><sup>_{e ∈E_:</sup><sup>_ϕ_(</sup><sup>_e_) =</sup><sup>_r}_. This formulation</sup> captures relation heterogeneity while retaining a single node type. 

**Heterogeneous graphs.** A heterogeneous graph is written as _G_ = ( _V, E, A, R, {_ **X**<sup>_a_</sup> _}a∈A, τ, ϕ_ ), where _A_ is the node-type set, _R_ is the relation-type set, _τ_ : _V →A_ assigns each node to a node type, and _ϕ_ : _E →R_ assigns each edge to a relation type. For each node type _a ∈A_ , nodes of that type are collected as _Va_ = _{v ∈V_ : _τ_ ( _v_ ) = _a}_ and have their own feature matrix **X**<sup>_a_</sup> _∈_ R<sup>_|Va|×da_</sup> . In our constructed benchmark, this stricter heterogeneous graph setting captures both relation-level and entity-level heterogeneity. 

**Fraud detection task.** Given a graph _G_ in one of the above formulations, we formulate financial fraud detection as binary node classification over a target node type. Let _a_<sup>_⋆_</sup> be the target type, _Va⋆_ be its nodes, and _VL ⊆Va⋆_ be the labeled training nodes. Unlabeled target nodes may remain in the graph as relational context but do not contribute to the supervised loss. Given labels _yv ∈{_ 0 _,_ 1 _}_ , a model assigns each target node a fraud score 



where _γ_ is a decision threshold. The supervised objective is 



In FinFraudBench, the target type is transaction, while customers, cards, merchants, categories, and locations provide relational context. 

### 2.2 RELATED WORK 

**Graph-based fraud detection.** Fraud detection has been studied using tabular transaction features, anomaly detection, and graph-based learning Bolton & Hand (2002); Phua et al. (2010); Chandola et al. (2009); Breunig et al. (2000); Liu et al. (2008); Akoglu et al. (2015); Ma et al. (2023). General GNN backbones provide message-passing, convolutional, inductive, attention-based, and scalable neighborhood aggregation mechanisms Scarselli et al. (2009); Gilmer et al. (2017); Kipf & Welling (2016); Hamilton et al. (2017); Veliˇckovi´c et al. (2017); Chiang et al. (2019); Zeng et al. (2019); Wu et al. (2021). In fraud detection, graph-based methods represent suspicious behaviors as relational structures among transactions, accounts, users, reviews, devices, and payment flows, while fraud-oriented GNNs further introduce assumptions about noisy neighborhoods, camouflage, label scarcity, partitioned propagation, or attribute association Liu et al. (2018; 2020); Dou et al. (2020); Chen et al. (2024); Zhuo et al. (2024); Duan et al. (2025); Li et al. (2026). These works motivate relational modeling for fraud detection, but their public evaluation settings are usually built on homogeneous graphs or single-node-type multi-relational graphs. 

3 

Preprint. Under review. 

**Heterogeneous graph learning.** Heterogeneous graph learning broadly studies graphs with typed nodes, typed edges, or both. To avoid ambiguity, we use multi-relational graphs for the single-nodetype setting with multiple relation types, and heterogeneous graphs for the setting with multiple node types and multiple relation types. Heterogeneous information network research formalizes entity types, relation types, and meta-path semantics Shi et al. (2017); Dong et al. (2017), while neural models learn relation-specific transformations, meta-path-based attention, learned composite relations, and node- and edge-type-dependent attention Schlichtkrull et al. (2018); Wang et al. (2019); Fu et al. (2020); Yun et al. (2019); Hu et al. (2020b); Yang et al. (2023). These methods are relevant to financial fraud detection because financial risk data naturally involve different entity roles and relation semantics, yet public fraud benchmarks rarely expose these elements together with type-specific attributes. 

**Fraud datasets and benchmarks.** Public benchmarks strongly influence how fraud detection models are designed and evaluated. YelpChi and Amazon are widely used in graph-based fraud detection; although not financial datasets, they test whether models handle noisy and suspicious relational patterns Rayana & Akoglu (2015); McAuley & Leskovec (2013); Zhang et al. (2020). In common graph-fraud settings, however, they are usually treated as single-node-type multi-relational graphs, where all nodes share the same prediction target type and edge types encode alternative relations between target nodes Liu et al. (2020); Dou et al. (2020). Financial fraud benchmarks such as Elliptic and DGraph are closer to our domain, but they are representative homogeneous graphs: Elliptic connects Bitcoin transaction nodes through payment flows, while DGraph models financial users with temporal interaction edges, strong class imbalance, and many unlabeled nodes Weber et al. (2019); Huang et al. (2022). Recent efforts such as H<sup>2</sup> GB construct large-scale heterogeneous graphs across domains, highlighting the value of realistic structural properties, but they are not specifically designed for fraud detection Lin et al. (2025). Benchmark studies further show that dataset structure shapes the modeling assumptions methods are expected to exploit Hu et al. (2020a); Dwivedi et al. (2023); Lv et al. (2021); Lin et al. (2025). The lack of public financial fraud benchmarks with heterogeneous graph structure therefore limits the development and evaluation of models that reason over multiple financial entity types, relation types, and type-specific attributes. FinFraudBench fills this gap by providing a unified benchmark with two heterogeneous graph datasets constructed from public transaction-level sources and standardized splits for node-level fraud detection. 

## 3 BENCHMARK CONSTRUCTION 

### 3.1 SOURCE DATA AND CONSTRUCTION PRINCIPLES 

We construct CreditCard-Fraud and BankTrans-Fraud from two public tabular fraud datasets Shenoy (2020); ComputingVictor (2024). Both raw sources are transaction-level tables: each row corresponds to one transaction and contains a fraud label together with non-label fields describing the transaction itself, such as amount and time, and the observable financial context around it, such as customer- or payment-instrument identifiers, merchant and category information, and geographic or billing attributes. These fields are provided as columns in transaction records rather than as separate entity or relation tables. Our goal is to convert such tabular records into heterogeneous graphs while avoiding label leakage in graph or feature construction. Figure 2 summarizes this construction pipeline for both datasets. 

The construction follows three principles. First, recurring financial objects are represented as typed nodes rather than being kept only as transaction attributes. Second, relation types follow the semantic roles between typed entities, so different entity associations are preserved as distinct edge types. Third, labels remain defined only on transaction nodes, while non-transaction nodes provide unlabeled context for limited-label fraud detection. 

### 3.2 GRAPH SCHEMA, ATTRIBUTES, AND LABELS 

Both datasets share a transaction-centered heterogeneous schema with six node types and seven semantic edge types. Transaction nodes are the prediction targets, while customer, card, merchant, category, and location nodes provide typed context, where location denotes state or location fields in the source records. The seven edge types include five transaction-context associations and two 

4 

Preprint. Under review. 



<!-- Start of picture text -->
Raw data Leakage  Remove labels Transactionamt, timedistance Customer Merchant<br>cc_numbertrans_nummerchantcategory 4111 1111 1111 1111T123456789GROCERYM987654 FeatureTyped filtering conditioned statisticsdecompositionRemove fraud-Temporal Customerage gender owns initiates paid to<br>stateamt 123.45CA (Leakage-free)Grouping transformationFeature Normalization Card uses Transaction<br>lat/longtime 2024-05-01 14:23:1137.77, -122.41 Split law record Frequencystatistics cc_numberusage count Card billed in has category<br>merchant_lat/longis_fraud... 37.78, -122.40...1 into typed nodefeatures assignmentType  DeduplicationGroup fields Merchant...merchant IDfrequency lives in Location Category<br>Label only<br><!-- End of picture text -->

Figure 2: Overview of the graph construction pipeline. Public transaction-level tables are converted into heterogeneous graphs by mapping transactions and recurring financial objects to typed nodes, deriving semantic relations between observed entities, constructing type-specific attributes, and assigning fraud labels only to transaction nodes. 

context-context associations, customer–card ownership and customer–location association. Adding reverse edges yields fourteen directed edge types. 

Each source-table row is mapped to one transaction node, with entity-valued fields deduplicated within their own node types. The induced typed edges preserve intermediate entities that link transactions, rather than projecting shared contexts into direct transaction–transaction edges. Node attributes are built from non-label source fields and leakage-free deterministic features, with typespecific dimensions ranging from 7 to 21. Fraud labels are attached only to transaction nodes; all other node types provide unlabeled relational context. A compact schema and feature summary is provided in Appendix A. 

## 4 DATASET STATISTICS AND ANALYSIS 

### 4.1 GRAPH SCALE AND HETEROGENEITY 

Table 1 summarizes the graph-scale and label statistics of the two datasets. CreditCard-Fraud contains 1.86M nodes and 18.53M directed typed edges, while the larger BankTrans-Fraud contains 8.99M nodes and 89.23M directed typed edges. Both datasets share the same schema of six node types and fourteen directed edge types, but differ substantially in scale and fraud prevalence. Although transaction nodes dominate graph size, the non-transaction context nodes are central to the relational structure: they represent customers, cards, merchants, categories, and locations, and link transactions through shared financial entities and contexts instead of collapsing these connections into direct transaction–transaction edges. 

### 4.2 LABEL IMBALANCE AND SPLITS 

Figure 3 visualizes the main transaction split proportions. Each dataset is organized into labeled training transactions, unlabeled training transactions, validation transactions, a full test split, and five balanced mini-test subsets. The labeled training portion is intentionally small overall, about 2% of transactions in each dataset: CreditCard-Fraud contains 37.0K labeled and 1.22M unlabeled training transactions, while BankTrans-Fraud contains 178.3K labeled and 6.78M unlabeled training transactions. Unlabeled training transactions remain in the graph as context, so semi-supervised and transductive methods can use their node attributes and local neighborhoods without observing their labels. The full test set preserves the natural class distribution for realistic evaluation, while balanced mini-test subsets contain 



<!-- Start of picture text -->
(a) (b)<br>CreditCard-Fraud BankTrans-Fraud<br>1.85M transactions 8.91M transactions<br>CreditCard-Fraud BankTrans-Fraud<br>Labeled train 2.0% 2.0%<br>Unlabeled train 66.0% 76.0%<br>Validation 2.0% 2.0%<br>Full test 30.0% 20.0%<br><!-- End of picture text -->

Figure 3: Transaction split proportions of the constructed fraud graphs. 

5 

Preprint. Under review. 

Table 1: Graph-scale and label statistics of the constructed datasets. 

|Dataset|#Trans. nodes|#Total nodes|#Context nodes|#Directed edges|#Fraud trans.|Fraud rate|
|---|---|---|---|---|---|---|
|CreditCard-Fraud|1.85M|1.86M|2.76K|18.53M|9,651|0.5210%|
|BankTrans-Fraud|8.91M|8.99M|72.14K|89.23M|13,332|0.1495%|



equal numbers of fraudulent and non-fraudulent transactions for broader and more stable comparison under extreme class imbalance in deployment-like settings. 

## 5 BENCHMARK TASKS AND EVALUATION PROTOCOL 

The benchmark evaluates transaction-level fraud detection under the splits defined in Section 4.2. The canonical input is the heterogeneous graph constructed in Section 3, and deterministic projections support methods that require feature-only, homogeneous, or multi-relational inputs. 

### 5.1 TASK SETUP 

Given the full graph or one of its projections, the task is binary node classification on transaction nodes. Models may use the structure and attributes available in their input view, but supervised labels are provided only for labeled training transactions. Validation labels are used only for model selection and early stopping. 

### 5.2 METRICS AND REPORTING PROTOCOL 

Our main experiments use the balanced mini-test subsets defined in Section 4.2 to compare ranking and classification behavior under equal fraud/non-fraud weight. We report six complementary metrics for each method. 

**AUROC and AUPRC.** AUROC measures whether fraudulent transactions receive higher risk scores than legitimate transactions across thresholds Fawcett (2006). AUPRC reflects the precision–recall trade-off for the fraud class and is especially important under class imbalance Davis & Goadrich (2006); Saito & Rehmsmeier (2015). Together, they evaluate score ranking before threshold selection in deployment settings. 

**Accuracy and Macro-F1.** Accuracy is usually misleading on naturally imbalanced fraud data, but is informative on our balanced mini-test subsets because both classes contribute equally. Macro-F1 averages the fraud and non-fraud F1 scores and is more sensitive to failures on either class. 

**Fraud F1 and Fraud Recall.** Fraud F1 summarizes positive-class detection while penalizing excessive false positives. Fraud Recall measures the fraction of detected fraud cases and captures missed-fraud risk, but should be interpreted with AUPRC and Fraud F1. 

**Reporting protocol.** In the main benchmark tables, we report mean performance over five balanced mini-test subsets. Unless otherwise stated, model selection uses validation AUPRC. AUROC and AUPRC are ranking metrics, while accuracy, Macro-F1, Fraud F1, and Fraud Recall are thresholddependent classification metrics. 

## 6 EXPERIMENTS 

We evaluate representative baselines that cover different modeling assumptions on the same benchmark. We organize methods into five comparison families. MLP and the target-only LLM prompting probes are non-GNN baselines. GCN and GraphSAGE represent homogeneous graph learning on collapsed graph views Kipf & Welling (2016); Hamilton et al. (2017). R-GCN represents relationaware message passing around transaction nodes Schlichtkrull et al. (2018); ConsisGAD is grouped with multi-relation methods because its evaluated implementation explicitly uses relation-specific graph channels on multi-relation fraud graphs Chen et al. (2024). PMP Zhuo et al. (2024) and GAAP Duan et al. (2025) represent fraud-oriented graph learning methods with assumptions tai- 

6 

Preprint. Under review. 

Table 2: Overall benchmark results on balanced mini-test subsets. Results are averaged over five mini-test subsets and reported as mean _±_ standard deviation. The best result for each dataset and metric is highlighted with boldface and gray shading for visual emphasis. 

|Dataset|Method|Model family|AUROC|AUPRC|Acc.|Macro-F1|Fraud F1|Fraud Recall|
|---|---|---|---|---|---|---|---|---|
||MLP|Non-GNN|0_._880_±_0_._006|0_._905_±_0_._005|0_._754_±_0_._005|0_._739_±_0_._006|0_._678_±_0_._009|0_._517_±_0_._010|
||LLM-ZS|Non-GNN|0_._659_±_0_._005|0_._688_±_0_._009|0_._551_±_0_._003|0_._452_±_0_._004|0_._219_±_0_._006|0_._126_±_0_._004|
||LLM-ICL-4|Non-GNN|0_._807_±_0_._042|0_._850_±_0_._036|0_._684_±_0_._012|0_._650_±_0_._016|0_._541_±_0_._026|0_._374_±_0_._025|
||GCN|Homogeneous GNN|0_._820_±_0_._011|0_._863_±_0_._007|0_._542_±_0_._003|0_._420_±_0_._007|0_._155_±_0_._012|0_._084_±_0_._007|
||GraphSAGE|Homogeneous GNN|0_._905_±_0_._006|0_._928_±_0_._004|0_._768_±_0_._010|0_._756_±_0_._012|0_._700_±_0_._017|0_._542_±_0_._020|
|CreditCard-Fraud|R-GCN|Multi-relation|0_._887_±_0_._007|0_._916_±_0_._004|0_._688_±_0_._007|0_._654_±_0_._009|0_._547_±_0_._014|0_._377_±_0_._013|
||ConsisGAD|Multi-relation|0_._911_±_0_._004|0_._932_±_0_._003|0_._653_±_0_._006|0_._605_±_0_._008|0_._468_±_0_._014|0_._305_±_0_._012|
||PMP|Fraud-oriented|0_._868_±_0_._008|0_._903_±_0_._005|0_._699_±_0_._007|0_._670_±_0_._009|0_._571_±_0_._013|0_._400_±_0_._012|
||GAAP|Fraud-oriented|**0**_._**924**_±_**0**_._**004**|**0**_._**934**_±_**0**_._**003**|0_._716_±_0_._008|0_._691_±_0_._010|0_._605_±_0_._014|0_._437_±_0_._014|
||HAN|Heterogeneous|0_._903_±_0_._004|0_._927_±_0_._002|0_._686_±_0_._008|0_._652_±_0_._011|0_._542_±_0_._017|0_._372_±_0_._016|
||SeHGNN|Heterogeneous|0_._903_±_0_._005|0_._928_±_0_._003|0_._758_±_0_._006|0_._743_±_0_._007|0_._681_±_0_._011|0_._517_±_0_._014|
||HGT|Heterogeneous|0_._915_±_0_._004|**0**_._**934**_±_**0**_._**004**|**0**_._**832**_±_**0**_._**008**|**0**_._**827**_±_**0**_._**008**|**0**_._**799**_±_**0**_._**011**|**0**_._**669**_±_**0**_._**014**|
||MLP|Non-GNN|0_._938_±_0_._004|0_._946_±_0_._004|0_._672_±_0_._003|0_._633_±_0_._004|0_._513_±_0_._007|0_._346_±_0_._006|
||LLM-ZS|Non-GNN|0_._809_±_0_._007|0_._813_±_0_._007|0_._517_±_0_._004|0_._372_±_0_._008|0_._070_±_0_._013|0_._036_±_0_._007|
||LLM-ICL-4|Non-GNN|0_._873_±_0_._019|0_._860_±_0_._012|0_._541_±_0_._032|0_._418_±_0_._063|0_._151_±_0_._111|0_._086_±_0_._068|
||GCN|Homogeneous GNN|0_._948_±_0_._003|0_._949_±_0_._003|0_._726_±_0_._005|0_._706_±_0_._007|0_._629_±_0_._010|0_._464_±_0_._011|
||GraphSAGE|Homogeneous GNN|0_._926_±_0_._002|0_._930_±_0_._003|0_._546_±_0_._004|0_._429_±_0_._008|0_._170_±_0_._014|0_._093_±_0_._009|
|BankTrans-Fraud|R-GCN|Multi-relation|0_._962_±_0_._004|0_._972_±_0_._003|0_._854_±_0_._008|0_._851_±_0_._009|0_._829_±_0_._011|0_._708_±_0_._016|
||ConsisGAD|Multi-relation|0_._966_±_0_._003|0_._975_±_0_._002|0_._822_±_0_._006|0_._816_±_0_._007|0_._784_±_0_._009|0_._644_±_0_._013|
||PMP|Fraud-oriented|0_._959_±_0_._004|0_._968_±_0_._003|0_._816_±_0_._009|0_._810_±_0_._010|0_._775_±_0_._013|0_._634_±_0_._018|
||GAAP|Fraud-oriented|0_._949_±_0_._005|0_._954_±_0_._004|0_._643_±_0_._004|0_._591_±_0_._006|0_._445_±_0_._010|0_._286_±_0_._008|
||HAN|Heterogeneous|0_._969_±_0_._003|0_._977_±_0_._002|0_._881_±_0_._004|0_._880_±_0_._004|0_._865_±_0_._006|0_._763_±_0_._009|
||SeHGNN|Heterogeneous|0_._969_±_0_._002|**0**_._**978**_±_**0**_._**001**|**0**_._**884**_±_**0**_._**003**|**0**_._**882**_±_**0**_._**003**|**0**_._**869**_±_**0**_._**004**|**0**_._**768**_±_**0**_._**007**|
||HGT|Heterogeneous|**0**_._**973**_±_**0**_._**002**|**0**_._**978**_±_**0**_._**001**|0_._779_±_0_._006|0_._768_±_0_._007|0_._717_±_0_._010|0_._559_±_0_._012|





<!-- Start of picture text -->
Non-GNN Homo. Multi-rel. Fraud-or. Hetero.<br>CC BT<br>AUROC AUPRC Acc.<br>1.00 1.000<br>0.975 0.9<br>0.95<br>0.950 0.8<br>0.90 0.925 0.7<br>0.900<br>Macro-F1 Fraud F1 Fraud Recall<br>0.9 0.8<br>0.8<br>0.8 0.6<br>0.7 0.6<br>0.4<br>0.6<br>0.4<br>Non-GNN Homo.Multi-rel.Fraud-or. Hetero. Non-GNN Homo.Multi-rel.Fraud-or. Hetero. Non-GNN Homo.Multi-rel.Fraud-or. Hetero.<br>Non-GNN Homo.Multi-rel.Fraud-or. Hetero. Non-GNN Homo.Multi-rel.Fraud-or. Hetero. Non-GNN Homo.Multi-rel.Fraud-or. Hetero.<br>Best score<br>Best score<br><!-- End of picture text -->

Figure 4: Family-level best results on balanced mini-test subsets. For each metric and model family, bars report the best-performing method within that family in Table 2; CC denotes CreditCard-Fraud and BT denotes BankTrans-Fraud. 

lored to graph fraud or anomaly detection. HAN, SeHGNN, and HGT represent heterogeneous graph learning methods with typed relation, meta-path, semantic, or node- and edge-type-aware message passing Wang et al. (2019); Yang et al. (2023); Hu et al. (2020b). The two LLM probes use Qwen2-7B-Instruct Yang et al. (2024): zero-shot prompting Brown et al. (2020); Kojima et al. (2022) and 4-shot in-context prompting Brown et al. (2020); Min et al. (2022). These probes serve as additional non-GNN references in our benchmark. 

### 6.1 OVERALL BENCHMARK RESULTS 

Table 2 reports method-level results averaged over five balanced mini-test subsets, while Figure 4 summarizes the best method in each family for every dataset and metric. We report AUROC, AUPRC, accuracy, Macro-F1, Fraud F1, and Fraud Recall, grouping methods into non-GNN, homogeneous GNN, multi-relation, fraud-oriented, and heterogeneous families. 

6.2 REPRESENTATION ANALYSIS 

7 

Preprint. Under review. 

Figure 5 complements Figure 4 with a compact family-level mean-score view across the two datasets. The radar profiles show that heterogeneous methods are strongest overall, while multi-relation and fraud-oriented methods remain competitive and non-GNN baselines are consistently weaker. 

**Transaction features provide a strong but incomplete baseline.** MLP reaches Macro-F1 scores of 0.739 and 0.633 on the two datasets, confirming that target-node attributes carry substantial fraud signals. However, it cannot use the customer, card, merchant, 



<!-- Start of picture text -->
Heterogeneous Fraud-oriented Multi-relation<br>Homogeneous Non-GNN<br>CreditCard-Fraud (CC)AUROC BankTrans-Fraud (BT)AUROC<br>Fraud Recall AUPRC Fraud Recall AUPRC<br>Fraud F1 Acc Fraud F1 Acc<br>Macro-F1 Macro-F1<br><!-- End of picture text -->

Figure 5: Family-level mean-score radar across benchmark metrics. 

category, and location nodes exposed by the benchmark. As shown in Table 2, homogeneous propagation is also not consistently beneficial: GCN trails MLP on CreditCard-Fraud, and GraphSAGE improves Macro-F1 there but falls below MLP on the larger graph. This suggests that the main challenge is not merely adding edges, but learning from the heterogeneous relational structure preserved in FinFraudBench. 

**Heterogeneous graph models are strongest overall.** HGT achieves the best accuracy, MacroF1, Fraud F1, and Fraud Recall on CreditCard-Fraud, while GAAP slightly leads AUROC and AUPRC. On BankTrans-Fraud, HGT obtains the best AUROC and AUPRC, while SeHGNN leads the classification metrics. R-GCN also improves substantially on the larger graph, indicating that relation semantics remain useful even without full node-type heterogeneity. Overall, the results support the benchmark motivation that relation semantics, node types, and type-specific attributes provide complementary fraud signals Schlichtkrull et al. (2018); Wang et al. (2019); Yang et al. (2023); Hu et al. (2020b). 

**Relation-aware and fraud-oriented biases remain useful but are not sufficient alone.** GAAP obtains the best AUROC and AUPRC on CreditCard-Fraud, while ConsisGAD and PMP remain competitive on BankTrans-Fraud Chen et al. (2024); Zhuo et al. (2024); Duan et al. (2025). Their gap to the strongest heterogeneous models on threshold-dependent classification metrics suggests that relation channels or fraud-oriented assumptions should be combined with explicit entity-type modeling. Several methods obtain high AUPRC but differ substantially in Fraud Recall; Figure 6 illustrates this metric mismatch and supports reporting both ranking metrics and threshold-dependent classification metrics. The LLM prompting baselines are weaker than most graph learning baselines, although 4-shot in-context prompting consistently improves over zero-shot prompting on both datasets, providing a target-only non-GNN reference point for the benchmark. 

### 6.3 SCALABILITY AND STABILITY ANALYSIS 

Scalability is part of the benchmark rather than a separate engineering detail. CreditCard-Fraud contains 18.53M directed typed edges, and BankTrans-Fraud contains 89.23M, so practical methods 



<!-- Start of picture text -->
(a) CreditCard-Fraud (b) BankTrans-Fraud<br>0.7 0.8<br>0.6 0.6<br>0.5<br>0.4<br>0.4<br>0.2<br>0.3<br>0.90 0.92 0.94 0.94 0.96 0.98<br>AUPRC AUPRC<br>MLP SAGE HAN HGT PMP<br>GCN R-GCN SeHGNN ConsisGAD GAAP<br>Fraud Recall<br><!-- End of picture text -->

Figure 6: AUPRC–Fraud Recall frontier for trained non-LLM baselines, showing that stronger ranking performance does not always lead to higher fraud recall at the selected decision threshold. Higher values indicate better performance on both axes. 

8 

Preprint. Under review. 

must combine predictive quality with sampling or batching strategies. This is especially relevant for graph-based baselines, which can use unlabeled training transactions as context but must do so without full-batch propagation. The balanced mini-test protocol yields stable estimates for most trained baselines across the five subsets, while the two LLM prompting probes show larger standard deviations and are therefore less stable than the graph-learning methods. 

## 7 DISCUSSION 

### 7.1 KEY FINDINGS 

The experiments suggest that FinFraudBench is useful not only for ranking baselines, but also for diagnosing which parts of the released schema a method can exploit. Transaction features, relation channels, entity types, type-specific attributes, and fraud-oriented assumptions contribute complementary signals for multi-entity financial fraud detection. 

**Heterogeneous graph design gives the strongest overall signal.** Across experiments, heterogeneous methods provide the most consistent gains. This suggests that FinFraudBench exposes useful signals through entity types, relation semantics, and type-specific attributes. Homogeneous or single-node-type multi-relational projections simplify this structure and can discard part of the original fraud entity-relation information. 

**Fraud-oriented designs can build on heterogeneous graphs.** Multi-relation and fraud-oriented methods remain competitive on several metrics, showing that relation channels and fraud-oriented inductive biases are useful for financial fraud detection. However, their remaining gap to the strongest heterogeneous methods suggests that these cues are most promising when combined with entity types and type-specific attributes in heterogeneous financial graphs. 

### 7.2 LIMITATIONS AND FUTURE WORK 

FinFraudBench is constructed from public transaction-level tables, so its graph signals are limited by the fields exposed in those sources and may not fully reflect richer real-world fraud contexts. Future work can extend the benchmark with more complete operational signals and develop fraudoriented models designed directly for heterogeneous fraud graphs under limited labels and extreme class imbalance in realistic deployment settings. 

## 8 CONCLUSION 

We presented FinFraudBench, a benchmark with two heterogeneous graph datasets for financial fraud detection constructed from public transaction-level fraud sources. The proposed graphs preserve multiple financial entity types, relation types, type-specific attributes, limited labels, and realistic fraud imbalance. Our baseline reproduction provides family-level insights into how model designs use heterogeneous fraud signals. The results show that heterogeneous GNNs perform best. Multi-relation and fraud-oriented methods remain competitive but less consistent, highlighting the value of preserving heterogeneous financial structure. 

## DATA AVAILABILITY 

The original tabular datasets used in this work are publicly available on Kaggle: https:// www.kaggle.com/datasets/kartik2112/fraud-detection and https://www. kaggle.com/datasets/computingvictor/transactions-fraud-datasets. 

## ETHICS AND REPRODUCIBILITY STATEMENT 

FinFraudBench is built from public transaction-level data and does not involve human-subject experiments or new data collection. The benchmark is intended for fraud detection research rather than operational decision making without additional validation. All preprocessing, split construction, and reported experiments are described in the paper and appendix. The code repository has 

9 

Preprint. Under review. 

been released openly, and the constructed datasets are available on Hugging Face with fixed random splits to support reproduction of the main results. 

## AI USE STATEMENT 

We used AI-assisted tools to support literature search and survey, manuscript writing, language polishing, and formatting during paper preparation. These tools were not used to design the proposed benchmark, construct the datasets, define the experimental protocol, or draw scientific conclusions. All scientific claims, dataset construction, experimental analysis, and final wording were carefully reviewed and approved by the authors. 

10 

Preprint. Under review. 

## REFERENCES 

- Leman Akoglu, Hanghang Tong, and Danai Koutra. Graph based anomaly detection and description: a survey. _Data mining and knowledge discovery_ , 29(3):626–688, 2015. 

- Richard J Bolton and David J Hand. Statistical fraud detection: A review. _Statistical science_ , 17(3): 235–255, 2002. 

- Markus M Breunig, Hans-Peter Kriegel, Raymond T Ng, and J¨org Sander. Lof: identifying densitybased local outliers. In _Proceedings of the 2000 ACM SIGMOD international conference on Management of data_ , pp. 93–104, 2000. 

- Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33:1877–1901, 2020. 

- Varun Chandola, Arindam Banerjee, and Vipin Kumar. Anomaly detection: A survey. _ACM computing surveys (CSUR)_ , 41(3):1–58, 2009. 

- Nan Chen, Zemin Liu, Bryan Hooi, Bingsheng He, Rizal Fathony, Jun Hu, and Jia Chen. Consistency training with learnable data augmentation for graph anomaly detection with limited supervision. In _The twelfth international conference on learning representations_ , 2024. 

- Wei-Lin Chiang, Xuanqing Liu, Si Si, Yang Li, Samy Bengio, and Cho-Jui Hsieh. Cluster-gcn: An efficient algorithm for training deep and large graph convolutional networks. In _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , KDD ’19, pp. 257–266, New York, NY, USA, 2019. Association for Computing Machinery. ISBN 9781450362016. doi: 10.1145/3292500.3330925. URL https://doi.org/10. 1145/3292500.3330925. 

- ComputingVictor. Financial transactions dataset: Analytics. Kaggle dataset, 2024. URL https://www.kaggle.com/datasets/computingvictor/ transactions-fraud-datasets. Accessed: 2026-07-18. 

- Jesse Davis and Mark Goadrich. The relationship between precision-recall and roc curves. In _Proceedings of the 23rd International Conference on Machine Learning_ , ICML ’06, pp. 233–240, New York, NY, USA, 2006. Association for Computing Machinery. ISBN 1595933832. doi: 10.1145/1143844.1143874. URL https://doi.org/10.1145/1143844.1143874. 

- Yuxiao Dong, Nitesh V. Chawla, and Ananthram Swami. metapath2vec: Scalable representation learning for heterogeneous networks. In _Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’17, pp. 135–144, New York, NY, USA, 2017. Association for Computing Machinery. ISBN 9781450348874. doi: 10.1145/3097983.3098036. URL https://doi.org/10.1145/3097983.3098036. 

- Yingtong Dou, Zhiwei Liu, Li Sun, Yutong Deng, Hao Peng, and Philip S Yu. Enhancing graph neural network-based fraud detectors against camouflaged fraudsters. In _Proceedings of the 29th ACM international conference on information & knowledge management_ , pp. 315–324, 2020. 

- Mingjiang Duan, Da He, Tongya Zheng, Lingxiang Jia, Mingli Song, Xinyu Wang, and Zunlei Feng. Global attribute-association pattern aggregation for graph fraud detection. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 39, pp. 11616–11624, 2025. 

- Vijay Prakash Dwivedi, Chaitanya K Joshi, Anh Tuan Luu, Thomas Laurent, Yoshua Bengio, and Xavier Bresson. Benchmarking graph neural networks. _Journal of Machine Learning Research_ , 24(43):1–48, 2023. 

- Tom Fawcett. An introduction to roc analysis. _Pattern Recognition Letters_ , 27(8):861–874, 2006. ISSN 0167-8655. doi: https://doi.org/10.1016/j.patrec.2005.10.010. URL https://www. sciencedirect.com/science/article/pii/S016786550500303X. ROC Analysis in Pattern Recognition. 

11 

Preprint. Under review. 

- Xinyu Fu, Jiani Zhang, Ziqiao Meng, and Irwin King. Magnn: Metapath aggregated graph neural network for heterogeneous graph embedding. In _Proceedings of the web conference 2020_ , pp. 2331–2341, 2020. 

- Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, and George E. Dahl. Neural message passing for quantum chemistry. In Doina Precup and Yee Whye Teh (eds.), _Proceedings of the 34th International Conference on Machine Learning_ , volume 70 of _Proceedings of Machine Learning Research_ , pp. 1263–1272. PMLR, 06–11 Aug 2017. URL https: //proceedings.mlr.press/v70/gilmer17a.html. 

- Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. _Advances in neural information processing systems_ , 30, 2017. 

- Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. Open graph benchmark: Datasets for machine learning on graphs. _Advances in neural information processing systems_ , 33:22118–22133, 2020a. 

- Ziniu Hu, Yuxiao Dong, Kuansan Wang, and Yizhou Sun. Heterogeneous graph transformer. In _Proceedings of the web conference 2020_ , pp. 2704–2710, 2020b. 

- Xuanwen Huang, Yang Yang, Yang Wang, Chunping Wang, Zhisheng Zhang, Jiarong Xu, Lei Chen, and Michalis Vazirgiannis. Dgraph: A large-scale financial dataset for graph anomaly detection. _Advances in Neural Information Processing Systems_ , 35:22765–22777, 2022. 

- Thomas N Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. _arXiv preprint arXiv:1609.02907_ , 2016. 

- Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. _Advances in neural information processing systems_ , 35:22199–22213, 2022. 

- Yuan Li, Jun Hu, Bryan Hooi, Bingsheng He, and Cheng Chen. Dgp: A dual-granularity prompting framework for fraud detection with graph-enhanced llms. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 40, pp. 15171–15179, 2026. 

- Junhong Lin, Xiaojie Guo, Shuaicheng Zhang, Yada Zhu, and Julian Shun. When heterophily meets heterogeneity: Challenges and a new large-scale graph benchmark. In _Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2_ , pp. 5607–5618, 2025. 

- Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation forest. In _2008 eighth ieee international conference on data mining_ , pp. 413–422. IEEE, 2008. 

- Kay Liu, Yingtong Dou, Yue Zhao, Xueying Ding, Xiyang Hu, Ruitong Zhang, Kaize Ding, Canyu Chen, Hao Peng, Kai Shu, et al. Bond: Benchmarking unsupervised outlier node detection on static attributed graphs. _Advances in Neural Information Processing Systems_ , 35:27021–27035, 2022. 

- Zhiwei Liu, Yingtong Dou, Philip S Yu, Yutong Deng, and Hao Peng. Alleviating the inconsistency problem of applying graph neural network to fraud detection. In _Proceedings of the 43rd international ACM SIGIR conference on research and development in information retrieval_ , pp. 1569–1572, 2020. 

- Ziqi Liu, Chaochao Chen, Xinxing Yang, Jun Zhou, Xiaolong Li, and Le Song. Heterogeneous graph neural networks for malicious account detection. In _Proceedings of the 27th ACM international conference on information and knowledge management_ , pp. 2077–2085, 2018. 

- Qingsong Lv, Ming Ding, Qiang Liu, Yuxiang Chen, Wenzheng Feng, Siming He, Chang Zhou, Jianguo Jiang, Yuxiao Dong, and Jie Tang. Are we really making much progress? revisiting, benchmarking and refining heterogeneous graph neural networks. In _Proceedings of the 27th ACM SIGKDD conference on knowledge discovery & data mining_ , pp. 1150–1160, 2021. 

12 

Preprint. Under review. 

- Xiaoxiao Ma, Jia Wu, Shan Xue, Jian Yang, Chuan Zhou, Quan Z. Sheng, Hui Xiong, and Leman Akoglu. A comprehensive survey on graph anomaly detection with deep learning. _IEEE Transactions on Knowledge and Data Engineering_ , 35(12):12012–12038, 2023. doi: 10.1109/TKDE.2021.3118815. 

- Julian John McAuley and Jure Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. In _Proceedings of the 22nd International Conference on World Wide Web_ , WWW ’13, pp. 897–908, New York, NY, USA, 2013. Association for Computing Machinery. ISBN 9781450320351. doi: 10.1145/2488388.2488466. URL https://doi.org/10.1145/2488388.2488466. 

- Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer. Rethinking the role of demonstrations: What makes in-context learning work? In Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (eds.), _Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing_ , pp. 11048–11064, Abu Dhabi, United Arab Emirates, December 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022. emnlp-main.759. URL https://aclanthology.org/2022.emnlp-main.759/. 

- Clifton Phua, Vincent Lee, Kate Smith, and Ross Gayler. A comprehensive survey of data miningbased fraud detection research. _arXiv preprint arXiv:1009.6119_ , 2010. 

- Shebuti Rayana and Leman Akoglu. Collective opinion spam detection: Bridging review networks and metadata. In _Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’15, pp. 985–994, New York, NY, USA, 2015. Association for Computing Machinery. ISBN 9781450336642. doi: 10.1145/2783258.2783370. URL https: //doi.org/10.1145/2783258.2783370. 

- Takaya Saito and Marc Rehmsmeier. The precision-recall plot is more informative than the roc plot when evaluating binary classifiers on imbalanced datasets. _PloS one_ , 10(3):e0118432, 2015. 

- Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini. The graph neural network model. _IEEE Transactions on Neural Networks_ , 20(1):61–80, 2009. doi: 10.1109/TNN.2008.2005605. 

- Michael Schlichtkrull, Thomas N Kipf, Peter Bloem, Rianne Van Den Berg, Ivan Titov, and Max Welling. Modeling relational data with graph convolutional networks. In _European semantic web conference_ , pp. 593–607. Springer, 2018. 

- Kartik Shenoy. Credit card transactions fraud detection dataset. _Kaggle. Available online: https://www. kaggle. com/datasets/kartik2112/fraud-detection (accessed on 29 July 2023)_ , 2020. 

- Chuan Shi, Yitong Li, Jiawei Zhang, Yizhou Sun, and Philip S. Yu. A survey of heterogeneous information network analysis. _IEEE Transactions on Knowledge and Data Engineering_ , 29(1): 17–37, 2017. doi: 10.1109/TKDE.2016.2598561. 

- Petar Veliˇckovi´c, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. _arXiv preprint arXiv:1710.10903_ , 2017. 

- Xiao Wang, Houye Ji, Chuan Shi, Bai Wang, Yanfang Ye, Peng Cui, and Philip S Yu. Heterogeneous graph attention network. In _The world wide web conference_ , pp. 2022–2032, 2019. 

- Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I Weidele, Claudio Bellei, Tom Robinson, and Charles E Leiserson. Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. _arXiv preprint arXiv:1908.02591_ , 2019. 

- Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long, Chengqi Zhang, and Philip S. Yu. A comprehensive survey on graph neural networks. _IEEE Transactions on Neural Networks and Learning Systems_ , 32(1):4–24, 2021. doi: 10.1109/TNNLS.2020.2978386. 

- An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jianxin Yang, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin 

13 

Preprint. Under review. 

Yang, Mei Li, Mingfeng Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren, Xuejing Liu, Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zhifang Guo, and Zhihao Fan. Qwen2 technical report, 2024. URL https://arxiv.org/abs/2407.10671. 

- Xiaocheng Yang, Mingyu Yan, Shirui Pan, Xiaochun Ye, and Dongrui Fan. Simple and efficient heterogeneous graph neural network. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 37, pp. 10816–10824, 2023. 

- Seongjun Yun, Minbyul Jeong, Raehyun Kim, Jaewoo Kang, and Hyunwoo J Kim. Graph transformer networks. _Advances in neural information processing systems_ , 32, 2019. 

- Hanqing Zeng, Hongkuan Zhou, Ajitesh Srivastava, Rajgopal Kannan, and Viktor Prasanna. Graphsaint: Graph sampling based inductive learning method. _arXiv preprint arXiv:1907.04931_ , 2019. 

- Shijie Zhang, Hongzhi Yin, Tong Chen, Quoc Viet Nguyen Hung, Zi Huang, and Lizhen Cui. Gcnbased user representation learning for unifying robust recommendation and fraudster detection. In _Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval_ , SIGIR ’20, pp. 689–698, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450380164. doi: 10.1145/3397271.3401165. URL https: //doi.org/10.1145/3397271.3401165. 

- Wei Zhuo, Zemin Liu, Bryan Hooi, Bingsheng He, Guang Tan, Rizal Fathony, and Jia Chen. Partitioning message passing for graph fraud detection. _arXiv preprint arXiv:2412.00020_ , 2024. 

14 

Preprint. Under review. 

## A ADDITIONAL DATASET DETAILS 

### A.1 TYPE-SPECIFIC FEATURE FIELDS 

Table 3 lists representative non-label feature groups used to build node attributes. The two graphs share the same node and relation schema, but the feature dimension of the same node type can differ across datasets because the two source tables expose different raw fields. In all cases, both graphs avoid label leakage in graph and feature construction. 

Table 3: Representative non-label feature groups by node type. 

|Node type|Representative feature groups|
|---|---|
|transaction<br>customer<br>card|amount, time fields, location fields, distance or transaction context<br>profile encodings, location fields, transaction counts and amount statistics<br>billing/context encodings, transaction counts, amount statistics, unique en-<br>tity counts|
|merchant<br>category|category encoding, transaction counts, amount statistics, unique cus-<br>tomer/card/state counts<br>transaction counts,<br>amount statistics,<br>unique merchant/customer/card<br>counts|
|location|transaction<br>counts,<br>amount<br>statistics,<br>unique<br>entity<br>counts,<br>loca-<br>tion/population summaries|



### A.2 DETAILED TRANSACTION SPLITS 

Table 4 reports the split statistics behind the compact split summary in the main paper. The unlabeled training split keeps transaction nodes available as graph context while hiding their labels from supervised training. 

Table 4: Detailed transaction split statistics. 

|Dataset|Split|#Transactions|#Fraud|#Benign|Fraud rate|
|---|---|---|---|---|---|
||train<br>~~l~~abeled|37.05K|214|36.83K|0.5776%|
|CditCdFd|train<br>~~u~~nlabeled|1.22M|7.08K|1.22M|0.5789%|
|rear-rau|validation|37.05K|214|36.83K|0.5776%|
||full<br>~~t~~est|555.72K|2.15K|553.57K|0.3860%|
||train<br>~~l~~abeled|178.30K|268|178.03K|0.1503%|
|BkTFd|train<br>~~u~~nlabeled|6.78M|10.13K|6.77M|0.1495%|
|anrans-rau|validation|178.30K|268|178.03K|0.1503%|
||full<br>~~t~~est|1.78M|2.67K|1.78M|0.1495%|



15 

Preprint. Under review. 

### A.3 COMPLETE BALANCED MINI-TEST RESULTS 

Tables 5 and 6 report the complete balanced mini-test results, including Fraud Precision, which is omitted from the main table to keep the main comparison compact. 

Table 5: Complete balanced mini-test results on CreditCard-Fraud. Values are means and standard deviations across five mini-test subsets. 

|Method|AUROC|AUPRC|Acc.||Macro-F1|Fraud F1|Fraud Prec.|Fraud Recall|
|---|---|---|---|---|---|---|---|---|
|MLP|0_._8798_±_0_._0057|0_._9046_±_0_._0052|0_._7539_±_0_._0050|0_._7393|_±_0_._0059 0_._6775|_±_0_._0087|0_._9822_±_0_._0020|0_._5172_±_0_._0103|
|GCN|0_._8199_±_0_._0107|0_._8632_±_0_._0067|0_._5416_±_0_._0033|0_._4204|_±_0_._0065 0_._1554|_±_0_._0115|0_._9861_±_0_._0099|0_._0844_±_0_._0068|
|GraphSAGE|0_._9046_±_0_._0059|0_._9279_±_0_._0044|0_._7681_±_0_._0102|0_._7556|_±_0_._0118 0_._7003|_±_0_._0167|0_._9890_±_0_._0044|0_._5422_±_0_._0195|
|R-GCN|0_._8870_±_0_._0072|0_._9163_±_0_._0044|0_._6876_±_0_._0066|0_._6542|_±_0_._0088 0_._5466|_±_0_._0137|0_._9957_±_0_._0030|0_._3768_±_0_._0128|
|HAN|0_._9025_±_0_._0038|0_._9269_±_0_._0024|0_._6858_±_0_._0080|0_._6515|_±_0_._0108 0_._5422|_±_0_._0170|0_._9978_±_0_._0023|0_._3724_±_0_._0160|
|SeHGNN|0_._9026_±_0_._0048|0_._9279_±_0_._0026|0_._7575_±_0_._0059|0_._7426|_±_0_._0073 0_._6807|_±_0_._0111|0_._9959_±_0_._0041|0_._5172_±_0_._0137|
|HGT|0_._9150_±_0_._0035|0_._9339_±_0_._0036|0_._8317_±_0_._0077|0_._8271|_±_0_._0082 0_._7990|_±_0_._0106|0_._9911_±_0_._0042|0_._6694_±_0_._0140|
|ConsisGAD|0_._9110_±_0_._0042|0_._9315_±_0_._0031|0_._6526_±_0_._0058|0_._6049|_±_0_._0084 0_._4676|_±_0_._0135|1_._0000_±_0_._0000|0_._3052_±_0_._0115|
|PMP|0_._8683_±_0_._0075|0_._9029_±_0_._0053|0_._6992_±_0_._0068|0_._6697|_±_0_._0086 0_._5709|_±_0_._0129|0_._9949_±_0_._0048|0_._4004_±_0_._0120|
|GAAP|0_._9237_±_0_._0037|0_._9344_±_0_._0033|0_._7155_±_0_._0077|0_._6915|_±_0_._0096 0_._6054|_±_0_._0142|0_._9873_±_0_._0062|0_._4366_±_0_._0142|
|LLM-ZS|0_._6591_±_0_._0046|0_._6877_±_0_._0086|0_._5510_±_0_._0032|0_._4519|_±_0_._0039 0_._2189|_±_0_._0059|0_._8412_±_0_._0249|0_._1258_±_0_._0036|
|LLM-ICL-4|0_._8067_±_0_._0417|0_._8495_±_0_._0360|0_._6839_±_0_._0120|0_._6501|_±_0_._0164 0_._5414|_±_0_._0260|0_._9841_±_0_._0051|0_._3739_±_0_._0247|



Table 6: Complete balanced mini-test results on BankTrans-Fraud. Values are means and standard deviations across five mini-test subsets. 

|Method|AUROC<br>AUPRC|Acc.||Macro-F1|Fraud F1|Fraud Prec.|Fraud Recall|
|---|---|---|---|---|---|---|---|
|MLP|0_._9384_±_0_._0043 0_._9456_±_0_._0041|0_._6718_±_0_._0030|0_._6329|_±_0_._0042 0_._5133|_±_0_._0068|0_._9926_±_0_._0032|0_._3462_±_0_._0063|
|GCN|0_._9476_±_0_._0032 0_._9486_±_0_._0030|0_._7257_±_0_._0052|0_._7055|_±_0_._0065 0_._6285|_±_0_._0099|0_._9732_±_0_._0051|0_._4642_±_0_._0111|
|GraphSAGE|0_._9263_±_0_._0019 0_._9302_±_0_._0026|0_._5460_±_0_._0043|0_._4286|_±_0_._0082 0_._1696|_±_0_._0144|0_._9915_±_0_._0093|0_._0928_±_0_._0086|
|R-GCN|0_._9615_±_0_._0039 0_._9717_±_0_._0028|0_._8542_±_0_._0082|0_._8510|_±_0_._0087 0_._8292|_±_0_._0112|1_._0000_±_0_._0000|0_._7084_±_0_._0164|
|HAN|0_._9687_±_0_._0028 0_._9766_±_0_._0021 <br>|0_._8813_±_0_._0043 <br>|0_._8796 <br>|_±_0_._0044 0_._8654 <br>|_±_0_._0055 <br>|0_._9995_±_0_._0012 <br>|0_._7630_±_0_._0088<br>|
|SeHGNN|0_._9689_±_0_._0019 0_._9784_±_0_._0012|0_._8838_±_0_._0032|0_._8822|_±_0_._0034 0_._8686|_±_0_._0041|0_._9995_±_0_._0007|0_._7680_±_0_._0065|
|HGT|0_._9729_±_0_._0020 0_._9784_±_0_._0009|0_._7793_±_0_._0062|0_._7680|_±_0_._0071 0_._7170|_±_0_._0100|0_._9989_±_0_._0016|0_._5592_±_0_._0116|
|ConsisGAD|0_._9657_±_0_._0031 0_._9751_±_0_._0019|0_._8221_±_0_._0064|0_._8163|_±_0_._0071 0_._7835|_±_0_._0095|1_._0000_±_0_._0000|0_._6442_±_0_._0129|
|PMP|0_._9592_±_0_._0036 0_._9685_±_0_._0027|0_._8163_±_0_._0090|0_._8099|_±_0_._0099 0_._7752|_±_0_._0134|0_._9978_±_0_._0009|0_._6340_±_0_._0179|
|GAAP|0_._9493_±_0_._0049 0_._9544_±_0_._0042|0_._6427_±_0_._0039|0_._5907|_±_0_._0060 0_._4447|_±_0_._0099|0_._9973_±_0_._0037|0_._2862_±_0_._0083|
|LLM-ZS<br>LLM-ICL-4|0_._8087_±_0_._0072 0_._8127_±_0_._0074 <br> 0_._8725_±_0_._0186 0_._8598_±_0_._0120|0_._5174_±_0_._0041 <br> 0_._5406_±_0_._0321|0_._3720 <br> 0_._4179|_±_0_._0076 0_._0697 <br>_±_0_._0628 0_._1513|_±_0_._0131 <br>_±_0_._1111|0_._9587_±_0_._0504 <br> 0_._9561_±_0_._0144|0_._0362_±_0_._0070<br> 0_._0856_±_0_._0678|



### A.4 MINI-TEST STABILITY 

Figure 7 reports the coefficient of variation across the five balanced mini-test subsets for each metric and trained non-LLM baseline. The figure complements the averaged results in the main paper by showing that the balanced mini-test protocol gives stable estimates for most graph-learning baselines. 



<!-- Start of picture text -->
(a) CreditCard-Fraud (b) BankTrans-Fraud<br>MLP 0.7 0.6 0.7 0.8 1.3 2.0 0.5 0.4 0.4 0.7 1.3 1.8<br>GCN 1.3 0.8 0.6 1.5 7.4 8.1 0.3 0.3 0.7 0.9 1.6 2.4<br>GraphSAGE 0.7 0.5 1.3 1.6 2.4 3.6 0.2 0.3 0.8 1.9 8.5 9.3<br>R-GCN 0.8 0.5 1.0 1.3 2.5 3.4 0.4 0.3 1.0 1.0 1.4 2.3<br>HAN 0.4 0.3 1.2 1.7 3.1 4.3 0.3 0.2 0.5 0.5 0.6 1.2<br>SeHGNN 0.5 0.3 0.8 1.0 1.6 2.6 0.2 0.1 0.4 0.4 0.5 0.8<br>HGT 0.4 0.4 0.9 1.0 1.3 2.1 0.2 0.1 0.8 0.9 1.4 2.1<br>ConsisGAD 0.5 0.3 0.9 1.4 2.9 3.8 0.3 0.2 0.8 0.9 1.2 2.0<br>PMP 0.9 0.6 1.0 1.3 2.3 3.0 0.4 0.3 1.1 1.2 1.7 2.8<br>GAAP 0.4 0.4 1.1 1.4 2.3 3.3 0.5 0.4 0.6 1.0 2.2 2.9<br>0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0<br>CV across five mini-test subsets (%)<br>AUROC AUPRC Acc.Macro-F1 Fraud F1Fraud Recall AUROC AUPRC Acc.Macro-F1 Fraud F1Fraud Recall<br><!-- End of picture text -->

Figure 7: Stability of balanced mini-test evaluation. Heatmaps report the coefficient of variation across five mini-test subsets; lighter cells indicate more stable estimates. 

16 

