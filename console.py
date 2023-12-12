#!/usr/bin/python3
"""Define HBNBCommand that build -> command interpreter"""
from cmd import Cmd
from shlex import split
from datetime import datetime
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models import storage
from models.base_model import BaseModel
from models.place import Place


class HBNBCommand(Cmd):
    """WELCOME TO MY CONSOLE"""

    prompt = "(hbnb) "
    bnb_cls = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "State": State,
        "City": City,
        "Review": Review,
        "Place": Place
    }

    def default(self, line):
        """Default function"""
        methods = {
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "count": self.do_count
            }
        flag = line.find('{')
        if flag != -1:
            self.update_dict(line)

        pieces = re.split(r'[.(,) ]', line)
        arg_list = pieces[2:-1]
        NewLine = ""
        for arg in arg_list:
            if arg == "":
                NewLine = NewLine + " "
            else:
                NewLine = NewLine + arg
        if NewLine == " ":
            NewLine = pieces[0]
        else:
            NewLine = pieces[0] + " " + NewLine
        fun_name = pieces[1]
        Cmd_fun = methods[fun_name]
        Cmd_fun(NewLine)

    def do_quit(self, arg):
        """Quit from command line interpreter"""
        quit()

    def do_EOF(self, arg):
        """End of file"""
        quit()

    def emptyline(self):
        """if empty line do nothing"""
        # Hello I am doing nothing
        pass

    # Complete
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

    # Complete
    def do_show(self, line):
        """
            Prints the string representation
            of an instance based on the class name and id.
        """
        args = self.parseline(line)
        cls_name = args[0]
        inst_id = args[1]

        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.bnb_cls:
            print("** class doesn't exist **")
        elif inst_id is None or inst_id == "":
            print("** instance id missing **")
        else:
            inst_key = f"{cls_name}.{inst_id}"
            obj = storage.all().get(inst_key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    # Complete
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = self.parseline(line)
        cls_name = args[0]
        inst_id = args[1]

        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.bnb_cls:
            print("** class doesn't exist **")
        elif inst_id is None or inst_id == "":
            print("** instance id missing **")
        else:
            inst_key = f"{cls_name}.{inst_id}"
            obj = storage.all().get(inst_key)
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[inst_key]
                storage.save()

    # Complete
    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        args = self.parseline(line)
        cls_name = args[0]
        str_inst = []

        if cls_name is None:
            for K, ob in storage.all().items():
                str_inst.append(ob.__str__())
            return print(str_inst)
        elif cls_name not in HBNBCommand.bnb_cls:
            return print("** class doesn't exist **")
        else:
            for K, ob in storage.all().items():
                if K.startswith(cls_name):
                    str_inst.append(ob.__str__())
            print(str_inst)

    def do_count(self, line):
        """retrieve the number of instances of a class"""
        objects = storage.all().values()
        n = 0
        for value in objects:
            if value.__class__.__name__ == line:
                n = n + 1
        print(n)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = split(line)
        # args[0] = class name
        # args[1] = id
        # args[2] = Attribute
        # args[3] = new value
        N_args = len(args)

        if N_args == 0:
            print("** class name missing **")
        if args[0] not in HBNBCommand.bnb_cls:
            print("** class doesn't exist **")
        elif N_args < 2:
            print("** instance id missing **")
        else:
            inst_key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(inst_key)

            if obj is None:
                print("** no instance found **")
            elif N_args < 3:
                print("** attribute name missing **")
            elif N_args < 4:
                print("** value missing **")
            else:
                setattr(obj, args[2], args[3])
                storage.save()

    # THE GOAL IS 
    ### CONVERT FORMAT FROM <<CLASS.FUNCTION(ID, DICT)
    ### TO do_update() FORMAT <<CLASS ID SINGLE_ATT SINGLE_VALUE
    def update_dict(self, line):
        """convert line to do_update form"""
        args = re.split(r"[.()]", line)

        # Extract pure dictionary from list
        start = args[2].find('{')
        end = args[2].find('}') + 1
        args[3] = args[2][start: end]
        args[3] = dict(eval(args[3]))

        # Extract pure id from args
        start = args[2].find('"') + 1
        end = args[2][1:].find('"')
        args[2] = args[2][start: end]

        #FUNCTION CLASS ID
        cls_id = args[0] + " " + args[2] + " "

        for att, val in args[3].items():
            update_formate = cls_id + str(att) + " " + str(val)
            # You can see WooooOOOOOOOOOooooW Format here
            # print(f"WOOOOW format: {update_formate}")
            self.do_update(update_formate)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
