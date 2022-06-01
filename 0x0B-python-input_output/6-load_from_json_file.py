#!/usr/bin/python3
"""Module 6-load_from_json_file.py"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        - filename: file to write into
    """

    with open(filename, 'r') as f:
        return json.load(f)
