#!/usr/bin/python3
"""Search and update a line in a text"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
        after each line containing a specific string

    Args:
        search_string: checks for specific string
        new_string: new string to insert
    """
    with open(filename. "r") as f:
        strings = f.readline()
    with open(filename, "w") as f:
        for string in strings:
            f.write(string)
            if search_string in string:
                f.write(new_string + '\n')
