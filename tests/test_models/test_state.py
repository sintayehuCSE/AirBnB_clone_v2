#!/usr/bin/python3
"""Test the state module."""
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


if __name__ == "__main__":
    unittest.main()