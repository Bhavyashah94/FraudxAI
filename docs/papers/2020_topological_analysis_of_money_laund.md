---
title: "Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting"
year: 2020
original_file: "topological_analysis_of_money_laund.pdf"
pdf_path: "docs/papers\2020_topological_analysis_of_money_laund.pdf"
---

# Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting

**Year:** 2020  
**Local PDF:** [`2020_topological_analysis_of_money_laund.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_topological_analysis_of_money_laund.pdf)

---

# **Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

**Yuzhou Chen**<sup>1 2</sup> **Ignacio Segovia-Dominguez**<sup>3 4</sup> **Yulia R. Gel**<sup>3 2</sup> 

## **Abstract** 

## **1. Introduction** 

There recently has been a surge of interest in developing a new class of deep learning (DL) architectures that integrate an explicit time dimension as a fundamental building block of learning and representation mechanisms. In turn, many recent results show that topological descriptors of the observed data, encoding information on the shape of the dataset in a topological space at different scales, that is, persistent homology of the data, may contain important complementary information, improving both performance and robustness of DL. As convergence of these two emerging ideas, we propose to enhance DL architectures with the most salient time-conditioned topological information of the data and introduce the concept of zigzag persistence into time-aware graph convolutional networks (GCNs). Zigzag persistence provides a systematic and mathematically rigorous framework to track the most important topological features of the observed data that tend to manifest themselves over time. To integrate the extracted time-conditioned topological descriptors into DL, we develop a new topological summary, zigzag persistence image, and derive its theoretical stability guarantees. We validate the new GCNs with a time-aware zigzag topological layer (Z-GCNETs), in application to traffic forecasting and Ethereum blockchain price prediction. Our results indicate that Z-GCNET outperforms 13 state-of-the-art methods on 4 time series datasets. 

1Department of Statistical Science, Southern Methodist University, TX, USA<sup>2</sup> Energy Storage & Distributed Resources Division, Lawrence Berkeley National Laboratory, CA, USA<sup>3</sup> Department of Mathematical Sciences, University of Texas at Dallas, TX, USA<sup>4</sup> NASA Jet Propulsion Laboratory, CA, USA. Correspondence to: Yuzhou Chen _<_ yuzhouc@smu.edu _>_ , Ignacio Segovia Dominguez _<_ ignacio.segoviadominguez@utdallas.edu _>_ , Yulia R. Gel _<_ ygl@utdallas.edu _>_ . 

_Proceedings of the 38_<sup>_th_</sup> _International Conference on Machine Learning_ , PMLR 139, 2021. Copyright 2021 by the author(s). 

Many real world phenomena are intrinsically dynamic by nature, and ideally neural networks, encoding the knowledge about the world should also be based on more explicit time-conditioned representation and learning mechanisms. However, most currently available deep learning (DL) architectures are inherently static and do not systematically integrate time-dimension into the learning process. As a result, such model architectures often cannot reliably, accurately and on time learn many salient time-conditioned characteristics of complex interdependent systems, often resulting in outdated decisions and requiring frequent model updates. 

In turn, in the last few years we observe an increasing interest to integrate deep neural network architectures with persistent homology representations of the learned objects, typically in a form of some topological layer in DL (Hofer et al., 2019; Carriere et al.` , 2020; Carlsson & Gabrielsson, 2020). Such persistent homology representations allow us to extract and learn descriptors of the object _shape_ . (By shape here we broadly understand data characteristics that are invariant under continuous transformations such as bending, stretching, and compressing.) Such interest in combining persistent homology representations with DL is explained by the complementary multi-scale information topological descriptors deliver about the underlying objects, and higher robustness of these salient object characterisations to perturbations. 

Here we take the first step toward merging the two directions. To enhance DL with the most salient _time-conditioned topological_ information, we introduce the concept of zigzag persistence into time-aware DL. Building on the fundamental results on quiver representations, zigzag persistence studies properties of topological spaces which are connected via inclusions going in both directions (Carlsson & Silva, 2010; Tausz & Carlsson, 2011; Carlsson, 2019). Such generalization of ordinary persistent homology allows us to track topological properties of time-conditioned objects by extracting and tracking salient _time-aware topological features_ through time-ordered inclusions. We propose to summarize the extracted time-aware zigzag persistence in a form of zigzag persistence images and then integrate the result- 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

ing information as a learnable time-aware zigzag layer into GCN. 

The key novelty of our paper can be summarized as follows: 

- This is the first approach bridging time-conditioned DL with time-aware persistent homology representations of the data. 

- We propose a new vectorized summary for time-aware persistence, namely, _zigzag persistence image_ and discuss its theoretical stability guarantees. 

- We introduce the concepts of time-aware zigzag persistence into learning time-conditioned graph structures and develop a zigzag topological layer (Z-GCNET) for time-aware graph convolutional networks (GCNs). 

- Our experiments on application Z-GCNET to traffic forecasting and Ethereum blockchain price prediction show that Z-GCNET surpasses 13 state-of-the-art methods on 4 benchmark datasets, both in terms of accuracy and robustness. 

## **2. Related Work** 

**Zigzag Persistence** is yet an emerging tool in applied topological data analysis, but many recent studies have already shown its high utility in such diverse applications as brain sciences (Chowdhury et al., 2018), imagery classification (Adams et al., 2020), cyber-security of mobile sensor networks (Adams & Carlsson, 2015; Gamble et al., 2015), and characterization of flocking and swarming behavior in biological sciences (Corcoran & Jones, 2017; Kim et al., 2020). An alternative to zigzag but a closely related approach to assess properties of time-varying data with persistent homology, namely, crocker stacks, has been recently suggested by Xian et al. (2020), though the crocker stacks representations are not learnable in DL models. While zigzag has been studied in conjunction with dynamic systems (Tymochko et al., 2020) and time-evolving point clouds (Corcoran & Jones, 2017), till now, the utility of zigzag persistence remains untapped not only in conjunction with GCNs but with any other DL tools. 

**Time series forecasting** From a deep learning perspective, Recurrent Neural Networks (RNNs) are natural methods to model time-dependent datasets (Yu et al., 2019). In particular, the stable architecture of Long Short Term Memories (LSTMs), and its variant called Gate Recurrent Unit (GRU), solves the gradient instability of predecessors and adds extra flexibility due to their memory storage and forget gates. The ability of LSTM and GRU to selectively learn historical patterns awaken an interest among researchers and major companies to solve a variety of time-dependant machine learning problems (Chae et al., 2018; Schmidhuber; Yuan 

et al., 2019; Shin & Kim, 2020). Although most of variants of LSTM architecture performs similarly well in large scale studies, see (Greff et al., 2017), GRU models has fewer parameters and, in general, perform similarly well as LSTM (Gao et al., 2020). Applications of RNN are limited by the underlying structure of the input data, these methods are not designed to handle data from non-Euclidean spaces, such as graphs and manifolds. 

