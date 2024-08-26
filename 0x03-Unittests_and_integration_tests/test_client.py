#!/usr/bin/env python3
"""test case for client.GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
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
        cls.mock = patch('requests.get')
        cls.mock_get = cls.mock.start()

        def sideEffect(url):
            resp = Mock()
            if url == "https://api.github.com/org_payload":
                resp.json.return_value = cls.org_payload.json()
                return resp
            elif url == "https://api.github.com/orgs/repos_payload":
                resp.json.return_value = cls.repos_payload.json()
                return resp
            elif url == "https://api.github.com/repos_payload":
                resp.json.return_value = cls.expected_repos.json()
                return resp
            elif url == "https://api.github.com/apache2_repos":
                resp.json.return_value = cls.apache2_repos.json()
                return resp
            elif "https://api.github.com/orgs/" in url:
                data = {}
                data["repos_url"] = cls.repos_payload
                resp.json.return_value = data
                return resp
            return None
        cls.mock_get.side_effect = sideEffect

    def test_public_repos(self):
        """test public_repos in integration test"""
        gitcl = GithubOrgClient("google")
        val = gitcl.public_repos()
        print("val:", val)
        self.assertEqual(val[0], "cpp-netlib")
        cls.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """test public_repos with license"""
        gitcl = GithubOrgClient("google")
        val = gitcl.public_repos("apache-2.0")
        self.assertEqual(val[0], "cpp-netlib")
        cls.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """tear down setted up class"""
        cls.mock_get.stop()


if __name__ == "__main__":
    unittest.main()
