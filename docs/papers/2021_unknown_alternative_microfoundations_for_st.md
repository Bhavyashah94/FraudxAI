---
title: "Alternative Microfoundations for Strategic Classification"
authors: "unknown"
year: 2021
arxiv_id: "2102.12560"
original_file: "2102.12560.pdf"
pdf_path: "docs/papers\2021_unknown_alternative_microfoundations_for_st.pdf"
---

# Alternative Microfoundations for Strategic Classification

**Authors:** Unknown et al.  
**Year:** 2021 | **arXiv:** [`2102.12560`](https://arxiv.org/abs/2102.12560)  
**Local PDF:** [`2021_unknown_alternative_microfoundations_for_st.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2021_unknown_alternative_microfoundations_for_st.pdf)

---

# **PsiPhi-Learning: Reinforcement Learning with Demonstrations using Successor Features and Inverse Temporal Difference Learning** 

**Angelos Filos**<sup>1</sup> **Clare Lyle**<sup>1</sup> **Yarin Gal**<sup>1</sup> **Sergey Levine**<sup>2</sup> **Natasha Jaques**<sup>* 2 3</sup> **Gregory Farquhar**<sup>* 4</sup> 

## **Abstract** 

We study reinforcement learning (RL) with noreward demonstrations, a setting in which an RL agent has access to additional data from the interaction of other agents with the same environment. However, it has no access to the rewards or goals of these agents, and their objectives and levels of expertise may vary widely. These assumptions are common in multi-agent settings, such as autonomous driving. To effectively use this data, we turn to the framework of successor features. This allows us to disentangle shared features and dynamics of the environment from agent-specific rewards and policies. We propose a multi-task inverse reinforcement learning (IRL) algorithm, called _inverse temporal difference learning_ (ITD), that learns shared state features, alongside peragent successor features and preference vectors, purely from demonstrations without reward labels. We further show how to seamlessly integrate ITD with learning from online environment interactions, arriving at a novel algorithm for reinforcement learning with demonstrations, called ΨΦ-learning (pronounced ‘Sci-Fi’). We provide empirical evidence for the effectiveness of ΨΦlearning as a method for improving RL, IRL, imitation, and few-shot transfer, and derive worstcase bounds for its performance in zero-shot transfer to new tasks. 

## **1. Introduction** 

If artificial agents are to be effective in the real world, they will need to thrive in environments populated by other agents. Agents are typically goal-directed, sometimes by definition (Franklin & Graesser, 1996). While their goals can be different, they often depend on shared salient fea- 

*Equal contribution 1University of Oxford 2University of California, Berkeley<sup>3</sup> Google Research, Brain team<sup>4</sup> DeepMind. Correspondence to: Angelos Filos _<_ angelos.filos@cs.ox.ac.uk _>_ . 

_Proceedings of the 38_<sup>_th_</sup> _International Conference on Machine Learning_ , PMLR 139, 2021. Copyright 2021 by the author(s). 



_Figure 1._ **The** ΨΦ **-learning algorithm for RL with no-reward demonstrations.** Demonstrations _D_ contain data from other agents for _unknown_ tasks. We employ _inverse temporal difference learning_ (ITD, cf. Section 3.1) to recover other agents’ successor features (SFs) Ψ<sup>_k_</sup> and preferences **w**<sup>_k_</sup> . The ego-agent combines the estimated SFs of others along with its own preferences **w**<sup>ego</sup> and SFs Ψ<sup>ego</sup> with generalised policy improvement (GPI, cf. Section 2.2), generating experience. Both the demonstrations and the ego-experience are used to learn the shared cumulants Φ. 

tures of the environment, and may be able to interact with and affect the environment in similar ways. Humans and other animals make ready use of these similarities to other agents while learning (Henrich, 2017; Laland, 2018). We can observe the goal-directed behaviours of other humans, and combine these observations with our own experiences, to quickly learn how to achieve our own goals. If reinforcement learning (RL, Sutton & Barto, 2018) agents could similarly interpret the behaviour of others, they could learn more efficiently, relying less on solitary trial and error. 

To this end, we formalise and address a problem setting in which an agent (the ‘ego-agent’) is given access to observations and actions drawn from the experiences of other goal-directed agents interacting with the same environment, but pursuing distinct goals. These observed trajectories are unlabelled in the sense that they lack the goals or rewards of the other agents. This type of data is readily available in many real-world settings, either from (i) observing other agents acting simultaneously with the ego-agent in the same (multi-agent) environment, or (ii) multi-task demonstrations collected independently from the ego-agent’s experiences. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

Consider autonomous driving as a motivating example: the car can observe the decisions of many nearby human drivers with various preferences and destinations, or may have access to a large offline dataset of such demonstrations. Because the other agents are pursuing their own varied goals, it can be difficult to directly use this information with conventional imitation learning methods (Widrow & Smith, 1964) or inverse RL (IRL) (Ng et al., 2000; Ziebart et al., 2008). 

While the ego-agent should not copy other agents directly, it is likely that the behaviour of all agents depends on shared features of the environment. To disentangle such shared features from agent-specific goals, we turn to the framework of successor features (Dayan, 1993; Kulkarni et al., 2016; Barreto et al., 2017). Successor features are a representation that captures the sum of state features an agent’s policy will reach in the future. An agent’s goal is represented separately as a preference vector. 

In this paper, we demonstrate how a reinforcement learner can benefit from multi-task demonstrations using the framework of successor features. The key contributions are: 

1. **Offline multi-task IRL:** We propose an inverse RL algorithm, called _inverse temporal difference_ (ITD) _learning_ . Using only demonstrations, we learn shared state features, alongside per-agent successor features and inferred preferences. The reward functions can be trivially computed from these learned quantities. We show empirically that ITD achieves superior or comparable performance to prior methods. 

2. **RL with no-reward demonstrations:** By combining ITD with learning from environment interactions, we arrive at a novel algorithm for RL with unlabelled demonstrations, called ΨΦ-learning (pronounced ‘SciFi’). ΨΦ-learning is compatible with sub-optimal demonstrations. It treats the demonstrated trajectories as being soft-optimal under _some_ task and employs ITD to recover successor features for the demonstrators’ policies. ΨΦ-learning inherits the unbiased, asymptotic performance of RL methods while leveraging the provided demonstrations with ITD. When the goals of any of the demonstrators are even partially aligned with the ΨΦ-learner, this enables much faster learning than solitary RL. Otherwise, when the demonstrations are not useful or even misleading, it gracefully falls back to standard RL, unlike na¨ıve behaviour cloning or IRL. 

3. **Few-shot adaptation with task inference:** Taking full-advantage of the successor features framework, our ΨΦ-learner can even adapt zero-shot to new goals it has never seen or experienced during training, but which are partially aligned with the demonstrated goals. This is possible due to the disentanglement of repre- 

sentations into task-specific features (i.e., preferences) and shared state features. We can efficiently update the task-specific preferences and rely on generalised policy improvement for safe policy updates. We derive worst-case bounds for the performance of ΨΦ-learning in zero-shot transfer to new tasks. 

We evaluate ΨΦ-learning in a set of grid-world environments, a traffic-flow simulator (Leurent, 2018), and a task from the ProcGen suite (Cobbe et al., 2020), observing advantages over vanilla RL, imitation learning (Reddy et al., 2019; Ho & Ermon, 2016), and auxiliary-task baselines (Hernandez-Leal et al., 2017). Thanks to the shared state features between the ITD and RL components, we find empirically that the ΨΦ-learner not only improves its egolearning with demonstrations, but also enhances its ability to model others agents using its own experience. 

## **2. Background and Problem Setting** 

We consider a world that can be represented as an infinite horizon controlled Markov process (CMP) given by the tuple: _C_ ≜ _⟨S, A, P, γ⟩_ . _S_ and _A_ represent the continuous state and discrete action spaces, respectively, **s**<sup>_′_</sup> _∼ P_ ( _·|_ **s** _,_ **a** ) describes the transition dynamics and _γ_ is the discount factor. A **task** is formulated as a Markov decision process (MDP, Puterman, 2014), characterised by a reward function, _R_ : _S × A →_ R, i.e., _M_ ≜ _⟨C, R⟩_ . 

The goal of an agent is to find a policy which maps from states to a probability distribution over actions, _π_ : _S →_ ∆( _A_ ), maximising the expected discounted sum of rewards _G_<sup>_R_</sup> ≜<sup>�</sup><sup>_∞_</sup> _t_ =0<sup>_γtR_(</sup><sup>**s**</sup><sup>_t,_</sup><sup>**a**</sup><sup>_t_).</sup> The actionvalue function of the policy _π_ is given by _Q_<sup>_π,R_</sup> ( **s** _,_ **a** ) ≜ E<sup>_C,π_�</sup> _G_<sup>_R_��</sup> **s** 0 = **s** _,_ **a** 0 = **a** �, where E<sup>_C,π_</sup> [ _·_ ] denotes expected value when following policy _π_ in environment _C_ . 

### **2.1. RL with No-Reward Demonstrations** 

We are interested in settings in which, in addition to an environment _C_ , the agent has also access to **demonstrations without rewards** , i.e., behavioural data of mixed and unknown quality. The demonstrations are generated by other agents, whose goals and levels of expertise are unknown, and who have no incentive to educate the controlled agent. We will refer to the controlled agent, i.e., reinforcement learner, as the ‘ego-agent’ and to the agents that generated the demonstrations as ‘other-agents’. We denote the demonstrations with _D_ = _{τ_ 1 _, τ_ 2 _, . . . , τN }_ , where the trajectory _τ_ ≜ ( **s** 0 _,_ **a** 0 _, . . . ,_ **s** _T ,_ **a** _T_ ; _k_ ) is generated by the _k_ -th agent. Note that each trajectory does include an identifier of the agent that generated it. The ego-agent also gathers its own experience by interacting with the environment, collecting data _B_ = _{_ ( **s** _,_ **a** _,_ **s**<sup>_′_</sup> _, r_<sup>ego</sup> ) _}_ . Due to the lack of reward annotations in _D_ , and the fact that the data may be irrelevant to the 

**Successor Features and Inverse TD Learning** 

ΨΦ **-Learning: RL with Demonstrations using** 

ego-agent’s task, it is not trivial to combine demonstrations from _D_ with the ego-agent’s experience _B_ . 

### **2.2. Successor Features and Cumulants** 

To make use of the demonstrations _D_ , we wish to capture the notion that while the agents’ rewards may differ, they share the same environment. To do so we turn to the framework of successor features (SFs) (Barreto et al., 2017), in which rewards are decomposed into cumulants and preferences: 

**Definition 1** (Cumulants and Preferences) **.** _The (one-step) rewards are decomposed into task-agnostic_ cumulants Φ( **s** _,_ **a** ) _∈_ R<sup>_d_</sup> _, and task-specific_ preferences **w** _∈_ R<sup>_d_</sup> _:_ 



The preferences **w** are a representation of a possible goal in the world _C_ , in the sense that each **w** gives rise to a task _M_<sup>**w**</sup> = _⟨C, R_<sup>**w**</sup> _⟩_ . We use ‘task’, ‘goal’, and ‘preferences’ interchangeably when context makes it clear whether we are referring to **w** itself, or the corresponding _M_<sup>**w**</sup> or _R_<sup>**w**</sup> . The action-value function for a policy _π_ in _M_<sup>**w**</sup> is then a function of the preferences **w** and the _π_ ’s successor features. 

**Definition 2** (Successor Features) **.** _For a given discount factor γ ∈_ [0 _,_ 1) _, policy π and cumulants_ Φ( **s** _,_ **a** ) _∈_ R<sup>_d_</sup> _, the successor features (SFs) for a state_ **s** _and action_ **a** _are:_ 



The _i_ -th component of Ψ<sup>_π_</sup> ( **s** _,_ **a** ) gives the expected discounted sum of Φ( **s** _,_ **a** )’s _i_ -th component, when starting from state **s** , taking action **a** and then following policy _π_ . Intuitively, cumulants Φ can be seen as a vector-valued reward function and SFs Ψ<sup>_π_</sup> the corresponding vector-valued state-action value function for policy _π_ . 

An action-value function is then given by the dot product of the preferences **w** and _π_ ’s SFs: 



_Proof._ See (Barreto et al., 2017). 

Note that if we have Ψ<sup>_π_</sup> , the value of _π_ for a new preference **w**<sup>_′_</sup> can be easily computed. This property allows the successor features of a set of policies to be repurposed for accelerating policy updates, as follows. 

**Definition 3** (Generalised Policy Improvement) **.** _Given a set of policies_ Π = _{π_ 1 _, . . . , πK} and a task with reward function R, generalised policy improvement (GPI) is the definition of a policy π_<sup>_′_</sup> _s.t._ 



Provided the SFs of a set of policies, i.e., _{_ Ψ<sup>_πk_</sup> _}_<sup>_K_</sup> _k_ =1<sup>, we can</sup> apply GPI to derive a new policy _π_<sup>_′_</sup> whose performance on a task **w** is no worse that the performance of any of _π ∈_ Π on the same task, given by 



Eqn. (5) suggests that if we could estimate the SFs of other agents, we could utilise them for improving the ego-agent’s policy with GPI. However, to do so with conventional methods we would require access to their rewards, cumulants and/or preferences. In our setting, we can only observe their sequence of states and actions (Section 2.1). Next, we introduce our method that only requires no-reward demonstrations to estimate SFs and can be integrated seamlessly with GPI for accelerating reinforcement learning. 

## **3. Accelerating RL with Demonstrations** 

We now present a novel method, ΨΦ-learning, that leverages reward-free demonstrations to accelerate RL, shown in Figure 1. Our approach consists of two components: (i) a novel inverse reinforcement learning algorithm, called _inverse temporal difference_ (ITD) _learning_ , for learning cumulants, per-agent successor features and corresponding agent preferences from demonstration without reward labels, and (ii) a novel RL algorithm that combines ITD with generalised policy improvement (GPI, Section 2.2). 

### **3.1. Inverse Temporal Difference Learning** 

Given demonstrations without rewards, _D_ , we model the agents that generated the data (i.e., blue nodes in Figure 1) as soft-optimal for an _unknown_ task. In particular, the _k_ -th agent’s policy is soft-optimal under task **w**<sup>_k_</sup> and is given by 



We choose to represent the action-value functions of the other agents with their SFs and preferences to enable GPI, and to expose task- and policy-agnostic structure in the form of shared cumulants Φ. The _k_ -th agent’s successor features are temporally consistent with these cumulants Φ 



To learn these quantities from _K_ demonstrators, we parameterise the SFs with **_θ_**<sup>Ψ</sup><sup>_k_</sup> , preferences with **w**<sup>_k_</sup> , and shared cumulants with **_θ_** Φ. A schematic of the model architecture and further details are provided in Appendix B. The parameters are learned by minimising a behavioural cloning and SFs TD loss based on equations (6) and (7). 

**Behavioural cloning loss.** Given demonstrations generated only by the _k_ -th agent, i.e., _D_<sup>_k_</sup> _⊂D_ , we train its successor features **_θ_** Ψ _k_ and the preferences **w**<sup>_k_</sup> by minimising 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

the negative log-likelihood of the demonstrations 



Importantly, Eqn. (8) reflects the fact that along a trajectory _τ_ , the successor features are a function of the state and action at each time-step, **s** _t_ and **a** _t_ , while the preferences **w**<sup>_k_</sup> are learnable but consistent across time and trajectories. The direction of the preference **w**<sup>_k_</sup> indicates the goal of the agent _k_ by showing how relatively rewarding it finds the different dimensions of the cumulant features Φ. The learned magnitude of **w**<sup>_k_</sup> can further capture how greedily the agent _k_ pursues this goal. 

A sparsity prior, i.e., _L_ 1 loss, on preferences **w**<sup>_k_</sup> is also used to promote disentangled cumulant dimensions (see Figure 4). We found the _L_ 1 loss made the algorithm more robust to the choice of dimension of Φ (see Figure 13 in the Appendix), but did not substantially affect overall performance. 

**Inverse temporal difference loss.** The cumulant parameters **_θ_** Φ are trained to be TD-consistent with all agents’ successor features. This procedure inverts<sup>1</sup> the standard TDlearning framework for SFs (Dayan, 1993; Barreto et al., 2017) where they are trained to be consistent with a fixed cumulant Φ. Instead, we first train the SFs and preference vectors to ‘explain’ the other agents’ behaviour with the behavioural cloning loss Eqn. (8), and then train **_θ_** Φ, **_θ_** Ψ _k_ to be (self-)consistent with these SFs by minimising 



In practice, our ITD-learning algorithm alternates between minimising _L_ BC- _Q_ for training only the successor features and preferences, and _L_ ITD for training both the shared cumulants and successor features, provided only with no-reward demonstrations, as illustrated in blue in Figure 1. 

From the definition of cumulants and preferences, we can recover the _k_ -th demonstrator’s reward, by applying Eqn. (1), i.e., _R_<sup>_k_</sup> ( **s** _,_ **a** ) _≈_ Φ( **s** _,_ **a** ; **_θ_** Φ)<sup>_⊤_</sup> **w**<sup>_k_</sup> . Our ITD algorithm returns both Q-functions that can be used for imitating a demonstrator and an explicit reward function for each agent, requiring only access to demonstrations without any online interaction with the simulator. Hence ITD-learning is an offline multi-task IRL algorithm. ITD is summarised in Algorithm 1. 

**Theorem 1** (Validity of the ITD Minimiser) **.** _The minimisers of LBC-Q and LITD are potentially-shaped cumulants that explain the observed reward-free demonstrations._ 

_Proof._ See Appendix C. 

> 1Hence the name _inverse TD learning_ . 

**Single-task setting.** To gain more intuition about the ITD algorithm, consider the simpler case of performing IRL with demonstrations from a single policy. This obviates the need for a representation of preferences, so we can use **w** = 1. In this case Ψ is the action-value function _Q_ and Φ is simply the reward _R_ . Minimising (8) reduces to finding a _Q_ -function whose softmax gives the observed policy, and minimising (9) finds a scalar reward that explains the _Q_ -function. Our more general formulation, with cumulants Φ in place of a scalar reward, allows us to perform ITD-learning on demonstrations from many policies, and to efficiently transfer to new tasks, as we show next. 

### **3.2.** ΨΦ **-Learning with No-Reward Demonstrations** 

Now we present our main contribution, ΨΦ-learning, which combines our ITD inverse RL algorithm with RL and GPI, using no-reward demonstrations from other agents to accelerating the ego-agent’s learning. ΨΦ-learning is depicted in Figure 1 and summarised in Algorithm 1. 

ΨΦ-learning is an off-policy algorithm based on Q- learning (Watkins & Dayan, 1992; Mnih et al., 2013). The action-value function is represented with successor features, Ψ<sup>ego</sup> , and preferences, **w**<sup>ego</sup> , as in Eqn. (3). The ego-agent interacts with the environment, storing its experience in a replay buffer, _B ←B ∪{_ ( **s** _,_ **a** _,_ **s**<sup>_′_</sup> _, r_<sup>ego</sup> ) _}_ . The ΨΦ-learner also has estimates for the cumulants, per-agent SFs and preferences obtained with ITD from the demonstrations _D_ . 

**Reward loss.** The ego-rewards, _r_<sup>ego</sup> , are used to ground the cumulants Φ and the preferences **w**<sup>ego</sup> , via the loss 



Importantly, we share the _same_ cumulants between the ITDlearning from other agents and the ego-learning, so that they span the joint space of reward functions. This can be also seen as a representation learning method, where by enforcing all agents, including the ego-agent, to share the same Φ, we transfer information about salient features of the environment from learning about one agent to benefit learning about all agents. 

**Temporal difference learning.** The ego-agent’s successor features are learned using two losses. First, we train the SFs to fit the Q-values using the Bellman error 



ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

We additionally train the successor features to be selfconsistent (i.e. to satisfy Equation 2) using a TD loss _L_ TD-Ψ. 



**GPI behavioural policy.** Provided SFs estimates for the other agents, _{_ **_θ_** Ψ _k }_<sup>_K_</sup> _k_ =1<sup>,andtheego-agent</sup><sup>**_θ_**Ψego,andin-</sup> ferred ego preferences, **w**<sup>ego</sup> , we adopt an action selection mechanism according to the GPI rule in Eqn. (5) 



The GPI step lets the agent estimate the value of the demonstration policies on its current task, and then copy the policy that it predicts will be most useful. We combat model overestimation by acting pessimistically with regard to an ensemble of two successor features approximators. If the agent’s estimated values are accurate and the demonstration policies are useful for the ego task, the GPI policy can obtain good performance faster than policy iteration with only the ego value function. The next section quantifies this claim. 

**Performance Bound.** Given a set of demonstration task vectors _{wk}_<sup>_K_</sup> _k_ =1<sup>and successor features for the correspond-</sup> ing optimal policies _{_ Ψ<sup>_πk_</sup> _}_<sup>_K_</sup> _k_ =1<sup>, Barreto et al. (2017) show</sup> that it is possible to bound the performance of the GPI policy on the ego-agent task _w_<sup>_′_</sup> as a function of the distance of _w_<sup>_′_</sup> from the closest demonstration task _wj_ , and the value approximation error of the predicted value functions _Q_ �<sup>_π_</sup> _i_ = Ψ<sup>_π_</sup> _iw_<sup>_′_</sup> . We extend this result to explicitly account for the reward approximation error _δr_ obtained by the the learned cumulants and the SF approximation error _δ_ Ψ. 

**Theorem 2** (Generalisation Bound of ΨΦ-Learning) **.** _Let π_<sup>_∗_</sup> _be the optimal policy for the ego task w_<sup>_′_</sup> _and let π be the GPI policy obtained from {Q_<sup>˜</sup><sup>_πi_</sup> _}, with δr, δ_ Ψ _the reward and successor feature approximation errors. Then ∀s, a_ 



_Proof._ See Appendix C for a formal statement. 

In settings where the agent has a good reward and SFs approximation, and the ego task vector _w_<sup>_′_</sup> is close to the demonstration tasks, Theorem 2 says that the ego-agent will attain near-optimal performance from the start of training. 

## **4. Experiments** 

We conduct a series of experiments to determine how well ΨΦ-learning functions as an RL, IRL, imitation learning, and transfer learning algorithm. 

**Baselines.** We benchmark against the following methods: (i) **DQN:** Deep Q-learning (Mnih et al., 2013), (ii) **BC:** Behaviour Cloning, a simple imitation learning method in which we learn _p_ ( **a** _|_ **s** ) via supervised learning on the demonstration data, (iii) **DQN+BC-AUX:** DQN with an additional behavior-cloning auxiliary loss (Hernandez-Leal et al., 2019), (iv) **GAIL:** Generative Adversarial Imitation Learning (Ho & Ermon, 2016), which uses a GAN-like approach to approximate the expert policy, and (v) **SQILv2** : Soft Q Imitation Learning (Reddy et al., 2019), a recently proposed imitation technique that combines imitation and RL, and works in the absence of rewards. For high-dimensional environments, we replace DQN with **PPO** , Proximal Policy Optimization (Schulman et al., 2017). Both DQN and PPO are trained to optimize environment reward through experience, and do not have access to other agents’ experiences. 

### **4.1. Environments** 

Experiments are conducted using four environments, shown in Figure 2. We cover a broad range of problem setting, including both multi-agent and single-agent environments, as well as learning online during RL training, or offline from previously collected demonstrations. 

**Highway** (Leurent, 2018) is a multi-agent autonomous driving environment in which the ego-agent must safely navigate around other cars and reach its goal. The other agents follow near-optimal scripted policies for various goals, depending on the scenario. In the **single-task** scenario, other agents have the same objective as the ego-agent, so their experience is directly relevant. In the **adversarial task** , the other agents do not move, and the ego-agent has to accelerate and go to a particular lane while avoiding other vehicles. Finally, in the **multi-task** scenario, the other agents and ego-agent have different preferences over target speed, preferred lane, and following distance. We consider the multi-task scenario to be the most realistic and representative of real highway driving with human drivers. In addition to highway driving, we also study the more complex **Roundabout** task. Roundabout is inherently multi-task, in that other agents randomly exit either the first or second exit, while the ego-agent must learn to take the third exit. 

**CoinGrid** is a single-agent grid-world, environment containing goals of different colours. We collect offline trajectories of pre-trained agents with preferences for different goals. red. During training, the ego-agent is only rewarded for collecting a subset of the possible goals. We can then test how well the ego-agent is able to transfer to a goal that was never 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 











<!-- Start of picture text -->
(a) Highway (b) Roundabout (c) CoinGrid (d) Fruit Bot<br><!-- End of picture text -->

_Figure 2._ Environments studied in this paper. Environments (a-b) are multi-agent environments in which the ego-agent must learn online from other agents, and learn to navigate around other agents in the environment (see Section 4.2). Environments (c-d) are single-agent. In environment (c) we test whether the ego-agent can learn offline from a set of demonstrations previously collected by other agents (see Section 4.5. Environment (d) is used to test whether our method can scale to more complex, high-dimensional tasks (see Section 4.2). 

experienced during training (Section 4.5). This environment also enables learning easily interpretable preference vectors, allowing us to visualize how well our method works as an IRL method for inferring rewards (Section 4.3). 

**FruitBot** is a high-dimensional, procedurally generated, single-agent environment from the OpenAI ProcGen (Cobbe et al., 2020) suite. We use FruitBot to test whether ΨΦlearning can scale up to more complex RL environments, requiring larger deep neural network architectures that learn directly from pixels. The agent must navigate around randomly generated obstacles while collecting fruit, and avoiding other objects and walls. To create a multi-task version of FruitBot, we define additional tasks which vary agents’ preferences over collecting objects in the environment, and train PPO baselines on these task variants. The ego-agent observes the states and actions of these trained agents playing the game in parallel with its own interactions. 

### **4.2. Accelerating RL with No-Reward Demonstrations** 

This section addresses two hypotheses: **H1:** When the unlabelled demonstrations are relevant, ΨΦ-learning can accelerate or improve performance of the ego-agent when learning with online RL; and **H2:** If the demonstrations are irrelevant, biased, or are generated by sub-optimal demonstrators, ΨΦ-learning can perform at least as well as standard RL. 

Figure 3 shows the results of ΨΦ-learning and the baselines in the Highway and FruitBot environments. In the single-task scenario (3a), when other agents’ experience is entirely relevant to the ego-agent’s task, imitation learning methods like BC and SQILv2 learn fastest. DQN learns slowly because it does not use the other agents’ experience. However, ΨΦ-learning achieves competitive results, outperforming DQN+BC-Aux (Hernandez-Leal et al., 2019; Ndousse et al., 2020). In the adversarial task (3b), the other agents’ behaviors are irrelevant for the ego-agent’s task, so imitation learning (BC and SQILv2) performs poorly, while traditional RL techniques (DQN and DQN+BC-Aux) perform best. The performance of ΨΦ-learning does not suffer 

like other imitation learning methods; instead, it retains the performance of standard RL ( **H2** ). ΨΦ-learning can flexibly reap the benefits of either imitation learning or RL, depending on what is most beneficial for the task. 

The multi-task scenario (3c) is the most realistic autonomous driving task, in which other agents navigate the highway with varying driving styles. Here, ΨΦ-learning clearly outperforms all other methods, suggesting it can leverage information about other agents’ preferences in order to learn the underlying task structure of the environment, acclerating performance on the ego-agent’s RL task ( **H1)** . FruitBot (3d) gives consistent results, showing that ΨΦ-learning scales well to high-dimensional, single-agent tasks while still outperforming BC, SQIL, PPO, and PPO+BC-Aux. 

### **4.3. Inverse Reinforcement Learning** 

We now test hypothesis **H3:** ITD is an effective IRL method, and can accurately infer other agents’ rewards. We present a quantitative and qualitative study of the rewards for other agents that are inferred by ITD, as well as the learned cumulants and preferences. Here, we focus solely on offline IRL and use only ITD to learn from offline reward-free demonstrations, without any ego-agent experience. 

To quantitatively evaluate how well ITD can infer rewards, we train an RL agent on the inferred reward function, and compare the performance to other imitation learning and IRL methods. Table 1 gives the performance in terms of normalised returns on all three environments. Using ITD to infer rewards results in significantly higher performance than BC and SQIL, in two environments, and competitive performance in FruitBot. We note that unlike ΨΦ-learning, BC and SQIL directly learn a policy from demonstrations, and do not actually infer an explicit reward function. In contrast, GAIL does infer an explicit reward function, and ITD gives consistently higher performance than GAIL in all three environments. These results demonstrate that ITD is an effective IRL technique ( **H3** ). 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 



<!-- Start of picture text -->
ΨϕL  (ours) RL BC RL + BC-Aux SQILv2<br>1.0 1.0 1.0 4<br>0.5 0.5 0.5 2<br>0.0 0.0 0.0 0<br>10 2 10 3 10 4 10 2 10 3 10 4 10 2 10 3 10 4 10 7 10 8<br>Timesteps Timesteps Timesteps Timesteps<br>(a) Highway: Single-task (b) Highway: Adversarial (c) Highway: Multi-task (d) FruitBot<br>Returns Returns Returns Returns<br><!-- End of picture text -->

_Figure 3._ Learning curves for ΨΦ-learning and baselines in three tasks in the multi-agent Highway environment (a-c), and in single-agent FruitBot (d). Tasks (a) and (b) represent extreme cases where either RL or imitation learning is irrelevant. In (a) other agents have the same task as the ego-agent, so imitation learning excels. In the adversarial task (b), other agents exhibit degenerative behaviour, so imitation learning performs extremely poorly and traditional RL (DQN) excels. In both of these extreme cases, ΨΦ-learning achieves good performance, showing it can flexibly reap the benefits of either imitation or RL as appropriate. Task (c) is most realistic; here, other agents have varied preferences and goals that may or may not relate to the ego-agent’s task. ΨΦ-learning clearly outperforms baseline techniques. Similar results are shown in Fruitbot (d), showing that ΨΦ-learning scales well to high-dimensional environments, consistently outperforming baselines like PPO and SQIL. We plot mean performance over 3 runs and individual runs with alpha. 

_Table 1._ We evaluate how well ΨΦ-learning is able to infer the correct reward function by training an RL agent on the inferred rewards, and comparing this to alternative imitation learning methods in three environments. All methods are trained on expert demonstrations. A “ _♦_ ” indicates methods that infer an _explicit_ reward function and then use one of DQN or PPO to train an RL agent, depending on the environment. A “ _♣_ ” indicates methods that directly learn a policy from demonstrations. A “ _†_ ” indicates methods that use privileged task id information for handling multi-task demonstrations. We report mean and standard error of _normalised returns_ over 3 runs, where higher-is-better and the performance is upper bounded by 1 _._ 0, reached by the same RL agent, trained with the ground truth reward function. 

|**Methods**<br>|Roundabout<sup>DQN</sup>|CoinGrid<sup>DQN</sup>|FruitBot<sup>PPO</sup>|
|---|---|---|---|
|BC<sup>_†♣_</sup>(Pomerleau,1989)|0_._81_±_0_._02|0_._69_±_0_._06|**0.37**_±_0_._02|
|SQIL<sup>_†♣_</sup>(Reddy et al.,2019)|0_._85_±_0_._02|0_._64_±_0_._05|**0.35**_±_0_._03|
|GAIL<sup>_†♦_</sup>(Ho & Ermon,2016)|0_._77_±_0_._07|0_._73_±_0_._02|0_._31_±_0_._02|
|ITD<sup>_♦_</sup>(ours, cf. Section3.1)|**0.92**_±_0_._01|**0.77**_±_0_._03|**0.35**_±_0_._04|



Qualitatively, we can evaluate how well the cumulants inferred by ITD in the CoinGrid environment span the space of possible goals. We compute the learned cumulants _φ_<sup>ˆ</sup> ( _s_ ) for each square _s_ in the grid. Figure 4a shows the original CoinGrid game, and Figure 4b-4d shows the first three dimensions of the learned cumulant vector, _φ_<sup>ˆ</sup> 1- _φ_<sup>ˆ</sup> 3 (the rest are given in the Appendix). We find that _φ_<sup>ˆ</sup> 1 is most active for red coins, _φ_<sup>ˆ</sup> 2 for green, and _φ_<sup>ˆ</sup> 3 for yellow. Clearly, ITD has learned cumulant features that span the space of goals for this game. See Appendix E for more details and visualisations of the learned rewards and preferences. 

### **4.4. Imitation learning** 

Here, we investigate hypothesis **H4:** ΨΦ-learning works as an effective imitation learning method, allowing for accurate prediction of other agents’ actions. To test this hypothesis, we train other agents in the Roundabout environment, then split no-reward demonstrations from these agents into a train 





<!-- Start of picture text -->
(a) CoinGrid (b)  φ 1 (c)  φ 2 (d)  φ 3<br><!-- End of picture text -->

_Figure 4._ Qualitative evaluation of the learned cumulants in the CoinGrid task. Cumulants _φ_ 1, _φ_ 2, and _φ_ 3 seem to capture the red, green, and yellow blocks, respectively. Therefore, linear combinations of the learned cumulants can represent arbitrary rewards in the environment, which involve stepping on the coloured blocks. 

dataset (80%) and a held-out test dataset. We use the train dataset to run ITD, which means that we use the data to learn both Φ and the Ψ and **w** for other agents. Because it is specifically designed to accurately predict other agents’ actions, we use BC as the baseline. We compare this to using only ITD, and using the full ΨΦ-learning algorithm including ITD _and_ learning from RL and experience to update the shared cumulants Φ. 

Accuracy in predicting other agents’ actions on the held-out test set is used to measure imitation learning performance. Figure 5 shows accuracy over the course of training. At each phase change marked in the figure, the ego-agent is given a new task, to test how the representation learning benefits from diverse ego-experience. We see that although BC obtains accurate train performance, it generalises poorly to the test set, reaching little over 80% accuracy. Without RL, ΨΦ-learning achieves similar performance. However, when using RL to improve imitation, ΨΦ-learning performs well on both the train and test set, achieving markedly higher accuracy ( _≈_ 95%) in predicting other agents’ behaviour. This suggests that when ΨΦ-learning uses RL and interaction with the world to improve the estimation of the shared cumulants Φ, this in turn improves its ability to model the _Q_ 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

function of other agents and predict their behaviour. Further, ΨΦ-learning adapts well when the agent’s goal changes, since it uses SFs to disentangle the representation of an agent’s goal from environment dynamics. Taken together, these results demonstrate that ΨΦ-learning also works as a competitive imitation learning method ( **H4** ). 



<!-- Start of picture text -->
100 ΨϕL  (ours)<br>ITD<br>80<br>BC<br>(new task)<br>60<br>train<br>0 10000 20000<br>test<br>Timesteps<br>Accuracy %<br><!-- End of picture text -->

_Figure 5._ Test accuracy in predicting other agents’ actions. The shared cumulants Φ for modelling others- and ego- reward functions allow our ΨΦ-learner to improve its ability to predict others’ actions by experiencing new ego-tasks. Pure imitation learning and our ITD inverse RL methods achieve high train accuracy but they do not have a mechanism for utilising RL experience to improve their generalisation to the test set as new tasks are provided. 

### **4.5. Transfer and Few-Shot Generalisation** 

Since SFs have been shown to improve generalization and transfer in RL, here we test hypothesis **H5:** ΨΦ-learning will be able to generalize effectively to new tasks in a fewshot transfer setting. Using the CoinGrid environment, it is possible to precisely test whether the ego-agent can generalise to a task it has never experienced during training. Specifically, we would like to determine whether: (i) the ego-agent can generalise to tasks it was never rewarded for during training (but which it may have seen other agents demonstrate), and (ii) the ego-agent can generalise to tasks not experienced by _any_ agents during training. 

Table 2 shows the results of transfer experiments in which agents are given 0, 1, or 100 additional training episodes to adapt to a new task. Unlike SQIL, ΨΦ-learning is able to adapt 0-shot to obtain some reward on the new tasks, and fully adapt after a single episode to achieve the maximum reward on all transfer tasks. This is because ΨΦ-learning uses SFs to disentangle preferences (goals) in the task representation, and learn about the space of possible preferences from observing other agents. To adapt to a new task, it need only infer the correct preference vector. Task inference is trivially implemented as a least squares regression problem, see Eqn. (10): Having experienced _B_<sup>new</sup> in the new task, the ΨΦ-learner identifies the preference vector for the new task by solving min **w** � _B_<sup>new</sup><sup>_L_R(</sup><sup>**_θ_**Φ</sup><sup>_,_</sup><sup>**w**).In contrast, SQIL</sup> requires 100 episodes to reach the same performance. 

## **5. Related Work** 

**Learning from demonstrations.** Learning from demonstrations, also referred to as imitation learning (IL, Widrow & Smith, 1964; Pomerleau, 1989; Atkeson & Schaal, 1997), is an attractive framework for sequential decision making when reliable, expert demonstrations are available. Early work on IL assumed access to high-quality demonstrations and aimed to match the expert policy (Pomerleau, 1991; Heskes, 1998; Ng et al., 2000; Abbeel & Ng, 2004; Billard et al., 2008; Argall et al., 2009; Ziebart et al., 2008). Building on this assumption, many recent works have studied various aspects of both _single-task_ (Ratliff et al., 2006; Wulfmeier et al., 2015; Choi & Kim, 2011; Finn et al., 2016b; Ho & Ermon, 2016; Finn et al., 2016a; Fu et al., 2017; Zhang et al., 2018; Rahmatizadeh et al., 2018) and _multi-task_ (Dimitrakakis & Rothkopf, 2011; Mulling et al.¨ , 2013; Stulp et al., 2013; Deisenroth et al., 2014; Sharma et al., 2018; Codevilla et al., 2018; Fu et al., 2019; Rhinehart et al., 2020; Filos et al., 2020) IL. However, these methods are all limited by the performance of the demonstrator that they try to imitate. Learning from suboptimal demonstrations has been studied by Coates et al. (2008); Grollman & Billard (2011); Zheng et al. (2014); Choi et al. (2019); Shiarlis et al. (2016); Brown et al. (2019), enabling, under certain assumptions, imitation learners to surpass their demonstrators’ performance. In contrast, our method integrates demonstrations into an online reinforcement learning pipeline and can use the demonstrations to improve learning on a new task. Our inverse TD (ITD) learning offline multitask inverse reinforcement learning algorithm is similar to the Cascaded Supervised IRL (CSI) approach (Klein et al., 2013). However, CSI assumes a single-task, deterministic expert while ITD does not. 

**Reinforcement learning with demonstrations.** Demonstration trajectories have been used to accelerate the learning of RL agents (Taylor et al., 2011; Vecerik et al., 2017; Rajeswaran et al., 2017; Hester et al., 2018; Gao et al., 2018; Nair et al., 2018; Paine et al., 2018; 2019), as well as demonstrations where actions and/or rewards are unknown (Borsa et al., 2017; Torabi et al., 2018; Sermanet et al., 2018; Liu et al., 2018; Aytar et al., 2018; Brown et al., 2019). In contrast to the standard imitation learning setup, these methods allow improving over the expert performance as the policy can be further fine-tuned via reinforcement learning. Offline reinforcement learning with online fine-tuning (Kalashnikov et al., 2018; Levine et al., 2020) can be framed under this settings too. Our method builds on the same principles, however, unlike these works, we do not assume that the demonstration data either come with reward annotations, or that they relate to the same task the RL agent is learning (i.e., we learn from multi-task demonstrations which may include irrelevant tasks). 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

_Table 2._ We evaluate how well ΨΦ-learning is able to transfer to new tasks in a few-shot fashion. We construct a multi-task variant of the CoinGrid environment: The ego-agent is provided demonstrations for either capturing only red coins R or only green coins G. Then it is evaluated on 4 different tasks: collecting (i) both red and green coins R+G, (ii) collecting red and avoiding green coins R-G, (iii) avoiding red and collecting green coins -R+G and (iv) avoiding both red and green coins -R-G. A “ _♦_ ” indicates methods that use a single model for all tasks, while “ _♣_ ” indicates methods that require one model per task, i.e., they comprise of 4 models. Because it disentangles preferences from task representation, ΨΦ-learning is able to adapt to reach optimal performance on the new tasks after a single episode or improve intra-episode from the first episode after experiencing the first rewards. In contrast, SQIL takes 100 episodes to adapt. 

|||0-|shot|||1-|shot|||100|-shot||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Methods**|R+G|R-G|-R+G|-R-G|R+G|R-G|-R+G|-R-G|R+G|R-G|-R+G|-R-G|
|SQILv2<sup>_♣_</sup>(Reddy et al.,2019)|1_._0_±_0_._0|0_._0_±_0_._0|0_._0_±_0_._0|_−_1_._0_±_0_._0|**1.0**_±_0_._0|0_._0_±_0_._0|0_._0_±_0_._0|_−_1_._0_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|
|ΨΦ-learning<sup>_♦_</sup>(ours, cf. Section3.2)|1_._0_±_0_._0|**0.2**_±_0_._1|**0.2**_±_0_._1|_−_**0.4**_±_0_._2|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|**1.0**_±_0_._0|



**Successor features.** Successor features (SFs) are a generalisation of the successor representation (Dayan, 1993) for continuous state and action spaces (Barreto et al., 2017). Prior work has used SFs for (i) zero-shot transfer (Barreto et al., 2017; Borsa et al., 2018; Barreto et al., 2020); (ii) exploration (Janz et al., 2019; Machado et al., 2020); (iii) skills discovery (Machado et al., 2017; Hansen et al., 2019); (iv) hierarchical RL (Barreto et al., 2019) and theory of mind (Rabinowitz et al., 2018). Nonetheless, in all the aforementioned settings, direct access to the rewards or cumulants was provided. Our method, instead, uses demonstrations without reward labels for inferring the cumulants and learning the corresponding SFs. More closely to this work, Lee et al. (2019) propose learning cumulants and successor features for a _single-task_ IRL setting. Their approach differs from ours in two key respects: first, they use a learned dynamics model to learn the cumulants. Second, the learned SFs are used for representing the action-value function, not to inform the behaviour policy with GPI. 

**Model of others in multi-agent learning.** Our method draws inspiration and builds on the multi-agent learning setting, where multiple agents participate in the same environment and the states, actions of others are observed (Davidson, 1999; Lockett et al., 2007; He et al., 2016; Jaques et al., 2019). However, we do not explore _strategic_ settings, where recursive reasoning (Stahl, 1993; Yoshida et al., 2008) is necessary for optimal behaviour. 

## **6. Discussion** 

We have presented two major algorithmic contributions. The first, ITD, is a novel and flexible offline IRL algorithm that discovers salient task-agnostic environment features in the form of cumulants, as well as learning successor features and preference vectors for each agent which provides demonstrations. The second, ΨΦ-learning, combines ITD with RL from online experience. This makes efficient use of unlabelled demonstrations to accelerate RL, and comes with theoretical worst-case performance guarantees. We showed empirically the advantages of these algorithms over various baselines: how imitation with ITD can improve RL and 

enable zero-shot transfer to new tasks, and how experience from online RL can help to improve imitation in turn. 

**Future Work.** We want to explore ways to: (i) adapt ΨΦlearning to multi-agent _strategic_ settings, where coordination and opponent modelling (Albrecht & Stone, 2018) are essential and (ii) use a universal successor features approximator (Borsa et al., 2018) for ITD, overcoming its current, linear scaling with the number of distinct demonstrators. 

**Acknowledgements.** We thank Pablo Samuel Castro, Anna Harutyunyan, RAIL, OATML and IRIS lab members for their helpful feedback. We also thank the anonymous reviewers for useful comments during the review process. A.F. is funded by a J.P.Morgan PhD Fellowship and C.L. is funded by an Open Phil AI Fellowship. 

## **References** 

- Abbeel, P. and Ng, A. Y. Apprenticeship learning via inverse reinforcement learning. In _Proceedings of the twenty-first international conference on Machine learning_ , pp. 1, 2004. 

- Albrecht, S. V. and Stone, P. Autonomous agents modelling other agents: A comprehensive survey and open problems. _Artificial Intelligence_ , 258:66–95, 2018. 

- Argall, B. D., Chernova, S., Veloso, M., and Browning, B. A survey of robot learning from demonstration. _Robotics and autonomous systems_ , 57(5):469–483, 2009. 

- Atkeson, C. G. and Schaal, S. Robot learning from demonstration. In _ICML_ , volume 97, pp. 12–20. Citeseer, 1997. 

- Aytar, Y., Pfaff, T., Budden, D., Paine, T. L., Wang, Z., and de Freitas, N. Playing hard exploration games by watching youtube. _arXiv preprint arXiv:1805.11592_ , 2018. 

- Babuschkin, I., Baumli, K., Bell, A., Bhupatiraju, S., Bruce, J., Buchlovsky, P., Budden, D., Cai, T., Clark, A., Danihelka, I., Fantacci, C., Godwin, J., Jones, C., Hennigan, T., Hessel, M., Kapturowski, S., Keck, T., Kemaev, I., King, M., Martens, L., Mikulik, V., Norman, T., Quan, 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

- J., Papamakarios, G., Ring, R., Ruiz, F., Sanchez, A., Schneider, R., Sezener, E., Spencer, S., Srinivasan, S., Stokowiec, W., and Viola, F. The DeepMind JAX Ecosystem, 2020. URL http://github.com/deepmind. 

- Barreto, A., Dabney, W., Munos, R., Hunt, J. J., Schaul, T., van Hasselt, H. P., and Silver, D. Successor features for transfer in reinforcement learning. In _Advances in neural information processing systems_ , pp. 4055–4065, 2017. 

- Barreto, A., Borsa, D., Hou, S., Comanici, G., Aygun, E.,¨ Hamel, P., Toyama, D., Mourad, S., Silver, D., Precup, D., et al. The option keyboard: Combining skills in reinforcement learning. In _Advances in Neural Information Processing Systems_ , pp. 13052–13062, 2019. 

- Barreto, A., Hou, S., Borsa, D., Silver, D., and Precup, D. Fast reinforcement learning with generalized policy updates. _Proceedings of the National Academy of Sciences_ , 117(48):30079–30087, 2020. 

- Biewald, L. Experiment tracking with weights and biases, 2020. URL https://www.wandb.com/. Software available from wandb.com. 

- Billard, A., Calinon, S., Dillmann, R., and Schaal, S. Survey: Robot programming by demonstration. _Handbook of robotics_ , 59(BOOK ~~C~~ HAP), 2008. 

- Borsa, D., Piot, B., Munos, R., and Pietquin, O. Observational learning by reinforcement learning. _arXiv preprint arXiv:1706.06617_ , 2017. 

- Borsa, D., Barreto, A., Quan, J., Mankowitz, D., Munos, R., van Hasselt, H., Silver, D., and Schaul, T. Universal successor features approximators. _arXiv preprint arXiv:1812.07626_ , 2018. 

- Boyd, S., Boyd, S. P., and Vandenberghe, L. _Convex optimization_ . Cambridge university press, 2004. 

- Bradbury, J., Frostig, R., Hawkins, P., Johnson, M. J., Leary, C., Maclaurin, D., Necula, G., Paszke, A., VanderPlas, J., Wanderman-Milne, S., and Zhang, Q. JAX: composable transformations of Python+NumPy programs, 2018. URL http://github.com/google/jax. 

- Brown, D. S., Goo, W., Nagarajan, P., and Niekum, S. Extrapolating beyond suboptimal demonstrations via inverse reinforcement learning from observations. _arXiv preprint arXiv:1904.06387_ , 2019. 

- Chevalier-Boisvert, M., Willems, L., and Pal, S. Minimalistic gridworld environment for openai gym. https:// github.com/maximecb/gym-minigrid, 2018. 

- Chevalier-Boisvert, M., Bahdanau, D., Lahlou, S., Willems, L., Saharia, C., Nguyen, T. H., and Bengio, Y. BabyAI: 

First steps towards grounded language learning with a human in the loop. In _International Conference on Learning Representations_ , 2019. URL https://openreview. net/forum?id=rJeXCo0cYX. 

- Choi, J. and Kim, K.-E. Inverse reinforcement learning in partially observable environments. _Journal of Machine Learning Research_ , 12:691–730, 2011. 

- Choi, S., Lee, K., and Oh, S. Robust learning from demonstrations with mixed qualities using leveraged gaussian processes. _IEEE Transactions on Robotics_ , 35(3):564– 576, 2019. 

- Coates, A., Abbeel, P., and Ng, A. Y. Learning for control from multiple demonstrations. In _Proceedings of the 25th international conference on Machine learning_ , pp. 144–151, 2008. 

- Cobbe, K., Hesse, C., Hilton, J., and Schulman, J. Leveraging procedural generation to benchmark reinforcement learning. In _International conference on machine learning_ , pp. 2048–2056. PMLR, 2020. 

- Codevilla, F., Miiller, M., L´opez, A., Koltun, V., and Dosovitskiy, A. End-to-end driving via conditional imitation learning. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 1–9. IEEE, 2018. 

- Davidson, A. Using artificial neural networks to model opponents in texas hold’em. _Unpublished manuscript_ , 1999. 

- Dayan, P. Improving generalization for temporal difference learning: The successor representation. _Neural Computation_ , 5(4):613–624, 1993. 

- Deisenroth, M. P., Englert, P., Peters, J., and Fox, D. Multitask policy search for robotics. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3876–3881. IEEE, 2014. 

- Dimitrakakis, C. and Rothkopf, C. A. Bayesian multitask inverse reinforcement learning. In _European workshop on reinforcement learning_ , pp. 273–284. Springer, 2011. 

- Espeholt, L., Soyer, H., Munos, R., Simonyan, K., Mnih, V., Ward, T., Doron, Y., Firoiu, V., Harley, T., Dunning, I., et al. Impala: Scalable distributed deep-rl with importance weighted actor-learner architectures. In _International Conference on Machine Learning_ , pp. 1407–1416. PMLR, 2018. 

- Filos, A., Tigkas, P., McAllister, R., Rhinehart, N., Levine, S., and Gal, Y. Can autonomous vehicles identify, recover from, and adapt to distribution shifts? In _International Conference on Machine Learning_ , pp. 3145–3153. PMLR, 2020. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

- Finn, C., Christiano, P., Abbeel, P., and Levine, S. A connection between generative adversarial networks, inverse reinforcement learning, and energy-based models. _arXiv preprint arXiv:1611.03852_ , 2016a. 

- Finn, C., Levine, S., and Abbeel, P. Guided cost learning: Deep inverse optimal control via policy optimization. In _International conference on machine learning_ , pp. 49–58, 2016b. 

- Franklin, S. and Graesser, A. Is it an agent, or just a program?: A taxonomy for autonomous agents. In _International Workshop on Agent Theories, Architectures, and Languages_ , pp. 21–35. Springer, 1996. 

- Fu, J., Luo, K., and Levine, S. Learning robust rewards with adversarial inverse reinforcement learning. _arXiv preprint arXiv:1710.11248_ , 2017. 

- Fu, J., Korattikara, A., Levine, S., and Guadarrama, S. From language to goals: Inverse reinforcement learning for vision-based instruction following. _arXiv preprint arXiv:1902.07742_ , 2019. 

- Gao, Y., Xu, H., Lin, J., Yu, F., Levine, S., and Darrell, T. Reinforcement learning from imperfect demonstrations. _arXiv preprint arXiv:1802.05313_ , 2018. 

- Grollman, D. H. and Billard, A. Donut as i do: Learning from failed demonstrations. In _2011 IEEE International Conference on Robotics and Automation_ , pp. 3804–3809. IEEE, 2011. 

- Hansen, S., Dabney, W., Barreto, A., Van de Wiele, T., Warde-Farley, D., and Mnih, V. Fast task inference with variational intrinsic successor features. _arXiv preprint arXiv:1906.05030_ , 2019. 

- He, H., Boyd-Graber, J., Kwok, K., and Daume´ III, H. Opponent modeling in deep reinforcement learning. In _International Conference on Machine Learning_ , pp. 1804– 1813, 2016. 

- Hennigan, T., Cai, T., Norman, T., and Babuschkin, I. Haiku: Sonnet for JAX, 2020. URL http://github.com/ deepmind/dm-haiku. 

- Henrich, J. _The secret of our success: How culture is driving human evolution, domesticating our species, and making us smarter_ . Princeton University Press, 2017. 

- Hernandez-Leal, P., Kaisers, M., Baarslag, T., and de Cote, E. M. A survey of learning in multiagent environments: Dealing with non-stationarity. _arXiv preprint arXiv:1707.09183_ , 2017. 

- Hernandez-Leal, P., Kartal, B., and Taylor, M. E. Agent modeling as auxiliary task for deep reinforcement learning. In _Proceedings of the AAAI Conference on Artificial_ 

_Intelligence and Interactive Digital Entertainment_ , volume 15, pp. 31–37, 2019. 

- Heskes, T. Solving a huge number of simular tasks: a combination of multi-task learning and a hierarchical bayesian approach. 1998. 

- Hester, T., Vecerik, M., Pietquin, O., Lanctot, M., Schaul, T., Piot, B., Horgan, D., Quan, J., Sendonaris, A., Osband, I., et al. Deep q-learning from demonstrations. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 32, 2018. 

- Ho, J. and Ermon, S. Generative adversarial imitation learning. _arXiv preprint arXiv:1606.03476_ , 2016. 

- Hoffman, M., Shahriari, B., Aslanides, J., Barth-Maron, G., Behbahani, F., Norman, T., Abdolmaleki, A., Cassirer, A., Yang, F., Baumli, K., et al. Acme: A research framework for distributed reinforcement learning. _arXiv preprint arXiv:2006.00979_ , 2020. 

- Hunter, J. D. Matplotlib: A 2d graphics environment. _IEEE Annals of the History of Computing_ , 9(03):90–95, 2007. 

- Jaderberg, M., Dalibard, V., Osindero, S., Czarnecki, W. M., Donahue, J., Razavi, A., Vinyals, O., Green, T., Dunning, I., Simonyan, K., et al. Population based training of neural networks. _arXiv preprint arXiv:1711.09846_ , 2017. 

- Janz, D., Hron, J., Mazur, P., Hofmann, K., Hernandez-´ Lobato, J. M., and Tschiatschek, S. Successor uncertainties: exploration and uncertainty in temporal difference learning. In _Advances in Neural Information Processing Systems_ , pp. 4507–4516, 2019. 

- Jaques, N., Lazaridou, A., Hughes, E., Gulcehre, C., Ortega, P., Strouse, D., Leibo, J. Z., and De Freitas, N. Social influence as intrinsic motivation for multi-agent deep reinforcement learning. In _International Conference on Machine Learning_ , pp. 3040–3049. PMLR, 2019. 

- Kalashnikov, D., Irpan, A., Pastor, P., Ibarz, J., Herzog, A., Jang, E., Quillen, D., Holly, E., Kalakrishnan, M., Vanhoucke, V., et al. Scalable deep reinforcement learning for vision-based robotic manipulation. In _Conference on Robot Learning_ , pp. 651–673. PMLR, 2018. 

- Kesting, A., Treiber, M., and Helbing, D. Enhanced intelligent driver model to access the impact of driving strategies on traffic capacity. _Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences_ , 368(1928):4585–4605, 2010. 

- Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

- Klein, E., Piot, B., Geist, M., and Pietquin, O. A cascaded supervised learning approach to inverse reinforcement learning. In _Joint European conference on machine learning and knowledge discovery in databases_ , pp. 1–16. Springer, 2013. 

- Kulkarni, T. D., Saeedi, A., Gautam, S., and Gershman, S. J. Deep successor reinforcement learning. _arXiv preprint arXiv:1606.02396_ , 2016. 

- Laland, K. N. _Darwin’s unfinished symphony: How culture made the human mind_ . Princeton University Press, 2018. 

- Lee, D., Srinivasan, S., and Doshi-Velez, F. Truly batch apprenticeship learning with deep successor features. _arXiv preprint arXiv:1903.10077_ , 2019. 

- Leurent, E. An environment for autonomous driving decision-making. https://github.com/ eleurent/highway-env, 2018. 

- Levine, S., Kumar, A., Tucker, G., and Fu, J. Offline reinforcement learning: Tutorial, review, and perspectives on open problems. _arXiv preprint arXiv:2005.01643_ , 2020. 

- Liaw, R., Liang, E., Nishihara, R., Moritz, P., Gonzalez, J. E., and Stoica, I. Tune: A research platform for distributed model selection and training. _arXiv preprint arXiv:1807.05118_ , 2018. 

- Liu, Y., Gupta, A., Abbeel, P., and Levine, S. Imitation from observation: Learning to imitate behaviors from raw video via context translation. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 1118–1125. IEEE, 2018. 

- Lockett, A. J., Chen, C. L., and Miikkulainen, R. Evolving explicit opponent models in game playing. In _Proceedings of the 9th annual conference on Genetic and evolutionary computation_ , pp. 2106–2113, 2007. 

- Machado, M. C., Rosenbaum, C., Guo, X., Liu, M., Tesauro, G., and Campbell, M. Eigenoption discovery through the deep successor representation. _arXiv preprint arXiv:1710.11089_ , 2017. 

- Machado, M. C., Bellemare, M. G., and Bowling, M. Countbased exploration with the successor representation. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 34, pp. 5125–5133, 2020. 

- Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. _arXiv preprint arXiv:1312.5602_ , 2013. 

- Mulling, K., Kober, J., Kroemer, O., and Peters, J.¨ Learning to select and generalize striking movements in robot table 

tennis. _The International Journal of Robotics Research_ , 32(3):263–279, 2013. 

- Nair, A., McGrew, B., Andrychowicz, M., Zaremba, W., and Abbeel, P. Overcoming exploration in reinforcement learning with demonstrations. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6292–6299. IEEE, 2018. 

- Ndousse, K., Eck, D., Levine, S., and Jaques, N. Multi-agent social reinforcement learning improves generalization. _arXiv preprint arXiv:2010.00581_ , 2020. 

- Ng, A. Y., Harada, D., and Russell, S. Policy invariance under reward transformations: Theory and application to reward shaping. In _Icml_ , volume 99, pp. 278–287, 1999. 

- Ng, A. Y., Russell, S. J., et al. Algorithms for inverse reinforcement learning. In _Icml_ , volume 1, pp. 663–670, 2000. 

- Paine, T. L., Colmenarejo, S. G., Wang, Z., Reed, S., Aytar, Y., Pfaff, T., Hoffman, M. W., Barth-Maron, G., Cabi, S., Budden, D., et al. One-shot high-fidelity imitation: Training large-scale deep nets with rl. _arXiv preprint arXiv:1810.05017_ , 2018. 

- Paine, T. L., Gulcehre, C., Shahriari, B., Denil, M., Hoffman, M., Soyer, H., Tanburn, R., Kapturowski, S., Rabinowitz, N., Williams, D., et al. Making efficient use of demonstrations to solve hard exploration problems. _arXiv preprint arXiv:1909.01387_ , 2019. 

- Pomerleau, D. A. Alvinn: An autonomous land vehicle in a neural network. In _Neural Information Processing Systems (NeurIPS)_ , pp. 305–313, 1989. 

- Pomerleau, D. A. Efficient training of artificial neural networks for autonomous navigation. _Neural computation_ , 3(1):88–97, 1991. 

- Puterman, M. L. _Markov decision processes: discrete stochastic dynamic programming_ . John Wiley & Sons, 2014. 

- Rabinowitz, N. C., Perbet, F., Song, H. F., Zhang, C., Eslami, S., and Botvinick, M. Machine theory of mind. _arXiv preprint arXiv:1802.07740_ , 2018. 

- Rahmatizadeh, R., Abolghasemi, P., Bol¨ oni, L., and Levine,¨ S. Vision-based multi-task manipulation for inexpensive robots using end-to-end learning from demonstration. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3758–3765. IEEE, 2018. 

- Rajeswaran, A., Kumar, V., Gupta, A., Vezzani, G., Schulman, J., Todorov, E., and Levine, S. Learning complex dexterous manipulation with deep reinforcement learning 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

- and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- Ratliff, N. D., Bagnell, J. A., and Zinkevich, M. A. Maximum margin planning. In _Proceedings of the 23rd international conference on Machine learning_ , pp. 729–736, 2006. 

- Reddy, S., Dragan, A. D., and Levine, S. Sqil: Imitation learning via reinforcement learning with sparse rewards. _arXiv preprint arXiv:1905.11108_ , 2019. 

- Rhinehart, N., McAllister, R., and Levine, S. Deep imitative models for flexible inference, planning, and control. In _International Conference on Learning Representations (ICLR)_ , April 2020. 

- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- Sermanet, P., Lynch, C., Chebotar, Y., Hsu, J., Jang, E., Schaal, S., Levine, S., and Brain, G. Time-contrastive networks: Self-supervised learning from video. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 1134–1141. IEEE, 2018. 

- Sharma, P., Mohan, L., Pinto, L., and Gupta, A. Multiple interactions made easy (mime): Large scale demonstrations data for imitation. _arXiv preprint arXiv:1810.07121_ , 2018. 

- Shiarlis, K., Messias, J., and Whiteson, S. Inverse reinforcement learning from failure. 2016. 

- Stahl, D. O. Evolution of smart-n players. _Games and Economic Behavior_ , 5(4):604–617, 1993. 

   - Van Rossum, G. and Drake Jr, F. L. _Python reference manual_ . Centrum voor Wiskunde en Informatica Amsterdam, 1995. 

   - Vecerik, M., Hester, T., Scholz, J., Wang, F., Pietquin, O., Piot, B., Heess, N., Rothorl, T., Lampe, T., and Riedmiller,¨ M. Leveraging demonstrations for deep reinforcement learning on robotics problems with sparse rewards. _arXiv preprint arXiv:1707.08817_ , 2017. 

   - Watkins, C. J. and Dayan, P. Q-learning. _Machine learning_ , 8(3-4):279–292, 1992. 

   - Widrow, B. and Smith, F. W. Pattern-recognizing control systems, 1964. 

   - Wulfmeier, M., Ondruska, P., and Posner, I. Maximum entropy deep inverse reinforcement learning. _arXiv preprint arXiv:1507.04888_ , 2015. 

   - Yoshida, W., Dolan, R. J., and Friston, K. J. Game theory of mind. _PLoS Comput Biol_ , 4(12):e1000254, 2008. 

   - Zhang, T., McCarthy, Z., Jow, O., Lee, D., Chen, X., Goldberg, K., and Abbeel, P. Deep imitation learning for complex manipulation tasks from virtual reality teleoperation. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 1–8. IEEE, 2018. 

   - Zheng, J., Liu, S., and Ni, L. M. Robust bayesian inverse reinforcement learning with sparse behavior noise. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 28, 2014. 

   - Ziebart, B. D., Maas, A. L., Bagnell, J. A., and Dey, A. K. Maximum entropy inverse reinforcement learning. In _Aaai_ , volume 8, pp. 1433–1438. Chicago, IL, USA, 2008. 

- Stulp, F., Raiola, G., Hoarau, A., Ivaldi, S., and Sigaud, O. Learning compact parameterized skills with a single regression. In _2013 13th IEEE-RAS International Conference on Humanoid Robots (Humanoids)_ , pp. 417–422. IEEE, 2013. 

- Sutton, R. S. and Barto, A. G. _Reinforcement learning: An introduction_ . MIT press, 2018. 

- Taylor, M. E., Suay, H. B., and Chernova, S. Integrating reinforcement learning with human demonstrations of varying ability. In _The 10th International Conference on Autonomous Agents and Multiagent Systems-Volume 2_ , pp. 617–624, 2011. 

- Torabi, F., Warnell, G., and Stone, P. Behavioral cloning from observation. _arXiv preprint arXiv:1805.01954_ , 2018. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

## **A. Experimental Details** 

In this section we describe the environments used in our experiments (see Section 4) and the experiment design. 

### **A.1. Highway** 

We build on the highway-v0 task from the highway-env traffic simulator (Leurent, 2018). The task is specified by: 

1. **State space,** _S_ **:** The kinematic information of the ego vehicle and the five closest ve= 

hicles (ordered from closest to the furthest) is used as the Markov state, i.e., **s** _t {_ [ _xt, yt, x_ ˙ _t, y_ ˙ _t_ ] _}_ ego _,_ other1 _, ...,_ other5 _∈_ R<sup>6</sup><sup>_×_4</sup> . The ego-car is illustrated in green and the other cars in blue. 

2. **Action space,** _A_ **:** We use a discrete action space, constructed by _K_ -means clustering of the continuous actions of the intelligent driving model (Kesting et al., 2010). We found out that keeping 9 actions was sufficient, i.e., **a** _t ∈{_ 0 _, . . . ,_ 8 _}_ . 



_Figure 6._ Highway 

3. **Demonstrations,** _D_ **:** At each time-step, the ego-car observes online the state-action pairs for the 5 closest cars. 

### **A.2. Roundabout** 

We build on the roundabot-v0 task from the highway-env traffic simulator (Leurent, 2018). The task is specified by: 

1. **State space,** _S_ **:** The kinematic information of the ego vehicle and the five closest ve= 

hicles (ordered from closest to the furthest) is used as the Markov state, i.e., **s** _t {_ [ _xt, yt, x_ ˙ _t, y_ ˙ _t_ ] _}_ ego _,_ other1 _, ...,_ other3 _∈_ R<sup>4</sup><sup>_×_4</sup> . The ego-car is illustrated in green and the other cars in blue. 

2. **Action space,** _A_ **:** We use a discrete action space, constructed by _K_ -means clustering of the continuous actions of the intelligent driving model (Kesting et al., 2010). We found out that keeping 6 actions was sufficient, i.e., **a** _t ∈{_ 0 _, . . . ,_ 5 _}_ . 



_Figure 7._ Roundabout 

3. **Demonstrations,** _D_ **:** At each time-step, the ego-car observes online the state-action pairs for the 3 closest cars. 

### **A.3. CoinGrid** 

We build a simple multi-task grid-world. The task is specified by: 

1. **State space,** _S_ **:** We use a symbolic, multi-channel representation of the 7 _×_ 7 gridworld (Chevalier-Boisvert et al., 2019): the first three channels specify the presence or absence of the three different coloured boxes, the forth channel was the walls mask and the fifth and last channel was the position and orientation of the agent. We represent the orientation of the agent by ‘painting’ the cell in front of the agent. Therefore **s** _t ∈{_ 0 _,_ 1 _}_<sup>7</sup><sup>_×_7</sup><sup>_×_5</sup> . 

2. **Action space,** _A_ **:** We use the _{_ LEFT, RIGHT, FORWARD _}_ actions from Minigrid (ChevalierBoisvert et al., 2018) to navigate the maze, i.e., **a** _t ∈{_ 0 _,_ 1 _,_ 2 _}_ . 

3. **Demonstrations,** _D_ **:** At the beginning of training, the agent is given state-action pairs of other agents collecting either red or green coins. 



_Figure 8._ CoinGrid 

### **A.4. Fruitbot** 

We build on the Fruitbot environment from OpenAI’s ProcGen benchmark (Cobbe et al., 2020). The task is specified by: 

1. **State space,** _S_ **:** We use the original high-dimensional 64 _×_ 64 RGB observations, i.e., **s** _t ∈_ [0 _,_ 1]<sup>64</sup><sup>_×_64</sup><sup>_×_3</sup> . 

2. **Action space,** _A_ **:** We use the original 15 discrete actions, i.e., **a** _t ∈{_ 0 _, . . . ,_ 14 _}_ . 

3. **Demonstrations,** _D_ **:** At each time-step, the agent observes online the states and actions of 3 trained agents playing the game in parallel: One agent collects both fruits and other objects, one collects other objects and avoids fruits and the last one randomly selects actions. 



_Figure 9._ Fruitbot 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

## **B. Implementation Details** 

For our experiments we used Python (Van Rossum & Drake Jr, 1995). We used JAX (Bradbury et al., 2018; Babuschkin et al., 2020) as the core computational library, Haiku (Hennigan et al., 2020) and Acme (Hoffman et al., 2020) for implementing ΨΦ-learning and the baselines, see Section 4. We also used Matplotlib (Hunter, 2007) for the visualisations and Weightd & Biases (Biewald, 2020) for managing the experiments. 

### **B.1. Computation Graph** 



<!-- Start of picture text -->
π ego<br>D GPI<br>k = 1  . . . K L BC- Q L TD- Q<br>Ψ ego Q ego B<br>Q k<br>L TD-Ψ<br>w k Ψ k Φ w ego<br>L ITD<br>r ego<br>LR<br><!-- End of picture text -->

_Figure 10._ **Computational graph of the** ΨΦ **-learning algorithm.** Demonstrations _D_ contain data from other agents for _unknown_ tasks. We employ _inverse temporal difference learning_ (ITD, see Section 3.1) to recover other agents’ successor features (SFs) and preferences. The ego-agent combines the estimated SFs of others along with its own preferences and successor features with generalised policy improvement (GPI, see Section 2.2), generating experience. Both the demonstrations and the ego-experience are used to learn the shared cumulants. Losses _L∗_ are represented with double arrows and gradients flow according to the pointed direction(s). 

### **B.2. Neural Network Architecture** 



<!-- Start of picture text -->
ΨΨ 11 (( ss tt, ·, · )) w 1 · · · ΨΨ KK (( ss tt, ·, · )) w K Φ( s t, · ) ΨΨ egoego (( ss tt, ·, · )) w ego<br>E<br>s t<br><!-- End of picture text -->

_Figure 11._ **Neural network architecture of the** ΨΦ **-learner.** The rectangular nodes are tensors parametrised by MLPs and the circles are learnable vectors. We share an observation network/torso, _E_ , across all the network heads. The network heads that related to the other agents are in blue and trained from demonstrations _D_ . The ego-agent’s experience _B_ is used for training the green heads. The shared cumulants and torso are trained with both _D_ and _B_ . An ensemble of two successor features approximators is used for the ego- and otheragents for combatting model overestimation, see Section 3. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

### **B.3. Hyperparameters** 

_Table 3._ ΨΦ **-learner’s hyperparameters per environment** . The tuning was performed on a DQN (Mnih et al., 2013) baseline with population based training (Jaderberg et al., 2017) using Weights & Biases (Biewald, 2020) integration with Ray Tune (Liaw et al., 2018). We selected the best hyperparameters configuration out of 32 trials per environment and used this for our ΨΦ-learner. 

||Highway|CoinGrid|FruitBot|
|---|---|---|---|
|**Torso network,**_E_|MLP([512, 256])|IMPALA (Espeholt et al.,2018), shallow (no LSTM)|IMPALA (Espeholt et al.,2018), deep (no LSTM)|
|**Cumulants approximator,**Φ|MLP([128, 128])|MLP([256, 128])|MLP([256, 128])|
|**Successor features approximator,**Ψ|MLP([256, 128])|MLP([512, 256])|MLP([512, 256])|
|**Ensemble size,**Ψ|2|2|2|
|_L_1**coefficient**|0.05|0.05|0.05|
|**Number of dimensions in**Φ|8|4|64|
|**Minibatch size**|512|64|32|
|_n_**-step**|4|8|128|
|**Discount factor,**_γ_|1.0|0.9|0.999|
|**Target network update period**|100|1000|2500|
|**Optimiser**|ADAM (Kingma & Ba,2014),lr=1e-3|ADAM (Kingma & Ba,2014),lr=1e-4|ADAM (Kingma & Ba,2014),lr=5e-5|



### **B.4. Compute Resources** 

All the experiments were run on Microsoft Azure Standard ~~N~~ C6s ~~v~~ 3 machines, i.e., with a 6-core vCPU, 112GB RAM and a single NVIDIA Tesla V100 GPU. The iteration cycle for (i) **Highway** experiments was 3 hours; (ii) **CoinGrid** experiments was 5.5 hours and (iii) **Fruitbot** experiments was 19 hours. 

ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

## **C. Proofs** 

First, we formalise the statement of Theorem 1. 

**Theorem 1** (Validity of the ITD Minimiser) **.** _The minimisers of LBC-Q and LITD are potentially-shaped cumulants that explain the observed reward-free demonstrations._ 

_Proof._ First, we prove the validity of the minimiser of the inverse temporal difference learning for the single-task setting. Next, we show that the result holds true in the vector (i.e., cumulants) case. 

**Single task.** We assume that our demonstrations are generated by an expert, who samples actions from a Boltzmann policy, according to the optimal (for its task) action-value function _Q_<sup>_π_expert</sup> and temperature _ν >_ 0, i.e., _D_ = _{_ ( **s** _,_ **a** ) _} ∼ π_ expert s.t. 



The minimiser of the behavioural cloning loss _L_ BC- _Q_ ( **_θ_** _Q_ ), i.e. Eqn. (8), for a single expert is s.t. 



where _F_ : _S →_ R is a state-dependent (bounded potential) function. We arrive at Eqn. (17) by (1) testing _ν_<sup><u>1</u></sup><sup>_Qπ_expert(</sup><sup>**s**</sup><sup>_,_</sup><sup>**a**) as a</sup> solution and noting that the “softmax“ function is convex in the exponent (Boyd et al., 2004) and (2) using the translation invariance property of the assumed Boltzmann policy parametrisation, i.e., for any _f_ : _S × A →_ R and _g_ : _S →_ R 



The minimiser of the inverse temporal difference learning loss _L_ ITD( **_θ_** _Q,_ **_θ_** _r_ ), Eqn. (9), for a single expert is s.t. 



where **_θ_**<sup>_∗_</sup> _Q_<sup>is minimising</sup><sup>_L_BC-</sup><sup>_Q_(</sup><sup>**_θ_**</sup><sup>_Q_) simultaneously, as in Eqn. (17).Therefore, it holds that</sup><sup>_L_ITD(</sup><sup>**_θ_**</sup><sup>_∗_</sup> _Q_<sup>_,_</sup><sup>**_θ_**</sup> _r_<sup>_∗_) = 0</sup> 



where _r_<sup>expert</sup> is the (unobserved) expert’s reward function. We have shown that the minimiser of _L_ BC- _Q_ and _L_ ITD leads to a reward function _r_ ( **s** _,_ **a** ; **_θ_**<sup>_∗_</sup> _r_<sup>) which is a potential-based shaped and scaled reward function of the expert reward function and</sup> hence the optimal policy for _r_ ( **s** _,_ **a** ; **_θ_**<sup>_∗_</sup> _r_<sup>) is also optimal for</sup><sup>_r_expert(</sup><sup>**s**</sup><sup>_,_</sup><sup>**a**) for all</sup><sup>**s**</sup><sup>_,_</sup><sup>**a**(Ng et al., 1999).</sup> 

**Multiple tasks.** The minimiser of the behavioural cloning loss _L_ BC- _Q_ ( **_θ_** Ψ _k ,_ **w**<sup>_k_</sup> ), i.e., Eqn. (8), for the _k_ -th expert is s.t. 



ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

where _Q_<sup>_πk_-expert</sup> is the _k_ -agent’s action-value function and _H_<sup>_k_</sup> : _S →_ R a state-dependent (bounded potential) function. Next, the minimiser of the inverse temporal difference learning loss _L_ ITD( **_θ_** Ψ _k ,_ **_θ_** Φ), Eqn. (9), for the _k_ -th expert is s.t. 



where **_θ_**<sup>_∗_</sup> Ψ<sup>_k_is minimising</sup><sup>_L_BC-</sup><sup>_Q_(</sup><sup>**_θ_**</sup> Ψ<sup>_k,_</sup><sup>**w**</sup><sup>_k_) simultaneously, as in Eqn. (25).Therefore, it holds that for</sup><sup>_L_ITD(</sup><sup>**_θ_**</sup> Ψ<sup>_∗k,_</sup><sup>**_θ_**</sup> Φ<sup>_∗_) = 0</sup> 





We have shown that the minimiser of _L_ BC- _Q_ and _L_ ITD leads to agent-agnostic cumulants Φ( **s** _,_ **a** ; **_θ_** Φ<sup>_∗_) and agent-specific</sup> preference vector **w**<sup>_k∗_</sup> , which when dot-producted, form a potential-based shaped and scaled reward function of the _k_ -th expert reward function and hence the optimal policy for Φ( **s** _,_ **a** ; **_θ_**<sup>_∗_</sup> Φ<sup>)</sup><sup>_⊤_</sup><sup>**w**</sup><sup>_k∗_is also optimal for</sup><sup>_rk_-expert(</sup><sup>**s**</sup><sup>_,_</sup><sup>**a**) for all</sup><sup>**s**</sup><sup>_,_</sup><sup>**a**(Ng</sup> et al., 1999). The result holds for all _k ∈{_ 1 _. . . K}_ since no assumptions were made for the proof about _k_ . 

Next, we formalise the statement of Theorem 2. When not specified the norm _∥· ∥_ refers to the 2-norm. Given a function _F_ : _X →_ R<sup>_d_</sup> for some finite set _X_ , we will write _F_ ( _x_ ) to denote the value of the function on input _x_ and _F_ to denote the matrix representation of this function in R<sup>_|X|×d_</sup> . 

**Theorem 2** (Generalisation Bound of ΨΦ-Learning) **.** _Let C_ = ( _S, A, P, γ_ ) _be a CMP with a finite state space. Let φ_ : _S →_ R<sup>_d_</sup> _, and let_ Φ = _φ_ ( _S_ ) _∈_ R<sup>_|S|×d_</sup> _. Let_ ( _ri_ )<sup>_k_</sup> _i_ =1<sup>_denote a set of reward functions on C,_˜Ψ</sup><sup>_i be a collection of successor_</sup> _features approximations for policies_ ( _π_<sup>_i_</sup> )<sup>_k_</sup> _i_ =1<sup>_(πioptimal forri) with true successor feature values_Ψ</sup><sup>_i,and withe best_</sup> _least-squares linear approximator of ri given_ Φ _, with errors_ 



_Let w_<sup>_′_</sup> _be a new preference vector for a reward function r_<sup>_′_</sup> _, with maximal error δr as well. Let Q_<sup>˜</sup><sup>_i_</sup> = Ψ<sup>˜</sup><sup>_i_</sup> _w_<sup>_′_</sup> _. Let π_<sup>_∗_</sup> _be the optimal policy for the ego task w_<sup>_′_</sup> _and let π be the GPI policy obtained from {Q_<sup>˜</sup><sup>_πi_</sup> _}, with δr, δ_ Ψ _the reward and successor feature approximation errors. Then for all s, a_ 



Barreto et al. (2017) construct their bound on the sub-optimality of the GPI policy as a function of the error of the value approximations _Q_<sup>�</sup><sup>_i_</sup> . Because we bound the reward approximation error, rather than the value approximation error, we require an additional step to obtain a bound on the errors of the value funciton approximations. To prove Theorem 1, we must therefore first use the following lemma to bound the effect of the _reward approximation error_ on the value approximation error. While this result is straightforward, we include a short proof for completeness. 

**Lemma 1.** _Fix some policy π. Let r be reward vector and let w be the least-squares solution to_ min _∥_ Φ _w − r∥. Let_ Ψ<sup>_π_</sup> _be the true successor features for_ Φ _under policy π, and let Q_<sup>_π_</sup> _be the value. Let δr_ = _R_ ( _S_ ) _−_ Φ _w, δmax_ = _∥δr∥∞. Then letting Q_<sup>˜</sup> = Ψ _w, we have_ 



_Proof._ 





ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

Since _P_<sup>_π_</sup> is a stochastic matrix, so are all of its powers, and so the rows of ( _P_<sup>_π_</sup> )<sup>_t_</sup> sum to 1. 





We now prove the main result. 

_Proof._ We follow the proof of Barreto et al. (2017, Theorem 2), with additional error terms to account for the reward and successor feature approximation errors. 



ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

## **D. Algorithms** 

|**Algorithm 1:** Inverse Temporal Difference Learning||
|---|---|
|**Input**<br>**:**<br>||
|_D_ =_{_(**s**1_,_**a**1_, . . . ,_**a**_T_;_k_)<sup>_K_</sup><br>_k_=1<sup>_}_</sup><br>No-reward demonstrations||
|_λ_**w**<br>_L_1loss coefficient||
|**Output :**||
|**_θ_**Φ<br>Parameters of cumulants network||
|_{_**_θ_**Ψ_k}_<sup>_K_</sup><br>_k_=1<br>Parameters of successor features approximators<br>||
|_{_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1<br>Preferences vectors for the_K_ agents||
|// initialisations||
|**1** Initialise parameters**_θ_**Φ_, {_**_θ_**Ψ_k,_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1||
|**2 while**_budget_**do**||
|**3**<br>Sample trajectories_{τi_ = (_s_<sup>(</sup><sup>_i_)</sup><br>1 <sup>_, a_(</sup><sup>_i_)</sup><br>1 <sup>_, . . . , s_(</sup><sup>_i_)</sup><br>_T _<sup>_, a_(</sup><sup>_i_)</sup><br>_T_ <sup>;</sup><sup>_k_(</sup><sup>_i_))</sup><sup>_}N_</sup><br>_i_=1 <sup>_∼D_</sup>||
|**4**<br>Calculate behavioural cloning loss_L_BC-_Q_(**_θ_**Ψ_k,_**w**<sup>_k_</sup>)on samples_{τi}_<sup>_N_</sup><br>_i_=1|_▷_see Eqn. (8)|
|**5**<br>**_θ_**Ψ_k_<br>_α←∇_**_θ_**Ψ_k L_BC-_Q_(**_θ_**Ψ_k,_**w**_k_)|_▷_update Ψs|
|**6**<br>**w**<sup>_k_</sup><br>_α←∇_**w**_k_<br>�<br>_L_BC-_Q_(**_θ_**Ψ_k,_**w**<sup>_k_</sup>) +_λ_**w**_∥_**w**<sup>_k_</sup>_∥_1<br>�|_▷_update **w**s|
|**7**<br>Calculate inverse temporal difference loss_L_ITD(**_θ_**Φ_,_**_θ_**Ψ_k_)on samples_{τi}_<sup>_N_</sup><br>_i_=1|_▷_see Eqn. (9)|
|**8**<br>**_θ_**Φ<br>_α←∇_**_θ_**Φ_L_ITD(**_θ_**Ψ_k,_**_θ_**Φ)|_▷_update Φ|
|**9**<br>**_θ_**Ψ_k_<br>_α←∇_**_θ_**Ψ_k L_ITD(**_θ_**Ψ_k,_**_θ_**Φ)|_▷_update Ψs|



ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

|**Algorithm 2:** ΨΦ-Learning|
|---|
|**Input**<br>**:**<br>|
|_D_ =_{_(**s**1_,_**a**1_, . . . ,_**a**_T_;_k_)<sup>_K_</sup><br>_k_=1<sup>_}_</sup><br>No-reward demonstrations|
|_λ_**w**<br>_L_1loss coefficient<br>|
|**Output :**|
|**_θ_**Ψ<sup>ego</sup><br>Ego successor features approximator|
|**_θ_**Φ<br>Parameters of cumulants network|
|_{_**_θ_**Ψ_k}_<sup>_K_</sup><br>_k_=1<br>Parameters of successor features approximators|
|_{_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1<br>Preferences vectors for the_K_ agents|
|// initialisations|
|**1** Empty replay buffer for ego-experience_B_ =_{}_<br>**2** Initialise parameters**_θ_**Ψego_,_**w**<sup>ego</sup>_,_**_θ_**Φ_, {_**_θ_**Ψ_k,_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1|
|**3 while**_budget_**do**<br>// agent-environment interaction|
|**4**<br>Reset episode,**s**_←_env.reset(),_t ←_0|
|**5**<br>**while**_not done_**do**|
|**6**<br>**w**<sup>ego</sup> _←_arg min_w L_R(**_θ_**Φ_, w_;_B_)<br>_▷_ego-task inference, see Eqn. (10)|
|**7**<br>**a**_←π_<sup>ego</sup><br>GPI<br>�<br>**s**; Ψ<sup>ego</sup>_,_**w**<sup>ego</sup>_, {_**_θ_**Ψ_k}_<sup>_K_</sup><br>_k_=1<br>�<br>_▷_GPI, see Eqn. (13)|
|**8**<br>Step in the environment,**s**<sup>_′_</sup>_, r_<sup>ego</sup>_,_done_←_env.step(**a**)|
|**9**<br>Append transition in the replay buffer,_B ←B ∪_(**s**_,_**a**_, r_<sup>ego</sup>_,_**s**<sup>_′_</sup>)|
|**10**<br>**s**<sup>_′ _</sup>_←_**s**,_t ←t_+ 1|
|**11**<br>(online demonstrations) Append demonstrations in_D_<br>_▷_optional|
|// parameter updates/learning|
|**12**<br>**_θ_**Φ_, {_**_θ_**Ψ_k,_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1 <sup>_←_ITD</sup><br>�<br>_D, λ_**w**_,_**_θ_**Φ_, {_**_θ_**Ψ_k,_**w**<sup>_k_</sup>_}_<sup>_K_</sup><br>_k_=1<br>�<br>_▷_see Algorithm. (1)|
|**13**<br>Sample transitions_{_(**s**<sup>(</sup><sup>_i_)</sup>_,_**a**<sup>(</sup><sup>_i_)</sup>_, r_<sup>ego</sup><sup>_,_(</sup><sup>_i_)</sup>_,_**s**<sup>_′_(</sup><sup>_i_)</sup>)_} ∼B_|
|**14**<br>Calculate the reward loss_L_R(**_θ_**Φ_,_**w**<sup>ego</sup>)<br>_▷_see Eqn. (10)|
|**15**<br>**_θ_**Φ<br>_α←∇_**_θ_**Φ_L_R(**_θ_**Φ_,_**w**ego)<br>_▷_update Φ|
|**16**<br>Calculate TD losses_LQ_(**_θ_**Ψego)and_L_TD-Ψ(**_θ_**Ψego)<br>_▷_see Eqn. (11,12)<br><br>|
|**17**<br>**_θ_**Ψego<br>_α←∇_**_θ_**Ψego<br>�<br>_LQ_(**_θ_**Ψego) +<br>1<br>_|_Ψ_|_<sup>_L_TD-Ψ(</sup><sup>**_θ_**Ψego)</sup><br>�<br>_▷_update Ψ<sup>ego</sup>|



ΨΦ **-Learning: RL with Demonstrations using Successor Features and Inverse TD Learning** 

## **E. Visualisations** 



<!-- Start of picture text -->
(a) CoinGrid (b)  φ 1<br><!-- End of picture text -->



<!-- Start of picture text -->
(c)  φ 2<br><!-- End of picture text -->



<!-- Start of picture text -->
(d)  φ 3 (e)  φ 4<br><!-- End of picture text -->

_Figure 12._ Qualitative evaluation of the learned cumulants in the CoinGrid task. Cumulants _φ_ 1, _φ_ 2, and _φ_ 3 seem to capture the red, green, and yellow blocks, respectively. The yellow blocks are captured by both and _φ_ 4. Therefore, linear combinations of the learned cumulants can represent arbitrary rewards in the environment, which involve stepping on the coloured blocks. 



<!-- Start of picture text -->
1.0 1.0 1.0<br>|Φ|<br>0.8 0.8 0.8 2 16<br>4 32<br>0.6 0.6 0.6 8 128<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0.0 2 4 8 16 32 128 0.0 2 4 8 16 32 128 0.010 2 10 3 10 4<br>|Φ| |Φ| Timesteps<br>(a) ITD for Roundabout (b) ITD for CoinGrid (c) ΨΦ-learning for Highway Multi-Task<br>Returns<br>Normalised Returns Normalised Returns<br><!-- End of picture text -->

_Figure 13._ Sensitivity of our ITD (see Section 3.1) and ΨΦ-learning (see Section 3.2) algorithms to the dimensionality of the learned cumulants. We consistently observe across all three experiments (a)-(c) that for a small number of Φ dimensions the cumulants are not expressive enough to capture the axis of variation of the different agents’ reward functions (including the ego-agent in (c)). We also note that the performance of both ITD and ΨΦ-learning is relative robust for a medium and large number of Φ dimensions. We attribute this to the used sparsity prior, i.e., _L_ 1 loss, to the preferences **w** . In our experiments we selected the smallest number of Φ dimensions that demonstrated good performance to keep the number of model parameters as small as possible (in bold in the figures and reported in Table 3). 

