---
title: "Strategic Classification is Causal Modeling in Disguise"
authors: "miller"
year: 2019
arxiv_id: "1910.10362"
original_file: "1910.10362.pdf"
pdf_path: "docs/papers\2019_miller_strategic_classification_is_causal.pdf"
---

# Strategic Classification is Causal Modeling in Disguise

**Authors:** Miller et al.  
**Year:** 2019 | **arXiv:** [`1910.10362`](https://arxiv.org/abs/1910.10362)  
**Local PDF:** [`2019_miller_strategic_classification_is_causal.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_miller_strategic_classification_is_causal.pdf)

---

# Strategic Classification is Causal Modeling in Disguise 

John Miller Smitha Milli Moritz Hardt 

February 19, 2020 

#### Abstract 

Consequential decision-making incentivizes individuals to strategically adapt their behavior to the specifics of the decision rule. While a long line of work has viewed strategic adaptation as gaming and attempted to mitigate its effects, recent work has instead sought to design classifiers that incentivize individuals to improve a desired quality. Key to both accounts is a cost function that dictates which adaptations are rational to undertake. In this work, we develop a causal framework for strategic adaptation. Our causal perspective clearly distinguishes between gaming and improvement and reveals an important obstacle to incentive design. We prove any procedure for designing classifiers that incentivize improvement must inevitably solve a non-trivial causal inference problem. Moreover, we show a similar result holds for designing cost functions that satisfy the requirements of previous work. With the benefit of hindsight, our results show much of the prior work on strategic classification is causal modeling in disguise. 

## 1 Introduction 

Individuals faced with consequential decisions about them often use knowledge of the decision rule to strategically adapt towards achieving a desirable outcome. Much work in computer science views such _strategic adaptation_ as adversarial behavior (Dalvi et al., 2004; Br¨uckner et al., 2012), manipulation, or _gaming_ (Hardt et al., 2016; Dong et al., 2018). More recent work rightfully recognizes that adaptation can also correspond to attempts at self-improvement (Bambauer and Zarsky, 2018; Kleinberg and Raghavan, 2019). Rather than seek classifiers that are robust to gaming (Hardt et al., 2016; Dong et al., 2018), these works suggest to design classifiers that explicitly _incentive improvement_ on some target measure (Kleinberg and Raghavan, 2019; Alon et al., 2019; Khajehnejad et al., 2019; Haghtalab et al., 2020). 

Incentivizing improvement requires a clear distinction between gaming and improvement. While this distinction may be intuitive in some cases, in others, it is subtle. Do employer rewards for punctuality improve productivity? It sounds plausible, but empirical evidence suggests otherwise (Gubler et al., 2016). Indeed, the literature is replete with examples of failed incentive schemes (Oates and Schwab, 2015; Rich and Larson, 1984; Belot and Schr¨oder, 2016). 

Our contributions in this work are two-fold. First, we provide the missing formal distinction between gaming and improvement. This distinction is a corollary of a comprehensive causal framework for strategic adaptation that we develop. Second, we give a formal reason why incentive design is so difficult. Specifically, we prove any successful attempt to incentivize improvement must have solved a non-trivial causal inference problem along the way. 

1 

### 1.1 Causal Framework 

We conceptualize individual adaptation as performing an _intervention_ in a causal model that includes all relevant features _X_ , a predictor _Y_<sup>ˆ</sup> , as well as the target variable _Y_ . We then characterize gaming and improvement by reasoning about how the corresponding intervention affects the predictor _Y_<sup>ˆ</sup> and the target variable _Y_ . This is illustrated in Figure 1. 

We combine the causal model with an _agent-model_ that describes how individuals with a given setting of features respond to a classification rule. For example, it is common in strategic classification to model agents as being rational with respect to a _cost function_ that quantifies the cost of feature changes. 

Combining the causal model and agent model, we can separate improvement from gaming. Informally speaking, improvement corresponds to the case where the agent response to the predictor causes a positive change in the target variable _Y_ . Gaming corresponds to the case where the agent response causes a change in the prediction _Y_<sup>ˆ</sup> but not the underlying target variable _Y_ . Making this intuition precise, however, requires the language of counterfactuals of the form: What value would the variable _Y_ have taken had the individual changed her features to _X_<sup>′</sup> given that her original features were _X_ ? 

If we think of the predictor as a _treatment_ , we can analogize our notion of improvement with the established causal quantity known as _effect of treatment on the treated_ . 

### 1.2 Inevitability of Causal Analysis 

Viewed through this causal lens, only adaptations on causal variables can lead to improvement. Intuitively, any mechanism for incentivizing improvement must therefore capture some knowledge of the causal relationship between the features and the target measure. We formalize this intuition and prove causal modeling is unavoidable in incentive design. Specifically, we establish a computationally efficient reduction from discovering the causal structure relating the variables (sometimes called causal graph discovery) to a sequence of incentive design problems. In other words, designing classifiers to incentivize improvement is as hard as causal discovery. 

Beyond incentivizing improvement, a number of recent works model individuals as acting in accordance with well-behaved cost functions that capture the difficulty of changing the target variable. We show constructing such _outcome-monotonic_ cost functions also requires modeling the causal structure relating the variables, and we give a similar reduction from designing outcome-monotonic cost functions to causal discovery. 

In conclusion, our contributions show that—with the benefit of hindsight—much work on strategic classification turns out to be causal modeling in disguise. 

### 1.3 Related Work 

This distinction between causal and non-causal manipulation in a classification setting is intuitive, and such considerations were present in early work on statistical risk assessment in lending (Hand et al., 1997). Although they do not explicitly use the language of causality, legal scholars Bambauer and Zarsky (2018) give a qualitatively equivalent distinction between gaming and improvement. While we focus on the incentives classification creates for individuals, Everitt et al. (2019) introduce a causal framework to study the incentives classification creates for decision-makers, e.g. which features the decision-maker is incentivized to use. 

2 



<!-- Start of picture text -->
The classification<br>Gaming Improvement<br>causal graph X 4 := x ˆ4 X 2 := x ˆ2<br>X 1 x 1 x 1<br>X 2 X 3 x 2 x 3 x ˆ2 x 3<br>Y Y ˆ y =0 y ˆ=1 y =1 y ˆ=1<br>X 4 x ˆ4 x ˆ4<br>Causal features Non-causal features Target variable Classifier output<br><!-- End of picture text -->

Figure 1: Illustration of the causal framework for strategic adaptation. Adaptation is modeled as interventions in a _counterfactual_ causal graph, conditioned on the individual’s initial features _X_ . Gaming corresponds to interventions that change the classification _Y_<sup>ˆ</sup> , but do not change the true label _Y_ . Improvement corresponds to interventions that change both the classification _Y_<sup>ˆ</sup> and the true label _Y_ . Incentivizing improvement requires inducing agents to intervene on _causal_ features that can change the label _Y_ rather than _non-causal_ features. Distinguishing between these two categories of features in general requires causal analysis. 

Numerous papers in strategic classification (Br¨uckner et al., 2012; Dalvi et al., 2004; Hardt et al., 2016; Dong et al., 2018) focuses on game-theoretic frameworks for preventing gaming. These frameworks form the basis of our agent-model, and Milli et al. (2019); Braverman and Garg (2019); Khajehnejad et al. (2019) introduce the outcome-monotonic cost functions we analyze in Section 5. Since these approaches do not typically distinguish between gaming and improvement, the resulting classifiers can be unduly conservative, which in turn can lead to undesirable social costs (Hu et al., 2019; Milli et al., 2019; Braverman and Garg, 2019). 

The creation of decision rules with optimal incentives, including incentives for improvement, has been long studied in economics, notably in principle-agent games (Ross, 1973; Grossman and Hart, 1992). In machine learning, recent work by Kleinberg and Raghavan (2019) and Alon et al. (2019) studies the problem of producing a classifier that incentivizes a given “effort profile”, the amount of desired effort an individual puts into certain actions, and assumes the evaluator knows which forms of agent effort would lead to improvement, which is itself a form of causal knowledge. Haghtalab et al. (2020) seek to design classifiers that maximize improvement across the population, while Khajehnejad et al. (2019) seek to maximize institutional utility, taking into account both improvement and gaming. While these works do not use the language of causality, we demonstrate that these approaches nonetheless must perform some sort of causal modeling if they succeed in incentivizing improvement. 

In this paper, we primarily consider questions of improvement or gaming from the perspective of the decision maker. However, what gets categorized as improvement or gaming also often reflects a moral judgement—gaming is bad, but improvement is good. Usually good 

3 

or bad means good or bad from the perspective of the system operator. Ziewitz (2019) analyzes how adaptation comes to be seen as ethical or unethical through a case study on search engine optimization. Burrell et al. (2019) argue that gaming can also be a form of individual “control” over the decision rule and that the exercise of control can be legitimate independently of whether an action is considered gaming or improvement in our framework. 

## 2 Causal background 

We use the language of _structural causal models_ (Pearl, 2009) as a formal framework for causality. A structural causal model (SCM) consists of endogenous variables _X_ = ( _X_ 1 _,...,Xn_ ), exogenous variables _U_ = ( _U_ 1 _,...,Un_ ), a distribution over the exogenous variables, and a set of structural equations that determine the values of the endogenous variables. The structural equations can be written 



where _gi_ is an arbitrary function, PA _i_ represents the other endogenous variables that determine _Xi_ , and _Ui_ represents exogenous noise due to unmodeled factors. 

A structural causal model gives rise to a _causal graph_ where a directed edge exists from _Xi_ to _Xj_ if _Xi_ is an input to the structural equation governing _Xj_ , i.e. _Xi_ ∈ PA _j_ . We restrict ourselves to _Markovian_ structural causal models, which have an acyclic causal graph and independent exogenous variables. The _skeleton_ of a causal graph is the undirected version of the graph. 

An _intervention_ is a modification to the structural equations of an SCM. For example, an intervention may consist of replacing the structural equation _Xi_ = _gi_ (PA _i,Ui_ ) with a new structural equation _Xi_ � _xi_ that holds _Xi_ at a fixed value. We use � to denote modifications of the original structural equations. When the structural equation for one variable is changed, other variables can also change. Suppose _Z_ and _X_ are two endogenous nodes, Then, we use the notation _ZX_ � _x_ to refer to the variable _Z_ in the modified SCM with structural equation _X_ � _x_ . 

Given the values _u_ of the exogenous variables _U_ , the endogenous variables are completely deterministic. We use the notation _Z_ ( _u_ ) to represent the deterministic value of the endogenous variable when the exogenous variables _U_ are equal to _u_ . Similarly, _ZX_ � _x_ ( _u_ ) is the value of _Z_ in the modified SCM with structural equation _X_ � _x_ when _U_ = _u_ . 

More generally, given some event _E_ , _ZX_ � _x_ ( _E_ ) is the random variable _Z_ in the modified SCM with structural equations _X_ � _x_ where the distribution of exogenous variables _U_ is updated by conditioning on the event _E_ . We make heavy use of this _counterfactual_ notion. For more details, see Pearl (2009). 

## 3 A Causal Framework for Strategic Adaptation 

In this section, we put forth a causal framework for reasoning about the incentives induced by a decision rule. Our framework consists of two components: _the agent model_ and _the causal model_ . The agent model is a standard component of work on strategic classification and determines what actions agents undertake in response to the decision rule. The causal model enables us to reason cogently about how these actions affect the agent’s true label. Pairing these models together allow us to distinguish between incentivizing _gaming_ and incentivizing _improvement_ . 

4 

### 3.1 The Agent Model 

As a running example, consider a software company that uses a classifier to filter software engineering job applicants. Suppose the model considers, among other factors, open-source contributions made by the candidate. Some individuals realize this and _adapt_ —perhaps they polish their resume; perhaps they focus more of their energy on making open source contributions. The agent model describes precisely how individuals choose to adapt in response to a classifier. 

As in prior work on strategic classification (Hardt et al., 2016; Dong et al., 2018), we model individuals as _best-responding_ to the classifier. Formally, consider an individual with features _x_ ∈X ⊆ R<sup>_n_</sup> , label _y_ ∈Y ⊆ R, and a classifier _f_ : R<sup>_n_</sup> →Y . The individual has a set of available actions A, and, in response to the classifier _f_ , takes action _a_ ∈A to adapt her features from _x_ to _x_ + _a_ . For instance, the features _x_ might encode the candidate’s existing open-source contributions, and the action _a_ might correspond to making additional open-source contributions. Crucially, these modifications incur a _cost c_ ( _a_ ; _x_ ), and the action the agent takes is determined by directly balancing the benefits of classification _f_ ( _x_ + _a_ ) with the cost of adaptation _c_ ( _a_ ; _x_ ). 

Definition 3.1 (Best-response agent model). Given a cost function _c_ : A × X → R+ and a classifier _f_ : X →Y , an individual with features _x_ best responds to the classifier _f_ by choosing action 



Let ∆( _x_ ; _f_ ) = _x_ + _a_<sup>∗</sup> denote a _best-response_ of the agent to classifier _f_ . When clear from context, we omit the dependence on _f_ and write ∆( _x_ ). 

In the best-response agent model, the cost function completely dictates what actions are rational for the agent to undertake and occupies a central modeling challenge. We discuss this further in Section 5. Our definition of the cost function in terms of an action set A is motivated by Ustun et al. (2019). However, this formulation is completely equivalent to the agent-models considered in other work (Hardt et al., 2016; Dong et al., 2018). In contrast to prior work, our main results only require that individuals approximately best-respond to the classifier. 

Definition 3.2 (Approximate best-response). For any _ε_ ∈ (0 _,_ 1), say ∆ _ε_ ( _x,f_ ) = _x_ + _a_ ˜ is an _ε_ - best-response to classifier _f_ if _f_ ( _x_ + ˜ _a_ ) − _c_ (˜ _a_ ; _x_ ) ≥ _ε_ · (max _a f_ ( _x_ + _a_ ) − _c_ ( _a_ ; _x_ )). 

### 3.2 The Causal Model 

While the agent model specifies which actions the agent takes in response to the classifier, the causal model describes how these actions effect the individual’s true label. 

Returning to the hiring example, suppose individuals decide increase their open-source contributions, _X_ . Does this improve their software engineering skill, _Y_ ? There are two different causal graphs that explain this scenario. In one scenario, _Y_ → _X_ : the more skilled one becomes, the more likely one is to contribute to open-source projects. In the other scenario, _X_ → _Y_ : the more someone contributes to open source, the more skilled they become. Only in the second world, when _X_ → _Y_ , do adaptations that increase open-source contributions raise the candidate’s skill. 

More formally, recall that a structural causal model has two types of nodes: endogenous nodes and exogenous nodes. In our model, the endogenous nodes are the individual’s true label 

5 

_Y_ , their features _X_ = { _X_ 1 _,...,Xn_ }, and their classification outcome _Y_<sup>ˆ</sup> . The structural equation for _Y_<sup>ˆ</sup> is represented by the classifier _Y_<sup>ˆ</sup> = _f_ ( _Z_ ), where _Z_ ⊆ _X_ are the features that the classifier _f_ has access to and uses. The exogenous variables _U_ represent all the other unmodeled factors. 

For an individual with features _X_ = _x_ , let ∆( _x,f_ ) denote the agent’s response to classifier _f_ . Since the agent chooses ∆( _x,f_ ) as a function of the observed features _x_ , the label after adaptation is a _counterfactual_ quantity. This, we model the individual’s adaptation as an intervention in the submodel _conditioned on observing features X_ = _x_ . What value would the label _Y_ take if the individual had features ∆( _X,f_ ), given that her features were originally _X_ ? 

Formally, let _A_ = { _i_ : ∆( _x,f_ ) _i_ � _xi_ } be the subset of features the individual adapts, and let _XA_ index those features. Then, the label after adaptation is given by _YXA_ �∆( _x,f_ ) _A_ ({ _X_ = _x_ }). The dependence on _A_ ensures that, if an individual only intervenes on a subset of features, the remaining features are still consistent with the original causal model. For brevity, we omit reference to _A_ and write _YX_ �∆( _x,f_ )({ _X_ = _x_ }). In the language of potential outcomes, both _X_ and _Y_ are completely deterministic given the exogenous variables _U_ = _u_ , and we can express the label under adaptation as _YX_ �∆( _x,f_ )( _u_ ). 

Much of the prior literature in strategic classification eschews explicit causal terminology and instead posits the existence of a “qualification function” or a “true binary classifier” _h_ : X →Y that maps the individual’s features to their “true quality” (Hardt et al., 2016; Hu et al., 2019; Braverman and Garg, 2019; Haghtalab et al., 2020). Such a qualification function should be thought of as the strongest possible causal model, where _X_ is causal for _Y_ , and the structural equation determining _Y_ is completely deterministic. 

### 3.3 Evaluating Incentives 

Equipped with both the agent model and the causal model, we can formally characterize the incentives induced by a decision rule _f_ . Key to our categorization is the notion of _improvement_ , which captures how the classifier induces agents to change their label on average over the population baseline. 

Definition 3.3. For a classifier _f_ and a distribution over features _X_ and label _Y_ generated by a structural causal model, define the _improvement_ incentivized by _f_ , as 



If _I_ ( _f_ ) _>_ 0, we say that _f incentivizes improvement_ . Otherwise, we say that _f incentivizes gaming_ . 

By the tower property, definition 3.3 can be equivalently written in terms of potential outcomes _I_ ( _f_ ) = E _U_ � _YX_ �∆( _x,f_ )( _U_ ) − _Y_ ( _U_ )�. In this view, if we imagine exposure to the classifier _f_ as a treatment, then improvement is the _treatment effect of exposure to classifier f on the label Y_ . In general, since all individuals are exposed and adapt to the classifier in our model, and estimating improvement becomes an exercise in estimating the effect of treatment on the treated, and identifying assumptions are provided in Shpitser and Pearl (2009). Our notion of improvement is closely related to notion of “gain” discussed in Haghtalab et al. (2020), albeit with a causal interpretation. We can similarly characterize improvement at the level of the individuals. 

Definition 3.4. For a classifier _f_ and a distribution over features _X_ and label _Y_ generated by a structural causal model, define the _improvement_ incentivized by _f_ for an individual with 

6 



<!-- Start of picture text -->
X Y Z Y ˆ<br><!-- End of picture text -->

Figure 2: Reasoning about incentives requires both the agent-model and the causal model. The cost function plays a central role in the agent-model. Even though the classification _Y_<sup>ˆ</sup> only depends on the non-causal feature _Z_ , the agent can change the label by manipulating, _X_ , _Z_ or both, depending on the cost function. The causal model determines how the agent’s adaptation affects the target measure, but the agent model, and in turn the cost function, determines which actions the agent actually takes. 

features _x_ as 



At first glance, the causal model and Definition 3.3 appear to offer a convenient heuristic for determining whether a classifier incentivizes gaming. Namely, does the classifier rely on non-causal features? However, even a classifier that uses purely non-causal features can still incentivize improvement if manipulating upstream, causal features is less costly than directly manipulating the non-causal features. The following example formalizes this intuition. Thus, reasoning about improvement requires considering both the agent model and the causal model. Example 3.1. Suppose we have a structural causal model with features _X,Z_ and label _Y_ disi.i.d. tributed as _X_ � _UX_ , _Y_ � _X_ + _UY_ , and _Z_ � _Y_ + _UZ_ , where _UX,UY ,UZ_ ∼N (0 _,_ 1). Let the classifier _f_ depend only on the non-causal feature, _Z_ , _f_ ( _z_ ) = _y_ ˆ. Let A = R<sup>2</sup> , and define the cost function _c_ ( _a_ ; _x_ ) = (1 _/_ 2) _a_<sup>⊤</sup> _Ca_ , where _C_ ≻ 0 is a symmetric, positive definite matrix with det( _C_ ) = 1. Then, direct computation shows ∆( _x,z_ ; _f_ ) = ( _x_ − _C_ 12 _,z_ + _C_ 11), and _I_ ( _f_ ) = − _C_ 12. Hence, provided _C_ 12 _<_ 0, _f_ incentivizes improvement despite only rely on non-causal features. When _C_ 12 _<_ 0 changing _x_ and _z_ jointly is less costly than manipulating _z_ alone. This _complementarity_ (Holmstrom and Milgrom, 1991) allows the decision-maker to incentivize improvement using only a non-causal feature. This example is illustrated in Figure 2. 

## 4 Incentivizing Improvement Requires Causal Modeling 

Beyond evaluating the incentives of a particular classifier, recent work has sought to _design_ classifiers that explicitly incentivize improvement. Haghtalab et al. (2020) seeks classifiers that _maximize_ the improvement of strategic individuals according to some quality score. Similarly, both Kleinberg and Raghavan (2019) and Alon et al. (2019) construct decision-rules that incentivize investment in a desired “effort profile” that ultimately leads to individual improvement. In this section, we show that when these approaches succeed in incentivizing improvement, they must also solve a non-trivial causal modeling problem. Therefore, while they may not explicitly discuss causality, much of this work is _necessarily_ performing causal reasoning. 

### 4.1 The Good Incentives Problem 

We first formally state the problem of designing classifiers that incentivize improvement, which we call the _good incentives problem_ . Consider the hiring example presented in Section 3. A 

7 

decision-maker has access to a distribution over features (open-source contributions, employment history, coding test scores, etc), a label (engineering ability), and wishes to design a decision rule that incentivizes strategic individuals to improve their engineering ability. As discussed in Section 3, the decision-maker must reason about the agent model governing adaptation, and we assume agent’s _approximately_ best-respond according to some specified cost function. 

Definition 4.1 (Good Incentives Problem). Assume agents _ε_ -best-respond to the classifier for some _ε >_ 0. Given: 

1. A joint distribution _PX,Y_ over examples ( _x,y_ ) ∈X ×Y entailed by structural causal model, and 

2. A cost function _c_ : A × X → R+, 

Find a classifier _f_<sup>∗</sup> : X →Y that incentivizes improvement, i.e. find a classifier with _I_ ( _f_<sup>∗</sup> ) _>_ 0. If no such classifier exists, output `Fail` . 

The good incentives problem is closely related to the improvement problem studied in Haghtalab et al. (2020). Translated into our framework, Haghtalab et al. (2020) seek classifiers that optimally incentivize improvement and solve max _f I_ ( _f_ ), which is a more difficult problem than finding _some_ classier that leads to improvement. 

In the sequel, let `GoodIncentives` be an oracle for the Good Incentives problem. `GoodIncentives` takes as input a cost function and a joint distribution over features and label, and either returns a classifier that incentivizes improvements or returns no such classifier exists. 

### 4.2 A Reduction From Causal Modeling to Designing Good Incentives 

Incentivizing improvement requires both (1) knowing which actions lead to improvement, and (2) incentivizing individuals to take those actions. Since only adaptation of causal features can affect the true label _Y_ , determining which actions lead to improvement necessitates distinguishing between causal and non-causal features. Consequently, any procedure that can provide incentives for improvement must capture some, possibly implicit, knowledge about the causal relationship between the features and the label. 

The main result of this section generalizes this intuition and establishes a reduction from orienting the edges in a causal graph to designing classifiers that incentivize improvement. Orienting the edges in a causal graph is not generally possible from observational data alone (Peters et al., 2017), though it can be addressed through active intervention (Eberhardt et al., 2005). Therefore, any procedure for constructing classifiers that incentivize improvement must at its core also solve a non-trivial causal discovery problem. 

We prove this result under a natural assumption: improvement is always possible by manipulating causal features. In particular, for any edge _V_ → _W_ in the causal graph, there is always _some_ intervention on _V_ a strategic agent can take to improve _W_ . We formally state this assumption below, and, as a corollary, we prove this assumption holds in a broad family of causal graphs: additive noise models. 

Assumption 4.1. _Let G_ = ( _X,E_ ) _be a causal graph, let X_ − _W denote the random variables X excluding node W . For any edge_ ( _V ,W_ ) ∈ _E with V_ → _W , there exists a real-valued function h mapping X_ − _w to an intervention v_<sup>∗</sup> = _h_ ( _x_ − _w_ ) _so that_ 



8 

Importantly, the intervention _v_<sup>∗</sup> = _h_ ( _x_ − _w_ ) discussed in Assumption 4.1 is an intervention in the counterfactual model, conditional on observing _X_ − _W_ = _x_ − _w_ . In strategic classification, this corresponds to choosing the adaptation conditional on the values of the observed features. Before proving Assumption 4.1 holds for faithful additive noise models, we first state and prove the main result. 

Under Assumption 4.1, we exhibit a reduction from orienting the edges in a causal graph to the good incentives problem. While Assumption 4.1 requires Equation (1) to hold for every edge in the causal graph, it is straightforward to modify the result when Equation (1) only holds for a subset of the edges. 

Theorem 4.1. _Let G_ = ( _X,E_ ) _be a causal graph induced by a structural causal model that satisfies Assumption 4.1. Assume X has bounded support_ X _. Given the skeleton of G, using_ | _E_ | _calls to_ `GoodIncentives` _, we can orient all of the edges in G._ 

_Proof of Theorem 4.1._ The reduction proceeds by invoking the good incentives oracle for each edge ( _Xi,Xj_ ), taking _Xj_ as the label and using a cost function that ensures only manipulations on _Xi_ are possible for an _ε_ -best-responding agent. If _Xi_ → _Xj_ , then Assumption 4.1 ensures that improvement is possible, and we show `GoodIncentives` must return a classifier that incentivizes improvement. Otherwise, if _Xi_ ← _Xj_ , no intervention on _Xi_ can change _Xj_ , so `GoodIncentives` must return `Fail` . 

More formally, let _Xi_ − _Xj_ be an undirected edge in the skeleton _G_ . We show how to orient _Xi_ − _Xj_ with a single oracle call. Let _X_ − _j_ ≜ _X_ \ � _Xj_ � be the set of features excluding _Xj_ , and let _x_ − _j_ denote an observation of _X_ − _j_ . 

Consider the following good incentives problem instance. Let _Xj_ be the label, and let the features be ( _X_ − _j, X_<sup>˜</sup> _i_ ), where _X_<sup>˜</sup> _i_ is an identical copy of _Xi_ with structural equation _X_<sup>˜</sup> _i_ � _Xi_ . Let the action set A = R<sup>_n_</sup> , and let _c_ be a cost function that ensures an _ε_ -best-responding agent will only intervene on _Xi_ . In particular, choose 



where _B_ = sup {∥ _x_ ∥∞ : _x_ ∈X}. In other words, the individuals pays no cost to take actions that only affect _Xi_ , but otherwise pays cost 2 _B_ . Since every feasible classifier _f_ takes values in X , _f_ ( _x_ ) ≤ _B_ , and any action _a_ with _ak_ � 0 leads to negative agent utility. At the same time, action _a_ = 0 has non-negative utility, so an _ε_ -best-responding agent can only take actions that affect _Xi_ . 

We now show `GoodIncentives` returns `Fail` if and only if _Xi_ ← _Xj_ . First, suppose _Xi_ ← _Xj_ . Then _Xi_ is not a parent nor an ancestor of _Xj_ since if there existed some _Xi_ � _Z_ � _Xj_ path, then _G_ would contain a cycle. Therefore, no intervention on _Xi_ can change the expectation of _Xj_ , and consequently no classifier that can incentivize improvement exists, so `GoodIncentives` must return `Fail` . 

On the other hand, suppose _Xi_ → _Xj_ . We explicitly construct a classifier _f_ that incentivizes improvement, so `GoodIncentives` cannot return `Fail` . By Assumption 4.1, there exists a function _h_ so that 



Since _X_<sup>˜</sup> _i_ � _Xi_ , Assumption 4.1 still holds additionally conditioning on _X_<sup>˜</sup> _i_ = _x_ ˜ _i_ . Any classifier that induces agents with features ( _x_ − _j,_ ˜ _xi_ ) to respond by adapting only _Xi_ � _h_ ( _x_ − _j_ ) will therefore 

9 

incentivize improvement. The intervention _Xi_ � _h_ ( _x_ − _j_ ) given _X_ − _j_ = _x_ − _j_ is incentivizable by the classifier 



where _x_ ˜ _j_ indicates that _xi_ is replaced by _x_ ˜ _i_ in the vector _x_ − _j_ . 

An _ε_ -best-responding agent will choose action _a_<sup>∗</sup> where _a_<sup>∗</sup> _i_<sup>=</sup><sup>_h_( ˜</sup><sup>_x_−</sup><sup>_j_)−</sup><sup>_xi_and otherwise</sup><sup>_a_</sup> _k_<sup>∗= 0</sup> in response to _f_ . To see this, _a_<sup>∗</sup> has cost 0. Since _X_<sup>˜</sup> _i_ � _Xi_ , we initially have _xi_ = _x_ ˜ _i_ . Moreover, by construction, _h_ ( ˜ _x_ − _j_ ) depends only on the feature copy _x_ ˜ _i_ , not _xi_ , so _h_ ( ˜ _x_ − _j_ ) is invariant to adaptations in _xi_ . Therefore, _h_ ( ˜ _x_ − _j_ + _a_ −<sup>∗</sup> _i_<sup>) =</sup><sup>_h_( ˜</sup><sup>_x_−</sup><sup>_j_) =</sup><sup>_xi_+</sup><sup>_a_</sup> _i_<sup>∗,so</sup><sup>_f_((</sup><sup>_x_−</sup><sup>_j,_˜</sup><sup>_xi_) +</sup><sup>_a_∗) = 1.Thus,action</sup> _a_<sup>∗</sup> has individual utility 1, whereas all other actions have zero or negative utility, so any _ε_ -best responding agent will choose _a_<sup>∗</sup> . Since all agents take _a_<sup>∗</sup> , it then follows by construction that _I_ ( _f_ ) _>_ 0. 

Repeating this procedure for each edge in the causal graph thus fully orients the skeleton with | _E_ | calls to `GoodIncentives` . 

We now turn to showing that Assumption 4.1 holds in a large class of nontrivial causal model, namely additive noise models (Peters et al., 2017). 

Definition 4.2 (Additive Noise Model). A structural causal model with graph _G_ = ( _X,E_ ) is an additive noise model if the structural assignments are of the form 



Further, we assume that all nodes _Xi_ are non-degenerate and that their joint distribution has a strictly positive density.<sup>1</sup> 

Before stating the result, we need one additional technical assumption, namely faithfulness. The faithfulness assumption is ubiquitous in causal graph discovery setting and rules out additional conditional independence statements that are not implied by the graph structure. For more details and a precise statement of the d-separation criteria, see Pearl (2009). 

Definition 4.3 (Faithful). A distribution _PX_ is _faithful_ to a DAG _G_ if _A_ ⊥⊥ _B_ | _C_ implies that _A_ and _B_ are d-separated by _C_ in _G_ 

Proposition 4.1. _Let_ ( _X_ 1 _,...,Xn_ ) _be an additive noise model, and let the joint distribution on_ ( _X_ 1 _,...,Xn_ ) _be faithful to the graph G. Then, G satisfies Assumption 4.1._ 

_Proof._ For intution, we prove the result in the two-variable case and defer the full proof to Appendix A. Suppose _X_ → _Y_ , so that _Y_ := _gY_ ( _X_ ) + _UY_ . Since _X_ is non-degenerate, _X_ takes at least two values with positive probability. Moreover, since the distribution is faithful to _G_ , _gY_ cannot be a constant function, since otherwise _Y_ ⊥⊥ _X_ . Define _x_<sup>∗</sup> ∈ argmax _x gY_ ( _x_ ). Then, we have 

E _X_ E [ _YX_ � _x_ ∗ ({ _X_ = _x_ })] = E _X_ E [ _gY_ ( _x_<sup>∗</sup> ) + _UY_ | _X_ = _x_ ] _>_ E [ _gY_ ( _X_ ) + _UY_ ] = E [ _Y_ ] _._ 

On the other hand, Assumption 4.1 can indeed fail in non-trivial cases. 

Example 4.1. Consider a two variable graph with _X_ → _Y_ . Let _Y_ = _εX_ where _X_ and _ε_ are independent and E [ _ε_ ] = 0. In general, _X_ and _Y_ are not independent, but for any _x,x_<sup>′</sup> , E [ _YX_ := _x_ ′ ({ _X_ = _x_ })] = _x_<sup>′</sup> E [ _ε_ ] = 0 = E [ _Y_ ]. 

> 1 The condition that the nodes _X_ have a strictly positive density is met when, for example, the functional relationships _fi_ are differentiable and the noise variables _Ui_ have a strictly positive density (Peters et al., 2017). 

10 

## 5 Designing Good Cost Functions Requires Causal Modeling 

The cost function occupies a central role in the best-response agent model and essentially determines which actions the individual undertakes. Consequently, not few works in strategic classification model individuals as behaving according to cost functions with desirable properties, among which is a natural _monotonicity_ condition—actions that raise an individual’s underlying qualification are more expensive than those that do not. In this section, we prove an analogous result to the previous section and show constructing these cost functions also requires causal modeling. 

### 5.1 Outcome-Monotonic Cost Functions 

Although they use all slightly different language, Milli et al. (2019), Khajehnejad et al. (2019), and Braverman and Garg (2019) all assume the cost function is well-aligned with the label. Intuitively, they both assume (i) actions that lead to large increases in one’s qualification are more costly than actions that lead to small increases, and (ii) actions that decrease or leave unchanged one’s qualification have no cost. Braverman and Garg (2019) define these cost functions using an arbitrary qualification function that maps features _X_ to label _Y_ , while Milli et al. (2019) and Khajehnejad et al. (2019) instead use the _outcome-likelihood_ Pr( _y_ | _x_ ) as the qualification function. Khajehnejad et al. (2019) explicitly assume a causal factorization so that Pr( _y_ | _x_ ) is invariant to interventions on _X_ , and the qualification function of Braverman and Garg (2019) ensures a similar causal relationship between _X_ and _Y_ . Translating these assumptions into the causal framework introduced in Section 3, we obtain a class of _outcome-monotonic_ cost functions. 

Definition 5.1 (Outcome-monotonic cost). A cost function _c_ : A×X → R+ is _outcome-monotonic_ if, for any features _x_ ∈X : 

1. For any action _a_ ∈A, _c_ ( _a_ ; _x_ ) = 0 if and only if E [ _YX_ � _x_ + _a_ ({ _X_ = _x_ })] ≤ E[ _Y_ | _X_ = _x_ ]. 

2. For pair of actions _a,a_<sup>′</sup> ∈A, _c_ ( _a_ ; _x_ ) ≤ _c_ ( _a_<sup>′</sup> _,x_ ) if and only if 

E [ _YX_ � _x_ + _a_ ({ _X_ = _x_ })] ≤ E [ _YX_ � _x_ + _a_ ′ ({ _X_ = _x_ })] _._ 

While several works assume the decision-maker has access to an outcome-monotonic cost, in general the decision-maker must explicitly construct such a cost function from data. This challenge results in the following problem. 

Definition 5.2 (Learning outcome-monotonic cost problem). Given action set A and a joint distribution _PX,Y_ over a set of features _X_ and label _Y_ entailed by a structural causal model, construct an outcome-monotonic cost function _c_ . 

### 5.2 A Reduction From Causal Modeling to Constructing Outcome-Monotonic Costs 

Outcome-monotonic costs are both conceptually desirable (Milli et al., 2019; Braverman and Garg, 2019) and algorithmically tractable (Khajehnejad et al., 2019). Simultaneously, outcomemonotonic cost functions encode significant causal information, and the main result of this section is a reduction from orienting the edges in a causal graph to learning outcome-monotonic cost functions under the same assumption as Section 4. Consequently, any procedure that can 

11 

successfully construct outcome-monotonic cost functions must inevitably solve a non-trivial causal modeling problem. 

Proposition 5.1. _Let G_ = ( _X,E_ ) _induced by a structural causal model that satisfies Assumption 4.1. Let_ `OutcomeMonotonicCost` _be an oracle for the outcome-monotonic cost learning problem. Given the skeleton of G,_ | _E_ | _calls to_ `OutcomeMonotonicCost` _suffices to orient all the edges in G._ 

_Proof._ Let _X_ denote the variables in the causal model, and let _Xi_ − _Xj_ be an undirected edge. We can orient this edge with a single call to `OutcomeMonotonicCost` . Let _X_ − _j_ ≜ _X_ \ � _Xj_ � denote the variables excluding _Xj_ . 

Construct an instance of the learning outcome-monotonic cost problem with features _X_ − _j_ , label _Xj_ , and action set A = { _αei_ : _α_ ∈ R}, where _ei_ is the _i_ -th standard basis vector. In other words, the only possible actions are those that adjust the _i_ -th coordinate. Let _c_ denote the outcome-monotonic cost function returned by the oracle `OutcomeMonotonicCost` . We argue _c_ ≡ 0 if and only if _Xi_ ← _Xj_ . 

Similar to the proof of Theorem 4.1, if _Xi_ ← _Xj_ , then _Xi_ can be neither a parent nor an ancestor of _Xj_ . Therefore, conditional on _X_ − _j_ = _x_ − _j_ , there is no intervention on _Xi_ that can change the conditional expectation of _Xj_ . Since no agent has a feasible action that can increase the expected value of the label _Xj_ and the cost function _c_ is outcome-monotonic, _c_ is identically 0. 

On the other hand, suppose _Xi_ → _Xj_ . Then, by Assumption 4.1, there is a real-valued function _h_ such that 



This inequality along with the tower property then implies there is some agent _x_ − _j_ such that 



since otherwise the expectation would be zero or negative. Since _h_ ( _x_ − _j_ ) _ei_ ∈A by construction, there is some action _a_ ∈A that can increase the expectation of the label _Xj_ for agents with features _x_ − _j_ , so _c_ ( _a_ ; _x_ − _j_ ) � 0, as required. 

The proof of Proposition 5.1 makes repeated calls to an oracle to construct outcome-monotonic cost functions to decode the causal structure of the graph _G_ . In many cases, however, even a single outcome-monotonic cost function encode significant information about the underlying graph, as the following example shows. 

Example 5.1. Consider a causal model with features ( _X,Z_ ) and label _Y_ with the following structural equations 



12 

for some set of non-zero coefficients _θi_ ∈ R and arbitrary functions _gj_ . In other words, the model consists of _n_ causal features, _m_ non-causal features, and a linear structural equation for _Y_ . 

Suppose the action set A = R<sup>_n_+</sup><sup>_m_</sup> , and let _c_ be any outcome-monotonic cost. Then, 2( _n_ + _m_ ) queries evaluations of _c_ suffice to determine (1) which features are causal, and (2) sign( _θi_ ) for _i_ = 1 _,...,n_ . To see this, evaluate the cost function at points _c_ ( _ei_ ;0) and _c_ (− _ei_ ;0), where _ei_ denotes the _i_ -th standard basis vector. Direct calculation shows 



Therefore, since _c_ is outcome-monotonic, if _c_ ( _ei_ ;0) _>_ 0, then sign( _θi_ ) = 1, if _c_ (− _ei_ ;0) _>_ 0, then sign( _θi_ ) = −1, and if both _c_ ( _ei_ ;0) = 0 and _c_ (− _ei_ ;0) = 0, then feature _i_ is non-causal. 

## 6 Discussion 

The large collection of empirical examples of failed incentive schemes is a testament to the difficulty of designing incentives for individual improvement. In this work, we argued an important source of this difficulty is that incentivize design must inevitably grapple with causal analysis. Our results are not hardness results per se. There are no fundamental computational or statistical barriers that prevent causal modeling beyond the standard unidentifiability results in causal inference. Rather, our work suggests attempts to design incentives for improvement without some sort of causal reasoning are unlikely to succeed. 

Beyond incentive design, we hope our causal perspective clarifies intuitive, though subtle notions like gaming and improvement and provides a clear and consistent formalism for reasoning about strategic adaptation more broadly. 

## References 

- Tal Alon, Magdalen Dobson, Ariel D Procaccia, Inbal Talgam-Cohen, and Jamie Tucker-Foltz. Multiagent evaluation mechanisms. 2019. 

- Jane Bambauer and Tal Zarsky. The algorithm game. _Notre Dame L. Rev._ , 94:1, 2018. 

- Mich`ele Belot and Marina Schr¨oder. The spillover effects of monitoring: A field experiment. _Management Science_ , 62(1):37–45, 2016. 

- Mark Braverman and Sumegha Garg. The role of randomness and noise in strategic classification. 2019. 

- Michael Br¨uckner, Christian Kanzow, and Tobias Scheffer. Static prediction games for adversarial learning problems. _Journal of Machine Learning Research_ , 13(Sep):2617–2654, 2012. 

- Jenna Burrell, Zoe Kahn, Anne Jonas, and Daniel Griffin. When users control the algorithms: values expressed in practices on twitter. _Proceedings of the ACM on Human-Computer Interaction_ , 3:19, 2019. 

13 

- Nilesh Dalvi, Pedro Domingos, Sumit Sanghai, Deepak Verma, et al. Adversarial classification. In _Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 99–108. ACM, 2004. 

- Jinshuo Dong, Aaron Roth, Zachary Schutzman, Bo Waggoner, and Zhiwei Steven Wu. Strategic classification from revealed preferences. In _Proceedings of the 2018 ACM Conference on Economics and Computation_ , pages 55–70. ACM, 2018. 

- Frederick Eberhardt, Clark Glymour, and Richard Scheines. On the number of experiments sufficient and in the worst case necessary to identify all causal relations among n variables. In _Proceedings of the Twenty-First Conference on Uncertainty in Artificial Intelligence_ , pages 178–184. AUAI Press, 2005. 

- Tom Everitt, Pedro A Ortega, Elizabeth Barnes, and Shane Legg. Understanding agent incentives using causal influence diagrams, part i: single action settings. _arXiv preprint arXiv:1902.09980_ , 2019. 

- Sanford J Grossman and Oliver D Hart. An analysis of the principal-agent problem. In _Foundations of Insurance Economics_ , pages 302–340. Springer, 1992. 

- Timothy Gubler, Ian Larkin, and Lamar Pierce. Motivational spillovers from awards: Crowding out in a multitasking environment. _Organization Science_ , 27(2):286–303, 2016. 

- Nika Haghtalab, Nicole Immorlica, Brendan Lucier, and Jack Wang. Maximizing welfare with incentive-aware evaluation mechanisms. 2020. 

- DJ Hand, KJ McConway, and E Stanghellini. Graphical models of applicants for credit. _IMA Journal of Management Mathematics_ , 8(2):143–155, 1997. 

- Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic classification. In _Proceedings of the 2016 ACM conference on innovations in theoretical computer science_ , pages 111–122. ACM, 2016. 

- Bengt Holmstrom and Paul Milgrom. Multitask principal–agent analyses: Incentive contracts, asset ownership, and job design. _The Journal of Law, Economics, and Organization_ , 7(special ~~i~~ ssue):24–52, 1991. 

- Lily Hu, Nicole Immorlica, and Jennifer Wortman Vaughan. The disparate effects of strategic manipulation. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 259–268. ACM, 2019. 

- Moein Khajehnejad, Behzad Tabibian, Bernhard Sch¨olkopf, Adish Singla, and Manuel Gomez-Rodriguez. Optimal decision making under strategic behavior. _arXiv preprint arXiv:1905.09239_ , 2019. 

- Jon Kleinberg and Manish Raghavan. How do classifiers induce agents to invest effort strategically? In _Proceedings of the 2019 ACM Conference on Economics and Computation_ , pages 825–844. ACM, 2019. 

- Smitha Milli, John Miller, Anca D Dragan, and Moritz Hardt. The social cost of strategic classification. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 230–239. ACM, 2019. 

14 

- Wallace E Oates and Robert M Schwab. The window tax: A case study in excess burden. _Journal of Economic Perspectives_ , 29(1):163–80, 2015. 

Judea Pearl. _Causality_ . Cambridge University Press, 2009. 

- J. Peters, D. Janzing, and B. Sch¨olkopf. _Elements of Causal Inference: Foundations and Learning Algorithms_ . Adaptive Computation and Machine Learning series. MIT Press, 2017. 

- Jude T Rich and John A Larson. Why some long-term incentives fail. _Compensation Review_ , 16 (1):26–37, 1984. 

- Stephen A Ross. The economic theory of agency: The principal’s problem. _The American Economic Review_ , 63(2):134–139, 1973. 

- Ilya Shpitser and Judea Pearl. Effects of treatment on the treated: identification and generalization. In _Proceedings of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence_ , pages 514–521, 2009. 

- Berk Ustun, Alexander Spangher, and Yang Liu. Actionable recourse in linear classification. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 10–19. ACM, 2019. 

- Malte Ziewitz. Rethinking gaming: The ethical work of optimization in web search engines. _Social studies of science_ , page 0306312719865607, 2019. 

15 

## A Missing Proofs 

_Proposition 4.1._ Let _V_ → _W_ be an edge in _G_ . We show there exists a real-valued function _h_ that maps a realization of nodes _X_ − _W_ = _x_ − _w_ to an intervention _v_<sup>∗</sup> that increases the expected value of _W_ . Therefore, we first condition on observing the remaining nodes _X_ − _W_ = _x_ − _w_ . In an additive noise model, given _X_ − _W_ = _x_ − _w_ the exogenous noise terms for all of the ancestors of _W_ can be uniquely recovered. In particular, the noise terms are determined by 



Let _U_ A denote the collection of noise variables for ancestors of _W excluding_ those only have a path through _V_ . Both _U_ A = _u_ A and _V_ = _v_ are fixed by _X_ − _W_ = _x_ − _w_ . 

Consider the structural equation for _W_ , _W_ = _gW_ (PA _W_ ) + _UW_ . The parents of _W_ , PA _W_ , are deterministic given _V_ and _U_ A. Therefore, given _V_ = _v_ and _U_ A = _u_ A, _gW_ (PA _W_ ) is a deterministic function of _v_ and _u_ A, which we write _g_ ˜ _W_ ( _v,u_ A). 

Now, we argue _g_ ˜ _W_ is not constant in _v_ . Suppose _g_ ˜ _W_ were constant in _v_ . Then, for every _u_ A, _g_ ˜ _W_ ( _v,u_ A) = _k_ ( _u_ A). However, this means _W_ = _k_ ( _U_ A) + _UW_ , and _U_ A is independent of _V_ , so we find that _V_ and _W_ are independent. However, since _V_ → _W_ in _G_ , this contradicts faithfulness. 

Since _g_ ˜ _W_ is not constant in _v_ , there exists at least one setting of _u_ A with _v,v_<sup>′</sup> so that _g_ ˜ _W_ ( _v_<sup>′</sup> _,u_ A) _> g_ ˜ _W_ ( _v,u_ A). Since _X_ has positive density, ( _v,ua_ ) occurs with positive probability. Consequently, if _h_ ( _u_ A) = argmax _v g_ ˜ _W_ ( _v,u_ A), then 



Finally, notice _h_ ( _u_ A) can be computed solely form _x_ − _w_ since _u_ A is fixed given _x_ − _w_ . Together, this establishes that Assumption 4.1 is satisfied for the additive noise model. 

16 

