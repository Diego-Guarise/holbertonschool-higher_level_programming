#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lista =[]
    for i in my_list:
        if i == search:
            lista.append(replace)
        else:
            lista.append(i)
    return lista
