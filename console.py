#!/usr/bin/python3
"""console file"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, arg):
        """to exit the program"""
        print("")
        return True

    def emptyline(self):
        """do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
