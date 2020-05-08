import pytest

from util.Calc import Calc


class Test_calc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        rest = self.calc.add(1, 2)
        assert 3 == rest

    def test_div_1(self):
        rest = self.calc.div(1, 2)
        assert 1 == rest


if __name__ == '__main__':
    pytest.main()
