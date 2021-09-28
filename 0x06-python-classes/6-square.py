#!/usr/bin/python3
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """


class Square:
    """Initializes the data."""
    def __init__(self, size = 0, position=(0, 0)):
	self.__size = size
	self.__position = position

    def area(self):
        """Returns the current square area."""
	return self.__size * self.__size

    @property
    def position(self):
        """Retrieves the position."""
	return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
	if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(c) != int or c < 0 for c in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Sets the size to a value."""
	return self.__size

    @size.setter
    def size(self, value):
        """Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
	if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ".format(), end="")
                for x in range(self.__size):
                    print("#".format(), end="")
                print()
