#!/usr/bin/python3
"""Test the User module"""
import unittest
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


if __name__ == "__main__":
    unittest.main()
