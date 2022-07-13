import itertools
import math
import utils

# 3.
# Count of combinations from n by k.
def combi_count1(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

#def combi_count2(n, k):
#    return sum(1 for _ in itertools.combinations(range(n), k))

def check_combi_count(n, k, expected):
    r = combi_count1(n, k)
    print('combi count from {} by {} = {}, {}'.format(n, k, r, "OK" if r == expected else "!!! expected {}".format(expected)))

def combinationsFrom53By13():
    check_combi_count(52, 13, 635013559600)
    check_combi_count(52, 51, 52)
    check_combi_count(0, 0, 1)

# 4.
# r = n! / (k! * (n - k)!). In simple numbers

# Check if n is simple number
# leftSimpleNumbers - all simple numbers less than n and greater than 1.
def isSimpleNumber(n, lessSimpleNumbers):
    for sn, _ in lessSimpleNumbers.items():
        if n % sn == 0:
            return False
    return True

def simpleNumbers(n):
    sn = {}
    for i in range(2, n + 1):
        if isSimpleNumber(i, sn):
            sn[i] = 0

    return sn

def printSimpleNumbers():
    utils.printExp('simpleNumbers(2)', {2:0}, globals(), locals())
    utils.printExp('simpleNumbers(3)', {2:0, 3:0}, globals(), locals())
    utils.printExp('simpleNumbers(7)', {2:0, 3:0, 5:0, 7:0}, globals(), locals())

def snPowerInFactorial(n, sn):
    p = 0
    while (n > 0):
        n = int (n / sn)
        p += n
    return p

def printSnPowerInFactorial():
    utils.printExp('snPowerInFactorial(1000, 3)', 498, globals(), locals())
    
def factorialSimpleNumbers(n):
    sn = simpleNumbers(n)
    for i, _ in sn.items():
        sn[i] = snPowerInFactorial(n, i)
    return sn

def printFactSn():
    utils.printExp('factorialSimpleNumbers(1000)', {}, globals(), locals())

def snSub(a, b):
    for i, v in b.items():
        a[i] = a[i] - v
        if (a[i] == 0):
            del a[i]
    return a

def combinationsSn(n, k):
    nSn = factorialSimpleNumbers(n)
    kSn = factorialSimpleNumbers(k)
    nkSn = factorialSimpleNumbers(n - k)
    
    nSn = snSub(nSn, kSn)
    nSn = snSub(nSn, nkSn)
    
    return nSn


def evalSn(sn):
    r = 1
    for i, v in sn.items():
        r *= math.pow(i, v)
    return r

def printCombinationsSn():
    utils.printExp('combinationsSn(52, 13)', {2: 4, 5: 2, 7: 2, 17: 1, 23: 1, 41: 1, 43: 1, 47: 1}, globals(), locals())
    utils.printExp('evalSn(combinationsSn(52, 13))', 635013559600, globals(), locals())


