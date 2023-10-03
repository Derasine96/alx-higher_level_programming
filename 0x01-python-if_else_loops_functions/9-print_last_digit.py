#!/usr/bin/bash
def print_last_digit(number):
    for last_digit in number:
        digit = abs(last_digit % 10)
    print("{}".format(digit))
