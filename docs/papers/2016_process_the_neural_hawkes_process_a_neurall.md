---
title: "The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process"
authors: "process"
year: 2016
arxiv_id: "1612.09328"
original_file: "1612.09328.pdf"
pdf_path: "docs/papers\2016_process_the_neural_hawkes_process_a_neurall.pdf"
---

# The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process

**Authors:** Process et al.  
**Year:** 2016 | **arXiv:** [`1612.09328`](https://arxiv.org/abs/1612.09328)  
**Local PDF:** [`2016_process_the_neural_hawkes_process_a_neurall.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2016_process_the_neural_hawkes_process_a_neurall.pdf)

---

## **The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process** 

**Hongyuan Mei Jason Eisner** 

Department of Computer Science, Johns Hopkins University 3400 N. Charles Street, Baltimore, MD 21218 U.S.A _{_ hmei,jason _}_ @cs.jhu.edu 

### **Abstract** 

Many events occur in the world. Some event types are stochastically excited or inhibited—in the sense of having their probabilities elevated or decreased—by patterns in the sequence of previous events. Discovering such patterns can help us predict _which type_ of event will happen next and _when_ . We model streams of discrete events in continuous time, by constructing a **neurally self-modulating multivariate point process** in which the intensities of multiple event types evolve according to a novel **continuous-time LSTM** . This generative model allows past events to influence the future in complex and realistic ways, by conditioning future event intensities on the hidden state of a recurrent neural network that has consumed the stream of past events. Our model has desirable qualitative properties. It achieves competitive likelihood and predictive accuracy on real and synthetic datasets, including under missing-data conditions. 

### **1 Introduction** 

Some events in the world are correlated. A single event, or a pattern of events, may help to cause or prevent future events. We are interested in learning the distribution of sequences of events (and in future work, the causal structure of these sequences). The ability to discover correlations among events is crucial to accurately predict the future of a sequence given its past, i.e., which events are likely to happen next and when they will happen. 

We specifically focus on sequences of discrete events in continuous time (“event streams”). Modeling such sequences seems natural and useful in many applied domains: 

- _Medical events._ Each patient has a sequence of acute incidents, doctor’s visits, tests, diagnoses, and medications. By learning from previous patients what sequences tend to look like, we could predict a new patient’s future from their past. 

- _Consumer behavior._ Each online consumer has a sequence of online interactions. By modeling the distribution of sequences, we can learn purchasing patterns. Buying cookies may temporarily depress purchases of all desserts, yet increase the probability of buying milk. 

- _“Quantified self” data._ Some individuals use cellphone apps to record their behaviors— eating, traveling, working, sleeping, waking. By anticipating behaviors, an app could perform helpful supportive actions, including issuing reminders and placing advance orders. 

- _Social media actions._ Previous posts, shares, comments, messages, and likes by a set of users are predictive of their future actions. 

- Other event streams arise in _news_ , _animal behavior_ , _dialogue_ , _music_ , etc. 

A basic model for event streams is the **Poisson process** (Palm, 1943), which assumes that events occur independently of one another. In a **non-homogenous Poisson process** , the (infinitesimal) probability of an event happening at time _t_ may vary with _t_ , but it is still independent of other events. A **Hawkes process** (Hawkes, 1971; Liniger, 2009) supposes that past events can temporarily _raise_ the probability of future events, assuming that such excitation is x positive, y additive over the past events, and z exponentially decaying with time. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA. 



<!-- Start of picture text -->
Intensity-1 Intensity-2<br>BaseRate-1 BaseRate-2<br>LSTM-Unit<br>Type-1 Type-2<br><!-- End of picture text -->



Figure 1: Drawing an event stream from a neural Hawkes process. An LSTM reads the sequence of past events (polygons) to arrive at a hidden state (orange). That state determines the future “intensities” of the two types of events—that is, their time-varying instantaneous probabilities. The intensity functions are continuous parametric curves (solid lines) determined by the most recent LSTM state, with dashed lines showing the steady-state asymptotes that they would eventually approach. In this example, events of type 1 excite type 1 but inhibit type 2. Type 2 excites itself, and excites or inhibits type 1 according to whether the count of type 2 events so far is odd or even. Those are immediate effects, shown by the sudden jumps in intensity. The events also have longer-timescale effects, shown by the shifts in the asymptotic dashed lines. 

However, real-world patterns often seem to violate these assumptions. For example, x is violated if one event inhibits another rather than exciting it: cookie consumption inhibits cake consumption. y is violated when the combined effect of past events is not additive. Examples abound: The 20th advertisement does not increase purchase rate as much as the first advertisement did, and may even drive customers away. Market players may act based on their own complex analysis of market history. Musical note sequences follow some intricate language model that considers melodic trajectory, rhythm, chord progressions, repetition, etc. z is violated when, for example, a past event has a delayed effect, so that the effect starts at 0 and increases sharply before decaying. 

We generalize the Hawkes process by determining the event intensities (instantaneous probabilities) from the hidden state of a recurrent neural network. This state is a deterministic function of the past history. It plays the same role as the state of a deterministic finite-state automaton. However, the recurrent network enjoys a continuous and infinite state space (a high-dimensional Euclidean space), as well as a learned transition function. In our network design, the state is updated discontinuously with each successive event occurrence and also evolves continuously as time elapses between events. 

Our main motivation is that our model can capture effects that the Hawkes process misses. The combined effect of past events on future events can now be superadditive, subadditive, or even subtractive, and can depend on the sequential ordering of the past events. Recurrent neural networks already capture other kinds of complex sequential dependencies when applied to language modeling—that is, generative modeling of linguistic word sequences, which are governed by syntax, semantics, and habitual usage (Mikolov et al., 2010; Sundermeyer et al., 2012; Karpathy et al., 2015). We wish to extend their success (Chelba et al., 2013) to sequences of events in _continuous_ time. 

Another motivation for a more expressive model than the Hawkes process is to cope with missing data. Even in a domain where Hawkes might be appropriate, it is hard to apply Hawkes when sequences are only partially observed. Real datasets may _systematically_ omit some types of events (e.g., illegal drug use, or offline purchases) which, in the true generative model, would have a strong influence on the future. They may also have _stochastically_ missing data, where the missingness mechanism—the probability that an event is not recorded—can be complex and data-dependent (MNAR). In this setting, we can fit our model directly to the observation sequences, and use it to predict observation sequences that were generated in the same way (using the same complete-data distribution and the same missingness mechanism). Note that if one knew the true complete-data distribution—perhaps Hawkes—and the true missingness mechanism, one would optimally predict the incomplete future from the incomplete past in Bayesian fashion, by integrating over possible completions (imputing the missing events and considering their influence on the future). Our hope is that the neural model is expressive enough that it can learn to approximate this true predictive distribution. Its hidden state after observing the past should implicitly encode the Bayesian posterior, and its update rule for this hidden state should emulate the “observable operator” that updates the posterior upon each new observation. See Appendix A.4 for further discussion. 

2 

A final motivation is that one might wish to _intervene_ in a medical, economic, or social event stream so as to improve the future course of events. Appendix D discusses our plans to deploy our model family as an environment model within reinforcement learning, where an agent controls some events. 

### **2 Notation** 

We are interested in constructing distributions over **event streams** ( _k_ 1 _, t_ 1) _,_ ( _k_ 2 _, t_ 2) _, . . ._ , where each _ki ∈{_ 1 _,_ 2 _, . . . , K}_ is an event type and 0 _< t_ 1 _< t_ 2 _< · · ·_ are times of occurrence.<sup>1</sup> That is, there are _K_ types of events, tokens of which are observed to occur in continuous time. 

For any distribution _P_ in our proposed family, an event stream is almost surely infinite. However, when we observe the process only during a time interval [0 _, T_ ], the number _I_ of observed events is almost surely finite. The _log-likelihood ℓ_ of the model _P_ given these _I_ observations is 



where the **history** _Hi_ is the prefix sequence ( _k_ 1 _, t_ 1), ( _k_ 2 _, t_ 2) _, . . . ,_ ( _ki−_ 1 _, ti−_ 1), and ∆ _ti_ =def _ti − ti−_ 1, and _P_ (( _ki, ti_ ) _| Hi,_ ∆ _ti_ ) _dt_ is the probability that the _next_ event occurs at time _ti_ and has type _ki_ . Throughout the paper, the subscript _i_ usually denotes quantities that affect the distribution of the next event ( _ki, ti_ ). These quantities depend only on the history _Hi_ . 

We use (lowercase) Greek letters for parameters related to the classical Hawkes process, and Roman letters for other quantities, including hidden states and affine transformation parameters. We denote vectors by bold lowercase letters such as **s** and **_µ_** , and matrices by bold capital Roman letters such as **U** . Subscripted bold letters denote distinct vectors or matrices (e.g., **w** _k_ ). Scalar quantities, including vector and matrix elements such as _sk_ and _αj,k_ , are written without bold. Capitalized scalars represent upper limits on lowercase scalars, e.g., 1 _≤ k ≤ K_ . Function symbols are notated like their return type. All R _→_ R functions are extended to apply elementwise to vectors and matrices. 

### **3 The Model** 

In this section, we first review Hawkes processes, and then introduce our model one step at a time. 

Formally, generative models of event streams are **multivariate point processes** . A (temporal) point process is a probability distribution over _{_ 0 _,_ 1 _}_ -valued functions on a given time interval (for us, [0 _, ∞_ )). A multivariate point process is formally a distribution over _K_ -tuples of such functions. The _k_<sup>th</sup> function indicates the times at which events of type _k_ occurred, by taking value 1 at those times. 

#### **3.1 Hawkes Process: A Self-Exciting Multivariate Point Process (SE-MPP)** 

A basic model of event streams is the **non-homogeneous multivariate Poisson process** . It assumes that an event of type _k_ occurs at time _t_ —more precisely, in the infinitesimally wide interval [ _t, t_ + _dt_ )—with probability _λk_ ( _t_ ) _dt_ . The value _λk_ ( _t_ ) _≥_ 0 can be regarded as a rate per unit time, just like the parameter _λ_ of an ordinary Poisson process. _λk_ is known as the **intensity function** , and the total intensity of all event types is given by _λ_ ( _t_ ) =<sup>�</sup><sup>_K_</sup> _k_ =1<sup>_λk_(</sup><sup>_t_).</sup> 

A well-known generalization that captures interactions is the **self-exciting multivariate point process (SE-MPP)** , or **Hawkes process** (Hawkes, 1971; Liniger, 2009), in which past events _h_ from the history conspire to _raise_ the intensity of each type of event. Such excitation is positive, additive over the past events, and exponentially decaying with time: 



where _µk ≥_ 0 is the base intensity of event type _k_ , _αj,k ≥_ 0 is the degree to which an event of type _j_ initially excites type _k_ , and _δj,k >_ 0 is the decay rate of that excitation. When an event occurs, all intensities are elevated to various degrees, but then will decay toward their base rates **_µ_** . 

> 1More generally, one could allow 0 _≤ t_ 1 _≤ t_ 2 _≤· · ·_ , where _ti_ is a **immediate event** if _ti−_ 1 = _ti_ and a **delayed event** if _ti−_ 1 _< ti_ . It is not too difficult to extend our model to assign positive probability to immediate events, but we will disallow them here for simplicity. 

3 

#### **3.2 Self-Modulating Multivariate Point Processes** 

The positivity constraints in the Hawkes process limit its expressivity. First, the positive interaction parameters _αj,k_ fail to capture inhibition effects, in which past events _reduce_ the intensity of future events. Second, the positive base rates **_µ_** fail to capture the inherent inertia of some events, which are unlikely until their cumulative excitation by past events crosses some threshold. To remove such limitations, we introduce two _self-modulating_ models. Here the intensities of future events are stochastically _modulated_ by the past history, where the term “modulation” is meant to encompass both excitation and inhibition. The intensity _λk_ ( _t_ ) can even fluctuate non-monotonically between successive events, because the competing excitatory and inhibitory influences may decay at different rates. 

#### **3.2.1 Hawkes Process with Inhibition: A Decomposable Self-Modulating MPP (D-SM-MPP)** 

Our first move is to enrich the Hawkes model’s expressiveness while still maintaining its decomposable structure. We relax the positivity constraints on _αj,k_ and _µk_ , allowing them to range over R, which allows _inhibition_ ( _αj,k <_ 0) and _inertia_ ( _µk <_ 0). However, the resulting total activation could now be negative. We therefore pass it through a non-linear **transfer function** _fk_ : R _→_ R+ to obtain a positive intensity function as required: 



As _t_ increases between events, the intensity _λk_ ( _t_ ) may both rise and fall, but eventually approaches the base rate _f_ ( _µk_ +0), as the influence of each previous event still decays toward 0 at a rate _δj,k >_ 0. 

What non-linear function _fk_ should we use? The ReLU function _f_ ( _x_ ) = max( _x,_ 0) is not strictly positive as required. A better choice is the scaled “softplus” function _f_ ( _x_ ) = _s_ log(1 + exp( _x/s_ )), which approaches ReLU as _s →_ 0. We learn a separate scale parameter _sk_ for each event type _k_ , which adapts to the rate of that type. So we instantiate (3a) as _λk_ ( _t_ ) = _fk_ ( _λ_<sup>˜</sup> _k_ ( _t_ )) = _sk_ log(1 + exp( _λ_<sup>˜</sup> _k_ ( _t_ ) _/sk_ )). Appendix A.1 graphs this and motivates the “softness” and the scale parameter. 

#### **3.2.2 Neural Hawkes Process: A Neurally Self-Modulating MPP (N-SM-MPP)** 

Our second move removes the restriction that the past events have independent, additive influence on _λ_<sup>˜</sup> _k_ ( _t_ ). Rather than predict _λ_<sup>˜</sup> _k_ ( _t_ ) as a simple summation (3b), we now use a recurrent neural network. This allows learning a complex dependence of the intensities on the number, order, and timing of past events. We refer to our model as a **neural Hawkes process** . 

Just as before, each event type _k_ has an time-varying intensity _λk_ ( _t_ ), which jumps discontinuously at each new event, and then drifts continuously toward a baseline intensity. In the new process, however, these dynamics are controlled by a hidden state vector **h** ( _t_ ) _∈_ ( _−_ 1 _,_ 1)<sup>_D_</sup> , which in turn depends on a vector **c** ( _t_ ) _∈_ R<sup>_D_</sup> of memory cells in a **continuous-time LSTM** .<sup>2</sup> This novel recurrent neural network architecture is inspired by the familiar discrete-time LSTM (Hochreiter and Schmidhuber, 1997; Graves, 2012). The difference is that in the continuous interval following an event, each memory cell _c exponentially decays_ at some rate _δ_ toward some steady-state value ¯ _c_ . 

At each time _t >_ 0, we obtain the intensity _λk_ ( _t_ ) by (4a), where (4b) shows how the hidden states **h** ( _t_ ) are continually obtained from the memory cells **c** ( _t_ ) as the cells decay: 



This says that on the interval ( _ti−_ 1 _, ti_ ]—in other words, after event _i−_ 1 up until event _i_ occurs at some time _ti_ —the **h** ( _t_ ) defined by equation (4b) determines the intensity functions via equation (4a). So for _t_ in this interval, according to the model, **h** ( _t_ ) is a sufficient statistic of the history ( _Hi, t − ti−_ 1) with respect to future events (see equation (1)). **h** ( _t_ ) is analogous to **h** _i_ in an LSTM language model (Mikolov et al., 2010), which summarizes the past event sequence _k_ 1 _, . . . , ki−_ 1. But in our decay architecture, it will also reflect the interarrival times _t_ 1 _−_ 0 _, t_ 2 _− t_ 1 _, . . . , ti−_ 1 _− ti−_ 2 _, t − ti−_ 1. This interval ( _ti−_ 1 _, ti_ ] ends when the next event _ki_ stochastically occurs at some time _ti_ . At this point, the continuous-time LSTM reads ( _ki, ti_ ) and updates the current (decayed) hidden cells **c** ( _t_ ) to new initial values **c** _i_ +1, based on the current (decayed) hidden state **h** ( _ti_ ). 

> 2We use one-layer LSTMs with _D_ hidden units in our present experiments, but a natural extension is to use multi-layer (“deep”) LSTMs (Graves et al., 2013), in which case **h** ( _t_ ) is the hidden state of the top layer. 

4 

How does the continuous-time LSTM make those updates? Other than depending on decayed values, the update formulas resemble the discrete-time case:<sup>3</sup> 



The vector **k** _i ∈{_ 0 _,_ 1 _}_<sup>_K_</sup> is the _i_<sup>th</sup> input: a one-hot encoding of the new event _ki_ , with non-zero value only at the entry indexed by _ki_ . The above formulas will make a discrete update to the LSTM state. They resemble the discrete-time LSTM, but there are two differences. First, the updates do not depend on the “previous” hidden state from just after time _ti−_ 1, but rather its value **h** ( _ti_ ) at time _ti_ , after it has decayed for a period of _ti − ti−_ 1. Second, equations (6b)–(6c) are new. They define how in future, as _t > ti_ increases, the elements of **c** ( _t_ ) will continue to deterministically decay (at different rates) from **c** _i_ +1 toward targets ¯ **c** _i_ +1. Specifically, **c** ( _t_ ) is given by (7), which continues to control **h** ( _t_ ) and thus _λk_ ( _t_ ) (via (4), except that _i_ has now increased by 1). 



In short, not only does (6a) define the usual cell values **c** _i_ +1, but equation (7) defines **c** ( _t_ ) on R _>_ 0. On the interval ( _ti, ti_ +1], **c** ( _t_ ) follows an exponential curve that begins at **c** _i_ +1 (in the sense that lim _t→t_ + _i_<sup>**c**(</sup><sup>_t_) =</sup><sup>**c**</sup><sup>_i_+1) and decays toward ¯</sup><sup>**c**</sup><sup>_i_+1 (which it would approach as</sup><sup>_t →∞_, if extrapolated).</sup> 

A schematic example is shown in Figure 1. As in the previous models, _λk_ ( _t_ ) drifts deterministically between events toward some base rate. But the neural version is different in three ways: x The base rate is not a constant _µk_ , but shifts upon each event.<sup>4</sup> y The drift can be non-monotonic, because the excitatory and inhibitory influences on _λk_ ( _t_ ) from different elements of **h** ( _t_ ) may decay at different rates. z The sigmoidal transfer function means that the behavior of **h** ( _t_ ) itself is a little more interesting than exponential decay. Suppose that **c** _i_ is very negative but increases toward a target **c** ¯ _i >_ 0. Then **h** ( _t_ ) will stay close to _−_ 1 for a while and then will rapidly rise past 0. This usefully lets us model a delayed response (e.g. the last green segment in Figure 1). 

We point out two behaviors that are naturally captured by our LSTM’s “forget” and “input” gates: 

- if **f** _i_ +1 _≈_ **1** and **i** _i_ +1 _≈_ **0** , then **c** _i_ +1 _≈_ **c** ( _ti_ ). So **c** ( _t_ ) and **h** ( _t_ ) will be _continuous_ at _ti_ . There is no jump due to event _i_ , though the steady-state target may change. 

- if<sup>¯</sup> **f** _i_ +1 _≈_ **1** and ¯ **_ı_** _i_ +1 _≈_ **0** , then ¯ **c** _i_ +1 _≈_ **c** ¯ _i_ . So although there may be a jump in activation, it is temporary. The memory cells will decay toward the same steady states as before. 

Among other benefits, this lets us fit datasets in which (as is common) some pairs of event types do _not_ influence one another. Appendix A.3 explains why all the models in this paper have this ability. 

The drift of **c** ( _t_ ) between events controls how the system’s expectations about future events change as more time elapses with no event having yet occured. Equation (7) chooses a moderately flexible parametric form for this drift function (see Appendix D for some alternatives). Equation (6a) was designed so that **c** in an LSTM could learn to count past events with discrete-time exponential discounting; and (7) can be viewed as extending that to continuous-time exponential discounting. 

Our memory cell vector **c** ( _t_ ) is a _deterministic_ function of the past history ( _Hi, t − ti_ ).<sup>5</sup> Thus, the event intensities at any time are also deterministic via equation (4). The stochastic part of the model is the random choice—based on these intensities—of _which_ event happens next and _when_ it happens. The events are in competition: an event with high intensity is likely to happen sooner than an event with low intensity, and whichever one happens first is fed back into the LSTM. If no event type has high intensity, it may take a long time for the next event to occur. 

Training the model means learning the LSTM parameters in equations (5) and (6c) along with the other parameters mentioned in this section, namely _sk ∈_ R and **w** _k ∈_ R<sup>_D_</sup> for _k ∈{_ 1 _,_ 2 _, . . . , K}_ . 

> 3The upright-font subscripts i, f, z and o are not variables, but constant labels that distinguish different **W** , **U** and **d** tensors. The<sup>¯</sup> **f** and ¯ **_ı_** in equation (6b) are defined analogously to **f** and **i** but with different weights. 

> 4Equations (4b) and (7) imply that after event _i −_ 1, the base rate jumps to _fk_ ( **w** _⊤_ ( **o** _i ⊙_ (2 _σ_ (2¯ **c** _i_ ) _−_ 1))). 

> 5Appendix A.2 explains how our LSTM handles the start and end of the sequence. 

5 

### **4 Algorithms** 

For the proposed models, the log-likelihood (1) of the parameters turns out to be given by a simple formula—the sum of the log-intensities of the events that happened, at the times they happened, minus an integral of the total intensities over the observation interval [0 _, T_ ]: 



The full derivation is given in Appendix B.1. Intuitively, the _−_ Λ term (which is _≤_ 0) sums the log-probabilities of infinitely many _non_ -events. Why? The probability that there was _not_ an event of any type in the infinitesimally wide interval [ _t, t_ + _dt_ ) is 1 _− λ_ ( _t_ ) _dt_ , whose log is _−λ_ ( _t_ ) _dt_ . 

We can locally maximize _ℓ_ using any stochastic gradient method. A detailed recipe is given in Appendix B.2, including the Monte Carlo trick we use to handle the integral in equation (8). 

If we wish to draw random sequences from the model, we can adopt the thinning algorithm (Lewis and Shedler, 1979; Liniger, 2009) that is commonly used for the Hawkes process. See Appendix B.3. 

Given an event stream prefix ( _k_ 1 _, t_ 1), ( _k_ 2 _, t_ 2), ..., ( _ki−_ 1 _, ti−_ 1), we may wish to predict the _time_ and _type_ of the single next event. The next event’s time _ti_ has density _pi_ ( _t_ ) = _P_ ( _ti_ = _t | Hi_ ) = _− λ_ ( _t_ ) exp � � _tti−_ 1<sup>_λ_(</sup><sup>_s_)</sup><sup>_ds_</sup> �. To predict a single time whose expected L2 loss is as low as possible, we should choose _t_<sup>ˆ</sup> _i_ = E[ _ti | Hi_ ] = � _t∞i−_ 1<sup>_tpi_(</sup><sup>_t_)</sup><sup>_dt_.Giventhenexteventtime</sup><sup>_ti_,themostlikely</sup> type would be argmax _k λk_ ( _ti_ ) _/λ_ ( _ti_ ), but the most likely next event type _without_ knowledge of _ti_ is _k_<sup>ˆ</sup> _i_ = argmax _k_ � _t∞i−_ 1 _λλk_ (( _tt_ ))<sup>_pi_(</sup><sup>_t_)</sup><sup>_dt_.Theintegralsintheprecedingequationscanbeestimatedby</sup> Monte Carlo sampling much as before (Appendix B.2). For event type prediction, we recommend a paired comparison that uses the same _t_ values for each _k_ in the argmax; this also lets us share the _λ_ ( _t_ ) and _pi_ ( _t_ ) computations across all _k_ . 

### **5 Related Work** 

The Hawkes process has been widely used to model event streams, including for topic modeling and clustering of text document streams (He et al., 2015; Du et al., 2015a), constructing and inferring network structure (Yang and Zha, 2013; Choi et al., 2015; Etesami et al., 2016), personalized recommendations based on users’ temporal behavior (Du et al., 2015b), discovering patterns in social interaction (Guo et al., 2015; Lukasik et al., 2016), learning causality (Xu et al., 2016), and so on. 

Recent interest has focused on expanding the expressivity of Hawkes processes. Zhou et al. (2013) describe a self-exciting process that removes the assumption of exponentially decaying influence (as we do). They replace the scaled-exponential summands in equation (2) with learned positive functions of time (the choice of function again depends on _ki, k_ ). Lee et al. (2016) generalize the constant excitation parameters _αj,k_ to be stochastic, which increases expressivity. Our model also allows non-constant interactions between event types, but arranges these via deterministic, instead of stochastic, functions of continuous-time LSTM hidden states. Wang et al. (2016) consider non-linear effects of past history on the future, by passing the intensity functions of the Hawkes process through a non-parametric isotonic link function _g_ , which is in the same place as our non-linear function _fk_ . In contrast, our _fk_ has a fixed parametric form (learning only the scale parameter), and is approximately linear when _x_ is large. This is because we model non-linearity (and other complications) with a continuous-time LSTM, and use _fk_ only to ensure positivity of the intensity functions. 

Du et al. (2016) independently combined Hawkes processes with recurrent neural networks (and Xiao et al. (2017a) propose an advanced way of estimating the parameters of that model). However, Du et al.’s architecture is different in several respects. They use standard discrete-time LSTMs without our decay innovation, so they must encode the intervals between past events as explicit numerical inputs to the LSTM. They have only a single intensity function _λ_ ( _t_ ), and it simply decays exponentially toward 0 between events, whereas our more modular model creates separate (potentially transferrable) functions _λk_ ( _t_ ), each of which allows complex and non-monotonic dynamics en route to a non-zero steady state intensity. Some structural limitations of their design are that _ti_ and _ki_ are conditionally independent given **h** (they are determined by separate distributions), and that their model cannot avoid a positive probability of extinction at all times. Finally, since they take 

6 

_f_ = exp, the effect of their hidden units on intensity is effectively multiplicative, whereas we take _f_ = softplus to get an approximately additive effect inspired by the classical Hawkes process. Our rationale is that additivity is useful to capture independent (disjunctive) causes; at the same time, the hidden units that our model adds up can each capture a complex joint (conjunctive) cause. 

### **6 Experiments**<sup>6</sup> 

We fit our various models on several simulated and real-world datasets, and evaluated them in each case by the _log-probability_ that they assigned to held-out data. We also compared our approach with that of Du et al. (2016) on their _prediction_ task. The datasets that we use in this paper range from one extreme with only _K_ = 2 event types but mean sequence length _>_ 2000, to the other extreme with _K_ = 5000 event types but mean sequence length 3. Dataset details can be found in Table 1 in Appendix C.1. Training details (e.g., hyperparameter selection) can be found in Appendix C.2. 

#### **6.1 Synthetic Datasets** 

In a pilot experiment with synthetic data (Appendix C.4), we confirmed that the neural Hawkes process generates data that is not well modeled by training an ordinary Hawkes process, but that ordinary Hawkes data can be successfully modeled by training an neural Hawkes process. 

In this experiment, we were not limited to measuring the likelihood of the models on the stochastic event sequences. We also knew the true latent intensities of the generating process, so we were able to directly measure whether the trained models predicted these intensities accurately. The pattern of results was similar. 

#### **6.2 Real-World Media Datasets** 

**Retweets Dataset** (Zhao et al., 2015) **.** On Twitter, _novel_ tweets are generated from some distribution, which we do not model here. Each novel tweet serves as the beginning-of-stream event (see Appendix A.2) for a subsequent stream of _retweet_ events. We model the dynamics of these streams: how retweets by various types of users ( _K_ = 3) predict later retweets by various types of users. 

Details of the dataset and its preparation are given in Appendix C.5. The dataset is interesting for its temporal pattern. People like to retweet an interesting post soon after it is created and retweeted by others, but may gradually lose interest, so the intervals between retweets become longer over time. In other words, the stream begins in a _self-exciting state_ , in which previous retweets increase the intensities of future retweets, but eventually interest dies down and events are less able to excite one another. The decomposable models are essentially incapable of modeling such a phase transition, but our neural model should have the capacity to do so. 

We generated learning curves (Figure 2) by training our models on increasingly long prefixes of the training set. As we can see, our self-modulating processes _significantly_ outperform the Hawkes process at _all_ training sizes. There is no obvious _a priori_ reason to expect inhibition or even inertia in this application domain, which explains why the D-SM-MPP makes only a small improvement over the Hawkes process when the latter is well-trained. But D-SM-MPP requires much less data, and also has more stable behavior (smaller error bars) on small datasets. Our neural model is even better. Not only does it do better on the average stream, but its _consistent_ superiority over the other two models is shown by the per-stream scatterplots in Figure 3, demonstrating the importance of our model’s neural component even with large datasets. 

**MemeTrack Dataset** (Leskovec and Krevl, 2014) **.** This dataset is similar in conception to Retweets, but with many more event types ( _K_ = 5000). It considers the reuse of fixed phrases, or “memes,” in online media. It contains time-stamped instances of meme use in articles and posts from 1.5 million different blogs and news sites. We model how the future occurrence of a meme is affected by its past trajectory across different websites—that is, given one meme’s past trajectory across websites, when and where it will be mentioned again. 

On this dataset,<sup>7</sup> the advantage of our full neural models was dramatic, yielding cross-entropy per event of around _−_ 8 relative to the _−_ 15 of D-SM-MPP—which in turn is _far_ above the _−_ 800 of the 

> 6Our code and data are available at https://github.com/HMEIatJHU/neurawkes. 

> 7Data preparation details are given in Appendix C.6. 

7 



<!-- Start of picture text -->
0 N-SM-MPPD-SM-MPPSE-MPP 5 N-SM-MPPD-SM-MPPSE-MPP 500 N-SM-MPPD-SM-MPPSE-MPP 100 N-SM-MPPD-SM-MPP<br>6 0 10<br>10<br>500 20<br>20 7 1000 30<br>30 8 1500 40<br>50<br>40 9 2000 60<br>125 250 500 1000 2000 4000 8000 16000 125 250 500 1000 2000 4000 8000 16000 1000 2000 4000 8000 16000 32000 4000 8000 16000 32000<br>number of training sequences number of training sequences number of training sequences number of training sequences<br>log-likelihood per event log-likelihood per event log-likelihood per event log-likelihood per event<br><!-- End of picture text -->

Figure 2: Learning curve (with 95% error bars) of all three models on the Retweets (left two) and MemeTrack (right two) datasets. Our neural model significantly outperforms our decomposable model (right graph of each pair), and both significantly outperform the Hawkes process (left of each pair—same graph zoomed out). 



<!-- Start of picture text -->
2 2<br>0 0<br>2 2<br>4 4<br>6<br>6<br>8<br>8<br>10<br>10<br>10 8 6 4 2 0 2 10 8 6 4 2 0 2<br>N-SM-MPP N-SM-MPP<br>SE-MPP D-SM-MPP<br><!-- End of picture text -->

Figure 3: Scatterplots of N-SM-MPP vs. SE-MPP (left) and N-SM-MPP vs. D-SM-MPP (right), comparing the held-out log-likelihood of the two models (when trained on our full Retweets training set) with respect to _each_ of the 2000 test sequences. Nearly all points fall to the right of _y_ = _x_ , since N-SM-MPP (the neural Hawkes process) is consistently more predictive than our non-neural model and the Hawkes process. 



<!-- Start of picture text -->
1.0<br>1.2<br>1.4<br>1.6<br>1.8<br>2.0<br>2.0 1.8 1.6 1.4 1.2 1.0<br>N-SM-MPP<br>SE-MPP<br><!-- End of picture text -->

Figure 4: Scatterplot of N-SMMPP vs. SE-MPP, comparing their log-likelihoods with respect to _each_ of the 31 incomplete sequences’ test sets. All 31 points fall to the right of _y_ = _x_ . 

Hawkes process. Figure 2 illustrates the persistent gaps among the models. A scatterplot similar to Figure 3 is given in Figure 13 of Appendix C.6. We attribute the poor performance of the Hawkes process to its failure to capture the latent properties of memes, such as their topic, political stance, or interestingness. This is a form of missing data (section 1), as we now discuss. 

As the table in Appendix C.1 indicates, most memes in MemeTrack are uninteresting and give rise to only a short sequence of mentions. Thus the base mention probability is low. An ideal analysis would recognize that if a specific meme has been mentioned several times already, it is _a posteriori_ interesting and will probably be mentioned in future as well. The Hawkes process cannot distinguish the interesting memes from the others, except insofar as they appear on more influential websites. By contrast, our D-SM-MPP can partly capture this inferential pattern by using _negative_ base rates **_µ_** to create “inertia” (section 3.2.1). Indeed, all 5000 of its learned _µk_ parameters were negative, with values ranging from _−_ 10 to _−_ 30, which numerically yields 0 intensity and is hard to excite. 

An ideal analysis would also recognize that if a specific meme has appeared mainly on conservative websites, it is _a posteriori_ conservative and unlikely to appear on liberal websites in the future. The D-SM-MPP, unlike the Hawkes process, can again partly capture this, by having conservative websites _inhibit_ liberal ones. Indeed, 24% of its learned _α_ parameters were negative. (We re-emphasize that this inhibition is merely a predictive effect—probably not a direct causal mechanism.) 

And our N-SM-MPP process is even more powerful. The LSTM state aims to learn sufficient statistics for predicting the future, so it can learn hidden dimensions (which fall in ( _−_ 1 _,_ 1)) that encode useful posterior beliefs in boolean properties of the meme such as interestingness, conservativeness, timeliness, etc. The LSTM’s “long short-term memory” architecture explicitly allows these beliefs to persist indefinitely through time in the absence of new evidence, without having to be refreshed by redundant new events as in the decomposable models. Also, the LSTM’s hidden dimensions are computed by sigmoidal activation rather than softplus activation, and so can be used implicitly to perform logistic regression. The flat left side of the sigmoid resembles softplus and can model _inertia_ as we saw above: it takes several mentions to establish interestingness. Symmetrically, the flat right side can model _saturation_ : once the posterior probability of interestingness is at 80%, it cannot climb much farther no matter how many more mentions are observed. 

A final potential advantage of the LSTM is that in this large- _K_ setting, it has fewer parameters than the other models (Appendix C.3), sharing statistical strength across event types (websites) to generalize better. The learning curves in Figure 2 suggest that on small data, the decomposable 

8 

(non-neural) models may overfit their _O_ ( _K_<sup>2</sup> ) interaction parameters _αj,k_ . Our neural model only has to learn _O_ ( _D_<sup>2</sup> ) pairwise interactions among its _D_ hidden nodes (where _D ≪ K_ ), as well as _O_ ( _KD_ ) interactions between the hidden nodes and the _K_ event types. In this case, _K_ = 5000 but _D_ = 64. This reduction by using latent hidden nodes is analogous to nonlinear latent factor analysis. 

#### **6.3 Modeling Streams With Missing Data** 

We set up an artificial experiment to more directly investigate the missing-data setting of section 1, where we do not observe _all_ events during [0 _, T_ ], but train and test our model just as if we had. 

We sampled synthetic event sequences from a standard Hawkes process (just as in our pilot experiment from 6.1), removed all the events of selected types, and then compared the neural Hawkes process (N-SM-MPP) with the Hawkes process (SE-MPP) as models of these censored sequences. Since we took _K_ = 5, there were 2<sup>5</sup> _−_ 1 = 31 ways to construct a dataset of censored sequences. As shown in Figure 4, for _each_ of the 31 resulting datasets, training a neural Hawkes model achieves better generalization. Appendix A.4 discusses why this kind of behavior is to be expected. 

#### **6.4 Prediction Tasks—Medical, Social and Financial** 

To compare with Du et al. (2016), we evaluate our model on the _prediction_ tasks and datasets that they proposed. The Financial Transaction dataset contains long streams of high frequency stock transactions for a single stock, with the two event types “buy” and “sell.” The electrical medical records (MIMIC-II) dataset is a collection of de-identified clinical visit records of Intensive Care Unit patients for 7 years. Each patient has a sequence of hospital visit events, and each event records its time stamp and disease diagnosis. The Stack Overflow dataset represents two years of user awards on a question-answering website: each user received a sequence of badges (of 22 different types). 

We follow Du et al. (2016) and attempt to predict every held-out event ( _ki, ti_ ) from its history _Hi_ , evaluating the prediction _k_<sup>ˆ</sup> _i_ with 0-1 loss (yielding an error rate, or ER) and evaluating the prediction _t_ ˆ _i_ with L2 loss (yielding a root-mean-squared error, or RMSE). We make minimum Bayes risk predictions as explained in section 4. Figure 8 in Appendix C.7 shows that our model consistently outperforms that of Du et al. (2016) on event type prediction on all the datasets, although for time prediction neither model is consistently better. 

#### **6.5 Sensitivity to Number of Parameters** 

Does our method do well because of its flexible nonlinearities or just because it has more parameters? The answer is both. We experimented on the Retweets data with reducing the number of hidden units _D_ . Our N-SM-MPP substantially outperformed SE-MPP (the Hawkes process) on held-out data even with very few parameters, although more parameters does even better: 

|number of hidden units|Hawkes|1|2|4|8|16|32|256|
|---|---|---|---|---|---|---|---|---|
|number of parameters|21|31|87|283|1011|3811|14787|921091|
|log-likelihood|-7.19|-6.51|-6.41|-6.36|-6.24|-6.18|-6.16|-6.10|



We also tried halving _D_ across several datasets, which had negligible effect, always decreasing held-out log-likelihood by _<_ 0 _._ 2% relative. 

More information about model sizes is given in Appendix C.3. Note that the neural Hawkes process does not _always_ have more parameters. When _K_ is large, we can greatly reduce the number of params below that of a Hawkes process, by choosing _D ≪ K_ , as for MemeTrack in section 6.2. 

### **7 Conclusion** 

We presented two extensions to the multivariate Hawkes process, a popular generative model of streams of typed, timestamped events. Past events may now either excite _or_ inhibit future events. They do so by _sequentially_ updating the state of a novel _continuous-time_ recurrent neural network (LSTM). Whereas Hawkes sums the time-decaying influences of past events, we instead sum the time-decaying influences of the LSTM nodes. Our extensions to Hawkes aim to address real-world phenomena, missing data, and causal modeling. Empirically, we have shown that both extensions yield a significantly improved ability to predict the course of future events. There are several exciting avenues for further improvements (discussed in Appendix D), including embedding our model within a reinforcement learner to discover causal structure and learn an intervention policy. 

9 

### **Acknowledgments** 

We are grateful to Facebook for enabling this work through a gift to the second author. Nan Du kindly helped us by making his code public and answering questions, and the NVIDIA Corporation kindly donated two Titan X Pascal GPUs. We also thank our lab group at Johns Hopkins University’s Center for Language and Speech Processing for helpful comments. The first version of this work appeared on arXiv in December 2016. 

### **References** 

- Ciprian Chelba, Tomas Mikolov, Mike Schuster, Qi Ge, Thorsten Brants, Phillipp Koehn, and Tony Robinson. One billion word benchmark for measuring progress in statistical language modeling. _Computing Research Repository_ , arXiv:1312.3005, 2013. URL http://arxiv.org/abs/ 1312.3005. 

- Edward Choi, Nan Du, Robert Chen, Le Song, and Jimeng Sun. Constructing disease network and temporal progression model via context-sensitive Hawkes process. In _Data Mining (ICDM), 2015 IEEE International Conference on_ , pages 721–726. IEEE, 2015. 

- Nan Du, Mehrdad Farajtabar, Amr Ahmed, Alexander J Smola, and Le Song. Dirichlet-Hawkes processes with applications to clustering continuous-time document streams. In _Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 219–228. ACM, 2015a. 

- Nan Du, Yichen Wang, Niao He, Jimeng Sun, and Le Song. Time-sensitive recommendation from recurrent user activities. In _Advances in Neural Information Processing Systems (NIPS)_ , pages 3492–3500, 2015b. 

- Nan Du, Hanjun Dai, Rakshit Trivedi, Utkarsh Upadhyay, Manuel Gomez-Rodriguez, and Le Song. Recurrent marked temporal point processes: Embedding event history to vector. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 1555–1564. ACM, 2016. 

- Jalal Etesami, Negar Kiyavash, Kun Zhang, and Kushagra Singhal. Learning network of multivariate Hawkes processes: A time series approach. _arXiv preprint arXiv:1603.04319_ , 2016. 

- Manuel Gomez Rodriguez, Jure Leskovec, and Bernhard Sch¨olkopf. Structure and dynamics of information pathways in online media. In _Proceedings of the Sixth ACM International Conference on Web Search and Data Mining_ , pages 23–32. ACM, 2013. 

- Alex Graves. _Supervised Sequence Labelling with Recurrent Neural Networks_ . Springer, 2012. URL http://www.cs.toronto.edu/˜graves/preprint.pdf. 

- Alex Graves, Navdeep Jaitly, and Abdel-rahman Mohamed. Hybrid speech recognition with deep bidirectional LSTM. In _Automatic Speech Recognition and Understanding (ASRU), 2013 IEEE Workshop on_ , pages 273–278. IEEE, 2013. 

- Fangjian Guo, Charles Blundell, Hanna Wallach, and Katherine Heller. The Bayesian echo chamber: Modeling social influence via linguistic accommodation. In _Proceedings of the Eighteenth International Conference on Artificial Intelligence and Statistics_ , pages 315–323, 2015. 

- Alan G Hawkes. Spectra of some self-exciting and mutually exciting point processes. _Biometrika_ , 58(1):83–90, 1971. 

- Xinran He, Theodoros Rekatsinas, James Foulds, Lise Getoor, and Yan Liu. Hawkestopic: A joint model for network inference and topic modeling from text-based cascades. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 871–880, 2015. 

- Sepp Hochreiter and J¨urgen Schmidhuber. Long short-term memory. _Neural computation_ , 9(8): 1735–1780, 1997. 

- Andrej Karpathy, Justin Johnson, and Li Fei-Fei. Visualizing and understanding recurrent networks. _arXiv preprint arXiv:1506.02078_ , 2015. 

10 

- Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2015. 

- Young Lee, Kar Wai Lim, and Cheng Soon Ong. Hawkes processes with stochastic excitations. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2016. 

- Jure Leskovec and Andrej Krevl. SNAP Datasets: Stanford large network dataset collection. http: //snap.stanford.edu/data, June 2014. 

- Peter A Lewis and Gerald S Shedler. Simulation of nonhomogeneous Poisson processes by thinning. _Naval Research Logistics Quarterly_ , 26(3):403–413, 1979. 

- Thomas Josef Liniger. _Multivariate Hawkes processes_ . Diss., Eidgen¨ossische Technische Hochschule ETH Z¨urich, Nr. 18403, 2009, 2009. 

- Michal Lukasik, PK Srijith, Duy Vu, Kalina Bontcheva, Arkaitz Zubiaga, and Trevor Cohn. Hawkes processes for continuous time sequence classification: An application to rumour stance classification in Twitter. In _Proceedings of 54th Annual Meeting of the Association for Computational Linguistics_ , pages 393–398, 2016. 

- Tomas Mikolov, Martin Karafi´at, Luk´as Burget, Jan Cernock´y, and Sanjeev Khudanpur. Recurrent neural network based language model. In _INTERSPEECH 2010, 11th Annual Conference of the International Speech Communication Association, Makuhari, Chiba, Japan, September 26-30, 2010_ , pages 1045–1048, 2010. 

- C. Palm. _Intensit¨atsschwankungen im Fernsprechverkehr_ . Ericsson technics, no. 44. L. M. Ericcson, 1943. URL https://books.google.com/books?id=5cy2NQAACAAJ. 

- Judea Pearl. Causal inference in statistics: An overview. _Statistics Surveys_ , 3:96–146, 2009. 

- Martin Sundermeyer, Hermann Ney, and Ralf Schluter. LSTM neural networks for language modeling. _Proceedings of INTERSPEECH_ , 2012. 

- Yichen Wang, Bo Xie, Nan Du, and Le Song. Isotonic Hawkes processes. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2016. 

- Shuai Xiao, Mehrdad Farajtabar, Xiaojing Ye, Junchi Yan, Xiaokang Yang, Le Song, and Hongyuan Zha. Wasserstein learning of deep generative point process models. In _Advances in Neural Information Processing Systems 30_ , 2017a. 

- Shuai Xiao, Junchi Yan, Mehrdad Farajtabar, Le Song, Xiaokang Yang, and Hongyuan Zha. Joint modeling of event sequence and time series with attentional twin recurrent neural networks. _arXiv preprint arXiv:1703.08524_ , 2017b. 

- Hongteng Xu, Mehrdad Farajtabar, and Hongyuan Zha. Learning Granger causality for Hawkes processes. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2016. 

- Shuang-hong Yang and Hongyuan Zha. Mixture of mutually exciting processes for viral diffusion. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 1–9, 2013. 

- Omar F. Zaidan and Jason Eisner. Modeling annotators: A generative approach to learning from annotator rationales. In _Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 31–40, 2008. 

- Qingyuan Zhao, Murat A Erdogdu, Hera Y He, Anand Rajaraman, and Jure Leskovec. Seismic: A self-exciting point process model for predicting tweet popularity. In _Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , pages 1513–1522. ACM, 2015. 

- Ke Zhou, Hongyuan Zha, and Le Song. Learning triggering kernels for multi-dimensional Hawkes processes. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 1301–1309, 2013. 

11 

# **Appendices** 

### **A Model Details** 

In this appendix, we discuss some qualitative properties of our models and give details about how we handle boundary conditions. 

#### **A.1 Discussion of the Transfer Function** 

As explained in section 3.2, when we allow _inhibition_ and _inertia_ , we need to pass the total activation through a non-linear **transfer function** _f_ : R _→_ R+ to obtain a positive intensity function. This was our equation (3a), namely _λk_ ( _t_ ) = _f_ ( _λ_<sup>˜</sup> _k_ ( _t_ )). 

What non-linear function _f_ should we use? The ReLU function _f_ ( _x_ ) = max( _x,_ 0) seems at first a natural choice. However, it returns 0 for negative _x_ ; we need to keep our intensities strictly positive at all times when an event could possibly occur, to avoid infinitely bad log-likelihood at training time or infinite log-loss at test time. 

A better choice would be the “softplus” function _f_ ( _x_ ) = log(1 + exp( _x_ )), which is strictly positive and approaches ReLU when _x_ is far from 0. Unfortunately, “far from 0” is defined in units of _x_ , so this choice would make our model sensitive to the units used to measure time. For example, if we switch the units of _t_ from seconds to milliseconds, then the base intensity _f_ ( _µk_ ) must become 1000 times lower, forcing _µk_ to be very negative and thus creating a much stronger inertial effect. 

To avoid this problem, we introduce a scale parameter _s >_ 0 and define _f_ ( _x_ ) = _s_ log(1+exp( _x/s_ )). The scale parameter _s_ controls the curvature of _f_ ( _x_ ), which approaches ReLU as _s →_ 0, as shown in Figure 5. We can regard _f_ ( _x_ ), _x_ , and _s_ as rates, with units of inverse time, so that _f_ ( _x_ ) _/s_ and _x/s_ are unitless quantities related by softplus. We actually learn a separate scale parameter _sk_ for each event type _k_ , which will adapt to the rate of events of that type. 



<!-- Start of picture text -->
2.0<br>soft-plus<br>ReLU<br>s=0.1<br>1.5 s=0.5<br>s=1.5<br>1.0<br>0.5<br>0.0<br>3 2 1 0 1 2<br>activation<br>intensity<br><!-- End of picture text -->

Figure 5: The softplus function is a soft approximation to a rectified linear unit (ReLU), approaching it as _x_ moves away from 0. We use it to ensure a strictly positive intensity function. We incorporate a scale parameter _s_ that controls the curvature. 

#### **A.2 Boundary Conditions for the LSTM** 

We initialize the continuous-time LSTM’s hidden state to **h** (0) = **0** , and then have it read a special beginning-of-stream (BOS) event ( _k_ 0 _, t_ 0), where _k_ 0 is a special event type (i.e., expanding the 

12 

LSTM’s input dimensionality by one) and _t_ 0 is set to be 0. Then equations (5)–(6) define **c** 1 (from **c** 0 =def **0** ), ¯ **c** 1, **_δ_** 1, and **o** 1. This is the initial configuration of the system as it waits for the first event to happen: this initial configuration determines the hidden state **h** ( _t_ ) and the intensity functions _λk_ ( _t_ ) over _t ∈_ (0 _, t_ 1] 

We do not generate the BOS event but only condition on it, which is why the log-likelihood formula (section 2) only sums over _i_ = 1 _,_ 2 _, . . ._ . This design is well-suited to various settings. In some settings, time 0 is special. For example, if we release children into a carnival and observe the stream of their actions there, then BOS is the release event and no other events can possibly precede it. In other settings, data before time 0 are simply missing, e.g., the observation of a patient starts in midlife; nonetheless, BOS in this case usefully indicates the beginning of the _observed_ sequence. In both kinds of settings, the initial configuration just after reading BOS characterizes the model’s belief about the unknown state of the true system just after time 0, as it waits for event 1. Computing the initial configuration by explicitly transitioning on BOS ensures that the initial hidden state **h** (0<sup>+</sup> ) =def lim _t→_ 0+ **h** ( _t_ ) falls in the space of hidden states achievable by LSTM transitions. More important, in future work, we will be able to attach metadata about the sequence as a “mark” to the BOS event (see footnote 13), and the LSTM can learn how these metadata affect the initial configuration. 

To allow finite streams, we could optionally choose to identify one of the observable types in _{_ 1 _,_ 2 _, . . . , K}_ as a special end-of-stream (EOS) event after which the stream cannot possibly continue. If the model generates EOS, all intensities are permanently forced to 0—the LSTM is no longer consulted, so it is not necessary for the model parameters to explain why no further events are observed on the interval [0 _, T_ ]: that is, the second term of equation (1) can be omitted. The integral in equation (8) should therefore be taken from _t_ = 0 to the time of the EOS event or _T_ , whichever is smaller. 

#### **A.3 Closure Under Superposition** 

Decomposable models have the nice property that they are closed under superposition of event streams. Let _E_ and _E_<sup>_′_</sup> be random event streams, on a common time interval [0 _, T_ ] but over disjoint sets of event types. If each stream is distributed according to a Hawkes process, then their superposition—that is, _E ∪E_<sup>_′_</sup> sorted into temporally increasing order—is also distributed according to a Hawkes process. It is easy to exhibit parameters for such a process, using a block-diagonal matrix of _αj,k_ so that the two sets of event types do not influence each other. The closure property also holds for our decomposable self-modulating process, and for the same simple reason. 

This is important since in various real settings, some event types tend not to interact. For example, the activities of two people Jay and Kay rarely influence each other,<sup>8</sup> although they are simultaneously monitored and thus form a single observed stream of events. We want our model to handle such situations naturally, rather than insisting that Kay always reacts to what Jay does. 

Thus, as section 3.2.2 noted, we have designed our neurally self-modulating process to preserve this ability to insulate event _k_ from event _j_ . By setting specific elements of **w** _k_ to 0, one could ensure that the intensity function _λk_ ( _t_ ) depends on only a subset _S_ of the LSTM hidden nodes. Then by setting specific LSTM parameters, one would make the nodes in _S_ insensitive to events of type _j_ : events of type _j_ should open these nodes’ forget gates ( **f** = **1** ) and close their input gates ( **i** = **0** )— as section 3.2.2 suggested—so that their cell memories **c** ( _t_ ) and hidden states **h** ( _t_ ) do not change at all but continue decaying toward their previous steady-state values.<sup>9</sup> Now events of type _j_ cannot affect the intensity _λk_ ( _t_ ). 

For example, the hidden states in _S_ are affected in the same way when the LSTM reads ( _k,_ 1) _,_ ( _j,_ 3) _,_ ( _j,_ 8) _,_ ( _k,_ 12) as when it reads ( _k,_ 1) _,_ ( _k,_ 12), even though the intervals ∆ _t_ between successive events are different. In other words, the architecture “knows” that 2 + 5 + 4 = 11. The simplicity of this solution is a consequence of how our design does not encode the time intervals 

> 8Their surnames might be Box and Cox, after the 19th-century farce about a day worker and a night worker unknowingly renting the same room. But any pair of strangers would do. 

> 9To be precise, we can achieve this arbitrarily closely, but not exactly, because a standard LSTM gate cannot be fully opened or closed. The openness is traditionally given by a sigmoid function and so falls in (0 _,_ 1), never achieving 1 or 0 exactly unless we are willing to set parameters to _±∞_ . In practice this should not be an issue because relatively small weights can drive the sigmoid function extremely close to 1 and 0—in fact, _σ_ (37) = 1 in 64-bit floating-point arithmetic. 

13 

numerically, but only reacts to these intervals indirectly, through the interaction between the timing of events and the spontaneous decay of the hidden states. The memory cells of _S_ decay for a total duration of 11 between the two _k_ events, even if that interval has been divided into subintervals 2 + 5 + 4. 

With this method, we can explicitly construct a superposition process with LSTM state space R<sup>_d_+</sup><sup>_d′_</sup> —the cross product of the state spaces R<sup>_d_</sup> and R<sup>_d′_</sup> of the original processes—in which Kay’s events are not influenced at all by Jay’s. 

If we know _a priori_ that particular event types interact only weakly, we can impose an appropriate prior on the neural Hawkes parameters. And in future work with large _K_ , we plan to investigate the use of sparsity-inducing regularizers during parameter estimation, to create an inductive bias toward models that have limited interactions, without specifying which particular interactions are present. 

Superposition is a formally natural operation on event streams. It barely arises for ordinary sequence models, such as language models, since the superposition of two sentences is not well-defined unless all of the words carry distinct real-valued timestamps. However, there is an analogue from formal language theory. The “shuffle” of two sentences is defined to be the set of _possible_ interleavings of their words—i.e., the set of superpositions that could result from assigning increasing timestamps to the words of each sentence, without duplicates. It is a standard exercise to show that regular languages are closed under shuffle. This is akin to our remark that neural-Hawkes-distributed random variables are closed under superposition, and indeed uses a similar cross-product construction on the finite-state automata. An important difference is that the shuffle construction does not require disjoint alphabets in the way that ours requires disjoint sets of event types. This is because finite-state automata allow nondeterministic state transitions and our processes do not. 

#### **A.4 Missing Data Discussion** 

We discussed the case of missing data in section 1. Supppose the true complete-data distribution _p_<sup>_∗_</sup> is itself an unknown neural Hawkes process. As section 1 pointed out, a sufficient statistic for prediction from the incompletely observed past would be the posterior distribution over the true hidden neural state **t** of the unknown process, which was reached by reading the _complete_ past. We would ideally obtain our predictions by correctly modeling the missing observations and integrating over them. However, inference would be computationally quite expensive even if _p_<sup>_∗_</sup> were known, to say nothing of the case where _p_<sup>_∗_</sup> is unknown and we must integrate over its parameters as well. 

We instead train a neural model that attempts to bypass these problems. The hope is that our model’s hidden state, after it reads only the observed _incomplete_ past, will be nearly as predictive as the posterior distribution above. 

We can illustrate the goal with reference to the experiment in section 6.3. There, the true completedata distribution _p_<sup>_∗_</sup> happened to be a classical Hawkes process, but we censored some event types. We then modeled the observed incomplete sequence as if it were a complete sequence. In this setting, a Hawkes process will in general be unable to fit the data well, which is why the neural Hawkes process has an advantage in all 31 experiments. 

What goes wrong with using the Hawkes model? Suppose that in the true Hawkes model _p_<sup>_∗_</sup> , type 1 is rare but strongly excites type 2 and type 3, which do not excite themselves or each other. Type 1 events are missing in the observed sequence. 

What is the correct predictive distribution in this situation (with knowledge of _p_<sup>_∗_</sup> )? Seeing lots of type 2 events in a row suggests that they were preceded by a (single) missing type 1 event, which predicts a higher intensity for type 3 in future. The more type 2 events we see, the surer we are that there was a type 1 event, but we doubt that there were multiple type 1 events, so the predicted intensity of type 3 is expected to increase sublinearly as _P_ (type = 1) approaches 1. 

As neural networks are universal function approximators , a neural Hawkes model may be able to recognize and fit this sublinear behavior in the incomplete training data. However, if we fit only a Hawkes model to the incomplete training data, it would have to posit that type 2 excites type 3 directly, so the predicted intensity of type 3 would incorrectly increase linearly with the number of type 2 events. 

14 

### **B Algorithmic Details** 

In this appendix, we elaborate on the details of algorithms. 

#### **B.1 Likelihood Function** 

For the proposed models, given complete observations of an event stream over the time interval [0 _, T_ ], the log-likelihood of the parameters turns out to be given by the simple formula shown in section 4. We start by giving the full derivation of that formula, repeated here: 



First, we define _N_ ( _t_ ) = _|{h_ : _th ≤ t}|_ to be the count of events (of any type) preceding time _t_ . So given the past history _Hi_ , the number of events in ( _ti−_ 1 _, t_ ] is denoted as ∆ _N_ ( _ti−_ 1 _, t_ ) =def _N_ ( _t_ ) _− N_ ( _ti−_ 1). Let _Ti > ti−_ 1 be the random variable of the next event time and let _Ki_ +1 be the random variable of the next event type. The cumulative distribution function and probability density function of _Ti_ (conditioned on _Hi_ ) are given by: 











where Λ( _t_ ) = �0 _t_<sup>_λ_(</sup><sup>_s_)</sup><sup>_ds_and</sup><sup>_λ_(</sup><sup>_t_) = �</sup> _k_<sup>_K_</sup> =1<sup>_λk_(</sup><sup>_t_).</sup> 

Moreover, given the past history _Hi_ and the next event time _ti_ , the distribution of _ki_ is given by: 



Therefore, we can derive the likelihood function as follows: 



and 



#### **B.2 Monte Carlo Gradient and Training Speed** 

We can locally maximize the log-likelihood _ℓ_ from equation (8) using any stochastic gradient method. For this, we need to be able to get an unbiased estimate of the gradient _∇ℓ_ with respect to the model parameters. This is straightforward to obtain by back-propagation. The trick 

15 

**Algorithm 1** Integral Estimation (Monte Carlo) **Input:** interval [0 _, T_ ]; model parameters and events ( _k_ 1 _, t_ 1) _, . . ._ for determining _λj_ ( _t_ ) Λ _←_ 0; _∇_ Λ _←_ **0 for** _N_ samples : _▷ e.g., take N >_ 0 _proportional to T_ draw _t ∼_ Unif(0 _, T_ ) **for** _j ←_ 1 **to** _K_ : Λ += _λj_ ( _t_ ) _▷ via current model parameters ∇_ Λ += _∇λj_ ( _t_ ) _▷ via back-propagation_ Λ _← T_ Λ _/N_ ; _∇_ Λ _← T ∇_ Λ _/N ▷ weight the samples_ **return** (Λ _, ∇_ Λ) 

for handling the integral in equation (8) is that the single function evaluation _Tλ_ ( _t_ ) at a random _t ∼_ Unif(0 _, T_ ) gives an unbiased estimate of the entire integral—that is, its expected value is Λ. Its gradient via back-propagation is therefore a unbiased estimate of _∇_ Λ (since gradient commutes with expectation). The Monte Carlo algorithm in Algorithm 1 averages over several samples to reduce the variance of this noisy estimator. 

Each step of Adam training computes the gradient on a training sequence. With _P_ params, this takes time _O_ ( _IP_ ) for Hawkes and _O_ (( _I_ + _M_ ) _P_ ) for neural Hawkes, if _I_ is the number of observed events and _M_ is the number of samples used to estimate the integral. We take _M_ = _O_ ( _I_ ) in practice (see Appendix C.2), so we have runtime _O_ ( _IP_ ) like Hawkes. 

Note that our stochastic gradient is unbiased for any _M_ ; large _M_ merely reduces its variance. The gradient for the Hawkes process has 0 variance, since it has analytical form and does not require sampling at all. 

#### **B.3 Thinning Algorithm for Sampling Sequences** 

If we wish to draw sequences from the self-modulating models of 3.2, we can adopt the thinning algorithm (Lewis and Shedler, 1979; Liniger, 2009) that is commonly used for the multivariate Hawkes process, as shown in Algorithm 2. We explain the algorithm here and illustrate its conception in Figure 6. 

Suppose we have already sampled the first _i −_ 1 events. The _K_ event types are now in a race to see who generates the next event. (Typically, the winning type will have relatively high intensity.) In our model, that next event will join the multivariate event stream as ( _ki, ti_ ), whereupon it updates the LSTM state and thus modulates the subsequent intensities that will be used to sample event _i_ + 1. 

How do we conduct the race? For each event type _k_ , let the function _λ_<sup>_i_</sup> _k_<sup>:(</sup><sup>_ti−_1</sup><sup>_, ∞_)</sup><sup>_→_R</sup><sup>_≥_0map</sup> each time _t_ to the intensity _λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_) that our model will define at time</sup><sup>_t_provided that event</sup><sup>_i_has not yet</sup> happened in the interval ( _ti−_ 1 _, t_ ). For each _k_ independently, we draw the time _ti,k_ of the next event from the non-homogeneous Poisson process over ( _ti−_ 1 _, ∞_ ) whose intensity function is _λ_<sup>_i_</sup> _k_<sup>.We then</sup> take _ti_ = min _k ti,k_ and _ki_ = argmin _k ti,k_ . That is, we keep just the earliest of the _K_ events. We cannot keep the rest because they are not correctly distributed according to the new intensities as updated by the earliest event. 

But how do we draw the next event time _ti,k_ from the non-homogeneous Poisson process given by _λ_<sup>_i_</sup> _k_<sup>?Recallfrom3.1thatadrawfromsuchapointprocessisactuallyawhole</sup><sup>_set_oftimesin</sup> ( _ti−_ 1 _, ∞_ ): we will take _ti,k_ to be the earliest of these. In theory, this set is drawn by _independently_ choosing at each time _t ∈_ ( _ti−_ 1 _, ∞_ ), with infinitesimal probability proportional to _λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_),whether</sup> an event occurs. One could do this by _independently_ applying rejection sampling at each time _t_ : choose with larger probability _λ_<sup>_∗_</sup> whether a “proposed event” occurs at time _t_ , and if it does, accept the proposed event with probability only _λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_)</sup><sup>_/λ∗≤_1.This is equivalent to simultanously</sup> drawing a set of proposed times from a _homogenous_ Poisson process with constant rate _λ_<sup>_∗_</sup> , and then “thinning” that proposed set, as illustrated in Figure 6. This approach helps because it is easy to draw from the homogenous process: the intervals between successive proposed events are IID Exp( _λ_<sup>_∗_</sup> ), so it is easy to sample the events in sequence. The inner **repeat** loop in Algorithm 2 lazily carries out just enough of this infinite homogenous draw from _λ_<sup>_∗_</sup> to determine the time _ti,k_ of the earliest _accepted_ event, which is the earliest event in the non-homogeneous draw from _λ_<sup>_i_</sup> _k_<sup>, as desired.</sup> 

16 



<!-- Start of picture text -->
Intensity Intensity Intensity<br>Time Time Time<br><!-- End of picture text -->

Figure 6: Sampling the next event, using the same visual notation as in Figure 1. The _x_ axis shows a prefix of the infinite interval ( _ti−_ 1 _,∞_ ). In the first graph, _gold_ events are proposed from a homogeneous Poisson process with intensity _λ_<sup>_∗_</sup> (gold straight line). In the second graph, the purple curve _λ_<sup>_i_</sup> 1<sup>randomly accepts some</sup> of these gold events, with probability _λ_<sup>_i_</sup> 1<sup>(</sup><sup>_t_)</sup><sup>_/λ∗_for the event at time</sup><sup>_t_; here it accepts three of the ones shown</sup> and rejects the others. In the third graph, the surviving type-1 events (purple squares) are interleaved with the surviving type-2 events (green pentagons). The next event is the earliest one among these surviving candidates. In practice, these sequences are constructed lazily so that we find only the earliest surviving event of each type. This is possible because the inter-arrival times between gold proposed events are distributed as Exp( _λ_<sup>_∗_</sup> ), making it straightforward to enumerate any finite prefix of a random infinite gold sequence. 

#### **Algorithm 2** Data Simulation (thinning algorithm) 

**Input:** interval [0 _, T_ ]; model parameters _t_ 0 _←_ 0; _i ←_ 1 **while** _ti−_ 1 _< T_ : _▷ draw event i, as it might fall in [0,T]_ **for** _k_ = 1 **to** _K_ : _▷ draw “next” event of each type_ find upper bound _λ_<sup>_∗_</sup> _≥ λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_) for all</sup><sup>_t ∈_(</sup><sup>_ti−_1</sup><sup>_, ∞_)</sup> _t ← ti−_ 1 **repeat** draw ∆ _∼_ Exp( _λ_<sup>_∗_</sup> ), _u ∼_ Unif(0 _,_ 1) _t_ += ∆ _▷ time of next proposed event_ **until** _uλ_<sup>_∗_</sup> _≤ λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_)</sup> _▷ accept proposal with prob λλ_<sup>_i_</sup> _<u>k</u>_<sup><u>(</u></sup><sup>_<u>∗t</u>_</sup><sup><u>)</u></sup> _ti,k ← t ti ←_ min _k ti,k_ ; _ki ←_ argmin _k ti,k ▷ earliest event wins i ← i_ + 1 **return** ( _k_ 1 _, t_ 1) _, . . ._ ( _ki−_ 1 _, ti−_ 1) 

Finally, how do we construct the upper bound _λ_<sup>_∗_</sup> on _λ_<sup>_i_</sup> _k_<sup>?Recallthatbothofourself-modulating</sup> models (equations (3a) and (4a)) define _λ_<sup>_i_</sup> _k_<sup>=</sup><sup>_fk_(˜</sup><sup>_λi_</sup> _k_<sup>), where</sup><sup>_fk_is monotonically non-decreasing. In</sup> both cases, _λ_<sup>˜</sup><sup>_i_</sup> _k_<sup>is a sum of</sup><sup>_bounded_functions on (</sup><sup>_ti−_1</sup><sup>_, ∞_) (equations (3b) and (4)).In other words,</sup> we can express _λ_<sup>˜</sup><sup>_i_</sup> _k_<sup>(</sup><sup>_t_) as</sup><sup>_µ_+</sup><sup>_g_1(</sup><sup>_t_) +</sup><sup>_· · ·_+</sup><sup>_gn_(</sup><sup>_t_).We can therefore replace each</sup><sup>_g_function by its</sup> upper bound to obtain _λ_<sup>_∗_</sup> = _fk_ ( _µ_ + max _t g_ 1( _t_ ) + _· · ·_ + max _t gn_ ( _t_ )), in which the argument to _fk_ is a finite constant. 

Specifically, in equation (3b), each summand _αkh,k_ exp( _−δkh,k_ ( _t − ti_ )) is upper-bounded by max( _αkh,k,_ 0). In equation (4), each summand _wkdhd_ ( _t_ ) = _wkd · oid ·_ (2 _σ_ (2 _cd_ ( _t_ )) _−_ 1) is upperbounded by max _c∈{cid,c_ ¯ _id} wkd · oid ·_ (2 _σ_ (2 _c_ ) _−_ 1). Note that the coefficients _αki,k_ and _wkd_ may be either positive or negative. 

While Algorithm 2 is classical and intuitive, we also implemented a more efficient variant. Instead of drawing the next event from each of _K different_ non-homogeneous Poisson processes and keeping the earliest, we can construct a _single_ non-homogenous Poisson process with aggregate intensity function _λ_<sup>_i_</sup> ( _t_ ) =<sup>�</sup><sup>_K_</sup> _k_ =1<sup>_λ_</sup> _k_<sup>_i_(</sup><sup>_t_)over(</sup><sup>_ti−_1</sup><sup>_, ∞_).Anupperbound</sup><sup>_λ∗_onthisaggregatefunctioncan</sup> be obtained by summing the upper bounds on the individual _λ_<sup>_i_</sup> _k_<sup>functions.We then use the thinning</sup> algorithm only to sample the next event time _ti_ from this aggregate process _λ_<sup>_i_</sup> . Finally, we “disaggregate” by choosing _ki_ from the distribution _p_ ( _k | ti_ ) = _λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_ti_)</sup><sup>_/λi_(</sup><sup>_ti_).10This is equivalent to</sup> Algorithm 2. In terms of Figure 6, this more efficient version enumerates a gold sequence that is the union of the _K_ gold sequences, and stops with the first accepted gold event. Thus, whereas Figure 6 

> 10In practice, acceptance and disaggregation can be combined into a single step. That is, each successive event _t_ proposed from the homogeneous Poisson( _λ_<sup>_∗_</sup> ) process is either kept as type _k_ , with probability _λ_<sup>_i_</sup> _k_<sup>(</sup><sup>_t_)</sup><sup>_/λ∗_, or rejected, with probability 1</sup><sup>_−λi_(</sup><sup>_t_)</sup><sup>_/λ∗_.If it is accepted, we have found our next event (</sup><sup>_ki, ti_).</sup> If it is rejected, we increment _t_ by ∆ _∼_ Exp( _λ_<sup>_∗_</sup> ) to get the next proposed event. 

17 

|DATASET|_K_|# OF|EVENTTOKEN|S|SEQU|ENCELE|NGTH|
|---|---|---|---|---|---|---|---|
|||TRAIN|DEV|TEST|MIN|MEAN|MAX|
|SYNTHETIC|5|_≈_480449|_≈_60217|_≈_60139|20|_≈_60|100|
|RETWEETS|3|1739547|215521|218465|50|109|264|
|MEMETRACK|5000|93267|14932|15440|1|3|31|
|MIMIC-II|75|_≈_1946|_≈_228|_≈_245|2|4|33|
|STACKOVERFLOW|22|_≈_343998|_≈_39247|_≈_97168|41|72|736|
|FINANCIAL|2|_≈_298710|_≈_33190|_≈_82900|829|2074|3319|



Table 1: Statistics of each dataset. We write “ _≈ N_ ” to indicate that _N_ is the average value over multiple splits of one dataset (MIMIC-II, Stack Overflow, Financial Transaction); the variance is small in each such case. 

|DATASET|_K_|_D_|# OF|MODELPARAME|TERS|
|---|---|---|---|---|---|
||||SE-MPP|D-SM-MPP|N-SM-MPP|
|SYNTHETIC|5|256|55|60|922117|
|RETWEETS|3|256|21|24|921091|
|MEMETRACK|5000|64|50005000|50010000|702856|



Table 2: Size of each trained model on each dataset. The number of parameters of neural Hawkes process is followed by the number of hidden nodes _D_ in its LSTM (chosen automatically on dev data). 

had to propose two type-1 events in order to get the first accepted type-1 event (the leftmost purple event), the more efficient version would not have had to spend time proposing either of those, because an earlier proposed event (the leftmost green event) had already been accepted and determined to be of type 2. 

### **C Experimental Details** 

In this appendix, we elaborate on the details of data generation, processing, and experimental results. 

#### **C.1 Dataset Statistics** 

Table 1 shows statistics about each dataset that we use in this paper. 

#### **C.2 Training Details** 

We used a single-layer LSTM (Graves, 2012) in section 3.2.2, selecting the number of hidden nodes from a small set _{_ 64 _,_ 128 _,_ 256 _,_ 512 _,_ 1024 _}_ based on the performance on the dev set of each dataset. We empirically found that the model performance is robust to these hyperparameters. 

When estimating integrals with Monte Carlo sampling, _N_ is the number of sampled negative observations in Algorithm 1, while _I_ is the number of positive observations. In practice, setting _N_ = _I_ was large enough for stable behavior, and we used this setting during training. For evaluation on dev and test data, we took _N_ = 10 _I_ for extra accuracy, or _N_ = _I_ when _I_ was very large. 

For learning, we used the Adam algorithm with its default settings (Kingma and Ba, 2015). Adam is a stochastic gradient optimization algorithm that continually adjusts the learning rate in each dimension based on adaptive estimates of low-order moments. Our training objective was unregularized log-likelihood.<sup>11</sup> We initialized the Hawkes process parameters and _sk_ scale factors to 1, and all other non-LSTM parameters (section 3.2.2) to small random values from _N_ (0 _,_ 0 _._ 01). We performed early stopping based on log-likelihood on the held-out dev set. 

> 11L2 regularization did not appear helpful in pilot experiments, at least for our dataset size and when sharing a single regularization coefficient among all parameters. 

18 



<!-- Start of picture text -->
1.360 1.245<br>0.98<br>1.365 1.250<br>1.00<br>1.370 1.255 1.02<br>1.375 1.260 1.04<br>1.380<br>1.265 1.06<br>1.385<br>1.270 1.08<br>0.455<br>0.110 0.270<br>0.450<br>0.105 0.445<br>0.265<br>0.440<br>0.100<br>0.260 0.435<br>0.095 0.430<br>0.255 0.425<br>0.090<br>0.420<br>1.468<br>1.43<br>0.002 1.516<br>1.44<br>0.004 1.518 1.45<br>1.46<br>0.006 1.520 1.47<br>1.48<br>0.008 1.522<br>1.49<br>0.010 1.524 1.50<br><!-- End of picture text -->

Figure 7: Log-likelihood (reported in nats per event) of each model on held-out synthetic data. Rows (top-down) are log-likelihood on the entire sequence, time interval, and event type. On each row, the figures (from left to right) are datasets generated by SE-MPP, D-SM-MPP and N-SM-MPP. In each figure, the models (from left to right) are Oracle, SE-MPP, D-SM-MPP and N-SM-MPP. Larger values are better. Note that log-likelihood for continuous variables can be positive, since it uses the log of a probability density that may be _>_ 1. 

#### **C.3 Model Sizes** 

The size of each trained model on each dataset is shown in Table 2. Our neural model has many parameters for expressivity, but it actually has considerably fewer parameters than the other models in the large- _K_ setting (MemeTrack). 

#### **C.4 Pilot Experiments on Simulated Data** 

Our hope is that the neural Hawkes process is a flexible tool that can be used to fit naturally occurring data. As mentioned in section 6.1, we first checked that we could successfully fit data generated from _known_ distributions. That is, when the generating distribution actually fell within our model family, could our training procedure recover the distribution in practice? When the data came from a decomposable process, could we nonetheless train our neural process to fit the distribution well? 

We used the thinning algorithm (Appendix B.3) to sample event streams from different processes with randomly generated parameters: (a) a standard Hawkes process (SE-MPP, section 3.1), (b) our decomposable self-modulating process (D-SM-MPP, section 3.2.1), (c) our neural self-modulating processes (N-SM-MPP, section 3.2.2). We then tried to fit each dataset with all these models.<sup>12</sup> 

The results are shown in Figure 7. We found that all models were able to fit the (a) and (b) datasets well with no statistically significant difference among them, but that the (c) models were substantially and significantly better at fitting the (c) datasets. In all cases, the (c) models were able to obtain a low KL divergence from the true generating model (the difference from the oracle column). This result suggests that the neural Hawkes process may be a wise choice: it introduces extra expressive power that is sometimes necessary and does not appear (at least in these experiments) to be harmful when it is not necessary. 

> 12Details of data generation can be found in Appendix C.4. 

19 

We used Algorithm 2 to sample event streams from three different processes with randomly generated parameters: (a) a standard Hawkes process (SE-MPP), (b) our decomposable self-modulating process (D-SM-MPP), (c) our neural self-modulating processes (N-SM-MPP). We then tried to fit each dataset with all these models. 

For each dataset, we took _K_ = 5 as the number of event types. To generate each event sequence, we first chose the sequence length _I_ (number of event tokens) uniformly from _{_ 20 _,_ 21 _,_ 22 _, . . . ,_ 100 _}_ and then used the thinning algorithm to sample the first _I_ events over the interval [0 _, ∞_ ). For subsequent training or testing, we treated this sequence (appropriately) as the complete set of events observed on the interval [0 _, T_ ] where _T_ = _tI_ , the time of the last generated event. For each dataset, we generate 8000, 1000 and 1000 sequences for the training, dev, and test sets respectively. 

For SE-MPP, we sampled the parameters as _µk ∼_ Unif[0 _._ 0 _,_ 1 _._ 0], _αj,k ∼_ Unif[0 _._ 0 _,_ 1 _._ 0], and _δj,k ∼_ Unif[10 _._ 0 _,_ 20 _._ 0]. The large decay rates _δj,k_ were needed to prevent the intensities from blowing up as the sequence accumulated more events. For D-SM-MPP, we sampled the parameters as _µk ∼_ Unif[ _−_ 1 _._ 0 _,_ 1 _._ 0], _αj,k ∼_ Unif[ _−_ 1 _._ 0 _,_ 1 _._ 0], and _δj,k ∼_ Unif[10 _._ 0 _,_ 20 _._ 0]. For N-SM-MPP, we sampled parameters from Unif[ _−_ 1 _._ 0 _,_ 1 _._ 0]. 

The results are shown in Figure 7, including log-likelihood (reported in nats per event) on the sequences and the breakdown of time interval and event types. 

Another interesting question is whether the trained neural Hawkes model accurately predicts the real-valued _intensities_ , since for the synthetic data we actually know the intensities. This is a more direct evaluation of whether the model is accurately recovering the dynamics of the underlying generative process. Here we compared only SE-MPP and N-SM-MPP. 

All types behaved similarly, so we report only averages over the _K_ types. For both processes (a) and (c), the true intensity’s variance was about 30% of the squared mean intensity. Thus, the intensity changes enough over time that predicting it at particular times is not a trivial challenge. To determine how well a model predicted the true intensity function, we measured the mean squared error (MSE) of predicted intensity at a large sample of times in the held-out test seqs, and report the MSE here as a percentage of the _variance_ of the true intensity. By this construction, a simple baseline of predicting each event type’s mean intensity at all times would get 100% MSE. 

Both the Hawkes and neural-Hawkes models predict the Hawkes intensities (a) accurately, at 1% MSE. This is similar to the leftmost column of Figure 7, where both models essentially achieved oracle performance. By contrast, for the complex neural Hawkes intensities (c), the neural Hawkes model achieves 9% MSE (still quite good) whereas Hawkes does far worse at 70% MSE. This is similar to the rightmost column of Figure 7, where the neural Hawkes model approached oracle performance but the Hawkes model did much worse. 

#### **C.5 Retweet Dataset Details** 

The Retweets dataset (section 6.2) includes 166076 retweet sequences, each corresponding to some original tweet. Each retweet event is labeled with the retweet time relative to the original tweet creation, so that the time of the original tweet is 0. (The original tweet serves as the beginning-ofstream (BOS) marker as explained in Appendix A.2.) Each retweet event is also marked with the number of followers of the retweeter. As usual, we assume that these 166076 streams are drawn independently from the same process, so that retweets in different streams do not affect one another. 

Unfortunately, the dataset does not specify the identity of each retweeter, only his or her popularity. To distinguish different kinds of events that might have different rates and different influences on the future, we divide the events into _K_ = 3 types: retweets by “small,” “medium” and “large” users. Small users have fewer than 120 followers (50% of events), medium users have fewer than 1363 (45% of events), and the rest are large users (5% events). Given the past retweet history, our model must learn to predict how soon it will be retweeted again and how popular the retweeter is (i.e., which of the three categories). 

We randomly sampled disjoint train, dev and test sets with 16000, 2000 and 2000 sequences respectively. We truncated sequences to a maximum length of 264, which affected 20% of them. For computing training and test likelihoods, we treated each sequence as the complete set of events observed on the interval [0 _, T_ ], where 0 denotes the time of the original tweet (which is not included in the sequence) and _T_ denotes the time of the last tweet in the (truncated) sequence. 

20 



<!-- Start of picture text -->
54.8<br>38.4 22 54.6<br>38.2 20 54.4<br>38.0 18 54.2<br>37.8 54.0<br>37.6 16 53.8<br>37.4 14 53.6<br>37.2 12 53.4<br>Du Model N-SM-MPP Du Model N-SM-MPP Du Model N-SM-MPP<br>Models Models Models<br>2.2 6.6<br>2.0 6.4 9.85<br>1.8<br>1.6 6.2 9.80<br>1.4 6.0<br>1.2 5.8 9.75<br>1.0<br>5.6 9.70<br>Du Model N-SM-MPP Du Model N-SM-MPP Du Model N-SM-MPP<br>Models Models Models<br>ErrorRate % ErrorRate % ErrorRate %<br>RMSE RMSE RMSE<br><!-- End of picture text -->

Figure 8: Prediction results on Financial Transactions, MIMIC-II, and Stack Overflow datasets (from left to right). Error bars show standard deviation over 5 experiments with different traindev-test splits. For prediction of the types _ki_ (top row), our method achieved lower error in 4/5, 5/5, and 5/5 of the experiments. For prediction of the times _ti_ (bottom row), our method achieved lower error in 5/5, 2/5, and 0/5 of the experiments. 

Figure 9 shows the learning curves of all the models, broken down by the log-probabilities of the event types and the time intervals separately. The scatterplot Figure 10 is a copy of Figure 3, and Figure 11 breaks down the log-likelihood by event type and time interval. 

#### **C.6 MemeTrack Dataset Details** 

The MemeTrack dataset (section 6.2) contains time-stamped instances of meme use in articles and posts from 1.5 million different blogs and news sites, spanning 10 months from August 2008 till May 2009, with several hundred million documents. 

As in Retweets, we decline to model the appearance of novel memes. Each novel meme serves as the BOS event for a stream of mentions on other websites, which we do model. The _K_ event types correspond to the different websites. Given one meme’s past trajectory across websites, our model must learn to predict how soon it will be mentioned again and where. 

We used the version of the dataset processed by Gomez Rodriguez et al. (2013), which selected the top 5000 websites in terms of the number of memes they mentioned. We truncated sequences to a maximum length of 32, which affected only 1% of them. We randomly sampled disjoint train, dev and test sets with 32000, 5000 and 5000 sequences respectively, treating them as before. 

Because our current implementation does not allow for a marked BOS event (see Appendix A.2), we currently ignore where the novel meme was originally posted, making the unfortunate assumption that the stream of websites is independent of the originating website. Even worse, we must assume that the stream of websites is independent of the actual text of the meme. However, as we see, our novel models have some ability to recover from these forms of missing data. 

Figure 12 shows the learning curves of the breakdown of log-likelihood with the same format as Figure 9. Figures 13 and 14 show the scatterplots in the same format as Figures 10 and 11. 

#### **C.7 Prediction Task Details** 

Finally, we give further details of the prediction experiments from section 6.4. To avoid tuning on the test data, we split the original training set into a new training set and a held-out dev set. We train our neural model and that of Du et al. (2016) on the new training set, and choose hyper-parameters on the held-out dev set. Following Du et al. (2016), we consider three datasets, and use five different train-dev-test splits of each dataset to generate the experimental results in Figure 8. (None of the test sets’ examples were used during manual development of our system.) 

21 



<!-- Start of picture text -->
0.6 N-SM-MPP N-SM-MPP<br>D-SM-MPP D-SM-MPP<br>0.7 SE-MPP 0 SE-MPP<br>0.8<br>10<br>0.9<br>1.0 20<br>1.1<br>30<br>1.2<br>1.3 40<br>125 250 500 1000 2000 4000 8000 16000 125 250 500 1000 2000 4000 8000 16000<br>number of training sequences number of training sequences<br>log-likelihood per event log-likelihood per event<br><!-- End of picture text -->

Figure 9: Learning curves (with 95% error bars) of all these models on the Retweets dataset, broken down by the log-probabilities of just the event types (left graph) and just the time intervals (right graph). 



<!-- Start of picture text -->
2 2<br>0 0<br>2 2<br>4<br>4<br>6<br>6<br>8<br>8<br>10<br>10<br>10 8 6 4 2 0 2 10 8 6 4 2 0 2<br>N-SM-MPP N-SM-MPP<br>SE-MPP D-SM-MPP<br><!-- End of picture text -->

Figure 10: A larger copy of Figure 3, repeated here for convenience. 



<!-- Start of picture text -->
0.5<br>1.0<br>1.5<br>2.0<br>2.5<br>2.5 2.0 1.5 1.0 0.5<br>N-SM-MPP<br>SE-MPP<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br>0<br>2<br>4<br>6<br>8<br>10<br>10 8 6 4 2 0 2<br>N-SM-MPP<br>SE-MPP<br><!-- End of picture text -->

Figure 11: Scatterplots of N-SM-MPP vs. SE-MPP on Retweets. Same comparison as the left graph in Figure 10, but broken down by the log-probabilities of the event types (left graph) and the time intervals (right graph). 

22 



<!-- Start of picture text -->
5 N-SM-MPPD-SM-MPP 500 N-SM-MPPD-SM-MPP<br>SE-MPP SE-MPP<br>6 0<br>7<br>500<br>8<br>1000<br>9<br>1500<br>10<br>2000<br>11<br>1000 2000 4000 8000 16000 32000 1000 2000 4000 8000 16000 32000<br>number of training sequences number of training sequences<br>log-likelihood per event log-likelihood per event<br><!-- End of picture text -->

Figure 12: Learning curve (with 95% error bars) of all three models on the MemeTrack dataset, broken down by the log-probabilities of the event types (left graph) and the time intervals (right graph). 



<!-- Start of picture text -->
0 0<br>100000 100<br>200000 200<br>300000<br>300<br>400000<br>400<br>400000 300000 200000 100000 0 400 300 200 100 0<br>N-SM-MPP N-SM-MPP<br>SE-MPP D-SM-MPP<br><!-- End of picture text -->

Figure 13: Scatterplot of N-SM-MPP vs. SE-MPP (left graph) and vs. D-SM-MPP (right graph) on MemeTrack. N-SM-MPP outperforms D-SM-MPP on 93.02% of the test sequences. This is not obvious from the plot, because almost all of the 5000 points are crowded near the upper right corner. Most of the visible points are outliers where N-SM-MPP performs unusually badly—and D-SM-MPP typically does even worse. 



<!-- Start of picture text -->
0<br>5<br>100000<br>10<br>200000<br>15 300000<br>20 400000<br>20 15 10 5 400000 300000 200000 100000 0<br>N-SM-MPP N-SM-MPP<br>SE-MPP SE-MPP<br><!-- End of picture text -->

Figure 14: Scatterplots of N-SM-MPP vs. SE-MPP on MemeTrack. Same comparison as the left graph of Figure 13, but broken down by the log-probabilities of the event types (left graph) and the time intervals (right graph). 

23 

### **D Ongoing and Future Work** 

We are currently exploring several extensions to deal with more complex datasets. Based on our survey of existing datasets, we are particularly interested in handling: 

- immediate events ( _ti−_ 1 = _ti_ ), as discussed in footnote 1 

- “baskets” of events (several events that are recorded as occuring simultaneously but without a specified order, e.g., the purchase of an entire shopping cart) 

- hard constraints on the event type sequence _k_ 1 _, k_ 2 _, . . ._ 

- marked events<sup>13</sup> and annotated events<sup>14</sup> 

- causation by external events (artificial clock ticks, periodic holidays, weather) 

- richer drift functions<sup>15</sup> 

- hybrid of D-SM-MPP and N-SM-MPP, allowing direct influence from past events 

- multiple agents each with their own state, who observe one another’s actions (events) 

More important, we are interested in modeling causality. The current model might pick up that a hospital visit elevates the instantaneous probability of death, but this does not imply that a hospital visit _causes_ death. (In fact, the severity of an earlier illness is usually the cause of both.) 

A model that can predict the result of interventions is called a causal model. Our model family can naturally be used here: any choice of parameters defines a generative story that follows the arrow of time, which can be interpreted as a causal model in which patterns of earlier events _cause_ later events to be more likely. Such a causal model predicts how the distribution over futures would change if we intervened in the stream of events. 

In general, one cannot determine the parameters of a causal model based on purely observational data (Pearl, 2009). Thus, in future, we plan to determine such parameters through randomized experiments by deploying our model family as an environment model within reinforcement learning. A reinforcement learning agent _tests_ the effect of random interventions to discover their effect (exploration) and thus orchestrate more rewarding futures (exploitation). 

In our setting, the agent is able to stochastically insert or suppress certain event types and observe the effect on subsequent events. Then our LSTM-based model will discover the causal effects of such actions, and the reinforcement learner will discover what actions it can take to affect future reward. Ultimately this could be a vehicle for personalized medical decision-making. Beyond the medical domain, a quantified-self smartphone app may intervene by displaying fine-grained advice on eating, sleeping, exercise, and travel; a charitable agency may intervene by sending a social worker to provide timely counseling or material support; a social media website may increase positive engagement by intelligently distributing posts; or a marketer may stimulate consumption by sending more targeted advertisements. 

> 13A “mark” is some structured data attached to an event: for example, the textual content associated with a tweet, or the medical records associated with a doctor visit. The model should predict the marks from each event and its underlying hidden state, and they should be fed back into the LSTM as additional input. 

> 14Humans may be asked to classify the events in an event stream or the relationships among its events. Unlike marks, these annotations are not involved in the process that generates the event stream, and so are not fed into the LSTM as input. Rather, they are assumed to be generated _post hoc_ by the human from the entire observed stream—and may depend on the human’s implicit reconstruction of the hidden states. We can use any available annotations to help reconstruct the hidden states (Zaidan and Eisner, 2008), if we model them as stochastic functions of the hidden states. In particular, annotations on the training data serve as side information to improve training of the model. As a simple example, an annotation of the training event ( _ki, ti_ ) could be assumed to depend also on the subsequent LSTM state **h** ( _t_<sup>+</sup> _i_<sup>)</sup> def= lim _t→t_ + _i_<sup>**h**(</sup><sup>_t_).</sup> 

> 15We expect the exponential drift in equation (7) to be expressive enough in most settings. In principle, however, one might want to allow periodic fluctuation of the intensity between events, say by using a _complex_ exponential in (7). Another way to increase expressivity would be to compute drift using the LSTM itself, by injecting special “clock tick” events into the input stream at regular intervals (compare Xiao et al., 2017b). Each clock tick event ( _ki, ti_ ) causes a rich nonlinear update of the LSTM state via equations (5)–(6), except that it should always set **c** _i_ +1 = **c** ( _ti_ ) for continuity. In this design, the interval between ordinary events is modeled piecewise—it is divided up into short pieces by the clock ticks, with **c** ( _t_ ) on each piece modeled using our current function family. 

24 

