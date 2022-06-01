#!/usr/bin/python3
"""Module 2-append_write.py"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file UTF8
    and returns the number of characters added
    Args:
        - filename: name of the file
        - text: text appended into the file
    """

    with open(filename, mode='a+', encoding='utf-8') as f:
        return f.write(text)
