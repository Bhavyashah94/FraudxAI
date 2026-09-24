---
title: "Hawkes Processes in Finance"
authors: "umr"
year: 2015
arxiv_id: "1502.04592"
original_file: "1502.04592.pdf"
pdf_path: "docs/papers\2015_umr_hawkes_processes_in_finance.pdf"
---

# Hawkes Processes in Finance

**Authors:** Umr et al.  
**Year:** 2015 | **arXiv:** [`1502.04592`](https://arxiv.org/abs/1502.04592)  
**Local PDF:** [`2015_umr_hawkes_processes_in_finance.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2015_umr_hawkes_processes_in_finance.pdf)

---

## Hawkes processes in finance 

Emmanuel Bacry<sup>1</sup> , Iacopo Mastromatteo<sup>1</sup> , and Jean-Fran¸cois Muzy<sup>1,2</sup> 

1Centre de Math´ematiques Appliqu´ees, CNRS, ´Ecole Polytechnique, UMR 7641, 91128 Palaiseau, France 

> 2Laboratoire Sciences Pour l’Environnement, CNRS, Universit´e de Corse, UMR 6134, 20250 Cort´e, France 

###### **Abstract** 

In this paper we propose an overview of the recent academic literature devoted to the applications of Hawkes processes in finance. Hawkes processes constitute a particular class of multivariate point processes that has become very popular in empirical high frequency finance this last decade. After a reminder of the main definitions and properties that characterize Hawkes processes, we review their main empirical applications to address many different problems in high frequency finance. Because of their great flexibility and versatility, we show that they have been successfully involved in issues as diverse as estimating the volatility at the level of transaction data, estimating the market stability, accounting for systemic risk contagion, devising optimal execution strategies or capturing the dynamics of the full order book. 

### **1 Introduction** 

The availability of high frequency financial data during the last decades allowed the empirical finance to devise and calibrate models of market microstructure, aiming at accounting for the intraday market dynamics in its finest details. Until recently, there were only few continuous time models for the high frequency price variations. Most approaches relied on discrete time models that consist either in aggregating the dynamics on intervals of a regular time grid or in considering the succession of discrete time events like trades (these models are generally referred to as “trading time” or “business time” models). Hasbrouck [36], Engle and Russel [28] in the nineties, were the first to advocate that the modeling of financial data at the transaction level could be advantageously done within the framework of continuous time “point processes”. Since then, point processes applications to finance is an ongoing, very active topic in the econometric literature. We refer the reader to the recent review of Bowens and Hautsch [9] on this subject. 

The first type of point processes proposed in the context of market microstructure is the ACD model introduced by Engle and Russel [28]. This model and its variants remains, by far, the most used model in high frequency econometrics [9]. In this class of models, the process is defined by the means of its “hazard function” that specifies the conditional law of inter-event (or duration) intervals. However, point processes (or counting processes) can alternatively be represented by their “intensity 

1 

function” that represents the conditional probability density of the occurrence of an event in the immediate future (see e.g. [22] for a comprehensive textbook on point process mathematical properties). 

In a pioneering work, Bowsher [15], recognized the flexibility and the advantages of using the class of multivariate counting processes that can be specified by a conditional intensity vector. More specifically, he introduced a bivariate Hawkes processes in order to model the joint dynamics of trades and mid-price changes of the NYSE. Hawkes processes is a class of multivariate point processes that were introduced in the seventies by A.G Hawkes [37, 38] notably to model the occurrence seismic events. They involve an intensity vector that is a simple linear function of past events (see e.g. [10, 9] for other examples of dynamical intensity point processes). Hawkes models are becoming more and more popular in the domain of high frequency finance. This popularity can be explained above all by their great simplicity and flexibility, as anticipated by Bowsher [15]. These models can easily account for the interaction of various types of events, for the influence of some intensive factors (through marks) or for the existence of non-stationarities. They are amenable to statistical inference and closed-form formulae can be obtained in some particular situations. Moreover since their parameters have a straightforward interpretation (notably through the cluster representation), they lead to a quite simple interpretation of many aspects of the complex dynamics of modern electronic markets. 

In this paper, we propose a survey of recent academic studies using Hawkes processes in the context of finance. As we already explained, there are many such studies. In order to present them in relation one to each other, we had to group them by “themes”. Of course, the boundaries of these themes are unclear (e.g., some of the studies belong to several themes), so the choices we have made are unavoidably somewhat arbitrary. However we believe it helps capturing the “picture” of Hawkes models in finance. 

This survey is organized as follows. Sec. 2 is devoted to the theory of Hawkes processes. It introduces the main definitions and the general properties that will be used all along the paper. The following Sections focus on the applications of Hawkes processes to finance. Sec. 3 starts with the main univariate models that can be found in the literature. That includes market activity or risk models (e.g., 1-dimensional market order flow models, extreme return models). Price models (mid-price or best limit price) are presented in Sec. 4 whereas Sec. 5 is devoted to impact models. In this Section, we do not only discuss the influence of market order flows on price moves but also the problems related to optimal execution. Models that involve more order flows are presented in Sec. 6. So-called level-I models (i.e., dealing “only” with the dynamics of the best limits) as well full order book models are discussed. Finally, various studies that did not clearly fit in any of the previous Sections are presented in Sec. 7 (e.g. systemic risk models, high-dimensional models or news models). More materials can be found in Appendices. In Appendix A, all the academic works that are discussed throughout our paper and which involves numerical experiments on financial data is listed in a single table. This table summarizes some essential characteristics of the models and data used in each work. Finally, two Appendices sum up the main results about simulation (App. B) and estimation (App. C) of Hawkes processes. 

2 

### **2 The Hawkes process** 

As mentioned in the introduction, Hawkes processes are a class of multivariate point processes introduced by Hawkes in the early seventies [37, 38] that are characterized by a stochastic intensity vector. If _Nt_ is a vector of counting processes<sup>1</sup> at time _t_ , then its intensity vector _λt_ is defined heuristically as (see e.g. [22] for a rigorous definition): 



where the filtration _Ft_ stands for the information available up to (but not including) time _t_ . In the case of Hawkes processes, _λt_ is simply a linear function of past jumps of the process as specified thereafter. 

#### **2.1 Definition** 

We consider a _D_ -variate counting-process _Nt_ = _{Nt_<sup>_i}D_</sup> _i_ =1<sup>, whose associated intensity</sup> vector is denoted as _λt_ = _{λ_<sup>_i_</sup> _t_<sup>_}D_</sup> _i_ =1<sup>.</sup> 

**Definition 1** (Hawkes process) **.** _A Hawkes process is a counting-process Nt such that the intensity vector can be written as_ 



_where the quantity µ_ = _{µ_<sup>_i_</sup> _}_<sup>_D_</sup> _i_ =1<sup>_isavectorofexogenousintensities,and_Φ(</sup><sup>_t_)=</sup> _{φ_<sup>_ij_</sup> ( _t_ ) _}_<sup>_D_</sup> _i,j_ =1<sup>_isamatrix-valuedkernelsuchthat:_</sup> 

- _It is component-wise positive, i.e., φ_<sup>_ij_</sup> ( _t_ ) _≥_ 0 _for each_ 1 _≤ i, j ≤ D;_ 

- _It is component-wise causal (if t <_ 0 _, φ_<sup>_ij_</sup> ( _t_ ) = 0 _for each_ 1 _≤ i, j ≤ D);_ 

- _Each component φ_<sup>_ij_</sup> ( _t_ ) _belongs to the space of L_<sup>1</sup> _-integrable functions_<sup>2</sup> 

**Notation 1** (Convolution) **.** _We can adopt a more compact notation so to rewrite Eq. (2) as_ 



_by defining the ∗ operation, corresponding to a matrix multiplication in which ordinary products are replaced by convolutions._ 

**Notation 2** (Event times) **.** _By introducing the couples {_ ( _tm, km_ ) _}_<sup>_M_</sup> _m_ =1<sup>_,wheretm_</sup> _denotes the time of event number m and km ∈_ [1 _, ..., D_ ] _indicates its component, Eq. (2) can also be rewritten as_ 



Fig. 1 shows as an example a specific realization of a multivariate Hawkes process. Even though the process defined by Eq. (2) is well-defined by any choice of kernel Φ( _t_ ) satisfying the three conditions stated above, the stationary case characterized below is of particular relevance in most of the applications of Hawkes processes to finance (see Sec. 2.2 for some notable exceptions). 

> 1A counting process is a stochastic process _{Nt}t≥_ 0, with values that are positive, integer, and increasing. By convention _N_ 0 = 0. 

> 2Strictly speaking, this definition only calls for _φij_ ( _t_ ) _∈ Lloc_ 1<sup>butthisisofnointerestforthispaper.</sup> 

3 



<!-- Start of picture text -->
5<br>4<br>3<br>2<br>1<br>i  =  D<br>. . .<br>i  = 3<br>i  = 2<br>i  = 1<br>0 5 10 15 20<br>Time t<br> iNt<br><!-- End of picture text -->

**Figure 1:** A realization of a multivariate Hawkes process. The dots represent individual events, while the different rows refer to different _i_ coordinates. 

**Proposition 1** (Stationarity) **.** _The process Nt has asymptotically stationary increments and λt is asymptotically stationary if the kernel satisfies the assumption, also referred to as the_ **stability condition** _:_ 

**(H)** _The matrix ||_ Φ _||_ = _{||φ_<sup>_ij_</sup> _||}_<sup>_D_</sup> _i,j_ =1<sup>_hasspectralradiussmallerthan1._</sup> 

**Notation 3** (Spectral radius) **.** _Here and in the following parts of the discussion, given a a scalar function f_ ( _t_ ) _we denote with the symbol ||f || its L_<sup>1</sup> _-norm, defined as_ � d _t |f_ ( _t_ ) _|. For a matrix F_ = _{f_<sup>_ij_</sup> _}, the notation ||F || will denote its spectral radius. Finally, for a matrix of functions F_ ( _t_ ) = _{f_<sup>_ij_</sup> ( _t_ ) _}_<sup>_D_</sup> _i,j_ =1<sup>_,wewillwrite||F||_=</sup> _{||f_<sup>_ij_</sup> _||}_<sup>_D_</sup> _i,j_ =1 

From now on, we will always consider (unless specified) that assumption **(H)** holds and that the Hawkes processes are in the asymptotically stationary regime. In particular, the averages taken in the stationary state will be denoted with E [ _. . ._ ], while the variances will be written as V [ _. . ._ ]. The consequences of the stationarity assumption **(H)** will be fully explored in the next subsection. Here, we will first provide a simple implementation of a Hawkes process, whose prototypical version is the one in which the kernel functions _φ_<sup>_ij_</sup> ( _t_ ) are exponential functions. 

**Example 1** (Exponential kernel) **.** _Consider a bivariate Hawkes process in which_ 

4 

_the kernel matrix has the form_<sup>3</sup> 



_where the kernel components have the exponential form_ 



_where_ 1 _x is an indicator function equal to 1 if x is true and zero otherwise. The above functions are L_<sup>1</sup> _-integrable, so that the choice α_<sup>(</sup><sup>_s/c_)</sup> _, β_<sup>(</sup><sup>_s/c_)</sup> _>_ 0 _ensures that the associated Hawkes process is well-defined. For the process to be stable, one needs to additionally require that the spectral norm satisfies ||_ Φ _||_ = _||φ_<sup>(</sup><sup>_s_)</sup> _||_ + _||φ_<sup>(</sup><sup>_c_)</sup> _|| <_ 1 _. Due to α_<sup>(</sup><sup>_s/c_)</sup> = �0 _∞ φ_<sup>(</sup><sup>_s/c_)</sup> ( _t_ ) _, the stability condition becomes_ 



_The α_<sup>(</sup><sup>_s/c_)</sup> _parameters can be interpreted as the ones setting the overall strength of the interactions, while the β_<sup>(</sup><sup>_s/c_)</sup> _control the relaxation time of the perturbations induced from past to future events._ 

The Hawkes process with exponential kernels has several advantageous properties, as it allows one to compute the expected value of arbitrary functions of _Nt_ (see Sec. 2.3.4 and Ref. [29]), to be directly simulated (see App. B), or to compute efficiently its likelihood (see App. C.1). Most of these properties descend from a Markov property which in its simplest form is stated as follows: 

**Proposition 2** (Markov property for exponential kernels) **.** _Consider a Hawkes process with exponential kernels φ_<sup>_ij_</sup> ( _t_ ) = _α_<sup>_ij_</sup> _βe_<sup>_βt_</sup> 1 _t∈_ R+ _. Then the couple_ ( _Nt, λt_ ) _is a Markov process. In particular, Eq. (2) for the intensity λt can be recast in Markovian form as_ 



This property can be extended to the case in which _(i)_ the coefficients _β_<sup>_ij_</sup> are non-constant across components and _(ii)_ the kernel Φ contains a finite sum of exponentials. The price to pay in this more general setting is the introduction of an extra set of _A_ auxiliary processes _{λ_<sup>˜(</sup> _t_<sup>_a_)</sup> _}_<sup>_A_</sup> _a_ =1<sup>,suitablychosensothattheresulting</sup> ( _A_ + 1)-uple ( _Nt, λ_<sup>˜(1)</sup> _t_<sup>_, . . . ,_˜</sup><sup>_λ_(</sup> _t_<sup>_A_)</sup> ) is Markovian. 

In the non-exponential case, the Hawkes process cannot be generally mapped to a Markovian process, implying that it is necessary to take track of all its past history in order to perform exact simulation and estimation. A particularly well-known example of a non-exponential kernel is the power-law one, proposed in Ref. [59] in order to describe temporal clusters of seismic activity. 

**Example 2** (Power-law kernel) **.** _Let’s now consider the case D_ = 1 _, and assume the kernel to be parameterized by the regularized power-law_ 



> 3The upperscript ( _s_ ) (resp. ( _c_ )) stands for the word _self_ (resp. _cross_ ), since it describes the self(resp. cross-) excitation of the two components. 

5 

_Also in this case the process is well-defined for α, β >_ 0 _. The stationarity condition in is met for_ 



_indicating that the tail exponent γ of a power law-kernel should be positive for the increments of the process to be stationary._ 

#### **2.2 Some extensions** 

Although the model defined in above section is the one originally introduced in [37, 38], and most widely used in the literature, several generalizations have been proposed since. 

##### **2.2.1 Marked Hawkes processes** 

Eq. (4) defining the Hawkes process can be enriched by endowing each event with a _mark_ variable, thus obtaining a sequence of event times, components and marks _{_ ( _tm, km, ξm_ ) _}_<sup>_M_</sup> _m_ =1<sup>.Onemayfurtherassumeseventslabeledwithdifferentmarks</sup> to have different effects on the future intensities, leading to a dynamics for _λt_ of the type 



Finally, one needs to introduce a generating mechanism for the marks, which are typically assumed to be i.i.d. random variables drawn with each event and sampled from a common distribution _p_ ( _ξ_ ). A typical choice for the interaction kernel is the one _φ_<sup>_ij_</sup> ( _t, ξ_ ) = _φ_<sup>_ij_</sup> ( _t_ ) _χ_<sup>_ij_</sup> ( _ξ_ ), in which one assumes a factorized form for the effect of the marks. This mechanism is used to describe events of different weights, and has been originally employed in order to model the occurrence of earthquakes of difference magnitudes [59]. In finance, marks can be used in order to model trades performed at times _tm_ with different volumes _ξm_ (as e.g. in [30, 5], see Sec. 4 and 5) or a drawdown intensity (as e.g. in [27, 18], see Sec. 3.1). On a more general ground, note that multivariate Hawkes processes can also be seen as an example of Hawkes processes with interacting marks [51]. 

##### **2.2.2 Exogenous non-stationarity** 

The exogenous intensity _µ_ can be generalized to a deterministic function of time _µ_ ( _t_ ). This choice allows to model a non-stationary system in which the interaction kernel is indeed independent of time. In finance, this is the case when one wants to model intra-day seasonalities (see the review article [9]) and/or spillover effects within successive days (as in [15]). 

##### **2.2.3 Endogenous non-stationarity** 

The scenarios _||_ Φ _|| >_ 1 and _||_ Φ _||_ = 1 have also been considered in order to model non-stationarity induced by endogenous interactions. These two cases present indeed an important difference: while in the former one the average intensity grows exponentially in time, in the latter one the process may possess a finite average event rate. This second type of non-stationarity, which we will call _quasi-stationarity_ , has 

6 

raised a strong interest in the literature due to the fact that the condition _||_ Φ _|| ≈_ 1 is often met when calibrating Hawkes processes to real financial data (see the detailed discussion in Sec. 3). The limiting behavior of a Hawkes process in the regime _||_ Φ _||_ = 1 has been analyzed by Br´emaud and Massouli´e in [17], where it is shown in particular that: 

**Proposition 3** (Degeneracy of critical, short-range Hawkes) **.** _Let Nt be a univariate Hawkes process as in Eq. (2) such that ||_ Φ _||_ = 1 _and µ_ = 0 _. Then if_ 



_the average of the conditional intensity is either_ 0 _or_ + _∞._ 

Hence in the _D_ = 1 case, short-ranged kernels always lead to trivial processes. The next result shows instead that interactions of broader range allow instead a richer behavior. 

**Theorem 1** (Existence of critical, stationarity) **.** _Let’s now consider a Hawkes process with ||_ Φ _||_ = 1 _, µ_ = 0 _and_ 





_where r, R >_ 0 _and γ ∈_ ]0 _,_ 1 _/_ 2[ _. Then the average intensity of such process is finite._ 

Summarizing, there exist non-trivial univariate Hawkes processes with _||_ Φ _||_ = 1 only for specific values of the tail exponent of Φ( _t_ ), which is required to lie in the interval _γ ∈_ ]0 _,_ 1 _/_ 2[. 

Notice that, even though in _D_ = 1 a quasi-stationary short-ranged Hawkes process is always degenerate, Ref. [42] describes a scaling regime for _Nt_ in which it is possible to obtain to a non-degenerate process in the limit _||_ Φ _|| →_ 1 by appropriately choosing an observation timescale for the process. This behavior will be reviewed in Sec. 2.3.6. 

In the multivariate setting, Ref. [51] shows that even in presence of kernels Φ satisfying the short-range condition Eq. (12) it is possible to define a non-trivial quasistationary Hawkes process in the large-dimensional limit. In particular Ref. [51] assumes a factorized form of the kernel, of the type 



with _||f ||_ = 1, and consider the _D →∞_ limit of the process _Nt_ . Such a limiting regime turns out to be well-defined also when _||_ Φ _||_ = _||α|| −−−−→D→∞_<sup>1,providedthat</sup> the matrix _α_ has a sufficiently low density of eigenvalues in the vicinity of the critical point _||α||_ = 1. Hence, a non-degenerate quasi-stationary limit for a Hawkes process can also be obtained as an effect of the interaction among a large number of components. 

7 

##### **2.2.4 Non-linear Hawkes** 

Non-linear generalizations of the Hawkes process have been considered by several authors [16, 65, 62, 69]. The intensity function in the non-linear case is written as 



where _h_ ( _·_ ) is a non-linear function with support in R<sup>+</sup> . Typical choices for _h_ include _h_ ( _x_ ) = 1 _x∈_ R+ and _h_ ( _x_ ) = _e_<sup>_x_</sup> . Note that the stability condition for various functions _h_ was studied by Br´emaud and Massouli´e in [16]. The main advantage introduced by this extension is the possibility of modeling inhibition through negative valued kernels, although the price that has to be paid is the loss of mathematical tractability for most of the properties of the process. Yet, simulation and calibration of the model are possible even in this scenario [33, 8]. As we will see, negative valued kernels are found in the context of finance (see for instance Sec. 6.1). 

Let us end this section by mentioning that we have only referred to the most common extensions of Hawkes original model but many further generalizations have been proposed like e.g., mixed diffusion-Hawkes models [29, 18], Hawkes models with shot noise exogenous events [23], Hawkes processes with generation dependent kernels [53]. 

#### **2.3 Properties** 

The linear structure of the stochastic intensity _λt_ of a Hawkes process allows us to characterize many of its properties in a completely analytical manner. Notably, its first- and second-order properties are particularly easy to compute, while a cluster representation of the process can be used in order to obtain a useful characterization of the Hawkes process. These properties are reviewed in the following Section. 

##### **2.3.1 First and second order properties** 

Assuming the hypothesis **(H)** , it is then possible to write explicitly the first- and the second-order properties of the model in term of the Laplace transform of the kernel Φ. In order to do this, it is necessary to introduce the function Ψ defined as follows: 

**Definition 2** (Kernel inversion) **.** _Consider a Hawkes process Nt with stationary increments. We define_ Ψ( _t_ ) _as the causal solution of the equation_ 



_As a consequence of_ **(H)** _,_ Ψ( _t_ ) _exists and can be expressed as the infinite convolution_ 



The matrix function Ψ can be characterized analytically in term of the Laplace transform of the kernel Φ, which we define as follows: 

**Notation 4** (Laplace transform) **.** _Given a scalar function f_ ( _t_ ) _∈ L_<sup>1</sup> ( _−∞,_ + _∞_ ) _, we denote its Laplace transform as_ 



8 

_Vector and matrix Laplace transforms are defined by applying the above transformation component-wise._ 

In the Laplace domain, Eq. (18) is then mapped to the algebraic relation 



where I denotes the identity matrix, allowing us to state the main result concerning the linear properties of a Hawkes process: 

**Proposition 4** (First- and second-order statistics) **.** _For a Hawkes process Nt with stationary increments, the following propositions hold:_ 

_1. The average intensity_ Λ = E [ d _Nt_ ] _/_ d _t is equal to_ 



_2. The Laplace transform of the linear correlation matrix_ 



_is equal to_ 



_where_ Σ _is a diagonal matrix with non-zero elements equal to_ Σ<sup>_ii_</sup> = Λ<sup>_i_</sup> _._ 

This useful characterization of the linear properties of a Hawkes process, first formulated in [37, 38] and then fully generalized in [8], allows to _(i)_ obtain the linear predictions of a Hawkes model given _µ_ and Φ as an input, _(ii)_ calibrate nonparametrically the kernel Φ from empirical data by inverting relations (21) and (23) (see App. C.1). 

Let us point out that, in Ref. [4], the authors have established that under general conditions, the empirical covariation of a multivariate Hawkes process converges towards its expected value, that can be easily expressed in terms of the Hawkes covariance matrix _c_ ( _t_ ) as given by Eq. (23). 

**Example 3** (Exponential kernel) **.** _Let’s consider again the bivariate case described by Eq. (5) in the stationary case_ 1 _> α_<sup>(</sup><sup>_s_)</sup> + _α_<sup>(</sup><sup>_c_)</sup> _. In that case, the Laplace transform of the kernel_ Φ(<sup>ˆ</sup> _z_ ) _reads:_ 



_implying that the kernel matrix is diagonal in the symmetric and antisymmetric combinations Nt_<sup>_±_</sup> = 2<sup>_−_1</sup><sup>_/_2</sup> ( _Nt_<sup>1</sup><sup>_±N_</sup> _t_<sup>2)</sup><sup>_._</sup> _The Laplace transform of the individual components of the kernel is_ 



_and due to the diagonal form of Eq. (5) the inverse kernel_ Ψ(<sup>ˆ</sup> _z_ ) _can be computed straightforwardly. If one assumes µ_ = ( _µ_ 0 _, µ_ 0) _, then the relations above imply that_ Λ = (Λ0 _,_ Λ0) _, with_ 





_The Laplace transforms of the lagged cross-correlations of the symmetric and antisymmetric combinations X±_ ( _t_ ) _, defined as_ 



_result_ 



_Above expression can be inverted explicitly so to obtain the lagged cross-correlations in real space. In the simpler case β_<sup>(</sup><sup>_s_)</sup> = _β_<sup>(</sup><sup>_c_)</sup> = _β_ 0 _, one obtains for example_ 



_Note that a singular component arises for t_ = 0 _due to the assumption of unitary jumps_ (d _N_ )<sup>2</sup> = d _N . Above formula also shows that by moving the spectral norm ||_ Φ _||_ = _α_<sup>(</sup><sup>_s_)</sup> + _α_<sup>(</sup><sup>_c_)</sup> _close to the instability point ||_ Φ _||_ = 1 _, the decay of the symmetric mode of correlation function becomes slower and slower. Fig. 2 illustrates the result above for the autocorrelation function of the modes Nt_<sup>_±._</sup> 



<!-- Start of picture text -->
Auto-correlation Normalized variance<br>Mode + Mode +<br>Mode − 1 . 4 Mode −<br>0 . 1<br>1 . 2<br>0<br>1<br>− 0 . 1<br>− 10 − 5 0 5 10 0 2 4 6 8 10<br>t t<br>() tc±<br>[()] /t V Nt±<br><!-- End of picture text -->

**Figure 2:** Autocorrelation function (left) and normalized variance (right) of the combinations _Nt_<sup>_±_</sup> diagonalizing the interaction kernel appearing in Eq. (5). We have used the parameter set _α_<sup>(</sup><sup>_s_)</sup> = 0, _α_<sup>(</sup><sup>_c_)</sup> = 0 _._ 1, _µ_ 0 = _β_ 0 = 1 in order to simulate a single realization of the process of length _T_ = 10<sup>5</sup> . For such a value of _T_ , the theoretical predictions (dashed lines) are almost exactly superimposed to the results of the simulations. The _δ_ ( _t_ ) component in the cross-covariance function has been omitted in the left panel for the sake of clarity. 

**Example 4** (Power-law kernel) **.** _Let’s now consider again the case of a power-law interaction kernel in dimension D_ = 1 _. For a kernel parameterized by Eq. (9), the_ 

10 

_Laplace transform reads_ 



_where_ Γ( _n, z_ ) _is the incomplete Gamma function. The inverse kernel_ Ψ(<sup>ˆ</sup> _t_ ) _may be expressed in the Laplace domain as_ 



_As shown in Sec. 2.1, in this case the spectral radius ||_ Φ _|| is equal to ||_ Φ _||_ = _|_ Φ(0)<sup>ˆ</sup> _|_ = _α/γ, so that the model is stable for α < γ. Under this assumption, the average intensity results_ 



_For a fixed value of the exogenous intensity µ, this relation interpolates between a total intensity equal to the exogenous one (in the non-interacting case α_ = 0 _) and an increasingly larger number of events as soon as α approaches the instability point α_ = _γ._ 

_The Laplace transform of the lagged cross-correlation matrix results_ 



_The above expression cannot be inverted analytically. One can indeed relate the tail behavior of the correlations to the small z behavior of c_ ˆ( _z_ ) _thanks to Tauberian Theorems. In particular, for βt ≫_ 1 _one has:_ 



_This behavior is illustrated in Fig. 3, where we compare the autocorrelation function of several univariate Hawkes processes with power-law kernel and different tail exponents. As a final note, we remark that for γ <_ 1 _/_ 2 _, and close to the instability point α_ = _γ, the function c_ ( _t_ ) _obeys an intermediate asymptotics c_ ( _t_ ) _∼ t_<sup>2</sup><sup>_γ−_1</sup> _, which holds as long as_ 



_In this particular regime, the Hawkes process develops an apparent Hurst exponent H_ = 1 _/_ 2 + _γ. This limiting behavior is a consequence of the quasi-stationarity condition ||_ Φ _||_ = 1 _, analyzed in Ref. [17] and reviewed in Sec. 2.2.3._ 

##### **2.3.2 Characterization through second order statistics** 

This section justifies why the Hawkes process can be thought of as the simplest example of an interacting point process. In fact, it is entirely characterized by its first- and second-order properties: means and correlations uniquely determine a Hawkes process through the solution of a Wiener-Hopf system. 

11 

###### Auto-correlation 



<!-- Start of picture text -->
γ = 2<br>γ = 1<br>100<br>γ = 0 . 5<br>γ = 0 . 25<br>10<br>1<br>0 . 1 1 10 100<br>t<br>22 []  / ΛdddE NNt − 0 t<br><!-- End of picture text -->

**Figure 3:** Comparison of the autocorrelation function for a set of univariate Hawkes processes with power-law kernels parametrized by Eq. (9). We used the values _µ_ = _β_ = 1, _α_ = 0 _._ 9 _γ_ , and simulated processes of length _T_ = 5 _·_ 10<sup>5</sup> (for _γ_ = 0 _._ 25 and 0 _._ 5), _T_ = 10<sup>6</sup> (for _γ_ = 1) and _T_ = 5 _·_ 10<sup>6</sup> (for _γ_ = 2) in order to obtain the curves represented in the plot. The image illustrates the crossover from the exponential decay of correlation obtained for _β >_ 1 to the power-law behavior detected for _β <_ 1. 

Let us start by defining the _conditional intensity_ matrix _g_ ( _t_ ), that we define for _t >_ 0 as 



Then one can prove straightforwardly [8] from Eq. (23) that 



which relates conditional averages and lagged cross-correlations. Hence by using Eq. (37) and (23), one can prove that [8]: 

**Theorem 2** (Wiener-Hopf equation) **.** _Consider a Hawkes process defined by Eq. (1) satisfying the stationarity assumption_ **(H)** _. Then the matrix function χ_ ( _t_ ) = Φ( _t_ ) _is the unique solution of the Wiener-Hopf system_ 



_such that the components χ_<sup>_ij_</sup> ( _t_ ) _are causal and χ_<sup>_ij_</sup> ( _t_ ) _∈ L_<sup>1</sup> _∀i, j._ 

This property implies that, when fixing an average intensity vector Λ and a conditional expectation _g_ ( _t_ ), there exist at most one Hawkes process consistent with 

12 

these observables. Indeed, such a process is not always guaranteed to exist, as a Hawkes process doesn’t necessarily reproduce the linear properties for systems in which inhibition is relevant. 

This result is the inverse one with respect to the one expressed by Eq. (23): while that equation expresses the fact that by fixing a kernel Φ( _t_ ) and an exogenous intensity _µ_ the correlations are uniquely determined, the theorem above states that correlations and average intensities uniquely fix the interactions. While the direct result was first proved in [37], the converse was shown in [8] by using the WienerHopf factorization technique. 

Finally note that the Wiener-Hopf system (38) is very useful in applications to empirical data, as it allows us to estimate non-parametrically the interaction kernel of a Hawkes process given a set of empirical observations (see App. C.2). 

##### **2.3.3 Auto-regressive projection** 

A Hawkes process with stationary increments can always be linearly approximated by suitably defined auto-regressive processes. In particular one can show that [51]: 

**Proposition 5** (Auto-regressive projection) **.** _Consider a Hawkes process Nt defined by Eq. (2) satisfying the stationarity assumption_ **(H)** _. Then the convolution Nt_<sup>(</sup><sup>_AR_)</sup> _defined by_ 



_where_ Ψ( _t_ ) _is the infinite convolution of the Hawkes kernel given by Eq. (18), and Wt is a standard D-dimensional Brownian motion, satisfies_ 





_where_ Λ _and c denote respectively the average intensity and the lagged cross-correlation matrix of Nt._ 

Hence, it is always possible to match the first and the second order properties of a stationary Hawkes process with interaction kernel Φ by using a convolution of Wiener processes. On the other hand, higher order moments cannot be matched in the same way. 

##### **2.3.4 Beyond second-order** 

The first- and second-order moments are not the only moments which can be computed analytically for a Hawkes process. In particular, Jovanovi´c _et al._ [44] have recently developed a combinatorial procedure allowing to calculate cumulants (and consequently, moments) of arbitrary order of a Hawkes process. More precisely, given a set of components _S ∈{_ 1 _, . . . , D}_ and one of times _tS_ = _{t_ 1 _, . . . t|S|}_ , it is possible to define a _cumulant density_ of a Hawkes process as 



where the sum runs over all the partitions _π_ of _S_ , _|π|_ denotes their number of blocks and _B_ labels individually the blocks of _π_ . Above equation generalizes the 

13 

definition of the average intensity, recovered for _|S|_ = 1, and of the lagged crosscorrelation function, obtained for _|S|_ = 2. Moment densities can be obtained from above expression by writing 



Ref. [44] shows how to express Eq. (42) as a sum of integral terms, which can be written explicitly in terms of _µ_ and Ψ( _t_ ). As each of such addends can be interpreted as a topologically distinct rooted tree with _|S|_ labeled leaves, the enumeration of all the contribution to Eq. (42) can be performed systematically. 

In the special case of a Hawkes processes with exponential kernel, a useful result is obtained by Errais _et al._ [29] by exploiting Dynkin’s formula for the couple ( _N, λ_ ) in the marked framework described in Sec. 2.2.1. In particular, they are able to express the generating function for the couple ( _N, λ_ ) in terms of the solution of an ordinary differential equation. While it may be necessary to solve numerically the equation for the generating function, closed-form expressions are available for specific moments of _Nt_ (see also the work of Dassios and Zhao [23] for similar results on a slight generalization of Hawkes processes). 

##### **2.3.5 Martingale representation** 

The process defined by Eq. (2) admits a convenient martingale representation once one introduces suitably defined _compensators_ �0 _t_<sup>d</sup><sup>_s λ_</sup> _s_<sup>_i_[22].</sup> 

**Theorem 3** (Martingale representation) **.** _Given a Hawkes process (2), the D stochastic processes_ 



_are martingales with respect to the canonical filtration of the process Nt [22]. Additionally, under the stability condition_ **(H)** _, the stochastic intensity λt admits the representation_ 



While the above result is valid even in the non-stationary regime, Eq. (45) takes a particularly simple form in the asymptotic regime of large _t_ , where it can be written as 



thanks to Eq. (21). The martingale property of the Hawkes process plays an important role in determining the first- and second-order properties discussed in above section, which are derived by means of Eq. (46) in [2, 8]. The representation Eq. (45) is also particularly useful in order perform predictions of the intensity of the Hawkes process given an historic filtration _Ft_ of the process. 

**Example 5** (Prediction of the intensity) **.** _Suppose that, given a Hawkes process which satisfies the stationary condition_ **(H)** _, one is interested in computing the predictor_ E � _λt_ �� _Fs_ � _for t > s. (see Ref. [40, 41] for direct applications in Finance)._ 

14 

_While, by naively applying the definition of the Hawkes processes, one can obtain an implicit equation of the type_ 



_the martingale representation Eq. (45) can be used in order to write the explicit expression_ 



##### **2.3.6 Scaling limit of the process** 

The structure of Hawkes processes is naturally adapted to describe systems in which the discrete nature of the jumps in the coordinates _Nt_ is relevant, making this model especially suitable for modeling high-frequency data. Indeed, in many applications one additionally needs to control the limiting behavior the system in the opposite regime of low frequencies, where the granularity of events is disregarded, and the scaling in time of _Nt_ needs to be known. 

**Diffusion towards a Brownian motion.** The following results, first proved in [4] allow us to establish that Hawkes processes, under appropriate hypotheses and after a suitable rescaling, behave at large times as linear combinations of Wiener processes. 

**Theorem 4** (Law of large numbers) **.** _Consider a Hawkes process as in Eq. (2) satisfying the stationarity assumption_ **(H)** _. Then_ 



_almost surely and in L_<sup>2</sup> _-norm._ 

Above result establishes a law of large numbers for the Hawkes process, valid for any stationary kernel. Indeed, under additional hypotheses it is also possible to formulate a corresponding functional central-limit theorem. 

**Theorem 5** (Central-limit theorem) **.** _Suppose that for all i, j ≤ D the kernel_ Φ( _t_ ) _satisfies_ 



_Then for u ∈_ [0 _,_ 1] _one has the following convergence is in law for the Skorokhod topology:_ 



_where Wt denotes a standard D-dimensional Brownian motion._ 

**Example 6** (Exponential kernel) **.** _Consider the bivariate Hawkes process analyzed in Sec. 2.1. Eqs. (5) and (51) above imply that_ 



15 

_which in term of the combinations Nt_<sup>_±_= 2</sup><sup>_−_1</sup><sup>_/_2(</sup><sup>_N_</sup> _t_<sup>1</sup><sup>_± N_</sup> _t_<sup>2)</sup><sup>_reads_</sup> 



_This behavior is summarized in Fig. 4, where we compare the rescaled processes NuT_<sup>_±_</sup> _at different timescales T ._ 



<!-- Start of picture text -->
Zu ± = 1 − (Λ α 0 ( s T )  ) ∓ 1 α/ 2( c ) � NuT ± − Λ ±uT �<br>2<br>0<br>− 2<br>0<br>− 2<br>0<br>− 2<br>0 0 . 25 0 . 5 0 . 75 1<br>u<br>T = 10<br>T = 100<br>T = 1000<br><!-- End of picture text -->

**Figure 4:** The figure illustrates the shape of the process _NuT_<sup>_±_at different timescales</sup> _T_ = 10 _,_ 100 _,_ 1000 for the same choice of parameters as in Fig. 2. The process has been rescaled according to Eq. (53) so to obtain a standard Wiener process _Wu_ in the limit _T →∞_ . The plot illustrates how the presence of discrete jumps, clarly visible at small times, becomes irrelevant in the scaling limit _T →∞_ . 

**Other scaling limits** It is well known that many of the microscopic observables involved in the price formation process do not diffuse at large scales (e.g., at the daily, or even monthly, time-scale) toward Brownian motion dynamics. For instance, the trading activity (i.e., the market-order flow) seems to be long-range dependent [14], while the volatility displays clusters that can last for months. Since, as we will see in the next sections, Hawkes processes tend to mimic very well the high-frequency 

16 

dynamics of financial time-series, it is natural to try to understand if diffusive limits other than the one described by Theorem 5 can be found. In a recent work by Jaisson and Rosenbaum [42], a sequence of rescaled univariate Hawkes processes 



indexed by a time-scale parameter _T_ and where _aT ∈_ [0 _,_ 1[ is proved to converge, when _T →_ + _∞_ , towards an integrated Cox, Ingersoll, Ross process [20] under the main following conditions<sup>4</sup> 

- the corresponding sequence of kernels _φ_<sup>(</sup><sup>_T_)</sup> ( _t_ ) satisfies _φ_<sup>(</sup><sup>_T_)</sup> ( _t_ ) = _aT φ_ ( _t_ ), where _φ_ is differentiable and it is such that _||φ||_ = _φ_<sup>ˆ</sup> (0) = 1, _φ_<sup>ˆ</sup><sup>_′_</sup> (0) _<_ + _∞_ , _||φ_<sup>_′_</sup> _||∞ <_ + _∞_ and _||φ_<sup>_′_</sup> _|| <_ + _∞_ , 

- the criticality condition **(H)** of Prop. 1 is met at a speed 



Hence, even though a quasi-stationary short-ranged Hawkes process is always degenerate, one can detect a non-trivial behavior of the rescaled counting function by suitably choosing an observation timescale _T ∼_ (1 _−||_ Φ<sup>(</sup><sup>_T_)</sup> _||_ )<sup>_−_1</sup> . Let us point out that the above conditions do not allow for _φ_ to have a power-law decay with an exponent strictly smaller than 2 (in the limit _t →_ + _∞_ ). As reviewed in Sec. 3, several studies tend to show that for many financial time-series (e.g., market order flow time-series) the relevant kernel has power-law tails with an exponent above but rather close to 1. Thus, strictly speaking, the previous framework is inappropriate to describe such behavior. Using the same asymptotics ( _T →_ + _∞_ ), Jaisson [41] studied the asymptotic limit of the correlation function of a 1-dimensional Hawkes process with a power-law kernel which decreases with an exponent 1 + _γ_ with _γ ∈_ ]0 _,_ 1 _/_ 2[. He proved that the auto-correlation function of the Hawkes process decreases asymptotically as a power-law with an exponent 1 _−_ 2 _γ_ , i.e., leading to a long-range dependence<sup>5</sup> . 

##### **2.3.7 Clustering representation** 

Another useful property of the Hawkes process is the _clustering_ property which emerges as a consequence of the linearity of Eq. (2). Such property allows one to _(i)_ build an efficient _simulation_ algorithm for the process (see App. B), _(ii)_ introduce the notion of _parenthood_ among different events (see Sec. 2.3.8 below), _(iii) infer_ parenthood relations among successive events from empirical data (see the paragraph about the EM method in App. C.2). 

**Proposition 6** (Clustering representation) **.** _Consider a positive integer D and a (non-necessarily finite) time interval_ [0 _, T_ ] _, in which we define a sequence of_ events _{_ ( _tm, km_ ) _}_<sup>_M_</sup> _m_ =1<sup>_accordingtothefollowingprocedure:_</sup> 

- _Mi_<sup>(0)</sup> 

- _• For each_ 1 _≤ i ≤ D, consider a set of_ immigrant _events {_ ( _t_<sup>(0)</sup> _m_<sup>_, i_)</sup><sup>_}_</sup> _m_ =1<sup>_extracted_</sup> _with homogeneous Poissonian rate µ_<sup>_i_</sup> _in the interval_ [0 _, T_ ] _._ 

> 4For precise formulation of the corresponding theorem, we refer the reader to [42]. 

> 5Let us notice that qualitative arguments for similar result were also given in [7] in a 2-dimensional framework. 

17 

- _For each immigrant event of type j, labeled by_ ( _t_<sup>(0)</sup> _m_<sup>_′, j_)</sup><sup>_,and for each_1</sup><sup>_≤i ≤N,_</sup> _Mi_<sup>(1)</sup> 

- _generate a sequence of_ first-generation _events {_ ( _t_<sup>(1)</sup> _m_<sup>_, i_)</sup><sup>_}_</sup> _m_ =1<sup>_sampled with time-_</sup> _dependent Poissonian rate φ_<sup>_ij_</sup> ( _t − tm′_ ) _in the interval_ [ _t_<sup>(0)</sup> _m_<sup>_′, T_]</sup><sup>_._</sup> 

- _Iterate above rule from generation n −_ 1 _to generation n, so to obtain the event sequence {_ ( _t_<sup>(</sup> _m_<sup>_n_)</sup><sup>_, k_</sup> _m_<sup>(</sup><sup>_n_))</sup><sup>_}M_</sup> _m_ =1<sup>(</sup><sup>_n_)</sup><sup>_,untilnomoreeventsaregeneratedin_[0</sup><sup>_, T_]</sup><sup>_._</sup> 

_Then the union of all the events_ 



_corresponds to the one generated by the Hawkes process (2) in the time interval_ [0 _, T_ ] _._ 

Note that the construction above (depicted in Fig. 5) can be equivalently taken as a definition for the Hawkes process, once the information encoding the generation _n_ is discarded by taking the union of all the events. Indeed, this richer definition 



<!-- Start of picture text -->
i  = 2<br>i  = 1<br>Time t<br>Clusterrepresentation<br><!-- End of picture text -->

**Figure 5:** Cluster representation of a Hawkes process: while the upper panel represents the branching structure of a bivariate Hawkes process, the lower panel shows its projection obtained by disregarding the cluster structure. The different components _i ∈{_ 1 _,_ 2 _}_ are shown in different colors, while the connected structures in the upper panel denote three different clusters. 

characterizes more transparently the stationarity condition **(H)** : by considering _T_ = _∞_ in above construction, it is possible to map the branching structure of the Hawkes 

18 

process described above onto the one of a Galton-Watson tree with average offspring _||_ Φ _||_ . The qualitative behavior of the model is in fact dictated by the average number of events generated by a parent event, equal to �0 _∞ φ_ ( _t_ ) = _φ_<sup>ˆ</sup> (0) = _||_ Φ _||_ . The three phases of the Hawkes process (stationary _||_ Φ _|| <_ 1, non-stationary _||_ Φ _|| >_ 1 and quasi-stationary _||_ Φ _||_ = 1) correspond then to the three phases of a Galton-Watson branching process, more precisely: 

1. For _||_ Φ _|| <_ 1, we have a _sub-critical_ phase in which each parent event generates on average less than one child event. This implies that the total progeny of each event is a.s. finite and the average number of generations before extinction is a.s. finite. 

2. For _||_ Φ _|| >_ 1, we have a _super-critical_ phase in which more than one child event is generated by each parent event. In that case the total progeny of a parent event might be infinite with finite probability. 

3. For _||_ Φ _||_ = 1 (the _critical_ case), the total progeny is a.s. finite, but the total size of the progeny has large fluctuations leading to a divergence of the average number of generations before extinction. 

##### **2.3.8 Causality** 

The parenthood relation introduced by using the clustering representation of the Hawkes process allows us to discuss the problem of causality in this context. In particular, after constructing a Hawkes process according to the branching procedure described above, one can introduce the counting functions 







so that _Nt_<sup>_i←_0</sup> +<sup>�</sup> _j_<sup>_N_</sup> _t_<sup>_i←j_</sup> = _Nt_<sup>_i←_0</sup> +<sup>�</sup> _j_<sup>_N_</sup> _t_<sup>_i←j∗_</sup> = _Nt_<sup>_i_.Hence,thesequantitiescan</sup> be used in order to express the overall number of events of type _i_ generated by an ancestor of a given type _j_ . In particular, it is easy to prove that: 

**Proposition 7** (Causality) **.** _For a stationary Hawkes process, the average increments of Nt_<sup>_i←_0</sup> _, Nt_<sup>_i←j_</sup> _and Nt_<sup>_i←j∗_</sup> _are expressed by_ 



The property above can be used in order to estimate the average fraction of events (directly or indirectly) caused by a specific component of a Hawkes process. Alternative notions of causality for point-processes have also been investigated. In particular, the notion of Granger-causality has been extended to point-processes in [57, 25]. 

19 

### **3 Univariate models** 

#### **3.1 Models of market activity and risk** 

The first straightforward application of Hawkes processes in high frequency finance is probably to model the so-called volatility clustering phenomenon. Since volatility at the transaction level can be directly related to the number _NT_ of a given type of events (trades, mid-price changes,...) that occur in a given time interval of size _T_<sup>6</sup> , the self-exciting nature of Hawkes processes provides a very simple picture that can explain the correlated nature of volatility fluctuations. This idea was first proposed by Bowsher [15] who calibrated a univariate Hawkes model with mixture of exponential kernels using intraday equity data from NASDAQ and NYSE<sup>7</sup> . 

In Ref. [2], Bacry _et al._ recently introduced a non-parametric estimation method for multivariate symmetric Hawkes processes based on the spectral factorization of the covariance matrix by the means of the Hilbert transform. By calibrating a 1- dimensional Hawkes model to the occurrence of trades of the 10 years Euro-Bund future front contract over 75 trading days in 2009, they discovered two important empirical facts: (i) the model is very close to its stability threshold _||_ Φ _||_ = 1 and (ii) the empirical kernel Φ( _t_ ) is very well described, over a wide range of scales, by the power-law function Eq. (9) 



with _γ ≃_ 0. The first observation directly concerns the level of endogeneity and the one of stability of financial markets, a problem, as discussed in the next section, that has been addressed afterwards by Filimonov and Sornette or Hardiman _et al._ [31, 32, 34, 35]. The power-law nature of Hawkes kernels with an exponent _γ ≃_ 0 has been confirmed by studies that followed, notably by Hardiman _et al._ on midprice changes of E-mini S&P500 futures [34] or by Bacry and Muzy on trades arrivals of EuroStoxx index futures [8]. The plots of Fig. 6 are directly extracted from these papers: they represent in log-log scales the estimated Hawkes kernel for the E-mini SP futures mid-price change events and the EuroStoxx market order occurrences. One can see that the two estimated kernels, corresponding to different data, different markets and different estimation methods, are strikingly similar. This suggests some universality of both _γ_ and _C_ = _αβ_<sup>_−γ_</sup> parameters in the algebraic decay of Eq. (63). 

The origin of this power-law behavior and, in particular, of the values of _α_ and _γ_ remains an open question. Previous empirical results motivated the work by Jaisson [41] (see also Ref. [7] and the section preceding Eq. (35)), who proved that, within a particular asymptotics (which includes the _L_<sup>1</sup> norm of the kernel converging to 1), a 1-dimensional kernel with a power-law decay with an exponent 1 + _γ_ (with _γ ∈_ ]0 _,_ 0 _._ 5[) leads to an auto-covariance function of the flow which is power-law with an exponent 1 _−_ 2 _γ_ , i.e., to a long-range dependence of the flow (see also the discussion in Sec. 2.3, Eq. (34)). The algebraic decay of Hawkes kernels can then 

> 6One can have in mind a simple price model where the price is build as the sum of independent random shocks. In this case, the volatility at scale _T_ is proportional to ( _NT_ )<sup>1</sup><sup>_/_2</sup> . The empirical results of Ref. [68] corroborate empirically this observation, allowing one to establish more precisely of the relation among impact per trade and volatility. 

> 7More precisely Bowsher considered a generalization of Hawkes processes in order to account for the peculiar non-stationarities observed at high frequency like intraday seasonalities and overnight gaps. 

20 



<!-- Start of picture text -->
Kernel comparison<br>10 2<br>10 1<br>10 0<br>10 − 1<br>10 − 2<br>10 − 3<br>E-mini (1998)<br>10 − 4 E-mini (2006)<br>E-mini (2009)<br>FXSE<br>10 − 5<br>10 − 3 10 − 2 10 − 1 10 0 10 1 10 2 10 3<br>Time t [s]<br>1[s]KernelΦ −<br><!-- End of picture text -->

**Figure 6:** Inferred kernel Φ( _t_ ) of the univariate Hawkes process describing midpoint changes of the E-mini S&P500 and for the trade arrivals of the EuroStoxx in different years, reproduced respectively from Refs. [8] and [34]. Strikingly, considering the different markets, traded contract, type of events considered, and periods of time considered in these studies, the shape of Φ( _t_ ) is almost identical. 

be related to the volatility clustering properties. Notice that within trading time models [14], the long-range nature of offer and demand has been mostly explained in terms of order splitting dynamics, and is supported by empirical results such as [66], in which broker-resolved data is analyzed in order to distinguish among the herding and splitting components of the order flow. It is thus likely that the observed slowly decreasing nature of the kernel directly results from the splitting of the meta-orders. Such an hypothesis remains however to be supported by quantitative arguments and to be confirmed by empirical observations. Beyond these fundamental questions, the power-law nature of Hawkes kernels remains a solid empirical fact which, at least, calls to question all the approaches based on exponential Hawkes models. 

In the same lines of the previously cited studies, Da Fonseca and Zaatour [21], perform a parametric estimation (using a GMM approach, see Sec. C.1) of a 1- dimensional Hawkes process with exponential kernels of the form _αβ_ exp( _−βt_ ) on (unsigned) market-order flow data. As expected, market-order clustering translates in a rather low value for _β ∈_ [0 _._ 02 _,_ 0 _._ 1] (depending on the financial time-series) and the _L_<sup>1</sup> norm of the kernel is found to be very close to criticality, i.e., _α ≥_ 0 _._ 9 (and very often _≥_ 0 _._ 95). One can also cite the work of Lallouache and Challet [45], who performed a maximum likelihood estimation on market orders using a sum of two exponential functions as the Hawkes kernel. They study forex EBS data which are throttled (market orders are gathered within slices of 0.1 seconds) which calls for a rather complex denoising preprocessing. Using goodness of fit tests, they conclude that, though the model performs well when applied to a 1 hour specific intraday 

21 

time (averaged every day over 3 months), the intraday seasonality of (mainly) the exogenous intensity _µ_ does not allow to fit well a whole day. 

Hawkes processes have also been used to model extreme price moves at a rather low frequency. In Ref. [27], Embrechts _et al._ study an equally weighted portfolio of 3 indices (Dow Jones, Nasdaq and SP) on an hourly time-frame (on 14 years). Only extreme quantiles of returns are kept (the smallest and the largest 1% quantiles) leading to a 1-dimensional point process whose jumps correspond to an extreme return of any of the three indices. The jumps are then marked using a 3-dimensional marks coding the excess of each index respect to the corresponding 1% quantile. The so-obtained point process is modeled using a 3-dimensional Hawkes process (with an exponential kernel) marked by 3-dimensional Gamma-distributed i.i.d. random variables. A maximum likelihood estimation is performed and goodness of tests show that this model is well suited for modeling extreme price moves. Let us point out that, in the same work, a very similar experiment is performed on daily logreturns of an (home-made) index of stocks using this time a 2-dimensional Hawkes process (for coding positive or negative extreme jumps) with 1-dimensional marks. In the same spirit, in Ref. [18], Chavez-Demoulin and Mc Gill constructed a model for the excesses of an asset price above a given threshold. This model combines a Hawkes process for the excess occurrences with Pareto distributed marks to the excess sizes. Within this approach, the author’s goal was to describe the clustering of large drawdown events through the self-excited dynamics of the Hawkes process. By performing backtests on equities intraday data, they have shown that this model captures very well extreme intraday events, notably as compared to standard nonparametric methods based on extreme value theory. 

#### **3.2 Measuring the endogeneity of stock markets** 

In a recent series of papers [31, 32, 34, 35], some authors addressed, within the framework of Hawkes models, the important problem of the so-called “ _volatility puzzle_ ”, namely the fact that the observed market volatility cannot be explained by classical economic theory. Indeed, it is well known that prices move too much compared to the flow of pertinent information that may impact the market. This observation naturally leads to the idea that price dynamics is highly endogenous, i.e. mainly driven by some internal feedback mechanisms. Filimonov and Sornette [31] were the first to propose a quantitative measure of the level of “market reflexivity”. For that purpose, they model the high frequency mid-price variations of some stock index (namely the E-mini S&P500) as a 1-dimensional Hawkes process. As explained in Sec. 2.3.8, _||_ Φ _||_ can be interpreted as a branching ratio, i.e., the number of events generated by any parent event. Each exogenous event occurring at rate _µ_ thus generates _||_ Φ _||/_ (1 _−||_ Φ _||_ ) events and therefore the ratio of endogenous event rate to the overall rate Λ in one dimension is, according to Eq. (21), 



This means that _||_ Φ _||_ provides a direct measure of the fraction of endogenous events within the whole population of mid-price changes and thus a measure of the market reflexivity. By analyzing the E-mini S&P500 future contracts over the period 1998-2010, Filimonov and Sornette found that the degree of reflexivity has strikingly increased during the last decade. They suggested that this effect could be directly 

22 

caused by the increasing amount of high frequency and algorithmic trading, raising the question of the impact of high frequency trading on the market stability. This analysis has been revisited by Hardiman, Bercot and Bouchaud [34] who noticed that Filimonov and Sornette estimation relying on an exponential parametrization is biased because, as discussed previously, empirical evidences suggest that Hawkes kernels have a slow (power-law) decay. Accounting for this feature on their estimation of _||_ Φ _||_ , Hardiman _et al._ found that the reflexivity of the E-mini S&P future hasn’t been increasing during the last decade, but has remained constant at a value very close to the critical one _||_ Φ _||_ = 1. It is noteworthy that Hardiman _et al._ also provided, in their study, empirical evidences of the existence of a high frequency cut-off of the Hawkes kernel (namely the parameter _β_<sup>_−_1</sup> in Eq. (63)) that decreases exponentially fast in time and that can be associated with the increase of the trading frequency. In a more recent paper, Filimonov and Sornette [32], have reviewed all the pitfalls associated with the estimation _||_ Φ _||_ in the case of a slowly decreasing kernel. They have shown that significant biases can be induced by the presence of outliers, edge effects or non stationary effects. Because some important issues are also related to the way one parametrizes the model (notably the choice of the high-frequency regularization), Hardiman and Bouchaud [35] proposed a simple non-parametric approximation of the branching ratio _||_ Φ _||_ that relies on Eq. (23). Indeed, by considering this equation in _z_ = 0, it is possible to relate the integral of the correlation function, _c_ ˆ(0) to _||_ Φ _||_ . The number of events _NT_ in a window of size _T_ , becomes, for _T_ large enough, _c_ ˆ(0) _≃ T_<sup>_−_1</sup> V [ _NT_ ] and therefore one gets 



This formula leads to a very intuitive interpretation of the degree of reflexivity: The occurrence of correlated events implies an increase of the variance of _NT_ with respect to its mean value (for a Poisson process, both quantities are equal so that one directly gets _||_ Φ _||_ = 0). Using this model free estimator, Hardiman and Bouchaud [35] have confirmed their former claims that the S&P 500 future appears to have, during the last ten years, a stable level of reflexivity, close to the criticality. Let us notice that this formula only holds for 1-dimensional Hawkes processes and has no simple extension in the multivariate situation. 

Beyond the debate on the most suitable estimator for the reflexivity parameter and its genuine behavior, the pioneering work of Filimonov and Sornette provided a quantitative framework allowing to study the endogeneity of market fluctuations with Hawkes processes. They notably have shown that such approach can be used to study particular events such as the flash crashes of April and May 2010 [31]. Their results may be helpful to devise warning tools in order to anticipate extreme drawdowns which are of endogenous origin. The prospects and applications along this path are numerous. One important question concerns the extension of such studies by accounting other types of events like e.g. order book events (see Sec. 6). 

### **4 Price models** 

Describing the fluctuations of price at the finest time scales, with notably the goal of improving volatility and covariance estimations, is a central issue of financial econometrics. The notion of microstructure noise was considered by many authors 

23 

as an additional noise, superimposed to the standard diffusion, that accounts for the small scale behavior of the signature plot. Indeed, it is well know that the signature plot 



that corresponds to the quadratic variation of the mid-price _Pt_ at scale _τ_ , strongly increases when _τ →_ 0 (see Fig. 7). Along the same line, the so-called Epps effect accounts for the vanishing covariation among the returns of pairs of assets when the return scale _τ_ goes to zero. Bacry _et al._ in [3] proposed as an alternative to standard “latent price” models, to directly account for the discrete nature of price variations. They have been the first ones to describe the tick-by-tick variation of the mid-price, _Pt_ , within the framework of Hawkes processes. In order to do so, these authors considered the two counting processes _Nt_<sup>1and</sup><sup>_N_</sup> _t_<sup>2associatedwithrespectivelythe</sup> arrival times of upward and downward price changes and set: 



where the couple ( _Nt_<sup>1</sup><sup>_, N_</sup> _t_<sup>2)isa2-dimensionalHawkesmodel.Since,inafirstap-</sup> proximation, the dynamics of the upward moves and of the downward moves are expected to be the same, it is natural to consider a matrix kernel Φ as the one considered in Eq. (5) with equal diagonal terms _φ_<sup>(</sup><sup>_s_)</sup> ( _t_ ) and anti-diagonal terms _φ_<sup>(</sup><sup>_c_)</sup> ( _t_ ). It is well known that, at the microstructure level, the price is essentially mean reverting, thus in [3], the authors considered the “purely mean-reverting scenario”, i.e., the case where _φ_<sup>(</sup><sup>_s_)</sup> ( _t_ ) = 0 and chose for _φ_<sup>(</sup><sup>_c_)</sup> ( _t_ ) an exponential shape. Within this simple framework, Bacry _et al._ provided a closed-form expression for the signature plot. Calibrating the model using MLE or GMM estimations on Euro-Bund and Euro-Bobl future data, they have shown that the model is able to reproduce the scale behavior of the signature plot (see Fig. 7). Bacry _et al._ also considered a natural extension of the previous model to a 4-dimensional Hawkes model in order to describe the joint mid-price dynamics of a pair of assets and to reproduce the Epps effect [3]. Let us recall that, in Ref. [4], the authors established that under general conditions, the empirical covariation of a multivariate Hawkes process converges towards its expected value, that can be easily expressed in terms of the Hawkes covariance matrix _c_ ( _t_ ) as given by Eq. (23). This result allows one, within the Hawkes price model of Bacry _et al._ , to provide analytical expressions for the signature plot, lead-lag behavior and the Epps effect in terms of Hawkes matrix kernel Φ [3, 4]. Let us also mention that, along the line the of previous model, in [21], the symmetric case was considered, i.e., the “purely trend following scenario”: _φ_<sup>(</sup><sup>_s_)</sup> ( _t_ ) = 0 and _φ_<sup>(</sup><sup>_c_)</sup> ( _t_ ) exponential shape. The authors compared this scenario with the “purely mean-reverting scenario” when used for daily volatility estimation using diffusive formula (53). They showed that the mean-reverting (resp. trend-following) scenario underestimates (resp. over-estimates) the volatility and concluded that a “full” model with both cross and self terms is more realistic and should lead to better volatility estimation. Let us notice that the existence of non-negligible diagonal and anti-diagonal terms has been confirmed by non-parametric estimations performed thereafter in [2, 7, 6]. 

One also expects the involved kernels not to be exponential functions. Indeed, as shown in many works, (e.g., in Ref. [2]) and as discussed previously in Sec. 3.1, empirical self-exciting kernels are closer to a power-law than to an exponential. It 

24 



<!-- Start of picture text -->
Fitted<br>0 . 04<br>Empirical<br>0 . 035<br>0 . 03<br>0 . 025<br>0 50 100 150 200<br>τ [seconds]<br>() Cτ<br><!-- End of picture text -->

**Figure 7:** Reproducing the mid-price behavior at the microstructural level using Bacry _et al._ 2-dimensional Hawkes model. The plots represent the Euro-Bund empirical signature plot as compared to its fit within the model of Bacry _et al._ . The figure has been reproduced from Ref. [3] 

is with that consideration in mind that Jaisson and Rosenbaum [42] developed the diffusive framework that we have already described in second part of Sec. 2.3.6. It is an alternative framework to the more classical Brownian motion diffusive framework developed in the first part of the same Section. In the second part of their paper, Jaisson and Rosenbaum used their framework to build a version of the 2-dimensional Hawkes model initially introduced by [3] that converges at large scales towards the Heston price model [39] which displays volatility clustering. This work can be seen as the very first step towards a “across scales” unified model that would fit both microstructure stylized facts of price (i.e., point process with strong mean reversion) and “diffusive” stylized facts (volatility clustering and multifractality). In that sense this is a very promising work. 

We can also mention a very interesting generalization of the model introduced by Bacry _et al._ in [3]. In [69], Zheng _et al._ introduced a model for the coupled dynamics of the best bid and ask prices. It starts by coding each best price using the Bacry _et al._ model leading to a 4-dimensional price model. The main difficulty comes from the fact that one needs to encode in the model the fact that the ask price needs to lie strictly above the bid price. This is achieved through a spread point process whose dynamics is coupled with the dynamics of both best prices. It is used to measure the distance (in ticks) between the ask price and the bid price: the spread is increased (resp. decreased) by 1 each time either the ask (resp. bid) component jumps upward (resp. downward) or the bid (resp. ask) component jumps downward (resp. upward). Finally a non-linear term is introduced in the Hawkes model: the intensities of the downward (resp. upward) jumps of the ask (resp. bid) price are set to 0 as soon as the spread process is equal to 1. The authors of [69] developed a whole new rigorous framework for this constrained, non-linear Hawkes model in which they were able to establish several properties (including a diffusive limits). They perform maximum likelihood estimation on real data (using exponential kernels) and show that they were able to reproduce rather well the signature plot. 

25 

Let us finally cite the work of Fauth and Tudor in [30] where the authors proposed to describe bid and ask prices of an asset (or a couple of assets) within the framework of marked multivariate Hawkes model. Motivated by the empirical observation (performed on high-frequency Euro/USD and Euro/GPB FX rates from 30-01-2012 to 10-03-2012) that, as the transaction volumes increase, the inter-trade durations decrease, the authors proposed to consider, in addition to an exponential Hawkes kernel, a multiplicative mark (the function _χ_ in Sec. 2.2.1) that corresponds to a power-law function of the volumes: _χ_ ( _v_ ) = _Cv_<sup>_ν_</sup> . Their model thus describes the events corresponding to an increase/decrease of the bid/ask as a four dimensional Hawkes process marked by transaction volumes. By adding suitable constraints in order to avoid infinite spread, they calibrated the model on FX rates data by a maximum likelihood approach. Fauth and Tudor have shown that their model is consistent with empirical data by reproducing the signature plots of the considered assets and the behavior of the high-frequency pair correlation function (Epps effect). 

### **5 Impact models** 

#### **5.1 Market impact modeling** 

Market impact modeling is a longstanding problem in market microstructure literature and is obviously of great interest both for theoreticians and practitioners (see e.g., [13] for a recent review). While for the former market impact reflects the mechanism enforcing the efficiency of markets, allowing prices to reflect fundamental information, for the latter it represents a cost which needs to be carefully minimized when executing an order. For a trader, market impact induces extra costs per transaction which needs to be added to the fees charged directly by the market, forcing him to split large orders and trade them incrementally in sequences of smaller child orders. Any of such sequences of orders is called a _meta-order_ , and quantifying their effect on prices is at the heart of market-microstructure regulation discussions. 

The theory of market price formation and the relationship between the order flow and price changes has made significant progress during the last decade thanks to the increasing availability of intraday data [14]. Many empirical studies have provided evidence that the price impact has, to many respects, some universal properties and is the main source of price variations. This corroborates the picture of an “endogenous” nature of price fluctuations that contrasts with the classical scenario according to which an “exogenous” flow of information drives the prices towards a fondamental value [14]. 

If a meta-order is placed at time _t_ = 0 and executed until time _t_ = _T_ , an associated market impact curve can be defined by a proxy of the price variation it directly or indirectly causes<sup>8</sup> . One generally distinguishes two phases: an increasing (concave) part during the execution of the meta-order (i.e., on the interval [0 _, T_ ]), followed by a decaying (generally convex) resilient part. The existence of permanent impact, i.e., a non zero asymptotic value (for large time) of the market impact curve, is a central problem that remains under debate. The typical shape of a market impact curve is shown in Fig. 8, that was was obtained by Bacry _et al._ in [5] by averaging empirical impact curves over a large database of broker meta-orders. Let 

> 8We focus here on the impact of meta-orders, rather than with the impact of individual orders, or with the one of trade imbalance, which have also received considerable interest in the literature. 

26 

us point out that this type of measure of market impact cannot be obtained using anonymous market data (i.e, one cannot easily identify the meta-order of a given agent). This, together with the extremely slow intensity of the price signal with respect to its statistical fluctuations, is the reason why empirical results in this respect have been obtained only in relatively recent years. 



<!-- Start of picture text -->
10<br>5<br>Fitted<br>Empirical<br>0<br>0 0 . 5 1 1 . 5 2<br>t/T<br>[]E P 0 t −<br><!-- End of picture text -->

**Figure 8:** Averaged empirical market impact curves (normalized in time) over a large database of broker meta-orders. The fit is performed using the impulsive HIM model. This figure has been reproduced from [5]. 

Bacry and Muzy proposed recently a price impact model based on Hawkes processes [7]. They suggested to directly account for the joint dynamics of mid-price and the market order occurrences. More precisely the four dimensions of their Hawkes model correspond to the mid-price upward and downward jumps and the buying and selling market order flow (they did not account for the volume of the orders nor the price jump sizes). The matrix kernel Φ can then be decomposed into four sub-blocks of size 2 _×_ 2. The first one describes the self-excitement of the market order flow, the second one the self-excitement of the price, the third one the (market) impact of the trades on the price while the last one accounts for the feedback influence of price moves on market order flow intensity. By calibrating the model directly from anonymous high-frequency data (using the Wiener-Hopf non-parametric estimation technique described in App. C.2 on the most liquid maturity of EuroStoxx and EuroBund future contracts over 800 trading days from 2009 to 2012), the authors of [7] were able to disentangle the self and cross excitation dynamics of mid-price changes from the impact of market orders. In particular, they have shown that the market impact block is mainly diagonal: buying (resp. selling) orders are mostly triggering upward (resp. downward) price moves. Moreover the shape of the diagonal impact function is very localized around _t_ = 0. This means that a market order no longer directly impacts the price after a very short delay (i.e. less that 0.1 _s_ ). They have also shown that the feedback sub-block is mostly anti-diagonal with slightly negative diagonal kernel functions (see Sec. 2.2.4 for a short discussion on negative kernels). That indicates that an upward (resp. downward) jump in the price tends to increase the intensity of the selling (resp. buying) market order flow and to decrease the intensity of the buying (resp. selling) market order flow. The shape of kernels in- 

27 

volved in the self-excitation of the market order flow or the price jumps confirms former estimations performed within lower dimensional models: long-range correlation of the signs of the trades and mainly long-range mean-reversion of the price. All these results were confirmed (using a database with a much higher precision in time) in the work of [6] (see Sec. 6.1). Bacry and Muzy established that, within their framework, it is possible to determine the entire impact profile of some meta-order that is built by accounting for the “bare” direct localized marked impact and by a “dressed” impact that involves mainly the trades power-law self-excitation. They provided analytical expressions for this curve and notably established in both the increasing and the decreasing phase of the impact function, its relationship with the power-law behavior of the self-exciting kernel of market order events. Using the previously described empirical findings, they have shown that one can recover the typical shape depicted in Fig. 8. 

In [5], an impact model based on the 2-dimensional Hawkes price model described in Example 1 of Sec. 2.1 (in which only mean-reversion influence has been kept, i.e., _φ_<sup>(</sup><sup>_s_)</sup> ( _t_ ) = 0) has been introduced. It takes into account the impact of an exogenous (buying) meta-order strategy _r_ ( _t_ ), where _r_ ( _t_ ) corresponds to the trading rate of the (buying) strategy per unit of time (so _r_ ( _t_ )d _t_ corresponds to the number of shares bought between time _t_ and _t_ + d _t_ ). More precisely, the so-obtained Hawkes Impact Model (HIM) writes 



where d _Nt_<sup>1(resp.d</sup><sup>_N_</sup> _t_<sup>1)codestheupward(resp.downward)jumpsofthepriceand</sup> _f_ ( _r_ ( _t_ )) _dt_ (with _f_ (0) = 0) codes the infinitesimal impact of a buy order of volume _r_ ( _t_ ) _dt_ . The function _f_ corresponds to the _instantaneous_ impact function and _φ_<sup>(</sup><sup>_I_)</sup> and _φ_<sup>(</sup><sup>_x_)</sup> correspond respectively to the impact kernel and the cross-impact kernel (this latter describes the impact of a buying order on downward jumps, of course, we expect that _||φ_<sup>(</sup><sup>_x_)</sup> _|| << ||φ_<sup>(</sup><sup>_I_)</sup> _||_ )<sup>9</sup> . Following the empirical findings of [7], the impulsive-HIM model corresponds to the particular choice of an impulsive (very localized) impact kernel _φ_<sup>(</sup><sup>_I_)</sup> ( _t_ ) = _δ_ ( _t_ ), i.e., a Dirac distribution. Moreover, as for the choice of _φ_<sup>(</sup><sup>_x_)</sup> , the impulsive-HIM model considers that the market reacts to the newly arrived order as if it triggered an upward jump: _φ_<sup>(</sup><sup>_x_)</sup> ( _t_ ) = _C_<sup>_<u>φ</u>_(</sup><sup>_s_)(</sup><sup>_t_</sup><sup><u>)</u></sup> _||φ_<sup>(</sup><sup>_s_)</sup> _||_<sup>.The</sup> constant _C >_ 0 is a very intuitive parameter that quantifies the ratio of “contrarian” reaction (i.e. impact decay) and of the “herding” reaction (i.e. impact amplification). Analytical formula for the market impact curve were obtained and three cases of interest for _C_ were distinguished in [5]: _C_ = 0 corresponds to no contrarian reaction (strong permanent impact), _C_ = 1 corresponds to a contrarian reaction as “strong” (in terms of the norm) as the herding one (no permanent impact) and finally _C ∈_ ]0 _,_ 1[ corresponds to a contrarian reaction which is not zero but strictly smaller than the herding reaction. Fig. 8 shows a fit of the empirical market impact curve using this model with a power-law microstructure kernel ( _φ_<sup>(</sup><sup>_s_)</sup> ( _t_ ) _∼ t_<sup>_−γ_</sup> , when _t →_ + _∞_ ), in which case, the market impact curve is proven to be decaying to the permanent market impact value with a power-law _t_<sup>_−_(</sup><sup>_γ_+1)</sup> . 

Let us point out, that in a totally different framework, Jaisson [41], linked, in the asymptotic limit defined by Jaisson and Rosenbaum in [42] (see Sec. 2.3.6), the power-law exponent of the self-excitement kernel involved in the market order flow and the power-law exponent of the market impact decay. He derived his results, 

> 9As for ( _s_ ) and ( _c_ ), ( _I_ ) stands for _impact_ and ( _x_ ) for _cross-impact_ . 

28 

within a 2-dimensional Hawkes model (with only self-excitement kernels) for the market order flow, from (i) a price martingale hypothesis and (ii) a linear market impact hypothesis. 

#### **5.2 Optimal execution** 

A natural application of price impact models is to define optimal liquidation strategies. Hewlett [40] was the first to address this problem using Hawkes models. He proposed to model the occurrence of buy and sell market orders on FX markets using a bivariate exponential Hawkes process. He found that these events are mostly self-excited, the cross excitation intensity between buy and sell events being negligible. Using Eq. (47), Hewlett determined the expected future trade imbalance that, within a linear price impact model, allows one to determine the expected future price returns and the associated risk. He then showed that this approach allows one to devise a liquidation strategy that maximizes a mean-variance utility function. 

Application of Hawkes model for optimal execution has also been considered more recently by Alfonsi and Blanc [1] who modelled the price process using a linear impact of liquidity takers. More precisely, the price is decomposed a the sum of a “fundamental” price which variations are proportional to a fraction of the trade imbalance and a “transient” price that is moved by the remaining fraction of the trade imbalance but with a damping term that represents the market resiliency caused by the market makers behavior. Alfonsi and Blanc have provided explicit expressions of optimal liquidation strategy (i.e. the one with the minimum expected cost) when the flow of buy/sell market orders that impact the price is either a Poisson process or a 2-dimensional Hawkes process with a symmetric exponential kernel matrix. They notably show that price manipulation strategies (i.e. liquidation strategies with negative expected cost) always exist for a Poisson model while they can be excluded in the Hawkes model provided its parameters meet some specific conditions. According the these conditions, the self-excitation should exactly compensate the price resiliency so that resulting price is a martingale. The other condition leads to identify the fraction of endogenous orders within the Hawkes model with the proportion of market orders involved in the transient part of the price behavior. 

### **6 Orderbook models** 

Modeling faithfully the occurrence of various type of orders in the order book with the aim of understanding the mechanisms at the origin of price formation, volatility and liquidity variations is probably the main challenge that the applications Hawkes processes in financial econometrics have to face. Although this goal is far from being reached, some authors have already tackled the problem and made significant progress on these issues. 

#### **6.1 Level-I book models** 

The Level-I book description concerns the events that exclusively occur at the best bid and best ask levels of the order book. Even if this approach discards most of the book information, since best bid or best ask values are directly related to the asset mid-price and market orders mostly impact the book at level-I, one can expect that this level of description is rich enough to capture most of the market features. The 

29 

study of Biais _et al._ [11] confirms indeed that most of the activity of an order book takes place close to the best quotes, while Cont _et al._ [19] indicate that a substantial part of the dynamics of prices can be accounted for by the evolution best bid and best ask only. 

One of the first applications of Hawkes models to order-book modeling at level-I was performed by Large [46] who formalized the concept of book resiliency, namely the ability of the order book to replenish after being depleted by a large trade. Large suggested to quantify resiliency by the way large trades alter future intensities of order occurrences. For that purpose he introduced the response kernel _G_<sup>_ij_</sup> ( _t_ ): 



_G_<sup>_ij_</sup> ( _t_ ) simply describes the increase of the future conditional intensity of events of type _i_ caused, directly or indirectly, by the the occurrence, at time _t_ = 0 of an event of type _j_ . In the case of a Hawkes process of kernel matrix Φ, Large proved that _G_<sup>_ij_</sup> satisfies the integral equation in Eq. (17) defining Ψ( _t_ ). In other words, the matrix Ψ( _t_ ) can be interpreted as the increase of the expected number of events after a lag _t_ caused by the occurrence of some event at time 0. Large then considered order book data from LSE, modeled as a 10-dimensional Hawkes processes where the book events are classified according to whether they move or not the mid-price: market and limit orders that move the mid-prices (4 components if one distinguishes bid and ask), market and limit orders that leave the book unchanged (4 components) and cancel orders (2 components). The impact of “aggressive” orders on the rate of forthcoming events is then studied. The processed data consisted in LSE stock data (Barclays equity) timestamped at the resolution of 1 _s_ during the 22 trading days of January 2002. Large used MLE estimation within the class of exponential kernels in order to estimate Ψ. His results allowed him to provide a “causal” interpretation (Large prefers the term “precipitation” than “cause”) of the main event occurrence in the book. He mainly found that aggressive limit orders are principally caused by aggressive market orders, measuring thereby the market resiliency in all his aspects, magnitude, trade direction and characteristic time. Consistently with former studies, Large estimated that the studied stock value is resilient less than 40 % of cases and, when it is the case, the book replenishment occurs within a time frame of around 20 _s_ . He also shown that market order dynamics is mostly self-excited and correlated over a large time. Aggressive market orders are also triggered by aggressive limit orders as a consequence of the “race to liquidity”. 

A similar analysis of level-I order book data was recently conducted by Bacry _et al._ [6]. These authors made a slightly different categorization than Large and distinguished all book events (market, limit and cancel orders) that leave the midprice unchanged (6 components accounting for bid and ask sides) from events that move the mid-price up or down (2 components). The dynamics of these event occurrence has then been modeled as a 8-dimensional Hawkes process. Unlike Large, Bacry _et al._ performed a non-parametric estimation of the matrix of kernels using the method described in Sec. C.2. They considered book data time-stamped at a time resolution of 10<sup>_−_6</sup> _s_ and the analysis has been performed up to lags of a few minutes. The event dynamics has thus been considered over a range of time scales close to eight decades. The main result reported by the authors is that the book event dynamics is mainly self-exciting, except for the mid-price changes for which cross-excitation effects are strongly dominating. This is illustrated in Fig. 9 

30 

where the values of the estimated kernel norms are reported using a color map: one can see that the resulting matrix is mainly diagonal except in the price subblock, that is anti-diagonal. The observation that price changes events are mainly 



<!-- Start of picture text -->
BUND DAX<br>1.0<br>P ( a ) P ( a )<br>0 . 8<br>P ( b ) P ( b )<br>0 . 6<br>T ( a ) T ( a )<br>0 . 4<br>T ( b ) T ( b )<br>0 . 2<br>L ( a ) L ( a )<br>0<br>L ( b ) L ( b )<br>− 0 . 2<br>C ( a ) C ( a )<br>− 0 . 4<br>C ( b ) C ( b )<br>− 0 . 6<br>P ( a ) P ( b ) T ( a ) T ( b ) L ( a ) L ( b ) C ( a ) C ( b ) P ( a ) P ( b ) T ( a ) T ( b ) L ( a ) L ( b ) C ( a ) C ( b )<br><!-- End of picture text -->

**Figure 9:** Empirical determination of the matrix of Hawkes kernel norms in the 8-dimensional model of level-I book events. _P_ stands for mid-price change events, _T_ for trade events, _L_ for limit order events and _C_ for cancel events. The superscripts ( _a_ ) ( _b_ ) indicates the direction, ask or bid of the events. This figure is reproduced from [6]. 

triggered by price change events is in agreement of Large previously reported results. Moreover, Bacry _et al._ observations confirmed the previously reported empirical fact that this triggering effect is mostly anti-diagonal, i.e., present price changes impact future price changes in the opposite direction. Previous findings using lowdimensional model concerning the kernel shapes were also confirmed: the market is highly endogenous, whatever the type of event one considers and all the dominating kernels (the diagonal kernels for orders leaving the price unchanged and the antidiagonal kernels for mid-price moves) are slowly decreasing, well described by a power-law behavior as in Eq. (63). The richness of the Hawkes model of [6] allowed the authors to account for a richer dynamical behavior than previous works and to describe and quantify the high-frequency influences between all types of events. They notably characterized the impact of price changes on the book event flow, a quantity that turns out to be very sensitive to the asset tick size (as estimated by the probability that the mid-price has to move). They also provided evidence of some inhibitory effects which result from negative values of some Hawkes kernels. For example it was observed that, for a large tick asset (like the Euro-Bund futures), an upward price move not only triggers forthcoming trades at bid but also inhibits trades on the ask side. 

Restricting previous Large model to market order flows at best bid and best ask, 

31 

Muni-Toke and Pomponio [56] studied the dynamics of trade-through orders. A market order is a trade-through if part of it is executed at the next best limit. Thus, for that purpose, they used the 2-dimensional Hawkes process (with exponential kernels) described by Eq. (53). Though very rare for some assets (e.g., Euro-Bund future), trade-through can be quite frequent on other contracts. For instance on the BNP stock [56] finds an average of 400 trade-throughs per day. Parametric estimation using MLE on exponential kernels have been performed on Euronext stocks restricting intraday-time to 9h30 to 11h30 am to avoid very strong intraday seasonality effects. Goodness of fit tests confirm that, as for the full market order flow, the main components of the 2-dimensional Hawkes kernel are the self-exciting kernel. 

#### **6.2 Full order book model** 

In [55], Muni Toke generalized the zero-intelligence model introduced in [64] to the Hawkes framework. While in the latter model the authors built a full model for the order book in which all the involved flows (i.e., limit and market orders at any level) are independent pure Poisson processes. It is clearly a very rough approximation, market orders are known to be long-range dependent (see Sec. 3.1) due to the splitting of large meta-orders. Moreover, one expect limit orders to be also highly auto-correlated as well as correlated with the market-order flow due to the fact market makers interact with market takers. In [55], a 2-agents model is introduced. It comprises the following agents: 

- A _liquidity provider_ : 

   - Arrivals of limit orders are modeled by using either a pure homogeneous Poisson process or a 1-dimensional Hawkes process with an exponential kernel (cancellations are treated as in the zero-intelligence model, i.e., each order has a life-time which is an i.i.d. exponential random variable using whose parameter is fixed a priori) 

   - The price-levels of new limit orders are randomly chosen by first choosing the (bid or ask) side with probability 1/2 and then by sampling their values from a Student distribution 

- A _liquidity taker_ : 

   - Modeled using either a pure homogeneous Poisson process or a 1-dimensional Hawkes process with an exponential kernel. 

All the volumes of both limit and market orders are i.i.d. and exponentially distributed variables. Hawkes processes use exponential kernels which are estimated parametrically using Maximum Likelihood Estimation. 

Not surprisingly, inter-trade times of market orders are shown to be much better modeled by a 1-dimensional Hawkes process (referred to as MM since the only Hawkes kernel involved is one which deals with the influence of Market orders on themselves) than by a pure Homogeneous Poisson process (HP). In the same way, inter-time of limit orders are shown to be much better modeled by a 1-dimensional Hawkes process (LL) than by HP. Along the same lines, the left panel of Fig. 10 shows that inter-time between a given market order and the first arrival time of a limit order after that market order is much better reproduced by a 2-dimensional Hawkes (referred to as MM+LL+LM) model with self-exciting kernels for both market (MM) and limit orders (LL) and a single cross-exciting kernel which corresponds to the influence of past market orders on future limit orders (LM). The figure shows that 

32 

33 



<!-- Start of picture text -->
0 . 7 0 . 35<br>Empirical Empirical<br>0 . 6 HP 0 . 3 HP<br>MM MM+LL<br>0 . 5 MM+LL 0 . 25 MM+LL+LM<br>MM+LL+LM<br>0 . 4 0 . 2<br>0 . 3 0 . 15<br>0 . 2 0 . 1<br>0 . 1 0 . 05<br>0 0<br>0 0 . 2 0 . 4 0 . 6 0 . 8 1 0 0 . 05 0 . 1 0 . 15 0 . 2<br>Time t Spread s<br>()Probabilitydensity tp ()Probabilitydensity ps<br><!-- End of picture text -->

**Figure 10:** (Left panel) Empirical density function of the distribution of the duration between a given market order and the first arrival of a limit order after that market order. The density function is displayed for empirical BNPP time-series, and for three different models that were fitted (using maximum likelihood) on these data, namely: a purely Homogeneous Poisson model (HP) for both market and limit orders, a model with a pure Poisson process for limit orders and a 1-dimensional Hawkes process for the market orders (MM), a model with two independent 1- dimensional Hawkes processes for limit and market orders (LL+MM) and finally this last model with a cross-exciting term which characterize the influence of past market orders on future limit orders (LM). (Right panel) Empirical density function of the distribution of the bid-ask spread. The density function is displayed for empirical BNPP time-series, and for three different models that were fitted (using maximum likelihood) on these data, namely: a purely Homogeneous Poisson model (HP) for both market and limit orders, a model with a pure Poisson process for limit orders and a 1-dimensional Hawkes process for the market orders (MM), a model with two independent 1-dimensional Hawkes processes for limit and market orders (LL+MM) and finally this last model with a cross-exciting term which characterize the influence of past market orders on future limit orders (LM). These figures are reproduced from Ref. [55]. 

a model with two independent Hawkes models (MM+LL) with no cross-exciting kernels (LM) does not perform well. In [55], Muni-Toke claims that the other crossexciting kernel (the one describing the influence of past limit orders on future market orders) is negligible. Thus the order book dynamics seems to be driven mainly by the liquidity taker agent rather than the liquidity provider, i.e., in a first approximation, the market makers strategy consists basically in reacting to liquidity takers, whereas liquidity takers take decisions independently from market makers. 

Finally the right panel of Fig. 10 shows the so-obtained distribution of the bid-ask spread for empirical data, the pure Homogeneous Poisson (HP) model, the MM+LL Hawkes model and the MM+LL+LM model. Again, this latter model is the one which best fits the empirical data. 

Let us mention a theoretical work by Jedidi and Abergel [43] in which a Hawkesbased markovian framework for the whole order-book dynamics is studied. 

### **7 Other models** 

#### **7.1 Systemic risk models** 

Hawkes models have been also be used at coarser time scales where asset prices are mainly diffusive. They can be used in mixed models in order, for instance, to account for jumps that occur over the diffusion process. This is the spirit of the model developed by A¨ıt-Sahalia _et al._ [63] that proposed to describe the contagion of a crisis across all the world markets by superimposing a multivariate self-excited Hawkes process to a standard multivariate continuous diffusion model. According to this model, called be the authors, “Mutually exciting Jump-Diffusion”, the log-price vector satisfies: 



where _Wt_ is a _D_ -dimensional Brownian motion, _σt_ is a stochastic volatility and _Nt_ is a _D_ -variate Hawkes process that accounts for the self-excited nature of price jumps occurrence ( _Zt_ is a random variable accounting for the direction and the intensity of the jump). A GMM estimation procedure is proposed in [63] based on a closed-form expressions of some moments associated with the returns variations in the univariate and bivariate cases with exponential Hawkes kernels. This estimation has been applied to five international equity indices data associated with respectively US, Europe, Asian, Pacian and Latin America zones. The authors found that the jumps terms have significant self-excitation components and as far as the “contagion” effect is concerned, it seems that the US equities are the ones with the greatest influence on other markets. 

In Ref. [29], Errais _et al._ proposed to model credit default events in a portfolio of securities as correlated point processes. More specifically they considered that the dynamics of such events is described by a marked Hawkes process with exponential kernels. A stated by Prop. 2, in this case, the couple of processes ( _λ, N_ ) is a Markov process. Thanks to the Dynkin formula, the authors provided explicit expressions for the conditional distribution of both the marked and counting processes. This result was used to price portfolios if credit derivatives such as index and tranch swaps. Their model was then calibrated from index and swap data during September 2008 that witnessed several credit default notably Lehman-Brothers default. The authors have shown that by, capturing the dependence of default events, their model provided 

34 

good fits of market data, unlike standard approaches that failed during this period. Errais _et al._ emphasized that marked Hawkes models with exponential kernels belong to the more general class of affine point processes introduced by Duffie _et al._ [26]. An affine point process involves a stochastic intensity vector which is a Markov process with drift, diffusion and jump terms. Errais _et al._ [29] have shown that their approach remains tractable within the class of affine point processes that provides a richer jump interaction structure. 

Let us also quote the recent similar work of Dassios and Zhao [23] who addressed the question of default risk modeling and contagion propagation within the framework of the so-called “Dynamic Contagion Process” that is an exponential marked Hawkes model but where the Poisson exogenous events (the “immigrants”) are replaced by a shot-noise (constructed as the first generation of the same exponential Hawkes model with a different mark probability density). The authors have established the theoretical distributional properties of this new process (that remains a Markov process) and provided analytic expressions for the its probability generating function. As in Errais _et al._ [29], they showed that their approach is particularly suitable for modeling the dependence structure of arriving events with dynamic contagion and proposed an application to credit risk, 

#### **7.2 Accounting for news** 

In [61], Rambaldi _et al._ used Hawkes processes for modeling the impact of news on the EBS (foreign exchange market) quotation time-series, consisting in a list of quotation timestamps. Let us note that, since EBS data are throttled (aggregated below a window of 0.1 _s_ ), a randomization procedure has been used for homogenization. The model for the quotation arrival times is a 1-dimensional Hawkes model involving either a double exponential or a power-law (expressed as a sum of 15 exponentials so to have a convenient Maximum Likelihood Estimation procedure). The impact of the news (on the quotation time-series) can be seen as particular instances of localized non stationarities. Thus, Rambaldi _et al._ introduced an exogenous kernel _φ_<sup>(</sup><sup>_news_)</sup> (an exponential function) that accounts for the impact of a particular instance of a news, leading to the model<sup>10</sup> : 



where _t_ 0 is the time of occurrence of a particular news. Let us point out that _φ_<sup>(</sup><sup>_n_)</sup> (where ( _n_ ) stands for _news_ ) is allowed to have a non-causal component (i.e., _φ_<sup>(</sup><sup>_n_)</sup> ( _t_ ) is non zero for _t <_ 0) in order to account for anticipation effects. Estimation is performed (using regular Maximum Likelihood Estimation procedure) on a 3 hour period around the considered news. Though the results are very noisy, the authors showed that the model captures nicely both the amplitude and the time scale of the news effect. The distribution of the _L_<sup>1</sup> norm _||φ_<sup>(</sup><sup>_n_)</sup> _||_ for the different news has broad distribution (that goes beyond 1) that clearly reflects the diverse effects of news on the market. Moreover, using some proxies for quantifying how unexpected a particular news is, Rambaldi _et al._ clearly showed that the norm _||φ_<sup>(</sup><sup>_n_)</sup> _||_ is not only related to the news impact but also to its degree of surprise. 

> 10Formally, this model can be seen as a 1-dimensional version of the 2-dimensional price impact model of Eq. (65) in which _f_ ( _rt_ ) is replaced by the Dirac distribution centered at time _t_ 0, _δ_ ( _t − t_ 0). 

35 

#### **7.3 High-dimensional models** 

**Modeling co-jumps.** In [12], Bormetti _et al._ modeled the complex dynamics of the extreme returns in a basket of stocks. They started by elaborating a rather elaborate procedure for identifying extreme returns (referred to as “jumps” in the paper, corresponding to anomalous values) from 1-minute returns time-series. On a basket of _N_ = 20 Italian stocks they found up to 280 jumps on a single stock on the overall period (of 88 days) and up to a total of 505 jumps per day on all the stocks. They clearly established that some jumps arrive at the same time, i.e., within the same time-window. This prevents from modeling the overall process as an _N_ -dimensional Hawkes process: Within such a framework, co-jumps cannot occur without introducing an impulsive component inside the kernel Φ. Bormetti _et al._ finally suggested the following model 

- A 1-dimensional Hawkes process is used for modeling the co-jumps arrival times. The kernel of the Hawkes process is chosen to be a sum of exponential functions. 

- Each time _t_ a co-jump occurs, each stock _i_ , independently one form each other, has a probability _pi_ to jump. These probabilities are estimated empirically from real data. 

- For each stock _i_ , a 1-dimensional Hawkes process is used to model the idiosyncratic jumps of that stock, i.e., the jumps that are do not correspond to co-jumps. Again, the kernels of the Hawkes process is chosen to be a sum of exponential functions. 

In their paper, Bormetti _et al._ developed a precise procedure to perform estimation of this model which is shown to be quite robust. Moreover they showed that it is able to capture simultaneously the time clustering of jumps and the high synchronization of jumps across assets. 

**Clustering with graph models.** In [49], Linderman and Adams developed a probabilistic model that combines Hawkes processes with random graphs models, that they applied on S&P100 data. Each component of the Hawkes kernel codes the changes (of more than 0 _._ 1%) in the last traded price of a given asset during a whole week. Thus a 100-dimensional point process with 182.037 events is obtained. The kernels are chosen as 

_φ_<sup>_ij_</sup> ( _t_ ) = _A_<sup>_ij_</sup> _W_<sup>_ij_</sup> _hθij_ ( _t_ ) _,_ (69) 

where _A_ is a random binary (0 or 1) valued matrix, _W_ a random matrix with positive entries and _hθ_ ( _t_ ) a parametric kernel (of parameters _θ_ ) such that � _hθ_ = 1 (a logistic normal density with two parameters is chosen). Intraday seasonality is modeled using an exogenous intensity of the form _µ_ = _m_ + _νe_<sup>_y_(</sup><sup>_t_)</sup> where _ν_ is a constant matrix and _y_ ( _t_ ) is univariate Gaussian process. The random graph model is used to reflect the probability of the different network structures through the prior distributions of the matrices _A_ and _W_ . They basically depend on a latent distance which is chosen in R<sup>2</sup> imposing an overall sparsity (20%) and a characteristic distance scale. Thus each stock _k_ corresponds to a latent coordinate _x_<sup>_k_</sup> in R<sup>2</sup> that is estimated through a fully-Bayesian, parallel inference algorithm. A figure is displayed where each stock is represented as a dot in the latent 2-dimensional space with a color coding corresponding to its corresponding sector (among six sectors). Linderman and Adams showed that some sectors, notably energy and financial, tend to cluster together, indicating an increased probability of interaction between stocks in the 

36 

same sector. Other sectors, such as consumer goods, are broadly distributed, suggesting that these stocks are less influenced by others in their sector. One can think that this approach will pave the way, with the framework of multivariate Hawkes processes, to very promising applications where one will process large amounts of data associated with a great number of interacting components/agents in order to shed new light on the complexity of financial markets. 

Finally, let us note that Mastromatteo and Marsili [52] tried to overcome the problem of the estimation of a high-dimensional Hawkes process by mapping it onto a graphical (Ising) model, so to describe the clustering of trading times in a set stocks. They reconstructed the interaction network of the _D_ = 100 most traded stocks of the NYSE during the year 2003 by using machine learning techniques, and reported an overall scaling of the weight matrix _W ∝ D_<sup>_−_1</sup> . Their study evidences the presence of a large collective market mode of the matrix _A_ , driving the overall level of market activity close to the critical point. 

### **8 Concluding remarks** 

Hawkes processes are extremely versatile processes that can be considered as the building blocks for modeling the occurrence of time-correlated discrete events, playing the same role that Auto-Regressive models have for describing continuous-valued signals. Within a relatively simple mathematical framework, they allow one to characterize precisely the interactions between different categories of events and to account for their causal relations. From the statistical point of view, they can be generated with relatively simple simulation algorithms, while several efficient estimation methods exist to calibrate them. 

Hawkes processes have already proven to be very useful in many domains like, e.g., the modeling of earthquakes, neuronal or social network activity. Because they allow one to describe data at the resolution of individual events and to account for endogenous triggering, contagion and cross-excitation phenomena, they have naturally found applications in the field of high-frequency finance. In this paper, we have proposed an overview of many of such applications that concern a wide variety of problems. From the question of the level of endogeneity of financial markets to the modeling of order-book events, including impact, risk contagion modeling, the design of optimal execution strategies, we saw that Hawkes models have been used to address a large spectrum of issues. 

Far from being exhaustive, this review is necessarily a “snapshot” of a topic that is promised to a rapid evolution and growth. Many of the studies we mentioned can be considered as pioneering works that bode more important results and a deeper understanding of the market dynamics at the microstructural level. Among the promising routes that will be explored in forthcoming studies, some can be easily anticipated. Since several market stylized facts at medium or large time scales seem to originate from the market microstructure, the micro-to-macro transition is an important issue. In that respect, understanding the long-time behavior of the Hawkes process and the instabilities that can emerge can be of great importance. One may hope not only to recover known models at larger times, but also to account for genuinely new phenomena like microstructural crashes. Beyond the Brownian limit which one expects in usual situations, elucidating the emerging properties of the Hawkes process close to the instability limit seems a promising area of research 

37 

due to the richness of the model in the vicinity of the critical point and also because empirical data seem to indicate that markets operate close to this instability threshold. 

The study and the estimation of Hawkes model in the high-dimensional regime is also a challenging prospect since the complexity of financial markets results notably from the interaction between a very large number of components (market participants, agents, assets, information fluxes,...). There have been many progresses made recently in that direction notably under the impetus of the community of big-data and the studies of viral diffusion across social networks. One can expect many interesting applications of theses approaches to high-frequency finance to be proposed in the next future. 

# **Appendices** 

### **A Table of financial applications found within each discussed paper** 

Each of the academic works discussed throughout our paper involving numerical experiments on financial data is listed in the following table. Apart from the column names that are explicit: _D_ stands for dimension of the Hawkes model, _T_ for the length of the historical data used to calibrate the model, d _t_ for the time resolution of the data, Φ( _t_ ) for the shape of the Hawkes kernel. _N_ -Exp stands for a sum of _N_ exponentials, PL for “power-law ” and NP for “non-parametric”. 

38 

|||||**Fi**|**tted Hawkes**||||
|---|---|---|---|---|---|---|---|---|
|||_D_|_Nt_|Contracts|_T_|d_t_|Φ(_t_)|Comments|
|**Sect**|**ion 2**||||||||
|[15]|Bowsher|1-2|Trade|Stocks|2 months|1s|2-Exp|+ Seasonality|
|[18]<br>|Chavez _et al._|1|Extreme ∆_P_|Stocks|1 year|1ms|2-Exp|Marked|
|[42]<br>|Jaisson _et al._<br>|8|Level-I|Futures|1 year|1_µ_s|NP||
|**Sect**|**ion 3**||||||||
|[2]|Bacry _et al._|1|Trade|Futures|3.5 months|1ms|NP||
|||2|Price|Futures|3.5 months|1ms|NP||
|[8]|Bacry _et al._|1|Trade|Futures<br>|4.5 years|1ms|NP||
|[21]|Da Fonseca _et al._|1|Trade|Stocks<br>Futures|2 years|1ms|Exp||
|||2|Mid-Price|Stocks<br>Futures|2 years|1ms|Exp||
|[27]|Embrechts _et al._|2|Extreme ∆_P_|Indices|17 years|1day|Exp|Marked|
|||1|Extreme ∆_P_|Indices|14 years|1h|Exp|3d-Marked|
|[31]|Filimonov _et al._|1|Mid-Price|Futures|13 years|1s|Exp||
|[32]|Filimonov _et al._|1|Mid-Price|Futures|15 years|1s|Exp||
|||1|Mid-Price|Futures|15 years|1s|PL||
|[34]|Hardiman _et al._|1|Mid-Price|Futures|14 years|1ms|N-Exp||
|||1|Mid-Price|Futures|1 year|1ms|NP||
|[35]|Hardiman _et al._|1|Mid-Price|Futures|16 years|1s|Exp||
|||1|Mid-Price|Futures|16 years|1ms|NP||
|[45]|Lallouache _et al._|1|Trade|FX|3 months|0.1s|2-Exp||
|**Sect**|**ion 4**||||||||
|[3]|Bacry _et al._|2|Price|Futures|2 hours|1ms|Exp||
|[30]|Fauth _et al._|4|Trades|FX-Rates|2 months|1ms|Exp|Marked|
|[69]|Zheng _et al._|2|Trade|FX|10 days|0.1s|Exp|Constrained|
|**Sect**|**ion 5**||||||||
|[7]|Bacry _et al._|4|Price+Trade|Futures|3.75 years|1ms|NP||
|[5]|Bacry _et al._|2|Price|Stocks|1 year|1ms|PL||
|[40]|Hewlett|2|Trades|FX|2 months|1s|Exp||
|**Sect**<br>|**ion 6**||||||||
|[46]|Large|10|Level-I|Stocks|22 days|1s|Exp||
|[56]|Muni Toke _et al._|2|Trade-through|Stocks|5 months|1ms|Exp||
|[55]|Muni Toke|2|Orderbook|Stocks|15 days|1ms|Exp||
|**Sect**|**ion 7**||||||||
|[12]|Bormetti _et al._|1_×_20|Price|Stocks|88 days|1 mn|Exp|Co-jump|
|[29]|Errais _et al._|1|Default|Credit|21 days|1day|Exp||
|[49]|Linderman _et al._|100|Extreme ∆_P_|Stocks|1 week|1s|Exp|Fixed decay<br>Random Graph|
|[52]|Mastromatteo _et al._|100|Trades|Stocks|1 year|1s|Exp||
|[61]|Rambaldi _et al._|1|Quotation|FX|1 year|0.1s|N-Exp|News|
|[63]|Sahalia _et al._|1-2|Price|Indices|[22_,_33] years|1day|Exp|Contagion|



### **B Simulation** 

There are two main frameworks for simulating Hawkes processes: an intensity-based framework and a cluster-based framework, depending on whether it makes direct use of the intensity regression Eq. (2) or of the cluster representation of the Hawkes process (see Sec. 2.3.7). The most popular method being certainly the intensitybased thinning method initially introduced by Lewis [48] in the general context of non homogeneous Poisson processes, and modified later by Ogata [58]. 

**Thinning.** The thinning algorithm is an incremental procedure in which the successive jumping times are generated sequentially. It can be easily adapted to the multi-dimensional context and can be generalized to the marked case. In its simplest version (valid for decreasing kernels), given a starting time _t_ it basically consists in sampling a candidate jumping time _t_ + ∆ _t_ using an exponentially distributed random variable ∆ _t_ with parameter _λ_<sup>(</sup> _t_<sup>_tot_)</sup> =<sup>�</sup><sup>_D_</sup> _k_ =1<sup>_λ_</sup> _t_<sup>_k_.Thenarandomvariable</sup><sup>_U_is</sup> uniformly drawn in the interval [0 _, λ_<sup>(</sup> _t_<sup>_tot_)</sup> ]. If _U < λ_<sup>(</sup> _t_<sup>_tot_)</sup> _−λ_<sup>(</sup> _t_ +∆<sup>_tot_)</sup> _t_<sup>, the jump is rejected.</sup> If not rejected, the jump is assigned to the component _i_ , where _i_ is the largest index satisfying _U ≥ λt −_<sup>�</sup><sup>_i_</sup> _k_<sup>_−_</sup> =1<sup>1</sup><sup>_λk_</sup> _t_ +∆ _t_<sup>.Letuspointoutthatthecomplexityofthe</sup> algorithm can be substantially reduced in the case of exponential kernels. 

**Time-change** Another common intensity-based approach for simulating a nonhomogeneous Poisson process _Nt_ uses the following well known fact: if one defines the cumulative intensity function _Ft_ = �0 _t_<sup>_λudu_,then</sup><sup>_N_</sup> _Ft_<sup>_−_1</sup> is an homogeneous Poisson process of intensity 1. Thus in order to perform simulation one needs to know how to simulate _Ft_<sup>_−_</sup> _m_<sup>1</sup> +1<sup>_−F −_</sup> _tm_<sup>1where</sup><sup>_tm_+1</sup><sup>_−tm_isexponentiallydistributed.</sup> This algorithm has been applied for instance in the case of exponential kernels in [24]. In fact, in this simpler case it is possible to invert analytically the function _F_ . 

**Cluster algorithm** The cluster approach consists basically in simulating the branching structure described in Sec. 2.3.7. Hence, the algorithm is sequential in the generations index _n_ rather then in real time _t_ . One can see for instance [54] which describes how one can perform simulation of marked Hawkes processes using the branching structure. A short survey and a more comprehensive list of references can be found in the recent work [24]. 

### **C Statistical inference** 

#### **C.1 Parametric estimation** 

**Maximum Likelihood Estimation.** The most commonly used technique for parametric estimation of Hawkes processes is the Maximum Likelihood Estimator (MLE), which has been first introduced by Ogata in [60]. The log-likelihood of a non-homogeneous, multi-dimensional Poisson defined as in Eq. (2) reads 



40 

where the couples _{_ ( _tm, km_ ) _}_<sup>_M_</sup> _m_ =1<sup>denoterespectivelyeventtimesandcomponents.</sup> Given a Hawkes kernel Φ _θ_ depending upon a set of parameters _θ_ , it is possible to estimate it from Eq. (70) by solving the problem 



In the case of a general Hawkes process, the computation of the likelihood (or its gradient) is of the order of _O_ ( _M_<sup>2</sup> _D_ ) where _M_ is the total number of jumps. The fact that it reduces to _O_ ( _MD_ ) when the kernels are exponential functions is one of the major reasons why exponential kernels (or sum of exponential kernels) are so commonly used in a parametric framework [27, 55, 56, 12, 61, 69]. 

**EM based Estimation.** In [67], the authors use an Expectation Maximization (EM) based technique, an iterative procedure comprising the alternation of two steps of _expectation_ (E) and _maximization_ (M), in order to exploit the cluster representation of the Hawkes process described in Sec. 2.3.7. Given a parametrization of the Hawkes kernel Φ _θ_ , and a set of parameters ( _µ, θ_ ), each iteration consists in: 

- **E-step** ( _µ, θ_ ) _→{pmm′}_ : Estimating, for all ordered pair of jumps ( _tm, tm′_ ) (with _tm < tm′_ ), the probability _pmm′_ that, within the cluster framework described in Sec. 2.3.7, _tm_ is an ancestor of _tm′_ . 

- **M-step** _{pmm′} →_ ( _µ, θ_ ): Computing the model parameters ( _µ, θ_ ) from the probabilities _{pmm′}_ estimated in the E-step. 

This algorithm converges very quickly when the product of the average intensity Λ and the characteristic timescale _τ_ of the support of Φ is small, i.e., Λ _τ ≪_ 1, meaning that few jumps are detected in intervals of size _τ_ . 

Let us point out that General Method of Moments (GMM) can be also used [21], based, for instance, on auto-covariance analytical formula such as (29). 

**High-dimensional estimation.** All the previous techniques cannot be applied in a large dimensional context (e.g., _D ≥_ 100) without substantial modifications. For instance, even in the case of “simple” exponential kernels, the number of parameters is of the order of _D_<sup>2</sup> , so that applications to contexts in which _D_ is large become unfeasible due to overfitting and/or computational issues. In order to address the issue of parametric estimation in large dimensions, one needs to use algorithms which involve regularization. Within the last year, Hawkes processes in large dimension have been the subject of numerous academical papers (see for instance [70]). Most of them, adapt more or less “classical” convex optimization techniques in the framework of Hawkes processes with exponential kernels of the form _α_<sup>_ij_</sup> _β_<sup>_ij_</sup> _e_<sup>_−βijt_</sup> . Let us point out that, in all these papers, in order to get a convex log-likelihood (70), the parameters _β_<sup>_ij_</sup> are a priori fixed (i.e., they are not estimated), and generally not chosen to depend on _i_ or _j_ . Thus, in that case, the kernel matrix Φ can be written in matrix form as Φ = _αβe_<sup>_−βt_</sup> , where _α_ is the so-called (weighted) adjacency matrix _α_ = _{α_<sup>_ij_</sup> _}_ 1 _≤i,j≤D_ . _α_ describes the “connections” between the different components of the Hawkes process. In order to solve the so-obtained convex-optimization of the log-likelihood, penalizations terms on _α_ are customarily introduced. They are generally of two sorts: an _L_<sup>1</sup> penalization that ensures sparsity and a trace-norm penalization that ensures low-rank. To the best of our knowledge, these types of algorithms have only been used once in the context of finance (see Sec. 7.3 about [49]). 

41 

Clearly, one can easily forecast that there will be, in the near future, a huge number of new algorithms for parametric estimation in large dimensions, some of them, improving the state of the art. 

#### **C.2 Non-parametric estimation** 

Very few non-parametric estimators of the kernel matrix of a Hawkes process have appeared in the academic literature so far. We review them in the next section. 

**EM based estimation.** Historically, the first one [47], corresponds to a nonparametric version of the EM estimation algorithm described in the previous section. It is based on regularization (via _L_<sup>2</sup> penalization) of the method initially introduced by [50] in the framework of ETAS model for seismology. It has been developed for 1-dimensional Hawkes processes. The maximum likelihood estimator is computed using the same two steps as in the parametric case. The E-step corresponds to estimating all the _pmm′_ probabilities and the M-step corresponds to estimating _φ_ ( _t_ ) and _µ_ from these probabilities. In [47], some numerical experiments on particular cases are performed successfully even when the exogenous intensity _µ_ depends slowly on time: the whole function _µ_ ( _t_ ) is estimated along with the kernel _φ_ ( _t_ ) with a very good approximation. However, as explained in [8], this method has two main drawbacks: 

- The convergence speed of the EM algorithm drastically decreases when the decay speed of the kernel _φ_ ( _t_ ) is low (e.g., power-law decaying kernel), 

- The probabilistic interpretation of the kernel values involved in the EM method prevents the kernels to have negative values (see Sec. 2.2.4). 

**Contrast function based estimation.** In a recent series of papers [62, 33], some authors proposed, within a rigorous statistical framework, a second approach for non-parametric estimation. It relies on the minimization of the so-called _L_<sup>2</sup> _contrast function_ . Given a realization of a Hawkes process _N_<sup>˜</sup> _t_ on an interval [0 _, T_ ], associated with the parameters (˜ _µ,_ Φ(<sup>˜</sup> _t_ )), the estimation is based on minimizing the _contrast function C_ ( _µ,_ Φ): 



where 



and 



Let us point out that, minimizing the expectancy of the contrast function is equivalent to minimizing the _L_<sup>2</sup> error on the intensity process. Indeed, if _Ft_ is the 

42 

information available up to time _t_<sup>_−_</sup> , since E � d _N_<sup>˜</sup> _t_<sup>_i_</sup> �� _Ft_ � = _λ_<sup>˜</sup><sup>_i_</sup> _t_<sup>d</sup><sup>_t_,onehas</sup> 



The minimum value (zero) is of course uniquely reached for Φ = Φ<sup>˜</sup> and _µ_ = _µ_ ˜. 

In [33], the authors chose to decompose Φ on a finite dimensional-space (in practice, the space of the constant piece-wise functions) and to solve directly the minimization problem (72) in that space. For that purpose, in order to regularize the solution (they are essentially working with some applications in mind for which only a small amount of data is available, and for which the kernels are known to be well localized), they chose to penalize the minimization with a Lasso term (which is well known to induce sparsity in the kernels), i.e., the _L_<sup>1</sup> norm of the components of Φ. Let us point out, that minimizing the contrast function and minimizing the expectancy of the contrast function are two different stories. The contrast function is stochastic, and nothing guarantees that the associated linear equation is not illconditioned. In [33], the authors prove that, under certain conditions on Φ, the linear equation is invertible, i.e., the associated random Gram matrix is almost surely positive definite. In practice (they study real signals from neurobiology), they choose the components of Φ to be piece-wise constant. 

**The Wiener-Hopf approach.** Let us point out that, since _λ_<sup>_i_</sup> _t_<sup>is expressed lin-</sup> early in terms of _µ_<sup>_i_</sup> and of the _{φ_<sup>_ij_</sup> ( _t_ ) _}_<sup>_D_</sup> _ij_ =1<sup>, minimizing the</sup><sup>_L_2 error (75) is equivalent</sup> to solving a linear equation, which is nothing but the Wiener Hopf Eq. (38). Consequently, minimizing the expectancy of the contrast function is equivalent to solving the Wiener-Hopf equation. In [7, 8], the authors chose to perform non-parametric estimation by directly inverting this system. They have proved that, as long as _g_ ( _t_ ) corresponds to a conditional intensity of a Hawkes process, (38) has a unique solution in _χ_ ( _t_ ) which is the kernel matrix Φ( _t_ ). The algorithm uses quadrature technique in order to discretize the system. It can be summarized in the following way: 

- Estimation of the vector Λ (simply using as an estimator of Λ<sup>_i_</sup> the number of jumps of the realization of _N_<sup>_i_</sup> divided by the overall time realization) 

- Non-parametric estimation of the matrix _g_ ( _t_ ) defined by (36) (using kernel density estimation techniques) 

- Fix the number of quadrature points (e.g., gaussian quadrature) to be used as well as the support for all the kernel functions. 

- Discretize the Wiener-Hopf system on the quadrature points and inverse it. This leads to an estimation of the kernel functions on the quadrature points. Estimation on a finer grid as well as _L_<sup>1</sup> norm can be obtained through simple quadrature formula. 

_•_ Estimation of the exogenous intensity _µ_ using (21). 

We refer the reader to [8] where the full algorithm (including the methodology for choosing the bandwidth value for density kernel estimation as well as the number of quadrature points) is described precisely along with the comparisons with the other 

43 

methods presented above. It has actually been improved in [6] to take particular care of slowly decreasing kernels. 

As compared to the approach developed in [33], this algorithm is better adapted to the case in which a large amount of data is available. As compared to the EM approach, we shall advocate its use over the EM algorithm mainly in two cases (which are often satisfied when dealing with financial data): 

- Either the kernel functions are not localized (e.g., power-law). Indeed, in that case the EM algorithm is known to be very slow to converge (see [47] and [8]), 

- Or some of the kernel functions have negative values (see second point on the EM algorithm above). We refer the reader to [33] for justification why Wiener-Hopf approach allows to deal with negative kernels. 

Finally, let us point out that, in the particular case the kernel matrix is known to be symmetric (which is always true if the dimension _D_ = 1), the method developed in [2] uses a spectral method for inverting (23) and deduces an estimation from the second-order statistics. It can be seen as a particularly elegant way of solving the Wiener-Hopf equation. 

### **Acknowledgements** 

We thank J.P. Bouchaud and S. Hardiman for providing data from Refs. [34, 35]. This research benefited from the support of the “Chair Markets in Transition”, under the aegis of “Louis Bachelier Finance and Sustainable Growth” laboratory, a joint initiative of Ecole<sup>´</sup> Polytechnique, Universit´e d’Evry<sup>´</sup> Val d’Essonne and F´ed´eration Bancaire Fran¸caise. 

### **References** 

- [1] A. Alfonsi and P. Blanc. Dynamic optimal execution in a mixed-market-impact hawkes price model. _arXiv preprint arXiv:1404.0648_ , 2014. 

- [2] E. Bacry, K. Dayri, and J.F. Muzy. Non-parametric kernel estimation for symmetric hawkes processes. application to high frequency financial data. _Eur. Phys. J. B_ , 85:157, 2012. 

- [3] E. Bacry, S. Delattre, M. Hoffmann, and J.F. Muzy. Modelling microstructure noise with mutually exciting point processes. _Quantitative Finance_ , 13:65–77, 2013. 

- [4] E Bacry, S Delattre, M. Hoffmann, and J.F. Muzy. Some limit theorems for hawkes processes and application to financial statistics. _Stochastic Processes and their Applications_ , 123(7):2475–2499, 2013. 

- [5] E. Bacry, A. Iuga, M. Lasnier, and C-A. Lehalle. Market impacts and the life cycle of investors orders. _arXiv preprint arxiv:1412.0217v2_ , 2014. 

- [6] E. Bacry, T. Jaisson, and J.F. Muzy. Estimation of slowly decreasing hawkes kernels: Application to high frequency order book modelling. _arXiv preprint arXiv:1412.7096_ , 2015. 

- [7] E. Bacry and J.F. M. Hawkes model for price and trades high-frequency dynamics. _Quantitative Finance_ , 14(7):1–20, 2014. 

- [8] E. Bacry and J.F. Muzy. Second order statistics characterization of hawkes processes and non-parametric estimation. _arXiv preprint arXiv:1401.0903_ , 2014. 

44 

- [9] L. Bauwens and N. Hautsch. _Modelling financial high frequency data using point processes_ . Springer, 2009. 

- [10] L. Bauwens and N. Hautsch. Stochastic conditional intensities processes. _Journal of Financial Econometrics_ , 4:450–493, 2009. 

- [11] B. Biais, P. Hillion, and C. Spatt. An empirical analysis of the limit order book and the order flow in the paris bourse. _the Journal of Finance_ , 50(5):1655–1689, 1995. 

- [12] G. Bormetti, L.M. Calcagnile, M. Treccani, F. Corsi, S. Marmi, and F. Lillo. Modelling systemic price cojumps with hawkes factor models. _Quantitative Finance (in press)_ , 2015. 

- [13] J.P. Bouchaud. Price impact. In R. Cont, editor, _Encyclopedia of Quantitative Finance_ . John Wiley & Sons Ltd., 2010. 

- [14] J.P. Bouchaud, J. D. Farmer, and F. Lillo. How markets slowly digest changes in supply and demand. In Thorsten Hens and Klaus Schenk-Hoppe, editors, _Handbook of Financial Markets: Dynamics and Evolution_ , pages 57–156. Elsevier: Academic Press, 2008. 

- [15] C.G. Bowsher. Modelling security market events in continuous time: Intensity based, multivariate point process models. _Journal of Econometrics_ , 141(2):876– 912, 2007. 

- [16] P. Br´emaud and L. Massouli´e. Stability of nonlinear hawkes processes. _The Annals of Probability_ , pages 1563–1588, 1996. 

- [17] P. Br´emaud, L. Massouli´e, et al. Hawkes branching point processes without ancestors. _Journal of applied probability_ , 38(1):122–135, 2001. 

- [18] V. Chavez-Demoulin and JA McGill. High-frequency financial data modeling using hawkes processes. _Journal of Banking & Finance_ , 36(12):3415–3426, 2012. 

- [19] R. Cont, A. Kukanov, and S. Stoikov. The price impact of order book events. _Journal of financial econometrics_ , 12(1):47–88, 2013. 

- [20] J.C. Cox, Jr Ingersoll, and S.A. Ross. A theory of the term structure of interest rates. _Econometrica_ , 5:385–407, 1985. 

- [21] J. Da Fonseca and R. Zaatour. Hawkes process: Fast calibration, application to trade clustering, and diffusive limit. _Journal of Futures Markets_ , 34(6):548–579, 2014. 

- [22] D.J. Daley and D. Vere-Jones. _An introduction to the theory of point processes_ , volume 2. Springer, 1988. 

- [23] A. Dassios and H. Zhao. A dynamic contagion process. _Advances in applied probability_ , 43(3):814–846, 2011. 

- [24] A. Dassios and H. Zhao. Exact simulation of hawkes process with exponentially decaying intensity. _Electronic Communications in Probabilities_ , 18(62), 2013. 

- [25] M. Dhamala, G. Rangarajan, and M. Ding. Estimating granger causality from fourier and wavelet transforms of time series data. _Phys. Rev. Lett._ , 100(1):18701, 2008. 

- [26] D. Duffie, D. Filipovic, and W. Schachermayer. Affine processes and applications in finance. _Annals of Applied Probability_ , 13:984–1053, 2003. 

- [27] P. Embrechts, T. Liniger, L. Lin, et al. Multivariate hawkes processes: an application to financial data. _Journal of Applied Probability_ , 48:367–378, 2011. 

- [28] R.F. Engle and J.R. Russel. Autoregressive conditional duration: A new model for irregulary spaced transaction data. _Econometrica_ , 66:1127–1162, 1998. 

- [29] E. Errais, K. Giesecke, and L.R. Goldberg. Affine point processes and portfolio credit risk. _SIAM Journal on Financial Mathematics_ , 1(1):642–665, 2010. 

45 

- [30] A. Fauth and C. Tudor. Modeling first line of an order book with multivariate marked point processes. _arXiv preprint arXiv:1211.4157v1_ , 2012. 

- [31] V. Filimonov and D. Sornette. Quantifying reflexivity in financial markets: Toward a prediction of flash crashes. _Physical Review E_ , 85(5):056108, 2012. 

- [32] V. Filimonov and D. Sornette. Apparent criticality and calibration issues in the hawkes self-excited point process model: application to high-frequency financial data. _arXiv preprint arXiv:1308.6756_ , 2013. 

- [33] N.R Hansen, P. Reynaud-Bouret, and V. Rivoirard. Lasso and probabilistic inequalities for multivariate point-processes. _arXiv preprint arXiv:12080570, To appear in Bernoulli._ 

- [34] S.J. Hardiman, N. Bercot, and J.P. Bouchaud. Critical reflexivity in financial markets: a hawkes process analysis. _arXiv preprint arXiv:1302.1405_ , 2013. 

- [35] S.J. Hardiman and J.P. Bouchaud. Branching ratio approximation for the selfexciting hawkes process. _arXiv preprint arXiv:1403.5227_ , 2014. 

- [36] J. Hasbrouck. Measuring the information content of stock trades. _Journal of Finance_ , 46:179–207, 1991. 

- [37] A.G. Hawkes. Point spectra of some mutually exciting point processes. _J. R. Statist. Soc. B_ , 33:438–443, 1971. 

- [38] A.G. Hawkes. Spectra of some self-exciting and mutually exciting point processes. _Biometrika_ , 58(1):83–90, 1971. 

- [39] S.L. Heston. A closed-form solution for options with stochastic volatility with applications to bond and currency options. _Review of financial studies_ , pages 385–407, 1993. 

- [40] P. Hewlett. Clustering of order arrivals, price impact and trade path optimisation. In _Workshop on Financial Modeling with Jump processes, Ecole Polytechnique_ , pages 6–8, 2006. 

- [41] T. Jaisson. Market impact as anticipation of the order flow imbalance. _arXiv preprint arXiv:1402.1288_ , 2014. 

- [42] T. Jaisson and M. Rosenbaum. Limit theorems for nearly unstable hawkes processes. _To appear in The Annals of Applied Probability._ , 2014. 

- [43] A. Jedidi and F. Abergel. Stability and price scaling limit of a Hawkes-process based order book model. 2013. 

- [44] Stojan Jovanivi´c, John Hertz, and Stefan Rotter. Cumulants of hawkes point processes. _arXiv preprint arXiv:1409.5353_ , 2014. 

- [45] M. Lallouache and D. Challet. Statistically significant fits of hawkes processes to financial data. _Available at SSRN 2450101_ , 2014. 

- [46] J. Large. Measuring the resiliency of an electronic limit order book. _Journal of Financial Markets_ , 10(1):1–25, 2007. 

- [47] E. Lewis and G. Mohler. A nonparametric em algorithm for multiscale hawkes processes. _preprint_ , 2011. 

- [48] P.A. Lewis and G.S. Shedler. Simulation of nonhomogeneous poisson processes by thinning. _Naval Research Logistics Quarterly_ , 3:403–413, 1979. 

- [49] S.L. Linderman and R.P. Adams. Discovering latent network structure in point process data. _arXiv preprint arXiv:1402.0914v1_ , 2014. 

- [50] D.. Marsan and O. Lenglin´e. Extending earthquakes’ reach through cascading. _Science_ , 319:1076, 2008. 

- [51] I. Mastromatteo, E. Bacry, and J.F. Muzy. Linear processes in high-dimension: phase space and critical properties. _arXiv preprint arXiv:1412.6998_ , 2014. 

46 

- [52] I. Mastromatteo and M. Marsili. On the criticality of inferred models. _Journal of Statistical Mechanics: Theory and Experiment_ , 2011(10):P10012, 2011. 

- [53] B. Mehrdad and L. Zhu. On the hawkes process with different exciting functions. _arXiv preprint arXiv:1403.0994_ , 2014. 

- [54] J. Moller and J.G. Rasmussen. Perfect simulation of hawkes processes. _Adv. in Appl. Probab._ , 37(3):629–646, 2005. 

- [55] I. Muni Toke. Market making” in an order book model and its impact on the bid-ask spread. In _Econophysics of Order-Driven Markets, New Economic Windows_ . Springer, 2010. 

- [56] I. Muni Toke and F. Pomponio. Modelling trades-through in a limit order book using hawkes processes. _Economics: The Open-Access, Open-Assessment E-Journal_ , 6(2012-22), 2012. 

- [57] A.G. Nedungadi, G. Rangarajan, N. Jain, and M. Ding. Analyzing multiple spike trains with nonparametric granger causality. _Journal of computational neuroscience_ , 27(1):55–64, 2009. 

- [58] Y. Ogata. On lewis’ simulation method for point processes. _Ieee Transactions On Information Theory_ , 27:23–31, January 1981. 

- [59] Y. Ogata. Statistical models for earthquake occurrences and residual analysis for point processes. _Journal of the American Statistical Association_ , pages 9–27, 1988. 

- [60] Y. Ogata and H. Akaike. On linear intensity models for mixed doubly stochastic poisson and self- exciting point processes. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 44(1):102–107, January 1982. ArticleType: research-article / Full publication date: 1982 / Copyright 1982 Royal Statistical Society. 

- [61] M. Rambaldi, P. Pennesi, and F. Lillo. Modeling fx market activity around macroeconomic news: a hawkes process approach. _Physical Review E_ , 91(1):012819, 2015. 

- [62] P. Reynaud-Bouret and S. Schbath. Adaptive estimation for hawkes processes; application to genome analysis. _Ann. Statist_ , 38:2781–2822, 2010. 

- [63] Y.A. Sahalia, J. Cacho-Diaz, and R.J.A. Laeven. Modeling financial contagion using mutually exciting jump processes. (15850), 2014. 

- [64] E. Smith, J.D. Farmer, L. Gillemot, and S. Krishnamurthy. Statistical theory of continuous double auction. _Quantitative Finance_ , 3:481–514, 2003. 

- [65] D. Sornette and G. Ouillon. Multifractal scaling of thermally activated rupture processes. _Phys. Rev. Lett._ , 94:038501, Jan 2005. 

- [66] Bence Tth, Imon Palit, Fabrizio Lillo, and J. Doyne Farmer. Why is equity order flow so persistent? _Journal of Economic Dynamics and Control_ , 51(0):218 – 239, 2015. 

- [67] A. Veen and F.P. Schoenberg. Estimation of space-time branching process models in seismology using an em-type algorithm. _J. Amer. Statist. Assoc._ , 103:614–624, 2008. 

- [68] M. Wyart, J.P. Bouchaud, J. Kockelkoren, M. Potters, and M. Vettorazzo. Relation between bid–ask spread, impact and volatility in order-driven markets. _Quantitative Finance_ , 8(1):41–57, 2008. 

- [69] B. Zheng, Roueff F., and F. Abergel. Ergodicity and scaling limit of a constrained multivariate hawkes process. _SIAM J. Financial Math_ , 5, 2014. 

47 

- [70] K. Zhou, H. Zha, and L. Song. Learning triggering kernels for multi-dimensional hawkes processes. In _Proceedings of the 30th International Conference on Machine Learning (ICML-13)_ , pages 1301–1309, 2013. 

48 

