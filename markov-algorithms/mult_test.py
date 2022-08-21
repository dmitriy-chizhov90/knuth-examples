#! python3

from mult import mult

class TestMult:
    def test_multCorrect(self):
        assert mult(4, 5, True) == 20
        assert mult(1, 5) == 5
        assert mult(5, 1) == 5
        assert mult(5, 0) == 0
        assert mult(0, 5, True) == 0
        





        

