---
title: "From local explanations to global understanding with explainable AI for trees"
authors: "unknown"
year: 2018
arxiv_id: "1802.03888"
original_file: "1802.03888.pdf"
pdf_path: "docs/papers\2018_unknown_from_local_explanations_to_global_u.pdf"
---

# From local explanations to global understanding with explainable AI for trees

**Authors:** Unknown et al.  
**Year:** 2018 | **arXiv:** [`1802.03888`](https://arxiv.org/abs/1802.03888)  
**Local PDF:** [`2018_unknown_from_local_explanations_to_global_u.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2018_unknown_from_local_explanations_to_global_u.pdf)

---

# **Consistent Individualized Feature Attribution for Tree Ensembles** 

Scott M. Lundberg, Gabriel G. Erion, and Su-In Lee 

University of Washington 

{slund1,erion,suinlee}@uw.edu 

## **ABSTRACT** 

Interpreting predictions from tree ensemble methods such as gradient boosting machines and random forests is important, yet feature attribution for trees is often heuristic and not individualized for each prediction. Here we show that popular feature attribution methods are _inconsistent_ , meaning they can lower a feature’s assigned importance when the true impact of that feature actually increases. This is a fundamental problem that casts doubt on any comparison between features. To address it we turn to recent applications of game theory and develop fast exact tree solutions for SHAP (SHapley <u>Additive exPlanation) values, which are the unique</u> consistent and locally accurate attribution values. We then extend SHAP values to interaction effects and define _SHAP interaction values_ . We propose a rich visualization of individualized feature attributions that improves over classic attribution summaries and partial dependence plots, and a unique “supervised” clustering (clustering based on feature attributions). We demonstrate better agreement with human intuition through a user study, exponential improvements in run time, improved clustering performance, and better identification of influential features. An implementation of our algorithm has also been merged into XGBoost and LightGBM, see http://github.com/slundberg/shap for details. 

## **1 INTRODUCTION** 

Understanding why a model made a prediction is important for trust, actionability, accountability, debugging, and many other tasks. To understand predictions from tree ensemble methods, such as gradient boosting machines or random forests, importance values are typically attributed to each input feature. These importance values can be computed either for a single prediction (individualized), or an entire dataset to explain a model’s overall behavior (global). 

Concerningly, popular current feature attribution methods for tree ensembles are _inconsistent_ . This means that when a model is changed such that a feature has a higher impact on the model’s output, current methods can actually lower the importance of that feature. Inconsistency strikes at the heart of what it means to be a good attribution method, because it prevents the meaningful comparison of attribution values across features. This is because inconsistency implies that a feature with a large attribution value might be less important than another feature with a smaller attribution (see Figure 1 and Section 2). 

To address this problem we turn to the recently proposed SHAP (SHapley Additive exPlanation) values [16], which are based on a unification of ideas from game theory [27] and local explanations [21]. Here we show that by connecting tree ensemble feature attribution methods with the class of _additive feature attribution methods_ [16] we can motivate SHAP values as the only possible consistent feature attribution method with several desirable properties. 

SHAP values are theoretically optimal, but like other model agnostic feature attribution methods [2, 9, 21, 27], they can be challenging to compute. To solve this we derive an algorithm for tree ensembles that reduces the complexity of computing exact SHAP values from _O_ ( _TL_ 2<sup>_M_</sup> ) to _O_ ( _TLD_<sup>2</sup> ) where _T_ is the number of trees, _L_ is the maximum number of leaves in any tree, _M_ is the number of features, and _D_ is the maximum depth of any tree. This exponential reduction in complexity allows predictions from previously intractable models with thousands of trees and features to now be explained in a fraction of a second. Entire datasets can now be explained, which enables new alternatives to traditional partial dependence plots and feature importance plots [11], which we term _SHAP dependence plots_ and _SHAP summary plots_ , respectively. 

Current attribution methods cannot directly represent interactions, but must divide the impact of an interaction among each feature. To directly capture pairwise interaction effects we propose _SHAP interaction values_ ; an extension of SHAP values based on the Shapley interaction index from game theory [12]. SHAP interaction values bring the benefits of guaranteed consistency to explanations of interaction effects for individual predictions. 

In what follows we first discuss current tree feature attribution methods and their inconsistencies. We then introduce SHAP values as the only possible consistent and locally accurate attributions, present Tree SHAP as a high speed algorithm for estimating SHAP values of tree ensembles, then extend this to SHAP interaction values. We use user study data, computational performance, influential feature identification, and supervised clustering to compare with previous methods. Finally, we illustrate SHAP dependence plots and SHAP summary plots with XGBoost and NHANES I national health study data [18]. 

## **2 INCONSISTENCIES IN CURRENT FEATURE ATTRIBUTION METHODS** 

Tree ensemble implementations in popular packages such as XGBoost [6], scikit-learn [20], and the _gbm_ R package [22] allow a user to compute a measure of feature importance. These values are meant to summarize a complicated ensemble model and provide insight into what features drive the model’s prediction. 

_Global_ feature importance values are calculated for an entire dataset (i.e., for all samples) in three primary ways: 

- (1) Gain: A classic approach to feature importance introduced by Breiman et al. in 1984 [3] is based on gain. Gain is the total reduction of loss or impurity contributed by all splits for a given feature. Though its motivation is largely heuristic [11], gain is widely used as the basis for feature selection methods [5, 13, 25]. 

- (2) Split Count: A second common approach is simply to count how many times a feature is used to split [6]. Since feature 

1 



<!-- Start of picture text -->
Model A Fever<br>Fever Cough Fever Cough<br>No Yes<br>Model A Attributions Model B Attributions<br>Tree SHAP<br>No Yes No Yes<br>Saabas Inconsistency<br>0 0 0 80<br>output = [Cough & Fever]*80<br>Model B mean(|Tree SHAP|)<br>No Yes<br>Gain Inconsistency<br>Fever Fever<br>No Yes No Yes Split Count Inconsistency<br>0 0 10 90 Permutation<br>Individualized<br>(Fever = yes, Cough = yes)<br>Global<br><!-- End of picture text -->

output = [Cough & Fever]*80 + [Cough]*10 

**Figure 1: Two simple tree models that demonstrate inconsistencies in the Saabas, gain, and split count attribution methods: The Cough feature has a larger impact in Model B than Model A, but is attributed less importance in Model B. Similarly, the Cough feature has a larger impact than Fever in Model B, yet is attributed less importance. The individualized attributions explain a single prediction of the model (when both Cough and Fever are Yes) by allocating the difference between the expected value of the model’s output (20 for Model A, 25 for Model B) and the current output (80 for Model A, 90 for Model B). The global attributions represent the overall importance of a feature in the model. Without consistency it is impossible to reliably compare feature attribution values.** 

   - splits are chosen to be the most informative, this can represent a feature’s importance. 

- (3) Permutation: A third common approach is to randomly permute the values of a feature in the test set and then observe the change in the model’s error. If a feature’s value is important then permuting it should create a large increase in the model’s error. Different choices about the method of feature value permutation lead to variations of this basic approach [1, 10, 14, 23, 26]. 

_Individualized_ methods that compute feature importance values for a single prediction are less established for trees. While model agnostic individualized explanation methods [2, 9, 16, 21, 27] can be applied to trees [17], they are significantly slower than treespecific methods and have sampling variability (see Section 5.3 for a computational comparison, or [16] for an overview). The only current tree-specific individualized explanation method we are aware of is by Sabbas [24]. The Saabas method is similar to the classic dataset-level gain method, but instead of measuring the reduction of loss, it measures the change in the model’s expected output. It proceeds by comparing the expected value of the model output at the root of the tree with the expected output of the subtree rooted at the child node followed by the decision path of the current input. The difference between these expectations is then attributed to the feature split on at the root node. By repeating this process recursively the method allocates the difference between the expected model output and the current output among the features on the decision path. 

_Unfortunately, the feature importance values from the gain, split count, and Saabas methods are all inconsistent._ This means that a model can change such that it relies more on a given feature, yet the importance estimate assigned to that feature decreases. Of the methods we consider, only SHAP values and permutationbased methods are consistent. Figure 1 shows the result of applying all these methods to two simple regression trees.<sup>1</sup> For the global calculations we assume an equal number of dataset points fall in each leaf, and the label of those points is exactly equal to the prediction of the leaf. Model A represents a simple AND function, while Model B represents the same AND function but with an additional increase in the predicted value when Cough is “Yes”. Note that because Cough is now more important it gets split on first in Model B. 

Individualized feature attribution is represented by Tree SHAP and Sabbas for the input Fever=Yes and Cough=Yes. Both methods allocate the difference between the current model output and the expected model output among the input features (80 − 20 for Model A). But the SHAP values are guaranteed to reflect the importance of the feature (see Section 2.1), while the Saabas values can give erroneous results, such as a larger attribution to Fever than to Cough in Model B. 

Global feature attribution is represented by four methods: the mean magnitude of the SHAP values, gain, split count, and feature permutation. Only the mean SHAP value magnitude and permutation correctly give Cough more importance than Fever in Model B. 

1For clarity we rounded small values in Figure 1. These small values are why the lower left splits in both models were not pruned during training. 

2 





**Figure 2: SHAP (SHapley** **<u>Additive</u> exPlanation) values explain the output of a function** _f_ **as a sum of the effects** _ϕi_ **of each feature being introduced into a conditional expectation. Importantly, for non-linear functions the order in which features are introduced matters. SHAP values result from averaging over all possible orderings. Proofs from game theory show this is the only possible consistent approach where**<sup>�</sup> _i_<sup>_M_</sup> =0<sup>_ϕi_=</sup><sup>_f_(</sup><sup>_x_)</sup><sup>**.Incontrast,theonlycurrentindividualizedfeatureattribution**</sup> **method for trees satisfies the summation, but is inconsistent because it only considers a single ordering [24].** 

This means gain and split count are not reliable measures of global feature importance, which is important to note given their widespread use. 

a subset _S_ of the input features. SHAP values combine these conditional expectations with the classic Shapley values from game theory to attribute _ϕi_ values to each feature: 

## **2.1 SHAP values as the only consistent and locally accurate individualized feature attributions** 

It was recently noted that many current methods for interpreting individual machine learning model predictions fall into the class of _additive feature attribution methods_ [16]. This class covers methods that explain a model’s output as a sum of real values attributed to each input feature. 

_Definition 2.1._ **Additive feature attribution methods** have an explanation model _д_ that is a linear function of binary variables: 



where _z_<sup>′</sup> ∈{0, 1}<sup>_M_</sup> , _M_ is the number of input features, and _ϕi_ ∈ R. 

The _zi_<sup>′variablestypicallyrepresentafeaturebeingobserved</sup> ( _zi_<sup>′= 1) or unknown (</sup><sup>_z_</sup> _i_<sup>′= 0), and the</sup><sup>_ϕi_’s are the feature attribution</sup> values. 

As previously described in Lundberg and Lee (2017), an important property of the class of additive feature attribution methods is that there is a single unique solution in this class with three desirable properties: _local accuracy_ , _missingness_ , and _consistency_ . Local accuracy states that the sum of the feature attributions is equal to the output of the function we are seeking to explain. Missingness states that features that are already missing (such that _zi_<sup>′= 0) are</sup> attributed no importance. Consistency states that changing a model so a feature has a larger impact on the model will never decrease the attribution assigned to that feature. 

Note that in order to evaluate the effect missing features have on a model _f_ , it is necessary to define a mapping _hx_ that maps between a binary pattern of missing features represented by _z_<sup>′</sup> and the original function input space. Given such a mapping we can evaluate _f_ ( _hx_ ( _z_<sup>′</sup> )) and so calculate the effect of observing or not observing a feature (by setting _zi_<sup>′= 1 or</sup><sup>_z_</sup> _i_<sup>′= 0).</sup> 

To compute SHAP values we define _fx_ ( _S_ ) = _f_ ( _hx_ ( _z_<sup>′</sup> )) = _E_ [ _f_ ( _x_ ) | _xS_ ] where _S_ is the set of non-zero indexes in _z_<sup>′</sup> (Figure 2), and _E_ [ _f_ ( _x_ ) | _xS_ ] is the expected value of the function conditioned on 



where _N_ is the set of all input features. 

As shown in Lundberg and Lee (2017), the above method is the only possible consistent, locally accurate method that obeys the missingness property and uses conditional dependence to measure missingness [16]. This is strong motivation to use SHAP values for tree ensemble feature attribution, particularly since the only previous individualized feature attribution method for trees, the Saabas method, satisfies both local accuracy and missingness using conditional dependence, but fails to satisfy consistency. This means that SHAP values provide a strict theoretical improvement by eliminating significant consistency problems (Figure 1). 

## **3 TREE SHAP: FAST SHAP VALUE COMPUTATION FOR TREES** 

Despite the compelling theoretical advantages of SHAP values, their practical use is hindered by two problems: 

- (1) The challenge of estimating _E_ [ _f_ ( _x_ ) | _xS_ ] efficiently. 

- (2) The exponential complexity of Equation 2. 

Here we focus on tree models and propose fast SHAP value estimation methods specific to trees and ensembles of trees. We start by defining a slow but straightforward algorithm, then present the much faster and more complex Tree SHAP algorithm. 

## **3.1 Estimating SHAP values directly in** _O_ ( _TL_ 2<sup>_M_</sup> ) **time** 

If we ignore computational complexity then we can compute the SHAP values for a tree by estimating _E_ [ _f_ ( _x_ ) | _xS_ ] and then using Equation 2 where _fx_ ( _S_ ) = _E_ [ _f_ ( _x_ ) | _xS_ ]. For a tree model _E_ [ _f_ ( _x_ ) | _xS_ ] can be estimated recursively using Algorithm 1, where _v_ is a vector of node values, which takes the value _internal_ for internal nodes. The vectors _a_ and _b_ represent the left and right node indexes for each internal node. The vector _t_ contains the thresholds for each internal node, and _d_ is a vector of indexes of the features used for splitting in internal nodes. The vector _r_ represents the cover of each node (i.e., how many data samples fall in that sub-tree). 

3 

The weight _w_ measures what proportion of the training samples matching the conditioning set _S_ fall into each leaf. 

**Algorithm 1** Estimating _E_ [ _<u>f</u>_ ( _x_ ) | _xS_ ] **procedure** EXPVALUE( _x_ , _S_ , _tree_ = { _v_ , _a_ , _b_ , _t_ , _r_ , _d_ }) **procedure** G( _j_ , _w_ ) **if** _vj_ � _internal_ **then return** _w_ · _vj_ **else if** _dj_ ∈ _S_ **then return** G( _aj_ , _w_ ) **if** _xdj_ ≤ _tj_ **else** G( _bj_ , _w_ ) **else return** G( _aj_ , _wraj_ / _rj_ ) + G( _bj_ , _wrbj_ / _rj_ ) **end if end if end procedure return** G(1, 1) **end procedure** 

## **3.2 Estimating SHAP values in** _O_ ( _TLD_<sup>2</sup> ) **time** 

Here we propose a novel algorithm to calculate the same values as above, but in polynomial time instead of exponential time. Specifically, we propose an algorithm that runs in _O_ ( _TLD_<sup>2</sup> ) time and _O_ ( _D_<sup>2</sup> + _M_ ) memory, where for balanced trees the depth becomes _D_ = log _L_ . Recall _T_ is the number of trees, _L_ is the maximum number of leaves in any tree, and _M_ is the number of features. 

The intuition of the polynomial time algorithm is to recursively keep track of what proportion of all possible subsets flow down into each of the leaves of the tree. This is similar to running Algorithm 1 simultaneously for all 2<sup>_M_</sup> subsets _S_ in Equation 2. It may seem reasonable to simply keep track of how many subsets (weighted by the cover splitting of Algorithm 1) pass down each branch of the tree. However, this combines subsets of different sizes and so prevents the proper weighting of these subsets, since the weights in Equation 2 depend on | _S_ |. To address this we keep track of each possible subset size during the recursion. The _EXTEND_ method in Algorithm 2 grows all these subsets according to a given fraction of ones and zeros, while the _UNWIND_ method reverses this process and is commutative with _EXTEND_ . The _EXTEND_ method is used as we descend the tree. The _UNWIND_ method is used to undo previous extensions when we split on the same feature twice, and to undo each extension of the path inside a leaf to compute weights for each feature in the path. 

In Algorithm 2, _m_ is the path of unique features we have split on so far, and contains four attributes: _d_ the feature index, _z_ the fraction of “zero” paths (where this feature is not in the set _S_ ) that flow through this branch, _o_ the fraction of “one” paths (where this feature is in the set _S_ ) that flow through this branch, and _w_ which is used to hold the proportion of sets of a given cardinality that are present. We use the dot notation to access these members, and for the whole vector _m_ . _d_ represents a vector of all the feature indexes. 

Algorithm 2 reduces the computational complexity of exact SHAP value computation from exponential to low order polynomial for trees and sums of trees (since the SHAP values of a sum of two functions is the sum of the original functions’ SHAP values). 

**Algorithm 2** Tree SHAP 

**procedure** TS( _x_ , _tree_ = { _v_ , _a_ , _b_ , _t_ , _r_ , _d_ }) _ϕ_ = array of _len_ ( _x_ ) zeros **procedure** RECURSE( _j_ , _m_ , _pz_ , _po_ , _pi_ ) _m_ = EXTEND( _m_ , _pz_ , _po_ , _pi_ ) **if** _vj_ � _internal_ **then for** _i_ ← 2 to _len_ ( _m_ ) **do** _w_ = _sum_ (UNWIND( _m_ , _i_ ). _w_ ) _ϕmi_ = _ϕmi_ + _w_ ( _mi_ . _o_ − _mi_ . _z_ ) _vj_ **end for else** _h_ , _c_ = _xdj_ ≤ _tj_ ? ( _aj_ , _bj_ ) : ( _bj_ , _aj_ ) _iz_ = _io_ = 1 _k_ = FINDFIRST( _m_ . _d_ , _dj_ ) **if** _k_ � nothing **then** _iz_ , _io_ = ( _mk_ . _z_ , _mk_ . _o_ ) _m_ = UNWIND( _m_ , _k_ ) **end if** RECURSE( _h_ , _m_ , _izrh_ / _rj_ , _io_ , _dj_ ) RECURSE( _c_ , _m_ , _izrc_ / _rj_ , 0, _dj_ ) **end if end procedure procedure** EXTEND( _m_ , _pz_ , _po_ , _pi_ ) _l_ = _len_ ( _m_ ) _m_ = _copy_ ( _m_ ) _ml_ +1.( _d_ , _z_ , _o_ , _w_ ) = ( _pi_ , _pz_ , _po_ , _l_ = 0 ? 1 : 0) **for** _i_ ← _l_ − 1 to 1 **do** _mi_ +1. _w_ = _mi_ +1. _w_ + _pomi_ . _w_ ( _i_ / _l_ ) _mi_ . _w_ = _pzmi_ . _w_ [( _l_ − _i_ )/ _l_ ] **end for return** m **end procedure procedure** UNWIND( _m_ , _i_ ) _l_ = _len_ ( _m_ ) _n_ = _ml_ . _w m_ = _copy_ ( _m_ 1... _l_ −1) **for** _j_ ← _l_ − 1 to 1 **do if** _mi_ . _o_ � 0 **then** _t_ = _mj_ . _w mj_ . _w_ = _n_ · _l_ /( _j_ · _mi_ . _o_ ) _n_ = _t_ − _mj_ . _w_ · _mi_ . _z_ (( _l_ − _j_ )/ _l_ ) **else** _mj_ . _w_ = ( _mj_ . _w_ · _l_ )/( _mi_ . _z_ ( _l_ − _j_ )) **end if end for for** _j_ ← _i_ to _l_ − 1 **do** _mj_ .( _d_ , _z_ , _o_ ) = _mj_ +1.( _d_ , _z_ , _o_ ) **end for return** m **end procedure** RECURSE(1, [], 1, 1, 0) **return** _ϕ_ **end procedure** 

4 

## **4 SHAP INTERACTION VALUES** 

Feature attributions are typically allocated among the input features, one for each feature, but we can gain additional insight by separating _interaction effects_ from main effects. If we consider pairwise interactions this leads to a matrix of attribution values representing the impact of all pairs of features on a given model prediction. Since SHAP values are based on classic Shapley values from game theory, a natural extension to interaction effects can be obtained though the more modern Shapley interaction index [12]: 





<!-- Start of picture text -->
SHAP<br>Saabas<br>Other<br><!-- End of picture text -->

when _i_ � _j_ , and 



In Equation 3 the SHAP interaction value between feature _i_ and feature _j_ is split equally between each feature so Φ _i_ , _j_ = Φ _j_ , _i_ and the total interaction effect is Φ _i_ , _j_ + Φ _j_ , _i_ . The main effects for a prediction can then be defined as the difference between the SHAP value and the SHAP interaction values for a feature: 



These SHAP interaction values follow from similar axioms as SHAP values, and allow the separate consideration of main and interaction effects for individual model predictions. This separation can uncover important interactions captured by tree ensembles that might otherwise be missed (Figure 10 in Section 5.5). 

While SHAP interaction values can be computed directly from Equation 3, we can leverage Algorithm 2 to drastically reduce their computational cost for tree models. As highlighted in Equation 5 SHAP interaction values can be interpreted as the difference between the SHAP values for feature _i_ when feature _j_ is present and the SHAP values for feature _i_ when feature _j_ is absent. This allows us to use Algorithm 2 twice, once while ignoring feature _j_ as fixed to present, and once with feature _j_ absent. This leads to a run time of _O_ ( _TMLD_<sup>2</sup> ), since we repeat the process for each feature. Note that even though this computational approach does not seem to directly enforce symmetry, the resulting Φ matrix is always symmetric. 

## **5 EXPERIMENTS AND APPLICATIONS** 

We compare Tree SHAP and SHAP interaction values with previous methods through both traditional metrics and three new applications we propose for individualized feature attributions: supervised clustering, SHAP summary plots, and SHAP dependence plots.<sup>2</sup> 

## **5.1 Agreement with Human Intuition** 

To validate that the SHAP values in Model A of Figure 1 are the most natural assignment of credit we ran a user study to measure people’s intuitive feature attribution values. Model A’s tree was shown to participants and said to represent risk for a certain disease. They were told that when a given person was found to have both a 

> 2Jupyter notebooks to compute all results are available at http://github.com/slundberg/ shap/notebooks/tree_shap_paper 

**Figure 3: Feature attribution values from 34 participants shown the tree from Model A in Figure 1. The first number represents the allocation to the Fever feature, while the second represents the allocation to the Cough feature. Participants from Amazon Mechanical Turk were not selected for machine learning expertise. No constraints were placed on the feature attribution values users entered.** 

cough and fever their risk went up from the prior risk of 20 (the expected value of risk) to a risk of 80. Participants were then asked to apportion the 60 point change in risk among the Cough and Fever features as they saw best. 

Figure 3 presents the results of the user study for Model A. The equal distribution of credit used by SHAP values was found to be the most intuitive. A smaller number of participants preferred to give greater weight to the first feature to be split on (Fever), while still fewer followed the allocation of the Saabas method and gave greater weight to the second feature split on (Cough). 

## **5.2 Computational Performance** 

Figure 5 demonstrates the significant run time improvement provided by Algorithm 2. Problems that were previously intractable for exact computation are now inexpensive. An XGBoost model with 1,000 depth 10 trees over 100 input features can now be explained in 0.08 seconds. 

## **5.3 Supervised Clustering** 

One intriguing application enabled by individualized feature attributions is what we term “supervised clustering,” where instead of using an unsupervised clustering method directly on the data features, you run clustering on the feature attributions. 

Supervised clustering naturally handles one of the most challenging problems in unsupervised clustering: determining feature weightings (or equivalently, determining a distance metric). Many times we want to cluster data using features with very different units. Features may be in dollars, meters, unit-less scores, etc. but whenever we use them as dimensions in a single multidimensional space it forces any distance metric to compare the relative importance of a change in different units (such as dollars vs. meters). Even if all our inputs are in the same units, often some features are more 

5 



<!-- Start of picture text -->
Samples sorted by explanation similarity<br>Large capital gain<br>Large capital loss<br>Married and well educated<br>Well educated older single<br>Young and single<br>Married and less educated<br>Middle aged less educated single Well educated young single<br>Log odds of making ≥50K<br><!-- End of picture text -->

**Figure 4: Supervised clustering with SHAP feature attributions in the UCI census dataset identifies among 2,000 individuals distinct subgroups of people that share similar reasons for making money. An XGBoost model with 500 trees of max depth six was trained on demographic data using a shrinkage factor of** _η_ = 0.005 **. This model was then used to predict the log odds that each person makes** ≥ $50 _K_ **. Each prediction was explained using Tree SHAP, and then clustered using hierarchical agglomerative clustering (imagine a dendrogram above the plot joining the samples). Red feature attributions push the score higher, while blue feature attributions push the score lower (as in Figure 2 but rotated 90**<sup>◦</sup> **). A few of the noticeable subgroups are annotated with the features that define them.** 



<!-- Start of picture text -->
Tree SHAP<br>Brute Force<br><!-- End of picture text -->

**Figure 5: Runtime improvement of Algorithm 2 over using Equation 2 and Algorithm 1. An XGBoost model with 50 trees was trained using an equally increasing number of input features and max tree depths. The time to explain one input vector is reported.** 

important than others. Supervised clustering uses feature attributions to naturally convert all the input features into values with the same units as the model output. This means that a unit change in any of the feature attributions is comparable to a unit change in any other feature attribution. It also means that fluctuations in the feature values only effect the clustering if those fluctuations have an impact on the outcome of interest. 

Here we demonstrate the use of supervised clustering on the classic UCI census dataset [15]. For this dataset the goal is to predict from basic demographic data if a person is likely to make more than $50K annually. By representing the positive feature attributions as red bars and the negative feature attributions as blue bars (as in Figure 2), we can stack them against each other to visually 

represent the model output as their sum. Figure 4 does this vertically for predictions from 2,000 people from the census dataset. The explanations for each person are stacked horizontally according the leaf order of a hierarchical clustering of the SHAP values. This groups people with similar reasons for a predicted outcome together. The formation of distinct subgroups of people demonstrates the power of supervised clustering to identify groups that share common factors related to income level. 

One way to quantify the improvement provided by SHAP values over the heuristic Saabas attributions is by examining how well supervised clustering based on each method explains the variance of the model output (note global feature attributions are not considered since they do not enable this type of supervised clustering). If feature attribution values well-represent the model then supervised clustering groups will have similar function outputs. Since hierarchical clusterings encode many possible groupings, we plot in Figure 6 the change in the _R_<sup>2</sup> value as the number of groups shrinks from one group per sample ( _R_<sup>2</sup> = 1) to a single group ( _R_<sup>2</sup> = 0). For the census dataset, groupings based on SHAP values outperform those from Saabas values (Figure 6A). For a dataset based on cognitive scores for Alzheimer’s disease SHAP values significantly outperform Saabas values (Figure 6B). This second dataset contains 200 gene expression module levels [4] as features and CERAD cognitive scores as labels [19]. 

## **5.4 Identification of Influential Features** 

Feature attribution values are commonly used to identify which features influenced a model’s prediction the most. To compare methods, the change in a model’s prediction can be computed when the most influential feature is perturbed. Figure 7 shows the result of this experiment on a sentiment analysis model of airline tweets [8]. An XGBoost model with 50 trees of maximum depth 30 was trained 

6 



<!-- Start of picture text -->
(A)<br>Census model<br>SHAP (AUC = 0.98)<br>Saabas (AUC = 0.97)<br>(B)<br>Alzheimer’s model<br>SHAP (AUC = 0.96)<br>Saabas (AUC = 0.88)<br><!-- End of picture text -->

**Figure 6: A quantitative measure of supervised clustering performance. If all samples are placed in their own group, and each group predicts the mean value of the group, then the** _R_<sup>2</sup> **value (the proportion of model output variance explained) will be** 1 **. If groups are then merged one-by-one the** _R_<sup>2</sup> **will decline until when there is only a single group it will be** 0 **. Hierarchical clusterings that well separate the model output value will retain a high** _R_<sup>2</sup> **longer during the merging process. Here supervised clustering with SHAP values outperformed the Sabbas method in both (A) the census data clustering shown in Figure 4, and (B) a clustering from genebased predictions of Alzheimer’s cognitive scores.** 

on 11,712 tweets with 1,686 bag-of-words features. Each tweet had a sentiment score label between -1 (negative) and 1 (positive). The predictions of the XGBoost model were then explained for 2,928 test tweets. For each method we choose the most influential negative feature and replaced it with the value of the same feature in another random tweet from the training set (this is designed to mimic the feature being unknown). The new input is then re-run through the model to produce an updated output. If the chosen feature significantly lowered the model output, then the updated model output should be higher than the original. By tracking the total change in model output as we progress through the test tweets we observe that SHAP values best identify the most influential negative feature. Since global methods only select a single feature for the whole dataset we only replaced this feature when it would likely 



<!-- Start of picture text -->
SHAP<br>500<br>Saabas<br>Gain<br>400<br>Permutation<br>300 Split Count<br>200<br>100<br>0<br>0 500 1000 1500 2000 2500 3000<br>Samples (tweets)<br>Total increase in model predictions<br><!-- End of picture text -->

**Figure 7: The total increase in a sentiment model’s output when the most negative feature is replaced. Five different attribution methods were used to determine the most negative feature for each sample. The higher the total increase in model output, the more accurate the attribution method was at identifying the most influential negative feature.** 

increase the sentiment score (for gain and permutation this meant randomly replacing the “thank” feature when it was missing, for split count it was the word “to”). 

## **5.5 SHAP Plots** 

Plotting the impact of features in a tree ensemble model is typically done with a bar chart to represent global feature importance, or a partial dependence plot to represent the effect of changing a single feature [11]. However, since SHAP values are individualized feature attributions, unique to every prediction, they enable new, richer visual representations. _SHAP summary plots_ replace typical bar charts of global feature importance, and _SHAP dependence plots_ provide an alternative to partial dependence plots that better capture interaction effects. 

To explore these visualizations we trained an XGBoost Cox proportional hazards model on survival data from the classic NHANES I dataset [18] using the NHANES I Epidemiologic Followup Study [7]. After selection for the presence of basic blood test data we obtained data for 9,932 individuals followed for up to 20 years after baseline data collection for mortality. Based on a 80/20 train/test split we chose to use 7,000 trees of maximum depth 3, _η_ = 0.001, and 50% instance sub-sampling. We then used these parameters and trained on all individuals to generate the final model. 

_5.5.1 SHAP Summary Plots._ Standard feature importance bar charts give a notion of relative importance in the training dataset, but they do not represent the range and distribution of impacts that feature has on the model’s output, and how the feature’s value relates to it’s impact. SHAP summary plots leverage individualized feature attributions to convey all these aspects of a feature’s importance while remaining visually concise (Figure 8). Features are first sorted by their global impact<sup>�</sup><sup>_N_</sup> _j_ =1<sup>|</sup><sup>_ϕ_</sup> _i_<sup>(</sup><sup>_j_)|, then dots representing the</sup> SHAP values _ϕi_<sup>(</sup><sup>_j_)</sup> are plotted horizontally, stacking vertically when they run out of space. This vertical stacking creates an effect similar 

7 



<!-- Start of picture text -->
M/F<br><!-- End of picture text -->

**Figure 8: SHAP summary plot of a 14 feature XGBoost survival model on 20 year mortality followup data from NHANES I [18]. The higher the SHAP value of a feature, the higher your log odds of death in this Cox hazards model. Every individual in the dataset is run through the model and a dot is created for each feature attribution value, so one person gets one dot on each feature’s line. Dot’s are colored by the feature’s value for that person and pile up vertically to show density.** 

to violin plots but without an arbitrary smoothing kernel width. Each dot is colored by the value of that feature, from low (blue) to high (red). If the impact of the feature on the model’s output varies smoothly as its value changes then this coloring will also have a smooth gradation. In Figure 8 we see (unsurprisingly) that age at baseline is the most important risk factor for death over the next 20 years. The density of the age plot shows how common different ages are in the dataset, and the coloring shows a smooth increase in the model’s output (a log odds ratio) as age increases. In contrast to age, systolic blood pressure only has a large impact for a minority of people with high blood pressure. The general trend of long tails reaching to the right, but not to the left, means that extreme values of these measurements can significantly raise your risk of death, but cannot significantly lower your risk. 

_5.5.2 SHAP Dependence Plots._ As described in Equation 10.47 of Friedman et al. (2001), partial dependence plots represent the expected output of a model when the value of a specific variable (or group of variables) is fixed. The values of the fixed variables are varied and the resulting expected model output is plotted. Plotting how the expected output of a function changes as we change a feature helps explain how the model depends on that feature. 

SHAP values can be used to create a rich alternative to partial dependence plots, which we term SHAP dependence plots. SHAP 



**Figure 9: Each dot is a person. The x-axis is their systolic blood pressure and the y-axis is the SHAP value attributed to their systolic blood pressure. Higher SHAP values represent higher risk of death due to systolic blood pressure. Coloring each dot by the person’s age reveals that high blood pressure is more concerning to the model when you are young (this represents an interaction effect).** 

dependence plots use the SHAP value of a feature for the y-axis and the value of the feature for the x-axis. By plotting these values for many individuals from the dataset we can see how the feature’s attributed importance changes as its value varies (Figure 9). While standard partial dependence plots only produce lines, SHAP dependence plots capture vertical dispersion due to interaction effects in the model. These effects can be visualized by coloring each dot with the value of an interacting feature. In Figure 9 coloring by age shows that high blood pressure is more alarming when you are young. Presumably because it is both less surprising as you age, and possibly because it takes time for high blood pressure to lead to fatal complications. 

Combining SHAP dependence plots with SHAP interaction values can reveal global interaction patterns. Figure 10A plots the SHAP main effect value for systolic blood pressure. Since SHAP main effect values represents the impact of systolic blood pressure after all interaction effects have been removed (Equation 6), there is very little vertical dispersion in Figure 10A. Figure 10B shows the SHAP interaction value of systolic blood pressure and age. As suggested by the coloring in Figure 9, this interaction accounts for most of the vertical variance in the systolic blood pressure SHAP values. 

## **6 CONCLUSION** 

Several common feature attribution methods for tree ensembles are inconsistent, meaning they can lower a feature’s assigned importance when the true impact of that feature actually increases. This can prevent the meaningful comparison of feature attribution values. In contrast, SHAP values consistently attribute feature importance, better align with human intuition, and better recover influential features. By presenting the first polynomial time algorithm for SHAP values in tree ensembles, we make them a practical 

8 



<!-- Start of picture text -->
(A)<br>(B)<br><!-- End of picture text -->

**Figure 10: SHAP interaction values separate the impact of systolic blood pressure into main effects (A; Equation 6) and interaction effects (B; Equation 3). Systolic blood pressure has a strong interaction effect with age, so the sum of (A) and (B) nearly equals Figure 9. There is very little vertical dispersion in (A) since all the interaction effects have been removed.** 

replacement for previous methods. We further defined SHAP interaction values as a consistent way of measuring potentially hidden pairwise interaction relationships. Tree SHAP’s exponential speed improvements open up new practical opportunities, such as supervised clustering, SHAP summary plots, and SHAP dependence plots, that advance our understanding of tree models. 

- [5] S Chebrolu, A Abraham, and J Thomas. 2005. Feature deduction and ensemble design of intrusion detection systems. _Computers & security_ 24, 4 (2005), 295–307. 

- [6] Tianqi Chen and Carlos Guestrin. 2016. XGBoost: A scalable tree boosting system. In _Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ . ACM, 785–794. 

- [7] Christine S Cox, Jacob J Feldman, Cordell D Golden, Madelyn A Lane, Jennifer H Madans, Michael E Mussolino, and Sandra T Rothwell. 1997. Plan and operation of the NHANES I Epidemiologic Followup Study, 1992. (1997). 

- [8] Crowdflower. 2015. Twitter US Airline Sentiment. https://www.kaggle.com/ crowdflower/twitter-airline-sentiment. (2015). Accessed: 2018-02-06. 

- [9] Anupam Datta, Shayak Sen, and Yair Zick. 2016. Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems. In _Security and Privacy (SP), 2016 IEEE Symposium on_ . IEEE, 598–617. 

- [10] R Díaz-Uriarte and S De Andres. 2006. Gene selection and classification of microarray data using random forest. _BMC bioinformatics_ 7, 1 (2006), 3. 

- [11] Jerome Friedman, Trevor Hastie, and Robert Tibshirani. 2001. _The elements of statistical learning_ . Vol. 1. Springer series in statistics Springer, Berlin. 

- [12] Katsushige Fujimoto, Ivan Kojadinovic, and Jean-Luc Marichal. 2006. Axiomatic characterizations of probabilistic and cardinal-probabilistic interaction indices. _Games and Economic Behavior_ 55, 1 (2006), 72–99. 

- [13] A Irrthum, L Wehenkel, P Geurts, et al. 2010. Inferring regulatory networks from expression data using tree-based methods. _PloS one_ 5, 9 (2010), e12776. 

- [14] Hemant Ishwaran et al. 2007. Variable importance in binary regression trees and forests. _Electronic Journal of Statistics_ 1 (2007), 519–537. 

- [15] M. Lichman. 2013. UCI ML Repository. (2013). http://archive.ics.uci.edu/ml 

- [16] Scott M Lundberg and Su-In Lee. 2017. A Unified Approach to Interpreting Model Predictions. In _Advances in Neural Information Processing Systems 30_ . Curran Associates, Inc., 4768–4777. http://papers.nips.cc/paper/ 7062-a-unified-approach-to-interpreting-model-predictions.pdf 

- [17] Scott M Lundberg, Bala Nair, Monica S Vavilala, Mayumi Horibe, Michael J Eisses, Trevor Adams, David E Liston, Daniel King-Wai Low, Shu-Fang Newman, Jerry Kim, et al. 2017. Explainable machine learning predictions to help anesthesiologists prevent hypoxemia during surgery. _bioRxiv_ (2017), 206540. 

- [18] Henry W Miller. 1973. Plan and operation of the health and nutrition examination survey, United States, 1971-1973. _DHEW publication no.(PHS)-Dept. of Health, Education, and Welfare (USA)_ (1973). 

- [19] Suzanne S Mirra, A Heyman, D McKeel, SM Sumi, Barbara J Crain, LM Brownlee, FS Vogel, JP Hughes, G Van Belle, L Berg, et al. 1991. The Consortium to Establish a Registry for Alzheimer’s Disease (CERAD) Part II. Stand. of the neuropathologic assessmen== of Alzheimer’s disease. _Neurology_ 41, 4 (1991), 479–479. 

- [20] F Pedregosa, G Varoquaux, A Gramfort, V Michel, B Thirion, O Grisel, M Blondel, P Prettenhofer, R Weiss, V Dubourg, et al. 2011. Scikit-learn: Machine learning in Python. _JMLR_ 12, Oct (2011), 2825–2830. 

- [21] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. Why should i trust you?: Explaining the predictions of any classifier. In _Proceedings of the 22nd ACM SIGKDD_ . ACM, 1135–1144. 

- [22] Greg Ridgeway. 2010. Generalized boosted regression models. Documentation on the R Package âĂŸgbmâĂŹ, version 1.6–3. (2010). 

- [23] W Rodenburg, G Heidema, J Boer, I Bovee-Oudenhoven, E Feskens, E Mariman, and J Keijer. 2008. A framework to identify physiological responses in microarraybased gene expression studies: selection and interpretation of biologically relevant genes. _Physiological genomics_ 33, 1 (2008), 78–90. 

- [24] Ando Saabas. 2014. Interpreting random forests. http://blog.datadive.net/ interpreting-random-forests/. (2014). Accessed: 2017-06-15. 

- [25] Marco Sandri and Paola Zuccolotto. 2008. A bias correction algorithm for the Gini variable importance measure in classification trees. _Journal of Computational and Graphical Statistics_ 17, 3 (2008), 611–628. 

- [26] C Strobl, A Boulesteix, T Kneib, T Augustin, and A Zeileis. 2008. Conditional variable importance for random forests. _BMC bioinformatics_ 9, 1 (2008), 307. 

- [27] Erik Štrumbelj and Igor Kononenko. 2014. Explaining prediction models and individual predictions with feature contributions. _Knowledge and information systems_ 41, 3 (2014), 647–665. 

_Acknowledgements:_ Vadim Khotilovich for helpful feedback. 

## **REFERENCES** 

- [1] Lidia Auret and Chris Aldrich. 2011. Empirical comparison of tree ensemble variable importance measures. _Chemometrics and Intelligent Laboratory Systems_ 105, 2 (2011), 157–170. 

- [2] David Baehrens, Timon Schroeter, Stefan Harmeling, Motoaki Kawanabe, Katja Hansen, and Klaus-Robert MÃžller. 2010. How to explain individual classification decisions. _Journal of Machine Learning Research_ 11, Jun (2010), 1803–1831. 

- [3] Leo Breiman, Jerome Friedman, Charles J Stone, and Richard A Olshen. 1984. _Classification and regression trees_ . CRC press. 

- [4] Safiye Celik, Benjamin Logsdon, and Su-In Lee. 2014. Efficient dimensionality reduction for high-dimensional network estimation. In _International Conference on Machine Learning_ . 1953–1961. 

9 

