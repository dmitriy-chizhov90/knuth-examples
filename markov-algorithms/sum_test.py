#! python3

from sum import sum

class TestSum:
    def test_sumCorrect(self):
        assert sum(10, 5) == 15
        assert sum(0, 5) == 5
        assert sum(10, 0) == 10
        assert sum(0, 0) == 0
        assert sum(-10, -5) == -15
        assert sum(10, -5) == 5
        assert sum(-5, 10) == 5
        assert sum(-10, 5) == -5
        assert sum(5, -10) == -5


        

