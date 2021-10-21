#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """contructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """attributes"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """return atrribute"""

        return self.__width

    @property
    def height(self):
        """return attribute"""

        return self.__height

    @property
    def x(self):
        """return attribute"""

        return self.__x

    @property
    def y(self):
        """return attribute"""

        return self.__y

    @width.setter
    def width(self, width):
        """set attribute"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """set attribute"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """set attribute"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """set attribute"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle"""

        for a in range(0, self.__height):
            for b in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        strr = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return strr

    def display(self):
        """print in stdout the Rectangle instance with the
        character # by taking care of x and y"""

        for f in range(0, self.__y):
            print()
        for c in range(0, self.__height):
            for d in range(0, self.__x):
                print(" ", end="")
            for e in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """changed attributes"""

        if args is not None and len(args) != 0:
            if len(args) >= 0:
                if type(args[0]) != int:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
