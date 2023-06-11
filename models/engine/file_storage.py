#!/usr/bin/python3
''' File Storage Module '''
import json
import os


class FileStorage():
    ''' File Cabinet for storing objects '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to the JSON file (path: __file_path) '''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        ''' Deserializes the JSON file to __objects '''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, obj_dict in new_dict.items():
                self.__objects[key] = eval(value["__class__"])(**value)
