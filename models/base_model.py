#!/usr/bin/python3
"""This is a module that define a base model class of the project."""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel():
    """A basemodel for all the object of this project.
Attr:
id (str): The id of projects entire object
created_at (datetime): The date and time at which project objects are created
updated_at (datetime): The date and time at which project objects are modified
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Initialize the common attributes of this project's objet.
            Args:
                args (tuple): List of items....
                kwargs (dict): A dictionary to set as object attribute
        """
        if kwargs:
            if '__class__' in kwargs:
                self.__dict__ = kwargs.copy()
                del self.__dict__['__class__']
                updated_at = datetime.fromisoformat(kwargs['updated_at'])
                self.__dict__['updated_at'] = updated_at
                created_at = datetime.fromisoformat(kwargs['created_at'])
                self.__dict__['created_at'] = created_at
            else:
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                        if hasattr(self, key):
                            setattr(self, key, value)
                    if 'id' not in kwargs:
                        self.id = str(uuid.uuid4())
                    if 'created_at' not in kwargs:
                        self.created_at = datetime.now()
                    if 'created_at' in kwargs and 'updated_at' not in kwargs:
                        self.updated_at = self.created_at
                    else:
                        self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        if '_sa_instance_state' in self.__dict__:
            # _sa_instance_state: is a non-database-persisted value used by
            # SQLAlchemy internally
            # (it refers to the InstanceState for the instance.
            del self.__dict__['_sa_instance_state']
        attribute_dict = self.__dict__.copy()
        attribute_dict['created_at'] = attribute_dict['created_at'].isoformat()
        attribute_dict['updated_at'] = attribute_dict['updated_at'].isoformat()
        attribute_dict['__class__'] = type(self).__name__
        return (attribute_dict)

    def delete(self):
        """
        Delete the object from a list of live objects of the project
        """
        models.storage.delete(obj=self)

    def __str__(self):
        """Return a nice printable string representation of the object."""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))
