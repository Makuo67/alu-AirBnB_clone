#!/usr/bin/python3
"""
Tests for Amenity Module
"""

import unittest
import pep8
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unit Tests"""

    def setUp(self):
        """setup"""
        self.amenity = Amenity()

    def test_amenity_init(self):
        """
        1. tests if new instance of the class 'Amenity'
        is created correctly
        2. tests if 'name' attribute of the Amenity
        object is an instance of the str class
        3. tests if the initial value of 'name'
        attribute is an empty string
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    def test_name_setter(self):
        """
        1. tests if 'name' attribute can
        be set to a new value correctly
        """
        self.amenity.name = "Internet"
        self.assertEqual(self.amenity.name, "Internet")

    def test_name_getter(self):
        """
        1. tests if 'name' attribute gets the
        correct value
        """
        self.amenity.name = "Electricity"
        self.assertEqual(self.amenity.name, "Electricity")

    def test_amenity_pep8(self):
        """test if amenity.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test for PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()