#!/usr/bin/python3
"""
Takes in a URL, sends a request to URL
and displays body of the response
"""
import requests
import sys

if __name__ == "__main__":
    # Fetching URL from command line argument
    url = sys.argv[1]

    # Making a GET request to the provided URL
    response = requests.get(url)

    # Checking HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Displaying the body of the response
        print(response.text)
