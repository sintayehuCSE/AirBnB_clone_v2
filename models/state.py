#!/usr/bin/python3
"""The State Module: Defines State class of the Project."""
from models.base_model import BaseModel, Base, storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """Desfine the State class."""
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
    else:  # getenv('HBNB_TYPE_STORAGE') is 'FileStorage':
        name = ''

        @property
        def cities(self):
            """
            This a getter property for FileStorage STORAGE type
            Returns:
            list of City instances with state_id equals to the current State.id

            => It will be the FileStorage relationship between State and City
            """
            city_list = storage.all(cls='City')
            state_city = []
            try:
                for key in city_list:
                    if city_list[key].state_id == self.id:
                        state_city.append(city_list[key])
            except AttributeError:
                pass
            finally:
                return (state_city)
