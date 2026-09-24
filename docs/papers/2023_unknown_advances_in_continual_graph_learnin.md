---
title: "Advances in Continual Graph Learning for Anti-Money Laundering Systems: A Comprehensive Review"
authors: "unknown"
year: 2023
arxiv_id: "2309.11201"
original_file: "2309.11201.pdf"
pdf_path: "docs/papers\2023_unknown_advances_in_continual_graph_learnin.pdf"
---

# Advances in Continual Graph Learning for Anti-Money Laundering Systems: A Comprehensive Review

**Authors:** Unknown et al.  
**Year:** 2023 | **arXiv:** [`2309.11201`](https://arxiv.org/abs/2309.11201)  
**Local PDF:** [`2023_unknown_advances_in_continual_graph_learnin.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2023_unknown_advances_in_continual_graph_learnin.pdf)

---

# Noise-induced transition from superfluid to vortex state in two-dimensional nonequilibrium polariton condensates – semi-analytical treatment 

Vladimir N. Gladilin and Michiel Wouters 

TQC, Universiteit Antwerpen, Universiteitsplein 1, B-2610 Antwerpen, Belgium 

(Dated: September 21, 2023) 

We develop a semi-analytical description for the Berezinskii-Kosterlitz-Thouless (BKT) like phase transition in nonequilibrium Bose-Einstein condensates. Our theoretical analysis is based on a noisy generalized Gross-Pitaevskii equation. Above a critical strength of the noise, spontaneous vortexantivortex pairs are generated. We provide a semi-analytical determination of the transition point based on a linearized Bogoliubov analysis, to which some nonlinear corrections are added. We present two different approaches that are in agreement with our numerical calculations in a wide range of system parameters. We find that for small losses and not too small energy relaxation, the critical point approaches that of the equilibrium BKT transition. Furthermore, we find that losses tend to stabilize the ordered phase: keeping the other parameters constant and increasing the losses leads to a higher critical noise strength for the spontaneous generation of vortex-antivortex pairs. Our theoretical analysis is relevant for experiments on microcavity polaritons. 

## I. INTRODUCTION 

The interest in nonequilibrium phase transitions of quantum many body systems has witnessed a rapid growth over the last decade thanks to the developments in Bose-Einstein condensation in optical systems (microcavity polaritons and photons in dye filled cavities) [1], circuit QED [2] and ultracold atomic gases [3]. One of the most elementary phase transitions in these systems is the onset of Bose-Einstein condensation, defined as the emergence of spontaneous long range phase coherence. Where at thermal equilibrium, long range phase coherence appears when the temperature is lowered below a density-dependent critical temperature, in nonequilibrium systems, the phase coherence is determined by the interplay between the hamiltonian and dissipative parts of the dynamics or even between competing dissipative mechanisms [4, 5]. 

Since quantum fluids of light are only available in one or two dimensions, true long range order is actually absent. In one-dimensional bose gases, both at thermal equilibrium and out of equilibrium, the spatial decay of the first order coherence function is always exponential [6, 7]. In two dimensions and at equilibrium there is the celebrated Berezinskii-Kosterlitz-Thouless phase transition [8, 9] that separates the normal and the superfluid state, with exponential and algebraic decay of the spatial coherence respectively. In equilibrium, the phase dynamics is in the XY universality class and the corresponding universal jump in the superfluid stiffness has been experimentally observed in<sup>4</sup> He [10]. More recently, the flexibility of the platform of ultracold atoms allowed a direct observation of the spontaneous formation of vortexantivortex pairs above the BKT transition [11]. The ultracold atomic gases are in the weakly interacting regime, for which the transition temperature was computed by Prokof’ev and Svistunov by a clever combination of the linear Bogoliubov approximation and numerical Monte Carlo simulations [12]. 

For photonic systems out of equilibrium, the phase dy- 

namics is actually in the Kardar-Parisi-Zhang universality class where a nonlinear term in the phase evolution is essential [13, 14]. For one-dimensional polariton systems, the spatial decay of the correlations remains qualitatively unaffected by the nonlinearity in the phase dynamics [15], but a specific spatiotemporal scaling emerges, that was recently observed experimentally [16]. 

In two dimensions, the KPZ phase dynamics was predicted to make long range phase coherence impossible in isotropic systems [13, 17]. Numerical studies on the other hand have shown a transition toward a state with algebraic decay of the coherence [18] and an associated disappearance of vortex-antivortex pairs [18–21] without the formation of topological defects even when the spatiotemporal correlations feature KPZ scaling [22, 23]. Since computational resources limit the system sizes for numerical studies, the discrepancy between the renormalisation group studies could be due to finite size effects, but at present it does not seem that the issue is fully settled. Even when the numerically observed BKT transition is due to a limited system size, experimentally available systems necessarily also work with relatively small sizes, so that there is a clear interest in the nonequilibrium BKT transition. Compared to the equilibrium case, the current understanding of the dependence of the BKT critical point on the system parameters is much less mature. The reason herefore is twofold. First, out of equilibrium the standard Boltzmann-Gibbs ensemble can no longer be used and the steady state has to be characterized by a more involved simulation of the system dynamics. Second, the nonequilibrium dynamics is governed by more parameters: in addition to the system Hamiltonian and environment temperature, also the details of the coupling to the environment come into play in the non-equilibrium situation. 

In our previous work on photon condensation [24], we have pinpointed the nonequilibrium BKT critical point with numerical simulations and developed a semianalytical approach in order to get a better understanding of the location of the critical point. In our nu- 

2 

merical simulations, the transition was approached from the ordered side with no vortices present in the initial state. Above a critical value of the noise strength in the stochastic classical field description of the dynamics, vortex-antivortex pairs spontaneously appear, signalling the BKT like transition to the disordered state. Our work involved both numerical simulations and analytical approximations that capture the dependences of the transition point on all the system parameters. The analytical approximation for photon condensates was based on the Bogoliubov approximation, combined with an infrared cutoff set by the inverse vortex core size [25]. In our previous study on the BKT transition for (interacting) polaritons [20], no such analytical estimate was given. 

In the present article, we wish to fill this gap. Moreover, we extend our previous results to the regime of vanishing interactions, so that we can elucidate the effect of both the nonequilibrium condition and of interactions on the BKT transition point. When the interactions become small compared to the gain saturation nonlinearity, the vortex core size can significantly deviate from the usual healing length defined as ξ = ℏ/<sup>√</sup> mgn¯, where m is the mass, g the interaction constant and n¯ the density of polaritons in the condensate. The vortex core size appears in our treatment as a good proxy for the inverse of the infrared cutoff that we have to introduce to avoid the divergence of a momentum integral. We therefore carried out a systematic analysis of the vortex size and structure as a function of the strength of the interactions and of the driving and dissipation. 

The structure of this paper is as follows. In Sec. II, we introduce our model for polariton condensates and derive the density and phase flucutations within the linear (Bogoliubov) approximation. In Sec. III, we construct some approximate formulae for the BKT critical point with a few fitting parameters that are able to capture our numerical simulations. We start with a simple approach that is able to capture the main dependencies of the critical point on the system parameters and then present a more refined approach that allows for a very good fitting of the numerical results. Conclusions are drawn in Sec. IV and the vortex structure is discussed in appendix A. 

## II. MODEL AND LINEARIZATION 

We consider nonresonantly excited two-dimensional polariton condensates. In the case of sufficiently fast relaxation in the exciton reservoir, this reservoir can be adiabatically eliminated and the condensate is described by the noisy generalized Gross-Pitaevskii equation [26– 29] 



Here m is the effective mass and the contact interaction between polaritons is characterized by the strength g. The imaginary term in the square brackets on the right hand side describes the saturable pumping (with strength P and saturation density ns) that compensates for the losses (γ). We take into account the energy relaxation κ in the condensate [30]. The complex stochastic increments have the correlation function ⟨ξ<sup>∗</sup> (x, t)ξ(x<sup>′</sup> , t<sup>′</sup> )⟩ = 2δ(r − r<sup>′</sup> )δ(t − t<sup>′</sup> ). Eq.(1) is a classical stochastic field model that describes all the fluctuations in the system as classical. This model is therefore only valid in the weakly interacting regime gm/ℏ<sup>2</sup> ≪ 1, where quantum fluctuations are small. 

For κ = 0, the zero momentum steady state of Eq. (1) is under homogeneous pumping ψ0(x, t) =<sup>√</sup> n0e<sup>−ign0t</sup> , with n0 = ns(P/γ−1). By expressing the particle density |ψ|<sup>2</sup> in units of n0, dividing time by ℏ(1 + κ<sup>2</sup> )/n0, length by ℏ/<sup>√</sup> 2mn0, and noise intensity by ℏ<sup>3</sup> n0/(2m), Eq. (1) takes the form: 



where ν = n0/ns. The steady state density is then in the absence of noise given by [20] 



with c ≡ γ/(2gns). 

In order to gain some insight in the physics of the fluctuations induced by the noise in Eq. (2), one can consider in first approximation the linearized equations for the density and phase fluctuations around the steady state: 



After a spatial Fourier transform, these obey the linearized equations of motion 





where 



3 

Using the Ito formula [31], one can obtain from Eqs. (5) and (6) a set of three equations: 



where 



Eqs. (8)-(10) can be solved for the density and phase fluctuations and are accurate when they are small. Close to the BKT transition, this condition however breaks down. In the following, we will outline how these equations can still be used in order to obtain an estimate for the critical point, in analogy with our study of the BKT transition in photon condensates [24]. 

## III. APPROXIMATIONS FOR THE BKT CRITICAL POINT 

## A. Heuristic estimate of density-phase correlator 

In order to obtain our estimate of the critical point, we start by integrating Eq. (8) over all momenta. In the right hand side, we then use that for a homogeneous system 



When integrating the left-hand side of Eq. (8) over k, we assume the presence of a finite UV momentum (energy) cutoff k+ (ǫ+ = k+<sup>2).Ournumericalsimulations</sup> are performed for a lattice with grid size h, for which our UV cutoff equals k+ = π/h [i.e, ǫ+ = (π/h)<sup>2</sup> ]. Furthermore, one has to take into account that for the systems, described by nonlinear equations similar to Eq. (2), the use of the linear approximation given by Eq. (11) is physically meaningful [12, 24] only for k above a certain 

IR momentum (energy) cutoff k− (ǫ− = k−<sup>2).Thenthe</sup> Fourier transform of the left-hand side of Eq. (8) can be represented as D[C1+ln(ǫ+/ǫ−)]/(4πn¯), where the fitting constant C1 approximates the contribution of momenta smaller than k−. 

Physically, the correlator ⟨δθδn⟩ expresses correlations between the density and current fluctuations (since the velocity is the spatial derivative of the phase). In nonequilibrium condensates, density and velocity fluctuations are correlated because the particle balance equation: a local suppression of the density leads to local reduction of particle losses, which is compensated by an outward flow of particles. In the context of the BKT transition, this physics plays an important role, because the density in a vortex core is reduced so that vortices are accompanied by outgoing radial currents. The magnitude of the density-phase correlator was estimated in Ref. [24] for nonequilibrium photon condensates. Following this approach, for the system under consideration here, we obtain 



where δN =<sup>�</sup> 0<sup>xδn(x′)dx′.Inthecaseofaplanedensity</sup> wave n = n¯(1 − a cos kx) one has 



At the BKT transition, vortices have to nucleate, which requires in a continuum model strong density fluctuations with amplitude n¯ (i.e. a = 1) [24]. Those strong fluctuations have appreciable probability only for relatively large momenta k ∼ k+ as seen from the fact that the best fitting in Ref. [24] corresponds to the effective momentum value k ≈ 0.3k+ in Eq. (15). Therefore, we approximate the correlator ⟨δθδn⟩ by C2n¯γ/ǫ˜ +, where C2 ∼ 1 is a fitting parameter. 

Analogously, the Fourier transform of ⟨δθ−kδnk⟩ /ǫk in the last term of Eq. (8) is approximated by C3n¯γ/ǫ˜<sup>2</sup> + with a fitting constant C3. As a result, we obtain the following approximate expression for the critical noise 



where dBKT ≡ (D/n¯)|BKT. 

In line with Refs. [12, 24], we will assume that at the transition ⟨δθ<sup>2</sup> ⟩BKT = 1/2. In the equilibrium case (and at κ<sup>2</sup> ≪ 1) the IR momentum cutoff is inversely proportional to the healing length, so that the corresponding energy cutoff is ∼ gn¯. Since the healing length corresponds at equilibrium to the vortex core size, a natural generalization to the nonequilibrium situation is to take a cutoff based on an estimate of the vortex core size. Our estimation of the vortex core size, detailed in appendix 

4 

A, leads to 



where B0 = 0.524. The average density n¯ in Eq. (17) will be approximated by its steady-state value in the absence of noise (3). 

The results of fitting the numerical data for dBKT with Eq. (16) are represented by the dashed lines in Figs. 1 and 2 where the determined fitting parameters are C1 = 8.87, C2 = 1.64, and C3 = 5.92 × 10<sup>−5</sup> . The small numerical value of C3 implies it can actually be set to zero without affecting the quality of the fits. The numerical data in Figs. 1(a) and 2(a) and the main panels in Figs. 1(b) and 2(b) are taken from Ref. [20]. To numerically solve Eq. (2), a finite-difference scheme was used. Specifically, we use periodic boundary conditions for a square of size Lx = Ly = 40 with grid step equal to 0.2. The location of the critical point is determined in the following way: after a long time evolution in the presence of noise, the system was evolved without noise for a short time (few our units of time) before checking for the presence of vortices. This noiseless evolution gives the advantage of cleaning up the density and phase fluctuations while it is too short for the unbound vortex-antivortex pairs to recombine. The propensity for their recombination is reduced [20] with respect to the equilibrium case thanks to outgoing radial currents that provide an effective repulsion between vortices and antivortices. To determine the critical noise for the BKT transition, DBKT, we use the following criterion. If for a noise intensity D unbound vortex pairs are present after a noise exposure time tD (and hence D > DBKT), while for a certain noise intensity D<sup>′</sup> < D no vortex pairs appear even at noise exposures few times longer then tD, then D<sup>′</sup> lies either below DBKT or above DBKT and closer to DBKT then to D. Therefore, the critical noise intensity can be estimated as DBKT = D<sup>′</sup> ± (D − D<sup>′</sup> ). 

As seen from the comparison between the dashed lines and the symbols in Figs. 1 and 2, Eq. (16) qualitatively reproduces the main trends in the behavior of the numerically determined dBKT(c, κ, ν, h) at relatively small grid steps h, when ǫ+ is considerably larger than ǫ−. This qualitative agreement is ensured, in particular, by taking into account the contributions related to density-phase correlation, which are zero in equilibrium systems but play a crucial role for the BKT transition out of equilibrium. At the same time, this simple and transparent heuristic estimate of these contributions does not appear sufficient for a good quantitative description of the numerical results. 

## B. Bogoliubov theory with nonlinear correction 

In order to obtain a better quantitative description of the numerics for the nonequilibrium BKT transition, we 



FIG. 1. Numerically (symbols) and semi-analyticaly (lines) determined renormalized critical noise dBKT = DBKT/nBKT as a function of c = γ/(2nsg) (a), κ (b), and ν (c). The insets in panels (b) and (c) show the dependence of dBKT on κ and ν, respectively, in the case of g = 0. The solid and dashed lines correspond to Eqs. (26) and (16), respectively. 

5 





<!-- Start of picture text -->
(a)<br>(b)<br><!-- End of picture text -->

FIG. 2. Numerically (symbols) and semi-analyticaly (lines) determined renormalized critical noise dBKT as a function of the grid step at κ ≥ 0.1 (a) and κ = 0 (b) for nonzero g. Inset in panel (b): dBKT as a function of the grid step at g = 0. The solid and dashed lines correspond to Eqs. (26) and (16), respectively. 

develop below a different approach that leads to a slightly more involved expression. To this purpose, we start from the linear approximation for the phase fluctuations in the steady state, obtained by solving Eqs. (8)-(10). Inserting D/n¯ from Eq. (8) and from Eq. (10) into �|δnk/n¯|<sup>2�</sup> Eq. (9), we obtain the relation 



Using Eq. (18), we express ⟨δθ−kδnk/n¯⟩ through ⟨|δθk|<sup>2</sup> ⟩ and insert the result into Eq. (8). For the phase fluctuations, this leads to the equation 



where 



with 



From Eqs. (19) and (20), one sees that the phase fluctuations are, as expected, proportional to the noise strength D and decrease as a function of the density n¯ and energy relaxation κ. For what concerns their energy dependence, Eq. (20) shows a 1/ǫ behavior both at small and large energies. As a consequence, the Fourier transform of phase fluctuations, needed to obtain their real space correlations requires the introduction of an infrared cutoff ǫ−, analogous to the treatment in Sec. III A. As a result of Fourier transformation, the local phase variance becomes 



where 



where the logarithmic dependence on the lower and upper energy cutoffs is a consequence of the 1/ǫ behavior of f (ǫ) at low and high energies. The term 



in Eq. (22) approximates the contribution of the integral over ǫ from 0 to ǫ−, where C− is a fitting parameter. 

Expression (22), derived with the use of linearized equations for the phase and density fluctuations, is expected to be applicable when these fluctuations are small. As discussed above, at the BKT transition, where both phase and density fluctuations are large, the real-space correlator ⟨δθδn⟩ is mainly determined by the contributions of k ∼ k+. According to Eq. (18), the quantity ⟨|δθk|<sup>2</sup> ⟩ contains a term that is exactly proportional to ⟨δθ−kδnk⟩. This implies that at the BKT transition the expression for the phase fluctuations ⟨δθ<sup>2</sup> ⟩, derived above, needs an additional “nonlinear correction”, which would describe an enhanced contribution of large momenta k ∼ k+ (large energies ǫ ∼ ǫ+). Here, we approximate this correction by adding to F the term 



6 



FIG. 3. Renormalized critical noise dBKT/κ, given by Eq. (26), as a function of γ/g˜ and κ at three different values of ǫ+/ǫ−. 

where C+ is a fitting parameter. Then at the BKT point we have 



where again we take ⟨δθ<sup>2</sup> ⟩BKT = 1/2. 

Applying Eq. (26) to fit the numerical data for dBKT, we obtain for the two fitting parameters: C− = 2.24 and C+ = 7.33. As compared to the results of the heuristic approach described in the previous subsection (dashed lines in Figs. 1 and 2), the results corresponding to more involved and accurate Eq. (26), which are shown by the solid lines in Figs. 1 and, demonstrate a much better quantitative agreement with the numerically determined dBKT. 

The semi-analytical expression for dBKT, given by Eq. (26) together with Eqs. (17), (20), (21), and (23)(25), can be considered as a function of three independent parameters: γ/g˜ , κ and ǫ+/ǫ−. In Fig. 3, the renormalized critical noise dBKT/κ, corresponding to Eq. (26), is plotted for a wide range of the parameters γ/g˜ and κ at three different values of the ratio ǫ+/ǫ−. 

For small losses and not too small κ, the ratio dBKT/κ is of order one, in line with the equilibrium BKT transition where according to fluctuation-dissipation relation D = κT [32] and where the critical temperature scales 

in first approximation as TBKT ∼ n. In line with our previous studies for polariton condensates [20] and photon condensates [24], we see that the losses stabilize the ordered phase: when γ˜ is increased at fixed κ, the noise required to make the transition to the state with free vortex-antivortex pairs increases. We explained this trend by the reduction of the density fluctuations for increased driving and dissipation [20], that manifests itself through density-phase correlations [24] [see discussions preceding Eq. (16) and Eq. (25)]. 

In the limit without losses (˜γ = 0), our estimate for the critical point reduces to 



Here, we have used that TBKT = DBKT/κ, defined A1 = C+ + C− + log(π<sup>2</sup> /2) ≈ 11.2 and restored physical units. We can compare this expression with the equilibrium BKT transition for the weakly interacting lattice Bose gas (Eq. (12) in [12]) 



with A = 6080. This expression can be written as 



with 



Assuming here m<sup>2</sup> h<sup>2</sup> gTBKT ≈ 1, one obtains A2 ≈ 9.1, which is reasonably close to our A1 ≈ 11.5 given the simplicity of our approach and considering that the equilibrium case is actually a somewhat singular limiting case of our model where the gain and losses simultaneously tend to zero. 

## IV. CONCLUSIONS 

In this paper, we have developed a semi-analytical approach to describe the BKT transition point for drivendissipative weakly interacting Bose gases. We start from the linearized equations of motion for the density and phase fluctuations and subsequently correct phenomenlogically for nonlinearities that are important close to the BKT transition. Our resulting analytical formulae contain some fitting parameters that are fitted to a series of numerical simulations in a wide parameter range. The good fitting of our numerical results indicates the validity of the physical intuition underlying our semi-analytical approach and promotes our formulae to a concise summary of the numerical results. 

Of course, our numerical results were obtained for a finite size system and we can therefore not settle what 

7 

will happen for much larger system sizes, where it remains possible that the KPZ nonlinearity may destabilize the algebraically ordered phase [13, 17], even though recent numerical work has shown that KPZ scaling can be witnessed in 2D nonequilibrium condensates without the phase coherence being destabilized by the formation 

- [1] J. Bloch, I. Carusotto, and M. Wouters, Nature Reviews Physics 4, 470–488 (2022). 

- [2] I. Carusotto, A. A. Houck, A. J. Koll´ar, P. Roushan, D. I. Schuster, and J. Simon, Nature Physics 16, 268 (2020). 

- [3] R. Labouvie, B. Santra, S. Heun, and H. Ott, Phys. Rev. Lett. 116, 235302 (2016). 

- [4] M. Van Regemortel, Z.-P. Cian, A. Seif, H. Dehghani, and M. Hafezi, Physical Review Letters 126, 123604 (2021). 

- [5] S. Diehl, A. Micheli, A. Kantian, B. Kraus, H. B¨uchler, and P. Zoller, Nature Physics 4, 878 (2008). 

- [6] M. Wouters and I. Carusotto, Physical Review B 74, 245316 (2006). 

- [7] A. Chiocchetta and I. Carusotto, EPL (Europhysics Letters) 102, 67007 (2013). 

- [8] V. Berezinskii, Sov. Phys. JETP 32, 493 (1971). 

- [9] J. M. Kosterlitz and D. J. Thouless, Journal of Physics C: Solid State Physics 6, 1181 (1973). 

- [10] D. Bishop and J. Reppy, Physical Review Letters 40, 1727 (1978). 

of vortex antivortex pairs [22, 23]. 

## ACKNOWLEDGEMENTS 

We thank Iacopo Carusotto for continuous stimulating discussions. VG was financially supported by the FWOVlaanderen through grant nr. G061820N. 

   - [24] V. N. Gladilin and M. Wouters, Physical Review A 104, 043516 (2021). 

   - [25] V. N. Gladilin and M. Wouters, Physical Review Letters 125, 215301 (2020). 

   - [26] M. Wouters and V. Savona, Phys. Rev. B 79 (2009), 10.1103/PhysRevB.79.165302. 

   - [27] M. H. Szymanska, J. Keeling, and P. B. Littlewood, Phys. Rev. B 75 (2007), 10.1103/PhysRevB.75.195331. 

   - [28] L. M. Sieberer, M. Buchhold, and S. Diehl, Reports on Progress in Physics 79, 096001 (2016). 

   - [29] I. Carusotto and C. Ciuti, Rev. Mod. Phys. 85, 299 (2013). 

   - [30] M. Wouters, New Journal of Physics 14, 075020 (2012). 

   - [31] K. Jacobs, Stochastic processes for physicists: understanding noisy systems (Cambridge University Press, 2010). 

   - [32] P. C. Hohenberg and B. I. Halperin, Reviews of Modern Physics 49, 435 (1977). 

   - [33] V. N. Gladilin and M. Wouters, New Journal of Physics 19, 105005 (2017). 

- [11] Z. Hadzibabic, P. Kr¨uger, M. Cheneau, B. Battelier, and J. Dalibard, Nature 441, 1118 (2006). 

- [12] N. Prokof’ev, O. Ruebenacker, and B. Svistunov, Physical review letters 87, 270402 (2001). 

- [13] G. Wachtel, L. Sieberer, S. Diehl, and E. Altman, Physical Review B 94, 104520 (2016). 

- [14] K. Ji, V. N. Gladilin, and M. Wouters, Physical Review B 91, 045301 (2015). 

- [15] V. N. Gladilin, K. Ji, and M. Wouters, Physical Review A 90, 023615 (2014). 

- [16] Q. Fontaine, D. Squizzato, F. Baboux, I. Amelio, A. Lemaˆıtre, M. Morassi, I. Sagnes, L. Le Gratiet, A. Harouri, M. Wouters, et al., Nature 608, 687 (2022). 

- [17] E. Altman, L. M. Sieberer, L. Chen, S. Diehl, and J. Toner, Physical Review X 5, 011017 (2015). 

- [18] G. Dagvadorj, J. Fellows, S. Matyja´skiewicz, F. Marchetti, I. Carusotto, and M. Szyma´nska, Physical Review X 5, 041028 (2015). 

- [19] D. Caputo, D. Ballarini, G. Dagvadorj, C. S. Mu˜noz, M. De Giorgi, L. Dominici, K. West, L. N. Pfeiffer, G. Gigli, F. P. Laussy, et al., Nature materials 17, 145 (2018). 

- [20] V. N. Gladilin and M. Wouters, Phys. Rev. B 100, 214506 (2019). 

- [21] G. Dagvadorj, P. Comaron, and M. Szymanska, arXiv preprint arXiv:2208.04167 (2022). 

- [22] Q. Mei, K. Ji, and M. Wouters, Physical Review B 103, 045302 (2021). 

- [23] K. Deligiannis, Q. Fontaine, D. Squizzato, M. Richard, S. Ravets, J. Bloch, A. Minguzzi, and L. Canet, Physical Review Research 4, 043207 (2022). 

## Appendix A: Vortex density profile 

The vortex core size plays an important role in the BKT physics, because it provides the low energy cutoff in our analytical treatment. In this appendix, we discuss how the vortex core size depends on the system parameters through an approximate solution of the gGPE, that is shown to compare favorably with the exact numerical solution. 

We consider a single-quantum vortex in an infinite 2D condensate. Assuming that the vortex-center position is fixed, the density distribution is circularly symmetric and the order parameter can be written in the cylindrical coordinates ρ and φ as ψ = χ(ρ)e<sup>−iφ</sup> , so that the condensate density is given by n = |χ|<sup>2</sup> . Inserting this into the noise-free form of Eq. (2), one has 



For analytical estimates it is convenient to represent χ as χ(ρ) =<sup>√</sup> ny¯ (ρ)e<sup>iθ(ρ)</sup> , where the real function y(ρ) is normalized by 1. Then, taking into account that for a steady state ∂y/∂t = 0, while ∂θ/∂t = −µ(1 + κ<sup>2</sup> ) with 

8 

µ, the chemical potential, one obtains from Eq. (A1) the following two coupled stationary differential equations: 





In Eq. (A3), the first term corresponds to circulating vortex flows, while the second term in the right-hand side is due to outward radial flows from the vortex core [33]. Considering Eq. (A3) in the limit ρ →∞, one obtains for the chemical potential 



Note that in the equilibrium case, when ∂θ/∂ρ = 0, the right hand side of Eq. (A3) is obviously positive. In order to keep it positive also far from equilibrium, one has to assume that (∂θ/∂ρ)<sup>2��</sup> �ρ→∞<sup>isnonzero.Inotherwords,</sup> in the presence of a vortex the chemical potential of a nonequilibrium system should increase. 

In the limit ρ → 0, when (∂θ/∂ρ)<sup>2</sup> and y<sup>2</sup> become negligibly small, the general non-divergent solution of the “reduced” equation, resulting from Eq. (A3), is simply CJ1(qρ), where J1(x) is the Bessel function and q =<sup>√</sup> µ. Let us consider the “equilibrium-like” version of Eq. (A3): 



Its solution can be approximated by the normalized by one, non-oscillating function 



where x = sqρ. The parameters s and x∗ are determined from the following two requirements. (i) At small ρ, the function y1(ρ) should coincide with CJ1(qρ) ≈ C[qρ/2 − (qρ)<sup>3</sup> /16]. This leads to s = (1 + 4/x<sup>2</sup> ∗<sup>)−1/2.(ii)y1(ρ)</sup> should satisfy Eq. (A5) in the limit ρ →∞. In this limit, one has 1 − y1(ρ) ∝ ρ<sup>−2</sup> and Eq. (A5) becomes 



leading for x∗ to the equation J1<sup>′(x∗)</sup> �x<sup>3</sup> ∗<sup>+ 4x∗</sup> � = J1(x∗), which gives x∗ = 1.72 and, correspondingly, s = 0.653. As we will see later, in the case of weak non-equilibrium, the function 



describes almost perfectly the vortex density profiles, found in numerical simulations. Moreover, close to the vortex center, this function works quite well even at relatively strong deviations from equilibrium. This is not surprising: close to the vortex center, the vortex circulatingcurrent density, which is proportional to 1/ρ, is much stronger than the radial-current density, so that just the former governs the particle-density suppression. 

Let us estimate ∂θ/∂ρ, which determines the radial particle flow. At ρ →∞, the last term of Eq. (A2) (which is proportional to divjρ) vanishes, while y goes to 1, so that we have 



Therefore, Eq. (A2) can be rewritten as 



with p = νn/¯ (1 + νn¯). From Eq. (A10) one obtains 



where 



A finite nonzero value of ∂θ/∂ρ|ρ→∞ is possible only if we assume that at ρ →∞ 



Then we have from Eqs. (A11) and (A12) 



At moderate distances from the vortex center, the radial current density increases with ρ. For sufficiently large γ˜, the suppressive effect of redial currents on y<sup>2</sup> becomes dominating above certain ρ, so that the behavior described by Eq. (A13) emerges. 

In order ro determine the parameter R, let us consider the crossover between the two regimes, described by Eqs. (A8) and (A13). Let us start with the case of noninteracting particles, g = 0. The suppressive effect of the radial currents on the particle density is determined by (∂θ/∂ρ)<sup>2</sup> . At ρ below the crossover point, y in Eq. (A12) can be approximated by y1, so that Qp depends on ρ only through x (see Fig. 4). It seems natural to expect that the crossover occurs at a distance ρc, where the value of Qp(x) is close to its maximum. For simplicity, we will assume that the crossover point ρc(p) just corresponds to the position of this maximum, xm(p), i.e ρc = xm/(sq). 

9 



FIG. 4. Function Qp(x) with y = y1 for three different values of p. Inset: parameter Bp as a function of p. 

At the crossover point, the solution y1 for small ρ should match the solution for large ρ, described by Eq. (A13). This leads to 



with 



where, as seen from Eq. (A6), y1(ρc) is determined solely by xm(p). The numerically determined dependence of Bp on p is shown in the inset of Fig. A12. 

We can expect that in the general case, where the interparticle interaction is non-negligible, the crossover occurs when, with increasing ρ, the density of the radial current becomes comparable with that of the circulating current, so that [see Eq. (A11)], 



Obviously, with increasing g the suppressive effect of radial currents on the particle density becomes relatively weaker. Therefore, R should decrease with increasing g or decreasing γ (R = 0 at γ = 0). This means that at non-negligible g the matching condition at the crossover point, R/ρc = 1 − y1<sup>2(xc),correspondstoarathersmall</sup> value of 1 − y1<sup>2(xc),whichcan beapproximated [seeEqs.</sup> Eq. (A6), (A7)] by 1/(qρc)<sup>2</sup> . Then the matching condition becomes 1/ρc = Rq<sup>2</sup> . Inserting this into Eq. (A17), we obtain 



For simplicity, in the denominator q<sup>3</sup> we approximate R by the value given by Eq. (A15). The constant C is determined by requiring that in the limit g → 0 the R, given by Eq. (A18), fits Eq. (A15). Then for R we finally have 



From Eqs. (A4) and (A14) with (A19), we obtain the relation 



Equations (A20) and (A9) completely define the chemical potential µ and average density n¯, which, together with the parameter R given by Eq. (A19), enter the density distributions (A8) and (A13) at small and large ρ, respectively. As a “smooth interpolation” between these distributions, we introduce the function 



Obviously, this function can somewhat underestimate n at ρ ∼ R, close to the “bottom” of the vortex core. Apart from this, as seen from Fig. 5a, at g = 0 the function n2(ρ) approximates rather well the vortex shape, found by solving Eq. (A6) numerically, although the analytical values of n¯ appears not quite accurate for (experimentally less relevant) large κ (red curves) and large ν (green curves). For strongly interacting particles and/or for week deviations from equilibrium, when the parameter c = γ/(2nsg) is smaller than 1, the numerical results are almost perfectly described by the “equilibrium-like profile” n1(ρ) (see the black and red curves in Fig. 5b). For c > 1, the numerically determined n(ρ) at large ρ is well approximated by n2(ρ) (see the green and blue curves in Fig. 5b). 

The obtained results show that the µ given by Eq. (A20) (q<sup>−1</sup> = 1/<sup>√</sup> µ) adequately describes the chemical potential (vortex core size) in the systems under consideration. This implies that Eq. (A20) can provide a suitable estimate for the lower energy cutoff ǫ−. Since for experimentally relevant p < 0.9 the parameter Bp relatively weakly depends on p, in this estimate, for simplicity, we replace Bp with B0 = 0.524. 

10 



<!-- Start of picture text -->
(a)<br>(b)<br><!-- End of picture text -->





FIG. 5. Numerically (solid lines) and analytically (dotted and dashed lines) calculated density profiles for noninteracting particles (a) and three finite values of the parameter c = γ/(2nsg) (b) at different ν and κ. 

