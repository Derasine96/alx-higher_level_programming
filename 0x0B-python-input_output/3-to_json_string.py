#!/usr/bin/python3
"""Converts a Python string"""
import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string

    Arg:
        my_obj: Python object
    """
    return json.dumps(my_obj)
