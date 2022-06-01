#!/usr/bin/python3
"""Module 12-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def factorial(num):
    """Returns factorial of a real number
    Args:
        - num: real number
    """
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    p = []
    if n <= 0:
        return p

    if n == 1:
        p = [[1]]
        return p

    p = [[1], ]
    for i in range(1, int(n)):
        new_list = []
        comb = 0
        for j in range(0, i + 1):
            comb = factorial(i) / (factorial(j) * factorial(i - j))
            new_list.append(int(comb))
        p.append(new_list)
    return p
