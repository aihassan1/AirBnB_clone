#!/usr/bin/python3
"""Define HBNBCommand that build -> command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """WELCOME TO MY CONSOLE"""

    prompt = "(hbnb) "
    bnb_cls = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity}

    def do_quit(self, arg):
        """Quit from command line interpreter"""
        print(arg)
        quit()

    def do_EOF(self, arg):
        """End of file"""
        quit()

    def emptyline(self):
        """if empty line do nothing"""
        # Hello I am doing nothing
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        line = self.parseline(line)
        cls_name = line[0]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.bnb_cls:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.bnb_cls[cls_name]()
            print(obj.id)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
