from generate_ampl_model import generate_ampl_model
from run_baron_neos import single_run_baron_neos, batch_run_baron_neos
from run_couenne_neos import single_run_couenne_neos, batch_run_couenne_neos

EMAIL = "rrele@asu.edu"

single_run_baron_neos(
        model="models/quadratic_equality_outside_ball.mod",
    log_output="../data/baron_quad_ex_test.log",
    email=EMAIL,
    timeout=600
)

single_run_couenne_neos(
    model="models/quadratic_equality_outside_ball.mod",
    log_output="../data/couenne_quad_ex_test.log",
    email=EMAIL,
    timeout=600
)