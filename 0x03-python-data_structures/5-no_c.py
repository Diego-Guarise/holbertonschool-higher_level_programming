#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        sinC = str(my_string)
        sinC = sinC.translate({ord("C"): None})
        sinC = sinC.translate({ord("c"): None})
        return sinC
