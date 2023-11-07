#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”

    Arg:
        filename: file to create
    """
    with open(filename, "r") as json_file:
        object_file = json.load(json_file)
    return object_file
