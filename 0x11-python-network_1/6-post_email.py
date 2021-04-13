#!/usr/bin/python3
""" sends POST request to url with email """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.port(url, data=value)
    print(r.text)
