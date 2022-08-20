#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={'q': q})
    try:
        dict = req.json()
        if dict == {}:
            print('No result')
        else:
            print('[{}] {}'.format(dict.get('id'), dict.get('name')))
    except:
        print('Not a valid JSON')
