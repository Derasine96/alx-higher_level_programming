#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': q})
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
