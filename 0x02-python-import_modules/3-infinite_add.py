#!/usr/bin/python3

from sys import argv

# The arguments are stored in the sys.argv list
# with the first element being the name of the script itself
# We can skip the first element using a slice


# Initialize the sum to 0

result = 0

# Iteratre through the agrs and add them to the sum

for s in argv[1:]:
    result += int(s)

print("{:d}".format(result))
