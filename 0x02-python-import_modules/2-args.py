#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    number = len(argv) - 1
    if number == 0:
        print("{} arguments.".format(number))
    elif number == 1:
        print("{}: argument:".format(number))
        print("{}: {}".format(number, argv[1]))
    else:
        print("{} arguments:".format(number))
        i = 1
        while i <= number:
            print("{}: {}".format(i, argv[i]))
            i += 1
