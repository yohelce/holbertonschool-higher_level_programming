#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        utf_content = the_page.decode('utf-8')
        print('Body response:')
        print(f'\t- type: {type(the_page)}')
        print(f'\t- content: {the_page}')
        print(f'\t- utf8 content: {utf_content}')
