#!/usr/bin/python3
"""
This is our file storage process
"""

import models
import json


class FileStorage:
    """
    This class creates file storage objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the objects attribute dict
        """
        return self.__objects

    def new(self, obj):
        """
        creates a new dictionary item
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        creates json of objects attribute
        """
        new_objs = {key: value.to_dict() for key, value in self.__objects.items()}

        with open((self.__file_path), 'w', encoding='utf-8') as f:
            json.dump((new_objs), f)

    def reload(self):
        """
        deserializes a json to a stored file
        """
        loaded_dictionary = {}
        try:
            with open(self.__file_path, 'r') as f:
                loaded_dictionary = json.load(f)
            for key, value in loaded_dictionary.items():
                x = value.get("__class__")
                if x in models.available_classes:
                    self.__objects[key] = models.available_classes[x](**value)
        except FileNotFoundError:
            pass
