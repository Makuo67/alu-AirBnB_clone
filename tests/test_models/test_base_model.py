#!/usr/bin/python3

"""Unit Test Suites"""
import unittest
import datetime
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
        self.assertTrue(BaseModel.__str__, str)

    def test_todict(self):
        """Test to_dict method to ensure in returns a dictionary"""
        dict_obj = BaseModel()
        new_dict = dict_obj.to_dict()
        self.assertIsInstance(new_dict['created_at'], str)
