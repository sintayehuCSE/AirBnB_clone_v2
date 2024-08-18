#!/usr/bin/python3
"""
This module contain a class that define database storage for the project
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User

class_dict = {
    'State': State,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'Review': Review,
    'User': User
}


class DBStorage():
    """
    Interface to the database storage of the project
    Attributes:
        __engine: The SQLAlchemy engine
        __session: The SQLALchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        create and initialize DBStorage object
        And drop all tables if running environment is test environment
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return a dictionary of objects of the specified class OR
        a dictionary of entire objects of the project
        """
        session = self.__session
        ret_dict = {}
        if cls:
            if type(cls) is not str:  # To check for valid class name
                cls = cls.__name__
            if cls in class_dict:
                cls = class_dict[cls]
                qry = session.query(cls).all()
                for inst in qry:
                    key = '{}.{}'.format(type(inst).__name__, inst.id)
                    ret_dict[key] = inst
            return (ret_dict)

        for key, table in class_dict.items():
            qry = session.query(table).all()
            for inst in qry:
                key = '{}.{}'.format(type(inst).__name__, inst.id)
                ret_dict[key] = inst
        return (ret_dict)

    def new(self, obj):
        """
        Add new object to the cureent database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy) and
        create the current database session (self.__session) from the
        engine (self.__engine) by using a sessionmaker

        The created session is scoped_session for making thread-safe Session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
