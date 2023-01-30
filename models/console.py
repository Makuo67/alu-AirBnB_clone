#!/usr/bin/python3

"""Script for the entry point of the command interpreter"""


import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage




class HBNBCommand(cmd.Cmd):
    """Command Interpreter for HBNB"""
    prompt = '(hbnb)'
    class_list = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]

    def do_quit(self,arg):
        """Quit the CLI prompt"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """Do nothing if empty line"""
        pass

    def help_quit(self):
        """Help for quit commands"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF commands"""
        print("EOF command to exit the program")

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""

        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        lists = line.split(" ")
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            tem_dict = FileStorage().all()
            key = f"{lists[0]}.{lists[1]}"
            if key in tem_dict:
                print(tem_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        lists = line.split(" ")
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            tem_dict = FileStorage().all()
            key = f"{lists[0]}.{lists[1]}"
            if key in tem_dict:
                del tem_dict[key]
                FileStorage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances based or not on the class name"""
        line_list = line.split(" ")
        obj_list = []
        tem_dict = FileStorage().all()
        if len(line) == 0:
            for objj in tem_dict.values():
                obj_list.append(str(objj))
            print(obj_list)
        elif line_list[0] in self.class_list:
            for key, value in tem_dict.items():
                if line_list[0] in key:
                    obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        line_list = line.split(" ")
        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            tmp_dict = FileStorage().all()
            key = f"{line_list[0]}.{line_list[1]}"
            if key not in tmp_dict:
                print("** no instance found **")
            elif len(line_list) == 2:
                print("** attribute name missing **")
            elif len(line_list) == 3:
                print("** value missing **")
            else:
                casting = type(eval(line_list[3]))
                arg_3 = line_list[3]
                arg_3 = arg_3.strip("'")
                arg_3 = arg_3.strip('"')
                setattr(tmp_dict.get(key), line_list[2], casting(arg_3))
                tmp_dict[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
