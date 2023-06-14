#!/usr/bin/python3
''' UnitTest for City '''
import unittest
import models
import os
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    ''' Test for State '''
    def test_init(self):
        self.assertEqual(State, type(State()))

    def test_state_name(self):
        Wakanda = State()
        self.assertEqual(str, type(State.name))
        self.assertIn('name', dir(State))
        self.assertNotIn('name', Wakanda.__dict__)


if __name__ == '__main__':
    unittest.main()
