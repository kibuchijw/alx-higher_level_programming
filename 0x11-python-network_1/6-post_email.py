#!/usr/bin/python3
"""
Takes in a URL and email address, sends a POST
request to passed URL and displays body of response
"""

import requests
import sys

if __name__ == "__main__":
    # Fetching URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = {'email': email}

    # Making a POST request to the provided URL with email as a parameter
    response = requests.post(url, data=data)

    # Displaying the body of the response
    print(response.text)
