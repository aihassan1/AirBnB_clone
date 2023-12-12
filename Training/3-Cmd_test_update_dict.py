#!/usr/bin/python3
"""Define HBNBCommand that build -> command interpreter"""
from cmd import Cmd
from shlex import split
from datetime import datetime
import re


class HBNBCommand(Cmd):
    """WELCOME TO MY CONSOLE"""

    prompt = "(hbnb) "

    # up_d STANDS FOR ---> update_dict
    # line--->User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
    def do_x(self, line):
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
        cls_id = "#" + args[0] + "#" + args[2]

        for att, val in args[3].items():
            update_formate = cls_id + "#" + str(att) + "#" + '\"'+ str(val) +'\"'
            # You can see WooooOOOOOOOOOooooW Format here
            print(f"WOOOOW format: {update_formate}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
