#!/usr/bin/nev python
# *-* coding:utf-8 *-*
# import sys
# print(sys.path)
import unittest

from python.calc import Cals



class TestCal(unittest.TestCase):

    def test_add1(self):
        self.calc = Cals()
        result = self.calc.add(1, 2)
        print(result)
        self.calc.add(3, result)

# unittest.main()