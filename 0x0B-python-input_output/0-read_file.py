#!/usr/bin/python3
""" Module 0-read_file"""


def read_file(filename=""):
    """ Reads a text file UTF8 and prints it to stdout
    Args:
        - filename: name of the file
    """

    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end='')
