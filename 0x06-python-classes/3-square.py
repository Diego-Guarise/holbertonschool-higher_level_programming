#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Initializes the data."""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size*self.__size
