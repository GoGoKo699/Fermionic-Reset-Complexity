# A 30-milestone map of fermionic reset complexity

This map describes the project's understanding targets for any reader. The canonical statements and proofs remain in the [scientific sources](../science/README.md). The milestones connect the physical task, the two control classes, and the arguments establishing their different dissipative costs; they do not attempt to cover every technical lemma or neighboring subject.

## Allocation and reading structure

**Background/preliminaries occupies M01–M12; narrative/innovation occupies M13–M30.** Twelve background milestones assemble finite-dimensional quantum information, fermionic structure, Markovian loss, and information concentration into one operational framework. Eighteen narrative milestones are needed because the result joins two substantial arguments: an optimized Gaussian obstruction and a universal interacting construction. Their combination also requires a general-control converse, a universal Gaussian upper bound, and careful interpretation of finite-size certificates.

Both phases progress from local to global. The background starts with one occupation and ends with a complete resource-and-error contract. The narrative starts with covariance evolution and a single compression stage, then builds complete protocols, matching asymptotic orders, and the physical meaning of the comparison. Dependencies name earlier milestones; a source pointer can lead to a later portion of a proof without making that whole proof a prerequisite.

| Range | Role in the scientific story |
| --- | --- |
| M01–M04 | States, references, channels, and observable error |
| M05–M09 | Fermionic controls, dissipative action, randomness, and concentration |
| M10–M12 | Composition of errors and the complete reset contract |
| M13–M18 | Gaussian spectral obstruction and its exact selected-input frontier |
| M19–M24 | A reference-uniform interacting protocol, from one stage to finite reset |
| M25–M27 | Converses and constructions establishing the universal hierarchy |
| M28–M30 | Finite certificates, quantitative limits, and integrated interpretation |

## The single educational anchor

The anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), and [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf). Section pointers below identify foundations relevant to each target, rather than prescribing entire chapters. Fermionic covariance, the Lindblad normalization, parity-respecting control, and the new bounds are supplied by the linked project sources and their primary references.

Two conventions require attention throughout. Watrous uses root fidelity, so vacuum population is the **square** of the book's fidelity with the vacuum. The book's unqualified logarithm has base two; this project uses natural logarithms for action and explicitly writes the binary entropy as $`h_2`$. The ordinary completely bounded trace norm is denoted by $`\|\cdot\|_\diamond`$ here, and reset error includes its factor of one half.

## Phase I: background/preliminaries

### M01 · Occupation and quantum states

