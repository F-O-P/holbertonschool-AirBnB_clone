#!/usr/bin/python3
''' Base Class for all other classes '''
import uuid
import storage
from datetime import datetime



class BaseModel:
    ''' Base class for all other classes '''


    time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        ''' Constructor for BaseModel class '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs is not None or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, 'time_format')
                setattr(self, key, value)
        else:
            storage.new(self)

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
        new_dict["created_at"] = self.created_at.strftime('time_format')
        new_dict["updated_at"] = self.updated_at.strftime('time_format')
        return new_dict
