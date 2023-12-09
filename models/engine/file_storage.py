#!/usr/bin/python3

"""Define FileStorage class that that make the projects persistent"""
from json import loads, dumps


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

    def all(self):
        "return __objects"
        return self.__objects

    def new(self, obj):
        """set new obj inside __objects"""
        pass

    def save(self):
        """save __objects in __file_path"""
        pass

    def reload(self):
        """load __objects from __file_path"""
        pass
