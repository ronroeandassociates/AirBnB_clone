#!/usr/bin/python3
"""
hbnb terminal app
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    methods for the basic controls of the hbnb terminal app
    """
    prompt = '(hbnb)'

    def do_quit(self, *args):
        """
        use quit to exit the terminal
        """
        return True

    def do_EOF(self, *args):
        """
        use ctrl+d (EOF) to exit the terminal
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        creates an object of class BaseModel
        usage: create BaseModel
        """
        print(args)
        if args == 'BaseModel':
            new_model = BaseModel()
            print("{}".format(new_model.id))
        elif not args:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
