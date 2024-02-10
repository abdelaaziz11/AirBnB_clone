#!/usr/bin/python3
"""console file"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
    def do_all(self, arg):
        """Prints all string representations of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = eval(arg)
                print([str(obj) for key, obj in objects.items() if key.split('.')[0] == arg])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        obj = storage.all()[key]
                        setattr(obj, args[2], eval(args[3]))
                        obj.save()
            except NameError:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (ctrl+D) to exit the program"""
        print("")
        return True

    def emptyline(self):
        """On empty line do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
