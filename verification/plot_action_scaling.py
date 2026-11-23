"""Compare exact Gaussian action with finite interacting certificates."""
from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/fermionic-reset-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from finite_protocol import gaussian_reset_action, mirrored_tree_certificate, plan


def main() -> None:
    root = Path(__file__).resolve().parent
    sizes = np.unique(np.round(np.geomspace(64, 1_000_000, 190)).astype(int))
    rows = []
    epsilon = 0.1
    for n in sizes:
        n = int(n)
        gaussian = gaussian_reset_action(n, epsilon)
        tree = mirrored_tree_certificate(n, epsilon)
        compression = plan(n, epsilon, q=0.2)
        certificates = {'equal Gaussian exposure': gaussian,
                        'mirrored tree': tree['action'],
                        'entropy compression': compression['compression_action']}
        selected = min(certificates, key=certificates.get)
        rows.append({'n': n, 'epsilon': epsilon, 'gaussian_optimal_action': gaussian,
                     'interacting_certified_upper': certificates[selected],
                     'interacting_lower': max(compression['general_spectral_lower'],
                                              -2 * math.log(epsilon)),
                     'selected_protocol': selected, 'mirrored_tree': tree})
    gaussian = np.array([x['gaussian_optimal_action']/x['n'] for x in rows])
    interacting = np.array([x['interacting_certified_upper']/x['n'] for x in rows])
    lower = np.array([x['interacting_lower']/x['n'] for x in rows])
    if not np.all(lower <= interacting+1e-10):
        raise ArithmeticError('Interacting lower/upper order failed')
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'svg.fonttype': 'none', 'svg.hashsalt': 'fermionic-reset',
                         'axes.spines.top': False,
                         'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(9.1, 5.3))
    navy, teal, gray = '#274C77', '#008571', '#737B83'
    ax.fill_between(sizes, lower, interacting, color=teal, alpha=0.10)
    ax.plot(sizes, gaussian, color=navy, linewidth=2.3, label='Exact Gaussian optimum')
    ax.plot(sizes, interacting, color=teal, linewidth=2.7,
            label='Interacting universal construction')
    ax.plot(sizes, lower, color=gray, linewidth=1.2, linestyle=':',
            label='Interacting lower bound')
    ax.set_xscale('log')
    ax.set_xlim(64, 1_000_000)
    ax.set_ylim(0, 17)
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
             'The interacting band is bounded by a converse and explicit schedules.',
             fontsize=9.3, color='#4C5662')
    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.145, top=0.83)
    figures = root/'figures'; figures.mkdir(exist_ok=True)
    svg = figures/'action_scaling.svg'
    fig.savefig(svg, metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig('/tmp/fermionic-reset-action-scaling.png', dpi=150)
    plt.close(fig)
    results = root/'results'; results.mkdir(exist_ok=True)
    (results/'scaling_series.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(f'PASS: {len(rows)} plotted protocols and bound-order checks; {figures}/action_scaling.svg')


if __name__ == '__main__':
    main()
