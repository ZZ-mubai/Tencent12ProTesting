#!/usr/bin/nev python
# *-* coding:utf-8 *-*
import pytest

def exc(x):
    if x == 0:
        raise ValueError("value not 0 or None")
    return 2 / x

def test_raises():
    with pytest.raises(ValueError, match="value not 0 or None"):
        print(exc(0))
    assert eval("1 + 2") == 3

