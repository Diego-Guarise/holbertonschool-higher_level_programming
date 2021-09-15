#!/usr/bin/python3
def roman_to_int(roman_string):
    romannum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = []
    suma = 0
    for letras in roman_string:
        for i, x in romannum.items():
            if letras == i:
                num.append(x)
    for j in num:
        if j < (j+1):
            suma += -j
        elif j > (j+1):
            suma += j
        else:
            suma += j
    return -suma
