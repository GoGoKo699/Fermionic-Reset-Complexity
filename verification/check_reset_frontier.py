"""Check the parity identities and finite reset schedules."""
import json
import math
from pathlib import Path
from fractions import Fraction

import numpy as np
from scipy.linalg import expm
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.stats import binom, poisson

from finite_protocol import gaussian_reset_action, gaussian_reset_error, mirrored_tree_certificate


def balanced_matchings(n, arity):
    m = 2 ** (n - 1)
    levels = [0] + [None] * (m - 1)
    def depth(v):
        return levels[v % m]

    def parity(v):
        return (depth(v) + v // m) % 2

    color_edges = [[] for _ in range(arity + 1)]
    parent_color = {}
    for parent in range(m):
        colors = iter(c for c in range(arity + 1) if c != parent_color.get(parent))
        first_child = arity * parent + 1
        for child in range(first_child, min(first_child + arity, m)):
            color = next(colors)
            levels[child] = levels[parent] + 1
            parent_color[child] = color
            for base in (0, m):
                color_edges[color].append((base + child, base + parent))
    for edges in color_edges:
        taken = {v for edge in edges for v in edge}
        unmatched = [v for v in range(m) if v not in taken]
        for i, left in enumerate(unmatched):
            right = left + m
            odd, even = (left, right) if parity(left) else (right, left)
            edges.append((odd, even) if i < len(unmatched) // 2 else (even, odd))
        assert sorted(v for edge in edges for v in edge) == list(range(2 * m))
        assert all(parity(s) != parity(t) for s, t in edges)
        assert sum(parity(s) for s, _ in edges) == m // 2
        assert all(source != 0 for source, _ in edges)
    rank = lambda v: depth(v) + 1 if v else 0
    all_edges = [edge for color in color_edges for edge in color]
    assert all(rank(s) >= rank(t) for s, t in all_edges)
    assert {s for s, t in all_edges if rank(s) > rank(t)} == set(range(1, 2 * m))
    return color_edges, max(levels) + 1


def generator(matchings, d):
    entries = [(row, s, value / len(matchings))
               for edges in matchings for s, t in edges
               for row, value in [(t, 1), (s, -1)]]
    rows, cols, vals = zip(*entries)
    return coo_matrix((vals, (rows, cols)), shape=(d, d)).tocsr()


def cycle_matchings(n):
    m = 2 ** (n - 1)
    matchings = [[], []]
    for left in range(2 * m):
        right = (left + 1) % (2 * m)
        edge = (right, left) if left < m else (left, right)
        matchings[left % 2].append(edge)
    for edges in matchings:
        assert sorted(v for edge in edges for v in edge) == list(range(2 * m))
        assert sum(source % 2 for source, _ in edges) == m // 2
        assert all(source != 0 for source, _ in edges)
    return matchings


def main():
    tree_cases = []
    for n in range(2, 12):
        failure_indicator = np.r_[0., np.ones(2 ** n - 1)]
        for arity in (2, 4):
            edges, max_rank = balanced_matchings(n, arity)
            gen = generator(edges, 2 ** n)
            for action in (n, 3*n, 6*n, 10*n):
                worst = max(expm_multiply(action * gen.T, failure_indicator))
                tail = poisson.cdf(max_rank - 1, action / (arity + 1))
                assert worst <= tail + 5e-13
                tree_cases.append([n, arity, action, float(worst), float(tail)])

    finite_tree_cases = 0
    for n in range(2, 10):
        failure_indicator = np.r_[0., np.ones(2 ** n - 1)]
        for arity in (2, 4):
            edges, max_rank = balanced_matchings(n, arity)
            for rounds in (n, 2*n, 4*n):
                for step_action in (.2, math.log(2)):
                    p_jump = -math.expm1(-step_action)
                    failure = failure_indicator.copy()
                    for _ in range(rounds):
                        for matching in reversed(edges):
                            sources, targets = np.array(matching).T
                            failure[sources] += p_jump * (failure[targets] - failure[sources])
                    assert max(failure) <= binom.cdf(max_rank - 1, rounds, p_jump) + 5e-13
                    finite_tree_cases += 1

    cycle_cases = []
    for n in range(2, 10):
        d = 2 ** n
        g = generator(cycle_matchings(n), d)
        odd = np.arange(d) % 2
        for action in (0., 1., 7., 30 * math.log(2), 50.):
            out = expm_multiply(action * g, odd / (d / 2))
            measured = float(np.sum(out[1:]))
            formula = float(np.mean(poisson.cdf(np.arange(0, d // 2, 2), action / 2)))
            assert abs(measured - formula) < 5e-13
            cycle_cases.append([n, action, measured, formula])

    identity_residual = 0.0
    reference_residual = 0.0
    rng = np.random.default_rng(78262)
    for n in range(1, 5):
        d = 2 ** n
        parities = np.array([(-1) ** i.bit_count() for i in range(d)])
        p = np.diag(parities)
        i = np.eye(d)
        x = np.array([[0, 1], [1, 0]], complex)
        y = np.array([[0, -1j], [1j, 0]], complex)
        z = np.diag([1, -1])
        local_i = np.eye(2)
        majoranas = []
        for j in range(n):
            for local in (x, y):
                w = np.ones((1, 1))
                for k in range(n):
                    w = np.kron(w, z if k < j else local if k == j else local_i)
                majoranas.append(w)
        h = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        h = (h + h.conj().T) * (parities[:, None] == parities) / d
        h -= np.trace(h) * i / d
        coeffs = (rng.normal(size=2*n) + 1j * rng.normal(size=2*n)) / math.sqrt(6*n)
        loss = sum(c*w for c, w in zip(coeffs, majoranas))
        number = loss.conj().T @ loss
        liouville = (np.kron(loss.conj(), loss)
                     - .5 * (np.kron(i, number) + np.kron(number.T, i))
                     - 1j * (np.kron(i, h) - np.kron(h.T, i)))
        duration = .8
        rate = 2 * np.vdot(coeffs, coeffs).real
        propagated = expm(duration * liouville) @ p.flatten(order="F")
        err = np.max(np.abs(propagated - math.exp(-rate*duration)*p.flatten(order="F")))
        identity_residual = max(identity_residual, float(err))
        assert err < 2e-12
        for action in (0., .02, .8, 3.1, 15.):
            q = math.exp(-action/n)
            pop = np.array([(q/2)**v.bit_count()*(1-q/2)**(n-v.bit_count())
                            for v in range(d)])
            conditional = np.array([pop+math.exp(-action)*p_s*parities/d for p_s in (1, -1)])
            a = rng.normal(size=(2*d, 2*d)) + 1j*rng.normal(size=(2*d, 2*d))
            rho = a @ a.conj().T
            rho /= np.trace(rho)
            blocks = rho.reshape(d, 2, d, 2)
            r_plus = sum(blocks[v, :, v, :] for v in range(d) if parities[v] > 0)
            r_minus = sum(blocks[v, :, v, :] for v in range(d) if parities[v] < 0)
            actual = np.kron(np.diag(conditional[0]), r_plus) + np.kron(np.diag(conditional[1]), r_minus)
            target = np.kron(np.diag(np.r_[1., np.zeros(d-1)]), r_plus+r_minus)
            err = np.linalg.norm(actual-target, ord="nuc") / 2
            pred = sum((1-conditional[k,0])*np.trace(r).real for k,r in enumerate((r_plus,r_minus)))
            reference_residual = max(reference_residual, float(abs(err-pred)))
            assert abs(err-pred) < 2e-12
            assert err <= 1-conditional[1,0]+2e-12

    action = 30 * math.log(2)
    x = action / 2
    p = math.exp(-action / 3) / 2
    gaussian = 3*p - 3*p**2 + 2*p**3
    interacting_upper = math.exp(-x) * (1 + x/2 + x*x/4)
    assert interacting_upper < gaussian

    n = 3
    d = 2 ** n
    initial_odd = [Fraction(v % 2, d // 2) for v in range(d)]
    populations = initial_odd.copy()
    for _ in range(16):
        for edges in cycle_matchings(n):
            for source, target in edges:
                transferred = populations[source] / 2
                populations[source] -= transferred
                populations[target] += transferred
    explicit_error = 1 - populations[0]
    explicit_gaussian_lower = 1 - (1 - Fraction(1, 4096)) ** 3
    assert explicit_error == Fraction(39, 65536)
    assert explicit_error < explicit_gaussian_lower
    for modes in (1, 2, 3, 19, 128):
        for epsilon in (0.4, 0.1, 1e-8):
            action_at_error = gaussian_reset_action(modes, epsilon)
            assert math.isclose(gaussian_reset_error(modes, action_at_error), epsilon, rel_tol=1e-12)
            if modes >= 2:
                tree = mirrored_tree_certificate(modes, epsilon)
                contact_jump = -math.expm1(-tree["contact_action"])
                assert binom.cdf(tree["rank_bound"] - 1, tree["sweeps"], contact_jump) <= epsilon

    result = {
        "tree_modes": [2, 11],
        "tree_checks": len(tree_cases),
        "finite_tree_checks": finite_tree_cases,
        "cycle_modes": [2, 9],
        "cycle_checks": len(cycle_cases),
        "majorana_parity_modes": [1, 4],
        "max_parity_residual": identity_residual,
        "reference_trace_norm_checks": 20,
        "max_reference_error_residual": reference_residual,
        "finite_three_mode_gap": {
            "action": "32 ln 2",
            "interacting_achievable_error": str(explicit_error),
            "strict_lower_bound_on_gaussian_error": str(explicit_gaussian_lower)
        },
        "strict_three_mode_gap": {
            "action": action,
            "exact_gaussian_error": gaussian,
            "interacting_achievable_error": interacting_upper
        }
    }
    target = Path(__file__).resolve().parent / "results" / "reset_frontier.json"
    target.parent.mkdir(exist_ok=True)
    report = json.dumps(result, indent=2) + "\n"
    target.write_text(report)
    print(report, end="")


if __name__ == "__main__":
    main()
