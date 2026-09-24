---
title: "Performative Prediction"
authors: "perdomo"
year: 2020
arxiv_id: "2002.06673"
original_file: "2002.06673.pdf"
pdf_path: "docs/papers\2020_perdomo_performative_prediction.pdf"
---

# Performative Prediction

**Authors:** Perdomo et al.  
**Year:** 2020 | **arXiv:** [`2002.06673`](https://arxiv.org/abs/2002.06673)  
**Local PDF:** [`2020_perdomo_performative_prediction.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_perdomo_performative_prediction.pdf)

---

# Performative Prediction 

Juan C. Perdomo* Tijana Zrnic* Celestine Mendler-Dünner Moritz Hardt {jcperdomo, tijana.zrnic, mendler, hardt}@berkeley.edu 

University of California, Berkeley 

March 2, 2021 

#### Abstract 

When predictions support decisions they may influence the outcome they aim to predict. We call such predictions _performative_ ; the prediction influences the target. Performativity is a well-studied phenomenon in policy-making that has so far been neglected in supervised learning. When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining. 

We develop a risk minimization framework for performative prediction bringing together concepts from statistics, game theory, and causality. A conceptual novelty is an equilibrium notion we call performative stability. Performative stability implies that the predictions are calibrated not against past outcomes, but against the future outcomes that manifest from acting on the prediction. Our main results are necessary and sufficient conditions for the convergence of retraining to a performatively stable point of nearly minimal loss. 

In full generality, performative prediction strictly subsumes the setting known as _strategic classification_ . We thus also give the first sufficient conditions for retraining to overcome strategic feedback effects. 

## 1 Introduction 

Supervised learning excels at pattern recognition. When used to support consequential decisions, however, predictive models can trigger actions that influence the outcome they aim to predict. We call such predictions _performative_ ; the prediction causes a change in the distribution of the target variable. 

Consider a simplified example of predicting credit default risk. A bank might estimate that a loan applicant has an elevated risk of default, and will act on it by assigning a high interest rate. In a self-fulfilling prophecy, the high interest rate further increases the customer's default risk. Put differently, the bank's predictive model is not calibrated to the outcomes that manifest from acting on the model. 

Once recognized, performativity turns out to be ubiquitous. Traffic predictions influence traffic patterns, crime location prediction influences police allocations that may deter crime, recommendations shape preferences and thus consumption, stock price prediction determines trading activity and hence prices. 

* Equal contribution. 

1 

When ignored, performativity can surface as a form of _distribution shift_ . As the decisionmaker acts according to a predictive model, the distribution over data points appears to change over time. In practice, the response to such distribution shifts is to frequently _retrain_ the predictive model as more data becomes available. Retraining is often considered an undesired — yet necessary — cat and mouse game of chasing a moving target. 

What would be desirable from the perspective of the decision maker is a certain equilibrium where the model is optimal for the distribution it induces. Such equilibria coincide with the stable points of retraining, that is, models invariant under retraining. Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance. 

This raises fundamental questions. When do such stable points exist? How can we efficiently find them? Under what conditions does retraining converge? When do stable points also have good predictive performance? In this work, we formalize performative prediction, tying together conceptual elements from statistical decision theory, causal reasoning, and game theory. We then resolve some of the fundamental questions that performativity raises. 

### 1.1 Our contributions 

We put performativity at the center of a decision-theoretic framework that extends the classical statistical theory underlying risk minimization. The goal of risk minimization is to find a decision rule, specified by model parameters _θ_ , that performs well on a fixed joint distribution D over covariates _X_ and an outcome variable _Y_ . 

Whenever predictions are performative, the choice of predictive model affects the observed distribution over instances _Z_ = ( _X,Y_ ). We formalize this intuitive notion by introducing a map D(·) from the set of model parameters to the space of distributions. For a given choice of parameters _θ_ , we think of D( _θ_ ) as the distribution over features and outcomes that results from making decisions according to the model specified by _θ_ . This mapping from predictive model to distribution is the key conceptual device of our framework. 

A natural objective in performative prediction is to evaluate model parameters _θ_ on the resulting distribution D( _θ_ ) as measured via a loss function _ℓ_ . This results in the notion we call _performative risk_ , defined as 



The difficulty in minimizing PR( _θ_ ) is that the distribution itself depends on the argument _θ_ , a dependence that defeats traditional theory for risk minimization. Moreover, we generally envision that the map D(·) is unknown to the decision maker. 

Perhaps the most natural algorithmic heuristic in this situation is a kind of fixed point iteration: repeatedly find a model that minimizes risk on the distribution resulting from the previous model, corresponding to the update rule 



We call this procedure _repeated risk minimization_ . We also analyze its empirical counterpart that works in finite samples. These procedures exemplify a family of _retraining_ heuristics that are ubiquitous in practice for dealing with all kinds of distributions shifts irrespective of cause. 

2 

When repeated risk minimization converges in objective value the model has minimal loss on the distribution it entails: 



We refer to this condition as _performative stability_ , noting that it is neither implied by nor does it imply minimal performative risk. 

Our central result can be summarized informally as follows. 

Theorem 1.1 (Informal). _If the loss is smooth, strongly convex, and the mapping_ D(·) _is sufficiently Lipschitz, then repeated risk minimization converges to performative stability at a linear rate._ 

_Moreover, if any one of these assumptions does not hold, repeated risk minimization can fail to converge at all._ 

The notion of Lipschitz continuity here refers to the Euclidean distance on model parameters and the Wasserstein distance on distributions. Informally, it requires that a small change in model parameters _θ_ does not have an outsized effect on the induced distribution D( _θ_ ). 

In contrast to standard supervised learning, convexity alone is _not_ sufficient for convergence in objective value, even if the other assumptions hold. Performative prediction therefore gives a new and interesting perspective on the importance of strong convexity. 

Strong convexity has a second benefit. Not only does retraining converge to a stable point at a linear rate, this stable point also approximately minimizes the performative risk. 

Theorem 1.2 (Informal). _If the loss is Lipschitz and strongly convex, and the map_ D(·) _is Lipschitz, all stable points and performative optima lie in a small neighborhood around each other._ 

Recall that performative stability on its own does not imply minimal performative risk. What the previous theorem shows, however, is that strong convexity guarantees that we can approximately satisfy both. 

We complement our main results with a case study in _strategic classification_ . Strategic classification aims to anticipate a strategic response to a classifier from an individual, who can change their features prior to being classified. We observe that strategic classification is a special case of performative prediction. On the one hand, this allows us to transfer our technical results to this established setting. In particular, our results are the first to give a guarantee on repeated risk minimization in the strategic setting. On the other hand, strategic classification provides us with one concrete setting for what the mapping D(·) can be. We use this as a basis of an empirical evaluation in a semi-synthetic setting, where the initial distribution is based on a real data set, but the distribution map is modeled. 

### 1.2 Related work 

Performativity is a broad concept in the social sciences, philosophy, and economics [18, 30]. Below we focus on the relationship of our work to the most relevant technical scholarship. 

Learning on non-stationary distributions. A closely related line of work considers the problem of _concept drift_ , broadly defined as the problem of learning when the target distribution over instances drifts with time. This setting has attracted attention both in the learning theory community [2, 3, 27] and by machine learning practitioners [14]. 

Concept drift is more general phenomenon than performativity in that it considers arbitrary sources of shift. However, studying the problem at this level of generality has led to a number 

3 

of difficulties in creating a unified language and objective [14, 40], an issue we circumvent by assuming that the population distribution is determined by the deployed predictive model. Importantly, this line of work also discusses the importance of retraining [14, 41]. However, it stops short of discussing the need for stability or analyzing the long-term behavior of retraining. 

Strategic classification. Strategic classification recognizes that individuals often adapt to the specifics of a decision rule so as to gain an advantage (see, e.g., [8, 11, 15, 24]). Recent work in this area considers issues of incentive design [4, 25, 32, 37], control over an algorithm [10], and fairness concerns [20, 33]. Importantly, the concurrent work of Bechavod et al. [4] analyzes the implications of retraining in the context of causal discovery in linear models. Our model of performative prediction includes all notions of strategic adaption that we are aware of as a special case. Unlike many works in this area, our results do not depend on a specific _cost function_ for changing individual features. Rather, we rely on an assumption about the sensitivity of the data-generating distribution to changes in the model parameters. 

Recently, there has been increased interest within the algorithmic fairness community in classification dynamics. See, for example, Liu et al. [28], Hu and Chen [19], and Hashimoto et al. [17]. The latter work considers repeated risk minimization, but from the perspective of what it does to a measure of disparity between groups. 

Causal inference. The reader familiar with causality can think of D( _θ_ ) as the interventional distribution over instances _Z_ resulting from a do-intervention that sets the model parameters to _θ_ in some underlying causal graph. Importantly, this mapping D(·) remains fixed and does not change over time or by intervention: deploying the same model at two different points in time must induce the same distribution over observations _Z_ . While causal inference focuses on estimating properties of interventional distributions such as treatment effects [21, 35], our focus is on a new stability notion and iterative retraining procedures for finding stable points. 

Convex optimization. The two solution concepts we introduce generalize the usual notion of optimality in (empirical) risk minimization to our new framework of performativity. Similarly, we extend the classical property of gradient descent acting as a contraction under smooth and strongly convex losses to account for distribution shifts due to performativity. Finally, we discuss how different regularity assumptions on the loss function affect convergence of retraining schemes, much like optimization works discuss these assumptions in the context of convergence of iterative optimization algorithms. 

Reinforcement learning. In general, any instance of performative prediction can be reframed as a reinforcement learning or contextual bandit problem. Yet, by studying performative prediction problems within such a broad framework, we lose many of the intricacies of performativity which make the problem interesting and tractable to analyze. We return to discuss some of the connections between both frameworks later on. 

## 2 Framework and main definitions 

In this section, we formally introduce the principal solution concepts of our framework: performative optimality and performative stability. 

4 

Throughout our presentation, we focus on predictive models that are parametrized by a vector _θ_ ∈ Θ, where the parameter space Θ ⊆ R<sup>_d_</sup> is a closed, convex set. We use capital letters to denote random variables and their lowercase counterparts to denote realizations of these variables. We consider instances _z_ = ( _x,y_ ) defined as feature, outcome pairs, where _x_ ∈ R<sup>_m_−1</sup> and _y_ ∈ R. Whenever we define a variable _θ_<sup>∗</sup> = argmin _θ g_ ( _θ_ ) as the minimizer of a function _g_ , we resolve the issue of the minimizer not being unique by setting _θ_<sup>∗</sup> to an arbitrary point in the argmin _θ g_ ( _θ_ ) set. 

### 2.1 Performative optimality 

In supervised learning, the goal is to learn a predictive model _fθ_ which minimizes the expected loss with respect to feature, outcome pairs ( _x,y_ ) drawn i.i.d. from a fixed distribution D. The optimal model _fθ_ SL solves the following optimization problem, 



where _ℓ_ ( _z_ ; _θ_ ) denotes the loss of _fθ_ at a point _z_ . 

We contrast this with the _performative optimum_ . As introduced previously, in settings where predictions support decisions, the manifested distribution over features and outcomes is in part determined by the deployed model. Instead of considering a fixed distribution D, each model _fθ_ induces a potentially different distribution D( _θ_ ) over instances _z_ . A predictive model must therefore be evaluated with regard to the expected loss over the distribution D( _θ_ ) it induces: its _performative risk_ . 

Definition 2.1 (performative optimality and risk). A model _fθ_ PO is _performatively optimal_ if the following relationship holds: 



We define PR( _θ_ )<sup>def</sup> = E _Z_ ∼D( _θ_ ) _ℓ_ ( _Z_ ; _θ_ ) as the _performative risk_ ; then, _θ_ PO = argmin _θ_ PR( _θ_ ). 

The following example illustrates the differences between the traditional notion of optimality in supervised learning and performative optima. 

Example 2.2 (biased coin flip). Consider the task of predicting the outcome of a biased coin flip where the bias of the coin depends on a feature _X_ and the assigned score _fθ_ ( _X_ ). 

In particular, define D( _θ_ ) in the following way. _X_ is a 1-dimensional feature supported on {±1} and _Y_ | _X_ ∼ Bernoulli(<sup><u>1</u></sup> 2<sup>+</sup><sup>_µX_+</sup><sup>_εθX_) with</sup><sup>_µ_∈(0</sup><sup>_,_</sup><sup><u>1</u></sup> 2<sup>) and</sup><sup>_ε <_</sup><sup><u>1</u></sup> 2<sup>−</sup><sup>_µ_.Assume that the class</sup> of predictors consists of linear models of the form _fθ_ ( _x_ ) = _θx_ +<sup><u>1</u></sup> 2<sup>and that the objective is to</sup> minimize the squared loss: _ℓ_ ( _z_ ; _θ_ ) = ( _y_ − _fθ_ ( _x_ ))<sup>2</sup> . 

The parameter _ε_ represents the performative aspect of the model. If _ε_ = 0, outcomes are independent of the assigned scores and the problem reduces to a standard supervised learning task where the optimal predictive model is the conditional expectation _fθ_ SL( _x_ ) = E[ _Y_ | _X_ = _x_ ] = <u>12</u><sup>+</sup><sup>_µx_, with</sup><sup>_θ_SL =</sup><sup>_µ_.</sup> 

In the performative setting with _ε_ � 0, the optimal model _θ_ PO balances between its predictive accuracy as well as the bias induced by the prediction itself. In particular, a direct calculation demonstrates that 



5 

Hence, the performative optimum and the supervised learning solution are equal if _ε_ = 0 and diverge as the performativity strength _ε_ increases. 

### 2.2 Performative stability 

A natural, desirable property of a model _fθ_ is that, given that we use the predictions of _fθ_ as a basis for decisions, those predictions are also simultaneously optimal for distribution that the model induces. We introduce the notion of _performative stability_ to refer to predictive models that satisfy this property. 

Definition 2.3 (performative stability and decoupled risk). A model _fθ_ PS is _performatively stable_ if the following relationship holds: 



We define DPR( _θ,θ_<sup>′</sup> )<sup>def</sup> = E _Z_ ∼D( _θ_ ) _ℓ_ ( _Z_ ; _θ_<sup>′</sup> ) as the _decoupled performative risk_ ; then, _θ_ PS = argmin _θ_ DPR( _θ_ PS _,θ_ ). 

A performatively stable model _fθ_ PS minimizes the expected loss on the distribution D( _θ_ PS) resulting from deploying _fθ_ PS in the first place. Therefore, a model that is performatively stable eliminates the need for retraining after deployment since any retraining procedure would simply return the same model parameters. Performatively stable models are _fixed points_ of risk minimization. We further develop this idea in the next section. 

Observe that performative optimality and performative stability are in general two distinct solution concepts. Performatively optimal models need not be performatively stable and performatively stable models need not be performatively optimal. We illustrate this point in the context of our previous biased coin toss example. 

Example 2.2 (continued). Consider again our model of a biased coin toss. In order for a predictive model _fθ_ to be performatively stable, it must satisfy the following relationship: 



Solving for _θ_ PS directly, we see that there is a unique performatively stable point. 

Therefore, performative stability and performative optimality need not identify. In fact, in this example they identify if and only if _ε_ = 0. Note that, in general, if the map D( _θ_ ) is constant across _θ_ , performative optima must coincide with performatively stable solutions. Furthermore, both coincide with "static" supervised learning solutions as well. 

For ease of presentation, we refer to a choice of parameters _θ_ as performatively stable (optimal) if the model parametrized by _θ_ , _fθ_ is performatively stable (optimal). We will occasionally also refer to performative stability as simply stability. 

Remark 2.4. _Notice that both performative stability and optimality can be expressed via the decoupled performative risk as follows:_ 



6 

## 3 When retraining converges to stable points 

Having introduced our framework for performative prediction, we now address some of the basic questions that arise in this setting and examine the behavior of common machine learning practices, such as retraining, through the lens of performativity. 

As discussed previously, performatively stable models have the favorable property that they achieve minimal risk for the distribution they induce and hence eliminate the need for retraining. However, it is a priori not clear that such stable points exist; and even if they do exist, whether we can find them efficiently. Furthermore, seeing as how performative optimality and stability are in general distinct solution concepts, under what conditions can we find models that approximately satisfy both? 

In this work, we begin to answer these questions by analyzing two different optimization strategies. The first is retraining, formally referred to as _repeated risk minimization_ (RRM), where the exact minimizer is repeatedly computed on the distribution induced by the previous model parameters. The second is _repeated gradient descent_ (RGD), in which the model parameters are incrementally updated using a single gradient descent step on the objective defined by the previous iterate. We introduce RGD as a computationally efficient approximation of RRM, which, as we show, adopts many favorable properties of RRM. 

Our algorithmic analysis of these methods reveals the existence of stable points under the assumption that the distribution map D(·) is sufficiently Lipschitz. We identify necessary and sufficient conditions for convergence to a performatively stable point and establish properties of the objective under which stable points and performative optima are close. 

We begin by analyzing the behavior of these procedures when they operate at a population level and then extend our analysis to finite samples. 

### 3.1 Assumptions 

It is easy to see that one cannot make any guarantees on the convergence of retraining or the existence of stable points without making some regularity assumptions on D(·). One reasonable way to quantify the regularity of D(·) is to assume Lipschitz continuity; the Lipschitz constant determines how sensitive the induced distribution is to a change in model parameters. Intuitively, such an assumption captures the idea that, if decisions are made according to similar predictive models, then the resulting distributions over instances should also be similar. We now introduce this key assumption of our work, which we call _ε-sensitivity_ . 

Definition 3.1 ( _ε_ -sensitivity). We say that a distribution map D(·) is _ε-sensitive_ if for all _θ,θ_<sup>′</sup> ∈ Θ: 



where _W_ 1 denotes the Wasserstein-1 distance, or earth mover’s distance. 

The earth mover’s distance is a natural notion of distance between probability distributions that provides access to a rich technical repertoire [38, 39]. Furthermore, we can verify that it is satisfied in various settings. 

Remark 3.2. _A simple example where this assumption is satisfied is for a Gaussian family. Given θ_ = ( _µ,σ_ 1 _,...,σp_ ) ∈ R<sup>2</sup><sup>_p_</sup> _, define_ D( _θ_ ) = N ( _ε_ 1 _µ,ε_ 2<sup>2</sup><sup>_diag_(</sup><sup>_σ_2</sup> 1<sup>_,...,σ_</sup> _p_<sup>2))</sup><sup>_whereε_</sup> 1<sup>_,ε_</sup> 2<sup>∈R</sup><sup>_.Then_D(·)</sup><sup>_is_</sup> _ε-sensitive for ε_ = max �| _ε_ 1| _,_ | _ε_ 2|� _._ 

7 

In addition to this assumption on the distribution map, we will often make standard assumptions on the loss function _ℓ_ ( _z_ ; _θ_ ) which hold for broad classes of losses. To simplify our presentation, let Z<sup>def</sup> = ∪ _θ_ ∈Θsupp(D( _θ_ )). 

- ( _joint smoothness_ ) We say that a loss function _ℓ_ ( _z_ ; _θ_ ) is _β_ -jointly smooth if the gradient ∇ _θℓ_ ( _z_ ; _θ_ ) is _β_ -Lipschitz in _θ and z_ , that is 



for all _θ,θ_<sup>′</sup> ∈ Θ and _z,z_<sup>′</sup> ∈Z. 

• ( _strong convexity_ ) We say that a loss function _ℓ_ ( _z_ ; _θ_ ) is _γ_ -strongly convex if 



for all _θ,θ_<sup>′</sup> ∈ Θ and _z_ ∈Z. If _γ_ = 0, this assumption is equivalent to convexity. 

We will sometimes refer to<sup>_<u>β</u>_</sup> _γ_<sup>, where</sup><sup>_β_is as in (A1) and</sup><sup>_γ_as in (A2), as the condition number.</sup> 

### 3.2 Repeated risk minimization 

We now formally define repeated risk minimization and prove one of our main results: sufficient and necessary conditions for retraining to converge to a performatively stable point. 

Definition 3.3 (RRM). _Repeated risk minimization_ (RRM) refers to the procedure where, starting from an initial model _fθ_ 0, we perform the following sequence of updates for every _t_ ⩾ 0: 



Using a toy example, we again argue that restrictions on the map D(·) are necessary to enable interesting analyses of RRM, otherwise it might be computationally infeasible to find performative optima, and performatively stable points might not even exist. 

Example 3.4. Consider optimizing the squared loss _ℓ_ ( _z_ ; _θ_ ) = ( _y_ − _θ_ )<sup>2</sup> , where _θ_ ∈ [0 _,_ 1] and the distribution of the outcome _Y_ , according to D( _θ_ ), is a point mass at 0 if _θ_ ⩾<sup><u>1</u></sup> 2<sup>, and a point mass</sup> at 1 if _θ <_<sup><u>1</u></sup> 2<sup>.Clearly there is no performatively stable point, and RRM will simply result in the</sup> alternating sequence 1 _,_ 0 _,_ 1 _,_ 0 _,..._ . The performative optimum in this case is _θ_ PO =<sup><u>1</u></sup> 2<sup>.</sup> 

To show convergence of retraining schemes, it is hence necessary to make a regularity assumption on D(·), such as _ε_ -sensitivity. We are now ready to state our main result regarding the convergence of repeated risk minimization. 

Theorem 3.5. _Suppose that the loss ℓ_ ( _z_ ; _θ_ ) _is β-jointly smooth_ (A1) _and γ-strongly convex_ (A2) _. If the distribution map_ D(·) _is ε-sensitive, then the following statements are true:_ 

- _(a)_ ∥ _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> )∥2 ⩽ _ε_<sup>_<u>β</u>_</sup> _γ_<sup>∥</sup><sup>_θ_−</sup><sup>_θ_′∥2</sup><sup>_,for all θ,θ_′ ∈Θ</sup><sup>_._</sup> 

- _(b) If ε <_<sup>_<u>γ</u>_</sup> _β_<sup>_, the iterates θtof RRM converge to a unique performatively stable point θ_PS</sup><sup>_at a linear_</sup> _rate:_ ∥ _θt_ − _θ_ PS∥2 ⩽ _δ for t_ ⩾ �1 − _ε γ_<sup>_<u>β</u>_</sup> �−1 log � <u>∥</u> _θ_ <u>0−</u> _δθ_ <u>PS∥2</u> � _._ 

8 

The main message of this theorem is that in performative prediction, if the loss function is sufficiently "nice" and the distribution map is sufficiently (in)sensitive, then one need only retrain a model a small number of times before it converges to a _unique_ stable point. The complete proof of Theorem 3.5 can be found in Appendix D.1. Here, we provide the main intuition through a proof sketch. 

_Proof Sketch._ Fix _θ,θ_<sup>′</sup> ∈ Θ. Let _f_ ( _ϕ_ ) = E _Z_ ∼D( _θ_ ) _ℓ_ ( _Z_ ; _ϕ_ ) and _f_<sup>′</sup> ( _ϕ_ ) = E _Z_ ∼D( _θ_ ′) _ℓ_ ( _Z_ ; _ϕ_ ). By applying standard properties of strong convexity and the fact that _G_ ( _θ_ ) is the unique minimizer of _f_ ( _ϕ_ ), we can derive that 



Next, we observe that ( _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> ))<sup>⊤</sup> ∇ _θℓ_ ( _z_ ; _G_ ( _θ_<sup>′</sup> )) is ∥ _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> )∥2 _β_ -Lipschitz in _z_ . This follows from applying the Cauchy-Schwarz inequality and the fact that the loss is _β_ -jointly smooth. Using the dual formulation of the earth mover’s distance (Lemma C.3) and _ε_ -sensitivity of D(·), as well as the first-order conditions of optimality for convex functions, a short calculation reveals that 



Claim (a) then follows by combining the previous two inequalities and rearranging. Intuitively, strong convexity forces the iterates to contract after retraining, yet this contraction is offset by the distribution shift induced by changing the underlying model parameters. Joint smoothness and _ε_ -sensitivity ensure that this shift is not too large. Part (b) is essentially a consequence of applying the Banach fixed-point theorem to the result of part (a). ■ 

One intriguing insight from our analysis is that this convergence result is in fact tight; removing any single assumption required for convergence by Theorem 3.5 is enough to construct a counterexample for which RRM diverges. 

Proposition 3.6. _Suppose that the distribution map_ D(·) _is ε-sensitive with ε >_ 0 _. RRM can fail to converge at all in any of the following cases, for any choice of parameters β,γ >_ 0 _:_ 

- _(a) The loss is β-jointly smooth and convex, but not strongly convex._ 

- _(b) The loss is γ-strongly convex, but not jointly smooth._ 

- _(c) The loss is β-jointly smooth and γ-strongly convex, but ε_ ⩾<sup>_<u>γ</u>_</sup> _β_<sup>_._</sup> 

We include a counterexample for statement (a), and defer the proofs of (b) and (c) to Appendix D.2. 

_Proof of Proposition 3.6(a):_ Consider the linear loss defined as _ℓ_ (( _x,y_ ); _θ_ ) = _βyθ_ , for _θ_ ∈ [−1 _,_ 1]. Note that this objective is _β_ -jointly smooth and convex, but not strongly convex. Let the distribution of _Y_ according to D( _θ_ ) be a point mass at _εθ_ , and let the distribution of _X_ be invariant with respect to _θ_ . Clearly, this distribution is _ε_ -sensitive. 

Here, the decoupled performative risk has the following form DPR( _θ,ϕ_ ) = _εβθϕ_ . The unique performatively stable point is 0. However, if we initialize RRM at any point other than 0, the procedure generates the sequence of iterates _...,_ 1 _,_ −1 _,_ 1 _,_ −1 _..._ , thus failing to converge. Furthermore, this behavior holds for all _ε,β >_ 0. ■ 

9 

Proposition 3.6 suggests a fundamental difference between strong and weak convexity in our framing of performative prediction (weak meaning _γ_ = 0). In supervised learning, using strongly convex losses generally guarantees a faster rate of optimization, yet asymptotically, the solution achieved with either strongly or weakly convex losses is globally optimal. However, in our framework, strong convexity is in fact _necessary_ to guarantee convergence of repeated risk minimization, even for arbitrarily smooth losses and an arbitrarily small sensitivity parameter. 

### 3.3 Repeated gradient descent 

Theorem 3.5 demonstrates that repeated risk minimization converges to a unique performatively stable point if the sensitivity parameter _ε_ is small enough. However, implementing RRM requires access to an exact optimization oracle. We now relax this requirement and demonstrate how a simple gradient descent algorithm also converges to a unique stable point. 

Definition 3.7 (RGD). _Repeated gradient descent_ (RGD) is the procedure where, starting from an initial model _fθ_ 0, we perform the following sequence of updates for every _t_ ⩾ 0: 



where _η >_ 0 is a fixed step size and ΠΘ denotes the Euclidean projection operator onto Θ. 

Note that repeated gradient descent only requires the loss _ℓ_ to be differentiable with respect to _θ_ . It does not require taking gradients of the performative risk. Like RRM, we can show that RGD is a contractive mapping for small enough sensitivity parameter _ε_ . 

Theorem 3.8. _Suppose that the loss ℓ_ ( _z_ ; _θ_ ) _is β-jointly smooth_ (A1) _and γ-strongly convex_ (A2) _. If the distribution map_ D(·) _is ε-sensitive with ε <_ _<u>γ</u>_ <u>2</u> ( _β_ + _γ_ )(1+1 _._ 5 _ηβ_ )<sup>_, then RGD with step size η_⩽</sup> _β_ + _γ satisfies the following:_ 



The conclusion of Theorem 3.8 is a strict generalization of a classical optimization result which considers a static objective, in which case the rate of contraction is �1 − _η β_<sup>_<u>βγ</u>_</sup> + _γ_ � (see for example Theorem 2.1.15 in [34] or Lemma 3.7 in [16]). Our rate exactly matches this classical result in the case that _ε_ = 0. The proof of Theorem 3.8 can be found in Appendix D.3. 

### 3.4 Finite-sample analysis 

We now extend our main results regarding the convergence of RRM and RGD to the finitesample regime. To do so, we leverage the fact that, under mild regularity conditions, the empirical distribution D<sup>_n_</sup> given by _n_ samples drawn i.i.d. from a true distribution D is with high probability close to D in earth mover’s distance [13]. 

We begin by defining the finite-sample version of these procedures. 

10 

Definition 3.9 (RERM & REGD). Define _repeated empirical risk minimization_ (RERM) to be the procedure where starting from a model _fθ_ 0 at every iteration _t_ ⩾ 0, we collect _nt_ samples from D( _θt_ ) and perform the update: 



Similarly, define _repeated empirical gradient descent_ (REGD) to be the optimization procedure with update rule: 



Here, _η >_ 0 is a step size and ΠΘ denotes the Euclidean projection operator onto Θ. 

The following theorem illustrates that with enough samples collected at every iteration, with high probability both algorithms converge to a small neighborhood around a stable point. Recall that _m_ is the dimension of data samples _z_ . 

Theorem 3.10. _Suppose that the loss ℓ_ ( _z_ ; _θ_ ) _is β-jointly smooth_ (A1) _and γ-strongly convex_ (A2) _,_ def = _and that there exist α >_ 1 _,µ >_ 0 _such that ξα,µ_ �R<sup>_m eµ_|</sup><sup>_x_|</sup><sup>_αd_D(</sup><sup>_θ_)</sup><sup>_is finite_∀</sup><sup>_θ_∈Θ</sup><sup>_.Let δ_∈(0</sup><sup>_,_1)</sup><sup>_be a_</sup> _radius of convergence. Consider running RERM or RGD with nt_ = _O_ <u>1</u> _samples at time t._ � ( _εδ_ )<sup>_m_log</sup> � _pt_ �� _(a) If_ D(·) _is ε-sensitive with ε <_ 2<sup>_<u>γ</u>_</sup> _β_<sup>_, then with probability_1 −</sup><sup>_p, RERM satisfies,_</sup> 



_(b) If_ D(·) _is ε-sensitive with ε <_ ( _β_ + _γ_ )(1+1 _<u>γ</u> ._ 5 _ηβ_ )<sup>_, then with probability_1 −</sup><sup>_p, REGD with satisfies,_</sup> 





_for a constant choice of step size η_ ⩽ _β_ +2 _γ_<sup>_._</sup> 

_Proof sketch._ The basic idea behind these results is the following. While ∥ _θt_ − _θ_ PS∥2 _> δ_ , the sample size _nt_ is sufficiently large to ensure a behavior similar to that on a population level: as in Theorems 3.5 and 3.8, the iterates _θt_ contract toward _θ_ PS. This implies that _θt_ eventually enters a _δ_ -ball around _θ_ PS, for some large enough _t_ . Once this happens, contrary to populationlevel results, a contraction is no longer guaranteed due to the noise inherent in observing only finite-sample approximations of D( _θt_ ). Nevertheless, the sample size _nt_ is sufficiently large to ensure that _θt_ cannot escape a _δ_ -ball around _θ_ PS either. ■ 

## 4 Relating performative optimality and stability 

As we discussed previously, while performative optima are always guaranteed to exist,<sup>1</sup> it is not clear whether performatively stable points exist in all settings. Our algorithmic analysis 

> 1In particular, they are guaranteed to exist over the extended real line, i.e. we allow _θ_ ∈ (R ∪{±∞}) _d_ . 

11 

of repeated risk minimization and repeated gradient descent revealed the existence of unique stable points under the assumption that the objective is strongly convex and smooth. The first result of this section illustrates existence of stable points under weaker assumptions on the loss, in the case where the solution space Θ is constrained. All proofs can be found in Appendix D. 

Proposition 4.1. _Let the distribution map_ D(·) _be ε-sensitive and_ Θ ⊂ R<sup>_d_</sup> _be compact. If the loss ℓ_ ( _z_ ; _θ_ ) _is convex and jointly continuous in_ ( _z,θ_ ) _, then there exists a performatively stable point._ 

A natural question to consider at this point is whether there are procedures analogous to RRM and RGD for efficiently computing performative optima. 

Our analysis suggests that directly minimizing the performative risk is in general a more challenging problem than finding performatively stable points. In particular, we can construct simple examples where the performative risk PR( _θ_ ) is non-convex, despite strong regularity assumptions on the loss and the distribution map. Proposition 4.2. _The performative risk_ PR( _θ_ ) _can be concave in θ, even if the loss ℓ_ ( _z_ ; _θ_ ) _is β-jointly smooth_ (A1) _, γ-strongly convex_ (A2) _, and the distribution map_ D(·) _is ε-sensitive with ε <_<sup>_<u>γ</u>_</sup> _β_<sup>_._</sup> 

However, what we can show is that there are cases where finding performatively stable points is sufficient to guarantee that the resulting model has low performative risk. In particular, our next result demonstrates that if the loss function _ℓ_ ( _z_ ; _θ_ ) is Lipschitz in _z_ and _γ_ -strongly convex, then all performatively stable points and performative optima lie in a small neighborhood around each other. Moreover, the theorem holds for cases where performative optima and performatively stable points are not necessarily unique. 

Theorem 4.3. _Suppose that the loss ℓ_ ( _z_ ; _θ_ ) _is Lz-Lipschitz in z, γ-strongly convex_ (A2) _, and that the distribution map_ D(·) _is ε-sensitive. Then, for every performatively stable point θ_ PS _and every performative optimum θ_ PO _:_ 



This result shows that in cases where repeated risk minimization converges to a stable point, the resulting model approximately minimizes the performative risk. 

Moreover, Theorem 4.3 suggests a way of converging close to performative optima _in objective value_ even if the loss function is smooth and convex, but not strongly convex. In particular, by adding quadratic regularization to the objective, we can ensure that RRM or RGD converge to a stable point that approximately minimizes the performative risk, see Appendix E. 

## 5 A case study in strategic classification 

Having presented our model for performative prediction, we now proceed to illustrate how these ideas can be applied within the context of strategic classification and discuss some of the implications of our theorems for this setting. 

We begin by formally establishing how strategic classification can be cast as a performative prediction problem and illustrate how our framework can be used to derive results regarding the convergence of popular retraining heuristics in strategic classification settings. Afterwards, we further develop the connections between both fields by empirically evaluating the behavior of repeated risk minimization on a dynamic credit scoring task. 

12 

Input: base distribution D, classifier _fθ_ , cost function _c_ , and utility function _u_ Sampling procedure for D( _θ_ ): 

1. Sample ( _x,y_ ) ∼D 

2. Compute best response _x_ BR ← argmax _x_ ′ _u_ ( _x_<sup>′</sup> _,θ_ ) − _c_ ( _x_<sup>′</sup> _,x_ ) 

3. Output sample ( _x_ BR _, y_ ) 

Figure 1: Distribution map for strategic classification. 

### 5.1 Stackelberg equilibria are performative optima 

Strategic classification is a two-player game between an institution which deploys a classifier and agents who selectively adapt their features in order to improve their outcomes. 

A classic example of this setting is that of a bank which uses a machine learning classifier to predict whether or not a loan applicant is creditworthy. Individual applicants react to the bank’s classifier by manipulating their features with the hopes of inducing a favorable classification. This game is said to have a _Stackelberg_ structure since agents adapt their features only after the bank has deployed their classifier. 

The optimal strategy for the institution in a strategic classification setting is to deploy the solution corresponding to the _Stackelberg equilibrium_ , defined as the classifier _fθ_ which achieves minimal loss over the induced distribution D( _θ_ ) in which agents have strategically adapted their features in response to _fθ_ . In fact, we see that this equilibrium notion exactly matches our definition of performative optimality: 



We think of D as a "baseline" distribution over feature-outcome pairs before any classifier deployment, and D( _θ_ ) denotes the distribution over features and outcomes obtained by strategically manipulating D. As described in existing work [8, 15, 33], the distribution function D( _θ_ ) in strategic classification corresponds to the data-generating process outlined in Figure 1. 

Here, _u_ and _c_ are problem-specific functions which determine the best response for agents in the game. Together with the base distribution D, these define the relevant distribution map D(·) for the problem of strategic classification. 

A strategy that is commonly adapted in practice as a means of coping with the distribution shift that arises in strategic classification is to repeatedly retrain classifiers on the induced distributions. This procedure corresponds to the repeated risk minimization procedure introduced in Definition 3.3. Our results describe the first set of sufficient conditions under which repeated retraining overcomes strategic effects. 

Corollary 5.1. _Let the institution’s loss ℓ_ ( _z_ ; _θ_ ) _be Lz- and Lθ-Lipschitz in z and θ respectively, β- jointly smooth_ (A1) _, and γ-strongly convex_ (A2) _. If the induced distribution map is ε-sensitive, with ε <_<sup>_<u>γ</u>_</sup> _β_<sup>_,thenRRMconvergesatalinearratetoaperformativelystableclassifierθ_PS</sup><sup>_thatis_</sup> 2 _Lzε_ ( _Lθ_ + _Lzε_ ) _γ_<sup>−1</sup> _close in objective value to the Stackelberg equilibrium._ 

### 5.2 Simulations 

We next examine the convergence of repeated risk minimization and repeated gradient descent in a simulated strategic classification setting. We run experiments on a dynamic credit scoring 

13 



<!-- Start of picture text -->
Repeated Risk Minimization Repeated Gradient Descent<br>-2<br>-2 10<br>10<br>ε = 0.01 ε = 0.01<br>-7 ε = 1 10-7 ε = 1<br>10 ε = 100 ε = 100<br>10-12 ε = 1000 10-12 ε = 1000<br>0 20 40 60 0 1000 2000 3000<br>Iteration t Iteration t<br> · ∥∥θθc + 12 −t<br><!-- End of picture text -->

Figure 2: Convergence in domain of RRM (left) and RGD (right) for varying _ε_ -sensitivity parameters. We add a marker if at the next iteration the distance between iterates is numerically zero. We normalize the distance by _c_ = ∥ _θ_ 0 _,S_ ∥<sup>−</sup> 2<sup>1.</sup> 

simulator in which an institution classifies the creditworthiness of loan applicants.<sup>2</sup> As motivated previously, agents react to the institution’s classifier by manipulating their features to increase the likelihood that they receive a favorable classification. 

To run our simulations, we construct a distribution map D( _θ_ ), as described in Figure 1. For the base distribution D, we use a class-balanced subset of a Kaggle credit scoring dataset [22]. Features _x_ ∈ R<sup>_m_−1</sup> correspond to historical information about an individual, such as their monthly income and number of credit lines. Outcomes _y_ ∈{0 _,_ 1} are binary variables which are equal to 1 if the individual defaulted on a loan and 0 otherwise. The institution makes predictions using a logistic regression classifier. We assume that individuals have linear utilities _u_ ( _θ,x_ ) = −⟨ _θ,x_ ⟩ and quadratic costs _c_ ( _x_<sup>′</sup> _,x_ ) = 2<sup><u>1</u></sup> _ε_<sup>∥</sup><sup>_x_′ −</sup><sup>_x_∥</sup> 2<sup>2, where</sup> _ε_ is a positive constant that regulates the cost incurred by changing features. Linear utilities indicate that agents wish to minimize their assigned probability of default. 

We divide the set of features into strategic features _S_ ⊆ [ _m_ − 1], such as the number of open credit lines, and non-strategic features (e.g., age). Solving the optimization problem described in Figure 1, the best response for an individual corresponds to the following update, 



where _xS,xS_<sup>′</sup><sup>_,θS_∈R|</sup><sup>_S_|.As per convention in the literature [8, 15, 33], individual outcomes</sup><sup>_y_are</sup> unaffected by strategic manipulation. 

Intuitively, this data-generating process is _ε_ -sensitive since for a given choice of classifiers, _fθ_ and _fθ_ ′ , an individual feature vector is shifted to _xS_ − _εθS_ and to _xS_ − _εθS_<sup>′, respectively.The</sup> distance between these two shifted points is equal to _ε_ ∥ _θS_ − _θS_<sup>′∥2.Since the optimal transport</sup> distance is bounded by _ε_ ∥ _θ_ − _θ_<sup>′</sup> ∥2 for every individual point, it is also bounded by this quantity over the entire distribution. A full proof of this claim is presented in Appendix B.2. 

For our experiments, instead of sampling from D( _θ_ ), we treat the points in the original dataset as the true distribution. Hence, we can think of all the following procedures as operating at the population level. Furthermore, we add a regularization term to the logistic loss to ensure that the objective is strongly convex. 

> 2Code is available at https://github.com/zykls/performative-prediction, and the simulator has been integrated into the WhyNot software package [31]. 

14 



<!-- Start of picture text -->
Performative Risk Accuracy<br>70.5%<br>0.620<br>70.0%<br>0.615<br>69.5%<br>0.610<br>0 10 20 30 0 10 20 30<br>Iteration Iteration<br><!-- End of picture text -->

Figure 3: Performative risk (left) and accuracy (right) of the classifier _θt_ at different stages of RRM for _ε_ = 80. Blue lines indicates the optimization phase and green lines indicate the effect of the distribution shift after the classifier deployment. 

Repeated risk minimization. The first experiment we consider is the convergence of RRM. From our theoretical analysis, we know that RRM is guaranteed to converge at a linear rate to a performatively stable point if the sensitivity parameter _ε_ is smaller than<sup>_<u>γ</u>_</sup> _β_<sup>.In Figure 2 (left),</sup> we see that RRM does indeed converge in only a few iterations for small values of _ε_ while it divergences if _ε_ is too large. 

The evolution of the performative risk during the RRM optimization is illustrated in Figure 3. We evaluate PR( _θ_ ) at the beginning and at the end of each optimization round and indicate the effect due to distribution shift with a dashed green line. We also verify that the surrogate loss is a good proxy for classification accuracy in the performative setting. 

Repeated gradient descent. In the case of RGD, we find similar behavior to that of RRM. While the iterates again converge linearly, they naturally do so at a slower rate than in the exact minimization setting, given that each iteration consists only of a single gradient step. Again, we can see in Figure 2 that the iterates converge for small values of _ε_ and diverge for large values. 

## 6 Discussion and Future Work 

Our work draws attention to the fundamental problem of performativity in statistical learning and decision-making. Performative prediction enjoys a clean formal setup that we introduced, drawing on elements from causality and game theory. 

Retraining is often considered a nuisance intended to cope with distribution shift. In contrast, our work interprets retraining as the natural equilibrating dynamic for performative prediction. The fixed points of retraining are performative stable points. Moreover, retraining converges to such stable points under natural assumptions, including strong convexity of the loss function. It is interesting to note that (weak) convexity alone is not enough. Performativity thus gives another intriguing perspective on why strong convexity is desirable in supervised learning. 

Several interesting questions remain. For example, by letting the step size of repeated gradient descent tend to 0, we see that this procedure converges for _ε < β_ + _<u>γγ</u>_<sup>.Exact repeated</sup> risk minimization, on the other hand, provably converges for every _ε <_<sup>_<u>γ</u>_</sup> _β_<sup>, and we showed this</sup> inequality is tight. It would be interesting to understand whether this gap is a fundamental difference between both procedures or an artifact of our analysis. 

15 

Lastly, we believe that the tools and ideas from performative prediction can be used to make progress in other subareas of machine learning. For example, in this paper, we have illustrated how reframing strategic classification as a performative prediction problem leads to a new understanding of when retraining overcomes strategic effects. However, we view this example as only scratching the surface of work connecting performative prediction with other fields. 

In particular, reinforcement learning can be thought of as a case of performative prediction. In this setting, the choice of policy _fθ_ , affects the distribution D( _θ_ ) over _z_ = {( _sh,ah_ )}<sup>∞</sup> _h_ =1<sup>, the set</sup> of visited states, _s_ , and actions, _a_ , in a Markov Decision Process. Building off this connection, we can reinterpret repeated risk minimization as a form of off-policy learning in which an agent first collects a batch of data under a particular policy _fθ_ , and then finds the optimal policy for that trajectory offline. We believe that some of the ideas developed in the context of performative prediction can shed new light on when these off-policy methods can converge. 

## Acknowledgements 

We wish to acknowledge support from the U.S. National Science Foundation Graduate Research Fellowship Program and the Swiss National Science Foundation Early Postdoc Mobility Fellowship Program. 

## References 

- [1] C.D. Aliprantis and K.C. Border. _Infinite Dimensional Analysis: A Hitchhiker’s Guide_ . Springer Berlin Heidelberg, 2006. 

- [2] Peter L. Bartlett. Learning with a Slowly Changing Distribution. In _Proceedings of the Fifth Annual ACM Conference on Computational Learning Theory (COLT)_ , pages 243–252, 1992. 

- [3] Peter L. Bartlett, Shai Ben-David, and Sanjeev R. Kulkarni. Learning Changing Concepts by Exploiting the Structure of Change. _Machine Learning_ , 41(2):153–174, 2000. 

- [4] Yahav Bechavod, Katrina Ligett, Zhiwei Steven Wu, and Juba Ziani. Causal Feature Discovery through Strategic Modification. _arXiv preprint arXiv:2002.07024_ , 2020. 

- [5] Claude Berge. _Topological Spaces_ . Courier Corporation, 1997. 

- [6] Richard J Bolton and David J Hand. Statistical Fraud Detection: A Review. _Statistical Science_ , pages 235–249, 2002. 

- [7] Léon Bottou, Jonas Peters, Joaquin Quiñonero-Candela, Denis X Charles, D Max Chickering, Elon Portugaly, Dipankar Ray, Patrice Simard, and Ed Snelson. Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising. _The Journal of Machine Learning Research_ , 14(1):3207–3260, 2013. 

- [8] Michael Brückner, Christian Kanzow, and Tobias Scheffer. Static Prediction Games for Adversarial Learning Problems. _Journal of Machine Learning Research_ , 13(Sep):2617–2654, 2012. 

- [9] Sébastien Bubeck. Convex Optimization: Algorithms and Complexity. _Foundations and Trends® in Machine Learning_ , 8(3-4):231–357, 2015. 

16 

- [10] Jenna Burrell, Zoe Kahn, Anne Jonas, and Daniel Griffin. When Users Control the Algorithms: Values Expressed in Practices on Twitter. _Proceedings of the ACM on HumanComputer Interaction_ , 3:19, 2019. 

- [11] Nilesh Dalvi, Pedro Domingos, Sumit Sanghai, and Deepak Verma. Adversarial Classification. In _Proceedings of the_ 10 _th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 99–108, 2004. 

- [12] Danielle Ensign, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger, and Suresh Venkatasubramanian. Runaway Feedback Loops in Predictive Policing. In _Proceedings of the 1st ACM Conference on Fairness, Accountability and Transparency_ , pages 160–171, 2018. 

- [13] Nicolas Fournier and Arnaud Guillin. On the Rate of Convergence in Wasserstein Distance of the Empirical Measure. _Probability Theory and Related Fields_ , 162(3):707–738, 2015. 

- [14] João Gama, Indre Žliobait˙ e, Albert Bifet, Mykola Pechenizkiy, and Abdelhamid Bouchachia.˙ A Survey on Concept Drift Adaptation. _ACM Computing Surveys (CSUR)_ , 46(4):1–37, 2014. 

- [15] Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic Classification. In _Proceedings of the ACM Conference on Innovations in Theoretical Computer Science_ , pages 111–122, 2016. 

- [16] Moritz Hardt, Ben Recht, and Yoram Singer. Train Faster, Generalize Better: Stability of Stochastic Gradient Descent. In _Proceedings of the 33rd International Conference on Machine Learning (ICML)_ , pages 1225–1234, 2016. 

- [17] Tatsunori Hashimoto, Megha Srivastava, Hongseok Namkoong, and Percy Liang. Fairness Without Demographics in Repeated Loss Minimization. In _Proceedings of the 35th International Conference on Machine Learning (ICML)_ , pages 1929–1938, 2018. 

- [18] Kieran Healy. The Performativity of Networks. _European Journal of Sociology/Archives Européennes de Sociologie_ , 56(2):175–205, 2015. 

- [19] Lily Hu and Yiling Chen. A Short-term Intervention for Long-term Fairness in the Labor Market. In _Proceedings of the World Wide Web Conference_ , pages 1389–1398, 2018. 

- [20] Lily Hu, Nicole Immorlica, and Jennifer Wortman Vaughan. The Disparate Effects of Strategic Manipulation. In _Proceedings of the 2nd ACM Conference on Fairness, Accountability, and Transparency_ , pages 259–268, 2019. 

- [21] Guido W Imbens and Donald B Rubin. _Causal Inference in Statistics, Social, and Biomedical sciences_ . Cambridge University Press, 2015. 

- [22] Kaggle. Give me some credit. `https://www.kaggle.com/c/GiveMeSomeCredit/data` , 2012. 

- [23] Shizuo Kakutani. A Generalization of Brouwer’s Fixed Point Theorem. _Duke Mathematical Journal_ , 8(3):457–459, 1941. 

- [24] Moein Khajehnejad, Behzad Tabibian, Bernhard Schölkopf, Adish Singla, and Manuel Gomez-Rodriguez. Optimal Decision Making Under Strategic Behavior. _arXiv preprint arXiv:1905.09239_ , 2019. 

17 

- [25] Jon Kleinberg and Manish Raghavan. How Do Classifiers Induce Agents to Invest Effort Strategically? In _Proceedings of the ACM Conference on Economics and Computation (EC)_ , pages 825–844, 2019. 

- [26] Amanda Kube, Sanmay Das, and Patrick J Fowler. Allocating Interventions Based on Predicted Outcomes: A Case Study on Homelessness Services. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 33, pages 622–629, 2019. 

- [27] Anthony Kuh, Thomas Petsche, and Ronald L Rivest. Learning Time-Varying Concepts. In _Advances in Neural Information Processing Systems (NIPS)_ , pages 183–189, 1991. 

- [28] Lydia T Liu, Sarah Dean, Esther Rolf, Max Simchowitz, and Moritz Hardt. Delayed Impact of Fair Machine Learning. In _Proceedings of the 35th International Conference on Machine Learning (ICML)_ , pages 3150–3158, 2018. 

- [29] Kristian Lum and William Isaac. To Predict and Serve? _Significance_ , 13(5):14–19, 2016. 

- [30] Donald A MacKenzie, Fabian Muniesa, and Lucia Siu. _Do Economists Make Markets?: On the Performativity of Economics_ . Princeton University Press, 2007. 

- [31] John Miller, Chloe Hsu, Jordan Troutman, Juan Perdomo, Tijana Zrnic, Lydia Liu, Yu Sun, Ludwig Schmidt, and Moritz Hardt. Whynot, 2020. 

- [32] John Miller, Smitha Milli, and Moritz Hardt. Strategic Classification is Causal Modeling in Disguise. _arXiv preprint arXiv:1910.10362_ , 2019. 

- [33] Smitha Milli, John Miller, Anca D Dragan, and Moritz Hardt. The Social Cost of Strategic Classification. In _Proceedings of the 2nd ACM Conference on Fairness, Accountability, and Transparency_ , pages 230–239, 2019. 

- [34] Yurii Nesterov. _Introductory Lectures on Convex Optimization: A Basic Course_ , volume 87. Springer Science & Business Media, 2013. 

- [35] Judea Pearl. _Causality_ . Cambridge University Press, 2009. 

- [36] Shai Shalev-Shwartz and Shai Ben-David. _Understanding Machine Learning: From Theory to Algorithms_ . Cambridge University Press, 2014. 

- [37] Yonadav Shavit, Benjamin Edelman, and Brian Axelrod. Learning From Strategic Agents: Accuracy, Improvement, and Causality. _arXiv preprint arXiv:2002.10066_ , 2020. 

- [38] Cédric Villani. _Topics in optimal transportation_ . Number 58. American Mathematical Society, 2003. 

- [39] Cédric Villani. _Optimal Transport: Old and New_ , volume 338. Springer Science & Business Media, 2008. 

- [40] Geoffrey I. Webb, Roy Hyde, Hong Cao, Hai Long Nguyen, and Francois Petitjean. Characterizing Concept Drift. _Data Mining and Knowledge Discovery_ , 30(4):964–994, 2016. 

- [41] Indre˙ Žliobaite.˙ Learning under Concept Drift: An Overview. _arXiv preprint arXiv:1010.4784_ , 2010. 

18 

- [42] Indre˙ Žliobaite,˙ Mykola Pechenizkiy, and Joao Gama. An Overview of Concept Drift Applications. In _Big Data Analysis: New Algorithms for a New Society_ , pages 91–114. Springer, 2016. 

19 

## A Applications of performativity 

To illustrate the fact that performativity is a common cause for concept drift, we review a table of concepts drift applications from [42]. In Table 1, we highlight those settings that naturally occur due to performativity. Below we briefly discuss the role of performativity in such applications. 

|Indust.<br>Appl.|Monitoring & control|Information management|Analytics & diagnostics|
|---|---|---|---|
|Security,<br>Police|fraud detection,<br>insider trading detection,<br>adversaryactions detection|next crime place<br>prediction|crime volume<br>prediction|
|Finance,<br>Banking,<br>Telecom,<br>Insurance,<br>Marketing,<br>Retail,<br>Advertising|monitoring & management<br>of customer segments,<br>bankruptcy prediction|product or service<br>recommendation,<br>including complimentary,<br>user intent or information<br>need prediction|demand prediction,<br>response rate<br>prediction, budget<br>planning|
|Production<br>industry|controlling output quality|-|predict bottlenecks|
|Education<br>(e-Learning,<br>e-Health),<br>Media,<br>Entertainment|gaming the system,<br>drop out prediction|music, VOD, movie,<br>news, learning object<br>personalized search<br>& recommendations|player-centered game<br>design, learner-centered<br>education|



Table 1: Table of concept drift applications from Žliobait˙e et al. [42] 

The role of _fraud detection_ systems is to predict whether an instance such as a transaction or email is legitimate or not. It is well-known that designers of such fraudulent instances adapt to the fraud detection system in place in order to breach security [6]. Therefore, the deployment of fraud detection systems shapes the features of fraudulent instances. 

_Crime place prediction_ , sometimes referred to as predictive policing [12, 26, 29], uses historical data to estimate the likelihood of crime at a given location. Those locations where criminal behavior is deemed likely by the system typically get more police patrols and better surveillance which act on the one hand to deter crime. These actions resulting from prediction significantly decrease the probability of crime taking place, thus changing the data used for future predictions. 

In _personalized recommendations_ , instances are recommended to a user based on their historical context, such as their ratings or purchases. The set of recommendations thus depends on the trained machine learning model, which in turn changes the user’s future ratings or purchases [7]. In other words, user features serving as input to a recommender inevitably depend on the previously used recommendation mechanisms. 

In _online two-player games_ , it is common to request an AI opponent. The level of sophistication of the AI opponent might be chosen depending on the user’s success history in the given game, with the goal of making the game appropriately challenging. This choice of AI opponent changes players’ future success profiles, again causing a distribution shift in the features serving as an input to the prediction system. 

_Gaming the system_ falls under the umbrella of strategic classification, which we discuss in detail in Section 5, so we avoid further discussion in this section. 

20 

## B Experiments 

### B.1 Visualizing the performative risk and trajectory of RRM 



<!-- Start of picture text -->
supervised learning classifier<br>performative optimum<br>stable point<br>RRM trajectory<br>(a) ε  = 25<br>supervised learning classifier<br>performative optimum<br>RRM trajectory<br>(b) ε  = 100<br>Feature 1<br>Feature 1<br>Feature 2<br>Feature 2<br>Performative Risk<br>Performative Risk<br><!-- End of picture text -->

Figure 4: Performative risk surface and trajectory of repeated risk minimization for two different values of sensitivity parameter _ε_ . The initial iterate is the risk minimizer on the base dataset (•). We mark the performative optimum ( _⋆_ ) and performatively stable point (×). 

We provide additional experimental results in which we visualize the trajectory of repeated risk minimization on the surface of the performative risk. We adopt the general setting of Section 5. However, to properly visualize the loss, we rerun the experiments on a reduced version of the dataset with only two features (i.e _x_ ∈ R<sup>2</sup> ), both of which are adapted strategically according to the update described in Section 5. 

Figure 4 plots the performative risk surface, together with the trajectory of RRM given by straight black lines. The top plot shows the trajectory for a suitably small sensitivity parameter 

21 

_ε_ . We see that RRM converges to a stable point which is close to the performative optimum. We contrast this behavior with that of RRM when _ε_ is large in the bottom plot. Here, we observe that the iterates oscillate and that the algorithm fails to converge. Both plots mark the risk minimizer on the initial data set (•), before any strategic adaptation takes place. This point also corresponds to the initial iterate of RRM _θ_ 0. We additionally mark the performative optimum ( _⋆_ ) on the risk curve. The top plot additionally marks the last iterate of RRM, which serves as a proxy for the performatively stable point (×). As predicted by our theory, this stable point is in a small neighborhood around the performative optimum. 

### B.2 Experimental details 

Base distribution. The base distribution consists of the Kaggle data set [22]. We subsample _n_ = 18 _,_ 357 points from the original training set such that both classes are approximately balanced (45% of points have _y_ equal to 1). There are a total of 10 features, 3 of which we treat as strategic features: utilization of credit lines, number of open credit lines, and number of real estate loans. We scale features in the base distribution so that they have zero mean and unit variance. 

Verifying _ε_ -sensitivity. We verify that the map D(·), as described in Section 5, is _ε_ -sensitive. To do so, we analyze _W_ 1(D( _θ_ ) _,_ D( _θ_<sup>′</sup> )), for arbitrary _θ,θ_<sup>′</sup> ∈ Θ. Fix a sample point _x_ ∈ R<sup>_m_−1</sup> from the base dataset. Because the base distribution D is supported on _n_ points, we can upper bound the optimal transport distance between any pair of distributions D( _θ_ ) and D( _θ_<sup>′</sup> ) by the Euclidean distance between the shifted versions of _x_ in D( _θ_ ) and D( _θ_<sup>′</sup> ). In our construction, the point _x_ is shifted to _x_ − _εθ_ and to _x_ − _εθ_<sup>′</sup> in D( _θ_ ) and D( _θ_<sup>′</sup> ) respectively. The distance between these two shifted points is ∥ _x_ − _εθ_ − _x_ + _εθ_<sup>′</sup> ∥2 = _ε_ ∥ _θ_ − _θ_<sup>′</sup> ∥2. Since the same relationship holds for all other samples _x_ in the base dataset, the optimal transport from D( _θ_ ) to D( _θ_<sup>′</sup> ) is at most _ε_ ∥ _θ_ − _θ_<sup>′</sup> ∥2. 

Verifying joint smoothness of the objective. For the experiments described in Figure 2, we run repeated risk minimization and repeated gradient descent on the logistic loss with _ℓ_ 2 regularization: 



For both the repeated risk minimization and repeated gradient descent we set _γ_ = 1000 _/n_ , where _n_ is the size of the base dataset. 

For a particular feature-outcome pair ( _xi,yi_ ), the logistic loss is<sup><u>1</u></sup> 4<sup>∥</sup><sup>_xi_∥</sup> 2<sup>2smooth [36].Therefore,</sup> the entire objective is 4<sup><u>1</u></sup> _n_ � _ni_ =1<sup>∥</sup><sup>_xi_∥2</sup> 2<sup>+</sup><sup>_γ_smooth.Due to the strategic updates,</sup><sup>_xBR_=</sup><sup>_x_−</sup><sup>_εθ_, the</sup> norm of individual features change depending on the choice of model parameters. Theoretically, we can upper bound the smoothness of the objective by finding the implicit constraints on Θ, which can be revealed by looking at the dual of the objective function for every fixed value of _ε_ . However, for simplicity, we simply calculate the worst-case smoothness of the objective, given the trajectory of iterates { _θt_ }, for every fixed _ε_ . 

Furthermore, we can verify the logistic loss is jointly smooth. For a fixed example _z_ = ( _x,y_ ), the gradient of the regularized logistic loss with respect to _θ_ is, 

22 



which is 2-Lipschitz in _z_ due to _y_ ∈{0 _,_ 1}. Hence, the overall objective is _β_ -jointly smooth with parameter 



For RRM, _ε_ is less than<sup>_<u>γ</u>_</sup> _β_<sup>only in the case that</sup><sup>_ε_= 0</sup><sup>_._01.For RGD,</sup><sup>_ε_is never smaller than the</sup> theoretical cutoff of _<u>γ</u>_ ( _β_ + _γ_ )(1+1 _._ 5 _ηβ_ )<sup>.</sup> 

Optimization details. The definition of RRM requires exact minimization of the objective at every iteration. We approximate this requirement by minimizing the objective described in expression (1) to small tolerance, 10<sup>−8</sup> , using gradient descent. We choose the step size at every iteration using backtracking line search. 

In the case of repeated gradient descent, we run the procedure as described in Definition 3.7 with a fixed step size of _η_ = _β_ +2 _γ_<sup>.</sup> 

## C Auxiliary lemmas 

Lemma C.1 (First-order optimality condition). _Let f be convex and let_ Ω _be a closed convex set on which f is differentiable, then_ 



_if and only if_ 

∇ _f_ ( _x_ ∗)<sup>_T_</sup> ( _y_ − _x_ ∗) ⩾ 0 _,_ ∀ _y_ ∈ Ω _._ 

Lemma C.2 (Bubeck, 2015 [9], Lemma 3.11). _Let f_ : R<sup>_d_</sup> → R _be β-smooth and γ-strongly convex, then for all x,y in_ R<sup>_d_</sup> _,_ 



Lemma C.3 (Kantorovich-Rubinstein). _A distribution map_ D(·) _is ε-sensitive if and only if for all θ,θ_<sup>′</sup> ∈ Θ _:_ 



Lemma C.4. _Let f_ : R<sup>_n_</sup> → R<sup>_d_</sup> _be an L-Lipschitz function, and let X,X_<sup>′</sup> ∈ R<sup>_n_</sup> _be random variables such that W_ 1( _X,X_<sup>′</sup> ) ⩽ _C. Then_ 



_Proof._ 



23 

E[ _<u>f</u>_ <u>(</u> _X_ <u>)]−E[</u> _<u>f</u>_ <u>(</u> _X_<sup>′</sup> <u>)]</u> Now define the unit vector _v_ := ∥ E[ _f_ ( _X_ )]−E[ _f_ ( _X_<sup>′</sup> )]∥2<sup>.By linearity of expectation, we can further</sup> write ∥ E[ _f_ ( _X_ )] − E[ _f_ ( _X_<sup>′</sup> )]∥<sup>2</sup> 2<sup>= ∥E[</sup><sup>_f_(</sup><sup>_X_)] −E[</sup><sup>_f_(</sup><sup>_X_′)]∥2(E[</sup><sup>_v_⊤</sup><sup>_f_(</sup><sup>_X_)] −E[</sup><sup>_v_⊤</sup><sup>_f_(</sup><sup>_X_′)])</sup><sup>_._</sup> 

For any unit vector _v_ and _L_ -Lipschitz function _f_ , _v_<sup>⊤</sup> _f_ is a one-dimensional _L_ -Lipschitz function, so we can apply Lemma C.3 to obtain 



Canceling out ∥ E[ _f_ ( _X_ )] − E[ _f_ ( _X_<sup>′</sup> )]∥2 from both sides concludes the proof. ■ 

## D Proofs of main results 

### D.1 Proof of Theorem 3.5 

Fix _θ,θ_<sup>′</sup> ∈ Θ. Let _f_ ( _ϕ_ ) = E _Z_ ∼D( _θ_ ) _ℓ_ ( _Z_ ; _ϕ_ ) and _f_<sup>′</sup> ( _ϕ_ ) = E _Z_ ∼D( _θ_ ′) _ℓ_ ( _Z_ ; _ϕ_ ). Since _f_ is _γ_ -strongly convex and _G_ ( _θ_ ) is the unique minimizer of _f_ ( _x_ ) we know that, 





Together, these two inequalities imply that 



Next, we observe that ( _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> ))<sup>⊤</sup> ∇ _θℓ_ ( _z_ ; _G_ ( _θ_<sup>′</sup> )) is ∥ _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> )∥2 _β_ -Lipschitz in _z_ . This follows from applying Cauchy-Schwarz and the fact that the loss is _β_ -jointly smooth. Using the dual formulation of the optimal transport distance (Lemma C.3) and _ε_ -sensitivity of D(·), 



