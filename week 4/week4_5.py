"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in Fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""


def main():
    x = input(
        'what would you like the temperature to be converted in press c for Centigrade and f for Fahrenheit: ').lower()
    while x != 'f' and x != "c":
        x = input('what would you like the temperature to be converted in press c for Centigrade and f for Fahrenheit: ').lower()

    temp = float(input('Input the temperature: '))
    print('The temperature is:', calculate(temp, x))


def calculate(temp, x):
    if x == 'f':
        a = temp * (9 / 5) + 32
        return a
    elif x == 'c':
        b = (temp - 32) * 5 / 9
        return b
main()
