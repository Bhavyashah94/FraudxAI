---
title: "Decisions, Counterfactual Explanations and Strategic Behavior"
authors: "tsirtsis"
year: 2020
arxiv_id: "2002.04333"
original_file: "2002.04333.pdf"
pdf_path: "docs/papers\2020_tsirtsis_decisions_counterfactual_explanatio.pdf"
---

# Decisions, Counterfactual Explanations and Strategic Behavior

**Authors:** Tsirtsis et al.  
**Year:** 2020 | **arXiv:** [`2002.04333`](https://arxiv.org/abs/2002.04333)  
**Local PDF:** [`2020_tsirtsis_decisions_counterfactual_explanatio.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_tsirtsis_decisions_counterfactual_explanatio.pdf)

---

# Decisions, Counterfactual Explanations and Strategic Behavior 

Stratis Tsirtsis and Manuel Gomez-Rodriguez 

Max Planck Institute for Software Systems _{_ stsirtsis, manuelgr _}_ @mpi-sws.org 

#### **Abstract** 

As data-driven predictive models are increasingly used to inform decisions, it has been argued that decision makers should provide explanations that help individuals understand what would have to change for these decisions to be beneficial ones. However, there has been little discussion on the possibility that individuals may use the above _counterfactual explanations_ to invest effort strategically and maximize their chances of receiving a beneficial decision. In this paper, our goal is to find policies and counterfactual explanations that are optimal in terms of utility in such a strategic setting. We first show that, given a pre-defined policy, the problem of finding the optimal set of counterfactual explanations is NP-hard. Then, we show that the corresponding objective is nondecreasing and satisfies submodularity and this allows a standard greedy algorithm to enjoy approximation guarantees. In addition, we further show that the problem of jointly finding both the optimal policy and set of counterfactual explanations reduces to maximizing a non-monotone submodular function. As a result, we can use a recent randomized algorithm to solve the problem, which also offers approximation guarantees. Finally, we demonstrate that, by incorporating a matroid constraint into the problem formulation, we can increase the diversity of the optimal set of counterfactual explanations and incentivize individuals across the whole spectrum of the population to self improve. Experiments on synthetic and real lending and credit card data illustrate our theoretical findings and show that the counterfactual explanations and decision policies found by our algorithms achieve higher utility than several competitive baselines. 

## **1 Introduction** 

Whenever a bank decides to offer a loan to a customer, a university decides to admit a prospective student, or a company decides to hire a new employee, the decision is increasingly informed by a datadriven predictive model. In all these high-stakes applications, the goal of the predictive model is to provide accurate predictions of the outcomes from a set of observable features while the goal of the decision maker is to take decisions that maximize a given utility function. For example, in university admissions, the predictive model may estimate the ability of each prospective student to successfully complete the graduate program while the decision maker may weigh the model’s estimate against other socio-economic considerations ( _e.g._ , number of available scholarships, diversity commitments). 

In this context, there has been a tremendous excitement on the potential of data-driven predictive models to enhance decision making in high-stakes applications. However, there has also been a heated debate about their lack of transparency and explainability (Doshi-Velez and Kim, 2017; Weller, 2017; Lipton, 2018; Gunning and Aha, 2019; Rudin, 2019). As a result, there already exists a legal requirement to grant individuals who are subject to (semi)-automated decision making the _right-to-explanation_ in the European Union (Voigt and Von dem Bussche, 2017; Wachter et al., 2017a). With this motivation, there has been a flurry of work on interpretable machine learning (Ribeiro et al., 2016; Koh and Liang, 2017; Lundberg and Lee, 2017; Chakraborty et al., 2017; Wachter et al., 2017b; Murdoch et al., 2019; Ustun et al., 2019; Karimi et al., 2019; Mothilal et al., 2020), which has predominantly focused on developing methods to find explanations for the predictions made by a predictive model. Within this line of work, the work most closely related to ours (Wachter et al., 2017b; Ustun et al., 2019; Karimi et al., 2019; Mothilal et al., 2020) aims to find counterfactual explanations that help individuals understand what would have to change for a predictive model to make a positive prediction about them. However, none of these works distinguish between decisions and predictions and, consequently, cannot be readily used to 

1 

provide explanations to the decisions taken by a decision maker, which are ultimately what individuals who are subject to (semi)-automated decision making typically care about. 

In our work, we build upon a recent line of work that explicitly distinguishes between predictions and decisions (Corbett-Davies et al., 2017; Kilbertus et al., 2019; Kleinberg et al., 2018; Mitchell et al., 2018; Tabibian et al., 2020; Valera et al., 2018) and then pursue the development of methods to find counterfactual explanations for the decisions taken by a decision maker who is assisted by a data-driven predictive model. These counterfactual explanations help individuals understand what would have to change in order to receive a beneficial decision, rather than a positive prediction. Moreover, once we focus on explaining decisions, we cannot overlook the possibility that individuals may use these explanations to invest effort strategically in order to maximize their chances of receiving a beneficial decision. However, this is also an opportunity for us to find counterfactual explanations that help individuals to self-improve and eventually increase the utility of a decision policy, as noted by several studies in economics (Coate and Loury, 1993; Fryer and Loury, 2013; Hu and Chen, 2018) and, more recently, in the computer science literature (Kleinberg and Raghavan, 2019; Perdomo et al., 2020; Tabibian et al., 2020). For example, if a bank explains to a customer that, if she reduces her credit card debt by 20%, she will receive the loan she is applying for, she may feel compelled to reduce her overall credit card debt by the proposed percentage to pay less interest, improving her financial situation, and this will eventually increase the profit the bank makes when she is able to successfully return the loan. This is in contrast with previous work on interpretable machine learning, which have ignored the influence that (counterfactual) explanations (of predictions by a predictive model) may have on the accuracy of predictive models and the utility of the decision policies<sup>1</sup> . 

**Our contributions.** We cast the above problem as a Stackelberg game in which the decision maker moves first and shares her counterfactual explanations before individuals best-respond to these explanations and invest effort to receive a beneficial decision. In this context, we assume that the decision maker takes decisions based on low dimensional feature vectors since, in many realistic scenarios, the data is summarized by just a small number of summary statistics ( _e.g._ , FICO scores) (Hardt et al., 2016b; Liu et al., 2018). Under this problem formulation, we first show that, given a pre-defined policy, the problem of finding the optimal set of counterfactual explanations is NP-hard by using a novel reduction of the Set Cover problem (Karp, 1972). Then, we show that the corresponding objective function is monotone and submodular and, as a direct consequence, it readily follows that a standard greedy algorithm offers approximation guarantees. In addition, we show that, given a pre-defined set of counterfactual explanations, the optimal policy is deterministic and can be computed in polynomial time. Moreover, building on this result, we can reduce the problem of jointly finding both the optimal policy and set of counterfactual explanations to maximizing a non-monotone submodular function. As a consequence, we can use a recent randomized algorithm to solve the problem, which also offers approximation guarantees. Further, we demonstrate that, by incorporating a matroid constraint into the problem formulation, we can increase the diversity of the optimal set of counterfactual explanations and incentivize individuals across the whole spectrum of the population to self improve. Experiments using real lending and credit card data illustrate our theoretical findings and show that the counterfactual explanations and decision policies found by the above algorithms achieve higher utility than several competitive baselines<sup>2</sup> . 

## **2 Problem Formulation** 

Given an individual with a feature vector **_x_** _∈{_ 1 _, ..., n}_<sup>_d_</sup> and a ( _ground-truth_ ) label _y ∈{_ 0 _,_ 1 _}_ , we assume a decision _d_ ( **_x_** ) _∈{_ 0 _,_ 1 _}_ controls whether the corresponding label is _realized_<sup>3</sup> . This setting fits a variety of real-world scenarios, where continuous features are often discretized into (percentile) ranges. For example, in university admissions, the decision specifies whether a student is admitted ( _d_ ( **_x_** ) = 1) or rejected ( _d_ ( **_x_** ) = 0); the label indicates whether the student completes the program ( _y_ = 1) or drops out ( _y_ = 0) upon acceptance; and the feature vector ( **_x_** ) may include her GRE scores, undergraduate GPA percentile, or research experience. Throughout the paper, we will denote the set of feature values as _X_ = _{_ **_x_** 1 _,_ **_x_** 2 _, . . . ,_ **_x_** _m}_ , where _m_ = _n_<sup>_d_</sup> denotes the number of feature values, and assume that the number of features _d_ is small, as discussed previously. 

> 1Refer to Appendix A for a discussion of further related work. 

> 2An open-source implementation can be found at https://github.com/Networks-Learning/strategic-decisions. 

> 3Without loss of generality, we assume each feature takes _n_ different values. 

2 

Each decision is sampled from a decision policy _d_ ( **_x_** ) _∼ π_ ( _d |_ **_x_** ), where, for brevity, we will write _π_ ( **_x_** ) = _π_ ( _d_ = 1 _|_ **_x_** ). For each individual, the label _y_ is sampled from a conditional probability distribution _y ∼ P_ ( _y |_ **_x_** ) and, without loss of generality, we index the feature values in decreasing order with respect to their corresponding outcome, _i.e._ , _i < j ⇒ P_ ( _y_ = 1 _|_ **_x_** _i_ ) _≥ P_ ( _y_ = 1 _|_ **_x_** _j_ ). Moreover, we adopt a Stackelberg game-theoretic formulation in which each individual with initial feature value **_x_** _i_ receives a (counterfactual) explanation from the decision maker by means of a feature value _E_ ( **_x_** _i_ ) _∈A ⊆Pπ_ := _{_ **_x_** _∈X_ : _π_ ( **_x_** ) = 1 _}_ before she (best-)responds<sup>4</sup> . This formulation fits a variety of real-world applications. For example, insurance companies often provide online car insurance simulators that, on the basis of a customer’s initial feature value **_x_** _i_ , let the customer know whether they are eligible for a particular deal. In case the customer does not qualify, the simulator could provide a counterfactual example _E_ ( **_x_** _i_ ) under which the individual is guaranteed to be eligible. In the remainder, we will refer to _A_ as the set of counterfactual explanations and, for each individual with initial feature value **_x_** _i_ , we will assume she does not know anything about the other counterfactual explanations _A\E_ ( **_x_** _i_ ) other individuals may receive nor the decision policy _π_ ( **_x_** ). 

Now, let _c_ ( **_x_** _, E_ ( **_x_** _i_ )) be the cost<sup>5</sup> an individual pays for changing from **_x_** _i_ to _E_ ( **_x_** _i_ ) and _b_ ( _π,_ **_x_** ) = E _d∼π_ ( _d | x_ )[ _d_ ( **_x_** )] be the (immediate) benefit she obtains from a policy _π_ , which is just the probability that the individual receives a positive decision. Then, following Tabibian et al. (2020), each individual’s best response is to change from her initial feature value **_x_** _i_ to _E_ ( **_x_** _i_ ) iff the gained benefit she would obtain outweighs the cost she would pay for changing features, _i.e._ , 



and it is to keep her initial feature value **_x_** _i_ otherwise. Here, we will refer to _R_ ( **_x_** _i_ ) as the _region of adaptation_ . Then, at a population level, the above best response results into a transportation of mass between the original feature distribution _P_ ( **_x_** ) and a new feature distribution _P_ ( **_x_** _| π, A_ ) induced by the policy _π_ and the counterfactual explanations _A_ . More specifically, we can readily derive an analytical expression for the induced feature distribution in terms of the original feature distribution, _i.e._ , for all **_x_** _j ∈X_ , 



Similarly as in previous work (Corbett-Davies et al., 2017; Valera et al., 2018; Kilbertus et al., 2019; Tabibian et al., 2020), we will assume that the decision maker is rational, has access to (an estimation of) the original feature distribution _P_ ( **_x_** ), and aims to maximize the (immediate) utility _u_ ( _π, γ_ ), which is the expected overall profit she obtains, _i.e._ , 



where _γ ∈_ (0 _,_ 1) is a given constant reflecting economic considerations of the decision maker. For example, in university admissions, the term _π_ ( **_x_** ) _P_ ( _y_ = 1 _|_ **_x_** ) is proportional to the expected number of students who are admitted and complete the program, the term _π_ ( **_x_** ) _γ_ is proportional to the number of students who are admitted, and _γ_ measures the cost of education in units of graduated students. As a direct consequence, given a feature value **_x_** _i_ and a set of counterfactual explanations _A_ , we can conclude that, if _R_ ( **_x_** _i_ ) _∩A̸_ = _∅_ , the decision maker will decide to provide the counterfactual explanation _E_ ( **_x_** _i_ ) that provides the largest utility gain under the assumption that individuals best respond, _i.e._ , 



and, if _R_ ( **_x_** _i_ ) _∩A_ = _∅_ , we arbitrarily assume that _E_ ( **_x_** _i_ ) = argmin **_x_** _∈A c_ ( **_x_** _i,_ **_x_** )<sup>6</sup> . 

> 4In practice, individuals with initial feature values **_x_** _i_ such that _π_ ( **_x_** ) = 1 may not receive any explanation since they are guaranteed to receive a positive decision. 

> 5In practice, the cost for each pair of feature values may be given by a parameterized function. 

> 6Note that, if _A ∩R_ ( **_x_** _i_ ) = _∅_ , the individual’s best response is to keep her initial feature value **_x_** _i_ and thus any choice of counterfactual explanation _E_ ( **_x_** _i_ ) leads to the same utility. 

3 

Given the above preliminaries, our goal is to help the decision maker to first find the optimal set of counterfactual explanations _A_ for a pre-defined policy in Section 3 and then both the optimal policy _π_ and set of counterfactual explanations _A_ in Section 4. 

**Remarks.** Given an individual with initial feature value **_x_** , one may think that, by providing the counterfactual explanation _E_ ( **_x_** ) _∈A ∩R_ ( **_x_** ) that gives the largest utility gain, the decision maker is not acting in the individual’s best interest but rather selfishly. This is because there may exist another counterfactual explanation _Em_ ( **_x_** ) _∈A ∩R_ ( **_x_** ) with lower cost for the individual, _i.e._ , _c_ ( **_x_** _, Em_ ( **_x_** )) _≤ c_ ( **_x_** _, E_ ( **_x_** )). In our work, we argue that the provided counterfactual explanations help the individual to achieve a greater self-improvement and this is likely to result in a superior long-term well-being, as illustrated in Figure 7(c) in Appendix E. For example, consider a bank issuing credit cards who wants to maintain credit for trustworthy customers and incentivize the more risky ones to improve their financial status. In this case, _E_ ( **_x_** ) is the explanation that maximally improves the financial status of the individual, making the repayment more likely, but requires her to pay a larger (immediate) cost. In contrast, _Em_ ( **_x_** ) is an alternate explanation that requires the individual to pay a smaller (immediate) cost but, in comparison with _E_ ( **_x_** ), would result in a higher risk of default. In this context, note that the individual would be “willing” to pay the cost of following either _E_ ( **_x_** ) or _Em_ ( **_x_** ) since both explanations lie within the region of adaptation _R_ ( **_x_** ). We refer the interested reader to Appendix F.2 for an anecdotal real-world example of _E_ ( **_x_** ) and _Em_ ( **_x_** ). 

As argued very recently (Kleinberg and Raghavan, 2019; Miller et al., 2019; Tabibian et al., 2020), due to Goodhart’s law, the conditional probability _P_ ( _y |_ **_x_** ) may change after individuals (best)-respond if the true causal effect between the observed features **_x_** and the outcome variable _y_ is partially described by unobserved features. Moreover, Miller et al. (2019) have argued that, to distinguish between gaming and improvement, it is necessary to have access to the full underlying causal graph between the features and the outcome variable. In this work, for simplicity, we assume that _P_ ( _y |_ **_x_** ) does not change, however, it would be very interesting to lift this assumption in future work. 

## **3 Finding the optimal counterfactual explanations for a policy** 

In this section, our goal is to find the optimal set of counterfactual explanations _A_<sup>_∗_</sup> for a pre-defined policy _π_ , _i.e._ , 



where the cardinality constraint on the set of counterfactual explanations balances the decision maker’s obligation to be transparent with trade secrets (Barocas et al., 2020). More specifically, note that, without this constraint, an adversary could reverse-engineer the entire decision policy _π_ ( **_x_** ) by impersonating individuals with different feature values **_x_** (css). 

As it will become clearer in the experimental evaluation in Section 6, our results may persuade decision makers to be transparent about their decision policies, something they are typically reluctant to be despite the increasing legal requirements, since we show that transparency increases the utility of the policies. Moreover, throughout this section, we will assume that the decision maker who picks the pre-defined policy is rational<sup>7</sup> and the policy is outcome monotonic<sup>89</sup> (Tabibian et al., 2020). Outcome monotonicity just implies that, the higher an individual’s outcome _P_ ( _y_ = 1 _|_ **_x_** ), the higher their chances of receiving a positive decision _π_ ( **_x_** ). 

Unfortunately, using a novel reduction of the Set Cover problem (Karp, 1972), the following theorem reveals that we cannot expect to find the optimal set of counterfactual explanations in polynomial time (proven in Appendix B.1): 

**Theorem 1** _The problem of finding the optimal set of counterfactual explanations that maximizes utility under a cardinality constraint is NP-Hard._ 

> 7Note that, if the decision maker is rational and her goal is to maximize the utility, as defined in Eq. 1, then, for all **_x_** _∈X_ such that _P_ ( _y_ = 1 _|_ **_x_** ) _< γ_ , it holds that _π_ ( **_x_** ) = 0. 

> 8A policy _π_ is called outcome monotonic if _P_ ( _y_ = 1 _|_ **_x_** _i_ ) _≥ P_ ( _y_ = 1 _|_ **_x_** _j_ ) _⇔ π_ ( **_x_** _i_ ) _≥ π_ ( **_x_** _j_ ) _∀_ **_x_** _i,_ **_x_** _j ∈X_ . 

> 9If the policy _π_ is deterministic, our results also hold for non outcome monotonic policies. 

4 

Even though Theorem 1 is a negative result, we will now show that the objective function in Eq. 3 satisfies a set of desirable properties, _i.e._ , non-negativity, monotonicity and submodularity<sup>10</sup> , which allow a standard greedy algorithm to enjoy approximation guarantees at solving the problem. To this aim, with a slight abuse of notation, we first express the objective function as a set function _f_ ( _A_ ) = _u_ ( _π, A_ ), which takes values over the ground set of counterfactual explanations, _Pπ_ . Then, we have the following proposition (proven in Appendix B.2): 

**Proposition 2** _The function f is non-negative, submodular and monotone._ 

The above result directly implies that the standard greedy algorithm (Nemhauser et al., 1978) for maximizing a non-negative, submodular and monotone function will find a solution _A_ to the problem such that _f_ ( _A_ ) _≥_ (1 _−_ 1 _/e_ ) _f_ ( _A_<sup>_∗_</sup> ), where _A_<sup>_∗_</sup> is the optimal set of counterfactual explanations. The algorithm starts from a solution set _A_ = _∅_ and it iteratively adds to _A_ the counterfactual explanation **_x_** _∈Pπ \ A_ that provides the maximum marginal difference _f_ ( _A∪{_ **_x_** _}_ ) _− f_ ( _A_ ). Algorithm 1 in Appendix C provides a pseudocode implementation of the algorithm. 

Finally, since the greedy algorithm computes the marginal difference of _f_ for at most _m_ elements per iteration and, following from the proof of Proposition 2, the marginal difference _f_ ( _A ∪{_ **_x_** _}_ ) _− f_ ( _A_ ) can be computed in _O_ ( _m_ ), then it immediately follows that, in our problem, the greedy algorithm has an overall complexity of _O_ ( _km_<sup>2</sup> ). 

## **4 Finding the optimal policy and counterfactual explanations** 

In this section, our goal is to jointly find the optimal decision policy and set of counterfactual explanations _A_<sup>_∗_</sup> , _i.e._ , 



where, similarly as in the previous section, _k_ is the maximum number of counterfactual explanations the decision maker is willing to provide to the population to balance the right to explanation with trade secrets. By jointly optimizing both the decision policy and the counterfactual explanations, we may obtain an additional gain in terms of utility in comparison with just optimizing for the set of counterfactual explanations given the optimal decision policy in a non-strategic setting, as shown in Figure 6 in Appendix D. Moreover, as we will show in the experimental evaluation in Section 6, this additional gain will be significant. 

Similarly as in Section 3, we cannot expect to find the optimal policy and set of counterfactual explanations in polynomial time. More specifically, we have the following negative result, which easily follows from Proposition 4 and slightly extending the proof of Theorem 1: 

**Theorem 3** _The problem of jointly finding both the optimal policy and the set of counterfactual explanations that maximize utility under a cardinality constraint is NP-hard._ 

However, while the problem of finding both the policy and the set of counterfactual explanations appears significantly more challenging than the problem of finding just the set of counterfactual explanations given a pre-defined policy (refer to Eq. 3), the following proposition shows that the problem is not inherently _harder_ . More specifically, for each possible set of counterfactual explanations, it shows that the policy that maximizes the utility can be easily computed (proven in Appendix B.3): 

**Proposition 4** _Given a set of counterfactual explanations A ⊆Y_ := _{_ **_x_** _∈X_ : _P_ ( _y_ = 1 _|_ **_x_** ) _≥ γ}_<sup>11</sup> _, the policy πA_<sup>_∗_=argmax</sup> _π_ : _A⊆Pπ_<sup>_u_(</sup><sup>_π, A_)</sup><sup>_thatmaximizestheutilityisdeterministicandcanbefoundin_</sup> _polynomial time,_ i.e. _,_ 



> 10A function _f_ : 2 _X →_ R is submodular if for every _A, B ⊆X_ : _A ⊆B_ and _x ∈X \ B_ it holds that _f_ ( _A ∪{x}_ ) _− f_ ( _A_ ) _≥ f_ ( _B ∪{x}_ ) _− f_ ( _B_ ). 

> 11Since the decision maker is rational, she will never provide an explanation that contributes negatively to her utility. 

5 

The above result implies that, to set all the values of the optimal decision policy, we only need to perform _O_ ( _km_ ) comparisons. Moreover, it reveals that, in contrast with the non strategic setting, the optimal policy given a set of counterfactual explanations is not a deterministic threshold rule with a single threshold (Corbett-Davies et al., 2017; Valera et al., 2018), _i.e._ , 



but rather a more conservative deterministic decision policy that does not depend only on the outcome _P_ ( _y_ = 1 _|_ **_x_** ) and _γ_ but also on the cost individuals pay to change features. Moreover, we can build up on the above result to prove that the problem of finding the optimal decision policy and set of counterfactual explanations can be reduced to maximizing a non-monotone submodular function. To this aim, let _πA_<sup>_∗_</sup> be the optimal policy induced by a given set of counterfactual explanations _A_ , as in Proposition 4, and define the set function _h_ ( _A_ ) = _u_ ( _πA_<sup>_∗, A_)overthegroundset</sup><sup>_Y_.Then,wehavethefollowingproposition</sup> (proven in Appendix B.4): 

**Proposition 5** _The function h is non-negative, submodular and non-monotone._ 

Fortunately, there exist efficient algorithms with global approximation guarantees for maximizing a non-monotone submodular function under cardinality constraints. In our work, we use the randomized polynomial time algorithm by Buchbinder et al. (2014), which can find a solution _A_ such that _h_ ( _A_ ) _≥_ (1 _/e_ ) _h_ ( _A_<sup>_∗_</sup> ), where _A_<sup>_∗_</sup> and _πA_<sup>_∗∗_aretheoptimalsetofcounterfactualexplanationsanddecisionpolicy,</sup> respectively. The algorithm is just a randomized variation of the standard greedy algorithm. It starts from a solution set _A_ = _∅_ and it iteratively adds one counterfactual explanation **_x_** _∈Y\A_ . However, instead of greedily choosing the element **_x_** that provides the maximum marginal difference _h_ ( _A ∪{_ **_x_** _}_ ) _− h_ ( _A_ ), it sorts all the candidate elements with respect to their marginal difference and picks one at random among the top _k_ . Algorithm 2 in Appendix C provides a pseudocode implementation of the algorithm. Finally, since the above randomized algorithm has a complexity of _O_ ( _km_ ) and, following from the proof of Proposition 5, the marginal difference of _h_ can be computed in _O_ ( _m_ ), it readily follows that, in our problem, the algorithm has a complexity of _O_ ( _km_<sup>2</sup> ). 

## **5 Increasing the diversity of the counterfactual explanations** 

In many cases, decision makers may like to ensure that individuals across the whole spectrum of the population are incentivized to self-improve. For example, in a loan scenario, the bank may use age group as a feature to estimate the probability that a customer repays the loan, however, it may like to deploy a decision policy that incentivizes individuals across all age groups in order to improve the financial situation of all. To this aim, the decision maker can increase the diversity of the optimal set of counterfactual explanations by incorporating a matroid constraint into the problem formulation, rather than a cardinality constraint. 

Formally, consider disjoint sets _X_ 1 _, X_ 2 _, . . . , Xl_ such that<sup>�</sup> _i_<sup>_Xi_=</sup><sup>_X_andintegers</sup><sup>_d_1</sup><sup>_, d_2</sup><sup>_, . . . , dl_such</sup> that _k_ =<sup>�</sup> _i_<sup>_di_.Then,apartitionmatroidisthecollectionofsets</sup><sup>_{S⊆_2</sup><sup>_X_:</sup><sup>_|S ∩Xi|≤di∀i∈_[</sup><sup>_l_]</sup><sup>_}_.In</sup> the loan example, the decision maker could search for a set of counterfactual explanations _A_ within a partition matroid where each one of the _Xi_ ’s corresponds to the feature values covered by each age group and _di_ = _k/l ∀i ∈_ [ _l_ ]. This way, the set of counterfactual explanations _A_ would include explanations for every age group. 

In this case, the decision maker could rely on a variety of polynomial time algorithms with global guarantees for submodular function maximization under matroid constraints, _e.g._ , the algorithm by Calinescu et al. (2011). 

## **6 Experiments** 

In this section, we evaluate Algorithms 1 and 2 using real loan and credit card data and show that the counterfactual explanations and decision policies found by our algorithms achieve higher utility than several competitive baselines. Appendix E contains additional experiments on synthetic data. 

6 

**Experimental setup.** We experiment with two publicly available datasets: (i) the _lending_ dataset (len), which contains information about all accepted loan applications in LendingClub during the 2007-2018 period and (ii) the _credit_ dataset (Yeh and Lien, 2009), which contains information about a bank’s credit card payoffs<sup>12</sup> . For each accepted loan applicant (or credit card holder), we use various demographic information and financial status indicators as features **_x_** and the current loan status (or credit payoff status) as label _y_ . Appendix F.1 contains more details on the specific features we used in each dataset and also describes the procedure we followed to approximate _P_ ( _y |_ **_x_** ). 

To set the values of the cost function _c_ ( **_x_** _i,_ **_x_** _j_ ), we use the maximum percentile shift among actionable features<sup>13</sup> , similarly as in Ustun et al. (2019). More specifically, let _L_ be the set of actionable (numerical) features and _L_<sup>¯</sup> be the set of non-actionable (discrete-valued) features<sup>14</sup> . Then, for each pair of feature values **_x_** _i,_ **_x_** _j_ we define the cost function as: 



where _xj,l_ is the value of the _l_ -th feature for the feature value **_x_** _j_ , _Ql_ ( _·_ ) is the CDF of the numerical feature _l ∈L_ and _α ≥_ 1 is a scaling factor. As an exception, in the credit dataset, we always set the cost _c_ ( **_x_** _i,_ **_x_** _j_ ) between two feature values to _∞_ if _Ql_ ( _xj,l_ ) _< Ql_ ( _xi,l_ ) for _l ∈{_ Total Overdue Counts _,_ Total Months Overdue _}_ considering the fact that history of overdue payments cannot be erased. In this context, we would like to acknowledge that more sophisticated cost functions can be designed in terms of feasibility and difficulty of adaptation, taking into account domain knowledge and information about the deployed classifier, however, it goes beyond the scope of our work. 

Finally, in our experiments, we compare the utility of the following decision policies and counterfactual explanations: 

— _Black box:_ decisions are taken by the optimal decision policy in the non-strategic setting, given by Eq. 6, and individuals do not receive any counterfactual explanations. 

— _Minimum cost:_ decisions are taken by the optimal decision policy in the non-strategic setting, given by Eq. 6, and individuals receive counterfactual explanations of minimum cost with respect to their initial feature values, similarly as in previous work (Ustun et al., 2019; Tolomei et al., 2017; Karimi et al., 2019). More specifically, we cast the problem of finding the set of counterfactual explanations as the minimization of the weighted average cost individuals pay to change their feature values to the closest counterfactual explanation, _i.e._ , 



and realize that this problem is a version of the k-median problem, which we can solve using a greedy heuristic (Solis-Oba, 2006). 

— _Diverse:_ decisions are taken by the optimal decision policy in the non-strategic setting, given by Eq. 6, and individuals receive a set of diverse counterfactual explanations of minimum cost with respect to their initial feature values, similarly as in previous work (Russell, 2019; Mothilal et al., 2020), _i.e._ , 



To solve the above problem, we realize it can be reduced to the weighted version of the maximum coverage problem, which can be solved using a well-known greedy approximation algorithm (Hochbaum and Pathria, 1998). 

— _Algorithm 1:_ decisions are taken by the optimal decision policy in the non-strategic setting, given by Eq. 6, and individuals receive counterfactual explanations given by Eq. 2, where _A_ is found using Algorithm 1. 

— _Algorithm 2:_ decisions are taken by the decision policy given by Eq. 5 and individuals receive counterfactual explanations given by Eq. 2, where _A_ is found using Algorithm 2. 

> 12We used a version of the credit dataset preprocessed by Ustun et al. (2019) 

> 13A feature is actionable if an individual can change its values in order to get a positive decision. 

> 14In the credit dataset, _L_ ¯ contains Marital Status, Age Group and Education Level and _L_ ¯ contains the remaining features and, in the lending dataset, _L_ contains all features. 

7 



<!-- Start of picture text -->
0 . 06<br>0 . 0225 Black box Black box<br>Minimum cost Minimum cost<br>0 . 0200 Diverse 0 . 05 Diverse<br>Algorithm 1 Algorithm 1<br>0 . 0175 Algorithm 2 Algorithm 2<br>0 . 04<br>0 . 0150<br>0 . 0125 0 . 03<br>0 . 0100<br>0 . 02<br>0 . 0075 10% 20% 30% 50% 100% 10% 20% 30% 50% 100%<br>Allowed percentile shift (1 /α ) Allowed percentile shift (1 /α )<br>(a) Lending dataset (b) Credit dataset<br>()  A Utility, uπ, ()  A Utility, uπ,<br><!-- End of picture text -->

Figure 1: Utility achieved by five types of decision policies and counterfactual explanations against the value of the parameter _α_ , in the lending and credit datasets. In panel (a), the number of feature values is _m_ = 400 and, in panel (b), it is _m_ = 3200. In both panels, we set _k_ = 0 _._ 05 _m_ and we repeat each experiment 20 times. 



<!-- Start of picture text -->
0.249 0.249 0.502 0.502 0 . 06<br>0 . 04<br>0 . 08 0 . 08 0 . 05<br>0.847 0.847 0.763 0.763<br>0 . 06 0 . 06 0 . 03 0 . 04<br>0.975 0.975 0.858 0.858<br>0 . 04 0 . 04 0 . 02 0 . 03<br>0.991 0.991 0.887 0.887 0 . 02<br>0.996 0 . 02 0.996 0 . 02 0.916 0 . 01 0.916 0 . 01<br>0.249 0.847 0.975 0.991 0.996 0 . 00 0.249 0.847 0.975 0.991 0.996 0 . 00 0.502 0.763 0.858 0.887 0.916 0 . 00 0.502 0.763 0.858 0.887 0.916 0 . 00<br>Final P ( y = 1  |  x ) Final P ( y = 1  |  x ) Final P ( y = 1  |  x ) Final P ( y = 1  |  x )<br>(a) Alg. 1, lending (b) Alg. 2, lending (c) Alg. 1, credit (d) Alg. 2, credit<br> | ()Initial P = 1  x y  | ()Initial P = 1  x y  | ()Initial P = 1  x y  | ()Initial P = 1  x y<br><!-- End of picture text -->

Figure 2: Transportation of mass induced by the policies and counterfactual explanations used in Algorithm 1 and 2 in both the lending and the credit dataset. For each individual in the population, whose best-response is to change her feature value, we record her outcome _P_ ( _y_ = 1 _|_ **_x_** ) before the best response (Initial _P_ ( _y_ = 1 _|_ **_x_** )) and after the best response (Final _P_ ( _y_ = 1 _|_ **_x_** )). In each panel, the color is proportional to the percentage of individuals who move from initial _P_ ( _y_ = 1 _|_ **_x_** ) to final _P_ ( _y_ = 1 _|_ **_x_** ) and we set _α_ = 2. 

**Results.** We start by comparing the utility achieved by each of the decision policies and counterfactual explanations in both datasets, for several values of the parameter _α_ , which is proportional to the difficulty of changing features. Figure 1 summarizes the results, which show that Algorithm 1 and Algorithm 2 consistently outperform all baselines and, as the cost of adapting to feature values with higher outcome values decreases (smaller _α_ ), the competitive advantage by jointly optimizing the decision policy and the counterfactual explanations (Algorithm 2) grows significantly. This competitive advantage is more apparent in the credit card dataset because it contains non actionable features ( _e.g._ , credit overdue counts) and, under the optimal decision policy in the non-strategic setting, it is difficult to incentivize individuals who receive a negative decision to improve by just optimizing the set of counterfactual explanations they receive. For specific examples of counterfactual explanations provided by Algorithm 1 and the minimum cost baseline, refer to Appendix F.2. 

To understand the differences in utility caused by the two proposed algorithms, we measure the transportation of mass induced by the policies and counterfactual explanations used in Algorithm 1 and 2 in both datasets, as follows. For each individual in the population whose best-response is to change her feature value, we record her outcome _P_ ( _y_ = 1 _|_ **_x_** ) before and after the best response. Then, we discretize the outcome values using percentiles. Figure 2 summarizes the results, which show several interesting insights. In the lending dataset, we observe that a large portion of individuals do improve their outcome even if we only optimize the counterfactual explanations (Panel (a)). In contrast, in the credit dataset, we observe that, if we only optimize the counterfactual explanations (Panel (c)), most individuals do not improve their outcome. That being said, if we jointly optimize the decision policy and counterfactual explanations (Panels (b) and (d)), we are able to incentivize a large portion of individuals to self improve in both datasets. 

Next, we focus on the lending dataset and evaluate the sensitivity of our algorithms. First, we measure the influence that the number of counterfactual explanations has on the utility achieved by each of the 

8 



<!-- Start of picture text -->
0 . 020 Black box 0 . 020<br>0 . 018 MinimumDiverse cost 0 . 018<br>0 . 016 AlgorithmAlgorithm 12 0 . 016<br>0 . 014 0 . 014<br>0 . 012 0 . 012 Black box<br>0 . 010 0 . 010 AlgorithmAlgorithm 22 -- ppll == 0.10.5<br>Algorithm 2 - pl = 0.9<br>0 . 008 0 . 008<br>0 2 4 10 20 0 4 10 20 40 100<br>k k<br>(a) Utility vs. k (b) Utility vs. k under leakage<br>()  A Utility, uπ, ()  A Utility, uπ,<br><!-- End of picture text -->

Figure 3: Number of counterfactual explanations and information leakage. Panel (a) shows the utility achieved by five types of decision policies and counterfactual explanations against the number of counterfactual explanations _k_ . Panel (b) shows the utility achieved by Algorithm 2 against the number of counterfactual explanations _k_ for several values of the leakage probability _pl_ . In both panels, we use the lending dataset, the number of feature values is _m_ = 400, we set _α_ = 2, we repeat each experiment involving randomization 20 times. 



<!-- Start of picture text -->
0 . 25 16 Cardinality 0 . 030 Cardinality<br>Matroid 0 . 025 Matroid<br>0 . 20 12<br>0 . 020<br>0 . 15<br>8 0 . 015<br>0 . 10 0 . 010<br>4<br>0 . 05 0 . 005<br>0 . 00 Under 25 25 - 39 40 - 59 Over 59 Under 25 25 - 39 40 - 59 Over 59 0 . 000 Under 25 25 - 39 40 - 59 Over 59<br>Age group Age group Age group<br>(a) Rejected population by age (b) Explanations by age (c) Relative improvement by age<br>Population Explanations<br>Relativeimprovement<br><!-- End of picture text -->

Figure 4: Increasing the diversity of the provided counterfactual explanations. Panel (a) shows the population per age group, rejected by the optimal threshold policy in the non strategic setting. Panel (b) shows a comparison of the age distribution of counterfactual explanations in _A_ produced by the greedy algorithm under a cardinality and a matroid constraint. Panel (c) shows the relative improvement of each age group. In all panels, we use the credit dataset and we set _k_ = 32 and _α_ = 2. 

decision policies and counterfactual explanations. As shown in Figure 3(a), our algorithms just need a small number of counterfactual explanations to provide significant gains in terms of utility with respect to all the baselines. Second, we challenge the assumption that individuals do not share the counterfactual explanations they receive with other individuals with different feature values. To this end, we assume that, given the set of counterfactual explanations _A_ found by Algorithm 2, individuals with initial feature value **_x_** receive the counterfactual explanation _E_ ( **_x_** ) _∈A_ given by Eq. 2 and, with probability _pl_ , they also receive an additional explanation _E_<sup>_′_</sup> ( **_x_** ) picked at random from _A_ and they follow the counterfactual explanation that benefits them the most. Figure 3(b) summarizes the results for several values of _pl_ and number of counterfactual explanations, which show that the policies and explanations provided by Algorithm 2 present a significant utility advantage even when the leakage probability _pl_ is large. 

Finally, we focus on the credit dataset and consider a scenario in which a bank aims not only to continue providing credit to the customers that are more likely to repay but also provide explanations that incentivize individuals across all age groups to maintain their credit. To this end, we incorporate a partition matroid constraint that ensures the counterfactual explanations are diverse across age groups, as described in Section 5, and use a slightly modified version of Algorithm 1 to solve the constrained problem (Nemhauser et al., 1978), which enjoys a 1 _/_ 2 approximation guarantee. Figure 4 summarizes the results, which show that: (i) optimizing under a cardinality constraint leads to an unbalanced set of explanations, favoring the more populated age groups (25 to 59) while completely ignoring the recourse potential of individuals older than 60; (ii) the relative group improvement, defined as<sup>�</sup> **_x_** _i∈Xz\Pπ_<sup>_P_(</sup><sup>**_x_**</sup><sup>_i_)[</sup><sup>_P_(</sup><sup>_y |_</sup><sup>**_x_**</sup> _j_<sup>_i_)</sup><sup>_−P_(</sup><sup>_y |_</sup><sup>**_x_**</sup><sup>_i_)]</sup><sup>_/_�</sup> **_x_** _i∈Xz\Pπ_<sup>_P_(</sup><sup>**_x_**</sup><sup>_i_),where</sup><sup>_Xz_isthesetoffeaturevaluescor-</sup> responding to age group _z_ and **_x_**<sup>_i_</sup> _j_<sup>isthebestresponseofindividualswithinitialfeaturevalue</sup><sup>**_x_**</sup><sup>_i∈Xz_,</sup> is more balanced across age groups, showing that the matroid constraint can be used to generate counterfactual explanations that help the entire spectrum of the population to self-improve. 

9 

## **7 Conclusions** 

In this paper, we have designed several algorithms that allow us to find the decision policies and counterfactual explanations that maximize utility in a setting in which individuals who are subject to the decisions taken by the policies use the counterfactual explanations they receive to invest effort strategically. Moreover, we have experimented with synthetic and real lending and credit card data and shown that the counterfactual explanations and decision policies found by our algorithms achieve higher utility than several competitive baselines. 

By uncovering a previously unexplored connection between strategic machine learning and interpretable machine learning, our work opens up many interesting directions for future work. For example, we have adopted a specific type of mechanism to provide counterfactual explanations ( _i.e._ , one feature value per individual using a Stackelberg formulation). A natural next step would be to extend our analysis to other types of mechanisms fitting a variety of real-world applications. Moreover, we have assumed that the cost individuals pay to change features is given. However, our algorithms would be more effective if we develop a methodology to reliably estimate the cost function from real observational (or interventional) data. In our work, we have assumed that features take discrete values and individuals who are subject to the decisions do not share information between them. It would be interesting to lift these assumptions, extend our analysis to real-valued feature values, and develop decision policies and counterfactual explanations that are robust to information sharing between individuals (refer to Figure 3(c)). Finally, by assuming that _P_ ( _y |_ **_x_** ) does not change after individuals best respond, we are implicitly assuming that there are not unobserved features that partially describe the true causal effect between the observed features **_x_** and the outcome variable _y_ . However, in practice, this assumption is likely to be violated and _P_ ( _y |_ **_x_** ) may change after individuals best respond, as recently noted by Miller et al. (2019). In this context, it would be very interesting to find counterfactual explanations that are robust to unmeasured confounding. 

## **References** 

Credit score simulator. https://www.creditkarma.com/tools/credit-score-simulator/. 

- Lending club dataset. https://www.kaggle.com/wordsforthewise/lending-club/version/3. 

- Solon Barocas, Andrew D Selbst, and Manish Raghavan. The hidden assumptions behind counterfactual explanations and principal reasons. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , pages 80–89, 2020. 

- Michael Br¨uckner and Tobias Scheffer. Stackelberg games for adversarial prediction problems. In _Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 547–555, 2011. 

- Niv Buchbinder, Moran Feldman, Joseph Naor, and Roy Schwartz. Submodular maximization with cardinality constraints. In _Proceedings of the twenty-fifth annual ACM-SIAM symposium on Discrete algorithms_ , pages 1433–1452. SIAM, 2014. 

- Gruia Calinescu, Chandra Chekuri, Martin Pal, and Jan Vondr´ak. Maximizing a monotone submodular function subject to a matroid constraint. _SIAM Journal on Computing_ , 40(6):1740–1766, 2011. 

- Supriyo Chakraborty, Richard Tomsett, Ramya Raghavendra, Daniel Harborne, Moustafa Alzantot, Federico Cerutti, Mani Srivastava, Alun Preece, Simon Julier, Raghuveer M Rao, et al. Interpretability of deep learning models: a survey of results. In _2017 IEEE SmartWorld, Ubiquitous Intelligence & Computing, Advanced & Trusted Computed, Scalable Computing & Communications, Cloud & Big Data Computing, Internet of People and Smart City Innovation (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI)_ , pages 1–6. IEEE, 2017. 

- S. Coate and G. Loury. Will affirmative-action policies eliminate negative stereotypes? _The American Economic Review_ , 1993. 

10 

- Sam Corbett-Davies, Emma Pierson, Avi Feller, Sharad Goel, and Aziz Huq. Algorithmic decision making and the cost of fairness. In _Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 797–806, 2017. 

- Nilesh Dalvi, Pedro Domingos, Sumit Sanghai, and Deepak Verma. Adversarial classification. In _Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 99–108, 2004. 

- Jinshuo Dong, Aaron Roth, Zachary Schutzman, Bo Waggoner, and Zhiwei Steven Wu. Strategic classification from revealed preferences. In _Proceedings of the 2018 ACM Conference on Economics and Computation_ , pages 55–70, 2018. 

- Finale Doshi-Velez and Been Kim. Towards a rigorous science of interpretable machine learning. _arXiv preprint arXiv:1702.08608_ , 2017. 

- R. Fryer and G. Loury. Valuing diversity. _Journal of Political Economy_ , 2013. 

- David Gunning and David W Aha. Darpa’s explainable artificial intelligence program. _AI Magazine_ , 40 (2):44–58, 2019. 

- Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic classification. In _Proceedings of the 2016 ACM conference on innovations in theoretical computer science_ , pages 111–122, 2016a. 

- Moritz Hardt, Eric Price, and Nati Srebro. Equality of opportunity in supervised learning. In _Advances in neural information processing systems_ , pages 3315–3323, 2016b. 

- Dorit S Hochbaum and Anu Pathria. Analysis of the greedy approach in problems of maximum k- coverage. _Naval Research Logistics (NRL)_ , 45(6):615–627, 1998. 

- L. Hu and Y. Chen. A short-term intervention for long-term fairness in the labor market. In _WWW_ , 2018. 

- Lily Hu, Nicole Immorlica, and Jennifer Wortman Vaughan. The disparate effects of strategic manipulation. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 259–268, 2019. 

- Amir-Hossein Karimi, Gilles Barthe, Borja Belle, and Isabel Valera. Model-agnostic counterfactual explanations for consequential decisions. _arXiv preprint arXiv:1905.11190_ , 2019. 

- Richard M Karp. Reducibility among combinatorial problems. In _Complexity of computer computations_ , pages 85–103. Springer, 1972. 

- Niki Kilbertus, Manuel Gomez-Rodriguez, Bernhard Sch¨olkopf, Krikamol Muandet, and Isabel Valera. Fair decisions despite imperfect predictions. In _AISTATS_ , 2019. 

- Jon Kleinberg and Manish Raghavan. How do classifiers induce agents to invest effort strategically? In _Proceedings of the 2019 ACM Conference on Economics and Computation_ , pages 825–844, 2019. 

- Jon Kleinberg, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, and Sendhil Mullainathan. Human decisions and machine predictions. _The quarterly journal of economics_ , 133(1):237–293, 2018. 

- Pang Wei Koh and Percy Liang. Understanding black-box predictions via influence functions. In _Proceedings of the 34th International Conference on Machine Learning_ , 2017. 

- Zachary C Lipton. The mythos of model interpretability. _Queue_ , 16(3):31–57, 2018. 

- Lydia T Liu, Sarah Dean, Esther Rolf, Max Simchowitz, and Moritz Hardt. Delayed impact of fair machine learning. In _Advances in neural information processing systems_ , 2018. 

- Scott M Lundberg and Su-In Lee. A unified approach to interpreting model predictions. In _Advances in neural information processing systems_ , 2017. 

11 

- John Miller, Smitha Milli, and Moritz Hardt. Strategic adaptation to classifiers: A causal perspective. _arXiv preprint arXiv:1910.10362_ , 2019. 

- Smitha Milli, John Miller, Anca D Dragan, and Moritz Hardt. The social cost of strategic classification. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 230–239, 2019. 

- Shira Mitchell, Eric Potash, Solon Barocas, Alexander D’Amour, and Kristian Lum. Predictionbased decisions and fairness: A catalogue of choices, assumptions, and definitions. _arXiv preprint arXiv:1811.07867_ , 2018. 

- Ramaravind K. Mothilal, Amit Sharma, and Chenhao Tan. Explaining machine learning classifiers through diverse counterfactual explanations. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , 2020. 

- W James Murdoch, Chandan Singh, Karl Kumbier, Reza Abbasi-Asl, and Bin Yu. Definitions, methods, and applications in interpretable machine learning. _Proceedings of the National Academy of Sciences_ , 116(44):22071–22080, 2019. 

- George L Nemhauser, Laurence A Wolsey, and Marshall L Fisher. An analysis of approximations for maximizing submodular set functions—i. _Mathematical programming_ , 14(1):265–294, 1978. 

- Juan C Perdomo, Tijana Zrnic, Celestine Mendler-D¨unner, and Moritz Hardt. Performative prediction. _arXiv preprint arXiv:2002.06673_ , 2020. 

- Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why should i trust you? explaining the predictions of any classifier. In _Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining_ , 2016. 

- Cynthia Rudin. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. _Nature Machine Intelligence_ , 1(5):206–215, 2019. 

- Chris Russell. Efficient search for diverse coherent explanations. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 20–28, 2019. 

- Roberto Solis-Oba. Approximation algorithms for the k-median problem. In _Efficient Approximation and Online Algorithms_ , pages 292–320. Springer, 2006. 

- Behzad Tabibian, Stratis Tsirtsis, Moein Khajehnejad, Adish Singla, Bernhard Sch¨olkopf, and Manuel Gomez-Rodriguez. Optimal decision making under strategic behavior. _Arxiv:1905.09239_ , 2020. 

- Gabriele Tolomei, Fabrizio Silvestri, Andrew Haines, and Mounia Lalmas. Interpretable predictions of tree-based ensembles via actionable feature tweaking. In _Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining_ , pages 465–474, 2017. 

- Berk Ustun, Alexander Spangher, and Yang Liu. Actionable recourse in linear classification. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ , pages 10–19, 2019. 

- Isabel Valera, Adish Singla, and Manuel Gomez Rodriguez. Enhancing the accuracy and fairness of human decision making. In _Advances in Neural Information Processing Systems_ , pages 1769–1778, 2018. 

- Paul Voigt and Axel Von dem Bussche. The eu general data protection regulation (gdpr). _A Practical Guide, 1st Ed., Cham: Springer International Publishing_ , 2017. 

- Sandra Wachter, Brent Mittelstadt, and Luciano Floridi. Why a right to explanation of automated decision-making does not exist in the general data protection regulation. _International Data Privacy Law_ , 7(2):76–99, 2017a. 

- Sandra Wachter, Brent Mittelstadt, and Chris Russell. Counterfactual explanations without opening the black box: Automated decisions and the gdpr. _Harv. JL & Tech._ , 31:841, 2017b. 

- Adrian Weller. Challenges for transparency. 2017. 

- I-Cheng Yeh and Che-hui Lien. The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. _Expert Systems with Applications_ , 36(2):2473–2480, 2009. 

12 

## **A Further related work** 

Our work builds upon previous work on interpretable machine learning, and strategic machine learning. 

Most previous work on interpretable machine learning has focused on one of the two following types of explanations: feature-based explanations (Ribeiro et al., 2016; Koh and Liang, 2017; Lundberg and Lee, 2017) or counterfactual explanations (Wachter et al., 2017b; Ustun et al., 2019; Karimi et al., 2019; Mothilal et al., 2020). Feature-based explanations help individuals understand the importance each feature has on a particular prediction, typically through local approximation, while counterfactual explanations help them understand what features would have to change for a predictive model to make a positive prediction about them. While there is not yet an agreement on what constitutes a _good_ post-hoc explanation in the literature on interpretable machine learning, counterfactual explanations are gaining prominence because they place no constraints on the model complexity, do not require model disclosure, facilitate actionable recourse, and seem to automate compliance with the law (Barocas et al., 2020). Motivated by these desirable properties, our work focuses on counterfactual explanations and sheds light on the possibility of using explanations to increase the utility of a decision policy, uncovering a previously unexplored connection between interpretable machine learning and the nascent field of strategic machine learning. 

Similarly as in our work, previous work on strategic machine learning also assumes that individuals may use knowledge, gained by transparency, to invest effort strategically in order to receive either a positive prediction (Br¨uckner and Scheffer, 2011; Dalvi et al., 2004; Dong et al., 2018; Hardt et al., 2016a; Hu et al., 2019; Milli et al., 2019; Miller et al., 2019; Perdomo et al., 2020) or a beneficial decision (Kleinberg and Raghavan, 2019; Tabibian et al., 2020). However, none of this previous work focuses on finding (counterfactual) explanations and they assume full transparency—individuals who are subject to (semi)-automated decision making can observe the entire predictive model or the decision policy. As a result, their formulation is fundamentally different and their technical contributions are orthogonal to ours. 

## **B Proofs** 

### **B.1 Proof of Theorem 1** 

Consider an instance of the Set Cover problem with a set of elements _U_ = _{u_ 1 _, . . . , un}_ and a collection _S_ = _{S_ 1 _, . . . , Sm} ⊆_ 2<sup>_U_</sup> such that<sup>�</sup> _i∈_ [ _m_ ]<sup>_Si_=</sup><sup>_U_.In the decision version of the problem, given a constant</sup> _k_ , we need to answer the question whether there are at most _k_ sets from the collection _S_ such that their union is equal to _U_ or not. With the following procedure, we show that any instance of that problem can be transformed to an instance of the problem of finding the optimal set of counterfactual explanations, defined in Eq. 3, in polynomial time. 

Consider _n_ + _m_ feature values corresponding to the _n_ elements of _U_ and the _m_ sets of _S_ . Moreover, denote the first _n_ feature values as **_x_** _u_ 1 _, . . . ,_ **_x_** _un_ and the remaining _m_ as **_x_** _S_ 1 _, . . . ,_ **_x_** _Sm_ . We set the decision maker’s parameter _γ_ to some positive constant less than 1. Then, we set the outcome probabilities _P_ ( _y_ = 1 _|_ **_x_** _ui_ ) = _γ ∀i ∈_ [ _n_ ] and _P_ ( _y_ = 1 _|_ **_x_** _Si_ ) = 1 _∀i ∈_ [ _m_ ] and the policy values _π_ ( **_x_** _ui_ ) = 0 _∀i ∈_ [ _n_ ] and _π_ ( **_x_** _Si_ ) = 1 _∀i ∈_ [ _m_ ]. This way, the portion of utility the decision-maker obtains from the first _n_ feature values is zero, while the portion of utility she obtains from the remaining _m_ is proportional to 1 _− γ_ . Regarding the cost function, we set _c_ ( **_x_** _ui,_ **_x_** _Sj_ ) = 0 _∀_ ( **_x_** _ui,_ **_x_** _Sj_ ) : _ui ∈ Sj_ , _c_ ( **_x_** _ui,_ **_x_** _ui_ ) = 0 _∀i ∈_ [ _n_ ], and all the remaining values of the cost function to 2. Finally, we set the initial feature value distribution to _P_ ( **_x_** _ui_ ) = _n_<sup><u>1</u></sup><sup>_∀i∈_[</sup><sup>_n_]and</sup><sup>_P_(</sup><sup>**_x_**</sup><sup>_Si_)=0</sup><sup>_∀i∈_[</sup><sup>_m_].Atoyexampleofthistransformationispresentedin</sup> Figure 5. 

In this setting, it easy to observe that an individual with initial feature value **_x_** _ui_ is always rejected at first and has the ability to move to a new feature value **_x_** _Sj_ recommended to her iff _c_ ( **_x_** _ui,_ **_x_** _Sj_ ) _≤_ 1 _⇔ ui ∈Sj_ . Also, we can easily see that the transformation of instances can be done in _O_ (( _m_ + _n_ )<sup>2</sup> ) time. 

Now, assume there exists an algorithm that optimally solves the problem of finding the optimal set of counterfactual explanations in polynomial time. Given the aforementioned instance and a maximum number of counterfactual explanations _k_ , the utility _u_ ( _π, A_ ) achieved by the set of counterfactual explanations _A_ the algorithm returns can fall into one of the following two cases: 

1. _u_ ( _π, A_ ) = 1 _− γ_ . This can happen only if all individuals, according to the induced distribution _P_ ( **_x_** _| π, A_ ), have moved to some of the feature values **_x_** _Sj_ , _i.e._ , for all **_x_** _ui_ with _i ∈_ [ _n_ ], there exists **_x_** _Sj_ with _j ∈_ [ _m_ ] such that **_x_** _Sj ∈A ∧ c_ ( **_x_** _ui,_ **_x_** _Sj_ ) _≤_ 1 with _|A| ≤ k_ . As a consequence, if we define 

13 



<!-- Start of picture text -->
0 0 0 0<br>u 1 u 2 S 1 S 2<br>2<br>0<br>0<br>0<br><!-- End of picture text -->

Figure 5: Consider that _U_ = _{u_ 1 _, u_ 2 _}_ and _S_ = _{S_ 1 _, S_ 2 _}_ with _S_ 1 = _{u_ 1 _, u_ 2 _}_ , _S_ 2 = _{u_ 2 _}_ . The red feature values have initial population _P_ ( **_x_** ) = 1 _/_ 2, _π_ ( **_x_** ) = 0 and _P_ ( _y_ = 1 _|_ **_x_** ) = _γ_ while for the green feature values it is _P_ ( **_x_** ) = 0, _π_ ( **_x_** ) = 1 and _P_ ( _y_ = 1 _|_ **_x_** ) = 1. The edges represent the cost between feature values corresponding to sets and their respective elements while all the non-visible pairwise costs are equal to 2. 

   - _S_<sup>_′_</sup> = _{Sj_ : **_x_** _Sj ∈A}_ , it holds that for all _ui_ with _i ∈_ [ _n_ ], there exists _Sj_ with _j ∈_ [ _m_ ] such that _Sj ∈S_<sup>_′_</sup> _∧ ui ∈Sj_ and therefore _S_<sup>_′_</sup> is a set cover with _|S_<sup>_′_</sup> _|_ = _|A| ≤ k_ . 

2. _u_ ( _π, A_ ) _<_ 1 _− γ_ . This can happen only if every possible set of _k_ counterfactual explanations leaves the individuals of at least one feature value **_x_** _ui_ with a best-response of not following the counterfactual explanation they were given, _i.e._ , for all _A ⊆Pπ_ such that _|A| ≤ k_ , there exists **_x_** _ui_ with _i ∈_ [ _n_ ] such that, for all **_x_** _Sj ∈A_ , it holds that _c_ ( **_x_** _ui,_ **_x_** _Sj_ ) _>_ 1. Equivalently, it holds that for all _S_<sup>_′_</sup> _⊆S_ such that _|S_<sup>_′_</sup> _| ≤ k_ , there exists _ui_ with _i ∈_ [ _n_ ] such that for all _Sj ∈S_<sup>_′_</sup> , it holds that _ui̸ ∈Sj_ and therefore there does not exist a set cover of size less or equal than _k_ . 

The above directly implies that we can have a decision about any instance of the Set Cover problem in polynomial time, which is a contradiction unless _P_ = _NP_ . This concludes the reduction and proves that the problem of finding the optimal set of counterfactual explanations for a given policy is NP-Hard. 

### **B.2 Proof of Proposition 2** 

It readily follows that the function _f_ is non-negative from the fact that, if the decision maker is rational, it holds that _π_ ( **_x_** ) = 0 for all **_x_** _∈X_ such that _P_ ( _y_ = 1 _|_ **_x_** ) _< γ_ . 

Now, consider two sets _A, B ⊆Pπ_ : _A ⊆B_ and a feature value **_x_** _∈Pπ \ B_ . Also, let _ES_ ( **_x_** _i_ ) be the counterfactual explanation given to the individuals with initial feature value **_x_** _i_ under a set of counterfactual explanations _S_ . It is easy to see that the marginal difference _f_ ( _S ∪{_ **_x_** _}_ ) _− f_ ( _S_ ) can only be affected by individuals with initial features **_x_** _i_ such that **_x_** _i̸ ∈Pπ_ , **_x_** _∈R_ ( **_x_** _i_ ) and **_x_** = _ES∪{_ **_x_** _}_ ( **_x_** _i_ ). Moreover, we can divide all of these individuals into two cases: 

1. _R_ ( **_x_** _i_ ) _∩A_ = _∅_ : in this case, the addition of **_x_** to _A_ causes a change in their best-response from **_x_** _i_ to **_x_** contributing to the marginal difference of _f_ by a factor _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− γ − π_ ( **_x_** _i_ )( _P_ ( _y_ = 1 _|_ **_x_** _i_ ) _− γ_ )]. However, considering the marginal difference of _f_ under the set of counterfactual explanations _B_ , three subcases are possible: 

   - (a) _EB_ ( **_x_** _i_ ) _∈R_ ( **_x_** _i_ ) _∧P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _> P_ ( _y_ = 1 _|_ **_x_** ): the contribution to the marginal difference of _f_ is zero. 

   - (b) _EB_ ( **_x_** _i_ ) _∈R_ ( **_x_** _i_ ) _∧P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _≤ P_ ( _y_ = 1 _|_ **_x_** ): the contribution to the marginal difference of _f_ is _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ ))]. Since _π_ is outcome monotonic, _EB_ ( **_x_** _i_ ) _∈Pπ_ and **_x_** _i̸ ∈Pπ_ , it holds that 

      - _P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _≥ P_ ( _y_ = 1 _|_ **_x_** _i_ ) _⇒_ 

_P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _− γ ≥ P_ ( _y_ = 1 _|_ **_x_** _i_ ) _− γ > π_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** _i_ ) _− γ_ ] _._ 

Therefore, it readily follows that 

- _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ ))] _< P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− γ − π_ ( **_x_** _i_ )( _P_ ( _y_ = 1 _|_ **_x_** _i_ ) _− γ_ )] _._ 

14 

   - (c) _R_ ( **_x_** _i_ ) _∩B_ = _∅_ : the contribution to the marginal difference of _f_ is _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− γ − π_ ( **_x_** _i_ )( _P_ ( _y_ = 1 _|_ **_x_** _i_ ) _− γ_ )]. 

2. _R_ ( **_x_** _i_ ) _∩A̸_ = _∅∧ P_ ( _y_ = 1 _|_ **_x_** ) _> P_ ( _y_ = 1 _| EA_ ( **_x_** _i_ )): In this case, the addition of **_x_** to _A_ causes a change in their best-response from _EA_ ( **_x_** _i_ ) to **_x_** contributing to the marginal difference of _f_ by a factor _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EA_ ( **_x_** _i_ ))]. Considering the marginal difference of _f_ under the set of counterfactual explanations _B_ , two subcases are possible: 

   - (a) _EB_ ( **_x_** _i_ ) _∈R_ ( **_x_** _i_ ) _∧P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _> P_ ( _y_ = 1 _|_ **_x_** ): the contribution to the marginal difference of _f_ is zero. 

   - (b) _EB_ ( **_x_** _i_ ) _∈R_ ( **_x_** _i_ ) _∧P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _≤ P_ ( _y_ = 1 _|_ **_x_** ). Then, the contribution of those individuals to the marginal difference of _f_ is _P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ ))]. Since _A ⊆B_ and _R_ ( **_x_** _i_ ) _∩A̸_ = _∅_ , it readily follows that 

_P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ )) _≥ P_ ( _y_ = 1 _| EA_ ( **_x_** _i_ )) _⇒_ 

_P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EA_ ( **_x_** _i_ ))] _≥ P_ ( **_x_** _i_ )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** _i_ ))] _._ 

Finally, because _A ⊆B_ , we can conclude that _f_ ( _B ∪{_ **_x_** _}_ ) _− f_ ( _B_ ) _̸_ = 0 _⇒ f_ ( _A ∪{_ **_x_** _}_ ) _− f_ ( _A_ ) _̸_ = 0 and therefore the aforementioned cases are sufficient. Combining all cases, we can see that the contribution of each individual to the marginal difference of _f_ is always greater or equal under the set of counterfactual explanations _A_ than under the set of counterfactual explanations _B_ . As a direct consequence, it follows that _f_ is submodular. Additionally, we can easily see that this contribution is always greater or equal than zero, leading to the conclusion that _f_ is also monotone. 

### **B.3 Proof of Proposition 4** 

By definition, since _A ⊆PπA_<sup>_∗_,itreadilyfollowsthat</sup><sup>_π_</sup> _A_<sup>_∗_(</sup><sup>**_x_**)=1forall</sup><sup>**_x_**</sup><sup>_∈A_.Tofindtheremaining</sup> values of the decision policy, we first observe that, for each **_x_** _∈A/_ , the value of the decision policy _πA_<sup>_∗_(</sup><sup>**_x_**)</sup> does not affect the best-responses of the individuals with initial feature values **_x_**<sup>_′̸_</sup> = **_x_** . As a result, we can just set _πA_<sup>_∗_(</sup><sup>**_x_**)forall</sup><sup>**_x_**</sup><sup>_∈A/_independentlyforeachfeaturevalue</sup><sup>**_x_**suchthatthebest-responseof</sup> the respective individuals is the one that contributes maximally to the overall utility. 

First, it is easy to see that, for all **_x_** _∈A/_ such that _P_ ( _y_ = 1 _|_ **_x_** ) _< γ_ , we should set _πA_<sup>_∗_(</sup><sup>**_x_**) = 0.Next,</sup> consider the feature values **_x_** _∈A/_ such that _P_ ( _y_ = 1 _|_ **_x_** ) _≥ γ_ . Here, we distinguish two cases. If there exists **_x_**<sup>_′_</sup> _∈A_ such that _c_ ( **_x_** _,_ **_x_**<sup>_′_</sup> ) _≤_ 1 _∧ P_ ( _y_ = 1 _|_ **_x_**<sup>_′_</sup> ) _> P_ ( _y_ = 1 _|_ **_x_** ), then, if the individuals move to that **_x_**<sup>_′_</sup> , the corresponding contribution to the utility will be higher. Moreover, the value of the decision policy that maximizes their region of adaption (and thus increases their chances of moving to **_x_**<sup>_′_</sup> ) is clearly _πA_<sup>_∗_(</sup><sup>**_x_**)=0.Iftheredoesnotexist</sup><sup>**_x_**</sup><sup>_′∈A_suchthat</sup><sup>_c_(</sup><sup>**_x_**</sup><sup>_,_</sup><sup>**_x_**</sup><sup>_′_)</sup><sup>_≤_1</sup><sup>_∧P_(</sup><sup>_y_=1</sup><sup>_|_</sup><sup>**_x_**</sup><sup>_′_)</sup><sup>_>P_(</sup><sup>_y_=1</sup><sup>_|_</sup><sup>**_x_**),</sup> then, the contribution of the corresponding individuals to the utility will be higher if they keep their initial feature values. Moreover, the value of the decision policy that will maximize this contribution will be clearly _πA_<sup>_∗_(</sup><sup>**_x_**) = 1.</sup> 

### **B.4 Proof of Proposition 5** 

It readily follows that the function _h_ is non-negative from the fact that, if the decision maker is rational, _π_ ( **_x_** ) = 0 for all **_x_** _∈X_ such that _P_ ( _y_ = 1 _|_ **_x_** ) _< γ_ . 

Next, consider two sets _A, B ⊆Y_ such that _A ⊆B_ and a feature value **_x_** _∈Y \ B_ . Also, let _ES_ ( **_x_** _i_ ) be the counterfactual explanation given to the individuals with initial feature value **_x_** _i_ under a set of counterfactual explanations _S_ . Then, it is clear that the marginal difference _h_ ( _S ∪{_ **_x_** _}_ ) _− h_ ( _S_ ) only depends on individuals with initial features **_x_** _i_ such that either 1 _− c_ ( **_x_** _i,_ **_x_** ) _≥_ 0 and **_x_** = _ES∪{_ **_x_** _}_ ( **_x_** _i_ ) or **_x_** _i_ = **_x_** . Moreover, if 1 _− c_ ( **_x_** _i,_ **_x_** ) _≥_ 0 and **_x_** = _ES∪{_ **_x_** _}_ ( **_x_** _i_ ), the contribution to the marginal difference is positive and, if **_x_** _i_ = **_x_** , the contribution to the marginal difference is negative. 

Consider first the individuals with initial features **_x_** _i_ such that 1 _− c_ ( **_x_** _i,_ **_x_** ) _≥_ 0 and **_x_** = _EA∪{_ **_x_** _}_ ( **_x_** _i_ ). We can divide all of these individuals into three cases: 

1. _πB_ ( **_x_** _i_ ) = 0: in this case, **_x_** _i̸ ∈B_ and the individuals change their best-response from _EB_ ( **_x_** _i_ ) to **_x_** . Moreover, under the set of counterfactual explanations _A_ , their best-response is either **_x_** _i_ or 

15 

_EA_ ( **_x_** _i_ ) and it changes to **_x_** . Then, using a similar argument as in the proof of proposition 2, we can conclude that the contribution of the individuals to the marginal difference is greater or equal under the set of counterfactual explanations _A_ than under _B_ . 

2. _πB_ ( **_x_** _i_ ) = 1 _∧πA_ ( **_x_** _i_ ) = 0: in this case, **_x_** _i̸ ∈A_ and **_x_** _i ∈B_ . Therefore, under the set of counterfactual explanations _A_ , the individuals’ best-response changes from _EA_ ( **_x_** _i_ ) to **_x_** and there is a positive contribution to the marginal difference while, under _B_ , the individuals’ best response does not change and the contribution to the marginal difference is zero. 

3. _πB_ ( **_x_** _i_ ) = 1 _∧ πA_ ( **_x_** _i_ ) = 1: in this case, **_x_** _i̸ ∈B_ . Therefore, the best-response changes from **_x_** _i_ to **_x_** under both sets of counterfactual explanations and there is an equal positive contribution to the marginal difference. 

Now, consider the individuals with initial features **_x_** _i_ such that **_x_** _i_ = **_x_** . We can divide all of these individuals also into three cases: 

1. _πA_ ( **_x_** ) = _πB_ ( **_x_** ) = 0: in this case, under both sets of counterfactual explanations, the counterfactual explanation **_x_** changes the value of the decision policy to _πA∪{_ **_x_** _}_ ( **_x_** ) = _πB∪{_ **_x_** _}_ ( **_x_** ) = 1. Moreover, the contribution to the marginal difference is less negative under the set of counterfactual explanations _A_ than under _B_ since _P_ ( _y_ = 1 _| EA_ ( **_x_** )) _≤ P_ ( _y_ = 1 _| EB_ ( **_x_** )) and thus _P_ ( **_x_** )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EA_ ( **_x_** ))] _≥ P_ ( **_x_** )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** ))]. 

2. _πA_ ( **_x_** ) = 1 _∧πB_ ( **_x_** ) = 0: in this case, under the set of counterfactual explanations _A_ , the individuals’ best response does not change and thus the contribution to the marginal difference is zero and, under the set of counterfactual explanations _B_ , their best-response changes from _EB_ ( **_x_** ) to **_x_** and thus there is a negative contribution to the marginal difference _i.e._ , _P_ ( **_x_** )[ _P_ ( _y_ = 1 _|_ **_x_** ) _− P_ ( _y_ = 1 _| EB_ ( **_x_** ))] _<_ 0. 

3. _πA_ ( **_x_** ) = _πB_ ( **_x_** ) = 1: in this case, under both sets of counterfactual explanations, the individuals’ best response does not change and thus the contribution to the marginal difference is zero. 

As a direct consequence of the above observations, it readily follows that _h_ ( _A ∪{_ **_x_** _}_ ) _− h_ ( _A_ ) _≥ h_ ( _B ∪{_ **_x_** _}_ ) _− h_ ( _B_ ) and therefore the function _h_ is submodular. 

However, in contrast with Section 3, the function _h_ is non-monotone since it can happen that the negative marginal contribution exceeds the positive one. For example, consider the following instance of the problem, where **_x_** _∈{_ 1 _,_ 2 _,_ 3 _}_ with _γ_ = 0 _._ 1: 



and 



Assume there is a set of counterfactual explanations _A_ = _{_ 1 _}_ . Then, the optimal policy is given by _πA_<sup>_∗_(1) = 1</sup><sup>_, π_</sup> _A_<sup>_∗_(2) = 0</sup><sup>_, π_</sup> _A_<sup>_∗_(3) = 0inducingamovementfromfeaturevalues2</sup><sup>_,_3tofeaturevalue1,giving</sup> a utility equal to 0 _._ 9. Now, add **_x_** = 2 to the set of counterfactual explanations _i.e._ , _A_ = _{_ 1 _,_ 2 _}_ . Then, the optimal policy is given by _πA_<sup>_∗_(1) = 1</sup><sup>_, π_</sup> _A_<sup>_∗_(2) = 1</sup><sup>_, π_</sup> _A_<sup>_∗_(3) = 0inducingamovementfromfeaturevalue</sup> 3 to feature value 1, giving a lower utility, equal to 0 _._ 5. Therefore, the function _h_ is non-monotone. 

## **C Additional details on the standard greedy algorithm and the randomized algorithm by Buchbinder et al. (2014)** 

To enjoy a 1 _/e_ approximation guarantee, Algorithm 2 requires that there are 2 _k < m_ candidate feature values whose marginal contribution to any set is zero. In our problem, this can be trivially satisfied by adding 2 _k_ feature values **_x_** to _X_ such that _P_ ( _y_ = 1 _|_ **_x_** ) = _γ_ , _P_ ( **_x_** ) = 0 and _c_ ( **_x_** _,_ **_x_** _j_ ) = _c_ ( **_x_** _j,_ **_x_** ) = 2 _∀_ **_x_** _j ∈ X_ . If the algorithm adds some of those counterfactual explanations to the set _A_ , it is easy to see that we can ignore them without causing any difference in utility or best-responses. 

16 

**ALGORITHM 1:** Standard greedy algorithm (Nemhauser et al., 1978) 

**Input:** Ground set of counterfactual explanations _Pπ_ , parameter _k_ and utility function _f_ **Output:** Set of counterfactual explanations _A_ 1: _A ←_ ∅ 2: **while** _|A| ≤ k_ **do** 3: **_x_**<sup>_∗_</sup> _←_ argmax **_x_** _∈Pπ \Af_ ( _A ∪{_ **_x_** _}_ ) _− f_ ( _A_ ) 4: _A ←A ∪{_ **_x_**<sup>_∗_</sup> _}_ 5: **end while** 6: **return** _A_ 

**ALGORITHM 2:** Randomized algorithm by Buchbinder et al. (2014) 

**Input:** Ground set of counterfactual explanations _Y_ , parameter _k_ and utility function _f_ **Output:** Set of counterfactual explanations _A_ 1: _A ←_ ∅ 2: **while** _|A| ≤ k_ **do** 3: _B ←_ GetTopK( _Y, A, f_ ) 4: **_x_**<sup>_∗_</sup> _∼B_ 5: _A ←A ∪{_ **_x_**<sup>_∗_</sup> _}_ 6: **end while** 

- 7: **return** _A_ 

## **D Jointly optimizing the decision policy and the counterfactual explanations** 

Figure 6 shows that, by jointly optimizing both the decision policy and the counterfactual explanations, we may obtain an additional gain in terms of utility in comparison with just optimizing for the set of counterfactual explanations given the optimal decision policy in a non-strategic setting. 



<!-- Start of picture text -->
P y = 1  𝐱) = 1<br>𝑃 𝑦= 1  𝒙) = 0<br>𝜋(𝒙) = 1<br>𝒙𝟐 ℛ(𝒙𝟒) 𝜋(𝒙) = 0 ℰ(𝒙𝟏) ℰ(𝒙𝒙𝟐𝟐) 𝒙𝟑<br>𝒙𝟏 𝒙𝟒 𝒙𝟏 𝒙𝟒<br>𝒙𝟑 𝒙𝟑 ℛ(𝒙𝟐)<br>ℛ(𝒙𝟑) ℛ(𝒙𝟏)<br>Non-strategic policy Strategic policy<br><!-- End of picture text -->

Figure 6: Jointly optimizing the decision policy and the counterfactual explanations can offer additional gains. The left panel shows the optimal (deterministic) decision policy _π_ under non-strategic behavior, as given by Eq. 6. Here, there does not exist a set of counterfactual explanations _A ∈Pπ_ that increases the utility of the policy. This happens because the area of adaption of **_x_** 3 and **_x_** 4 does not include any feature value that receives a positive decision. The right panel shows the decision policy and counterfactual explanations that are (jointly) optimal in terms of utility, as given by Eq. 4. Here, the individuals with feature values **_x_** 1 and **_x_** 2 receive _E_ ( **_x_** 1) and _E_ ( **_x_** 2), respectively, as counterfactual explanations. Since these explanations are within their areas of adaptation _R_ ( **_x_** 1) and _R_ ( **_x_** 2), they change their initial feature values in order to receive a positive decision. 

## **E Experiments on Synthetic Data** 

**Experimental setup.** For simplicity, we consider feature values **_x_** _∈{_ 0 _, . . . , m −_ 1 _}_ and _P_ ( **_x_** = _i_ ) = _pi/_<sup>�</sup> _j_<sup>_pj_where</sup><sup>_pi_issampledfromaGaussiandistribution</sup><sup>_N_(</sup><sup>_µ_=0</sup><sup>_._5</sup><sup>_, σ_=0</sup><sup>_._1)truncatedfrombelow</sup> at zero. We also sample _P_ ( _y_ = 1 _|_ **_x_** ) _∼ U_ [0 _,_ 1], _c_ ( **_x_** _i,_ **_x_** _j_ ) _∼ U_ [0 _,_ 1] for 50% of all pairs and _c_ ( **_x_** _i,_ **_x_** _j_ ) = 2 

17 



<!-- Start of picture text -->
1 . 0 1 . 0 0 . 5<br>Black box Black box Black box<br>0 . 8 MinimumDiverse cost 0 . 8 MinimumDiverse cost 0 . 4 MinimumDiverse cost<br>Algorithm 1 Algorithm 1 Algorithm 1<br>0 . 6 Algorithm 2 0 . 6 Algorithm 2 0 . 3 Algorithm 2<br>0 . 4 0 . 4 0 . 2<br>0 . 2 0 . 2 0 . 1<br>0 . 0 10 20 50 100 200 0 . 0 0 1 2 5 10 20 30 40 0 . 0 0 1 2 5 10 20 30 40<br>m k k<br>(a) Utility vs. # feature values (b) Utility vs. # explanations (c) Individual cost vs. # expla-<br>nations<br>()  A Utility, uπ, ()  A Utility, uπ,<br>Averageindividualcost<br><!-- End of picture text -->

Figure 7: Results on synthetic data. Panels (a) and (b) show the utility achieved by six types of decision policies and counterfactual explanations against the total number of feature values _m_ and the number of counterfactual explanations _k_ , respectively. Panel (c) shows the average cost individuals had to pay to change from their initial features to the feature value of the counterfactual explanation they receive under the same five types of decision policies and counterfactual explanations. In Panel (a), we set _k_ = 0 _._ 1 _m_ and, in Panels (b) and (c), we set _m_ = 200. In all panels, we repeat each experiment 20 times. 

for the rest. Finally, we set _γ_ = 0 _._ 3. In this section, we compare the utility achieved by our explanation methods with the same baselines we used on real data. 

**Results.** Figures 7(a,b) show the utility achieved by each of the decision policies and counterfactual explanations for several numbers of feature values _m_ and counterfactual explanations _k_ . We find several interesting insights: (i) the decision policies given by Eq. 5 and the counterfactual explanations found by Algorithm 2 beat all other alternatives by large margins across the whole spectrum, showing that jointly optimizing the decision policy and the counterfactual explanations offer clear additional gains; (ii) the counterfactual explanations found by Algorithms 1 and 2 provide higher utility gains as the number of feature values increases and thus the search space of counterfactual explanations becomes larger; and, (iii) a small number of counterfactual explanations is enough to provide significant gains in terms of utility with respect to the optimal decision policy without counterfactual explanations. 

Figure 7(c) shows the average cost individuals had to pay to change from their initial features to the feature value of the counterfactual explanation they receive. As one may have expected, the results show that, under the counterfactual explanations of minimum cost (Minimum cost and Diverse), the individuals invest less effort to change their initial features and the effort drops as the number of counterfactual explanations increases. In contrast, our methods incentivize the individuals to achieve the highest self-improvement, particularly when we jointly optimize the decision policy and the counterfactual explanations. 

## **F Additional details on the experiments on real data** 

### **F.1 Feature representation & preprocessing steps** 

For each applicant in the lending dataset, the label _y_ indicates whether an applicant fully pays a loan ( _y_ = 1) or ends up to a default/charge-off ( _y_ = 0) and the features **_x_** are: 

- Loan Amount: The amount that the applicant initially requested. 

- Employment Length: How long the applicant has been employed. 

- Debt to Income Ratio: The ratio between the applicant’s financial debts and her average income. 

- FICO Score: The applicant’s FICO score, which is a credit score based on consumer credit files. The FICO scores are in the range of 300-850 and the average of the high and low range for the FICO score of each applicant has been used for this study. 

- Annual Income: The declared annual income of the applicant. 

Here, we assume that all of the aforementioned features are _actionable_ , meaning that an individual denied a loan can change their values in order to get a positive decision. 

For each credit card holder in the credit dataset, the label indicates whether a credit card holder will default during the next month ( _y_ = 0) or not ( _y_ = 1) and the features **_x_** are: 

18 

Table 1: Dataset details 

|Dataset|# of samples|Classifier|_k_|Accuracy|_m_|_γ_|
|---|---|---|---|---|---|---|
|credit|30000|Logistic Regression|100|80_._4%|3200|0_._85|
|lending|1266817|Logistic Regression|400|89_._9%|400|0_._97|



- Marital status: Whether the person is married or single. 

- Age Group: Group depending on the person’s age (¡25, 25-39, 40-59, ¿60). 

- Education Level: The level of education the individual has acquired (1-4). 

- Maximum Bill Amount Over Last 6 Months 

- Maximum Payment Amount Over Last 6 Months 

- Months With Zero Balance Over Last 6 Months 

- Months With Low Spending Over Last 6 Months 

- Months With High Spending Over Last 6 Months 

- Most Recent Bill Amount 

- Most Recent Payment Amount 

- Total Overdue Counts 

- Total Months Overdue 

Here, we assume that all features except Marital Status, Age Group and Education Level are actionable and, among the actionable features, we assume that Total Overdue Counts and Total Months Overdue can only increase. 

In both cases, note that the actionable features are numerical, however, our methodology only allows for discrete valued features. Therefore, rather than using the numerical values as features, we first cluster the loan applicants (or credit card holders) into _k_ groups based on the original numerical features using k-clustering and then, for each applicant (or credit card holder), use the cluster identifier it belongs to, represented using a one-hot encoding, as a feature. After this preprocessing step, the discrete feature values **_x_** _i_ consists of all possible value combinations of discrete non-actionable features, if any, and cluster identifiers. 

To approximate the values of the conditional distribution _P_ ( _y |_ **_x_** ), we train four types of classifiers (Multi-layer perceptron, support vector machine, logistic regression, decision tree) using the default scikit-learn parameters and then choose the pair of classifier type and number of clusters _k_ that maximizes accuracy, estimated using 5-fold cross validation. Finally, we set _γ_ equal to the 50-th percentile of all the individuals’ _P_ ( _y_ = 1 _|_ **_x_** ) values causing a 50% acceptance rate by the optimal threshold policy in the non strategic setting. Table F.1 summarizes the resulting experimental setup for both datasets. 

### **F.2 Examples of counterfactual explanations** 

In this section, we focus on the credit dataset and look more closely into the counterfactual explanations _Em_ ( **_x_** ) and _E_ ( **_x_** ) provided by the minimum cost baseline and Algorithm 1, respectively, by means of an (anecdotal) example. To this end, for a fixed _α_ and _k_ , we first track down the individuals whose best-response under both methods is to change their initial features to the provided counterfactual explanation. Then, for each of these individuals, we compare the counterfactual explanations provided by each of both methods. 

Table F.2 shows the initial features **_x_** together with the counterfactual explanations _Em_ ( **_x_** ) and _E_ ( **_x_** ) for one of the above individuals picked at random. In this example, the individual is a university student, unmarried and under the age of 25 who is advised to follow the counterfactual explanations to maintain 

19 

Table 2: Counterfactual explanations _Em_ ( **_x_** ) and _E_ ( **_x_** ) provided by the minimum cost baseline and Algorithm 1, respectively, to an individual with initial feature value **_x_** . Initially, the individual’s outcome is _P_ ( _y_ = 1 _|_ **_x_** ) = 0 _._ 84 and, after best-response, her outcome is _P_ ( _y_ = 1 _| Em_ ( **_x_** )) = 0 _._ 87 and _P_ ( _y_ = 1 _| E_ ( **_x_** )) = 0 _._ 89, respectively. In both methods, we set _α_ = 2 and _k_ = 160. 

|Feature|**_x_**|_Em_(**_x_**)|_E_(**_x_**)|
|---|---|---|---|
|Married|No|No|No|
|Age group|Under 25|Under 25|Under 25|
|Education|Student|Student|Student|
|Maximum Bill Amount Over Last 6 Months|$2246|$2084|$1929|
|Maximum Payment Amount Over Last 6 Months|$191|$188|$221|
|Months With Zero Balance Over Last 6 Months|0|0|0|
|Months With Low Spending Over Last 6 Months|0|0|0|
|Months With High Spending Over Last 6 Months|4|2|1|
|Most Recent Bill Amount|$2145|$2003|$1750|
|Most Recent Payment Amount|$123|$124|$100|
|Total Overdue Counts|0|0|0|
|Total Months Overdue|0|0|0|



her credit. Since the marital status, age group and level of education are all non-actionable features, both counterfactual explanations maintain the initial values for those features. Under the minimum cost baseline, the bank would advise the individual to reduce her monthly credit card bill by _∼_ $150 and limit high spending to 2 months per semester so that her risk of default would decrease from 16% to 13%. However, under Algorithm 1, the bank would advise to reduce her monthly credit card bill by _∼_ $400, limit high spending to 1 month per semester, and additionally increase her monthly credit card payoff slightly so that her risk of default would decrease to 11%. Since by construction, both _Em_ ( **_x_** ) and _E_ ( **_x_** ) are inside the region of adaptation of **_x_** , the individual is guaranteed to follow the advice in both cases, however, under Algorithm 1, the individual would be less likely to default and achieve a superior long-term well being. 

20 