Furthermore, using the first-order optimality conditions for convex functions, we have ( _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> ))<sup>⊤</sup> ∇ _f_<sup>′</sup> ( _G_ ( _θ_<sup>′</sup> )) ⩾ 0, and hence ( _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> ))<sup>⊤</sup> ∇ _f_ ( _G_ ( _θ_<sup>′</sup> )) ⩾ − _εβ_ ∥ _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> )∥2∥ _θ_ − _θ_<sup>′</sup> ∥2 _._ Therefore, we conclude that, 



Claim (a) then follows by rearranging. 

To prove claim (b) we note that _θt_ = _G_ ( _θt_ −1) by the definition of RRM, and _G_ ( _θ_ PS) = _θ_ PS by the definition of stability. Applying the result of part (a) yields 



Setting this expression to be at most _δ_ and solving for _t_ completes the proof of claim (b). 

### D.2 Proof of Proposition 3.6 

As for statement (a), we provide one counterexample for each of the statements (b) and (c). 

24 

Proof of (b): Consider a type of regularized hinge loss _ℓ_ ( _z_ ; _θ_ ) = _C_ max(−1 _,yθ_ ) +<sup>_<u>γ</u>_</sup> 2<sup>(</sup><sup>_θ_−1)2, and</sup> suppose Θ ⊇ [− 2<sup><u>1</u></sup> _ε_<sup>_,_</sup> 2<sup><u>1</u></sup> _ε_<sup>].</sup> 

