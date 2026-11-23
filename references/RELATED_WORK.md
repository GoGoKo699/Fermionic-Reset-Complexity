# Related work and scope of the contribution

Literature and source versions checked on 30 October 2026. The bibliography is in [references.bib](references.bib). The comparisons below identify the models and theorem statements actually inspected; they are a scoped literature assessment, not an exhaustive priority certification.

## 1. The result being compared

The [Gaussian theorem](../science/gaussian_bound.md) optimizes vacuum population from the maximally mixed state of an entire register of $`n`$ fermionic modes. For Majoranas satisfying $`\{w_j,w_k\}=2\delta_{jk}I`$, linear jumps $`L_\alpha=l_\alpha^T w`$, and $`M=\sum_\alpha l_\alpha l_\alpha^\dagger`$, the charged resource is

```math
A=\int 2\mathrm{Tr}M(t)\,dt.
```
A single loss operator $`L=\sqrt\kappa\,c_1`$ therefore costs $`\int\kappa(t)\,dt`$; its occupation survival probability is $`e^{-A}`$. Arbitrary quadratic Hamiltonians, including pairing, and instantaneous Gaussian unitary pulses are free in this metric. The exact optimum is

```math
F_{\mathrm G}(n,A)=\left(1-\frac12e^{-A/n}\right)^n.
```
The [universal frontier](../science/universal-frontier.md) combines this state optimum with the parity decay mode to attain exact Gaussian error $`1-F_{\rm G}+2^{-n}e^{-A}`$. The [interacting result](../science/interacting-frontier.md) gives joint action $`\Theta(n+\ln(1/\epsilon))`$ for $`0<\epsilon\le1/2`$ and exponent $`1/2`$ at fixed $`n\ge2`$. Both classes are tested in half-diamond distance with the same single-port action.

Both classes may use input-independent classical randomness over Gaussian controls, with the action cap imposed on every realization. An averaged output need not be Gaussian; the converse is applied separately to each realization. No extra quantum modes, supplied pure workspace, measurement, postselection, bath-record feedback, or discarded system outputs are supplied. All input modes must be reset. The action metric leaves coherent gate synthesis, locality, strength, and duration uncharged. Accordingly, the hierarchy concerns dissipation action under ideal fast control; it does not by itself give a physical elapsed-time, circuit-complexity, heat, or work advantage.

## 2. Established ingredients and the specific addition

| Ingredient | Established source | Role in this repository |
|---|---|---|
| State control with one switchable amplitude-damping qubit | Bergholm and collaborators, 2012 and expanded 2016 preprints | Supplies the closest single-port antecedent and the sequential cooling benchmark. |
| Coherent redistribution of dissipation and contraction-volume constraints | Dive, Burgarth and Mintert, 2016 | Supplies the general control-theoretic perspective; a contraction identity alone does not optimize Gaussian purity. |
| Affine fermionic covariance dynamics and Gaussian spectral factorization | Onuma-Kalu et al., 2019; Barthel and Zhang, 2022; Surace and Tagliacozzo, 2022 | Supplies the representation used in the Gaussian proof. |
| Fast-unitary reduction to eigenvalue dynamics and coolability | Malvetti et al., 2025; Malvetti, 2024 | Supplies spectral-control and eigenvalue-inflow context. |
| Fermion-parity decay | Schulenborg et al., 2016 and Bruch et al., 2021 | Supplies the parity right mode used to identify the odd worst input. |
| Reversible entropy concentration and bath-assisted algorithmic cooling | Schulman and Vazirani, 1999; Boykin et al., 2002 | Supplies the compression mechanism used for attainability. |
| Reset operations assembled from nonunital noise and coherent compression | Ben-Or, Gottesman and Hassidim, 2013; Shtanko and Sharma, 2025 | Establishes the broader refrigeration paradigm. |

Complete positivity constrains the paired Gaussian spectral defects by $`\prod_j(1-\nu_j)\ge e^{-A}`$. Equal exposure saturates this constraint. The universal theorem additionally identifies the exact parity correction and shows how a parity twirl attains the corrected bound for arbitrary references. The interacting proof combines a no-jump determinant with balanced port matchings to obtain the joint action law and the fixed-size exponent.

## 3. Closest control-theoretic antecedents

### Single-port damping and the existing sequential benchmark

