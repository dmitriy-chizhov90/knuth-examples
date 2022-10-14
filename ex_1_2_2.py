#! python3

import math
import numpy as np
import matplotlib.pyplot as plt
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

def print_bits_count():
    numbers = [randrange(1000000) for i in range(100)]
    numbers = sorted(numbers + [1, 9, 10, 11, 99, 100, 101, 999, 1000, 1001])

    for n in numbers:
        bits = bits_count(n)
        upper = int(math.pow(2, bits))
        lower = int(math.pow(2, bits-1))
        print(f'{n}: {digits_count(n)} {bits}, [{lower}; {upper}]')

# 23.

def drawPlot(d, vlines=[], hlines=[], xtext=[], ytext=[], dots=[]):
    plt.margins(x=0, y=0)

    for l in vlines:
        plt.axvline(x = l, color = '#000000', alpha=0.1)

    for l in hlines:
        plt.axhline(y = l, color = '#000000', alpha=0.1)

    for x,txt in xtext:
        plt.text(x, -0.1, txt, va='top', ha='center')
    for y,txt in ytext:
        plt.text(-0.1, y, txt, va='center', ha='right')

    d()

    for x,y in dots:
        plt.plot(x,y,'ro')

    plt.legend()
    plt.show()

def stretch_along_y(i, k1, k2, t0,shift=None):
    shift = t0 if shift is None else shift
    return ((k1-t0)*(i-shift)/(k2-t0))+t0
    
