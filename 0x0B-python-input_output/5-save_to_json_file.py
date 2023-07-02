#!/usr/bin/python3
"""define a function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to the file filename"""
    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
