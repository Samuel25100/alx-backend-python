#!/usr/bin/env python3
"""test case for client.GithubOrgClient"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    """test github api"""

    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json', return_value={"stat": "200"})
    def test_org(self, org_nm, mock_get):
        """test GithubOrgClient.org"""
        gitcl = GithubOrgClient(org_nm)
        val = gitcl.org
        self.assertEqual(val, {"stat": "200"})
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
