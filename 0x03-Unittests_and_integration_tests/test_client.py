#!/usr/bin/env python3
"""
Write unit tests for client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client
from client import GithubOrgClient


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
