#!/usr/bin/python3
"""Check instance of class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class
    that inherited from a_class, otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) == a_class:
        return False
    return True
