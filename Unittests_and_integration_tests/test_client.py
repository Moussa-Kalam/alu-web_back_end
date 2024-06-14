#!/usr/bin/env python3
""" Test for client.py """

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ Test org """
        mock.return_value = {"org": org_name}
        org = GithubOrgClient("test")
        self.assertEqual(org.org, mock.return_value)
        mock.assert_called_once()

    @patch("client.GithubOrgClient.org",
           {"repos_url": "https://api.github.com/orgs/izzy"})
    def test_public_repos_url(self):
        """ Test public repos url """
        org = GithubOrgClient("izzy")
        self.assertEqual(
            org._public_repos_url,
            "https://api.github.com/orgs/izzy")

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """ Test public repos """
        mock.return_value = [{"name": "testing"}, {"name": "todo-app"}]
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          return_value="https://api.github.com/orgs/izzy"):
            org = GithubOrgClient("izzy")
            self.assertEqual(org.public_repos(), ["testing", "todo-app"])
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, has):
        """ Test License """
        has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_license, has)


if __name__ == '__main__':
    unittest.main()
