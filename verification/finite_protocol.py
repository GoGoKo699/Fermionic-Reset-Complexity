"""Evaluate the explicit size-dependent entropy-compression reset protocol.

The analytical certificate is in science/finite_size.md. These deterministic
finite evaluations check that the chosen integer thresholds satisfy its bounds;
they are not an optimizer over all interacting controls or interval arithmetic.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def binary_entropy(p: float) -> float:
    if p == 0 or p == 1:
        return 0.0
    return -(p * math.log(p) + (1-p) * math.log1p(-p)) / math.log(2)


def gaussian_witness_action(n: int, epsilon: float) -> float:
    """Exact maximally mixed-input lower bound, with stable cancellation."""
    defect = -math.expm1(math.log1p(-epsilon) / n)
    return max(0.0, -n * math.log(2 * defect))


def plan(n: int, epsilon: float = 0.1, q: float = 0.2) -> dict:
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    if not 0 < epsilon < 1 or not 0 < q < 1:
        raise ValueError('epsilon and q must lie in (0,1)')
    p = q / 2
    m = n
    stages = []
    while True:
        delta = epsilon / (4 * m * (m+1))
        k = math.ceil(p*m + math.sqrt(m * math.log(1/delta) / 2))
        r = k / m
        if r >= 0.5:
            break
        # Two spare modes rather than one give extra capacity slack in finite
        # evaluation; the extra constant has no asymptotic effect.
        trash = math.ceil(m * binary_entropy(r)) + 2
        log_parity_residue = m * math.log(q) - math.log(2)
        parity_residue = math.exp(log_parity_residue)
        if trash >= m or log_parity_residue > math.log(delta):
            break
        tail = math.exp(-2*m*(r-p)**2)
        if tail > delta * (1+1e-12):
            raise ArithmeticError('Chosen threshold failed its tail budget')
        error = tail + parity_residue
        if error > 2*delta*(1+1e-12):
            raise ArithmeticError('Stage error exceeds its allocated budget')
        stages.append({'active_modes': m, 'good_weight_max': k,
                       'trash_modes': trash, 'threshold_fraction': r,
                       'loss_survival': q, 'action': m*math.log(1/q),
                       'allocated_error': 2*delta,
                       'hoeffding_tail_evaluation': tail,
                       'parity_residue_evaluation': parity_residue,
                       'log_parity_residue': log_parity_residue})
        m = trash
    final_q = epsilon / (2*m)
    final_action = m * math.log(1/final_q)
    allocated = sum(s['allocated_error'] for s in stages)
    computed_error = sum(s['hoeffding_tail_evaluation'] + s['parity_residue_evaluation']
                         for s in stages) + epsilon/2
    # The reported certificate uses allocated analytical budgets. Tiny parity
    # residues can underflow in evaluation; they are never certified as zero.
    error_bound = allocated + epsilon/2
    action = sum(s['action'] for s in stages) + final_action
    if allocated > epsilon/2 * (1+1e-12) or error_bound > epsilon*(1+1e-12):
        raise ArithmeticError('Global error certificate failed')
    gaussian_upper = n * math.log(n/epsilon)
    return {'n': n, 'epsilon': epsilon, 'q': q,
            'stage_count': len(stages), 'stages': stages,
            'final_modes': m, 'final_survival': final_q,
            'stage_allocated_error': allocated,
            'compression_error_bound': error_bound,
            'compression_computed_error_evaluation': computed_error,
            'compression_action': action,
            'gaussian_universal_upper': gaussian_upper,
            'interacting_certified_upper': min(action, gaussian_upper),
            'selected_protocol': ('compression' if action < gaussian_upper
                                  else 'Gaussian universal reset'),
            'selected_protocol_error_bound': (error_bound if action < gaussian_upper
                                               else epsilon),
            'gaussian_witness_lower': gaussian_witness_action(n, epsilon),
            'general_spectral_lower': max(0.0, n*math.log(2)+math.log1p(-epsilon)),
            'asymptotic_compression_coefficient': math.log(1/q)/(1-binary_entropy(p))}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).parent/'results'/'finite_protocol.json')
    args = parser.parse_args()
    sizes = [64, 256, 1024, 4096, 16384, 65536, 1000000]
    examples = [plan(n) for n in sizes]
    # Deliberate small-register and high-accuracy checks exercise the cleanup
    # branch and the non-asymptotic error bookkeeping.
    edge = [plan(n, e) for n in [1, 2, 7, 128]
            for e in [0.49, 0.1, 1e-6]]
    result = {'status': 'passed', 'examples': examples,
              'additional_cases_checked': len(edge),
              'scope': 'Explicit achievable upper bounds, not interacting optima; fixed-error asymptotics are analytical.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    for x in examples:
        print(f"n={x['n']:7d}  G_lower/n={x['gaussian_witness_lower']/x['n']:.6f}  "
              f"I_upper/n={x['interacting_certified_upper']/x['n']:.6f}  "
              f"stages={x['stage_count']:2d}  final={x['final_modes']:3d}  "
              f"selected_error_bound={x['selected_protocol_error_bound']:.8f}")
    print(f'PASS: {len(examples)+len(edge)} deterministic plans; {args.output}')


if __name__ == '__main__':
    main()
