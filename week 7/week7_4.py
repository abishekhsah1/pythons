"""one approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is trick"""


def frequency_analysis(message):
    message = message.lower()
    message = message.replace(" ", "")#space is removed
    letter_counts = {}
    for letter in message:
        if letter in letter_counts:
            letter_counts[letter] += 1# if already in message add 1
        else:
            letter_counts[letter] = 1# if not only 1
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_letter_counts[:6]

message = input("Enter your message to encrypt: ")
result = frequency_analysis(message)
for letter, count in result:
    print(f"{letter}: {count}")