#!/usr/bin/python3
"""class user unittest"""
import unittest
from models import BaseModel
from models.place import place


class TestPlace(unittest.TestCase):
    """user class tests"""

     def setUp(self):
        self.testPlace = Place()

    def testPlace(self):
        self.assertTrue(issubclass(self.testPlace.__class__, BaseModel))

    def test_city_id(self):
        self.assertIsInstance(self.testPlace.city_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.testPlace.user_id, str)

    def test_name(self):
        self.assertIsInstance(self.testPlace.name, str)

    def test_description(self):
        self.assertIsInstance(self.testPlace.description, str)

    def test_number_rooms(self):
        self.assertIsInstance(self.testPlace.number_rooms, int)

    def test_number_bathrooms(self):
        self.assertIsInstance(self.testPlace.number_bathrooms, int)

    def test_max_guest(self):
        self.assertIsInstance(self.testPlace.max_guest, int)

    def test_price_by_night(self):
        self.assertIsInstance(self.testPlace.price_by_night, int)

    def test_latitude(self):
        self.assertIsInstance(self.testPlace.latitude, float)

    def test_longitude(self):
        self.assertIsInstance(self.testPlace.longitude, float)

    def test_amenity_ids(self):
        self.assertIsInstance(self.testPlace.amenity_ids, list)
