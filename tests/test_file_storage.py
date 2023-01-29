import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test suites for the FileStorage class"""
    my_model = BaseModel()

    def test_storageinstance(self):
        """Tests if storage is an instance of Filestorage"""
        self.assertIsInstance(storage, FileStorage)
