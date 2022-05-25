#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_typical_cases(self):
        self.assertEqual(max_integer([3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([-7, -1, -9]), -1)
        self.assertEqual(max_integer([2.0, 3.14, 6.19]), 6.19)
        self.assertEqual(max_integer(['A', 'B', 'C']), 'C')
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))
        self.assertEqual(max_integer([True, False, 1, 2, 3]), 3)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, 6)
        self.assertRaises(TypeError, max_integer, ["a", "b", 10])
        self.assertRaises(TypeError, max_integer, [None, 1, 2])
        self.assertRaises(TypeError, max_integer, {5, 8, 0, 99})

if __name__ == '__main__':
    unittest.main()
