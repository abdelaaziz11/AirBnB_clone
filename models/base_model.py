#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def save(self):
        self.update_at = datetime.now()
    """def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")"""

    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['create_at'] = self.create_at.isoformat()
        dict_obj['update_at'] = self.update_at.isoformat()
        return dict_obj
    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
