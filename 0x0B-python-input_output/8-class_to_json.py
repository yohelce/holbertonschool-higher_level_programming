#!/usr/bin/python3
"""Module 8-class_to_json.py"""


def class_to_json(obj):
    """Creates a dict description of obj
    Args:
        - obj: object to serialize
    Returns: dictionnary description of obj
    """

    return obj.__dict__
