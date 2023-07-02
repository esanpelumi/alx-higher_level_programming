#!/usr/bin/python3
"""Define a function append_write"""


def append_write(filename="", text=""):
    """Append text to the filename

    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file.
    Returns:
        the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as fil:
        return (fil.write(text))
