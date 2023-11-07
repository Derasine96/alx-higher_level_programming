#!/usr/bin/python3
"""Write JSON to a File"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write Json data to a file

    Args:
        my_obj: object to be written
        filename: file to write into
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
