#!/usr/bin/python3
"""Test the amenity module."""
import unittest
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
	

if __name__ == "__main__":
	unittest.main()