#! python3

from diff import diff

class TestDiff:
    def test_diffCorrect(self):
        assert diff(10, 6) == 4
        assert diff(10, 10) == 0
        assert diff(4, 10) == -6
        assert diff(10, -6) == 16
        assert diff(-10, 6) == -4
        assert diff(10, 0) == 10
        assert diff(-10, 0) == -10
        assert diff(0, 10) == -10
        assert diff(0, -10) == 10
        




        

