#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        bg.integer_validator("width", width)
        self.__width = width
        bg.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the string representation of the Rectangle"""
        str1 = "[" + str(self.__class__.__name__)
        str1 += "] " + str(self.__width) + "/" + str(self.__height)
        return (str1)
