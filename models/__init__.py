#!/usr/bin/python3
"""Initialize and packagize the models directory/folder"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
