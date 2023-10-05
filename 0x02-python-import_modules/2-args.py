#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    if len(arguments) == 1:
        print("0 arguments")
    elif len(arguments) == 2:
        print("1 argument:")
        print("1: {}".format(arguments[1]))
    else:
        print("{} arguments:".format(len(arguments) - 1))
        for i, arg in enumerate(arguments[1:], 1):
            print("{}: {}".format(i, arg))

