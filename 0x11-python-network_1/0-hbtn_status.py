#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    # URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'
    # Making a request to the URL
    with urllib.request.urlopen(url) as response:
        # Reading and decoding the body of the response
        body = response.read()
        content_type = type(body)  # Getting the type of content (bytes)
        content = body.decode('utf-8')  # Decoding content to UTF-8
        # Displaying additional information and body response as requested
        print("Body response:")
        print(f"    - type: {content_type}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {content}")
