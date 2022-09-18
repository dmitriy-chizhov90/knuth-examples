#! python3

import math
import numpy as np
from tabulate import tabulate

# 8.

def power(n, m):
    p = 1
    for i in range(m):
        p *= n
    return p

def bin_search(u, m):
    v = int(u)
    part = v

    while True:
        sq = power(v, m)
        sq_next = power(v+1, m)
        if sq <= u and u < sq_next:
            return v
        if part > 1:
            part = part // 2
        if u < sq:
            v -= part
        else:
            v += part
        
def check_bin_search(u, m, exp):
    v = bin_search(u, m)
    if v != exp:
        print(f'FAIL! bin_search({u}, {m}) = {v}, but {exp} expected')
    else:
        print(f'bin_search({u}, {m}) = {v}')

def test_bin_search():
    check_bin_search(4, 2, 2)
    check_bin_search(27, 3, 3)
    check_bin_search(25, 2, 5)
    check_bin_search(64, 2, 8)
    check_bin_search(10, 2, 3)
    check_bin_search(2, 2, 1)
    check_bin_search(1.5, 2, 1)
    check_bin_search(1, 2, 1)
    check_bin_search(0.9, 2, 0)

def chop_0(digits):
    while len(digits) > 1 and digits[-1] == '0':
        digits = digits[:-1]
    return digits

def sqrt_seq(u, m, k=100):
    n = bin_search(u, m)
    c = 1
    v, v_real, v_real_next = n, n, n
    sq = power(v, m)
    digits = []

    for i in range(k):
        c *= 10
        v *= 10
        for i in range(10):
           v_next  = v + 1
           v_real_next = v_next / c
           sq_next = power(v_real_next, m)
           if sq <= u and u < sq_next:
               digits.append(str(i))
               break
           sq, v, v_real = sq_next, v_next, v_real_next

    digits = chop_0(digits)
    print(v_real, v_real_next, f'{n}.{"".join(digits)}')
    return v_real, v_real_next

def check_sqrt_seq(u, m, exp):
    v, v_next = sqrt_seq(u, m)
    if v <= exp and exp < v_next:
        print(f'sqrt_seq({u}, {m}) = {v}, {v_next} ({power(v, m)}, {power(v_next, m)})')
    else:
        print(f'FAIL! sqrt_seq({u}, {m}) = {v} ({power(v, m)}), {v_next} ({power(v_next, m)}), but {exp} ({power(exp, m)}) expected. ')

def test_sqrt_seq():
    check_sqrt_seq(10, 2, 3.1622776601683793007424583265674300491809844970703125)

test_sqrt_seq()
