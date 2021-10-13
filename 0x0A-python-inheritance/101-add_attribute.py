#!/usr/bin/python3
"""define"""


def add_attribute(*args):
    """add"""
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
