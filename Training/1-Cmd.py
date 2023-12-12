from cmd import Cmd
from shlex import split

class my_console(Cmd):
    prompt = "### "

    def do_ok(self, line):
        # str
        print(type(line))
        # tuple
        print(type(self.parseline(line)))

        args = self.parseline(line)
        print(args)
        """
        arg1 = args[0]
        arg2 = args[1]
        arg3 = args[2]
        arg4 = args[3]
        print(arg1, arg2, arg3, arg4)
        """
        arg1 = args[0]
        arg2 = args[1]
        arg3 = args[2]
        print (arg1, arg2, arg3)

    def do_gg(self, line):
        args = split(line)
        print(type(args))
        print(args)
        arg1 = args[0]
        arg2 = args[1]
        print(arg1, arg2)


if __name__ == '__main__':
    my_console().cmdloop()
