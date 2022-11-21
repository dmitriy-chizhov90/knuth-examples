#! python3

import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from random import randrange

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

# 38.
def sum_38(x, y):
    s = 0
    n = math.ceil(y)
    for k in range(n):
        s+=int(math.floor(x+float(k)/y))
    st=math.floor(x)*math.ceil(y)+math.ceil(y)-math.ceil(y*(1-x+math.floor(x)))
    print(f"sum_38(x: {x}, y: {y})={s} or {st}")
    return s

def print_sum_38():
    sum_38(10,2)
    sum_38(10.5,2.5)
    sum_38(10.5,9.5)

# 41.
# Функция возвращает k для суммы арифметической прогрессии Sk=1+2+...+k.
def revert_arithmetic(sk):
    return (math.sqrt(8*sk+1)-1)/2

def print_revert_arithmetic():
    for i in range(1,16):
        k=revert_arithmetic(i)
        print(f'{i}: {math.ceil(k)}')

#print_revert_arithmetic()

#44.
def first_frac_44(n, b, k):
    return n/math.pow(b, k+1)

def second_frac_44(j, b):
    return j/b

def item_44(n, j, b, k):
    return first_frac_44(n, b, k)+second_frac_44(j, b)

def item_floor_44(n,j,b,k):
    return int(math.floor(item_44(n,j,b,k)))

def sum_j_44(n,b,k):
    s=0
    for j in range(1, b):
       s+=item_floor_44(n,j,b,k)
    return s

def first_approx_44(n,b,k):
    return item_floor_44(n,b-1,b,k)

def print_sums_j_44(n, b, kmax):
    print(f'n: {n}, b: {b}, log_{{b}}{{n}}: {math.log(n, b) if n>0 else 0:.3f}')
    headers = ["j\k"]
    rows=[[f"{i+1}"] for i in range(b-1)]
    sums=["s"]
    part_sums=["part_s"]
    j_lower=["j_lower"]
    j_upper=["j_upper"]
    first_approx=["first_approx"]
    for k in range(kmax):
        headers.append(k)
        for j in range(1,b):
            rows[j-1].append(f"{item_floor_44(n,j,b,k)} is {item_44(n,j,b,k):.3f} is {first_frac_44(n,b,k):.3f}+{second_frac_44(j,b):.3f}")
        sums.append(sum_j_44(n,b,k))
        part_sums.append((b-1)*item_floor_44(n,b-1,b,k))
        jl=(int(math.floor(first_frac_44(n,b,k)))+1)*b-n/math.pow(b,k)-1
        j_lower.append(f"{math.ceil(jl):.3f}")
        j_upper.append(f"{-math.floor(-jl):.3f}")
        first_approx.append(f"{first_approx_44(n,b,k):.3f}")
    rows.append(sums)
    rows.append(part_sums)
    rows.append(j_lower)
    rows.append(j_upper)
    rows.append(first_approx)

    print(tabulate(rows, headers=headers, tablefmt='orgtbl'))
def print_tables_44():
    print_sums_j_44(10, 7, 5)
    print_sums_j_44(81, 9, 5)
    print_sums_j_44(80, 9, 5)
    print_sums_j_44(79, 9, 5)
    print_sums_j_44(78, 9, 5)
    print_sums_j_44(77, 9, 5)
    print_sums_j_44(76, 9, 5)
    print_sums_j_44(75, 9, 5)
    print_sums_j_44(74, 9, 5)
    print_sums_j_44(73, 9, 5)
    print_sums_j_44(72, 9, 5)
    print_sums_j_44(71, 9, 5)
    print_sums_j_44(-71, 9, 5)
    
def check_44(n, b):
    l=int(math.floor(math.log(n,b)))
    d=[]
    s=f'{n}='
    c=0
    for i in range(l):
        p=l-i
        pp=math.pow(b,p)
        q,r=int(n/pp), n%pp
        n=r
        d.append(q)
        s+=f'{q}*{b}^{p}+'
        c+=q*pp
    s+=f'{n}'
    c+=n
    print(s, c)


#check_44(73, 9)

#45.
def check_floor_revertion(m,n):
    for j in range(n):
        r=int(math.floor(m*j/n))
        jc=int(math.ceil(n*r/m))
        print(f'{"SUCC" if j==jc else "FAIL"}: m: {m}, n: {n}, j: {j}, r: {r}, j\': {jc}')

def random_check():
    for i in range(10):
        check_floor_revertion(randrange(100)+1, randrange(100)+1)
            
random_check()
        