- **Phase:** Background/preliminaries.
- **Central question:** What does it mean for one mode, and then a register, to be empty, uncertain, or coherent?
- **Understanding target:** Interpret occupation-basis density matrices, their eigenvalues, the vacuum, and the maximally mixed state $`\tau_n=I/2^n`$. Separate an occupation probability from a coherent amplitude and from a spectral eigenvalue.
- **Dependencies and story role:** None within the map. This establishes the local objects whose preparation cost will be compared.
- **Conceptual connection:** A reset target is a particular pure state in the same retained register; uncertainty is represented by the input density operator.
- **Source pointers:** [Watrous §§2.1.1–2.1.2](https://jhwatrous.github.io/TQI.2.pdf); [model §1](../science/model.md#1-register-reference-and-error); [Gaussian proof §1](../science/gaussian_bound.md#1-model-normalization-and-admissible-controls).

### M02 · Joint states and an inaccessible reference

- **Phase:** Background/preliminaries.
- **Central question:** Why can a register's own density matrix omit information relevant to reset?
- **Understanding target:** Distinguish a marginal state from a joint system-reference state, including classical correlations and entanglement. Interpret the target $`|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R`$ as reset with the reference marginal preserved.
- **Dependencies and story role:** M01. Expands the local occupation picture to the correlations a reusable register must lose.
- **Conceptual connection:** The reference is an arbitrary external system used to specify correctness; it is not a controlled ancillary workspace.
- **Source pointers:** [Watrous §§2.1.2–2.1.3](https://jhwatrous.github.io/TQI.2.pdf); [model §1](../science/model.md#1-register-reference-and-error); [interacting proof §1, Eq. (I1)](../science/interacting_reset.md#1-the-statement-and-its-resources).

### M03 · Physical evolution as a quantum channel

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical condition lets an operation act consistently on an unknown, correlated input?
- **Understanding target:** Identify complete positivity and trace preservation, channel composition, and identity extension to a reference. Distinguish unitary evolution, dissipative evolution, and the ideal replacement channel.
- **Dependencies and story role:** M01–M02. Supplies the common language for permitted protocols and their correctness criterion.
- **Conceptual connection:** A dilation is a representation of a channel; it does not grant the controller access to a pure ancilla or a fresh bath swap.
- **Source pointers:** [Watrous §§2.2.1–2.2.2, Theorem 2.22 and Corollary 2.27](https://jhwatrous.github.io/TQI.2.pdf); [model §§1–2](../science/model.md); [interacting proof §1](../science/interacting_reset.md#1-the-statement-and-its-resources).

### M04 · Measurable error and vacuum population

- **Phase:** Background/preliminaries.
- **Central question:** How does the chance of finding an excitation relate to distance from the reset target?
- **Understanding target:** Interpret $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$ through distinguishability. Recognize that vacuum measurement gives a lower bound on trace error, while equality requires additional structure; vacuum population is not generally a complete reference-sensitive certificate.
- **Dependencies and story role:** M01–M03. Connects a concrete measurement to the norm used in the proofs.
- **Conceptual connection:** Many small local occupation errors can produce a large global failure probability. The project's overlap convention differs from Watrous's root fidelity.
- **Source pointers:** [Watrous §3.1.1, Theorem 3.4, and §3.2, Definition 3.11](https://jhwatrous.github.io/TQI.3.pdf); [Gaussian proof §7, Eq. (32)](../science/gaussian_bound.md#7-attainment-by-equal-exposure); [interpretation: global reset](../science/interpretation.md#global-reset-requires-more-than-small-local-occupation).

### M05 · Fermionic operators and parity

- **Phase:** Background/preliminaries.
- **Central question:** Which physical structure is hidden by writing the occupation space as $`n`$ binary factors?
- **Understanding target:** Relate annihilation operators, Majoranas, the canonical anticommutation relations, and total parity. Distinguish a parity-preserving unitary from a number-conserving one, and recognize why fermionic loss can carry a parity string in a tensor representation.
- **Dependencies and story role:** M01–M03. Identifies the symmetry and operator algebra that both control classes must respect.
- **Conceptual connection:** The binary occupation basis supports ordinary channel mathematics, while the CAR determine which transformations and locality statements are physically valid.
- **Source pointers:** [Watrous §§2.1.1–2.1.2](https://jhwatrous.github.io/TQI.2.pdf) for register notation only; [model §1](../science/model.md#1-register-reference-and-error); [Gaussian proof §1](../science/gaussian_bound.md#1-model-normalization-and-admissible-controls); [interacting proof: fermionic suffix](../science/interacting_reset.md#why-a-fermionic-suffix-is-legitimate).

### M06 · Gaussian covariance and binary spectral factors

- **Phase:** Background/preliminaries.
- **Central question:** What information makes fermionic Gaussian dynamics especially constrained?
- **Understanding target:** Relate an even Gaussian state's covariance to paired magnitudes $`\nu_j`$ and binary density-spectrum factors $`(1\pm\nu_j)/2`$. Understand that quadratic unitaries, including pairing, rotate the covariance without changing these spectral magnitudes; a general state need not be determined by its covariance.
- **Dependencies and story role:** M01, M05. Supplies the reduced description on which the Gaussian converse operates.
- **Conceptual connection:** The defects $`\delta_j=1-\nu_j`$ quantify residual mixedness in canonical modes, linking a small matrix to the register's largest eigenvalue.
- **Source pointers:** [Watrous §1.1](https://jhwatrous.github.io/TQI.1.pdf) for spectral foundations; [Gaussian proof §§4 and 6](../science/gaussian_bound.md#4-spectral-pairing-at-degeneracies); [related work: covariance methods](../references/RELATED_WORK.md#fermionic-covariance-methods).

### M07 · Loss exposure and the charged resource

- **Phase:** Background/preliminaries.
- **Central question:** What is paid for when a mode is cooled through the loss port?
- **Understanding target:** Read the vacuum-loss generator and its survival law $`q=e^{-a}`$. Interpret total action as integrated damping strength, including the sum of rates for parallel ports, and distinguish it from elapsed time or coherent gate cost.
- **Dependencies and story role:** M03, M05–M06. Connects the dynamics to a normalized resource shared by both classes.
- **Conceptual connection:** Gaussian routing lets one physical port expose different existing modes; adding ports does not supply free action.
- **Source pointers:** [Watrous §§2.2.1–2.2.2](https://jhwatrous.github.io/TQI.2.pdf) for channel foundations; [model §2](../science/model.md#2-the-common-loss-resource); [Gaussian proof §2, Eqs. (10)–(11)](../science/gaussian_bound.md#2-covariance-equation-and-physical-rate).

### M08 · Random control without a purity resource

- **Phase:** Background/preliminaries.
- **Central question:** What changes when the controller uses a classical random seed and then ignores it?
- **Understanding target:** Distinguish a conditioned control branch from the averaged channel. Recognize that random unitary averaging is unital, that a mixture of Gaussian branches need not be Gaussian, and that a pathwise action cap bounds every realization rather than only its mean.
- **Dependencies and story role:** M03, M06–M07. Fixes the randomization resource before it enters either argument.
- **Conceptual connection:** The same input-independent randomness is available to both classes; it can standardize unknown input information while fixing the maximally mixed state.
- **Source pointers:** [Watrous §§2.1.2 and 2.2.1](https://jhwatrous.github.io/TQI.2.pdf); [model §3](../science/model.md#3-coherent-control-classes); [interpretation: randomization](../science/interpretation.md#what-the-randomization-does).

### M09 · Bias, concentration, and reversible storage of uncertainty

- **Phase:** Background/preliminaries.
- **Central question:** Why can many biased occupations store their uncertainty in fewer modes?
- **Understanding target:** Connect binary entropy, concentration of probability on a restricted set of strings, and the dimension needed to store those strings. A reversible rearrangement preserves the full spectrum and entropy while relocating uncertainty between subsystems.
- **Dependencies and story role:** M01–M02, M05, M07. Introduces the information-concentration mechanism that interactions will implement.
- **Conceptual connection:** Source coding supplies the counting intuition; the reset protocol additionally needs a reversible parity-preserving embedding using only the original modes.
- **Source pointers:** [Watrous §§5.1.1, 5.2.1, and 5.3.1](https://jhwatrous.github.io/TQI.5.pdf); [Watrous §1.2.2, Theorem 1.16](https://jhwatrous.github.io/TQI.1.pdf) for concentration background; [interacting proof §4](../science/interacting_reset.md#4-reversible-compression-inside-each-parity-sector), including its precise one-sided Hoeffding bound.

### M10 · Comparison states and composable error bounds

- **Phase:** Background/preliminaries.
- **Central question:** How can a multistage proof use ideal states without supplying ideal reset as a physical operation?
- **Understanding target:** Combine trace-distance contractivity with the triangle inequality to track a real state against a sequence of comparison states. Distinguish a mathematical replacement used in a proof from a channel available to the controller.
- **Dependencies and story role:** M02–M04, M08–M09. Assembles the error-accounting tools needed to move from one stage to a complete protocol.
- **Conceptual connection:** Applying the same physical channel to real and comparison states controls pre-existing error, even when the active block remains correlated with a reference.
- **Source pointers:** [Watrous §§3.3.1–3.3.2, including Proposition 3.48](https://jhwatrous.github.io/TQI.3.pdf); [interacting proof §4, Eq. (I16)](../science/interacting_reset.md#turning-a-probability-bound-into-joint-trace-distance); [interacting proof §5](../science/interacting_reset.md#5-repeating-the-stage-without-losing-the-reference-guarantee).

### M11 · Universal reset as an ordinary channel-norm task

- **Phase:** Background/preliminaries.
- **Central question:** What single condition guarantees reset for every unknown input and reference?
- **Understanding target:** Interpret $`\tfrac12\|\Phi-\mathcal R_n\|_\diamond`$ as the worst joint-state trace error. Understand why a reference dimension $`2^n`$ suffices and why the ordinary matrix-algebra norm used here includes arbitrary coherences, exceeding a restriction to parity-compatible tests.
- **Dependencies and story role:** M02–M05, M10. Integrates states, channels, and errors into the operational success criterion.
- **Conceptual connection:** A reference-uniform upper bound solves a stronger task than preparation from one witness state; the norm itself supplies no additional controlled system.
- **Source pointers:** [Watrous §§3.3.2–3.3.3, Definition 3.43 and Theorems 3.46 and 3.51](https://jhwatrous.github.io/TQI.3.pdf); [model §1](../science/model.md#1-register-reference-and-error); [interacting proof Eq. (I1)](../science/interacting_reset.md#1-the-statement-and-its-resources).

### M12 · The complete matched comparison

- **Phase:** Background/preliminaries.
- **Central question:** Which differences between the controllers are allowed to explain a difference in reset cost?
- **Understanding target:** State the common loss port, randomization, pathwise budget, retained output, and universal error target. Separate quadratic control with pairing from arbitrary fast parity-preserving control, and distinguish the selected-input cost $`A_{\rm G}^{\tau}`$ from the universal costs $`A_{\rm G}`$ and $`A_{\rm I}`$.
- **Dependencies and story role:** M01–M11. Completes the background phase by joining the physical system, information task, and optimization domain.
- **Conceptual connection:** Pure ancillary workspace, measurements, postselection, and bath-record feedback are absent; nonlocal nonlinear synthesis remains unpriced. These assumptions define what the coming hierarchy means.
- **Source pointers:** [Watrous §§2.2.1–2.2.2](https://jhwatrous.github.io/TQI.2.pdf) and [§§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf) for the underlying channel framework; [model §§1–5](../science/model.md).

## Phase II: narrative/innovation

### M13 · Complete positivity as a spectral resource inequality

- **Phase:** Narrative/innovation.
- **Central question:** How does the physical damping rate enter covariance evolution?
- **Understanding target:** Connect the linear-jump matrix $`M\succeq0`$ to $`\dot G=XG+GX^T+D`$, with $`G=I+i\gamma`$, $`D=4M\succeq0`$, and $`\mathrm{Tr}X=-\Gamma`$. Identify why this covers arbitrary linear jumps while retaining the single-port action normalization.
- **Dependencies and story role:** M03, M06–M07, M12. Establishes the local dynamical identity from which the converse grows.
- **Conceptual connection:** Complete positivity provides the sign of the affine term; coherent rotations do not contribute to the trace cost.
- **Source pointers:** [Watrous §2.2.2, Theorem 2.22](https://jhwatrous.github.io/TQI.2.pdf) for complete positivity; [Gaussian proof §2 and Eq. (13)](../science/gaussian_bound.md#2-covariance-equation-and-physical-rate); [model §4](../science/model.md#4-a-larger-gaussian-class-for-the-converse).

### M14 · A valid spectral argument at finite action

- **Phase:** Narrative/innovation.
- **Central question:** Why do logarithms and eigenvalue derivatives remain legitimate under arbitrary admissible Gaussian controls?
- **Understanding target:** Relate the variation-of-constants positivity bound to strictly positive defects at finite action. Understand the role of absolute continuity and conjugate spectral pairing at degeneracies, including zero covariance, without assuming globally smooth eigenvectors or isolated crossings.
- **Dependencies and story role:** M06–M07, M13. Makes the forthcoming differential argument valid for the full control class, pulses, and limits.
- **Conceptual connection:** A physically meaningful converse must survive the singular-looking cases where a convenient eigenbasis changes.
- **Source pointers:** [Watrous §1.1](https://jhwatrous.github.io/TQI.1.pdf) for Hermitian spectral foundations; [Gaussian proof §§3–4, Eqs. (14)–(20)](../science/gaussian_bound.md#3-finite-action-positivity) for the positivity and almost-everywhere argument supplied here.

### M15 · The integrated Gaussian defect budget

- **Phase:** Narrative/innovation.
- **Central question:** What can no quadratic control schedule improve at fixed action?
- **Understanding target:** Explain how paired eigenvectors recover $`\mathrm{Tr}X`$ and how $`D\succeq0`$ yields $`\frac{d}{dt}\sum_j\ln\delta_j\ge-\Gamma`$, hence $`\prod_j\delta_j\ge e^{-A}`$ from the maximally mixed input. Keep the direction of this lower bound on the defect product explicit.
- **Dependencies and story role:** M13–M14. Converts local evolution into the global resource obstruction.
- **Conceptual connection:** Unitary rotations preserve the defects; loss can reduce their product only at a rate paid for by the integrated bath strength.
- **Source pointers:** [Watrous §1.1](https://jhwatrous.github.io/TQI.1.pdf) for trace and spectral notation; [Gaussian proof §5, Eqs. (21)–(25)](../science/gaussian_bound.md#5-integrated-log-defect-inequality).

### M16 · From a product constraint to the exact overlap bound

- **Phase:** Narrative/innovation.
- **Central question:** Why does evenly distributed Gaussian purification maximize pure-state overlap?
- **Understanding target:** Connect $`\lambda_{\max}=\prod_j(1-\delta_j/2)`$ with concavity and monotonicity of $`\ln(1-e^x/2)`$. Recover the upper frontier $`(1-\tfrac12e^{-A/n})^n`$ and understand why it survives random-branch averaging even though the averaged state may not be Gaussian.
- **Dependencies and story role:** M04, M06, M08, M15. Turns the defect obstruction into an operational bound.
- **Conceptual connection:** A branchwise structural theorem extends to the average by linearity of target population and convexity of the largest eigenvalue, under the pathwise cap.
- **Source pointers:** [Watrous §1.2.2, Theorem 1.14](https://jhwatrous.github.io/TQI.1.pdf) for Jensen's inequality; [Gaussian proof §6, Eqs. (26)–(29)](../science/gaussian_bound.md#6-exact-fidelity-bound).

### M17 · Attainment with one port and equal exposure

- **Phase:** Narrative/innovation.
- **Central question:** Is the Gaussian bound only a restriction, or can a permitted protocol reach it?
- **Understanding target:** Follow equal exposure $`A/n`$ of each initially maximally mixed mode, producing populations $`e^{-A/n}/2`$. Explain why Gaussian routing through one port attains the frontier and why the resulting diagonal state's trace error equals one minus its vacuum population.
- **Dependencies and story role:** M04, M07, M16. Completes the optimization for the specified input.
- **Conceptual connection:** A converse proved for a larger linear-jump class is already tight in the smaller single-port model, so extra linear bath orientations provide no improvement for this task.
- **Source pointers:** [Watrous §§2.1.2 and 2.2.1](https://jhwatrous.github.io/TQI.2.pdf); [Gaussian proof §7, Eqs. (30)–(32)](../science/gaussian_bound.md#7-attainment-by-equal-exposure).

### M18 · A selected-input optimum becomes a universal converse

- **Phase:** Narrative/innovation.
- **Central question:** What does the exact Gaussian frontier establish about unknown-input reset?
- **Understanding target:** Interpret its inverse $`A_{\rm G}^{\tau}(n,\epsilon)`$, including zero-action and exact-reset endpoints. Explain the fixed-error law $`n\ln n+O_\epsilon(n)`$ and the implication $`A_{\rm G}\ge A_{\rm G}^{\tau}`$ without identifying an exact finite-action universal optimum.
- **Dependencies and story role:** M11–M12, M16–M17. Integrates the Gaussian arc into the full task as a necessary bound.
- **Conceptual connection:** Universal correctness must pass the maximally mixed witness; successful preparation of that witness alone cannot establish universal correctness.
- **Source pointers:** [Watrous §§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf); [Gaussian proof §8, Eqs. (33)–(34)](../science/gaussian_bound.md#8-error-thresholds-and-asymptotics); [model §5](../science/model.md#5-exact-state-frontier-and-universal-hierarchy).

### M19 · Twirling an unknown block while retaining its reference

- **Phase:** Narrative/innovation.
- **Central question:** How can an input-independent Gaussian operation simplify every active-block input?
- **Understanding target:** Explain why averaging even Majorana monomials leaves only identity and parity terms. Interpret the exact joint output $`I/2^m\otimes\rho_R+P_m/2^m\otimes\Delta_R`$, with $`\|\Delta_R\|_1\le1`$, including the parity-dependent information that survives.
- **Dependencies and story role:** M02–M03, M05, M08, M12. Starts the universal construction with a controlled reduction of arbitrary input structure.
- **Conceptual connection:** The twirl is shared unital randomness, not purification or conditional decoupling given its seed; its guarantee concerns the averaged channel.
- **Source pointers:** [Watrous §§2.1.2–2.1.3 and 2.2.1](https://jhwatrous.github.io/TQI.2.pdf); [interacting proof §2, Eqs. (I5)–(I8)](../science/interacting_reset.md#2-an-even-gaussian-twirl-preserves-only-parity-information).

### M20 · Loss suppresses the surviving parity information

- **Phase:** Narrative/innovation.
- **Central question:** Why does constant exposure make a large unknown block comparable to independent biased bits?
- **Understanding target:** Relate equal survival $`q`$ to the comparison state $`\sigma_q^{\otimes m}\otimes\rho_R`$ and the exact residual term $`q^mP_m\otimes\Delta_R/2^m`$. Identify its trace-distance bound $`q^m/2`$ and the action $`m\ln(1/q)`$.
- **Dependencies and story role:** M04–M05, M07, M19. Supplies a quantitative bridge from arbitrary quantum input to classical concentration.
- **Conceptual connection:** Jordan–Wigner signs cancel on occupation-diagonal operators with reference coefficients; independent damping is justified on this algebra, not assumed on arbitrary fermionic tensor factors.
- **Source pointers:** [Watrous §§2.1.3 and 2.2.1](https://jhwatrous.github.io/TQI.2.pdf); [interacting proof §3, Eqs. (I9)–(I10)](../science/interacting_reset.md#3-finite-loss-exposure-suppresses-the-remaining-parity-term).

### M21 · Parity-preserving compression within the existing block

- **Phase:** Narrative/innovation.
- **Central question:** How can likely occupation strings be concentrated without violating parity or adding clean modes?
- **Understanding target:** Connect the count $`|T_{m,r}|\le2^{mh_2(r)}`$ to separate even and odd trash-sector capacities. Understand the extra-mode allowance, completion to a reversible permutation, and the exponentially small excluded probability for $`p=q/2\lt r\lt 1/2`$.
- **Dependencies and story role:** M05, M09, M20. Establishes the nonlinear operation that turns local bias into a shorter active block.
- **Conceptual connection:** The unitary relocates uncertainty while preserving the spectrum; the bath, rather than the permutation, removes entropy.
- **Source pointers:** [Watrous §§5.1.1 and 5.3.1](https://jhwatrous.github.io/TQI.5.pdf); [Watrous §1.2.2, Theorem 1.16](https://jhwatrous.github.io/TQI.1.pdf) for concentration background; [interacting proof §4, Eqs. (I13)–(I15)](../science/interacting_reset.md#counting-good-strings), with the primary one-sided tail attribution there.

### M22 · A probability bound becomes a joint-state stage guarantee

- **Phase:** Narrative/innovation.
- **Central question:** Why does a small bad-string probability suffice despite arbitrary reference correlations?
- **Understanding target:** Interpret the exact identity $`D(\theta,\mathcal Q_B\theta)=\Pr(B\ne0)`$ for a classical prefix with positive operator-valued coefficients. Combine it with the parity residue to obtain one-stage error $`e^{-2m(r-p)^2}+q^m/2`$ and a comparison state with unchanged reference marginal.
- **Dependencies and story role:** M02, M04, M10, M20–M21. Completes the local compression lemma in the metric required by reset.
- **Conceptual connection:** The probability-to-distance step avoids an unnecessary square-root loss; the analytical prefix replacement is not an extra physical reset resource.
- **Source pointers:** [Watrous §3.1.1](https://jhwatrous.github.io/TQI.3.pdf); [interacting proof Lemma I1 and Eq. (I16)](../science/interacting_reset.md#lemma-i1-one-compression-stage).

### M23 · Retaining a cold prefix through successive stages

- **Phase:** Narrative/innovation.
- **Central question:** How can the controller keep shrinking the active block without losing the guarantee on earlier modes?
- **Understanding target:** Explain the CAR form $`c_j=P_F\otimes\widetilde c_j`$ and why it gives exact active-block dynamics on the ideal vacuum prefix. Use the same physical channel on real and comparison states to obtain additive stage errors, retaining every output mode and the reference marginal.
- **Dependencies and story role:** M05, M10–M11, M22. Lifts the local lemma into a valid recursive construction.
- **Conceptual connection:** The proof does not treat imperfectly cooled modes as supplied pure workspace, nor assume tensor-local loss on an arbitrary prefix.
- **Source pointers:** [Watrous §3.3.2, Proposition 3.48](https://jhwatrous.github.io/TQI.3.pdf) for composability; [interacting proof §5, especially Eq. (I20)](../science/interacting_reset.md#5-repeating-the-stage-without-losing-the-reference-guarantee).

### M24 · A complete finite protocol with linear action

- **Phase:** Narrative/innovation.
- **Central question:** How do shrinking active blocks yield a universal reset protocol for every finite register?
- **Understanding target:** Combine geometric contraction, a summable stage-error bound, a fixed error-dependent stopping size, and final twirl-and-loss cleanup. Explain why small registers use cleanup directly and why deterministic sizes and exposures give $`A\le Cn+C_\epsilon`$ on every random branch.
- **Dependencies and story role:** M07–M08, M11, M21–M23. Completes the interacting upper bound, including references and finite-size endpoints.
- **Conceptual connection:** Most modes receive only a bounded amount of damping before their uncertainty is concentrated into the shrinking suffix; the final high-accuracy cost is confined to the small remaining block.
- **Source pointers:** [Watrous §§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf) for the norm contract; [interacting proof Theorem I and §§5–6, Eqs. (I17)–(I25)](../science/interacting_reset.md#theorem-i-linear-action-for-the-interacting-class).

### M25 · A converse even with unrestricted coherent rearrangement

- **Phase:** Narrative/innovation.
- **Central question:** Why can interactions not make the required damping sublinear in the register size?
- **Understanding target:** Explain the growth bound $`\lambda_{\max}(\rho(T))\le e^A\lambda_{\max}(\rho(0))`$, including the top-eigenspace directional derivative at degeneracy. Apply the maximally mixed witness to obtain $`A\ge\max\{0,n\ln2+\ln(1-\epsilon)\}`$ and understand its survival under pulses and branch averaging.
- **Dependencies and story role:** M01, M04, M07–M08, M11–M12. Supplies the necessary bound that turns the interacting construction into an optimal scaling order.
- **Conceptual connection:** Coherent control can rearrange eigenvectors but cannot itself raise the largest eigenvalue; the loss port limits that rate even beyond Gaussian dynamics.
- **Source pointers:** [Watrous §1.1](https://jhwatrous.github.io/TQI.1.pdf) for spectral foundations; [interacting proof §7, Eqs. (I26)–(I28)](../science/interacting_reset.md#7-a-lower-bound-for-arbitrary-coherent-control), including its almost-everywhere and Dini-derivative treatment.

### M26 · A universal upper bound using Gaussian control alone

- **Phase:** Narrative/innovation.
- **Central question:** Can the Gaussian witness lower bound be matched in order for the full reference-sensitive task?
- **Understanding target:** Apply the shared twirl and equal loss to all $`n`$ modes, choose $`q=\epsilon/n`$, and connect the biased product error and parity residue to a uniform error at most $`\epsilon`$. Identify the resulting action $`n\ln(n/\epsilon)`$ as an achievable universal bound.
- **Dependencies and story role:** M11–M12, M19–M20. Supplies the missing constructive side of the Gaussian scaling statement.
- **Conceptual connection:** Every conditioned schedule is Gaussian; the averaged channel belongs to the explicitly randomized class without any claim that its output is always Gaussian.
- **Source pointers:** [Watrous §§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf); [interacting proof §8, Eqs. (I29)–(I30)](../science/interacting_reset.md#8-gaussian-universal-upper-bound).

### M27 · The universal action hierarchy

- **Phase:** Narrative/innovation.
- **Central question:** Which lower and upper bounds together establish the separation?
- **Understanding target:** Assemble $`A_{\rm G}=\Theta_\epsilon(n\ln n)`$ and $`A_{\rm I}=\Theta_\epsilon(n)`$ for fixed $`0\lt \epsilon\lt 1`$. Distinguish an exact selected-input frontier, a witness converse, a universal construction, and an optimal asymptotic order.
- **Dependencies and story role:** M12, M18, M24–M26. Integrates the two proof arcs into the main result under one resource contract.
- **Conceptual connection:** The logarithmic advantage follows from comparing optimized control classes with the same bath and error requirement; it is not inferred solely from a slow sequential baseline.
- **Source pointers:** [Watrous §§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf) for the common task; [model §5](../science/model.md#5-exact-state-frontier-and-universal-hierarchy); [interpretation](../science/interpretation.md).

### M28 · An explicit certificate for a chosen finite register

- **Phase:** Narrative/innovation.
- **Central question:** How can the asymptotic construction become a deterministic schedule with a finite error certificate?
- **Understanding target:** Interpret the size-dependent budget $`\delta_m=\epsilon/[4m(m+1)]`$, integer weight threshold, conservative two-mode trash guard, and stopping conditions. Connect the telescoping error budget and final cleanup to the exact sum of charged stage actions; the rule depends on sizes, not observed inputs.
- **Dependencies and story role:** M21–M24, M27. Refines the transparent linear-action proof into a directly evaluable upper bound.
- **Conceptual connection:** Integer rounding, parity capacity, residue control, and cleanup all matter before an asymptotic statement can certify a finite protocol.
- **Source pointers:** [Watrous §1.2.2](https://jhwatrous.github.io/TQI.1.pdf) and [§5.3.1](https://jhwatrous.github.io/TQI.5.pdf) for concentration and counting foundations; [finite-size construction §§1–2](../science/finite_size.md#1-choose-the-next-active-block); [verification guide](../verification/README.md).

### M29 · Attainable coefficients and the limits of finite evidence

- **Phase:** Narrative/innovation.
- **Central question:** What do the quantitative coefficient and the numerical comparison establish beyond scaling order?
- **Understanding target:** Interpret the attainable coefficient $`\ln(1/q)/[1-h_2(q/2)]`$, about $`3.03`$ for $`q=1/5`$, against the converse coefficient $`\ln2`$. Distinguish this asymptotic upper coefficient from an optimal constant, a finite-register action, and the floating-point checks of analytical certificates.
- **Dependencies and story role:** M09, M25, M27–M28. Integrates asymptotic refinement with finite, reproducible statements and their remaining gap.
- **Conceptual connection:** A constructive upper curve below the Gaussian witness lower curve certifies a finite advantage; matrix examples and schedule evaluations do not prove arbitrary-control optimality.
- **Source pointers:** [Watrous §5.1.1](https://jhwatrous.github.io/TQI.5.pdf) for the entropy convention; [finite-size construction §§3–4](../science/finite_size.md#3-a-smaller-asymptotic-coefficient); [verification guide: distinguish the bounds](../verification/README.md#keep-the-bounds-distinct).

### M30 · Mechanism, contribution, and physical scope

- **Phase:** Narrative/innovation.
- **Central question:** What is the complete scientific explanation for the action saved by interactions?
- **Understanding target:** Join the Gaussian defect-product obstruction to global accuracy, and the interacting advantage to uncertainty concentration into geometrically shrinking blocks. Place the optimized Gaussian law and matched universal comparison alongside established covariance methods, single-port cooling, and algorithmic cooling, with the arbitrary-reference and parity requirements intact.
- **Dependencies and story role:** M12, M15–M18, M19–M29. Completes the narrative by integrating mechanism, evidence, attribution, and limitations.
- **Conceptual connection:** The result concerns total dissipative exposure under fast control. It does not establish an optimal interacting coefficient, optimal joint dependence on $`n`$ and $`\epsilon`$, efficient nonlinear synthesis, or a total hardware-runtime advantage.
- **Source pointers:** [Watrous §§3.3.2–3.3.3](https://jhwatrous.github.io/TQI.3.pdf) and [§§5.2.1 and 5.3.1](https://jhwatrous.github.io/TQI.5.pdf) for the operational and information-concentration foundations; [interpretation](../science/interpretation.md); [model](../science/model.md); [related work §§2–5](../references/RELATED_WORK.md#2-established-ingredients-and-the-specific-addition); [verification guide](../verification/README.md).
