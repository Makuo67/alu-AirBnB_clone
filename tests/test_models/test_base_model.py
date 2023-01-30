#!/usr/bin/python3

"""Unit Test Suites"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """Tests all the attributes and methods of BaseModel class"""

    def test_uniqueid(self):
        """Tests if the id is unique"""
        id_1 = BaseModel()
        id_2 = BaseModel()
        id_1 = id_1.id
        id_2 = id_2.id
        self.assertIsInstance(id_1, BaseModel)
        self.assertTrue(hasattr(id_1, "id"))
        self.assertIsInstance(id_1, str)
        self.assertNotEqual(id_1, id_2)

    def test_created_at(self):
        """Tests for the return type of created_at"""
        created_at = BaseModel()
        self.assertIsInstance(created_at.created_at, datetime)

    def test__str__(self):
        """Test if a string representation of the class is returned"""
        my_obj = BaseModel()
        a = my_obj.__str__()
        f = f'[{my_obj.__class__.__name__}] ({my_obj.id}) {my_obj.__dict__}'
        self.assertIn(f, a)

    def test_todict(self):
        """Test to_dict method to ensure in returns a dictionary"""
        dict_obj = BaseModel()
        new_dict = dict_obj.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        obj.name = "Makuo"
        obj.save()

        first_dict = obj.to_dict()
        obj.name = "Okeke"
        obj.save()
        second_dict = obj.to_dict()

        self.assertEqual(first_dict['created_at'], second_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], second_dict['updated_at'])

if __name__ == "__main__":
    unittest.main()