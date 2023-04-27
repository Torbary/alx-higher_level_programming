#!/bin/bash
# Get the URL from the command line arguments
url="$1"

# Send a request to the URL using curl and store the output in a variable
response=$(curl -sI "$url")

# Get the content length of the response using grep and awk
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}')

# Display the content length in bytes
echo "$content_length"
