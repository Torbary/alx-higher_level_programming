#!/bin/bash
# Display all HTTP methods the server will accept for a given URL
curl -sI "$1" | awk '/Allow:/ {print substr($0, 8)}'