**Graph convolutional networks** To overcome the limitations of traditional convolution on graph structured data, graph convolution-based methods (Defferrard et al., 2016; Kipf & Welling, 2017; Velickoviˇ c et al.´ , 2018) are proposed to explore both global and local structures. GCNs usually consists of graph convolution layers which extract the edge characteristics between neighbor nodes and aggregate feature information from neighborhood via graph filters. In addition to convolution, there has been a surge of interest in applying GCNs time series forecasting tasks (Yu et al., 2018b; Yao et al., 2018; Yan et al., 2018; Guo et al., 2019; Weber et al., 2019; Pareja et al., 2020). Although these methods have achieved state-of-the-art performance in traffic flow forecasting, human action recognition, and anti-money laundering regulation, the design of spatial temporal graph convolution network framework is mostly based on modeling spatial-temporal correlation in terms of feature-level and pre-defined graph structure. 

## **3. Time-Aware Topological Signatures of Graphs** 

**Spatio-temporal Data as Graph Structures** The spatialtemporal networks can be represented as a sequence of discrete snapshots, _{G_ 1 _, G_ 2 _, . . . , GT }_ , where _Gt_ = _{V, Et, Wt}_ represents the graph structure at time step _t_ , _t_ = 1 _, . . . , T_ . In spatial network _Gt_ , _V_ is a node set with cardinality _|V|_ of _N_ and _Et ⊆V ×V_ is an edge set. A nonnegative symmetric _N × N_ -matrix _Wt_ with entries _{ωij_<sup>_t}_1</sup><sup>_≤i,j≤N_represents the</sup> adjacency matrix of _Gt_ , that is, _ωij_<sup>_t>_0forany</sup><sup>_et_</sup> _ij_<sup>_∈Et_</sup> and _ωij_<sup>_t_= 0, otherwise.Let</sup><sup>_F, F∈_Z</sup><sup>_>_0 be the number of</sup> different node features associated each node _v ∈V_ . Then, a _N × F_ feature matrix **_X_** _t_ serves as an input to the framework of time series process modeling. 

**Background on Persistent Homology** Persistent homology is a mathematical machinery to extract the intrinsic shape properties of _G_ that are invariant under continuous transformations such as bending, stretching, and twisting. The key idea is, based on some appropriate scale parameter, to associate _G_ with a graph filtration _G_<sup>1</sup> _⊆ . . . ⊆G_<sup>_n_</sup> = _G_ and then to equip each _G_<sup>_i_</sup> with an abstract simplicial complex _C_ ( _G_<sup>_i_</sup> ), 1 _≤ i ≤ n_ , yielding a filtration of complexes _C_ ( _G_<sup>1</sup> ) _⊆ . . . ⊆ C_ ( _G_<sup>_n_</sup> ). Now, we can systematically and efficiently track evolution of various patterns such as connected components, cycles, and voids throughout this hierar- 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

chical sequence of complexes. Each topological feature, or _p_ -hole (e.g., number of connected components and voids), 0 _≤ p ≤ d_ , is represented by a unique pair ( _ib, jd_ ), where birth _ib_ and death _jd_ are the scale parameters at which the feature first appears and disappears, respectively. The lifespan of the feature is defined as _id − jb_ . The extracted topological information can be then summarized as a persistence diagram Dgm = _{_ ( _ib, jd_ ) _∈_ R<sup>2</sup> _|ib < jd}_ . Multiplicity of a point ( _ib, jd_ ) _∈D_ is the number of _p_ -dimensional topological features ( _p_ -holes) that are born and die at _ib_ and _jb_ , respectively. Points at the diagonal Dgm are taken with infinite multiplicity. The idea is then to evaluate topological features that persist (i.e. have longer lifespan) over the complex filtration and, hence, are likelier to contain important structural information on the graph. 

Finally, a filtration of the weighted graph _G_ can be constructed in multiple ways. For instance, (i) we can select a scale parameter as edge weight and, as an abstract simplicial complex _C_ on _G_ , consider a Vietoris–Rips (VR) complex _V R_<sup>_ν∗_</sup> ( _G_ ) = _{G ′ ⊆G|diam_ ( _G ′_ ) _≤ ν∗}_ , that is, _V Rν∗_ ( _G_ ) consists of nodes with a shortest weighted path of at most _ν∗_ . Hence, for a set of scale thresholds _ν_ 1 _≤ . . . νn_ , we obtain a VR filtration _V R_<sup>1</sup> _⊆ . . . ⊆ V R_<sup>_n_</sup> . Alternatively, (ii) we can consider a sublevel filtration induced by a continuous function _f_ defined on nodes of _G_ . Let _f_ : _V �_ R and _ν_ 1 _< ν_ 2 _< . . . < νn_ be a sequence of sorted filtered values, then _C_<sup>_i_</sup> = _{σ ∈ C_ : max _v∈σ f_ ( _v_ ) _≤ νi}_ . Note that a VR filtration (i) is a subcase of sublevel filtration (ii) with _f_ being the diameter function (Adams et al., 2017; Bauer, 2019). 

**Time-Aware Zigzag Persistence** Since our primary aim 

is to assess interconnected evolution of multiple timeconditioned objects, the developed methodology for tracking topological and geometric properties of these objects shall ideally account for their intrinsically dynamic nature. We address this goal by introducing the concept of _zigzag_ persistence into GNN. Zigzag persistence is a generalization of persistent homology proposed by (Carlsson & Silva, 2010) and provides a systematic and mathematically rigorous framework to track the most important topological features of the data persisting over time. 

Let _{Gt}_ 1<sup>_T_be a sequence of networks observed over time.</sup> The key idea of zigzag persistence is to evaluate pairwise compatible topological features in this time-ordered sequence of networks. First, we define a set of network inclusions over time 



where _Gk ∪Gk_ +1 is defined as a graph with a node set _Vk ∪ Vk_ +1 and an edge set _Ek ∪ Ek_ +1. Second, we fix a 

scale parameter _ν∗_ and build a zigzag diagram of simplicial complexes for the given _ν∗_ over the constructed set of network inclusions 



Using the zigzag filtration for the given _ν∗_ , we can track birth and death of each topological feature over _{Gt}_ 1<sup>_T_as</sup> time points _tb_ and _td_ , 1 _≤ tb ≤ td ≤ T_ , respectively. Similarly to a non-dynamic case, we can extend the notion of persistence diagram for the analysis of topological characteristics of time-varying data delivered by the zigzag persistence. 

**Definition 3.1** (Zigzag Persistence Diagram (ZPD)) **.** Let _tb_ and _td_ be time points, when a topological feature first appears (i.e., is born) and disappears (i.e., dies) in the time period [1 _, T_ ] over the zigzag diagram of simplicial complexes for a fixed scale parameter _ν∗_ , respectively. If the topological feature first appears in _C_ ( _Gk, ν∗_ ), _tb_ = _k_ ; if it first appears in _C_ ( _Gk ∪Gk_ +1 _, ν∗_ ), _tb_ = _k_ +1 _/_ 2. Similarly, if a topological feature last appears in _C_ ( _Gk, ν∗_ ), _td_ = _k_ ; and if it last appears in _C_ ( _Gk ∪Gk_ +1 _, ν∗_ ), _td_ = _k_ +1 _/_ 2. A multiset of points in R<sup>2</sup> DgmZZ _ν∗_ = _{_ (tb _,_ td) _∈_ R<sup>2</sup> _|_ tb _<_ tb _}_ for a fixed _ν∗_ is called a _zigzag persistence diagram (ZPD)_ . 

