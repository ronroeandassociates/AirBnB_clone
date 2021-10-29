#!/usr/bin/python3
from models import BaseModel
"""
Creates a city object
"""
class City(BaseModel):
    """
    attributes of a city object
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self)

