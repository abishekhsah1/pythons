"""2. Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).
"""


def main():
    x = int(input("enter the number to find factor of : "))
    factors(x)


def factors(x):
    print ("the factor of x is:")
    for i in range(1, x + 1):
        # if it is perfectly divisible it is a factor otherwise it is not a factor
        if x % i == 0:
            print(i)


main()