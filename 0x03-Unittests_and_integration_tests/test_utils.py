#!/usr/bin/env python3
"""test for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """untils file test case"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nest_map, path, expected):
        """use above parameters to make test for access_nested_map method"""
        self.assertEqual(access_nested_map(nest_map, path), expected)


if __name__ == "__main__":
    unittest.main()
