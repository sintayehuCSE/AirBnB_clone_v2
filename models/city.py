#!/usr/bin/python3
"""The city Module: Holds City class for the Project."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Define the City class of the project."""
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
        places = relationship('Place', back_populates='cities',
                              cascade='all, delete, delete-orphan')
    else:  # getenv('HBNB_TYPE_STORAGE') is 'FileStorage':
        name = ''
        state_id = ''

        @property
        def state(self):
            """
            Get the State Object of the current City Object
            """
            state_list = models.storage.all('State')
            city_state = None
            for key, value in state_list.items():
                if self.state_id == value.id:
                    city_state = value
            return city_state
