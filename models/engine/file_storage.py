#!/usr/bin/python3
"""
"""

import models
import json


class FileStorage:
    """
    """
    __file_path = "file.json"
    --objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save{self):
        """
        """
        new_objs = {}

        for key,  value in self.__objects.items():
            new_objs[key] = value.to_dict()
        with open(self.__file_path), "w") as f:
            json.dump(new_objs), f)

    def reload(self):
        """
        """
        loaded_dictionary = {}
        try:
            with open(self.__file_path, "r") as f:
                loaded_dictionary = json.load(f)
            for key, value in loaded_dictionary.items():
                x = value.get("__class__")
                if x in models.available_rooms:
                    self.__objects[key] = models.available_rooms[x](**value)
        except FileNotFoundError:
            pass
