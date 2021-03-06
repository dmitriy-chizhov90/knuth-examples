#! python3

import math
import matplotlib.pyplot as plt
import numpy as np

def printFloorCeil():
    printExp("math.floor(1.1)", 1)
    printExp("math.floor(-1.1)", -2)
    printExp("math.ceil(-1.1)", -1)
    printExp("math.floor(0.99999)", 0)
    printExp("math.floor(math.log2(35))", 5)


def round(x):
    return math.floor(x + 0.5)

def printRound():
    printExp("round(0.1)", 0)
    printExp("round(0.4)", 0)
    printExp("round(0.5)", 1)
    printExp("round(0.9)", 1)
    printExp("round(0.49999999999)", 0)
    printExp("round(0.50000000001)", 1)

    printExp("round(-0.1)", 0)
    printExp("round(-0.4)", 0)
    printExp("round(-0.5)", 0)
    printExp("round(-0.9)", -1)
    printExp("round(-0.49999999999)", 0)
    printExp("round(-0.50000000001)", -1)

    printExp("round(0.5)", 1)
    printExp("round(-0.5)", 0)

def findInversion(a, m):
    for i in range(1000):
        if (a * i) % m == 1:
            return i

    return 0

def printFindInversion():
    printExp("findInversion(10, 5)", 0)
    printExp("findInversion(6, 3)", 0)

# 34.
def printLogarithms():
    t = np.arange(1., 500., 0.2)

    plt.plot(t, np.floor(np.log10(t)), 'r-', t, np.floor(np.log10(np.floor(t))), 'g-')
    plt.plot(t, np.floor(np.log(t)), 'm-', t, np.floor(np.log(np.floor(t))), 'b-')
    plt.show()
