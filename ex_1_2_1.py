#! python3

import math

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

def formula_11_item(i):
    return math.pow(-1, i) * math.pow(2*i+1, 3) / (math.pow(2*i+1, 4) + 4)

def formula_11(n):
    s = 0
    for i in range(n + 1):
        s += formula_11_item(i)
    return s

for i in range(100):
    print(i, formula_11(i), formula_11_item(i))
