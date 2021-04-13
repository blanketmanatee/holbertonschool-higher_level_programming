#!/usr/bin/python3
""" takes in a letter and sends a POST request to http://0.0.0.0:5000/search_u\
ser """

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv)
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json
