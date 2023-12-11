#!/usr/bin/python3
"""test the user model """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Class for testing the City class"""

    def setUp(self):
        """Sets up City for testing"""
        self.class_instance = City()
        self.class_instance.name = "Abdelrahman"
        self.class_instance.state_id = "string"

    def test_inheritance(self):
        """Check if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance_creation(self):
        """Test if a City instance is created"""
        class_instance = City()
        self.assertIsInstance(class_instance, City)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        expected_str = "[City] ({}) {}".format(self.class_instance.id,
                                               self.class_instance.__dict__)
        self.assertEqual(str(self.class_instance), expected_str)

    def test_attributes_values(self):
        """
        Ensure that a City instance is created correctly
        , and its attributes are initialized to the default values.
        """
        class_instance = City()
        self.assertEqual(class_instance.name, '')

    def test_attribute_assignment(self):
        """test attribute_assignment """
        class_instance = City()
        class_instance.name = 'Abdelrahman'
        class_instance.state_id = "string"
        self.assertEqual(class_instance.name, 'Abdelrahman')
        self.assertTrue(hasattr(class_instance, "name"))
        self.assertEqual(type(class_instance.name), str)

        self.assertEqual(class_instance.state_id, 'string')
        self.assertTrue(hasattr(class_instance, "state_id"))
        self.assertEqual(type(class_instance.state_id), str)

    def test_user_to_dict(self):
        """Tests user to_dict"""
        self.assertEqual(type(self.class_instance.to_dict()), dict)

    def test_kwargs(self):
        """Tests user kwargs"""
        new_user = City(**self.class_instance.to_dict())
        self.assertEqual(self.class_instance.id, new_user.id)
        self.assertEqual(self.class_instance.created_at, new_user.created_at)
        self.assertEqual(self.class_instance.updated_at, new_user.updated_at)
        self.assertNotEqual(self.class_instance, new_user)


"""
    def test_user_save(self):
        "Tests user save"
        self.class_instance.save()
    self.assertEqual(type(self.class_instance.updated_at).__name__, "datetime")
"""

if __name__ == '__main__':
    unittest.main()
