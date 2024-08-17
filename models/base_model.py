#!/usr/bin/python3
"""This is a module that define a base model class of the project."""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """A basemodel for all the object of this project."""
    def __init__(self, *args, **kwargs):
        """ Initialize the common attributes of this project's objet.
            Args:
                args (tuple): List of items....
                kwargs (dict): A dictionary to set as object attribute
        """
        if kwargs:
            self.__dict__ = kwargs.copy()
            del self.__dict__['__class__']
            updated_at = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__['updated_at'] = updated_at
            created_at = datetime.fromisoformat(kwargs['created_at'])
            self.__dict__['created_at'] = created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())
            storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        attribute_dict = self.__dict__.copy()
        attribute_dict['created_at'] = attribute_dict['created_at'].isoformat()
        attribute_dict['updated_at'] = attribute_dict['updated_at'].isoformat()
        attribute_dict['__class__'] = type(self).__name__
        return (attribute_dict)

    def __str__(self):
        """Return a nice printable string representation of the object."""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))
