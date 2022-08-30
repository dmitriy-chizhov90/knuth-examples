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
                Formula('|c', 'c|'), # Проталкиваем палки в конец, а c -- в начало, чтобы завершить итерацию
                Formula('b|', '|b'), # Проталкиваем b в конец, а a -- в начало, чтобы можно было продолжать вычитание.
                Formula('|a', 'a|'),
                Formula('|*|', 'a*b'), # Вычитание
                Formula('a|', '|'), # Когда вычитание завершено убираем ненужные буквы
                Formula('|b', '|'),
                Formula('a*b', 'd*d'), # Числа равны. Прекращаем вычитание. Заменяем на d.
                Formula('db', 'dd'),
                Formula('ad', 'dd'),
                Formula('a', 'e'), # Числа не равны. Заменяем на c.
                Formula('b', 'c'),
                Formula('c', '|'), # Заменяем на палки и получаем новое вычитаемое.
                Formula('e', '|'),
                Formula('*d', '*'), # Убираем правое число и разделитель. Получаем ответ.!
                Formula('*', ''),
                Formula('d', '|')],
            verbose)

    def compute(self):
        p = f'{self.cmp.lhs.s}*{self.cmp.rhs.s}'
        return self.cmp.compute(p)

def euclides(a, b, verbose=False):
    return EuclidesComputer(a, b, verbose).compute()


        
    
    
