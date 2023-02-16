import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestCreateCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        HBNBCommand().onecmd("create")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistent_class_name(self, mock_stdout):
        HBNBCommand().onecmd("create MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_object(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel name="My House" value=42.0')
        object_id = mock_stdout.getvalue().strip()
        self.assertTrue(object_id)
        storage.delete(BaseModel(id=object_id))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_attributes(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel name="My House" value=invalid')
        self.assertEqual(mock_stdout.getvalue().strip(), "** attribute value not valid **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_format(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel invalid_format')
        self.assertEqual(mock_stdout.getvalue().strip(), "** attribute format not valid **")


if __name__ == '__main__':
    unittest.main()
