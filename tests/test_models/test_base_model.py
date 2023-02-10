#!/usr/bin/python3
"""
Base Model tests
"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
import time
import os


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
        """test save."""
        base = BaseModel()
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)
        self.assertTrue(base.updated_at > base.created_at)

    def test_save_file(self):
        """test save."""
        if os.path.isfile("file.json"):
            os.remove(os.path.join("file.json"))
            print(os.path.isfile("file.json"))
        base = BaseModel()
        print(base.id)
        time.sleep(1)
        base.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", 'w') as file:
            serialized_content = json.load(file)
            for item in serialized_content.values():
                self.assertIsNotNone(item['__class__'])


if __name__ == "__main__":
    unittest.main()
