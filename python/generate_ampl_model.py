def generate_ampl_model(
    filename,
    objective,
    constraints,
    variables,
    bounds
):
    """
Generate a simple AMPL model for polynomial optimization.
Intended for BARON / Couenne via NEOS.
"""

    with open(filename, "w") as f:
        f.write("# Generated AMPL model\n\n")

        for v in variables:
            lo, hi = bounds[v]
            f.write(f"var {v} >= {lo} <= {hi};\n")

        f.write("\n")
        f.write(f"minimize obj: {objective};\n")

    print(f"Wrote AMPL model: {filename}")
