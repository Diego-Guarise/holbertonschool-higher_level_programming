#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lista = []
    for i, j in a_dictionary.items():
        if j == value:
            lista.append(i)
    for x in lista:
        del a_dictionary[x]
    return a_dictionary
