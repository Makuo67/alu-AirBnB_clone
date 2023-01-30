#!/usr/bin/python3
""" user test """
import unittest
from models import BaseModel
from models.user import User


class Testuser(unittest.TestCase):
    """ tests for user class"""

    def setup(self):
        self.testUser = User()

     def test_first_name(self):
        self.assertIsInstance(self.testUser.first_name, str)

    def test_last_name(self):
        self.assertIsInstance(self.testUser.last_name, str)

    def test_user(self):
        """Test if User class:."""
        self.assertTrue(issubclass(self.testUser.__class__, BaseModel)) 
    def test_email(self):
        """Test email."""
        self.assertIsInstance(self.testUser.email, str)

    def test_password(self):
        self.assertIsInstance(self.testUser.password, str)


if __name__ == '__main__':
    unittest.main()



