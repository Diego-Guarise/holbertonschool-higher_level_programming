#!/usr/bin/python3
"""
    Prints #
"""


def print_square(size):
    """
    print a square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
