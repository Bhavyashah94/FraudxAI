---
title: "Privacy-Preserving Federated Subgraph Learning Across Banking Silos"
authors: "unknown"
year: 2022
arxiv_id: "2203.04591"
original_file: "2203.04591.pdf"
pdf_path: "docs/papers\2022_unknown_privacypreserving_federated_subgrap.pdf"
---

# Privacy-Preserving Federated Subgraph Learning Across Banking Silos

**Authors:** Unknown et al.  
**Year:** 2022 | **arXiv:** [`2203.04591`](https://arxiv.org/abs/2203.04591)  
**Local PDF:** [`2022_unknown_privacypreserving_federated_subgrap.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_unknown_privacypreserving_federated_subgrap.pdf)

---

# **Yield-stress transition in suspensions of deformable droplets** 

Giuseppe Negro<sup>1</sup> , Livio Nicola Carenza<sup>2</sup> , Giuseppe Gonnella<sup>1</sup> , 

Fraser Mackay<sup>3</sup> , Alexander Morozov<sup>3</sup> , Davide Marenduzzo<sup>3</sup> 

> 1 _Dipartimento di Fisica, Universit´a degli Studi di Bari and INFN,_ 

_Sezione di Bari, via Amendola 173, Bari, I-70126, Italy,_ 

> 2 _Instituut-Lorentz, Universiteit Leiden, P.O. Box 9506, 2300 RA Leiden, Netherlands,_ 

> 3 _SUPA, School of Physics and Astronomy, University of Edinburgh,_ 

_Peter Guthrie Tait Road, Edinburgh, EH9 3FD, UK_ 

Yield-stress materials, which require a sufficiently large forcing to flow, are currently ill-understood theoretically. To gain insight into their yielding transition, here we study numerically the rheology of a suspension of deformable droplets under pressure-driven flow. We show that the suspension displays yield-stress behaviour, with the droplets remaining motionless when the applied body-force is below a critical value. In the non-flowing phase, droplets jam to form an amorphous structure, whereas they order in the flowing phase. Yielding is linked to a percolation transition in the contacts of droplet-droplet overlaps, and requires suitable wetting boundary conditions and strict conservation of the droplet area to exist. Close to the yielding transition, we find strong oscillations in the droplet motion which closely resemble those found experimentally in confined colloidal glasses under flow. We show that even when droplets are static the underlying solvent moves by permeation, so that the viscosity of the composite system is never truly infinite, and, as we discuss, its precise value ceases to be a bulk material property of the system. 

Yield-stress fluids are materials which flow only when subject to a sufficiently large stress, or external forcing [1, 2]. The critical stress above which there is flow is known as the yield stress. Examples of yield-stress fluids abound in everyday materials and include toothpaste, whipping or shaving cream, mayonnaise and cement. The defining property of an ideal yield-stress fluid is that the apparent viscosity should be infinite below yielding, so that the yield stress should mark a transition between a solidlike and a fluid-like regime. Nevertheless, in practice it is often arduous to distinguish this behaviour from that of a strongly shear-thinning fluid for which the viscosity drops by orders of magnitude at the yielding point, such that the material always flows albeit very slowly under any external forcing, however small [2]. 

Phenomenological theories for yield-stress fluids typically assume a non-Newtonian and non-linear relation between the shear stress _σ_ and the shear rate (or velocity gradient) _γ_ ˙ . A popular model is the HerschelBulkley one [3], which is based on the generic equation _σ_ = _σy_ + _η∞γ_ ˙<sup>_n_</sup> , with _σy_ the yield stress, _η∞_ a material parameter and _n_ a generic exponent found by fitting experimental data, and smaller than 1 for shear-thinning fluids. Phenomenological models like this are extremely useful to analyse and compare experiments, but – by their nature – they do not address the fundamental physical mechanisms underlying the _existence_ of a yield stress. 

Yield-stress fluids can be characterised according the softness of their constituents [2, 4], and range from bubble foams [5–7] to suspensions of nearly-hard colloidal spheres [8, 9] (e.g., spherical particles stabilised sterically with a thin polymer layer). In all cases, at large enough particle concentrations – such that the system is the jammed, or glassy, phase respectively – these ma- 

terials are experimentally known to undergo a yielding transition. They also display soft glassy rheology, as described by the Herschel-Bulkley model [10–12]. In colloidal fluids, rheological experiments further show that the effective viscosity of the system becomes very large, and possibly diverges [2, 9]. A confounding factor hampering a conclusive demonstration of ideal yield-stress behaviour in experiments is that the solid-like phase in a colloidal glass is amorphous, and the fundamental physics of the amorphous state is not fully understood [2]. Additionally, as we show to be relevant here, colloidal glasses or foams are composite materials, so that the behaviour of the dispersed particles and the underlying solvent may differ, thereby complicating the picture. 

Here we consider a generic universal model system for a yield-stress fluid: a suspension of soft deformable droplets embedded in a Newtonian fluid [13–16]. By changing the particle softness – in particular interpenetrability and surface tension – our model encompasses foams, stabilised oil-in-water emulsions and colloidal suspensions as special cases. We show that these deformable suspensions display the hallmark of yield-stress fluids, as the droplets are immobile even when subjected to a (small) pressure difference, or forcing. In this immobile phase, the droplets are arranged in an amorphous pattern, and the network of droplet-droplet contacts, or overlaps, percolates. These overlaps provide the soft analogue of frictional contacts, which are known to play a crucial role in colloidal rheology [17]. Upon yielding, contact percolation is lost, while droplets order as they flow. Importantly, we find that even in the phase where droplets are static the solvent flows by permeation, meaning that the viscosity of the overall system is never truly infinite. Close to the yielding point, sustained velocity 

2 

oscillations occur, similarly to what found experimentally in flowing colloidal fluids close to the glass transition [18]. Our results allow to gain more insight into the microscopic physical mechanisms underlying the yielding transition. In our system, the latter is controlled by an inverse Bingham number, measuring the ratio between viscous and interfacial forces. Notably, this is the same number which controls discontinuous shear thinning at larger forces [13, 14, 19]. Finally, our simulations suggest that yielding disappears when the droplets area is not strictly conserved, suggesting that systems featuring evaporation-condensation phenomena can evade yield-stress behaviour and flow under any forcing. 

To study the rheology of our soft droplet suspension, we work in 2 _D_ (Fig. 1) and consider two models: the first strictly conserves the area of each droplet, the second allows it to fluctuate around a target value, for instance due to evaporation or condensation phenomena. We refer to these as the conserved and non-conserved model, respectively. In both cases, the _N_ droplets in the system are non-coalescing, and we ensure this by describing them in terms of _N_ distinct phase fields, _φi_ , with _i_ = 1 _, . . . , N_ . The hydrodynamics of the suspension can then be studied by following the coupled evolution of the phase-field variables and of the velocity field **v** of the underlying solvent. The use of phase-field means that lubrication forces, which are notoriously challenging to accurately account for in simulations [17, 20] are altogether absent. At the same time, frictional forces, which are known to play a crucial role in colloidal rheology [17], are present, in the form of overlaps between different phase-fields. 

The thermodynamics of the conserved model is governed by a free energy _F_ whose density is 



Here, the first two terms favour the formation of circular droplets with _φi ≃ φ_ 0 in their interior, and _φi ≃_ 0 outside. The material constants _α_ and _K_ determine the surface tension _γ_ = �8 _Kα/_ 9 and the interfacial thickness _ξ_ = �2 _K/α_ of the droplets [21]. The term proportional to _ϵ >_ 0 describes soft repulsion pushing droplets apart when overlapping. The phase-field variables evolve according to a set of coupled Cahn-Hilliard equations, 



where _M_ is the mobility, _µi_ = _δF/δφi_ the chemical potential of the _i_ -th droplet. The flow obeys the NavierStokes equation 



where _ρ_ indicates the total fluid density, _p_ denotes the hydrodynamic pressure and _η_ 0 the solvent viscosity [26]. 

The term **f**<sup>_th_</sup> = _−_<sup>�</sup> _i_<sup>_φi∇µi_standsfortheinternalther-</sup> modynamic force field due to the presence of non-trivial compositional order parameters, while _f_ is the magnitude of the body-force, which we take along the horizontal direction (Fig. 1a). 

In our second model for the non-conserved concentration field, the free energy _F_ is supplemented by an additional term, 



with _λ >_ 0 a constant which quantifies droplet compressibility, and provides a soft constraint for the droplet area. The phase-fields evolve according to a relaxational and overdamped dynamics defined by 



where Γ is a friction-like parameter and _F_<sup>_′_</sup> = _F_ + _Fconstraint_ . The equation for **v** is still given by Eq. (3). 

The dynamics are integrated with a parallel hybrid lattice Boltzmann approach [23–25] where Eq. (3) is solved by a lattice Boltzmann algorithm, and Eqs. (2),(5) are solved by finite difference methods. We consider flow in a channel with no-slip boundary conditions at the top and bottom walls, driven by a fixed pressure difference along the _y_ direction – leading to Poiseuille, parabolic, flow for a Newtonian fluid. At the wall, neutral wetting boundary conditions are imposed for each droplet. For more details, and a full list of parameters used, see [26]. 

We first study the rheological response of a droplet suspension (with packing fraction _ϕ ≃_ 0 _._ 5) in the conserved model. A key result is that there exists a critical body-force _fc_ separating two fundamentally different behaviours. For small forcing (Figs. 1a and 2a) the suspended droplets are jammed and settle into a stationary non-flowing configuration (Suppl. Movie 1) where they are immobile for the whole duration of the numerical experiment ( _∼O_ (10<sup>8</sup> ) iterations). The snapshot shown in Fig. 1a shows a typical droplet configuration for this regime. For larger _f_ , there is a subtle morphological rearrangement of the droplets (Fig. 1b), which is accompanied by a yielding transition, as droplets now steadily move (Fig. 2a). The snapshot shown in Fig. 1b shows a typical late time configuration, which is travelling from left to right at a fixed velocity (Fig. 2a and Suppl. Movie 2). An inspection of the configurations shows that while the non-flowing state is amorphous (Fig. 1a), in the flowing state droplets order (Fig. 1b; see [26] for a quantification of flow-induced ordering). This morphological adjustment is accompanied by a fundamental change in the patterns of contacts, or overlaps, between droplets. As shown in the left inset of Fig. 1c, such overlaps create a percolating network in the non-flowing state, whereas after yielding contacts no longer percolate along the flow 

3 



FIG. 1. **Yielding transition in the conserved model. (a)-(b)** Color map of _φ_ =<sup>�</sup> _i_<sup>_φi_for</sup><sup>_f<fc_(</sup><sup>_f_=2</sup><sup>_._0</sup><sup>_×_10</sup><sup>_−_6in</sup> panel (a)) and _f > fc_ ( _f_ = 4 _._ 0 _×_ 10<sup>_−_6</sup> in panel (b)), for the conserved model. Black and red regions correspond to _φ_ = 0 and _φ_ = 2 respectively. **(c)** Free energy of overlaps (see text) as a function of body-force _f_ . The insets of panel (c) show clusters of contacting droplets, resulting from a density-based spatial clustering analysis on the free energy of overlaps [26]. Different colors correspond to different clusters. Left and right inset correspond to the configuration shown in panels (a) and (b) respectively. Movies of the dynamics corresponding to (a) and (b) can be seen in Suppl. Movies 1 and 2 respectively [26]. 

gradient direction (right inset of Fig. 1c and Fig S1). The change in droplet contacts can be quantified by plotting the overlap free energy ( _F_ overlaps = _ϵ_ � _dydz_<sup>�</sup> _i,j_<sup>_φ_</sup> _i_<sup>2</sup><sup>_φ_2</sup> _j_<sup>)</sup> as a function of body-force (Fig. 1c): this quantity drops sharply at the yielding transition, corresponding to the loss of contacts between droplets near the wall (right inset). As discussed in more detail below, another key feature is that droplets need to deform at least transiently when the system yields [26]. 

To quantify the yielding transition we compute two quantities: _(i)_ the mean velocity of the droplets’ center of mass _⟨vy⟩d,_ (Figs. 2a,c) and _(ii)_ the throughput flow _Q_ = � _dydz_ v _y_ (Figs. 2b,d). While _⟨vy⟩d_ quantifies the motility of the suspended particles, _Q_ can be used to compute the effective viscosity of the suspension, _η_ eff . The latter quantity can be estimated as _η_ eff = _η_ 0 _<u>QQ</u>_ <u>0</u><sup>,</sup> where _Q_ 0 = 12<sup>_<u>f</u>L_</sup> _η_<sup>3</sup> 0<sup>isthethroughputflowofaNewtonian</sup> fluid with viscosity _η_ 0 subject to a body-force _f_ , and _L_ the channel width. The yield-stress behavior is apparent from the plot of _⟨vy⟩d_ in Fig. 2a. Close to criticality, the mean droplet speed behaves as _∼_ ( _f − fc_ )<sup>_β_</sup> , with _β ≃_ 0 _._ 54 (dotted curve in the inset of Fig. 2a). The phenomenology resembles that of the Prandtl-Thomlinson model (where _β_ = 1 _/_ 2) which describes a particle in a dashboard potential, and provides a simple microscopic model for dry friction [27]. 

Importantly, even in the non-flowing phase in which droplets are at rest, the underlying solvent flows (Fig. 2b): indeed _Q_ is non-zero for all values of _f_ . In more detail we find that there is a well-defined linear regime at small forcing, which corresponds to a high but finite effective viscosity (inset of Fig. 2b). In stark contrast, yield-stress fluid under shear exhibit wall slip and an infinite effective viscosity [2]. This shows the exact value of _η_ eff depends on the geometry of the system, and hence 

can no longer be viewed one of its bulk material property. The flow at 0 _< f < fc_ is purely permeative, as the solvent flows through an immobile network of jammed droplets. The distinct behaviour of the droplet and solvent components in the suspension is instructive, and shows that the composite material behaves in a more complex way than what would be predicted for an ideal single-phase yield-stress fluid. In our conserved model, yielding can therefore be viewed as a continuous transition between a permeation regime with jammed amorphous droplets where solvent flows mainly around them, and a flowing ordered phase. In the latter phase, the flow is plug-like [13, 26], as found experimentally for colloidal suspensions in a pressure-driven flow [28]. 

It is interesting to contrast the behaviour we have just discussed with that of the non-conserved model, where evaporation and condensation effects are included. Surprisingly, replacing strict area conservation with a soft constraint leads to a complete loss of yield-stress behaviour (Figs. 2c,d). In the non-conserved model, droplets flow at any value of the forcing, however small, so that it is not possible to define a yield stress. While a yielding-like behaviour can still be observed as a smooth crossover, there is no longer a singularity in the droplet velocity curve (Fig. 2c). An analysis of the area of each droplet show that the droplet motion is accompanied by area oscillations whose magnitude in controlled by _λ_ , signalling that motion occurs via evaporation-condensation (inset of Fig. 2c). The behaviour of the throughput flow mirrors that of the droplet velocity in this non-conserved model (Fig. 2d) 

More insight into the fundamental difference between the conserved and non-conserved models can be gained by analysing the behaviour of a single droplet at a solid wall under an external forcing, and with neutral wet- 

4 



FIG. 2. **Flow behaviour in the conserved and nonconserved models** . **(a)-(b)** Average droplet velocity (a) and throughput flow (b) for the conserved model. The inset of panel (a) shows the mean droplet speed close to criticality and the result of the fit (dashed line) with the function _⟨v⟩∝_ ( _f − fc_ )<sup>_β_</sup> , with _β ≃_ 0 _._ 54. The inset of panel (b) shows the effective viscosity _η_ eff as a function of the body-force _f_ . **(c)(d)** Average droplet velocity (c) and throughput flow (d) for the non-conserved model. The inset of panel (c) shows the area of three nearby droplets versus time for _f_ = 1 _._ 0 _×_ 10<sup>_−_6</sup> . 

ting boundary conditions (Fig. S5 and Suppl. Movie 3). While in the conserved model the droplet sticks to the wall and requires a finite forcing to start moving, in the non-conserved model evaporation and condensation provide another pathway for contact line motion [29], and the droplet drifts along the wall for any value of the forcing. Therefore, besides the presence of a percolating network of droplet overlaps (Fig. 1), the existence of a well-defined yielding transition also requires a suitable behaviour of droplets close to the wall. 

To understand the microscopic mechanism underlying yielding in the conserved model more deeply, we now consider their dynamics close to _fc_ . Just after yielding, we find a “stick-slip” behaviour where the emulsion alternates between plug-like motion, where droplets flow, with stationary spells, where they are almost jammed (Suppl. Movie 4). The throughput solvent flow and the average droplet velocity both show irregular oscillations over time (red and orange curves in Fig. 3a). The average variance (or amplitude) of the stochastic oscillations increases with the forcing, and approaches zero at _fc_ (Fig. 3b). This behaviour is reminiscent of that found in velocity oscillations of colloidal glasses close to the yielding transition [18]. There are indeed some key qualitative analogies between the two cases. In both systems, the non-flowing and flowing states subtly differ in the typical particle configuration. In our non-flowing emulsions, overlaps between droplets abound and create a nearly percolating chain through the system, just like 



FIG. 3. **Oscillations near the yielding transition. (a)** Throughput flow versus time, for the conserved model, for different values of _f_ near _fc_ = 3 _._ 15 _×_ 10<sup>_−_6</sup> . **(b)** Plot of the variance of the oscillations as a function of _f_ . 

frictional contacts for hard-sphere colloids. Instead, in the flowing states there are gaps between most particles [18]. Analysing the dynamics in more details reveals an important distinction, though. In our system, instantaneous yielding events – i.e., transitions from jammed to flowing states – are typically accompanied by a sudden change in behaviour in the deformation free energy ( _F_ def =<sup>_<u>K</u>_</sup> 2 �� _i_<sup>(</sup><sup>_∇φi_)2</sup><sup>_dydz_, see [26]).This suggest that</sup> yielding in our deformable suspensions requires a transient change in droplet shape, which is instead essentially fixed for colloids. 

To verify that our qualitative mechanism for yielding through interfacial deformations is correct, we independently varied the parameters in Eq. 1 to see how they affect the value of the critical forcing. We found that _fc_ scales linearly with surface tension, _γ_ (Fig. 4a), and interfacial width, _ξ_ (see Fig. S6). The only other parameters appreciably affecting _fc_ are the system size _L_ and the droplet radius _R_ : increasing either of these lengthscales leads to a decrease in _fc_ (Fig. 4b). Our data therefore suggest that a key dimensionless parameter may be the capillary number _Ca_ = _fLR_<sup>2</sup> _/_ ( _γξ_ ), which was also empirically found to determine the physics of discontinuous shear thinning [13, 14, 19]. This can be viewed as an inverse Bingham number _σv/σy_ , with _σv ∼ fL_ the viscous stress and _σy ∼ γξ/R_<sup>2</sup> an effective yield stress. The form of this dimensionless control parameter suggests that in order for the suspension to yield the external forcing has to overcome free energy barriers associated with changes in particle shape, whose cost increases with _γ_ and _ξ_ . 

In summary, we studied the rheology of a soft droplet suspension under pressure-driven flow. We found that the droplets only start moving when the forcing they are subjected to exceeds a critical threshold, as in an ideal yield-stress fluid. However, unlike one such material, even when droplets are jammed the solvent flows through them via permeation, as in sheared cholesteric [30] and smectic liquid crystals [31], leading to an effective viscosity which depends on the system geometry and ceases to be a bulk property of the material. Yielding is accompanied by a morphological transition. The jammed 

5 



FIG. 4. **Yielding phase diagram. (a)** Phase diagram as a function of body-force _f_ and surface tension _γ_ . Orange squares: flowing systems; purple circles: non-moving states. **(b)** Phase diagram as a function of _f_ and system size _L_ plane. Red squares: flowing systems; blue circles: non-moving states. 

phase is amorphous and the network of droplet-droplet contacts, or overlaps, percolates in the direction perpendicular to the wall, conferring rigidity to the system. In the flowing phase, droplets order and contact percolation is lost. Within this picture, overlaps play a qualitatively similar role to frictional contacts in hard colloids [17]. In our case, though, the transition between the jammed and flowing phase requires a transient change in droplet shape. More quantitatively, yielding occurs for a sufficiently large value of an inverse Bingham number, controlling the balance between viscous and interfacial stresses. The mechanism is therefore similar to that determining discontinuous shear thinning at larger forcing [13, 14, 19]: the main difference is that at the yielding transition interfacial deformations are spatially localised and transient in time, whereas at the discontinuous shear thinning transitions they affect large portions of the system and occur at all times. Strikingly, we predict the yield-stress behaviour can be completely eliminated in our model by allowing droplet areas to fluctuate, for instance due to evaporation/condensation phenomena. We hope that our results will stimulate experiments to directly test our predictions, such as the importance of permeation and the scaling of _fc_ . To assess the universality of our results, one could investigate the yielding transition in other materials, such as biological tissues [32–34], red blood cell suspensions [35], and liquid crystalline emulsions [36]. 

## **ACKNOWLEDGMENTS** 

The work has been performed under the Project HPCEUROPA3 (INFRAIA-2016-1-730897), with the support of the EC Research Innovation Action under the H2020 Programme. Part of this work was carried out on the Dutch national e-infrastructure with the support of SURF through the Grant 2021.028 for computational 

time (L.N.C and G.N.). We acknowledge funding from MIUR Project No. PRIN 2020/PFCXPE. 

- [1] R. A. L. Jones, Soft Condensed Matter (Oxford University Press, New York, 2002). 

- [2] D. Bonn, M. M. Denn, L. Berthier, T. Divous and S. Manneville, Yield stress materials in soft condensed matter, _Rev. Mod. Phys._ **89** , 035002 (2017). 

- [3] W. Herschel and R. Bulkley, Konsistenzmessungen von Gummi-Benzoll¨osungen, _Kolloid Z._ **39** , 291 (1926). 

- [4] J. Ruiz-Franco, F. Camerin, N. Gnan, and E. Zaccarelli, _Phys. Rev. Materials_ **4** , 045601 (2020). 

- [5] J. P. Heller and M. S. Kuntamukkula, Critical review of the foam rheology literature, _Ind. Eng. Chem. Res._ **26** , 318-325 (1987). 

- [6] A. Z. Zinchenko and R. H. Davis, General rheology of highly concentrated emulsions with insoluble surfactants, _J. Fluid Mech._ **816** , 661 (2017). 

- [7] M. Cloitre, R. Borrega, F. Monti and L. Leibler, Glassy dynamics and flow properties of soft colloidal pastes, _Phys. Rev. Lett._ **90** , 068303 (2003). 

- [8] P. Pusey and W. van Megen, Phase behaviour of concentrated suspensions of nearly hard colloidal spheres, _Nature_ **320** , 340 (1986). 

- [9] K. N. Pham, G. Petekidis, D. Vlassopoulos, S. U. Egelhaaf, P. N. Pusey and W. C. K. Poon, Yielding of colloidal glasses, _Europhys. Lett._ **75** , 624 (2006). 

- [10] P. Sollich, F. Lequeux, P. Hebraud and M. E. Cates, Rheology of soft glassy materials, _Phys. Rev. Lett._ **78** , 2020 (1997). 

- [11] C. B. Holmes, M. Fuchs and M. E. Cates, Jamming transitions in a schematic model of suspension rheology, _Europhys. Lett._ **63** , 240 (2003). 

- [12] J. Paredes, M. A. J. Michels and D. Bonn, Rheology across the zero-temperature jamming transition, _Phys. Rev. Lett._ **111** , 105701 (2013). 

- [13] M. Foglino, A. N. Morozov, O. Henrich and D. Marenduzzo, Flow of deformable droplets: discontinuous shear thinning and velocity oscillations, _Phys. Rev. Lett._ **119** , 208002 (2017). 

- [14] M. Foglino, A. N. Morozov and D. Marenduzzo, Rheology and microrheology of deformable droplet suspensions, _Soft Matter_ **14** , 9361 (2018). 

- [15] A. Tiribocchi, A. Montessori, F. Bonaccorso, M. Lauricella and S. Succi, Concentrated phase emulsion with multicore morphology under shear: a numerical study, _Phys. Rev. Fluids_ **5** , 113606 (2020). 

- [16] N. Gnan and E. Zaccarelli, The microscopic role of deformation in the dynamics of soft colloids, _Nat. Phys._ **15** , 683–688 (2019). 

- [17] M. Wyart and M. E. Cates, Discontinous shear thickening without inertia in dense non-Brownian suspensions, _Phys. Rev. Lett._ **112** , 098302 (2014). 

- [18] L. Isa, R. Besseling, A. N. Morozov and W. C. K. Poon, Velocity oscillations in microfluidic flows of concentrated colloidal suspensions, _Phys. Rev. Lett._ **102** , 058302 (2009). 

- [19] L. Fei, A. Scagliarini, K. H. Luo and S. Succi, Discrete fluidization of dense monodisperse emulsions in neutral wetting microchannels, _Soft Matter_ , **16** , 651 (2020). 

6 

- [20] N.-Q. Nguyen and A. J. C. Ladd, Lubrication corrections for lattice-Boltzmann simulations of particle suspensions, _Phys. Rev. E_ **66** , 046702 (2002). 

- [21] I. Pagonabarraga, A. J. Wagner and M. E. Cates, Bindary fluid demixing: the crossover region, _J. Stat. Phys._ **107** , 39 (2002). 

- [22] M. E. Cates and E. Tjhung, Theories of binary fluid mixtures: from phase-separation kinetics to active emulsions, _J. Fluid Mech._ **836** , P1 (2017). 

- [23] A. Tiribocchi, N. Stella, G. Gonnella and A. Lamura, Hybrid lattice Boltzmann model for binary fluid mixtures, _Phys. Rev. E_ **80** , 026701 (2009). 

- [24] D. Marenduzzo, E. Orlandini, M. E. Cates and J. M. Yeomans, Steady-state hydrodynamic instabilities of active liquid crystals: hybrid lattice Boltzmann simulations, _Phys. Rev. E_ **76** , 031921 (2007). 

- [25] L. N. Carenza, G. Gonnella, A. Lamura, G. Negro and A. Tiribocchi, Lattice Boltzmann methods and active fluids, _Eur. Phys. J. E_ **42** , 81 (2019). 

- [26] See online Supplemental Material at XXX, which includes more simulation details, additional results and Refs. [37–39]. 

- [27] V. L. Popov, _Contact Mechanics and Friction._ Springer, Berlin, Heidelberg (2017). 

- [28] L. Isa, R. Besseling and W. C. K. Poon, Shear zones and wall slip in the capillary flow of concentrated colloidal suspensions, _Phys. Rev. Lett._ **98** , 198305 (2007). 

- [29] D. Bonn, J. Eggers, J. Indekeu, J. Meunier and E. Rolley, Wetting and spreading, _Rev. Mod. Phys._ **81** , 739 (2009). 

- [30] W. Helfrich, Capillary flow of cholesteric and smectic liquid crystals, _Phys. Rev. Lett._ **23** , 372 (1969). 

ative flows in 1 dimensionally ordered systems, _J. Phys. II_ **1** , 289 (1991). 

   - [32] D. Bi, X. Yang, M. C. Marchetti and M. L. Manning, Motility-driven glass and jamming transitions in biological tissues, _Phys. Rev. X_ **6** , 021011 (2016). 

   - [33] M. Chiang and D. Marenduzzo, Glass transitions in the cellular Potts model, _EPL_ **116** , 28009 (2016). 

   - [34] B. Loewe, M. Chiang, D. Marenduzzo and M. C. Marchetti, Solid-liquid transition of deformable and overlapping active particles, _Phys. Rev. Lett._ **125** , 038003 (2020). 

   - [35] G. R. L´azaro, A. Hern´andez-Machado and I. Pagonabarraga, Rheology of red blood cells under flow in highly confined microchannels: I. effect of elasticity, _Soft Matter_ **10** , 7195 (2014). 

   - [36] J. S. Lintuvuori, K. Stratford, M. E. Cates and D. Marenduzzo, Mixtures of Blue Phase Liquid Crystal with Simple Liquids: Elastic Emulsions, _Phys. Rev. Lett._ **121** , 037802 (2018). 

   - [37] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, A densitybased algorithm for discovering clusters in large spatial databases with noise, Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (1996). 

   - [38] L. N. Carenza, G. Gonnella, D. Marenduzzo, and G. Negro, Rotation and propulsion in 3D active chiral droplets, Proc. Natl. Acad. Sci. U.S.A. 116, 22065 (2019). 

   - [39] L. N. Carenza, G. Gonnella, D. Marenduzzo, and G. Negro, Chaotic and periodical dynamics of active chiral droplets, Physica (Amsterdam) 559A, 125025 (2020). 

- [31] J. Prost, Y. Pomeau and E. Guyon, Stability of perme- 

