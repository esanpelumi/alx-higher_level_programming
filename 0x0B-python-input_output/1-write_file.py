#!/usr/bin/python3
"""Define function write_file"""


def write_file(filename="", text=""):
    """Return: the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as fil:
        return (fil.write(text))
