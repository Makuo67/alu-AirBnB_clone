#!/usr/bin/python3
"""
Cmd console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Prompt command"""
    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Call quit command"""
        return True

    def do_EOF(self, line):
        """Exit if EOF occurs"""
        print()
        return True

    def emptyline(self):
        """Ignore empty line"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            # eval(line) will call class ex. if line is BaseModel
            #  eval(line)() = BaseModel()
            created = eval(line)()
            created.save()
            print(created.id)

    def do_show(self, line):
        """
        Shows the string representation of an instance based
        on the class name and id
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
            if key in tmp_dict:
                print(tmp_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
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
            if key in tmp_dict:
                del tmp_dict[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        line_list = line.split(" ")
        obj_list = []
        tmp_dict = FileStorage().all()
        if len(line) == 0:
            for obj in tmp_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif line_list[0] in self.class_list:
            for key, val in tmp_dict.items():
                if line_list[0] in key:
                    obj_list.append(str(val))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
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