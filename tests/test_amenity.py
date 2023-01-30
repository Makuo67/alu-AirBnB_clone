#!/usr/bin/python3
"""user class unittest"""
import unittest 
from models import BaseModel
from models.amenity import Amenity


class TestTheState(unittest.TestCase):
    """ class amenity tests"""

    def setUp(self):
        self.testAmenity = Amenity()

    def test_amenity(self):
        self.assertTrue(issubclass(self.testAmenity.__class__. BaseModel))

    def test_name(self):
        self.assertIsInstance(self.testAmenity.name, str)
