#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and
displays the body of the response """
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":

    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
