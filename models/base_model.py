#!/usr/bin/python3
/*
Title:AirBnB_Clone
author:kelly villa
date:feb 2020
Availabiltiy:https://github.com/02KellyV/AirBnB_clone/blob/master/models/base_model.py */

""" The base class for the entire project """

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ Base for all common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        if kwargs:
            for keys, val in kwargs.items():
                if keys != "__class__"
                if keys=="created_at" or keys == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f") 
                setattr(self, keys, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        newbase = self.__dict__.copy()
        newbase["__class__"] = self.__class__.__name__
        newbase["created_at"] = self.created_at.isoformat()
        newbase["updated_at"] = self.updated_at.isoformat()
        return newbase
