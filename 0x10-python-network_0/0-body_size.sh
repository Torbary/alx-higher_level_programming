#!/bin/bash
# Get the URL from the command line arguments
curl -s "$1" | wc -c
