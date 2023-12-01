#!/usr/bin/python3
"""
A Script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Fetching URL from command line argument
    url = sys.argv[1]
    # Making a request to the provided URL
    with urllib.request.urlopen(url) as response:
        # Retrieving and displaying the value of the 'X-Request-Id' header
        request_id = response.headers['X-Request-Id']
        print(f"{request_id}")
