from cmd import Cmd
from shlex import split

class my_console(Cmd):
    prompt = "### "

    def do_ok(self, line):
        print(type(line)) # str
        print(type(self.parseline(line))) # tuple

        args = self.parseline(line)
        """
        parse input intor 3 elements stored in tuple
        """
        print(args) # print tuple
        print(f"(Command): {args[0]}\n(Remainder): {args[1]}\n(Input): {args[2]}")

    def do_gg(self, line):
        args = split(line)
        print(type(args))
        print(args)
        arg1 = args[0]
        arg2 = args[1]
        print(arg1, arg2)


if __name__ == '__main__':
    my_console().cmdloop()
