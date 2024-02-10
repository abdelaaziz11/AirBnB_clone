#!/usr/bin/python3
"""The BaseModel Class"""
from datetime import datetime
from uuid import uuid4
#import models
#from models.__init__ import storage

class BaseModel:
    def __init__(self):
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.today()
        #storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict_obj = self.__dict__.copy()
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['__class__'] = self.__class__.__name__
        return dict_obj

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
