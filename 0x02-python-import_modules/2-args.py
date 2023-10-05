#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    if len(arguments) == 1:
        print("{} arguments".format(0))
    elif len(arguments) == 2:
        print("{} argument:".format(1))
        for i, arg in enumerate(arguments[1:], 1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(len(arguments)))
        for i, arg in enumerate(arguments[1:], 1):
            print("{}: {}".format(i, arg))
