#!/usr/bin/python3
"""Write the first class Base"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file"""
        if list_objs is None or list_objs == []:
            a = "[]"
        else:
            a = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(a)