Inspired by the notion of a persistent image as a summary of ordinary persistence (Adams et al., 2017), to input topological information summarized by ZPD into a GNN, we propose a representation of ZPD as _zigzag persistence image_ (ZPI). ZPI is a finite-dimensional vector representation of a ZPD and can be computed through the following steps: 

- _Step 1:_ Map a zigzag persistence diagram DgmZZ _ν∗_ to an integrable function _ρ_ DgmZZ _ν∗_ : R<sup>2</sup> _�_ R<sup>2</sup> , called a _zigzag persistence surface_ . The zigzag persistence surface is given by sums of weighted Gaussian functions that are centered at each point in DgmZZ _ν∗_ . 

- _Step 2:_ Perform a discretization and linearization of a subdomain of zigzag persistence surface _ρ_ DgmZZ _ν∗_ in a grid. 

- _Step 3:_ The ZPI, i.e., a matrix of pixel values, can be obtained by subsequent integration over each grid box. 

The value of each pixel _z ∈_ R<sup>2</sup> within a ZPI is defined as: 



where DgmZZ<sup>_′_</sup> _ν∗_<sup>is the transformed multi-set in DgmZZ</sup> _ν∗_<sup>,</sup> i.e., DgmZZ<sup>_′_</sup> _ν∗_<sup>(x</sup><sup>_,_y)=(x</sup><sup>_,_y</sup><sup>_−_x);</sup><sup>_g_(</sup><sup>_µ_)isaweighting</sup> 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

function with mean _µ_ = ( _µx, µy_ ) _∈_ R<sup>2</sup> and variance _ϑ_<sup>2</sup> , which depends on the distance from the diagonal. Here the zigzag persistence surface is defined by _ρ_ DgmZZ _ν∗_ = � _µ∈ZP D_<sup>_′ g_(</sup><sup>_µ_) exp</sup> � _−||z − µ||_<sup>2</sup> _/_ 2 _ϑ_<sup>2�</sup> . 

**Proposition 3.1.** _Let g_ : R<sup>2</sup> _�_ R _be a non-negative continuous and piece-wise differentiable function. Let_ DgmZZ _ν∗ be a zigzag persistence diagram for some fixed scale parameter ν∗, and let_ ZPI _ν∗ be its corresponding zigzag persistence image. Then,_ ZPI _ν∗ is stable with respect to the Wasserstein1 distance between zigzag persistence diagrams._ 

Tracking evolution of topological patterns in these sequences of time-evolving graphs allows us to glean insights into which properties of the observed time-conditioned objects, e.g., traffic data or Ethereum transaction graphs, tend to persist over time and, hence, are likelier to play a more important role in predictive tasks. 

## **4. Z-GCNETs** 

Given the graph _G_ and graph signals **_X_**<sup>_τ_</sup> = _{_ **_X_** _t−τ , . . . ,_ **_X_** _t−_ 1 _} ∈_ R<sup>_τ×N×F_</sup> of _τ_ past time periods (i.e. window size _τ_ ; where **_X_** _i ∈_ R<sup>_N×F_</sup> and _i ∈{t − τ, . . . , t −_ 1 _}_ ), we employ a model targeted on multi-step time series forecasting. That is, given the windows size _τ_ of past graph signals and the ahead horizon size _h_ , our goal is to learn a mapping function which maps the historical data _{_ **_X_** _t−τ , . . . ,_ **_X_** _t−_ 1 _}_ into the future data 



_Figure 1._ Illustrations of 0- and 1-dimensional ZPD and 0- and 1-dimensional ZPI for PeMSD4 dataset using the sliding window size _τ_ = 12, i.e., dynamic network with 12 graphs. Upper part shows the 0-dimensional ZPD and ZPI whilst the lower part is the 1-dimensional ZPD and ZPI. 

_{_ **_X_** _t, . . . ,_ **_X_** _t_ + _h}_ . 

**Laplacianlink** In spatial-temporal domain, the topology of graph may have different structure at different points in time. In this paper, we use the self-adaptive adjacency matrix (Wu et al., 2019) as the normalized Laplacian by trainable node embedding dictionaries **_φ_** _∈_ R<sup>_N×c_</sup> , i.e., **_L_** = _softmax_ ( _ReLU_ ( **_φφ_**<sup>_⊤_</sup> )), where the dimension of embedding _c ≥_ 1. Although introducing node embedding dictionaries allows capture hidden spatial dependence information, it cannot sufficiently capture the global graph information and the similarity between nodes. To overcome the limits and explore neighborhoods of nodes at different depths, we define a novel polynomial representation for Laplacian based on positive powers of the Laplacian matrix. In this work, Laplacianlink **_L_**<sup>˜</sup> is formulated as: 



where _K ≥_ 1, **_I_** _∈_ R<sup>_N×N_</sup> represents the identity matrix, and **_L_**<sup>_k_</sup> _∈_ R<sup>_N×N_</sup> , with 0 _≤ k ≤ K_ , denotes the power series of normalized Laplacian. 

By _linking_ (i.e., stacking) the power series of normalized Laplacian, we build a diffusion formalism to accumulate neighbors’ information of different power levels. Hence, each node will successfully exploit and propagate spatialtemporal correlations after spatial and temporal graph convolutional operations. 

**Spatial graph convolution** To model the spatial network _Gt_ at timestamp _t_ with its node feature matrix **_X_** _t_ , we define the spatial graph convolution as multiplying the input of each layer with the Laplacianlink **_L_**<sup>˜</sup> , which is then fed into the trainable projection matrix **Θ** = **_φV_** (where **_V_** stands for the trainable weight). In spatial-temporal graph modeling, we prefer to use weight sharing in matrix factorization rather than directly assigning a trainable weight matrix in order not only to avoid the risk of over-fitting but also to reduce the computational complexity. We compute the transformation in spatial domain, in each layer, as follows: 



where **_φ_** _∈_ R<sup>_N×c_</sup> is the node embedding and **_V_** _∈_ R<sup>_c×_(</sup><sup>_K_+1)</sup><sup>_×Cin×_(</sup><sup>_Cout/_2)</sup> is the trainable weight ( _Cin_ and _Cout_ are the number of channels in input and output, respectively). **_H_**<sup>(</sup> _i,_<sup>_ℓ_</sup> _S_<sup>_−_1)</sup> _∈_ R<sup>_N×_(</sup><sup>_Cin/_2)</sup> is the matrix of activations of spatial graph convolution to the _ℓ_ -th layer and **_H_**<sup>(0)</sup> _i,S_<sup>=</sup><sup>**_X_**</sup><sup>_i_.Asaresult,allinformationregardingthe</sup> _ℓ_ -layered input at time _i_ are reflected in the latest state variable. 