def printHiper():
    x, y = 4., 25.
    xy = x*y
    t0 = 1.
    _y = xy-y
    _x = xy-x

    hiper = np.vectorize(lambda i: 1./i)
    hiper_div_x = np.vectorize(lambda i: 1./i/x)
    hiper_str_x = np.vectorize(lambda i: 1./stretch_along_y(i,y,_x+t0,t0,x)/x)
    hiper_div_y = np.vectorize(lambda i: 1./i/y)
    hiper_str_y = np.vectorize(lambda i: 1./stretch_along_y(i,x,_y+t0,t0,y)/y)
    ln = np.vectorize(lambda i: math.log(i))
    ln_div_x = np.vectorize(lambda i: math.log(i)/x)
    ln_str_x = np.vectorize(lambda i: math.log(stretch_along_y(i,y,xy,t0)))
    ln_div_y = np.vectorize(lambda i: math.log(i)/y)
    ln_str_y = np.vectorize(lambda i: math.log(stretch_along_y(i,x,xy,t0)))

    step = 0.001
    i_y = np.arange(t0, y+step, step)
    i_x = np.arange(t0, x+step, step)
    i_xy = np.arange(t0, xy+step, step)
    i_76 = np.arange(t0, _y+t0+step, step) #[1..76]
    i_97 = np.arange(t0, _x+t0+step, step) #[1..97]
    i_25 = np.arange(y, xy+step, step) #[25..100]
    i_4 = np.arange(x, xy+step, step) #[4..100]
    i_all = np.arange(step, xy+step, step)

    hiper_str = r'$\frac{1}{i}$'
    ln_str = r'$\ln{i}$'
    ln_div_x_str = r'$\frac{\ln{i}}{x}$'
    ln_div_y_str = r'$\frac{\ln{i}}{y}$'
    ln_str_x_str = r'$\ln{\frac{y-t_0}{xy-t_0}(i-t_0)+t_0}$'
    ln_str_y_str = r'$\ln{\frac{x-t_0}{xy-t_0}(i-t_0)+t_0}$'
    s_y_str = r'$S [1..y] \frac{1}{i}$'
    s_x_str = r'$S [1..x] \frac{1}{i}$'
    s_y_div_x_str = r'$S [1..y] \frac{1}{x i}$'
    s_x_div_y_str = r'$S [1..x] \frac{1}{y i}$'
    hiper_str_x_str = r'$S [x..xy] \frac{1}{x (\frac{i-x}{x}+t_0)}$'
    hiper_str_y_str = r'$S [y..xy] \frac{1}{y (\frac{i-y}{y}+t_0)}$'
    ln_sum_str=r'$\ln{(\frac{x-t_0}{xy-t_0}(i-t_0)+t_0)}+\ln{(\frac{y-t_0}{xy-t_0}(i-t_0)+t_0)}$'
    
    def drHiper(): plt.plot(i_xy, hiper(i_xy), 'b-', label=hiper_str)
    def drLn(i=i_xy): plt.plot(i, ln(i), 'r-', label=ln_str)
    def drLnDivX(): plt.plot(i_y, ln_div_x(i_y), 'm-', label=ln_div_x_str)
    def drLnDivY(): plt.plot(i_x, ln_div_y(i_x), 'c-', label=ln_div_y_str)
    def drLnStrX(): plt.plot(i_xy, ln_str_x(i_xy), 'c-', label=ln_str_x_str)
    def drLnStrY(): plt.plot(i_xy, ln_str_y(i_xy), 'm-', label=ln_str_y_str)
    def drHiperY(c='c'): plt.fill_between(i_y, hiper(i_y), color=c, label=s_y_str)
    def drHiperX(c='m'): plt.fill_between(i_x, hiper(i_x), color=c, label=s_x_str)
    def drHiperStrX(): plt.fill_between(i_4,hiper_str_x(i_4),color='c',label=hiper_str_x_str)
    def drHiperStrY(): plt.fill_between(i_25,hiper_str_y(i_25),color='m',label=hiper_str_y_str)
    def drHiperDivX(): plt.fill_between(i_y, hiper_div_x(i_y),color='m',label=s_y_div_x_str)
    def drHiperDivY(): plt.fill_between(i_x, hiper_div_y(i_x),color='c',label=s_x_div_y_str)
    def drLnSum(): plt.plot(i_xy,ln_str_x(i_xy)+ln_str_y(i_xy),'r--',label=ln_sum_str)

    # Гипербола и логарифм
    drawPlot(
        lambda: (drHiper(),drLn(),drHiperY(),drHiperX()),
        vlines=[x,y],
        hlines=[math.log(x),math.log(y),math.log(xy)],
        xtext=[(x,str((int(x)))),(y,str(int(y)))],
        ytext=[
            (math.log(x),str(r'$\ln{x}$')),
            (math.log(y),r'$\ln{y}$'),
            (math.log(xy),r'$\ln{xy}$')],
        dots=[(x,math.log(x)),(y,math.log(y)),(xy,math.log(xy))]
    )

    # Логарифм x'
    drawPlot(
        lambda:(drHiper(),drHiperX('r'),drHiperDivY(),drHiperStrY()),
        vlines=[x],
        hlines=[math.log(x)/y],
        xtext=[(x,str(int(x))), (y,str(int(y)))],
        ytext=[(math.log(x)/y,r'$\frac{\ln{x}}{y}$')]
    )

    # Логарифм y'
    drawPlot(
        lambda:(drHiper(),drHiperStrX(), drHiperDivX()),
        vlines=[y],
        hlines=[math.log(y)/x],
        xtext=[(x,str(int(x))), (y,str(int(y)))],
        ytext=[(math.log(y)/x,r'$\frac{\ln{y}}{x}$')]
    )
    
    # Логарифм x*y
    drawPlot(
        lambda:(drLn(),drLnStrX(),drLnStrY(),drLnSum()),
        vlines=[x,y],
        hlines=[math.log(x), math.log(y)],
        xtext=[(x,str(int(x))),(y,str(int(y)))],
        ytext=[
            (math.log(x),r'$\ln{x}$'),
            (math.log(y),r'$\ln{y}$'),
        ],
        dots=[(x,math.log(x)),(y,math.log(y)),(xy,math.log(xy))]
    )
        
# printHiper()

# 24. Вычисление логарифма по основанию 10 log_{10}{n}.
# Вычисление целой части логарифма
def logn_floor(x, base):
    n=0
    bound=1.
    while True:
        if x >= (bound*base):
            bound *= base
            n += 1
        elif x < bound:
            bound /= base
            n -= 1
        else:
            return n

