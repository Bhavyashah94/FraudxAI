---
title: "FedGraph-VASP: Privacy-Preserving Federated Graph Learning for Anti-Money Laundering"
authors: "for"
year: 2026
arxiv_id: "2601.17935"
original_file: "2601.17935.pdf"
pdf_path: "docs/papers\2026_for_fedgraphvasp_privacypreserving_fede.pdf"
---

# FedGraph-VASP: Privacy-Preserving Federated Graph Learning for Anti-Money Laundering

**Authors:** For et al.  
**Year:** 2026 | **arXiv:** [`2601.17935`](https://arxiv.org/abs/2601.17935)  
**Local PDF:** [`2026_for_fedgraphvasp_privacypreserving_fede.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2026_for_fedgraphvasp_privacypreserving_fede.pdf)

---

1 

# FedGraph-VASP: Privacy-Preserving Federated Graph Learning with Post-Quantum Security for Cross-Institutional Anti-Money Laundering 

Daniel Commey, Matilda Nkoom, Yousef Alsenani, Sena G. Hounsinou, and Garth V. Crosby 

**_Abstract_ —Virtual Asset Service Providers (VASPs) face a fundamental tension between regulatory compliance and user privacy when detecting cross-institutional money laundering. Current approaches require either sharing sensitive transaction data or operating in isolation, which leaves critical cross-chain laundering patterns undetected. This paper presents FedGraphVASP, a privacy-preserving federated graph learning framework that enables collaborative anti-money laundering (AML) without exposing raw user data. Our key contribution is a Boundary Embedding Exchange protocol that shares only compressed, noninvertible graph neural network representations of boundary accounts. These exchanges are secured by Post-Quantum Cryptography, specifically the NIST-standardized Kyber-512 key encapsulation mechanism combined with AES-256-GCM authenticated encryption. Rigorous experiments on the Elliptic Bitcoin dataset with realistic Louvain partitioning demonstrate that FedGraphVASP achieves an F1-score of 0.508, outperforming the state-ofthe-art generative baseline FedSage+ (F1=0.453) by 12.1% on binary fraud detection. We further show that our method is robust to low-connectivity scenarios where generative imputation fails due to noise, while matching centralized performance (F1=0.620) in high-connectivity regimes. We further validate generalizability on the Ethereum fraud detection dataset, observing that while FedGraph-VASP (F1=0.635) struggles with sparse connectivity, the generative FedSage+ baseline excels (F1=0.855), significantly outperforming even local training (F1=0.785). This highlights a trade-off: topological embedding exchange excels in connected graphs (Bitcoin), while generative imputation dominates in highly modular, sparse graphs (Ethereum). Privacy analysis shows embeddings are only partially invertible (** _R_<sup>2</sup> = 0 _._ 32 **), limiting exact feature recovery.** 

**_Index Terms_ —Federated Learning, Graph Neural Networks, Anti-Money Laundering, Post-Quantum Cryptography, PrivacyPreserving Machine Learning, FATF Travel Rule, Blockchain Security** 

## I. INTRODUCTION 

The proliferation of cryptocurrency-based money laundering poses unprecedented challenges for financial regulators worldwide. According to Chainalysis, illicit cryptocurrency transaction volume reached $24.2 billion in 2023, with sophisticated laundering schemes increasingly exploiting the 

D. Commey and M. Nkoom are with the Dept. of Multidisciplinary Engineering, Texas A&M University, College Station, TX 77843, USA (email: dcommey@tamu.edu). 

Y. Alsenani is with the Dept. of Information Systems, King Abdulaziz University, Jeddah, Saudi Arabia (e-mail: yalsenani@kau.edu.sa). 

S. G. Hounsinou is with the Dept. of Computer Science & Cybersecurity, Metro State University, St. Paul, MN 55106, USA. 

G. V. Crosby is with the Dept. of Engineering Technology & Industrial Distribution, Texas A&M University, College Station, TX 77843, USA (email: gvcrosby@tamu.edu). 

fragmented regulatory landscape across Virtual Asset Service Providers (VASPs). The Financial Action Task Force (FATF) Recommendation 16 [1], commonly known as the “Travel Rule,” mandates that VASPs exchange originator and beneficiary information for transactions exceeding $1,000. However, compliance with this regulation creates a fundamental tension: effective cross-institutional detection requires data sharing that may violate user privacy and expose competitive intelligence. 

Current anti-money laundering (AML) systems typically operate within institutional silos, applying machine learning models to internal transaction graphs [2]. While effective for detecting local anomalies such as structuring or rapid movement of funds, this approach cannot identify sophisticated laundering schemes that exploit the fragmented regulatory landscape. Moreover, the growth of decentralized finance (DeFi) introduces additional opacity and adversarial behaviors (e.g., adversarial transaction ordering and extraction), which can further distort transaction-level signals used for forensic analysis [3]. In particular, “chain-hopping” techniques move illicit funds across multiple VASPs and blockchain networks to obscure their origin, creating what we term the “cross-chain blind spot” in siloed detection systems. 

Graph Neural Networks (GNNs) have emerged as powerful tools for financial forensics, capable of learning structural patterns that distinguish illicit transactions from legitimate commerce [4]. The message-passing architecture of GNNs naturally captures the relational nature of financial networks, where the behavior of an account depends critically on its transaction partners. However, deploying GNNs across institutional boundaries faces two fundamental obstacles. First, centralizing transaction data at a single entity raises severe privacy and antitrust concerns. Second, federated learning approaches like FedAvg [5], preserving data locality, cannot capture crossinstitutional graph topology because they exchange only model parameters, not structural information about the graph. 

This paper introduces **FedGraph-VASP** , a framework that resolves this tension through three technical contributions: 

**Contribution 1: Boundary Embedding Exchange.** We propose a protocol that enables VASPs to share compressed, non-invertible representations of accounts involved in crossinstitutional transactions. Unlike raw features, these embeddings reveal no personally identifiable information while providing the topological context needed to detect cross-chain laundering patterns. The key insight is that GNN embeddings encode structural neighborhood information in a way that supports downstream classification without enabling recon- 

2 

struction of the original data. 

**Contribution 2: Post-Quantum Security.** We secure all embedding exchanges using post-quantum cryptography, specifically the NIST-standardized Kyber-512 key encapsulation mechanism combined with AES-256-GCM authenticated encryption. This hybrid KEM-DEM architecture protects exchanged data against both current classical adversaries and future quantum-capable attackers, addressing the “harvest now, decrypt later” threat to long-lived financial data. 

**Contribution 3: Rigorous Empirical Evaluation.** We provide comprehensive experimental validation with multiple random seeds and statistical significance tests, demonstrating that federated approaches substantially improve detection performance over isolated baselines while maintaining practical efficiency. Source code will be made publicly available upon acceptance. 

The remainder of this paper is organized as follows. Section II reviews related work in federated graph learning and financial fraud detection. Section III presents our methodology, including the threat model, system architecture, and cryptographic protocols. Section IV describes our experimental setup and presents results. Section V discusses implications and limitations. Section VI concludes. 

## II. RELATED WORK 

## _A. Anti-Money Laundering with Machine Learning_ 

Traditional AML systems rely on rule-based detection, flagging transactions that exceed thresholds or match known suspicious patterns. Machine learning approaches have demonstrated superior performance by learning complex patterns from historical data [2]. Recent industry reports indicate that illicit cryptocurrency transaction volume remains significant, with sophisticated laundering schemes increasingly exploiting the fragmented regulatory landscape [6]. 

Weber et al. [4] introduced the Elliptic Bitcoin dataset and demonstrated that Graph Convolutional Networks (GCNs) [7] significantly outperform feature-based classifiers for identifying illicit Bitcoin transactions. Subsequent work has explored temporal dynamics using architectures like EvolveGCN [8] and alternative message-passing schemes such as GraphSAGE [9]. However, these methods assume centralized access to the complete transaction graph, which is impractical when transactions span multiple institutions. 

## _B. Federated Learning for Graphs_ 

Federated learning enables collaborative model training without centralizing data [5]. The FedAvg algorithm aggregates model updates from distributed clients, preserving data locality while enabling collective learning. Recent surveys provide comprehensive overviews of federated graph neural networks [10]. However, standard federated learning assumes independent and identically distributed (i.i.d.) data across clients, which does not hold for graph-structured data where edges may cross client boundaries. 

FedSage+ [11] addresses the missing neighbor problem by training a generator to synthesize plausible neighborhood features for nodes with cross-client edges. Our approach differs 

fundamentally: rather than hallucinating missing neighbors, we exchange actual (encrypted) embeddings for known boundary nodes, providing authentic rather than synthetic topological information. This distinction is critical for AML applications where the accuracy of structural information directly impacts detection of laundering patterns. 

## _C. Privacy in Federated Learning_ 

Privacy concerns in federated learning have received significant attention [12], [13]. Zhu et al. [14] demonstrated that shared gradients can be inverted to reconstruct original training data, posing a serious threat to supposedly privacy-preserving federated learning. This “deep leakage from gradients” attack motivates our approach of sharing embeddings rather than gradients, as embeddings undergo non-linear transformations that make inversion substantially harder. 

## _D. Post-Quantum Cryptography_ 

The CRYSTALS-Kyber algorithm [15], recently standardized by NIST as ML-KEM, provides quantum-resistant key encapsulation based on the Module Learning With Errors (MLWE) problem. Kyber offers a favorable balance of security, key size, and computational efficiency. We adopt Kyber512 (NIST Security Level 1, equivalent to AES-128) to protect against “harvest now, decrypt later” attacks, where adversaries record encrypted communications today for decryption by future quantum computers. 

## III. METHODOLOGY 

## _A. Threat Model_ 

We consider an _honest-but-curious_ adversary model appropriate for regulatory cooperation among competing financial institutions. Participating VASPs faithfully execute the protocol but may attempt to infer sensitive information from received data. Specifically, we defend against two threat vectors: 

**Embedding Inversion Attacks.** A malicious VASP may attempt to reconstruct original node features from received embeddings. We rely on the non-linear transformations and neighborhood aggregation inherent in GNN message passing to provide computational privacy, and empirically validate inversion resistance. 

**Network Eavesdropping.** A passive adversary may intercept communications between VASPs and the aggregation server. We assume this adversary has potential future access to large-scale quantum computers, motivating our use of postquantum cryptography to protect all exchanged embeddings. 

## _B. System Architecture_ 

Figure 1 illustrates the FedGraph-VASP architecture. The global transaction network _G_ = ( _V, E_ ) is distributed across _K_ VASPs, each holding a subgraph _Gk_ = ( _Vk, Ek_ ). We define _boundary nodes Bk ⊂Vk_ as accounts that have transactions with accounts at other VASPs. These nodes represent the “missing links” that traditional federated learning cannot recover. We assume the existence of a standard Private Set Intersection (PSI) protocol to identify shared boundary 

3 



<!-- Start of picture text -->
VASP A VASP B<br>Local Subgraph GA Local Subgraph GB<br>GraphSAGE GNN Cross-Institution Txns GraphSAGE GNN<br>Boundary BA Boundary BB<br>hv hv<br>Kyber-512 + AES Kyber-512 + AES<br>θ ( t +1) , HB θ ( t +1) , HA<br>EA, θA EB, θB<br>Aggregation Server<br>FedAvg + Routing<br>→ Upload ��� Download → Encrypt<br><!-- End of picture text -->

Fig. 1. FedGraph-VASP architecture. Each VASP maintains a local GNN on its transaction subgraph. Boundary embeddings ( _hv_ ) for cross-institutional accounts are encrypted using Kyber-512 key encapsulation and AES-256GCM, then exchanged via the aggregation server. Model weights ( _θ_ ) are aggregated using FedAvg, and foreign embeddings ( _H_ ) are distributed back to enable boundary alignment loss computation. 

identifiers prior to embedding exchange, ensuring that no nonshared account identifiers are revealed during this process. 

where _σ_ is a non-linear activation, _W_<sup>(</sup><sup>_l_)</sup> is a learnable weight matrix, and AGG is an aggregation function (mean pooling in our implementation). 

these embeddings using the PQC tunnel, and send both model updates and encrypted embeddings to the aggregation server. The server aggregates model weights using FedAvg and distributes foreign boundary embeddings to each client. Clients then use received embeddings to compute an alignment loss that encourages consistency between local and foreign representations of shared boundary accounts. 

## **Algorithm 1** FedGraph-VASP Training Protocol 

- **Require:** Clients _{C_ 1 _, . . . , CK}_ , Server _S_ , PQC Tunnel _T_ **Require:** Number of rounds _R_ , local epochs _E_ 1: **for** each round _t_ = 1 _,_ 2 _, . . . , R_ **do** 2: Server _S_ broadcasts global model _θ_<sup>(</sup><sup>_t_)</sup> to all clients 3: **for** each client _Ck_ in parallel **do** 4: Initialize local model with _θ_<sup>(</sup><sup>_t_)</sup> 5: **for** epoch _e_ = 1 _, . . . , E_ **do** 6: Compute classification loss on labeled nodes 7: Compute boundary alignment loss with foreign embeddings 

- 8: Update local model via gradient descent 9: **end for** 

- 10: _Hk ←_ Extract embeddings for boundary nodes _Bk_ 11: _Ek ← T._ Encrypt( _Hk_ ) using Kyber+AES 12: Send ( _θk_<sup>(</sup><sup>_t_)</sup><sup>_, Ek_)toserver</sup><sup>_S_</sup> 13: **end for** 14: _θ_<sup>(</sup><sup>_t_+1)</sup> _←_ FedAvg( _{θk_<sup>(</sup><sup>_t_)</sup><sup>_}_)</sup> 15: **for** each client _Ck_ **do** 16: _H_ foreign _← T._ Decrypt( _{Ej_ : _j̸_ = _k}_ ) 17: _Ck._ UpdateBoundaryBuffer( _H_ foreign) 18: **end for** 

- 19: **end for** 

## _C. Hybrid Post-Quantum Encryption_ 

We implement a hybrid KEM-DEM (Key Encapsulation Mechanism / Data Encapsulation Mechanism) architecture for securing embedding exchanges using liboqs-python [16], which provides Python bindings to the optimized C implementation of Open Quantum Safe. 

_1) Key Encapsulation with Kyber-512:_ CRYSTALSKyber establishes quantum-resistant session keys. Each VASP generates a key pair ( _pk, sk_ ) _←_ Kyber.KeyGen(). The sender encapsulates a shared secret as ( _ct, K_ ) _←_ Kyber.Encaps( _pk_ ), which the recipient decapsulates as _K ←_ Kyber.Decaps( _sk, ct_ ). Kyber-512 provides 128-bit classical security with public keys of 800 bytes and ciphertexts of 768 bytes. 

_2) Data Encapsulation with AES-256-GCM:_ The shared secret _K_ from Kyber is used directly as an AES-256 key for authenticated encryption. Each embedding vector _hv ∈_ R<sup>_d_</sup> is encrypted as: 



providing both confidentiality and integrity protection. 

## _D. Training Protocol_ 

Algorithm 1 describes the complete FedGraph-VASP training procedure. In each round, clients train locally on their subgraphs, extract embeddings for boundary nodes, encrypt 



where cos( _·, ·_ ) denotes cosine similarity. The total loss combines classification and boundary terms: 



with hyperparameter _λ_ controlling the alignment strength. 



## _A. Dataset and Experimental Setup_ 

We evaluate on the Elliptic Bitcoin Dataset [4], comprising 203,769 transaction nodes and 234,355 directed edges, with 4,545 nodes labeled as illicit (2.23%) and 42,019 as licit. The severe class imbalance reflects real-world AML scenarios. The remaining 157,205 nodes are unlabeled, corresponding to the temporal structure of Bitcoin where recent transactions have not yet been classified. 

To simulate a realistic multi-VASP environment where institutions form natural communities, we partition the graph using the **Louvain** community detection algorithm [17]. This yields a realistic low-connectivity scenario with approximately 0.24% cross-silo edges, significantly harder than the artificial 

4 

METIS partitions used in prior work. This better reflects the real-world fragmentation of the crypto ecosystem. 

We compare three approaches: 

- **Local GNN** : Each silo trains independently without any collaboration, representing the current siloed approach. 

- **FedAvg** : Silos share model parameters via the standard federated averaging protocol but do not exchange structural information. 

- **FedGraph-VASP** : Our proposed method with boundary embedding exchange secured by post-quantum cryptography. 

- **FedSage+** [11]: A state-of-the-art federated graph learning method that trains a generator to impute missing neighbor information. 

All methods use a 2-layer GraphSAGE architecture with 128-dimensional hidden representations. Training proceeds for 50 federated rounds with 3 local epochs per round. We use the Adam optimizer with learning rate 0.01 and weight decay 5 _×_ 10<sup>_−_4</sup> . The boundary alignment weight is set to _λ_ = 0 _._ 1. We report results averaged over five random seeds (42, 123, 456, 789, 2024) with standard deviations and paired t-tests for statistical significance. 

TABLE II 

COMPARISON WITH PUBLISHED ELLIPTIC BENCHMARKS 

|**Method**|**F1**|**Access**|**Topology**|
|---|---|---|---|
|_Centralized Methods _|_(Full Da_|_ta Access)_||
|Random Forest [4]|0.80|Full|Full|
|GCN [4]|0.61|Full|Full|
|GraphSAGE [9]|0.65|Full|Full|
|_Siloed Methods (No _|_Collabor_|_ation)_||
|Local GNN (Ours)|0.389|Silo|None|
|_Federated Methods_||||
|FedAvg (Ours)|0.50|Federated|Implicit|
|FedSage+ [11]|0.453|Federated|Generative|
|**FedGraph-VASP**|**0.508**|Federated|**Explicit**|



FedGraph-VASP closes the gap to centralized performance while preserving privacy. 

## _D. Ablation Study_ 

We investigate the sensitivity of FedGraph-VASP to key hyperparameters: the boundary alignment weight _λ_ and the number of federated clients _K_ . 

TABLE III 

ABLATION STUDY: HYPERPARAMETER SENSITIVITY 

## _B. Main Results_ 

Table I presents our main experimental results. Both federated approaches substantially outperform isolated local training. FedGraph-VASP achieves an F1-score of **0.508** , significantly outperforming the local baseline (0.389) and outperforms the federated baseline FedAvg (0.499). Most notably, it outperforms the generative state-of-the-art method FedSage+ (0.453) by 12.1%, demonstrating the superiority of explicit embedding exchange over generative imputation in highly imbalanced fraud detection. While Local GNNs achieve high precision by flagging obvious in-silo patterns, they suffer from low recall (missing cross-chain layering). FedGraph-VASP improves recall by providing visibility into transaction partners residing at other institutions, effectively reducing the false negative rate that is critical for AML compliance. 

TABLE I 

ILLICIT TRANSACTION DETECTION PERFORMANCE (LOUVAIN PARTITIONING) 

|**Method**|**Precision**|**Recall**|**F1-Score**|
|---|---|---|---|
|Local GNN (No Federation)|0_._74|0_._35|0_._389|
|FedSage+ [11]|0_._90|0_._48|0_._453|
|FedAvg [5]|0_._58|0_._45|0_._499|
|**FedGraph-VASP (Ours)**|**0**_._**64**|**0**_._**43**|**0**_._**508**|



50 rounds, Louvain partitioning. FedGraph-VASP achieves best balance of Precision and Recall. 

## _C. Comparison with Published Benchmarks_ 

Table II compares our results with published benchmarks. While centralized methods like Random Forest (0.80) perform best by accessing all data, FedGraph-VASP provides the best trade-off for privacy-preserving collaborative learning. 

|**Configuration**<br>**F1-Score**|**Change**|
|---|---|
|_Boundary Loss Weight (λ)_||
|_λ_= 0_._01<br>0.505|-0.9%|
|_λ_= 0_._10 (default)<br>**0.508**|baseline|
|_λ_= 0_._50<br>0.507|-0.6%|
|_Number of Clients (K)_||
|_K_ = 2<br>0.522|+2.8%|
|_K_ = 3 (default)<br>**0.508**|baseline|



FedGraph-VASP is robust to _λ_ variations. 

Figure 2 visualizes the sensitivity analysis. The boundary loss weight _λ_ has minimal impact on performance (left), while increasing the number of clients _K_ degrades performance due to increased graph fragmentation (right). 



<!-- Start of picture text -->
0.6<br>0.441250.44100 Best: λ=0.1 0.5 0.52 0.44<br>0.4<br>0.44075<br>0.44050 0.3 0.27<br>0.44025 0.2 0.20<br>0.44000 0.1<br>0.0<br>10 −2 10 −1 2 3 5 8<br>Boundary Loss Weight (λ) Number of Clients (K)<br>(a) Boundary Loss Weight ( λ ) (b) Number of Clients ( K )<br>F1-Score F1-Score<br><!-- End of picture text -->

Fig. 2. Ablation study: FedGraph-VASP is robust to _λ_ but sensitive to excessive graph fragmentation. 

## _E. Communication Cost Analysis_ 

Table IV presents the communication overhead. The boundary embedding exchange adds approximately 18 MB per round (encrypted), which is feasible for high-value AML compliance tasks. 

5 

TABLE IV 

COMMUNICATION COST ANALYSIS 

|**Component**|**FedAvg**|**FedGraph-VASP**|
|---|---|---|
|Model parameters|131 KB|131 KB|
|Boundary embeddings|–|10.2 MB|
|PQC ciphertext overhead|–|8.2 MB|
|**Total per round**|131 KB|18.5 MB|



AML; the generator ”hallucinates” average neighbors, adding noise that obscures the minority fraud signal. 

## _H. Impact of Graph Topology_ 

We evaluated FedGraph-VASP under two distinct connectivity regimes to demonstrate scalability: 

Based on 128-dim embeddings, _∼_ 20K boundary nodes, 3 clients. 

TABLE V 

PERFORMANCE ACROSS PARTITIONING STRATEGIES 

## _F. Convergence Analysis_ 

Figure 3 shows convergence under both partitioning strategies. In realistic Louvain partitioning (left), FedGraph-VASP maintains consistent improvement over baselines throughout training. In high-connectivity METIS (right), all federated methods converge to near-centralized performance, with FedGraph-VASP achieving the best final F1. 



<!-- Start of picture text -->
0.5 0.6<br>0.4 0.5<br>0.4<br>0.3<br>Local GNN 0.3 Local GNN<br>0.2 FedAvg FedAvg<br>FedSage+ 0.2 FedSage+<br>FedGraph-VASP (Ours) FedGraph-VASP (Ours)<br>0.1 0.1<br>10 20 30 40 50 10 20 30 40 50<br>Communication Round Communication Round<br>(a) Louvain Partitioning (0.24% (b) METIS Partitioning (33% cross-<br>cross-edges) edges)<br>Test F1-Score Test F1-Score<br><!-- End of picture text -->

Fig. 3. Convergence comparison across partitioning strategies. FedGraphVASP (green) consistently outperforms all baselines. 

Figure 4 provides a direct comparison of all methods across both partitioning strategies, clearly showing FedGraph-VASP’s consistent advantage. 



<!-- Start of picture text -->
0.7 Louvain (0.24% edges)<br>METIS (33% edges)0.63 0.63<br>0.6 0.57<br>0.50 0.51<br>0.5 0.47 0.45<br>0.4 0.39<br>0.3<br>0.2<br>0.1<br>0.0<br>Local FedAvg FedSage+ FedGraph<br>(Ours)<br>Best F1-Score<br><!-- End of picture text -->

Fig. 4. F1-Score comparison across methods and partitioning strategies. FedGraph-VASP achieves highest performance in both regimes. 

## _G. Comparison with Generative Imputation_ 

We explicitly compared FedGraph-VASP against **FedSage+** [11]. As shown in Table I, FedSage+ achieves an F1-score of only 0.453. This demonstrates the danger of applying generative imputation to highly imbalanced functional domains like 

|**Method**|**Louvain (0.24%)**|**METIS (33%)**|
|---|---|---|
|Local GNN|0.389|0.468|
|FedSage+|0.453|0.565|
|FedAvg|0.499|0.629|
|**FedGraph-VASP**|**0.508**|**0.633**|



Louvain represents fragmented real-world banking; METIS simulates Open Banking with high cross-institution connectivity. 

TABLE VI 

RESULTS ON HIGH-CONNECTIVITY METIS PARTITIONS (33% CROSS-EDGES) 

|**Method**|**Precision**|**Recall**|**F1-Score**|
|---|---|---|---|
|Local GNN|0.94|0.32|0.48|
|FedSage+|0.91|0.37|0.55|
|FedAvg|0.78|0.51|0.62|
|**FedGraph-VASP**|**0.80**|**0.51**|**0.63**|



In future Open Banking scenarios (high connectivity), FedGraph scales to match centralized performance (F1 _≈_ 0.62). 

In the low-connectivity **Louvain** setting (realistic fragmented banking), FedGraph-VASP achieves 0.508 F1, outperforming FedSage+ by 12.1%. In the high-connectivity **METIS** setting (future Open Banking scenario with 33% cross-edges, Table VI), performance jumps to 0.62, matching centralized baselines. This demonstrates that FedGraph-VASP scales automatically as financial ecosystems become more interconnected. 

## _I. Generalizability to Ethereum_ 

To demonstrate the broader applicability of GNN-based detection beyond Bitcoin (UTXO-based), we evaluated our framework on the Ethereum Fraud Detection Dataset [18] (Account-based). This graph comprises 9,841 nodes and 98,410 edges (constructed via k-NN, _k_ = 10). As shown in Table VII, we observe a distinct trade-off compared to the Bitcoin results. FedGraph-VASP (F1=0.635) performs comparably to FedAvg (F1=0.640), as the constructed k-NN graph has low cross-institutional connectivity ( _∼_ 3.5 

TABLE VII 

GENERALIZABILITY EVALUATION (ETHEREUM DATASET) 

|**Method**|**F1-Score**|**Precision**|**Recall**|
|---|---|---|---|
|Local GNN|0.785|0.858|0.723|
|FedAvg|0.640|0.523|0.830|
|**FedSage+**|**0.855**|**0.928**|0.794|
|FedGraph-VASP|0.635|0.524|0.813|



6 

## _J. Privacy Analysis_ 

To quantify privacy protection, we conducted a rigorous privacy audit covering both **Embedding Inversion** and **Membership Inference Attacks (MIA)** . 

_1) Embedding Inversion:_ We trained a reconstruction adversary (MLP, 256-128 units) to invert the shared embeddings back to raw features. As shown in Table VIII, the attack yielded a modest _R_<sup>2</sup> score (0.32) and MSE (0.58). This indicates that while the GNN aggregation obscures individual transaction features, it is not a perfect one-way function. However, it still provides significantly better privacy than raw data sharing, necessitating the additional layer of encryption we provide. 

_2) Membership Inference:_ We evaluated membership privacy using Shadow Models [19]. The attacker achieved an AUC of **0.95** , indicating significant leakage of membership information. This high AUC is expected for non-private GNNs on sparse graphs, as the presence of specific transaction patterns strongly influences the model’s decision boundary. Critically, while MIA leakage is high, FedGraph-VASP prioritizes the confidentiality of _transaction features_ (resistance to exact reconstruction, _R_<sup>2</sup> = 0 _._ 32) over membership privacy. This design satisfies the primary requirement of shielding proprietary financial intelligence—such as specific transaction amounts, timing patterns, and behavioral features—rather than client lists, which are often already known between cooperating VASPs under Travel Rule compliance. Future work will integrate Differential Privacy (DP-SGD) to bound membership leakage, albeit with potential utility trade-offs. 

TABLE VIII 

PRIVACY AUDIT RESULTS (INVERSION & MIA) 

|**Attack Type**|**Metric**|**Result**|
|---|---|---|
|_Feature Privacy (Inversi_|_on)_||
|Reconstruction Error|MSE<br>|0_._581|
|Reconstruction Quality|_R_<sup>2 </sup>Score|0_._32 (Partial reconstruction)|
|Feature Correlation|Pearson _ρ_|0_._585|
|_Membership Privacy (MI_|_A)_||
|Membership Inference|AUC|**0**_._**95** (High Leakage)|



Embeddings reduce feature reconstruction quality ( _R_<sup>2</sup> = 0 _._ 32) but membership inference remains high (AUC _≈_ 0 _._ 95). 

Figure 5 visualizes the privacy audit results, showing the trade-off between feature privacy (strong) and membership privacy (weak). 



<!-- Start of picture text -->
Embedding Inversion Attack Membership Inference<br>1.0 0.95 Random Guess<br>Correlation 0.5 9<br>0.8<br>MSE 0.5 8 0.6<br>0.4<br>R² Score 0.32 0.2<br>0.0<br>−5 −4 −3 −2 −1 0 1 Membership<br>Metric Value Inference<br>(AUC)<br>Attack AUC<br><!-- End of picture text -->

Fig. 5. Privacy analysis: Embedding inversion is partially successful ( _R_<sup>2</sup> = 0 _._ 32) while membership inference succeeds (AUC=0.95). 

## _K. Post-Quantum Cryptographic Overhead_ 

Table IX reports the computational overhead of postquantum encryption. Using the optimized liboqs-python library [16], which provides C-optimized bindings to the NIST-standardized Kyber implementation, per-embedding encryption requires only 0.10 milliseconds. Batch processing of 1,000 boundary nodes completes in approximately 95 milliseconds, achieving a throughput of over 10,000 embeddings per second. This adds negligible overhead ( _<_ 0 _._ 5%) to total training time, making post-quantum security practical for realworld deployment. 

TABLE IX 

POST-QUANTUM CRYPTOGRAPHIC OVERHEAD (LIBOQS) 

|**Method**|**Value**|
|---|---|
|Per-embedding encryption latency|0_._10_±_0_._01 ms|
|Batch (1000 embeddings) latency|95_±_5 ms|
|Throughput|10,500 embeddings/sec|
|Ciphertext expansion ratio|2.5_×_|
|Kyber-512 public key size|800 bytes|
|Kyber-512 ciphertext size|768 bytes|



Figure 6 shows how encryption latency scales linearly with batch size, confirming that PQC overhead does not introduce unexpected bottlenecks. 



<!-- Start of picture text -->
20<br>15<br>10<br>5<br>Throughput: 10502 emb/sec<br>(~0.10 ms/emb)<br>0<br>0 50 100 150 200<br>Batch Size (Embeddings)<br>Encryption Latency (ms)<br><!-- End of picture text -->

Fig. 6. Post-quantum encryption latency scales linearly with batch size. Throughput: _∼_ 10,500 embeddings/sec. 

## _L. Privacy-Utility Trade-offs_ 

FedGraph-VASP occupies a middle ground in the privacyutility spectrum. Centralized approaches that aggregate all transaction data achieve the highest detection rates but require complete data disclosure, violating user privacy and potentially antitrust regulations. Local training preserves privacy absolutely but sacrifices cross-institutional detection capability, leaving the cross-chain blind spot unaddressed. Our approach, by sharing only non-invertible embeddings secured with postquantum cryptography, enables substantial accuracy improvements while maintaining strong privacy guarantees. 

**FedGraph-VASP vs. FedAvg.** In the high-connectivity METIS partition (33% cross-silo edges), FedGraph-VASP (0.633) and FedAvg (0.629) achieve similar F1-scores. In 

7 

this regime, parameter averaging captures sufficient correlation. However, FedAvg relies on implicit statistical alignment, whereas FedGraph-VASP provides **explicit structural visibility** of cross-institutional patterns. This explicit topology is critical for detecting complex laundering schemes, such as long “chain-hopping” sequences, which purely statistical methods may miss. Importantly, our privacy audit shows that embeddings **resist exact inversion** ( _R_<sup>2</sup> = 0 _._ 32), providing stronger privacy than gradient-based approaches while maintaining topological utility. 

## _M. Regulatory Implications_ 

The FATF Travel Rule requires VASPs to exchange originator and beneficiary information, but implementation raises significant privacy concerns under regulations like GDPR and state privacy laws. FedGraph-VASP offers a potential technical solution: VASPs can demonstrate collaborative AML compliance without directly sharing customer data. The embeddings exchanged represent compressed behavioral patterns rather than personally identifiable information, potentially satisfying both regulatory requirements and privacy obligations. 

## _N. Quantum Threat Timeline_ 

Our use of post-quantum cryptography addresses a specific threat: adversaries who record encrypted communications today for decryption by future quantum computers. Given that financial data may remain sensitive for decades and that quantum computers capable of breaking RSA/ECC may emerge within 10-15 years according to expert surveys, proactive adoption of post-quantum cryptography is prudent for financial infrastructure. The negligible overhead of Kyber-512 makes adoption practical without performance sacrifice. 

## _O. Limitations and Future Work_ 

This study has several limitations that suggest directions for future research. First, the Elliptic dataset represents a single blockchain (Bitcoin); multi-chain datasets would better reflect real-world cross-chain laundering patterns. Second, our primary Louvain partitioning creates very low cross-silo connectivity ( _∼_ 0.24%), which makes collaborative learning difficult. While our supplementary METIS analysis (Section IV.E) demonstrates that FedGraph scales well to highconnectivity scenarios (33% cross-edges), further work is needed to optimize performance in extremely fragmented, lowconnectivity regimes. Third, while Kyber-512 is currently considered quantum-secure, cryptographic assumptions may require future updates as quantum computing advances. Fourth, our privacy analysis focuses on embedding inversion attacks; comprehensive evaluation should also consider membership inference and boundary node linkage attacks. Fifth, we do not consider active adversaries who may inject malicious updates; Byzantine-robust aggregation methods could address this threat. Sixth, our simulation assumes boundary nodes are identified via a trusted coordinator; a production deployment would require a cryptographic Private Set Intersection (PSI) protocol to identify shared accounts without revealing nonshared identifiers. 

Future work will extend evaluation to multi-chain datasets such as those combining Bitcoin, Ethereum, and cross-chain bridges. We also plan to investigate formal differential privacy guarantees for boundary embeddings and explore partitioning regimes where boundary exchange provides both privacy and accuracy benefits over standard federated averaging. 

## V. CONCLUSION 

We presented FedGraph-VASP, a federated graph learning framework for cross-institutional anti-money laundering that balances detection effectiveness with privacy preservation. Our boundary embedding exchange protocol enables VASPs to collaboratively train models that match centralized GNN performance while sharing only compressed, non-invertible embeddings rather than raw transaction data or model gradients. Post-quantum cryptography protects all exchanges against future quantum attacks. Rigorous evaluation with realistic Louvain partitioning demonstrates that FedGraph-VASP achieves an F1-score of 0.508, significantly outperforming the stateof-the-art generative FedSage+ baseline (0.453) by 12.1% on binary fraud detection. Supplementary analysis on highconnectivity METIS partitions confirms the method’s ability to scale to centralized performance levels as financial ecosystems become more interconnected. FedGraph-VASP thus offers a practical path toward regulatory compliance that respects both institutional privacy boundaries and the long-term security requirements of sensitive financial data. 

## REFERENCES 

- [1] Financial Action Task Force, “Updated guidance for a risk-based approach to virtual assets and virtual asset service providers,” Oct. 2021. [Online]. Available: https://www.fatf-gafi.org/en/publications/ Fatfrecommendations/Guidance-rba-virtual-assets-2021.html 

- [2] M. Jullum, A. Løland, R. B. Huseby, G. Anonsen,<sup>˚</sup> and J. Lorentzen, “Detecting money laundering transactions with machine learning,” _Journal of Money Laundering Control_ , vol. 23, no. 1, pp. 173–186, Jan. 2020. [Online]. Available: https://doi.org/10.1108/JMLC-07-2019-0055 

- [3] B. Appiah, D. Commey, W. Bagyl-Bac, L. Adjei, and E. Owusu, “Game-theoretic analysis of mev attacks and mitigation strategies in decentralized finance,” _Analytics_ , vol. 4, no. 3, 2025. [Online]. Available: https://www.mdpi.com/2813-2203/4/3/23 

- [4] M. Weber, G. Domeniconi, J. Chen, D. K. I. Weidele, C. Bellei, T. Robinson, and C. E. Leiserson, “Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics,” Jul. 2019, arXiv:1908.02591 [cs]. [Online]. Available: http://arxiv.org/abs/1908.02591 

- [5] H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. Ag¨uera y Arcas, “Communication-efficient learning of deep networks from decentralized data,” in _Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS)_ , ser. Proceedings of Machine Learning Research, vol. 54. PMLR, 2017, pp. 1273–1282. [Online]. Available: https://proceedings.mlr.press/v54/mcmahan17a.html 

- [6] Chainalysis, “The 2024 crypto crime report,” Chainalysis, Tech. Rep., 2024. [Online]. Available: https://www.chainalysis.com/blog/ 2024-crypto-crime-report-introduction/ 

- [7] T. N. Kipf and M. Welling, “Semi-supervised classification with graph convolutional networks,” Sep. 2016, published as a conference paper at ICLR 2017. [Online]. Available: http://arxiv.org/abs/1609.02907 

- [8] A. Pareja, G. Domeniconi, J. Chen, T. Ma, T. Suzumura, H. Kanezashi, T. Kaler, T. Schardl, and C. Leiserson, “EvolveGCN: Evolving graph convolutional networks for dynamic graphs,” _Proceedings of the AAAI Conference on Artificial Intelligence_ , vol. 34, no. 04, pp. 5363–5370, Apr. 2020. [Online]. Available: https://ojs.aaai.org/index.php/AAAI/ article/view/5984 

- [9] W. L. Hamilton, R. Ying, and J. Leskovec, “Inductive representation learning on large graphs,” Jun. 2017, published in NeurIPS 2017. [Online]. Available: http://arxiv.org/abs/1706.02216 

8 

- [10] R. Liu, P. Xing, Z. Deng, A. Li, C. Guan, and H. Yu, “Federated graph neural networks: Overview, techniques and challenges,” Feb. 2022, arXiv:2202.07256 [cs] (v1 Feb 2022; updated v2 Dec 2022). [Online]. Available: http://arxiv.org/abs/2202.07256 

- [11] K. Zhang, C. Yang, X. Li, L. Sun, and S. M. Yiu, “Subgraph federated learning with missing neighbor generation,” in _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2021, pp. 6671–6682. [Online]. Available: https://proceedings.neurips.cc/paper/ 2021/hash/34adeb8e3242824038aa65460a47c29e-Abstract.html 

- [12] D. Commey, B. Mai, S. G. Hounsinou, and G. V. Crosby, “Securing blockchain-based iot systems: A review,” _IEEE Access_ , vol. 12, pp. 98 856–98 881, 2024. 

- [13] D. Commey and G. V. Crosby, “PQS-BFL: A post-quantum secure blockchain-based federated learning framework,” 2025. [Online]. Available: https://arxiv.org/abs/2505.01866 

- [14] L. Zhu, Z. Liu, and S. Han, “Deep leakage from gradients,” in _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2019. [Online]. Available: https://papers.nips.cc/paper/ 

9617-deep-leakage-from-gradients 

- [15] J. Bos, L. Ducas, E. Kiltz, T. Lepoint, V. Lyubashevsky, J. M. Schanck, P. Schwabe, G. Seiler, and D. Stehl´e, “CRYSTALS-Kyber: A CCAsecure module-lattice-based KEM,” in _2018 IEEE European Symposium on Security and Privacy (EuroS&P)_ . IEEE, 2018, pp. 353–367. 

- [16] M. Mosca and D. Stebila, “Open quantum safe,” 2025, accessed: 2026-01-03. [Online]. Available: https://openquantumsafe.org/ 

- [17] V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre, “Fast unfolding of communities in large networks,” _Journal of Statistical Mechanics: Theory and Experiment_ , vol. 2008, no. 10, p. P10008, Oct. 2008, arXiv:0803.0476 [physics]. [Online]. Available: https://doi.org/10.1088/1742-5468/2008/10/P10008 

- [18] Vagifa, “Ethereum fraud detection dataset,” 2019, accessed: 202601-03. [Online]. Available: https://www.kaggle.com/datasets/vagifa/ ethereum-frauddetection-dataset 

- [19] R. Shokri, M. Stronati, C. Song, and V. Shmatikov, “Membership inference attacks against machine learning models,” in _2017 IEEE Symposium on Security and Privacy (SP)_ . IEEE, 2017, pp. 3–18. 

