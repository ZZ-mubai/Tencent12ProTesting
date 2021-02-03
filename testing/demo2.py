#!/usr/bin/nev python
# *-* coding:utf-8 *-*


__all__ = ["hello"] # 提供对外开放有哪些内容（方法、列表、变量、类等，并且在使用`from testing.demo2 import Demo2`才会生效 ）

hello = 'hello demo2'

def f():
    print("demo2.py  f()")

class Demo2:
    pass