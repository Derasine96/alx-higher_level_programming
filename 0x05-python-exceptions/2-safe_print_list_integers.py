#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in range(0, x):
        try:
            number = "{:d}".format(my_list[element])
            print(number, end='')
            count += 1
        except (ValueError, TypeError):
            continue
    print('')
    return count
