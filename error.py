#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:37:45 2022

@author: david
"""


def function_inverse(x):
    if type(x) != float or int:
        raise TypeError("I can't handle things other than numbers")
    if x == 0:
        raise ZeroDivisionError("0 has no inverse")
    x = 1/x
    return x


def main():
    # assert 'as' == 'ast'  # AssertionError
    # a = 3/0  # ZeroDivisionError
    # b = float('a')  # ValueError
    try:
        ans = function_invers(1)  # NameError
    except NameError:
        print("Wrong function name")
    # from Blood_Calculator import BMI_Calculator
    # BMI_Calculator()  # ImportError
    finally:
        print("End")


if __name__ == "__main__":
    main()
