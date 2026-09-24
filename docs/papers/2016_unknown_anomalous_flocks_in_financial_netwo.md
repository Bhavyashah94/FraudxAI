---
title: "Anomalous Flocks in Financial Networks: Community Detection and Evasion in Banking Rails"
authors: "unknown"
year: 2016
arxiv_id: "1603.01892"
original_file: "1603.01892.pdf"
pdf_path: "docs/papers\2016_unknown_anomalous_flocks_in_financial_netwo.pdf"
---

# Anomalous Flocks in Financial Networks: Community Detection and Evasion in Banking Rails

**Authors:** Unknown et al.  
**Year:** 2016 | **arXiv:** [`1603.01892`](https://arxiv.org/abs/1603.01892)  
**Local PDF:** [`2016_unknown_anomalous_flocks_in_financial_netwo.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2016_unknown_anomalous_flocks_in_financial_netwo.pdf)

---

# Monopole-Enriched Groundstates of Two-Dimensional BCS Models<sup>∗</sup> 

David Roberts<sup>1</sup><sup>_,_2</sup> 

1 _Department of Physics, Harvard University, Cambridge MA 02138, USA_ 

2 _NASA Quantum Artificial Intelligence Laboratory, Moffett Field, CA 94035, USA_ 

(Dated: December 18, 2016) 

We extract the macroscopic characteristics of the groundstate sectors of two dimensional Bosecondensed BCS models with a fixed number of magnetic flux quanta, on length scales much larger than the characteristic size of the Cooper-pair bound states. We show that this reduces to the problem of computing the moduli space of gauge-inequivalent solutions to the Gross-Pitaevskii equations on a nontrivial fibre bundle. Inspired in part by the physical arguments of Oshikawa and Senthil in _Fractionalization, Topological Order, and Quasiparticle Statistics_ , we extract a large class of groundstates from this moduli space. 

### I. INTRODUCTION 

### II. BACKGROUND 

One of the hallmarks of a topological phase of matter is a marked dependence of the number of groundstates on the topology of the system. Superconductors share this property, in that the groundstate degeneracy of a superconductor shaped like a manifold Σ is a topological invariant of Σ. However, topological groundstate degeneracy in superconductors with non-zero net magnetic flux is less well-understood. Therefore, in this paper, we address this gap and compute the groundstates of two-dimensional superconductors with background monopoles. We find a continuum of superconducting groundstates, as well as other exotic physics. 

Our model of the superconductor is the standard BCS model with the _s_ -wave pairing hypothesis, in the ultradilute, infinite volume limit, in which the BCS energy density on Σ becomes well-approximated by the GrossPitaevskii energy density. The set of physically-distinct superconducting groundstates is then the moduli space of gauge-inequivalent solutions to the Gross-Pitaevskii equations on a complex line bundle L → Σ. Therefore, we use the variational principle of quantum mechanics to extract the superconducting groundstates. 

In this variational method, the difficulty of extracting the superconducting groundstates with monopoles translates into the difficulty of solving the GP equations on a nontrivial line bundle L. Despite this difficulty, we surmount it using powerful mathematical methods, inspired in part by geometric analysis (Taubes’s PhD thesis _Vortices and Monopoles_ ), and in part by condensed matter physics (Oshikawa and Senthil in _Fractionalization, Topological Order, and Quasiparticle Statistics_ ). 

### A. Quantization of Fermions on a Riemann Surface 

To even discuss the BCS model on a nontrivial surface requires some work. A great way to start is to construct the Hilbert spaces involved, as well as the local field algebra of observables, in a manifestly covariant way. 



Figure 1. The superconductor Σ. In this case, _g_ = 1 (Source: Google Images). 

We begin with the observation that the space of states for a fermion on Σ is _unitarily_ isomorphic to the Hilbertspace _L_<sup>2</sup> (L) of square-integrable cross-sections of some hermitian line bundle L over Σ. 

Now, if we fix a surface Σ, there are many line bundles L → Σ. In fact a standard result of the theory of characteristic classes is that these are classified modulo diffeomorphisms by their first Chern class. By the ChernWeil homorphism, this integer is precisely the number of magnetic flux quanta penetrating the surface: 

> ∗ Honors thesis written under the supervision of Clifford Taubes 

_c_ 1(L) ∈ _H_<sup>2</sup> (Σ) ≃ Z 

2 

_n_ is also commonly known as the magnetic monopole number, but this is only a convenient device for physical intuition; there is no "outside" of the surface. 

We can then ask: what line bundle should we consider for our model? In this paper, we allow all possibilities: each fixed _n_ defines a unique line bundle L up to diffeomorphisms. Thus each topological sector contains a distinct smooth structure and ultimately a full-fledged BCS model. The construction goes like this: having fixed an integer _n_ , we then define an electromagnetic gauge field _A_ , inducing a holomorphic structure on L. In the corresponding Yang-Mills theory, the dynamical variable is the _holomorphic structure_ of L: as the gauge field evolves through time, the holomorphic structure of L may vary through time. In contrast, the topological structure of L is static, i.e. magnetic charge is conserved. 

Here, E _Y M_ denotes the standard Yang-Mills energy density of ∇, which is the covariant derivative on L specified by the gauge field (here, it is acting on the second argument of _ϕ_ 0). Having defined the energy functional, the variational principle yields the set of groundstates for the BCS model: 



However, because there is no additional structure on L that allows an observer to distinguish between isometric gauges, we must physically identify two groundstates which are related by a gauge transformation. Mathematically, this corresponds to modding-out H _BCS_ by the action of the gauge group. 

Accordingly, we define the moduli space of _s_ -wave superconducting groundstates on a surface Σ by 



Having fixed a topological structure, we can then construct the corresponding many-body Hilbert space H for the fermions as the exterior algebra on the Hilbert space of square-integrable cross-sections of L (here, _n_ indexes fermion, not monopole, number): 



The observable algebra O can then also be constructed, as the union of local algebras {O _U_ } generated by fermonic creation and annihilation operators of crosssections supported on open subsets _U_ of Σ. 

### B. The BCS Energy Density 

This and the next subsection will both closely model the discussions in [1]. The many-fermion model on Σ that we wish to study is a standard BCS model with _s_ - wave pairing. The groundstate postulates of BCS theory with _s_ -wave pairing can be stated succinctly as 



where the _s_ -wave BCS variational ansatz | _ϕ_ 0 _,ϕ_ 1� is defined to be the unique quasi-free state determined by the following two-point functions on the fermonic field algebra O: 



The final relevant assumption of the BCS model with _s_ - wave pairing is that the expectation value of the energy of the BCS variational ansatz (i.e. the BCS energy functional), is assumed to satisfy (see [1]): 



where G denotes the action of gauge transformations on the triple ( _A,ϕ_ 0 _,ϕ_ 1) induced by gauge transformations of the fermonic field algebra O. Because we have now modded-out by gauge transformations, M _BCS_ (Σ) is equal to the set of physically-distinguishable groundstates of a BCS model on Σ. 

### C. The Macroscopic Limit and the GP Energy Density 

Following [1], we introduce an ultra-dilute infinitevolume limit _ϵ_ → 0, in which the expected number of fermions goes to zero as _ϵ_ , and the volume of the surface approaches infinity as 1 _/ϵ_<sup>2</sup> . Based on the results of [1], we expect E _BCS_ to be well-approximated by the GrossPitaevskii energy functional 



i.e. the energy density depends only on an order parameter _ψ_ ∈ _L_<sup>2</sup> (L ⊗L) for paired electrons. This is expected, because the superconducting state, according to the BCS theory, is a BEC of paired electrons, and the Gross-Pitaevskii functional is well-known to describe the energy of a BEC, as proven by Erdos et. al. in [2]. Here, 



i.e., the covariant derivative on the Cooper-pairs is constructed via second-quantization of the single-particle covariant derivative. Therefore, in this ultra-dilute, infinite-volume limit, the set of groundstates for the _s_ - wave BCS model is, effectively 



3 

Again, because there is no structure on L that allows an observer to distinguish between isometric gauges, we must mod-out the action of the gauge group on H<sup>_α_</sup> _GP_<sup>.</sup> 

Accordingly, the moduli space of solutions to the GP equations on a surface Σ modulo gauge transformations is defined as 



where G denotes the action of gauge transformations on the pair ( _A,ψ_ ) induced by gauge transformations of the fermonic field algebra O. Because we have now modded-out by gauge transformations, M _GP_ (Σ) is equal to the set of physically-distinguishable groundstates of a BCS model on Σ, in this ultra-dilute, infinite-volume limit. 

### III. THE BCS GROUNDSTATE SECTOR WITHOUT MONOPOLES 

Here, we consider the case _n_ = 0, where the analysis will reproduce N. Read and Green’s fascinating result in [3], namely, that a BCS model on a Riemann surface has ground states exactly corresponding to the spin structures on that surface, without referring to details of the BCS Hamiltonian. All of this power comes at the price that our results are only relevant in the ultra-dilute, infinite-volume limit. 

To analyze the GP functional in the _n_ = 0 sector, we break it up into three parts. Also, to simplify the analysis, we will set the single-particle potential _U_ ∈ _C_<sup>∞</sup> (Σ) to be a constant. In this case, we can write 



The reason why we are decomposing the action in this way is because, in the topologically-trivial sector, all three terms can be simultaneously minimized: to minimize E1 _,_ E2 _,_ and E3, it suffices to have, separately, 



where the first condition only makes sense on a trivial line bundle. Since these equations are simultaneously satisfiable, the corresponding space of solutions modulo gauge transformations is exactly M<sup>_α_</sup> _GP_<sup>(Σ).</sup> 



Figure 2: _A superconducting groundstate on a surface_ Σ _(here g_ = 2 _), in the absence of monopoles, is labeled by_ 2 _g bits, one for each generator of the fundamental group of the surface (Source: Google Images)._ 

We now do as stated, that is, compute the solutions to the system of three minimization conditions (A.1). The first condition implies that _A_ is flat. The second condition implies that the value of the order parameter at any given point is the parallel transport of its value from anywhere else: 



Since _ψ_ is a global section, this implies that the holonomy of the connection ∇<sup>(2)</sup> is always trivial inside the superconducting region. Since we have, for every closed loop _γ_ , 



We have that the holonomy of _A_ squares to one, and therefore lies in the subgroup Z2 ⊂ _U_ (1). We now can state the following theorem: 

## Theorem III.1 (Groundstate Subspace) _We have an isomorphism of sets_ 



_where_ M _flat_ (Σ _,_ Z2) _denotes the holonomy_ ±1 _-subspace of the moduli space of flat connections on_ Σ _modulo gauge transformations._ 

_Proof._ Every groundstate of the superconductor, by the analysis above, corresponds to an equivalence class [��� _ψ,A_ �], where _A_ is a flat gauge field with holonomy ±1, and we have, for _θ_ ∈ _C_<sup>∞</sup> (Σ), 



4 

Therefore, we are essentially claiming that it suffices to represent each groundstate by the gauge-equivalence class of _A_ , and forget about the order parameter. 

This is because, to specify _ψ_ , all we need is the value _ψ_ 0 of the order parameter at a single point _x_ 0 in the superconducting region; to obtain the value anywhere else, we parallel transport via ∇<sup>(2)</sup> : 



Therefore, by specifying a value _ψ_ 0 of the order parameter at a fixed point _x_ , we can recover the groundstate which represents any given gauge field. 

Once we choose such a value _ψ_ 0 along with representatives _Ai_ from each equivalence class of flat gauge fields, we find that this defines a map of sets 



which factors onto a isomorphism M<sup>_α_</sup> _GP_<sup>(Σ)</sup> ≃ Mflat(Σ _,_ Z2), upon modding-out by gauge transformations on both sides. □ 

By our theorem, the groundstates of a superconductor are in one-to-one correspondence with the holonomy ±1-subspace of the moduli space of flat connections on Σ modulo gauge transformations. By the universal coefficient theorem, 



and therefore we have an exact solution 



Note that, in deriving this formula, we did not have to assume that Σ was two-dimensional. For the special case of a Riemann surface, however, we can go further: the rank-one cohomology of a Riemann surface with coefficients in Z2 is the direct product of 2 _g_ copies of Z2, where _g_ = 0 _,_ 1 _,_ 2 _,_ ··· is the genus. Therefore, 



Therefore, we have, as desired, reproduced the results of [3] demonstrating the one-to-one correspondence of groundstates of the BCS model to spin structures on Σ, without referring to the microscopic details of the BCS Hamiltonian. 

|Σ|_H_<sup>1</sup>(Σ;Z2)||M<sup>_α_</sup><br>_GP_ <sup>(Σ)| (GSD)</sup>|
|---|---|---|
|_S_<sup>1 </sup>×_S_<sup>1</sup>|Z2 ×Z2|<br>4|
|Σ(_g_= 2)|Z<sup>4</sup><br>2|64|
|Σ(_g_= 3)|Z<sup>6</sup><br>2|256|



TABLE I. The groundstate degeneracy of a monopole-free BCS model on a surface Σ exhibits a marked dependence on the topology of Σ. 

### IV. THE BCS GROUNDSTATE SECTOR WITH MONOPOLES, AT _α_ = 1 _/_ 4 

Now we allow ourselves to be in a topologically nontrivial sector, and allow _n_ � 0. The calculation of the moduli space of groundstates of the BCS model will be vastly more difficult in this case, and so we focus on the special case _α_ = 1 _/_ 4, where the GP energy functional coincides with the Yang-Mills-Higgs action functional. Roughly, 



This will allow us to efficiently extract a large subspace of M<sup>1</sup> _GP_<sup>_/_4(Σ),i.e.,alargeclassofsuperconducting</sup> groundstates, in spite of the complications caused by the net magnetic flux through the surface. 



We now introduce the Yang-Mills-Higgs action, at level _τ_ , on a complex line bundle L → Σ, by the following expression: 



The moduli space of solutions modulo gauge transformations to the corresponding Yang-Mills-Higgs equations in the topological sector _c_ 1(L) = _n_ was computed by Bradlow in 1990 [4] to be, in the limit Vol(Σ) ≫ _τ_ , isomorphic to the _n_ -fold symmetric product of the surface with itself: 



Therefore, if we treated the Yang-Mills-Higgs action as an energy density E _Y MH_<sup>_τ_foraquantummany-</sup> body Hamiltonian, i.e., identical to the situation with E _GP_<sup>_α_,thenthegroundstatesectorforthisHamiltonian</sup> would be isomorphic to the _n_ -particle component of the bosonic Fock space on Σ, i.e. each groundstate |Ω _Y MH_ ⟩ would admit a labelling by vortex locations: 



5 

### B. Injecting the Yang-Mills-Higgs moduli space into the space of superconducting groundstates 

We now take advantage of the miraculous coincidence between the Yang-Mills-Higgs functional at _τ_ = −8 _U_ and the superconducting energy functional at _α_ = 1 _/_ 4 to extract crucial information about the superconducting groundstates in the presence of monopoles. The relation is most succinctly stated as 



where the constant of proportionality is positive. Therefore, if we take any equivalence class [��� _ψ,A_ �] in the Yang-Mills-Higgs moduli space, then, automatically, ��� _ψ,A/_ 2� is an equivalence class of superconducting groundstates: 



Furthermore, if [��� _ψ_ ′ _,A_ ′�] � [��� _ψ,A_ �] ∈M _Y MH_ −8 _U_<sup>(Σ)are</sup> distinct in the Yang-Mills-Higgs moduli space, then the corresponding superconducting groundstates constructed via (A.3) are also distinct in the Gross-Pitaevski moduli space: 



To see this, suppose to the contrary that 



Then, in particular, this means that there exists a gauge transformation _g_ , such that, in a local trivialization 



Therefore, letting _h_ be the gauge transformation _g_ composed with itself twice, then, in that same trivialization, 



Therefore, since this analysis holds in each local trivialization, we have [��� _ψ_ ′ _,A_ ′�] = [��� _ψ,A_ �] ∈M _Y MH_ −8 _U_<sup>(Σ),con-</sup> tradicting our original assumption that the two classes were unequal in the Yang-Mills-Higgs moduli space. Therefore, in total, we have constructed an injection of moduli spaces 



Figure 3. _The refined construction: each equivalence class of solutions to the Yang-Mills-Higgs equations splits into a distinct family of gauge-inequivalent solutions to the α_ = 1 _/_ 4 _GP equations._ 

In particular, the set of superconducting groundstates in the image of this injection, by Bradlow’s calculation earlier, is isomorphic to the _n_ -fold symmetric product of the surface with itself: 



Therefore, identical to the situation earlier, each superconducting groundstate |ΩBCS⟩ in this subset admits a labelling by vortex locations: 



### C. Refining the Lower-Bound 

Having sketched a basic construction, namely the injection of the Yang-Mills-Higgs moduli space into the Gross-Pitaevskii moduli space at _α_ = 1 _/_ 4, we can refine this construction in a way that will increase the lower bound by a sizable topological factor. In particular, for each class ��� _ψ,A_ � ∈M− _Y MH_ 8 _U_<sup>(Σ), we actually can construct</sup> up to 2<sup>2</sup><sup>_g_</sup> distinct superconducting groundstates 



defined by the integral equations 



sending [| _ψ,A_ ⟩] �→ [| _ψ,A/_ 2⟩], that allows us to view M<sup>−</sup> _Y MH_<sup>8</sup><sup>_U_(Σ) as a subset of M1</sup> _GP_<sup>_/_4(Σ).This gives us a lower-</sup> bound on the number of superconducting groundstates on Σ in this nontrivial setting, where it is relatively difficult to obtain information. 



where _γ_ 1 _,_ ··· _,γ_ 2 _g_ are the fundamental cycles of the surface. These are manifestly gauge inequivalent, because holonomies are invariant under gauge transformations. 

6 

Therefore, each solution of the Yang-Mills-Higgs equations splits into a family of 2<sup>2</sup><sup>_g_</sup> physically-distinct superconducting groundstates. This is the topological fractionalization phenomenon detailed in _Fractionalization, Topological Order, and Quasiparticle Statistics_ . Therefore, the initial estimate as to the number of superconducting groundstates at _α_ = 1 _/_ 4 can be multiplied by the rank of the holonomy ±1 subspace of the moduli space of flat connections on Σ: 



Unpacking the physics, this class of superconducting groundstates is labelled by a combination of both continuous quantum numbers, corresponding to vortex locations, and discrete quantum numbers, corresponding to holonomy of _A_ around the generators _γ_ 1 _,_ ··· _,γ_ 2 _g_ of the fundamental group of Σ: 



Therefore, we have found a continuum of superconducting groundstates, labelled by a mixture of both discrete and continuous quantum numbers. 

### D. Example: Groundstate Sector of BCS Theory at _α_ = 1 _/_ 4 on the Hopf Bundle _S_<sup>3</sup> 

We now focus on a concrete example, to illuminate the relevant characteristics of the classification program we have carried out for two-dimensional BCS theory. Therefore, we will solve the _α_ = 1 _/_ 4 GP equations on the bundle LHopf → _S_<sup>2</sup> , the associated line bundle to the Hopf bundle _S_<sup>3</sup> → _S_<sup>2</sup> . 



Figure 4 _. The Hopf Fibration (Source: Google Images)._ Since the associated bundle LHopf has Chern number _c_ 1(LHopf) = 1, and since Mflat( _S_<sup>2</sup> _,_ Z2) = 0, our technique 

extracts a class of groundstates 



in one-to-one correspondence with the surface _S_<sup>2</sup> itself. Physically, this makes sense: since there is only one vortex, each superconducting groundstate is labelled by the location _z_ ∈ _S_<sup>2</sup> of that vortex. Furthermore, all loops on a two-dimensional sphere can be contracted to a point, and so a flat gauge field has trivial holomomy; so there is no additional ground state degeneracy (GSD) that we can deduce from fractionalization arguments. 

### V. SUMMARY AND OUTLOOK 

The physics of superconductivity has been incredibly successful in inspiring revolutionary technologies such as SQUIDs, superconducting qubits, MRI, and more. In this paper, we examined the topological groundstate degeneracy (GSD) of two-dimensional superconductors with non-zero net magnetic flux. In the already wellknown case _n_ = 0, we reproduced the results of Read and Green in [3] by explicitly identifying superconducting groundstates on a surface Σ with the set of spin structures on that surface: 



In dimension two and _n_ � 0, we witnessed new physics, including a continuum of superconducting groundstates, parametrized both by continuous vortex locations as well as discrete flux values around noncontractible loops on the surface. This was proven by our identification of a large class of solutions to the Gross-Pitaevskii equations at _α_ = 1 _/_ 4: 



Once again, study of superconductivity over the past century has inspired new technologies, and we hope that, by pushing the boundaries of superconducting physics, the results will be no different, inspiring new technological paradigms. 

### VI. ACKNOWLEDGEMENTS 

I would like to acknowledge my thesis advisor Clifford Taubes for being an incredible mentor during my senior year at Harvard. I am also grateful for many fruitful discussions with Bertrand Halperin, from whom, throughout my last three semesters of college, I learned much condensed matter theory. Finally, I would like to thank Harvard junior Jake McNamara for helping me understand the relevant aspects of Spin 

7 

structures. Finally, I also am indebted to Peter Kronheimer at Harvard University, and Andre Petukhov and Sergey Knysh at NASA QuAIL for providing useful feedback on this work. 

### VII. REFERENCES 

- [1] Christian Hainzl, Benjamin Schlein, _Dynamics of Bose-Einstein condensates of fermion pairs in the low density limit of BCS theory_ , (2001), `https:// arxiv.org/abs/1203.2811` . 

- [2] Laszlo Erdos, Benjamin Schlein, Horng-Tzer Yau, _Derivation of the Gross-Pitaevskii equation for the dynamics of Bose-Einstein condensate_ , (2010), Annals of Mathematics. 

- [3] N. Read, Dmitry Green, _Paired states of fermions in two dimensions with breaking of parity and timereversal symmetries, and the fractional quantum Hall effect_ , Phys. Rev. B, (2000), `https://arxiv.org/ abs/cond-mat/9906453` 

- [4] Bradlow, _Vortices in holomorphic line bundles over closed Kahler manifolds_ , Communications in Mathematical Physics, (1990), `http: //projecteuclid.org/euclid.cmp/1104201917` 

- [5] Jaffe, A., Taubes, C., _Vortices and Monopoles, Structure of Static Gauge Theories_ , Progress in Physics 2, Boston-Basel-Stuttgart, Birkhauser Verlag (1980), 287 S., DM 30,-. ISBN 3-7643-3025-2 

- [6] Masaki Oshikawa, T. Senthil, _Fractionalization, topological order, and quasiparticle statistics_ , Phys. Rev. Lett. 96, 060601, (2006), `https://arxiv. org/abs/cond-mat/0506008` 

