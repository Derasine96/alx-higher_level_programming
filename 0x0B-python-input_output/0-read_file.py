#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Prints a text file UTF8 to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
