#!/usr/bin/python3
"""
Test for storage engine class.
"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models import storage


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage Engine class."""

    def reset_storage(self):
        """Reset the file after updating it with test method."""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    def test_obje_creation(self):
        """Check cretion of Storage object."""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_FileStorage__objects(self):
        """Test the type of __object container holding live objecct."""
        self.assertIs(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage__file_path(self):
        """Test the type of __file_path of Storage engine."""
        self.assertIs(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_methods(self):
        """check presence of method in Engine file."""
        live_dict = storage.all()
        storage.save()
        live_obj = storage.reload()
        file_dict = storage.all()
        self.assertEqual(len(live_dict), len(file_dict))
        self.reset_storage()

    def test_method_documented(self):
        """Check if method of thee class are documented."""
        self.assertIsNotNone(FileStorage.all.__dict__)
        self.assertIsNotNone(FileStorage.new.__dict__)
        self.assertIsNotNone(FileStorage.save.__dict__)
        self.assertIsNotNone(FileStorage.reload.__dict__)


if __name__ == "__main__":
    unittest.main()
