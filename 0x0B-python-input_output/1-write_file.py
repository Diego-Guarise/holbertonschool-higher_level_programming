#!/usr/bin/python3
"""write"""


def write_file(filename="", text=""):
    """In a file"""
    with open(filename, "w") as f:
        return f.write(text)
