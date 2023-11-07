#!/usr/bin/python3
"""Converts a JSON string"""
import json


def from_json_string(my_str):
    """Converts a JSON string to Python data structure

    Arg:
        my_str: Json string
    """
    return json.loads(my_str)
