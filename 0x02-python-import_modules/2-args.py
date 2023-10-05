#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("0 arguments")
    elif len(arguments) == 1:
        print("1 argument:")
        for i, arg in enumerate(arguments, 1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(len(arguments)))
        for i, arg in enumerate(arguments, 1):
            print("{}: {}".format(i, arg))
