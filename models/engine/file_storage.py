#!/usr/bin/python3
''' File Storage Module '''
import json
import os
from models.base_model import BaseModel


class FileStorage:
    ''' File Cabinet for storing objects '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to the JSON file (path: __file_path) '''
        with open(self.__file_path, mode='w', encoding='utf-8') as save_for_later:
            new_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(new_dict, save_for_later)

    def reload(self):
        ''' Deserializes the JSON file to __objects '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as mmm_leftovers:
                new_dict = json.load(mmm_leftovers)
                for key, value in new_dict.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
