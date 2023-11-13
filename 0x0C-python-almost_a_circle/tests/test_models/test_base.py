#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests the Base class."""

    def setUp(self):
        self.test = Base()

    def tearDown(self):
        del self.test

    def test_pep8_model(self):
        """Tests for pep8 model"""
        file_size = os.stat("models/__init__.py").st_size / 1024
        self.assertAlmostEqual(file_size, 65.79, places=2,
                               msg="File size is not right!")

    def test_pep8_tests(self):
        """Tests for pep8 tests"""
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_docstring(self):
        """Checks if docstrings are defined correctly."""
        self.assertTrue(
            inspect.getdoc(Rectangle.__init__) and
            inspect.getdoc(Square.__init__)
        ) is not None, "Missing docstring in file!"

    def test_init(self):
        """Checks that a new instance of Base has no attributes."""
        with self.assertRaises(AttributeError) as context:
            self.test.__dict__['name'] = 'Chidera'
        self.assertTrue('\'Base\' object has no attribute \'name\''
                        in str(context.exception))

    def test_setattr(self):
        """Checks that setting an attribute raises AttributeError."""
        with self.assertRaises(AttributeError) as context:
            self.test.name = 'Chidera'
        self.assertTrue('can\'t set attribute' in str(context.exception))

    def test_get_shape(self):
        """Checks that get_shape returns None when there is no shape."""
        self.assertIsNone(self.test.get_shape())

    def test_add_shape(self):
        """Checks that add_shape adds shapes to the list."""
        rectangle1 = Rectangle(5, 6)
        square2 = Square(7)
        self.test.add_shape(rectangle1)
        self.test.add_shape(square2)
        self.assertEqual(len(self.test._shapes), 2)
        self.assertIn(rectangle1, self.test._shapes)
        self.assertIn(square2, self.test._shapes)

    def test_id(self):
        """Test check for id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_rectangle(self):
        """Test check for rectangle"""
        R1 = Rectangle(4, 5, 6)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_square(self):
        """Test check for square creation"""
        S1 = Square(44, 55, 66, 77)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_file_rectangle(self):
        """Test check if file loads from rectangle"""
        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        """Test check if file loads from square"""
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)

    def test_from_json_string(self):
        """Test check from json string"""
        s = '{"name": "test", "type": "Rectangle",  "width": 20, "height": 30}'
        r = Rectangle.from_json_string(s)
        self.assertIsInstance(r, Rectangle)
        self.assertTrue(hasattr(r, '__dict__'))
        self.assertIn('name', r.__dict__.keys())
        self.assertIn('type', r.__dict__.keys())
        self.assertIn('width', r.__dict__.keys())
        self.assertIn('height', r.__dict__.keys())
        self.assertEqual(r.name, 'test')
        self.assertEqual(r.type, 'Rectangle')
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)

    def test_from_json_list(self):
        """Test check from json list of rectangles and squares"""
        s = ('[{"name": "test", "type": "Rectangle", "width": 20,'
             '{"height": 30}, {"name": "test2", "type": "Square"}]')
        lR = Rectangle.from_json_list(s)
        self.assertIsInstance(lR, list)
        self.assertEqual(len(lR), 2)
        for i in range(len(lR)):
            self.assertIsInstance(lR[i], Rectangle)
            self.assertTrue(hasattr(lR[i], '__dict__'))
            self.assertIn('name', lR[i].__dict__.keys())
            self.assertIn('type', lR[i].__dict__.keys())
            self.assertIn('width', lR[i].__dict__.keys())
            self.assertIn('height', lR[i].__dict__.keys())
            self.assertEqual(lR[i].name, 'test')
            self.assertEqual(lR[i].type, 'Rectangle')
            self.assertEqual(lR[i].width, 20)
            self.assertEqual(lR[i].height, 30)
            self.assertEqual(lR[i].side, None)


if __name__ == "__main__":
    # Run all tests if this file was run directly
    unittest.main()
