#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Function that prints a rectangle """

    def __init__(self, width=0, height=0):
        """Initializes the data"""

        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rectangle += '#'
            rectangle += '\n'
        return rectangle[:-1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return the Area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return the Perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
