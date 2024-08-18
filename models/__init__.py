#!/usr/bin/python3
""" Initialize and packagize the models directory/folder

    Creates a link between the application and the Data Storage
    of interest i.e either FileStorage or DBStorage
"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:  # getenv('HBNB_TYPE_STORAGE') is 'FileStorage':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
