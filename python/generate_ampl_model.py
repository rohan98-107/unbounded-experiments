def generate_ampl_model(
    filename,
    objective,
    constraints,
    variables=None,
    bounds=None
):
    """
Generate a simple AMPL model for polynomial optimization.
Intended for BARON / Couenne via NEOS.
"""

    with open(filename, "w") as f:
        f.write("# Generated AMPL model\n\n")

        for v in variables:
            if bounds is not None and v in bounds:
                lo, hi = bounds[v]

                if lo is None and hi is None:
                    f.write(f"var {v};\n")
                elif lo is None:
                    f.write(f"var {v} <= {hi};\n")
                elif hi is None:
                    f.write(f"var {v} >= {lo};\n")
                else:
                    f.write(f"var {v} >= {lo} <= {hi};\n")
            else:
                f.write(f"var {v};\n")

        f.write("\n")
        f.write(f"minimize obj: {objective};\n\n")

        for i, c in enumerate(constraints):
            f.write(f"subject to c{i+1}: {c};\n")

    print(f"Wrote AMPL model: {filename}")
