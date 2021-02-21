#!/usr/bin/nev python
# *-* coding:utf-8 *-*
import pytest
# 计算器Calc测试用例补全（add,div），根据 等价类划分去编写自动化的测试用例
class Cals:

    def add(self, a, b):
        try:
            return a + b
        except:
            return "TypeError"
        # if isinstance(a,int) and isinstance(b,int):
        #     return a + b
        # elif isinstance(a, float) and isinstance(b,int):
        #     return a + b
        # elif isinstance(a,int) and isinstance(b,float):
        #     return a + b
        # elif isinstance(a,float) and isinstance(b, float):
        #     return a + b
        # elif isinstance(a,float) and isinstance(b, float):
        #     return a + b
        # else:
        #     return "错误类型"


    def div(self, a, b):
        # return a / b
        # if b == 0:
        #     raise ValueError("value not 0")
        # return a / b
        try:
            return a / b
        except :
            return "TypeError"
        # # except ValueError:
        # #     print("输入的需要是数值型整数")
        # except:
        #     return "这是一个通用异常"

        # try:
        #     if isinstance(a,int) and isinstance(b,int):
        #         return a / b
        #     elif isinstance(a, float) and isinstance(b,int):
        #         return a / b
        #     elif isinstance(a,int) and isinstance(b,float):
        #         return a / b
        #     elif isinstance(a,float) and isinstance(b, float):
        #         return a / b
        #     elif isinstance(a,float) and isinstance(b, float):
        #         return a / b
        #     else:
        #         return "错误类型"
        # except:
        #     print("ZeroDivisionError: division by zero")






if __name__ == '__main__':
    num = Cals()
    # print(num.add(0, 2))
    # num.input_password()
    print(num.div('1',0))