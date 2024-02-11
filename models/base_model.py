#!/usr/bin/python3
"""The BaseModel Class"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseMode for AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Create a new BaseModel.
        Args: *args is unused and **kwargs is for attributes.
        """
        formattime = "%Y-%m-%dT%H:%M:%S.%f" 
        self.updated_at = datetime.today()
        self.id = str(uuid4())
        self.created_at = datetime.today()
        if len(kwargs) != 0:
            for keys, values in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    self.__dict__[keys] = datetime.strptime(values, formattime)
                else:
                    self.__dict__[keys] = values
        else:
            models.storage.new(self)
    def save(self):
        """updates the public instance attribute"""     
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all 
        keys/values of __dict__
        """
        dict_obj = self.__dict__.copy()
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['__class__'] = self.__class__.__name__
        return dict_obj

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
