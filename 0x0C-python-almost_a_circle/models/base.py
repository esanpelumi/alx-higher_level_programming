#!/usr/bin/python3
import json
import csv
"""Define a class base"""


class Base:
    """
    Represent the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the id

        Args:
            id (int, optional): id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fil:
            if list_objs == []:
                fil.write("[]")
            else:
                dicts = [x.to_dictionary() for x in list_objs]
                fil.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance

        Returns:
            class:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return (new_instance)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated

        Returns:
            list: List of instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as fil:
                list_dicts = Base.from_json_string(fil.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as fil:
            if list_objs == []:
                fil.write("[]")
            else:
                if cls.__name__ == "Square":
                    items = ["id", "size", "x", "y"]
                else:
                    items = ["id", "width", "height", "x", "y"]
                csv_write = csv.DictWriter(fil, fieldnames=items)
                for obj in list_objs:
                    csv_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
