#! python3

import math

def mult_26_1(n, af):
    p = 1
    for i in range(n + 1):
        intp = 1
        for j in range(i + 1):
            ai = af(i)
            aj = af(j)
            intp *= (ai * aj)
            print ('{_del}{_ai} * {_aj}'.format(_ai=ai, _aj=aj, _del=(' * ' if j != 0 else '')), end='')

        p *= intp
        print('')

    return p

def a1(i):
    return 3 + i

def mult_26_2(n, af):
    p = 1
    for i in range(n + 1):
        p *= af(i)

    return math.pow(p, n + 2)

print()
for n in range(5):
    print('{_n}, {_r}'.format(_n=n, _r=('pass' if mult_26_1(n, a1) == mult_26_2(n, a1) else 'fail')))

