#!/usr/bin/env python3
""" Test utils
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """ Tests utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any):
        """ Test the return value of access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence, expected: Any):
        """ Test the exceptions raised by access_nested_map """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected}'")


class TestGetJson(unittest.TestCase):
    """Test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get):
        """ Set up the mock response to return test_payload
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # call the function under test
        result = get_json(test_url)

        # Assert the request.gget was called once with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the response from get_json matches the expected
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize
    """
    def test_memoize(self):
        """ tests if memoize works
        """
        class TestClass:
            """ Test class with a memoized property
            """
            def a_method(self):
                '''Returns 42'''
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method()

        # Use patch to mock a_method
        with patch.object(
                TestClass,
                'a_method',
                return_value=42) as mock_method:
            # Instantiate the class
            test_instance = TestClass()

            # Access the memoized property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Assert that the results are as expected
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Assert a_method was only called once
            mock_method.assert_called_once()
