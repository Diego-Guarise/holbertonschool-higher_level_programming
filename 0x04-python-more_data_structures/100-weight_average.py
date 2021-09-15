#!/usr/bin/python3
def weight_average(my_list=[]):
    dividendo = 0
    divisor = 0
    if not my_list:
        return 0
    for i in my_list:
        dividendo += (i[0]*i[1])
        divisor += i[1]
    return dividendo/divisor
