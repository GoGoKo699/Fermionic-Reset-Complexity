#!/usr/bin/env python3
"""Check covariance conventions against finite-dimensional GKSL evolution.

This is numerical validation of the convention and finite examples, not proof
of the control theorem in science/gaussian_bound.md.

Run from the repository root:
    python verification/gaussian_hilbert_conventions.py

Dependencies: NumPy and SciPy. The JSON summary is printed and saved to
verification/results/gaussian_hilbert_conventions.json. The numerical checks
use the fixed seed below; the summary also records dependency versions.
"""

import json
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm


SEED = 20261030
TOL = 1e-10
RNG = np.random.default_rng(SEED)


def kron_all(factors):
    result = np.ones((1, 1), dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def majoranas(n_modes):
    identity = np.eye(2)
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    pauli_z = np.diag([1, -1])
    operators = []
    for mode in range(n_modes):
        for local in (pauli_x, pauli_y):
            operators.append(
                kron_all(
                    [pauli_z] * mode
                    + [local]
                    + [identity] * (n_modes - mode - 1)
                )
            )
    return operators


def covariance(rho, operators):
    dimension = len(operators)
    gamma = np.zeros((dimension, dimension), dtype=complex)
    for j, left in enumerate(operators):
        for k, right in enumerate(operators):
            gamma[j, k] = 0.5j * np.trace(rho @ (left @ right - right @ left))
    assert np.max(abs(gamma.imag)) < TOL
    assert np.max(abs(gamma + gamma.T)) < TOL
    return gamma.real


def hilbert_generator(operators, hamiltonian_matrix, jump_coefficients):
    size = operators[0].shape[0]
    identity = np.eye(size)
    hamiltonian = np.zeros((size, size), dtype=complex)
    for j, left in enumerate(operators):
        for k, right in enumerate(operators):
            hamiltonian += 0.25j * hamiltonian_matrix[j, k] * (left @ right)
    assert np.max(abs(hamiltonian - hamiltonian.conj().T)) < TOL
    generator = -1j * (
        np.kron(identity, hamiltonian) - np.kron(hamiltonian.T, identity)
    )
    for coefficients in jump_coefficients:
        jump = sum(coefficient * operator for coefficient, operator in zip(coefficients, operators))
        square = jump.conj().T @ jump
        generator += (
            np.kron(jump.conj(), jump)
            - 0.5 * np.kron(identity, square)
            - 0.5 * np.kron(square.T, identity)
        )
    return generator


def covariance_step(gamma, hamiltonian_matrix, jump_coefficients, duration):
    dimension = gamma.shape[0]
    matrix_m = sum(
        np.outer(coefficients, coefficients.conj())
        for coefficients in jump_coefficients
    )
    drift = hamiltonian_matrix - 2 * matrix_m.real
    source = 4 * matrix_m.imag
    block = np.zeros((2 * dimension, 2 * dimension))
    block[:dimension, :dimension] = drift
    block[:dimension, dimension:] = source
    block[dimension:, dimension:] = -drift.T
    propagator = expm(duration * block)
    fundamental = propagator[:dimension, :dimension]
    affine = propagator[:dimension, dimension:] @ fundamental.T
    result = fundamental @ gamma @ fundamental.T + affine
    rate = 2 * np.trace(matrix_m).real
    assert abs(rate + np.trace(drift)) < TOL
    return (result - result.T) / 2, rate


def check_example(n_modes, kind):
    operators = majoranas(n_modes)
    dimension = 2 * n_modes
    size = 2**n_modes
    initial = np.eye(size) / size
    raw = RNG.standard_normal((dimension, dimension))
    hamiltonian_matrix = raw - raw.T
    duration = 0.73
    if kind == "general_linear_jumps":
        coefficients = (
            RNG.standard_normal((dimension, dimension))
            + 1j * RNG.standard_normal((dimension, dimension))
        )
        coefficients /= np.sqrt(2 * np.sum(abs(coefficients) ** 2))
        jump_coefficients = list(coefficients)
    elif kind == "uniform_loss":
        hamiltonian_matrix[:] = 0
        jump_coefficients = []
        for mode in range(n_modes):
            coefficients = np.zeros(dimension, dtype=complex)
            coefficients[2 * mode] = 1 / (2 * np.sqrt(n_modes))
            coefficients[2 * mode + 1] = 1j / (2 * np.sqrt(n_modes))
            jump_coefficients.append(coefficients)
    elif kind == "gain_and_hermitian_jump":
        coefficients = np.zeros(dimension, dtype=complex)
        coefficients[0] = 0.5
        coefficients[1] = -0.5j
        hermitian = np.zeros(dimension, dtype=complex)
        hermitian[-1] = 0.3
        jump_coefficients = [coefficients, hermitian]
    else:
        raise ValueError(kind)

    generator = hilbert_generator(operators, hamiltonian_matrix, jump_coefficients)
    evolved_vector = expm(duration * generator) @ initial.reshape(-1, order="F")
    rho = evolved_vector.reshape((size, size), order="F")
    assert np.max(abs(rho - rho.conj().T)) < TOL
    assert abs(np.trace(rho) - 1) < TOL
    assert np.linalg.eigvalsh(rho).min() >= -TOL

    gamma_hilbert = covariance(rho, operators)
    gamma_affine, rate = covariance_step(
        np.zeros((dimension, dimension)),
        hamiltonian_matrix,
        jump_coefficients,
        duration,
    )
    covariance_error = np.max(abs(gamma_hilbert - gamma_affine))
    assert covariance_error < TOL

    defects = np.linalg.eigvalsh(np.eye(dimension) + 1j * gamma_affine)[:n_modes]
    predicted_largest = float(np.prod(1 - defects / 2))
    actual_largest = float(np.linalg.eigvalsh(rho)[-1])
    spectral_error = abs(predicted_largest - actual_largest)
    assert spectral_error < TOL

    action = rate * duration
    fidelity_bound = (1 - 0.5 * np.exp(-action / n_modes)) ** n_modes
    log_defect_margin = float(np.log(defects).sum() + action)
    assert log_defect_margin >= -TOL
    assert actual_largest <= fidelity_bound + TOL
    if kind == "uniform_loss":
        assert abs(actual_largest - fidelity_bound) < TOL
        assert abs(rho[0, 0].real - fidelity_bound) < TOL
        assert abs(log_defect_margin) < TOL
    return {
        "n_modes": n_modes,
        "case": kind,
        "action": float(action),
        "covariance_error": float(covariance_error),
        "gaussian_spectrum_error": float(spectral_error),
        "largest_eigenvalue": actual_largest,
        "fidelity_bound": float(fidelity_bound),
        "log_defect_margin": log_defect_margin,
        "passed": True,
    }


def main():
    results = [
        check_example(n_modes, kind)
        for n_modes in (1, 2, 3)
        for kind in (
            "general_linear_jumps",
            "uniform_loss",
            "gain_and_hermitian_jump",
        )
    ]
    payload = json.dumps(
        {
            "seed": SEED,
            "tolerance": TOL,
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "results": results,
            "all_passed": True,
        },
        indent=2,
    )
    output = Path(__file__).resolve().parent / "results" / "gaussian_hilbert_conventions.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(payload + "\n")
    print(payload)


if __name__ == "__main__":
    main()
