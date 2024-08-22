#!/usr/bin/python3
"""Test the city module."""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class Test_City(unittest.TestCase):
    """Test the City class of the project."""

    def test_city_obj(self):
        """Check creation of City object."""
        obj = City()
        self.assertIsInstance(obj, City)
    
    def test_city_name(self):
        """Check the type of City name."""
        self.assertIs(str, type(City.name))
    
    def test_city_state_id(self):
        """Test the state Id in City class."""
        self.assertIs(str, type(City.state_id))

class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()