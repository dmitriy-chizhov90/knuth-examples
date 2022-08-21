#! python3

from engine.engine import Formula
from engine.engine import Schema
from engine.converter import StringValue

class Computer:
    def __init__(self, l, r, formulas, verbose):
        self.lhs = StringValue(_val=l)
        self.rhs = StringValue(_val=r)
        self.schema = Schema(formulas, verbose=verbose)

        self.result = None
        self.error = None
        
    def compute(self, p):
        rs = self.schema.process(p)
        
        self.result = StringValue(_str=rs).v
        return self.result


        
    
    
