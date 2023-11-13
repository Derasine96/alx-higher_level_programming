#!/usr/bin/python3
"""Unittest module for Rectangle class"""
import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_init(self):
        """Test initialization of Rectangle."""
        rectangle = Rectangle(1, 1, 1, 1)
        self.assertEqual(1, rectangle.width)
        self.assertEqual(1, rectangle.height)
        self.assertEqual(1, rectangle.x)
        self.assertEqual(1, rectangle.y)

    def test_set_dimensions(self):
        """Test setting dimensions of a Rectangle."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(5, rectangle.width)
        self.assertEqual(10, rectangle.height)

    def test_area(self):
        """Test the area method of Rectangle."""
        rectangle = Rectangle(4, 6)
        self.assertEqual(24, rectangle.area())

    def test_str_representation(self):
        """Test the string representation (__str__) of Rectangle."""
        rectangle = Rectangle(3, 4, 1, 2, 99)
        expected_output = "[Rectangle] (99) 1/2 - 3/4"
        self.assertEqual(expected_output, str(rectangle))

    def test_initialization_with_specific_values(self):
        """Test initializing a rectangle with specific values."""
        rectangle = Rectangle(3, 4, 1, 2, 99)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 99)

    def test_exception_handling_invalid_width_height(self):
        """Test initializing a rectangle with
            invalid values for width and height."""
        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(-3, 4)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle(4, "invalid")
        self.assertEqual(
            str(context.exception), "height must be an integer")

    def test_update_method(self):
        """Test using the update method with different
            combinations of arguments and keyword arguments."""
        rectangle = Rectangle(3, 4, 1, 2, 99)
        rectangle.update(10, 5, 6, y=8, x=7)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when no argument is passed to update method
        rectangle.update()
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when only one argument is passed to update method
        rectangle.update(10)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when all arguments are passed in reverse order
        rectangle.update(y=8, x=7, id=10, height=6, width=5)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when only two arguments are passed to update method
        rectangle.update(7, 8)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when three arguments are passed to update method
        rectangle.update(7, 8, 9)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 9)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)
        # Testing when four arguments are passed to update method
        rectangle.update(7, 8, 9, 10)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 9)
        self.assertEqual(rectangle.x, 10)
        self.assertEqual(rectangle.y, 8)
        # Testing when five arguments are passed to update method
        rectangle.update(7, 8, 9, 10, 11)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 9)
        self.assertEqual(rectangle.x, 10)
        self.assertEqual(rectangle.y, 8)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method and ensure that it
            returns the correct dictionary representation."""
        rectangle = Rectangle(3, 4, 1, 2, 99)
        rect_dict = rectangle.to_dictionary()
        expected_dict = {'id': 99, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(rect_dict, expected_dict)

    def test_create_method(self):
        """Test the create method by providing a dictionary and
            verifying the object is created with the correct attributes."""
        rect_dict = {'id': 10, 'width': 5, 'height': 6, 'x': 7, 'y': 8}
        rectangle = Rectangle.create(**rect_dict)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)

    def test_create_method(self):
        """Test the create method by providing a dictionary and
            verifying the object is created with the correct attributes."""
        rect_dict = {'id': 10, 'width': 5, 'height': 6, 'x': 7, 'y': 8}
        rectangle = Rectangle.create(**rect_dict)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)

    def test_edge_cases(self):
        """Test edge cases."""
        rectangle_width_1 = Rectangle(1, 4)
        rectangle_height_1 = Rectangle(3, 1)
        self.assertEqual(rectangle_width_1.width, 1)
        self.assertEqual(rectangle_height_1.height, 1)
    # Test updating attributes with extreme values
        rectangle = Rectangle(3, 4, 1, 2, 99)
        rectangle.update(10, 500, 600, y=800, x=700)
        self.assertEqual(rectangle.width, 500)
        self.assertEqual(rectangle.height, 600)
        self.assertEqual(rectangle.x, 700)
        self.assertEqual(rectangle.y, 800)

    def test_display_method_output(self):
        """Test the display method output."""
        rectangle = Rectangle(3, 4, 1, 2, 99)
        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            rectangle.display()
            sys.stdout = sys.__stdout__
        expected_output = "    ###\n    ###\n    ###\n    ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    if __name__ == "__main__":
        unittest.main()
