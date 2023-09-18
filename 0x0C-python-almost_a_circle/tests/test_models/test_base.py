#!/usr/bin/python3
"""
Defines unittests for base.py.

Unittest classes:

"""
import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.Testcase):
    """ Unittests to test Base class instantiation """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_four_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b4.id - 3)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)


if __name__ == "__main__":
    unittest.main()
