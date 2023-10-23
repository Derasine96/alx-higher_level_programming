#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        number = "{:d}".format(value)
        print(number)
        return True
    except Exception as e:
        print('Exception: {}'.format(e))
        return False
