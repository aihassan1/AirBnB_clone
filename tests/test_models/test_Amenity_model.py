#!/usr/bin/python3
"""test AmenityModel"""
import unittest
from models.Amenity import Amenity
from models.base_model import BaseModel


class TestAmenityModel(unittest.TestCase):
    """testing the AmenityModel """

    def test_inheritance(self):
        """Check if class inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance_creation(self):
        """Test if a class instance is created"""
        new_instance = Amenity()
        self.assertIsInstance(new_instance, Amenity)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        new_instance = Amenity()
        expected_str = "[Amenity] ({}) {}".format(new_instance.id,
                                                  new_instance.__dict__)
        self.assertEqual(str(new_instance), expected_str)

    def test_attributes_default_values(self):
        """Test if attributes have the correct default values"""
        new_instance = Amenity()
        self.assertEqual(new_instance.name, '')

    def test_attributes_assignment(self):
        """Test if attributes can be correctly assigned"""
        new_instance = Amenity()
        new_instance.name = 'test example'
        self.assertEqual(new_instance.name, 'test example')


if __name__ == '__main__':
    unittest.main()
