#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        utf_content = the_page.decode('utf-8')
        print('Body response:')
        print('\t- type: {}'.format(type(the_page)))
        print('\t- content: {}'.format(the_page))
        print('\t- utf8 content: {}'.format(utf_content))
