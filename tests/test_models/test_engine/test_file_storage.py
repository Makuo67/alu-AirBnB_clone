#!/usr/bin/python3
"""Test suites for File storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage(unittest.TestCase):
    """Test suites for the FileStorage class"""

    def test_storageinstance(self):
        """Tests if storage is an instance of Filestorage"""
        self.assertIsInstance(storage, FileStorage)
