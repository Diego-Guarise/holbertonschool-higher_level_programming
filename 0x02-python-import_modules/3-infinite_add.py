#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    number = len(argv) - 1
    if number == 0:
        print("{}".format(number))
    else:
        i = 1
        result = 0
        while i <= number:
            result += int(argv[i])
            i += 1
        print("{}".format(result))
