#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""
import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    status = req.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(req.text)
