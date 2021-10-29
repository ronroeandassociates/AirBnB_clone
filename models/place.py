#!/usr/bin/python3
from models import BaseModel
"""
Creates a place object
"""
class place(BaseModel):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        for key, value in kwargs.items():
            """
            """
            if key == City_id:
                self.city_id = value
            if key == User.id:
                self.user_id = value
            if key == name:
                self.name = value
            if key == description:
                self.description = value
            if key == number_rooms:
                self.number_rooms = value
            if key == number_bedrooms:
                self.number_bedrooms = value
            if key == max_guest:
                self.max_guest = value
            if key == price_by_night:
                self.price_by_night = value
            if key == latitude:
                self.latitude = value
            if key == longitude:
                self.longitude = value
            if key == Amenity.id:
                self.amenity_id = value
