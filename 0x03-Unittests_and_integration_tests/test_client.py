#!/usr/bin/env python3
"""
Write unit tests for client.py
"""
import unittest
from unittest.mock import patch
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
