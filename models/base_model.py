#!/usr/bin/python3
"""
BaseModel class module
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes
            Attrs:
                id (str): instance identity
                created_at: date of instance creation
                updated_at: date of instance attrs change
        """
        if kwargs:
            for keys in kwargs:
                if keys != __class__:
                    self.__dict__[keys] = kwargs[keys]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Changes the time of instance attrs change
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance including new attrs
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        if type(self.updated_at) is not str:
            obj_dict['created_at'] = datetime.isoformat(self.updated_at)
        if type(self.created_at) is not str:
            obj_dict['updated_at'] = datetime.isoformat(self.created_at)
        return obj_dict

#2023-02-18T10:44:10.497797