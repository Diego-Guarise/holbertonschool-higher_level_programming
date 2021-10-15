#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file:"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    lista = load_from_json_file("add_item.json") + argv[1:]
    save_to_json_file(lista, "add_item.json")
except Exception:
    save_to_json_file(argv[1:], "add_item.json")
