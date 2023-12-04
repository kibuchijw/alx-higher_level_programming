#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request
to passed URL with the email as parameter, and displays body of the response
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Fetching URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    # Making a POST request to the provided URL with email as a parameter
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        # Reading and decoding the body of the response
        body = response.read().decode('utf-8')
        print(body)
