#!/usr/bin/python3
"""Test the city module."""
import unittest
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


if __name__ == "__main__":
    unittest.main()