import os
print("RUNNING FILE:", os.path.abspath(__file__))

import pyomo.environ as pyo

m = pyo.ConcreteModel()

# IMPORTANT FIX: explicitly set domain or bounds
m.x = pyo.Var(domain=pyo.Reals)
m.y = pyo.Var(domain=pyo.Reals)

m.obj = pyo.Objective(expr=m.x**2 + m.y**2)

def con_rule(m):
    print("Executing constraint rule")
    return m.x + m.y <= 5

m.c = pyo.Constraint(rule=con_rule)

m.write("test.nl", io_options={"symbolic_solver_labels": True})
print("Wrote test.nl")
