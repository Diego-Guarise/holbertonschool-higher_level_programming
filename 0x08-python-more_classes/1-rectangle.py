#!/usr/bin/python3
'''Defines a class Square'''


class Rectangle:

    '''Represents an empty square.'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        '''see wifth'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''See height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
