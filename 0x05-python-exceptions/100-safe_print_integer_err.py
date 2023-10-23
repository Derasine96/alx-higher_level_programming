#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        number = "{:d}".format(value)
        print(number)
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
