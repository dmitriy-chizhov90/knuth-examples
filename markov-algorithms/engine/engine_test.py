#! python3

from engine.engine import Formula
from engine.engine import Schema

class TestFormula:
    def test_formulaAbBa(self):
        f = Formula('ab', 'ba')
        assert f.process('') == None
        assert f.process('ababab') == 'baabab'
        assert f.process('baabab') == 'babaab'
        assert f.process('babaab') == 'bbaaab'
        assert f.process('bbaaab') == 'bbaaba'
        assert f.process('bbaaba') == 'bbabaa'
        assert f.process('bbabaa') == 'bbbaaa'
        assert f.process('bbbaaa') == None

    def test_formulaEmpty(self):
        f = Formula('', 'ab')
        assert f.process('') == 'ab'
        assert f.process('ababab') == 'abababab'

    def test_formulaDelete(self):
        f = Formula('ab', '')
        assert f.process('') == None
        assert f.process('ababab') == 'abab'
        assert f.process('ab') == ''

class TestSchema:
    def test_emptyFormula(self):
        s = Schema([Formula('', '', True)])
        assert s.process('abra') == 'abra'

    def test_emptyEndless(self):
        s = Schema([Formula('', '')], mIterCnt = 1000)
        assert s.process('abra') == None

    def test_endless(self):
        s = Schema([Formula('', 'ab')], mWSize = 1000)
        assert s.process('abra') == None

    
    
