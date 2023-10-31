#!/usr/bin/python3
"""
Defines a function to print name(s)
This module can be imported and used to print first and last name.
Last name can be excluded when calling the function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name or names

    Args:
        first_name (str): The first name (a string).
        last_name (str, optional): string Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not last_name:
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
