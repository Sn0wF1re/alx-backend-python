#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class
that inherits from unittest.TestCase
"""
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Write unit tests
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
