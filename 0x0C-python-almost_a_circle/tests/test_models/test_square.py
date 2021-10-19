#!/usr/bin/python3
"""
=============================
All tests for Class Rectangle
=============================
"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestCaseSquare(unittest.TestCase):

    def test_args(self):
        """ test different type of args """

        s_1 = Square(10, 2)
        s_2 = Square(2, 10)
        s_3 = Square(10, 2, 0, 12)

        self.assertEqual(s_1.id, 4)
        self.assertEqual(s_2.id, 5)
        self.assertEqual(s_3.id, 12)

        s1 = Square(4, 2, 1, 12)

        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

        s2 = Square(5, 7)

        self.assertEqual(s2.id, 6)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 0)

        s2.update(8, 9, 12, 13)

        self.assertEqual(s2.id, 8)
        self.assertEqual(s2.size, 9)
        self.assertEqual(s2.x, 12)
        self.assertEqual(s2.y, 13)

        s2.update(x=18, y=23)

        self.assertEqual(s2.id, 8)
        self.assertEqual(s2.size, 9)
        self.assertEqual(s2.x, 18)
        self.assertEqual(s2.y, 23)

    def test_errors(self):
        """ try different errors """

        with self.assertRaises(TypeError):
            s1 = Square("2")
            raise TypeError()

        with self.assertRaises(TypeError):
            s2 = Square(10, 2)
            s2.x = {}
            raise TypeError()

        with self.assertRaises(ValueError):
            s3 = Square(10, 2)
            s3.width = -10
            raise ValueError()

        with self.assertRaises(ValueError):
            s4 = Square(10, 2, 3, -1)
            raise ValueError()

    def test_bool(self):
        """ validate objects """

        s1 = Square(10, 2, 1, 9)
        s2 = Square(10, 2, 1, 9)

        self.assertFalse(s1 == s2)

        s3 = Square(10, 2, 1, 9)
        s3_dictionary = s3.to_dictionary()
        s4 = Square(1, 1)
        s4.update(**s3_dictionary)

        self.assertFalse(s3 == s4)

        s5 = Square(3, 5, 1)
        s5_dictionary = s5.to_dictionary()
        s6 = Square.create(**s5_dictionary)

        self.assertFalse(s5 is s6)
        self.assertFalse(s5 == s6)

        self.assertTrue(issubclass(Square, Rectangle))

    def test_type(self):
        """ validate the types """

        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_area(self):
        """ verify areas results """

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.area(), 9)
