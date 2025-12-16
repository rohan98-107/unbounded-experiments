include("test_unbounded.jl")

@polyvar x1 x2

f = (x1^2 - x2^2)^2 - x2^3

K = @set ((x1^2 - x2^2)^2 <= 0) && (1 - x1^2 - x2^2 <= 0)

test_unbounded(
    "Quadratic-equality cone outside ball (2D)",
    f;
    domain = K
)

