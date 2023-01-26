#!/usr/bin/python3

"""Unit Test Suites"""

import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """Tests all the attributes and methods of BaseModel class"""

    def test_uniqueid(self):
        """Tests if the id is unique"""
        id_1 = BaseModel()
        id_2 = BaseModel()
        id_1 = id_1.id
        id_2 = id_2.id

        self.assertNotEqual(id_1, id_2)

    def test_created_at(self):
        """Tests that times for created_at and updated_at are not the same"""
        created_at = BaseModel()
        self.assertNotEqual(created_at.created_at, created_at.updated_at)
