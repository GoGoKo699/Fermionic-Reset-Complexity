# Reproduce the finite checks and action comparison

This directory checks conventions, finite matrix identities, and the explicit action certificates used in the accompanying proofs. The universal statements are analytical: see the [universal frontier](../science/universal-frontier.md), [interacting frontier](../science/interacting-frontier.md), and [finite-size compression certificate](../science/finite_size.md). Numerical examples do not establish the bounds for arbitrary controls, inputs, references, or register sizes.

## Environment and commands

The recorded environment uses Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. The package versions are pinned in [requirements.txt](requirements.txt). From the repository root, install them into the Python environment you intend to use:

    python -m pip install -r verification/requirements.txt

Run these scripts with ordinary Python so that their assertions remain enabled:

    python verification/gaussian_hilbert_conventions.py
    python verification/check_gaussian_action.py
    python verification/check_reference_twirl.py
    python verification/check_reset_frontier.py
    python verification/finite_protocol.py
    python verification/plot_action_scaling.py

Each script creates its output directory as needed. JSON results are written under verification/results/; the action figure is written under verification/figures/. The randomized diagnostics fix their seeds. Their floating-point residuals can vary slightly across numerical-library builds. The Gaussian-action report also records a UTC execution time, so its JSON is not intended to be byte-identical between runs.

## What each script checks

| Script | Numerical scope | Saved output |
| --- | --- | --- |
| [Hilbert-space conventions](gaussian_hilbert_conventions.py) | Nine one-, two-, and three-mode examples compare full Jordan–Wigner GKSL evolution with the affine covariance equation. They include general linear jumps, uniform losses, and gain plus a Hermitian Majorana jump. The checks also compare the actual density-matrix largest eigenvalue with the Gaussian spectral formula and verify uniform-loss saturation. Tolerance: 1e-10. | [Conventions JSON](results/gaussian_hilbert_conventions.json) |
| [Gaussian action](check_gaussian_action.py) | For n = 1, 2, 3, 5, integrate 100 piecewise-constant segments for both general linear jumps and a rotated single-loss port, with arbitrary quadratic drift. Check the log-defect inequality and largest-eigenvalue bound at every segment, then verify four uniform-loss saturation cases. Tolerance: 1e-9. | [Action JSON](results/gaussian_action.json) |
| [Reference twirl and parity](check_reference_twirl.py) | For one through four modes and a reference qubit, check the even-Majorana twirl and the subsequent loss identity on fixed-seed joint density matrices. Also check parity-embedding capacities and contraction for integer active sizes 24 through 999, plus the explicit cutoff inequalities at five target errors. Matrix-identity tolerance: 2e-12. | [Twirl JSON](results/reference_twirl.json) |
| [Reset frontiers](check_reset_frontier.py) | Dense parity evolution and reference trace norms, matching balance, finite sweep tails, and rational three-mode separation. | [Frontier JSON](results/reset_frontier.json) |
| [Finite schedules](finite_protocol.py) | Evaluate the deterministic, size-dependent compression schedule and its analytic error/action bounds. The default run covers seven register sizes from 64 to one million modes, plus 12 small-register or high-accuracy cases. It checks threshold rounding, stage error budgets, cleanup, and the total error certificate. These large-register evaluations manipulate formulas and integer schedules; they do not simulate the full many-body state. | [Protocol JSON](results/finite_protocol.json) |
| [Action-scaling figure](plot_action_scaling.py) | Evaluate the exact Gaussian action, the finite mirrored-tree and compression certificates, and the joint interacting converse at global half-diamond error 0.1. Check lower and upper ordering and plot action per mode. | [Scaling JSON](results/scaling_series.json) and [figure](figures/action_scaling.svg) |

The matrix-exponential steps evaluate the stated finite-dimensional generators in floating-point arithmetic. The certificate and plotting scripts also use floating-point functions; they are not interval-arithmetic proofs or searches over all admissible controllers.

## What the plotted curves represent

The Gaussian line evaluates the inverse, in $`A`$, of the exact channel error:

```math
r_{\rm G}(n,A)=1-(1-e^{-A/n}/2)^n+2^{-n}e^{-A}.
```

The interacting upper line selects the least action among three available guarantees: Gaussian equal exposure, mirrored-tree sweeps with a binomial certificate, and entropy compression. The lower line uses the larger of the spectral inflow and odd-parity no-jump bounds. The region between the interacting curves includes the unknown finite-action optimum.

The compression examples retain the report's field names. There, gaussian_witness_lower refers to the $`I/2^n`$ state witness, gaussian_universal_upper to the simple Gaussian channel construction, and interacting_certified_upper to the smaller action of compression and that construction. The allocated stage budgets and final cleanup determine the compression error certificate. Tiny numerical residues can underflow.

The exact Gaussian error, joint action laws and fixed-size decay exponents follow from the analytical arguments. The finite checks support the rate conventions, rank calculations and explicit examples.
