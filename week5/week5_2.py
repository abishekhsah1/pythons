"""Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument)."""

import sys

num = len(sys.argv[3:])
print(f"Number of command-line arguments: {num}")