#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * ((self.__width) + (self.__height))
        return (perimeter)

    def __str__(self):
        """return a string for the rectangle"""
        ret = []
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        for i in range(self.__height):
            [ret.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append('\n')
        return ("".join(ret))

    def __repr__(self):
        """return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Delete the instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """compare rectangles

        Args:
            rect_1 (): 1st rectangle
            rect_2 (): 2ND rectangle

        Raises:
            TypeError: must be an integer
            TypeError: must be an integer

        Returns:
            method
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)

        elif rect_1.area() > rect_2.area():
            return (rect_1)

        elif rect_1.area() < rect_2.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """square

        Args:
            size (int, optional): _description_. Defaults to 0.

        Returns:
            Rectangle: with width and height = size
        """
        return (cls(size, size))
