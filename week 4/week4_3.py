"""Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur"""


def greetings():
    name = input("Enter your name: ")

    # first letter is uppercase and the rest is lowercase
    Given_name = name.capitalize()

    # Display the greeting with the formatted name
    print(f"Namaste, {Given_name}!")

# Call the greetings function
greetings()
