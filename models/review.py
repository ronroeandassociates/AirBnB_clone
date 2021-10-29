#!/usr/bin/python3
from models import BaseModel
"""
Creates a review object
"""
class review(BaseModel):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        for key, value in kwargs.items():
            if key == Place.id:
                place_id = value
            if key == User_id:
                user_id = value
            else:
                text = value
