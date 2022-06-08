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

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute"""

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        self.__y = value
