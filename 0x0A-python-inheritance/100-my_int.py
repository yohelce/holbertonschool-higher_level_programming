#!/usr/bin/python3
""" Module 100-my_int"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behavior of != and ==.
    """

    def __eq__(self, value):
        """Equality becomes inequality"""

        return super().__ne__(value)

    def __ne__(self, value):
        """"Inequality becomes equality."""

        return super().__eq__(value)
