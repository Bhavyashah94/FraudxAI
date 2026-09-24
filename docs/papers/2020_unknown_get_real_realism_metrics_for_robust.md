---
title: "Get Real: Realism Metrics for Robust Limit Order Book Market Simulations"
authors: "unknown"
year: 2020
arxiv_id: "2006.14384"
original_file: "2006.14384.pdf"
pdf_path: "docs/papers\2020_unknown_get_real_realism_metrics_for_robust.pdf"
---

# Get Real: Realism Metrics for Robust Limit Order Book Market Simulations

**Authors:** Unknown et al.  
**Year:** 2020 | **arXiv:** [`2006.14384`](https://arxiv.org/abs/2006.14384)  
**Local PDF:** [`2020_unknown_get_real_realism_metrics_for_robust.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_unknown_get_real_realism_metrics_for_robust.pdf)

---

# Dual-Free Stochastic Decentralized Optimization with Variance Reduction 

Hadrien Hendrikx<sup>_∗†_</sup> 

( `hadrien.hendrikx@inria.fr` ) 

Francis Bach<sup>_∗†_</sup> 

( `francis.bach@inria.fr` ) 

Laurent Massoulié<sup>_∗†_</sup> 

( `laurent.massoulie@inria.fr` ) 

##### **Abstract** 

We consider the problem of training machine learning models on distributed data in a decentralized way. For finite-sum problems, fast single-machine algorithms for large datasets rely on stochastic updates combined with variance reduction. Yet, existing decentralized stochastic algorithms either do not obtain the full speedup allowed by stochastic updates, or require oracles that are more expensive than regular gradients. In this work, we introduce a Decentralized stochastic algorithm with Variance Reduction called DVR. DVR only requires computing stochastic gradients of the local functions, and is computationally as fast as a standard stochastic variance-reduced algorithms run on a 1 _/n_ fraction of the dataset, where _n_ is the number of nodes. To derive DVR, we use Bregman coordinate descent on a well-chosen dual problem, and obtain a dual-free algorithm using a specific Bregman divergence. We give an accelerated version of DVR based on the Catalyst framework, and illustrate its effectiveness with simulations on real data. 

## **1 Introduction** 

We consider the regularized empirical risk minimization problem distributed on a network of _n_ nodes. Each node has a local dataset of size _m_ , and the problem thus writes: 



where _fij_ typically corresponds to the loss function for training example _j_ of machine _i_ , and _σi_ is the local regularization parameter for node _i_ . We assume that each function _fij_ is convex and _Lij_ -smooth (see, _e.g._ , Nesterov [2013]), and that each function _fi_ is _Mi_ -smooth. Following Xiao et al. [2019], we denote _κi_ = (1 +<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_Lij_)</sup><sup>_/σi_thestochasticconditionnumberof</sup><sup>_fi_,and</sup><sup>_κs_= max</sup><sup>_i κi_.</sup> Similarly, the batch condition number is _κb_ = max _i Mi/σi_ . It always holds that _κb ≤ κs ≤ mκb_ , but generally _κs ≪ mκb_ , which explains the success of stochastic methods. Indeed, _κs ≈ mκb_ when all Hessians are orthogonal to one another which is rarely the case in practice, especially for a large dataset. 

> _∗_ Département d’informatique de l’ENS, ENS, CNRS, PSL University, Paris, France 

> _†_ INRIA, Paris, France 

1 

Regarding the distributed aspect, we follow the standard _gossip_ framework [Boyd et al., 2006, Nedic and Ozdaglar, 2009, Duchi et al., 2012, Scaman et al., 2017] and assume that nodes are linked by a communication network which we represent as an undirected graph _G_ . We denote _N_ ( _i_ ) the set of neighbors of node _i_ and 1 _∈_ R<sup>_d_</sup> the vector with all coordinates equal to 1. Communication is abstracted by multiplication by a positive semi-definite matrix _W ∈_ R<sup>_n×n_</sup> , which is such that _Wkℓ_ = 0 if _k ∈N/_ ( _ℓ_ ), and Ker( _W_ ) = Span(1). The matrix _W_ is called the _gossip matrix_ , and we denote its spectral gap by _γ_ = _λ_<sup>+</sup> min<sup>(</sup><sup>_W_)</sup><sup>_/λ_max(</sup><sup>_W_),theratiobetweenthesmallestnon-zeroandthe</sup> highest eigenvalue of _W_ , which is a key quantity in decentralized optimization. We finally assume that nodes can compute a local stochastic gradient _∇fij_ in time 1, and that communication ( _i.e._ , multiplication by _W_ ) takes time _τ_ . 

**Single-machine stochastic methods.** Problem (1) is generally solved using first-order methods. When _m_ is large, computing _∇F_ becomes very expensive, and batch methods require _O_ ( _κb_ log( _ε_<sup>_−_1</sup> )) iterations, which takes time _O_ ( _mκb_ log( _ε_<sup>_−_1</sup> )), to minimize _F_ up to precision _ε_ . In this case, updates using the stochastic gradients _∇fij_ , where ( _i, j_ ) is selected randomly, can be much more effective [Bottou, 2010]. Yet, these updates are noisy and plain stochastic gradient descent (SGD) does not converge to the exact solution unless the step-size goes to zero, which slows down the algorithm. One way to fix this problem is to use variance-reduced methods such as SAG [Schmidt et al., 2017], SDCA [Shalev-Shwartz and Zhang, 2013], SVRG [Johnson and Zhang, 2013] or SAGA [Defazio et al., 2014]. These methods require _O_ (( _nm_ + _κs_ ) log( _ε_<sup>_−_1</sup> )) stochastic gradient evaluations, which can be much smaller than _O_ ( _mκb_ log( _ε_<sup>_−_1</sup> )). 

**Decentralized methods.** Decentralized adaptations of gradient descent in the smooth and strongly convex setting include EXTRA [Shi et al., 2015], DIGing [Nedic et al., 2017] or NIDS [Li et al., 2019]. These algorithms have sparked a lot of interest, and the latest convergence results [Jakovetić, 2018, Xu et al., 2020, Li and Lin, 2020] show that EXTRA and NIDS require time _O_ (( _κb_ + _γ_<sup>_−_1</sup> )( _m_ + _τ_ )) log( _ε_<sup>_−_1</sup> )) to reach precision _ε_ . A generic acceleration of EXTRA using Catalyst [Li and Lin, 2020] obtains the (batch) optimal _O_ (<sup>_√_</sup> _<u>κb</u>_ <u>(1 +</u> _τ/_<sup>_√_</sup> _<u>γ</u>_ <u>) log(</u> _ε_<sup>_−_1</sup> )) rate up to log factors. Another line of work on decentralized algorithms is based on the _penalty method_ [Li et al., 2018, Dvinskikh and Gasnikov, 2019]. This consists in performing traditional optimization algorithms to problems augmented with a Laplacian penalty, and in particular enables the use of accelerated methods. Yet, these algorithms are sensitive to the value of the penalty parameter (when it is fixed), since it directly influences the solution they converge to. Another natural way to construct decentralized optimization algorithms is through dual approaches [Scaman et al., 2017, Uribe et al., 2020]. Although the dual approach leads to algorithms that are optimal both in terms of number of communications and computations [Scaman et al., 2019, Hendrikx et al., 2020], they generally assume access to the proximal operator or the gradient of the Fenchel conjugate of the local functions, which is not very practical in general since it requires solving a subproblem at each step. 

**Decentralized stochastic optimization.** Although both stochastic and decentralized methods have a rich litterature, there exist few decentralized stochastic methods with linear convergence rate. Although DSA [Mokhtari and Ribeiro, 2016], or GT-SAGA [Xin et al., 2020] propose such algorithms, they respectively take time _O_ (( _mκs_ + _κ_<sup>4</sup> _s_<sup>_γ−_1(1 +</sup><sup>_τ_) log(</sup><sup>_ε−_1))and</sup><sup>_O_((</sup><sup>_m_+</sup><sup>_κ_2</sup> _s_<sup>_γ−_2)(1 +</sup><sup>_τ_) log(</sup><sup>_ε−_1))to</sup> reach precision _ε_ . Therefore, they have significantly worse rates than decentralized batch methods when _m_ = 1, and than single-machine stochastic methods when _n_ = 1. Other methods have better rates of convergence [Shen et al., 2018, Hendrikx et al., 2019b] but they require evaluation of proximal operators, which may be expensive. 

**Our contributions.** This work develops a dual approach similar to that of Hendrikx et al. 

2 

[2019b], which leads to a decentralized stochastic algorithm with rate _O_ ( _m_ + _κs_ + _τκb/_<sup>_√_</sup> _<u>γ</u>_ ), where the<sup>_√_</sup> _<u>γ</u>_ factor comes from Chebyshev acceleration, such as used in Scaman et al. [2017]. Yet, our algorithm, called DVR, can be formulated in the primal only, thus avoiding the need for computing expensive dual gradients or proximal operators. Besides, DVR is derived by applying Bregman coordinate descent to the dual of a specific augmented problem. Thus, its convergence follows from the convergence of block coordinate descent with Bregman gradients, which we prove as a side contribution. When executed on a single-machine, DVR is similar to dual-free SDCA [Shalev-Shwartz, 2016], and obtains similar rates. We believe that the same methodology could be applied to tackle non-convex problems, but we leave these extensions for future work. 

We present in Section 2 the derivations leading to DVR, namely the dual approach and the dual-free trick. Then, Section 3 presents the actual algorithm along with a convergence theorem based on block Bregman coordinate descent (presented in Appendix A). Section 4 shows how to accelerate DVR, both in terms of network dependence (Chebyshev acceleration) and global iteration complexity (Catalyst acceleration [Lin et al., 2017]). Finally, experiments on real-world data are presented in Section 5, that demonstrate the effectiveness of DVR. 

## **2 Algorithm Design** 

This section presents the key steps leading to DVR. We start by introducing a relevant dual formulation from Hendrikx et al. [2019b], then introduce the dual-free trick based on Lan and Zhou [2017], and finally show how this leads to DVR, an actual implementable decentralized stochastic algorithm, as a special case of the previous derivations. 

### **2.1 Dual formulation** 

The standard dual formulation of Problem (1) is obtained by associating a parameter vector to each node, and imposing that two neighboring nodes have the same parameters [Boyd et al., 2011, Jakovetić et al., 2014, Scaman et al., 2017]. This leads to the following constrained problem, in which we write _θ_<sup>(</sup><sup>_i_)</sup> _∈_ R<sup>_d_</sup> the local vector of node _i_ : 



Following the approach of Hendrikx et al. [2019b, 2020], we further split the _fi_ ( _θ_<sup>(</sup><sup>_i_)</sup> ) term into _σi∥θ_<sup>(</sup><sup>_i_)</sup> _∥_<sup>2</sup> _/_ 2 +<sup>�</sup><sup>_n_</sup> _j_ =1<sup>_fij_(</sup><sup>_θ_(</sup><sup>_ij_)),withtheconstraintthat</sup><sup>_θ_(</sup><sup>_i_)=</sup><sup>_θ_(</sup><sup>_ij_)forall</sup><sup>_j_.Thisisequivalenttothe</sup> previous approach performed on an augmented graph [Hendrikx et al., 2019b, 2020] in which each node is split into a star network with the regularization in the center and a local summand at each tip of the star. Thus, the equivalent augmented constrained problem that we consider writes: 



We now use Lagrangian duality, and introduce two kinds of multipliers. The variable _x_ corresponds to multipliers associated with the constraints given by edges of the communication graph ( _i.e._ , _θ_<sup>(</sup><sup>_k_)</sup> = _θ_<sup>(</sup><sup>_ℓ_)</sup> if _k ∈N_ ( _ℓ_ )), that we will call _communication edges_ . Similarly, _y_ corresponds to the 

3 

constraints associated with the edges that are specific to the augmented graph ( _i.e._ , _θ_<sup>(</sup><sup>_i_)</sup> = _θ_<sup>(</sup><sup>_ij_)</sup> _∀i, j_ ) that we call _computation_ or _virtual edges_ , since they are not present in the original graph and were constructed for the augmented problem. Therefore, there are _E_ communication edges (number of edges in the initial graph), and _nm_ virtual edges. The dual formulation of Problem (3) thus writes: 



and where ( _x, y_ ) _∈_ R<sup>(</sup><sup>_E_+</sup><sup>_nm_)</sup><sup>_d_</sup> is the concatenation of vectors _x ∈_ R<sup>_Ed_</sup> , which is associated with the communication edges, and _y ∈_ R<sup>_nmd_</sup> , which is the vector associated with computation edges. We denote Σ = Diag( _σ_ 1<sup>_−_1</sup><sup>_, · · ·, σ_</sup> _n_<sup>_−_1</sup><sup>_,_0</sup><sup>_, · · ·,_0)</sup><sup>_⊗Id∈_R</sup><sup>_n_(</sup><sup>_m_+1)</sup><sup>_d×n_(</sup><sup>_m_+1)</sup><sup>_d_and</sup><sup>_A_issuchthatforall</sup><sup>_z∈_R</sup><sup>_d_,</sup> _A_ ( _ek,ℓ ⊗ z_ ) = _µkℓ_ ( _uk − uℓ_ ) _⊗ Pkℓz_ for edge ( _k, ℓ_ ), where _Pkℓ_ = _Id_ if ( _k, ℓ_ ) is a communication edge, _Pij_ is the projector on Ker( _fij_ )<sup>_⊥_</sup> ≜ ( _∩x∈_ R _d_ Ker( _∇_<sup>2</sup> _fij_ ( _x_ )))<sup>_⊥_</sup> if ( _i, j_ ) is a virtual edge, _z_ 1 _⊗ z_ 2 is the Kronecker product of vectors _z_ 1 and _z_ 2, and _ek,ℓ ∈_ R<sup>_E_+</sup><sup>_nm_</sup> and _uk ∈ R_<sup>_n_(</sup><sup>_m_+1)</sup> are the unit vectors associated with edge ( _k, ℓ_ ) and node _k_ respectively. 

Note that the upper left _nd × nd_ block of _AA_<sup>_⊤_</sup> (corresponding to the communication edges) is equal to _W ⊗ Id_ where _W_ is a gossip matrix (see, _e.g._ , [Scaman et al., 2017]) that depends on the _µkℓ_ . In particular, _W_ is equal to the Laplacian of the communication graph if _µ_<sup>2</sup> _kℓ_<sup>=1</sup><sup>_/_2forall</sup> ( _k, ℓ_ ). For computation edges, the projectors _Pij_ account for the fact that the parameters _θ_<sup>(</sup><sup>_i_)</sup> and _θ_<sup>(</sup><sup>_ij_)</sup> only need to be equal on the subspaces on which _fij_ is not constant, and we choose _µij_ such that _µ_<sup>2</sup> _ij_<sup>=</sup><sup>_αLij_forsome</sup><sup>_α >_0.Althoughthisintroducesheaviernotations,explicitlywriting</sup><sup>_A_as</sup> an _n_ (1 + _m_ ) _d ×_ ( _E_ + _nm_ ) _d_ matrix instead of an _n_ (1 + _m_ ) _×_ ( _E_ + _nm_ ) matrix allows to introduce the projectors _Pij_ , which then yields a better communication complexity than choosing _Pij_ = _Id_ . See Hendrikx et al. [2019b, 2020] for more details on this dual formulation, and in particular on the construction on the augmented graph. Now that we have obtained a suitable dual problem, we would like to solve it without computing gradients or proximal operators of _fij_<sup>_∗_,whichcanbevery</sup> expensive. 

### **2.2 Dual-free trick** 

Dual methods are based on variants of Problem (4), and apply different algorithms to it. In particular, Scaman et al. [2017], Uribe et al. [2020] use accelerated gradient descent [Nesterov, 2013], and Hendrikx et al. [2019a,b] use accelerated (proximal) coordinate descent [Lin et al., 2015b]. Let _p_ comm denote the probability of performing a communication step and _pij_ be the probability that node _i_ samples a gradient of _fij_ , which are such that for all _i_ ,<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_pij_=1</sup><sup>_−p_comm.Applying</sup> a coordinate update with step-size _η/p_ comm to Problem (4) in the direction _x_ (associated with communication edges) writes: 



where we denote _∇x_ the gradient in coordinates that correspond to _x_ (communication edges), and _∇y,ij_ the gradient for coordinate ( _ij_ ) (computation edge). Similarly, the standard coordinate update of a local computation edge ( _i, j_ ) can be written as: 



4 

where the minimization problem actually has a closed form solution. Yet, as mentioned before, solving Equation (6) requires computing the derivative of _fij_<sup>_∗_.Inordertoavoidthis,atrickintroduced</sup> by Lan and Zhou [2017] and later used in Wang and Xiao [2017] is to replace the Euclidean distance term by a well-chosen Bregman divergence. More specifically, the Bregman divergence of a convex function _φ_ is defined as: 



Bregman gradient algorithms typically enjoy the same kind of guarantees as standard gradient algorithms, but with slightly different notions of _relative_ smoothness and strong convexity [Bauschke et al., 2017, Lu et al., 2018]. Note that the Bregman divergence of the squared Euclidean norm is the squared Euclidean distance, and the standard gradient descent algorithm is recovered in that case. We now replace the Euclidean distance by the Bregman divergence induced by function _φ_ : _y �→_ ( _Lij/µ_<sup>2</sup> _ij_<sup>)</sup><sup>_f_</sup> _ij_<sup>_∗_(</sup><sup>_µijy_(</sup><sup>_ij_)),whichisnormalizedtobe1-stronglyconvexsince</sup><sup>_f_</sup> _ij_<sup>_∗_is</sup><sup>_L−_</sup> _ij_<sup>1-strongly</sup> convex. We introduce the constant _α >_ 0 such that _µ_<sup>2</sup> _ij_<sup>=</sup><sup>_αLij_forallcomputationedges(</sup><sup>_i, j_).</sup> Using the definition of the Bregman divergence with respect to _φ_ , we write: 



In particular, if we know _∇fij_<sup>_∗_(</sup><sup>_µijy_</sup> _t_<sup>(</sup><sup>_ij_)</sup> ) then it is possible to compute _yt_<sup>(</sup> +1<sup>_ij_).Besides,</sup> 



so we can also compute _∇fij_<sup>_∗_(</sup><sup>_µijy_</sup> _t_<sup>(</sup> +1<sup>_ij_)),andwecanuseitforthenextstep.Therefore,insteadof</sup> computing a dual gradient at each step, we can simply choose _y_ 0<sup>(</sup><sup>_i_)</sup> = _µ_<sup>_−_</sup> _ij_<sup>1</sup><sup>_∇fij_(</sup><sup>_z_</sup> 0<sup>(</sup><sup>_ij_)</sup> ) for any _z_ 0<sup>(</sup><sup>_ij_)</sup> , and iterate from this. Therefore, the Bregman coordinate update applied to Problem (4) in the block of direction ( _i, j_ ) with _y_ 0<sup>(</sup><sup>_ij_)</sup> = _µ_<sup>_−_</sup> _ij_<sup>1</sup><sup>_∇fi_(</sup><sup>_z_</sup> 0<sup>(</sup><sup>_ij_)</sup> ) yields: 



The iterations of (9) are called a _dual-free_ algorithm because they are a transformation of the iterations from (6) that do not require computing _∇fij_<sup>_∗_anymore.Thisisobtainedbyreplacingthe</sup> Euclidean distance in (6) by the Bregman divergence of a function proportional to _fij_<sup>_∗_.</sup> 

### **2.3 Distributed implementation** 

Iterations from (9) do not involve functions _fij_<sup>_∗_anymore, which was our first goal.Yet, they consist in</sup> updating dual variables associated with edges of the augmented graph, and have no clear distributed meaning yet. In this section, we rewrite the updates of (9) in order to have an easy to implement 

5 

distributed algorithm. The key steps are (i) multiplication of the updates by _A_ , (ii) expliciting the gossip matrix and (iii) remarking that _θt_<sup>(</sup><sup>_i_)</sup> = (Σ _A_ ( _xt, yt_ ))<sup>(</sup><sup>_i_)</sup> converges to the primal solution for all _i_ . For a vector _z ∈_ R<sup>(</sup><sup>_n_+</sup><sup>_nm_)</sup><sup>_d_</sup> , we denote [ _z_ ]comm _∈_ R<sup>_nd_</sup> its restriction to the communication nodes, and [ _M_ ]comm _∈_ R<sup>_nd×nd_</sup> similarly refers to the restriction on communication edges of a matrix _M ∈_ R<sup>(</sup><sup>_n_+</sup><sup>_nm_)</sup><sup>_d×_(</sup><sup>_n_+</sup><sup>_nm_)</sup><sup>_d_</sup> . By abuse of notations, we call _A_ comm _∈_ R<sup>_nd×Ed_</sup> the restriction of _A_ to communication nodes and edges. We denote _P_ comm the projector on communication edges, and _P_ comp the projector on _y_ . We multiply the _x_ (communication) update in (9) by _A_ on the left (which is standard [Scaman et al., 2017, Hendrikx et al., 2019b]) and obtain: 



Note that [ _P_ comm _A_<sup>_⊤_</sup> Σ _A_ ( _xt, yt_ )]comm = [ _P_ comm _A_<sup>_⊤_</sup> ]comm[Σ _A_ ( _xt, yt_ )]comm because _P_ comm and Σ are non-zero only for communication edges and nodes. Similarly, and as previously stated, one can verify that _A_ comm[ _P_ comm _A_<sup>_⊤_</sup> ]comm = [ _AP_ comm _A_<sup>_⊤_</sup> ]comm = _W ⊗ Id ∈_ R<sup>_nd×nd_</sup> where _W_ is a gossip matrix. We finally introduce _x_ ˜ _t ∈_ R<sup>_nd_</sup> which is a variable associated with nodes, and which is such that _x_ ˜ _t_ = _A_ comm _xt_ . With this rewriting, the communication update becomes: 



To show that [ _A_ ( _xt, yt_ )]comm is locally accessible to each node, we write: 



We note this rescaled local vector _θt_ = Σcomm([ _A_ ( _xt, yt_ )]comm), and obtain for variables _x_ ˜ _t_ the gossip update of (12). Note that we directly write _yt_<sup>(</sup><sup>_ij_)</sup> instead of _Pijyt_<sup>(</sup><sup>_ij_)</sup> even though there has been a multiplication by the matrix _A_ . This is allowed because Equation (13) implies that (i) _yt_<sup>(</sup><sup>_ij_)</sup> _∈_ Ker( _fij_ )<sup>_⊥_</sup> for all _t_ , and (ii) the value of ( _Id − Pij_ ) _zt_<sup>(</sup><sup>_ij_)</sup> does not matter since _zt_<sup>(</sup><sup>_ij_)</sup> is only used to compute _∇fij_ . We now consider computation edges, and remark that: 



Plugging Equation (11) into the updates of (9), we obtain the following updates: 



for communication edges, and for the local update of the _j_ -th component of node _i_ : 



Finally, Algorithm 1 is obtained by expressing everything in terms of _θt_ and removing variable _x_ ˜ _t_ . To simplify notations, we further consider _θ_ as a matrix in R<sup>_n×d_</sup> (instead of a vector in R<sup>_nd_</sup> ), and so the communication update of Equation (12) is a standard gossip update with matrix _W_ , which we recall is such that _W ⊗ Id_ = [ _AP_ comm _A_<sup>_⊤_</sup> ]comm. We now discuss the local updates of Equation (13) more in details, which are closely related to dual-free SDCA updates [Shalev-Shwartz, 2016]. 

6 

**Algorithm 1** DVR( _z_ 0) 



## **3 Convergence Rate** 

The goal of this section is to set parameters _η_ and _α_ in order to get the best convergence guarantees. We introduce _κ_ comm = _γλ_ max( _A_<sup>_⊤_</sup> comm<sup>Σcomm</sup><sup>_A_comm)</sup><sup>_/λ_+</sup> min<sup>(</sup><sup>_A_</sup> comm<sup>_⊤D_</sup> _M_<sup>_−_1</sup><sup>_A_comm),where</sup><sup>_λ_</sup> min<sup>+and</sup><sup>_λ_max</sup> respectively refer to the smallest non-zero and the highest eigenvalue of the corresponding matrices. We denote _DM_ the diagonal matrix such that ( _DM_ ) _ii_ = _σi_ + _λ_ max(<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_LijPij_),where</sup><sup>_∇_2</sup><sup>_fij_(</sup><sup>_x_) ≼</sup> _LijPij_ for all _x ∈_ R<sup>_d_</sup> . Note that we use notation _κ_ comm since it corresponds to a condition number. In particular, _κ_ comm _≤ κs_ when _σi_ = _σj_ for all _i, j_ , and _κ_ comm more finely captures the interplay between regularity of local functions (through _DM_ and Σcomm) and the topology of the network (through _A_ ) otherwise. 

**Theorem 1.** _We choose p_ comm = �1 + _γ κ_<sup>_<u>m</u>_</sup> comm<sup><u>+</u></sup><sup>_<u>κs</u>_</sup> � _−_ 1 _, pij ∝_ (1 _− p_ comm)(1 + _Lij/σi_ ) _and α and η as in Algorithm 1. Then, there exists C_ 0 _>_ 0 _that only depends on θ_ 0 _(initial conditions) such that for all t >_ 0 _, the error and the expected time Tε required to reach precision ε are such that:_ 



_Proof sketch._ We have seen in Section 2 that DVR is obtained by applying Bregman coordinate descent on a well-chosen dual problem. Therefore, one of our key results consists in proving convergence rates for Bregman coordinate descent. In order to ease the reading of the paper, we present these results for a general setting in Appendix A, which is self-contained and which we believe to be of independent interest (beyond its application to decentralized optimization). 

Then, Appendix B focuses on the application to decentralized optimization. In particular, we recall the Equivalence between DVR and Bregman coordinate descent applied to the dual problem of Equation (4), and show that its structure is suited to the application of coordinate descent. Indeed, no two virtual edges adjacent to the same node are updated at the same time with our sampling. Then, we evaluate the relative smoothness and strong convexity constants of the augmented problem, 

7 

which allows to derive adequate values for parameters _α_ and _η_ . Finally, we choose _p_ comm in order to minimize the execution time of DVR. 

We would like to highlight the fact that the convergence theory of DVR decomposes nicely into several building blocks, and thus simple rates are obtained. This is not so usual for decentralized algorithms, for instance many follow-up papers were needed to obtain a tight convergence theory for EXTRA [Shi et al., 2015, Jakovetić, 2018, Xu et al., 2020, Li and Lin, 2020]. We now discuss the convergence rate of DVR more in details. 

**Computation complexity.** The computation complexity of DVR is the same computation complexity as locally running a stochastic algorithm with variance reduction at each node. This is not surprising since, as we argue later, DVR can be understood as a decentralized version of an algorithm that is closely related to dual-free SDCA [Shalev-Shwartz, 2016]. Therefore, this improves the computation complexity of EXTRA from _O_ ( _m_ ( _κb_ + _γ_<sup>_−_1</sup> )) individual gradients to _O_ ( _m_ + _κs_ ), which is the expected improvement for stochastic variance-reduced algorithm. In comparison, GT-SAGA [Xin et al., 2020], a recent decentralized stochastic algorithm, has a computation complexity of order _O_ ( _m_ + _κ_<sup>2</sup> _s_<sup>_/γ_2),whichissignificantlyworsethanthatofDVR,andgenerallyworsethanthatof</sup> EXTRA as well. 

**Communication complexity.** The communication complexity of DVR ( _i.e._ , the number of communications, so the communication time is retrieved by multiplying by _τ_ ) is of order _O_ ( _κ_ comm _/γ_ ), and can be improved to _O_ ( _κ_ comm _/_<sup>_√_</sup> _<u>γ</u>_ <u>)</u> using Chebyshev acceleration (see Section 4). Yet, this is in general worse than the _O_ ( _κb_ + _γ_<sup>_−_1</sup> ) communication complexity of EXTRA or NIDS, which can be interpreted as a partly accelerated communication complexity since the optimal dependence is _O_ ( ~~�~~ _κb/γ_ ) [Scaman et al., 2019], and 2 ~~�~~ _κb/γ_ = _κb_ + _γ_<sup>_−_1</sup> in the worst case ( _κb_ = _γ_<sup>_−_1</sup> ). Yet, stochastic updates are mainly intended to deal with cases in which the computation time dominates, and we show in the experimental section that DVR outperforms EXTRA and NIDS for a wide range of communication times _τ_ (the computation complexity dominates roughly as long as _τ < √γ_ <u>(</u> _m_ + _κs_ ) _/κ_ comm). Finally, the communication complexity of DVR is significantly lower than that of DSA and GT-SAGA, the primal decentralized stochastic alternatives presented in Section 1. **Homogeneous parameter choice.** In the homogeneous case ( _σi_ = _σj_ for all _i, j_ ), choosing the optimal _p_ comp and _p_ comm described above leads to _ηλ_ max( _W_ ) = _σp_ comm. Therefore, the communication update becomes _θt_ +1 = ( _I − W/λ_ max( _W_ )) _θt_ , which is a gossip update with a standard step-size (independent of the optimization parameters). Similarly, _αη_ ( _m_ + _κs_ ) = _p_ comp, and so the step-size for the computation updates is independent of the network. **Links with SDCA.** The single-machine version of Algorithm 1 ( _n_ = 1, _p_ comm = 0) is closely related to dual-free SDCA [Shalev-Shwartz, 2016]. The difference is in the stochastic gradient used: DVR uses _∇fij_ ( _zt_<sup>(</sup><sup>_ij_)</sup> ), where _zt_<sup>(</sup><sup>_ij_)</sup> is a convex combination of _θk_<sup>(</sup><sup>_i_)</sup> for _k < t_ , whereas dual-free SDCA uses _gt_<sup>(</sup><sup>_ij_)</sup> , which is a convex combination of _∇fij_ ( _θk_<sup>(</sup><sup>_i_))for</sup><sup>_k< t_.Bothalgorithmsobtainthesame</sup> rates. 

**Local synchrony.** Instead of using the synchronous communications of Algorithm 1, it is possible to update edges one at a time, as in Hendrikx et al. [2019b]. This can be very efficient in heterogeneous settings (both in terms of computation and communication times) and similar convergence results can be obtained using the same framework, and we leave the details for future work. 

8 

## **4 Acceleration** 

We show in this section how to modify DVR to improve the convergence rate of Theorem 1. 

**Network acceleration.** Algorithm 1 depends on _γ_<sup>_−_1</sup> , also called the _mixing time_ of the graph, which can be as high as _O_ ( _n_<sup>2</sup> ) for a chain of length _n_ [Mohar, 1997]. However, it is possible to improve this dependency to _γ_<sup>_−_1</sup><sup>_/_2</sup> by using Chebyshev acceleration, as in Scaman et al. [2017]. To do so, the first step is to choose a polynomial _P_ of degree _k_ and communicate with _P_ ( _W_ ) instead of _W_ . In terms of implementation, this comes down to performing _k_ communication rounds instead of one, but this makes the algorithm depend on the spectral gap of _P_ ( _W_ ). Then, the important fact is that there is a polynomial _Pγ_ of degree _⌈γ_<sup>_−_1</sup><sup>_/_2</sup> _⌉_ such that the spectral gap of _Pγ_ ( _W_ ) is of order 1. Each communication step with _Pγ_ ( _W_ ) only takes time _τ_ deg( _Pγ_ ) = _τ ⌈γ_<sup>_−_1</sup><sup>_/_2</sup> _⌉_ , and so the communication term in Theorem 1 can be replaced by _τκ_ comm _γ_<sup>_−_1</sup><sup>_/_2</sup> , thus leading to _network acceleration_ . The polynomial _Pγ_ can for example be chosen as a Chebyshev polynomial, and we refer the interested reader to Scaman et al. [2017] for more details. Finally, other polynomials yield even faster convergence when the graph topology is known [Berthier et al., 2020]. 

**Catalyst acceleration.** Catalyst [Lin et al., 2015a] is a generic framework that achieves acceleration by solving a sequence of subproblems. Because of space limitations, we only present the accelerated convergence rate without specifying the algorithm in the main text. Yet, only mild modifications to Algorithm 1 are required to obtain these rates, and the detailed derivations and proofs are presented in Appendix C. 

**Theorem 2.** _DVR can be accelerated using catalyst, so that the time Tε required to reach precision ε is equal (up to log factors) to Tε_ = _O_<sup>˜</sup> �� _m_ +<sup>_√_</sup> _<u>mκs</u>_ + _τ_ ~~�~~ _κ_ comm _/γ_ ~~�~~ _mκ_ comm _/κs_ <u>�</u> log _ε_<sup>_−_1�</sup> _._ 

This rate recovers the computation complexity of optimal finite sum algorithms such as ADFS [Hendrikx et al., 2019b, 2020]. Although the communication time is slightly increased (by a factor ~~�~~ _mκ_ comm _/κs_ ), ADFS uses a stronger oracle than DVR (proximal operator instead of gradient), which is why we develop DVR in the first place. Although both ADFS and DVR are derived using the same dual formulation, both the approach and the resulting algorithms are rather different: ADFS uses accelerated coordinate descent, and thus has strong convergence guarantees at the cost of requiring dual oracles. DVR uses coordinate descent with the Bregman divergence of _φij ∝ fij_<sup>_∗_inordertoworkwithprimaloracles,butthuslosesdirectacceleration,whichisrecovered</sup> through the Catalyst framework. Note that the parameters of accelerated DVR can also be set such that _Tε_ = _O_<sup>˜</sup> � _√κ_ comm � _m_ + _τ/_<sup>_√_</sup> _<u>γ</u>_ <u>�</u> log _ε_<sup>_−_1�</sup> , which recovers the convergence rate of optimal batch algorithms, but loses the finite-sum speedup. 

## **5 Experiments** 

We investigate in this section the practical performances of DVR. We solve a regularized logistic regression problem on the RCV1 dataset [Lewis et al., 2004] ( _d_ = 47236) with _n_ = 81 (leading to _m_ = 2430) and two different graph topologies: an Erdős-Rényi random graph (see, _e.g._ , [Bollobás, 2001]) and a grid. We choose _µ_<sup>2</sup> _kℓ_<sup>= 1</sup><sup>_/_2forallcommunicationedges,sothegossipmatrix</sup><sup>_W_isthe</sup> Laplacian of the graph. 

Figure 1 compares the performance of DVR with that of state-of-the-art primal algorithms such as EXTRA [Shi et al., 2015], NIDS [Li et al., 2019], GT-SAGA [Xin et al., 2020], and Catalyst accelerated versions of EXTRA [Li and Lin, 2020] and DVR. Suboptimality refers to _F_ ( _θt_<sup>(0))</sup><sup>_−F_(</sup><sup>_θ⋆_),</sup> 

9 



<!-- Start of picture text -->
10 0 10 0 EXTRA<br>10 2 DVR<br>10 3 10 3 NIDS<br>10 5 GTSAGA<br>10 6 10 6 Acc. EXTRA<br>10 9 10 8 10 9 Acc. DVR<br>10 12 10 11 10 12<br>0 1 2 3 4 0 2000 4000 6000 8000 0.00 0.25 0.50 0.75 1.00<br>Nb. of indiv. gradients 1e5 Nb. of co mm unications Time 1e7<br>(a) Erdős-Rényi, σ =  m ·  10 − 5<br>10 1 10 1 10 1<br>10 4 10 2 10 2<br>10 5 10 5<br>10 7<br>10 8 10 8<br>10 10 10 11 10 11<br>10 13 10 14 10 14<br>0.0 0.5 1.0 1.5 0.0 0.5 1.0 0 1 2 3<br>Time ( = 250) 1e6 Time ( = 250) 1e7 Time ( = 250) 1e7<br>(b) Grid, σ =  m ·  10 − 5 (c) Erdős-Rényi, σ =  m ·  10 − 7 (d) Grid, σ =  m ·  10 − 7<br>Suboptimality Suboptimality Suboptimality<br>Suboptimality Suboptimality Suboptimality<br><!-- End of picture text -->

Figure 1: Experimental results for the RCV1 dataset with different graphs of size _n_ = 81, with _m_ = 2430 samples per node, and with different regularization parameters. 

where node 0 is chosen arbitrarily and _F_ ( _θ_<sup>_⋆_</sup> ) is approximated by the minimal error over all iterations. Each subplot of Figure 1(a) shows the same run with different x axes. The left plot measures the complexity in terms of individual gradients ( _∇fij_ ) computed by each node whereas the center plot measures it in terms of communications (multiplications by _W_ ). All other plots are taken with respect to (simulated) time ( _i.e._ , computing _∇fij_ takes time 1 and multiplying by _W_ takes time _τ_ ) with _τ_ = 250 in order to report results that are independent of the computing cluster hardware and status. All parameters are chosen according to theory, except for the smoothness of the _fi_ , which requires finding the smallest eigenvalue of a _d × d_ matrix. For this, we start with _Lb_ = _σi_ +<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_Lij_</sup> (which is a known upper bound), and decrease it while convergence is ensured, leading to _κb_ = 0 _._ 01 _κs_ . The parameters for accelerated EXTRA are chosen as in Li and Lin [2020] since tuning the number of inner iterations does not significantly improve the results (at the cost of a high tuning effort). For accelerated DVR, we set the number of inner iterations to _N/p_ comp (one pass over the local dataset). We use Chebyshev acceleration for (accelerated) DVR but not for (accelerated) EXTRA since it is actually slower, as predicted by the theory. 

As expected from their theoretical iteration complexities, NIDS and EXTRA perform very similarly Li and Lin [2020], and GT-SAGA is the slowest method. Therefore, we only plot NIDS and GT-SAGA in Figure 1(a). We then see that though it requires more communications, DVR has a much lower computation complexity than EXTRA, which illustrates the benefits of stochastic methods. We see that DVR is faster overall if we choose _τ_ = 250, and both methods perform similarly for _τ ≈_ 1000, at which point communicating takes roughly as much time as computing a full local gradient. We then see that accelerated EXTRA has quite a lot of overhead and, despite 

10 

our tuning efforts, is slower than EXTRA when the regularization is rather high. On the other hand, accelerated DVR consistently outperforms DVR by a relatively large margin. The communication complexity is in particular greatly improved, allowing accelerated DVR to be the fastest method regardless of the setting. Further experimental results are given in Appendix D, and the code is available in supplementary material. 

## **6 Conclusion** 

This paper introduces DVR, a Decentralized stochastic algorithm with Variance Reduction obtained using Bregman block coordinate descent on a well-chosen dual formulation. Thanks to this approach, DVR inherits from the fast rates and simple theory of dual approaches without the computational burden of relying on dual oracles. Therefore, DVR has a drastically lower computational cost than standard primal decentralized algorithms, although sometimes at the cost of a slight increase in communication complexity. The framework used to derive DVR is rather general and could in particular be extended to analyze asynchronous algorithms. Finally, although deriving a direct acceleration of DVR is a challenging open problem, Catalyst and Chebyshev accelerations allow to significantly reduce DVR’s communication overhead both in theory and in practice. 

## **Acknowledgements** 

This work was funded in part by the French government under management of Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). We also acknowledge support from the European Research Council (grant SEQUOIA 724063) and from the MSR-INRIA joint centre. 

## **References** 

- Heinz H. Bauschke, Jérôme Bolte, and Marc Teboulle. A descent lemma beyond Lipschitz gradient continuity: first-order methods revisited and applications. _Mathematics of Operations Research_ , 42(2):330–348, 2017. 

- Raphaël Berthier, Francis Bach, and Pierre Gaillard. Accelerated gossip in networks of given dimension using jacobi polynomial iterations. _SIAM Journal on Mathematics of Data Science_ , 2 (1):24–47, 2020. 

- Béla Bollobás. _Random graphs_ . Number 73 in Cambridge studies in advanced mathematics. Cambridge University Press, 2001. 

- Léon Bottou. Large-scale machine learning with stochastic gradient descent. In _Proceedings of COMPSTAT_ , pages 177–186. Springer, 2010. 

- Stephen Boyd, Arpita Ghosh, Balaji Prabhakar, and Devavrat Shah. Randomized gossip algorithms. _IEEE Transactions on Information Theory_ , 52(6):2508–2530, 2006. 

- Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, and Jonathan Eckstein. Distributed optimization and statistical learning via the alternating direction method of multipliers. _Foundations and Trends_ R _⃝ in Machine learning_ , 3(1):1–122, 2011. 

11 

- Aaron Defazio, Francis Bach, and Simon Lacoste-Julien. SAGA: A fast incremental gradient method with support for non-strongly convex composite objectives. In _Advances in Neural Information Processing Systems_ , pages 1646–1654, 2014. 

- John C. Duchi, Alekh Agarwal, and Martin J. Wainwright. Dual averaging for distributed optimization: Convergence analysis and network scaling. _IEEE Transactions on Automatic Control_ , 57(3): 592–606, 2012. 

- Darina Dvinskikh and Alexander Gasnikov. Decentralized and parallelized primal and dual accelerated methods for stochastic convex programming problems. _arXiv preprint arXiv:1904.09015_ , 2019. 

- Hadrien Hendrikx, Francis Bach, and Laurent Massoulié. Accelerated decentralized optimization with local updates for smooth and strongly convex objectives. In _Artificial Intelligence and Statistics_ , 2019a. 

- Hadrien Hendrikx, Francis Bach, and Laurent Massoulié. An accelerated decentralized stochastic proximal algorithm for finite sums. In _Advances in Neural Information Processing Systems_ , 2019b. 

- Hadrien Hendrikx, Francis Bach, and Laurent Massoulié. An optimal algorithm for decentralized finite sum optimization. _arXiv preprint arXiv:2005.10675_ , 2020. 

- Dušan Jakovetić. A unification and generalization of exact distributed first-order methods. _IEEE Transactions on Signal and Information Processing over Networks_ , 5(1):31–46, 2018. 

- Dušan Jakovetić, José M. F. Moura, and Joao Xavier. Linear convergence rate of a class of distributed augmented Lagrangian algorithms. _IEEE Transactions on Automatic Control_ , 60(4):922–936, 2014. 

- Rie Johnson and Tong Zhang. Accelerating stochastic gradient descent using predictive variance reduction. In _Advances in Neural Information Processing Systems_ , pages 315–323, 2013. 

- Guanghui Lan and Yi Zhou. An optimal randomized incremental gradient method. _Mathematical Programming_ , pages 1–49, 2017. 

- David D Lewis, Yiming Yang, Tony G Rose, and Fan Li. Rcv1: A new benchmark collection for text categorization research. _Journal of machine learning research_ , 5(Apr):361–397, 2004. 

- Huan Li and Zhouchen Lin. Revisiting EXTRA for smooth distributed optimization. _arXiv preprint arXiv:2002.10110_ , 2020. 

- Huan Li, Cong Fang, Wotao Yin, and Zhouchen Lin. A sharp convergence rate analysis for distributed accelerated gradient methods. _arXiv preprint arXiv:1810.01053_ , 2018. 

- Zhi Li, Wei Shi, and Ming Yan. A decentralized proximal-gradient method with network independent step-sizes and separated convergence rates. _IEEE Transactions on Signal Processing_ , 67(17): 4494–4506, 2019. 

- Hongzhou Lin, Julien Mairal, and Zaid Harchaoui. A universal catalyst for first-order optimization. In _Advances in Neural Information Processing Systems_ , pages 3384–3392, 2015a. 

12 

- Hongzhou Lin, Julien Mairal, and Zaid Harchaoui. Catalyst acceleration for first-order convex optimization: from theory to practice. _Journal of Machine Learning Research_ , 18(1):7854–7907, 2017. 

- Qihang Lin, Zhaosong Lu, and Lin Xiao. An accelerated randomized proximal coordinate gradient method and its application to regularized empirical risk minimization. _SIAM Journal on Optimization_ , 25(4):2244–2273, 2015b. 

- Haihao Lu, Robert M. Freund, and Yurii Nesterov. Relatively smooth convex optimization by first-order methods, and applications. _SIAM Journal on Optimization_ , 28(1):333–354, 2018. 

- Bojan Mohar. Some applications of laplace eigenvalues of graphs. In _Graph Symmetry_ , pages 225–275. Springer, 1997. 

- Aryan Mokhtari and Alejandro Ribeiro. DSA: Decentralized double stochastic averaging gradient algorithm. _Journal of Machine Learning Research_ , 17(1):2165–2199, 2016. 

- Angelia Nedic and Asuman Ozdaglar. Distributed subgradient methods for multi-agent optimization. _IEEE Transactions on Automatic Control_ , 54(1):48–61, 2009. 

- Angelia Nedic, Alex Olshevsky, and Wei Shi. Achieving geometric convergence for distributed optimization over time-varying graphs. _SIAM Journal on Optimization_ , 27(4):2597–2633, 2017. 

- Yurii Nesterov. _Introductory Lectures on Convex Optimization: A Basic Course_ , volume 87. Springer Science & Business Media, 2013. 

- Kevin Scaman, Francis Bach, Sébastien Bubeck, Yin Tat Lee, and Laurent Massoulié. Optimal algorithms for smooth and strongly convex distributed optimization in networks. In _International Conference on Machine Learning_ , pages 3027–3036, 2017. 

- Kevin Scaman, Francis Bach, Sébastien Bubeck, Yin Lee, and Laurent Massoulié. Optimal convergence rates for convex distributed optimization in networks. _Journal of Machine Learning Research_ , 20:1–31, 2019. 

- Mark Schmidt, Nicolas Le Roux, and Francis Bach. Minimizing finite sums with the stochastic average gradient. _Mathematical Programming_ , 162(1-2):83–112, 2017. 

- Shai Shalev-Shwartz. SDCA without duality, regularization, and individual convexity. In _International Conference on Machine Learning_ , pages 747–754, 2016. 

- Shai Shalev-Shwartz and Tong Zhang. Stochastic dual coordinate ascent methods for regularized loss minimization. _Journal of Machine Learning Research_ , 14(Feb):567–599, 2013. 

- Zebang Shen, Aryan Mokhtari, Tengfei Zhou, Peilin Zhao, and Hui Qian. Towards more efficient stochastic decentralized learning: Faster convergence and sparse communication. In _International Conference on Machine Learning_ , pages 4631–4640, 2018. 

- Wei Shi, Qing Ling, Gang Wu, and Wotao Yin. Extra: An exact first-order algorithm for decentralized consensus optimization. _SIAM Journal on Optimization_ , 25(2):944–966, 2015. 

13 

- César A. Uribe, Soomin Lee, Alexander Gasnikov, and Angelia Nedić. A dual approach for optimal algorithms in distributed optimization over networks. _Optimization Methods and Software_ , pages 1–40, 2020. 

- Jialei Wang and Lin Xiao. Exploiting strong convexity from data with primal-dual first-order algorithms. In _International Conference on Machine Learning_ , pages 3694–3702, 2017. 

- Lin Xiao, Adams Wei Yu, Qihang Lin, and Weizhu Chen. DSCOVR: Randomized primal-dual block coordinate algorithms for asynchronous distributed optimization. _Journal of Machine Learning Research_ , 20(43):1–58, 2019. 

- Ran Xin, Soummya Kar, and Usman A Khan. Decentralized stochastic optimization and machine learning: A unified variance-reduction framework for robust performance and fast convergence. _IEEE Signal Processing Magazine_ , 37(3):102–113, 2020. 

- Jinming Xu, Ye Tian, Ying Sun, and Gesualdo Scutari. Distributed algorithms for composite optimization: Unified and tight convergence analysis. _arXiv preprint arXiv:2002.11534_ , 2020. 

14 

This appendix contains the details of the derivations and proofs from the main text. More specifically, Appendix A is a self-contained appendix that specifies the Bregman coordinate descent algorithm and proves its convergence rate. Appendix B focuses on the application of Bregman coordinate descent to the dual problem (relative smoothness and strong convexity constants, sparsity structure), and how to retrieve guarantees on the primal parameters. Appendix C is devoted to presenting the Catalyst acceleration of DVR and proving its convergence speed, and Appendix D details the experimental setting, along with more experiments. 

## **A Block Coordinate descent** 

We focus in this section on the general problem minimizing _f_ + _g_ using coordinate Bregman gradient, where _g_ is separable, _i.e._ , _g_ ( _x_ ) =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_gi_(</sup><sup>_x_(</sup><sup>_i_)).Thisisaself-containedsection,andnotationsmay</sup> differ from the rest of the paper. In particular, function _f_ is for now arbitrary and not related to _F_ or _fi_ from Problem (1), and the dimension _d_ is arbitrary as well. 

We first precise the blocks sampling rule. More specifically, we define a block _b ⊂{_ 1 _, . . . , d}_ as a collection of coordinates, and _B_ is the set of all blocks that can be chosen for the updates. Then, the algorithm updates each block _b ∈B_ with probability _p_ ( _b_ ), so that the probability of updating a given coordinate is given by _pi_ =<sup>�</sup> _i∈b_<sup>_p_(</sup><sup>_b_).Similarlytoindividualcoordinates,wewrite</sup><sup>_x_(</sup><sup>_b_)</sup> the restriction of _x_ to coordinates in _b_ . The Bregman coordinate gradient update for a block of coordinates _b_ writes: 



where _∇if_ denotes the gradient of _f_ in direction _i_ . Note that this update is more general than the one used to derive DVR, for which _g_ = 0. In order to derive strong guarantees for this block coordinate descent algorithm, we need to ensure that there is some separability in functions _f_ and _φ_ , and that the block structure is suited to this separability. All the assumptions about the separability structure of _f_ , _g_ and _φ_ are contained in the following assumption. 

**Assumption 1** (Separability) **.** _The function g is separable and the function φ is block-separable for b, meaning that for all b ∈B, there exist two convex functions φb and φ_<sup>_⊥_</sup> _b_<sup>_suchthatforallx,_</sup> 



_Besides, for all b ∈B, either of the following two hold:_ 





_2. pi_ = _pj for all i, j ∈ b._ 

If _φ_ is not block-separable, the support of the Bregman update in direction _b_ may not restricted to _b_ . This causes some of the derivations below to fail, which is why we prevent it by assuming that Equation (16) holds. 

15 

Then, the first option ensures that within a block, the updates do not affect each other. The function _f_ is not separable, but some directions can be updated independently from others. To have these independent updates, we also need to assume further separability of _φ_ within the blocks. The second option states that if only block-separability of _φ_ is assumed then within each block for which _φ_ and _f_ are not separable, coordinates must be picked with the same probability. 

Assumption 1 is a bit technical but we actually require all statements in order to derive DVR. In particular, the first option is verified when updating within the same block virtual edges that are adjacent to different nodes in the dual problem. The second option is verified when picking all communication edges at once within the same block. 

Now that we have made assumptions on the structure of _f_ , _g_ and _φ_ , we will make assumptions on their regularity. We start by a directional relative smoothness assumption between _f_ and _φ_ , _i.e._ , we assume that for all _i_ , there exists _L_<sup>_i_</sup> rel<sup>suchthatforall</sup><sup>_δ>_0and</sup><sup>_ei_theunitvectorofdirection</sup><sup>_i_,</sup> 



Similarly, for _σ_ rel _>_ 0, _f_ is said to be _σ_ rel-strongly convex relatively to _φ_ if for all _x, y_ : 



We finally assume that _f_ and _φ_ are convex (but not necessarily smooth). We can now state the central theorem of this section: 

**Theorem 3.** _Let f and φ be such that f is L_<sup>_i_</sup> rel<sup>_-smoothindirectioniandσ_rel</sup><sup>_-stronglyconvex_</sup> _relatively to φ. Denote p_ min = min _i pi, and_ 



_Then, if the blocks B respect Assumption 1 (separability) and ηtL_<sup>_i_</sup> rel<sup>_<piforalli,theBregman_</sup> _coordinate descent algorithm guarantees for all x:_ 



_The same result holds with L_<sup>_′_</sup> _t_<sup>=</sup><sup>_Dφ_(</sup><sup>_x, xt_) +</sup> _L_<sup><u>max</u></sup> rel1 ( _F_ ( _xt_ ) _− F_ ( _x_ )) _, where L_<sup>max</sup> rel = max _i L_<sup>_i_</sup> rel<sup>_._</sup> 

To prove this theorem, we start by proving the monotonicity of such iterations. 

**Lemma 1** (Monotonicity) **.** _We note δi_ = _e_<sup>_⊤_</sup> _i_<sup>(</sup><sup>_xt_+1</sup><sup>_−xt_)</sup><sup>_ei.Ifxt_+1= arg min</sup><sup>_x V_</sup> _t_<sup>_b_(</sup><sup>_x_)</sup><sup>_then:_</sup> _1. If φ and f are separable for b then for all i ∈ b, if ηtL_<sup>_i_</sup> rel<sup>_≤pithenF_(</sup><sup>_xt_)</sup><sup>_≥F_(</sup><sup>_xt_+</sup><sup>_δi_)</sup><sup>_._</sup> _2. If pi_ = _pj for all i, j ∈ b and ηtL_<sup>_b_</sup> rel<sup>_≤pbthenF_(</sup><sup>_xt_)</sup><sup>_≥F_(</sup><sup>_xt_+1)</sup><sup>_._</sup> 

_Proof._ We start by the first point. If _φ_ is separable for _b_ then this means that each coordinate is updated independently. By definition of _x_<sup>(</sup> _t_ +1<sup>_i_),wehave</sup><sup>_V_</sup> _t_<sup>_b_(</sup><sup>_x_(</sup> _t_ +1<sup>_b_))</sup><sup>_≤V_</sup> _t_<sup>_b_(</sup><sup>_xt_).Thiswrites,splitting</sup> 

16 

over each _i_ and using the fact that _Dφi_ ( _xt, xt_ ) = 0: 



The result follows from summing over all _i ∈ b_ , and using Assumption 1. For the second point, it is not possible to split the update per coordinate since _φ_ is not separable. Yet, we can still write (using separability of _g_ ): 



Since _g_ is separable and _pi_ = _pb_ for all _i ∈ b_ , Equation (19) writes: 



Note that this crucially relies on _xt_ +1 _− xt_ having support on _b_ , which is enforced by the blockseparability of _φ_ . Then, the proof is similar to that of the first point, using that _ηtL_<sup>_b_</sup> rel<sup>_≤pb_.</sup> 

Using this monotonicity result allows us to prove Theorem 3. 

_Proof of Theorem 3._ First note that by convexity of all _gi_ , 



Therefore, we have _DVtb_<sup>(</sup><sup>_x, y_)</sup><sup>_≥Dφ_(</sup><sup>_x, y_)forall</sup><sup>_x, y∈_R</sup><sup>_d_.Applyingthiswith</sup><sup>_y_=</sup><sup>_xt_+1yields:</sup> 



Then, _∇Vt_<sup>_b_(</sup><sup>_xt_+1) = 0bydefinitionof</sup><sup>_xt_+1,soEquation(21)writes:</sup> 



We first consider that the first option of Assumption 1 holds, _i.e._ , that _f_ and _φ_ are separable in _b_ . We note _δi_ = _e_<sup>_⊤_</sup> _i_<sup>(</sup><sup>_xt_+1</sup><sup>_−xt_)</sup><sup>_ei_,sothat:</sup> 



17 

Therefore, if _ηtL_<sup>_i_</sup> rel<sup>_≤pi_forall</sup><sup>_i ∈b_,</sup> 



The _gi_ ( _x_<sup>(</sup> _t_ +1<sup>_i_))</sup><sup>_−gi_(</sup><sup>_x_(</sup><sup>_i_)) term can be replaced by</sup><sup>_g_(</sup><sup>_xt_+</sup><sup>_δi_)</sup><sup>_−g_(</sup><sup>_xt_)+</sup><sup>_gi_(</sup><sup>_x_</sup> _t_<sup>(</sup><sup>_i_))</sup><sup>_−gi_(</sup><sup>_x_(</sup><sup>_i_)) since</sup><sup>_gj_(</sup><sup>_xt_+1) =</sup> _gj_ ( _xt_ ) for _j̸_ = _i_ . Therefore, we obtain: 



The separability of _F_ in _b_ and its monotonicity lead to, using the fact that _xt_ +1 = _xt_ +<sup>�</sup> _i∈b_<sup>_δi_:</sup> 



Therefore, if the first option of Assumption 1 holds, we obtain: 

If the second option holds, _i.e._ , _pi_ = _p_ for all _i ∈ b_ , then 



and Equation (23) can be obtained through similar derivations (at the block-level). Using the separability of _g_ , we obtain that 



Then, since E �� _i∈b p_ <u>1</u> _i_<sup>_∇if_(</sup><sup>_xt_)</sup> � =<sup>�</sup> _i_<sup>_p−_</sup> _i_<sup>1</sup> � _b_ : _i∈b_<sup>_p_(</sup><sup>_b_)</sup><sup>_∇if_(</sup><sup>_xt_)=</sup><sup>_∇f_(</sup><sup>_xt_),andtherelativestrong</sup> convexity assumption yields: 



18 

Therefore, taking the expectation of Equation (22) yields: 



We obtain after some rewriting: 



Finally, _σ_ rel _≤ L_<sup>_i_</sup> rel<sup>so</sup><sup>_ηtσ_rel</sup><sup>_≤ηtLi_</sup> rel<sup>_≤pi_forall</sup><sup>_i_,andinparticular1</sup><sup>_−p_min</sup><sup>_≤_1</sup><sup>_−ηtσ_rel,which</sup> yields the desired result. The result on _L_<sup>_′_</sup> _t_<sup>isbeobtainedbybounding</sup><sup>_η/p_minby</sup><sup>_L_max</sup> rel = max _i L_<sup>_i_</sup> rel<sup>andremarkingthat</sup> 1 _− ηtL_<sup>max</sup> rel _≤_ 1 _− ηtσ_ rel since _L_<sup>max</sup> rel _≥ σ_ rel. 

## **B Convergence results for DVR** 

We now give a series of small results, that justify our approach. We start by showing the applicability of Theorem 3 to Problem (4), and the associated constants. Finally, we show how to obtain rates for the primal iterates _θt_ . 

### **B.1 Application to the dual of the augmented problem** 

In this section, we note _f_ sum<sup>_∗_= �</sup><sup>_n_</sup> _i_ =1 � _mj_ =1<sup>_f_</sup> _ij_<sup>_∗_,sothatProblem4writes:</sup> min _x,y_<sup>_qA_(</sup><sup>_x, y_) +</sup><sup>_f_</sup> sum<sup>_∗_(</sup><sup>_y_)</sup> (24) 

**Lemma 2.** _The iterations of Algorithm 1 are equivalent to the iteration of Equations_ (15) _applied to Problem_ (4) _with g_ = 0 _and φ_ ( _x, y_ ) = _φ_ comm( _x_ ) +<sup>�</sup><sup>_n_</sup> _i_ =1 � _mj_ =1<sup>_φij_(</sup><sup>_y_(</sup><sup>_ij_))</sup><sup>_,withφ_comm(</sup><sup>_x_) =</sup> 2<sup><u>1</u></sup><sup>_∥x∥_2</sup> _A_<sup>_†_</sup> _A for coordinates associated with communication edges, and φij_ ( _y_<sup>(</sup><sup>_ij_)</sup> ) =<sup>_L_</sup> _µ_<sup>2</sup> _ij_<sup>_ijf_</sup> _ij_<sup>_∗_(</sup><sup>_µijyij_)</sup><sup>_forcoordinates_</sup> _associated with computation edges._ 

_Proof._ This result follows from the dual-free and implementation-friendly derivations presented in the previous section. 





_3. qA_ + _f_ sum<sup>_∗is(Lij_</sup> rel<sup>_)-smoothrelativelytoφinthedirectionofvirtualedge_(</sup><sup>_i, j_)</sup><sup>_,with_</sup> 





_Proof._ First note that _∇_<sup>2</sup> _f_ sum<sup>_∗_isablock-diagonalmatrix,andits</sup><sup>_ij_-thblockisequalto</sup> 



where _uij ∈_ R<sup>_n_(1+</sup><sup>_m_)</sup> denotes the unit vector corresponding to virtual _node_ ( _i, j_ ). We denote ˜Σ = Σ +<sup>�</sup><sup>_n_</sup> _i_ =1 � _mj_ =1 _L_ <u>1</u> _ij_<sup>(</sup><sup>_uiju_</sup> _ij_<sup>_⊤_)</sup><sup>_⊗Id_.Then,</sup> 



**Relative strong convexity.** Then, Hendrikx et al. [2020, Lemma 6.5] leads to _A_<sup>_⊤_</sup> Σ<sup>˜</sup> _A_ ≽ _σF A_<sup>_†_</sup> _A_ . Note that the notations are slightly different, and the matrix Σ<sup>˜</sup> in this paper is the same as the matrix Σ<sup>_†_</sup> in Hendrikx et al. [2020]. Then, remark that ( _A_<sup>_†_</sup> _A_ ) _ij_ = _Pij_ = _µ_ <u>1</u><sup>2</sup> _ij_<sup>(</sup><sup>_A⊤_[(</sup><sup>_uiju_</sup> _ij_<sup>_⊤_)</sup><sup>_⊗Pij_]</sup><sup>_A_)</sup><sup>_ij_,</sup> and _φij_ = _α_<sup>_−_1</sup> _fij_<sup>_∗_,sothat:</sup> 



Finally, using that Equation (25) along with the fact that _σF ≤ α_ implies that _qA_ + _f_ sum<sup>_∗_is</sup> _σF_ -relatively strongly convex with respect to _φ_ . 

**Relative smoothness.** We first prove the relative smoothness property for communicate edges. For any _x_ ˜ _∈ R_<sup>_Ed_</sup> , Equation (26) leads to: 



Similarly, for any _θ ∈_ R<sup>_d_</sup> , we consider _y_ ˜ = _eij ⊗ θ_ and write: 

with 



Finally, _∇_<sup>2</sup> _fij_<sup>_∗_(</sup><sup>_µijy_(</sup><sup>_ij_))≽</sup><sup>_Pij/Lij_,and</sup><sup>_α≤L_</sup> rel<sup>_i_,whichendstheproofofthedirectionalrelative</sup> smoothness result. 

**Lemma 4.** _Assumption 1 holds with f_ = _qA_ + _f_ sum<sup>_∗,g_=0</sup><sup>_,andφasinLemma2,andwhenthe_</sup> _sampling is such that either:_ 

- _All communication edges are sampled at once, or_ 

20 

_• Each node samples exactly one virtual edge._ 

_Proof._ First of all, _g_ = 0 is separable, and _φ_ is separable with respect to the communication and computation blocks by construction. 

We note _b_ comm the block of all communication edges, which is sampled with probability _p_ comm. All communication edges are sampled at the same time, so _pi_ = _p_ comm for all _i ∈ b_ comm and so _φ_ respects option 2 for the communication block. 

Let us now consider a computation block _b_ . First of all, _φ_ is separable for the virtual edges. Then, virtual blocks contain exactly one virtual edge per node, and so _b_ = _{_ (1 _, j_ 1) _, · · · ,_ ( _n, jn_ ) _}_ . Let _k̸_ = _ℓ_ , then 



Therefore, 



Finally, _f_ sum<sup>_∗_isseparable,andso</sup><sup>_qA_+</sup><sup>_f_</sup> sum<sup>_∗_respectsoption2.</sup> 

We can now prove the main theorem on the convergence rate of DVR. 

**Theorem 4.** _We choose p_ comm = �1 + _γ κ_<sup>_<u>m</u>_</sup> comm<sup><u>+</u></sup><sup>_<u>κs</u>_</sup> � _−_ 1 _and pij ∝_ (1 _− p_ comm)(1 + _Lij/σi_ ) _. Then, for all θ_ 0 _∈_ R<sup>_n×d_</sup> _and all t >_ 0 _, the error is such that:_ 



_with p_ min = min( _p_ comm _,_ min _ij pij_ ) _, λt_ = ( _xt, yt_ ) _and D_ = _−_ ( _qA_ + _f_ sum<sup>_∗_)</sup><sup>_.Therefore,theexpectedtime_</sup> _Tε required to reach precision ε is equal to:_ 



_Proof._ Using Lemmas 4 and 3, we apply Theorem 3 (convergence of Bregman coordinate gradient de. scent), and obtain that the convergence rate is _ηtα/_ 2, with _ηt ≤_ min _ij pij/L_<sup>_i_</sup> rel<sup>and</sup><sup>_ηt≤p_comm</sup><sup>_/L_comm</sup> rel Therefore, for communication edges, we have that 



For computation edges, we know that _pij_ = _p_ comm(1 + _Lij/σi_ ) _/_ (<sup>�</sup><sup>_m_</sup> _j_ =1<sup>(1 +</sup><sup>_Lij/σi_)),andso</sup> 



21 

with _κs ≥ σi_<sup>_−_1</sup> � _mj_ =1<sup>_Lij_forall</sup><sup>_i_.</sup> 

In the end, we would like these two bounds to be equal, so we choose _p_ comp and _p_ comm such that 



Yet, we also know that _p_ comm = 1 _− p_ comp, so 



Equivalently, this corresponds to taking 



With this choice, one can verify that _ηt_ verifies both _ηtα ≤_ 2 _p_ comm and _ηtα ≤_ 2 min _ij pij_ , so the rate is: 



The expected execution time to reach precision _ε_ , denoted _Tε_ , is equal to _Tε_ = _ρ_<sup>_−_1</sup> ( _p_ comp + _τp_ comm) _Kε_ with _Kε_ such that _C_ (1 _− ηtα/_ 2)<sup>_Kε_</sup> _< ε_ for some constant _C_ , and so: 



### **B.2 Primal guarantees** 

The goal of this section is to recover primal guarantees from dual guarantees. Although the initial setting is inspired from Lin et al. [2015b], the proof is different, and in particular does not require smoothness of the _fij_<sup>_∗_oranextraproximalstep.Wedefinefor</sup><sup>_β≥_0theLagrangianfunction:</sup> 



The dual problem _D_ ( _λ_ ) is defined as 



Given an approximate dual solution _λk_ , we can get an approximate primal solution _θk_ = arg min _θ L_ ( _λk, θ_ ), which is obtained as: 



22 

Note that _θt_<sup>(</sup><sup>_ij_)</sup> corresponds to the _zt_<sup>(</sup><sup>_ij_)</sup> from Algorithm 1. We chose to use a different notation in the main text to emphasize on the fact that these are the parameters for the virtual nodes, but _zt_<sup>(</sup><sup>_ij_)</sup> actually converge to the solution as well. Similarly, _λt_ corresponds to ( _xt, yt_ ) the concatenation of the parameters for communication and virtual edges from Section 2. The last difference is that the Lagrangian defined in Equation (28) actually corresponds to a Lagrangian associated to a perturbed version of Problem (1) in which _f_<sup>˜</sup> _i_ ( _θ_ ) = _fi_ ( _θ_ ) +<sup>_<u>β</u>_</sup> 2<sup>_∥θ −ω_(</sup><sup>_i_)</sup><sup>_∥_2.Thesolutiontotheinitialproblem</sup> can be retrieved by taking _β_ = 0, but this more general formulation enables us to derive results that also holds for the inner problems solved by the Catalyst accelerated version of DVR. 



= <u>1</u> _Proof._ Using the fact that _θt_<sup>(</sup><sup>_i_)</sup> _σi_ + _β_<sup>((</sup><sup>_Aλt_)(</sup><sup>_i_) +</sup><sup>_ω_</sup> _t_<sup>(</sup><sup>_i_))(andsimilarlyfor</sup><sup>_θ⋆_),whereΣ</sup><sup>_β_istheblock</sup> diagonal matrix such that (Σ _β_ ) _ii_ = ( _σi_ + _β_ )<sup>_−_1</sup> _Id_ , we obtain: 



Using the min(( _σ_ max + _β_ )<sup>_−_1</sup> _, L_<sup>_−_</sup> _ij_<sup>1)-strongconvexityof</sup><sup>_θ�→_</sup> 2<sup><u>1</u></sup><sup>_x⊤_Σ</sup><sup>_βx_+ �</sup> _i,j_<sup>_f_</sup> _ij_<sup>_∗_(</sup><sup>_x_(</sup><sup>_ij_)),weobtain:</sup> 



Then, we add _p_ min _ηt_<sup>_−_1</sup><sup>_Dφ_(</sup><sup>_λ⋆, λt_)</sup><sup>_≥_0andapplyTheorem4,whichyields</sup> 



Then, Theorem 1 is a direct consequence of Theorem 4 and Lemma 5. 

## **C Catalyst acceleration** 

We show in this Section how to apply Catalyst acceleration to DVR, and prove the convergence speed in this case. 

23 

### **C.1 Derivation and rates** 

In the main text, we derived DVR to solve regularized finite sum problems. Although not so different, the subproblem obtained with Catalyst is not in the form of Problem (1), and some adjustments need to be made. More specifically, we would like to solve problems of the form: 



An easy way to adapt the algorithm is to consider the extra ( _β/_ 2) _∥θ − ωt_<sup>(</sup><sup>_i_)</sup><sup>_∥_2asjustanother</sup> component of the sum. Yet, the point of this extra term is to make the problem easier to solve by adding strong convexity. This would not be the case if this term were is treated as just another term in the sum. Therefore, we want to include it with the quadratic term. We define: 



then _h_<sup>_∗_</sup> ( _x_ ) = 2( _β_ <u>1+</u> _σ_ )<sup>_∥x_+</sup><sup>_βω_</sup> _t_<sup>(</sup><sup>_i_)</sup><sup>_∥_2</sup><sup>_−_</sup><sup>_<u>β</u>_</sup> 2<sup>_∥ω_</sup> _t_<sup>(</sup><sup>_i_)</sup><sup>_∥_2.Therefore,Problem(4)becomes:</sup> 



with (Σ _β_ ) _ii_ = ( _σi_ + _β_ )<sup>_−_1</sup> for _i ∈{_ 1 _, . . . , n}_ . The linear term does not affect the Hessians, and thus the convergence rate is the same as before, with _σ_ replaced by _σ_ + _β_ . In terms of algorithms, we just need to modify the gradient term, and obtain Algorithm 2. The only term that changes is _∇qA_ ( _x, y_ ), to which an extra _β_ Σ _βωt_ term is added. Therefore, the updates to _θt_ and _zt_ remain unchanged, and only the initial expression of _θt_ requires some adjustments since we now have that (as written in Equation 30): 



If we only consider 1 inner loop then the only thing that changes is the initial condition. If we consider several outer loops, then the we must choose the new parameter as _θ_ 0<sup>_t_+1</sup> = _θT_<sup>_t_+Σ</sup><sup>_β_(</sup><sup>_ωt_+1</sup><sup>_−ωt_)</sup> in order to maintain the invariant, but a remarkable fact is that the inner iterations remain the same, with the only exception that Σ is replaced by Σ _β_ . Note that it is possible to warm-start the _zt_ +1 _,_ 0 as well, but this requires updating _θt,_ 0 accordingly with _∇fij_ ( _zt,_<sup>(</sup><sup>_ij_</sup> 0<sup>)),whichrequiresafullpass</sup> over the local dataset. We therefore choose not to do it. 

However, it is not obvious that Algorithm 2 corresponds to a genuine Catalyst acceleration yet. Indeed, Catalyst acceleration requires having a feasible _εt_ -approximations for the primal problem, _i.e._ , points _θt ∈_ R<sup>_d_</sup> such that _Ft_ ( _θt_ ) _−_ min _θ F_ ( _θ_ ) _≤ εt_ . In our case, we only have dual guarantees and approximate feasibility. We know that the parameters converge to consensus, but they do not reach it at any time. This is a problem because it is then not possible to adequately define _Ft_ +1 based on the local approximations of the solutions of _Ft_ . Yet, following the approach of Li and Lin [2020], we note that 



24 

**Algorithm 2** Accelerated DVR( _z_ 0) 1: _α_ = 2 _λ_<sup>+</sup> min<sup>(</sup><sup>_A_</sup> comm<sup>_⊤D_</sup> _M_<sup>_−_1</sup><sup>_A_comm),</sup><sup>_η_= min</sup> <u>�</u> _λ_ max( _A_<sup>_⊤_</sup> comm _<u>p</u>_ <u>comm</u><sup>Σ</sup> _β,_ comm<sup>_A_comm)</sup><sup>_,_</sup> _α_ (1+ _σpii_<sup>_−_</sup> _<u>j</u>_<sup>1</sup> _Lij_ ) <u>�</u> 2: _q_ = _σ_ min _<u>σ</u>_ <u>min+</u> _β_ // _Initialization_ 3: _ω_ 0<sup>(</sup><sup>_i_)</sup> = _− σi_ <u>1+</u> _β_ � _mj_ =1<sup>_∇fij_(</sup><sup>_z_</sup> 0<sup>(</sup><sup>_ij_)</sup> ), _θ_ 0<sup>(</sup><sup>_i_)</sup> = �1 + _σiβ_ + _β_ � _ω_ 0<sup>(</sup><sup>_i_).</sup> // _z_ 0 _is arbitrary but not θ_ 0 _._ 4: **for** _t_ = 0 to _T −_ 1 **do** // _T outer loops_ 5: **for** _k_ = 0 to _K −_ 1 **do** // _Inner loop runs for K iterations_ 6: _zt,k_ +1 = _zt,k_ . 7: Sample _ut_ uniformly in [0 _,_ 1]. // _Randomly decide the kind of update_ 8: **if** _ut ≤ p_ comm **then** 9: _θt,k_ +1 = _θt,k − p_ comm _<u>ηt</u>_<sup>Σ</sup><sup>_βWθt,k_</sup> // _Communication using W_ 10: **else** 11: **for** _i_ = 1 to _n_ **do** 12: Sample _j ∈{_ 1 _, · · · , m}_ with probability _pij_ . 13: _zt,k_<sup>(</sup><sup>_ij_</sup> +1<sup>)=</sup> �1 _− p_ comp _αη_ <u>�</u> _zt,k_<sup>(</sup><sup>_ij_)+</sup> _p_ comp _αη_<sup>_θ_</sup> _t,k_<sup>(</sup><sup>_i_)</sup> // _Computing new virtual node parameter_ <u>1</u> 14: _θt,k_<sup>(</sup><sup>_i_)</sup> +1<sup>=</sup><sup>_θ_</sup> _t,k_<sup>(</sup><sup>_i_)</sup><sup>_−_</sup> _σi_ + _β_ � _∇fij_ ( _zt,k_<sup>(</sup><sup>_ij_</sup> +1<sup>))</sup><sup>_−∇fij_(</sup><sup>_z_</sup> _t,k_<sup>(</sup><sup>_ij_))</sup> � // _Local update using fij_ _<u>q</u>_ 15: _ωt_ +1 = _θt,K_ +<sup>1</sup> 1+<sup>_−√_</sup><sup>_~~√~~_</sup> _<u>q</u>_<sup>(</sup><sup>_θt,K−θt−_1</sup><sup>_,K_)</sup> _<u>β</u>_ 16: _θt_ +1 _,_ 0 = _θt,K_ + _β_ + _σi_<sup>(</sup><sup>_ωt_+1</sup><sup>_−ωt_)</sup> 17: _zt_ +1 _,_ 0 = _zt,K_ 18: **return** _θT_ 

where _ω_ ¯ _t_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_ω_</sup> _t_<sup>(</sup><sup>_i_).Thismeansthatalthough</sup><sup>_Ft_isonlydefinedwiththelocalvariables</sup><sup>_ω_</sup> _t_<sup>(</sup><sup>_i_),</sup> _solving Ft is equivalent to solving a problem involving ω_ ¯ _t only_ . Besides, the Catalyst iterations are linear, meaning that performing the extrapolation step on _θ_<sup>¯</sup> _t_ is equivalent to performing it on each _θt_<sup>(</sup><sup>_i_)</sup> individually. Therefore, although Catalyst is implemented in a fully decentralized manner (each node knowing only its own parameter), it is conceptually applied to a mean parameter _θ_<sup>¯</sup> _t_ (that is never explicitly computed). In the following, we thus analyze the performances of the following algorithm: 



where we recall that _q_ = _σ_ min _/_ ( _σ_ min + _β_ ). Recall that the inner problem is approximated using DVR and the means do not need to be computed explicitly. Let _κ_<sup>_β_</sup> _s_<sup>= max</sup> _i_<sup>1 + (�</sup><sup>_m_</sup> _j_ =1<sup>_Lij_)</sup><sup>_/_(</sup><sup>_β_+</sup><sup>_σi_),</sup> and _κ_<sup>_β_</sup> comm<sup>beobtainedsimilarlyto</sup><sup>_κ_</sup> comm<sup>butreplacingΣbyΣ</sup> _β_<sup>.Weconsiderinthissectionthat</sup> _σi_ = _σ_ for all _i ∈{_ 1 _, . . . , n}_ in order to simplify exposition, but the results hold more generally. Note that _α_ and _η_ have slightly different expressions than in the main text since _β_ is now involved in their definitions. We define the sequence _εt_ which is such that: 



We then prove the following theorem: 

25 

**Theorem 5.** _Consider Algorithm 2 with p_ comm = �1+ _γ κ_<sup>_<u>mβ</u>_</sup> comm<sup><u>+</u></sup><sup>_<u>κ</u>_</sup> _<u>s</u>_<sup>_β_</sup> � _−_ 1 _, pij ∝_ (1 _−p_ comm)(1+ _Lij/_ ( _σi_ + _β_ )) _. If K_ = _O_<sup>˜</sup> (1 _/_ ( _ηtα_ )) _then for all t ≤ T , Ft_ ( _θ_<sup>¯</sup> _t_ ) _− Ft_ ( _θt_<sup>_⋆_)</sup><sup>_≤εtand_</sup> 



Note that the error is on the mean parameter, and we also want _θt_<sup>(</sup><sup>_i_)</sup> to be close to _θ_<sup>¯</sup> _t_ for all _i_ . This is ensured by Lemma 5. Before we start the proof of Theorem 5, we show that Theorem 2 is a corollary of Theorem 5. 

_Proof of Theorem 2._ Using the same argument as in Theorem 1, we obtain that each inner loop takes time 



in expectation, so the total number of inner iterations is of order: 



Therefore, we see that if we choose _β_ + _σ_ = _L_ comm then, taking into account the fact that _κs ≤ mκ_ comm, the algorithm takes time: 



Therefore, using Chebyshev acceleration allows to recover the rate of optimal batch algorithms (up to log factors). On the other hand, if we choose _β_ = _Ls/m − σ_ then if _β ≥_ 0 ( _i.e._ , _κs ≥ m_ ), the time to convergence is equal to: 



This can be rewritten as: 



Therefore, we obtain the optimal<sup>_√_</sup> _<u>mκs</u>_ computation complexity in this case, with a slightly suboptimal communication complexity due to the ~~�~~ _mκ_ comm _/κs_ term. When this term is equal to 1 then<sup>_√_</sup> _<u>mκs</u>_ = _m_<sup>_√_</sup> _<u>κb</u>_ and so nothing is gained from using a stochastic algorithm. Otherwise, this allows to trade-off communications for computations. 

The proof of Theorem 5 is obtained in several steps, that we emphasize below: 

1. Equivalent decentralized implementation of Catalyst. 

2. Bounding the primal suboptimality as _Ft_ ( _θ_<sup>¯</sup> _t_ ) _−_ min _θ Ft_ ( _θ_ ) _≤_ (1 _−_ ( _ηα_ ) _/_ 2)<sup>_k_</sup> _D_ 0<sup>_t_,with</sup><sup>_k_the</sup> number of inner iterations and _D_ 0<sup>_t_a dual error.This quantifies how precisely the inner problem</sup> is solved. 

26 

3. Evaluating the initial dual suboptimality _D_ 0<sup>_t_,whichdependson</sup><sup>_θt−_1(anditsassociateddual</sup> parameter _λt−_ 1). This quantifies how good _θ_<sup>¯</sup> _t−_ 1 already is as a solution to _Ft_ . 

In the end, this allows us to use the catalyst general results with primal criterion, and with simple warm-start scheme (warm-start on the last iterate of the last outer iteration). The first point is presented at the beginnning of this section and the second one is adressed by Lemma 5. The following section deals the last point. 

### **C.2 Proof of Theorem 5** 

We now show a bound on the initial error of an inner loop when warm-starting on the last iterate of the previous inner loop. Indeed, the convergence results for DVR depend on the initial dual error and so results from [Lin et al., 2017] cannot be used directly. Yet, it can be adapted, as we show in this section. We note _Dt_ ( _λ_ ) the dual function at outer step _t_ (which should not be mistaken with the Bregman divergence _Dφ_ ), and _λ⋆_<sup>_t_itsminimizer.Similarly,wenote</sup><sup>_θ_</sup> _⋆_<sup>_t_=arg min</sup><sup>_θFt_(</sup><sup>_θ_),</sup> whereas _θ_<sup>_⋆_</sup> is the global minimizer of _F_ . The following theorem ensures convergence of _θ_<sup>¯</sup> _t_ to the true optimum, given that the subproblems are solved precisely enough. 

**Theorem 6.** _[Lin et al., 2017, Proposition 5]. If Fk_ ( _θ_<sup>¯</sup> _k_ ) _− Fk_ ( _θ⋆_<sup>_k_)</sup><sup>_≤εkforallk≤tthen_</sup> 



Therefore, our goal is to prove that _Ft_ ( _θ_<sup>¯</sup> _t_ +1) _− Ft_ ( _θ⋆_<sup>_t_)</sup><sup>_≤εt_forall</sup><sup>_t_.Thesmoothnessof</sup><sup>_Ft_ensures</sup> that this is achieved if 



Yet, using Lemma 5, we know that, since _θt_<sup>(</sup> +1<sup>_i_)isobtainedbyapplying</sup><sup>_K_stepsofDVRto</sup><sup>_Ft_starting</sup> from _λ_<sup>_t_</sup> 0<sup>.</sup> 



Unfortunately, we have no control over the dual error at this point. In the remainder of this section, we prove by recursion that Equation (40) holds for all _t_ . More specifically, we start by assuming that: 





where _C_ 1 and _C_ 2 are such that the conditions are verified for _t_ = _−_ 1, with _D−_ 1 = _D_ 0, _θ⋆_<sup>_−_1</sup> = _θ⋆_<sup>0,</sup> and _λ_<sup>_−_</sup> _⋆_<sup>1</sup> = _λ_<sup>0</sup> _⋆_<sup>.Equation(41)maynotholdfor</sup><sup>_t_=</sup><sup>_−_1,butmakingitholdattime</sup><sup>_t_=0would</sup> only require a slightly longer first inner iteration, meaning at most an extra log factor. Therefore 

27 

we assume without loss of generality that it is the case, since the final complexities are given up to logarithmic factors. The rest of this section is devoted to showing that if _K_ is chosen as in Theorem 5 then Equations (41), (42) and (43) hold regardless of _t_ . The first part focuses on assessing the initial error of outer iteration _t_ + 1 when the conditions hold at the end of outer iteration _t_ , and the second part on showing how these errors shrink during outer iteration _t_ + 1. 

#### **C.2.1 Warm-start error** 

We know that DVR converges linearly, and so the error for each subproblem decreases exponentially fast. Yet, we need to know how big the error is when solving a new problem in order to make sure that the progress from solving previous subproblems is not lost. The point of this is to avoid an extra log( _ε_<sup>_−_1</sup> ) factor in the rate, which would come from having to solve each subproblem from a _O_ (1) precision to an _ε_ precision using DVR. We show in this section that the initial error is actually much lower than _O_ (1) and decreases with the outer iterations. We first start by bounding the variations of _ωt_ across iterations, which we will need for the next proofs. 

**Lemma 6** (Distance between subproblems) **.** _It holds that_ 



_Proof._ The form of the updates yields that (see Lin et al. [2017, Proposition 12] or Li and Lin [2020, Proof of Lemma 10]) 



Note that here, _θ_<sup>_⋆_</sup> is the actual solution of the primal problem without the catalyst perturbation. Then, the error can be decomposed as: 



Finally, the strong convexity of _F_ leads to 



where in the last inequality we use [Lin et al., 2017, Proposition 5], which holds because _Fk_ ( _θ_<sup>¯</sup> _k_ ) _− Fk_ ( _θ⋆_<sup>_k_)</sup><sup>_≤εk_forall</sup><sup>_k<t_.Indeed,</sup><sup>_K_issuchthatforall</sup><sup>_k≤t_,</sup><sup><u>1</u></sup> 2 � _ni_ =1<sup>_∥θ_</sup> _k_<sup>(</sup><sup>_i_)</sup><sup>_−θ_</sup> _⋆_<sup>_k∥_2</sup><sup>_≤_</sup> _L_<sup>_<u>n</u>εk_,which</sup> yields: 



Therefore, 

28 

and a similar bound can be used for _θt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>and</sup><sup>_θ_</sup> _t_<sup>(</sup> _−_<sup>_i_)</sup> 2<sup>.Then,wefinishproofbyplugginginthe</sup> expression of _εt−_ 1. 

We then use Lemma 6 to bound the initial dual error. We denote _θk_<sup>_t_(and</sup><sup>_λt_</sup> _k_<sup>)theparametersat</sup> inner iteration _k_ of outer iteration _t_ . 

**Lemma 7** (Dual error warm-start) **.** _The warm-started dual error verifies:_ 



Note that we simply warm-start the dual coordinates for an outer iteration using the last iterate from the previous one. Yet, this leads to _θ_ 0<sup>_t_=</sup><sup>_θ_</sup> _K_<sup>_t−_1</sup> + _β_ Σ<sup>_−_</sup> _β_<sup>1(</sup><sup>_ωt_+1</sup><sup>_−ωt_),asinAlgorithm2.</sup> 

_Proof._ Equation (34) implies that _Dt_ ( _λ_ ) can be written as: 



with _R_ comp( _λ_ ) that only depends on _λ_<sup>(</sup><sup>_ij_)</sup> and not on _ωt_<sup>(</sup><sup>_i_)</sup> for _i ∈{_ 1 _, · · · , n}_ . Therefore, 



Equation (30) writes ( _Aλ_<sup>_t_</sup> _⋆_<sup>)(</sup><sup>_i_)= (</sup><sup>_β_+</sup><sup>_σi_)</sup><sup>_θ_</sup> _⋆_<sup>_t−βω_</sup> _t_<sup>(</sup><sup>_i_),andso:</sup> _Aλ_<sup>_t_</sup> _⋆_<sup>_−Aλt_</sup> _K_<sup>_−_1</sup> = _Aλ_<sup>_t_</sup> _⋆_<sup>_−Aλt_</sup> _⋆_<sup>_−_1</sup> + _Aλ_<sup>_t_</sup> _⋆_<sup>_−_1</sup> _− Aλ_<sup>_t_</sup> _K_<sup>_−_1</sup> = Σ<sup>_−_</sup> _β_<sup>1(</sup><sup>_θ_</sup> _⋆_<sup>_t−θ_</sup> _⋆_<sup>_t−_1</sup> ) + _Aλ_<sup>_t_</sup> _⋆_<sup>_−_1</sup> _− Aλ_<sup>_t_</sup> _K_<sup>_−_1</sup> _− β_ ( _ωt − ωt−_ 1) _._ Then, we know from the equivalent reformulation of Equation (35) that _θt_<sup>_⋆_= arg min</sup><sup>_F_(</sup><sup>_θ_)+</sup><sup>_<u>β</u>_</sup> 2<sup>_∥θ−ω_¯</sup><sup>_t∥_2,</sup> so using the 1-Lipschitzness of the proximal operator yields 



Plugging in Equation (47) yields: 



Finally note that _Dt−_ 1( _λ_<sup>_t_</sup> _⋆_<sup>)</sup><sup>_≤Dt−_1(</sup><sup>_λ_</sup> _⋆_<sup>_t−_1</sup> ) since _λ⋆_<sup>_t−_1</sup> is the maximizer of _Dt−_ 1, and ( _θK_<sup>_t−_1)(</sup><sup>_i_)=</sup><sup>_θ_</sup> _t_<sup>(</sup><sup>_i_)</sup> since it is the output of DVR after inner iteration _t_ . The final expression is obtained using 6 and the recursion assumptions given by Equations (41) and (43). 

29 

Finally, the warm-start error on the nodes parameters is given by the two following lemmas. 





We finish this part on warm starts by proving the following lemma, that links the initial dual parameters error (computed with the Bregman divergence of _φ_ ), to the other parameters which we already know how to control. 

**Lemma 10** (Dual parameters warm-start, as measured by the Bregman divergence) **.** 





_Proof._ We first decompose the Bregman divergence as: 



30 

Then, we bound the communication term as: 



Using Lemmas 8 and 9, we obtain: 



For the computation part, we use the duality property of the Bregman divergence, which yields 

Therefore, 



Substituting Equations (52) and (53) into Equation (51) finishes the proof. 

#### **C.2.2 Inner iteration error decrease** 

Now that we have bounded the error at the beginning of each outer iteration, we bound error at the end of each outer iteration by using the convergence results for DVR. We first prove the following Lemma, which controls the distance between the virtual parameters and the actual one: 

**Lemma 11** (Virtual error decrease) **.** _For all_ ( _i, j_ ) _,_ 



31 

_Proof._ We cannot retrieve direct control over the _θt_<sup>(</sup> +1<sup>_ij_)fromcontroloverthedualvariablesorthe</sup> dual error, since this would require the _fij_<sup>_∗_functionstobesmooth,whichtheymaynotbe.Yet,</sup> we leverage the fact that _θt_<sup>(</sup> +1<sup>_ij_)isobtainedbyaconvexcombinationbetween</sup><sup>_θ_</sup> _t_<sup>(</sup><sup>_ij_)</sup> and _θt_<sup>(</sup><sup>_i_)</sup> to obtain convergence of to _θ⋆_<sup>_t_.Wenote</sup><sup>_jt,k_(</sup><sup>_i_)thevirtualnodethatisupdatedattime(</sup><sup>_t, k_)fornode</sup><sup>_i_.We</sup> note E _k_ the expectation relative to the value of _jt,k_ ( _i_ ). We start by remarking that: 



where in the last inequality we used the convexity of the squared norm. We use that _pijρij ≥ ρ_ (equal for the smallest one), and write that: 





Using Lemma 5, we know that<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_∥_(</sup><sup>_θ_</sup> _k_<sup>_t_)(</sup><sup>_i_)</sup><sup>_−θ_</sup> _⋆_<sup>_t∥_2</sup><sup>_≤C_0(</sup><sup>_t_)(1</sup><sup>_−ρ_)</sup><sup>_k_,with</sup><sup>_C_0(</sup><sup>_t_)aconstantthat</sup> depends on the initial conditions of outer iteration _t_ . Therefore, 



In the end, 



This lemma has the following corollary: 

**Corollary 1** (Warm-started virtual error decrease) **.** _For all_ ( _i, j_ ) _,_ 



_with_ 

_Proof._ Using Lemmas 5, 10 and 7, we write: 

We use Lemma 8 for the first term. 

32 

**Lemma 12** (Condition on _K_ ) **.** _If Equations_ (41) _,_ (42) _and_ (43) _hold at time t, and K is such that:_ 



_then they also hold at time t_ + 1 _._ 

_Proof._ Using Corollary 1, we obtain that if _K_ is set such that 



then the recursion condition is respected for the virtual parameters. This yields the first and second conditions on _K_ . Now, we write _CL_ = � _<u>p</u>_ <u>min</u> _ηt_<sup>_Cφ_+</sup><sup>_CD_</sup> �, then using Lemmas 10 and 7 (where _Cφ_ and _CD_ are defined), we obtain using Theorem 4 that 



since _λt_ +1 is obtained by performing _K_ iterations of DVR to minimize _Ft_ starting from _λt_ . This yields the third condition on _K_ . Finally, the last condition on _K_ is obtained by leveraging Lemma 5. 

## **D Experiments** 

For the experiments, the following logistic regression problem is solved: 



where the pairs ( _Xij, yij_ ) _∈_ R<sup>_d_</sup> _× {−_ 1 _,_ 1 _}_ are taken from the RCV1 dataset, which we downloaded from `https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html` . 

Figure 2 is the full version of Figure 1, in which we report the number of individual gradients and number of communications for each configuration. We see that accelerated EXTRA actually outperforms EXTRA when the regularization is small, as already mentioned in the main text. We also see that Accelerated EXTRA and Accelerated DVR have comparable communication complexity on the grid graph, when _γ_ is smaller. Yet, the computation complexity of (accelerated) DVR is much smaller, so accelerated DVR is much faster overall as long as _τ_ is not too big. 

33 



<!-- Start of picture text -->
10 0 10 0 EXTRA<br>10 2 DVR<br>10 3 10 3 NIDS<br>10 5 GTSAGA<br>10 6 10 6 Acc. EXTRA<br>10 9 10 8 10 9 Acc. DVR<br>10 12 10 11 10 12<br>0 1 2 3 4 0 2000 4000 6000 8000 0.00 0.25 0.50 0.75 1.00<br>Nb. of indiv. gradients 1e5 Nb. of co mm unications Time 1e7<br>(a) Erdős-Rényi, σ =  m ·  10 − 5<br>10 2 10 1 10 1<br>10 4 10 4<br>10 5<br>10 7 10 7<br>10 8<br>10 10 10 10<br>10 11 10 13 10 13<br>0 2 4 6 0 2000 4 00 0 0.0 0.5 1.0 1.5<br>Nb. of indiv. gradients 1e 5 Nb. of communications Time ( = 250) 1e6<br>(b) Grid, σ =  m ·  10 − 5<br>10 2 10 2 10 1<br>10 0 10 2<br>10 2 10 5 10 5<br>10 4 10 8 10 8<br>10 6 10 11<br>10 11<br>10 8 10 14<br>0 2 4 0 1 2 3 0.0 0.5 1.0<br>Nb. of indiv. gradients 1e6 Nb. of communications 1e4 Time ( = 250) 1e7<br>(c) Erdős-Rényi, σ =  m ·  10 − 7<br>10 1 10 1 10 1<br>10 2<br>10 3 10 3 10 5<br>10 8<br>10 5 10 11<br>10 5<br>10 14<br>0 1 2 3 0 1 2 3 0 1 2 3<br>Nb. of indiv. gradients 1e6 Nb. of communications 1e4 Time ( = 250) 1e7<br>(d) Grid, σ =  m ·  10 − 7<br>Suboptimality Suboptimality Suboptimality<br>Suboptimality Suboptimality Suboptimality<br>Suboptimality Suboptimality Suboptimality<br>Suboptimality Suboptimality Suboptimality<br><!-- End of picture text -->

Figure 2: Experimental results for the RCV1 dataset with different graphs of size _n_ = 81, with _m_ = 2430 samples per node, and with different regularization parameters. 

34 

