#!/usr/bin/python3
"""
Inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename.
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
