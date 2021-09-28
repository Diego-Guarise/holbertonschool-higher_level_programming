#!/usr/bin/python3
class Square:
    def __init__(self, size = 0, position=(0, 0)):
            self.__size = size
            self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(c) != int or c < 0 for c in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
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
