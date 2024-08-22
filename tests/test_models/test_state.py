#!/usr/bin/python3
"""Test the state module."""
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.state import State

class Test_State(unittest.TestCase):
    """Test the State class of the project."""

    def test_state_obj(self):
        """Check creation of State object."""
        obj = State()
        self.assertIsInstance(obj, State)
    
    def test_state_name(self):
        """Check the type of state name."""
        self.assertIs(str, type(State.name))

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()