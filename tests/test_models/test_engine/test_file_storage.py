#!/usr/bin/python3
"""Test suites for File storage"""

import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test suites for the FileStorage class"""
    def setUp(self):
        self.storage = FileStorage()
        self.bm = BaseModel()

    def test_HasAttr(self):
        """Tests for the attributes of FileStorage"""
        self.assertEqual(hasattr(FileStorage, '__filepath'), True)
        self.assertEqual(hasattr(FileStorage, '__objects'), True)

    def test_all_method(self):
        """Tests the all method in FileStorage"""
        self.storage.new(self.bm)
        self.assertEqual(self.storage.all(), {"BaseModel.{}".format(self.bm.id): self.bm})

    def test_new_method(self):
        """Tests the new method"""
        self.storage.new(self.bm)
        self.assertIn("BaseModel.{}".format(self.bm.id), self.storage.all().keys())

    def test_save_method(self):
        """Tests the save method"""
        self.storage.new(self.bm)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn('"BaseModel.{}"'.format(self.bm.id), f.read())

    def test_reload_method(self):
        """Tests the reload method"""
        self.storage.new(self.bm)
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        self.assertEqual(self.bm.to_dict(), self.storage.all()["BaseModel.{}".format(self.bm.id)].to_dict())

if __name__ == '__main__':
    unittest.main()
