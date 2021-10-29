#!/usr/bin/python3
from models import BaseModel
"""
Creates a user object
"""
class User(BaseModel):
    """
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(self)

