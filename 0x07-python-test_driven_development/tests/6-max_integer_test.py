#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer([1,2,3,"hi"])

    def test_one_value(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed(self):
        self.assertEqual(max_integer([99, 58, 7, 2.2, 45, 3.3, 1e5]), 1e5)

if __name__ == "__main__":
    unittest.main()