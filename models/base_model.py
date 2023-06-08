#!/usr/bin/python3
''' Base Class for all other classes '''
import uuid
from datetime import datetime



class BaseModel:
    ''' Base class for all other classes '''


    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' String representation of the BaseModel class '''
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' Updates the public instance attribute updated_at with the current datetime '''
        self.updated_at = datetime.now()


    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__ of the instances '''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict["updated_at"] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return new_dict
