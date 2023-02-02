#!/usr/bin/python3
"""class user unittest"""
import unittest
from models import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """user class tests"""

     def setUp(self):
        self.testReview = Review()

    def testState(self):
        self.assertTrue(issubclass(self.testReview.__class__, BaseModel))

    def test_place_id(self):
        self.assertIsInstance(self.testReview.place_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.testReview.user_id, str)

    def test_text(self):
        self.assertIsInstance(self.testReview.text, str)
