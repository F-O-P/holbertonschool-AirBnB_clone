#!/usr/bin/python3
''' Unittest for base_model '''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Unittest for base_model '''

    def test_save(self):

        self.assertTrue(self.updated_at != self.created_at)
    
if __name__ == '__main__':
    unittest.main()
