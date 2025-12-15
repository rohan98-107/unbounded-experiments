from generate_ampl_model import generate_ampl_model
from run_baron_neos import single_run_baron_neos

EMAIL = "rrele@asu.edu"

single_run_baron_neos(
    model="models/highdim_maskedA_unbounded_n12.mod",
    log_output="../data/baron_constraints_test.log",
    email=EMAIL,
    timeout=600
)