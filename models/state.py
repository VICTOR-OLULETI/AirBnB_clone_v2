#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="delete")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter attribute cities for the file storage"""
            #or state_id = self.id
            from models import storage
            #list_city = storage.all(City)
            
            list_city = []
            for temp in list(storage.all(City).values()):
                if (self.id == temp.state_id ):
                    list_city.append(temp)
            # return self.cities
            #return [list_city, state_id]
            return list_city