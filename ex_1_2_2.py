#! python3

import math
import numpy as np
from tabulate import tabulate
from random import randrange

# 8.

def power(n, u, m):
    p = 1
    for i in range(m):
        p *= n
    return p

def sqrt_cmp(u, m, sq, sq_next):
    if u < sq:
        return -1
    if u >= sq_next:
        return 1
    return 0

def bin_search(u, m, f_check, f_cmp):
    v = int(u)
    part = v

    while True:
        sq = f_check(v, u, m)
        sq_next = f_check(v+1, u, m)
        rel = f_cmp(u, m, sq, sq_next)
        if rel == 0:
            return v
        if part > 1:
            part = part // 2
        if rel == -1:
            v -= part
        else:
            v += part

def bin_search_sqrt(u, m):
    return bin_search(u, m, power, sqrt_cmp)
        
def check_bin_search(u, m, exp):
    v = bin_search_sqrt(u, m)
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

def seq_search(u, m, f_check, f_cmp, k=100):
    n = bin_search(u, m, f_check, f_cmp)
    c = 1
    v, v_real, v_real_next = n, n, n
    sq = f_check(v, u, m)
    digits = []

    for i in range(k):
        c *= 10
        v *= 10
        for i in range(10):
           v_next  = v + 1
           v_real_next = v_next / c
           sq_next = f_check(v_real_next, u, m)
           if f_cmp(u, m, sq, sq_next) == 0:
               digits.append(str(i))
               break
           sq, v, v_real = sq_next, v_next, v_real_next

    digits = chop_0(digits)
    print(v_real, v_real_next, f'{n}.{"".join(digits)}')
    return v_real, v_real_next

def sqrt_seq(u, m):
    return seq_search(u, m, power, sqrt_cmp)

def check_sqrt_seq(u, m, exp):
    v, v_next = sqrt_seq(u, m)
    if v <= exp and exp < v_next:
        print(f'sqrt_seq({u}, {m}) = {v}, {v_next} ({power(v, m)}, {power(v_next, m)})')
    else:
        print(f'FAIL! sqrt_seq({u}, {m}) = {v} ({power(v, m)}), {v_next} ({power(v_next, m)}), but {exp} ({power(exp, m)}) expected. ')

def test_sqrt_seq():
    check_sqrt_seq(10, 2, 3.1622776601683793007424583265674300491809844970703125)

#test_sqrt_seq()

# 11.

def power2(v, u, m):
    return math.pow(u, v)

def log_cmp(b, c, sq, sq_next):
    if c < sq:
        return -1
    if c >= sq_next:
        return 1
    return 0

def log_seq(b, c, k):
    return seq_search(b, c, power2, log_cmp, k)

def print_log_10_2():
    for i in range(20):
        p, p_next = log_seq(10, 2, i)
        print(math.pow(10, p), math.pow(10, p_next))

    x = math.log10(2)
    bx = math.pow(10, x)
    xl = 0.3010299956639812
    xu = 0.30102999566398129
    bxl = math.pow(10, xl)
    bxu = math.pow(10, xu)
    print(f'x: {x}, bx: {bx}, bxl: {bxl}, bxu: {bxu}')

#print_log_10_2()

# 19. Оценка объема памяти для числа.
def digits_count(n):
    return int(math.floor(math.log10(n) + 1))

def bits_count(n):
    d = digits_count(n)
    return math.ceil(d*10/3)

numbers = [randrange(1000000) for i in range(100)]
numbers = sorted(numbers + [1, 9, 10, 11, 99, 100, 101, 999, 1000, 1001])

for n in numbers:
    bits = bits_count(n)
    upper = int(math.pow(2, bits))
    lower = int(math.pow(2, bits-1))
    print(f'{n}: {digits_count(n)} {bits}, [{lower}; {upper}]')


