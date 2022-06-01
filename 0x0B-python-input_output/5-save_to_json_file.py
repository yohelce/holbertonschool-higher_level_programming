#!/usr/bin/python3
"""Module 5-save_to_json_file.py"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        - my_obj: object to write
        - filename: file to write into
    """

    with open(filename, mode='w+', encoding='utf-8') as f:
        json.dump(my_obj, f)
