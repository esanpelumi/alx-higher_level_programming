#!/usr/bin/python3
"""Create a read file function"""


def read_file(filename=""):
    """Print the contents of the file to stdout"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
