#!/usr/bin/python3
''' Unittest for base_model '''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Unittest for base_model '''

    def test_save(self):
        ''' Tests that save() updates'''

        base_model = BaseModel()

        initial_updated_at = base_model.updated_at

        base_model.save()

        updated_updated_at = base_model.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)

if __name__ == '__main__':
    unittest.main()
