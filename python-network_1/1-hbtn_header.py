#!/usr/bin/env python3
"""
Python script to fetch and display the value of X-Request-Id from the response header.
"""

import requests
import sys

def fetch_x_request_id(url):
    """
    Fetches and displays the value of X-Request-Id from the response header of the given URL.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
   
    if x_request_id is not None:
        print(x_request_id)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fetch_x_request_id(url)
