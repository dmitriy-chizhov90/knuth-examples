#! python3

from engine.engine import Formula
from engine.computer import Computer


# 100/30
# ||||| ||||| ||||| ||||| * |||||  ;

# 100 30 10 0
# 100 70 40 30 20 10 0


class EuclidesComputer:
    def __init__(self, l, r, verbose=False):
        self.cmp = Computer(
            l,
            r,
            [
                Formula('|*', 'a*'),
                Formula('*|', '*b'),
                Formula('|a', 'aa'),
                Formula('b|', 'bb'),
                Formula('a*b', 'ab'),

                Formula('cb', 'ac'),
                Formula('cd', 'bc'),
                Formula('c', ''),
                
                Formula('abb', 'bab'),
                Formula('ab', 'd'),
                Formula('b', 'cb'),
                Formula('d', 'cd'),

                Formula('eaa', '|ea'),
                Formula('ea', '|'),
                Formula('a', 'ea')],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def euclides(a, b, verbose=False):
    return EuclidesComputer(a, b, verbose).compute()


        
    
    
