#!/usr/bin/python3
"""
Module for file storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """
    serializes and deserializes data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for k, ob in self.__objects.items():
            new_dict[k] = ob.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to objects"""
        new_obj_dict = {}
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for k, v in new_obj_dict.items():
                    self.__objects[k] = eval(v["__class__"])(**v)

        except FileNotFoundError:
            pass
