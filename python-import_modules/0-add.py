#!/usr/bin/python3

a = 1
b = 2

if __name__ == "__main__":
    add_module = __import__('add_0')
    add = add_module.add
    print("{} + {} = {}".format(a, b, add(a, b)))
