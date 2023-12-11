#!/usr/bin/python3
"""Define TestFileStorage Class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import remove


class TestFileStorage(unittest.TestCase):
    # You should creat file and delete it after each call of functions here
    # # # Stay Sharp # # #

    def setUp(self):
        """Creat storage instance to check"""
        self.storage = FileStorage()

    def tearDown(self):
        """Remove file after finish test"""
        try:
            remove("AirBnB_Storage.json")
        except FileNotFoundError:
            pass

    def test_Instance(self):
        """test instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_FilePath(self):
        """test filepath attripute"""
        self.assertIsInstance("AirBnB_Storage.json", str)

    def test_All(self):
        """test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_New(self):
        """test new method"""
        # check key format
        # check the type of value of key
        obj = BaseModel()
        self.storage.new(obj)
        key_formate = f"BaseModel.{obj.id}"
        self.assertIn(key_formate, self.storage.all().keys())

    def test_Save(self):
        """test save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("AirBnB_Storage.json", "r", encoding="utf-8") as j_file:
            self.assertIn(obj.id, j_file.read())

    def test_Reload(self):
        """test reload method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key_formate = f"BaseModel.{obj.id}"
        self.assertIn(key_formate, self.storage.all())
