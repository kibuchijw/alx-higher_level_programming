#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -siX OPTIONS | grep "Allow" | cut -d " " -f 2-
