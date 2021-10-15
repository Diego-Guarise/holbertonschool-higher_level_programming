#!/usr/bin/python3
"""that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def append_after(filename="", search_string="", new_string=""):
    """append"""
    string = ""

    with open(filename) as a:

        for line in a:
            string += line

            if search_string in line:
                string += new_string

    with open(filename, "w") as f:
        f.write(string)
