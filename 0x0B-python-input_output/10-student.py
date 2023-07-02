#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Object student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the public instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represntation of a simple data structure."""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {key: getattr(self, key) for key
                    in attrs if hasattr(self, key)}
        return (self.__dict__)
