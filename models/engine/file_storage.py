#!/usr/bin/python3
"""
Class that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instance to JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            serial_obj = {key: obj.to_dict() for key,
                          obj in self.__objects.items()}
            json.dump(serial_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing. If the
            file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                serialized_objs = json.load(file)
                for key, value in serialized_objs.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
