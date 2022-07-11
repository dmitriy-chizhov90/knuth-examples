import math

import ex_1_2_4 as utils

# 1.
def printFactorials():
    utils.printExp('math.factorial(36)', 371993326789901217467999448150835200000000)
    utils.printExp('math.factorial(52)', 80658175170943878571660636856403766975289505440883277824000000000000)

# 4.
def printFractPowers():
    utils.printExp('math.pow(10, 0.5)', 3.1622776601683795)
    utils.printExp('math.pow(10, 1.5)', 31.622776601683793)
    utils.printExp('math.pow(10, 2.5)', 316.22776601683796)
    utils.printExp('math.pow(10, 3.5)', 3162.2776601683795)

    utils.printExp('math.pow(10, 0.60464)', 4.023833481595328)

# 5.
utils.printExp('math.sqrt(2.*math.pi*8.)*math.pow((8./math.e), 8.)*(1. + 1./(12.*8.))', 40318.045405288554)
utils.printExp('math.factorial(8)', 40320)
utils.printExp('(40320 - 40318.045405288554)/40320*100', 0.004847705137514086)

