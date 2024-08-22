#!/usr/bin/python3
"""The place module: It Holds the Place class of the Project."""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Define the Place class."""
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='places', viewonly=False)
    else:  # If Storage env is FileStorage
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Get a list of review instances that belong to the
            current place object/instance
            """
            review_inst = models.storage.all('Review')
            place_review = []
            for key in review_inst:
                if self.id == review_inst[key].place_id:
                    place_review.append(review_inst[key])
            return (place_review)

        @property
        def amenities(self):
            """
            Get a list of all amenity instance of this place
            """
            amenity_inst = models.storage.all('Amenity')
            place_amenity = []
            for key in amenity_inst:
                if amenity_inst[key].id in self.amenity_ids:
                    place_amenity.append(amenity_inst[key])
            return (place_amenity)

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
