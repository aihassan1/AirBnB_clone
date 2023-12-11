#!/usr/bin/python3
"""Define FileStorage class that make the projects persistent"""
from json import load, dump
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """
        FileStorage class

        Attributes:
            __file_path (string): path to the JSON file
            __objects (dictionary): empty - storeobjects by <class name>.id

        Methods:
        all - new - save - reload
    """

    __file_path = "AirBnB_Storage.json"
    __objects = {}

    # Complete
    def all(self):
        "return __objects"
        return FileStorage.__objects

    # Complete
    def new(self, obj):
        """set new obj inside __objects"""
        K_format = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[K_format] = obj

    # Complete
    def save(self):
        """save __objects in __file_path"""
        obj_dict_form = {}

        for key, value_obj in FileStorage.__objects.items():
            obj_dict_form[key] = value_obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as Jfile:
            dump(obj_dict_form, Jfile)

    # Complete
    def reload(self):
        """load __objects from __file_path"""
        classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity}
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as Jfile:
                data = load(Jfile)
                for values in data.values():
                    cls_name = values['__class__']
                    selected_cls = classes[cls_name]
                    self.new(selected_cls(**values))
        except FileNotFoundError:
            pass
