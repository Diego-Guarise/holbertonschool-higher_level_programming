#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """creat"""
    with open(filename, "r") as a:
        return json.load(a)