**Temporal graph convolution** In addition to spatial domain, the nature of spatial-temporal networks includes temporal relationships among consistent spatial networks. To catch 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 



_Figure 2._ The architecture of Z-GCNETs. Given a sliding window, e.g. ( _Gt−_ 3 _, . . . , Gt_ ), we extract zigzag persistence image (ZPI) based on zigzag filtration. For the ZPI _∈_ R<sup>2</sup> with the shape of _p × p_ , Z-GCNETs first learn the topological features of the ZPI through CNN-based framework, and then apply global max-pooling to obtain the maximum values among pooled activation maps. The output of zigzag persistence representation learning is decoded into spatial graph convolution and temporal graph convolution, where the inputs of spatial graph convolution and temporal graph convolution are current timestamps, e.g. _Gt_ in red dashed box, and the sliding window (i.e., ( _Gt−_ 3 _, . . . , Gt_ ) in yellow dashed box) respectively. After graph convolution operations, features from time-aware zigzag topological layer are combined and moved to GRU to perform forecasting. Symbol _⊗_ represents dot product whilst _⊕_ denotes combination. 

the temporal correlation patterns of nodes, we choose longer window size (i.e., by using the entire sliding window as input) and apply temporal graph convolution to graph signals in sliding window **_X_**<sup>_τ_</sup> . The mechanism has several excellent properties: (i) there is no need to select a particular size of nested sliding window, i.e., does not introduce additional computational complexity, (ii) temporal correlation patterns can be well captured and evaluated by (long) window sizes, whereas short window sizes (i.e., nested sliding window) are likely to be bias and noise, and (iii) the sliding window **_X_**<sup>_τ_</sup> maximizes the efficiency of estimating temporal correlations. The temporal graph convolution is presented in the form: 



where **_U_**<sup>(</sup><sup>_ℓ_)</sup> _∈_ R<sup>_c×Cin×_(</sup><sup>_Cout/_2)</sup> is trainable weight and **_U_**<sup>(0)</sup> _∈_ R<sup>_c×F ×_(</sup><sup>_Cout/_2)</sup> , **_Q_** _∈_ R<sup>_τ×_1</sup> is the trainable projection vector in temporal graph convolutional layer, and **_H_**<sup>(</sup><sup>_ℓ−_1)</sup> _∈_ R<sup>_τ×N×_(</sup><sup>_Cin/_2)</sup> is the hidden matrix fed to the _i,T ℓ_ -th layer and **_H_**<sup>(0)</sup> _i,T_<sup>=</sup><sup>**_X_**</sup><sup>_τ∈_R</sup><sup>_τ×N×F_.</sup> 

**Time-aware zigzag topological layer** To learn the topological features across a range of spatial and temporal scales, we extend the CNN model to be used along with ZPI. In this research, we present a framework to aggregate the topological persistent features into the feature representation learned from GCN. Let ZPI<sup>_τ_</sup> denotes the ZPI based on the sliding window **_X_**<sup>_τ_</sup> . (Here for brevity we suppress dependence of ZPI on a scale parameter _ν∗_ .) We design the time-aware zigzag topological layer to (i) extract and learn the spatial-temporal topological features contained in ZPI, (ii) aggregate transformed information from (spatial or temporal) graph convolution and spatial-temporal topological information from zigzag persistence module, and (iii) mix spatial-temporal and spatial-temporal topological 

information. The information’s extraction, aggregation, and combination processes are expressed as: 



where _f_ cnn<sup>(</sup><sup>_ℓ_)representstheconvolutionalneuralnetwork</sup> (CNN) in the _ℓ_ -th layer, _ξ_ max( _·_ ) denotes global max-pooling operation, **_Z_**<sup>(</sup><sup>_ℓ_)</sup> _∈_ R<sup>(</sup><sup>_Cout/_2)</sup> is the learned zigzag persistence representation from CNN, **_S_**<sup>(</sup> _i_<sup>_ℓ_)</sup> _∈_ R<sup>_N×_(</sup><sup>_Cout/_2)</sup> is the aggregated spatial<sup>2</sup> -temporal representation, **_T_**<sup>(</sup> _i_<sup>_ℓ_)</sup> _∈_ R<sup>_N×_(</sup><sup>_Cout/_2)</sup> is the aggregated spatial-temporal<sup>2</sup> representation, and the output of time-aware zigzag topological layer **_H_**<sup>(</sup> _i,out_<sup>_ℓ_)</sup><sup>_∈_R</sup><sup>_N×Cout_combines hidden states</sup><sup>**_S_**</sup> _i_<sup>(</sup><sup>_ℓ_)</sup> and **_T_**<sup>(</sup> _i_<sup>_ℓ_)</sup> at time _i_ . 

**GRU with time-aware zigzag topological layer** GRU is a variant of LSTM network. Compared with LSTM, GRU has a simpler structure, fewer training parameters, and more easily overcome vanishing and exploding gradient problems. The feed forward propagation of GRU with time-aware zigzag topological layer is recursively conducted as: 



where _ϕ_ ( _·_ ) is a non-linear function, i.e., the ReLU function; _⊙_ is the elementwise product; **_z_** _i_ and **_r_** _i_ are update gate and reset gate, respectively; **_b_** _z_ , **_b_** _r_ , **_b_** _o_ , **_W_** _z_ , **_W_** _r_ , and **_W_** _o_ 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

_Table 1._ Summary of datasets used in time series forecasting tasks. [ _†_ ] means the average number of edges in transportation networks under threshold _ν∗_ . 

|**Dataset**|**# Nodes**|**Avg # edge**|**s**<br>**Time range**|
|---|---|---|---|
|Bytom|100|9.98|27/07/2017 - 07/05/2018|
|Decentraland|100|16.94|14/10/2017 - 07/05/2018|
|PeMSD4|307|316.10<sup>_†_</sup>|01/01/2018 - 28/02/2018|
|PeMSD8|170|193.53<sup>_†_</sup>|01/07/2016 - 31/08/2016|



are trainable parameters; [ **_O_** _i−_ 1 _,_ **_H_** _i,out_ ] and **_O_** _i_ are the input and output of GRU model, respectively. In this way, Z-GCNETs contains structural, temporal, and topological information. 

## **5. Experiments** 

### **5.1. Datasets** 

We consider two types of networks (i) traffic network and (ii) Ethereum token network. Statistical overview of all datasets is given in Table 1. We now describe the detailed construction of traffic and Ethereum transaction networks as follows (i) The freeway Performance Measurement System (PeMS) data sources (i.e., PeMSD4 and PeMSD8) (Chen et al., 2001) collects real time traffic data in California. Both PeMSD4 and PeMSD8 datasets are aggregated to 5 minutes, therefore there are overall 16,992 and 17,856 data points in PeMSD4 and PeMSD8, respectively. In the traffic network, the node is represented by the loop detector which can detect real time measurement of traffic conditions and the edge is a freeway segment between two nearest nodes. Thus, the node feature matrix of traffic network _Xt ∈_ R<sup>_N×_3</sup> denotes that each node has 3 features (i.e., flow rate, speed, and occupancy) at time _t_ . To capture both spatial and temporal dependencies, we reconstruct the traffic graph structure _Gt_ = _{V, E, Wt_<sup>_ν∗}_attime</sup><sup>_t_.Here,wedefinethe</sup><sup>_right_</sup> _censoring_ weight _Wt_<sup>_ν∗_</sup> 



