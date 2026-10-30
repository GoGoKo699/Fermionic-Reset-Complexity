# Reproduce the finite checks and action comparison

This directory checks conventions, finite matrix identities, and the explicit action certificates used in the accompanying proofs. The universal statements are analytical: see the [Gaussian bound](../science/gaussian_bound.md), [interacting reset proof](../science/interacting_reset.md), and [finite-size construction](../science/finite_size.md). Numerical examples do not establish the bounds for arbitrary controls, inputs, references, or register sizes.

## Environment and commands

The recorded environment uses Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. The package versions are pinned in [requirements.txt](requirements.txt). From the repository root, install them into the Python environment you intend to use:

    python -m pip install -r verification/requirements.txt

Run the five scripts with ordinary Python so that their assertions remain enabled:

    python verification/gaussian_hilbert_conventions.py
    python verification/check_gaussian_action.py
    python verification/check_reference_twirl.py
    python verification/finite_protocol.py
    python verification/plot_action_scaling.py

Each script creates its output directory as needed. JSON results are written under verification/results/; the action figure is written under verification/figures/. The three matrix checks use seed 20261030. Their floating-point residuals can vary slightly across numerical-library builds. The Gaussian-action report also records a UTC execution time, so its JSON is not intended to be byte-identical between runs.

## What each script checks

| Script | Numerical scope | Saved output |
| --- | --- | --- |
| [gaussian_hilbert_conventions.py](gaussian_hilbert_conventions.py) | Nine one-, two-, and three-mode examples compare full Jordan–Wigner GKSL evolution with the affine covariance equation. They include general linear jumps, uniform losses, and gain plus a Hermitian Majorana jump. The checks also compare the actual density-matrix largest eigenvalue with the Gaussian spectral formula and verify uniform-loss saturation. Tolerance: 1e-10. | [gaussian_hilbert_conventions.json](results/gaussian_hilbert_conventions.json) |
| [check_gaussian_action.py](check_gaussian_action.py) | For n = 1, 2, 3, 5, integrate 100 piecewise-constant segments for both general linear jumps and a rotated single-loss port, with arbitrary quadratic drift. Check the log-defect inequality and largest-eigenvalue bound at every segment, then verify four uniform-loss saturation cases. Tolerance: 1e-9. | [gaussian_action.json](results/gaussian_action.json) |
| [check_reference_twirl.py](check_reference_twirl.py) | For one through four modes and a reference qubit, check the even-Majorana twirl and the subsequent loss identity on fixed-seed joint density matrices. Also check parity-embedding capacities and contraction for integer active sizes 24 through 999, plus the explicit cutoff inequalities at five target errors. Matrix-identity tolerance: 2e-12. | [reference_twirl.json](results/reference_twirl.json) |
| [finite_protocol.py](finite_protocol.py) | Evaluate the deterministic, size-dependent compression schedule and its analytic error/action bounds. The default run covers seven register sizes from 64 to one million modes, plus 12 small-register or high-accuracy cases. It checks threshold rounding, stage error budgets, cleanup, and the total error certificate. These large-register evaluations manipulate formulas and integer schedules; they do not simulate the full many-body state. | [finite_protocol.json](results/finite_protocol.json) |
| [plot_action_scaling.py](plot_action_scaling.py) | Evaluate the same finite protocol over the plotted register-size grid at global half-diamond error epsilon = 0.1, check the displayed lower/upper-bound order, and plot action per mode. It imports the protocol calculation directly instead of copying its formulas. | [scaling_series.json](results/scaling_series.json) and [action_scaling.svg](figures/action_scaling.svg) |

The matrix-exponential steps evaluate the stated finite-dimensional generators in floating-point arithmetic. The certificate and plotting scripts also use floating-point functions; they are not interval-arithmetic proofs or searches over all admissible controllers.

## Keep the bounds distinct

The exact Gaussian state-preparation frontier is

$$
F_{\mathrm G}(n,A)=\left(1-\frac12e^{-A/n}\right)^n.
$$

It starts from the maximally mixed input. Its inverse, $A_{\mathrm G}^{\tau}(n,\epsilon)$, is the exact action needed for that selected-input task and a lower bound for universal Gaussian reset. The scripts' gaussian_witness_lower field refers to this witness. It is not an exact finite-action universal-reset optimum.

The universal Gaussian construction supplies the achievable upper bound $n\ln(n/\epsilon)$. The Gaussian shaded region in the figure lies between this construction and the maximally mixed-input witness. Reference correlations are included in the proof of the construction.

The interacting_certified_upper field is the smaller action of two explicitly available universal protocols: the size-dependent compression protocol and the Gaussian universal construction. The selected protocol's name and error bound are reported with it. This is an attainable interacting upper bound, not an optimized interacting action. The general spectral lower bound,

$$
\max\{0,n\ln2+\ln(1-\epsilon)\},
$$

applies to arbitrary allowed coherent control. It need not meet the constructive interacting upper bound at finite size.

In the finite-protocol report, compression_error_bound sums the allocated analytical stage budgets and the final cleanup budget $\epsilon/2$. The selected_protocol_error_bound refers to the chosen construction: it equals $\epsilon$ for the Gaussian fallback and the compression budget otherwise. The separate tail and residue evaluation fields are floating-point diagnostics; log_parity_residue retains the logarithm when a displayed residue underflows. An evaluated zero is not a certificate of exactly zero error.

The fixed-error orders $A_{\mathrm G}=\Theta_\epsilon(n\ln n)$ and $A_{\mathrm I}=\Theta_\epsilon(n)$ follow from the analytical converses and constructions. The finite reports illustrate and check their implementation. They do not establish an optimal interacting coefficient, a sharp joint dependence on $n$ and $\epsilon$, or a bound on coherent gate synthesis, locality, or hardware duration.
