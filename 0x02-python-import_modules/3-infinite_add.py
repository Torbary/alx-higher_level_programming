#!/usr/bin/python3

import sys

# The arguments are stored in the sys.argv list
# with the first element being the name of the script itself
# We can skip the first element using a slice

args = sys.argv[1:]

# Initialize the sum to 0

result = 0

# Iteratre through the agrs and add them to the sum

for s in args:
    result += int(s)

print(result)
