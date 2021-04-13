#!/usr/bin/python3
""" takes in url sends a request to url and displays value of X-Request-Id var frm header """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]


    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
