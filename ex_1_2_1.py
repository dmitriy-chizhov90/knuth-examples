#! python3

import math
import numpy
from tabulate import tabulate

# 7.

def square_sum(n):
    s = 0
    sg = -1 if n % 2 == 0 else 1
    for i in range(n):
        s += sg * int(math.pow((i+1), 2))
        sg *= -1
    return s

def print_square_sum():
    for i in range(5):
        print(i+1, square_sum(i+1))

# 11.

def nomerator_11(i):
    return math.pow(2*i+1, 3)

def denom_11(i):
    return (math.pow(2*i+1, 4) + 4)

def formula_11_item(i):
    return math.pow(-1, i) * nomerator_11(i) / denom_11(i)

def formula_11(n):
    s = 0
    for i in range(n + 1):
        s += formula_11_item(i)
    return s

def lcm(a, b):
    return (a*b) // math.gcd(a, b)

def print_formula_11():
    _n, _d, _s = 0, 1, -1
    
    for i in range(100):
        
        n, d, s = int(nomerator_11(i)), int(denom_11(i)), _s * (-1)
        dd = lcm(_d, d)
        _k, k = dd//_d, dd//d
        nn = _k*_n + k*n*s
        
        gcd = math.gcd(int(nn), int(dd))
    
        _n, _d, _s = nn//gcd,dd//gcd,s
        print(i, _n, _d, formula_11(i), formula_11_item(i), _n/_d)

# 12.

def is_non_negative_sqrt2(y, z):
    if y == 0 and z == 0:
        return True
    if y == 0:
        return z >= 0
    if z == 0:
        return y >= 0
    if y > 0 and z > 0:
        return True
    if y < 0 and z < 0:
        return False
    if y*y > 2*z*z:
        return y > 0
    return z > 0

def division_sqrt2(u, v, w, x):
    c = 0
    while True:
        u, v = dif_sqrt2(u, v, w, x)
        if is_non_negative_sqrt2(u, v):
            c += 1
        else:
            return c

def mult_sqrt2(u, v, w, x):
    return (u*w + 2*v*x), (u*x + v*w)

def sum_sqrt2(u, v, w, x):
    return (u+w), (v+x)

def dif_sqrt2(u, v, w, x):
    return (u-w), (v-x)

def mod_sqrt2(u, v, w, x, q):
    mu, mv = mult_sqrt2(w, x, q, 0)
    return dif_sqrt2(u, v, mu, mv)

def is_zero_sqrt(u, v):
    u2, v2 = mult_sqrt2(u, v, u, v)
    return ((u2 + v2) == 0)

headers = ['mu', 'mv', 'nu', 'nv', 'du', 'dv']
table = []

def fsqrt2(u, v):
    if v == 0:
        return f'{u}'
    if u == 0:
        return f'{v}\/2'
    return f'{u}{v:+}\/2'

def euclides_sqrt2(mu, mv, nu, nv):
    i, cnt = 0, 100
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    while not is_zero_sqrt(nu, nv):
        q = division_sqrt2(mu, mv, nu, nv)
        q10 = division_sqrt2(mu*10, mv*10, nu, nv)
        q100 = division_sqrt2(mu*100, mv*100, nu, nv)
        du, dv = mod_sqrt2(mu, mv, nu, nv, q)
        ratio = 0
        print(f'{i}:: m: {fsqrt2(mu, mv)}, n: {fsqrt2(nu, nv)}, d: {fsqrt2(du, dv)}, q: {q}, q10: {q10}, q100: {q100}')
        mu, mv = nu, nv
        nu, nv = du, dv
        
        i += 1
        if cnt == i:
            return None, None
    return mu, mv

def add_euclides(mu, mv, nu, nv):
    global table
    du, dv = euclides_sqrt2(mu, mv, nu, nv)
    table.append([mu, mv, nu, nv, du, dv])

def print_euclides_sqrt2():
    add_euclides(1347, 0, 52, 0)
    add_euclides(1, 0, 0, 1)

    print(tabulate(table, headers, tablefmt='orgtbl'))

# 13.

def euclides_cnt(m, n):
    rows = []
    T = 0

    T += 1
    a, _a = 0, 1
    b, _b = 1, 0
    c, d = m, n
    
    while True:
        T += 1
        q, r = c // d, c % d

        rows.append([(T-2)/3, T, c, d, q, r, a, b, _a, _b, n-r])

        T += 1
        if r == 0:
            return rows

        T += 1
        c, d = d, r
        _a, a = a, _a - q*a
        _b, b = b, _b - q*b
   
headers=['(T-2)/3', 'T', 'c', 'd', 'q', 'r', 'a', 'b', '_a', '_b', 'n-3']
for i in range(34, 35):
    print(tabulate(euclides_cnt(1347, i), headers, tablefmt='orgtbl'))
