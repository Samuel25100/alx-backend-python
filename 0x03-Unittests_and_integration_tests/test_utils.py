#!/usr/bin/env python3
"""test for utils.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nest_map, path):
        """check access_nested_map if raise keyerror correctly"""
        self.assertRaises(KeyError, access_nested_map, nest_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, url, out, mock_get):
        """test get_json method that fetch from url"""
        mock_get.return_value.json.return_value = out
        self.assertEqual(get_json(url), out)


if __name__ == "__main__":
    unittest.main()
