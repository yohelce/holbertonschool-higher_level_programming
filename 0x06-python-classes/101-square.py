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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if \
           type(position) != tuple or \
           len(position) != 2 or type(position[0]) != int or \
           type(position[1]) != int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def __str__(self):
        """Str method for print from main module."""
        my_str = ""
        if self.__size == 0:
            return "\n"
        else:
            my_str += "\n" * self.__position[1]
            for row in range(0, self.__size):
                my_str += " " * self.__position[0]
                my_str += "#" * self.__size
                my_str += "\n"
            return my_str[:-1]

    def area(self):
        """Public instance method that returns area of a square"""
        return self.__size ** 2

    def my_print(self):
        """"Public instance method that prints a square with the character #"""
        if self.__size == 0:
            print()
        else:
            for blank in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                print(" " * self.__position[0], end="")
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
        if \
           type(value) != tuple or \
           len(value) != 2 or type(value[0]) != int or \
           type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
