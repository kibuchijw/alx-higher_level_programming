#!/usr/bin/python3
def magic_calculation(a, b):
    """Performs calculations based on the given bytecode instructions."""
    from magic_calculation_102 import add, sub  # Import functions from module

    if a < b:
        c = add(a, b)
        for i in range(4, 6):  # Iterate from 4 to 5 (inclusive)
            c = add(c, i)
        return c
    else:
        return sub(a, b)
