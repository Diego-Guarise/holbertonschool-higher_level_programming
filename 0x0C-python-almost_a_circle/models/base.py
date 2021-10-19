#!/usr/bin/python3
"""Write the first class Base"""


class Base:
    """contructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        """set attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
