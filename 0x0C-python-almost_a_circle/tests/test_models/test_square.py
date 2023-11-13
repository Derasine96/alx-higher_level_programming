#!/usr/bin/python3
"""Unittest module for Square class"""
import unittest
import sys
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_init(self):
        """Test initialization of Square."""
        square = Square(1, 1, 1)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 1)

    def test_set_side(self):
        """Test setting side length of Square."""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_area(self):
        """Test the area method of Square."""
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_initialization_with_specific_values(self):
        """Test initializing a square with specific values."""
        square = Square(3, 1, 2, 99)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 99)

    def test_exception_handling_invalid_size(self):
        """Test initializing a square with invalid values for size."""
        with self.assertRaises(ValueError) as context:
            square = Square(-3)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(TypeError) as context:
            square = Square("invalid")
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_exception_handling_invalid_coordinates(self):
        """Test initializing a square with invalid values for coordinates."""
        with self.assertRaises(ValueError) as context:
            square = Square(3, -1, 2, 99)
            self.assertEqual(str(context.exception), "x must be >= 0")
            square = Square(3, 2, -1, 99)
            self.assertEqual(str(context.exception), "y must be >= 0")

    def test_str_representation(self):
        """Test the string representation (__str__) of Square."""
        square = Square(3, 1, 2, 99)
        expected_output = "[Square] (99) 1/2 - 3"
        self.assertEqual(expected_output, str(square))

    def test_update_method(self):
        """Test using the update method with different
            combinations of arguments and keyword arguments."""
        square = Square(3, 1, 2, 99)
        square.update(10, 5, x=7, y=8)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)
        # Testing when no argument is passed to update method
        square.update()
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)
        # Testing when only one argument is passed to update method
        square.update(6)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)
        # Testing when only two arguments are passed to update method
        square.update(4, 7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method and ensure that
            it returns the correct dictionary representation."""
        square = Square(3, 1, 2, 99)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 99, 'size': 3, 'x': 1, 'y': 2}
        self.assertEqual(square_dict, expected_dict)

    def test_create_method(self):
        """Test the create method by providing a dictionary and
            verifying the object is created with the correct attributes."""
        square_dict = {'id': 10, 'size': 5, 'x': 7, 'y': 8}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_edge_cases(self):
        """Test edge cases."""
        square_size_1 = Square(1, 4, 5)
        self.assertEqual(square_size_1.size, 1)
    # Test updating attributes with extreme values
        square = Square(3, 1, 2, 99)
        square.update(10, 500, y=800, x=700)
        self.assertEqual(square.size, 500)
        self.assertEqual(square.x, 700)
        self.assertEqual(square.y, 800)

    def test_display_method_output(self):
        """Test the display method output."""
        square = Square(3, 4, 10, 2)
        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            square.display()
            sys.stdout = sys.__stdout__
        expected_output = "    ###\n    ###\n    ###\n    ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    if __name__ == "__main__":
        unittest.main()
