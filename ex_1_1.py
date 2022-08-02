#! python3

import math
from tabulate import tabulate

def euclides(m, n):
    if n == 0:
        return m 
    
    while True:
        r = m % n
        if r == 0:
            return n
        m, n = n, r

rows = [
    [120, 17],
    [120, 20],
    [120, 25],
    [25, 120],
    [10, 1],
    [0, 123],
    [123, 0],
    [120, -25],
    [-120, 25],
    [-120, -25],
    [2166, 6099]
]

rows = [[m, n, euclides(m, n)] for m, n in rows]

print(tabulate(rows, headers=['m', 'n', 'E'], tablefmt='orgtbl'))

def checkE(f):
    for m, n, v in rows:
        if f(m, n) != v:
            print(f'Check failed: {m}, {n} = {f(m,n)}, but {v} expected')

# 3. E without assignment
def euclidesUnassign(m, n):
    if n == 0:
        return m 
    
    while True:
        m = m % n
        if m == 0:
            return n
        n = n % m
        if n == 0:
            return m

checkE(euclidesUnassign)

# 6. T_5

def euclidesE1Cnt(m, n):
    if n == 0:
        return 0 
    cnt = 0
    while True:
        r = m % n
        cnt += 1
        if r == 0:
            return cnt
        m, n = n, r

r5 = [[i+1, 5, euclides(i+1, 5), euclidesE1Cnt(i+1, 5)] for i in range(15)]
        
print(tabulate(r5, headers=['m', 'n', 'E', 'cnt'], tablefmt='orgtbl'))

# 7. U_m

r5 = [[5, i+1, euclides(5, i+1), euclidesE1Cnt(5, i+1)] for i in range(15)]
        
print(tabulate(r5, headers=['m', 'n', 'E', 'cnt'], tablefmt='orgtbl'))
