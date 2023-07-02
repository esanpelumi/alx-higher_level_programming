#!/usr/bin/python3
"""define the function fron_json_string"""
import json


def from_json_string(my_str):
    """return the object representation of the string"""
    return json.loads(my_str)
