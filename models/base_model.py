#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """ Base class for other classes """

    def __init__(self, *args, **kwargs):
        """the BaseClass constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass

                if key == "created_at" or key == "updated_at":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, time_format))

    def __str__(self):
        """Return a string representation of the object """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary representation of the object """
        the_dict = {}

        # Add instance attributes to the dictionary
        the_dict = self.__dict__.copy()

        # Add class name to the dictionary
        the_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()

        return the_dict
