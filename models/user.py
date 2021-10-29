#!/usr/bin/python3
from models import BaseModel
"""
Creates a user object
"""
class User(BaseModel):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(self)
        for key, value in kwargs.items():
            if key == email:
                self.email = value
            if key == password:
                self.password = value
            if key == first_name:
                self.first_name = value
            if key == last_name:
                self.last_name = key.value
