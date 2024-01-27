"""Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you)."""

countries = {'nepal': 'kathmandu', 'japan': 'tokyo', 'germany': 'berlin', 'russia': 'moscow',
                  'usa': 'washington dc'}

while True:
    country = input("Enter a country ot type exit: ").lower().strip()

    if country.lower() == 'exit':
        break

    if country in countries:
        capital = countries[country]
        print(f"Capital of {country} is {capital}")

    elif country in countries:
        print("The capital of", country, "is", countries[country])

    else:
        capital = input(f"Enter the capital of {country}: ")
        countries[country] = capital
        print(f"Added {country} , {capital}")