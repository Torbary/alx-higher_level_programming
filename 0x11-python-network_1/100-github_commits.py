#!/usr/bin/python3
"""Get the last 10 commits from a github repo"""

import requests
import sys


if len(sys.argv) == 3:
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    else:
        print(f"Error: {response.status_code} {response.reason}")
else:
    print("Usage: python script.py <repo> <owner>")
