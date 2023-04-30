#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={"q":
                                 letter})
        data = response.json()

        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
