---
title: "Causal Strategic Classification"
authors: "unknown"
year: 2020
arxiv_id: "2006.04683"
original_file: "2006.04683.pdf"
pdf_path: "docs/papers\2020_unknown_causal_strategic_classification.pdf"
---

# Causal Strategic Classification

**Authors:** Unknown et al.  
**Year:** 2020 | **arXiv:** [`2006.04683`](https://arxiv.org/abs/2006.04683)  
**Local PDF:** [`2020_unknown_causal_strategic_classification.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_unknown_causal_strategic_classification.pdf)

---

1 

# **Causal Structure Identification from Corrupt Data-Streams** 

Venkat Ram Subramanian, Andrew Lamperski, and Murti V. Salapaka 

**_Abstract_ —Complex networked systems can be modeled and represented as graphs, with nodes representing the agents and the links describing the dynamic coupling between them. The fundamental objective of network identification for dynamic systems is to identify causal influence pathways. However, dynamically related data-streams that originate from different sources are prone to corruption caused by asynchronous timestamps, packet drops, and noise. In this article, we show that identifying causal structure using corrupt measurements results in the inference of spurious links. A necessary and sufficient condition that delineates the effects of corruption on a set of nodes is obtained. Our theory applies to nonlinear systems, and systems with feedback loops. Our results are obtained by the analysis of conditional directed information in dynamic Bayesian networks. We provide consistency results for the conditional directed information estimator that we use by showing almostsure convergence.** 

## I. INTRODUCTION 

Models of systems as networks of interacting systems are central to many domains such as climate science [1], geoscience [2], biological systems [3] [4], quantitative finance [5], social sciences [6], and in many engineered systems like the Internet of Things [7] and wireless sensor networks [8].In many scenarios such as the power grid [9] and metabolic pathways in cells [10] it is impractical or impermissible to externally influence the system. Here causal structure identification via passive means is to be accomplished. With advancements in measurement technology, data processing and communication systems coupled with sensors and measurement devices becoming inexpensive, passive identification of causal graphs of dynamically related agents is becoming more tenable. 

Often, the data-streams in such large systems are not immune to effects of noise [11], asynchronous sensor clocks [12] and packet drops [13]. When dealing with problems of identifying structural and functional connectivity of a large network, there is a pressing need to rigorously study such uncertainties and address detrimental effects of corrupt datastreams on network reconstruction. 

## _A. Related Work_ 

Network identification for linear systems is extensively studied. Methods for identifying transfer functions that dynamically link nodes from time-series data are provided in [14], [15], and [16]. However, these works assume that the time-series are perfect. 

The authors are with the Department of Electrical and Computer Engineering, University of Minnesota, Minneapolis, MN 55455, USA.subra148@umn.edu, alampers@umn.edu, murtis@umn.edu 

Work supported in part by NSF CMMI 1727096. 

Authors in [17] leveraged multivariate Wiener filters to reconstruct the undirected topology of the generative network model. Moreover, assuming that the interaction dynamics are _strictly causal_ and using multivariate estimation based on a Granger filter, it was shown that the interaction structure can be accurately recovered with directions, and without any spurious links. Here too, results assume data to be uncorrupted with the interaction between agents governed via Linear time-invariant (LTI) dynamics. 

For a network of interacting agents with nonlinear, dynamic dependencies and strictly causal interactions, the authors in [18] proposed the use of directed information to determine the directed structure of the network. Sufficient conditions to recover the directed structure are provided. More recently, [19], [20] defined and used _information transfer_ to determine underlying causal interactions in a power network. Here too it is assumed that the data-streams are ideal with no distortions. 

The authors in [21], [22] use dynamical structure functions (DSF) for network recosntruction [23] and consider measurement noise and non-linearities in the network dynamics. The proposed method first finds optimal DSF for all possible Boolean structures and then adopt a model selection procedure to determine the best estimate. The authors concluded that the performance of their algorithms degrades as noise, network size and non-linearities increase. However, a precise characterization of drawing spurious inferences in structure is not provided. In this article, we provide exact location of spurious links that arise during network reconstruction from corrupt data-streams. 

Inspite its significance, little is known on the effects of uncertainties in the data-streams on network idetnification. Recently in [24], the issues of observation noise and undersampling on causal discovery from time-series data has been addressed. Although authors concluded that spurious links can be inferred, a rigorous characterization of such links was not proven nor a generalization of corruption models was provided. In [25] focusing on networks with linear timeinvariant (LTI) interactions, authors provided characterization of the extent of spurious links that can appear due to datacorruption. However, the analysis is restricted to LTI systems. Moreover, in [25] the objective is to determine the topology of the networked system and not to deduce the directions. 

## _B. Our Contribution_ 

In this article, we focus our study to determine the directed structure of a network thereby informing the causal structure of the network, using non-invasive means from corrupt data-streams. We consider networks admitting non-linear and strictly causal dynamical interactions. 

We provide necessary and sufficient conditions to determine the directed network structure from corrupt data-streams. We 

2 

present tight characterization for the spurious links that arise due to corruption of data-streams by determining their location and orientation. 

In [26], preliminary results that characterized the spurious links, in the framework of this article are provided. However, the analysis was limited to dynamical interactions such that every node was dependent dynamically on the entire history (strict) of its _parent_ nodes. In this article, we consider general class of non-linear systems by relaxing the above assumption on dynamics. Moreover, we provide detailed and rigorous proofs to genralize the results obtained in [26] wherein only a proof sketch was provided. In addition, we establish convergence results for the estimator that we use to determine conditional directed information. 

## _C. Paper Organization_ 

We review needed graph theory notions and describe the framework for generative models in Section II. In Section III, we provide models to characterize corruption of data streams that captures time uncertainty, packet loss and measurement noise. The methods to infer directed network structure for non-linear dynamical systems are described in Section IV. Our directed information estimator and simulation results are described in Section V. Finally, a conclusion is provided in Section VI. 

## II. PRELIMINARIES 

## _A. Notations_ 

_y_ [ _·_ ] denotes a sequence and _y_<sup>(</sup><sup>_t_)</sup> denotes the sequence _y_ [0] _, y_ [1] _, . . . y_ [ _t_ ]. 

_PX_ represents the probability density function of a random variable _X_ . 

_X ⊥⊥ Y_ denotes that the random variables _X_ and _Y_ are independent. E[ _·_ ] denotes the expectation operator. 

## _B. Graph Theory Background_ 

In this subsection, few terminologies from graph theory that will be extensively used for network structure inference are reviewed. For furhter reference, see [27]. 

**Definition 1** (Directed Graph) **.** A _directed graph G_ is a pair ( _V, A_ ) where _V_ is a set of vertices or nodes and _A_ is a set of edges given by ordered pairs ( _i, j_ ) where _i, j ∈ V_ . If ( _i, j_ ) _∈ A_ , then we say that there is an edge from _i_ to _j_ . 

We shall use _i → j_ indicates an arc or edge or link from node _i_ to node _j_ in a directed graph. _i − j_ denotes one of _i → j_ or _j → i_ 

**Definition 2** (Children and Parents) **.** Given a directed graph _G_ = ( _V, A_ ) and a node _j ∈ V_ , the _children_ of _j_ are defined as _C_ ( _j_ ) := _{i|j → i ∈ A}_ and the _parents_ of _j_ as _P_ ( _j_ ) := _{i|i → j ∈ A}_ . 

**Definition 3** (Trail/Path) **.** Nodes _v_ 1 _, v_ 2 _, . . . , vk ∈ V_ forms a _trail_ or a _path_ in a directed graph, _G_ , if for every _i_ = 1 _,_ 2 _, . . . , k −_ 1 we have _vi − vi_ +1. 



<!-- Start of picture text -->
1 2 3 4<br>(a) Trail connecting 1 and 4 is active given Z =  {} .<br>1 2 3 4<br>(b) Trail connecting 1 and 4 is active given Z =  { 2 } .<br><!-- End of picture text -->

Fig. 1: This figure shows when the trail connecting nodes 1 and 4 is active given _Z_ . 

**Definition 4** (Chain) **.** In a directed graph _G_ , a _chain_ from node _vi_ to node _vj_ comprises of a sequence of _k_ nodes such that _vi → w_ 1 _→· · · → wk−_ 2 _→ vj_ holds in _G_ . 

**Definition 5** (Descendants and Ancestors) **.** Suppose there exists a chain from a node _vj_ to _vk_ in a directed graph, _G_ . Then, _vk_ is called a _descendant_ of node _vj_ and _vj_ is called an _ancestor_ of _vk_ . 

**Definition 6** (Fork) **.** A node _vk_ is a _fork_ in a directed graph _G_ , if there are two other nodes _vi, vj_ such that _vi ← vk → vj_ holds. 

**Definition 7** (Collider) **.** A node _vk_ is a _collider_ in a directed graph, _G_ , if there are two other nodes _vi, vj_ such that _vi → vk ← vj_ holds. 

**Definition 8** (Active Trail) **.** In a directed graph _G_ , a trail _v_ 1 _−v_ 2 _−· · ·−vn_ is _active_ given a set of nodes _Z_ if one of the following statements holds for every triple _vm−_ 1 _− vm − vm_ +1 along the trail: 

a) If _vm_ is not a collider, then _vm ∈/ Z_ . 

b) If _vm_ is a collider, then _vm_ or one of its descendants is in _Z_ . 

where _m ∈{_ 2 _, . . . , n −_ 1 _}_ . 

See Figure 1 for an illustration. 

**Definition 9** (d-separation) **.** Let _X, Y_ and _Z_ be a set of nodes in a directed graph, _G_ . In _G_ , _X_ and _Y_ are _d-separated_ by _Z_ if and only if there is no active trail between any _x ∈ X_ and any _y ∈ Y_ given _Z_ . It is denoted as d-sep ( _X, Y | Z_ ). 

**Definition 10** (Directed Cycle) **.** A _directed cycle_ from a node _vi_ to _vi_ in a directed graph, _G_ , has the form _vi → w_ 1 _→ · · · → wk → vi_ for some set of nodes _{wn}_<sup>_k_</sup> _n_ =1<sup>in</sup><sup>_G_.</sup> 

**Definition 11** (Directed Acyclic Graph) **.** A directed graph with no directed cycles is called a _directed acyclic graph_ (DAG). 

**Definition 12** (Bayesian Network) **.** Suppose _G_ = ( _V, A_ ) is a DAG whose _N_ nodes represent random variables _a_ 1 _, . . . , aN_ . _G_ is called a _Bayesian Network_ (BN) if for any three subsets _X, Y_ and _Z_ of _V_ , d-sep( _X, Y | Z_ ) implies _X_ is independent of _Y_ given _Z._ 

**Definition 13** (Faithful Bayesian network) **.** Suppose _G_ = ( _V, A_ ) is a DAG whose _N_ nodes represent random variables _a_ 1 _, . . . , aN_ . _G_ is called a _Faithful Bayesian network_ if for any three subsets _X, Y_ and _Z_ of _V_ , it holds that _X_ and _Y_ are independent given _Z_ , if and only if d-sep( _X, Y | Z_ ) is true. 

3 



<!-- Start of picture text -->
y 1 [0] y 1 [1] y 1 [2]<br>y 2 [0] y 2 [1] y 2 [2]<br>1 y 3 [0] y 3 [1] y 3 [2]<br>2 3<br>y 4 [0] y 4 [1] y 4 [2]<br>4<br>5 y 5 [0] y 5 [1] y 5 [2]<br>(a) Generative Graph G (b) DBN G ′ for 3 time slices<br><!-- End of picture text -->

Fig. 2: This figure shows 2a generative graph, 2b its associated DBN for 3 time slices. 

## _C. Generative Model_ 

In this subsection, the _generative model_ that is assumed to generate the measured data is described. Consider _N_ agents that interact over a network. For each agent _i_ , we associate a discrete time sequence _yi_ [ _·_ ] and a sequence _ei_ [ _·_ ] _._ We assume _ei_ and _yi_ to be random processes. The process _ei_ [ _·_ ] is considered innate to agent _i_ and thus _ei_ is independent of _ej_ if _i̸_ = _j._ Moreover, _ei_ is considered to be uncorrelated across time. Let _Y_ denote the set of all random process _{y_ 1 _, . . . , yN }_ with a parent set _P_<sup>_′_</sup> ( _i_ ) defined for _i_ = 1 _, . . . , N._ We consider strictly causal non-linear dynamical relations. Here, _i_ can belong to the parent set _P_<sup>_′_</sup> ( _i_ ). The generative model takes the form: 



where _fi_ ’s can be any finite valued non-linear function such that _|fi| < ∞_ . 

For an illustration, consider the dynamics of a generative model described by: 



We remark that if _yj_ appears on the right hand side of (1) for any time instant _t_ , then _j ∈P_<sup>_′_</sup> ( _i_ ); the parent set is thus not dependent on time. 

## _D. Graphical Representation_ 

Here we describe how networks of dynamical systems are represented by graphs. 

_Generative Graph:_ The structural description of (1) induces a _generative graph G_ = ( _V, A_ ) formed by identifying each vertex _vi_ in _V_ with random process _yi_ and the set of directed links, _A,_ obtained by introducing a directed link from every element in the parent set _P_<sup>_′_</sup> ( _i_ ) of agent _i_ to _i._ Note that we 

do not show _i → i_ in the generative graph and neither do we show the processes _ei_ . 

The generative graph associated with the example described in (2) is given by Fig. 2(a). Note that the generative graph describes the relationships between the stochastic processes _yi_ . When the time variable is unraveled we obtain the Dynamic Bayesian Network as defined below. 

_Dynamic Bayesian Network (DBN):_ Let _G_ = ( _V, A_ ) be a generative graph. Let _yi_ be as defined in (1) for all _i ∈ V_ . Suppose all discrete time sequences have a finite horizon assumed to be _T_ . Let _Sij_ [ _t_ ] = _{t_<sup>_′_</sup> : _yj_ [ _t_<sup>_′_</sup> ] _∈ yj_<sup>(</sup><sup>_t−_1)</sup> as an argument of _fi_ in expression of _yi_ [ _t_ ] in (1) _}_ for all _j ∈ P_<sup>_′_</sup> ( _i_ ) _∪{i}_ and for all _t_ . Consider the graph 



The joint distribution of _Y_<sup>(</sup><sup>_T_)</sup> is given by: 



where the parents of _yi_ [ _t_ ] are obtained from _G_<sup>_′_</sup> _._ It can be shown that _G_<sup>_′_</sup> is the Bayesian network for the random variables _{yi_ [ _t_ ] : _t_ = 0 _,_ 1 _,_ 2 _, . . . , T, i_ = 1 _,_ 2 _, . . . , N }_ and is considered the _Dynamic Bayesian Network_ for _{yi_ : _i_ = 1 _,_ 2 _, . . . , N }_ (see [27]). Figure 2(b) represents the DBN for the system in (2) for three time steps. 

## III. UNCERTAINTY DESCRIPTION 

In this section we provide a description for how uncertainty affects the time-series _yi._ We interchangeably use corruption or perturbation to denote uncertainties in daata-streams. 

## _A. General Perturbation Models_ 

Consider _i_<sup>_th_</sup> node in a generative graph and it’s associated unperturbed time-series _yi_ . The corrupt data-stream _ui_ associated with _i_ follows: 



where _ui_ can depend dynamically on _yi_ till time _t_ , its own values in the strict past, and _ζi_ [ _t_ ] which represents a stochastic process that is independent across time. We highlight a few important perturbation models that are practically relevant. See [26] for more details. 

_Temporal Uncertainty:_ Consider a node _i_ in a generative graph. Suppose _t_ is the true clock index but the node _i_ measures a noisy clock index which is given by a random process, _ζi_ [ _t_ ]. One such probabilistic model is given by the following IID Bernoulli process: 



where _d_ 1 and _d_ 2 are any non-positive integers such that at least one of _d_ 1 and _d_ 2 are not equal to 0. Randomized delays 

4 



<!-- Start of picture text -->
u 1[0] u 1[1] u 1[2]<br>y 1[0] y 1[1] y 1[2]<br>y 2[0] y 2[1] y 2[2]<br>y 3[0] y 3[1] y 3[2]<br>y 4[0] y 4[1] y 4[2]<br>y 5[0] y 5[1] y 5[2]<br><!-- End of picture text -->

Fig. 3: Perturbed DBN _G_<sup>_′_</sup> _Z_<sup>for 3 time slices when node</sup> 1 is corrupt. Node 1 ideal stream denoted by _y_ 1 is shaded because it is not observed or measured. Only, the its corrupted data-stream, _u_ 1, is measured. 

in information transmission can be modeled as a convolution operation with the impulse function _δ_ [ _t_ ] shifted by _ζi_ [ _t_ ] as follows : 



where, 



_Noisy Filtering:_ Given a node _i_ in a generative graph, the data-stream _yi_ is causally filtered and corrupted with independent measurement noise _ζi_ [ _·_ ]. This perturbation model is described by: 



where _Li_ is a stable causal linear time invariant filter. 

_Packet Drops:_ The measurement _ui_ [ _t_ ] corresponding to an ideal data-point _yi_ [ _t_ ] packet reception at time _t_ can be stochastically modeled as: 



Consider an IID Bernoulli process _ζi_ described by, 



The corruption model in (4) takes the form: 



## _B. Perturbed Dynamic Bayesian Network_ 

Here, we provide a discussion on how the dynamic Bayesian network associated with the measured data-streams gets altered when the data-streams are subject to corruption. Consider a generative graph _G_ = ( _V, A_ ). Let _yi_ be as defined in (1) for all _i ∈ V_ . Suppose all discrete time sequences have a finite horizon assumed to be _T_ . Let _G_<sup>_′_</sup> = ( _V_<sup>_′_</sup> _, A_<sup>_′_</sup> ) 

be the associated dynamic Bayesian network. Suppose _Z ⊂ V_ is the set of perturbed nodes with perturbation model described in (4). For _i ∈ Z_ , the measured(corrupt) data-stream corresponding to agent _i_ , _ui_ , is related to _yi_ via (4). Let _UZ_ = _{ui}i∈Z_ and _YZ_ ¯ = _{yj}j∈Z_ ¯<sup>where</sup> _Z_ ¯ = _V \ Z_ . Due to corruption only _UZ_ and _YZ_ ¯<sup>are</sup> measured and observed. Denote the measured data-streams by _W_ = _UZ ∪ YZ_ ¯<sup>.Forall</sup><sup>_j∈Z_let</sup><sup>_SUj_[</sup><sup>_t_]=</sup><sup>_{t′_:</sup><sup>_uj_[</sup><sup>_t′_]</sup><sup>_∈_</sup> _u_<sup>(</sup> _j_<sup>_t−_1)</sup> as an argument of _gi_ in expression of _uj_ [ _t_ ] in (4) _}_ and let _SYj_ [ _t_ ] = _{t_<sup>_′_</sup> : _yj_ [ _t_<sup>_′_</sup> ] _∈ yj_<sup>(</sup><sup>_t_)</sup> as an argument of _gi_ in expression of _uj_ [ _t_ ] in (4) _}_ for all _t_ . Consider the graph _G_<sup>_′_</sup> _Z_ = ( _VZ_<sup>_′, A_</sup> _Z_<sup>_′_)</sup>   where _VZ_<sup>_′_</sup> = _V_<sup>_′_</sup> _∪_  � _uk_ [ _t_ ] and _A_<sup>_′_</sup> _Z_ = _k∈Z_  _t∈{_ 0 _,_ 1 _,...T }_      _A_<sup>_′_</sup> _∪_  � _yk_ [ _i_ ] _→ uk_ [ _t_ ]  � _uk_ [ _i_ ] _→ uk_ [ _t_ ] _k∈Z k∈Z_  _i∈SYk_ [ _t_ ]  _∪_  _i∈SUk_ [ _t_ ]  for all _t ∈{_ 0 _,_ 1 _,_ 2 _, . . . , T }_ . Note that the vertex set _VZ_<sup>_′_consists</sup> of all measurements given by the set _W_ , and the uncorrupted versions _yk_ of the corrupted versions _uk_ for _k ∈ Z._ 

Consider the set of random variables, _R_ = _{yi_ [ _t_ ] : _i ∈ {_ 1 _,_ 2 _, . . . , N }_ and _t ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . . , T }} ∪{ui_ [ _t_ ] : _i ∈ {_ 1 _,_ 2 _, . . . , N }_ and _t ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . . , T }}_ . The joint distribution _PR_ is given by: 



where the parents of _ui_ [ _t_ ] _, yj_ [ _t_ ] are obtained from _GZ_<sup>_′.G′_</sup> _Z_ is the Bayesian Network for the random variables _R_ and is considered as the perturbed DBN (PDBN) associated with _UZ ∪ Y_ . 

Fig 3. shows an example of a perturbed DBN corresponding to the generative graph in Fig. 2(a) for three time slices when node 1 data-streams are corrupt following a noisy filtering model described in (6). 

## IV. STRUCTURE IDENTIFICATION 

## _A. Structure Inference from Ideal Data-Streams_ 

First, we recall how the structure of a generative graph can be inferred using directed information in the case of ideal data-streams. Consider a generative graph _G_ with _N_ nodes and let _Y_ denote the collection of _N_ data-streams that are measured. The authors in [18] defined and applied directed information (DI) in a network of of dynamically interacting agents, to determine if a process causally influences another. A slightly modified definition of DI as defined in [18] is: 

**Definition 14** (Directed Information) **.** The directed information (DI) from data-stream _yj_ to _yi_ is given by: 



5 



Note that DI is always non-negative. So, if there is no directed edge from _j_ to _i_ in _G_ , then we must have that _I_ ( _yj → yi ∥ Y_ ¯ _i_ ¯ _j_ ) = 0. 

The following theorem was proved in [18] that specifies a necessary and sufficient condition to detect a presence of link in the generative graph. 

**Theorem 1.** _A directed edge from j to i exists in the directed graph G if and only if I_ ( _yj → yi ∥ Y_ ¯ _i_ ¯ _j_ ) _>_ 0 _._ 

**Remark 1.** In [18], the authors assume positive distribution for the random processes in _Y_ . Under this assumption the result in Theorem 1 is both necessary and sufficient. 

_B. Main Result: Inferring Directed Graphs from Corrupt Data-streams_ 

In this subsection, we will describe how data uncertainty will lead to spurious probabilistic relationships between nodes that are not connected in the original graph. 

To present the main result in Theorem 2, some definitions are required. 

**Definition 15** (Perturbed Graph) **.** Let _G_ = ( _V, A_ ) be a generative graph. Suppose _Z ⊂ V_ is the set of perturbed nodes with each perturbation model admitting a description provided in (4). The perturbed graph, _GZ_ = ( _V, AZ_ ), is a directed graph where there is an edge _i → j ∈ AZ_ if and only if there is a trail, _trlG_ : _i_ = _v_ 1 _− v_ 2 _−· · · − vk−_ 1 _− vk_ = _j_ in _G_ such that the following conditions hold: 

- P1) If _j ∈/ Z_ , then _vk−_ 1 _→ j ∈ A_ . 

- P2) For _m ∈{_ 2 _,_ 3 _, . . . , k −_ 1 _}_ , if _vm−_ 1 _→ vm ← vm_ +1, and _vm ∈/ Z_ , then _vm_ +1 _∈ Z_ . 

- P3) If _vm_ is a node such that _vm−_ 1 _−vm −vm_ +1 is a sub-path of the path _v_ 1 _− . . . − vk_ and _vm_ is not a collider, then _vm ∈ Z._ 

**Remark 2.** Note that the existence of a trail that does not meet the ‘if’ conditions in P1), P2) and P3) guarantees that _i → j ∈ AZ_ . For example, if _i → j ∈ A_ then _i → j ∈ AZ_ . Indeed, if _j ∈/ Z_ then _i → j ∈ AZ_ by condition P1).Conditions P2) and P3) are not applicable. On the other hand, if _j ∈ Z_ , then none of the conditions P1), P2) or P3) are applicable to the trail _i → j_ . So, _i → j ∈ AZ_ . 

= **Definition 16** (Spurious Links) **.** Let _G_ ( _V, A_ ) be a generative graph, _Z ⊂ V_ be the set of perturbed nodes and _GZ_ = ( _V, AZ_ ) be the perturbed graph. Spurious links are those links _i → j ∈ AZ_ that do not belong to _A_ . 

The following lemma will be used to prove our main result in Theorem 2. 

**Lemma 1.** _Consider a generative graph, G_ = ( _V, A_ ) _, consisting of N nodes. Let Z_ = _{v_ 1 _, . . . , vn} ⊂ V be the set of n perturbed nodes where each perturbation is described by_ (4) _. Denote the data-streams as follows: UZ_ := _{ui}i∈Z_ 

_and YZ_ ¯<sup>:=</sup><sup>_{yj}_</sup> _j∈Z_<sup>¯</sup><sup>_whereZ_¯=</sup><sup>_V\Z.Letthemeasured_</sup> _data-streams be W_ = _UZ ∪ YZ_ ¯<sup>=</sup><sup>_{w_1</sup><sup>_, w_2</sup><sup>_, . . . , wN}.Let_</sup> _G_<sup>_′_</sup> = ( _V_<sup>_′_</sup> _, A_<sup>_′_</sup> ) _be the dynamic Bayesian network (DBN) associated with G and G_<sup>_′_</sup> _Z_<sup>= (</sup><sup>_V_</sup> _Z_<sup>_′, A′_</sup> _Z_<sup>)</sup><sup>_be the perturbed DBN._</sup> _If i → j ∈/ A and if a trail in G_<sup>_′_</sup> _Z_<sup>_betweenw_</sup> _i_<sup>(</sup><sup>_t−_1)</sup> _and wj_ [ _t_ ] _contains a node αbm_ [ _tm_ ] _such that tm ≥ t and bm ∈ V , then for all t >_ 0 _, the trail is not active given {wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}._ 

_Proof._ Consider any trail from a node in _wi_<sup>(</sup><sup>_t−_1)</sup> to _wj_ [ _t_ ] in _G_<sup>_′_</sup> _Z_<sup>.Denotethisby</sup><sup>_trlG_</sup> _Z_<sup>_′_:=</sup><sup>_wi_[</sup><sup>_t_1]=</sup><sup>_αb_</sup> 1<sup>[</sup><sup>_t_1]</sup><sup>_−αb_</sup> 2<sup>[</sup><sup>_t_2]</sup><sup>_−_</sup> _· · ·−αbr−_ 1[ _tr−_ 1] _−αbr_ [ _tr_ ] = _wj_ [ _t_ ] where 0 _≤ t_ 1 _< t_ . Here, _bk_ denotes the corresponding vertex in _V_ for _k_ = _{_ 1 _,_ 2 _, . . . , r}_ . Also, _αbk_ [ _tk_ ] = _ubk_ [ _tk_ ] if _bk ∈ Z_ or _αbk_ [ _tk_ ] = _ybk_ [ _tk_ ] otherwise. For compact notation, set _θ_ := _{wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}_ . 

_The trail has length at least 3._ As _i → j ∈/ A_ and if _j ∈/ Z_ , then _yj_ [ _t_ ] does not dynamically depend on process _yi_ and clearly not on _ui_ . If _j ∈ Z_ , then by (4), _uj_ [ _t_ ] does not dynamically depend on _yi_ nor _ui_ . Thus, there is no direct link of the form _αi_ [ _t_<sup>_′_</sup> ] _→ αj_ [ _t_ ”] in _GZ_<sup>_′_, for any</sup><sup>_t′, t_”. In particular,</sup> _wi_ [ _t_ 1] _→ wj_ [ _t_ ] _∈/ GZ_<sup>_′_.Thus,thereareatleast3nodesinthe</sup> trail, _trlG_<sup>_′_</sup> _Z_<sup>.</sup> 

_Unobserved collider in trail._ Without loss of generality, choose _tm_ = max _{t_ 1 _, . . . , tr−_ 1 _} ≥ t_ . Consider the sub-trail _subtrl_<sup>_′_</sup> := _αbm−_ 1[ _tm−_ 1] _− αbm_ [ _tm_ ] _− αbm_ +1[ _tm_ +1] of _trlGZ_<sup>_′_.</sup> By maximality of _tm_ , _tm ≥ tm−_ 1 and _tm ≥ tm_ +1. We will show that one of _αbm−_ 1[ _tm−_ 1] _, αbm_ [ _tm_ ] _,_ and _αbm_ +1[ _tm_ +1] is a collider not in _θ_ and therefore the trail _trlG_<sup>_′_</sup> _Z_<sup>cannotbe</sup> active given _θ_ . 

Suppose _tm > tm−_ 1 and _tm > tm_ +1. Then, _subtrl_<sup>_′_</sup> is of the form, _αbm−_ 1[ _tm−_ 1] _→ αbm_ [ _tm_ ] _← αbm_ +1[ _tm_ +1]. Note that, as _tm ≥ t,_ it follows that neither _αbm_ [ _tm_ ] nor any of its descendants can be in _θ_ and hence not observed. 

Now, consider _tm > tm−_ 1 and _tm_ = _tm_ +1. (The case of _tm > tm_ +1 and _tm_ = _tm−_ 1 can be proven similarly). By the generative model in (1), by strict causality, for any node _p ∈ V_ , _yp_ [ _tp_ ] does not dynamically depend on any _yq_ [ _tp_ ] for _q ∈{p, P_<sup>_′_</sup> ( _p_ ) _}_ . By the perturbation model described by (4), for any _q ∈ Z_ , _uq_ [ _tq_ ] dynamically depends only on _{u_<sup>(</sup> _q_<sup>_tq−_1)</sup> _, yq_<sup>(</sup><sup>_tq_)</sup> _}_ . As _tm_ = _tm_ +1, we therefore have _bm_ = _bm_ +1 such that _bm ∈ Z_ and, one of _αbm_ [ _tm_ ] and _αbm_ +1[ _tm_ +1] is actually a perturbed measurement _ubm_ [ _tm_ ] while the other being _ybm_ [ _tm_ ]. 

= = Suppose _αbm_ [ _tm_ ] _ubm_ [ _tm_ ]. Then, _αbm_ +1[ _tm_ +1] _ybm_ [ _tm_ ]. As _tm > tm−_ 1, _subtrl_<sup>_′_</sup> is in fact _αbm−_ 1[ _tm−_ 1] _→ αbm_ [ _tm_ ] = _ubm_ [ _tm_ ] _← αbm_ +1[ _tm_ +1] = _ybm_ [ _tm_ ]. Therefore, _αbm_ [ _tm_ ] is a collider and as _tm ≥ t_ , this node is not observed in _θ_ . 

Suppose instead that _αbm_ [ _tm_ ] = _ybm_ [ _tm_ ]. Then, _αbm_ +1[ _tm_ +1] = _ubm_ [ _tm_ ]. As _bm ∈ Z_ and maximality of _tm_ implies _αbm_ +2[ _tm_ +2] _∈{u_<sup>(</sup> _b_<sup>_t_</sup> _m_<sup>_m−_1)</sup> _, yb_<sup>(</sup><sup>_t_</sup> _m_<sup>_m−_1)</sup> _}_ . Thus, we have _αbm−_ 1[ _tm−_ 1] _− αbm_ [ _tm_ ] = _ybm_ [ _tm_ ] _→ αbm_ +1[ _tm_ +1] = _ubm_ [ _tm_ ] _← αbm_ +2[ _tm_ +2] in _trlG_<sup>_′_</sup> _Z_<sup>.Therefore,</sup><sup>_αb_</sup> _m_ +1<sup>[</sup><sup>_tm_+1]</sup> is a collider not observed in _θ_ . 

The following theorem states that the perturbed graph precisely characterizes the spurious links which arise from probabilistic relationships that are spuriously introduced due to corruption. 

6 

**Theorem 2.** _Consider a generative graph, G_ = ( _V, A_ ) _, consisting of N nodes. Let Z_ = _{v_ 1 _, . . . , vn} ⊂ V be the set of n perturbed nodes where each perturbation is described by_ (4) _. Denote the data-streams as follows: UZ_ := _{ui}i∈Z and YZ_ ¯<sup>:=</sup><sup>_{yj}_</sup> _j∈Z_<sup>¯</sup><sup>_whereZ_¯=</sup><sup>_V\Z.Letthemeasured_</sup> _data-streams be W_ = _UZ ∪ YZ_ ¯<sup>=</sup><sup>_{w_1</sup><sup>_, w_2</sup><sup>_, . . . , wN}.Let_</sup> _the perturbed graph be GZ_ = ( _V, AZ_ ) _and its associated perturbed DBN be G_<sup>_′_</sup> _Z_<sup>=(</sup><sup>_V_</sup> _Z_<sup>_′, A_</sup> _Z_<sup>_′_)</sup><sup>_.Ifi→j∈/AZ,then_</sup> _d-sep(wj_ [ _t_ ] _, wi_<sup>(</sup><sup>_t−_1)</sup> _| {wi_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}_ ) _holds in G_<sup>_′_</sup> _Z_<sup>_forall_</sup> _t >_ 0 _._ 

_Proof._ We will show that if _i → j ∈/ AZ_ , then there is no trail between _wi_<sup>(</sup><sup>_t−_1)</sup> and _wj_ [ _t_ ] that is active given _{wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}_ in _G_<sup>_′_</sup> _Z_<sup>_,_forall</sup><sup>_t >_0.Forrestoftheproof,</sup> denote _θ_ := _{wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}_ . Note that if _i → j ∈/ AZ_ , then there is no directed edge from _i_ to _j_ in _G_ , and every trail from _i_ to _j_ in _G_ violates at least one of the conditions of Definition 15. We will consider these cases separately and show that no active trail exists in _G_<sup>_′_</sup> _Z_<sup>ineachcase.Denoteatrail</sup> connecting a node in _wi_<sup>(</sup><sup>_t−_1)</sup> and _wj_ [ _t_ ] in _GZ_<sup>_′_,by</sup><sup>_trlG′_</sup> _Z_<sup>:=</sup> _wi_ [ _t_ 1] = _αb_ 1[ _t_ 1] _−αb_ 2[ _t_ 2] _−· · ·−αbr−_ 1[ _tr−_ 1] _−αbr_ [ _tr_ ] = _wj_ [ _t_ ] where 0 _≤ t_ 1 _< t_ and _bk_ denotes the corresponding vertex in _V_ for _k_ = _{_ 1 _,_ 2 _, . . . , r}_ . Here, _αv_ [ _tv_ ] = _uv_ [ _tv_ ] if _v ∈ Z_ or _αv_ [ _tv_ ] = _yv_ [ _tv_ ] otherwise. Using Lemma 1, if any _t_<sup>_′_</sup> in _{t_ 2 _, . . . , tr−_ 1 _}_ is such that _t_<sup>_′_</sup> _≥ t_ , then _trlG_<sup>_′_</sup> _Z_<sup>isnotactive.</sup> Now, consider 0 _≤ t_ 1 _, t_ 2 _, t_ 3 _, . . . , tr−_ 1 _< t_ . Construct a trail in _G_ , _trlG_ := _i_ = _v_ 1 _− v_ 2 _− v_ 3 _. . . vk−_ 1 _− vk_ = _j_ from the trail _trlG_<sup>_′_</sup> _Z_<sup>:</sup><sup>_wi_[</sup><sup>_t_1]=</sup><sup>_αb_</sup> 1<sup>[</sup><sup>_t_1]</sup><sup>_−αb_</sup> 2<sup>[</sup><sup>_t_2]</sup><sup>_−· · · −αb_</sup> _r−_ 1<sup>[</sup><sup>_tr−_1]</sup><sup>_−_</sup> _αbr_ [ _tr_ ] = _wj_ [ _t_ ] as follows: 



Additionally, note that _vk − vk_ +1 corresponds to an edge _αvk_ [ _sk_ ] _− αvk_ +1[ _τk_ +1] in _GZ_<sup>_′_.</sup> 

Now, let us reason out why such a construction is always feasible. To this, we claim that for any successive pair _αbl_ [ _tl_ ] _− αbl_ +1[ _tl_ +1], either _bl_ = _bl_ +1 or, _bl̸_ = _bl_ +1 and _bl − bl_ +1 _∈ A_ with the same direction as in _αbl_ [ _tl_ ] _− αbl_ +1[ _tl_ +1]. Assume _αbl_ [ _tl_ ] _→ αbl_ +1[ _tl_ +1]. (The case of _αbl_ [ _tl_ ] _← αbl_ +1[ _tl_ +1] is similar). Then, either _tl_ = _tl_ +1 or _tl < tl_ +1. Consider, _tl_ = _tl_ +1. Then, the link must have the form _ybl_ [ _tl_ ] _→ ubl_ [ _tl_ ], as this is the only instantaneous influence defined in (1) or (4). Thus, _bl_ = _bl_ +1 in this case. 

Suppose, _tl < tl_ +1. Either, _bl_ +1 _∈ Z_ or _bl_ +1 _∈/ Z_ . Consider _bl_ +1 _∈ Z_ . By the perturbation model described by (4), _αbl_ [ _tl_ ] _∈{yb_<sup>(</sup><sup>_t_</sup> _l_ +1<sup>_l_+1</sup><sup>_−_1)</sup> _, u_<sup>(</sup> _b_<sup>_t_</sup> _l_ +1<sup>_l_+1</sup><sup>_−_1)</sup> _}_ . Therefore, _bl_ = _bl_ +1. Suppose, _bl_ +1 _∈/ Z_ . Then, _αbl_ +1[ _tl_ +1] = _ybl_ +1[ _tl_ +1]. By the generative model in (1), we either have dynamic dependence on self-history or history of other nodes. That is, _αbl_ [ _tl_ ] _∈_ 

_{yb_<sup>(</sup><sup>_t_</sup> _l_<sup>_l_+1</sup><sup>_−_1)</sup> _, ∪ q }_ . Then, _bl_ = _bl_ +1 when there _q∈P_<sup>_′_</sup> ( _bl_ +1)<sup>_y_(</sup><sup>_tl_+1</sup><sup>_−_1)</sup> is dependence on self-history. Otherwise, _bl ∈P_<sup>_′_</sup> ( _bl_ +1). Thus, _bl → bl_ +1 _∈ A_ . Let us consider an example- from a trail of the form _u_ 1[ _t_ 1] _← y_ 1[ _t_ 2] _← y_ 2[ _t_ 3] _→ y_ 3[ _t_ 4] _→ y_ 3[ _t_ 5] _→ u_ 3[ _t_ ] in _G_<sup>_′_</sup> _Z_<sup>,atrail</sup><sup>_trlG_in</sup><sup>_G_canbeconstructedas1</sup><sup>_←_2</sup><sup>_→_3.</sup> 

Additionally, we may assume that for _m_ = 2 _, · · · , r −_ 1 we have that _αbm_ [ _tm_ ] _̸_ = _wi_ [ _tm_ ] in _trlG_<sup>_′_</sup> _Z_<sup>.If</sup><sup>_αb_</sup> _m_<sup>[</sup><sup>_tm_]=</sup><sup>_wi_[</sup><sup>_tm_]</sup> for some _m >_ 1, then the sub-trail of _trlG_<sup>_′_</sup> _Z_<sup>,</sup><sup>_wi_[</sup><sup>_tm_]=</sup> _αbm_ [ _tm_ ] _− αbm_ +1[ _tm_ +1] _−· · · − αr_ [ _tr_ ] = _wj_ [ _t_ ] is a trail from _wi_ [ _tm_ ] _∈ wi_<sup>(</sup><sup>_t−_1)</sup> to _wj_ [ _t_ ]. This trail is of strictly shorter length than _trlG_<sup>_′_</sup> _Z_<sup>.Thus,iftheshortertrailcannotbeactive</sup> then the longer trail, _trlG_<sup>_′_</sup> _Z_<sup>,cannotbeactiveeither.Also,</sup> by following the construction procedure described above, this condition implies that _vl̸_ = _i_ for _l_ = 2 _,_ 3 _, · · · , k_ in _trlG_ . Call this condition _loopi_ . To summarize, let _trlG_ := _i_ = _v_ 1 _− v_ 2 _− v_ 3 _. . . vk−_ 1 _− vk_ = _j_ be the trail in _G_ constructed by following the above procedure from the trail _trlG_<sup>_′_</sup> _Z_<sup>:</sup> _wi_ [ _t_ 1] = _αb_ 1[ _t_ 1] _−αb_ 2[ _t_ 2] _−· · ·−αbr−_ 1[ _tr−_ 1] _−αbr_ [ _tr_ ] = _wj_ [ _t_ ]. Since, _i → j ∈/ AZ_ , this trail must violate any of the conditions P1), P2) and P3). We will now consider these cases separately and prove that there is no corresponding active trail in _G_<sup>_′_</sup> _Z_<sup>.</sup> 

If condition P1) is violated, then _trlG_ must have that _j ∈/ Z_ and _vk−_ 1 _← j_ . In this case, _wj_ = _yj_ . Then, either _br−_ 1 = _j_ or _br−_ 1 _̸_ = _j_ . By construction of _trlG_ , if _br−_ 1 _̸_ = _j_ , then _br−_ 1 = _vk−_ 1. As _vk−_ 1 _← j_ , we must then have _αbr−_ 1[ _tr−_ 1] _← αbr_ [ _tr_ ]. However, this implies _tr_ = _t < tr−_ 1 which violates the condition that 0 _≤ t_ 1 _, t_ 2 _, t_ 3 _, . . . , tr−_ 1 _< t_ . Thus, _br−_ 1 = _j_ . That is, _αbr−_ 1[ _tr−_ 1] = _yj_ [ _tr−_ 1]. As _tr−_ 1 _< t_ and _j ∈/ Z_ we have _αbr−_ 1[ _tr−_ 1] = _yj_ [ _tr−_ 1] _→ αbr_ [ _t_ ] = _yj_ [ _t_ ] as a sub-trail of _trlG_<sup>_′_</sup> _Z_<sup>.Clearly,</sup><sup>_yj_[</sup><sup>_tr−_1]isnotacollider.As</sup><sup>_tr−_1</sup><sup>_< t_,we</sup> have _yj_ [ _tr−_ 1] _∈ θ_ . Thus the trail cannot be active. 

Recall the definitions of _sk_ and _τk_ +1 during construction of the trail in _G_ . If condition P2) is violated, then a sub-path of _trlG_ , _vm−_ 1 _→ vm ← vm_ +1, must have a collider, _vm_ , such that _vm ∈/ Z_ and _vm_ +1 _∈/ Z_ where _m_ = _{_ 2 _,_ 3 _· · · , k −_ 1 _}_ . = = If _vm_ +1 _j_ and _τm_ +1 _t_ , P1) also fails, and the argument above shows that the trail in _G_<sup>_′_</sup> _Z_<sup>isnotactive.If</sup> _vm_ +1 = _j_ and _τm_ +1 _< t_ then we have that _αvm_ +1[ _τm_ +1] = _yvm_ +1[ _τm_ +1] _∈ θ_ which is an observed node along the trail and is not a collider. Thus, the trail _trlG_<sup>_′_</sup> _Z_<sup>cannotbeactive.</sup> So, assume that _vm_ +1 _̸_ = _j_ . By condition _loopi_ , _m_ + 1 _̸_ = _i_ . As _vm ← vm_ +1 _∈ trlG_ , by construction we must have _yvm_ [ _sm_ ] = _αvm_ [ _sm_ ] _← αvm_ +1[ _τm_ +1] = _yvm_ +1[ _τm_ +1] along _trlG_<sup>_′_</sup> _Z_<sup>with</sup><sup>_τm_+1</sup><sup>_<sm<t_.Notethatsince</sup><sup>_vm_+1</sup><sup>_∈/Z_</sup> and _τm_ +1 _< t_ , _αvm_ +1[ _τm_ +1] = _yvm_ +1[ _τm_ +1] is an observed non-collider in _θ_ . Thus, the trail cannot be active. 

Finally consider the case that P3) is violated. Then along the trail, _trlG_ , in _G_ , there must be a sub-trail _vm−_ 1 _− vm − vm_ +1 such that the intermediate node, _vm_ , is not a collider and _vm ∈/ Z_ . As _vm_ is not a collider, there is one outgoing directed edge from _vm_ in the trail _trlG_ to either _vm−_ 1 or _vm_ +1. By construction, there must be a corresponding node _αvm_ [ _tf_ ] in the trail _trlGZ_<sup>_′_suchthatithasanoutgoingedge</sup> to either _αvm−_ 1[ _tp_ ] or _αvm_ +1[ _tq_ ] for some _tp > tm_ or _tq > tm_ respectively. Clearly, there is one _αvm_ [ _tm_ ] in _trlG_<sup>_′_</sup> _Z_<sup>which is a</sup> non-collider. Then, as _vm ∈/ Z_ , we must have that _αvm_ [ _tm_ ] = _wvm_ [ _tm_ ] = _yvm_ [ _tm_ ]. Note that _vm̸_ = _i_ by condition _loopi_ . As 

7 

_tm < t_ , _αvm_ [ _tm_ ] is an intermediate non-collider node in _θ_ and is thus observed. Hence, _trlG_<sup>_′_</sup> _Z_<sup>cannotbeactive.</sup> 

We will now show that if conditional directed information, _I_ ( _wi → wj ∥W_ ¯ _j_ ¯ _i_ ), are computed using corrupt data-streams, and were applied for causal structure inference, then spurious links in the graph would result. 

**Corollary 1.** _Consider a generative graph, G_ = ( _V, A_ ) _, consisting of N nodes. Let Z_ = _{v_ 1 _, . . . , vn} ⊂ V be the set of n perturbed nodes where each perturbation is described by_ (4) _. Denote the data-streams as follows: UZ_ := _{ui}i∈Z and YZ_ ¯<sup>:=</sup><sup>_{yj}_</sup> _j∈Z_<sup>¯</sup><sup>_whereZ_¯=</sup><sup>_V\Z.Letthemeasured_</sup> _data-streams be W_ = _UZ ∪ YZ_ ¯<sup>=</sup><sup>_{w_1</sup><sup>_, w_2</sup><sup>_, . . . , wN}.Letthe_</sup> _perturbed graph be GZ_ = ( _V, AZ_ ) _. If I_ ( _wi → wj ∥W_ ¯ _j_ ¯ _i_ ) _>_ 0 _, then i → j ∈ AZ._ 

_Proof._ We will show that if _i → j ∈/ AZ_ , then _I_ ( _wi → wj ∥ W_ ¯ _j_ ¯ _i_ ) = 0. Suppose, _i → j ∈/ AZ_ . Let _GZ_<sup>_′_=(</sup><sup>_V′, A′_</sup> _Z_<sup>)be</sup> the perturbed dynamic Bayesian network (DBN) associated with the perturbed graph, _GZ_ . Then, using Theorem 2, for all _t >_ 0, d-sep( _wj_ [ _t_ ] _, wi_<sup>(</sup><sup>_t−_1)</sup> _| wi_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> ) holds in _G_<sup>_′_</sup> = _Z_<sup>.Inotherwords,thisimplies</sup><sup>_P_</sup> _wj_ [ _t_ ] _|wj_<sup>(</sup><sup>_t−_1)</sup> _,wi_<sup>(</sup><sup>_t−_1)</sup> _,W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _Pwj_ [ _t_ ] _|wj_ ( _t−_ 1) _,W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> will hold true for all _t_ and thus, _I_ ( _wi → wj ∥W_ ¯ _j_ ¯ _i_ ) = 0. 

The following example illustrates the intuition behind the presence of active trails and hence, the spurious links in the perturbed graph. 

**Example 1.** Consider a generative graph as shown in Figure 4a). Suppose node 3 is subject to data-corruption and let _u_ 3 be its measured data-stream. Denote the measured datastreams at nodes 1 and 2 as _y_ 1 and _y_ 2. _u_ 3 is related to its ideal counterpart _y_ 3 via (4). The measured data streams are _{w_ 1 = _y_ 1 _, w_ 2 = _y_ 2 _, w_ 3 = _u_ 3 _}_ . The perturbed graph _GZ_ , is constructed as defined in definition 15 and is shown in figure 4b). The corresponding perturbed DBN, _G_<sup>_′_</sup> _Z_<sup>,isshownfor3</sup> time steps in figure 4c). We will reason out the presence and absence of an edge in _GZ_ by identifying the presence and absence of active trails in the perturbed DBN. 

Consider 1 _→_ 3 _∈ AZ_ . There is a trail _w_ 1[0] = _y_ 1[0] _→ w_ 2[1] = _y_ 2[1] _← y_ 3[0] _→ y_ 3[1] _→ w_ 3[2] _∈ A_<sup>_′_</sup> _Z_<sup>.Notethatthe</sup> collider _w_ 2[1] is observed. Therefore, the trail is active given _{w_ 3<sup>(1)</sup><sup>_, w_</sup> 2<sup>(1)</sup><sup>_}_.</sup> 

Take the edge 2 _→_ 3 _∈ AZ_ . There exists a trail _w_ 2[1] = _w_ 2[1] _← y_ 3[0] _→ w_ 3[2] in _G_<sup>_′_</sup> _Z_<sup>. Note that the node</sup><sup>_y_3[0] is not</sup> a collider and is not observed. Thus, the trail is active given _{w_ 3<sup>(1)</sup><sup>_, w_</sup> 1<sup>(1)</sup><sup>_}_.</sup> 

The edges 3 _→_ 1 and 2 _→_ 1 are absent in _GZ_ . Ideally, we look for a trail from _w_ 3<sup>(</sup><sup>_t−_1)</sup> to _w_ 1[ _t_ ] = _y_ 1[ _t_ ] that is active given _{w_ 1<sup>(</sup><sup>_t−_1)</sup> _, w_ 2<sup>(</sup><sup>_t−_1)</sup> _}_ and a trail from _w_ 2<sup>(</sup><sup>_t−_1)</sup> to _w_ 1[ _t_ ] = _y_ 1[ _t_ ] that is active given _{w_ 1<sup>(</sup><sup>_t−_1)</sup> _, w_ 3<sup>(</sup><sup>_t−_1)</sup> _}_ . Note that every trail from _w_ 3<sup>(</sup><sup>_t−_1)</sup> and _w_ 2<sup>(</sup><sup>_t−_1)</sup> to _w_ 1[ _t_ ] traverses through a node in _w_ 1<sup>(</sup><sup>_t−_1)</sup> which is in the observed set and this holds for all _t_ . This blocks the information flow along the trail. Therefore, all these trails are inactive. 



<!-- Start of picture text -->
1 2 3<br>1 2 3<br><!-- End of picture text -->

(a) _G_ corresponding to ideal (b) _GZ_ corresponding to unreliMeasurements _Y_ able Measurements _U_ . 



<!-- Start of picture text -->
u 3[0] u 3[1] u 3[2]<br>y 3 [0] y 3 [1] y 3 [2]<br>y 2[0] y 2[1] y 2[2]<br>y 1[0] y 1[1] y 1[2]<br><!-- End of picture text -->

(c) Perturbed dynamic Bayesian network for 3 time steps 

Fig. 4: This figure illustrates the proof of Theorem 2 

**Remark 3.** The results in Theorem 2 and Corollary 1 respectively shows that existence of active trails is the PDBN and non-zero conditional directed information is sufficient to infer the presence of a directed link in the perturbed graph. However, under a mild assumption on the generative and the perturbation model, it can be shown that the respective conditions are also necessary to detect a directed link in the perturbed graph. 

**Assumption 1.** Let the following conditions on the generative and the perturbation model hold: 

C1) In the generative model (1), for all agents _i ∈ {_ 1 _,_ 2 _, . . . , N }_ , and all _j ∈P_<sup>_′_</sup> ( _i_ ), there is a number _kij ≥_ 1 such that _yj_ [ _t − kij_ ] is an argument of _fi_ . 

C2) For all perturbed nodes _i ∈ Z_ , in the perturbation model (4), there is a number _ki ≥_ 1 such that _gi_ always takes _yi_ [ _t − ki_ ] as it’s argument. 

In addition, let at least one of the following conditions on corruption model hold: 

B1) If a node _i ∈ Z_ , then there is a number _ki_<sup>_′≥_1suchthat</sup> _yi_ [ _t − ki_<sup>_′_]isanargumentof</sup><sup>_fi_in(1).</sup> 

B2) If a node _i ∈ Z_ , then _yi_ [ _t_ ] is an argument of _gi_ in (4). 

The following theorem asserts that if _i → j ∈ AZ_ then there exists a corresponding active trail in perturbed DBN. 

**Theorem 3.** _Consider a generative graph, G_ = ( _V, A_ ) _, consisting of N nodes. Let Z_ = _{v_ 1 _, . . . , vn} ⊂ V be the set of n perturbed nodes where each perturbation is described by_ (4) _. Denote the data-streams as follows: UZ_ := _{ui}i∈Z and YZ_ ¯<sup>:=</sup><sup>_{yj}_</sup> _j∈Z_<sup>¯</sup><sup>_whereZ_¯=</sup><sup>_V\ Z.Letthemeasureddata-_</sup> _streams be W_ = _UZ ∪ YZ_ ¯<sup>=</sup><sup>_{w_1</sup><sup>_, w_2</sup><sup>_, . . . , wN}.Suppose,_</sup> _the generative model and the perturbation model satisfies the conditions for dynamics that is mentioned in Assumption 1. If there is a directed edge from i to j in perturbed graph, GZ_ = ( _V, AZ_ ) _, then there exists a trail between a node in wi_<sup>(</sup><sup>_t−_1)</sup> _and wj_ [ _t_ ] _that is active given {wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _} in G_<sup>_′_</sup> _Z_<sup>_,_</sup> _for some t >_ 0 _._ 

_Proof._ The proof is given in appendix A. 

8 

Under the following assumption we can in fact show that _I_ ( _wi → wj ∥ w_ ¯ _j_ ¯ _i_ ) _>_ 0 is also a necessary condition for _i → j ∈ AZ_ as showin in Corollary 2. 

**Assumption 2.** We assume that the generative model in (1) and the perturbation model in (4) are such that the corresponding DBN and PDBN are faithful Bayesian networks. Moreover, we consider positive joint distributions for the random processes _Y_ and _U_ . **Corollary 2.** _Under assumption 2 and dynamics as described in Assumption 1, if i → j ∈ AZ, then I_ ( _wi → wj ∥ w_ ¯ _j_ ¯ _i_ ) _>_ 0 _. Proof._ By theorem 3, if _i → j ∈ AZ_ , then there exists an trail in PDBN between _wi_<sup>(</sup><sup>_t−_1)</sup> and _wj_ [ _t_ ] that is active given _{wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}_ in _G_<sup>_′_</sup> _Z_<sup>_,_forsome</sup><sup>_t >_0.Underfaith-</sup> fulness assumption, this implies _Pwj_ [ _t_ ] _|wj_ ( _t−_ 1) _,wi_<sup>(</sup><sup>_t−_1)</sup> _,W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> = _Pwj_ [ _t_ ] _|wj_ ( _t−_ 1) _,W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> . Thus, _I_ ( _wi → wj ∥W_ ¯ _j_ ¯ _i_ ) _>_ 0. 

## V. ESTIMATION OF DIRECTED INFORMATION 

In [28], consistency results for estimating directed information(DI) between a pair of random processes from data was proposed. However, in this article we extend the methods to determine the directed information between two processes conditioned on a set of other random processes. We provide consistency results of the estimator by showing convergence in almost sure sense(denoted as P-a.s). 

## _A. Pairwise Estimation of Directed Information_ 

Here, we present the definition used for directed information estimator proposed in [28] Before that, the following notion of universal probability assignment is needed. 

_1) Universal Probability Assignment:_ Let _Q_ denote a sequential probability assignment for a sequence _x_ . That is, the conditional probability mass function(pmf) for _x_ [ _i_ ] given _x_<sup>(</sup><sup>_i−_1)</sup> is given by _Q_ ( _x_ [ _i_ ] _| x_<sup>(</sup><sup>_i−_1)</sup> ). The joint pmf for _x_<sup>(</sup><sup>_n_)</sup> is given by _Q_ ( _x_<sup>(</sup><sup>_n_)</sup> ) = _Q_ ( _x_ [0]) _Q_ ( _x_ [1] _| x_ [0]) _Q_ ( _x_ [2] _| x_<sup>(1)</sup> ]) _· · · Q_ ( _x_ [ _n_ ] _| x_<sup>(</sup><sup>_n−_1)</sup> ). 

**Definition 17** (Universal Probability Assignment) **.** Let _P_ be the true joint pmf for _x_<sup>(</sup><sup>_n_)</sup> . Then, a probability assignment _Q_ is called as _universal_ if the following holds: 



Context tree weighting(CTW) algorithm developed by [29] will be used for computing sequential probability assignment. _2) DI estimation:_ Let _X_ and _Y_ be jointly stationary and ergodic processes. The directed information from _X_ to _Y_ can be expressed in terms of the entropy as follows: 



= = where _H_ ( _Y_ ) E[ _−_ log _P_ ( _Y_ )] and _H_ ( _Y ∥ X_ ) E[ _−_ log _P_ ( _Y ∥ X_ )] denotes the entropy of _Y_ and the causally conditioned entropy [30] respectively. The directed information rate (DIR) from _X_ to _Y_ is defined as: 



Let _Hr_ ( _Y_ ) := lim _n→∞ n_<sup><u>1</u></sup><sup>_H_(</sup><sup>_Y_(</sup><sup>_n_))andlet</sup><sup>_Hr_(</sup><sup>_Y∥X_):=</sup> lim _n→∞ n_<sup><u>1</u></sup><sup>_H_(</sup><sup>_Y_(</sup><sup>_n_)</sup><sup>_∥X_(</sup><sup>_n_)).Thus,if</sup><sup>_Hr_(</sup><sup>_Y_)and</sup><sup>_Hr_(</sup><sup>_Y∥X_)</sup> converge, then _Ir_ is convergent. That is, 



In [28], the following DIR estimator was defined: 



We will extend the above to define conditional directed information as described in the following subsection. 

## _B. Estimation of Conditional Directed Information_ 

Let _X, Y, Z_ be jointly stationary and ergodic processes. The conditional directed information from _X_ to _Y_ conditioned on _Z_ can be expressed in terms of the entropy as follows: 





Let _Hr_ ( _Y ∥ X, Z_ ) := lim _n→∞ n_<sup><u>1</u></sup><sup>_H_(</sup><sup>_Y_(</sup><sup>_n_)</sup><sup>_∥X_(</sup><sup>_n_)</sup><sup>_,Z_(</sup><sup>_n_)).</sup> Thus, if _Hr_ ( _Y ∥ Z_ ) and _Hr_ ( _Y ∥ X, Z_ ) converge, then _Ir_ is convergent. That is, 



The conditional directed information estimator _I_<sup>ˆ</sup> ( _X_<sup>(</sup><sup>_n_)</sup> _→ Y_<sup>(</sup><sup>_n_)</sup> _∥ Z_<sup>(</sup><sup>_n_)</sup> ) is defined as under: 





The following theorem establishes the consistency result in estimating conditional DIR as defined in (19). The proof is given in appendix B. 

**Theorem 4.** _Let Q be the probability assignment in the CTW algorithm. Suppose, X, Y, Z are jointly stationary irreducible aperiodic finite-alphabet Markov processes whose order is_ 

9 



<!-- Start of picture text -->
1 4<br>1 4<br>1 2 3<br>1 2 3 2 5 2 5<br>(a) Ideal Measurements Y (b) Unreliable Measurements U .<br>3 6 3 6<br>(a) True generative graph. (b) Network inferred from cor-<br>rupt data-streams at nodes 2 and<br>5<br>(c) Comparison of directed information estimates<br>between perfect measurements and corrupted data-<br>streams. DIR I is shown along X-axis and the sample<br>length n is along Y-axis.<br><!-- End of picture text -->

Fig. 5: This figure shows how unreliable measurements at node 3 can result in spuriously inferring a direct dynamic influence of node 1 on the third and a spurious influence of node 2 on node 3. 

_bounded by the prescribed tree depth of the CTW algorithm. Then,_ 

(c) Comparison of directed information rate (DIR) estimates for links from nodes 1 and 2, between ideal data-streams _Y_ and uncertain measurements _U_ . DIR _I_ is shown along X-axis and the sample length _n_ is along Y-axis. 

Fig. 6: 6a) shows true generative graph. 6c) depicts DIR estimates to detect links from nodes 1 and 2 using ideal measurements _Y_ and when there is corruption at nodes 2 and 5. It can be observed that many spurious links are detected. 





## _C. Simulation Results_ 

To verify the predictions of Theorem 2, we first performed a simulation on a network consisting of 3 nodes with a single node being perturbed and on a network consisting of 6 nodes, of which 2 are corrupt. We estimate the directed information rates (DIR), which are DI estimates that are averaged along the sequence length till the horizon. We used the estimator described in (19) to compute DIR. For both the networks, the horizon length is chosen as 10<sup>4</sup> . The DIR estimates were then averaged over 50 trials. 

_1) Single node Perturbation:_ Consider a network consisting of 2 nodes with a common child as shown in Fig. 5a). The dynamic interactions in the true generative model are as follows: 



where _e_ 1[ _t_ ] _∼_ Bernouilli(0.7), _e_ 2[ _t_ ] _∼_ Bernouilli(0.4) and _e_ 3[ _t_ ] _∼_ Bernouilli(0.6) and ‘+’ is logical ‘OR’ operation. Each of _y_ 1[ _t_ ] _, y_ 2[ _t_ ] and _y_ 3[ _t_ ] has a finite alphabet _{_ 0 _,_ 1 _}._ 

The perturbation considered here is the time-origin uncertainty at node 3. The corruption model takes the form: 



The perturbed graph predicted by Theorem 2 is shown in Fig. 5b). The DIR estimates from ideal ( _Y_ ) and unreliable measurements ( _U_ ) are shown in Fig. 5c). We observe non-zero DIR estimates and add edges to _GZ_ respectively. In particular, note the substantial rise in _I_ ( _u_ 1 _→ u_ 3 _∥ u_ 2) and in _I_ ( _u_ 2 _→ u_ 3 _∥ u_ 1). This indicates the presence of spurious links 1 _→_ 3 and 2 _→_ 3 in the inferred perturbed graph. 

_2) Multiple Perturbation:_ Consider a network of 6 nodes as shown in Fig. 6a). The dynamic interactions in the true generative model are as follows: 



where _e_ 1[ _t_ ] _∼_ Bernouilli(0.55), _e_ 2[ _t_ ] _∼_ Bernouilli(0.5), _e_ 3[ _t_ ] _∼_ Bernouilli(0.2), _e_ 4[ _t_ ] _∼_ Bernouilli(0.4), _e_ 5[ _t_ ] _∼_ and _e_ 6[ _t_ ] _∼_ Bernouilli(0.3)and ‘+’ is logical ‘OR’ operation while ‘ _·_ ’ is logical ‘AND’ operation. Each of _y_ 1[ _t_ ] _, y_ 2[ _t_ ] _, . . . , y_ 6[ _t_ ] has a finite alphabet _{_ 0 _,_ 1 _}._ The perturbations considered here are time-origin uncertainties at nodes 2 and 5. The corruption models takes the form: 



10 



(a) A comparison of DIR estimates to detect links from nodes 3 and 4 using ideal measurements and when there is corruption at nodes 2 and 5 is shown. DIR _I_ is shown along X-axis and the sample length _n_ is along Y-axis. 



(b) A comparison of DIR estimates to detect links from nodes 5 and 6 using ideal measurements and when there is corruption at nodes 2 and 5 is shown. DIR _I_ is shown along X-axis and the sample length _n_ is along Y-axis. 

Fig. 7: DI estimates to detect links from nodes 3,4,5 and 6. 

and 



The perturbed graph predicted by Theorem 2 is shown in figure 6b). The DIR estimates from ideal ( _Y_ ) and unreliable measurements ( _U_ ) are shown in figures 6c) and 7). We observe non-zero DIR estimates and add edges to _GZ_ respectively. For clarity of visualization, only non-zero DIR estimates that would be predicted by Theorem 2 are shown. 

## VI. CONCLUSION 

We studied the problem of inferring directed graphs for a large class of networks that admit non-linear and strictly causal interactions between several agents. We provided necessary and sufficient conditions to determine the directed structure from corrupt data-streams. Doing so, we particularly established that inferring causal structure from corrupt data-streams results in spurious edges and we precisely characterized the directionality of such spurious edges. Finally, we provided convergence results for the estimation of conditional directed information that was used to determine the directed structure. Simulation results were provided to verify the theoretical predictions. 

## _Future Work_ 

Currently, the emphasis was on characterizing the effects of data corruption on network inference and determining how spurious probabilistic relations are introduced. Future work will focus on quantifying the amount of data that is needed to detect network inter-relationships using directed information. Moreover, the problem of removing spurious edges in the network reconstructed from corrupt data streams will be addressed in future. This will play an integral role preceding system identification on networked systems. 

## APPENDIX A 

## PROOF FOR THEOREM 3 

Suppose _i → j_ is in _AZ_ . Then there is a trail, _trlG_ , described by _i_ = _v_ 1 _− v_ 2 _−· · · − vk_ = _j_ in _G_ satisfying conditions in Definition 15. We will first construct a trail in the perturbed DBN, _G_<sup>_′_</sup> _Z_<sup>_,_fromanodein</sup><sup>_w_</sup> _i_<sup>(</sup><sup>_t−_1)</sup> to _wj_ [ _t_ ] for some _t >_ 0. We can construct a trail in _G_<sup>_′_</sup> _Z_<sup>asfollows:for</sup> all _l ∈{_ 1 _,_ 2 _, . . . , k −_ 1 _}_ , set _tl_ = _tl_ +1 _− kvl_ +1 _vl_ if _vl → vl_ +1 holds in _trlG_ . Otherwise, set _tl_ = _tl_ +1 + _kvlvl_ +1 if _vl ← vl_ +1 holds in _trlG_ . Such a construction is feasible because by condition C 1), numbers _kvl_ +1 _vl_ and _kvlvl_ +1 exists for all _l ∈{_ 1 _,_ 2 _, . . . , k −_ 1 _}_ and at all times. Thus, we have a trail _yi_ [ _t_ 1] _− yv_ 2[ _t_ 2] _− yv_ 3[ _t_ 3] _− . . . − yvk−_ 1[ _tk−_ 1] _− yj_ [ _tk_ ]. For all _m ∈{_ 1 _,_ 2 _, . . . , k}_ if _vm ∈ Z_ , there exists a number _km >_ 0 following conditions C 2). If B 2) also holds, then _km ≥_ 0. Let _t >_ max _{t_ 1 _, . . . , tk−_ 1 _}_ , and for all _m ∈{_ 1 _,_ 2 _, . . . , k}_ if _vm ∈ Z_ , let _t > tm_ + _km_ also hold. Depending on whether _i_ or _j_ is a perturbed node, we have four cases on either end of the above trail. 

- A) Consider the case _i, j ∈ Z_ . As _i ∈ Z_ , using condition C 2) _ui_ [ _t_ 1 + _ki_ ] _← yi_ [ _t_ 1] holds true. Choose _t_ sufficiently large so that _t > t_ 1 + _ki_ also holds. As _j ∈ Z_ , using C 2), _t_ can be sufficiently large so that we have _yj_ [ _tk_ ] _→ uj_ [ _t_ ] where _t_ = _tk_ + _kj_ and _kj ≥_ 1. If B 1) holds, then we can choose _t_ sufficiently large such that at the end of the trail we take _s_ steps from _yj_ [ _tk_ ] to _uj_ [ _t_ ] such that the tail is of the form _yj_ [ _tk_ ] _→ yj_ [ _tk_ + _kj_<sup>_′_]</sup><sup>_→· · ·→yj_[</sup><sup>_tk_+</sup><sup>_sk_</sup> _j_<sup>_′_]</sup><sup>_→uj_[</sup><sup>_t_]with</sup> _t_ = _tk_ + _skj_<sup>_′_+</sup><sup>_kj_. Thus, the constructed trail in</sup><sup>_G_</sup> _Z_<sup>_′_is either</sup> _wi_ [ _t_ 1 + _ki_ ] = _ui_ [ _t_ 1 + _ki_ ] _← yi_ [ _t_ 1] _− yv_ 2[ _t_ 2] _− yv_ 3[ _t_ 3] _− · · ·−yvk−_ 1[ _tk−_ 1] _−yj_ [ _tk_ ] _→ uj_ [ _t_ ] = _wj_ [ _t_ ], or _wi_ [ _t_ 1 + _ki_ ] = _ui_ [ _t_ 1 + _ki_ ] _← yi_ [ _t_ 1] _−yv_ 2[ _t_ 2] _−yv_ 3[ _t_ 3] _−· · ·−yvk−_ 1[ _tk−_ 1] _− yj_ [ _tk_ ] _→ yj_ [ _tk_ + _kj_<sup>_′_]</sup><sup>_→· · · →yj_[</sup><sup>_tk_+</sup><sup>_sk_</sup> _j_<sup>_′_]</sup><sup>_→uj_[</sup><sup>_t_] =</sup><sup>_wj_[</sup><sup>_t_]</sup> with _t >_ max _{t_ 1 + _ki, t_ 1 _, . . . , tk, . . . , tk_ + _skj_<sup>_′}_,andfor</sup> all _m ∈{_ 1 _,_ 2 _, . . . , k}_ if _vm ∈ Z_ , _t > tm_ + _km_ . 

- B) Consider the case _i ∈ Z_ but _j̸ ∈ Z_ . Choose _t_ as _tk_ . As _i ∈ Z_ , using condition C 2) _ui_ [ _t_ 1 + _ki_ ] _← yi_ [ _t_ 1] holds true. Choose _t_ sufficiently large so that _t > t_ 1 + _ki_ also holds. Thus, we have constructed a trail in _G_<sup>_′_</sup> _Z_<sup>whichisofthe</sup> form: _wi_ [ _t_ 1+ _ki_ ] = _ui_ [ _t_ 1+ _ki_ ] _← yi_ [ _t_ 1] _−yv_ 2[ _t_ 2] _−yv_ 3[ _t_ 3] _− · · · − yvk−_ 1[ _tk−_ 1] _− yj_ [ _t_ ] = _wj_ [ _t_ ] with _t >_ max _{t_ 1 + _ki, t_ 1 _, . . . , tk−_ 1 _}_ , and for all _m ∈{_ 1 _,_ 2 _, . . . , k}_ if _vm ∈ Z_ , _t > tm_ + _km_ . 

- C) Consider the case _i̸ ∈ Z_ but _j ∈ Z_ . Following arguments presented in case (A) we conclude that the constructed trail of form _wi_ [ _t_ 1] = _yi_ [ _t_ 1] _− yv_ 2[ _t_ 2] _− yv_ 3[ _t_ 3] _−· · · − yvk−_ 1[ _tk−_ 1] _− yj_ [ _tk_ ] _→ uj_ [ _t_ ] = _wj_ [ _t_ ], or of form _wi_ [ _t_ 1] = 

11 

_yi_ [ _t_ 1] _− yv_ 2[ _t_ 2] _− yv_ 3[ _t_ 3] _−· · · − yvk−_ 1[ _tk−_ 1] _− yj_ [ _tk_ ] _→ yj_ [ _tk_ + _kj_<sup>_′_]</sup><sup>_→· · · →yj_[</sup><sup>_tk_+</sup><sup>_sk_</sup> _j_<sup>_′_]</sup><sup>_→uj_[</sup><sup>_t_] =</sup><sup>_wj_[</sup><sup>_t_] exists in</sup> the perturbed DBN _G_<sup>_′_</sup> _Z_<sup>with</sup><sup>_t >_max</sup><sup>_{t_1</sup><sup>_, . . . , tk, . . . , tk_+</sup> _skj_<sup>_′}_,andforall</sup><sup>_m ∈{_1</sup><sup>_,_2</sup><sup>_, . . . , k}_if</sup><sup>_vm∈Z_,</sup><sup>_t > tm_+</sup> _km_ . 

- D) Consider the case _i̸ ∈ Z_ and _j̸ ∈ Z_ . Following arguments presented in Case (B) we conclude that the trail _wi_ [ _t_ 1] = _yi_ [ _t_ 1] _− yv_ 2[ _t_ 2] _− yv_ 3[ _t_ 3] _−· · · − yvk−_ 1[ _tk−_ 1] _− yj_ [ _t_ ] = _wj_ [ _t_ ] exists in the perturbed DBN _GZ_<sup>_′_with</sup> _t >_ max _{t_ 1 _, . . . , tk−_ 1 _}_ , and for all _m ∈{_ 1 _,_ 2 _, . . . , k}_ if _vm ∈ Z_ , _t > tm_ + _km_ . 

We will now argue that in each of the cases above, the constructed trail is active given _θ_ := _{wj_<sup>(</sup><sup>_t−_1)</sup> _, W_ ¯ _j_<sup>(</sup> ¯ _i_<sup>_t−_1)</sup> _}. Sub-trails with colliders:_ For all the trails in _G_<sup>_′_</sup> _Z_<sup>con-</sup> structed under various cases above consider a sub-trail of the form _yvm−_ 1[ _tm−_ 1] _→ yvm_ [ _tm_ ] _← yvm_ +1[ _tm_ +1]. Clearly, _vm_ cannot be either _i_ or _j._ If _vm̸ ∈ Z_ then as _tm < t_ , we have _yvm_ [ _tm_ ] _∈ w_ ¯ _j_<sup>(</sup> ¯<sup>_t_</sup> _i_<sup>_−_1)</sup> and thus the sub-trail is active. If _vm ∈ Z_ then the corrupted version of _yvm_ [ _tm_ ] is _uvm_ [ _tm_ + _kvm_ ] = _wvm_ [ _tm_ + _kvm_ ] and as _tm_ + _kvm < t_ , we have _wvm_ [ _tm_ + _km_ ] _∈ w_ ¯ _j_<sup>(</sup> ¯<sup>_t_</sup> _i_<sup>_−_1)</sup> . Thus the collider _yvm_ [ _tm_ ] has a descendant _wvm_ [ _tm_ + _kvm_ ] _∈ θ_ . Thus the sub-trail remains active. Thus no collider can deactivate the trails in _G_<sup>_′_</sup> _Z_<sup>_._</sup> 

_Sub-trails with with no colliders:_ Now consider any node _yvm_ [ _tm_ ] which is not a collider. Note that in the trails for the cases (A), (B), (C), and (D), _yj_ and _yi_ can only appear as an intermediate node only if they are corrupted. In such cases, neither _yi_ [ _t_ 1] nor _yj_ [ _tk_ ] belong to _θ._ Thus, if _yj_ or _yi_ are intermediate nodes, they cannot deactivate the trails given _θ._ Consider an intermediate node _vm̸ ∈{i, j}._ From Definition 15P 3), _vm_ is corrupted. Thus _yvm_ [ _tm_ ] _̸_ = _wvm_ [ _tm_ ] and _yvm_ [ _tm_ ] cannot deactivate the trail as _yvm_ [ _tm_ ] _̸ ∈ θ._ 

## APPENDIX B 

## PROOF FOR THEOREM 4 

To prove the theorem, we require two results from [28]. The following lemma shows that with sufficiently large data, the conditional probability assignment by CTW converges to the true probability assignment for a Markov process. 

**Lemma 2.** _Let Q be the probability assignment described by CTW. Let X be a stationary and finite alphabet Markov process with finite Markov order which is bounded by the prescribed tree depth of CTW algorithm. Let P be the true probability for x. Then,_ 





Next, we will later use the following proposition which is a rephrased result from [28]. 

**Proposition 1.** _Let Q be the probability assignment in the CTW algorithm. Suppose, X, Y are jointly stationary irreducible aperiodic finite-alphabet Markov processes whose order is bounded by the prescribed tree depth of the CTW algorithm. Let H_<sup>ˆ</sup> ( _Y_<sup>(</sup><sup>_n_)</sup> _∥ X_<sup>(</sup><sup>_n_)</sup> ) = _− n_<sup><u>1</u></sup> � _ni_ =1 � _yi_<sup>_Q_(</sup><sup>_y_[</sup><sup>_i_]</sup><sup>_|_</sup> _X_<sup>(</sup><sup>_i−_1)</sup> _, Y_<sup>(</sup><sup>_i−_1)</sup> ) _·_ log _Q_ ( _y_ [ _i_ ] _|X_<sup>(</sup><sup>_i−_</sup> <u>1</u><sup>1)</sup> _,Y_<sup>(</sup><sup>_i−_1)</sup> )<sup>_.Then,_</sup> 



Recall the expression for the conditional DI estimator from (19): 



We will show that the first term(call it T1) in equation (23) converges to _Hr_ ( _Y ∥ Z_ ) and the second term (call it T2) in (23) converges to _Hr_ ( _Y ∥ X, Z_ ). 

Convergence of T2: Let _V_ = _{X, Z}_ . Thus, T2 can be written as _H_ ˆ ( _Y_<sup>(</sup><sup>_n_)</sup> _∥ V_<sup>(</sup><sup>_n_)</sup> ) = _− n_<sup><u>1</u></sup> � _ni_ =1 � _y_ [ _i_ ]<sup>_Q_(</sup><sup>_y_[</sup><sup>_i_]</sup><sup>_|_</sup> _V_<sup>(</sup><sup>_i−_1)</sup> _, Y_<sup>(</sup><sup>_i−_1)</sup> ) _·_ log _Q_ ( _y_ [ _i_ ] _|V_<sup>(</sup><sup>_i−_</sup> <u>1</u><sup>1)</sup> _,Y_<sup>(</sup><sup>_i−_1)</sup> )<sup>. Using, proposition 1,</sup> we thus have that lim _n→∞ H_<sup>ˆ</sup> ( _Y_<sup>(</sup><sup>_n_)</sup> _∥ V_<sup>(</sup><sup>_n_)</sup> ) _→ Hr_ ( _Y ∥ V_ ) almost surely. 

Convergence of T1: Subtract _Hr_ ( _Y ∥ Z_ ) from _T_ 1 and express _T_ 1 _− Hr_ ( _Y ∥ Z_ ) = _Fn_ + _Sn_ where, 







By ergodicity, _Sn_ converges to zero almost surely. We need to show that _Fn_ converges to zero almost surely. Rewrite _Fn_ = _n_ <u>1</u> � _ni_ =1<sup>_βi_where,</sup> 



By Lemma 2, the CTW probabilities _Q_ ( _y_ [ _i_ ] _| X_<sup>(</sup><sup>_i−_1)</sup> _, Y_<sup>(</sup><sup>_i−_1)</sup> _, Z_<sup>(</sup><sup>_i−_1)</sup> ) converges to true probabilities _P_ ( _y_ [ _i_ ] _| X_<sup>(</sup><sup>_i−_1)</sup> _, Y_<sup>(</sup><sup>_i−_1)</sup> _, Z_<sup>(</sup><sup>_i−_1)</sup> ) almost surely. Therefore, _i_ lim _→∞_<sup>_βi_= 0</sup> P-a.s. (27) 

Hence, by Cesaro mean [31] we have: 



12 

- [27] D. Koller and N. Friedman, _Probabilistic Graphical Models: Principles and Techniques_ . The MIT Press, 2009. 

## REFERENCES 

- [1] M. Kretschmer, D. Coumou, J. F. Donges, and J. Runge, “Using causal effect networks to analyze different arctic drivers of midlatitude winter circulation,” _Journal of Climate_ , vol. 29, no. 11, pp. 4069–4081, 2016. 

- [2] A. Sendrowski, K. Sadid, E. Meselhe, W. Wagner, D. Mohrig, and P. Passalacqua, “Transfer entropy as a tool for hydrodynamic model validation,” _Entropy_ , vol. 20, no. 1, p. 58, 2018. 

- [3] N. Omranian, J. M. Eloundou-Mbebi, B. Mueller-Roeber, and Z. Nikoloski, “Gene regulatory network inference using fused lasso on multiple data sets,” _Scientific reports_ , vol. 6, p. 20533, 2016. 

   - [28] J. Jiao, H. H. Permuter, L. Zhao, Y. Kim, and T. Weissman, “Universal estimation of directed information,” _IEEE Transactions on Information Theory_ , vol. 59, no. 10, pp. 6220–6242, 2013. 

   - [29] F. M. Willems, Y. M. Shtarkov, and T. J. Tjalkens, “The context-tree weighting method: basic properties,” _IEEE Transactions on Information Theory_ , vol. 41, no. 3, pp. 653–664, 1995. 

   - [30] G. Kramer, _Directed information for channels with feedback_ . HartungGorre, 1998. 

   - [31] T. M. Cover and J. A. Thomas, _Elements of information theory_ . John Wiley & Sons, 2012. 

- [4] D. S. Bassett and O. Sporns, “Network neuroscience,” _Nature neuroscience_ , vol. 20, no. 3, p. 353, 2017. 

- [5] P. Fiedor, “Networks in financial markets based on the mutual information rate,” _Phys. Rev. E_ , vol. 89, p. 052801, May 2014. 

- [6] S. P. Borgatti, A. Mehra, D. J. Brass, and G. Labianca, “Network analysis in the social sciences,” _science_ , vol. 323, no. 5916, pp. 892–895, 2009. 

- [7] C. Zhu, V. C. Leung, L. Shu, and E. C.-H. Ngai, “Green internet of things for smart world,” _IEEE Access_ , vol. 3, pp. 2151–2162, 2015. 

- [8] S. Yang, U. Adeel, Y. Tahir, and J. A. McCann, “Practical opportunistic data collection in wireless sensor networks with mobile sinks,” _IEEE Transactions on Mobile Computing_ , vol. 16, no. 5, pp. 1420–1433, 2016. 

- [9] D. Deka, S. Backhaus, and M. Chertkov, “Structure learning in power distribution networks,” _IEEE Transactions on Control of Network Systems_ , vol. 5, no. 3, pp. 1061–1074, Sept 2018. 

- [10] J. D. Finkle, J. J. Wu, and N. Bagheri, “Windowed granger causal inference strategy improves discovery of gene regulatory networks,” _Proceedings of the National Academy of Sciences_ , vol. 115, no. 9, 2018. 

- [11] M. S. Stankovic, S. S. Stankovic, and K. H. Johansson, “Distributed time synchronization for networks with random delays and measurement noise,” _Automatica_ , vol. 93, pp. 126 – 137, 2018. 

**Venkat Ram Subramanian** received the B.Tech degree in electrical engineering from SRM University, Chennai, India, in 2014, and the M.S. degree in electrical engineering from the University of Minnesota, Minneapolis, in 2016. Currently, he is working towards a Ph.D. degree at the University of Minnesota. His Ph.D. research is on learning dynamic relations in networks from corrupt datastreams. In addition to system identification and stochastic systems, his research interests also include grid modernization and optimal energy management in Distributed Energy Resources (DER). 

- [12] H.-H. Cho, C.-Y. Chen, T. K. Shih, and H.-C. Chao, “Survey on underwater delay/disruption tolerant wireless sensor network routing,” _IET Wireless Sensor Systems_ , vol. 4, no. 3, pp. 112–121, 2014. 

- [13] A. S. Leong, S. Dey, and D. E. Quevedo, “Sensor scheduling in variance based event triggered estimation with packet drops,” _IEEE Transactions on Automatic Control_ , vol. 62, no. 4, pp. 1880–1895, 2017. 

- [14] H. H. Weerts, P. M. V. den Hof, and A. G. Dankers, “Identifiability of linear dynamic networks,” _Automatica_ , vol. 89, pp. 247 – 258, 2018. 

- [15] J. M. Hendrickx, M. Gevers, and A. S. Bazanella, “Identifiability of dynamical networks with partial node measurements,” _IEEE Transactions on Automatic Control_ , 2018. 

- [16] D. Materassi and M. V. Salapaka, “Signal selection for estimation and identification in networks of dynamic systems: a graphical model approach,” _arXiv preprint arXiv:1905.12132_ , 2019. 

- [17] ——, “On the problem of reconstructing an unknown topology via locality properties of the wiener filter,” _IEEE transactions on automatic control_ , vol. 57, no. 7, pp. 1765–1777, 2012. 

- [18] C. J. Quinn, N. Kiyavash, and T. P. Coleman, “Directed Information Graphs,” _IEEE Transactions on Information Theory_ , vol. 61, no. 12, pp. 6887–6909, 2015. 

- [19] S. Sinha, P. Sharma, U. Vaidya, and V. Ajjarapu, “Identifying causal interaction in power system: Information-based approach,” in _2017 IEEE 56th Annual Conference on Decision and Control (CDC)_ , 2017, pp. 2041–2046. 

- [20] ——, “On information transfer based characterization of power system stability,” _IEEE Transactions on Power Systems_ , 2019. 

- [21] Y. Yuan, G. B. Stan, S. Warnick, and J. Goncalves, “Robust dynamical network structure reconstruction,” _Automatica_ , vol. 47, no. 6, pp. 1230 – 1235, 2011, special Issue on Systems Biology. 

- [22] V. Chetty, D. Hayden, J. Goncalves, and S. Warnick, “Robust signalstructure reconstruction,” in _52nd IEEE Conference on Decision and Control_ , Dec 2013, pp. 3184–3189. 

- [23] J. Goncalves and S. Warnick, “Necessary and sufficient conditions for dynamical structure reconstruction of lti networks,” _IEEE Transactions on Automatic Control_ , vol. 53, no. 7, pp. 1670–1674, Aug 2008. 

- [24] J. Runge, “Causal network reconstruction from time series: From theoretical assumptions to practical estimation,” _Chaos: An Interdisciplinary Journal of Nonlinear Science_ , vol. 28, no. 7, p. 075310, 2018. 

- [25] V. R. Subramanian, A. Lamperski, and M. V. Salapaka, “Network topology identification from corrupt data streams,” in _IEEE 56th Annual Conference on Decision and Control (CDC)_ , 2017, pp. 1695–1700. 

**Andrew Lamperski** (S’05–M’11) received the B.S. degree in biomedical engineering and mathematics in 2004 from the Johns Hopkins University, Baltimore, MD, and the Ph.D. degree in control and dynamical systems in 2011 from the California Institute of Technology, Pasadena. He held postdoctoral positions in control and dynamical systems at the California Institute of Technology from 2011– 2012 and in mechanical engineering at The Johns Hopkins University in 2012. From 2012–2014, did postdoctoral work in the Department of Engineering, 



University of Cambridge, on a scholarship from the Whitaker International Program. In 2014, he joined the Department of Electrical and Computer Engineering, University of Minnesota as an Assistant Professor. His research interests include optimal control, optimization, and identification, with applications to neuroscience and robotics. 

**Murti Salapaka** (SM’01–F’19) Murti Salapaka received the bachelors degree from the Indian Institute of Technology, Madras, India, in 1991, and the Masters and Ph.D. degrees from the University of California, Santa Barbara, CA, USA, in 1993 and 1997, respectively, all in mechanical engineering. He was with Electrical Engineering department, Iowa State University, from 1997 to 2007. He is currently the Vincentine Hermes-Luh Chair Professor with the Electrical and Computer Engineering Department, University of Minnesota, Minneapolis, MN, USA. 



Prof. Salapaka was the recipient of the NSF CAREER Award and the ISUYoung Engineering Faculty Research Award for the years 1998 and 2001, respectively. He is an IEEE Fellow. 

- [26] ——, “Inferring directed graphs for networks from corrupt data streams (in progress),” in _IEEE 57th Annual Conference on Decision and Control (CDC)_ , 2018. 

