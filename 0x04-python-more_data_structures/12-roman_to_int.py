#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if type(roman_string) is not str:
        return 0
    romannum = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = []
    suma = 0
    for letras in roman_string:
        for i, x in romannum.items():
            if letras == i:
                num.append(x)
    o = num
    p = 0
    for j in num:
        p = str(o[j+1])
        if j < p:
            print("casa")
            suma += j
        elif j > p:
            print("chau")
            suma += j
        else:
            print("gola")
            suma += j
    return suma