Let the distribution of _Y_ according to D( _θ_ ) be a point mass at _εθ_ , and let the distribution of _X_ be invariant with respect to _θ_ . Clearly, this distribution is _ε_ -sensitive. 

Let _θ_ 0 = 2. Then, by picking _C_ big enough, RRM prioritizes to minimize the first term exactly, and hence we get _θ_ 1 = − 2<sup><u>1</u></sup> _ε_<sup>.In the next step, again due to large</sup><sup>_C_, we get</sup><sup>_θ_2 = 2.Thus,</sup> RRM keeps oscillating between 2 and − 2<sup><u>1</u></sup> _ε_<sup>,failingtoconverge.Thisargumentholdsforall</sup> _γ,ε >_ 0. 

Proof of (c): Suppose that the loss function is the squared loss, _ℓ_ ( _z_ ; _θ_ ) = ( _y_ − _θ_ )<sup>2</sup> , where _y,θ_ ∈ R. Note that this implies _β_ = _γ_ . Let the distribution of _Y_ according to D( _θ_ ) be a point mass at 1 + _εθ_ , and let the distribution of _X_ be invariant with respect to _θ_ . This distribution family satisfies _ε_ -sensitivity, because 



By properties of the squared loss, we know 



It is thus not hard to see that RRM does not contract if _ε_ ⩾<sup>_<u>γ</u>_</sup> _β_<sup>= 1:</sup> | _G_ ( _θ_ ) − _G_ ( _θ_<sup>′</sup> )| = ���1 + _εθ_ − 1 − _εθ_ ′��� = _ε_ | _θ_ − _θ_ ′| _,_ 

