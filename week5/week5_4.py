"""Write a program that takes a URL as a command-line argument and reports
whether there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend"""

import sys
import requests

tag = sys.argv[1]

url = 'http://' + tag

resp = requests.get(url)

print(url)