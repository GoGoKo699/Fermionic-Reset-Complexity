# Scientific reading route

The result compares the integrated damping needed to reset an entire fermionic register under Gaussian and interacting coherent control. Every input mode is retained, arbitrary reference correlations are included, and both classes use the same loss port and classical randomization.

Start with [the interpretation](interpretation.md) for the mechanism and [the model](model.md) for the operational contract.

| Question | Authoritative account |
|---|---|
| Which controls, inputs, outputs and resources are allowed? | [The reset task and its control resources](model.md) |
| Why does global accuracy create a Gaussian logarithmic overhead? | [Physical interpretation](interpretation.md) |
| What is the exact Gaussian frontier for a maximally mixed input? | [Gaussian cooling bound](gaussian_bound.md), including normalization, finite-action positivity, spectral degeneracies and attainment |
| How can interactions reset an unknown register with linear action? | [Universal interacting reset](interacting_reset.md), including parity, references, deterministic cost and the general-control lower bound |
| What action is certified for a finite register? | [Finite-size protocol](finite_size.md), including threshold rounding, error allocation and an achievable asymptotic coefficient |
| What was checked computationally, and how is it reproduced? | [Verification guide](../verification/README.md) |
| Which mechanisms and mathematical ingredients are inherited? | [Related work](../references/RELATED_WORK.md) and [bibliography](../references/references.bib) |

For the full proof, read model → Gaussian bound → interacting reset → finite-size protocol. The exact Gaussian formula is a selected-input state-preparation result. The universal reset comparison establishes $`\Theta_\epsilon(n\ln n)`$ versus $`\Theta_\epsilon(n)`$ at fixed global error. Finite-size curves are bounds and constructions, not a numerical solution of the unrestricted control optimum.
