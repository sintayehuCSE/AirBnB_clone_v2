#!/usr/bin/python3
"""The review Module: Holds Review class of the project."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Define the Review Class."""
    __tablename__ = 'reviews'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        place = relationship('Place', back_populates='reviews')
        user = relationship('User', back_populates='reviews')
    else:
        place_id = ""
        user_id = ""
        text = ""
