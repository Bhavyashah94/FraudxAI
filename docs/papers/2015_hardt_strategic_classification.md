---
title: "Strategic Classification"
authors: "hardt"
year: 2015
arxiv_id: "1506.06980"
original_file: "1506.06980.pdf"
pdf_path: "docs/papers\2015_hardt_strategic_classification.pdf"
---

# Strategic Classification

**Authors:** Hardt et al.  
**Year:** 2015 | **arXiv:** [`1506.06980`](https://arxiv.org/abs/1506.06980)  
**Local PDF:** [`2015_hardt_strategic_classification.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2015_hardt_strategic_classification.pdf)

---

# Strategic Classification 

### Moritz Hardt 

Nimrod Megiddo 

Christos Papadimitriou 

Mary Wootters 

November 24, 2015 

##### Abstract 

Machine learning relies on the assumption that unseen test instances of a classification problem follow the same distribution as observed training data. However, this principle can break down when machine learning is used to make important decisions about the welfare (employment, education, health) of strategic individuals. Knowing information about the classifier, such individuals may manipulate their attributes in order to obtain a better classification outcome. As a result of this behavior—often referred to as _gaming_ —the performance of the classifier may deteriorate sharply. Indeed, gaming is a well-known obstacle for using machine learning methods in practice; in financial policy-making, the problem is widely known as Goodhart’s law. In this paper, we formalize the problem, and pursue algorithms for learning classifiers that are robust to gaming. 

We model classification as a sequential game between a player named “Jury” and a player named “Contestant.” Jury designs a classifier, and Contestant receives an input to the classifier drawn from a distribution. Before being classified, Contestant may change his input based on Jury’s classifier. However, Contestant incurs a cost for these changes according to a cost function. Jury’s goal is to achieve high classification accuracy with respect to Contestant’s original input and some underlying target classification function, assuming Contestant plays best response. Contestant’s goal is to achieve a favorable classification outcome while taking into account the cost of achieving it. 

For a natural class of _separable_ cost functions, and certain generalizations, we obtain computationally efficient learning algorithms which are near optimal, achieving a classification error that is arbitrarily close to the theoretical minimum. Surprisingly, our algorithms are efficient even on concept classes that are computationally hard to learn. For general cost functions, designing an approximately optimal strategy-proof classifier, for inverse-polynomial approximation, is NP-hard. 

## 1 Introduction 

Studies have found that a student’s success at school is highly correlated with the _number of books in the parents’ household_ [EKST10]. Therefore, in theory, this attribute should be of great value when using machine-learning techniques for student admission. However, this statistical pattern is obviously open to manipulation: books are relatively cheap and, knowing that their number matters, parents can easily buy an attic full of unread books in preparation for admission decisions. 

This behavior is often called _gaming_ : the strategic use of methods that, while not dishonest or against the rules, give the individual an unintended advantage.<sup>1</sup> The problem of gaming is well known and can be seen as a consequence of a classical principle in financial policy making known as _Goodhart’s law_ : 

_“If a measure becomes the public’s goal, it is no longer a good measure.”_ 

Goodhart’s law is highly relevant for the practice of machine learning today. Machine learning relies on the idea that patterns observed in training data translate to accurate predictions about unseen instances of a classification problem. Machine learning is increasingly used to make decisions about individuals in areas such as employment, health, education and commerce. In each such application, an individual may try to achieve a more favorable classification outcome with little effort by exploiting information that may be available about the classifier. Goodhart’s law suggests that if a classifier is exposed to public scrutiny, its prediction accuracy vanishes and it becomes useless. Indeed, concerns of gaming and manipulation are often used as a reason for keeping classification mechanisms secret, which is a major concern in credit scoring (cf. [CP14]). Secrecy is not a robust solution to the problem; information about a classifier may leak, and it is often possible for an outsider to learn such information from classification outcomes. Moreover, transparency is highly desirable and sometimes even mandated by regulation in applications of public interest. 

Our goal in this work is to formalize gaming in classification and to develop approaches and techniques for designing classifiers that are near optimal in the presence of public scrutiny and gaming. The hope is that this analysis may lead, in certain cases, to classifiers with performance comparable to ones that rely on secrecy. In other cases, our analysis may lead to the realization that secrecy is necessary for a good classification performance. 

As gaming entails strategic behavior, any attempt to formalize it must incorporate the strategic response of an individual to a classifier. We propose a general model for _strategic classification_ , based on a sequential two-player game between a party that wishes to learn a classifier and a party that is being classified. This is different from the standard supervisedlearning setup, which is commonly viewed as a one-shot learning process, in which an algorithm produces a classifier from labeled training examples. Our model combines the statistical elements of learning theory—namely, seeking a small generalization error given a finite number of training data—with a game-theoretic notion of equilibrium. This combination allows us to build classifiers that achieve high classification accuracy at equilibrium, when both parties respond strategically to each other. 

Informal description of our model and results. We model learning and classification as a sequential two-player game. The first player, named “Jury," has a learning task: she is given 

> 1See, for instance, `http://www.thefreedictionary.com/gamesmanship` . 

2 

labeled examples from some true classifier _h_ , and must publish a classifier _f_ . The second player, named “Contestant," receives an input to the classifier, and is given a chance to “game" it. That is, Contestant may change his input based on _f_ . However, Contestant incurs a cost for these changes according to a _cost function_ known to both players. Jury’s goal is to achieve high classification accuracy with respect to Contestant’s _original_ input and the true classifier _h_ . Contestant’s goal is to be accepted by Jury, without paying too much to change his input. The cost function plays an important role in our framework as it determines the flexibility of Contestant in changing his input. Ideally, the cost function should capture ground truth or our best approximation thereof. 

Our contributions are the following: 

- For certain cost functions, we give an efficient strategy for Jury which approaches the optimal payoff. Surprisingly, this result holds even for concept classes which are computationally intractable to learn. The intuitive reason is that Contestant’s changes to his input “smooth out” any intractability. 

- Those cost functions for which Jury has near-optimal algorithms include _separable cost functions_ . This is a natural class of cost functions which generalize our introductory example of school admissions and books. We also obtain results for a broad generalization of these separable functions. 

– In contrast, we show that, for general cost functions—even for cost functions which are metrics, another nice class—it is hard to approximate the optimum classification score with reasonable accuracy. 

- We observe through experiments on real data that our approach leads to higher classification accuracy compared with standard classifiers in situations where even a small amount of gaming occurs. We also experimentally demonstrate the robustness of our framework to inaccuracies in our modeling assumptions and the modeling of the cost function. 

### 1.1 Our model 

We first describe an idealized version of the game, where Jury has perfect information. This will serve as a reference point for how well Jury may hope to do. We will later relax this to a version where Jury knows neither _h_ nor D, and only sees labeled examples. 

Definition 1.1 (Full information game). The players are Jury and Contestant. Fix a _population X_ , and a probability distribution D over _X_ . Fix a _cost function c_ : _X_ × _X_ → R+ and a _target_ classifier _h_ : _X_ →{−1 _,_ 1}. 

1. Jury (who knows the cost function _c_ , the distribution D, and the true classifier _h_ ) publishes a classifier _f_ : _X_ →{−1 _,_ 1}. 

2. Contestant (who knows _c,h,_ D, and _f_ ), produces a function ∆ : _X_ → _X_ . 

The payoff to Jury is Pr _x_ ∼D { _h_ ( _x_ ) = _f_ (∆( _x_ ))}. The payoff to Contestant is E _x_ ∼D [ _f_ (∆( _x_ )) − _c_ ( _x,_ ∆( _x_ ))]. 

Definition 1.1 is an example of a _Stackelberg competition_ , which means that the first player (Jury) has the ability to commit to her strategy (a classifier _f_ ) before the second player (Contestant) responds. We wish to find a _Stackelberg equilibrium_ , that is, a highest-payoff strategy 

3 

for Jury, assuming best response of Contestant; equivalently, a perfect equilibrium in the corresponding strategic-form game. 

Notice that designing the optimum _f_ , given _h_ , D and _c_ , for a finite _X_ , is a conventional combinatorial optimization problem. We seek to label the points in _X_ with ±1 so that the expectation, over D, of _h_ ( _x_ ) · _f_ (∆( _x_ )) is maximized. Here, ∆( _x_ ) is a best move of Contestant, that is, 



We note that ∆( _x_ ) may not be well-defined, if there are multiple _y_ which attain the maximum. In the following, we assume that Contestant may move to any of them; for simplicity, we do assume that if one of the maximum-attaining _y_ is _x_ itself, then ∆( _x_ ) = _x_ . That is, if Contestant is indifferent between moving and not moving, he will default to not moving. We refer to the best payoff for Jury in the above full-information game at the “strategic maximum" of the game: 

Definition 1.2 (Strategic Maximum). The _strategic maximum_ in the full-information game is defined as 



where ∆( _x_ ) is defined as in (1). Notice that ∆( _x_ ) depends on _f_ . 

Remark 1.3. _For intuition, notice that if c_ ( _x,x_ ) = 0 _(that is, it costs nothing for Contestant to stay where he is), then_ ∆( _x_ ) _has the following characterization:_ 

_– if f_ ( _x_ ) = 1 _, then_ ∆( _x_ ) = _x;_ 

_– if f_ ( _x_ ) = −1 _, let y_ = argmin _y_ ∈ _X_ : _f_ ( _y_ )=1 _c_ ( _x,y_ ) _; then_ 



_Indeed, since Contestant is best-responding, he only makes a move from input x to point y if c_ ( _x,y_ ) _is strictly less than_ 2 _, which is the payoff he obtains by improving his outcome from “rejected" to “accepted." In this case, the quantity f_ (∆( _x_ )) _in the definition of the strategic maximum becomes_ 



In Section 4 we show that, for general cost functions, the strategic maximum is NP-hard to approximate. However, we will also show that for a natural class of cost functions, it is possible to to design a classifier for which Jury’s payoff is arbitrarily close to the strategic maximum, even when Jury has _incomplete_ information. To formalize this, we introduce a second game, which we call the _statistical classification game._ In this game, Jury does not know the target classifier _h_ for every point in _X_ , but instead is given a few labeled examples from an unknown distribution D. Contestant best-responds to Jury’s published classifier _f_ . 

Definition 1.4 (Statistical Classification Game). The players are Jury and Contestant. Fix a _population X_ and a probability distribution D over _X_ . Fix a _cost function c_ : _X_ × _X_ → R+ and a target classifier _h_ : _X_ →{−1 _,_ 1}. 

4 

1. Jury (who knows only the cost function _c_ ) can request labeled examples of the form ( _x,h_ ( _x_ )), with _x_ being drawn from D. She publishes a classifier _f_ : _X_ →{−1 _,_ 1}. 

2. Contestant (who knows _c_ and _f_ ), produces a function ∆ : _X_ → _X_ . 

The payoff to Jury is Pr _x_ ∼D { _h_ ( _x_ ) = _f_ (∆( _x_ ))}. The payoff to Contestant is E _x_ ∼D[ _f_ (∆( _x_ ))− _c_ ( _x,_ ∆( _x_ ))]. 

### 1.2 Strategy-robust learning 

A learning algorithm in our setting has to accomplish two goals. First, it needs to learn the unknown target classifier from labeled examples. Second, it needs to achieve high payoff for Jury in the statistical classification game, by anticipating Contestant’s best response. Below, we give two definitions of stategy-robust learning which combine these goals; the second is a stronger requirement than the first. In our first definition, we fix an unknown target classifier _h_ , and demand an algorithm which, with high probability over the samples, returns a classifier _f_ guaranteeing a near-optimal payoff to Jury in the statistical classification game. In our second definition, we present a uniform notion: the learning algorithm must, with high probability, return a classifier that is guaranteed to work on _any_ target classifier _h_ in some concept class H. 

Definition 1.5 (Strategy-robust learning). Let C be a class of cost functions. We say that an algorithm A is a _strategy-robust_ learning algorithm for C if the condition that follows holds. For all distributions D, for all classifiers _h_ , all _c_ ∈C and for all _ε_ and _δ_ , given a description of _c_ and access to labeled examples of the form ( _x,h_ ( _x_ )), where _x_ ∼D, A produces a classifier _f_ : _X_ →{−1 _,_ 1} so that, with probability at least 1 − _δ_ over the samples, 



where ∆( _x_ ) is defined as in (1). 

One might expect, in line with PAC-learning [Val84], that Definition 1.5 might restrict _h_ to be in some concept class H. However, we will show that for a natural class C of cost functions, in fact it is possible to achieve strategy-robust learning with no dependence on _h_ ! 

However, we may want to ask a bit more. Suppose that Jury builds a classifier for some property, and later wants to re-use the data to build a classifier for a slightly different property. For example, returning to the scenario from the introduction, suppose that the school admissions board collects data on students and tries to predict academic success. Later, the board is charged with recruiting to maximize the quality of the basketball team; they would like to use the same dataset to predict who will be a good student-athlete. Later still, suppose that the this data set is made public, and many other schools try to use it to predict many things. If enough different classifiers are trained on this data, the guarantee of Definition 1.5 starts to degrade. A strategy-robust learning algorithm should succeed with high probability on a single classifier, but there are no guarantees (beyond what the union bound gives) if it is used repeatedly. This situation motivates the following definition. 

Definition 1.6 (Uniform strategy-robust learning). Let H be a concept class and C be a class of cost functions. We say that an algorithm A is a _uniform strategy-robust_ learning algorithm for (H _,_ C) if the condition that follows holds. For all distributions D, for all _c_ ∈C and for all _ε_ and _δ_ , with probability at least 1− _δ_ over draws _x_ ∼D, the following holds simultaneously for all _h_ ∈H. 

5 

Given a description of _c_ and access to labels ( _x,h_ ( _x_ )), A produces a classifier _f_ : _X_ →{−1 _,_ 1} so that 



where ∆( _x_ ) is defined as in (1). 

We will typically specify the number of labeled examples that the algorithm requires as a function of _ε_ , _δ_ and a parameter that depends on the domain size (e.g., the number of features). 

### 1.3 Our contributions 

Our main result is a strategy-robust learning algorithm, which comes with both uniform and non-uniform guarantees. Our algorithm is computationally efficient when the cost function comes from a broad class of functions that we call _separable_ . In the non-uniform case, the target classifier _h_ can be anything. In the uniform case, the algorithm is efficient as long as the concept class H is statistically learnable, but it notably does not require that H be efficiently learnable. 

Separable cost functions are functions of the form _c_ ( _x,y_ ) = max{0 _,c_ 2( _y_ ) − _c_ 1( _x_ )}, where _c_ 1 and _c_ 2 are arbitrary functions, mapping the domain _X_ into the real numbers. We take the maximum with 0 to obtain a nonnegative cost function. We will later see and discuss a number of natural examples of separable cost functions. 

Our main theorem, and our stronger result, is about uniform strategy-robust learning. 

Theorem 1.7 (Informal). _Let_ H _be a concept class that is learnable from m examples up to error ε and confidence_ 1 − _δ, and let_ S _be the class of separable cost functions. Then, there is a uniform strategyrobust learning algorithm for_ (H _,_ S) _with running time and sample complexity_ poly( _m,_ 1 _/ε,_ log(1 _/δ_ )) _._ 

In fact, (the formal statement of) this theorem implies a non-uniform result: 

Theorem 1.8 (Informal). _Let_ S _be the class of separable cost functions. There is a non-uniform strategy-robust learning algorithm for_ S _with polynomial running time and sample complexity._ 

Our main theorem (and the non-uniform corollary) can be extended to a more general class of cost functions, which are obtained by taking the minimum of _k_ separable cost functions. We state only the uniform version here, the non-uniform version follows similarly. 

Theorem 1.9 (Informal). _Let_ H _be a concept class that is learnable from m examples up to error ε and confidence_ 1 − _δ, and let_ S<sup>(</sup><sup>_k_)</sup> _be the class of minima of k separable cost functions. Then, there is a uniform strategy-robust learning algorithm for_ (H _,_ S<sup>(</sup><sup>_k_)</sup> ) _with sample complexity_ poly( _m,k,_ 1 _/ε,_ log(1 _/δ_ )) _and running time_ poly( _m,_ exp( _k_ ) _,_ 1 _/ε,_ log(1 _/δ_ )) _._ 

Theorem 1.9 applies to a broad class of cost functions: it is not hard to see that any cost function on a finite domain _X_ can be written as a minimum of separable cost functions. Of course, the sample complexity in Theorem 1.9 depends on _k_ , the number of cost functions involved. For general cost functions, _k_ grows with | _X_ | and might be quite large. However, many spaces admit a more efficient representation—for instance, if the cost function defines a metric that admits a small _ε_ -net, _k_ depends only on the size of the net. Thus, _k_ is a parameter that interpolates nicely between tractable cases where _k_ is small and the general case where _k_ is unrestricted. 

The fact that the sample complexity in Theorem 1.9 might be large is unavoidable: for general cost functions, we have the following negative result. 

6 

Theorem 1.10 (Informal). _There is a class of metrics_ S _such that, unless P = NP, there is no efficient strategy-robust learning algorithm for_ S _that achieves expected payoff within ε_ = 1 _/_ | _X_ |<sup>_η_</sup> _of the optimum, for any constant η >_ 0 _._ 

Recall that a distance function is a _metric_ if it is non-negative, symmetric, and satisfies the triangle inequality. This result is an immediate corollary of the fact (which we will prove in Section 4) that approximating the strategic maximum for metrics is NP-complete. 

#### 1.3.1 Experimental evaluation 

We experimentally evaluate our framework on real data from a Brazilian social network called Apontador. The data set deals with instances of review spam and was recently studied in the context of spam fighting [CdCMBB14]. Classification of spammers is a natural setting for our methods, because spammers will of course try to game any automated attempt to identify them. We model a cost function that roughly reflects the loss in revenue that a spammer experiences when changing certain attributes. For instance, when a spam message contains a URL pointing to malware, it is costly for the spammer to remove this URL from his message as his message loses its intended purpose. Acknowledging that the modeling of a cost function can never be perfectly realistic, we evaluate our approach while explicitly taking into account several types of modeling inaccuracies. Specifically, we only assume that our cost function is roughly correct and that the amount of gaming is possibly below or above the threshold predicted by our theoretical framework. Our empirical observations demonstrate that even in the presence of significant modeling errors and only a small amount of gaming, our algorithm already outperforms a standard SVM classifier. Complementing our robustness analysis, we explore an approach for creating hybrid classifiers that interpolate between our classifier and standard classifiers that aren’t by themselves strategy-robust. We observe that such hybrids often achieve an excellent trade-off between resilience to gaming and classification accuracy. 

### 1.4 Related work 

The deterioration of prediction accuracy due to unforeseen events is often described as _concept drift_ and arises in a number of contexts. A sequence of works on _adversarial learning_ is motivated by the question of learning in the presence of an adversary that tampers with the examples of a learning algorithm. Typical application examples in this line of work include intrusion detection and spam fighting. Early works considered zero-sum games [DDM<sup>+</sup> 04] which are not very applicable to our problem as there are almost always cases where the payoff should be high for both players (e.g, a good student being admitted to a good college). More recent work considers alternative game-theoretic notions [BS09, BS11, BKS12, GSBS13]. The most closely related is the work by Brückner and Scheffer [BS11], which considered a Stackelberg competition for adversarial learning. A notable difference with our setup is that they define the equilibrium with respect to the sample, while we define it with respect to the underlying distribution. Our definition requires us to provide generalization bounds. Beyond this difference, Brückner and Scheffer focus on learning centered linear classifiers when the Euclidean squared norm is the cost function. The Euclidean norm is not separable and so our results are incomparable. Stackelberg competitions have also been studied extensively in the context of security games [KYK<sup>+</sup> 11, KCP10]. 

7 

## 2 Separable cost functions 

We begin by studying the class of _separable_ cost functions, which arise naturally in the context of gaming. To motivate the definition, recall the example of the school board which wants to exploit the correlation between parents’ books and students’ performance. In this (admittedly rather stylized) example, the cost to Contestant from moving from a household _x_ ∈ _X_ with 50 books to a household _y_ ∈ _X_ with 100 books is simply the cost of the the additional books. 

More generally, this logic applies to any situation where Contestant can assign a cost to each state _x_ ∈ _X_ , independently of how it was reached. If the cost of a state _x_ is _g_ ( _x_ ), then the cost to Contestant of moving from _x_ to _y_ is simply any additional cost: _c_ ( _x,y_ ) = max {0 _,g_ ( _y_ ) − _g_ ( _x_ )}. For example, suppose that Jury is designing a spam filter, and Contestant wishes to send an email. Independently of the spam filter, Contestant wants his message to serve a purpose such as advertising or distributing malware. We can assign a score _g_ ( _x_ ) to each message in _x_ ∈ _X_ that expresses how much utility the spammer experiences when this message is delivered without being classified as spam. For example, a message is significantly less useful for the spammer after the URL pointing to malware has been removed. The expression max{0 _,g_ ( _y_ ) − _g_ ( _x_ )} then captures the loss in utility (or expected revenue) when moving from _x_ to _y._ We will return to this example in detail in our experimental evaluation in Section 5. 

With these examples in mind, we define a _separable_ cost function as follows. 

Definition 2.1. A cost function _c_ ( _x,y_ ) is called separable if it can be written as 



for functions _c_ 1 _,c_ 2 : _X_ → R satsifying _c_ 1( _X_ ) ⊂ _c_ 2( _X_ ). 

Above, the term “separable" is a slight abuse of terminology, because the cost function cannot be negative, and because of the assumption about _c_ 1( _X_ ) ⊂ _c_ 2( _X_ ); a truly “separable" function would be of the form _c_ 2( _y_ ) − _c_ 1( _x_ ), for arbitrary _c_ 1 _,c_ 2. However, we will stick with it for simplicity of exposition. The two extra conditions are natural for cost functions. The maximum with 0 ensures that the cost function is non-negative. The condition _c_ 1( _X_ ) ⊂ _c_ 2( _X_ ) means that there is always a 0-cost option (that is, Contestant can opt not to game, and can pay nothing). 

Another important special case of a separable cost functions are linear cost functions of the form 



for _α_ ∈ R<sup>_n_</sup> . With this cost function, each attribute can be increased independently at some linear cost, and can be decreased for free. For our arguments that follow, a linear cost function is helpful for intuition. 

Our main result is that for separable cost functions, there is a nearly optimal algorithm for Jury, with a uniform guarantee. The sample complexity and running time of this algorithm depend on the Rademacher complexity of the class H of classifiers. 

Definition 2.2. For a class F of functions _f_ : _X_ → R, the Rademacher complexity of F with sample size _m_ is defined as 



where _σ_ 1 _,...,σm_ are i.i.d. Rademacher random variables. 

8 

Our algorithm, given below as Algorithm 1, has the following uniform guarantee. 

Theorem 2.3. _Suppose the cost function c is separable, i.e., c_ ( _x,y_ ) = max{0 _,c_ 2( _y_ ) − _c_ 1( _x_ )} _and c_ 1( _X_ ) ⊆ _c_ 2( _X_ ) _. Let_ H _be a concept class, and let_ D _be a distribution. Let m denote the number of samples in Algorithm 1, and suppose_ 



_Under these conditions, with probability at least_ 1 − _δ,_ (3) _holds for all h_ ∈H _._ 

Notice that Theorem 2.3 indeed implies the “informal" version, Theorem 1.7. That is, if H is statistically learnable (i.e., _Rm_ (H) decays inversely polynomially with _m_ for all distributions D, or sufficiently that the VC dimension of H is bounded<sup>2</sup> ), then Algorithm 1 is a efficient, uniform strategy-robust learning algorithm for H. 

It is worth pointing out that Algorithm 1 is _computationally_ efficient as long as H has low sample complexity—even if H itself is not computationally efficiently learnable! As we mentioned above, the proof of Theorem 2.3 also implies that our algorithm satisfies the following non-uniform guarantee. 

Corollary 2.4. _Suppose the cost function c is separable. Let m denote the number of samples in Algorithm 1, and suppose that_ 



_Then with probability at least_ 1 − _δ,_ (3) _holds for all distributions_ D _. In particular, Algorithm 1 is an efficient (non-uniform) strategy-robust learning algorithm._ 

Corollary 2.4 follows from Theorem 2.3 by setting H = { _h_ }, the singleton containing the fixed target classifier _h_ . Indeed, in this case _Rm_ (H) = 0. 

Before proving Theorem 2.3, we state the algorithm and discuss the intuition behind it. In Figure 1, we illustrate the idea for a linear cost function, _c_ ( _x,y_ ) =<sup>�</sup> _α,y_ − _x_<sup>�</sup> +<sup>.Because moving</sup> perpendicularly to _α_ is free for Contestant, Jury may as well choose a classifier _f_ that accepts some affine halfspace whose normal is equal to _α_ (see Figure 1). Thus, the only issue is finding the correct shift for this halfspace. Because the calculated shift can only be based on samples, we choose the shift that is empirically the best. The latter can be calculated quickly because it is a one-dimensional problem. 

For a more general separable cost function 



by the same argument, Jury may as well return a classifier _c_ 2[ _t_ ] of the form: 



for some _t_ . Algorithm 1 gives the details, and we proceed with the proof below. 

2Indeed, if _d_ is the VC dimension of H, we have 



for all distributions D (notice that _Rm_ (H) depends on D). 

9 



<!-- Start of picture text -->
f ′<br>f<br>x ′ y<br>α x<br><!-- End of picture text -->

Figure 1: Suppose the optimal classifier for Jury is _f_ (which accepts the dark gray region), and the cost function is _c_ ( _x,y_ ) =<sup>�</sup> _α,y_ − _x_<sup>�</sup> +<sup>.Because moving perpendicular to</sup><sup>_α_is free for Contestant, then the payoff</sup> for Jury if she plays _f_<sup>′</sup> (shown above, which accepts the light gray region) is the same as her payoff if she plays _f_ . Indeed, suppose that the agent _x_ shown above would be willing to move to _y_ to get accepted by _f_ . Then _x_<sup>′</sup> would also be willing to move to _y_ , because the cost is the same. Thus, Jury may restrict his or her search to classifiers _f_<sup>′</sup> that accept all points in some affine halfspace whose normal is equal to _α_ . 

Algorithm 1: A: <u>gaming-robust classification algorithm for separable cost functions</u> 

- 1 Inputs: Labeled examples ( _x_ 1 _,h_ ( _x_ 1)) _,...,_ ( _xm,h_ ( _xm_ )) from _xi_ ∼D i.i.d.. Also, a description of a separable cost function _c_ ( _x,y_ ) = max{0 _,c_ 2( _y_ ) − _c_ 1( _x_ )}. 

- 2 For _i_ = 1 _,...,m_ , let 



For convenience, set _sm_ +1 = ∞. 3 Compute 



4 Find _i_<sup>∗</sup> , 1 ⩽ _i_<sup>∗</sup> ⩽ _m_ + 1, that minimizes err(� _si_ ). 5 Return: _f_ := _c_ 2[ _si_ ∗]. 

10 

Remark 2.5 (Input to Algorithm 1). Algorithm 1 takes a cost function _c_ ( _x,y_ ) = max{0 _,c_ 2( _y_ ) − _c_ 1( _x_ )} as an input, and it returns some threshold function based on _c_ 2. We have been a little sloppy about how exactly _c_ should be represented. A quick inspection of the algorithm shows that in order to compute the threshold, A needs only black-box access to _c_ 1, and enough access to _c_ 2 to determine _c_ 2( _X_ ) ∩ [ _ti,ti_ + 2]. In order to return the classifier _f_ , A additionally needs whatever access to _c_ 2 it is expected to return. For example, if we only ask that A be able to provide black-box access to _f_ , then black-box access to _c_ 2 suffices for this step. If we ask that A return a short description of _f_ , then a short description of _c_ 2 suffices for this step. 

_Proof of Theorem 2.3._ Assume for simplicity that the cost function satisfies _c_ ( _x,y_ ) � 2, for all _x,y_ ∈ _X_ . First, for any mapping _f_ : _X_ →{−1 _,_ 1}, define 



Claim 2.6. Γ ( _f_ ) _is the set of x_ ∈ _X such that f_ (∆( _x_ )) = 1 _when_ ∆ _is a best response of Contestant._ 

_Proof._ Indeed, for _x_ ∈ Γ ( _f_ ), there exists some _y_ such that _f_ ( _y_ ) = 1, so that the payoff to Contestant when he plays ∆( _x_ ) = _y_ is equal to 1 − _c_ ( _x,y_ ) _>_ −1. On the other hand, suppose that Contestant plays ∆( _z_ ) ∈ _X_ for some with _f_ ( _z_ ) � 1. Then the best payoff of Contestant is equal to −1 − _c_ ( _x,z_ ) ⩽ −1, because _c_ ( _x,z_ ) ⩾ 0. So, the best response of Contestant is to choose ∆( _x_ ) = _y_ for some _y_ with _f_ ( _y_ ) = 1. This establishes that Γ ( _f_ ) ⊆{ _x_ ∈ _X_ : _f_ (∆( _x_ )) = 1}. 

For the other direction, suppose that _f_ (∆( _x_ )) = 1. Then there is some _y_ ∈ _X_ so that 



using from the definition of separability that _c_ 1( _X_ ) ⊆ _c_ 2( _X_ ), and hence for all _x_ , 



In particular, _c_ ( _x,y_ ) _<_ 2, and so _x_ ∈ Γ ( _x_ ). This establishes that 



and proves the claim. ■ 

Claim 2.6 is the only place in the proof where we need either of the extra conditions in Definition 2.1 (that _c_ ( _x,y_ ) ⩾ 0 and _c_ 1( _X_ ) ⊆ _c_ 2( _X_ )). 

Given this characterization of Γ ( _f_ ), we next argue that we may replace _f_ by a much more structured function _f_<sup>′</sup> so that Γ ( _f_ ) = Γ ( _f_<sup>′</sup> ); in particular, the payoff to Jury under _f_ will be the same as under _f_<sup>′</sup> , and so we can restrict our attention to these more structured functions. For any _f_ , let 



Then we have 

11 



In particular, for any true classifier _h_ ∈H, the payoff to Jury if she plays _f_ is the same as if she plays _f_<sup>′</sup> : 



Above, △ denotes symmetric difference. Thus, it suffices to consider classifiers of the form of (4). That is, our classifier may as well be equal to _c_ 2[ _s_ ], for some _s_ ∈ _c_ 2( _X_ ) ∪{∞}, where _s_ plays the role of min{ _c_ 2( _z_ ) : _f_ ( _z_ ) = 1 }, and _s_ = ∞ means that there is no _z_ such that _f_ ( _z_ ) = 1. Let 



be the set of these relevant values of _s_ . Recall the definition of _si_ from Algorithm 1. For _s_ ∈ _S_ , we have<sup>3</sup> 



The best possible payoff to Jury is obtained by finding the best threshold _s_ , i.e., 



where err( _s_ ) := P { _h_ ( _x_ ) � _c_ 1[ _s_ − 2]( _x_ )} _._ In Algorithm 1, Jury returns _f_ = _c_ 2[ _si_ ∗], and as above the payoff to Jury from this _f_ is equal to 



Thus, to prove Theorem 2.3, it suffices to show that for all _h_ ∈H, 



To establish this, we first observe that there is no loss of generality in Algorithm 1 by considering only the _si_ , _i_ = 1 _,...,m_ + 1, where as in Algorithm 1 we set _sm_ +1 = ∞. 

Claim 2.7. 



_Proof._ The first equality is just the definition of _i_<sup>∗</sup> . The second equality follows from the fact that 



only changes when _c_ 1[ _s_ − 2]( _xj_ ) changes for some _j_ . Thus, by construction, this sum takes on every possible value (as _s_ ranges over _S_ = _c_ 2( _X_ ) ∩{∞}) at the points _si_ , _i_ = 1 _,...,m_ + 1. ■ 

> 3 As usual, ∞− 2 = ∞. 

12 

Claim 2.8. _With probability at least_ 1 − _δ, for all h_ ∈H _and for all s_ ∈ _S,_ 



_In particular, under the conditions of Theorem 2.3, with probability at least_ 1 − _δ,_ 

sup {|err(� _s_ ) − err( _s_ ) | : _h_ ∈H _, s_ ∈ _S_ } ⩽ _ε/_ 2 _._ 

_Proof._ Writing out the definition of err� and err, we need to bound the absolute value of the difference 



simultaneously for all _h_ ∈H, _s_ ∈ _S_ . By standard arguments (see, for example, Theorem 3.2 in [BBL05]), for all _h_ ∈C _,s_ ∈ _S_ , 



where 



Thus, it suffices to control the Rademacher complexity of X , which is in turn controlled by 



where Y = { _c_ 1[ _s_ − 2] : _s_ ∈ _S_ }. Note that, because all the functions in H ∪Y are ±1-valued, 



for every _x_ . Inequality (7) follows from a contraction principle (see, e.g., Theorem 4.2 in [LT91]) and the definition of the Rademacher complexity. 

It remains to bound _Rm_ (Y ). Fix _x_ 1 _,...,xm_ ∈ _X_ and sign flips _σi_ ∈{−1 _,_ 1}. As in the proof of Claim 2.7, all of the values that<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_σic_1[</sup><sup>_s_−2](</sup><sup>_xi_) takes on as</sup><sup>_s_ranges over</sup><sup>_S_are attained at</sup> { _s_ 1 _,...,sm_ +1}. Thus, for fixed _x_ 1 _,...,xm_ ∈ _X_ , using a Chernoff bound and the union bound, and integrating to bound the expectation, we obtain 



Thus, we have 



and altogether inequality (6) implies that for all _h_ ∈H and _s_ ∈ _S_ , 



which completes the proof of the claim. 



13 

Claims 2.7 and 2.8 establish Theorem 2.3. Indeed, we have, with probability at least 1 − _δ_ , for all _h_ ∈C, 



establishing inequality (5) and completing the proof. 

## 3 General cost functions 

While separable cost functions are quite reasonable, they do not capture everything. In this section, we consider more general cost functions. We extend Algorithm 1 to work for a cost function that is the minimum of an arbitrary set of separable cost functions. This is a much broader class. In fact, _every_ cost function can be represented as the minimum of separable cost functions, although not necessarily very parsimoniously. 

Proposition 3.1. _Let X be any finite set and let c_ : _X_ × _X_ → R _be any mapping. Suppose_ 



_Under these conditions,_ 



Since each of the cost functions _cw,z_ ( _x,y_ ) = _c_ ( _w,z_ ) + _D_ · 1 { _x_ � _w_ } + _D_ · 1 { _y_ � _z_ } is a separable cost function, Proposition 3.1 implies that any _c_ can be written as the minimum of | _X_ |<sup>2</sup> cost functions. The sample complexity of our extension depends on the number of cost functions; since | _X_ | may be quite large (possibly exponential in the parameter of interest), Proposition 3.1 might not help. However, a smaller number of cost functions can be used if _X_ has nice geometric structure. 

Proposition 3.2. _Let X be any finite set and let c_ : _X_ × _X_ → R _be a metric. Let S be an ε-net of X: that is, for every x_ ∈ _X, there is some s_ ∈ _S so that c_ ( _x,s_ ) ⩽ _ε. Under these conditions, for every x,y_ ∈ _X,_ 



Thus, when _c_ is a metric, our problem is very close to a problem where the cost function is the minimum of separable cost functions, and the number of cost functions we need to consider depends essentially on the covering number of the metric space ( _X,c_ ). 

Algorithm 2 is an adaptation of Algorithm 1 for cost functions of the form 



where each function _b_ ∈B is separable, i.e., 



14 

Algorithm 2: A: gaming-robust classification algorithm for minima of separable cost <u>functions</u> 

- 1 Inputs: Labeled examples ( _x_ 1 _,h_ ( _x_ 1)) _,...,_ ( _xm,h_ ( _xm_ )) from _xi_ ∼D i.i.d.. Also, a description of _k_ separable cost functions _b_ ( _x,y_ ) = max{0 _,b_ 2( _y_ ) − _b_ 1( _x_ )} for _b_ ∈B. 

- 2 For _i_ = 1 _,...,m_ and _b_ ∈B, set 



and set _sm_ +1 _,b_ = ∞ for all _b_ ∈B. 3 For each _s_ ∈ � _b_ ∈B � _si,b_ : _i_ = 1 _,...,m_ + 1�, compute 





Theorem 3.3. _Suppose the cost function c is the minimum of separable functions,_ 



_where each b_ : _X_ × _X_ → R _is separable. Let_ D _be a distribution on X and suppose that Algorithm 2 uses m samples, so that m satisfies_ 



_Under these conditions, with probability at least_ 1 − _δ,_ (3) _holds for all h_ ∈H _and for the distribution_ D _. The running time of Algorithm 2 is O_ ( _m_<sup>|B|</sup> ) _._ 

The intuition for Algorithm 2 is similar to that for Algorithm 1, and is illustrated in Figure 2 for the minimum of two linear cost functions. The proof of Theorem 3.3 is also similar to that of Theorem 2.3; for completeness, we give it in Appendix A. 

Remark 3.4 (Improvements for structured classes B). _When the size of_ B _is small, Theorem 3.3 gives a nice bound. However, if_ B _is large (as in our extreme example of the beginning of this section), these guarantees are not so good. An inspection of the proof (in Appendix A) shows that the term_ <u>|B|</u> ln( _m_ +1) ~~�~~ _m may be replaced by Rm_ (H) _, where_ 



_For some sets_ B _of separable cost functions, this may be much smaller._ 

15 



<!-- Start of picture text -->
f ′<br>f<br>β<br>α<br><!-- End of picture text -->

Figure 2: Suppose the the optimal classifier for Jury is _f_ (which accepts the dark grey region), and the cost function is _c_ ( _x,y_ ) = min �� _β,y_ − _x_ �+<sup>_,_�</sup><sup>_α,y_−</sup><sup>_x_�</sup> +�. For the same reasoning as in Figure 1, the classifier _f_<sup>′</sup> has the same payoff to Jury as _f_ does. Thus, Jury may restrict his/her search to classifiers _f_ that are the intersections of two affine halfspaces. 

## 4 NP-completeness 

What happens when the cost function _c_ is not separable? It turns out that for general cost functions, any algorithm for Jury requires more than polynomial time to obtain a near-optimum classifier, unless _P_ = _NP_ . This holds true 

- (a) even if the underlying distance function is a metric (another very natural class of cost function), and 

- (b) even if the learning algorithm were given correct labels _h_ ( _x_ ) for _all_ members _x_ ∈ _X_ of the population, 

when the desired deviation _ε_ is inverse-polynomially small and the distribution D is uniform. The above statements are consequences of the following result: 

Theorem 4.1. _Given a finite population X with the uniform distribution, a metric c on X, and a target labeling h_ : _X_ �→{−1 _,_ +1} _, it is NP-hard to compute the strategic optimum within ε_ = | _X_ <u>1|</u><sup>_<u>η</u>for_</sup> _any constant η >_ 0 _._ 

_Proof of Theorem 4.1._ We will reduce from 3Sat. Suppose we are given a 3Sat Boolean formula with _n_ variables _x_ 1 _,...,xn_ and _m_ clauses _C_ 1 _,...,Cm_ , where _Ci_ has three literal occurrences _Li_ 1 _,Li_ 2 _,Li_ 3. We now construct our instance of Strategic Optimum as follows. We need to specify _X_ , _h_ , and _c_ . We begin by constructing a weighted population _Y_ , which will consist of points _y_ and positive integer weights _w_ ( _y_ ) for each _y_ ∈ _Y_ . Our population _X_ will simply consist of _w_ ( _y_ ) identical copies of each _y_ ∈ _Y_ . Thus, | _X_ | =<sup>�</sup> _y_ ∈ _Y_<sup>_w_(</sup><sup>_y_).We will also specify labels</sup><sup>_h_(</sup><sup>_y_) for</sup> each _y_ ∈ _Y_ , which the points _x_ ∈ _X_ will inherit. Fix a number _K_ (polynomial in _m_ ) to be chosen later. Our weighted population _Y_ consists of: 

- 3 _m_ points _Lik_ for 1 ⩽ _i_ ⩽ _m_ and _k_ ∈{1 _,_ 2 _,_ 3}, corresponding to the literal occurrences in the clauses. These points each have weight _w_ ( _Lik_ ) = _K_ ( _m_ − 1 − _m_<sup><u>1</u>) and label</sup><sup>_h_(</sup><sup>_Lik_) = −1.</sup> 

- <sup>�</sup><sup>_m_</sup> 2� points _Pij_ for 1 ⩽ _i < j_ ⩽ _m_ corresponding to unordered pairs { _Ci,Cj_ } of clauses. These points each have weight _w_ ( _Pij_ ) = 2 _K_ and label _h_ ( _Pij_ ) = +1. 

16 

- 9 ·<sup>�</sup><sup>_m_</sup> 2� points _Qikjℓ_ , for 1 ⩽ _i < j_ ⩽ _m_ , and for _k,ℓ_ ∈{1 _,_ 2 _,_ 3} so that _Lik_ is _not_ the negation of _Ljℓ_ . These points correspond to unordered pairs of literal occurrences { _Lik,Ljℓ_ } of literal occurrences in different clauses _which are not contradictory_ . They have weight _w_ ( _Qijkℓ_ ) = 1 and label _h_ ( _Qijkℓ_ ) = −1. (Actually, their label does not matter). 

- One other point _R_ with a huge weight _w_ ( _R_ ) = _KM_ , for a very large value _M_ , and label _h_ ( _R_ ) = −1. Choose _M_ = 2<sup>�</sup><sup>_m_</sup> 2�. 

We next define a metric _c_ : _X_ × _X_ → R+. It will take only two nonzero values, 1 _._ 5 and 2 _._ 5. Notice that this guarantees _c_ satisfies the triangle inequality. We will choose _c_ so that _c_ ( _x,x_ ) = 0 and _c_ ( _x,y_ ) = _c_ ( _y,x_ ), and so _c_ will indeed be a metric. To describe _c_ , it suffices to describe the points which are “close," that is, which have distance 1 _._ 5. Further, it suffices to define _c_ for points in _Y_ , and we will extend it to _X_ in a natural way: for points _x,x_<sup>′</sup> ∈ _X_ , if they come from the same _y_ ∈ _Y_ , they will have distance 1 _._ 5; if _x,x_<sup>′</sup> come from _y_ � _y_<sup>′</sup> respectively, then _c_ ( _x,x_<sup>′</sup> ) = _c_ ( _y,y_<sup>′</sup> ). The close pairs of points in _Y_ are: 

- All pairs of the form { _Pij,Qijkl_ }; 

- All pairs of the form { _Pij,R_ }; 

- All pairs of the form { _Qijkℓ,Lik_ } or { _Qijkℓ,Ljℓ_ }. 

Claim 4.2. _If the given formula is unsatisfiable, the number of points labeled_ +1 _by the Jury’s optimum f is equal to_ 



_which we call the_ baseline _payoff. Otherwise, if the given formula is satisfiable, then there is a labeling f of the points with payoff at least b_ + _K_ − 9<sup>�</sup><sup>_m_</sup> 2� _._ 

_Proof._ In the following, we will consider a graph with vertices _Y_ . Two vertices _x,y_ are neighbors in this graph if _c_ ( _x,y_ ) = 1 _._ 5. Let Γ ( _x_ ) denote the neighbors of _x_ in this graph. Thus, the bestresponse ∆ to a classifier _f_ is 



where above if _y_ in the last case is not uniquely defined Contestant can pick any such _y_ . 

First observe that the baseline payoff is obtained by the classifier _f_ ( _x_ ) = −1 for all _x_ ∈ _X_ , and so it is certainly acheivable. We now argue that Jury can do better if and only if the original formula was satisfiable. We make a few observations about Jury’s optimal classifier _f_ . 

- First, because of our choice of _M_ , we must have _f_ ( _Pij_ ) = −1 for all _i,j_ . Indeed, our choice implies that _KM >_ | _X_ | − _KM_ ; thus, if _f_ ( _Pij_ ) = 1 for some _i,j_ , then Contestant will set ∆( _R_ ) = _Pij_ , and Jury will mis-classify the point _R_ , and get a payoff worse than the baseline. 

- Next, _f_ ( _Lik_ ) = −1 for all _i,k_ . Indeed, since _h_ ( _Lik_ ) = −1 and _h_ ( _x_ ) = −1 for all of the ( _Q_ -type) neighbors of _Lik_ , there can be no benefit to Jury for making _f_ ( _Lik_ ) = +1. 

17 

– For each _Pij_ , at most one _Q_ -point _Qikjℓ_ in Γ ( _Pij_ ) has _f_ ( _Qikjℓ_ ) = +1. Indeed, each _Q_ -point is connected to exactly one _Pij_ , and once one of them is accepted by Jury, she can gain nothing by accepting additional points of Γ ( _Pij_ ). 

Thus, the optimal _f_ only assigns positive weights to _Q_ points, and it does so to at most one _Q_ -point in each Γ ( _Pij_ ). Suppose that _f_ ( _x_ ) = +1 for the set _A_ of _Q_ -points, and let _B_ = Γ _L_ ( _A_ ) be the set of _L_ -points adjacent to _A_ . Now, the size of _B_ can vary based on how the literals overlap with the clauses. It satisfies 



where the lower end is attained when there are complete collisions, and the upper end is attained when there are no collisions. Now consider the number of points of _X_ that Jury classifies correctly under such an _f_ . It is 



where 



Consider this first term, which is multiplied by _K_ . This is only positive when | _B_ | = _m_<sup>2|</sup> −<sup>_A_</sup> 1<sup><u>|</u>is as</sup> small as it can possibly be, which happens only if | _A_ | =<sup>�</sup><sup>_m_</sup> 2� and | _B_ | = _m_ . In this case, the first term is equal to _K_ , and we have _δ_ = _K_ −| _A_ | ⩾ _K_ − 9<sup>�</sup><sup>_m_</sup> 2�. But this happens if and only if we can choose _m_ different literals _Lik_ , one from each clause, so that no pair of them contradict each other; that is, if and only if the original formula was satisfiable. ■ 

Now the theorem follows quickly from the claim. We choose _K_ to be a large polynomial in _m_ , say _m_<sup>2</sup><sup>_/η_</sup> for some small constant _η_ . Thus, | _X_ | is on the order of _m_<sup>2</sup><sup>_/η_+2</sup> . Suppose there is a polynomial-time algorithm which approximates the strategic optimum up to _ε_ . Claim 4.2 implies a contradiction for any 



Using our choice of _K_ , for sufficiently large _m_ the right hand side is at least | _X_ |<sup>−</sup><sup>_η_</sup> . Thus, we have a contradiction whenever _ε <_ | _X_ |<sup>−</sup><sup>_η_</sup> . ■ 

The metric constructed in the proof has “separability dimension” (the smallest number of separable functions needed to achieve it as a minimum) that grows linearly with the population. The same dimension appears in the exponent of the running time of the algorithm of the previous section. It is an interesting open problem to determine whether this exponential dependence is inherent; the other possibility is that the problem is _fixed-parameter tractable_ with respect to the “separability dimension” parameter. We suspect that exponential dependence is necessary. 

18 

## 5 Experiments 

We conducted experiments on real data from a Brazilian social network called Apontador that provides location-based recommendations and reviews. The data set was introduced in the context of spam fighting in a recent work by Costa et al. [CdCMBB14] and is available from the authors upon request. The data set consists of 7076 instances of so-called “tips” half of which are labeled as “spam”. Tips are pieces of user-provided content associated with the places listed on Apontador. The paper distinguishes between different types of spam, but the distinction does not matter for us, so we will only consider one category. There are 60 features in total, but to facilitate the modeling of a cost function we restricted our attention to the 15 most discriminative features as indicated by previous work [CdCMBB14]. We normalized all features of the data to have zero mean and unit standard deviation. 

The goal of our cost function is not primarily to capture monetary cost of changing certain attributes. Apart from attributes like “number of followers”, most attributes are technically easy to change. Rather the goal of a cost function is to capture the loss in expected revenue that a spammer experiences when changing certain parts of the spam message. If, for instance, it is essential for the spam message to contain a URL or contact information, then the spammer experiences lost revenue when such information is omitted. Similarly, the spammer could choose to post his messages on the pages of lower-rated places, but such pages are less frequented and hence his utility decreases. Similar reasoning applies to the modeling of the other attributes. Cheap attributes are those that can be changed without a loss in utility for the spammer. For example, the “number of words” is not robust as the spammer can freely choose to write longer or shorter messages. 

With this intuition in mind, we model our cost function as a simple linear function truncated at 0 to make it non-negative. That is we consider a cost function of the form _c_ ( _x,y_ ) = ⟨ _α,y_ − _x_ ⟩+ _._ Truncation at 0 is a meaningful modeling decision, since a spammer doesn’t derive any utility from, say, decreasing the number of his followers even though it is costly to increase this attribute. 

The cost vector _α_ specifies for each attribute a coefficient quantifying the cost of changing that attribute. We do not attempt to construct as realistic a cost function as possible. We only distinguish between three types of cost: somewhat costly to increase (coefficient 1), somewhat costly to decrease (coefficient −1 _._ 0) and cheap to increase (coefficient 0 _._ 1). The concrete values of these coefficients are rather arbitrary and different choices may be more suitable. The next table details each feature with its description and its associated cost. For a more detailed explanation of these features, the reader is referred to [CdCMBB14]. 

19 

||Description|Cost coefficient|
|---|---|---|
|1|Number of tips on the place|−1|
|2|Place rating|−1|
|3|Number of emails|−1|
|4|Number of contact information|−1|
|5|Number of URLs|−1|
|6|Number of phone numbers|−1|
|7|Number of numeric characters|−1|
|8|SentiStrength score|1|
|9|Combined-method|1|
|10|Number of words|0_._1|
|11|Ratio of followers to followees|1|
|12|Number of distinct 1-grams|0_._1|
|13|Number of tips posted by user|0_._1|
|14|Number of followers|1|
|15|Number of capital letters|0_._1|



We made no attempt to arrive at a perfectly-realistic cost function. Instead our focus is on a qualitative comparison of our approach with a standard SVM classifier, which does not take gaming into account. We selected SVM as a representative classifier as it was shown in previous work [CdCMBB14] to achieve high classification accuracy on this data set compared with other standard classifiers. For simplicity and increased interpretability, we use a _linear_ SVM which still achieves high accuracy. 

If we were to assume that our model of gaming and choice of cost function were perfectly correct, then a standard SVM would perform very poorly when compared with our algorithm. To obtain a more balanced comparison, we take modeling inaccuracies into account in our experiments. Specifically, we account for two potential inaccuracies in our model: 

1. The true cost function is not the one on which we train our algorithm. 

2. The amount of gaming varies and does not necessarily correspond to the threshold predicted by our theoretical framework. 

Finally, we explore a convenient way to interpolate between the classifier suggested by our approach and standard classifiers. This leads to different trade-offs which are more favorable in certain settings. 

### 5.1 Comparison with SVM under robustness to modeling errors 

We now show that our method is robust to significant modeling errors while simultaneously outperforming SVM even if only a small amount of gaming occurs. 

To formalize our error model, we assume that there is a true underlying cost function which differs from the cost function we feed into Algorithm 1. We imagine that the true cost function is some mixture of the linear cost function described above, plus a squared Euclidean distance term: 



On the other hand, we run our algorithm on a cost function which is incorrect in two ways. First, it is separable, so it necessarily ignores the squared-distance term. Second, we do not 

20 

imagine that we have correctly identified _α_ , and we replace it with some _α_<sup>′</sup> : 



The addition of the Euclidean norm in (8) reflects the possibility that our separability assumption does not exactly hold. The difference between _α_ and _α_<sup>′</sup> reflects the possibility that we may not even have accurately identified the separable part. We stress that not only does our algorithm not know the true cost function, it also does not know the parameter _ε_ , or how much _α_ differs from _α_<sup>′</sup> . 

For our experiments, we considered a range of values of _ε_ , and we generated _α_<sup>′</sup> from _α_ at random by adding Gaussian noise and re-normalizing. We develop our classifier using _c_ assumed, but then for tests allow Contestant to best-respond to the classifier given the cost function _c_ true. We note that finding the best response to a linear classifier given the cost function _c_ true is a simple calculus problem. 

The other parameter we varied is the amount of gaming allowed. In our theoretical framework above, the Contestant is always willing to pay a cost of up to 2, since his payoff for switching is 1 − (−1) = 2. To relax this assumption and vary the amount of gaming allowed, we multiply both _c_ true and _c_ assumed by 2 _/t_ ; we say that this allows _t_ units of gaming. Notice that by the definition of _c_ true, this means that the Contestant is willing to move distance _t_ in the direction of _α_ , and possibly more in other directions. As mentioned above, we have normalized the standard deviation of all attributes to be 1. 

Within the above error model, we compare our algorithm with SVM as a representative standard classifier. Figures 3 show that our algorithm outperforms SVM, even under a small amount of gaming, and even in the presence of significant modeling errors. 

### 5.2 A hybrid approach for higher accuracy 

In practice it is convenient to start from a standard classifier and make it more robust to gaming and as opposed to adopting an entirely new classifier. Our framework gives a convenient way to incorporate a set of known classifiers into the design of a strategy-robust classifier. As we show below this can lead to more favorable trade-offs between gaming and accuracy. 

The basic idea is to use each known classifier as a feature to which we assign a positive weight in the cost function. In other words, we stipulate that the classifier is by itself a somewhat reliable attribute of the data. Below we try out this hybrid approach by combining our classifier with the standard SVM classifier. Indeed, we find in our experiments that the hybrid has higher accuracy in a robust range of parameters. This is shown in Figure 4. 

In the case of a linear SVM, the decision boundary is given by a vector _β_ and we can simple add this vector to our cost function. We assume that the true cost function _c_ true is as above, but we modify _c_ assumed as: 



where _β_ are the SVM coefficients learned from the training data set. 

## Acknowledgments 

We are grateful for stimulating discussions with Cynthia Dwork, Brendan Juba, Silvio Micali, Omer Reingold and Aaron Roth. We are also grateful to Fabricio Benevenuto for pointing us to 

21 



<!-- Start of picture text -->
Comparison with SVM Comparison with SVM<br>0.80 0.68<br>Ours, ϵ =0.1<br>0.66<br>Ours, ϵ =0.3<br>0.75<br>SVM, ϵ =0.1 0.64<br>SVM, ϵ =0.3<br>0.70 0.62<br>0.60<br>0.65<br>0.58<br>0.60 0.56<br>Ours, ϵ =0.1<br>0.54 Ours, ϵ =0.3<br>0.55<br>SVM, ϵ =0.1<br>0.52<br>SVM, ϵ =0.3<br>0.50 0.50<br>0.5 1.0 1.5 2.0 2.5 3.0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8<br>Gaming Angle<br>Accuracy Accuracy<br><!-- End of picture text -->

Figure 3: Left: Our algorithm compared with SVM as the amount of gaming is increased. The _x_ -axis tracks the amount of gaming, which is quantified as described above. The parameter _ε_ in _c_ true is specified in the legend. We have set sin _θ_ ( _α,α_<sup>′</sup> ) = 0 _._ 394 (again, _α_<sup>′</sup> was randomly generated from _α_ by adding Gaussian noise and re-normalizing). Right: Our algorithm compared with SVM as the angle between _α_ and _α_<sup>′</sup> increases. The _x_ -axis measures the angle sin _θ_ ( _α,α_<sup>′</sup> ). The amount of gaming was fixed at 1 _._ 0, and the parameter _ε_ in _c_ true is specified in the legend. 

the Apondator data set and sharing it with us, and to an anonymous reviewer for pointing out that our uniform result implied the non-uniform corollary. 

## References 

- [BBL05] Stéphane Boucheron, Olivier Bousquet, and Gábor Lugosi. Theory of classification: A survey of some recent advances. _ESAIM: probability and statistics_ , 9:323–375, 2005. 

- [BKS12] Michael Brückner, Christian Kanzow, and Tobias Scheffer. Static prediction games for adversarial learning problems. _Journal of Machine Learning Research_ , 13:2617–2654, 2012. 

- [BS09] Michael Brückner and Tobias Scheffer. Nash equilibria of static prediction games. In _Proc._ 23 _rd NIPS 2009_ , pages 171–179, 2009. 

- [BS11] Michael Brückner and Tobias Scheffer. Stackelberg games for adversarial prediction problems. In _Proc_ 17 _th ACM SIGKDD_ , pages 547–555, 2011. 

- [CdCMBB14] Helen Costa, Luiz Henrique de Campos Merschmann, Fabrício Barth, and Fabrício Benevenuto. Pollution, bad-mouthing, and local marketing: The underground of location-based social networks. _Inf. Sci._ , 279:123–137, 2014. 

- [CP14] Danielle Keats Citron and Frank Pasquale. The scored society: Due process for automated predictions. _89 Washington Law Review_ , 1, 2014. 

22 



<!-- Start of picture text -->
Hybrid approach<br>0.85<br>0.80<br>0.75<br>0.70<br>0.65 0<br>0.25<br>0.60 0.5<br>.75<br>0.55 1.0<br>SVM<br>0.50<br>0.5 1.0 1.5 2.0 2.5 3.0<br>Gaming<br>Accuracy<br><!-- End of picture text -->

Figure 4: Interpolation between the SVM classifier and our classifier. In the model above, we begin with a cost function that has sin _θ_ ( _α,α_<sup>′</sup> ) ≈ 0 _._ 2 and _ε_ = 0 _._ 2. Then we mix the weight vector _α_<sup>′</sup> with the weights _β_ obtained from SVM to arrive at _α_<sup>′′</sup> = (1− _γ_ ) _α_ + _γβ_ which defines the assumed cost function. The lines in the plot above show what happens as the amount of gaming increases when setting _γ_ = 0 _,_ 0 _._ 25 _,_ 0 _._ 5 _,_ 0 _._ 75 _,_ 1. Notice that the difference between the SVM curve and the curve with _γ_ = 1 is that the classifier for _γ_ = 1 is shifted according to our algorithm. 

- [DDM<sup>+</sup> 04] Nilesh N. Dalvi, Pedro Domingos, Mausam, Sumit K. Sanghai, and Deepak Verma. Adversarial classification. In _Proc_ 10 _th ACM SIGKDD_ , pages 99–108, 2004. 

- [EKST10] M.D.R. Evans, J. Kelley, J. Sikora, and D. J. Treiman. Family scholarly culture and educational success: Evidence from 27 nations. _Research in Social Stratification and Mobility_ , 28:171–197, 2010. 

- [GSBS13] Michael Großhans, Christoph Sawade, Michael Brückner, and Tobias Scheffer. Bayesian games for adversarial regression problems. In _Proc._ 30 _th ICML_ , pages 55–63, 2013. 

- [KCP10] Dmytro Korzhyk, Vincent Conitzer, and Ronald Parr. Complexity of computing optimal Stackelberg strategies in security resource allocation games. In _Proc. AAAI_ , 2010. 

- [KYK<sup>+</sup> 11] Dmytro Korzhyk, Zhengyu Yin, Christopher Kiekintveld, Vincent Conitzer, and Milind Tambe. Stackelberg vs. Nash in security games: An extended investigation of interchangeability, equivalence, and uniqueness. _J. Artif. Intell. Res.(JAIR)_ , 41:297–327, 2011. 

- [LT91] Michel Ledoux and Michel Talagrand. _Probability in Banach Spaces: isoperimetry and processes_ , volume 23. Springer, 1991. 

23 

[Val84] Leslie Valiant. A theory of the learnable. _Communications of the ACM_ , 27(11):1134–1142, 1984. 

## A Proof of Theorem 3.3 

_Proof of Theorem 3.3._ Fix _h_ ∈C. As in the proof of Theorem 2.3, we begin by defining the set Γ ( _f_ ) of _x_ ∈ _X_ so that _f_ (∆( _x_ )) = 1 when ∆ is a best response to _f_ . For every _f_ ∈C, we have 



Now we can again restrict our attention to nicely structured functions. For any _f_ , let 



Then, as in the proof of Theorem 2.3, we have 



for all _b_ ∈B. Indeed, 



by definition of _f_<sup>′</sup> , and 



using the fact that 



for all _b_ ∈B. Thus, 



Thus, as before, the payoff to Jury if she plays _f_ is the same as if she plays _f_<sup>′</sup> : 



24 

Thus, it suffices to consider classifiers _f_ of the form (9). Moving the quantifiers around, it suffices to consider classifiers of the form 



for 



Here, _sb_ plays the role of min{ _b_ 2( _z_ ) : _f_ ( _z_ ) = 1}, and _sb_ = ∞ means that _f_ ( _z_ ) = −1 for all _z_ ∈ _X_ . For _f_ as in (10), we have 



and a best-possible payoff to Jury is obtained by finding the best thresholds _s_ : 



In Algorithm 2, Jury returns 



and as above the payoff to Jury from this _f_ is 



As in the proof of Theorem 2.3, to prove Theorem 3.3 it suffices to show that for all _h_ ∈C, 



As before, we have 



so it suffices to establish that err(� _s_ ) is close to err( _s_ ), uniformly over _s_ ∈ _S_ B. Claim A.1. _With probability at least_ 1 − _δ, for all h_ ∈C _and s_ ∈ _S_ B _,_ 



_In particular, if the hypotheses of the lemma are met, with probability at least_ 1 − _δ,_ 



_Proof._ Again, this follows very similarly to the proof of Theorem 2.3. We need to bound the absolute value of the following difference: 



25 

for all _h_ ∈C and _s_ ∈ _S_ B. As before (via, say, Theorem 3.2 in [BBL05]), we have for all _h_ ∈C _, s_ ∈ _S_ B, 



where 



As before, 



where H = {min _b_ ∈B _b_ 1[ _sb_ − 2] : _s_ ∈ _S_ B}, so it remains to bound _Rm_ (H). For fixed _x_ 1 _,...,xm_ ∈ _X_ , we have 



Thus, we have 



and, along with Equation 13, this finishes the claim. 

As in the proof of Theorem 2.3, Equation 12 and Claim A.1 finish the proof of Theorem 3.3. ■ 



26 

