#!/usr/bin/python3
from models import BaseModel
"""
Creates a amenity object
"""
class amenity(BaseModel):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        for key, value in kwargs.items():
            if key == name:
                self.name == value
