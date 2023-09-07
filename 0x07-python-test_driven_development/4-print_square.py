#!/usr/bin/python3
"""
Print square of '#' characters
Size of square to be passed to function
Raise various erros depending on input
"""


def print_square(size):
    """
    Print square with '#'
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size >= 0:
        raise TypeError("size must be an integer")
    # Check if size is >= 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for _ in range(size):
        print("#" * size)