where _wt,uv_ = _e_<sup>_−||xt,u−xt,v||_2</sup><sup>_/γ_</sup> is based on the Radial Basis Function (RBF). To investigate the topology of weighted graph, the traffic graph structure _Gt_ is obtained via sub-level sets of the weight function, that is, we restrict to the final graph keep all edges of weights _ωt,uv_<sup>_ν∗_beloworequalto</sup> threshold _ν∗_ and therefore threshold _ν∗_ makes a difference in the topology of resulting graphs at different observation points. In experiments, we assign parameter _γ_ = 1 _._ 0 to RBF and set the thresholds in PeMSD4 and PeMSD8 to _ν∗_ = 0 _._ 5 and _ν∗_ = 0 _._ 3, respectively. (ii) The Ethereum blockchain was developed in 2014 to implement Smart Con- 

tracts, which are used to create and sell digital assets on the network<sup>1</sup> . In particular, token assets are specially valuable because each token naturally represents a network layer with the same nodes, i.e., addresses of users, appearing in the networks, i.e., layers, of multiple tokens (di Angelo & Salzer, 2020). For our experiments, we extract two token networks with more than $100M in market value<sup>2</sup> , Bytom and Decentraland tokens, from the publicly available Ethereum blockchain. We focus our analysis on the dynamic network generated by the daily transactions on each token network, and historical daily closed prices<sup>2</sup> . Since each token has different creation date<sup>3</sup> , Bytom dynamic network contains 285 nets whilst Decentraland dynamic network has 206 nets. Ethereum’s token networks have an average of 442788/1192722 nodes/edges. To maintain a reasonable computation time, we obtain a subgraph via the maximum weight subgraph approximation method of (Vassilevska et al., 2006), which allows to reduce the dynamic network size considering only most _M_ active edges and its corresponding nodes. In these experiments, we use dynamic networks with _N_ = 100 nodes. Let _Gt_ = _{Vt, Et, W_<sup>˜</sup> _t}_ denotes the reduced Ethereum blockchain network on day _t_ and _Xt ∈_ R<sup>_N×_1</sup> be the node feature matrix, we assume a solely node feature: the node degree. Each node in _Vt_ is a buyer/seller and edges in _Et_ represent transactions in the network. To construct the similarity matrix _W_<sup>˜</sup> _t_ , the normalized number of transactions between node pairs ( _u, v_ ) serves as the edge weight value _wt,uv ∈ W_<sup>˜</sup> _t_ . 

### **5.2. Experiment Settings** 

For multi-step time series forecasting, we evaluate the performances of Z-GCNETs on 4 time series datasets versus 13 state-of-the-art baselines (SOAs). Among them, Historical Average (HA) and Vector Auto-Regression (VAR) (Hamilton, 2020) are the statistical time series models. FCLSTM (Sutskever et al., 2014) and GRU-ED (Cho et al., 2014) are RNN-based neural networks. DSANet (Huang et al., 2019) is the self-attention networks. DCRNN (Li et al., 2018), STGCN (Yu et al., 2018a), GraphWaveNet (Wu et al., 2019), ASTGCN (Guo et al., 2019), MSTGCN (Guo et al., 2019), STSGCN (Song et al., 2020) are the spatial-temporal GCNs. AGCRN (Bai et al., 2020) and LSGCN (Huang et al., 2020) are the GRU-based GCNs. We conduct our experiments on NVIDIA GeForce RTX 3090 GPU card with 24GB memory. The PeMSD4 and PeMSD8 are split in chronological order with 60% for training sets, 20% for validation sets, and 20% for test sets. For PeMSD4 and PeMSD8, Z-GCNETs contains 2 layers, with each layer has 64 hidden units. We consider the window size _τ_ = 12 and horizon _h_ = 12 for Z-GCNETs on both PeMSD4 and 

> 1Ethereum.org 

> 2EtherScan.io 

> 3End date: May 7, 2018 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

_Table 2._ Forecasting <u>performance comparison of different approaches on PeMSD4 and PeMSD8 datasets.</u> 

|**Model**||**PeMSD**|**4**||**PeMSD**|**8**|
|---|---|---|---|---|---|---|
||MAE|RMSE|MAPE|MAE|RMSE|MAPE|
|HA|38.03|59.24|27.88%|34.86|52.04|24.07%|
|VAR (Hamilton,2020)|24.54|38.61|17.24%|19.19|29.81|13.10%|
|FC-LSTM (Sutskever et al.,2014)|26.77|40.65|18.23%|23.09|35.17|14.99%|
|GRU-ED (Cho et al.,2014)|23.68|39.27|16.44%|22.00|36.23|13.33%|
|DSANet (Huang et al.,2019)|22.79|35.77|16.03%|17.14|26.96|11.32%|
|DCRNN (Li et al.,2018)|21.22|37.23|14.17%|16.82|26.36|10.92%|
|STGCN (Yu et al.,2018a)|21.16|35.69|13.83%|17.50|27.09|11.29%|
|GraphWaveNet (Wu et al.,2019)|28.15|39.88|18.52%|20.30|30.82|13.84%|
|ASTGCN (Guo et al.,2019)|22.93|34.33|16.56%|18.25|28.06|11.64%|
|MSTGCN (Guo et al.,2019)|23.96|37.21|14.33%|19.00|29.15|12.38%|
|STSGCN (Song et al.,2020)|21.19|33.69|13.90%|17.13|26.86|10.96%|
|AGCRN (Bai et al.,2020)|19.83|32.30|12.97%|15.95|25.22|10.09%|
|LSGCN (Huang et al.,2020)|21.53|33.86|13.18%|17.73|26.76|11.20%|
|**Z-GCNETs (ours)**|**19.50**|**31.61**|**12.78%**|**15.76**|**25.11**|**10.01%**|



PeMSD8 datasets. Besides, the inputs of PeMSD4 and PeMSD8 are normalized by min-max normalization approach. We split Bytom and Decentraland with 80% for 

_Table 3._ The computation cost for the generation of zigzag persistence image (ZPI) and a single training epoch of Z-GCNETs. 

|**Dataset**|**Window Size **|<sup>**Aver**</sup><br>ZPI|<sup>**age Time Taken (sec)**</sup><br>Z-GCNETs (epoch)|
|---|---|---|---|
|Decentraland|7|0.03|2.09|
|Bytom|7|0.03|2.05|
|PeMSD4|12|0.86|30.12|
|PeMSD8|12|0.65|36.76|



