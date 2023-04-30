#!/usr/bin/python3
""" if the status code is >= 400 print Error code: 401 else print the text
"""

import requests
import sys


def main():
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
