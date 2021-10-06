#!/usr/bin/python3
"""
    Add two numbers (integer or float)
"""


def add_integer(a, b=98):
    """
    add
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