training sets and 20% for test sets. For token networks, Z- GCNETs contains 2 layers, where each layer has 16 hidden units. We use one week historical data to predict the next week’s data, i.e., window size _τ_ = 7 and horizon _h_ = 7 over Bytom and Decentralnad datasets. All reported results are based on the weight rank clique filtration. More detailed description of the experimental settings can be found in Appendix A, while the analysis of sensitivity with respect to the choice of filtration is in Appendix B. The code is available at https://github.com/Z-GCNETs/Z-GCNETs.git. 

Table 3 reports the average running time of ZPI generation and training time per epoch of our Z-GCNETs model on all datasets. 

### **5.3. Comparison with the Baseline Methods** 

Table 2 shows the comparison of our proposed Z-GCNETs and SOAs for traffic flow forecasting tasks. We assess model performance with Mean Absolute Error (MAE), Root Mean 

Square Error (RMSE), and Mean Absolute Percentage Error (MAPE) on PeMSD4 and PeMSD8. From Table 2, we find that our proposed model Z-GCNETs consistently outperforms SOAs on PeMSD4 and PeMSD8. The improvement gain of Z-GCNETs over the next most accurate methods ranges from 0.44% to 2.06% in RMSE for PeMSD4 and PeMSD8. Table 4 shows the performance results on Bytom and Decentraland using RMSE. We find that Z-GCNETsfor the weight rank clique filtration outperforms AGCRN by margins of 3.42% and 2.94% (see the results in Appendix B for other types of filtrations). In contrast with SOAs, Z- GCNETs fully leverages the topological information by incorporating zigzag topological features via CNN on topological space. Given the continuous nature of time series data, our analysis and experiments show that establishing a connection between the time zigzag pairs is naturally a perfect fit to topological spaces and continuous maps. 

_Table 4._ Forecasting results (MAPE) on Ethereum token networks. 

|**Model**|**Bytom **|**Decentraland**|
|---|---|---|
|FC-LSTM (Sutskever et al.,2014)|40.72%|33.46%|
|DCRNN (Li et al.,2018)|35.36%|27.69%|
|STGCN (Yu et al.,2018a)|37.33%|28.22%|
|GraphWaveNet (Wu et al.,2019)|39.18%|37.67%|
|ASTGCN (Guo et al.,2019)|34.49%|27.43%|
|AGCRN (Bai et al.,2020)|34.46%|26.75%|
|LSGCN (Huang et al.,2020)|34.91%|28.37%|
|**Z-GCNETs**|**31.04%**|**23.81%**|



**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

### **5.4. Ablation Study** 

To better understand the importance of the different components in Z-GCNETs, we conduct ablation studies on PeMSD4 and PeMSD8 and the results are presented in Table 5. The results show that Z-GCNETs have better performance over Z-GCNETs without zigzag persistence representation learning (zigzag learning), spatial graph convolution (GCNSpatial), or temporal graph convolution (GCNTemporal). Specifically, we observe that when removing GCNTemporal, the multi-step forecasting is affected significantly, i.e., Z- GCNETs outperforms Z-GCNETs without temporal graph convolution with relative gain 6.46% on RMSE for PeMSD4. Comparison results on PeMSD8, w/o zigzag learning and w/o show the necessity for encoding topological information and modeling spatial structural information in multi-step forecasting over spatial-temporal time series dataset. Additional results for the ablation study on Ethereum tokens are presented in Appendix C. 

_Table 6._ Results of zigzag persistence on the dynamic network with different dimensional features and threshold values <u>(</u> _ν∗_ <u>).</u> 

||**Zigzag module**||**PeMSD**|**4**|
|---|---|---|---|---|
|||MAE|RMSE|MAPE|
||0-th ZPI_ν∗_=0_._3|19.73|32.04|12.93%|
|**Z-GCNETs**+|1-st ZPI_ν∗_=0_._3|19.47|31.66|12.75%|
||0-th ZPI_ν∗_=0_._5|19.78|32.20|12.98%|
||1-st ZPI_ν∗_=0_._5|19.50|31.61|12.78%|
||**Zigzag module**||**PeMSD**|**8**|
|||MAE|RMSE|MAPE|
||0-th ZPI_ν∗_=0_._3|17.14|27.24|10.66%|
|**Z-GCNETs**+|1-st ZPI_ν∗_=0_._3|15.76|25.11|10.01%|
||0-th ZPI_ν∗_=0_._5|17.22|27.41|10.77%|
||1-st ZPI_ν∗_=0_._5|16.77|26.62|10.39%|



### **5.6. Robustness Study** 

_Table 5._ Ablation study of the network architecture. [*] means the GCNSpatial is only applied to the most recent time point in the sliding window. 

||**Architecture**|**MAE **|**RMSE **|**MAPE**|
|---|---|---|---|---|
||**Z-GCNETs**|**19.50**|**31.61**|**12.78%**|
|**PMSD4**|W/o Zigzag learning|19.65|31.94|13.01%|
|**e**|W/o GCNSpatial<sup>_∗_</sup>|19.86|31.96|13.19%|
||W/o GCNTemporal|20.76|33.18|13.60%|
||**Z-GCNETs**|**15.76**|**25.11**|**10.01%**|
|**PMSD8**|W/o Zigzag learning|17.16|27.06|10.77%|
|**e**|W/o GCNSpatial<sup>_∗_</sup>|16.92|26.86|10.33%|
||W/o GCNTemporal|16.66|26.44|10.39%|



To assess robustness of Z-GCNETs under noisy conditions, we consider adding Gaussian noise into 30% of training sets. The added noise follows zero-mean i.i.d Gaussian density with fixed variance _ς_<sup>2</sup> , i.e., _N_ (0 _, ς_<sup>2</sup> ), where _ς ∈{_ 2 _,_ 4 _}_ . In Table 7 we report comparisons with two competitive baselines (AGCRN and LSGCN) on Decentraland and PeMSD4 using two different noise levels. Table 7 shows the performance of Z-GCNETs and two SOAs under described noisy conditions. We can see that the performance of all methods decays slowly with respect to the Gaussian noises. Despite that, we can see that Z-GCNETs is still consistently more robust than SOAs on both Decentraland and PeMSD4. On the other hand, for influence shown in Table 7, all methods have relative lower RMSE, proving that the Gaussian noises are usually less effective for graph convolution-based models. 

### **5.5. How does time-aware zigzag persistence help?** 

To track the importance of _p_ -dimensional topological features in Z-GCNETs (i.e., 0-dimensional and 1-dimensional holes), we evaluate the performance of Z-GCNETs on two different aspects: (i) the sensitivity of Z-GCNETs to different dimensional topological features and (ii) the effects of threshold _ν∗_ in constructed input networks along with zigzag persistence. Table 6 summarizes the results using different dimensional topological features and different thresholds on PeMSD4 and PeMSD8. Under the same scale parameter _ν∗_ , we find that 1-dimensional topological features consistently outperform 0-dimensional terms on both datasets. Furthermore, the forecasting results on PeMSD4 are not significantly affected by varying _ν∗_ . However, on on PeMSD8 1-dimensional topological features constructed under _ν∗_ of 0.3 yield better results than 1-dimensional terms constructed under _ν∗_ = 0 _._ 5. 

