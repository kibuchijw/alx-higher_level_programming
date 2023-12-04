#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays body of the response(decoded in utf-8
"""

import urllib.request
import urllib.error
import sys

# Fetching URL from command line argument
url = sys.argv[1]

# Making a GET request to the provided URL
try:
    with urllib.request.urlopen(url) as response:
        # Reading and decoding the body of the response
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    # Handling HTTPError and printing the status code
    print(f"Error code: {e.code}")