which exactly matches the bound of Theorem 3.5 and proves the first statement of the proposition. The unique performatively stable point of this problem is _θ_ such that _θ_ = 1 + _εθ_ , which is _θ_ PS = 1−1 _ε_<sup>for</sup><sup>_ε >_1.</sup> 

For _ε_ = 1, no performatively stable point exists, thereby proving the second claim of the proposition. If _ε >_ 1 on the other hand, and _θ_ 0 � _θ_ PS, we either have _θt_ →∞ or _θt_ →−∞, because 



thus concluding the proof. 

### D.3 Proof of Theorem 3.8 

Since projecting onto a convex set can only bring two iterates closer together, in this proof we ignore the projection operator ΠΘ and treat _G_ gd as performing merely the gradient step. 

We begin by expanding out ∥ _G_ gd( _θ_ ) − _G_ gd( _θ_<sup>′</sup> )∥2<sup>2,</sup> 



25 

Next, we analyze each term individually, 



We start by lower bounding _T_ 2: 



where in the last step we apply the Cauchy-Schwarz inequality. By smoothness, ∇ _θℓ_ ( _Z_ ; _θ_ ) is _β_ -Lipschitz in _Z_ . Together with the fact that _Z_ is _ε_ -sensitive, we can lower bound the first term in the above expression by applying Lemma C.4, which results in − _βε_ ∥ _θ_ − _θ_<sup>′</sup> ∥<sup>2</sup> 2<sup>.</sup> We apply Lemma C.2 to lower bound the second term by 



