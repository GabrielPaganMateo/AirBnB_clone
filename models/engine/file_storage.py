#!/usr/bin/python3
"""COMMENT"""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes and deserializes"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        key_nm = f"{obj.__class__.__name__}.id"
        self.__objects[key_nm] = obj

    def save(self):
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        if path.exists(self.__file_path) is False:
            pass
        else:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)