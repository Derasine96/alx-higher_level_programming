#!/usr/bin/python3
"""Test max_integer.py
    Usage:
        max_integer(list[...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class that tests the function"""

    def test_max_integer(self):
        """Test for maximum value"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_empty_list(self):
        """Test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test for a single integer"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test for negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicates(self):
        """Test for duplicate numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        """Test for float values"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_large_list(self):
        """Test a large list of numbers"""
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

    def test_large_numbers(self):
        """Test Large numbers"""
        self.assertEqual(max_integer([100000, 10000, 1111111, 1000]), 1111111)
        
    def test_booleans(self):
        """Test booleans"""
        self.assertTrue(max_integer([True, False]))
        self.assertTrue(max_integer([False, True]))
    
    def test_strings(self):
        """Test list of strings"""
        list1 = ["hamza", "code", "programming", "bugs"]
        self.assertEqual(max_integer(list1), max(list1))


if __name__ == '__main__':
    unittest.main()
