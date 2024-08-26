#!/usr/bin/env python3
"""test case for client.GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from parameterized import parameterized_class
from fixtures import TEST_PAYLOAD
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_k, result):
        """test has_license"""
        val = GithubOrgClient.has_license(repo, license_k)
        self.assertEqual(val, result)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for client"""

    @classmethod
    def setUpClass(cls):
        """setUp class for test"""
        cls.mock_get = patch('requests.get')
        cls.mock_get.start()

        def sideEffect(url):
            if url == "https://api.github.com/org_payload":
                return json(cls.org_payload)
            elif url == "https://api.github.com/repos_payload":
                return json(cls.repos_payload)
            elif url == "https://api.github.com/repos_payload":
                return json(cls.expected_repos)
            elif url == "https://api.github.com/apache2_repos":
                return json(cls.apache2_repos)
            return None
        cls.mock_get.side_effect = sideEffect

    @classmethod
    def tearDownClass(cls):
        """tear down setted up class"""
        cls.mock_get.stop()


if __name__ == "__main__":
    unittest.main()
