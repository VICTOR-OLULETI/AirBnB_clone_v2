#!/usr/bin/python3
"""
    This module defines the database Storage
"""
import os 
from models.base_model import Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


# get environment variables
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
HBNB_ENV = os.getenv('HBNB_ENV')

class DBStorage:
    """This class defines the attributes for the dbstorage
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB
            ),
            pool_pre_ping=True)
    # Base.metadata.create_all(self.__engine)
    if (HBNB_ENV == 'test'):
        Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        temp = {}
        if (cls is None):
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
        else:
            obj = self.__session.query(cls).all()
            
        for item in obj:
            key = type(item).__name__ + '.' + item.id
            temp.update({key: item})
        # print("\n\nThis is the")
        return temp
    
    def new(self, obj):
        """ Adds a new object to the current database
            session """
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete from the current database session"""
        if (obj is not None):
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=True)
        Session = scoped_session(session_factory)
        self.__session = Session()