#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10
str = "Last digit of {} is {} and is ".format(number, digit)
if digit >= 6:
    print(str + "greater than 5")
elif digit == 0:
    print(str + "0")
else:
    print(str + "less than 6 and not 0")
