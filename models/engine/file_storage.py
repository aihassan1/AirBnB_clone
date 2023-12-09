#!/usr/bin/python3

from json import loads, dumps


class FileStorage:

    __file_path = ""
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass
