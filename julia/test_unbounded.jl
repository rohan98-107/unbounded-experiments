using JuMP
using DynamicPolynomials
using SumOfSquares
using MosekTools

function test_unbounded(name, f; domain = nothing, maxdegree = nothing)
    println("---------------------------------------------------")
    println("TEST: ", name)
    println("f = ", f)
    println("---------------------------------------------------")

    model = SOSModel(MosekTools.Optimizer)
    set_time_limit_sec(model, 300.0)

    @variable(model, γ)

    if domain === nothing
        if maxdegree === nothing
            @constraint(model, f - γ in SOSCone())
        else
            @constraint(model, f - γ in SOSCone(), maxdegree = maxdegree)
        end
    else
        if maxdegree === nothing
            @constraint(model, f - γ in SOSCone(), domain = domain)
        else
            @constraint(model, f - γ in SOSCone(), domain = domain, maxdegree = maxdegree)
        end
    end

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
