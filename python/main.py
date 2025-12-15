from run_baron_neos import run_baron_neos
from run_couenne_neos import run_couenne_neos


MOD_FILE = "models/curved_feasible_unbounded.mod"
EMAIL = "rrele@asu.edu"


baron_log = run_baron_neos(MOD_FILE, EMAIL)
with open("../data/baron_false_boundedness.log", "w") as f:
    f.write(baron_log)

print("Saved BARON log")

'''
couenne_log = run_couenne_neos(MOD_FILE, EMAIL)
with open("../data/couenne_false_boundedness.log", "w") as f:
    f.write(couenne_log)

print("Saved Couenne log")
'''