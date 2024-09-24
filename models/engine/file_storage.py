#!/usr/bin/python3
""" A class for file storage Engine."""
import json
from datetime import datetime


class FileStorage():
    """Serialize project instances to a JSON file and
        Deserialize JSON file to instances.

        Attributes:
            __file_path (string): Path to the JSON file [ex: file.json]
            __objects (dict): Empty but will store all live objects by
                              <class name>.id (ex:  to store a BaseModel object
                              with id=12121212, the key will be
                               BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects OR dict objects of
        specified class
        """
        if cls:
            from models.base_model import BaseModel
            from models.user import User
            from models.city import City
            from models.place import Place
            from models.state import State
            from models.amenity import Amenity
            from models.review import Review

            cls_dict = {
                'BaseModel': BaseModel,
                'User': User,
                'City': City,
                'Place': Place,
                'State': State,
                'Amenity': Amenity,
                'Review': Review
            }
            ret_dict = {}
            try:
                if type(cls) is not str:
                    cls = cls.__name__
                constructor = cls_dict[cls]
            except KeyError as e:
                print(e)
            else:
                for key in FileStorage.__objects:
                    if type(FileStorage.__objects[key]) is constructor:
                        ret_dict[key] = FileStorage.__objects[key]
            finally:
                return ret_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                new_dict = {}
                for key in FileStorage.__objects.keys():
                    new_dict[key] = FileStorage.__objects[key].to_dict()
                json.dump(new_dict, f)
        except IsADirectoryError:
            pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key in new_dict.keys():
                    kwargs = new_dict[key]
                    obj = self.create_obj(new_dict[key]['__class__'], **kwargs)
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, IsADirectoryError):
            pass

    def create_obj(self, class_name, **kwargs):
        """Re-load previously creeated object of a project
            from a JSON file.

            Args:
                class_name (str): The class of object to be reloaded
                kwargs (dict): The attribute dictionarry of the object
            Return:
                new_obj (obj): The newly  created object memory address
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'State': State,
            'Amenity': Amenity,
            'Review': Review
            }
        new_obj = class_dict[class_name](**kwargs)
        return new_obj

    def delete(self, obj=None):
        """
        Deletes an object from the live object list of the project
        Args:
            obj (object): Object to be deleted
        """
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """Deseraliaze the JSON file to python objects via reload()"""
        self.reload()
