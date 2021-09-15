#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    my_list1 = list(map(lambda num: num * number, my_list))
    return my_list1
