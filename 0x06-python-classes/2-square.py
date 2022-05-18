#!/usr/bin/python3
"""Empty Class Square"""


class Square:
    """Represents a square.
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """

    def __init__(self, size=0):
        """Initialize the data defining size of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
