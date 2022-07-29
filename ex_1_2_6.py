import itertools
import math
import utils
from tabulate import tabulate

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

# 5.
# 11^4 = 14641
#         10       11
# 0       10        1
# 1      110       11
# 2     1210      121
# 3    13310     1331
# 4             14641
def pascal11(p):
    rows = [[0, 10, 1]]
    for i in range(1, p + 1):
        prev = rows[i - 1]
        pow = prev[1] + prev[2];
        rows.append([i, 10 * pow, pow])
    return rows

def printPascal11():
    print(tabulate(pascal11(4), headers=['', '10', '11'], tablefmt='orgtbl'))

# (10 + 1)^4 = 10^4 + 4 * 10^3 + 6 * 10^2 + 4 * 10 + 1 = 10000 + 4000 + 600 + 40 + 1 = 14641

# 6.
# pascal triangle
row0 = {0: 1}

def getPascalRow(rowIndex, prev, left, right):
    row = {}
    for i in range(left, right + 1):
        v = prev.get(i - 1, 0) + prev.get(i, 0)
        if v != 0:
            row[i] = v
    return row

def getPrevPascalRow(rowIndex, next, left, right):
    row = {0: 1}
    for i in range(1, right + 1):
        v = next.get(i, 0) - row.get(i - 1, 0)
        if v != 0:
            row[i] = v
    return row

def rowToList(row, i, l, r):
    list = [i]
    for i in range(l, r + 1):
        list.append(row.get(i, 0))
    return list

def printPascalTriangle():
    l = 0
    r = 9
    headers = ['r']
    for i in range(l, r + 1):
        headers.append('by ' + str(i))
    values = []
    row = row0
    for i in range(-1, -4, -1):
        row = getPrevPascalRow(i, row, l, r)
        values.insert(0, rowToList(row, i, l, r))
    values.append(rowToList(row0, 0, l, r))
    row = row0
    for i in range(1, r + 1):
        row = getPascalRow(i, row, l, r)
        values.append(rowToList(row, i, l, r))
    print(tabulate(values, headers=headers, tablefmt='orgtbl'))

def callPrintPascalTriangle():
    printPascalTriangle()

# 7. max combinations count
#c = n! / (k! (n-k)!)

#n (n-1) (n-2) ... (n-k+1)
#1 2 3 ... k

# После n/2 числитель начинает расти медленнее знаменателя, следовательно максимум при k=(n/2).
# Для нечетных n максимум = floor(n/2)=ceil(n/2) в силу симметричности.

#8.
# C1(0) = C1(1)
# C2(0) = C2(2)
# C3(1) = C3(2), C3(0) = C3(3)
# Cn(k) = Cn(n-k)

#9. Cn(n) = Cn(0)
# n >= 0: Cn(n) = 1
# n < 0:
#     n = -1: Cn(n) != Cn(0)
# Из треугольника Паскаля для отрицательных n видно, что Cn(0) = 1.
# Однако из треугольника также видно, что для всех k < 0 Cn(k) должно быть равно 0.

        
# 10.
# Cn(k)
#n (n-1) (n-2) ... (n-k+1)
#1 2 3 ... k

n n-1 n-2
k k-1 k-2

C8(5)
8 7 6
5 4 3

p = 4

n mod p = 8 mod 4 = 0
k mod p = 5 mod 4 = 1

C0(1) = 1
