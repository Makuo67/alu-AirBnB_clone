#!/usr/bin/python3
"""
Base Model tests
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout


class TestBaseModel(unittest.TestCase):
    """ Unit Tests"""

    def test_to_dict(self):
        """tests for to_dict method"""

        copy = BaseModel()
        copy_dict = copy.to_dict()
        self.assertIsInstance(copy_dict["created_at"], str)

    def test_unique_id(self):
        """tests for id uniqueness"""
        copy = BaseModel()
        copy_2 = BaseModel()
        self.assertNotEqual(copy.id, copy_2.id)

    def test_created_at(self):
        """tests for created_at attribute"""
        copy = BaseModel()
        self.assertIsInstance(copy.created_at, datetime)

    def test_str(self):
        """tests for str method"""
        with StringIO() as bufr, redirect_stdout(bufr):
            my_cop = BaseModel()
            print(my_cop.__str__())
            a = bufr.getvalue()
        self.assertIn(
            f'[{my_cop.__class__.__name__}] ({my_cop.id}) {my_cop.__dict__}',
            a)

    def test_save(self):
        """test for save method"""
        copy_1 = BaseModel()
        copy_1.name = "James"
        copy_1.save()
        self.assertNotEqual(copy_1.created_at, copy_1.updated_at)


if __name__ == "__main__":
    unittest.main()