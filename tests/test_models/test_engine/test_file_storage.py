#!/usr/bin/python3
''' UnitTest for FileStorage '''
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    ''' Test for FileStorage '''

    def setUp(self):
        ''' Set up the test environment '''
        self.file_storage = FileStorage()
        self.file_path = self.file_storage._FileStorage__file_path
        self.objects = self.file_storage._FileStorage__objects

    def tearDown(self):
        ''' Clean up the test environment '''
        self.file_storage._FileStorage__objects = {}

    def test_file_storage_new(self):
        ''' Test the new method of FileStorage '''
        test_object = BaseModel()
        self.file_storage.new(test_object)
        objects = self.file_storage.all()
        self.assertIn(test_object, objects.values())

    def test_file_storage_all(self):
        ''' Test the all method of FileStorage '''
        test_object = BaseModel()
        self.file_storage.new(test_object)
        objects = self.file_storage.all()
        self.assertIn(test_object, objects.values())

    def test_file_storage_save(self):
        ''' Test the save method of FileStorage '''
        test_object = BaseModel()
        self.file_storage.new(test_object)
        self.file_storage.save()
        with open(self.file_path, 'r') as read_later:
            reading_now = json.load(read_later)
            self.assertEqual(test_object.to_dict(), reading_now['BaseModel.{}'.format(test_object.id)])

    def test_file_storage_reload(self):
        ''' Test the reload method of FileStorage '''
        test_object = BaseModel()
        self.file_storage.new(test_object)
        self.file_storage.save()
        self.file_storage._FileStorage__objects = {}
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertEqual(test_object.to_dict(), objects['BaseModel.{}'.format(test_object.id)].to_dict())

    def test_file_storage_file_path(self):
        ''' Test the file_path attribute of FileStorage '''
        self.assertIsInstance(self.file_storage._FileStorage__file_path, str)


if __name__ == '__main__':
    unittest.main()

