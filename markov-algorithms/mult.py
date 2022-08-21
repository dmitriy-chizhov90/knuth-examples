#! python3

from engine.engine import Formula
from engine.computer import Computer


# 4*5
# ||||*|||||   ; |* -> *a
# |||*a|||||   ; a| -> b|a
# |||*b|a||||
# |||*b|b|a|||
# |||*b|b|b|a||
# |||*b|b|b|b|a|
# |||*b|b|b|b|b|a ; a -> 
# |||*b|b|b|b|b|  ; b| -> |b
# |||*|bb|b|b|b|
# |||*|b|bb|b|b|
# ...
# |||*|||||bbbbb
# ...
# *|||||bbbbb bbbbb bbbbb bbbbb ; *| -> *
...
# * bbbbb bbbbb bbbbb bbbbb ; * ->
# bbbbb bbbbb bbbbb bbbbb       ; b -> c
# ccccc ccccc ccccc ccccc       ; c -> |
# ||||| ||||| ||||| |||||
# 

class MultComputer:
    def __init__(self, l, r, verbose=False):
        self.cmp = Computer(
            l,
            r,
            [
                Formula('a|', 'b|a'),
                Formula('a', ''),
                Formula('b|', '|b'),
                Formula('|*', '*a'),
                Formula('*|', '*'),
                Formula('*', ''),
                Formula('b', 'c'),
                Formula('c', '|') ],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def mult(a, b, verbose=False):
    return MultComputer(a, b, verbose).compute()


        
    
    
