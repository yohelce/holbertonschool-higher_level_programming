#!/usr/bin/python3
""" Module base """


import json


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
            return "[]"
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        return json.loads(json_string)
