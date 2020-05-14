import pytest

from util.Calc import Calc


class Test_calc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.second
    @pytest.mark.parametrize("a,b,c",
                             [(1, 2, 3), (2, 3, 5), (None, None, None), (-1, 0, -1), (0.1, 0.1, 0.2), (0, 0, 0),
                              (9223372036854775807, 1, 9223372036854775808)])
    def calc_add(self, a, b, c):
        try:
            rest = self.calc.add(a, b)
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest

    @pytest.mark.first
    @pytest.mark.parametrize("a,b,c",
                             [(8, 4, 2), (-1, 1, -1), (1, -1, -1), (0.1, 0.5, 0.2), (1, 0, 1), (None, None, None)])
    def calc_div(self, a, b, c):
        try:
            rest = self.calc.div(a, b)
        except ZeroDivisionError:
            assert b == 0
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest

    @pytest.mark.parametrize("a,b,c",
                             [(8, 4, 4), (-1, 1, -2), (1, -1, 2), (0.1, 0.5, -0.4), (1, 0, 1)])
    def calc_sub(self, a, b, c):
        rest = self.calc.sub(a, b)
        assert c == rest

    @pytest.mark.parametrize("a,b,c",
                             [(8, 4, 32), (-1, 1, -1), (1, -1, -1), (0.1, 0.5, 0.05), (1, 0, 0)])
    def calc_mul(self, a, b, c):
        rest = self.calc.mul(a, b)
        assert c == rest


if __name__ == '__main__':
    pytest.main()
