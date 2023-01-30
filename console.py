#!/usr/bin/python3
/*
Title:AirBnB Clone
Author: kelly villa
Date:feb 2020
Availaility:https://github.com/02KellyV/AirBnB_clone/blob/master/console.py */
""" Entry points for a command interpreter """

import cmd
import models
from models.user import user
from models.base_model import BaseModel
from model.place import place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
import Shlex

classes_dict= {"Amenity": Amenity, "BaseModel":BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """
    commnand interpreter entry point
    """
    collection_keys = classes_dict.keys()
    prompt = '(hbnb)'

    def do_EOF(self, _input):
        """ exiting the cmd console"""
        return True

    def do_quit(self, _input):
        """exit command"""
        return True

    def emptyline(self):
        """empty line"""
        return False

    def do_create(self, _input_class_name):
        """creates a bew instance of BaseModel and saves in JSON"""
          if not _input_class_name:
            print("** class name missing **")
            return
        if _input_class_name not in classes_dict.keys():
            print("** class doesn't exist **")
            return
        newinstance = classes_dict[_input_class_name]()
        newinstance.save()
        print(newinstance.id

    def do_show(self, _input):
        """ prints the string rep of an instance according to class name and id"""
        input_2 = _input
        if len(input2.split(' ')[0] is 0:
            print("** class name missing **")
            return
        if input2.split(' ')[0] not in self.collection_keys:
           print("** class doesn't exit **")
           return
        if len(input2.split()) is 1:
           print("** instance id missing **")
           return
        models.storage.reload()
        for key, value in models.storage.all().items():
            if value.__class__.__name__== input2.split(' ')[0] \ and value.id == input2.split(' ')[1]:
            print(value.__str__())
            return
        print("** no instance found **")

    def do_destroy(self, _input):
    """ deletes an instance according to class name and id """
    if len(_input.split(' ')[0] is 0:
        print("** class name missing **")
        return
    if _input.split(' ')[0] not in self.collection_keys:
        print("** class doesn't exist **")
        return
    if len(_input.split(' ')) is 1:
       print("** instance id missing **")
       return
       class_name, class_id = (_input.split(' ')[0], _input.split(' ')[1])
        query_key = class_name + '.' + class_id
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()[query_key]
        models.storage.save()

    def do_all(self, _input_class):
        """Prints all string repr of all instances
            based or not on the class name
        """

        if _input_class:
            if _input_class not in self.collection_keys:
                print("** class doesn't exist **")
                return

        for key_items in models.storage.all().keys():
            key_items = models.storage.all()[key_items]
            print(key_items)
        return

    def do_update(self, _input):
        """Updates an instance based on the class name and id by adding
           or updating attribute and saves the change into the JSON file
        """
        _input = shlex.split(_input)
        query_key = ''

        if len(_input) is 0:
            print("** class name missing **")
            return
        if _input[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return
        if len(_input) is 1:
            print("** instance id missing **")
            return
        if len(_input) > 1:
            query_key = _input[0] + '.' + _input[1]
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(_input) is 2:
            print('** attribute name missing **')
            return
        if len(_input) is 3:
            print('** value missing **')
            return
        key_name = _input[2]
        input_value = _input[3]
        setattr(models.storage.all()[query_key], key_name, input_value)

        models.storage.all()[query_key].save()

    def default(self, inp):
        """Retrieve all instances class using: <class name>.all()"""
        count = 0
        words = inp.split(".")

        if words[0] in classes_dict and words[1] == "all()":
            self.do_all(words[0])
        elif words[0] in classes_dict and words[1] == "count()":
            if (words[0] not in classes_dict):
                print("** class doesn't exist **")
                return (False)
            else:
                for key in models.storage.all():
                    if key.startswith(words[0]):
                        count += 1
                print(count)
        else:
            print("*** Unknown syntax: {}".format(inp))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
