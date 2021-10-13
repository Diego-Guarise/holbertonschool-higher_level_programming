#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle
"""import the rectangle"""


class Square(Rectangle):
    """define"""
    def __init__(self, size):
        """size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(self.size, self.size)
        self.__size = size

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def __str___(self):
        """print"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
