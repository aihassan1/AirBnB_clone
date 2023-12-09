import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test___str__method(self):
        """
        Test if the __str__ method returns the expected string representation
        """
        model = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(model.id,
                                                       model.__dict__)
        self.assertEqual(str(model), expected_string)

    def test_save_method(self):
        """
        Test if the save method updates the 'updated_at' attribute
        """
        model = BaseModel()
        initial_updated_at_time = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at_time, model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with expected keys and values
        """
        model = BaseModel()
        model_dictionary = model.to_dict()

        # Check if keys are present in the dictionary
        self.assertIn('id', model_dictionary)
        self.assertIn('__class__', model_dictionary)
        self.assertIn('created_at', model_dictionary)
        self.assertIn('updated_at', model_dictionary)

        # Check if the values are correct
        self.assertEqual(model_dictionary['id'], model.id)
        self.assertEqual(model_dictionary['__class__'],
                         model.__class__.__name__)
        self.assertEqual(model_dictionary['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dictionary['updated_at'],
                         model.updated_at.isoformat())

