#!/usr/bin/python3
number = len(argv)
if argv == 0:
    print("{} argument.".format(number))
else:
    print("{}: argument:".format(number))
i = 0
while i < number:
    print("{}: argv[i]".format(number))
