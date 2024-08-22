#!/usr/bin/python3
"""Test the amenity module."""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity

class Test_Amenity(unittest.TestCase):
	"""Test the Amenity class of the project."""

	def test_amenity_obj(self):
		"""Check creation of Amenity object."""
		obj = Amenity()
		self.assertIsInstance(obj, Amenity)
	
	def test_amenity_name(self):
		"""Check the type of Amenity name."""
		self.assertIs(str, type(Amenity.name))

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == "__main__":
	unittest.main()