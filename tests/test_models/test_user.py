import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' Class reps a user and inherits from basemodel'''

    def test_attributes(self):
        ''' Initialize new instance of User class'''

        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        user.email = "john@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_inheritance(self):
        '''Tests if user inherits from BaseModel'''
        user = User()

        self.assertIsInstance(user, BaseModel)

if __name__ == '__main__':
    unittest.main()
