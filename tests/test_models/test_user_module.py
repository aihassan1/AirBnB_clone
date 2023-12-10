#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Class for testing the User class"""

    def test_inheritance(self):
        """Check if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance_creation(self):
        """Test if a User instance is created"""
        user_instance = User()
        self.assertIsInstance(user_instance, User)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        user_instance = User()
        expected_str = "[User] ({}) {}".format(user_instance.id,
                                               user_instance.__dict__)
        self.assertEqual(str(user_instance), expected_str)

    def test_attribiutes_values(self):
        """
        Ensure that a User instance is created correctly
        , and its attributes are initialized to the default values.
        """
        user_instance = User()

        self.assertEqual(user_instance.email, '')
        self.assertEqual(user_instance.password, '')
        self.assertEqual(user_instance.first_name, '')
        self.assertEqual(user_instance.last_name, '')

    def test_attribute_assignment(self):
        """test attribute_assignment """
        user_instance = User()
        user_instance.email = 'abcd@gmail.com'
        user_instance.password = '123456789'
        user_instance.first_name = 'Abdelrahman'
        user_instance.last_name = 'Ibrahim'

        self.assertEqual(user_instance.email, 'abcd@gmail.com')
        self.assertEqual(user_instance.password, '123456789')
        self.assertEqual(user_instance.first_name, 'Abdelrahman')
        self.assertEqual(user_instance.last_name, 'Ibrahim')

    def test_to_dict_method(self):
        """
        Ensure that the to_dict method returns the expected
        dictionary representation of the User instance.
        """
        user_instance = User()
        expected_dict = {
            'id': user_instance.id,
            'created_at': user_instance.created_at.isoformat(),
            'updated_at': user_instance.updated_at.isoformat(),
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': '',
            '__class__': 'User'
        }
        self.assertEqual(user_instance.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
