#! python3

from engine.engine import Formula
from engine.computer import Computer


# 20/5
# ||||| ||||| ||||| ||||| * |||||  ; |*| -> *b; b| -> |b
#...
# ||||| ||||| ||||| * bbbbb ; b -> c
# ...
# ||||| ||||| ||||| * ccccc ; |*c -> |a*d; dc -> dd; |a -> a|
# ...
# a ||||| ||||| ||||| * dddddd ; d -> |
# ...
# a ||||| ||||| ||||| * |||||;
# ...
# aaaa * ||||| ; a*| -> a*
#...
# aaaa *; a* -> a; a-> |
# ...
# ||||



class DivisionComputer:
    def __init__(self, l, r, verbose=False):
        self.cmp = Computer(
            l,
            r,
            [
                Formula('dc', 'dd'),
                Formula('|a', 'a|'),
                Formula('d', '|'),
                
                Formula('|*|', '*b'),
                Formula('b|', '|b'),
                Formula('b', 'c'),
                Formula('*c', 'a*d'),
                Formula('|c', '|'),
                
                Formula('*|', '*'),
                # Деление на 0 -> inf                
                Formula('|*', '||*'), 
                Formula('*', ''),
                Formula('a', '|')],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def divide(a, b, verbose=False):
    return DivisionComputer(a, b, verbose).compute()


        
    
    
