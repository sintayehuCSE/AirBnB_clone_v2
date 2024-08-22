#!/usr/bin/python3
"""Test the city module."""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class Test_Review(unittest.TestCase):
    """Test the City class of the project."""

    def test_review_obj(self):
        """Check creation of City object."""
        obj = Review()
        self.assertIsInstance(obj, Review)  
    
    def test_review_place_id(self):
        """Test the type of review place_id."""
        self.assertIs(str, type(Review.place_id))

    def test_review_user_id(self):
        """Test the type of place user_id."""
        self.assertIs(str, type(Review.user_id))

    def test_review_text(self):
        """Test the type of revie text."""
        self.assertIs(str, type(Review.text))

class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

if __name__ == "__main__":
    unittest.main()