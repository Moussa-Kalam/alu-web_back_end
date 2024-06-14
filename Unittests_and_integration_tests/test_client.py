#!/usr/bin/env python3
""" Test for client.py """

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, Mock
import requests
from fixtures import TEST_PAYLOAD


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
        """ test public repos """
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
        """ Test license """
        has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_license, has)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test integration """

    @classmethod
    def setUpClass(cls):
        """ Setup class """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public repos """
        org = GithubOrgClient("test")
        repos = org.public_repos()
        payload = self.repos_payload
        self.assertEqual(repos, self.expected_repos)
        self.assertEqual(payload, self.repos_payload)


if __name__ == '__main__':
    unittest.main()