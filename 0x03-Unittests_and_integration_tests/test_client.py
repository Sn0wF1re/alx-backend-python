#!/usr/bin/env python3
"""
Write unit tests for client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Write tests for GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock):
        """
        test that GithubOrgClient.org returns the correct value
        """
        test = GithubOrgClient(org)
        resp = test.org
        self.assertEqual(resp, mock.return_value)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """
        unit-test GithubOrgClient._public_repos_url
        """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": 89}
            testOrg = GithubOrgClient('holberton')
            test_result = testOrg._public_repos_url
            self.assertEqual(test_result,
                             mock_org.return_value.get("repos_url"))
            mock_org.assert_called_once()

    @patch("client.get_json", return_value=[{"name": "Solana"},
                                            {"name": "alx"},
                                            {"name": "Ethereum"}])
    def test_public_repos(self, mock_repo):
        """
        unit-test GithubOrgClient.public_repos
        """
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test = GithubOrgClient('solana')
            result = test.public_repos()
            for i in range(3):
                self.assertIn(mock_repo.return_value[i]["name"], result)
            mock_repo.assert_called_once()
            mock_pub.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected) -> None:
        """
        unit-test GithubOrgClient.has_license
        """
        instance = GithubOrgClient('solana')
        hasLicense = instance.has_license(repo, license_key)
        self.assertEqual(hasLicense, expected)


def get_requests(*args, **kwargs):
    """
    Mock requests.get
    """
    class MockResp:
        """
        Mock response
        """
        def __init__(self, json_data):
            """
            initialize class instance
            """
            self.json_data = json_data

        def json(self):
            """
            return the json data
            """
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResp(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResp(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """
        mock requests.get to return example payloads found in the fixtures
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=get_requests)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Unit test public_repos() without license
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Unit test public_repos() with license
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)
