#!/usr/bin/python3

import json

class FileStorage:
    """construct"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                n_obj = json.load(f)
                for key, value in n_obj.items():
                    Cname = value['__class__']
                    objs = eval(Cname)(**value)
                    FileStorage.__objects[key] = objs
        except Exception:
            pass
