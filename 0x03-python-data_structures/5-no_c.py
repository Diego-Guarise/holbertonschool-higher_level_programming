#!/usr/bin/python3
def no_c(my_string):
    new_string = str(my_string)
    new_string = new_string.translate({ord("C"): None})
    new_string = new_string.translate({ord("c"): None})
    return new_string
