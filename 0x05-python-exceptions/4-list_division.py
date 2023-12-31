#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for elements in range(list_length):
        if elements >= len(my_list_1) or elements >= len(my_list_2):
            print('out of range')
            my_list.append(0)
        else:
            try:
                result = my_list_1[elements] / my_list_2[elements]
            except ZeroDivisionError:
                result = 0
                print('division by 0')
            except TypeError:
                result = 0
                print('wrong type')
            except IndexError:
                print('out of range')
            finally:
                my_list.append(result)
    return my_list
