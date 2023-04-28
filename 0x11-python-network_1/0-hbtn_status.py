#!/usr/bin/env python3
"""python script that fetches the gioven URL using urllib package"""


import urllib.request
"""import urllib and access request"""

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decode("utf-8")))
