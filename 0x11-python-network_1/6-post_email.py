#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    post = requests.post(url, data=email)
    print(post.text))
