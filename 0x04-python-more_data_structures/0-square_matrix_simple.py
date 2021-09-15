#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matri = []
    matr = []
    for i in matrix:
        matr = [x**2 for x in i]
        matri.append(matr)
    return matri
