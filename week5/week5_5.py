"""You wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!"""

import sys


def main():
    a = [float(temperature) for temperature in sys.argv[1:]]
    print('The maximum, minimum, and mean temperatures are:', calculate(a))


def calculate(a):
    max_temperature = max(a)
    min_temperature = min(a)
    mean_temperature = sum(a) / len(a)
    return max_temperature, min_temperature, mean_temperature


main()