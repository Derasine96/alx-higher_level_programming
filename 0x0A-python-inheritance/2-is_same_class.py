#!/usr/bin/python3
"""Check instance of class"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of class_type
        otherwise False."""
    return type(obj) == a_class
