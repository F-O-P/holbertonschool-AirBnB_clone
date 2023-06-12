#!/usr/bin/python3
''' Base Class for all other classes '''
import uuid
from datetime import datetime
import models



class BaseModel:
    ''' Base class for all other classes '''


    def __init__(self, *args, **kwargs):
        ''' Constructor for BaseModel class '''
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat('2020-01-08T15:29:52.040435')
                if key != '__class__':
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                    self.created_at = self.updated_at = datetime.now()
                else:
                    models.storage.new(self)

    def __str__(self):
        ''' String representation of the BaseModel class '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' Updates the public instance attribute updated_at with the current datetime '''
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        ''' Return a dictionary containing all keys/values of __dict__ of the instances '''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
