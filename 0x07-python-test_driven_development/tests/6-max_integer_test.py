#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

"""
    Unittest for max_integer([..])
"""


class TestMaxInteger(unittest.TestCase):
    """ class """

    def test_last(self):
        """ test """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_first(self):
        """ test """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_middle(self):
        """ test """
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

    def test_list_type(self):
        """ test """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "hi"])

    def test_list_type(self):
        """ test """
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_type(self):
        """ test """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "hi"])

    def test_str(self):
        """ test """
        self.assertEqual(max_integer("hi man"), "n")

    def test_one_value(self):
        """ test """
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        """ test """
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """ test """
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        """ test """
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed(self):
        """ test """
        self.assertEqual(max_integer([99, 58, 7, 2.2, 45, 3.3, 1e5]), 1e5)

    def test_tuple(self):
        """ test """
        self.assertEqual(max_integer((99, 58, 7, 2.2, 45, 3.3, 1e5)), 1e5)


if __name__ == "__main__":
    unittest.main()
