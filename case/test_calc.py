import pytest
from util.Calc import Calc
class test_calc:
    def test_add_1(self):
        self.calc = Calc()
        rest = self.calc.add(1,2)
        print(rest)
        assert 4 == rest