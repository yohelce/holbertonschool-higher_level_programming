#!/usr/bin/python3
""" Module 101-add_attribute """


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it’s possible.
    Args:
        - obj: object to add the attribute to
        - attr: name of the attribute
        - value: value of the attribute to add
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
