#!/usr/bin/python3
"""COMMENT"""
import json
from models.base_model import BaseModel


class FileStorage():
    """Class that serializes and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary with all objects atributes"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the BaseModel instance"""
        key_nm = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key_nm] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(self.__file_path, "w", encoding='utf-8') as file:
            (json.dump({k: v.to_dict()
             for k, v in self.__objects.items()}, file))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                self.__objects = ({k: BaseModel(**v)
                                  for k, v in json.load(file).items()})
        except Exception:
            pass
