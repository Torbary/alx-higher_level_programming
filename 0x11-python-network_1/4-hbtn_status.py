#!/usr/bin/python3
""" script that uses request package to get the URL"""

import requests
"""import module"""

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
