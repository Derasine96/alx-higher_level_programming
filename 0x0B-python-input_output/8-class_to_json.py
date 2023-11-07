#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """A function that returns the dict. desc. with simple data structure
        list, dict, str, int and bool for JSON serialization of an object

    Arg:
        obj: instance of a class
    """
    if not isinstance(obj, type):
        serialized_dict = {}
        for name, value in vars(obj).items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_data[name] = value
        return serialized_data
