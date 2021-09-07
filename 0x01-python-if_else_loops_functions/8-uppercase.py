#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            char = chr(ord(i) - 32)
        else:
            char = i
        print("{}".format(char), end="")
    print("")
