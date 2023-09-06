#!/bin/bash/python3
"""
Adds two integer or floats and returns integer
Floats are typcasted to int before addition
Raises: TypeError if either a or b are not float or int
"""

def add_integer(a, b=98):
    """
    Integer addition function
    """
    #  Check if a and b are integers/floats
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
