#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
            'place_amenity', Base.metadata,
            Column(
                'place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False
            ),
            Column(
                'amenity_id', String(60),
                ForeignKey('amenities.id'),
                primary_key=True, nullable=False
            )
        )


class Place(BaseModel, Base):
    """ A place to stay in the MySQL database.
        city_id (string)
        user_id (string)
        name (string)
        description (string)
        number_rooms (Integer)
        number_bathrooms(Integer)
        max_guest (Integer)
        price_by_night (Integer)
        latitude (Float)
        longitude (Float)
        reviews (relationship): The Place-Review relationship
        amenities (relationship): The Place-Amenity relationship.
        amenity_ids (list)

    """
    __tablename__ = 'places'
    # id = Column(String(60), primary_key=True, nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade="delete")
    # amenities = relationship(
            # 'Amenity', secondary="place_amenity",
            # backref='place_amenity', viewonly=False
            # )
    amenities = relationship(
            'Amenity', secondary="place_amenity",
            viewonly=False)
    # amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review
                instances with place_id equals to Place.id
            """
            from models import storage
            list_review = []
            for temp in storage.all(Review).values():
                if (self.id == temp.place_id):
                    list_review.append(temp)
            return temp

        @property
        def amenities(self):
            """getter attribute amenities that returns the list of Amenity
                instances based on the attribute amenity_ids that containes
                all Amenity.id linked to the Place.
            """
            from models import storage
            list_amenities = []
            for temp in storage.all(Amenity).values():
                if (temp.amenity_ids):
                    list_amenities.append(temp)
            return temp

        @amenities.setter
        def amenities(self, args):
            from models import storage
            for temp in storage.all(Amenity).values():
                if (temp.id == args):
                    temp.amenity_ids.append(args)
        # def amenities(self, args):
        #    if type(args) == Amenity:
        #        self.amenity_ids.append(args.id)
