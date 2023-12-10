#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Class for testing the User class"""

    def test_instance_creation(self):
        """Test if a User instance is created"""
        user_instance = User()
        self.assertIsInstance(user_instance, User)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        user_instance = User()
        expected_str = "[User] ({}) {}".format(user_instance.id, user_instance.__dict__)
        self.assertEqual(str(user_instance), expected_str)

    

if __name__ == '__main__':
    unittest.main()
