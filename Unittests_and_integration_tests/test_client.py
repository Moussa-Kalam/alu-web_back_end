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


if __name__ == '__main__':
    unittest.main()
