#!/usr/bin/python3
"""Test suites for File storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suites for the FileStorage class"""

    def test_HasAttr(self):
        """Tests for the attributes of FileStorage"""
        self.assertEqual(hasattr(FileStorage, '__filepath'), True)
        self.assertEqual(hasattr(FileStorage, '__objects'), True)






