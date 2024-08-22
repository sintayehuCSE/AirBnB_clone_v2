#!/usr/bin/python3
"""Test the User module"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class Test_User(unittest.TestCase):
    """Test the status of User class."""
    def test_user_obj(self):
        """Test creation of User Object."""
        u = User()
        self.assertIsInstance(u, User)

    def test_user_email(self):
        """Test the type of user email."""
        self.assertIs(str, type(User.email))

    def test_user_password(self):
        """Test the type of user password."""
        self.assertIs(str, type(User.password))

    def test_user_first_name(self):
        """Test the type of user first name."""
        self.assertIs(str, type(User.first_name))

    def test_user_last_name(self):
        """Test the type of User last name."""
        self.assertIs(str, type(User.last_name))

class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

if __name__ == "__main__":
    unittest.main()
