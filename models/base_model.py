#!/usr/bin/python3
""" base model class definition """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for other classes """

    # complete
    def __init__(self, *args, **kwargs):
        """the BaseClass constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    formated_time = datetime.strptime(value, time_format)
                    setattr(self, key, formated_time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    # Complete
    def __str__(self):
        """Return a string representation of the object """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    # Complete
    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    # Complete
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
