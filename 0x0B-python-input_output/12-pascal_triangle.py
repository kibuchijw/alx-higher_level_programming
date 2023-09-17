#!/usr/bin/python3
"""
Generate Pascal's triangle up to the nth row
:param n: Number of rows to generate in Pascal's triangle
:return: List of lists representing Pascal's triangle
"""


def pascal_triangle(n):
    """
    Function that returns Pascal's triangle
    """
    if n <= 0:
        return []
        #  Return empty list for n <= 0

    triangle = []
    #  Initialize empty list to store Pascal's triangle

    for i in range(n):
        row = []
        #  Initialize empty list for each row
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
                #  First and last elements of each row are always 1
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