where we have applied Jensen’s inequality in the last line. Putting everything together, we get 



Now we upper bound _T_ 3. We begin by expanding out the square just as before, 

We again bound each term individually. By the smoothness of the loss and Lemma C.4, 



26 

Moving on to the last term in (5): 



= E _Z_ ∼D( _θ_ ′ <u>) ∇</u> _θℓ_ <u>(</u> _Z_ ; _θ_ <u>)−E</u> _Z_ ∼D( _θ_ ′ <u>) ∇</u> _θℓ_ <u>(</u> _Z_ ; _θ_<sup>′</sup> <u>)</u> where we define the unit vector _v_<sup>def</sup> ∥E _Z_ ∼D( _θ_ ′ ) ∇ _θℓ_ ( _Z_ ; _θ_ )−E _Z_ ∼D( _θ_ ′ ) ∇ _θℓ_ ( _Z_ ; _θ_<sup>′</sup> )∥2<sup>.By smoothness of the loss,</sup> we can conclude that _v_<sup>⊤</sup> ∇ _θℓ_ ( _Z,θ_ ) is _β_ -Lipschitz, so by _ε_ -sensitivity we get 



where in the last step we again apply smoothness. Hence, 



Having bounded all the terms, we now conclude that 



If we take the step size _η_ to be small enough, namely _η_ ⩽ _β_ +2 _γ_<sup>, we get</sup> 



