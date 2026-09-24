---
title: "Outside the Echo Chamber: Optimizing the Performative Risk"
authors: "risk"
year: 2021
arxiv_id: "2102.08570"
original_file: "2102.08570.pdf"
pdf_path: "docs/papers\2021_risk_outside_the_echo_chamber_optimizing.pdf"
---

# Outside the Echo Chamber: Optimizing the Performative Risk

**Authors:** Risk et al.  
**Year:** 2021 | **arXiv:** [`2102.08570`](https://arxiv.org/abs/2102.08570)  
**Local PDF:** [`2021_risk_outside_the_echo_chamber_optimizing.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2021_risk_outside_the_echo_chamber_optimizing.pdf)

---

# Outside the Echo Chamber: Optimizing the Performative Risk 

John Miller* Juan C. Perdomo* Tijana Zrnic* {miller_john, jcperdomo, tijana.zrnic}@berkeley.edu 

University of California, Berkeley 

June 17, 2021 

#### Abstract 

In performative prediction, predictions guide decision-making and hence can influence the distribution of future data. To date, work on performative prediction has focused on finding performatively stable models, which are the fixed points of repeated retraining. However, stable solutions can be far from optimal when evaluated in terms of the performative risk, the loss experienced by the decision maker when deploying a model. In this paper, we shift attention beyond performative stability and focus on optimizing the performative risk directly. We identify a natural set of properties of the loss function and model-induced distribution shift under which the performative risk is convex, a property which does not follow from convexity of the loss alone. Furthermore, we develop algorithms that leverage our structural assumptions to optimize the performative risk with better sample efficiency than generic methods for derivative-free convex optimization. 

## 1 Introduction 

Predictions in social settings are rarely made in isolation, but rather to inform decision-making. This link between predictions and decisions causes predictive models to often be _performative_ , meaning they can alter their environment once deployed. For example, election forecasts impact campaign spending and affect voter turnout, hence influencing the final election outcome [44]. Similarly, long-term climate forecasts shape policy decisions which can then affect future weather patterns. 

Performative prediction is a recent framework introduced by Perdomo et al. [28] which formalizes the idea that predictive models can impact the data-generating process. So far, work in this area has focused on a particular equilibrium notion known as _performative stability_ [5, 10, 22]. Stability is a local definition of optimality, by which a model minimizes the expected risk for the specific distribution that it induces. However, stability provides no general guarantees of performance beyond this equilibrium notion. In fact, stable models can have exceedingly poor _performative risk_ , the central measure of performance in the performative prediction framework which captures the true risk incurred by the learner when deploying the model. 

* Equal contribution. 

1 

Reasoning by analogy, stable classifiers can be thought of as an _echo chamber_ in an online platform. In an echo chamber, one is reassured of their ideas by voicing them, but it’s not clear whether they are reasonable outside of this niche community. Similarly, stable classifiers minimize risk on the distribution that they induce, but they provide no global guarantees of performance. 

Therefore, to develop accurate predictions in performative settings, we shift attention past performative stability and study optimizing the performative risk directly. This task has so far remained elusive due to the complexities of model-induced distribution shift, i.e. performative effects. In particular, even in simple settings with convex losses, these distribution shifts can make the performative risk non-convex as noted in [28]. Furthermore, optimizing the performative risk requires a different algorithmic approach than what was previously studied in performative prediction. For instance, the learner needs to actively _anticipate_ performative effects rather than myopically retrain until convergence, as the latter would only lead to stability. In short, repeated retraining is an inadequate method of overcoming performative distribution shifts. 

### 1.1 Our Contributions 

In this paper, we provide the first set of results describing when and how the performative risk may be optimized efficiently. We identify natural assumptions under which the performative risk is convex, even in settings where performative effects can be arbitrarily strong. Furthermore, we study optimization algorithms which explicitly model distribution shift and provably minimize the performative risk in an efficient manner. 

To give an overview of our main results, we recall the relevant concepts from the performative prediction framework. Relative to supervised learning, where the learner observes data from a single _static_ distribution, the key conceptual innovation in the performative prediction framework is the notion of a _distribution map_ D(·), which maps model parameters _θ_ ∈ R<sup>_d_</sup> to a distribution D( _θ_ ) over instances _z_ . Given a loss _ℓ_ , the quality of a predictive model parameterized by _θ_ is measured according to its _performative risk_ , 



A classifier _θ_ PO is _performatively optimal_ if it minimizes the performative risk, i.e _θ_ PO ∈ argmin _θ_ PR( _θ_ ). On the other hand, a classifier _θ_ PS is _performatively stable_ if it satisfies the fixed-point condition, 



In other words, stable classifiers are those which are optimal for the particular distribution they induce. However, stability has little bearing on whether a classifier has low performative risk. More specifically, the following observation motivates a large part of our later analysis: 

_Stable classifiers can maximize the performative risk even when the loss is well-behaved and performative effects are small._ 

Not only can stable points maximize the performative risk, but they can also have an arbitrarily large suboptimality gap, PR( _θ_ PS) − PR( _θ_ PO). The most natural first step towards optimizing the performative risk is to ensure that it is _convex_ . Our first main result states that under an appropriate stochastic dominance condition which ensures the distribution map is well-behaved, there exists a critical threshold on the strength of performative effects that guarantees convexity: 

2 

Theorem 1.1 (Informal). _Assume that the loss is β-smooth in z and γ-strongly convex in θ. If the map_ D(·) _is ε-Lipschitz and satisfies an appropriate stochastic dominance condition, then the performative risk is guaranteed to be convex if and only if ε_ ⩽<sup>_<u>γ</u>_</sup> 2 _β_<sup>_._</sup> 

Interestingly, previous work has established that _ε < γ/β_ is a threshold for repeated retraining to provably converge to a performatively stable point. We show that if we halve this quantity, we get another threshold which determines whether the performative risk is provably convex. 

While Theorem 1.1 suggests that performative effects need to be small in order to guarantee convexity, we prove that this need not be the case for the setting of _location-scale_ families. These are natural classes of distribution maps in which performative effects enter through an additive or multiplicative factor that is linear in _θ_ . Many examples of distribution maps that have appeared in prior work are in fact location-scale families. For this setting, we generalize Theorem 1.1 to prove the following structural result. 

Theorem 1.2 (Informal). _If the loss is smooth, strongly convex and the map_ D(·) _is a location-scale family, then the performative risk can be convex irrespective of the Lipschitz constant of_ D(·) _._ 

Finally, having established these structural properties, we turn to algorithms for finding performative optima. Modulo weak regularity assumptions, convexity alone is sufficient to apply classical zeroth-order algorithms in order to find optima in polynomial time. That said, the convergence rate of these algorithms is typically quite slow. 

To address this problem, we propose a _two-stage_ approach, by which the learner first creates an explicit model of the distribution map D<sup>�</sup> , and then optimizes a proxy objective for the performative risk obtained by “plugging in” D<sup>�</sup> as if it were really the true distribution map. We instantiate this two-stage procedure in the context of location families, and prove that it optimizes the performative risk with significantly better sample efficiency then generic zerothorder algorithms. 

### 1.2 Related Work 

We build on the recent line of work on performative prediction started by Perdomo et al. [28]. While previous papers in this area have focused on performative stability [5, 10, 22], we move past this solution concept and instead analyze conditions under which one can compute performatively optimal classifiers. 

Given that strategic classification is formally a special case of performative prediction (see Section 5 or discussion in [28] for further details), the study of performative optimality has been implicitly considered in the growing body of work on strategic classification [3, 6, 13– 15, 23, 36, 41]. More specifically, performatively optimal classifiers correspond to Stackelberg equilibria in strategic classification. In contrast to papers within this literature, our analysis relies on identifying macro-level assumptions on the loss and the distribution shift which make the problem tractable, rather than specific micro-level assumptions on the costs or utilities of the agents. For example, Dong et al. [9] prove that the institution’s objective (performative risk) is convex by assuming that the agents are rational and compute best-responses according to particular utilities and cost functions. On the other hand, our conditions are on the distribution map and do not directly constrain behavior at the agent level. 

Similarly, several papers in strategic classification [9, 26] and policy design [43] have recognized that one can apply zeroth-order algorithms [1, 11, 35] to find optima of the institution’s risk. The main challenge in applying zeroth-order optimization is the fact that, in general, 

3 

the performative risk might not satisfy any structural properties which would imply that its stationary points have low risk. One of the main contributions of this paper is precisely to identify under what conditions we can expect this behavior to hold. 

Several works within the economics literature [12, 26] have also contrasted fixed points of retraining and institutional optima; these analyses resemble our comparisons of stability and optimality, albeit in a more specific setting. Furthermore, there are other settings beyond strategic classification that have similarly studied optimality in the face of performative effects, such as in the context of rankings or selection bias [17, 31, 39]. 

Lastly, our two-stage approach to minimizing the performative risk, whereby we first estimate a model of the distribution map and then optimize a proxy objective, is closely related to ideas in neighboring fields. At a high level, this general principle has appeared in semiparametric statistics [4, 16, 18, 27, 29] and more recently in double machine learning [7, 8, 19]. Furthermore, this idea has been extensively studied in the controls literature where it is referred to as certainty equivalence [20, 37, 38, 40], or as model-based planning in reinforcement learning [2]. 

### 1.3 Additional Preliminaries 

As done by previous works in this area, we limit ourselves to considering predictive models parameterized by a finite-dimensional vector _θ_ ∈ Θ ⊆ R<sup>_d_</sup> , where Θ is a closed, convex set. The distribution map D(·) maps parameter vectors to data distributions over real-valued instances _z_ ∈ R<sup>_m_</sup> . While each model _θ_ can induce a potentially distinct distribution D( _θ_ ), we expect similar classifiers to induce similar distributions. This intuition is captured by the notion of _ε_ - _sensitivity_ , which is essentially a Lipschitz condition on the distribution map D(·). We state that D(·) is _ε_ -sensitive for some _ε_ ⩾ 0 if for all _θ,θ_<sup>′</sup> ∈ Θ, 



Here, _W_ 1 denotes the Wasserstein-1 or earth mover’s distance between two distributions. 

## 2 Contrasting Optimality and Stability 

Up until now, all works within the performative prediction literature have focused on analyzing when different algorithms converge to stable points. While the primary motivation for stability was eliminating the need for retraining, it was observed as a useful byproduct that stable points can approximately minimize the performative risk. 

More specifically, Perdomo et al. [28] prove that all stable points and performative optima lie within _ℓ_ 2-distance at most 2 _Lzε/γ_ of each other, where _ε_ is the sensitivity of the distribution map, _γ_ denotes the strong convexity parameter of the loss, and _Lz_ denotes the Lipschitz constant of the loss _in z_ . At first glance, this result implicitly suggests that stable points also have good predictive performance. While this is sometimes the case, in many settings _Lz_ is large enough to make the bound vacuous. For example, there exist cases where the performative risk is strongly convex, but stable points actually _maximize_ the performative risk. 

Proposition 2.1. _For any γ,_ ∆ _>_ 0 _, there exists a performative prediction problem where the loss is γ-strongly convex in θ, yet the unique stable point θ_ PS _maximizes the performative risk and_ PR( _θ_ PS) − min _θ_ PR( _θ_ ) ⩾ ∆ _._ 

4 

_Proof._ We prove the proposition by constructing an example. Let _z_ ∼D( _θ_ ) be a point mass at _εθ_ , and define the loss to be: 



for some _β_ ⩾ 0. This loss is _γ_ -strongly convex and the distribution map is _ε_ -sensitive. A short calculation shows that the performative risk simplifies to 



For _ε_ � _γ/β_ , there is a unique performatively stable point at the origin, and if _ε >_ 2 _<u>γβ</u>_<sup>this</sup> point is the unique maximizer of the performative risk. Moreover, for _ε >_ 2<sup>_<u>γ</u>_</sup> _β_<sup>,min</sup><sup>_θ_PR(</sup><sup>_θ_) =</sup> ( _γ/_ 2 − _εβ_ ) · max _θ_ ∈Θ ∥ _θ_ ∥<sup>2</sup> 2<sup>.Therefore, depending on the radius of Θ, the suboptimality gap of</sup><sup>_θ_PS</sup> can be arbitrarily large. ■ 

In the above example, ∇ _θℓ_ ( _z_ ; _θ_ ) is _β_ -Lipschitz in _z_ , a condition commonly referred to as _smoothness_ in prior work on performativity. The previous proposition thus shows that stable points can have an arbitrary suboptimality gap when _ε >_ 2<sup>_<u>γ</u>_</sup> _β_<sup>.This is important since</sup><sup>_ε <_</sup><sup>_<u>γ</u>_</sup> _β_<sup>is</sup> the regime where previously studied algorithms for optimizing under performativity—such as repeated risk minimization or different variants of gradient descent [22, 28]—converge to stability. Applying these methods when _ε_ ∈ ( _γ/_ (2 _β_ ) _,γ/β_ ) would hence maximize the performative risk on this problem. 

Moreover, we remark that the Lipschitz constant _Lz_ is equal to _β_ ·max _θ_ ∈Θ ∥ _θ_ ∥2. Therefore, the results of [28] imply that stable points and optima are at distance at most<sup>2</sup><sup>_Lzε_</sup> =<sup>2</sup><sup>_<u>βε</u>_</sup> _γ γ_<sup>max</sup><sup>_θ_∈Θ ∥</sup><sup>_θ_∥2.</sup> When _ε >_ 2<sup>_<u>γ</u>_</sup> _β_<sup>, as assumed in the proof of Proposition 2.1, this bound on the distance becomes</sup> vacuous: ∥ _θ_ PS − _θ_ PO∥2 ⩽ max _θ_ ∈Θ ∥ _θ_ ∥2. 

Lastly, we point out that _ε_ = 2<sup>_<u>γ</u>_</sup> _β_<sup>is a sharp threshold for convexity of the performative risk</sup> in this example, as can be seen in Equation (1). In the following section, we show that this threshold behavior is not an artifact of this particular setting, but rather a phenomenon that holds more generally. 

## 3 Convexity of the Performative Risk 

We now introduce our main structural results illustrating how the performative risk can be convex in various natural settings, and hence amenable to direct optimization. Throughout our presentation, we adopt the following convention. We state that the performative risk is _λ_ -convex, for some _λ_ ∈ R, if the objective, 



is convex. In other words, if _λ_ is positive, then PR( _θ_ ) is _λ_ -strongly convex. If _λ_ is negative, then adding the analogous regularizer<sup>_<u>λ</u>_</sup> 2<sup>∥</sup><sup>_θ_∥2 ensures PR(</sup><sup>_θ_) is convex.Furthermore, in addition to</sup> _ε_ -sensitivity, we will make repeated use of the following assumptions throughout the remainder of the paper. To facilitate readability, we let Z<sup>def</sup> = ∪ _θ_ ∈Θsupp(D( _θ_ )). We say that a loss function _ℓ_ ( _z_ ; _θ_ ) is _β_ - _smooth_ in _z_ if for all _θ_ ∈ Θ and _z,z_<sup>′</sup> ∈Z, 



5 

Furthermore, a loss function _ℓ_ ( _z_ ; _θ_ ) is _γ_ - _strongly convex_ in _θ_ if for all _θ,θ_<sup>′</sup> _,θ_ 0 ∈ Θ, 



If _γ_ = 0, this assumption is equivalent to convexity. Similarly, we say that the loss is _γz_ -strongly convex in _z_ if for all _θ_ ∈ Θ and _z,z_<sup>′</sup> ∈Z, 



Lastly, we state that a distribution map, loss pair (D(·) _,ℓ_ ) satisfies _mixture dominance_ if the following condition holds for all _θ,θ_<sup>′</sup> _,θ_ 0 ∈ Θ and _α_ ∈ (0 _,_ 1): 



Smoothness and strong convexity are standard and have appeared previously in the context of performative prediction. The mixture dominance condition is novel and plays a central role in our analysis of when the performative risk is convex. To provide some intuition for this condition, we recall the definition of the _decoupled performative risk_ : 



Notice that asserting convexity of the performative risk is equivalent to showing convexity of DPR( _θ,θ_ ) when both arguments are forced to be the same. While convexity (A3a) guarantees that DPR is convex in the second argument, mixture dominance (A4) essentially posits convexity of DPR in the first argument. Importantly, assuming convexity in each argument separately does _not_ directly imply that the performative risk is convex. 

On a more intuitive level, this assumption (A4) is essentially a stochastic dominance statement: the mixture distribution _α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ) “dominates” D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) under a certain loss function. Similar conditions have been extensively studied within the literature on stochastic orders [33], which we further discuss in Appendix A. Part of our analysis relies on incorporating tools from this literature, and we believe that further exploring technical connections between this field and performative prediction could be valuable. For example, using results from stochastic orders we can show that (A4) holds when the loss is convex in _z_ and the distribution map D(·) forms a _location-scale family_ of the form: 



where _z_ 0 ∼D0 is a sample from a fixed zero-mean distribution D0, and Σ( _θ_ ) _,µ_ are linear maps (see Proposition A.4 for a formal proof). Distribution maps of this sort are ubiquitous throughout the performative prediction literature and hence satisfy mixture dominance if the loss _ℓ_ is convex. For instance, the distribution map for the strategic classification simulator in [28] is a location family. Other examples of location families can be found in previous work on strategic classification [12, 13]. Mixture dominance can also hold in discrete settings, e.g. D( _θ_ ) = Bernoulli( _a_<sup>⊤</sup> _θ_ + _b_ ) satisfies this condition for any loss. Having provided some context on the mixture dominance condition, we can now state the main result of this section: 

Theorem 3.1. _Suppose that the loss function ℓ_ ( _z_ ; _θ_ ) _is γ-strongly convex in θ_ (A3a) _, β-smooth in z_ (A2) _, and that_ D(·) _is ε-sensitive_ (A1) _. If mixture dominance_ (A4) _holds, then the performative risk is λ-convex for λ_ = _γ_ − 2 _εβ._ 

6 

Together with the example from the proof of Proposition 2.1, this theorem shows that 2<sup>_<u>γ</u>_</sup> _β_<sup>is a</sup> sharp threshold for convexity of the performative risk. If _ε_ is strictly less than this threshold, then under mixture dominance and appropriate conditions on the loss, the performative risk is strongly convex by Theorem 3.1. On the other hand, if _ε_ is above this threshold, the example from Proposition 2.1 shows that there exists a performative prediction instance which satisfies the remaining assumptions, yet is non-convex; in particular, for _ε >_ 2<sup>_<u>γ</u>_</sup> _β_<sup>the performative risk</sup> is strictly concave in that example. This threshold was also implicitly observed by Perdomo et al. [28] in the proof of Proposition 4.2 as byproduct of showing that the performative risk can be non-convex for _ε_ ⩽<sup>_<u>γ</u>_</sup> _β_<sup>.However, they provide no general analysis of when the performative</sup> risk is convex. Note that all of the above examples satisfy mixture dominance. 

While the threshold _ε_ = _γ/_ (2 _β_ ) is in general tight as argued above, for certain families of distribution maps the conclusion of Theorem 3.1 can be made considerably stronger. Indeed, in some cases the performative risk is convex _regardless_ of the magnitude of performative effects, as observed for the following location family. 

Example 3.2. Consider the following stylized model of predicting the final vote margin in an election contest. Features _x_ , such as past polling averages, are drawn i.i.d. from a static distribution, _x_ ∼D _x_ . Since predicting a large margin in either direction can dissuade people from voting, we consider outcomes drawn from the conditional distribution: _y_ | _x_ ∼ _g_ ( _x_ )+ _µ_<sup>⊤</sup> _θ_ + _ξ_ , where _g_ : R<sup>_d_</sup> → R is an arbitrary map, _µ_ ∈ R<sup>_d_</sup> is a fixed vector, and _ξ_ is a zero-mean noise variable. If _ℓ_ is the squared loss, _ℓ_ (( _x,y_ ); _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_y_−</sup><sup>_x_⊤</sup><sup>_θ_)2, or the absolute loss,</sup><sup>_ℓ_((</sup><sup>_x,y_);</sup><sup>_θ_) = |</sup><sup>_y_−</sup><sup>_x_⊤</sup><sup>_θ_|, then</sup> the performative risk is convex for any _g_ and _µ_ . 

The proof follows by simply observing that in both cases, the performative risk can be written as a linear function in _θ_ composed with a convex function. Another interesting property of this example is that the distribution map is _ε_ -sensitive with _ε_ = ��� _µ_ ���2, yet the sensitivity parameter plays no role in the characterization of convexity. Motivated by this observation, we specialize the analysis in Theorem 3.1 to the particular case of location-scale families, and obtain a result that is at least as tight as the previous theorem. 

Theorem 3.3. _Suppose that ℓ_ ( _z_ ; _θ_ ) _is γ-strongly convex in θ_ (A3a) _, β-smooth_ (A2) _, and γz-strongly convex in z_ (A3b) _. Furthermore, suppose that_ D( _θ_ ) _forms a location-scale family_ (2) _with ε as its sensitivity parameter_<sup>1</sup> _. Define_ Σ _z_ 0 _to be the covariance matrix of z_ 0 ∼D0 _, and let_ 



_Then, the performative risk is λ-convex for λ equal to:_ 



This tighter bound leverages the fact that some losses are strongly convex in the performative variables, such as the squared loss when only the outcome variable exhibits performative effects. In general, one can achieve a tighter analysis of when the performative risk is convex by distinguishing between variables which are _static_ , whose distribution is the same under D( _θ_ ) for all _θ_ , and performative variables which are influenced by the deployed classifier. For the most part we avoid this distinction in the main body for the sake of readability, however, we elaborate 

> 1The sensitivity parameter _ε_ for location-scale families can be explicitly bounded in terms of the parameters _µ_ and Σ( _θ_ ); see Remark C.3 in the Appendix. 

7 

on how the analysis can be strengthened in Appendix B. We now illustrate an application of Theorem 3.3 on a scale family example. 

Example 3.4. Suppose that _x >_ 0 is a one-dimensional feature drawn from a fixed distribution D _x_ , and let _y_ | _x_ ∼ _θx_ · Exp(1) be distributed as an exponential random variable with mean _θx_ . Let the loss be the squared loss, _ℓ_ (( _x,y_ ); _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_y_−</sup><sup>_θ_·</sup><sup>_x_)2and let Θ = R+.Note that this example</sup> exhibits a self-fulfilling prophecy property whereby all solutions are performatively stable. On the other hand, PR( _θ_ ) = _θ_<sup>2</sup> E _x_<sup>2</sup> , and the unique performative optimum is _θ_ PO = 0. Again, we see how stability has no bearing on whether a solution has low performative risk. 

However, we note that the loss is 1-strongly convex in _y_ . Furthermore, by averaging over the static features, we observe that PR( _θ_ ) is E _x_<sup>2</sup> -strongly convex in _θ_ and E _x_ -smooth in _y_ . Therefore, according to Theorem 3.3, the performative risk is convex and hence tractable to optimize, since _γ_ − _β_<sup>2</sup> _/γz_ = E _x_<sup>2</sup> − (E _x_ )<sup>2</sup> ⩾ 0 by Jensen’s inequality. 

While this example, like most others in this section, is intended as a toy problem to provide the reader with some intuition regarding the intricacies of performativity, many instances of performative prediction in the real world do exhibit a self-fulfilling prophecy aspect whereby predicting a particular outcome increases the likelihood that it occurs. For instance, predicting that a student is unlikely to do well on a standardized exam may discourage them from studying in the first place and hence lower their final grade. Settings like these where stability is a vacuous guarantee of performance remind us how developing reliable predictive models requires going outside the stability echo chamber. 

As a final note, to prove the results in this section, we have imposed additional assumptions such as mixture dominance, or analyzed the special case of location-scale families. The reader might naturally ask whether these settings are so restrictive that one can optimize the performative risk using previous optimization methods for performative prediction which find stable points. Or in particular, whether stable points and performative optima now identify. 

It turns out that both solutions can still have qualitatively different behavior, regardless of the strength of performative effects. First, notice that the example in the proof of Proposition 2.1 is a location family, and as such it satisfies mixture dominance. In that example, when _ε_ ∈ ( 2<sup>_<u>γ</u>_</sup> _β_<sup>_,_</sup><sup>_<u>γ</u>_</sup> _β_<sup>),</sup> methods for finding stable points converge to a maximizer of the performative risk; however, this is outside the regime where the performative risk is convex. In what follows, by relying on Theorem 3.3, we provide another scale family example where the performative risk is convex regardless of _ε_ , yet stable points can be arbitrarily suboptimal. 

Example 3.5. Suppose that D( _θ_ ) = N ( _µ,ε_<sup>2</sup> _θ_<sup>2</sup> ) for some _µ_ ∈ R and _ε >_ 0. This distribution map is _ε_ -sensitive. Furthermore, if _ℓ_ is the squared loss, _ℓ_ ( _z_ ; _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_z_−</sup><sup>_θ_)2, then there is a unique</sup> stable point _θ_ PS = _µ_ . On the other hand, _θ_ PO = _µ/_ (1 + _ε_<sup>2</sup> ). 

Notice how, contrary to the performative optimum _θ_ PO, the stable point _θ_ PS is independent of _ε_ and hence oblivious to the performative effects. Depending on _µ_ , the stable point can be arbitrarily suboptimal, since PR( _θ_ PS) − PR( _θ_ PO) = Ω( _µ_<sup>2</sup> ). Note also that, according to Theorem 3.3, the performative risk is _γ_ − 2 _εβ_ + _γzσ_ min<sup>2(Σ) = 1 −2</sup><sup>_ε_+</sup><sup>_ε_2-convex.Since 1 −2</sup><sup>_ε_+</sup><sup>_ε_2 = (</sup><sup>_ε_−1)2 ⩾0,</sup> the performative risk is always convex and hence tractable to optimize. 

## 4 Optimization Algorithms 

Having identified conditions under which the performative risk is convex, we now consider methods for efficiently optimizing it. One of the main challenges of carrying out this task 

8 

is that, even in convex settings, the learner can only access the objective via noisy function evaluations corresponding to classifier deployments. Without knowledge of the underlying distribution map, it is infeasible to compute gradients of the performative risk. A naive solution is to apply a zeroth-order method, however, these algorithms are in general hard to tune, and their performance scales poorly with the problem dimension. 

Our main algorithmic contribution is to show how one can address these issues by creating an explicit _model_ of the distribution map and then optimizing a proxy objective for the performative risk offline. We refer to this as the two-stage procedure for optimizing the performative risk and show it is provably efficient for the case of location families. To develop further intuition, consider the following simple example. Let _z_ ∼N ( _εθ,_ 1) be a one-dimensional Gaussian and let _ℓ_ ( _z_ ; _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_z_−</sup><sup>_θ_)2be the squared loss.Then, the performative</sup> risk, PR( _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_ε_−1)2</sup><sup>_θ_2, is a simple, convex function for all values of</sup><sup>_ε_(as indeed confirmed by</sup> Theorem 3.3, since _γ_ − 2 _εβ_ + _γzσ_ min<sup>2(</sup><sup>_µ_) = 1 −2</sup><sup>_ε_+</sup><sup>_ε_2 ⩾0).However, gradients are unavailable</sup> since they depend on the density of D( _θ_ ), denoted _pθ_ , which is typically unknown: 



Despite the simplicity of this example, earlier approaches to optimization in performative prediction, such as repeated retraining [28], fail on this problem. The reason is that they essentially ignore the second term in the gradient computation which requires explicitly anticipating performative effects. For example, retraining computes the sequence of updates _θt_ +1 = argmin _θ_ E _z_ ∼D( _θt_ ) 2<sup><u>1</u>(</sup><sup>_z_−</sup><sup>_θ_)2 =</sup><sup>_εθt_, which diverges for |</sup><sup>_ε_|</sup><sup>_>_1.</sup> 

### 4.1 Generic Derivative-Free Methods 

Having observed the difficulty of computing gradients, the most natural starting point for optimizing the performative risk is to consider derivative-free methods for convex optimization [1, 11, 35]. These methods work by constructing a noisy estimate of the gradient by querying the objective function at a randomly perturbed point around the current iterate. For instance, Flaxman et al. [11] sample a vector _u_ ∼ Unif(S<sup>_d_−1</sup> ) to get a slightly biased gradient estimator, 



for some small _δ >_ 0. Generic derivative-free algorithms for convex optimization require few assumptions beyond those given in the previous section to ensure convexity. Moreover, they guarantee convergence to a performative optimum given sufficiently many samples. However, their rate of convergence can be slow and scales poorly with the problem dimension. In general, zeroth-order methods require _O_<sup>�</sup> ( _d_<sup>2</sup> _/_ ∆<sup>2</sup> ) samples to obtain a ∆-suboptimal point [1, 35], which can be prohibitively expensive if samples are hard to come by. 

### 4.2 Two-Stage Approach 

In cases where we have further structure, an alternative solution to derivative-free methods is to utilize a _two-stage_ approach to optimizing the performative risk. In the first stage, we estimate a coarse model of the distribution map, D<sup>�</sup> (·) via experiment design. Then, in the second stage, the 

9 

Algorithm 1 Two-Stage Algorithm for Location Families 

Stage 1: Construct a model of the distribution map // Estimate location parameter _µ_ with experiment design for _i_ = 1 to _n_ do i.i.d. -Sample and deploy classifier _θi_ ∼N (0 _,Id_ ). -Observe _zi_ ∼D( _θi_ ). end for -Estimate _µ_ via ordinary least squares, � _µ_ ∈ argmin _µ_ � _ni_ =1 ��� _zi_ − _µθi_ ���22<sup>.</sup> // Gather samples from the base distribution for _j_ = _n_ + 1 to 2 _n_ do -Deploy classifier _θj_ = 0, and observe _zj_ ∼D(0). end for Stage 2: Minimize a finite-sample approximation of the performative risk, argmin _θ_ ∈Θ _n_ <u>1 �2</u> _j_ = _nn_ +1<sup>_ℓ_(</sup><sup>_zj_+ �</sup><sup>_µθ_;</sup><sup>_θ_).</sup> 

algorithm optimizes a proxy to the performative risk treating the estimated D<sup>�</sup> as if it were the true distribution map: 



The exact implementation of this idea depends on the problem setting at hand; to make things concrete, we instantiate the approach in the context of location families and prove that it optimizes the performative risk with significantly better sample complexity than generic zeroth-order methods. For the remainder of this section, we assume the distribution map D is parameterized by a location family 



where the matrix _µ_ ∈ R<sup>_m_×</sup><sup>_d_</sup> is an unknown parameter, and _z_ 0 ∼D0 is a zero-mean random variable.<sup>2</sup> 

As discussed previously, location-scale families encompass many formal examples discussed in prior work. They capture the intuition that in performative settings, the data points are composed of a _base_ component _z_ 0, representing the natural data distribution in the absence of performativity, and an additive performative term. 

In the first stage of our two-stage procedure we build a model of the distribution map D<sup>�</sup> that in effect allows us to draw samples _z_ ∼ D<sup>�</sup> ( _θ_ ) ≈D( _θ_ ). To do this, we perform experiment design to recover the unknown parameter _µ_ which captures the performative effects. In particular, we sample and deploy _n_ classifiers _θi_ , _i_ ∈ [ _n_ ], observe data _zi_ ∼D( _θi_ ), and then construct an estimate � _µ_ of the location map _µ_ using ordinary least squares. We then gather samples from the base distribution D0 by repeatedly deploying the zero classifier. In the location-family model, deploying the zero classifier ensures we observe data points _z_ 0, without performative effects. With both of these components, given any _θ_<sup>′</sup> , we can simulate _z_ ∼ D<sup>�</sup> ( _θ_<sup>′</sup> ) by taking _z_ = _z_ 0 + � _µθ_<sup>′</sup> . 

> 2The variable _z_ 0 being zero-mean is only to simplify the exposition; the same analysis carries over when there is an additional intercept term. Similarly, the choice of Gaussian noise in the experiment design phase of Algorithm 1 is made for convenience. In general, any subgaussian distribution with full rank covariance would suffice. 

10 

In the second stage, we use the estimated model to construct a proxy objective. Define the perturbed performative risk: 



Note that PR( _θ_ ) = E _z_ 0∼D0 _ℓ_ ( _z_ 0 + _µθ_ ; _θ_ ). Using the estimated parameter � _µ_ and samples _zi_ ∼D0, we can construct a finite-sample approximation to the perturbed performative risk and find the following optimizer: 



The main technical result in this section shows that, under appropriate regularity assumptions on the loss, Algorithm 1 efficiently approximates the performative optimum. In particular, when the data dimensionality _m_ is comparable to the model dimensionality _d_ , i.e. _m_ = _O_ ( _d_ ), then computing a ∆-suboptimal classifier requires _O_ ( _d/_ ∆) samples. In contrast, the derivative-free methods considered previously require _O_<sup>�</sup> ( _d_<sup>2</sup> _/_ ∆<sup>2</sup> ) samples to compute a classifier of similar quality. The formal statement and proof of this result is deferred to Appendix C.2. 

Theorem 4.1 (Informal). _Under appropriate smoothness and strong convexity assumptions on the loss ℓ, if the distribution of z_ 0 _is subgaussian, and if the number of samples n_ ⩾ Ω ( _d_ + _m_ + log(1 _/δ_ )) _, then, with probability_ 1 − _δ, Algorithm 1 returns a point θ_<sup>�</sup> _n such that_ 



While we analyze this two-stage procedure in the context of location families, the principles behind the approach can be extended to more general settings. Whenever the distribution map has enough structure to efficiently estimate a model D<sup>�</sup> that supports sampling new data, we can always use the “plug-in” approach above and construct and optimize a perturbed version of the performative risk. 

## 5 Experiments 

We complement our theoretical findings with an empirical evaluation of different methods on two tasks: the strategic classification simulator from [28], and a synthetic linear regression example. 

We pay particular attention to understanding the differences in empirical performance between algorithms which converge to performative optima, such as the two-stage procedure or derivative-free methods from Section 4.1, versus existing optimization algorithms for finding stable points, in particular greedy and lazy SGD due to Mendler-Dünner et al.[22]. In addition, we focus on highlighting the differences in the sample efficiency of the different algorithms and examine their sensitivity to the relevant structural assumptions outlined in Section 3. To evaluate derivative-free methods, we implement the “gradient descent without a gradient” algorithm from [11], which we refer to from here on out as the “DFO algorithm.” For each of the following experiments, we run each algorithm 50 times and display 95% bootstrap confidence intervals. We provide a formal description of all the procedures, as well as a detailed description of the experimental setup in Appendix D. 

11 



<!-- Start of picture text -->
Performative Regression ( ϵ = 0.01) Performative Regression ( ϵ = 100)<br>10 6<br>10 3<br>10 4<br>10 1<br>10 2<br>10 − 1<br>10 0<br>10 − 3 10 − 2<br>0 5000 10000 15000 20000 0 5000 10000 15000 20000<br>Number of Samples Number of Samples<br>Two-Stage Algorithm DFO Greedy SGD Lazy SGD<br>()() θ PR PO − ()() θ PR PO −<br><!-- End of picture text -->

Figure 1: Suboptimality gap versus number of samples collected for the two-stage algorithm, DFO algorithm, greedy SGD, and lazy SGD, for _ε_ = 0 _._ 01 (left) and _ε_ = 100 (right). Each experiment is repeated 50 times, and we display 95% bootstrap confidence intervals. 

Linear regression experiments. We begin by evaluating how increasing the strength of performative effects affects the behavior of the different optimization procedures in settings where the performative risk is convex. We recall the setup from Example 3.2, where the learner attempts to solve a linear regression with performative labels. Given a parameter _θ_ , data are drawn from D( _θ_ ) according to: 



This distribution map is a location family, and is _ε_ -sensitive with _ε_ = ��� _µ_ ���2. Performance is measured according to the squared loss, _ℓ_ (( _x,y_ ); _θ_ ) =<sup><u>1</u></sup> 2<sup>(</sup><sup>_y_−</sup><sup>_θ_⊤</sup><sup>_x_)2.Furthermore, the performative</sup> risk is convex for all choices of _µ_ . 

For small _ε_ , we see that greedy and lazy SGD converge to a stable point that approximately minimizes the performative risk (see left panel in Figure 1). However, as we increase the strength of performative effects, these methods fail to make any progress, and are outperformed by both the DFO algorithm and the two-stage approach by a considerable margin (see right panel in Figure 1). The two-stage procedure efficiently converges after a small number of samples and its behavior is largely unaffected as we increase the value of _ε_ , while the DFO algorithm becomes considerably slower when _ε_ is large. 

Strategic classification simulator. We next consider experiments on the credit scoring simulator from [28], which has been employed as an empirical benchmark for performative prediction in several works [5, 10, 22]. The simulator models a strategic classification problem between a bank and individual agents seeking a loan. The bank deploys a logistic regression classifier _fθ_ to determine the individuals’ default probabilities, while agents strategically manipulate their features to achieve a more favorable classification. 

More specifically, individuals correspond to feature, label pairs ( _x,y_ ) drawn i.i.d. from a base distribution D0. Given a classifier _fθ_ , agents compute a best-response set of features _x_ BR by solving an optimization problem. The bank then observes the manipulated data points 

12 



<!-- Start of picture text -->
Strategic Classification ( ϵ  = 0.0001) Strategic Classification ( ϵ  = 100)<br>0.70<br>0.70<br>0.65<br>0.65<br>0.60<br>0.60 0.55<br>0.50<br>0.55<br>0 200000 600000 1000000 0 20000 60000 100000<br>Number of Samples Number of Samples<br>Two-Stage Algorithm DFO Greedy SGD Lazy SGD<br>Accuracy Accuracy<br><!-- End of picture text -->

Figure 2: Classification accuracy versus number of samples collected for the two-stage algorithm, DFO algorithm, greedy SGD, and lazy SGD, for _ε_ = 0 _._ 0001 ⩽ 2 _<u>γβ</u>_<sup>(left)and</sup><sup>_ε_=100≫</sup> 2 _<u>γβ</u>_<sup>(right).Each</sup> experiment is repeated 50 times, and we display 95% bootstrap confidence intervals. 

( _x_ BR _,y_ ) ∼D( _θ_ ). For an appropriate choice of the agents’ objective function, the distribution map forms a location family, _x_ BR = _x_ + _εθ_ , where _ε_ is a parameter of the agents’ objective. It also serves as a measure of performativity, since this distribution map is _ε_ -sensitive. As a final remark, we add _ℓ_ 2-regularization to the logistic loss to ensure strong convexity. See discussion in [28] and Appendix D for full details. 

Since the logistic loss is not strongly convex in the features, we only have a certificate of convexity when _ε_ is small enough (namely, _ε_ ⩽ 2<sup>_<u>γ</u>_</sup> _β_<sup>).We consider two values of</sup><sup>_ε_:one which is</sup> below this critical threshold, and one large value for which we do not have theoretical guarantees. When _ε_ is small, both the DFO algorithm and the two-stage method yield significantly higher accuracy solutions compared to the two variants of SGD (see left panel of Figure 2). Together with the linear regression experiments, this observation serves as further evidence that stable points have significantly worse performative risk relative to performative optima, even in regimes where _ε < γ/_ (2 _β_ ). Note also that, although both the DFO algorithm and the two-stage algorithm improve upon methods for repeated retraining, the two-stage algorithm converges with significantly fewer samples and significantly lower variance. Indeed, a few thousand samples suffice for convergence of the two-stage method, whereas the DFO algorithm has still not fully converged after a million samples. 

Lastly, on the top right plot, we evaluate these methods for _ε_ ≫ _γ/_ (2 _β_ ) which is outside the regime of our theoretical analysis. Consequently, we have no convergence guarantees for any of the four algorithms. Despite the lack of guarantees and the increased strength of performative effects, we see that the two-stage procedure achieves only a slightly lower accuracy than in the previous setting. On the other hand, as described in our echo chamber analogy, greedy and lazy SGD rapidly converge to a local minimum and do not significantly improve predictive performance after the 10k sample mark. Despite extensive tuning, we were unable to improve the performance of the DFO algorithm and achieve nontrivial accuracy with this method. 

13 

## 6 Discussion and Future Work 

Given the stark difference between performative stability and optimality, the goal of our work is to identify the first set of conditions and algorithmic procedures by which one might be able to provably optimize the performative risk. To this end, we focus on analyzing the problem at a broad level of generality, identifying simple, structural conditions under which the optimization problem becomes tractable. 

However, when applying these ideas in practice, there are a number of important considerations determined by the relevant social context that are not explicitly addressed by our theoretical analysis and which we believe are an important direction for future work. In social settings, such as credit scoring or election forecasts, the choice of loss function must balance predictive accuracy with any externalities that arise from the classifier’s impact on the observed distribution. For example, in lending we may wish to find a classifier _fθ_ that accurately predicts individual defaults, but that also induces a distribution D( _θ_ ) over which the mean probability of default is low (or which satisfies some other socially desirable property). 

In order to balance between predictive accuracy and other concerns about the observed distribution, one possibility is to directly incorporate a penalty on D( _θ_ ). For instance, if we would like D( _θ_ ) to satisfy E _z_ ∼D( _θ_ )[ _z_ ] ≈ _z⋆_ , e.g., to control the mean probability of default, we can modify our loss by including a regularization term of the form ( _z_ − _z⋆_ )<sup>⊤</sup> _Q_ ( _z_ − _z⋆_ ), where _Q_ is some PSD matrix. Importantly, incorporating such a regularization term does not alter the convexity of the performative risk. More formally, given any loss _ℓ_ and distribution map D(·), which satisfy the conditions from Theorem 3.3, and hence for which PR( _θ_ ) = E _z_ ∼D( _θ_ ) _ℓ_ ( _z_ ; _θ_ ) is convex, our analysis proves that the regularized objective, 



is also convex. Furthermore, this phenomenon does not just hold for quadratics, Theorem 3.3 shows that the performative risk remains convex after we incorporate any convex function _f_ ( _z_ ) independent of _θ_ . 

Reasoning about regularizers of this form illustrates another important difference between performatively stable solutions and performative optima. In particular, the set of stable points is the same for both PR( _θ_ ) and its regularized version PR<sup>′</sup> ( _θ_ ) as defined in equation (3), since the regularization term is _independent_ of _θ_ . Therefore, retraining algorithms such as RRM [28] or greedy/lazy SGD [22] essentially ignore any kind of signal provided by these regularizers and converge to the same point on both the regularized and unregularized objective. To find performatively optimal classifiers whose induced distributions satisfy socially desirable criteria, we must directly engage with and anticipate performative effects, rather than just passively retrain. 

Lastly, to date, work on performative prediction has mostly studied the problem from a theoretical perspective. We believe that evaluating the ideas and different design choices raised by these papers in the context of specific applications and case studies on performative prediction would be of high value to the community and an exciting direction for future work. 

## Acknowledgements 

We thank Moritz Hardt and Celestine Mendler-Dünner for many helpful conversations during the course of this project as well as for providing detailed feedback on a draft of this manuscript. 

14 

We would also like to thank the anonymous reviewers whose comments helped improve the quality of our work. 

This research was generously supported in part by the National Science Foundation Graduate Research Fellowship Program under Grant No. DGE 1752814. 

## References 

- [1] Alekh Agarwal and Ofer Dekel. Optimal algorithms for online convex optimization with multi-point bandit feedback. In _Conference on Learning Theory_ , pages 28–40, 2010. 

- [2] Alekh Agarwal, Sham Kakade, and Lin F Yang. Model-based reinforcement learning with a generative model is minimax optimal. In _Conference on Learning Theory_ , pages 67–83, 2020. 

- [3] Yahav Bechavod, Katrina Ligett, Steven Wu, and Juba Ziani. Gaming helps! learning from strategic interactions in natural dynamics. In _International Conference on Artificial Intelligence and Statistics_ , pages 1234–1242, 2021. 

- [4] Peter J Bickel. On adaptive estimation. _The Annals of Statistics_ , pages 647–671, 1982. 

- [5] Gavin Brown, Shlomi Hod, and Iden Kalemaj. Performative prediction in a stateful world. _arXiv preprint arXiv:2011.03885_ , 2020. 

- [6] Yiling Chen, Yang Liu, and Chara Podimata. Learning strategy-aware linear classifiers. In _Advances in Neural Information Processing Systems_ , volume 33, pages 15265–15276, 2020. 

- [7] Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, and Whitney Newey. Double/debiased/Neyman machine learning of treatment effects. _American Economic Review_ , 107(5):261–65, 2017. 

- [8] Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, and James Robins. Double/debiased machine learning for treatment and structural parameters, 2018. 

- [9] Jinshuo Dong, Aaron Roth, Zachary Schutzman, Bo Waggoner, and Zhiwei Steven Wu. Strategic classification from revealed preferences. In _Proceedings of the 2018 ACM Conference on Economics and Computation_ , pages 55–70. ACM, 2018. 

- [10] Dmitriy Drusvyatskiy and Lin Xiao. Stochastic optimization with decision-dependent distributions. _arXiv preprint arXiv:2011.11173_ , 2020. 

- [11] Abraham D Flaxman, Adam Tauman Kalai, and H Brendan McMahan. Online convex optimization in the bandit setting: gradient descent without a gradient. In _Symposium on Discrete Algorithms_ , pages 385–394, 2005. 

- [12] Alex Frankel and Navin Kartik. Improving information from manipulable data. _Journal of the European Economic Association_ , 2021. 

- [13] Nika Haghtalab, Nicole Immorlica, Brendan Lucier, and Jack Z Wang. Maximizing welfare with incentive-aware evaluation mechanisms. In _International Joint Conference on Artificial Intelligence_ , 2020. 

15 

- [14] Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic classification. In _Proceedings of the ACM Conference on Innovations in Theoretical Computer Science_ , pages 111–122, 2016. 

- [15] Lily Hu, Nicole Immorlica, and Jennifer Wortman Vaughan. The disparate effects of strategic manipulation. In _Proceedings of the 2nd ACM Conference on Fairness, Accountability, and Transparency_ , pages 259–268, 2019. 

- [16] Il’dar Abdulovich Ibragimov and Rafail Zalmanovich Has’ Minskii. _Statistical estimation: asymptotic theory_ , volume 16. Springer Science & Business Media, 2013. 

- [17] Niki Kilbertus, Manuel Gomez Rodriguez, Bernhard Schölkopf, Krikamol Muandet, and Isabel Valera. Fair decisions despite imperfect predictions. In _International Conference on Artificial Intelligence and Statistics_ , pages 277–287, 2020. 

- [18] B Ya Levit. On the efficiency of a class of non-parametric estimates. _Theory of Probability & Its Applications_ , 20(4):723–740, 1976. 

- [19] Lester Mackey, Vasilis Syrgkanis, and Ilias Zadik. Orthogonal machine learning: Power and limitations. In _International Conference on Machine Learning_ , pages 3375–3383, 2018. 

- [20] Horia Mania, Stephen Tu, and Benjamin Recht. Certainty equivalence is efficient for linear quadratic control. In _Advances in Neural Information Processing Systems_ , pages 10154–10164, 2019. 

- [21] Nikolai Matni and Stephen Tu. A tutorial on concentration bounds for system identification. In _2019 IEEE 58th Conference on Decision and Control (CDC)_ , pages 3741–3749. IEEE, 2019. 

- [22] Celestine Mendler-Dünner, Juan Perdomo, Tijana Zrnic, and Moritz Hardt. Stochastic optimization for performative prediction. In _Advances in Neural Information Processing Systems_ , volume 33, pages 4929–4939, 2020. 

- [23] Smitha Milli, John Miller, Anca D Dragan, and Moritz Hardt. The social cost of strategic classification. In _Proceedings of the 2nd ACM Conference on Fairness, Accountability, and Transparency_ , pages 230–239, 2019. 

- [24] Alfred Müller and Ludger Rüschendorf. On the optimal stopping values induced by general dependence structures. _Journal of applied probability_ , pages 672–684, 2001. 

- [25] Alfred Müller and Dietrich Stoyan. _Comparison methods for stochastic models and risks_ , volume 389. Wiley, 2002. 

- [26] Evan Munro. Learning to personalize treatments when agents are strategic. _arXiv preprint arXiv:2011.06528_ , 2020. 

- [27] Whitney K Newey. Semiparametric efficiency bounds. _Journal of applied econometrics_ , 5(2):99–135, 1990. 

- [28] Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. Performative prediction. In _International Conference on Machine Learning_ , pages 7599–7609, 2020. 

16 

- [29] Peter M Robinson. Root-n-consistent semiparametric regression. _Econometrica: Journal of the Econometric Society_ , pages 931–954, 1988. 

- [30] Horn Roger and R Johnson Charles. Topics in matrix analysis, 1994. 

- [31] Nir Rosenfeld, Anna Hilgard, Sai Srivatsa Ravindranath, and David C Parkes. From predictions to decisions: Using lookahead regularization. In _Advances in Neural Information Processing Systems_ , volume 33, pages 4115–4126, 2020. 

- [32] Sheldon M Ross, John J Kelly, Roger J Sullivan, William James Perry, Donald Mercer, Ruth M Davis, Thomas Dell Washburn, Earl V Sager, Joseph B Boyce, and Vincent L Bristow. _Stochastic processes_ , volume 2. Wiley New York, 1996. 

- [33] Moshe Shaked and J George Shanthikumar. _Stochastic orders_ . Springer Science & Business Media, 2007. 

- [34] Shai Shalev-Shwartz, Ohad Shamir, Nathan Srebro, and Karthik Sridharan. Learnability, stability and uniform convergence. _The Journal of Machine Learning Research_ , 11:2635–2670, 2010. 

- [35] Ohad Shamir. On the complexity of bandit and derivative-free stochastic convex optimization. In _Conference on Learning Theory_ , pages 3–24, 2013. 

- [36] Yonadav Shavit, Benjamin Edelman, and Brian Axelrod. Causal strategic linear regression. In _International Conference on Machine Learning_ , pages 8676–8686, 2020. 

- [37] Max Simchowitz and Dylan Foster. Naive exploration is optimal for online LQR. In _International Conference on Machine Learning_ , pages 8937–8948, 2020. 

- [38] Herbert A Simon. Dynamic programming under uncertainty with a quadratic criterion function. _Econometrica, Journal of the Econometric Society_ , pages 74–81, 1956. 

- [39] Behzad Tabibian, Vicenç Gomez, Abir De, Bernhard Schölkopf, and Manuel Gomez Rodriguez. On the design of consequential ranking algorithms. In _Conference on Uncertainty in Artificial Intelligence_ , pages 171–180, 2020. 

- [40] Henri Theil. A note on certainty equivalence in dynamic planning. _Econometrica: Journal of the Econometric Society_ , pages 346–349, 1957. 

- [41] Stratis Tsirtsis and Manuel Gomez Rodriguez. Decisions, counterfactual explanations and strategic behavior. In _Advances in Neural Information Processing Systems_ , volume 33, pages 16749–16760, 2020. 

- [42] Roman Vershynin. _High-dimensional probability: An introduction with applications in data science_ , volume 47. Cambridge university press, 2018. 

- [43] Stefan Wager and Kuang Xu. Experimenting in equilibrium. _Management Science_ , 2021. 

- [44] Sean Jeremy Westwood, Solomon Messing, and Yphtach Lelkes. Projecting confidence: How the probabilistic horse race confuses and demobilizes the public. _The Journal of Politics_ , 82(4):1530–1544, 2020. 

17 

## A Background on Stochastic Orders 

In this section we provide the necessary preliminaries from the literature on stochastic orders. First, we recall the notion of the _convex order_ : for two random vectors _z,z_<sup>′</sup> ∈ R<sup>_m_</sup> , we say that _z_ is less than _z_<sup>′</sup> in the convex order, denoted _z_ ⩽ _cx z_<sup>′</sup> , if for all convex functions _g_ : R<sup>_m_</sup> → R, it holds that 



Using a slight abuse of notation, we will also write D1 ⩽ _cx_ D2 for two distributions D1 _,_ D2 when _z_ ∼D1 _,z_<sup>′</sup> ∼D2 and _z_ ⩽ _cx z_<sup>′</sup> . 

Therefore, an immediate way to satisfy condition (A4) is to assume that the loss function _ℓ_ ( _z_ ; _θ_ ) is convex in _z_ , and to require D( _αθ_ +(1− _α_ ) _θ_<sup>′</sup> ) ⩽ _cx α_ D( _θ_ )+(1− _α_ )D( _θ_<sup>′</sup> ). The latter condition has been long studied in classical statistical literature and many equivalent characterizations are known (see, e.g., [25, 32, 33]). This leads to the following corollary of Theorem 3.1. 

Corollary A.1. _Suppose that the loss function is γ-strongly convex in θ_ (A3a) _and β-smooth in z_ (A2) _, and that the distribution map_ D(·) _is ε-sensitive_ (A1) _. Further, assume that ℓ_ ( _z_ ; _θ_ ) _is convex in z and that_ D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) ⩽ _cx α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ) _. Then, the performative risk_ PR( _θ_ ) _is_ ( _γ_ − 2 _εβ_ ) _-convex._ 

Now we discuss important families of distributions that satisfy the convex order condition D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) ⩽ _cx α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ). 

Example A.2. An obvious example where D ( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) ⩽ _cx α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ) is when D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) = _α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ). An important setting which satisfies this linearity property is when the probability of a positive outcome of a binary variable is linear in _θ_ : _zθ_ ∼ Bern( _a_ + _w_<sup>⊤</sup> _θ_ ) defines _zθ_ ∼D( _θ_ ). In this case, D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) = _α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ). 

For further examples, we invoke a convenient characterization of the convex order condition. Lemma A.3 ([24]). _Two random vectors z and z_<sup>′</sup> _satisfy z_ ⩽ _cx z_<sup>′</sup> _if and only if there exists a coupling of z and z_<sup>′</sup> _such that_ E[ _z_<sup>′</sup> | _z_ ] = _z a.s._ 

By applying Lemma A.3, we show that the important case of _location-scale families_ satisfies the convex order condition. Therefore, if the loss function is additionally convex in _z_ , condition (A4) follows. 

Proposition A.4. _Suppose that_ D( _θ_ ) _forms a location-scale family_ (2) _such that_ Σ0 + Σ( _θ_ ) _has full rank for all θ_ ∈ Θ _. Then,_ D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ) ⩽ _cx α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ) _for all θ,θ_<sup>′</sup> ∈ Θ _._ 

_Proof._ We will construct a coupling ( _z,z_<sup>′</sup> ) such that _z_ ∼D( _αθ_ +(1− _α_ ) _θ_<sup>′</sup> ) _,z_<sup>′</sup> ∼ _α_ D( _θ_ )+(1− _α_ )D( _θ_<sup>′</sup> ), and E[ _z_<sup>′</sup> | _z_ ] = _z_ . Let _z_ ∼D( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ); then we define _z_<sup>′</sup> in terms of _z_ as 



where 



18 

is independent of _z_ . Notice that 

- E[ _z_<sup>′</sup> | _z_ ] = E �(Σ0 + Σ( _G_ ))(Σ0 + Σ( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ))<sup>−1</sup> ( _z_ − _µ_ 0 − _µ_ ( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> )) + _µ_ 0 + _µG_ | _z_ � = (Σ0 + E[Σ( _G_ )])(Σ0 + Σ( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> ))<sup>−1</sup> ( _z_ − _µ_ 0 − _µ_ ( _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> )) + _µ_ 0 + E[ _µG_ ] = _z,_ 

which follows by linearity of _µ_ and Σ(·) and the fact that E[ _G_ ] = _αθ_ + (1 − _α_ ) _θ_<sup>′</sup> . 

We now only need to verify that _z_<sup>′</sup> ∼ _α_ D( _θ_ ) + (1 − _α_ )D( _θ_<sup>′</sup> ) in order to apply Lemma A.3 and conclude that _z_<sup>′</sup> ⩽ _cx z_ . Indeed, with probability _α_ we have _G_ = _θ_ , and on that event _z_<sup>′</sup> =<sup>_d_</sup> (Σ0 + Σ( _θ_ )) _z_ 0 + _µ_ 0 + _µθ_ ; a similar argument applies to _θ_<sup>′</sup> . Therefore, putting everything together we conclude that _z_ ⩽ _cx z_<sup>′</sup> . ■ 

Proposition A.4 implies that for all convex functions _g_ : R<sup>_m_</sup> → R, 



We now show that for _strongly_ convex _g_ , this conclusion can be made even stronger. This result allows for deriving a tighter version of Theorem 3.1 for the important class of location-scale families, stated in Theorem 3.3. 

Proposition A.5. _Let g_ : R<sup>_m_</sup> → R _be a γz-strongly convex function for some γz_ ⩾ 0 _, and let_ D( _θ_ ) _form a location-scale family_ (2) _. Then,_ 



_Proof._ Since _g_ is strongly convex, we can write _g_ ( _z_ ) = _g_ 0( _z_ )+<sup>_<u>γ</u>_</sup> 2<sup>_<u>z</u>_∥</sup><sup>_z_∥</sup> 2<sup>2, where</sup><sup>_g_0 is a convex function.</sup> Thus, we want to prove 



By Proposition A.4, we know that 



Therefore, we only need to argue that 



Without loss of generality, we take _z,z_<sup>′</sup> to be coupled as in equation (4). Then, we can write 



19 

where the second steps follows by iterating expectations, because E[ _z_<sup>′</sup> | _z_ ] = _z_ . By further taking an expectation over _G_ , we get: 



■ 

## B Distinguishing between Static and Performative Variables 

In many natural examples, the performative effects are only present in a subset of the variables that make up _z_ . For example, in strategic classification, the performative effects are often only present in the strategically manipulated features, and not in the label. In Example 3.2, on the other hand, the effects are only present in the label. For simplicity of exposition, we suppress this distinction between _performative_ and _static_ variables, that is, those whose distribution does not change for different D( _θ_ ). However, the reader should think of all assumptions on _z_ , such as strong convexity or various Lipschitz assumptions, as only having to apply to the performative variables, while the static ones can be averaged out. To give one example, suppose that _z_ = ( _zs,zp_ ), where _zs_ denotes the static variables and _zp_ denotes the performative ones. Using this distinction, the step in equation (6) would proceed as follows: 



Here, _β_ ( _zs_ ) is the Lipschitz constant of ∇ _θℓ_ (( _zs,_ ·); _θ_ ), and _ε_ ( _zs_ ) is the sensitivity parameter of the distribution of _zp_ , conditional on _zs_ . As clear from the above example, stating all conditions and proofs while emphasizing this distinction is fairly cumbersome, so we opted for a simplified presentation. Similar calculations can be carried out for the rest of the proofs of the structural results. 

## C Deferred Proofs 

### C.1 Convexity of the Performative Risk 

Proof of Theorem 3.1. We begin by writing out the gradient of the performative risk: 



20 

By the first-order condition for convexity, we know that PR( _θ_ ) is ( _γ_ − 2 _εβ_ )-convex if and only if 



for all _θ,θ_<sup>′</sup> ∈ Θ. By assumption (A4), we know that for all _θ,θ_<sup>′</sup> _,θ_ 0 ∈ Θ, 



This assumption is equivalent to saying that _gθ_ 0( _θ_ ) = E _z_ ∼D( _θ_ )[ _ℓ_ ( _z_ ; _θ_ 0)] is a convex function of _θ_ , for all _θ_ 0. We can express this convexity condition using the equivalent first-order characterization: 



Since the mixture dominance condition holds for all _θ,θ_<sup>′</sup> and _θ_ 0, we can set _θ_ 0 equal to _θ_ in the inequality above to conclude that 



Going back to equation (5), we see that a sufficient condition for ( _γ_ − 2 _εβ_ )-convexity of the performative risk is 



By the assumption that the loss is _γ_ -strongly convex in _θ_ , we know 

and thus we have further simplified the sufficient condition to 

Since the loss is _β_ -smooth in _z_ , we have that ∇ _θℓ_ ( _z_ ; _θ_ )<sup>⊤</sup> ( _θ_<sup>′</sup> − _θ_ ) is _β_ ∥ _θ_ − _θ_<sup>′</sup> ∥2-Lipschitz in _z_ . Now, we can use the fact that the distribution map is _ε_ -sensitive to upper bound the left-hand side by applying the Kantorovich-Rubinstein duality theorem: 



Therefore, we can conclude that the performative risk is ( _γ_ − 2 _εβ_ )-convex. 

Proof of Theorem 3.3. Following the steps of Theorem 3.1, we know that PR( _θ_ ) is _λ_ -convex if and only if 



for all _θ,θ_<sup>′</sup> ∈ Θ. 

We now state a technical lemma which rephrases the conclusion of Proposition A.5 in an equivalent way, deferring its proof to the end of this section. 

21 

Lemma C.1. _Suppose that_ 



_Then,_ 



Therefore, by Proposition A.5 and Lemma C.1, we know 



where we take _g_ ( _z_ ) = _ℓ_ ( _z_ ; _θ_ ). 

Thus it suffices to show 



By the assumption that the loss is _γ_ -strongly convex, we know 



With this, we have simplified the sufficient condition for _γ_ -convexity to 



We bound the left-hand side by applying smoothness of the loss together with the KantorovichRubinstein duality theorem; for this, we need a bound on _W_ (D( _θ_ ) _,_ D( _θ_<sup>′</sup> )). We will use the bound implied by _ε_ -sensitivity, as well as the bound implied by the following lemma. 

Lemma C.2. _Suppose that the distribution map_ D( _θ_ ) _forms a location-scale family_ (2) _. Then,_ 



_Proof of Lemma C.2._ By definition, _W_ (D( _θ_ ) _,_ D( _θ_<sup>′</sup> )) = infΠ(D( _θ_ ) _,_ D( _θ_ ′)) E( _zθ,zθ_ ′ )∼Π(D( _θ_ ) _,_ D( _θ_ ′))[∥ _zθ_ − _zθ_ ′ ∥2], where Π(D( _θ_ ) _,_ D( _θ_<sup>′</sup> )) denotes a coupling of D( _θ_ ) and D( _θ_<sup>′</sup> ). The simplest way to couple D( _θ_ ) and D( _θ_<sup>′</sup> ), or equivalently _zθ_ and _zθ_ ′ , is to sample _z_ 0 ∼D, and set _zθ_ = (Σ0 + Σ( _θ_ )) _z_ 0 + _µ_ 0 + _µ_ ( _θ_ ) and _zθ_ ′ = (Σ0 + Σ( _θ_<sup>′</sup> )) _z_ 0 + _µ_ 0 + _µ_ ( _θ_<sup>′</sup> ). With this choice, ∥ _zθ_ − _zθ_ ′ ∥2 = ∥Σ( _θ_ − _θ_<sup>′</sup> ) _z_ 0 + _µ_ ( _θ_ − _θ_<sup>′</sup> )∥2, and hence _W_ (D( _θ_ ) _,_ D( _θ_<sup>′</sup> )) ⩽ E ∥Σ( _θ_ − _θ_<sup>′</sup> ) _z_ 0 + _µ_ ( _θ_ − _θ_<sup>′</sup> )∥2. ■ 

Therefore, the left-hand side in equation (7) can be bounded by 

_z_ ∼DE( _θ_ )<sup>[∇</sup><sup>_θℓ_(</sup><sup>_z_;</sup><sup>_θ_)]⊤(</sup><sup>_θ_′ −</sup><sup>_θ_) −</sup> _z_ ∼DE( _θ_<sup>′</sup> )<sup>[∇</sup><sup>_θℓ_(</sup><sup>_z_;</sup><sup>_θ_)]⊤(</sup><sup>_θ_′ −</sup><sup>_θ_) ⩽</sup><sup>_β_E∥Σ(</sup><sup>_θ_−</sup><sup>_θ_′)</sup><sup>_z_0 +</sup><sup>_µ_(</sup><sup>_θ_−</sup><sup>_θ_′)∥2∥</sup><sup>_θ_′ −</sup><sup>_θ_∥2</sup><sup>_,_</sup> 

22 

but also by applying _ε_ -sensitivity 



Finally, to show _λ_ = max � _γ_ − _β_<sup>2</sup> _/γz, γ_ + _γz_ ( _σ_ min<sup>2(</sup><sup>_µ_) +</sup><sup>_σ_</sup> min<sup>2(Σ)) −2</sup><sup>_βε_</sup> �-convexity it suffices to show both _β_ E ∥Σ( _θ_ − _θ_<sup>′</sup> ) _z_ 0 + _µ_ ( _θ_ − _θ_<sup>′</sup> )∥2∥ _θ_<sup>′</sup> − _θ_ ∥2 ⩽<sup>_<u>β</u>_2</sup><sup>_/γz_</sup> ∥ _θ_ − _θ_<sup>′</sup> ∥<sup>2</sup> 2<sup>+</sup><sup>_<u>γz</u>_</sup> 2<sup>(8)</sup> 2 2<sup>E∥Σ(</sup><sup>_θ_−</sup><sup>_θ_′)</sup><sup>_z_0 +</sup><sup>_µ_(</sup><sup>_θ_−</sup><sup>_θ_′)∥2</sup> 

and 



By the AM-GM inequality, we have 



and so condition (8) follows. 

For condition (9), we observe that 



Applying _σ_ min(Σ)∥ _θ_ − _θ_<sup>′</sup> ∥2 ⩽ ∥Σ<sup>1</sup> _z_ 0<sup>_/_2Σ(</sup><sup>_θ_−</sup><sup>_θ_′)⊤∥</sup> _F_<sup>and</sup><sup>_σ_</sup> min<sup>(</sup><sup>_µ_)∥</sup><sup>_θ_−</sup><sup>_θ_′∥</sup> 2<sup>⩽∥</sup><sup>_µ_(</sup><sup>_θ_−</sup><sup>_θ_′)∥</sup> 2<sup>completes the</sup> proof of the theorem. 

_Proof of Lemma C.1._ The proof follows the standard argument for proving equivalent formulations of strong convexity. 

First we show that E _z_ ∼D( _θ_ )[ _g_ ( _z_ )] −<sup>_<u>γ</u>_</sup> 2<sup>_<u>z</u>_E∥Σ(</sup><sup>_θ_)</sup><sup>_z_0 +</sup><sup>_µθ_∥</sup> 2<sup>2is convex in</sup><sup>_θ_.This follows because:</sup> 



23 

By the equivalent first-order characterization, this means that 





Remark C.3. _We note that the sensitivity parameter ε can be bounded in terms of the location and scale parameters for location-scale families. In particular, in showing condition_ (9) _, we saw that_ 



_If we then denote_ 



_we can see that_ E ∥Σ( _θ_ − _θ_<sup>′</sup> ) _z_ 0 + _µ_ ( _θ_ − _θ_<sup>′</sup> )∥<sup>2</sup> 2<sup>⩽</sup><sup>_σ_2</sup> max<sup>(</sup><sup>_µ_)∥</sup><sup>_θ_−</sup><sup>_θ_′∥2</sup> 2<sup>+</sup><sup>_σ_</sup> max<sup>2(Σ)∥</sup><sup>_θ_−</sup><sup>_θ_′∥2</sup> 2<sup>_.Combining this_</sup> _result with Lemma C.2 and Jensen’s inequality, we get that_ 



_and so ε_ ⩽ _σ_ max<sup>2</sup> ( _µ_ ) + _σ_ max<sup>2</sup> (Σ) _._ � 

### C.2 Two-Stage Algorithm for Location Families 

We carefully review the problem setup and introduce the remaining assumptions. The distribution map D parameterizes a location family 



where _z_ 0 ∼D0. We assume the base distribution D0 is zero-mean and subgaussian with parameter _K_ . The loss function _ℓ_ ( _z_ ; _θ_ ) is _Lz_ -Lipschitz in _z_ , _L_ -Lipschitz and in _θ_ , and _β_ -smooth in ( _z,θ_ ) in the sense that ∇ _ℓ_ ( _z_ ; _θ_ ) ∈ R<sup>_m_+</sup><sup>_d_</sup> is Lipschitz in ( _z,θ_ ). 

We also assume that _λ_ = max{ _γ_ − _β_<sup>2</sup> _/γz,γ_ − 2 _εβ_ + _γzσ_ min<sup>2(</sup><sup>_µ_)}</sup><sup>_>_0,where</sup><sup>_γ_and</sup><sup>_γz_arethe</sup> strong convexity parameters of the loss in _θ_ and _z_ , respectively. By Theorem 3.3, this implies that the performative risk is _λ_ -strongly convex. 

We assume that the performative optimum _θ_ PO is contained in a ball of radius _R_ , so in the second stage we can set the domain of optimization to be Θ = { _θ_ : ∥ _θ_ ∥2 ⩽ _R_ }. Finally, we assume that the minimizer of the perturbed performative risk at the population level, _θ_ � ∈ argmin _θ_ ∈Θ �PR( _θ_ ) is contained in the interior of Θ with probability 1. 

24 

Theorem C.4. _Under the preceding assumptions, if n_ ⩾ Ω ( _d_ + _m_ + log(1 _/δ_ )) _, then, with probability_ 1 − _δ, Algorithm 1 returns a point θ_<sup>�</sup> _n such that_ 



Before proceeding to the proof of this result, we first state four auxiliary lemmas, which constitute the bulk of our analysis. The proofs of the lemmas are included in Appendix C.3. The first lemma is a standard result about ordinary least-squares estimation. 

Lemma C.5. _If n_ ⩾ Ω( _d_ + _m_ + log(1 _/δ_ )) _, then with probability_ 1 − _δ,_ 



The next lemma is a simple adaptation from Theorem 2 in [34] controlling the generalization gap of the empirical risk minimizer for strongly convex losses. 

Lemma C.6. _Suppose_ PR<sup>�</sup> _n is λ_<sup>�</sup> _-strongly convex. Then, with probability at least_ 1 − _δ,_ 



The next lemma controls the difference in gradients between the true performative risk PR and the perturbed performative risk PR.<sup>�</sup> 

Lemma C.7. _For any θ_ ∈ Θ _,_ 



Finally, the last lemma shows that the smoothness assumptions on the loss ensure smoothness of the performative risk. Here, by _βθ_ -smoothness we mean that ∇ _θ_ PR( _θ_ ) is _βθ_ -Lipschitz. 

Lemma C.8. _Under the proceeding assumptions, the performative risk_ PR( _θ_ ) _is βθ_ = _O_ (��� _µ_ ���2) _-smooth._ 

With these lemmas in hand, we are now ready to prove Theorem C.4. 

_Proof of Theorem C.4._ By assumption, the performative risk PR( _θ_ ) is _λ_ -strongly convex, for some _λ >_ 0. This implies 



Since _θ_<sup>�</sup> PO is an interior minimizer of PR<sup>�</sup> , we know ∇PR<sup>�</sup> ( _θ_<sup>�</sup> PO) = 0. Using ∥ _a_ + _b_ ∥<sup>2</sup> ⩽ 2 ∥ _a_ ∥<sup>2</sup> +2 ∥ _b_ ∥<sup>2</sup> , 



25 

We bound each of these terms separately. For the first term, by Lemma C.7, 





For the second term in equation (10), notice that _λ_ = max{ _γ_ − _β_<sup>2</sup> _/γz,γ_ − 2 _εβ_ + _γzσ_ min<sup>2(</sup><sup>_µ_)}</sup><sup>_>_0</sup> implies that PR<sup>�</sup> is at least _λ_<sup>�</sup> = _λ_ − _O_ ( ~~√~~<sup><u>1</u></sup> _n_<sup>)-strongly convex. This follows because |</sup><sup>_σ_min(</sup><sup>_µ_)−</sup><sup>_σ_min(�</sup><sup>_µ_)| ⩽</sup> ∥ _µ_ −� _µ_ ∥ by Weyl’s inequality (see for example Theorem 3.3.16 in [30]), and PR<sup>�</sup> is _O_ (���� _µ_ ���)-sensitive, so by Lemma C.5, each term depending on _ε_ or _σ_ min(� _µ_ ) is within _O_ (1 _/_<sup>√</sup> _n_ ) or _O_ (1 _/n_ ) of the corresponding values for the non-perturbed risk PR. Hence, when _n_ ⩾ Ω(1 _/λ_<sup>2</sup> ), the strong convexity parameter of the perturbed performative risk, _λ_<sup>�</sup> , is at least _λ/_ 2. 

With this, we can apply the fact that _θ_<sup>�</sup> PO is an interior minimizer of PR<sup>�</sup> by assumption to conclude that when _n_ ⩾ Ω(1 _/λ_<sup>2</sup> ), 



Now, when PR<sup>�</sup> is strongly convex, the finite-sample performative risk PR<sup>�</sup> _n_ is also strongly convex because Theorem 3.3 does not depend on the base distribution D0, and PR<sup>�</sup> _n_ is simply PR<sup>�</sup> when the base distribution D0 is replaced with the uniform distribution on { _z_ 1 _,...,zn_ }. Consequently, by Lemma C.6, with probability 1 − _δ_ , 



By Lemma C.8, PR is<sup>�</sup> _O_ (���� _µ_ ���2)-smooth. Applying the previous display then gives us, 



By the triangle inequality and repeated application of ( _a_ + _b_ )<sup>2</sup> ⩽ 2 _a_<sup>2</sup> +2 _b_<sup>2</sup> , ���� _µ_ ���6 ⩽ 128 ���� _µ_ − _µ_ ���6+ 128 ��� _µ_ ���6. Therefore, the above term is _O_ (��� _µ_ ���6 _/δn_ ). Putting everything together with a union bound, we have shown that with probability 1 − _δ_ , if _n_ ⩾ Ω( _d_ + _m_ + log(1 _/δ_ )), it holds that 

as desired. 



26 

### C.3 Proofs of Lemmas for Two-Stage Algorithm Analysis 

The proof of Lemma C.5 is essentially standard (see, e.g., [21]), but we include it for completeness. 

_Proof of Lemma C.5._ Define _Z_ ∈ R<sup>_n_×</sup><sup>_m_</sup> with rows _zi_ and Θ ∈ R<sup>_n_×</sup><sup>_d_</sup> with rows _θi_ , 1 ⩽ _i_ ⩽ _n_ . Then, _Z_ = Θ _µ_<sup>⊤</sup> + _Z_ 0, where _Z_ 0 ∈ R<sup>_n_×</sup><sup>_m_</sup> is a matrix with base samples from D0 as rows. Temporarily assume that Θ<sup>⊤</sup> Θ is invertible; we will later condition on this event. Separately optimizing over each row of _µ_ , we can write the least-squares estimator as 



Consequently, we can bound the estimation error as 



Since _θi_ ∼N (0 _,I_ ), Θ ∈ R<sup>_n_×</sup><sup>_d_</sup> has i.i.d. N (0 _,_ 1) entries, and so Θ<sup>⊤</sup> Θ is a standard Wishart matrix. The standard bound on the minimum eigenvalue of a Wishart matrix (see Theorem 4.6.1 in [42]) gives, with probability 1 − _δ_ , 



Therefore, if _n_ ⩾ Ω( _d_ + log(2 _/δ_ )), then, with probability 1 − _δ/_ 2, 



Control of the second term, ∥Θ<sup>⊤</sup> _Z_ 0∥, also follows from a standard covering argument followed by the Bernstein bound. Write Θ<sup>⊤</sup> _Z_ 0 =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_θi_(</sup><sup>_z_0)⊤</sup> _i_<sup>.Let B</sup><sup>_d_and B</sup><sup>_m_denote the unit</sup> balls in R<sup>_d_</sup> and R<sup>_m_</sup> , respectively. Then, 



Let N _ε_ , and M _ε_ denote _ε_ -coverings of B<sup>_d_</sup> and B<sup>_m_</sup> , respectively. A volumetric bound gives |N _ε_ | ⩽ �1 +<sup><u>2</u></sup> _ε_ � _d_ and similarly |M _ε_ | ⩽ �1 +<sup><u>2</u></sup> _ε_ � _m_ (see Corollary 4.2.13 in [42]). Taking _ε_ = 1 _/_ 4, |N _ε_ | ⩽ 9<sup>_d_</sup> and |M _ε_ | ⩽ 9<sup>_m_</sup> . Approximating the supremum over the _ε_ -nets gives 



Fix _x,y_ ∈N _ε,_ M _ε_ . Since _θi_ ∼N (0 _,I_ ) and ∥ _x_ ∥2 = 1, _x_<sup>⊤</sup> _θi_ ∼N (0 _,_ 1), which has subgaussian norm 1. Similarly, since ( _z_ 0) _i_ is subgaussian with parameter _K_ and ��� _y_ ���2 = 1, the marginal ( _z_ 0)<sup>⊤</sup> _i_<sup>_y_is subgaussian with parameter</sup><sup>_K_.Since</sup><sup>_z_0and</sup><sup>_θ_are independent and zero-mean, the</sup> 

27 

product ( _x_<sup>⊤</sup> _θi_ )(( _z_ 0)<sup>⊤</sup> _i_<sup>_y_) is zero-mean and subexponential with parameter</sup><sup>_K_.Since each term is</sup> subexponential, by the Bernstein bound (see Theorem 2.8.1 in [42]), for any _t >_ 0, 



for some universal constant _c_ . Taking a union bound over the _ε_ -nets, 



If _n_ ⩾ Ω ( _d_ + _m_ + log(2 _/δ_ )), then with probability at least 1 − _δ/_ 2, 



Combining equations (11) and (12) with a union bound, if _n_ ⩾ Ω( _d_ + _m_ + log(1 _/δ_ )), then 





_Proof of Lemma C.7._ Under the location-family parameterization, we can write 



so the gradients are given by 



This representation allows us to write 



Applying the chain rule, together with the triangle-inequality, gives 



We bound each of these terms separately. For the first term, _β_ -smoothness in _z_ immediately gives 



28 

For the second term, adding and subtracting _µ_<sup>⊤</sup> ∇ _zℓ_ ( _z_ 0 + � _µθ_ ; _θ_ ) and then using the triangle inequality, 



where the last line used _β_ -smoothness in _z_ . Combining both pieces, we have 



Using the trivial bound ∥ _θ_ ∥2 ⩽ _R_ , and then squaring both sides, 

_Proof of Lemma C.8._ By applying the location family parameterization as in the proof of Lemma C.7, we get 



Using the chain rule and the triangle inequality, 

For the first term in equation (13), adding and subtracting ∇ _θℓ_ ( _z_ + _µθ_<sup>′</sup> ; _θ_ ) and using the triangle inequality gives 



where we used Jensen’s inequality and the assumption that ∇ _θℓ_ ( _z_ ; _θ_ ) is _β_ -Lipschitz in _z_ (for the first term) and _β_ -Lipschitz in _θ_ (for the second term). 

Now, for the second term in equation (13), similarly adding and subtracting _µ_<sup>⊤</sup> ∇ _zℓ_ ( _z_ + _µθ_<sup>′</sup> ; _θ_ ) and using the triangle inequality gives 



where we used ∇ _zℓ_ ( _z_ ; _θ_ ) is _β_ Lipschitz in _z_ (for the first term) and _β_ Lipschitz in _θ_ (for the second term). This completes the proof. ■ 

29 

## D Experimental Details 

Lastly, we elaborate on the implementation details of the various simulators and algorithms evaluated in Section 5. 

### D.1 Synthetic Linear Regression Example 

Data generating process. Given a parameter vector _θ_ ∈ R<sup>_d_</sup> , as per Example 3.2, feature label pairs ( _x,y_ ) are generated according to the following data generating process: 

1. _x_ ∼N (0 _,_ Σ _x_ ). 

2. _y_ = _β_<sup>⊤</sup> _x_ + _µ_<sup>⊤</sup> _θ_ + _Uy_ where _Uy_ ∼N (0 _,σy_<sup>2).</sup> 

In our experiments, we take _d_ = 20, and set _σy_<sup>2= 0</sup><sup>_._01.For each trial, we sample Σ</sup> _x_<sup>as a random</sup> symmetric positive-definite matrix with operator norm 0 _._ 01, sample _β_ ∼N (0 _,Id_ ), and sample _w_ uniformly on the sphere of radius _ε_ , where _ε_ is the sensitivity parameter of the distribution map. In our experiments, we choose _ε_ ∈{0 _._ 01 _,_ 100}. 

For this example, the performative optimum _θ_ PO can be computed in closed-form due to the squared-loss and the linearity of the performative effects. In particular, 



Algorithms. We compare four different algorithms. In all four cases, we set Θ = { _θ_ : ∥ _θ_ ∥2 ⩽ 10}. 

1. The two-stage procedure. For a budget of _n_ samples, the two-stage procedure consists of first deploying _n/_ 2 classifiers _θi_ ∼N (0 _,Id_ ) and observing data ( _xi,yi_ ). We then compute an estimate � _µ_ by solving a least-squares problem: 



After computing � _µ_ , the algorithm collects another _n/_ 2 samples ( _xi,yi_ ) by repeatedly deploying _θi_ = 0 for _i_ = _n_ + 1 _,...,_ 2 _n_ , and computes _θ_<sup>�</sup> _n_ by solving another least-squares problem 



2. DFO. We run the derivative-free optimization procedure from Flaxman et al. [11]. We initialize _θ_ 0 = 1, use step-size sequence _c_ 0 _/t_ , _c_ 0 = 0 _._ 01, a batch size of 20 samples per-step, and take _δ_ = 10. These parameter were chosen via a small grid search over _c_ 0 ∈ [1 _e_ − 4 _,_ 1], batch size in [1 _,_ 500], and _δ_ ∈ [0 _._ 1 _,_ 100]. However, the algorithm still has variance across runs, especially in the small _ε_ regime. 

3. Greedy SGD. We use the greedy SGD variant introduced by Mendler-Dünner et al. [22] with initial point _θ_ 0 = 1 and step-size sequence 1 _/_ √ _t_ , which we found to slightly outperform the step-sequence 1 _/t_ in our experiments. For the sake of brevity, we omit the full pseudocode of greedy/lazy SGD instead point the reader to Figure 1 in [22]. 

4. Lazy SGD. We use the lazy SGD algorithm [22] with initial point _θ_ 0 = 1, step-size sequence _c/_ ( _k_ 0 + _t_ ) with parameters _c_ = 1 _,k_ 0 = 1, and _k_<sup>2</sup> collected samples in _k_ -th update. 

30 

Evaluation. We ran each algorithm for 50 trials, and in Figure 1, we compare the suboptimality gap PR( _θ_ ) − PR( _θ_ PO) of each algorithm as a function of the number of samples. For each sample size _n_ , we bootstrap 95% confidence intervals over the 50 trials. 

### D.2 Strategic Classification 

Data generation. We use the same strategic classification simulator as [28]. For detailed information about the simulator, please refer to Appendix B.2 of [28]. 

The strategic responses are determined according to 



for some matrix _B_ which determines the subset of features that are performative. Here, _θ_ ∈ R<sup>11</sup> parameterizes a logistic regression classifier. The logistic loss is regularized by an additional _ℓ_ 2-penalty, which makes it strongly convex. The computation of the smoothness parameter can be found in [28]. 

We consider two different values of the sensitivity parameter, _ε_ ∈{0 _._ 0001 _,_ 100}, and set the magnitude of the regularizer to be _λ_ = 0 _._ 002. We restrict the radius of the optimization domain to be 10, Θ = { _θ_ : ∥ _θ_ ∥2 ⩽ 10}. This choice of parameters ensures that _ε_ = 0 _._ 0001 is below the critical threshold 2<sup>_<u>γ</u>_</sup> _β_<sup>, while</sup><sup>_ε_= 100 is above the threshold.</sup> 

Algorithms. We compare the same four algorithms as the previous section. 

1. Two-stage procedure. In the first stage, we deploy random _θi_ ∼N (0 _,I_ ) and perform linear regression to estimate _µ_ , 



Then, having collected samples from the base distribution, we solve the proxy logistic regression objective offline by running gradient descent with a line search procedure until a tolerance criterion is met. In particular, we solve, 



where _ℓ_ ( _z_ ; _θ_ ), is the regularized logistic regression objective, until the improvement between consecutive iterates is smaller than 1e-10. 

2. DFO. We again run the derivative-free optimization procedure from Flaxman et al. [11]. We initialize _θ_ 0 = 0, use step-size sequence 1 _/t_ , a batch size of 100 samples per-step, and set _δ_ = 1. We tried several other parameter configurations and found this one to perform best on this problem setting. 

3. Greedy SGD. We run the greedy SGD variant with initial point _θ_ 0 = 0 and step-size sequence as suggested by [22]. See Appendix A in [22] for details. 

4. Lazy SGD. We use the lazy SGD algorithm with initial point _θ_ 0 = 0 and _k_<sup>2</sup> collected samples in _k_ -th update. As for greedy SGD, we use the step-size sequence suggested by [22]. 

31 

Evaluation. We ran each algorithm for 50 trials, and in Figure 2, we compare the performative risk PR( _θ_ ) of each algorithm as a function of the number of samples. For each sample size _n_ , we bootstrap 95% confidence intervals over the 50 trials. 

32 

