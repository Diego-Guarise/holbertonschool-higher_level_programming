#!/usr/bin/python3
for i in range(0, 10):
    for x in range(i, 10):
        if i == x:
            continue
        if i == 10 & x == 8:
            break
        print("{}{}".format(i, x), end=", ")
print("89")
