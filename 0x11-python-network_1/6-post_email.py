#!/usr/bin/python3
"""a script that takes in a URL and an email address, send a POST request
   to the passes URL with the email as a parameter and finally
   displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={"email": email})
    print(response.text)