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
        if kwargs:
            formattime = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                    if key == '__class__':
                        continue
                    elif key == 'created_at':
                        self.created_at = datetime.strptime(kwargs['created_at'], formattime)
                    elif key == 'updated_at':
                        self.updated_at = datetime.strptime(kwargs['updated_at'], formattime)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
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
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['__class__'] = self.__class__.__name__
        return dict_obj

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
