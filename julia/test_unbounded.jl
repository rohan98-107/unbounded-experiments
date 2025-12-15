using JuMP, DynamicPolynomials, SumOfSquares, MosekTools

function test_unbounded(name, f)
    println("---------------------------------------------------")
    println("TEST: ", name)
    println("f = ", f)
    println("---------------------------------------------------")

    model = Model(MosekTools.Optimizer)
    @variable(model, γ)
    @constraint(model, f - γ in SOSCone())
    @objective(model, Max, γ)

    optimize!(model)

    println("Status: ", termination_status(model))
    println("Primal: ", primal_status(model))
    println("Dual: ", dual_status(model))

    try
        println("γ = ", value(γ))
    catch
        println("γ undefined")
    end

    println()
end