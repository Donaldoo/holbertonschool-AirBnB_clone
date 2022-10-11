#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    classDict = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, arg):
        """Quit command to return quit program function"""
        return True

    def do_EOF(self, arg):
        """EOF command to return exit program function"""
        return True

    def emptyline(self):
        """Empty line handeler"""
        return False

    def do_create(self, arg):
        """create a new intance of basemodel"""
        args = arg.split()
        if args[0] in self.classDict:
            newEl = self.classDict.get(args[0])()
            storage.save()
            print(newEl.id)
        else:
            print("** class doesn't exist **")
        if len(args) == 0:
            return "** class name missing **"

if __name__ == '__main__':
    HBNBCommand().cmdloop()
