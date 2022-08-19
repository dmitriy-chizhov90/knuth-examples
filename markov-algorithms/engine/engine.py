#! python3

# Формула для схемы алгоритма.
class Formula:
    """Formula for schema of algorithm"""
    left = ''
    right = ''
    isFinal = False

    def __init__(self, l, r, isFinal = False):
        self.left = l
        self.right = r
        self.isFinal = isFinal

    def process(self, p):
        i = p.find(self.left)
        l = len(self.left)
        if i < 0 and l > 0:
            return None
        return p[0:i] + self.right + p[(i+l):]


class Schema:
    """Algorithm schema"""
    formulas = []
    maxIterCount = 1000000
    maxWordSize = 1000000

    def __init__(self, fs, mIterCnt=1000000, mWSize=1000000, verbose=False):
        self.formulas = fs
        self.maxIterCount = mIterCnt
        self.maxWordSize = mWSize
        self.verbose = verbose

    def process(self, p):
        i = 0
        self.print(p, self.formulas)
        while True:
            i += 1
            if i > self.maxIterCount or len(p) > self.maxWordSize:
                # Считаем алгоритм бесконечным, т.е. неприменимым к данному слову
                self.print(f'Interupted: iterations {i}, word length {len(p)}')
                return None

            isApplied = False
            for f in self.formulas:
                r = f.process(p)
                if r is not None:
                    p = r
                    self.print(f'{f} applied: {p}')
                    if f.isFinal:
                        return p
                    # Формула применена, переходим к новой итерации
                    isApplied = True
                    break

            if not isApplied:
                # Не удалось применить ни одной формулы.
                # Алгоритм естественно завершается.
                self.print(f'Natural exit')
                return p
                
    def print(self, *args):
        if not self.verbose:
            return False
        print(args)
