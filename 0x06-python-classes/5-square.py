#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Initializes the data."""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints to stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#".format(), end="")
                print()
