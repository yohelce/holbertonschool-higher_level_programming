#!/usr/bin/python3
""" Takes 2 arguments in order to solve a Holberton challenge"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    req =  requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(owner, repo))
    my_dict = req.json()
    if req.status_code == 200:
        for elem in my_dict[:10]:
            print('{}: {}'.format(elem.get('sha'), elem.get('commit').get('author').get('name')))
