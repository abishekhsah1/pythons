"""Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.
"""


def main():
    x = input("Enter the first word: ")
    y = input("Enter the second word: ")
    print("Either word:", either(x, y))
    print("Both words:", both(x, y))
    print("Not both:", notinboth(x, y))


def either(x, y):
    # union
    return sorted(list(set(x.lower()) | set(y.lower())))


def both(x, y):
    # intersection
    return sorted(list(set(x.lower()) & set(y.lower())))


def notinboth(x, y):
    # x-y and y-x
    return sorted(list(set(x.lower()) ^ set(y.lower())))


main()