import numpy as np
from _bootstrap import bootstrap_asymptoticFunction
bootstrap_asymptoticFunction()

from asymptoticFunction.numerical.sampling import sample_sphere
from certificate_tests import *

def certify_unbounded_vanilla(
        f_asymptotic,
        g_asymptotics,
        dim,
        *,
        n_samples=4096,
        seed=0
):
    """
Vanilla asymptotic certificate.

Parameters
----------
f_asymptotic : callable
Function (f, d, **params) -> float computing f_∞(d)
g_asymptotics : list of callables
Each g_i_∞(d)
dim : int
Dimension
n_samples : int
Number of directions sampled on the unit sphere
seed : int

Returns
-------
dict with keys:
unbounded : bool
witness   : ndarray or None
f_value   : float or None
"""

    D = sample_sphere(
        n_samples=n_samples,
        dim=dim,
        method="sobol",
        seed=seed
    )

    ### ---------------------------------------------------------------------
    ### THIS IS NOT TECHNICALLY PART OF THE CERTIFICATE, THIS IS AXIS-CHECKING
    axes = np.vstack([np.eye(dim), -np.eye(dim)])
    D = np.vstack([axes, D])
    ### ----------------------------------------------------------------------

    for d in D:
        # check asymptotic feasibility
        feasible = True
        for g_inf in g_asymptotics:
            if g_inf(None, d) >= 0.0:
                feasible = False
                break

        if not feasible:
            continue

        # check objective descent
        f_val = f_asymptotic(None, d)
        if f_val < 0.0:
            return {
                "status": "proved unbounded",
                "witness": d,
                "f_inf": float(f_val)
            }

    return {
        "status": "unable to find unbounded direction",
        "direction": None,
        "f_inf": None
    }

def main():
    dim = 2

    f_inf, g_infs = build_paper_hard_example()

    res = certify_unbounded_vanilla(
        f_asymptotic=f_inf,
        g_asymptotics=g_infs,
        dim=dim,
        n_samples=65536,   # you can vary this
        seed=0
    )

    print(res)


if __name__ == "__main__":
    main()
