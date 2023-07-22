#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args_list = argv[1:]

    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''), end='')
    if num_args == 0:
        print(" (or .) ")
    else:
        print()
        for i, arg in enumerate(args_list):
            print("{}: {}".format(i + 1, arg))
