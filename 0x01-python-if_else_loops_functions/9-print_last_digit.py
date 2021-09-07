#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    i = number % 10
    print("{}".format(i), end="")
    return i
