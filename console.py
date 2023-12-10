#!/usr/bin/python3
"""Define HBNBCommand that build -> command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """WELCOME TO MY CONSOLE"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit from command line interpreter"""
        quit()

    def do_EOF(self, arg):
        """End of file"""
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