To ensure a contraction, we need 2 _η β_<sup>_<u>βγ</u>_</sup> + _γ_<sup>−</sup><sup>_η_2</sup><sup>_ε_2</sup><sup>_β_2 −2</sup><sup>_η_2</sup><sup>_β_2</sup><sup>_ε_−2</sup><sup>_ηβε >_0.Canceling out</sup><sup>_ηβ_, and</sup> assuming _ε_ ⩽ 1, it suffices to have _β_ 2+ _<u>γγ</u>_<sup>−3</sup><sup>_ηεβ_−2</sup><sup>_ε >_0.Therefore, if</sup><sup>_ε <_</sup> ( _β_ + _γ_ )(1+1 _<u>γ</u> ._ 5 _ηβ_ )<sup>⩽1, the</sup> map _G_ gd is contractive. In particular, we have 



27 

where we use the fact that √1 − _x_ ⩽ 1 − 2<sup>_<u>x</u>_for</sup><sup>_x_∈[0</sup><sup>_,_1].This completes the proof of part (a).</sup> Since we have shown _G_ gd is contractive, by the Banach fixed-point theorem we know that there exists a unique fixed point of _G_ gd. That is, there exists _θ_ PS such that E _Z_ ∼D( _θ_ PS) ∇ _θℓ_ ( _Z_ ; _θ_ PS) = 0. By convexity of the loss function, this means that _θ_ PS is the optimum of E _Z_ ∼D( _θ_ PS) _ℓ_ ( _Z_ ; _θ_ ) over _θ_ , which in turn implies that _θ_ PS is performatively stable. Recursively applying the result of part (a) we get the rate of convergence of RRM to _θ_ PS: 



