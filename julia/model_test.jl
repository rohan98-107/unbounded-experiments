include("test_unbounded.jl")

@polyvar x y
f_hard = x^4 + y^4 + 2x^2*y^2 - 3x^3 + 4*x*y^2 - 6*y

test_unbounded("Moderately difficult unbounded example", f_hard)
