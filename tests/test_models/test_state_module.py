#!/usr/bin/python3
"""test the user model """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Class for testing the State class"""

    def setUp(self):
        """Sets up State for testing"""
        self.class_instance = State()
        self.class_instance.name = "Abdelrahman"

    def test_inheritance(self):
        """Check if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance_creation(self):
        """Test if a State instance is created"""
        class_instance = State()
        self.assertIsInstance(class_instance, State)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        expected_str = "[State] ({}) {}".format(self.class_instance.id,
                                                self.class_instance.__dict__)
        self.assertEqual(str(self.class_instance), expected_str)

    def test_attributes_values(self):
        """
        Ensure that a State instance is created correctly
        , and its attributes are initialized to the default values.
        """
        class_instance = State()
        self.assertEqual(class_instance.name, '')

    def test_attribute_assignment(self):
        """test attribute_assignment """
        class_instance = State()
        class_instance.name = 'Abdelrahman'
        self.assertEqual(class_instance.name, 'Abdelrahman')
        self.assertTrue(hasattr(class_instance, "name"))
        self.assertEqual(type(class_instance.name), str)

    def test_user_to_dict(self):
        """Tests user to_dict"""
        self.assertEqual(type(self.class_instance.to_dict()), dict)

    def test_kwargs(self):
        """Tests user kwargs"""
        new_user = State(**self.class_instance.to_dict())
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
