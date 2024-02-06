#!/usr/bin/python3

import datetime
import uuid
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()
    def __str__(self):
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

#def save(self):

#def to_dict(self):


