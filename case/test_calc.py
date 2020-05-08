import pytest
from util.Calc import Calc


class test_calc:
    def test_add_1(self):
        self.calc = Calc()
        rest = self.calc.add(1, 2)
        assert 4 == rest

    def test_div_1(self):
        self.calc = Calc()
        rest = self.calc.div(1, 2)
        assert 2 == rest


if __name__ == '__main__':
    pytest.main()
