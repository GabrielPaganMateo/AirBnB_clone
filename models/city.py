#!/usr/bin/python3
"""
Module with Class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines class City
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
