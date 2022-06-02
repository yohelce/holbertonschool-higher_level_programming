#!/usr/bin/python3
"""Module 10-student.py"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
           - attrs: attributes
        Returns: the dict representation of the instance.
        """

        if attrs is None:
            return self.__dict__

        my_dict = {}
        for i in attrs:
            if i in self.__dict__ and isinstance(i, str):
                my_dict[i] = self.__dict__.get(i)

        return my_dict
