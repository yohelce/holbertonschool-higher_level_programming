#!/usr/bin/python3
""" Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(username, pwd))
    my_dict = req.json()
    if req.status_code == 200:
        print(my_dict.get('id'))
    else:
        print('None')
