#!/usr/bin/python3
"""
========================
All tests for Class Base
========================
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestCaseBase(unittest.TestCase):

    def test_args(self):
        """ test differents types of args """

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(-3)
        b7 = Base('a')
        b8 = Base("hello")
        b9 = Base(None)
        b10 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -3)
        self.assertEqual(b7.id, 'a')
        self.assertEqual(b8.id, "hello")
        self.assertEqual(b9.id, 5)
        self.assertEqual(b10.id, 6)

        self.assertTrue(type(b10), Base)

    def test_to_json_string(self):
        """ try func to_json_string """

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertTrue(type(dictionary), dict)
        self.assertTrue(type(json_dictionary), str)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        """ check if the file was saved correctly """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.exists('Rectangle.json'))

    def test_from_json_string(self):
        """ check if the func can load the json string """

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(list_output), list)
        self.assertTrue(type(list_output[0]), Rectangle)

        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_create(self):
        """ check if can create the instances """

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertTrue(type(r1), Rectangle)
        self.assertTrue(type(r2), Rectangle)
        self.assertTrue(type(r1_dictionary), dict)

    def test_load_from_file(self):
        """ check the load to a list of instances """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertTrue(os.path.exists('Rectangle.json'))
        self.assertTrue(type(r1), Rectangle)
        self.assertTrue(type(r2), Rectangle)
        self.assertTrue(type(list_rectangles_input), list)
        self.assertTrue(type(list_rectangles_input[0]), Rectangle)
        self.assertTrue(type(list_rectangles_input[1]), Rectangle)
        self.assertTrue(type(list_rectangles_output), list)
        self.assertTrue(type(list_rectangles_output[0]), Rectangle)
        self.assertTrue(type(list_rectangles_output[1]), Rectangle)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertTrue(os.path.exists('Square.json'))
        self.assertTrue(type(s1), Square)
        self.assertTrue(type(s2), Square)
        self.assertTrue(type(list_squares_input), list)
        self.assertTrue(type(list_squares_input[0]), Square)
        self.assertTrue(type(list_squares_input[1]), Square)
        self.assertTrue(type(list_squares_output), list)
        self.assertTrue(type(list_squares_output[0]), Square)
        self.assertTrue(type(list_squares_output[1]), Square)
