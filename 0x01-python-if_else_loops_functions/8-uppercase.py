#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            print("{0}".format(chr(ord(i) - 32)), end="")
        else:
            print("{0}".format(i), end="")
    print("")
