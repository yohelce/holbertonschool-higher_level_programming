#!/usr/bin/python3
"""Class Square"""


class Square:
    """Represents a square.
    "Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data defining size and position of square"""
        self.__size = size
        self.__position = position

    def area(self):
        """Public instance method that returns area of a square"""
        return self.__size ** 2

    def my_print(self):
        """"Public instance method that prints a square with the character #"""
        if self.__position and self.__position[1] > 0:
            print("\n" * self.__position[1], end='')
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.value = value

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
