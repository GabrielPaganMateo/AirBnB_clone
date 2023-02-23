#!/usr/bin/python3
"""Module provide User class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
