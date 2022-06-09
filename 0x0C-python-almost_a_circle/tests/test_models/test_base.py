#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def test_normal_id_cases(self):
        self.assertEqual(Base(8).id, 8)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(-10).id, -10)
        self.assertEqual(Base("Hello").id, "Hello")
        self.assertEqual(Base(False).id, False)
