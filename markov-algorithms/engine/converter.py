#! python3

# Кодирование/декодирование различных типов данных в строку.
class StringValue:
    """Encode/decode different data types to str"""
    s = None
    v = None

    def __init__(self, _str=None, _val=None):
        self.init(_str, _val)
        
    def init(self, _str, _val):
        if _str is not None and _val is not None:
            self.s = _str
            self.v = _val
            return
        if _str is not None:
            self.s = _str
            self.v = self.decode()
        if _val is not None:
            self.v = _val
            self.s = self.encode()
            
    def setStr(self, _str):
        self.init(_str, None)
        return self.v

    def setVal(self, _val):
        self.init(None, _val)
        return self.s
            
    def encode(self):
        self.s = None
        
        if self.v is None:
            return self.s

        if type(self.v) is int:
            if self.v < 0:
                self.s = '-' * (-self.v)
            else:
                self.s = '|' * self.v

        return self.s

    def decode(self):
        self.v = None

        if self.s is None:
            return self.v

        alphabet = sorted({c for c in self.s})

        if len(alphabet) == 0:
            self.v = 0
        elif len(alphabet) == 1:
            c = alphabet[0]
            if c == '|':
                self.v = len(self.s)
            elif c == '-':
                self.v = -len(self.s)

        return self.v
                
