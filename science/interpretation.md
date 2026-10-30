# Why interactions reduce the damping needed for reset

Quadratic control cannot remove the logarithmic overhead of resetting a large fermionic register to fixed global accuracy. Interacting control can remove it by concentrating the remaining uncertainty into progressively fewer modes. The comparison uses the same vacuum-loss port, the same classical randomization, and the same requirement to reset every retained mode.

At fixed $`0<\epsilon<1`$, the optimal dissipative actions are

```math
A_{\rm G}(n,\epsilon)=\Theta_\epsilon(n\ln n),
\qquad
A_{\rm I}(n,\epsilon)=\Theta_\epsilon(n).
```

The [model](model.md) specifies the resource being optimized: integrated Markovian damping under arbitrarily fast coherent control. The Gaussian class includes pairing terms, nonlocal quadratic Hamiltonians, Gaussian pulses, and mixtures selected by an input-independent classical seed.

## Global reset requires more than small local occupation

A mode with excited population $`p\ll1`$ looks nearly empty locally. A product of $`n`$ such modes has vacuum probability $`(1-p)^n`$, however. A fixed nonzero $`p`$ therefore gives a vanishing chance that the entire register is empty as $`n`$ grows. Under independent loss, reducing each residual occupation to order $`1/n`$ takes a logarithmic exposure per mode.

The operational task also includes quantum correlations. For every input $`\rho_{SR}`$, including entanglement with an inaccessible reference, the output must approach

```math
|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R.
```

Half-diamond distance measures the worst joint-state error of this channel replacement. A good expectation value for one observable does not establish it. The [interacting construction](interacting_reset.md) controls the joint error throughout compression and cleanup, so all modes are ready for reuse and the reference marginal is preserved. The channel-norm convention follows [Watrous, Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/).

## The Gaussian obstruction is a constraint on spectral defects

A fermionic Gaussian state's covariance eigenvalues occur in conjugate pairs. Write their magnitudes as $`\nu_j\in[0,1]`$, and define defects $`\delta_j=1-\nu_j`$. In a suitable Gaussian mode basis, the density-matrix spectrum factorizes into binary populations, with smaller population $`\delta_j/2`$. This normal form is standard; see [Barthel and Zhang](https://arxiv.org/abs/2112.08344v5).

Quadratic unitary control rotates the covariance basis without changing these magnitudes. Dissipation changes them, but complete positivity and spectral pairing impose the integrated bound

```math
\prod_{j=1}^n\delta_j\ge e^{-A}
```

when the initial state is maximally mixed. The [Gaussian proof](gaussian_bound.md) establishes this inequality for arbitrary integrable quadratic Hamiltonians and linear jumps, including eigenvalue crossings and pulses. It applies more broadly than the single loss port needed for attainment.

The largest eigenvalue of the state is $`\prod_j(1-\delta_j/2)`$, which bounds every pure-state overlap. Global accuracy requires the sum of the defects to stay bounded as the number of modes increases. Optimizing their distribution under the product constraint makes equal defects best. The exact resulting frontier is

```math
F_{\rm G}(n,A)=\left(1-\frac12e^{-A/n}\right)^n.
```

Equal loss exposure attains it. Arbitrarily strong quadratic rotations, pairing, and changes of bath orientation cannot improve this frontier at the same action. The logarithmic overhead therefore persists after optimization over the Gaussian controls; it is not inferred merely from the performance of sequential damping.

## Interactions concentrate uncertainty into a smaller block

A reversible unitary does not reduce the entropy of the full register. It can nevertheless change where that entropy is stored. After a constant loss exposure, an active block resembles independent biased occupation bits. Most of its probability lies on a set of strings substantially smaller than the full occupation basis.

A parity-preserving permutation places those likely strings into states with a zero prefix and a shorter active suffix. The construction makes room separately for even and odd strings, so it respects fermion parity without a parity reference or a clean ancillary mode. The excluded probability is charged to the global error.

The zero-prefix modes remain in the output. The controller applies another cooling-and-compression stage only to the active suffix. Its size decreases geometrically, making the total number of mode exposures linear in $`n`$. A final loss step resets the remaining small block. The proof adds the stage errors using channel contractivity and an exact probability-to-trace-distance identity.

This is entropy compression in the tradition of [Schulman and Vazirani](https://arxiv.org/abs/quant-ph/9804060v1) and [Boykin et al.](https://arxiv.org/abs/quant-ph/0106093). Its role here is to attain the interacting side of a matched action comparison. Single-port cooling itself is also established; [Bergholm and collaborators](https://arxiv.org/abs/1605.06473v2) provide the closest controlled-damping antecedent. The [related-work account](../references/RELATED_WORK.md) separates these ingredients from the Gaussian optimality result.

## What the randomization does

Both classes receive the same input-independent random Gaussian controls. Their average is unital: it fixes the maximally mixed state and cannot supply purification. The universal construction uses an even Majorana twirl to standardize an unknown active block within each parity sector.

The twirl leaves one parity-dependent component, which may remain correlated with the reference. Equal loss with survival $`q`$ on $`m`$ modes suppresses that component by $`q^m`$, permitting comparison with independent biased occupations. The subsequent compression therefore works for an unknown input, rather than only for a preselected thermal state.

The guarantee concerns the averaged channel after the controller's classical record is ignored. Every realization has the same predetermined sizes and loss exposures. On the converse side, the Gaussian bound holds separately for each realization and survives averaging; the averaged state need not itself be Gaussian.

## Reading the bounds and their cost

The exact formula $`F_{\rm G}`$ concerns preparation from the specified maximally mixed input. It supplies a lower bound for universal reset. The universal theorem establishes matching asymptotic orders, not an exact finite-action Gaussian channel optimum.

The [finite-size protocol](finite_size.md) gives explicit upper bounds with integer thresholds and a final cleanup cost. Its choice $`q=1/5`$ has an attainable asymptotic coefficient of about $`3.03`$ multiplying $`n`$. The general lower coefficient is $`\ln2`$; this gap remains. The coefficient $`3.03`$ is neither an optimal interacting value nor a replacement for the finite-register certificate. The [verification guide](../verification/README.md) explains the numerical evaluations and their relation to the proofs.

Action counts the integral of the **sum** of damping rates. Exposing $`n`$ modes simultaneously at rate $`\kappa`$ each costs $`n\kappa t`$, rather than $`\kappa t`$. At a fixed total-rate cap, action sets a lower bound on dissipative exposure time. Coherent routing and nonlinear synthesis remain unpriced in the fast-control model. The hierarchy identifies what interactions can save in dissipative exposure; a hardware-duration comparison must also account for implementing those controls.
