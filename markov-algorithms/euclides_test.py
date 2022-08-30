#! python3

from euclides import euclides

class TestMult:
    def test_euclidesCorrect(self):
        assert euclides(6, 4, True) == 2
        assert euclides(4, 6, True) == 2
        assert euclides(4, 4, True) == 4
        assert euclides(1, 1, True) == 1
        assert euclides(17, 13, True) == 1
        assert euclides(9, 6, True) == 3
        assert euclides(42, 9, True) == 3
        assert euclides(51, 42, True) == 3
        assert euclides(348, 51, True) == 3
        assert euclides(51, 348, True) == 3
        
        

        





        

