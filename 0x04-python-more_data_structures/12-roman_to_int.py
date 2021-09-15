#!/usr/bin/python3
def roman_to_int(roman_string):
    romannum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return 0
    for i in roman_string:
        if i == romannum:
            print("hola")
        else:
            print("chau")
