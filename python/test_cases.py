# Canonical polynomial test cases used across Julia (SOS)
# and Python (BARON / Couenne via NEOS)

TEST_CASES = {
    "false_boundedness": {
        "problem": {
            "vars": ["x", "y"],
            "bounds": 1000,
            "objective": (
                "x^4 + y^4 + 2*x^2*y^2 "
                "- 3*x^3 + 4*x*y^2 - 6*y"
            ),
        },
        "meta": {
            "description": (
                "SOS/MOSEK returns OPTIMAL with γ ≈ -9.0155 "
                "even though the true infimum is -∞"
            ),
            "source": "Julia moderate_dim_unbounded example",
        }
    }
}
