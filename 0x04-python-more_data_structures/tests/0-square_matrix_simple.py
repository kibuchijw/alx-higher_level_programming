#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = lambda x: x ** 2
    squared_matrix = list(map(lambda row: list(map(squared, row)), matrix))

    return squared_matrix

