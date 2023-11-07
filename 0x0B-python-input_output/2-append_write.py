#!/usr/bin/python3
"""Defines a text file-creating and writing function"""


def write_file(filename="", text=""):
    """Appends a string to a text file UTF8

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
