#!/usr/bin/python3
"""Define a function is_same_class"""


def is_same_class(obj, a_class):
    """Return a boolean if they are the same instance"""
    if type(obj) == a_class:
        return (True)
    return (False)
