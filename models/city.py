#!/usr/bin/python3
from models import BaseModel
"""
Creates a city object
"""
class City(BaseModel):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        for key, value in kwargs.items():
            if key == State_id:
                self.state_id = value
            if key == name:
                self.name = value
