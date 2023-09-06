#!/bin/bash/python3
""" Defines integer addition """


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns integer result

    Args:
        a (int or float): Fist number to add
        b (int or float, optional): Second number to add

    Returns:
        int: Sum of a and b

    Raises:
        TypeError: If a and b are not integers or floats
    """
    #  Check if a and b are integers/floats
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