where in the last step we use the fact that 1 − _x_ ⩽ _e_<sup>−</sup><sup>_x_</sup> . Setting this expression to be at most _δ_ and solving for _t_ completes the proof. 

### D.4 Proof of Theorem 3.10 

Proof of (a): We introduce the main proof idea and then present the full argument. The proof proceeds by case analysis. First, we show that if ∥ _θt_ − _θ_ PS∥2 _> δ_ , performing ERM ensures that with high probability ∥ _θt_ +1 − _θ_ PS∥2 ⩽ 2 _ε γ_<sup>_<u>β</u>_∥</sup><sup>_θt_−</sup><sup>_θ_PS∥2.Using our assumption that</sup><sup>_ε <_</sup> 2<sup>_<u>γ</u>_</sup> _β_<sup>,this</sup> implies that the iterate _θt_ +1 contracts toward _θ_ PS. 

On the other hand, if ∥ _θt_ − _θ_ PS∥2 ⩽ _δ_ , we show that while ERM might not contract, it cannot push _θt_ +1 too far from _θ_ PS either. In particular, _θt_ +1 must be in a<sup>_εβ_</sup> 2 _γ_<sup>_δ_-ball around</sup><sup>_θ_PS.The proof</sup> then concludes by arguing that _θt_ for _t_ ⩾<sup>log(∥</sup><sup>_θ_</sup><sup><u>0−</u></sup><sup>_θ_</sup><sup><u>PS∥2</u></sup><sup>_/δ_</sup><sup><u>)</u></sup> must enter a ball of radius _δ_ around _θ_ PS. log( _γ/_ 2 _εβ_ ) Once this event occurs, no future iterate can exit the<sup>_εβ_</sup> 2 _γ_<sup>_δ_-ball around</sup><sup>_θ_PS.</sup> 

<u>Case 1:</u> ∥ _θt_ − _θ_ PS∥2 _> δ_ . If the current iterate is outside the ball, we show that with high probability the next iterate contracts towards a performatively stable point. In particular, 



To prove this claim, we begin by showing that 



Since the _W_ 1-distance is a metric on the space of distributions, we can apply the triangle inequality to get 



The second term is bounded deterministically by _ε_ ∥ _θt_ − _θ_ PS∥2 due to _ε_ -sensitivity. By Theorem <u>1</u> _t_<sup>2</sup> _π_<sup>2</sup> _c_ <u>1</u> 2 of Fournier & Guillin, 2015 [13], for _nt_ ⩾ , the probability that the first term _c_ 2( _εδ_ )<sup>_m_log</sup> � 6 _p_ � 6 _<u>p</u>_ is greater than _εδ_ is less that _t_<sup>2</sup> _π_<sup>2.Here, the positive constants</sup><sup>_c_1</sup><sup>_,c_2depend on</sup><sup>_α,µ,ξα,µ_and</sup><sup>_m_.</sup> Therefore, 



