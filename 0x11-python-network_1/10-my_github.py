#!/usr/bin/python3
"""The script is using Basic Authentication with a personal access token
   to access the GitHub API to get the user's information.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print("None")
