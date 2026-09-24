---
title: "Causal Strategic Classification: A Tale of Two Shifts"
authors: "horowitz"
year: 2023
arxiv_id: "2302.06280"
original_file: "2302.06280.pdf"
pdf_path: "docs/papers\2023_horowitz_causal_strategic_classification_a_t.pdf"
---

# Causal Strategic Classification: A Tale of Two Shifts

**Authors:** Horowitz et al.  
**Year:** 2023 | **arXiv:** [`2302.06280`](https://arxiv.org/abs/2302.06280)  
**Local PDF:** [`2023_horowitz_causal_strategic_classification_a_t.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2023_horowitz_causal_strategic_classification_a_t.pdf)

---

**Causal Strategic Classification: A Tale of Two Shifts** 

**Guy Horowitz**<sup>1</sup> **Nir Rosenfeld**<sup>1</sup> 

# **Abstract** 

When users can benefit from certain predictive outcomes, they may be prone to act to achieve those outcome, e.g., by strategically modifying their features. The goal in strategic classification is therefore to train predictive models that are robust to such behavior. However, the conventional framework assumes that changing features does not change actual outcomes, which depicts users as ‘gaming’ the system. Here we remove this assumption, and study learning in a causal strategic setting where true outcomes do change. Focusing on accuracy as our primary objective, we show how strategic behavior and causal effects underlie two complementing forms of distribution shift. We characterize these shifts, and propose a learning algorithm that balances between these two forces and over time, and permits end-to-end training. Experiments on synthetic and semi-synthetic data demonstrate the utility of our approach. 

# **1. Introduction** 

The field of strategic classification (Bruckner et al.¨ , 2012; Hardt et al., 2016) studies learning in a setting where users can strategically respond to a learned classifier by modifying their features, at some cost, to obtain favorable predictive outcomes. Such behavior can be expected when predictions are used to inform decisions about users, and from which users stand to gain (or lose); common examples include loans approval, university admissions, and job hiring. The framework of strategic classification succinctly captures a widespread form of tension that naturally arises between a classifier and the users it targets, and which applies broadly. This has made it the target of much recent interest (Dong et al., 2018; Miller et al., 2020; Tsirtsis & Gomez Rodriguez, 2020; Jagadeesan et al., 2021; Ghalme et al., 2021; Zrnic et al., 2021; Levanon & Rosenfeld, 2021; 2022; Estornell 

> 1Technion – Israel Institute of Technology, Haifa, Israel. Correspondence to: Nir Rosenfeld _<_ nirr@cs.technion.ac.il _>_ . 

_Proceedings of the 40_<sup>_th_</sup> _International Conference on Machine Learning_ , Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright 2023 by the author(s). 

et al., 2021; Lechner & Urner, 2021; Ahmadi et al., 2022; Nair et al., 2022; Eilat et al., 2022; Barsotti et al., 2022). 

As a learning problem, strategic classification is appealing in that its simple and clean formulation permits and feasible practical challenges. But simplicity comes at a price, and the framework’s general applicability is hindered by its reliance on a set of strong assumptions. As part of a growing community effort to extend strategic classification beyond its original narrow form, our goal in this work is to take one step towards making strategic classification more flexible. In particular, here we target one of the key assumptions in strategic classification, which is the assumption that true outcomes _y_ do _not_ change when features _x_ are modified. Under this assumption, strategic behavior amounts to gaming, and users are depicted as acting to ‘fool’ the classifier. But in reality, this assumption rarely holds, since actions taken by users to change predictions can also change true outcomes. 

The observation that changes in _x_ can causally affect _y_ has been made by several authors (Miller et al., 2020; Shavit et al., 2020; Bechavod et al., 2021; Harris et al., 2022). But to date, works that have addressed this point focus primarily on the question of _improvement_ , i.e., whether (and how) learning can incentivize users to change _x_ in ways that improve outcomes _y_ . While this is an important goal, here we argue that the current perspective conflates (i) the mere fact that _y_ can change, with (ii) the desire for _y_ to change favorably. But from a purely predictive point of view, _any_ changes to _y_ —whether for better or for worse—may deteriorate performance. Hence, and given that the implications of causal strategic behavior on learning are not yet well-understood, here we choose to focus entirely on the conventional goal of optimizing predictive accuracy, and study appropriate notions of robustness. We view this as an essential first step, intended to set the ground for more elaborate learning tasks such as incentivizing for improvement. 

Towards this, and aiming to remain as true as possible to the original formulation, we seek to take the minimal necessary step beyond strategic classification for introducing meaningful causal relations. Our proposed setting, which generalizes vanilla strategic classification, can be described succinctly by a simple causal graph depicting the relations between different variable types: _causal_ , _non-causal_ (or ‘correlative’), and _unobserved_ . The graph’s structure defines 

1 

**Causal Strategic Classification: A Tale of Two Shifts** 

the learning objective, which in turn determines the precise form in which learning must be strategically-robust. This formulation reveals where and how causality can impede learning, and hints at how these challenges can be addressed. 

In essence, strategic behavior can be viewed as entailing a certain form of distribution shift—with the key property that _how_ the distribution shifts depends on the choice of classifier, indirectly through how it shapes user responses (Drusvyatskiy & Xiao, 2022; Maheshwari et al., 2022). Our first contribution is characterizing the role causality plays in this process. When causality is absent, strategic updates _x�→x_<sup>_′_</sup> change _p_ ( _x_ ), but also _p_ ( _y|x_ ); this is since the induced _p_<sup>_′_</sup> ( _y|x_<sup>_′_</sup> ) must ‘remember’ the original _y_ . Conversely, we show that in a fully causal setting, learning reduces to a particular instance of _decision-dependent covariate shift_ , in which strategic behavior affects only the marginal _p_ ( _x_ ); In other words, causality ‘cancels out’ the strategic effect on _p_ ( _y|x_ ). Thus, the challenge in learning lies in correctly balancing between two distinct notions of robustness. 

Based on these insights, our second contribution is a learning algorithm for strategic causal classification. We focus on the setting where users respond rationally and under a predetermined feature partition; this places emphasis on coping with the uncertainty in _y_ introduced by the causal structure. Here the challenge is that learning must simultaneously account for (i) _strategic_ changes in _x_ , in response to the learned classifier _f_ ; and (ii) _causal_ changes in _y_ , which result from changes in _x_ . The key to effective learning therefore lies in correctly decoupling strategic and causal effects; towards this, and relying on our theoretical analysis, our algorithm makes use of an estimated marginal density model _p_ ˆ( _x_ ), which is novel in this space. As we show, our approach effectively separates informational uncertainty, which is irreducible, from statistical uncertainty—which our approach efficiently reduces by making use of additional strategically-modified (i.e., ‘dirty’) data. 

Our approach becomes especially effective over _time_ : here we make connections to the literature on _performative prediction_ (Perdomo et al., 2020), and study causal strategic learning in a temporal setting and under retraining dynamics. In standard strategic classification, learning is known to converge after a single time-step (Hardt et al., 2016); but this notion breaks once causal effects are introduced. The fact that both _p_ ( _y|x_ ) and _p_ ( _x_ ) can now temporally change poses a challenge, but also an opportunity: using an appropriate form of regularization, we show how learning can be made to incentivize feature updates that reveal labeled information from under-represented areas of _p_ ( _x_ ), which contribute to an improved estimation of _p_ ( _y|x_ ). 

Finally, we conduct a series of experiments that empirically validate our approach. First, using synthetic data, we design experiments aimed at showcasing the challenges, pitfalls, 

and opportunities that arise when learning in causal strategic environments. Then, we use real data (augmented with simulated responses) to compare our approach to several baselines. We report both quantitative and qualitative results, and perform sensitivity analysis regarding to our structural assumptions. Overall, our results shed light on the importance of accounting for causal effects in strategic setting, and the need to correctly balance between these forces. All code is made publicly available and can be found at: https://github.com/guyhorowitz/CSC. 

## **1.1. Related work** 

**Strategic classification.** Since its introduction (Bruckner¨ et al., 2012; Hardt et al., 2016), the literature on strategic classification has been growing rapidly. Efficient learning algorithms have been proposed for the original batch setting (Levanon & Rosenfeld, 2021; 2022), as well as online formulations (Chen et al., 2020; Ahmadi et al., 2021). On the theoretical front, Zhang & Conitzer (2021); Sundaram et al. (2021) extend PAC theory via strategic VC analysis. Ongoing efforts aim to extend the original setting to handle utilities that are unknown (Dong et al., 2018), noisy (Jagadeesan et al., 2021), estimated (Ghalme et al., 2021; Bechavod et al., 2022; Barsotti et al., 2022), allow for arbitrary preferences (Levanon & Rosenfeld, 2022), or are linked by a graph (Eilat et al., 2022). Other works break or relax some core assumptions, such as the order of play (Nair et al., 2022) or the role of time (Zrnic et al., 2021). Our work joins these efforts, with the aim of allowing true outcomes to causally change when features are modified. 

**Causal strategic learning.** Several works blend causality with strategic learning, but these focus almost exclusively on improvement. Kleinberg & Raghavan (2020) study the problem of incentivizing agents to improve, and Alon et al. (2020); Haghtalab et al. (2020) generalize their setting to multiple agents; however, neither of these works directly consider learning. Miller et al. (2020) show that learning to incentivize improvement inevitably requires solving a non-trivial causal inference problem; thus, coping with causality requires making some assumptions about the underlying causal structure. Some works make assumptions that permit causal inference, acting either through indirect experimentation in online learning (Bechavod et al., 2021) or by using the published classifiers as instruments in an offline setting (Harris et al., 2022); these works, however, are restricted to regression. Other works consider particular causal relations, such as Mendler-Dunner et al.¨ (2022) who study predictions as interventions, or Chen et al. (2021) who decouple gaming and improving effects in both learning and evaluation. Closest to ours is Shavit et al. (2020), who provide learning algorithms for improvement, estimation, and (to some extent) accuracy; however, they focus on linear regression (in which strategic responses are invertible), 

2 

**Causal Strategic Classification: A Tale of Two Shifts** 

consider a realizable (linear) setting, and make assumptions that permit causal discovery. Our work studies (agnostic) classification and focuses predominantly on accuracy. 

# **2. Problem setup** 

We start by briefly describing standard strategic classification, and continue with our proposal for injecting causality. 

## **2.1. Standard strategic classification** 

In the original formulation of strategic classification (Hardt et al., 2016), users have feature representations _x ∈X_ = R<sup>_d_</sup> and binary labels _y ∈Y_ = _{±_ 1 _}_ . Let _p_ ( _x, y_ ) be a joint distribution over (nonstrategic) features and labels. The primary goal in learning is to find a classifier _f_ : _X →Y_ from a class _F_ that achieves high expected accuracy, given a train set _S_ = _{_ ( _xi, yi_ ) _}_<sup>_m_</sup> _i_ =1<sup>with (</sup><sup>_xi, yi_)</sup> _iid∼ p_ ( _x, y_ ). At test time, however, _f_ is evaluated on strategically-modified data, where users update features via the _best-response mapping_ : 



where _c_ ( _x, x_<sup>_′_</sup> ) is a cost function that determines the cost of changing _x_ to _x_<sup>_′_</sup> , and is assumed to be known to all. The goal of learning is to minimize the expected 0-1 loss, but under the strategically-induced distribution: 



We focus on the common choice of linear classifiers _y_ ˆ = _f_ ( _x_ ) = sign ( _w_<sup>_⊤_</sup> _x_ + _b_ ) and generalized quadratic costs _cQ_ ( _x, x_<sup>_′_</sup> ) = ( _x_<sup>_′_</sup> _− x_ )<sup>_⊤_</sup> _Q_ ( _x_<sup>_′_</sup> _− x_ ) = _∥x_<sup>_′_</sup> _− x∥_<sup>2</sup> _Q_<sup>for PSD</sup><sup>_Q_.</sup> 

## **2.2. Causal strategic classification** 

A key assumption in standard strategic classification is that changes in _x_ (via ∆ _f_ ) do _not_ affect _y_ ; this is encoded directly in Eq. (2). We will be interested in breaking this assumption by allowing changes in _x_ to causally affect _y_ . To account for causal effects, we require a concrete structure that determines how changes in _x_ translate to changes in _y_ . We seek to take the minimally-necessary step for generalizing the standard setting to include causal effects. 

**The causal structure.** Our main structural assumption is that observable features _x_ can be partitioned into _causal_ features _xc ∈Xc_ = R<sup>_dc_</sup> that affect _y_ , and _correlative_ features _xr ∈Xr_ = R<sup>_dr_</sup> that do not. Together, we denote _x_ = ( _xc, xr_ ). To enable both _xc_ and _xr_ to be distinctly important in prediction, we allow for additional _unobserved_ causal features, _u ∈U_ = R<sup>_du_</sup> , with which _xr_ correlates. Thus, _xr_ can be informative of _y_ beyond what is conveyed by _xc_ , and therefore complementarily useful in learning. This mimics a setting in which some known causes are 



<!-- Start of picture text -->
xc xc xc<br>u y y y ˆ<br>xr xr xr<br>(a) (b) (c)<br><!-- End of picture text -->

Figure 1: **(a)** The true causal graph over user features and labels. Solid lines represent direct causal effects, dashed lines depict correlation (whose source is abstracted away). **(b)** The causal graph, as perceived by the system. Note that _u_ is unobserved, but its relation to _y_ carries over to _xr_ , making it predictively informative of _y_ . **(c)** The causal graph, as perceived by users, who seek positive predictions _y_ ˆ = 1. 

observed ( _xc_ ), but alone cannot fully explain _y_ , and so are complemented by additional features ( _xr_ ) which relate to other possible causes of _y_ , but are themselves non-causal. We assume ( _x, u_ ) _∼ p_ ( _x, u_ ) for some unknown distribution _p_ ( _x, u_ ). For labels, we consider _y_ as determined jointly by _xc_ and _u_ via _y ∼ h_<sup>_∗_</sup> ( _xc, u_ ), for some stochastic groundtruth labeling function _h_<sup>_∗_</sup> . Figure 1 compactly describes our proposed causal structure using a simple causal graph.<sup>1</sup> 

**Implications on learning.** Since only ( _xc, xr_ ) are observed, the classifier _f_ can only be a function of these, i.e., _f_ ( _xc, xr_ ), and users respond just as in Eq. (1), i.e., via: 



Note this implies that users are incentivized to change only _xc_ and _xr_ , but _not u_ : once ∆ _f_ has been applied, the underlying features become ( _x_<sup>_f_</sup> _c_<sup>_, xf_</sup> _r_<sup>_, u_), and the updated label—</sup> which is the true target of prediction—is _y_<sup>_f_</sup> = _h_<sup>_∗_</sup> ( _x_<sup>_f_</sup> _c_<sup>_, u_).</sup> Given this, our causal strategic learning objective is: 



In the simple case where _xr_ = _u_ (but noting _xr�→x_<sup>_f_</sup> _r_ does _not_ change _u_ ), _y_<sup>_f_</sup> can be interpreted as _h_<sup>_∗_</sup> (¯ _x_ ), where _x_ ¯ = ( _x_<sup>_f_</sup> _c_<sup>_, xr_) is the ‘projection’ of</sup><sup>_xf_onto the causal sub-</sup> space (see Figure 2). In the special case where there are no causal features (i.e., _x_ = _xr_ ), Eq. (4) reduces to the standard strategic classification objective in Eq. (2) with _y_ = _h_<sup>_∗_</sup> ( _u_ ), and any discrepancies between _xr_ and _u_ manifest as noise. 

1Despite our structural assumptions, our setting remains quite flexible. First, relations between _xr_ and _u_ can be arbitrary; e.g., _xr_ can be a causal child of _u_ , or _xr_ and _u_ have a common parent _z_ . Second, _h_<sup>_∗_</sup> can be any stochastic function of _xc_ and _u_ , and we make no assumptions on its form or relation to _F_ . Third, we allow _u_ and _x_ to be dependent (this is abstracted away in Fig. 1). Fourth, we assume _u_ includes _some_ variables that correlate with _xr_ , but make no assumptions on, nor require knowledge of, their nature. 

3 

**Causal Strategic Classification: A Tale of Two Shifts** 

**Challenges and prospects.** The main challenge in optimizing Eq. (4) is that in addition to accounting for strategic responses _x �→ x_<sup>_f_</sup> , learning must now also anticipate how such changes affect labels via _y_<sup>_f_</sup> = _h_<sup>_∗_</sup> ( _x_<sup>_f_</sup> _c_<sup>_, u_).Intuitively,</sup> since points move to obtain positive predictions _y_ ˆ = 1, correctly estimating _y_<sup>_f_</sup> is important for (i) _avoiding_ negative post-strategic labels _y_<sup>_f_</sup> = _−_ 1 (on which _f_ errs), as well as for (ii) _encouraging_ positive post-strategic labels _y_<sup>_f_</sup> = 1 (on which _f_ is correct). This reveals how user interests ( _y_ ˆ = 1) align system goals ( _y_ ˆ = _y_<sup>_f_</sup> ) with the general aim of improvement ( _y_<sup>_f_</sup> = 1). Nonetheless, these notions remain distinct, and optimizing for one criterion does _not_ imply optimality for the other (see Appendix B.1). 

Since _h_<sup>_∗_</sup> is unknown, our approach for optimizing Eq. (4) will be to replace _h_<sup>_∗_</sup> with some estimated _h_<sup>ˆ</sup> . However, since training data _S_ includes only ‘clean’ points ( _x, y_ ), the challenge in this is twofold: (i) due to strategic behavior, _h_<sup>_∗_</sup> might need to be queried on points that lie outside the data distribution, and for which _S_ (on which _h_<sup>ˆ</sup> is trained) may not be representative, and (ii) even though _x_<sup>_f_</sup> _c_<sup>can be computed,</sup> _u_ remains to be unobserved. As we will show, allowing learning to make use of additional ‘dirty’ data ( _x_<sup>_f_</sup> _, y_<sup>_f_</sup> ), collected _over time_ and under different deployed classifiers _f_ , can enable learning to contend with these challenges. 

## **2.3. Learning over time** 

To study temporal aspects of causal strategic learning, we adopt the general formulation of _performative prediction_ (Perdomo et al., 2020). Here, learning proceeds in discrete rounds, where at each round _t >_ 0 the currently deployed model _ft_ determines the data distribution in the next round, _pt_ +1 = _p_<sup>_ft_</sup> = _D_ ( _ft_ ; _p_ 0), for some initial _p_ 0 and distribution mapping _D_ . The overall goal is to optimize _f_ on the distribution it induces, namely minimize the _performative risk_ : 



In our setting, _D_ corresponds to feature updates via ∆ _f_ and label updates via _h_<sup>_∗_</sup> , and Eq. (4) is a special case of Eq. (5).<sup>2</sup> 

Similarly to Miller et al. (2021), we allow _T_ rounds of retraining and deployment. At each round _t ≤ T_ , the system observes new data _St ∼ pt_ , and (re)-trains _ft_ ; then, it deploys _ft_ , which induces a distribution shift: 



<!-- Start of picture text -->
𝑥! strategic + causal strategic<br>ℎ ∗ 𝑥= −1 ℎ ∗ 𝑥= 1<br>Δ% 𝑦 "<br>𝑦 "<br>𝑥 " 𝑦<br>Δ% 𝑦 " 𝑓 causal<br>𝑥̅<br>𝑥 𝑦 "<br>Δ%<br>𝑦 "<br>𝑥#<br>𝑐≤2<br><!-- End of picture text -->

Figure 2: **An example of causal strategic classification.** Given _f_ , strategic users move clean points _x_ = ( _xc, xr_ ) onto the decision boundary, _x_<sup>_f_</sup> = ∆ _f_ ( _x_ ), when costs permit. Labels, however, are affected only by the updated causal component, _x_<sup>_f_</sup> _c_<sup>, via</sup><sup>_yf_=</sup><sup>_h∗_(</sup><sup>_xf_</sup> _c_<sup>_, u_) (c.f.strategic-</sup> only or causal-only cases). For _xr_ = _u_ , labels _y_<sup>_f_</sup> are given by projecting _x_<sup>_f_</sup> onto the causal subspace, _x_ ¯ = ( _x_<sup>_f_</sup> _c_<sup>_, xr_).</sup> 

the dynamics, and so are required to perform well at each point in time. Note rounds _t >_ 0 includes fresh samples, which consist purely of ‘dirty’ inputs ( _x_<sup>_ft_</sup> _, y_<sup>_ft_</sup> ) _∼ pt_ +1; importantly, for these points, their corresponding original ‘clean’ ( _x, y_ ) remain unknown. Finally, at time _T_ , the system commits to some final _f ∈{ft}t<T_ , to be used henceforth, and on which performative risk is evaluated. 

# **3. Analysis** 

To learn well in causal strategic settings, we must first understand how strategic behavior and causal effects translate into distribution shifts. In this section we characterize such shifts by analyzing the induced marginal _p_<sup>_f_</sup> ( _x_<sup>_f_</sup> ) and conditional _p_<sup>_f_</sup> ( _y_<sup>_f_</sup> _|x_ ) for different cases. Throughout we use capital letters to denote random variables (e.g., _X, U, Y_ ) and lowercase for their realizations (e.g., _x, u, y_ ). Our analysis makes use of an ‘inverse’ response mapping operator: 



which for any ‘shifted’ point _x_<sup>_′_</sup> returns the set of points _x_ from which _x_<sup>_′_</sup> could have originated. For simplicity here we present results for deterministic _h_<sup>_∗_</sup> , but these also hold in the stochastic case. Proofs are deferred to Appendix A. 

## **3.1. Case #1: Correlative-only features** 



where in our setting _p_ 0 = _p_ is the ‘clean’ distribution, and _S_ = _S_ 0. In retraining dynamics, each _ft_ is optimized for accuracy using currently available data: this relates to settings where deployed models are used throughout 

> 2Note Eq. (2) is also a special case of Eq. (5), but which is known to converge after one round when ∆ is known. 

Using _xr_ to predict _y_ can be useful due to its correlation with _u_ , which is a direct (and potentially distinct) cause of _y_ . When _f_ relies only on _xr_ , all of the features that are used for learning are non-causal, hence changes in _x_ do not affect _y_ . **Observation 1.** _When using only xr, causal strategic classification reduces to standard strategic classification._ 

Denote _x_<sup>_′_</sup> _r_<sup>= ∆</sup><sup>_f_(</sup><sup>_xr_).Our first result shows the connection</sup> 

4 

**Causal Strategic Classification: A Tale of Two Shifts** 

between the original and induced distributions. 

**Lemma 1.** _Let p_ ( _xr, y_ ) _be some base distribution. Then for any classifier f , the induced p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _r_<sup>_, y_)</sup><sup>_can be expressed_</sup> _using the base marginal p_ ( _xr_ ) _and conditional p_ ( _y|xr_ ) _as:_ 



Eq. (7) simply states that the probability of observing some modified _x_<sup>_′_</sup> _r_<sup>derives from all points</sup><sup>_xr_that map to it via ∆</sup><sup>_f_.</sup> Eq. (8) then shows that predicting for _x_<sup>_′_</sup> _r_<sup>its corresponding</sup> _y_ (which remains unmodified) requires reasoning about the possible labels of all points in ∆<sup>–</sup> _f_<sup>1(</sup><sup>_x_</sup> _r_<sup>_′_); since this is a set,</sup> the implication is inherent (informational) uncertainty in _y_ , which cannot be reduced through statistical means (i.e., observing more data from _p_<sup>_f_</sup> ). This reveals the mechanism through which strategic behavior can hinder accuracy, _<u>p</u>_ <u>(</u> _xr_ <u>)</u> where _p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _r_ )<sup>expresseshowstrategicbehavior‘distorts’</sup> the base probability _p_ ( _y|xr_ ) (which already includes any uncertainty due to _u_ , and to _xc_ if it exists). 

Lemma 1 shows that the case of _x_ = _xr_ entails _full distribution shift_ , i.e., both _p_ ( _x_ ) and _p_ ( _y|x_ ) can vary. Nonetheless, it provides useful insight, which is immediate from Eq. (8): 

**Corollary 1.** _When using only xr, knowing the base distribution suffices for constructing the Bayes-optimal classifier._ 

Corollary 1 highlights why clean samples are useful; it also suggests that learning might benefit from incorporating a marginal density estimator, _p_ ˆ( _x_ ), into the training procedure—a notion we adopt in our algorithm in Sec. 4. 

## **3.2. Case #2: Causal-only features** 

Using _xc_ is useful for learning as it is a direct cause of _y_ in itself. We now analyze the case of using only _xc_ for prediction, which requires us to directly account for _u_ . In this case, the base conditional has the following form: 



which is simply the uncertainty in _y_ due to _u_ . Further assuming that _Xc_ and _U_ are independent reveals a tight connection. Denote _x_<sup>_′_</sup> _c_<sup>= ∆</sup><sup>_f_(</sup><sup>_xc_) and</sup><sup>_y′_=</sup><sup>_h∗_(</sup><sup>_x_</sup> _c_<sup>_′, u_).</sup> 

**Lemma 2.** _Let p_ ( _xc, y_ ) _be some base distribution, and_ 

_assume xc⊥u. Then for any classifier f , we have:_ 



_and p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _c_<sup>)</sup><sup>_is as in Eq._(7)</sup><sup>_(with xcreplacing xr)._</sup> 

Because the induced marginal is susceptible only to strategic effects, its form remains the same regardless of which features are used. More interestingly, Eq. (10) states that the induced conditional _p_<sup>_f_</sup> ( _y_<sup>_′_</sup> _|x_<sup>_′_</sup> _c_<sup>) remains exactly the same as</sup> the _original_ base _p_ ( _y|x_ ) (Eq. (9)). Thus, causal effects ‘cancel out’ the strategic effect of _f_ on _p_ ( _y|xc_ ), and only _p_<sup>_f_</sup> ( _xc_ ) remains susceptible to strategic shifts. Thus, for _any f_ , it holds that _P_ ( _Y_<sup>_′_</sup> = _y_<sup>_′_</sup> _|Xc_<sup>_′_=</sup><sup>_x_</sup> _c_<sup>_′_)=</sup><sup>_P_(</sup><sup>_Y_=</sup><sup>_y′|Xc_=</sup><sup>_x_</sup> _c_<sup>_′_),</sup> which is a special case of _covariate shift_ (Shimodaira, 2000). 

**Corollary 2.** _If xc and u are independent, then irrespective of f , using only xc reduces to learning under covariate shift._ 

## **3.3. Case #3: Using all features** 

We now consider the most general case when all feature types are used (and with no assumptions on independence). 

**Lemma 3.** _For any p_ ( _x, u_ ) _and any classifier f , we have:_ 



_where:_ 



_and p_<sup>_f_</sup> ( _x_<sup>_′_</sup> ) _is as in Eq._ (7) _(with x replacing xr)._ 

While covariate shift no longer holds, note that Eq. (11) matches Eq. (10) up to the term _νf_ . Hence, _νf_ quantifies the deviation from covariate shift due to _f_ : when _νf_ ( _u_ ; _x_<sup>_′_</sup> ) takes values close to one across _u_ , then covariate shift ‘approximately’ holds; otherwise, we have a particular form of full distribution shift. Note that in itself, _νf_ relates to Eq. (8), in that the strategic effects also express as a distorted probability term integrated over the inverse response set. 

**Interpretation.** Our analysis thus far reveals a tradeoff: Correlative features _xr_ are susceptible to gaming—which manifests as full distribution shift, but requires only clean data to accommodate. Conversely, causal features _xc_ (and their relation to _u_ ) bring learning closer to covariate shift, which is simpler, but introduces larger uncertainty in _y_ . Note this uncertainty stems from points _x_<sup>_f_</sup> moving to regions of low density under _p_ ; hence, in principle, dirty data gathered over time and in response to different models _f_ may aid in decreasing uncertainty and improving performance. Our approach, presented next, aims to balance these two forces. 

5 

**Causal Strategic Classification: A Tale of Two Shifts** 

# **4. Method** 

Recall that our goal is to optimize the causal strategic learning objective in Eq. (4). Given a finite sample _S_ , we adopt the conventional ERM approach and aim to minimize the empirical risk. Ideally, we would like to solve: 



However, this introduces several challenges: (i) the 0-1 loss is non-differentiable; (ii) _x_<sup>_f_</sup> is the output of ∆ _f_ ( _x_ ), which is an argmax operator that is also non-differentiable; (iii) _h_<sup>_∗_</sup> is unknown, and (iv) _u_ is unobserved, which together prevent us from computing updated labels _y_<sup>_f_</sup> = _h_<sup>_∗_</sup> ( _x_<sup>_f_</sup> _c_<sup>_, u_).Also</sup> note that Eq. (13) makes no use of the observed clean _y_ . 

Our first step is to replace 1 _{·}_ with an appropriate proxy loss; for this, we adopt the _strategic hinge ℓ_ s-hinge from Levanon & Rosenfeld (2022), which accounts for strategic behavior and provides favorable generalization guarantees. Importantly, it does not explicitly rely on ∆ _f_ , and is entirely differentiable. Next, for handling _h_<sup>_∗_</sup> and _u_ , our general approach will be to replace _h_<sup>_∗_</sup> with a learned _h_ , and use _xr_ as a surrogate for _u_ .<sup>3</sup> We first describe our approach for clean data, and then extend it to utilize additional dirty data. Pseudocode for our entire procedure is given in Algorithm (1). 

## **4.1. Learning with clean data** 

We propose to replace _h_<sup>_∗_</sup> in Eq. (13) with a differentiable estimate _h_ : _Xc × Xr →_ [ _−_ 1 _,_ 1], learned from data over some chosen function class _H_ . Here the goal is to exploit the correlation between _u_ and the observed (pre-strategic) _xr_ ; i.e. _h_ uses _xr_ as a ”substitute” for how _h_<sup>_∗_</sup> uses _u_ , and as a complement to _x_<sup>_f_</sup> _c_<sup>.4Sincecleandataincludesclean</sup> labels _y_ = _h_<sup>_∗_</sup> ( _xc, u_ ), we can use _S_ to optimize _h_ via: 



for some standard proxy loss _ℓ_ (e.g., hinge loss or log loss). Note that _h_ is learned on ( _xc, xr_ ), but used on ( _x_<sup>_f_</sup> _c_<sup>_, xr_).In</sup> principle, _h_<sup>_∗_</sup> is needed only for points that move, since if _x_<sup>_f̸_</sup> = _x_ then _y_<sup>_f_</sup> = _h_<sup>_∗_</sup> ( _x_<sup>_f_</sup> _c_<sup>_, u_),and otherwise</sup><sup>_yf_=</sup><sup>_y_.To</sup> prevent _h_ from needlessly erring in such cases, we implement _y_<sup>_f_</sup> as a differentiable ‘soft if’, _y_ ˜ _h_ , as follows. First, note that _x_ moves iff it is necessary _and_ cost-effective, i.e.: 





> 3Our approach requires to operationally define a feature partition as input to the learning algorithm. In Sec. 6.4 we empirically demonstrate its robustness to misspecified partitionings. 

> 4Note _h∗_ takes inputs ( _xc, u_ ), whereas _h_ operates on ( _xc, xr_ ). 

## **Algorithm 1** CSERM 

- 1: **Input:** clean data _S_ , regularization schedule _λt_ 

- 2: _S_ 0 _← S_ 

- 3: _p_ ˆ _←_ KDE( _S_ ) 





## **4.2. Utilizing additional dirty data** 

The limitation in using only clean data for training _h_ is that _h_ is tailored to _p_ , and may not approximate _h_<sup>_∗_</sup> well outside it—a likely scenario when points move strategically. Towards this, we propose to use temporally-gathered dirty data, sampled from induced distributions _p_<sup>_f_</sup> , to iteratively improve _h_ by retraining it at each round _t_ on all available data, namely training _ht_ on _S≤t_ = _∪t′≤tSt′_ where _St′ ∼ p_<sup>_t′_</sup> = _p_<sup>_ft′−_1</sup> . Unfortunately, dirty data isn’t immediately useful, and na¨ıvely training _ht_ on it may introduce bias. To see why, note that dirty data includes inputs ( _x_<sup>_f_</sup> _c_<sup>_, xf_</sup> _r_<sup>_, yf_);incontrast,theobserved</sup><sup>_yf_dependsvia</sup><sup>_h∗_</sup> on _x_<sup>_f_</sup> _c_<sup>andon</sup><sup>_u_.Whereas</sup><sup>_xf_</sup> _c_<sup>isuseful,whatwerequire</sup> is the original _xr_ , which is informative of _u_ —instead, we observe the modified _x_<sup>_f_</sup> _r_<sup>, which is inappropriate.Ideally, we</sup> would like to train _ht_ on ‘mixed’ pairs ( _x_<sup>_f_</sup> _c_<sup>_, xr_), but these</sup> are unavailable. As a solution, we propose to reconstruct _x_ ˜ _r ≈ xr_ using a density model ˆ _p_ ( _x_ ) _≈ p_ ( _x_ ), trained once at the onset on clean data. Since _x_<sup>_f_</sup> is the strategic response to some _x_ , we can estimate the likelihood for any given _xr_ as _p_ ˆ( _xr|x_<sup>_f_</sup> ); by considering all points in ∆<sup>–</sup> _f_<sup>1(</sup><sup>_xf_), we define:</sup> 



To obtain a single entry, we compute the expected value: 



6 

**Causal Strategic Classification: A Tale of Two Shifts** 

and use these for training _h_ . Appendix B.2 shows how to efficiently compute Eq. (17) , using the fact that ∆<sup>–</sup> _f_<sup>1(</sup><sup>_xf_)</sup> can be expressed as a closed interval of points in R<sup>_d_</sup> . 

**Regularization for exploration.** Although dirty data can be helpful in extending the regions of data on which _ht_ is trained, _what_ those regions are is determined entirely by the set of previous _ft_ . To promote variation in dirty data, we propose to augment Eq. (16) with a regularization term that encourages _f_ to push points _x_<sup>_f_</sup> to regions of low density: 



Here, _q_ ˆ is a density model that is (re)-trained on aggregate data _S≤t_ at each round _t_ , since its role is to inform us of uncertainty in _ht_ . Our final regularized learning objective is: 

argmin � _ℓ_ s-hinge � _f_ ( _x_<sup>_f_</sup> ) _,_ ˜ _yh_ ( _x, x_<sup>_f_</sup> )� + _λR_ ( _f_ ; _S,_ ˆ _q_ ) _f ∈F_ ( _x,y_ ) _∈S_ (19) 

This equips our approach with a mild form of exploration, whose degree is determined by _λ_ . Practically we found it useful to use a gradually decaying _λt_ : this places initial emphasis on exploration, which gradually shifts towards exploitation as more data is collected. In our experiments we use a kernel density estimator (KDE) for ˆ _q_ , which is differentiable; hence, the entire objective can be trained end-to-end. 

# **5. Experiments using synthetic data** 

We begin with a series of synthetic experiments, each designed to demonstrate a different aspect of our setting and approach. We consider _x ∈_ R<sup>2</sup> (which can be visualized), and fix _x_ 1 = _xc_ and _x_ 2 = _xr_ = _u_ . We compare learning using our strategic causal approach ( `CSERM` ) to (i) a na¨ıve `ERM` approach, and (ii) a strategically-aware (but causally-oblivious) baseline that optimizes Eq. (2) using the approach in Levanon & Rosenfeld (2022) ( `SERM` ). We also consider a non-strategic benchmark ( `ns-bench` ) in which `ERM` is evaluated on clean (i.e., non-strategic) data. 

**Utilizing improvement.** Our first experiment studies the ability of our approach to identify and make use of regions where _h_<sup>_∗_</sup> is _positive_ to increase predictive performance (Fig. 3 A). We construct _p_ ( _xc, u_ ) to include two clusters that are separable by a linear _h_<sup>_∗_</sup> , but inject noise so that it is no longer separable by any _f_ ( _x_ ) (while preserving the majority class in each cluster). As expected, `SERM` (80% accuracy) operates by taking the optimal `ERM` solution (54%) and making it more strict to prevent negative points from crossing; from its own perspective, this is sensible, since if _y_ does not change, then negative points that move cause _f_ to err. In contrast, `CSERM` (89%) utilizes its knowledge of _h_<sup>_∗_</sup> (via _h_ ) to push negative points to positive regions; once these points move, they obtain both positive predictions _and_ positive labels, and accuracy increases—surpassing `ns-bench` (80%). 



<!-- Start of picture text -->
A ERM (54%) SERM (80%) CSERM (89%)<br>B ERM (50%) SERM (50%) CSERM@t=0 (50%)<br>C ERM (50%) SERM (50%)<br>CSERM@t=2 (98%)<br>CSERM@t=0 (41%) CSERM@t=3 (53%) CSERM@t=6 (100%)<br>h<br>f<br>h<br>h<br>f<br>f<br>f<br>f<br>f<br>h<br>f<br>f<br>h<br>f<br>f<br>f<br>f<br>h<br><!-- End of picture text -->

Figure 3: Results on synthetic experiments (A,B,C) for `ERM` , strategic `ERM` ( `SERM` ), and our approach ( `CSERM` ) (acc. in parentheses). Here _x_ 1= _xc_ (x-axis) and _x_ 2= _xr_ = _u_ (y-axis). Hollow circles show pre-modified (‘clean’) data, filled circles show strategically-modified (‘dirty’) data. Colored regions depict _h_<sup>_∗_</sup> ; red lines show learned _f_ , dashed lines mark regions of movement for ∆ _f_ , blue lines show learned _h_ . 

**Avoiding pitfalls.** We next experiment in a setting in which knowledge about where _h_<sup>_∗_</sup> is _negative_ is crucial for preserving accuracy (Fig. 3 B). Here the clean _p_ ( _xc, u_ ) also defines two clusters, but which can now be separated by a learned _f_ . However, outside _p_ ( _xc, u_ ), we define _h_<sup>_∗_</sup> to be positive precisely on the positive cluster, and negative elsewhere. Here the optimal solution is to use only _xr_ since it preserves the original _y_ . `ERM` (50%) fails due to strategic behavior; `SERM` (50%) anticipates strategic responses, but is oblivious to _h_<sup>_∗_</sup> , and so inadvertently pushes positive points to become negative, and errs. `CSERM` , by estimating _h_<sup>_∗_</sup> with _h_ , is able to find the optimal solution, though this takes time. 

**The role of exploration.** Our last synthetic experiment considers the canonical XOR classification task, which is well-known to be non-linearly separable (Fig. 3 C). Indeed, `ERM` fails catastrophically (50%), as does `SERM` (50%). Nonetheless, our approach can obtain perfect accuracy—by utilizing causal knowledge to incentivize strategic behavior that _makes_ the data separable. This, however, requires 

7 

**Causal Strategic Classification: A Tale of Two Shifts** 

Table 1: Results on real data. 

|||**ca**|**rd frau**|**d**||||**spam**|||
|---|---|---|---|---|---|---|---|---|---|---|
||accuracy|%improve|%move|%neg_�→_pos|welfare|accuracy|perceived|%improve|%move|%pos_�→_neg|
|`CSERM`_λ_|**87.8****_±_0****_._2**|**12.2**|60.1|**13.8**|-0.65|**92.7****_±_0****_._5**|97.0|3.1|37.5|**0.1**|
|`CSERM`|**86.6****_±_0****_._5**|**10.2**|58.9|**11.8**|-0.48|**92.4****_±_0****_._4**|97.1|2.4|36.7|**0.1**|
|`SERM`|78.4_±_0_._2|0.8|45.9|1.6|-0.16|84.0_±_0_._3|**91.2**|**-7.2**|41.3|7.2|
|`RRM`|75.8_±_0_._5|0.5|24.7|0.7|-0.06|77.2_±_2_._4|76.6|-2.1|30.5|2.8|
|`ERM`|66.7_±_0_._6|0.3|19.8|0.4|0.25|75.4_±_0_._3|91.2|0.4|17.1|0.0|
|`oracle`|87.0_±_0_._2|10.1|57.9|11.8|-0.60|93.5_±_0_._1|93.5|4.5|41.7|0.0|



exploration: without regularization, `CSERM` is unable to improve, since newly collected dirty points do not improve _h_ ; however, by encouraging _f_ to uncover uncertain regions, _h_ improves over time, until it is sufficiently informative of _h_<sup>_∗_</sup> for learning to find the optimal _f_ (100%), which pushes one cluster of negative points to a positive region. 

# **6. Experiments using real data** 

We now turn to experiments based on real data using two public datasets: (i) spam, used originally in Hardt et al. (2016), and (ii) card fraud, used in Levanon & Rosenfeld (2021). Appendix D includes further details on data, methods, and optimization. 

**Procedure.** Experimenting in a causal setting requires us to be able to query labels for arbitrary (modified) points ( _x_<sup>_′_</sup> _c_<sup>_, u_).</sup> Towards this, we begin each experiment by determining a partition of the original features into _xc_ and _u_ , and use points ( _xc, u_ ) to train a ground-truth labeling function _h_<sup>_∗_</sup> using original labels _y_<sup>_∗_</sup> . For consistency we use _h_<sup>_∗_</sup> to generate labels _y_ for both clean and dirty examples. We then define a mapping _u�→xr_ , which can be lossy and noisy. 

Next, we split the data roughly 60-10-30 into train, validation, and test sets. The train set is then further partitioned into a clean set, and an inventory from which dirty data is sampled (see Appendix E.2 for additional results on different ratios of clean vs. dirty data). Validation data is used for early stopping and model selection, and held-out test data is used for final evaluation. In line with our temporal setup in Sec. 2.3, we consider _T_ = 10 rounds of retraining, where at each round _t_ , we generate on the basis of _ft_ dirty samples _St_ . These are obtained by taking a 1 _/T_ -portion of the reserved inventory, and simulating strategic responses via _x_<sup>_ft_</sup> = ∆ _ft_ ( _x_ ) and label updates _y_<sup>_ft_</sup> = _h_<sup>_∗_</sup> ( _xc_<sup>_ft, u_).Once</sup> _St_ is obtained, at round _t_ + 1 it can be used for training _ft_ +1. Non-temporal methods are given access to the full (clean) train set. Costs are _cα_ ( _x, x_<sup>_′_</sup> ) = _α∥x − x_<sup>_′_</sup> _∥_ 2<sup>2, where</sup> for consistency across datasets we set _α_ so that _∼_ 50% of points move on round _t_ = 1. Appendix E.2 includes results on additional _α_ -s and for all methods, exhibiting qualitatively similar performance trends. 

Finally, we run all methods and compare performance. For methods that make use of dirty data over time, we report results for each round, as well as for the best model (chosen on validation data) to which the method commits. We report average results and standard errors over 15 random splits. 

**Methods.** In addition to (i) `ERM` , (ii) `SERM` , and (iii) our `CSERM` , here we consider the following additional methods: (iv) repeated risk minimization ( `RRM` ) (Perdomo et al., 2020), which applies `ERM` independently at each round; (v) `RRM` _≤t_ , which uses all previous data; and (vi) `RRMc` , which uses only causal features to avoid dealing with ‘gaming’ behavior. For our approach, we distinguish between non-regularized ( `CSERM` ) and regularized ( `CSERM` _λ_ ) variants (by default _λ_ 0 = 1). We include the non-strategic `ns-bench` , and an `oracle` - like benchmark which combines _h_<sup>_∗_</sup> within our approach. 

## **6.1. Utilizing improvement on card fraud** 

For fraud, we set _h_<sup>_∗_</sup> be 3-layer MLP, on top of which we add noise, so that some regions of _x_ -space include a mixture of positive and negative labels. Potentially, if _f_ can incentivize such points to move to areas where _h_<sup>_∗_</sup> is more positive, then this should entail better accuracy. Table 1 (left) shows results. As can be seen, `CSERM` improves significantly over other methods, gaining +8.2% by accounting for changes in _y_ (vs. `SERM` ) in addition to strategic effects (+19.9% vs. `ERM` ). which here `RRM` is also able to achieve using time. Regularization adds +1.2%. To gain insight as to why, notice that `CSERM` incentivizes more movement (14% vs. `SERM` ); of this, 14% of points shift from _y_ = _−_ 1 to _y_<sup>_f_</sup> = 1, giving an overall improvement rate of 12%. In comparison, other methods improve by _<_ 1%. Improvement, however, does not imply that users necessarily benefit: when considering welfare, defined as average utility minus costs (and so in [ _−_ 1 _,_ 1]), the predictive success of `CSERM` comes at the price of reduced welfare, _despite_ improvement. 

## **6.2. Avoiding pitfalls on spam** 

For spam, we set _h_<sup>_∗_</sup> to be linear, except for one ‘tricky’ causal feature _ci_ which we concavify by preserving its positive slope _in-domain_ , but reversing its slope to negative _out-of-domain_ . This mimics a setting where having some 

8 

**Causal Strategic Classification: A Tale of Two Shifts** 



<!-- Start of picture text -->
card fraud spam<br>method 0.85<br>0.90<br>0.85 CSERM 0.80<br>0.85 CSERM = 1 CSERM wrong feature type<br>0.80 0.80 RRMRRMc 0.750.70 CSERM discard featureSERM<br>0.75 0.75 RRM t knowledgefull 1 2 3 4 5 6 7 8 9 10 11 wrongall<br>0.70 0.70 0 .92 0 0.9<br>0 .87 0.0<br>0.65 0 .90 0.1<br>0.65 0 .86 0.5 0.8 CSERM wrong feature type<br>0.60 0 .85 0.60 0 .88 1.03.0 0.7 CSERM discard featureSERM<br>0 .84 0.55 0 .86 5.0 full 1 2 3 4 all<br>1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 knowledge wrong<br>round round #unknown features type<br>accuracy<br>card fraud<br>accuracy accuracy<br>psam<br>accuracy<br><!-- End of picture text -->

Figure 4: **(Left:)** Results for temporal methods over rounds. Inlay shows accuracy of `CSERM` _λ_ for different values of _λ_ . **(Right:)** Sensitivity analysis, showing accuracy for increasingly ’wrong’ feature type attribution (causal vs. correlative). 

amount of _ci_ is helpful for obtaining _y_ = 1, but having ‘too much’ is not. Table 1 (right) shows results. Here as well, `CSERM` exhibits significant gains, but this time through different means. To see this, notice first that `SERM` ’s failure comes from causing positive points to become negative (7.2%); this occurs since its reliance on _ci_ —which is predictivelyuseful in-domain—breaks once points move out-of-domain in that direction (interestingly, `SERM` is blind to this, as its ‘perceived’ accuracy 7% higher than its actual accuracy). Conversely, and by correctly identifying its nature, `CSERM` dodges the _ci_ ‘trap’, and diverts movement elsewhere. 

which simply discards the wrong features ( `CSERM` DISCARD). Results are shown in Fig. 4 (right), with average and standard deviation over 10 random seeds and min _{_ 30 _,_ � _dd_<sup>_′_</sup> � _}_ feature subsets per experimental condition. As expected, errors in feature type attribution do entail reduced performance for `CSERM` WRONG; however, performance goes down slowly, either reaching `SERM` when all features are wrong ( _d_<sup>_′_</sup> = _d_ ; for card fraud), or remaining above it (spam). In contrast, discarding the same ‘wrong’ features causes performance to deteriorate quickly and sharply. 

# **7. Discussion** 

## **6.3. Time and regularization** 

Fig. 4 (left) shows the performance of temporal methods over time. Over time, and by utilizing additional dirty data, `CSERM` is able to improve performance (relative to _t_ = 1) by _∼_ 3% in card fraud, and _∼_ 6% in spam. `RRMc` also improves over time—but to a significantly lesser degree; this shows the effectiveness of using causally-affected dirty data, but at the same time, reveals the (unutilized) potential of using non-causal features. `RRM` does use all features, but its performance over time is unstable (in spam performance _decreases_ over time). `RRM` _≤t_ does improve, but is inconsistent across datasets. As for the effect of regularization, results show how `CSERM` _λ_ initially performs worse than `CSERM` —but proceeds to outperform it for both datasets. This holds for all _λ_ , and becomes more pronounced (for better and worse) as _λ_ grows (see inlays). 

## **6.4. Sensitivity analysis** 

Our final experiment tests the sensitivity of our approach to errors in features type attribution (i.e., considering a causal feature as non-causal, and vice versa). Towards this, for each _d_<sup>_′_</sup> _≤ d_ , we evaluate a variant of `CSERM` which wrongly associates the type of a random subset of _d_<sup>_′_</sup> features ( `CSERM` WRONG). We compare this to `SERM` (which does not use feature type information at all), and to a variant of `CSERM` 

This paper extends the study of strategic classification to causal settings in which changing inputs can also change outputs. By focusing on the fundamental goal of optimizing accuracy, our analysis surfaces the need for learning to accommodate two interwoven forms of distribution shift. These differ in the challenges they present, but are also complementary in their relation to _time_ ; our approach utilizes these properties to provide a learning algorithm that is effective and efficient. Our choice of remaining true to the original problem formulation permits a clean formulation, and allows us to make connections to existing works. Nonetheless, the current literature on strategic classification remains far from being applicable in real social settings; we view our work as taking one step toward this ultimate goal. 

## **Acknowledgements** 

This research was supported by the Israel Science Foundation (grant No. 278/22). 

# **References** 

- Ahmadi, S., Beyhaghi, H., Blum, A., and Naggita, K. The strategic perceptron. In _Proceedings of the 22nd ACM Conference on Economics and Computation_ , pp. 6–25, 2021. 

9 

**Causal Strategic Classification: A Tale of Two Shifts** 

- Ahmadi, S., Beyhaghi, H., Blum, A., and Naggita, K. On classification of strategic agents who can both game and improve. _arXiv preprint arXiv:2203.00124_ , 2022. 

- Alon, T., Dobson, M., Procaccia, A., Talgam-Cohen, I., and Tucker-Foltz, J. Multiagent evaluation mechanisms. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 34, pp. 1774–1781, 2020. 

- Barsotti, F., Koc¸er, R. G., and Santos, F. P. Transparency, detection and imitation in strategic classification. In _Proceedings of the 31st International Joint Conference on Artificial Intelligence, IJCAI 2022_ , 2022. 

- Bechavod, Y., Ligett, K., Wu, S., and Ziani, J. Gaming helps! Learning from strategic interactions in natural dynamics. In _International Conference on Artificial Intelligence and Statistics_ , pp. 1234–1242. PMLR, 2021. 

- Bechavod, Y., Podimata, C., Wu, S., and Ziani, J. Information discrepancy in strategic learning. In _International Conference on Machine Learning_ , pp. 1691–1715. PMLR, 2022. 

- Bruckner, M., Kanzow, C., and Scheffer, T. Static prediction¨ games for adversarial learning problems. _The Journal of Machine Learning Research_ , 13(1):2617–2654, 2012. 

- Chen, Y., Liu, Y., and Podimata, C. Learning strategyaware linear classifiers. _Advances in Neural Information Processing Systems_ , 33:15265–15276, 2020. 

- Chen, Y., Wang, J., and Liu, Y. Linear classifiers that encourage constructive adaptation. In _Algorithmic Recourse workshop at ICML’21_ , 2021. 

- Costa, H., Merschmann, L. H., Barth, F., and Benevenuto, F. Pollution, bad-mouthing, and local marketing: the underground of location-based social networks. _Information Sciences_ , 279:123–137, 2014. 

- Dong, J., Roth, A., Schutzman, Z., Waggoner, B., and Wu, Z. S. Strategic classification from revealed preferences. In _Proceedings of the 2018 ACM Conference on Economics and Computation_ , pp. 55–70, 2018. 

- Drusvyatskiy, D. and Xiao, L. Stochastic optimization with decision-dependent distributions. _Mathematics of Operations Research_ , 2022. 

- Eilat, I., Finkelshtein, B., Baskin, C., and Rosenfeld, N. Strategic classification with graph neural networks. _arXiv preprint arXiv:2205.15765_ , 2022. 

- Estornell, A., Das, S., Liu, Y., and Vorobeychik, Y. Unfairness despite awareness: Group-fair classification with strategic agents. In _Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS), StratML workshop_ , 2021. 

- Ghalme, G., Nair, V., Eilat, I., Talgam-Cohen, I., and Rosenfeld, N. Strategic classification in the dark. In _International Conference on Machine Learning_ , pp. 3672–3681. PMLR, 2021. 

- Haghtalab, N., Immorlica, N., Lucier, B., and Wang, J. Z. Maximizing welfare with incentive-aware evaluation mechanisms. In Bessiere, C. (ed.), _Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, IJCAI-20_ , pp. 160–166, 7 2020. Main track. 

- Hardt, M., Megiddo, N., Papadimitriou, C., and Wootters, M. Strategic classification. In _Proceedings of the 2016 ACM conference on innovations in theoretical computer science_ , pp. 111–122, 2016. 

- Harris, K., Ngo, D. D. T., Stapleton, L., Heidari, H., and Wu, S. Strategic instrumental variable regression: Recovering causal relationships from strategic responses. In _International Conference on Machine Learning_ , pp. 8502–8522. PMLR, 2022. 

- Jagadeesan, M., Mendler-Dunner, C., and Hardt, M.¨ Alternative microfoundations for strategic classification. In _International Conference on Machine Learning_ , pp. 4687– 4697. PMLR, 2021. 

- Kleinberg, J. and Raghavan, M. How do classifiers induce agents to invest effort strategically? _ACM Transactions on Economics and Computation (TEAC)_ , 8(4):1–23, 2020. 

- Lechner, T. and Urner, R. Learning losses for strategic classification. In _Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS), Workshop on Learning in Presence of Strategic Behavior_ , 2021. 

- Levanon, S. and Rosenfeld, N. Strategic classification made practical. In _International Conference on Machine Learning_ , pp. 6243–6253. PMLR, 2021. 

- Levanon, S. and Rosenfeld, N. Generalized strategic classification and the case of aligned incentives. In _Proceedings of the 39th International Conference on Machine Learning (ICML)_ , 2022. 

- Maheshwari, C., Chiu, C.-Y., Mazumdar, E., Sastry, S., and Ratliff, L. Zeroth-order methods for convex-concave minmax problems: Applications to decision-dependent risk minimization. In _International Conference on Artificial Intelligence and Statistics_ , pp. 6702–6734. PMLR, 2022. 

- Mendler-Dunner,¨ C., Ding, F., and Wang, Y. Predicting from predictions. In _Advances in neural information processing systems_ , 2022. 

- Miller, J., Milli, S., and Hardt, M. Strategic classification is causal modeling in disguise. In _International Conference on Machine Learning_ , pp. 6917–6926. PMLR, 2020. 

10 

**Causal Strategic Classification: A Tale of Two Shifts** 

- Miller, J. P., Perdomo, J. C., and Zrnic, T. Outside the echo chamber: Optimizing the performative risk. In _International Conference on Machine Learning_ , pp. 7710– 7720. PMLR, 2021. 

- Nair, V., Ghalme, G., Talgam-Cohen, I., and Rosenfeld, N. Strategic representation. In _International Conference on Machine Learning_ , pp. 16331–16352. PMLR, 2022. 

- Perdomo, J., Zrnic, T., Mendler-Dunner, C., and Hardt, M.¨ Performative prediction. In _International Conference on Machine Learning_ , pp. 7599–7609. PMLR, 2020. 

- Shavit, Y., Edelman, B., and Axelrod, B. Causal strategic linear regression. In _International Conference on Machine Learning_ , pp. 8676–8686. PMLR, 2020. 

- Shimodaira, H. Improving predictive inference under covariate shift by weighting the log-likelihood function. _Journal of statistical planning and inference_ , 90(2):227–244, 2000. 

- Sundaram, R., Vullikanti, A., Xu, H., and Yao, F. PAClearning for strategic classification. In _International Conference on Machine Learning_ , pp. 9978–9988. PMLR, 2021. 

- Tsirtsis, S. and Gomez Rodriguez, M. Decisions, counterfactual explanations and strategic behavior. _Advances in Neural Information Processing Systems_ , 33:16749– 16760, 2020. 

- Zhang, H. and Conitzer, V. Incentive-aware PAC learning. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 35, pp. 5797–5804, 2021. 

- Zrnic, T., Mazumdar, E., Sastry, S., and Jordan, M. Who leads and who follows in strategic classification? _Advances in Neural Information Processing Systems_ , 34, 2021. 

11 

**Causal Strategic Classification: A Tale of Two Shifts** 

# **A. Proofs** 

## **A.1. Lemma 1** 

_Proof._ Let _p_ ( _xr, y_ ) be some base distribution, and let _f_ be a classifier _f_ : _Xr →Y_ . Given _f_ , denote _x_<sup>_′_</sup> _r_<sup>=∆</sup><sup>_f_(</sup><sup>_xr_), for</sup> which we can write the induced joint distribution as _p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _r_<sup>_y′_).To consider both</sup><sup>_xr_and</sup><sup>_x′_</sup> _r_<sup>together, we denote their joint</sup> distribution with _y_ by _q_<sup>_f_</sup> ( _xr, x_<sup>_′_</sup> _r_<sup>_, y′_), whose definition derives immediately from ∆</sup><sup>_f_.Since ∆</sup><sup>_f_is deterministic, we get that</sup> _q_<sup>_f_</sup> ( _x_<sup>_′_</sup> _r_<sup>_|xr_) = 1</sup><sup>_{_∆</sup><sup>_f_(</sup><sup>_xr_) =</sup><sup>_x_</sup> _r_<sup>_′}_= 1</sup><sup>_{xr∈_∆–</sup> _f_<sup>1(</sup><sup>_x_</sup> _r_<sup>_′_)</sup><sup>_}_.</sup> 

First, with the law of total probability, we get the following expression for the induced marginal density: 



For the induced conditional density, again using the law of total probability we get: 



Now, since _y_ is sampled jointly with _xr_ from _p_ , and since _x_<sup>_′_</sup> _r_<sup>is a function only of</sup><sup>_xr_(which in itself is non-causal), we get</sup> that _q_<sup>_f_</sup> ( _y|xr, x_<sup>_′_</sup> _r_<sup>) =</sup><sup>_p_(</sup><sup>_y|xr_).Also, from Bayes’ theorem, we have</sup><sup>_qf_(</sup><sup>_xr|x′_</sup> _r_<sup>) =</sup><sup>_qf_(</sup><sup>_x′_</sup> _r_<sup>_|xr_)</sup><sup>_<u>p</u>_</sup><sup><u>(</u></sup><sup>_xr_</sup><sup><u>)</u></sup> _p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _r_ )<sup>.With these we get</sup> 



## **A.2. Lemma 3** 

_Proof._ Let _p_ ( _x, u, y_ ) be some base distribution, and let _f_ be a classifier _f_ : _X →Y_ . Given _f_ , we denote _x_<sup>_′_</sup> = ∆ _f_ ( _x_ ), and define the joint distributions _p_<sup>_f_</sup> ( _x_<sup>_′_</sup> _, u, y_<sup>_′_</sup> ) and _q_<sup>_f_</sup> ( _x, u, x_<sup>_′_</sup> _, y_<sup>_′_</sup> ). From Eq. (20) and replacing _xr_ with _x_ , we get: 



For the induced conditional density, with the law of total probability, we get: 



For a stochastic _h_<sup>_∗_</sup> = _p_<sup>_∗_</sup> , since _xc, u_ are both causal (and _xr_ is not), and since they jointly fully determine _y_ (up to irreducible noise in _h_<sup>_∗_</sup> ), we get that: 



Plugging in we get: 



Again using the law of total probability, generally we have: 



12 

**Causal Strategic Classification: A Tale of Two Shifts** 

However, this can be simplified using the fact that _x_<sup>_′_</sup> originates from some _x_ , i.e., _x_<sup>_′_</sup> = ∆ _f_ ( _x_ ). For the second term, since _x_<sup>_′_</sup> is a function of _x_ alone, we get that _q_<sup>_f_</sup> ( _u|x_<sup>_′_</sup> _, x_ ) = _p_ ( _u|x_ ). For the first term, and similarly to the proof in A.1, using Bayes’ theorem and the definition of ∆<sup>–</sup> _f_<sup>1we get:</sup> 



Plugging into the equation above gives: 



With the definition of _νf_ as: 



Taking out _p_ ( _u_ ) we can write: 



Plug it in back to Eq. (25), we get: 



In the case of a deterministic _h_<sup>_∗_</sup> , i.e. _p_<sup>_∗_</sup> ( _y_<sup>_′_</sup> _|x_<sup>_′_</sup> _c_<sup>_, u_) = 1</sup><sup>_{h∗_(</sup><sup>_x′_</sup> _c_<sup>_, u_) =</sup><sup>_y′}_, this simplifies to:</sup> 



Additionally, in the case where _x, u_ are independent, we get that _p_ ( _x|u_ ) = _p_ ( _x_ ), therefore: 



which gives: 



## **A.3. Lemma 2** 

_Proof._ This is a special case of Lemma 3. Replacing _x_ with _xc_ in Eq. (33) completes the proof. 

13 

**Causal Strategic Classification: A Tale of Two Shifts** 



<!-- Start of picture text -->
𝑥𝑟 = 𝑢<br>ℎ ∗<br>𝑓 𝑖𝑚𝑝 𝑓 𝑎𝑐𝑐<br>𝑥𝑐<br><!-- End of picture text -->

Figure 5: An optimal classifier for improvement is not necessarily optimal for accuracy. 

# **B. Additional results** 

## **B.1. Accuracy and improvement can be at odds** 

Fig. 5 illustrates the idea that an optimal classifier in terms of maximizing improvement is not necessarily optimal for maximizing accuracy. In this example, the red and the green circles represent clusters of negative points ( _y_ = _−_ 1) and positive points ( _y_ = 1) respectively. The decision boundary of _h_<sup>_∗_</sup> is illustrated by a dashed line, and _xr_ = _u_ . _f_<sup>imp</sup> makes all the negative points move from the red circle to its decision boundary; half of the points (the upper half of the circle) become positive ( _y_<sup>_′_</sup> = 1) since after movement their projection on their original _u_ = _xr_ lies in the positive region of _h_<sup>_∗_</sup> , and half of the points (the lower half of the circle) remains negative ( _y_<sup>_′_</sup> = _−_ 1) since after movement their projection on their original _xr_ lies in the negative region of _h_<sup>_∗_</sup> . The points from the lower half of the red circle could never become positive: no matter how they move, their projection on their original _xr_ will always lie in the negative region of _h_<sup>_∗_</sup> . Therefore, _f_<sup>imp</sup> turns all the possibly improvable points into positive and keeps all the originally positive points positive, hence it is optimal for maximizing improvement. However, since the points from the lower half of the red circle move to the decision boundary of _f_<sup>imp</sup> , they are classified as positive ( _y_ ˆ = 1), which means _f_<sup>imp</sup> err ( _y_ ˆ _̸_ = _y_<sup>_′_</sup> ) on each point from the lower half of the red circle. In contrast, _f_<sup>acc</sup> make only the positive points from the green circle to move, and after moving their projection on their original _xr_ stays in the positive region of _h_<sup>_∗_</sup> , therefore they are classified correctly ( _y_ ˆ = _y_<sup>_′_</sup> = 1); since the negative points from the red cluster don’t move they are also classified correctly ( _y_ ˆ = _y_<sup>_′_</sup> = _−_ 1), which means _f_<sup>acc</sup> gets 100% accuracy, hence it is an optimal classifier for maximizing accuracy, with higher accuracy than _f_<sup>imp</sup> . 

## **B.2. Efficient computation of** _x_ ˜ _r_ 

In this section, we show how to efficiently compute _x_ ˜ _r_ = E _xr∼p_ ˆ( _xr|xf_ )[ _xr_ ] for a linear _f_ and a generalized quadratic cost _cQ_ ( _x, x_<sup>_′_</sup> ) = ( _x_<sup>_′_</sup> _− x_ )<sup>_⊤_</sup> _Q_ ( _x_<sup>_′_</sup> _− x_ ) = _∥x_<sup>_′_</sup> _− x∥_<sup>2</sup> _Q_<sup>for PSD</sup><sup>_Q_.Recall that the idea underlying our definition of</sup><sup>_x_˜</sup><sup>_r_is that we’d</sup> like to ‘reconstruct’ _xr_ , to the best of our ability, given a strategically modified example _x_<sup>_f_</sup> . This is done by considering its likelihood, _p_<sup>_f_</sup> ( _xr|x_<sup>_f_</sup> ). We can express this likelihood using the clean marginal density: 



where 



14 

**Causal Strategic Classification: A Tale of Two Shifts** 

Using a model of the clean marginal density _p_ ˆ( _x_ ) _≈ p_ ( _x_ ) we can estimate _p_<sup>_f_</sup> ( _xr|x_<sup>_f_</sup> ) for any point by replacing _p_ with _p_ ˆ in this expression. The expected value of this likelihood is 





In practice, we compute these integrals numerically. 

# **C. Experimental details - synthetic data** 

In all of our synthetic experiments, we used 500 samples for clean training data, 150 samples of dirty data collected at each round (out of total _T_ = 10 rounds), 100 samples for validation set, and 400 samples for test set. We will now specify experimental details for each experiment. 

## **C.1. Experiment A - utilizing improvement** 

1. Structure of _h_<sup>_∗_</sup> : in this experiment, _h_<sup>_∗_</sup> is a linear function wrapped with a stochastic mechanism that creates noisy labels near the decision boundary. 

2. Structure _p_ ( _xc, u_ ): _p_ ( _xc, u_ ) is constructed from 3 normal distributed clusters: i) cluster of positive points with _µ_ = (2 _,_ 2) _, σ_<sup>2</sup> = 0 _._ 4 that contains 15% of the total points, ii) cluster of negative points with _µ_ = ( _−_ 5 _._ 5 _, −_ 5 _._ 5) _, σ_<sup>2</sup> = 0 _._ 6 that contains 10% of the total points, and iii) cluster of a mixture of positive and negative points with _µ_ = ( _−_ 2 _, −_ 2) _, σ_<sup>2</sup> = 0 _._ 6 that contains 75% of the total points. 

3. Cost scale = 0.035. 

4. Class of _h_ : polynomial model with a degree of 3. 

5. Hyper-parameters: _f_ learning-rate = 0.01, _h_ learning-rate = 0.01, batch-size = 64, sigmoid temperature =4 , _l_ 2 regularization coefficient for _f_ = 0, _l_ 2 regularization coefficient for _h_ = 0. 

15 

**Causal Strategic Classification: A Tale of Two Shifts** 

## **C.2. Experiment B - avoiding pitfalls** 

1. Structure of _h_<sup>_∗_</sup> : in this experiment, _h_<sup>_∗_</sup> has a circle shape with a center in (0 _,_ 0) where points inside the circle are labeled as positive and points outside it are labeled as negative. 

2. Structure _p_ ( _xc, u_ ): _p_ ( _xc, u_ ) is constructed from 2 normal distributed clusters: i) cluster of positive points with _µ_ = (0 _,_ 0) _, σ_<sup>2</sup> = 0 _._ 3 that contains 50% of the total points, ii) cluster of negative points with _µ_ = ( _−_ 5 _._ 5 _, −_ 5 _._ 5) _, σ_<sup>2</sup> = (0 _._ 3 _,_ 0 _._ 45) that contains 50% of the total points. 

3. Cost scale = 0.07 

4. Class of _h_ : polynomial model with a degree of 3. 

5. Hyper-parameters: _f_ learning-rate = 0.1, _h_ learning-rate = 0.1, batch-size = 64, sigmoid temperature = 20, _l_ 2 regularization coefficient for _f_ = 0.1, _l_ 2 regularization coefficient for _h_ = 0. 

## **C.3. Experiment C - XOR** 

1. Structure of _h_<sup>_∗_</sup> : in this experiment, _h_<sup>_∗_</sup> is constructed from 3 ellipses: 2 vertical ellipses with centers (2 _,_ 0) and ( _−_ 2 _,_ 0) and one horizontal ellipse with a canter (0 _,_ 0). Together these ellipses create a shape where points inside it are labeled as negative, and points outside it are labeled as negative. 

2. Structure _p_ ( _xc, u_ ): _p_ ( _xc, u_ ) is constructed from 4 normal distributed clusters, each contains 25% of the points and with _σ_<sup>2</sup> = 0 _._ 3: i) cluster of positive points with _µ_ = (0 _,_ 2 _._ 5), ii) cluster of positive points with _µ_ = (0 _, −_ 2 _._ 5) iii) cluster of negative points with _µ_ = (2 _._ 5 _,_ 0), and iiii) cluster of negative points with _µ_ = ( _−_ 2 _._ 5 _,_ 0). 

3. Cost scale = 0.08 

4. Class of _h_ : polynomial model with a degree of 4. 

5. Hyper-parameters: _f_ learning-rate = 0.05, _h_ learning-rate = 0.01, batch-size = 64, sigmoid temperature = 20, _l_ 2 regularization coefficient for _f_ = 1, _l_ 2 regularization coefficient for _h_ = 0.01, exploration regularization coefficient _λ_ = 5 with decay of 0.4. 

# **D. Experimental details - real data** 

## **D.1. Data and preprocessing** 

## D.1.1. CARD FRAUD 

**Data description.** The data is publicly available at https://www.kaggle.com/datasets/mlg-ulb/ creditcardfraud. This dataset contains transactions made by credit cards that occurred in two days during September 2013 by European cardholders. This data set is highly unbalanced and contained 492 frauds out of 284,807 transactions. The data contains 31 numerical features: ’Time’ which contains the seconds elapsed between each transaction and the first transaction in the dataset, ’Amount’ which is the transaction amount, and additional 29 features which are the result of a PCA transformation. 

**Preprocessing.** As preprocessing, we removed the ’Time’ feature and then performed Z-score normalization to the data, followed by a division by the square root of the data dimension. 

**Data augmentation.** Since this dataset contains only 492 negative samples, we created synthetic negative samples for the experiment by fitting a KDE model to the negative samples and then sampling generated samples from the model. 

**Data split.** We sampled 5500 balanced samples for the experiment and set 3000 of them ( _∼_ 54%) as training data, 500 ( _∼_ 9%) as validation data, and 2000 ( _∼_ 36%) as test data. The baseline that doesn’t use time used all of the training data in a single round. For the methods that do use time, including ours, we split the training data into 1000 clean samples and 2000 assigned to be dirty samples, partitioned into 10 batches of 200 samples each. in the first round, they got access only to the clean samples, and then during 10 rounds, each round _t_ , they got access to additional 200 dirty samples that were created by applying ∆ _f_ on the _t_ -batch of the dirty samples inventory. 

**Experiment repetition.** We repeated the experiment 15 times, each time with a random data split. The reported results are the averages and standard error over these random splits. 

16 

**Causal Strategic Classification: A Tale of Two Shifts** 

## D.1.2. SPAM 

**Data description.** The data can be obtained by the authors of Costa et al. (2014). The data includes features describing users of a large social network, some of which are spammers. The data is balanced with a total of 7076 samples and contains 60 numerical features and binary labels (spammer or not). 

**Preprocessing.** As preprocessing, we kept only 15 features: qTips ~~p~~ lc, rating ~~p~~ lc, qEmail ~~t~~ ip, qContacts ~~t~~ ip, qURL ~~t~~ ip, qPhone tip, qNumeriChar ~~t~~ ip, sentistrength ~~t~~ ip, combined ~~t~~ ip, qWords ~~t~~ ip, followers ~~f~~ ollowees ~~g~~ ph, qUnigram ~~a~~ vg ~~t~~ ip’, qTips usr, indeg gph, qCapitalChar ~~t~~ ip. After removing the other features we performed Z-score normalization on the data, followed by a division by the square root of the data dimension. 

**Data split.** Same as in card fraud. 

**Experiment repetition.** Same as in card fraud. 

## **D.2. Feature partition and labeling function** _h_<sup>_∗_</sup> 

## D.2.1. CARD FRAUD 

**Feature partition.** After preprocessing we selected 6 features to be _xc_ , and 16 features to be _u_ . We create _xr_ by takings the first 6 features from _u_ and multiplying them by a random square matrix. 

**Labeling function.** We created _h_<sup>_∗_</sup> by fitting an MLP with 3 hidden layers with hidden dimensions of 10 on a balanced subset of the original data (before augmenting it with a KDE). We then wrapped the MLP model with a stochastic mechanism that given an input _x_ , assigns a probability _p_ as a function of the distance of _x_ from the decision boundary of the model and then multiply the scores MLP( _x_ ) by _−_ 1 with a probability of _p_ . After assigning score _s_ to a sample, its label is sign( _s_ ). In this way, points from the region near the decision boundary of _h_<sup>_∗_</sup> have noisy labels and they are a mixture of negative and positive points. 

## D.2.2. SPAM 

**Feature partition.** After preprocessing we selected 3 features to be _xc_ , and 12 features to be _u_ . We create _xr_ by takings the first 2 features from _u_ and multiplying them by a random square matrix. 

**Labeling function.** We created _h_<sup>_∗_</sup> by first fitting a linear model _g_ on the data. We then wrapped the _g_ with a ’tricky-feature’ mechanism defined for a feature _ci_ , a threshold _γ_ and a slope _β_ : given an input _x_ , if _xci > γ_ , then replace the score _s_ = _g_ ( _x_ ) of the linear model with _s ← g_ ( _x_ ) _− β_ ( _xci − γ_ ). After assigning score _s_ to a sample, its label is sign( _s_ ). We used _γ_ = 0 _._ 05 and _β_ = 20; these values were chosen such that this mechanism will cause label flip to only _∼_ 5% of the original data. 

## **D.3. Density estimation** 

For both usages of a density model in our algorithm, _p_ ˆ and _q_ ˆ, we used KDE with a Gaussian kernel. The hyper-parameter of the model is the kernel bandwidth, which we choose using a grid search cross-validation. 

## **D.4. Training, tuning, and optimization** 

For both card fraud and spam experiments, we used the following parameters, which we choose manually: 

1. class of _h_ : MLP with 3 layers with a width of 10 

2. _f_ , _h_ learning-rate = 0.01 

3. batch size = 64 

4. epochs = 100 

5. an early stopping mechanism when there are 7 consecutive epochs without accuracy improvement on the validation set 

6. sigmoid temperature _τ_ = 4 

7. exploration regularization coefficients: in `CSERM` _λ_ = 0 _._ 1 we used _λ_ 0 = 0 _._ 1 which decays in each round with factor of 0.4. in `CSERM` _λ_ = 1 we used _λ_ 0 = 1 which decays in each round with factor of 0.4. 

17 

**Causal Strategic Classification: A Tale of Two Shifts** 



<!-- Start of picture text -->
card fraud spam<br>0.85 0.90<br>0.85 method<br>CSERM - best<br>0.80 0.80 CSERM - @t=1<br>SERM - best<br>RRM - best<br>0.75 0.75 RRM - @t=1<br>ERM - best<br>0.70<br>0.70<br>0.65<br>0.65 0.60<br>1/6 1/3 1/2 2/3 5/6 1/6 1/3 1/2 2/3 5/6<br>clean data ratio clean data ratio<br>accuracy accuracy<br><!-- End of picture text -->

Figure 6: Accuracy across different ratios of clean vs dirty data. 

In each experiment, we used a different cost scale _α_ , chosen such that there will _∼_ 50% of strategically moving points: at card fraud we used _α_ = 1, and in spam we used _α_ = 40. 

## **D.5. Baselines and benchmarks** 

In our experiments, we used two benchmarks: 

1. `ns-bench` : the result of a na¨ıve `ERM` tested on a non-strategic test; this benchmark shows us the maximal possible accuracy when there is no strategic behavior. 

2. `oracle` : our method ( `CSERM` ) with oracle access to _h_<sup>_∗_</sup> and _u_ , therefore in training it can accurately fix _y �→ y_<sup>_′_</sup> , for moving points; this benchmark shows us the maximal possible accuracy in a causal strategic setting, where there are no information gaps to the learner. 

Additionally, we used the following baselines: 

1. `ERM` : simulate a na¨ıve learner who doesn’t aware to strategic behaviour. The results of this baseline show us how much the learner can lose by not accounting for strategic behavior. 

2. `SERM` : a strategically-aware but causally-oblivious baseline that optimizes Eq. (2) using the strategic hinge loss (Levanon & Rosenfeld, 2022). The results of this baseline show us how much the learner can lose by accounting only for the strategic movement of _x_ and not for the possible change in the label _y_ . 

3. `RRM` : a baseline that uses time by collecting dirty data at each round, and at each round applies `ERM` using only the last collected dataset. This baseline simulates a learner that is aware of the distribution shift, but either doesn’t know the structure of the shift or simply doesn’t know how to tackle the problem of the specific distribution shift caused by strategic behavior and causality. 

4. `RRM` _≤t_ : a version of `RRM` that at each round uses the collected data from all previous rounds. This baseline simulates a learner that is aware of the fact that data from various distributions can be useful for learning under the distribution shift. 

5. `RRMc` : a version of `RRM` _≤t_ that uses only causal features and uses all previous data. This baseline simulates a learner that is aware of the causal strategic structure of the distribution shift, knows the partition of features to _xc_ and _xr_ , and chooses to use only _xc_ to avoid dealing with ‘gaming’ behavior that the use of _xr_ causes. 

6. `CSERM` : our approach, without regularizing for exploration. 

7. `CSERM` _λ_ = 0 _._ 1: our approach with exploration regularization coefficient of 0 _._ 1 in the first round, and decaying with a factor of 0 _._ 4 in each round. 

8. `CSERM` _λ_ = 1: our approach with exploration regularization coefficient of 1 in the first round, and decaying with a factor of 0 _._ 4 in each round. 

18 

**Causal Strategic Classification: A Tale of Two Shifts** 



<!-- Start of picture text -->
card fraud spam<br>0.95<br>0.90<br>0.90<br>0.85<br>method<br>0.85<br>0.80 CSERM = 1<br>CSERM<br>0.75 0.80 SERM<br>RRM<br>0.70 0.75 ERM<br>0.65 0.70<br>0.60 0.65<br>12 2 4 12 2 4<br>cost scale cost scale<br>accuracy accuracy<br><!-- End of picture text -->

Figure 7: Accuracy across different cost scales. 

# **E. Additional experimental results** 

## **E.1. Varying clean data ratio** 

This experiment tests the effect of the ratio of clean vs. dirty data on the performance of temporal methods that use dirty data over time in addition to clean data. Towards this, for each _r ∈{_<sup><u>1</u></sup> 6<sup>_,_</sup><sup><u>1</u></sup> 3<sup>_,_</sup><sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>2</u></sup> 3<sup>_,_</sup><sup><u>5</u></sup> 6<sup>_}_we assigned an</sup><sup>_r_-fraction of the training data</sup> to include clean example, and the remaining 1 _− r_ -fraction to include dirty samples, while keeping the total size of training data fixed to 3,000 samples. Figure 6 plots performance as a function of _r_ . As can be seen, the overall trend of the effect of _r_ on accuracy changes across methods and datasets. However, results show that our approach remains effective across the entire spectrum of _r_ , i.e. both when the number of clean samples is relatively small, and when it is relatively large. 

## **E.2. Varying cost scales** 

In this section we report results for all methods and for multiple cost scales _α_ . Our results in the main paper (Table 1 in Sec. 6) show performance for _α_ chosen such that _∼_ 50% of points move (per dataset): in card fraud we set _α_ = 1, and in spam we set _α_ = 40. Here we show results for other cost scales, including<sup><u>1</u></sup> 2<sup>_α_,</sup><sup>_α_,2</sup><sup>_α_,and4</sup><sup>_α_.Figure7plots</sup> performance as a function of _α_ . As can be seen, in each dataset the relations between the accuracies of the baseline remain similar across different cost scales, but as the cost scale decreases, there is less movement, and the absolute gap between the methods decreases as well. The next pages include tables reporting full results for all considered cost scales, first for card fraud, and then for spam. 

19 

**Causal Strategic Classification: A Tale of Two Shifts** 

||||**card **|**fraud, cos**|**t scale **<sup>**1**</sup><br>**2**<sup>**_α_**</sup>|||
|---|---|---|---|---|---|---|---|
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|91.5_±_0_._2|95.2|15.3|59.9|16.9|1.5|-0.67|
|`CSERM`_λ_ = 0_._1|91.2_±_0_._3|94.9|15.0|59.6|16.4|1.5|-0.7|
|`CSERM`|90.7_±_0_._4|95.0|14.4|59.7|16.0|1.6|-0.57|
|`SERM`|79.7_±_0_._2|77.5|2.2|55.5|3.4|1.2|-0.24|
|`RRM`|72.7_±_0_._8|73.5|0.7|24.6|0.9|0.2|0.05|
|`RRM`_≤t_|69.6_±_0_._2|77.7|0.3|16.1|0.3|0.0|0.2|
|`RRMc`|60.8_±_0_._3|74.8|0.4|22.8|0.5|0.0|0.4|
|`ERM`|61.4_±_0_._6|77.5|0.6|26.7|0.6|0.0|0.30|
|`oracle`|89.8_±_0_._2|94.2|13.0|58.5|14.4|1.4|-0.72|
|`ns-bench`|77.5_±_0_._2|-|-|-|-|-|-|
||||**card **|**fraud, co**|**st scale****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|87.8_±_0_._2|93.5|12.2|60.1|13.8|1.7|-0.65|
|`CSERM`_λ_ = 0_._1|87.7_±_0_._2|93.6|11.4|58.9|13.0|1.6|-0.5|
|`CSERM`|86.6_±_0_._5|93.4|10.2|58.9|11.8|1.5|-0.48|
|`SERM`|78.4_±_0_._2|77.5|0.8|45.9|1.6|0.7|-0.16|
|`RRM`|75.8_±_0_._5|70.5|0.5|24.7|0.7|0.2|-0.06|
|`RRM`_≤t_|71.6_±_0_._2|77.6|0.2|12.5|0.2|0.0|0.2|
|`RRMc`|63.6_±_0_._3|74.7|0.3|18.8|0.3|0.0|0.4|
|`ERM`|66.7_±_0_._6|77.5|0.3|19.8|0.4|0.0|0.25|
|`oracle`|87.0_±_0_._2|93.3|10.1|57.9|11.8|1.6|-0.60|
|`ns-bench`|77.5_±_0_._2|-|-|-|-|-|-|
||||**card **|**fraud, cos**|**t scale 2****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|82.8_±_0_._3|92.4|6.3|57.8|7.5|1.2|-0.58|
|`CSERM`_λ_ = 0_._1|82.3_±_0_._5|92.3|6.5|58.8|7.7|1.2|-0.7|
|`CSERM`|82.4_±_0_._4|92.8|5.8|57.9|7.0|1.2|-0.52|
|`SERM`|77.8_±_0_._1|77.6|0.3|22.7|0.7|0.4|-0.05|
|`RRM`|77.0_±_0_._3|69.9|0.1|22.9|0.3|0.3|-0.11|
|`RRM`_≤t_|73.6_±_0_._1|77.5|0.1|8.7|0.1|0.0|0.2|
|`RRMc`|64.9_±_0_._3|74.2|0.2|15.9|0.2|0.0|0.4|
|`ERM`|70.6_±_0_._4|77.5|0.1|13.5|0.2|0.0|0.22|
|`oracle`|83.6_±_0_._1|91.4|6.7|56.9|8.0|1.3|-0.53|
|`ns-bench`|77.5_±_0_._2|-|-|-|-|-|-|
||||**card **|**fraud, cos**|**t scale 4****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|79.1_±_0_._5|85.9|2.5|35.4|3.1|0.6|-0.30|
|`CSERM`_λ_ = 0_._1|79.2_±_0_._4|88.2|2.3|42.0|3.0|0.6|-0.4|
|`CSERM`|78.2_±_0_._3|85.3|0.8|29.1|1.1|0.4|-0.14|
|`SERM`|77.5_±_0_._1|77.5|0.0|7.3|0.2|0.2|0.06|
|`RRM`|77.8_±_0_._2|70.9|0.4|18.8|0.5|0.1|-0.08|
|`RRM`_≤t_|74.8_±_0_._2|77.7|0.0|6.6|0.1|0.0|0.2|
|`RRMc`|66.6_±_0_._3|74.0|0.2|12.9|0.2|0.0|0.3|
|`ERM`|73.5_±_0_._3|77.5|0.1|8.7|0.1|0.0|0.20|
|`oracle`|79.6_±_0_._5|85.6|2.3|38.4|2.9|0.6|-0.37|
|`ns-bench`|<br>77.5_±_0_._2|-|-|-|-|-|-|



20 

**Causal Strategic Classification: A Tale of Two Shifts** 

||||**spa**|**m, cost sca**|**le **<sup>**1**</sup><br>**2**<sup>**_α_**</sup>|||
|---|---|---|---|---|---|---|---|
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|94.2_±_0_._1|97.6|6.4|57.0|6.4|0.0|-0.27|
|`CSERM`_λ_ = 0_._1|94.0_±_0_._2|97.9|5.8|53.9|5.8|0.0|-0.3|
|`CSERM`|94.1_±_0_._1|97.6|5.8|52.8|5.8|0.0|-0.25|
|`SERM`|78.6_±_0_._6|91.2|-12.6|56.0|0.0|12.6|-0.36|
|`RRM`|72.5_±_2_._9|76.9|0.4|36.1|1.3|0.9|0.13|
|`RRM`_≤t_|74.0_±_0_._8|90.9|0.1|21.0|0.3|0.2|0.2|
|`RRMc`|74.9_±_0_._6|87.1|-1.2|21.6|0.2|1.4|0.2|
|`ERM`|65.6_±_0_._3|91.2|0.4|27.0|0.4|0.0|0.26|
|`oracle`|94.4_±_0_._1|94.4|6.1|58.6|6.1|0.0|-0.31|
|`ns-bench`|91.2_±_0_._1|-|-|-|-|-|-|
||||**spa**|**m, cost sc**|**ale****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|92.7_±_0_._5|97.0|3.1|37.5|3.2|0.1|-0.23|
|`CSERM`_λ_ = 0_._1|92.6_±_0_._4|97.3|2.9|37.2|2.9|0.0|-0.1|
|`CSERM`|92.4_±_0_._4|97.1|2.4|36.7|2.5|0.1|-0.21|
|`SERM`|84.0_±_0_._3|91.2|-7.2|41.3|0.0|7.2|-0.17|
|`RRM`|77.2_±_2_._4|76.6|-2.1|30.5|0.6|2.8|0.07|
|`RRM`_≤t_|78.7_±_0_._6|91.2|0.1|14.8|0.3|0.1|0.2|
|`RRMc`|79.1_±_0_._6|87.4|-0.8|15.8|0.2|1.1|0.2|
|`ERM`|75.4_±_0_._3|91.2|0.4|17.1|0.4|0.0|0.23|
|`oracle`|93.5_±_0_._1|93.5|4.5|41.7|4.5|0.0|-0.17|
|`ns-bench`|91.2_±_0_._1|-|-|-|-|-|-|
||||**spa**|**m, cost sca**|**le 2****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|89.3_±_0_._4|94.3|-1.3|21.6|0.2|1.5|-0.03|
|`CSERM`_λ_ = 0_._1|88.9_±_0_._3|95.8|-1.8|22.4|0.1|1.9|0.0|
|`CSERM`|89.4_±_0_._4|95.1|-1.4|22.0|0.2|1.5|-0.05|
|`SERM`|87.1_±_0_._1|91.2|-4.1|25.7|0.0|4.1|-0.07|
|`RRM`|80.4_±_2_._0|79.0|-2.3|22.1|0.3|2.6|0.00|
|`RRM`_≤t_|82.6_±_0_._6|90.9|0.1|9.7|0.2|0.1|0.2|
|`RRMc`|81.7_±_0_._4|87.5|-0.4|11.5|0.2|0.6|0.2|
|`ERM`|81.8_±_0_._3|91.2|0.2|10.5|0.2|0.0|0.22|
|`oracle`|89.0_±_0_._3|89.0|-1.9|23.2|0.0|1.9|-0.04|
|`ns-bench`|91.2_±_0_._1|-|-|-|-|-|-|
||||**spa**|**m, cost sca**|**le 4****_α_**|||
||accuracy|perceived|%improve|%move|%neg_�→_pos|%pos_�→_neg|welfare|
|`CSERM`_λ_ = 1|89.1_±_0_._1|93.5|-1.6|11.8|0.0|1.6|0.06|
|`CSERM`_λ_ = 0_._1|89.0_±_0_._2|93.2|-1.6|11.9|0.0|1.6|0.1|
|`CSERM`|89.1_±_0_._2|93.4|-1.7|12.4|0.0|1.7|0.07|
|`SERM`|88.9_±_0_._1|91.2|-2.3|15.4|0.0|2.3|0.01|
|`RRM`|83.3_±_1_._9|81.2|-0.8|16.3|0.2|1.0|0.02|
|`RRM`_≤t_|84.8_±_0_._4|91.0|0.0|7.2|0.1|0.1|0.2|
|`RRMc`|83.6_±_0_._2|87.4|-0.2|8.3|0.1|0.3|0.2|
|`ERM`|85.4_±_0_._2|91.2|0.0|6.8|0.0|0.0|0.20|
|`oracle`|89.1_±_0_._1|89.1|-1.9|13.2|0.0|1.9|0.05|
|`ns-bench`|<br>91.2_±_0_._1|-|-|-|-|-|-|



21 

