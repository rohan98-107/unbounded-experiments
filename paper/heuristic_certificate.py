import numpy as np
from _bootstrap import bootstrap_asymptoticFunction
bootstrap_asymptoticFunction()

from asymptoticFunction.numerical.sampling import sample_sphere
from certificate_tests import *
from vanilla_certificate import certify_unbounded_vanilla


def certify_unbounded_biased(
        f_asymptotic,
        g_asymptotics,
        dim,
        *,
        n_samples=4096,
        seed=0,
        tau=1e-3,
        f_tol=0.0
):
    D = sample_sphere(
        n_samples=n_samples,
        dim=dim,
        method="sobol",
        seed=seed
    )

    axes = np.vstack([np.eye(dim), -np.eye(dim)])
    D = np.vstack([axes, D])

    for d in D:
        max_v = -np.inf
        for g_inf in g_asymptotics:
            v = g_inf(None, d)
            if v > max_v:
                max_v = v

        if max_v > tau:
            continue

        f_val = f_asymptotic(None, d)
        if f_val < f_tol:
            return {
                "status": "candidate",
                "direction": d,
                "f_inf": float(f_val)
            }

    return {
        "status": "unable to find unbounded direction",
        "direction": None,
        "f_inf": None
    }



def verify_ray_descent(f, g_list, d, *, t_vals=(1, 10, 100, 1000)):
    for t in t_vals:
        x = t * d
        for g in g_list:
            if g(x) > 0.0:
                return False
        if f(x) >= 0.0:
            return False
    return True


def run_test(name, builder, *, n_trials=10, n_samples=4096, tau=1e-6, f_tol=0.0):
    vanilla_proved = 0
    heuristic_candidates = 0
    heuristic_verified = 0

    print(name)

    for seed in range(n_trials):
        f_inf, g_infs, dim, f, g = builder()

        res_v = certify_unbounded_vanilla(
            f_asymptotic=f_inf,
            g_asymptotics=g_infs,
            dim=dim,
            n_samples=n_samples,
            seed=seed
        )
        vanilla_proved += (res_v["status"] == "proved")

        res_b = certify_unbounded_biased(
            f_asymptotic=f_inf,
            g_asymptotics=g_infs,
            dim=dim,
            n_samples=n_samples,
            seed=seed,
            tau=tau,
            f_tol=f_tol
        )

        if res_b["status"] == "candidate":
            heuristic_candidates += 1
            if verify_ray_descent(f, g, res_b["direction"]):
                heuristic_verified += 1

    print(f"vanilla proved      : {vanilla_proved}/{n_trials}")
    print(f"heuristic candidates: {heuristic_candidates}/{n_trials}")
    print(f"heuristic verified  : {heuristic_verified}/{n_trials}\n")



def main():
    tests = [
        ("Singleton-ray equality-like", build_singleton_ray_equality_like),
        ("Coordinate-cross cone", lambda: build_coordinate_cross_cone(dim=6)),
        ("False positive (bounded)", build_false_positive_bounded_example),
    ]

    n_samples = 4096

    for name, builder in tests:
        print(name)

        f_inf, g_infs, dim, f_orig, g_origs = builder()

        res_v = certify_unbounded_vanilla(
            f_asymptotic=f_inf,
            g_asymptotics=g_infs,
            dim=dim,
            n_samples=n_samples
        )

        res_b = certify_unbounded_biased(
            f_asymptotic=f_inf,
            g_asymptotics=g_infs,
            dim=dim,
            n_samples=n_samples,
            tau=1e-6,
            f_tol=0.0
        )

        print("  vanilla status :", res_v["status"])

        if res_b["status"] == "candidate":
            ok = verify_ray_descent(
                f_orig,
                g_origs,
                res_b["direction"]
            )
            print("  heuristic candidate -> verified:", ok)
        else:
            print("  heuristic status :", res_b["status"])

        print()


if __name__ == "__main__":
    main()
