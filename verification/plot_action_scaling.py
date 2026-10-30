"""Generate the action comparison directly from the certified finite protocol."""
from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/fermionic-reset-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from finite_protocol import plan


def main() -> None:
    root = Path(__file__).resolve().parent
    sizes = np.unique(np.round(np.geomspace(64, 1_000_000, 190)).astype(int))
    rows = []
    for n in sizes:
        data = plan(int(n), epsilon=0.1, q=0.2)
        rows.append({key: data[key] for key in [
            'n', 'epsilon', 'q', 'gaussian_witness_lower',
            'gaussian_universal_upper', 'interacting_certified_upper',
            'general_spectral_lower', 'selected_protocol',
            'selected_protocol_error_bound']})
    lower = np.array([x['gaussian_witness_lower']/x['n'] for x in rows])
    upper = np.array([x['gaussian_universal_upper']/x['n'] for x in rows])
    interacting = np.array([x['interacting_certified_upper']/x['n'] for x in rows])
    spectral = np.array([x['general_spectral_lower']/x['n'] for x in rows])
    if not np.all(lower <= upper+1e-10):
        raise ArithmeticError('Gaussian lower/upper order failed')
    if not np.all(spectral <= interacting+1e-10):
        raise ArithmeticError('Interacting lower/upper order failed')
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'svg.fonttype': 'none', 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(9.1, 5.3))
    navy, teal, gray = '#274C77', '#008571', '#737B83'
    ax.fill_between(sizes, lower, upper, color=navy, alpha=0.13,
                    label='Gaussian universal optimum: bounded region')
    ax.plot(sizes, lower, color=navy, linewidth=2.1,
            label='Exact maximally mixed-input lower bound')
    ax.plot(sizes, upper, color=navy, linewidth=1.3, linestyle='--',
            label='Gaussian universal construction')
    ax.plot(sizes, interacting, color=teal, linewidth=2.7,
            label='Interacting universal construction')
    ax.plot(sizes, spectral, color=gray, linewidth=1.2, linestyle=':',
            label='General spectral lower bound')
    ax.set_xscale('log')
    ax.set_xlim(64, 1_000_000)
    ax.set_ylim(0, 17.5)
    ax.set_xlabel('Register size n (modes)', labelpad=8)
    ax.set_ylabel('Damping action per mode, A / n', labelpad=8)
    ax.set_title('Interactions remove the global-reset logarithm',
                 loc='left', pad=28, fontsize=16, fontweight='bold')
    ax.text(0, 1.035, 'Global half-diamond error ε = 0.1  ·  one loss port  ·  fast coherent control',
            transform=ax.transAxes, color='#4C5662', fontsize=10)
    ax.grid(axis='y', color='#DDE2E7', linewidth=0.65)
    ax.set_axisbelow(True)
    ax.legend(loc='upper left', frameon=False, fontsize=9.1,
              labelspacing=0.65, handlelength=3.0)
    fig.text(0.12, 0.015,
             'Upper curves include reference correlations. Coherent synthesis cost is not included.',
             fontsize=9.3, color='#4C5662')
    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.145, top=0.83)
    figures = root/'figures'; figures.mkdir(exist_ok=True)
    fig.savefig(figures/'action_scaling.svg', metadata={'Date': None})
    fig.savefig('/tmp/fermionic-reset-action-scaling.png', dpi=150)
    plt.close(fig)
    results = root/'results'; results.mkdir(exist_ok=True)
    (results/'scaling_series.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(f'PASS: {len(rows)} plotted protocols and bound-order checks; {figures}/action_scaling.svg')


if __name__ == '__main__':
    main()
