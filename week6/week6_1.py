"""1. Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!
"""
def main():
    x = int(input("enter a  number: "))
    print("binary version of the number is", binary(x))


def binary(x):
    return bin(x)


main()
