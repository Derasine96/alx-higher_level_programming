#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = "{:d}".format(value)
        print(x)
        return True
    except (ValueError, TypeError):
        pass
    return False
