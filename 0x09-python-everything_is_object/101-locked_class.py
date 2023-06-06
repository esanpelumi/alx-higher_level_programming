#!/usr/bin/python3
"""Define a LockedClass"""


class LockedClass:
    """
    The class prevent any other instances of name except firstname
    """
    __slots__ = "first_name"
