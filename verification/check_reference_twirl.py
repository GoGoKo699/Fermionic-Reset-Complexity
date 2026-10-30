"""Finite checks for the parity-preserving universal reset construction.

These checks validate algebra and finite inequalities. They are not the proof
of the universal action bound, which is in science/interacting_reset.md.

Run from the repository root: python verification/check_reference_twirl.py
The JSON summary is printed and saved to verification/results/reference_twirl.json.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm


def kron_all(parts):
    out = np.array([[1.0 + 0j]])
    for part in parts:
        out = np.kron(out, part)
    return out


I = np.eye(2)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1])
sm = np.array([[0, 1], [0, 0]], complex)


def ptrace_system(rho, dim):
    return np.trace(rho.reshape(dim, 2, dim, 2), axis1=0, axis2=2)


def loss_channel(rho, c, q):
    n = c.conj().T @ c
    k0 = np.eye(c.shape[0]) + (math.sqrt(q) - 1) * n
    k1 = math.sqrt(1-q) * c
    return k0 @ rho @ k0.conj().T + k1 @ rho @ k1.conj().T


def run():
    rng = np.random.default_rng(20261030)
    twirl_errors = []
    loss_errors = []
    for m in [1, 2, 3, 4]:
        d = 2**m
        w = []
        for j in range(m):
            for local in [X, Y]:
                w.append(kron_all([Z]*j+[local]+[I]*(m-j-1)))
        parity = kron_all([Z]*m)
        mat = rng.normal(size=(2*d, 2*d)) + 1j*rng.normal(size=(2*d, 2*d))
        rho = mat @ mat.conj().T
        rho /= np.trace(rho)
        rr = ptrace_system(rho, d)
        delta = ptrace_system(np.kron(parity, I) @ rho, d)
        predicted = np.kron(np.eye(d)/d, rr)+np.kron(parity/d, delta)
        twirled = np.zeros_like(rho)
        count = 0
        for bits in range(2**(2*m)):
            if bits.bit_count()%2:
                continue
            u = np.eye(d, dtype=complex)
            for j in range(2*m):
                if (bits >> j)&1:
                    u = u @ w[j]
            ur = np.kron(u, I)
            twirled += ur @ rho @ ur.conj().T
            count += 1
        twirled /= count
        err = np.linalg.norm(twirled-predicted, ord='nuc')/2
        twirl_errors.append(float(err))
        assert err < 2e-12
        q = 0.25
        out = twirled.copy()
        for j in range(m):
            c = kron_all([Z]*j+[sm]+[I]*(m-j-1))
            out = loss_channel(out, np.kron(c, I), q)
        sigma = np.diag([1-q/2, q/2])
        rhs = np.kron(kron_all([sigma]*m),rr)+q**m*np.kron(parity/d,delta)
        err = np.linalg.norm(out-rhs, ord='nuc')/2
        loss_errors.append(float(err))
        assert err < 2e-12

    h = -0.25*math.log2(0.25)-0.75*math.log2(0.75)
    alpha = (1+h)/2
    for m in range(24, 1000):
        mp = math.ceil(h*m)+1
        assert mp <= alpha*m+1e-12
        k = m//4
        ev = sum(math.comb(m,j) for j in range(0,k+1,2))
        od = sum(math.comb(m,j) for j in range(1,k+1,2))
        assert max(ev,od) <= 2**(mp-1)
    constants = []
    for epsilon in [0.49,0.1,1e-3,1e-6,1e-12]:
        cutoff=max(24,math.ceil(32*math.log(256/epsilon)))
        error=math.exp(-cutoff/32)/(1-math.exp(-1/32)) + 0.5*4.0**(-cutoff)/(1-0.25)
        assert error <= epsilon/2
        constants.append({'epsilon':epsilon,'cutoff':cutoff,'stage_error_bound':error,
                          'linear_action_coefficient':math.log(4)/(1-alpha),
                          'final_action_bound':cutoff*math.log(2*cutoff/epsilon)})
    result={'status':'passed','seed':20261030,
            'twirl_dimensions_modes':[1,2,3,4],
            'max_reference_twirl_half_trace_residual':max(twirl_errors),
            'max_reference_loss_identity_half_trace_residual':max(loss_errors),
            'parity_embedding_sizes_checked':[24,999],
            'cutoff_inequalities':constants,
            'scope':'Finite algebra/constant checks; universal proof is analytical.'}
    path=Path(__file__).resolve().parent/'results'/'reference_twirl.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