28 

Using this, we can now prove that the iterates contract. Following the first steps of the proof of Theorem 3.5, we have that 



Like in the proof of Theorem 3.5, the term ( _G_<sup>_nt_</sup> ( _θt_ ) − _G_ ( _θ_ PS))<sup>⊤</sup> E _Z_ ∼D _nt_ ( _θt_ ) ∇ _θℓ_ ( _Z_ ; _G_<sup>_nt_</sup> ( _θt_ )) is 6 _<u>p</u>_ ∥ _G_<sup>_nt_</sup> ( _θt_ ) − _G_ ( _θ_ PS)∥2 · _β_ Lipschitz in _Z_ . Using equation (6), with probability 1 − _π_<sup>2</sup> _t_<sup>2wecan</sup> bound the first term by 





And by strong convexity, 

Plugging back into equation (7), we conclude that with high probability 



Applying a union bound, we conclude that the iterates contract at every iteration where ∥ _θt_ − _θ_ PS∥2 _> δ_ with probability at least 1−<sup>�∞</sup> _t_ =1 _π_ 6<sup>2</sup> _<u>pt</u>_<sup>2= 1−</sup><sup>_p_.Therefore, for</sup><sup>_t_⩾</sup> �1 −<sup>2</sup> _γ_<sup>_εβ_</sup> �−1 log � <u>∥</u> _θ_ <u>0−</u> _δθ_ <u>PS∥2</u> � steps we have 



where we use 1 − _x_ ⩽ _e_<sup>−</sup><sup>_x_</sup> . This implies that _θt_ eventually contracts to a ball of radius _δ_ around _θ_ PS. 

<u>Case 2:</u> ∥ _θt_ − _θ_ PS∥2 ⩽ _δ_ . We show that the RERM iterates can leave a ball of radius _δ_ around _θ_ PS only with negligible probability. We begin by applying the triangle inequality just as we did in the previous case, 

_W_ 1(D<sup>_nt_</sup> ( _θt_ ) _,_ D( _θ_ PS)) ⩽ _W_ 1(D<sup>_nt_</sup> ( _θt_ ) _,_ D( _θt_ )) + _W_ 1(D( _θt_ ) _,_ D( _θ_ PS)) ⩽ _W_ 1(D<sup>_nt_</sup> ( _θt_ ) _,_ D( _θt_ )) + _εδ._ For our choice of _nt_ , with probability at least 1 − _π_<sup>62</sup><sup>_<u>p</u>_</sup> _t_<sup>2this quantity is upper bounded by</sup> 



With this information, we can now apply the exact same steps as in the previous case, but now using the fact that _W_ 1(D<sup>_nt_</sup> ( _θt_ ) _,_ D( _θ_ PS)) ⩽ 2 _εδ_ instead of _W_ 1(D<sup>_nt_</sup> ( _θt_ ) _,_ D( _θ_ PS)) ⩽ 2 _ε_ ∥ _θt_ − _θ_ PS∥2, to conclude that with probability at least 1 − _π_<sup>62</sup><sup>_<u>p</u>_</sup> _t_<sup>2</sup> 



As before, a union bound argument proves that the entire analysis holds with probability 1 − _p_ . 

29 

Proof of (b): The only difference between part (b) in relation to part (a) is the fact that one needs to invoke the steps of Theorem 3.8 rather than Theorem 3.5. 

### D.5 Proof of Proposition 4.1 

We begin by defining the set-valued function, _g_ ( _θ_ ) = argmin _θ_ ′∈Θ DPR( _θ,θ_<sup>′</sup> ). Observe that fixed points of this function correspond to models which are performatively stable. The proof thereby follows from showing that the function _g_ (·) has a fixed point. 

Since the loss is jointly continuous and the set Θ is compact, we can apply Berge’s Maximum Theorem [1, 5] to conclude that the function _g_ (·) is upper hemicontinuous with compact and non-empty values. Furthermore, by convexity of the loss, it follows that in addition to being compact and non-empty, _g_ ( _θ_ ) is a convex set for every _θ_ ∈ Θ. Therefore, the conditions of Kakutani’s Theorem [23] (also see Ch 17. in [1]) hold and we can conclude that _g_ (·) has a fixed point. Hence, a performatively stable model exists. 

### D.6 Proof of Proposition 4.2 

We make a slight modification to Example 2.2 to prove the proposition. As in the example, D( _θ_ ) is given as follows: _X_ is a single feature supported on {±1} and _Y_ | _X_ ∼ Bernoulli(<sup><u>1</u></sup> 2<sup>+</sup><sup>_µX_+</sup><sup>_εθX_),</sup> where Θ = [0 _,_ 1]. We let _ε_ ⩾<sup><u>1</u></sup> 2<sup>, and constrain</sup><sup>_µ_to satisfy |</sup><sup>_µ_+</sup><sup>_ε_| ⩽</sup><sup><u>1</u></sup> 2<sup>.We assume that outcomes</sup> are predicted according to the model _fθ_ ( _x_ ) = _θx_ +<sup><u>1</u></sup> 2<sup>and that performance is measured via the</sup> squared loss, _ℓ_ ( _z_ ; _θ_ ) = ( _y_ − _fθ_ ( _x_ ))<sup>2</sup> . This loss has condition number<sup>_<u>β</u>_</sup> _γ_<sup>= 1.</sup> 

A direct calculation demonstrates that the performative risk is a quadratic in _θ_ : 



Therefore, if _ε_ ∈ � 21<sup>_,_1</sup> �, the performative risk is a concave function of _θ_ , even though _ε <_<sup>_<u>γ</u>_</sup> _β_<sup>.</sup> 

### D.7 Proof of Theorem 4.3 

By definition of performative optimality and performative stability we have that: 

DPR( _θ_ PO _,θ_ PO) ⩽ DPR( _θ_ PS _,θ_ PS) ⩽ DPR( _θ_ PS _,θ_ PO) _._ 





30 

Since the population distributions are _ε_ -sensitive and the loss is _Lz_ -Lipschitz in _z_ , we have that DPR( _θ_ PS _,θ_ PO) − DPR( _θ_ PO _,θ_ PO) ⩽ _Lzε_ ∥ _θ_ PO − _θ_ PS∥2. If _ε <_<sup>_<u>γ</u>_</sup><sup><u>∥</u></sup><sup>_θ_</sup><sup><u>PO</u></sup> 2 _L_<sup>−</sup> _z_<sup>_θ_</sup><sup><u>PS∥2</u></sup> then we have that _Lzε_ ∥ _θ_ PO − _θ_ PS∥2 _<_<sup>_<u>γ</u>_</sup> 2<sup>∥</sup><sup>_θ_PO −</sup><sup>_θ_PS∥</sup> 2<sup>2which is a contradiction since it must hold that</sup> 

DPR( _θ_ PS _,θ_ PO) − DPR( _θ_ PO _,θ_ PO) ⩾ DPR( _θ_ PS _,θ_ PO) − DPR( _θ_ PS _,θ_ PS) _._ 

### D.8 Proof of Corollary 5.1 

By Theorem 3.5 we know that repeated risk minimization converges at a linear rate to a performatively stable point _θ_ PS. Furthermore, by Theorem 4.3, this performatively stable point is close in domain to the institution’s Stackelberg equilibrium classifier _θ_ SE, 



We can then use the fact that the loss is Lipschitz to show that this performatively stable classifier is close in objective value to the Stackelberg equilibrium: 



Here, we have used the Kantorovich-Rubinstein Lemma (C.3) to bound the second term. 

## E Approximately minimizing performative risk via regularization 

Recall that in Proposition 3.6 we have shown that RRM might not converge at all if the objective is smooth and convex, but not strongly convex. In this section, we show how adding a small amount of quadratic regularization to the objective guarantees that RRM will converge to a stable point which approximately minimizes the performative risk on the original loss. 

To do so, we additionally require that the space of model parameters Θ be bounded with diameter _D_ = sup _θ,θ_ ′∈Θ ∥ _θ_ − _θ_<sup>′</sup> ∥2. We can assume without loss of generality that _D_ = 1. 

Proposition E.1. _Suppose that the loss ℓ_ ( _z_ ; _θ_ ) _is Lz-Lipschitz iz z and Lθ-Lipschitz in θ, β-jointly smooth_ (A1) _and convex (but not necessarily strongly convex). Furthermore, suppose that distribution map_ D(·) _is ε-sensitive with ε <_ 1 _, and that the set_ Θ _is bounded with diameter 1. Then, there exists a choice of α, such that running RRM with loss ℓ_<sup>_reg_</sup> ( _z_ ; _θ_ )<sup>def</sup> = _ℓ_ ( _z_ ; _θ_ ) +<sup>_<u>α</u>_</sup> 2<sup>∥</sup><sup>_θ_−</sup><sup>_θ_0∥</sup> 2<sup>2</sup><sup>_convergestoa_</sup> _performatively stable point θ_ PS<sup>_regwhich satisfies the following_</sup> 



We note that in the case where _ε_ = 0, the limit point _θ_ PS<sup>regofregularizedrepeatedrisk</sup> minimization is also performatively optimal. 

31 

_Proof._ First, we observe that the regularized loss function _ℓ_<sup>reg</sup> ( _z_ ; _θ_ ) is _α_ -strongly convex and _α_ + _β_ -jointly smooth. Since _ε <_ 1, we can then choose an _α_ such that _ε < αα_ + _β_<sup>.In particular, we</sup> choose _α_ =<sup>√</sup> _εβ/_ (1 − _ε_ ). 

From our choice of _α_ , we have that _ε_ is smaller than the inverse condition number. Hence, by Theorem 3.5 repeated risk minimization converges at a linear rate to a performatively stable solution _θ_ PS<sup>_reg_of the regularized objective.</sup> 

To finish the proof, we show that the objective value at the _θ_ PS<sup>_reg_is close to the objective value</sup> at the performative optima of the original objective _θ_ PO. We do so by bounding their difference using the triangle inequality: 



We can bound the first difference via Lipschitzness: 



In the last two lines, we have applied the fact that _D_ = sup _θ,θ_ ′∈Θ ∥ _θ_ − _θ_<sup>′</sup> ∥2 = 1 as well as Theorem 4.3. For the second difference, by definition of performative optimality we have that, 



Where we have again used the fact that _D_ = 1 for the last inequality. Combining these two together, we can bound the total difference: 



~~<u>√</u>~~ _εβ_ Plugging in _α_ = 1− _ε_<sup>completes the proof.</sup> 



32 

