#!/usr/bin/python3
def print_arg(argv):
    if len(argv) == 0:
        print("0 arguments")
    elif len(argv) == 1:
        print("1 argument:")
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(len(argv)))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    print_arg(arguments)
