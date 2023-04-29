#!/usr/bin/python3
""" script that handles an error """

import urllib.request
import urllib.error
import sys
"""imported modules"""


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()

        print(html.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
