#!/usr/bin/python3
""" that returns a list of lists of integers
representing the Pascal’s triangle of """


def append_after(filename="", search_string="", new_string=""):
    """append"""
    i = ""

    with open(filename) as a:

        for line in a:
            i += line

            if search_string in line:
                i += new_string

    with open(filename, "w") as f:
        f.write(i)
