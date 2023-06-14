#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in range(2):
        for j in range(2):
            new_matrix[i][j] = (new_matrix[i][j])**2
    return new_matrix
