#!/usr/bin/python3
def no_c(my_string):
    string = str(my_string)
    string = string.translate({ord("C"): None})
    string = string.translate({ord("c"): None})
    return string