_Table 7._ Robustness study on Decentraland and PeMSD4 (RMSE). 

||**Noise**<br>|**AGCRN LSGCN Z-**|**GCNETs (ours)**|
|---|---|---|---|
|**Dtld**|<sup>_N_(0</sup><sup>_,_ 2) </sup>|<sup>27.69</sup><br>36.10|**24.12**|
|**ecenraan**|<br>_N_(0_,_4)|28.12<br>36.79|**25.03**|
|**PeMSD4**|_N_(0_,_2)|32.24<br>34.16|**31.95**|
||_N_(0_,_4)|32.67<br>34.75|**32.18**|



## **6. Conclusion** 

Inspired the recent call for developing time-aware deep learning mechanisms by the US Defense Advanced Research Projects Agency (DARPA), we have proposed a new time-aware zigzag topological layer (Z-GCNETs) for timeconditioned GCNs. Our idea is based on the concepts of 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

zigzag persistence whose utility remains unexplored not only in conjunction with time-aware GCN but DL in general. The new Z-GCNETs layer allows us to track the salient timeaware topological characterizations of the data persisting over time. Our results on spatio-temporal graph structured data have indicated that integration of the new time-aware zigzag topological layer into GCNs results both in enhanced forecasting performance and substantial robustness gains. 

## **7. Acknowledgements** 

The project has been supported in part by the grants NSF DMS 1925346, NSF ECCS 2039701, and NSF ECCS 1824716. 

## **References** 

- Adams, H. and Carlsson, G. Evasion paths in mobile sensor networks. _The International Journal of Robotics Research_ , 34(1):90–104, 2015. 

- Adams, H., Emerson, T., Kirby, M., Neville, R., Peterson, C., Shipman, P., Chepushtanova, S., Hanson, E., Motta, F., and Ziegelmeier, L. Persistence images: A stable vector representation of persistent homology. _Journal of Machine Learning Research_ , 18, 2017. 

- Adams, H., Bush, J., Carr, B., Kassab, L., and Mirth, J. A torus model for optical flow. _Pattern Recognition Letters_ , 129:304–310, 2020. 

- Bai, L., Yao, L., Li, C., Wang, X., and Wang, C. Adaptive graph convolutional recurrent network for traffic forecasting. _Advances in Neural Information Processing Systems_ , 33, 2020. 

- Bauer, U. Ripser: efficient computation of vietoris-rips persistence barcodes. _arXiv:1908.02518_ , 2019. 

- Carlsson, G. Persistent homology and applied homotopy theory. _Handbook of Homotopy Theory_ , 2019. 

- Carlsson, G. and Gabrielsson, R. B. Topological approaches to deep learning. In _Topological Data Analysis_ , pp. 119– 146. Springer, 2020. 

- Carlsson, G. and Silva, V. Zigzag persistence. _Found. Comput. Math._ , 10(4):367–405, August 2010. ISSN 16153375. 

