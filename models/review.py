#!/usr/bin/python3
from models import BaseModel
"""
Creates a review object
"""
class review(BaseModel):
    """
    attributes of a review object
    """
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        super().__init__(self)
