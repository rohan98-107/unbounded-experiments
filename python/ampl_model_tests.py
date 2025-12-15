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
