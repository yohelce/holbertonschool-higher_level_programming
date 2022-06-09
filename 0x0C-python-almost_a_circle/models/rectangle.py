#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""


import json
from models.base import Base


class Rectangle(Base):
    """Class describing a rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):

        return self.__width

    @property
    def height(self):

        return self.__height

    @property
    def x(self):

        return self.__x

    @property
    def y(self):

        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(0, self.__y):
            print()
        for row in range(0, self.__height):
            for j in range(0, self.__x):
                print(" ", end='')
            for col in range(0, self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args is not None and len(args) > 0:
            if type(args[0]) is not int and args[0] is not None:
                raise TypeError("id must be an integer")
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                if arg == 1:
                    self.width = args[1]
                if arg == 2:
                    self.height = args[2]
                if arg == 3:
                    self.x = args[3]
                if arg == 4:
                    self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
