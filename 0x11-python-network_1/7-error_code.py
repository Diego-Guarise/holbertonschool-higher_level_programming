#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to
the URL and displays the body of the response."""

if __name__ == "__main__":
    import requests
    from sys import argv

    html = requests.get(argv[1])
    if html.status_code < 400:
        print(html.text)
    else:
        print("Error code: {}".format(html.status_code))
