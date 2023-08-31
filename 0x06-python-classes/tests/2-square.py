#!/usr/bin/python3
""" Define class Square """

class Square:
    """
    This class represents a square

    Attributes:
        __size (int): Size of square(private).
    """
    def __init__(self, size=0):
        """
        Initializes square instance

        Args:
            size(int, optional): Size of the square, default 0

            Raises:
                TypeError: If size if not an integer
                ValueError: If size if less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