[Bergholm and Schulte-Herbrüggen, arXiv:1206.4945v2](https://arxiv.org/abs/1206.4945v2), and [Bergholm, Wilhelm and Schulte-Herbrüggen, arXiv:1605.06473v2](https://arxiv.org/abs/1605.06473v2), establish asymptotic state controllability using full coherent control and one switchable local amplitude-damping process. Example 1 of the expanded paper starts from $`I/2^n`$ and allocates equal damping exposure to each qubit. Its Eq. (7) already displays an $`n\log n`$ noise-time cost at fixed global Frobenius error, in addition to swap time. The earlier paper gives the corresponding example and Eq. (9).

Thus the sequential $`n\log n`$ benchmark is inherited. Those examples provide protocols, rather than a converse over the Gaussian control class. The inspected statements concern state transfer and use a different error metric; they do not establish the present reference-uniform channel comparison. The expanded paper's finite-temperature and partner-pairing discussion in Appendix B is also relevant algorithmic-cooling context.

### Fermion-parity relaxation

[Schulenborg et al., *Fermion-parity duality and energy relaxation in interacting open systems*](https://doi.org/10.1103/PhysRevB.93.081411), Eq. (5) and Supplemental Eq. (S-4), identify fermion parity as a right decay mode at the coupling rate in their weak-coupling transport model. [Bruch et al., *Fermionic duality: General symmetry of open systems with strong dissipation and memory*](https://arxiv.org/abs/2104.11202), Eq. (32), gives the time-propagator parity identity in a wide-band setting. For the prescribed Markovian schedule here, the CAR give the integrated-rate identity directly. Its role is to identify the worst input and connect the mixed-input optimum to an exact channel optimum.

### Contraction constraints

[Dive, Burgarth and Mintert, *Isotropy and control of dissipative quantum dynamics*, PRA 94, 012119 (2016)](https://doi.org/10.1103/PhysRevA.94.012119), derive constraints on dissipative evolution under coherent control, including a determinant relation for total contraction and restrictions on anisotropy and non-unitality. Their Sec. III and Eqs. (11)–(14) are direct antecedents for the idea that Hamiltonian control redistributes contraction without creating additional total contraction. Their concluding discussion identifies Gaussian systems as a further application. The present proof needs a bound on the lower half of the paired covariance spectrum and its relation to vacuum population; the determinant identity for the full dynamical map alone does not yield that bound.

### Fast-unitary spectral control

[Malvetti, vom Ende, Dirr and Schulte-Herbrüggen, *Reachability, Coolability, and Stabilizability of Open Markovian Quantum Systems with Fast Unitary Control*, SIAM J. Control Optim. 63, S53–S81 (2025)](https://doi.org/10.1137/23M1594467), is a particularly close general control reference. In the inspected [arXiv:2308.00561v1](https://arxiv.org/html/2308.00561v1), Sec. 2.2, Theorem 4 relates the full dynamics to controlled eigenvalue dynamics. Sec. 4.1, Theorem 26 characterizes asymptotic coolability and its equivalence to the existence of a suitable constant Hamiltonian with a unique attractive pure steady state. These are reachability statements. They do not optimize the finite integrated action as the number of fermionic modes grows or impose a Gaussian restriction. The published article's metadata and abstract were checked; the theorem comparison uses the accessible preprint, not the gated published full text.

[Malvetti, *Provably Time-Optimal Cooling of Markovian Quantum Systems*, arXiv:2403.05285v1](https://arxiv.org/html/2403.05285v1), studies optimal spectral control in small dimensions. Sec. VI.A.2 includes two qubits with a lowering operator on one, making the bath resource directly relevant. A qualification matters: Conjecture VI.3 identifies an achievable-derivative polytope, and the spin-spin analysis in Sec. VIII explicitly assumes that conjecture. This version must not be cited as an unconditional arbitrary-register optimum. Lemma VI.5 gives eigenvalue-inflow constraints related to the elementary largest-eigenvalue growth bound used here. The present proof states that bound directly and does not depend on the conjecture.

## 4. Gaussian dynamics and Gaussian cooling restrictions

### Fermionic covariance methods

[Onuma-Kalu, Grimmer, Mann and Martín-Martínez, *A classification of Markovian fermionic Gaussian master equations*, J. Phys. A 52, 435302 (2019)](https://doi.org/10.1088/1751-8121/ab40e1), gives the affine covariance equation and its complete-positivity constraints, particularly Eqs. (31)–(35) of [arXiv:1902.02239v2](https://arxiv.org/abs/1902.02239v2). Majorana and dissipator normalizations differ between references; this repository fixes the factors through the one-mode occupation law $`p(t)=e^{-\kappa t}p(0)`$.

[Barthel and Zhang, *Solving quasi-free and quadratic Lindblad master equations for open fermionic and bosonic systems*, J. Stat. Mech. (2022) 113101](https://doi.org/10.1088/1742-5468/ac8e5c), provides the covariance formalism, Gaussian-state evolution, and treatment of parity sectors. Proposition 1 of [arXiv:2112.08344v5](https://arxiv.org/abs/2112.08344v5) is especially relevant. Their broader class of quadratic master equations also permits quadratic Hermitian jump operators, which can produce non-Gaussian states. Those jumps are outside the Gaussian class used here: the allowed jumps are linear and the Hamiltonians quadratic.

[Surace and Tagliacozzo, *Fermionic Gaussian states: an introduction to numerical approaches*, SciPost Phys. Lect. Notes 54 (2022)](https://doi.org/10.21468/SciPostPhysLectNotes.54), gives a useful account of CAR, Majorana coordinates, covariance matrices, and density-matrix spectra. Sections 2.1–2.6 and 3.1–3.6 of [arXiv:2111.08343v2](https://arxiv.org/abs/2111.08343v2) cover the standard identities behind Gaussian spectral factorization.

### Bosonic thermal-operation restrictions

[Serafini et al., *Gaussian Thermal Operations and the Limits of Algorithmic Cooling*, PRL 124, 010602 (2020)](https://doi.org/10.1103/PhysRevLett.124.010602), characterizes bosonic Gaussian thermal operations. Its algorithmic-cooling result concerns a single bosonic mode without ancillary systems, allowing intervening unitaries, including non-Gaussian ones. The initial and bath entropies bound the obtainable entropy. This does not give a finite-action fermionic register bound: the system, available thermal operations, and resource accounting differ, and a zero-temperature entropy floor is zero. The comparison uses the model and algorithmic-cooling section of [arXiv:1909.06123v3](https://arxiv.org/abs/1909.06123v3).

[Png, Hu and Scarani, *Sub-Bath Cooling in Bosonic Systems: Gaussian Constraints and Non-Gaussian Enhancements*, PRX Quantum 7, 020316 (2026)](https://doi.org/10.1103/3qnz-6bcz), is a close conceptual comparison. Theorem 1 of [arXiv:2512.10703v2](https://arxiv.org/abs/2512.10703v2) characterizes the target temperatures reachable by Gaussian heat-bath algorithmic cooling in terms of machine frequencies. Theorem 2 and Sec. III.B analyze heat and swap ordering; Sec. IV studies non-Gaussian excitation exchanges. This establishes Gaussian cooling restrictions and non-Gaussian improvements for a bosonic target and thermal machines. It does not supply the finite loss-action optimum for resetting every retained mode of a fermionic register. The broad Gaussian/non-Gaussian cooling distinction is therefore background, while the task-specific action hierarchy requires its own theorem.

### Fermionic non-Gaussianity and Williamson majorization

[Turkeshi, Sierant and Tarabunga, *Williamson majorization theory of fermionic non-Gaussianity*, arXiv:2608.10140v2](https://arxiv.org/abs/2608.10140v2), constrains covariance Williamson spectra under Gaussian protocols. Theorem 1 treats pure inputs and pure output branches. The allowed resources include pure Gaussian ancillas, measurements, discards, and feedforward. Supplement S6 extends the argument to mixed inputs when the required measurement and discard records are retained, and explicitly limits the extension involving unrecorded discards. There is no integrated Markovian-rate budget. In particular, supplying a vacuum ancillary register and permitting swaps and discards changes the reset problem substantially. The shared covariance spectrum does not identify these theorems: the log-defect inequality here concerns finite dissipative exposure without additional modes.

## 5. Entropy compression, refrigeration, and convergence

[Schulman and Vazirani, *Molecular scale heat engines and scalable quantum computation*, STOC 1999, pp. 322–329](https://doi.org/10.1145/301250.301332), develops reversible polarization concentration near the information-theoretic limit. Its early preprint is titled [*Scalable NMR Quantum Computation*, arXiv:quant-ph/9804060v1](https://arxiv.org/abs/quant-ph/9804060v1). [Boykin, Mor, Roychowdhury, Vatan and Vrijen, *Algorithmic cooling and scalable NMR quantum computers*, PNAS 99, 3388–3393 (2002)](https://doi.org/10.1073/pnas.241641898), combines entropy compression with relaxation to a bath. These are primary sources for the mechanism in the interacting upper bound. Its classical tail estimate is the bounded-independent-variable inequality of [Hoeffding, JASA 58, 13–30 (1963), Theorem 2](https://doi.org/10.1080/01621459.1963.10500830). The parity-sector embedding and reference-uniform error accounting are proved explicitly in this repository.

[Ben-Or, Gottesman and Hassidim, *Quantum Refrigerator*, arXiv:1301.1995v1](https://arxiv.org/abs/1301.1995v1), studies computation without a continuing supply of fresh ancilla qubits. It is included as historical refrigeration context; its abstract and its role in the later work were checked, rather than undertaking a new full-proof audit.

[Shtanko and Sharma, *Complexity of Local Quantum Circuits under Nonunital Noise*, PRX Quantum 6, 030347 (2025)](https://doi.org/10.1103/xwz2-wfr4), constructs approximate reset operations using passive cooling, a coherent compressor, and a swap. The published article's Fig. 1, Secs. III.A–III.C, and Lemma 7 make the antecedent explicit. Their model counts noisy local-circuit depth and ancillary overhead; the reset target can use additional qubits initially in the maximally mixed state. Here every one of the $`n`$ input modes remains part of the required output, the port action is charged, and coherent compression is idealized as arbitrarily fast. The combination of randomized cooling and compression itself is established. The claimed separation rests on the Gaussian converse and the matched all-register reset accounting.

Two recent fermionic cooling analyses further clarify the error metric. [Zhan et al., *Rapid quantum ground state preparation via dissipative dynamics*, PRX 16, 011004 (2026)](https://doi.org/10.1103/wzb3-dbg9), relates quasi-free convergence in trace distance to a one-body non-Hermitian spectral gap; Theorem 1 and Eqs. (37)–(38) of [arXiv:2503.15827v3](https://arxiv.org/abs/2503.15827v3) concern specified generators. [Molpeceres, Lu, Cirac and Kraus, *Quantum algorithms for cooling: a simple case study*, Phys. Rev. Research 7, 033162 (2025)](https://doi.org/10.1103/4hx7-xnhw), distinguishes global convergence from local energy accuracy in a solvable fermionic model; the comparison uses Eqs. (25)–(28) and Appendix C of [arXiv:2503.24330v2](https://arxiv.org/abs/2503.24330v2). A logarithmic size penalty for global accuracy is therefore familiar. Neither inspected result is an optimization over all time-dependent Gaussian controls at fixed total action.

## 6. Related public research repositories

These comparisons use pinned public scientific files. They identify shared ingredients and different resource contracts without treating repository descriptions as substitutes for external literature.

| Repository and pinned source | Shared ingredient | Difference relevant to this theorem |
|---|---|---|
| [Boundary-Memory-Erasure: model](https://github.com/GoGoKo699/Boundary-Memory-Erasure/blob/7f9e4191fce6cdbec8119641caffadd6b5ad9553/science/model.md) and [erasure protocol](https://github.com/GoGoKo699/Boundary-Memory-Erasure/blob/7f9e4191fce6cdbec8119641caffadd6b5ad9553/science/erasure_protocol.md) | One-site nonunital control can export information, and a nearly pure intermediate state supports reference-decoupling. | The fixed order-preserving qutrit chain retains a spin-word memory; its final erasure target is maximally mixed. The $`O(L^3)`$ loss/refill protocol and unital obstruction depend on transport and bounded endpoint rates. Its Gaussian charge reduction is not an optimization over the full Gaussian control class. |
| [Noise-Assisted-Fermionic-Reset: reset theorem](https://github.com/GoGoKo699/Noise-Assisted-Fermionic-Reset/blob/25838345de4bb477f4ca2329d1825003bfeb3b15/science/reset_theorem.md) | A fully occupied witness supplies a finite-time strengthening in a number-conserving determinant argument. | That result covers a boundary-loss hopping chain and number-conserving phase trajectories. The universal frontier here includes general Gaussian pairing and attains the half-diamond optimum through an odd mixed-sector witness. |
| [Quantum-Mixing-Depth: model](https://github.com/GoGoKo699/Quantum-Mixing-Depth/blob/e059785fc822cb7701e12bffb97b60b95738aa3c/science/model.md) and [interpretation](https://github.com/GoGoKo699/Quantum-Mixing-Depth/blob/e059785fc822cb7701e12bffb97b60b95738aa3c/science/interpretation.md) | Coherent control changes the rate of complete-channel information loss under a prescribed bath. | The model uses local unitary layers and depolarization on every site, with no fresh control randomness. Geometry and operator spreading determine depth to the maximally mixed replacement channel. Pure-state reset and entropy concentration use a different mechanism and cost. |
| [Landauer-Bath-Threshold: compression](https://github.com/GoGoKo699/Landauer-Bath-Threshold/blob/c94a44d2ab3d81593de7e379386debe3b0e6e68b/science/compression.md) | A completed basis permutation maps a high-probability subspace into a reset sector, including an arbitrary reference. | The finite thermal bath is a supplied resource and heat is charged to it. Here bias is repeatedly generated in the same input register, no finite bath register is supplied as workspace, and every input mode is eventually reset using the Markovian port. |
| [Measurement-Free-Memory-Cost: model](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/9f1528066d8a53496855dc13da541cbfae7eb46c/science/model.md) and [control cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/9f1528066d8a53496855dc13da541cbfae7eb46c/science/control_cost.md) | A restricted coherent-control class has a quantitative limitation, and nonlinear processing can overcome it. | The task preserves unknown quantum information under depolarization. Clifford gates and fixed replacement resets are free, while non-Clifford processing is charged. Its memory-lifetime and continuing gate-budget bounds do not count the action needed to implement reset, which is the resource studied here. |

## 7. Read boundaries and remaining scope

The central comparisons used full primary text at the following specific locations. Publication metadata was cross-checked against arXiv, publisher records, or author-hosted copies. This does not imply a line-by-line review of every cited paper.

| Source | Version and inspected material |
|---|---|
| Bergholm et al. | 1206.4945v2 (12 December 2012): model, Theorems 1–2, Example 1/Eq. (9); 1605.06473v2 (20 April 2017): model, Example 1/Eq. (7), Appendix B/Theorem 4/Eq. (B41). |
| Dive et al. | 1509.07163v2 (5 August 2016): Sec. III, Eqs. (4)–(7), (11)–(14), (21)–(23), and conclusion. |
| Onuma-Kalu et al.; Barthel and Zhang | 1902.02239v2 (14 January 2020): covariance and complete positivity, Eqs. (31)–(35); 2112.08344v5 (2 February 2023): Proposition 1, Gaussian preservation and broader quadratic-jump distinction. |
| Malvetti and collaborators | 2308.00561v1 (1 August 2023): Sec. 2.2/Theorem 4 and Sec. 4.1/Theorem 26; 2403.05285v1 (8 March 2024): full/reduced model, Sec. VI.A.2, Conjecture VI.3, Lemma VI.5, and Sec. VIII. |
| Serafini et al.; Png et al. | 1909.06123v3 (20 January 2020): model and algorithmic-cooling section; 2512.10703v2 (4 May 2026): setup, Theorems 1–2, Secs. III–IV. |
| Turkeshi et al. | 2608.10140v2 (17 August 2026): operational model, Theorem 1, Supplement S6 and its mixed-state/record qualification. |
| Schulenborg et al. and Bruch et al. | [1508.06145](https://arxiv.org/pdf/1508.06145), Eq. (5) and Supplemental Eq. (S-4); [2104.11202](https://arxiv.org/pdf/2104.11202), Eq. (32), parity right mode. |
| Compression and refrigeration | Schulman–Vazirani early preprint and publication metadata; Boykin et al. published author copy; Hoeffding Theorem 2; Shtanko–Sharma published reset/compressor construction. Ben-Or et al. was screened at abstract level. |
| Public repository comparisons | Scientific files linked above at the displayed commits; no claim of a full audit of unrelated files or later revisions. |

The closest inspected accounts establish the fermion-parity mode, single-port controllability, sequential cooling and reversible compression. The remaining questions include the exact finite-action interacting error and the local synthesis cost of the permutations.
