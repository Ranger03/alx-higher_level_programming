#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(2):
        for j in range(2):
            matrix[i][j] = (matrix[i][j])**2
