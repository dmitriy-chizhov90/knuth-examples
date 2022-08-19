#! python3

from engine.converter import StringValue

class TestStringValue:
    def test_None(self):
        s = StringValue()
        assert s.s == None
        assert s.v == None

        s.encode()
        assert s.v == None

        s.decode()
        assert s.v == None

    def test_EncodeTrash(self):
        s = StringValue()
        assert s.setVal('trash') == None
        assert s.setVal(0.1234) == None
        assert s.setVal([1, 2, 3]) == None

    def test_DecodeTrash(self):
        s = StringValue()
        assert s.setStr('||||||||||-----') == None
        assert s.setStr('||||*||||') == None
        assert s.setStr('trash') == None
        assert s.setStr('*') == None

    def test_EncodeInt(self):
        s = StringValue()
        assert s.setVal(10) == '||||||||||'
        assert s.setVal(0) == ''
        assert s.setVal(-10) == '----------'

    def test_DecodeInt(self):
        s = StringValue()
        assert s.setStr('||||||||||') == 10
        assert s.setStr('') == 0
        assert s.setStr('----------') == -10

