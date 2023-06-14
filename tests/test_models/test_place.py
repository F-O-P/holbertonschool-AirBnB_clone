#!/usr/bin/python3
''' UnitTest for City '''
import unittest
import models
import os
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    ''' Test for Place '''
    def test_init(self):
        self.assertEqual(Place, type(Place()))

    def test_place_in_city(self):
        Jitters = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn('city_id', dir(Jitters))
        self.assertNotIn('city_id', Jitters.__dict__)

    def test_place_user_id(self):
        Jitters = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn('user_id', dir(Jitters))
        self.assertNotIn('user_id', Jitters.__dict__)


if __name__ == '__main__':
    unittest.main()
