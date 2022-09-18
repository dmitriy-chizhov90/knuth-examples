#! python3

import math
import numpy
from tabulate import tabulate

# 8.

def power(n, m):
    p = 1
    for i in range(m):
        p *= n
    return p

def bin_search(u, m):
    print(f'%%%%%%%%%%%%%%%%%%%% {u} {m}')
    v = int(u)
    part = v

    while True:
        sq = power(v, m)
        sq_next = power(v+1, m)
        if sq <= u and u < sq_next:
            return v
        if part > 1:
            part = part // 2
        print(f'v {v}, part {part}')
        if u < sq:
            v -= part
        else:
            v += part
        

def print_bin_search(u, m):
    print(f'bin_search({u}, {m}) = {bin_search(u, m)}')

print_bin_search(4, 2)
print_bin_search(27, 3)
print_bin_search(64, 2)
print_bin_search(10, 2)
print_bin_search(2, 2)
print_bin_search(1.5, 2)
print_bin_search(1, 2)
print_bin_search(0.9, 2)


#def sqrt_seq(u, m):
    
