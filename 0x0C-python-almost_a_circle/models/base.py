#!/usr/bin/python3
""" Module base """


import json
import csv
from os.path import exists


class Base:
    """Class with:
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance.
        Args:
            - id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        if list_objs is None or list_objs == []:
            jlist = "[]"
        else:
            jlist = cls.to_json_string([d.to_dictionary() for d in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as f:
            f.write(jlist)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "":
            return []
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = cls.__name__ + ".json"
        new_list = []
        if exists(filename) is True:
            with open(filename, mode="r") as f:
                dicts = cls.from_json_string(f.read())
                for d in dicts:
                    new_list.append(cls.create(**d))
                return new_list
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format
        and saves it to a file.
        Args:
            - list_objs: list of instances
        """

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "square":
                    fieldnames = ["id", "size", "x", "y"]
                spamwriter = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    spamwriter.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.
        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        result = []

        if exists(filename) is True:
            with open(filename, mode="r", newline="") as f:
                obj_list = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                    for data in obj_list:
                        new_dict = {}
                        for k, v in zip(fieldnames, data):
                            new_dict[k] = int(v)
                        result.append(cls.create(**new_dict))
                elif cls.__name__ == "square":
                    fieldnames = ["id", "size", "x", "y"]
                    fieldnames = ["id", "width", "height", "x", "y"]
                    for data in obj_list:
                        new_dict = {}
                        for k, v in zip(fieldnames, data):
                            new_dict[k] = int(v)
                        result.append(cls.create(**new_dict))
        return result
