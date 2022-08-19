#! python3

from engine.engine import Formula
from engine.engine import Schema
from engine.converter import StringValue

class SumComputer:
    def __init__(self, l, r, verbose=False):
        self.lhs = StringValue(_val=l)
        self.rhs = StringValue(_val=r)

        self.result = None
        self.error = None
        
        self.schema = Schema([
            Formula('*', ''),
            Formula('|-', ''),
            Formula('-|', ''),
        ], verbose=verbose)

    def compute(self):
        p = f'{self.lhs.s}*{self.rhs.s}'
        rs = self.schema.process(p)
        
        self.result = StringValue(_str=rs).v
        return self.result

def sum(a, b, verbose=False):
    return SumComputer(a, b, verbose).compute()

        
    
    
