#! python3

from engine.engine import Formula
from engine.computer import Computer


# 
# ||||| ||||| ||||| ||||| * |||||  ; |*| - > *


class DifferenceComputer:
    def __init__(self, l, r, verbose=False):
        self.cmp = Computer(
            l,
            r,
            [
                Formula('|*|', '*'),
                Formula('-*|', '*'),
                Formula('*|', '-'),
                Formula('*-', '|*'),
                Formula('-|', '--'),
                Formula('*', '')],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def diff(a, b, verbose=False):
    return DifferenceComputer(a, b, verbose).compute()


        
    
    
