#!/usr/bin/python3
""" This function that prints a square with the character # """


def print_square(size):
    """ Prints a square using the '#' character
        Arguments:
        - size: is the size length of the square and
        must be an integer and not less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            print("#" * size)
