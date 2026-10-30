#!/usr/bin/env python3
"""Reproducible sanity checks for the Gaussian cooling action inequality.

These checks validate finite examples and conventions, not the general theorem.
The analytical proof is in science/gaussian_bound.md.

Run from the repository root: python verification/check_gaussian_action.py
Dependencies: numpy, scipy.  All random numbers use the stated fixed seed.
The JSON summary is printed and saved to verification/results/gaussian_action.json.
"""

import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm


SEED = 20261030
RNG = np.random.default_rng(SEED)
DT = 0.03
STEPS = 100
TOLERANCE = 1e-9


def evolve_covariance(gamma, drift, source, duration):
    """Exact affine step via the Van Loan block exponential."""
    dimension = gamma.shape[0]
    block = np.zeros((2 * dimension, 2 * dimension))
    block[:dimension, :dimension] = drift
    block[:dimension, dimension:] = source
    block[dimension:, dimension:] = -drift.T
    propagator = expm(duration * block)
    fundamental = propagator[:dimension, :dimension]
    noise = propagator[:dimension, dimension:] @ fundamental.T
    output = fundamental @ gamma @ fundamental.T + noise
    assert np.linalg.norm(output + output.T) < TOLERANCE
    return (output - output.T) / 2


def random_generator(n_modes, kind):
    dimension = 2 * n_modes
    raw_hamiltonian = RNG.standard_normal((dimension, dimension))
    hamiltonian = 4 * (raw_hamiltonian - raw_hamiltonian.T)
    if kind == "full_rank_linear_jumps":
        raw_jumps = RNG.standard_normal((dimension, dimension))
        raw_jumps = raw_jumps + 1j * RNG.standard_normal((dimension, dimension))
        jump_matrix = raw_jumps @ raw_jumps.conj().T
        jump_matrix = jump_matrix / (2 * np.trace(jump_matrix).real)
    elif kind == "single_rotated_loss":
        rotation, _ = np.linalg.qr(RNG.standard_normal((dimension, dimension)))
        rotation[:, -1] *= np.linalg.det(rotation)
        # L = (w'_1 + i w'_2)/2: unit ordinary amplitude-damping rate.
        jump = (rotation[:, 0] + 1j * rotation[:, 1]) / 2
        jump_matrix = np.outer(jump, jump.conj())
    else:
        raise ValueError(kind)
    drift = hamiltonian - 2 * jump_matrix.real
    source = 4 * jump_matrix.imag
    rate = 2 * np.trace(jump_matrix).real
    cp_matrix = -drift - drift.T + 1j * source
    assert np.linalg.eigvalsh(cp_matrix).min() >= -TOLERANCE
    assert abs(rate + np.trace(drift)) < TOLERANCE
    assert abs(rate - 1) < TOLERANCE
    return drift, source, rate


def spectral_statistics(gamma, action):
    n_modes = gamma.shape[0] // 2
    eigenvalues = np.linalg.eigvalsh(np.eye(2 * n_modes) + 1j * gamma)
    assert eigenvalues.min() > 0
    assert eigenvalues.max() <= 2 + TOLERANCE
    defects = eigenvalues[:n_modes]
    assert np.max(abs(eigenvalues + eigenvalues[::-1] - 2)) < TOLERANCE
    defect_margin = np.log(defects).sum() + action
    fidelity = np.prod(1 - defects / 2)
    exact_bound = (1 - np.exp(-action / n_modes) / 2) ** n_modes
    assert defect_margin >= -TOLERANCE
    assert fidelity <= exact_bound + TOLERANCE
    return float(defect_margin), float(fidelity), float(exact_bound)


def random_path(n_modes, kind):
    gamma = np.zeros((2 * n_modes, 2 * n_modes))
    action = 0.0
    minimum_defect_margin = float("inf")
    minimum_fidelity_slack = float("inf")
    for _ in range(STEPS):
        drift, source, rate = random_generator(n_modes, kind)
        gamma = evolve_covariance(gamma, drift, source, DT)
        action += rate * DT
        margin, fidelity, bound = spectral_statistics(gamma, action)
        minimum_defect_margin = min(minimum_defect_margin, margin)
        minimum_fidelity_slack = min(minimum_fidelity_slack, bound - fidelity)
    return {
        "case": kind,
        "n_modes": n_modes,
        "segments": STEPS,
        "action": action,
        "final_fidelity": fidelity,
        "exact_fidelity_bound": bound,
        "minimum_log_defect_margin": minimum_defect_margin,
        "minimum_fidelity_slack": minimum_fidelity_slack,
        "passed": True,
    }


def uniform_loss_saturation(n_modes):
    dimension = 2 * n_modes
    gamma = np.zeros((dimension, dimension))
    jump_matrix = np.zeros((dimension, dimension), dtype=complex)
    for mode in range(n_modes):
        jump = np.zeros(dimension, dtype=complex)
        jump[2 * mode] = 1 / (2 * np.sqrt(n_modes))
        jump[2 * mode + 1] = 1j / (2 * np.sqrt(n_modes))
        jump_matrix += np.outer(jump, jump.conj())
    drift = -2 * jump_matrix.real
    source = 4 * jump_matrix.imag
    action = STEPS * DT
    gamma = evolve_covariance(gamma, drift, source, action)
    margin, fidelity, bound = spectral_statistics(gamma, action)
    assert abs(margin) < TOLERANCE
    assert abs(fidelity - bound) < TOLERANCE
    return {
        "case": "uniform_loss_saturation",
        "n_modes": n_modes,
        "action": action,
        "final_fidelity": fidelity,
        "exact_fidelity_bound": bound,
        "log_defect_margin": margin,
        "passed": True,
    }


def main():
    report = {
        "purpose": "Finite-example convention and inequality checks; not a proof.",
        "utc": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "dt": DT,
        "steps": STEPS,
        "tolerance": TOLERANCE,
        "results": [],
    }
    for n_modes in (1, 2, 3, 5):
        for kind in ("full_rank_linear_jumps", "single_rotated_loss"):
            report["results"].append(random_path(n_modes, kind))
        report["results"].append(uniform_loss_saturation(n_modes))
    report["all_passed"] = True
    payload = json.dumps(report, indent=2)
    output = Path(__file__).resolve().parent / "results" / "gaussian_action.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(payload + "\n")
    print(payload)


if __name__ == "__main__":
    main()
