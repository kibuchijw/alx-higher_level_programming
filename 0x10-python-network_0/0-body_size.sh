#!/bin/bash
# Send a GET request using curl and display the size of the response body in bytes
curl -s "$1" | wc -c
