from generate_ampl_model import generate_ampl_model

generate_ampl_model(
    filename="models/quadratic_equality_outside_ball.mod",
    objective="(x1^2 - x2^2)^2 - x2^3",
    constraints=[
        "(x1^2 - x2^2)^2 <= 0",
        "1 - x1^2 - x2^2 <= 0"
    ],
    variables=["x1", "x2"]
)
