#!/usr/bin/python3
'''Defines a class Rectangle'''


class Rectangle:

    '''Represents an empty rectangle.'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        '''area'''
        return self.__width * self.__height

    def perimeter(self):
        '''perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

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

    def __str__(self):
        '''str'''
        strr = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for f in range(self.__height):
                for c in range(self.__width):
                    strr += str(self.print_symbol)
                strr += '\n'
            return strr[:-1]

    def __repr__(self):
        '''repr'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''del'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compare'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
