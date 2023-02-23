#!/usr/bin/python3
"""
BaseModel class module
"""
import uuid
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
            for keys, value in kwargs.items():
                if keys in ['created_at', 'updated_at']:
                    self.__dict__[keys] = (datetime.strptime
                                           (value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif keys != '__class__':
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
