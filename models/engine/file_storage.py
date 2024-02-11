#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON
"""

import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """ serializes instances to a JSON file 
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """JSON file to __objects if it exists"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except:
                pass
