#!/usr/bin/python3
""" test for user class"""
import unittest
from models.state import State
from models import BaseModel


class TestState(unittest.TestCase):
    """ tests for user"""

    def setUp(self):
        self.test.State = State()

    def testState(self):
        self.assertTrue(issubclass(self.testState.__class__, BaseModel))

    def test_name(self):
        self.assertIsInstance(self.testState.name, str)


if __name__ == "__main__":
    unittest.main()
