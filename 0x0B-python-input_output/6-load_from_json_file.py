#!/usr/bin/python3
"""Define a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Return the object from the file"""
    with open(filename) as fil:
        return (json.load(fil))
