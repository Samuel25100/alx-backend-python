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

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """test public_repos"""
        mock_get.return_value = [{"name": "repo_name1"},
                                 {"name": "repo_name2"}]
        with patch.object(GithubOrgClient, '_public_repos_url') as mock_pub:
            gitcl = GithubOrgClient('google')
            mock_pub.return_value = 200
            val = gitcl.public_repos()
            url = gitcl._public_repos_url()
            self.assertEqual(val, ["repo_name1", "repo_name2"])
            mock_get.assert_called_once()
            mock_pub.assert_called_once()


if __name__ == "__main__":
    unittest.main()
