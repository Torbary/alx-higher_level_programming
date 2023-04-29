#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
   URL with the email as a parameter
"""


import urllib.request
import urllib.parse
import sys
"""import modules"""


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html.decode("utf-8"))
