#!/bin/bash
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a GET request using curl and display the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$URL"
