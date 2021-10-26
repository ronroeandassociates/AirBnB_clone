#!/usr/bin/python3
"""
This module sets up the data for the base class for HBnB
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Creates the uuid, and other attributes
    """

    def __init__(self, *args, **kwargs):
        """
        initialize some attributes
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self. updated_at = datetime.now()

    def __str__(self):
        """
        outputs the attributes in string format
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the updated at attribute when changes are made
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        creates the object as a dictionary
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return my_dict
