#!/usr/bin/python3
"""Test the place module."""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class Test_Amenity(unittest.TestCase):
    """Test the Place class of the project."""

    def test_place_obj(self):
        """Check creation of Place object."""
        obj = Place()
        self.assertIsInstance(obj, Place)
    
    def test_place_city_id(self):
        """Check the type of Place city_id."""
        self.assertIs(str, type(Place.city_id))

    def test_place_user_id(self):
        """Check the type of place user_id."""
        self.assertIs(str, type(Place.user_id))

    def test_place_name(self):
        """Test the type of place name."""
        self.assertIs(str, type(Place.name))
    
    def test_place_description(self):
        """Test the type of place description."""
        self.assertIs(str, type(Place.description))

    def test_place_number_rooms(self):
        """Test the type of place number_rooms."""
        self.assertIs(int, type(Place.number_rooms))

    def test_place_number_bathrooms(self):
        """Test the type of place number_bathrooms."""
        self.assertIs(int, type(Place.number_bathrooms))

    def test_place_max_guest(self):
        """Test the type of place max_guest."""
        self.assertIs(int, type(Place.max_guest))

    def test_place_price_by_night(self):
        """Test the type of place price_by_night."""
        self.assertIs(int, type(Place.price_by_night))

    def test_place_latitude(self):
        """Test the type of place latitude."""
        self.assertIs(float, type(Place.latitude))

    def test_place_longitude(self):
        """Test the type of place longitude."""
        self.assertIs(float, type(Place.longitude))
    
    def test_place_amenity_id(self):
        """Test the type of place amenity_id."""
        self.assertIs(list, type(Place.amenity_ids))
 
class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()