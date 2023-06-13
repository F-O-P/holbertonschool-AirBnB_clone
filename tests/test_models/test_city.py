#!/usr/bin/python3
''' UnitTest for City '''
import unittest
import models
import os
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):
    ''' Test for City '''
    def test_init(self):
        self.assertEqual(City, type(City()))
    
    def test_city_state_id(self):
        Central_City = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn('state_id', dir(Central_City))
        self.assertNotIn('state_id', Central_City.__dict__)

if __name__ == '__main__':
    unittest.main()
