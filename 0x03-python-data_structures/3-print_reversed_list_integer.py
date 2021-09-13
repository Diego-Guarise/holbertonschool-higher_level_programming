#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenna = (len(my_list) - 1)
    for i in range(lenna, -1, -1):
        print("{}".format(my_list[i]))
