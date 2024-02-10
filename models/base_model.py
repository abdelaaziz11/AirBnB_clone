#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models
from models.__init__ import storage

class BaseModel:
    def __init__(self, *arg, **kwargs):
        """ base model """
        formt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for keys, values in kwargs.items():
                """if keys != '__class__':
                    setattr(self, keys, values)"""
                if keys == "created_at":
                    self.__dict__[keys] = datetime.strptime(values, formt)
                elif keys == "updated_at":
                    self.__dict__[keys] = datetime.strptime(values, formt)
                else:
                    self.__dict__[k] = v

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
    """def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")"""
    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

