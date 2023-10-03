#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number % 10)
    if digit < 0:
        digit = -digit
    print("{}".format(digit))
    return digit