- Carriere, M., Chazal, F., Ike, Y., Lacombe, T., Royer, M.,` and Umeda, Y. Perslay: A neural network layer for persistence diagrams and new graph topological signatures. In _AISTATS_ , pp. 2786–2796, 2020. 

- Chae, S., Kwon, S., and Lee, D. Predicting infectious disease using deep learning and big data. _International_ 

_Journal of Environmental Research and Public Health_ , 15:1596, 07 2018. doi: 10.3390/ijerph15081596. 

- Chen, C., Petty, K., Skabardonis, A., Varaiya, P., and Jia, Z. Freeway performance measurement system: mining loop detector data. _Transportation Research Record_ , 1748(1): 96–102, 2001. 

- Cho, K., Van Merrienboer,¨ B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., and Bengio, Y. Learning phrase representations using rnn encoder-decoder for statistical machine translation. _arXiv preprint arXiv:1406.1078_ , 2014. 

- Chowdhury, S., Dai, B., and Memoli,´ F. The importance of forgetting: Limiting memory improves recovery of topological characteristics from neural data. _PloS one_ , 13 (9):e0202561, 2018. 

- Corcoran, P. and Jones, C. B. Modelling topological features of swarm behaviour in space and time with persistence landscapes. _IEEE Access_ , 5:18534–18544, 2017. 

- Defferrard, M., Bresson, X., and Vandergheynst, P. Convolutional neural networks on graphs with fast localized spectral filtering. In Lee, D., Sugiyama, M., Luxburg, U., Guyon, I., and Garnett, R. (eds.), _Advances in Neural Information Processing Systems_ , volume 29, pp. 3844– 3852. Curran Associates, Inc., 2016. 

- di Angelo, M. and Salzer, G. Tokens, types, and standards: Identification and utilization in ethereum. In _2020 IEEE International Conference on Decentralized Applications and Infrastructures (DAPPS)_ , pp. 1–10, 2020. doi: 10. 1109/DAPPS49028.2020.00001. 

- Gamble, J., Chintakunta, H., and Krim, H. Coordinate-free quantification of coverage in dynamic sensor networks. _Signal Processing_ , 114:1–18, 2015. 

- Gao, S., Huang, Y., Zhang, S., Han, J., Wang, G., Zhang, M., and Lin, Q. Short-term runoff prediction with gru and lstm networks without requiring time step optimization during sample generation. _Journal of Hydrology_ , 589:125188, 2020. ISSN 0022-1694. doi: https://doi.org/10.1016/j.jhydrol.2020.125188. URL https://www.sciencedirect.com/ science/article/pii/S002216942030648X. 

- Greff, K., Srivastava, R. K., Koutn´ık, J., Steunebrink, B. R., and Schmidhuber, J. Lstm: A search space odyssey. _IEEE Transactions on Neural Networks and Learning Systems_ , 28(10):2222–2232, 2017. doi: 10.1109/TNNLS.2016. 2582924. 

- Guo, S., Lin, Y., Feng, N., Song, C., and Wan, H. Attention based spatial-temporal graph convolutional networks for 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

- traffic flow forecasting. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 33, pp. 922–929, 2019. 

- Hamilton, J. D. _Time series analysis_ . Princeton university press, 2020. 

- Hofer, C. D., Kwitt, R., and Niethammer, M. Learning representations of persistence barcodes. _JMLR_ , 20(126): 1–45, 2019. 

- Huang, R., Huang, C., Liu, Y., Dai, G., and Kong, W. Lsgcn: Long short-term traffic prediction with graph convolutional networks. In Bessiere, C. (ed.), _Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, IJCAI-20_ , pp. 2355–2361, 2020. 

- Huang, S., Wang, D., Wu, X., and Tang, A. Dsanet: Dual self-attention network for multivariate time series forecasting. In _Proceedings of the 28th ACM International Conference on Information and Knowledge Management_ , pp. 2129–2132, 2019. 

- Kim, W., Memoli, F., and Smith, Z.´ Analysis of dynamic graphs and dynamic metric spaces via zigzag persistence. In _Topological Data Analysis_ , pp. 371–389. Springer, 2020. 

- Kipf, T. N. and Welling, M. Semi-supervised classification with graph convolutional networks. _ICLR_ , 2017. 

- Li, Y., Yu, R., Shahabi, C., and Liu, Y. Diffusion convolutional recurrent neural network: Data-driven traffic forecasting. _International Conference on Learning Representations_ , 2018. 

- Pareja, A., Domeniconi, G., Chen, J., Ma, T., Suzumura, T., Kanezashi, H., Kaler, T., Schardl, T., and Leiserson, C. Evolvegcn: Evolving graph convolutional networks for dynamic graphs. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 34, pp. 5363–5370, 2020. 

- Schmidhuber, J. LSTM: Impact on the world’s most valuable public companies. http://people.idsia.ch/˜juergen/ impact-on-most-valuable-companies. html. Accessed: 2020-03-19. 

- Shin, S. and Kim, W. Skeleton-based dynamic hand gesture recognition using a part-based gru-rnn for gesture-based interface. _IEEE Access_ , 8:50236–50243, 2020. doi: 10. 1109/ACCESS.2020.2980128. 

- Song, C., Lin, Y., Guo, S., and Wan, H. Spatial-temporal synchronous graph convolutional networks: A new framework for spatial-temporal network data forecasting. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 34, pp. 914–921, 2020. 

- Sutskever, I., Vinyals, O., and Le, Q. V. Sequence to sequence learning with neural networks. _Advances in neural information processing systems_ , 27:3104–3112, 2014. 

- Tausz, A. and Carlsson, G. Applications of zigzag persistence to topological data analysis. _arXiv:1108.3545_ , 2011. 

- Tymochko, S., Munch, E., and Khasawneh, F. A. Hopf bifurcation analysis using zigzag persistence. _Algorithms_ , 13(11):278, 2020. 

- Vassilevska, V., Williams, R., and Yuster, R. Finding the smallest h-subgraph in real weighted graphs and related problems. In _Automata, Languages and Programming_ , pp. 262–273. Springer Berlin Heidelberg, 2006. 

- Velickoviˇ c, P., Cucurull, G., Casanova, A., Romero, A., Lio,´ P., and Bengio, Y. Graph attention networks. _ICLR_ , 2018. 

- Weber, M., Domeniconi, G., Chen, J., Weidele, D. K. I., Bellei, C., Robinson, T., and Leiserson, C. E. Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. _arXiv preprint arXiv:1908.02591_ , 2019. 

- Wu, Z., Pan, S., Long, G., Jiang, J., and Zhang, C. Graph wavenet for deep spatial-temporal graph modeling. In _Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19_ , pp. 1907– 1913, 2019. 

- Xian, L., Adams, H., Topaz, C. M., and Ziegelmeier, L. Capturing dynamics of time-varying data via topology. _arXiv:2010.05780_ , 2020. 

- Yan, S., Xiong, Y., and Lin, D. Spatial temporal graph convolutional networks for skeleton-based action recognition. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 32, 2018. 

- Yao, H., Wu, F., Ke, J., Tang, X., Jia, Y., Lu, S., Gong, P., Ye, J., and Li, Z. Deep multi-view spatial-temporal network for taxi demand prediction. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 32, 2018. 

- Yu, B., Yin, H., and Zhu, Z. Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting. In _Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18_ , pp. 3634–3640, 2018a. 

- Yu, B., Yin, H., and Zhu, Z. Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting. In _Proceedings of the TwentySeventh International Joint Conference on Artificial Intelligence, IJCAI-18_ , pp. 3634–3640. International Joint Conferences on Artificial Intelligence Organization, 7 

**Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting** 

- 2018b. doi: 10.24963/ijcai.2018/505. URL https: //doi.org/10.24963/ijcai.2018/505. 

- Yu, Y., Si, X., Hu, C., and Zhang, J. A review of recurrent neural networks: Lstm cells and network architectures. _Neural Comput._ , 31(7):1235–1270, 2019. 

- Yuan, J., Wang, H., Lin, C., Liu, D., and Yu, D. A novel gru-rnn network model for dynamic path planning of mobile robot. _IEEE Access_ , 7:15140–15151, 2019. doi: 10.1109/ACCESS.2019.2894626. 

## **C. Ablation study on Ethereum token networks** 

To make sure that all the components of the Z-GCNETs perform well, we also conduct ablation study on Ethereum token networks. Table 9 summarizes the results obtained on Bytom and Decentraland. The results demonstrate that our Z-GCNETs outperforms Z-GCNETs without zigzag persistence representation learning (zigzag learning), spatial graph convolution (GCNSpatial), and temporal graph convolution (GCNTemporal). 

_Table 9._ Ablation study <u>(MAPE) of Ethereum token networks.</u> 

## **A. Additional Experimental Settings** 

On PeMSD4 and PeMSD8, we train our model using Adam optimizer with an initial learning rate _lr_ = 0 _._ 003 and decay rate of _ρ_ = 0 _._ 3; whilst we set learning rate _lr_ to 0.001 and decay rate _ρ_ to 0.1 in Bytom and Decentraland datasets. The length of Laplacianlink is set to 2 and 3 for transportation networks and token networks, respectively. Our Z-GCNETs is trained with batch sizes of 64 and 8 on PeMSD4 and PeMSD8, respectively. On Ethereum token networks, we set the batch size to 8. We run the experiments for 300 epochs and 100 epochs on transportation networks and Ethereum token networks, respectively. In all experiments, we set the grid size of ZPI to 100 _×_ 100 and use CNN model to learn zigzag persistence representation. The CNN model consists of 2 CNN layers with number of filter set to 8, kernel size to 3, stride to 2, and the global max-pooling with the pool size of 5 _×_ 5. 

|**Architecture**|**D**<br>Bytom|**ataset**<br>Decentraland|
|---|---|---|
|**Z-GCNETs**|**31.04%**|**23.81%**|
|W/o Zigzag learning|33.19%|24.24%|
|W/o GCNSpatial|34.32%|25.22%|
|W/o GCNTemporal|31.25%|24.62%|



## **B. The Choice of Filtration** 

We now have also run experiments on the impact of the filtration choice. In addition to the weight rank clique filtration, we consider for power and weighted-degree sublevel filtrations. Table 8 shows a subset of illustrative results for Ethereum token networks. For sparser graphs such as Bytom, all filtrations tend to yield similar results. For more heterogeneous dynamic graphs with a richer topological structure, e.g., Decentraland, power filtration is the winner as it better captures evolution of the underlying graph organization. The proposed methodology is compatible with any filtration. 

_Table 8._ Z-GCNETs (MAPE) for different zigzag filtrations. 

|**Filtration**|**Weighted-deg**|**ree sublevel set**|**Power**|
|---|---|---|---|
|**Dataset**_\_**Scale**|Transaction|Volume|Volume|
|Bytom|30.56|30.80|30.79|
|Decentraland|25.18|24.93|22.15|



