#!/usr/bin/python3
"""using a request package to display the value of X-Request-id in
   the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-id"))
