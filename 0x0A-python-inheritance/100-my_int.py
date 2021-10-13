#!/usr/bin/python3
"""create a class"""


class MyInt(int):
    """define"""
    def __init__(self, value):
        self.num = value

    def __eq__(self, other):
        """eq"""
        return self.num != other

    def __ne__(self, other):
        """ne"""
        return self.num == other
