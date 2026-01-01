import numpy as np
from asymptoticFunction.heuristics.exact_forms import (
    linear_asymptotic,
    quadratic_asymptotic,
    polynomial_decomposed_asymptotic
)


def build_linear_needle_cone(dim, eps):
    phi = [
        lambda d: 0.0,
        lambda d: -d[0]
    ]

    f_inf = lambda f, d: polynomial_decomposed_asymptotic(f, d, phi=phi)

    def g_inf(f, d):
        return float(np.sum(d[1:] ** 2) - eps * d[0] ** 2)

    def f_original(x):
        return -x[0]

    def g_original(x):
        return np.sum(x[1:] ** 2) - eps * x[0] ** 2

    return f_inf, [g_inf], dim, f_original, [g_original]


def build_needle_cone_problem(dim, eps):
    def phi4(d):
        return np.sum(d[1:] ** 4) - 2.0 * (eps ** 2) * (d[0] ** 4)

    phi = [
        lambda d: 0.0,
        lambda d: -d[0],
        lambda d: 0.0,
        lambda d: 0.0,
        phi4
    ]

    f_inf = lambda f, d: polynomial_decomposed_asymptotic(f, d, phi=phi)

    def g_inf(f, d):
        return float(np.sum(d[1:] ** 2) - eps * d[0] ** 2)

    def f_original(x):
        return (x[0] ** 2) * (np.sum(x[1:] ** 2) ** 2) - x[0]

    def g_original(x):
        return np.sum(x[1:] ** 2) - eps * x[0] ** 2

    return f_inf, [g_inf], dim, f_original, [g_original]


def build_singleton_ray_equality_like():
    def g_inf(_, d):
        return d[1] ** 2

    def f_inf(_, d):
        return -d[0]

    def f_original(x):
        return -x[0]

    def g_original(x):
        return x[1] ** 2

    return f_inf, [g_inf], 2, f_original, [g_original]


def build_coordinate_cross_cone(dim):
    g_infs = []
    g_originals = []

    for i in range(dim):
        for j in range(i + 1, dim):
            def g_inf(_, d, i=i, j=j):
                return (d[i] * d[j]) ** 2

            def g_original(x, i=i, j=j):
                return (x[i] * x[j]) ** 2

            g_infs.append(g_inf)
            g_originals.append(g_original)

    def f_inf(_, d):
        return -d[0]

    def f_original(x):
        return -x[0]

    return f_inf, g_infs, dim, f_original, g_originals


def build_false_positive_bounded_example():
    def g1_inf(_, d):
        return d[1] ** 2

    def g2_inf(_, d):
        return -d[0]

    def f_inf(_, d):
        return -d[1]

    def f_original(x):
        return -x[1]

    def g1_original(x):
        return x[1] ** 2

    def g2_original(x):
        return -x[0]

    return f_inf, [g1_inf, g2_inf], 2, f_original, [g1_original, g2_original]
    