#!/usr/bin/python3
"""
Fetches the value of the X-Req-ID header from the url given 

"""
import requests
import sys

def main():
    """Main function to fetch and display The X-req-Id header"""
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)


    url = sys.argv[1]
    response = requests.get(url)
    x_req_id =response.headers.get('X-Req-Id')

    if x_req_id is not None:
        print(x_req_id)

if __name__ == "__main__":
    main()    

