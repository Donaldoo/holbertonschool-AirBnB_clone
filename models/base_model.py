#!/usr/bin/python3
"""Task 3"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Created base class"""
    str_format = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, BaseModel.str_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        return (F"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def save(self):
        storage.save()
