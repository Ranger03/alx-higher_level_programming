#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(3):
        for j in range(3):
            matrix[i][j] = (matrix[i][j])**2
