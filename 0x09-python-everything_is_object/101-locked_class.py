#!/usr/bin/python3
"""clae"""


class LockedClass:
    """previene que el usuario cree una instancia"""
    __slots__ = ["first_name"]
