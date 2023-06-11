#!/usr/bin/python3
"""Define a function inherits_from"""


def inherits_from(obj, a_class):
    """Return a boolean upon call"""
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return (True)
    return (False)
