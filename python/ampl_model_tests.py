from generate_ampl_model import generate_ampl_model

# Regenerate the masked high-dimensional model (now with constraints!)
generate_ampl_model(
    filename="models/highdim_maskedA_unbounded_n12.mod",
    objective=(
        "x1^8*((x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + "
        "x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2) - 1)^2 "
        "- (x1^2*(x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + "
        "x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2))^2 "
        "- x1"
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