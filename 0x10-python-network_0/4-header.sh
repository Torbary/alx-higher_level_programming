#!/bin/bash
#takes in a URL as an assignment, sends a GET request to the URL,
url="$1"
curl -sH "X-School-User-Id: 98" "$url"
