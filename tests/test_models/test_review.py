#!/usr/bin/python3
''' UnitTest for City '''
import unittest
import models
import os
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    ''' Test for Review '''
    def test_init(self):
        self.assertEqual(Review, type(Review()))

    def test_review_place_id(self):
        Jitters = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn('place_id', dir(Review()))
        self.assertNotIn('place_id', Jitters.__dict__)

    def test_reveiw_user_id(self):
        Jitters = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn('user_id', dir(Review()))
        self.assertNotIn('user_id', Jitters.__dict__)


if __name__ == '__main__':
    unittest.main()
