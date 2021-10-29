#!/usr/bin/python3
from models import BaseModel
"""
Creates a amenity object
"""
class amenity(BaseModel):
    """
    attributes of an amenity object
    """

    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(self)
