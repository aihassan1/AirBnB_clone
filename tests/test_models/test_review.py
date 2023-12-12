#!/usr/bin/python3
"""test the user model """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Class for testing the Review class"""

    def setUp(self):
        """Sets up Review for testing"""
        self.class_instance = Review()
        self.class_instance.place_id = "some place"
        self.class_instance.text = "some text"
        self.class_instance.user_id = "some user_id"

    def test_inheritance(self):
        """Check if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance_creation(self):
        """Test if a Review instance is created"""
        class_instance = Review()
        self.assertIsInstance(class_instance, Review)

    def test_str_method(self):
        """Test if the __str__ method is implemented"""
        expected_str = "[Review] ({}) {}".format(self.class_instance.id,
                                                 self.class_instance.__dict__)
        self.assertEqual(str(self.class_instance), expected_str)

    def test_attributes_values(self):
        """
        Ensure that a Review instance is created correctly
        , and its attributes are initialized to the default values.
        """
        self.assertEqual(self.class_instance.text, 'some text')
        self.assertEqual(self.class_instance.place_id, 'some place')
        self.assertEqual(self.class_instance.user_id, 'some user_id')

    def test_attribute_assignment(self):
        """test attribute_assignment """
        class_instance = Review()
        class_instance.user_id = 'Abdelrahman'
        class_instance.place_id = "string"
        class_instance.text = 'some text'

        self.assertEqual(class_instance.user_id, 'Abdelrahman')
        self.assertEqual(class_instance.place_id, 'string')
        self.assertEqual(class_instance.text, 'some text')

        self.assertTrue(hasattr(class_instance, "user_id"))
        self.assertTrue(hasattr(class_instance, "place_id"))
        self.assertTrue(hasattr(class_instance, "text"))

        self.assertEqual(type(class_instance.user_id), str)
        self.assertEqual(type(class_instance.place_id), str)
        self.assertEqual(type(class_instance.text), str)

    def test_user_to_dict(self):
        """Tests user to_dict"""
        self.assertEqual(type(self.class_instance.to_dict()), dict)

    def test_kwargs(self):
        """Tests user kwargs"""
        new_user = Review(**self.class_instance.to_dict())
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
