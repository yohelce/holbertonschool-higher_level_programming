#!/usr/bin/python3
""" Module text_indentation """


def text_indentation(text):
    """Prints a text with 2 new lines after each 
    of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delim = ".?:"
    for element in delim: 
        text = [each_line.strip() for each_line in text.split(element)]
        text = (element + "\n\n").join(text)
    print(f"{text}", end= '')
