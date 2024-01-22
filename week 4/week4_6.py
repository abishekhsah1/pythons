"""Write a program that takes a centigrade temperature and displays the equivalent in
Fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format"""


def main():
    temp = input("Input the temperature in centigrade: ").strip().lower()
    temp = temp.removesuffix('c')
    temp = int(temp)
    print('The temperature is:', calculate(temp))


def calculate(temp):
    a = temp * (9 / 5) + 32
    a = str(a) + "c"
    return a


main()