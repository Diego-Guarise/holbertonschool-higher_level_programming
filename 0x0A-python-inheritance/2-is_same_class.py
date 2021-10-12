#!/usr/bin/python3


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    return isinstance(type(obj), a_class)
