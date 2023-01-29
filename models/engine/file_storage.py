#!/usr/bin/python3

"""Storage module for Airbnb Instances"""

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns  the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets the object id in the dictionary"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserialize JSON to __objects"""
        try:
            with open('file.json', 'r') as json_file:
                new_dict = json.load(json_file)
                print(new_dict)
        except FileNotFoundError:
            pass
