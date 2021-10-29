#!/usr/bin/python3
from models import BaseModel
"""
Creates a state object
"""
class State(BaseModel):
    """
    attributes of a state object
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self)
