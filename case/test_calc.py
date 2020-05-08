import pytest

from util.Calc import Calc


class Test_calc:
    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize("a,b,c",[(1,2,3),(2,3,4),(None,None,None),(-1,0,-1),(0.1,0.1,0.2),(0,0,0),(9223372036854775807,1,9223372036854775808)])
    def test_add_1(self,a,b,c):
        try:
            rest = self.calc.add(a, b)
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest
    @pytest.mark.parametrize("a,b,c",[(8,4,2),(-1,1,-1),(1,-1,-1),(0.1,0.5,0.2),(1,0,1),(None,None,None)])
    def test_div_1(self,a,b,c):
        try:
            rest = self.calc.div(a, b)
        except ZeroDivisionError:
            assert b == 0
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest


if __name__ == '__main__':
    pytest.main()
