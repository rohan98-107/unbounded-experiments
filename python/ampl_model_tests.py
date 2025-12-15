from generate_ampl_model import generate_ampl_model

# Existing bounded test
generate_ampl_model(
    filename="models/bounded_test.mod",
    objective="x^4 + y^4 + x^2*y + 3*x",
    constraints=[
        "x + y <= 5",
        "x - y >= -10"
    ],
    variables=["x", "y"],
    bounds={"x": (-100, 100), "y": (-100, 100)}
)

# Julia false-boundedness test
generate_ampl_model(
    filename="models/false_boundedness.mod",
    objective=(
        "x^4 + y^4 + 2*x^2*y^2 "
        "- 3*x^3 + 4*x*y^2 - 6*y"
    ),
    constraints=[],
    variables=["x", "y"],
    bounds={"x": (-1000, 1000), "y": (-1000, 1000)}
)

# true unboundedness
generate_ampl_model(
    filename="models/diagonal_unbounded.mod",
    objective="x^4 + y^4 + 2*x^2*y^2 - 4*x^3*y - 6*y",
    constraints=[
        "y - x = 0"
    ],
    variables=["x", "y"]
)

# Curved-feasible-set asymptotic unboundedness
generate_ampl_model(
    filename="models/curved_feasible_unbounded.mod",
    objective="x^2*y^2 - x^3",
    constraints=[
        "y^2 - x <= 0"
    ],
    variables=["x", "y"]
)

# High-degree unbounded (n = 12, k = 4)
generate_ampl_model(
    filename="models/highdim_highdegree_unbounded_n12_k4.mod",
    objective=(
        "-x1^9 + "
        "x1^8*(x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + "
        "x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2)"
    ),
    constraints=[
        "x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + "
        "x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2 - x1 <= 0",
        "1 - (x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + "
        "x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2) <= 0"
    ],
    variables=[
        "x1","x2","x3","x4","x5","x6",
        "x7","x8","x9","x10","x11","x12"
    ]
)

