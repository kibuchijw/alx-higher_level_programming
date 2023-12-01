#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
"""

import requests
import sys

if __name__ == "__main__":
    # Fetching URL from command line argument
    url = sys.argv[1]
    # Making a GET request to the provided URL
    response = requests.get(url)

    # Retrieving and displaying the value of the 'X-Request-Id' header
    request_id = response.headers['X-Request-Id']
    print(f"{request_id}")
