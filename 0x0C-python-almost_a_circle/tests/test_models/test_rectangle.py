#!/usr/bin/python3
"""
=============================
All tests for Class Rectangle
=============================
"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestCaseRectangle(unittest.TestCase):

    def test_args(self):
        """ test different type of args """

        r_1 = Rectangle(10, 2)
        r_2 = Rectangle(2, 10)
        r_3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r_1.id, 1)
        self.assertEqual(r_2.id, 2)
        self.assertEqual(r_3.id, 12)

        r1 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

        r2 = Rectangle(5, 7)

        self.assertEqual(r2.id, 3)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r2.update(8, 9, 12, 13)

        self.assertEqual(r2.id, 8)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 12)
        self.assertEqual(r2.x, 13)
        self.assertEqual(r2.y, 0)

        r2.update(x=18, y=23)

        self.assertEqual(r2.id, 8)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 12)
        self.assertEqual(r2.x, 18)
        self.assertEqual(r2.y, 23)

    def test_errors(self):
        """ try different errors """

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")
            raise TypeError()

        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2)
            r2.x = {}
            raise TypeError()

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 2)
            r3.width = -10
            raise ValueError()

        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, 3, -1)
            raise ValueError()

    def test_bool(self):
        """ validate objects """

        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(10, 2, 1, 9)

        self.assertFalse(r1 == r2)

        r3 = Rectangle(10, 2, 1, 9)
        r3_dictionary = r3.to_dictionary()
        r4 = Rectangle(1, 1)
        r4.update(**r3_dictionary)

        self.assertFalse(r3 == r4)

        r5 = Rectangle(3, 5, 1)
        r5_dictionary = r5.to_dictionary()
        r6 = Rectangle.create(**r5_dictionary)

        self.assertFalse(r5 is r6)
        self.assertFalse(r5 == r6)

        self.assertTrue(issubclass(Rectangle, Base))

    def test_type(self):
        """ validate the types """

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_area(self):
        """ verify areas results """

        r_4 = Rectangle(3, 2, 0, 0, 23)
        self.assertEqual(r_4.area(), 6)

        r_5 = Rectangle(2, 10, 0, 0, 23)
        self.assertEqual(r_5.area(), 20)

        r_6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r_6.area(), 56)
