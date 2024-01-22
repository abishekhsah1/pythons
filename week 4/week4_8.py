"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value"""


def main():
    a = []
    while True:
        temperature = input("Enter temperature list (at least 1) : press Enter to finish: ")
        if not temperature:
            break
        else:
            a.append(float(temperature))
    print('The maximum, minimum, and mean temperatures are:', calculate(a))


def calculate(a):
    print(a)
    max_temperature = max(a)
    min_temperature = min(a)
    mean_temperature = sum(a) / len(a)
    return max_temperature, min_temperature, mean_temperature


main()