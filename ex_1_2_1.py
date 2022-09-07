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

for i in range(5):
    print(i+1, square_sum(i+1))
