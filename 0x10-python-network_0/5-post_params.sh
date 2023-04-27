#!/bin/bash
# Send a POST request to a URL and display the response body
curl -sLX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
