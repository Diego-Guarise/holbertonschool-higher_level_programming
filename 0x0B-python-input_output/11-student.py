#!/usr/bin/python3
"""Write a class Student that defines a student by:"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return"""
        lis = {}
        if type(attrs) is list:
            for i in attrs:
                try:
                    lis[i] = getattr(self, i)
                except Exception:
                    pass
            return lis
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for i in json.keys():
            setattr(self, i, json[i])