def logn(x, base):
    e = 10
    n = logn_floor(x, base)

    x_prev = x/math.pow(base,n)
    b = []
    divisor = math.pow(2,e)
    nominator = 0
    power = 1
    
    for i in range(e):
        x_prev=x_prev*x_prev
        r=0
        if x_prev >= base:
            r=1
            x_prev /= base
        b.append(str(r))
        power *= 2
        k = divisor/power
        nominator += r*k
    
    return n, n+nominator/divisor, ''.join(b)

def print_log_table(base):
    headers = ['x', 'floor(log{x})', 'log{x}', 'digits', 'check', 'eps(%)']
    table = []
    fx = lambda i: i/100
    for i in range(1,2001):
        x=fx(i)
        v_floor, v, digits = logn(x, base)
        check = math.pow(base,v)
        eps = abs(check-x)/x*100
        table.append([x,v_floor,v,digits,check,eps])

    print(tabulate(table, headers, tablefmt='orgtbl'))

def print_log_tables():
    #print_log_table(10)
    print_log_table(2)

# 25. y = log_{base}{x}
def rshift(x, n=1):
    r = x
    for i in range(n):
        r/=2
    return r

def log_compute(x, base):
    if x < 1 or x >= 2:
        raise Exception(f"x={x}, expected 1 <= x < 2")
    verbose=True
    if verbose: print(f'x: {x}, base: {base}')
    y=0;z=rshift(x);k=1
    if verbose: print(f'y=0;z=x>>1;k=1 // y: {y}, z: {z}, k: {k}')
    while x>1:
        if verbose: print(f'while x({x})>1:')
        while x-z < 1:
            if verbose: print(f'    while x({x})-z({z}) ({x-z}) < 1:')
            z=rshift(z); k+=1
            if verbose: print(f'        z >>= 1 ({z}); k+=1 ({k})')
        if verbose: print(f'    while x({x})-z({z}) ({x-z}) < 1: break')
        x-=z; z=rshift(x,k); kp2=math.pow(2,k)
        if verbose: print(f'    x-=z ({x}); z=int(x)>>k ({z}); kp2=math.pow(2,k) ({kp2})')
        y+=math.log(kp2/(kp2-1), base)
        if verbose: print(f'    y+=math.log(kp2/(kp2-1), base) ({y})')
    if verbose: print(f'while x({x})>1: break')
    return y

def print_log_table_25(base):
    headers = ['x', 'log{x}', 'check', 'eps(%)']
    table = []
    #for i in range(1,101):
    i=1.5
    if True:
        x=i
        y = log_compute(x, base)
        check = math.log(x, base)
        print(x,y,check)
        eps = 0 if (check==0 and y==0) else (abs(check-y)/check*100)
        table.append([x,y,check,eps])

    print(tabulate(table, headers, tablefmt='orgtbl'))

#print_log_table_25(10)

# 29.

def draw_logarithms_b():
    t0 = 1.
    x=100

    ln = np.vectorize(lambda i, b: math.log(i, b))
    lnb = np.vectorize(lambda i, b: b*math.log(i, b))
    step = 0.001
    i_x = np.arange(t0, x+step, step)

    ln_str = lambda b: r'$ log_{' + str(b) + r'}(x)$'
    lnb_str = lambda b: str(b) + r'$ log_{' + str(b) + r'}(x)$'
    
    def drLn(b): plt.plot(i_x, ln(i_x, b), 'r-', label=ln_str(b), linewidth=b*2)
    def drLnb(b): plt.plot(i_x, lnb(i_x, b), 'b-', label=lnb_str(b), linewidth=b*2)
    
    drawPlot(
        lambda: (drLn(1.5), drLnb(1.5), drLn(2), drLnb(2), drLn(math.e), drLnb(math.e), drLn(3), drLnb(3), drLn(5), drLnb(5)),
        vlines=[],
        hlines=[],
        xtext=[],
        ytext=[],
        dots=[]
    )


    
draw_logarithms_b()
