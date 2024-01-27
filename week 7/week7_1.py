"""Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']."""


def main():
    x = input("Enter the string: ")
    print("The unique sorted characters are", sor(x))


a = []


def sor(x):
    for i in x:
        if i not in a:
            a.append(i)
    a.sort()
    return a


main()