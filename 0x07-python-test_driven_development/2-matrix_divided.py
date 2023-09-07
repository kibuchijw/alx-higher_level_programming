#!/usr/bin/python3
""" matrix division """

def matrix_divided(matrix, div):
    """
    Divide all matrix elements by specified number

    Args:
        matrix: Matrix to be divided
        div: Divisor

    Returns:
        list of lists: New matrix with divided numbers

    Raises:
        TypeError: If several conditions are not met
        ZeroDivisionError: If divisor is zero
    """

    # Check if matrix is a list of lists of floats and ints
    if not (
            isinstance(matrix, list) and
            all(
                isinstance(row, list) and
                all(isinstance(num, (int, float)) for num in row)
                for row in matrix
            )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows of matric have same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix
