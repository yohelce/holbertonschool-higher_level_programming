#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
