#!/usr/bin/env python3
def no_c(my_string):
    sinC = str(my_string)
    sinC = sinC.translate({ord("c"): None})
    sinC = sinC.translate({ord("C"): None})
    return sinC
