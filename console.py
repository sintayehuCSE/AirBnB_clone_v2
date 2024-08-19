#!/usr/bin/python3
"""The entry point of the command interpreter for
    ABNB Clone project
"""
import cmd
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage

key_name = 'abcdefghijklmnopqrstuvwxyz_'
value_name = 'abcdefghijklmnopqrstuvwxyz_'

class HBNBCommand(cmd.Cmd):
    """ A simple framework for line-oriented command interpretor
        of Abnb Clone project
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Make the interpretor passive and do nothing
            on recieving emptly line + keyboard ENTER hit.
        """
        pass

    def do_quit(self, arg):
        """Qiuts the command interpretor session."""
        return True

    def do_EOF(self, arg):
        """Qiuts the command interpretor session."""
        print(arg)
        return True

    def do_create(self, arg):
        """Usage: create <Class Name> OR create <Class Name> <param 1> <param 2> <param 3>...
        Param syntax: <key name>=<value>
        
        Create a new class instance and print its id.
        """
        constructor, param = self.find_class(arg)
        if constructor:
            obj = constructor()
            print(obj.id)
        if constructor and param:
            param_dict = self.format_param(param)
            for key in param_dict:
                try:
                    if hasattr(obj, key):
                        try:
                            if os.getenv('HBNB_TYPE_STORAGE') == 'db':
                                obj.__dict__[key] = param_dict[key]
                            else:  # os.getenv('HBNB_TYPE_STORAGE') is 'FileStorage':
                                obj.__dict__[key] = type(getattr(obj, key))(param_dict[key])
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
        if constructor:
            obj.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        class_name, obj_id = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            obj = self.find_obj(class_name, obj_id)
            if obj:
                print(obj)

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        class_name, obj_id = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            obj = self.find_obj(class_name, obj_id)
            if obj:
                live_obj = storage.all()
                key = "{}.{}".format(class_name, obj_id)
                del live_obj[key]
                del obj
                storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        live_obj = storage.all()
        str_repr = []
        if arg:
            constructor = self.find_class(arg)
            if constructor:
                for key in live_obj.keys():
                    if type(live_obj[key]).__name__ == arg:
                        str_repr.append(str(live_obj[key]))
                print(str_repr)
        else:
            for key in live_obj.keys():
                str_repr.append(str(live_obj[key]))
            print(str_repr)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        class_name, obj_info = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            old_identchars = self.identchars
            self.identchars = self.identchars + '-"'
            obj_id, obj_attr = self.parse_arg(obj_info)
            obj_id = obj_id.strip('"')
            obj_attr = obj_attr.strip(' ')
            obj = self.find_obj(class_name, obj_id)
            if obj:
                attr_name, attr_value = self.parse_arg(obj_attr)
                attr_name = attr_name.strip('"')
                attr_value = attr_value.strip(' ')
                if not attr_name and obj_attr == '':
                    print("** attribute name missing **")
                elif not attr_value:
                    print("** value missing **")
                else:
                    self.identchars += '.'
                    if obj_attr[0] != '{':
                        attr_value, other_arg = self.parse_arg(attr_value)
                        attr_value = attr_value.strip('"')
                        cnst = (attr_name != 'id' and attr_name != 'created_at'
                               and attr_name != 'updated_at')
                        if cnst:
                            if hasattr(obj, attr_name):
                                try:
                                    attr_type = type(obj.__dict__[attr_name])
                                    setattr(obj, attr_name, attr_type(attr_value))
                                except KeyError:
                                    attr_type = type(type(obj).__dict__[attr_name])
                                    setattr(obj, attr_name, attr_type(attr_value))
                            else:
                                setattr(obj, attr_name, attr_value)
                            obj.save()
                        self.identchars = old_identchars
                    else:
                        if obj:
                            # Update by passed in dictionary.
                            obj_attr = obj_attr.replace("'", '"')
                            try:
                                with open("update_by_dict.json", 'w',
                                          encoding='utf-8') as f:
                                    f.write(obj_attr)
                                with open("update_by_dict.json", 'r',
                                          encoding='utf-8') as f:
                                    obj_attr = json.load(f)
                                for k in obj_attr.keys():
                                    if k not in ['id', 'created_at', 'updated_at']:
                                        if hasattr(obj, k):
                                            try:
                                                attr_type = type(obj.__dict__[k])
                                                setattr(obj, k,
                                                        attr_type(obj_attr[k]))
                                            except KeyError:
                                                attr_type = type(type(obj).__dict__[k])
                                                setattr(obj, k,
                                                        attr_type(obj_attr[k]))
                                        else:
                                            setattr(obj, k, obj_attr[k])
                                obj.save()
                                os.remove("update_by_dict.json")
                            except (Exception) as e:
                                print(e)

    def do_User(self, arg):
        """Print List of all instances of User class. OR thier count"""
        self.class_command("User", arg)

    def do_BaseModel(self, arg):
        """Print List of all instances of BaseModel class. OR thier count"""
        self.class_command("BaseModel", arg)

    def do_Place(self, arg):
        """Print List of all instances of Place class. OR thier count"""
        self.class_command("Place", arg)

    def do_State(self, arg):
        """Print List of all instances of State class. OR thier count"""
        self.class_command("State", arg)

    def do_City(self, arg):
        """Print List of all instances of City class. OR thier count"""
        self.class_command("City", arg)

    def do_Amenity(self, arg):
        """Print List of all instances of Amenity class. OR thier count"""
        self.class_command("Amenity", arg)

    def do_Review(self, arg):
        """Print List of all instances of Review class. OR thier count"""
        self.class_command("Review", arg)

    def find_class(self, arg):
        """Check if a specified class name is valid
            Args:
                arg (str): User-input class-name
            Return:
                1. Requested Class constructor if arg is valid class-name OR
                2. None if arg is not valid class-name.
        """
        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'State': State,
            'Amenity': Amenity,
            'Review': Review
        }
        if not arg:
            print("** class name missing **")
            return (None, None)
        try:
            class_name, param = self.parse_arg(arg)
            return (class_dict[class_name], param)
        except KeyError:
            print("** class doesn't exist **")
            return (None, None)

    def parse_arg(self, arg):
        """Parse the input argument to the command of HBNB interpretor
            Divide the argument into two parts.
            Args:
                arg (str): The input argument to the HBNB interpretor
                command OR its fragment.
            Return:
                (first_arg, second_arg) (tuple): Return tuple of argument
                recieved from input or its fragment after successive call.
        """
        i, n = 0, len(arg)
        while (i < n and arg[i] in self.identchars):
            if arg[i] == '"':
                i = i + 1
                while arg[i] != '"':
                    i = i + 1
                else:
                    i = i + 1
                    break
            else:
                i = i + 1
        first_arg, second_arg = arg[:i], arg[i + 1:]
        return first_arg, second_arg

    def find_obj(self, class_name, obj_id):
        """Check if object with the specified ID is a live object.
            Args:
                class_name (str): The class of the object
                obj_id (str): The object ID
            Return:
                The live object OR None
        """
        live_obj = storage.all()

        if not obj_id:
            print("** instance id missing **")
            return None
        try:
            key = "{}.{}".format(class_name, obj_id)
            return live_obj[key]
        except KeyError:
            print("** no instance found **")
            return None

    def count(self, class_name):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        count = 0
        live_obj = storage.all()
        constructor = self.find_class(class_name)
        if constructor:
            for key in live_obj.keys():
                if type(live_obj[key]) is constructor:
                    count += 1
            print(count)

    def class_command(self, class_name, arg):
        """Perform the requested class command."""
        if arg == ".all()":
            self.do_all(class_name)
        elif arg == '.count()':
            self.count(class_name)
        elif arg.startswith(".show(") and arg.endswith(")"):
            obj_id = arg[6:].lstrip('"')
            self.do_show(class_name + " " + obj_id.rstrip('")'))
        elif arg.startswith(".destroy(") and arg.endswith(")"):
            obj_id = arg[9:].lstrip('("')
            self.do_destroy(class_name + " " + obj_id.rstrip('")'))
        elif arg.startswith(".update(") and arg.endswith(")"):
            arg_format = arg[8:].rstrip(')')
            self.do_update(class_name + " " + arg_format)
        else:
            print("*** Unknown syntax: {}{}".format(class_name, arg))
    
    def format_param(self, param):
        """
            Formats the input key-value pairs in to a dictionary attribute
            Args:
                param (str): The key-value input parameters as oject attribute
        """
        att_dict = {}
        while param:
            key = param[:param.find('=')].strip(' ')
            param = param[len(key) + 1:].strip(' ')
            if ' ' in param:
                value = param[:param.find(' ')].strip(' ')
                param = param[param.find(' ') + 1:].strip(' ')
            else:
                value = param
                param = ''
            value = value.strip('"')
            valid_key = self.check_key_validity(key)
            value = value.replace('_', ' ', len(value))
            if valid_key:
                att_dict[key] = value
            else:
                return {}
        return att_dict
    
    def check_key_validity(self, key):
        """
            Check that key name conforms to conventional attribute name of python3
            Args:
                key (str): The key to be checked
            Returns:
                1 if key is valid attribute name else 0
        """
        res = 1
        for i in range(len(key)):
            if key[i] not in key_name:
                res = 0
                break
        return res



if __name__ == "__main__":
    HBNBCommand().cmdloop()
