#!/usr/bin/python3
"""test the user model """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Class for testing the User class"""

    def setUp(self):
        """Sets up User for testing"""
        self.user_instance = User()
        self.user_instance.email = 'abcd@gmail.com'
        self.user_instance.password = '123456789'
        self.user_instance.first_name = 'Abdelrahman'
        self.user_instance.last_name = 'Ibrahim'

    def test_inheritance(self):
        """Check if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance_creation(self):
        """Test if a User instance is created"""
        user_instance = User()
        self.assertIsInstance(user_instance, User)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        expected_str = "[User] ({}) {}".format(self.user_instance.id,
                                               self.user_instance.__dict__)
        self.assertEqual(str(self.user_instance), expected_str)

    def test_attributes_values(self):
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

        self.assertTrue(hasattr(user_instance, "password"))
        self.assertTrue(hasattr(user_instance, "email"))
        self.assertTrue(hasattr(user_instance, "first_name"))
        self.assertTrue(hasattr(user_instance, "last_name"))

        self.assertEqual(type(user_instance.email), str)
        self.assertEqual(type(user_instance.password), str)
        self.assertEqual(type(user_instance.first_name), str)
        self.assertEqual(type(user_instance.last_name), str)

    def test_user_to_dict(self):
        """Tests user to_dict"""
        self.assertEqual(type(self.user_instance.to_dict()), dict)

    def test_kwargs(self):
        """Tests user kwargs"""
        new_user = User(**self.user_instance.to_dict())
        self.assertEqual(self.user_instance.id, new_user.id)
        self.assertEqual(self.user_instance.created_at, new_user.created_at)
        self.assertEqual(self.user_instance.updated_at, new_user.updated_at)
        self.assertNotEqual(self.user_instance, new_user)


"""
    def test_user_save(self):
        "Tests user save"
        self.class_instance.save()
    self.assertEqual(type(self.class_instance.updated_at).__name__, "datetime")
"""

if __name__ == '__main__':
    unittest.main()
