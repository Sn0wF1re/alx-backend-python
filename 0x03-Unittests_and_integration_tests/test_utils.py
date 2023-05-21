#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class
that inherits from unittest.TestCase
"""
import unittest
from utils import access_nested_map, get_json
from typing import Mapping, Sequence
from parameterized import parameterized
import requests
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Write unit tests for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        test that the method returns what it is supposed to
        """
        resp = access_nested_map(nested_map, path)
        self.assertEqual(resp, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        test that a KeyError is raised
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Write unit tests for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: dict, mock_get) -> None:
        """
        test that utils.get_json returns the expected result
        """
        mock_get.return_value.json.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)
        mock_get.assert_called_once_with(test_url)
