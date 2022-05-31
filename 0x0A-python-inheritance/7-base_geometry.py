#!/usr/bin/python3
"""Module 7-base_geometry.
Creates a BaseGeometry class.
"""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
