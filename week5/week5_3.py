"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them"""

import sys


def main():
    a = sys.argv[1:]
    print('shortest is:', calc(a))


def calc(a):
    a.sort(key=len)
    return a[0]


main()