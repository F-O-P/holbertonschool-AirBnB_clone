#!/usr/bin/python3
''' Unittest for base_model '''
import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ''' Unittest for base_model '''

    def test_save(self):
        ''' Tests that save() updates'''

        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_str(self):
        ''' Tests output of the string method'''

        base_model = BaseModel()

        output = str(base_model)

        self.assertIn(base_model.__class__.__name__, output)
        self.assertIn(base_model.id, output)
        self.assertIn(str(base_model.__dict__), output)

    def test_to_dict(self):

        base_model = BaseModel()

        result = base_model.to_dict()

        self.assertIsInstance(result, dict)

        self.assertIn('id', result)
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)

        self.assertEqual(result['__class__'], base_model.__class__.__name__)
        self.assertEqual(result['created_at'], base_model.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(result['updated_at'], base_model.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))

    def test_id(self):
        '''Test id uniqueness'''

        base_model1 = BaseModel()
        base_model2 = BaseModel()

        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_at(self):
        '''Test that current datetime is used when value is created'''

        base_model = BaseModel()
        current_time = datetime.now()
        delta = current_time - base_model.created_at

        self.assertAlmostEqual(delta.total_seconds(), 0, delta=0.001)

if __name__ == '__main__':
    unittest.main()
