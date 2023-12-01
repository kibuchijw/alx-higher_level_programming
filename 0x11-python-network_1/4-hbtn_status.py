#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using requests package
"""

import requests

if __name__ == "__main__":
    # Making a GET request to the URL
    response = requests.get("https://alx-intranet.hbtn.io/status")

    # Displaying the body of the response with tabulation before each line
    body = response.text.split('\n')
    for line in body:
        print("Body response:")
        print(f"    - type: {type(response.text)}")
        print(f"    - content: {response.text}")
