#!/usr/bin/python3
from models import BaseModel
"""
Creates a review object
"""


class Review(BaseModel):
    """
    attributes of a review object
    """
    place_id = ""
    user_id = ""
    text = ""
