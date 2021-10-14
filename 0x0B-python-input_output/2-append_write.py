#!/usr/bin/python3
"""write"""


def append_write(filename="", text=""):
    """In a file"""
    with open(filename, "a") as f:
        return f.write(text)
