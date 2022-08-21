#! python3

from engine.engine import Formula
from engine.computer import Computer

class SumComputer:
    def __init__(self, l, r, verbose=False):
        self.cmp = Computer(
            l,
            r,
            [
                Formula('*', ''),
                Formula('|-', ''),
                Formula('-|', '')],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def sum(a, b, verbose=False):
    return SumComputer(a, b, verbose).compute()

        
    
    
