#!/usr/bin/env python3
"""
Write unit tests for client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client
from client import GithubOrgClient
from typing import Dict


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
