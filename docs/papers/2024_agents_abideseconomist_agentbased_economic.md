---
title: "ABIDES-Economist: Agent-Based Economic Simulation for Policy Evaluation"
authors: "agents"
year: 2024
arxiv_id: "2402.09563"
original_file: "2402.09563.pdf"
pdf_path: "docs/papers\2024_agents_abideseconomist_agentbased_economic.pdf"
---

# ABIDES-Economist: Agent-Based Economic Simulation for Policy Evaluation

**Authors:** Agents et al.  
**Year:** 2024 | **arXiv:** [`2402.09563`](https://arxiv.org/abs/2402.09563)  
**Local PDF:** [`2024_agents_abideseconomist_agentbased_economic.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2024_agents_abideseconomist_agentbased_economic.pdf)

---

# ABIDES-Economist: Agent-Based Simulator of Economic Systems with Learning Agents 

Kshama Dwarakanath<sup>1*</sup> , Tucker Balch<sup>**_†_**2</sup> and Svitlana Vyetrenko<sup>1</sup> 

> 1AI Research, JP Morgan Chase, San Francisco, California, USA. 

> 2Goizueta Business School, Emory University, Atlanta, Georgia, USA. 

**_†_** Tucker Balch’s contributions to this paper were made while employed by JPMorgan Chase. 

*Corresponding author(s). E-mail(s): kshama.dwarakanath@jpmorgan.com; Contributing authors: tucker.balch@emory.edu; svitlana.vyetrenko@gmail.com; 

###### **Abstract** 

We present ABIDES-Economist, an agent-based simulator for economic systems that includes heterogeneous households, firms, a central bank, and a government. Agent behavior can be defined using domain-specific behavioral rules or learned through reinforcement learning by specifying their objectives. We integrate reinforcement learning capabilities for all agents using the OpenAI Gym environment framework for the multi-agent system. To enhance the realism of our model, we base agent parameters and action spaces on economic literature and real U.S. economic data. To tackle the challenges of calibrating heterogeneous agent-based economic models, we conduct a comprehensive survey of stylized facts related to both microeconomic and macroeconomic time series data. We then validate ABIDES-Economist by demonstrating its ability to generate simulated data that aligns with the relevant stylized facts for the economic scenario under consideration, following the learning of all agent behaviors via reinforcement learning. Specifically, we train our economic agents’ policies under two broad configurations. The first configuration demonstrates that the learned economic agents produce system data consistent with macroeconomic and microeconomic stylized facts. The second configuration illustrates the utility of the validated simulation platform in designing regulatory policies for the central bank and government. These policies outperform standard rule-based approaches from the literature, which often overlook agent heterogeneity, shocks, and agent adaptability. 

**Keywords:** Agent-Based Modeling, Reinforcement Learning, Calibration, Stylized Facts, Agent-Based Economic Systems 

1 

## **1 Introduction** 

Agent-based modeling (ABM) offers significant potential for advancing economics by defining agents and their interactions to produce complex emergent behaviors even from simple rules [1]. The main motivation behind applying ABMs to a domain is in the generation of emergent system-level behaviors that could not have been reasonably inferred from the underlying agent behaviors [2]. ABMs have been applied in robotics [3], financial markets [4], traffic management [5], social networks [6], and recently, in simulating social interactions with LLMs [7]. Prominent economists highlight the benefits of ABMs in modeling complex scenarios accounting for human adaptation and learning [8]. The field of Agent-Based Computational Economics advocates for ABMs’ ability to simulate ‘turbulent’ social conditions unseen in historical data, and to model dynamics out of equilibrium [9, 10]. [11] promotes ABMs for bridging the gap between microeconomics (individual agent modeling) and macroeconomics (aggregate observations at system level). [12] highlights the advantages of heterogeneous ABMs as a bottom-up approach towards modeling nuances of the real world more accurately. 

An agent is an entity that senses its environment to make a goal-oriented decision that is implemented by taking an action on the environment [13]. Reinforcement learning (RL) deals with problems where an agent learns to act in an uncertain, dynamic environment through trial-and-error to maximize its objectives over a horizon [14]. When there are multiple agents that are attempting to learn to act in a common environment, they each introduce non-stationarity and (potential) partial observability for other agents [15]. Multi-agent reinforcement learning (MARL) studies such problems by modeling the multi-agent system as a stochastic game where the state of the environment evolves in response to joint action across all agents [16, 17]. MARL is closely related to game theory which typically involves the study of multiple agents in static one-step or repeated tasks [18, 19]. 

The field of industrial organization has a well-established literature on dynamic games, particularly focusing on the concept of Markov perfect equilibria within Markov Perfect models, which closely align with the Markov Decision Processes paradigm in RL [20]. In MARL, the Markov assumption serves to restrict the space of game equilibria from which joint agent policies can be chosen, while allowing for unknown transition dynamics, unlike dynamic games. RL is a powerful tool for leveraging agent experiences from simulation runs to develop more flexible and robust agent behaviors. In economic systems, RL allows for flexible agent behaviors without restrictive parametric assumptions on how agents forecast the future. Specifically, the classical rational expectations assumption is an extreme version of such an assumption, where the forecasting mechanism is self-consistent: behavior based on these forecasts results in an environment that obeys these forecasted rules in expectation. Conversely, RL makes no such assumptions and allows for a more flexible (and more realistic [21]) model of agent behavior, which can adapt more effectively to changes in policy and shock scenarios than traditional descriptive behavioral rules. This is particularly advantageous when agent objectives are easily formalized, as is often the case for firms and central banks. 

2 

Recent work has incorporated ABMs and RL in economic systems, but these are often restricted to simplistic 2D grid world environments [22], single agent (type) learning with rule-based background agents [23–26], or a limited number of agent types learning alongside rule-based regulatory bodies [27, 28]. Many of these approaches lack agent heterogeneity that is prevalent in real economies, and fail to model economic shocks within the system. Furthermore, there is no unified effort to define and apply calibration and validation practices for such ABMs with learning agents, as seen in traditional economic rule-based ABMs [29]. Empirical calibration of simulation models is crucial for enhancing confidence in their results and their utility for economic decision-making [30]. However, the high degree of freedom inherent in ABMs [31], combined with the learning agents poses significant challenges to these efforts. Additionally, MARL can result in stability issues due to the interaction between agent decisions and the environment, alongside the explosion of parameters coming from ABMs, leading to an explosion in the space of possible equilibria that the system converges to. This is alongside learning instabilities inherent with MARL. We partially address these challenges in this work by introducing inductive biases to regularize the space of possible joint agent behaviors by assuming symmetry/exchangeability of policies per agent category [20], and via empirical validation of the resulting system with learned agents. These inductive biases serve as an equilibrium selection mechanism within the large space of joint agent policies considered by MARL within ABMs. 

In this work, we introduce a customizable agent-based simulator for economic systems, implemented in Python, that incorporates multi-agent learning, agent heterogeneity, and economic shocks. We also examine stylized facts - recurring patterns observed in real economic data at both macro and micro levels — to guide the calibration of our ABM with learning agents. Once strategies are learned for all agents in our simulated economy, we validate these strategies against the stylized facts. Finally, we demonstrate the utility of our simulation platform and the learned policies of economic agents by benchmarking their performance against standard baselines. Our contributions are summarized as follows: 

- **Development of a Versatile Agent-Based Simulator** : We have developed an agent-based simulator for economic systems that includes heterogeneous households, firms, a central bank, and a government. This simulator is highly versatile and customizable to various economic scenarios, allowing for the addition of regional agents, modification of inter-agent connections, and other system-specific configurations. 

- **Integration of Multi-Agent Reinforcement Learning** : In order to model agent adaptation to one another, we integrate reinforcement learning capabilities for all agents using OpenAI Gym-style environments within the multi-agent system. To efficiently scale multi-agent training, we adopt a shared policy network for all agents of a given type, incorporating their heterogeneity parameters as additional inputs. This along with communication of realistically shareable information between agents enable partial mitigation of non-stationarity and partial observability challenges associated with multi-agent learning.<sup>1</sup> 

> 1We note that this also serves as a form of regularization that limits the space of possible agent strategies, and has previously been considered in the literature as the exchangeability assumption or symmetric Markov Perfect equilibrium in dynamic games [20]. 

3 

- **Specification of Agent Heterogeneity and Action Spaces** : We specify agent heterogeneity parameters and action spaces grounded in economic literature and real-world economic data, to ensure realistic modeling. 

- **Survey and Validation of Stylized Facts** : We conduct a comprehensive survey of stylized facts (or empirical regularities) in historical economic data at both macroeconomic and microeconomic levels. This facilitates the validation of economic agent-based models. We validate our model by demonstrating its ability to generate simulated data that adheres to these facts, even as all agents in the platform are learning. 

- **Demonstration of Scalability and Configurability** : We demonstrate the simulator’s scalability and configurability by simulating 10,503 microeconomic agents, including 250 farms, 1,250 companies, 250 retail stores, 8,750 households, one regional bank, a central bank, and a government, where each agent follows rulebased strategies. Additionally, we demonstrate scalability for multi-agent learning by simulating 112 macroeconomic agents, comprising 100 households, 10 firms, a central bank, and a government, each using deep reinforcement learning to arrive at objective-maximizing strategies. 

- **Utility for Monetary and Fiscal Policy Design** : We demonstrate the simulator’s utility for monetary and fiscal policy design through two economic scenarios. In these scenarios, we compare the performance of learned central bank and government policies against standard rule-based policies, illustrating the superior performance of the learned policies. 

## **2 Literature Review** 

### **2.1 Agent-Based Models (in Finance)** 

Agent-Based models (ABMs) are powerful tools for simulating complex systems by defining individual agents and their interactions, even when governed by simple rules. These models often result in emergent behaviors that are far more intricate than the rules themselves [1]. ABMs have found applications across diverse domains, including robotics [3], financial markets [4, 32], traffic management [5], social networks [6]. Recent advances have leveraged large language models (LLMs) as agents to simulate realistic social interactions [7] and achieve human-level performance in strategic games like Diplomacy by integrating natural language negotiation with planning and reinforcement learning [33]. In finance and economics, ABMs are particularly popular for analyzing and developing trading and investment strategies, where real-world testing can be prohibitively expensive or impractical. One of the most significant advantages of ABMs lies in their ability to capture emergent phenomena - outcomes driven by interactions among nonlinear and heterogeneous agents [34]. 

There is long-standing literature in agent-based finance following the Santa Fe Stock Market project [35, 36]. Past works consider agent-based financial modeling within continuous double auction (CDA) markets such as NASDAQ and the New York Stock Exchange [37, 38], using the simulator to (1) investigate particular trading practices such as latency arbitrage [39], spoofing [40], market making [41]; (2) to simulate rare events such as flash crashes [42, 43]; and (3) to design and test new financial 

4 

policies before implementation in real markets [44, 45]. An alternate line of research models over-the-counter (OTC) markets such as foreign exchange markets where liquidity providers and takers interact in a decentralized manner with direct connections to each other (in absence of a centralized exchange) [46, 47]. [48] propose a searchtheoretic framework to model OTC markets, documenting empirical regularities that are common across OTC markets. With access to these simulators, one can use reinforcement learning to learn approximately optimal strategies for different objectives, such as for market making [49–51], large order execution [52], daily investment [52, 53], as well as for mechanism design experiments [44, 45, 54]. 

### **2.2 Economic Models** 

Dynamic Stochastic General Equilibrium (DSGE) models are macroeconomic models widely used by Central Banks for macroeconomic forecasting and policy analysis [55]. They are _dynamic_ as they model the evolution of economic observables over time, _stochastic_ in incorporating external random shocks to the economy. And, they model economies in _general equilibrium_ where the assumption is that supply equals demand for goods and labor. Early work, like [56], introduced a DSGE model with a representative household and firm, analyzing stochastic dynamics local to a balanced-growth path and perturbations around them. [57] overcomes the representative agent assumption of having a single household in the economy by incorporating household heterogeneity in income, wealth, and temporal preferences, using a continuum of households subject to employment shocks. 

Modern macroeconomic modeling focuses on models estimated from real data [58, 59]. This is also seen in [60], where Bayesian techniques are used to estimate a DSGE model with a representative household and firm, incorporating price setting by firms and wage setting by labor unions. [61] explored the impact of monetary policy on household consumption and labor, including dual-asset savings with transaction costs. Numerous software packages are available for estimating and solving DSGE models [62, 63]. The Federal Reserve Bank of New York provides public access to its DSGE model [64], and forecasts [65]. 

Despite the extensive literature, DSGE models rely on restrictive assumptions, such as representative agents, general equilibrium, and individual and aggregate rationality [66]. The representative agent assumption is often employed because authors find that when focusing solely on aggregate macroeconomic behavior, a model with a representative agent performs comparably to more complex models. This finding hinges on the requirement of complete markets and the rational expectations assumption. However, these simplifying assumptions limit DSGE models’ ability to capture the full complexity of real economies [67] and make them susceptible to model mis-specification errors [8]. DSGE models have particularly struggled to simultaneously explain certain stylized facts observed in real economies, especially those related to heterogeneity [68]. Nonetheless, these models are easier to calibrate than agent-based models due to their fewer parameters, restricting the space of equilibria for joint agent policies. 

Numerous studies have examined expectation formation among economic agents, highlighting how individuals interpret the world and form expectations, which influences their economic activity. This underscores the limitations of rule-based behavioral 

5 

modeling of agents by assigning parametric assumptions to agents’ expectations, as restricting the complexity of their decisions. Critiques of the rational expectations model, where agents are assumed to have perfect forecasts of the world, have been noted [21, 69], advocating for the inclusion of adaptive expectations and learning for agents [70]. 

### **2.3 Agent-Based Models in Economics** 

The field of Agent-based Computational Economics (ACE) employs ABMs to simulate interactions among economic agents, addressing key limitations of DSGE models including the inability to capture agent heterogeneity, adaptive behaviors, and outof-equilibrium dynamics [10]. ABMs provide a versatile framework to model complex, heterogeneous, and boundedly rational economic agents with diverse objectives [71]. Furthermore, [21] critiques the assumption of rational expectations in heterogeneous macroeconomic modeling as unrealistic, suggesting that least-squares learning and reinforcement learning are promising approaches to overcome this challenge. 

A prominent example of ABMs in economics is the EURACE project [72], which aimed to build a large-scale model of the European economy. Early simulations explored labor market dynamics, involving capital and consumer goods firms alongside households employing rule-based strategies. Subsequent iterations extended the framework to encompass interactions between labor markets, industry evolution, credit markets, and consumption [73]. 

In studies of systemic risk and financial crises, ABMs have been used to model housing markets, which played a pivotal role in the 2007-2009 financial crisis [74, 75]. These models include mortgage-borrowing households (homeowners) with diverse characteristics who can choose to make payments, prepay loans, or face foreclosure, alongside mortgage lenders. Key scenarios involve examining how exogenous leverage or income shocks impact borrowers’ loan repayment capacity [74, 75]. 

In the context of climate economics, there has been recent work on using ABMs to simulate the impact of global climate negotiations and agreements on global temperatures. [76] introduced a calibrated multi-region climate-economic-trade simulation platform to study negotiation protocols and their effect on fostering cooperation among global regions with differing economic policy objectives. Building upon traditional heterogeneous agent equilibrium models, such as [77], this platform incorporates negotiation protocols, and accounts for international trade and tariffs, offering a testbed for climate-economic policy design. 

ABMs are increasingly being explored as experimental platforms for macroeconomic policy design across a range of applications, including fiscal and monetary policy, bank regulation, structural reforms in the labor market, and climate change policies. However, important challenges remain, particularly regarding their empirical validation, over-parameterization, estimation, and calibration [66]. Calibrating ABMs with numerous agents and diverse agent types using real data presents challenges due to the large degree of freedom arising from the variables and parameters that characterize agents’ decision rules [31]. 

The most common method for validating the assumptions and effectiveness of an ABM as a realistic model of the true economic system is through indirect calibration. 

6 

This involves assessing whether the model can replicate a set of statistical regularities observed in real economic data, known as _stylized facts_ , which are selected by the model designer for validation purposes. Substantial work has focused on ABMs of endogenous growth and business cycles, which are empirically validated by replicating sets of microeconomic and macroeconomic stylized facts [78, 79]. These models typically employ rule-based agents with predefined behaviors, providing a framework for comparing behavioral rules, particularly in the context of monetary and fiscal policies [80]. For a comprehensive survey of ABMs in macroeconomic analysis, see [81]. 

### **2.4 Agent-Based Economic Modeling and Reinforcement Learning** 

Since economic models often depict households as entities maximizing their discounted utility over time, reinforcement learning (RL) techniques are particularly well-suited for modeling household behavior [82]. For instance, [24] employed RL to derive consumption, saving, and labor strategies for a representative household in a DSGE model proposed in [83]. Similarly, [23] applied RL to learn consumption and labor strategies for heterogeneous households in macroeconomic models that incorporate epidemiological dynamics under equilibrium. In the domain of housing markets, [84] utilized RL to develop policies for mortgage-borrowing households within an ABM encompassing heterogeneous households, mortgage servicers, mortgage owners, and the broader economy. Their experiments examined the impacts of exogenous income shocks on borrowers across income quartiles, revealing that lower-income borrowers were disproportionately affected. 

Beyond household strategies, RL has been used to optimize other economic strategies. For example, [85] explored the design of a human-preferred revenue redistribution mechanism, while [24, 25] investigated central bank monetary policy, and [22] examined government tax policy. [85] addressed the problem of ‘value alignment’, focusing on developing AI systems whose decisions align with human preferences. They used RL to design a shared revenue redistribution mechanism in an online investment game played by groups of humans. Their findings indicated that the RL mechanism, trained to maximize votes from virtual human players (modeled using sample human data), was preferred by real players over baseline mechanisms, including egalitarian and libertarian approaches. [25] demonstrated that their RL-derived monetary policy outperformed traditional rule-based interest rate policies, like those in [86, 87], in achieving inflation and productivity targets [88]. Here, the environment (containing everything other than the central bank), modeled as a neural network fitted to historical U.S. data, predicted inflation and productivity in response to actions of the central bank. 

Despite significant advancements, many RL studies focus on strategies for a single agent type or a small subset of agent types. However, a significant critique of modeling and learning economic agents in isolation comes from [89], which highlights the inability of such models to account for how other agents react to changes in an agent’s policy. [22] pioneered the use of multi-agent RL (MARL) in economic ABMs by exploring tax policy design with four agents and a planner. The planner optimized marginal tax rates to balance equality and productivity, while agents maximized utility based 

7 

on their endowments. [27] introduced a macroeconomic real-business-cycle ABM that applied MARL to 100 consumers, 10 firms, and a government. However, their model omitted unemployment modeling, the central bank’s role in monetary policy, used uniform tax redistribution, and lacked economic shocks. [28] developed an ABM for taxation study, using MARL for 10,000 household agents that optimized consumption utilities while the government aimed to enhance social welfare and economic growth. Similarly, [26] utilized MARL in a macroeconomic ABM with capital and credit markets to learn price-quantity strategies for 20 consumer-goods firms, while households, capital-goods firms, and banks followed fixed strategies. 

While MARL applications in economic ABMs remain relatively nascent, this field is expanding [90–93]. In this work, we develop an economic model with heterogeneous households, heterogeneous firms, a central bank, and a government. All agents learn and adapt using MARL, in presence of economic shocks. To reduce the space of possible joint agent policies, we assume symmetric/exchangeable policies across agents within each category. Crucially, to calibrate the multi-agent economic system, we ground agent parameters and actions in real economic data. Subsequently, we validate the model where agents follow their learned policies, against a broad set of economic stylized facts which are also surveyed in this work. 

## **3 Multi-Agent Economic System** 

Our economic model consists of four types of agents as shown in Figure 1. 

- **Households** who are the consumers of goods and provide labor for the production of goods 

- **Firms** who utilize labor to produce goods and pay wages 

- **Central Bank** that monitors price inflation and production to set interest rate for household savings and firm deposits 

- **Government** that collects income taxes from households and corporate taxes from firms, part of which could be redistributed as tax credits 

Each agent type has specific objectives and uses available economic information to adjust their actions to meet those objectives. Households aim to maximize utility from consumption and savings, adjusting their consumption based on prices, wages, interest rates, and tax information. Firms seek to maximize profits by setting prices and wages, informed by labor availability, past consumption, interest rates, and tax rates. The central bank targets inflation control and GDP growth, adjusting interest rates based on current inflation and GDP data. The government focuses on social welfare, setting tax rates and distributing tax credits based on household inequality and tax revenue. 

Overall, each agent uses available economic information to adjust their actions. This behavior can be defined using functional rules that map input information to output actions, such as the Taylor rule for monetary policy or firm pricing using a fixed markup over production costs. While such predefined behavioral rules allow for faster simulations, they can limit agents’ ability to achieve higher utility in shock scenarios, thereby restricting the robustness of their behaviors (as we demonstrate in our experiments). In contrast, the availability of a simulator combined with advances 

8 



**Fig. 1** Agent types and interactions in ABIDES-Economist. 

in deep reinforcement learning (RL) enables us to learn these behavioral rules from simulated agent interaction data, including data from shock scenarios. Thus, while our simulator accommodates both rule-based and learning agents, we focus on agents that learn behaviors through interactions, using a multi-agent reinforcement learning (MARL) framework. In this MARL framework, each agent’s long-term objectives are represented through a per-step reward function that is accumulated over time. And, we aim to learn policy functions (behavioral rules) that map observations to actions. 

Formally, our economic model with multiple RL agents is represented as a Markov Game, where each agent has partial observability of the global system state [16, 17]. The global system state encompasses all information relevant to all agents in the system (e.g. savings of all households, inventories of all firms, etc.), as well as systemspecific information like shock variables. So, the global system state along with actions of all agents fully determine the next global state, capturing the Markov assumption. As expected, each agent only has access to partial information about the global state, including their own observables and publicly available data such as tax and interest rates. 

A finite horizon Partially Observable Markov Game (POMG) is denoted by Γ = _⟨N , S, {Ai}_<sup>_n_</sup> _i_ =1<sup>_, {Oi}n_</sup> _i_ =1<sup>_,_T</sup><sup>_, {_O</sup><sup>_i}n_</sup> _i_ =1<sup>_, {Ri}n_</sup> _i_ =1<sup>_, {βi}n_</sup> _i_ =1<sup>_, H⟩_where</sup> 

- _N_ = _{_ 1 _,_ 2 _, · · · , n}_ is the set of agents 

- _S_ is the state space 

- _Ai_ is the action space of agent _i_ with _A_ = _A_ 1 _× A_ 2 _× · · · × An_ denoting the joint action space 

- _Oi_ is the observation space of agent _i_ 

- T : _S × A →_ P ( _S_ ) is the transition function mapping the current state and joint action to a probability distribution over the next state 

9 

- O _i_ : _S →_ P ( _Oi_ ) is the observation function mapping the current state to a probability distribution over observations of agent _i_ 

- _Ri_ : _S × A →_ R is the reward function of agent _i_ 

- _βi ∈_ [0 _,_ 1) is the discount factor of agent _i_<sup>2</sup> 

- _H_ is the horizon 

The objective of each agent _i ∈N_ in a POMG is to find a sequence of their own actions that maximizes their expected sum of discounted rewards over the horizon 



where _s_ ( _t_ + 1) _∼_ T ( _s_ ( _t_ ) _, a_ 1( _t_ ) _, · · · , an_ ( _t_ )) _∀t_ . Here, _t_ represents a time step in the simulation, typically one quarter of a year in macroeconomic models. Hence, an agent _i_ with a predefined behavioral rule has a fixed function _f_ that outputs its action given its observation as _ai_ ( _t_ ) = _f_ ( _oi_ ( _t_ )) where _oi_ ( _t_ ) _∈Oi_ and _ai_ ( _t_ ) _∈Ai_ . In a learning context, this function _f_ is updated over training steps using simulated agent interaction data. Without loss of generality, we describe the learning agent setup where we use index _i_ for households and _j_ for firms as we detail agent observations, actions, and rewards, thereby formalizing the POMG for our system. 

### **3.1 Households** 

Households are the consumer-workers in the economic system that provide labor for production at firms, while also consuming some of the produced goods. When employed, they are paid wages for their labor at their employer firm, and pay for the price of consumed goods. The government collects income taxes on their labor income, part of which could be redistributed back to households as tax credits in the subsequent time step. They also earn (accrue) interest on their savings (debt) from the central bank. These monetary inflows and outflows govern the dynamics of household savings/deposits from one time step to the next. 

The **observations** of household _i_ at time _t_ include tax credit _κt,i_ , tax rate _τt,_ H, interest rate _rt_ , prices of goods of all firms _{pt,j_ : _∀j}_ , wage at employer firm � _j_<sup>_wt,jet,ij_where</sup><sup>_et,ij_istheemploymentindicatorofhousehold</sup><sup>_i_atfirm</sup><sup>_j_,their</sup> monetary savings _mt,i_ and their skills at all firms _{ωij_ : _∀j}_ . The employment indica1 _,_ if household _i_ is employed by firm _j_ at time _t_ tor _et,ij_ = captures if and where �0 _,_ otherwise household _i_ is employed at time _t_ . Note that<sup>�</sup> _j_<sup>_et,ij≤_1sothateveryhouseholdcan</sup> be employed by at most one firm at time _t_ . Household skills are used by firms in their hiring and firing decisions as described in section 3.2. When employed, each household provides _n_ ¯ hours of labor at their employer firm. 

The **actions** of household _i_ include the units of good requested for consumption at all firms _{c_<sup>req</sup> _t,ij_<sup>:</sup><sup>_∀j}_.</sup> 

> 2The symbol _β_ is used for the discount factor instead of the standard _γ_ , as _γ_ is designated for a parameter related to households. 

10 

The **dynamics** related to household _i_ are given by 



where (1) handles the case when the requested consumption per firm _j_ exceeds its inventory along with produced goods. Here, goods are distributed proportionally to households based on their requests, to give the realized consumption for household _i_ of goods of firm _j_ at _t_ as _ct,ij_ . (2) is the evolution of savings from _t_ to _t_ + 1 based on interest earned/accrued, labor income, consumption spending, taxes paid on labor income, and tax credits received from the government. 



where 

with an isoelastic utility from consumption and savings, and a quadratic disutility of labor<sup>3</sup> [83]. Households can exhibit heterogeneity in their skill levels across firms and in the parameters of their utility functions. Table 1 provides an overview of agent parameters, including those associated with heterogeneity. 

### **3.2 Firms** 

Firms are the producer-employers in the economic system that use household labor to produce goods for consumption. They forecast consumption demand to set desired production and employment levels based on which they hire/fire households based on their skills. Labor from employed households is used to produce goods subject to an exogenous, stochastic production factor that captures any external shocks [23]. Firms accumulate inventory when they produce more goods than consumed by households, which they seek to minimize. They profit on revenue from prices paid by households for consumed goods, and pay wages for labor received from employed households. They pay taxes to the government on non-negative profits, and earn (accrue) interest on their deposits (debt) from the central bank. These monetary inflows and outflows govern the dynamics of firm deposits from one time step to the next. 

The **observations** of firm _j_ at time _t_ include tax rate _τt,_ F, interest rate _rt_ , total household labor ¯ _n_<sup>�</sup> _i_<sup>_et,ij_, total consumption �</sup> _i_<sup>_ct,ij_, exogenous shock</sup><sup>_εt,j_, exogenous</sup> production factor _ϵt−_ 1 _,j_ , previous wage _wt,j_ , previous price _pt,j_ , inventory _Yt,j_ , and deposits _dt,j_ . 

> 3Although we consider utility that is additive in consumption, labor and savings, our framework is flexible to use of any other. 

11 

|Agent|Parameter|
|---|---|
|Household _i_|_ωij_: Skill level at firm _j_<br>_γi_: Isoelasticity parameter<br>_νi_: Weighting of labor disutility<br>_µi_: Weighting of savings utility<br>_βi,_H: Discount factor<br>¯_n_: Number of hours of labor at employer|
|Firm _j_|_ω_min: Minimum household skill to be hired by this firm<br>_αj_: Production elasticity for labor<br>_ρj,_¯_εj, σj_: Parameters of the exogenous shock process<br>_χj_: Weighting of inventory risk<br>_βj,_F: Discount factor|
|Central Bank|_π_<sup>_⋆_</sup>: Target inflation<br>_λ_: Weighting factor for production<br>_β_CB: Discount factor|
|Government|_lt,i_: Weighting of households for social welfare<br>_ξ_: Portion of collected tax redistributed among households<br>_θ_: Weighting of household utility in government reward<br>_β_G: Discount factor|



**Table 1** Parameters for agents in our economic model. 

The **actions** of firm _j_ include wage per unit of labor _wt_ +1 _,j_ and price per unit of good _pt_ +1 _,j_ that go into effect at the next time step. 

The **dynamics** of quantities related to firm _j_ are given by 















At the beginning of time step _t_ , each firm _j_ forecasts net consumption demand from all households _C_<sup>ˆ</sup> _t,j_ based on previous values as in (3), to compute the desired production _y_ ˆ _t,j_ based on current inventory in (4) and desired labor hours from employees _N_<sup>ˆ</sup> _t,j_ in (5). The hiring/firing process for firms works as follows. If the firm requires more labor than can be provided by current employees _N_<sup>ˆ</sup> _t,j > n_ ¯<sup>�</sup> _i_<sup>_et−_1</sup><sup>_,ij_,itsendshiring</sup> 

12 

requests to all unemployed households with high skill _ωij ≥ ω_ min<sup>4</sup> . Each unemployed household chooses among all hiring firms to provide labor to that firm at which it has highest skill. If the firm requires less labor than will be provided by current employees _N_ ˆ _t,j < n_ ¯<sup>�</sup> _i_<sup>_et−_1</sup><sup>_,ij_,itsendsfiringrequeststoallextraemployeeswithlowestskills,</sup> ensuring it has at least one employee. 

After hiring/firing/not changing employees, the firm produces with employee labor per a Cobb-Douglas production function with elasticity parameter _αj ∈_ [0 _,_ 1] [94] as in (7). Here, _ϵt,j_ represents an exogenous production factor following a log-autoregressive process with coefficient _ρj ∈_ [0 _,_ 1] as in (6), with _ϵ_ 0 _,j_ = 1 and _εt,j ∼N_ � _ε_ ¯ _j, σj_<sup>2</sup> � being an exogenous shock. The firm updates its inventory for the next time step based on current inventory and the difference between supply and demand as in (8). The deposits of the firm evolve from _t_ to _t_ + 1 based on interest earned/accrued, profits, and taxes paid to the government on non-negative profits as in (9). 

The **reward** for firm _j_ at _t_ is given by 



where the first two terms represent monetary profits as the difference in revenue from consumed goods and wages paid, with the last term capturing the risk of accumulated inventory. Firms exhibit heterogeneity in their sectors, which is equivalently captured by the shock process and the production function that transforms labor into goods. The parameters related to firm heterogeneity are provided in Table 1. 

### **3.3 Central Bank** 

The central bank is the regulatory agency that monitors the prices and production of goods to set interest rates for household and firm deposits. By changing the interest rate on deposits, it affects the consumption patterns of households, which in turn affect the prices of goods produced by firms. The central bank seeks to set interest rates to meet inflation targets and boost production. Although it is uncommon for standard economics papers to focus on learning a policy for the Central Bank, our simulator retains this capability for generality of application e.g. learning monetary policy in presence of rule-based household and firm agents. Previous studies have explored similar learning models for central banks, as seen in [25, 69, 70]. 

The **observations** of the central bank at time _t_ include previous interest rate _rt_ , total price of goods over the last five quarters _{_<sup>�</sup> _j_<sup>_pt−k,j_:</sup><sup>_∀k∈{_0</sup><sup>_,_1</sup><sup>_,_2</sup><sup>_,_3</sup><sup>_,_4</sup><sup>_}}_,and</sup> total production across firms<sup>�</sup> _j_<sup>_yt,j_.</sup> 

The **action** of the central bank includes the interest rate _rt_ +1 that goes into effect at the next time step. 

The **dynamics** related to the central bank are given by 



> 4Although it is straightforward to assign different minimum skill thresholds across firms, we adopt a uniform threshold for simplicity. 

13 

where _πt_ is the annual inflation in total price. 

The **reward** for the central bank is given by 



where _π_<sup>_⋆_</sup> is the target inflation rate. And, _λ >_ 0 weighs the production reward in relation to inflation targeting. 

### **3.4 Government** 

The government is the regulatory agency that collects taxes from households on their labor income and from firms on their profits, in order to maintain infrastructure. It sets tax rates and can choose to distribute a portion of the collected taxes back to households as tax credits in order to improve social welfare. 

The **observations** of the government at time _t_ include the previous tax rates _τt,_ H, _τt,_ F, previous tax collected _{τt,_ H � _j_<sup>_et,ijnw_¯</sup><sup>_t,j_:</sup><sup>_∀i}_,</sup><sup>_{τt,_F max</sup><sup>_{_0</sup><sup>_, pt,j_</sup> � _i_<sup>_ct,ij−_</sup> _wt,j_ � _i_<sup>_ne_¯</sup><sup>_t,ij}_:</sup><sup>_∀j}_,previoustaxcredits</sup><sup>_{κt,i_:</sup><sup>_∀i}_,andatimevaryingweightasso-</sup> ciated to each household in relation to social welfare _{lt,i_ : _∀i}_ . Our framework allows the designer to choose weights _lt,i_ based on their choice of social welfare metric e.g., _lt,i ≡_ 1 for the utilitarian social welfare function versus _lt,i_ = 1 _{i_ = arg min _k mt,k}_ for the Rawlsian social welfare function. 

The **actions** of the government include the tax rates _τt_ +1 _,_ H, _τt_ +1 _,_ F, and the fraction of tax credit distributed to each household _i_ , _ft_ +1 _,i_ that go into effect at the next time step. 

The **dynamics** related to the government are given by 



where _ft,i ∈_ [0 _,_ 1] with<sup>�</sup> _i_<sup>_ft,i_= 1sothataportion</sup><sup>_ξ∈_[0</sup><sup>_,_1]ofallcollectedtaxesare</sup> redistributed. (11) gives the tax credit for household _i_ at _t_ + 1 as a fraction _ft_ +1 _,i_ of the _ξ_ portion of total tax collected in step _t_ . 

The **reward** for the government is a measure of household social welfare, computed herein as a weighted sum of household utilities and tax credits as 



where _lt,i_ is the weight associated to household _i_ , _Rt,i,_ H = _u_ �� _j_<sup>_ct,ij,_¯</sup><sup>_n_�</sup> _j_<sup>_et,ij, mt_+1</sup><sup>_,i_;</sup><sup>_γi, νi, µi_</sup> � is the reward function measuring the utility for household _i_ at time _t_ , and _θ ∈_ [0 _,_ 1] weighs household utility relative to tax credits. 

14 

## **4 ABIDES-Economist Simulator** 

Our simulator is based on ABIDES, an agent-based interactive discrete event simulator that has been widely used to simulate financial markets with different types of trading agents [4]. Agents in ABIDES have access to their internal states, and can receive information about other agents via messages. A simulation kernel handles message passing between agents, and runs simulations over a specified time horizon while maintaining timestamps for all agents and the simulation itself. We now describe the key components of setting up and running a simulation in ABIDES-Economist. 

### **4.1 Agent Configuration** 

ABIDES-Economist defines a distinct agent class for each agent type described in Section 3, initialized with default parameters obtained from the literature. Table 2 outlines the default parameter values and their sources used in our simulator. For every simulation run, users must specify the simulation horizon in quarters, the number of agents within each type, and any agent heterogeneity parameters that deviate from the default values. When modeling agent heterogeneity or testing hypothetical economic scenarios, the default parameters are replaced by the specified values. 

Agents in our simulator can only access their internal states, so any information from other agents must be explicitly requested through message-based communication. When a message request for information is sent, the recipient responds by sharing the relevant part of their internal state with the sender. To configure agents, we establish message-based communication channels based on the granularity and dynamics of the economic system. For instance, a household agent sends a message to each firm agent requesting the price of its goods. The firm agent responds with this information, which the household incorporates into its observations. Conversely, households only communicate with their current employers to obtain information about wages. 

This messaging scheme ensures that all features in an agent’s observation that are external to itself are dynamically acquired through inter-agent communication. The ABIDES kernel processes these messages sequentially, resulting in simulation run time complexity that is linear in the number of messages exchanged. To optimize performance, we minimize the number of messages in the system. Specifically, regulatory bodies communicate with households and firms through one-way messages, and only employee households exchange labor-related information with their employers. This design reduces overhead while preserving the necessary information flow for accurate agent behavior and system dynamics. 

#### **4.1.1 Temporal Progression in the Simulation** 

Here is how the economic simulation proceeds from one time step _t_ (think quarter of year) to the next over a specified time horizon. At the start of the simulation, 

- Households start with $0 savings, with i.i.d skills sampled at the beginning of every training episode as _ωij ∼N_ (1 _._ 0 _,_ 0 _._ 3). 

- Firms start with 0 units of inventory and $0 deposits, with production elasticity i.i.d sampled at the beginning of every training episode as _αj ∼U_ [0 _._ 05 _,_ 1 _._ 0]. Also, 

15 

|Agent|Parameter|Value|Source|
|---|---|---|---|
|Household _i_|_ωij_|i.i.d _N_(1_._0_,_0_._3)||
||_γi_|0_._33|[24]|
||_νi_|0_._50|[24]|
||_µi_|0_._10|[24]|
||_βi,_H|0_._99|[24]<br>|
||¯_n_|480|40 hours/week<br>_≈_480 hours/quarter|
|Firm _j_|_ω_min|1.0|Mean of each _ωij_|
||_αj_|i.i.d _U_[0_._05_,_1_._0]|[95], see appendix A|
||_ρj,_¯_εj, σj_<br>_χj_<br>_βj,_F|0_._97_,_0_._00_,_0_._10<br>0_._50<br>0_._99|[23]|
||_f_(_ct−_1_, · · · , c_0)|Exponential Moving Average<br>with half-life of 4 quarters|[78]|
|Central Bank|_π_<sup>_⋆_</sup>|1_._02|[25, 88]|
||_λ_|1_._00|[25]|
||_β_CB|0_._99|[25]|
|Government|_lt,i_<br>_ξ_|_lt,i_ =<br>1<br>_mt,i_+max_i{−mt,i}_+_ϵl_ <sup>,</sup><br>normalized by <sup>�</sup><br>_k _<sup>_lt,k_ with</sup> <sup>_ϵl_ = 1</sup><sup>_._0</sup><br>0_._10|Inverse-income<br>weights<br>[96]<sup>_∗_</sup>|
||_θ_|1_._00||
||_β_G|0_._99||



**Table 2** Default agent parameters in ABIDES-Economist. 

> _∗_ Based on IRS data from 2023, 15% of the income taxes collected from businesses and individuals were refunded to individuals [96]. We assume that two-thirds of these refunds, equivalent to 10%, are related to tax credits, while the remaining portion is due to excess tax refunds. 

they each draw independent samples of price and wage for _t_ = 0 from a uniform distribution over their action space. 

- All households are distributed among firms for employment uniformly at random, so that every household is employed at _t_ = 0. 

- Central Bank samples the initial interest rate for _t_ = 0 from a uniform distribution over its action space. 

- Government sets default tax rate and gives out $0 of tax credits for _t_ = 0. 

At each time step _t ≥_ 0, 

1. Each firm computes expected demand for this step based on past demand to compute desired number of employees (3) - (5). 

2. Each firm sends out employment decisions of hiring, firing or status quo based on skills of households. 

3. Unemployed households choose from hiring firms based on highest skill match. 

16 

4. Each firm uses labor from employee households to produce goods (6) - (7), and pays wages to employees. 

5. Each household observes tax rate, tax credits, interest rate, prices, and wage to decide on requested consumption. 

6. Each firm fulfills consumption (1), updates its inventory (8), and pays taxes to the government (9). 

7. Each household updates savings based on realized consumption (2) and pays taxes to the government (2). 

8. Each firm sets price, wage for the next step based on consumption, labor in this step. 

9. Central Bank monitors firm prices until this step and productions at this step to set interest rate for next step. 

10. Government collects taxes to set tax rate and distribute credits for next step (11). 

### **4.2 Scaling of Simulation Run Time with Agent Count** 

Simulation run time within ABIDES-Economist is influenced by three main factors: agent initialization, message processing, and variable/data structure operations. 

- **Agent Initialization** : This involves constructing objects for each agent in the configuration and scales linearly with the total number of agents. 

- **Message Processing** : This accounts for the transmission of information between agents via messages. It is the most significant factor, accounting for over 80% of the total simulation run time. Recall that any information external to an agent must be conveyed via a message object from the sender agent who owns that information. The ABIDES kernel manages message passing between agents by processing them sequentially, resulting in a run time contribution that is linear in the number of messages processed. The number of messages is determined by the specific simulation dynamics described in Section 4.1.1. The greatest message volume complexity arises from price communications between producers and consumers, which scales as _O_ ( _mn_ ), where _m_ is the number of firms and _n_ is the number of households. This, combined with labor/employment interactions, leads to quadratic scaling in run time with the total number of agents. 

- **Data Structure Operations** : These deal with compute operations within agents, and have been optimized using more efficient alternatives. For instance, we employ custom implementations of the Exponential Moving Average instead of the pandas version and replace `numpy.sum()` with Python’s built-in `sum()` function for lists, among other optimizations. 

In summary, the simulation run time per simulation time step within ABIDESEconomist scales quadratically with the total number of agents, and accumulates over the time steps in the simulation horizon. 

To assess the scalability of our simulation platform, we simulate a regional economy with _m_ farms, 5 _m_ companies, _m_ retail stores, 35 _m_ households (five times as many households as employers), along with one regional bank, a central bank, and a government, where each agent follows rule-based strategies. Here, farms and companies fall within the firm category mentioned throughout this paper, with retail stores sourcing 

17 

products from farms and selling to households, while companies sell directly. Farms, companies, and retail stores act as employers, with households serving as potential employees. The regional agents including farms, companies, retail stores, households and regional bank update their actions every two weeks, while the federal agents including the central bank and the government update their actions every quarter. Hence, the regional agents act 26 times a year while the federal agents act four times a year. 

The objective of this agent configuration is to test scalability in a scenario with increased inter-agent communication and to demonstrate the customizability of our simulator, which allows for adaptation of the agent configuration to fit specific scenarios of interest. The increase in inter-agent communication arises from two sources. Firstly, these regional agents act more frequently than the macroeconomic agents presented earlier, which act once per quarter. Secondly, there is an increase in inter-agent connections from introducing a retail firm layer between households and farms and designating the regional bank to handle the banking needs of all microeconomic agents, while the central bank focuses on macroeconomic monetary policy. 



**Fig. 2** Simulation run time and number of messages processed as functions of agent count. Note that the run time scales quadratically with the agent count and linearly with the number of messages processed. 

We vary _m_ in the range _{_ 2 _,_ 25 _,_ 50 _,_ 75 _,_ 100 _,_ 125 _,_ 150 _,_ 175 _,_ 200 _,_ 225 _,_ 250 _}_ and plot the simulation run time and total number of messages processed per biweekly period across 10 instantiations of each configuration in Figure 2. We used an AWS EC2 instance (type c5.4xlarge) with 16 vCPUs and 32GB RAM. The first subplot of Figure 2 shows boxplots of the simulation run time as a function of the total agent count, displaying a quadratic relationship. The second subplot shows boxplots of the number of messages processed by the kernel as a function of agent count, again displaying a quadratic relationship. The last subplot displays median simulation run time as a function of the median number of messages processed, showing a linear relationship. These trends align with our earlier explanation that sequential message processing is the primary factor influencing the scalability of simulations as the agent count increases. 

Notably, we successfully simulated a model with up to 10,503 rule-based agents, exchanging nearly 50 million messages per simulation step of two weeks, with a run time of around 20 minutes on the specified instance. We capped the agent count at 10,000 because increasing it beyond 15,000 led to out-of-memory issues on the instance from instantiating the large number of agent objects. Further reductions in run time can be achieved in economic scenarios with fewer inter-agent connections or where 

18 

these connections are not continuously active. For instance, macroeconomic configurations with fewer inter-agent connections, fixed employment relationships without constant hiring and firing, or less frequent updates by regulatory bodies, such as the central bank and government, can improve efficiency. 

### **4.3 Reinforcement Learning capabilities** 

#### **4.3.1 Single-Agent Learning** 

The original ABIDES framework was extended to incorporate a single reinforcement learning (RL) agent using an OpenAI Gym-style extension [52]. In this ABIDES-Gym setup, a Gym environment encapsulating the Markov Decision Process (MDP) for a single RL agent interacts with the core of ABIDES, which contains all rule-based agents, through a placeholder agent known as the Gym agent. The Gym agent serves as a proxy for the learning RL agent in its interactions with the rule-based environment. In this setup, the Gym agent takes an action based on the current state of the world, prompting the remaining background agents to react and evolve the system to the next state. The Gym environment computes the corresponding next state and reward for the learning agent. Subsequently, any RL algorithm can be employed to derive an approximately optimal policy for the learning agent. 

The learning process for a single RL agent involves three key steps: (1) MDP formulation by defining the states, actions, and rewards within the Gym environment; (2) capturing transition dynamics through the simulator’s agent configuration, which includes all other background agents; and (3) selecting an appropriate RL algorithm to derive an optimal policy for the agent using environment interactions. The first two steps were discussed previously. For the third step, the choice of algorithm depends on the type of state and action space for the agent. Classical RL algorithms, like tabular Q-Learning [97], are suited for discrete state and action spaces. In our scenarios, we typically encounter continuous states and/or actions, necessitating the use of neural network representations for the value function and/or policy, i.e., requiring deep RL algorithms. 

Popular deep RL algorithms for continuous state/action spaces include deep Q- Learning [98], vanilla policy gradient [99], trust region policy optimization [100], and proximal policy optimization (PPO) [101]. The latter three are policy gradient algorithms, which construct a parameterized representation of the policy using a neural network, with weights updated by gradient ascent on the value/advantage function [99]. These algorithms are favored for their learning stability, with PPO demonstrating reliably superior performance across benchmark RL tasks [101]. 

#### **4.3.2 Multi-Agent Learning** 

We extend ABIDES-Gym to accommodate multiple RL agents by creating a multiagent Gym environment that encapsulates a formalized Markov Game, with the Gym agent representing all learning agents in the system. This Gym agent interacts with the core of ABIDES which contains all rule-based agents, to generate the next system state. And, the Gym environment uses it to compute the learning agents’ rewards. This setup allows for a mix of learning and rule-based agents. A similar extension to 

19 

multi-agent reinforcement learning (MARL) within ABIDES has been applied in the financial domain [45]. 

The learning process for multiple agents involves three key steps: (1) Markov Game formulation by defining observations, actions, and rewards for all learning agents within the Gym environment; (2) capturing transition dynamics through the simulator’s agent configuration, which includes all other rule-based agents; and (3) selecting an appropriate MARL algorithm to develop effective policies for multiple learning agents using environment interactions. Here, the choice of algorithm is also influenced by the nature of agent interactions - collaborative (shared rewards), competitive (zero-sum rewards), or mixed (neither cooperative nor competitive), in addition to the observation and action spaces of the agents. In our scenario, agents have individual objectives that are neither cooperative nor competitive, placing their interactions in the mixed category. Given their continuous observation spaces, deep MARL algorithms are required. 

From a theoretical perspective, as more agents are equipped with RL capabilities, the learning problem becomes more challenging due to non-stationarity. Transition dynamics and agent rewards are both functions of all agents’ actions, which are adapted over time. As multiple agents simultaneously change their behaviors, each agent’s environment (everything other than itself) becomes non-stationary, causing the optimal policy to change over time as other agents’ policies evolve [102]. This can result in learning process instabilities, preventing convergence. Additionally, partial observability presents a challenge, as agents cannot see other agents’ information and are unaware of the global system state. Their reward functions depend on the global state and other agents’ actions, neither of which are observable. While algorithms exist for partially observable Markov Games, they require agents to maintain beliefs over the global state and other agents’ policies, which can become intractable in high-dimensional problems with many learning agents [103]. 

In this work, we partially mitigate non-stationarity and partial observability challenges using the following techniques: 

1. **Realistic Agent Communication** : Agents exchange realistically shareable information, which alleviates much of the observability limitations, especially concerning agent rewards. For example, firms share prices with consumers and wages with employees, while regulatory bodies share tax and interest rates with all agents. 

2. **Partial Centralized Training** : We adopt a hybrid approach that falls in between fully centralized training and independent learning [104]. All agents of the same type share a common policy network, allowing them to exchange experience tuples with each other. This enables agents of the same type to share knowledge and diverse experiences, potentially accelerating the learning process [103]. These four shared policy networks corresponding to the four agent types, are then updated simultaneously using independent learning. As mentioned in the introduction 1, this inductive bias helps regularize the space of potential joint agent behaviors by assuming exchangeability of policies within each agent category [20]. It also acts as an equilibrium selection mechanism within the extensive space of joint agent policies considered by MARL within ABMs. 

20 

3. **Learning Rates** : Through trial-and-error, we discovered that having firms and the central bank adapt more quickly than households and the government leads to improvement and approximate convergence of all agents’ rewards over training episodes. We attribute this division into two tiers of learner groups - one adapting faster than the other - to the specific dynamics of our system, as described in Section 3. Notably, firms have greater authority in setting wages, with households having limited options to respond to low wages in the labor market, other than reducing consumption. These wages also influence the income taxes collected by the government and subsequent tax credits. Similarly, households lack alternative investment options beyond depositing their savings in the central bank, thus limiting their response to interest rates to varying consumption. Consequently, we hypothesize that having households and the government adapt more slowly than the more influential actors, such as firms and the central bank, stabilizes the learning process. 

#### **4.3.3 Scalability of Multi-Agent Learning** 

We define training time as the total compute time required to achieve improvement and approximate convergence of rewards for all learning agents. Our goal is to quantify how training time scales as a function of (1) the total agent count and (2) the learning agent count. Training time can be decomposed as the product of two contributing factors: simulation time per training episode and the number of training episodes. As discussed previously, simulation run time scales quadratically with the total number of agents. This relationship holds true even when multiple agents are learning, as it depends solely on the total number of agents in the configuration, irrespective of the number of learning agents. 

Regarding the second contributing factor, training time scales linearly with the number of training episodes since episodes are executed sequentially. However, the number of episodes needed to reach a desired level of performance is heavily influenced by the specific dynamics and interactions among the agents, as well as the number of learning agents or even the total number of agents. For instance, cooperating agents who share information may require fewer training episodes when learning together compared to learning individually. Conversely, competing agents may need significantly more episodes when learning in the presence of other competing learners than when learning alone. In the next subsection, we conduct a small study of training time to provide further insight into this relationship within our economic system. 

In summary, training time increases at least quadratically with the total number of agents when the number of learning agents is fixed. It also scales linearly with the number of training episodes required for approximate convergence. The relationship between the number of training episodes required and the total agent count or learning agent count is heavily dependent on the problem setup. In practice, we utilize the RLlib package, which offers a wide selection of off-the-shelf single-agent and multiagent RL algorithms [105]. This package also provides scalability through parallel environment sampling, allowing the simultaneous collection of training batches that are used to update the policy networks. By sampling environments in parallel, we 

21 

can significantly reduce the total training time compared to sequential sampling, by a factor proportional to the number of parallel environment samplers. 

#### **4.3.4 Impact of Multiple Learning Agents** 

To better understand the impact of having multiple learning agents on training time and learned policies, we conduct a simple experiment. We consider three economic configurations, each comprising one household ( _ω_ = 1), one firm ( _α_ =<sup><u>2</u></sup> 3<sup>asin[23],</sup> _σ_ = 0 _._ 01), one central bank, and one government ( _θ_ = 0 _._ 2), over a 10-year horizon. 

- **Configuration 1 (LH)** : A policy is learned for the single household, while all other agents follow random policies. 

- **Configuration 2 (LF)** : A policy is learned for the single firm, with all other agents following random policies. 

- **Configuration 3 (LH + LF)** : Policies are learned for both the household and the firm, while the remaining agents follow random policies. 

The use of random policies for other agents simulates the presence of rule-based background agents, with the rule being defined by the random initialization of their policy neural networks. 

To assess the impact on training time, we examine the number of training episodes required for the rewards to improve and approximately converge. Specifically, after confirming reward improvement over training episodes, we determine the number of training episodes _Nϵ_ beyond which agents’ rewards remain within an _ϵ_ -percentage range around the mean long-run reward. This provides an estimate of the required compute time _Tϵ_ needed to reach a certain level of training convergence in the different configurations. These experiments are run on an AWS EC2 instance (type c5.12xlarge) with 48 vCPUs and 96GB RAM, where we allocate 16 vCPUs per configuration. Figure 3 shows the training rewards along with _Nϵ_ and _Tϵ_ for _ϵ_ = 5%. When only the household is learning, it takes _Nϵ_ = 71 _,_ 489 episodes (or 60.44 minutes of training time) to reach and remain within 5% of the long-term rewards. Similarly, when only the firm is learning, it takes _Nϵ_ = 2 _,_ 703 episodes (or 2.14 minutes of training time) to achieve approximate convergence. On the other hand, when both agents are learning, the number of episodes needed for convergence significantly increases to over 132,000 for the household reward and over 131,000 for the firm reward. This demonstrates that as the learning agent count increases even with the same total agent count, the training time for our economic system also increases. 

To evaluate the impact on learned policies, we play out the three sets of learned policies in 100 test episodes each. Figure 4 shows the distribution of key household and firm observables across test episodes for the three configurations. The legends display the mean values, with standard deviations indicated in brackets. When the household is learning, it maximizes consumption to the highest level allowed as it can sustain savings while achieving positive consumption and savings utilities. When the firm is learning, it reduces wages to maximize profits thereby reducing household income. At the same time, it also lowers prices to maintain household consumption and minimize inventory risk. Comparing the three configurations, we observe that when only one agent is learning, its rewards are higher than when only the other agent is learning. For 

22 



**Fig. 3** Training rewards for the **LH** , **LF** , and **LH + LF** configurations to demonstrate the impact of multiple learning agents. When both household and firm are learning, more training episodes are needed for the rewards to improve and converge as compared to when only one of them is learning. 













**Fig. 4** Histograms of key household and firm variables to demonstrate the impact of multiple learning agents. Notice the increase in household consumption, decrease in firm wages, and decrease in firm prices when one or both agents are learning. Importantly, both agents achieve higher rewards when both are learning, as they adapt their behavior in response to one another. 

example, the household achieves higher rewards in the **LH** configuration than in **LF** , while the firm achieves higher rewards in **LF** than under **LH** . Interestingly, both the household and firm achieve higher rewards when both are learning, as they optimize their own objectives while also learning to respond to each other. This is also affected by the choice of random policies for the non-learning agents in all configurations. That is, in **LF** , the household follows a random policy whereas in **LH + LF** , it learns a policy that increases consumption in presence of the firm that learns a policy to further reduce prices. This reduces the inventory risk and improves the reward of the firm alongside the household reward from consumption. 

23 

### **4.4 Sources of randomness** 

There are two primary sources of randomness in each simulation run of our economic system. The first pertains to the employment process. At the start of each simulation episode, households are randomly assigned to firms for initial employment. Over the course of the episode, firms adjust their workforce by hiring or firing households based on their desired production levels to meet demand. When hiring, they seek unemployed households with high skill and when firing, they lay off employees with low skills. The second source of randomness arises from the exogenous shock that impacts firm production. 

A subtle related point is that during training, households are assigned random skills in every episode. This ensures that policies are trained on a diverse set of observations encompassing varied skill profiles. Similarly, firms are assigned random production elasticity parameters in every episode. During testing, these skill levels and production elasticity parameters are fixed across multiple simulation episodes to evaluate policy behavior under specific scenarios. However, the randomness associated with initial employment assignments and exogenous shocks remains, introducing variability to test outcomes across episodes and providing insights into policy robustness. 

## **5 Calibration and Stylized Facts** 

The primary objective of any model representing a real-world system is to approximate the true data-generating process accurately enough to provide a faithful representation of the data [29]. For a model to be effective in forecasting system behavior or conducting policy analysis, it must closely mirror the real-world system under study. 

Agent-based economic models view the system as evolving from interactions among individual actors, whose modeling is informed by empirical observations of real decision-makers. Compared to general equilibrium models, ABMs offer greater flexibility in capturing heterogeneity among economic actors, such as households and firms, and in modeling agent adaptation to changes in the economic system and environment. However, a key barrier to their widespread adoption by economists is the perceived lack of robustness, stemming from the complex relationship between ABMs and empirical data [31]. Despite realistic assumptions and agent descriptions, ABMs often suffer from over-parameterization due to their many degrees of freedom. Establishing the realism or robustness of ABMs is further complicated, compared to dynamic stochastic general equilibrium (DSGE) models, due to the non-linearities, randomness in individual behaviors and interactions, and feedback between micro and macro levels. 

Existing validation approaches for ABMs fall into three categories: (1) the indirect calibration approach of comparing simulated and real world data using _stylized facts_ [29], (2) the Werker-Brenner approach of calibrating model parameters and initial conditions via empirical validation of resulting outputs [30], and (3) the history-friendly approach of calibrating model parameters and agent decision rules via reproducing historical traces [31]. In a related context, [106] introduces the method of simulated moments (MSM) for financial ABMs, where summary statistics from time series data, termed _moments_ , are identified. These targeted moments capture select stylized facts of interest for model validation. For example, in the context of stock price returns, 

24 

these facts include the absence of return autocorrelations and volatility clustering. The goal of MSM is to adjust the ABM’s parameters so that simulated moments closely match empirical moments for selected stylized facts or targeted moments. Moments not used for validation are untargeted moments, and the choice of targeted moments depends on the economic or financial scenario being simulated. 

The indirect calibration approach is the most widely used given the overparameterization issues common in ABMs, coupled with the requirement for highquality empirical data, especially at micro-levels. Indirect calibration involves four steps: (1) identifying real-world stylized facts relevant to the economic scenario, (2) specifying the model, including dynamical equations for individual agents’ behavior and system evolution, (3) validating the model by comparing its output with real-world data, and (4) optionally using the validated model for policy analysis. We examined the dynamics governing individual agents and their interactions in section 3. In this section, we provide a comprehensive list of stylized facts at various economic granularities, a subset of which may be targeted for specific problems of interest. We calibrate agent parameters and allowed actions using real U.S. economic data as detailed in Tables 2 and 3. We validate the model in section 6.2 and subsequently use the validated model for policy analysis in Section 6.3. 

Stylized facts are empirical regularities observed in real economic data, useful for validating economic models [107]. These patterns that persist over time can vary by scale, ranging from macroeconomic and business cycle related facts to microeconomic facts at the firm and household levels [108]. We survey and categorize stylized facts into macroeconomic facts that relate to aggregate macroeconomic variables such as the Gross Domestic Product (GDP), consumption, inflation, interest rate, unemployment rate, etc.; and microeconomic facts that concern distributions of household and firm variables within a region or country. 

### **5.1 Macroeconomic Stylized Facts** 

#### **5.1.1 Business Cycle Facts** 

We adopt the definition of a business cycle from [109], which describes it as: _“Consisting of expansions occurring at about the same time in many economic activities, followed by similarly general recessions, contractions, and revivals which merge into the expansion phase of the next cycle.”_ According to this definition, business cycles are recurrent but not periodic, with durations ranging from more than one year to ten or twelve years. Importantly, these cycles are indivisible into shorter cycles of a similar character. 

Stylized facts about macroeconomic time series data related to business cycles involve observed empirical relationships between Gross Domestic Product (GDP) and other economic variables at business cycle frequencies [110]. The cyclical components of macroeconomic time series refer to movements within the range of periodicities associated with business cycle durations. Extracting these cyclical components has been extensively studied, with significant contributions on appropriate methodologies and potential pitfalls [111–113]. 

25 

In this work, we use the band-pass filtering technique from [113] to decompose macroeconomic time series into trend, cyclical, and irregular components. Then, we calculate the cross-correlation between the cyclical components of various economic series and GDP, which serves as a proxy for the business cycle. Economic series with large positive correlations with GDP are said to be pro-cyclical, while those with large negative correlations are counter-cyclical. This methodology was employed by [110] to analyze U.S. economic data from 1953 to 1996, revealing the following empirical relationships: 

- Pro-cyclical consumption expenditure 

- Counter-cyclical prices (Consumer Price Index level) 

- Pro-cyclical investment in equipment 

- Pro-cyclical inflation rate 

- Pro-cyclical sectoral employment 

- Pro-cyclical total employment 

- Counter-cyclical unemployment rate 

- Pro-cyclical total labor hours 

- Pro-cyclical average labor productivity 

- Counter-cyclical nominal wages 

- Low correlation of real wages 

- Pro-cyclical nominal interest rate 

- Pro-cyclical imports 

- Counter-cyclical trade balance 

- _(Phillips’ Curve)_ Negative correlation between cyclical components of unemployment and inflation rate 

Among these, the Phillips’ Curve, first proposed by [114], is a widely studied relationship between unemployment and inflation. While Phillips observed a long-run negative relationship between unemployment and inflation in U.K. data, [110] found no stable long-run relationship between these variables in U.S. data. However, they did observe a negative correlation between their cyclical components, which supports the inclusion of this relationship among business cycle facts. 

#### **5.1.2 Empirical regularities unrelated to Business Cycles** 

We now list empirical regularities associated with macroeconomic variables over the long run (unrelated to business cycle durations). 

1. _(Phillips’ Curve)_ A negative relationship between unemployment and the rate of change of nominal wages except when there is a rapid rise in import prices (indicating a shock or war regime), as observed in economic data for the U.K. over 1861-1957 [114]. The Phillips’ curve also expects a negative relationship between unemployment and inflation rate of prices, so that low unemployment is associated with high inflation of prices and vice versa. As mentioned previously, [110] do not find a stable relationship between unemployment and rate of change of wages in the U.S., but do find a negative relationship between their cyclical components. 

26 

2. _(Okun’s Law)_ A negative relationship between rates of change of unemployment and real GDP (expressed in percentage points), as first observed in data for the U.S. for 1947 - 1960 [115]. While this paper estimated that a 1 percentage point increase in unemployment would be associated with a 3.3 percentage point decrease in GDP, this relationship including the magnitude of which have been questioned over the years [116, 117]. 

3. _(Beveridge Curve)_ An inverse relationship between the unemployment rate and the job vacancy rate (defined as the fraction of vacant jobs relative to the labor force size), as evidenced in monthly U.S. economic data from 1952 to 1988 [118, 119]. This relationship is typically represented graphically, with the vacancy rate on the vertical axis and the unemployment rate on the horizontal axis. An outward shift of the curve over time indicates a scenario where the same level of vacancies is associated with higher unemployment, reflecting decreased labor market efficiency. 

4. _(Kaldor’s Stylized Facts on Economic Growth)_ Nicholas Kaldor proposed a set of six stylized facts to describe long-term patterns observed in economic growth, focusing on aggregate production, capital, and income distribution [120–122]. These facts were formulated as ‘stylized’ summaries intended to capture general tendencies, not tied to precise historical accuracy but informed by economic data in the U.K. and U.S.. They are as follows: 

- (a) Steady growth in aggregate production and labor productivity over time, with no observable trend of diminishing productivity growth. 

- (b) Steady growth in amount of capital per worker over time, irrespective of the specific measure of capital used. 

- (c) A stable rate of profit on capital, consistently higher than the long-term risk-free rate. 

- (d) Stability in the capital-GDP ratio over time, reflecting proportional growth in production and capital stock. 

- (e) Stable shares of capital and labor in GDP, suggesting proportional growth in real wages and productivity. 

- (f) Variations in GDP growth and labor productivity rates across countries, with faster-growing economies experiencing rates in the range of 2–5%. 

### **5.2 Microeconomic Stylized Facts** 

#### **5.2.1 Household Facts** 

Here, we investigate the distribution of household variables such as income, wealth, and consumption across households within a region or country. Household income and wealth distributions exhibit significant inequality, characterized by right-skewed, fat-tailed distributions. This indicates that a small fraction of households control a disproportionately large share of income and wealth [123, 124]. Fat tails reflect the slower decay of the upper end of the distribution compared to exponential or normal distributions, emphasizing the concentration of resources among a minority. 

Using data from the Survey of Consumer Finances, [125] analyzed household income, earnings, and wealth distributions in the U.S. from 1989 to 2013. Metrics such as the Gini coefficient, the coefficient of variation, and Lorenz curves were employed 

27 

to quantify and visualize inequality<sup>5</sup> . Similarly, [126] constructed micro-files of pretax and post-tax household income in the U.S. spanning 1913 to 2014, combining tax, survey, and national account data to align microeconomic observations with macroeconomic aggregates. [127] reviewed theoretical and empirical studies on household wealth distributions, exploring the economic mechanisms that drive skewness and fat tails in wealth distribution. 

These studies reveal the following key stylized facts about household income and wealth distributions: 

- Distribution of household income is right-skewed and fat-tailed. 

- Distribution of household wealth is right-skewed and fat-tailed. 

- Distribution of household wealth is more fat-tailed than income. 

- Post-tax income is more equally distributed than pre-tax income 

- Over time, the share of income held by the bottom 50% of households has declined relative to the entire economy. 

- Over time, the share of income held by the top 1% of households has increased relative to the entire economy. 

where bottom 50% of households corresponds to those households whose incomes are lower than or equal to the median income. Similarly, the top 1% of households corresponds to those households whose incomes lie in the 99 - 100 percentiles of the income distribution. 

#### **5.2.2 Firm Facts** 

Here, we investigate the distribution of firm-related variables such as firm size, production output, profits, productivity, and growth. The statistical properties of firm size and growth rate distributions have long been the focus of empirical research [128– 130]. A comprehensive survey of these stylized facts is provided by [107], which draws on data from U.S. manufacturing (Compustat data [131]) and Italian manufacturing (ISTAT data [132]). The key stylized facts identified in this literature include: 

1. Distribution of firm sizes within sectors is right skewed, with inter-sectoral differences in firm size distributions. 

2. Distribution of firm growth rates is fat-tailed. 

3. Decrease in variance in firm growth rates with increase in firm size. 

4. Widespread profitability differences across firms within each sector. 

5. Distribution of rate of change of firm profitabilities per sector is fat-tailed. 

6. Productivity heterogeneity across firms within each sector. 

where the following definitions hold: 

- Firm size is defined as the value added from sales (i.e., consumption spending from all households at this firm). 

> 5Lorenz curves provide a visual representation of inequality by plotting the cumulative share of income (or wealth) against the cumulative share of the population, sorted by income. The degree of divergence from the 45-degree line of perfect equality underscores the concentration of resources among a small fraction of households. 

28 

- Firm growth rate is defined as the change in the logarithm of firm size from step _t_ to step _t_ + 1. 

- Firm profitability is defined as the difference between value added and labor costs. 

- Firm productivity is defined as the value added per employee labor hour. 

### **5.3 Other Empirical Patterns.** 

##### **_Household Finance._** 

The field of household finance aims to understand the theory and empirics underlying household financial decisions [133]. A key focus is on how households make savings and consumption decisions, which influence their participation in liquid and illiquid asset markets, borrowing choices, engagement with insurance markets, and retirement savings strategies [134]. [135] provides a summary of empirical regularities in household financial behavior, particularly in the areas of consumption and savings, borrowing, asset allocation, and insurance. Drawing primarily on U.S. data, the analysis offers insights into how households manage their finances over their lifetimes. Notable regularities include: 

- Income-consumption co-movement, with consumption expenditures closely following expected and unexpected income changes. And, expenditures declining upon retirement. 

- Low accumulation of liquid wealth, such as monetary savings, over the life cycle. 

- High incidence of credit card borrowing. 

- High accumulation of illiquid wealth, such as housing, retirement accounts, and life insurance policies, over the life cycle. 

- Increased stock market participation with increase in household wealth. 

## **6 Experimental Results** 

We begin by detailing the training setup used to learn policies for all economic agents through independent multi-agent reinforcement learning within ABIDES-Economist. We train agent policies under two primary economic configurations. The first configuration is aimed at validating our simulated data’s ability to replicate key stylized facts outlined in Section 5. The second configuration is designed to showcase the utility of our simulation platform in crafting and comparing monetary (central bank) and fiscal (government) policies. 

For each configuration, we begin by confirming the improvement and approximate convergence of training rewards. We then evaluate the learned policies across various economic scenarios. These scenarios are crafted to either demonstrate the policies’ capability to generate simulated data that aligns with targeted stylized facts among those outlined in Section 5, or to illustrate the simulator’s effectiveness in developing superior monetary and fiscal policies compared to baseline rule-based approaches. 

For instance, we compare the performance of two central bank policies: the learned central bank policy, which was present during the training of other agents, and a baseline Taylor rule policy, a widely recognized benchmark in economic literature [136]. The Taylor rule policy is introduced as an unforeseen change, allowing us to 

29 

highlight the differences between the two monetary policies, while maintaining the learned policies for other agents unchanged. These experiments are run on an AWS EC2 instance (type c5.12xlarge) with 48 vCPUs and 96GB RAM. 

### **6.1 Learning Setup** 

To scale the training process, we employed a shared policy network for all agents of the same type, reducing the number of policies to be learned to four: one for each agent type in the system. The policy network for each type receives as input the observations detailed in Section 3, augmented with the heterogeneity parameters of agents as specified in Table 2. Specifically, the household policy network takes skills ( _ωij_ ) while the firm policy network takes production elasticity ( _αj_ ), as inputs in addition to the observations. Unless otherwise stated, agent parameters are as specified in Table 2. 

Each policy has a continuous observation space and a discrete action space. Table 3 provides an overview of the values and sources for the action spaces used in our simulator. For households and firms, action spaces comprise a uniform grid of values centered around the default values in **bold** , while adhering to any minimum value constraints. For the central bank, the action space spans a uniform grid of values corresponding to the range of US Federal Funds rates observed from 1950 to 2022. For the government, the action space includes tax rates applicable to each tax bracket in 2022. 

To facilitate learning, agent observations and rewards are normalized as described in Table 4. Policies were trained using the Proximal Policy Optimization (PPO) algorithm implemented in the RLlib package [101, 105]. Learning rates were determined via a grid search over _{_ 10<sup>_−_5</sup> _,_ 2 _×_ 10<sup>_−_5</sup> _,_ 5 _×_ 10<sup>_−_5</sup> _}_ for each agent type, selecting the first configuration that ensured consistent reward improvement across all agent types throughout training episodes. 

### **6.2 Verification of Stylized Facts** 

The selection of stylized facts to be verified must be tailored to the specific economic scenario under analysis, similar to the moments being targeted for model validation in the MSM approach. For instance, in a macroeconomic simulation investigating the effects of monetary policy on aggregate prices and production, macroeconomic facts from Section 5.1 are more relevant than microeconomic ones from Section 5.2. Even within macroeconomic facts, those related to business cycles may be more important than those concerning growth theory. Conversely, in scenarios aimed at assessing and designing fiscal policy and tax credit distribution for households, validating microeconomic facts - particularly those related to household income and wealth distributions - is crucial for accurately capturing household-level disparities before informing policy decisions. 

For the first economic configuration, we train our economic agents across diverse regimes, including variations in household skills, firm production parameters, and exogenous shocks, as detailed in Section 4. Consider an economy with 100 heterogeneously skilled households, 10 heterogeneous firms, a central bank and a government 

30 

|Agent|Action|Values|Source|
|---|---|---|---|
|Household _i_|_c_<sup>req</sup><br>_t,ij_|_{_0_,_6_,_**12**_,_18_,_24_}_|Per capita consumption<br>of 1lb of bread<br>per week [137].|
|Firm _j_|_wt,j_<br>_pt,j_|_{_7_._25_,_19_._65_,_**32.06**_,_44_._46_,_56_._87_}_<br>_{_188_,_255_,_**322**_,_389_,_456_}_|Minimum wage [138]<br>and average hourly earnings<br>in May 2022 [139].<br>Price of bread/lb in<br>May 2022 [140] multiplied<br>by 200 consumable goods.|
|Central Bank|_rt_|_{_0_._00250_,_0_._01625_,_0_._03_,_0_._04375_,_0_._05750_}_|Federal funds rate [141]|
|Government|_τt,_H<br>_τt,_F<br>_ft,i_|_{_0_._1000_,_0_._1675_,_0_._2350_,_0_._3025_,_0_._3700_}_<br>_{_0_._1000_,_0_._1675_,_0_._2350_,_0_._3025_,_0_._3700_}_<br>_{_1_,_2_,_3_,_4_,_5_}_ then, normalized by <sup>�</sup><br>_k _<sup>_ft,k_</sup>|Lowest to highest tax<br>brackets in 2022 [142]|



**Table 3** Agent action spaces in ABIDES-Economist. 

|Agent|Reward|Normalized reward|
|---|---|---|
|Household _i_|_u_<br>��<br>_j _<sup>_ct,ij,_ ¯</sup><sup>_n_ �</sup><br>_j _<sup>_et,ij, mt_+1</sup><sup>_,i_;</sup><sup>_γi, νi, µi_</sup><br>�|_u_<br>��<br>_j_<br>_ct,ij_<br>¯_ci _<sup>_,_ �</sup><br>_j _<sup>_et,ij,_</sup><br>_mt_+1_,i_<br>¯_n·_Avg_j{_¯<br>_wj}_<sup>;</sup><sup>_γi, νi, µi_</sup><br>�|
|Firm _j_|_pt,j_<br>�<br>_i _<sup>_ct,ij −wt,j_</sup><br>�<br>_i_ <sup>¯</sup><sup>_net,ij −χjpt,jYt_+1</sup><sup>_,j_</sup>|_pt,j_<br>�<br>_i _<sup>_ct,ij−wt,j_</sup><br>�<br>_i_ <sup>¯</sup><sup>_net,ij−χjpt,jYt_+1</sup><sup>_,j_</sup><br>¯_pj·_<sup>�</sup><br>_i_ <sup>¯</sup><sup>_ci_</sup>|
|Central Bank|_−_(_πt −π_<sup>_⋆_</sup>)<sup>2 </sup>+_λ_<br>��<br>_j _<sup>_yt,j_</sup><br>�2|_−_(_πt −π_<sup>_⋆_</sup>)<sup>2 </sup>+_λ_<br>��<br>_j _<sup>_yt,j_</sup><br>�<br>_j_ <sup>¯</sup><sup>_yj_</sup><br>�2<br>where ¯_yj_ =<br>�<br>¯_n_<br>�<br>_i_ <sup>1</sup><br>�<br>_j_ <sup>1</sup><br>�_αj_|
|Government|_θ_ <sup>�</sup><br>_i _<sup>_lt,iRt,i,_H + (1</sup><sup>_−θ_) �</sup><br>_i _<sup>_lt,iκt,i_</sup>|_θ_ <sup>�</sup><br>_i _<sup>_lt,iR_norm</sup><br>_t,i,_H<br>+(1_−θ_) <sup>�</sup><br>_i_<br>_lt,iκt,i_<br>_ξ·_Avg_j{_¯_pj}·_Avg_i{_¯_ci}_|



**Table 4** Normalization of agent rewards. The value of default labor hours _n_ ¯ is given in Table 2, while those for consumption _c_ ¯ _i_ , price _p_ ¯ _j_ and wage _w_ ¯ _j_ are given by the **bold faced** values in Table 3. 

as learning agents over a horizon of 10 years (40 quarters), with parameters as in Table 2. The households share a common policy network, and as do the firms. Learning rates are set at 2 _×_ 10<sup>_−_5</sup> for the household policy, 5 _×_ 10<sup>_−_5</sup> for the firm policy, 5 _×_ 10<sup>_−_5</sup> for the central bank policy, and 2 _×_ 10<sup>_−_5</sup> for the government policy. Figure 5 is a plot of discounted cumulative rewards during training for the four policies as a function of training episodes. We observe that rewards improve and stabilize beyond 5 _×_ 10<sup>4</sup> training episodes demonstrating training convergence. In particular, it takes _Nϵ_ = 42 _,_ 753 episodes (or 31 hours of training time) for the moving averages of agents’ rewards to reach and remain within 5% of the long-term rewards<sup>6</sup> . 

> 6Note here that we measure convergence by the moving average of rewards remaining within the _ϵ_ - percentage range around long-term rewards, rather than the rewards themselves, due to their higher 

31 



**Fig. 5** Discounted cumulative rewards per policy during training for the first economic configuration. Observe that moving averages of rewards converge within a 5%-range around long-term rewards after 42,753 episodes. 

To validate the ability of our simulator to replicate stylized facts, we apply these policies across three distinct economic test scenarios. Each scenario is designed to target a specific set of stylized facts among macroeconomic facts in section 5.1, household microeconomic facts in section 5.2.1, and firm microeconomic facts in section 5.2.2. 

#### **6.2.1 Verification of Macroeconomic Stylized Facts** 

In this macroeconomic scenario, we play out the learned policies in 100 test episodes in an economy with homogeneous households with skills _ωij ≡_ 1, homogeneous firms with production elasticity _αj ≡_ 0 _._ 9<sup>7</sup> and low exogenous shocks _σj ≡_ 0 _._ 01. We then extract the cyclical components of the resulting macroeconomic time series following the methodology described in Section 5.1.1. 

Figure 6 shows the cyclical component of key macroeconomic time series alongside that of real GDP, while Table 5 displays their cross-correlations with real GDP. The bottom subplot of Figure 6 examines the cyclical components of unemployment and inflation to assess the validity of the _Phillips’ Curve_ . Similarly, the last row of Table 5 quantifies the cross-correlation between the cyclical components of unemployment and inflation, further validating this relationship. We observe that the simulated data align with all the stylized business cycle facts listed in Section 5.1.1, except for those related to inflation and interest rates. 

We attribute the observed negative correlation between inflation and GDP to the absence of market-clearing assumptions in the goods market. Without market clearing, 

> variability, This increase in variability results from (1) the presence of numerous households and firms with heterogeneous parameters, and (2) the higher standard deviation of the exogenous production shock _σj_ . That is to say that the training time for this configuration with 100 learning households, 10 learning firms, learning central bank and learning government is significantly higher than that observed in section 4.3.4 when using the same instance type. 

> 7We choose _αj_ so that the production of each firm with full employment is approximately equal to the maximum consumption across households. 

32 



**Fig. 6** Cyclical components of macroeconomic variables alongside that of real GDP, unless otherwise stated. Observe that our simulated data exhibits most empirical relationships observed in real macroeconomic data related to business cycles. 

33 

|Variable|Cross Correlation|
|---|---|
|Total employment|0.158642|
|Unemployment rate|-0.158289|
|Consumption expenditure|0.129125|
|Total labor hours|0.158642|
|Labor productivity|0.993994|
|Prices (Consumer Price Index)|-0.050842|
|Nominal wage|-0.181873|
|Real wage|-0.043230|
|Inflation|-0.564621|
|Interest rate|-0.014768|
|Phillips’ Curve (Unemployment, Inflation)|-0.031113|



**Table 5** Cross correlations between cyclical components of macroeconomic variables with that of real GDP, unless otherwise stated. Observe that our simulated data satisfies most macroeconomic stylized facts related to business cycles. 







**Fig. 7** Validation of macroeconomic facts unrelated to business cycles. 

the mechanism driving this negative relationship is as follows: Higher GDP is associated with increased production, leading to a buildup of firm inventory. To mitigate inventory holding risks, firms lower prices, resulting in a negative correlation between inflation and GDP. On the other hand, under market-clearing conditions, higher GDP associated with higher production is matched by increased consumption. In this scenario, stronger demand drives prices upward, leading to a positive relationship between inflation and GDP. 

34 

Among the macroeconomic stylized facts unrelated to business cycles listed in Section 5.1.2, _Kaldor’s Facts_ do not apply to our economic model as we do not explicitly model firm capital and investment. Nonetheless, Figure 7 illustrates relationships relevant to the _Phillips’ Curve_ , _Okun’s Law_ , and the _Beveridge Curve_ . Our findings are consistent with those observed in empirical literature. Specifically: 

- _Phillips’ Curve_ : We observe no stable relationship between long-run unemployment and nominal wage changes or inflation, aligning with prior empirical findings. 

- _Okun’s Law_ : We observe a negative relationship between changes in unemployment and real GDP, indicating that reductions in unemployment correspond with increases in GDP, thereby satisfying _Okun’s Law_ . 

- _Beveridge Curve_ : We observe an inverse relationship between the job vacancy rate and the unemployment rate, confirming that high unemployment levels are associated with low job vacancy rates. 

Thus, we successfully validate a large set of targeted macroeconomic stylized facts, including those related and unrelated to business cycles. 

#### **6.2.2 Verification of Microeconomic Stylized Facts related to Households** 

In this microeconomic scenario, we play out the learned policies in 10 test episodes in an economy with heterogeneous households with skills _ω_ : _j ∼N_ (0 _._ 8 _,_ 0 _._ 3), heterogeneous firms with production elasticities linearly spaced in the range _αj ∈_ [0 _._ 9 _,_ 1 _._ 0], and exogenous shocks as seen during training _σj ≡_ 0 _._ 1. The objective is to validate our simulated data on the stylized facts outlined in Section 5.2.1, particularly the emergence of a right-skewed distribution for household income and wealth. Several models have been proposed in the literature to induce this income distribution using heterogeneities of productivity and talent [127]. To ensure heterogeneity in income and employment outcomes, we set household skill and firm production parameters based on the following considerations: 

1. Since all households with skill _ωij ≥_ 1 are treated equally when firms make hiring decisions, generating income heterogeneity among employed households requires wage differentiation that results from firm heterogeneity. 

2. To allow for unemployment and zero-income households in the simulation, we set higher _αj_ values and ensure that a significant fraction of households have skills below the minimum employment threshold _ω_ min = 1 (see Section 3.2). 

Figure 8 presents the distribution across households of average household income and final savings over the simulation horizon, accompanied by skewness and excess kurtosis metrics to quantify the asymmetry and fat-tailed nature of the distributions. Both income and savings exhibit right-skewed distributions with similar levels of skewness. However, the distributions do not exhibit fat tails, as indicated by the low kurtosis values. This is due to the limited number of discrete wage levels in our simulator, which constrains the range of possible income values. Additionally, since income tax rates are constant across income brackets in our setup, the post-tax income distribution mirrors the pre-tax income distribution. 

35 





**Fig. 8** Distribution of average income across households (left) and final savings across households (right). Observe that income and savings are both right-skewed. 





**Fig. 9** Visualization of household income inequality via the Lorenz curve (left) and temporal progression of income shares of the bottom 50% and top 1% of households (right). Observe the deviation of the Lorenz curve from the 45<sup>_◦_</sup> line with positive a Gini index. Also, observe the temporal decline in the income share of the bottom 50% of households in the economy. 

Figure 9 further illustrates income inequality. The left subplot shows the Lorenz curve for household income, which visualizes income inequality by plotting the cumulative share of income against the cumulative share of the population, sorted by income. The extent of deviation from the 45<sup>_◦_</sup> line of perfect equality highlights the concentration of resources among a small fraction of households. As observed in [125], our results show a significant deviation from perfect equality, with a large portion of the population holding a disproportionately small share of total income. This is also evident from the positive Gini index and Coefficient of variation computed on the household incomes. The right subplot of Figure 9 shows the temporal evolution of the shares of income held by the bottom 50% and top 1% of households. The share of income held by the bottom 50% declines over time, while the share of the top 1% initially increases slightly before stabilizing. 

Overall, our simulated data successfully replicates the targeted microeconomic stylized facts related to households, validating the emergence of right-skewed income and wealth distributions, persistent income inequality, and the shifting of income shares between different segments of the population. 

#### **6.2.3 Verification of Microeconomic Stylized Facts related to Firms** 

In this microeconomic scenario, we play out the learned policies in 10 test episodes in an economy with homogeneous households with skills _ωij ≡_ 1, heterogeneous firms with production elasticities drawn from a log-normal distribution fit to U.S. industrial 

36 

data and scaled to lie within the range _αj ∈_ [0 _._ 6 _,_ 1 _._ 0]<sup>8</sup> , and low exogenous shocks _σj ≡_ 0 _._ 01. The objective is to validate our simulated data on the stylized facts outlined in Section 5.2.2, those concerning the following firm-level variables: 

- Firm size: Measured as the total value of consumed goods _pt,j_ � _i_<sup>_ct,ij_.</sup> 

- Growth rate: Defined as the change in log-firm size. 

- Profitability: Measured as the difference between the total value of consumed goods and labor costs _pt,j_ � _i_<sup>_ct,ij−wt,j_</sup> � _i_<sup>_ne_¯</sup><sup>_t,ij_.</sup> 

- • Productivity: Defined as the value of consumed goods per hour of employee labor _<u>pt,j</u>_ <u>�</u> _<u>i</u>_<sup>_ct,ij_</sup> 

   - _i_<sup>_ne_¯</sup><sup>_t,ij_.</sup> 

Due to computational constraints, our experimental setup includes only 10 firms, limiting our ability to match empirical firm distributions exactly. Instead, we analyze histograms and compute skewness and excess kurtosis metrics over samples to capture distributional asymmetry and the presence of fat tails. 

Figure 10 presents histograms of the aforementioned variables, averaged per firm over the simulation horizon, along with the average rate of change of profitability. Figure 10 also displays the relationship between variance in firm growth rates across time steps and firm size. Here, we observe heterogeneity across firms in all measured variables. The histogram of firm sizes exhibits positive skewness, consistent with empirical findings. The firm growth rate histogram shows positive excess kurtosis, indicating fatter tails than a normal distribution. Likewise, the rate of change of profitability is also fat-tailed. Importantly, despite the small number of firms, we observe an inverse relationship between firm size and the variance of growth rates, as shown in the bottom-right subplot of Figure 10. 

Overall, our simulated data successfully replicates the targeted microeconomic stylized facts related to firm heterogeneity, though the small sample size of firms presents some limitations in matching real-world distributions exactly. 

### **6.3 Utility for Monetary and Fiscal Policy Design** 

We now demonstrate the efficacy of our simulation platform in aiding policy design and analysis for regulatory bodies, such as the central bank and government. Specifically, we aim to illustrate the impact of different regulatory policies on achieving policy objectives in the presence of heterogeneous and adaptive households and firms. For comparison, we utilize two central bank policies: the learned policy which was seen during the training of other agents, and the widely adopted rule-based Taylor Rule policy [86], which serves as an unforeseen change. Likewise, we compare the learned government policy with a uniform tax rule on fiscal policy efficacy. These baselines are introduced as unforeseen changes to regulatory policy, as they were not encountered by other agents during their learning process. 

This second economic configuration mirrors the first in capturing diverse regimes via variations in household skills, firm production parameters, and exogenous shocks, as described in Section 6.2. However, it introduces a key modification to the government reward parameter, specifically setting _θ_ = 0 _._ 2 to place greater emphasis on tax 

> 8The scaling ensures that each firm produces at least one unit of goods per consumer household under full employment. For additional details on parameter fitting to real U.S. data, refer to the appendix. 

37 













**Fig. 10** Histograms of key firm-related variables with skewness and excess kurtosis metrics, alongside the inverse relationship between variance in growth rate and firm size. Observe the heterogeneity across all variables, right-skewed firm size distribution, and fat-tailed distributions for growth rate and profitability rates of change. 

credit redistribution over resulting household utility, as outlined in equation (12). The choice of a different _θ_ value, where _θ <_ 1, is intentional as it aims to enhance the redistribution of tax credits towards reducing savings inequality among households. This adjustment influences our simulated data’s ability to generate microeconomic patterns related to household inequality, as the government actively seeks to minimize discrepancies, prompting households to adapt accordingly. To address these dynamics, we explore two distinct economic configurations: (1) for the validation of stylized facts, as discussed in the previous subsection, and (2) for demonstrating the simulator’s utility in policy design, as covered in this subsection. 

For the second economic configuration, consider an economy with 100 heterogeneously skilled households, 10 heterogeneous firms, a central bank and a government as learning agents over a horizon of 10 years (40 quarters), with parameters as in Table 2 except with _θ_ = 0 _._ 2. The households share a common policy network, and as do the firms. Learning rates are set at 2 _×_ 10<sup>_−_5</sup> for the household policy, 5 _×_ 10<sup>_−_5</sup> for the firm policy, 5 _×_ 10<sup>_−_5</sup> for the central bank policy, and 2 _×_ 10<sup>_−_5</sup> for the government policy. Figure 11 is a plot of discounted cumulative rewards during training for the four policies as a function of training episodes. We observe that rewards improve and stabilize beyond 10<sup>5</sup> training episodes demonstrating training convergence. In particular, it takes _Nϵ_ = 105 _,_ 000 episodes (or 76 hours of training time) for the moving averages of agents’ rewards to reach and remain within 5% of the long-term rewards. 

38 



**Fig. 11** Discounted cumulative rewards per policy during training for the second economic configuration. Observe that moving averages of rewards converge within a 5%-range around long-term rewards after 105,000 episodes. 

#### **6.3.1 Utility for Monetary Policy Design** 

In this macroeconomic scenario, we play out the learned policies in 100 test episodes, with a focus on central bank decision-making. The economy consists of homogeneous households with skills _ωij ≡_ 1, heterogeneous firms with production elasticities linearly spaced in the range _αj ∈_ [0 _._ 05 _,_ 1 _._ 00], and low exogenous shocks _σj ≡_ 0 _._ 01. Subsequently, to establish a baseline for comparison and highlight the benefits of learning a central bank policy, we substitute the learned central bank policy with a non-inertial Taylor rule for setting interest rates, as described in [86]: 



where _r_<sup>_⋆_</sup> = 2% represents the equilibrium interest rate, _πt_ is the current inflation rate, _π_<sup>_⋆_</sup> = 2% is the target inflation rate, and _yt − yt_<sup>_⋆_denotestheoutputgapbetween</sup> current production output _yt_ =<sup>�</sup> _j_<sup>_pt,jyt,j_andanestimateofpotentialoutput</sup><sup>_y_</sup> _t_<sup>_⋆_</sup> computed using a linear fit to past outputs. We evaluate the performance of the learned central bank policy against the Taylor rule under identical conditions, where all other economic agents continue to use their learned policies. The discounted sum of the central bank’s rewards as defined in equation (10) capture the central bank’s utility from minimizing deviations from target inflation, and maximizing GDP. This serves as the performance metric for comparing monetary policies. 

Figure 12 presents the distribution of central bank utility and other monetary observables across test episodes. The results for the Taylor rule are shown in blue, while those for the learned policy are shown in orange. The legends display the average value and standard deviation (in brackets) across test episodes. We observe that the central bank achieves slightly higher utility with lower variance under the learned policy compared to the Taylor rule. In addition, while the Taylor rule utilizes nearly all interest rate options, the learned policy typically employs at most two rate options 

39 



**Fig. 12** Distribution of Central Bank utility from inflation targeting and GDP, along with other monetary observables for the Taylor rule (blue) and learned policy (orange) in a regular economy with low production shocks. The learned policy achieves higher utility with lower variance. 

on average<sup>9</sup> . Furthermore, although both policies achieve similar inflation targeting, the learned policy is more effective in promoting production. 

To further assess the robustness of the learned policy, we compare its performance with that of the Taylor rule in a volatile economic scenario with high exogenous shocks to the firms. In particular, the mean of the firm shock process is linearly spaced in the range _ε_ ¯ _j ∈_ [0 _._ 10 _,_ 0 _._ 00], with the standard deviation linearly spaced in the range _σj ∈_ [0 _._ 20 _,_ 0 _._ 10]. This scenario represents an economic environment where the firm with the lowest production elasticity _α_ 1 = 0 _._ 05 experience positive production shocks with high mean and variance (¯ _ε_ 1 _, σ_ 1) = (0 _._ 10 _,_ 0 _._ 20). And, the firm with the highest production elasticity _α_ 1 = 1 _._ 0 experiences low production shocks as before, with low mean and variance (¯ _ε_ 1 _, σ_ 1) = (0 _._ 00 _,_ 0 _._ 10). 

Figure 13 presents the distribution of central bank utility and other monetary observables across test episodes in this economic scenario characterized by high variability due to heterogeneity in firm productions and exogenous shocks. We observe that the learned policy significantly outperforms the Taylor rule in achieving higher utility for the central bank in inflation targeting and GDP promotion, while also maintaining lower variance across episodes. Notably, the variance in central bank utility for the learned policy remains similar to the previous low-shock scenario, whereas the variance for the Taylor rule is substantially higher than before. As previously noted, while both policies achieve similar inflation targeting objectives, the learned policy is more effective in promoting production under such shock scenarios compared to the Taylor rule. This highlights the effectiveness of the learned central bank policy in meeting inflation and production targets through strategic interest rate setting even in volatile economic scenarios. 

> 9This comparison is based on the average interest rate over the horizon across test episodes, so variability over the horizon is still present, as expected. 

40 



**Fig. 13** Distribution of Central Bank utility from inflation targeting and GDP, along with other monetary observables for the Taylor rule (blue) and learned policy (orange) in a volatile economy with high production shocks. The learned policy significantly outperforms the Taylor rule, and has lower variance that is similar to the scenario without shocks. 

#### **6.3.2 Utility for Fiscal Policy Design** 

We consider a macroeconomic scenario akin to the one above for monetary policy testing, but now with a focus on government decision-making, particularly concerning heterogeneous households. We play out learned policies in 100 test episodes mirroring regimes seen during training. The economy consists of heterogeneous households with skills _ωij ∼N_ (1 _._ 0 _,_ 0 _._ 3), heterogeneous firms with production elasticities linearly spaced in the range _αj ∈_ [0 _._ 05 _,_ 1 _._ 00], and low exogenous shocks _σj ≡_ 0 _._ 01. Subsequently, to establish a baseline for comparison and highlight the benefits of learning a government policy for tax redistribution, we substitute the learned government policy with a fixed median tax rate and a uniform tax redistribution policy: 



where 0 _._ 2350 is the tax rate corresponding to the mid tax bracket in Table 3, and _n_ denotes the number of households. We evaluate the performance of the learned government policy against this uniform tax rate rule under identical conditions, where all other economic agents continue to use their learned policies. The discounted sum of the government’s reward as defined in equation (12), reflects its utility from household social welfare as a weighted sum of household utilities and tax credits. This serves as the performance metric for comparing fiscal policies. Note that we apply inverseincome weights for households, as detailed in Table 2. 

Figure 14 displays the distribution of social welfare, alongside the tax rates for households and firms, taxes collected from them, and the tax credits provided to households across test episodes. Results for the uniform tax rule are shown in blue, while those for the learned policy are shown in orange. The learned tax policy achieves 

41 



**Fig. 14** Distribution of household social welfare and tax related observables for the uniform tax policy (blue) and learned policy (orange) in a regular economy with low production shocks. The learned policy achieves higher social welfare via greater tax collection and redistribution than a rulebased uniform tax policy. 

higher social welfare compared to the uniform tax policy. It sets higher tax rates on average and collects larger amounts of taxes from both households and firms, which facilitates the redistribution of larger tax credits to households. This highlights the effectiveness of the learned government policy in enhancing social welfare through strategic tax credit distribution. 

Similar to our approach with monetary policy, we further assess the robustness of the learned tax policy in a volatile economic scenario characterized by high exogenous shocks to firms. Specifically, the mean of the firm shock process is linearly spaced in the range _ε_ ¯ _j ∈_ [0 _._ 10 _,_ 0 _._ 00], with the standard deviation linearly spaced in the range _σj ∈_ [0 _._ 20 _,_ 0 _._ 10]. This scenario features high economic variability due to heterogeneity in firm productions and exogenous shocks, alongside the heterogeneity in household skills. 

Figure 15 presents the corresponding distribution of social welfare and tax-related observables across the test episodes. We observe that both fiscal policies achieve slightly higher social welfare due to increased tax collection from firms, even with unchanged tax rates. This increase is attributed to higher firm profits resulting from greater production due to the positive shocks. Notably, the percentage increase in social welfare is larger for the learned policy compared to the previous low-shock scenario. The increased variability of shocks is reflected in the higher variance of social welfare for both fiscal policies compared to the low-shock scenario. Nonetheless, the percentage increase in the variance of social welfare is lower for the learned policy than for the rule-based policy. Importantly, the learned policy continues to outperform the rule-based uniform tax policy even in this volatile high-shock economy. 

42 



**Fig. 15** Distribution of household social welfare and tax related observables for the uniform tax policy (blue) and learned policy (orange) in a volatile economy with high production shocks. The learned policy achieves higher social welfare via greater tax collection and redistribution. While both fiscal policies exhibit an increase in social welfare variability due to shock volatility, the variance increase is smaller for the learned policy. 

## **7 Conclusion** 

We introduce ABIDES-Economist, a multi-agent simulation platform designed for economic systems featuring heterogeneous households, firms, a central bank, and a government. Our simulator is configurable for both microeconomic and macroeconomic granularities, offering versatility for simulating diverse economic scenarios. It enables economic agents to utilize reinforcement learning algorithms to develop strategies that maximize their objectives, even in the presence of shocks, agent heterogeneity, and adaptation. 

A key contribution of our work is toward calibration and validation of economic agent-based simulators with learning agents. We provide a comprehensive survey of macroeconomic and microeconomic stylized facts for households and firms. By grounding our agent parameters in real U.S. economic data where available, we validate our platform’s ability to replicate a wide range of targeted micro- and macroeconomic facts, even when all agents use reinforcement learning to determine their behavioral policies. Upon validation, we demonstrate the platform’s utility for economic policymaking, particularly in scenarios where agent heterogeneity and economic shocks are significant. We compare policies developed within our platform to standard rule-based approaches from the literature, illustrating the superior performance of our policies. This paves the way for studying and designing economic policies within a validated and controlled framework before real-world implementation. 

While we demonstrate the platform’s utility for economic policy analysis and design, we also recognize the challenges of scalability and learning instability inherent to multi-agent reinforcement learning. Our experiments showcase the capability to simultaneously learn policies for 100 households, 10 firms, 1 central bank, and 1 government. We achieve this scaling by sharing a single policy network across all agents of the 

43 

same type to accelerate learning through shared experiences. Additionally, we implement realistic agent communication, where agents exchange shareable information, reducing partial observability challenges associated with multi-agent reinforcement learning. 

Lastly, the quality of the equilibrium to which the learned policies converge remains uncertain. We propose incorporating game-theoretic tools suited for agentbased models, such as empirical game-theoretic analysis, to compare and identify different equilibria for multi-agent systems with learning agents [143, 144]. Although this approach incurs additional computational costs due to simulating utilities for an exponentially increasing set of joint policies as the agent/policy count grows, it can mitigate instabilities in multi-agent reinforcement learning by allowing agents to iterate over unilaterally improving their policies. 

44 

**Acknowledgements.** The authors would like to thank Dr. Jesse Perla for his insightful comments on existing literature from economics and macrofinance. This paper was prepared for informational purposes in part by the Artificial Intelligence Research group of JPMorgan Chase & Co. and its affiliates (“JP Morgan”) and is not a product of the Research Department of JP Morgan. JP Morgan makes no representation and warranty whatsoever and disclaims all liability, for the completeness, accuracy, or reliability of the information contained herein. This document is not intended as investment research or investment advice, or a recommendation, offer or solicitation for the purchase or sale of any security, financial instrument, financial product, or service, or to be used in any way for evaluating the merits of participating in any transaction, and shall not constitute a solicitation under any jurisdiction or to any person, if such solicitation under such jurisdiction or to such person would be unlawful. 

## **Appendix A Estimating Firm Productivity from Labor using Real Data** 

We obtained annual employment and output data for all industry sectors within the United States from the Bureau of Labor Statistics [95]. This data includes aggregated variables related to employment and productivity for firms across 167 sectors, which are grouped into 22 industry groups. For example, the group _‘Agriculture, Forestry, Fishing, and Hunting’_ encompasses data from six sectors, including crop production; animal production and aquaculture; forestry; logging; fishing, hunting and trapping; and support activities for agriculture and forestry. We filtered 20 out of the 22 groups, excluding the special industries and value-added industries groups due to incomplete data. As a result, we have annual data for 163 industry sectors within these 20 groups. Specifically, we utilize annual domestic industry output in millions of current dollars from 1997 to 2023 and annual total labor hours of all employed persons in millions from 2014 to 2023. We then aggregate labor hours and employment by group, calculating total labor hours and total employment for each of the 20 industry groups over ten years. 

To estimate the production elasticity for labor _αj_ for each industry group _j_ , we fit a linear regression model to the log-transformed labor hours and output data: 



We scale the resulting _αj_ values by the largest elasticity and exclude the two groups with negative elasticities, as we require all production elasticities to lie within [0 _,_ 1]. This yields the production elasticities fitted to real U.S. data, as shown in Figure A1. 

For verifying microeconomic stylized facts related to firms in Section 5.2.2, we first scale this set of elasticities to lie within [0 _._ 6 _,_ 1 _._ 0]. Next, we determine the best-fit distribution for the resulting histogram using the distfit package [145], identifying the lognormal distribution as the best fit, as shown in Figure A2. 

45 



**Fig. A1** Histogram of production elasticities for labor, fit to employment and output data for 18 industry groups in the U.S. 



**Fig. A2** Histogram of fitted production elasticities for labor scaled to lie within [0 _._ 6 _,_ 1 _._ 0], used for verifying microeconomic stylized facts related to firms. 

## **References** 

- [1] Macal, C.M., North, M.J.: Tutorial on agent-based modeling and simulation. In: Proceedings of the Winter Simulation Conference (2005) 

- [2] Lavin, A., Krakauer, D., Zenil, H., Gottschlich, J., Mattson, T., Brehmer, J., Anandkumar, A., Choudry, S., Rocki, K., Baydin, A.G., et al.: Simulation intelligence: Towards a new generation of scientific methods. arXiv preprint arXiv:2112.03235 (2021) 

- [3] Vorotnikov, S., Ermishin, K., Nazarova, A., Yuschenko, A.: Multi-agent robotic systems in collaborative robotics. In: Interactive Collaborative Robotics: Third International Conference, pp. 270–279 (2018) 

- [4] Byrd, D., Hybinette, M., Balch, T.H.: Abides: Towards high-fidelity market simulation for ai research. arXiv preprint arXiv:1904.12066 (2019) 

- [5] Adler, J.L., Satapathy, G., Manikonda, V., Bowles, B., Blue, V.J.: A multi-agent approach to cooperative traffic management and route guidance. Transportation Research Part B: Methodological **39** (4), 297–318 (2005) 

- [6] Gatti, M., Cavalin, P., Neto, S.B., Pinhanez, C., Santos, C., Gribel, D., Appel, A.P.: Large-scale multi-agent-based modeling and simulation of microbloggingbased online social network. In: Multi-Agent-Based Simulation XIV: International Workshop, pp. 17–33 (2014) 

46 

- [7] Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S.: Generative agents: Interactive simulacra of human behavior. arXiv preprint arXiv:2304.03442 (2023) 

- [8] Farmer, J.D., Foley, D.: The economy needs agent-based modelling. Nature **460** (7256), 685–686 (2009) 

- [9] Srbljinovi´c, A., Skunca,<sup>ˇ</sup> O.: An introduction to agent based modelling and simulation of social processes. Interdisciplinary Description of Complex Systems **1** (1-2), 1–8 (2003) 

- [10] Tesfatsion, L., Judd, K.L.: Handbook of Computational Economics: Agent-based Computational Economics. Elsevier, The Netherlands (2006) 

- [11] Hamill, L., Gilbert, N.: Agent-based Modelling in Economics. John Wiley & Sons, United Kingdom (2015) 

- [12] Arthur, W.B.: Foundations of complexity economics. Nature Reviews Physics **3** (2), 136–145 (2021) 

- [13] Dorri, A., Kanhere, S.S., Jurdak, R.: Multi-agent systems: A survey. Ieee Access **6** , 28573–28593 (2018) 

- [14] Kaelbling, L.P., Littman, M.L., Moore, A.W.: Reinforcement learning: A survey. Journal of Artificial Intelligence Research **4** , 237–285 (1996) 

- [15] Busoniu, L., Babuska, R., De Schutter, B.: A comprehensive survey of multiagent reinforcement learning. IEEE Transactions on Systems, Man, and Cybernetics **38** (2), 156–172 (2008) 

- [16] Littman, M.L.: Markov games as a framework for multi-agent reinforcement learning. In: Machine Learning Proceedings, pp. 157–163 (1994) 

- [17] Hu, J., Wellman, M.P.: Multiagent reinforcement learning: Theoretical framework and an algorithm. In: Proceedings of the Fifteenth International Conference on Machine Learning, pp. 242–250 (1998) 

- [18] Fudenberg, D., Levine, D.K.: The Theory of Learning in Games vol. 2. MIT press, Massachusetts (1998) 

- [19] Bowling, M., Veloso, M.: An Analysis of Stochastic Game Theory for Multiagent Reinforcement Learning. Citeseer, Pennsylvania (2000) 

- [20] Pakes, A., McGuire, P.: Stochastic algorithms, symmetric markov perfect equilibrium, and the ‘curse’of dimensionality. Econometrica **69** (5), 1261–1281 (2001) 

- [21] Moll, B.: The trouble with rational expectations in heterogeneous agent models: 

47 

A challenge for macroeconomics. London School of Economics, mimeo, available at https://benjaminmoll. com (2024) 

- [22] Zheng, S., Trott, A., Srinivasa, S., Parkes, D.C., Socher, R.: The AI economist: Taxation policy design via two-level deep multiagent reinforcement learning. Science Advances **8** (18), 2607 (2022) https://doi.org/10.1126/sciadv.abk2607 

- [23] Hill, E., Bardoscia, M., Turrell, A.: Solving heterogeneous general equilibrium economic models with deep reinforcement learning. arXiv preprint arXiv:2103.16977 (2021) 

- [24] Chen, M., Joseph, A., Kumhof, M., Pan, X., Shi, R., Zhou, X.: Deep reinforcement learning in a monetary model. arXiv preprint arXiv:2104.09368 (2021) 

- [25] Hinterlang, N., T¨anzer, A.: Optimal monetary policy using reinforcement learning. Technical report, Deutsche Bundesbank Discussion Paper (2021) 

- [26] Brusatin, S., Padoan, T., Coletta, A., Delli Gatti, D., Glielmo, A.: Simulating the economic impact of rationality through reinforcement learning and agentbased modelling. In: Proceedings of the 5th ACM International Conference on AI in Finance, pp. 159–167 (2024) 

- [27] Curry, M., Trott, A., Phade, S., Bai, Y., Zheng, S., et al.: Analyzing microfounded general equilibrium models with many agents using deep reinforcement learning. Technical report (2022) 

- [28] Mi, Q., Xia, S., Song, Y., Zhang, H., Zhu, S., Wang, J.: Taxai: A dynamic economic simulator and benchmark for multi-agent reinforcement learning. arXiv preprint arXiv:2309.16307 (2023) 

- [29] Fagiolo, G., Guerini, M., Lamperti, F., Moneta, A., Roventini, A.: Validation of agent-based models in economics and finance. Computer simulation validation: fundamental concepts, methodological frameworks, and philosophical perspectives, 763–787 (2019) 

- [30] Werker, C., Brenner, T.: Empirical calibration of simulation models (2004) 

- [31] Windrum, P., Fagiolo, G., Moneta, A.: Empirical validation of agent-based models: Alternatives and prospects. Journal of Artificial Societies and Social Simulation **10** (2), 8 (2007) 

- [32] Raberto, M., Cincotti, S., Focardi, S.M., Marchesi, M.: Agent-based simulation of a financial market. Physica A: Statistical Mechanics and its Applications **299** (1-2), 319–327 (2001) 

- [33] (FAIR)†, M.F.A.R.D.T., Bakhtin, A., Brown, N., Dinan, E., Farina, G., Flaherty, 

48 

C., Fried, D., Goff, A., Gray, J., Hu, H., _et al._ : Human-level play in the game of diplomacy by combining language models with strategic reasoning. Science **378** (6624), 1067–1074 (2022) 

- [34] Bonabeau, E.: Agent-based modeling: Methods and techniques for simulating human systems. Proceedings of the national academy of sciences **99** (suppl ~~3~~ ), 7280–7287 (2002) 

- [35] Palmer, R.G., Arthur, W.B., Holland, J.H., LeBaron, B., Tayler, P.: Artificial economic life: a simple model of a stockmarket. Physica D: Nonlinear Phenomena **75** (1-3), 264–274 (1994) 

- [36] LeBaron, B.: Agent-based computational finance: Suggested readings and early research. Journal of Economic Dynamics and Control **24** (5-7), 679–702 (2000) 

- [37] Byrd, D., Hybinette, M., Balch, T.H.: Abides: Towards high-fidelity multi-agent market simulation. In: Proceedings of the 2020 ACM SIGSIM Conference on Principles of Advanced Discrete Simulation, pp. 11–22 (2020) 

- [38] Vyetrenko, S., Byrd, D., Petosa, N., Mahfouz, M., Dervovic, D., Veloso, M., Balch, T.: Get real: Realism metrics for robust limit order book market simulations. In: Proceedings of the First ACM International Conference on AI in Finance, pp. 1–8 (2020) 

- [39] Wah, E., Wellman, M.P.: Latency arbitrage, market fragmentation, and efficiency: a two-market model. In: Proceedings of the Fourteenth ACM Conference on Electronic Commerce, pp. 855–872 (2013) 

- [40] Wang, X., Wellman, M.P.: Spoofing the limit order book: An agent-based model. In: Workshops at the Thirty-First AAAI Conference on Artificial Intelligence (2017) 

- [41] Wah, E., Wright, M., Wellman, M.P.: Welfare effects of market making in continuous double auctions. Journal of Artificial Intelligence Research **59** , 613–650 (2017) 

- [42] Paddrik, M., Hayes, R., Todd, A., Yang, S., Beling, P., Scherer, W.: An agent based model of the E-Mini S&P 500 applied to Flash Crash analysis. In: 2012 IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr), pp. 1–8 (2012). IEEE 

- [43] Zhu, H., Vyetrenko, S., Dwarakanath, K., Balch, T., Grundl, S., Byrd, D.: Once burned, twice shy? the effect of stock market bubbles on traders that learn by experience. In: 2023 Winter Simulation Conference (WSC), pp. 291–302 (2023). IEEE 

- [44] Dwarakanath, K., Vyetrenko, S., Balch, T.: Equitable marketplace mechanism 

49 

design. In: Proceedings of the Third ACM International Conference on AI in Finance, pp. 232–239 (2022) 

- [45] Dwarakanath, K., Vyetrenko, S., Balch, T., Oyebode, T.: Transparency as delayed observability in multi-agent systems. In: 2023 Winter Simulation Conference (WSC), pp. 279–290 (2023). IEEE 

- [46] Ardon, L., Vann, J., Garg, D., Spooner, T., Ganesh, S.: Phantom–an rl-driven framework for agent-based modeling of complex economic systems and markets. arXiv preprint arXiv:2210.06012 (2022) 

- [47] Vadori, N., Ardon, L., Ganesh, S., Spooner, T., Amrouni, S., Vann, J., Xu, M., Zheng, Z., Balch, T., Veloso, M.: Towards multi-agent reinforcement learningdriven over-the-counter market simulations. Mathematical Finance **34** (2), 262– 347 (2024) 

- [48] Hugonnier, J., Lester, B., Weill, P.-O.: The Economics of Over-the-Counter Markets: A Toolkit for the Analysis of Decentralized Exchange. Princeton University Press, ??? (2025) 

- [49] Spooner, T., Fearnley, J., Savani, R., Koukorinis, A.: Market making via reinforcement learning. In: Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems, pp. 434–442 (2018) 

- [50] Ganesh, S., Vadori, N., Xu, M., Zheng, H., Reddy, P., Veloso, M.: Reinforcement learning for market making in a multi-agent dealer market. arXiv preprint arXiv:1911.05892 (2019) 

- [51] Dwarakanath, K., Vyetrenko, S.S., Balch, T.: Profit equitably: an investigation of market maker’s impact on equitable outcomes. In: Proceedings of the Second ACM International Conference on AI in Finance, pp. 1–8 (2021) 

- [52] Amrouni, S., Moulin, A., Vann, J., Vyetrenko, S., Balch, T., Veloso, M.: Abidesgym: gym environments for multi-agent discrete event simulation and application to financial markets. In: Proceedings of the Second ACM International Conference on AI in Finance, pp. 1–9 (2021) 

- [53] Mascioli, C., Gu, A., Wang, Y., Chakraborty, M., Wellman, M.: A financial market simulation environment for trading agents using deep reinforcement learning. In: Proceedings of the 5th ACM International Conference on AI in Finance, pp. 117–125 (2024) 

- [54] Darley, V., Outkin, A.V.: A NASDAQ Market Simulation: Insights on a Major Market from the Science of Complex Adaptive Systems. WORLD SCIENTIFIC, https://www.worldscientific.com/doi/pdf/10.1142/6217 (2007) 

- [55] Del Negro, M., Schorfheide, F.: Dsge model-based forecasting. In: Handbook of 

50 

Economic Forecasting vol. 2, pp. 57–140. Elsevier, ??? (2013) 

- [56] Kydland, F.E., Prescott, E.C.: Time to build and aggregate fluctuations. Econometrica: Journal of the Econometric Society, 1345–1370 (1982) 

- [57] Krusell, P., Smith, A.A. Jr: Income and wealth heterogeneity in the macroeconomy. Journal of political Economy **106** (5), 867–896 (1998) 

- [58] Christiano, L.J., Eichenbaum, M., Evans, C.L.: Nominal rigidities and the dynamic effects of a shock to monetary policy. Journal of political Economy **113** (1), 1–45 (2005) 

- [59] Woodford, M.: Convergence in macroeconomics: elements of the new synthesis. American economic journal **1** (1), 267–279 (2009) 

- [60] Smets, F., Wouters, R.: Shocks and frictions in us business cycles: A bayesian dsge approach. American economic review **97** (3), 586–606 (2007) 

- [61] Kaplan, G., Moll, B., Violante, G.L.: Monetary policy according to hank. American Economic Review **108** (3), 697–743 (2018) 

- [62] Adjemian, S., Bastani, H., Juillard, M., Karam´e, F., Mihoubi, F., Mutschler, W., Pfeifer, J., Ratto, M., Rion, N., Villemot, S.: Dynare: Reference Manual Version 5. Technical report, CEPREMAP (2022) 

- [63] Cao, D., Luo, W., Nie, G.: Global dsge models. Review of Economic Dynamics (2023) 

- [64] Del Negro, M., Giannoni, M.P., Schorfheide, F.: Inflation in the great recession and new keynesian models. American Economic Journal: Macroeconomics **7** (1), 168–96 (2015) 

- [65] Del Negro, M., Giannoni, M., Li, P., Moszkowski, E., Smith, M.: New York Fed DSGE Model (Version 1002). GitHub (2015) 

- [66] Fagiolo, G., Roventini, A.: Macroeconomic policy in dsge and agent-based models redux: New developments and challenges ahead. Available at SSRN 2763735 (2016) 

- [67] Haldane, A.G., Turrell, A.E.: Drawing on different disciplines: macroeconomic agent-based models. Journal of Evolutionary Economics **29** , 39–66 (2019) 

- [68] Fukac, M., Pagan, A., _et al._ : Issues in adopting dsge models for use in the policy process. Australian National University, Centre for Applied Macroeconomic Analysis, CAMA Working Paper **10** , 2006 (2006) 

- [69] Evans, G.W., Honkapohja, S.: Learning and expectations in macroeconomics. In: Learning and Expectations in Macroeconomics. Princeton University Press, 

51 

??? (2012) 

- [70] Sargent, T.J.: The Conquest of American Inflation. Princeton University Press, ??? (1999) 

- [71] Stiglitz, J.E.: Where modern macroeconomics went wrong. Oxford Review of Economic Policy **34** (1-2), 70–106 (2018) 

- [72] Deissenberg, C., Van Der Hoog, S., Dawid, H.: Eurace: A massively parallel agent-based model of the european economy. Applied mathematics and computation **204** (2), 541–552 (2008) 

- [73] Dawid, H., Harting, P., Hoog, S., Neugart, M.: A heterogeneous agent macroeconomic model for policy evaluation: Improving transparency and reproducibility (2016) 

- [74] Geanakoplos, J., Axtell, R., Farmer, D.J., Howitt, P., Conlee, B., Goldstein, J., Hendrey, M., Palmer, N.M., Yang, C.-Y.: Getting at systemic risk via an agentbased model of the housing market. American Economic Review **102** (3), 53–58 (2012) 

- [75] Carro, A., Hinterschweiger, M., Uluc, A., Farmer, J.D.: Heterogeneous effects and spillovers of macroprudential policy in an agent-based model of the uk housing market. Industrial and Corporate Change **32** (2), 386–432 (2023) 

- [76] Zhang, T., Williams, A., Phade, S., Srinivasa, S., Zhang, Y., Gupta, P., Bengio, Y., Zheng, S.: Ai for global climate cooperation: modeling global climate negotiations, agreements, and long-term cooperation in rice-n. arXiv preprint arXiv:2208.07004 (2022) 

- [77] Nordhaus, W.D., Yang, Z.: A regional dynamic general-equilibrium model of alternative climate-change strategies. The American Economic Review, 741–765 (1996) 

- [78] Dosi, G., Fagiolo, G., Roventini, A.: An evolutionary model of endogenous business cycles. Computational Economics **27** , 3–34 (2006) 

- [79] Dosi, G., Napoletano, M., Roventini, A., Treibich, T.: Micro and macro policies in the keynes+ schumpeter evolutionary models. Journal of Evolutionary Economics **27** , 63–90 (2017) 

- [80] Dosi, G., Fagiolo, G., Napoletano, M., Roventini, A., Treibich, T.: Fiscal and monetary policies in complex evolving economies. Journal of Economic Dynamics and Control **52** , 166–189 (2015) 

- [81] Dawid, H., Gatti, D.D.: Agent-based macroeconomics. Handbook of computational economics **4** , 63–156 (2018) 

52 

- [82] Atashbar, T., Shi, R.A.: AI and Macroeconomic Modeling: Deep Reinforcement Learning in an RBC Model. International Monetary Fund, ??? (2023) 

- [83] Evans, G.W., Honkapohja, S.: Policy interaction, expectations and the liquidity trap. Review of Economic Dynamics **8** (2), 303–323 (2005) 

- [84] Garg, D., Evans, B.P., Ardon, L., Narayanan, A.L., Vann, J., Madhushani, U., Henry-Nickie, M., Ganesh, S.: A heterogeneous agent model of mortgage servicing: An income-based relief analysis. arXiv preprint arXiv:2402.17932 (2024) 

- [85] Koster, R., Balaguer, J., Tacchetti, A., Weinstein, A., Zhu, T., Hauser, O., Williams, D., Campbell-Gillingham, L., Thacker, P., Botvinick, M., _et al._ : Human-centred mechanism design with democratic ai. Nature Human Behaviour **6** (10), 1398–1407 (2022) 

- [86] Taylor, J.B.: Discretion versus policy rules in practice. In: Carnegie-Rochester Conference Series on Public Policy, vol. 39, pp. 195–214 (1993) 

- [87] Nikolsko-Rzhevskyy, A., Papell, D.H., Prodan, R.: Policy rules and economic performance. Journal of Macroeconomics **68** , 103291 (2021) 

- [88] Svensson, L.E.: Monetary policy strategies for the federal reserve. Technical report, National Bureau of Economic Research (2020) 

- [89] Lucas Jr, R.E.: Econometric policy evaluation: A critique. In: CarnegieRochester Conference Series on Public Policy, vol. 1, pp. 19–46 (1976) 

- [90] Lan, T., Srinivasa, S., Wang, H., Zheng, S.: Warpdrive: fast end-to-end deep multi-agent reinforcement learning on a gpu. Journal of Machine Learning Research **23** (316), 1–6 (2022) 

- [91] Dwarakanath, K., Vyetrenko, S., Tavallali, P., Balch, T.: Abides-economist: Agent-based simulation of economic systems with learning agents. arXiv preprint arXiv:2402.09563v1 (2024) 

- [92] Dwarakanath, K., Dong, J., Vyetrenko, S.: Tax credits and household behavior: The roles of myopic decision-making and liquidity in a simulated economy. In: Proceedings of the 5th ACM International Conference on AI in Finance, pp. 168–176 (2024) 

- [93] Dwarakanath, K., Vyetrenko, S., Balch, T.: Empirical equilibria in agent-based economic systems with learning agents. arXiv preprint arXiv:2408.12038 (2024) 

- [94] Cobb, C.W., Douglas, P.H.: A theory of production. American Economic Association (1928) 

- [95] U.S. Bureau of Labor Statistics: Industry Output and Employment. https:// 

53 

www.bls.gov/emp/data/industry-out-and-emp.htm (2024) 

- [96] Internal Revenue Service: Returns filed, taxes collected and refunds issued. https: //www.irs.gov/statistics/returns-filed-taxes-collected-and-refunds-issued? secureweb=POWERPNT (2023) 

- [97] Watkins, C.J., Dayan, P.: Q-learning. Machine learning **8** , 279–292 (1992) 

- [98] Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.A., Veness, J., Bellemare, M.G., Graves, A., Riedmiller, M., Fidjeland, A.K., Ostrovski, G., _et al._ : Human-level control through deep reinforcement learning. nature **518** (7540), 529–533 (2015) 

- [99] Mnih, V.: Asynchronous methods for deep reinforcement learning. arXiv preprint arXiv:1602.01783 (2016) 

- [100] Schulman, J.: Trust region policy optimization. arXiv preprint arXiv:1502.05477 (2015) 

- [101] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O.: Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 (2017) 

- [102] Bowling, M., Veloso, M.: Multiagent learning using a variable learning rate. Artificial intelligence **136** (2), 215–250 (2002) 

- [103] Wong, A., B¨ack, T., Kononova, A.V., Plaat, A.: Deep multiagent reinforcement learning: Challenges and directions. Artificial Intelligence Review **56** (6), 5023– 5056 (2023) 

- [104] Tan, M.: Multi-agent reinforcement learning: Independent vs. cooperative agents. In: Proceedings of the Tenth International Conference on Machine Learning, pp. 330–337 (1993) 

- [105] Liang, E., Liaw, R., Nishihara, R., Moritz, P., Fox, R., Goldberg, K., Gonzalez, J., Jordan, M., Stoica, I.: Rllib: Abstractions for distributed reinforcement learning. In: International Conference on Machine Learning (2018) 

- [106] Franke, R., Westerhoff, F.: Structural stochastic volatility in asset pricing dynamics: Estimation and model contest. Journal of Economic Dynamics and Control **36** (8), 1193–1211 (2012) 

- [107] Dosi, G.: Statistical regularities in the evolution of industries: a guide through some evidence and challenges for the theory. Technical report, LEM working paper series (2005) 

- [108] Dosi, G., Roventini, A.: More is different... and complex! the case for agent-based macroeconomics. Journal of Evolutionary Economics **29** , 1–37 (2019) 

- [109] Burns, A.F., Mitchell, W.C.: Measuring Business Cycles. National bureau of 

54 

economic research, Massachusetts (1946) 

- [110] Stock, J.H., Watson, M.W.: Business cycle fluctuations in us macroeconomic time series. Handbook of macroeconomics **1** , 3–64 (1999) 

- [111] Hodrick, R.J., Prescott, E.C.: Postwar us business cycles: an empirical investigation. Journal of Money, credit, and Banking, 1–16 (1997) 

- [112] Harvey, A.C., Jaeger, A.: Detrending, stylized facts and the business cycle. Journal of applied econometrics **8** (3), 231–247 (1993) 

- [113] Baxter, M., King, R.G.: Measuring business cycles: approximate band-pass filters for economic time series. Review of economics and statistics **81** (4), 575–593 (1999) 

- [114] Phillips, A.W.: The relation between unemployment and the rate of change of money wage rates in the united kingdom, 1861-1957. economica **25** (100), 283–299 (1958) 

- [115] Okun, A.M.: Potential GNP: Its Measurement and Significance. Cowles Foundation for Research in Economics at Yale University, Connecticut (1963) 

- [116] Knotek II, E.S.: How useful is okun’s law? Economic Review-Federal Reserve Bank of Kansas City **92** (4), 73 (2007) 

- [117] Ball, L., Leigh, D., Loungani, P.: Okun’s law: Fit at 50? Journal of Money, Credit and Banking **49** (7), 1413–1441 (2017) 

- [118] Diamond, P., Blanchard, O.: The beveridge curve. Brookings Papers on Economic Activity **1** , 1–76 (1989) 

- [119] Shimer, R.: The cyclical behavior of equilibrium unemployment and vacancies. American economic review **95** (1), 25–49 (2005) 

- [120] Kaldor, N.: Capital accumulation and economic growth. In: The Theory of Capital: Proceedings of a Conference Held by the International Economic Association, pp. 177–222 (1961). Springer 

- [121] Jones, C.I., Romer, P.M.: The new kaldor facts: ideas, institutions, population, and human capital. American Economic Journal: Macroeconomics **2** (1), 224–245 (2010) 

- [122] Arroyo Abad, L., Khalifa, K.: What are stylized facts? Journal of Economic Methodology **22** (2), 143–156 (2015) 

- [123] Wolff, E.N.: Estimates of household wealth inequality in the us, 1962–1983. Review of Income and Wealth **33** (3), 231–256 (1987) 

55 

- [124] Piketty, T., Saez, E.: Income inequality in the united states, 1913–1998. The Quarterly journal of economics **118** (1), 1–41 (2003) 

- [125] Kuhn, M., R´ıos-Rull, J.-V., _et al._ : 2013 update on the us earnings, income, and wealth distributional facts: A view from macroeconomics. Federal Reserve Bank of Minneapolis Quarterly Review **37** (1), 2–73 (2016) 

- [126] Piketty, T., Saez, E., Zucman, G.: Distributional national accounts: methods and estimates for the united states. The Quarterly Journal of Economics **133** (2), 553–609 (2018) 

- [127] Benhabib, J., Bisin, A.: Skewed wealth distributions: Theory and empirics. Journal of Economic Literature **56** (4), 1261–1291 (2018) 

- [128] Gibrat, R., Les In´egalites Economiques,<sup>´</sup> L.d.R.: Sirey. Paris, France (1931) 

- [129] Bottazzi, G., Secchi, A.: Common properties and sectoral specificities in the dynamics of us manufacturing companies. Review of Industrial Organization **23** , 217–232 (2003) 

- [130] Parham, R.: Facts of us firm scale and growth 1970-2019: An illustrated guide. arXiv preprint arXiv:2302.02485 (2023) 

- [131] S&P Global Marketplace: Compustat Financials. https://www.marketplace. spglobal.com/en/datasets/compustat-financials-(8) (2025) 

- [132] Istituto Nazionale di Statistica: Istat Data. https://www.istat.it/en/data/ (2025) 

- [133] Campbell, J.Y.: Household finance. The journal of finance **61** (4), 1553–1604 (2006) 

- [134] Gomes, F., Haliassos, M., Ramadorai, T.: Household finance. Journal of Economic Literature **59** (3), 919–1000 (2021) 

- [135] Beshears, J., Choi, J.J., Laibson, D., Madrian, B.C.: Behavioral household finance. In: Handbook of Behavioral Economics: Applications and Foundations 1 vol. 1, pp. 177–276. Elsevier, ??? (2018) 

- [136] Taylor, J.B., Williams, J.C.: Simple and robust rules for monetary policy. In: Handbook of Monetary Economics vol. 3, pp. 829–859. Elsevier, ??? (2010) 

- [137] Statista: Per capita consumption of the bread and cereal products in the United States from 2017 to 2027. https://www.statista.com/forecasts/1374278/ size-of-the-bread-and-cereal-product-market-in-the-united-states (2023) 

- [138] USA.gov: Minimum wage. https://www.usa.gov/minimum-wage (2023) 

56 

- [139] U.S. Bureau of Labor Statistics: Average hourly and weekly earnings of all employees on private nonfarm payrolls by industry sector, seasonally adjusted. https://www.bls.gov/news.release/empsit.t19.htm (2023) 

- [140] U.S. Bureau of Labor Statistics: Average price data (in U.S. dollars), selected items. https://www.bls.gov/charts/consumer-price-index/ consumer-price-index-average-price-data.htm (2023) 

- [141] Federal Reserve Board: Selected Interest Rates (Daily). https://www. federalreserve.gov/releases/h15/ (2023) 

- [142] Internal Revenue Service: 2022 Tax Rate Schedules. https://www.irs.gov/ media/166986 (2022) 

- [143] Wellman, M.P.: Economic reasoning from simulation-based game models. Œconomia. History, Methodology, Philosophy (10-2), 257–278 (2020) 

- [144] Lanctot, M., Zambaldi, V., Gruslys, A., Lazaridou, A., Tuyls, K., P´erolat, J., Silver, D., Graepel, T.: A unified game-theoretic approach to multiagent reinforcement learning. Advances in neural information processing systems **30** (2017) 

- [145] Taskesen, E.: distfit Is a Python Library for Probability Density Fitting. https: //erdogant.github.io/distfit 

57 

