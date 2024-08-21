#!/usr/bin/python3
"""The amenity module: Holds Amenity class of the project."""
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Defines the amenity class."""
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        places = relationship('Place', secondary=place_amenity, back_populates='amenities')
    else:  # If Storage env is FileStorage
        name = ""
