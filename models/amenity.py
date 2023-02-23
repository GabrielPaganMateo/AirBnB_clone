#!/usr/bin/python3
"""
Module with Class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Define Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
