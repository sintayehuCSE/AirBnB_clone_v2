#!/usr/bin/python3
"""User Management Module. It contains User() class that inherit
    From BaseModel() class.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Defines the User object interface for the project."""
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', back_populates='user', cascade='all, delete, delete-orphan')
    else:  # if Storage env is FileStorage
        email = ""
        password = ""
        first_name = ""
        last_name = ""
