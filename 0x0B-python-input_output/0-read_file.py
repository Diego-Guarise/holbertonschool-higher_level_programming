#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """RTFM"""
    with open(filename) as f:
        print(f.read(), end="")

    f.closed
