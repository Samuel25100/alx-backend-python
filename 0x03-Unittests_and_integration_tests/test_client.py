#!/usr/bin/env python3
"""test case for client.GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """test public_repo"""
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mock_pub:
            mock_pub.return_value = {"repos_url": 200}
            gitcl = GithubOrgClient('google')
            val = gitcl._public_repos_url
            self.assertEqual(val, 200)


if __name__ == "__main__":
    unittest.main()
