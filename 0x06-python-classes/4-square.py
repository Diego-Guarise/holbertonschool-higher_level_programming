#!/usr/bin/python3
"""Represents a square.
Private instance attribute: size:
   - property def size(self)
   - property setter def size(self, value)
Instantiation with optional size.
Public instance method: def area(self).
"""


class Square:
    def __init__(self, size = 0):
        """Initializes the data."""
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
