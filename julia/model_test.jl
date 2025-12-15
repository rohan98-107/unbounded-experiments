include("test_unbounded.jl")

@polyvar x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12

s = x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2

f = x1^8 * s - x1^9

K = @set (s - x1 <= 0) && (1 - s <= 0)

test_unbounded(
    "High-degree unbounded (n = 12, k = 4)",
    f;
    domain = K,
    maxdegree = 12
)
