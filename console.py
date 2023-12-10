#!/usr/bin/python3
"""Define HBNBCommand that build -> command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """WELCOME TO MY CONSOLE"""

    prompt = "(hbnb) "
    bnb_cls = {"BaseModel": BaseModel}

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
        args = self.parseline(line)
        cls_name = args[0]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.bnb_cls:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.bnb_cls[cls_name]()
            print(obj.id)
            storage.save()

    def do_show(self, line):
        args = self.parseline(line)
        cls_name = args[0]
        obj_id = args[1]
        if cls_name is None:
            print("")
        elif cls_name not in HBNBCommand.bnb_cls:
            print("")
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
