---
title: "CARE-GNN: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters"
authors: "unknown"
year: 2020
arxiv_id: "2008.08692"
original_file: "2008.08692.pdf"
pdf_path: "docs/papers\2020_unknown_caregnn_enhancing_graph_neural_netw.pdf"
---

# CARE-GNN: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters

**Authors:** Unknown et al.  
**Year:** 2020 | **arXiv:** [`2008.08692`](https://arxiv.org/abs/2008.08692)  
**Local PDF:** [`2020_unknown_caregnn_enhancing_graph_neural_netw.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_unknown_caregnn_enhancing_graph_neural_netw.pdf)

---

# **Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters** 

Yingtong Dou<sup>1</sup> , Zhiwei Liu<sup>1</sup> , Li Sun<sup>2</sup> , Yutong Deng<sup>2</sup> , Hao Peng<sup>3</sup> , Philip S. Yu<sup>1</sup> 

1Department of Computer Science, University of Illinois at Chicago 

2School of Computer Science, Beijing University of Posts and Telecommunications 

3Beijing Advanced Innovation Center for Big Data and Brain Computing, Beihang University {ydou5,zliu213,psyu}@uic.edu,{l.sun,buptdyt}@bupt.edu.cn,penghao@act.buaa.edu.cn 

## **ABSTRACT** 

Graph Neural Networks (GNNs) have been widely applied to fraud detection problems in recent years, revealing the suspiciousness of nodes by aggregating their neighborhood information via different relations. However, few prior works have noticed the camouflage behavior of fraudsters, which could hamper the performance of GNNbased fraud detectors during the aggregation process. In this paper, we introduce two types of camouflages based on recent empirical studies, i.e., the feature camouflage and the relation camouflage. Existing GNNs have not addressed these two camouflages, which results in their poor performance in fraud detection problems. Alternatively, we propose a new model named CAmouflage-REsistant GNN (CARE-GNN), to enhance the GNN aggregation process with three unique modules against camouflages. Concretely, we first devise a label-aware similarity measure to find informative neighboring nodes. Then, we leverage reinforcement learning (RL) to find the optimal amounts of neighbors to be selected. Finally, the selected neighbors across different relations are aggregated together. Comprehensive experiments on two real-world fraud datasets demonstrate the effectiveness of the RL algorithm. The proposed CAREGNN also outperforms state-of-the-art GNNs and GNN-based fraud detectors. We integrate all GNN-based fraud detectors as an opensource toolbox<sup>1</sup> . The CARE-GNN code and datasets are available at https://github.com/YingtongDou/CARE-GNN. 

## **CCS CONCEPTS** 

• **Security and privacy** → **Web application security** ; • **Computing methodologies** → **Neural networks** . 

## **KEYWORDS** 

Graph Neural Networks, Fraud Detection, Reinforcement Learning 

**ACM Reference Format:** 

Yingtong Dou<sup>1</sup> , Zhiwei Liu<sup>1</sup> , Li Sun<sup>2</sup> , Yutong Deng<sup>2</sup> , Hao Peng<sup>3</sup> , Philip S. Yu<sup>1</sup> . 2020. Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters. In _Proceedings of the 29th ACM International_ 

1https://github.com/safe-graph/DGFraud 

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _CIKM ’20, October 19–23, 2020, Virtual Event, Ireland_ 

© 2020 Association for Computing Machinery. ACM ISBN 978-1-4503-6859-9/20/10...$15.00 https://doi.org/10.1145/3340531.3411903 

_Conference on Information and Knowledge Management (CIKM ’20), October 19–23, 2020, Virtual Event, Ireland._ ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3340531.3411903 

## **1 INTRODUCTION** 

As Internet services thrive, they also incubate various kinds of fraudulent activities [14]. Fraudsters disguise as regular users to bypass the anti-fraud system and disperse disinformation [44] or reap end-users’ privacy [32]. To detect those fraudulent activities, graph-based methods have become an effective approach in both academic [7, 21, 38] and industrial communities [2, 28, 50]. Graphbased methods connect entities with different relations and reveal the suspiciousness of these entities at the graph level, since fraudsters with the same goal tend to connect with each other [1]. 

Recently, as the development of Graph Neural Networks (GNNs) (e.g., GCN [17], GAT [34], and GraphSAGE [12]), many GNN-based fraud detectors have been proposed to detect opinion fraud [19, 25, 39], financial fraud [23, 24, 37], mobile fraud [41], and cyber criminal [48]. In contrast to traditional graph-based approaches, GNN-based methods aggregate neighborhood information to learn the representation of a center node with neural modules. They can be trained in an _end-to-end_ and _semi-supervised_ fashion, which saves much feature engineering and data annotation cost. 

However, existing GNN-based fraud detection works only apply GNNs in a narrow scope while ignoring the camouflage behaviors of fraudsters, which have been drawing great attention from both researchers [8, 15, 16, 49] and practitioners [2, 19, 41]. Meanwhile, theoretical studies prove the limitations and vulnerabilities of GNNs when graphs have noisy nodes and edges [3, 4, 13, 33]. Therefore, failing to tackle the camouflaged fraudsters would sabotage the performance of GNN-based fraud detectors. Though some recent works [4, 9, 13, 25, 41] have noticed similar challenges, their solutions either fail to fit the fraud detection problems or break the end-to-end learning fashion of GNNs. 

To demonstrate the challenges induced by camouflaged fraudsters during the neighbor aggregation of GNNs, as shown in Figure 1, we construct a graph with two relations and two types of entities. The relation can be any common attributes supposing to be shared by similar entities (e.g., the _User-IP-User_ relation connects entities with the same IP address). There are two types of _camouflages_ as follows: **1) Feature camouflage:** smart fraudsters may adjust their behaviors [8, 10], add special characters in reviews [19, 41] (so-called spamouflage), or employ deep language generation models [15] to gloss over explicit suspicious outcomes. Like Figure 1 shows, a fraudster can add some special characters to a fake review, which helps to bypass feature-based detectors [41]. **2)** 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Dou and Liu, et al. 



<!-- Start of picture text -->
Click this<br>l1nk to<br>win 💵200<br>Benign User<br>Fraudster<br>Relation I<br>Relation II<br><!-- End of picture text -->

**Figure 1: Two types of fraudster camouflage. (1) Feature camouflage: fraudsters add special characters to the text and make it delusive for feature-based spam detectors. (2) Relation camouflage: center fraudster connects to many benign entities under Relation II to attenuate its suspiciousness.** 

**Relation camouflage:** previous works [16, 49] show that crowd workers are actively committing opinion fraud on online social networks. They can probe the graphs used by defenders [43] and adjust their behavior to alleviate the suspiciousness [44]. Specifically, these crafty fraudsters camouflage themselves via connecting to many benign entities (i.e., posting regular reviews or connecting to reputable users). As Figure 1 shows, under Relation II, there are more benign entities than fraudsters. 

Directly applying GNNs to graphs with camouflaged fraudsters will hamper the neighbor aggregation process of GNNs. As Figure 1 shows, if we aggregate neighbors with the intriguing reviews as node features, it will probably smooth out the suspiciousness of the center fraudster [13, 25]. Similarly, if we aggregate all neighbors under Relation II, where there are more dissimilar neighbors, it will eliminate the suspiciousness of the center fraudster. 

Considering the agility of real-world fraudsters [8, 10], designing GNN-based detectors that exactly capture these camouflaged fraudsters is impractical. Therefore, based on the outcomes of two camouflages and the aggregation process of GNNs, we propose _three_ neural modules to enhance the GNNs against the camouflages. **1)** For the feature camouflage, we propose a **label-aware similarity measure** to find the most similar neighbors based on node features. Specifically, we design a neural classifier as a similarity measure, which is directly optimized according to experts with domain knowledge (i.e., annotated data). **2)** For the relation camouflage, we devise a **similarity-aware neighbor selector** to select the similar neighbors of a center node within a relation. Furthermore, we leverage reinforcement learning (RL) to adaptively find the optimal neighbor selection threshold along with the GNN training process. **3)** We utilize the neighbor filtering thresholds learned by RL to formulate a **relation-aware neighbor aggregator** which combines neighborhood information from different relations and obtains the final center node representation. 

We integrate above three modules together with general GNN frameworks and name our model as <u>CAmouflage REsistant Graph Neural Network (CARE-GNN). Experimental results on two real-</u> world fraud datasets demonstrate that our model boosts the GNN performance on graphs with camouflaged fraudsters. The proposed neighbor selector can find optimal neighbors and CARE-GNN outperforms state-of-the-art baselines under various settings. 

**Table 1: Glossary of Notations.** 

|**Symbol**|**Definition**|
|---|---|
|G;V;E;X|Graph; Node set; Edge set; Node feature set|
|_yv_;_Y_|Label for node_v_; Node label set|
|_r_;_R_|Relation; Total number of relations|
|_l_;_L_|GNN layer number; Total number of layers|
|_b_;_B_|Trainingbatch number; Total number of batches|
|_e_;_E_|Trainingepoch number; Total number of epochs|
|V_train_;V_b_<br>|Nodes in the trainingset; Node set at batch_b_|
|E<sup>(</sup><sup>_l_)</sup><br>_r_|Edge set under relation_r_ at the_l_-th layer|
|h<sup>(</sup><sup>_l_)</sup><br>_v_|The embeddingof node_v_ at the_l_-th layer|
|h<sup>(</sup><sup>_l_)</sup><br>_v_,_r_|The embeddingof node_v_ under relation_r_ at the_l_-th layer|
|D<sup>(</sup><sup>_l_)</sup>(_v_,_v_<sup>′</sup>)|The distance between node_v_ and_v_<sup>′ </sup>at the_l_-th layer|
|_S_<sup>(</sup><sup>_l_)</sup>(_v_,_v_<sup>′</sup>)<br>|The similaritybetween node_v_ and_v_<sup>′ </sup>at the_l_-th layer|
|_p_<sup>(</sup><sup>_l_)</sup><br>_r_<br>∈_P_<br>|The filteringthreshold for relation_r_ at the_l_-th layer|
|_a_<sup>(</sup><sup>_l_)</sup><br>_r_<br>∈_A_;_τ_<br>|RL action space; Action stepsize|
|_G_(D<sup>(</sup><sup>_l_)</sup><br>_r_ <sup>)</sup>|Average neighbor distances for relation_r_ at the_l_-th layer|
|_f_ (_p_<sup>(</sup><sup>_l_)</sup><br>_r_ <sup>,</sup><sup>_a_(</sup><sup>_l_)</sup><br>_r_ <sup>)</sup><br>|RL reward function|
|AGG<sup>(</sup><sup>_l_)</sup><br>_r_|Intra-relation aggregator for relation_r_ at the_l_-th layer|
|AGG<sup>(</sup><sup>_l_)</sup><br>_all_|Inter-relation aggregator at the_l_-th layer|
|z_v_|Final embeddingfor node_v_|



We highlight the advantages of CARE-GNN as follows: 

- **Adaptability.** CARE-GNN adaptively selects best neighbors for aggregation given arbitrary multi-relation graph. 

- **High-efficiency.** CARE-GNN has a high computational efficiency without attention and deep reinforcement learning. 

- **Flexibility.** Many other neural modules and external knowledge can be plugged into the CARE-GNN. 

## **2 PROBLEM DEFINITION** 

In this section, we first define the multi-relation graph and the graph-based fraud detection problem. Then, we introduce how to apply GNN to fraud detection problems. All important notations in this paper are summarized in Table 1. 

**Definition 2.1. Multi-relation Graph.** We define a multi-relation graph as G = �V, X, {E _r_ }| _r_<sup>_R_</sup> =1<sup>,</sup><sup>_Y_</sup> �, where V is the set of nodes { _v_ 1, . . . , _vn_ }. Each node _vi_ has a _d_ -dimensional feature vector x _i_ ∈ R<sup>_d_</sup> and X = {x1, . . . , x _n_ } represents a set of all node features. _ei_<sup>_r_</sup> , _j_<sup>=(</sup><sup>_vi_,</sup><sup>_vj_)∈E</sup><sup>_r_isanedgebetween</sup><sup>_vi_and</sup><sup>_vj_witha</sup> relation _r_ ∈{1, · · · , _R_ }. Note that an edge can be associated with multiple relations and there are _R_ different types of relations. _Y_ is the a set of labels for each node in V. 

**Definition 2.2. Fraud Detection on Graph.** For the fraud detection problem, the node _v_ represents the target entity whose suspiciousness needs to be justified. For example, it can be a review on the review website [19, 29] or a transaction in the trading system [23, 37]. The node has a label _yv_ ∈{0, 1} ∈ _Y_ where 0 represents _benign_ and 1 represents _suspicious_ . The relations _R_ are rules, interactions, or shared attributes between nodes, e.g., two reviews from the same user [25] or transactions from the same devices [24]. The graph-based fraud detection problem is a semi-supervised binary node classification problem on the graph. Graph-based fraud detectors are trained based on the labeled node information along 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters 



<!-- Start of picture text -->
update<br>  𝑓 𝑃 RL-Module RL-Module RL-Module<br>Aggregation<br>" "<br>𝑣! 𝑣" 𝒗 𝟎 𝑝" 𝑝# 𝒗 𝟏 𝒗 𝑳<br>𝑟" 𝑟"<br>𝑣 𝒗𝟏𝟎 𝑺 (𝟏) 𝒓𝟏 𝒉𝒗,𝟏𝟏 … 𝒗𝟏𝟏 … 𝒗𝟏𝑳<br>𝑣#𝑟# 𝒗𝟐𝟎 𝑺 (𝟏) 𝒓𝟐 𝒉𝒗,𝟐𝟏 … 𝒗𝟐𝟏 … … 𝒗𝟐𝑳<br>… 𝟏 … 𝑳<br>𝒗𝟑𝟎 𝑺 (𝟏) 𝒗𝟑 𝒗𝟑 𝓛𝐆𝐍𝐍<br>Center node 𝑳𝒂𝒚𝒆𝒓 𝟏 Propagation 𝑳𝒂𝒚𝒆𝒓 𝟐 𝑳𝒂𝒚𝒆𝒓 𝑳<br>Neighbor node<br>RL flow<br>𝑺 (𝟏) SimilarityAggregationMeasureflow 𝓛(𝟏)𝐒𝐢𝐦𝐢 𝓛𝐂𝐀𝐑𝐄<br>Inter-relation AGG Inter-relation AGG<br>Inter-relation AGG<br>Neighbor Selector Intra-relation AGG Neighbor Selector Intra-relation AGG Neighbor Selector Intra-relation AGG<br><!-- End of picture text -->

**Figure 2: The aggregation process of proposed CARE-GNN at the training phase.** 

with the graph composed of multi-relations. The trained models are then used to predict the suspiciousness of unlabeled nodes. 

**Definition 2.3. GNN-based Fraud Detection.** A Graph Neural Network (GNN) is a deep learning framework to embed graphstructured data via aggregating the information from its neighboring nodes [12, 17, 34]. Based on the defined multi-relation graph in Definition 2.2, we unify the formulation of GNNs from the perspective of neighbor aggregation (as shown in the left side of Figure 2): 



For a center node _v_ , h _v_<sup>(</sup><sup>_l_)is the hidden embedding at</sup><sup>_l_-th layer and</sup> h _v_<sup>(0)= x</sup> _i_<sup>is the input feature. E</sup> _r_<sup>(</sup><sup>_l_)</sup> denotes edges under relation _r_ at the _l_ -th layer. h _v_<sup>(</sup><sup>_l_′−</sup> , _r_<sup>1)is the embedding of neighboring node</sup><sup>_v_′ under</sup> relation _r_ . AGG represents the aggregation function that mapping the neighborhood information from different relations into a vector, e.g., mean aggregation [12] and attention aggregation [34]. ⊕ is the operator that combines the information of _v_ and its neighboring information, e.g., concatenation or summation [12]. 

For fraud detection problems, we first construct a multi-relation graph based on domain knowledge. Then, the GNN is trained with partially labeled nodes supervised by binary classification loss functions. Instead of directly aggregating the neighbors for all relations, we separate the aggregation part as _intra-relation_ aggregation and _inter-relation_ aggregation process. During the intra-relation aggregation process, the embedding of neighbors under each relation is aggregated simultaneously. Then, the embeddings for each relation are combined during the inter-relation aggregation process. Finally, the node embeddings at the last layer are used for prediction. 

## **3 PROPOSED MODEL** 

## **3.1 Model Overview** 

The proposed CARE-GNN has three neural modules and its pipeline is shown in Figure 2. For a center node _v_ , we first compute its neighbor similarities based with proposed label-aware similarity measure (Section 3.2). Then we filter the dissimilar neighbors under each 

relation with the proposed neighbor selector (Section 3.3). The neighbor selector is optimized using reinforcement learning during training the GNN (purple module in Figure 2). At the aggregation step, we first use the intra-relation aggregator to aggregate neighbor embeddings under each relation. Then, we combine embeddings across different relations with the inter-relation aggregator (Section 3.4). The optimization steps and the algorithm procedure are presented in Section 3.5 and Algorithm 1, respectively. 

## **3.2 Label-aware Similarity Measure** 

Previous studies have introduced various fraudster camouflage types from behavior [8, 10] and semantic [15, 41] perspectives. Those camouflages could make the features of fraudsters and benign entities similar to each other, and further mislead GNNs to generate uninformative node embeddings. To tackle those node feature camouflages, we deem that an effective similarity measure is needed to filter the camouflaged neighbors before applying GNNs. Previous works have proposed unsupervised similarity metrics like _Cosine Similarity_ [25] or Neural Networks [45]. However, many fraud problems like financial fraud and opinion fraud require extra domain knowledge to identify fraud instances. For example, in opinion fraud, unsupervised similarity measures could not identify the camouflaged fake reviews, which are even indistinguishable by humans [15]. Therefore, we need a parameterized similarity measure to compute node similarity with supervised signals from domain experts (e.g., high-fidelity data annotations). 

For the parameterized similarity measure, AGCN [20] employs a _Mahalanobis distance_ plus a _Gaussian kernel_ , and DIAL-GNN [6] uses the parameterized _cosine similarity_ . However, those two types of measures suffer from high time complexity _O_ (|V| _Dd_<sup>¯</sup> ), where _D_<sup>¯</sup> is the average degree of nodes which is extremely high in real-world graphs (see Table 2) and _d_ is the feature dimension. 

**Label-aware Similarity Measure.** Inspired by LAGCN [4] which uses a Multi-layer Perceptron (MLP) as the edge label predictor, we employ a one-layer MLP as the node label predictor at each layer and use the _l_ 1-distance between the prediction results of two nodes as their similarity measure. For a center node _v_ under relation _r_ at 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Dou and Liu, et al. 

the _l_ -th layer and edge ( _v_ , _v_<sup>′</sup> ) ∈E _r_<sup>(</sup><sup>_l_−1)</sup> , the distance between _v_ and _v_<sup>′</sup> is the _l_ 1-distance of two embeddings: 



and we can define the similarity measure as: 



where each layer has its own similarity measure. The input of MLP at the _l_ -th layer is the node embedding at the previous layer, and the output of MLP is a scalar which is then fed into a nonlinear activation function _σ_ (we use tanh in our work). To save the computational cost, we only take the embedding of the node itself as the input instead of using combined embeddings like the LAGCN [4]. Therefore, taking the _Sr_<sup>(1)(</sup><sup>_v_,</sup><sup>_v_′) as an example where</sup> the input is the raw feature, the time complexity of the proposed similarity measure reduces significantly from _O_ (|V| _Dd_<sup>¯</sup> ) to _O_ (|V| _d_ ) since it predicts the node label solely based on its feature. 

**Optimization.** To train the similarity measure together with GNNs, a heuristic approach is to append it as a new layer before the aggregation layer of GCN [20]. However, if the similarity measure could not effectively filter the camouflaged neighbors at the first layer, it will hamper the performance of following GNN layers. Consequently, the MLP parameters cannot be well-updated through the back-propagation process. To train the similar measure with a direct supervised signal from labels, like [35], we define the cross-entropy loss of the MLP at _l_ -layer as: 



During the training process, the similarity measure parameters are directly updated through the above loss function. It guarantees similar neighbors can be quickly selected within the first few batches and help regularize the GNN training process. 

## **3.3 Similarity-aware Neighbor Selector** 

Given the similarity scores between the center node and its neighbors with Eq. (3), we should select similar neighbors (i.e., filter camouflaged ones) to improve the capability of GNNs. According to the relation camouflage, fraudsters may connect to different amounts of benign entities under different relations [44]. However, since data annotation is costly for real-world fraud detection problems, computing the number of similar neighbors under each relation through data labeling is impossible. We should devise an adaptive filtering/sampling criteria to select an optimal amount of similar neighbors automatically. Thus, we design a similarity-aware neighbor selector. It selects similar neighbors under each relation using _top-p_ sampling with an adaptive filtering threshold. We also devise a reinforcement learning (RL) algorithm to find optimal thresholds during the GNN training process. 

_3.3.1 Top-p Sampling._ We employ _top-p_ sampling to filter camouflaged neighbors under each relation. The filtering threshold for relation _r_ at the _l_ -th layer is _pr_<sup>(</sup><sup>_l_)</sup> ∈[0, 1]. The closed interval means we could discard or keep all neighbors of a node under a relation. Specifically, during the training phase, for a node _v_ in current batch under relation _r_ , we first compute a set of similarity scores 

{ _S_<sup>(</sup><sup>_l_)</sup> ( _v_ , _v_<sup>′</sup> )} using Eq. (3) at the _l_ -th layer where ( _v_ , _v_<sup>′</sup> ) ∈E _r_<sup>(</sup><sup>_l_). E</sup> _r_<sup>(</sup><sup>_l_)</sup> is a set of edges under relation _r_ at the _l_ -th layer. Then we rank its neighbors based on { _S_<sup>(</sup><sup>_l_)</sup> ( _v_ , _v_<sup>′</sup> )} in descending order and take the first _pr_<sup>(</sup><sup>_l_)</sup> · |{ _S_<sup>(</sup><sup>_l_)</sup> ( _v_ , _v_<sup>′</sup> )}| neighbors as the selected neighbors at the _l_ -th layer. All other nodes are discarded at the current batch and will not attend the aggregation process. The _top-p_ sampling process is applied to the center node at every layer for each relation. 

_3.3.2 Finding the Optimal Thresholds with RL._ Previous works [6, 25] set the filtering threshold as a hyperparameter and tune it with validation to find the optimal value. However, their models are built upon homogeneous benchmark graphs, and without noise induced by camouflaged fraudsters. However, owing to the multi-relation graph of fraud problems as well as the relation camouflage problem, we need an automatic approach to find the optimal threshold _pr_<sup>(</sup><sup>_l_)</sup> for each relation. Since _pr_<sup>(</sup><sup>_l_)</sup> is a probability and has no gradient, we cannot use back-propagation from the classification loss to update it. Meanwhile, given a _pr_<sup>(</sup><sup>_l_), it is infeasible to estimate the quality</sup> of selected neighbors solely based on the similarity scores under the current batch/epoch. To overcome the above challenges, we propose to employ a reinforcement learning (RL) framework to find optimal thresholds. 

Concretely, we formulate the RL process as a Bernoulli Multiarmed Bandit (BMAB) B( _A_ , _f_ , _T_ ) between the neighbor selector and the GNN with the similarity measure. _A_ is the action space, _f_ is the reward function, and _T_ is the terminal condition [36]. Given an initial _pr_<sup>(</sup><sup>_l_), the neighbor selector choose to increase or decrease</sup> _pr_<sup>(</sup><sup>_l_)</sup> as actions and the reward is dependent on the average distance differences between two consecutive epochs. Next, we introduce the details of each BMAB component: 

- **Action.** The action represents how RL updates the _pr_<sup>(</sup><sup>_l_)</sup> based on the reward. Since _pr_<sup>(</sup><sup>_l_)</sup> ∈[0, 1], we define the action _ar_<sup>(</sup><sup>_l_)</sup> as plus or minus a fixed small value _τ_ ∈[0, 1] from _pr_<sup>(</sup><sup>_l_).</sup> 

- **Reward.** The optimal _pr_<sup>(</sup><sup>_l_)</sup> is expected to find the most similar (i.e., minimum distances in Eq. (2)) neighbors of a center node under relation _r_ at the _l_ -th layer. We cannot sense the state of GNN due to its black-box nature; thus, we design a binary stochastic reward solely based on the average distance differences between two consecutive epochs. The average neighbor distances for relation _r_ at the _l_ -th layer for epoch _e_ is: 



Then, we can define the reward for epoch _e_ as: 



The reward is positive when the average distance of newly selected neighbors at epoch _e_ is less than that of the previous epoch, and vice versa. It is not easy to estimate the cumulative reward. Thus, we use the immediate reward to update the action greedily without exploration. Concretely, we increase _pr_<sup>(</sup><sup>_l_)</sup> with a positive reward and decrease it vice versa. 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters 



GNN as a cross-entropy loss function: 



Together with the loss function of the similarity measure in Eq. (4), we define the loss of CARE-GNN as: 

It means that the RL converges in the recent ten epochs and indicates an optimal threshold _pr_<sup>(</sup><sup>_l_)</sup> is discovered. After the RL module terminates, the filtering thresholds are fixed as the optimal one until the convergence of GNN. 



where ||Θ||2 is the _L_ 2-norm of all model parameters, _λ_ 1 and _λ_ 2 are weighting parameters. Since the neighbor filtering process at the first layer is critical to both GNN and similarity measures in the following layers, we only use the similarity measure loss at the first layer to update the parameterized similarity measure in Eq. (3). 

**Discussion.** Different node classes may have different amounts of similar neighbors under the same relation. For instance, as Table 2 shows, under the _R-S-R_ relation of the Yelp dataset, for positive nodes, only 5% of their neighbors have the same label. This is due to the class-imbalance nature of fraud problems and the relation camouflage of fraudsters. According to the cost-sensitive learning research [30], misclassifying a fraudster has a much higher cost to defenders than misclassifying a benign entity. Meanwhile, a large number of benign entities already fuel sufficient information for the classifier. Therefore, to accelerate the training process, we compute the filtering thresholds by only considering positive center nodes (i.e., fraudsters) and apply them for all node classes. The complete RL process is shown in Lines 15-19 of Algorithm 1. The experiment results in Section 4.4 verify the RL effectiveness. 

**Algorithm Description.** Algorithm 1 shows the training process of the proposed CARE-GNN. Given a multi-relational fraud graph, we employ the mini-batch training technique [11] as the result of its large scale. In the beginning, we randomly initialize the parameters of the similarity measure module and GNN module. We initialize all filtering thresholds as 0.5 (Line 2). For each batch of nodes, we first compute the neighbor similarities using Eq. (3) (Line 7) and 

### **Algorithm 1: CARE-GNN:** Camouflage Resistant GNN. 



## **3.4 Relation-aware Neighbor Aggregator** 

After filtering neighbors under each relation, the next step is to aggregate the neighbor information from different relations. Previous methods adopt attention mechanism [23, 37, 48] or devise weighting parameters [24] to learn the relation weights during aggregating information from different relations. However, supposing we have selected the most similar neighbors under each relation, the attention coefficients or weighting parameters should be similar among different relations. Thus, to save the computational cost while retaining the relation importance information, we directly apply the optimal filtering threshold _pr_<sup>(</sup><sup>_l_)</sup> learned by the RL process as the inter-relation aggregation weights. Formally, under relation _r_ at the _l_ -th layer, after applying the _top-p_ sampling, for node _v_ , we define the **intra-relation** neighbor aggregation as follows: 

### **1** // Initialization 



where a mean aggregator is used for all AGG _r_<sup>(</sup><sup>_l_). Then, we define</sup> the **inter-relation** aggregation as follows: 



where h _v_<sup>(</sup><sup>_l_−1)</sup> is the center node embedding at the previous layer, h<sup>(</sup><sup>_l_)</sup> _v_ , _r_<sup>is the intra-relation neighbor embedding at the</sup><sup>_l_-th layer and</sup> _pr_<sup>(</sup><sup>_l_)</sup> is filtering threshold of relation _r_ which is directly used as its inter-relation aggregation weight. ⊕ denotes the embedding summation operation. AGG<sup>_l_</sup> _all_<sup>can be any type of aggregator, and</sup> we test them in Section 4.3. 

## **3.5 Proposed CARE-GNN** 

**Optimization.** For each node _v_ , its final embedding is the output of the GNN at the last layer z _v_ = h _v_<sup>(</sup><sup>_L_). We can define the loss of</sup> 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Dou and Liu, et al. 

then filter the neighbors using _top-p_ sampling (Line 8). Then, we can compute the intra-relation embeddings (Line 9), inter-relation embeddings (Line 10), loss functions (Lines 11-14) for the current batch, respectively. As for the RL process, we assign random actions for the first epoch since it has no reference. From the second epoch, we update _pr_<sup>(</sup><sup>_l_)</sup> according to Lines 15-19. 

## **4 EXPERIMENTS** 

In the experiment section, we mainly present: 

- how we construct multi-relation graphs upon different fraud data (Section 4.1.2); 

- camouflage evidences in real-world fraud data (Section 4.2); 

- the performance comparison over baselines and CARE-GNN variants (Section 4.3); 

- the learning process and explanation of the RL algorithm (Section 4.4); 

- the sensitivity study of hyper-parameters and their effects on model designing (Section 4.5). 

## **4.1 Experimental Setup** 

**Table 2: Dataset and graph statistics.** 

||**#Nodes**<br>(**Fraud%**)|**Relation**|**#Edges**|**Avg. Feature**<br>**Similarity**|**Avg. Label**<br>**Similarity**|
|---|---|---|---|---|---|
|||_R-U-R_|49,315|0.83|0.90|
|**lp**|45,954|_R-T-R_|573,616|0.79|0.05|
|**Ye**|(14.5%)|_R-S-R_|3,402,743|0.77|0.05|
|||_ALL_|3,846,979|0.77|0.07|
|**n**||_U-P-U_|175,608|0.61|0.19|
|**azo**|11,944|_U-S-U_|3,566,479|0.64|0.04|
|**m**|(9.5%)|_U-V-U_|1,036,737|0.71|0.03|
|**A**||_ALL_|4,398,392|0.65|0.05|



_4.1.1 Dataset._ We use the Yelp review dataset [29] and Amazon review dataset [26] to study the fraudster camouflage and GNNbased fraud detection problem. The Yelp dataset includes hotel and restaurant reviews filtered (spam) and recommended (legitimate) by Yelp. The Amazon dataset includes product reviews under the Musical Instruments category. Similar to [47], we label users with more than 80% helpful votes as benign entities and users with less than 20% helpful votes as fraudulent entities. Though previous works have proposed other fraud datasets like Epinions [18] and Bitcoin [40], they only contain graph structures and compacted features, with which we cannot build meaningful multi-relation graphs. In this paper, we conduct a spam review detection (fraudulent user detection resp.) task on the Yelp dataset (Amazon dataset resp.), which is a binary classification task. We take 32 handcrafted features from [29] (25 handcrafted features from [47] resp.) as the raw node features for Yelp (Amazon resp.) dataset. Table 2 shows the dataset statistics. 

_4.1.2 Graph Construction._ **Yelp:** based on previous studies [27, 29] which show that opinion fraudsters have connections in user, product, review text, and time, we take reviews as nodes in the graph and design three relations: 1) _R-U-R_ : it connects reviews posted by the same user; 2) _R-S-R_ : it connects reviews under the 

same product with the same star rating (1-5 stars); 3) _R-T-R_ : it connects two reviews under the same product posted in the same month. **Amazon:** similarly, we take users as nodes in the graph and design three relations: 1) _U-P-U_ : it connects users reviewing at least one same product; 2) _U-S-V_ : it connects users having at least one same star rating within one week; 3) _U-V-U_ : it connects users with top 5% mutual review text similarities (measured by TF-IDF) among all users. The number of edges belonging to each relation is shown in Table 2. 

_4.1.3 Baselines._ To verify the ability of CARE-GNN in alleviating the negative influence induced by camouflaged fraudsters, we compare it with various GNN baselines under the semi-supervised learning setting. We select GCN [17], GAT [34], RGCN [31], and GraphSAGE [12] to represent general GNN models. We choose GeniePath [23], Player2Vec [48], SemiGNN [37], and GraphConsis [25] as four state-of-the-art GNN-based fraud detectors. Their detailed introduction can be found in Section 5. We also implement several variants of CARE-GNN: CARE- _Att_ , CARE- _Weight_ , and CARE- _Mean_ , and they differ from each other in Attention [34], Weight [24], and Mean [12] inter-relation aggregator respectively. 

Among those baselines, GCN, GAT, GraphSAGE, and GeniePath are run on homogeneous graphs (i.e., Relation _ALL_ in Table 2) where all relations are merged together. Other models are run on multi-relation graphs where they handle information from different relations in their approaches. 

_4.1.4 Experimental Setting._ From Table 2, we can see that the percentage of fraudsters are small in both datasets. Meanwhile, realworld graphs usually have great scales. To improve the training efficiency and avoid overfitting, we employ mini-batch training [11] and under-sampling [22] techniques to train CARE-GNN and other baselines. Specifically, under each mini-batch, we randomly sample the same number of negative instances as the number of positive instances. We also study the sample ratio sensitivity in Section 4.5. 

We use unified node embedding size (64), batch size (1024 for Yelp, 256 for Amazon), number of layers(1), learning rate (0.01), optimizer (Adam), and L2 regularization weight ( _λ_ 2 = 0.001) for all models. For CARE-GNN and its variants, we set the RL action step size ( _τ_ ) as 0.02 and the similarity loss weight ( _λ_ 1) as 2. In Section 4.5, we present the sensitivity study for the number of layers, embedding size, and _λ_ 1. 

_4.1.5 Implementation._ For the GCN, GAT, RGCN, GraphSAGE, GeniePath, we use the source code provided by authors. For Player2Vec, SemiGNN, and GraphConsis, we use the open-source implementations<sup>2</sup> . We implement CARE-GNN with Pytorch. All models are running on Python 3.7.3, 2 NVIDIA GTX 1080 Ti GPUs, 64GB RAM, 3.50GHz Intel Core i5 Linux desktop. 

_4.1.6 Evaluation Metric._ Since the Yelp dataset has imbalanced classes, and we focus more on fraudsters (positive instances), like previous work [29], we utilize ROC-AUC (AUC) and Recall to evaluate the overall performance of all classifiers. AUC is computed based on the relative ranking of prediction probabilities of all instances, which could eliminate the influence of imbalanced classes. 

2https://github.com/safe-graph/DGFraud 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters 

**Table 3: Fraud detection performance (%) on two datasets under different percentage of training data.** 

|**Metric**|**Train%**|**GCN**|**GAT**|**RGCN**|**Graph-**<br>**SAGE**|**Genie-**<br>**Path**|**Player-**<br>**2Vec**|**Semi-**<br>**GNN**|**Graph-**<br>**Consis**|**CARE-**<br>**_Att_**|**CARE-**<br>**_Weight_**|**CARE-**<br>**_Mean_**|**CARE-**<br>**GNN**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||5%|54.98|56.23|50.21|53.82|56.33|51.03|53.73|61.58|66.08|71.10|69.83|**71.26**|
|AUC|10%|50.94|55.45|55.12|54.20|56.29|50.15|51.68|62.07|70.21|71.02|71.85|**73.31**|
||20%|53.15|57.69|55.05|56.12|57.32|51.56|51.55|62.31|73.26|74.32|73.32|**74.45**|
|**lp**|40%|52.47|56.24|53.38|54.00|55.91|53.65|51.58|62.07|74.98|74.42|74.77|**75.70**|
|**Ye**|5%|53.12|54.68|50.38|54.25|52.33|50.00|52.28|62.60|63.52|66.64|**68.09**|67.53|
|Rll|10%|51.10|52.34|51.75|52.23|54.35|50.00|52.57|62.08|67.38|68.35|**68.92**|67.77|
|eca|20%|53.87|53.20|50.92|52.69|54.84|50.00|52.16|62.35|68.34|69.07|**69.48**|68.60|
||40%|50.81|54.52|50.43|52.86|50.94|50.00|50.59|62.08|71.13|70.22|69.25|**71.92**|
||5%|74.44|73.89|75.12|70.71|71.56|76.86|70.25|85.46|89.49|89.36|89.35|**89.54**|
||10%|75.25|74.55|74.13|73.97|72.23|75.73|76.21|85.29|**89.58**|89.37|89.43|89.44|
|**n**<br>AUC|20%|75.13|72.10|75.58|73.97|71.89|74.55|73.98|85.50|89.58|**89.68**|89.34|89.45|
|**zo**|40%|74.34|75.16|74.68|75.27|72.65|56.94|70.35|85.50|89.70|89.69|89.52|**89.73**|
|**ma**|5%|65.54|63.22|64.23|69.09|65.56|50.00|63.29|85.49|88.22|88.31|88.02|**88.34**|
|**A**<br>ll|10%|67.81|65.84|67.22|69.36|66.63|50.00|63.32|85.38|87.87|**88.36**|88.12|88.29|
|Reca|20%|66.15|67.13|65.08|70.30|65.08|50.00|61.28|85.59|88.40|**88.60**|88.00|88.27|
||40%|67.45|65.51|67.68|70.16|65.41|50.00|62.89|85.53|88.41|88.45|88.22|**88.48**|



## **4.2 Camouflage Evidence** 

We analyze fraudster camouflage using two metrics introduced in [25]. For the feature camouflage, we compute the feature similarity of neighboring nodes based on their feature vectors’ Euclidean distance, ranging from 0 to 1. The average feature similarity is normalized w.r.t. the total number of edges, which is presented in Table 2. We observe that the averaged similarity scores under all relations are high. High feature similarity implies that fraudsters camouflage their features in a similar way to benign nodes. Moreover, the minor feature similarity difference across different relations proves that the unsupervised similarity measure cannot effectively discriminate fraudsters and benign entities. For instance, the label similarity difference between _R-U-R_ and _R-T-R_ is 0.85, but the feature similarity difference is only 0.04. 

For the relation camouflage, we study it by calculating the label similarity based on whether two connected nodes have the same label. The label similarity is normalized w.r.t. the total number of edges. The average label similarity for each relation is shown in Table 2. High label similarity score implies that the fraudsters fail to camouflage, and low score implies that fraudsters camouflage successfully. We observe that only _R-U-R_ relation has a high label similarity score, while the other relations have label similarity scores less than 20%. It suggests that we need to select different amounts of neighbors for different relations to facilitate the GNN aggregation process. Meanwhile, we should distinguish relations in order to prevent fraudsters from camouflaging. 

## **4.3 Overall Evaluation** 

Table 3 shows the performance of proposed CARE-GNN and various GNN baselines under the fraud detection task on two datasets. We report the best testing results after thirty epochs. We observe that CARE-GNN outperforms other baselines under most of the training proportions and metrics. 

**Single-relation vs. Multi-relation.** Among all GNN baselines in Table 3, GCN, GAT, GraphSAGE, and GeniePath run on singlerelation (i.e., homogeneous) graph where all relations are merged 

together ( _ALL_ in Table 2). Other baselines are built upon multirelation graphs. The performances of single-relation GNNs are better than Player2Vec and SemiGNN, which indicates previously designed fraud detection methods are not suitable for multi-relation graphs. Among the multi-relation GNNs, GraphConsis outperforms all other multi-relation GNNs. The reason is that GraphConsis samples the neighbors based on the node features before aggregating them. Better than GraphConsis, CARE-GNN and its variants adopt parameterized similarity measure and adaptive sampling thresholds, which could better identify and filter camouflaged fraudsters. It demonstrates that neighbor filtering is critical to GNNs when the graph contains many noises (i.e., dissimilar/camouflaged neighbors). Also, CARE-GNN has higher scores than all single-relation GNNs, suggesting that a noisy graph undermines the performance of multi-relation GNNs. A possible reason is the higher complexity of multi-relation GNNs comparing to single-relation ones. 

**Training Percentage.** From Table 3, there is little performance gain for GNNs when increasing the training percentages. It demonstrates the advantage of semi-supervised learning, where a small amount of supervised signals is enough to train a good model. Meanwhile, with informative handcraft features as inputs for two datasets, GNNs are much easier to learn high-quality embeddings. 

**CARE-GNN Variants.** The last four columns of Table 3 show the performance of CARE-GNN and its variants with different interrelation aggregators. It is observed that those four models have similar performances under most training percentages and metrics. It verifies our assumption in Section 3.4 that the attention coefficients and relation weights will become unnecessary when we select similar neighbors under all relations. Moreover, for the Yelp dataset, the CARE- _Att_ has worse performances under a smaller training percentage (e.g., 5%). While for CARE-GNN, since it does not need to train extra attention weights, it attains the best performance against other variants. The first column of Figure 3 presents more evidence that the relation weights finally become equal for all relations under both datasets. The better performance of CAREGNN comparing to CARE- _Mean_ shows that keeping the filtering 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Dou and Liu, et al. 



<!-- Start of picture text -->
0.7 0.020<br>R-U-R R-U-R 0.50 R-U-R 0.75<br>0.6 R-T-R 0.018 R-T-R R-T-R<br>0.5 R-S-R 0.015 R-S-R 0.45 R-S-R 0.70<br>0.013 0.40<br>0.4 0.65<br>0.010 0.35<br>0.3 0.007 0.30 0.60<br>0.2<br>0.1 0.0050.003 0.250.20 0.550.50 AUC-GNNAUC-Simi Recall-GNNRecall-Simi<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 6 12 18 24 30<br>Epoch Epoch Epoch Epoch<br>0.55 0.90<br>0.40 U-P-U 0.35 U-P-U U-P-U<br>U-S-U U-S-U 0.50 U-S-U<br>0.38 U-V-U 0.30 U-V-U 0.45 U-V-U 0.80<br>0.36 0.25 0.40<br>0.70<br>0.34 0.20 0.35<br>0.32 0.15 0.30 0.60<br>0.30 0.10 0.25<br>0.28 0.05 0.20 0.50 AUC-GNN AUC-Simi Recall-GNN Recall-Simi<br>0 8 16 24 32 40 48 56 0 8 16 24 32 40 48 56 0 8 16 24 32 40 48 56 0 8 16 24 32 40 48 56<br>Epoch Epoch Epoch Epoch<br>Performance<br>Relation Weight Relation Distance Filter Threshold<br>Performance<br>Relation Weight Relation Distance Filter Threshold<br><!-- End of picture text -->

**Figure 3: The training process and testing performance of CARE-** **_Weight_ on Yelp (upper) and Amazon (lower) dataset.** 

threshold as inter-relation aggregation weights could enhance the GNN performance and reduce model complexity. 

**GNN vs. Similarity Measure (Figure 3 Column 4).** Figure 3 Column 4 shows the testing performances solely based on the outputs of the GNN module and similarity measure module during training. For the Yelp dataset, GNN has better AUC and Recall than the similarity measure, which suggests that leveraging the structural information benefits the model to classify fraud and benign entities. For Amazon, the performance of GNN and the similarity measure are comparable with each other. It is because the input features provide enough information to discriminate fraudsters. 

## **4.4 RL Process Analysis** 

In this paper, we jointly train the similarity measure and GNN together and employ RL to find the neighbor filtering thresholds adaptively. To present the RL process from different perspectives, in Figure 3, we plot the updating process of three parameters without terminating the RL process during training CARE- _Weight_ . Since CARE- _Weight_ learns the aggregation weight for each relation, plotting its training process instead of CARE-GNN could help understand the effects of our proposed GNN enhancement modules. During training, we also test the model every three epochs for Yelp (four epochs for Amazon) and plot the testing performance for both GNN and similarity measure at the last column of Figure 3. 

**Relation Weights (Figure 3 Column 1).** We observe that the randomly initialized relation aggregation weights gradually converge to the same value as the neighbor selector updates its filtering thresholds and selects more similar neighbors under each relation. When neighbors under each relation provide similar information, their aggregation weights will be similar as well. 

**Relation Distance (Figure 3 Column 2).** As the training epoch increases, it is clearly that the differences between neighbor distances under each relation (computed by Eq. (5)) become larger and comparable to each other. The reason is that the GNN projects the node embeddings to a broader range of space and makes them more distinguishable. As the model filters more noisy neighbors, the average distance across different relations become closer. 

**Neighbor Filtering Threshold (Figure 3 Column 3).** We take 0.02 as the action step size; all thresholds are updated and converge to different values. When the filtering threshold oscillates for several rounds, it reaches the terminal condition in Eq. (7). For different datasets, the proposed RL algorithm could adaptively find the optimal filtering thresholds. 

To demonstrate the advantage of the optimal neighbor filtering thresholds found by RL, in Figure 4, we plot the testing performances of three different neighbor selection criteria under two datasets. Adaptive filters neighbors using converged thresholds found by RL (as shown in Figure 3 Column 3); Fixed-Half keeps the _top_ 50% similar neighbors under each relation and Fixed-All keeps all neighbors without filtering. It is illustrated that CAREGNN with adaptive filtering thresholds is optimized faster than the other two neighbor selectors. Meanwhile, it has a better and smoother performance during training. It verifies the effectiveness of the proposed RL algorithm, which is able to find informative neighbors under each relation. 

## **4.5 Hyper-parameter Sensitivity** 

Figure 5 shows the testing performance of CARE-GNN regarding four hyper-parameters on the Yelp dataset. From Figure 5(a), we observe that increasing the number of layers barely improves the performance of CARE-GNN. For the three-layer model, the CAREGNN suffers the overfitting problem (Recall = 0.5). Therefore, the 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters 



<!-- Start of picture text -->
Adaptive Fixed-Half Fixed-ALL<br>0.8 0.8<br>0.7 0.7<br>0.6 0.6<br>0.5 0.5<br>0.4 0.4<br>0.3 0.3<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Epoch Epoch<br>0.9 0.9<br>0.8 0.8<br>0.7 0.7<br>0.6 0.6<br>0.5 0.5<br>0.4 0.4<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Epoch Epoch<br>Yelp-AUC Yelp-Recall<br>Amazon-AUC Amazon-Recall<br><!-- End of picture text -->

**Figure 4: The testing AUC and Recall for CARE-GNN with different neighbor filtering methods during training.** 

one-layer model is not only able to save the computational cost but also achieve better classification results. Figure 5(b) presents the CARE-GNN performance under different under-sampling ratios as introduced in Section 4.1.4. Note that CARE-GNN is tested on an imbalanced test set. Moreover, CARE-GNN is overfitted when negative instances are less than positive ones (under 1:0.2 and 1:0.5, Recalls are equal to 0.5). An equal under-sampling ratio guarantees a good and fair performance of CARE-GNN. Figure 5(c) shows the influence of different embedding sizes. Embedding sizes with 16, 32, and 64 have comparable performance. Figure 5(d) illustrates the effects of different weighting values for the similarity loss ( _λ_ 1 in Eq. (11)). When the weight of similarity loss is doubled compared to which of GNN loss, CARE-GNN reaches the best performance. Therefore, the similarity measure is crucial for GNN training. 

## **4.6 Discussion** 

Since the multi-relation graphs used in the experiments are very dense (average node degree > 150), one-layer CARE-GNN (which aggregates one-hop neighbors) has already utilized abundant information and thus can achieve excellent performance. CARE-GNN with more layers is suitable for sparse graphs. We improve the computational efficiency using multiple approaches: the light-weight similarity measure, the classic and fast RL framework, positive-node based neighbor selector, no attention mechanism, and mini-batch training with under-sampling. For CARE-GNN, each epoch only takes 17 seconds on Yelp (3 seconds on Amazon), and it has a great performance gain comparing to other baselines. 

## **5 RELATED WORK** 

**GNN and Its Enhancement.** As the most popular deep learning framework on graph data, GNNs have two major types [42]: 1) Spectral-based GNNs (GCN [17], AGCN [20]): they turn a graph into a Laplacian matrix and make convolutional operations in the spectral domain. 2) Spatial-based GNNs (GAT [34], GraphSAGE [12]): they propagate the information based on the spatial relation (i.e., the adjacent nodes). Since spatial-based GNNs are more flexible, many GNN variants belong to this type. The proposed CARE-GNN is a spatial-based GNN as well. 

To enhance the GNN performance on graphs with noisy nodes. One approach is the _graph structure learning_ (GSL) [6, 9, 20]. Those works learn new graph structures from original graphs, which could 



<!-- Start of picture text -->
0 . 8<br>AUC<br>Recall<br>0 . 6<br>0 . 4<br>1 2 3 1:0.2 1:0.5 1:1 1:2<br>0 . 8 (a) Number of Layers (b) Under-sampling ratio (pos:neg)<br>0 . 6<br>0 . 4<br>16 32 64 128 0.5 1 2 4<br>(c) Embedding Size (d) Simi Loss Weight ( λ 1)<br>Score<br>Score<br><!-- End of picture text -->

**Figure 5: Parameter Sensitivity. For each parameter configuration, only the best results among 30 epochs are recorded.** 

better render the latent connections between nodes. Comparing to our work, those papers only investigate the single-relation benchmark datasets without camouflaged fraudsters. Our model filters dissimilar neighbors instead of learning new structures. 

Another approach is the _metric learning_ [4, 13]. Those works devise new metrics to measure the similarity between connect nodes and aggregate neighbors according to the metrics. Among those works, [4] proposes a neural network to predict the labels of neighboring nodes. [13] devises two metrics to measure the average neighborhood similarity and label similarity in a graph. However, those methods either have weak similarity metrics or fixed neighbor filtering thresholds, which need to be calibrated empirically. CARE-GNN proposed by us is more flexible which could learn the similarity metric based on domain knowledge. The relation filtering thresholds of CARE-GNN are optimized during training GNN which retains the end-to-end learning fashion. 

GNN sampling methods [5, 46, 51] also filter the neighbors. While these works only consider selecting representative nodes to accelerate GNN training. For our work, taking account of domain knowledge and relational information, our goal is to filter dissimilar neighbors before aggregation, which could alleviate the negative effect of camouflaged fraudsters. 

**GNN-based Fraud Detection.** Many GNN-based fraud detectors transfer the heterogeneous data into homogeneous data before applying GNNs. Fdgars [39] and GraphConsis [25] construct a single homo-graph based on multiple relations and employ GNNs to aggregate neighborhood information. GeniePath [23] learns convolutional layers and neighbor weights using LSTM and the attention mechanism [34]. GEM [24], SemiGNN [37], ASA [41], and Player2Vec [48] all construct multiple homo-graphs based on node relations in corresponding datasets. After aggregating neighborhood information with GNNs on each homo-graph, SemiGNN and Player2Vec adopt attention mechanism to aggregate node embeddings across multiple homo-graphs; while GEM learns weighting parameters for different homo-graphs, and ASA directly sums information from each homo-graph. Player2Vec leverages GCN & GAT to encode the intra- & inter-relation neighbor information. GAS [19] learns unique aggregators for different node types and updates the embeddings of each node types iteratively. 

In this paper, CARE-GNN constructs multiple homo-graphs with only one node type like GEM and ASA. Among the above works, 

CIKM ’20, October 19–23, 2020, Virtual Event, Ireland 

Dou and Liu, et al. 

only two works [25, 41] have noticed the camouflage behaviors of fraudsters. While [41] only crafts new but inflexible features, and [25] suffers from unsupervised similarity measures and fixed filtering thresholds. CARE-GNN remedies those shortcomings by filtering neighbors based on label-aware similarity measures with adaptive filtering thresholds. 

- [19] A. Li, Z. Qin, R. Liu, Y. Yang, and D. Li. 2019. Spam Review Detection with Graph Convolutional Networks. In _CIKM_ . 

- [20] R. Li, S. Wang, F. Zhu, and J. Huang. 2018. Adaptive graph convolutional neural networks. In _AAAI_ . 

- [21] X. Li, S. Liu, Z. Li, X. Han, C. Shi, B. Hooi, H. Huang, and X. Cheng. 2020. FlowScope: Spotting Money Laundering Based on Graphs. In _AAAI_ . 

- [22] X. Liu, J. Wu, and Z. Zhou. 2008. Exploratory undersampling for class-imbalance learning. _IEEE TSMC_ (2008). 

- [23] Z. Liu, C. Chen, L. Li, J. Zhou, X. Li, L. Song, and Y. Qi. 2019. Geniepath: Graph neural networks with adaptive receptive paths. In _AAAI_ . 

## **6 CONCLUSION** 

This paper investigates the camouflage behavior of fraudsters and their negative influence on GNN-based fraud detectors. To enhance the GNN-based fraud detectors against the feature camouflage and relation camouflage of fraudsters, we propose a label-aware similarity measure and a similarity-aware neighbor selector using reinforcement learning. Along with two neural modules, we further propose a relation-aware aggregator to maximize the computational utility. Experiment results on real-world fraud datasets present evidence of fraudster camouflage and demonstrate the effectiveness and efficiency of proposed enhancement modules, especially the reinforcement learning module. 

## **ACKNOWLEDGMENTS** 

This work is supported by NSF under grants III-1526499, III-1763325, III-1909323, and CNS-1930941. For any correspondence, please refer to Hao Peng. 

## **REFERENCES** 

- [1] L. Akoglu, H. Tong, and D. Koutra. 2015. Graph based anomaly detection and description: a survey. _Data mining and knowledge discovery_ (2015). 

- [2] A. Breuer, R. Eilat, and U. Weinsberg. 2020. Friend or Faux: Graph-Based Early Detection of Fake Accounts on Social Networks. In _WWW_ . 

- [3] D. Chen, Y. Lin, Wei Li, Peng Li, J. Zhou, and Xu Sun. 2020. Measuring and Relieving the Over-smoothing Problem for Graph Neural Networks from the Topological View. In _AAAI_ . 

- [4] H. Chen, L. Wang, S. Wang, D. Luo, W. Huang, and Z. Li. 2019. Label Aware Graph Convolutional Network–Not All Edges Deserve Your Attention. _arXiv preprint arXiv:1907.04707_ (2019). 

- [5] J. Chen, T. Ma, and C. Xiao. 2018. Fastgcn: fast learning with graph convolutional networks via importance sampling. In _ICLR_ . 

- [6] Y. Chen, L. Wu, and M. J. Zaki. 2020. Deep Iterative and Adaptive Learning for Graph Neural Networks. _AAAI Workshops_ (2020). 

- [7] S. Dhawan, S.C.R. Gangireddy, S. Kumar, and T. Chakraborty. 2019. Spotting Collusive Behaviour of Online Fraud Groups in Customer Reviews. In _IJCAI_ . 

- [8] Y. Dou, G. Ma, P. S. Yu, and S. Xie. 2020. Robust Spammer Detection by Nash Reinforcement Learning. In _KDD_ . 

- [9] L. Franceschi, M. Niepert, M. Pontil, and X. He. 2019. Learning discrete structures for graph neural networks. In _ICML_ . 

- [10] S. Ge, G. Ma, S. Xie, and P. S. Yu. 2018. Securing behavior-based opinion spam detection. In _IEEE Big Data_ . 

- [11] P. Goyal, P. Dollár, R. Girshick, P. Noordhuis, L. Wesolowski, A. Kyrola, A. Tulloch, Y. Jia, and K. He. 2017. Accurate, large minibatch sgd: Training imagenet in 1 hour. _arXiv preprint arXiv:1706.02677_ (2017). 

- [12] W. Hamilton, Z. Ying, and J. Leskovec. 2017. Inductive representation learning on large graphs. In _NeurIPS_ . 

- [13] Y. Hou, J. Zhang, J. Cheng, K. Ma, R. T. B. Ma, H. Chen, and M. Yang. 2020. Measuring and Improving the Use of Graph Information in Graph Neural Networks. In _ICLR_ . 

- [14] M. Jiang, P. Cui, and C. Faloutsos. 2016. Suspicious behavior detection: Current trends and future directions. _IEEE Intelligent Systems_ (2016). 

- [15] P. Kaghazgaran, M. Alfifi, and J. Caverlee. 2019. Wide-Ranging Review Manipulation Attacks: Model, Empirical Study, and Countermeasures. In _CIKM_ . 

- [16] P. Kaghazgaran, J. Caverlee, and A. Squicciarini. 2018. Combating crowdsourced review manipulators: A neighborhood-based approach. In _WSDM_ . 

- [17] T.N. Kipf and M. Welling. 2017. Semi-supervised classification with graph convolutional networks. In _ICLR_ . 

- [18] S. Kumar, B. Hooi, D. Makhija, M. Kumar, C. Faloutsos, and VS Subrahmanian. 2018. Rev2: Fraudulent user prediction in rating platforms. In _WSDM_ . 

- [24] Z. Liu, C. Chen, X. Yang, J. Zhou, X. Li, and L. Song. 2018. Heterogeneous Graph Neural Networks for Malicious Account Detection. In _CIKM_ . 

- [25] Z. Liu, Y. Dou, P. S. Yu, Y. Deng, and H. Peng. 2020. Alleviating the Inconsistency Problem of Applying Graph Neural Network to Fraud Detection. _SIGIR_ . 

- [26] J. McAuley and J. Leskovec. 2013. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. In _WWW_ . 

- [27] A. Mukherjee, V. Venkataraman, B. Liu, and N. S. Glance. 2013. What Yelp Fake Review Filter Might Be Doing?. In _ICWSM_ . 

- [28] H. Nilforoshan and N. Shah. 2019. SilceNDice: Mining Suspicious Multi-attribute Entity Groups with Multi-view Graphs. In _DSAA_ . 

- [29] S. Rayana and L. Akoglu. 2015. Collective Opinion Spam Detection: Bridging Review Networks and Metadata. In _KDD_ . 

- [30] Y. Sahin, S. Bulkan, and E. Duman. 2013. A cost-sensitive decision tree approach for fraud detection. _Expert Systems with Applications_ (2013). 

- [31] M. Schlichtkrull, T. N. Kipf, P. Bloem, R. Van Den Berg, I. Titov, and M. Welling. 2018. Modeling relational data with graph convolutional networks. In _ESWC_ . 

- [32] L. Sun, B. Cao, J. Wang, W. Srisa-an, P. Yu, A. D. Leow, and S. Checkoway. 2020. KOLLECTOR: Detecting Fraudulent Activities on Mobile Devices Using Deep Learning. _IEEE TMC_ (2020). 

- [33] L. Sun, Y. Dou, C. Yang, J. Wang, P. S. Yu, and B. Li. 2018. Adversarial Attack and Defense on Graph Data: A Survey. _arXiv preprint arXiv:1812.10528_ (2018). 

- [34] P. Veličković, G. Cucurull, A. Casanova, A. Romero, P. Lio, and Y. Bengio. 2017. Graph attention networks. In _ICLR_ . 

- [35] V. Verma, M. Qu, A. Lamb, Y. Bengio, J. Kannala, and J. Tang. 2019. GraphMix: Regularized Training of Graph Neural Networks for Semi-Supervised Learning. _arXiv preprint arXiv:1909.11715_ (2019). 

- [36] J. Vermorel and M. Mohri. 2005. Multi-armed bandit algorithms and empirical evaluation. In _ECML_ . 

- [37] D. Wang, J. Lin, P. Cui, Q. Jia, Z. Wang, Y. Fang, Q. Yu, J. Zhou, S. Yang, and Y. Qi. 2019. A Semi-supervised Graph Attentive Network for Fraud Detection. In _ICDM_ . 

- [38] H. Wang, C. Zhou, J. Wu, W. Dang, X. Zhu, and J. Wang. 2018. Deep structure learning for fraud detection. In _ICDM_ . 

- [39] J. Wang, R. Wen, C. Wu, Y. Huang, and J. Xiong. 2019. FdGars: Fraudster Detection via Graph Convolutional Networks in Online App Review System. In _WWW Workshops_ . 

- [40] M. Weber, G. Domeniconi, J. Chen, D. K. I. Weidele, C. Bellei, T. Robinson, and C. E. Leiserson. 2019. Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. _KDD Workshops_ (2019). 

- [41] R. Wen, J. Wang, C. Wu, and J. Xiong. 2020. ASA: Adversary Situation Awareness via Heterogeneous Graph Convolutional Networks. In _WWW Workshops_ . 

- [42] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu. 2020. A comprehensive survey on graph neural networks. _IEEE TNNLS_ (2020). 

- [43] C. Yang, H. Wang, L. Sun, and B. Li. 2020. Secure Network Release with Link Privacy. _arXiv preprint arXiv:2005.00455_ (2020). 

- [44] X. Yang, Y. Lyu, T. Tian, Y. Liu, Y. Liu, and X. Zhang. 2020. Rumor Detection on Social Media with Graph Structured Adversarial Learning. In _IJCAI_ . 

- [45] S. F Yilmaz and S. S Kozat. 2020. Unsupervised Anomaly Detection via Deep Metric Learning with End-to-End Optimization. _arXiv preprint arXiv:2005.05865_ (2020). 

- [46] H. Zeng, H. Zhou, A. Srivastava, R. Kannan, and V. Prasanna. 2020. Graphsaint: Graph sampling based inductive learning method. _ICLR_ (2020). 

- [47] S. Zhang, H. Yin, T. Chen, Q. V. N. Hung, Z. Huang, and L. Cui. 2020. GCNBased User Representation Learning for Unifying Robust Recommendation and Fraudster Detection. In _SIGIR_ . 

- [48] Y. Zhang, Y. Fan, Y. Ye, L. Zhao, and C. Shi. 2019. Key Player Identification in Underground Forums over Attributed Heterogeneous Information Network Embedding Framework. In _CIKM_ . 

- [49] H. Zheng, M. Xue, H. Lu, S. Hao, H. Zhu, X. Liang, and K. Ross. 2018. Smoke screener or straight shooter: Detecting elite sybil attacks in user-review social networks. _NDSS_ (2018). 

- [50] Q. Zhong, Y. Liu, X. Ao, B. Hu, J. Feng, J. Tang, and Q. He. 2020. Financial Defaulter Detection on Online Credit Payment via Multi-View Attributed Heterogeneous Information Network. In _WWW_ . 

- [51] D. Zou, Z. Hu, Y. Wang, S. Jiang, Y. Sun, and Q. Gu. 2019. Layer-dependent importance sampling for training deep and large graph convolutional networks. In _NeurIPS_ . 

