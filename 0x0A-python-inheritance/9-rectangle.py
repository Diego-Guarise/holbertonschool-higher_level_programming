#!/usr/bin/python3
"""BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Base por altura"""
        return (self.__width * self.__height)

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))