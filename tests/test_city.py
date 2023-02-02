#!/usr/bin/python3
"""class user test"""
import unittest
from models.city import City


class TestCity(unittest.Testcase):
    """class user tests"""

    def setUp(self):
        self.testCity =city()

    def test_state_id(self):
        self.assertIsInstance(self.testCity.state_id, str)

    def test_name(self):
        self.assertIsInstance(self.testCity.name, str)

