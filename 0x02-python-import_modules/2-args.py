#!/usr/bin/python3
from sys import argv, exit
number = len(argv) - 1
if __name__ == "__main__":
    if number == 0:
        print("{} argument.".format(number))
        exit
    elif number == 1:
        print("{}: argument:".format(number))
        print("{}: {}".format(number, argv[1]))
        exit
    else:
        print("{} arguments:".format(number))
        i = 1
        while i <= number:
            print("{}: {}".format(i, argv[i]))
            i += 1
