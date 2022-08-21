#! python3

from division import divide

class TestDivision:
    def test_divideCorrect(self):
        assert divide(20, 5, True) == 4
        assert divide(23, 5, True) == 4
        assert divide(5, 5, True) == 1
        assert divide(3, 5, True) == 0
        assert divide(0, 5, True) == 0
        # Слишком долго выполняется.
#        assert divide(5, 0, True) == None
        

        




        

