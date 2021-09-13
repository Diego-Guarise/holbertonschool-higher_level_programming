#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(len(i)):
            if x < (len(i) - 1):
                print("{:d}".format(i[x]), end=" ")
            elif x == (len(i) - 1):
                print("{:d}".format(i[x]), end="")
        print('')
