#!/usr/bin/nev python
# *-* coding:utf-8 *-*
from python.calc import Cals
import pytest
import yaml

class YamlData:
    def __init__(self,data_path):
        self.data_path = yaml.safe_load(open(data_path))

    def get_data(self, name):
        return self.data_path[name]

add = YamlData("./add_data.yaml")
div = YamlData("./div_data.yaml")

class TestCalc:
    def setup(self):
        self.calc = Cals()

    @pytest.mark.parametrize("test_case",add.get_data('case'))
    def test_add_1(self, test_case):
        result = self.calc.add(test_case['a'] ,test_case['b'])
        assert test_case['res'] == result

    @pytest.mark.parametrize("test_case",div.get_data('case'))
    def test_div(self, test_case):
        result = self.calc.div(test_case['a'], test_case['b'])
        # with pytest.raises(ValueError) as exc_info:
        #     self.calc.div(test_case['a'], test_case['b'])
        # assert exc_info.type is ValueError
        assert test_case['res'] == result

    # @pytest.mark.parametrize("a, b",[(10, 20)])
    # def test_add_1(self):
    #     result = self.calc.add(1 ,2)
    #     print(result)
    #     assert 3 == result
    #
    # def test_add_2(self):
    #     result = self.calc.add(1,1.1)
    #     print(result)
    #     assert 2.1 == result
    #
    # def test_add_3(self):
    #     result = self.calc.add(1.111111,1)
    #     print(result)
    #     assert 2.111111 == result
    #
    # def test_add_4(self):
    #     result = self.calc.add(1.111, 2.2)
    #     print(result)
    #     assert 3.311 == result
    #
    # def test_add_5(self):
    #     result = self.calc.add('a', 2.2)
    #     print(result)
    #     assert '错误类型' == result
    #
    # def test_add_6(self):
    #     result = self.calc.add(1.111, 'a')
    #     print(result)
    #     assert '错误类型' == result

    # @pytest.mark.parametrize("a, b",yaml.safe_load(open('./data.yaml')))
    # def test_div(self, a, b):
    #     self.calc = Cals()
    #     result = self.calc.div(2,2)
    #     assert 1 == result

if __name__ == '__main__':
    pytest.main(['-v','./test_pytest.py::TestCalc::test_div'])