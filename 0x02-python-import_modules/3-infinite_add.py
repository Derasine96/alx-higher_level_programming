#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    sum = 0
    for i in range(args):
        args = sys.argv[i + 1]
        sum += int(args)
    print("{}".format(sum))
